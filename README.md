# Program WiFi Kosan

Program ini bertujuan untuk mencatat siapa saja yang terhubung ke WiFi kosan. Pengguna dapat login untuk terhubung ke WiFi, sementara admin dapat melihat daftar pengguna yang terhubung, lengkap dengan IP address mereka.

## Deskripsi Program

Program ini terbagi menjadi tiga komponen utama:
1. **Class Data**: Menyimpan informasi pengguna dan IP address acak yang diberikan saat login.
2. **Class Process**: Mengatur proses login pengguna dan admin, serta menampilkan daftar pengguna.
3. **Class View**: Menampilkan menu interaktif bagi pengguna untuk memilih login sebagai pengguna atau admin.

### Alur Program
1. **Pengguna** memasukkan **username** dan **password** (password default: `kospavi`).
2. Jika login berhasil, pengguna akan ditambahkan ke daftar pengguna dan diberikan IP address acak.
3. **Admin** login dengan **username** dan **password** admin (username: `adminkost`, password: `admin123`), kemudian dapat melihat daftar pengguna yang terhubung beserta IP address mereka.

## Flowchart Program

Berikut adalah flowchart yang menggambarkan alur program:

```mermaid
flowchart TD
    A[Start] --> B[Display Main Menu]
    B --> C{Choose Option}
    C -->|Login as User| D[Login as User]
    C -->|Login as Admin| E[Login as Admin]
    C -->|Exit| F[Exit Program]
    D --> G[Input Username and Password]
    G --> H{Password Correct?}
    H -->|Yes| I[Add User and Generate IP]
    I --> B
    H -->|No| J[Display Error]
    J --> B
    E --> K[Input Admin Username and Password]
    K --> L{Admin Credentials Correct?}
    L -->|Yes| M[Display Users with IP]
    L -->|No| N[Display Error]
    N --> B
    M --> B
    F --> Z[End]
