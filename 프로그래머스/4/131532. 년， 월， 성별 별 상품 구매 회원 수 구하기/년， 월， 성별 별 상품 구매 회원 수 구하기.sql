-- 코드를 입력하세요
SELECT YEAR(SALES_DATE) AS YEAR, MONTH(SALES_DATE) AS MONTH, GENDER, COUNT(DISTINCT U.USER_ID) AS USERS
FROM USER_INFO U, ONLINE_SALE S
WHERE U.USER_ID = S.USER_ID
AND U.GENDER IS NOT NULL
AND U.USER_ID IN (SELECT A.USER_ID
                 FROM USER_INFO A, ONLINE_SALE B
                 WHERE A.USER_ID = B.USER_ID
                 AND A.JOINED <= SALES_DATE)
GROUP BY YEAR, MONTH, GENDER
ORDER BY YEAR,MONTH,GENDER


