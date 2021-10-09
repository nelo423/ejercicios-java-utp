def cajero(informacion:dict) -> dict:
    id_p = informacion['id_prestamo']
    cas = informacion['casado']
    dep = informacion['dependientes']
    edu = informacion['educacion']
    indp = informacion['independiente']
    i_d = informacion['ingreso_deudor']
    i_c = informacion['ingreso_codeudor']
    c_p = informacion['cantidad_prestamo']
    p_p = informacion['plazo_prestamo']
    h_c = informacion['historia_credito']
    t_p = informacion['tipo_propiedad']
    aprobado = bool
    

    if h_c == True:
        if i_c > 0 and i_d/9 > c_p:
            aprobado = True
        else:
            if dep > 2 and indp == 'Si':
                i_c/12 > c_p
            else:
                c_p < 200
    else:
        if h_c == False:
            if indp == True:
                if (cas and dep > 1):
                    if i_d/10 > c_p or i_c/10 > c_p:
                       c_p < 180
                    else:
                        aprobado = False
                else:
                    aprobado = False
            else:
                if t_p and dep < 2:
                    if edu :
                        i_d/11 > c_p and i_c/11 > c_p
                    else:
                        aprobado = False
                else:
                    aprobado = False
    diccionario = {
    'id_prestamo':id_p,
    'aprobado':True}
    return diccionario
informacion = {
'id_prestamo' : 'RETOS2_001',
'casado' : 'No',
'dependientes' : 1,
'educacion':'Graduado',
'independiente':'Si',
'ingreso_deudor':4692,
'ingreso_codeudor':0,
'cantidad_prestamo':106,
'plazo_prestamo':360,
'historia_credito':1,
'tipo_propiedad':'Rural'}
print(cajero(informacion))
