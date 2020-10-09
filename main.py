from collections import defaultdict
from random import choice
from typing import List, Dict, Tuple, Optional, Union

_Dataset = Tuple[Dict[str, List[str]], List[str]]


def _process_file(uri: str) -> List[str]:
    pass


def _build_map_and_initial_words(words: List[str]) -> _Dataset:
    initials = list(filter(lambda x: x[0].isupper(), words))
    mapping = defaultdict(list)

    for idx in range(len(words)):
        current = words[idx]

        if len(words) == idx + 1:
            break

        the_next = words[idx + 1]
        mapping[current.lower()].append(the_next)
        pass

    return mapping, initials


_max_words: int = 20
_min_words: int = 5
_terminators: List[str] = [".", "!", "?"]


def _ensure_has_terminator(sentence: List[str]) -> List[str]:
    if sentence[-1] not in _terminators:
        sentence[-1] = sentence[-1] + _terminators[0]

    return sentence


def _visit(mapping: Dict[str, List[str]], promoted_word: str, sentence: List[str]) -> Tuple[List[str], bool]:
    copy = list(sentence)
    copy.append(promoted_word)
    possible_next_words = mapping[promoted_word.lower()]

    if promoted_word[-1] in _terminators:
        return copy, len(sentence) >= _min_words

    if len(copy) == _max_words:
        return _ensure_has_terminator(copy), True

    if not possible_next_words:
        return _ensure_has_terminator(copy), len(sentence) >= _min_words

    next_word = choice(possible_next_words)
    new, suc = _visit(mapping, next_word, copy)

    if suc:
        return new, suc
    else:
        return _visit(mapping, copy[-2], copy[:-1])


def _generate(n: int, dataset: _Dataset) -> str:
    mapping, initials = dataset
    sentences = []

    for _ in range(n):
        ls, success = _visit(mapping, choice(initials), [])

        if not success:
            print(ls)
            raise NotImplementedError()

        sentences.append(ls)

    return " ".join(map(lambda x: " ".join(x), sentences))


_ds = _build_map_and_initial_words(["Кошка", "съела", "колбасу.", "Кошка", "играет", "с", "кошкой"])
print(_generate(2, _ds))
