"""
21_volume_concentration — Base Features 076-150 (extended to 200)
Domain: concentration / inequality of volume distribution across days within a window —
        down-day concentration, up-day concentration, conditional shares, tail measures.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

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


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _topn_share(arr: np.ndarray, n: int) -> float:
    """Share of total held by top-n values."""
    total = arr.sum()
    if total <= 0:
        return np.nan
    top = np.partition(arr, -min(n, len(arr)))[-min(n, len(arr)):]
    return float(top.sum() / total)


def _herfindahl(arr: np.ndarray) -> float:
    """Herfindahl index of the volume distribution."""
    total = arr.sum()
    if total <= 0:
        return np.nan
    shares = arr / total
    return float((shares ** 2).sum())


def _gini(arr: np.ndarray) -> float:
    """Gini coefficient of the volume distribution."""
    n = len(arr)
    if n < 2:
        return np.nan
    s = arr.sum()
    if s <= 0:
        return np.nan
    sorted_a = np.sort(arr)
    idx = np.arange(1, n + 1)
    return float((2 * (idx * sorted_a).sum() - (n + 1) * s) / (n * s))


def _entropy(arr: np.ndarray) -> float:
    """Shannon entropy (nats) of volume shares."""
    total = arr.sum()
    if total <= 0:
        return np.nan
    shares = arr / total
    shares = shares[shares > 0]
    return float(-(shares * np.log(shares)).sum())


def _days_to_pct(arr: np.ndarray, pct: float) -> float:
    """Min number of largest days needed to account for pct of total volume."""
    total = arr.sum()
    if total <= 0:
        return np.nan
    sorted_d = np.sort(arr)[::-1]
    cumfrac = np.cumsum(sorted_d) / total
    hits = np.searchsorted(cumfrac, pct) + 1
    return float(min(hits, len(arr)))


def _cv(arr: np.ndarray) -> float:
    """Coefficient of variation (std/mean) of arr."""
    m = arr.mean()
    if m <= 0:
        return np.nan
    return float(arr.std() / m)


def _pareto_ratio(arr: np.ndarray, top_frac: float) -> float:
    """Share of total volume in top top_frac fraction of days."""
    n = len(arr)
    if n < 2:
        return np.nan
    k = max(1, int(np.ceil(n * top_frac)))
    top = np.partition(arr, -k)[-k:]
    total = arr.sum()
    if total <= 0:
        return np.nan
    return float(top.sum() / total)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-085): Conditional concentration on down-price days ---

def vcc_076_top1_share_21d_down_days(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Top-1 volume share within 21d, computed only over down-price days."""
    down_vol = volume.where(close < close.shift(1), 0.0)
    return down_vol.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _topn_share(a[a > 0], 1) if (a > 0).sum() > 0 else np.nan, raw=True)


def vcc_077_hhi_21d_down_days(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Herfindahl index of volume distribution restricted to 21d down-price days."""
    down_vol = volume.where(close < close.shift(1), 0.0)
    return down_vol.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _herfindahl(a[a > 0]) if (a > 0).sum() > 1 else np.nan, raw=True)


def vcc_078_gini_21d_down_days(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Gini coefficient of volume distribution restricted to 21d down-price days."""
    down_vol = volume.where(close < close.shift(1), 0.0)
    return down_vol.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _gini(a[a > 0]) if (a > 0).sum() > 1 else np.nan, raw=True)


def vcc_079_entropy_21d_down_days(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Shannon entropy of volume distribution restricted to 21d down-price days."""
    down_vol = volume.where(close < close.shift(1), 0.0)
    return down_vol.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _entropy(a[a > 0]) if (a > 0).sum() > 1 else np.nan, raw=True)


def vcc_080_top1_share_63d_down_days(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Top-1 volume share restricted to 63d down-price days."""
    down_vol = volume.where(close < close.shift(1), 0.0)
    return down_vol.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        lambda a: _topn_share(a[a > 0], 1) if (a > 0).sum() > 0 else np.nan, raw=True)


def vcc_081_hhi_63d_down_days(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Herfindahl index of volume distribution restricted to 63d down-price days."""
    down_vol = volume.where(close < close.shift(1), 0.0)
    return down_vol.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        lambda a: _herfindahl(a[a > 0]) if (a > 0).sum() > 1 else np.nan, raw=True)


def vcc_082_gini_63d_down_days(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Gini coefficient of volume restricted to 63d down-price days."""
    down_vol = volume.where(close < close.shift(1), 0.0)
    return down_vol.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        lambda a: _gini(a[a > 0]) if (a > 0).sum() > 1 else np.nan, raw=True)


def vcc_083_down_day_vol_share_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 21-day total volume occurring on down-price days."""
    down_vol = volume.where(close < close.shift(1), 0.0)
    tot = _rolling_sum(volume, _TD_MON)
    dn_tot = _rolling_sum(down_vol, _TD_MON)
    return _safe_div(dn_tot, tot)


def vcc_084_down_day_vol_share_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 63-day total volume occurring on down-price days."""
    down_vol = volume.where(close < close.shift(1), 0.0)
    tot = _rolling_sum(volume, _TD_QTR)
    dn_tot = _rolling_sum(down_vol, _TD_QTR)
    return _safe_div(dn_tot, tot)


def vcc_085_down_day_vol_share_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 252-day total volume occurring on down-price days."""
    down_vol = volume.where(close < close.shift(1), 0.0)
    tot = _rolling_sum(volume, _TD_YEAR)
    dn_tot = _rolling_sum(down_vol, _TD_YEAR)
    return _safe_div(dn_tot, tot)


# --- Group I (086-095): Conditional concentration on up-price days ---

def vcc_086_top1_share_21d_up_days(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Top-1 volume share restricted to 21d up-price days."""
    up_vol = volume.where(close > close.shift(1), 0.0)
    return up_vol.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _topn_share(a[a > 0], 1) if (a > 0).sum() > 0 else np.nan, raw=True)


