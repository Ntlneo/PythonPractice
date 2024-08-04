def is_decimal(chuoi):
    # Xử lý dấu âm
    if chuoi.startswith('-'):
        chuoi = chuoi[1:]

    # Kiểm tra nếu chuỗi có dấu chấm
    if '.' in chuoi:
        # Tách phần nguyên và phần thập phân-a
        parts = chuoi.split('.')
        # Phần thập phân phải có ít nhất một ký tự và không chứa ký tự không phải số
        return len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit()
    else:
        # Nếu không có dấu chấm, kiểm tra nếu chuỗi chỉ chứa số
        return chuoi.isdigit()

# Nhập chuỗi từ người dùng
chuoi = input("Nhập một số: ")

if is_decimal(chuoi):
    so = float(chuoi)
    if so != 0:
        print(f"{chuoi} là một số thập phân hợp lệ và không phải là số 0.")
    else:
        print(f"{chuoi} không phải là một số thập phân dương hoặc âm (số 0).")
else:
    print(f"{chuoi} không phải là một số thập phân hợp lệ.")
