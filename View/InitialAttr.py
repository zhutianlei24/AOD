import random
from tkinter import *
from View.Skills import *
import tkinter.messagebox
from View.ToolTip import *
from Model.PC import *

class InitialAttr():

    def __init__(self, master):
        self.root = master
        self.ui = Frame(self.root,)
        self.ui.pack(fill=BOTH, expand=True)

        hello = StringVar()
        hello.set("请在此处输入你的姓名，年龄和九大属性，确认后不可修改")
        hellolabel = Label(self.ui, textvariable=hello, width=100, height=2)
        # hellolabel.pack()
        hellolabel.place(x=-10, y=0)

        name = StringVar()
        name.set("姓名：")
        self.namelabel = Label(self.ui, textvariable=name, width=80, height=2)
        self.namelabel.place(x=-50, y=50)
        nameinfo = CreateToolTip(self.namelabel,
                                 "来一个狂拽酷炫吊炸天的名字吧！比如说璃莹殇·安洁莉娜·樱雪羽晗灵·血丽魑·魅·J·Q·"
                                 "安塔利亚·伤梦薰魅·海瑟薇·蔷薇玫瑰泪·羽灵·邪儿·凡多姆海威恩·夏影·琉璃舞·雅·"
                                 "蕾玥瑷雅·曦梦月·玥蓝·岚樱·紫蝶·丽馨·蕾琦洛·凤·颜鸢·希洛·玖兮·雨烟·叶洛莉兰·"
                                 "凝羽冰·泪伊如冰落·殇心樱语冰凌伊娜·洛丽塔紫心爱·蝶梦如璃紫陌悠千艳·优花梦冰玫瑰灵伤如爱·"
                                 "晶泪墨阳云筱残伤雅·琉璃爱梦莲泪·冰雪殇璃陌梦·爱樱沫渺·落璃琴依语·千梦然丝伤·可薇·茉殇黎·"
                                 "幽幻紫银·泪如韵影倾乐兰慕·冰雪殇璃陌梦·凝羽冰蓝璃·泪伊如琉璃爱梦莲泪·冰雅泪落冰紫蝶梦·"
                                 "殇心樱语冰凌伊蝶梦如·璃紫陌悠千艳优墨阳云筱残·雪莲茉·伊文思·蕊夏清·碎墨音·芊乐梦黛怡·"
                                 "墨丽莎·梦灵苏魅香·紫蓝幽幻倾城萌美迷离·茉莉白嫩爱凤风魑·殇泪花如霜梦兰·萝莉心梦妖丽百千艳·"
                                 "瑰百合香珠合梦喃·泪伤梦雅爱之瑰·墨艳黎")

        self.entryname = Entry(self.ui)
        self.entryname.pack(side = LEFT)
        self.entryname.place(x=300, y=60)

        age = StringVar()
        age.set("年龄：")
        self.agelabel = Label(self.ui, textvariable=age, width=80, height=2)
        self.agelabel.place(x=-50, y=100)
        ageinfo = CreateToolTip(self.agelabel,
                                "当前版本仅支持15到49岁哦\n"
                                "15-19岁：力量和体型合计减5点。教育减５点。决定幸运值时可以骰2次并取较好的一次（本软件会自动进行判定）。\n"
                                "20-39岁：对教育进行１次增强检定（本软件会自动进行判定）。\n"
                                "40-49岁：对教育进行２次增强检定。力量体质敏捷合计减5点。外貌减5点（本软件会自动进行判定）。\n")
        initialage = StringVar()
        initialage.set("0")
        check_is_number = self.ui.register(self.number_only)
        self.entryage = Entry(self.ui, textvariable = initialage, validate='all', validatecommand = (check_is_number,'%P'))
        self.entryage.place(x=300, y=110)


        strength = StringVar()
        strength.set("力量：")
        self.strengthlabel = Label(self.ui, textvariable=strength, width=80, height=2)
        self.strengthlabel.place(x=-50, y=150)
        strengthinfo = CreateToolTip(self.strengthlabel,
                                     "投掷三枚六面骰(.r3d6)，其结果乘五，数值范围15到90。\n"
                                     "力量是调查员肌肉能力的量化。力量越高，调查员就能举起更重的东西或更强有力的抓住物体。"
                                     "该属性会决定调查员在近战中造成的伤害。力量降低为０时，调查员就成为了一个无法离开床铺的病号。")
        initialstr = StringVar()
        initialstr.set("0")
        self.entrystrength = Entry(self.ui, textvariable = initialstr, validate='all', validatecommand = (check_is_number,'%P'))
        self.entrystrength.place(x=300, y=160)

        constitution = StringVar()
        constitution.set("体质：")
        self.constitutionlabel = Label(self.ui, textvariable=constitution, width=80, height=2)
        self.constitutionlabel.place(x=-50, y=200)
        constitutioninfo = CreateToolTip(self.constitutionlabel,
                                         "投掷三枚六面骰(.r3d6)，其结果乘五，数值范围15到90。\n"
                                         "体质意味着健康、生气和活力。毒药和疾病会与调查员的体质属性正面相斗。高体质的调"
                                         "查员会有更多的生命值——能承受更多伤害和攻击。严重的物理损伤或魔法攻击有可能降"
                                         "低该属性，而当体质降为０时，调查员就死咯。")
        initialcon = StringVar()
        initialcon.set("0")
        self.entryconstitution = Entry(self.ui, textvariable = initialcon, validate='all', validatecommand = (check_is_number,'%P'))
        self.entryconstitution.place(x=300, y=210)

        size = StringVar()
        size.set("体型：")
        self.sizelabel = Label(self.ui, textvariable=size, width=80, height=2)
        self.sizelabel.place(x=-50, y=250)
        sizeinfo = CreateToolTip(self.sizelabel,
                                 "投掷两枚六面骰后加六(.r2d6 + 6)，其结果乘五，数值范围40到90。\n"
                                 "体型值将身高和体重整合成了一个数字。伸长脖子越过矮墙观望，或者挤进狭窄的空间，或者判定"
                                 "谁的头在蹲下时也会高处草堆一个截时，就看体型了。体型可以帮助决定生命值和删改加值和体格。"
                                 "体型的减少通常意味着丢失肢体，当然这也意味着敏捷的减少。对于调查员来说，失去所有体型，"
                                 "应该意味着他消失了——只有上帝知道他在哪！")
        initialsiz = StringVar()
        initialsiz.set("0")
        self.entrysize = Entry(self.ui, validate='all', textvariable = initialsiz, validatecommand = (check_is_number,'%P'))
        self.entrysize.place(x=300, y=260)

        dexterity = StringVar()
        dexterity.set("敏捷：")
        self.dexteritylabel = Label(self.ui, textvariable=dexterity, width=80, height=2)
        self.dexteritylabel.place(x=-50, y=300)
        dexterityinfo = CreateToolTip(self.dexteritylabel,
                                      "投掷三枚六面骰(.r3d6)，其结果乘五，数值范围15到90。\n"
                                      "高敏捷的调查员更为迅捷灵敏，肉体更加柔韧。敏捷检定可以帮助你在坠落中抓住支撑，"
                                      "或高速穿越敌人，或做到一些纤细的行动。敏捷降为０的调查员神经将会絮乱，"
                                      "无法完成任何物理行动。在战斗中，高敏捷的角色会优先行动")
        initialdex = StringVar()
        initialdex.set("0")
        self.entrydexterity = Entry(self.ui, textvariable = initialdex, validate='all', validatecommand = (check_is_number,'%P'))
        self.entrydexterity.place(x=300, y=310)

        appearence = StringVar()
        appearence.set("外貌：")
        self.appearencelabel = Label(self.ui, textvariable=appearence, width=80, height=2)
        self.appearencelabel.place(x=-50, y=350)
        appearencelabel = CreateToolTip(self.appearencelabel,
                                        "投掷三枚六面骰(.r3d6)，其结果乘五，数值范围15到90。\n"
                                        "外貌统括了肉体吸引力和人格魅力。高外貌的人潇洒而惹人喜爱，但不一定会有一副好面孔。"
                                        "外貌降为０的人恐怖而丑陋，有着十足令人厌恶的举止，走到哪都会引发议论和震动。"
                                        "外貌会在社交遭遇中发生效用，或在试图给某人留下好印象时有所帮助（可能获得奖励骰)")
        initialapp = StringVar()
        initialapp.set("0")
        self.entryappearence = Entry(self.ui, textvariable = initialapp, validate='all', validatecommand = (check_is_number,'%P'))
        self.entryappearence.place(x=300, y=360)

        education = StringVar()
        education.set("教育：")
        self.educationlabel = Label(self.ui, textvariable=education, width=80, height=2)
        self.educationlabel.place(x=-50, y=400)
        educationinfo = CreateToolTip(self.educationlabel,
                                      "投掷两枚六面骰后加六(.r2d6 + 6)，其结果乘五，数值范围40到90。\n"
                                      "教育属性是调查员所真正掌握的正规知识的量化，它表明了调查员在全日制学习中花费了多"
                                      "长时间。教育表示的是调查员保持的信息数量（晶体智力），而非机智应变使用信息的能力（流体智力）。"
                                      "教育为０的角色估计是新生儿或者失忆过——没有关于世界的常识，就会显得十分好奇而容易受骗。")
        initialedu = StringVar()
        initialedu.set("0")
        self.entryeducation = Entry(self.ui, textvariable = initialedu, validate='all', validatecommand = (check_is_number,'%P'))
        self.entryeducation.place(x=300, y=410)

        intelligence = StringVar()
        intelligence.set("智力/灵感：")
        self.intelligencelabel = Label(self.ui, textvariable=intelligence, width=80, height=2)
        self.intelligencelabel.place(x=-50, y=450)
        intelligenceinfo = CreateToolTip(self.intelligencelabel,
                                       "投掷两枚六面骰后加六(.r2d6 + 6)，其结果乘五，数值范围40到90。\n"
                                       "智力表示为调查员学习力、理解力、信息分析力和解密能力的优劣度（流体智力）。智力降为０的调查员就会如同婴儿般是个留涎的傻瓜"
                                       "智力决定了调查员的兴趣技能点的数量，也同样影响着灵感检定和智力检定（看不懂没关系)")
        initialint = StringVar()
        initialint.set("0")
        self.entryintelligence = Entry(self.ui, textvariable = initialint, validate='all', validatecommand = (check_is_number,'%P'))
        self.entryintelligence.place(x=300, y=460)

        power = StringVar()
        power.set("意志：")
        self.powerlabel = Label(self.ui, textvariable=power, width=80, height=2)
        self.powerlabel.place(x=-50, y=500)
        powerinfo = CreateToolTip(self.powerlabel,
                                  "投掷三枚六面骰(.r3d6)，其结果乘五，数值范围15到90。\n"
                                  "意志正是心意的力量；意志越高，学习和抵抗魔法的资质就越高。意志降为０的调查员如同行尸走肉，"
                                  "没有了意念，当然也无法使用魔法。除非特有说明，否则游戏中意志的降低会是永久性的。"
                                  "理智点（ＳＡＮ）的游戏初始值等于角色的意志")
        initialpow = StringVar()
        initialpow.set("0")
        self.entrypower = Entry(self.ui, textvariable = initialpow, validate='all', validatecommand = (check_is_number,'%P'))
        self.entrypower.place(x=300, y=510)

        luck = StringVar()
        luck.set("幸运：")
        self.lucklabel = Label(self.ui, textvariable=luck, width=80, height=2)
        self.lucklabel.place(x=-50, y=550)
        luckinfo = CreateToolTip(self.lucklabel,
                                 "投掷三枚六面骰(.r3d6)，其结果乘五，数值范围15到90。\n"
                                 "幸运是判断一个角色受到幸运女神眷顾的程度，比如找东西，叫出租车，打电话等等，"
                                 "偶尔也可以用于在危急时刻对自身的保护，如一个幸运高的人可能在毫无察觉的情况下很巧的避开一块从天上掉下来的玻璃而不受伤。"
                                 "幸运甚至可以用于修改部分判定的结果，不过因此消耗的幸运值一般情况下是很难恢复的（看不懂没关系)")
        initialluck = StringVar()
        initialluck.set("0")
        self.entryluck = Entry(self.ui, textvariable = initialluck, validate='all', validatecommand = (check_is_number,'%P'))
        self.entryluck.place(x=300, y=560)

        summe = StringVar()
        summe.set("九大属性总和（带幸运）：")
        summmelabel = Label(self.ui, textvariable = summe, width = 80, height = 2)
        summmelabel.place(x=-50, y=600)
        entrysumme = Entry(self.ui, state='disabled')
        entrysumme.place(x=300, y =610)
        def random_attribute():
            stre = random.randint(1, 6) * 5 + random.randint(1, 6) * 5 + random.randint(1, 6) * 5
            con = random.randint(1, 6) * 5 + random.randint(1, 6) * 5 + random.randint(1, 6) * 5
            siz = (random.randint(1, 6) + random.randint(1, 6) + 6) * 5
            dex = random.randint(1, 6) * 5 + random.randint(1, 6) * 5 + random.randint(1, 6) * 5
            app = random.randint(1, 6) * 5 + random.randint(1, 6) * 5 + random.randint(1, 6) * 5
            int = (random.randint(1, 6) + random.randint(1, 6) + 6) * 5
            pow = random.randint(1, 6) * 5 + random.randint(1, 6) * 5 + random.randint(1, 6) * 5
            edu = (random.randint(1, 6) + random.randint(1, 6) + 6) * 5
            luck = random.randint(1, 6) * 5 + random.randint(1, 6) * 5 + random.randint(1, 6) * 5

            self.entrystrength.delete(0, END)
            self.entrystrength.insert(END, stre)
            self.entryconstitution.delete(0, END)
            self.entryconstitution.insert(END, con)
            self.entrysize.delete(0, END)
            self.entrysize.insert(END, siz)
            self.entrydexterity.delete(0, END)
            self.entrydexterity.insert(END, dex)
            self.entryappearence.delete(0, END)
            self.entryappearence.insert(END, app)
            self.entryeducation.delete(0, END)
            self.entryeducation.insert(END, edu)
            self.entryintelligence.delete(0, END)
            self.entryintelligence.insert(END, int)
            self.entrypower.delete(0, END)
            self.entrypower.insert(END, pow)
            self.entryluck.delete(0, END)
            self.entryluck.insert(END, luck)
            entrysumme.delete(0,END)
            he = stre + con + siz + dex + app + int + pow + edu + luck
            entrysumme.configure(state = 'normal')
            entrysumme.delete(0, END)
            entrysumme.insert(END,he)
            entrysumme.configure(state='disabled')

        def create_character():
            error_message, result = self.check_attributes()
            if(result == True):
                print("角色创建成功！")
                this_Player = player(self.entryname.get(), int(self.entryage.get()), int(self.entrystrength.get()),
                                     int(self.entryconstitution.get()), int(self.entrysize.get()), int(self.entrydexterity.get()),
                                     int(self.entryappearence.get()), int(self.entryeducation.get()), int(self.entryintelligence.get()),
                                     int(self.entrypower.get()), int(self.entryluck.get()))
                self.ui.destroy()
                skills = Skills(self.root, this_Player)

            else:
                print(error_message)

        def getsum():
            sum = int(self.entrystrength.get())  + int(self.entryconstitution.get()) + int(self.entrysize.get())+ int(self.entrydexterity.get())  + int(self.entryappearence.get()) + int(self.entryintelligence.get())+ int(self.entrypower.get()) + int(self.entryeducation.get()) + int(self.entryluck.get())
            entrysumme.configure(state = 'normal')
            entrysumme.delete(0, END)
            entrysumme.insert(END,sum)
            entrysumme.configure(state='disabled')

        wannarandom = Button(self.ui, text='懒？直接随机一下？', width=18, height=2, command=random_attribute)
        wannarandom.place(x=150, y=660)

        jiesuan = Button(self.ui, text='属性结算', width=10, height=2, command=getsum)
        jiesuan.place(x=320, y=660)

        createchara = Button(self.ui, text='数值确认无误，创建！', width=18, height=2, command=create_character)
        createchara.place(x=430, y=660)



    ##独立方法
    def number_only(self, content):
        if content.isdigit()or content == "":
            return True
        else:
            return False

    def check_attributes(self):
        error_message = ""
        result = False
        name = self.entryname.get()
        age = int(self.entryage.get())
        stre = int(self.entrystrength.get())
        con = int(self.entryconstitution.get())
        siz = int(self.entrysize.get())
        dex = int(self.entrydexterity.get())
        app = int(self.entryappearence.get())
        edu = int(self.entryeducation.get())
        inte = int(self.entryintelligence.get())
        pow = int(self.entrypower.get())
        luck = int(self.entryluck.get())
        if (name == ''):
            error_message = "名字呢？"
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "名字呢？鼠标悬停属性获得更多信息")
            return (error_message, result)
        if (age < 15 or age > 49):
            error_message = "请确认年龄范围"
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "请确认年龄范围，鼠标悬停属性获得更多信息")
            return (error_message, result)
        if (stre < 15 or stre > 90 or stre % 5 != 0):
            error_message = "请确认力量范围"
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "请确认力量数值（必须为五的倍数）以及范围，鼠标悬停属性获得更多信息")
            return (error_message, result)
        if (con < 15 or con > 90 or con % 5 != 0):
            error_message = "请确认体质范围"
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "请确认体质数值（必须为五的倍数）以及范围，鼠标悬停属性获得更多信息")
            return (error_message, result)
        if (siz < 40 or siz > 90 or siz % 5 != 0):
            error_message = "请确认体型范围"
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "请确认体型数值（必须为五的倍数）以及范围，鼠标悬停属性获得更多信息")
            return (error_message, result)
        if (dex < 15 or dex > 90 or dex % 5 != 0):
            error_message = "请确认敏捷范围"
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "请确认敏捷数值（必须为五的倍数）以及范围，鼠标悬停属性获得更多信息")
            return (error_message, result)
        if (app < 15 or app > 90):
            error_message = "请确认外貌范围"
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "请确认外貌数值（必须为五的倍数）以及范围，鼠标悬停属性获得更多信息")
            return (error_message, result)
        if (inte < 40 or inte > 90 or inte % 5 != 0):
            error_message = "请确认智力范围"
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "请确认智力数值（必须为五的倍数）以及范围，鼠标悬停属性获得更多信息")
            return (error_message, result)
        if (pow < 15 or pow> 90 or pow % 5 != 0):
            error_message = "请确认意志范围"
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "请确认意志数值（必须为五的倍数）以及范围，鼠标悬停属性获得更多信息")
            return (error_message, result)
        if (edu < 40 or edu> 90 or edu % 5 != 0):
            error_message = "请确认教育范围"
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "请确认教育数值（必须为五的倍数）以及范围，鼠标悬停属性获得更多信息")
            return (error_message, result)
        if (luck < 15 or luck> 90 or luck % 5 != 0):
            error_message = "请确认幸运范围"
            tkinter.messagebox.showinfo("我康你啊，还是不懂哦", "请确认幸运数值（必须为五的倍数）以及范围，鼠标悬停属性获得更多信息")
            return (error_message, result)
        result = True
        return (error_message, result)


