from pydantic_ai import Agent
from dotenv import load_dotenv
import os

load_dotenv()
agent_model = os.environ[('GROQ_AGENT_LLM')]

triage_agent = Agent(agent_model)

print(triage_agent.run_sync("Hi."))