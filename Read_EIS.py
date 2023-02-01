# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from galvani import BioLogic
import pandas as pd
import os
import matplotlib.pyplot as plt
import glob

for eisfile in glob.glob('*PEIS*.mpr'):
    print(eisfile)
    file = BioLogic.MPRfile(eisfile)
    df = pd.DataFrame(file.data)
    df_Z = df.loc[:, ['freq/Hz', 'Re(Z)/Ohm', '-Im(Z)/Ohm']]
    numbers=["_02_","_04_","_06_","_08_","_10_"]
    voltages=["_3-8V_","_4-1V_","_4-2V_","_4-3V_","_4-4V_"]
    for x in numbers:
        newString=eisfile.replace(x,voltages[numbers.index(x)])
        if newString != eisfile:
            eisfile=newString
            break
    df_Z.to_csv(eisfile[:-4]+'.txt', index=False, sep='\t')
    #df_Z.to_csv(eisfile[:-4]+'.csv', index=False)


#for sample in glob.glob('*.csv'):
#    df1 = pd.read_csv(sample,header=0)
#    fig, ax1 = plt.subplots(1,1)
#    ax1.plot(df1.iloc[:,1], df1.iloc[:,2], 'o', label=sample[:-16])
#    ax1.legend(fontsize=10, frameon = False)
#    ax1.set_xlabel(r'Re(Z) [Ohm]',fontsize=12)
#    ax1.set_ylabel('-Im(Z) [Ohm]', fontsize=12)
#    ax1.tick_params(axis='both', which='major', pad=8, length=8)
#    ax1.grid(lw=0.5, ls=':')
    
#    fig.tight_layout()
    #fig.savefig(sample[:-4]+'.png', dpi=300, facecolor = 'w')

