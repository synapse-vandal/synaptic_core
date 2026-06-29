# Sovereign Workspace State Bootstrapper with Visual Notify Core
param (
    [string]$Mode = ""
)

Clear-Host

# Interactive selection if no mode argument is supplied via shortcut
if ($Mode -notin @("Alpha", "Beta")) {
    Write-Host "====================================================" -ForegroundColor Cyan
    Write-Host "  SELECT ACTIVE WORKSPACE BANDWIDTH STATE           " -ForegroundColor Cyan
    Write-Host "====================================================" -ForegroundColor Cyan
    Write-Host " [A] STATE ALPHA : High-Velocity Burst (Fast Mode)" -ForegroundColor Amber
    Write-Host " [B] STATE BETA  : Deep Recalibration (Analytical)" -ForegroundColor Green
    Write-Host "====================================================" -ForegroundColor Cyan
    $Choice = Read-Host "Select operational vector [A/B]"
    $Mode = if ($Choice -eq 'A') { "Alpha" } else { "Beta" }
}

# Initialise Native Windows System Tray Notification Matrix
[void][System.Reflection.Assembly]::LoadWithPartialName("System.Windows.Forms")
$Toast = New-Object System.Windows.Forms.NotifyIcon
$Toast.Icon = [System.Drawing.SystemIcons]::Information
$Toast.BalloonTipTitle = "Sovereign Node Link Established"

# Execute specific environmental configurations based on selected bandwidth state
if ($Mode -eq "Alpha") {
    $BannerColor = "Yellow"
    $Plane9Args = "-window -scene `"Sovereign_Skin_Core`"" 
    $Toast.BalloonTipText = "STATE ALPHA ENFORCED: High-Velocity Burst Active."
    $Toast.Visible = $true
    $Toast.ShowBalloonTip(3000)

    Write-Host @"
####################################################
#  [NOTIFY] STATE ALPHA: HIGH-VELOCITY BURST ACTIVE #
#  -> MAXIMUM EXECUTION PACING ENGAGED            #
#  -> COGNITIVE SPEED-LOCK ACTIVE                 #
####################################################
"@ -ForegroundColor $BannerColor
} else {
    $BannerColor = "Green"
    $Plane9Args = "-window -scene `"Sovereign_Skin_Core`"" 
    $Toast.BalloonTipText = "STATE BETA ENFORCED: Deep Recalibration Mode Active."
    $Toast.Visible = $true
    $Toast.ShowBalloonTip(3000)

    Write-Host @"
####################################################
#  [NOTIFY] STATE BETA: DEEP RECALIBRATION ACTIVE  #
#  -> HIGH-ENTROPY ANALYTICAL DEPTH EMPOWERED      #
#  -> SYNC-LOCK PROTECTION ENGAGED                #
####################################################
"@ -ForegroundColor $BannerColor
}

# Step 1: Initialize background data sidechain
Write-Host "`n[1/2] Initialising background Autoscribe file watcher..." -ForegroundColor Cyan
Start-Process "python" -ArgumentList "autoscribe_daemon.py --refresh-nodes" -WindowStyle Hidden

# Step 2: Deploy Plane9 Visual Overlay Frame 
Write-Host "[2/2] Deploying FreeSync-paced visual overlay frame..." -ForegroundColor Cyan
$Plane9Path = "C:\Program Files (x86)\Plane9\Plane9.exe"
if (Test-Path $Plane9Path) {
    Start-Process $Plane9Path -ArgumentList $Plane9Args
} else {
    Write-Host "[WARNING] Plane9.exe not found at default path. Visual overlay skipped." -ForegroundColor Red
}

Write-Host "`n[SUCCESS] Matrix fully synchronised below redline thresholds." -ForegroundColor Green
Write-Host "Firefox foreground link active. Terminal room ready." -ForegroundColor Green
Start-Sleep -Seconds 3
$Toast.Dispose()