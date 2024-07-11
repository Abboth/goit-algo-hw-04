from colorama import Fore, Style
from pathlib import Path
import sys


def folder_research(path: Path, indent=0):
    if path.exists():
        for item in path.iterdir():
            if item.is_file():
                print(Fore.GREEN + "    " * indent, item.name)
            else:
                print(Fore.BLUE + "    " * indent, item.name)
                folder_research(item, indent + 1)
    else:
        print(Fore.RED + Style.BRIGHT + "This path is not exist, check it")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        console_to_path = Path(sys.argv[1])
        folder_research(console_to_path)
