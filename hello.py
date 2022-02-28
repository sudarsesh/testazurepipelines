from datetime import datetime

print("hello-world")

now_str = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

if os.path.isdir('/tmp/test_logs') is False:
    os.path.mkdir('/tmp/test_logs')

log_path = "/tmp/test_logs"
    
with open(f'{log_path}/hello.log', 'w') as logfile:
    logfile.write(f"{now_str} sample log\n")

with open(f'{log_path}/hello.log') as logfile:
    print(logfile.read())
