import platform
from pathlib import Path
from subprocess import run, DEVNULL


def init_shell():
    print("셸을 초기화합니다")
    system = platform.system()
    print("운영 체제:", system)
    if system == "Linux":
        return BashShell()
    
    elif system == "Windows":
        return PowerShell()
    
    # macOS
    elif system == "Darwin":
        return NotImplementedError
    

class PowerShell:
    def __init__(self) -> None:
        try:
            run(
                ["pwsh", "-V"],
                stdout=DEVNULL,
                stderr=DEVNULL,
            )
            self.shell = "pwsh"
        except FileNotFoundError as e:
            print("파워셸을 찾을 수 없습니다.")
            # 구식 파워셸을 사용
            self.shell = "powershell"
    
    @staticmethod
    def _make_string_path_list(paths: list[Path]) -> str:
        return "', '".join(str(path).replace("'", "`'") for path in paths)
    
    def ignore_paths(self, paths: list[Path]) -> None:
        path_list = self._make_string_path_list(paths)
        command = (
            "Set-Content -Path '{path_list}' "
            "-Stream com.dropbox.ignore -Value 1"
        )
        run([self.shell, "-NoProfile", "-Command", command], check=True)
        print("완료!")


class BashShell:
    @staticmethod
    def _make_string_path_list(paths: list[Path]) -> str:
        return "' '".join(str(path).replace("'", "\\'") for path in paths)
    
    def ignore_paths(self, paths: list[Path]) -> None:
        path_list = self._make_string_path_list(paths)
        command = (
            f"for f in '{path_list}'\n do\n "
            f"attr -s com.dropbox.ignore -V 1 $f\n "
            "done"
        )
        run(["bash", "-c", command], check=True)
        print("완료!")