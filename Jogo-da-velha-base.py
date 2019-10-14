#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 7 11:16:17 2019

@author: rayssarosa
"""
import numpy as np
import sys
     
Regras = "Para inserir o lugar no tabuleiro digite o número da linha seguido de um espaço seguido do numero da coluna. Exemplo: `3 3` "

#Constantes do jogo
X=1
O=2
dimensao = 3 

 
tabuleiro = []
jogada=0 
ganhador=0 
# 0-> Sem ganhador
# 1-> X ganhou
# 2-> O ganhou

#Função acionada quando jogo acaba
def fimDeJogo():
    global ganhador
    global dimensao
    if ganhador==0 and jogada==dimensao:
        print("O jogo empatou")
        sys.exit()
    elif ganhador==2:
        print("Jogador O ganhou!")
        sys.exit()
    elif ganhador==1:
        print("Jogador X ganhou!")
        sys.exit()
    

#Printando Tabuleiro
def printaTabuleiro():
    global tabuleiro
    global dimensao
    for i in range(dimensao):
        linhai = ""
        for j in range(dimensao):
            linhai += " " +tabuleiro[i][j]+" "
            if j<dimensao-1:
                linhai+= "|" 
        print(linhai)
        if i<dimensao-1:
            print("---+---+---")
        

#Criando tabuleiro
def criaTabuleiro():
    global tabuleiro
    global dimensao
    for i in range(dimensao):
        linha = []
        for j in range(dimensao):
            linha.append(' ')
        tabuleiro.append(linha)
        
#Conferindo se ganhou
def confereTabuleiro():
    global dimensao
    global ganhador
    global tabuleiro
    #confere linhas
    for i in range(dimensao):
        plx=0
        g=True
        #para x
        for j in range(dimensao):
            if tabuleiro[i][j]!= "X":
                g=False
                break
        if g:
            ganhador=X
        g=True
        
        #para O
        for j in range(dimensao):
            if tabuleiro[i][j]!= "O":
                g=False
                break
        if g:
            ganhador=O
        g=True
    
    #confere Colunas
    for j in range(dimensao):
        g=True
        #para x
        for i in range(dimensao):
            if tabuleiro[i][j]!= "X":
                g=False
                break
        if g:
            ganhador=X
        g=True
        
        #para O
        for i in range(dimensao):
            if tabuleiro[i][j]!= "O":
                g=False
                break
        if g:
            ganhador=O
        g=True
            
    #Confere diagonal 1 para x
    g=True
    for i in range(dimensao):
        if tabuleiro[i][i]!= "X":
            g=False
            break
    if g:
        ganhador=X
        
    #Confere diagonal 1 para O
    g=True
    for i in range(dimensao):
        if tabuleiro[i][i]!= "O":
                g=False
                break
    if g:
        ganhador=O
        
    #Confere diagonal 2 para x
    g=True
    for i in range(dimensao):
        if tabuleiro[i][dimensao-1-i]!= "X":
            g=False
            break
    if g:
        ganhador=X
            
    #Confere diagonal 2 para x
    g=True
    for i in range(dimensao):
        if tabuleiro[i][dimensao-1-i]!= "O":
            g=False
            break
    if g:
        ganhador=O
        
def jogo():
    criaTabuleiro()
    global jogada
    for i in range(dimensao*dimensao):
        jogada+=1
        if i % 2 ==0:
            acerto=False
            while acerto==False:
                entrada = input('Jogador X: ')
                entrada.split()
                if tabuleiro[int(entrada[0])-1][int(entrada[2])-1] == " ":
                    acerto=True
                else:
                    print("Opção invalida")
            tabuleiro[int(entrada[0])-1][int(entrada[2])-1] = "X" 
            printaTabuleiro()
        if i % 2 !=0:
            acerto=False
            while acerto==False:
                entrada = input('Jogador O: ')
                entrada.split()
                if tabuleiro[int(entrada[0])-1][int(entrada[2])-1] == " ":
                    acerto=True
                else:
                    print("Opção invalida")
            tabuleiro[int(entrada[0])-1][int(entrada[2])-1] = "O" 
            printaTabuleiro()
        if jogada>(dimensao*2)-2:
            confereTabuleiro()
            fimDeJogo()
jogo()