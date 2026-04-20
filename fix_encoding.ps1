$path = "C:\Users\camil\Downloads\clo\index.html"
$bytes = [System.IO.File]::ReadAllBytes($path)
$c = [System.Text.Encoding]::UTF8.GetString($bytes)

# Fix all mojibake sequences
$c = $c.Replace("Ã¡","á")
$c = $c.Replace("Ã©","é")
$c = $c.Replace("Ã­","í")
$c = $c.Replace("Ã³","ó")
$c = $c.Replace("Ãº","ú")
$c = $c.Replace("Ã±","ñ")
$c = $c.Replace("Â·","·")
$c = $c.Replace("Â¿","¿")
$c = $c.Replace("Â¡","¡")
$c = $c.Replace("Ã‰","É")
$c = $c.Replace("Ã"","Ó")
$c = $c.Replace("Ãš","Ú")

# Write back as UTF-8 without BOM
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::WriteAllText($path, $c, $utf8NoBom)

Write-Host "Done. Checking Catalogo..."
$matches2 = [regex]::Matches($c, 'Cat.logo')
foreach ($m in $matches2) { Write-Host "  Found: $($m.Value)" }
if ($c.Contains("Ã")) { Write-Host "WARN: still has corrupted Ã chars" } else { Write-Host "OK: no corrupted chars" }
Write-Host "Lines: $(($c -split "`n").Count)"
