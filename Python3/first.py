print("Welcome to the Quiz")

score = 0

q1 = input("What is the capital of France: ")

if q1.lower() == "paris":
    score += 1

q2 = input("2 + 2 = ?")
if q2 == 4:
    score += 1

print("Your score is: ", score, "/2")