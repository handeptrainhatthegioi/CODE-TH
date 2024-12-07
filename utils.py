def find_max(lst):
    """Tìm phần tử lớn nhất trong danh sách và vị trí của nó."""
    if not lst:
        return None, None
    max_value = lst[0]
    max_index = 0
    for index, num in enumerate(lst):
        if num > max_value:
            max_value = num
            max_index = index
    return max_value, max_index

def find_min(lst):
    """Tìm phần tử nhỏ nhất trong danh sách và vị trí của nó."""
    if not lst:
        return None, None
    min_value = lst[0]
    min_index = 0
    for index, num in enumerate(lst):
        if num < min_value:
            min_value = num
            min_index = index
    return min_value, min_index
