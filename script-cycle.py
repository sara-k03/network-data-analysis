import matplotlib.pyplot as plt
from cycle_separation import *
from fits import *
from plot_cycle import * 

cycle = 5

# a-values
a_values = [ 0, 0.25, 0.5, 0.75, 1 ]

# RAW DATA

"""ORIENTATION O"""

# V, a=0
compression_x_raw_VA0_O, compression_y_raw_VA0_O, release_x_raw_VA0_O, release_y_raw_VA0_O = cycle_separation("DATA/PC0204N6_Voronoi_1.5mm_75mm_a0_OrientationO.csv", n=cycle, foam_load=38)
# V, a=0.25
compression_x_raw_VA25_O, compression_y_raw_VA25_O, release_x_raw_VA25_O, release_y_raw_VA25_O = cycle_separation("DATA/PC216V3D_Voronoi_1.5mm_75mm_a0.25_OrientationO.csv", n=cycle, foam_load=36)
# V, a=0.5
compression_x_raw_VA5_O, compression_y_raw_VA5_O, release_x_raw_VA5_O, release_y_raw_VA5_O = cycle_separation("DATA/PC216V3D_Voronoi_1.5mm_75mm_a0.5_OrientationO.csv", n=cycle, foam_load=36)
# V, a=0.75
compression_x_raw_VA75_O, compression_y_raw_VA75_O, release_x_raw_VA75_O, release_y_raw_VA75_O = cycle_separation("DATA/PC216V3D_Voronoi_1.5mm_75mm_a0.75_OrientationO.csv", n=cycle, foam_load=44)
# V, a=1
compression_x_raw_VA1_O, compression_y_raw_VA1_O, release_x_raw_VA1_O, release_y_raw_VA1_O = cycle_separation("DATA/PC216V3D_Voronoi_1.5mm_75mm_a1_OrientationO.csv", n=cycle, foam_load=36)
# D, a=0.5
compression_x_raw_DA5_O, compression_y_raw_DA5_O, release_x_raw_DA5_O, release_y_raw_DA5_O = cycle_separation("DATA/PC216D3D_Delaunay_1.5mm_75mm_a0.5_orientationO.csv", n=cycle, foam_load=36)
# C, a=0.5
compression_x_raw_CA5_O, compression_y_raw_CA5_O, release_x_raw_CA5_O, release_y_raw_CA5_O = cycle_separation("DATA/PC216C3D_Centroidal_1.5mm_75mm_a0.5_OrientationO.csv", n=cycle, foam_load=36)
# G, a=0.5
compression_x_raw_GA5_O, compression_y_raw_GA5_O, release_x_raw_GA5_O, release_y_raw_GA5_O = cycle_separation("DATA/PC216G3D_Gabriel_1.5mm_75mm_a0.5_orientationO.csv", n=cycle, foam_load=36)

# EXTRACTING LINEAR MODULI FOR ALL VORONOI
# a=0
lm_0_O, lm_0err_O, lf_x_up_VA0_O, lf_y_up_VA0_O, lf_comp_eq_VA0_O, lf_x_down_VA0_O, lf_y_down_VA0_O, lf_rel_eq_VA0_O = linear_fit( compression_x_raw_VA0_O, compression_y_raw_VA0_O, release_x_raw_VA0_O, release_y_raw_VA0_O )
# a=0.25
lm_25_O, lm_25err_O, lf_x_up_VA25_O, lf_y_up_VA25_O, lf_comp_eq_VA25_O, lf_x_down_VA25_O, lf_y_down_VA25_O, lf_rel_eq_VA25_O = linear_fit( compression_x_raw_VA25_O, compression_y_raw_VA25_O, release_x_raw_VA25_O, release_y_raw_VA25_O )
# a=0.5
lm_5_O, lm_5err_O, lf_x_up_VA5_O, lf_y_up_VA5_O, lf_comp_eq_VA5_O, lf_x_down_VA5_O, lf_y_down_VA5_O, lf_rel_eq_VA5_O = linear_fit( compression_x_raw_VA5_O, compression_y_raw_VA5_O, release_x_raw_VA5_O, release_y_raw_VA5_O )
# a=0.75
lm_75_O, lm_75err_O, lf_x_up_VA75_O, lf_y_up_VA75_O, lf_comp_eq_VA75_O, lf_x_down_VA75_O, lf_y_down_VA75_O, lf_rel_eq_VA75_O = linear_fit( compression_x_raw_VA75_O, compression_y_raw_VA75_O, release_x_raw_VA75_O, release_y_raw_VA75_O )
# a=1
lm_1_O, lm_1err_O, lf_x_up_VA1_O, lf_y_up_VA1_O, lf_comp_eq_VA1_O, lf_x_down_VA1_O, lf_y_down_VA1_O, lf_rel_eq_VA1_O = linear_fit( compression_x_raw_VA1_O, compression_y_raw_VA1_O, release_x_raw_VA1_O, release_y_raw_VA1_O )

