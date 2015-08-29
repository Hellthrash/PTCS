#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

def conectar():
    con = sqlite3.connect('citasmedicas')
    con.row_factory = sqlite3.Row
    return con

def obtener_pacientes():
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM paciente"
    resultado = c.execute(query)
    pacientes = resultado.fetchall()
    con.close()
    return pacientes

def delete(rut):
    exito = False
    con = conectar()
    c = con.cursor()
    query = "DELETE FROM paciente WHERE rut = ?"
    try:
        resultado = c.execute(query, [rut])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito
