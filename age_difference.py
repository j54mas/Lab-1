# make sure input values are valid inputs
while True:
    try:
        # name and age of first person
        person1 = input("Enter the name of the first person: ")
        age1 = int(input("Enter the age of the first person: "))

        # name and age of second person
        person2 = input("Enter the name of the second person: ")
        age2 = int(input("Enter the age of the second person: "))
        break
    except ValueError:
        print("Please enter a valid integer for age.")

difference = 0

# determine age difference and who is older
if age1 > age2:
    difference = age1 - age2
    print(person1 + " is older than " + person2 + " by " + str(difference) + " years.")
elif age2 > age1:
    difference = age2 - age1
    print(person2 + " is older than " + person1 + " by " + str(difference) + " years.")
else:
    print(person1 + " and " + person2 + " are of the same age.")