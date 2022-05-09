import sys

def exit_application(shopping_list):
    del shopping_list
    print("List cleared")
    sys.exit('Application closed')