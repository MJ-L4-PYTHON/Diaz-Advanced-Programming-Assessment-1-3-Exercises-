import random

def displayMenu():
    print("DIFFICULTY LEVEL")
    print("1. Easy")
    print("2. Moderate")
    print("3. Advanced")

def randomInt(difficulty):
    if difficulty == 1:
        return random.randint(1, 9)
    elif difficulty == 2:
        return random.randint(10, 99)
    elif difficulty == 3:
        return random.randint(1000, 9999)

def decideOperation():
    return random.choice(['+', '-'])

def displayProblem(num1, num2, operation):
    print(f"{num1} {operation} {num2} = ", end="")
    answer = int(input())
    return answer

def isCorrect(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Correct!")
        return True
    else:
        print("Incorrect.")
        return False

def displayResults(score):
    print(f"Your final score is: {score}/100")
    if score > 90:
        print("Rank: A+")
    elif score > 80:
        print("Rank: A")
    elif score > 70:
        print("Rank: B")
    elif score > 60:
        print("Rank: C")
    else:
        print("Rank: D")

def main():
    play_again = 'y'
    
    while play_again.lower() == 'y':
        displayMenu()
        difficulty = int(input("Select a difficulty level (1-3): "))
        
        score = 0
        for _ in range(10):
            num1 = randomInt(difficulty)
            num2 = randomInt(difficulty)
            operation = decideOperation()
            
            if operation == '+':
                correct_answer = num1 + num2
            else:
                correct_answer = num1 - num2
            
            user_answer = displayProblem(num1, num2, operation)
            
            if isCorrect(user_answer, correct_answer):
                score += 10
            else:
                user_answer = int(input("Try again: "))
                if isCorrect(user_answer, correct_answer):
                    score += 5
        
        displayResults(score)
        
        play_again = input("Would you like to play again? (y/n): ")

if __name__ == "__main__":
    main()