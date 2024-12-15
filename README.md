## Google Search News Scraper

Script ini digunakan untuk menjalankan pencarian di Google (tab berita) dan mengambil data berita, lalu menyimpannya ke dalam file `.md`.

---

### **Cara Menjalankan**

1. **Aktifkan Virtual Environment**
   
   Jika belum memiliki virtual environment, Anda bisa membuatnya dengan perintah berikut:
   ```bash
   python -m venv venv
   ```
   Aktifkan virtual environment:
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **Linux/Mac**:
     ```bash
     source venv/bin/activate
     ```

2. **Install Dependencies**
   
   Pastikan semua dependensi yang diperlukan telah terinstal. Jalankan perintah berikut:
   ```bash
   pip install -r requirements.txt
   ```

3. **Jalankan Script**
   
   Untuk menjalankan script dengan mode debug Playwright, gunakan perintah:
   ```bash
   PWDEBUG=1 pytest -s test_example.py
   ```
   
   Perintah ini akan membuka browser interaktif untuk melihat proses scraping yang berjalan.

---

### **Hasil Output**

- Script akan menyimpan data berita yang diambil ke dalam file Markdown (`.md`).
- Nama file output akan mengikuti format `news<index>.md`, di mana `<index>` adalah angka yang menunjukkan urutan berita yang diambil.

---

### **Catatan Penting**
- Pastikan Anda memiliki koneksi internet yang stabil.
- Jika Google memberikan CAPTCHA, Anda mungkin perlu menyelesaikannya secara manual.
- Jika ada kendala, gunakan mode debug Playwright untuk memantau proses scraping.
