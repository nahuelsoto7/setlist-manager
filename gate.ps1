Write-Host "EJECUTANDO GATE DE VERIFICACION"
Write-Host "--------------------------------"
py -3 -m unittest discover -s tests
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Los tests fallaron"
    Write-Host "BLOQUEADO: Arregla el codigo y volve a correr"
    exit 1
} else {
    Write-Host "OK: Todos los tests pasaron"
    exit 0
}