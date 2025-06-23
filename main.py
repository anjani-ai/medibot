print("[DEBUG] agent-starter-pack/main.py is executing.")
# NOTE: Use absolute imports for ADK package structure
from agent_starter_pack.my_agents.intake_agent import IntakeAgent
from agent_starter_pack.my_agents.triage_agent import TriageAgent
from agent_starter_pack.my_agents.diagnostics_agent import DiagnosticsAgent
from agent_starter_pack.my_agents.report_agent import ReportAgent

SAMPLE_INPUT = "Hi, I'm 34. I've had a sore throat and fever for 3 days, and I have asthma. I've been feeling tired too."

def main():
    print("=== MediBot AI Pipeline ===")
    # Intake
    intake_agent = IntakeAgent()
    intake_result = intake_agent.run(SAMPLE_INPUT)
    print("\n[IntakeAgent Output]")
    print(intake_result)
    # Triage
    triage_agent = TriageAgent()
    triage_result = triage_agent.run(intake_result)
    print("\n[TriageAgent Output]")
    print(triage_result)
    # Diagnostics
    diagnostics_agent = DiagnosticsAgent()
    diagnostics_result = diagnostics_agent.run(intake_result)
    print("\n[DiagnosticsAgent Output]")
    print(diagnostics_result)
    # Report
    report_agent = ReportAgent()
    report_result = report_agent.run(intake_result, triage_result, diagnostics_result)
    print("\n[ReportAgent Output]")
    print(report_result)
    print("\n=== End of Pipeline ===")

if __name__ == "__main__":
    main() 