import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument("--row_count", default=1000, type=int)
parser.add_argument("--max_row_length", default=200, type=int)

args = parser.parse_args()
row_cnt = args.row_count
max_row_len = args.max_row_length

chars = "1234567890abcdefghijklmnoprstyqwxz "
with open("sample_data", "w+") as f:
    f.truncate()
    for row in range(row_cnt):
        f.write("".join(random.choices(chars, k=random.randint(1, max_row_len))) + ("\n" if row < row_cnt - 1 else ""))
