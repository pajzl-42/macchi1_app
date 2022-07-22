import itertools

def list_to_string(lst):
    output_string = ""
    for index, value in enumerate(lst):
        if index == len(lst)-1:
            output_string = output_string + str(value)
        else:
            output_string = output_string + str(value) + "\n"
    return output_string

def percentage_calculator(value,list_of_three):
    output_list = []
    for i in list_of_three:
        output_list.append(i*0.01*value)
    return output_list

def alternating_merge(list1,list2):
    merged_lists = [sub[item] for item in range(len(list2)) for sub in [list1, list2]]
    return merged_lists

def filler(length, mode):
    if mode == "text":
        output_list = ['''""''' for i in range(length)]
    elif mode == "zero":
        output_list = [0 for i in range(length)]
    return output_list

def line_speed(percentage_list, thickness, throughput, density_per_layer_list, width):
    output_list = []
    die_diameter = 500
    die_gap = 0.150
    throughput_per_layer = percentage_calculator(throughput, percentage_list)
    thickness_per_layer = percentage_calculator(thickness, percentage_list)
    for index, value in enumerate(throughput_per_layer):
        result = (die_diameter * value)/(thickness_per_layer[index] * width * density_per_layer_list[index]\
                                         * 60 * 2 * (die_diameter - die_gap) * 10**(-6))
        output_list.append(result)

    final_result = sum([a * b * 0.01 for a, b in zip(percentage_list,output_list)])
    return final_result

def check_for_empty_values(list_of_three_lists):
    output_list = []
    inner_list = []
    for i in list_of_three_lists:
        for j in i:
            if j == "":
                inner_list.append('''""''')
            else:
                inner_list.append(j)
        output_list.append(inner_list)
        inner_list = []
    print(inner_list)
    print(output_list)
    return output_list



