from random import choice, random
from string import ascii_lowercase
from time import perf_counter, sleep


print(
    "무작위 시간이 지난 뒤 화면에 글자가 표시됩니다.\n"
    "글자가 보이면 가능한 빠르게 글자와 엔터를 누르세요.\n\n"
    "준비가 되면 엔터를 누르세요.\n"
)
input()
print("준비하세요!")
sleep(random() * 5 + 2)
target_letter = choice(ascii_lowercase)
print(f"=====\n= {target_letter} =\n=====\n")

start = perf_counter()
while True:
    if input() == target_letter:
        break
    else:
        print("틀렸습니다. 다시 시도하세요.")
end = perf_counter()

print(f"반응 속도: {(end - start) * 1000:.0f} milliseconds!")