import time

while True:
    time.sleep(1)
    with open("image-service.txt", "a", encoding="utf-8") as f:
        read_data = f.read()
        if read_data.isnumeric():
            our_num = float(read_data)