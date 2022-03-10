#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from graphics import *
import time
import random
import pprint
win = GraphWin("点格棋", 600, 500)

list_h = []
list_s = []
list_c = []
lis_result=[]



now = 0;  # 1 玩家1    -1 玩家2
result = [0, 0]
cnt = 1
switch=0


aiFirst = Text(Point(520,100),"AI 先手")
manFirst = Text(Point(520,140),"我先手")
notice = Text(Point(520,290),"请选择先手") #提示轮到谁落子
notice.setFill('red')
QUIT = Text(Point(520,40),"退出")
QUIT.setFill('red')
result_ai = Text(Point(520,330),"玩家：0") #AI最后落子点
result_man = Text(Point(520,370),"AI：0") #玩家最后落子点

def drawWin():
    win.setBackground('LightGoldenrod1')
    x = 18
    for i in range(5):
        lis = []
        y = 10
        for j in range(6):
            h = Rectangle(Point(x, y), Point(80 + x, 8 + y))
            h.setFill("PeachPuff")
            l = [h, 0]
            lis.append(l)
            h.draw(win)
            y += 88
        list_h.append(lis)
        x += 88

    y = 18
    for i in range(5):
        lis = []
        x = 10
        for j in range(6):
            s = Rectangle(Point(x, y), Point(x + 8, y + 80))
            s.setFill("PeachPuff")
            l = [s, 0]
            lis.append(l)
            s.draw(win)
            x += 88
        list_s.append(lis)
        y += 88

    s = Rectangle(Point(10, 10), Point(458, 458))
    s.draw(win)

    y = 18
    for i in range(5):
        x = 18
        for j in range(5):
            c = Rectangle(Point(x, y), Point(x + 80, y + 80))
            l = [c, []]
            list_c.append(l)
            c.draw(win)
            x += 88
        y += 88

    Rectangle(Point(480, 25), Point(560, 55)).draw(win)
    Rectangle(Point(480, 85), Point(560, 115)).draw(win)
    Rectangle(Point(480, 125), Point(560, 155)).draw(win)
    Rectangle(Point(478, 275), Point(562, 305)).draw(win)
    Rectangle(Point(478, 307), Point(562, 395)).draw(win)
    aiFirst.draw(win)
    manFirst.draw(win)
    notice.draw(win)
    QUIT.draw(win)
    result_ai.draw(win)
    result_man.draw(win)

#产生并返回一个连同解
def ai1(list_h, list_s, list_c,lis_res):
    for lis in list_c:
        l = list(set([1, 2, 3, 4]) - set(lis[1]))
        m = list_c.index(lis) % 5
        n = list_c.index(lis) // 5
        if len(l) == 1:
            lis_res.append(m + n * 5)
            if l[0] == 1:
                list_s[n][m][1] = 1
                if m > 0:
                    list_c[m + n * 5 - 1][1].append(3)
                list_c[m + n * 5][1].append(1)

            elif l[0] == 2:
                list_h[m][n][1] = 1
                if n > 0:
                    list_c[m + (n - 1) * 5][1].append(4)
                list_c[m + (n) * 5][1].append(2)

            elif l[0] == 3:
                list_s[n][m + 1][1] = 1
                if m < 4:
                    list_c[m + n * 5 + 1][1].append(1)
                list_c[m + n * 5][1].append(3)
            elif l[0] == 4:
                list_h[m][n + 1][1] = 1
                if n < 4:
                    list_c[m + (n + 1) * 5][1].append(2)
                list_c[m + (n) * 5][1].append(4)

            ai1(list_h, list_s, list_c,lis_res)

            if l[0] == 1:
                list_s[n][m][1] = 0
                if m > 0:
                    list_c[m + n * 5 - 1][1].remove(3)
                list_c[m + n * 5][1].remove(1)

            elif l[0] == 2:
                list_h[m][n][1] = 0
                if n > 0:
                    list_c[m + (n - 1) * 5][1].remove(4)
                list_c[m + (n) * 5][1].remove(2)

            elif l[0] == 3:
                list_s[n][m + 1][1] = 0
                if m < 4:
                    list_c[m + n * 5 + 1][1].remove(1)
                list_c[m + n * 5][1].remove(3)
            elif l[0] == 4:
                list_h[m][n + 1][1] = 0
                if n < 4:
                    list_c[m + (n + 1) * 5][1].remove(2)
                list_c[m + (n) * 5][1].remove(4)

            return lis_res

