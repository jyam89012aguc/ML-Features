"""f23_on_balance_volume_family base features 001-075.

Domain: On-Balance Volume (OBV) family — cumulative signed volume and its
derivatives/variants. OBV = cumsum(sign(close - close.shift(1)) * volume).
Variants used here: ADL (Accumulation/Distribution Line — cumulative CLV*volume),
PVT (Price-Volume Trend — cumulative pct_change*volume), NVI/PVI (Negative/
Positive Volume Index), Force Index (Elder), Klinger Volume Oscillator,
high-low signed cumulative volume, close-open signed cumulative volume.

Every feature references OBV or an OBV-variant cumulative-signed-volume
construction. Distinct from f21 (raw volume), f22 (volume trend regression),
f24 (price-volume confirmation), f26 (CLV-specific A/D pattern).

NaN policy: never fillna(<value>); only replace([inf,-inf], nan) at the
final return. Window > 21d uses closeadj; <= 21d uses close. Each function
spells its formula inline.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Helpers — cumulative signed volume constructors. Each feature spells its
# formula inline using these helpers (helpers are allowed per the guide).
# ---------------------------------------------------------------------------


def _obv(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Standard OBV = cumsum(sign(close.diff()) * volume). NaN until 2nd bar."""
    s = np.sign(close.diff())
    signed = s * volume
    return signed.cumsum()


