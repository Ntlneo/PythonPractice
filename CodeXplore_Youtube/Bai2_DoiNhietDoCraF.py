# Nhập độ C sẽ in ra độ F
# Công thức F = C*9/5 + 32
# Ko nhap thì se yeu cau phai nhap hoài

def getDoC():
    doC = input("Nhập nhiệt độ C: ").strip()
    return doC

def ConvertCtoF():
    while True:    
        doC = getDoC()    
        if not doC:
            print("Ko thể để độ C bằng EMPTY")            
            continue
        elif doC.find('-') >= 0 or doC.find('.') >= 0 or doC.isdigit():     # làm cách này thì nó nhập chữ có chứa dấu - or . gì cũng hợp lệ, và gọi làm float sẽ bị văng exception ValueError
            doC = float(doC)
            doF = round(doC*9/5 + 32,1)
            print(f"{doC} độ C là bằng {doF} độ F")
            break
        else:
        # elif not doC.isnumeric():   # cái này sai với số âm
            print("Độ C ko thể có chữ. Chỉ chấp nhận số") 
            continue   
        
if __name__ == "__main__":
    ConvertCtoF()
    
    