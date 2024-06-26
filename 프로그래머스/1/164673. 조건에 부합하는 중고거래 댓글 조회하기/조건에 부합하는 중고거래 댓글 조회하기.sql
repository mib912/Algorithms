-- 코드를 입력하세요
SELECT UGB.TITLE, UGB.BOARD_ID, UGR.REPLY_ID, UGR.WRITER_ID, UGR.CONTENTS, DATE_FORMAT(UGR.CREATED_DATE, '%Y-%m-%d') as CREATED_DATE
FROM USED_GOODS_BOARD UGB, USED_GOODS_REPLY UGR
WHERE UGB.BOARD_ID = UGR.BOARD_ID
AND UGB.CREATED_DATE LIKE '2022-10%'
ORDER BY UGR.CREATED_DATE, UGB.TITLE