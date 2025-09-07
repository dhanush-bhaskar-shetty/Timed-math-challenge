import random
import time

operator=["+","-","*"]
total_problems=int(input("enter the number of problem you want to solve "))

def generate_problem():
    left=random.randint(3,10)
    right=random.randint(3,10)
    op=random.choice(operator)
    exp=str(left)+op+str(right)
    answer=eval(exp)   #evaluates valid string expression
    return exp,answer
wrong_answer=0
start_time=time.time()

for i in range(total_problems):
    expression,answer=generate_problem()
    while True:
        guess=int(input("answer of"+expression+"= "))
        if(answer==guess):
          break
        
        wrong_answer+=1

end_time=time.time()
time_taken= end_time-start_time
time_taken=int(time_taken)
print("nice work,you finished in "+str(time_taken)+" seconds")
print("wrong count= ",wrong_answer)

