def list_to_string(lst):
    output_string = ""
    for i in lst:
        output_string += str(i)
    return output_string

def list_to_string_new_line(lst):
    output_string = ""
    for index, value in enumerate(lst):
        if index == len(lst)-1:
            output_string = output_string + str(value)
        else:
            output_string = output_string + str(value) + "\n"
    return output_string