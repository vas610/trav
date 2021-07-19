# Challenge

1.	Parse the attached Json and create a CSV file 
	
2.	Perform the below descriptive analysis; 
    - i.	Get only the maximum rating for an industry
    - ii.	Get the minimum rating of a child company for the parent company
    - iii.	Transpose all the child companies as columns for a parent company


# Note

1. Possible test data error: The given JSON file wasn't a valid json. It had two JSON records. I assumed both the records need to be combined before the analysis.
2. _Get the minimum rating of a child company for the parent company_ Assumed the company with minimum rating for a parent is needed.
3. _Transpose all the child companies as columns for a parent company_ Assumed child comapnies to be pivoted to respective parent company. 



## Outputs

1. Save JSON as CSV - [1_output.csv](1_output.csv)


2.  

    -  i. Max rating per industry

           industry
           Business Services    780
           Energy/Resources     710
           Engineering          760
           Finance              700
           Manufacturing        770
           Technology           760
           Name: rating, dtype: int64
    
  
    -  ii. Company with minimum rating per parent  
  
           parent_guid                                  guid                                            name  rating           industry  is_service_provider rating_type  is_subscribed                   EventTS EventTypeCd                       FormCd
           6 7585a01a-fa62-4c26-be3f-f8e82aa819e0  d7bdd7da-3c5b-4209-86aa-9899ade317c6  KYOCERA International, Inc. - Display Division     730      Manufacturing                False     CURATED          False  2018-10-15T18:37:27.712Z    BITSIGHT  Companies_GUID_Company-tree
           7 69012de7-10d4-4b13-940c-872e8cc4a0f0  06c8cb4d-d3e8-40a4-9be5-20886a453468                KYOCERA Document Solutions Group     510      Manufacturing                False     CURATED          False  2018-10-15T18:37:27.712Z    BITSIGHT  Companies_GUID_Company-tree
           12 ad8b9521-d8b8-4c02-bbe8-74dfbcc11255  28aac3bc-2e4a-4bc7-98b2-ce475cd07ea7         KYOCERA Document Solutions Asia Limited     610  Business Services                False     CURATED          False  2018-10-15T18:37:27.712Z    BITSIGHT  Companies_GUID_Company-tree
           15 06c8cb4d-d3e8-40a4-9be5-20886a453468  e32e733a-3111-468c-9bee-81b74542cfb9         KYOCERA Document Solutions Europe Group     550  Business Services                False     CURATED          False  2018-10-15T18:37:27.712Z    BITSIGHT  Companies_GUID_Company-tree
           18 e32e733a-3111-468c-9bee-81b74542cfb9  fe409d83-0260-4a38-a6aa-88309cf6947b         KYOCERA Document Solutions Belgium N.V.     490  Business Services                False     CURATED          False  2018-10-15T18:37:27.712Z    BITSIGHT  Companies_GUID_Company-tree
           35 9d00093b-10f4-4675-b6a1-3153c52fd6bf  431ef8db-be7a-4da1-b4ac-30387feaac0e                          KYOCERA UNIMERCO Group     610        Engineering                False     CURATED          False  2018-10-15T18:37:27.712Z    BITSIGHT  Companies_GUID_Company-tree
           36 431ef8db-be7a-4da1-b4ac-30387feaac0e  dda08a8c-4648-4430-9be8-a0eb975a5bf7                            KYOCERA UNIMERCO A/S     620        Engineering                False     CURATED          False  2018-10-15T18:37:27.712Z    BITSIGHT  Companies_GUID_Company-tree
           50 708e91f9-1197-4cee-a3bf-d407c80c2f61  b17dce7b-8d46-4048-a9b0-8a1697abefee             KYOCERA SENCO Netherlands Companies     520        Engineering                False     CURATED          False  2018-10-15T18:37:27.712Z    BITSIGHT  Companies_GUID_Company-tree
           51 b17dce7b-8d46-4048-a9b0-8a1697abefee  859e3bc6-fd1b-46f9-9195-46d5333f567a                       KYOCERA SENCO Deutschland     570      Manufacturing                False     CURATED          False  2018-10-15T18:37:27.712Z    BITSIGHT  Companies_GUID_Company-tree
