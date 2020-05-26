Param($vm_os, $vm_name)

$Cluster = "10.0.10.20"

Connect-viserver 10.0.15.39 -user Administrator@vsphere.local -password Qwerty1@#$ -WarningAction 0

New-VM -Name $vm_name -VM $vm_os -VMHost $Cluster -DiskStorageFormat Thin -RunAsync