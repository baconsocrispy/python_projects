# use the range function with one parameter to display 0 1 2 3
for num in range(4):
  print(num)

# use the range function with 3 params to display 3 2 1 0
nums = []
for num in range(3, -1, -1):
  nums += [num]
print(*nums)

# use the range function with 3 params to display 8 6 4 2
nums = []
for num in range(8, 0, -2):
  nums += [num]
print(*nums)

