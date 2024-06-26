SELECT SUM(SCORE) AS SCORE, HR_EMPLOYEES.EMP_NO, EMP_NAME, POSITION, EMAIL
FROM HR_EMPLOYEES JOIN HR_DEPARTMENT ON HR_EMPLOYEES.DEPT_ID = HR_DEPARTMENT.DEPT_ID JOIN HR_GRADE ON HR_EMPLOYEES.EMP_NO = HR_GRADE.EMP_NO
GROUP BY EMP_NO
ORDER BY SUM(SCORE) DESC
LIMIT 1;
