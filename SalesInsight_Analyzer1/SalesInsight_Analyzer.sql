CREATE TABLE sales_data (
    Date DATE,
    Product_Category VARCHAR(50),
    Product VARCHAR(50),
    Sales_Quantity INT,
    Unit_Price DECIMAL(10,2)
);

INSERT INTO sales_data 
VALUES
('2023-01-01', 'Electronics', 'Laptop', 10, 800),
('2023-01-01', 'Electronics', 'Smartphone', 5, 600),
('2023-01-01', 'Clothing', 'T-Shirt', 20, 20),
('2023-01-02', 'Clothing', 'Jeans', 15, 50),
('2023-01-01', 'Electronics', 'Laptop', 10, 800),
('2023-01-02', 'Electronics', 'Headphones', 8, 30),
('2023-01-02', 'Accessories', 'Watch', 3, 120);

SELECT * FROM sales_data;

-- 1. Total revenue for each product category
SELECT 
    Product_Category,
    SUM(Sales_Quantity * Unit_Price) AS Total_Revenue
FROM sales_data
GROUP BY Product_Category
ORDER BY Total_Revenue DESC;

-- 2. Average sales quantity for each product category
SELECT 
    Product_Category,
    AVG(Sales_Quantity) AS Avg_Sales_Quantity
FROM sales_data
GROUP BY Product_Category
ORDER BY Avg_Sales_Quantity DESC;

-- 3. Product with the highest total revenue
SELECT 
    Product,
    SUM(Sales_Quantity * Unit_Price) AS Total_Revenue
FROM sales_data
GROUP BY Product
ORDER BY Total_Revenue DESC
LIMIT 1;

-- 4. For line chart data - sales quantity by date
SELECT 
    Date,
    SUM(Sales_Quantity) AS Daily_Sales_Quantity
FROM sales_data
GROUP BY Date
ORDER BY Date;



-- 5. Total revenue, cost, and profit for each day (cost = 60% of revenue)
SELECT 
    Date,
    SUM(Sales_Quantity * Unit_Price) AS Total_Revenue,
    SUM(Sales_Quantity * Unit_Price) * 0.6 AS Total_Cost,
    SUM(Sales_Quantity * Unit_Price) * 0.4 AS Profit
FROM sales_data
GROUP BY Date
ORDER BY Date;



-- Complete summary query combining multiple metrics
SELECT 
    Product_Category,
    SUM(Sales_Quantity * Unit_Price) AS Total_Revenue,
    AVG(Sales_Quantity) AS Avg_Sales_Quantity,
    SUM(Sales_Quantity) AS Total_Units_Sold,
    COUNT(*) AS Number_of_Transactions
FROM sales_data
GROUP BY Product_Category
ORDER BY Total_Revenue DESC;
