
# Opening a file in python
# file = open('sample.txt', 'r').read()
# print(file)

# file = open('sample.txt', 'r').readlines()
# print(file)

# file = open('sample.txt', 'r').read().split()
# ans = []
# for word in file:
#     ans.append(word)
# print(ans)

# with open('sample.txt', 'a') as file:
#     file.write('\nThis is a new line')

file = open('sample.txt', 'a').write('\tThis is another new line')