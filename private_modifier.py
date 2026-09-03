class Student:
    def __init__(self):
        self.name="Mahima"
        self._age=35   #protected
        self.__gender="F"  #private
    def _display1(self):
        print("Scope India TVM")
    def __display2(self):   ###private method
            print("Scope India NGL")
    def display(self):
            print("Scope India")
            self.__display2()
obj=Student()
obj._display1()
obj.display()
