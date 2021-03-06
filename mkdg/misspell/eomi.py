"""
어미
"""
from mkdg.utils.chgword import chg_word


def load_eomi():
    from mkdg.utils.getmisspell import misspell_single_data
    """
    Load eomi data

    Returns: eomi dictionary, alternative list
    """
    eomi = misspell_single_data("eomi")
    alternative = {
        "습니다": "니다",
        "는데요": "는데",

    }
    return eomi, alternative


if __name__ == "__main__":
    test = [
        "오늘 코로나에 걸린 사람이 줄었습니다.",
        "많은 연구원들이 좋아할 것 입니다.",
        "병원 관계자들 또한 좋아할 것입니다."
    ]

    print("Origin: ", test)
    eomi, alt = load_eomi()
    result = chg_word(test, eomi, alt)
    print("Result: ", result)
