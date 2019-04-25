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