linear_moduli_O = [ lm_0_O, lm_25_O, lm_5_O, lm_75_O, lm_1_O ]
linear_moduli_err_O = [ lm_0err_O, lm_25err_O, lm_5err_O, lm_75err_O, lm_1err_O ]

# EXTRACTING UPWARDS & DOWNWARDS EXPONENT FOR ALL VORONOI
# a=0
c_0_O, r_0_O, pf_x_up_VA0_O, pf_y_up_VA0_O, pf_comp_eq_VA0_O, pf_x_down_VA0_O, pf_y_down_VA0_O, pf_rel_eq_VA0_O, c_0err_O, r_0err_O = power_fit( compression_x_raw_VA0_O, compression_y_raw_VA0_O, release_x_raw_VA0_O, release_y_raw_VA0_O )
# a=0.25
c_25_O, r_25_O, pf_x_up_VA25_O, pf_y_up_VA25_O, pf_comp_eq_VA25_O, pf_x_down_VA25_O, pf_y_down_VA25_O, pf_rel_eq_VA25_O, c_25err_O, r_25err_O = power_fit( compression_x_raw_VA25_O, compression_y_raw_VA25_O, release_x_raw_VA25_O, release_y_raw_VA25_O )
# a=0.5
c_5_O, r_5_O, pf_x_up_VA5_O, pf_y_up_VA5_O, pf_comp_eq_VA5_O, pf_x_down_VA5_O, pf_y_down_VA5_O, pf_rel_eq_VA5_O, c_5err_O, r_5err_O = power_fit( compression_x_raw_VA5_O, compression_y_raw_VA5_O, release_x_raw_VA5_O, release_y_raw_VA5_O )
# a=0.75
c_75_O, r_75_O, pf_x_up_VA75_O, pf_y_up_VA75_O, pf_comp_eq_VA75_O, pf_x_down_VA75_O, pf_y_down_VA75_O, pf_rel_eq_VA75_O, c_75err_O, r_75err_O = power_fit( compression_x_raw_VA75_O, compression_y_raw_VA75_O, release_x_raw_VA75_O, release_y_raw_VA75_O )
# a=1
c_1_O, r_1_O, pf_x_up_VA1_O, pf_y_up_VA1_O, pf_comp_eq_VA1_O, pf_x_down_VA1_O, pf_y_down_VA1_O, pf_rel_eq_VA1_O, c_1err_O, r_1err_O = power_fit( compression_x_raw_VA1_O, compression_y_raw_VA1_O, release_x_raw_VA1_O, release_y_raw_VA1_O )

# Arrays
compression_exponents_O = [c_0_O, c_25_O, c_5_O, c_75_O, c_1_O]
release_exponents_O = [r_0_O, r_25_O, r_5_O, r_75_O, r_1_O]
compression_errors_O = [c_0err_O, c_25err_O, c_5err_O, c_75err_O, c_1err_O]
release_errors_O = [r_0err_O, r_25err_O, r_5err_O, r_75err_O, r_1err_O]

"""ORIENTATION 1"""

# V, a=0
compression_x_raw_VA0_1, compression_y_raw_VA0_1, release_x_raw_VA0_1, release_y_raw_VA0_1 = cycle_separation("DATA/PC0204N6_Voronoi_1.5mm_75mm_a0_Orientation1.csv", n=cycle, foam_load=70) # MIGHT NEED TO RETAKE
# V, a=0.25
compression_x_raw_VA25_1, compression_y_raw_VA25_1, release_x_raw_VA25_1, release_y_raw_VA25_1 = cycle_separation("DATA/PC216V3D_Voronoi_1.5mm_75mm_a0.25_Orientation1.csv", n=cycle, foam_load=36)
# V, a=0.5
compression_x_raw_VA5_1, compression_y_raw_VA5_1, release_x_raw_VA5_1, release_y_raw_VA5_1 = cycle_separation("DATA/PC216V3D_Voronoi_1.5mm_75mm_a0.5_Orientation1.csv", n=cycle, foam_load=36)
# V, a=0.75
compression_x_raw_VA75_1, compression_y_raw_VA75_1, release_x_raw_VA75_1, release_y_raw_VA75_1 = cycle_separation("DATA/PC216V3D_Voronoi_1.5mm_75mm_a0.75_Orientation1.csv", n=cycle, foam_load=76) # MIGHT NEED TO RETAKE
# V, a=1
compression_x_raw_VA1_1, compression_y_raw_VA1_1, release_x_raw_VA1_1, release_y_raw_VA1_1 = cycle_separation("DATA/PC216V3D_Voronoi_1.5mm_75mm_a1_Orientation1.csv", n=cycle, foam_load=47)
# D, a=0.5
compression_x_raw_DA5_1, compression_y_raw_DA5_1, release_x_raw_DA5_1, release_y_raw_DA5_1 = cycle_separation("DATA/PC216D3D_Delaunay_1.5mm_75mm_a0.5_orientation1.csv", n=cycle, foam_load=36)
# C, a=0.5
compression_x_raw_CA5_1, compression_y_raw_CA5_1, release_x_raw_CA5_1, release_y_raw_CA5_1 = cycle_separation("DATA/PC216C3D_Centroidal_1.5mm_75mm_a0.5_Orientation1.csv", n=cycle, foam_load=36)
# G, a=0.5
compression_x_raw_GA5_1, compression_y_raw_GA5_1, release_x_raw_GA5_1, release_y_raw_GA5_1 = cycle_separation("DATA/PC216G3D_Gabriel_1.5mm_75mm_a0.5_orientation1.csv", n=cycle, foam_load=36)

