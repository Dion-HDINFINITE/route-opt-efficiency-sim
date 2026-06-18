import csv
import argparse
import time

from heuristic import fungsi_heuristik
from exact import solve_exact 
from cost_function import hitung_tco_dan_bensin

def load_data(filepath):
    """Fungsi murni untuk membaca CSV tanpa library eksternal."""
    nodes = []
    distance_matrix = []
    
    try:
        with open(filepath, mode='r') as file:
            reader = csv.reader(file)
            header = next(reader)
            
            for row in reader:
                node_id = int(row[0])
                name = row[1]
                weight = float(row[2])
                
                distances = [float(x) for x in row[3:]]
                
                nodes.append({
                    'id': node_id,
                    'name': name,
                    'weight': weight
                })
                distance_matrix.append(distances)
                
        return nodes, distance_matrix
    except FileNotFoundError:
        print(f"Error: File {filepath} tidak ditemukan!")
        exit(1)

def main():
    # Setup CLI Argument Parser
    parser = argparse.ArgumentParser(description="Simulasi TCO Last-Mile Delivery")
    parser.add_argument('--scenario', type=str, choices=['subsidi', 'krisis'], required=True,
                        help="Pilih skenario ekonomi: 'subsidi' (BBM Murah) atau 'krisis' (BBM Mahal)")
    args = parser.parse_args()

    print(f"=== Menjalankan Simulasi TCO | Skenario: {args.scenario.upper()} ===\n")

    # 1. Load Data
    print("[*] Membaca data lokasi dan matriks jarak...")
    nodes, dist_matrix = load_data('data/dataset.csv')
    print(f"[+] Berhasil memuat {len(nodes)} titik lokasi.\n")

    # 2. Fungsi Algoritma Heuristik
    print("[*] Menjalankan Algoritma Heuristik (Greedy)...")
    # Memanggil fungsi kamu dengan mengalirkan output dari load_data
    hasil_heuristik = fungsi_heuristik(dist_matrix, nodes)
    
    # Menampilkan hasil rute nama dan waktu eksekusi ke Terminal CLI
    print(f"[+] Rute Heuristik : {' -> '.join(hasil_heuristik['route_names'])}")
    print(f"[+] Waktu Eksekusi : {hasil_heuristik['execution_time_ms']:.4f} ms")

    # 3. Panggil Fungsi Algoritma Eksak
    print("\n[*] Menjalankan Algoritma Eksak (DFS/Backtracking)...")
    exact_route_indices, exact_dist, exact_time = solve_exact(dist_matrix)
    exact_names = [nodes[idx]['name'] for idx in exact_route_indices]
    print(f"[+] Rute Eksak     : {' -> '.join(exact_names)}")
    print(f"[+] Waktu Eksekusi : {exact_time:.4f} ms")

    # 4. Panggil Fungsi Kalkulasi TCO
    print("\n[*] Menghitung Total Cost of Ownership (TCO)...")
    
    if args.scenario == 'subsidi':
        harga_bensin = 5000
    else:
        harga_bensin = 20000

    h_jarak, h_liter, h_bbm, h_srv, h_tco = hitung_tco_dan_bensin(
        hasil_heuristik['route_indices'], nodes, dist_matrix, harga_bensin, hasil_heuristik['execution_time_ms']
    )
    
    e_jarak, e_liter, e_bbm, e_srv, e_tco = hitung_tco_dan_bensin(
        exact_route_indices, nodes, dist_matrix, harga_bensin, exact_time
    )

    print("\n" + "="*50)
    print(f" HASIL KOMPARASI BIAYA ({args.scenario.upper()})")
    print("="*50)
    print(">> ALGORITMA HEURISTIK (Greedy)")
    print(f"Konsumsi BBM : {h_liter:.4f} Liter (Rp {h_bbm:,.2f})")
    print(f"Biaya Server : Rp {h_srv:,.2f}")
    print(f"TCO Final    : Rp {h_tco:,.2f}\n")
    
    print(">> ALGORITMA EKSAK (Backtracking)")
    print(f"Konsumsi BBM : {e_liter:.4f} Liter (Rp {e_bbm:,.2f})")
    print(f"Biaya Server : Rp {e_srv:,.2f}")
    print(f"TCO Final    : Rp {e_tco:,.2f}\n")

    print("=== KESIMPULAN BISNIS ===")
    if e_tco < h_tco:
        print(f"Algoritma EKSAK lebih menguntungkan (Hemat Rp {h_tco - e_tco:,.2f})")
    else:
        print(f"Algoritma HEURISTIK lebih menguntungkan (Hemat Rp {e_tco - h_tco:,.2f})")

    print("\n=== Simulasi Selesai ===")

if __name__ == "__main__":
    main()