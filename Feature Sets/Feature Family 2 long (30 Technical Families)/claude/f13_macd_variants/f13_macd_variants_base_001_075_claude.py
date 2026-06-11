"""f13_macd_variants base features 001-075.

Domain: MACD construct and variants. Classic MACD = EMA(close,12) - EMA(close,26).
Signal line = EMA(MACD, 9). Histogram = MACD - signal. Every feature references
an MACD-like construct (fast MA minus slow MA used as a momentum oscillator).

Each function is a fully-expanded def block, formula inline. Window > 21d uses
closeadj. Windows <= 21d use close. NaN policy: never fillna(<value>); preserve
NaN through warm-up. Only replace([inf,-inf], nan) at the function's final return.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Helpers (each feature uses these inside its own expanded expression)
# ---------------------------------------------------------------------------


def _ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False, min_periods=n).mean()


def _wilder(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()


def _wma(s: pd.Series, n: int) -> pd.Series:
    w = np.arange(1, n + 1, dtype=float)
    return s.rolling(n, min_periods=n).apply(
        lambda x: float(np.dot(x, w) / w.sum()), raw=True
    )


def _hma(s: pd.Series, n: int) -> pd.Series:
    n2 = max(2, n // 2)
    sq = max(2, int(np.sqrt(n)))
    return _wma(2.0 * _wma(s, n2) - _wma(s, n), sq)


def _dema(s: pd.Series, n: int) -> pd.Series:
    e1 = _ema(s, n)
    e2 = _ema(e1, n)
    return 2.0 * e1 - e2


def _zlema(s: pd.Series, n: int) -> pd.Series:
    lag = (n - 1) // 2
    return _ema(s + (s - s.shift(lag)), n)


# ---------------------------------------------------------------------------
# Features 001-075. Heavy structural diversity to keep |corr| <= 0.95:
# few raw MACD lines; most features are signs/streaks/ranks/z-scores/
# discrete-state transforms of MACD-like constructs.
# ---------------------------------------------------------------------------


# --- (3) Raw MACD lines — widely spaced windows ----------------------------


def f13mc_f13_macd_variants_macddetrend_12_26_base_v001_signal(close):
    """Classic MACD(12,26) MINUS 30d trailing mean — drift-detrended classic MACD line."""
    m = _ema(close, 12) - _ema(close, 26)
    return (m - m.rolling(30, min_periods=15).mean()).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_macdslowdetrend_50_200_base_v002_signal(closeadj):
    """Long-term MACD(50,200) MINUS its 100d trailing mean — drift-removed slow MACD line
    (decorrelated from the normalized version)."""
    m = _ema(closeadj, 50) - _ema(closeadj, 200)
    return (m - m.rolling(100, min_periods=50).mean()).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_macd_3_10_base_v003_signal(close):
    """Very-fast MACD(3,10) on close. Reactive raw line."""
    m = _ema(close, 3) - _ema(close, 10)
    return m.replace([np.inf, -np.inf], np.nan)


# --- (5) Normalized MACDs at different scales (drift-stable) ---------------


def f13mc_f13_macd_variants_macdnorm_12_26_base_v004_signal(close):
    """Normalized MACD: (EMA12 - EMA26) / EMA26 — percent-of-price MACD."""
    e12 = _ema(close, 12)
    e26 = _ema(close, 26)
    out = (e12 - e26) / e26.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_macdrank_8_21_60d_base_v005_signal(close):
    """Pct rank (0-1) of MACD(8,21) over trailing 60 bars — bounded rank-form fast MACD."""
    m = _ema(close, 8) - _ema(close, 21)
    return m.rolling(60, min_periods=30).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_macdnorm_50_200_base_v006_signal(closeadj):
    """Long-term normalized MACD(50,200) — percent vs EMA200."""
    e1 = _ema(closeadj, 50)
    e2 = _ema(closeadj, 200)
    out = (e1 - e2) / e2.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_macdsignagree_5_35_19_39_base_v007_signal(close):
    """sign(MACD(5,35)) * sign(MACD(19,39)) — fast/slow MACD-sign agreement (+1/-1)."""
    a = _ema(close, 5) - _ema(close, 35)
    b = _ema(close, 19) - _ema(close, 39)
    return (np.sign(a) * np.sign(b)).where(~a.isna() & ~b.isna()).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_macdnorm_19_39_z_base_v008_signal(closeadj):
    """Z-score of normalized MACD(19,39) over 90d — drift-removed slow normalized MACD."""
    e1 = _ema(closeadj, 19)
    e2 = _ema(closeadj, 39)
    r = (e1 - e2) / e2.replace(0.0, np.nan)
    mu = r.rolling(90, min_periods=45).mean()
    sd = r.rolling(90, min_periods=45).std()
    return ((r - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- (3) MACD signal lines (smoothed MACD) at different windows -----------


def f13mc_f13_macd_variants_signal_12_26_9_base_v009_signal(close):
    """Classic MACD signal: EMA(MACD(12,26), 9). Smoothed MACD line."""
    m = _ema(close, 12) - _ema(close, 26)
    return _ema(m, 9).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_signalnorm_19_39_13_base_v010_signal(closeadj):
    """Normalized signal of MACD(19,39,13) / EMA39 — bounded percent."""
    e1 = _ema(closeadj, 19)
    e2 = _ema(closeadj, 39)
    m = e1 - e2
    out = _ema(m, 13) / e2.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- (5) Histograms (MACD - signal) — fundamentally different from MACD --


def f13mc_f13_macd_variants_hist_12_26_9_base_v011_signal(close):
    """Classic MACD histogram = MACD - signal (12,26,9)."""
    m = _ema(close, 12) - _ema(close, 26)
    sig = _ema(m, 9)
    return (m - sig).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_hist_8_21_5_base_v012_signal(close):
    """MACD histogram on faster (8,21,5)."""
    m = _ema(close, 8) - _ema(close, 21)
    sig = _ema(m, 5)
    return (m - sig).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_hist_50_200_30_base_v013_signal(closeadj):
    """Slow MACD histogram on (50,200,30)."""
    m = _ema(closeadj, 50) - _ema(closeadj, 200)
    sig = _ema(m, 30)
    return (m - sig).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_histdetrend_12_26_9_base_v014_signal(close):
    """Histogram MINUS its 20-bar trailing mean — drift-removed histogram (12,26,9)."""
    m = _ema(close, 12) - _ema(close, 26)
    sig = _ema(m, 9)
    h = m - sig
    return (h - h.rolling(20, min_periods=20).mean()).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_histabs_12_26_9_base_v015_signal(close):
    """Absolute histogram / close — magnitude of MACD-signal divergence."""
    m = _ema(close, 12) - _ema(close, 26)
    sig = _ema(m, 9)
    h = (m - sig).abs()
    return (h / close.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- (6) Sign-of-MACD-construct features (discrete states) ----------------


def f13mc_f13_macd_variants_signxsig_12_26_9_base_v016_signal(close):
    """sign(MACD - signal) (12,26,9) — line vs signal discrete state."""
    m = _ema(close, 12) - _ema(close, 26)
    sig = _ema(m, 9)
    return np.sign(m - sig).where(~m.isna() & ~sig.isna()).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_signxzero_12_26_base_v017_signal(close):
    """sign(MACD(12,26)) — above/below zero classic state."""
    m = _ema(close, 12) - _ema(close, 26)
    return np.sign(m).where(~m.isna()).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_signxzero_50_200_base_v018_signal(closeadj):
    """sign(MACD(50,200)) — long-term zero-line position (regime indicator)."""
    m = _ema(closeadj, 50) - _ema(closeadj, 200)
    return np.sign(m).where(~m.isna()).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_bullstate_12_26_9_base_v019_signal(close):
    """+1 MACD>signal AND MACD>0 (bull), -1 both negative (bear), 0 mixed."""
    m = _ema(close, 12) - _ema(close, 26)
    sig = _ema(m, 9)
    bull = ((m > sig) & (m > 0.0)).astype(float)
    bear = ((m < sig) & (m < 0.0)).astype(float)
    out = bull - bear
    return out.where(~m.isna() & ~sig.isna()).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_quaddays_12_26_9_base_v020_signal(close):
    """Days-since-last-quadrant-change of (sign(MACD), sign(MACD-signal)), capped 60.
    Discrete-state persistence on the MACD quadrant."""
    m = _ema(close, 12) - _ema(close, 26)
    sig = _ema(m, 9)
    state = 2.0 * np.sign(m) + np.sign(m - sig)
    flip = (state != state.shift(1)).astype(float).where(~state.isna() & ~state.shift(1).isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return 60.0
        return float(len(x) - 1 - idx[-1])
    return flip.rolling(60, min_periods=20).apply(_ds, raw=True).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_histslopesign_12_26_9_base_v021_signal(close):
    """sign of 3-bar diff of MACD histogram — short-term histogram direction."""
    m = _ema(close, 12) - _ema(close, 26)
    h = m - _ema(m, 9)
    return np.sign(h.diff(3)).where(~h.isna() & ~h.shift(3).isna()).replace([np.inf, -np.inf], np.nan)


# --- (6) Days-since / streaks / cross-counts on MACD constructs ----------


def f13mc_f13_macd_variants_dayssincex_12_26_9_base_v022_signal(close):
    """Days since last MACD/signal cross (12,26,9), capped 100."""
    m = _ema(close, 12) - _ema(close, 26)
    sig = _ema(m, 9)
    s = np.sign(m - sig)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return 100.0
        return float(len(x) - 1 - idx[-1])
    return flip.rolling(100, min_periods=20).apply(_ds, raw=True).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_dayssincez_19_39_base_v023_signal(closeadj):
    """Days since last MACD(19,39) zero-line cross, capped 120."""
    m = _ema(closeadj, 19) - _ema(closeadj, 39)
    s = np.sign(m)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return 120.0
        return float(len(x) - 1 - idx[-1])
    return flip.rolling(120, min_periods=30).apply(_ds, raw=True).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_streakabove_12_26_9_base_v024_signal(close):
    """Bipolar streak: +k if MACD>signal for k bars; -k if MACD<signal. Cap +/-60."""
    m = _ema(close, 12) - _ema(close, 26)
    sig = _ema(m, 9)
    above = (m > sig).astype(float).where(~m.isna() & ~sig.isna())
    grp = (above != above.shift(1)).cumsum()
    run = above.groupby(grp).cumcount() + 1.0
    out = np.where(above > 0.5, run, -run)
    s = pd.Series(out, index=close.index, dtype=float).clip(-60.0, 60.0)
    return s.where(~above.isna()).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_streakabovez_50_200_base_v025_signal(closeadj):
    """Bipolar streak above/below zero for MACD(50,200), cap +/-150."""
    m = _ema(closeadj, 50) - _ema(closeadj, 200)
    above = (m > 0.0).astype(float).where(~m.isna())
    grp = (above != above.shift(1)).cumsum()
    run = above.groupby(grp).cumcount() + 1.0
    out = np.where(above > 0.5, run, -run)
    s = pd.Series(out, index=closeadj.index, dtype=float).clip(-150.0, 150.0)
    return s.where(~above.isna()).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_xcount_12_26_9_60d_base_v026_signal(closeadj):
    """Count of MACD/signal sign flips in trailing 60 bars (12,26,9)."""
    m = _ema(closeadj, 12) - _ema(closeadj, 26)
    sig = _ema(m, 9)
    s = np.sign(m - sig)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(60, min_periods=60).sum().replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_xcountz_19_39_120d_base_v027_signal(closeadj):
    """MACD(19,39) zero-line cross count in trailing 120 bars."""
    m = _ema(closeadj, 19) - _ema(closeadj, 39)
    s = np.sign(m)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(120, min_periods=120).sum().replace([np.inf, -np.inf], np.nan)


# --- (5) Histogram ranks / z / skew / kurt — distributional histograms ---


def f13mc_f13_macd_variants_histrank_12_26_9_60d_base_v028_signal(closeadj):
    """Pct rank (0-1) of MACD histogram within trailing 60 bars."""
    m = _ema(closeadj, 12) - _ema(closeadj, 26)
    h = m - _ema(m, 9)
    return h.rolling(60, min_periods=30).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_histratio_to_macdabs_60d_base_v029_signal(closeadj):
    """histogram / rolling mean(|MACD|,60d) — histogram relative to MACD-magnitude scale.
    Differs from rank by being unbounded and from z by no recentering by mean."""
    m = _ema(closeadj, 12) - _ema(closeadj, 26)
    h = m - _ema(m, 9)
    sc = m.abs().rolling(60, min_periods=30).mean()
    return (h / sc.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_histskew_12_26_9_60d_base_v030_signal(closeadj):
    """Skew of MACD histogram over trailing 60 bars."""
    m = _ema(closeadj, 12) - _ema(closeadj, 26)
    h = m - _ema(m, 9)
    return h.rolling(60, min_periods=30).skew().replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_histkurt_12_26_9_80d_base_v031_signal(closeadj):
    """Excess kurtosis of MACD histogram over trailing 80 bars."""
    m = _ema(closeadj, 12) - _ema(closeadj, 26)
    h = m - _ema(m, 9)
    return h.rolling(80, min_periods=40).kurt().replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_histrank_19_39_13_120d_base_v032_signal(closeadj):
    """Pct rank of slow-MACD histogram (19,39,13) over trailing 120 bars."""
    m = _ema(closeadj, 19) - _ema(closeadj, 39)
    h = m - _ema(m, 13)
    return h.rolling(120, min_periods=60).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# --- (4) MACD rank / z / band-position ----------------------------------


def f13mc_f13_macd_variants_macdrank_12_26_120d_base_v033_signal(closeadj):
    """Pct rank (0-1) of MACD line in trailing 120 bars."""
    m = _ema(closeadj, 12) - _ema(closeadj, 26)
    return m.rolling(120, min_periods=60).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_macdz_12_26_60d_base_v034_signal(closeadj):
    """Z-score of MACD line over trailing 60d."""
    m = _ema(closeadj, 12) - _ema(closeadj, 26)
    mu = m.rolling(60, min_periods=30).mean()
    sd = m.rolling(60, min_periods=30).std()
    out = (m - mu) / sd.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_macdbandbreaks_12_26_60d_base_v035_signal(closeadj):
    """Count in trailing 30 bars of MACD breaks above mu+2sd band (60d) — extreme-state count."""
    m = _ema(closeadj, 12) - _ema(closeadj, 26)
    mu = m.rolling(60, min_periods=30).mean()
    sd = m.rolling(60, min_periods=30).std()
    upper = mu + 2.0 * sd
    flag = (m > upper).astype(float).where(~upper.isna() & ~m.isna())
    return flag.rolling(30, min_periods=15).sum().replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_macdrank_50_200_252d_base_v036_signal(closeadj):
    """Pct rank of slow MACD(50,200) in trailing 252 bars (annual)."""
    m = _ema(closeadj, 50) - _ema(closeadj, 200)
    return m.rolling(252, min_periods=120).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# --- (4) Bounded transforms of MACD constructs --------------------------


def f13mc_f13_macd_variants_macdvszero_dist_12_26_60d_base_v037_signal(closeadj):
    """|MACD(12,26)| / std(MACD,60d) — magnitude of MACD relative to its rolling vol."""
    m = _ema(closeadj, 12) - _ema(closeadj, 26)
    sd = m.rolling(60, min_periods=30).std()
    return (m.abs() / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_tanhmacdz_19_39_60d_base_v038_signal(closeadj):
    """tanh of MACD(19,39) z-score on 60d."""
    m = _ema(closeadj, 19) - _ema(closeadj, 39)
    z = (m - m.rolling(60, min_periods=30).mean()) / m.rolling(60, min_periods=30).std().replace(0.0, np.nan)
    return np.tanh(z).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_tanhhist_8_21_5_base_v039_signal(close):
    """tanh(histogram(8,21,5)/close * 200) — bounded histogram-flavor osc."""
    m = _ema(close, 8) - _ema(close, 21)
    h = (m - _ema(m, 5)) / close.replace(0.0, np.nan)
    return np.tanh(h * 200.0).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_signhist_50_200_30_base_v040_signal(closeadj):
    """sign of slow histogram (50,200,30) — discrete state of slow MACD-vs-signal."""
    m = _ema(closeadj, 50) - _ema(closeadj, 200)
    h = m - _ema(m, 30)
    return np.sign(h).where(~h.isna()).replace([np.inf, -np.inf], np.nan)


# --- (4) MACD slopes (intra-feature short-window slope of MACD construct) -


def f13mc_f13_macd_variants_macdslopenorm_12_26_base_v041_signal(close):
    """5-bar MACD slope normalized by rolling-mean(|MACD|,20) — bounded MACD velocity."""
    m = _ema(close, 12) - _ema(close, 26)
    base = m.abs().rolling(20, min_periods=10).mean()
    return (m.diff(5) / base.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_histslope5_12_26_9_base_v042_signal(close):
    """5-bar diff of MACD histogram (12,26,9) — histogram velocity."""
    m = _ema(close, 12) - _ema(close, 26)
    h = m - _ema(m, 9)
    return h.diff(5).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_macdcurv_50_200_base_v043_signal(closeadj):
    """Curvature of slow MACD(50,200): m - 2*m.shift(10) + m.shift(20)."""
    m = _ema(closeadj, 50) - _ema(closeadj, 200)
    out = m - 2.0 * m.shift(10) + m.shift(20)
    return out.replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_histcurv_12_26_9_base_v044_signal(close):
    """Curvature of MACD histogram: h - 2*h.shift(3) + h.shift(6)."""
    m = _ema(close, 12) - _ema(close, 26)
    h = m - _ema(m, 9)
    out = h - 2.0 * h.shift(3) + h.shift(6)
    return out.replace([np.inf, -np.inf], np.nan)


# --- (5) Alternative-kernel MACDs (HMA / DEMA / ZLEMA / Wilder / WMA) ----


def f13mc_f13_macd_variants_hma_macd_12_26_base_v045_signal(close):
    """HMA(12) - HMA(26) — Hull-MA flavored MACD."""
    out = _hma(close, 12) - _hma(close, 26)
    return out.replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_dema_macd_12_26_base_v046_signal(close):
    """DEMA(12) - DEMA(26) — Double-EMA MACD."""
    out = _dema(close, 12) - _dema(close, 26)
    return out.replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_zlemaMACD_histsign_12_26_5_base_v047_signal(close):
    """sign of (ZLEMA-MACD - EMA(ZLEMA-MACD,5)) — zero-lag MACD histogram sign discrete."""
    m = _zlema(close, 12) - _zlema(close, 26)
    h = m - _ema(m, 5)
    return np.sign(h).where(~h.isna()).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_wilderhist_12_26_9_base_v048_signal(close):
    """Wilder(12) - Wilder(26) MINUS Wilder-smoothed signal(9) — Wilder histogram."""
    m = _wilder(close, 12) - _wilder(close, 26)
    sig = _wilder(m, 9)
    return (m - sig).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_wma_macd_12_26_base_v049_signal(close):
    """WMA(12) - WMA(26) — linear-weight MACD."""
    out = _wma(close, 12) - _wma(close, 26)
    return out.replace([np.inf, -np.inf], np.nan)


# --- (4) Kernel-vs-classic MACD differentials (drift-free) --------------


def f13mc_f13_macd_variants_macdkerdiff_hma_base_v050_signal(closeadj):
    """(HMA12 - HMA26) - (EMA12 - EMA26) — HMA vs classic MACD differential."""
    h = _hma(closeadj, 12) - _hma(closeadj, 26)
    e = _ema(closeadj, 12) - _ema(closeadj, 26)
    return (h - e).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_macdkerdiff_dema_base_v051_signal(close):
    """(DEMA12 - DEMA26) - (EMA12 - EMA26) — DEMA lead/lag vs classic."""
    d = _dema(close, 12) - _dema(close, 26)
    e = _ema(close, 12) - _ema(close, 26)
    return (d - e).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_macdkerdiff_zlema_hma_base_v052_signal(close):
    """(ZLEMA12 - ZLEMA26) - (HMA12 - HMA26) — two lead-kernel MACDs' differential.
    Differs structurally from HMA-vs-EMA differential."""
    z = _zlema(close, 12) - _zlema(close, 26)
    h = _hma(close, 12) - _hma(close, 26)
    return (z - h).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_macdkerdiff_wilder_base_v053_signal(closeadj):
    """(Wilder12 - Wilder26) - (EMA12 - EMA26) on closeadj."""
    w = _wilder(closeadj, 12) - _wilder(closeadj, 26)
    e = _ema(closeadj, 12) - _ema(closeadj, 26)
    return (w - e).replace([np.inf, -np.inf], np.nan)


# --- (3) Cross-MACD configuration differentials -------------------------


def f13mc_f13_macd_variants_macdsign_xor_base_v054_signal(close):
    """sign(MACD(8,21)) - sign(MACD(12,26)) — discrete agreement between two configs
    in {-2,0,2}. Decorrelated from raw histogram by being binary-sign-based."""
    m1 = _ema(close, 8) - _ema(close, 21)
    m2 = _ema(close, 12) - _ema(close, 26)
    return (np.sign(m1) - np.sign(m2)).where(~m1.isna() & ~m2.isna()).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_macddiff_fastslow_base_v055_signal(closeadj):
    """Normalized MACD(5,35)/EMA35 - Normalized MACD(19,39)/EMA39 — fast vs slow."""
    e1f = _ema(closeadj, 5); e2f = _ema(closeadj, 35)
    e1s = _ema(closeadj, 19); e2s = _ema(closeadj, 39)
    m1 = (e1f - e2f) / e2f.replace(0.0, np.nan)
    m2 = (e1s - e2s) / e2s.replace(0.0, np.nan)
    return (m1 - m2).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_macddiff_short_long_base_v056_signal(closeadj):
    """sign(MACD(8,21)) - sign(MACD(50,200)) — fast-vs-slow regime alignment in {-2,-1,0,1,2}."""
    m1 = _ema(closeadj, 8) - _ema(closeadj, 21)
    m2 = _ema(closeadj, 50) - _ema(closeadj, 200)
    return (np.sign(m1) - np.sign(m2)).where(~m1.isna() & ~m2.isna()).replace([np.inf, -np.inf], np.nan)


# --- (3) Volume-confirmed / volume-based MACD --------------------------


def f13mc_f13_macd_variants_macdvolconf_12_26_base_v057_signal(close, volume):
    """sign(volume - SMA(volume,20)) * sign(MACD(12,26)) — vol confirmation."""
    m = _ema(close, 12) - _ema(close, 26)
    vs = np.sign(volume - volume.rolling(20, min_periods=20).mean())
    out = np.sign(m) * vs
    return out.where(~m.isna() & ~vs.isna()).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_vwmacd_norm_12_26_base_v058_signal(close, volume):
    """Normalized VWMA-MACD: (VWMA12 - VWMA26) / VWMA26."""
    pv = close * volume
    n12 = pv.rolling(12, min_periods=12).sum() / volume.rolling(12, min_periods=12).sum().replace(0.0, np.nan)
    n26 = pv.rolling(26, min_periods=26).sum() / volume.rolling(26, min_periods=26).sum().replace(0.0, np.nan)
    out = (n12 - n26) / n26.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_volmacd_12_26_base_v059_signal(volume):
    """MACD on log volume: EMA(logV,12) - EMA(logV,26) — volume momentum osc."""
    lv = np.log(volume.replace(0.0, np.nan))
    return (_ema(lv, 12) - _ema(lv, 26)).replace([np.inf, -np.inf], np.nan)


# --- (3) MACD-vs-price slope agreement (light divergence) ---------------


def f13mc_f13_macd_variants_macdpx_agree_12_26_10d_base_v060_signal(close):
    """sign(MACD.diff(10)) * sign(close.diff(10)) — +1 agree, -1 disagree."""
    m = _ema(close, 12) - _ema(close, 26)
    ms = np.sign(m.diff(10))
    ps = np.sign(close.diff(10))
    return (ms * ps).where(~ms.isna() & ~ps.isna()).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_macdpx_disag_19_39_30d_base_v061_signal(closeadj):
    """Count of MACD-vs-price slope DISAGREEMENT events in trailing 30 bars."""
    m = _ema(closeadj, 19) - _ema(closeadj, 39)
    ms = np.sign(m.diff(21))
    ps = np.sign(closeadj.diff(21))
    dis = (ms * ps < 0.0).astype(float).where(~ms.isna() & ~ps.isna())
    return dis.rolling(30, min_periods=30).sum().replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_macdvspx_diff_50_200_base_v062_signal(closeadj):
    """MACD(50,200) z(60) - close z(60) — divergence-flavored differential."""
    m = _ema(closeadj, 50) - _ema(closeadj, 200)
    mz = (m - m.rolling(60, min_periods=30).mean()) / m.rolling(60, min_periods=30).std().replace(0.0, np.nan)
    cz = (closeadj - closeadj.rolling(60, min_periods=30).mean()) / closeadj.rolling(60, min_periods=30).std().replace(0.0, np.nan)
    return (mz - cz).replace([np.inf, -np.inf], np.nan)


# --- (3) MACD anti-momentum / acceleration ------------------------------


def f13mc_f13_macd_variants_histaccelsign_12_26_9_base_v063_signal(close):
    """sign(hist_slope_3) - sign(hist_slope_3.shift(5)) — discrete histogram-slope-sign
    transition (in {-2,-1,0,1,2}). Structurally different from raw histogram curvature."""
    m = _ema(close, 12) - _ema(close, 26)
    h = m - _ema(m, 9)
    ss = np.sign(h.diff(3))
    out = ss - ss.shift(5)
    return out.where(~ss.isna() & ~ss.shift(5).isna()).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_triplecross_12_26_9_30d_base_v064_signal(close):
    """Histogram-flip count in last 30 bars — anti-momentum measure."""
    m = _ema(close, 12) - _ema(close, 26)
    h = m - _ema(m, 9)
    s = np.sign(h)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(30, min_periods=30).sum().replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_histslopechange_19_39_13_base_v065_signal(closeadj):
    """sign(diff(h_slow,5)) - sign(diff(h_slow,5).shift(5)) — slope-sign change of slow hist."""
    m = _ema(closeadj, 19) - _ema(closeadj, 39)
    h = m - _ema(m, 13)
    sl = np.sign(h.diff(5))
    return (sl - sl.shift(5)).where(~sl.isna() & ~sl.shift(5).isna()).replace([np.inf, -np.inf], np.nan)


# --- (3) Ratio-style MACD features ------------------------------------


def f13mc_f13_macd_variants_histovermacd_12_26_9_base_v066_signal(close):
    """histogram / |MACD| — relative histogram vs MACD-line magnitude (12,26,9)."""
    m = _ema(close, 12) - _ema(close, 26)
    h = m - _ema(m, 9)
    return (h / m.abs().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_histoversig_12_26_9_base_v067_signal(close):
    """histogram / |signal| — histogram vs signal magnitude."""
    m = _ema(close, 12) - _ema(close, 26)
    sig = _ema(m, 9)
    h = m - sig
    return (h / sig.abs().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_signoverhist_12_26_9_base_v068_signal(close):
    """sign(signal) * (1 - tanh(|hist|/|signal|)) — bounded indicator of weak histograms
    relative to a non-zero signal; uses sign of signal to give directional context."""
    m = _ema(close, 12) - _ema(close, 26)
    sig = _ema(m, 9)
    h = m - sig
    ratio = h.abs() / sig.abs().replace(0.0, np.nan)
    return (np.sign(sig) * (1.0 - np.tanh(ratio))).replace([np.inf, -np.inf], np.nan)


# --- (3) Smoothed-MACD variants (different smoothers) -------------------


def f13mc_f13_macd_variants_macdstd_60d_base_v069_signal(closeadj):
    """Rolling std of MACD line over 60d — MACD volatility regime indicator."""
    m = _ema(closeadj, 12) - _ema(closeadj, 26)
    return m.rolling(60, min_periods=30).std().replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_medmacd_12_26_15_base_v070_signal(close):
    """Median MACD over 15 bars — robust smoother for MACD."""
    m = _ema(close, 12) - _ema(close, 26)
    return m.rolling(15, min_periods=15).median().replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_macd_vs_smaMACD_signdays_base_v071_signal(close):
    """Days-since MACD line crosses its own SMA(20) of MACD line. Capped 60. Persistence indicator."""
    m = _ema(close, 12) - _ema(close, 26)
    sma20 = m.rolling(20, min_periods=20).mean()
    s = np.sign(m - sma20)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return 60.0
        return float(len(x) - 1 - idx[-1])
    return flip.rolling(60, min_periods=20).apply(_ds, raw=True).replace([np.inf, -np.inf], np.nan)


# --- (4) MACD composite / log-ratio / spread ---------------------------


def f13mc_f13_macd_variants_macdcomposite_base_v072_signal(closeadj):
    """Composite normalized MACD across (8,21),(19,39),(50,200) configurations."""
    m1 = (_ema(closeadj, 8) - _ema(closeadj, 21)) / _ema(closeadj, 21).replace(0.0, np.nan)
    m2 = (_ema(closeadj, 19) - _ema(closeadj, 39)) / _ema(closeadj, 39).replace(0.0, np.nan)
    m3 = (_ema(closeadj, 50) - _ema(closeadj, 200)) / _ema(closeadj, 200).replace(0.0, np.nan)
    return ((m1 + m2 + m3) / 3.0).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_macdratio_log_50_200_base_v073_signal(closeadj):
    """log(EMA50 / EMA200) MINUS rolling-60d-mean of itself — drift-detrended log-ratio MACD."""
    e1 = _ema(closeadj, 50)
    e2 = _ema(closeadj, 200)
    lr = np.log(e1.replace(0.0, np.nan) / e2.replace(0.0, np.nan))
    return (lr - lr.rolling(60, min_periods=30).mean()).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_histsignconf_12_26_9_base_v074_signal(close):
    """sign(MACD-signal) AND sign(diff(hist,3))>0 — bullish-histogram-momentum-confirmation
    indicator (+1, -1, 0)."""
    m = _ema(close, 12) - _ema(close, 26)
    sig = _ema(m, 9)
    h = m - sig
    same = (np.sign(h) * np.sign(h.diff(3))).where(~h.isna() & ~h.shift(3).isna())
    return same.replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_macdbias_19_39_60d_base_v075_signal(closeadj):
    """MACD(19,39) / rolling-std(MACD,60) — bias of slow MACD line."""
    m = _ema(closeadj, 19) - _ema(closeadj, 39)
    sd = m.rolling(60, min_periods=30).std()
    return (m / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f13_macd_variants_base_001_075_REGISTRY = {
    "f13mc_f13_macd_variants_macddetrend_12_26_base_v001_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_macddetrend_12_26_base_v001_signal},
    "f13mc_f13_macd_variants_macdslowdetrend_50_200_base_v002_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_macdslowdetrend_50_200_base_v002_signal},
    "f13mc_f13_macd_variants_macd_3_10_base_v003_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_macd_3_10_base_v003_signal},
    "f13mc_f13_macd_variants_macdnorm_12_26_base_v004_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_macdnorm_12_26_base_v004_signal},
    "f13mc_f13_macd_variants_macdrank_8_21_60d_base_v005_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_macdrank_8_21_60d_base_v005_signal},
    "f13mc_f13_macd_variants_macdnorm_50_200_base_v006_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_macdnorm_50_200_base_v006_signal},
    "f13mc_f13_macd_variants_macdsignagree_5_35_19_39_base_v007_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_macdsignagree_5_35_19_39_base_v007_signal},
    "f13mc_f13_macd_variants_macdnorm_19_39_z_base_v008_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_macdnorm_19_39_z_base_v008_signal},
    "f13mc_f13_macd_variants_signal_12_26_9_base_v009_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_signal_12_26_9_base_v009_signal},
    "f13mc_f13_macd_variants_signalnorm_19_39_13_base_v010_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_signalnorm_19_39_13_base_v010_signal},
    "f13mc_f13_macd_variants_hist_12_26_9_base_v011_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_hist_12_26_9_base_v011_signal},
    "f13mc_f13_macd_variants_hist_8_21_5_base_v012_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_hist_8_21_5_base_v012_signal},
    "f13mc_f13_macd_variants_hist_50_200_30_base_v013_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_hist_50_200_30_base_v013_signal},
    "f13mc_f13_macd_variants_histdetrend_12_26_9_base_v014_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_histdetrend_12_26_9_base_v014_signal},
    "f13mc_f13_macd_variants_histabs_12_26_9_base_v015_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_histabs_12_26_9_base_v015_signal},
    "f13mc_f13_macd_variants_signxsig_12_26_9_base_v016_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_signxsig_12_26_9_base_v016_signal},
    "f13mc_f13_macd_variants_signxzero_12_26_base_v017_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_signxzero_12_26_base_v017_signal},
    "f13mc_f13_macd_variants_signxzero_50_200_base_v018_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_signxzero_50_200_base_v018_signal},
    "f13mc_f13_macd_variants_bullstate_12_26_9_base_v019_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_bullstate_12_26_9_base_v019_signal},
    "f13mc_f13_macd_variants_quaddays_12_26_9_base_v020_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_quaddays_12_26_9_base_v020_signal},
    "f13mc_f13_macd_variants_histslopesign_12_26_9_base_v021_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_histslopesign_12_26_9_base_v021_signal},
    "f13mc_f13_macd_variants_dayssincex_12_26_9_base_v022_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_dayssincex_12_26_9_base_v022_signal},
    "f13mc_f13_macd_variants_dayssincez_19_39_base_v023_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_dayssincez_19_39_base_v023_signal},
    "f13mc_f13_macd_variants_streakabove_12_26_9_base_v024_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_streakabove_12_26_9_base_v024_signal},
    "f13mc_f13_macd_variants_streakabovez_50_200_base_v025_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_streakabovez_50_200_base_v025_signal},
    "f13mc_f13_macd_variants_xcount_12_26_9_60d_base_v026_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_xcount_12_26_9_60d_base_v026_signal},
    "f13mc_f13_macd_variants_xcountz_19_39_120d_base_v027_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_xcountz_19_39_120d_base_v027_signal},
    "f13mc_f13_macd_variants_histrank_12_26_9_60d_base_v028_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_histrank_12_26_9_60d_base_v028_signal},
    "f13mc_f13_macd_variants_histratio_to_macdabs_60d_base_v029_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_histratio_to_macdabs_60d_base_v029_signal},
    "f13mc_f13_macd_variants_histskew_12_26_9_60d_base_v030_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_histskew_12_26_9_60d_base_v030_signal},
    "f13mc_f13_macd_variants_histkurt_12_26_9_80d_base_v031_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_histkurt_12_26_9_80d_base_v031_signal},
    "f13mc_f13_macd_variants_histrank_19_39_13_120d_base_v032_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_histrank_19_39_13_120d_base_v032_signal},
    "f13mc_f13_macd_variants_macdrank_12_26_120d_base_v033_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_macdrank_12_26_120d_base_v033_signal},
    "f13mc_f13_macd_variants_macdz_12_26_60d_base_v034_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_macdz_12_26_60d_base_v034_signal},
    "f13mc_f13_macd_variants_macdbandbreaks_12_26_60d_base_v035_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_macdbandbreaks_12_26_60d_base_v035_signal},
    "f13mc_f13_macd_variants_macdrank_50_200_252d_base_v036_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_macdrank_50_200_252d_base_v036_signal},
    "f13mc_f13_macd_variants_macdvszero_dist_12_26_60d_base_v037_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_macdvszero_dist_12_26_60d_base_v037_signal},
    "f13mc_f13_macd_variants_tanhmacdz_19_39_60d_base_v038_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_tanhmacdz_19_39_60d_base_v038_signal},
    "f13mc_f13_macd_variants_tanhhist_8_21_5_base_v039_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_tanhhist_8_21_5_base_v039_signal},
    "f13mc_f13_macd_variants_signhist_50_200_30_base_v040_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_signhist_50_200_30_base_v040_signal},
    "f13mc_f13_macd_variants_macdslopenorm_12_26_base_v041_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_macdslopenorm_12_26_base_v041_signal},
    "f13mc_f13_macd_variants_histslope5_12_26_9_base_v042_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_histslope5_12_26_9_base_v042_signal},
    "f13mc_f13_macd_variants_macdcurv_50_200_base_v043_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_macdcurv_50_200_base_v043_signal},
    "f13mc_f13_macd_variants_histcurv_12_26_9_base_v044_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_histcurv_12_26_9_base_v044_signal},
    "f13mc_f13_macd_variants_hma_macd_12_26_base_v045_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_hma_macd_12_26_base_v045_signal},
    "f13mc_f13_macd_variants_dema_macd_12_26_base_v046_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_dema_macd_12_26_base_v046_signal},
    "f13mc_f13_macd_variants_zlemaMACD_histsign_12_26_5_base_v047_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_zlemaMACD_histsign_12_26_5_base_v047_signal},
    "f13mc_f13_macd_variants_wilderhist_12_26_9_base_v048_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_wilderhist_12_26_9_base_v048_signal},
    "f13mc_f13_macd_variants_wma_macd_12_26_base_v049_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_wma_macd_12_26_base_v049_signal},
    "f13mc_f13_macd_variants_macdkerdiff_hma_base_v050_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_macdkerdiff_hma_base_v050_signal},
    "f13mc_f13_macd_variants_macdkerdiff_dema_base_v051_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_macdkerdiff_dema_base_v051_signal},
    "f13mc_f13_macd_variants_macdkerdiff_zlema_hma_base_v052_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_macdkerdiff_zlema_hma_base_v052_signal},
    "f13mc_f13_macd_variants_macdkerdiff_wilder_base_v053_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_macdkerdiff_wilder_base_v053_signal},
    "f13mc_f13_macd_variants_macdsign_xor_base_v054_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_macdsign_xor_base_v054_signal},
    "f13mc_f13_macd_variants_macddiff_fastslow_base_v055_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_macddiff_fastslow_base_v055_signal},
    "f13mc_f13_macd_variants_macddiff_short_long_base_v056_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_macddiff_short_long_base_v056_signal},
    "f13mc_f13_macd_variants_macdvolconf_12_26_base_v057_signal": {"inputs": ["close", "volume"], "func": f13mc_f13_macd_variants_macdvolconf_12_26_base_v057_signal},
    "f13mc_f13_macd_variants_vwmacd_norm_12_26_base_v058_signal": {"inputs": ["close", "volume"], "func": f13mc_f13_macd_variants_vwmacd_norm_12_26_base_v058_signal},
    "f13mc_f13_macd_variants_volmacd_12_26_base_v059_signal": {"inputs": ["volume"], "func": f13mc_f13_macd_variants_volmacd_12_26_base_v059_signal},
    "f13mc_f13_macd_variants_macdpx_agree_12_26_10d_base_v060_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_macdpx_agree_12_26_10d_base_v060_signal},
    "f13mc_f13_macd_variants_macdpx_disag_19_39_30d_base_v061_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_macdpx_disag_19_39_30d_base_v061_signal},
    "f13mc_f13_macd_variants_macdvspx_diff_50_200_base_v062_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_macdvspx_diff_50_200_base_v062_signal},
    "f13mc_f13_macd_variants_histaccelsign_12_26_9_base_v063_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_histaccelsign_12_26_9_base_v063_signal},
    "f13mc_f13_macd_variants_triplecross_12_26_9_30d_base_v064_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_triplecross_12_26_9_30d_base_v064_signal},
    "f13mc_f13_macd_variants_histslopechange_19_39_13_base_v065_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_histslopechange_19_39_13_base_v065_signal},
    "f13mc_f13_macd_variants_histovermacd_12_26_9_base_v066_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_histovermacd_12_26_9_base_v066_signal},
    "f13mc_f13_macd_variants_histoversig_12_26_9_base_v067_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_histoversig_12_26_9_base_v067_signal},
    "f13mc_f13_macd_variants_signoverhist_12_26_9_base_v068_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_signoverhist_12_26_9_base_v068_signal},
    "f13mc_f13_macd_variants_macdstd_60d_base_v069_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_macdstd_60d_base_v069_signal},
    "f13mc_f13_macd_variants_medmacd_12_26_15_base_v070_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_medmacd_12_26_15_base_v070_signal},
    "f13mc_f13_macd_variants_macd_vs_smaMACD_signdays_base_v071_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_macd_vs_smaMACD_signdays_base_v071_signal},
    "f13mc_f13_macd_variants_macdcomposite_base_v072_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_macdcomposite_base_v072_signal},
    "f13mc_f13_macd_variants_macdratio_log_50_200_base_v073_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_macdratio_log_50_200_base_v073_signal},
    "f13mc_f13_macd_variants_histsignconf_12_26_9_base_v074_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_histsignconf_12_26_9_base_v074_signal},
    "f13mc_f13_macd_variants_macdbias_19_39_60d_base_v075_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_macdbias_19_39_60d_base_v075_signal},
}


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------


def _synthetic_inputs(n: int = 800, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    seg = n // 4
    rest = n - 3 * seg
    ret = np.concatenate([
        rng.normal(0.0012, 0.011, seg),
        rng.normal(-0.0005, 0.018, seg),
        rng.normal(-0.0010, 0.014, seg),
        rng.normal(0.0008, 0.012, rest),
    ])
    close = 50.0 * np.exp(np.cumsum(ret))
    adj_drift = rng.normal(0.0, 0.0003, size=n).cumsum()
    closeadj = close * np.exp(adj_drift)
    intraday = rng.normal(0.0, 0.008, size=n)
    open_ = close * np.exp(-intraday * 0.5)
    high = np.maximum(close, open_) * np.exp(np.abs(rng.normal(0.0, 0.006, size=n)))
    low = np.minimum(close, open_) * np.exp(-np.abs(rng.normal(0.0, 0.006, size=n)))
    volume = rng.lognormal(mean=13.0, sigma=0.6, size=n)
    idx = pd.RangeIndex(n)
    return pd.DataFrame({
        "open": pd.Series(open_, index=idx, dtype=float),
        "high": pd.Series(high, index=idx, dtype=float),
        "low": pd.Series(low, index=idx, dtype=float),
        "close": pd.Series(close, index=idx, dtype=float),
        "closeadj": pd.Series(closeadj, index=idx, dtype=float),
        "volume": pd.Series(volume, index=idx, dtype=float),
    })


def _self_test() -> None:
    df = _synthetic_inputs(n=800, seed=42)
    results: dict[str, pd.Series] = {}
    for name, entry in f13_macd_variants_base_001_075_REGISTRY.items():
        args = [df[col] for col in entry["inputs"]]
        out = entry["func"](*args)
        assert isinstance(out, pd.Series), f"{name}: not a Series"
        assert len(out) == len(df), f"{name}: length mismatch"
        clean = out.dropna()
        assert len(clean) > 0, f"{name}: all NaN"
        assert float(clean.std()) > 0.0 or clean.nunique() > 1, f"{name}: constant/all-zero"
        results[name] = out

    warm = 252
    coverage_ok = sum(1 for s in results.values() if s.iloc[warm:].isna().mean() < 0.5)
    frac = coverage_ok / len(results)
    assert frac >= 0.80, f"NaN-coverage too low: {frac:.2%} have <50% NaN after warm-up"

    aligned = pd.concat({n: results[n] for n in results}, axis=1).iloc[warm:]
    aligned = aligned.replace([np.inf, -np.inf], np.nan)
    corr = aligned.corr(min_periods=50).abs()
    np.fill_diagonal(corr.values, 0.0)
    max_corr = float(corr.max().max())
    if max_corr > 0.95:
        print(f"FAILING max |corr| = {max_corr:.4f}. Top pairs:")
        for i, a in enumerate(corr.columns):
            for j, b in enumerate(corr.columns):
                if j > i and corr.iloc[i, j] > 0.94:
                    print(f"  {a}  vs  {b}  ->  {corr.iloc[i, j]:.4f}")
    assert max_corr <= 0.95 + 1e-9, f"max pairwise |corr|={max_corr:.4f} exceeds 0.95"
    print(f"OK base_001_075: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
