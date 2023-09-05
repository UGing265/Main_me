

from tqdm import tqdm
import time

def show_loading_animation():
    for i in tqdm(range(100)):
        time.sleep(0.0001)  # Do some work

show_loading_animation()
print(tqdm)

import time
 # Output: 32
 

def show_loading_animation():
    k = []
    z = []
    x = []
    while True:
        for i in ['_ ']:
            k.append(i)
            if len(k) < 20:
             print(i,end='')
             time.sleep(0.1)
            elif len(k)==20:
                print("\\")
            else:

               for i in ['\t\t\t\t      |']:
                z.append(i)
                if len(z) < 10:
                 print(i)
                 time.sleep(0.1)
                elif len(z) == 10:
                  print("'\t\t\t\t      /")
                else:
                    for i in reversed(['\t\t\t\t      ']):
                     x.append(i)
                    if len(x) < 20:
                     print(i,end='')
                     time.sleep(0.1)
                   


#def die():
    