$exclude = @("venv", "Exemplo_Web_SSl.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "Exemplo_Web_SSl.zip" -Force