def credito(informacion:dict)-> dict:
    id_p = informacion['id_prestamo']
    cas  = informacion['casado']
    dep  = informacion['dependiente']
    edu  = informacion['educacion']
    idep = informacion['independiente']
    i_d  = informacion['ingreso_deudor']
    i_cod = informacion['ingreso_codeudor']
    c_p  = informacion['cantidad_prestamo'] 
    p_p  = informacion['plazo_prestamo']
    h_c  = informacion['historia_credito']
    t_p  = informacion['tipo_propiedad']
    aprobado = bool

    if h_c == True:
        if h_c > 0 and (i_d / 9 ) > c_p:
          aprobado == True
        else:
            if dep > 2 and idep > 2:
              i_cod /12 > c_p
            else:
                c_p < 200
    else:
        if h_c ==False:
            if idep == True:
                if cas > 1 and dep > 1:
                    if (i_d / 10) > c_p or (i_cod /10) > c_p :
                     c_p < 180
                    else:
                      aprobado == False
                else:
                    aprobado == False
            else:
                if  t_p or dep > 2:
                        if edu == True:
                         (i_d / 11) > c_p or (i_cod / 11) > c_p
                        else:
                            aprobado == False
                else:
                        aprobado == False
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

print(credito(informacion))
