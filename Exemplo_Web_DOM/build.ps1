$exclude = @("venv", "Exemplo_Web_1.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "Exemplo_Web_1.zip" -Force