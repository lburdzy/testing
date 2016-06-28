FOLDER_NAME = '4DSR_Modyfikacje'
modline = ''
lista = ['@CBA_A3', '@ace', '@task_force_radio',
         '@CUP_Terrains', '@RHS_AFRF', '@RHS_USF',
         '@RHS_GREF', '@PSZ', '@4DSR', '@4DSR_WaV',
         '@4DSR_Maps']


def gen_modline(lista, mod_folder_name='4DSR_Modyfikacje'):
    modline = ''
    for modname in lista:
        modline += '{}/{};'.format(FOLDER_NAME, modname)
    return modline
