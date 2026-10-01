from .agent import triage_agent
from .models import ClarificationRequest, WorkPlan

def render_plan(
    output: WorkPlan,
) -> None:
    print("\n[WORK PLAN]\n")

    print("Goal:")
    print(f"  {output.goal}")

    if output.deadline:
        print("\nDeadline:")
        print(f"  {output.deadline}")

    if output.stakeholders:
        print("\nStakeholders:")

        for stakeholder in output.stakeholders:
            print(f"  - {stakeholder}")

    if output.constraints:
        print("\nConstraints:")

        for constraint in output.constraints:
            print(f"  - {constraint}")

    if output.assumptions:
        print("\nAssumptions:")

        for assumption in output.assumptions:
            print(f"  - {assumption}")

    print("\nTasks:")

    for task in sorted(
        output.tasks,
        key=lambda item: item.order,
    ):
        print(
            f"\n  {task.order}. "
            f"[{task.priority.upper()}] "
            f"{task.task}"
        )

        print(
            f"     Reason: "
            f"{task.rationale}"
        )

        if task.depends_on:
            print("     Depends on:")

            for dependency in task.depends_on:
                print(f"       - {dependency}")

    print("\nNext steps:")

    for step in output.next_steps:
        print(f"  - {step}")

    if output.unresolved_optional_information:
        print("\nOptional information still unknown:")

        for item in output.unresolved_optional_information:
            print(f"  - {item}")

def render_clarification(
    output: ClarificationRequest,
) -> None:
    print("\n[CLARIFICATION REQUIRED]\n")

    print("Understood goal:")
    print(f"  {output.understood_goal}")

    print("\nMissing critical information:")

    for item in output.missing_critical_information:
        print(f"  - {item}")

    if output.conflicts:
        print("\nConflicts:")

        for conflict in output.conflicts:
            print(f"  - {conflict}")

    print("\nQuestions:")

    for index, question in enumerate(
        output.questions,
        start=1,
    ):
        print(f"\n  {index}. {question.question}")
        print(f"     Field: {question.field}")
        print(f"     Why: {question.reason}")


def main():
    message_history = []

    while True:
        user_input = input("\nYou > ").strip()

        result = triage_agent.run_sync(
            user_input,
            message_history=message_history
        )

        if isinstance(result.output, ClarificationRequest):
            render_clarification(output=result.output)
        else:
            render_plan(output=result.output)

        message_history = result.all_messages()


if __name__ == "__main__":
    main()