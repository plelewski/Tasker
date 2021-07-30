from views import MainMenu
import sys

class Application:
    def main(self):
        menu = MainMenu()
        menu.draw()

        while True:
            option = menu.get_option()
            option.draw()
            if option.EXIT:
                sys.exit()


if __name__ == '__main__':
    app = Application()
    app.main()
