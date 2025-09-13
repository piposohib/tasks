from book import book
from member import member
from  staffmember import staff_member
book1 = book("zekola", "D.ahmed khaled twfeek", "9780743273565", True)
member1 = member("sohib", "M12345", ["zekola", "amareta"])
staff1 =  staff_member("S001", True)
print(book1.title)
print(book1.author)
print(book1.isbn)
print(book1.is_available())
print(member1.name)
print(member1.membership_id)
print(member1.borrowed_books)
print(staff1.staff_id)
print(staff1.add_book)
