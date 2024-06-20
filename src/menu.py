menu = (
    "1. Import event files\n"
    "2. Import team files\n"
    "3. Add leagues from config\n"
    "4. Add league manually\n"
    "5. Settings\n"
    "6. Quit\n"
)

sub_menu_settings = (
    "1. Change event files path\n"
    "2. Change team files path\n"
    "3. Show files path\n"
    "4. Back"
)

def show_menu():
    print(menu)

def show_sub_menu():
    print(sub_menu_settings)


def get_choice():
    return input("Enter choice: ")