def vcc_087_hhi_21d_up_days(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Herfindahl index of volume restricted to 21d up-price days."""
    up_vol = volume.where(close > close.shift(1), 0.0)
    return up_vol.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _herfindahl(a[a > 0]) if (a > 0).sum() > 1 else np.nan, raw=True)


def vcc_088_gini_21d_up_days(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Gini coefficient of volume restricted to 21d up-price days."""
    up_vol = volume.where(close > close.shift(1), 0.0)
    return up_vol.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _gini(a[a > 0]) if (a > 0).sum() > 1 else np.nan, raw=True)


def vcc_089_up_day_vol_share_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 21-day total volume occurring on up-price days."""
    up_vol = volume.where(close > close.shift(1), 0.0)
    tot = _rolling_sum(volume, _TD_MON)
    up_tot = _rolling_sum(up_vol, _TD_MON)
    return _safe_div(up_tot, tot)


def vcc_090_up_day_vol_share_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 63-day total volume occurring on up-price days."""
    up_vol = volume.where(close > close.shift(1), 0.0)
    tot = _rolling_sum(volume, _TD_QTR)
    up_tot = _rolling_sum(up_vol, _TD_QTR)
    return _safe_div(up_tot, tot)


def vcc_091_down_vs_up_vol_share_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of down-day volume share to up-day volume share over 21 days."""
    dn = vcc_083_down_day_vol_share_21d(close, volume)
    up = vcc_089_up_day_vol_share_21d(close, volume)
    return _safe_div(dn, up)


def vcc_092_down_vs_up_vol_share_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of down-day volume share to up-day volume share over 63 days."""
    dn = vcc_084_down_day_vol_share_63d(close, volume)
    up = vcc_090_up_day_vol_share_63d(close, volume)
    return _safe_div(dn, up)


def vcc_093_down_day_hhi_vs_total_hhi_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of down-day HHI to all-day HHI over 21d (selective concentration)."""
    dn_hhi = vcc_077_hhi_21d_down_days(close, volume)
    all_hhi = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _herfindahl, raw=True)
    return _safe_div(dn_hhi, all_hhi)


def vcc_094_down_day_gini_vs_total_gini_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of down-day Gini to all-day Gini over 21d."""
    dn_gini = vcc_078_gini_21d_down_days(close, volume)
    all_gini = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _gini, raw=True)
    return _safe_div(dn_gini, all_gini)


def vcc_095_down_day_vol_share_21d_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 21-day down-day volume share within trailing 252-day distribution."""
    s = vcc_083_down_day_vol_share_21d(close, volume)
    m = _rolling_mean(s, _TD_YEAR)
    sd = _rolling_std(s, _TD_YEAR)
    return _safe_div(s - m, sd)


# --- Group J (096-105): Volume coefficient of variation and dispersion ---

def vcc_096_cv_21d(volume: pd.Series) -> pd.Series:
    """Coefficient of variation (std/mean) of daily volume over 21-day window."""
    return volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _cv, raw=True)


def vcc_097_cv_63d(volume: pd.Series) -> pd.Series:
    """Coefficient of variation of daily volume over 63-day window."""
    return volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        _cv, raw=True)


def vcc_098_cv_126d(volume: pd.Series) -> pd.Series:
    """Coefficient of variation of daily volume over 126-day window."""
    return volume.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(
        _cv, raw=True)


def vcc_099_cv_252d(volume: pd.Series) -> pd.Series:
    """Coefficient of variation of daily volume over 252-day window."""
    return volume.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        _cv, raw=True)


def vcc_100_cv_21d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 21-day CV within trailing 252-day distribution."""
    cv = vcc_096_cv_21d(volume)
    m = _rolling_mean(cv, _TD_YEAR)
    s = _rolling_std(cv, _TD_YEAR)
    return _safe_div(cv - m, s)


def vcc_101_cv_21d_vs_252d_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day CV to 252-day CV (short-run vs long-run dispersion)."""
    return _safe_div(vcc_096_cv_21d(volume), vcc_099_cv_252d(volume))


def vcc_102_cv_63d_vs_252d_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 63-day CV to 252-day CV."""
    return _safe_div(vcc_097_cv_63d(volume), vcc_099_cv_252d(volume))


def vcc_103_vol_iqr_ratio_21d(volume: pd.Series) -> pd.Series:
    """IQR / median of daily volume over 21 days (robust dispersion)."""
    q75 = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.75)
    q25 = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.25)
    med = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).median()
    return _safe_div(q75 - q25, med)


def vcc_104_vol_iqr_ratio_63d(volume: pd.Series) -> pd.Series:
    """IQR / median of daily volume over 63 days."""
    q75 = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.75)
    q25 = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.25)
    med = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).median()
    return _safe_div(q75 - q25, med)


def vcc_105_vol_90th_10th_ratio_21d(volume: pd.Series) -> pd.Series:
    """90th-percentile to 10th-percentile volume ratio over 21 days."""
    q90 = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.90)
    q10 = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.10)
    return _safe_div(q90, q10)


# --- Group K (106-115): Pareto-style top-fraction share ---

def vcc_106_pareto_top20pct_share_21d(volume: pd.Series) -> pd.Series:
    """Share of 21d total volume in the top-20% highest-volume days."""
    return volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _pareto_ratio(a, 0.20), raw=True)


def vcc_107_pareto_top20pct_share_63d(volume: pd.Series) -> pd.Series:
    """Share of 63d total volume in the top-20% highest-volume days."""
    return volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        lambda a: _pareto_ratio(a, 0.20), raw=True)


def vcc_108_pareto_top10pct_share_21d(volume: pd.Series) -> pd.Series:
    """Share of 21d total volume in the top-10% highest-volume days."""
    return volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _pareto_ratio(a, 0.10), raw=True)


def vcc_109_pareto_top10pct_share_63d(volume: pd.Series) -> pd.Series:
    """Share of 63d total volume in the top-10% highest-volume days."""
    return volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        lambda a: _pareto_ratio(a, 0.10), raw=True)


def vcc_110_pareto_top10pct_share_252d(volume: pd.Series) -> pd.Series:
    """Share of 252d total volume in the top-10% highest-volume days."""
    return volume.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        lambda a: _pareto_ratio(a, 0.10), raw=True)


def vcc_111_pareto_top20pct_share_252d(volume: pd.Series) -> pd.Series:
    """Share of 252d total volume in the top-20% highest-volume days."""
    return volume.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        lambda a: _pareto_ratio(a, 0.20), raw=True)


