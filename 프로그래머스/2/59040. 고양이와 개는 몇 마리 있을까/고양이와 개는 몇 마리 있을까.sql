-- 코드를 입력하세요
SELECT ANIMAL_TYPE, COUNT(ANIMAL_ID) as count
FROM ANIMAL_INS AS INS 
GROUP BY ANIMAL_TYPE 
ORDER BY ANIMAL_TYPE;