# 获取一个区域的一边
def get_XY(c,i):
    x=0
    y=0
    l = list(set([1, 2, 3, 4]) - set(list_c[c][1]))
    m = c % 5
    n = c // 5
    if i==1 and c>=20:
        r=l[0]
    else:
        r=l[1]
    if r == 1:
        x = list_s[n][m][0].getP1().getX()
        y = list_s[n][m][0].getP1().getY()

    elif r == 2:
        x = list_h[m][n][0].getP1().getX()
        y = list_h[m][n][0].getP1().getY()

    elif r == 3:
        x = list_s[n][m + 1][0].getP1().getX()
        y = list_s[n][m + 1][0].getP1().getY()

    elif r == 4:
        x = list_h[m][n + 1][0].getP1().getX()
        y = list_h[m][n + 1][0].getP1().getY()
    return x,y




lis_fc=[]

def right(c,l,lis_res):

    if c in lis_res:
        lis_res.append("false")
        return

    lis_res.append(c)
    lis_fc.remove(c)

    if l == 1:
        if c%5==0:
            return

        l = list(set([1, 2, 3, 4]) - set(list_c[c - 1][1]))
        l.remove(3)
        # print(c - 1, l[0])
        if len(l)==1:
            right(c - 1, l[0],lis_res)
        if len(l)==0:
            lis_res.append(c-1)
            lis_fc.remove(c-1)

    if l == 2:
        if c < 5:
            return

        l = list(set([1, 2, 3, 4]) - set(list_c[c - 5][1]))
        l.remove(4)
        if len(l)==1:
            right(c - 5, l[0],lis_res)
        if len(l)==0:
            lis_res.append(c-5)
            lis_fc.remove(c-5)

    if l == 3:
        if c%5 == 4:
            return

        l = list(set([1, 2, 3, 4]) - set(list_c[c + 1][1]))
        l.remove(1)
        if len(l)==1:
            right(c + 1, l[0],lis_res)
        if len(l)==0:
            lis_res.append(c+1)
            lis_fc.remove(c+1)

    if l == 4:
        if c >=20:
            return

        l = list(set([1, 2, 3, 4]) - set(list_c[c + 5][1]))
        l.remove(2)
        if len(l)==1:
            right(c + 5, l[0],lis_res)
        if len(l)==0:
            lis_res.append(c+5)
            lis_fc.remove(c+5)

    # print(l)



def remain_connected():
    global lis_fc
    lis_result=[]

    lis_fc.clear()
    for lis in list_c:
        if len(lis[1]) != 4:
            lis_fc.append(list_c.index(lis))


    for i in range(len(list_c)):
        if len(list_c[i][1]) == 2 and i in lis_fc:

            l = list(set([1, 2, 3, 4]) - set(list_c[i][1]))

            lis_res = []
            right(i, l[0], lis_res)

            if lis_res[-1] != 'false':
                lis_res.remove(i)
                lis_fc.append(i)

                right(i, l[1], lis_res)
            else:
                lis_res.remove('false')
            lis_result.append(lis_res)
    return lis_result


count = []
count_res = []


def a(c, l, lis_res):
    global count

    count.append([c, l])
    lis_res.append(c)

    if l == 1:
        if c % 5 == 0:
            return

        l = list(set([1, 2, 3, 4]) - set(list_c[c - 1][1]))
        l.remove(3)
        # print(c - 1, l[0])
        if len(l) == 1:
            a(c - 1, l[0], lis_res)
        if len(l) == 0:
            lis_res.append(c - 1)

    if l == 2:
        if c < 5:
            return

        l = list(set([1, 2, 3, 4]) - set(list_c[c - 5][1]))
        l.remove(4)
        if len(l) == 1:
            a(c - 5, l[0], lis_res)
        if len(l) == 0:
            lis_res.append(c - 5)

    if l == 3:
        if c % 5 == 4:
            return

        l = list(set([1, 2, 3, 4]) - set(list_c[c + 1][1]))
        l.remove(1)
        if len(l) == 1:
            a(c + 1, l[0], lis_res)
        if len(l) == 0:
            lis_res.append(c + 1)

    if l == 4:
        if c >= 20:
            return

        l = list(set([1, 2, 3, 4]) - set(list_c[c + 5][1]))
        l.remove(2)
        if len(l) == 1:
            a(c + 5, l[0], lis_res)
        if len(l) == 0:
            lis_res.append(c + 5)


