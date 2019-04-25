from View.InitialAttr import *



window = Tk()
window.title("COC新人车卡模拟器|作者：阳明|请勿用于商业用途！")

window.geometry('740x730')
InitialAttr(window)
window.mainloop()

# hello = StringVar()
# hello.set("请在此处输入你的姓名，年龄和九大属性，确认后不可修改")
# hellolabel  = Label(window, textvariable = hello, width=100,height=2)
# hellolabel.place(x = -10, y = 0)

# name = StringVar()
# name.set("姓名：")
# namelabel = Label(window, textvariable = name, width=80,height=2)
# namelabel.place(x = -50, y = 50)
# entryname = Entry(window)
# entryname.place(x = 300, y = 60)
#
# age = StringVar()
# age.set("年龄：")
# agelabel = Label(window, textvariable = age, width=80,height=2)
# agelabel.place(x = -50, y = 100)
# entryage = Entry(window)
# entryage.place(x = 300, y = 110)
#
# strength = StringVar()
# strength.set("力量：")
# strengthlabel = Label(window, textvariable = strength, width=80,height=2)
# strengthlabel.place(x = -50, y = 150)
# entrystrength = Entry(window)
# entrystrength.place(x = 300, y = 160)
#
# constitution = StringVar()
# constitution.set("体质：")
# constitutionlabel = Label(window, textvariable = constitution, width=80,height=2)
# constitutionlabel.place(x = -50, y = 200)
# entryconstitution = Entry(window)
# entryconstitution.place(x = 300, y = 210)
#
# size = StringVar()
# size.set("体型：")
# sizelabel = Label(window, textvariable = size, width=80,height=2)
# sizelabel.place(x = -50, y = 250)
# entrysize = Entry(window)
# entrysize.place(x = 300, y = 260)
#
# dexterity = StringVar()
# dexterity.set("敏捷：")
# dexteritylabel = Label(window, textvariable = dexterity, width=80,height=2)
# dexteritylabel.place(x = -50, y = 300)
# entrydexterity = Entry(window)
# entrydexterity.place(x = 300, y = 310)
#
# appearence = StringVar()
# appearence.set("外貌：")
# appearencelabel = Label(window, textvariable = appearence, width=80,height=2)
# appearencelabel.place(x = -50, y = 350)
# entryappearence = Entry(window)
# entryappearence.place(x = 300, y = 360)
#
# education = StringVar()
# education.set("教育：")
# educationlabel = Label(window, textvariable = education, width=80,height=2)
# educationlabel.place(x = -50, y = 400)
# entryeducation = Entry(window)
# entryeducation.place(x = 300, y = 410)
#
# intelligence = StringVar()
# intelligence.set("智力/灵感：")
# intelligencelabel = Label(window, textvariable = intelligence, width=80,height=2)
# intelligencelabel.place(x = -50, y = 450)
# entryintelligence = Entry(window)
# entryintelligence.place(x = 300, y = 460)
#
# power = StringVar()
# power.set("意志：")
# powerlabel = Label(window, textvariable = power, width=80,height=2)
# powerlabel.place(x = -50, y = 500)
# entrypower = Entry(window)
# entrypower.place(x = 300, y = 510)
#
# luck = StringVar()
# luck.set("幸运：")
# lucklabel = Label(window, textvariable = luck, width=80,height=2)
# lucklabel.place(x = -50, y = 550)
# entryluck = Entry(window)
# entryluck.place(x = 300, y = 560)
#
# def randomattr():
#     stre = random.randint(1,6) * 5 + random.randint(1,6) * 5 + random.randint(1,6) * 5
#     con = random.randint(1,6) * 5 + random.randint(1,6) * 5 + random.randint(1,6) * 5
#     siz = (random.randint(1,6) + random.randint(1,6) + 6) * 5
#     dex = random.randint(1,6) * 5 + random.randint(1,6) * 5 + random.randint(1,6) * 5
#     app = random.randint(1,6) * 5 + random.randint(1,6) * 5 + random.randint(1,6) * 5
#     int = (random.randint(1,6) + random.randint(1,6) + 6) * 5
#     pow = random.randint(1,6) * 5 + random.randint(1,6) * 5 + random.randint(1,6) * 5
#     edu = (random.randint(1,6) + random.randint(1,6) + 6) * 5
#     luck = random.randint(1,6) * 5 + random.randint(1,6) * 5 + random.randint(1,6) * 5
#
#     entrystrength.delete(0,END)
#     entrystrength.insert(END,stre)
#     entryconstitution.delete(0,END)
#     entryconstitution.insert(END,con)
#     entrysize.delete(0,END)
#     entrysize.insert(END,siz)
#     entrydexterity.delete(0,END)
#     entrydexterity.insert(END,dex)
#     entryappearence.delete(0,END)
#     entryappearence.insert(END,app)
#     entryeducation.delete(0,END)
#     entryeducation.insert(END,edu)
#     entryintelligence.delete(0,END)
#     entryintelligence.insert(END,int)
#     entrypower.delete(0,END)
#     entrypower.insert(END,pow)
#     entryluck.delete(0,END)
#     entryluck.insert(END,luck)
#
#
# wannarandom=Button(window,text='懒？直接随机一下？',width=15,height=2,command=randomattr)
# wannarandom.place(x = 150, y = 640)
#
# createchara=Button(window,text='数值确认无误，创建！',width=20,height=2,command=randomattr)
# createchara.place(x = 450, y = 640)


# var=StringVar()#tk中特定的变量形式，字符串变量。
# var.set("进行话术鉴定")
# l=Label(window,textvariable=var,
#     width=40,height=2)
# l.pack()
#
# def huashu():
#     PChuashu = 60
#     flag = False
#     if(PChuashu >= 50):
#         flag = True
# #     dice = random.randint(1, 100)
#     if(dice <= PChuashu ):
#         if((dice <= 5 and flag) or (dice == 1)):
#             str = "进行话术鉴定：", dice, "/", PChuashu, "大成功"
#             var.set(str)
#         else:
#             str = "进行话术鉴定：",dice,"/",PChuashu,"成功"
#             var.set(str)
#     else:
#         if((dice >=96 and not flag) or (dice == 100)):
#             str = "进行话术鉴定：", dice, "/", PChuashu, "大失败"
#             var.set(str)
#         else:
#             str = "进行话术鉴定：",dice,"/",PChuashu,"失败"
#             var.set(str)
# #
# bt = Button(window,text = "话术",width = 7, height = 1, command = huashu)
# bt.pack()




# mynpc = player("拉冰娜",30,80,60,80,25,40,70,60,40)
# mynpc.add_zhongxingjixie(10,0)
# for i in range(1,6):
#  print(mynpc.roll_zhongxingjixie())