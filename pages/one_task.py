import datetime

temp_one_task = {
    'task_id': '',
    'parent_task_id': '',
    'task_name': '',
    'task_description': '',
    'task_status': '',
    'task_due_date': '',
    'task_subtasks_id': '',
}


class OneTask:
    def __init__(self):
        self.task_id = ''
        self.parent_task_id = None
        self.task_name = ''
        self.task_description = ''
        self.task_status = 0
        self.task_created_date = ''
        self.task_due_date = ''
        self.task_is_favorite = False
        self.task_subtasks_id = []  # list of subtasks id


if __name__ == "__main__":
    task = OneTask()
    columns = [attr for attr in vars(task) if not attr.startswith('__')]
    print(columns)
