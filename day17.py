from aocd import data

data = int(data)
print(data)
buffer = [0]

position = 0
for x in range(1,2018):
    position = ((position+data)%len(buffer))+1
    buffer.insert(position, x)

print(position+1)

buffer_len=1
position=0
val_at_loc_1 =  -1
for x in range(1, 50000000):
    position = ((position + data) % buffer_len) + 1
    if position==1:
        val_at_loc_1 = x
    buffer_len += 1

print(val_at_loc_1)


