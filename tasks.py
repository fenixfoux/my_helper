import json
import random


class Task:
    def __init__(self, task_name: str, task_description: str, task_subtasks: None, task_id: int):
        self.task_id = task_id
        self.task_name = task_name
        self.task_description = task_description
        self.task_subtasks = task_subtasks


def generate_unique_task_id(existing_ids):
    while True:
        task_id = random.randint(1, 999999)
        if task_id not in existing_ids:
            return task_id


def add_task_recursive(main_list_tasks, task_name, task_description, parent_task_id=None):
    if parent_task_id is None:
        task_id = generate_unique_task_id(main_list_tasks.keys())
        new_task = Task(task_id, task_name, task_description, [])
        main_list_tasks[task_id] = new_task.__dict__
    else:
        parent_task = find_task_by_id(main_list_tasks.values(), parent_task_id)
        print(f"All tasks: {main_list_tasks}")
        if parent_task:
            task_id = generate_unique_task_id([subtask["task_id"] for subtask in parent_task.get("task_subtasks", [])])
            new_task = Task(task_id, task_name, task_description, [])
            parent_task_subtasks = parent_task.get("task_subtasks", [])
            parent_task_subtasks.append(new_task.__dict__)
            parent_task["task_subtasks"] = parent_task_subtasks
        else:
            print(f"Parent task with ID {parent_task_id} not found.")

    save_tasks_to_json(main_list_tasks)


def find_task_by_id(tasks, task_id):
    for task_data in tasks:
        if isinstance(task_data, dict):
            if task_data.get("task_id") == task_id:
                return task_data
            elif task_data.get("task_subtasks"):
                found_task = find_task_by_id(task_data["task_subtasks"], task_id)
                if found_task:
                    return found_task
    return None


def delete_task_by_id(main_list_tasks, task_id):
    task_to_delete = find_task_by_id(main_list_tasks.values(), task_id)

    if task_to_delete:
        parent_task = find_parent_task(main_list_tasks.values(), task_id)
        if parent_task:
            parent_task_subtasks = parent_task.get("task_subtasks", [])
            parent_task_subtasks = [subtask for subtask in parent_task_subtasks if subtask["task_id"] != task_id]
            parent_task["task_subtasks"] = parent_task_subtasks
        else:
            # Deleting root task
            del main_list_tasks[str(task_id)]

        save_tasks_to_json(main_list_tasks)
        print(f"Task with ID {task_id} deleted.")
    else:
        print(f"Task with ID {task_id} not found.")


def find_parent_task(tasks, task_id):
    for task_data in tasks:
        if isinstance(task_data, dict):
            if task_data.get("task_subtasks"):
                for subtask in task_data["task_subtasks"]:
                    if subtask["task_id"] == task_id:
                        return task_data
                found_parent = find_parent_task(task_data["task_subtasks"], task_id)
                if found_parent:
                    return found_parent
    return None


def update_task_by_id(main_list_tasks, task_id, new_task_name=None, new_task_description=None):
    task_to_update = find_task_by_id(main_list_tasks.values(), task_id)

    if task_to_update:
        if new_task_name:
            task_to_update["task_name"] = new_task_name
        if new_task_description:
            task_to_update["task_description"] = new_task_description

        save_tasks_to_json(main_list_tasks)
        print(f"Task with ID {task_id} updated.")
    else:
        print(f"Task with ID {task_id} not found.")


def save_tasks_to_json(tasks):
    with open("all_tasks.json", "w") as json_file:
        json.dump(tasks, json_file, indent=4)


def load_tasks():
    try:
        with open("all_tasks.json", "r") as json_file:
            tasks_data = json.load(json_file)
            return tasks_data
    except FileNotFoundError:
        print("File not found. Creating a new file.")
        with open("all_tasks.json", "w") as new_file:
            json.dump({}, new_file)
        return []


# Пример использования добавления задачи
# main_list_tasks_loaded = load_tasks()
# add_task_recursive(main_list_tasks_loaded, "Task 2", "Description 2")
# add_task_recursive(main_list_tasks_loaded, "Task 2", "Description 2", parent_task_id=774701)
# add_task_recursive(main_list_tasks_loaded, "Task 2", "Description 2", parent_task_id=165021)

# Пример использования удаления задачи
# delete_task_by_id(main_list_tasks_loaded, 932593)


# Пример использования изменения задачи
# update_task_by_id(main_list_tasks_loaded, 652164, new_task_name="New Task Name", new_task_description="New Task Description")
# update_task_by_id(main_list_tasks_loaded, 550673, new_task_name="New Task Name")
# update_task_by_id(main_list_tasks_loaded, 550673, new_task_description="New Task Description")