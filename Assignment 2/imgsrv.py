import time

# read image-service.txt
while True:
    time.sleep(1)
    f = open("image-service.txt", "r", encoding="utf-8")
    read_data = f.read().strip()
    print(f"IMAGE read-data read this: {read_data}")

    if read_data != "run" and read_data != "" and "/Users/jessifrenzel" not in read_data:
        f.close()
        with open("image-service.txt", "w") as f:
            our_num = int(read_data)

            # write path to the image
            f.write(f"/Users/jessifrenzel/PycharmProjects/CS361-starfrenzy/Assignment 2/cs361_images/{our_num}")
            print(f"Writing this path: /Users/jessifrenzel/PycharmProjects/CS361-starfrenzy/Assignment 2/cs361_images/{our_num}")

        # close file - happens automatically because we used 'with'