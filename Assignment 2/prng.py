import time

while True:
    time.sleep(1)
    with open("prng-service.txt", "a", encoding="utf-8") as f:
        read_data = f.read()
        for line in read_data:
            if line == "run":
                #generate random number
                # erase "run" from prng-services.txt
                #write random number to prng-service.txt
        # close file - happens automatically because we used 'with'
