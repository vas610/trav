#!venv/bin/python3
# %%
import sys
import os
import json
import logging
import pandas as pd
import numpy as np
from tabulate import tabulate

# Something to make pandas display in print much more readable
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.set_option('expand_frame_repr', False)

# Setting up the logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

# STDOUT handler
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(formatter)

# Log file handler
os.makedirs('logs', mode=0o777, exist_ok=True)
file_handler = logging.FileHandler('logs/logs.log', 'w+')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Adding handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(stdout_handler)

# %%


def parse_json(parentId, parentName, EventTS, EventTypeCd, FormCd, obj):
    """
    This function will parse the input json and return one row per child with
    the parent id of the child

    :parentId: parent id
    :obj: child json/dict object to be parsed

    :yield: describe what it returns
    """

    if (len(obj) > 0):
        for obj_item in obj:
            yield (parentId, parentName,
                   obj_item.get("guid"),
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
                                  obj_item.get("name"),
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
        listAll.append([None,
                        None,
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
                top_parent_id, top_parent_name,
                top_parent_EventTS, top_parent_EventTypeCd,
                top_parent_FormCd, _o["children"]):

            listAll.append(list(i))

    df = pd.DataFrame(listAll, columns=["parent_guid", "parent_name",
                                        "guid", "name",
                                        "rating", "industry",
                                        "is_service_provider",
                                        "rating_type", "is_subscribed",
                                        "EventTS", "EventTypeCd", "FormCd"])
    return df

# %%


def create_csv(input_file, df):
    """
    Creates a csv file for input json

    :input_file: parent id
    :obj: child json/dict object to be parsed

    :return: csv file
    """
    output_csv_file = os.path.abspath(input_file)
    input_file_path = os.path.sep.join(
        output_csv_file.split(os.path.sep)[:-2])
    input_file_name = output_csv_file.split(os.path.sep)[-1].split('.')[0]
    output_csv_file = os.path.join(input_file_path, 'output',
                                   input_file_name + '.csv')
    try:
        os.remove(output_csv_file)
    except OSError:
        pass
    df.to_csv(output_csv_file, index=False)
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
def pivot_child_companies_to_parent(df):
    """
    Returns a pivoted dataframe with companies tied to respective parent

    :df: input data frame
    :return: df
    """
    # To keep it simeple, selected only the
    # parent_guid, parent_name, guid and name
    df_temp_1 = df[['parent_guid', 'parent_name', 'guid', 'name']]
    cols_agg = ['guid', 'name']
    df_temp_2 = df_temp_1.groupby(['parent_guid', 'parent_name']).agg(
        {cols_agg[0]: '|'.join, cols_agg[1]: '|'.join}).reset_index()
    df_temp_3 = df_temp_2['name'].str.split(
        '|', expand=True).add_prefix('child_name_')
    df_temp_4 = df_temp_2['guid'].str.split(
        '|', expand=True).add_prefix('child_guid_')
    df_temp_5 = pd.concat([df_temp_3, df_temp_4], axis=1).replace(np.nan, '-')
    df_final = pd.concat(
        [df_temp_2[
            ['parent_guid',
             'parent_name']],
            df_temp_3, df_temp_4], axis=1).replace(np.nan, '-')
    return df_final


# %%
if __name__ == '__main__':
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    input_file = input(
        "Enter a json file name (with path) to process: ").strip()
    if input_file is None or len(input_file) == 0:
        # input_file = '../b.i/b.i.test/sample.json'
        input_file = 'input/sample.json'
        logger.info(f"No input file given. Using a sample file {input_file}")
    with open(input_file,
              encoding='utf-8') as _in_file:
        _raw_obj = _in_file.readlines()
        df = create_df(_raw_obj)
        logger.info("================Save Parse JSON as CSV=============")
        logger.info(create_csv(input_file, df))
        logger.info("===================================================\n")
        logger.info("===============Max rating per industry=============")
        logger.info("\n" + str(max_rating_per_industry(df)))
        logger.info("===================================================\n")
        logger.info("==========Company with min rating per parent=======")
        logger.info("\n" + tabulate(company_with_min_rating_per_parent(df),
                                    headers='keys', tablefmt='github'))
        logger.info("===================================================\n")
        logger.info("==========Pivot / transpose child to parent=======")
        # print(pivot_child_companies_to_parent(df))
        logger.info("\n" + tabulate(pivot_child_companies_to_parent(df),
                                    headers='keys', tablefmt='github'))
        logger.info("===================================================\n")

# %%
