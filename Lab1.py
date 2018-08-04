import gym
import gym_pull
import numpy
import random
#gym_pull.pull('github.com/ppaquette/gym-super-mario')
env = gym.make('ppaquette/SuperMarioBros-1-1-v0')

move = {
                0 : [ 0 , 0 , 0 , 0 , 0 , 0 ],   # NOOP
                1 : [ 1 , 0 , 0 , 0 , 0 , 0 ],   # Arriba
                2 : [ 0 , 0 , 1 , 0 , 0 , 0 ],   # Abajo
               # 3 : [ 0 , 1 , 0 , 0 , 0 , 0 ],   # Izquierda
               # 4 : [ 0 , 1 , 0 , 0 , 1 , 0 ],   # Izquierda + A
               # 5 : [ 0 , 1 , 0 , 0 , 0 , 1 ],   # Izquierda + B
               # 6 : [ 0 , 1 , 0 , 0 , 1 , 1 ],   # Izquierda + A + B
                3 : [ 0 , 0 , 0 , 1 , 0 , 0 ],   # Derecha
                4 : [ 0 , 0 , 0 , 1 , 1 , 0 ],   # Derecha + A
                5 : [ 0 , 0 , 0 , 1 , 0 , 1 ],   # Derecha + B
                6 : [ 0 , 0 , 0 , 1 , 1 , 1 ],   # Derecha + A + B
                7 : [ 0 , 0 , 0 , 0 , 1 , 0 ],   # A
                8 : [ 0 , 0 , 0 , 0 , 0 , 1 ],   # B
                9 : [ 0 , 0 , 0 , 0 , 1 , 1 ],   # A + B
            }

for i_episode in range(100):
    observation = env.reset()
    while True:
     
        env.render()
        a=[]
        contador=0
        c=1
        distancia=0

        a = move[random.randint(0,9)]
          if a==3:
            contador=contador+1
            print contador

        action=a
       
        #a = numpy.insert(a,contador,action,axis=0)
        archivo = open("archivo.txt", "a")
        archivo.write(str(action))
        archivo.write("\n")
               
        print action
        [0,0,0,0,0,0]
        observation, reward, done, info = env.step(action)
        print info

        if done:
            break
