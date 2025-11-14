import matplotlib.pyplot as plt
import numpy as np

# Rangs de mida d'entrada (n)
n_values = np.logspace(1, 6, num=100, base=10)  

# Complexitats temporals (creixements asimptòtics)
def classic(n):
    return n**2

def karatsuba(n):
    return n**(np.log2(3)) 

def toom_cook_3(n):
    return n**(np.log2(5)/np.log2(3))  

def fft(n):
    return n * np.log2(n)

# Calcular valors
classic_vals = classic(n_values)
karatsuba_vals = karatsuba(n_values)
toom_vals = toom_cook_3(n_values)
fft_vals = fft(n_values)

# Gràfic logarítmic
plt.figure(figsize=(12, 7))
plt.loglog(n_values, classic_vals, label='Clàssic (O(n²))', linewidth=2)
plt.loglog(n_values, karatsuba_vals, label='Karatsuba (O(n^1.585))', linewidth=2)
plt.loglog(n_values, toom_vals, label='Toom-Cook 3 (O(n^1.465))', linewidth=2)
plt.loglog(n_values, fft_vals, label='FFT (O(n log n))', linewidth=2)

plt.title('Comparació de la Complexitat Temporal en Algorismes de Multiplicació', fontsize=16, fontweight='bold')
plt.xlabel('Mida de l\'entrada (n)', fontsize=12)
plt.ylabel('Operacions (proporcionals al temps)', fontsize=12)
plt.legend(loc='upper left', fontsize=10)
plt.grid(True, which="both", ls="--", lw=0.5, alpha=0.7)

# Marca d'aigua 
plt.annotate('© Bilal Chakroun', xy=(0.98, 0.02), xycoords='axes fraction', fontsize=16,
             color='gray', alpha=0.6, ha='right', va='bottom', rotation=0, style='italic')

# Afegir text amb la diferència relativa final entre algorismes
n_final = n_values[-1]
diff_classic_fft = classic(n_final) / fft(n_final)
diff_karatsuba_fft = karatsuba(n_final) / fft(n_final)
diff_toom_fft = toom_cook_3(n_final) / fft(n_final)

info_text = (
    f"Per n = {int(n_final):,}:\n"
    f"Clàssic vs FFT: {diff_classic_fft:,.0f}x més lent\n"
    f"Karatsuba vs FFT: {diff_karatsuba_fft:,.0f}x més lent\n"
    f"Toom-Cook 3 vs FFT: {diff_toom_fft:,.0f}x més lent"
)

plt.annotate(info_text, xy=(0.17, 0.9), xycoords='axes fraction', fontsize=10,
             bbox=dict(boxstyle="round", fc="white", ec="gray", alpha=0.7))

plt.tight_layout()
plt.show()
