
# written by cwa -- 21/12/23

import matplotlib.pyplot as plt

# data:
# figures marked pe were supplied by pro-eradicationsists
# figures marked ae were supplied by anti-eradicationsists
pe_max_estimated_deer_population = 900
pe_min_estimated_deer_population = 600
ae_estimated_deer_population = 300
actual_deer_killed = 84
fallow_deer_killed = 66
native_deer_killed = actual_deer_killed - fallow_deer_killed

target_pe_max_estimated_deer_population = pe_max_estimated_deer_population * 0.90
target_pe_min_estimated_deer_population = pe_min_estimated_deer_population * 0.90
target_ae_estimated_deer_population = ae_estimated_deer_population * 0.90

plt.figure(figsize=(15, 9))

# bars for each population estimate
plt.bar('Max Deer Population Estimate \n(pro-eradication)', pe_max_estimated_deer_population, color='#253494')
plt.bar('Min Deer Population Estimate \n(pro-eradication)', pe_min_estimated_deer_population, color='#41b6c4')
plt.bar('Deer Population Estimate \n(anti-eradication)', ae_estimated_deer_population, color='#a1dab4')

# bar for actual deer killed
plt.bar('Actual Deer Killed in Phase 1', native_deer_killed, color='#e34a33', label='Native Deer Killed in Phase 1')
plt.bar('Actual Deer Killed in Phase 1', fallow_deer_killed, color='#fdcc8a', bottom=native_deer_killed, label='Fallow Deer Killed in Phase 1')

# these horizontal lines mark the 90% Phase 1 targets that were set out by Parks Canada (one for each population estimate)
plt.hlines(y=target_pe_max_estimated_deer_population, xmin = 0, xmax=1.95, color='#253494', linestyle=':', label='90% Target for Phase 1 (based on pro-eradication max estimate)')
plt.hlines(y=target_pe_min_estimated_deer_population, xmin = 1, xmax=3.65, color='#41b6c4', linestyle=':', label='90% Target for Phase 1  (based on pro-eradication min estimate)')
plt.hlines(y=target_ae_estimated_deer_population, xmin = 2, xmax=3.65, color='#a1dab4', linestyle=':', label='90% Target for Phase 1  (based on anti-eradication estimate)')

plt.text(1, target_pe_max_estimated_deer_population + 0.1, '90% Phase 1 Target', va='bottom', ha='right', color='#253494')
plt.text(2, target_pe_min_estimated_deer_population + 0.1, '90% Phase 1 Target', va='bottom', ha='right', color='#41b6c4')
plt.text(3, ae_estimated_deer_population + 0.1, '90% Phase 1 Target', va='bottom', ha='right', color='#a1dab4')

plt.vlines(x=3.65, ymin=84, ymax=(target_pe_max_estimated_deer_population + target_pe_min_estimated_deer_population)/2, colors='#fd1717', linestyle='-', label='Discrepancy Between Averaged Target[1] and Outcome')
plt.hlines(y=84, xmin=3.6, xmax=3.7, colors='#fd1717')
plt.hlines(y=(target_pe_max_estimated_deer_population + target_pe_min_estimated_deer_population) / 2, xmin=3.6, xmax=3.7, colors='#fd1717')

plt.title('Fallow Deer Eradication on Sidney Island : Phase 1 Outcome')
plt.ylabel('Number of Deer')
plt.legend()

# quick footnote for the maths
plt.figtext(0.5, 0.01, '[1] Averaged Target was calculated as 90% of 750\n((900)(0.9) + (600)(0.9)) / 2', ha="center", fontsize=10, color="gray")

# labels
plt.text(0, pe_max_estimated_deer_population + 30, f'{pe_max_estimated_deer_population}', ha='center')
plt.text(1, pe_min_estimated_deer_population + 30, f'{pe_min_estimated_deer_population}', ha='center')
plt.text(2, ae_estimated_deer_population + 30, f'{ae_estimated_deer_population}', ha='center')
plt.text(3, actual_deer_killed + 30, f'{actual_deer_killed} (~21% Native Deer)', ha='center')

plt.show()