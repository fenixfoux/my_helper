tab_names = {
    'eng': {
        'all': "all",
        '0': 'active',
        '1': 'completed'
    },
    'rus': {
        'all': "все",
        '0': 'в процессе',
        '1': 'готово'
    }
}
selected_lang = 'eng'
gg = "active"
print(tab_names[selected_lang])
for elem in tab_names[selected_lang]:
    # print(f"elem is '{elem}'") # get keys
    # print(tab_names[selected_lang][elem])
    if tab_names[selected_lang][elem] == gg:
        print(f"tab_names[selected_lang][elem] == gg is {tab_names[selected_lang][elem] == gg}")
        # print(tab_names[selected_lang][elem])
        print(elem)
