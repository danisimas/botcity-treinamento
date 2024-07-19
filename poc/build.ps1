$exclude = @("venv", "poc.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "poc.zip" -Force