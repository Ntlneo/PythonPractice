
### Escape chars. Dùng dấu \
s = "I'm god tier \"Programer\""
s= "Trả lời câu hỏi của PV Thanh Niên về việc VN phải làm gì trước tình trạng giới trẻ ngại sinh con,\
ông Matt Jackson cho rằng cách tiếp cận là \
tôn trọng quyền của các cá nhân và quyền của các cặp vợ chồng trong việc sinh con theo cách mà họ muốn. \
Về phương diện quốc gia tôi thấy, điều quan trọng là phải chăm sóc, đáp ứng nhu cầu sinh sản của người dân, đặc biệt là những người trẻ tuổi."

s= "Trả lời câu hỏi của PV Thanh Niên về việc VN phải làm gì trước tình trạng giới trẻ ngại sinh con,\n\
ông Matt Jackson cho rằng cách tiếp cận là \t\
tôn trọng quyền của các cá nhân và quyền của các cặp vợ chồng trong việc sinh con theo cách mà họ muốn. \t\
Về phương diện quốc gia tôi thấy, điều quan trọng là phải chăm sóc, đáp ứng nhu cầu sinh sản của người dân, đặc biệt là những người trẻ tuổi."

### Substring
s = "Hello@ world@, how are you?"


luythua = f"{[2**n for n in range(3, 9)]}"
sochan = f"{[n for n in range(1,10) if n%2 == 0]}"
print(luythua)
print(sochan)

# In format string
ten = "Lam Nguyen"
tuoi = 28
sinhNgay = "28071984"
soPi = 3.1456
listz = [ten,tuoi,sinhNgay,soPi]
# print(f"Tôi tên {ten}, tuổi là {tuoi}. Và số pi là {soPi:.2}")
# print(f"Name: {ten}",f"Tuổi: {tuoi}", sep='\n')
# print(*listz,sep='\n')


# Lấy = index
LayChar = s[5]
LayraLowestIndex = s.index('world@')
# print(LayraLowestIndex)
# print(LayChar)



# Lấy = slice
s1 = "This's my house in Saigon"
s2 = "This's my bikes in Saigon"
substring = slice(7,-10)
newstring1 = s1[substring]
newstring2 = s2[substring]
# print(newstring1)
# print(newstring2)

LayChuWorld = s[6:11]
LayChuWorldDenHet = s[6:]
LayChuHowDenDau1 = s[:-9]
LayChuHowDenDau2 = s[:16]
LayCach3Chu = s[::3]
DaoNguoc = s[::-1]
# print(DaoNguoc)
# print(LayCach3Chu)
# print(LayChuHowDenDau2)
# print(LayChuHowDenDau1)
# print(LayChuWorldDenHet)
# print(LayChuWorld)

