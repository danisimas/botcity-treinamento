$exclude = @("venv", "Bot_Youtube.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "Bot_Youtube.zip" -Force