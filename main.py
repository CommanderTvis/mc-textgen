from collections import defaultdict
from typing import List, Dict, Tuple

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
        mapping[current].append(the_next)
        pass

    return mapping, initials


def _generate(n: int, dataset: _Dataset) -> str:
    pass


print(_build_map_and_initial_words(["Кошка", "съела", "колбасу.", "Кошка", "играет", "с", "кошкой"]))
