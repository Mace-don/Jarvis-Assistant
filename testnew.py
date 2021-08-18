import re

x = "Hello Jarvis"
pattern = re.compile('Jarvis|Wake up Jarvis|Hello Jarvis|Hi Jarvis')
search_result = pattern.search(x)
print(search_result)