def vcc_112_pareto_top20pct_share_21d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 21d top-20%-share within 252-day distribution."""
    r = vcc_106_pareto_top20pct_share_21d(volume)
    m = _rolling_mean(r, _TD_YEAR)
    s = _rolling_std(r, _TD_YEAR)
    return _safe_div(r - m, s)


def vcc_113_pareto_top10pct_share_21d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21d top-10%-share within 252-day distribution."""
    r = vcc_108_pareto_top10pct_share_21d(volume)
    return r.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vcc_114_pareto_top20pct_21d_vs_252d_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 21d top-20%-share to 252d top-20%-share."""
    return _safe_div(vcc_106_pareto_top20pct_share_21d(volume),
                     vcc_111_pareto_top20pct_share_252d(volume))


def vcc_115_pareto_top10pct_21d_vs_252d_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 21d top-10%-share to 252d top-10%-share."""
    return _safe_div(vcc_108_pareto_top10pct_share_21d(volume),
                     vcc_110_pareto_top10pct_share_252d(volume))


# --- Group L (116-125): Volume tail ratios (max-cluster vs rest) ---

def vcc_116_top2_vs_bottom2_ratio_21d(volume: pd.Series) -> pd.Series:
    """Sum of top-2 volume days divided by sum of bottom-2 volume days (21d)."""
    def _ratio(arr):
        if len(arr) < 4:
            return np.nan
        s = arr.sum()
        if s <= 0:
            return np.nan
        top2 = np.partition(arr, -2)[-2:].sum()
        bot2 = np.partition(arr, 2)[:2].sum()
        if bot2 <= 0:
            return np.nan
        return float(top2 / bot2)
    return volume.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(
        _ratio, raw=True)


def vcc_117_top5_vs_bottom5_ratio_63d(volume: pd.Series) -> pd.Series:
    """Sum of top-5 volume days divided by sum of bottom-5 volume days (63d)."""
    def _ratio(arr):
        if len(arr) < 10:
            return np.nan
        top5 = np.partition(arr, -5)[-5:].sum()
        bot5 = np.partition(arr, 5)[:5].sum()
        if bot5 <= 0:
            return np.nan
        return float(top5 / bot5)
    return volume.rolling(_TD_QTR, min_periods=max(10, _TD_QTR // 2)).apply(
        _ratio, raw=True)


def vcc_118_max_day_vs_min_day_ratio_21d(volume: pd.Series) -> pd.Series:
    """Ratio of maximum to minimum daily volume over 21-day window."""
    mx = _rolling_max(volume, _TD_MON)
    mn = _rolling_min(volume, _TD_MON)
    return _safe_div(mx, mn)


def vcc_119_max_day_vs_min_day_ratio_63d(volume: pd.Series) -> pd.Series:
    """Ratio of maximum to minimum daily volume over 63-day window."""
    mx = _rolling_max(volume, _TD_QTR)
    mn = _rolling_min(volume, _TD_QTR)
    return _safe_div(mx, mn)


def vcc_120_max_day_vs_min_day_ratio_252d(volume: pd.Series) -> pd.Series:
    """Ratio of maximum to minimum daily volume over 252-day window."""
    mx = _rolling_max(volume, _TD_YEAR)
    mn = _rolling_min(volume, _TD_YEAR)
    return _safe_div(mx, mn)


def vcc_121_top3_share_21d_expanding_max(volume: pd.Series) -> pd.Series:
    """Expanding all-time maximum of 21-day top-3 volume share."""
    r = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _topn_share(a, 3), raw=True)
    return r.expanding(min_periods=1).max()


def vcc_122_hhi_21d_expanding_max(volume: pd.Series) -> pd.Series:
    """Expanding all-time maximum of 21-day HHI (peak concentration record)."""
    r = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _herfindahl, raw=True)
    return r.expanding(min_periods=1).max()


def vcc_123_top1_share_21d_expanding_rank(volume: pd.Series) -> pd.Series:
    """Expanding percentile rank of 21-day top-1 share (all-history extremity)."""
    r = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _topn_share(a, 1), raw=True)
    return r.expanding(min_periods=5).rank(pct=True)


def vcc_124_gini_21d_expanding_rank(volume: pd.Series) -> pd.Series:
    """Expanding percentile rank of 21-day Gini."""
    r = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _gini, raw=True)
    return r.expanding(min_periods=5).rank(pct=True)


def vcc_125_days_to_90pct_21d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of days-to-90%-of-21d-vol within 252-day distribution."""
    d = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _days_to_pct(a, 0.90), raw=True)
    return d.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group M (126-135): High-volume day count and threshold features ---

def vcc_126_days_above_2x_mean_21d(volume: pd.Series) -> pd.Series:
    """Count of days in 21d window where volume > 2x the 21d mean volume."""
    mean21 = _rolling_mean(volume, _TD_MON)
    above = (volume > 2.0 * mean21).astype(float)
    return _rolling_sum(above, _TD_MON)


def vcc_127_days_above_2x_mean_63d(volume: pd.Series) -> pd.Series:
    """Count of days in 63d window where volume > 2x the 63d mean volume."""
    mean63 = _rolling_mean(volume, _TD_QTR)
    above = (volume > 2.0 * mean63).astype(float)
    return _rolling_sum(above, _TD_QTR)


def vcc_128_days_above_3x_mean_21d(volume: pd.Series) -> pd.Series:
    """Count of days in 21d window where volume > 3x the 21d mean volume."""
    mean21 = _rolling_mean(volume, _TD_MON)
    above = (volume > 3.0 * mean21).astype(float)
    return _rolling_sum(above, _TD_MON)


def vcc_129_share_of_days_above_2x_mean_21d(volume: pd.Series) -> pd.Series:
    """Fraction of 21d days with volume > 2x mean (concentration-by-count)."""
    mean21 = _rolling_mean(volume, _TD_MON)
    above = (volume > 2.0 * mean21).astype(float)
    return _rolling_sum(above, _TD_MON) / _TD_MON


def vcc_130_share_of_days_above_2x_mean_63d(volume: pd.Series) -> pd.Series:
    """Fraction of 63d days with volume > 2x mean."""
    mean63 = _rolling_mean(volume, _TD_QTR)
    above = (volume > 2.0 * mean63).astype(float)
    return _rolling_sum(above, _TD_QTR) / _TD_QTR


def vcc_131_high_vol_day_share_of_total_21d(volume: pd.Series) -> pd.Series:
    """Volume on days >2x mean as fraction of 21d total volume."""
    mean21 = _rolling_mean(volume, _TD_MON)
    high_vol = volume.where(volume > 2.0 * mean21, 0.0)
    tot = _rolling_sum(volume, _TD_MON)
    high_tot = _rolling_sum(high_vol, _TD_MON)
    return _safe_div(high_tot, tot)


def vcc_132_high_vol_day_share_of_total_63d(volume: pd.Series) -> pd.Series:
    """Volume on days >2x mean as fraction of 63d total volume."""
    mean63 = _rolling_mean(volume, _TD_QTR)
    high_vol = volume.where(volume > 2.0 * mean63, 0.0)
    tot = _rolling_sum(volume, _TD_QTR)
    high_tot = _rolling_sum(high_vol, _TD_QTR)
    return _safe_div(high_tot, tot)


def vcc_133_high_vol_day_share_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 21d high-vol-day share within 252-day distribution."""
    s = vcc_131_high_vol_day_share_of_total_21d(volume)
    m = _rolling_mean(s, _TD_YEAR)
    sd = _rolling_std(s, _TD_YEAR)
    return _safe_div(s - m, sd)


