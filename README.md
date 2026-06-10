# 📊 Laporan Audit Statistik: pandas-dev/pandas

**Mata Kuliah:** Statistika dan Probabilitas (Minggu 11–14) | **Program Studi:** Sistem dan Teknologi Informasi (STI) 2025  
**Repositori Target:** [pandas-dev/pandas](https://github.com/pandas-dev/pandas)

---

## 🚀 Tinjauan Proyek & Sumber Data
Audit ini bertujuan untuk mengukur metrik kesehatan dan perilaku repositori *open-source* `pandas-dev/pandas` secara statistik. Repositori ini dipilih karena memenuhi syarat mutlak: memiliki lebih dari 1.000 *issue* tertutup, 500+ *Pull Request* (PR) yang berhasil di-*merge*, serta memiliki rekam jejak waktu (*timestamp*) yang jelas.

* **Sumber API:** GitHub REST API v3
* **Limitasi Data:** Data ditarik sebanyak 2.000 sampel menggunakan metode *pagination* berdasarkan batasan *rate limit* API reguler. Meskipun dataset mentah mencakup status *open* dan *closed*, keseluruhan analisis statistik (seperti estimasi probabilitas dan waktu penyelesaian) difokuskan secara eksklusif pada *issue* dan PR yang telah mencapai status akhir (*closed* atau *merged*).

---

## 👥 Tim Peneliti & Peran

| Anggota Tim | Peran | Fokus Tanggung Jawab |
|---|---|---|
| **Soko Selowansyah** (1519625063) | Data Engineer | Ekstraksi API, pembersihan data (*cleaning*), EDA, visualisasi awal |
| 
| 
| 
| 
---

## 🎯 Fokus Pertanyaan Riset (RQ)
Setiap lapisan analisis (Minggu 11-14) dirancang untuk berkesinambungan dan menjawab tiga pertanyaan krusial berikut:

1. **Fase Estimasi & Inferensi (Modul 02 & 03):** Berapa estimasi probabilitas sebuah PR diterima (*merged*) di repositori Pandas, beserta rata-rata harian frekuensi *issue* baru, dan seberapa besar rentang ketidakpastian dari estimasi tersebut?
2. **Fase Pengujian Hipotesis (Modul 04):** Apakah terdapat perbedaan waktu penyelesaian (*time-to-close*) yang signifikan secara statistik antara *issue* yang ditangani oleh *Core Member* dengan *Contributor* eksternal?
3. **Fase Simulasi Komputasi (Modul 05):** Berapa probabilitas terjadinya penumpukan beban kerja (*bottleneck*) dalam penyelesaian *issue* di masa mendatang jika diestimasi tanpa menggunakan rumus analitik?

---

## 📁 Struktur Repository

```text
stat-audit-pandas-sti-2025/
├── README.md                         ← Deskripsi proyek & temuan
├── AI_USAGE_LOG.md                   ← Log transparansi AI
├── data/
│   ├── raw/                          ← Data mentah (JSON)
│   └── clean/dataset.csv             ← Data bersih siap analisis
├── src/
│   ├── estimator.py                  ← Fungsi MLE & Posterior
│   ├── inference.py                  ← Fungsi Confidence/Credible Interval
│   ├── hypothesis.py                 ← Fungsi Uji Z-Test
│   └── simulation.py                 ← Fungsi Stokastik & MCMC
├── notebooks/
│   ├── 01_eda.ipynb                  ← Analisis Data Eksploratif
│   ├── 02_estimation.ipynb           ← Estimasi Parameter 
│   ├── 03_confidence_interval.ipynb  ← Inferensi Statistik
│   ├── 04_hypothesis_testing.ipynb   ← Uji Hipotesis
│   └── 05_simulation.ipynb           ← Simulasi Komputasi
├── report/
│   
├── presentation/
│   
└── requirements.txt
``` 

## ⚙️ Petunjuk Eksekusi (*How-to-Run*)

Pastikan lingkungan Python 3 Anda sudah siap. Kode dan *notebook* disusun dengan rapi agar dapat dieksekusi secara berurutan dari hulu ke hilir.

```bash
# 1. Clone repositori ke mesin lokal
git clone https://github.com/tobslayerr/stat-audit-pandas-sti-2025.git
cd stat-audit-pandas-sti-2025

# 2. Instalasi dependensi wajib
pip install -r requirements.txt

# 3. Jalankan server Jupyter Notebook
jupyter notebook
```
## 📈 Temuan Utama

Berdasarkan hasil analisis komprehensif dari fase ekstraksi data (EDA), estimasi parameter titik (MLE), hingga uji inferensial hipotesis,hingga simulasi komputasional **Pertanyaan Riset 1 (P1), Pertanyaan Riset 2 (P2), dan Pertanyaan Riset 3 (P3)** dengan temuan sebagai berikut:

1. **Estimasi & Inferensi Probabilitas (Menjawab P1):**
   Estimasi probabilitas sebuah PR berhasil diterima (*merged*) di repositori Pandas adalah sebesar **64.39%** (0.6439). Berdasarkan pengukuran rentang ketidakpastian menggunakan pendekatan *Confidence Interval* (Frequentist) dan *Credible Interval* (Bayesian) pada tingkat kepercayaan 95%, tim menyimpulkan bahwa probabilitas penerimaan populasi yang sesungguhnya berada pada rentang presisi **0.6214 hingga 0.6665**. Selain itu, rata-rata kemunculan *issue* baru diprediksi sebesar **14.71 issue per hari** dengan margin ketidakpastian (*Confidence Interval* 95%) berada pada rentang sempit antara **14.06 hingga 15.35 issue per hari**.

2. **Uji Hipotesis Performa Penyelesaian (Menjawab P2):**
   Berdasarkan pengujian hipotesis (Z-Test Dua Sampel Independen) pada tingkat signifikansi 5% ($\alpha = 0.05$), tim **menolak H0**. Terdapat bukti statistik yang kuat bahwa **ada perbedaan signifikan pada rata-rata waktu penyelesaian (time-to-close) antara Core Member dan Contributor eksternal**. *Core Member* terbukti jauh lebih cepat dalam menyelesaikan tugas dengan rata-rata waktu **120.65 jam** (~5 hari), berbanding lurus dengan kontributor eksternal yang memakan waktu rata-rata **220.16 jam** (~9 hari).

3. **Simulasi Komputasi & Optimasi Sistem (Menjawab P3):**
   **1.Prediksi Bottleneck:** Simulasi Monte Carlo dengan 50.000 iterasi memproyeksikan probabilitas terjadinya penumpukan pekerjaan (isu tertunda > 30 hari) sebesar 9.05% (0.0905) berdasarkan distribusi empiris.
   **2.Deduplikasi Isu::** Implementasi Bloom Filter (n=2000, m=10000, k=5) berhasil menyaring laporan ganda dengan False Positive Rate (FPR) teoretis yang sangat efisien, yaitu 0.02% (0.00020).
   **3.Optimasi Sprint Planning:** Algoritma MCMC Knapsack berhasil mengoptimasi alokasi kerja maintainer. Dari kapasitas maksimal 1000.0 jam, algoritma merekomendasikan alokasi beban kerja optimal sebesar 893 jam dengan total nilai dampak (value) maksimal di angka 132.
   
---

---

## 📚 Referensi Akademik
Seluruh formulasi matematis dan implementasi fungsi di dalam direktori `src/` disusun dengan mematuhi referensi utama:
> Tsun, A. (2020). *Probability and Statistics for Engineers and Scientists*. (Format MLE, aturan konjugasi Beta, perhitungan interval, dan uji hipotesis).# 📊 Laporan Audit Statistik: pandas-dev/pandas

**Mata Kuliah:** Statistika dan Probabilitas (Minggu 11–14) | **Program Studi:** Sistem dan Teknologi Informasi (STI) 2025  
**Repositori Target:** [pandas-dev/pandas](https://github.com/pandas-dev/pandas)

---

## 🚀 Tinjauan Proyek & Sumber Data
Audit ini bertujuan untuk mengukur metrik kesehatan dan perilaku repositori *open-source* `pandas-dev/pandas` secara statistik. Repositori ini dipilih karena memenuhi syarat mutlak: memiliki lebih dari 1.000 *issue* tertutup, 500+ *Pull Request* (PR) yang berhasil di-*merge*, serta memiliki rekam jejak waktu (*timestamp*) yang jelas.

* **Sumber API:** GitHub REST API v3
* **Limitasi Data:** Data ditarik sebanyak 2.000 sampel menggunakan metode *pagination* berdasarkan batasan *rate limit* API reguler. Meskipun dataset mentah mencakup status *open* dan *closed*, keseluruhan analisis statistik (seperti estimasi probabilitas dan waktu penyelesaian) difokuskan secara eksklusif pada *issue* dan PR yang telah mencapai status akhir (*closed* atau *merged*).

---

## 👥 Tim Peneliti & Peran

| Anggota Tim | Peran | Fokus Tanggung Jawab |
|---|---|---|
| **Zaida Alfaiz Sofyan** (1519625047) | Data Engineer | Ekstraksi API, pembersihan data (*cleaning*), EDA, visualisasi awal |
| **Ihsan Nurrahman Syauqy** (1519625037) | Estimation Analyst | Kalkulasi MLE (Poisson/Bernoulli), konjugasi Beta Posterior, visualisasi *likelihood* |
| **Kevin Christman Lumban Tobing** (1519625025) | Inference Analyst | Perhitungan rentang ketidakpastian (*Confidence & Credible Intervals*) |
| **Safani Nuraini** (1519625008) | Hypothesis Analyst | Uji hipotesis Z-Test, penetapan H0/H1, interpretasi keputusan *p-value* |
| **Fernando Iskandar Yusuf** (1519625042) | Computation Analyst | Prediksi dengan Simulasi Monte Carlo, optimasi Bloom Filter, MCMC |

---

## 🎯 Fokus Pertanyaan Riset (RQ)
Setiap lapisan analisis (Minggu 11-14) dirancang untuk berkesinambungan dan menjawab tiga pertanyaan krusial berikut:

1. **Fase Estimasi & Inferensi (Modul 02 & 03):** Berapa estimasi probabilitas sebuah PR diterima (*merged*) di repositori Pandas, beserta rata-rata harian frekuensi *issue* baru, dan seberapa besar rentang ketidakpastian dari estimasi tersebut?
2. **Fase Pengujian Hipotesis (Modul 04):** Apakah terdapat perbedaan waktu penyelesaian (*time-to-close*) yang signifikan secara statistik antara *issue* yang ditangani oleh *Core Member* dengan *Contributor* eksternal?
3. **Fase Simulasi Komputasi (Modul 05):** Berapa probabilitas terjadinya penumpukan beban kerja (*bottleneck*) dalam penyelesaian *issue* di masa mendatang jika diestimasi tanpa menggunakan rumus analitik?

---

## 📁 Struktur Repository

```text
stat-audit-pandas-sti-2025/
├── README.md                         ← Deskripsi proyek & temuan
├── AI_USAGE_LOG.md                   ← Log transparansi AI
├── data/
│   ├── raw/                          ← Data mentah (JSON)
│   └── clean/dataset.csv             ← Data bersih siap analisis
├── src/
│   ├── estimator.py                  ← Fungsi MLE & Posterior
│   ├── inference.py                  ← Fungsi Confidence/Credible Interval
│   ├── hypothesis.py                 ← Fungsi Uji Z-Test
│   └── simulation.py                 ← Fungsi Stokastik & MCMC
├── notebooks/
│   ├── 01_eda.ipynb                  ← Analisis Data Eksploratif
│   ├── 02_estimation.ipynb           ← Estimasi Parameter 
│   ├── 03_confidence_interval.ipynb  ← Inferensi Statistik
│   ├── 04_hypothesis_testing.ipynb   ← Uji Hipotesis
│   └── 05_simulation.ipynb           ← Simulasi Komputasi
├── report/
│   
├── presentation/
│   
└── requirements.txt
``` 

## ⚙️ Petunjuk Eksekusi (*How-to-Run*)

Pastikan lingkungan Python 3 Anda sudah siap. Kode dan *notebook* disusun dengan rapi agar dapat dieksekusi secara berurutan dari hulu ke hilir.

```bash
# 1. Clone repositori ke mesin lokal
git clone https://github.com/tobslayerr/stat-audit-pandas-sti-2025.git
cd stat-audit-pandas-sti-2025

# 2. Instalasi dependensi wajib
pip install -r requirements.txt

# 3. Jalankan server Jupyter Notebook
jupyter notebook
```
## 📈 Temuan Utama

Berdasarkan hasil analisis komprehensif dari fase ekstraksi data (EDA), estimasi parameter titik (MLE), hingga uji inferensial hipotesis,hingga simulasi komputasional **Pertanyaan Riset 1 (P1), Pertanyaan Riset 2 (P2), dan Pertanyaan Riset 3 (P3)** dengan temuan sebagai berikut:

1. **Estimasi & Inferensi Probabilitas (Menjawab P1):**
   Estimasi probabilitas sebuah PR berhasil diterima (*merged*) di repositori Pandas adalah sebesar **64.39%** (0.6439). Berdasarkan pengukuran rentang ketidakpastian menggunakan pendekatan *Confidence Interval* (Frequentist) dan *Credible Interval* (Bayesian) pada tingkat kepercayaan 95%, tim menyimpulkan bahwa probabilitas penerimaan populasi yang sesungguhnya berada pada rentang presisi **0.6214 hingga 0.6665**. Selain itu, rata-rata kemunculan *issue* baru diprediksi sebesar **14.71 issue per hari** dengan margin ketidakpastian (*Confidence Interval* 95%) berada pada rentang sempit antara **14.06 hingga 15.35 issue per hari**.

2. **Uji Hipotesis Performa Penyelesaian (Menjawab P2):**
   Berdasarkan pengujian hipotesis (Z-Test Dua Sampel Independen) pada tingkat signifikansi 5% ($\alpha = 0.05$), tim **menolak H0**. Terdapat bukti statistik yang kuat bahwa **ada perbedaan signifikan pada rata-rata waktu penyelesaian (time-to-close) antara Core Member dan Contributor eksternal**. *Core Member* terbukti jauh lebih cepat dalam menyelesaikan tugas dengan rata-rata waktu **120.65 jam** (~5 hari), berbanding lurus dengan kontributor eksternal yang memakan waktu rata-rata **220.16 jam** (~9 hari).

3. **Simulasi Komputasi & Optimasi Sistem (Menjawab P3):**
   **1.Prediksi Bottleneck:** Simulasi Monte Carlo dengan 50.000 iterasi memproyeksikan probabilitas terjadinya penumpukan pekerjaan (isu tertunda > 30 hari) sebesar 9.05% (0.0905) berdasarkan distribusi empiris.
   **2.Deduplikasi Isu::** Implementasi Bloom Filter (n=2000, m=10000, k=5) berhasil menyaring laporan ganda dengan False Positive Rate (FPR) teoretis yang sangat efisien, yaitu 0.02% (0.00020).
   **3.Optimasi Sprint Planning:** Algoritma MCMC Knapsack berhasil mengoptimasi alokasi kerja maintainer. Dari kapasitas maksimal 1000.0 jam, algoritma merekomendasikan alokasi beban kerja optimal sebesar 893 jam dengan total nilai dampak (value) maksimal di angka 132.
   
---

---

## 📚 Referensi Akademik
Seluruh formulasi matematis dan implementasi fungsi di dalam direktori `src/` disusun dengan mematuhi referensi utama:
> Tsun, A. (2020). *Probability and Statistics for Engineers and Scientists*. (Format MLE, aturan konjugasi Beta, perhitungan interval, dan uji hipotesis).
