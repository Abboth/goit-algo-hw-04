from pathlib import Path
import re


def get_total_salary(path: Path) -> str:
    if path.exists():
        with open(path, "r", encoding='utf-8') as file:
            salaries = []
            pattern = r",\s*(\d+\.?\d*)"

            for line in file:
                match = re.search(pattern, line)
                if match:
                    salary = float(match.group(1))
                    salaries.append(salary)

            average_salary = sum(salaries) / len(salaries)

            return f"Общая сумма зарплат: {sum(salaries)}\nсредняя зарплата: {average_salary}"
    else:
        print(f"{path} не существует")
