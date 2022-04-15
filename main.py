import csv

NOTE_MIN = 0
NOTE_MAX = 20
K = 3
DATA_FILENAME = 'data.csv'
SAMPLE_DATA = [14.84,14.14,16.22,86,85,85,14.84,13,15.85,9.99,12.04,15.03,16.22,12,84,10.20,11.03,11.03]

try:
    with open(DATA_FILENAME, 'r') as file:
        read = csv.reader(file)
        moyennes = []
        data = list(read)[0]

        for i in range(len(data)):
            try:
                valid_data = float(data[i])
                moyennes.append(valid_data)
            except ValueError:
                pass

except (FileNotFoundError, IndexError):
    moyennes = SAMPLE_DATA

(moyennes := [value for value in moyennes if NOTE_MIN <= value <= NOTE_MAX]).sort()

print(f'Les {K} plus basses moyennes sont  {moyennes[:K]}')
print(f'Les {K} plus hautes moyennes sont  {moyennes[-K:]}')