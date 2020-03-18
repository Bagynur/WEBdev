a = int(input())
div = int(2)

while div < a+1:
    if(a%div == 0):
        print(div)
        break
    else:
        div = div + 1