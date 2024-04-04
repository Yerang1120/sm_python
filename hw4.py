def get_fixed_price(a,b):
    ap=int(input(a+"상품의 할인된 가격은?"))
    price=int(ap*(100/(100-b)))
    return price
    

a=int(input("할인률은?"))
ad=get_fixed_price("A",a)
bd=get_fixed_price("B",a)
print("A 상품의 정가는",ad,"원")
print("B 상품의 정가는",bd,"원")
