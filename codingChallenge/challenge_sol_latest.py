#!/usr/bin/python3
# %%

import os
import json
import pandas as pd
import glob

pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.set_option('expand_frame_repr', False)

# %%


def parse_json(parentId, EventTS, EventTypeCd, FormCd, obj):
    """
    This function will parse the input json and return one row per child with
    the parent id of the child

    :parentId: parent id
    :obj: child json/dict object to be parsed

    :yield: describe what it returns
    """

    if (len(obj) > 0):
        for obj_item in obj:
            yield (parentId, obj_item.get("guid"),
                   obj_item.get("name"),
                   obj_item.get("rating"),
                   obj_item.get("industry"),
                   obj_item.get("is_service_provider"),
                   obj_item.get("rating_type"),
                   obj_item.get("is_subscribed"),
                   EventTS,
                   EventTypeCd,
                   FormCd
                   )
            yield from parse_json(obj_item.get("guid"),
                                  EventTS, EventTypeCd, FormCd,
                                  obj_item.get("children"))

# %%


def create_df(obj):
    """
    Creates a pandas dataframe for input json

    :return: panads frame with input data
    """

    listAll = []
    for _o in obj:
        _o = json.loads(_o)
        top_parent_id = _o["guid"]
        top_parent_name = _o["name"]
        top_parent_rating = _o["rating"]
        top_parent_industry = _o["industry"]
        top_parent_is_service_provider = _o["is_service_provider"]
        top_parent_rating_type = _o["rating_type"]
        top_parent_is_subscribed = _o["is_subscribed"]
        top_parent_EventTS = _o["EventTS"]
        top_parent_EventTypeCd = _o["EventTypeCd"]
        top_parent_FormCd = _o["FormCd"]
        listAll.append([top_parent_id,
                        top_parent_id,
                        top_parent_name,
                        top_parent_rating,
                        top_parent_industry,
                        top_parent_is_service_provider,
                        top_parent_rating_type,
                        top_parent_is_subscribed,
                        top_parent_EventTS,
                        top_parent_EventTypeCd,
                        top_parent_FormCd])
        for i in parse_json(
                top_parent_id, top_parent_EventTS, top_parent_EventTypeCd,
                top_parent_FormCd, _o["children"]):

            listAll.append(list(i))

    df = pd.DataFrame(listAll, columns=["parent_guid", "guid", "name",
                                        "rating", "industry",
                                        "is_service_provider",
                                        "rating_type", "is_subscribed",
                                        "EventTS", "EventTypeCd", "FormCd"])
    return df

# %%


def create_csv(input_file, df):
    """
    Creates a csv file for input json

    :input_file: input json file name
    :df: dataframe to be saved as csv

    :return: csv file name with path
    """
    output_csv_file = os.path.abspath(input_file)
    input_file_path = os.path.sep.join(
        output_csv_file.split(os.path.sep)[:-1])
    input_file_name = output_csv_file.split(os.path.sep)[-1].split('.')[0]
    output_csv_file = os.path.join(input_file_path, input_file_name + '.csv')
    try:
        os.remove(output_csv_file)
    except OSError:
        pass
    df.to_csv(output_csv_file, index=False, sep='\t')
    return output_csv_file



# %%
def max_rating_per_industry(df):
    """
    Return the max rating per industry

    :df: input data frame
    :return: df series
    """
    return df.groupby(["industry"])["rating"].max()


# %%
def company_with_min_rating_per_parent(df):
    """
    Return company with minimum rating per parent

    :df: input data frame
    :return: df series
    """
    df_temp = df.loc[df['parent_guid'] != df['guid']]
    return (
        df_temp.loc[
            df_temp.groupby('parent_guid').rating.idxmin()].sort_index())


# %%
if __name__ == '__main__':
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    input_file = input().strip()
    if input_file is None or len(input_file) == 0:
        # input_file = '../b.i/b.i.test/sample.json'
        input_file = 'json'
        print("No input file given. Using a sample file")
    with open(input_file,
              encoding='utf-8') as _in_file:
        _raw_obj = _in_file.readlines()
        df = create_df(_raw_obj)
        print("================Save Parse JSON as CSV=============")
        print(create_csv(input_file, df))
        print("===================================================")
        print("===============Max rating per industry=============")
        print(max_rating_per_industry(df))
        print("===================================================")
        print("==========Company with min rating per parent=======")
        print(company_with_min_rating_per_parent(df))
        print("===================================================")
