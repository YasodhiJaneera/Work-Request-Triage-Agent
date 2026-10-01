from .agent import triage_agent

from .models import ClarificationRequest, WorkPlan


def render_clarification_request(request:ClarificationRequest):
    print(request.question)

def main():

    message_history = []
    while True:
        user_input = input("\nYou > ").strip()

        result = triage_agent.run_sync(user_input,message_history=message_history)


        if isinstance(result.output, ClarificationRequest):
            render_clarification_request(request=result.output)
        else:
            print("coming soon")
            
        #print(f"\nSystem >  {result}")
        #print(f"\nSystem > {type(result.output)}")

    message_history +=[
        {
        "user": user_input,
        "agent":f"{result.output}"
        }
    ]

if __name__ == "__main__":
    main()