# Challenge

1.	Parse the attached Json and create a CSV file 
	
2.	Perform the below descriptive analysis; 
    - i.	Get only the maximum rating for an industry
    - ii.	Get the minimum rating of a child company for the parent company
    - iii.	Transpose all the child companies as columns for a parent company


# Note

1. Possible test data error: The given JSON file wasn't a valid json. It had two JSON records. I assumed both the records need to be combined before the analysis.
2. _Get the minimum rating of a child company for the parent company_  - Assumed the company with minimum rating for a parent is needed.
3. _Transpose all the child companies as columns for a parent company_  - Assumed child comapnies to be pivoted to respective parent company. 


## Setup
    
    # Required python3.6 or higher in a linux / unix system
    
    git@github.com:vas610/trav.git
    
    cd trav/codingChallenge
    
    python -m venv venv
    
    source ./venv/bin/activate
    
    pip install -e .
    
## Outputs

1. Save JSON as CSV - [1_output.csv](1_output.csv)

   |parent_guid                         |guid                                |name                                             |rating|industry         |is_service_provider|rating_type|is_subscribed|EventTS                 |EventTypeCd|FormCd                     |
   |------------------------------------|------------------------------------|-------------------------------------------------|------|-----------------|-------------------|-----------|-------------|------------------------|-----------|---------------------------|
   |69012de7-10d4-4b13-940c-872e8cc4a0f0|69012de7-10d4-4b13-940c-872e8cc4a0f0|KYOCERA Group                                    |490   |Manufacturing    |False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |69012de7-10d4-4b13-940c-872e8cc4a0f0|28837c60-21e8-49d2-aa29-6ab1a69af529|KYOCERA Asia Pacific Pte. Ltd.                   |650   |Manufacturing    |False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |69012de7-10d4-4b13-940c-872e8cc4a0f0|adbbff76-3846-46f3-bdd8-f0c4206e6803|KYOCERA Chemical (Wuxi) Co., Ltd.                |730   |Manufacturing    |False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |69012de7-10d4-4b13-940c-872e8cc4a0f0|b159d957-ec00-480a-948a-fb690836442a|KYOCERA Corporation                              |560   |Manufacturing    |False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |69012de7-10d4-4b13-940c-872e8cc4a0f0|7585a01a-fa62-4c26-be3f-f8e82aa819e0|KYOCERA Display Group                            |750   |Manufacturing    |False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |7585a01a-fa62-4c26-be3f-f8e82aa819e0|5c0ec5d1-f582-422b-8881-bdfada235ce5|KYOCERA Display Corporation                      |770   |Manufacturing    |False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |7585a01a-fa62-4c26-be3f-f8e82aa819e0|d7bdd7da-3c5b-4209-86aa-9899ade317c6|KYOCERA International, Inc. - Display Division   |730   |Manufacturing    |False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |69012de7-10d4-4b13-940c-872e8cc4a0f0|06c8cb4d-d3e8-40a4-9be5-20886a453468|KYOCERA Document Solutions Group                 |510   |Manufacturing    |False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |06c8cb4d-d3e8-40a4-9be5-20886a453468|3b510573-53a7-45ba-b221-4051fd274209|Annodata Limited                                 |760   |Technology       |False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |06c8cb4d-d3e8-40a4-9be5-20886a453468|6b6ab696-8717-4b5e-8043-67ed6febbca0|Ceyoniq Technology GmbH                          |740   |Technology       |False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |06c8cb4d-d3e8-40a4-9be5-20886a453468|ad8b9521-d8b8-4c02-bbe8-74dfbcc11255|KYOCERA Document Solutions Asia Companies        |590   |Business Services|False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |ad8b9521-d8b8-4c02-bbe8-74dfbcc11255|61277b5d-38cf-471a-afc3-082e7671a710|KYOCERA Document Solutions (Thailand) Corp., Ltd.|640   |Business Services|False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |ad8b9521-d8b8-4c02-bbe8-74dfbcc11255|28aac3bc-2e4a-4bc7-98b2-ce475cd07ea7|KYOCERA Document Solutions Asia Limited          |610   |Business Services|False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |ad8b9521-d8b8-4c02-bbe8-74dfbcc11255|e14470f7-09d4-4a25-bf55-c1719ca60b0c|KYOCERA Document Solutions Hong Kong Limited     |650   |Business Services|False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |06c8cb4d-d3e8-40a4-9be5-20886a453468|58629abb-a0a1-48cb-acbf-a078825aa6b8|KYOCERA Document Solutions Brazil                |620   |Business Services|False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |06c8cb4d-d3e8-40a4-9be5-20886a453468|e32e733a-3111-468c-9bee-81b74542cfb9|KYOCERA Document Solutions Europe Group          |550   |Business Services|False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |e32e733a-3111-468c-9bee-81b74542cfb9|4a709042-c8cd-485c-8167-aac08fa68cce|KYOCERA Document Solutions (U.K.) Limited        |740   |Business Services|False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |e32e733a-3111-468c-9bee-81b74542cfb9|6ce6e3c9-863b-468d-a0d7-4204092eab1e|KYOCERA Document Solutions Austria GmbH          |740   |Business Services|False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |e32e733a-3111-468c-9bee-81b74542cfb9|fe409d83-0260-4a38-a6aa-88309cf6947b|KYOCERA Document Solutions Belgium N.V.          |490   |Business Services|False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |e32e733a-3111-468c-9bee-81b74542cfb9|dc5062ad-862f-498e-8956-ae6a33155958|KYOCERA Document Solutions Denmark A/S           |730   |Business Services|False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |e32e733a-3111-468c-9bee-81b74542cfb9|f2ac7dbf-1ff0-4b41-9d2b-ffd35c5456bd|KYOCERA Document Solutions Deutschland GmbH      |780   |Business Services|False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |e32e733a-3111-468c-9bee-81b74542cfb9|512eac6c-8161-4951-a8fa-a67d390efa83|KYOCERA Document Solutions España S.A.           |690   |Business Services|False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |e32e733a-3111-468c-9bee-81b74542cfb9|5cdcc6a0-6d96-48b9-b90b-2cd7e70f1f6a|KYOCERA Document Solutions Europe B.V.           |730   |Business Services|False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |e32e733a-3111-468c-9bee-81b74542cfb9|00f35eed-8fa0-4699-a491-a1ecb5273ac0|KYOCERA Document Solutions Finland Oy            |750   |Technology       |False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |e32e733a-3111-468c-9bee-81b74542cfb9|afe0c76c-7bff-4c08-ad45-6a08017f43a2|KYOCERA Document Solutions France S.A.S.         |770   |Business Services|False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |e32e733a-3111-468c-9bee-81b74542cfb9|c29c8e98-621f-4af9-b6a8-c01a190d115d|KYOCERA Document Solutions Italia S.p.A.         |670   |Business Services|False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |e32e733a-3111-468c-9bee-81b74542cfb9|49064d45-fc23-4671-8ed3-3732ba01b429|KYOCERA Document Solutions Middle East           |740   |Business Services|False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |e32e733a-3111-468c-9bee-81b74542cfb9|35c100af-bfaa-4bb3-b124-395f5f9ad497|KYOCERA Document Solutions Norge NUF             |740   |Business Services|False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |e32e733a-3111-468c-9bee-81b74542cfb9|8a39941d-2b9f-40c3-ba4f-b90b3163a1b1|KYOCERA Document Solutions Russia LLC            |740   |Business Services|False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |06c8cb4d-d3e8-40a4-9be5-20886a453468|232770b2-7095-42b8-99ef-63798b3676b7|KYOCERA Document Solutions Inc.                  |630   |Business Services|False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |06c8cb4d-d3e8-40a4-9be5-20886a453468|09380a90-a0a4-4a58-9406-691f2ddfd58d|KYOCERA Document Solutions New England, Inc.     |570   |Business Services|False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |06c8cb4d-d3e8-40a4-9be5-20886a453468|51b7729b-7fb6-4f18-807d-dd6125acd60a|TA Triumph-Adler GmbH                            |680   |Technology       |False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |69012de7-10d4-4b13-940c-872e8cc4a0f0|9d00093b-10f4-4675-b6a1-3153c52fd6bf|KYOCERA Fineceramics Group                       |620   |Manufacturing    |False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |9d00093b-10f4-4675-b6a1-3153c52fd6bf|2a5d7b7b-18d8-4302-85d1-f1f53fc8a6aa|KYOCERA Fineceramics GmbH                        |700   |Manufacturing    |False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |9d00093b-10f4-4675-b6a1-3153c52fd6bf|b4194b6a-2935-4f17-910c-1842d9ad1a55|KYOCERA Fineceramics Ltd                         |760   |Manufacturing    |False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |9d00093b-10f4-4675-b6a1-3153c52fd6bf|431ef8db-be7a-4da1-b4ac-30387feaac0e|KYOCERA UNIMERCO Group                           |610   |Engineering      |False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |431ef8db-be7a-4da1-b4ac-30387feaac0e|dda08a8c-4648-4430-9be8-a0eb975a5bf7|KYOCERA UNIMERCO A/S                             |620   |Engineering      |False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |431ef8db-be7a-4da1-b4ac-30387feaac0e|2f28866f-99e8-4dfb-a978-3866c529df2f|KYOCERA UNIMERCO Tooling AS (Norway)             |760   |Engineering      |False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |431ef8db-be7a-4da1-b4ac-30387feaac0e|1722fd16-fc46-4212-9c55-4b7e8cc3227f|KYOCERA UNIMERCO Tooling GmbH                    |660   |Engineering      |False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |431ef8db-be7a-4da1-b4ac-30387feaac0e|52258991-fdfd-4279-bf1d-50bb08f122c0|KYOCERA UNIMERCO Tooling Inc.                    |740   |Engineering      |False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |431ef8db-be7a-4da1-b4ac-30387feaac0e|e63c4318-bef1-4bea-9af1-5262917c2c04|KYOCERA UNIMERCO Tooling Ltd.                    |760   |Engineering      |False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |69012de7-10d4-4b13-940c-872e8cc4a0f0|960b263d-6db7-49be-a673-a5fb596eccfd|KYOCERA France                                   |710   |Manufacturing    |False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |69012de7-10d4-4b13-940c-872e8cc4a0f0|9fc1b6b3-20af-4df0-87a6-fd852e66c92e|KYOCERA Italia                                   |720   |Manufacturing    |False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |69012de7-10d4-4b13-940c-872e8cc4a0f0|eecb8129-2674-44ae-b973-8932de5b31df|KYOCERA Mexicana, S.A. de C.V.                   |730   |Manufacturing    |False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |69012de7-10d4-4b13-940c-872e8cc4a0f0|86beb991-da5c-4ec7-aebd-f0b1f0a2e3cd|KYOCERA Optec Co., Ltd.                          |730   |Manufacturing    |False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |69012de7-10d4-4b13-940c-872e8cc4a0f0|1bef262e-2a12-45c4-912c-494edb2494d2|KYOCERA Portugal                                 |720   |Manufacturing    |False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |69012de7-10d4-4b13-940c-872e8cc4a0f0|b833f149-5e47-48fe-8fe5-2cc695f8b659|KYOCERA Precision Tools, Inc.                    |670   |Manufacturing    |False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |69012de7-10d4-4b13-940c-872e8cc4a0f0|8eba2032-19e2-43cf-979a-2b9f2105de52|KYOCERA Russia                                   |720   |Manufacturing    |False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |69012de7-10d4-4b13-940c-872e8cc4a0f0|708e91f9-1197-4cee-a3bf-d407c80c2f61|KYOCERA SENCO Industrial Tools Group             |530   |Engineering      |False              |CURATED    |True         |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |708e91f9-1197-4cee-a3bf-d407c80c2f61|233ed996-11fb-42a6-95df-ec253ab4b4d1|KYOCERA SENCO Industrial Tools, Inc.             |610   |Engineering      |False              |CURATED    |True         |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |708e91f9-1197-4cee-a3bf-d407c80c2f61|b17dce7b-8d46-4048-a9b0-8a1697abefee|KYOCERA SENCO Netherlands Companies              |520   |Engineering      |False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |b17dce7b-8d46-4048-a9b0-8a1697abefee|859e3bc6-fd1b-46f9-9195-46d5333f567a|KYOCERA SENCO Deutschland                        |570   |Manufacturing    |False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |b17dce7b-8d46-4048-a9b0-8a1697abefee|e5861f3b-73e7-4b38-aa15-e426fa36e15c|KYOCERA SENCO Netherlands B.V.                   |580   |Business Services|False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |b17dce7b-8d46-4048-a9b0-8a1697abefee|f5265a90-bf28-4a3a-9e1a-023ef1e22195|KYOCERA SENCO UK                                 |720   |Manufacturing    |False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |708e91f9-1197-4cee-a3bf-d407c80c2f61|fe025d9b-97a3-452b-b65a-fe9d7fc9ebb4|SENCO Latín América S.A.S.                       |730   |Engineering      |False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |69012de7-10d4-4b13-940c-872e8cc4a0f0|d8453fc4-da76-4c50-84ad-09ef835f15a3|KYOCERA do Brasil Componentes Industriais Ltda.  |740   |Engineering      |False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |69012de7-10d4-4b13-940c-872e8cc4a0f0|6c5133db-a43a-4e22-b224-24bfe4b3cd53|Kyocera Solar, Inc.                              |710   |Energy/Resources |False              |CURATED    |False        |2018-10-15T18:37:27.712Z|BITSIGHT   |Companies_GUID_Company-tree|
   |5ec089ca-beb6-42e4-9184-216a7fd95612|5ec089ca-beb6-42e4-9184-216a7fd95612|Huntington Bancshares, Inc.                      |700   |Finance          |False              |CURATED    |True         |2018-10-15T18:36:26.690Z|BITSIGHT   |Companies_GUID_Company-tree|
   



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
	   
	   
    -  ii. Company with minimum rating per parent  	   
    
    
           parent_guid                                parent_name                                       child_name_0                                    child_name_1                                  child_name_2                            child_name_3                                 child_name_4                            child_name_5                                  child_name_6                           child_name_7                              child_name_8                              child_name_9                           child_name_10                         child_name_11                          child_name_12                         child_name_13                                    child_name_14        child_name_15
           0  06c8cb4d-d3e8-40a4-9be5-20886a453468           KYOCERA Document Solutions Group                                   Annodata Limited                         Ceyoniq Technology GmbH     KYOCERA Document Solutions Asia Companies       KYOCERA Document Solutions Brazil      KYOCERA Document Solutions Europe Group         KYOCERA Document Solutions Inc.  KYOCERA Document Solutions New England, Inc.                  TA Triumph-Adler GmbH                                         -                                         -                                       -                                     -                                      -                                     -                                                -                    -
           1  431ef8db-be7a-4da1-b4ac-30387feaac0e                     KYOCERA UNIMERCO Group                               KYOCERA UNIMERCO A/S            KYOCERA UNIMERCO Tooling AS (Norway)                 KYOCERA UNIMERCO Tooling GmbH           KYOCERA UNIMERCO Tooling Inc.                KYOCERA UNIMERCO Tooling Ltd.                                       -                                             -                                      -                                         -                                         -                                       -                                     -                                      -                                     -                                                -                    -
           2  69012de7-10d4-4b13-940c-872e8cc4a0f0                              KYOCERA Group                     KYOCERA Asia Pacific Pte. Ltd.               KYOCERA Chemical (Wuxi) Co., Ltd.                           KYOCERA Corporation                   KYOCERA Display Group             KYOCERA Document Solutions Group              KYOCERA Fineceramics Group                                KYOCERA France                         KYOCERA Italia            KYOCERA Mexicana, S.A. de C.V.                   KYOCERA Optec Co., Ltd.                        KYOCERA Portugal         KYOCERA Precision Tools, Inc.                         KYOCERA Russia  KYOCERA SENCO Industrial Tools Group  KYOCERA do Brasil Componentes Industriais Ltda.  Kyocera Solar, Inc.
           3  708e91f9-1197-4cee-a3bf-d407c80c2f61       KYOCERA SENCO Industrial Tools Group               KYOCERA SENCO Industrial Tools, Inc.             KYOCERA SENCO Netherlands Companies                    SENCO Latín América S.A.S.                                       -                                            -                                       -                                             -                                      -                                         -                                         -                                       -                                     -                                      -                                     -                                                -                    -
           4  7585a01a-fa62-4c26-be3f-f8e82aa819e0                      KYOCERA Display Group                        KYOCERA Display Corporation  KYOCERA International, Inc. - Display Division                                             -                                       -                                            -                                       -                                             -                                      -                                         -                                         -                                       -                                     -                                      -                                     -                                                -                    -
           5  9d00093b-10f4-4675-b6a1-3153c52fd6bf                 KYOCERA Fineceramics Group                          KYOCERA Fineceramics GmbH                        KYOCERA Fineceramics Ltd                        KYOCERA UNIMERCO Group                                       -                                            -                                       -                                             -                                      -                                         -                                         -                                       -                                     -                                      -                                     -                                                -                    -
           6  ad8b9521-d8b8-4c02-bbe8-74dfbcc11255  KYOCERA Document Solutions Asia Companies  KYOCERA Document Solutions (Thailand) Corp., Ltd.         KYOCERA Document Solutions Asia Limited  KYOCERA Document Solutions Hong Kong Limited                                       -                                            -                                       -                                             -                                      -                                         -                                         -                                       -                                     -                                      -                                     -                                                -                    -
           7  b17dce7b-8d46-4048-a9b0-8a1697abefee        KYOCERA SENCO Netherlands Companies                          KYOCERA SENCO Deutschland                  KYOCERA SENCO Netherlands B.V.                              KYOCERA SENCO UK                                       -                                            -                                       -                                             -                                      -                                         -                                         -                                       -                                     -                                      -                                     -                                                -                    -
           8  e32e733a-3111-468c-9bee-81b74542cfb9    KYOCERA Document Solutions Europe Group          KYOCERA Document Solutions (U.K.) Limited         KYOCERA Document Solutions Austria GmbH       KYOCERA Document Solutions Belgium N.V.  KYOCERA Document Solutions Denmark A/S  KYOCERA Document Solutions Deutschland GmbH  KYOCERA Document Solutions España S.A.        KYOCERA Document Solutions Europe B.V.  KYOCERA Document Solutions Finland Oy  KYOCERA Document Solutions France S.A.S.  KYOCERA Document Solutions Italia S.p.A.  KYOCERA Document Solutions Middle East  KYOCERA Document Solutions Norge NUF  KYOCERA Document Solutions Russia LLC                                     -                                                -                    -
