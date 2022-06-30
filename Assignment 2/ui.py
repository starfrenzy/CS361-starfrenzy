import time

# prompt user to enter command
response = input("Please press 1 to continue.")

if response == "1":
    # call the PRNG service
    yellow = False
    while yellow is False:
        f = open("prng-service.txt", "r", encoding="utf-8")
        if f.read() == "":
            f.close()
            # open file
            with open("prng-service.txt", "w", encoding="utf-8") as write_prng:
                write_prng.write("run")
                time.sleep(5)

        # read the random number from prng-service.txt and write it to image-service.txt
        with open("prng-service.txt", "r", encoding="utf-8") as read_prng:
            rand_num = read_prng.read()

        if rand_num != "run":
            with open("image-service.txt", "w", encoding="utf-8") as write_image:
                write_image.write(rand_num)

                # then image service reads image-service.txt, erases it, and writes an image path to it

        # return here to read image-service.txt and display the path to the user
            with open("image-service.txt", "r", encoding="utf-8") as read_image:
                time.sleep(3)
                img_path = read_image.readline()
                yellow = True
