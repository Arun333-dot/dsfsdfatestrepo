WITH flatten AS (

  SELECT * 
  
  FROM {{ ref('flatten')}}

)

SELECT *

FROM flatten
