"""
21_volume_concentration — Extended Features 001-075
Domain: deeper volume-concentration measures — dollar-volume concentration,
        worst-return-day concentration, price-low proximity, Lorenz-area,
        Renyi/Tsallis entropy variants, tail-weighted HHI, effective-N,
        up/down asymmetry on longer windows, volume-weighted return dispersion,
        concentration trends, statistical transforms on novel bases.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# -- Constants -----------------------------------------------------------------
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_MON  = 21
_TD_WEEK = 5
_EPS     = 1e-9

# -- Utility helpers -----------------------------------------------------------

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()

# -- Scalar helpers for rolling(..).apply() ------------------------------------

def _gini_scalar(arr: np.ndarray) -> float:
    """Gini coefficient (scalar, raw=True safe)."""
    n = len(arr)
    if n < 2:
        return np.nan
    s = arr.sum()
    if s <= _EPS:
        return np.nan
    sorted_a = np.sort(arr)
    idx = np.arange(1, n + 1)
    return float((2.0 * (idx * sorted_a).sum() - (n + 1) * s) / (n * s))


def _hhi_scalar(arr: np.ndarray) -> float:
    """Herfindahl-Hirschman index (scalar)."""
    total = arr.sum()
    if total <= _EPS:
        return np.nan
    p = arr / total
    return float((p ** 2).sum())


def _entropy_scalar(arr: np.ndarray) -> float:
    """Shannon entropy in nats (scalar)."""
    total = arr.sum()
    if total <= _EPS:
        return np.nan
    p = arr / total
    p = p[p > 0]
    return float(-(p * np.log(p)).sum())


def _renyi2_scalar(arr: np.ndarray) -> float:
    """Renyi entropy of order 2 (collision entropy) in nats (scalar)."""
    total = arr.sum()
    if total <= _EPS:
        return np.nan
    p = arr / total
    p = p[p > 0]
    sq = float((p ** 2).sum())
    if sq <= _EPS:
        return np.nan
    return float(-np.log(sq))


def _renyi05_scalar(arr: np.ndarray) -> float:
    """Renyi entropy of order 0.5 in nats (scalar)."""
    total = arr.sum()
    if total <= _EPS:
        return np.nan
    p = arr / total
    p = p[p > 0]
    val = float((p ** 0.5).sum())
    if val <= _EPS:
        return np.nan
    return float(2.0 * np.log(val))


def _tsallis2_scalar(arr: np.ndarray) -> float:
    """Tsallis entropy of order 2 (scalar)."""
    total = arr.sum()
    if total <= _EPS:
        return np.nan
    p = arr / total
    p = p[p > 0]
    return float(1.0 - float((p ** 2).sum()))


def _tsallis05_scalar(arr: np.ndarray) -> float:
    """Tsallis entropy of order 0.5 (scalar)."""
    total = arr.sum()
    if total <= _EPS:
        return np.nan
    p = arr / total
    p = p[p > 0]
    return float((float((p ** 0.5).sum()) - 1.0) / 0.5)


def _lorenz_area_scalar(arr: np.ndarray) -> float:
    """Area between perfect-equality line and Lorenz curve."""
    n = len(arr)
    if n < 2:
        return np.nan
    s = arr.sum()
    if s <= _EPS:
        return np.nan
    sorted_a = np.sort(arr)
    cumvol = np.cumsum(sorted_a) / s
    cumeq = np.arange(1, n + 1) / float(n)
    lorenz_integral = float(np.trapz(cumvol, cumeq))
    return float(0.5 - lorenz_integral)


def _effective_n_scalar(arr: np.ndarray) -> float:
    """Effective number of active days = 1/HHI."""
    total = arr.sum()
    if total <= _EPS:
        return np.nan
    p = arr / total
    hhi = float((p ** 2).sum())
    if hhi <= _EPS:
        return np.nan
    return float(1.0 / hhi)


def _tail_hhi_scalar(arr: np.ndarray, tail_frac: float) -> float:
    """HHI restricted to top tail_frac fraction of days by volume."""
    n = len(arr)
    if n < 2:
        return np.nan
    k = max(1, int(np.ceil(n * tail_frac)))
    idx = np.argpartition(arr, -k)[-k:]
    return _hhi_scalar(arr[idx])


def _bottom_share_scalar(arr: np.ndarray, bot_frac: float) -> float:
    """Share of total volume in the bottom bot_frac fraction of days."""
    n = len(arr)
    if n < 2:
        return np.nan
    k = max(1, int(np.floor(n * bot_frac)))
    total = arr.sum()
    if total <= _EPS:
        return np.nan
    idx = np.argpartition(arr, k - 1)[:k]
    return float(arr[idx].sum() / total)


def _top3_share_scalar(arr: np.ndarray) -> float:
    """Share of top-3 values in array total."""
    total = arr.sum()
    if total <= _EPS:
        return np.nan
    k = min(3, len(arr))
    return float(np.partition(arr, -k)[-k:].sum() / total)


def _topn_worst_ret_vol_share(vol_arr: np.ndarray, ret_arr: np.ndarray, n: int) -> float:
    """Share of total volume concentrated in the n worst-return days."""
    total = vol_arr.sum()
    if total <= _EPS or len(ret_arr) < 1:
        return np.nan
    nn = min(n, len(ret_arr))
    idx_worst = np.argpartition(ret_arr, nn - 1)[:nn]
    return float(vol_arr[idx_worst].sum() / total)


def _vol_near_low_share(vol_arr: np.ndarray, low_arr: np.ndarray,
                        close_arr: np.ndarray, frac: float) -> float:
    """Share of volume on days where close is within frac above window low."""
    win_low = low_arr.min()
    threshold = win_low * (1.0 + frac)
    mask = close_arr <= threshold
    total = vol_arr.sum()
    if total <= _EPS:
        return np.nan
    return float(vol_arr[mask].sum() / total)


def _worst_ret_vol_share_loop(volume: pd.Series, ret: pd.Series,
                               w: int, n: int) -> pd.Series:
    """Rolling helper: share of volume in n worst-return days."""
    result = pd.Series(np.nan, index=volume.index, dtype=float)
    va = volume.values
    ra = ret.values
    length = len(va)
    mp = max(1, w // 2)
    for i in range(length):
        start = max(0, i - w + 1)
        sub_v = va[start:i + 1]
        sub_r = ra[start:i + 1]
        if len(sub_v) < mp:
            continue
        result.iat[i] = _topn_worst_ret_vol_share(sub_v, sub_r, n)
    return result


def _vol_near_low_loop(volume: pd.Series, low: pd.Series,
                       close: pd.Series, w: int, frac: float) -> pd.Series:
    """Rolling helper: share of volume near price low."""
    result = pd.Series(np.nan, index=volume.index, dtype=float)
    va = volume.values
    la = low.values
    ca = close.values
    length = len(va)
    mp = max(1, w // 2)
    for i in range(length):
        start = max(0, i - w + 1)
        if i + 1 - start < mp:
            continue
        result.iat[i] = _vol_near_low_share(
            va[start:i+1], la[start:i+1], ca[start:i+1], frac)
    return result


def _up_minus_down_share_loop(volume: pd.Series, ret: pd.Series, w: int) -> pd.Series:
    """Rolling helper: up-day share minus down-day share."""
    result = pd.Series(np.nan, index=volume.index, dtype=float)
    va = volume.values
    ra = ret.values
    length = len(va)
    mp = max(1, w // 2)
    for i in range(length):
        start = max(0, i - w + 1)
        sub_v = va[start:i + 1]
        sub_r = ra[start:i + 1]
        if len(sub_v) < mp:
            continue
        total = sub_v.sum()
        if total <= _EPS:
            continue
        up = sub_v[sub_r > 0].sum() / total
        dn = sub_v[sub_r < 0].sum() / total
        result.iat[i] = float(up - dn)
    return result


# -- Feature Functions 001-075 -------------------------------------------------

# Group A (ext_001-010): Dollar-volume (close*volume) concentration

def vcc_ext_001_dv_hhi_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """HHI of daily dollar-volume (close*volume) shares over 21-day window."""
    dv = close * volume
    return dv.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _hhi_scalar, raw=True)


def vcc_ext_002_dv_hhi_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """HHI of daily dollar-volume shares over 63-day window."""
    dv = close * volume
    return dv.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        _hhi_scalar, raw=True)


def vcc_ext_003_dv_gini_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Gini coefficient of daily dollar-volume distribution over 21-day window."""
    dv = close * volume
    return dv.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _gini_scalar, raw=True)


