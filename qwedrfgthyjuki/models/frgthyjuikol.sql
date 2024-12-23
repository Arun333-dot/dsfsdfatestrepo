WITH deeply_nested_json AS (

  SELECT * 
  
  FROM {{ source('hive_metastore.rohit', 'deeply_nested_json') }}

),

Reformat_1 AS (

  SELECT * 
  
  FROM deeply_nested_json AS in0

)

SELECT *

FROM Reformat_1
