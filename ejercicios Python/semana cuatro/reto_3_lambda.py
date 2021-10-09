def calcular_ingresos(datos:list) -> dict:
    pre: str = "prepagada"
    sub: str = "subsidiada"
    total: int = 0 
    total_pre: int = 0
    total_sub: int = 0
    cont_pre: int = 0
    cont_sub: int = 0

    for item in datos:
        total = total + item["valor_a_pagar"]
        if item["salud"] == pre:
            total_pre = total_pre + item["valor_a_pagar"] 
            cont_pre = cont_pre + 1
        elif item["salud"] == sub:
             total_sub = total_sub + item["valor_a_pagar"]
             cont_sub = cont_sub + 1
    prom_pre: float = 0
    prom_sub: float = 0
    if cont_pre > 0:
        prom_pre= round((total_pre / cont_pre),1)
    if cont_sub > 0:
        prom_sub= round((total_sub / cont_sub),1)
    respuesta : dict = {
        "total" : total,
        "promedio_salud_prepagada"  : prom_pre,
        "promedio_salud_subsidiada" : prom_sub
    }
    return respuesta
    
datos: list = [
    {
        "salud": "prepagada",
        "valor_a_pagar": 20000
    },
    {
        "salud": "subsidiada",
        "valor_a_pagar": 25000
    },
    {
        "salud": "prepagada",
        "valor_a_pagar": 32000
    },
    {
        "salud": "prepagada",
        "valor_a_pagar": 38000
    },
    {
        "salud": "subsidiada",
        "valor_a_pagar": 25000
    },
    {
        "salud": "prepagada",
        "valor_a_pagar": 33000
    },
    {
        "salud": "subsidiada",
        "valor_a_pagar": 28000
    }
]
    
print(calcular_ingresos(datos))



  
