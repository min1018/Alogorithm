-- 코드를 입력하세요
SELECT count(USER_ID) as USERS 
FROM USER_INFO
WHERE AGE BETWEEN 20 and 29 and JOINED like '2021%';