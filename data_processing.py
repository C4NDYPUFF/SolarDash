import pandas as pd 


def load_data(file_path):
    df = pd.read_excel(file_path)
    return df

def mapear_asistencia(asistencia):
    if pd.isna(asistencia):
        return 'NO'
    if asistencia == True:
        return 'SI'
    if asistencia == False:
        return 'NO'
    else:
        return str(asistencia).upper()

def renombrar_cargos(cargo):
    # Convertimos el cargo a cadena si no es NaN, en caso contrario retornamos 'OTROS'
    if pd.isna(cargo):
        return 'INFORMACION NO DISPONIBLE'
    cargo_str = str(cargo).upper()
    # Verificamos si el cargo contiene la palabra 'DIRECTOR'
    if 'DIRECTOR' in cargo_str:
        return 'DIRECTOR'
    if 'JEFE' in cargo_str:
        return 'DIRECTOR'
    # Lista de otros cargos que queremos mantener
    otros_cargos_permitidos = ['ESTUDIANTE', 'GERENTE', 'VENTAS', 'PERSONAL OPERATIVO']
    # Verificamos si el cargo actual contiene algún otro cargo permitido
    for oc in otros_cargos_permitidos:
        if oc in cargo_str:
            return oc
    # Si el cargo no es uno de los permitidos, lo renombramos a 'OTROS'
    return 'OTROS'



# Define a function to categorize values
def categorize_empresa(x):
    match_string = {'UNIVERSIDAD', 'INSTITUTO'}
    if any(keyword in x.upper() for keyword in match_string):
        return 'UNIVERSIDAD'
    elif x.upper() == 'NAN':
        return 'OTROS'
    else:
        return 'EMPRESA'
