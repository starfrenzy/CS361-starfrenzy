import time

# prompt user to enter command
response = input("Please press 1 to continue.")

if response == "1":
    # call the PRNG service
    while True:
        time.sleep(1)
        # open file
        with open("prng-service.txt", "w", encoding="utf-8") as f:
            f.write("run")

        # read the random number from prnt-service.txt and write it to image-service.txt
        with open("prng-service.txt", "r", encoding="utf-8") as f:
            read_data = f.read()
            for line in read_data:
                rand_num = line

        with open("image-service.txt", "w", encoding="utf-8") as f:
            f.write(rand_num)
            # then image service reads image-service.txt, erases it, and writes an image path to it

    # return here to read image-service.txt and display the path to the user
        with open("image-service.txt", "r", encoding="utf-8") as f:
            img_path = f.readline()
            print(f"File Path: {img_path}")
