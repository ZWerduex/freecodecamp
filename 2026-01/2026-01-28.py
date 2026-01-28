def flatten(arr):
    flat = []
    for i in arr:
        if type(i) == list:
            flat.extend(flatten(i))
        else:
            flat.append(i)
    return flat