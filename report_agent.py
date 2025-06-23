from google.adk.agents import LlmAgent
from google.adk.tools import FunctionTool
from fpdf import FPDF
import os
import tempfile

def report_logic(intake, triage, diagnostics):
    markdown = f"""
## Patient Info
- Age: {intake.get('age')}
- Medical History: {', '.join(intake.get('medical_history', []))}

## Symptoms
- {', '.join(intake.get('symptoms', []))}
- Duration: {intake.get('duration')}

## Triage
- Urgency: {triage.get('urgency')}
- Rationale: {' '.join(triage.get('rationale', []))}

## Possible Conditions
- {diagnostics.get('possible_conditions')}

> {diagnostics.get('disclaimer')}
"""
    # Generate PDF using fpdf2
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in markdown.split('\n'):
        pdf.cell(0, 10, line, ln=1)
    # Save to a temp file
    temp_dir = tempfile.gettempdir()
    pdf_path = os.path.join(temp_dir, "medibot_report.pdf")
    pdf.output(pdf_path)
    return {"markdown": markdown, "pdf_path": pdf_path}

report_tool = FunctionTool(report_logic)

class ReportAgent(LlmAgent):
    def __init__(self):
        super().__init__(
            name="ReportAgent",
            model="gemini-1.5-flash",
            tools=[report_tool]
        )
    def run(self, intake, triage, diagnostics):
        return report_logic(intake, triage, diagnostics)

if __name__ == "__main__":
    agent = ReportAgent()
    intake = {"age": 34, "symptoms": ["sore throat", "fever", "tired"], "duration": "3 days", "medical_history": ["asthma"]}
    triage = {"urgency": "priority", "rationale": ["Relevant comorbidity present."]}
    diagnostics = {"possible_conditions": "Viral pharyngitis, Influenza", "disclaimer": "This is not a diagnosis. For informational purposes only."}
    print(agent.run(intake, triage, diagnostics)) 