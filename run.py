from app import Blog
from app.models import Post, User


def run_blog():
    print("Welcome to the Kekambas Blog!")
    # Create an instance of the Blog class
    blog = Blog()

    # CREATE SOME INITIAL DATA
    user1 = User('brians', 'abc123')
    user2 = User('jumpman23', '6rings')
    blog.users.append(user1)
    blog.users.append(user2)
    post1 = Post('Fri-yay!', 'It is Friday, hooray!', user1)
    post2 = Post('Weekend', 'I am ready for the weekend', user2)
    blog.posts.append(post1)
    blog.posts.append(post2)

    # Start "running" our blog until the user quits
    while True:
        if blog.current_user is None:
            # print our menu options
            print("1. Sign Up\n2. Log In\n3. View All Posts\n4. View Single Post\n5. Quit")
            # Ask the user what they would like to do
            to_do = input('Which option would you like to do? ')
            # While the user inputs an invalid option
            while to_do not in {'1', '2', '3', '4', '5'}:
                # redefine to_do with a new input
                to_do = input('Invalid option. Please choose 1, 2, 3, 4, or 5: ')
            # Different "Routes" - different options for what to do
            if to_do == '5':
                break
            elif to_do == '1':
                # Call the create new user method on the blog
                blog.create_new_user()
            elif to_do == '2':
                # Call the log user in function
                blog.log_user_in()
            elif to_do == '3':
                blog.view_posts()
            elif to_do == '4':
                post_id = input('What is the ID of the post you would like to view? ')
                # If the post is not a digit, re-ask the question
                while not post_id.isdigit():
                    post_id = input('Invalid ID. Must be an interger. Please enter ID again: ')
                # Call the view single post method with the integer version of post_id
                blog.view_post(int(post_id))
            else:
                print(f'Option {to_do} is a work in progress!')
        else:
            # print menu options for a logged in user
            print("1. Sign Out\n2. Create A Post\n3. View All Posts\n4. View Single Post\n5. Edit A Post\n6. Delete A Post")
            # Ask the user what they would like to do
            to_do = input('Which option would you like to do? ')
            # While the user inputs an invalid option
            while to_do not in {'1', '2', '3', '4', '5', '6'}:
                # redefine to_do with a new input
                to_do = input('Invalid option. Please choose 1, 2, 3, 4, 5, or 6: ')
            if to_do == '1':
                blog.log_user_out()
            elif to_do == '2':
                blog.create_new_post()
            elif to_do == '3':
                blog.view_posts()
            elif to_do == '4':
                post_id = input('What is the ID of the post you would like to view? ')
                # If the post is not a digit, re-ask the question
                while not post_id.isdigit():
                    post_id = input('Invalid ID. Must be an interger. Please enter ID again: ')
                # Call the view single post method with the integer version of post_id
                blog.view_post(int(post_id))
            elif to_do == '5':
                post_id = input('What is the ID of the post you would like to edit? ')
                # If the post is not a digit, re-ask the question
                while not post_id.isdigit():
                    post_id = input('Invalid ID. Must be an interger. Please enter ID again: ')
                blog.edit_post(int(post_id))
            elif to_do == '6':
                post_id = input('What is the ID of the post you would like to delete? ')
                # If the post is not a digit, re-ask the question
                while not post_id.isdigit():
                    post_id = input('Invalid ID. Must be an interger. Please enter ID again: ')
                blog.delete_post(int(post_id))
            

    # Once the user quits
    print('Thanks for checking out the blog.')
    print(blog.users)
    print(blog.posts)
    print('Goodbye!')
        
    
# If this file is executed by name (as opposed to imported), call the run_blog function
if __name__ == "__main__":
    run_blog()
