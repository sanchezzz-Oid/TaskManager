from task import Task
from datetime import datetime


class TaskManager:
    """Класс для управления списком задач"""

    def __init__(self, name: str):
        """
        Конструктор класса TaskManager

        Args:
            name: Название менеджера задач
        """
        self.__name = name
        self.__tasks = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name.strip()) > 0:
            self.__name = new_name
        else:
            raise ValueError("Название менеджера не может быть пустым")

    def add_task(self, task: Task):
        """Добавление задачи в менеджер"""
        self.__tasks.append(task)
        print(f"Задача '{task.title}' добавлена в '{self.__name}'")

    def remove_task(self, index: int):
        """Удаление задачи по индексу"""
        if 0 <= index < len(self.__tasks):
            removed_task = self.__tasks.pop(index)
            print(f"Задача '{removed_task.title}' удалена")
        else:
            print("Неверный индекс задачи")

    def get_tasks(self):
        """Получение всех задач"""
        return self.__tasks.copy()

    def get_completed_tasks(self):
        """Получение выполненных задач"""
        return [task for task in self.__tasks if task.completed]

    def get_pending_tasks(self):
        """Получение невыполненных задач"""
        return [task for task in self.__tasks if not task.completed]

    def get_tasks_by_priority(self, priority: str):
        """Получение задач по приоритету"""
        return [task for task in self.__tasks if task.priority == priority]

    def mark_task_completed(self, index: int):
        """Отметить задачу как выполненную по индексу"""
        if 0 <= index < len(self.__tasks):
            self.__tasks[index].mark_completed()
        else:
            print("Неверный индекс задачи")

    def show_all_tasks(self):
        """Показать все задачи"""
        if not self.__tasks:
            print("Список задач пуст")
            return

        print(f"\n=== {self.__name} - Все задачи ===\n")
        for i, task in enumerate(self.__tasks, 1):
            print(f"{i}. {task}")

    def show_tasks_by_priority(self, priority: str):
        """Показать задачи по приоритету"""
        tasks = self.get_tasks_by_priority(priority)
        if not tasks:
            print(f"Нет задач с приоритетом '{priority}'")
            return

        print(f"\n=== {self.__name} - Задачи с приоритетом '{priority}' ===\n")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

    def get_statistics(self):
        """Получение статистики по задачам"""
        total = len(self.__tasks)
        if total == 0:
            return "Нет задач"

        completed = len(self.get_completed_tasks())
        pending = total - completed

        high_priority = len(self.get_tasks_by_priority("высокий"))
        medium_priority = len(self.get_tasks_by_priority("средний"))
        low_priority = len(self.get_tasks_by_priority("низкий"))

        stats = f"Всего задач: {total}\n"
        stats += f"Выполнено: {completed}\n"
        stats += f"Осталось: {pending}\n"
        stats += f"По приоритетам: высокий {high_priority}, средний {medium_priority}, низкий {low_priority}"

        return stats

    def __str__(self):
        """Статистика по задачам"""
        total = len(self.__tasks)
        completed = len(self.get_completed_tasks())
        pending = total - completed
        return f"{self.__name}: всего {total} задач (выполнено: {completed}, осталось: {pending})"

    def __len__(self):
        """Количество задач"""
        return len(self.__tasks)