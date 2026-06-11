"""f26_accumulation_distribution base features 001-075.

Domain: Accumulation/Distribution Line (A/D), Close Location Value (CLV =
((close-low)-(high-close))/(high-low)), Chaikin Money Flow (CMF), Chaikin
Oscillator (EMA(A/D,3)-EMA(A/D,10)), Klinger Volume Force, money flow
features (MFI), up/down accumulation, A/D ranks, bounded transforms and
distribution-detection (negative-CLV streaks). Every feature uses CLV
or A/D-line or a Chaikin variant — DISTINCT from f23 (OBV: just
sign(price-diff)*volume) and f25 (VWAP).

NaN policy: NEVER fillna(<value>); preserve NaN through warm-up; only
replace([inf,-inf], nan) at final return. Window>21 uses closeadj; <=21
uses close. OHLC features within a single bar use unadjusted open/high
/low/close.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Helpers (CLV/A-D constructors). Each feature spells its full formula inline.
# ---------------------------------------------------------------------------


def _sma(s: pd.Series, n: int) -> pd.Series:
    return s.rolling(n, min_periods=n).mean()


def _ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False, min_periods=n).mean()


def _clv(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rng = (high - low).replace(0.0, np.nan)
    return ((close - low) - (high - close)) / rng


def _adline(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rng = (high - low).replace(0.0, np.nan)
    clv = ((close - low) - (high - close)) / rng
    mfv = clv * volume
    return mfv.cumsum()


def _streak_run(x: np.ndarray) -> float:
    """Length of trailing run of >0.5 values; 0 if last value <= 0.5."""
    c = 0
    for v in x[::-1]:
        if v > 0.5:
            c += 1
        else:
            break
    return float(c)


# ---------------------------------------------------------------------------
# Features 001-075
# ---------------------------------------------------------------------------


# === Raw CLV-family (single bar window) ====================================


def f26ad_f26_accumulation_distribution_raw_clv_1d_base_v001_signal(high, low, close):
    """Raw CLV = ((close-low)-(high-close))/(high-low). Bounded [-1,+1]."""
    rng = (high - low).replace(0.0, np.nan)
    out = ((close - low) - (high - close)) / rng
    return out.replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clv_sign_1d_base_v002_signal(high, low, close):
    """sign(CLV). Discrete-bar tri-state direction of close-in-range placement."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((close - low) - (high - close)) / rng
    return np.sign(clv).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clv_mean_5d_base_v003_signal(high, low, close):
    """Mean CLV over 5d — short-window accumulation pressure."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((close - low) - (high - close)) / rng
    return clv.rolling(5, min_periods=5).mean().replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clv_mean_21d_base_v004_signal(high, low, close):
    """Mean CLV over 21d."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((close - low) - (high - close)) / rng
    return clv.rolling(21, min_periods=21).mean().replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clv_mean_63d_base_v005_signal(high, low, closeadj):
    """Mean CLV over 63d — quarter-window accumulation pressure (closeadj for >21d window)."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    return clv.rolling(63, min_periods=63).mean().replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clv_volratio_5d_base_v006_signal(high, low, close, volume):
    """Sum(CLV*vol,5)/Sum(vol,5) — short-window CMF analog."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((close - low) - (high - close)) / rng
    num = (clv * volume).rolling(5, min_periods=5).sum()
    den = volume.rolling(5, min_periods=5).sum().replace(0.0, np.nan)
    return (num / den).replace([np.inf, -np.inf], np.nan)


# === CMF at multiple windows (volume-weighted CLV) =========================


