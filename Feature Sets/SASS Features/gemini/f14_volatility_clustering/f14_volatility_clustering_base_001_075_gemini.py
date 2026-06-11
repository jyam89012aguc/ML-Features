# f14_volatility_clustering — REAL indicator logic (base 001..075)
# Indicator: volatility clustering / ARCH effects.
# Core math: autocorrelation of SQUARED and ABSOLUTE returns at lags 1/2/3/5/10
# (the ARCH signature), volatility persistence (EWMA-vol autocorrelation),
# GARCH-like half-life of vol shocks, a Ljung-Box-style statistic on squared
# returns, clustering strength (summed squared-return ACF), high-vol streaks,
# vol-of-vol, and current-vs-trailing volatility ratios.
# Windows > 21d use 'closeadj' (per spec). Returns are log closeadj returns.
import numpy as np
import pandas as pd

WINDOWS = [21, 63, 126, 252]
LAGS = [1, 2, 3, 5, 10]


def _ret(df):
    """Log returns on closeadj (the >21d-safe adjusted close)."""
    c = df['closeadj'].astype(float)
    return np.log(c / c.shift(1))


def _clean(s):
    return s.replace([np.inf, -np.inf], np.nan)


def _rolling_acf(x, lag, window):
    """Rolling autocorrelation of series x at a given lag over `window` obs.

    Computed as the rolling correlation between x and x.shift(lag); this is the
    standard sample-ACF estimator and is the heart of the ARCH-effect signal.
    """
    return _clean(x.rolling(window).corr(x.shift(lag)))


def _ewma_vol(r, span):
    """EWMA volatility (RiskMetrics-style) of returns."""
    return np.sqrt(r.pow(2).ewm(span=span, min_periods=max(5, span // 3)).mean())


def _z(s, window):
    m = s.rolling(window).mean()
    sd = s.rolling(window).std()
    return _clean((s - m) / sd)


def _half_life(rho):
    """Half-life implied by an AR(1) persistence coefficient rho in (0,1).

    hl = ln(0.5)/ln(rho); rho clipped to (0,1) so the log is well-defined.
    """
    r = rho.clip(lower=1e-4, upper=0.9999)
    return _clean(np.log(0.5) / np.log(r))


def get_f14_volatility_clustering_base_001_075(df):
    features = {}
    r = _ret(df)
    r2 = r.pow(2)        # squared returns  -> ARCH effects
    ra = r.abs()         # absolute returns -> long-memory clustering

    def put(i, series):
        features[f'f14_volatility_clustering_{i:03d}'] = _clean(series)

    i = 1

    # --- Facet A: ACF of SQUARED returns at lags 1/2/3/5/10, all windows (20) ---
    # The canonical ARCH signature: squared-return autocorrelation.
    for w in WINDOWS:
        for lag in LAGS:
            put(i, _rolling_acf(r2, lag, w)); i += 1

    # --- Facet B: ACF of ABSOLUTE returns at lags 1/2/3/5/10, all windows (20) ---
    # |r| ACF captures volatility long-memory / clustering persistence.
    for w in WINDOWS:
        for lag in LAGS:
            put(i, _rolling_acf(ra, lag, w)); i += 1

    # --- Facet C: clustering strength = SUM of squared-return ACF over lags 1..10 ---
    # Larger sum => stronger ARCH clustering. One per window (4).
    for w in WINDOWS:
        acf_sum = sum(_rolling_acf(r2, lag, w) for lag in LAGS)
        put(i, acf_sum); i += 1

    # --- Facet D: clustering strength on |returns| (sum of |r| ACF), per window (4) ---
    for w in WINDOWS:
        acf_sum = sum(_rolling_acf(ra, lag, w) for lag in LAGS)
        put(i, acf_sum); i += 1

    # --- Facet E: Ljung-Box-style statistic on squared returns (4) ---
    # Q = n * sum_k rho_k^2  (k=1..10): magnitude of ARCH dependence.
    for w in WINDOWS:
        q = sum(_rolling_acf(r2, lag, w).pow(2) for lag in LAGS) * float(w)
        put(i, q); i += 1

    # --- Facet F: Ljung-Box-style statistic on |returns| (4) ---
    for w in WINDOWS:
        q = sum(_rolling_acf(ra, lag, w).pow(2) for lag in LAGS) * float(w)
        put(i, q); i += 1

    # --- Facet G: vol persistence via EWMA-vol lag-1 autocorrelation (4) ---
    # Persistent vol => high autocorrelation of the EWMA vol process itself.
    for w in WINDOWS:
        ev = _ewma_vol(r, span=w)
        put(i, _rolling_acf(ev, 1, w)); i += 1

    # --- Facet H: GARCH-like half-life of vol shocks (4) ---
    # From AR(1) persistence of the EWMA-vol series.
    for w in WINDOWS:
        ev = _ewma_vol(r, span=w)
        rho = _rolling_acf(ev, 1, w)
        put(i, _half_life(rho)); i += 1

    # --- Facet I: current vol / trailing vol ratio (4) ---
    # Vol clustering => the short-window vol stays elevated relative to its own
    # trailing average (ratio > 1 during clusters).
    for w in WINDOWS:
        short = r.rolling(max(5, w // 5)).std()
        trail = r.rolling(w).std()
        put(i, _clean(short / trail)); i += 1

    # --- Facet J: z-score of the squared-return lag-1 ACF (4) ---
    # How extreme is current ARCH clustering vs its own recent history.
    for w in WINDOWS:
        acf1 = _rolling_acf(r2, 1, w)
        put(i, _z(acf1, w)); i += 1

    # i is now 77 -> we have produced 76? guard: we need exactly 075.
    # Counts: A20 B20 C4 D4 E4 F4 G4 H4 I4 J4 = 72. Need 3 more (73,74,75).

    # --- Facet K: short-vs-long clustering spread (squared-ACF lag1) (3) ---
    # Difference between a short-window and a long-window ARCH estimate.
    acf1_21 = _rolling_acf(r2, 1, 21)
    acf1_63 = _rolling_acf(r2, 1, 63)
    acf1_126 = _rolling_acf(r2, 1, 126)
    acf1_252 = _rolling_acf(r2, 1, 252)
    put(i, _clean(acf1_21 - acf1_63)); i += 1
    put(i, _clean(acf1_63 - acf1_126)); i += 1
    put(i, _clean(acf1_126 - acf1_252)); i += 1

    out = pd.DataFrame(features)
    # Ensure exact ordering / naming 001..075
    cols = [f'f14_volatility_clustering_{k:03d}' for k in range(1, 76)]
    return out[cols]
