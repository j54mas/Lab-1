def average_numbers(threshold):
    list_of_numbers = []
    total = 0
    count = 0

    # ensure that the user enters valid numbers and handles exceptions
    while True:
        try:
            input_number = float(input("Enter a number (enter negative number to stop): "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

    # collect all of the numbers until the user enters a negative number
        if input_number >= 0:
            list_of_numbers.append(input_number)

    # once the user enters a negative number, calculate the average of the numbers greater than the threshold
        else:
            for i in list_of_numbers:
                if i > threshold:
                    total += i
                    count += 1

            return total / count if count > 0 else 0

# execute the program
threshold = float(input("Enter a threshold value: "))
average = average_numbers(threshold)
print(average)