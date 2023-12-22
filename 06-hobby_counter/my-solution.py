#!/usr/bin/env python3

from collections import Counter

people = [
    {"name": "Reuven", "age": 47, "hobbies": ["Python", "cooking", "reading"]},
    {"name": "Atara", "age": 16, "hobbies": ["horses", "cooking", "art"]},
    {"name": "Shikma", "age": 14, "hobbies": ["Python", "piano", "cooking"]},
    {"name": "Amotz", "age": 11, "hobbies": ["biking", "cooking"]},
]


class HobbyCounter:
    def __init__(self, data):
        self._data = data
        self._hobby_counts = Counter([k for i in self._data
                                        for k in i["hobbies"]])

    def avg_age_under_25(self):
        ages = [i["age"] for i in self._data if i["age"] < 25]
        return sum(ages) / len(ages)

    def diff_hobbies(self):
        return list(self._hobby_counts)

    def hobby_count(self):
        return "\n".join([f"{k}={v}" for k, v in self._hobby_counts.items()])

    def most_common_hobby_3(self):
        return "\n".join([f"{h}={c}"
                          for h, c in self._hobby_counts.most_common(3)])

    def most_common_hobby_3_more2(self):
        c = Counter(
            [k for i in self._data if len(i["hobbies"]) >= 2
               for k in i["hobbies"]]
        ).most_common(3)
        return "\n".join([f"{i}={k}" for i, k in c])


def main():
    hc = HobbyCounter(people)

    print("\nAverage age unde 25:", hc.avg_age_under_25())
    print("\nUnique hobbies:", hc.diff_hobbies())
    print("\nHobby count:")
    print(hc.hobby_count())
    print("\nThree most common hobbies:")
    print(hc.most_common_hobby_3())
    print("\nThree most common hobbies for those with 2 or more:")
    print(hc.most_common_hobby_3_more2())

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
