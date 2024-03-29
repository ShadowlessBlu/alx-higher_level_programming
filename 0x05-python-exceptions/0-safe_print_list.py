#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Safely prints x elements of a list.

    Args:
        my_list: The list to be printed.
        x: The number of elements to print.

    Returns:
        The real number of elements printed.
    """
    count = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            count += 1
    except (TypeError, IndexError):
        pass
    finally:
        print()
        return count


if __name__ == "__main__":
    # Test cases
    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list(my_list, 2)
    print("nb_print: {:d}".format(nb_print))

    nb_print = safe_print_list(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))

    nb_print = safe_print_list(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))
