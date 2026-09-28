from pydantic_ai import Agent
from dotenv import load_dotenv
import os

load_dotenv()
agent_model = os.environ[('GROQ_AGENT_LLM')]

triage_agent = Agent(os.environ[('GROQ_API_KEY')], model=os.environ[('GROQ_AGENT_LLM')])

print(triage_agent)