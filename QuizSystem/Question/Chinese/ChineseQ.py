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
    pass


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
