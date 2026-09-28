from agent import triage_agent

def main():

    message_history = []
    while True:
        user_input = input("\nYou > ").strip()

        result = triage_agent.run_sync(user_input,message_history=message_history)
        print(f"\nSystem >  {result}")

    message_history +=[
        {
        "user": user_input,
        "agent":f"{result.output}"
        }
    ]

if __name__ == "__main__":
    main()