# EXTRACTING LINEAR MODULI FOR ALL VORONOI
# a=0
lm_0_1, lm_0err_1, lf_x_up_VA0_1, lf_y_up_VA0_1, lf_comp_eq_VA0_1, lf_x_down_VA0_1, lf_y_down_VA0_1, lf_rel_eq_VA0_1 = linear_fit( compression_x_raw_VA0_1, compression_y_raw_VA0_1, release_x_raw_VA0_1, release_y_raw_VA0_1 )
# a=0.25
lm_25_1, lm_25err_1, lf_x_up_VA25_1, lf_y_up_VA25_1, lf_comp_eq_VA25_1, lf_x_down_VA25_1, lf_y_down_VA25_1, lf_rel_eq_VA25_1 = linear_fit( compression_x_raw_VA25_1, compression_y_raw_VA25_1, release_x_raw_VA25_1, release_y_raw_VA25_1 )
# a=0.5
lm_5_1, lm_5err_1, lf_x_up_VA5_1, lf_y_up_VA5_1, lf_comp_eq_VA5_1, lf_x_down_VA5_1, lf_y_down_VA5_1, lf_rel_eq_VA5_1 = linear_fit( compression_x_raw_VA5_1, compression_y_raw_VA5_1, release_x_raw_VA5_1, release_y_raw_VA5_1 )
# a=0.75
lm_75_1, lm_75err_1, lf_x_up_VA75_1, lf_y_up_VA75_1, lf_comp_eq_VA75_1, lf_x_down_VA75_1, lf_y_down_VA75_1, lf_rel_eq_VA75_1 = linear_fit( compression_x_raw_VA75_1, compression_y_raw_VA75_1, release_x_raw_VA75_1, release_y_raw_VA75_1 )
# a=1
lm_1_1, lm_1err_1, lf_x_up_VA1_1, lf_y_up_VA1_1, lf_comp_eq_VA1_1, lf_x_down_VA1_1, lf_y_down_VA1_1, lf_rel_eq_VA1_1 = linear_fit( compression_x_raw_VA1_1, compression_y_raw_VA1_1, release_x_raw_VA1_1, release_y_raw_VA1_1 )

linear_moduli_1 = [ lm_0_1, lm_25_1, lm_5_1, lm_75_1, lm_1_1 ]
linear_moduli_err_1 = [ lm_0err_1, lm_25err_1, lm_5err_1, lm_75err_1, lm_1err_1 ]

# EXTRACTING UPWARDS & DOWNWARDS EXPONENT FOR ALL VORONOI
# a=0
c_0_1, r_0_1, pf_x_up_VA0_1, pf_y_up_VA0_1, pf_comp_eq_VA0_1, pf_x_down_VA0_1, pf_y_down_VA0_1, pf_rel_eq_VA0_1, c_0err_1, r_0err_1 = power_fit( compression_x_raw_VA0_1, compression_y_raw_VA0_1, release_x_raw_VA0_1, release_y_raw_VA0_1 )
# a=0.25
c_25_1, r_25_1, pf_x_up_VA25_1, pf_y_up_VA25_1, pf_comp_eq_VA25_1, pf_x_down_VA25_1, pf_y_down_VA25_1, pf_rel_eq_VA25_1, c_25err_1, r_25err_1 = power_fit( compression_x_raw_VA25_1, compression_y_raw_VA25_1, release_x_raw_VA25_1, release_y_raw_VA25_1 )
# a=0.5
c_5_1, r_5_1, pf_x_up_VA5_1, pf_y_up_VA5_1, pf_comp_eq_VA5_1, pf_x_down_VA5_1, pf_y_down_VA5_1, pf_rel_eq_VA5_1, c_5err_1, r_5err_1 = power_fit( compression_x_raw_VA5_1, compression_y_raw_VA5_1, release_x_raw_VA5_1, release_y_raw_VA5_1 )
# a=0.75
c_75_1, r_75_1, pf_x_up_VA75_1, pf_y_up_VA75_1, pf_comp_eq_VA75_1, pf_x_down_VA75_1, pf_y_down_VA75_1, pf_rel_eq_VA75_1, c_75err_1, r_75err_1 = power_fit( compression_x_raw_VA75_1, compression_y_raw_VA75_1, release_x_raw_VA75_1, release_y_raw_VA75_1 )
# a=1
c_1_1, r_1_1, pf_x_up_VA1_1, pf_y_up_VA1_1, pf_comp_eq_VA1_1, pf_x_down_VA1_1, pf_y_down_VA1_1, pf_rel_eq_VA1_1, c_1err_1, r_1err_1 = power_fit( compression_x_raw_VA1_1, compression_y_raw_VA1_1, release_x_raw_VA1_1, release_y_raw_VA1_1 )

