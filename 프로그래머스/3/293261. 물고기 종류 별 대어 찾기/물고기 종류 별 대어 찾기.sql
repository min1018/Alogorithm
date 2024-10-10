select id, fish_name, length
from fish_info join fish_name_info on fish_info.fish_type = fish_name_info.fish_type 
where (fish_info.fish_type, length) in (select fish_type, max(length) 
                      from fish_info
                      group by fish_type)