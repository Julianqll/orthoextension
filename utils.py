import math
from fractions import Fraction
from functools import reduce
from math import gcd


def modulo(vector):
  sum = 0
  for i in range(len(vector)):
    sum += vector[i]*vector[i]
  raiz = math.sqrt(sum)
  if Fraction(raiz).denominator == 1:
    raiz = int(raiz)
    suma = (1/raiz,'1/'+str(raiz),sum)
  else:
    suma = (1/raiz,'1/√'+str(sum), sum)
  return suma

def multvector(vector, modulo):
  vectorn=[]
  for i in range(len(vector)):
    vectorn.append(vector[i]*modulo)
  return vectorn

def prodintercan(vector1, vector2):
  prodint = 0
  for i in range(len(vector1)):
    prodint += vector1[i]*vector2[i]
  return prodint

def restvector(vector1, vector2):
  vectorn = []
  for i in range(len(vector1)):
    vectorn.append(vector1[i]-vector2[i])
  return vectorn

def find_gcd(list):
    x = reduce(gcd, list)
    return x

def maxcd(vector):
  vectorn = vector
  gcd = find_gcd(vectorn)
  if gcd != 1:
    for i in range(len(vectorn)):
      vectorn[i] = int(vectorn[i]/gcd)
    return vectorn
  return vector
    

def frac(vector):
  vectorn = []
  for i in range(len(vector)):
    vector[i] = round(vector[i],2)
  for i in range(len(vector)):
    if int(Fraction(vector[i]).denominator) !=1:
      denominador = int((Fraction(vector[i]).limit_denominator(10)).denominator)
      for j in range(len(vector)):
        vector[j]=int((Fraction(vector[j]).limit_denominator(10)).numerator)*denominador/((Fraction(vector[j]).limit_denominator(10)).denominator)
    vectorn.append(int(vector[i]))
  return vectorn
