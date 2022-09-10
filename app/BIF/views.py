from re import search
from django.http.response import HttpResponse
from django.shortcuts import render
# Libreria para generar csv
import csv
import io
import json
# Validar fechas
from datetime import datetime
# importar models
from .models import Property, Occupancy, Licence, Status
# Responder pdf
from django.conf import settings
# Importar validacion de csv
from .validate import validate_csv
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.
@login_required
def home(request):
    data = {
        'usuario': request.user
    }
    return render(request, 'bif/index.html', data)


@login_required
def reporte(request):
    # Revisa si la petición incluye un parametro de busqueda
    try:
        search = request.GET['search']
    except:
        search = None
    # Realiza la consulta a la base de datos de acuerdo a la busqueda
    if search:
        inmuebles = Property.objects.filter(Q(predial__icontains=search) | Q(status__name__icontains=search)).order_by('-id')
    if not search:
        inmuebles = Property.objects.all().order_by('-id')
    # Se organiza la información por páginas, para que sea más rápido la visualización
    paginator = Paginator(inmuebles, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # Se genera el contexto para la vista
    data = {
        'usuario': request.user,
        'page_obj': page_obj,
        'search': search
    }
    # Se retorna la vista
    return render(request, 'bif/reporte.html', data)


def mapa(request):
    # Revisa si la petición incluye un parametro de busqueda
    try:
        search = request.GET['search']
    except:
        search = None
    # Realiza la consulta a la base de datos de acuerdo a la busqueda
    if search:
        inmuebles = Property.objects.exclude(coordenates__isnull=True, coordenates="").filter(Q(predial__icontains=search) | Q(status__name__icontains=search))
    if not search:
        inmuebles = Property.objects.exclude(coordenates__isnull=True, coordenates="")
    predios = []
    # Se obtienen los predios que se encuentran en la base de datos con coordenadas
    for inmueble in inmuebles:
        if inmueble.coordenates:
            # 'nombre':inmueble.status.name,
            # 'direccion':inmueble.status.addres,
            # 'propietario':inmueble.occupancy.owner,
            predios.append({
                'coordenadas': inmueble.coordenates,
                'predial': inmueble.predial,
                'real_register': inmueble.real_state_register,
                'occupancy': inmueble.occupancy.type_occupancy,
                'name_occupancy': inmueble.occupancy.ocuppancy_name,
                'video': inmueble.status.video,
                'id': inmueble.id
            })
    # Se genera el contexto para la vista
    data = {
        'usuario': request.user,
        'inmuebles': json.dumps(predios),
        'search': search
    }
    # Se retorna la vista
    return render(request, 'bif/mapa.html', data)


# Obtener las imagenes de una obra o contrato
def upload_csv(data):
    # Realizar solo si la peticion es de tipo POST
    # if request.method == 'POST' and request.FILES['csvfile']:
    if data.method == 'POST':
        # Obtener las imagenes disponibles para cada contrato
        try:
            myfile = data.FILES['file']
        except:
            pass
        if myfile:
            # Leer archivo csv
            file = myfile.read().decode('utf-8-sig')
            reader = csv.DictReader(io.StringIO(file), delimiter=';')
            data = [line for line in reader]

            # Validar csv
            error = validate_csv(data)
            # Si no ha sido validado, retornar errores en archivo csv
            if error:
                filename = "errores.txt"
                response = HttpResponse(error, content_type='text/plain')
                response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
                return response
            # Si no hay errores, generar el archivo de carga
            else:
                # Guardar cada uno de los registros del archivo en la base de datos
                for obj in data:
                    # Sector
                    try:
                        if obj['ID']:
                            inm_obj = Property.objects.get(id=obj['ID'])
                        else:
                            inm_obj = Property.objects.create(id=obj['ID'])
                    except Property.DoesNotExist:
                        inm_obj = Property.objects.create(id=obj['ID'])

                    if obj['FECHA DE DOCUMENTO'] == "":
                        fecha_documento_conv = None
                    else:
                        fecha_documento_conv = datetime.strptime(obj['FECHA DE DOCUMENTO'], '%d/%m/%Y').date()

                    if obj['FECHA DE LICENCIA DE CONSTRUCCION'] == "":
                        fecha_licencia_const = None
                    else:
                        fecha_licencia_const = datetime.strptime(obj['FECHA DE LICENCIA DE CONSTRUCCION'], '%d/%m/%Y').date()

                    if obj['FECHA EJECUTORIA DE LICENCIA'] == "":
                        fecha_exe_licencia = None
                    else:
                        fecha_exe_licencia = datetime.strptime(obj['FECHA EJECUTORIA DE LICENCIA'], '%d/%m/%Y').date()

                    inm_obj.predial = obj['NUMERO PREDIAL']
                    inm_obj.alternative_predial = obj['IDENTIFICACION PREDIAL ALTERNATIVA']
                    inm_obj.appraisal = obj['AVALUO COMERCIAL']
                    inm_obj.document_type = obj['TIPO DE DOCUMENTO PROPIEDAD']
                    inm_obj.act = obj['ACTO DE DOCUMENTO']
                    inm_obj.document_number = obj['NUMERO DE DOCUMENTO']
                    inm_obj.real_state_register = obj['MATRICULA INMOBILIARIA']
                    inm_obj.document_date = fecha_documento_conv
                    inm_obj.coordenates = obj['COORDENADAS']
                    inm_obj.save()

                    try:
                        status = Status.objects.get(id_property=inm_obj)
                    except Status.DoesNotExist:
                        status = Status()
                        status.id_property = inm_obj
                    status.number = obj['NUMERO']
                    status.category = obj['CATEGORIA']
                    status.type_property = obj['TIPO DEL ESTABLECIMIENTO']
                    status.name = obj['NOMBRE DEL INMUEBLE']
                    status.video = obj['VIDEO']
                    status.addres = obj['DIRECCION DEL INMUEBLE O NOMENCLATURA']
                    status.class_property = obj['CLASE DE INMUEBLE']
                    status.use = obj['DESTINACION O USO']
                    status.save()

                    try:
                        licence = Licence.objects.get(id_property=inm_obj)
                    except Licence.DoesNotExist:
                        licence = Licence()
                        licence.id_property = inm_obj
                    licence.curation = obj['CURADURIA']
                    licence.modality = obj['MODALIDAD DE LICENCIA']
                    licence.type_construction = obj['TIPO DE CONSTRUCCION']
                    licence.licence_number = obj['NUMERO DE LICENCIA DE CONSTRUCCION']
                    licence.licence_date = fecha_licencia_const
                    licence.construction_date = fecha_exe_licencia
                    try:
                        if obj['AREA']:
                            licence.area = float(obj['AREA'].replace('.', '').replace(',', '.'))
                    except:
                        pass
                    licence.save()

                    try:
                        occupancy = Occupancy.objects.get(id_property=inm_obj)
                    except Occupancy.DoesNotExist:
                        occupancy = Occupancy()
                        occupancy.id_property = inm_obj
                    occupancy.owner = obj['PROPIETARIO']
                    occupancy.contract = obj['CONTRATO']
                    occupancy.type_occupancy = obj['TIPO DE OCUPACION']
                    occupancy.id_document = obj['DOCUMENTO DE IDENTIFICACION']
                    occupancy.ocuppancy_document = obj['IDENTIFICACION DEL OCUPANTE']
                    occupancy.ocuppancy_name = obj['NOMBRE DEL OCUPANTE']
                    occupancy.seppi = obj['SEPPI']
                    occupancy.observation = obj['OBSERVACIONES']
                    occupancy.save()

    return HttpResponse("success")


# Guardar el archivo pdf en la base de datos
def upload_pdf(data):
    # Realizar solo si la peticion es de tipo POST
    if data.method == 'POST':
        # Intentar guardar el archivo
        try:
            myfile = data.FILES['file']
        except:
            myfile = None
        if myfile:
            try:
                predio = Property.objects.get(predial=data.POST['id'])
                if not predio.predial:
                    predio.predial = myfile
                    predio.save()
            except Property.DoesNotExist:
                pass
            # except Exception as e:
                # print(e)
    return HttpResponse("success")


@login_required
def show_pdf(request, id):
    try:
        file_pdf = Property.objects.get(predial=id)
        # Obtener solo el nombre el archivo
        file_name = 'staticfiles/files/' + file_pdf.predial.name.split('/')[-1]
        # Obtener el archivo pdf
        pdf = open(settings.MEDIA_ROOT + file_name, 'rb')
        # Crear el response
        # Agregar force-download or pdf para visualizar en el navegador
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'filename=Informacion-BIF.pdf'
        # retornar el archivo pdf
        return response
    # except:
        # return HttpResponse("No existe el archivo")
    except Exception as e:
        print(e)
        return HttpResponse("No existe el archivo")
