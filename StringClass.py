import string


class StringClass:
    def __init__(self,str):
        self.str=str

    def length(self):
        print(len(self.str))


    def stringToListChar(self):

        self.str = self.str.split()
        list1 = list(map(list, self.str))
        print(list1)


str=StringClass("Hello")
str.length()
str.stringToListChar()

