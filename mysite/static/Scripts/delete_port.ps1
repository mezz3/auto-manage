Param($pg_name)

Connect-viserver 10.0.15.39 -user Administrator@vsphere.local -password Qwerty1@#$ -WarningAction 0

Get-VirtualPortGroup -Name $pg_name | Remove-VirtualPortGroup -Confirm:$false