import sqlite3 as sq
import os
from pages.one_task import OneTask
from storages.all_variables import todo_db_filepath, todo_table_name


def check_for_db():
    if not os.path.exists(todo_db_filepath):
        # con = sq.connect(todo_db_filepath)
        # con.commit()
        # con.close()
        create_empty_tables()


def create_empty_tables():
    """that function will be used for create empty tables when the app will be firstly started"""
    db = sq.connect(todo_db_filepath)
    cur = db.cursor()
    create_todo_table_sql = (f"CREATE TABLE IF NOT EXISTS {todo_table_name} "
                             f"( "
                             f"task_id INTEGER PRIMARY KEY AUTOINCREMENT,"
                             f"parent_task_id INTEGER,"
                             f"task_name TEXT,"
                             f"task_description TEXT,"
                             f"task_status TEXT,"
                             f"task_created_date TEXT, "
                             f"task_due_date TEXT, "
                             f"task_is_favorite TEXT "
                             f" )")
    cur.execute(create_todo_table_sql)

    db.commit()
    db.close()


# def get_task_by_id(task_id: int):
#     db = sq.connect(todo_db_filepath)
#
#     cur = db.cursor()
#     query = f"SELECT * FROM {todo_table_name} WHERE TASK_ID = {task_id}"
#     cur.execute(query)
#     task = cur.fetchone()
#
#     db.close()
#     print(type(task))
#     return task
def save_new_task(one_task_obj: OneTask):
    with sq.connect(todo_db_filepath) as db_con:
        cur = db_con.cursor()
        # query = f"SELECT * FROM {todo_table_name}"
        print(f"received object:\n"
              f"one_task_name: {one_task_obj.task_name}\n"
              f"one_task_parent_task_id: {one_task_obj.parent_task_id}\n"
              f"one_task_description: {one_task_obj.task_description}\n"
              f"one_task_status: {one_task_obj.task_status}\n"
              f"one_task_due_date: {one_task_obj.task_due_date}")
        query = (f"insert into {todo_table_name} "
                 f"(parent_task_id, task_name, task_description, task_status, task_created_date, task_due_date, task_is_favorite) "
                 f"VALUES (?, ?, ?, ?, ?, ?, ?)")

        cur.execute(query, (
            one_task_obj.parent_task_id,
            one_task_obj.task_name,
            one_task_obj.task_description,
            one_task_obj.task_status,
            one_task_obj.task_created_date,
            one_task_obj.task_due_date,
            one_task_obj.task_is_favorite
        ))


def update_task(one_task_obj: OneTask):
    with sq.connect(todo_db_filepath) as db_con:
        cur = db_con.cursor()
        query = (f"UPDATE {todo_table_name} SET "
                 f"task_name = ?, "
                 f"task_description = ?, "
                 f"task_status = ?, "
                 f"task_due_date = ?, "
                 f"task_is_favorite = ? "
                 f"WHERE task_id = {one_task_obj.task_id}"
                 )
        cur.execute(query, (
            one_task_obj.task_name,
            one_task_obj.task_description,
            one_task_obj.task_status,
            one_task_obj.task_due_date,
            one_task_obj.task_is_favorite))
        db_con.commit()


# dd = OneTask()
# dd.task_id = str(7)
# dd.task_name = 'test'
# dd.task_description = 'test'
# dd.task_status = str(1)
# dd.task_due_date = "2024-04-08"
# update_task(dd)


def remove_task_by_id(task_id):
    with sq.connect(todo_db_filepath) as db_con:
        cur = db_con.cursor()
        query = (f"DELETE FROM {todo_table_name} "
                 f"WHERE TASK_ID = {task_id}")
        cur.execute(query)
        db_con.commit()


def get_all_tasks():
    list_of_tasks = []
    with sq.connect(todo_db_filepath) as db_con:

        cur = db_con.cursor()
        query = f"SELECT * FROM {todo_table_name}"
        cur.execute(query)
        tasks = cur.fetchall()

        table_column_names = [description[0] for description in cur.description]

        for row in tasks:
            # Create a new task object
            task_obj = OneTask()

            # Set attributes dynamically based on column names
            for idx, column_name in enumerate(table_column_names):
                setattr(task_obj, column_name, row[idx])

            # Append the task object to the list
            list_of_tasks.append(task_obj)
        return list_of_tasks


def get_subtasks(id_list: list):
    str_ids = ','.join(map(str, id_list))

    db = sq.connect(todo_db_filepath)
    cur = db.cursor()
    query = f"SELECT * FROM {todo_table_name} WHERE TASK_ID in ({str_ids})"
    cur.execute(query)
    tasks = cur.fetchall()
    db.close()

    return tasks

# def get_
