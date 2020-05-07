Param([int]$vm_count, [int]$count)

$vCenter="10.0.15.39"
$vCenterUser="Administrator@vsphere.local"
$vCenterUserPassword="Qwerty1@#$"

$clone = "GNS3 VM"

$Cluster = "10.0.10.20"

$VM_prefix = "gns3vm-"

$check = $vm_count+$count
# Connect-viserver 10.0.15.39 -user Administrator@vsphere.local -password Qwerty1@#$ -WarningAction 0
write-host "Connecting to vCenter Server $vCenter" -foreground green
Connect-viserver $vCenter -user $vCenterUser -password $vCenterUserPassword -WarningAction 0

For ($i=$count; $i -le $check-1; $i++) {
    $VM_name = $VM_prefix + $i
    Get-VMHost -state connected | Get-Random
    write-host "Creation of VM $VM_name initiated" -foreground green
    New-VM -Name $VM_Name -VM $clone -VMHost $Cluster -DiskStorageFormat Thin -RunAsync
}