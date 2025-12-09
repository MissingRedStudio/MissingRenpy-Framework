# 🚀 MissingRed Ren'Py Template Documentation

Template ini adalah *framework* siap pakai untuk membuat Visual Novel (VN) di Ren'Py 8.x dengan sistem manajemen karakter, *auto-dimming*, narasi sinematik, dan *menu* dialog yang terpusat.

## ⚙️ Struktur Proyek

Semua logika dan aset dikelompokkan dalam subfolder di bawah `game/` untuk memudahkan pengelolaan:

| Folder/File | Isi | Fungsi Utama |
| :--- | :--- | :--- |
| `game/config/` | (`10_config.rpy`, `11_characters.rpy`, `13_audio.rpy`, dll.) | Pusat *wrapper* dan definisi kustom. **Hampir tidak perlu diubah** setelah *setup* awal. |
| `game/scenes/` | (`s01_prologue.rpy`, `s02_kafe_pagi.rpy`, dll.) | File-file *script* cerita modular (per bab/peristiwa). |
| `game/images/sprites/` | `bulan/`, `hari/`, dll. | Lokasi semua aset *sprite* karakter. |
| `game/audio/` | Musik (BGM), Efek Suara (SFX), dan *Voice* (VA). | Lokasi semua aset audio. |

-----

## 👤 Manajemen Karakter dan Aset (Setup Awal)

### 1\. Penamaan Aset Sprite

Sistem *template* ini menggunakan fungsi *Auto-Indexing* untuk menemukan aset. Pastikan format aset Anda konsisten:

| Elemen | Lokasi | Format Penamaan |
| :--- | :--- | :--- |
| **Folder** | `game/images/sprites/[tag_karakter]/` | `game/images/sprites/bulan/` (Lowercase) |
| **File** | Di dalam folder karakter | `[tag_karakter]_[ekspresi].png` |
| **Contoh** | `game/images/sprites/bulan/` | `bulan_happy.png`, `bulan_normal.png` |

### 2\. Pendaftaran Karakter

Buka **`game/config/11_characters.rpy`** dan tambahkan data karakter ke *list* `character_list`.

```python
define character_list = [
    {'tag': 'bulan', 'name': 'Bulan', 'color': '#FFC0CB'},
    {'tag': 'hari', 'name': 'Hari', 'color': '#7799BB'},
    # Tambahkan karakter baru di sini
]
```

  * **`tag`**: Nama pendek (lowercase) yang akan digunakan di perintah `call talk` (Contoh: `call talk("bulan", ...)`).
  * **`name`**: Nama lengkap yang akan muncul di *dialog box*.
  * **`color`**: Warna teks Ren'Py.

-----

## 💬 Wrapper Dialog dan Narasi

Template ini menggantikan *statement* Ren'Py standar dengan *labels* khusus.

### 1\. `call talk` (Dialog Karakter Utama)

Ini adalah *wrapper* utama untuk dialog karakter. Secara otomatis akan mengubah ekspresi, mengaktifkan status *dim* (redup) pada karakter lain, dan mendukung *Voice Acting*.

```renpy
call talk(tag_karakter, teks_dialog, ekspresi, voice_file=None)
```

| Parameter | Wajib? | Contoh Nilai | Deskripsi |
| :--- | :--- | :--- | :--- |
| `tag_karakter` | Ya | `"bulan"` | Tag karakter yang sedang bicara (dari `11_characters.rpy`). |
| `teks_dialog` | Ya | `"Halo, apa kabar?"` | Kalimat dialog. |
| `ekspresi` | Tidak | `"happy"`, `"sad"` | Ekspresi karakter saat bicara (Default: `"normal"`). |
| `voice_file` | Tidak | `"audio/bulan_salam.ogg"` | Path ke file Voice Acting (VA) untuk baris ini. |

### 2\. `call narator` (Narasi Sinematik)

Untuk menampilkan teks narasi berwarna hitam di tengah layar. Otomatis akan hilang setelah *click* atau *timeout* (5 detik).

```renpy
call narator(teks_narasi, duration=5.0)
```

| Parameter | Wajib? | Contoh Nilai | Deskripsi |
| :--- | :--- | :--- | :--- |
| `teks_narasi`| Ya | `"Waktu berlalu..."` | Teks narasi yang ingin ditampilkan. |
| `duration` | Tidak | `10.0` | Durasi sebelum narasi hilang otomatis (Default: 5.0 detik). |

-----

## 🎬 Manajemen Adegan dan Pergerakan

### 1\. Menampilkan/Menyembunyikan Karakter

| Aksi | Perintah | Catatan |
| :--- | :--- | :--- |
| **Muncul** | `show bulan normal at pos_left with default_chara_transition` | Selalu gunakan posisi `pos_...` yang sudah terdefinisi. |
| **Menghilang** | `hide bulan with default_chara_transition` | Gunakan `with None` untuk menghilang instan. |

### 2\. Pergerakan Karakter Tunggal

Gunakan `chara_move_transition` untuk efek geser yang halus.

```renpy
# Pindahkan Bulan dari kiri ke tengah
show bulan normal at pos_center with chara_move_transition 
```

### 3\. Pergerakan Karakter Bersamaan (Concurrent)

Gunakan *statement* `with` di baris terpisah untuk menjalankan beberapa perintah `show`/`move` secara serempak.

```renpy
# Pergerakan dan kemunculan terjadi pada saat yang sama
show bulan normal at pos_center 
show senja normal at pos_far_right 
show hari normal at pos_far_left 
with chara_move_transition # Eksekusi semua perintah di atas secara serempak
```

### 4\. `call setExpr` (Manual Dimming/Ekspresi)

Digunakan untuk mengatur ekspresi/status *dim* secara manual di luar *wrapper* `talk`.

```renpy
call setExpr(list_tag_karakter, ekspresi, isListen)
```

  * **`isListen=True`**: Karakter menjadi redup (*dim*).
  * **`isListen=False`**: Karakter menjadi terang (siap bicara).

-----

## 🎶 Manajemen Audio

| Fungsi | Contoh Panggilan | Deskripsi |
| :--- | :--- | :--- |
| **BGM** | `call play_music("audio/track1.mp3", volume=0.5)` | Mulai/ganti musik dengan *fade* dan volume yang ditentukan (0.0 - 1.0). |
| **Ambience** | `call play_ambience("audio/hujan.ogg")` | Memutar suara latar (kafe, alam, dll.). |
| **SFX** | `call play_sfx("audio/bell.wav", volume=0.8)` | Memutar efek suara sekali jalan. |
| **Stop** | `call stop_music(fade_time=2.0)` | Menghentikan BGM/Ambience dengan *fade out*. |

-----

## 🚪 Akhir Game

Untuk mengakhiri cerita, bersihkan semua elemen dan kembalikan pemain ke *Main Menu*.

```renpy
jump endGame # Akan fade out ke hitam, tampilkan "TAMAT", lalu kembali ke Main Menu.
```
