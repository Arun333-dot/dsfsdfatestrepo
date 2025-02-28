{{
  config({    
    "materialized": "table"
  })
}}

WITH dsfg AS (

  SELECT * 
  
  FROM {{ ref('dsfg')}}

)

SELECT *

FROM dsfg
