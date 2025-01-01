class Process:
    def __init__(self, data):
        self.data = data

    def login_user(self):
        try:
            username = input("Masukkan username: ")
            password = input("Masukkan password (kospavi): ")

            if password != "kospavi":
                raise ValueError("Password salah!")

            self.data.add_user(username)
            print(f"Selamat datang {username}! Anda telah terhubung ke wifi kosan.")
        except ValueError as e:
            print(f"Error: {e}")

    def admin_login(self):
        try:
            admin_username = input("Masukkan username admin: ")
            admin_password = input("Masukkan password admin: ")

            if admin_username != self.data.admin_username or admin_password != self.data.admin_password:
                raise ValueError("Username atau password admin salah!")

            self.show_users()

        except ValueError as e:
            print(f"Error: {e}")

    def show_users(self):
        users = self.data.get_users()
        if not users:
            print("Belum ada pengguna yang terhubung.")
        else:
            print("\nDaftar Pengguna yang Terhubung ke Wifi Kosan:")
            print("="*70)
            print(f"{'No':<5}{'Username':<30}{'IP Address':<15}")
            print("="*70)
            for idx, (user, ip) in enumerate(users, 1):
                print(f"{idx:<5}{user:<30}{ip:<15}")
            print("="*70)
