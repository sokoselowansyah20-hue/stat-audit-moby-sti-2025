"""
simulation.py — Computation Analyst Module (Member E)
Statistical Audit of pandas-dev/pandas
STI Final Group Assignment 2025

All formulas sourced from:
    Tsun, Probability & Statistics with Applications to Computing, 2020

Functions:
    estimate_probability(event_fn, n_trials=50000)
    BloomFilter(k, m) — class with add(), contains(), theoretical_fpr()
    mcmc_knapsack(items, capacity, n_iter=100000)
"""

import numpy as np
import math
import hashlib


# ---------------------------------------------------------------------------
# 1. Monte Carlo Simulation
# ---------------------------------------------------------------------------

def estimate_probability(event_fn, n_trials: int = 50_000) -> float:
    """
    Estimasi probabilitas suatu kejadian menggunakan Monte Carlo.

    Metode ini mensimulasikan n_trials percobaan independen, menghitung
    frekuensi relatif kejadian yang memenuhi event_fn, dan menggunakannya
    sebagai estimator probabilitas.

    Formula (Tsun, 2020, p. 323):
        P(A) ≈ (jumlah kejadian A) / n_trials

    Parameters
    ----------
    event_fn : callable
        Fungsi tanpa argumen yang mengembalikan True/False pada setiap trial.
        Contoh: lambda: np.random.exponential(30) > 30
    n_trials : int, default 50_000
        Jumlah iterasi simulasi. Semakin besar → estimasi semakin akurat.

    Returns
    -------
    float
        Estimasi probabilitas antara 0.0 dan 1.0.

    Examples
    --------
    >>> # P(issue butuh > 30 hari untuk ditutup) jika rata-rata = 25 hari
    >>> p = estimate_probability(lambda: np.random.exponential(25) > 30)
    >>> round(p, 2)  # sekitar 0.30
    """
    np.random.seed(42)
    successes = sum(1 for _ in range(n_trials) if event_fn())
    return successes / n_trials


def monte_carlo_issue_resolution(
    mean_days: float,
    threshold_days: float = 30,
    n_trials: int = 50_000
) -> dict:
    """
    Estimasi probabilitas bahwa sebuah issue pandas membutuhkan lebih dari
    threshold_days hari untuk diselesaikan, menggunakan distribusi Exponential.

    Konteks penelitian:
        RQ3 — "Berapa probabilitas sebuah issue dipilih secara acak memerlukan
        lebih dari 30 hari untuk ditutup, tanpa rumus analitik?"

    Formula Monte Carlo (Tsun, 2020, p. 323):
        P(X > t) ≈ #{X_i > t} / n_trials

    Parameters
    ----------
    mean_days : float
        Rata-rata waktu penyelesaian issue (dari data EDA).
    threshold_days : float, default 30
        Ambang batas hari yang diuji.
    n_trials : int, default 50_000
        Jumlah simulasi.

    Returns
    -------
    dict dengan kunci:
        'p_estimate'   : float — probabilitas estimasi
        'mean_days'    : float
        'threshold'    : float
        'n_trials'     : int
        'std_error'    : float — standar error Monte Carlo
    """
    np.random.seed(42)
    samples = np.random.exponential(scale=mean_days, size=n_trials)
    p_hat = np.mean(samples > threshold_days)
    std_err = np.sqrt(p_hat * (1 - p_hat) / n_trials)
    return {
        "p_estimate": float(p_hat),
        "mean_days": mean_days,
        "threshold": threshold_days,
        "n_trials": n_trials,
        "std_error": float(std_err),
    }


# ---------------------------------------------------------------------------
# 2. Bloom Filter
# ---------------------------------------------------------------------------

