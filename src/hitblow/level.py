def select_level():
    """
    難易度を選択する
    3: 3桁
    4: 4桁
    """
    while True:
        level = input("難易度を選んでください（3 または 4）> ").strip()

        if level == "3":
            return 3
        elif level == "4":
            return 4
        else:
            print("3 または 4 を入力してください。")