import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 

surf4 = pd.read_csv('surf4mut_all.csv')

#wide-to-long format
long_surf4 = pd.melt(surf4, id_vars='repl', var_name='LgSURF4', value_name='Luciferase_signal')

#Replicate averages
RepAvg = long_surf4.groupby(['repl', 'LgSURF4'], as_index=False).agg({'Luciferase_signal':"mean"})
RepAvgPivot = RepAvg.pivot_table(columns = 'LgSURF4', values = 'Luciferase_signal', index = 'repl')

#t-tests
statistic, LgNeg_pval = stats.ttest_rel(RepAvgPivot['WT'], RepAvgPivot['LgNeg'])
LgNeg_pval = str(float(round(LgNeg_pval, 6)))
statistic, Phe_loop_pval = stats.ttest_rel(RepAvgPivot['WT'], RepAvgPivot['Phe_loop'])
Phe_loop_pval = str(float(round(Phe_loop_pval, 3)))
statistic, DE_pval = stats.ttest_rel(RepAvgPivot['WT'], RepAvgPivot['DE'])
DE_pval = str(float(round(DE_pval, 3)))
statistic, EW_pval = stats.ttest_rel(RepAvgPivot['WT'], RepAvgPivot['EW'])
EW_pval = str(float(round(EW_pval, 3)))

#plot
sns.swarmplot(x = "LgSURF4", y = "Luciferase_signal", hue = "repl", data = long_surf4, legend = False)

ax = sns.swarmplot(x = "LgSURF4", y = "Luciferase_signal", hue = "repl", size = 10, edgecolor = "k", 
                   linewidth = 1, data = RepAvg, legend = False)

x = -0.2
y = 1.35

plt.text(x, y, LgNeg_pval)
plt.text((x+2), y, Phe_loop_pval)
plt.text((x+3), y, DE_pval)
plt.text((x+4), y, EW_pval)

plt.savefig('SURF4mut_SEC24A.png', dpi = 600)







