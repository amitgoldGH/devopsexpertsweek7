from datetime import datetime

print("Hello, World!")

now = datetime.now()
formatted = now.strftime("%H:%M:%S")
print("Today's date and time is:", formatted)