def vcc_134_days_below_half_mean_21d(volume: pd.Series) -> pd.Series:
    """Count of days with volume < 0.5x mean in 21d window (low-activity days)."""
    mean21 = _rolling_mean(volume, _TD_MON)
    below = (volume < 0.5 * mean21).astype(float)
    return _rolling_sum(below, _TD_MON)


def vcc_135_high_to_low_vol_day_count_ratio_21d(volume: pd.Series) -> pd.Series:
    """Count(vol>2x mean) / count(vol<0.5x mean) over 21d."""
    mean21 = _rolling_mean(volume, _TD_MON)
    high = _rolling_sum((volume > 2.0 * mean21).astype(float), _TD_MON)
    low = _rolling_sum((volume < 0.5 * mean21).astype(float), _TD_MON)
    return _safe_div(high, low)


# --- Group N (136-145): Concentration composite and z-score indices ---

def vcc_136_concentration_index_21d(volume: pd.Series) -> pd.Series:
    """Equal-weight composite of HHI-21d, Gini-21d, and top-3-share-21d."""
    h = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _herfindahl, raw=True)
    g = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _gini, raw=True)
    t = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _topn_share(a, 3), raw=True)
    h_n = h * _TD_MON
    return (h_n + g + t) / 3.0


def vcc_137_concentration_index_63d(volume: pd.Series) -> pd.Series:
    """Equal-weight composite of HHI-63d, Gini-63d, and top-5-share-63d."""
    h = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        _herfindahl, raw=True)
    g = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        _gini, raw=True)
    t = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        lambda a: _topn_share(a, 5), raw=True)
    h_n = h * _TD_QTR
    return (h_n + g + t) / 3.0


def vcc_138_concentration_index_21d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 21-day concentration composite within 252-day distribution."""
    ci = vcc_136_concentration_index_21d(volume)
    m = _rolling_mean(ci, _TD_YEAR)
    s = _rolling_std(ci, _TD_YEAR)
    return _safe_div(ci - m, s)


def vcc_139_concentration_index_63d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 63-day concentration composite within 252-day distribution."""
    ci = vcc_137_concentration_index_63d(volume)
    m = _rolling_mean(ci, _TD_YEAR)
    s = _rolling_std(ci, _TD_YEAR)
    return _safe_div(ci - m, s)


def vcc_140_concentration_index_21d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21d concentration composite in 252d distribution."""
    ci = vcc_136_concentration_index_21d(volume)
    return ci.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vcc_141_concentration_index_21d_vs_63d_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 21d concentration index to 63d concentration index."""
    return _safe_div(vcc_136_concentration_index_21d(volume),
                     vcc_137_concentration_index_63d(volume))


def vcc_142_concentration_index_21d_ewm(volume: pd.Series) -> pd.Series:
    """21-day EMA of the 21-day concentration index (smoothed signal)."""
    ci = vcc_136_concentration_index_21d(volume)
    return _ewm_mean(ci, _TD_MON)


def vcc_143_concentration_index_21d_expanding_max(volume: pd.Series) -> pd.Series:
    """Expanding all-time maximum of 21d concentration index."""
    ci = vcc_136_concentration_index_21d(volume)
    return ci.expanding(min_periods=1).max()


def vcc_144_top1_share_21d_gt_threshold_flag(volume: pd.Series) -> pd.Series:
    """Flag: 21d top-1-share exceeds 0.25 (single day has 25%+ of period volume)."""
    r = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _topn_share(a, 1), raw=True)
    return (r > 0.25).astype(float)


def vcc_145_hhi_21d_gt_2x_uniform_flag(volume: pd.Series) -> pd.Series:
    """Flag: 21d HHI exceeds 2x the uniform benchmark (highly concentrated window)."""
    hhi = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _herfindahl, raw=True)
    return (hhi > 2.0 / _TD_MON).astype(float)


# --- Group O (146-150): Multi-input conditional concentration ---

def vcc_146_top3_down_vol_share_of_total_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume on top-3 down-price days as fraction of 21d total volume."""
    down_vol = volume.where(close < close.shift(1), 0.0)
    def _top3_ratio(a):
        total = a.sum()
        if total <= 0:
            return np.nan
        nz = a[a > 0]
        if len(nz) == 0:
            return np.nan
        top3 = np.partition(nz, -min(3, len(nz)))[-min(3, len(nz)):].sum()
        return float(top3 / total)
    return down_vol.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _top3_ratio, raw=True)


def vcc_147_top3_up_vol_share_of_total_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume on top-3 up-price days as fraction of 21d total volume."""
    up_vol = volume.where(close > close.shift(1), 0.0)
    def _top3_ratio(a):
        total = a.sum()
        if total <= 0:
            return np.nan
        nz = a[a > 0]
        if len(nz) == 0:
            return np.nan
        top3 = np.partition(nz, -min(3, len(nz)))[-min(3, len(nz)):].sum()
        return float(top3 / total)
    return up_vol.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _top3_ratio, raw=True)


