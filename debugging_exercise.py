#Should calc average of positive numbers entered by the user.
#Should end when the user enters 0.
case_closed = False
total_sum,count,active = 0,0,True

# if the user enters zero immediately, the program will attempt to divide zero
while active:
    val = int(input("Enter a number (0 to stop): "))
    if val == 0:
        active = False
        break
    if val > 0:
        total_sum = total_sum + val
        count += 1
try: 
    average = total_sum/count
except (ZeroDivisionError):
    print(f"The average of your numbers is: 0")
    case_closed = True

if not case_closed:
    print(f"The average of your numbers is: {average}")
