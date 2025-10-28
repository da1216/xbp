for i in range(1,4): #コロンが入っていることに注意
    import random
    answer = random.choice(["1","2"])
    select=input("1か2を選んでください")
    if select == answer:
     print("えらい！！すごい！！")
    else:
     print("残念！！無念！！また来年！！")

    print(i,"回目") #タブでずらしていることに注意！


