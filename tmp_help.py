for i in range(32):
    print("\"",i,"\"",",",end='')

list = ((1,2),(3,4))

for i in list:
    print(i)
    for j in i:
        print(j)

list = (('K0001', '河北', '山西', 14050505, '0911', '1022', 999, 998.0, 333.0, 0.7, 'SH48A'), ('Y7381', '河北', '山西', 14050505, '1933', '1022', 999, 132.0, 333.0, 0.8, 'SH48A'), ('Z1919', '湖南', '山东', 14050505, '1933', '2235', 676, 132.0, 67.0, 0.8, 'JNSS'))
# 断开数据库的连接，释放资源；
r = 0
c = 0
for row in list:
    c = 0
    print(row)
    for column in row:
        if c == 3 or c > 5 and c < 10:
            print(c)
        else:
            print(c)
        print(column)
        c = c + 1
    r = r + 1

month = '9'
if int(month) < 10:
    month = '0'+month

print(month)


date = '2000' + '05' + '05'
for i in date:
    print(i)

year = '2000'
month = '5'
date = '5'

if int(month) < 10:
    month = '0' + month
if int(date) < 10:
    date = '0' + date
dataTime = year + month + date
for i in dataTime:
    print(i)

print(dataTime[2:])