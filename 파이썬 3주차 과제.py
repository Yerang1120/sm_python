def change(a):
    b=a//500
    n=a%500
    c=n//100
    n=n%100
    d=n//50
    n=n%50
    e=n//10
    print("500원 동전의 개수:",b)
    print("100원 동전의 개수:",c)
    print("50원 동전의 개수:",d)
    print("10원 동전의 개수:",e)
def get_integer(b):
    return int(input(b))
cost=get_integer("동전으로 교환하고자 하는 금액은?")
change(cost)
