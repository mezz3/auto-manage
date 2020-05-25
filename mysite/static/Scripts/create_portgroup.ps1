Param($pg_name, $pg_vlan)

Connect-viserver 10.0.15.39 -user Administrator@vsphere.local -password Qwerty1@#$ -WarningAction 0

$vportgroup =  New-VirtualPortGroup -VirtualSwitch vSwitch1 -Name $pg_name -VlanId $pg_vlan