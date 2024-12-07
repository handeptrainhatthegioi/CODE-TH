from my_module import find_max, find_min

def main():
    n = int(input("Nhập số lượng phần tử trong danh sách: "))
    lst = []
    for i in range(n):
        value = float(input(f"Nhập giá trị phần tử thứ {i + 1}: "))
        lst.append(value)
    max_value = find_max(lst)
    min_value = find_min(lst)

    print(f"Phần tử lớn nhất là: {max_value}")
    print(f"Phần tử nhỏ nhất là: {min_value}")

if __name__ == "__main__":
    main()
