"""
20_up_down_volume — Base Features 001-075
Domain: direction-conditioned volume balance — down-day vs up-day volume asymmetry,
        up/down volume ratios, OBV-style accumulation, volume share on down days,
        volume-weighted day counts, and fraction of volume on worst-return days.
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
    """Rolling mean with half-window min_periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    """Rolling std with half-window min_periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    """Rolling sum with half-window min_periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    """Rolling min with half-window min_periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    """Rolling max with half-window min_periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    """Exponential weighted mean."""
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    """Log of series clipped at EPS."""
    return np.log(s.clip(lower=_EPS))


def _daily_ret(close: pd.Series) -> pd.Series:
    """Simple daily return."""
    return close.pct_change(1)


def _down_vol(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume on down-price days; NaN on up/flat days."""
    return volume.where(close < close.shift(1), np.nan)


def _up_vol(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume on up-price days; NaN on down/flat days."""
    return volume.where(close > close.shift(1), np.nan)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Rolling average volume on down vs up days ---

def udv_001_avg_down_vol_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume on down-price days over trailing 21 days."""
    return _down_vol(close, volume).rolling(_TD_MON, min_periods=1).mean()


def udv_002_avg_up_vol_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume on up-price days over trailing 21 days."""
    return _up_vol(close, volume).rolling(_TD_MON, min_periods=1).mean()


def udv_003_avg_down_vol_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume on down-price days over trailing 63 days."""
    return _down_vol(close, volume).rolling(_TD_QTR, min_periods=1).mean()


def udv_004_avg_up_vol_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume on up-price days over trailing 63 days."""
    return _up_vol(close, volume).rolling(_TD_QTR, min_periods=1).mean()


def udv_005_avg_down_vol_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume on down-price days over trailing 252 days."""
    return _down_vol(close, volume).rolling(_TD_YEAR, min_periods=_TD_QTR).mean()


def udv_006_avg_up_vol_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume on up-price days over trailing 252 days."""
    return _up_vol(close, volume).rolling(_TD_YEAR, min_periods=_TD_QTR).mean()


def udv_007_down_up_avg_vol_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of avg down-day volume to avg up-day volume over 21 days."""
    return _safe_div(udv_001_avg_down_vol_21d(close, volume),
                     udv_002_avg_up_vol_21d(close, volume))


def udv_008_down_up_avg_vol_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of avg down-day volume to avg up-day volume over 63 days."""
    return _safe_div(udv_003_avg_down_vol_63d(close, volume),
                     udv_004_avg_up_vol_63d(close, volume))


def udv_009_down_up_avg_vol_ratio_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of avg down-day volume to avg up-day volume over 252 days."""
    return _safe_div(udv_005_avg_down_vol_252d(close, volume),
                     udv_006_avg_up_vol_252d(close, volume))


def udv_010_down_up_avg_vol_ratio_21d_log(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Log of 21-day down/up average volume ratio (compresses tail)."""
    ratio = udv_007_down_up_avg_vol_ratio_21d(close, volume)
    return np.log(ratio.clip(lower=_EPS))


# --- Group B (011-020): Sum of volume on down vs up days ---

def udv_011_sum_down_vol_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Total volume traded on down-price days over trailing 21 days."""
    dv = volume.where(close < close.shift(1), 0.0)
    return _rolling_sum(dv, _TD_MON)


def udv_012_sum_up_vol_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Total volume traded on up-price days over trailing 21 days."""
    uv = volume.where(close > close.shift(1), 0.0)
    return _rolling_sum(uv, _TD_MON)


def udv_013_sum_down_vol_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Total volume traded on down-price days over trailing 63 days."""
    dv = volume.where(close < close.shift(1), 0.0)
    return _rolling_sum(dv, _TD_QTR)


def udv_014_sum_up_vol_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Total volume traded on up-price days over trailing 63 days."""
    uv = volume.where(close > close.shift(1), 0.0)
    return _rolling_sum(uv, _TD_QTR)


def udv_015_sum_down_vol_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Total volume traded on down-price days over trailing 252 days."""
    dv = volume.where(close < close.shift(1), 0.0)
    return _rolling_sum(dv, _TD_YEAR)


def udv_016_sum_up_vol_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Total volume traded on up-price days over trailing 252 days."""
    uv = volume.where(close > close.shift(1), 0.0)
    return _rolling_sum(uv, _TD_YEAR)


def udv_017_net_vol_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Net volume (up-vol minus down-vol) over trailing 21 days; negative = bearish."""
    return udv_012_sum_up_vol_21d(close, volume) - udv_011_sum_down_vol_21d(close, volume)


def udv_018_net_vol_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Net volume (up-vol minus down-vol) over trailing 63 days."""
    return udv_014_sum_up_vol_63d(close, volume) - udv_013_sum_down_vol_63d(close, volume)


def udv_019_net_vol_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Net volume (up-vol minus down-vol) over trailing 252 days."""
    return udv_016_sum_up_vol_252d(close, volume) - udv_015_sum_down_vol_252d(close, volume)


def udv_020_sum_down_up_vol_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of total down-day volume to total up-day volume over 21 days."""
    return _safe_div(udv_011_sum_down_vol_21d(close, volume),
                     udv_012_sum_up_vol_21d(close, volume))


# --- Group C (021-030): Down-day volume share of total volume ---

def udv_021_down_vol_share_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of total 21-day volume occurring on down-price days."""
    dv = _rolling_sum(volume.where(close < close.shift(1), 0.0), _TD_MON)
    tv = _rolling_sum(volume, _TD_MON)
    return _safe_div(dv, tv)


def udv_022_down_vol_share_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of total 63-day volume occurring on down-price days."""
    dv = _rolling_sum(volume.where(close < close.shift(1), 0.0), _TD_QTR)
    tv = _rolling_sum(volume, _TD_QTR)
    return _safe_div(dv, tv)


def udv_023_down_vol_share_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of total 252-day volume occurring on down-price days."""
    dv = _rolling_sum(volume.where(close < close.shift(1), 0.0), _TD_YEAR)
    tv = _rolling_sum(volume, _TD_YEAR)
    return _safe_div(dv, tv)


def udv_024_up_vol_share_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of total 21-day volume occurring on up-price days."""
    uv = _rolling_sum(volume.where(close > close.shift(1), 0.0), _TD_MON)
    tv = _rolling_sum(volume, _TD_MON)
    return _safe_div(uv, tv)


def udv_025_up_vol_share_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of total 63-day volume occurring on up-price days."""
    uv = _rolling_sum(volume.where(close > close.shift(1), 0.0), _TD_QTR)
    tv = _rolling_sum(volume, _TD_QTR)
    return _safe_div(uv, tv)


def udv_026_down_vol_share_minus_up_vol_share_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Down-vol share minus up-vol share (21d); positive = more vol on down days."""
    return udv_021_down_vol_share_21d(close, volume) - udv_024_up_vol_share_21d(close, volume)


def udv_027_down_vol_share_minus_up_vol_share_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Down-vol share minus up-vol share (63d)."""
    return udv_022_down_vol_share_63d(close, volume) - udv_025_up_vol_share_63d(close, volume)


def udv_028_down_vol_share_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day down-vol share within trailing 252-day distribution."""
    s = udv_021_down_vol_share_21d(close, volume)
    return s.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def udv_029_down_vol_share_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 21-day down-vol share relative to 252-day mean/std."""
    s = udv_021_down_vol_share_21d(close, volume)
    m = _rolling_mean(s, _TD_YEAR)
    sd = _rolling_std(s, _TD_YEAR)
    return _safe_div(s - m, sd)


def udv_030_down_vol_share_21d_gt60_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: 21-day down-vol share exceeds 60% (distress signal)."""
    return (udv_021_down_vol_share_21d(close, volume) > 0.60).astype(float)


# --- Group D (031-040): On-balance-volume style accumulation ---

def udv_031_obv_raw(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Classic on-balance volume: cumulative signed volume based on price direction."""
    direction = np.sign(close.diff(1)).fillna(0)
    return (direction * volume).cumsum()


def udv_032_obv_21d_change(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day change in OBV (recent accumulation/distribution momentum)."""
    obv = udv_031_obv_raw(close, volume)
    return obv.diff(_TD_MON)


def udv_033_obv_63d_change(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day change in OBV."""
    obv = udv_031_obv_raw(close, volume)
    return obv.diff(_TD_QTR)


def udv_034_obv_norm_by_avg_vol_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV 21-day change normalized by 21-day average total volume."""
    chg = udv_032_obv_21d_change(close, volume)
    avg_tv = _rolling_mean(volume, _TD_MON)
    return _safe_div(chg, avg_tv * _TD_MON)


def udv_035_obv_sma21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day SMA of OBV (smoothed accumulation trend)."""
    obv = udv_031_obv_raw(close, volume)
    return _rolling_mean(obv, _TD_MON)


def udv_036_obv_vs_sma21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV minus its 21-day SMA (OBV deviation from trend)."""
    obv = udv_031_obv_raw(close, volume)
    return obv - _rolling_mean(obv, _TD_MON)


def udv_037_obv_sma_crossover_21_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV SMA21 minus OBV SMA63 (positive = accumulating; negative = distributing)."""
    obv = udv_031_obv_raw(close, volume)
    return _rolling_mean(obv, _TD_MON) - _rolling_mean(obv, _TD_QTR)


def udv_038_obv_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of OBV within trailing 252-day OBV distribution."""
    obv = udv_031_obv_raw(close, volume)
    return obv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def udv_039_obv_21d_change_sign(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sign of 21-day OBV change: +1 accumulation, -1 distribution, 0 flat."""
    return np.sign(udv_032_obv_21d_change(close, volume)).astype(float)


def udv_040_obv_63d_zscore(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of OBV 63-day change relative to 252-day distribution of 63-day changes."""
    chg = udv_033_obv_63d_change(close, volume)
    m = _rolling_mean(chg, _TD_YEAR)
    sd = _rolling_std(chg, _TD_YEAR)
    return _safe_div(chg - m, sd)


# --- Group E (041-050): Volume-weighted day counts ---

def udv_041_vol_wtd_down_day_count_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted count of down days over 21 days (high-vol down days count more)."""
    avg_vol = _rolling_mean(volume, _TD_MON)
    wt = _safe_div(volume, avg_vol).where(close < close.shift(1), 0.0)
    return _rolling_sum(wt, _TD_MON)


def udv_042_vol_wtd_up_day_count_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted count of up days over 21 days."""
    avg_vol = _rolling_mean(volume, _TD_MON)
    wt = _safe_div(volume, avg_vol).where(close > close.shift(1), 0.0)
    return _rolling_sum(wt, _TD_MON)


def udv_043_vol_wtd_down_day_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted count of down days over 63 days."""
    avg_vol = _rolling_mean(volume, _TD_QTR)
    wt = _safe_div(volume, avg_vol).where(close < close.shift(1), 0.0)
    return _rolling_sum(wt, _TD_QTR)


def udv_044_vol_wtd_up_day_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted count of up days over 63 days."""
    avg_vol = _rolling_mean(volume, _TD_QTR)
    wt = _safe_div(volume, avg_vol).where(close > close.shift(1), 0.0)
    return _rolling_sum(wt, _TD_QTR)


def udv_045_vol_wtd_down_up_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of volume-weighted down count to volume-weighted up count (21d)."""
    return _safe_div(udv_041_vol_wtd_down_day_count_21d(close, volume),
                     udv_042_vol_wtd_up_day_count_21d(close, volume))


def udv_046_vol_wtd_down_up_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of volume-weighted down count to volume-weighted up count (63d)."""
    return _safe_div(udv_043_vol_wtd_down_day_count_63d(close, volume),
                     udv_044_vol_wtd_up_day_count_63d(close, volume))


def udv_047_vol_wtd_down_up_ratio_21d_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 21d vol-weighted down/up ratio within 252-day distribution."""
    s = udv_045_vol_wtd_down_up_ratio_21d(close, volume)
    return s.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def udv_048_vol_wtd_down_count_minus_up_count_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol-weighted down count minus vol-weighted up count (21d net balance)."""
    return (udv_041_vol_wtd_down_day_count_21d(close, volume)
            - udv_042_vol_wtd_up_day_count_21d(close, volume))


def udv_049_vol_wtd_down_count_minus_up_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol-weighted down count minus vol-weighted up count (63d net balance)."""
    return (udv_043_vol_wtd_down_day_count_63d(close, volume)
            - udv_044_vol_wtd_up_day_count_63d(close, volume))


def udv_050_vol_wtd_down_frac_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol-weighted down count as fraction of total vol-weighted day count (21d)."""
    d = udv_041_vol_wtd_down_day_count_21d(close, volume)
    u = udv_042_vol_wtd_up_day_count_21d(close, volume)
    return _safe_div(d, d + u)


# --- Group F (051-060): Volume on worst-return days ---

def udv_051_vol_share_worst5_ret_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 63-day total volume on the 5 worst-return days in that window."""
    ret = close.pct_change(1)
    tv = _rolling_sum(volume, _TD_QTR)
    def _worst5_vol_share(idx):
        if idx < _TD_QTR - 1:
            return np.nan
        r_window = ret.iloc[idx - _TD_QTR + 1: idx + 1]
        v_window = volume.iloc[idx - _TD_QTR + 1: idx + 1]
        threshold = r_window.nsmallest(5).max()
        worst_vol = v_window[r_window <= threshold].sum()
        total = v_window.sum()
        return worst_vol / total if total > 0 else np.nan
    n = len(close)
    result = pd.Series(np.nan, index=close.index)
    for i in range(_TD_QTR - 1, n):
        r_w = ret.iloc[i - _TD_QTR + 1: i + 1]
        v_w = volume.iloc[i - _TD_QTR + 1: i + 1]
        threshold = r_w.nsmallest(5).max()
        worst_vol = v_w[r_w <= threshold].sum()
        total = v_w.sum()
        result.iloc[i] = worst_vol / total if total > 0 else np.nan
    return result


def udv_052_avg_vol_worst_ret_quintile_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume on the bottom-quintile return days over trailing 21 days."""
    ret = close.pct_change(1)
    q20 = ret.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.20)
    worst_vol = volume.where(ret <= q20, np.nan)
    return worst_vol.rolling(_TD_MON, min_periods=1).mean()


def udv_053_avg_vol_worst_ret_quintile_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume on the bottom-quintile return days over trailing 63 days."""
    ret = close.pct_change(1)
    q20 = ret.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.20)
    worst_vol = volume.where(ret <= q20, np.nan)
    return worst_vol.rolling(_TD_QTR, min_periods=1).mean()


def udv_054_vol_ratio_worst_vs_best_quintile_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of avg vol on bottom-quintile days to avg vol on top-quintile days (21d)."""
    ret = close.pct_change(1)
    q20 = ret.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.20)
    q80 = ret.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.80)
    worst_vol = volume.where(ret <= q20, np.nan).rolling(_TD_MON, min_periods=1).mean()
    best_vol = volume.where(ret >= q80, np.nan).rolling(_TD_MON, min_periods=1).mean()
    return _safe_div(worst_vol, best_vol)


def udv_055_vol_ratio_worst_vs_best_quintile_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of avg vol on bottom-quintile days to avg vol on top-quintile days (63d)."""
    ret = close.pct_change(1)
    q20 = ret.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.20)
    q80 = ret.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.80)
    worst_vol = volume.where(ret <= q20, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    best_vol = volume.where(ret >= q80, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    return _safe_div(worst_vol, best_vol)


def udv_056_vol_on_down_days_vs_total_avg_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg down-day volume divided by overall avg daily volume (21d); >1 = heavier selling."""
    avg_down = udv_001_avg_down_vol_21d(close, volume)
    avg_all = _rolling_mean(volume, _TD_MON)
    return _safe_div(avg_down, avg_all)


def udv_057_vol_on_down_days_vs_total_avg_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg down-day volume divided by overall avg daily volume (63d)."""
    avg_down = udv_003_avg_down_vol_63d(close, volume)
    avg_all = _rolling_mean(volume, _TD_QTR)
    return _safe_div(avg_down, avg_all)


def udv_058_vol_on_up_days_vs_total_avg_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg up-day volume divided by overall avg daily volume (21d); <1 = weak buying."""
    avg_up = udv_002_avg_up_vol_21d(close, volume)
    avg_all = _rolling_mean(volume, _TD_MON)
    return _safe_div(avg_up, avg_all)


def udv_059_vol_on_up_days_vs_total_avg_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg up-day volume divided by overall avg daily volume (63d)."""
    avg_up = udv_004_avg_up_vol_63d(close, volume)
    avg_all = _rolling_mean(volume, _TD_QTR)
    return _safe_div(avg_up, avg_all)


def udv_060_sum_down_vol_ratio_63d_vs_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 63-day total down-day volume to 252-day total down-day volume (recency)."""
    s63 = udv_013_sum_down_vol_63d(close, volume)
    s252 = udv_015_sum_down_vol_252d(close, volume)
    return _safe_div(s63, s252)


# --- Group G (061-075): Down/up volume asymmetry and EWM variants ---

def udv_061_down_up_vol_ratio_ewm21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """EWM21 ratio of down-day volume to up-day volume (exponential weighting)."""
    dv = volume.where(close < close.shift(1), 0.0)
    uv = volume.where(close > close.shift(1), 0.0)
    edv = _ewm_mean(dv, _TD_MON)
    euv = _ewm_mean(uv, _TD_MON)
    return _safe_div(edv, euv)


def udv_062_down_up_vol_ratio_ewm63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """EWM63 ratio of down-day volume to up-day volume."""
    dv = volume.where(close < close.shift(1), 0.0)
    uv = volume.where(close > close.shift(1), 0.0)
    edv = _ewm_mean(dv, _TD_QTR)
    euv = _ewm_mean(uv, _TD_QTR)
    return _safe_div(edv, euv)


def udv_063_net_vol_ewm21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """EWM21 of signed volume (positive on up days, negative on down days)."""
    signed = volume.where(close > close.shift(1), -volume)
    signed = signed.where(close != close.shift(1), 0.0)
    return _ewm_mean(signed, _TD_MON)


def udv_064_net_vol_ewm63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """EWM63 of signed volume."""
    signed = volume.where(close > close.shift(1), -volume)
    signed = signed.where(close != close.shift(1), 0.0)
    return _ewm_mean(signed, _TD_QTR)


def udv_065_down_vol_share_ewm21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """EWM21 of down-vol share (down-vol / total-vol per day, then smoothed)."""
    ret = close.diff(1)
    dv_frac = volume.where(ret < 0, 0.0) / volume.replace(0, np.nan)
    return _ewm_mean(dv_frac, _TD_MON)


def udv_066_down_vol_share_ewm63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """EWM63 of down-vol share."""
    ret = close.diff(1)
    dv_frac = volume.where(ret < 0, 0.0) / volume.replace(0, np.nan)
    return _ewm_mean(dv_frac, _TD_QTR)


def udv_067_down_up_vol_ratio_21d_vs_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 21-day down/up avg-vol ratio to 252-day down/up avg-vol ratio (recency premium)."""
    r21 = udv_007_down_up_avg_vol_ratio_21d(close, volume)
    r252 = udv_009_down_up_avg_vol_ratio_252d(close, volume)
    return _safe_div(r21, r252)


def udv_068_down_up_vol_ratio_63d_vs_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 63-day to 252-day down/up avg-vol ratio."""
    r63 = udv_008_down_up_avg_vol_ratio_63d(close, volume)
    r252 = udv_009_down_up_avg_vol_ratio_252d(close, volume)
    return _safe_div(r63, r252)


def udv_069_net_vol_21d_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day net volume within trailing 252-day distribution."""
    s = udv_017_net_vol_21d(close, volume)
    return s.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def udv_070_net_vol_63d_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 63-day net volume within trailing 252-day distribution."""
    s = udv_018_net_vol_63d(close, volume)
    return s.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def udv_071_down_vol_share_21d_expanding_rank(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of 21-day down-vol share."""
    s = udv_021_down_vol_share_21d(close, volume)
    return s.expanding(min_periods=5).rank(pct=True)


def udv_072_down_up_vol_ratio_21d_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 21-day down/up avg-vol ratio relative to 252-day distribution."""
    s = udv_007_down_up_avg_vol_ratio_21d(close, volume)
    m = _rolling_mean(s, _TD_YEAR)
    sd = _rolling_std(s, _TD_YEAR)
    return _safe_div(s - m, sd)


def udv_073_vol_asymmetry_index_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(down_vol_share - 0.5) * 2 scaled to [-1,+1]; positive = distribution dominance (21d)."""
    share = udv_021_down_vol_share_21d(close, volume)
    return (share - 0.5) * 2.0


def udv_074_vol_asymmetry_index_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(down_vol_share - 0.5) * 2 scaled to [-1,+1] over 63 days."""
    share = udv_022_down_vol_share_63d(close, volume)
    return (share - 0.5) * 2.0


def udv_075_down_vol_share_21d_above_63d_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: 21-day down-vol share exceeds 63-day down-vol share (recent acceleration)."""
    s21 = udv_021_down_vol_share_21d(close, volume)
    s63 = udv_022_down_vol_share_63d(close, volume)
    return (s21 > s63).astype(float)


# --- Group H (151-175): New window variants, streaks, normalized flows, log-odds ---

def udv_151_down_vol_share_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of total 126-day volume occurring on down-price days."""
    dv = _rolling_sum(volume.where(close < close.shift(1), 0.0), _TD_HALF)
    tv = _rolling_sum(volume, _TD_HALF)
    return _safe_div(dv, tv)


def udv_152_up_vol_share_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of total 126-day volume occurring on up-price days."""
    uv = _rolling_sum(volume.where(close > close.shift(1), 0.0), _TD_HALF)
    tv = _rolling_sum(volume, _TD_HALF)
    return _safe_div(uv, tv)


def udv_153_down_up_avg_vol_ratio_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of avg down-day volume to avg up-day volume over 126 days."""
    dv = volume.where(close < close.shift(1), np.nan).rolling(_TD_HALF, min_periods=_TD_QTR // 2).mean()
    uv = volume.where(close > close.shift(1), np.nan).rolling(_TD_HALF, min_periods=_TD_QTR // 2).mean()
    return _safe_div(dv, uv)


def udv_154_net_vol_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Net volume (up minus down) over trailing 126 days."""
    uv = _rolling_sum(volume.where(close > close.shift(1), 0.0), _TD_HALF)
    dv = _rolling_sum(volume.where(close < close.shift(1), 0.0), _TD_HALF)
    return uv - dv


def udv_155_obv_126d_change(close: pd.Series, volume: pd.Series) -> pd.Series:
    """126-day change in OBV (half-year accumulation/distribution momentum)."""
    obv = (np.sign(close.diff(1)).fillna(0) * volume).cumsum()
    return obv.diff(_TD_HALF)


def udv_156_down_vol_share_21d_ema_crossover_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """EWM21 of down-vol share minus EWM63 of down-vol share (short vs med-term distribution)."""
    dv_frac = volume.where(close < close.shift(1), 0.0) / volume.replace(0, np.nan)
    e21 = _ewm_mean(dv_frac, _TD_MON)
    e63 = _ewm_mean(dv_frac, _TD_QTR)
    return e21 - e63


def udv_157_vol_surge_on_down_days_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of down days with volume >1.5x the 63-day avg volume, trailing 21 days."""
    avg63 = _rolling_mean(volume, _TD_QTR)
    flag = ((close < close.shift(1)) & (volume > 1.5 * avg63)).astype(float)
    return _rolling_sum(flag, _TD_MON)


def udv_158_vol_surge_on_up_days_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of up days with volume >1.5x the 63-day avg volume, trailing 21 days."""
    avg63 = _rolling_mean(volume, _TD_QTR)
    flag = ((close > close.shift(1)) & (volume > 1.5 * avg63)).astype(float)
    return _rolling_sum(flag, _TD_MON)


def udv_159_down_vol_3x_avg_count_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of down days with volume >3x the 21-day avg, trailing 21 days (panic signals)."""
    avg21 = _rolling_mean(volume, _TD_MON)
    flag = ((close < close.shift(1)) & (volume > 3 * avg21)).astype(float)
    return _rolling_sum(flag, _TD_MON)


def udv_160_down_vol_3x_avg_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of down days with volume >3x the 63-day avg, trailing 63 days."""
    avg63 = _rolling_mean(volume, _TD_QTR)
    flag = ((close < close.shift(1)) & (volume > 3 * avg63)).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def udv_161_net_vol_21d_sign_consecutive_neg_streak(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling count of trailing consecutive days where 21-day net volume is negative."""
    net = _rolling_sum(volume.where(close > close.shift(1), 0.0), _TD_MON) - \
          _rolling_sum(volume.where(close < close.shift(1), 0.0), _TD_MON)
    is_neg = (net < 0).astype(float)
    streak = is_neg * (is_neg.groupby((is_neg != is_neg.shift(1)).cumsum()).cumcount() + 1)
    return streak


def udv_162_down_vol_share_21d_above_75pct_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: 21-day down-vol share exceeds 75% (extreme distress signal)."""
    return (udv_021_down_vol_share_21d(close, volume) > 0.75).astype(float)


def udv_163_vol_on_consecutive_down_days_3d_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 21-day volume on days that are the 3rd consecutive down day."""
    down = close < close.shift(1)
    consec3 = (down & down.shift(1).fillna(0).astype(bool) & down.shift(2).fillna(0).astype(bool)).astype(float)
    cv = _rolling_sum(volume * consec3, _TD_MON)
    tv = _rolling_sum(volume, _TD_MON)
    return _safe_div(cv, tv)


def udv_164_obv_norm_by_avg_vol_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day OBV change normalized by 63-day average total volume."""
    obv = (np.sign(close.diff(1)).fillna(0) * volume).cumsum()
    chg63 = obv.diff(_TD_QTR)
    avg_tv = _rolling_mean(volume, _TD_QTR)
    return _safe_div(chg63, avg_tv * _TD_QTR)


def udv_165_down_vol_share_21d_pct_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day down-vol share within trailing 126-day distribution."""
    s = udv_021_down_vol_share_21d(close, volume)
    return s.rolling(_TD_HALF, min_periods=_TD_QTR // 2).rank(pct=True)


def udv_166_net_vol_21d_norm_by_avg_vol(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day net volume normalized by 21-day average total daily volume."""
    uv = _rolling_sum(volume.where(close > close.shift(1), 0.0), _TD_MON)
    dv = _rolling_sum(volume.where(close < close.shift(1), 0.0), _TD_MON)
    avg_vol = _rolling_mean(volume, _TD_MON)
    return _safe_div(uv - dv, avg_vol * _TD_MON)


def udv_167_net_vol_63d_norm_by_avg_vol(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day net volume normalized by 63-day average total daily volume."""
    uv = _rolling_sum(volume.where(close > close.shift(1), 0.0), _TD_QTR)
    dv = _rolling_sum(volume.where(close < close.shift(1), 0.0), _TD_QTR)
    avg_vol = _rolling_mean(volume, _TD_QTR)
    return _safe_div(uv - dv, avg_vol * _TD_QTR)


def udv_168_down_day_count_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Raw count of down-price days in trailing 21 days."""
    return (close < close.shift(1)).astype(float).rolling(_TD_MON, min_periods=1).sum()


def udv_169_down_day_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Raw count of down-price days in trailing 63 days."""
    return (close < close.shift(1)).astype(float).rolling(_TD_QTR, min_periods=1).sum()


def udv_170_down_day_frac_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of days that are down-days in trailing 21 days."""
    return _safe_div(udv_168_down_day_count_21d(close, volume),
                     pd.Series(_TD_MON, index=close.index, dtype=float))


def udv_171_down_day_frac_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of days that are down-days in trailing 63 days."""
    return _safe_div(udv_169_down_day_count_63d(close, volume),
                     pd.Series(_TD_QTR, index=close.index, dtype=float))


def udv_172_obv_ewm21_vs_ewm63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """EWM21 of OBV minus EWM63 of OBV (short vs medium accumulation trend)."""
    obv = (np.sign(close.diff(1)).fillna(0) * volume).cumsum()
    return _ewm_mean(obv, _TD_MON) - _ewm_mean(obv, _TD_QTR)


def udv_173_down_vol_share_21d_log_odds(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Log-odds of 21-day down-vol share: log(share / (1-share)); positive = distribution."""
    s = udv_021_down_vol_share_21d(close, volume).clip(lower=_EPS, upper=1 - _EPS)
    return np.log(s / (1 - s))


def udv_174_vol_wtd_down_day_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted count of down days over 252 days (high-vol down days count more)."""
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    wt = _safe_div(volume, avg_vol).where(close < close.shift(1), 0.0)
    return _rolling_sum(wt, _TD_YEAR)


def udv_175_net_vol_252d_pct_rank(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day net volume within expanding all-history distribution."""
    uv = _rolling_sum(volume.where(close > close.shift(1), 0.0), _TD_MON)
    dv = _rolling_sum(volume.where(close < close.shift(1), 0.0), _TD_MON)
    net = uv - dv
    return net.expanding(min_periods=5).rank(pct=True)


# ── Registry ──────────────────────────────────────────────────────────────────

UP_DOWN_VOLUME_REGISTRY_001_075 = {
    "udv_001_avg_down_vol_21d": {"inputs": ["close", "volume"], "func": udv_001_avg_down_vol_21d},
    "udv_002_avg_up_vol_21d": {"inputs": ["close", "volume"], "func": udv_002_avg_up_vol_21d},
    "udv_003_avg_down_vol_63d": {"inputs": ["close", "volume"], "func": udv_003_avg_down_vol_63d},
    "udv_004_avg_up_vol_63d": {"inputs": ["close", "volume"], "func": udv_004_avg_up_vol_63d},
    "udv_005_avg_down_vol_252d": {"inputs": ["close", "volume"], "func": udv_005_avg_down_vol_252d},
    "udv_006_avg_up_vol_252d": {"inputs": ["close", "volume"], "func": udv_006_avg_up_vol_252d},
    "udv_007_down_up_avg_vol_ratio_21d": {"inputs": ["close", "volume"], "func": udv_007_down_up_avg_vol_ratio_21d},
    "udv_008_down_up_avg_vol_ratio_63d": {"inputs": ["close", "volume"], "func": udv_008_down_up_avg_vol_ratio_63d},
    "udv_009_down_up_avg_vol_ratio_252d": {"inputs": ["close", "volume"], "func": udv_009_down_up_avg_vol_ratio_252d},
    "udv_010_down_up_avg_vol_ratio_21d_log": {"inputs": ["close", "volume"], "func": udv_010_down_up_avg_vol_ratio_21d_log},
    "udv_011_sum_down_vol_21d": {"inputs": ["close", "volume"], "func": udv_011_sum_down_vol_21d},
    "udv_012_sum_up_vol_21d": {"inputs": ["close", "volume"], "func": udv_012_sum_up_vol_21d},
    "udv_013_sum_down_vol_63d": {"inputs": ["close", "volume"], "func": udv_013_sum_down_vol_63d},
    "udv_014_sum_up_vol_63d": {"inputs": ["close", "volume"], "func": udv_014_sum_up_vol_63d},
    "udv_015_sum_down_vol_252d": {"inputs": ["close", "volume"], "func": udv_015_sum_down_vol_252d},
    "udv_016_sum_up_vol_252d": {"inputs": ["close", "volume"], "func": udv_016_sum_up_vol_252d},
    "udv_017_net_vol_21d": {"inputs": ["close", "volume"], "func": udv_017_net_vol_21d},
    "udv_018_net_vol_63d": {"inputs": ["close", "volume"], "func": udv_018_net_vol_63d},
    "udv_019_net_vol_252d": {"inputs": ["close", "volume"], "func": udv_019_net_vol_252d},
    "udv_020_sum_down_up_vol_ratio_21d": {"inputs": ["close", "volume"], "func": udv_020_sum_down_up_vol_ratio_21d},
    "udv_021_down_vol_share_21d": {"inputs": ["close", "volume"], "func": udv_021_down_vol_share_21d},
    "udv_022_down_vol_share_63d": {"inputs": ["close", "volume"], "func": udv_022_down_vol_share_63d},
    "udv_023_down_vol_share_252d": {"inputs": ["close", "volume"], "func": udv_023_down_vol_share_252d},
    "udv_024_up_vol_share_21d": {"inputs": ["close", "volume"], "func": udv_024_up_vol_share_21d},
    "udv_025_up_vol_share_63d": {"inputs": ["close", "volume"], "func": udv_025_up_vol_share_63d},
    "udv_026_down_vol_share_minus_up_vol_share_21d": {"inputs": ["close", "volume"], "func": udv_026_down_vol_share_minus_up_vol_share_21d},
    "udv_027_down_vol_share_minus_up_vol_share_63d": {"inputs": ["close", "volume"], "func": udv_027_down_vol_share_minus_up_vol_share_63d},
    "udv_028_down_vol_share_pct_rank_252d": {"inputs": ["close", "volume"], "func": udv_028_down_vol_share_pct_rank_252d},
    "udv_029_down_vol_share_zscore_252d": {"inputs": ["close", "volume"], "func": udv_029_down_vol_share_zscore_252d},
    "udv_030_down_vol_share_21d_gt60_flag": {"inputs": ["close", "volume"], "func": udv_030_down_vol_share_21d_gt60_flag},
    "udv_031_obv_raw": {"inputs": ["close", "volume"], "func": udv_031_obv_raw},
    "udv_032_obv_21d_change": {"inputs": ["close", "volume"], "func": udv_032_obv_21d_change},
    "udv_033_obv_63d_change": {"inputs": ["close", "volume"], "func": udv_033_obv_63d_change},
    "udv_034_obv_norm_by_avg_vol_21d": {"inputs": ["close", "volume"], "func": udv_034_obv_norm_by_avg_vol_21d},
    "udv_035_obv_sma21": {"inputs": ["close", "volume"], "func": udv_035_obv_sma21},
    "udv_036_obv_vs_sma21": {"inputs": ["close", "volume"], "func": udv_036_obv_vs_sma21},
    "udv_037_obv_sma_crossover_21_63": {"inputs": ["close", "volume"], "func": udv_037_obv_sma_crossover_21_63},
    "udv_038_obv_pct_rank_252d": {"inputs": ["close", "volume"], "func": udv_038_obv_pct_rank_252d},
    "udv_039_obv_21d_change_sign": {"inputs": ["close", "volume"], "func": udv_039_obv_21d_change_sign},
    "udv_040_obv_63d_zscore": {"inputs": ["close", "volume"], "func": udv_040_obv_63d_zscore},
    "udv_041_vol_wtd_down_day_count_21d": {"inputs": ["close", "volume"], "func": udv_041_vol_wtd_down_day_count_21d},
    "udv_042_vol_wtd_up_day_count_21d": {"inputs": ["close", "volume"], "func": udv_042_vol_wtd_up_day_count_21d},
    "udv_043_vol_wtd_down_day_count_63d": {"inputs": ["close", "volume"], "func": udv_043_vol_wtd_down_day_count_63d},
    "udv_044_vol_wtd_up_day_count_63d": {"inputs": ["close", "volume"], "func": udv_044_vol_wtd_up_day_count_63d},
    "udv_045_vol_wtd_down_up_ratio_21d": {"inputs": ["close", "volume"], "func": udv_045_vol_wtd_down_up_ratio_21d},
    "udv_046_vol_wtd_down_up_ratio_63d": {"inputs": ["close", "volume"], "func": udv_046_vol_wtd_down_up_ratio_63d},
    "udv_047_vol_wtd_down_up_ratio_21d_pct_rank_252d": {"inputs": ["close", "volume"], "func": udv_047_vol_wtd_down_up_ratio_21d_pct_rank_252d},
    "udv_048_vol_wtd_down_count_minus_up_count_21d": {"inputs": ["close", "volume"], "func": udv_048_vol_wtd_down_count_minus_up_count_21d},
    "udv_049_vol_wtd_down_count_minus_up_count_63d": {"inputs": ["close", "volume"], "func": udv_049_vol_wtd_down_count_minus_up_count_63d},
    "udv_050_vol_wtd_down_frac_21d": {"inputs": ["close", "volume"], "func": udv_050_vol_wtd_down_frac_21d},
    "udv_051_vol_share_worst5_ret_days_63d": {"inputs": ["close", "volume"], "func": udv_051_vol_share_worst5_ret_days_63d},
    "udv_052_avg_vol_worst_ret_quintile_21d": {"inputs": ["close", "volume"], "func": udv_052_avg_vol_worst_ret_quintile_21d},
    "udv_053_avg_vol_worst_ret_quintile_63d": {"inputs": ["close", "volume"], "func": udv_053_avg_vol_worst_ret_quintile_63d},
    "udv_054_vol_ratio_worst_vs_best_quintile_21d": {"inputs": ["close", "volume"], "func": udv_054_vol_ratio_worst_vs_best_quintile_21d},
    "udv_055_vol_ratio_worst_vs_best_quintile_63d": {"inputs": ["close", "volume"], "func": udv_055_vol_ratio_worst_vs_best_quintile_63d},
    "udv_056_vol_on_down_days_vs_total_avg_ratio_21d": {"inputs": ["close", "volume"], "func": udv_056_vol_on_down_days_vs_total_avg_ratio_21d},
    "udv_057_vol_on_down_days_vs_total_avg_ratio_63d": {"inputs": ["close", "volume"], "func": udv_057_vol_on_down_days_vs_total_avg_ratio_63d},
    "udv_058_vol_on_up_days_vs_total_avg_ratio_21d": {"inputs": ["close", "volume"], "func": udv_058_vol_on_up_days_vs_total_avg_ratio_21d},
    "udv_059_vol_on_up_days_vs_total_avg_ratio_63d": {"inputs": ["close", "volume"], "func": udv_059_vol_on_up_days_vs_total_avg_ratio_63d},
    "udv_060_sum_down_vol_ratio_63d_vs_252d": {"inputs": ["close", "volume"], "func": udv_060_sum_down_vol_ratio_63d_vs_252d},
    "udv_061_down_up_vol_ratio_ewm21": {"inputs": ["close", "volume"], "func": udv_061_down_up_vol_ratio_ewm21},
    "udv_062_down_up_vol_ratio_ewm63": {"inputs": ["close", "volume"], "func": udv_062_down_up_vol_ratio_ewm63},
    "udv_063_net_vol_ewm21": {"inputs": ["close", "volume"], "func": udv_063_net_vol_ewm21},
    "udv_064_net_vol_ewm63": {"inputs": ["close", "volume"], "func": udv_064_net_vol_ewm63},
    "udv_065_down_vol_share_ewm21": {"inputs": ["close", "volume"], "func": udv_065_down_vol_share_ewm21},
    "udv_066_down_vol_share_ewm63": {"inputs": ["close", "volume"], "func": udv_066_down_vol_share_ewm63},
    "udv_067_down_up_vol_ratio_21d_vs_252d": {"inputs": ["close", "volume"], "func": udv_067_down_up_vol_ratio_21d_vs_252d},
    "udv_068_down_up_vol_ratio_63d_vs_252d": {"inputs": ["close", "volume"], "func": udv_068_down_up_vol_ratio_63d_vs_252d},
    "udv_069_net_vol_21d_pct_rank_252d": {"inputs": ["close", "volume"], "func": udv_069_net_vol_21d_pct_rank_252d},
    "udv_070_net_vol_63d_pct_rank_252d": {"inputs": ["close", "volume"], "func": udv_070_net_vol_63d_pct_rank_252d},
    "udv_071_down_vol_share_21d_expanding_rank": {"inputs": ["close", "volume"], "func": udv_071_down_vol_share_21d_expanding_rank},
    "udv_072_down_up_vol_ratio_21d_zscore_252d": {"inputs": ["close", "volume"], "func": udv_072_down_up_vol_ratio_21d_zscore_252d},
    "udv_073_vol_asymmetry_index_21d": {"inputs": ["close", "volume"], "func": udv_073_vol_asymmetry_index_21d},
    "udv_074_vol_asymmetry_index_63d": {"inputs": ["close", "volume"], "func": udv_074_vol_asymmetry_index_63d},
    "udv_075_down_vol_share_21d_above_63d_flag": {"inputs": ["close", "volume"], "func": udv_075_down_vol_share_21d_above_63d_flag},
    "udv_151_down_vol_share_126d": {"inputs": ["close", "volume"], "func": udv_151_down_vol_share_126d},
    "udv_152_up_vol_share_126d": {"inputs": ["close", "volume"], "func": udv_152_up_vol_share_126d},
    "udv_153_down_up_avg_vol_ratio_126d": {"inputs": ["close", "volume"], "func": udv_153_down_up_avg_vol_ratio_126d},
    "udv_154_net_vol_126d": {"inputs": ["close", "volume"], "func": udv_154_net_vol_126d},
    "udv_155_obv_126d_change": {"inputs": ["close", "volume"], "func": udv_155_obv_126d_change},
    "udv_156_down_vol_share_21d_ema_crossover_63d": {"inputs": ["close", "volume"], "func": udv_156_down_vol_share_21d_ema_crossover_63d},
    "udv_157_vol_surge_on_down_days_21d": {"inputs": ["close", "volume"], "func": udv_157_vol_surge_on_down_days_21d},
    "udv_158_vol_surge_on_up_days_21d": {"inputs": ["close", "volume"], "func": udv_158_vol_surge_on_up_days_21d},
    "udv_159_down_vol_3x_avg_count_21d": {"inputs": ["close", "volume"], "func": udv_159_down_vol_3x_avg_count_21d},
    "udv_160_down_vol_3x_avg_count_63d": {"inputs": ["close", "volume"], "func": udv_160_down_vol_3x_avg_count_63d},
    "udv_161_net_vol_21d_sign_consecutive_neg_streak": {"inputs": ["close", "volume"], "func": udv_161_net_vol_21d_sign_consecutive_neg_streak},
    "udv_162_down_vol_share_21d_above_75pct_flag": {"inputs": ["close", "volume"], "func": udv_162_down_vol_share_21d_above_75pct_flag},
    "udv_163_vol_on_consecutive_down_days_3d_21d": {"inputs": ["close", "volume"], "func": udv_163_vol_on_consecutive_down_days_3d_21d},
    "udv_164_obv_norm_by_avg_vol_63d": {"inputs": ["close", "volume"], "func": udv_164_obv_norm_by_avg_vol_63d},
    "udv_165_down_vol_share_21d_pct_rank_126d": {"inputs": ["close", "volume"], "func": udv_165_down_vol_share_21d_pct_rank_126d},
    "udv_166_net_vol_21d_norm_by_avg_vol": {"inputs": ["close", "volume"], "func": udv_166_net_vol_21d_norm_by_avg_vol},
    "udv_167_net_vol_63d_norm_by_avg_vol": {"inputs": ["close", "volume"], "func": udv_167_net_vol_63d_norm_by_avg_vol},
    "udv_168_down_day_count_21d": {"inputs": ["close", "volume"], "func": udv_168_down_day_count_21d},
    "udv_169_down_day_count_63d": {"inputs": ["close", "volume"], "func": udv_169_down_day_count_63d},
    "udv_170_down_day_frac_21d": {"inputs": ["close", "volume"], "func": udv_170_down_day_frac_21d},
    "udv_171_down_day_frac_63d": {"inputs": ["close", "volume"], "func": udv_171_down_day_frac_63d},
    "udv_172_obv_ewm21_vs_ewm63": {"inputs": ["close", "volume"], "func": udv_172_obv_ewm21_vs_ewm63},
    "udv_173_down_vol_share_21d_log_odds": {"inputs": ["close", "volume"], "func": udv_173_down_vol_share_21d_log_odds},
    "udv_174_vol_wtd_down_day_count_252d": {"inputs": ["close", "volume"], "func": udv_174_vol_wtd_down_day_count_252d},
    "udv_175_net_vol_252d_pct_rank": {"inputs": ["close", "volume"], "func": udv_175_net_vol_252d_pct_rank},
}
