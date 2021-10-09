def perfumes(diccionario:dict) -> dict:
    precio = diccionario['precio']
    b_a = diccionario['base_alcohol']
    n_f = diccionario['notas_frescas']
    n_c = diccionario['notas_citricas']
    i = diccionario['importado']
    

    if precio > 200000:
        if b_a:
            if n_f:
                if n_c:
                       if i:
                           perfume = 'Chanel No 5'
                       else:
                            perfume = 'Jean Pascal'
                else:
                    perfume = 'Vanilla'
            else:
                perfume = 'Gucci Guilty'
        else:    
            if i:
                perfume = 'Oud'        
            else:
                 perfume = 'Floral'
    else:
        if b_a:
            if n_f:
                if n_c:
                    if i:
                        perfume = 'Salvatore Ferragamo'
                    else:
                        perfume = 'Arturo Calle'      
                else:
                    perfume = 'Mercedes Benz'     
            else:
                perfume = 'Nautica'    
        else:
            perfume = 'Alexandria'       

    diccionarioResultado={
            'cliente':str(diccionario['nombre']) + " " + str(diccionario['apellido']),
            'perfume':perfume
    }        

    return diccionarioResultado

cliente = {
'nombre': 'Laura',
'apellido': 'García',
'precio': 250000,
'base_alcohol' : 1,
'notas_frescas': 0,
'notas_citricas': 1,
'importado': 0
}
print(perfumes(cliente))
cliente = {
'nombre': 'Luis',
'apellido': 'Giraldo',
'precio': 500000,
'base_alcohol': 0,
'notas_frescas': 1,
'notas_citricas': 1,
'importado': 0
}
print(perfumes(cliente))







'''

    valor   = int(input('Ingrese valor de compra :'))
    id_nom:str = cliente['nombre']
    id_ape:str = cliente['apellido']
    
    
    
    
    
    fragancia = (fragancia:dict) :
    id_oud = fragancia['id_oud']    
    id_flo = fragancia['id_floral']
    id_guc = fragancia['id_Gucci_Guilty']
    id_van = fragancia['id_vainilla']
    id_chan= fragancia['id_Chanel_No_5']
    id_jean = fragancia['id_Jean_Pascal']
    id_ale = fragancia['id_alexandria']
    id_nau = fragancia['id_nautica']
    id_m_b  = fragancia['id_Mercedez_Benz']
    id_s_f  = fragancia['id_Salvatore_Ferragano']
    id_a_c  = fragancia['id_Arturo_Calle']
    
    if precio = int((valor)>= 200000) :
        if bas_alc == True:
            if impor == False:
                fragancia = id_flo
                if bas_alc == True:
                    if nota_fres == False:
                        fragancia = id_Gucci_Guilty
                        if nota_cit == False:
                            fragancia = id_vainilla
                            if nota_cit == True:
                               if impor == True:
                                  fragancia = id_Chanel_No_5
                                  if impor == False:
                                     fragancia = id_Jean_Pascal
                                  else:
                                       impor ==True
                                else:
                                     impor = False
                            else:
                                nota_cit = False
                        else:
                            nota_cit = True
                    else:
                         nota_fres = True
                else:
                    bas_alc = False
            else:
                impor = True
        else:
            if bas_alc == False:
               fragancia = id_ale
    else:
        precio = valor < 200000
        if bas_alc == True:
            if nota_fres == False:
                fragancia = id_nautica
                if nota_fres == True:
                    if nota_cit == False:
                        fragancia = id_Mercedez_Benz
                    else:
                        if nota_cit ==True:
                           if impor ==False:
                              fragancia = id_Arturo_Calle
                              if impor == True:
                                 fragancia = id_Salvatore_Ferragano
                             else:
                                 impor = False
                          else:
                               impor = False
                        else:
                            nota_fres = False
                    else:
                        nota_fres = False
                else:
                    bas_alc = False
            else:
                bas_alc = True
    recomendacion = {
    id_nom : 'nombre',
    id_ape : 'apellido',
    fragancia = True}
    return cliente
perfumes = {
'nombre' :'Laura', 
'apellido':'Garcia',
'precio' : 250000,
'base_alcohol' :1,
'notas_frescas' :0,
'notas_citricas' : 1;
'id_importado' : 0}
print(perfumes(cliente))
'''

    #apellido str Apellido de quien compra el perfume 
    #precio int Precio del perfume
#base_alcohol bool Indica si al cliente le gustan los perfumes de alcohol
#notas_frescas bool Indica si al cliente le gustan los perfumes con notas frescas
#notas_citricas  bool Indica si al cliente le gustan los perfumes con notas cítricas
#importado bool Indica si al cliente le gustan los perfumes importados

