def create_template(count):
    d = dict()
    for i in range(1, count + 1):
        d[i] = {
            "Q": {
                "text": "", "img": ""
            },
            "Option": {
                "A": {"text": "", "img": ""},
                "B": {"text": "", "img": ""},
                "C": {"text": "", "img": ""},
                "D": {"text": "", "img": ""}
            },
            "isImage": ""
        }

    return d


def year112():
    question = {
        1: {
            'Q': {'text': '有四個算式如下圖，這些算式的計算結果，從大到小順序為何？', 'img': './Question/images/math/112_math_1_Q.PNG'},
            'Option': {
                'A': {'text': '(A)丙 ＞ 甲 ＞ 乙 ＞ 丁', 'img': ''},
                'B': {'text': '(B)丙 ＞ 丁 ＞ 甲 ＞ 乙', 'img': ''},
                'C': {'text': '(C)丁 ＞ 甲 ＞ 乙 ＞ 丙', 'img': ''},
                'D': {'text': '(D)丁 ＞ 丙 ＞ 甲 ＞ 乙', 'img': ''}
            }, 'isImage': 'Q'},
        2: {
            'Q': {'text': '本題題目如下圖所示：', 'img': './Question/images/math/112_math_2_Q.PNG'},
            'Option': {
                'A': {'text': '', 'img': './Question/images/math/112_math_2_A.PNG'},
                'B': {'text': '', 'img': './Question/images/math/112_math_2_B.PNG'},
                'C': {'text': '', 'img': './Question/images/math/112_math_2_C.PNG'},
                'D': {'text': '', 'img': './Question/images/math/112_math_2_D.PNG'}
            }, 'isImage': 'Q&A'},
        3: {
            'Q': {'text': '某鄉舉辦吉祥物票選活動，鄉民每人一票，票選結果統計表如下，下列何者為吉祥物票選結果的眾數？', 'img': './Question/images/math/112_math_3_Q.PNG'},
            'Option': {
                'A': {'text': '(A)福氣豬', 'img': ''},
                'B': {'text': '(B)溫柔兔', 'img': ''},
                'C': {'text': '(C)7609', 'img': ''},
                'D': {'text': '(D)30944', 'img': ''}
            }, 'isImage': 'Q'},
        4: {
            'Q': {'text': '投擲一顆公正的六面骰子，下列敘述何者正確？', 'img': ''},
            'Option': {
                'A': {'text': '(A)每投擲6次，就會有一次出現6點', 'img': ''},
                'B': {'text': '(B)投擲10次，連續出現6點是不可能的', 'img': ''},
                'C': {'text': '(C)投擲300次，出現6點的次數可能超\n   過65次', 'img': ''},
                'D': {'text': '(D)投擲66000次後的結果，每個點數出\n   現的次數必定相同', 'img': ''}
            }, 'isImage': ''},
        5: {
            'Q': {'text': '', 'img': ''},
            'Option': {
                'A': {'text': '', 'img': ''},
                'B': {'text': '', 'img': ''},
                'C': {'text': '', 'img': ''},
                'D': {'text': '', 'img': ''}
            }, 'isImage': ''},
        6: {
            'Q': {'text': '', 'img': ''},
            'Option': {
                'A': {'text': '', 'img': ''},
                'B': {'text': '', 'img': ''},
                'C': {'text': '', 'img': ''},
                'D': {'text': '', 'img': ''}
            }, 'isImage': ''},
        7: {
            'Q': {'text': '', 'img': ''},
            'Option': {
                'A': {'text': '', 'img': ''},
                'B': {'text': '', 'img': ''},
                'C': {'text': '', 'img': ''},
                'D': {'text': '', 'img': ''}
            }, 'isImage': ''},
        8: {
            'Q': {'text': '', 'img': ''},
            'Option': {
                'A': {'text': '', 'img': ''},
                'B': {'text': '', 'img': ''},
                'C': {'text': '', 'img': ''},
                'D': {'text': '', 'img': ''}
            }, 'isImage': ''},
        9: {
            'Q': {'text': '', 'img': ''},
            'Option': {
                'A': {'text': '', 'img': ''},
                'B': {'text': '', 'img': ''},
                'C': {'text': '', 'img': ''},
                'D': {'text': '', 'img': ''}
            }, 'isImage': ''},
        10: {
            'Q': {'text': '', 'img': ''},
            'Option': {
                'A': {'text': '', 'img': ''},
                'B': {'text': '', 'img': ''},
                'C': {'text': '', 'img': ''},
                'D': {'text': '', 'img': ''}
            }, 'isImage': ''},
        11: {
            'Q': {'text': '', 'img': ''},
            'Option': {
                'A': {'text': '', 'img': ''},
                'B': {'text': '', 'img': ''},
                'C': {'text': '', 'img': ''},
                'D': {'text': '', 'img': ''}
            }, 'isImage': ''},
        12: {
            'Q': {'text': '', 'img': ''},
            'Option': {
                'A': {'text': '', 'img': ''},
                'B': {'text': '', 'img': ''},
                'C': {'text': '', 'img': ''},
                'D': {'text': '', 'img': ''}
            }, 'isImage': ''},
        13: {
            'Q': {'text': '', 'img': ''},
            'Option': {
                'A': {'text': '', 'img': ''},
                'B': {'text': '', 'img': ''},
                'C': {'text': '', 'img': ''},
                'D': {'text': '', 'img': ''}
            }, 'isImage': ''},
        14: {'Q': {'text': '', 'img': ''}, 'Option': {'A': {'text': '', 'img': ''}, 'B': {'text': '', 'img': ''}, 'C': {'text': '', 'img': ''}, 'D': {'text': '', 'img': ''}}, 'isImage': ''}, 15: {'Q': {'text': '', 'img': ''}, 'Option': {'A': {'text': '', 'img': ''}, 'B': {'text': '', 'img': ''}, 'C': {'text': '', 'img': ''}, 'D': {'text': '', 'img': ''}}, 'isImage': ''}, 16: {'Q': {'text': '', 'img': ''}, 'Option': {'A': {'text': '', 'img': ''}, 'B': {'text': '', 'img': ''}, 'C': {'text': '', 'img': ''}, 'D': {'text': '', 'img': ''}}, 'isImage': ''}, 17: {'Q': {'text': '', 'img': ''}, 'Option': {'A': {'text': '', 'img': ''}, 'B': {'text': '', 'img': ''}, 'C': {'text': '', 'img': ''}, 'D': {'text': '', 'img': ''}}, 'isImage': ''}, 18: {'Q': {'text': '', 'img': ''}, 'Option': {'A': {'text': '', 'img': ''}, 'B': {'text': '', 'img': ''}, 'C': {'text': '', 'img': ''}, 'D': {'text': '', 'img': ''}}, 'isImage': ''}, 19: {'Q': {'text': '', 'img': ''}, 'Option': {'A': {'text': '', 'img': ''}, 'B': {'text': '', 'img': ''}, 'C': {'text': '', 'img': ''}, 'D': {'text': '', 'img': ''}}, 'isImage': ''}, 20: {'Q': {'text': '', 'img': ''}, 'Option': {'A': {'text': '', 'img': ''}, 'B': {'text': '', 'img': ''}, 'C': {'text': '', 'img': ''}, 'D': {'text': '', 'img': ''}}, 'isImage': ''}, 21: {'Q': {'text': '', 'img': ''}, 'Option': {'A': {'text': '', 'img': ''}, 'B': {'text': '', 'img': ''}, 'C': {'text': '', 'img': ''}, 'D': {'text': '', 'img': ''}}, 'isImage': ''}, 22: {'Q': {'text': '', 'img': ''}, 'Option': {'A': {'text': '', 'img': ''}, 'B': {'text': '', 'img': ''}, 'C': {'text': '', 'img': ''}, 'D': {'text': '', 'img': ''}}, 'isImage': ''}, 23: {'Q': {'text': '', 'img': ''}, 'Option': {'A': {'text': '', 'img': ''}, 'B': {'text': '', 'img': ''}, 'C': {'text': '', 'img': ''}, 'D': {'text': '', 'img': ''}}, 'isImage': ''}, 24: {'Q': {'text': '', 'img': ''}, 'Option': {'A': {'text': '', 'img': ''}, 'B': {'text': '', 'img': ''}, 'C': {'text': '', 'img': ''}, 'D': {'text': '', 'img': ''}}, 'isImage': ''}, 25: {'Q': {'text': '', 'img': ''}, 'Option': {'A': {'text': '', 'img': ''}, 'B': {'text': '', 'img': ''}, 'C': {'text': '', 'img': ''}, 'D': {'text': '', 'img': ''}}, 'isImage': ''}, 26: {'Q': {'text': '', 'img': ''}, 'Option': {'A': {'text': '', 'img': ''}, 'B': {'text': '', 'img': ''}, 'C': {'text': '', 'img': ''}, 'D': {'text': '', 'img': ''}}, 'isImage': ''}}

    return question


def year111():
    pass


def year110():
    pass


def year109():
    pass


def year108_2():
    pass


def year108_1():
    pass


def year106():
    pass


def year105():
    pass


def year104():
    pass


def year103():
    pass


# print(create_template(26))
YEARS = [
    year112(), year111(), year110(), year109(), year108_2(),
    year108_1(), year106(), year105(), year104(), year103()
]
