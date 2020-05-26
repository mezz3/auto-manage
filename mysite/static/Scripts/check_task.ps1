# Param($vm_name, $pg_name)

Connect-viserver 10.0.15.39 -user Administrator@vsphere.local -password Qwerty1@#$ -WarningAction 0

get-task | ?{$_.name -like "CloneVm_Task"}