import csv
import argparse
import time

from heuristic import fungsi_heuristik

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

    # 4. Panggil Fungsi Kalkulasi TCO
    print("\n[*] Menghitung Total Cost of Ownership (TCO)...")
    
    print("\n=== Simulasi Selesai ===")

if __name__ == "__main__":
    main()