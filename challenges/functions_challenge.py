## create a function / execute format() method
talking_heads = {'Vocals': 'David Byrne', 'Bass': 'Tina Weymouth', 'Drums': 'Chris Frantz', 'Guitar': 'Jerry Harrison'}
depeche_mode = {'Vocals': ['Martin Gore', 'Dave Gahan'], 'Keyboards': ['Andy Fletcher', 'Martin Gore']}
radiohead = ['Thom Yorke', 'Jonny Greenwood', "Ed O'Brien", 'Phil Selway', 'Colin Greenwood']

def who_plays(instrument, band):
    if instrument not in band:
        print('No one plays {}'.format(instrument))
        return
    members = band[instrument]
    if isinstance(members, list):
        print(', '.join(members))
    else:
        print(members)
        
## call a function
who_plays('Keyboards', depeche_mode)
who_plays('Bass', talking_heads)

## create an array
radiohead = ['Thom Yorke', 'Jonny Greenwood', "Ed O'Brien", 'Phil Selway', 'Colin Greenwood']

## loop through elements of the array using a for loop
for member in radiohead:
    print(member + ' seems angsty')

## Use the count() method on an array
print(radiohead.count('Thom Yorke'))

## Use the sort() method on an array
radiohead.sort()
print(radiohead)

## Create a lambda function
more_greenwoods = lambda person: person + ' Greenwood'
print(more_greenwoods('Jimzo'))

## Execute a format() function
print('This is {0:b} in binary'.format(75))

## function assignment
def getTwo(num1, num2):
    answer = num1 + num2
    print('The answer is {}'.format(answer))

getTwo(2, 4)
myAdd = getTwo

myAdd(2, 4)
