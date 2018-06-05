'''
Created on Jun 5, 2018

@author: shiwamsingh
'''
squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

squares = list(map(lambda x: x**2, range(10)))
print(squares)

squares = [x**2 for x in range(10)]
print(squares)


combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

print(combs)

combs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(combs)


vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
doubled = [x*2 for x in vec]
print(doubled)

# filter the list to exclude negative numbers
positives = [x for x in vec if x >= 0]
print(positives)

# apply a function to all the elements
absolute = [abs(x) for x in vec]
print(absolute)

# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
stripped = [weapon.strip() for weapon in freshfruit]
print(stripped)

# create a list of 2-tuples like (number, square)
doubles = [(x, x**2) for x in range(6)]
print(doubles)

# the tuple must be parenthesized, otherwise an error is raised
#doubles = [x, x**2 for x in range(6)]




# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
print(vec)
vec = [num for elem in vec for num in elem]
print(vec)