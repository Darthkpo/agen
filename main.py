import time
import sys
from random import randint

print "Generador de actas v1.0 - fsociety"

date = time.strftime("%d/%m/%Y")

hra_str_h = int(time.strftime("%H"))
hra_str_m = int(time.strftime("%M"))
hra_str_s = int(time.strftime("%S"))

hra_end_h = int(time.strftime("%H")) + randint(0,1)
hra_end_m = int(time.strftime("%M")) + randint(30,55)
hra_end_s = int(time.strftime("%S")) + randint(0,59)

if hra_str_s + hra_end_s >= 59 :
	hra_end_s = abs(hra_str_s - hra_end_s)
	hra_end_m += 1

if hra_str_m + hra_end_m >= 59 :
	hra_end_m = abs(hra_str_m - hra_end_m)
	hra_end_h += 1

hra_str = "%02d:%02d:%02d" % (hra_str_h,hra_str_m,hra_str_s)
hra_end = "%02d:%02d:%02d" % (hra_end_h,hra_end_m,hra_end_s)


asistentes = [ "Nicolas Aguirre", "Facundo Winter", "Guillermo Rodriguez" ]
if "-nomaxi" not in sys.argv:
	asistentes.append("Maximiliano Bizera")

print "FECHA: " + date
print "HRA COMIENZO: " + hra_str
print "HRA FINALIZACION: " + hra_end
print "ASISTENTES: "
for persona in asistentes:
	print "    " + persona
