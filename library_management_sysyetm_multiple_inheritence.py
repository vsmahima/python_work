#Create a multiple inheritence library management system, where class book details and Member
#memberdetails ae inherited by Library transaction to manage book issue records
class BookDetails:
    def __init__(self,name,author,year,copy):
        self.bname=name
        self.author=author
        self.year=year
        self.copy=copy
    def book_display(self):
        print(f"Book Name: {self.bname}")
        print(f"Author: {self.author}")
        print(f"No: of copies: {self.copy}") 
        print(f"Year of publication: {self.yeaar}")
    def store_books(self)
        self.temp=({self.bname:[self.author,self.copy,self.year]})
        return self.temp
class MemberDetails:
        def __init__(self,id,name,date,book_issued):
            self.mem_id=id
            self.mem_name=name
            self.join_date=date
            self.book_issued=book_issued
class LibraryTransaction(BookDetails,MemberDetails):
     def display(self):
          print(self.copy)

obj=LibraryTransaction('aa','bb','cc',21)
obj.display()
#.............ADDING BOOK DETAILS.......
details={}
while True:
    bobj=BookDetails()
    bname=input("Enter book name: ")
    bauthor=input("Enter Author name: ")
    byear= input("Enter year of publication: ")
    bcopy=int(input("No: of copies: "))
    bobj=BookDetails(bname,bauthor,byear,bcopy)
    
    details=details.update()
    ch=input("Do you want to add more Books Details (y|n):")
    if(ch.lower()=='n'):
         break




          

                   