def f26ad_f26_accumulation_distribution_cmf_21d_base_v007_signal(high, low, close, volume):
    """Chaikin Money Flow at 21d: sum(CLV*vol,21)/sum(vol,21). Bounded."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((close - low) - (high - close)) / rng
    num = (clv * volume).rolling(21, min_periods=21).sum()
    den = volume.rolling(21, min_periods=21).sum().replace(0.0, np.nan)
    return (num / den).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_cmf_50d_base_v008_signal(high, low, closeadj, volume):
    """CMF at 50d (closeadj for >21d window)."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    num = (clv * volume).rolling(50, min_periods=50).sum()
    den = volume.rolling(50, min_periods=50).sum().replace(0.0, np.nan)
    return (num / den).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_cmf_100d_base_v009_signal(high, low, closeadj, volume):
    """CMF at 100d — long-horizon volume-weighted accumulation pressure."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    num = (clv * volume).rolling(100, min_periods=100).sum()
    den = volume.rolling(100, min_periods=100).sum().replace(0.0, np.nan)
    return (num / den).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_cmf_sign_21d_base_v010_signal(high, low, close, volume):
    """sign(CMF_21). Discrete +/- accumulation indicator."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((close - low) - (high - close)) / rng
    num = (clv * volume).rolling(21, min_periods=21).sum()
    den = volume.rolling(21, min_periods=21).sum().replace(0.0, np.nan)
    cmf = num / den
    return np.sign(cmf).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_cmf50_minus_cmf21_sign_base_v011_signal(high, low, closeadj, volume):
    """sign(CMF_50 - CMF_21). Discrete short-vs-long CMF crossover state.
    Drift-stable on closeadj (cross-window differential cancels base drift)."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    cv = clv * volume
    n1 = cv.rolling(21, min_periods=21).sum()
    d1 = volume.rolling(21, min_periods=21).sum().replace(0.0, np.nan)
    n2 = cv.rolling(50, min_periods=50).sum()
    d2 = volume.rolling(50, min_periods=50).sum().replace(0.0, np.nan)
    return np.sign((n2 / d2) - (n1 / d1)).replace([np.inf, -np.inf], np.nan)


# === A/D line distance/slope features ======================================


def f26ad_f26_accumulation_distribution_ad_minus_sma_30d_base_v012_signal(high, low, closeadj, volume):
    """(A/D - SMA(A/D,30))/abs(SMA(A/D,30)) — normalised distance vs trend."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    sma = ad.rolling(30, min_periods=30).mean()
    return ((ad - sma) / sma.abs().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_ad_minus_sma_120d_base_v013_signal(high, low, closeadj, volume):
    """(A/D - SMA(A/D,120))/abs(SMA(A/D,120))."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    sma = ad.rolling(120, min_periods=120).mean()
    return ((ad - sma) / sma.abs().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_ad_slope_norm_30d_base_v014_signal(high, low, closeadj, volume):
    """(A/D - A/D.shift(30)) / sum(volume,30) — normalised net accumulation."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    return ((ad - ad.shift(30)) / volume.rolling(30, min_periods=30).sum().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_ad_path_curvature_120d_base_v015_signal(high, low, closeadj, volume):
    """log(|A/D - A/D.shift(120)|) - log(sum |CLV*vol|, 120). Compressed long-horizon
    flow magnitude ratio; structurally distinct from raw CMF_100 (uses abs in numerator)."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    cv = clv * volume
    ad = cv.cumsum()
    net = (ad - ad.shift(120)).abs()
    path = cv.abs().rolling(120, min_periods=120).sum().replace(0.0, np.nan)
    return (np.log(net.replace(0.0, np.nan)) - np.log(path)).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_ad_curv_50d_base_v016_signal(high, low, closeadj, volume):
    """A/D curvature: A/D - 2*A/D.shift(25)+A/D.shift(50), normalised by sum vol."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    den = volume.rolling(50, min_periods=50).sum().replace(0.0, np.nan)
    return ((ad - 2.0 * ad.shift(25) + ad.shift(50)) / den).replace([np.inf, -np.inf], np.nan)


# === Chaikin Oscillator (EMA(A/D,3) - EMA(A/D,10)) =========================


def f26ad_f26_accumulation_distribution_chaikin_osc_3_10_base_v017_signal(high, low, closeadj, volume):
    """Chaikin Oscillator: EMA(A/D,3) - EMA(A/D,10), normalised by sum vol over 10d."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    e3 = ad.ewm(span=3, adjust=False, min_periods=3).mean()
    e10 = ad.ewm(span=10, adjust=False, min_periods=10).mean()
    den = volume.rolling(10, min_periods=10).sum().replace(0.0, np.nan)
    return ((e3 - e10) / den).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_chaikin_pct_change_10d_base_v018_signal(high, low, closeadj, volume):
    """Pct change of Chaikin Oscillator 3-10 over 10d, sign-preserving via signed-log.
    Direction-of-momentum of Chaikin, less dependent on level."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    e3 = ad.ewm(span=3, adjust=False, min_periods=3).mean()
    e10 = ad.ewm(span=10, adjust=False, min_periods=10).mean()
    co = e3 - e10
    prev = co.shift(10)
    return (np.sign(co - prev) * np.log1p((co - prev).abs() / (prev.abs() + 1.0))).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_chaikin_osc_sign_3_10_base_v019_signal(high, low, closeadj, volume):
    """sign(Chaikin Osc 3-10) — zero-line state of Chaikin Oscillator."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    e3 = ad.ewm(span=3, adjust=False, min_periods=3).mean()
    e10 = ad.ewm(span=10, adjust=False, min_periods=10).mean()
    return np.sign(e3 - e10).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_chaikin_zero_streak_60d_base_v020_signal(high, low, closeadj, volume):
    """Days since Chaikin Osc crossed zero, capped 60d. Distribution/accumulation regime length."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    e3 = ad.ewm(span=3, adjust=False, min_periods=3).mean()
    e10 = ad.ewm(span=10, adjust=False, min_periods=10).mean()
    s = np.sign(e3 - e10)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(60, min_periods=60).apply(_streak_run, raw=True).replace([np.inf, -np.inf], np.nan)


# === Klinger Volume Force ===================================================


def f26ad_f26_accumulation_distribution_klinger_osc_34_55_base_v021_signal(high, low, closeadj, volume):
    """Klinger Volume Force oscillator: EMA(KVF,34)-EMA(KVF,55) normalised.
    KVF = volume * sign(trend) where trend = (high+low+close) - prior(high+low+close)."""
    hlc = high + low + closeadj
    trend = np.sign(hlc - hlc.shift(1))
    kvf = volume * trend
    e34 = kvf.ewm(span=34, adjust=False, min_periods=34).mean()
    e55 = kvf.ewm(span=55, adjust=False, min_periods=55).mean()
    den = volume.rolling(55, min_periods=55).mean().replace(0.0, np.nan)
    return ((e34 - e55) / den).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_klinger_sign_34_55_base_v022_signal(high, low, closeadj, volume):
    """sign(Klinger Osc) — Klinger zero-line state."""
    hlc = high + low + closeadj
    trend = np.sign(hlc - hlc.shift(1))
    kvf = volume * trend
    e34 = kvf.ewm(span=34, adjust=False, min_periods=34).mean()
    e55 = kvf.ewm(span=55, adjust=False, min_periods=55).mean()
    return np.sign(e34 - e55).replace([np.inf, -np.inf], np.nan)


# === Up vs Down Accumulation (CLV>0 vs CLV<0 partitioning) =================


def f26ad_f26_accumulation_distribution_upclv_volsum_21d_base_v023_signal(high, low, close, volume):
    """Sum of (CLV*volume) on CLV>0 days over 21d, normalised by sum vol(21d)."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((close - low) - (high - close)) / rng
    pos = (clv * volume).where(clv > 0.0, 0.0)
    den = volume.rolling(21, min_periods=21).sum().replace(0.0, np.nan)
    return (pos.rolling(21, min_periods=21).sum() / den).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_downclv_volshare_50d_base_v024_signal(high, low, closeadj, volume):
    """sum(vol where CLV<0, 50) / sum(vol, 50). Volume share on distribution days only.
    Structurally distinct from CMF (volume only, no CLV multiplication)."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    neg_vol = volume.where(clv < 0.0, 0.0)
    den = volume.rolling(50, min_periods=50).sum().replace(0.0, np.nan)
    return (neg_vol.rolling(50, min_periods=50).sum() / den).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_upclv_downclv_ratio_30d_base_v025_signal(high, low, closeadj, volume):
    """log(sum_pos_CLVvol / |sum_neg_CLVvol|) over 30d. Accumulation/distribution log-ratio."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    cv = clv * volume
    pos = cv.where(cv > 0.0, 0.0).rolling(30, min_periods=30).sum()
    neg = (-cv.where(cv < 0.0, 0.0)).rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    return np.log(pos.replace(0.0, np.nan) / neg).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_count_clvpos_30d_base_v026_signal(high, low, closeadj):
    """Count of CLV>0 days in 30d window — discrete accumulation tally."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    pos = (clv > 0.0).astype(float).where(~clv.isna())
    return pos.rolling(30, min_periods=30).sum().replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_count_clvneg_75d_base_v027_signal(high, low, closeadj):
    """Count of CLV<0 days in 75d window — distribution tally."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    neg = (clv < 0.0).astype(float).where(~clv.isna())
    return neg.rolling(75, min_periods=75).sum().replace([np.inf, -np.inf], np.nan)


# === Distribution-detection: streaks and threshold counts ==================


def f26ad_f26_accumulation_distribution_clvneg_streak_40d_base_v028_signal(high, low, closeadj):
    """Length of trailing run of CLV<0 days (capped 40d). Distribution streak (closeadj for >21d window)."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    neg = (clv < 0.0).astype(float).where(~clv.isna())
    return neg.rolling(40, min_periods=40).apply(_streak_run, raw=True).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clvpos_streak_40d_base_v029_signal(high, low, closeadj):
    """Length of trailing run of CLV>0 days (capped 40d). Accumulation streak."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    pos = (clv > 0.0).astype(float).where(~clv.isna())
    return pos.rolling(40, min_periods=40).apply(_streak_run, raw=True).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_high_dist_days_50d_base_v030_signal(high, low, closeadj, volume):
    """Fraction of last 50d with CMF_21<-0.05 (distribution flag). Bounded [0,1]."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    num = (clv * volume).rolling(21, min_periods=21).sum()
    den = volume.rolling(21, min_periods=21).sum().replace(0.0, np.nan)
    cmf = num / den
    flag = (cmf < -0.05).astype(float).where(~cmf.isna())
    return flag.rolling(50, min_periods=50).mean().replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_high_acc_days_50d_base_v031_signal(high, low, closeadj, volume):
    """Fraction of last 50d with CMF_21>+0.05 (accumulation flag). Bounded [0,1]."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    num = (clv * volume).rolling(21, min_periods=21).sum()
    den = volume.rolling(21, min_periods=21).sum().replace(0.0, np.nan)
    cmf = num / den
    flag = (cmf > 0.05).astype(float).where(~cmf.isna())
    return flag.rolling(50, min_periods=50).mean().replace([np.inf, -np.inf], np.nan)


# === CMF z-score / rank / slope (bounded transforms) =======================


def f26ad_f26_accumulation_distribution_cmf21_zscore_120d_base_v032_signal(high, low, closeadj, volume):
    """Z-score of CMF_21 over 120d. Removes regime drift."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    num = (clv * volume).rolling(21, min_periods=21).sum()
    den = volume.rolling(21, min_periods=21).sum().replace(0.0, np.nan)
    cmf = num / den
    mu = cmf.rolling(120, min_periods=120).mean()
    sd = cmf.rolling(120, min_periods=120).std(ddof=0).replace(0.0, np.nan)
    return ((cmf - mu) / sd).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_cmf50_rank_180d_base_v033_signal(high, low, closeadj, volume):
    """Percentile rank of CMF_50 within rolling 180d."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    num = (clv * volume).rolling(50, min_periods=50).sum()
    den = volume.rolling(50, min_periods=50).sum().replace(0.0, np.nan)
    cmf = num / den
    def _rank_last(x):
        last = x[-1]
        if not np.isfinite(last):
            return np.nan
        return float((x < last).sum()) / float(len(x))
    return cmf.rolling(180, min_periods=180).apply(_rank_last, raw=True).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_cmf21_slope_10d_base_v034_signal(high, low, close, volume):
    """CMF_21 - CMF_21.shift(10). Direction-of-CMF, removes level."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((close - low) - (high - close)) / rng
    num = (clv * volume).rolling(21, min_periods=21).sum()
    den = volume.rolling(21, min_periods=21).sum().replace(0.0, np.nan)
    cmf = num / den
    return (cmf - cmf.shift(10)).replace([np.inf, -np.inf], np.nan)


# === Bounded transforms (arctan, tanh, sigmoid) ============================


def f26ad_f26_accumulation_distribution_arctan_cmf21_base_v035_signal(high, low, closeadj, volume):
    """arctan(3*CMF_21). Smooth bounded compressor of CMF."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    num = (clv * volume).rolling(21, min_periods=21).sum()
    den = volume.rolling(21, min_periods=21).sum().replace(0.0, np.nan)
    cmf = num / den
    return np.arctan(3.0 * cmf).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_tanh_ad_zscore_60d_base_v036_signal(high, low, closeadj, volume):
    """tanh of z-score of A/D - SMA(A/D,60) over 60d."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    dev = ad - ad.rolling(60, min_periods=60).mean()
    sd = dev.rolling(60, min_periods=60).std(ddof=0).replace(0.0, np.nan)
    return np.tanh((dev / sd)).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_sigmoid_chaikin_3_10_base_v037_signal(high, low, closeadj, volume):
    """sigmoid(Chaikin Osc / sigma) — bounded smoothed Chaikin."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    e3 = ad.ewm(span=3, adjust=False, min_periods=3).mean()
    e10 = ad.ewm(span=10, adjust=False, min_periods=10).mean()
    co = e3 - e10
    sd = co.rolling(60, min_periods=60).std(ddof=0).replace(0.0, np.nan)
    z = co / sd
    return (1.0 / (1.0 + np.exp(-z))).replace([np.inf, -np.inf], np.nan)


# === A/D vs OBV (compare two distinct signed-volume measures) ==============


def f26ad_f26_accumulation_distribution_ad_obv_corr_60d_base_v038_signal(high, low, closeadj, volume):
    """Rolling 60d corr of A/D-line vs OBV. Compares CLV-signed-vol vs sign(close-diff)-signed-vol."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    obv = (np.sign(closeadj.diff(1)) * volume).cumsum()
    return ad.rolling(60, min_periods=60).corr(obv).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_ad_obv_diff_norm_30d_base_v039_signal(high, low, closeadj, volume):
    """(A/D - OBV) / sum(volume,30) — divergence between A/D and OBV, normalised."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    obv = (np.sign(closeadj.diff(1)) * volume).cumsum()
    den = volume.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    return ((ad - obv) / den).replace([np.inf, -np.inf], np.nan)


# === A/D rank / percentile features ========================================


def f26ad_f26_accumulation_distribution_ad_zscore_60d_base_v040_signal(high, low, closeadj, volume):
    """Z-score of A/D level over 60d."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    mu = ad.rolling(60, min_periods=60).mean()
    sd = ad.rolling(60, min_periods=60).std(ddof=0).replace(0.0, np.nan)
    return ((ad - mu) / sd).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_ad_rank_200d_base_v041_signal(high, low, closeadj, volume):
    """Percentile rank of A/D within rolling 200d window."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    def _rank_last(x):
        last = x[-1]
        if not np.isfinite(last):
            return np.nan
        return float((x < last).sum()) / float(len(x))
    return ad.rolling(200, min_periods=200).apply(_rank_last, raw=True).replace([np.inf, -np.inf], np.nan)


# === Money Flow Index (RSI on typical_price * volume) ======================


def f26ad_f26_accumulation_distribution_mfi_14d_base_v042_signal(high, low, close, volume):
    """MFI_14 normalised to [-1,+1] (= 2*MFI/100 - 1). RSI-style on typical_price*volume."""
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    direction = np.sign(tp.diff(1))
    pos = rmf.where(direction > 0.0, 0.0)
    neg = rmf.where(direction < 0.0, 0.0)
    pf = pos.rolling(14, min_periods=14).sum()
    nf = neg.rolling(14, min_periods=14).sum().replace(0.0, np.nan)
    mr = pf / nf
    mfi = 100.0 - 100.0 / (1.0 + mr)
    return (2.0 * mfi / 100.0 - 1.0).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_mfi_28d_base_v043_signal(high, low, closeadj, volume):
    """MFI_28 normalised to [-1,+1]."""
    tp = (high + low + closeadj) / 3.0
    rmf = tp * volume
    direction = np.sign(tp.diff(1))
    pos = rmf.where(direction > 0.0, 0.0)
    neg = rmf.where(direction < 0.0, 0.0)
    pf = pos.rolling(28, min_periods=28).sum()
    nf = neg.rolling(28, min_periods=28).sum().replace(0.0, np.nan)
    mr = pf / nf
    mfi = 100.0 - 100.0 / (1.0 + mr)
    return (2.0 * mfi / 100.0 - 1.0).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_mfi14_slope_10d_base_v044_signal(high, low, closeadj, volume):
    """MFI_14 minus MFI_14.shift(10). Directional change of money flow oscillator."""
    tp = (high + low + closeadj) / 3.0
    rmf = tp * volume
    direction = np.sign(tp.diff(1))
    pos = rmf.where(direction > 0.0, 0.0)
    neg = rmf.where(direction < 0.0, 0.0)
    pf = pos.rolling(14, min_periods=14).sum()
    nf = neg.rolling(14, min_periods=14).sum().replace(0.0, np.nan)
    mr = pf / nf
    mfi = 100.0 - 100.0 / (1.0 + mr)
    return (mfi - mfi.shift(10)).replace([np.inf, -np.inf], np.nan)


# === Positive Money Flow Ratio over fixed N ================================


def f26ad_f26_accumulation_distribution_pos_mf_ratio_21d_base_v045_signal(high, low, close, volume):
    """sum(pos_money_flow,21)/sum(|money_flow|,21). Bounded [0,1]."""
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    direction = np.sign(tp.diff(1))
    pos = rmf.where(direction > 0.0, 0.0)
    neg = rmf.where(direction < 0.0, 0.0)
    psum = pos.rolling(21, min_periods=21).sum()
    nsum = (-neg).rolling(21, min_periods=21).sum()
    tot = (psum + nsum).replace(0.0, np.nan)
    return (psum / tot).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_pos_mf_ratio_100d_base_v046_signal(high, low, closeadj, volume):
    """sum(pos_money_flow,100)/sum(|money_flow|,100). Long-horizon positive fraction."""
    tp = (high + low + closeadj) / 3.0
    rmf = tp * volume
    direction = np.sign(tp.diff(1))
    pos = rmf.where(direction > 0.0, 0.0)
    neg = rmf.where(direction < 0.0, 0.0)
    psum = pos.rolling(100, min_periods=100).sum()
    nsum = (-neg).rolling(100, min_periods=100).sum()
    tot = (psum + nsum).replace(0.0, np.nan)
    return (psum / tot).replace([np.inf, -np.inf], np.nan)


# === A/D vs price divergence (light: sign-agreement only) ==================


def f26ad_f26_accumulation_distribution_ad_price_divergence_30d_base_v047_signal(high, low, closeadj, volume):
    """sign(A/D.diff(30)) - sign(close.diff(30)). Disagreement flag in {-2,-1,0,1,2}."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    return (np.sign(ad.diff(30)) - np.sign(closeadj.diff(30))).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_ad_price_divergence_100d_base_v048_signal(high, low, closeadj, volume):
    """sign(A/D.diff(100)) - sign(close.diff(100)). Long-horizon divergence."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    return (np.sign(ad.diff(100)) - np.sign(closeadj.diff(100))).replace([np.inf, -np.inf], np.nan)


# === CLV * volume per bar features (money flow per bar) ====================


def f26ad_f26_accumulation_distribution_clvvol_per_bar_mean_10d_base_v049_signal(high, low, close, volume):
    """Rolling 10d mean of (CLV*volume), normalised by 10d mean volume."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((close - low) - (high - close)) / rng
    cv = clv * volume
    return (cv.rolling(10, min_periods=10).mean() / volume.rolling(10, min_periods=10).mean().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clvvol_per_bar_z_30d_base_v050_signal(high, low, closeadj, volume):
    """z-score of (CLV*volume)/mean_volume over 30d."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    cv = clv * volume
    norm = cv / volume.replace(0.0, np.nan)
    mu = norm.rolling(30, min_periods=30).mean()
    sd = norm.rolling(30, min_periods=30).std(ddof=0).replace(0.0, np.nan)
    return ((norm - mu) / sd).replace([np.inf, -np.inf], np.nan)


# === A/D vs time correlation (regression-style) ============================


def f26ad_f26_accumulation_distribution_ad_time_corr_60d_base_v051_signal(high, low, closeadj, volume):
    """Pearson corr of A/D vs time over 60d. Persistence of accumulation trend."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    t = pd.Series(np.arange(len(ad), dtype=float), index=ad.index)
    return ad.rolling(60, min_periods=60).corr(t).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_ad_time_corr_150d_base_v052_signal(high, low, closeadj, volume):
    """Pearson corr of A/D vs time over 150d. Long-horizon persistence."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    t = pd.Series(np.arange(len(ad), dtype=float), index=ad.index)
    return ad.rolling(150, min_periods=150).corr(t).replace([np.inf, -np.inf], np.nan)


# === Money Flow Volume sum over fixed windows ==============================


def f26ad_f26_accumulation_distribution_clv_entropy_30d_base_v053_signal(high, low, closeadj):
    """Entropy of CLV sign categories (pos/zero/neg) over 30d. Bounded [0, log(3)].
    Measures distributional uniformity of accumulation/distribution bars (closeadj for >21d window)."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    sgn = np.sign(clv)
    def _ent(x):
        if len(x) == 0:
            return np.nan
        x = x[np.isfinite(x)]
        if len(x) == 0:
            return np.nan
        p_pos = float((x > 0.5).sum()) / len(x)
        p_neg = float((x < -0.5).sum()) / len(x)
        p_zero = max(0.0, 1.0 - p_pos - p_neg)
        e = 0.0
        for p in (p_pos, p_neg, p_zero):
            if p > 0.0:
                e -= p * np.log(p)
        return float(e)
    return sgn.rolling(30, min_periods=30).apply(_ent, raw=True).replace([np.inf, -np.inf], np.nan)


# === Frac of CMF sign agreement across windows =============================


def f26ad_f26_accumulation_distribution_cmf_multiwin_signagree_base_v054_signal(high, low, closeadj, volume):
    """Average of sign(CMF_n) across n in {21,50,100}. Tri-state averaged. Bounded [-1,+1]."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    cv = clv * volume
    out = pd.Series(0.0, index=closeadj.index)
    mask = pd.Series(True, index=closeadj.index)
    for n in (21, 50, 100):
        num = cv.rolling(n, min_periods=n).sum()
        den = volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
        cmf = num / den
        out = out + np.sign(cmf)
        mask = mask & ~cmf.isna()
    return (out / 3.0).where(mask).replace([np.inf, -np.inf], np.nan)


# === A/D MACD-style (EMA(A/D) - EMA(A/D)) with normalisation ==============


def f26ad_f26_accumulation_distribution_chaikin_signal_xover_streak_50d_base_v055_signal(high, low, closeadj, volume):
    """Length of trailing run of (Chaikin Osc > Chaikin Osc EMA(9)) — Chaikin-signal-line streak."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    e3 = ad.ewm(span=3, adjust=False, min_periods=3).mean()
    e10 = ad.ewm(span=10, adjust=False, min_periods=10).mean()
    co = e3 - e10
    sig9 = co.ewm(span=9, adjust=False, min_periods=9).mean()
    above = (co > sig9).astype(float).where(~co.isna() & ~sig9.isna())
    return above.rolling(50, min_periods=50).apply(_streak_run, raw=True).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_chaikin_kurt_120d_base_v056_signal(high, low, closeadj, volume):
    """Excess kurtosis of Chaikin Oscillator (normalised by sum vol) over 120d.
    Captures tail-event regime in accumulation pulses."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    e3 = ad.ewm(span=3, adjust=False, min_periods=3).mean()
    e10 = ad.ewm(span=10, adjust=False, min_periods=10).mean()
    den = volume.rolling(10, min_periods=10).sum().replace(0.0, np.nan)
    co = (e3 - e10) / den
    return co.rolling(120, min_periods=120).kurt().replace([np.inf, -np.inf], np.nan)


# === Days since CLV last positive / last extreme distribution ==============


def f26ad_f26_accumulation_distribution_days_since_clv_pos_base_v057_signal(high, low, closeadj):
    """Days since CLV last >+0.5 (strong accumulation bar), capped 60d."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    flag = (clv > 0.5).astype(float).where(~clv.isna())
    return flag.rolling(60, min_periods=60).apply(lambda x: float(len(x) - 1 - (np.where(x > 0.5)[0][-1] if (x > 0.5).any() else -1)) if (x > 0.5).any() else float(len(x)), raw=True).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_days_since_clv_neg_base_v058_signal(high, low, closeadj):
    """Days since CLV last <-0.5 (strong distribution bar), capped 60d."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    flag = (clv < -0.5).astype(float).where(~clv.isna())
    return flag.rolling(60, min_periods=60).apply(lambda x: float(len(x) - 1 - (np.where(x > 0.5)[0][-1] if (x > 0.5).any() else -1)) if (x > 0.5).any() else float(len(x)), raw=True).replace([np.inf, -np.inf], np.nan)


# === CMF dispersion / variability ==========================================


def f26ad_f26_accumulation_distribution_cmf21_std_60d_base_v059_signal(high, low, closeadj, volume):
    """Rolling 60d std of CMF_21. Stability/dispersion of accumulation pressure."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    num = (clv * volume).rolling(21, min_periods=21).sum()
    den = volume.rolling(21, min_periods=21).sum().replace(0.0, np.nan)
    cmf = num / den
    return cmf.rolling(60, min_periods=60).std(ddof=0).replace([np.inf, -np.inf], np.nan)


# === Volume-weighted CLV summary statistics ================================


def f26ad_f26_accumulation_distribution_clv_volwtd_skew_50d_base_v060_signal(high, low, closeadj, volume):
    """Volume-weighted CLV skewness over 50d (3rd-moment style)."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    cv = clv * volume
    den = volume.rolling(50, min_periods=50).sum().replace(0.0, np.nan)
    mu = cv.rolling(50, min_periods=50).sum() / den
    dev = clv - mu
    m3 = (dev ** 3 * volume).rolling(50, min_periods=50).sum() / den
    m2 = (dev ** 2 * volume).rolling(50, min_periods=50).sum() / den
    sd3 = m2 ** 1.5
    return (m3 / sd3.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === CLV autocorrelation ====================================================


def f26ad_f26_accumulation_distribution_clv_ac1_30d_base_v061_signal(high, low, closeadj):
    """Autocorr(CLV, lag=1) over 30d window."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    def _ac1(x):
        if len(x) < 3:
            return np.nan
        s = pd.Series(x)
        return float(s.autocorr(lag=1)) if s.std(ddof=0) > 0 else np.nan
    return clv.rolling(30, min_periods=30).apply(_ac1, raw=True).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clv_ac5_75d_base_v062_signal(high, low, closeadj):
    """Autocorr(CLV, lag=5) over 75d window."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    def _ac5(x):
        if len(x) < 10:
            return np.nan
        s = pd.Series(x)
        return float(s.autocorr(lag=5)) if s.std(ddof=0) > 0 else np.nan
    return clv.rolling(75, min_periods=75).apply(_ac5, raw=True).replace([np.inf, -np.inf], np.nan)


# === Net accumulation in fixed window ======================================


def f26ad_f26_accumulation_distribution_clv_high_extreme_frac_45d_base_v063_signal(high, low, closeadj):
    """Fraction of last 45d with |CLV|>0.8 (extreme close-in-range events).
    Bounded [0,1]; structurally distinct from CMF (no volume-weighting, threshold-based)."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    flag = (clv.abs() > 0.8).astype(float).where(~clv.isna())
    return flag.rolling(45, min_periods=45).mean().replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clvvol_volzscore_corr_60d_base_v064_signal(high, low, closeadj, volume):
    """Rolling 60d corr of CLV and (volume - mean(volume)) / std(volume) bar-by-bar.
    Captures whether high-volume days systematically have higher/lower CLV."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    vmu = volume.rolling(60, min_periods=60).mean()
    vsd = volume.rolling(60, min_periods=60).std(ddof=0).replace(0.0, np.nan)
    vz = (volume - vmu) / vsd
    return clv.rolling(60, min_periods=60).corr(vz).replace([np.inf, -np.inf], np.nan)


# === Klinger Volume Force pure (no oscillator) =============================


def f26ad_f26_accumulation_distribution_klinger_sign_streak_45d_base_v065_signal(high, low, closeadj, volume):
    """Length of trailing run of (Klinger Osc > 0), capped 45d. Klinger regime persistence."""
    hlc = (high + low + closeadj) / 3.0
    trend = np.sign(hlc.diff(1))
    kvf = volume * trend
    e34 = kvf.ewm(span=34, adjust=False, min_periods=34).mean()
    e55 = kvf.ewm(span=55, adjust=False, min_periods=55).mean()
    above = (e34 > e55).astype(float).where(~e34.isna() & ~e55.isna())
    return above.rolling(45, min_periods=45).apply(_streak_run, raw=True).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_klinger_vf_norm_100d_base_v066_signal(high, low, closeadj, volume):
    """Rolling 100d sum of Klinger VF, normalised by sum vol(100)."""
    hlc = (high + low + closeadj) / 3.0
    trend = np.sign(hlc.diff(1))
    kvf = volume * trend
    den = volume.rolling(100, min_periods=100).sum().replace(0.0, np.nan)
    return (kvf.rolling(100, min_periods=100).sum() / den).replace([np.inf, -np.inf], np.nan)


# === MFI sign ===============================================================


def f26ad_f26_accumulation_distribution_mfi14_sign_base_v067_signal(high, low, close, volume):
    """sign(MFI_14 - 50). Discrete bullish/bearish money flow state."""
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    direction = np.sign(tp.diff(1))
    pos = rmf.where(direction > 0.0, 0.0)
    neg = rmf.where(direction < 0.0, 0.0)
    pf = pos.rolling(14, min_periods=14).sum()
    nf = neg.rolling(14, min_periods=14).sum().replace(0.0, np.nan)
    mr = pf / nf
    mfi = 100.0 - 100.0 / (1.0 + mr)
    return np.sign(mfi - 50.0).replace([np.inf, -np.inf], np.nan)


# === CMF/CLV cross-window differential ====================================


def f26ad_f26_accumulation_distribution_cmf21_minus_cmf100_base_v068_signal(high, low, closeadj, volume):
    """CMF_21 - CMF_100. Short-vs-long accumulation pressure differential."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    cv = clv * volume
    n1 = cv.rolling(21, min_periods=21).sum()
    d1 = volume.rolling(21, min_periods=21).sum().replace(0.0, np.nan)
    n2 = cv.rolling(100, min_periods=100).sum()
    d2 = volume.rolling(100, min_periods=100).sum().replace(0.0, np.nan)
    return ((n1 / d1) - (n2 / d2)).replace([np.inf, -np.inf], np.nan)


# === Chaikin Oscillator slope ===============================================


def f26ad_f26_accumulation_distribution_chaikin_3_10_slope_5d_base_v069_signal(high, low, closeadj, volume):
    """Chaikin Osc 3-10 minus Chaikin Osc.shift(5), all normalised by sum vol(10)."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    e3 = ad.ewm(span=3, adjust=False, min_periods=3).mean()
    e10 = ad.ewm(span=10, adjust=False, min_periods=10).mean()
    den = volume.rolling(10, min_periods=10).sum().replace(0.0, np.nan)
    co = (e3 - e10) / den
    return (co - co.shift(5)).replace([np.inf, -np.inf], np.nan)


# === Williams A/D variant (uses TR instead of high-low) ====================


def f26ad_f26_accumulation_distribution_williams_ad_slope_30d_base_v070_signal(high, low, closeadj, volume):
    """Williams A/D variant: signed momentum * volume, summed over 30d normalised.
    sign(close-prior_close)*max(close-low, high-close)*volume, sum/sum_vol(30)."""
    pc = closeadj.shift(1)
    up_part = (closeadj - low.combine(pc, np.minimum))
    dn_part = (closeadj - high.combine(pc, np.maximum))
    sgn = np.sign(closeadj - pc)
    wad_bar = np.where(sgn > 0.0, up_part, np.where(sgn < 0.0, dn_part, 0.0))
    wad_bar = pd.Series(wad_bar, index=closeadj.index)
    wad_vol = wad_bar * volume
    den = volume.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    return (wad_vol.rolling(30, min_periods=30).sum() / den).replace([np.inf, -np.inf], np.nan)


# === CMF kurtosis / dispersion variants ===================================


def f26ad_f26_accumulation_distribution_cmf21_kurt_120d_base_v071_signal(high, low, closeadj, volume):
    """Excess kurtosis of CMF_21 over 120d."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    num = (clv * volume).rolling(21, min_periods=21).sum()
    den = volume.rolling(21, min_periods=21).sum().replace(0.0, np.nan)
    cmf = num / den
    return cmf.rolling(120, min_periods=120).kurt().replace([np.inf, -np.inf], np.nan)


# === MFI - 50 difference (bounded oscillator centred at 0) ================


def f26ad_f26_accumulation_distribution_mfi_overbought_frac_60d_base_v072_signal(high, low, closeadj, volume):
    """Fraction of 60d where MFI_14 > 70 (overbought money flow). Bounded [0,1]."""
    tp = (high + low + closeadj) / 3.0
    rmf = tp * volume
    direction = np.sign(tp.diff(1))
    pos = rmf.where(direction > 0.0, 0.0)
    neg = rmf.where(direction < 0.0, 0.0)
    pf = pos.rolling(14, min_periods=14).sum()
    nf = neg.rolling(14, min_periods=14).sum().replace(0.0, np.nan)
    mr = pf / nf
    mfi = 100.0 - 100.0 / (1.0 + mr)
    flag = (mfi > 70.0).astype(float).where(~mfi.isna())
    return flag.rolling(60, min_periods=60).mean().replace([np.inf, -np.inf], np.nan)


# === Crossover counts for Chaikin Oscillator ==============================


def f26ad_f26_accumulation_distribution_chaikin_zero_xover_count_120d_base_v073_signal(high, low, closeadj, volume):
    """Count of Chaikin Osc zero-line crossovers in 120d window."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    e3 = ad.ewm(span=3, adjust=False, min_periods=3).mean()
    e10 = ad.ewm(span=10, adjust=False, min_periods=10).mean()
    s = np.sign(e3 - e10)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(120, min_periods=120).sum().replace([np.inf, -np.inf], np.nan)


# === Volume-weighted CLV mean as deviation =================================


def f26ad_f26_accumulation_distribution_clv_volwtd_mean_minus_simple_30d_base_v074_signal(high, low, closeadj, volume):
    """Volume-weighted CLV mean minus simple CLV mean over 30d.
    Detects whether high-volume bars systematically accumulate or distribute."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    den = volume.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    vw = (clv * volume).rolling(30, min_periods=30).sum() / den
    sw = clv.rolling(30, min_periods=30).mean()
    return (vw - sw).replace([np.inf, -np.inf], np.nan)


# === CMF percentile difference (short vs long) ============================


def f26ad_f26_accumulation_distribution_cmf21_rank_minus_cmf50_rank_180d_base_v075_signal(high, low, closeadj, volume):
    """rank(CMF_21,180) - rank(CMF_50,180). Cross-window CMF percentile differential."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    cv = clv * volume
    n1 = cv.rolling(21, min_periods=21).sum()
    d1 = volume.rolling(21, min_periods=21).sum().replace(0.0, np.nan)
    cmf1 = n1 / d1
    n2 = cv.rolling(50, min_periods=50).sum()
    d2 = volume.rolling(50, min_periods=50).sum().replace(0.0, np.nan)
    cmf2 = n2 / d2
    def _rank_last(x):
        last = x[-1]
        if not np.isfinite(last):
            return np.nan
        return float((x < last).sum()) / float(len(x))
    r1 = cmf1.rolling(180, min_periods=180).apply(_rank_last, raw=True)
    r2 = cmf2.rolling(180, min_periods=180).apply(_rank_last, raw=True)
    return (r1 - r2).replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f26_accumulation_distribution_base_001_075_REGISTRY = {
    "f26ad_f26_accumulation_distribution_raw_clv_1d_base_v001_signal": {"inputs": ["high", "low", "close"], "func": f26ad_f26_accumulation_distribution_raw_clv_1d_base_v001_signal},
    "f26ad_f26_accumulation_distribution_clv_sign_1d_base_v002_signal": {"inputs": ["high", "low", "close"], "func": f26ad_f26_accumulation_distribution_clv_sign_1d_base_v002_signal},
    "f26ad_f26_accumulation_distribution_clv_mean_5d_base_v003_signal": {"inputs": ["high", "low", "close"], "func": f26ad_f26_accumulation_distribution_clv_mean_5d_base_v003_signal},
    "f26ad_f26_accumulation_distribution_clv_mean_21d_base_v004_signal": {"inputs": ["high", "low", "close"], "func": f26ad_f26_accumulation_distribution_clv_mean_21d_base_v004_signal},
    "f26ad_f26_accumulation_distribution_clv_mean_63d_base_v005_signal": {"inputs": ["high", "low", "closeadj"], "func": f26ad_f26_accumulation_distribution_clv_mean_63d_base_v005_signal},
    "f26ad_f26_accumulation_distribution_clv_volratio_5d_base_v006_signal": {"inputs": ["high", "low", "close", "volume"], "func": f26ad_f26_accumulation_distribution_clv_volratio_5d_base_v006_signal},
    "f26ad_f26_accumulation_distribution_cmf_21d_base_v007_signal": {"inputs": ["high", "low", "close", "volume"], "func": f26ad_f26_accumulation_distribution_cmf_21d_base_v007_signal},
    "f26ad_f26_accumulation_distribution_cmf_50d_base_v008_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_cmf_50d_base_v008_signal},
    "f26ad_f26_accumulation_distribution_cmf_100d_base_v009_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_cmf_100d_base_v009_signal},
    "f26ad_f26_accumulation_distribution_cmf_sign_21d_base_v010_signal": {"inputs": ["high", "low", "close", "volume"], "func": f26ad_f26_accumulation_distribution_cmf_sign_21d_base_v010_signal},
    "f26ad_f26_accumulation_distribution_cmf50_minus_cmf21_sign_base_v011_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_cmf50_minus_cmf21_sign_base_v011_signal},
    "f26ad_f26_accumulation_distribution_ad_minus_sma_30d_base_v012_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_ad_minus_sma_30d_base_v012_signal},
    "f26ad_f26_accumulation_distribution_ad_minus_sma_120d_base_v013_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_ad_minus_sma_120d_base_v013_signal},
    "f26ad_f26_accumulation_distribution_ad_slope_norm_30d_base_v014_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_ad_slope_norm_30d_base_v014_signal},
    "f26ad_f26_accumulation_distribution_ad_path_curvature_120d_base_v015_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_ad_path_curvature_120d_base_v015_signal},
    "f26ad_f26_accumulation_distribution_ad_curv_50d_base_v016_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_ad_curv_50d_base_v016_signal},
    "f26ad_f26_accumulation_distribution_chaikin_osc_3_10_base_v017_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_chaikin_osc_3_10_base_v017_signal},
    "f26ad_f26_accumulation_distribution_chaikin_pct_change_10d_base_v018_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_chaikin_pct_change_10d_base_v018_signal},
    "f26ad_f26_accumulation_distribution_chaikin_osc_sign_3_10_base_v019_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_chaikin_osc_sign_3_10_base_v019_signal},
    "f26ad_f26_accumulation_distribution_chaikin_zero_streak_60d_base_v020_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_chaikin_zero_streak_60d_base_v020_signal},
    "f26ad_f26_accumulation_distribution_klinger_osc_34_55_base_v021_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_klinger_osc_34_55_base_v021_signal},
    "f26ad_f26_accumulation_distribution_klinger_sign_34_55_base_v022_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_klinger_sign_34_55_base_v022_signal},
    "f26ad_f26_accumulation_distribution_upclv_volsum_21d_base_v023_signal": {"inputs": ["high", "low", "close", "volume"], "func": f26ad_f26_accumulation_distribution_upclv_volsum_21d_base_v023_signal},
    "f26ad_f26_accumulation_distribution_downclv_volshare_50d_base_v024_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_downclv_volshare_50d_base_v024_signal},
    "f26ad_f26_accumulation_distribution_upclv_downclv_ratio_30d_base_v025_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_upclv_downclv_ratio_30d_base_v025_signal},
    "f26ad_f26_accumulation_distribution_count_clvpos_30d_base_v026_signal": {"inputs": ["high", "low", "closeadj"], "func": f26ad_f26_accumulation_distribution_count_clvpos_30d_base_v026_signal},
    "f26ad_f26_accumulation_distribution_count_clvneg_75d_base_v027_signal": {"inputs": ["high", "low", "closeadj"], "func": f26ad_f26_accumulation_distribution_count_clvneg_75d_base_v027_signal},
    "f26ad_f26_accumulation_distribution_clvneg_streak_40d_base_v028_signal": {"inputs": ["high", "low", "closeadj"], "func": f26ad_f26_accumulation_distribution_clvneg_streak_40d_base_v028_signal},
    "f26ad_f26_accumulation_distribution_clvpos_streak_40d_base_v029_signal": {"inputs": ["high", "low", "closeadj"], "func": f26ad_f26_accumulation_distribution_clvpos_streak_40d_base_v029_signal},
    "f26ad_f26_accumulation_distribution_high_dist_days_50d_base_v030_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_high_dist_days_50d_base_v030_signal},
    "f26ad_f26_accumulation_distribution_high_acc_days_50d_base_v031_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_high_acc_days_50d_base_v031_signal},
    "f26ad_f26_accumulation_distribution_cmf21_zscore_120d_base_v032_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_cmf21_zscore_120d_base_v032_signal},
    "f26ad_f26_accumulation_distribution_cmf50_rank_180d_base_v033_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_cmf50_rank_180d_base_v033_signal},
    "f26ad_f26_accumulation_distribution_cmf21_slope_10d_base_v034_signal": {"inputs": ["high", "low", "close", "volume"], "func": f26ad_f26_accumulation_distribution_cmf21_slope_10d_base_v034_signal},
    "f26ad_f26_accumulation_distribution_arctan_cmf21_base_v035_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_arctan_cmf21_base_v035_signal},
    "f26ad_f26_accumulation_distribution_tanh_ad_zscore_60d_base_v036_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_tanh_ad_zscore_60d_base_v036_signal},
    "f26ad_f26_accumulation_distribution_sigmoid_chaikin_3_10_base_v037_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_sigmoid_chaikin_3_10_base_v037_signal},
    "f26ad_f26_accumulation_distribution_ad_obv_corr_60d_base_v038_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_ad_obv_corr_60d_base_v038_signal},
    "f26ad_f26_accumulation_distribution_ad_obv_diff_norm_30d_base_v039_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_ad_obv_diff_norm_30d_base_v039_signal},
    "f26ad_f26_accumulation_distribution_ad_zscore_60d_base_v040_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_ad_zscore_60d_base_v040_signal},
    "f26ad_f26_accumulation_distribution_ad_rank_200d_base_v041_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_ad_rank_200d_base_v041_signal},
    "f26ad_f26_accumulation_distribution_mfi_14d_base_v042_signal": {"inputs": ["high", "low", "close", "volume"], "func": f26ad_f26_accumulation_distribution_mfi_14d_base_v042_signal},
    "f26ad_f26_accumulation_distribution_mfi_28d_base_v043_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_mfi_28d_base_v043_signal},
    "f26ad_f26_accumulation_distribution_mfi14_slope_10d_base_v044_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_mfi14_slope_10d_base_v044_signal},
    "f26ad_f26_accumulation_distribution_pos_mf_ratio_21d_base_v045_signal": {"inputs": ["high", "low", "close", "volume"], "func": f26ad_f26_accumulation_distribution_pos_mf_ratio_21d_base_v045_signal},
    "f26ad_f26_accumulation_distribution_pos_mf_ratio_100d_base_v046_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_pos_mf_ratio_100d_base_v046_signal},
    "f26ad_f26_accumulation_distribution_ad_price_divergence_30d_base_v047_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_ad_price_divergence_30d_base_v047_signal},
    "f26ad_f26_accumulation_distribution_ad_price_divergence_100d_base_v048_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_ad_price_divergence_100d_base_v048_signal},
    "f26ad_f26_accumulation_distribution_clvvol_per_bar_mean_10d_base_v049_signal": {"inputs": ["high", "low", "close", "volume"], "func": f26ad_f26_accumulation_distribution_clvvol_per_bar_mean_10d_base_v049_signal},
    "f26ad_f26_accumulation_distribution_clvvol_per_bar_z_30d_base_v050_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_clvvol_per_bar_z_30d_base_v050_signal},
    "f26ad_f26_accumulation_distribution_ad_time_corr_60d_base_v051_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_ad_time_corr_60d_base_v051_signal},
    "f26ad_f26_accumulation_distribution_ad_time_corr_150d_base_v052_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_ad_time_corr_150d_base_v052_signal},
    "f26ad_f26_accumulation_distribution_clv_entropy_30d_base_v053_signal": {"inputs": ["high", "low", "closeadj"], "func": f26ad_f26_accumulation_distribution_clv_entropy_30d_base_v053_signal},
    "f26ad_f26_accumulation_distribution_cmf_multiwin_signagree_base_v054_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_cmf_multiwin_signagree_base_v054_signal},
    "f26ad_f26_accumulation_distribution_chaikin_signal_xover_streak_50d_base_v055_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_chaikin_signal_xover_streak_50d_base_v055_signal},
    "f26ad_f26_accumulation_distribution_chaikin_kurt_120d_base_v056_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_chaikin_kurt_120d_base_v056_signal},
    "f26ad_f26_accumulation_distribution_days_since_clv_pos_base_v057_signal": {"inputs": ["high", "low", "closeadj"], "func": f26ad_f26_accumulation_distribution_days_since_clv_pos_base_v057_signal},
    "f26ad_f26_accumulation_distribution_days_since_clv_neg_base_v058_signal": {"inputs": ["high", "low", "closeadj"], "func": f26ad_f26_accumulation_distribution_days_since_clv_neg_base_v058_signal},
    "f26ad_f26_accumulation_distribution_cmf21_std_60d_base_v059_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_cmf21_std_60d_base_v059_signal},
    "f26ad_f26_accumulation_distribution_clv_volwtd_skew_50d_base_v060_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_clv_volwtd_skew_50d_base_v060_signal},
    "f26ad_f26_accumulation_distribution_clv_ac1_30d_base_v061_signal": {"inputs": ["high", "low", "closeadj"], "func": f26ad_f26_accumulation_distribution_clv_ac1_30d_base_v061_signal},
    "f26ad_f26_accumulation_distribution_clv_ac5_75d_base_v062_signal": {"inputs": ["high", "low", "closeadj"], "func": f26ad_f26_accumulation_distribution_clv_ac5_75d_base_v062_signal},
    "f26ad_f26_accumulation_distribution_clv_high_extreme_frac_45d_base_v063_signal": {"inputs": ["high", "low", "closeadj"], "func": f26ad_f26_accumulation_distribution_clv_high_extreme_frac_45d_base_v063_signal},
    "f26ad_f26_accumulation_distribution_clvvol_volzscore_corr_60d_base_v064_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_clvvol_volzscore_corr_60d_base_v064_signal},
    "f26ad_f26_accumulation_distribution_klinger_sign_streak_45d_base_v065_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_klinger_sign_streak_45d_base_v065_signal},
    "f26ad_f26_accumulation_distribution_klinger_vf_norm_100d_base_v066_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_klinger_vf_norm_100d_base_v066_signal},
    "f26ad_f26_accumulation_distribution_mfi14_sign_base_v067_signal": {"inputs": ["high", "low", "close", "volume"], "func": f26ad_f26_accumulation_distribution_mfi14_sign_base_v067_signal},
    "f26ad_f26_accumulation_distribution_cmf21_minus_cmf100_base_v068_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_cmf21_minus_cmf100_base_v068_signal},
    "f26ad_f26_accumulation_distribution_chaikin_3_10_slope_5d_base_v069_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_chaikin_3_10_slope_5d_base_v069_signal},
    "f26ad_f26_accumulation_distribution_williams_ad_slope_30d_base_v070_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_williams_ad_slope_30d_base_v070_signal},
    "f26ad_f26_accumulation_distribution_cmf21_kurt_120d_base_v071_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_cmf21_kurt_120d_base_v071_signal},
    "f26ad_f26_accumulation_distribution_mfi_overbought_frac_60d_base_v072_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_mfi_overbought_frac_60d_base_v072_signal},
    "f26ad_f26_accumulation_distribution_chaikin_zero_xover_count_120d_base_v073_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_chaikin_zero_xover_count_120d_base_v073_signal},
    "f26ad_f26_accumulation_distribution_clv_volwtd_mean_minus_simple_30d_base_v074_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_clv_volwtd_mean_minus_simple_30d_base_v074_signal},
    "f26ad_f26_accumulation_distribution_cmf21_rank_minus_cmf50_rank_180d_base_v075_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_cmf21_rank_minus_cmf50_rank_180d_base_v075_signal},
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
    for name, entry in f26_accumulation_distribution_base_001_075_REGISTRY.items():
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
