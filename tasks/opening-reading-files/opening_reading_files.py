from math import sqrt

# Errore strumentale
errore_spazio = 0.2  # m
errore_tempo = 0.1   # s

FILENAME = "esperimento_mru.txt"

# 1. Lettura del file
with open(FILENAME, "r") as file:
    righe = file.readlines()

print(righe)

# 2. Dizionario: intestazioni come chiavi, dati come liste
#    (le righe che iniziano con "#" sono commenti/risultati: le saltiamo)
righe = [r for r in righe if r.strip() and not r.startswith("#")]

intestazioni = righe[0].strip().split(",")
dati = {chiave: [] for chiave in intestazioni}

for riga in righe[1:]:
    valori = riga.strip().split(",")
    for i, chiave in enumerate(intestazioni):
        dati[chiave].append(float(valori[i]))

# 3. Mostra i dati
print("\nDati letti dal file:")
for chiave in dati:
    print(f"{chiave}: {dati[chiave]}")

# 4. Modifica un valore (secondo valore di spazio) e riscrivi il file
dati["spazio"][1] = 2.5

with open(FILENAME, "w") as file:
    file.write(",".join(intestazioni) + "\n")
    for i in range(len(dati["tempo"])):
        file.write(f"{dati['tempo'][i]},{dati['spazio'][i]}\n")

# 5. Velocità media v = Δs / Δt (tra istante iniziale e finale)
delta_s = dati["spazio"][-1] - dati["spazio"][0]
delta_t = dati["tempo"][-1] - dati["tempo"][0]
v = delta_s / delta_t

# 6. Errore su v (propagazione per un rapporto)
#    Δs e Δt sono differenze di due misure -> errore = sqrt(2) * errore strumentale
err_delta_s = sqrt(2) * errore_spazio
err_delta_t = sqrt(2) * errore_tempo
err_v = v * sqrt((err_delta_s / delta_s) ** 2 + (err_delta_t / delta_t) ** 2)

# 7. Stampa e aggiungi in coda al file
risultato = f"Velocità media: v = ({v:.2f} ± {err_v:.2f}) m/s"
print("\n" + risultato)

with open(FILENAME, "a") as file:
    file.write("# " + risultato + "\n")
