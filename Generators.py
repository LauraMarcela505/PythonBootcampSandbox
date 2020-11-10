# Generators

# without Generator

def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result

for x in create_cubes(10):
    print(x)

print(create_cubes(4)) # output: [0, 1, 8, 27]

# with Generator

def create_cube(n):
    for x in range(n):
        yield x**3

for x in create_cube(10):
    print(x)

print(create_cube(4)) # output: <generator object create_cube at 0x02EFB4C0>

# both will end up having the same output, but the one with the generator is more memory efficient

c = create_cube(2)

print(next(c)) # this is how you can iterate through it even though it doesn't have a list -
print(next(c))


# iter

s = "hello"

for letter in s:
    print(letter)

s_iter = iter(s) # have to add iter in order to use the "next"
print(next(s_iter)) # output: h

