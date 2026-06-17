import time

def fungsi_heuristik(distance_matrix, nodes):
    """
    Fungsi Algoritma A (Heuristik) - Menggunakan Pendekatan Greedy (Nearest Neighbor).
    """
    num_locations = len(nodes)
    
    # 1. Inisialisasi pelacak kunjungan. Hub Jatinangor (indeks 0) ditandai True sejak awal.
    visited = [False] * num_locations
    visited[0] = True 
    
    current_node = 0
    route_indices = [0] # Memulai rute perjalanan dari Hub (indeks 0)
    
    # Mulai pencatatan waktu presisi tinggi (skala milidetik)
    start_time = time.perf_counter()
    
    # 2. Loop Utama Heuristik: Kunjungi seluruh pelanggan (N-1 lokasi sisa)
    for _ in range(num_locations - 1):
        nearest_node = -1
        min_distance = float('inf')
        
        # Loop Dalam (Strategi Greedy): Cari lokasi terdekat berikutnya yang valid
        for next_node in range(num_locations):
            # Syarat: Belum dikunjungi DAN jarak > 0 (menghindari diagonal ke diri sendiri)
            if not visited[next_node] and distance_matrix[current_node][next_node] > 0:
                dist = distance_matrix[current_node][next_node]
                if dist < min_distance:
                    min_distance = dist
                    nearest_node = next_node
        
        # Melangkah ke pelanggan terdekat yang ditemukan (Local Optimum)
        if nearest_node != -1:
            visited[nearest_node] = True
            route_indices.append(nearest_node)
            current_node = nearest_node
            
    # 3. KETENTUAN TSP: Wajib kembali ke Hub Jatinangor (indeks 0) untuk menutup siklus rute
    route_indices.append(0)
    
    # Selesai pencatatan waktu eksekusi
    end_time = time.perf_counter()
    execution_time_ms = (end_time - start_time) * 1000
    
    # Konversi susunan indeks rute menjadi nama lokasi asli menggunakan data 'name' 
    route_names = [nodes[idx]['name'] for idx in route_indices]
    
    return {
        "route_indices": route_indices,        # Digunakan untuk hitung bensin dinamis
        "route_names": route_names,            # Digunakan untuk cetak rute di CLI
        "execution_time_ms": execution_time_ms # Metrik performa untuk hitung biaya komputasi server
    }