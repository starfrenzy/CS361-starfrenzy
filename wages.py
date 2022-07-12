import time

def wage_calc(day=0, daily_totals={}):
    new_week = input("Hi! Is this a new week? Y/N: ")

    if new_week.lower() == "y":  # .lower() in case they put in upper case
        start = input("How much do you pay per hour? ")
        wages = float(start)
        print(f"wages: {wages}")
        todays_hours = hours_input()
        daily_totals[day] = todays_hours
        print("Thanks! See you tomorrow.")
        time.sleep(5)
        wage_calc(day, daily_totals)

    elif new_week.lower() == "n":
        day += 1
        todays_hours = hours_input()
        daily_totals[day] = todays_hours

        if day == 6:  # stop and calculate
            weekly_sum = daily_totals[0] + daily_totals[1] + daily_totals[2] + daily_totals[3] + daily_totals[4] + daily_totals[5] + daily_totals[6]
            print(f"{weekly_sum} is the total number of hours worked this week.")
            print(f"The payment should be ${wages}*{weekly_sum}.")

        else:
            print("Thanks! See you tomorrow.")
            time.sleep(5)
            wage_calc(day, daily_totals)

    else:
        wage_calc(day, daily_totals)  # if input was not y/n, run again

def wages_input():  # separate function to allow for CSH 5 Undo/Redo/Backtracking
    wages =
def hours_input():
    hours = input("How many hours were worked today? ")
    verify_1 = input(f"Is {hours} hours correct? Y/N: ")  # CSH 5 Undo/Redo/Backtracking

    if verify_1.lower() == "y":
        return hours

    else:
        hours_input()

wage_calc()