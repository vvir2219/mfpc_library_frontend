def clear():
    print('\n'*100)
    #  os.system('clear')

def menu_item(prompt, f=lambda : print("Command not implemented")):
    return { "prompt": prompt, "function": f }

def exit_menu_item(prompt):
    return menu_item(prompt, lambda: 'exit_command')

def print_menu(items):
    for command, item in items.items():
        print(f"[ {command} ] {item['prompt']}")

def menu(top_message='', prompt='> ', clear_screen=True, exit_command = { 'exit': { 'prompt': 'Exit', 'function': lambda: 'exit_command'}}, menu_items={}):
    menu_items = { **menu_items, **exit_command }

    loop = True
    response = None
    while (loop):
        if (clear_screen): clear()

        print(top_message)
        print_menu(menu_items)
        command = input(prompt).lower()

        if command not in menu_items:
            input("Unknown command!")
            continue

        response = menu_items[command]["function"]()
        if response == 'exit_command':
            loop = False
        else:
            if response != 'no_keypress': input()
            if response == 'redo': loop = False

    return command, response

def api_menu(
    top_message='',
    prompt='> ',
    clear_screen=True,
    exit_command = { 'exit': { 'prompt': 'Exit', 'function': lambda: 'exit_command'}},
    get_items=lambda: print("Error, missing get items function"),
    no_items_message="Missing no items message!",
    item_command=lambda _: print("Error, missing command function"),
    item_repr=lambda _: print("Error, missing repr function"),
    item_func=lambda _: print("Error, missing func function"),
):
    response = None
    while (response != 'exit_command'):
        items = get_items()
        if len(items) == 0:
            print(no_items_message); input()
            break
        else:
            def do_func(item):
                def do():
                    item_func(item)
                    return 'redo'
                return do

            menu_items= { item_command(item):menu_item(item_repr(item), do_func(item)) for item in items }
            _, response = menu(
                top_message=top_message,
                prompt=prompt,
                clear_screen=clear_screen,
                exit_command=exit_command,
                menu_items=menu_items)

    return 'no_keypress'

