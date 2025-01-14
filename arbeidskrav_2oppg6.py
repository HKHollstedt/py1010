import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200)

f = (-x**2) -5

plt.xlabel("X-linja")
plt.ylabel("Y-linja")
plt.title("Oppgave 6 innlevering")

plt.grid()
plt.plot (f)
