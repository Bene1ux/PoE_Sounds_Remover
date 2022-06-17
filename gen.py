from pathlib import Path

NAMES_FILE = 'General_Gameplay.txt'
CONTENT_FILE = 'Crit.wav'
TARGET_DIR = 'General_Gameplay'

def main() -> None:
  dir = Path(TARGET_DIR)
  with open(NAMES_FILE, 'rt') as names_file:
    file_names: list[str] = [it.strip() for it in names_file.readlines()]

  with open(CONTENT_FILE, 'rt') as content_file:
    content: str = content_file.read()

  for file_name in file_names:
    file = dir / file_name
    file.write_text(content)


if __name__ == '__main__':
  main()