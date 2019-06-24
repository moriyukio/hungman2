# http://tinyurl.com/jhrvs94

import random, time

def hangman(word):                      # wordは当てなきゃいけない単語。
    wrong = 0                           # 間違えた回数
    stages = ["",
              "----------          ",
              "|        |          ",
              "|        |          ",
              "|        O          ",
              "|       /|\         ",
              "|       / \         ",
              "|                   ",
              ]
    rletters = list(word)               # 回答のwordを一文字づつのリスト変数化
    board = ["-"] * len(word)           # 表示用の文字列。－をwordの文字数分
    win = False                         # 勝ち負けの判定。
    print("ハングマンにようこそ！")     # welcomメッセージ
    
    while wrong < len(stages) - 1:      # wrong(間違えた回数)がリストstagesの要素数-1より小さくなるまで。
        print("\n")                     # 改行を表示
        msg = "１文字を予想してね : "      # メッセージのセット
        char = input(msg)               # インプットを要求

        if char in rletters:            # charの中身がリストrlettersの要素の中にあったら。。
            cind = rletters.index(char) # その文字のインデックスをcindに代入
            board[cind] = char          # boardの該当インデックスのことろの要素を、入力された文字に変更
            rletters[cind] = '$'        # rlettersの該当要素を＄に変更する。
        else:
            wrong += 1
        print(" ".join(board))          # リストboardの要素を、間に" "を挟んで接続して表示
        e = wrong + 1                   # eにwrong(間違えた回数）＋１を代入
        print("\n".join(stages[0:e]))   # リスト変数sagesの要素をインデックスeまで、/nを挟んで接続
        if "-" not in board:            # boardの要素に"-"が無かったら
            print("あなたの勝ち！")     # メッセージを表示
            print(" ".join(board))      # boardの要素を" "を挟んで接続したものを表示
            win = True
            time.sleep(10)
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！！！！！正解は {}.".format(word))
        time.sleep(10)

words = ["cat", "dog", "cae", "cad", "ant", "ash", "bee", "bow", "box", "boy",
         "bus", "cow", "ear", "eel", "eye", "fly", "fox", "guy", "hen", "inn",
         "jaw", "key", "law", "leg", "saw", "ray", "row", "owl", "nap", "mud"
         ]
ans_word = words[random.randint(0, 39)]
# print(ans_word)
hangman(ans_word)
