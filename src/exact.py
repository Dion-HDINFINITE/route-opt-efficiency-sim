import time

def solve_exact(matrix):
    """
    Fungsi utama untuk menjalankan algoritma eksak (Backtracking + Pruning).
    matrix: Matriks ketetanggaan (Adjacency Matrix) berisi jarak antar lokasi.
    """
    num_locations = len(matrix)
    
    best_route = []
    min_distance = float('inf') 

    def backtrack(current_node, visited, current_route, current_distance):
        nonlocal min_distance, best_route
        
        # --- 1. PRUNING ---
        if current_distance >= min_distance:
            return

        # --- 2. BASE CASE ---
        if len(visited) == num_locations:
            distance_to_hub = matrix[current_node][0]
            total_distance = current_distance + distance_to_hub
            
            if total_distance < min_distance:
                min_distance = total_distance
                best_route = current_route + [0]
            return

        # --- 3. REKURSI & EXPLORASI ---
        for next_node in range(num_locations):
            if next_node not in visited:
                visited.add(next_node)
                current_route.append(next_node)
                
                backtrack(
                    current_node=next_node,
                    visited=visited,
                    current_route=current_route,
                    current_distance=current_distance + matrix[current_node][next_node]
                )
                
                # --- BACKTRACK ---
                current_route.pop()
                visited.remove(next_node)

    # --- Mulai Pencatatan Waktu ---
    start_time = time.time()
    
    initial_visited = {0}
    initial_route = [0]
    
    backtrack(
        current_node=0, 
        visited=initial_visited, 
        current_route=initial_route, 
        current_distance=0
    )
    
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000  # ms

    return best_route, min_distance, execution_time

# --- BLOK TES MANDIRI ---
if __name__ == "__main__":
    # Dummy matrix 4x4 (1 Hub + 3 Pelanggan) untuk ngetes kode berjalan atau tidak
    matrix_simulasi = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    
    rute, jarak, waktu = solve_exact(matrix_simulasi)
    
    print("=== HASIL TES MANDIRI ALGORITMA EKSAK ===")
    print(f"Rute Terbaik : {rute}")
    print(f"Total Jarak  : {jarak} km")
    print(f"Waktu Proses : {waktu:.4f} ms")