Param($pg_name)

Connect-viserver 10.0.15.39 -user Administrator@vsphere.local -password Qwerty1@#$ -WarningAction 0
Get-VM | where { ($_ | Get-NetworkAdapter | where { $_.networkname -match $pg_name })} | select Name, PowerState