import json
import random

ALL_EXISTING_KEYS = []

# todo: refactor code to use class object instead of dictionaries when will wil change storage from json to sqlite3
def generate_unique_task_id(existing_task_ids):
    while True:
        new_task_id = random.randint(1, 999999)
        if new_task_id not in existing_task_ids:
            return new_task_id


def get_all_existing_keys(all_tasks: list):
    global ALL_EXISTING_KEYS
    for task in all_tasks:
        ALL_EXISTING_KEYS.append(task['task_id'])
        if task['task_subtasks']:
            get_all_existing_keys(task['task_subtasks'])


def modify_task_recursive(new_task: dict, tasks: list, parent_task_id, operation_type):
    for task in tasks:
        if task['task_id'] == parent_task_id:
            print(f"parent task found")
            print(task)
            if operation_type == 'adding':
                task['task_subtasks'].append(new_task)
            elif operation_type == 'modify':
                print(f"you searched task with id: '{parent_task_id}' and the task with this id was found!!!\n"
                      f"Loook!!!:\n{task}\n{new_task}")
                task['task_name'] = new_task['task_name']
                task['task_description'] = new_task['task_description']
            elif operation_type == 'deleting':
                tasks.remove(task)
            else:
                print("Invalid operation_type. Please use 'adding', 'modify', or 'deleting'.")
            break
        elif task['task_subtasks']:
            modify_task_recursive(new_task, task['task_subtasks'], parent_task_id, operation_type)


def task_crud(main_list_tasks, task_name, task_description, parent_task_id=None, operation_type=''):
    get_all_existing_keys(main_list_tasks['all_tasks'])
    print(f"all existed task_id: {ALL_EXISTING_KEYS}")

    temp_task = {
        "task_id": generate_unique_task_id(ALL_EXISTING_KEYS),
        "task_name": task_name,
        "task_description": task_description,
        "task_subtasks": []
    }
    if parent_task_id is None:
        if operation_type == 'adding':
            main_list_tasks['all_tasks'].append(temp_task)
        else:
            print(f"without parent_task_id is available only 'adding' operation."
                  f"actual provided operation_type: '{operation_type}'")
            return
    else:
        if operation_type in ['modify', 'deleting']:
            if parent_task_id not in ALL_EXISTING_KEYS:
                print(f"there isn't any task with provided parent id: '{parent_task_id}'")
                return
            else:
                temp_task['task_id'] = parent_task_id
        modify_task_recursive(
            new_task=temp_task,
            tasks=main_list_tasks['all_tasks'],
            parent_task_id=parent_task_id,
            operation_type=operation_type)
    save_tasks_to_json(main_list_tasks)


def save_tasks_to_json(tasks):
    with open("all_tasks.json", "w") as json_file:
        json.dump(tasks, json_file, indent=4)


def load_tasks():
    try:
        with open("all_tasks.json", "r", encoding='utf-8') as json_file:
            tasks_data = json.load(json_file)
            return tasks_data
    except FileNotFoundError:
        print("File not found. Creating a new file.")
        with open("all_tasks.json", "w", encoding='utf-8') as new_file:
            json.dump({"all_tasks":[
                {
                    "task_id": 1,
                    "task_name": "default task name",
                    "task_description": "default description",
                    "task_subtasks": []
                }
            ]}, new_file, indent=4)
        return {}


# all_existing_tasks = load_tasks()

# create_and_add_task(all_existing_tasks, "kkk", "kkk 2")
# task_crud(all_existing_tasks, "kkk", "kkk 2", None, operation_type='asdfd')
# task_crud(all_existing_tasks, "kkk", "kkk 2", None, operation_type='adding')
# task_crud(all_existing_tasks, "kkk", "kkk 2", 950703, operation_type='adding')
# task_crud(all_existing_tasks, "kkk", "kkk 2", 758067, operation_type='adding')
# task_crud(all_existing_tasks, "Kupite xxxx", "kxxxd", 2, operation_type='deleting')

# Вывод обновленного JSON
# print(json.dumps(main_list_tasks_loaded, indent=2))

# add_task_recursive(main_list_tasks_loaded, "Task 2", "Description 2", parent_task_id=948650)
# add_task_recursive(main_list_tasks_loaded, "Task 2", "Description 2", parent_task_id=165021)

# Пример использования удаления задачи
# delete_task_by_id(main_list_tasks_loaded, 932593)


# Пример использования изменения задачи
# update_task_by_id(main_list_tasks_loaded, 652164, new_task_name="New Task Name", new_task_description="New Task Description")
# update_task_by_id(main_list_tasks_loaded, 550673, new_task_name="New Task Name")
# update_task_by_id(main_list_tasks_loaded, 550673, new_task_description="New Task Description")
