import json
import os
import random

from storage import all_variables as all_vars


def check_storage_file():
    if not os.path.exists(all_vars.storage_file_path):
        with open(all_vars.storage_file_path, "w", encoding='utf-8') as new_file:
            json.dump({"all_tasks": [
                {
                    "task_id": 1,
                    "task_name": "default task name",
                    "task_description": "default description",
                    "task_subtasks": []
                }
            ]}, new_file, indent=4)


# check_storage_file()

def load_tasks():
    try:
        with open(all_vars.storage_file_path, "r", encoding='utf-8') as json_file:
            tasks_data = json.load(json_file)
            return tasks_data['all_tasks']
    except FileNotFoundError:
        print("File not found. Creating a new file.")
        with open(all_vars.storage_file_path, "w", encoding='utf-8') as new_file:
            json.dump({"all_tasks": [
                {
                    "task_id": 1,
                    "task_name": "default task name",
                    "task_description": "default description",
                    "task_subtasks": []
                }
            ]}, new_file, indent=4)
        return {}


def save_tasks_to_json(tasks):
    with open(all_vars.storage_file_path, "w", encoding='utf-8') as json_file:
        json.dump(tasks, json_file, indent=4)


def get_all_existing_keys(all_tasks: list, all_existing_keys):
    for task in all_tasks:
        all_existing_keys.append(task['task_id'])
        if task['task_subtasks']:
            get_all_existing_keys(task['task_subtasks'], all_existing_keys)
    return all_existing_keys


def generate_unique_task_id(existing_task_ids):
    while True:
        new_task_id = random.randint(1, 999999)
        if new_task_id not in existing_task_ids:
            return new_task_id


def prepare_new_task_dict(task_id, task_name, task_description):
    """
    take collected values from fields for create/update task, and return as dictionary for next operations
    :param task_id: int, task id
    :param task_name: str, task name value
    :param task_description: str, task description value
    :return:
    """
    return {
        'task_id': task_id,
        'task_name': task_name,
        'task_description': task_description,
        'task_subtasks': []
    }


def create_task(all_tasks_list: list, new_task: dict, parent_task_id=None):
    """
    Take the list of all tasks, add a new task, and return an updated list of all tasks.
    If parent_task_id is not None, it means a subtask needs to be added.
    :param all_tasks_list: list of all existed tasks
    :param new_task: dictionary with collected data from fields of create/update task
    :param parent_task_id: this is the task's ID which will be passed to this function for create a subtask
    :return:
    """
    updated_tasks_list = all_tasks_list.copy()

    if parent_task_id is None:
        updated_tasks_list.append(new_task)
    else:
        for task in updated_tasks_list:
            if task['task_id'] == parent_task_id:
                task['task_subtasks'].append(new_task)
                break
            elif task['task_subtasks']:
                create_task(task['task_subtasks'], new_task, parent_task_id)

    # Create a new dictionary with the updated all_tasks_list
    updated_tasks_dict = {'all_tasks': updated_tasks_list}

    # Save the updated dictionary to JSON
    save_tasks_to_json(updated_tasks_dict)


def find_task_by_id(all_tasks: list, task_id):
    for task in all_tasks:
        if task['task_id'] == task_id:
            return task
        elif task['task_subtasks']:
            find_task_by_id(task['task_subtasks'], task_id)
    return None


def read_task():
    pass


def update_task(all_tasks_list: list, updated_task_data: dict):
    """
    take the list of all tasks, find task by id, update task and return updated list of all tasks
    :param all_tasks_list: list of all existing tasks, each task is presented as dictionary
    :param updated_task_data: modified task, in dictionary format
    :return:
    """
    updated_tasks_list = all_tasks_list.copy()
    for task in updated_tasks_list:
        # print(task['task_id'] == updated_task_data['task_id'])
        # print(f"{type(task['task_id'])} and {type(updated_task_data['task_id'])}")
        # print(f"{task['task_id']} and {updated_task_data['task_id']}")
        if task['task_id'] == updated_task_data['task_id']:
            task['task_name'] = updated_task_data['task_name']
            task['task_description'] = updated_task_data['task_description']
            break
        elif task['task_subtasks']:
            update_task(task['task_subtasks'], updated_task_data)

    # Create a new dictionary with the updated all_tasks_list
    updated_tasks_dict = {'all_tasks': updated_tasks_list}

    # Save the updated dictionary to JSON
    save_tasks_to_json(updated_tasks_dict)


def delete_task(all_tasks_list: list, task_id_to_delete: int):
    """
    Take the list of all tasks, find task by id, update task, and return the updated list of all tasks.
    """
    paths_to_delete = []

    def find_paths_to_delete(tasks, current_path):
        for i, task in enumerate(tasks):
            if task['task_id'] == task_id_to_delete:
                paths_to_delete.append(current_path + [i])
            elif task['task_subtasks']:
                find_paths_to_delete(task['task_subtasks'], current_path + [i])

    find_paths_to_delete(all_tasks_list, [])

    # remove the tasks marked for deletion
    for path in reversed(paths_to_delete):
        node = all_tasks_list
        for index in path[:-1]:
            node = node[index]['task_subtasks']
        node.pop(path[-1])

    # create a new dictionary with the updated all_tasks_list
    updated_tasks_dict = {'all_tasks': all_tasks_list}

    # Save the updated dictionary to JSON
    save_tasks_to_json(updated_tasks_dict)

# check_storage_file()
# loaded_tasks = load_tasks()['all_tasks']

# # CREATE TASK FUNCTION TESTS
# create_task(loaded_tasks, all_vars.new_task_creation) # create new task, it means the parent_task_id is None
# create_task(loaded_tasks, all_vars.new_task_creation, 7595)  # add a subtask, it means the parent_task_id is not None
#
# # UPDATE TASK FUNCTION TESTS
# update_task(all_tasks_list=loaded_tasks, updated_task_data=all_vars.new_task_creation)
#
# # DELETE TASK FUNCTION TESTS
# delete_task(all_tasks_list=loaded_tasks, task_id_to_delete=333)
