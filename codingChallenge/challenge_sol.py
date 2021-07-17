#!/usr/bin/python3
import json
import json_flatten
import pandas as pd

with open('../b.i/sample.json',
          encoding='utf-8') as _in_file:
    _json = json.load(_in_file)


# def parse_dict_of_dict(_dict, ret_dict={}):
#     _guid, _children, = _dict["guid"], _dict.get('children', None),
#     if _guid not in ret_dict:
#         ret_dict[_guid] = []
#      if _children is not None:
#         if isinstance(_children, list):
#             for _child in _children:
#                    parse_dict_of_dict(_child, ret_dict)
#     ret_dict[_guid] =
#     return ret_dict


# for i in _json:
#     print(parse_dict_of_dict(i))
# %%

def iter_cls(parentId, obj):
    if (len(obj) > 0):
        for obj_item in obj:
            yield (parentId, obj_item.get("guid"),
                   obj_item.get("name"), obj_item.get(
                       "rating"), obj_item.get("industry"),
                   obj_item.get("is_service_provider"), obj_item.get(
                       "rating_type"),
                   obj_item.get("is_subscribed")
                   )
            yield from iter_cls(obj_item.get("guid"), obj_item.get("children"))


listAll = []
for i in _json:
    top_cls_id = i["guid"]
    top_cls_name = i["name"]
    top_cls_rating = i["rating"]
    top_industry = i["industry"]
    top_cls_is_service_provider = i["is_service_provider"]
    top_rating_type = i["rating_type"]
    top_is_subscribed = i["is_subscribed"]
    listAll.append([top_cls_id, top_cls_id, top_cls_name, top_cls_rating, top_industry,
                    top_cls_is_service_provider, top_rating_type, top_is_subscribed])
    for i in iter_cls(top_cls_id, i["children"]):
        listAll.append(list(i))

df = pd.DataFrame(listAll, columns=["pid", "id", "name", "rating",
                                    "industry", "is_service_provider", "rating_type", "is_subscribed"])

df.groupby(["industry"])["rating"].max()


# %%
df.loc[df.groupby('pid').rating.idxmin()].sort_index()
# %%
