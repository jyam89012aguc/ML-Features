"""
21_volume_concentration — Base Features 001-075 (extended to 100)
Domain: concentration / inequality of volume distribution across days within a window —
        top-N-day share, Herfindahl index, Gini coefficient, entropy, min-days-to-X-pct.
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
    """Share of total held by the top-n values in arr."""
    total = arr.sum()
    if total <= 0:
        return np.nan
    top = np.partition(arr, -min(n, len(arr)))[-min(n, len(arr)):]
    return float(top.sum() / total)


def _herfindahl(arr: np.ndarray) -> float:
    """Herfindahl-Hirschman index of volume shares (sum of squared share fractions)."""
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
    """Shannon entropy (nats) of the volume distribution."""
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


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): Top-N-day volume share (21-day window) ---

def vcc_001_top1_share_21d(volume: pd.Series) -> pd.Series:
    """Share of 21-day total volume in the single largest-volume day."""
    return volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _topn_share(a, 1), raw=True)


def vcc_002_top2_share_21d(volume: pd.Series) -> pd.Series:
    """Share of 21-day total volume in the top-2 largest-volume days."""
    return volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _topn_share(a, 2), raw=True)


def vcc_003_top3_share_21d(volume: pd.Series) -> pd.Series:
    """Share of 21-day total volume in the top-3 largest-volume days."""
    return volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _topn_share(a, 3), raw=True)


def vcc_004_top5_share_21d(volume: pd.Series) -> pd.Series:
    """Share of 21-day total volume in the top-5 largest-volume days."""
    return volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _topn_share(a, 5), raw=True)


def vcc_005_top1_share_63d(volume: pd.Series) -> pd.Series:
    """Share of 63-day total volume in the single largest-volume day."""
    return volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        lambda a: _topn_share(a, 1), raw=True)


def vcc_006_top3_share_63d(volume: pd.Series) -> pd.Series:
    """Share of 63-day total volume in the top-3 largest-volume days."""
    return volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        lambda a: _topn_share(a, 3), raw=True)


def vcc_007_top5_share_63d(volume: pd.Series) -> pd.Series:
    """Share of 63-day total volume in the top-5 largest-volume days."""
    return volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        lambda a: _topn_share(a, 5), raw=True)


def vcc_008_top10_share_63d(volume: pd.Series) -> pd.Series:
    """Share of 63-day total volume in the top-10 largest-volume days."""
    return volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        lambda a: _topn_share(a, 10), raw=True)


def vcc_009_top1_share_126d(volume: pd.Series) -> pd.Series:
    """Share of 126-day total volume in the single largest-volume day."""
    return volume.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(
        lambda a: _topn_share(a, 1), raw=True)


def vcc_010_top5_share_126d(volume: pd.Series) -> pd.Series:
    """Share of 126-day total volume in the top-5 largest-volume days."""
    return volume.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(
        lambda a: _topn_share(a, 5), raw=True)


def vcc_011_top10_share_126d(volume: pd.Series) -> pd.Series:
    """Share of 126-day total volume in the top-10 largest-volume days."""
    return volume.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(
        lambda a: _topn_share(a, 10), raw=True)


def vcc_012_top1_share_252d(volume: pd.Series) -> pd.Series:
    """Share of 252-day total volume in the single largest-volume day."""
    return volume.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        lambda a: _topn_share(a, 1), raw=True)


def vcc_013_top5_share_252d(volume: pd.Series) -> pd.Series:
    """Share of 252-day total volume in the top-5 largest-volume days."""
    return volume.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        lambda a: _topn_share(a, 5), raw=True)


def vcc_014_top10_share_252d(volume: pd.Series) -> pd.Series:
    """Share of 252-day total volume in the top-10 largest-volume days."""
    return volume.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        lambda a: _topn_share(a, 10), raw=True)


def vcc_015_top20_share_252d(volume: pd.Series) -> pd.Series:
    """Share of 252-day total volume in the top-20 largest-volume days."""
    return volume.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        lambda a: _topn_share(a, 20), raw=True)


# --- Group B (016-025): Herfindahl index of volume distribution ---

def vcc_016_hhi_21d(volume: pd.Series) -> pd.Series:
    """Herfindahl index of daily volume shares over 21-day window."""
    return volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _herfindahl, raw=True)


def vcc_017_hhi_63d(volume: pd.Series) -> pd.Series:
    """Herfindahl index of daily volume shares over 63-day window."""
    return volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        _herfindahl, raw=True)


def vcc_018_hhi_126d(volume: pd.Series) -> pd.Series:
    """Herfindahl index of daily volume shares over 126-day window."""
    return volume.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(
        _herfindahl, raw=True)


def vcc_019_hhi_252d(volume: pd.Series) -> pd.Series:
    """Herfindahl index of daily volume shares over 252-day window."""
    return volume.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        _herfindahl, raw=True)


def vcc_020_hhi_21d_norm_uniform(volume: pd.Series) -> pd.Series:
    """HHI-21d divided by the uniform benchmark (1/21); ratio > 1 = concentrated."""
    hhi = vcc_016_hhi_21d(volume)
    uniform = 1.0 / _TD_MON
    return hhi / uniform


def vcc_021_hhi_63d_norm_uniform(volume: pd.Series) -> pd.Series:
    """HHI-63d divided by uniform benchmark (1/63); ratio > 1 = concentrated."""
    hhi = vcc_017_hhi_63d(volume)
    uniform = 1.0 / _TD_QTR
    return hhi / uniform


def vcc_022_hhi_252d_norm_uniform(volume: pd.Series) -> pd.Series:
    """HHI-252d divided by uniform benchmark (1/252); ratio > 1 = concentrated."""
    hhi = vcc_019_hhi_252d(volume)
    uniform = 1.0 / _TD_YEAR
    return hhi / uniform


def vcc_023_hhi_21d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 21-day HHI relative to trailing 252-day distribution."""
    hhi = vcc_016_hhi_21d(volume)
    m = _rolling_mean(hhi, _TD_YEAR)
    s = _rolling_std(hhi, _TD_YEAR)
    return _safe_div(hhi - m, s)


