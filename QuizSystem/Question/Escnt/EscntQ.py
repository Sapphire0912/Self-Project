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
            'Q': {'text': '下列大腦區域何者與情緒控制較有關係？', 'img': ''},
            'Option': {
                'A': {'text': '(A)額葉', 'img': ''},
                'B': {'text': '(B)頂葉', 'img': ''},
                'C': {'text': '(C)枕葉', 'img': ''},
                'D': {'text': '(D)顳葉', 'img': ''}
            },
            "isImage": ""
        },
        2: {
            'Q': {'text': '下列何者是指「透過各種社會互動經驗，人們逐漸形成一組對自己優點、缺點、能力、態度、與價值等的整體性知覺」？', 'img': ''},
            'Option': {
                'A': {'text': '(A)自我概念 (self-concept)', 'img': ''},
                'B': {'text': '(B)自我效能 (self-efficacy)', 'img': ''},
                'C': {'text': '(C)自我監控 (self-monitoring)', 'img': ''},
                'D': {'text': '(D)自我管理 (self-management)', 'img': ''}
            },
            "isImage": ""
        },
        3: {
            'Q': {'text': '二年級的小華被診斷為「注意力缺陷過動症」(ADHD) 的「注意力不集中型」(inattention)。根據診斷，下列何者較不可能是小華會出現的臨床症狀？', 'img': ''},
            'Option': {
                'A': {'text': '(A)經常無法仔細注意細節', 'img': ''},
                'B': {'text': '(B)在日常生活中常忘東忘西', 'img': ''},
                'C': {'text': '(C)經常無法遵循指示完成功課', 'img': ''},
                'D': {'text': '(D)經常在問題還沒說完時衝口說出答案', 'img': ''}
            },
            "isImage": ""
        },
        4: {
            'Q': {'text': '老師在教「長度」概念時，要學生在三分鐘內想出十種測量長度的方法，小雄想到的比其他人多。小雄在創造力的哪一個層面表現突出？', 'img': ''},
            'Option': {
                'A': {'text': '(A)流暢力', 'img': ''},
                'B': {'text': '(B)獨創力', 'img': ''},
                'C': {'text': '(C)精進力', 'img': ''},
                'D': {'text': '(D)變通力', 'img': ''}
            },
            "isImage": ""
        },
        5: {
            'Q': {'text': '小慧全家從北部搬到南部，因而轉學到新學校。他很快就熟悉學校周遭的環境，能跟老師及同學有不錯的互動，也能掌握導師的期許和班規。依據史坦伯格 (R.Sternberg)的智力三元論，大智展現了哪一種智力？', 'img': ''},
            'Option': {
                'A': {'text': '(A)情境智力\n   (contextual intelligence)', 'img': ''},
                'B': {'text': '(B)經驗智力\n   (experiential intelligence)', 'img': ''},
                'C': {'text': '(C)社交智力\n   (interpersonal intelligence)', 'img': ''},
                'D': {'text': '(D)組合智力\n   (componential intelligence)', 'img': ''}
            },
            "isImage": ""
        },
        6: {
            'Q': {'text': '下列哪些是個人中心學派治療關係的要件？\n甲、同情心\n乙、真誠一致\n丙、積極鼓勵\n丁、無條件積極關注', 'img': ''},
            'Option': {
                'A': {'text': '(A)甲乙', 'img': ''},
                'B': {'text': '(B)甲丁', 'img': ''},
                'C': {'text': '(C)乙丙', 'img': ''},
                'D': {'text': '(D)乙丁', 'img': ''}
            },
            "isImage": ""
        },
        7: {
            'Q': {'text': '下列何者不是小團體初期階段的重要目標？', 'img': ''},
            'Option': {
                'A': {'text': '(A)確立成員須共同遵守的規範', 'img': ''},
                'B': {'text': '(B)協助成員感到自己是團體的一份子', 'img': ''},
                'C': {'text': '(C)協助成員深入了解、掌握與發展自我', 'img': ''},
                'D': {'text': '(D)幫助成員建立自己參與團隊的個人目\n   標', 'img': ''}
            },
            "isImage": ""
        },
        8: {
            'Q': {'text': '學生跟老師說：「每次分組，小豪都拒絕跟我同組，他是不是在排擠我？｣下列老師的回答，何者是較具有同理心的回應？', 'img': ''},
            'Option': {
                'A': {'text': '(A)「是他自己有問題，你不要理他。｣', 'img': ''},
                'B': {'text': '(B)「你很難過，覺得自己不被接納。｣', 'img': ''},
                'C': {'text': '(C)「別這麼說，事情應該不是這樣。｣', 'img': ''},
                'D': {'text': '(D)「你這樣想，對你一點好處都沒有。｣', 'img': ''}
            },
            "isImage": ""
        },
        9: {
            'Q': {'text': '下列哪一個學派主張將諮商的目標放在具體的問題行為上，以可觀察、可測量的行為來敘述諮商的目標，且特別強調提出具體、明確的解決步驟？', 'img': ''},
            'Option': {
                'A': {'text': '(A)心理分析學派', 'img': ''},
                'B': {'text': '(B)認知治療學派', 'img': ''},
                'C': {'text': '(C)行為治療學派', 'img': ''},
                'D': {'text': '(D)個人中心學派', 'img': ''}
            },
            "isImage": ""
        },
        10: {
            'Q': {'text': '小英這次閱讀測驗考了 65 分，遠低於全班的平均成績，所以林老師讓他放學後留下接受課後輔導。老師使用交互教學法 (reciprocal teaching) 教小英摘要與提問等閱讀策略，並逐漸將責任轉移給小英。小英在一週後重寫相同測驗的複本，得到了85分。根據以上的情境，下列敘述何者錯誤？', 'img': ''},
            'Option': {
                'A': {'text': '(A)老師的作法符合維高思基\n   (L.Vygotsky)的社會文化論', 'img': ''},
                'B': {'text': '(B)老師提供的鷹架(scaffolding)有助於\n   提升小英的閱讀表現', 'img': ''},
                'C': {'text': '(C)85分代表小英的近側發展區\n   (zoneofproximal development,ZPD)', 'img': ''},
                'D': {'text': '(D)65分可視為小英近側發展區\n   (zoneofproximal development,ZPD)\n   的下限', 'img': ''}
            },
            "isImage": ""
        },
        11: {
            'Q': {'text': '老師給小元看兩個盒子，一個盒子有泡芙圖案，另一個則有糖果圖案。老師在小元面前把泡芙放入糖果圖案的盒子。這時，老師問小元：「等一下小華進來後，會到哪個盒子找泡芙吃？」老師主要想測試小元的哪一種能力？', 'img': ''},
            'Option': {
                'A': {'text': '(A)自我調節 (self-regulating)', 'img': ''},
                'B': {'text': '(B)道德推理 (moral reasoning)', 'img': ''},
                'C': {'text': '(C)語言組成 (language making)', 'img': ''},
                'D': {'text': '(D)觀點取替 (perspective taking)', 'img': ''}
            },
            "isImage": ""
        },
        12: {
            'Q': {'text': '下列敘述何者不符合柯柏格 (L.Kohlberg) 道德發展階段論的觀點？', 'img': ''},
            'Option': {
                'A': {'text': '(A)發展階段的前後順序會因不同文化而\n   異', 'img': ''},
                'B': {'text': '(B)道德發展可依俗例(convention)分為\n   三期(levels)', 'img': ''},
                'C': {'text': '(C)發展階段所提供的道德思考架構，可\n   應用至各種情境', 'img': ''},
                'D': {'text': '(D)除了第一階段之外，各階段的發展都建\n   立在前一階段的推理之上', 'img': ''}
            },
            "isImage": ""
        },
        13: {
            'Q': {'text': '教師應依據學生不同的需求與情境來安排座位。下列何種座位安排方式較為不妥？', 'img': ''},
            'Option': {
                'A': {'text': '(A)為增加學生互動機會與提升教學效果\n   ，將桌椅排成ㄇ字型', 'img': ''},
                'B': {'text': '(B)為激勵學生更加精進，按照成績高低\n   依序安排全班的座位', 'img': ''},
                'C': {'text': '(C)運用匿名方式了解學生的人際關係，\n   作為安排座位的參考', 'img': ''},
                'D': {'text': '(D)為維護其他同學的受教權，把嚴重違\n   反紀律的學生暫時安排在教室角落', 'img': ''}
            },
            "isImage": ""
        },
        14: {
            'Q': {'text': '根據行為學派的理論，老師輔導學生從事學習時，運用哪種增強方式較有效？', 'img': ''},
            'Option': {
                'A': {'text': '(A)當學生進步時，提高增強的頻率', 'img': ''},
                'B': {'text': '(B)整個過程皆應使用立即與持續的增強', 'img': ''},
                'C': {'text': '(C)一開始先持續性增強，之後再間歇性\n   增強', 'img': ''},
                'D': {'text': '(D)一開始先間歇性增強，之後再持續性\n   增強', 'img': ''}
            },
            "isImage": ""
        },
        15: {
            'Q': {'text': '老師在前兩週的數學課教了最大公因數的概念及算法，小柏做了很多練習才終於學會。這週開始，老師開始教最小公倍數的概念及算法，結果小柏覺得很混淆，原本之前已經學會的最大公因數算法反而不會了。下列心理歷程何者較能解釋前述現象？', 'img': ''},
            'Option': {
                'A': {'text': '(A)順攝抑制\n   (proactive inhibition)', 'img': ''},
                'B': {'text': '(B)順攝助長\n   (proactive facilitation)', 'img': ''},
                'C': {'text': '(C)倒攝抑制\n   (retroactive inhibition)', 'img': ''},
                'D': {'text': '(D)倒攝助長\n   (retroactive facilitation)', 'img': ''}
            },
            "isImage": ""
        },
        16: {
            'Q': {'text': '小志要參加校外教學，前一天晚上就買好隔日的午餐（御飯糰加飲料）放在冰箱內。為了怕忘記帶午餐，特別在門把上夾了一張紙條，上面畫了一個三角形提醒自己。小志使用的是下列哪一項記憶策略？', 'img': ''},
            'Option': {
                'A': {'text': '(A)精緻化 (elaboration)', 'img': ''},
                'B': {'text': '(B)意元集組(chunking)', 'img': ''},
                'C': {'text': '(C)選擇性注意(selectiveattention)', 'img': ''},
                'D': {'text': '(D)外在記憶輔助(external memoryaids)', 'img': ''}
            },
            "isImage": ""
        },
        17: {
            'Q': {'text': '有關特定學習障礙學童的陳述，下列何者正確？', 'img': ''},
            'Option': {
                'A': {'text': '(A)學習障礙不會伴隨知覺動作障礙', 'img': ''},
                'B': {'text': '(B)學習障礙不是由智力影響而造成', 'img': ''},
                'C': {'text': '(C)學習障礙主要是由心理社會不利因素\n   所造成', 'img': ''},
                'D': {'text': '(D)學習障礙在臺灣的盛行率介於10%至\n   20%之間', 'img': ''}
            },
            "isImage": ""
        },
        18: {
            'Q': {'text': '小揚在教室奔跑時不小心把同學的水杯打翻了，以下老師的作法何者符合「邏輯後果」的管教原則？', 'img': ''},
            'Option': {
                'A': {'text': '(A)要求小揚寫班規一遍', 'img': ''},
                'B': {'text': '(B)要求小揚上台唱歌娛樂同學', 'img': ''},
                'C': {'text': '(C)要求小揚反省並檢討自己的錯誤之處', 'img': ''},
                'D': {'text': '(D)要求小揚把地板拖乾並且向同學道歉', 'img': ''}
            },
            "isImage": ""
        },
        19: {
            'Q': {'text': '小江今年六年級，第一次段考成績不理想，讓他感到失望。小江可以採取下列哪種問題中心因應策略 (problem-centeredcoping)？', 'img': ''},
            'Option': {
                'A': {'text': '(A)透過運動放鬆心情', 'img': ''},
                'B': {'text': '(B)鼓勵自己把握下次的機會', 'img': ''},
                'C': {'text': '(C)向老師或同學請教學習方法', 'img': ''},
                'D': {'text': '(D)告訴自己想開一點，分數不是最重要\n   的事', 'img': ''}
            },
            "isImage": ""
        },
        20: {
            'Q': {'text': '媽媽在小明面前向他的朋友說：「小明這次段考成績不理想，根本就是不夠用功！」回家後，小明跟媽媽說：「考試成績不理想，並不是我不認真，數學本來就很難。每次你都在你的朋友面前說我表現不好，一點都不考慮我的感受，讓我心裡很不舒服。」小明把成績不理想做何種歸因？', 'img': ''},
            'Option': {
                'A': {'text': '(A)外在而穩定', 'img': ''},
                'B': {'text': '(B)內在而穩定', 'img': ''},
                'C': {'text': '(C)外在而不穩定', 'img': ''},
                'D': {'text': '(D)內在而不穩定', 'img': ''}
            },
            "isImage": ""
        },
        21: {
            'Q': {'text': '輔導教師協助來談者明確地表達個人的感覺、經驗與行為，聚焦於來談者自己的故事，而非漫無目標的談話。這屬於何種諮商技術？', 'img': ''},
            'Option': {
                'A': {'text': '(A)澄清(clarification)', 'img': ''},
                'B': {'text': '(B)面質(confrontation)', 'img': ''},
                'C': {'text': '(C)摘要(summarization)', 'img': ''},
                'D': {'text': '(D)具體化(concreteness)', 'img': ''}
            },
            "isImage": ""
        },
        22: {
            'Q': {'text': '小家有高度的數學考試焦慮。李老師試著讓他想像會激起焦慮的考試情境，從引發輕微焦慮的情境直到引發劇烈焦慮的情境。同時引導他面對每一個情境學習放鬆、舒緩壓力，至終解除焦慮。李老師採用的是哪一種治療方法？', 'img': ''},
            'Option': {
                'A': {'text': '(A)現場暴露法', 'img': ''},
                'B': {'text': '(B)系統減敏感法', 'img': ''},
                'C': {'text': '(C)社會技巧訓練', 'img': ''},
                'D': {'text': '(D)自我肯定訓練', 'img': ''}
            },
            "isImage": ""
        },
        23: {
            'Q': {'text': '高老師班上的國輝時常會與同學發生衝突，若同學不小心碰到他或開他玩笑，他就會攻擊同學或用髒話罵同學。高老師問國輝為何如此，國輝回答：「誰叫他們要故意弄我？」根據以上敘述，國輝的適應問題較可能歸類為下列何者？', 'img': ''},
            'Option': {
                'A': {'text': '(A)學業適應問題', 'img': ''},
                'B': {'text': '(B)內向性行為問題', 'img': ''},
                'C': {'text': '(C)外向性行為問題', 'img': ''},
                'D': {'text': '(D)創傷後壓力症候群', 'img': ''}
            },
            "isImage": ""
        },
        24: {
            'Q': {'text': '七歲的怡君和媽媽及兩歲的妹妹到餐廳吃飯。用完餐後，媽媽離開座位去櫃台結帳，怡君安慰著妹妹說：「媽媽很快就回來了，不要怕，姊姊在這裡陪妳。」下列何者較能說明怡君安慰妹妹的現象？', 'img': ''},
            'Option': {
                'A': {'text': '(A)怡君能夠清楚意識到自己的情緒', 'img': ''},
                'B': {'text': '(B)怡君對於自己的情緒調節掌握得很好', 'img': ''},
                'C': {'text': '(C)怡君非常遵守文化中情緒表達的規則', 'img': ''},
                'D': {'text': '(D)怡君能根據過去經驗預測並理解妹妹\n   的情緒', 'img': ''}
            },
            "isImage": ""
        },
        25: {
            'Q': {'text': '五年級的小貞和小惠是好朋友，他們常常聊天分享生活點滴。最近小貞的父母發生一些爭吵，小貞和小惠每天談論父母的問題，他們的心情也因此跟著低落下來。此一現象符應下列哪一個概念？', 'img': ''},
            'Option': {
                'A': {'text': '(A)同儕壓力\n   (peerpressure)', 'img': ''},
                'B': {'text': '(B)共同反芻\n   (co-rumination)', 'img': ''},
                'C': {'text': '(C)替代學習\n   (vicarious learning)', 'img': ''},
                'D': {'text': '(D)負增強陷阱\n   (negativereinforcement trap)', 'img': ''}
            },
            "isImage": ""
        }
    }

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


# print(create_template(25))
YEARS = [
    year94(), year95(), year96(), year97(), year98(),
    year99(), year100(), year101(), year102(), year103(),
    year104(), year105(), year106(), year108_1(), year108_2(),
    year109(), year110(), year111(), year112()
]
