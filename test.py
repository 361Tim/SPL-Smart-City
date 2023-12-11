import datetime
import random
import json
import time
import os


def input1():
    return random.randint(0, 1)

def input2():
    return random.randint(0, 1)


count = 0
location = "Birkenwiese"
while True:


    input1_value = input1()
    input2_value = input2()

    if input1_value == 1 and input2_value == 1:
        time.sleep(5)
        count += 1

        data = {
            'timestamp': str(datetime.datetime.now()),
            'count': count,
            'location': location,
            'input1': input1_value,
            'input2': input2_value
            }

        with open('data.json', 'a') as json_file:
            json.dump(data, json_file)
            json_file.write('\n')