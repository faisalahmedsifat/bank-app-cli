from ui.bank_app_ui import BankAppUI


class BankAppCLI:
    def __init__(self, ui):
        self.ui = ui

    def create_new_user(self):
        self.ui.create_new_user()

    def display_all_accounts(self):
        self.ui.display_all_accounts()

    def update_an_account(self):
        self.ui.update_an_account()

    def delete_an_account(self):
        self.ui.delete_an_account()

    def deposit_to_an_account(self):
        self.ui.deposit_to_an_account()

    def withdraw_from_an_account(self):
        self.ui.withdraw_from_an_account()

    def search_for_an_account(self):
        self.search_for_an_account()

    def loop(self):
        while True:
            ui.display_menu()
            choice = ui.get_user_choice()
            print("\n")

            if choice == "1":
                self.create_new_user()
            elif choice == "2":
                self.display_all_accounts()
            elif choice == "3":
                self.update_an_account()
            elif choice == "4":
                self.delete_an_account()
            elif choice == "5":
                self.deposit_to_an_account()
            elif choice == "6":
                self.withdraw_from_an_account()
            elif choice == "7":
                self.search_for_an_account()
            elif choice == "8":
                print("Exiting the program")
                break
            else:
                print("Invalid choice")
            print("\n")

    def run(self):
        self.loop()


if __name__ == "__main__":
    ui = BankAppUI()
    app = BankAppCLI(ui)
    app.run()