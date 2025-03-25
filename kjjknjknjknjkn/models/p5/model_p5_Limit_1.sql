{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_p5_post_Limit_1_0",
    "database": "hive_metastore",
    "schema": "arun123"
  })
}}

WITH prophecy__temp_p5_post_SFTPSource_1_0 AS (

  SELECT * 
  
  FROM {{ source('prophecy__temp_p5_source', 'prophecy__temp_p5_post_SFTPSource_1_0') }}

),

Limit_1 AS (

  SELECT * 
  
  FROM prophecy__temp_p5_post_SFTPSource_1_0 AS in0
  
  LIMIT 10

)

SELECT *

FROM Limit_1
