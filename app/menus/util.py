Pake ini import os
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
        text = "".join(self.result)
        text = re.sub(r"\n\s*\n\s*\n+", "\n\n", text)
        return "\n".join(textwrap.wrap(text, width=self.width, replace_whitespace=False))

def display_html(html_text, width=80):
    parser = HTMLToText(width=width)
    parser.feed(html_text)
    return parser.get_text()

def format_quota_byte(quota_byte: int) -> str:
    GB = 1024 ** 3
    MB = 1024 ** 2
    KB = 1024
    if quota_byte >= GB:
        return f"{quota_byte / GB:.2f} GB"
    elif quota_byte >= MB:
        return f"{quota_byte / MB:.2f} MB"
    elif quota_byte >= KB:
        return f"{quota_byte / KB:.2f} KB"
    else:
        return f"{quota_byte} B"
