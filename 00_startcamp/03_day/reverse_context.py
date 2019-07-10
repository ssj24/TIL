"""
0
1
2
3
quest.txt를
3
2
1
0
reverse_quest.txt로 저장하시오
#1. 읽고
with open('quest.txt', 'r') as f:
    lines = f.readlines()
    #print(lines)
#2. 뒤집고
    lines.reverse()
#3. 작성하고
with open('reverse_quest.txt', 'w') as f:
    for line in lines:
        f.write(line)
OR
with open('reverse_quest.txt', 'w') as f:
    f.writelines()
"""

with open('quest.txt', 'w') as f:
    for i in range(0, 4):
        f.write(f'{i}\n')

with open('quest.txt', 'r') as f:
    lines = f.readlines()
    lines.reverse()
    # for line in lines:
    #     print(line.strip())
   
with open('reverse_quest.txt', 'w') as f:
    for line in lines:
        f.write(line)


