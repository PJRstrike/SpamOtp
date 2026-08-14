#!/usr/bin/env python3
# main.py - ZANZY OTP SPAMMER v3.1

import sys
import time
import platform
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

# ============================================================
#  LOGO ZANZY (MERAH + KEREN)
# ============================================================
BANNER = f"""
{Fore.RED}╔══════════════════════════════════════════════════════════════╗
{Fore.RED}║{Fore.WHITE}   ███████╗ █████╗ ███╗   ██╗███████╗██╗   ██╗     {Fore.RED}║
{Fore.RED}║{Fore.WHITE}   ╚══███╔╝██╔══██╗████╗  ██║╚══███╔╝╚██╗ ██╔╝     {Fore.RED}║
{Fore.RED}║{Fore.WHITE}     ███╔╝ ███████║██╔██╗ ██║  ███╔╝  ╚████╔╝      {Fore.RED}║
{Fore.RED}║{Fore.WHITE}    ███╔╝  ██╔══██║██║╚██╗██║ ███╔╝    ╚██╔╝       {Fore.RED}║
{Fore.RED}║{Fore.WHITE}   ███████╗██║  ██║██║ ╚████║███████╗   ██║        {Fore.RED}║
{Fore.RED}║{Fore.WHITE}   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝        {Fore.RED}║
{Fore.RED}║                                                          {Fore.RED}║
{Fore.RED}║   {Fore.YELLOW}>> ZANZY OTP SPAMMER v3.1 <<{Fore.RED}               ║
{Fore.RED}║   {Fore.GREEN}>> 38 API ACTIVE <<{Fore.RED}                         ║
{Fore.RED}║   {Fore.CYAN}>> BY @violexzy <<{Fore.RED}                           ║
{Fore.RED}╚══════════════════════════════════════════════════════════════╝
{Fore.RESET}
"""

# ============================================================
#  FUNGSI DUMMY (UNTUK TESTING TANPA LICENSE)
# ============================================================
def clear_screen():
    import os
    os.system('clear' if os.name == 'posix' else 'cls')

def log_header():
    print(BANNER)

def log_info(msg):
    print(f"{Fore.CYAN}[INFO]{Fore.WHITE} {msg}{Style.RESET_ALL}")

def log_success(msg):
    print(f"{Fore.GREEN}[SUCCESS]{Fore.WHITE} {msg}{Style.RESET_ALL}")

def log_warning(msg):
    print(f"{Fore.YELLOW}[WARNING]{Fore.WHITE} {msg}{Style.RESET_ALL}")

def log_error(msg):
    print(f"{Fore.RED}[ERROR]{Fore.WHITE} {msg}{Style.RESET_ALL}")

def log_input(msg):
    return input(f"{Fore.MAGENTA}{msg}{Fore.WHITE}")

def check_license():
    return "premium", 999, "DEVICE_ID"

def use_quota(device_id):
    return True

def get_device_id():
    return "DEVICE_ID"

def check_user(device_id):
    return {"quota": 999}

def get_license_price():
    return 25000

def get_whatsapp_admin():
    return "+6285656384779"

def get_telegram_username():
    return "@violetxzy"

def get_active_apis():
    return 38

def is_maintenance():
    return False

def get_maintenance_message():
    return ""

def get_trial_quota():
    return 5

def get_total_users():
    return 100

def get_user_stats():
    return 80, 20

