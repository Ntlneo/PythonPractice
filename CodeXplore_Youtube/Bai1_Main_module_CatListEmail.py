from Bai1_CatEmail import emailProcess, printResult

def main():
    listEmail = ['a1@gmail.com', 'xxx@zzz.commmm', 'ngaymainguoita@lay.chong']
    for email in listEmail:
        user,domain = emailProcess(email)
        printResult(user,domain)
    
if __name__ == '__main__':
    main()