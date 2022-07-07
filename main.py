import funcs
while True:
    a = input("Введите команду\n-r для рега нового пользовтеля\n-l для запуска клиента \n-s для начала обучения\n:")
    if a == "-r":
        funcs.authAndDownload()
    elif a == "-l":
        funcs.launch_Client()
    elif a == "-s":
       funcs.learn()
    else:
        print("Такой команды нет")