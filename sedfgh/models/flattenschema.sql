WITH nested_arraysjosn AS (

  SELECT * 
  
  FROM {{ source('hive_metastore.rohit', 'nested_arraysjosn') }}

),

project_durations AS (

  {#Extracts project duration details from nested project data.#}
  SELECT nested_array.col AS projects_nested_array
  
  FROM nested_arraysjosn AS in0, 
  LATERAL explode_outer(projects) AS projects, 
  LATERAL explode_outer(projects.col.nested_array) AS nested_array

),

databricks_null AS (

  SELECT * 
  
  FROM {{ source('hive_metastore.rohit', 'databricks_null') }}

),

databricks_flatten_jsonarray AS (

  SELECT * 
  
  FROM {{ source('hive_metastore.rohit', 'databricks_flatten_jsonarray') }}

),

age_selection AS (

  {#Extracts age data from a structured dataset for demographic analysis.#}
  SELECT age AS age
  
  FROM databricks_flatten_jsonarray AS in0

),

databricks_large AS (

  SELECT * 
  
  FROM {{ source('hive_metastore.rohit', 'databricks_large') }}

),

databricks123 AS (

  SELECT * 
  
  FROM {{ source('hive_metastore.rohit', 'databricks123') }}

)

SELECT *

FROM project_durations
