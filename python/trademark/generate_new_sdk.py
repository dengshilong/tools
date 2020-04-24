import re


names = []
with open('name.txt', encoding='utf-8') as f:
    names = [line.strip() for line in f]

with open('new_sdk.js', 'w') as new_f:
    with open('sdk.js') as f:
        for line in f:
            t = re.search(r'_\$dM\[(\d+)\]', line)
            while t:
                index = int(t.group(1))
                line = re.sub(r'_\$dM\[(\d+)\]', '"{}"'.format(names[index]), line)
                t = re.search(r'_\$dM\[(\d+)\]', line)
            new_f.write(line)
