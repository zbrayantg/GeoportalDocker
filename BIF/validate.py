
# Validar fechas
from datetime import datetime

# Validar archivo csv
def validate_csv(data):
    ''' 
    Valida que el archivo csv sea correcto
    Argumentos:
        data: Archivo csv a validar
    Retorna:
        True: Si el archivo es correcto
        False: Si el archivo no es correcto
        csv_error: Archivo de errores
     '''

    msg = ""
    #Validar que el archivo tenga los campos correctos
    headers_csv_file = list(data[0].keys())
    headers_required = ['ID','NUMERO', 'CATEGORIA', 'TIPO DEL ESTABLECIMIENTO', 'NOMBRE DEL INMUEBLE', 'VIDEO', 'DIRECCION DEL INMUEBLE O NOMENCLATURA', 'CLASE DE INMUEBLE', 'DESTINACION O USO', 'NUMERO PREDIAL', 'IDENTIFICACION PREDIAL ALTERNATIVA', 'AVALUO COMERCIAL', 'TIPO DE DOCUMENTO PROPIEDAD', 'ACTO DE DOCUMENTO', 'NUMERO DE DOCUMENTO', 'MATRICULA INMOBILIARIA', 'FECHA DE DOCUMENTO', 'CURADURIA', 'MODALIDAD DE LICENCIA', 'TIPO DE CONSTRUCCION', 'NUMERO DE LICENCIA DE CONSTRUCCION', 'FECHA DE LICENCIA DE CONSTRUCCION', 'FECHA EJECUTORIA DE LICENCIA', 'AREA', 'PROPIETARIO', 'CONTRATO', 'TIPO DE OCUPACION', 'DOCUMENTO DE IDENTIFICACION', 'IDENTIFICACION DEL OCUPANTE', 'NOMBRE DEL OCUPANTE', 'SEPPI', 'OBSERVACIONES', 'COORDENADAS']
    #Validar que el archivo tenga los campos correctos
    for header in headers_required:
        if header not in headers_csv_file:
            msg += f'El archivo no tiene el encabezado "{header}"\n'


    #Mostrar los campos que faltan o tienen errores en su sintaxis   
    if msg != "":
        context = "Estimad@ usuario: \n\n \
            Se ha generado un error al validar los encabezados disponibles en el archivo \n \
            A continuación se detallan los fallos obtenidos\n\n\n" + msg
        return context

    #Validación de la data
    #Listados de verificación
    sectors_list = ["1","2","3","4","Rural", ""]
    locations_list = ["Urbana","Rural", "Rural-Urbana", ""]
    destinations_list = ["Institucional", "Espacio público", "Construcción", "Dotacional", "Educativo", "Equipamiento comunitario", "Equipamiento público", "Fiscal", "Inmueble", "Parque", "Terreno", "Recreacional", "Residencial", "Vías", ""]
    type_document_property_list=["Escritura pública","Contrato de compraventa","Resolución", "Sentencia","Promesa de compraventa","Sin información","Acta de donación", ""]
    

    num_row = 1
    content = ""
    #Validación de datos
    for reg in data:
        num_row += 1

        #Validar que el número predial no sea vacio, es la llave primaria y por ende obligatoria
        ''' num_predial=reg['Número predial']
        if num_predial == "":
            msg += "El campo 'Número predial' no puede estar vacio \n" '''

        #Validar que el sector este en la lista de sectores
        ''' sector = reg['Sector']
        if sector not in sectors_list:
            msg += "El sector no es válido. \n" '''

        #Validar la localización
        ''' location=reg['Localización']
        if location not in locations_list:
            msg += "El campo 'Localización' no es una localización válida \n" '''
    
        #Validar que la destinación o uso no sea vacia y corresponda a una de las opciones
        ''' utility=reg['Destinación o uso']
        if utility not in destinations_list:
            msg += "El campo 'Destinación o uso' no es una destinación o uso válido \n" '''

        #Validar que el tipo de documento de propiedad corresponda a una de las opciones
        ''' type_document_property=reg['Tipo documento de propiedad']
        if type_document_property not in type_document_property_list:
            msg += "El campo 'Tipo documento de propiedad' no es un tipo de documento de propiedad válido \n" '''

        #Validar que la fecha de documento sea una fecha o sea vacia
        date_document=reg['FECHA DE DOCUMENTO']
        if date_document:
            #Validar que sea una fecha
            try:
                datetime.strptime(date_document, '%d/%m/%Y').date()
            except ValueError:
                msg += "El campo 'FECHA DE DOCUMENTO'("+str(date_document)+") debe ser una fecha con el formato 'DD/MM/YYYY' \n"
        
        #Validar que la fecha de la licencia sea una fecha o sea vacia
        date_licence=reg['FECHA DE LICENCIA DE CONSTRUCCION']
        if date_licence:
            #Validar que sea una fecha
            try:
                datetime.strptime(date_licence, '%d/%m/%Y').date()
            except ValueError:
                msg += "El campo 'FECHA DE LICENCIA DE CONSTRUCCION'("+str(date_licence)+") debe ser una fecha con el formato 'DD/MM/YYYY' \n"
        
        #Validar que la fecha de la licencia  ejecutoria sea una fecha o sea vacia
        date_exe_licence=reg['FECHA EJECUTORIA DE LICENCIA']
        if date_exe_licence:
            #Validar que sea una fecha
            try:
                datetime.strptime(date_exe_licence, '%d/%m/%Y').date()
            except ValueError:
                msg += "El campo 'FECHA EJECUTORIA DE LICENCIA'("+str(date_exe_licence)+") debe ser una fecha con el formato 'DD/MM/YYYY' \n"
        
        
        #Validar que el área sea un número o sea vacia
        ''' area=reg['Área']
        if area != "":
            try:
                float(area.replace(',','.'))
            except ValueError:
                msg += "El campo 'Área' debe ser un valor númerico \n" '''
        
        # Agregar fila y el mensaje
        if msg:
            content += "\nEn la fila #" + str(num_row) + "\n \n"
            content += msg
            msg = ""
    # Se retorna el mensaje
    return content
    