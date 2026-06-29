$AliasPayload = @"
if (Test-Path ".\Invoke-SovereignAudit.ps1") {
    & ".\Invoke-SovereignAudit.ps1"
} else {
    Write-Host "[ERROR] Master audit engine script missing from current path." -ForegroundColor Red
}
"@
$AliasPayload | Out-File -FilePath ".\rcbe.ps1" -Encoding UTF8 -Force
Write-Host "[DONE] Audit loop shortcut successfully short-bound to .\rcbe.ps1" -ForegroundColor Green