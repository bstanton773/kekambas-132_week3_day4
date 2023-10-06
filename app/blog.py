from app.models import User, Post

class Blog:
    def __init__(self):
        self.users = []
        self.posts = []
        self.current_user = None

    # Private Method that will get a post by its ID or return None if no post with that ID
    def _get_post_from_id(self, post_id):
        # Loop through all of the posts in the blog
        for post in self.posts:
            # If the post's ID matches the post_id arugment
            if post.id == post_id:
                # return the post instance
                return post
        # If we finish the loop, that means the post with that ID does not exist
        return None

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

    # Method to add a new post to the blog, authored by the logged in user
    def create_new_post(self):
        # Check to make sure we have a logged in user
        if self.current_user is not None:
            # Get the title and body for the new post from input
            title = input("Enter new post title: ")
            body = input("Enter new post body: ")
            # Create a new instance of Post with the inputted info + logged in user
            new_post = Post(title, body, self.current_user)
            # Add the new post to the blog's posts list
            self.posts.append(new_post)
            print(f"{new_post.title} has been created!")
        else:
            print("You must be logged in to perform this action") # 401 Unauthorized Status Code

    # Method to view all posts
    def view_posts(self):
        # Check if there are any posts
        if self.posts:
            # Loop through the blog's posts list
            for post in self.posts:
                # print the post (__str__ already formats it for us)
                print(post)
        else:
            print("There are currently no posts for this blog :( ")

    # Method to view a SINGLE post by ID
    def view_post(self, post_id):
        post = self._get_post_from_id(post_id)
        if post:
            print(post)
        else:
            print(f"Post with an ID of {post_id} does not exist") # 404 Not Found

    # Method to edit a post by ID
    def edit_post(self, post_id):
        post = self._get_post_from_id(post_id)
        if post:
            # Check to see if the logged in user is the author of the post
            if post.author == self.current_user:
                # print the post so the user can see what they are editing
                print(post)

                # Ask for the new title or have them skip to keep the current title
                new_title = input("Enter a new title or type 'skip' to keep the current title: ")
                if new_title.lower() != 'skip':
                    # Set the title attribute on the post to the new title
                    post.title = new_title

                # Ask for the new body or have them skip to keep the current body
                new_body = input("Enter a new body or type 'skip' to keep the current body: ")
                if new_body.lower() != 'skip':
                    # Set the body attribute on the post to the new body
                    post.body = new_body

                print(f'{post.title} has been updated!')
                
            # If the user is logged in but not the author
            elif self.current_user is not None:
                print("You do not have permission to edit this post.") # 403 Forbidden
            # If the user is not logged in at all
            else:
                print("You must be logged in to perform this action.") # 401 Unauthorized

        else:
            print(f"Post with an ID of {post_id} does not exist") # 404 Not Found

    # Method to delete a post by ID
    def delete_post(self, post_id):
        post = self._get_post_from_id(post_id)
        if post:
            # Check to see if the logged in user is the author of the post
            if post.author == self.current_user:
                print(post)

                # Ask if they are sure
                you_sure = input("Are you sure you want to delete this post? This action cannot be undone. Enter 'yes' or 'y' to delete ").lower()

                if you_sure == 'yes' or you_sure == 'y':
                    # Remove the post from the blog's posts list
                    self.posts.remove(post)
                    print(f"{post.title} has been removed")
                else:
                    print(f"Okay. We will not delete {post.title}")
                
            # If the user is logged in but not the author
            elif self.current_user is not None:
                print("You do not have permission to delete this post.") # 403 Forbidden
            # If the user is not logged in at all
            else:
                print("You must be logged in to perform this action.") # 401 Unauthorized

        else:
            print(f"Post with an ID of {post_id} does not exist") # 404 Not Found