def vcc_148_down_top3_vs_up_top3_vol_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of top-3 down-day volume share to top-3 up-day volume share (21d)."""
    dn = vcc_146_top3_down_vol_share_of_total_21d(close, volume)
    up = vcc_147_top3_up_vol_share_of_total_21d(close, volume)
    return _safe_div(dn, up)


def vcc_149_concentration_index_21d_pct_rank_504d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21d concentration index in trailing 504-day distribution."""
    ci = vcc_136_concentration_index_21d(volume)
    return ci.rolling(504, min_periods=_TD_YEAR // 2).rank(pct=True)


def vcc_150_hhi_21d_expanding_zscore(volume: pd.Series) -> pd.Series:
    """Expanding z-score of 21-day HHI (all-history extremity of concentration)."""
    hhi = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _herfindahl, raw=True)
    m = hhi.expanding(min_periods=5).mean()
    s = hhi.expanding(min_periods=5).std()
    return _safe_div(hhi - m, s)


# --- Group P (176-200): New constructions — vol acceleration, range-conditioned, multi-window ---

def vcc_176_vol_acceleration_21d(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day total volume to prior 21-day total volume (vol acceleration)."""
    tot = _rolling_sum(volume, _TD_MON)
    return _safe_div(tot, tot.shift(_TD_MON))


def vcc_177_vol_acceleration_63d(volume: pd.Series) -> pd.Series:
    """Ratio of 63-day total volume to prior 63-day total volume."""
    tot = _rolling_sum(volume, _TD_QTR)
    return _safe_div(tot, tot.shift(_TD_QTR))


def vcc_178_down_day_cv_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """CV (std/mean) of volume restricted to 21d down-price days."""
    down_vol = volume.where(close < close.shift(1), 0.0)
    return down_vol.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _cv(a[a > 0]) if (a > 0).sum() > 1 else np.nan, raw=True)


def vcc_179_up_day_cv_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """CV (std/mean) of volume restricted to 21d up-price days."""
    up_vol = volume.where(close > close.shift(1), 0.0)
    return up_vol.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _cv(a[a > 0]) if (a > 0).sum() > 1 else np.nan, raw=True)


def vcc_180_down_day_cv_vs_up_day_cv_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of down-day CV to up-day CV over 21d (asymmetric dispersion)."""
    return _safe_div(vcc_178_down_day_cv_21d(close, volume),
                     vcc_179_up_day_cv_21d(close, volume))


def vcc_181_large_range_day_vol_share_21d(close: pd.Series, high: pd.Series,
                                           low: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume on days with range > 2x mean daily range as share of 21d total."""
    rng = high - low
    mean_rng = _rolling_mean(rng, _TD_MON)
    large_vol = volume.where(rng > 2.0 * mean_rng, 0.0)
    tot = _rolling_sum(volume, _TD_MON)
    return _safe_div(_rolling_sum(large_vol, _TD_MON), tot)


def vcc_182_large_range_day_vol_share_63d(close: pd.Series, high: pd.Series,
                                           low: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume on days with range > 2x mean daily range as share of 63d total."""
    rng = high - low
    mean_rng = _rolling_mean(rng, _TD_QTR)
    large_vol = volume.where(rng > 2.0 * mean_rng, 0.0)
    tot = _rolling_sum(volume, _TD_QTR)
    return _safe_div(_rolling_sum(large_vol, _TD_QTR), tot)


def vcc_183_small_range_day_vol_share_21d(close: pd.Series, high: pd.Series,
                                           low: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume on days with range < 0.5x mean daily range as share of 21d total."""
    rng = high - low
    mean_rng = _rolling_mean(rng, _TD_MON)
    small_vol = volume.where(rng < 0.5 * mean_rng, 0.0)
    tot = _rolling_sum(volume, _TD_MON)
    return _safe_div(_rolling_sum(small_vol, _TD_MON), tot)


def vcc_184_hhi_21d_pct_rank_126d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day HHI within trailing 126-day distribution."""
    hhi = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _herfindahl, raw=True)
    return hhi.rolling(_TD_HALF, min_periods=_TD_QTR // 2).rank(pct=True)


def vcc_185_gini_21d_pct_rank_126d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day Gini within trailing 126-day distribution."""
    g = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _gini, raw=True)
    return g.rolling(_TD_HALF, min_periods=_TD_QTR // 2).rank(pct=True)


def vcc_186_vol_75th_25th_ratio_21d(volume: pd.Series) -> pd.Series:
    """75th-percentile to 25th-percentile volume ratio over 21 days."""
    q75 = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.75)
    q25 = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.25)
    return _safe_div(q75, q25)


def vcc_187_vol_75th_25th_ratio_63d(volume: pd.Series) -> pd.Series:
    """75th-percentile to 25th-percentile volume ratio over 63 days."""
    q75 = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.75)
    q25 = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.25)
    return _safe_div(q75, q25)


def vcc_188_top1_share_126d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 126-day top-1 share in trailing 252-day distribution."""
    r = volume.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(
        lambda a: _topn_share(a, 1), raw=True)
    return r.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vcc_189_concentration_index_252d(volume: pd.Series) -> pd.Series:
    """Equal-weight composite of HHI-252d, Gini-252d, and top-10-share-252d."""
    h = volume.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        _herfindahl, raw=True)
    g = volume.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        _gini, raw=True)
    t = volume.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        lambda a: _topn_share(a, 10), raw=True)
    h_n = h * _TD_YEAR
    return (h_n + g + t) / 3.0


