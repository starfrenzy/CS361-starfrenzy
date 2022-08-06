import time
import zmq


def wages_calc(day=0, daily_totals=None, day_names=None):
    """
    This function asks a user for daily hours worked and wages paid and calculates a payment sum. It incorporates
    a microservice to keep a record of each week's hours over time. At the end of each week, the total hours and payment
     amount are printed and the 'daily_totals' dictionary is added to a JSON list of all weeks' daily hours.
    """
    if daily_totals is None:
        daily_totals = {}

    if day_names is None:
        day_names = {
            0 : "Monday",
            1 : "Tuesday",
            2 : "Wednesday",
            3 : "Thursday",
            4 : "Friday",
            5 : "Saturday",
            6 : "Sunday"
        }

    today = day_names[day]  # new week starts on Monday
    print(f"It's {today}! Let's record today's hours.")
    todays_hours = hours_input()
    daily_totals[today] = todays_hours
    day += 1
    print(f"\nDaily totals: {daily_totals}")

    if day != 7:
        print(f"{today}'s hours have been recorded! Please make sure to enter hours every single day"
              f" to receive a total.\n")
        time.sleep(2)
        wages_calc(day, daily_totals, day_names)

    else:  # stop and calculate
        weekly_sum = daily_totals["Monday"] + daily_totals["Tuesday"] + daily_totals["Wednesday"] + \
                     daily_totals["Thursday"] + daily_totals["Friday"] + daily_totals["Saturday"] + daily_totals["Sunday"]
        print("\nIt's payday!")
        print(f"{weekly_sum} is the total number of hours worked this week.\n")
        wages = wages_input()
        payment = weekly_sum * wages
        print(f"\nThe total amount due is ${payment:.2f}.")

        daily_totals.update({"Total Hours": weekly_sum, "Amount Paid": payment})

        # microservice starts here
        context = zmq.Context()

        #  Socket to talk to server
        print("Connecting to server 2000...")
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://localhost:2000")

        # Send dictionary as JSON
        print("Sending dictionary as json ...")
        socket.send_json(daily_totals)

        #  Get the reply.
        message = socket.recv()
        print(f"Received [ {message} ]")


def wages_input():  # separate function to allow for CSH 5 Undo/Redo/Backtracking
    """
    This function asks the user how much they pay per hour, verifies that input, and returns the wages
    for use in the wage_calc function.
    Verification allows for CSH 5: Undo/Redo/Backtracking.
    """
    wages_str = input("How much do you pay per hour? ")
    wages = float(wages_str)
    verify_1 = input(f"Is ${wages:.2f} per hour the correct wage? Y/N: ")  # CSH 5 Undo/Redo/Backtracking

    if verify_1.lower() == "y":
        return wages

    else:
        return wages_input()


def hours_input():
    """
    This function asks the user how many hours were worked today, verifies that input, and returns the
    number of hours for use in the wage_calc function.
    Verification allows for CSH 5: Undo/Redo/Backtracking.
    """
    hours_str = input("How many hours were worked? ")
    hours = float(hours_str)

    if hours < 0:
        print("Error: Please enter a positive number.")
        return hours_input()

    verify_2 = input(f"Is {hours} hours correct? Y/N: ")  # CSH 5 Undo/Redo/Backtracking

    if verify_2.lower() == "y":
        return hours

    else:
        return hours_input()


wages_calc()