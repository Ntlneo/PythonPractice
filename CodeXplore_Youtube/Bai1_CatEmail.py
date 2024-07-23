
# ### Lấy user và domain của email ###
# # VD: alibaba@aaa.com
# mail = input("Nhập email của mài: ").strip()

# # 1. Dùng split
# name, domain = mail.split('@')
# print(f"Name:  {name}")
# print(f"Domain: {domain}")

# # 2. Dùng slice
# user = mail[:mail.index('@')]       # lấy phần trước @
# domain = mail[mail.index('@')+1:]   # lấy phần sau @
# print(f"Name:  {name}")
# print(f"Domain: {domain}")

### Viết chuẩn men, cái quần gì cũng bỏ vô hàm :)
def emailProcess(email: str):
    indexChar = email.index('@')
    user = email[:indexChar]
    domain = email[indexChar+1:]
    return [user,domain]
    
def printResult(user,domain):
    print(f'user là: {user}')
    print(f'domain là: {domain}')    

def main():
    email = input("Nhập 1 email: ").strip()
    user,domain = emailProcess(email)
    printResult(user,domain)

# main()
if __name__ == "__main__":
    main()


    
