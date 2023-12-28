#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    listt = []
    count = 0
    try:
        for a, b in my_list_1, my_list_2:
            if count == list_length:
                break
            try:
                div = a / b
            except ZeroDivisionError:
                print("division by 0")
                listt.append(0)
                count += 1
                continue
            except (ValueError, TypeError):
                print("wrong type")
                listt.append(0)
                count += 1
                continue
            else:
                listt.append(div)
                count += 1
    except ValueError:
        print("out of range")
    return (listt)