# Arrays
compression_exponents_1 = [c_0_1, c_25_1, c_5_1, c_75_1, c_1_1]
release_exponents_1 = [r_0_1, r_25_1, r_5_1, r_75_1, r_1_1]
compression_errors_1 = [c_0err_1, c_25err_1, c_5err_1, c_75err_1, c_1err_1]
release_errors_1 = [r_0err_1, r_25err_1, r_5err_1, r_75err_1, r_1err_1]

# Plotting 
"""
Things to plot 
- Compression Exponent vs. Disorder Factor (All Cycles, both Orientations)
- Release Exponent vs. Disorder Factor (All Cycles, both Orientations)
- Linear Exponent vs. Disorder Factor (All Cycles, both Orientations)
- Create a quick function to comment out to plot a cycle, power fit, and linear fit
- Total Edge Length vs. Linear Modulus
- Mass vs. Linear Modulus
- Average Number of Edges per Node (Degree) vs. Linear Modulus
Network package: https://networkx.org/en/ 
"""

"""Linear Moduli vs. Mass"""

# add here

"""Exponents vs. Mass"""
# add here

"""Exponents vs. Average Degree"""

# Useless messure, a=0 is 5, and the rest of them are all 4

"""Specific Modulus (Linear Modulus/Mass) vs. Disorder"""

fig, ax = plt.subplots()

masses = [10.13, 17.26, 17.58, 17.85, 18.25]
specific_modulus_O = [0] * 5
specific_modulus_1 = [0] * 5
specfic_modulus_0_err = [0] * 5
specfic_modulus_1_err = [0] * 5

for i in range(len(masses)):
    specific_modulus_O[i] = linear_moduli_O[i] / masses[i]
    specific_modulus_1[i] = linear_moduli_1[i] / masses[i]
    specfic_modulus_0_err[i] = linear_moduli_err_O[i] / masses[i]
    specfic_modulus_1_err[i] = linear_moduli_err_1[i] / masses[i]

markers = ['o', 's', '^', 'D', 'P']  # circle, square, triangle, diamond, plus
colors = ["#C1C187", '#a1dab4', '#41b6c4', '#2c7fb8', '#253494']

for i in range(len(a_values)):
    ax.errorbar(a_values[i], specific_modulus_O[i], yerr=specfic_modulus_0_err[i],
                fmt=markers[i], color=colors[i], markersize=12, capsize=8,
                elinewidth=2, label=f"a={a_values[i]}")
    ax.errorbar(a_values[i], specific_modulus_1[i], yerr=specfic_modulus_1_err[i],
                fmt=markers[i], color=colors[i], markersize=12, capsize=8,
                elinewidth=2)

ax.set_xlabel("Kick Size, α", fontsize=12)
ax.set_ylabel(r"Specific Modulus, $\mathrm{N\ mm^{-1}\ kg^{-1}}$", fontsize=12)
ax.set_xticks(a_values)
ax.set_ylim(bottom=0, top=0.50) # Changed, 3/17, 9:13
ax.legend()

plt.tick_params(axis='both', labelsize=12)
plt.title(f"Cycle {cycle}")
plt.savefig(f"plots/Specific-Modulus-vs-Disorder-Cycle{cycle}.png")
plt.savefig(f"plots/Specific-Modulus-vs-Disorder-Cycle{cycle}.pdf")

"""Linear Moduli vs. Disorder"""

# add here

"""Exponents Cycle vs. Disorder"""

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), sharey=True)

markers = ['o', 's', '^', 'D', 'P']
colors = ["#C1C187", '#a1dab4', '#41b6c4', '#2c7fb8', '#253494']

