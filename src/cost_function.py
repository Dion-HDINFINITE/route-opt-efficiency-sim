def hitung_tco_dan_bensin(rute_indices, nodes, matrix, harga_bensin, exec_time_ms):

    # Menghitung biaya operasional (BBM + Server).
    # Rasio konsumsi bensin berkurang seiring paket yang di-drop

    berat_total = sum([n['weight'] for n in nodes])
    
    total_jarak = 0
    total_bensin_liter = 0
    berat_saat_ini = berat_total
    
    # Looping menghitung biaya per ruas jalan 
    for i in range(len(rute_indices) - 1):
        asal = rute_indices[i]
        tujuan = rute_indices[i+1]
        
        jarak = matrix[asal][tujuan]
        total_jarak += jarak
        
        # Asumsi rasio: Motor kosong 0.02 L/km, tiap 1kg nambah boros 0.001 L/km 
        rasio_bbm = 0.02 + (berat_saat_ini * 0.001)
        total_bensin_liter += jarak * rasio_bbm
        
        # Kurangi beban paket setelah sampai di tujuan
        berat_saat_ini -= nodes[tujuan]['weight']
        if berat_saat_ini < 0:
            berat_saat_ini = 0
            
    # TCO Formula = Biaya BBM + Biaya Komputasi Server 
    biaya_bbm = total_bensin_liter * harga_bensin
    biaya_server = exec_time_ms * 50.0 # Rp50 per ms eksekusi 
    tco = biaya_bbm + biaya_server
    
    return total_jarak, total_bensin_liter, biaya_bbm, biaya_server, tco