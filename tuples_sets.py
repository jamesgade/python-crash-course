# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.


# Create Tuple

fruits = ('Apples', 'Oranges',  'Grapes');  print(type(fruits), ' fruits :', fruits);
fruits2 = ('Kiwi', 'Papaya',  'Melon');  print(type(fruits2), ' fruits2 :', fruits2);
withConstructor = tuple(('Apples', 'Oranges', 'Grapes'));  print(type(fruits),' withConstructor :', withConstructor)

# If tuple has one value, leave trailing comma
withoutTrailingComma = ('Apples');  print(type(withoutTrailingComma), ' withoutTrailingComma : ', withoutTrailingComma) # not tuple
withTrailingComma = ('Apples',);  print(type(withTrailingComma), ' withTrailingComma : ', withTrailingComma)    # tuple

# access tuple value with index
print(fruits[1])

#  'tuple' object does not support item assignment
# fruits2[0] = 'Banana'


# delete a tuple
print('fruits2 :', fruits2)
del fruits2;
# print('fruits2 :', fruits2) # name 'fruits2' is not defined


# length of tuple
print(len(fruits))      # 3





# A Set is a collection which is unordered and unindexed. No duplicate members.

# create set

fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if Item is in set
print('Apples' in fruits_set)

# add to set

