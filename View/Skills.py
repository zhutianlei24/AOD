from tkinter import *
import tkinter.messagebox
from View.ToolTip import *
from Model.PC import *
from View.Skill1 import *
from View.Skill2 import *

class Skills():

    def __init__(self, master, player):
        self.root = master
        self.ui = Frame(self.root, )
        self.ui.pack(fill=BOTH, expand=True)

        self.player = player

        self.zhiye = ["护士","神秘学家"]
        self.qujian = [(9,30),(9,65)]
        self.xingyu = dict(zip(self.zhiye, self.qujian))

        self.jinengdict = {}
        self.jinengdict[''] = ['']
        self.jinengdict["护士"] = ["急救","医学","心理学","聆听"]
        self.jinengdict["神秘学家"] = ["人类学","历史","图书馆","神秘学"]

        sk1 = Skill1(master, self.ui, player)
        sk2 = Skill2(master, self.ui, player)
        self.frames = {}
        self.frames["Skill1"] = sk1
        self.frames["Skill2"] = sk2



        self.name = StringVar()
        self.name.set("调查员:" + player.name)
        self.namelabel = Label(self.ui, textvariable=self.name, width=15, height=2)
        self.namelabel.place(x=0, y=0)

        self.age = StringVar()
        self.age.set("年龄:" + str(player.age))
        self.agelabel = Label(self.ui, textvariable=self.age, width=5, height=2)
        self.agelabel.place(x=130, y=0)

        self.stre = StringVar()
        self.stre.set("力量:" + str(player.str))
        self.strelabel = Label(self.ui, textvariable=self.stre, width=5, height=2)
        self.strelabel.place(x=180, y=0)

        self.con = StringVar()
        self.con.set("体质:" + str(player.con))
        self.conlabel = Label(self.ui, textvariable=self.con, width=5, height=2)
        self.conlabel.place(x=230, y=0)

        self.siz = StringVar()
        self.siz.set("体型:" + str(player.siz))
        self.sizlabel = Label(self.ui, textvariable=self.siz, width=5, height=2)
        self.sizlabel.place(x=280, y=0)

        self.dex = StringVar()
        self.dex.set("敏捷:" + str(player.dex))
        self.dexlabel = Label(self.ui, textvariable=self.dex, width=5, height=2)
        self.dexlabel.place(x=330, y=0)

        self.app = StringVar()
        self.app.set("外貌:" + str(player.app))
        self.applabel = Label(self.ui, textvariable=self.app, width=5, height=2)
        self.applabel.place(x=380, y=0)

        self.inte = StringVar()
        self.inte.set("智力:" + str(player.int))
        self.intelabel = Label(self.ui, textvariable=self.inte, width=5, height=2)
        self.intelabel.place(x=430, y=0)

        self.pow = StringVar()
        self.pow.set("意志:" + str(player.pow))
        self.powlabel = Label(self.ui, textvariable=self.pow, width=5, height=2)
        self.powlabel.place(x=480, y=0)

        self.edu = StringVar()
        self.edu.set("教育:" + str(player.edu))
        self.edulabel = Label(self.ui, textvariable=self.edu, width=5, height=2)
        self.edulabel.place(x=530, y=0)

        self.luck = StringVar()
        self.luck.set("幸运:" + str(player.luck))
        self.lucklabel = Label(self.ui, textvariable=self.luck, width=5, height=2)
        self.lucklabel.place(x=580, y=0)

        self.summe = StringVar()
        self.summe.set("总和:" + str(player.str + player.con + player.siz + player.dex + player.app + player.int + player.pow + player.edu + player.luck))
        self.summelabel = Label(self.ui, textvariable=self.summe, width=15, height=2)
        self.summelabel.place(x=630, y=0)

        self.selectzhiye = StringVar()
        self.selectzhiye.set("请选择你的职业:")
        self.selectzhiyelabel = Label(self.ui, textvariable=self.selectzhiye, width=15, height=2)
        self.selectzhiyelabel.place(x=195, y=50)
        selectzhiyelabel = CreateToolTip(self.selectzhiyelabel,
                                         "什么是职业？\n职业就是你的PC在参加这个剧本前所从事的行业。你可以根据你的属性(但请不要刻意)"
                                         "来合理的挑选职业，例如一个好看的人有可能从事社交职业，然而一个难看但是受过高等教育的人可能更倾向于科研工作。"
                                         "\n一旦确定了职业，本职技能（点数）也会随之确定。本职技能指的是这个职业的人应该会做什么，比如一个医生"
                                         "应该擅长急救和医学，但是可能并不擅长攀爬和跳跃。与之相对应的称为兴趣技能，兴趣技能是你的PC在工作之余的兴趣所在。还是拿医生举例子，"
                                         "可能因为工作需要他会在茶余饭后经常看书，因此可能会有很强的图书馆使用能力。\n技能通常会有上限限制，当前版本仅支持："
                                         "本职技能上限：80，兴趣技能上限：50。\n（注：超过50（含）的技能意味着你的角色已经可以以此为生，而超过75（含）的技能说明你已经"
                                         "是这个职业的专家了，超过90（含）的技能意味你得编很长一大段的背景来说服KP你的PC是在这个行业已经是名人堂般的存在，否则就是纯属瞎搞")

        self.zhiyeoption = StringVar(self.ui)
        self.zhiyeoption.set(self.zhiye[0])  # default value
        zhiyebox = OptionMenu(self.ui, self.zhiyeoption, *self.zhiye)
        zhiyebox.place(x=300, y=51)

        confirm_zhiye = Button(self.ui, text="决定！",  command=lambda: self.save_zhiye(self.zhiyeoption.get()))
        confirm_zhiye.place(x=390, y=52)


        self.xingyu1 = StringVar()
        self.xingyu1.set("信用评级范围根据职业所确定")
        xingyu1label = Label(self.ui, textvariable=self.xingyu1, width=30, height=2)
        xingyu1label.place(x=230, y=85)
        xingyu1labeldes = CreateToolTip(xingyu1label,"什么是信用？\n"
                                                       "调查员的信用评级取决于角色的选择，和调查员的职业。游戏中，信用评级决定了角色可以使用的金钱数量。"
                                                       "调查员的信用评级初始为0。每个职业都有它特定的信用评级起始点数和增长范围，而玩家在信用评级上的分配也会展现出该调查员不同的风范。"
                                                       "举个例子，“罪犯”可以是一个街头穷困的偷包贼（信用评级9），也可以是一个富有的黑帮头子（信用评级90）。"
                                                       "你可以在信用评级上任意投入技能点，只要不超过职业给定的范围就好。")

        self.xingyu2 = StringVar()
        xingyu2label = Label(self.ui, textvariable=self.xingyu2, width=70, height=1)
        xingyu2label.place(x=100, y=110)

        sex = StringVar()
        sex.set("性别:")
        sexlabel = Label(self.ui, textvariable=sex, width=5, height=2)
        sexlabel.place(x=200, y=135)
        sexinfo = CreateToolTip(sexlabel,"这个不用解释了吧？所以我为什么要做这个hint???")
        initialsex = StringVar()
        initialsex.set("N/A")
        self.entrypower = Entry(self.ui, textvariable=initialsex)
        self.entrypower.place(x=300, y=143)

        living = StringVar()
        living.set("住地:")
        livinglabel = Label(self.ui, textvariable=living, width=5, height=2)
        livinglabel.place(x=200, y=165)
        livinginfo = CreateToolTip(livinglabel, "PC住地，例如东京")
        initialliving = StringVar()
        initialliving.set("N/A")
        self.entrypower = Entry(self.ui, textvariable=initialliving)
        self.entrypower.place(x=300, y=173)

        born = StringVar()
        born.set("出生地:")
        bornlabel = Label(self.ui, textvariable=born, width=5, height=2)
        borninfo = CreateToolTip(bornlabel, "PC出生地，可与上面一致")
        bornlabel.place(x=200, y=195)
        initialborn = StringVar()
        initialborn.set("N/A")
        self.entrypower = Entry(self.ui, textvariable=initialborn)
        self.entrypower.place(x=300, y=203)

        appdes = StringVar()
        appdes.set("形象描述:")
        appdeslabel = Label(self.ui, textvariable=appdes, width=7, height=2)
        appdeslabel.place(x=200, y=225)
        appdesinfo = CreateToolTip(appdeslabel, "PC简单的外貌描述，例如儒雅随和")
        initialappdes = StringVar()
        initialappdes.set("N/A")
        self.entrypower = Entry(self.ui, textvariable=initialappdes)
        self.entrypower.place(x=300, y=233)


        thoughts = StringVar()
        thoughts.set("思想与信念:")
        thoughtslabel = Label(self.ui, textvariable=thoughts, width=8, height=2)
        thoughtslabel.place(x=200, y=255)
        thoughtsinfo = CreateToolTip(thoughtslabel, "PC的信念，例如传火")
        initialthoughts = StringVar()
        initialthoughts.set("N/A")
        self.entrypower = Entry(self.ui, textvariable=initialthoughts)
        self.entrypower.place(x=300, y=263)

        love = StringVar()
        love.set("重要之人:")
        lovelabel = Label(self.ui, textvariable=love, width=8, height=2)
        lovelabel.place(x=200, y=285)
        loveinfo = CreateToolTip(lovelabel, "PC的重要之人，例如带带大师兄")
        initiallove = StringVar()
        initiallove.set("N/A")
        self.entrypower = Entry(self.ui, textvariable=initiallove)
        self.entrypower.place(x=300, y=293)

        place = StringVar()
        place.set("意义非凡之地:")
        placelabel = Label(self.ui, textvariable=place, width=10, height=2)
        placelabel.place(x=195, y=315)
        placeinfo = CreateToolTip(placelabel, "PC的重要之地，例如亚楠村")
        initialplace = StringVar()
        initialplace.set("N/A")
        self.entrypower = Entry(self.ui, textvariable=initialplace)
        self.entrypower.place(x=300, y=323)

        tresure = StringVar()
        tresure.set("宝贵之物:")
        tresurelabel = Label(self.ui, textvariable=tresure, width=8, height=2)
        tresurelabel.place(x=200, y=345)
        tresureinfo = CreateToolTip(tresurelabel, "PC的重要之物，例如XXX打过的篮球")
        initialtresure = StringVar()
        initialtresure.set("N/A")
        self.entrypower = Entry(self.ui, textvariable=initialtresure)
        self.entrypower.place(x=300, y=353)

        special = StringVar()
        special.set("特质:")
        speciallabel = Label(self.ui, textvariable=special, width=8, height=2)
        speciallabel.place(x=200, y=375)
        specialinfo = CreateToolTip(speciallabel, "PC的性格特点，例如就是嘴臭")
        initialspecial = StringVar()
        initialspecial.set("N/A")
        self.entrypower = Entry(self.ui, textvariable=initialspecial)
        self.entrypower.place(x=300, y=383)

        background = StringVar()
        background.set("背景故事：")
        backgroundlabel = Label(self.ui, textvariable=background, width=8, height=2)
        backgroundlabel.place(x=200, y=405)
        backgroundinfo = CreateToolTip(backgroundlabel, "把上面这么多东西串起来，结合你的属性已经你准备点的技能"
                                                        "编一个故事来说服KP你这个角色的存在是合理的")
        # initialbackground = StringVar()
        # initialbackground.set("N/A")
        self.textbackground = Text(self.ui, width=40, height=20)
        self.textbackground.place(x=300, y=413)
        self.textbackground.insert(END,'N/A')


        jump_skillpage1 = Button(self.ui, text="技能页1",  command=lambda: self.show_frame("Skill1"))
        jump_skillpage1.place(x=150, y=690)

        jump_skillpage2 = Button(self.ui, text="技能页2",  command=lambda: self.show_frame("Skill2"))
        jump_skillpage2.place(x=550, y=690)

        create_txt = Button(self.ui, text="人物作成",  command=lambda: self.export_txt())
        create_txt.place(x=350, y=690)


    def export_txt(self):
        tx = 5 + int(self.frames["Skill1"].kuaijientry1.get("1.0",'end-1c')) + int(self.frames["Skill1"].kuaijientry2.get("1.0",'end-1c'))
        if("会计" not in self.jinengdict[self.player.zhiye]):
            if(tx > 50):
                print("非本职技能")
        else:
            if(tx > 80):
                print("过高")


    def save_zhiye(self, zhiye):
        self.player.zhiye = zhiye
        lowbound = str(self.xingyu[zhiye][0])
        highbound = str(self.xingyu[zhiye][1])
        str1 = zhiye + "的信用评级范围是" + lowbound + "至" + highbound
        str2 = "请将至少" + lowbound + "点，至多" + highbound + "点本职技能点分配与技能页中信用那一栏"
        self.xingyu1.set(str1)
        self.xingyu2.set(str2)
        print(self.player.zhiye)

    def show_frame(self, controller):
        frame=self.frames[controller]
        self.ui.pack_forget()
        frame.raise_up()
        # frame.ui.tkraise()



