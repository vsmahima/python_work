#Create multiple book Object and display all book name and authors
class Book:
    def __init__(self,name,author):
        self.bname=name
        self.bauthor=author
        pass
    def book_details_store(self):
        self.details={}
        self.details.update({self.bname:self.bauthor})
        # print(f"Book Name: {self.bname}")
        # print(f"Author: {self.bauthor}")
        return self.details
    # def book_details_print(self):
    #     print(self.details)
book_detail={}
for i in range(1,5):
    book_name=input("Enter book name: ")
    book_author=input("Enter author name: ")
    book_obj=Book(book_name,book_author)
    temp= book_obj.book_details_store()
    book_detail.update(temp)
    #print("vlue=",temp)
print("Book and Authors:")
print(book_detail)
  


