import random

def load_jokes(filename="jokes.txt"):
    with open(filename, 'r', encoding='utf-8') as file:
        jokes = [line.strip() for line in file.readlines() if '?' in line]
    return jokes

def tell_joke(jokes):
    joke = random.choice(jokes)
    setup, punchline = joke.split('?')
    print(setup + '?')
    input("Press any key to see the punchline...")
    print(punchline)

def main():
    jokes = load_jokes('jokes.txt')
    print("Type 'Alexa tell me a Joke' to hear a joke or 'quit' to exit.")
    
    while True:
        command = input("Your command: ").strip().lower()
        if command == "alexa tell me a joke":
            tell_joke(jokes)
        elif command == "quit":
            print("Goodbye!")
            break
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()