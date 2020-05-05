Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false
Connect-viserver 10.0.15.39 -user Administrator@vsphere.local -password Qwerty1@#$ -WarningAction 0