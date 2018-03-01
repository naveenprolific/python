import re

randstr="https://www.youtube.com http://www.google.com"

regex = re.compile(r"(https?://([\w.]+))")
ranstr = re.sub(regex,r"<a href='\1'>\2</a>",randstr)

print(ranstr,"\n")
