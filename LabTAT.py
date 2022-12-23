import pandas as pd
lab = pd.read_csv("D:\\DS\\books\\ASSIGNMENTS\\Hypothesis testing\\LabTAT.csv")
lab

lab.head()
lab.tail()

# ANOVA ftest statistics :
import scipy.stats as ftable
ft = ftable.f(dfn=4, dfd=120)
ft.ppf(0.95).round(4)

import scipy.stats as stats
Fcalc, pval = stats.f_oneway(lab.iloc[0:,0],lab.iloc[0:,1],lab.iloc[0:,2],lab.iloc[0:,3])

print("F_Calculated value: ", Fcalc)
print("P_value: ", pval)

alpha = 0.05

if pval<alpha:
    print("Ho is Rejected and H1 is Accepted")
else:
    print("Ho is Accepted and H1 is Rejected")
    
# CONCLUSION
"""
In this Ho is Rejected and H1 is Accepted then there is significant 
difference between the laboratories at level of 5%.
"""
    






