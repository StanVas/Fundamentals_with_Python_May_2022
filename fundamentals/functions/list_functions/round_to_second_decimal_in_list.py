def final(lst):
    final_lst = []
    for element in lst:
        element += element * 0.4
        element = "%.2f" % element
        final_lst.append(float(element))
    return final_lst