def vcc_ext_004_dv_gini_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Gini coefficient of daily dollar-volume distribution over 63-day window."""
    dv = close * volume
    return dv.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        _gini_scalar, raw=True)


def vcc_ext_005_dv_entropy_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Shannon entropy of daily dollar-volume shares over 21-day window."""
    dv = close * volume
    return dv.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _entropy_scalar, raw=True)


def vcc_ext_006_dv_entropy_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Shannon entropy of daily dollar-volume shares over 63-day window."""
    dv = close * volume
    return dv.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        _entropy_scalar, raw=True)


def vcc_ext_007_dv_top1_share_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Top-1 day share of 21-day total dollar-volume."""
    dv = close * volume
    dv_max = _rolling_max(dv, _TD_MON)
    dv_tot = _rolling_sum(dv, _TD_MON)
    return _safe_div(dv_max, dv_tot)


def vcc_ext_008_dv_top3_share_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Top-3 day share of 21-day total dollar-volume."""
    dv = close * volume
    return dv.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _top3_share_scalar, raw=True)


def vcc_ext_009_dv_hhi_21d_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 21-day dollar-volume HHI within trailing 252-day distribution."""
    h = vcc_ext_001_dv_hhi_21d(close, volume)
    m = _rolling_mean(h, _TD_YEAR)
    s = _rolling_std(h, _TD_YEAR)
    return _safe_div(h - m, s)


def vcc_ext_010_dv_gini_21d_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day dollar-volume Gini within 252-day distribution."""
    g = vcc_ext_003_dv_gini_21d(close, volume)
    return g.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# Group B (ext_011-017): Worst-return-day volume concentration

def vcc_ext_011_top1_worst_ret_vol_share_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Share of 21-day total volume on the single worst-return day."""
    ret = close.pct_change().fillna(0.0)
    return _worst_ret_vol_share_loop(volume, ret, _TD_MON, 1)


