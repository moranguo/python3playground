# -*- coding: utf-8 -*-


def add(a, *args):
    my_sum = a
    for item in args:
        my_sum += item
    return my_sum


def test_add_two_number():
    assert 33 == add(11, 22)
    assert 55.55 == add(22.22, 33.33)


def test_add_three_number():
    assert 101 == add(10, 90, 1)
