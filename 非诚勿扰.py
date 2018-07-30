man_age = int(input())
man_height = int(input())
man_weight =int(input())
man_income =int(input())
woman_age = int(input())
woman_height = int(input())
woman_weight =int(input())
woman_income =int(input())

if(20<=woman_age<=28 and 160<=woman_height<=175 and 40<=woman_weight<=60 and 2000<=woman_income<=5000):
    if(20<=man_age<=28 and 175<=man_height<=180 and 60<=man_weight<=70 and 3000<=man_income<=5000):
        print("匹配成功")
    else:
            print("男生不符合女生要求")
else:
    print("女生不符合男生要求")
