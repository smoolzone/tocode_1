import glob
import os.path

all_files = glob.glob('*.*')
print(all_files)


counter = {}

for filename in all_files:
    _, ext = os.path.splitext(filename)
    try:
        counter[ext] += 1
    except KeyError:
        counter[ext] = 1
print(counter)