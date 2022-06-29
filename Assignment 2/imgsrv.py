import time

# read image-service.txt
while True:
    time.sleep(1)
    with open("image-service.txt", "r+", encoding="utf-8") as f:
        read_data = f.read()
        if read_data.isnumeric():
            our_num = float(read_data)

        # erase image-service.txt
        f.truncate()  # clears file
        f.seek(0)  # moves to the beginning of the file

        # write path to the image
        f.write(f"/Users/jessifrenzel/PycharmProjects/CS361-starfrenzy/Assignment 2/cs361_images/{our_num}")

        # handoff to UI

        # close file - happens automatically because we used 'with'