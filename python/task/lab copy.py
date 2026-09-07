from abc import ABC, abstractmethod
class resturent(ABC):
    def database(self):
        print("calling database")
    @abstractmethod
    def menu(self):
        pass
class Menu(resturent):
    def menu(self):
        print("Restaurant Menu")
        print("1. Pizza")
        print("2. Burger")
        print("3. Pasta")
    def print_database(self):
        self.database()
obj = Menu()
obj.print_database()
obj.menu()