from time import perf_counter, sleep
from random import random


print("시작하려면 엔터를 누르세요")
input()
print("'go!'가 출력되면 엔터를 누르세요!")
sleep(random() * 5 + 1)
print("go!")
start = perf_counter()
input()
end = perf_counter()
print(f"반응 속도: {(end - start) * 1000:.0f} milliseconds!")