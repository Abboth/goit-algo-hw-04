from pathlib import Path
from pprint import pprint

def get_cat_info(path: Path):
    if path.exists():

        with open(path, "r", encoding="utf-8") as data:
            cat_info_dict = []

            for line in data:
                part = line.strip().split(",")
                cat_info_dict.append({
                    "id": part[0],
                    "name": part[1],
                    "age": part[2]
                })

            pprint(cat_info_dict)

    else:
        print(f"{path} не существует")

