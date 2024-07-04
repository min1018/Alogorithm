WITH VALUE AS (SELECT MEMBER_ID
              FROM REST_REVIEW 
              GROUP BY MEMBER_ID 
              ORDER BY COUNT(REVIEW_ID) DESC 
              LIMIT 1 )
SELECT MEMBER_NAME, REVIEW_TEXT, DATE_FORMAT(REVIEW_DATE, '%Y-%m-%d') as REVIEW_DATE
FROM MEMBER_PROFILE JOIN REST_REVIEW 
ON REST_REVIEW.MEMBER_ID = MEMBER_PROFILE.MEMBER_ID
WHERE REST_REVIEW.MEMBER_ID IN (SELECT MEMBER_ID 
                               FROM VALUE )
ORDER BY REVIEW_DATE, REVIEW_TEXT;
# 리뷰를 가장 많이 작성한 회원 -> 모든 리뷰 