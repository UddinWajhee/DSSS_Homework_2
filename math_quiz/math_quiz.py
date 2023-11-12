import random


def generate_random_integer(minimum, maximum):
    """
    Generate a random integer between the specified minimum and maximum values.
    """
    return random.randint(minimum, maximum)


def generate_random_operator():
    """
    Generate a random mathematical operator from the set {+, -, *}.
    """
    return random.choice(['+', '-', '*'])


def perform_operation(num1, num2, operator):
    """
    Perform the mathematical operation based on the given numbers and operator.
    Returns a tuple containing the problem string and the correct answer.
    """
    problem = f"{num1} {operator} {num2}"
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    return problem, answer


def math_quiz():
    """
    Conduct a math quiz game where the user needs to provide correct answers to given problems.
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5.5)
        operator = generate_random_operator()

        problem, correct_answer = perform_operation(num1, num2, operator)
        print(f"\nQuestion: {problem}")
        
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
