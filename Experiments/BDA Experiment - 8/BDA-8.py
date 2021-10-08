import os
import time

def add_1(data, idx, max_key, cnt):
  data[0] = [[idx, cnt]] + data[0]
  current = 0
  while len(data[current]) > 2:
    assert len(data[current]) == 3
    buckets = data[current][-2:]
    data[current] = data[current][:1]
    current += 1

  if data.get(current, None) is None:
    data[current] = [buckets[0]]
    max_key = current
    # assert max_key == current
  else:
    data[current] = [buckets[0]] + data[current]
  return max_key 

def output_data(data, max_key):
  cnt = 0
  mul = 1
  for i in range(max_key + 1):
    # print(len(data[i]) * mul)
    cnt += len(data[i]) * mul
    mul *= 2
    print("DGIM Count:", cnt - mul // 4)
  return cnt - mul // 4

cnt = 0
idx = 0
bucket_dict = {0: []}
max_key = 0
window_size = 1000

start = time.time()
with open("C:\Users\ameyt\Downloads\stream_data_dgim.txt", "r") as f:
  while True:
    input_bit = f.read(1)
    if not input_bit:
      DGIM_count = output_data(bucket_dict, max_key)
      break
    if input_bit == "\t":
      continue
    if len(bucket_dict[0]) > 0 and idx == bucket_dict[max_key][-1][0]:
      bucket_dict[max_key] = bucket_dict[max_key][:-1]
      if len(bucket_dict[max_key]) == 0:
        bucket_dict.pop(max_key)
        max_key -= 1
    if input_bit == '1':
      max_key = add_1(bucket_dict, idx, max_key, cnt)
    cnt += 1
    idx = cnt % window_size

end = time.time()
print("DGIM Run Time(s): %.4f" % (end - start))