def vcc_190_concentration_21d_vs_252d_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 21d concentration index to 252d concentration index."""
    ci21 = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _herfindahl, raw=True) * _TD_MON
    ci252 = vcc_189_concentration_index_252d(volume)
    return _safe_div(ci21, ci252)


def vcc_191_days_above_4x_mean_21d(volume: pd.Series) -> pd.Series:
    """Count of days in 21d window where volume > 4x the 21d mean volume."""
    mean21 = _rolling_mean(volume, _TD_MON)
    above = (volume > 4.0 * mean21).astype(float)
    return _rolling_sum(above, _TD_MON)


def vcc_192_days_above_3x_mean_63d(volume: pd.Series) -> pd.Series:
    """Count of days in 63d window where volume > 3x the 63d mean volume."""
    mean63 = _rolling_mean(volume, _TD_QTR)
    above = (volume > 3.0 * mean63).astype(float)
    return _rolling_sum(above, _TD_QTR)


def vcc_193_top5_share_21d_ewm_63(volume: pd.Series) -> pd.Series:
    """EWM(span=63) of 21-day top-5 share — smoothed concentration signal."""
    r = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _topn_share(a, 5), raw=True)
    return _ewm_mean(r, _TD_QTR)


def vcc_194_hhi_252d_pct_rank_expanding(volume: pd.Series) -> pd.Series:
    """Expanding percentile rank of 252-day HHI (all-history extremity)."""
    hhi = volume.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        _herfindahl, raw=True)
    return hhi.expanding(min_periods=5).rank(pct=True)


def vcc_195_vol_iqr_ratio_252d(volume: pd.Series) -> pd.Series:
    """IQR / median of daily volume over 252 days (long-run robust dispersion)."""
    q75 = volume.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.75)
    q25 = volume.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.25)
    med = volume.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).median()
    return _safe_div(q75 - q25, med)


def vcc_196_up_day_hhi_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Herfindahl index of volume distribution restricted to 63d up-price days."""
    up_vol = volume.where(close > close.shift(1), 0.0)
    return up_vol.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        lambda a: _herfindahl(a[a > 0]) if (a > 0).sum() > 1 else np.nan, raw=True)


def vcc_197_down_up_hhi_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 63d down-day HHI to 63d up-day HHI (panic vs accumulation concentration)."""
    dn = volume.where(close < close.shift(1), 0.0)
    up = volume.where(close > close.shift(1), 0.0)
    dn_hhi = dn.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        lambda a: _herfindahl(a[a > 0]) if (a > 0).sum() > 1 else np.nan, raw=True)
    up_hhi = up.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        lambda a: _herfindahl(a[a > 0]) if (a > 0).sum() > 1 else np.nan, raw=True)
    return _safe_div(dn_hhi, up_hhi)


def vcc_198_down_day_entropy_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Shannon entropy of volume distribution restricted to 63d down-price days."""
    down_vol = volume.where(close < close.shift(1), 0.0)
    return down_vol.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        lambda a: _entropy(a[a > 0]) if (a > 0).sum() > 1 else np.nan, raw=True)


def vcc_199_high_vol_share_of_total_252d(volume: pd.Series) -> pd.Series:
    """Volume on days >2x 252d mean as fraction of 252d total volume."""
    mean252 = _rolling_mean(volume, _TD_YEAR)
    high_vol = volume.where(volume > 2.0 * mean252, 0.0)
    tot = _rolling_sum(volume, _TD_YEAR)
    return _safe_div(_rolling_sum(high_vol, _TD_YEAR), tot)


