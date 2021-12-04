import unittest
from typing import TypeGuard, TypeVar

from btypes import Any, Int, List, Str, Type

T = TypeVar("T")


def isinstance_elements(lst: List[Any], t: Type[T]) -> TypeGuard[List[T]]:
    """Check whether all elements in `lst` are of type `t`."""
    return all(isinstance(e, t) for e in lst)


class TestIsinstance(unittest.TestCase):
    def test_str(self):
        self.assertIsInstance("foo", Str)

    def test_list(self):
        lst = [0, 2, 3, 5, -1]
        self.assertIsInstance(lst, List)
        self.assertTrue(isinstance_elements(lst, Int))
