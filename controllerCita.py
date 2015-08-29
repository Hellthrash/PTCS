#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

def conectar():
    con = sqlite3.connect('citasmedicas')
    con.row_factory = sqlite3.Row
    return con

def obtener_citas():
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM citas"
    resultado = c.execute(query)
    citas = resultado.fetchall()
    con.close()
    return citas

def delete(id):
    exito = False
    con = conectar()
    c = con.cursor()
    query = "DELETE FROM citas WHERE id = ?"
    try:
        resultado = c.execute(query, [id])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito