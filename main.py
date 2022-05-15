import dataCollector
import dataCollector as dc
import sys

def show_help():
    helpList = ['Type "add" to add an item',
                'Type "remove" to remove an item',
                'Type "view" to view your list',
                'Type "delete all" to delete the entire list',
                'Type "help" to see this list again']

    [print(i) for i in helpList ]


def print_greeting(name):
    print('Hello {}!. You can type "help" at anytime to see command options'.format(name))





def print_list2(shopping_list):
    print(f"{'THIS PRINT CALL IS FROM MAIN'}")
    for count, value in enumerate(shopping_list):
        print(f"{count+1}. {value['item']} x{value['quantity']}")


# TODO learn more about functional programming and change this code accordingly


def main():
    # Creating list
    shopping_list = []

    # Previously added

    # Show user 'help' commands
    # show_help()

    # Collect user info and pass the returned value to print_greeting()
    print_greeting(dataCollector.user_info())
    show_help()
    while True:
        # start
        # display help message to guide the user on how to navigate the application
        # initiate the dataCollector method
        dataCollector.receive_verify_forward_input(shopping_list)
        # Receive the shopping list back and print for the user
        print_list2(shopping_list)
        # Repeat above





if __name__ == '__main__':
    main()

