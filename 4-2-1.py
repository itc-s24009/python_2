def number_to_day(num=0):
    '''任意の整数が与えられたら今日、昨日、明日、それ以外を判定して返す

    戻り値
        昨日（numが−１の場合）
        今日（numが０の場合）
        明日（numが１の場合）
        今日より一日を超えて離れた日（numが上記以外の場合）
    '''
    if num == 0:
        day = "今日"
    elif num == 1:
        day = "明日"
    elif num == -1:
        day = "昨日"
    else:
        day = "今日より一日を超えて離れた日"
    return day
