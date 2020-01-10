import requests
import json
import re
import os
url = "https://images.dmzj.com/b/蝙蝠侠-8354/第52卷/JOJO_Batman_052_000a.jpg"
heads = {
    'Referer': 'https://manhua.dmzj.com/bianfuxianew52/',
    'cookle':'show_tip_1=0; display_mode=0; pt_198bb240=uid=edOEM6GYeqO4gKBq0KblYg&nid=0&vid=JvLvpalHPJIX-RJtcFWA-A&vn=2&pvn=1&sact=1553756426909&to_flag=1&pl=J8gHIAMoYA2Eg1lD2m4zWQ*pt*1553756146653',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
urls = [ 'https://images.dmzj.com/b/\\u8759\\u8760\\u4fa0-8354/51/JOJO_Batman_051_000b.jpg', 'https://images.dmzj.com/b/\\u8759\\u8760\\u4fa0-8354/51/JOJO_Batman_051_001.jpg', 'https://images.dmzj.com/b/\\u8759\\u8760\\u4fa0-8354/51/JOJO_Batman_051_002.jpg', 'https://images.dmzj.com/b/\\u8759\\u8760\\u4fa0-8354/51/JOJO_Batman_051_003.jpg', 'https://images.dmzj.com/b/\\u8759\\u8760\\u4fa0-8354/51/JOJO_Batman_051_004.jpg', 'https://images.dmzj.com/b/\\u8759\\u8760\\u4fa0-8354/51/JOJO_Batman_051_005.jpg', 'https://images.dmzj.com/b/\\u8759\\u8760\\u4fa0-8354/51/JOJO_Batman_051_006.jpg', 'https://images.dmzj.com/b/\\u8759\\u8760\\u4fa0-8354/51/JOJO_Batman_051_007.jpg', 'https://images.dmzj.com/b/\\u8759\\u8760\\u4fa0-8354/51/JOJO_Batman_051_008.jpg', 'https://images.dmzj.com/b/\\u8759\\u8760\\u4fa0-8354/51/JOJO_Batman_051_009.jpg', 'https://images.dmzj.com/b/\\u8759\\u8760\\u4fa0-8354/51/JOJO_Batman_051_010.jpg', 'https://images.dmzj.com/b/\\u8759\\u8760\\u4fa0-8354/51/JOJO_Batman_051_011.jpg', 'https://images.dmzj.com/b/\\u8759\\u8760\\u4fa0-8354/51/JOJO_Batman_051_012.jpg', 'https://images.dmzj.com/b/\\u8759\\u8760\\u4fa0-8354/51/JOJO_Batman_051_013.jpg', 'https://images.dmzj.com/b/\\u8759\\u8760\\u4fa0-8354/51/JOJO_Batman_051_014.jpg', 'https://images.dmzj.com/b/\\u8759\\u8760\\u4fa0-8354/51/JOJO_Batman_051_015.jpg', 'https://images.dmzj.com/b/\\u8759\\u8760\\u4fa0-8354/51/JOJO_Batman_051_016.jpg', 'https://images.dmzj.com/b/\\u8759\\u8760\\u4fa0-8354/51/JOJO_Batman_051_017.jpg', 'https://images.dmzj.com/b/\\u8759\\u8760\\u4fa0-8354/51/JOJO_Batman_051_018.jpg']
a = []
f = requests.get(url,headers=heads,verify=False)
print(f.status_code)