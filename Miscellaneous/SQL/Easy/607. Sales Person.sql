-- https://leetcode.com/problems/sales-person/description/

-- Write your MySQL query statement below
select SalesPerson.name as name from SalesPerson 
where SalesPerson.sales_id not in (
    select Orders.sales_id from Orders join Company on Company.com_id = Orders.com_id
    where Company.name = "RED"
)
