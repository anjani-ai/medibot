from google.adk.agents import LlmAgent
from google.adk.tools import FunctionTool

def triage_logic(intake_data: dict):
    symptoms = [s.lower() for s in intake_data.get("symptoms", [])]
    history = [h.lower() for h in intake_data.get("medical_history", [])]
    urgent_symptoms = {"chest pain", "shortness of breath", "severe headache"}
    comorbidities = {"asthma", "diabetes", "heart disease"}
    urgency = "routine"
    rationale = []
    if any(s in urgent_symptoms for s in symptoms):
        urgency = "urgent"
        rationale.append("Urgent symptom present.")
    elif any(h in comorbidities for h in history):
        urgency = "priority"
        rationale.append("Relevant comorbidity present.")
    elif "fever" in symptoms and "sore throat" in symptoms and intake_data.get("duration", "").startswith("3"):
        urgency = "priority"
        rationale.append("Fever and sore throat for 3+ days.")
    else:
        rationale.append("No urgent symptoms or comorbidities.")
    return {"urgency": urgency, "rationale": rationale}

triage_tool = FunctionTool(triage_logic)

class TriageAgent(LlmAgent):
    def __init__(self):
        super().__init__(
            name="TriageAgent",
            model="gemini-1.5-flash",
            tools=[triage_tool]
        )
    def run(self, intake_data: dict):
        return triage_logic(intake_data)

if __name__ == "__main__":
    agent = TriageAgent()
    sample = {
        "age": 34,
        "symptoms": ["sore throat", "fever", "tired"],
        "duration": "3 days",
        "medical_history": ["asthma"]
    }
    print(agent.run(sample)) 