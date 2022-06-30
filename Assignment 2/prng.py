import time
import random

while True:
    # open file
    f = open("prng-service.txt", "r", encoding="utf-8")
    read_data = f.read()
    print(f"PRNG read-data read this: {read_data}")

    if read_data == "run":
        f.close()
        f = open("prng-service.txt", "w")
        # generate random number from 1 to 5
        rand_num = random.randint(1, 5)

        # write rand_num to prng-service.txt
        rand_str = str(rand_num)
        f.write(rand_str)
        print(f"we are writing this to prng-service:{rand_str} ")
        f.close()

    # close file - happens automatically because we used 'with'