def _adl(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Accumulation/Distribution Line: cumsum(CLV * volume).
    CLV = ((close-low) - (high-close)) / (high-low)."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((close - low) - (high - close)) / rng
    return (clv * volume).cumsum()


def _pvt(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Price-Volume Trend = cumsum(pct_change * volume)."""
    return (close.pct_change() * volume).cumsum()


def _obv_hl(high: pd.Series, volume: pd.Series) -> pd.Series:
    """High-low signed: cumsum(sign(high.diff()) * volume)."""
    return (np.sign(high.diff()) * volume).cumsum()


def _obv_co(open_: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Close-open signed: cumsum(sign(close - open) * volume)."""
    return (np.sign(close - open_) * volume).cumsum()


def _nvi(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Negative Volume Index: cumulative product factor that updates only on
    down-volume days. NVI[t] = NVI[t-1] * (1 + r[t]) if vol[t]<vol[t-1] else NVI[t-1]."""
    r = close.pct_change()
    v_down = volume < volume.shift(1)
    factor = np.where(v_down, 1.0 + r, 1.0)
    factor = np.where(np.isfinite(factor), factor, 1.0)
    out = pd.Series(np.cumprod(factor), index=close.index)
    out.iloc[0] = np.nan  # no prior bar
    return out


def _pvi(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Positive Volume Index: complement of NVI; updates on up-volume days."""
    r = close.pct_change()
    v_up = volume > volume.shift(1)
    factor = np.where(v_up, 1.0 + r, 1.0)
    factor = np.where(np.isfinite(factor), factor, 1.0)
    out = pd.Series(np.cumprod(factor), index=close.index)
    out.iloc[0] = np.nan
    return out


def _force_index(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Elder Force Index raw: close.diff() * volume."""
    return close.diff() * volume


def _klinger_vf(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Klinger Volume Force raw: volume * trend_sign * 2 * (dm/cm - 1) * 100.
    Simplified: vf = volume * sign(typical.diff()) where typical = (H+L+C)/3."""
    tp = (high + low + close) / 3.0
    return volume * np.sign(tp.diff())


def _sma(s: pd.Series, n: int) -> pd.Series:
    return s.rolling(n, min_periods=n).mean()


def _ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False, min_periods=n).mean()


def _signed_log(s: pd.Series) -> pd.Series:
    """Sign-preserving log: sign(s) * log1p(|s|)."""
    return np.sign(s) * np.log1p(s.abs())


# ---------------------------------------------------------------------------
# Features 001-075
# ---------------------------------------------------------------------------


# === OBV-relative-to-volume-MA (normalized levels) =========================


def f23ob_f23_on_balance_volume_family_obv_norm_volsma20_base_v001_signal(close, volume):
    """OBV / SMA(volume, 20). Normalized OBV by avg trading volume."""
    obv = (np.sign(close.diff()) * volume).cumsum()
    return (obv / volume.rolling(20, min_periods=20).mean()).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_obv_diff21_diff63_ratio_base_v002_signal(closeadj, volume):
    """OBV.diff(21) / OBV.diff(63). Short-vs-long accumulation ratio.
    Bounded-ish, decorrelated from raw OBV level."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    return (obv.diff(21) / obv.diff(63).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_obvco_netfrac_60d_base_v003_signal(open, closeadj, volume):
    """sum(sign(close-open)*volume, 60) / sum(volume, 60). Intra-bar net accumulation fraction."""
    sv = np.sign(closeadj - open) * volume
    num = sv.rolling(60, min_periods=60).sum()
    den = volume.rolling(60, min_periods=60).sum().replace(0.0, np.nan)
    return (num / den).replace([np.inf, -np.inf], np.nan)


# === OBV SLOPES (diff at various N) — signed accumulation impulse ==========


def f23ob_f23_on_balance_volume_family_obv_slope_10d_norm_base_v004_signal(close, volume):
    """OBV.diff(10) / SMA(volume, 10). Short impulse normalized by volume."""
    obv = (np.sign(close.diff()) * volume).cumsum()
    v = volume.rolling(10, min_periods=10).mean().replace(0.0, np.nan)
    return (obv.diff(10) / v).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_obv_slope_42d_norm_base_v005_signal(closeadj, volume):
    """OBV.diff(42) / SMA(volume, 42). Two-month accumulation impulse."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    v = volume.rolling(42, min_periods=42).mean().replace(0.0, np.nan)
    return (obv.diff(42) / v).replace([np.inf, -np.inf], np.nan)


# === OBV MA DISTANCES (level-distance — kept small, varied widely) =========


def f23ob_f23_on_balance_volume_family_obv_dist_sma20_base_v006_signal(close, volume):
    """(OBV - SMA(OBV, 20)) / SMA(volume, 20). OBV distance from short MA."""
    obv = (np.sign(close.diff()) * volume).cumsum()
    m = obv.rolling(20, min_periods=20).mean()
    v = volume.rolling(20, min_periods=20).mean().replace(0.0, np.nan)
    return ((obv - m) / v).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_obv_dist_ema100_base_v007_signal(closeadj, volume):
    """(OBV - EMA(OBV, 100)) / SMA(volume, 100). OBV distance from long EMA."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    e = obv.ewm(span=100, adjust=False, min_periods=100).mean()
    v = volume.rolling(100, min_periods=100).mean().replace(0.0, np.nan)
    return ((obv - e) / v).replace([np.inf, -np.inf], np.nan)


# === OBV CROSSOVER SIGNS (discrete) ========================================


def f23ob_f23_on_balance_volume_family_sign_obv_sma20_base_v008_signal(close, volume):
    """sign(OBV - SMA(OBV, 20)). Discrete trend filter on OBV."""
    obv = (np.sign(close.diff()) * volume).cumsum()
    m = obv.rolling(20, min_periods=20).mean()
    return np.sign(obv - m).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_sign_obv_ema60_base_v009_signal(closeadj, volume):
    """sign(OBV - EMA(OBV, 60)). Discrete sign of OBV vs long EMA."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    e = obv.ewm(span=60, adjust=False, min_periods=60).mean()
    return np.sign(obv - e).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_sign_obv_shift21_base_v010_signal(closeadj, volume):
    """sign(OBV - OBV.shift(21)). Sign of 21d OBV change (discrete direction)."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    return np.sign(obv - obv.shift(21)).replace([np.inf, -np.inf], np.nan)


# === DAYS-SINCE OBV CROSSED ITS MA (discrete counter) ======================


def f23ob_f23_on_balance_volume_family_daysince_obv_sma20_50d_base_v011_signal(close, volume):
    """Bars since last (OBV vs SMA(OBV, 20)) sign-change, capped 50."""
    obv = (np.sign(close.diff()) * volume).cumsum()
    diff = obv - obv.rolling(20, min_periods=20).mean()
    s = np.sign(diff)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return float(len(x))
        return float(len(x) - 1 - idx[-1])
    return flip.rolling(50, min_periods=50).apply(_ds, raw=True).replace([np.inf, -np.inf], np.nan)


# === STREAK above OBV MA (consecutive bars) ================================


def f23ob_f23_on_balance_volume_family_streak_obv_above_sma40_60d_base_v012_signal(closeadj, volume):
    """Consecutive bars where OBV > SMA(OBV, 40), capped 60."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    m = obv.rolling(40, min_periods=40).mean()
    sgn = (obv > m).astype(float).where(~m.isna())
    def _consec(x):
        c = 0
        for v in x[::-1]:
            if v > 0.5:
                c += 1
            else:
                break
        return float(c)
    return sgn.rolling(60, min_periods=60).apply(_consec, raw=True).replace([np.inf, -np.inf], np.nan)


# === OBV PCT-CHANGE (relative) =============================================


def f23ob_f23_on_balance_volume_family_obv_relchange_15d_base_v013_signal(close, volume):
    """(OBV - OBV.shift(15)) / OBV.abs(). Relative OBV change, signed."""
    obv = (np.sign(close.diff()) * volume).cumsum()
    return ((obv - obv.shift(15)) / obv.abs().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === OBV CURVATURE (acceleration) ==========================================


def f23ob_f23_on_balance_volume_family_obv_curv_30d_norm_base_v014_signal(closeadj, volume):
    """(OBV - 2*OBV.shift(15) + OBV.shift(30)) / SMA(volume, 30). OBV curvature."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    c = obv - 2.0 * obv.shift(15) + obv.shift(30)
    v = volume.rolling(30, min_periods=30).mean().replace(0.0, np.nan)
    return (c / v).replace([np.inf, -np.inf], np.nan)


# === ACCUMULATION/DISTRIBUTION LINE (ADL) — slope and MA distance ==========


def f23ob_f23_on_balance_volume_family_adl_slope_30d_norm_base_v015_signal(high, low, closeadj, volume):
    """ADL.diff(30) / SMA(volume, 30). ADL impulse over 30d."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    adl = (clv * volume).cumsum()
    v = volume.rolling(30, min_periods=30).mean().replace(0.0, np.nan)
    return (adl.diff(30) / v).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_adl_close_corr_60d_base_v016_signal(high, low, closeadj, volume):
    """60d Pearson corr between ADL.diff(5) and closeadj.pct_change(5).
    ADL-price agreement of short impulses."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    adl = (clv * volume).cumsum()
    return adl.diff(5).rolling(60, min_periods=60).corr(closeadj.pct_change(5)).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_adl_diff_zscore_50d_base_v017_signal(high, low, closeadj, volume):
    """z-score of ADL.diff(10) over 50d. Standardized ADL impulse — oscillates both signs."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    adl = (clv * volume).cumsum()
    d = adl.diff(10)
    mu = d.rolling(50, min_periods=50).mean()
    sd = d.rolling(50, min_periods=50).std()
    return ((d - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === PRICE-VOLUME TREND (PVT) — slope and MA distance ======================


def f23ob_f23_on_balance_volume_family_pvt_slope_21d_base_v018_signal(close, volume):
    """PVT.diff(21) / SMA(volume, 21). PVT impulse normalized."""
    pvt = (close.pct_change() * volume).cumsum()
    v = volume.rolling(21, min_periods=21).mean().replace(0.0, np.nan)
    return (pvt.diff(21) / v).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_pvt_dist_ema63_base_v019_signal(closeadj, volume):
    """(PVT - EMA(PVT, 63)) / SMA(volume, 63). PVT distance from EMA."""
    pvt = (closeadj.pct_change() * volume).cumsum()
    e = pvt.ewm(span=63, adjust=False, min_periods=63).mean()
    v = volume.rolling(63, min_periods=63).mean().replace(0.0, np.nan)
    return ((pvt - e) / v).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_sign_pvt_sma100_base_v020_signal(closeadj, volume):
    """sign(PVT - SMA(PVT, 100)). Discrete PVT trend filter."""
    pvt = (closeadj.pct_change() * volume).cumsum()
    m = pvt.rolling(100, min_periods=100).mean()
    return np.sign(pvt - m).replace([np.inf, -np.inf], np.nan)


# === OBV Z-SCORE in trailing window =========================================


def f23ob_f23_on_balance_volume_family_obv_zscore_60d_base_v021_signal(closeadj, volume):
    """z-score of OBV in trailing 60d window (its own mean/std)."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    mu = obv.rolling(60, min_periods=60).mean()
    sd = obv.rolling(60, min_periods=60).std()
    return ((obv - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_obvhl_pctrank_140d_base_v022_signal(high, volume):
    """140d percentile rank of OBV_HL (high-direction signed cum volume).
    Long rank of high-pivot accumulation."""
    obvhl = (np.sign(high.diff()) * volume).cumsum()
    return obvhl.rolling(140, min_periods=140).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# === OBV PERCENTILE RANK ===================================================


def f23ob_f23_on_balance_volume_family_obv_madstd_ratio_60d_base_v023_signal(closeadj, volume):
    """MAD/std of OBV.diff() over 60 bars. Robust-vs-L2 scale ratio of daily signed-volume.
    Distinct from skew/kurt — measures dispersion shape."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    d = obv.diff()
    mad = d.rolling(60, min_periods=60).apply(
        lambda x: float(np.mean(np.abs(x - np.mean(x)))), raw=True,
    )
    sd = d.rolling(60, min_periods=60).std()
    return (mad / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_obv_pctrank_180d_base_v024_signal(closeadj, volume):
    """180d percentile rank of OBV."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    return obv.rolling(180, min_periods=180).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# === HIGH-LOW signed cumulative volume (OBV variant on highs) ==============


def f23ob_f23_on_balance_volume_family_obvhl_slope_21d_norm_base_v025_signal(high, volume):
    """OBV_HL.diff(21) / SMA(volume, 21) where OBV_HL = cumsum(sign(high.diff())*volume)."""
    obvhl = (np.sign(high.diff()) * volume).cumsum()
    v = volume.rolling(21, min_periods=21).mean().replace(0.0, np.nan)
    return (obvhl.diff(21) / v).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_sign_obvhl_sma40_base_v026_signal(high, volume):
    """sign(OBV_HL - SMA(OBV_HL, 40)). OBV variant on highs, sign filter."""
    obvhl = (np.sign(high.diff()) * volume).cumsum()
    m = obvhl.rolling(40, min_periods=40).mean()
    return np.sign(obvhl - m).replace([np.inf, -np.inf], np.nan)


# === CLOSE-OPEN signed cumulative volume (intra-bar direction) =============


def f23ob_f23_on_balance_volume_family_obvco_slope_15d_norm_base_v027_signal(open, close, volume):
    """OBV_CO.diff(15)/SMA(volume,15) where OBV_CO = cumsum(sign(close-open)*volume)."""
    obvco = (np.sign(close - open) * volume).cumsum()
    v = volume.rolling(15, min_periods=15).mean().replace(0.0, np.nan)
    return (obvco.diff(15) / v).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_obvco_zscore_90d_base_v028_signal(open, closeadj, volume):
    """z-score of OBV_CO (close-open signed cum volume) over 90d."""
    obvco = (np.sign(closeadj - open) * volume).cumsum()
    mu = obvco.rolling(90, min_periods=90).mean()
    sd = obvco.rolling(90, min_periods=90).std()
    return ((obvco - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === OBV DIVERGENCE-WITH-PRICE (light — full divergence in f28) ============


def f23ob_f23_on_balance_volume_family_obv_close_sign_div_21d_base_v029_signal(close, volume):
    """sign(OBV.diff(21)) - sign(close.diff(21)). Divergence-sign in {-2,0,2}."""
    obv = (np.sign(close.diff()) * volume).cumsum()
    return (np.sign(obv.diff(21)) - np.sign(close.diff(21))).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_obv_close_slopediff_42d_base_v030_signal(closeadj, volume):
    """(OBV.diff(42)/SMA(vol,42)) - (closeadj.pct_change(42)*scaler). OBV vs close slope.
    Scaler 100 keeps both on roughly comparable order of magnitude."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    v = volume.rolling(42, min_periods=42).mean().replace(0.0, np.nan)
    obv_sl = obv.diff(42) / v
    close_sl = closeadj.pct_change(42) * 100.0
    return (obv_sl - close_sl).replace([np.inf, -np.inf], np.nan)


# === FORCE INDEX (Elder) — raw and EMA ====================================


def f23ob_f23_on_balance_volume_family_force_index_ema13_base_v031_signal(close, volume):
    """EMA(close.diff() * volume, 13). Elder Force Index smoothed."""
    fi = close.diff() * volume
    return fi.ewm(span=13, adjust=False, min_periods=13).mean().replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_fi_zscore_120d_base_v032_signal(closeadj, volume):
    """z-score of EMA(FI, 13) over 120d. Standardized force-index level."""
    fi = closeadj.diff() * volume
    e = fi.ewm(span=13, adjust=False, min_periods=13).mean()
    mu = e.rolling(120, min_periods=120).mean()
    sd = e.rolling(120, min_periods=120).std()
    return ((e - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_fi_sign_streak_30d_base_v033_signal(close, volume):
    """Consecutive bars (capped 30) where EMA(FI, 5) > 0. Force-index regime streak."""
    fi = close.diff() * volume
    e = fi.ewm(span=5, adjust=False, min_periods=5).mean()
    sgn = (e > 0).astype(float).where(~e.isna())
    def _consec(x):
        c = 0
        for v in x[::-1]:
            if v > 0.5:
                c += 1
            else:
                break
        return float(c)
    return sgn.rolling(30, min_periods=30).apply(_consec, raw=True).replace([np.inf, -np.inf], np.nan)


# === NEGATIVE/POSITIVE VOLUME INDEX (NVI/PVI) =============================


def f23ob_f23_on_balance_volume_family_nvi_dist_ema100_base_v034_signal(closeadj, volume):
    """log(NVI / EMA(NVI, 100)). NVI distance from long EMA."""
    r = closeadj.pct_change()
    v_down = volume < volume.shift(1)
    factor = np.where(v_down, 1.0 + r, 1.0)
    factor = np.where(np.isfinite(factor), factor, 1.0)
    nvi = pd.Series(np.cumprod(factor), index=closeadj.index)
    nvi.iloc[0] = np.nan
    e = nvi.ewm(span=100, adjust=False, min_periods=100).mean()
    return np.log(nvi / e).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_pvi_dist_ema60_base_v035_signal(closeadj, volume):
    """log(PVI / EMA(PVI, 60)). PVI distance from long EMA."""
    r = closeadj.pct_change()
    v_up = volume > volume.shift(1)
    factor = np.where(v_up, 1.0 + r, 1.0)
    factor = np.where(np.isfinite(factor), factor, 1.0)
    pvi = pd.Series(np.cumprod(factor), index=closeadj.index)
    pvi.iloc[0] = np.nan
    e = pvi.ewm(span=60, adjust=False, min_periods=60).mean()
    return np.log(pvi / e).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_nvi_pvi_logratio_base_v036_signal(closeadj, volume):
    """log(NVI / PVI). Dumb-money vs smart-money index ratio."""
    r = closeadj.pct_change()
    v_down = volume < volume.shift(1)
    v_up = volume > volume.shift(1)
    f_n = np.where(v_down, 1.0 + r, 1.0)
    f_p = np.where(v_up, 1.0 + r, 1.0)
    f_n = np.where(np.isfinite(f_n), f_n, 1.0)
    f_p = np.where(np.isfinite(f_p), f_p, 1.0)
    nvi = pd.Series(np.cumprod(f_n), index=closeadj.index); nvi.iloc[0] = np.nan
    pvi = pd.Series(np.cumprod(f_p), index=closeadj.index); pvi.iloc[0] = np.nan
    return np.log(nvi / pvi).replace([np.inf, -np.inf], np.nan)


# === KLINGER VOLUME OSCILLATOR =============================================


def f23ob_f23_on_balance_volume_family_klinger_kvo_base_v037_signal(high, low, closeadj, volume):
    """KVO = EMA(VF,34) - EMA(VF,55). VF = volume * sign(typical.diff())."""
    tp = (high + low + closeadj) / 3.0
    vf = volume * np.sign(tp.diff())
    return (vf.ewm(span=34, adjust=False, min_periods=34).mean()
            - vf.ewm(span=55, adjust=False, min_periods=55).mean()).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_klinger_vf_netfrac_30d_base_v038_signal(high, low, closeadj, volume):
    """sum(volume_force, 30) / sum(volume, 30). Klinger volume-force net direction fraction.
    Bounded in [-1,1] — structurally different from raw KVO."""
    tp = (high + low + closeadj) / 3.0
    vf = volume * np.sign(tp.diff())
    num = vf.rolling(30, min_periods=30).sum()
    den = volume.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    return (num / den).replace([np.inf, -np.inf], np.nan)


# === OBV RSI (RSI applied to OBV series) ===================================


def f23ob_f23_on_balance_volume_family_obv_signflip_count_30d_base_v039_signal(close, volume):
    """Count of sign-flips of OBV.diff() over last 30 bars. Choppiness of accumulation."""
    obv = (np.sign(close.diff()) * volume).cumsum()
    s = np.sign(obv.diff())
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(30, min_periods=30).sum().replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_pvt_zscore_diff_60d_base_v040_signal(closeadj, volume):
    """z-score of PVT.diff(10) over 60d. Standardized PVT impulse."""
    pvt = (closeadj.pct_change() * volume).cumsum()
    d = pvt.diff(10)
    mu = d.rolling(60, min_periods=60).mean()
    sd = d.rolling(60, min_periods=60).std()
    return ((d - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === STOCHASTIC of OBV =====================================================


def f23ob_f23_on_balance_volume_family_obv_diff_autocorr_60d_base_v041_signal(closeadj, volume):
    """60d lag-1 autocorrelation of OBV.diff(). Persistence of accumulation flow."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    d = obv.diff()
    return d.rolling(60, min_periods=60).apply(
        lambda x: float(pd.Series(x).autocorr(lag=1)) if pd.Series(x).std() > 0 else np.nan,
        raw=False,
    ).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_obv_lead_close_corr_42d_base_v042_signal(closeadj, volume):
    """42d corr between OBV.diff(5) and closeadj.pct_change(5).shift(-5).
    Measures whether OBV LEADS price (negative shift = future)."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    return obv.diff(5).rolling(42, min_periods=42).corr(closeadj.pct_change(5).shift(-5)).replace([np.inf, -np.inf], np.nan)


# === OBV OLS REGRESSION SLOPE vs time ======================================


def f23ob_f23_on_balance_volume_family_obv_regslope_40d_base_v043_signal(closeadj, volume):
    """OLS slope of OBV vs time index over 40 bars, normalized by SMA(vol, 40)."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    v = volume.rolling(40, min_periods=40).mean().replace(0.0, np.nan)
    def _slope(x):
        n = len(x); t = np.arange(n, dtype=float)
        mt = t.mean(); mx = x.mean()
        cov = np.sum((t - mt) * (x - mx))
        var = np.sum((t - mt) ** 2)
        if var == 0.0 or not np.isfinite(mx):
            return np.nan
        return float(cov / var)
    sl = obv.rolling(40, min_periods=40).apply(_slope, raw=True)
    return (sl / v).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_obv_rsq_80d_base_v044_signal(closeadj, volume):
    """R^2 of OLS fit of OBV vs time over 80 bars. Trend purity of accumulation."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    def _rsq(x):
        n = len(x); t = np.arange(n, dtype=float)
        mt = t.mean(); mx = x.mean()
        cov = np.sum((t - mt) * (x - mx))
        vt = np.sum((t - mt) ** 2); vx = np.sum((x - mx) ** 2)
        if vt == 0.0 or vx == 0.0:
            return np.nan
        r = cov / np.sqrt(vt * vx)
        return float(r * r)
    return obv.rolling(80, min_periods=80).apply(_rsq, raw=True).replace([np.inf, -np.inf], np.nan)


# === OBV vs PRICE correlation ==============================================


def f23ob_f23_on_balance_volume_family_obv_price_corr_60d_base_v045_signal(closeadj, volume):
    """60d Pearson corr between OBV and closeadj. Co-movement of accumulation and price."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    return obv.rolling(60, min_periods=60).corr(closeadj).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_obv_price_corr_180d_base_v046_signal(closeadj, volume):
    """180d Pearson corr between OBV and closeadj."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    return obv.rolling(180, min_periods=180).corr(closeadj).replace([np.inf, -np.inf], np.nan)


# === BOUNDED transforms of OBV =============================================


def f23ob_f23_on_balance_volume_family_obvco_signflip_60d_base_v047_signal(open, closeadj, volume):
    """Count of sign-flips of OBV_CO.diff() over 60 bars. Intra-bar direction churn."""
    obvco = (np.sign(closeadj - open) * volume).cumsum()
    s = np.sign(obvco.diff())
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(60, min_periods=60).sum().replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_tanh_obv_slope_30d_base_v048_signal(closeadj, volume):
    """tanh of (OBV.diff(30) / SMA(volume,30) / scaler). Bounded OBV slope."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    v = volume.rolling(30, min_periods=30).mean().replace(0.0, np.nan)
    raw = obv.diff(30) / v
    sd = raw.rolling(60, min_periods=60).std()
    return np.tanh(raw / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === OBV vs SUM(volume) — net accumulation fraction ========================




def f23ob_f23_on_balance_volume_family_obv_netfrac_120d_base_v050_signal(closeadj, volume):
    """sum(signed_volume, 120) / sum(volume, 120). Long-horizon net accumulation fraction."""
    sv = np.sign(closeadj.diff()) * volume
    num = sv.rolling(120, min_periods=120).sum()
    den = volume.rolling(120, min_periods=120).sum().replace(0.0, np.nan)
    return (num / den).replace([np.inf, -np.inf], np.nan)


# === OBV SLOPE-vs-CLOSE-SLOPE differential (light divergence) ==============


def f23ob_f23_on_balance_volume_family_obv_pct_vs_close_pct_15d_base_v051_signal(close, volume):
    """(OBV.pct_change(15)*scaler) - close.pct_change(15). Sign of accumulation lag/lead."""
    obv = (np.sign(close.diff()) * volume).cumsum()
    return (obv.pct_change(15) * 0.001 - close.pct_change(15)).replace([np.inf, -np.inf], np.nan)


# === SIGNED LOG transform of OBV (safety for both signs) ==================


def f23ob_f23_on_balance_volume_family_signedlog_obv_dist_sma30_base_v052_signal(close, volume):
    """sign(d)*log1p(|d|) where d = (OBV - SMA(OBV, 30)). Sign-preserving compression."""
    obv = (np.sign(close.diff()) * volume).cumsum()
    d = obv - obv.rolling(30, min_periods=30).mean()
    return (np.sign(d) * np.log1p(d.abs())).replace([np.inf, -np.inf], np.nan)


# === FRACTION-OF-BARS where OBV > its MA (regime measure) =================


def f23ob_f23_on_balance_volume_family_obv_fracabove_sma30_50d_base_v053_signal(closeadj, volume):
    """Fraction of last 50 bars where OBV > SMA(OBV, 30)."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    m = obv.rolling(30, min_periods=30).mean()
    sgn = (obv > m).astype(float).where(~m.isna())
    return sgn.rolling(50, min_periods=50).mean().replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_obv_fracabove_ema100_140d_base_v054_signal(closeadj, volume):
    """Fraction of last 140 bars where OBV > EMA(OBV, 100). Long regime measure."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    e = obv.ewm(span=100, adjust=False, min_periods=100).mean()
    sgn = (obv > e).astype(float).where(~e.isna())
    return sgn.rolling(140, min_periods=140).mean().replace([np.inf, -np.inf], np.nan)


# === RELATIVE-OBV-CHANGE z-score (acceleration normalized) ================


def f23ob_f23_on_balance_volume_family_obv_diff_zscore_42d_base_v055_signal(closeadj, volume):
    """z-score of OBV.diff(1) over trailing 42d. Standardized instantaneous accumulation."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    d = obv.diff()
    mu = d.rolling(42, min_periods=42).mean()
    sd = d.rolling(42, min_periods=42).std()
    return ((d - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === ADL/OBV CROSS-CONSISTENCY (sign agreement) ============================


def f23ob_f23_on_balance_volume_family_adl_obv_sign_agree_30d_base_v056_signal(high, low, closeadj, volume):
    """Frac of last 30 bars where sign(OBV.diff(5)) == sign(ADL.diff(5))."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    adl = (clv * volume).cumsum()
    s_o = np.sign(obv.diff(5))
    s_a = np.sign(adl.diff(5))
    agree = (s_o == s_a).astype(float).where(~s_o.isna() & ~s_a.isna())
    return agree.rolling(30, min_periods=30).mean().replace([np.inf, -np.inf], np.nan)


# === KLINGER signal-line crossover sign ====================================


def f23ob_f23_on_balance_volume_family_sign_kvo_signal_base_v057_signal(high, low, closeadj, volume):
    """sign(KVO - EMA(KVO, 13)). Klinger above/below its signal-line."""
    tp = (high + low + closeadj) / 3.0
    vf = volume * np.sign(tp.diff())
    kvo = (vf.ewm(span=34, adjust=False, min_periods=34).mean()
           - vf.ewm(span=55, adjust=False, min_periods=55).mean())
    sig = kvo.ewm(span=13, adjust=False, min_periods=13).mean()
    return np.sign(kvo - sig).replace([np.inf, -np.inf], np.nan)


# === FORCE-INDEX percentile rank ============================================


def f23ob_f23_on_balance_volume_family_fi_signpos_frac_50d_base_v058_signal(closeadj, volume):
    """Fraction of last 50 bars where EMA(FI, 13) > 0. Force-index positive regime fraction."""
    fi = closeadj.diff() * volume
    e = fi.ewm(span=13, adjust=False, min_periods=13).mean()
    sgn = (e > 0).astype(float).where(~e.isna())
    return sgn.rolling(50, min_periods=50).mean().replace([np.inf, -np.inf], np.nan)


# === OBV-VS-ADL log-ratio of MA-distances (cross-construction differential) =


def f23ob_f23_on_balance_volume_family_obv_adl_ma50dist_diff_base_v059_signal(high, low, closeadj, volume):
    """(OBV-SMA(OBV,50))/SMA(vol,50)  -  (ADL-SMA(ADL,50))/SMA(vol,50). Cross-method spread."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    adl = (clv * volume).cumsum()
    v = volume.rolling(50, min_periods=50).mean().replace(0.0, np.nan)
    a = (obv - obv.rolling(50, min_periods=50).mean()) / v
    b = (adl - adl.rolling(50, min_periods=50).mean()) / v
    return (a - b).replace([np.inf, -np.inf], np.nan)


# === OBV-VS-PVT log-ratio (cross-construction differential) ================


def f23ob_f23_on_balance_volume_family_pvt_rsq_60d_base_v060_signal(closeadj, volume):
    """R^2 of OLS fit PVT vs time over 60 bars. Trend purity of price-volume."""
    pvt = (closeadj.pct_change() * volume).cumsum()
    def _rsq(x):
        n = len(x); t = np.arange(n, dtype=float)
        mt = t.mean(); mx = x.mean()
        cov = np.sum((t - mt) * (x - mx))
        vt = np.sum((t - mt) ** 2); vx = np.sum((x - mx) ** 2)
        if vt == 0.0 or vx == 0.0:
            return np.nan
        r = cov / np.sqrt(vt * vx)
        return float(r * r)
    return pvt.rolling(60, min_periods=60).apply(_rsq, raw=True).replace([np.inf, -np.inf], np.nan)


# === OBV REVERSION RATE (sign-flip frequency) ==============================


def f23ob_f23_on_balance_volume_family_obv_revrate_sma20_50d_base_v061_signal(closeadj, volume):
    """50d count of sign-flips of (OBV - SMA(OBV, 20)) / 50."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    diff = obv - obv.rolling(20, min_periods=20).mean()
    s = np.sign(diff)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return (flip.rolling(50, min_periods=50).sum() / 50.0).replace([np.inf, -np.inf], np.nan)


# === HIGH-LOW OBV z-score (a different cumulative signed series) ==========


def f23ob_f23_on_balance_volume_family_obvhl_zscore_70d_base_v062_signal(high, volume):
    """z-score of OBV_HL (high-direction signed cum volume) over 70d."""
    obvhl = (np.sign(high.diff()) * volume).cumsum()
    mu = obvhl.rolling(70, min_periods=70).mean()
    sd = obvhl.rolling(70, min_periods=70).std()
    return ((obvhl - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === STREAK days OBV up-bars (consecutive OBV.diff > 0) ====================




# === OBV-DRIFT ratio (cumulative / accumulated absolute) ====================


def f23ob_f23_on_balance_volume_family_obv_efficiency_30d_base_v064_signal(closeadj, volume):
    """|sum(signed_vol, 30)| / sum(|signed_vol|, 30) over 30 bars. Accumulation efficiency."""
    sv = np.sign(closeadj.diff()) * volume
    num = sv.rolling(30, min_periods=30).sum().abs()
    den = sv.abs().rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    return (num / den).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_obv_efficiency_120d_base_v065_signal(closeadj, volume):
    """120d accumulation efficiency: |net signed| / total absolute signed volume."""
    sv = np.sign(closeadj.diff()) * volume
    num = sv.rolling(120, min_periods=120).sum().abs()
    den = sv.abs().rolling(120, min_periods=120).sum().replace(0.0, np.nan)
    return (num / den).replace([np.inf, -np.inf], np.nan)


# === ADL pctrank and OBV-style discrete ribbon =============================


def f23ob_f23_on_balance_volume_family_adl_pctrank_120d_base_v066_signal(high, low, closeadj, volume):
    """120d percentile rank of ADL."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    adl = (clv * volume).cumsum()
    return adl.rolling(120, min_periods=120).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_obv_ma_ribbon_count_base_v067_signal(closeadj, volume):
    """Count of OBV-MAs from {SMA(OBV, 10,20,40,80,160)} that OBV exceeds. Range 0-5."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    mas = [obv.rolling(k, min_periods=k).mean() for k in (10, 20, 40, 80, 160)]
    cnt = pd.Series(0.0, index=obv.index)
    mask = ~mas[0].isna()
    for m in mas:
        cnt = cnt + (obv > m).astype(float)
        mask = mask & ~m.isna()
    return cnt.where(mask).replace([np.inf, -np.inf], np.nan)


# === OBV-MA-pair logratio (long-term OBV trend differential) ===============


def f23ob_f23_on_balance_volume_family_obv_signed_logmadiff_30_90_base_v068_signal(closeadj, volume):
    """sign-log of (SMA(OBV,30) - SMA(OBV,90)) normalized by SMA(vol, 90).
    Cross-window OBV-MA differential."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    diff = obv.rolling(30, min_periods=30).mean() - obv.rolling(90, min_periods=90).mean()
    v = volume.rolling(90, min_periods=90).mean().replace(0.0, np.nan)
    raw = diff / v
    return (np.sign(raw) * np.log1p(raw.abs())).replace([np.inf, -np.inf], np.nan)


# === KLINGER stochastic (KVO position within own range) ====================


def f23ob_f23_on_balance_volume_family_kvo_stoch_80d_base_v069_signal(high, low, closeadj, volume):
    """Stoch-%K of KVO over 80d window."""
    tp = (high + low + closeadj) / 3.0
    vf = volume * np.sign(tp.diff())
    kvo = (vf.ewm(span=34, adjust=False, min_periods=34).mean()
           - vf.ewm(span=55, adjust=False, min_periods=55).mean())
    hi = kvo.rolling(80, min_periods=80).max()
    lo = kvo.rolling(80, min_periods=80).min()
    return ((kvo - lo) / (hi - lo).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === NVI/PVI percentile-rank (NEW class on volume-index variants) ==========


def f23ob_f23_on_balance_volume_family_nvi_pctrank_180d_base_v070_signal(closeadj, volume):
    """180d percentile rank of NVI."""
    r = closeadj.pct_change()
    v_down = volume < volume.shift(1)
    factor = np.where(v_down, 1.0 + r, 1.0)
    factor = np.where(np.isfinite(factor), factor, 1.0)
    nvi = pd.Series(np.cumprod(factor), index=closeadj.index); nvi.iloc[0] = np.nan
    return nvi.rolling(180, min_periods=180).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# === FORCE-INDEX bounded transform (tanh of z) ==============================


def f23ob_f23_on_balance_volume_family_fi_tanh_z_60d_base_v071_signal(closeadj, volume):
    """tanh of z-score of EMA(FI,13) over 60d. Bounded volume-force."""
    fi = closeadj.diff() * volume
    e = fi.ewm(span=13, adjust=False, min_periods=13).mean()
    mu = e.rolling(60, min_periods=60).mean()
    sd = e.rolling(60, min_periods=60).std()
    return np.tanh((e - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === PVT-VS-OBV correlation (cross-construction agreement) =================


def f23ob_f23_on_balance_volume_family_pvt_obv_corr_90d_base_v072_signal(closeadj, volume):
    """90d Pearson corr between PVT and OBV. Cross-construction agreement."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    pvt = (closeadj.pct_change() * volume).cumsum()
    return obv.rolling(90, min_periods=90).corr(pvt).replace([np.inf, -np.inf], np.nan)


# === OBV REGRESSION RESIDUAL STD (trend "purity" inverse) ==================


def f23ob_f23_on_balance_volume_family_obv_regresid_60d_base_v073_signal(closeadj, volume):
    """Std of residuals of OLS fit OBV vs time over 60 bars, normalized by SMA(vol, 60)."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    v = volume.rolling(60, min_periods=60).mean().replace(0.0, np.nan)
    def _r(x):
        n = len(x); t = np.arange(n, dtype=float)
        mt = t.mean(); mx = x.mean()
        cov = np.sum((t - mt) * (x - mx))
        vt = np.sum((t - mt) ** 2)
        if vt == 0.0:
            return np.nan
        b = cov / vt; a = mx - b * mt
        resid = x - (a + b * t)
        return float(np.std(resid))
    rs = obv.rolling(60, min_periods=60).apply(_r, raw=True)
    return (rs / v).replace([np.inf, -np.inf], np.nan)


# === OBV SKEW (NEW class: distributional shape of OBV.diff) ================


def f23ob_f23_on_balance_volume_family_obv_diff_skew_80d_base_v074_signal(closeadj, volume):
    """80d rolling skew of OBV.diff(). Asymmetry of daily signed-volume."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    return obv.diff().rolling(80, min_periods=80).skew().replace([np.inf, -np.inf], np.nan)


# === OBV KURTOSIS ==========================================================


def f23ob_f23_on_balance_volume_family_obv_diff_kurt_120d_base_v075_signal(closeadj, volume):
    """120d rolling kurtosis of OBV.diff(). Tail-heaviness of daily signed-volume."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    return obv.diff().rolling(120, min_periods=120).kurt().replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f23_on_balance_volume_family_base_001_075_REGISTRY = {
    "f23ob_f23_on_balance_volume_family_obv_norm_volsma20_base_v001_signal": {"inputs": ["close", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_norm_volsma20_base_v001_signal},
    "f23ob_f23_on_balance_volume_family_obv_diff21_diff63_ratio_base_v002_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_diff21_diff63_ratio_base_v002_signal},
    "f23ob_f23_on_balance_volume_family_obvco_netfrac_60d_base_v003_signal": {"inputs": ["open", "closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obvco_netfrac_60d_base_v003_signal},
    "f23ob_f23_on_balance_volume_family_obv_slope_10d_norm_base_v004_signal": {"inputs": ["close", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_slope_10d_norm_base_v004_signal},
    "f23ob_f23_on_balance_volume_family_obv_slope_42d_norm_base_v005_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_slope_42d_norm_base_v005_signal},
    "f23ob_f23_on_balance_volume_family_obv_dist_sma20_base_v006_signal": {"inputs": ["close", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_dist_sma20_base_v006_signal},
    "f23ob_f23_on_balance_volume_family_obv_dist_ema100_base_v007_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_dist_ema100_base_v007_signal},
    "f23ob_f23_on_balance_volume_family_sign_obv_sma20_base_v008_signal": {"inputs": ["close", "volume"], "func": f23ob_f23_on_balance_volume_family_sign_obv_sma20_base_v008_signal},
    "f23ob_f23_on_balance_volume_family_sign_obv_ema60_base_v009_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_sign_obv_ema60_base_v009_signal},
    "f23ob_f23_on_balance_volume_family_sign_obv_shift21_base_v010_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_sign_obv_shift21_base_v010_signal},
    "f23ob_f23_on_balance_volume_family_daysince_obv_sma20_50d_base_v011_signal": {"inputs": ["close", "volume"], "func": f23ob_f23_on_balance_volume_family_daysince_obv_sma20_50d_base_v011_signal},
    "f23ob_f23_on_balance_volume_family_streak_obv_above_sma40_60d_base_v012_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_streak_obv_above_sma40_60d_base_v012_signal},
    "f23ob_f23_on_balance_volume_family_obv_relchange_15d_base_v013_signal": {"inputs": ["close", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_relchange_15d_base_v013_signal},
    "f23ob_f23_on_balance_volume_family_obv_curv_30d_norm_base_v014_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_curv_30d_norm_base_v014_signal},
    "f23ob_f23_on_balance_volume_family_adl_slope_30d_norm_base_v015_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_adl_slope_30d_norm_base_v015_signal},
    "f23ob_f23_on_balance_volume_family_adl_close_corr_60d_base_v016_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_adl_close_corr_60d_base_v016_signal},
    "f23ob_f23_on_balance_volume_family_adl_diff_zscore_50d_base_v017_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_adl_diff_zscore_50d_base_v017_signal},
    "f23ob_f23_on_balance_volume_family_pvt_slope_21d_base_v018_signal": {"inputs": ["close", "volume"], "func": f23ob_f23_on_balance_volume_family_pvt_slope_21d_base_v018_signal},
    "f23ob_f23_on_balance_volume_family_pvt_dist_ema63_base_v019_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_pvt_dist_ema63_base_v019_signal},
    "f23ob_f23_on_balance_volume_family_sign_pvt_sma100_base_v020_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_sign_pvt_sma100_base_v020_signal},
    "f23ob_f23_on_balance_volume_family_obv_zscore_60d_base_v021_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_zscore_60d_base_v021_signal},
    "f23ob_f23_on_balance_volume_family_obvhl_pctrank_140d_base_v022_signal": {"inputs": ["high", "volume"], "func": f23ob_f23_on_balance_volume_family_obvhl_pctrank_140d_base_v022_signal},
    "f23ob_f23_on_balance_volume_family_obv_madstd_ratio_60d_base_v023_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_madstd_ratio_60d_base_v023_signal},
    "f23ob_f23_on_balance_volume_family_obv_pctrank_180d_base_v024_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_pctrank_180d_base_v024_signal},
    "f23ob_f23_on_balance_volume_family_obvhl_slope_21d_norm_base_v025_signal": {"inputs": ["high", "volume"], "func": f23ob_f23_on_balance_volume_family_obvhl_slope_21d_norm_base_v025_signal},
    "f23ob_f23_on_balance_volume_family_sign_obvhl_sma40_base_v026_signal": {"inputs": ["high", "volume"], "func": f23ob_f23_on_balance_volume_family_sign_obvhl_sma40_base_v026_signal},
    "f23ob_f23_on_balance_volume_family_obvco_slope_15d_norm_base_v027_signal": {"inputs": ["open", "close", "volume"], "func": f23ob_f23_on_balance_volume_family_obvco_slope_15d_norm_base_v027_signal},
    "f23ob_f23_on_balance_volume_family_obvco_zscore_90d_base_v028_signal": {"inputs": ["open", "closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obvco_zscore_90d_base_v028_signal},
    "f23ob_f23_on_balance_volume_family_obv_close_sign_div_21d_base_v029_signal": {"inputs": ["close", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_close_sign_div_21d_base_v029_signal},
    "f23ob_f23_on_balance_volume_family_obv_close_slopediff_42d_base_v030_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_close_slopediff_42d_base_v030_signal},
    "f23ob_f23_on_balance_volume_family_force_index_ema13_base_v031_signal": {"inputs": ["close", "volume"], "func": f23ob_f23_on_balance_volume_family_force_index_ema13_base_v031_signal},
    "f23ob_f23_on_balance_volume_family_fi_zscore_120d_base_v032_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_fi_zscore_120d_base_v032_signal},
    "f23ob_f23_on_balance_volume_family_fi_sign_streak_30d_base_v033_signal": {"inputs": ["close", "volume"], "func": f23ob_f23_on_balance_volume_family_fi_sign_streak_30d_base_v033_signal},
    "f23ob_f23_on_balance_volume_family_nvi_dist_ema100_base_v034_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_nvi_dist_ema100_base_v034_signal},
    "f23ob_f23_on_balance_volume_family_pvi_dist_ema60_base_v035_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_pvi_dist_ema60_base_v035_signal},
    "f23ob_f23_on_balance_volume_family_nvi_pvi_logratio_base_v036_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_nvi_pvi_logratio_base_v036_signal},
    "f23ob_f23_on_balance_volume_family_klinger_kvo_base_v037_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_klinger_kvo_base_v037_signal},
    "f23ob_f23_on_balance_volume_family_klinger_vf_netfrac_30d_base_v038_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_klinger_vf_netfrac_30d_base_v038_signal},
    "f23ob_f23_on_balance_volume_family_obv_signflip_count_30d_base_v039_signal": {"inputs": ["close", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_signflip_count_30d_base_v039_signal},
    "f23ob_f23_on_balance_volume_family_pvt_zscore_diff_60d_base_v040_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_pvt_zscore_diff_60d_base_v040_signal},
    "f23ob_f23_on_balance_volume_family_obv_diff_autocorr_60d_base_v041_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_diff_autocorr_60d_base_v041_signal},
    "f23ob_f23_on_balance_volume_family_obv_lead_close_corr_42d_base_v042_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_lead_close_corr_42d_base_v042_signal},
    "f23ob_f23_on_balance_volume_family_obv_regslope_40d_base_v043_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_regslope_40d_base_v043_signal},
    "f23ob_f23_on_balance_volume_family_obv_rsq_80d_base_v044_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_rsq_80d_base_v044_signal},
    "f23ob_f23_on_balance_volume_family_obv_price_corr_60d_base_v045_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_price_corr_60d_base_v045_signal},
    "f23ob_f23_on_balance_volume_family_obv_price_corr_180d_base_v046_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_price_corr_180d_base_v046_signal},
    "f23ob_f23_on_balance_volume_family_obvco_signflip_60d_base_v047_signal": {"inputs": ["open", "closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obvco_signflip_60d_base_v047_signal},
    "f23ob_f23_on_balance_volume_family_tanh_obv_slope_30d_base_v048_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_tanh_obv_slope_30d_base_v048_signal},
    "f23ob_f23_on_balance_volume_family_obv_netfrac_120d_base_v050_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_netfrac_120d_base_v050_signal},
    "f23ob_f23_on_balance_volume_family_obv_pct_vs_close_pct_15d_base_v051_signal": {"inputs": ["close", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_pct_vs_close_pct_15d_base_v051_signal},
    "f23ob_f23_on_balance_volume_family_signedlog_obv_dist_sma30_base_v052_signal": {"inputs": ["close", "volume"], "func": f23ob_f23_on_balance_volume_family_signedlog_obv_dist_sma30_base_v052_signal},
    "f23ob_f23_on_balance_volume_family_obv_fracabove_sma30_50d_base_v053_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_fracabove_sma30_50d_base_v053_signal},
    "f23ob_f23_on_balance_volume_family_obv_fracabove_ema100_140d_base_v054_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_fracabove_ema100_140d_base_v054_signal},
    "f23ob_f23_on_balance_volume_family_obv_diff_zscore_42d_base_v055_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_diff_zscore_42d_base_v055_signal},
    "f23ob_f23_on_balance_volume_family_adl_obv_sign_agree_30d_base_v056_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_adl_obv_sign_agree_30d_base_v056_signal},
    "f23ob_f23_on_balance_volume_family_sign_kvo_signal_base_v057_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_sign_kvo_signal_base_v057_signal},
    "f23ob_f23_on_balance_volume_family_fi_signpos_frac_50d_base_v058_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_fi_signpos_frac_50d_base_v058_signal},
    "f23ob_f23_on_balance_volume_family_obv_adl_ma50dist_diff_base_v059_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_adl_ma50dist_diff_base_v059_signal},
    "f23ob_f23_on_balance_volume_family_pvt_rsq_60d_base_v060_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_pvt_rsq_60d_base_v060_signal},
    "f23ob_f23_on_balance_volume_family_obv_revrate_sma20_50d_base_v061_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_revrate_sma20_50d_base_v061_signal},
    "f23ob_f23_on_balance_volume_family_obvhl_zscore_70d_base_v062_signal": {"inputs": ["high", "volume"], "func": f23ob_f23_on_balance_volume_family_obvhl_zscore_70d_base_v062_signal},
    "f23ob_f23_on_balance_volume_family_obv_efficiency_30d_base_v064_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_efficiency_30d_base_v064_signal},
    "f23ob_f23_on_balance_volume_family_obv_efficiency_120d_base_v065_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_efficiency_120d_base_v065_signal},
    "f23ob_f23_on_balance_volume_family_adl_pctrank_120d_base_v066_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_adl_pctrank_120d_base_v066_signal},
    "f23ob_f23_on_balance_volume_family_obv_ma_ribbon_count_base_v067_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_ma_ribbon_count_base_v067_signal},
    "f23ob_f23_on_balance_volume_family_obv_signed_logmadiff_30_90_base_v068_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_signed_logmadiff_30_90_base_v068_signal},
    "f23ob_f23_on_balance_volume_family_kvo_stoch_80d_base_v069_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_kvo_stoch_80d_base_v069_signal},
    "f23ob_f23_on_balance_volume_family_nvi_pctrank_180d_base_v070_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_nvi_pctrank_180d_base_v070_signal},
    "f23ob_f23_on_balance_volume_family_fi_tanh_z_60d_base_v071_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_fi_tanh_z_60d_base_v071_signal},
    "f23ob_f23_on_balance_volume_family_pvt_obv_corr_90d_base_v072_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_pvt_obv_corr_90d_base_v072_signal},
    "f23ob_f23_on_balance_volume_family_obv_regresid_60d_base_v073_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_regresid_60d_base_v073_signal},
    "f23ob_f23_on_balance_volume_family_obv_diff_skew_80d_base_v074_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_diff_skew_80d_base_v074_signal},
    "f23ob_f23_on_balance_volume_family_obv_diff_kurt_120d_base_v075_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_diff_kurt_120d_base_v075_signal},
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
    for name, entry in f23_on_balance_volume_family_base_001_075_REGISTRY.items():
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
