from datetime import datetime

now = datetime.now()

formatted = now.strftime("%m-%y-%d %H:%M:%S")

print(formatted)