for i in range(len(a_values)):
    ax1.errorbar(a_values[i], compression_exponents_O[i], yerr=compression_errors_O[i],
                 fmt=markers[i], color=colors[i], markersize=12, capsize=8,
                 elinewidth=2, label=f"a={a_values[i]}")
    ax1.errorbar(a_values[i], compression_exponents_1[i], yerr=compression_errors_1[i],
                 fmt=markers[i], color=colors[i], markersize=12, capsize=8,
                 elinewidth=2)

    ax2.errorbar(a_values[i], release_exponents_O[i], yerr=release_errors_O[i],
                 fmt=markers[i], color=colors[i], markersize=12, capsize=8,
                 elinewidth=2, label=f"a={a_values[i]}")
    ax2.errorbar(a_values[i], release_exponents_1[i], yerr=release_errors_1[i],
                 fmt=markers[i], color=colors[i], markersize=12, capsize=8,
                 elinewidth=2)

ax1.set_xlabel("Kick Size, α", fontsize=12)
ax1.set_ylabel("Compression Exponent", fontsize=12)
ax2.set_xlabel("Kick Size, α", fontsize=12)
ax2.set_ylabel("Release Exponent", fontsize=12)
ax1.set_xticks(a_values)
ax2.set_xticks(a_values)
ax1.set_ylim(bottom=0)
ax1.legend()

plt.tick_params(axis='both', labelsize=12)
fig.suptitle(f"Cycle {cycle}")
plt.tight_layout()
plt.savefig(f"plots/Exponents-vs-Disorder-Cycle{cycle}.png")
plt.savefig(f"plots/Exponents-vs-Disorder-Cycle{cycle}.pdf")

"""Specific Modulus vs. All_Triangles"""

fig, ax = plt.subplots()

masses = [10.13, 17.26, 17.58, 17.85, 18.25]
specific_modulus_O = [0] * 5
specific_modulus_1 = [0] * 5
specific_modulus_O_err = [0] * 5
specific_modulus_1_err = [0] * 5

for i in range(len(masses)):
    specific_modulus_O[i] = linear_moduli_O[i] / masses[i]
    specific_modulus_1[i] = linear_moduli_1[i] / masses[i]
    specific_modulus_O_err[i] = linear_moduli_err_O[i] / masses[i]
    specific_modulus_1_err[i] = linear_moduli_err_1[i] / masses[i]

# Omitting a=0
specific_moduli_O_clipped = specific_modulus_O[1:]
specific_moduli_1_clipped = specific_modulus_1[1:]
specific_moduli_err_O_clipped = specific_modulus_O_err[1:]
specific_moduli_err_1_clipped = specfic_modulus_1_err[1:]

# 0.25, 0.50, 0.75, 1.00
all_triangles = [299, 207, 185, 209]

markers = ['o', 's', '^', 'D', 'P']
colors = ["#C1C187", '#a1dab4', '#41b6c4', '#2c7fb8', '#253494']

for i in range(len(all_triangles)):
    ax.errorbar(all_triangles[i], specific_moduli_O_clipped[i], yerr=specific_moduli_err_O_clipped[i],
                fmt=markers[i], color=colors[i], markersize=12, capsize=8,
                elinewidth=2, label=f"a={a_values[i+1]}, {all_triangles[i]} triangles")
    ax.errorbar(all_triangles[i], specific_moduli_1_clipped[i], yerr=specific_moduli_err_1_clipped[i],
                fmt=markers[i], color=colors[i], markersize=12, capsize=8,
                elinewidth=2)

ax.set_xlabel("Num. of Triangles", fontsize=12)
ax.set_ylabel(r"Specific Modulus, $\mathrm{N\ mm^{-1}\ kg^{-1}}$", fontsize=12)
ax.set_ylim(bottom=0, top=0.28) # Changed, 3/17, 9:13
ax.legend()

plt.tick_params(axis='both', labelsize=12)
plt.title(f"Cycle {cycle}")
plt.savefig(f"plots/Specific-Modulus-vs-Num-Triangles-Cycle{cycle}.png")
plt.savefig(f"plots/Specific-Modulus-vs-Num-Triangles-Cycle{cycle}.pdf")

"""Specific Modulus vs. Node Betweenness Centrality 
- High Mean Betweenness - The network has a few highly critical nodes that dominate stress transfer
- Low Mean Betweenness - Stress paths are more evenly distributed across a lot of nodes
The mean betweenness is the average of of the betweenness between all pairs of nodes in the graph
"""

# Version without a=0

fig, ax = plt.subplots()

# 0, 0.25, 0.50, 0.75, 1.00 
# a=0 --> 0.022712453814388175
mean_betweenness = [0.007172267683872396, 0.007322198192188916, 0.007361541599991833, 0.00768314864078401] 

markers = ['o', 's', '^', 'D', 'P']
colors = ["#C1C187", '#a1dab4', '#41b6c4', '#2c7fb8', '#253494']

