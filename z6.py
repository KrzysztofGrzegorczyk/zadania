def merge_and_cube(list1, list2):
    merged_list = list(set(list1 + list2))
    cubed_list = [x**3 for x in merged_list]
    return cubed_list