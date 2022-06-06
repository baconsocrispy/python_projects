## Create a list
talking_heads = ['David Byrne', 'Tina Weymouth', 'Chris Frantz', 'Jerry Harrison']

## Loop through list with for loop
for i in talking_heads:
    print(i)

## Use append() method
talking_heads.append('Bernie Worrell')
print(talking_heads[-1])

## Make a copy of a list
new_heads = talking_heads.copy()
print(new_heads[1])

## Concatenate two lists
concat_heads = new_heads + talking_heads
print(concat_heads[8])

## Use the reverse() method
talking_heads.reverse()
print(talking_heads[0])
