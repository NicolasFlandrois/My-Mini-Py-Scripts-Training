#!/usr/bin/python3.7
# UTF8
# Date:
# Author: Nicolas Flandrois
# Description: How to use Threads in Python? Practice exercices from
# Corey Schafer : https://youtu.be/IEEhzQoKtQU
# Running scripts concurrently (in the same time, not one after the other)
# Asynchronism

import concurrent.futures
import requests
import time
# import threading


start = time.perf_counter()

def do_something():
    print('sleeping 1 second...')
    time.sleep(1)
    print('Done sleeping...')

def do_something_arg(seconds):
    print(f'sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print('Done sleeping...')

def do_something_conc(seconds):
    print(f'sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done sleeping...{seconds}'

# Expl, No Threading... 1 command after an other:
# do_something()
# do_something()
# do_something()
# Total running time should be: 3s (3 x 1s)

###########################################
# Simple Threading exemple (the long way/older way/manual way)

# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)
# t3 = threading.Thread(target=do_something)

# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()
# # this thread takes 1 sec to run instead of 3s

################################################
# If need to thread in a loop multiple times...:

# threads = []

# for _ in range(10):
#     t = threading.Thread(target=do_something)
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()

# If 10 do_something function were to be done in a for loop, 1 after the other
# It would take about 10 seconds minimum. By threading them, it takes 1.02s only


#################################################
# Threading a function in a for loop, changing the argument through a list...

# threads = []

# for _ in range(10):
#     t = threading.Thread(target=do_something_arg, args=[1.5])
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()

# Script finished in 1.5s run time instead of 15s one after the other...
########################################################################
########################################################################
# The New way > more code optimisation

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     f1 = executor.submit(do_something_conc, 1)
#     f2 = executor.submit(do_something_conc, 1)
#     print(f1.result())
#     print(f2.result())
#     # This is 1 way to do it, but don't allow to successively run through large number of repetition

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     secs = [5, 4, 3, 2, 1]
#     results = [executor.submit(do_something_conc, sec) for sec in secs]
#     for f in concurrent.futures.as_completed(results):
#         print(f.result())
    # Even if this thread, starts with the 5s, it returns results by fastest accomplished (First Finished, First Out)
    # Running time = 5s instead of 15s
########################################################################
########################################################################
# # Using Map method with threading
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     secs = [5, 4, 3, 2, 1]
#     results = executor.map(do_something_conc, secs)
#     # Doesn't return results as completed, but returns(print) them after complession, in the order it came in (Fisrt In First Out)
#     # Running time is still optimised down. Running time 5s, instead of 15s.
#     for result in results:
#         print(result)

##############################################################################
##############################################################################
##############################################################################
# Real Life Exemple:

img_urls = [
    'https://unsplash.com/photos/BO14MMJLMIk',
    'https://unsplash.com/photos/XVaXbzQul90',
    'https://unsplash.com/photos/KCEwOduK8ck',
    'https://unsplash.com/photos/_0TevBj2F1M',
    'https://unsplash.com/photos/JiqalEW6Ml0',
    'https://unsplash.com/photos/z3dW9lLdyO0',
    'https://unsplash.com/photos/6KZZJMEbdQg',
    'https://unsplash.com/photos/gSF6qeKM6qs',
    'https://unsplash.com/photos/Js4jgpksRGk',
    'https://unsplash.com/photos/PfMDvyzryk4',
    'https://unsplash.com/photos/h6pXog1m8T0'
    ]

########
# The Old way... For loop, 1 after the other, downloading each photos

# for img_url in img_urls:
#     img_bytes = requests.get(img_url).content
#     img_name = img_url.split('/')[4]
#     img_name = f'{img_name}.jpg'
#     with open(img_name, 'wb') as img_file:  # Openning a file in Byte mode, & Write mode
#         img_file.write(img_bytes)
#         print(f'{img_name} was downloaded')
#         # For those 11 pictures, run time = 6.5s if old fashion way, 1 after the other in e for loop
#         # The longer the list, the longer the run time
##########################################
# Threading!

def download_img(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[4]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_img, img_urls)
# This I/O process is takin 1.12s running time to download all URL images, instead of 6.5s

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