def get_formatted_datetime():
    now = datetime.now()
    days = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    months = ["Januari", "Februari", "Maret", "April", "Mei", "Juni",
              "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    return f"{days[now.weekday()]}, {now.day} {months[now.month-1]} {now.year}"

def get_device_name():
    try:
        return platform.node()
    except:
        return "Unknown Device"

def show_user_stats():
    premium, trial = get_user_stats()
    total = premium + trial
    print(f"{Fore.CYAN}Total Pengguna  : {Fore.WHITE}{total}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}├─ Premium      : {Fore.GREEN}{premium}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}└─ Trial        : {Fore.YELLOW}{trial}{Style.RESET_ALL}")

def show_buy_guide():
    clear_screen()
    log_header()
    license_price = get_license_price()
    whatsapp_admin = get_whatsapp_admin()
    telegram_username = get_telegram_username()
    total_apis = get_active_apis()

    print(f"{Fore.CYAN}PANDUAN PEMBELIAN LISENSI PREMIUM{Style.RESET_ALL}")
    print()
    print(f"{Fore.WHITE}Keuntungan Premium:{Style.RESET_ALL}")
    print(f"  {Fore.GREEN}•{Style.RESET_ALL} Akses FULL semua API ({total_apis} API)")
    print(f"  {Fore.GREEN}•{Style.RESET_ALL} Unlimited penggunaan (tanpa batas kuota)")
    print(f"  {Fore.GREEN}•{Style.RESET_ALL} Mendapat update tools terbaru")
    print(f"  {Fore.GREEN}•{Style.RESET_ALL} Dukungan prioritas dari admin")
    print()
    print(f"{Fore.CYAN}Harga: {Fore.GREEN}Rp. {license_price:,}{Style.RESET_ALL} (sekali bayar, akses selamanya)")
    print()
    print(f"{Fore.YELLOW}Cara Pembelian:{Style.RESET_ALL}")
    print(f"  1. Chat admin via WhatsApp atau Telegram")
    print(f"  2. Kirim Device ID Anda")
    print(f"  3. Lakukan pembayaran via QRIS")
    print(f"  4. Tunggu aktivasi")
    print()
    print(f"{Fore.CYAN}Kontak Admin:{Style.RESET_ALL}")
    print(f"  WhatsApp : {Fore.GREEN}{whatsapp_admin}{Style.RESET_ALL}")
    print(f"  Telegram : {Fore.WHITE}{telegram_username}{Style.RESET_ALL}")
    print()
    print(f"{Fore.CYAN}Device ID Anda:{Style.RESET_ALL}")
    print(f"  {Fore.WHITE}{get_device_id()}{Style.RESET_ALL}")
    print()
    input("Tekan Enter untuk kembali ke menu utama...")

def show_thread_menu():
    clear_screen()
    log_header()
    print(f"{Fore.CYAN}Pilih Jumlah Thread (default 1){Style.RESET_ALL}")
    print()
    print(f"  {Fore.GREEN}[1]{Style.RESET_ALL} 1 Thread (slow)")
    print(f"  {Fore.GREEN}[2]{Style.RESET_ALL} 2 Thread")
    print(f"  {Fore.GREEN}[3]{Style.RESET_ALL} 3 Thread")
    print(f"  {Fore.GREEN}[4]{Style.RESET_ALL} 4 Thread")
    print(f"  {Fore.GREEN}[5]{Style.RESET_ALL} 5 Thread (recommended)")
    print(f"  {Fore.GREEN}[6]{Style.RESET_ALL} 6 Thread")
    print(f"  {Fore.GREEN}[7]{Style.RESET_ALL} 7 Thread")
    print(f"  {Fore.GREEN}[8]{Style.RESET_ALL} 8 Thread")
    print(f"  {Fore.GREEN}[9]{Style.RESET_ALL} 9 Thread")
    print(f"  {Fore.GREEN}[10]{Style.RESET_ALL} 10 Thread (fast)")
    print()
    return log_input("Pilih thread (1-10, enter untuk default 1): ").strip()

def show_menu_premium():
    print(f"{Fore.CYAN}Menu Premium{Style.RESET_ALL}")
    print(f"  {Fore.GREEN}[1]{Style.RESET_ALL} Single Round")
    print(f"  {Fore.GREEN}[2]{Style.RESET_ALL} Infinite Loop")
    print(f"  {Fore.GREEN}[3]{Style.RESET_ALL} Keluar")
    print()

# ============================================================
#  MAIN
# ============================================================
def main():
    status, quota, device_id = check_license()

    if status == "premium":
        while True:
            clear_screen()
            log_header()
            print(f"{Fore.CYAN}{get_formatted_datetime()} | {Fore.WHITE}{get_device_name()}{Style.RESET_ALL}")
            print()
            show_user_stats()
            print()
            print(f"{Fore.GREEN}Premium Active - Full Access{Style.RESET_ALL}")
            print()
            show_menu_premium()

            choice = log_input("Pilih menu (1/2/3): ").strip()

            if choice == "1":
                thread_choice = show_thread_menu()
                try:
                    threads = int(thread_choice) if thread_choice.strip() else 1
                    if threads < 1: threads = 1
                    elif threads > 10: threads = 10
                except:
                    threads = 1
                from main_engine import run_single_round
                run_single_round(threads=threads)
                log_info("Tekan Enter untuk kembali ke menu...")
                input()

            elif choice == "2":
                from main_engine import run_infinite_loop
                run_infinite_loop()
                log_info("Tekan Enter untuk kembali ke menu...")
                input()

            elif choice == "3":
                log_info("Keluar...")
                sys.exit(0)

            else:
                log_warning("Pilihan tidak valid. Tekan Enter untuk kembali...")
                input()

if __name__ == "__main__":
    main()
