#檔案的讀取、寫入

#Open("檔案路徑", mode= "開啟模式")
# 絕對路徑 Ex: C:/Users/didd4/OneDrive/文件\python
# 相對路徑 以程式的位置做延伸 ex: 123.txt


# mode = "r" 讀取  
# mode = "w" 複寫
# mode = "a" 在原先的資料後寫東西

file = open("123.txt",mode="a",encoding="utf-8")
# for line in file:
#    print(line)
file.write("\n蔡陰魂")
file.close()
