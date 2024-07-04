SELECT REST_INFO.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, ROUND(AVG(REVIEW_SCORE), 2) AS 'SCORE' 
FROM REST_INFO JOIN REST_REVIEW ON REST_INFO.REST_ID = REST_REVIEW.REST_ID
WHERE ADDRESS LIKE '서울%'
GROUP BY REST_ID 
ORDER BY SCORE DESC, FAVORITES DESC;

# 리뷰 평균 점수 -> 세자리 반올림 
# 평균 내림, 즐겨찾기 내림 