-- 코드를 작성해주세요
SELECT SUM(G.SCORE) AS SCORE, E.EMP_NO, E.EMP_NAME, E.POSITION, E.EMAIL
FROM HR_EMPLOYEES E JOIN HR_GRADE G
ON E.EMP_NO = G.EMP_NO
GROUP BY YEAR, E.EMP_NO
HAVING YEAR = '2022'
ORDER BY SCORE DESC
LIMIT 1