$exclude = @("venv", "Exemplo_1.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "Exemplo_1.zip" -Force