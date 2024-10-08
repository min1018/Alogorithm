SELECT FOOD_ORDER.PRODUCT_ID, PRODUCT_NAME, SUM(AMOUNT * PRICE) AS 'TOTAL_SALES'
FROM (SELECT * FROM FOOD_ORDER WHERE PRODUCE_DATE LIKE '2022-05%') AS FOOD_ORDER JOIN FOOD_PRODUCT ON FOOD_ORDER.PRODUCT_ID = FOOD_PRODUCT.PRODUCT_ID
GROUP BY FOOD_ORDER.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, PRODUCT_ID;