def vcc_ext_012_top3_worst_ret_vol_share_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Share of 21-day total volume on the 3 worst-return days."""
    ret = close.pct_change().fillna(0.0)
    return _worst_ret_vol_share_loop(volume, ret, _TD_MON, 3)


def vcc_ext_013_top5_worst_ret_vol_share_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Share of 63-day total volume on the 5 worst-return days."""
    ret = close.pct_change().fillna(0.0)
    return _worst_ret_vol_share_loop(volume, ret, _TD_QTR, 5)


def vcc_ext_014_top10_worst_ret_vol_share_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Share of 63-day total volume on the 10 worst-return days."""
    ret = close.pct_change().fillna(0.0)
    return _worst_ret_vol_share_loop(volume, ret, _TD_QTR, 10)


def vcc_ext_015_top3_worst_ret_vol_share_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Share of 63-day total volume on the 3 worst-return days."""
    ret = close.pct_change().fillna(0.0)
    return _worst_ret_vol_share_loop(volume, ret, _TD_QTR, 3)


def vcc_ext_016_top1_worst_ret_vol_share_21d_zscore_252d(
        close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 21d worst-return-day vol share within 252-day distribution."""
    s = vcc_ext_011_top1_worst_ret_vol_share_21d(close, volume)
    m = _rolling_mean(s, _TD_YEAR)
    sd = _rolling_std(s, _TD_YEAR)
    return _safe_div(s - m, sd)


def vcc_ext_017_top3_worst_ret_vol_share_21d_pct_rank_252d(
        close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 21d top-3-worst-return vol share in 252-day distribution."""
    s = vcc_ext_012_top3_worst_ret_vol_share_21d(close, volume)
    return s.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# Group C (ext_018-025): Volume concentrated near price lows

def vcc_ext_018_vol_near_low_5pct_21d(
        close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Share of 21-day volume on days where close is within 5pct above window low."""
    return _vol_near_low_loop(volume, low, close, _TD_MON, 0.05)


def vcc_ext_019_vol_near_low_10pct_21d(
        close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Share of 21-day volume on days where close is within 10pct above window low."""
    return _vol_near_low_loop(volume, low, close, _TD_MON, 0.10)


def vcc_ext_020_vol_near_low_5pct_63d(
        close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Share of 63-day volume on days where close is within 5pct above window low."""
    return _vol_near_low_loop(volume, low, close, _TD_QTR, 0.05)


def vcc_ext_021_vol_near_low_10pct_63d(
        close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Share of 63-day volume on days where close is within 10pct above window low."""
    return _vol_near_low_loop(volume, low, close, _TD_QTR, 0.10)


def vcc_ext_022_vol_near_low_5pct_21d_zscore_252d(
        close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 21d near-low-5pct vol share within 252-day distribution."""
    s = vcc_ext_018_vol_near_low_5pct_21d(close, low, volume)
    m = _rolling_mean(s, _TD_YEAR)
    sd = _rolling_std(s, _TD_YEAR)
    return _safe_div(s - m, sd)


def vcc_ext_023_vol_near_low_10pct_21d_pct_rank_252d(
        close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 21d near-low-10pct vol share in 252-day distribution."""
    s = vcc_ext_019_vol_near_low_10pct_21d(close, low, volume)
    return s.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vcc_ext_024_vol_near_low_5pct_63d_zscore_252d(
        close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 63d near-low-5pct vol share within 252-day distribution."""
    s = vcc_ext_020_vol_near_low_5pct_63d(close, low, volume)
    m = _rolling_mean(s, _TD_YEAR)
    sd = _rolling_std(s, _TD_YEAR)
    return _safe_div(s - m, sd)


def vcc_ext_025_vol_near_low_ratio_21d_vs_63d(
        close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 21d to 63d near-low-5pct volume share (recent vs medium-run)."""
    s21 = vcc_ext_018_vol_near_low_5pct_21d(close, low, volume)
    s63 = vcc_ext_020_vol_near_low_5pct_63d(close, low, volume)
    return _safe_div(s21, s63)


# Group D (ext_026-035): Renyi and Tsallis entropy variants

def vcc_ext_026_renyi_entropy_2_21d(volume: pd.Series) -> pd.Series:
    """Renyi entropy of order 2 (collision entropy) of volume shares over 21d."""
    return volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _renyi2_scalar, raw=True)


def vcc_ext_027_renyi_entropy_2_63d(volume: pd.Series) -> pd.Series:
    """Renyi entropy of order 2 of volume shares over 63d."""
    return volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        _renyi2_scalar, raw=True)


def vcc_ext_028_renyi_entropy_05_21d(volume: pd.Series) -> pd.Series:
    """Renyi entropy of order 0.5 of volume shares over 21d."""
    return volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _renyi05_scalar, raw=True)


def vcc_ext_029_tsallis_entropy_2_21d(volume: pd.Series) -> pd.Series:
    """Tsallis entropy of order 2 of volume shares over 21d."""
    return volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _tsallis2_scalar, raw=True)


def vcc_ext_030_tsallis_entropy_2_63d(volume: pd.Series) -> pd.Series:
    """Tsallis entropy of order 2 of volume shares over 63d."""
    return volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        _tsallis2_scalar, raw=True)


def vcc_ext_031_tsallis_entropy_05_21d(volume: pd.Series) -> pd.Series:
    """Tsallis entropy of order 0.5 of volume shares over 21d."""
    return volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _tsallis05_scalar, raw=True)


