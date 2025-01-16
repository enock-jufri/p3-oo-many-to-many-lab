class Author:
    all=[]
    def __init__(self,name):
        self.name= name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author==self]
    def books(self):
        return [contract.book for contract in Contract.all if contract.author==self]

    def sign_contract(self,book,date,royalties):
        return Contract(self,book,date,royalties)
    
    def total_royalties(self):
        return sum([contract.royalties for contract in Contract.all if contract.author == self])
class Book:
    all=[]
    def __init__(self,title):
        self.title=title
        
    def contracts(self):
        return [contract for contract in Contract.all if contract.book==self]
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book ==self]
    
class Contract:
    all=[]
    def __init__(self,author,book,date,royalties):
        self.author=self.set_author(author)
        self.book=self.set_book(book)
        self.date=self.set_date(date)
        self.royalties=self.set_royalties(royalties)
        Contract.all.append(self)
        
    def set_author(self,author):
        if isinstance(author,Author):
            return author
        else:
            raise TypeError("author not of Author")
        
    def set_book(self,book):
        if isinstance(book,Book):
            return book
        else:
            raise TypeError("book not of Book")
    def set_date(self,date):
        if isinstance(date,str):
            return date
        else:
            raise TypeError("date not a string")
    
    def set_royalties(self,royalties):
        if isinstance(royalties,int):
            return royalties
        else:
            raise TypeError("royalties not an integer")
        
    @classmethod
    def contracts_by_date(cls,date):
        return [contract for contract in Contract.all if contract.date ==date]
        
        
Contract.all = []
author1 = Author("Name 1")
book1 = Book("Title 1")
book2 = Book("Title 2")
book3 = Book("Title 3")
author2 = Author("Name 2")
book4 = Book("Title 4")
contract1 = Contract(author1, book1, "02/01/2001", 10)
contract2 = Contract(author1, book2, "01/01/2001", 20)
contract3 = Contract(author1, book3, "03/01/2001", 30)
contract4 = Contract(author2, book4, "01/01/2001", 40)