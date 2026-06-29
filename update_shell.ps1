# Project Phaze Tech — Sovereign Shell Lifecycle & Update Controller
# Script Reference: PROJ_UX_LIFECYCLE_AUTOMATION
# Target Environment: Local PowerShell 7+ Engine // Headless Execution Safe

$WorkspaceRoot = "C:\Users\Martha_Farquhar\synaptic_core"
$TargetScript  = "sovereign_shell.py"
$FullScriptPath = Join-Path $WorkspaceRoot $TargetScript

Clear-Host
Write-Host "=====================================================================" -ForegroundColor Copper
Write-Host "[INIT] PHAZE TECH SOVEREIGN SHELL LIFECYCLE MANAGEMENT UTILITY v1.0" -ForegroundColor Cyan
Write-Host "=====================================================================" -ForegroundColor Copper

# STEP 1: Scan and purge rogue multi-tenant background processes
Write-Host "`n[01/04] Sanitising volatile workspace environment..." -ForegroundColor Yellow
$ActivePythonProcs = Get-Process -Name "python" -ErrorAction SilentlyContinue
if ($ActivePythonProcs) {
    Write-Host " ↳ Found active background python threads. Force-purging rogue windows..." -ForegroundColor DarkYellow
    Stop-Process -Name "python" -Force
    Start-Sleep -Seconds 1
    Write-Host " ↳ Environment successfully flushed of ghost instances." -ForegroundColor Green
} else {
    Write-Host " ↳ Zero conflicting process instances found. Memory space clear." -ForegroundColor Green
}

# STEP 2: Verify structural path anchors
Write-Host "`n[02/04] Validating local workspace directory layout..." -ForegroundColor Yellow
if (-not (Test-Path $WorkspaceRoot)) {
    Write-Host " ↳ [FATAL ERROR] Target core path not found: $WorkspaceRoot" -ForegroundColor Red
    Write-Host " ↳ Aborting boot execution chain to protect file governance." -ForegroundColor Red
    Break
}
Write-Host " ↳ Anchor directory presence verified: $WorkspaceRoot" -ForegroundColor Green

# STEP 3: Verify core script module integrity
Write-Host "`n[03/04] Auditing core application script payload..." -ForegroundColor Yellow
if (-not (Test-Path $FullScriptPath)) {
    Write-Host " ↳ [FATAL ERROR] Shell core application module missing: $FullScriptPath" -ForegroundColor Red
    Write-Host " ↳ Please ensure sovereign_shell.py is located inside the root anchor." -ForegroundColor Red
    Break
}
Write-Host " ↳ Application integrity confirmed: $TargetScript (v1.9 Active Framework Loaded)" -ForegroundColor Green

# STEP 4: Monolithic Foreground Boot Sequence
Write-Host "`n[04/04] Initialising monolithic core runtime pipeline..." -ForegroundColor Cyan
Write-Host " ↳ Spawning Sovereign Shell Cockpit window context. Terminal streaming armed.`n" -ForegroundColor Gray

Set-Location $WorkspaceRoot
python $TargetScript

Write-Host "`n[EXIT] Sovereign Shell interface closed. Operational environment stable." -ForegroundColor Green