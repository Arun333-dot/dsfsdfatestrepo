WITH deeply_nested_json AS (

  SELECT * 
  
  FROM {{ source('hive_metastore.rohit', 'deeply_nested_json') }}

),

FlattenSchema_1 AS (

  {#Simplifies complex project data to show roles, task statuses, and notes for better team management.#}
  SELECT 
    members.col.role AS role,
    sub_tasks.col.status AS status,
    notes.col.note AS note,
    id AS id
  
  FROM deeply_nested_json AS in0, 
  LATERAL explode_outer(team) AS team, 
  LATERAL explode_outer(team.col.members) AS members, 
  LATERAL explode_outer(projects) AS projects, 
  LATERAL explode_outer(projects.col.tasks) AS tasks, 
  LATERAL explode_outer(tasks.col.sub_tasks) AS sub_tasks, 
  LATERAL explode_outer(sub_tasks.col.notes) AS notes

)

SELECT *

FROM FlattenSchema_1