def vcc_ext_032_renyi_entropy_2_21d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 21d Renyi-2 entropy within 252-day distribution."""
    r = vcc_ext_026_renyi_entropy_2_21d(volume)
    m = _rolling_mean(r, _TD_YEAR)
    s = _rolling_std(r, _TD_YEAR)
    return _safe_div(r - m, s)


def vcc_ext_033_renyi_entropy_2_21d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21d Renyi-2 entropy in 252-day distribution."""
    r = vcc_ext_026_renyi_entropy_2_21d(volume)
    return r.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vcc_ext_034_renyi_vs_shannon_ratio_21d(volume: pd.Series) -> pd.Series:
    """Ratio of Renyi-2 entropy to Shannon entropy over 21d (tail-weight indicator)."""
    r2 = vcc_ext_026_renyi_entropy_2_21d(volume)
    sh = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _entropy_scalar, raw=True)
    return _safe_div(r2, sh.clip(lower=_EPS))


def vcc_ext_035_tsallis_entropy_2_21d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 21d Tsallis-2 entropy within 252-day distribution."""
    t = vcc_ext_029_tsallis_entropy_2_21d(volume)
    m = _rolling_mean(t, _TD_YEAR)
    s = _rolling_std(t, _TD_YEAR)
    return _safe_div(t - m, s)


# Group E (ext_036-043): Lorenz-curve area

def vcc_ext_036_lorenz_area_21d(volume: pd.Series) -> pd.Series:
    """Lorenz-curve area (area between equality line and Lorenz curve) over 21d."""
    return volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _lorenz_area_scalar, raw=True)


def vcc_ext_037_lorenz_area_63d(volume: pd.Series) -> pd.Series:
    """Lorenz-curve area over 63d."""
    return volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        _lorenz_area_scalar, raw=True)


def vcc_ext_038_lorenz_area_126d(volume: pd.Series) -> pd.Series:
    """Lorenz-curve area over 126d."""
    return volume.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(
        _lorenz_area_scalar, raw=True)


def vcc_ext_039_lorenz_area_21d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 21d Lorenz area within 252-day distribution."""
    la = vcc_ext_036_lorenz_area_21d(volume)
    m = _rolling_mean(la, _TD_YEAR)
    s = _rolling_std(la, _TD_YEAR)
    return _safe_div(la - m, s)


def vcc_ext_040_lorenz_area_63d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 63d Lorenz area within 252-day distribution."""
    la = vcc_ext_037_lorenz_area_63d(volume)
    return la.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vcc_ext_041_lorenz_area_21d_vs_63d_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 21d Lorenz area to 63d Lorenz area."""
    return _safe_div(vcc_ext_036_lorenz_area_21d(volume),
                     vcc_ext_037_lorenz_area_63d(volume))


def vcc_ext_042_lorenz_area_21d_ewm_signal(volume: pd.Series) -> pd.Series:
    """21-day EMA of the 21d Lorenz area (smoothed concentration trend)."""
    la = vcc_ext_036_lorenz_area_21d(volume)
    return _ewm_mean(la, _TD_MON)


def vcc_ext_043_lorenz_area_21d_21d_roc(volume: pd.Series) -> pd.Series:
    """21-day rate-of-change of the 21d Lorenz area."""
    la = vcc_ext_036_lorenz_area_21d(volume)
    return la.diff(_TD_MON)


# Group F (ext_044-051): Effective-N (inverse-HHI)

def vcc_ext_044_effective_n_21d(volume: pd.Series) -> pd.Series:
    """Effective number of trading days (1/HHI) over 21-day window."""
    return volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _effective_n_scalar, raw=True)


def vcc_ext_045_effective_n_63d(volume: pd.Series) -> pd.Series:
    """Effective number of trading days (1/HHI) over 63-day window."""
    return volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        _effective_n_scalar, raw=True)


def vcc_ext_046_effective_n_252d(volume: pd.Series) -> pd.Series:
    """Effective number of trading days (1/HHI) over 252-day window."""
    return volume.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        _effective_n_scalar, raw=True)


def vcc_ext_047_effective_n_21d_norm(volume: pd.Series) -> pd.Series:
    """Effective-N-21d divided by 21 (fraction of fully active days, 0-1 scale)."""
    return _safe_div(vcc_ext_044_effective_n_21d(volume),
                     pd.Series(float(_TD_MON), index=volume.index))


def vcc_ext_048_effective_n_63d_norm(volume: pd.Series) -> pd.Series:
    """Effective-N-63d divided by 63."""
    return _safe_div(vcc_ext_045_effective_n_63d(volume),
                     pd.Series(float(_TD_QTR), index=volume.index))


def vcc_ext_049_effective_n_21d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 21d effective-N within 252-day distribution."""
    en = vcc_ext_044_effective_n_21d(volume)
    m = _rolling_mean(en, _TD_YEAR)
    s = _rolling_std(en, _TD_YEAR)
    return _safe_div(en - m, s)


def vcc_ext_050_effective_n_21d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21d effective-N within 252-day distribution."""
    en = vcc_ext_044_effective_n_21d(volume)
    return en.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vcc_ext_051_effective_n_21d_5d_roc(volume: pd.Series) -> pd.Series:
    """5-day rate-of-change of 21d effective-N (trend in activity breadth)."""
    en = vcc_ext_044_effective_n_21d(volume)
    return en.diff(_TD_WEEK)


