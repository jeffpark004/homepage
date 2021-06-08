from winsound import Beep
from time import sleep
from 두음법칙 import 두음법칙

print ("/끝말잇기, /포기, /끝, /정보")

mefirst = "저부터 할게요."
notonlist = "사전에 있는 단어를 입력하셔야죠."
taunt = "너무 쉽네요. 한 판 더해요!"
length = "한 글자 이상 입력하셔야죠."
win = "제가 이겼어요!"
spacebar = "단어를 입력하셔야죠."
lose = "잘하시네요. 한 판 더해요!"
doubt = "있는 단어인지 의심되네요. 그래도 계속할게요."
rule = "이어지는 단어를 입력하셔야죠."
idk = "이해하지 못했어요."
bye = "다음에 또 봐요!"


import random
words = open("일반단어.txt", "r").read().split()
finisher = open("한방단어.txt", "r", encoding='UTF8').read().split()


def judge(word1, word2):
#    if word2 not in words:      #사용자가 입력한 단어가 일반단어.txt에 있는지 확인
#      print(notonlist) 
#      return False
    if len(word2) == 1:         #한 글자 단어 금지
        print (length)
        return False            #공백 입력 금지
    if ' 'in word2:
        print (spacebar)
        return False
    if len(word2) > 10:         #사용자가 입력한 단어가 10글자가 넘을 경우, 의심 메세지 출력
         print (doubt)
         return True
    if word1[-1] == word2[0]:
        return True
    if word2 == "/포기":      
        return False
        
    else:
        print (rule)
        return False

def word_selection(previous_word):
        if not previous_word:
            return random.choice(words)
        else:
            available_finishers = [i for i in finisher if i[0] == previous_word[-1] and len(i) > 1]
        if available_finishers:
            return  random.choice(available_finishers)+"(한방단어)"
        else:
            available_words = [i for i in words if i[0] == previous_word[-1] and len(i) > 1]
        if not available_words:
            return ''
        else:
            return random.choice(available_words)


def word_chain():
    user_word=''
    print (mefirst)
    while True:
        computer_word1 = word_selection(user_word)
        if "한방단어" in computer_word1:
            print("컴퓨터:", computer_word1)
            Beep(800, 200)
            print(taunt)        #한방단어 쓴 후 도발하기
            break
        if not computer_word1:
            print(lose)
            sleep(1)
            user_word = ''
            continue
        
        else:
            print("컴퓨터:", computer_word1)
            computer_word = 두음법칙(computer_word1)
            Beep(1000, 200)
            user_word1 =input("단어 입력: ")
            user_word = 두음법칙(user_word1)


            if not judge(computer_word, user_word):
                print(win)
                break

    
    

while True:
    user = input("명령어 입력: ")
    if user == "/끝":
        print(bye)
        sleep(3)
        break
    elif user == "/정보":
        print(" 화이트 코딩 동아리 11011 박준서 제작, 악질 끝말잇기' \n 왜 악질인지는 해 보면 알 것입니다.")
    elif user == "/끝말잇기":
        word_chain()
    else:
        print ("적절한 명령어가 아닙니다.")
