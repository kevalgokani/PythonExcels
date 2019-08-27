# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 13:25:04 2019

@author: ekevgok
"""

import pandas as pd
import numpy as np

dframe=pd.read_excel(r"C:\Other Automation\Pivot Python\LTE.xlsx",sheet_name="LTE")


table1 = dframe.pivot_table(values="LTE_Cell_Availability", index="object",columns="time", aggfunc=np.mean, fill_value=0)
table2 = dframe.pivot_table(values="LTE_Traffic_Data_Volume_DL_MB", index="object",columns="time", aggfunc=np.mean, fill_value=0)
table3 = dframe.pivot_table(values="LTE_Traffic_Data_Volume_UL_MB", index="object",columns="time", aggfunc=np.mean, fill_value=0)
table4 = dframe.pivot_table(values="LTE_VOLTE_TRAFFIC", index="object",columns="time", aggfunc=np.mean, fill_value=0)

writer = pd.ExcelWriter(r"C:\Other Automation\Pivot Python\LTE.xlsx")
dframe.to_excel(writer, sheet_name = 'LTE')
table1.to_excel(writer, sheet_name = 'LTE_Cell_Availability')
table2.to_excel(writer, sheet_name = 'LTE_Traffic_Data_Volume_DL_MB')
table3.to_excel(writer, sheet_name = 'LTE_Traffic_Data_Volume_UL_MB')
table4.to_excel(writer, sheet_name = 'LTE_VOLTE_TRAFFIC')
writer.save()
writer.close()


