def two_arrays(str):
    array_switch = True
    temparray1 = []
    temparray2 = []
    for s in str:
        if (s == ':') or (s == ','):
            array_switch = not array_switch
        if array_switch:
            if (s == ':') or (s == ',') or (s == ' '):
                pass
            else:
                temparray1.append(s)
        else:
            if (s == ':') or (s == ',') or (s == ' '):
                pass
            else:
                temparray2.append(s)

    return temparray1, temparray2

# code to test above
# str = "a:1, b:2, c:3"
# array1 = []
# array2 = []
# array1, array2 = two_arrays(str)
# print(array1)
# print(array2)