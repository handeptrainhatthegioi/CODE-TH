def find_max(lst):
    """Tìm phần tử lớn nhất trong danh sách."""
    if not lst:
        return None
    max_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
    return max_value

def find_min(lst):
    """Tìm phần tử nhỏ nhất trong danh sách."""
    if not lst:
        return None
    min_value = lst[0]
    for num in lst:
        if num < min_value:
            min_value = num
    return min_value
