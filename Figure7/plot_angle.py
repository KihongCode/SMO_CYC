import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# Load the data
file_path = './Angles_82_Active/Angles_82_Active9.npy'
active_angles = np.load(file_path)
active_angles = np.array([val[0] for val in active_angles], dtype=np.float32)*(180 / np.pi)
file_path = './Angles_82_Inactive/Angles_82_Inactive9.npy'
inactive_angles = np.load(file_path)
inactive_angles = np.array([val[0] for val in inactive_angles], dtype=np.float32)*(180 / np.pi)

# Create kernel density estimators for both datasets
active_kde = gaussian_kde(active_angles)
inactive_kde = gaussian_kde(inactive_angles)

# Generate points for plotting the KDE curves
x_values = np.linspace(min(active_angles.min(), inactive_angles.min()),
                      max(active_angles.max(), inactive_angles.max()), num=1000)

# Calculate KDE values for the x_values
active_kde_values = active_kde(x_values)
inactive_kde_values = inactive_kde(x_values)

# Plot the kernel density estimates for both datasets
plt.figure(figsize=(6.4, 5.2))
plt.plot(x_values, active_kde_values, label='Active', color='green', linewidth=2)
plt.plot(x_values, inactive_kde_values, label='Inactive', color='magenta', linewidth=2)
plt.ylim(0,0.027)
plt.xlim(-180,181)
plt.yticks(np.arange(0, 0.0271, 0.009))
plt.xticks(range(-180, 181, 60))
plt.xlabel('Y472 $\chi^2$ angle',fontsize=18, fontweight='bold')
plt.ylabel('Probability Density',fontsize=20, fontweight='bold')
plt.legend(loc='upper left')
plt.savefig('/home/pdb3/kihongk2/Images/82_R_PB/Angle9_82.png', transparent=True, dpi=300)

plt.show()
