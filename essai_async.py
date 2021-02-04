import asyncio
import time
""" essais de programmation asynchrone coroutine.
Pour utiliser la programmation asynchrone, il faut identifier dans son code
une partie qui est bloquante, c’est-à-dire qui passe du temps à attendre après
des I/O.
Il faut donc sortir cette partie du code linéaire et en faire une coroutine.
Cette notion de coroutine est à la base de la programmation asynchrone.
Voici l’exemple le plus basique, adapté de la documentation officielle :"""

async def main():
    print(f"hello {time.strftime('%X')}")
    await async.sleep(5)
    print(f"world {time.strftime('%X')}")


async def main_say_after(): 
    task1 = asyncio.create_task(say_after(1, ’hello’))
    task2 = asyncio.create_task(say_after(2, ’world’)) 
    task3 = asyncio.create_task(say_after(1, ’!!!!!’))

    print(f"started at {time.strftime(’%X’)}") 
    print(f"await task 1 {time.strftime(’%X’)}") 
    await task1 
    print(f"await task 2 {time.strftime(’%X’)}") 
    await task2 
    print(f"await task 3 {time.strftime(’%X’)}") 
    await task3 
     
    print(f"finished at {time.strftime(’%X’)}")
#meme fonction mais plus compact.
async def main_say_after_2(): 
    print(f"started at {time.strftime(’%X’)}") 
    await asyncio.gather( 
        say_after(1, ’hello’), 
        say_after(2, ’world’), 
        say_after(1, ’!!!!!’), 
        ) 
    print(f"finished at {time.strftime(’%X’)}") 

