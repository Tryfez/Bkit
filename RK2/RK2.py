from operator import itemgetter
class PR:
    def __init__(self, id, name_pr, v, pc_id):
        self.id = id
        self.name_pr = name_pr
        self.v = v
        self.pc_id = pc_id
class PC:
    def __init__(self, id, name):
        self.id = id
        self.name = name
class PR_Pc:
    """
    связь многие ко многим
    """
    def __init__(self, pc_id, pr_id):
        self.pc_id = pc_id
        self.pr_id = pr_id
Pcs = [
PC(1, 'компьютер Acer'),
PC(2, 'компьютер Samsung'),
PC(3, 'компютер Lenovo'),
PC(4, 'Imac'),
]
prs = [
PR(1, 'PyCharm', 224, 3),
PR(2, 'Photoshop', 2048, 2),
PR(3, 'Zoom', 289, 1),
PR(4, 'Telegram', 129, 4),
]
prs_pcs = [
PR_Pc(1,1),
PR_Pc(1,4),
PR_Pc(2,2),
PR_Pc(2,3),
PR_Pc(3,4),
PR_Pc(3,3),
PR_Pc(4,4),
PR_Pc(4,1),
]

    # Соединение данных один-ко-многим
one_to_many = [(pr.name_pr, pr.v, p.name)
for p in Pcs
for pr in prs
if pr.pc_id==p.id]
# Соединение данных многие-ко-многим
many_to_many_temp = [(p.name, pp.pc_id, pp.pr_id)
for p in Pcs
for pp in prs_pcs
if p.id==pp.pc_id]
many_to_many = [(pr.name_pr, pr.v, pc_name)
for pc_name, pc_id, pr_id in many_to_many_temp
for pr in prs if pr.id==pr_id]
def e1():
    print('Задание E1')
    res1 = []
    for name_pr, v, name in one_to_many:
        if 'компьютер' in name:
            res1.append((name, name_pr))
    return res1
def e2():            
    print('\nЗадание E2')
    res2_unsorted = []
    for p in Pcs:
        prss = list(filter(lambda i: i[2]==p.name, one_to_many))
        if len(prss) > 0:
            v_ob = [v for _,v,_ in prss]
            sum_a = sum(v_ob)/len(v_ob)
            res2_unsorted.append((p.name, sum_a))
    res2 = sorted(res2_unsorted, key=itemgetter(1))
    return res2
def e3():    
    print('\nЗадание E3')
    res3 = []
    for name_pr, v, name in many_to_many:
        if name_pr.find("P") == 0:
         res3.append((name_pr, name))
    return res3
def main():
    e1()
    e2()
    e3()

if __name__ == '__main__':
    main()
