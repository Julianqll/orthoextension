from flask import Flask
from utils import *

app = Flask(__name__)


@app.route("/orthoextension/<vectoresbase>", methods=["GET", "POST"])
def ortonormalizar(vectoresbase):
  vectores = []
  vectoresbase = str((vectoresbase).replace('(',''))
  vectoresbase = str((vectoresbase).replace(')',''))
  puntocomas = vectoresbase.count(";")
  for i in range (puntocomas):
    vectorcitos = vectoresbase.split(";")
  for i in range(len(vectorcitos)):
    prevectores = vectorcitos[i].split(",")
    vector = []
    for j in range(len(prevectores)):
      elemento = int(prevectores[j])
      vector.append(elemento)
    vectores.append(vector)


  ortonormales = []
  ortonormalesmulti= []
  ortonormalesvect= []
  modulos = []
  ortonormalestxt = []
  for i in range(len(vectores)):
    if i == 0:
      #dividir vector por modulo
      modul = modulo(vectores[i])
      modulos.append(modul[2])
      ortonormal = multvector(vectores[i], modul[0])
      ortonormales.append(ortonormal)
      ortonormalesmulti.append("("+modul[1]+")")
      ortonormalesvect.append(vectores[i])
    else:
      j = i
      zeta = vectores[i]
      while j > 0:
        #imaginando que i=1
        #productointernocanonico
        prodint = prodintercan(vectores[i], ortonormalesvect[j-1])
        #<v1,u0>u0
        prodint = prodint/modulos[j-1]
        operacion = multvector(ortonormalesvect[j-1],prodint)
        #resta v1 - ...
        zeta = restvector(zeta, operacion)
        j-=1
      zeta = frac(zeta)
      modul = modulo(zeta)
      modulos.append(modul[2])
      ortonormal = multvector(zeta, modul[0])
      ortonormales.append(ortonormal)
      ortonormalesmulti.append("("+modul[1]+")")
      ortonormalesvect.append(zeta)

  for i in range(len(ortonormalesmulti)):
    ortonormalestxt.append(ortonormalesmulti[i]+str(ortonormalesvect[i]))

  return "<p>"+str(ortonormalestxt)+"</p>"
