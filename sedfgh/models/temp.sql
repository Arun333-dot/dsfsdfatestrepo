WITH customers AS (

  SELECT * 
  
  FROM {{ ref('customers')}}

),

Reformat_1 AS (

  {#Simplifies customer data by focusing on essential identifiers and names.#}
  SELECT 
    customer_id AS customer_id,
    first_name AS first_name
  
  FROM customers

)

SELECT *

FROM Reformat_1
