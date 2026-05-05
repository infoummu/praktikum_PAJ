import os
import platform

def ping_sweep():
    print("======================================")
    print("      Memulai Network Scanner (Python)  ")
    print("======================================")

    # Daftar IP target (Bisa diubah sesuai topologi jaringan Anda)
    ip_list = [
        "192.168.1.1",
        "192.168.1.2",
        "8.8.8.8", # IP Google DNS sebagai contoh eksternal
        "10.0.0.5"
    ]

    # Menentukan parameter ping berdasarkan Sistem Operasi
    # Windows menggunakan '-n' untuk jumlah ping, Linux/Mac menggunakan '-c'
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    for ip in ip_list:
        # Menyusun perintah command line
        # > /dev/null 2>&1 (Linux) atau > nul 2>&1 (Windows) menyembunyikan output asli
        null_path = "nul" if platform.system().lower() == 'windows' else "/dev/null"
        command = f"ping {param} 1 {ip} > {null_path} 2>&1"
        
        # Menjalankan perintah dan menangkap hasilnya
        response = os.system(command)
        
        # Jika response == 0, berarti ping berhasil (Reply)
        if response == 0:
            print(f"[+] Host {ip:<15} : UP (Tersambung)")
        else:
            print(f"[-] Host {ip:<15} : DOWN (Terputus)")

    print("======================================")
    print("          Selesai Pengecekan          ")
    print("======================================")

if __name__ == "__main__":
    ping_sweep()
