import subprocess
from time import sleep


with subprocess.Popen(
    ["python3", "timer.py", "5"],
    stdout=subprocess.PIPE,
) as process:
    def poll_and_read():
        print(f"조사 결과: {process.poll()}")
        print(f"stdout: {process.stdout.read1().decode()}")
    
    poll_and_read()
    sleep(3)
    poll_and_read()
    sleep(3)
    poll_and_read()