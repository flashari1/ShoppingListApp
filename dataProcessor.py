import sys

def print_list(shopping_list):
    for count, value in enumerate(shopping_list):
        print(f"{count+1}. {value['item']} x{value['quantity']}")


def exit_application(shopping_list):
    del shopping_list
    print("List cleared")
    sys.exit('Application closed')