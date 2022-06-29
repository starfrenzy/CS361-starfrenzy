import time
import random

while True:
    time.sleep(1)
    with open("prng-service.txt", "a", encoding="utf-8") as f:
        read_data = f.read()
        for line in read_data:
            if line == "run":
                rand_num = random.randint(1, 5)
                # erase "run" from prng-services.txt
                # write rand_num to prng-service.txt
        # close file - happens automatically because we used 'with'
