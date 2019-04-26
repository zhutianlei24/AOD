from tkinter import *
import tkinter.messagebox
from View.ToolTip import *
from Model.PC import *
from View.Skill1 import *
from View.Skill2 import *
import copy

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

        self.dianshudict = {}
        self.dianshudict[''] = 0
        self.dianshudict["护士"] = player.edu * 4
        self.dianshudict["神秘学家"] = player.edu * 4

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

        tmp_player = copy.deepcopy(self.player)

        maxbenzhi = 80
        maxxingqu = 50

        benzhi = 0
        xingqu = 0

        benzhi_total = self.dianshudict[tmp_player.zhiye]
        xingqu_total =tmp_player.int * 2

        ##会计
        if self.frames["Skill1"].kuaijientry1.get("1.0",'end-1c') == '' or self.frames["Skill1"].kuaijientry2.get("1.0",'end-1c') == '':
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "不要给加点那页留空白,不点就乖乖的回去输入0,我抓Exception很累的")
            return
        benzhi = int(self.frames["Skill1"].kuaijientry1.get("1.0",'end-1c'))
        xingqu  = int(self.frames["Skill1"].kuaijientry2.get("1.0",'end-1c'))
        total = tmp_player.kuaiji + benzhi + xingqu

        if "会计" not in self.jinengdict[tmp_player.zhiye]:
            if(benzhi != 0):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "会计不是本职技能哦，不可分配本职技能点哦")
                return
            if(total > maxxingqu):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "会计不是本职技能哦，不可以点超过50哦")
                return
        else:
            if(total > maxbenzhi):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "会计虽然是本职技能，但是不能超过80哦")
                return
        benzhi_total -= benzhi
        xingqu_total -= xingqu
        tmp_player.add_kuaiji(benzhi,xingqu)

        ##人类学
        if self.frames["Skill1"].renleixueentry1.get("1.0",'end-1c') == '' or self.frames["Skill1"].renleixueentry2.get("1.0",'end-1c') == '':
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "不要给加点那页留空白,不点就乖乖的回去输入0,我抓Exception很累的")
            return
        benzhi = int(self.frames["Skill1"].renleixueentry1.get("1.0",'end-1c'))
        xingqu  = int(self.frames["Skill1"].renleixueentry2.get("1.0",'end-1c'))
        total = tmp_player.renleixue + benzhi + xingqu

        if "人类学" not in self.jinengdict[tmp_player.zhiye]:
            if(benzhi != 0):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "人类学不是本职技能哦，不可分配本职技能点哦")
                return
            if(total > maxxingqu):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "人类学不是本职技能哦，不可以点超过50哦")
                return
        else:
            if(total > maxbenzhi):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "人类学虽然是本职技能，但是不能超过80哦")
                return
        benzhi_total -= benzhi
        xingqu_total -= xingqu
        tmp_player.add_renleixue(benzhi,xingqu)


        ##估价
        if self.frames["Skill1"].gujiaentry1.get("1.0",'end-1c') == '' or self.frames["Skill1"].gujiaentry2.get("1.0",'end-1c') == '':
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "不要给加点那页留空白,不点就乖乖的回去输入0,我抓Exception很累的")
            return
        benzhi = int(self.frames["Skill1"].gujiaentry1.get("1.0",'end-1c'))
        xingqu  = int(self.frames["Skill1"].gujiaentry2.get("1.0",'end-1c'))
        total = tmp_player.gujia + benzhi + xingqu

        if "估价" not in self.jinengdict[tmp_player.zhiye]:
            if(benzhi != 0):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "估价不是本职技能哦，不可分配本职技能点哦")
                return
            if(total > maxxingqu):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "估价不是本职技能哦，不可以点超过50哦")
                return
        else:
            if(total > maxbenzhi):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "估价虽然是本职技能，但是不能超过80哦")
                return
        benzhi_total -= benzhi
        xingqu_total -= xingqu
        tmp_player.add_gujia(benzhi,xingqu)

        ##考古学
        if self.frames["Skill1"].kaoguxueentry1.get("1.0",'end-1c') == '' or self.frames["Skill1"].kaoguxueentry2.get("1.0",'end-1c') == '':
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "不要给加点那页留空白,不点就乖乖的回去输入0,我抓Exception很累的")
            return
        benzhi = int(self.frames["Skill1"].kaoguxueentry1.get("1.0",'end-1c'))
        xingqu  = int(self.frames["Skill1"].kaoguxueentry2.get("1.0",'end-1c'))
        total = tmp_player.kaoguxue + benzhi + xingqu

        if "考古学" not in self.jinengdict[tmp_player.zhiye]:
            if(benzhi != 0):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "考古学不是本职技能哦，不可分配本职技能点哦")
                return
            if(total > maxxingqu):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "考古学不是本职技能哦，不可以点超过50哦")
                return
        else:
            if(total > maxbenzhi):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "考古学虽然是本职技能，但是不能超过80哦")
                return
        benzhi_total -= benzhi
        xingqu_total -= xingqu
        tmp_player.add_kaoguxue(benzhi,xingqu)


        ##魅惑
        if self.frames["Skill1"].meihuoentry1.get("1.0",'end-1c') == '' or self.frames["Skill1"].meihuoentry2.get("1.0",'end-1c') == '':
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "不要给加点那页留空白,不点就乖乖的回去输入0,我抓Exception很累的")
            return
        benzhi = int(self.frames["Skill1"].meihuoentry1.get("1.0",'end-1c'))
        xingqu  = int(self.frames["Skill1"].meihuoentry2.get("1.0",'end-1c'))
        total = tmp_player.meihuo + benzhi + xingqu

        if "魅惑" not in self.jinengdict[tmp_player.zhiye]:
            if(benzhi != 0):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "魅惑不是本职技能哦，不可分配本职技能点哦")
                return
            if(total > maxxingqu):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "魅惑不是本职技能哦，不可以点超过50哦")
                return
        else:
            if(total > maxbenzhi):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "魅惑虽然是本职技能，但是不能超过80哦")
                return
        benzhi_total -= benzhi
        xingqu_total -= xingqu
        tmp_player.add_meihuo(benzhi,xingqu)

        ##攀爬
        if self.frames["Skill1"].panpaentry1.get("1.0",'end-1c') == '' or self.frames["Skill1"].panpaentry2.get("1.0",'end-1c') == '':
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "不要给加点那页留空白,不点就乖乖的回去输入0,我抓Exception很累的")
            return
        benzhi = int(self.frames["Skill1"].panpaentry1.get("1.0",'end-1c'))
        xingqu  = int(self.frames["Skill1"].panpaentry2.get("1.0",'end-1c'))
        total = tmp_player.panpa + benzhi + xingqu

        if "攀爬" not in self.jinengdict[tmp_player.zhiye]:
            if(benzhi != 0):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "攀爬不是本职技能哦，不可分配本职技能点哦")
                return
            if(total > maxxingqu):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "攀爬不是本职技能哦，不可以点超过50哦")
                return
        else:
            if(total > maxbenzhi):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "攀爬虽然是本职技能，但是不能超过80哦")
                return
        benzhi_total -= benzhi
        xingqu_total -= xingqu
        tmp_player.add_panpa(benzhi,xingqu)


        ##计算机使用
        if self.frames["Skill1"].jisuanjientry1.get("1.0",'end-1c') == '' or self.frames["Skill1"].jisuanjientry2.get("1.0",'end-1c') == '':
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "不要给加点那页留空白,不点就乖乖的回去输入0,我抓Exception很累的")
            return
        benzhi = int(self.frames["Skill1"].jisuanjientry1.get("1.0",'end-1c'))
        xingqu  = int(self.frames["Skill1"].jisuanjientry2.get("1.0",'end-1c'))
        total = tmp_player.jisuanji + benzhi + xingqu

        if "计算机使用" not in self.jinengdict[tmp_player.zhiye]:
            if(benzhi != 0):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "计算机使用不是本职技能哦，不可分配本职技能点哦")
                return
            if(total > maxxingqu):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "计算机使用不是本职技能哦，不可以点超过50哦")
                return
        else:
            if(total > maxbenzhi):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "计算机使用虽然是本职技能，但是不能超过80哦")
                return
        benzhi_total -= benzhi
        xingqu_total -= xingqu
        tmp_player.add_jisuanji(benzhi,xingqu)

        ##信用评级
        if self.frames["Skill1"].xinyongentry1.get("1.0",'end-1c') == '' or self.frames["Skill1"].xinyongentry2.get("1.0",'end-1c') != '0':
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "信用评级只可使用本职技能点哦，而且一定要点哦，具体信用区间看你的职业下方有提示(不可留空）")
            return
        benzhi = int(self.frames["Skill1"].xinyongentry1.get("1.0",'end-1c'))
        total = tmp_player.xinyong + benzhi

        if total < self.xingyu[tmp_player.zhiye][0] or total > self.xingyu[tmp_player.zhiye][1]:
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "请确认信用评级区间，上面写的明明白白的了！")
            return

        benzhi_total -= benzhi
        tmp_player.add_xinyong(benzhi,0)

        ##乔庄
        if self.frames["Skill1"].qiaozhuangentry1.get("1.0",'end-1c') == '' or self.frames["Skill1"].qiaozhuangentry2.get("1.0",'end-1c') == '':
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "不要给加点那页留空白,不点就乖乖的回去输入0,我抓Exception很累的")
            return
        benzhi = int(self.frames["Skill1"].qiaozhuangentry1.get("1.0",'end-1c'))
        xingqu  = int(self.frames["Skill1"].qiaozhuangentry2.get("1.0",'end-1c'))
        total = tmp_player.qiaozhuang + benzhi + xingqu

        if "乔庄" not in self.jinengdict[tmp_player.zhiye]:
            if(benzhi != 0):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "乔庄不是本职技能哦，不可分配本职技能点哦")
                return
            if(total > maxxingqu):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "乔庄不是本职技能哦，不可以点超过50哦")
                return
        else:
            if(total > maxbenzhi):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "乔庄虽然是本职技能，但是不能超过80哦")
                return
        benzhi_total -= benzhi
        xingqu_total -= xingqu
        tmp_player.add_qiaozhuang(benzhi,xingqu)


        ##闪避
        if self.frames["Skill1"].shanbientry1.get("1.0",'end-1c') == '' or self.frames["Skill1"].shanbientry2.get("1.0",'end-1c') == '':
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "不要给加点那页留空白,不点就乖乖的回去输入0,我抓Exception很累的")
            return
        benzhi = int(self.frames["Skill1"].shanbientry1.get("1.0",'end-1c'))
        xingqu  = int(self.frames["Skill1"].shanbientry2.get("1.0",'end-1c'))
        total = tmp_player.shanbi + benzhi + xingqu

        if "闪避" not in self.jinengdict[tmp_player.zhiye]:
            if(benzhi != 0):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "闪避不是本职技能哦，不可分配本职技能点哦")
                return
            if(total > maxxingqu):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "闪避不是本职技能哦，不可以点超过50哦")
                return
        else:
            if(total > maxbenzhi):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "闪避虽然是本职技能，但是不能超过80哦")
                return
        benzhi_total -= benzhi
        xingqu_total -= xingqu
        tmp_player.add_shanbi(benzhi,xingqu)


        ##汽车驾驶
        if self.frames["Skill1"].qichejiashientry1.get("1.0",'end-1c') == '' or self.frames["Skill1"].qichejiashientry2.get("1.0",'end-1c') == '':
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "不要给加点那页留空白,不点就乖乖的回去输入0,我抓Exception很累的")
            return
        benzhi = int(self.frames["Skill1"].qichejiashientry1.get("1.0",'end-1c'))
        xingqu  = int(self.frames["Skill1"].qichejiashientry2.get("1.0",'end-1c'))
        total = tmp_player.qichejiashi + benzhi + xingqu

        if "汽车驾驶" not in self.jinengdict[tmp_player.zhiye]:
            if(benzhi != 0):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "汽车驾驶不是本职技能哦，不可分配本职技能点哦")
                return
            if(total > maxxingqu):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "汽车驾驶不是本职技能哦，不可以点超过50哦")
                return
        else:
            if(total > maxbenzhi):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "汽车驾驶虽然是本职技能，但是不能超过80哦")
                return
        benzhi_total -= benzhi
        xingqu_total -= xingqu
        tmp_player.add_qichejiashi(benzhi,xingqu)

        ##电器维修
        if self.frames["Skill1"].dianqiweixiuentry1.get("1.0",'end-1c') == '' or self.frames["Skill1"].dianqiweixiuentry2.get("1.0",'end-1c') == '':
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "不要给加点那页留空白,不点就乖乖的回去输入0,我抓Exception很累的")
            return
        benzhi = int(self.frames["Skill1"].dianqiweixiuentry1.get("1.0",'end-1c'))
        xingqu  = int(self.frames["Skill1"].dianqiweixiuentry1.get("1.0",'end-1c'))
        total = tmp_player.dianqiweixiu + benzhi + xingqu

        if "电器维修" not in self.jinengdict[tmp_player.zhiye]:
            if(benzhi != 0):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "电器维修不是本职技能哦，不可分配本职技能点哦")
                return
            if(total > maxxingqu):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "电器维修不是本职技能哦，不可以点超过50哦")
                return
        else:
            if(total > maxbenzhi):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "电器维修虽然是本职技能，但是不能超过80哦")
                return
        benzhi_total -= benzhi
        xingqu_total -= xingqu
        tmp_player.add_dianqiweixiu(benzhi,xingqu)


        ##电子学
        if self.frames["Skill1"].dianzixueentry1.get("1.0",'end-1c') == '' or self.frames["Skill1"].dianzixueentry2.get("1.0",'end-1c') == '':
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "不要给加点那页留空白,不点就乖乖的回去输入0,我抓Exception很累的")
            return
        benzhi = int(self.frames["Skill1"].dianzixueentry1.get("1.0",'end-1c'))
        xingqu  = int(self.frames["Skill1"].dianzixueentry2.get("1.0",'end-1c'))
        total = tmp_player.dianzixue + benzhi + xingqu

        if "电子学" not in self.jinengdict[tmp_player.zhiye]:
            if(benzhi != 0):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "电子学不是本职技能哦，不可分配本职技能点哦")
                return
            if(total > maxxingqu):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "电子学不是本职技能哦，不可以点超过50哦")
                return
        else:
            if(total > maxbenzhi):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "电子学虽然是本职技能，但是不能超过80哦")
                return
        benzhi_total -= benzhi
        xingqu_total -= xingqu
        tmp_player.add_dianzixue(benzhi,xingqu)


        ##话术
        if self.frames["Skill1"].huashuentry1.get("1.0",'end-1c') == '' or self.frames["Skill1"].huashuentry2.get("1.0",'end-1c') == '':
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "不要给加点那页留空白,不点就乖乖的回去输入0,我抓Exception很累的")
            return
        benzhi = int(self.frames["Skill1"].huashuentry1.get("1.0",'end-1c'))
        xingqu  = int(self.frames["Skill1"].huashuentry2.get("1.0",'end-1c'))
        total = tmp_player.huashu + benzhi + xingqu

        if "话术" not in self.jinengdict[tmp_player.zhiye]:
            if(benzhi != 0):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "话术不是本职技能哦，不可分配本职技能点哦")
                return
            if(total > maxxingqu):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "话术不是本职技能哦，不可以点超过50哦")
                return
        else:
            if(total > maxbenzhi):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "话术虽然是本职技能，但是不能超过80哦")
                return
        benzhi_total -= benzhi
        xingqu_total -= xingqu
        tmp_player.add_huashu(benzhi,xingqu)


        ##斗殴
        if self.frames["Skill1"].dououentry1.get("1.0",'end-1c') == '' or self.frames["Skill1"].dououentry2.get("1.0",'end-1c') == '':
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "不要给加点那页留空白,不点就乖乖的回去输入0,我抓Exception很累的")
            return
        benzhi = int(self.frames["Skill1"].dououentry1.get("1.0",'end-1c'))
        xingqu  = int(self.frames["Skill1"].dououentry2.get("1.0",'end-1c'))
        total = tmp_player.douou + benzhi + xingqu

        if "斗殴" not in self.jinengdict[tmp_player.zhiye]:
            if(benzhi != 0):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "斗殴不是本职技能哦，不可分配本职技能点哦")
                return
            if(total > maxxingqu):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "斗殴不是本职技能哦，不可以点超过50哦")
                return
        else:
            if(total > maxbenzhi):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "斗殴虽然是本职技能，但是不能超过80哦")
                return
        benzhi_total -= benzhi
        xingqu_total -= xingqu
        tmp_player.add_douou(benzhi,xingqu)

        ##手枪
        if self.frames["Skill1"].shouqiangentry1.get("1.0",'end-1c') == '' or self.frames["Skill1"].shouqiangentry2.get("1.0",'end-1c') == '':
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "不要给加点那页留空白,不点就乖乖的回去输入0,我抓Exception很累的")
            return
        benzhi = int(self.frames["Skill1"].shouqiangentry1.get("1.0",'end-1c'))
        xingqu  = int(self.frames["Skill1"].shouqiangentry2.get("1.0",'end-1c'))
        total = tmp_player.shouqiang + benzhi + xingqu

        if "手枪" not in self.jinengdict[tmp_player.zhiye]:
            if(benzhi != 0):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "手枪不是本职技能哦，不可分配本职技能点哦")
                return
            if(total > maxxingqu):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "手枪不是本职技能哦，不可以点超过50哦")
                return
        else:
            if(total > maxbenzhi):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "手枪虽然是本职技能，但是不能超过80哦")
                return
        benzhi_total -= benzhi
        xingqu_total -= xingqu
        tmp_player.add_shouqiang(benzhi,xingqu)

        ##急救
        if self.frames["Skill1"].jijiuentry1.get("1.0",'end-1c') == '' or self.frames["Skill1"].jijiuentry2.get("1.0",'end-1c') == '':
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "不要给加点那页留空白,不点就乖乖的回去输入0,我抓Exception很累的")
            return
        benzhi = int(self.frames["Skill1"].jijiuentry1.get("1.0",'end-1c'))
        xingqu  = int(self.frames["Skill1"].jijiuentry2.get("1.0",'end-1c'))
        total = tmp_player.jijiu + benzhi + xingqu

        if "急救" not in self.jinengdict[tmp_player.zhiye]:
            if(benzhi != 0):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "急救不是本职技能哦，不可分配本职技能点哦")
                return
            if(total > maxxingqu):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "急救不是本职技能哦，不可以点超过50哦")
                return
        else:
            if(total > maxbenzhi):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "急救虽然是本职技能，但是不能超过80哦")
                return
        benzhi_total -= benzhi
        xingqu_total -= xingqu
        tmp_player.add_jijiu(benzhi,xingqu)


        ##历史
        if self.frames["Skill1"].lishientry1.get("1.0",'end-1c') == '' or self.frames["Skill1"].lishientry2.get("1.0",'end-1c') == '':
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "不要给加点那页留空白,不点就乖乖的回去输入0,我抓Exception很累的")
            return
        benzhi = int(self.frames["Skill1"].lishientry1.get("1.0",'end-1c'))
        xingqu  = int(self.frames["Skill1"].lishientry2.get("1.0",'end-1c'))
        total = tmp_player.lishi + benzhi + xingqu

        if "历史" not in self.jinengdict[tmp_player.zhiye]:
            if(benzhi != 0):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "历史不是本职技能哦，不可分配本职技能点哦")
                return
            if(total > maxxingqu):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "历史不是本职技能哦，不可以点超过50哦")
                return
        else:
            if(total > maxbenzhi):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "历史虽然是本职技能，但是不能超过80哦")
                return
        benzhi_total -= benzhi
        xingqu_total -= xingqu
        tmp_player.add_lishi(benzhi,xingqu)

        ##恐吓
        if self.frames["Skill1"].kongheentry1.get("1.0",'end-1c') == '' or self.frames["Skill1"].kongheentry2.get("1.0",'end-1c') == '':
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "不要给加点那页留空白,不点就乖乖的回去输入0,我抓Exception很累的")
            return
        benzhi = int(self.frames["Skill1"].kongheentry1.get("1.0",'end-1c'))
        xingqu  = int(self.frames["Skill1"].kongheentry2.get("1.0",'end-1c'))
        total = tmp_player.konghe + benzhi + xingqu

        if "恐吓" not in self.jinengdict[tmp_player.zhiye]:
            if(benzhi != 0):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "恐吓不是本职技能哦，不可分配本职技能点哦")
                return
            if(total > maxxingqu):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "恐吓不是本职技能哦，不可以点超过50哦")
                return
        else:
            if(total > maxbenzhi):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "恐吓虽然是本职技能，但是不能超过80哦")
                return
        benzhi_total -= benzhi
        xingqu_total -= xingqu
        tmp_player.add_konghe(benzhi,xingqu)


        ##跳跃
        if self.frames["Skill1"].tiaoyueentry1.get("1.0",'end-1c') == '' or self.frames["Skill1"].tiaoyueentry2.get("1.0",'end-1c') == '':
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "不要给加点那页留空白,不点就乖乖的回去输入0,我抓Exception很累的")
            return
        benzhi = int(self.frames["Skill1"].tiaoyueentry1.get("1.0",'end-1c'))
        xingqu  = int(self.frames["Skill1"].tiaoyueentry2.get("1.0",'end-1c'))
        total = tmp_player.tiaoyue + benzhi + xingqu

        if "跳跃" not in self.jinengdict[tmp_player.zhiye]:
            if(benzhi != 0):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "跳跃不是本职技能哦，不可分配本职技能点哦")
                return
            if(total > maxxingqu):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "跳跃不是本职技能哦，不可以点超过50哦")
                return
        else:
            if(total > maxbenzhi):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "跳跃虽然是本职技能，但是不能超过80哦")
                return
        benzhi_total -= benzhi
        xingqu_total -= xingqu
        tmp_player.add_tiaoyue(benzhi,xingqu)

        ##法律
        if self.frames["Skill1"].falventry1.get("1.0",'end-1c') == '' or self.frames["Skill1"].falventry2.get("1.0",'end-1c') == '':
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "不要给加点那页留空白,不点就乖乖的回去输入0,我抓Exception很累的")
            return
        benzhi = int(self.frames["Skill1"].falventry1.get("1.0",'end-1c'))
        xingqu  = int(self.frames["Skill1"].falventry2.get("1.0",'end-1c'))
        total = tmp_player.falv + benzhi + xingqu

        if "法律" not in self.jinengdict[tmp_player.zhiye]:
            if(benzhi != 0):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "法律不是本职技能哦，不可分配本职技能点哦")
                return
            if(total > maxxingqu):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "法律不是本职技能哦，不可以点超过50哦")
                return
        else:
            if(total > maxbenzhi):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "法律虽然是本职技能，但是不能超过80哦")
                return
        benzhi_total -= benzhi
        xingqu_total -= xingqu
        tmp_player.add_falv(benzhi,xingqu)

        ##图书馆使用
        if self.frames["Skill1"].tushuguanentry1.get("1.0",'end-1c') == '' or self.frames["Skill1"].tushuguanentry2.get("1.0",'end-1c') == '':
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "不要给加点那页留空白,不点就乖乖的回去输入0,我抓Exception很累的")
            return
        benzhi = int(self.frames["Skill1"].tushuguanentry1.get("1.0",'end-1c'))
        xingqu  = int(self.frames["Skill1"].tushuguanentry2.get("1.0",'end-1c'))
        total = tmp_player.tushuguan + benzhi + xingqu

        if "图书馆使用" not in self.jinengdict[tmp_player.zhiye]:
            if(benzhi != 0):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "图书馆使用不是本职技能哦，不可分配本职技能点哦")
                return
            if(total > maxxingqu):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "图书馆使用不是本职技能哦，不可以点超过50哦")
                return
        else:
            if(total > maxbenzhi):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "图书馆使用虽然是本职技能，但是不能超过80哦")
                return
        benzhi_total -= benzhi
        xingqu_total -= xingqu
        tmp_player.add_tushuguan(benzhi,xingqu)


        ##聆听
        if self.frames["Skill1"].lingtingentry1.get("1.0",'end-1c') == '' or self.frames["Skill1"].lingtingentry2.get("1.0",'end-1c') == '':
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "不要给加点那页留空白,不点就乖乖的回去输入0,我抓Exception很累的")
            return
        benzhi = int(self.frames["Skill1"].lingtingentry1.get("1.0",'end-1c'))
        xingqu  = int(self.frames["Skill1"].lingtingentry2.get("1.0",'end-1c'))
        total = tmp_player.lingting + benzhi + xingqu

        if "聆听" not in self.jinengdict[tmp_player.zhiye]:
            if(benzhi != 0):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "聆听不是本职技能哦，不可分配本职技能点哦")
                return
            if(total > maxxingqu):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "聆听不是本职技能哦，不可以点超过50哦")
                return
        else:
            if(total > maxbenzhi):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "聆听虽然是本职技能，但是不能超过80哦")
                return
        benzhi_total -= benzhi
        xingqu_total -= xingqu
        tmp_player.add_lingting(benzhi,xingqu)


        ##锁匠
        if self.frames["Skill1"].suojiangentry1.get("1.0",'end-1c') == '' or self.frames["Skill1"].suojiangentry2.get("1.0",'end-1c') == '':
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "不要给加点那页留空白,不点就乖乖的回去输入0,我抓Exception很累的")
            return
        benzhi = int(self.frames["Skill1"].suojiangentry1.get("1.0",'end-1c'))
        xingqu  = int(self.frames["Skill1"].suojiangentry2.get("1.0",'end-1c'))
        total = tmp_player.suojiang + benzhi + xingqu

        if "锁匠" not in self.jinengdict[tmp_player.zhiye]:
            if(benzhi != 0):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "锁匠不是本职技能哦，不可分配本职技能点哦")
                return
            if(total > maxxingqu):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "锁匠不是本职技能哦，不可以点超过50哦")
                return
        else:
            if(total > maxbenzhi):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "锁匠虽然是本职技能，但是不能超过80哦")
                return
        benzhi_total -= benzhi
        xingqu_total -= xingqu
        tmp_player.add_suojiang(benzhi,xingqu)


        ##机械维修
        if self.frames["Skill1"].jixieweixiuentry1.get("1.0",'end-1c') == '' or self.frames["Skill1"].jixieweixiuentry2.get("1.0",'end-1c') == '':
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "不要给加点那页留空白,不点就乖乖的回去输入0,我抓Exception很累的")
            return
        benzhi = int(self.frames["Skill1"].jixieweixiuentry1.get("1.0",'end-1c'))
        xingqu  = int(self.frames["Skill1"].jixieweixiuentry2.get("1.0",'end-1c'))
        total = tmp_player.jixieweixiu + benzhi + xingqu

        if "机械维修" not in self.jinengdict[tmp_player.zhiye]:
            if(benzhi != 0):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "机械维修不是本职技能哦，不可分配本职技能点哦")
                return
            if(total > maxxingqu):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "机械维修不是本职技能哦，不可以点超过50哦")
                return
        else:
            if(total > maxbenzhi):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "机械维修虽然是本职技能，但是不能超过80哦")
                return
        benzhi_total -= benzhi
        xingqu_total -= xingqu
        tmp_player.add_jixieweixiu(benzhi,xingqu)


        ##医学
        if self.frames["Skill1"].yixueentry1.get("1.0",'end-1c') == '' or self.frames["Skill1"].yixueentry2.get("1.0",'end-1c') == '':
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "不要给加点那页留空白,不点就乖乖的回去输入0,我抓Exception很累的")
            return
        benzhi = int(self.frames["Skill1"].yixueentry1.get("1.0",'end-1c'))
        xingqu  = int(self.frames["Skill1"].yixueentry2.get("1.0",'end-1c'))
        total = tmp_player.yixue + benzhi + xingqu

        if "医学" not in self.jinengdict[tmp_player.zhiye]:
            if(benzhi != 0):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "医学不是本职技能哦，不可分配本职技能点哦")
                return
            if(total > maxxingqu):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "医学不是本职技能哦，不可以点超过50哦")
                return
        else:
            if(total > maxbenzhi):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "医学虽然是本职技能，但是不能超过80哦")
                return
        benzhi_total -= benzhi
        xingqu_total -= xingqu
        tmp_player.add_yixue(benzhi,xingqu)


        ##博物学
        if self.frames["Skill1"].bowuxueentry1.get("1.0",'end-1c') == '' or self.frames["Skill1"].bowuxueentry2.get("1.0",'end-1c') == '':
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "不要给加点那页留空白,不点就乖乖的回去输入0,我抓Exception很累的")
            return
        benzhi = int(self.frames["Skill1"].bowuxueentry1.get("1.0",'end-1c'))
        xingqu  = int(self.frames["Skill1"].bowuxueentry2.get("1.0",'end-1c'))
        total = tmp_player.bowuxue + benzhi + xingqu

        if "博物学" not in self.jinengdict[tmp_player.zhiye]:
            if(benzhi != 0):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "博物学不是本职技能哦，不可分配本职技能点哦")
                return
            if(total > maxxingqu):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "博物学不是本职技能哦，不可以点超过50哦")
                return
        else:
            if(total > maxbenzhi):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "博物学虽然是本职技能，但是不能超过80哦")
                return
        benzhi_total -= benzhi
        xingqu_total -= xingqu
        tmp_player.add_bowuxue(benzhi,xingqu)


        ##领航
        if self.frames["Skill1"].linghangentry1.get("1.0",'end-1c') == '' or self.frames["Skill1"].linghangentry2.get("1.0",'end-1c') == '':
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "不要给加点那页留空白,不点就乖乖的回去输入0,我抓Exception很累的")
            return
        benzhi = int(self.frames["Skill1"].linghangentry1.get("1.0",'end-1c'))
        xingqu  = int(self.frames["Skill1"].linghangentry2.get("1.0",'end-1c'))
        total = tmp_player.linghang + benzhi + xingqu

        if "领航" not in self.jinengdict[tmp_player.zhiye]:
            if(benzhi != 0):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "领航不是本职技能哦，不可分配本职技能点哦")
                return
            if(total > maxxingqu):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "领航不是本职技能哦，不可以点超过50哦")
                return
        else:
            if(total > maxbenzhi):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "领航虽然是本职技能，但是不能超过80哦")
                return
        benzhi_total -= benzhi
        xingqu_total -= xingqu
        tmp_player.add_linghang(benzhi,xingqu)

        ##神秘学
        if self.frames["Skill1"].shengmixueentry1.get("1.0",'end-1c') == '' or self.frames["Skill1"].shengmixueentry2.get("1.0",'end-1c') == '':
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "不要给加点那页留空白,不点就乖乖的回去输入0,我抓Exception很累的")
            return
        benzhi = int(self.frames["Skill1"].shengmixueentry1.get("1.0",'end-1c'))
        xingqu  = int(self.frames["Skill1"].shengmixueentry2.get("1.0",'end-1c'))
        total = tmp_player.shenmixue + benzhi + xingqu

        if "神秘学" not in self.jinengdict[tmp_player.zhiye]:
            if(benzhi != 0):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "神秘学不是本职技能哦，不可分配本职技能点哦")
                return
            if(total > maxxingqu):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "神秘学不是本职技能哦，不可以点超过50哦")
                return
        else:
            if(total > maxbenzhi):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "神秘学虽然是本职技能，但是不能超过80哦")
                return
        benzhi_total -= benzhi
        xingqu_total -= xingqu
        tmp_player.add_shenmixue(benzhi,xingqu)


        ##操作重型机械
        if self.frames["Skill1"].zhongxingjixieentry1.get("1.0",'end-1c') == '' or self.frames["Skill1"].zhongxingjixieentry2.get("1.0",'end-1c') == '':
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "不要给加点那页留空白,不点就乖乖的回去输入0,我抓Exception很累的")
            return
        benzhi = int(self.frames["Skill1"].zhongxingjixieentry1.get("1.0",'end-1c'))
        xingqu  = int(self.frames["Skill1"].zhongxingjixieentry2.get("1.0",'end-1c'))
        total = tmp_player.zhongxingjixie + benzhi + xingqu

        if "操作重型机械" not in self.jinengdict[tmp_player.zhiye]:
            if(benzhi != 0):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "操作重型机械不是本职技能哦，不可分配本职技能点哦")
                return
            if(total > maxxingqu):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "操作重型机械不是本职技能哦，不可以点超过50哦")
                return
        else:
            if(total > maxbenzhi):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "操作重型机械虽然是本职技能，但是不能超过80哦")
                return
        benzhi_total -= benzhi
        xingqu_total -= xingqu
        tmp_player.add_zhongxingjixie(benzhi,xingqu)


        ##说服
        if self.frames["Skill1"].shuofuentry1.get("1.0",'end-1c') == '' or self.frames["Skill1"].shuofuentry2.get("1.0",'end-1c') == '':
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "不要给加点那页留空白,不点就乖乖的回去输入0,我抓Exception很累的")
            return
        benzhi = int(self.frames["Skill1"].shuofuentry1.get("1.0",'end-1c'))
        xingqu  = int(self.frames["Skill1"].shuofuentry2.get("1.0",'end-1c'))
        total = tmp_player.shuofu + benzhi + xingqu

        if "说服" not in self.jinengdict[tmp_player.zhiye]:
            if(benzhi != 0):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "说服不是本职技能哦，不可分配本职技能点哦")
                return
            if(total > maxxingqu):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "说服不是本职技能哦，不可以点超过50哦")
                return
        else:
            if(total > maxbenzhi):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "说服虽然是本职技能，但是不能超过80哦")
                return
        benzhi_total -= benzhi
        xingqu_total -= xingqu
        tmp_player.add_shuofu(benzhi,xingqu)

        ##精神分析
        if self.frames["Skill1"].jingshengfengxientry1.get("1.0",'end-1c') == '' or self.frames["Skill1"].jingshengfengxientry2.get("1.0",'end-1c') == '':
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "不要给加点那页留空白,不点就乖乖的回去输入0,我抓Exception很累的")
            return
        benzhi = int(self.frames["Skill1"].jingshengfengxientry1.get("1.0",'end-1c'))
        xingqu  = int(self.frames["Skill1"].jingshengfengxientry2.get("1.0",'end-1c'))
        total = tmp_player.jingshengfenxi + benzhi + xingqu

        if "精神分析" not in self.jinengdict[tmp_player.zhiye]:
            if(benzhi != 0):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "精神分析不是本职技能哦，不可分配本职技能点哦")
                return
            if(total > maxxingqu):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "精神分析不是本职技能哦，不可以点超过50哦")
                return
        else:
            if(total > maxbenzhi):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "精神分析虽然是本职技能，但是不能超过80哦")
                return
        benzhi_total -= benzhi
        xingqu_total -= xingqu
        tmp_player.add_jingshengfenxi(benzhi,xingqu)

        ##心理学
        if self.frames["Skill1"].xinglixueentry1.get("1.0",'end-1c') == '' or self.frames["Skill1"].xinglixueentry2.get("1.0",'end-1c') == '':
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "不要给加点那页留空白,不点就乖乖的回去输入0,我抓Exception很累的")
            return
        benzhi = int(self.frames["Skill1"].xinglixueentry1.get("1.0",'end-1c'))
        xingqu  = int(self.frames["Skill1"].xinglixueentry2.get("1.0",'end-1c'))
        total = tmp_player.xinlixue + benzhi + xingqu

        if "心理学" not in self.jinengdict[tmp_player.zhiye]:
            if(benzhi != 0):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "心理学不是本职技能哦，不可分配本职技能点哦")
                return
            if(total > maxxingqu):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "心理学不是本职技能哦，不可以点超过50哦")
                return
        else:
            if(total > maxbenzhi):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "心理学虽然是本职技能，但是不能超过80哦")
                return
        benzhi_total -= benzhi
        xingqu_total -= xingqu
        tmp_player.add_xinlixue(benzhi,xingqu)

        ##骑术
        if self.frames["Skill1"].qishuentry1.get("1.0",'end-1c') == '' or self.frames["Skill1"].qishuentry2.get("1.0",'end-1c') == '':
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "不要给加点那页留空白,不点就乖乖的回去输入0,我抓Exception很累的")
            return
        benzhi = int(self.frames["Skill1"].qishuentry1.get("1.0",'end-1c'))
        xingqu  = int(self.frames["Skill1"].qishuentry2.get("1.0",'end-1c'))
        total = tmp_player.qishu + benzhi + xingqu

        if "骑术" not in self.jinengdict[tmp_player.zhiye]:
            if(benzhi != 0):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "骑术不是本职技能哦，不可分配本职技能点哦")
                return
            if(total > maxxingqu):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "骑术不是本职技能哦，不可以点超过50哦")
                return
        else:
            if(total > maxbenzhi):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "骑术虽然是本职技能，但是不能超过80哦")
                return
        benzhi_total -= benzhi
        xingqu_total -= xingqu
        tmp_player.add_qishu(benzhi,xingqu)


        ##妙手
        if self.frames["Skill1"].miaoshouentry1.get("1.0",'end-1c') == '' or self.frames["Skill1"].miaoshouentry2.get("1.0",'end-1c') == '':
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "不要给加点那页留空白,不点就乖乖的回去输入0,我抓Exception很累的")
            return
        benzhi = int(self.frames["Skill1"].miaoshouentry1.get("1.0",'end-1c'))
        xingqu  = int(self.frames["Skill1"].miaoshouentry2.get("1.0",'end-1c'))
        total = tmp_player.miaoshou + benzhi + xingqu

        if "妙手" not in self.jinengdict[tmp_player.zhiye]:
            if(benzhi != 0):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "妙手不是本职技能哦，不可分配本职技能点哦")
                return
            if(total > maxxingqu):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "妙手不是本职技能哦，不可以点超过50哦")
                return
        else:
            if(total > maxbenzhi):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "妙手虽然是本职技能，但是不能超过80哦")
                return
        benzhi_total -= benzhi
        xingqu_total -= xingqu
        tmp_player.add_miaoshou(benzhi,xingqu)


        ##侦查
        if self.frames["Skill1"].zhengchaentry1.get("1.0",'end-1c') == '' or self.frames["Skill1"].zhengchaentry2.get("1.0",'end-1c') == '':
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "不要给加点那页留空白,不点就乖乖的回去输入0,我抓Exception很累的")
            return
        benzhi = int(self.frames["Skill1"].zhengchaentry1.get("1.0",'end-1c'))
        xingqu  = int(self.frames["Skill1"].zhengchaentry2.get("1.0",'end-1c'))
        total = tmp_player.zhencha + benzhi + xingqu

        if "侦查" not in self.jinengdict[tmp_player.zhiye]:
            if(benzhi != 0):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "侦查不是本职技能哦，不可分配本职技能点哦")
                return
            if(total > maxxingqu):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "侦查不是本职技能哦，不可以点超过50哦")
                return
        else:
            if(total > maxbenzhi):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "侦查虽然是本职技能，但是不能超过80哦")
                return
        benzhi_total -= benzhi
        xingqu_total -= xingqu
        tmp_player.add_zhencha(benzhi,xingqu)


        ##潜行
        if self.frames["Skill1"].qianxingentry1.get("1.0",'end-1c') == '' or self.frames["Skill1"].qianxingentry2.get("1.0",'end-1c') == '':
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "不要给加点那页留空白,不点就乖乖的回去输入0,我抓Exception很累的")
            return
        benzhi = int(self.frames["Skill1"].qianxingentry1.get("1.0",'end-1c'))
        xingqu  = int(self.frames["Skill1"].qianxingentry2.get("1.0",'end-1c'))
        total = tmp_player.qianxing + benzhi + xingqu

        if "潜行" not in self.jinengdict[tmp_player.zhiye]:
            if(benzhi != 0):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "潜行不是本职技能哦，不可分配本职技能点哦")
                return
            if(total > maxxingqu):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "潜行不是本职技能哦，不可以点超过50哦")
                return
        else:
            if(total > maxbenzhi):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "潜行虽然是本职技能，但是不能超过80哦")
                return
        benzhi_total -= benzhi
        xingqu_total -= xingqu
        tmp_player.add_qianxing(benzhi,xingqu)

        ##游泳
        if self.frames["Skill1"].youyongentry1.get("1.0",'end-1c') == '' or self.frames["Skill1"].youyongentry2.get("1.0",'end-1c') == '':
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "不要给加点那页留空白,不点就乖乖的回去输入0,我抓Exception很累的")
            return
        benzhi = int(self.frames["Skill1"].youyongentry1.get("1.0",'end-1c'))
        xingqu  = int(self.frames["Skill1"].youyongentry2.get("1.0",'end-1c'))
        total = tmp_player.youyong + benzhi + xingqu

        if "游泳" not in self.jinengdict[tmp_player.zhiye]:
            if(benzhi != 0):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "游泳不是本职技能哦，不可分配本职技能点哦")
                return
            if(total > maxxingqu):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "游泳不是本职技能哦，不可以点超过50哦")
                return
        else:
            if(total > maxbenzhi):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "游泳虽然是本职技能，但是不能超过80哦")
                return
        benzhi_total -= benzhi
        xingqu_total -= xingqu
        tmp_player.add_youyong(benzhi,xingqu)


        ##投掷
        if self.frames["Skill1"].touzhientry1.get("1.0",'end-1c') == '' or self.frames["Skill1"].touzhientry2.get("1.0",'end-1c') == '':
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "不要给加点那页留空白,不点就乖乖的回去输入0,我抓Exception很累的")
            return
        benzhi = int(self.frames["Skill1"].touzhientry1.get("1.0",'end-1c'))
        xingqu  = int(self.frames["Skill1"].touzhientry2.get("1.0",'end-1c'))
        total = tmp_player.touzhi + benzhi + xingqu

        if "投掷" not in self.jinengdict[tmp_player.zhiye]:
            if(benzhi != 0):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "投掷不是本职技能哦，不可分配本职技能点哦")
                return
            if(total > maxxingqu):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "投掷不是本职技能哦，不可以点超过50哦")
                return
        else:
            if(total > maxbenzhi):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "投掷虽然是本职技能，但是不能超过80哦")
                return
        benzhi_total -= benzhi
        xingqu_total -= xingqu
        tmp_player.add_touzhi(benzhi,xingqu)


        ##追踪
        if self.frames["Skill1"].zhuizongentry1.get("1.0",'end-1c') == '' or self.frames["Skill1"].zhuizongentry2.get("1.0",'end-1c') == '':
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "不要给加点那页留空白,不点就乖乖的回去输入0,我抓Exception很累的")
            return
        benzhi = int(self.frames["Skill1"].zhuizongentry1.get("1.0",'end-1c'))
        xingqu  = int(self.frames["Skill1"].zhuizongentry2.get("1.0",'end-1c'))
        total = tmp_player.zhuizong + benzhi + xingqu

        if "追踪" not in self.jinengdict[tmp_player.zhiye]:
            if(benzhi != 0):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "追踪不是本职技能哦，不可分配本职技能点哦")
                return
            if(total > maxxingqu):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "追踪不是本职技能哦，不可以点超过50哦")
                return
        else:
            if(total > maxbenzhi):
                tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "追踪虽然是本职技能，但是不能超过80哦")
                return
        benzhi_total -= benzhi
        xingqu_total -= xingqu
        tmp_player.add_zhuizong(benzhi,xingqu)

        if(benzhi_total < 0):
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "小贪心哦，本职点数用的多了哦，再回去口算一下")
            return

        if(xingqu_total < 0):
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "小贪心哦，兴趣点数用的多了哦，再回去口算一下")
            return




        print("本职还剩" + str(benzhi_total))
        print("兴趣还剩" + str(xingqu_total))





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



