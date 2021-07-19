import pytest
import sys
import json
import os
import challenge_solution


input_file = 'input/sample.json'

with open(input_file, encoding='utf-8') as _in_file:
    _raw_obj = _in_file.readlines()


def test_create_df():
    df = challenge_solution.create_df(_raw_obj)
    assert len(df) == 7


def test_1_fn_industry_rating():
    assert 1 == 1
