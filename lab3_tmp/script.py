import csv
import re

from checksum import calculate_checksum, serialize_result

PATTERNS = {
    "email":      re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"),
    "height":     re.compile(r"^(?:1\.\d{2}|2\.[0-4]\d|2\.50)$"),
    "inn":        re.compile(r"^\d{12}$"),
    "passport":   re.compile(r"^\d{2} \d{2} \d{6}$"),
    "occupation": re.compile(r"^[А-ЯЁA-Z][А-Яа-яЁёA-Za-z]*(?:[ -][А-Яа-яЁёA-Za-z]+)*$"),
    "latitude":   re.compile(r"^-?(?:[0-8]?\d|90)\.\d{6}$"),
    "hex_color":  re.compile(r"^#[0-9a-fA-F]{6}$"),
    "issn":       re.compile(r"^\d{4}-\d{4}$"),
    "uuid":       re.compile(r"^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$"),
    "time":       re.compile(r"^(?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d\.\d{6}$")
}

VARIANT = 79
CSV_FILENAME = "79.csv"


def is_row_valid(row: dict) -> bool:
    """Проверяет строку на соответствие всем регулярным выражениям."""
    for column, pattern in PATTERNS.items():
        value = row.get(column, "")
        if not pattern.fullmatch(value):
            return False
    return True


def main():
    invalid_lines = []

    try:
        with open(CSV_FILENAME, encoding="utf-8", newline="") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            
            for line_num, row in enumerate(reader, start=0):
                if not is_row_valid(row):
                    invalid_lines.append(line_num)
                    
    except FileNotFoundError:
        print(f"Ошибка: Файл {CSV_FILENAME} не найден в текущей директории.")
        return

    print(f"Найдено невалидных строк: {len(invalid_lines)}")
    
    checksum_value = calculate_checksum(invalid_lines)
    print(f"Контрольная сумма: {checksum_value}")

    serialize_result(VARIANT, checksum_value)
    print("Результат успешно записан в result.json")


if __name__ == "__main__":
    main()