def vcc_024_hhi_63d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 63-day HHI relative to trailing 252-day distribution."""
    hhi = vcc_017_hhi_63d(volume)
    m = _rolling_mean(hhi, _TD_YEAR)
    s = _rolling_std(hhi, _TD_YEAR)
    return _safe_div(hhi - m, s)


def vcc_025_hhi_21d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day HHI within trailing 252-day distribution."""
    hhi = vcc_016_hhi_21d(volume)
    return hhi.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group C (026-035): Gini coefficient of volume distribution ---

def vcc_026_gini_21d(volume: pd.Series) -> pd.Series:
    """Gini coefficient of daily volume distribution over 21-day window."""
    return volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _gini, raw=True)


def vcc_027_gini_63d(volume: pd.Series) -> pd.Series:
    """Gini coefficient of daily volume distribution over 63-day window."""
    return volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        _gini, raw=True)


def vcc_028_gini_126d(volume: pd.Series) -> pd.Series:
    """Gini coefficient of daily volume distribution over 126-day window."""
    return volume.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(
        _gini, raw=True)


def vcc_029_gini_252d(volume: pd.Series) -> pd.Series:
    """Gini coefficient of daily volume distribution over 252-day window."""
    return volume.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        _gini, raw=True)


def vcc_030_gini_21d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 21-day Gini relative to trailing 252-day distribution."""
    g = vcc_026_gini_21d(volume)
    m = _rolling_mean(g, _TD_YEAR)
    s = _rolling_std(g, _TD_YEAR)
    return _safe_div(g - m, s)


def vcc_031_gini_63d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 63-day Gini relative to trailing 252-day distribution."""
    g = vcc_027_gini_63d(volume)
    m = _rolling_mean(g, _TD_YEAR)
    s = _rolling_std(g, _TD_YEAR)
    return _safe_div(g - m, s)


def vcc_032_gini_21d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day Gini within trailing 252-day distribution."""
    g = vcc_026_gini_21d(volume)
    return g.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vcc_033_gini_63d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 63-day Gini within trailing 252-day distribution."""
    g = vcc_027_gini_63d(volume)
    return g.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vcc_034_gini_21d_ewm_signal(volume: pd.Series) -> pd.Series:
    """21-day EMA of the 21-day Gini coefficient (smoothed concentration trend)."""
    g = vcc_026_gini_21d(volume)
    return _ewm_mean(g, _TD_MON)


def vcc_035_gini_63d_expanding_max(volume: pd.Series) -> pd.Series:
    """Expanding maximum of the 63-day Gini (all-time peak concentration record)."""
    g = vcc_027_gini_63d(volume)
    return g.expanding(min_periods=1).max()


# --- Group D (036-045): Shannon entropy of volume distribution ---

def vcc_036_entropy_21d(volume: pd.Series) -> pd.Series:
    """Shannon entropy (nats) of daily volume shares over 21-day window."""
    return volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _entropy, raw=True)


def vcc_037_entropy_63d(volume: pd.Series) -> pd.Series:
    """Shannon entropy (nats) of daily volume shares over 63-day window."""
    return volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        _entropy, raw=True)


def vcc_038_entropy_126d(volume: pd.Series) -> pd.Series:
    """Shannon entropy (nats) of daily volume shares over 126-day window."""
    return volume.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(
        _entropy, raw=True)


def vcc_039_entropy_252d(volume: pd.Series) -> pd.Series:
    """Shannon entropy (nats) of daily volume shares over 252-day window."""
    return volume.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        _entropy, raw=True)


def vcc_040_entropy_21d_norm_max(volume: pd.Series) -> pd.Series:
    """21-day entropy normalized by log(21) — maximum possible entropy for window."""
    ent = vcc_036_entropy_21d(volume)
    return ent / np.log(_TD_MON)


