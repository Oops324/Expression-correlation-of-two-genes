#!/usr/bin/env python

import numpy as np
import os
import re
import sys
import matplotlib.pyplot as plt
from math import log

def Plot_scatter (exp1_L,exp2_L,gene1,gene2):
	output_fn = "{}-{}".format(gene1, gene2) +"_NT"
	count = len(exp1_L)
	exp1L_Log = [log(float(y),10) for y in exp1_L]
	exp2L_Log = [log(float(y),10) for y in exp2_L]

	fig = plt.figure()
	axes = fig.add_subplot(111, aspect=1.0)
	
	# Calculate the r squared
	corr = np.corrcoef(exp1L_Log, exp2L_Log)[0,1]
	r_squared = corr ** 2
	print "corr:",corr
	print "r_squared:",r_squared
	
	
	# Make the plot
	axes.plot(exp1L_Log, exp2L_Log, 'o', markersize=1)
	plt.xlabel(gene1)
	plt.ylabel(gene2)
	plt.title("FPKM-UQ Counts for {} and {} (n={})".format(gene1, gene2,count))
	

	# Tidy axes
	axes.set_axisbelow(True)
	axes.tick_params(which='both', labelsize=8, direction='out', top=False, right=False)

	# Add a label about r squared
	plt.subplots_adjust(bottom=0.15)
	plt.text(1, -0.15, r'$r^2$ = {:2f}'.format(r_squared),
		horizontalalignment='right', fontsize=8, transform=axes.transAxes)

	# SAVE OUTPUT
	png_fn = "{}.png".format(output_fn)
	pdf_fn = "{}.pdf".format(output_fn)

	#plt.show()
	plt.savefig(png_fn)
	plt.savefig(pdf_fn)
	plt.close(fig)


def GetData(expF,gene1,gene2):
	expF_handle = open(expF,"r")
	exp1_L =[]
	exp2_L =[]

	for line in expF_handle:
		line = line.rstrip()
		if gene1 in line:
			exp1_L = line.split()
		if gene2 in line:
			exp2_L = line.split()
	exp1_L = exp1_L[2:]
	exp2_L = exp2_L[2:]
	return exp1_L,exp2_L
			 

if __name__ == "__main__":
	expF = sys.argv[1]
	gene1 = "HSF1"
	gene2="MAD1L1"

	exp1_L,exp2_L = GetData(expF,gene1,gene2)
	Plot_scatter(exp1_L,exp2_L,gene1,gene2)

