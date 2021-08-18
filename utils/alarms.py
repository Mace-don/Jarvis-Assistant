import re


voice_input = "set an alarm for 01:00 Midnight "
date = "(^|[^0-9a-z])([0-9][0-9])(^|[^0-9a-z])"
days = "(^|[^0-9a-z])(Mon|Monday|Tue|Tuesday|Wed|Wednesday|Thu|Thursday|Fri|Friday|Sat|Saturday|Sun|Sunday)(^|[" \
       " ^0-9a-z]) "
month = "(^|[^0-9a-z])(Jan|January|Feb|February|Mar|March|Apr|April|Jun|June|Aug|August|Sep|September|Oct|October|Nov" \
        "|November|Dec|December)(^|[^0-9a-z]) "


def match(string,regex):
    compiled = re.compile(regex)
    result = compiled.search(string)
    return result.group()

print(match(voice_input,date))

