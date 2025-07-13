SELECT * FROM pardavimai.`sales_data.csv`;

/*Sales per region*/

SELECT Region, SUM(Sales_Amount) as Total_Sales
FROM pardavimai.`sales_data.csv`
GROUP BY Region
ORDER BY Total_Sales DESC;


/*Profit by Product Category*/

SELECT Product_Category,
       SUM((Unit_Price - Unit_Cost) * Quantity_Sold) AS Profit
FROM pardavimai.`sales_data.csv`
GROUP BY Product_Category
ORDER BY Profit DESC;


/*Sales per month*/

SELECT DATE_FORMAT(Sale_Date, '%Y-%m') AS Month,
       SUM(Sales_Amount) AS Total_Sales
FROM pardavimai.`sales_data.csv`
GROUP BY Month
ORDER BY Month;


/*How many sales occurred through channels (e-commerce, physical sales, etc.)*/

SELECT Sales_Channel, COUNT(*) AS Num_Transactions, SUM(Sales_Amount) AS Total_Sales
FROM pardavimai.`sales_data.csv`
GROUP BY Sales_Channel
ORDER BY Total_Sales DESC;


/*Comparison of returning and new customers*/

SELECT Customer_Type, COUNT(*) AS Transactions, SUM(Sales_Amount) AS Total_Sales
FROM pardavimai.`sales_data.csv`
GROUP BY Customer_Type;






