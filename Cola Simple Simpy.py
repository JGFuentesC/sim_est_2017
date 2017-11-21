# -*- coding: utf-8 -*-
from __future__ import division
import simpy
from scipy import stats

class Banco:
    def __init__(self,env):
        self.cajeros = simpy.Resource(env,capacity=2)

lst_llegadas = []
lst_atenciones = []
lst_salidas = []

def cliente(nombre,env,banco):
    print "Cliente %02d llegando en %d" %(nombre,env.now)
    lst_llegadas.append((nombre,env.now))
    with banco.cajeros.request() as req:
        yield req
        print "Cliente %02d es atendido en %d" %(nombre,env.now)
        lst_atenciones.append((nombre, env.now))
        yield env.timeout(5)
        print "Cliente %02d sale en %d" % (nombre, env.now)
        lst_salidas.append((nombre, env.now))

def generador_clientes(env,banco):
    for i in range(10):
        env.process(cliente(i,env,banco))
        yield env.timeout(4)


env = simpy.Environment()
banco = Banco(env)
gen_clientes = env.process(generador_clientes(env,banco))
env.run(until=200)

print lst_llegadas
print lst_atenciones
print lst_salidas