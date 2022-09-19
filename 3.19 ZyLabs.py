import math

height = int(input('Enter wall height (feet):'))

width = int(input('\nEnter wall width (feet):'))

area = height * width
paint_needed = area / 350
cans = int(math.ceil(paint_needed))

print('\nWall area: ' + str(int(round(area))), 'square feet')

print('Paint needed: %.2f gallons' % paint_needed)

print('Cans needed: ' + str(cans) + ' can(s)')

color = input('\nChoose a color to paint the wall:')
if color == 'red':
    cost = 35 * cans
elif color == 'blue':
    cost = 25 * cans
elif color == 'green':
    cost = 23 * cans
else:
    cost = 0

print('\nCost of purchasing', color, 'paint: $' + str(cost))
