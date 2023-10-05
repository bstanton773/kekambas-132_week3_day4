from app import Blog


def run_blog():
    print("Welcome to the Kekambas Blog!")
    # Create an instance of the Blog class
    blog = Blog()
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
            

    # Once the user quits
    print('Thanks for checking out the blog.')
    print(blog.users)
    print(blog.posts)
    print('Goodbye!')
        
    

if __name__ == "__main__":
    run_blog()
