#!/usr/bin/python3
def element_at(my_list, idx):
    n = len(my_list)
    if idx < 0:
        return None
    elif idx >= n:
        return None
    else:
        for i in my_list:
            for j in range[0, n]:
                if j == idx:
                    print("{:d}".format(i))
