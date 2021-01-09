import random 
print ("qwq需要什么服务嘛？")
print ("1.猜数字")
print ("2.查询好感度")
print ("3.退出")
chushi = input("输入数字:") #初始值（话说不能直接就int嘛，为什么是str）
intchushi = int(chushi) #初始值int转换
if intchushi == 1 or intchushi == 2: #判断值是不是1或者2，如果是1或者2返回True
    if intchushi == 1: #判断值是不是1，如果是1返回Ture
        caice = input("qwq猜猜我想的是什么数字吧?")
        suiji = random.randint(1,2) #一个从1到10的随机数字（包括1和10）
        while caice !=suiji:
            caice = input("再试一试？猜猜布丁想的是什么数字")
            caice = int(caice)
            if caice == suiji:
                print ("QAQ你竟然知道")
                duqu2 = open("ceshi.txt")
                duqu3 = duqu2.read()
                duqu4 = int(duqu3)
                duqu2.close()
                cucun1 = duqu4 + 1
                cucun2 = str(cucun1)
                cucun = open("ceshi.txt", "w")
                cucun.write(cucun2)
                print ("布丁对你的好感度+1")
            else:
                if caice > suiji:
                        print ("好像大了")
                else:
                        print ("好像小了")
    else:
        duqu = open("ceshi.txt")
        print("好感度为:"+duqu.read())
else: #初始输入的值不是1或者2就运行这里
    if intchushi == 3: #如果是3就退出程序
        print ("程序退出")
    else: #啥都不是输出这里
        print ("你输入些什么!?") #貌似可以在这里加个循环功能