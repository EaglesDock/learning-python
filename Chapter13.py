>>> class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]

    def change_data(self, index, n):
        self.nums[index] = n

>>> data_one = Data()
>>> data_one.nums[0] = 100
>>> print(data_one.nums)
[100, 2, 3, 4, 5]

>>> data_two = Data()
>>> data_two.change_data(0, 100)
>>> print(data_two.nums)
[100, 2, 3, 4, 5]

##Class Data, Data is the object.
##Def is defining it, __init__ is initializing it.
##the variables is held in a list.
##Change_data is a method.
