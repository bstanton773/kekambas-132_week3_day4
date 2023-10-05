from app import Blog


def run_blog():
    print("Welcome to the Kekambas Blog!")
    # Create an instance of the Blog class
    blog = Blog()
    # Start "running" our blog until the user quits
    while True:
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
        else:
            print(f'Option {to_do} is a work in progress!')

    # Once the user quits
    print('Thanks for checking out the blog.')
    print(blog.users)
    print(blog.posts)
    print('Goodbye!')
        
    

if __name__ == "__main__":
    run_blog()
