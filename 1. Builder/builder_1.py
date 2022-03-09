words = ['hello', 'park']
parts = ['<ul>']

for w in words:
    parts.append(f' <li>{w}</li>')

parts.append('</ul>')
print('\n'.join(parts))

