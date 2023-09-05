import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(12, 6))

x = np.arange(0, 10, 0.1)
y = np.sin(x)
z = np.cos(x)

ax.plot(y, color='blue', label='Sine wave')
ax.plot(z, color='black', label='Cosine wave')
ax.set_title('Sine and cosine waves')
ax.set_xlabel('Time')
ax.set_ylabel('Intensity')
leg = ax.legend()

plt.show()