import random
print("==============")
print("[MATH] MATH CHALLANGE")
print("==========")
name=input("enter your name:")
score=0
for i in range(5):
    num1=random.randint(1,20)
    num2=random.randint(1,20)
    print("\n question",i+1)
    print(num1,"+",num2,"=?")
    answer=int(input("Answer:"))
    if answer==num1+num2:
        print("[OK]Correct!")
        score+=10
    else:
        print("[x]Wrong!")
        print("Correct answer:",num1+num2)
print("==========")
print("      RESULT")
print("===========")
print("Student:",name)
print("score:",score,"/50")
if score==50:
    print("thumbsup]Good job!")
else:
    print("[books]Practice more!")
print("========")