def connected():
    global count_res, lis_result, count
    count_res.clear()
    lis_result.clear()

    lis_fc.clear()
    for lis in list_c:
        if len(lis[1]) != 4:
            lis_fc.append(list_c.index(lis))


    for i in range(len(list_c)):
        if len(list_c[i][1]) == 3 and i in lis_fc:
            l = list(set([1, 2, 3, 4]) - set(list_c[i][1]))
            lis_res = []
            count = []
            a(i, l[0], lis_res)
            lis_res.sort()
            lis_result.append(lis_res)
            count_res.append(count)




def res_sum(res):
    _res=[]
    for i in range(len(res)):
        if res[i][1] not in list_c[res[i][0]][1]:
            m = res[i][0] % 5
            n = res[i][0] // 5

            if res[i][1] == 1:
                list_s[n][m][1] = 1
                if m > 0:
                    list_c[m + n * 5 - 1][1].append(3)
                list_c[m + n * 5][1].append(1)

            elif res[i][1] == 2:
                list_h[m][n][1] = 1
                if n > 0:
                    list_c[m + (n - 1) * 5][1].append(4)
                list_c[m + (n) * 5][1].append(2)

            elif res[i][1] == 3:
                list_s[n][m + 1][1] = 1
                if m < 4:
                    list_c[m + n * 5 + 1][1].append(1)
                list_c[m + n * 5][1].append(3)
            elif res[i][1] == 4:
                list_h[m][n + 1][1] = 1
                if n < 4:
                    list_c[m + (n + 1) * 5][1].append(2)
                list_c[m + (n) * 5][1].append(4)


            for lis in list_c:
                l = list(set([1, 2, 3, 4]) - set(lis[1]))
                if len(l) == 1:
                    if res[i][1] == 1:
                        list_s[n][m][1] = 0
                        if m > 0:
                            list_c[m + n * 5 - 1][1].remove(3)
                        list_c[m + n * 5][1].remove(1)

                    elif res[i][1] == 2:
                        list_h[m][n][1] = 0
                        if n > 0:
                            list_c[m + (n - 1) * 5][1].remove(4)
                        list_c[m + (n) * 5][1].remove(2)

                    elif res[i][1] == 3:
                        list_s[n][m + 1][1] = 0
                        if m < 4:
                            list_c[m + n * 5 + 1][1].remove(1)
                        list_c[m + n * 5][1].remove(3)
                    elif res[i][1] == 4:
                        list_h[m][n + 1][1] = 0
                        if n < 4:
                            list_c[m + (n + 1) * 5][1].remove(2)
                        list_c[m + (n) * 5][1].remove(4)
                    break

            else:
                _res.append(res[i])


    for i in range(len(_res)):

        m = _res[i][0] % 5
        n = _res[i][0] // 5

        if _res[i][1] == 1:
            list_s[n][m][1] = 0
            if m > 0:
                list_c[m + n * 5 - 1][1].remove(3)
            list_c[m + n * 5][1].remove(1)

        elif _res[i][1] == 2:
            list_h[m][n][1] = 0
            if n > 0:
                list_c[m + (n - 1) * 5][1].remove(4)
            list_c[m + (n) * 5][1].remove(2)

        elif _res[i][1] == 3:
            list_s[n][m + 1][1] = 0
            if m < 4:
                list_c[m + n * 5 + 1][1].remove(1)
            list_c[m + n * 5][1].remove(3)
        elif _res[i][1] == 4:
            list_h[m][n + 1][1] = 0
            if n < 4:
                list_c[m + (n + 1) * 5][1].remove(2)
            list_c[m + (n) * 5][1].remove(4)

    return len(_res)


