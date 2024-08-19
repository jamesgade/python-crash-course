# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'James'
age = 23

# Concatenate
print('Hello, my name is ' + name + ' and I am ' + str(age))            # Hello, my name is James and I am 23

# String Formatting

# Arguments by position
print('My name is {name} and I am {age}'.format(name=name, age=age))    # My name is James and I am 23

# F-strings (3.6+)  
print(f'Hello, This is {name} and I am {age} years old')                # Hello, This is James and I am 23 years old

# String Methods

a = 'hello world'


print(a.capitalize())                    # Hello world                    # Capitalize string
print(a.upper())                         # HELLO WORLD                    # make all uppercase
print(a.lower())                         # hello world                    # make all lowercase
print(a.swapcase())                      # HELLO WORLD                    # swap case
print(len(a))                            # 11                             # get length
print(a.replace('world', 'everyone'))    # hello everyone                 # replace
print(a.count('l'))                      # 3                              # count of a character
print(a.startswith('he'))                # True                           # starts with
print(a.endswith('dl'))                  # False                          # ends with
print(a.split())                         # ['hello', 'world']             # split string into list
print(a.find('w'))                       # 6                              # find position
print(a.isalnum())                       # False                          # is all alpha-numeric (false due to space)                    
print(a.isalpha())                       # False                          # is all alphabetic (false due to space)
print(a.isnumeric())                     # False                          # is all numeric
