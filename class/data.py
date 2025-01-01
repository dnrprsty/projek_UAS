class Data:
    def __init__(self):
        self.users = []  # Menyimpan daftar pengguna yang sudah terhubung
        self.admin_username = "adminkost"
        self.admin_password = "admin123"

    def add_user(self, username):
        ip_address = self.generate_ip()
        self.users.append((username, ip_address))

    def get_users(self):
        return self.users

    def generate_ip(self):
        return f"192.168.0.{random.randint(2, 254)}"
