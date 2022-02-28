from datetime import datetime

print("hello-world")

now_str = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

with open('hello.log', 'w') as logfile:
    logfile.write(f"{now_str} sample log\n")

with open('hello.log') as logfile:
    print(logfile.read())
