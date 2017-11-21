# -*- coding: utf-8 -*-

import simpy

def main():
    env = simpy.Environment()
    env.process(semaforo(env))
    env.run(until=60)
    print "fin de la simulación"


def semaforo(env):
    while True:
        print "Verde en %.1f" % (env.now)
        yield env.timeout(5)
        print "Amarillo en %.1f" % (env.now)
        yield env.timeout(0.5)
        print "Rojo en %.1f" % (env.now)
        yield env.timeout(10)


if __name__ == '__main__':
    main()
