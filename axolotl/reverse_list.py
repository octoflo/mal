# A program to reverse a given list ex. a, b, c -> c, b, a
# Used to show the difference between the same program in LISP and Axolotl

# Python
def rev(data_list):
    last_index = len(data_list) - 1
    end_index = -1
    direction = -1
    new_list = []

    for l in range(last_index, end_index, direction):
        new_list.append(data_list[l])

    # or with a comprhension:
    # return [data_list[l]
            # for l in range(last_index, end_index, -1)]
