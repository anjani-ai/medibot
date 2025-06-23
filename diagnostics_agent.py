from google.adk.agents import LlmAgent
from google.adk.tools import FunctionTool

def diagnostics_logic(intake_data: dict):
    # In a real system, call Gemini or another LLM here
    # Here, we mock the output for the sample input
    if "sore throat" in intake_data.get("symptoms", []) and "fever" in intake_data.get("symptoms", []):
        possible_conditions = "Viral pharyngitis, Influenza"
    else:
        possible_conditions = "Unknown"
    disclaimer = "This is not a diagnosis. For informational purposes only."
    return {"possible_conditions": possible_conditions, "disclaimer": disclaimer}

diagnostics_tool = FunctionTool(diagnostics_logic)

class DiagnosticsAgent(LlmAgent):
    def __init__(self):
        super().__init__(
            name="DiagnosticsAgent",
            model="gemini-1.5-flash",
            tools=[diagnostics_tool]
        )
    def run(self, intake_data: dict):
        return diagnostics_logic(intake_data)

if __name__ == "__main__":
    agent = DiagnosticsAgent()
    sample = {
        "age": 34,
        "symptoms": ["sore throat", "fever", "tired"],
        "duration": "3 days",
        "medical_history": ["asthma"]
    }
    print(agent.run(sample)) 