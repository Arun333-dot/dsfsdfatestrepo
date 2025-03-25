{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_p4_post_OrderBy_1_1_0",
    "database": "hive_metastore",
    "schema": "arun123"
  })
}}

WITH prophecy__temp_p4_post_SFTPSource_1_0 AS (

  SELECT * 
  
  FROM {{ source('prophecy__temp_p4_source', 'prophecy__temp_p4_post_SFTPSource_1_0') }}

),

Reformat_1_1 AS (

  SELECT * 
  
  FROM prophecy__temp_p4_post_SFTPSource_1_0 AS in0

),

OrderBy_1_1 AS (

  SELECT * 
  
  FROM Reformat_1_1 AS in0
  
  ORDER BY id ASC, name ASC, email ASC, age ASC, city ASC, country ASC

)

SELECT *

FROM OrderBy_1_1
