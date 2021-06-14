from winsound import Beep
from time import sleep

print ("/끝말잇기, /포기, /끝, /정보")

mefirst = "저부터 할게요."
notonlist = "사전에 있는 단어를 입력하셔야죠."
taunt = "너무 쉽네요. 한 판 더해요!"
length = "한 글자 이상 입력하셔야죠."
win = "제가 이겼어요!"
spacebar = "띄어쓰기는 안되죠."
lose = "잘하시네요. 한 판 더해요!"
doubt = "있는 단어인지 의심되네요. 그래도 계속할게요."
rule = "이어지는 단어를 입력하셔야죠."
idk = "이해하지 못했어요."
bye = "다음에 또 봐요!"


import random
words = open("일반단어.txt", "r").read().split()
finisher = open("한방단어.txt", "r", encoding='UTF8').read().split()

def 두음법칙(word):
        if word[-1] == "라":
            word = word.replace('라','나')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "락":
            word = word.replace('락','낙')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "란":
            word = word.replace('란','난')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "람":
            word = word.replace('람','남')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "랍":
            word = word.replace('랍','납')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "랑":
            word = word.replace('랑','낭')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "랄":
            word = word.replace('랄','날')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "래":
            word = word.replace('래','내')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "랭":
            word = word.replace('랭','냉')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "냥":
            word = word.replace('냥','양')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "렵":
            word = word.replace('렵','엽')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "로":
            word = word.replace('로','노')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "록":
            word = word.replace('록','녹')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "론":
            word = word.replace('론','논')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "롱":
            word = word.replace('롱','농')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "뢰":
            word = word.replace('뢰','뇌')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "룡":
            word = word.replace('룡','용')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "루":
            word = word.replace('루', '누')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "륜":
            word = word.replace('륜', '윤')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "률":
            word = word.replace('률', '율')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "륭":
            word = word.replace('륭', '융')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "륵":
            word = word.replace('륵', '늑')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "름":
            word = word.replace('름', '늠')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "릉":
            word = word.replace('릉', '능')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "릉":
            word = word.replace('릉', '능')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "린":
            word = word.replace('린', '인')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "림":
            word = word.replace('림', '임')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "립":
            word = word.replace('립', '입')
            print("(두음법칙: "+word[-1]+")")
            return word
        
        if word[-1] == "냑":
            word = word.replace('냑', '약')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "략":
            word = word.replace('략', '약')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "냥":
            word = word.replace('냥', '양')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "량":
            word = word.replace('량', '양')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "녀":
            word = word.replace('녀', '여')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "려":
            word = word.replace('려', '여')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "녁":
            word = word.replace('녁', '역')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "력":
            word = word.replace('력', '역')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "년":
            word = word.replace('년', '연')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "련":
            word = word.replace('년', '연')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "녈":
            word = word.replace('녈', '열')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "렬":
            word = word.replace('렬', '열')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "념":
            word = word.replace('념', '염')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "렴":
            word = word.replace('렴', '염')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "녕":
            word = word.replace('녕', '영')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "령":
            word = word.replace('령', '영')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "녜":
            word = word.replace('녜', '예')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "례":
            word = word.replace('례', '예')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "뇨":
            word = word.replace('뇨', '요')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "료":
            word = word.replace('료', '요')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "뉴":
            word = word.replace('뉴', '유')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "류":
            word = word.replace('류', '유')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "뉵":
            word = word.replace('뉵', '육')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "륙":
            word = word.replace('륙', '육')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "니":
            word = word.replace('니', '이')
            print("(두음법칙: "+word[-1]+")")
            return word
        if word[-1] == "리":
            word = word.replace('리', '이')
            print("(두음법칙: "+word[-1]+")")
            return word
        else:
            return word
        #위의 경우 외에는 두음법칙으로 인정하지 않음

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
            return  random.choice(available_finishers)+"(한방단어)" #적절한 한방단어가 있다면 그 단어 return
        else:
            available_words = [i for i in words if i[0] == previous_word[-1] and len(i) > 1] 
        if not available_words:
            return '' # 적절한 일반단어가 없다면 게임종료
        else:
            return random.choice(available_words) #적절한 일반단어가 있다면 그 단어 return


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
            computer_word = 두음법칙(computer_word1) #두음법칙 적용
            Beep(1000, 200)
            user_word1 =input("단어 입력: ")
            user_word = 두음법칙(user_word1) #두음법칙 적용


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
        print(" 화이트 코딩 동아리 11011 박준서 제작, '악질 끝말잇기' \n 왜 악질인지는 해 보면 알 것입니다.")
    elif user == "/끝말잇기":
        word_chain()
    else:
        print ("적절한 명령어가 아닙니다.")
