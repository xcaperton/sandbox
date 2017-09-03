# func_tools.py


def prompt_selection(header_str, selection_dict):
    print(header_str)
    for key, value in selection_dict.items():
        print('{}: {}'.format(key, value))

    user_input = str(input())

    if user_input in selection_dict:
        print('You selected {}'.format(selection_dict[user_input]))
        return selection_dict[user_input]
    else:
        print('Invalid selection.')
