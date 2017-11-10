# -*- coding: utf-8 -*- 
#Hora=28, si h>30, 3% mas por h extra

while True:
    print "------------------------------------"
    horas=input("Horas trabajadas> ")
    if(horas<=30):
        pago=horas*28
     
        print "Pago total= $"+`pago`
    else:
        pago=horas*28
        extras=horas-30
        pago=pago+(extras*28*0.03)
        print "Horas extras: "+`extras`
        print "Pago h. extras= $"+`(extras*28*1.03)`
        print "Pago total= $"+`pago`




