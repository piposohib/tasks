from member import member
class staff_member(member):
    def __init__(self , staff_id  , add_book):
        self.staff_id = staff_id
        self.add_book = add_book