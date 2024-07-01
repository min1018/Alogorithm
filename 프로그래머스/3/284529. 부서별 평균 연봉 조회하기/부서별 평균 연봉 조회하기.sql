-- 코드를 작성해주세요
SELECT HR_DEPARTMENT.DEPT_ID, DEPT_NAME_EN, ROUND(AVG(SAL),0) AS AVG_SAL
FROM HR_EMPLOYEES JOIN HR_DEPARTMENT ON HR_EMPLOYEES.DEPT_ID = HR_DEPARTMENT.DEPT_ID 
GROUP BY HR_DEPARTMENT.DEPT_ID
ORDER BY AVG(SAL) DESC;