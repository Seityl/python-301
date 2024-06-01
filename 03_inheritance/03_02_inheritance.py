# CLASSES AND INHERITANCE
# =======================
# 1) Define an empty `Movie()` class.
# 2) Add a dunder init method that takes two arguments `year` and `title`
# 3) Create a sub-class called `RomCom()` that inherits from the `Movie()` class
# 4) Create another sub-class of the `Movie()` class called `ActionMovie()`
#     that overwrites the dunder init method of `Movie()` and adds another
#     instance variable called `pg` that is set by default to the number `13`.
# 5) Practice planning out and flushing out these classes even more.
#     Take notes in your notebook. What other attributes could a `Movie()` class
#     contain? What methods? What should the child classes inherit as-is or overwrite?

class Movie:
    """Defines a movie."""
    def __init__(self, year, title):
        self.year = year
        self.title = title

    def __str__(self) -> str:
        return f"Movie(year={self.year}, title={self.title})"

class RomCom(Movie):

    """Defines a RomCom movie."""
    def __init__(self, year, title, length):
        self.year = year
        self.title = title
        self.genre = "RomCom"
        self.length = length
        self.pg = 13
        
    def __str__(self):
        return f"RomCom(year={self.year}, title={self.title}, genre={self.genre}, length={self.length}, pg={self.pg})"

class ActionMovie(Movie):

    """Defines an Action movie."""
    def __init__(self, year, title, length):
        self.year = year
        self.title = title
        self.genre = "Action"
        self.length = length
        self.pg = 18
        
    def __str__(self):
        return f"ActionMovie(year={self.year}, title={self.title}, genre={self.genre}, length={self.length}, pg={self.pg})"

m1 = Movie(2024, "My Movie")
print(m1)
r1 = RomCom(m1.year, m1.title, 120)
print(r1)
r1 = ActionMovie(m1.year, m1.title, 120)
print(r1)