#!/usr/bin/python3

"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    determines if all the boxes can be opened
    or not:
    if can be opened: return True
    else: return False
    """
    numero_cajas = set(range(0, len(boxes)))
    numero_keys = set(boxes[0])
    numero_cajas_visitadas = set({0})
    while len(numero_keys - numero_cajas_visitadas) > 0:
        # indice de la sublista caja_actual
        # el indice de la caja que tengo llave y no ha sido abierta
        caja_actual = (numero_keys - numero_cajas_visitadas).pop()
        numero_cajas_visitadas.add(caja_actual)
        try:
            numero_keys.update(boxes[caja_actual])
        except:
            continue
    if len(numero_cajas - numero_cajas_visitadas) == 0:
        return True
    else:
        return False
