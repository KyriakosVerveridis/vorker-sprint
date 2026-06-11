# Vorker Compliance Agent

An AI Agent specialized in Swedish business law, designed to bridge the "Compliance Gap" for Small and Medium Enterprises (SMEs).

## Architecture (The Architect)
- **Model:** Google Gemini (via API)
- **RAG Implementation:** Grounded in official documentation from Skatteverket, Bolagsverket, and verksamt.se.
- **Grounding:** The agent responds exclusively based on the files provided in the `/data` directory to ensure high-fidelity accuracy.

## Strategy (The Strategist)
- **Value Proposition:** Mitigates legal and fiscal risks for Swedish entrepreneurs by providing grounded, actionable advice.
- **Target Audience:** Swedish startups and SMEs navigating complex local regulations.
- **Monetization:** SaaS subscription model with tiered access.

## Installation
1. `pip install -r requirements.txt`
2. Add your API key to a `.env` file.
3. Start the Agent's web interface:
   `adk web --port 8000`
4. Open your browser and navigate to `http://localhost:8000` to interact with the agent.

## Compliance Note
The system relies strictly on official authoritative sources. In cases of ambiguity, the agent is instructed to direct the user to verksamt.se for official guidance.