def remove_same(s):
    res_s=[[s[0]]]
    for _s in s[1::]:
        f=0
        for rs in res_s:
            for r in rs:
                if r[0] == _s[0]:
                    res_s[res_s.index(rs)].append(_s)
                    f=1
                    break
                if r[1] == 3 and r[0]+ 1 == _s[0] :
                    res_s[res_s.index(rs)].append(_s)
                    f=1
                    break
                if r[1]==4 and r[0]+5==_s[0]:
                    res_s[res_s.index(rs)].append(_s)
                    f=1
                    break
                if r[1]==4 and _s[1]==3 and r[0] +4==_s[0]:
                    res_s[res_s.index(rs)].append(_s)
                    f=1
                    break
            if f==1:
                break
        if f ==0:
            res_s.append([_s])


    return len([ i[0] for i in res_s])


def select():
    result_select=[]
    for lis in list_c:
        l=list(set([1, 2, 3, 4]) - set(lis[1]))
        m = list_c.index(lis) % 5
        n = list_c.index(lis) // 5
        for i in l:

            if i == 1:
                if m > 0:
                    list_c[m + n * 5 - 1][1].append(3)
                list_c[m + n * 5][1].append(1)

            elif i == 2:
                if n > 0:
                    list_c[m + (n - 1) * 5][1].append(4)
                list_c[m + (n) * 5][1].append(2)

            elif i == 3:
                if m < 4:
                    list_c[m + n * 5 + 1][1].append(1)
                list_c[m + n * 5][1].append(3)
            elif i == 4:
                if n < 4:
                    list_c[m + (n + 1) * 5][1].append(2)
                list_c[m + (n) * 5][1].append(4)

            result_sel=remain_connected()
            for li in list_c:
                l = list(set([1, 2, 3, 4]) - set(li[1]))
                if len(l) == 1:
                    break
            else:
                result_select.append([[list_c.index(lis),i],result_sel])

            if i == 1:
                if m > 0:
                    list_c[m + n * 5 - 1][1].remove(3)
                list_c[m + n * 5][1].remove(1)

            elif i == 2:
                if n > 0:
                    list_c[m + (n - 1) * 5][1].remove(4)
                list_c[m + (n) * 5][1].remove(2)

            elif i == 3:
                if m < 4:
                    list_c[m + n * 5 + 1][1].remove(1)
                list_c[m + n * 5][1].remove(3)
            elif i == 4:
                if n < 4:
                    list_c[m + (n + 1) * 5][1].remove(2)
                list_c[m + (n) * 5][1].remove(4)



    print(result_select)

    result_s = [i[0] for i in result_select]


    s = []
    for i in result_s:
        if not ((i[0] % 5 == 0 and i[1] == 1) or (i[0] < 5 and i[1] == 2) or (i[0] % 5 == 4 and i[1] == 3) or (
                i[0] >= 20 and i[1] == 4)):
            if not ((i[0]==0 or i[0]==4 or i[0]==20 or i[0]==24) and len(list_c[i[0]][1])==0):

                if (i[1] == 3):
                    for j in result_s:
                        if (i[0] + 1 == j[0] and j[1] == 1 and len(list_c[i[0]][1])<2 and len(list_c[j[0]][1])<2):
                            a=0
                            for flag in result_s:
                                if flag[0] == i[0]:
                                    a+=1
                            if a>1:
                                a=0
                                for flag in result_s:
                                    if flag[0] == j[0]:
                                        a += 1
                                if a>1:
                                    s.append(i)
                                    break
                if (i[1] == 4):
                    for j in result_s:
                        if (i[0] + 5 == j[0] and j[1] == 2):
                            a = 0
                            for flag in result_s:
                                if flag[0] == i[0]:
                                    a += 1
                            if a > 1:
                                a = 0
                                for flag in result_s:
                                    if flag[0] == j[0]:
                                        a += 1
                                if a > 1:
                                    s.append(i)
                                    break


    print(len(s))

    print('特殊：',s)

    x=len(s)
    if len(s)<4 and s:
        x=remove_same(s);
    print('特殊====：',s)


    res=result_s.copy()

    res=[i for i in res if i not in s]
    sum=0
    sum=res_sum(res)
    last = [-1, 4, sum]


    # _sum=0
    # res=s.copy()
    # while res:
    #     flag = res[0]
    #     for r in res:
    #         if flag[1] ==4 and r[1]==3 and (r[0]==flag[0]+5 or r[0]==flag[0]+4):
    #             _sum+=1
    #             res.remove(r)
    #         # elif  flag[1] ==3 and r[1]==4 and (r[0]==flag[0]+1 or r[0]==flag[0]-4):
    #         #     _sum += 1
    #         #     res.remove(r)
    #         else:
    #             res.remove(r)



    t = 0
    if not (x == 1 or x==2):
        f=0
        for flag in result_s:
            for s1 in s:
                if (s1[0]==flag[0]) or (s1[1] == 3 and flag[0] == s1[0]+1) or (s1[1] == 4 and flag[0] == s1[0] + 5) :
                    f=1
                    break
            if f==0:
                i = result_s.index(flag)
                for j in result_select[i][1]:
                    # j[0][1]==3

                    if len(j) <= 2:
                        t += 1
                if (last[2] + t) % 2 == 1:
                    print("flag:",flag)
                    return flag


    if x==1 or x==2:


        if len(s)%2==0:
            last[2]+=1


        t = 0
        s=s[0]
        print("=======",result_s)
        i = result_s.index(s)
        last[2]-=1
        for j in result_select[i][1]:
            if len(j)<=2:
                t+=1


        if (last[2]+t)%2==1:
            return s

        last[2] += 1

        t=0
        for flag in result_s:
            if flag[0] == s[0] and flag[1]!=s[1]:
                i=result_s.index(flag)
                for j in result_select[i][1]:
                    if len(j) <= 2:
                        t += 1
                if (last[2] + t) % 2 == 1:
                    print("flag:", flag)
                    return flag

        t = 0
        if s[1]==3:
            for flag in result_s:
                if flag[0] == s[0]+1 and flag[1] != 1:
                    i = result_s.index(flag)
                    for j in result_select[i][1]:
                        if len(j) <= 2:
                            t += 1
                    if (last[2] + t) % 2 == 1:
                        print("flag:", flag)
                        return flag

        t = 0
        if s[1] == 4:
            for flag in result_s:
                if flag[0] == s[0] + 5 and flag[1] != 2:
                    i = result_s.index(flag)
                    for j in result_select[i][1]:
                        if len(j) <= 2:
                            t += 1
                    if (last[2] + t) % 2 == 1:
                        print("flag:", flag)
                        return flag


