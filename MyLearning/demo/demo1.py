import re

text = "马云创立了阿里巴巴"
pattern = r"(.+?)创立了(.+?)"
match = re.search(pattern, text)
if match:
    print(f"创始人: {match.group(1)}, 公司: {match.group(2)}")