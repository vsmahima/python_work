class House:
    owner="Mahiama"
    def rooms(self):
        print("2 rooms")
    def hall(self):
        print("1 rooms")
class Home(House):
    pass
obj=Home()
obj.rooms()
print(obj.owner)