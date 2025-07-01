from argparse import ArgumentParser
from time import sleep


parser = ArgumentParser()
parser.add_argument("time", type=int)
args = parser.parse_args()
print(f"{args.time} 초를 세는 타이머 시작!")
for _ in range(args.time):
    print(".", end="", flush=True)
    sleep(1)
print("완료!")