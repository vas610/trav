#!/usr/bin/python3
# i.	Get only the maximum rating for an industry
import json


def fn_industry_rating(obj):
    """
    function to parse the json/dict and return a list of industry and rating
    from each node

    obj: input dict
    """

    for k, v in obj.items():
        if k == 'industry':
            # x = dict((v,obj['rating']))
            x = {}
            x[v] = obj['rating']
            array.append(x)
            # _l.append(dict((v, obj['rating'])))
        elif k == 'children' and isinstance(v, list) and len(v) > 0:
            for i in v:
                fn_industry_rating(i)


if __name__ == '__main__':

    # main clause

    array = [] # A list to hold all industry rating
    max_industry_rating = {}  # A dict to hold max industry rating

    # with open('sample.json',
    #           encoding='utf-8') as _in_file:
    #     _json = json.load(_in_file)


    with open('part-r-00000-ace4d84a-d8cb-4eaa-a377-9d3e8bbf73b2',
              encoding='utf-8') as _in_file:
        _json = json.load(_in_file)


    for i in _json:
        fn_industry_rating(i)
        idx = 0
        while idx < len(array):
            for key in array[idx]:
                val = array[idx][key]
                if key not in max_industry_rating:
                    max_industry_rating[key] = val
                elif ((key in max_industry_rating) and
                       (max_industry_rating[key] < val)):
                    max_industry_rating[key] = val
            idx += 1

    print(max_industry_rating)

    # Output
    #  {'Manufacturing': 770,
    #   'Technology': 760,
    #   'Business Services': 780,
    #   'Engineering': 760,
    #   'Energy/Resources': 710,
    #   'Finance': 700}

