from random import randint
from ascii_magic import AsciiArt

class User:
    id_counter = 1

    def __init__(self, username, password):
        self.id = User.id_counter
        User.id_counter += 1
        self.username = username
        self.__password = password # private variable
        self.image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{randint(1,150)}.png"

    def __str__(self):
        return self.username

    def __repr__(self):
        return f"<User {self.id}|{self.username}>"

    # Method that will take in a password guess and return True if it matches the "private" password, else False 
    def check_password(self, password_guess):
        return self.__password == password_guess

    # Method that will print the User's image to the terminal
    def display_image(self):
        prof_image = AsciiArt.from_url(self.image_url)
        prof_image.to_terminal()


class Post:
    id_counter = 1

    def __init__(self, title, body, author):
        """
        title: str
        body: str
        author: User
        """
        self.id = Post.id_counter
        Post.id_counter += 1
        self.title = title
        self.body = body
        self.author = author

    def __str__(self):
        return f"""
        {self.id} - {self.title}
        By: {self.author}
        {self.body}
        """
    
    def __repr__(self):
        return f"<Post {self.id}|{self.title}>"
