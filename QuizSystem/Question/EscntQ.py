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
            'Q': {'text': '吳老師鼓勵學生利用課餘時間組成讀書會，共同研讀文學作品。此種學習方式與內容，屬於下列何種課程？', 'img': ''},
            'Option': {
                'A': {'text': '(A)正式課程', 'img': ''},
                'B': {'text': '(B)懸缺課程', 'img': ''},
                'C': {'text': '(C)空無課程', 'img': ''},
                'D': {'text': '(D)非正式課程', 'img': ''}
            },
            'isImage': ''
        },
        2: {
            'Q': {'text': '運用 CIPP 模式實施課程評鑑，其中有關學校課程目標的適切性，屬於下列何種層面的評鑑？', 'img': ''},
            'Option': {
                'A': {'text': '(A)背景評鑑', 'img': ''},
                'B': {'text': '(B)輸入評鑑', 'img': ''},
                'C': {'text': '(C)過程評鑑', 'img': ''},
                'D': {'text': '(D)成果評鑑', 'img': ''}
            },
            'isImage': ''
        },
        3: {
            'Q': {'text': '沈老師編了一份數學成就測驗，發現班上學生在此測驗的得分，與其在該縣市的學習能力檢測之數學表現，在班級排名大致相當。代表此測驗具有下列何種效度？', 'img': ''},
            'Option': {
                'A': {'text': '(A)表面效度', 'img': ''},
                'B': {'text': '(B)內容效度', 'img': ''},
                'C': {'text': '(C)聚斂效度', 'img': ''},
                'D': {'text': '(D)效標關聯效度', 'img': ''}
            },
            'isImage': ''
        },
        4: {
            'Q': {'text': '下列敘述何者較符合課程實施的相互調適觀？', 'img': ''},
            'Option': {
                'A': {'text': '(A)課程實施前，課程設計人員與教師\n   討論後，再進行課程規劃', 'img': ''},
                'B': {'text': '(B)課程實施時，宜因應學校教育的實\n   際情境，再加以彈性調整', 'img': ''},
                'C': {'text': '(C)課程設計人員給予教師明確的說明\n   ，指導教師如何進行教學', 'img': ''},
                'D': {'text': '(D)為確保課程實施品質，課程設計人\n   員彼此間需相互交換意見', 'img': ''}
            },
            'isImage': ''
        },
        5: {
            'Q': {'text': '有關腦力激盪法(brainstorming)，下列敘述何者錯誤？', 'img': ''},
            'Option': {
                'A': {'text': '(A)其功能在於激發跳出框架的思考', 'img': ''},
                'B': {'text': '(B)發散階段時的討論，意見愈多愈好', 'img': ''},
                'C': {'text': '(C)聚斂階段時的討論，不做評價論斷', 'img': ''},
                'D': {'text': '(D)可運用改編、替代等方法得到不同意見', 'img': ''}
            },
            'isImage': ''
        }, 6: {'Q': {'text': '', 'img': ''}, 'Option': {'A': {'text': '', 'img': ''}, 'B': {'text': '', 'img': ''}, 'C': {'text': '', 'img': ''}, 'D': {'text': '', 'img': ''}}, 'isImage': ''}, 7: {'Q': {'text': '', 'img': ''}, 'Option': {'A': {'text': '', 'img': ''}, 'B': {'text': '', 'img': ''}, 'C': {'text': '', 'img': ''}, 'D': {'text': '', 'img': ''}}, 'isImage': ''}, 8: {'Q': {'text': '', 'img': ''}, 'Option': {'A': {'text': '', 'img': ''}, 'B': {'text': '', 'img': ''}, 'C': {'text': '', 'img': ''}, 'D': {'text': '', 'img': ''}}, 'isImage': ''}, 9: {'Q': {'text': '', 'img': ''}, 'Option': {'A': {'text': '', 'img': ''}, 'B': {'text': '', 'img': ''}, 'C': {'text': '', 'img': ''}, 'D': {'text': '', 'img': ''}}, 'isImage': ''}, 10: {'Q': {'text': '', 'img': ''}, 'Option': {'A': {'text': '', 'img': ''}, 'B': {'text': '', 'img': ''}, 'C': {'text': '', 'img': ''}, 'D': {'text': '', 'img': ''}}, 'isImage': ''}, 11: {'Q': {'text': '', 'img': ''}, 'Option': {'A': {'text': '', 'img': ''}, 'B': {'text': '', 'img': ''}, 'C': {'text': '', 'img': ''}, 'D': {'text': '', 'img': ''}}, 'isImage': ''}, 12: {'Q': {'text': '', 'img': ''}, 'Option': {'A': {'text': '', 'img': ''}, 'B': {'text': '', 'img': ''}, 'C': {'text': '', 'img': ''}, 'D': {'text': '', 'img': ''}}, 'isImage': ''}, 13: {'Q': {'text': '', 'img': ''}, 'Option': {'A': {'text': '', 'img': ''}, 'B': {'text': '', 'img': ''}, 'C': {'text': '', 'img': ''}, 'D': {'text': '', 'img': ''}}, 'isImage': ''}, 14: {'Q': {'text': '', 'img': ''}, 'Option': {'A': {'text': '', 'img': ''}, 'B': {'text': '', 'img': ''}, 'C': {'text': '', 'img': ''}, 'D': {'text': '', 'img': ''}}, 'isImage': ''}, 15: {'Q': {'text': '', 'img': ''}, 'Option': {'A': {'text': '', 'img': ''}, 'B': {'text': '', 'img': ''}, 'C': {'text': '', 'img': ''}, 'D': {'text': '', 'img': ''}}, 'isImage': ''}, 16: {'Q': {'text': '', 'img': ''}, 'Option': {'A': {'text': '', 'img': ''}, 'B': {'text': '', 'img': ''}, 'C': {'text': '', 'img': ''}, 'D': {'text': '', 'img': ''}}, 'isImage': ''}, 17: {'Q': {'text': '', 'img': ''}, 'Option': {'A': {'text': '', 'img': ''}, 'B': {'text': '', 'img': ''}, 'C': {'text': '', 'img': ''}, 'D': {'text': '', 'img': ''}}, 'isImage': ''}, 18: {'Q': {'text': '', 'img': ''}, 'Option': {'A': {'text': '', 'img': ''}, 'B': {'text': '', 'img': ''}, 'C': {'text': '', 'img': ''}, 'D': {'text': '', 'img': ''}}, 'isImage': ''}, 19: {'Q': {'text': '', 'img': ''}, 'Option': {'A': {'text': '', 'img': ''}, 'B': {'text': '', 'img': ''}, 'C': {'text': '', 'img': ''}, 'D': {'text': '', 'img': ''}}, 'isImage': ''}, 20: {'Q': {'text': '', 'img': ''}, 'Option': {'A': {'text': '', 'img': ''}, 'B': {'text': '', 'img': ''}, 'C': {'text': '', 'img': ''}, 'D': {'text': '', 'img': ''}}, 'isImage': ''}, 21: {'Q': {'text': '', 'img': ''}, 'Option': {'A': {'text': '', 'img': ''}, 'B': {'text': '', 'img': ''}, 'C': {'text': '', 'img': ''}, 'D': {'text': '', 'img': ''}}, 'isImage': ''}, 22: {'Q': {'text': '', 'img': ''}, 'Option': {'A': {'text': '', 'img': ''}, 'B': {'text': '', 'img': ''}, 'C': {'text': '', 'img': ''}, 'D': {'text': '', 'img': ''}}, 'isImage': ''}, 23: {'Q': {'text': '', 'img': ''}, 'Option': {'A': {'text': '', 'img': ''}, 'B': {'text': '', 'img': ''}, 'C': {'text': '', 'img': ''}, 'D': {'text': '', 'img': ''}}, 'isImage': ''}, 24: {'Q': {'text': '', 'img': ''}, 'Option': {'A': {'text': '', 'img': ''}, 'B': {'text': '', 'img': ''}, 'C': {'text': '', 'img': ''}, 'D': {'text': '', 'img': ''}}, 'isImage': ''}, 25: {'Q': {'text': '', 'img': ''}, 'Option': {'A': {'text': '', 'img': ''}, 'B': {'text': '', 'img': ''}, 'C': {'text': '', 'img': ''}, 'D': {'text': '', 'img': ''}}, 'isImage': ''}}


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


def year102():
    pass


def year101():
    pass


def year100():
    pass


def year99():
    pass


def year98():
    pass


def year97():
    pass


def year96():
    pass


def year95():
    pass


def year94():
    pass


print(create_template(25))

YEARS = [
    year112(), year111(), year110(), year109(), year108_2(),
    year108_1(), year106(), year105(), year104(), year103(),
    year102(), year101(), year100(), year99(), year98(),
    year97(), year96(), year95(), year94()
]
