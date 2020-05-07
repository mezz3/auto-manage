Param($vm_name)

Connect-viserver 10.0.15.39 -user Administrator@vsphere.local -password Qwerty1@#$ -WarningAction 0

Remove-VM $vm_name -DeletePermanently -Confirm:$false