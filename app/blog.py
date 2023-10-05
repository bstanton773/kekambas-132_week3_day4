from app.models import User

class Blog:
    def __init__(self):
        self.users = []
        self.posts = []
        self.current_user = None

    # Method to a create a new user instance and add to the Blog's user list
    def create_new_user(self):
        # Get user info from input
        username = input('Please enter a username: ')
        # Check to see if a user with that username already exists
        if username in [u.username for u in self.users]:
            print(f"User with the username {username} already exists.")
        else:
            password = input('Please enter a password: ')
            # Create a new instance of User with the inputted info
            new_user = User(username, password)
            # Add the new user to the blog's user list
            self.users.append(new_user)
            print(f"{new_user} has been created.")

    # Method to log a user in by setting the current_user to a User instance
    def log_user_in(self):
        # Get the user credentials via input
        username = input('What is your username? ')
        password = input('What is your password? ')
        # Loop through the blog's user list
        for user in self.users:
            # Check if that user's username and password match the inputs
            if user.username == username and user.check_password(password):
                # If both are True, set the blog's current user to that user
                self.current_user = user
                print(f'{user} has logged in.')
                # Once we find the right user, we don't need to search any more
                break
        # if we go through the for loop without breaking, we know we have invalid credentials
        else:
            print('Username and/or password is incorrect.')

    # Method to log a user out by setting the current_user to None
    def log_user_out(self):
        username = self.current_user.username
        self.current_user = None
        print(f'{username} has successfully logged out')
