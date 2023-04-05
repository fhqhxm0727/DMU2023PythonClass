mdict_list = {'기본햄버거' : 4000, '치즈햄버거' : 4500, '불고기버거' : 5000, '와퍼킹버거' : 7000}
print(mdict_list)


mdict_list['새우버거'] = 5000 # 딕셔너리 값 추가
print(mdict_list)

mdict_list['불고기버거'] = mdict_list['불고기버거'] + 500
print(mdict_list)

del(mdict_list['기본햄버거'])
mdict_list['나이스버거'] = 2000
print(mdict_list)



for i in mdict_list.keys() :
    print(i, ':' , mdict_list[i])