def vcc_041_entropy_63d_norm_max(volume: pd.Series) -> pd.Series:
    """63-day entropy normalized by log(63) — efficiency of volume distribution."""
    ent = vcc_037_entropy_63d(volume)
    return ent / np.log(_TD_QTR)


def vcc_042_entropy_252d_norm_max(volume: pd.Series) -> pd.Series:
    """252-day entropy normalized by log(252)."""
    ent = vcc_039_entropy_252d(volume)
    return ent / np.log(_TD_YEAR)


def vcc_043_entropy_21d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 21-day entropy within trailing 252-day distribution."""
    ent = vcc_036_entropy_21d(volume)
    m = _rolling_mean(ent, _TD_YEAR)
    s = _rolling_std(ent, _TD_YEAR)
    return _safe_div(ent - m, s)


def vcc_044_entropy_63d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 63-day entropy within trailing 252-day distribution."""
    ent = vcc_037_entropy_63d(volume)
    m = _rolling_mean(ent, _TD_YEAR)
    s = _rolling_std(ent, _TD_YEAR)
    return _safe_div(ent - m, s)


def vcc_045_entropy_21d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day entropy within trailing 252-day distribution."""
    ent = vcc_036_entropy_21d(volume)
    return ent.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group E (046-055): Ratio of largest day to window total ---

def vcc_046_max_day_ratio_21d(volume: pd.Series) -> pd.Series:
    """Ratio of single-day maximum volume to 21-day total volume."""
    mx = _rolling_max(volume, _TD_MON)
    tot = _rolling_sum(volume, _TD_MON)
    return _safe_div(mx, tot)


def vcc_047_max_day_ratio_63d(volume: pd.Series) -> pd.Series:
    """Ratio of single-day maximum volume to 63-day total volume."""
    mx = _rolling_max(volume, _TD_QTR)
    tot = _rolling_sum(volume, _TD_QTR)
    return _safe_div(mx, tot)


def vcc_048_max_day_ratio_126d(volume: pd.Series) -> pd.Series:
    """Ratio of single-day maximum volume to 126-day total volume."""
    mx = _rolling_max(volume, _TD_HALF)
    tot = _rolling_sum(volume, _TD_HALF)
    return _safe_div(mx, tot)


def vcc_049_max_day_ratio_252d(volume: pd.Series) -> pd.Series:
    """Ratio of single-day maximum volume to 252-day total volume."""
    mx = _rolling_max(volume, _TD_YEAR)
    tot = _rolling_sum(volume, _TD_YEAR)
    return _safe_div(mx, tot)


def vcc_050_max_to_mean_ratio_21d(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day max day volume to 21-day mean volume (spike magnitude)."""
    mx = _rolling_max(volume, _TD_MON)
    mn = _rolling_mean(volume, _TD_MON)
    return _safe_div(mx, mn)


def vcc_051_max_to_mean_ratio_63d(volume: pd.Series) -> pd.Series:
    """Ratio of 63-day max day volume to 63-day mean volume."""
    mx = _rolling_max(volume, _TD_QTR)
    mn = _rolling_mean(volume, _TD_QTR)
    return _safe_div(mx, mn)


