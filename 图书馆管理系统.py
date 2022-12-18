books = {
    "理想国": {
        "author": "柏拉图",
        "publisher": "未知",
        "number": 4
    },
    "罗摩衍那": {
        "author": "塞尔达",
        "publisher": "未知",
        "number": 0
    },
    "三体": {
        "author": "刘慈欣",
        "publisher": "未知",
        "number": 2
    },
    "罗密欧与朱丽叶": {
        "author": "莎士比亚",
        "publisher": "未知",
        "number": 1
    }
}
def show_books(books):
    for book_name, book_info in books.items():
        print(f"书名：{book_name}")
        print(f"作者：{book_info['author']}")
        print(f"出版社：{book_info['publisher']}")
        print()

def find_book(books, book_name):
    if book_name in books:
        book_info = books[book_name]
        print(f"找到了《{book_name}》这本书！")
        print(f"作者：{book_info['author']}")
        print(f"出版社：{book_info['publisher']}")
    else:
        print(f"没有找到《{book_name}》这本书。")
#find_book(books, "罗摩衍那")
def borrow_book(books,book_name,student):
    if book_name in books:
        if books[book_name]['number'] == 0:
            print('此书售罄')
        else:
            print(f"{student}借了《{book_name}》这本书")
            books[book_name]['number'] -= 1
            print(f"此店剩余{books[book_name]['number']}本书")
    else:
        print("查无此书")
def return_book(books,book_name):
    if book_name in books:
        books[book_name]['number'] += 1
        print('已归还')
        print(f"此店剩余{books[book_name]['number']}本《{book_name}》")
    else:
        print(f"不是本馆的书")
def add_book(books,book_name,author,publisher,number):
    if book_name in books:
        books[book_name]['number'] += number
        print(f"此店剩余{books[book_name]['number']}本《{book_name}》")
    else:
        books[book_name] = {'author': author , "publisher": publisher , "number": number}
        print(f"本馆新增《{book_name}》")
        print()
def print_book_info(books):
    print("+------------+------------+")
    # print("|    书名    |    " + book[""] + "    |")
    # print("+------------+------------+")
    print("|    作者    |    " + book["author"] + "    |")
    print("+------------+------------+")
    print("|   出版社   |    " + book["publisher"] + "    |")
    print("+------------+------------+")
    print("| 剩余本数 |    " + book["number"] + "    |")
    print("+------------+------------+")

# 使用函数
book = {
    "title": "简·爱",
    "author": "费滋·勃朗特",
    "publisher": "约翰·牛津出版社",
    "remaining copies": "unknown"
}
