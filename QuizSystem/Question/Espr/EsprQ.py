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
            'Q': {'text': '詐騙集團以精心編製的 SOP 手冊教導新成員詐騙技巧，成效卓著。根據以上描述，這樣的教學活動明顯牴觸哪一項教育的規準？', 'img': ''},
            'Option': {
                'A': {'text': '(A)合認知性', 'img': ''},
                'B': {'text': '(B)合價值性', 'img': ''},
                'C': {'text': '(C)合自願性', 'img': ''},
                'D': {'text': '(D)合意向性', 'img': ''}
            },
            'isImage': ''
        },
        2: {
            'Q': {'text': '假新聞經由社會知名人士傳述時，易使民眾不假思索的接受與散播，此現象凸顯媒體識讀教育的重要。這種「訴諸人身」、「因人而信」的傾向，顯示人在認知上容易受到哪一種力量的影響？', 'img': ''},
            'Option': {
                'A': {'text': '(A)權威', 'img': ''},
                'B': {'text': '(B)理性', 'img': ''},
                'C': {'text': '(C)感官', 'img': ''},
                'D': {'text': '(D)天啟', 'img': ''}
            },
            'isImage': ''
        },
        3: {
            'Q': {'text': '下列敘述何者不符合弗雷勒(P.Freire)對話式教學的意涵？', 'img': ''},
            'Option': {
                'A': {'text': '(A)學生可以同時是教學者，教師可以同\n   時是學習者', 'img': ''},
                'B': {'text': '(B)對話式教學的目的之一，在於保持教\n   學價值中立', 'img': ''},
                'C': {'text': '(C)師生間採取非宰制的對待他人，以溝\n   通代替對立', 'img': ''},
                'D': {'text': '(D)教師避免囤積式的教學，以啟發學生\n   的批判能力', 'img': ''}
            },
            'isImage': ''
        },
        4: {
            'Q': {'text': '小華最近沈迷於手機遊戲，熬夜的結果導致每天賴床，家長必須三催四請，才不甘願的到校上課。家長無奈之餘，只好向導師請益。正巧小華的導師推崇盧梭(J.-J.Rousseau)的教育主張，導師比較可能對家長提出哪一項建議？', 'img': ''},
            'Option': {
                'A': {'text': '(A)幫小華報名多種才藝課，轉移小華對\n   手機遊戲的興趣', 'img': ''},
                'B': {'text': '(B)沒收小華的手機，直到小華戒掉熬夜\n   玩手機遊戲為止', 'img': ''},
                'C': {'text': '(C)與小華約法三章，明訂每天讀書及玩\n   手機遊戲的時間', 'img': ''},
                'D': {'text': '(D)不再叫小華起床，讓小華上學遲到，\n   受到應有的懲罰', 'img': ''}
            },
            'isImage': ''
        },
        5: {
            'Q': {'text': '為了讓學生了解紅樹林的生態與生長環境，王老師帶領學生前往嘉義縣鰲鼓溼地進行觀察與體驗。王老師的教學規劃最接近下列哪一種教育理念？', 'img': ''},
            'Option': {
                'A': {'text': '(A)理性主義', 'img': ''},
                'B': {'text': '(B)自由主義', 'img': ''},
                'C': {'text': '(C)經驗主義', 'img': ''},
                'D': {'text': '(D)觀念主義', 'img': ''}
            },
            'isImage': ''
        },
        6: {
            'Q': {'text': '《漢娜．鄂蘭：思想的行動》紀錄片中的「平庸之惡(The Banality of Evil)」意指人們面對不公義的狀況時，缺乏獨立思考及批判能力而任人擺布。李老師深受啟發，開始關注教育現場各項措施的合理性，並提出建言。下列教育現場的現象，何者最符合鄂蘭所述的「平庸之惡」？', 'img': ''},
            'Option': {
                'A': {'text': '(A)陽奉陰違的應付', 'img': ''},
                'B': {'text': '(B)盲目的順從體制', 'img': ''},
                'C': {'text': '(C)不經思索的反對', 'img': ''},
                'D': {'text': '(D)違法的濫用處罰', 'img': ''}
            },
            'isImage': ''
        },
        7: {
            'Q': {'text': '稻米學校以「節氣」為核心，發展跨領域課程，例如：「驚蟄」時節，讓學生學習此時令之大氣變化、動植物生長、當季飲食、合乎時節的作息與文化活動。該課程最符合下列哪一種哲學理念？', 'img': ''},
            'Option': {
                'A': {'text': '(A)道法自然', 'img': ''},
                'B': {'text': '(B)道德法則', 'img': ''},
                'C': {'text': '(C)兼愛非攻', 'img': ''},
                'D': {'text': '(D)理想世界', 'img': ''}
            },
            'isImage': ''
        },
        8: {
            'Q': {'text': '張老師利用日本動畫《進擊的巨人》中阿爾敏的臺詞：「堅信待在城牆內就能永遠安心的想法是有問題的，就算城牆 100 年來都沒有被摧毀，也無法保證未來不會被摧毀。」引導學生討論經驗與知識之關聯。上述臺詞反映的知識觀，與下列哪一位學者的理論最相關？', 'img': ''},
            'Option': {
                'A': {'text': '(A)培根(F.Bacon)—\n   知識即力量', 'img': ''},
                'B': {'text': '(B)傅柯(M.Foucault)—\n   知識即權力', 'img': ''},
                'C': {'text': '(C)波普(K.Popper)—\n   知識的可否證性', 'img': ''},
                'D': {'text': '(D)李歐塔(J.-F.Lyotard)—\n   知識的操作性', 'img': ''}
            },
            'isImage': ''
        },
        9: {
            'Q': {'text': '在網路化時代，人們可以隨時透過各種網路平台學習知識技能、交換資訊及結識學習夥伴。這樣的情形較接近下列哪一部教育著作的主張？', 'img': ''},
            'Option': {
                'A': {'text': '(A)伊利希(I. Illich)的\n   《非學校化社會》', 'img': ''},
                'B': {'text': '(B)格拉塞(W.Glasser)的\n   《沒有失敗的學校》', 'img': ''},
                'C': {'text': '(C)康茲(G.S.Counts)的\n   《學校敢勇於建立新的社會秩序嗎？》', 'img': ''},
                'D': {'text': '(D)赫西(E.D. Hirsch)的《我們所需要的\n   學校以及為何我們沒有這些學校》', 'img': ''}
            },
            'isImage': ''
        },
        10: {
            'Q': {'text': '某校的「學生法庭」是具有民主教育意義的「教育庭」，由學生自己擔任法庭成員，處理校內學生的爭執事件，讓學生學習自主、負責、權利、義務、對話與溝通。學生法庭的設立，最符合下列哪一位思想家的哲學觀點？', 'img': ''},
            'Option': {
                'A': {'text': '(A)柏拉圖(Plato)', 'img': ''},
                'B': {'text': '(B)尼爾(A.Neill)', 'img': ''},
                'C': {'text': '(C)布魯姆(B.Bloom)', 'img': ''},
                'D': {'text': '(D)笛卡兒(R.Descartes)', 'img': ''}
            },
            'isImage': ''
        },
        11: {
            'Q': {'text': '教師的言行易對學生發揮潛在的影響力，教師不僅需要肩負德育職責，且自身需要敦品，這種主張著眼於教師的哪一種權威？', 'img': ''},
            'Option': {
                'A': {'text': '(A)行政法理權威', 'img': ''},
                'B': {'text': '(B)學術認知權威', 'img': ''},
                'C': {'text': '(C)傳統習俗權威', 'img': ''},
                'D': {'text': '(D)道德涵養權威', 'img': ''}
            },
            'isImage': ''
        },
        12: {
            'Q': {'text': '教師面對新課綱跨領域的課程設計不免有些疑慮，例如：陳老師認為各學科有不同的知識系統，安排跨領域的課程，勢必會縮減學科內容的授課時間，降低學生的學習成效。陳老師的觀點屬於伯恩斯坦(B.Bernstein)課程論述中哪一種分類與架構？', 'img': ''},
            'Option': {
                'A': {'text': '(A)強分類強架構', 'img': ''},
                'B': {'text': '(B)強分類弱架構', 'img': ''},
                'C': {'text': '(C)弱分類強架構', 'img': ''},
                'D': {'text': '(D)弱分類弱架構', 'img': ''}
            },
            'isImage': ''
        },
        13: {
            'Q': {'text': '原生家庭為勞工階級的孫老師，以自己就是靠讀書向上流動而成為中產階級為例，在課堂中帶領學生了解社會階級與教育的關係。孫老師的信念較符合下列哪一個理論？', 'img': ''},
            'Option': {
                'A': {'text': '(A)階級衝突論', 'img': ''},
                'B': {'text': '(B)結構功能論', 'img': ''},
                'C': {'text': '(C)符號互動論', 'img': ''},
                'D': {'text': '(D)社會重建論', 'img': ''}
            },
            'isImage': ''
        },
        14: {
            'Q': {'text': '小恩時常跟著父母一同到國家音樂廳參加音樂會，或到美術館觀賞畫作，而他最擅長的才藝就是鋼琴演奏及繪畫，還經常代表學校參加各項音樂或繪畫比賽。小恩累積的經驗最符合下列哪一種資本？', 'img': ''},
            'Option': {
                'A': {'text': '(A)經濟資本', 'img': ''},
                'B': {'text': '(B)象徵資本', 'img': ''},
                'C': {'text': '(C)人力資本', 'img': ''},
                'D': {'text': '(D)文化資本', 'img': ''}
            },
            'isImage': ''
        },
        15: {
            'Q': {'text': '王老師是新進教師，校長要求結合她的資訊專長與校長自身的課程領導經驗，帶動全校跨領域的教學風氣，但王老師希望能先專心於班級教學。她的處境可以用下列哪一種概念說明？', 'img': ''},
            'Option': {
                'A': {'text': '(A)角色距離', 'img': ''},
                'B': {'text': '(B)角色衝突', 'img': ''},
                'C': {'text': '(C)角色模糊', 'img': ''},
                'D': {'text': '(D)角色擴散', 'img': ''}
            },
            'isImage': ''
        },
        16: {
            'Q': {'text': '依據《新住民就讀大學辦法》之規定，新住民申請大學入學，各校招生名額採外加百分之二計算。此做法屬於下列哪一種教育概念的實踐？', 'img': ''},
            'Option': {
                'A': {'text': '(A)文化再製', 'img': ''},
                'B': {'text': '(B)文化同化', 'img': ''},
                'C': {'text': '(C)積極性差別待遇', 'img': ''},
                'D': {'text': '(D)補救性教育措施', 'img': ''}
            },
            'isImage': ''
        },
        17: {
            'Q': {'text': '某校學務主任閱讀青少年次文化著作，書中提及勞工階級家庭背景學生的反學校文化，包括崇尚陽剛、輕蔑學術知識與文憑等。該著作最接近哪一位學者的觀點？', 'img': ''},
            'Option': {
                'A': {'text': '(A)艾波(M. Apple)', 'img': ''},
                'B': {'text': '(B)布迪爾(P.Bourdieu)', 'img': ''},
                'C': {'text': '(C)傅柯(M.Foucault)', 'img': ''},
                'D': {'text': '(D)衛里斯(P.Willis)', 'img': ''}
            },
            'isImage': ''
        },
        18: {
            'Q': {'text': '《高級中等學校訂定學生服裝儀容規定之原則》提及，學生的服裝儀容於重要活動應遵守學校統一規定，學校對於違反規定者，得視情節，採取適當且合乎比例原則之輔導或管教措施，並不得加以處罰。實際上，為達班級凝聚之目的，同儕會相互約束統一服儀。上述情境最符合涂爾幹(E.Durkheim)的哪一個理論觀點？', 'img': ''},
            'Option': {
                'A': {'text': '(A)道德規範', 'img': ''},
                'B': {'text': '(B)社會正義', 'img': ''},
                'C': {'text': '(C)權力展演', 'img': ''},
                'D': {'text': '(D)社會認同', 'img': ''}
            },
            'isImage': ''
        },
        19: {
            'Q': {'text': '趙老師認為不是每個人都足以擔任學校或幼兒園的領導者，領導者要能掌控自己的情緒、充滿自信、正直、具備責任感。上述看法較接近下列哪一種領導理論？', 'img': ''},
            'Option': {
                'A': {'text': '(A)行為論', 'img': ''},
                'B': {'text': '(B)權變論', 'img': ''},
                'C': {'text': '(C)情境論', 'img': ''},
                'D': {'text': '(D)特質論', 'img': ''}
            },
            'isImage': ''
        },
        20: {
            'Q': {'text': '某天聽覺障礙的女學生向導師反映，在下課時間，隔壁班的男生經過她身邊時藉機摸她的胸部，讓她感覺非常不舒服。導師立即告知學務處，學校也依規定在 24 小時內向主管機關通報。此乃依循下列哪一種法規進行通報？', 'img': ''},
            'Option': {
                'A': {'text': '(A)性騷擾防治法', 'img': ''},
                'B': {'text': '(B)特殊教育法', 'img': ''},
                'C': {'text': '(C)學生輔導法', 'img': ''},
                'D': {'text': '(D)性別平等教育法', 'img': ''}
            },
            'isImage': ''
        },
        21: {
            'Q': {'text': '依照現行《師資培育法》第 3 條規定，師資生應於參加教師資格考試前，修畢師資職前教育課程，下列哪一種課程未明訂於該法規中？', 'img': ''},
            'Option': {
                'A': {'text': '(A)校訂課程', 'img': ''},
                'B': {'text': '(B)普通課程', 'img': ''},
                'C': {'text': '(C)專門課程', 'img': ''},
                'D': {'text': '(D)教育專業課程', 'img': ''}
            },
            'isImage': ''
        },
        22: {
            'Q': {'text': '某縣(市)政府委託本國自然人，將該縣(市)內偏遠地區公立學校轉型為公辦民營實驗教育學校。上述情形是依據下列哪一種法規辦理？', 'img': ''},
            'Option': {
                'A': {'text': '(A)學校型態實驗教育實施條例', 'img': ''},
                'B': {'text': '(B)偏遠地區學校教育發展條例', 'img': ''},
                'C': {'text': '(C)公立高級中等以下學校委託私人辦理\n   實驗教育條例', 'img': ''},
                'D': {'text': '(D)高級中等以下教育階段非學校型態實\n   驗教育實施條例', 'img': ''}
            },
            'isImage': ''
        },
        23: {
            'Q': {'text': '教育行政的理論模式區分為理性系統、自然系統、開放系統、非均衡系統，下列哪一種理論屬於自然系統模式？', 'img': ''},
            'Option': {
                'A': {'text': '(A)權變理論\n   (contingency theory)', 'img': ''},
                'B': {'text': '(B)科層理論\n   (theory of bureaucracy)', 'img': ''},
                'C': {'text': '(C)人際關係理論\n   (human relations theory)', 'img': ''},
                'D': {'text': '(D)科學管理理論\n   (theory of scientific management)', 'img': ''}
            },
            'isImage': ''
        },
        24: {
            'Q': {'text': '某日學生在教室爭吵打架，導師馬上積極介入且認為已妥善處理，豈料班上的學生紛紛轉學，隨之，社會輿論沸騰，嚴重影響學校聲譽。此一現象最符合混沌理論的哪一種特性？', 'img': ''},
            'Option': {
                'A': {'text': '(A)蝴蝶效應(butterfly effect)', 'img': ''},
                'B': {'text': '(B)奇特吸引子(strange attractor)', 'img': ''},
                'C': {'text': '(C)耗散結構(dissipative structure)', 'img': ''},
                'D': {'text': '(D)回饋機制(feedback mechanism)', 'img': ''}
            },
            'isImage': ''
        },
        25: {
            'Q': {'text': '孫老師認為教師工作深具價值與意義，能夠發揮教育專業，陪伴學生一同成長，與同事、家長和學生維持良好的互動關係，積極投入教學工作，並獲得成就感。他遭遇挫折時，能正向思考，樂觀面對挑戰。孫老師的情形最符合下列哪一種概念？', 'img': ''},
            'Option': {
                'A': {'text': '(A)自我效能\n   (self-efficacy)', 'img': ''},
                'B': {'text': '(B)學術樂觀\n   (academic optimism)', 'img': ''},
                'C': {'text': '(C)幸福感\n   (psychological well-being)', 'img': ''},
                'D': {'text': '(D)組織承諾\n   (organizational commitment)', 'img': ''}
            },
            'isImage': ''
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
    year112(), year111(), year110(), year109(), year108_2(),
    year108_1(), year106(), year105(), year104(), year103(),
    year102(), year101(), year100(), year99(), year98(),
    year97(), year96(), year95(), year94()
]