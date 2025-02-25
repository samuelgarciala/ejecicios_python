personas={
    1:"Juan",
    2:"pepe"
    
}
datos_juan=personas[1]
datos_pepe=personas.get(3)

personas[1]="Maria"
datos_maria=personas[1]





notas={
    "pepe":{
        "matematicas":5,
        "español":7
    },
    "juan":{
        "matematicas":3,
        "español":10
        }
    }
    
print(notas)