for i in range(len(mean_betweenness)):
    ax.errorbar(mean_betweenness[i], specific_moduli_O_clipped[i], yerr=specific_moduli_err_O_clipped[i],
                fmt=markers[i], color=colors[i], markersize=12, capsize=8,
                elinewidth=2, label=f"a={a_values[i+1]}, BC={mean_betweenness[i]:.4f}")
    ax.errorbar(mean_betweenness[i], specific_moduli_1_clipped[i], yerr=specific_moduli_err_1_clipped[i],
                fmt=markers[i], color=colors[i], markersize=12, capsize=8,
                elinewidth=2)

ax.set_xlabel("Mean Node Betweenness Centrality", fontsize=12)
ax.set_ylabel(r"Specific Modulus, $\mathrm{N\ mm^{-1}\ kg^{-1}}$", fontsize=12)
ax.set_ylim(bottom=0, top=0.28) # Changed, 3/17, 9:13
ax.legend()

plt.tick_params(axis='both', labelsize=12)
plt.title(f"Cycle {cycle}")
plt.savefig(f"plots/Specific-Modulus-vs-Node-Betweenness-Centrality-Cycle{cycle}.png")
plt.savefig(f"plots/Specific-Modulus-vs-Node-Betweenness-Centrality-Cycle{cycle}.pdf")

# Version with a=0

fig, ax = plt.subplots()

# 0, 0.25, 0.50, 0.75, 1.00 
# a=0 --> 0.022712453814388175
mean_betweenness = [0.022712453814388175, 0.007172267683872396, 0.007322198192188916, 0.007361541599991833, 0.00768314864078401] 

markers = ['o', 's', '^', 'D', 'P']
colors = ["#C1C187", '#a1dab4', '#41b6c4', '#2c7fb8', '#253494']

for i in range(len(mean_betweenness)):
    ax.errorbar(mean_betweenness[i], specific_modulus_O[i], yerr=specific_modulus_O_err[i],
                fmt=markers[i], color=colors[i], markersize=12, capsize=8,
                elinewidth=2, label=f"a={a_values[i]}, BC={mean_betweenness[i]:.4f}")
    ax.errorbar(mean_betweenness[i], specific_modulus_1[i], yerr=specific_modulus_1_err[i],
                fmt=markers[i], color=colors[i], markersize=12, capsize=8,
                elinewidth=2)

ax.set_xlabel("Mean Betweenness Centrality", fontsize=12)
ax.set_ylabel(r"Specific Modulus, $\mathrm{N\ mm^{-1}\ kg^{-1}}$", fontsize=12)
ax.set_ylim(bottom=0, top=0.28) # Changed, 3/17, 9:13
ax.legend()

plt.tick_params(axis='both', labelsize=12)
plt.title(f"Cycle {cycle}")
plt.savefig(f"plots/Specific-Modulus-vs-Betweenness-Centrality-Version2-Cycle{cycle}.png")
plt.savefig(f"plots/Specific-Modulus-vs-Betweenness-Centrality-Version2-Cycle{cycle}.pdf")

"""Betweeness Centrality vs. Disorder"""

fig, ax = plt.subplots(figsize=(8, 6))

# 0, 0.25, 0.50, 0.75, 1.00
mean_betweenness_all = [0.007172267683872396, 0.007322198192188916, 0.007361541599991833, 0.00768314864078401]
a_values = [0.25, 0.5, 0.75, 1]

markers = ['o', 's', '^', 'D', 'P']
colors = ["#C1C187", '#a1dab4', '#41b6c4', '#2c7fb8', '#253494']

for i in range(len(mean_betweenness_all)):
    ax.plot(a_values[i], mean_betweenness_all[i],
            marker=markers[i], color=colors[i], markersize=12,
            label=f"a={a_values[i]}, BC={mean_betweenness_all[i]:.4f}")

ax.set_xlabel("Disorder, $α$", fontsize=12)
ax.set_ylabel("Mean Betweenness Centrality", fontsize=12)
ax.set_xticks(a_values)
ax.set_xlim(left=0)
ax.legend()

plt.tick_params(axis='both', labelsize=12)
plt.title(f"Cycle {cycle}")
plt.savefig(f"plots/Betweenness-Centrality-vs-Disorder-Cycle{cycle}.png")
plt.savefig(f"plots/Betweenness-Centrality-vs-Disorder-Cycle{cycle}.pdf")

# Version with a=0

fig, ax = plt.subplots(figsize=(8, 6))

# 0, 0.25, 0.50, 0.75, 1.00
mean_betweenness_all = [0.022712453814388175, 0.007172267683872396, 0.007322198192188916, 0.007361541599991833, 0.00768314864078401]
a_values = [0, 0.25, 0.5, 0.75, 1]

markers = ['o', 's', '^', 'D', 'P']
colors = ["#C1C187", '#a1dab4', '#41b6c4', '#2c7fb8', '#253494']

