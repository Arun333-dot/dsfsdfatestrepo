{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_p5_post_OrderBy_1_0",
    "database": "hive_metastore",
    "schema": "arun123"
  })
}}

WITH prophecy__temp_p5_post_SFTPSource_1_0 AS (

  SELECT * 
  
  FROM {{ source('prophecy__temp_p5_source', 'prophecy__temp_p5_post_SFTPSource_1_0') }}

),

Reformat_1 AS (

  SELECT * 
  
  FROM prophecy__temp_p5_post_SFTPSource_1_0 AS in0

),

OrderBy_1 AS (

  SELECT * 
  
  FROM Reformat_1 AS in0
  
  ORDER BY id ASC NULLS FIRST

)

SELECT *

FROM OrderBy_1