# Group G (ext_052-059): Tail-HHI and bottom-share

def vcc_ext_052_tail_hhi_top20pct_21d(volume: pd.Series) -> pd.Series:
    """HHI restricted to the top-20pct volume days over 21-day window."""
    return volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _tail_hhi_scalar(a, 0.20), raw=True)


def vcc_ext_053_tail_hhi_top20pct_63d(volume: pd.Series) -> pd.Series:
    """HHI restricted to the top-20pct volume days over 63-day window."""
    return volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        lambda a: _tail_hhi_scalar(a, 0.20), raw=True)


def vcc_ext_054_tail_hhi_top10pct_63d(volume: pd.Series) -> pd.Series:
    """HHI restricted to the top-10pct volume days over 63-day window."""
    return volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        lambda a: _tail_hhi_scalar(a, 0.10), raw=True)


def vcc_ext_055_bottom20pct_vol_share_21d(volume: pd.Series) -> pd.Series:
    """Share of 21-day total volume in the bottom-20pct lowest-volume days."""
    return volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _bottom_share_scalar(a, 0.20), raw=True)


def vcc_ext_056_bottom20pct_vol_share_63d(volume: pd.Series) -> pd.Series:
    """Share of 63-day total volume in the bottom-20pct lowest-volume days."""
    return volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        lambda a: _bottom_share_scalar(a, 0.20), raw=True)


def vcc_ext_057_top_vs_bottom_20pct_ratio_21d(volume: pd.Series) -> pd.Series:
    """Ratio of top-20pct volume share to bottom-20pct volume share over 21d."""
    def _top20(arr):
        n = len(arr)
        k = max(1, int(np.ceil(n * 0.20)))
        total = arr.sum()
        if total <= _EPS:
            return np.nan
        return float(np.partition(arr, -k)[-k:].sum() / total)
    top = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _top20, raw=True)
    bot = vcc_ext_055_bottom20pct_vol_share_21d(volume)
    return _safe_div(top, bot.clip(lower=_EPS))


def vcc_ext_058_tail_hhi_top20pct_21d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 21d tail-HHI(top20pct) within 252-day distribution."""
    h = vcc_ext_052_tail_hhi_top20pct_21d(volume)
    m = _rolling_mean(h, _TD_YEAR)
    s = _rolling_std(h, _TD_YEAR)
    return _safe_div(h - m, s)


def vcc_ext_059_bottom20pct_vol_share_21d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21d bottom-20pct share within 252-day distribution."""
    s = vcc_ext_055_bottom20pct_vol_share_21d(volume)
    return s.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# Group H (ext_060-067): Volume-weighted return concentration

def vcc_ext_060_vol_weighted_abs_ret_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted average of |daily return| over 21d."""
    ret = close.pct_change().abs().fillna(0.0)
    vw = (volume * ret).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).sum()
    tot = _rolling_sum(volume, _TD_MON)
    return _safe_div(vw, tot)


def vcc_ext_061_vol_weighted_abs_ret_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted average of |daily return| over 63d."""
    ret = close.pct_change().abs().fillna(0.0)
    vw = (volume * ret).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum()
    tot = _rolling_sum(volume, _TD_QTR)
    return _safe_div(vw, tot)


def vcc_ext_062_vol_weighted_neg_ret_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted average of |negative daily returns| over 21d."""
    ret = close.pct_change().fillna(0.0)
    neg_ret = ret.clip(upper=0.0).abs()
    vw = (volume * neg_ret).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).sum()
    tot = _rolling_sum(volume, _TD_MON)
    return _safe_div(vw, tot)


def vcc_ext_063_vol_weighted_neg_ret_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted average of |negative daily returns| over 63d."""
    ret = close.pct_change().fillna(0.0)
    neg_ret = ret.clip(upper=0.0).abs()
    vw = (volume * neg_ret).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum()
    tot = _rolling_sum(volume, _TD_QTR)
    return _safe_div(vw, tot)


