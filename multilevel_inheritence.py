class Grandfather:
    def skill1(self):
        print("Developer")
class Mother(Grandfather):
    def skill2(self):
        print("Cook")
class Child(Mother):
    def skill3(self):
        print("AI developer")
val=Child()
val.skill1()
val.skill2()
val.skill3()