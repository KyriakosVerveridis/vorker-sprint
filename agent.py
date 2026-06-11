from google.adk.agents.llm_agent import Agent
import os

# Tool to read Swedish legal documents from the local 'data' directory
def read_law(topic: str) -> str:
    """Reads Swedish compliance documents from the data folder."""
    try:
        # Construct the file path using the topic name
        file_path = os.path.join("data", f"{topic}.txt")
        
        # Check if the file exists before attempting to read
        if not os.path.exists(file_path):
            return f"Information about {topic} could not be found."
            
        # Open and return the content of the file
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        # Return error message if file reading fails
        return f"Error reading document: {str(e)}"

# System prompt defining the agent's behavior and constraints
SYSTEM_PROMPT = """
You are a Swedish compliance expert. 
1. Use the 'read_law' tool to fetch information from the 'data' folder. 
2. Always rely on the provided documents for your answers. 
3. If information is missing, direct the user to official sources like verksamt.se.
4. Maintain a professional and concise tone.
"""

# Initialize the agent with the defined configuration
root_agent = Agent(
    model='gemini-flash-latest',
    name='swedish_compliance_agent',
    description="Provides expert advice on Swedish corporate and tax law.",
    instruction=SYSTEM_PROMPT,
    tools=[read_law],
)