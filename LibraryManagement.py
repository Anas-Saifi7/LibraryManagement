class Library:
  def __init__(self):
    self.noBooks = 0
    self.books = []

  def addBook(self, book):
    self.books.append(book)
    self.noBooks = len(self.books)

  def showDetails(self):
    print(f"The library has {self.noBooks} books. The books are{self.books}")

l1 = Library()
l1.addBook("English")
l1.addBook("Maths")
l1.addBook("Hindi")
l1.addBook("Urdu")
l1.showDetails()
   
  