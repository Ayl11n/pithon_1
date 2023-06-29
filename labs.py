diccionario_r ={
    
   "Id_r":{"8","10"},
    "Nombre_r":{"BioBio","Los lagos"},
    "Superficie(km2)":{"23.890", "48.583"},
    "habitantes":{"1.556.805","828.708"}
}
print(diccionario_r)

densidad_b=1556805/23890
densidad_l=828708/48583

densidad={
    "BioBio_densidad":{round(densidad_b,1)},
    "Loslagos_densidad":{round(densidad_l,1)}
}
diccionario_r.update(densidad)

capital={
    "BioBio_capital":"Concepcion",
    "Loslagos_capital":"Puerto Montt"
}
diccionario_r.update(capital)

comunas={
    "BioBio_comunas":["Lota", "Lebu", "Los Ángeles"],
    "Loslagos_comunas":["Castro", "Puerto Varas", "Purranque"]

}
diccionario_r.update(comunas)

provincias={
    "BioBio_provincias":("Biobío", "Arauco","Concepción"),
    "Loslagos_provincias":("Osorno", "Llanquihue","Chiloé", "Palena")

}
diccionario_r.update(provincias)

print(f"Diccionario actualizado: ",diccionario_r)