def ai():
    x = 0
    y = 0
    global lis_res,lis_result,switch


    lis_result=remain_connected()
    print('lis_result=======',lis_result)


    for lis in list_c:
        l = list(set([1, 2, 3, 4]) - set(lis[1]))
        if len(l) == 1:
            m = list_c.index(lis) % 5
            n = list_c.index(lis) // 5
            if len(lis_result)!=1:

                connected()
                lis_result.sort(key=len)
                count_res.sort(key=len)

                if switch==1 and len(lis_result)==2:
                    m = count_res[0][0][0] % 5
                    n = count_res[0][0][0] // 5
                    l[0] = count_res[0][0][1]
                    if lis_result[0]==lis_result[1]:
                        lis_result.pop(-1)


                if switch==1 and len(lis_result)==1:
                    if ((len(count_res[0])==3 and len(lis_result[0])==4) or (len(count_res[0])==2 and len(lis_result[0])==2) ):
                        m=count_res[0][1][0] % 5
                        n=count_res[0][1][0] // 5
                        l[0]=count_res[0][1][1]


            if l[0] == 1:
                x = list_s[n][m][0].getP1().getX()
                y = list_s[n][m][0].getP1().getY()
            elif l[0] == 2:
                x = list_h[m][n][0].getP1().getX()
                y = list_h[m][n][0].getP1().getY()
            elif l[0] == 3:
                x = list_s[n][m + 1][0].getP1().getX()
                y = list_s[n][m + 1][0].getP1().getY()
            elif l[0] == 4:
                x = list_h[m][n + 1][0].getP1().getX()
                y = list_h[m][n + 1][0].getP1().getY()
            if x != 0 and y != 0:
                return x, y


    s=[]
    s=select()
    if s :
        print(s)

        m = s[0] % 5
        n = s[0] // 5
        if s[1] == 1:
            x = list_s[n][m][0].getP1().getX()
            y = list_s[n][m][0].getP1().getY()

        elif s[1] == 2:
            x = list_h[m][n][0].getP1().getX()
            y = list_h[m][n][0].getP1().getY()

        elif s[1] == 3:
            x = list_s[n][m + 1][0].getP1().getX()
            y = list_s[n][m + 1][0].getP1().getY()

        elif s[1] == 4:
            x = list_h[m][n + 1][0].getP1().getX()
            y = list_h[m][n + 1][0].getP1().getY()
        return x, y





    for lis in random.sample(list_c, 25):
        l = list(set([1, 2, 3, 4]) - set(lis[1]))
        if len(l) == 4:

            m = list_c.index(lis) % 5
            n = list_c.index(lis) // 5
            for i in range(len(l)):
                r = random.choice(l)
                # print(l,r, m, n)
                l.remove(r)

                if r == 1:
                    if m == 0 or len(list_c[m + n * 5 - 1][1]) != 2:
                        x = list_s[n][m][0].getP1().getX()
                        y = list_s[n][m][0].getP1().getY()
                elif r == 2:
                    if n == 0 or len(list_c[m + (n - 1) * 5][1]) != 2:
                        x = list_h[m][n][0].getP1().getX()
                        y = list_h[m][n][0].getP1().getY()
                elif r == 3:
                    if m == 4 or len(list_c[m + n * 5 + 1][1]) != 2:
                        x = list_s[n][m + 1][0].getP1().getX()
                        y = list_s[n][m + 1][0].getP1().getY()
                elif r == 4:
                    if n == 4 or len(list_c[m + (n + 1) * 5][1]) != 2:
                        x = list_h[m][n + 1][0].getP1().getX()
                        y = list_h[m][n + 1][0].getP1().getY()
                if x != 0 and y != 0:
                    return x, y


    for lis in random.sample(list_c, 25):
        l = list(set([1, 2, 3, 4]) - set(lis[1]))
        if len(l) == 3:

            m = list_c.index(lis) % 5
            n = list_c.index(lis) // 5
            for i in range(len(l)):
                r = random.choice(l)
                # print(l,r, m, n)
                l.remove(r)

                if r == 1:
                    if m == 0 or len(list_c[m + n * 5 - 1][1]) != 2:
                        x = list_s[n][m][0].getP1().getX()
                        y = list_s[n][m][0].getP1().getY()
                elif r == 2:
                    if n == 0 or len(list_c[m + (n - 1) * 5][1]) != 2:
                        x = list_h[m][n][0].getP1().getX()
                        y = list_h[m][n][0].getP1().getY()
                elif r == 3:
                    if m == 4 or len(list_c[m + n * 5 + 1][1]) != 2:
                        x = list_s[n][m + 1][0].getP1().getX()
                        y = list_s[n][m + 1][0].getP1().getY()
                elif r == 4:
                    if n == 4 or len(list_c[m + (n + 1) * 5][1]) != 2:
                        x = list_h[m][n + 1][0].getP1().getX()
                        y = list_h[m][n + 1][0].getP1().getY()
                if x != 0 and y != 0:
                    return x, y




    l = [len(item) for item in lis_result]
    c=lis_result[l.index(min(l))][0]
    switch=1
    if min(l)==2:
        return get_XY(c,1)
    else:
        return get_XY(c,0)


