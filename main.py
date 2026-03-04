from task import Task, ImportantTask
from manager import TaskManager


def main():
    """Главная функция для демонстрации всех возможностей проекта"""
    print("=== ТЕСТИРОВАНИЕ TASK MANAGER ===\n")

    # Создаем менеджер задач
    my_tasks = TaskManager("Мои задачи")

    # Создаем обычные задачи
    task1 = Task("Купить продукты", "Молоко, хлеб", "средний")
    task2 = Task("Сделать зарядку", "30 минут утром", "низкий")

    # Создаем важную задачу (наследник)
    important_task = ImportantTask(
        "Сдать проект",
        "Подготовить презентацию",
        "пятница 18:00"
    )
    important_task.set_reminder()

    # Добавляем задачи в менеджер
    my_tasks.add_task(task1)
    my_tasks.add_task(task2)
    my_tasks.add_task(important_task)

    # Показываем все задачи (полиморфизм!)
    my_tasks.show_all_tasks()

    print("\n=== ДЕТАЛЬНАЯ ИНФОРМАЦИЯ ===\n")
    print(important_task.get_info())

    print("\n=== ФИЛЬТРАЦИЯ ===\n")

    # Получаем задачи по приоритету
    high_priority = my_tasks.get_tasks_by_priority("высокий")
    print("Задачи с высоким приоритетом:")
    for task in high_priority:
        print(f"  - {task}")

    # Отмечаем задачу выполненной
    task1.mark_completed()

    print("\n=== СТАТИСТИКА ===\n")
    print(my_tasks)

    # Поиск задач
    print("\n=== ПОИСК ===\n")
    found = my_tasks.find_tasks("проект")
    print("Найденные задачи:")
    for task in found:
        print(f"  - {task}")


def demonstrate_advanced_features():
    """Демонстрация продвинутых возможностей"""
    print("=== ДЕМОНСТРАЦИЯ ПРОДВИНУТЫХ ВОЗМОЖНОСТЕЙ ===\n")

    # Создаем менеджер задач
    manager = TaskManager("Рабочие задачи")

    # 1. Демонстрация обработки ошибок
    print("1. ОБРАБОТКА ОШИБОК:")
    manager.add_task("не задача")  # Ошибка типа
    manager.add_task(Task("Купить молоко"))  # OK
    manager.add_task(Task("Купить молоко"))  # Дубликат

    # 2. Добавляем разные задачи
    print("\n2. ДОБАВЛЕНИЕ ЗАДАЧ:")
    manager.add_task(Task("Сделать отчет", "Заполнить таблицы", "высокий"))
    manager.add_task(ImportantTask("Встреча с клиентом", "Подготовить презентацию", "завтра 10:00"))

    # 3. Демонстрация магических методов
    print("\n3. МАГИЧЕСКИЕ МЕТОДЫ:")
    print(f"Количество задач: {len(manager)}")
    print(f"Первая задача: {manager[0]}")
    print(f"'Купить молоко' в списке? {'Да' if 'Купить молоко' in manager else 'Нет'}")

    # 4. Создание задачи из строки (статический метод)
    print("\n4. СОЗДАНИЕ ИЗ СТРОКИ:")
    task_str = "Позвонить партнеру | Обсудить контракт | высокий"
    new_task = Task.create_from_string(task_str)
    if new_task:
        manager.add_task(new_task)

    # 5. Сохранение в файл
    print("\n5. СОХРАНЕНИЕ В ФАЙЛ:")
    manager.save_to_file("my_tasks.json")

    # 6. Загрузка из файла (создаем новый менеджер)
    print("\n6. ЗАГРУЗКА ИЗ ФАЙЛА:")
    loaded_manager = TaskManager.load_from_file("Загруженные задачи", "my_tasks.json")
    loaded_manager.show_all_tasks()

    # 7. Демонстрация работы с исключениями
    print("\n7. РАБОТА С ИНДЕКСАМИ:")
    task = manager.get_task_by_index(10)  # Несуществующий индекс
    task = manager.get_task_by_index("два")  # Неверный тип


if __name__ == "__main__":
    main()
    print("\n" + "=" * 50)
    demonstrate_advanced_features()
    print("\n" + "=" * 50)
    print("ПРОЕКТ УСПЕШНО ЗАВЕРШЕН!")