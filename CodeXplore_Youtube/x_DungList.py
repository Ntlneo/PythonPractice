### Gán biến cho list

list1 = ['user1','user2','user3']
list2 = ['pass1','pass2','pass3']
list3 = ['token1','token2','token3']

for a,b,c in zip(list1,list2,list3):
    print(f'Login voi username {a} và password {b} dùng token {c}')


### Slice cắt lát cho list xuôi và ngược (::-1)
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
reverse_sub_list = my_list[8:1:-1]
print(reverse_sub_list)