from argparse import ArgumentParser
from pathlib import Path
import subprocess


def create_new_project(name: str):
    project_folder = Path.cwd().absolute() / name
    project_folder.mkdir()
    (project_folder / "README.md").touch()
    with open(project_folder / ".gitignore", "w") as f:
        f.write("\n".join(["venv", "__pycache__"]))
    commands = [
        ["python3", "-m", "venv", f"{project_folder}/venv"],
        ["git", "-C", project_folder, "init"],
        ["git", "-C", project_folder, "add", "."],
        ["git", "-C", project_folder, "commit", "-m", "Initial commit"],
    ]
    for command in commands:
        try:
            subprocess.run(command, check=True, timeout=60,)
        except FileNotFoundError as e:
            print(f"파일을 찾을 수 없어 {command} 명령이 실패했습니다.\n", e)
        except subprocess.CalledProcessError as e:
            print(f"반환 부호가 '성공'이 아니어서 {command} 명령이 실패했습니다.\n", e)
        except subprocess.TimeoutExpired as e:
            print(f"시간 초과로 {command} 명령이 실패했습니다.\n", e)


def main():
    parser = ArgumentParser()
    parser.add_argument("project_name", type=str)
    args = parser.parse_args()
    create_new_project(args.project_name)


if __name__ == "__main__":
    main()