# MediBot AI – Multi-Agent Medical Workflow Assistant

## Overview
MediBot AI automates the medical intake-to-summary process in clinics using Google Cloud's Agent Development Kit (ADK) and Gemini via Vertex AI. It features a multi-agent pipeline for extracting, triaging, reasoning, and summarizing patient information, deployable on Google Cloud Run.

## Features
- **IntakeAgent**: Extracts symptoms, duration, and history from natural language
- **TriageAgent**: Assigns urgency levels based on symptoms/comorbidities
- **DiagnosticsAgent**: Suggests likely conditions (not a diagnosis)
- **ReportAgent**: Aggregates and formats a medical summary
- **BigQuery Logging**: Logs intake events for analytics

## Project Structure
```
agent-starter-pack/
├── my_agents/
│   ├── intake_agent.py
│   ├── triage_agent.py
│   ├── diagnostics_agent.py
│   └── report_agent.py
├── main.py
├── agent.yaml
├── requirements.txt
├── README.md
```

## Setup
1. **Clone the repo**
   ```sh
   git clone <your-repo-url>
   cd agent-starter-pack
   ```
2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
3. **Configure GCP credentials**
   - Set up a service account with Vertex AI and BigQuery permissions
   - Export credentials:
     ```sh
     export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/credentials.json"
     ```
4. **Edit `agent.yaml`** as needed for your environment

## Running Locally
```sh
python main.py
```

## Deploying to Cloud Run
1. **Build and deploy**
   ```sh
   gcloud builds submit --tag gcr.io/<PROJECT-ID>/medibot
   gcloud run deploy medibot \
     --image gcr.io/<PROJECT-ID>/medibot \
     --platform managed \
     --region <REGION> \
     --allow-unauthenticated
   ```
2. **Set environment variables** in Cloud Run for credentials if needed

## Sample Input
```
Hi, I'm 34. I've had a sore throat and fever for 3 days, and I have asthma. I've been feeling tired too.
```

## Sample Output
See `main.py` for a full pipeline run and agent outputs.

## Hackathon Notes
- Built for the [Google Cloud Multi-Agent Hackathon](https://googlecloudmultiagents.devpost.com/)
- Uses only ADK-compliant agents and GCP tools

---
**Disclaimer:** MediBot AI is for workflow automation and not for diagnosis or treatment decisions. 