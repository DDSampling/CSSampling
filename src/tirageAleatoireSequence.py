#!C:\Python27
#-*- coding:Utf-8 -*-

__author__ = "DIOP Lamine BSF"

import os
import sys
import math
import csv
import re
import random



# sum of the weightings of the sequences' database
def sommePonderation(maBP):
	return sum(maBP)


#Random draw of a sequence according to its weight
def tirageSequence(contenuBaseSequence,basePonderee,tabSigma):
	i,nbSeq=0,len(contenuBaseSequence)
	somme=tabSigma[nbSeq-1]
	alea=somme*random.random()
	m=trouver(tabSigma,i,nbSeq,alea)
	return contenuBaseSequence[m],basePonderee[m]



def trouver(tab,i,j,x):
	m=(i+j)/2
	if m==0 or (tab[m-1]<x and x<=tab[m]):
		return m
	if tab[m]<x:
		return trouver(tab,m+1,j,x)
	return trouver(tab,i,m,x)
	








