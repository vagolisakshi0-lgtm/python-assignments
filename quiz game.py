def ask_question(question, correct_answer, options=None):
    print(question)
    if options:
        for opt in options:
              print(opt)
    answer = input("Your answer: ").strip().lower()
    if answer == correct_answer.lower():
        print("Correct!\n")
        return True
    else:
        print(f"Wrong! The correct answer was: {correct_answer}\n")
        return False
def main():
        print("=" * 40)

        print("      WELCOME TO THE PYTHON QUIZ")
        print("=" * 40)
        score = 0
        total_questions = 5
        # Question 1
        if ask_question(
            "Q1. Which keyword is used to define a function in Python?",
            "b",
            ["a) func", "b) def", "c) function", "d) define"]
            ):
            score += 1
         # Question 2
        if ask_question(
             "Q2. What is the output of 3 + 2 * 2?",
             "b",
             ["a) 10", "b) 7", "c) 12", "d) 8"]
             ):
             score += 1
         # Question 3
        if ask_question(
             "Q3. Which loop is used when the number of iterations is known?",
             "b",
             ["a) while", "b) for", "c) do-while", "d) repeat"]
             ): 
             score += 1
             
         # Question 4
        if ask_question(
             "Q4. Which module is used to generate random numbers in Python?",
             "c",
             ["a) math", "b) numpy", "c) random", "d) os"]
             ):
             score += 1
         # Question 5
        if ask_question(
            "Q5. What data type is the result of 10 / 2 in Python 3?",
            "b",
            ["a) int", "b) float", "c) str", "d) bool"]
            ):
            score += 1
        # Final result
        print("=" * 40)
        print(f"Quiz Over! You scored {score} out of {total_questions}")
        percentage = (score / total_questions) * 100
        if percentage == 100:
            print("Perfect score! Excellent work!")
        elif percentage >= 80:
            print("Great job!")
        elif percentage >= 50:
            print("Good effort, keep practicing!")
        else:
            print("Needs improvement. Try again!")
            print("=" * 40)
if __name__ == "__main__":
    main()
            
