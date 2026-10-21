import random as r
import CHATBOTV1.options.greeting as g
import CHATBOTV1.options.jokes as j
import CHATBOTV1.options.wheather as w
import CHATBOTV1.options.cheese as c

def process_choice():
    while True:
        print("\nCHOOSE OPTION:\n1. Greet\n2. Cheese\n3. Joke\n4. Weather\n5. Exit")

        choice = input("Enter your choice (1-5): ")

        try:
            choice = int(choice)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            print(r.choice(g.greetings))

        elif choice == 5:
            print("Goodbye!")
            break

        elif choice == 3:
            print(r.choice(j.jokes))

        elif choice == 4:
            print(r.choice(w.wheather))

        elif choice == 2:
            print("cheese: " + r.choice(c.cheese))

        else:
            print("Invalid choice. Please enter 1 - 5.")


process_choice()
