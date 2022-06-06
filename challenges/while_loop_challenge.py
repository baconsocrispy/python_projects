## Execute a while loop, use the break/continue/else statements
talking_heads = ['David Byrne', 'Tina Weymouth', 'Chris Frantz', 'Jerry Harrison']

i = 0
while i < len(talking_heads):
    if talking_heads[i] == 'Chris Frantz':
        break
    elif talking_heads[i] == 'David Byrne':
        i += 1
        continue
    else:
        print(talking_heads[i])
        i += 1

## Execute a for loop, use break/continue/else statements
## and the range() function

for i in range(len(talking_heads)):
    if talking_heads[i] == 'Tina Weymouth':
        print('Tina is the bass player')
        i += 1
    elif talking_heads[i] == 'Jerry Harrison':
        break
    else:
        i += 1
        continue

