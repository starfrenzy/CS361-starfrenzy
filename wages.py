import time

def wages_calc(day=0, daily_totals={}):
    new_week = input("Hi! Is this a new week? Y/N: ")  # todo: consider removing this if not needed to determine new week

    if new_week.lower() == "y":  # .lower() in case they put in upper case
        # start = input("How much do you pay per hour? ")
        # wages = float(start)
        # print(f"wages: {wages}")
        todays_hours = hours_input()
        daily_totals[day] = todays_hours
        print("Thanks! See you tomorrow.")
        time.sleep(3)
        wages_calc(day, daily_totals)

    elif new_week.lower() == "n":
        day += 1
        todays_hours = hours_input()
        daily_totals[day] = todays_hours
        print(daily_totals)  # todo remove before submit/video

        if day != 6:
            print("Thanks! See you tomorrow.")
            time.sleep(3)
            wages_calc(day, daily_totals)

        else:  # stop and calculate
            weekly_sum = daily_totals[0] + daily_totals[1] + daily_totals[2] + daily_totals[3] + daily_totals[4] + daily_totals[5] + daily_totals[6]
            print("It's payday! n/"
                  f"{weekly_sum} is the total number of hours worked this week.")
            wages = wages_input()
            print(f"The payment should be ${wages}*{weekly_sum}.")


    else:
        wages_calc(day, daily_totals)  # if input was not y/n, run again

def wages_input():  # separate function to allow for CSH 5 Undo/Redo/Backtracking
    """
    This function asks the user how much they pay per hour, verifies that input, and returns the wages
    for use in the wage_calc function.
    Verification allows for CSH 5: Undo/Redo/Backtracking.
    """
    wages_str = input("How much do you pay per hour? ")
    wages = float(wages_str)
    verify_1 = input(f"Is ${wages} per hour the correct wage? Y/N: ")  # CSH 5 Undo/Redo/Backtracking

    if verify_1.lower() == "y":
        return wages

    else:
        wages_input()  # todo fix error returning NONE - messing up calculations


def hours_input():
    """
    This function asks the user how many hours were worked today, verifies that input, and returns the
    number of hours for use in the wage_calc function.
    Verification allows for CSH 5: Undo/Redo/Backtracking.
    """
    hours_str = input("How many hours were worked today? ")
    hours = float(hours_str)
    verify_2 = input(f"Is {hours} hours correct? Y/N: ")  # CSH 5 Undo/Redo/Backtracking

    if verify_2.lower() == "y":
        return hours

    else:
        hours_input()


wages_calc()