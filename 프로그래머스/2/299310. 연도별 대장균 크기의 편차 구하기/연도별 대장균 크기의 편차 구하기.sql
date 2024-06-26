WITH VALUE AS (SELECT YEAR(DIFFERENTIATION_DATE) AS YEAR, MAX(SIZE_OF_COLONY) AS MAXIMUM
              FROM ECOLI_DATA
              GROUP BY YEAR(DIFFERENTIATION_DATE))
SELECT YEAR(ECOLI_DATA.DIFFERENTIATION_DATE) AS YEAR, (MAXIMUM - SIZE_OF_COLONY) AS YEAR_DEV, ID
FROM ECOLI_DATA JOIN VALUE ON VALUE.YEAR = YEAR(ECOLI_DATA.DIFFERENTIATION_DATE)
ORDER BY YEAR, YEAR_DEV;