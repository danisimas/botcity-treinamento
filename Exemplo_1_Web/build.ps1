$exclude = @("venv", "Exemplo_1_Web.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "Exemplo_1_Web.zip" -Force