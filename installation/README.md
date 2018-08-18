# Bemerkungen zur Installation auf Acer-Laptops und zur W-Lan Einrichtung

## W-Lan

Da das Netz ITMC-WPA2 am 01.10.18 abgeschaltet werden soll(te), hier die Einstellungen für eduroam.
 - Wi-Fi security: WPA- & WPA2-Enterprise
 - Authentication: Geschütztes EAP (PEAP)
 - Anonymous Identity: telesec@tu-dortmund.de
 - Domain: tu-dortmund.de
 - CA-Zertifikat: T-TeleSec_GlobalRoot_Class_2.crt
    - zu finden in usr/share/ca-certificates/mozilla/T-TeleSec_GlobalRoot_Class_2.crt
 - PEAP-Version: Automatisch
 - Inner authentication: MSCHAPv2
 - Username: smxxxx@udo.edu
 - Passwort: *******


## Acer-Installation
Acer ist der Ansicht, dass nur von Ihnen ausgesuchte Betribessysteme bootfähig sein sollen.
Da das vor allem im Dualboot mit Windows und Unix-OS zu Problemen führt, hier zusammengefasst was man machen kann. Der erste Weg funktioniert bei einer Platte, oder mehreren Platten, wenn die EFI-Partition auf der ersten Platte liegt. Dann klappt es auch bei einer Dualboot-Installation.

Quelle: https://wiki.ubuntuusers.de/EFI_Problembehebung/, abgerufen 15.08.18

### 1. Weg
Vor der Installation:
 - UEFI mit `F2` aufrufen
 - Touchpadmodus auf **Basic** stellen
 - `Security` → `Set Supervisor Password`
    - Vorschlag *passwort*, wird nach der Installtaion wieder entfernt
 - `Boot`
    - Modus: **UEFI**
    - Secure Boot: **enabled**
 - mit `F10` und *yes* verlassen

Die Installation läuft wie gewohnt ab.

Nach der Installation, beim ersten Start:
 - UEFI mit `F2` aufrufen
 - Passwort eingeben, z.B. *passwort*
 - `Security` → `Select an UEFI file as trusted for executing`
 - `HDD0` → `EFI` → `<ubuntu>` → `shimx64.efi`
 - Supervisor Password wieder entfernen
 - mit `F10` und *yes* verlassen

### 2. Weg

Diesen Weg habe ich nicht selber getestet, er hat letztes Jahr, 2017, wohl funktioniert.

Link: https://askubuntu.com/questions/627416/acer-aspire-e15-will-not-dual-boot, abgerufen 15.08.2018