def vcc_052_max_to_median_ratio_21d(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day max day volume to 21-day median volume."""
    mx = _rolling_max(volume, _TD_MON)
    med = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).median()
    return _safe_div(mx, med)


def vcc_053_max_to_median_ratio_63d(volume: pd.Series) -> pd.Series:
    """Ratio of 63-day max day volume to 63-day median volume."""
    mx = _rolling_max(volume, _TD_QTR)
    med = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).median()
    return _safe_div(mx, med)


def vcc_054_max_day_ratio_21d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 21-day max-day-ratio within trailing 252-day distribution."""
    r = vcc_046_max_day_ratio_21d(volume)
    m = _rolling_mean(r, _TD_YEAR)
    s = _rolling_std(r, _TD_YEAR)
    return _safe_div(r - m, s)


def vcc_055_max_day_ratio_63d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 63-day max-day-ratio within trailing 252-day distribution."""
    r = vcc_047_max_day_ratio_63d(volume)
    return r.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group F (056-065): Days-to-X%-of-volume (min days accounting for X% of total) ---

def vcc_056_days_to_50pct_21d(volume: pd.Series) -> pd.Series:
    """Min days (largest first) needed to reach 50% of 21-day total volume."""
    return volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _days_to_pct(a, 0.50), raw=True)


def vcc_057_days_to_75pct_21d(volume: pd.Series) -> pd.Series:
    """Min days (largest first) needed to reach 75% of 21-day total volume."""
    return volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _days_to_pct(a, 0.75), raw=True)


def vcc_058_days_to_90pct_21d(volume: pd.Series) -> pd.Series:
    """Min days (largest first) needed to reach 90% of 21-day total volume."""
    return volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _days_to_pct(a, 0.90), raw=True)


def vcc_059_days_to_50pct_63d(volume: pd.Series) -> pd.Series:
    """Min days (largest first) needed to reach 50% of 63-day total volume."""
    return volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        lambda a: _days_to_pct(a, 0.50), raw=True)


def vcc_060_days_to_75pct_63d(volume: pd.Series) -> pd.Series:
    """Min days (largest first) needed to reach 75% of 63-day total volume."""
    return volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        lambda a: _days_to_pct(a, 0.75), raw=True)


def vcc_061_days_to_90pct_63d(volume: pd.Series) -> pd.Series:
    """Min days (largest first) needed to reach 90% of 63-day total volume."""
    return volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        lambda a: _days_to_pct(a, 0.90), raw=True)


def vcc_062_days_to_50pct_252d(volume: pd.Series) -> pd.Series:
    """Min days (largest first) needed to reach 50% of 252-day total volume."""
    return volume.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        lambda a: _days_to_pct(a, 0.50), raw=True)


def vcc_063_days_to_75pct_252d(volume: pd.Series) -> pd.Series:
    """Min days (largest first) needed to reach 75% of 252-day total volume."""
    return volume.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        lambda a: _days_to_pct(a, 0.75), raw=True)


def vcc_064_days_to_50pct_21d_norm(volume: pd.Series) -> pd.Series:
    """Days-to-50%-of-21d-vol divided by 21 (normalized, lower = more concentrated)."""
    return _safe_div(vcc_056_days_to_50pct_21d(volume),
                     pd.Series(_TD_MON, index=volume.index))


def vcc_065_days_to_75pct_63d_norm(volume: pd.Series) -> pd.Series:
    """Days-to-75%-of-63d-vol divided by 63."""
    return _safe_div(vcc_060_days_to_75pct_63d(volume),
                     pd.Series(_TD_QTR, index=volume.index))


# --- Group G (066-075): Cross-window and ratio comparisons ---

def vcc_066_hhi_21d_vs_252d_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day HHI to 252-day HHI (recent vs long-run concentration)."""
    return _safe_div(vcc_016_hhi_21d(volume), vcc_019_hhi_252d(volume))


def vcc_067_gini_21d_vs_252d_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day Gini to 252-day Gini (recent vs long-run inequality)."""
    return _safe_div(vcc_026_gini_21d(volume), vcc_029_gini_252d(volume))


def vcc_068_entropy_21d_vs_252d_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day entropy to 252-day entropy (recent vs historical spread)."""
    return _safe_div(vcc_036_entropy_21d(volume), vcc_039_entropy_252d(volume))


def vcc_069_top1_share_21d_vs_252d_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day top-1 share to 252-day top-1 share."""
    return _safe_div(vcc_001_top1_share_21d(volume), vcc_012_top1_share_252d(volume))


def vcc_070_top5_share_21d_vs_252d_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day top-5 share to 252-day top-5 share."""
    return _safe_div(vcc_004_top5_share_21d(volume), vcc_013_top5_share_252d(volume))


def vcc_071_hhi_63d_vs_252d_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 63-day HHI to 252-day HHI (medium-run vs long-run)."""
    return _safe_div(vcc_017_hhi_63d(volume), vcc_019_hhi_252d(volume))


def vcc_072_top3_share_63d_vs_21d_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 63-day top-3 share to 21-day top-3 share."""
    return _safe_div(vcc_006_top3_share_63d(volume), vcc_003_top3_share_21d(volume))


def vcc_073_days_to_75pct_21d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of days-to-75%-of-21d-vol in trailing 252-day distribution."""
    d = vcc_057_days_to_75pct_21d(volume)
    return d.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vcc_074_entropy_deficit_21d(volume: pd.Series) -> pd.Series:
    """Max-entropy minus actual 21-day entropy (nats of lost diversity)."""
    ent = vcc_036_entropy_21d(volume)
    return np.log(_TD_MON) - ent


def vcc_075_gini_hhi_composite_21d(volume: pd.Series) -> pd.Series:
    """Average of normalized Gini-21d and HHI-21d (combined concentration score)."""
    g = vcc_026_gini_21d(volume)
    h = vcc_020_hhi_21d_norm_uniform(volume)
    h_norm = h / h.rolling(_TD_YEAR, min_periods=_TD_QTR).max().clip(lower=_EPS)
    return (g + h_norm) / 2.0


# --- Group H-ext (151-175): Volume-weighted price range concentration / new constructions ---

def vcc_151_vol_weighted_price_range_21d(close: pd.Series, high: pd.Series,
                                          low: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted mean daily range (high-low) over 21d, normalized by close."""
    rng = (high - low) / close.clip(lower=_EPS)
    wt = _rolling_sum(volume * rng, _TD_MON)
    tot = _rolling_sum(volume, _TD_MON)
    return _safe_div(wt, tot)


def vcc_152_top1_vol_price_impact_21d(close: pd.Series, high: pd.Series,
                                       low: pd.Series, volume: pd.Series) -> pd.Series:
    """Range of the highest-volume day in 21d as fraction of 21d mean close."""
    rng = (high - low)
    def _top1_rng(arr_v, arr_r):
        if arr_v.sum() <= 0:
            return np.nan
        idx = np.argmax(arr_v)
        return float(arr_r[idx])
    rng_roll = pd.Series(index=volume.index, dtype=float)
    for i in range(len(volume)):
        w = _TD_MON
        start = max(0, i - w + 1)
        sv = volume.values[start:i+1]
        sr = rng.values[start:i+1]
        if len(sv) >= max(1, w // 2):
            rng_roll.iloc[i] = _top1_rng(sv, sr)
    m = _rolling_mean(close, _TD_MON)
    return _safe_div(rng_roll, m)


def vcc_153_hhi_126d_norm_uniform(volume: pd.Series) -> pd.Series:
    """HHI-126d divided by uniform benchmark (1/126); concentration ratio."""
    hhi = volume.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(
        _herfindahl, raw=True)
    return hhi / (1.0 / _TD_HALF)


def vcc_154_top2_share_126d(volume: pd.Series) -> pd.Series:
    """Share of 126-day total volume in the top-2 largest-volume days."""
    return volume.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(
        lambda a: _topn_share(a, 2), raw=True)


def vcc_155_top20_share_63d(volume: pd.Series) -> pd.Series:
    """Share of 63-day total volume in the top-20 largest-volume days."""
    return volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        lambda a: _topn_share(a, 20), raw=True)


def vcc_156_gini_126d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 126-day Gini within trailing 252-day distribution."""
    g = vcc_028_gini_126d(volume)
    return g.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vcc_157_entropy_126d_norm_max(volume: pd.Series) -> pd.Series:
    """126-day entropy normalized by log(126) — distribution efficiency."""
    ent = vcc_038_entropy_126d(volume)
    return ent / np.log(_TD_HALF)


def vcc_158_days_to_90pct_63d(volume: pd.Series) -> pd.Series:
    """Min days (largest first) needed to reach 90% of 63-day total volume."""
    return volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        lambda a: _days_to_pct(a, 0.90), raw=True)


def vcc_159_days_to_95pct_21d(volume: pd.Series) -> pd.Series:
    """Min days (largest first) needed to reach 95% of 21-day total volume."""
    return volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _days_to_pct(a, 0.95), raw=True)


def vcc_160_days_to_95pct_63d(volume: pd.Series) -> pd.Series:
    """Min days (largest first) needed to reach 95% of 63-day total volume."""
    return volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        lambda a: _days_to_pct(a, 0.95), raw=True)


def vcc_161_entropy_deficit_63d(volume: pd.Series) -> pd.Series:
    """Max-entropy minus actual 63-day entropy (nats of lost diversity)."""
    ent = vcc_037_entropy_63d(volume)
    return np.log(_TD_QTR) - ent


def vcc_162_entropy_deficit_252d(volume: pd.Series) -> pd.Series:
    """Max-entropy minus actual 252-day entropy (nats of lost diversity)."""
    ent = vcc_039_entropy_252d(volume)
    return np.log(_TD_YEAR) - ent


def vcc_163_vol_skewness_21d(volume: pd.Series) -> pd.Series:
    """Skewness of daily volume distribution over 21-day window."""
    return volume.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).skew()


def vcc_164_vol_skewness_63d(volume: pd.Series) -> pd.Series:
    """Skewness of daily volume distribution over 63-day window."""
    return volume.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).skew()


def vcc_165_vol_kurtosis_21d(volume: pd.Series) -> pd.Series:
    """Excess kurtosis of daily volume distribution over 21-day window."""
    return volume.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).kurt()


def vcc_166_vol_kurtosis_63d(volume: pd.Series) -> pd.Series:
    """Excess kurtosis of daily volume distribution over 63-day window."""
    return volume.rolling(_TD_QTR, min_periods=max(4, _TD_QTR // 2)).kurt()


def vcc_167_vol_skewness_21d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 21-day volume skewness within trailing 252-day distribution."""
    sk = vcc_163_vol_skewness_21d(volume)
    m = _rolling_mean(sk, _TD_YEAR)
    s = _rolling_std(sk, _TD_YEAR)
    return _safe_div(sk - m, s)


def vcc_168_vol_kurtosis_21d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day volume kurtosis in trailing 252-day distribution."""
    k = vcc_165_vol_kurtosis_21d(volume)
    return k.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vcc_169_pareto_top30pct_share_21d(volume: pd.Series) -> pd.Series:
    """Share of 21d total volume in the top-30% highest-volume days."""
    def _par30(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        k = max(1, int(np.ceil(n * 0.30)))
        top = np.partition(arr, -k)[-k:]
        total = arr.sum()
        if total <= 0:
            return np.nan
        return float(top.sum() / total)
    return volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _par30, raw=True)


def vcc_170_pareto_top30pct_share_63d(volume: pd.Series) -> pd.Series:
    """Share of 63d total volume in the top-30% highest-volume days."""
    def _par30(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        k = max(1, int(np.ceil(n * 0.30)))
        top = np.partition(arr, -k)[-k:]
        total = arr.sum()
        if total <= 0:
            return np.nan
        return float(top.sum() / total)
    return volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        _par30, raw=True)


def vcc_171_hhi_21d_ewm_span63(volume: pd.Series) -> pd.Series:
    """EWM(span=63) of 21-day HHI — smoothed long-run concentration level."""
    hhi = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _herfindahl, raw=True)
    return _ewm_mean(hhi, _TD_QTR)


def vcc_172_gini_21d_ewm_span63(volume: pd.Series) -> pd.Series:
    """EWM(span=63) of 21-day Gini — smoothed long-run inequality level."""
    g = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _gini, raw=True)
    return _ewm_mean(g, _TD_QTR)


def vcc_173_top5_share_21d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day top-5 share within trailing 252-day distribution."""
    r = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _topn_share(a, 5), raw=True)
    return r.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vcc_174_entropy_21d_ewm_span63(volume: pd.Series) -> pd.Series:
    """EWM(span=63) of 21-day entropy — smoothed diversity trend."""
    ent = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _entropy, raw=True)
    return _ewm_mean(ent, _TD_QTR)


