#!/usr/bin/env python3
'''
MIT License Copyright (c) 2020 Ayush Bhardwaj (classicayush@gmail.com), Kaushlendra Pratap
(kaushlendrapratap.9837@gmial.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished
to do so, subject to the following conditions:

The above copyright notice and this permission notice (including the next
paragraph) shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF
OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

import random
import itertools
import os


def splitter(file,dirname):
    counter = 0
    with open(file, 'r') as f:
        para = sum(line.isspace() for line in f) + 1

    with open(file, 'r+') as f:
        contents = f.read()

    contents = contents.split('\n\n')
    os.mkdir(dirname)
    lst = []
    for i in range(para):
        counter += 1
        name = dirname + '{}.txt'.format(counter)
        with open(os.path.join(dirname,name), 'w') as o1:
            print(contents)
            if i in range(len(contents)):
                o1.write(str(contents[i]))
        
        lst.append(name)
    # print(lst)
    # print(counter)
    # print(dirname)
    
    get_random_pairs(lst,counter,dirname)
    



 
 
def get_random_pairs(lst,counter,dirname): 
    pairs = list(itertools.combinations(lst, 2))
    tri_pairs = list(itertools.combinations(lst, 3)) 
    
    random.shuffle(pairs)
    random.shuffle(tri_pairs) 
    # print(pairs)
    # print(tri_pairs)
                       
    if pairs:
        for fname in pairs:
            counter +=1
            name = dirname + '{}.txt'.format(counter)
            print(name)
            with open(os.path.join(dirname,name),'w') as outfile:
                for indi in fname:
                    indi = dirname + '/{}'.format(indi)
                    with open(indi) as infile:
                        outfile.write(infile.read())
                    outfile.write("\n\n")
        
    if tri_pairs:
        for fname in pairs:
            counter +=1
            name = dirname + '{}.txt'.format(counter)
            with open(os.path.join(dirname,name),'w') as outfile:
                for indi in fname:
                    indi = dirname + '/{}'.format(indi)
                    with open(indi) as infile:
                        outfile.write(infile.read())
                    outfile.write("\n\n")


def main():
    path = "Original-SPDX-Dataset/"
    for roots, dirs, files in os.walk(path,topdown=True):
        for name in files:

            dirname = os.path.splitext(name)[0]
            file = os.path.join(path,name)
            splitter(file,dirname)        






  
   


if __name__ == "__main__":
    main()

    # splitter('Original-SPDX-Dataset/MIT.txt')
    







# def permutation(lst): 
  
    
#     if len(lst) == 0: 
#         return [] 
  

#     if len(lst) == 1: 
#         return [lst] 
  

  
#     l = []
#     for i in range(len(lst)): 
#        m = lst[i] 
  

#        remLst = lst[:i] + lst[i+1:] 
  

#        for p in permutation(remLst): 
#            l.append([m] + p) 
#     return l     

# def pop_random(lst):
#     idx = random.randrange(0,len(lst))
#     return lst.pop(idx)


    # pairs = {}

    # for p in range(len(lst)//2):
    #     pairs[p+1] = (lst.pop(random.randrange(len(lst))),lst.pop(random.randrange(len(lst))))

    # print(pairs)


    # pairs = []
    # while len(lst) >1:
    #     rand1 = pop_random(lst)
    #     rand2 = pop_random(lst)
    #     pair = [rand1, rand2]
    #     pairs.append(pair)
    #     # final_pairs = pairs[-1]
    #     final = set(pairs)
    #     for names in final:
    #         print(names)