for i in range(len(mean_betweenness_all)):
    ax.plot(a_values[i], mean_betweenness_all[i],
            marker=markers[i], color=colors[i], markersize=12,
            label=f"a={a_values[i]}, BC={mean_betweenness_all[i]:.4f}")

ax.set_xlabel("Disorder, $a$", fontsize=12)
ax.set_ylabel("Mean Betweenness Centrality", fontsize=12)
ax.set_xticks(a_values)
ax.set_ylim(bottom=0)
ax.legend()

plt.tick_params(axis='both', labelsize=12)
plt.title(f"Cycle {cycle}")
plt.savefig(f"plots/Betweenness-Centrality-vs-Disorder-Version2-Cycle{cycle}.png")
plt.savefig(f"plots/Betweenness-Centrality-vs-Disorder-Version2-Cycle{cycle}.pdf")

"""Number of Triangles vs Disorder"""

fig, ax = plt.subplots()

# 0, 0.25, 0.50, 0.75, 1.00
all_triangles = [0, 299, 207, 185, 209]
a_values = [0, 0.25, 0.5, 0.75, 1]

markers = ['o', 's', '^', 'D', 'P']
colors = ["#C1C187", '#a1dab4', '#41b6c4', '#2c7fb8', '#253494']

for i in range(len(all_triangles)):
    ax.plot(a_values[i], all_triangles[i],
            marker=markers[i], color=colors[i], markersize=12,
            label=f"a={a_values[i]}")

ax.set_xlabel("Disorder, $α$", fontsize=12)
ax.set_ylabel("Num. of Triangles", fontsize=12)
ax.set_xticks(a_values)
ax.set_ylim(bottom=0)
ax.legend()

plt.tick_params(axis='both', labelsize=12)
plt.title(f"Cycle {cycle}")
plt.savefig(f"plots/Num-Triangles-vs-Disorder-Cycle{cycle}.png")
plt.savefig(f"plots/Num-Triangles-vs-Disorder-Cycle{cycle}.pdf")

"""Plotting a cycle"""

fig, ax = plt.subplots(figsize=(10, 6))

# Shift raw data to origin (same shift applied internally by the fit functions)
comp_x_shifted, comp_y_shifted, rel_x_shifted, rel_y_shifted, _, _ = shift_raw(compression_x_raw_VA5_O, compression_y_raw_VA5_O, release_x_raw_VA5_O, release_y_raw_VA5_O)

# Raw data
plot_cycle(comp_x_shifted, comp_y_shifted, "Displacement (mm)", "Force (N)", "Compression (raw)", "Black", ax, "None", "--")
plot_cycle(rel_x_shifted, rel_y_shifted, "Displacement (mm)", "Force (N)", "Release (raw)", "Gray", ax, "None", "--")

# Power fits
plot_cycle(pf_x_up_VA5_O, pf_y_up_VA5_O, "Displacement (mm)", "Force (N)", f"Power fit compression: {pf_comp_eq_VA5_O}", "Red", ax, "None", "-")
plot_cycle(pf_x_down_VA5_O, pf_y_down_VA5_O, "Displacement (mm)", "Force (N)", f"Power fit release: {pf_rel_eq_VA5_O}", "Orange", ax, "None", "-")

# Linear fit
plot_cycle(lf_x_down_VA5_O, lf_y_down_VA5_O, "Displacement (mm)", "Force (N)", f"Linear fit release: {lf_rel_eq_VA5_O}", "Cyan", ax, "None", "-")

ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
ax.set_xlim(left=0)
ax.set_ylim(bottom=0)

plt.title("Voronoi, a=0.5, Cycle 5")
plt.tight_layout()
plt.tick_params(axis='both', labelsize=12)
plt.savefig(f"plots/Voronoi-a0.5-OrientationO-Cycle{cycle}.png")
plt.savefig(f"plots/Voronoi-a0.5-OrientationO-Cycle{cycle}.pdf")

"""Specific Modulus vs. Clustering Coefficient"""

# .25, .5, .75, 1
# a=0 --> 0
mean_clustering = [0.06686046511627906, 0.048820754716981135, 0.043549905838041435, 0.05026455026455026]

fig, ax = plt.subplots()

masses = [10.13, 17.26, 17.58, 17.85, 18.25]
specific_modulus_O = [0] * 5
specific_modulus_1 = [0] * 5
specific_modulus_O_err = [0] * 5
specific_modulus_1_err = [0] * 5

for i in range(len(masses)):
    specific_modulus_O[i] = linear_moduli_O[i] / masses[i]
    specific_modulus_1[i] = linear_moduli_1[i] / masses[i]
    specific_modulus_O_err[i] = linear_moduli_err_O[i] / masses[i]
    specific_modulus_1_err[i] = linear_moduli_err_1[i] / masses[i]

