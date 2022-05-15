for i in range(1,4):
    print("#", end="")
    for x in range(1,22):
        print("*", end="")
    print("#")
print("#COVID Symptom Checker#")
for j in range(1,4):
    print("#", end="")
    for k in range(1,22):
        print("*", end="")
    print("#")
from functions import calculation
from functions import database
choice = input("Choose a or b\na. Calculate the probability that you have Covid\nb. See past results\nc. Terminate program\n")
choice = choice.lower()
while choice == "a" or choice == "b":
    if choice == "a":
        calculation()
    elif choice == "b":
        database()
