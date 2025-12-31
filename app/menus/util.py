import os
import sys
import time

# --- FUNGSI HELPER (YANG TADI ILANG) ---
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    print("")
    input("Tekan Enter untuk lanjut...")

def format_quota_byte(size_in_bytes):
    try:
        size = int(size_in_bytes)
        if size >= 1_000_000_000:
            return f"{size / 1_000_000_000:.2f} GB"
        elif size >= 1_000_000:
            return f"{size / 1_000_000:.2f} MB"
        elif size >= 1_000:
            return f"{size / 1_000:.2f} KB"
        else:
            return f"{size} B"
    except:
        return "0 B"

# ==========================================
#  BAGIAN BYPASS (JANTUNG OPERASINYA)
# ==========================================
def verify_api_key(api_key):
    # KITA PAKSA JADI 'TRUE' (VALID)
    return True

def get_hwid():
    return "HWID-BYPASS-BY-REZA-XYZ"

def validate_license(key):
    return True
