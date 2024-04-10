"""file for all variables in all languages"""
storage_path = './storages/'

todo_db_name = 'todo_db.db'
todo_table_name = 'todo'
todo_db_filepath = storage_path + todo_db_name

key_list_of_cards = 'list_of_cards'
key_task_id = 'task_id'

# KEYS
key_section_new_task_creation = 'new_task_creation'
key_new_task_name = 'new_task_name'
key_new_task_description = 'new_task_description'
key_tabs_section = 'tabs_section'
key_list_of_card = 'list_of_cards'
key_due_date_field = 'due_date_field'

new_task_name_hint_eng = 'task name'
new_task_description_hint_eng = 'task description'

# BUTTONS
test_button_text_eng = 'test'
button_back_text_eng = 'go home page'
save_text_eng = 'save'
clear_fields_new_task_button_text_eng = 'clear'

# PAGE NAMES
todo_page_name_eng = 'todo page'

# FIELDS TEXT
all_field_texts = {
    'eng': {
        'due_date_text' : "due date"
    },
    'rus': {
        'due_date_text' : "дата выполнения"
    }
}

# ALERT TEXT STRINGS
alert_empty_task_name_eng = "Task name can't be empty!"

#
# all_tab_names_eng = ["all", "active", "completed"]
all_tab_names = {
    'eng': {
        'all': "all",
        '0': 'active',
        '1': 'completed',
        'favorite': 'favorite'
    },
    'rus': {
        'all': "все",
        '0': 'в процессе',
        '1': 'готово',
        'favorite': 'избранное'
    }
}
