#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 1, 2014

@author: anroco

I'm working with lists in python and want to know how I can access a list item?

Estoy trabajando con listas en python y quiero saber ¿como puedo acceder a un
elemento de la lista?
'''

#create a list with numbers
lista = [1, 2, 3, 4, 5]
print (lista)

#get item by index
item = lista[1]
print (item)
item = lista[4]
print (item)

#create a list from a str
lista = list('hello world')
print (lista)

#get item by index negative
item = lista[-2]
print (item)
item = lista[-7]
print (item)
