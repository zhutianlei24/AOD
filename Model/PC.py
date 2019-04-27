import random
from math import floor
class player(object):

    def __init__(self, NAME, AGE, STR, CON, SIZ, DEX, APP, EDU, INT, POW, LUCK):
        ##这一段是初始化基本属性
        self.name = NAME
        self.age = AGE
        self.str = STR
        self.con = CON
        self.siz = SIZ
        self.dex = DEX
        self.app = APP
        self.edu = EDU
        self.int = INT
        self.pow = POW
        self.hp = floor((CON + SIZ)/10)
        self.san = POW
        self.luck = LUCK
        if(15 <= self.age <=19):
            tmp = (random.randint(1,6) + random.randint(1,6) + random.randint(1,6))*5
            self.luck = self.luck if self.luck > tmp else tmp
            self.edu -= 5
            strreduce = random.randint(0,1)
            self.str -= strreduce * 5
            self.siz -= (5 - strreduce * 5)
        if (20 <= self.age <= 39):
            tmp = random.randint(1,100)
            if(tmp >= self.edu):
                eduadd = random.randint(1,10)
                self.edu += eduadd
        if (40 <= self.age <= 49):
            for i in range(1,3):
                tmp = random.randint(1, 100)
                if (tmp >= self.edu):
                    eduadd = random.randint(1, 10)
                    self.edu += eduadd
            strreduce = random.randint(0, 1)
            self.str -= strreduce * 5
            if(strreduce == 0):
                sizreduce = random.randint(0, 1)
                self.siz -= sizreduce * 5
                self.con -= (5 - sizreduce * 5)
            self.app -= 5

        self.db = 0;
        if (124 < (self.str + self.con) < 165):
            db = 1
        if (164 < (self.str + self.con) < 205):
            db = 2
        ###这一段是初始化技能
        self.kuaiji = 5 ##会计
        self.renleixue = 1 ##人类学
        self.gujia = 5 ##估价
        self.kaoguxue = 5 ##考古学
        self.meihuo = 15 ##魅惑
        self.panpa = 20 ##攀爬
        self.jisuanji = 5 ##计算机使用
        self.xinyong = 0 ##信用评级
        self.qiaozhuang = 5 ##乔庄
        self.shanbi = floor(self.dex/2) ##闪避
        self.qichejiashi = 20 ##汽车驾驶
        self.dianqiweixiu = 10 ##电器维修
        self.dianzixue = 1 ##电子学
        self.huashu = 5 ##话术
        self.douou = 25 ##斗殴
        self.shouqiang = 20 ##手枪
        self.jijiu = 30 ##急救
        self.lishi = 5 ##历史
        self.konghe = 15 ##恐吓
        self.tiaoyue = 20 ##跳跃
        self.muyu = self.edu ##母语
        self.falv = 5 ##法律
        self.tushuguan = 20 ##图书馆
        self.lingting = 20 ##聆听
        self.suojiang = 1 ##锁匠
        self.jixieweixiu = 10 ##机械维修
        self.yixue = 1 ##医学
        self.bowuxue = 10 ##博物学
        self.linghang = 10 ##领航
        self.shenmixue = 5 ##神秘学
        self.zhongxingjixie = 1 ##操作重型机械
        self.shuofu = 10 ##说服
        self.jingshengfenxi = 1 ##精神分析
        self.xinlixue = 10 ##心理学
        self.qishu = 5 ##骑术
        self.miaoshou = 10 ##妙手
        self.zhencha = 25 ##侦查
        self.qianxing = 20 ##潜行
        self.youyong = 20 ##游泳
        self.touzhi = 20 ##投掷
        self.zhuizong = 10 ##追踪


        self.zhiye = ''
        self.sex = ''
        self.living = ''
        self.born = ''
        self.appdes = ''
        self.thoughts = ''
        self.love = ''
        self.place = ''
        self.tresure = ''
        self.special = ''
        self.things = ''
        self.background = ''

    ##获取八大属性和
    def sum_attr(self):
        sum = self.str + self.con + self.siz + self.dex + self.app + self.edu + self.int + self.pow
        rt = "八大属性和:"+ str(sum) + "， 幸运" + str(self.luck)
        return rt

    # ##会计
    # def add_kuaiji(self, zhiye, xingqu):
    #     self.kuaiji += zhiye + xingqu
    # def roll_kuaiji(self):
    #     flag = False
    #     done = False
    #     lvl = 0
    #     if (self.kuaiji >= 50):
    #         flag = True
    #     dice = random.randint(1, 100)
    #     if (dice <= self.kuaiji):
    #          if ((dice <= 5 and flag) or (dice == 1)):
    #             rt = self.name, "进行会计鉴定：", str(dice), "/", str(self.kuaiji), "大成功"
    #             lvl = 5
    #             done = True
    #          if (dice <= round(self.kuaiji/5) and not done):
    #             rt = self.name, "进行会计鉴定：", str(dice), "/", str(self.kuaiji), "极限成功"
    #             lvl = 4
    #             done = True
    #          if(dice <= round(self.kuaiji/2) and not done):
    #             rt = self.name, "进行会计鉴定：", str(dice), "/", str(self.kuaiji), "困难成功"
    #             lvl = 3
    #             done = True
    #          if(not done):
    #             rt = self.name, "进行会计鉴定：", str(dice), "/", str(self.kuaiji), "成功"
    #             lvl = 2
    #             done = True
    #     else:
    #          if ((dice >= 96 and not flag) or (dice == 100)):
    #             rt = self.name, "进行会计鉴定：", str(dice), "/", str(self.kuaiji), "大失败"
    #             lvl = 0
    #          else:
    #             rt = self.name, "进行会计鉴定：", str(dice), "/", str(self.kuaiji), "失败"
    #             lvl = 1
    #     return ("".join(rt),lvl)

    ##通用判定方法
    def roll_attr(self, shuzhi, mingcheng):
        flag = False
        done = False
        lvl = 0
        if(shuzhi >= 50):
            flag = True
        dice = random.randint(1, 100)
        if (dice <= shuzhi):
            if ((dice <= 5 and flag) or (dice == 1)):
                rt = self.name, "进行", mingcheng, "鉴定：", str(dice), "/", str(shuzhi), "大成功"
                lvl = 5
                done = True
            if (dice <= floor(shuzhi / 5) and not done):
                rt = self.name, "进行", mingcheng, "鉴定：",str(dice), "/", str(shuzhi), "极限成功"
                lvl = 4
                done = True
            if (dice <= floor(shuzhi / 2) and not done):
                rt = self.name, "进行", mingcheng, "鉴定：", str(dice), "/", str(shuzhi), "困难成功"
                lvl = 3
                done = True
            if (not done):
                rt = self.name, "进行", mingcheng, "鉴定：", str(dice), "/", str(shuzhi), "成功"
                lvl = 2
                done = True
        else:
            if ((dice >= 96 and not flag) or (dice == 100)):
                rt = self.name, "进行", mingcheng, "鉴定：", str(dice), "/", str(shuzhi), "大失败"
                lvl = 0
            else:
                rt = self.name, "进行", mingcheng, "鉴定：", str(dice), "/", str(shuzhi), "失败"
                lvl = 1
        return ("".join(rt), lvl)

    ##会计
    def add_kuaiji(self, zhiye, xingqu):
        self.kuaiji += zhiye + xingqu
    def roll_kuaiji(self):
        result = self.roll_attr(self.kuaiji, "会计")
        return result

    ##人类学
    def add_renleixue(self, zhiye, xingqu):
        self.renleixue += zhiye + xingqu
    def roll_renleixue(self):
        result = self.roll_attr(self.renleixue, "人类学")
        return result

    ##估价
    def add_gujia(self, zhiye, xingqu):
        self.gujia += zhiye + xingqu
    def roll_gujia(self):
        result = self.roll_attr(self.gujia, "估价")
        return result

    ##考古学
    def add_kaoguxue(self, zhiye, xingqu):
        self.kaoguxue += zhiye + xingqu
    def roll_kaoguxue(self):
        result = self.roll_attr(self.kaoguxue, "考古学")
        return result

    ##魅惑
    def add_meihuo(self, zhiye, xingqu):
        self.meihuo += zhiye + xingqu
    def roll_meihuo(self):
        result = self.roll_attr(self.meihuo, "魅惑")
        return result

    ##攀爬
    def add_panpa(self, zhiye, xingqu):
        self.panpa += zhiye + xingqu
    def roll_panpa(self):
        result = self.roll_attr(self.panpa, "攀爬")
        return result

    ##计算机使用
    def add_jisuanji(self, zhiye, xingqu):
        self.jisuanji += zhiye + xingqu
    def roll_jisuanji(self):
        result = self.roll_attr(self.jisuanji, "计算机使用")
        return result

    ##信用评级
    def add_xinyong(self, zhiye, xingqu):
        self.xinyong += zhiye + xingqu
    def roll_xinyong(self):
        result = self.roll_attr(self.xinyong, "信用")
        return result

    ##乔庄
    def add_qiaozhuang(self, zhiye, xingqu):
        self.qiaozhuang += zhiye + xingqu
    def roll_qiaozhuang(self):
        result = self.roll_attr(self.qiaozhuang, "乔庄")
        return result

    ##闪避
    def add_shanbi(self, zhiye, xingqu):
        self.shanbi += zhiye + xingqu
    def roll_shanbi(self):
        result = self.roll_attr(self.shanbi, "闪避")
        return result

    ##汽车驾驶
    def add_qichejiashi(self, zhiye, xingqu):
        self.qichejiashi += zhiye + xingqu
    def roll_qichejiashi(self):
        result = self.roll_attr(self.qichejiashi, "汽车驾驶")
        return result

    ##电器维修
    def add_dianqiweixiu(self, zhiye, xingqu):
        self.dianqiweixiu += zhiye + xingqu
    def roll_dianqiweixiu(self):
        result = self.roll_attr(self.dianqiweixiu, "电器维修")
        return result

    ##电子学
    def add_dianzixue(self, zhiye, xingqu):
        self.dianzixue += zhiye + xingqu
    def roll_dianzixue(self):
        result = self.roll_attr(self.dianzixue, "电子学")
        return result

    ##话术
    def add_huashu(self, zhiye, xingqu):
        self.huashu += zhiye + xingqu
    def roll_huashu(self):
        result = self.roll_attr(self.huashu, "话术")
        return result

    ##斗殴
    def add_douou(self, zhiye, xingqu):
        self.douou += zhiye + xingqu
    def roll_douou(self):
        result = self.roll_attr(self.douou, "斗殴")
        return result

    ##手枪射击
    def add_shouqiang(self, zhiye, xingqu):
        self.shouqiang += zhiye + xingqu
    def roll_shouqiang(self):
        result = self.roll_attr(self.shouqiang, "手枪射击")
        return result

    ##急救
    def add_jijiu(self, zhiye, xingqu):
        self.jijiu += zhiye + xingqu
    def roll_jijiu(self):
        result = self.roll_attr(self.jijiu, "急救")
        return result

    ##历史
    def add_lishi(self, zhiye, xingqu):
        self.lishi += zhiye + xingqu
    def roll_lishi(self):
        result = self.roll_attr(self.lishi, "历史")
        return result

    ##恐吓
    def add_konghe(self, zhiye, xingqu):
        self.konghe += zhiye + xingqu
    def roll_konghe(self):
        result = self.roll_attr(self.konghe, "恐吓")
        return result

    ##跳跃
    def add_tiaoyue(self, zhiye, xingqu):
        self.tiaoyue += zhiye + xingqu
    def roll_tiaoyue(self):
        result = self.roll_attr(self.tiaoyue, "跳跃")
        return result

    ##跳跃
    def add_tiaoyue(self, zhiye, xingqu):
        self.tiaoyue += zhiye + xingqu
    def roll_tiaoyue(self):
        result = self.roll_attr(self.tiaoyue, "跳跃")
        return result

    ##母语
    ##母语不存在增强，只有roll点（很少出现）
    def roll_muyu(self):
        result = self.roll_attr(self.muyu, "母语")
        return result

    ##法律
    def add_falv(self, zhiye, xingqu):
        self.falv += zhiye + xingqu
    def roll_falv(self):
        result = self.roll_attr(self.falv, "法律")
        return result

    ##图书馆使用
    def add_tushuguan(self, zhiye, xingqu):
        self.tushuguan += zhiye + xingqu
    def roll_tushuguan(self):
        result = self.roll_attr(self.tushuguan, "图书馆使用")
        return result

    ##聆听
    def add_lingting(self, zhiye, xingqu):
        self.lingting += zhiye + xingqu
    def roll_lingting(self):
        result = self.roll_attr(self.lingting, "聆听")
        return result

    ##锁匠
    def add_suojiang(self, zhiye, xingqu):
        self.suojiang += zhiye + xingqu
    def roll_suojiang(self):
        result = self.roll_attr(self.suojiang, "锁匠")
        return result

    ##机械维修
    def add_jixieweixiu(self, zhiye, xingqu):
        self.jixieweixiu += zhiye + xingqu
    def roll_jixieweixiu(self):
        result = self.roll_attr(self.jixieweixiu, "机械维修")
        return result

    ##医学
    def add_yixue(self, zhiye, xingqu):
        self.yixue += zhiye + xingqu
    def roll_yixue(self):
        result = self.roll_attr(self.yixue, "医学")
        return result

    ##博物学
    def add_bowuxue(self, zhiye, xingqu):
        self.bowuxue += zhiye + xingqu
    def roll_bowuxue(self):
        result = self.roll_attr(self.bowuxue, "博物学")
        return result

    ##领航
    def add_linghang(self, zhiye, xingqu):
        self.linghang += zhiye + xingqu
    def roll_linghang(self):
        result = self.roll_attr(self.linghang, "领航")
        return result

    ##神秘学
    def add_shenmixue(self, zhiye, xingqu):
        self.shenmixue += zhiye + xingqu
    def roll_shenmixue(self):
        result = self.roll_attr(self.shenmixue, "神秘学")
        return result

    ##操作重型机械
    def add_zhongxingjixie(self, zhiye, xingqu):
        self.zhongxingjixie += zhiye + xingqu
    def roll_zhongxingjixie(self):
        result = self.roll_attr(self.zhongxingjixie, "操作重型机械")
        return result

    ##说服
    def add_shuofu(self, zhiye, xingqu):
        self.shuofu += zhiye + xingqu
    def roll_shuofu(self):
        result = self.roll_attr(self.shuofu, "说服")
        return result

    ##精神分析
    def add_jingshengfenxi(self, zhiye, xingqu):
        self.jingshengfenxi += zhiye + xingqu
    def roll_jingshengfenxi(self):
        result = self.roll_attr(self.jingshengfenxi, "精神分析")
        return result

    ##心理学
    def add_xinlixue(self, zhiye, xingqu):
        self.xinlixue += zhiye + xingqu
    def roll_xinlixue(self):
        result = self.roll_attr(self.xinlixue, "心理学")
        return result

    ##骑术
    def add_qishu(self, zhiye, xingqu):
        self.qishu += zhiye + xingqu
    def roll_qishu(self):
        result = self.roll_attr(self.qishu, "心理学")
        return result

    ##妙手
    def add_miaoshou(self, zhiye, xingqu):
        self.miaoshou += zhiye + xingqu
    def roll_miaoshou(self):
        result = self.roll_attr(self.miaoshou, "妙手")
        return result

    ##侦查
    def add_zhencha(self, zhiye, xingqu):
        self.zhencha += zhiye + xingqu
    def roll_zhencha(self):
        result = self.roll_attr(self.zhencha, "侦查")
        return result

    ##潜行
    def add_qianxing(self, zhiye, xingqu):
        self.qianxing += zhiye + xingqu
    def roll_qianxing(self):
        result = self.roll_attr(self.qianxing, "潜行")
        return result

    ##游泳
    def add_youyong(self, zhiye, xingqu):
        self.youyong += zhiye + xingqu
    def roll_youyong(self):
        result = self.roll_attr(self.youyong, "游泳")
        return result

    ##投掷
    def add_touzhi(self, zhiye, xingqu):
        self.touzhi += zhiye + xingqu
    def roll_touzhi(self):
        result = self.roll_attr(self.touzhi, "投掷")
        return result

    ##追踪
    def add_zhuizong(self, zhiye, xingqu):
        self.zhuizong += zhiye + xingqu
    def roll_zhuizong(self):
        result = self.roll_attr(self.zhuizong, "追踪")
        return result
