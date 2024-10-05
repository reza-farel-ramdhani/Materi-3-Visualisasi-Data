#Reza Farel Ramdhani
#NIM.1227030028
#Tugas 3 - Gerak Jatuh Bebas

import matplotlib.pyplot as plt
import numpy as np

# Constants
g = 9.8  # Percepatan gravitasi dalam m/s^2
h0 = 150  # Ketinggian awal dari titik jatuh

# Menghitung waktu jatuh objek dari h0 hingga ke permukaan t = sqrt(2 * h0 / g)
t_jatuh = np.sqrt(2 * h0 / g)

# Membuat rentang waktu untuk grafik dari waktu 0 - waktu akhir tepat menyentuh permukaan
t = np.linspace(0, t_jatuh, 500)

# Mengkalkukasi kecepatan gerak jatuh bebas v = g * t
v = g * t

#Mengukur ketinggian sebagai fungsi waktu h(t) = h0 - 0.5 * g * t^2
h = h0 - 0.5 * g * t**2

# Mengukur kecepatan akhir saat menyentuh permukaan
v_akhir = v[-1]

# Mengukur ketinggian akhir (permukaan, mendekati atau sama dengan 0)
h_akhir = h[-1]

# mengukur waktu, kecepatan, dan ketinggian akhir
t_jatuh, v_akhir, h_akhir

# Plotting kecepatan dan perubahan ketinggian sebagai fungsi waktu

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

print(f"Waktu jatuh benda: {t_jatuh} detik")
print(f"Kecepatan akhir benda: {v_akhir} m/s")
print(f"Ketinggian akhir benda: {h_akhir} meter")

# Grafik kecepatan benda terhadap waktu
ax1.plot(t, v, color='blue')
ax1.set_title('Grafik Kecepatan Benda terhadap Waktu')
ax1.set_xlabel('Waktu (s)')
ax1.set_ylabel('Kecepatan (m/s)')
ax1.grid(True)

# Grafik ketinggian benda terhadap waktu
ax2.plot(t, h, color='yellow')
ax2.set_title('Grafik Ketinggian Benda terhadap Waktu')
ax2.set_xlabel('Waktu (s)')
ax2.set_ylabel('Ketinggian (m)')
ax2.grid(True)

# Penampil plotting
plt.tight_layout()
plt.show()
