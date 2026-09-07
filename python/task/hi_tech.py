import os
from datetime import datetime
try:
    a = 80
    b = 0
    x = a / b
    print("Result:", x)

except Exception as e:
    with open("error.log2", "a") as file:
        file.write("Error: " + str(e) + "\n")
        file.write("Path: " + os.path.abspath(__file__) + "\n")
        file.write("Log File Path: " + os.path.abspath("error.log2") + "\n")
        file.write("DateTime: " + datetime.now().strftime("%d-%m-%Y %H:%M:%S") + "\n")
