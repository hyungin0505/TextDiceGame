#############################################
#############################################
###### Build: hyungin0505(KoGandhi05)  ######
#############################################
#############################################

import random as r
import time as t

print("===================================")
print("==========  <홀짝 게임>  ==========")
print("===================================")
t.sleep(2)

print("")
print("===============================================================================")
print("기본으로 100포인트가 주어집니다.") 
point = 100
t.sleep(3)
print("배팅 가능한 최소 포인트는 10, 최대 포인트는 50입니다.")
t.sleep(3)
print("홀, 짝을 맞출 시 포인트의 두 배, 더블을 맞출 시 포인트의 다섯 배가 지급됩니다.")
t.sleep(3)
print("두 주사위 눈의 합을 맞추시면 됩니다.")
print("===============================================================================")
t.sleep(2)

print("")
print("=================================")
print("게임을 시작하려면 0을 눌러주세요")
print("=================================")

def exit():
    print("3초 후에 게임이 종료됩니다.")
    t.sleep(3)
    quit()

def game():
    print("")
    print("=================================")
    print("게임이 시작되었습니다.")
    print("=================================")
    print("")
    t.sleep(2)

    def loop():
        print("===========================================")
        print("배팅할 포인트를 입력해주세요 (숫자만 입력)")
        global bat_p

        def bat():
            global bat_p, b
            bat_p = int(input("입력: "))
            if bat_p < 10:
                print("배팅할 수 있는 최소 포인트는 10 이상입니다.")
                bat()
            elif bat_p > 50:
                print("배팅할 수 있는 최대 포인트는 50 이상입니다.")
                bat()
            elif bat_p > point:
                print("포인트가 부족합니다.")
                print("(현재 포인트: {}".format(str(point)))
                bat()
        bat()
        print("{}포인트를 배팅하였습니다.".format(str(bat_p)))
        print("===========================================")
        print("")

        print("=======================================================")
        print("홀 / 짝 / 더블 중 한 가지를 입력해주세요.")
        print("(홀수: 0, 짝수: 1, 더블: 2 / 숫자 또는 한글로 입력 가능)")
        print("=======================================================")

        def sel():
            global a, b
            a = str(input("입력: "))
            if a == "홀" or a== "0" or a== "홀수":
                b = "홀수를"
            elif a == "짝" or a == "1" or a == "짝수":
                b = "짝수를"
            elif a == "더블" or a == "2":
                b = "더블을"
            else:
                print("다시 정확히 입력해주세요.")
                sel()
        sel()
        print("{} 선택하셨습니다.".format(b))
        print("==================================")
        t.sleep(1)
        print("")
        print("==================================")
        print("주사위를 굴립니다", end = "")
        for i in range(1,4):
            print(".", end = "")
            t.sleep(0.8)
            i = i + 1
        t.sleep(1)
        print("")

        def main():
            global point, bat_p

            dice1 = r.randrange(1,6)
            print("첫 번째 주사위 눈의 수는 {}입니다.".format(str(dice1)))
            t.sleep(2)
            dice2 = r.randrange(1,6)
            print("두 번째 주사위 눈의 수는 {}입니다.".format(str(dice2)))
            print("==================================")
            print("")

            dice = dice1 + dice2
            if dice % 2 == 0:
                if dice1 == dice2:
                    c = "더블이"
                else:
                    c = "짝수"
            elif dice % 2 == 1:
                if dice1 == dice2:
                    c = "더블이"
                else:
                    c = "홀수"

            t.sleep(2)
            print("=================================")
            if a == "0" or a == "홀":
                if dice % 2 == 0:
                    print("맞추지 못했습니다.")
                    print("주사위의 숫자는 {}, {}였습니다.".format(str(dice), c))
                    point = point - bat_p
                    print("포인트를 잃었습니다.")
                    print("(현재 포인트: {})".format(str(point)))
                elif dice % 2 == 1:
                    print("맞추었습니다.")
                    print("주사위의 숫자는 {}, {}였습니다.".format(str(dice), c))
                    point = point + (2 * bat_p)
                    print("포인트를 얻었습니다.")
                    print("(현재 포인트: {})".format(str(point)))

            elif a == "1" or a == "짝":
                if dice % 2 == 1 or dice1 == dice2:
                    print("맞추지 못했습니다.")
                    print("주사위의 숫자는 {}, {}였습니다.".format(str(dice), c))
                    point = point - bat_p
                    print("포인트를 잃었습니다.")
                    print("(현재 포인트: {})".format(str(point)))
                elif dice % 2 == 0 and dice1 != dice2:
                    print("맞추었습니다.")
                    print("주사위의 숫자는 {}, {}였습니다.".format(str(dice), c))
                    point = point + (2 * bat_p)
                    print("포인트를 얻었습니다.")
                    print("(현재 포인트: {})".format(str(point)))

            elif a == "2" or a == "더블":
                if dice1 == dice2:
                    print("맞추었습니다.")
                    print("주사위의 숫자는 {}, {}였습니다.".format(str(dice), c))
                    point = point + (2 * bat_p)
                    print("포인트를 얻었습니다.")
                    print("(현재 포인트: {})".format(str(point)))
                else:
                    print("맞추지 못했습니다.")
                    print("주사위의 숫자는 {}, {}였습니다.".format(str(dice), c))
                    point = point - bat_p
                    print("포인트를 잃었습니다.")
                    print("(현재 포인트: {})".format(str(point)))
            else:
                print("정확히 입력해주세요.")
            print("=================================")
        main()

        if point > 0:
            print("재도전하려면 Y, 게임을 종료하려면 N 또는 아무 키을 입력해주세요")
            reset = str(input("입력: "))
            if reset == "Y" or reset == "y":
                loop()
            else:
                exit()
        else:
            print("포인트를 모두 잃었습니다...")
            exit()
    loop()
        
    
start = input("입력: ")
if start == "0":
    game()
else:
    exit()
