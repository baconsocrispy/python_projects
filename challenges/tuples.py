## making changes to immutable tuple lists
animal = ('zebra', 'alligator', 'giraffe', 'goat', 'ox')

animals = list(animal)
print(animals)

animals.append('honey badger')
print(animals)

## making changes to immutable strings
string = "This is an example of a string"
new_string = list(string)
print(new_string)

new_string = string.split(" ")
print(new_string)

## Create a tuple and print it
talking_tuple = ('David Byrne', 'Tina Weymouth', 'Chris Frantz', 'Jerry Harrison')
print(talking_tuple)

## Loop through tuple with for loop
for i in talking_tuple:
    print(i)

## Use the count() method
david_count = talking_tuple.count('David Byrne')
print(david_count)
