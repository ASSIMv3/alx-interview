#!/usr/bin/python3
""" function to solve the lockboxes algorrithm """


def canUnlockAll(boxes):
    """ determines if all the boxes can be opened """
    length = len(boxes)
    keys = set()
    next_box = []
    i = 0

    while i < length:
        oldi = i
        next_box.append(i)
        keys.update(boxes[i])
        for key in keys:
            if key != 0 and key < length and key not in next_box:
                i = key
                break
        if oldi != i:
            continue
        else:
            break

    for i in range(length):
        if i not in next_box and i != 0:
            return False
    return True
