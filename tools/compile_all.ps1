param(
    [Parameter(Mandatory = $true)]
    [string]$SannyRoot,

    [string]$OutputDirectory = ".validation-cache/compiled",

    [switch]$SkipModelAliasFiles
)

$ErrorActionPreference = "Stop"
$Workspace = Split-Path -Parent $PSScriptRoot
$Sanny = Join-Path $SannyRoot "sanny.exe"

if (-not (Test-Path $Sanny)) {
    throw "sanny.exe was not found at $Sanny"
}

$OutputDirectory = Join-Path $Workspace $OutputDirectory
if (Test-Path $OutputDirectory) {
    Remove-Item $OutputDirectory -Recurse -Force
}
New-Item $OutputDirectory -ItemType Directory | Out-Null

$SourceFiles = @()
foreach ($directory in @("examples", "scripts")) {
    $path = Join-Path $Workspace $directory
    if (Test-Path $path) {
        $SourceFiles += Get-ChildItem $path -Filter "*.txt" -File | Sort-Object FullName
    }
}

$Failures = @()
$Compiled = 0
$Skipped = 0

foreach ($source in $SourceFiles) {
    $text = Get-Content $source.FullName -Raw
    if ($SkipModelAliasFiles -and $text -match '#[A-Za-z_][A-Za-z0-9_]*') {
        Write-Host "SKIP model aliases: $($source.FullName)"
        $Skipped += 1
        continue
    }

    $relative = [IO.Path]::GetRelativePath($Workspace, $source.FullName)
    $relativeDirectory = Split-Path $relative -Parent
    $targetDirectory = Join-Path $OutputDirectory $relativeDirectory
    New-Item $targetDirectory -ItemType Directory -Force | Out-Null

    $extension = if ($text -match '\{\$CLEO\s+\.cm\}') { ".cm" } else { ".cs" }
    $target = Join-Path $targetDirectory ($source.BaseName + $extension)
    $compileLog = Join-Path $SannyRoot "compile.log"
    if (Test-Path $compileLog) {
        Remove-Item $compileLog -Force
    }

    Write-Host "COMPILE $relative"
    & $Sanny --compile $source.FullName $target --no-splash --mode sa_sbl `
        -o Compiler::CheckConditions 1 `
        -o Compiler::CheckLocalVariables 1

    if ($LASTEXITCODE -ne 0 -or -not (Test-Path $target)) {
        $log = if (Test-Path $compileLog) { Get-Content $compileLog -Raw } else { "No compile.log" }
        $Failures += "$relative`n$log"
        continue
    }
    $Compiled += 1
}

Write-Host "Compiled: $Compiled; skipped: $Skipped; failed: $($Failures.Count)"
if ($Compiled -eq 0) {
    throw "No source files were compiled."
}
if ($Failures.Count -gt 0) {
    $Failures | ForEach-Object { Write-Error $_ }
    exit 1
}
