def two_arrays(str):
    array_switch = False
    change_array_one = True
    tempstring = ""
    temparray1 = []
    temparray2 = []
    index = 0
    for s in str:
        stop_int = len(str)
        if (s == ':') or (s == ','):
            array_switch = True
        elif (index + 1 == stop_int):
            array_switch = True
            tempstring = tempstring + s
        elif s != ' ':
            tempstring = tempstring + s
        if array_switch:
            if change_array_one:
                temparray1.append(tempstring)
                tempstring = ""
                change_array_one = False
                array_switch = False
            else:
                temparray2.append(tempstring)
                tempstring = ""
                change_array_one = True
                array_switch = False
        index += 1

    return temparray1, temparray2

# test code
# str = "abc:123, def:456, ghi:789"
# array1 = []
# array2 = []
# array1, array2 = two_arrays(str)
# print(array1)
# print(array2)