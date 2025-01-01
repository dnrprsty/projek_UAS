class View:
    def __init__(self, process):
        self.process = process

    def display_menu(self):
        while True:
            print("\n----- Menu Wifi Kosan -----")
            print("1. Login sebagai Pengguna")
            print("2. Login sebagai Admin")
            print("3. Keluar")

            choice = input("Pilih menu (1/2/3): ")

            if choice == "1":
                self.process.login_user()
            elif choice == "2":
                self.process.admin_login()
            elif choice == "3":
                print("Terima kasih telah menggunakan program ini.")
                break
            else:
                print("Pilihan tidak valid!")
