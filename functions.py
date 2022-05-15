def calculation():
    global prob
    global name
    global userSymptoms
    global today
    global covid
    global afterTest
    global confirm
    symptoms = ["a. fever or chills", "b. cough", "c. shortness of breath or difficulty breathing", "d. fatigue", "e. muscle or body aches", "f. headache", "g. new loss of taste or smell", "h. sore throat", "i. congestion or runny nose", "j. nausea or vomiting", "k. diarrhea"]
    percent = [11.69, 10.39, 12.34, 8.44, 7.79, 7.79, 12.34, 10.39, 7.14, 5.84, 5.84]
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    name = input("What is your name?\n")
    userSymptoms = []
    prob = 0
    for x in symptoms:
        print(*x, sep="")
    symp = input("Enter the letter of your symptom from the list above\n")
    symp = symp.lower()
    while symp in letters:
        if symp in letters:
            index = letters.index(symp)
            prob = prob + percent[index]
            userSymptoms.append(symp)
        elif symp == "done":
            break
        symp = input("Enter your symptom letter from the list above. Type done when done.\n")
        symp = symp.lower()
        if symp == "done":
            print("This is the probability that you have COVID:", prob, "%\nAnything over 20% can be considered positive\n*IT IS RECOMMENDED TO GET TESTED FOR A CONFIRMED RESULT*\n*CONTACT PRIMARY CARE PROVIDER FOR NON-COVID RELATED SYMPTOMS*")
        elif symp not in letters:
            print("Invalid value")
    from datetime import date
    today = date.today()
    afterTest = input("Did you have COVID?\n")
    afterTest = afterTest.lower()
    if afterTest == "yes":
        afterTest = True
    elif afterTest == "no":
        afterTest = False
    if prob >= 20:
        covid = True
    else:
        covid = False
    if afterTest == covid:
        confirm = True
    else:
        confirm = False
    import csv
    list_data=[name, today, userSymptoms, prob, covid, afterTest, confirm]
    from csv import writer
    with open('Covid.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(list_data)
        f_object.close()

def database():
    global prob
    global name
    global userSymptoms
    global today
    global covid
    global afterTest
    global confirm
    global list_data
    import csv
    import pandas as pd
    from datetime import date
    today = date.today()
    df = pd.read_csv("Covid.csv")
    print(df)
    file = open("Covid.csv")
    reader = csv.reader(file)
    df = pd.read_csv("Covid.csv", sep=',', header=0)
    classify = input("How do you want to classify the data?\na. Date\nb. Confirmed cases\nc. Name\nd. None\n")
    while classify == "a" or classify == "b" or classify =="c":
        if classify == "b":
            df['confirm']
            confirm = df['confirm']
            print("The number of confirmed cases are:\n", df['confirm'][confirm].value_counts())
        elif classify == "a":
            df['date']
            date = df['date']
            print("Cases by date are:\n", date.value_counts())
        elif classify == "c":
            df['name']
            name = df['name']
            print("Cases by name are:\n", name.value_counts())
        classify = input("How do you want to classify the data?\na. Date\nb. Confirmed cases\nc. Name\nd. None\n")
    if classify == "d":
        print("Ok")
    else:
        print("Invalid Value")
