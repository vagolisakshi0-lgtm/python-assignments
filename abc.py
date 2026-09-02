emp_id=int(input("enter emp_id:"))
emp_name=input("enter emp_name:")
department=input("enter department:")
experience=int(input("enter experience:"))
salary=int(input("enter salary:"))
ratings=int(input("enter ratings:"))
if ratings>1 or rating>5 or experience<0 or salary<0:
           print("invalid!")
else:
    if rating==5:
           bonus=0.20
           category="very good"
    elif rating==4:
      bonus=0.15
      category="good"
    elif rating==3:
        bonus=0.10
        category="average"
    elif rating==2:
        bonus=0.5
        category="poor"
    else:
        rating=1
        bonus=0.0
        category="very poor"
bonus=salary*bonus
final_salary=salary+bonus
print("bonus")
print("final_salary")
print("category")
if exp>=5 and exp<=5:
    print("promoted")
else:
    print("not promoted")
    
        
      
      
                  
