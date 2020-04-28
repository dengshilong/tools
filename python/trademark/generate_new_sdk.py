import re


names = []
with open('name.txt', encoding='utf-8') as f:
    names = [line.strip() for line in f]

with open('new_sdk.js', 'w') as new_f:
    with open('sdk.js') as f:
        for line in f:
            s = r'_\$5U\[(\d+)\]'
            t = re.search(s, line)
            while t:
                index = int(t.group(1))
                line = re.sub(s, '"{}"'.format(names[index]), line)
                t = re.search(s, line)
            new_f.write(line)