def vcc_200_pareto_top5pct_share_63d(volume: pd.Series) -> pd.Series:
    """Share of 63d total volume in the top-5% highest-volume days."""
    def _par5(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        k = max(1, int(np.ceil(n * 0.05)))
        top = np.partition(arr, -k)[-k:]
        total = arr.sum()
        if total <= 0:
            return np.nan
        return float(top.sum() / total)
    return volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        _par5, raw=True)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_CONCENTRATION_REGISTRY_076_150 = {
    "vcc_076_top1_share_21d_down_days": {"inputs": ["close", "volume"], "func": vcc_076_top1_share_21d_down_days},
    "vcc_077_hhi_21d_down_days": {"inputs": ["close", "volume"], "func": vcc_077_hhi_21d_down_days},
    "vcc_078_gini_21d_down_days": {"inputs": ["close", "volume"], "func": vcc_078_gini_21d_down_days},
    "vcc_079_entropy_21d_down_days": {"inputs": ["close", "volume"], "func": vcc_079_entropy_21d_down_days},
    "vcc_080_top1_share_63d_down_days": {"inputs": ["close", "volume"], "func": vcc_080_top1_share_63d_down_days},
    "vcc_081_hhi_63d_down_days": {"inputs": ["close", "volume"], "func": vcc_081_hhi_63d_down_days},
    "vcc_082_gini_63d_down_days": {"inputs": ["close", "volume"], "func": vcc_082_gini_63d_down_days},
    "vcc_083_down_day_vol_share_21d": {"inputs": ["close", "volume"], "func": vcc_083_down_day_vol_share_21d},
    "vcc_084_down_day_vol_share_63d": {"inputs": ["close", "volume"], "func": vcc_084_down_day_vol_share_63d},
    "vcc_085_down_day_vol_share_252d": {"inputs": ["close", "volume"], "func": vcc_085_down_day_vol_share_252d},
    "vcc_086_top1_share_21d_up_days": {"inputs": ["close", "volume"], "func": vcc_086_top1_share_21d_up_days},
    "vcc_087_hhi_21d_up_days": {"inputs": ["close", "volume"], "func": vcc_087_hhi_21d_up_days},
    "vcc_088_gini_21d_up_days": {"inputs": ["close", "volume"], "func": vcc_088_gini_21d_up_days},
    "vcc_089_up_day_vol_share_21d": {"inputs": ["close", "volume"], "func": vcc_089_up_day_vol_share_21d},
    "vcc_090_up_day_vol_share_63d": {"inputs": ["close", "volume"], "func": vcc_090_up_day_vol_share_63d},
    "vcc_091_down_vs_up_vol_share_ratio_21d": {"inputs": ["close", "volume"], "func": vcc_091_down_vs_up_vol_share_ratio_21d},
    "vcc_092_down_vs_up_vol_share_ratio_63d": {"inputs": ["close", "volume"], "func": vcc_092_down_vs_up_vol_share_ratio_63d},
    "vcc_093_down_day_hhi_vs_total_hhi_21d": {"inputs": ["close", "volume"], "func": vcc_093_down_day_hhi_vs_total_hhi_21d},
    "vcc_094_down_day_gini_vs_total_gini_21d": {"inputs": ["close", "volume"], "func": vcc_094_down_day_gini_vs_total_gini_21d},
    "vcc_095_down_day_vol_share_21d_zscore_252d": {"inputs": ["close", "volume"], "func": vcc_095_down_day_vol_share_21d_zscore_252d},
    "vcc_096_cv_21d": {"inputs": ["volume"], "func": vcc_096_cv_21d},
    "vcc_097_cv_63d": {"inputs": ["volume"], "func": vcc_097_cv_63d},
    "vcc_098_cv_126d": {"inputs": ["volume"], "func": vcc_098_cv_126d},
    "vcc_099_cv_252d": {"inputs": ["volume"], "func": vcc_099_cv_252d},
    "vcc_100_cv_21d_zscore_252d": {"inputs": ["volume"], "func": vcc_100_cv_21d_zscore_252d},
    "vcc_101_cv_21d_vs_252d_ratio": {"inputs": ["volume"], "func": vcc_101_cv_21d_vs_252d_ratio},
    "vcc_102_cv_63d_vs_252d_ratio": {"inputs": ["volume"], "func": vcc_102_cv_63d_vs_252d_ratio},
    "vcc_103_vol_iqr_ratio_21d": {"inputs": ["volume"], "func": vcc_103_vol_iqr_ratio_21d},
    "vcc_104_vol_iqr_ratio_63d": {"inputs": ["volume"], "func": vcc_104_vol_iqr_ratio_63d},
    "vcc_105_vol_90th_10th_ratio_21d": {"inputs": ["volume"], "func": vcc_105_vol_90th_10th_ratio_21d},
    "vcc_106_pareto_top20pct_share_21d": {"inputs": ["volume"], "func": vcc_106_pareto_top20pct_share_21d},
    "vcc_107_pareto_top20pct_share_63d": {"inputs": ["volume"], "func": vcc_107_pareto_top20pct_share_63d},
    "vcc_108_pareto_top10pct_share_21d": {"inputs": ["volume"], "func": vcc_108_pareto_top10pct_share_21d},
    "vcc_109_pareto_top10pct_share_63d": {"inputs": ["volume"], "func": vcc_109_pareto_top10pct_share_63d},
    "vcc_110_pareto_top10pct_share_252d": {"inputs": ["volume"], "func": vcc_110_pareto_top10pct_share_252d},
    "vcc_111_pareto_top20pct_share_252d": {"inputs": ["volume"], "func": vcc_111_pareto_top20pct_share_252d},
    "vcc_112_pareto_top20pct_share_21d_zscore_252d": {"inputs": ["volume"], "func": vcc_112_pareto_top20pct_share_21d_zscore_252d},
    "vcc_113_pareto_top10pct_share_21d_pct_rank_252d": {"inputs": ["volume"], "func": vcc_113_pareto_top10pct_share_21d_pct_rank_252d},
    "vcc_114_pareto_top20pct_21d_vs_252d_ratio": {"inputs": ["volume"], "func": vcc_114_pareto_top20pct_21d_vs_252d_ratio},
    "vcc_115_pareto_top10pct_21d_vs_252d_ratio": {"inputs": ["volume"], "func": vcc_115_pareto_top10pct_21d_vs_252d_ratio},
    "vcc_116_top2_vs_bottom2_ratio_21d": {"inputs": ["volume"], "func": vcc_116_top2_vs_bottom2_ratio_21d},
    "vcc_117_top5_vs_bottom5_ratio_63d": {"inputs": ["volume"], "func": vcc_117_top5_vs_bottom5_ratio_63d},
    "vcc_118_max_day_vs_min_day_ratio_21d": {"inputs": ["volume"], "func": vcc_118_max_day_vs_min_day_ratio_21d},
    "vcc_119_max_day_vs_min_day_ratio_63d": {"inputs": ["volume"], "func": vcc_119_max_day_vs_min_day_ratio_63d},
    "vcc_120_max_day_vs_min_day_ratio_252d": {"inputs": ["volume"], "func": vcc_120_max_day_vs_min_day_ratio_252d},
    "vcc_121_top3_share_21d_expanding_max": {"inputs": ["volume"], "func": vcc_121_top3_share_21d_expanding_max},
    "vcc_122_hhi_21d_expanding_max": {"inputs": ["volume"], "func": vcc_122_hhi_21d_expanding_max},
    "vcc_123_top1_share_21d_expanding_rank": {"inputs": ["volume"], "func": vcc_123_top1_share_21d_expanding_rank},
    "vcc_124_gini_21d_expanding_rank": {"inputs": ["volume"], "func": vcc_124_gini_21d_expanding_rank},
    "vcc_125_days_to_90pct_21d_pct_rank_252d": {"inputs": ["volume"], "func": vcc_125_days_to_90pct_21d_pct_rank_252d},
    "vcc_126_days_above_2x_mean_21d": {"inputs": ["volume"], "func": vcc_126_days_above_2x_mean_21d},
    "vcc_127_days_above_2x_mean_63d": {"inputs": ["volume"], "func": vcc_127_days_above_2x_mean_63d},
    "vcc_128_days_above_3x_mean_21d": {"inputs": ["volume"], "func": vcc_128_days_above_3x_mean_21d},
    "vcc_129_share_of_days_above_2x_mean_21d": {"inputs": ["volume"], "func": vcc_129_share_of_days_above_2x_mean_21d},
    "vcc_130_share_of_days_above_2x_mean_63d": {"inputs": ["volume"], "func": vcc_130_share_of_days_above_2x_mean_63d},
    "vcc_131_high_vol_day_share_of_total_21d": {"inputs": ["volume"], "func": vcc_131_high_vol_day_share_of_total_21d},
    "vcc_132_high_vol_day_share_of_total_63d": {"inputs": ["volume"], "func": vcc_132_high_vol_day_share_of_total_63d},
    "vcc_133_high_vol_day_share_zscore_252d": {"inputs": ["volume"], "func": vcc_133_high_vol_day_share_zscore_252d},
    "vcc_134_days_below_half_mean_21d": {"inputs": ["volume"], "func": vcc_134_days_below_half_mean_21d},
    "vcc_135_high_to_low_vol_day_count_ratio_21d": {"inputs": ["volume"], "func": vcc_135_high_to_low_vol_day_count_ratio_21d},
    "vcc_136_concentration_index_21d": {"inputs": ["volume"], "func": vcc_136_concentration_index_21d},
    "vcc_137_concentration_index_63d": {"inputs": ["volume"], "func": vcc_137_concentration_index_63d},
    "vcc_138_concentration_index_21d_zscore_252d": {"inputs": ["volume"], "func": vcc_138_concentration_index_21d_zscore_252d},
    "vcc_139_concentration_index_63d_zscore_252d": {"inputs": ["volume"], "func": vcc_139_concentration_index_63d_zscore_252d},
    "vcc_140_concentration_index_21d_pct_rank_252d": {"inputs": ["volume"], "func": vcc_140_concentration_index_21d_pct_rank_252d},
    "vcc_141_concentration_index_21d_vs_63d_ratio": {"inputs": ["volume"], "func": vcc_141_concentration_index_21d_vs_63d_ratio},
    "vcc_142_concentration_index_21d_ewm": {"inputs": ["volume"], "func": vcc_142_concentration_index_21d_ewm},
    "vcc_143_concentration_index_21d_expanding_max": {"inputs": ["volume"], "func": vcc_143_concentration_index_21d_expanding_max},
    "vcc_144_top1_share_21d_gt_threshold_flag": {"inputs": ["volume"], "func": vcc_144_top1_share_21d_gt_threshold_flag},
    "vcc_145_hhi_21d_gt_2x_uniform_flag": {"inputs": ["volume"], "func": vcc_145_hhi_21d_gt_2x_uniform_flag},
    "vcc_146_top3_down_vol_share_of_total_21d": {"inputs": ["close", "volume"], "func": vcc_146_top3_down_vol_share_of_total_21d},
    "vcc_147_top3_up_vol_share_of_total_21d": {"inputs": ["close", "volume"], "func": vcc_147_top3_up_vol_share_of_total_21d},
    "vcc_148_down_top3_vs_up_top3_vol_ratio_21d": {"inputs": ["close", "volume"], "func": vcc_148_down_top3_vs_up_top3_vol_ratio_21d},
    "vcc_149_concentration_index_21d_pct_rank_504d": {"inputs": ["volume"], "func": vcc_149_concentration_index_21d_pct_rank_504d},
    "vcc_150_hhi_21d_expanding_zscore": {"inputs": ["volume"], "func": vcc_150_hhi_21d_expanding_zscore},
    "vcc_176_vol_acceleration_21d": {"inputs": ["volume"], "func": vcc_176_vol_acceleration_21d},
    "vcc_177_vol_acceleration_63d": {"inputs": ["volume"], "func": vcc_177_vol_acceleration_63d},
    "vcc_178_down_day_cv_21d": {"inputs": ["close", "volume"], "func": vcc_178_down_day_cv_21d},
    "vcc_179_up_day_cv_21d": {"inputs": ["close", "volume"], "func": vcc_179_up_day_cv_21d},
    "vcc_180_down_day_cv_vs_up_day_cv_ratio_21d": {"inputs": ["close", "volume"], "func": vcc_180_down_day_cv_vs_up_day_cv_ratio_21d},
    "vcc_181_large_range_day_vol_share_21d": {"inputs": ["close", "high", "low", "volume"], "func": vcc_181_large_range_day_vol_share_21d},
    "vcc_182_large_range_day_vol_share_63d": {"inputs": ["close", "high", "low", "volume"], "func": vcc_182_large_range_day_vol_share_63d},
    "vcc_183_small_range_day_vol_share_21d": {"inputs": ["close", "high", "low", "volume"], "func": vcc_183_small_range_day_vol_share_21d},
    "vcc_184_hhi_21d_pct_rank_126d": {"inputs": ["volume"], "func": vcc_184_hhi_21d_pct_rank_126d},
    "vcc_185_gini_21d_pct_rank_126d": {"inputs": ["volume"], "func": vcc_185_gini_21d_pct_rank_126d},
    "vcc_186_vol_75th_25th_ratio_21d": {"inputs": ["volume"], "func": vcc_186_vol_75th_25th_ratio_21d},
    "vcc_187_vol_75th_25th_ratio_63d": {"inputs": ["volume"], "func": vcc_187_vol_75th_25th_ratio_63d},
    "vcc_188_top1_share_126d_pct_rank_252d": {"inputs": ["volume"], "func": vcc_188_top1_share_126d_pct_rank_252d},
    "vcc_189_concentration_index_252d": {"inputs": ["volume"], "func": vcc_189_concentration_index_252d},
    "vcc_190_concentration_21d_vs_252d_ratio": {"inputs": ["volume"], "func": vcc_190_concentration_21d_vs_252d_ratio},
    "vcc_191_days_above_4x_mean_21d": {"inputs": ["volume"], "func": vcc_191_days_above_4x_mean_21d},
    "vcc_192_days_above_3x_mean_63d": {"inputs": ["volume"], "func": vcc_192_days_above_3x_mean_63d},
    "vcc_193_top5_share_21d_ewm_63": {"inputs": ["volume"], "func": vcc_193_top5_share_21d_ewm_63},
    "vcc_194_hhi_252d_pct_rank_expanding": {"inputs": ["volume"], "func": vcc_194_hhi_252d_pct_rank_expanding},
    "vcc_195_vol_iqr_ratio_252d": {"inputs": ["volume"], "func": vcc_195_vol_iqr_ratio_252d},
    "vcc_196_up_day_hhi_63d": {"inputs": ["close", "volume"], "func": vcc_196_up_day_hhi_63d},
    "vcc_197_down_up_hhi_ratio_63d": {"inputs": ["close", "volume"], "func": vcc_197_down_up_hhi_ratio_63d},
    "vcc_198_down_day_entropy_63d": {"inputs": ["close", "volume"], "func": vcc_198_down_day_entropy_63d},
    "vcc_199_high_vol_share_of_total_252d": {"inputs": ["volume"], "func": vcc_199_high_vol_share_of_total_252d},
    "vcc_200_pareto_top5pct_share_63d": {"inputs": ["volume"], "func": vcc_200_pareto_top5pct_share_63d},
}
