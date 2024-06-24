import requests
from datetime import datetime

# 获取当前日期
today = datetime.today().strftime('%Y%m%d')
year = datetime.today().strftime('%Y')
month_day = datetime.today().strftime('%m%d')

# 图片 URL
url = f"https://img.owspace.com/Public/uploads/Download/{year}/{month_day}.jpg"

# 保存路径
filename = f"images/{today}.jpg"

# 下载图片
response = requests.get(url)
if response.status_code == 200:
    with open(filename, 'wb') as file:
        file.write(response.content)
    print(f"Image saved as {filename}")
else:
    print(f"Failed to retrieve image. Status code: {response.status_code}")
