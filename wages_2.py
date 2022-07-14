import time


def wages_calc(day=0, daily_totals=None, day_names=None):
    """
    This function asks a user for daily hours worked and wages paid and calculates a payment sum.
    """
    if daily_totals is None:
        daily_totals = {}

    if day_names is None:
        day_names = {
            0 : "Monday",
            2 : "Tuesday",
            3 : "Wednesday",
            4 : "Thursday",
            5 : "Friday",
            6 : "Saturday",
            7 : "Sunday"
        }
    print(f"Today is {day_names[day]}. Let's record today's hours.")
    todays_hours = hours_input()
    today = day_names[day]
    daily_totals[today] = todays_hours
    day += 1
    print(daily_totals)  # todo remove before final submit - just checking for None

    if day != 7:
        print("Thanks! See you tomorrow.")
        time.sleep(3)
        wages_calc(day, daily_totals, day_names)

    else:  # stop and calculate
        weekly_sum = daily_totals[0] + daily_totals[1] + daily_totals[2] + daily_totals[3] + daily_totals[4] + daily_totals[5] + daily_totals[6]
        print(f"It's payday! \n{weekly_sum} is the total number of hours worked this week.")
        print(f"The daily hours were {daily_totals}.")
        wages = wages_input()
        payment = weekly_sum * wages
        print(f"\nThe total amount due is ${payment}.")


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
        wages_input()


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
        hours_input()    # todo fix error returning NONE - messing up calculations


wages_calc()