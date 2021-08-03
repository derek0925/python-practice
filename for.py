# for 迴圈

# for 變數 in 字串OR列表:
#    要重覆執行的程式碼

#for letter in "我是皮卡丘":
#    print(letter)


#for num in[0,1,2,3,4]:
#    print(num)

#for num in range(2,7):
#    print(num)

def power(base_num,pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
print(power(2,5)) 
    

