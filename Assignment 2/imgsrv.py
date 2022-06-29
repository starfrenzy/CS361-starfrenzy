import time

# read image-service.txt
while True:
    time.sleep(1)
    with open("image-service.txt", "r+", encoding="utf-8") as f:
        read_data = f.read()
        if read_data.isnumeric():
            our_num = float(read_data)

# erase image-service.txt

# write path to the image


#handoff to UI