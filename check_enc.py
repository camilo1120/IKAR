path = r'C:\Users\camil\Downloads\clo\index.html'
with open(path,'r',encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
# Find and print lines with Catalogo
for i, line in enumerate(lines, 1):
    if 'logo de Apartamentos' in line or 'Catálogo' in line:
        print(f'Line {i}: {line.strip()[:120]}')

# verify the á character
idx = text.find('Catálogo')
if idx >= 0:
    print(f'\nFound Catálogo at position {idx}')
    print('ENCODING IS CORRECT')
else:
    print('\nCatálogo NOT found - checking alternatives...')
    idx2 = text.find('Cat')
    if idx2 >= 0:
        snippet = text[idx2:idx2+10]
        print(f'Found Cat at {idx2}: {repr(snippet)}')
        # Show unicode code points
        for c in snippet:
            print(f'  U+{ord(c):04X} = {c}')
