# import main
import dataProcessor


def user_info():
    name = input('Please enter your name:\n-->').capitalize()
    return name

    # def user_input():
    # Directly send the user input to verify_input() for error catching/verifying input


def receive_verify_forward_input(shopping_list):
    accepted_commands = ['add', 'remove', 'delete all', 'help', 'exit', 'view']
    try:
        # verify input
        user_command = input('I would like to:\n-->')
        if user_command not in accepted_commands:
            raise ValueError('That command is not supported :(\nPlease try again or type "help"'.upper())
    except ValueError as err:
        print(err)
        # raise exception
    else:
        # if no exception raise
        # TODO: make the following code more efficient (try not to use if/else)
        if user_command == 'add':
            add_to_list(shopping_list)
        elif user_command == 'remove':
            remove_from_list(shopping_list)
        elif user_command == 'view':
            print(f"{'THIS CALL IF FROM THE VIEW FUNCTION'}")
            # main.print_list(shopping_list)
        elif user_command == 'delete all':
            shopping_list.clear()
        elif user_command == 'exit':
            '''main.exit_application(shopping_list)'''
        else:
            return shopping_list


def add_to_list(shopping_list):
    # start by printing list back to user
    # main.print_list(shopping_list)
    # add the item to the list
    print("Please type 'done' once you're done adding items")
    item = input("(retyping a previous item will increase the quantity)\nItem name:\n-->")
    # log of previously entered items
    print("DEBUG#1: Reaching this point")
    quantity = 1
    print("DEBUG#2: Reaching this point")
    if item == 'exit':
        print("DEBUG#3: Reaching this point")
        # main.exit_application(shopping_list)
    elif item == 'done':
        # TODO: fix this
        print("DEBUG#4: Reaching this point")
        return None
    elif len(shopping_list) == 0:
        print("DEBUG#4.1: Reaching this point")
        shopping_list.append([item, quantity])
        add_to_list(shopping_list)
    else:
        counter = 0
        while counter < len(shopping_list):
            if item == shopping_list[counter][0]:
                print("DEBUG#4.3: Reaching this point")
                # increment the quantity
                shopping_list[counter][1] += 1
                add_to_list(shopping_list)
                break
            counter += 1
        else:
            print("DEBUG#4.4: Reaching this point")
            shopping_list.append([item, quantity])
            add_to_list(shopping_list)


def remove_from_list(shopping_list):
    # Start by printing the list back to user
    # main.print_list(shopping_list)
    # remove the item from the list
    print("Please 'done' once you're done removing items")
    item = input("Item name:\n-->")
    if item == 'exit':
        print()
        dataProcessor.exit_application()
    elif item == 'done':
        return shopping_list
    elif len(shopping_list) <= 0:
        print("Oops! your list is already empty".upper())
        return shopping_list
    else:
        counter = 0
        while counter < len(shopping_list):
            if item == shopping_list[counter][0]:
                # remove item from list
                del shopping_list[counter]
                remove_from_list(shopping_list)
                break
            counter += 1
        else:
            print("That item is not in your list, please try again".upper())
            remove_from_list(shopping_list)

