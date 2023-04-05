menu = ('기본햄버거', '치즈햄버거', '불고기버거', '와퍼킹버거')
price = (4000, 4500, 5000, 7000)


for i in range(0, len(menu)) :
    print(i+1, " : %s : %d" % (menu[i], price[i]) )


# 튜플 수정을 위한 리스트 형변환

list_menu = list(menu)
list_price = list(price)
list_menu.append('새우버거')
list_price.append(5500)

menu = tuple(list_menu)
price = tuple(list_price)

print(menu)
print(price)