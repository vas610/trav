import os
import os.path
from os import path
import pytest
import sys
import json
import challenge_solution


input_file = 'input/sample.json'

with open(input_file, encoding='utf-8') as _in_file:
    _raw_obj = _in_file.readlines()


def test_create_df():
    df = challenge_solution.create_df(_raw_obj)
    assert len(df) == 7


@pytest.fixture
def create_df():
    df = challenge_solution.create_df(_raw_obj)
    return df


def test_create_csv(create_df):
    output_csv_file = challenge_solution.create_csv(input_file, create_df)
    assert path.exists(output_csv_file) is True


def test_max_rating_per_industry(create_df):
    out_df = challenge_solution.max_rating_per_industry(create_df)
    assert len(out_df) == 1
    assert out_df.to_dict()['Manufacturing'] == 770


def test_company_with_min_rating_per_parent(create_df):
    out_df = challenge_solution.company_with_min_rating_per_parent(create_df)
    out_df_dict = out_df.to_dict('records')
    assert len(out_df_dict) == 2
    assert (out_df_dict[0]['parent_guid'] == '69012de7-10d4-4b13-940c-872e8cc4a0f0'
            and out_df_dict[0]['guid'] == 'b159d957-ec00-480a-948a-fb690836442a')


def test_pivot_child_companies_to_parent(create_df):
    out_df = challenge_solution.pivot_child_companies_to_parent(create_df)
    out_df_dict = out_df.to_dict('records')
    assert len(out_df_dict) == 2
    assert (out_df_dict[0]['parent_guid'] == '69012de7-10d4-4b13-940c-872e8cc4a0f0'
            and out_df_dict[0]['child_name_0'] == 'KYOCERA Asia Pacific Pte. Ltd.'
            and out_df_dict[1]['parent_guid'] == '7585a01a-fa62-4c26-be3f-f8e82aa819e0'
            and out_df_dict[1]['child_name_1'] == 'KYOCERA International, Inc. - Display Division')
