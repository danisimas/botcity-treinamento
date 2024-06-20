$exclude = @("venv", "Exemplo_2.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "Exemplo_2.zip" -Force