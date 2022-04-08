print("Welcome to my quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print(" so Let's play :)")
score = 0

answer = input("What does EBIDTA stands for ? ")
if answer.lower() == "earnings before interest, taxes, depreciation, and amortization":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Which language is this program written in? ")
if answer.lower() == "python":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Who is best person in this world? ")
if answer.lower() == "karan":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("which language is used for game dev? ")
if answer.lower() == "c#":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")