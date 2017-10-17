def shift_policy(prev, lst):
    index = lst.index(prev) if prev is not None else -1

    return lst[index + 1] if index + 1 < len(lst) else lst[0]
