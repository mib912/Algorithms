-- 코드를 작성해주세요

SELECT fi.ID as ID, fni.fish_name as FISH_NAME, fi.LENGTH as LENGTH
FROM fish_info fi JOIN fish_name_info fni
ON fi.fish_type = fni.fish_type
WHERE fi.fish_type IN (select fish_type
                      from fish_info
                      group by fish_type
                      having length = max(length)
                )
ORDER BY ID ASC