from tkinter import *
import tkinter.messagebox
from View.ToolTip import *
from Model.PC import *

class Skill1():
    def __init__(self, master, fr, player):
        self.root = master
        self.fr = fr
        self.ui = Frame(self.root, )
        # self.ui.pack(fill=BOTH, expand=True)

        self.player = player
        self.jinengdict = {}
        self.jinengdict[''] = ['']
        self.jinengdict["护士"] = ["急救","医学","心理学","聆听"]
        self.jinengdict["神秘学家"] = ["人类学","历史","图书馆","神秘学"]

        self.dianshudict = {}
        self.dianshudict[''] = 0
        self.dianshudict["护士"] = player.edu * 4
        self.dianshudict["神秘学家"] = player.edu * 4


        zhiyedes = StringVar()
        zhiyedes.set("职业：")
        zhiyedeslabel = Label(self.ui, textvariable=zhiyedes, width=5, height=2)
        zhiyedeslabel.place(x=20, y=0)

        self.zhiye = StringVar()
        self.zhiye.set(self.player.zhiye)
        zhiyelabel = Label(self.ui, textvariable=self.zhiye, width=7, height=2)
        zhiyelabel.place(x=50, y=0)

        jinengdes = StringVar()
        jinengdes.set("本职技能为：")
        jinengdeslabel = Label(self.ui, textvariable=jinengdes, width=10, height=2)
        jinengdeslabel.place(x=105, y=0)

        self.benzhijineng = StringVar()
        self.benzhijineng.set('')
        benzhijinenglabel = Label(self.ui, textvariable=self.benzhijineng, width=23, height=2)
        benzhijinenglabel.place(x=170, y=0)


        self.jinenghint = StringVar()
        self.jinenghint.set("")
        jinenghintlabel = Label(self.ui, textvariable=self.jinenghint, width=50, height=2)
        jinenghintlabel.place(x=370, y=0)


        self.notice = StringVar()
        self.notice.set("注意！本职技能上限为80，非本职技能上限为50，本职技能点仅可用于本职技能上，而兴趣技能点则可用于任意技能上（包括本职)")
        noticelabel = Label(self.ui, textvariable=self.notice, width=150, height=2)
        noticelabel.place(x=-160, y=30)

        jinengname = StringVar()
        jinengname.set("技能")
        jinengnamelabel = Label(self.ui, textvariable=jinengname, width=5, height=1)
        jinengnamelabel.place(x=14, y=70)

        base = StringVar()
        base.set("基础")
        baselabel = Label(self.ui, textvariable=base, width=5, height=1)
        baselabel.place(x=55, y=70)

        benzhi = StringVar()
        benzhi.set("本职技能点分配")
        benzhilabel = Label(self.ui, textvariable=benzhi, width=12, height=1)
        benzhilabel.place(x=95, y=70)

        xingqu = StringVar()
        xingqu.set("兴趣技能点分配")
        xingqulabel = Label(self.ui, textvariable=xingqu, width=12, height=1)
        xingqulabel.place(x=195, y=70)

        ##会计
        kuaiji = StringVar()
        kuaiji.set("会计:")
        kuaijilabel = Label(self.ui, textvariable=kuaiji, width=5, height=1)
        kuaijilabel.place(x=14, y=100)
        kuaijides = CreateToolTip(kuaijilabel,"使你理解会计工作的流程以及一个企业或者个人的金融职务。"
                                              "通过检查账簿，你可以发现做假账的员工，对资金的偷偷挪用，"
                                              "对行贿或者敲诈的款项支付，以及经济状况是否比表面陈述的更好或者更差。"
                                              "通过仔细检查旧账户，你可以了解过去的资金的得与失以及这些资金是付给了谁以及为了什么款项而支付。"
                                              "（特定场合才能用到吧）")

        kuaijibase = StringVar()
        kuaijibase.set(5)
        kuaijilabel = Label(self.ui, textvariable=kuaijibase, width=5, height=1)
        kuaijilabel.place(x=55, y=100)

        self.kuaijientry1 = Text(self.ui, width = 12, height = 1)
        self.kuaijientry1.place(x=97, y=103)
        self.kuaijientry1.insert(END,0)

        self.kuaijientry2 = Text(self.ui, width = 12, height = 1)
        self.kuaijientry2.place(x=197, y=103)
        self.kuaijientry2.insert(END, 0)

        ##人类学
        renleixue = StringVar()
        renleixue.set("人类学:")
        renleixuelabel = Label(self.ui, textvariable=renleixue, width=5, height=1)
        renleixuelabel.place(x=14, y=130)
        renleixuedes = CreateToolTip(renleixuelabel, "使使用者能够通过观察来辨认和理解一个人的生活方式。如果技能使用者持续观察一个其他的文化一段时间，或"
                                                     "者在有着关于某种已消失文化的正确资料环境下工作，那么他可以对文化方式以及道德习惯进行简单的预测"
                                                     "，即使证据可能并不完整。通过学习文化一个月或者更久，人类学家开始理解这种文化是如何运作的以及，"
                                                     "如果结合心理学，可以预测那些研究文化的行为和信仰。（注：不是用来判断这个NPC是不是人哦）")

        renleixuebase = StringVar()
        renleixuebase.set(1)
        renleixuelabel = Label(self.ui, textvariable=renleixuebase, width=5, height=1)
        renleixuelabel.place(x=55, y=130)

        self.renleixueentry1 = Text(self.ui, width = 12, height = 1)
        self.renleixueentry1.place(x=97, y=133)
        self.renleixueentry1.insert(END,0)

        self.renleixueentry2 = Text(self.ui, width = 12, height = 1)
        self.renleixueentry2.place(x=197, y=133)
        self.renleixueentry2.insert(END, 0)

        ##估价
        gujia = StringVar()
        gujia.set("估价:")
        gujialabel = Label(self.ui, textvariable=gujia, width=5, height=1)
        gujialabel.place(x=14, y=160)
        gujiades = CreateToolTip(gujialabel, "用来估计某种物品的价值，包括质量，使用的材料以及工艺。相关的，技能使用者"
                                             "可以准确地辨认出物品的年龄，评估它的历史关联性以及发现赝品。（用于对抗伪造或者判断"
                                             "一件物品是什么做的）")

        gujiabase = StringVar()
        gujiabase.set(5)
        gujialabel = Label(self.ui, textvariable=gujiabase, width=5, height=1)
        gujialabel.place(x=55, y=160)

        self.gujiaentry1 = Text(self.ui, width = 12, height = 1)
        self.gujiaentry1.place(x=97, y=163)
        self.gujiaentry1.insert(END,0)

        self.gujiaentry2 = Text(self.ui, width = 12, height = 1)
        self.gujiaentry2.place(x=197, y=163)
        self.gujiaentry2.insert(END, 0)

        ##考古学
        kaoguxue = StringVar()
        kaoguxue.set("考古学:")
        kaoguxuelabel = Label(self.ui, textvariable=kaoguxue, width=5, height=1)
        kaoguxuelabel.place(x=14, y=190)
        kaoguxuedes = CreateToolTip(kaoguxuelabel, "允许从过去的文化中鉴定一件古董的年代以及辨别它，以及可以用来发现赝品。"
                                                   "使获得建立以及开掘一个挖掘遗址的专业知识。通过对遗址的勘察，"
                                                   "使用者可以推断留下这遗址的生物的目的和生活方式。人类学可能对此会有所帮助。"
                                                   "考古学还有助于辨认已消失的人类语言的书面形式。（特定场合才可能用到吧）")

        kaoguxuebase = StringVar()
        kaoguxuebase.set(1)
        kaoguxuelabel = Label(self.ui, textvariable=kaoguxuebase, width=5, height=1)
        kaoguxuelabel.place(x=55, y=190)

        self.kaoguxueentry1 = Text(self.ui, width = 12, height = 1)
        self.kaoguxueentry1.place(x=97, y=193)
        self.kaoguxueentry1.insert(END,0)

        self.kaoguxueentry2 = Text(self.ui, width = 12, height = 1)
        self.kaoguxueentry2.place(x=197, y=193)
        self.kaoguxueentry2.insert(END, 0)

        ##魅惑
        meihuo = StringVar()
        meihuo.set("魅惑:")
        meihuolabel = Label(self.ui, textvariable=meihuo, width=5, height=1)
        meihuolabel.place(x=14, y=220)
        meihuodes = CreateToolTip(meihuolabel, "魅惑允许通过许多形式来使用，包括肉体魅力、诱惑、奉承或是单纯令人感到温暖的人格魅力。"
                                                   "魅惑可能可以被用于迫使某人进行特定的行动，但是不会是与个人日常举止完全相反的行为。"
                                                   "魅惑或是心理学技能可以用于对抗魅惑技能。魅惑技能可以被用于讨价还价来使一件物品或者服务的价格降低。"
                                                   "如果成功，使用者得到了卖家的赞同，并且他们可能乐意降低一点价格。(属于四大交涉技能，其他三个为：恐吓，话术和说服。"
                                                   "此技能与外貌挂钩，外貌高者有可能获得奖励骰，低者则相反)")

        meihuobase = StringVar()
        meihuobase.set(15)
        meihuolabel = Label(self.ui, textvariable=meihuobase, width=5, height=1)
        meihuolabel.place(x=55, y=220)

        self.meihuoentry1 = Text(self.ui, width = 12, height = 1)
        self.meihuoentry1.place(x=97, y=223)
        self.meihuoentry1.insert(END,0)

        self.meihuoentry2 = Text(self.ui, width = 12, height = 1)
        self.meihuoentry2.place(x=197, y=223)
        self.meihuoentry2.insert(END, 0)

        ##攀爬
        panpa = StringVar()
        panpa.set("攀爬:")
        panpalabel = Label(self.ui, textvariable=panpa, width=5, height=1)
        panpalabel.place(x=14, y=250)
        panpades = CreateToolTip(panpalabel, "这项技能允许一名角色借助或者不借助绳索或者登山工具进行爬树、墙以及其他垂直表面。"
                                             "这项技能也同样包括用绳索下降。攀爬表面是否坚固，是否有可以用手握住的地方，"
                                             "风力，可见度，雨等等坏境状况都可能会影响难度等级。（点了这个技能记得随身带个绳索什么的）")

        panpabase = StringVar()
        panpabase.set(20)
        panpalabel = Label(self.ui, textvariable=panpabase, width=5, height=1)
        panpalabel.place(x=55, y=250)

        self.panpaentry1 = Text(self.ui, width = 12, height = 1)
        self.panpaentry1.place(x=97, y=253)
        self.panpaentry1.insert(END,0)

        self.panpaentry2 = Text(self.ui, width = 12, height = 1)
        self.panpaentry2.place(x=197, y=253)
        self.panpaentry2.insert(END, 0)

        ##计算机使用
        jisuanji = StringVar()
        jisuanji.set("计算机:")
        jisuanjilabel = Label(self.ui, textvariable=jisuanji, width=5, height=1)
        jisuanjilabel.place(x=14, y=280)
        jisuanjides = CreateToolTip(jisuanjilabel, "这项技能允许调查员用各种不同的电脑语言进行编程；恢复或者分析隐藏的数据；"
                                                   "解除被加了保护的系统；探索一个复杂的网络；或者发现别人的骇入、后门程序、病毒。"
                                                   "对电脑系统的特殊操作可能会需要这个检定。（日常上网并不需要鉴定，定向（明确了搜什么）在网上搜集一"
                                                   "个信息可能要过图书馆鉴定而不是计算机使用）")

        jisuanjibase = StringVar()
        jisuanjibase.set(5)
        jisuanjilabel = Label(self.ui, textvariable=jisuanjibase, width=5, height=1)
        jisuanjilabel.place(x=55, y=280)

        self.jisuanjientry1 = Text(self.ui, width = 12, height = 1)
        self.jisuanjientry1.place(x=97, y=283)
        self.jisuanjientry1.insert(END,0)

        self.jisuanjientry2 = Text(self.ui, width = 12, height = 1)
        self.jisuanjientry2.place(x=197, y=283)
        self.jisuanjientry2.insert(END, 0)

        ##信用
        xinyong = StringVar()
        xinyong.set("信用:")
        xinyonglabel = Label(self.ui, textvariable=xinyong, width=5, height=1)
        xinyonglabel.place(x=14, y=310)
        xinyongdes = CreateToolTip(xinyonglabel, "衡量了调查员表现出来的富裕程度以及经济上的自信度。钱是敲门砖；"
                                                 "如果调查员尝试用他的经济地位来达成某个目标，那么也许使用信用评级技能会比较合适。"
                                                 "信用评级可以被用来取代APP来评估第一印象。信用评级并不是一个被用于评估经济富裕度的技能，"
                                                 "也不应该与其他技能挂钩。一个高信用评级在游戏中将会是一个有用的资源，并且应当在创造调查员时加上一定的点数。"
                                                 "每个职业有着起始的信用评级范围，并且应当花费技能点来达到这个评级范围内。（注:这个技能并不像看上去那么鸡肋，"
                                                 "高信用在团里有时候会有意想不到的好处)")

        xinyongbase = StringVar()
        xinyongbase.set(0)
        xinyonglabel = Label(self.ui, textvariable=xinyongbase, width=5, height=1)
        xinyonglabel.place(x=55, y=310)

        self.xinyongentry1 = Text(self.ui, width = 12, height = 1)
        self.xinyongentry1.place(x=97, y=313)
        self.xinyongentry1.insert(END,0)

        self.xinyongentry2 = Text(self.ui, width = 12, height = 1)
        self.xinyongentry2.place(x=197, y=313)
        self.xinyongentry2.insert(END, 0)


        ##乔庄
        qiaozhuang = StringVar()
        qiaozhuang.set("乔庄:")
        qiaozhuanglabel = Label(self.ui, textvariable=qiaozhuang, width=5, height=1)
        qiaozhuanglabel.place(x=14, y=340)
        qiaozhaungdes = CreateToolTip(qiaozhuanglabel, "使用在当你想要演出除你自己外的别人时。使用者改变了态度，习惯，"
                                                       "以及/或声音来进行一个乔装，以另一个人或者另一类人的形象出现。"
                                                       "戏剧化妆品可能会有所帮助，还有伪造的身份证。(点了这个技能千万记得"
                                                       "把要用来乔庄的东西放在自己随身物品里，否则你可能要过一系列的技能鉴定才能达到乔庄的目的)")

        qiaozhuangbase = StringVar()
        qiaozhuangbase.set(5)
        qiaozhuanglabel = Label(self.ui, textvariable=qiaozhuangbase, width=5, height=1)
        qiaozhuanglabel.place(x=55, y=340)

        self.qiaozhuangentry1 = Text(self.ui, width = 12, height = 1)
        self.qiaozhuangentry1.place(x=97, y=343)
        self.qiaozhuangentry1.insert(END,0)

        self.qiaozhuangentry2 = Text(self.ui, width = 12, height = 1)
        self.qiaozhuangentry2.place(x=197, y=343)
        self.qiaozhuangentry2.insert(END, 0)

        ##闪避
        shanbi = StringVar()
        shanbi.set("闪避:")
        shanbilabel = Label(self.ui, textvariable=shanbi, width=5, height=1)
        shanbilabel.place(x=14, y=370)
        shanbides = CreateToolTip(shanbilabel, "允许调查员本能地闪避攻击，投掷过来的投射物以及诸如此类的。一名角色可以尝试在一场战斗轮中使用任何次数的闪避。"
                                               "当然了再快也不可能躲过子弹，面对有枪械的敌人时应该选择寻找掩体（过幸运）或者缴械（足够近时过斗殴）而不是闪避")

        shanbibase = StringVar()
        shanbibase.set(player.shanbi)
        shanbilabel = Label(self.ui, textvariable=shanbibase, width=5, height=1)
        shanbilabel.place(x=55, y=370)

        self.shanbientry1 = Text(self.ui, width = 12, height = 1)
        self.shanbientry1.place(x=97, y=373)
        self.shanbientry1.insert(END,0)

        self.shanbientry2 = Text(self.ui, width = 12, height = 1)
        self.shanbientry2.place(x=197, y=373)
        self.shanbientry2.insert(END, 0)


        ##汽车驾驶
        qichejiashi = StringVar()
        qichejiashi.set("汽车驾驶:")
        qichejiashilabel = Label(self.ui, textvariable=qichejiashi, width=10, height=1)
        qichejiashilabel.place(x=-10, y=400)
        qichejiashides = CreateToolTip(qichejiashilabel, "任何有着这项技能的人都可以驾驶一辆汽车或者轻型卡车，进行常规的移动，"
                                                         "并且处理机动车的一般毛病(无需技能判定)。如果调查员想要甩掉一名追踪者或者追踪某人，则需要一个汽车驾驶检定。"
                                                         "(注：骑马等事物有骑术技能，而不是使用汽车驾驶）")

        qichejiashibase = StringVar()
        qichejiashibase.set(20)
        qichejiashilabel = Label(self.ui, textvariable=qichejiashibase, width=5, height=1)
        qichejiashilabel.place(x=55, y=400)

        self.qichejiashientry1 = Text(self.ui, width = 12, height = 1)
        self.qichejiashientry1.place(x=97, y=403)
        self.qichejiashientry1.insert(END,0)

        self.qichejiashientry2 = Text(self.ui, width = 12, height = 1)
        self.qichejiashientry2.place(x=197, y=403)
        self.qichejiashientry2.insert(END, 0)


        ##电器维修
        dianqiweixiu = StringVar()
        dianqiweixiu.set("电器维修:")
        dianqiweixiulabel = Label(self.ui, textvariable=dianqiweixiu, width=10, height=1)
        dianqiweixiulabel.place(x=-10, y=430)
        dianqiweixiudes = CreateToolTip(dianqiweixiulabel, "使调查员能够修理或者改装电气设备，例如自动点火装置，电动机，"
                                                           "保险丝盒，以及防盗自动警铃。在现代，这项技能对现代电子器件几乎做不到什么。"
                                                           "为了维修电气设备，可能需要特殊的部件或者工具。在1920年代的职业可能会需要这个技能，并且需要机"
                                                           "械维修技能作为组合。电气维修也可能在现代的爆破上被使用，例如雷管，"
                                                           "C-4塑料炸弹，以及地雷。这些武器被设计得简单易用；只有一个大失败的结果才会造成不启动。"
                                                           "但拆除爆炸物是远远更为复杂的，因为它们可能被安装了反拆改装置；当用于解除爆炸物时应当提高难度等级")


        dianqiweixiubase = StringVar()
        dianqiweixiubase.set(10)
        dianqiweixiulabel = Label(self.ui, textvariable=dianqiweixiubase, width=5, height=1)
        dianqiweixiulabel.place(x=55, y=430)

        self.dianqiweixiuentry1 = Text(self.ui, width = 12, height = 1)
        self.dianqiweixiuentry1.place(x=97, y=433)
        self.dianqiweixiuentry1.insert(END,0)

        self.dianqiweixiuentry2 = Text(self.ui, width = 12, height = 1)
        self.dianqiweixiuentry2.place(x=197, y=433)
        self.dianqiweixiuentry2.insert(END, 0)


        ##电子学
        dianzixue = StringVar()
        dianzixue.set("电子学:")
        dianzixuelabel = Label(self.ui, textvariable=dianzixue, width=10, height=1)
        dianzixuelabel.place(x=-10, y=460)
        dianzixuedes = CreateToolTip(dianzixuelabel, "用来发现并对电子设备的故障进行维修。允许制作简单的电子设备。这是个现代"
                                                     "技能—在1920年代则是使用物理学以及电气维修来应对电子设备。不像电气维修技能，电子学工作的部件通常是不能临时配备的："
                                                     "它们通过精密的工作被设计出来。通常如果没有正确的微晶片或者电路板，技能的使用者就无法进行工作，"
                                                     "除非他们可以策划出一些形式的应急方案。（所以老规矩，随身写清楚带什么设备吧）")

        dianzixuebase = StringVar()
        dianzixuebase.set(1)
        dianzixuelabel = Label(self.ui, textvariable=dianzixuebase, width=5, height=1)
        dianzixuelabel.place(x=55, y=460)

        self.dianzixueentry1 = Text(self.ui, width = 12, height = 1)
        self.dianzixueentry1.place(x=97, y=463)
        self.dianzixueentry1.insert(END,0)

        self.dianzixueentry2 = Text(self.ui, width = 12, height = 1)
        self.dianzixueentry2.place(x=197, y=463)
        self.dianzixueentry2.insert(END, 0)


        ##话术
        huashu = StringVar()
        huashu.set("话术:")
        huashulabel = Label(self.ui, textvariable=huashu, width=10, height=1)
        huashulabel.place(x=-10, y=490)
        huashudes = CreateToolTip(huashulabel, "四大交涉技能之一，其余三个为：魅惑，恐吓和说服。"
                                               "话术特别限定于言语上的哄骗，欺骗以及误导，例如迷惑一名门卫来让你进入一间俱乐部，"
                                               "让某人在一张他还没有读的文件上签字，误导警察看向另一边，以及诸如此类的。"
                                               "这项技能的对立技能为心理学或者话术。话术的效果总是暂时性的，和魅惑一样，也可以用来砍价。"
                                               "（注：不推荐新人点话术，新人更容易roleplay的像恐吓或者说服，如果连roleplay都省了直接说"
                                               "我要用话术搞定这个NPC，那请右上角）")

        huashubase = StringVar()
        huashubase.set(5)
        huashulabel = Label(self.ui, textvariable=huashubase, width=5, height=1)
        huashulabel.place(x=55, y=490)

        self.huashuentry1 = Text(self.ui, width = 12, height = 1)
        self.huashuentry1.place(x=97, y=493)
        self.huashuentry1.insert(END,0)

        self.huashuentry2 = Text(self.ui, width = 12, height = 1)
        self.huashuentry2.place(x=197, y=493)
        self.huashuentry2.insert(END, 0)

        ##斗殴
        douou = StringVar()
        douou.set("斗殴:")
        dououlabel = Label(self.ui, textvariable=douou, width=10, height=1)
        dououlabel.place(x=-10, y=520)
        dououdes = CreateToolTip(dououlabel, "斗殴属于格斗技能之一，包括空手格斗以及任何人都可以捡起并使用的基础武器，"
                                             "例如棍棒，小刀，以及许多临时武器，例如瓶子以及椅子腿。本版本简化格斗技能仅保留斗殴这一项"
                                             "，之后版本可能会添加别的吧（咕咕咕）。（注：被攻击（不包括枪械）时也可使用斗殴判定进行反击）")

        dououbase = StringVar()
        dououbase.set(25)
        dououlabel = Label(self.ui, textvariable=dououbase, width=5, height=1)
        dououlabel.place(x=55, y=520)

        self.dououentry1 = Text(self.ui, width = 12, height = 1)
        self.dououentry1.place(x=97, y=523)
        self.dououentry1.insert(END,0)

        self.dououentry2 = Text(self.ui, width = 12, height = 1)
        self.dououentry2.place(x=197, y=523)
        self.dououentry2.insert(END, 0)

        ##手枪
        shouqiang = StringVar()
        shouqiang.set("手枪:")
        shouqianglabel = Label(self.ui, textvariable=shouqiang, width=10, height=1)
        shouqianglabel.place(x=-10, y=550)
        shouqiangdes = CreateToolTip(shouqianglabel, "用来使用所有的类似于手枪的火器，进行非连续的射击。对于现代游戏中的全自动手枪（MAC-11，乌兹手枪，等等），"
                                                     "当使用连射时，用冲锋枪的技能进行判定。（这个版本没有做）上了膛的枪械会让你在战斗中更有优势（首轮战斗轮敏捷+50）")

        shouqiangbase = StringVar()
        shouqiangbase.set(20)
        shouqianglabel = Label(self.ui, textvariable=shouqiangbase, width=5, height=1)
        shouqianglabel.place(x=55, y=550)

        self.shouqiangentry1 = Text(self.ui, width = 12, height = 1)
        self.shouqiangentry1.place(x=97, y=553)
        self.shouqiangentry1.insert(END,0)

        self.shouqiangentry2 = Text(self.ui, width = 12, height = 1)
        self.shouqiangentry2.place(x=197, y=553)
        self.shouqiangentry2.insert(END, 0)

        ##急救
        jijiu = StringVar()
        jijiu.set("急救:")
        jijiulabel = Label(self.ui, textvariable=jijiu, width=10, height=1)
        jijiulabel.place(x=-10, y=580)
        jijiudes = CreateToolTip(jijiulabel, "使用者有能力可以提供紧急的医疗处理。这可能包括：对摔断了的腿用夹板进行处理，"
                                             "止血，处理烧伤，对一名溺水的受害者进行复苏处理，包扎以及清理伤口等等。"
                                             "急救不能用于治疗疾病（这需要医学技能），当然啦，也需要有趁手的急救材料。")

        jijiubase = StringVar()
        jijiubase.set(30)
        jijiulabel = Label(self.ui, textvariable=jijiubase, width=5, height=1)
        jijiulabel.place(x=55, y=580)

        self.jijiuentry1 = Text(self.ui, width = 12, height = 1)
        self.jijiuentry1.place(x=97, y=583)
        self.jijiuentry1.insert(END,0)

        self.jijiuentry2 = Text(self.ui, width = 12, height = 1)
        self.jijiuentry2.place(x=197, y=583)
        self.jijiuentry2.insert(END, 0)

        ##历史
        lishi = StringVar()
        lishi.set("历史:")
        lishilabel = Label(self.ui, textvariable=lishi, width=10, height=1)
        lishilabel.place(x=-10, y=610)
        lishides = CreateToolTip(lishilabel, "让一名调查员能够记住一个国家，城市，区域或者个人及其相关的重要情报。"
                                             "一个成功的检定可以用来帮助辨认先祖所熟悉的工具，科技，或者想法，"
                                             "但是对当下的所知甚少。（所以如果不从事相关行业的话，为什么不点图书馆而点这个？？）")

        lishibase = StringVar()
        lishibase.set(5)
        lishilabel = Label(self.ui, textvariable=lishibase, width=5, height=1)
        lishilabel.place(x=55, y=610)

        self.lishientry1 = Text(self.ui, width = 12, height = 1)
        self.lishientry1.place(x=97, y=613)
        self.lishientry1.insert(END,0)

        self.lishientry2 = Text(self.ui, width = 12, height = 1)
        self.lishientry2.place(x=197, y=613)
        self.lishientry2.insert(END, 0)

        ##游泳
        youyong = StringVar()
        youyong.set("游泳:")
        youyonglabel = Label(self.ui, textvariable=youyong, width=10, height=1)
        youyonglabel.place(x=-10, y=640)
        youyongdes = CreateToolTip(youyonglabel, "有能力在水或者其他液体中漂浮以及移动。只有在遭遇危险的时候需要进行游泳技能检定（不是很长的河或者急流或者有怪则不需要判定）")

        youyongbase = StringVar()
        youyongbase.set(20)
        youyonglabel = Label(self.ui, textvariable=youyongbase, width=5, height=1)
        youyonglabel.place(x=55, y=640)

        self.youyongentry1 = Text(self.ui, width = 12, height = 1)
        self.youyongentry1.place(x=97, y=643)
        self.youyongentry1.insert(END,0)

        self.youyongentry2 = Text(self.ui, width = 12, height = 1)
        self.youyongentry2.place(x=197, y=643)
        self.youyongentry2.insert(END, 0)


        ##投掷
        touzhi = StringVar()
        touzhi.set("投掷:")
        touzhilabel = Label(self.ui, textvariable=touzhi, width=10, height=1)
        touzhilabel.place(x=-10, y=670)
        touzhides = CreateToolTip(touzhilabel, "当需要用物体击中目标或者用物件的正确部分击中目标（例如小刀或者短柄小斧的刃）时，使用投掷技能。一件有着合理平衡构架的可以藏于手中大小的物"
                                               "品可以被投掷至多等同于STR码距离。")

        touzhibase = StringVar()
        touzhibase.set(20)
        touzhilabel = Label(self.ui, textvariable=touzhibase, width=5, height=1)
        touzhilabel.place(x=55, y=670)

        self.touzhientry1 = Text(self.ui, width = 12, height = 1)
        self.touzhientry1.place(x=97, y=673)
        self.touzhientry1.insert(END,0)

        self.touzhientry2 = Text(self.ui, width = 12, height = 1)
        self.touzhientry2.place(x=197, y=673)
        self.touzhientry2.insert(END, 0)



