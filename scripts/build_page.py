# Run from the repository root: python3 scripts/build_page.py
s = open('scripts/template.html').read()
p = (s.replace('__DATA__', open('data/data.json').read().replace('</', '<\\/'))
      .replace('__GEO__', open('data/geo.json').read())
      .replace('__ASP__', open('data/asp.json').read().replace('</', '<\\/')))
open('index.html', 'w').write(p)
print('index.html', len(p) // 1024, 'KB')
