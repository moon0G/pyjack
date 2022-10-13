import os

for x in os.listdir():
    print(f'"{x[:-4]}": ["{x}"],')
