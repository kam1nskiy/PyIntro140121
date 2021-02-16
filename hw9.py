# names = []
# for i in open('/Users/kaminskyi/PycharmProjects/PyIntro140121/names.txt'):
#     names.append(i[:-1])
#     print(names)
from typing import List



# with open('/Users/kaminskyi/PycharmProjects/PyIntro140121/names.txt', 'r') as f:
#     nums = f.read().splitlines()
# print(nums)

# with open('/Users/kaminskyi/PycharmProjects/PyIntro140121/names.txt', 'r') as f:
#     for eachLine in f:
#         a = eachLine.strip().split()
#         l = list(int(x) for x in a[2][1:-1].replace(',',""))
#         print(l)

lines = [line.rstrip('\n') for line in open('/Users/kaminskyi/PycharmProjects/PyIntro140121/names.txt')]
print(lines)