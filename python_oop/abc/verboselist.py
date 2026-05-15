#!/usr/bin/env python3
"""Module that defines a VerboseList class extending the built-in list"""


class VerboseList(list):
    """Custom list class that prints notifications on modifications"""

    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, x):
        items_count = len(x)
        super().extend(x)
        print(f"Extended the list with [{items_count}] items.")

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        item = self[index]
        print(f"Popped [{item}] to the list.")
        return super().pop(index)
