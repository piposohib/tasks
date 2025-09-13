class book :
    def __init__(self , title , author , isbn , available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available
    def is_available(self):
        if self.available == True:
            return True
        else:
            return False