import src.menu as menu
import src.ETL as ETL

class Manager:

    def __init__(self):
        self.is_running = True
        self.choices = {
             "3": ETL.add_leagues_from_file,
             "5": self.display_sub_menu_settings,
             "6": self.quit
        }
        self.choices_sub_menu_settings = {
             "4": self.sub_menu_go_to_main_menu
        }
        self.start()

    def start(self):
        while self.is_running:
            menu.show_menu()
            user_choice = menu.get_choice()
            self.choices.get(user_choice)()

    
    def display_sub_menu_settings(self):
        menu.show_sub_menu()
        user_choice = menu.get_choice()

    def sub_menu_change_event_files_path(self):
        new_path = input("New path: ")

    def sub_menu_change_match_files_path(self):
        new_path = input("New path: ")
    
    def sub_menu_go_to_main_menu(self):
        self.start()
            
    def quit(self):
        self.is_running = False

if __name__ == "__main__":
    Manager()