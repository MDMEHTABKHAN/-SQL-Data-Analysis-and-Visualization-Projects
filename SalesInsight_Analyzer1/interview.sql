
CREATE TABLE employee01 (
    Employee_ID INT PRIMARY KEY,
    Name VARCHAR(100),
    Department VARCHAR(50),
    Salary DECIMAL(10,2),
    Hire_Date DATE
);

INSERT INTO employee01
VALUES
(1, 'Alice Johnson', 'Sales', 60000, '2020-03-15'),
(2, 'Bob Smith', 'Marketing', 55000, '2019-07-22'),
(3, 'Charlie Brown', 'Sales', 62000, '2021-01-10'),
(4, 'Diana Prince', 'HR', 58000, '2018-11-30'),
(5, 'Ethan Hunt', 'IT', 75000, '2022-05-05'),
(6, 'Fiona Glenanne', 'Marketing', 53000, '2020-09-17'),
(7, 'George Costanza', 'Sales', 61000, '2019-12-01'),
(8, 'Hannah Baker', 'IT', 60000, '2021-06-25'),
(9, 'Ian Fleming', 'HR', 57000, '2017-08-14'),
(10, 'Jane Doe', 'Sales', 55000, '2022-02-20');

INSERT INTO employee01
VALUES
(11, 'Kevin Mitnick', 'IT', 75000, '2023-01-15'),
(12, 'Laura Palmer', 'Marketing', 54000, '2021-03-30');


SELECT MAX(salary) AS Second_Highest_salary
FROM employee01
WHERE Salary < (
    SELECT MAX(Salary) FROM employee01
);

SELECT *
FROM employee01
WHERE Salary > (
    SELECT AVG(Salary) FROM employee01
);


SELECT department, Name, Salary,
ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary ASC) AS Salary_Rank,
RANK() OVER (PARTITION BY department ORDER BY salary ASC) AS Salary_Rank2,
DENSE_RANK() OVER (PARTITION BY department ORDER BY salary ASC) AS Salary_Rank3
FROM employee01;



SELECT department, Name, Salary,
ROW_NUMBER() OVER ( ORDER BY salary ASC) AS Salary_Rank,
RANK() OVER (ORDER BY salary ASC) AS Salary_Rank2,
DENSE_RANK() OVER (ORDER BY salary ASC) AS Salary_Rank3
FROM employee01;


SELECT Salary
FROM (SELECT Salary,department,
                DENSE_RANK()OVER (ORDER BY Salary DESC) AS salary_rank
        FROM employee01) AS ranked_salaries
WHERE salary_rank = 3;

SELECT Department, COUNT(*) AS Employee_Count
FROM employee01
GROUP BY Department
HAVING COUNT(*) > 1;

