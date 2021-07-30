from abc import ABC, abstractmethod


class AbstractView:
    @abstractmethod
    def draw(self):
        pass


class AddTask(AbstractView):
    SHORTCUT = 'at'
    LABEL = 'dodaj zadanie'

    def draw(self):
        pass


class DeleteTask(AbstractView):
    SHORTCUT = 'dt'
    LABEL = 'usuń zadanie'

    def draw(self):
        pass


class ListTasks(AbstractView):
    SHORTCUT = 'lt'
    LABEL = 'pokaż listę zadań'

    def draw(self):
        pass


class ExitApp:
    SHORTCUT = 'e'
    LABEL = 'wyjdź'
    EXIT = True

    def draw(self):
        print("exit?")


class MainMenu(AbstractView):
    OPTIONS = {
        AddTask.SHORTCUT: AddTask(),
        DeleteTask.SHORTCUT: DeleteTask(),
        ListTasks.SHORTCUT: ListTasks(),
        ExitApp.SHORTCUT: ExitApp()
    }

    def draw(self):
        print('MENU:')

        for choise, label in MainMenu.OPTIONS.items():
            print(f'[{choise}] - {label.LABEL}')

    def get_option(self):
        option = None
        while option not in MainMenu.OPTIONS:
            option = input('Wybierz dostępną opcję: ')

        return MainMenu.OPTIONS[option]
