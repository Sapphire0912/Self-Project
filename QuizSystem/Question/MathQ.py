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


# print(create_template(25))
YEARS = [
    year112(), year111(), year110(), year109(), year108_2(),
    year108_1(), year106(), year105(), year104(), year103()
]
