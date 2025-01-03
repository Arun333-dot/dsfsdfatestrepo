WITH databricks_nested AS (

  SELECT * 
  
  FROM {{ source('hive_metastore.rohit', 'databricks_nested') }}

),

FlattenSchema_1 AS (

  {#Simplifies project data by extracting project names and associated technologies.#}
  SELECT 
    projects.col.name AS name,
    technologies.col AS technologies
  
  FROM databricks_nested AS in0, 
  LATERAL explode_outer(projects) AS projects, 
  LATERAL explode_outer(projects.col.technologies) AS technologies

)

SELECT *

FROM FlattenSchema_1
