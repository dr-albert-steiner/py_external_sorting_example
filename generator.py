import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument("--row_count", default=1000, type=int)
parser.add_argument("--max_row_length", default=200, type=int)
parser.add_argument("--available_ram", default=1024 * 1024 * 10, type=int)

args = parser.parse_args()
row_cnt = args.row_count
max_row_len = args.max_row_length
available_ram = args.available_ram

chars = "1234567890abcdefghijklmnoprstyqwxz "

with open("sample_data", "w") as f:
    buffer = []
    buffer_size = 0
    for i in range(row_cnt):
        line = "".join(random.choices(chars, k=random.randint(1, max_row_len))) + "\n"
        buffer_size += len(line)
        if buffer_size >= available_ram:
            print(buffer_size)
            f.writelines(buffer)
            buffer.clear()
            buffer_size = 0
    if buffer_size > 0:
        f.writelines(buffer)
