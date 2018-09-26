# -*- coding = utf-8 -*-

import os
import random
import food

if __name__ == '__main__':

    print("=====一日将始，日日有饭食，生活乐滋滋=====")
    print("【XXX今日待客菜谱如下——】")

    #random.sample(list,x)从列表中随机取出x个元素为一个新列表
    porridge = random.sample(food.Porridge,1)
    moStable = random.sample(food.MoStable,2)
    pickles = random.sample(food.Pickles,2)
    #print(moStable)

    #os.path.join(path1[,path2[,...]])将多个路径组合后返回
    #MorningList = os.path.join(porridge, moStable, pickles)

    #合并列表，+生成新列表，append追加一个，extend追加一表等价于+=
    MorningList = porridge + moStable + pickles
    # join()函数返回一个以分隔符'sep'连接各个元素后生成的字符串
    #print('，'.join(MorningList))
    print("早午膳："+'，'.join(MorningList))

    stable = random.sample(food.Stable,1)
    meat = random.sample(food.Meat,2)
    vegetable = random.sample(food.Vegetable,2)
    soup = random.sample(food.Soup,1)
    AfternoonList = stable + meat + vegetable + soup
    print("午晚膳：白米饭\\"+'，'.join(AfternoonList))

    NightList = random.sample(food.Supper,5)
    print("夜宵："+'，'.join(NightList))

    TeaList = random.sample(food.Refreshments,7)
    print("茶点："+'，'.join(TeaList))

    print("【XX贵客若另有喜好，亦可寻楼厨大师傅点单】")
    print("========================")
    print("【XXX饭食如下——】")

    #random.choice(list)从列表中随机取出一个元素
    gPorridge = random.choice(food.GPorridge)
    gPickles = random.choice(food.Pickles)
    print("巳时早午餐：" + gPorridge + '，' + gPickles)

    gStable = random.choice(food.GStable)
    gVege = random.choice(food.GVegetable)
    gSoup = random.choice(food.GSoup)
    print("申时午后餐："+ gStable + '，' + gVege + '，' + gSoup)

    gRefreshment = random.choice(food.GRefreshments)
    print("子时后夜宵：" + gRefreshment)

    # random.randint()返回在[a,b]区间的随机整数，包括a，b
    fruit = random.randint(1,food.FruNum) # python计数下标从0开始
    print("余下食水：清水，"+food.Fruits[fruit-1]) #有+则输出无空格

    print("【XX】")
    print("============按时用膳，身体倍赞============")

    os.system("pause")

