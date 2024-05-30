# SIA - TP2: Algoritmos Genéticos
Grupo 4: Luciano Neimark, María Otegui, Nicolás Tordomar, Paz Aramburu
--
En este trabajo se implementó un motor de algoritmos genéticos que buscaban optimizar los parámetros de los jugadores en un juego de roles.

## Implementación
### Mutación:
- Mutación de un gen
- Mutación multigen uniforme
- Mutación multigen limitada
- Mutación completa

Los métodos de mutación pueden ser uniformes o no uniformes.
### Cruza:
- Cruce de un punto
- Cruce de dos puntos
- Cruce uniforme
- Cruce anular
### Selección:
- Elite
- Universal
- Ruleta
- Torneo determinístico
- Torneo probabilístico
- Boltzmann
- Ranking

## Requisitos
Para poder correr el proyecto se necesitan tener:
- Python3
- pip3
- pipenv

## Dependencias
El proyecto utiliza distintas dependencias. Para poder usarlo hay que insatalarlas corriendo el siguiente comando:
```shell
pipenv install
```

Ejecución
--
Para poder probar el proyecto hay que ejecutar el main.py. En config.json se especifican los distintos parámetros. A continuación se muestran las opciones disponibles para ellos.

"[>0]": número real mayor a 0

"[0-1]": número real entre 0 y 1

"[opcion1|opcion2|...]": poner cualquier opción entre comillas dobles. 
**Si una opción es null, ponerla sin comillas dobles**

" true | false ": elegir true o false

```json
{
    "clase": "[GUERRERO|ARQUERO|DEFENSOR|INFILTRADO]",
    "n": "[>0]",
    "K": "[>0]",
    "condicion_corte": {
        "tipo": "[cantidad_generaciones|contenido|estructura|optimo]",
        "cantidad_generaciones": {
            "max_generacion": "[>0]"
        },
        "contenido": {
            "generaciones_sin_cambio": "[>0]",
            "generaciones_igual_fitness": "[>0]"
        },
        "estructura": {
            "generaciones_iguales": "[0-1]"
        },
        "max_fitness": "[>0]"
    },
    "seleccion": {
        "metodo1": "[elite|universal|ruleta|determinista|probabilistica|boltzmann|ranking]",
        "metodo2": "[elite|universal|ruleta|determinista|probabilistica|boltzmann|ranking]",
        "A": "[0-1]",
        "torneo_deterministico": {
            "muestra": "[>0]"
        },
        "torneo_probabilistico": {
            "threshold": "[0-1]"
        },
        "boltzmann": {
            "T_C": "[>0]",
            "T_0": "[>0]",
            "T_K": "[>0]"
        }
    },
    "reemplazo": {
        "metodo3": "[elite|universal|ruleta|determinista|probabilistica|boltzmann|ranking]",
        "metodo4": "[elite|universal|ruleta|determinista|probabilistica|boltzmann|ranking]",
        "B": "[0-1]"
    },
    "cruce": {
        "metodo": "[un_punto|dos_puntos|anular|uniforme]",
        "probabilidad": "[0-1]",
        "metodo_seleccion_cruce": "[puntas|escalonado|fitness]"
    },
    "sesgo": {
        "joven": " true | false "
    },
    "mutacion": {
        "metodo": "[gen|multigen|completa|limitada]",
        "no_uniforme": {
            "funcion": "[creciente|decreciente|null]",
            "factor": "[0-1]"
        },
        "probabilidad": "[0-1]",
        "rango": {
            "min": "[>0]",
            "max": "[>0]"
        }
    }
}

```

## Link a la presentación TP2

https://docs.google.com/presentation/d/1fMst1zYPzgmAhkh2W6q2rzegr-6VeSozbGJouFpUN8c/edit?usp=sharing