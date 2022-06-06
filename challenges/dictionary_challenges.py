
## Create a dictionary
talking_dictionary = { 'Vocals': 'David Byrne', 'Bass': 'Tina Weymouth', 'Drums': 'Chris Frantz', 'Guitar': 'Jerry Harrison' }

## Use the get() method
print(talking_dictionary.get('Drums'))

## Change a  value within the dictionary
talking_dictionary['Guitar'] = 'Alex Weir'
print(talking_dictionary.get('Guitar'))

## Add an item to a dictionary
talking_dictionary['Keyboard'] = 'Bernie Worrell'
print(talking_dictionary.get('Keyboard'))

## Create a nested dictionary
talking_dictionary['Guitar'] = { 'Stop Making Sense': 'Alex Weir', 'Remain In Light': 'Jerry Harrison' }
print(talking_dictionary['Guitar']['Remain In Light'])

## Use the fromkeys() method
band_blueprint = ('Guitar', 'Bass', 'Drums', 'Vocals', 'Keyboard')
band_template = dict.fromkeys(band_blueprint)
print(band_template)
