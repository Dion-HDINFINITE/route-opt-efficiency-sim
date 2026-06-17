# route-opt-efficiency-sim
A CLI-based simulation pipeline benchmarking Exact vs Heuristic algorithms for Last-Mile Delivery under dynamic fuel constraints to analyze Total Cost of Ownership (TCO).

## Analisis Kompleksitas Algoritma A: Heuristik (Nearest Neighbor / Greedy)

### 1. Kompleksitas Waktu (Time Complexity): O(N^2)

Algoritma Heuristik berbasis pendekatan Greedy (Nearest Neighbor) yang ditulis dari nol  ini memiliki kompleksitas waktu sebesar **O(N^2)** dalam skenario terburuk (*worst-case*) maupun rata-rata (*average-case*), di mana **N** menyatakan jumlah total titik lokasi (Hub + Pelanggan).

**Breakdown Analisis:**
* **Loop Utama (Luar):** Berjalan sebanyak **N-1** kali karena kurir harus mengunjungi seluruh lokasi pelanggan yang tersisa setelah berangkat dari Hub.
* **Loop Pencarian (Dalam):** Di setiap langkah iterasi luar, algoritma melakukan *scanning* linear ke seluruh simpul (N lokasi) untuk mengecek kondisi `if not visited[next_node]` dan mencari nilai jarak terkecil pada `distance_matrix`.
* **Kombinasi Operasi:** Jumlah operasi perbandingan jarak secara matematis membentuk deret aritmatika:
  $$\text{Total Operasi} \approx (N-1) \times N = N^2 - N \implies O(N^2)$$

| Skenario        | Kompleksitas Waktu | Keterangan                                        | Skenario | Kompleksitas Waktu | Keterangan |
| :--- | :--- | :--- |
| **Best Case** | $O(N^2)$ | Tetap harus memindai seluruh matriks untuk memastikan jarak terdekat. |
| **Average Case**| $O(N^2)$ | Rata-rata pencarian tetangga terdekat di setiap titik. |
| **Worst Case** | $O(N^2)$ | Seluruh kombinasi node tidak terkunci dan harus divalidasi satu per satu. |

### 2. Kompleksitas Ruang (Space Complexity): $O(N)$

Kompleksitas ruang dari implementasi algoritma ini adalah **O(N)** (Linear), yang berarti penggunaan memori komputer akan tumbuh secara proporsional sebanding dengan bertambahnya jumlah lokasi objek pengantaran.

**Alokasi Memori Efektif:**
* **`visited` Array:** Membutuhkan ruang sebesar N elemen boolean (`[False] * num_locations`) untuk melacak status kunjungan lokasi agar tidak terjadi pengulangan (siklus tak berujung).
* **`route_indices` & `route_names` List:** Menyimpan struktur hasil rute perjalanan yang memiliki panjang tepat N + 1elemen (karena kurir harus kembali lagi ke Hub asal).
* **Matriks Jarak:** Penggunaan memori matriks 2D (O(N^2)) tidak dihitung sebagai beban memori algoritma heuristik karena data tersebut bersifat *read-only* dan tidak dialokasikan ulang di dalam fungsi heuristik.

---