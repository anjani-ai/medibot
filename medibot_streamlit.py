import streamlit as st
from agent_starter_pack.my_agents.intake_agent import IntakeAgent
from agent_starter_pack.my_agents.triage_agent import TriageAgent
from agent_starter_pack.my_agents.diagnostics_agent import DiagnosticsAgent
from agent_starter_pack.my_agents.report_agent import ReportAgent
import os

st.set_page_config(page_title="MediBot AI – Medical Intake Assistant", page_icon="🩺", layout="centered")
st.markdown("""
<style>
    .main {background-color: #181c20;}
    .stButton>button {background-color: #1976d2; color: white; font-weight: bold;}
    .stDownloadButton>button {background-color: #43a047; color: white; font-weight: bold;}
    div[data-testid="stTextArea"] textarea {
        background-color: #181c20 !important;
        color: #fff !important;
        font-size: 1.1em !important;
        border: 1.5px solid #1976d2 !important;
        caret-color: #fff !important;
    }
    div[data-testid="stTextArea"] label {
        color: #1976d2 !important;
        font-weight: bold;
    }
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.image("https://storage.googleapis.com/gweb-cloudblog-publish/images/Google_Cloud_Logo.max-2800x2800.png", width=80)
st.title("🏥 MediBot AI – Medical Intake Assistant")
st.markdown("<span style='color:#1976d2;font-size:1.2em;'>Automate the medical intake-to-summary process with Google ADK agents.</span>", unsafe_allow_html=True)

with st.expander("ℹ️ About this demo", expanded=False):
    st.write("""
    **MediBot** is a multi-agent AI workflow for clinics, built with Google Cloud's Agent Development Kit (ADK) and Gemini. Enter patient intake text or upload a file to see the full pipeline in action!
    """)

with st.form("intake_form"):
    col1, col2 = st.columns([2,1])
    with col1:
        patient_input = st.text_area(
            "Enter patient intake text:",
            "Hi, I'm 34. I've had a sore throat and fever for 3 days, and I have asthma. I've been feeling tired too.",
            height=120
        )
    with col2:
        uploaded_file = st.file_uploader("or upload a .txt file", type=["txt"])
    submitted = st.form_submit_button("Run MediBot Pipeline 🩺")

if submitted:
    if uploaded_file is not None:
        patient_input = uploaded_file.read().decode("utf-8")
    st.markdown("---")
    with st.spinner("Extracting intake info..."):
        intake_agent = IntakeAgent()
        intake_result = intake_agent.run(patient_input)
    with st.container():
        st.markdown("#### 📝 IntakeAgent Output")
        st.json(intake_result)

    with st.spinner("Triage in progress..."):
        triage_agent = TriageAgent()
        triage_result = triage_agent.run(intake_result)
    with st.container():
        st.markdown("#### 🚦 TriageAgent Output")
        st.json(triage_result)

    with st.spinner("Diagnostics in progress..."):
        diagnostics_agent = DiagnosticsAgent()
        diagnostics_result = diagnostics_agent.run(intake_result)
    with st.container():
        st.markdown("#### 🧠 DiagnosticsAgent Output")
        st.json(diagnostics_result)

    with st.spinner("Generating report and PDF..."):
        report_agent = ReportAgent()
        report_result = report_agent.run(intake_result, triage_result, diagnostics_result)
    with st.container():
        st.markdown("#### 📄 ReportAgent Output")
        st.markdown("### Medical Summary (Markdown)")
        st.markdown(report_result["markdown"])
        # PDF download
        if os.path.exists(report_result["pdf_path"]):
            with open(report_result["pdf_path"], "rb") as pdf_file:
                st.download_button(
                    label="⬇️ Download PDF report",
                    data=pdf_file,
                    file_name="medibot_report.pdf",
                    mime="application/pdf"
                )
        else:
            st.warning("PDF not found.")

st.markdown("---")
st.markdown("<div style='text-align:center;font-size:0.9em;color:#888;'>Built for the <a href='https://googlecloudmultiagents.devpost.com/' target='_blank'>Google Cloud Multi-Agent Hackathon</a> | Powered by <b>Google ADK</b> & <b>Gemini</b></div>", unsafe_allow_html=True) 