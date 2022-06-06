
## Assign string to a variable
beer = 'Samuel Adams'

## Assign a multiline string to a variable.
poe_quote = """Filled with mingled cream and amber,
            I will drain that glass again.
            Such hilarious visions clamber
            Through the chamber of my brain.
            Quaintest thoughts, queerest fancies
            Come to life and fade away.
            What care I how time advances;
            I am drinking ale today."""

## Return a range of characters by using the slice syntax.
snippet = poe_quote[0:50]

## Use the len() function.
poe_length = len(poe_quote)

## Use the strip() method.
beer2 = "xxxxxxx.....Samuel Adamsllllllpppp"
stripped = beer2.strip("x.lp")

## Use the upper() method.
BEER = beer.upper()

## Use the in or not in keyword
print('Samuel' in beer)
print('Radams' not in beer)

## Concatenate a string
two_sams = beer + " " + stripped

## Use an escape character
aytoun_quote = "The Empty Bottle: \"Ah, liberty! how like thou art to this large bottle lying here\""

