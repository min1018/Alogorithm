select year(sales_date) as year, month(sales_date) as month, gender, count(distinct sale.user_id) as users 
from user_info as info join online_sale as sale 
on info.user_id = sale.user_id 
group by year, month, gender
having gender is not null
order by year, month, gender;
