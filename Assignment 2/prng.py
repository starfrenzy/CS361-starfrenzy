import time
import random

while True:
    time.sleep(1)
    # open file
    with open("prng-service.txt", "r+", encoding="utf-8") as f:
        read_data = f.read()
        for line in read_data:
            if line == "run":
                # generate random number from 1 to 5
                rand_num = random.randint(1, 5)

                # erase "run" from prng-services.txt
                f.truncate()  # clears prng-services.txt
                f.seek(0)  # moves to the beginning of the file

                # write rand_num to prng-service.txt
                rand_str = str(rand_num)
                f.write(rand_str)

    # close file - happens automatically because we used 'with'