#####################################第二列



        jinengname2 = StringVar()
        jinengname2.set("技能")
        jinengname2label = Label(self.ui, textvariable=jinengname, width=5, height=1)
        jinengname2label.place(x=414, y=70)

        base2 = StringVar()
        base2.set("基础")
        base2label = Label(self.ui, textvariable=base2, width=5, height=1)
        base2label.place(x=455, y=70)

        benzhi2 = StringVar()
        benzhi2.set("本职技能点分配")
        benzhi2label = Label(self.ui, textvariable=benzhi2, width=12, height=1)
        benzhi2label.place(x=495, y=70)

        xingqu2 = StringVar()
        xingqu2.set("兴趣技能点分配")
        xingqu2label = Label(self.ui, textvariable=xingqu, width=12, height=1)
        xingqu2label.place(x=595, y=70)

        ##恐吓
        konghe = StringVar()
        konghe.set("恐吓:")
        konghelabel = Label(self.ui, textvariable=konghe, width=5, height=1)
        konghelabel.place(x=414, y=100)
        konghedes = CreateToolTip(konghelabel, "四大交涉技能之一，其他三个为：魅惑，话术和说服。恐吓可以以许多形式使用，包括武力威慑，心理操控，以及威胁。这通常被用来使某人害怕，"
                                               "并迫使其进行某种特定的行为。恐吓的对抗技能为恐吓或者心理学。携带武器或者其他的有力的威胁或诱因（长得奇丑无比）来协助恐吓可能可以降低难度等级。")

        konghebase = StringVar()
        konghebase.set(15)
        konghelabel = Label(self.ui, textvariable=konghebase, width=5, height=1)
        konghelabel.place(x=455, y=100)

        self.kongheentry1 = Text(self.ui, width = 12, height = 1)
        self.kongheentry1.place(x=497, y=103)
        self.kongheentry1.insert(END,0)

        self.kongheentry2 = Text(self.ui, width = 12, height = 1)
        self.kongheentry2.place(x=597, y=103)
        self.kongheentry2.insert(END, 0)

        ##跳跃
        tiaoyue = StringVar()
        tiaoyue.set("跳跃:")
        tiaoyuelabel = Label(self.ui, textvariable=tiaoyue, width=5, height=1)
        tiaoyuelabel.place(x=414, y=130)
        tiaoyuedes = CreateToolTip(tiaoyuelabel, "如果成功，调查员可以在垂直方向上跳起或跳下，或者从一个站立点或起步点水平向外跳。"
                                                 "当坠落时，跳跃可以被用来降低可能造成的坠落伤害（一般距离超过自身身高就需要进行跳跃判定了）")

        tiaoyuebase = StringVar()
        tiaoyuebase.set(20)
        tiaoyuelabel = Label(self.ui, textvariable=tiaoyuebase, width=5, height=1)
        tiaoyuelabel.place(x=455, y=130)

        self.tiaoyueentry1 = Text(self.ui, width = 12, height = 1)
        self.tiaoyueentry1.place(x=497, y=133)
        self.tiaoyueentry1.insert(END,0)

        self.tiaoyueentry2 = Text(self.ui, width = 12, height = 1)
        self.tiaoyueentry2.place(x=597, y=133)
        self.tiaoyueentry2.insert(END, 0)


        ##法律
        falv = StringVar()
        falv.set("法律:")
        falvlabel = Label(self.ui, textvariable=falv, width=5, height=1)
        falvlabel.place(x=414, y=160)
        falvdes = CreateToolTip(falvlabel, "代表你对相关法律、早期事件、法庭辩术或者法院程序了解的可能性。（特定情况下使用）")

        falvbase = StringVar()
        falvbase.set(5)
        falvlabel = Label(self.ui, textvariable=falvbase, width=5, height=1)
        falvlabel.place(x=455, y=160)

        self.falventry1 = Text(self.ui, width = 12, height = 1)
        self.falventry1.place(x=497, y=163)
        self.falventry1.insert(END,0)

        self.falventry2 = Text(self.ui, width = 12, height = 1)
        self.falventry2.place(x=597, y=163)
        self.falventry2.insert(END, 0)


        ##图书馆
        tushuguan = StringVar()
        tushuguan.set("图书馆:")
        tushuguanlabel = Label(self.ui, textvariable=tushuguan, width=5, height=1)
        tushuguanlabel.place(x=414, y=190)
        tushuguandes = CreateToolTip(tushuguanlabel, "御三家技能之一。图书馆使用使一名调查员能在图书馆找到一些信息，例如特定的一本书，新闻或者参考书，"
                                                     "搜集文件或者资料库，假设需要的东西确实在那里的话。使用这个技能需要数小时的连续的调查。（缺点是耗时，优点是"
                                                     "KP可以给你塞信息）。从一堆凌乱的文件中找到自己想要的或者从报纸中发现不寻常的线索等这样的情况过的都是图书馆，甚至可能是组合判定。")

        tushuguanbase = StringVar()
        tushuguanbase.set(20)
        tushuguanlabel = Label(self.ui, textvariable=tushuguanbase, width=5, height=1)
        tushuguanlabel.place(x=455, y=190)

        self.tushuguanentry1 = Text(self.ui, width = 12, height = 1)
        self.tushuguanentry1.place(x=497, y=193)
        self.tushuguanentry1.insert(END,0)

        self.tushuguanentry2 = Text(self.ui, width = 12, height = 1)
        self.tushuguanentry2.place(x=597, y=193)
        self.tushuguanentry2.insert(END, 0)


        ##聆听
        lingting = StringVar()
        lingting.set("聆听:")
        lingtinglabel = Label(self.ui, textvariable=lingting, width=5, height=1)
        lingtinglabel.place(x=414, y=220)
        lingtingdes = CreateToolTip(lingtinglabel, "御三家技能之一。衡量一名调查员理解声音的能力，包括偶然听到的对话，一扇关着的门后的轻声嘀咕，以及咖啡厅里的私语。其对抗技能为潜行。")

        lingtingbase = StringVar()
        lingtingbase.set(20)
        lingtinglabel = Label(self.ui, textvariable=lingtingbase, width=5, height=1)
        lingtinglabel.place(x=455, y=220)

        self.lingtingentry1 = Text(self.ui, width = 12, height = 1)
        self.lingtingentry1.place(x=497, y=223)
        self.lingtingentry1.insert(END,0)

        self.lingtingentry2 = Text(self.ui, width = 12, height = 1)
        self.lingtingentry2.place(x=597, y=223)
        self.lingtingentry2.insert(END, 0)


        ##锁匠
        suojiang = StringVar()
        suojiang.set("锁匠:")
        suojianglabel = Label(self.ui, textvariable=suojiang, width=5, height=1)
        suojianglabel.place(x=414, y=250)
        suojiangdes = CreateToolTip(suojianglabel, "锁匠技能可以打开车门，热线自动装置，用铁撬撬开图书馆的窗子，解决中国机关箱，"
                                                   "以及穿过常规的商用警报系统。使用者可能会修复锁，制作钥匙，或者在万能钥匙，"
                                                   "开锁工具或者其他工具的帮助下打开锁。特别困难的锁可能会需要一个更高的难度等级。（看似废技"
                                                   "实则神技，今天有人点开所了吗？没人的话我过一会再来问问）")

        suojiangbase = StringVar()
        suojiangbase.set(1)
        suojianglabel = Label(self.ui, textvariable=suojiangbase, width=5, height=1)
        suojianglabel.place(x=455, y=250)

        self.suojiangentry1 = Text(self.ui, width = 12, height = 1)
        self.suojiangentry1.place(x=497, y=253)
        self.suojiangentry1.insert(END,0)

        self.suojiangentry2 = Text(self.ui, width = 12, height = 1)
        self.suojiangentry2.place(x=597, y=253)
        self.suojiangentry2.insert(END, 0)

        ##机械维修
        jixieweixiu = StringVar()
        jixieweixiu.set("机械维修:")
        jixieweixiulabel = Label(self.ui, textvariable=jixieweixiu, width=12, height=1)
        jixieweixiulabel.place(x=380, y=280)
        jixieweixiudes = CreateToolTip(jixieweixiulabel, "这项技能允许调查员修理一个破损的机器或者制造一个新的。基础的木工手艺和管道项目也可以执行，制作物品也同样可以（例如一组滑轮系统）以及维修物品（例如蒸汽泵）。"
                                                         "在使用技能中可能会需要特殊的工具或者部件。这项技能可以用来打开普通的家庭锁，"
                                                         "但是更加专业的就不能了—见锁匠技能来打开更加复杂的锁。机械维修是一个与电气维修相伴随的技能，"
                                                         "并且两者都可能需要来为了修理一个复杂的设备，例如汽车或者飞行器。")

        jixieweixiubase = StringVar()
        jixieweixiubase.set(10)
        jixieweixiulabel = Label(self.ui, textvariable=jixieweixiubase, width=5, height=1)
        jixieweixiulabel.place(x=455, y=280)

        self.jixieweixiuentry1 = Text(self.ui, width=12, height=1)
        self.jixieweixiuentry1.place(x=497, y=283)
        self.jixieweixiuentry1.insert(END, 0)

        self.jixieweixiuentry2 = Text(self.ui, width=12, height=1)
        self.jixieweixiuentry2.place(x=597, y=283)
        self.jixieweixiuentry2.insert(END, 0)

        ##医学
        yixue = StringVar()
        yixue.set("医学:")
        yixuelabel = Label(self.ui, textvariable=yixue, width=5, height=1)
        yixuelabel.place(x=414, y=310)
        yixuedes = CreateToolTip(yixuelabel, "使用者可以诊断并治疗事故，创伤，疾病，毒药等，并且可以提供公共健康建议。"
                                             "如果一个时代还并没有好的治疗某种疾病的疗法，那么这项技能的效果是有限的，不确定的，或者无效的。"
                                             "医学技能能给予大范围的对于药片以及药剂，是自然还是人造的知识，以及对副作用以及禁忌症状的理解。用医学技能来进行治疗最少要花费1小时时间，"
                                             "并且可以在造成了伤害后的任何时间进行处理。（回复1d3的血，但是一定要有设备和场地！！）")

        yixuebase = StringVar()
        yixuebase.set(1)
        yixuelabel = Label(self.ui, textvariable=yixuebase, width=5, height=1)
        yixuelabel.place(x=455, y=310)

        self.yixueentry1 = Text(self.ui, width = 12, height = 1)
        self.yixueentry1.place(x=497, y=313)
        self.yixueentry1.insert(END,0)

        self.yixueentry2 = Text(self.ui, width = 12, height = 1)
        self.yixueentry2.place(x=597, y=313)
        self.yixueentry2.insert(END, 0)

        ##博物学
        bowuxue = StringVar()
        bowuxue.set("博物学:")
        bowuxuelabel = Label(self.ui, textvariable=bowuxue, width=5, height=1)
        bowuxuelabel.place(x=414, y=340)
        bowuxuedes = CreateToolTip(bowuxuelabel, "博物学达标了传统的（非科学的）知识以及农民，渔民，优秀的业余者，"
                                                 "以及单纯的爱好者的个人观察。它可以一般地对物种，栖息地进行辨认，并且可以辨认踪迹、"
                                                 "足迹以及叫声，也可以允许对什么事物可能对某种特定物种来说很重要进行猜测。"
                                                 "如果要一个对自然世界的科学性的理解，那么应当去看生物学，植物学以及动物学技能。（该版本没有，在做了）")

        bowuxuebase = StringVar()
        bowuxuebase.set(10)
        bowuxuelabel = Label(self.ui, textvariable=bowuxuebase, width=5, height=1)
        bowuxuelabel.place(x=455, y=340)

        self.bowuxueentry1 = Text(self.ui, width = 12, height = 1)
        self.bowuxueentry1.place(x=497, y=343)
        self.bowuxueentry1.insert(END,0)

        self.bowuxueentry2 = Text(self.ui, width = 12, height = 1)
        self.bowuxueentry2.place(x=597, y=343)
        self.bowuxueentry2.insert(END, 0)

        ##领航
        linghang = StringVar()
        linghang.set("领航:")
        linghanglabel = Label(self.ui, textvariable=linghang, width=5, height=1)
        linghanglabel.place(x=414, y=370)
        linghangdes = CreateToolTip(linghanglabel, "允许使用者在早上或者晚上，在暴风雨或者晴朗天气中认清自己的路。"
                                                   "有着更高技能的人将对天文表图和工具，以及卫星定位装置十分熟悉，"
                                                   "如果他们是在有着那些东西的时代的话。一名角色也可以用这项技能来测量以及对一块区域进行绘图（制图学），"
                                                   "判断是有着几平方米的小岛或者是一块内陆区域—使用现代工具可以降低甚至取消难度等级。")

        linghangbase = StringVar()
        linghangbase.set(10)
        linghanglabel = Label(self.ui, textvariable=linghangbase, width=5, height=1)
        linghanglabel.place(x=455, y=370)

        self.linghangentry1 = Text(self.ui, width = 12, height = 1)
        self.linghangentry1.place(x=497, y=373)
        self.linghangentry1.insert(END,0)

        self.linghangentry2 = Text(self.ui, width = 12, height = 1)
        self.linghangentry2.place(x=597, y=373)
        self.linghangentry2.insert(END, 0)


        ##神秘学
        shengmixue = StringVar()
        shengmixue.set("神秘学:")
        shengmixuelabel = Label(self.ui, textvariable=shengmixue, width=5, height=1)
        shengmixuelabel.place(x=414, y=400)
        shengmixuedes = CreateToolTip(shengmixuelabel, "使用者可以识别出神秘学道具，用语和概念，以及民间传统，并且可以辨认魔法书以及神秘学记号。"
                                                       "神秘学家对有着代代相传的神秘知识的家庭十分熟悉。（除非接连大失败，否则不存在神秘学高san值掉的快这种说法，就好比外科医生还能给血吓晕了？）")

        shengmixuebase = StringVar()
        shengmixuebase.set(5)
        shengmixuelabel = Label(self.ui, textvariable=shengmixuebase, width=5, height=1)
        shengmixuelabel.place(x=455, y=400)

        self.shengmixueentry1 = Text(self.ui, width = 12, height = 1)
        self.shengmixueentry1.place(x=497, y=403)
        self.shengmixueentry1.insert(END,0)

        self.shengmixueentry2 = Text(self.ui, width = 12, height = 1)
        self.shengmixueentry2.place(x=597, y=403)
        self.shengmixueentry2.insert(END, 0)

        ##重型机械
        zhongxingjixie = StringVar()
        zhongxingjixie.set("重型机械:")
        zhongxingjixielabel = Label(self.ui, textvariable=zhongxingjixie, width=12, height=1)
        zhongxingjixielabel.place(x=384, y=430)
        zhongxingjixiedes = CreateToolTip(zhongxingjixielabel, "当驾驶以及操纵一辆坦克，反铲挖土机，蒸汽挖土机或者其他巨型建造机械时需要这个技能。（很少用）")

        zhongxingjixiebase = StringVar()
        zhongxingjixiebase.set(1)
        zhongxingjixielabel = Label(self.ui, textvariable=zhongxingjixiebase, width=5, height=1)
        zhongxingjixielabel.place(x=455, y=430)

        self.zhongxingjixieentry1 = Text(self.ui, width = 12, height = 1)
        self.zhongxingjixieentry1.place(x=497, y=433)
        self.zhongxingjixieentry1.insert(END,0)

        self.zhongxingjixieentry2 = Text(self.ui, width = 12, height = 1)
        self.zhongxingjixieentry2.place(x=597, y=433)
        self.zhongxingjixieentry2.insert(END, 0)

        ##说服
        shuofu = StringVar()
        shuofu.set("说服:")
        shuofulabel = Label(self.ui, textvariable=shuofu, width=12, height=1)
        shuofulabel.place(x=384, y=460)
        shuofudes = CreateToolTip(shuofulabel, "四大交涉技能之一。使用说服来通过一场有理有据的论述、争辩以及讨论让目标相信一个确切的想法，"
                                                               "概念，或者信仰。说服并不一定需要涉及真实的内容。成功的说服技能的运用将花费不少的时间："
                                                               "至少半小时。如果你想快速地说（欺）服（骗）某人，你应该使用话术技能。")

        shuofubase = StringVar()
        shuofubase.set(10)
        shuofulabel = Label(self.ui, textvariable=shuofubase, width=5, height=1)
        shuofulabel.place(x=455, y=460)

        self.shuofuentry1 = Text(self.ui, width = 12, height = 1)
        self.shuofuentry1.place(x=497, y=463)
        self.shuofuentry1.insert(END,0)

        self.shuofuentry2 = Text(self.ui, width = 12, height = 1)
        self.shuofuentry2.place(x=597, y=463)
        self.shuofuentry2.insert(END, 0)


        ##精神分析
        jingshengfengxi = StringVar()
        jingshengfengxi.set("精神分析:")
        jingshengfengxilabel = Label(self.ui, textvariable=jingshengfengxi, width=12, height=1)
        jingshengfengxilabel.place(x=384, y=490)
        jingshengfengxides = CreateToolTip(jingshengfengxilabel, "当一个调查员或者NPC陷入疯狂时可以使用，一个成功的精神分析可以使其暂时摆脱疯狂状态。")

        jingshengfengxibase = StringVar()
        jingshengfengxibase.set(1)
        jingshengfengxilabel = Label(self.ui, textvariable=jingshengfengxibase, width=5, height=1)
        jingshengfengxilabel.place(x=455, y=490)

        self.jingshengfengxientry1 = Text(self.ui, width = 12, height = 1)
        self.jingshengfengxientry1.place(x=497, y=493)
        self.jingshengfengxientry1.insert(END,0)

        self.jingshengfengxientry2 = Text(self.ui, width = 12, height = 1)
        self.jingshengfengxientry2.place(x=597, y=493)
        self.jingshengfengxientry2.insert(END, 0)


        ##心理学
        xinglixue = StringVar()
        xinglixue.set("心理学:")
        xinglixuelabel = Label(self.ui, textvariable=xinglixue, width=12, height=1)
        xinglixuelabel.place(x=384, y=520)
        xinglixuedes = CreateToolTip(xinglixuelabel, "对所有人来说都很通用的洞察技能，允许使用者研究个人并且形成对于其他某人动机和人格的了解。其对抗技能为社交技能。（注："
                                                     "心理学不等于读心术！心理学需要暗骰！除非大成功，否则KP给与一个模棱两可的答复是理所当然的！）")

        xinglixuebase = StringVar()
        xinglixuebase.set(10)
        xinglixuelabel = Label(self.ui, textvariable=xinglixuebase, width=5, height=1)
        xinglixuelabel.place(x=455, y=520)

        self.xinglixueentry1 = Text(self.ui, width = 12, height = 1)
        self.xinglixueentry1.place(x=497, y=523)
        self.xinglixueentry1.insert(END,0)

        self.xinglixueentry2 = Text(self.ui, width = 12, height = 1)
        self.xinglixueentry2.place(x=597, y=523)
        self.xinglixueentry2.insert(END, 0)

        ##骑术
        qishu = StringVar()
        qishu.set("骑术:")
        qishulabel = Label(self.ui, textvariable=qishu, width=12, height=1)
        qishulabel.place(x=384, y=550)
        qishudes = CreateToolTip(qishulabel, "这项技能被用于给坐在鞍上驾驭马，驴子或者骡子，以及获得对这些骑乘动物、骑乘工具的基础照料知识，"
                                             "以及如何在疾驰中或困难地形上操纵坐骑。当坐骑出乎意外地抬起身子或失足时，骑手保持自己在坐骑上不摔落的几率等同于他的骑术技能。"
                                             "偏坐在马鞍上进行骑乘将会提高一个等级的难度等级。对于不熟悉的坐骑（例如骆驼）也可以成功地骑乘，但是可能会需要更高的难度等级。")

        qishubase = StringVar()
        qishubase.set(5)
        qishulabel = Label(self.ui, textvariable=qishubase, width=5, height=1)
        qishulabel.place(x=455, y=550)

        self.qishuentry1 = Text(self.ui, width = 12, height = 1)
        self.qishuentry1.place(x=497, y=553)
        self.qishuentry1.insert(END,0)

        self.qishuentry2 = Text(self.ui, width = 12, height = 1)
        self.qishuentry2.place(x=597, y=553)
        self.qishuentry2.insert(END, 0)


        ##妙手
        miaoshou = StringVar()
        miaoshou.set("妙手:")
        miaoshoulabel = Label(self.ui, textvariable=miaoshou, width=12, height=1)
        miaoshoulabel.place(x=384, y=580)
        miaoshoudes = CreateToolTip(miaoshoulabel, "允许对物体进行视觉上的遮住，藏匿，或者掩盖，也许通过残害，"
                                                   "衣服或者其他的干涉或促成错觉的材料，也许通过使用一个秘密的嵌板或者隔间。"
                                                   "任何种类的巨大物件应当增加藏匿的难度。妙手包括偷窃，卡牌魔术，以及秘密使用手机。"
                                                   "对抗技能为侦查（又是一个看似废招实则神技）")

        miaoshoubase = StringVar()
        miaoshoubase.set(10)
        miaoshoulabel = Label(self.ui, textvariable=miaoshoubase, width=5, height=1)
        miaoshoulabel.place(x=455, y=580)

        self.miaoshouentry1 = Text(self.ui, width = 12, height = 1)
        self.miaoshouentry1.place(x=497, y=583)
        self.miaoshouentry1.insert(END,0)

        self.miaoshouentry2 = Text(self.ui, width = 12, height = 1)
        self.miaoshouentry2.place(x=597, y=583)
        self.miaoshouentry2.insert(END, 0)


        ##侦查
        zhengcha = StringVar()
        zhengcha.set("侦查:")
        zhengchalabel = Label(self.ui, textvariable=zhengcha, width=12, height=1)
        zhengchalabel.place(x=384, y=610)
        zhengchades = CreateToolTip(zhengchalabel, "御三家技能之一。这项技能允许使用者发现密门或者秘密隔间，注意到隐藏的闯入者，发现并不明显的线索，"
                                                   "发现重新涂过漆的汽车，意识到埋伏，注意到鼓出的口袋，或者任何类似的事情。对于调查员来说，这是一个很重要的技能。（嗅觉属于侦查）")

        zhengchabase = StringVar()
        zhengchabase.set(25)
        zhengchalabel = Label(self.ui, textvariable=zhengchabase, width=5, height=1)
        zhengchalabel.place(x=455, y=610)

        self.zhengchaentry1 = Text(self.ui, width = 12, height = 1)
        self.zhengchaentry1.place(x=497, y=613)
        self.zhengchaentry1.insert(END,0)

        self.zhengchaentry2 = Text(self.ui, width = 12, height = 1)
        self.zhengchaentry2.place(x=597, y=613)
        self.zhengchaentry2.insert(END, 0)

        ##潜行
        qianxing = StringVar()
        qianxing.set("潜行:")
        qianxinglabel = Label(self.ui, textvariable=qianxing, width=12, height=1)
        qianxinglabel.place(x=384, y=640)
        qianxingdes = CreateToolTip(qianxinglabel, "安静地移动以及/或者躲藏的技巧，不惊扰到那些可能在听或者看的人们。"
                                                   "当尝试躲避探查，玩家应当进行一个潜行的技能检定。与这项技能相关的能力意味"
                                                   "着要么角色能够安静地移动（轻声轻足）以及/或者在伪装技巧上有所训练。（潜行不等于隐身，对抗技能为侦查）")

        qianxingbase = StringVar()
        qianxingbase.set(20)
        qianxinglabel = Label(self.ui, textvariable=qianxingbase, width=5, height=1)
        qianxinglabel.place(x=455, y=640)

        self.qianxingentry1 = Text(self.ui, width = 12, height = 1)
        self.qianxingentry1.place(x=497, y=643)
        self.qianxingentry1.insert(END,0)

        self.qianxingentry2 = Text(self.ui, width = 12, height = 1)
        self.qianxingentry2.place(x=597, y=643)
        self.qianxingentry2.insert(END, 0)


        ##追踪
        zhuizong = StringVar()
        zhuizong.set("追踪:")
        zhuizonglabel = Label(self.ui, textvariable=zhuizong, width=12, height=1)
        zhuizonglabel.place(x=384, y=670)
        zhuizongdes = CreateToolTip(zhuizonglabel, "一名调查员可以凭借追踪技能来通过土壤上的脚印，或是物体通过植被时留下的印记来追踪别人，"
                                                   "或者是交通工具以及地球上的动物。时间的经过，雨，以及土地的种类都可能会影响追踪的难度等级。（在大街上追人属于追踪）")

        zhuizongbase = StringVar()
        zhuizongbase.set(10)
        zhuizonglabel = Label(self.ui, textvariable=qianxingbase, width=5, height=1)
        zhuizonglabel.place(x=455, y=670)

        self.zhuizongentry1 = Text(self.ui, width = 12, height = 1)
        self.zhuizongentry1.place(x=497, y=673)
        self.zhuizongentry1.insert(END,0)

        self.zhuizongentry2 = Text(self.ui, width = 12, height = 1)
        self.zhuizongentry2.place(x=597, y=673)
        self.zhuizongentry2.insert(END, 0)









        jump_back = Button(self.ui, text="back",  command = lambda: self.jumpback(self.fr))
        jump_back.place(x=350, y=690)

    def raise_up(self):
        self.zhiye.set(self.player.zhiye)
        self.jinenghint.set("请将" + str(self.dianshudict[self.player.zhiye]) + "点技能点分配于本职技能，" + str(self.player.int * 2) + "点技能点分配于任意技能")
        self.benzhijineng.set(', '.join(self.jinengdict[self.player.zhiye]))


        self.ui.pack(fill=BOTH, expand=True)

    def jumpback(self, controller):
        self.ui.pack_forget()
        self.fr.pack(fill=BOTH, expand=True)