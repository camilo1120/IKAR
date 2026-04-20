with open(r'C:\Users\camil\Downloads\clo\index.html', 'rb') as f:
    raw = f.read()

# The corrupted star ★ appears as: \xc3\xa2\xcb\x9c\xe2\x80\xa6 (5 times for ★★★★★)
bad_star  = b'\xc3\xa2\xcb\x9c\xe2\x80\xa6'
good_star = '&#9733;'.encode('utf-8')

# Count before
count_before = raw.count(bad_star)
print(f'Corrupted star sequences found: {count_before}')

# Replace: 5 bad stars in a row → 5 good stars
bad_five  = bad_star * 5
good_five = good_star * 5
raw2 = raw.replace(bad_five, good_five)

# Also handle single ones that remain
raw2 = raw2.replace(bad_star, good_star)

count_after = raw2.count(bad_star)
count_good  = raw2.count(good_star)
print(f'Remaining corrupted: {count_after}')
print(f'Good star entities:  {count_good}')

# Now also fix other remaining corruption in text layer
text = raw2.decode('utf-8')

# Fix © copyright - appears as \xc2\xa9 which is correct UTF-8 for ©
# but if displayed wrong, replace with entity
text = text.replace('\u00a9', '&copy;')

# Fix ² (superscript 2) - appears as \xc2\xb2 - correct UTF-8
# Replace with HTML entity to be safe
text = text.replace('\u00b2', '&#178;')

# Fix ✅ emoji (U+2705) - triple-encoded probably
# Fix ➕ emoji (U+2795)  
# Fix emoji in admin panel titles - replace with text
text = text.replace('✅', '&#10003;')  # checkmark
text = text.replace('➕', '+')
text = text.replace('📋', '')
text = text.replace('🌐', '')

with open(r'C:\Users\camil\Downloads\clo\index.html', 'wb') as f:
    f.write(text.encode('utf-8'))

print('File written. Verifying...')
with open(r'C:\Users\camil\Downloads\clo\index.html', 'r', encoding='utf-8') as f:
    verify = f.read()
print(f'Star entities in final file: {verify.count("&#9733;")}')
print('ALL DONE')
