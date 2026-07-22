from pathlib import Path

my_dir = Path("./")
for obj in my_dir.iterdir():
    print(obj)

