import subprocess


subprocess.run(["bash", "-c", f"ls {input('조회할 경로를 입력하세요: ')}"])