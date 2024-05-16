def buy(dics):
    while True:
        print("[구입]")
        a=input("상품명?")
        if a == "" :
            return False
        b=int(input("수량은?"))
        dics[a]=b
        print(f"장바구니에 {a} {b}개가 담겼습니다.\n")

def show(bag):
    print(f">>> 장바구니 보기: {bag} ")
def find(bagg):
    print("[검색]")
    n=input("장바구니에서 확인하고자 하는 상품은?")
    if n in bagg:
        p=bagg[n]
        print(f"장바구니에 {n}은(는) {p}개 담겨있습니다.")
    elif n not in bagg:
        print(f"장바구니에 {n}은(는) 없습니다.")
        
shopping_bag={}

while True :
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)
