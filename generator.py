import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument("--row_count", default=1000, type=int)
parser.add_argument("--max_row_length", default=200, type=int)
parser.add_argument("--available_ram", default=1024 * 1024 * 100, type=int)  # 100 mb
parser.add_argument("--output", default="sample_data", type=str)

args = parser.parse_args()
row_cnt = args.row_count
max_row_len = args.max_row_length
available_ram = args.available_ram
out_file = args.output

chars = "1234567890abcdefghijklmnoprstyqwxz "

with open(out_file, "w+") as f:
    f.truncate()
    buffer = []
    buffer_size = 0
    for i in range(row_cnt):
        line = "".join(random.choices(chars, k=random.randint(1, max_row_len))) + "\n"
        buffer.append(line)
        buffer_size += len(line)
        if buffer_size >= available_ram:
            f.writelines(buffer)
            buffer.clear()
            buffer_size = 0

    if buffer_size > 0:
        f.writelines(buffer)
