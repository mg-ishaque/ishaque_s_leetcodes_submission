WITH ranked_salary AS (
    SELECT 
        salary,
        departmentId,
        name,
        RANK() OVER (
            PARTITION BY departmentId 
            ORDER BY salary DESC
        ) AS rnk
    FROM Employee
)

SELECT 
    e.name AS "Employee",
    d.name AS "Department",
    salary
FROM ranked_salary e
JOIN Department d 
    ON e.departmentId = d.id
WHERE rnk = 1;