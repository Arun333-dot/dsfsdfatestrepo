WITH deeply_nested_json AS (

  SELECT * 
  
  FROM {{ source('hive_metastore.rohit', 'deeply_nested_json') }}

),

Reformat_1 AS (

  {#Extracts task status, notes, and team member roles from project data.#}
  SELECT 
    projects.tasks.sub_tasks.status AS status,
    projects.tasks.sub_tasks.notes.note AS note,
    team.members.role AS role
  
  FROM deeply_nested_json AS in0

)

SELECT *

FROM Reformat_1
