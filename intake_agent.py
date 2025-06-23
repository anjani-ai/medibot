from google.adk.agents import LlmAgent
from google.adk.tools import FunctionTool

# Example extraction logic (replace with LLM or regex as needed)
def extract_intake_info(text: str):
    # In a real system, call an LLM or use regex for extraction
    # Here, we mock the output for the sample input
    if "sore throat" in text and "fever" in text:
        return {
            "age": 34,
            "symptoms": ["sore throat", "fever", "tired"],
            "duration": "3 days",
            "medical_history": ["asthma"]
        }
    return {}

extract_tool = FunctionTool(extract_intake_info)

class IntakeAgent(LlmAgent):
    def __init__(self):
        super().__init__(
            name="IntakeAgent",
            model="gemini-1.5-flash",
            tools=[extract_tool]
        )
    def run(self, patient_input: str):
        return extract_intake_info(patient_input)

if __name__ == "__main__":
    agent = IntakeAgent()
    sample = "Hi, I'm 34. I've had a sore throat and fever for 3 days, and I have asthma. I've been feeling tired too."
    print(agent.run(sample)) 