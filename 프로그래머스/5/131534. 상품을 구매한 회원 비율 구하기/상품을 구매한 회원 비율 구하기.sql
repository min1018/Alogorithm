SELECT YEAR(SALES_DATE) AS 'YEAR', MONTH(SALES_DATE) AS 'MONTH', 
COUNT(DISTINCT ONLINE_SALE.USER_ID) AS 'PURCHASED_USERS', 
ROUND(COUNT(DISTINCT ONLINE_SALE.USER_ID) / (SELECT COUNT(USER_ID)
                                FROM USER_INFO
                                WHERE JOINED LIKE '2021%') , 1) AS 'PUCHASED_RATIO'
FROM USER_INFO JOIN ONLINE_SALE ON USER_INFO.USER_ID = ONLINE_SALE.USER_ID
WHERE JOINED LIKE '2021%'
GROUP BY YEAR(SALES_DATE) , MONTH(SALES_DATE)
ORDER BY YEAR(SALES_DATE) , MONTH(SALES_DATE);
# 2021 전체 
# 2021 가입 중 구매 / 2021 전체 