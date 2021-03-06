from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from django.conf import settings
import base64
import re
import wave
import os
import subprocess
from django.views.decorators.csrf import csrf_exempt
from .models import Paciente, Medicine


@csrf_exempt
def index(request):
	if request.method == "POST":
		print('aca ando')

		print(request.POST.keys())
		if Paciente.objects.filter(id_name=int(request.POST['id_name'])).exists():
		        obj= Paciente.objects.get(id_name=request.POST['id_name'])
			number_sessions_send=int(request.POST['number_session'])
			number_session_recive=obj.session_count
			principal_dir=settings.MEDIA_ROOT+obj.id_name+'/'
			for number_session in range(number_session_recive,number_session_recive+number_sessions_send):
				os.mkdir(settings.MEDIA_ROOT+request.POST['id_name']+'/Session'+str(number_session+1))
				obj.session_count=(obj.session_count+1)
				obj.save()
			for key in request.POST.keys():
		        	#audio64 = base64.b64decode(request.POST[key],' /')
						if key!= 'id_name' and key!='number_session':
							print(key)
							audio64=request.POST[key].decode('base64')
							print(key[key.index('Session')+6:])


		    					f=open(principal_dir+'Session'+key[key.index('Session')+7:]+'/'+key[0:-8]+".wav","wb") #wave.open cuando para agregar la metadata
				#f.setparams((1,2,8000,len(audio64),"NONE","not compressed")) #necesario si el wav no tiene metadata

							f.write(audio64)
							f.close()
			#wd="intelligibility/decode"

	#		subprocess.run('./script.sh',cwd=wd,stdout=True)
	#		t = open(wd+"/text")
	#		text=t.read().replace('audio ','')
	#        db_register= Paciente(nombres='Daniel', id_name=30052,edad=24,genero='masculino', birthday='26/09/1994',smoker=True,year_diag=2019,other_disorder='no',educational_level=5,weight=2.35,height=120,session_conunt=1)
	#        db_register.save()
			return HttpResponse('Datos enviados')# Create your views here.
		else:
			return HttpResponse('El paciente no ha sido creado en el servidor')

@csrf_exempt
def CreatePacient(request):
    if request.method == "POST":
        print('creando paciente')
        print(request.POST.keys())
	if(Paciente.objects.filter(id_name=int(request.POST['id_name'])).exists()):
           return HttpResponse('Este paciente ya existe')
        else:
	   birthday=datetime.strptime(request.POST['birthday'][4:10]+' '+request.POST['birthday'][-4:], '%b %d %Y')
           db_register= Paciente(name=request.POST['name_pacient'],id_name=request.POST['id_name'],gender=request.POST['gender'],birthday=birthday,smoker=bool(request.POST['smoker']),year_diag=int(request.POST['year_diag']),other_disorder=request.POST['other_disorder'],educational_level=int(request.POST['educational_level']),weight=request.POST['weight'],height=int(request.POST['height']),session_count=0)
	   db_register.save()
           os.mkdir(settings.MEDIA_ROOT+request.POST['id_name'])
     	   return HttpResponse('El paciente ha sido creado')
    return HttpResponse('')

@csrf_exempt
def NumberSession(request):
	if request.method == "POST":
		if Paciente.objects.filter(id_name=int(request.POST['id_name'])).exists():
			obj= Paciente.objects.get(id_name=request.POST['id_name'])
			return HttpResponse(str(obj.session_count))
		else:
			return HttpResponse(str(1))

@csrf_exempt
def CreateMedicine(request):
	if request.method == "POST":
		if Paciente.objects.filter(id_name=int(request.POST['id_name'])).exists():
			number_medicine=int(request.POST['number_medicine'])
			count_medicine=0

			for medicine in range(0,number_medicine):
				if not(Medicine.objects.filter(id_name=int(request.POST['id_name'])).exists() and Medicine.objects.filter(medicinename=request.POST['name_medicine'+str(medicine)]).exists()and Medicine.objects.filter(dose=int(request.POST['dose'+str(medicine)])).exists()and Medicine.objects.filter(intaketime=int(request.POST['intaketime'+str(medicine)])).exists()):
					print(Paciente.objects.filter(id_name=int(request.POST['id_name'])).exists())

				   	db_medicine= Medicine(medicinename=request.POST['name_medicine'+str(medicine)],id_name=request.POST['id_name'],dose=int(request.POST['dose'+str(medicine)]),intaketime=int(request.POST['intaketime'+str(medicine)]))
				   	db_medicine.save()
					count_medicine=count_medicine+1
			return HttpResponse('Se almacenaron '+str(count_medicine)+' medicinas nuevas')
		else:
			return HttpResponse('El paciente no ha sido creado en el servidor')
