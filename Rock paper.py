import random
def get_computer_choice():
    choices=["rock","paper","scissors"]
    return random.choice(choices)
def decide_winner(user,computer):
    if user==computer:
       return"tie"
    elif(
        (user=="rock" and computer=="scissors") or
        (user=="paper" and computer=="rock") or
        (user=="scissors" and computer=="paper")
    ):
        return "user"
    else:
        return"computer"
odef main():
    print("="*40)
    print("   ROCK = PAPER = SCISSORS")
    print("="*40)
    print("Type 'quit'at any time to exit.\n")
    user_score=0
    computer_score=0
    while True:
        user_choice=input("Enter rock,paper,or,scissors:").strip().lower()
        if user_choice=="quit":
            break
        if user_choice not in ["rock","paper","scissors"]:
            print("Invalid choice:{computer_choice}")
            continue
        computer_choice=get_computer_choice()
        print(f"Computer chose:{computer_choice}")
        result=decide_winner(user_choice,computer_choice)
        if result=="tie":
            print("It's a tie!\n")
        elif result=="user":
            print("YOU win this round!\n")
            user_score+=1
        else:
            print("Computer wins this round!\n")
            computer_score+=1
        print(f"Score -> You:{user_score} Computer:{computer_score}\n")
        print("="*40)
        print("Final Score")
        print(f"You:{user_score} Computer:{computer_score}")
        if user_score>computer_score:
            print("Congratulations,you won overall!")
        elif user_score<computer_score:
            print("Computer won overall.Better luck next time!")
        else:
            print("Overall it's a tie!")
        print("="*40)
if __name__ =="__main__":
   main()
                  
        
        