class BloomFilter:
    """
    Implementasi Bloom Filter probabilistik untuk deteksi kontributor duplikat.

    Bloom Filter menggunakan k fungsi hash dan bit-array berukuran m untuk
    memeriksa keanggotaan dengan kemungkinan false positive (FPR) terkontrol.
    Berguna untuk memeriksa apakah sebuah username kontributor pernah tercatat
    tanpa menyimpan seluruh daftar.

    Formula FPR (Tsun, 2020, p. 329):
        FPR = (1 - (1 - 1/m)^n)^k
        ≈ (1 - e^(-kn/m))^k  untuk m besar

    Parameters
    ----------
    k : int
        Jumlah fungsi hash yang digunakan.
    m : int
        Ukuran bit-array (jumlah bit).

    Examples
    --------
    >>> bf = BloomFilter(k=3, m=1000)
    >>> bf.add("pandas-dev")
    >>> bf.contains("pandas-dev")
    True
    >>> bf.contains("unknown-user")
    False
    """

    def __init__(self, k: int, m: int):
        """
        Inisialisasi Bloom Filter.

        Parameters
        ----------
        k : int — jumlah fungsi hash
        m : int — ukuran bit-array
        """
        self.k = k
        self.m = m
        self._bits = bytearray(m)  # bit-array, 0 atau 1
        self._n_inserted = 0       # jumlah elemen yang sudah ditambahkan

    def _hash_positions(self, item: str) -> list[int]:
        """
        Menghasilkan k posisi hash untuk item yang diberikan.
        Menggunakan MD5 dengan seed berbeda untuk setiap fungsi hash ke-i.

        Parameters
        ----------
        item : str — elemen yang akan di-hash

        Returns
        -------
        list[int] — daftar k indeks posisi dalam bit-array
        """
        positions = []
        for i in range(self.k):
            digest = hashlib.md5(f"{i}:{item}".encode()).hexdigest()
            pos = int(digest, 16) % self.m
            positions.append(pos)
        return positions

    def add(self, item: str) -> None:
        """
        Tambahkan item ke Bloom Filter dengan menyetel k bit menjadi 1.

        Parameters
        ----------
        item : str — string yang akan ditambahkan (mis. username kontributor)
        """
        for pos in self._hash_positions(item):
            self._bits[pos] = 1
        self._n_inserted += 1

    def contains(self, item: str) -> bool:
        """
        Periksa apakah item mungkin ada dalam filter.

        Jika semua k bit bernilai 1 → kemungkinan ada (bisa false positive).
        Jika ada bit yang 0 → pasti tidak ada (no false negative).

        Parameters
        ----------
        item : str — string yang diperiksa

        Returns
        -------
        bool — True jika mungkin ada, False jika pasti tidak ada
        """
        return all(self._bits[pos] == 1 for pos in self._hash_positions(item))

    def theoretical_fpr(self, n: int) -> float:
        """
        Hitung False Positive Rate teoritis untuk n elemen yang disisipkan.

        Formula (Tsun, 2020, p. 329):
            FPR = (1 - (1 - 1/m)^n)^k

        Parameters
        ----------
        n : int — jumlah elemen yang telah disisipkan

        Returns
        -------
        float — probabilitas false positive antara 0.0 dan 1.0
        """
        fpr = (1 - (1 - 1 / self.m) ** n) ** self.k
        return float(fpr)


# ---------------------------------------------------------------------------
# 3. MCMC — Metropolis-Hastings untuk Knapsack
# ---------------------------------------------------------------------------

def mcmc_knapsack(
    items: list[dict],
    capacity: int,
    n_iter: int = 100_000
) -> dict:
    """
    Gunakan MCMC (Metropolis-Hastings) untuk memperkirakan distribusi nilai
    total isu/PR yang dapat diselesaikan dalam satu sprint (kapasitas terbatas).

    Analogi knapsack: setiap "item" mewakili sebuah issue/PR dengan atribut:
      - 'weight' : perkiraan waktu pengerjaan (hari)
      - 'value'  : skor prioritas kontribusi (mis. jumlah komentar, reactions)

    Rantai Markov memulai dari solusi acak dan menerima/menolak flip bit
    menggunakan kriteria Metropolis untuk menjelajahi ruang solusi yang layak.

    Konteks penelitian (Tsun, 2020, p. 335):
        MCMC digunakan untuk menjelajahi ruang solusi yang terlalu besar
        untuk dihitung secara analitik (2^n kemungkinan subset).

    Parameters
    ----------
    items : list[dict]
        Setiap dict memiliki kunci 'weight' (int) dan 'value' (int).
    capacity : int
        Kapasitas maksimum total weight yang diizinkan.
    n_iter : int, default 100_000
        Jumlah langkah Markov Chain.

    Returns
    -------
    dict dengan kunci:
        'best_value'     : int — nilai tertinggi yang ditemukan
        'best_items'     : list[int] — indeks item dalam solusi terbaik
        'value_trace'    : list[int] — riwayat nilai yang diterima (tiap 1000 iter)
        'acceptance_rate': float — rasio penerimaan langkah
        'n_items'        : int
        'capacity'       : int
    """
    np.random.seed(42)
    n = len(items)
    weights = np.array([it["weight"] for it in items])
    values  = np.array([it["value"]  for it in items])

    # State awal: semua item tidak dipilih
    state = np.zeros(n, dtype=int)

    def total_weight(s):
        return int(np.dot(s, weights))

    def total_value(s):
        return int(np.dot(s, values))

    current_val   = 0
    best_state    = state.copy()
    best_val      = 0
    value_trace   = []
    accepted       = 0

    for step in range(n_iter):
        # Proposal: flip satu bit secara acak
        idx = np.random.randint(0, n)
        proposal = state.copy()
        proposal[idx] = 1 - proposal[idx]

        # Periksa kelayakan (feasibility)
        if total_weight(proposal) > capacity:
            # Tolak langsung jika melebihi kapasitas
            pass
        else:
            prop_val = total_value(proposal)
            # Kriteria Metropolis: terima jika lebih baik, atau secara probabilistik
            delta = prop_val - current_val
            if delta >= 0 or np.random.random() < np.exp(delta / max(current_val, 1)):
                state = proposal
                current_val = prop_val
                accepted += 1

                if current_val > best_val:
                    best_val   = current_val
                    best_state = state.copy()

        if (step + 1) % 1000 == 0:
            value_trace.append(current_val)

    return {
        "best_value":      best_val,
        "best_items":      list(np.where(best_state == 1)[0]),
        "value_trace":     value_trace,
        "acceptance_rate": round(accepted / n_iter, 4),
        "n_items":         n,
        "capacity":        capacity,
    }
