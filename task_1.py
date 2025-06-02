from pathlib import Path
import argparse
import shutil

def copy_files(path_from:Path, path_to: Path):
    try:
        for child in path_from.iterdir():
            if child.is_dir():
                copy_files(child, path_to)
            elif child.is_file():
                try:
                    ext = child.suffix.lower().lstrip('.') or 'no_extension'
                    target_path = path_to / ext
                    target_path.mkdir(parents=True, exist_ok=True)

                    shutil.copy2(child, target_path / child.name)
                    print(f'Copied: {child} → {target_path / child.name}')
                except Exception as e:
                    print(f'Помилка копіювання файлу {child}: {e}')
    except Exception as e:
        print(f'Помилка читання директорії {path_from}: {e}')  

def parse_arguments():
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання та сортування файлів за розширенням.")
    parser.add_argument("source", type=Path, help="Шлях до вихідної директорії")
    parser.add_argument("destination", type=Path, nargs='?', default=Path("dist"), help="Шлях до директорії призначення (за замовчуванням: ./dist)")
    return parser.parse_args()


def main():
    args = parse_arguments()
    source_dir = args.source.resolve()
    destination_dir = args.destination.resolve()

    if not source_dir.is_dir():
        print(f"Вихідна директорія {source_dir} не існує або не є директорією.")
        return

    destination_dir.mkdir(parents=True, exist_ok=True)
    print(f"Копіювання з: {source_dir}")
    print(f"До: {destination_dir}")

    copy_files(source_dir, destination_dir)
    print("Завершено!")


if __name__ == "__main__":
    main()