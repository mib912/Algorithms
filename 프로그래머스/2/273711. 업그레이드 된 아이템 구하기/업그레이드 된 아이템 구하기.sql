-- 코드를 작성해주세요

select i.item_id, i.item_name, i.rarity
from item_info i, item_tree t
where i.item_id = t.item_id
and t.parent_item_id in (
    select ii.item_id
    from item_info ii
    where ii.rarity = 'RARE'
)
order by i.item_id desc