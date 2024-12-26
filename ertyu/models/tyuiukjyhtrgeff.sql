WITH databricks AS (

  SELECT * 
  
  FROM {{ source('hive_metastore.rohit', 'databricks') }}

)

SELECT *

FROM databricks
