import os
from datetime import datetime
try:
    number= int(input("video section:"))
except Exception as e:
    with open("raj.log","w")as file:
        file.write(str(e)+"\n")
        file.write("Path: " + os.path.abspath(__file__) + "\n")
        file.write("DateTime: " + datetime.now().strftime("%d-%m-%Y %H:%M:%S") + "\n")


    
