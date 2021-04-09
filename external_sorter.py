import os
import heapq
import argparse
from math import ceil

parser = argparse.ArgumentParser()
parser.add_argument("--available_ram", default=1024 * 1024 * 100, type=int)  # 100mb default
parser.add_argument("--input", default="sample_data", type=str)
parser.add_argument("--output", default="sample_data_sorted", type=str)
args = parser.parse_args()

available_RAM = args.available_ram
input_file_path = args.input
output_file_path = args.output

chunks_cnt = 0
chunks = []

with open(input_file_path, 'r') as input_file:
    while True:
        chunk = input_file.readlines(available_RAM)
        if len(chunk) == 0:
            break
        chunk_name = f"{input_file_path}_chunk{chunks_cnt}"
        chunks.append(chunk_name)
        with open(chunk_name, "w") as chunk_file:
            chunk_file.writelines(sorted(chunk))
        chunks_cnt += 1

slice_size = ceil(available_RAM / (chunks_cnt + 1))
heap = []
opened_chunks = []
for chunk in chunks:
    opened_chunks.append(open(chunk))


def slice_chunks():
    found = True
    lns_cnt = 0
    while found:
        found = False
        for chunk_f in opened_chunks:
            line = chunk_f.readline()
            if line:
                lns_cnt += 1
                found = True
                yield line


with open(output_file_path, "w+") as output_f:
    output_f.truncate()
    buffer = []
    buffer_size = 0
    for id, item in enumerate(slice_chunks()):
        if id >= chunks_cnt:
            line = heapq.heappop(heap)
            buffer.append(line)
            buffer_size += len(line)

        if buffer_size >= available_RAM:
            output_f.writelines(buffer)
            buffer.clear()
            buffer_size = 0
        heapq.heappush(heap, item)
    while len(heap) > 0:
        buffer.append(heapq.heappop(heap))
    output_f.writelines(buffer)

for i in range(chunks_cnt):
    opened_chunks[i].close()
    os.remove(chunks[i])
