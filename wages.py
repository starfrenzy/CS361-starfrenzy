import time

def wage_calc(day=0, daily_totals={}):

    new_week = input("Hi! Is this a new week? Y/N: ")
    if new_week.lower() == "y":  # in case they put in upper case
        start = input("How much do you pay per hour? ")
        wages = float(start)
        print(f"wages: {wages}")
        hours = input("How many hours were worked today? ")
        daily_totals[day] = hours
        print("Thanks! See you tomorrow.")
        time.sleep(5)
        wage_calc(day, daily_totals)

    elif new_week.lower() == "n":
        day += 1
        hours = input("How many hours were worked today? ")
        daily_totals[day] = hours
        print("Thanks! See you tomorrow.")
        time.sleep(5)
        wage_calc(day, daily_totals)
        # todo add in a STOP at 7 days. Calculate and print.

    else:
        wage_calc()  # if input was not y/n, run again

wage_calc()