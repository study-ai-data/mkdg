"""
접속사
"""
from mkdg.utils.chgword import chg_word


def load_conjunction():
    conjunction = {
        "그럼": [
            "그러면", "그럼",
            "글면", "구럼", "그롬", "구롬", "고럼", "글묜",
            "고러면", "구러면", "그로면", "그르면", "그르묜",
        ],
        "그리고": [
            "그리고",
            "글구", "구리구", "구리고", "그리구",
        ],
        "또": [
            "또",
            "또오",
        ],
        "근데": [
            "근데", "그런데",
            "그렁대", "그렁데", "그론데", "그론디", "그런디",
            "긍데", "근디", "긍디",
        ],
        "그래도": [
            "그래도",
            "그래두", "구래도", "구래두",
        ],
        "그래서": [
            "그래서", "따라서",
            "구래서", "그뤠서", "구뤠서",
            "따라숴", "따롸서",
        ],
        "그러니까": [
            "그러니까",
            "구로니까", "구러니까", "그로니까",
        ],
    }

    alternative = {
        "그러면": "그럼",
        "그런데": "근데",
        "따라서": "그래서",
    }

    return conjunction, alternative


if __name__ == "__main__":
    test = [
        "오늘 코로나에 걸린 사람이 줄었습니다.",
        "많은 연구원들이 좋아할 것 입니다.",
        "병원 관계자들 또한 좋아할 것입니다."
    ]

    print("Origin: ", test)
    conjunction, alt = load_conjunction()
    result = chg_word(test, conjunction, alt)
    print("Result: ", result)
