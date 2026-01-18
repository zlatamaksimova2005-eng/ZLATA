from typing import List, Any

def index(lst: List[Any], value: Any) -> List[int]:

    indices = [i for i, x in enumerate(lst) if x == value]
    if not indices:
        raise ValueError(f"{value} is not in list")
    return indices

if __name__ == '__main__':
    list_items = [1, 2, "3", 1]
    print(index(list_items, 1) == [0, 3])  # True
