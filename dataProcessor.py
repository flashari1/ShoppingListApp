'''elif item in previously_added:
        print("DEBUG#5: Reaching this point")
        print("Item: {}".format(item))
        for element in shopping_list:
            print("DEBUG#5.1: Reaching this point")
            print("DEBUG#6: Reaching this point")
            if item == element[0]:
                print("DEBUG#7: Reaching this point")
                item0 = list(shopping_list[shopping_list.index(element)])
                print("DEBUG#8: Reaching this point")
                item0[1] += 1
                print("DEBUG#9: Reaching this point")
                shopping_list[shopping_list.index(element)] = item0
                print("DEBUG#10: Reaching this point")
                main.print_list(shopping_list)
                print("DEBUG#11: Reaching this point")
                add_to_list(shopping_list)
                print("DEBUG#12: Reaching this point")
            else:
                print("DEBUG#13: Reaching this point")
                main.print_list(shopping_list)
                add_to_list(shopping_list)'''