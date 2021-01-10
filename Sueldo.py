
print('Jornal diario')


Día=(input('Ingrese el día que trabajo: ' ))
Turno=input('Ingrese el turno que trabajo (Diurno o Nocturno): ')

if(Día=='Domingo' or 'domingo'):
    h=float(input('Ingrese horas trabajadas: '))
if(Turno=='Diurno' or Turno=='diurno' and h<=40):
    jornal=h*100
    print('Su jornal es de: ', jornal)
elif(Turno=='Nocturno' or Turno=='nocturno' and h<=40):
    jornal=h*200
    print('Su jornal es de: ', jornal)
elif(Turno=='Diurno' or Turno=='diurno' and 48>h>48):
    jornal=40*100 + (h-40)*200
    print('Su jornal es de: ', jornal)
elif(Turno=='Diurno' or Turno=='diurno' and h>48):
    jornal=40*100 + 8*200 + (h-40)*300
    print('Su jornal es de: ', jornal)
elif(Turno=='Nocturno' or Turno=='nocturno' and h>48):
    jornal=40*200 + 8*400 + (h-40)*600
    print('Su jornal es de: ', jornal)

if(Día!='Domingo' or Turno=='domingo'):
    h=float(input('Ingrese horas trabajadas: '))
elif(Turno=='Diurno' or Turno=='diurno' and h<=40):
    jornal=h*40
    print('Su jornal es de: ', jornal)
elif(Turno=='Nocturno' or Turno=='nocturno' and h<=40):
    jornal=h*100
    print('Su jornal es de: ', jornal)
elif(Turno=='Diurno' or Turno=='diurno' and 48>h>48):
    jornal=40*40 + (h-40)*80
    print('Su jornal es de: ', jornal)
elif(Turno=='Diurno' or Turno=='diurno' and h>48):
    jornal=40*40 + 8*80 + (h-40)*120
    print('Su jornal es de: ', jornal)
elif(Turno=='Nocturno' or Turno=='nocturno' and h>48):
    jornal=40*100 + 8*200 + (h-48)*300
    print('Su jornal es de: ', jornal)
else:
    print('Fin del proceso')