# Omitting a=0
specific_moduli_O_clipped = specific_modulus_O[1:]
specific_moduli_1_clipped = specific_modulus_1[1:]
specific_moduli_err_O_clipped = specific_modulus_O_err[1:]
specific_moduli_err_1_clipped = specfic_modulus_1_err[1:]

markers = ['o', 's', '^', 'D', 'P']
colors = ["#C1C187", '#a1dab4', '#41b6c4', '#2c7fb8', '#253494']

for i in range(len(mean_clustering)):
    ax.errorbar(mean_clustering[i], specific_moduli_O_clipped[i], yerr=specific_moduli_err_O_clipped[i],
                fmt=markers[i], color=colors[i], markersize=12, capsize=8,
                elinewidth=2, label=f"a={a_values[i+1]}, CC={mean_clustering[i]:.4f}")
    ax.errorbar(mean_clustering[i], specific_moduli_1_clipped[i], yerr=specific_moduli_err_1_clipped[i],
                fmt=markers[i], color=colors[i], markersize=12, capsize=8,
                elinewidth=2)

ax.set_xlabel("Mean Clustering Coefficient", fontsize=12)
ax.set_ylabel(r"Specific Modulus, $\mathrm{N\ mm^{-1}\ kg^{-1}}$", fontsize=12)
# ax.set_ylim(bottom=0)
ax.set_ylim(bottom=0, top=0.28) # Changed, 3/17, 9:13
ax.legend()

plt.tick_params(axis='both', labelsize=12)
plt.title(f"Cycle {cycle}")
plt.tight_layout()
plt.savefig(f"plots/Specific-Modulus-vs-Clustering-Coefficient-Cycle{cycle}.png", bbox_inches='tight')
plt.savefig(f"plots/Specific-Modulus-vs-Clustering-Coefficient-Cycle{cycle}.pdf", bbox_inches='tight')

# Without a=0

# 0, .25, .5, .75, 1
mean_clustering = [0, 0.06686046511627906, 0.048820754716981135, 0.043549905838041435, 0.05026455026455026]

fig, ax = plt.subplots()

markers = ['o', 's', '^', 'D', 'P']
colors = ["#C1C187", '#a1dab4', '#41b6c4', '#2c7fb8', '#253494']

for i in range(len(mean_clustering)):
    ax.errorbar(mean_clustering[i], specific_modulus_O[i], yerr=specific_modulus_O_err[i],
                fmt=markers[i], color=colors[i], markersize=12, capsize=8,
                elinewidth=2, label=f"a={a_values[i]}, CC={mean_clustering[i]:.4f}")
    ax.errorbar(mean_clustering[i], specific_modulus_1[i], yerr=specific_modulus_1_err[i],
                fmt=markers[i], color=colors[i], markersize=12, capsize=8,
                elinewidth=2)

ax.set_xlabel("Mean Clustering Coefficient", fontsize=12)
ax.set_ylabel(r"Specific Modulus, $\mathrm{N\ mm^{-1}\ kg^{-1}}$", fontsize=12)
ax.set_ylim(bottom=0, top=0.28) # Changed, 3/17, 9:13
ax.legend()

plt.tick_params(axis='both', labelsize=12)
plt.title(f"Cycle {cycle}")
plt.tight_layout()
plt.savefig(f"plots/Specific-Modulus-vs-Clustering-Coefficient-Version2-Cycle{cycle}.png")
plt.savefig(f"plots/Specific-Modulus-vs-Clustering-Coefficient-Version2-Cycle{cycle}.pdf")

"""Clustering Coefficient vs. Disorder"""

# 0, 0.25, 0.50, 0.75, 1.00
mean_clustering_all = [0, 0.06686046511627906, 0.048820754716981135, 0.043549905838041435, 0.05026455026455026]
a_values = [0, 0.25, 0.5, 0.75, 1]

fig, ax = plt.subplots(figsize=(8, 6))

markers = ['o', 's', '^', 'D', 'P']
colors = ["#C1C187", '#a1dab4', '#41b6c4', '#2c7fb8', '#253494']

for i in range(len(mean_clustering_all)):
    ax.plot(a_values[i], mean_clustering_all[i],
            marker=markers[i], color=colors[i], markersize=12,
            label=f"a={a_values[i]}, CC={mean_clustering_all[i]:.4f}")

ax.set_xlabel("Disorder, $a$", fontsize=12)
ax.set_ylabel("Mean Clustering Coefficient", fontsize=12)
ax.set_xticks(a_values)
ax.set_ylim(bottom=0)
ax.legend()

plt.tick_params(axis='both', labelsize=12)
plt.title(f"Cycle {cycle}")
plt.tight_layout()
plt.savefig(f"plots/Clustering-Coefficient-vs-Disorder-Cycle{cycle}.png", bbox_inches='tight')
plt.savefig(f"plots/Clustering-Coefficient-vs-Disorder-Cycle{cycle}.pdf", bbox_inches='tight')