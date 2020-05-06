$vCenter="10.0.15.39"
$vCenterUser="Administrator@vsphere.local"
$vCenterUserPassword="Qwerty1@#$"

$vm_count = 5

$clone = "GNS3 VM"

$Cluster = "10.0.10.20"

$VM_prefix = "gns3vm-"

write-host "Connecting to vCenter Server $vCenter" -foreground green
Connect-viserver $vCenter -user $vCenterUser -password $vCenterUserPassword -WarningAction 0
# $vm_count | foreach {
# $y="{0:D1}" -f + $_
# $VM_name= $VM_prefix + $y
# Get-VMHost -state connected | Get-Random
# write-host "Creation of VM $VM_name initiated" -foreground green
# New-VM -Name $VM_Name -VM $clone -VMHost $Cluster -DiskStorageFormat Thin -RunAsync
# }
For ($i=1; $i -le $vm_count; $i++) {
    $VM_name= $VM_prefix + $i
    Get-VMHost -state connected | Get-Random
    write-host "Creation of VM $VM_name initiated" -foreground green
    New-VM -Name $VM_Name -VM $clone -VMHost $Cluster -DiskStorageFormat Thin -RunAsync
}

# $vCenter="10.0.15.39"
# $vCenterUser="Administrator@vsphere.local"
# $vCenterUserPassword="Qwerty1@#$"

# $vm_count = "2"

# $clone = "GNS3 VM"

# $Cluster = "10.0.10.20"

# $VM_prefix = "gns3vm-"

# $exists = 'already exists'

# write-host "Connecting to vCenter Server $vCenter" -foreground green
# Connect-viserver $vCenter -user $vCenterUser -password $vCenterUserPassword -WarningAction 0
# 1..$vm_count | foreach {
# $y="{0:D1}" -f + $_
# $VM_name= $VM_prefix + $y
# Get-VMHost -state connected | Get-Random
#     if ($exists) {
#         $integer = [int]$y
#         $VM_name = $VM_prefix + ($integer+1)
#         write-host "Creation of VM $VM_name initiated" -foreground green
#         New-VM -Name $VM_Name -VM $clone -VMHost $Cluster -DiskStorageFormat Thin -RunAsync
#     }
#     else {
#         write-host "Creation of VM $VM_name initiated" -foreground green
#         New-VM -Name $VM_Name -VM $clone -VMHost $Cluster -DiskStorageFormat Thin -RunAsync
#     }
# }