if __name__ == '__main__':
    drawWin()

    while now==0:
        p = win.getMouse()
        y = p.getY()
        x = p.getX()
        if 480<=x<=560 :
            if 85<=y<=115:
                now=-1
            if 125<=y<=155:
                now=1
            if 25<=y<=55:
                QUIT.setText("正在退出")
                time.sleep(1)
                exit(0)

    while (True):

        if cnt <= -25:
            #time.sleep(0.01)
            x, y = ai();
            # flash.clear()
        else:
            if now == 1:
                notice.setText("请你下棋")
                p = win.getMouse()
                y = p.getY()
                x = p.getX()
                if 480 <= x <= 560 and 25 <= y <= 55:
                    QUIT.setText("正在退出")
                    time.sleep(1)
                    exit(0)

            elif now == -1:
                notice.setText("AI下棋")
                time.sleep(0.5)
                x, y = ai();



        flag = ''
        for lis in list_h:
            for i in lis:
                if i[0].getP1().getX() <= x < i[0].getP2().getX() and i[0].getP1().getY() <= y < i[0].getP2().getY() and \
                        i[1] == 0:
                    if now == -1:
                        i[0].setFill("red")
                    elif now == 1:
                        i[0].setFill("DeepSkyBlue")
                    i[1] = 1
                    now = -1 * now
                    cnt += 1
                    m = list_h.index(lis)
                    n = lis.index(i)
                    flag = 'h'
                    if n > 0:
                        list_c[m + (n - 1) * 5][1].append(4)
                        # flash.append([m + (n - 1) * 5,4])
                    if n < 5:
                        list_c[m + (n) * 5][1].append(2)
                        # flash.append([m + (n) * 5,2])
                    break
            if flag != '':
                break
        else:
            for lis in list_s:
                for i in lis:
                    if i[0].getP1().getX() <= x < i[0].getP2().getX() and i[0].getP1().getY() <= y < i[
                        0].getP2().getY() and i[1] == 0:
                        if now == -1:
                            i[0].setFill("red")
                        elif now == 1:
                            i[0].setFill("DeepSkyBlue")
                        i[1] = 1
                        n = list_s.index(lis)
                        m = lis.index(i)
                        now = -1 * now
                        cnt += 1
                        flag = 's'
                        if m > 0:
                            list_c[n * 5 + m - 1][1].append(3)
                            # flash.append([n * 5 + m - 1,3])
                        if m < 5:
                            list_c[n * 5 + m][1].append(1)
                            # flash.append([n * 5 + m,1])
                        break
                if flag != '':
                    break






        if flag == 's':
            f1 = 0
            if m > 0:
                if len(list_c[n * 5 + m - 1][
                           1]) == 4:  # 左
                    f1 = 1
                    if now == 1:
                        list_c[n * 5 + m - 1][0].setFill("red")
                        result[0] += 1

                    elif now == -1:
                        list_c[n * 5 + m - 1][0].setFill("DeepSkyBlue")
                        result[1] += 1

            if m < 5:
                if len(list_c[n * 5 + m][1]) == 4: #右
                    f1 = 1
                    if now == 1:
                        list_c[n * 5 + m][0].setFill("red")
                        result[0] += 1

                    elif now == -1:
                        list_c[n * 5 + m][0].setFill("DeepSkyBlue")
                        result[1] += 1

            if f1 == 1: now = -1 * now

        elif flag == 'h':
            f1 = 0
            if n > 0:
                if len(list_c[m + (n - 1) * 5][
                           1]) == 4:  #上
                    f1 = 1
                    if now == 1:
                        list_c[m + (n - 1) * 5][0].setFill("red")
                        result[0] += 1

                    if now == -1:
                        list_c[m + (n - 1) * 5][0].setFill("DeepSkyBlue")
                        result[1] += 1

            if n < 5:
                if len(list_c[m + (n) * 5][
                           1]) == 4:  #下
                    f1 = 1
                    if now == 1:
                        list_c[m + (n) * 5][0].setFill("red")
                        result[0] += 1

                    if now == -1:
                        list_c[m + (n) * 5][0].setFill("DeepSkyBlue")
                        result[1] += 1

            if f1 == 1: now = -1 * now

        result_ai.setText("AI:" + str(result[0]))
        result_man.setText("玩家:" + str(result[1]))
        for i in list_c:
            if len(i[1]) != 4:
                break
        else:
            if result[0] > result[1]:
                notice.setText("红方胜利")
            elif result[0] < result[1]:
                notice.setText("蓝方胜利")

            p = win.getMouse()
            y = p.getY()
            x = p.getX()
            if 480 <= x <= 560 and 25 <= y <= 55:
                QUIT.setText("正在退出")
                time.sleep(1)
                exit(0)