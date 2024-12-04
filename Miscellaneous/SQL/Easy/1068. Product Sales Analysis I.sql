-- https://leetcode.com/problems/product-sales-analysis-i/description/

-- Write your MySQL query statement below
select Product.product_name as product_name, Sales.year as year, Sales.price as price from Sales 
join Product on Sales.product_id = Product.product_id