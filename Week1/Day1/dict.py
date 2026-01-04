from collections import defaultdict, Counter
from typing import Any, Dict, Iterable, Tuple

# Concise examples and common patterns for Python dicts
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# Dictionary is a built-in data type that stores data in key-value pairs. It is an unordered, mutable, and indexed collection. Each key in a dictionary is unique and maps to a value.
def basics() -> None:
    # creation
    d1 = {"a": 1, "b": 2}
    d2 = dict(x=10, y=20)
    d3 = dict([("k", 99), ("m", 100)])
    print("created:", d1, d2, d3)

    # access
    print("d1['a']:", d1["a"])
    print("get safe:", d1.get("z", "missing"))

    # set and update
    d1["c"] = 3
    d1.update({"a": 11, "d": 4})
    print("after set/update:", d1)

    # remove
    popped = d1.pop("b", None)
    print("popped b:", popped, "remaining:", d1)
    key, val = d1.popitem()  # remove last inserted item (Py3.7+ preserves order)
    print("popitem:", (key, val), "now:", d1)


def iterate_examples(d: Dict[str, Any]) -> None:
    print("keys:", list(d.keys()))
    print("values:", list(d.values()))
    print("items:", list(d.items()))
    # iterate
    for k in d:
        print("key:", k, "value:", d[k])
    # unpack items
    for k, v in d.items():
        print("item:", k, "->", v)


def comprehensions_and_constructors() -> None:
    # comprehension
    squares = {n: n * n for n in range(5)}
    print("squares:", squares)

    # fromkeys: sets same value for given keys
    fk = dict.fromkeys(["a", "b", "c"], 0)
    print("fromkeys:", fk)


def merging_and_copying() -> None:
    a = {"a": 1, "b": 2}
    b = {"b": 20, "c": 3}

    # merge (Python 3.9+: | operator)
    merged = a | b  # b overrides a where keys conflict
    print("merged (|):", merged)

    # update in-place
    a_copy = a.copy()
    a_copy.update(b)
    print("updated in-place:", a_copy)

    # shallow copy vs reference
    ref = a
    ref["a"] = 100
    print("original a changed via ref:", a)


def nested_and_mutability() -> None:
    nested = {"row1": {"x": 1}, "row2": {"y": 2}}
    # shallow copy doesn't copy nested dicts
    c = nested.copy()
    c["row1"]["x"] = 999
    print("nested mutated through shallow copy:", nested)


def useful_patterns() -> None:
    # defaultdict: automatic factory for missing keys
    dd = defaultdict(list)
    dd["cats"].append("whiskers")
    print("defaultdict:", dict(dd))

    # Counter for counting
    cnt = Counter("abracadabra")
    print("most common:", cnt.most_common(3))

    # setdefault: create if missing and return
    d = {}
    d.setdefault("nums", []).append(1)
    print("setdefault:", d)

    # safe removal without KeyError
    removed = d.pop("nope", None)
    print("pop missing safe:", removed)


def keys_require_hashable_types() -> None:
    good = {(1, 2): "tuple key", "s": "string key"}
    try:
        bad = {[1, 2]: "list key"}  # will raise TypeError when executed
    except TypeError:
        print("lists are unhashable and cannot be dict keys")
    print("good keys example:", good)


def main() -> None:
    print("=== basics ===")
    basics()
    print("\n=== iterate ===")
    iterate_examples({"a": 1, "b": 2})
    print("\n=== comprehensions ===")
    comprehensions_and_constructors()
    print("\n=== merge/copy ===")
    merging_and_copying()
    print("\n=== nested ===")
    nested_and_mutability()
    print("\n=== useful patterns ===")
    useful_patterns()
    print("\n=== hashable keys ===")
    keys_require_hashable_types()


if __name__ == "__main__":
    main()