def vcc_ext_064_vol_weighted_abs_ret_21d_zscore_252d(
        close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 21d vol-weighted |ret| within 252-day distribution."""
    s = vcc_ext_060_vol_weighted_abs_ret_21d(close, volume)
    m = _rolling_mean(s, _TD_YEAR)
    sd = _rolling_std(s, _TD_YEAR)
    return _safe_div(s - m, sd)


def vcc_ext_065_vol_weighted_neg_ret_21d_pct_rank_252d(
        close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 21d vol-weighted negative-ret in 252-day distribution."""
    s = vcc_ext_062_vol_weighted_neg_ret_21d(close, volume)
    return s.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vcc_ext_066_neg_vs_pos_vol_weighted_ret_ratio_21d(
        close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of vol-weighted |neg-ret| to vol-weighted pos-ret over 21d."""
    ret = close.pct_change().fillna(0.0)
    neg_ret = ret.clip(upper=0.0).abs()
    pos_ret = ret.clip(lower=0.0)
    vw_neg = (volume * neg_ret).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).sum()
    vw_pos = (volume * pos_ret).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).sum()
    return _safe_div(vw_neg, vw_pos.clip(lower=_EPS))


def vcc_ext_067_up_minus_down_vol_share_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Up-day volume share minus down-day volume share over 21d."""
    ret = close.pct_change().fillna(0.0)
    return _up_minus_down_share_loop(volume, ret, _TD_MON)


# Group I (ext_068-075): Short windows, cross-type ratios, and roc

def vcc_ext_068_gini_10d(volume: pd.Series) -> pd.Series:
    """Gini coefficient of volume distribution over 10-day window."""
    w = 10
    return volume.rolling(w, min_periods=max(1, w // 2)).apply(
        _gini_scalar, raw=True)


def vcc_ext_069_hhi_10d(volume: pd.Series) -> pd.Series:
    """Herfindahl index of volume over 10-day window."""
    w = 10
    return volume.rolling(w, min_periods=max(1, w // 2)).apply(
        _hhi_scalar, raw=True)


def vcc_ext_070_effective_n_10d(volume: pd.Series) -> pd.Series:
    """Effective-N (1/HHI) over 10-day window (biweekly breadth)."""
    w = 10
    return volume.rolling(w, min_periods=max(1, w // 2)).apply(
        _effective_n_scalar, raw=True)


def vcc_ext_071_gini_10d_vs_21d_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 10d Gini to 21d Gini (very-short vs short concentration)."""
    g10 = vcc_ext_068_gini_10d(volume)
    g21 = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _gini_scalar, raw=True)
    return _safe_div(g10, g21.clip(lower=_EPS))


def vcc_ext_072_dv_hhi_21d_vs_vol_hhi_21d_ratio(
        close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of dollar-volume HHI-21d to volume HHI-21d (price-weight divergence)."""
    dv_h = vcc_ext_001_dv_hhi_21d(close, volume)
    vol_h = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _hhi_scalar, raw=True)
    return _safe_div(dv_h, vol_h.clip(lower=_EPS))


def vcc_ext_073_dv_gini_21d_vs_vol_gini_21d_diff(
        close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar-volume Gini-21d minus volume Gini-21d (price-weighting effect)."""
    dv_g = vcc_ext_003_dv_gini_21d(close, volume)
    vol_g = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _gini_scalar, raw=True)
    return dv_g - vol_g


def vcc_ext_074_lorenz_area_21d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21d Lorenz area within 252-day distribution."""
    la = vcc_ext_036_lorenz_area_21d(volume)
    return la.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vcc_ext_075_vol_near_low_5pct_21d_5d_roc(
        close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day rate-of-change of 21d near-low-5pct vol share (trend in low-price buying)."""
    s = vcc_ext_018_vol_near_low_5pct_21d(close, low, volume)
    return s.diff(_TD_WEEK)


# -- Registry ------------------------------------------------------------------

VOLUME_CONCENTRATION_EXTENDED_REGISTRY_001_075 = {
    "vcc_ext_001_dv_hhi_21d": {
        "inputs": ["close", "volume"], "func": vcc_ext_001_dv_hhi_21d},
    "vcc_ext_002_dv_hhi_63d": {
        "inputs": ["close", "volume"], "func": vcc_ext_002_dv_hhi_63d},
    "vcc_ext_003_dv_gini_21d": {
        "inputs": ["close", "volume"], "func": vcc_ext_003_dv_gini_21d},
    "vcc_ext_004_dv_gini_63d": {
        "inputs": ["close", "volume"], "func": vcc_ext_004_dv_gini_63d},
    "vcc_ext_005_dv_entropy_21d": {
        "inputs": ["close", "volume"], "func": vcc_ext_005_dv_entropy_21d},
    "vcc_ext_006_dv_entropy_63d": {
        "inputs": ["close", "volume"], "func": vcc_ext_006_dv_entropy_63d},
    "vcc_ext_007_dv_top1_share_21d": {
        "inputs": ["close", "volume"], "func": vcc_ext_007_dv_top1_share_21d},
    "vcc_ext_008_dv_top3_share_21d": {
        "inputs": ["close", "volume"], "func": vcc_ext_008_dv_top3_share_21d},
    "vcc_ext_009_dv_hhi_21d_zscore_252d": {
        "inputs": ["close", "volume"], "func": vcc_ext_009_dv_hhi_21d_zscore_252d},
    "vcc_ext_010_dv_gini_21d_pct_rank_252d": {
        "inputs": ["close", "volume"], "func": vcc_ext_010_dv_gini_21d_pct_rank_252d},
    "vcc_ext_011_top1_worst_ret_vol_share_21d": {
        "inputs": ["close", "volume"], "func": vcc_ext_011_top1_worst_ret_vol_share_21d},
    "vcc_ext_012_top3_worst_ret_vol_share_21d": {
        "inputs": ["close", "volume"], "func": vcc_ext_012_top3_worst_ret_vol_share_21d},
    "vcc_ext_013_top5_worst_ret_vol_share_63d": {
        "inputs": ["close", "volume"], "func": vcc_ext_013_top5_worst_ret_vol_share_63d},
    "vcc_ext_014_top10_worst_ret_vol_share_63d": {
        "inputs": ["close", "volume"], "func": vcc_ext_014_top10_worst_ret_vol_share_63d},
    "vcc_ext_015_top3_worst_ret_vol_share_63d": {
        "inputs": ["close", "volume"], "func": vcc_ext_015_top3_worst_ret_vol_share_63d},
    "vcc_ext_016_top1_worst_ret_vol_share_21d_zscore_252d": {
        "inputs": ["close", "volume"],
        "func": vcc_ext_016_top1_worst_ret_vol_share_21d_zscore_252d},
    "vcc_ext_017_top3_worst_ret_vol_share_21d_pct_rank_252d": {
        "inputs": ["close", "volume"],
        "func": vcc_ext_017_top3_worst_ret_vol_share_21d_pct_rank_252d},
    "vcc_ext_018_vol_near_low_5pct_21d": {
        "inputs": ["close", "low", "volume"], "func": vcc_ext_018_vol_near_low_5pct_21d},
    "vcc_ext_019_vol_near_low_10pct_21d": {
        "inputs": ["close", "low", "volume"], "func": vcc_ext_019_vol_near_low_10pct_21d},
    "vcc_ext_020_vol_near_low_5pct_63d": {
        "inputs": ["close", "low", "volume"], "func": vcc_ext_020_vol_near_low_5pct_63d},
    "vcc_ext_021_vol_near_low_10pct_63d": {
        "inputs": ["close", "low", "volume"], "func": vcc_ext_021_vol_near_low_10pct_63d},
    "vcc_ext_022_vol_near_low_5pct_21d_zscore_252d": {
        "inputs": ["close", "low", "volume"],
        "func": vcc_ext_022_vol_near_low_5pct_21d_zscore_252d},
    "vcc_ext_023_vol_near_low_10pct_21d_pct_rank_252d": {
        "inputs": ["close", "low", "volume"],
        "func": vcc_ext_023_vol_near_low_10pct_21d_pct_rank_252d},
    "vcc_ext_024_vol_near_low_5pct_63d_zscore_252d": {
        "inputs": ["close", "low", "volume"],
        "func": vcc_ext_024_vol_near_low_5pct_63d_zscore_252d},
    "vcc_ext_025_vol_near_low_ratio_21d_vs_63d": {
        "inputs": ["close", "low", "volume"],
        "func": vcc_ext_025_vol_near_low_ratio_21d_vs_63d},
    "vcc_ext_026_renyi_entropy_2_21d": {
        "inputs": ["volume"], "func": vcc_ext_026_renyi_entropy_2_21d},
    "vcc_ext_027_renyi_entropy_2_63d": {
        "inputs": ["volume"], "func": vcc_ext_027_renyi_entropy_2_63d},
    "vcc_ext_028_renyi_entropy_05_21d": {
        "inputs": ["volume"], "func": vcc_ext_028_renyi_entropy_05_21d},
    "vcc_ext_029_tsallis_entropy_2_21d": {
        "inputs": ["volume"], "func": vcc_ext_029_tsallis_entropy_2_21d},
    "vcc_ext_030_tsallis_entropy_2_63d": {
        "inputs": ["volume"], "func": vcc_ext_030_tsallis_entropy_2_63d},
    "vcc_ext_031_tsallis_entropy_05_21d": {
        "inputs": ["volume"], "func": vcc_ext_031_tsallis_entropy_05_21d},
    "vcc_ext_032_renyi_entropy_2_21d_zscore_252d": {
        "inputs": ["volume"], "func": vcc_ext_032_renyi_entropy_2_21d_zscore_252d},
    "vcc_ext_033_renyi_entropy_2_21d_pct_rank_252d": {
        "inputs": ["volume"], "func": vcc_ext_033_renyi_entropy_2_21d_pct_rank_252d},
    "vcc_ext_034_renyi_vs_shannon_ratio_21d": {
        "inputs": ["volume"], "func": vcc_ext_034_renyi_vs_shannon_ratio_21d},
    "vcc_ext_035_tsallis_entropy_2_21d_zscore_252d": {
        "inputs": ["volume"], "func": vcc_ext_035_tsallis_entropy_2_21d_zscore_252d},
    "vcc_ext_036_lorenz_area_21d": {
        "inputs": ["volume"], "func": vcc_ext_036_lorenz_area_21d},
    "vcc_ext_037_lorenz_area_63d": {
        "inputs": ["volume"], "func": vcc_ext_037_lorenz_area_63d},
    "vcc_ext_038_lorenz_area_126d": {
        "inputs": ["volume"], "func": vcc_ext_038_lorenz_area_126d},
    "vcc_ext_039_lorenz_area_21d_zscore_252d": {
        "inputs": ["volume"], "func": vcc_ext_039_lorenz_area_21d_zscore_252d},
    "vcc_ext_040_lorenz_area_63d_pct_rank_252d": {
        "inputs": ["volume"], "func": vcc_ext_040_lorenz_area_63d_pct_rank_252d},
    "vcc_ext_041_lorenz_area_21d_vs_63d_ratio": {
        "inputs": ["volume"], "func": vcc_ext_041_lorenz_area_21d_vs_63d_ratio},
    "vcc_ext_042_lorenz_area_21d_ewm_signal": {
        "inputs": ["volume"], "func": vcc_ext_042_lorenz_area_21d_ewm_signal},
    "vcc_ext_043_lorenz_area_21d_21d_roc": {
        "inputs": ["volume"], "func": vcc_ext_043_lorenz_area_21d_21d_roc},
    "vcc_ext_044_effective_n_21d": {
        "inputs": ["volume"], "func": vcc_ext_044_effective_n_21d},
    "vcc_ext_045_effective_n_63d": {
        "inputs": ["volume"], "func": vcc_ext_045_effective_n_63d},
    "vcc_ext_046_effective_n_252d": {
        "inputs": ["volume"], "func": vcc_ext_046_effective_n_252d},
    "vcc_ext_047_effective_n_21d_norm": {
        "inputs": ["volume"], "func": vcc_ext_047_effective_n_21d_norm},
    "vcc_ext_048_effective_n_63d_norm": {
        "inputs": ["volume"], "func": vcc_ext_048_effective_n_63d_norm},
    "vcc_ext_049_effective_n_21d_zscore_252d": {
        "inputs": ["volume"], "func": vcc_ext_049_effective_n_21d_zscore_252d},
    "vcc_ext_050_effective_n_21d_pct_rank_252d": {
        "inputs": ["volume"], "func": vcc_ext_050_effective_n_21d_pct_rank_252d},
    "vcc_ext_051_effective_n_21d_5d_roc": {
        "inputs": ["volume"], "func": vcc_ext_051_effective_n_21d_5d_roc},
    "vcc_ext_052_tail_hhi_top20pct_21d": {
        "inputs": ["volume"], "func": vcc_ext_052_tail_hhi_top20pct_21d},
    "vcc_ext_053_tail_hhi_top20pct_63d": {
        "inputs": ["volume"], "func": vcc_ext_053_tail_hhi_top20pct_63d},
    "vcc_ext_054_tail_hhi_top10pct_63d": {
        "inputs": ["volume"], "func": vcc_ext_054_tail_hhi_top10pct_63d},
    "vcc_ext_055_bottom20pct_vol_share_21d": {
        "inputs": ["volume"], "func": vcc_ext_055_bottom20pct_vol_share_21d},
    "vcc_ext_056_bottom20pct_vol_share_63d": {
        "inputs": ["volume"], "func": vcc_ext_056_bottom20pct_vol_share_63d},
    "vcc_ext_057_top_vs_bottom_20pct_ratio_21d": {
        "inputs": ["volume"], "func": vcc_ext_057_top_vs_bottom_20pct_ratio_21d},
    "vcc_ext_058_tail_hhi_top20pct_21d_zscore_252d": {
        "inputs": ["volume"], "func": vcc_ext_058_tail_hhi_top20pct_21d_zscore_252d},
    "vcc_ext_059_bottom20pct_vol_share_21d_pct_rank_252d": {
        "inputs": ["volume"], "func": vcc_ext_059_bottom20pct_vol_share_21d_pct_rank_252d},
    "vcc_ext_060_vol_weighted_abs_ret_21d": {
        "inputs": ["close", "volume"], "func": vcc_ext_060_vol_weighted_abs_ret_21d},
    "vcc_ext_061_vol_weighted_abs_ret_63d": {
        "inputs": ["close", "volume"], "func": vcc_ext_061_vol_weighted_abs_ret_63d},
    "vcc_ext_062_vol_weighted_neg_ret_21d": {
        "inputs": ["close", "volume"], "func": vcc_ext_062_vol_weighted_neg_ret_21d},
    "vcc_ext_063_vol_weighted_neg_ret_63d": {
        "inputs": ["close", "volume"], "func": vcc_ext_063_vol_weighted_neg_ret_63d},
    "vcc_ext_064_vol_weighted_abs_ret_21d_zscore_252d": {
        "inputs": ["close", "volume"],
        "func": vcc_ext_064_vol_weighted_abs_ret_21d_zscore_252d},
    "vcc_ext_065_vol_weighted_neg_ret_21d_pct_rank_252d": {
        "inputs": ["close", "volume"],
        "func": vcc_ext_065_vol_weighted_neg_ret_21d_pct_rank_252d},
    "vcc_ext_066_neg_vs_pos_vol_weighted_ret_ratio_21d": {
        "inputs": ["close", "volume"],
        "func": vcc_ext_066_neg_vs_pos_vol_weighted_ret_ratio_21d},
    "vcc_ext_067_up_minus_down_vol_share_21d": {
        "inputs": ["close", "volume"], "func": vcc_ext_067_up_minus_down_vol_share_21d},
    "vcc_ext_068_gini_10d": {
        "inputs": ["volume"], "func": vcc_ext_068_gini_10d},
    "vcc_ext_069_hhi_10d": {
        "inputs": ["volume"], "func": vcc_ext_069_hhi_10d},
    "vcc_ext_070_effective_n_10d": {
        "inputs": ["volume"], "func": vcc_ext_070_effective_n_10d},
    "vcc_ext_071_gini_10d_vs_21d_ratio": {
        "inputs": ["volume"], "func": vcc_ext_071_gini_10d_vs_21d_ratio},
    "vcc_ext_072_dv_hhi_21d_vs_vol_hhi_21d_ratio": {
        "inputs": ["close", "volume"],
        "func": vcc_ext_072_dv_hhi_21d_vs_vol_hhi_21d_ratio},
    "vcc_ext_073_dv_gini_21d_vs_vol_gini_21d_diff": {
        "inputs": ["close", "volume"],
        "func": vcc_ext_073_dv_gini_21d_vs_vol_gini_21d_diff},
    "vcc_ext_074_lorenz_area_21d_pct_rank_252d": {
        "inputs": ["volume"], "func": vcc_ext_074_lorenz_area_21d_pct_rank_252d},
    "vcc_ext_075_vol_near_low_5pct_21d_5d_roc": {
        "inputs": ["close", "low", "volume"],
        "func": vcc_ext_075_vol_near_low_5pct_21d_5d_roc},
}
