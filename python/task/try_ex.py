import os
from datetime import datetime
try:
    a = 19
    b = 0
    x = a / b
    print("Result:", x)

except Exception as e:
    with open("error.log", "a") as file:
        file.write("Error: " + str(e) + "\n")
        file.write("Path: " + os.path.abspath(__file__) + "\n")
        file.write("DateTime: " + datetime.now().strftime("%d-%m-%Y %H:%M:%S") + "\n")