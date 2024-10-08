SELECT ITEM_INFO.ITEM_ID, ITEM_NAME, RARITY
FROM ITEM_INFO LEFT JOIN 
(SELECT ITEM_ID, IFNULL(PARENT_ITEM_ID,-1) AS 'PARENT_ITEM_ID' 
 FROM ITEM_TREE) AS ITEM_TREE ON ITEM_INFO.ITEM_ID = ITEM_TREE.PARENT_ITEM_ID
WHERE ITEM_TREE.PARENT_ITEM_ID IS NULL
ORDER BY ITEM_ID DESC;