class film:
    def load_film(self):
        f=open('films.txt', 'r')
        dict = {}
        for i in f:
            s=i.split(',')
            dict.update({int(s[0]) : s[1][0:-1]})
        return dict


class users:
    def load_users(self):
        f=open('users.txt', 'r')
        res=[]
        for i in f:
            m = list(map(int, i.split(',')))
            res.append(m)
        return res


class analiz():
    def recomend(input):
        dict_films=film.load_film(open('films.txt'))
        ls_users=users.load_users(open('users.txt'))
        m=list(map(int,input.split(',')))
        res=[]
        for i in ls_users:
            count = 0
            for j in m:
                if i.count(j) > 0:
                    count += 1
            if count>=len(m)//2:
                res.append([count, i])
        res = sorted(res, reverse=True)
        for i in m:
            for j in range(len(res)):
                while i in res[j][1]:
                    res[j][1].remove(i)

        nums = []
        for _, second_half in res:
            nums.extend(second_half)
        my_dict = {key: 0 for key in nums}

        for i in ls_users:
            for j in i:
                if j in my_dict:
                    my_dict[j] += 1
                else:
                    my_dict[j] = 1
        otv=max(my_dict, key=my_dict.get)
        return dict_films[otv]


#print(analiz.recomend('2,3'))