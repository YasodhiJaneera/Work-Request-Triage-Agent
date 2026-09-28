from agent import triage_agent

def main():
    while True:
        user_input = input("\nYou > ").strip()

        result = triage_agent.run_sync(user_input)
        print(f"\nSystem >  {result}")


if __name__ == "__main__":
    main()