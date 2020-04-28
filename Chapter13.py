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
##data_one variable uses the nums to change it.
##
>>> data_three = Data()
>>> data_three.nums[1] = 200
>>> print(data_three.nums)
[1, 200, 3, 4, 5]
>>> print(data_two.nums)
[100, 2, 3, 4, 5]
#it means the nums is static? and data_one and data_two and data_three
#its difficult trying to understand the terminology aswel as actually learn the coding + the syntax of it + Practicallity of it.

>>> data_two = Data()
>>> data_two.change_data(0, 100)
>>> print(data_two.nums)
[100, 2, 3, 4, 5]
#Would printing data_two differ to printing data_one?
>>> print(data_one)
<__main__.Data object at 0x0352B3E8>
##That does not work
>>> print(data_one.nums)
[100, 2, 3, 4, 5]
#Lets change data_two
#Check on data_two:
>>> print(data_two.nums)
[100, 2, 3, 4, 5]
##change data_two
>>> data_two.change_data(1, 200)
>>> print(data_two.nums)
[100, 200, 3, 4, 5]
##Using the syntax by changing the first number to the original which was 1.
>>> data_two.change_data(0, 1)
>>> print(data_two.nums)
[1, 200, 3, 4, 5]
#Worked.
#Change_data is backed up by the original code on line5 and 6. which is a method.

