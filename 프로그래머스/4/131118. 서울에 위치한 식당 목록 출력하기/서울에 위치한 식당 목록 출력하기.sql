SELECT REST_REVIEW.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, ROUND(AVG(REVIEW_SCORE) ,2) AS 'SCORE'
FROM (SELECT * FROM REST_INFO WHERE ADDRESS LIKE '서울%') AS REST_INFO JOIN REST_REVIEW ON REST_INFO.REST_ID = REST_REVIEW.REST_ID
GROUP BY REST_ID
ORDER BY SCORE DESC, FAVORITES DESC;