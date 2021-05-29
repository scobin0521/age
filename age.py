drive = input('請問你有沒有開過車?')
if drive != '有' and drive != '沒有':
    print('只能輸入 有/沒有')
    raise SystemExit    #如出現錯誤程式會停止

age = int(input('請問你的年齡？'))
#input得到的值都會被轉成字串
#所以字串和整數比較會出現錯誤，必須先將age轉成整數(int)
if drive == '有':
    if age >= 18:
        print('你通過測驗了')
    else:
        print('奇怪!你怎麼會開過車？')
elif drive == '沒有':
    if age >= 18:
        print('你可以考駕照了啊，怎麼還不去考呢?')
    else:
        print('很好，再過' + str(18 - age) + '年就可以考駕照')
else:
    print('只能輸入 有/沒有')
