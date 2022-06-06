## Run an if/else statement that prints when the condition is true
talking_heads = ['David Byrne', 'Tina Weymouth', 'Chris Frantz', 'Jerry Harrison' ]
if 'Tina Weymouth' in talking_heads:
    print("Ya man")
else:
    print("nah man")

## Run if/else that prints when false
if 'David Bowie' in talking_heads:
    print("Ya man")
else:
    print("nah man")

## Use the elif/else keywords within an if statement
if 'Bernie Worrell' in talking_heads:
    print('Sick, I love that guy')
elif 'Alex Weir' in talking_heads:
    print('That guy rules at guitar')
else:
    best_lineup = talking_heads + ['Bernie Worrell', 'Alex Weir']
    print('The best Talking Heads lineup is:')
    for i in best_lineup:
        print(i)

## Execute a nested if statement
bandmate = 'Helen of Troy'
instrument = 'Guitar'
if bandmate in talking_heads:
    if instrument == 'Guitar':
        print('Yeah that guy/girl plays ' + instrument)
else:
    print('Are you some kind of nerd who thinks ' + bandmate + ' is in Talking Heads?')


## run a condition in an if statement/use the bool() and isinstance() functions
boolean = True
if isinstance(boolean, bool) and bool(boolean):
    print("I guess it must be true")

