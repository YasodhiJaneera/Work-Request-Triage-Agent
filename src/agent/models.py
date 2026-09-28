from pydantic import BaseModel, Field
from typing import Literal


class ClarificationRequest(BaseModel):
    
    field:str = Field(
        description="The missing or conflict information"
    )
    
    question:str = Field(
        description="A Question to ask from user"
    )
    
    reason:str = Field(
        description="Why this information needed"
    )
class PlanTask(BaseModel):
    order: int = Field(ge=1)

    task: str

    priority: Literal[
        "high",
        "medium",
        "low",
    ]

    rationale: str

    depends_on: list[str] = Field(
        default_factory=list
    )
class WorkPlan(BaseModel):
    kind: Literal["plan"] = "plan"

    goal: str

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