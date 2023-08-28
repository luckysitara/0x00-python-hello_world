#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    index = 0
    for item in range(x):
        try:
            print("{}".format(my_list=[item], end=''))
            index++
        except (ValueError, TypeError)
        pass
    print()
    return index
