SELECT YEAR(SALES_DATE) AS 'YEAR', MONTH(SALES_DATE) AS 'MONTH', GENDER, COUNT(DISTINCT ONLINE_SALE.USER_ID) AS 'USERS'
FROM USER_INFO JOIN ONLINE_SALE ON USER_INFO.USER_ID = ONLINE_SALE.USER_ID
GROUP BY YEAR, MONTH, GENDER 
HAVING GENDER IS NOT NULL
ORDER BY YEAR, MONTH, GENDER 