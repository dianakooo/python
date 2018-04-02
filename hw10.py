import re

with open("einstein.html", encoding = "utf-8") as f:
    text = f.read()

match = re.search('Научная сфера</th><td>\n(.*?)title="(.*)"', text)
if match:
    sphere = match.group(2)

with open("result.txt", "w", encoding = "utf-8") as a:
    a.write(sphere)
