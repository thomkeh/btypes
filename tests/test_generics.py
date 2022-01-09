import unittest

from btypes import List, Type


class A:
    ...


class B(A):
    ...


def f(x: List[A]) -> None:
    del x


def g(t: Type[A]) -> None:
    del t


class TestGenerics(unittest.TestCase):
    def test_covariance(self) -> None:
        a: List[A] = [B()]
        f(a)
        g(B)
