import random as r
import json
from pathlib import Path


import CHATBOTV1.src.greeting as g
import CHATBOTV1.src.jokes as j
import CHATBOTV1.src.wheather as w
import CHATBOTV1.src.cheese as c

HISTORY_FILE = Path(__file__).with_name("chatbot_history.json")


def save_history(history):
    with HISTORY_FILE.open("w", encoding="utf-8") as file:
        json.dump(history, file, indent=2, ensure_ascii=False)

def load_history():
    if HISTORY_FILE.exists():
        with HISTORY_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    return []

def process_choice():
    history = load_history()

    while True:
        print("\nCHOOSE OPTION:\n1. Greet\n2. Cheese\n3. Joke\n4. Weather\n5. Exit")

        choice = input("Enter your choice (1-5): ")

        try:
            choice = int(choice)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            response = r.choice(g.greetings)

        elif choice == 5:
            print("Goodbye!")
            save_history(history)
            print(f"Chat history saved to {HISTORY_FILE}")
            break

        elif choice == 3:
            response = r.choice(j.jokes)

        elif choice == 4:
            response = r.choice(w.wheather)

        elif choice == 2:
            response = "cheese: " + r.choice(c.cheese)

        else:
            print("Invalid choice. Please enter 1 - 5.")
            continue

        print(response)
        history.append({"choice": choice, "response": response})


process_choice()
