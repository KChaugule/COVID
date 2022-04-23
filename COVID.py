symptoms = ["fever or chills", "cough", "shortness of breath or difficulty breathing", "fatigue", "muscle or body aches", "headache", "new loss of taste or smell", "sore throat", "congestion or runny nose", "nausea or vomiting", "diarrhea"]
percent = [11.69, 10.39, 12.34, 8.44, 7.79, 7.79, 12.34, 10.39, 7.14, 5.84, 5.84]
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
prob = 0
know = input("Do you want to know the probability that you have COVID-19?\n")
know = know.lower()
