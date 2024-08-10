
"""
comprehension là một cách ngắn gọn và hiệu quả để tạo ra các cấu trúc dữ liệu như danh sách, từ điển, tập hợp.

"""
### List Comprehension:           new_list = [expression for item in iterable if condition]
# Lấy danh sách các số lẻ trong khoảng từ 0 đến 10
numbers = [x for x in range(10) if x % 2 != 0]
print(numbers)  # Output: [1, 3, 5, 7, 9]

### Dictionary Comprehension:     new_dict = {key_expression: value_expression for item in iterable if condition}
# Tạo ra 1 dic với key từ 1 đến 5, value = key mũ 3
numbers = [1, 2, 3, 4, 5]
squared_dict = {x: x**3 for x in numbers}
print(squared_dict)  # Output: {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

### Set Comprehension:            new_set = {expression for item in iterable if condition}
# Lấy ra 1 set các số chia hết cho 3
numbers = {x for x in range(10) if x % 3 == 0}
print(numbers)  # Output: {0, 3, 6, 9}

### Nested Comprehension:     lồng liên tiếp các comprehension
# Tạo ra 1 ma trận 5 dòng 3 cột
matrix = [[j for j in range(3)] for i in range(5)]                                                                                                                                                                         
print(matrix)  # Output: [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]]
for row in matrix:
    print(row)

### Generator Comprehension: chỉ sử dụng dc 1 lần, muốn dùng tiếp thì phải tạo mới lại
gen_exp = (x for x in range(10) if x % 2 == 0)
print(gen_exp)  # Output: <generator object <genexpr> at 0x...>

# Từ generator có thể chuyển thành các dạng khác như List, Tuple, Dic, Set
gen_exp = (x for x in range(10) if x % 2 == 0)  # gen sớ chẵn
print(f"Đổi Gen thành List: {list(gen_exp)}")

gen_exp = (x for x in range(10) if x % 2 != 0)  # gen sớ lẻ
print(f"Đổi Gen thành Tuple: {tuple(gen_exp)}")

gen_exp = (x**2 for x in range(10) if x % 2 == 0)  # gen số chẵn mũ 2
print(f"Đổi Gen thành Set: {set(gen_exp)}")

gen_exp = ((x, x*2) for x in range(10) if x % 2 != 0)   # gen sớ lẻ x 2
print([item for item in gen_exp])
print(f"Đổi Gen thành Dic: {dict(gen_exp)}")


