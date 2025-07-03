import subprocess


def get_char(process) -> str:
    character = process.stdout.read(1)
    print(
        character,
        end="",
        flush=True,
    )
    return character

def search_for_output(strings, process):
    buffer = ""
    # strings의 모든 원소가 버퍼에 포함되지 않으면...
    while not any(string in buffer for string in strings):
        # 프로세스의 출력 스트림을 버퍼에 추가합니다.
        buffer += get_char(process)


with subprocess.Popen(
    # -u: 출력 스트림과 오류 스트림을 버퍼에 쌓지 않습니다.
    ["python3", "-u", "reaction_game_v2.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    text=True,
    encoding="utf-8",
) as process:
    process.stdin.write("\n") 
    process.stdin.flush()
    search_for_output(["==\n= ", "==\r\n= "], process)
    target_char = get_char(process)
    stdout, stderr = process.communicate(
        input=f"{target_char}\n",
        timeout=10,
    )
    print(stdout)