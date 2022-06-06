## Create a set
talking_set = { 'David Byrne', 'Tina Weymouth', 'Chris Frantz', 'Jerry Harrison' }

## add item to set with add()
talking_set.add('Bernie Worrell')
print(talking_set)

## Use remove() to take an item out of the set
talking_set.remove('Bernie Worrell')
print(talking_set)

## use the difference() method on a set
tom_tom_set = { 'Tina Weymouth', 'Chris Frantz', 'Mystic Bowie', 'Victoria Clamp' }
not_heads = tom_tom_set.difference(talking_set)
print(not_heads)
