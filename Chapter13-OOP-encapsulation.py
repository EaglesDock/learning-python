class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.len = l


    def area(self):
        return self.width * self.len
      
      #Encapsulation code 
      #Objects group variables and methods too.
      #len and width hold objects state.
      #Object state grouped in the same unit? as method area, unit being object?
      #method uses objects state to return rectangle area.
      #method being area(self): on line 7.
      #
      
class Data: 
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]

    def change_data(self, index, n):
        self.nums[index] = n
        
#contains instance variables. which is nums. Nums contains a list of integers
#Object is data, created as a class, class = object.
#to change the items change_data METHOD. OR direct access to nums instance variable
