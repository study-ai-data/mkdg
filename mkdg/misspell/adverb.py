"""
부사
"""
from mkdg.utils.chgword import chg_word


def load_adverb():
    from mkdg.utils.getmisspell import misspell_single_data
    """
    Load adverb data

    Returns: adverb dictionary, alternative list
    """
    adverb = misspell_single_data("adverb")
    alternative = {

    }
    return adverb, alternative


if __name__ == "__main__":
    test = [
        "오늘 코로나에 걸린 사람이 줄었습니다.",
        "많은 연구원들이 좋아할 것 입니다.",
        "병원 관계자들 또한 좋아할 것입니다."
    ]

    print("Origin: ", test)
    adverb, alt = load_adverb()
    result = chg_word(test, adverb)  # , alt)
    print("Result: ", result)
