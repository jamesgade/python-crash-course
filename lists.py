# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers = [1,2,3,4,5]
numbers2 = list((1,2,3,4,5))                                                                        # using constructor
fruits = ['Apple', 'Papaya', 'Grapes']

print(numbers, numbers2)                        # [1, 2, 3, 4, 5] [1, 2, 3, 4, 5]

print(fruits[1])                                # Papaya                                            # get a value

print(len(fruits))                              # 3                                                 # get number of items in list

fruits.append('Mangoes');  print(fruits)        # ['Apple', 'Papaya', 'Grapes', 'Mangoes']          # Append to list

fruits.remove('Grapes'); print(fruits)          # ['Apple', 'Papaya', 'Mangoes']                    # remove from list

fruits.insert(2, 'Strawberry'); print(fruits)   # ['Apple', 'Papaya', 'Strawberry', 'Mangoes']      # insert into position

fruits[0] = 'Blueberry'; print(fruits)          # ['Blueberry', 'Papaya', 'Mangoes']                # change value in position

fruits.pop(2); print(fruits)                    # ['Blueberry', 'Papaya', 'Mangoes']                # remove from position

fruits.reverse(); print(fruits)                 # ['Mangoes', 'Papaya', 'Blueberry']                # reverse list

fruits.sort(); print(fruits)                    # ['Blueberry', 'Mangoes', 'Papaya']                # sort list alphabetically

fruits.sort(reverse=True); print(fruits)        # ['Papaya', 'Mangoes', 'Blueberry']                # sort list alphabetically reverse


