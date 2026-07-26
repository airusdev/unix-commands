# build the permission string

from datetime import datetime
from pathlib import Path
import stat
import pwd
import grp
from tabulate import tabulate


directory = Path("./")
my_dir = sorted([obj.name for obj in directory.iterdir()])
ordered_dir = sorted([item for item in directory.iterdir()])
table = []

for obj in ordered_dir:
    is_dotfile = obj.name.split('.')[0] == ''
    if is_dotfile:
        continue 
    
    oct_st = oct(obj.stat().st_mode)
    permission = str(oct_st[-3::])
    permission_str = []

    if obj.is_dir():
        permission_str.append('d')
    else:
        permission_str.append('-')

    """NEED TO REWRITE MY PERMISSION STRING LOGIC"""

    # permission string 
    sub_permission_str = []
    for num in permission:
        num = int(num)
        if num >= 4:
            sub_permission_str.append("r")
            num -= 4
        else:
            sub_permission_str.append('-')
        if num >= 2:
            sub_permission_str.append('w')
            num -= 2
        else:
            sub_permission_str.append('-')

        if num >= 1:
            sub_permission_str.append('x')
            num -= 1
        else:
            sub_permission_str.append('-')

    permission_str.append(''.join(sub_permission_str))
    permission_str = ''.join(permission_str)
    # print(permission_str, obj)

    # number of hard links
    nlinks = obj.stat().st_nlink

    # owner
    owner = pwd.getpwuid(obj.stat().st_uid).pw_name

    # group
    group = grp.getgrgid(obj.stat().st_gid).gr_name

    # file size
    file_size = obj.stat().st_size

    # modification time
    seconds = obj.stat().st_mtime
    time_modified = datetime.fromtimestamp(seconds)
    month = time_modified.strftime('%B')[:3]
    day = time_modified.strftime('%b')
    time = time_modified.strftime('%H:%M') 

    obj_details = f'{permission_str} {nlinks} {owner} {group} {file_size} {month} {day} {time} {obj}'
    table_row = obj_details.split()
    table.append(table_row)
    
print(tabulate(table, tablefmt='plain', numalign=1, stralign=1))




"""
'r'     4 = read
'w'     2 = write
'x'     1 = execute
"""
# from tabulate import tabulate, simple_separated_format
# data = [["Alice", 24, "New York"], ["Bob", 109, "Chicago"]]
# headers = ["Name", "Age", "City"]
# # print(tabulate(data, tablefmt=simple_separated_format(" ")))
# print(tabulate(data, tablefmt='plain'))
