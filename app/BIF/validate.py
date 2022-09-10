
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
    # Validar que el archivo tenga los campos correctos
    headers_csv_file = list(data[0].keys())
    headers_required = ['ID', 'NUMERO', 'CATEGORIA', 'TIPO DEL ESTABLECIMIENTO', 'NOMBRE DEL INMUEBLE', 'VIDEO', 'DIRECCION DEL INMUEBLE O NOMENCLATURA', 'CLASE DE INMUEBLE', 'DESTINACION O USO', 'NUMERO PREDIAL', 'IDENTIFICACION PREDIAL ALTERNATIVA', 'AVALUO COMERCIAL', 'TIPO DE DOCUMENTO PROPIEDAD', 'ACTO DE DOCUMENTO', 'NUMERO DE DOCUMENTO', 'MATRICULA INMOBILIARIA', 'FECHA DE DOCUMENTO', 'CURADURIA', 'MODALIDAD DE LICENCIA', 'TIPO DE CONSTRUCCION', 'NUMERO DE LICENCIA DE CONSTRUCCION', 'FECHA DE LICENCIA DE CONSTRUCCION', 'FECHA EJECUTORIA DE LICENCIA', 'AREA', 'PROPIETARIO', 'CONTRATO', 'TIPO DE OCUPACION', 'DOCUMENTO DE IDENTIFICACION', 'IDENTIFICACION DEL OCUPANTE', 'NOMBRE DEL OCUPANTE', 'SEPPI', 'OBSERVACIONES', 'COORDENADAS']
    # Validar que el archivo tenga los campos correctos
    for header in headers_required:
        if header not in headers_csv_file:
            msg += f'El archivo no tiene el encabezado "{header}"\n'

    # Mostrar los campos que faltan o tienen errores en su sintaxis
    if msg != "":
        context = "Estimad@ usuario: \n\n \
            Se ha generado un error al validar los encabezados disponibles en el archivo \n \
            A continuación se detallan los fallos obtenidos\n\n\n" + msg
        return context

    num_row = 1
    content = ""
    # Validación de datos
    for reg in data:
        num_row += 1

        # Validar que la fecha de documento sea una fecha o sea vacia
        date_document = reg['FECHA DE DOCUMENTO']
        if date_document:
            # Validar que sea una fecha
            try:
                datetime.strptime(date_document, '%d/%m/%Y').date()
            except ValueError:
                msg += "El campo 'FECHA DE DOCUMENTO'(" + str(date_document) + ") debe ser una fecha con el formato 'DD/MM/YYYY' \n"

        # Validar que la fecha de la licencia sea una fecha o sea vacia
        date_licence = reg['FECHA DE LICENCIA DE CONSTRUCCION']
        if date_licence:
            # Validar que sea una fecha
            try:
                datetime.strptime(date_licence, '%d/%m/%Y').date()
            except ValueError:
                msg += "El campo 'FECHA DE LICENCIA DE CONSTRUCCION'(" + str(date_licence) + ") debe ser una fecha con el formato 'DD/MM/YYYY' \n"

        # Validar que la fecha de la licencia  ejecutoria sea una fecha o sea vacia
        date_exe_licence = reg['FECHA EJECUTORIA DE LICENCIA']
        if date_exe_licence:
            # Validar que sea una fecha
            try:
                datetime.strptime(date_exe_licence, '%d/%m/%Y').date()
            except ValueError:
                msg += "El campo 'FECHA EJECUTORIA DE LICENCIA'(" + str(date_exe_licence) + ") debe ser una fecha con el formato 'DD/MM/YYYY' \n"

        # Agregar fila y el mensaje
        if msg:
            content += "\nEn la fila #" + str(num_row) + "\n \n"
            content += msg
            msg = ""
    # Se retorna el mensaje
    return content