def vcc_175_vol_90th_10th_ratio_63d(volume: pd.Series) -> pd.Series:
    """90th-percentile to 10th-percentile volume ratio over 63 days."""
    q90 = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.90)
    q10 = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.10)
    return _safe_div(q90, q10)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_CONCENTRATION_REGISTRY_001_075 = {
    "vcc_001_top1_share_21d": {"inputs": ["volume"], "func": vcc_001_top1_share_21d},
    "vcc_002_top2_share_21d": {"inputs": ["volume"], "func": vcc_002_top2_share_21d},
    "vcc_003_top3_share_21d": {"inputs": ["volume"], "func": vcc_003_top3_share_21d},
    "vcc_004_top5_share_21d": {"inputs": ["volume"], "func": vcc_004_top5_share_21d},
    "vcc_005_top1_share_63d": {"inputs": ["volume"], "func": vcc_005_top1_share_63d},
    "vcc_006_top3_share_63d": {"inputs": ["volume"], "func": vcc_006_top3_share_63d},
    "vcc_007_top5_share_63d": {"inputs": ["volume"], "func": vcc_007_top5_share_63d},
    "vcc_008_top10_share_63d": {"inputs": ["volume"], "func": vcc_008_top10_share_63d},
    "vcc_009_top1_share_126d": {"inputs": ["volume"], "func": vcc_009_top1_share_126d},
    "vcc_010_top5_share_126d": {"inputs": ["volume"], "func": vcc_010_top5_share_126d},
    "vcc_011_top10_share_126d": {"inputs": ["volume"], "func": vcc_011_top10_share_126d},
    "vcc_012_top1_share_252d": {"inputs": ["volume"], "func": vcc_012_top1_share_252d},
    "vcc_013_top5_share_252d": {"inputs": ["volume"], "func": vcc_013_top5_share_252d},
    "vcc_014_top10_share_252d": {"inputs": ["volume"], "func": vcc_014_top10_share_252d},
    "vcc_015_top20_share_252d": {"inputs": ["volume"], "func": vcc_015_top20_share_252d},
    "vcc_016_hhi_21d": {"inputs": ["volume"], "func": vcc_016_hhi_21d},
    "vcc_017_hhi_63d": {"inputs": ["volume"], "func": vcc_017_hhi_63d},
    "vcc_018_hhi_126d": {"inputs": ["volume"], "func": vcc_018_hhi_126d},
    "vcc_019_hhi_252d": {"inputs": ["volume"], "func": vcc_019_hhi_252d},
    "vcc_020_hhi_21d_norm_uniform": {"inputs": ["volume"], "func": vcc_020_hhi_21d_norm_uniform},
    "vcc_021_hhi_63d_norm_uniform": {"inputs": ["volume"], "func": vcc_021_hhi_63d_norm_uniform},
    "vcc_022_hhi_252d_norm_uniform": {"inputs": ["volume"], "func": vcc_022_hhi_252d_norm_uniform},
    "vcc_023_hhi_21d_zscore_252d": {"inputs": ["volume"], "func": vcc_023_hhi_21d_zscore_252d},
    "vcc_024_hhi_63d_zscore_252d": {"inputs": ["volume"], "func": vcc_024_hhi_63d_zscore_252d},
    "vcc_025_hhi_21d_pct_rank_252d": {"inputs": ["volume"], "func": vcc_025_hhi_21d_pct_rank_252d},
    "vcc_026_gini_21d": {"inputs": ["volume"], "func": vcc_026_gini_21d},
    "vcc_027_gini_63d": {"inputs": ["volume"], "func": vcc_027_gini_63d},
    "vcc_028_gini_126d": {"inputs": ["volume"], "func": vcc_028_gini_126d},
    "vcc_029_gini_252d": {"inputs": ["volume"], "func": vcc_029_gini_252d},
    "vcc_030_gini_21d_zscore_252d": {"inputs": ["volume"], "func": vcc_030_gini_21d_zscore_252d},
    "vcc_031_gini_63d_zscore_252d": {"inputs": ["volume"], "func": vcc_031_gini_63d_zscore_252d},
    "vcc_032_gini_21d_pct_rank_252d": {"inputs": ["volume"], "func": vcc_032_gini_21d_pct_rank_252d},
    "vcc_033_gini_63d_pct_rank_252d": {"inputs": ["volume"], "func": vcc_033_gini_63d_pct_rank_252d},
    "vcc_034_gini_21d_ewm_signal": {"inputs": ["volume"], "func": vcc_034_gini_21d_ewm_signal},
    "vcc_035_gini_63d_expanding_max": {"inputs": ["volume"], "func": vcc_035_gini_63d_expanding_max},
    "vcc_036_entropy_21d": {"inputs": ["volume"], "func": vcc_036_entropy_21d},
    "vcc_037_entropy_63d": {"inputs": ["volume"], "func": vcc_037_entropy_63d},
    "vcc_038_entropy_126d": {"inputs": ["volume"], "func": vcc_038_entropy_126d},
    "vcc_039_entropy_252d": {"inputs": ["volume"], "func": vcc_039_entropy_252d},
    "vcc_040_entropy_21d_norm_max": {"inputs": ["volume"], "func": vcc_040_entropy_21d_norm_max},
    "vcc_041_entropy_63d_norm_max": {"inputs": ["volume"], "func": vcc_041_entropy_63d_norm_max},
    "vcc_042_entropy_252d_norm_max": {"inputs": ["volume"], "func": vcc_042_entropy_252d_norm_max},
    "vcc_043_entropy_21d_zscore_252d": {"inputs": ["volume"], "func": vcc_043_entropy_21d_zscore_252d},
    "vcc_044_entropy_63d_zscore_252d": {"inputs": ["volume"], "func": vcc_044_entropy_63d_zscore_252d},
    "vcc_045_entropy_21d_pct_rank_252d": {"inputs": ["volume"], "func": vcc_045_entropy_21d_pct_rank_252d},
    "vcc_046_max_day_ratio_21d": {"inputs": ["volume"], "func": vcc_046_max_day_ratio_21d},
    "vcc_047_max_day_ratio_63d": {"inputs": ["volume"], "func": vcc_047_max_day_ratio_63d},
    "vcc_048_max_day_ratio_126d": {"inputs": ["volume"], "func": vcc_048_max_day_ratio_126d},
    "vcc_049_max_day_ratio_252d": {"inputs": ["volume"], "func": vcc_049_max_day_ratio_252d},
    "vcc_050_max_to_mean_ratio_21d": {"inputs": ["volume"], "func": vcc_050_max_to_mean_ratio_21d},
    "vcc_051_max_to_mean_ratio_63d": {"inputs": ["volume"], "func": vcc_051_max_to_mean_ratio_63d},
    "vcc_052_max_to_median_ratio_21d": {"inputs": ["volume"], "func": vcc_052_max_to_median_ratio_21d},
    "vcc_053_max_to_median_ratio_63d": {"inputs": ["volume"], "func": vcc_053_max_to_median_ratio_63d},
    "vcc_054_max_day_ratio_21d_zscore_252d": {"inputs": ["volume"], "func": vcc_054_max_day_ratio_21d_zscore_252d},
    "vcc_055_max_day_ratio_63d_pct_rank_252d": {"inputs": ["volume"], "func": vcc_055_max_day_ratio_63d_pct_rank_252d},
    "vcc_056_days_to_50pct_21d": {"inputs": ["volume"], "func": vcc_056_days_to_50pct_21d},
    "vcc_057_days_to_75pct_21d": {"inputs": ["volume"], "func": vcc_057_days_to_75pct_21d},
    "vcc_058_days_to_90pct_21d": {"inputs": ["volume"], "func": vcc_058_days_to_90pct_21d},
    "vcc_059_days_to_50pct_63d": {"inputs": ["volume"], "func": vcc_059_days_to_50pct_63d},
    "vcc_060_days_to_75pct_63d": {"inputs": ["volume"], "func": vcc_060_days_to_75pct_63d},
    "vcc_061_days_to_90pct_63d": {"inputs": ["volume"], "func": vcc_061_days_to_90pct_63d},
    "vcc_062_days_to_50pct_252d": {"inputs": ["volume"], "func": vcc_062_days_to_50pct_252d},
    "vcc_063_days_to_75pct_252d": {"inputs": ["volume"], "func": vcc_063_days_to_75pct_252d},
    "vcc_064_days_to_50pct_21d_norm": {"inputs": ["volume"], "func": vcc_064_days_to_50pct_21d_norm},
    "vcc_065_days_to_75pct_63d_norm": {"inputs": ["volume"], "func": vcc_065_days_to_75pct_63d_norm},
    "vcc_066_hhi_21d_vs_252d_ratio": {"inputs": ["volume"], "func": vcc_066_hhi_21d_vs_252d_ratio},
    "vcc_067_gini_21d_vs_252d_ratio": {"inputs": ["volume"], "func": vcc_067_gini_21d_vs_252d_ratio},
    "vcc_068_entropy_21d_vs_252d_ratio": {"inputs": ["volume"], "func": vcc_068_entropy_21d_vs_252d_ratio},
    "vcc_069_top1_share_21d_vs_252d_ratio": {"inputs": ["volume"], "func": vcc_069_top1_share_21d_vs_252d_ratio},
    "vcc_070_top5_share_21d_vs_252d_ratio": {"inputs": ["volume"], "func": vcc_070_top5_share_21d_vs_252d_ratio},
    "vcc_071_hhi_63d_vs_252d_ratio": {"inputs": ["volume"], "func": vcc_071_hhi_63d_vs_252d_ratio},
    "vcc_072_top3_share_63d_vs_21d_ratio": {"inputs": ["volume"], "func": vcc_072_top3_share_63d_vs_21d_ratio},
    "vcc_073_days_to_75pct_21d_pct_rank_252d": {"inputs": ["volume"], "func": vcc_073_days_to_75pct_21d_pct_rank_252d},
    "vcc_074_entropy_deficit_21d": {"inputs": ["volume"], "func": vcc_074_entropy_deficit_21d},
    "vcc_075_gini_hhi_composite_21d": {"inputs": ["volume"], "func": vcc_075_gini_hhi_composite_21d},
    "vcc_151_vol_weighted_price_range_21d": {"inputs": ["close", "high", "low", "volume"], "func": vcc_151_vol_weighted_price_range_21d},
    "vcc_152_top1_vol_price_impact_21d": {"inputs": ["close", "high", "low", "volume"], "func": vcc_152_top1_vol_price_impact_21d},
    "vcc_153_hhi_126d_norm_uniform": {"inputs": ["volume"], "func": vcc_153_hhi_126d_norm_uniform},
    "vcc_154_top2_share_126d": {"inputs": ["volume"], "func": vcc_154_top2_share_126d},
    "vcc_155_top20_share_63d": {"inputs": ["volume"], "func": vcc_155_top20_share_63d},
    "vcc_156_gini_126d_pct_rank_252d": {"inputs": ["volume"], "func": vcc_156_gini_126d_pct_rank_252d},
    "vcc_157_entropy_126d_norm_max": {"inputs": ["volume"], "func": vcc_157_entropy_126d_norm_max},
    "vcc_158_days_to_90pct_63d": {"inputs": ["volume"], "func": vcc_158_days_to_90pct_63d},
    "vcc_159_days_to_95pct_21d": {"inputs": ["volume"], "func": vcc_159_days_to_95pct_21d},
    "vcc_160_days_to_95pct_63d": {"inputs": ["volume"], "func": vcc_160_days_to_95pct_63d},
    "vcc_161_entropy_deficit_63d": {"inputs": ["volume"], "func": vcc_161_entropy_deficit_63d},
    "vcc_162_entropy_deficit_252d": {"inputs": ["volume"], "func": vcc_162_entropy_deficit_252d},
    "vcc_163_vol_skewness_21d": {"inputs": ["volume"], "func": vcc_163_vol_skewness_21d},
    "vcc_164_vol_skewness_63d": {"inputs": ["volume"], "func": vcc_164_vol_skewness_63d},
    "vcc_165_vol_kurtosis_21d": {"inputs": ["volume"], "func": vcc_165_vol_kurtosis_21d},
    "vcc_166_vol_kurtosis_63d": {"inputs": ["volume"], "func": vcc_166_vol_kurtosis_63d},
    "vcc_167_vol_skewness_21d_zscore_252d": {"inputs": ["volume"], "func": vcc_167_vol_skewness_21d_zscore_252d},
    "vcc_168_vol_kurtosis_21d_pct_rank_252d": {"inputs": ["volume"], "func": vcc_168_vol_kurtosis_21d_pct_rank_252d},
    "vcc_169_pareto_top30pct_share_21d": {"inputs": ["volume"], "func": vcc_169_pareto_top30pct_share_21d},
    "vcc_170_pareto_top30pct_share_63d": {"inputs": ["volume"], "func": vcc_170_pareto_top30pct_share_63d},
    "vcc_171_hhi_21d_ewm_span63": {"inputs": ["volume"], "func": vcc_171_hhi_21d_ewm_span63},
    "vcc_172_gini_21d_ewm_span63": {"inputs": ["volume"], "func": vcc_172_gini_21d_ewm_span63},
    "vcc_173_top5_share_21d_pct_rank_252d": {"inputs": ["volume"], "func": vcc_173_top5_share_21d_pct_rank_252d},
    "vcc_174_entropy_21d_ewm_span63": {"inputs": ["volume"], "func": vcc_174_entropy_21d_ewm_span63},
    "vcc_175_vol_90th_10th_ratio_63d": {"inputs": ["volume"], "func": vcc_175_vol_90th_10th_ratio_63d},
}
