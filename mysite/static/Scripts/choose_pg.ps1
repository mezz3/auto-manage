Param($vm_name, $pg_name)

Connect-viserver 10.0.15.39 -user Administrator@vsphere.local -password Qwerty1@#$ -WarningAction 0

Get-vm "$vm_name" | Get-NetworkAdapter | Set-NetworkAdapter -NetworkName "$pg_name" -Confirm:$false