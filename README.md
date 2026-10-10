# Work Request Triage Agent

A simple agentic AI project that turns unstructured work requests into either a focused clarification request or a structured, prioritized work plan.

The project demonstrates how an AI agent can **reason about a request, identify missing information, make a decision, and choose the next step** instead of immediately generating recommendations.

## Project Goal

Work requests are often vague or incomplete. For example:

> "We need to improve the onboarding process before next month."

Before creating a plan, the agent checks whether it understands the goal and has enough important information. If essential details are missing, it asks focused clarification questions. If there is enough information, it creates an actionable plan.

This is intentionally a **single-agent, no-tool project**. Its main focus is decision-making rather than external integrations.

## Key Features

- Understands a user's work request.
- Extracts the goal, deadline, stakeholders, constraints, and expected deliverables when provided.
- Identifies missing or contradictory information.
- Distinguishes essential missing information from optional details.
- Asks focused clarification questions when necessary.
- Produces a structured work plan when enough information is available.
- Helps prioritize tasks and identify next steps.
- Avoids inventing requirements or claiming that work has already been completed.

## How It Works

```text
User Work Request
        |
        v
Understand the Request
        |
        v
Extract Requirements
        |
        v
Check Information and Constraints
        |
        v
Is the Information Sufficient?
       / \
     No   Yes
     |     |
     v     v
Ask Focused   Create a Prioritized
Clarification Work Plan
       \     /
        v   v
    Return Structured Outcome
```

The agent follows this basic loop:

**Understand → Extract → Check Gaps → Clarify or Plan → Prioritize → Complete**

## A.G.E.N.T. Design Framework

The project uses the A.G.E.N.T. framework as its design lifecycle.

### A — Aim

Convert unclear work requests into clear, actionable outcomes without inventing requirements.

**Target users:** Team leads, project managers, product managers, consultants, and individual contributors.

### G — Gather

Use the information available in the conversation. Identify important context such as:

- Goal and expected outcome
- Deadline
- Constraints
- Stakeholders
- Expected deliverable
- Priority

The agent should distinguish critical missing details from optional details so that unnecessary questions do not block progress.

### E — Execution

Understand the request, extract requirements, detect gaps, ask targeted questions when needed, and create a prioritized plan when enough information is available.

### N — Navigation

Move between decision states according to information sufficiency, contradictions, and feasibility.

Suggested states:

`UNDERSTAND → CHECK_INFORMATION → CLARIFY or PLAN → COMPLETE`

### T — Test

Evaluate whether the agent asks useful questions, avoids unnecessary clarification, and creates practical plans.

Important test cases include complete requests, vague requests, missing optional details, missing essential details, contradictory requirements, changed requirements, and impossible objectives.

## Expected Outcomes

The agent returns one of two main outcomes:

1. **Clarification request** — asks for essential information needed to understand the request.
2. **Structured work plan** — organizes the goal, assumptions, priorities, tasks, and next steps.

When a request is contradictory or infeasible, the agent should explain the issue rather than silently making up an answer.

## Project Structure

```text
work-request-agent/
├── src/
│   └── agent/
│       ├── __init__.py
│       ├── cli.py
│       └── ...
├── .env.sample
├── .gitignore
├── .python-version
├── README.md
├── pyproject.toml
└── uv.lock
```

*The exact files inside `src/agent/` may vary as the project develops.*

## Technologies

- **Python** — application programming language
- **Pydantic AI** — agent framework and structured outputs
- **Pydantic** — data validation and typed models
- **uv** — Python project and dependency management
- **LLM provider** — configured through environment variables

## Requirements

- Python version specified in `.python-version` and `pyproject.toml`
- [uv](https://docs.astral.sh/uv/)
- An API key for the LLM provider configured by your project

## Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/YasodhiJaneera/Work_Request_Agent.git
cd Work_Request_Agent
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Configure environment variables

Copy `.env.sample` to `.env` and add the required API key and model settings.

On Windows Command Prompt:

```bat
copy .env.sample .env
```

On PowerShell:

```powershell
Copy-Item .env.sample .env
```

Use the variable names shown in `.env.sample`. Keep your real `.env` file and API keys private. **Do not commit secrets to GitHub.**

### 4. Run the agent

Run the application as a Python module from the project root:

```bash
uv run python -m src.agent.cli
```

Enter a work request when prompted and review the agent's clarification request or work plan.

## Example

**Input**

```text
We need to improve the onboarding process before next month.
```

**Possible behavior**

The agent checks whether the objective is clear enough and whether essential details are missing. If they are, it asks a focused question, such as what part of onboarding needs improvement. If enough context is available, it creates a prioritized plan.

*The exact response depends on the model and the information supplied by the user.*

## Design Boundaries

- The agent structures and prioritizes work; it does not perform the work itself.
- It should not invent deadlines, stakeholders, business facts, or completed actions.
- It should ask only questions that are needed to make progress.
- Optional missing details should not unnecessarily prevent planning.
- It should explain contradictions and limitations and suggest a realistic alternative where possible.

## Testing and Evaluation

Evaluate the agent using these scenarios:

| Scenario | Expected behavior |
|---|---|
| Complete request | Produce a structured plan |
| Very vague request | Ask a focused clarification question |
| Missing optional information | Continue when reasonable, stating assumptions |
| Missing essential information | Ask for the missing information |
| Contradictory requirements | Explain the conflict |
| User changes a requirement | Update or recreate the plan |
| Impossible objective | Explain the limitation and suggest a feasible alternative |

## Current Scope and Future Improvements

The current project focuses on a single agent that reasons, decides, clarifies, and plans without using external tools. Future versions could add integrations, persistent memory, document retrieval, or task-management tools while keeping clear decision rules and human oversight.

## Learning Outcome

This project demonstrates a minimum viable agentic loop:

**Reason → Decide → Clarify → Plan → Stop**

An effective agent is not simply one that generates more text. It is one that determines what should happen next.

## Author

**Yasodhi Janeera**

GitHub: [YasodhiJaneera](https://github.com/YasodhiJaneera)

## License

No license has been specified yet. Add a `LICENSE` file if you intend to distribute the project under an open-source license.
