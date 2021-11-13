print ('>> Mohit Namdeo')
print ('>> Check the File Size')

('Using os module')
import os

file_stat = os.stat('my_file.txt')
print(file_stat.st_size)

('Using pathlib module')
from pathlib import Path

file = Path('my_file.txt')
print(file.stat().st_size)