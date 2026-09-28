from pydantic import BaseModel, Field
from typing import Literal


class ClarificationRequest(BaseModel):
    field: str = Field(
        description="The missing or conflict information"
    )

    question: str = Field(
        description="A question to ask the user"
    )

    reason: str = Field(
        description="Why this information is needed"
    )


class PlanTask(BaseModel):
    order: int = Field(
        ge=1,
        description="The order of the task"
    )

    task: str = Field(
        description="The task to be completed"
    )

    priority: Literal[
        "high",
        "medium",
        "low",
    ]

    rationale: str = Field(
        description="Why this task is needed"
    )

    depends_on: list[str] = Field(
        default_factory=list,
        description="Tasks that must be completed first"
    )


class WorkPlan(BaseModel):
    kind: Literal["plan"] = "plan"

    goal: str = Field(
        description="The main goal of the work request"
    )

    assumptions: list[str] = Field(
        default_factory=list
    )

    constraints: list[str] = Field(
        default_factory=list
    )

    deadline: str | None = Field(
        default=None,
        description=(
            "Deadline explicitly supplied by the user. "
            "Never invent a deadline."
        ),
    )

    stakeholders: list[str] = Field(
        default_factory=list,
        description=(
            "Stakeholders explicitly supplied by the user."
        ),
    )

    tasks: list[PlanTask] = Field(
        min_length=1
    )

    next_steps: list[str] = Field(
        min_length=1
    )

    unresolved_optional_information: list[str] = Field(
        default_factory=list
    )


TriageOutput = ClarificationRequest | WorkPlan