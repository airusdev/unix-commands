# build the permission string

from pathlib import Path
import stat

my_dir = Path("./")
for obj in my_dir.iterdir():
    oct_st = oct(obj.stat().st_mode)
    permission = oct_st[-3::] 

    print(permission)
