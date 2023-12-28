#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    listt = []
    count = 0
    while count < list_length:
        try:
            a = my_list_1[count]
            b = my_list_2[count]
        except IndexError:
            for x in range(count, list_length):
                listt.append(0)
                print("out of range")
            break
        else:
            try:
                div = a / b
            except ZeroDivisionError:
                print("division by 0")
                listt.append(0)
                count += 1
            except (ValueError, TypeError):
                print("wrong type")
                listt.append(0)
                count += 1
            else:
                listt.append(div)
                count += 1
            finally:
                continue
        finally:
            pass
    return (listt)
