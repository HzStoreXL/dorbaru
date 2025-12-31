import os
import sys
import time
import requests # Biarin di-import biar ga error kalau ada yg manggil librarynya

# --- FUNGSI MEMBERSIHKAN LAYAR ---
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# --- FUNGSI PAUSE ---
def pause():
    print("")
    input("Tekan Enter untuk kembali...")

# ==========================================
#  BAGIAN BYPASS (JANTUNG OPERASINYA)
# ==========================================

def verify_api_key(api_key):
    """
    Fungsi ini aslinya ngecek ke server mashu.lol.
    TAPI SEKARANG KITA PAKSA JADI 'TRUE' (VALID).
    """
    # print(f"Mengecek key: {api_key}...") <-- Gak usah diprint biar cepet
    
    # Kita tipu scriptnya, seolah-olah server bilang OK.
    return True

# Kadang ada fungsi get_hwid juga di file ini yang bikin error
def get_hwid():
    return "HWID-BYPASS-BY-WAROENG-DIGITALL"

# Kalau ada fungsi validate lain, kita kasih True semua
def validate_license(key):
    return True
