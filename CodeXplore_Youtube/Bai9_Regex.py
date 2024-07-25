import re

text = "Please contact us at support@example.com or sales@company.co.uk."
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}'
email_pattern2 = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

# 1. re.findall() tìm tất cả các chuỗi con khớp với mẫu trong văn bản và trả về danh sách các kết quả khớp
emails = re.findall(email_pattern, text)
emails2 = re.findall(email_pattern2, text)
print(emails)
print(emails2)

# 2. re.search() tìm kiếm mẫu đầu tiên khớp với biểu thức chính quy trong chuỗi và trả về đối tượng match đầu tiên
match = re.search(email_pattern, text)
if match:
    print("Email found:", match.group())
else:
    print("No email found.")
    
# 3. re.match() kiểm tra xem chuỗi có khớp với mẫu từ đầu chuỗi hay không.
match = re.match(email_pattern, text)
if match:
    print("Email matched:", match.group())
else:
    print("No match found at the beginning.")
    
# 4. re.sub() thay thế tất cả các chuỗi con khớp với mẫu bằng chuỗi thay thế.
replacement = "[EmailCuaTao@gmail.com]"
new_text = re.sub(email_pattern, replacement, text)
print(new_text)

# 5. re.split() chia chuỗi thành list các chuỗi con dựa trên mẫu regex.
textX = "apple, orange; banana: @grape"
patternX = r'[,\s;:@]+'
result = re.split(patternX, textX)
print(result)

# 6. re.finditer() tìm tất cả các chuỗi con khớp với mẫu và trả về iterator của các đối tượng match.
matches = re.finditer(email_pattern, text)
for match in matches:
    print("Email found:", match.group())

