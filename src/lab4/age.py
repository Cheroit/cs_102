# res=[]
# a=input('Введите границы возрастных групп: ')
# while True:
#     s = input()
#     if s == 'END':
#         break
#     res.append(s)
# res=list(map(str,res.split(',')))
# print(res)

users_ls=[]
age_ls = list(map(str,input().split()))
age_ls=[0]+age_ls
s = input('фио,возраст')
while s != 'END':
    m = s.split(',')
    users_ls.append([m[0], int(m[1])])
    s = input('фио,возраст')



if s=='END':
    diap = []
    dict = {}
    for i in range(0, len(age_ls)-1):
        diap.append([int(age_ls[i])+1, age_ls[i + 1]])
    for i in users_ls:
        for j in diap:
            # условие если возраст в диапазоне
            if int(i[1]) >= int(j[0]) and int(i[1]) <= int(j[1]):
                group = str(j[0]) + '-' + str(j[1])
                if group in dict.keys():
                    dict[group].append(str(i[0]) + ' ' + '(' + str(i[1]) + ')')
                else:
                    dict.update({group: [str(i[0]) + ' ' +'('+str(i[1])+')']})
                break
            elif i[1] >= 101:
                # случай 101+
                group = '101+'
                if group in dict.keys():
                    dict[group].append(str(i[0]) + ' ' + '(' + str(i[1]) + ')')
                else:
                    dict.update({group: [str(i[0]) + ' ' + '(' + str(i[1]) + ')']})
                break
            elif i[1] >= 123:
                break

for key, value in dict.items():
    print(f"{key}: {value[0]}")