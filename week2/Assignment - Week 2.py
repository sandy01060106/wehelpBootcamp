#task1
def find_and_print(messages, current_station): 
    # 填寫程式碼
messages = { 
    "Leslie": "I'm at home near Xiaobitan station.", 
    "Bob": "I'm at Ximen MRT station.", 
    "Mary": "I have a drink near Jingmei MRT station.", 
    "Copper": "I just saw a concert at Taipei Arena.", 
    "Vivian": "I'm at Xindian station waiting for you." 
} 
find_and_print(messages, "Wanlong") # 輸出 Mary 
find_and_print(messages, "Songshan") # 輸出 Copper 
find_and_print(messages, "Qizhang") # 輸出 Leslie 
find_and_print(messages, "Ximen") # 輸出 Bob 
find_and_print(messages, "Xindian City Hall") # 輸出 Vivian


#task2
# 填寫程式碼
def book(consultants, hour, duration, criteria): 
    # 填寫程式碼
consultants = [ 
    {"name": "John", "rate": 4.5, "price": 1000}, 
    {"name": "Bob", "rate": 3, "price": 1200}, 
    {"name": "Jenny", "rate": 3.8, "price": 800} 
] 
book(consultants, 15, 1, "price") # 輸出 Jenny 
book(consultants, 11, 2, "price") # 輸出 Jenny 
book(consultants, 10, 2, "price") # 輸出 John 
book(consultants, 20, 2, "rate") # 輸出 John 
book(consultants, 11, 1, "rate") # 輸出 Bob 
book(consultants, 11, 2, "rate") # 輸出 No Service 
book(consultants, 14, 3, "price") # 輸出 John 

#task3
def func(*data): 
    # 填寫程式碼
func("彭大牆", "陳王明雅", "吳明") # 輸出 彭大牆 
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # 輸出 林花花 
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # 輸出 沒有 
func("郭宣雅", "夏曼藍波安", "郭宣恆") # 輸出 夏曼藍波安 

#task4
def get_number(index): 
    # 填寫程式碼
get_number(1) # 輸出 4 
get_number(5) # 輸出 15 
get_number(10) # 輸出 25 
get_number(30) # 輸出 70 

#task5
def find(spaces, stat, n): 
    # 填寫程式碼
find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2) # 輸出 5 
find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # 輸出 -1 
find([4, 6, 5, 8], [0, 1, 1, 1], 4) # 輸出 2 

