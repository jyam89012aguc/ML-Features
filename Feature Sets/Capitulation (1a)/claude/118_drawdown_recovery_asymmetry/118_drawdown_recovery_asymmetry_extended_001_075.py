"""
118_drawdown_recovery_asymmetry — Extended Features 001-075
Domain: asymmetry between down-legs and up-legs within the price path —
        deeper variants: multi-bar run analysis, high/low open-to-close asymmetry,
        volume-weighted ratchet geometry, expanding/regime-aware asymmetry,
        high-frequency tail analysis, cross-window asymmetry composites,
        ATR-normalized leg comparison.
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


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _atr(high: pd.Series, low: pd.Series, close: pd.Series, w: int) -> pd.Series:
    """Average True Range over window w."""
    prev_close = close.shift(1)
    tr = pd.concat([high - low,
                    (high - prev_close).abs(),
                    (low - prev_close).abs()], axis=1).max(axis=1)
    return _rolling_mean(tr, w)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Multi-bar run analysis ---

def dra_ext_001_avg_dn_run_length_21d(close: pd.Series) -> pd.Series:
    """Mean length of down-runs (consecutive dn-day segments) over 21 days.
    Measures how many days a typical decline sustains before a reversal."""
    ret = close.pct_change(1)
    dn = (ret < 0).astype(int)
    # Tag end-of-run: last bar of each down-run
    ends = dn & (dn.shift(-1, fill_value=0) == 0)
    cur_len = _consec_streak(ret < 0)
    run_len = cur_len.where(ends.astype(bool))
    return run_len.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def dra_ext_002_avg_up_run_length_21d(close: pd.Series) -> pd.Series:
    """Mean length of up-runs (consecutive up-day segments) over 21 days."""
    ret = close.pct_change(1)
    up = (ret > 0).astype(int)
    ends = up & (up.shift(-1, fill_value=0) == 0)
    cur_len = _consec_streak(ret > 0)
    run_len = cur_len.where(ends.astype(bool))
    return run_len.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def dra_ext_003_run_length_ratio_21d(close: pd.Series) -> pd.Series:
    """Ratio of mean dn-run length to mean up-run length over 21 days."""
    return _safe_div(dra_ext_001_avg_dn_run_length_21d(close),
                     dra_ext_002_avg_up_run_length_21d(close))


def dra_ext_004_avg_dn_run_length_63d(close: pd.Series) -> pd.Series:
    """Mean length of down-runs over 63 days."""
    ret = close.pct_change(1)
    dn = (ret < 0).astype(int)
    ends = dn & (dn.shift(-1, fill_value=0) == 0)
    cur_len = _consec_streak(ret < 0)
    run_len = cur_len.where(ends.astype(bool))
    return run_len.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


def dra_ext_005_avg_up_run_length_63d(close: pd.Series) -> pd.Series:
    """Mean length of up-runs over 63 days."""
    ret = close.pct_change(1)
    up = (ret > 0).astype(int)
    ends = up & (up.shift(-1, fill_value=0) == 0)
    cur_len = _consec_streak(ret > 0)
    run_len = cur_len.where(ends.astype(bool))
    return run_len.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


def dra_ext_006_run_length_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio of mean dn-run length to mean up-run length over 63 days."""
    return _safe_div(dra_ext_004_avg_dn_run_length_63d(close),
                     dra_ext_005_avg_up_run_length_63d(close))


def dra_ext_007_dn_run_magnitude_21d(close: pd.Series) -> pd.Series:
    """Mean magnitude of completed down-runs (cumulative dn-ret per run) over 21 days."""
    ret = close.pct_change(1)
    dn_mag = (-ret).clip(lower=0.0)
    dn = (ret < 0).astype(int)
    ends = dn & (dn.shift(-1, fill_value=0) == 0)
    group = (~(ret < 0)).cumsum()
    cum_dn = dn_mag.groupby(group).cumsum()
    run_mag = cum_dn.where(ends.astype(bool))
    return run_mag.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def dra_ext_008_up_run_magnitude_21d(close: pd.Series) -> pd.Series:
    """Mean magnitude of completed up-runs (cumulative up-ret per run) over 21 days."""
    ret = close.pct_change(1)
    up_mag = ret.clip(lower=0.0)
    up = (ret > 0).astype(int)
    ends = up & (up.shift(-1, fill_value=0) == 0)
    group = (~(ret > 0)).cumsum()
    cum_up = up_mag.groupby(group).cumsum()
    run_mag = cum_up.where(ends.astype(bool))
    return run_mag.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def dra_ext_009_run_magnitude_ratio_21d(close: pd.Series) -> pd.Series:
    """Ratio of mean dn-run magnitude to mean up-run magnitude over 21 days."""
    return _safe_div(dra_ext_007_dn_run_magnitude_21d(close),
                     dra_ext_008_up_run_magnitude_21d(close))


def dra_ext_010_num_dn_runs_21d(close: pd.Series) -> pd.Series:
    """Count of distinct down-runs completed in trailing 21 days."""
    ret = close.pct_change(1)
    dn = (ret < 0).astype(int)
    ends = (dn & (dn.shift(-1, fill_value=0) == 0)).astype(float)
    return _rolling_sum(ends, _TD_MON)


# --- Group B (011-020): ATR-normalized leg asymmetry ---

def dra_ext_011_dn_ret_atr_norm_21d(close: pd.Series, high: pd.Series,
                                     low: pd.Series) -> pd.Series:
    """Mean down-day return normalized by ATR over 21 days."""
    dn = (-close.pct_change(1)).clip(lower=0.0)
    atr21 = _atr(high, low, close, _TD_MON)
    normed = _safe_div(dn, atr21.replace(0, np.nan))
    return _rolling_mean(normed, _TD_MON)


def dra_ext_012_up_ret_atr_norm_21d(close: pd.Series, high: pd.Series,
                                     low: pd.Series) -> pd.Series:
    """Mean up-day return normalized by ATR over 21 days."""
    up = close.pct_change(1).clip(lower=0.0)
    atr21 = _atr(high, low, close, _TD_MON)
    normed = _safe_div(up, atr21.replace(0, np.nan))
    return _rolling_mean(normed, _TD_MON)


def dra_ext_013_atr_norm_dn_up_ratio_21d(close: pd.Series, high: pd.Series,
                                          low: pd.Series) -> pd.Series:
    """Ratio of ATR-normalized mean dn to ATR-normalized mean up over 21 days."""
    return _safe_div(dra_ext_011_dn_ret_atr_norm_21d(close, high, low),
                     dra_ext_012_up_ret_atr_norm_21d(close, high, low))


def dra_ext_014_dn_ret_atr_norm_63d(close: pd.Series, high: pd.Series,
                                     low: pd.Series) -> pd.Series:
    """Mean down-day return normalized by ATR over 63 days."""
    dn = (-close.pct_change(1)).clip(lower=0.0)
    atr63 = _atr(high, low, close, _TD_QTR)
    normed = _safe_div(dn, atr63.replace(0, np.nan))
    return _rolling_mean(normed, _TD_QTR)


def dra_ext_015_up_ret_atr_norm_63d(close: pd.Series, high: pd.Series,
                                     low: pd.Series) -> pd.Series:
    """Mean up-day return normalized by ATR over 63 days."""
    up = close.pct_change(1).clip(lower=0.0)
    atr63 = _atr(high, low, close, _TD_QTR)
    normed = _safe_div(up, atr63.replace(0, np.nan))
    return _rolling_mean(normed, _TD_QTR)


def dra_ext_016_atr_norm_dn_up_ratio_63d(close: pd.Series, high: pd.Series,
                                          low: pd.Series) -> pd.Series:
    """Ratio of ATR-normalized mean dn to mean up over 63 days."""
    return _safe_div(dra_ext_014_dn_ret_atr_norm_63d(close, high, low),
                     dra_ext_015_up_ret_atr_norm_63d(close, high, low))


def dra_ext_017_dn_range_atr_ratio_21d(close: pd.Series, high: pd.Series,
                                        low: pd.Series) -> pd.Series:
    """Mean daily down-range (prev_close - low) normalized by ATR over 21 days."""
    prev = close.shift(1)
    dn_range = (prev - low).clip(lower=0.0)
    atr21 = _atr(high, low, close, _TD_MON)
    normed = _safe_div(dn_range, atr21.replace(0, np.nan))
    return _rolling_mean(normed, _TD_MON)


def dra_ext_018_up_range_atr_ratio_21d(close: pd.Series, high: pd.Series,
                                        low: pd.Series) -> pd.Series:
    """Mean daily up-range (high - prev_close) normalized by ATR over 21 days."""
    prev = close.shift(1)
    up_range = (high - prev).clip(lower=0.0)
    atr21 = _atr(high, low, close, _TD_MON)
    normed = _safe_div(up_range, atr21.replace(0, np.nan))
    return _rolling_mean(normed, _TD_MON)


def dra_ext_019_dn_up_range_ratio_21d(close: pd.Series, high: pd.Series,
                                       low: pd.Series) -> pd.Series:
    """Ratio of ATR-normalized dn-range to up-range over 21 days."""
    return _safe_div(dra_ext_017_dn_range_atr_ratio_21d(close, high, low),
                     dra_ext_018_up_range_atr_ratio_21d(close, high, low))


def dra_ext_020_intraday_dn_pressure_21d(close: pd.Series, high: pd.Series,
                                          low: pd.Series, open_: pd.Series) -> pd.Series:
    """Mean fraction of day's total range traded below open over 21 days.
    (open - low) / (high - low). High = intraday selling pressure dominates."""
    rng = (high - low).replace(0, np.nan)
    below_open = (open_ - low).clip(lower=0.0)
    frac = _safe_div(below_open, rng)
    return _rolling_mean(frac, _TD_MON)


# --- Group C (021-030): Expanding / regime-aware asymmetry ---

def dra_ext_021_gain_loss_ratio_expanding_min(close: pd.Series) -> pd.Series:
    """Expanding all-time minimum of 21d gain/loss ratio (worst ever asymmetry)."""
    ret = close.pct_change(1)
    ratio = _rolling_sum(ret.clip(lower=0.0), _TD_MON) / (
        _rolling_sum((-ret).clip(lower=0.0), _TD_MON) + _EPS)
    return ratio.expanding(min_periods=_TD_MON).min()


def dra_ext_022_vol_asym_expanding_max(close: pd.Series) -> pd.Series:
    """Expanding all-time maximum of 21d vol-asymmetry ratio."""
    ret = close.pct_change(1)
    dn_vol = (-ret).clip(lower=0.0).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).std()
    up_vol = ret.clip(lower=0.0).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).std()
    ratio = _safe_div(dn_vol, up_vol.replace(0, np.nan))
    return ratio.expanding(min_periods=_TD_MON).max()


def dra_ext_023_gain_loss_ratio_current_vs_expanding_min(close: pd.Series) -> pd.Series:
    """Current 21d gain/loss ratio divided by its expanding minimum (1.0 = at the worst)."""
    ret = close.pct_change(1)
    ratio = _rolling_sum(ret.clip(lower=0.0), _TD_MON) / (
        _rolling_sum((-ret).clip(lower=0.0), _TD_MON) + _EPS)
    exp_min = ratio.expanding(min_periods=_TD_MON).min()
    return _safe_div(ratio, exp_min.replace(0, np.nan))


def dra_ext_024_dn_participation_expanding_max(close: pd.Series) -> pd.Series:
    """Expanding all-time maximum of 21d dn-participation rate."""
    ret = close.pct_change(1)
    dn_sq = _rolling_sum(((-ret).clip(lower=0.0)) ** 2, _TD_MON)
    up_sq = _rolling_sum((ret.clip(lower=0.0)) ** 2, _TD_MON)
    rate = _safe_div(dn_sq, dn_sq + up_sq + _EPS)
    return rate.expanding(min_periods=_TD_MON).max()


def dra_ext_025_speed_asym_expanding_max(close: pd.Series) -> pd.Series:
    """Expanding all-time maximum of 21d speed-asymmetry ratio."""
    ret = close.pct_change(1)
    dn_sum = _rolling_sum((-ret).clip(lower=0.0), _TD_MON)
    dn_cnt = _rolling_sum((ret < 0).astype(float), _TD_MON).replace(0, np.nan)
    up_sum = _rolling_sum(ret.clip(lower=0.0), _TD_MON)
    up_cnt = _rolling_sum((ret > 0).astype(float), _TD_MON).replace(0, np.nan)
    ratio = _safe_div(_safe_div(dn_sum, dn_cnt), _safe_div(up_sum, up_cnt))
    return ratio.expanding(min_periods=_TD_MON).max()


def dra_ext_026_gain_loss_half_year(close: pd.Series) -> pd.Series:
    """Gain/loss ratio over trailing 126 days (half-year window)."""
    ret = close.pct_change(1)
    up = _rolling_sum(ret.clip(lower=0.0), _TD_HALF)
    dn = _rolling_sum((-ret).clip(lower=0.0), _TD_HALF)
    return _safe_div(up, dn.replace(0, np.nan))


def dra_ext_027_vol_asym_half_year(close: pd.Series) -> pd.Series:
    """Vol-asymmetry ratio (dn_vol / up_vol) over trailing 126 days."""
    ret = close.pct_change(1)
    dn_vol = (-ret).clip(lower=0.0).rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).std()
    up_vol = ret.clip(lower=0.0).rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).std()
    return _safe_div(dn_vol, up_vol.replace(0, np.nan))


def dra_ext_028_dn_participation_half_year(close: pd.Series) -> pd.Series:
    """Downside-participation rate over trailing 126 days."""
    ret = close.pct_change(1)
    dn_sq = _rolling_sum(((-ret).clip(lower=0.0)) ** 2, _TD_HALF)
    up_sq = _rolling_sum((ret.clip(lower=0.0)) ** 2, _TD_HALF)
    return _safe_div(dn_sq, dn_sq + up_sq + _EPS)


def dra_ext_029_gain_loss_ratio_5w(close: pd.Series) -> pd.Series:
    """Gain/loss ratio over trailing 5 weeks (25 days)."""
    w = _TD_WEEK * 5
    ret = close.pct_change(1)
    up = _rolling_sum(ret.clip(lower=0.0), w)
    dn = _rolling_sum((-ret).clip(lower=0.0), w)
    return _safe_div(up, dn.replace(0, np.nan))


def dra_ext_030_speed_asym_half_year(close: pd.Series) -> pd.Series:
    """Speed-asymmetry ratio over trailing 126 days."""
    ret = close.pct_change(1)
    dn_sum = _rolling_sum((-ret).clip(lower=0.0), _TD_HALF)
    dn_cnt = _rolling_sum((ret < 0).astype(float), _TD_HALF).replace(0, np.nan)
    up_sum = _rolling_sum(ret.clip(lower=0.0), _TD_HALF)
    up_cnt = _rolling_sum((ret > 0).astype(float), _TD_HALF).replace(0, np.nan)
    return _safe_div(_safe_div(dn_sum, dn_cnt), _safe_div(up_sum, up_cnt))


# --- Group D (031-040): Tail analysis (large-move asymmetry) ---

def dra_ext_031_top5pct_dn_ret_mean_21d(close: pd.Series) -> pd.Series:
    """Mean of the worst 5% down-day returns over 21 days (tail dn severity)."""
    ret = close.pct_change(1)
    dn = (-ret).clip(lower=0.0)
    def tail_mean(x):
        v = x[x > 0]
        if len(v) == 0:
            return np.nan
        threshold = np.percentile(v, 95)
        tail = v[v >= threshold]
        return tail.mean() if len(tail) > 0 else np.nan
    return dn.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(tail_mean, raw=True)


def dra_ext_032_top5pct_up_ret_mean_21d(close: pd.Series) -> pd.Series:
    """Mean of the best 5% up-day returns over 21 days (tail up strength)."""
    ret = close.pct_change(1)
    up = ret.clip(lower=0.0)
    def tail_mean(x):
        v = x[x > 0]
        if len(v) == 0:
            return np.nan
        threshold = np.percentile(v, 95)
        tail = v[v >= threshold]
        return tail.mean() if len(tail) > 0 else np.nan
    return up.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(tail_mean, raw=True)


def dra_ext_033_tail_dn_up_ratio_21d(close: pd.Series) -> pd.Series:
    """Ratio of top-5% dn tail mean to top-5% up tail mean over 21 days."""
    return _safe_div(dra_ext_031_top5pct_dn_ret_mean_21d(close),
                     dra_ext_032_top5pct_up_ret_mean_21d(close))


def dra_ext_034_large_dn_count_21d(close: pd.Series) -> pd.Series:
    """Count of down days with return > 2% magnitude over trailing 21 days."""
    dn = (-close.pct_change(1)).clip(lower=0.0)
    return _rolling_sum((dn > 0.02).astype(float), _TD_MON)


def dra_ext_035_large_up_count_21d(close: pd.Series) -> pd.Series:
    """Count of up days with return > 2% over trailing 21 days."""
    up = close.pct_change(1).clip(lower=0.0)
    return _rolling_sum((up > 0.02).astype(float), _TD_MON)


def dra_ext_036_large_dn_vs_up_count_ratio_21d(close: pd.Series) -> pd.Series:
    """Ratio of large-dn-day count to large-up-day count over 21 days."""
    return _safe_div(dra_ext_034_large_dn_count_21d(close),
                     dra_ext_035_large_up_count_21d(close))


def dra_ext_037_dn_ret_p90_21d(close: pd.Series) -> pd.Series:
    """90th percentile of down-day return magnitudes over 21 days."""
    dn = (-close.pct_change(1)).clip(lower=0.0)
    return dn.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.9)


def dra_ext_038_up_ret_p90_21d(close: pd.Series) -> pd.Series:
    """90th percentile of up-day return magnitudes over 21 days."""
    up = close.pct_change(1).clip(lower=0.0)
    return up.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.9)


def dra_ext_039_p90_dn_up_ratio_21d(close: pd.Series) -> pd.Series:
    """Ratio of 90th-pctile dn to 90th-pctile up return over 21 days."""
    return _safe_div(dra_ext_037_dn_ret_p90_21d(close), dra_ext_038_up_ret_p90_21d(close))


def dra_ext_040_dn_ret_iqr_21d(close: pd.Series) -> pd.Series:
    """IQR of down-day return magnitudes over 21 days (spread of dn sizes)."""
    dn = (-close.pct_change(1)).clip(lower=0.0)
    q75 = dn.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.75)
    q25 = dn.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.25)
    return q75 - q25


# --- Group E (041-050): Volume-weighted ratchet geometry ---

def dra_ext_041_vol_weighted_ratchet_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted ratchet score: sum of (dn_ret * dn_vol) - (up_ret * up_vol) over 21 days."""
    ret = close.pct_change(1)
    dn_term = (-ret).clip(lower=0.0) * volume
    up_term = ret.clip(lower=0.0) * volume
    return _rolling_sum(dn_term - up_term, _TD_MON)


def dra_ext_042_vol_weighted_gain_loss_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted gain/loss ratio over 21 days: sum(up*vol) / sum(dn*vol)."""
    ret = close.pct_change(1)
    up_term = ret.clip(lower=0.0) * volume
    dn_term = (-ret).clip(lower=0.0) * volume
    return _safe_div(_rolling_sum(up_term, _TD_MON),
                     _rolling_sum(dn_term, _TD_MON).replace(0, np.nan))


def dra_ext_043_vol_weighted_gain_loss_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted gain/loss ratio over 63 days."""
    ret = close.pct_change(1)
    up_term = ret.clip(lower=0.0) * volume
    dn_term = (-ret).clip(lower=0.0) * volume
    return _safe_div(_rolling_sum(up_term, _TD_QTR),
                     _rolling_sum(dn_term, _TD_QTR).replace(0, np.nan))


def dra_ext_044_dn_vol_intensity_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (dn_ret * volume) over 21 days — total volume-weighted downside pressure."""
    ret = close.pct_change(1)
    dn_term = (-ret).clip(lower=0.0) * volume
    return _rolling_sum(dn_term, _TD_MON)


def dra_ext_045_up_vol_intensity_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (up_ret * volume) over 21 days — total volume-weighted upside pressure."""
    ret = close.pct_change(1)
    up_term = ret.clip(lower=0.0) * volume
    return _rolling_sum(up_term, _TD_MON)


def dra_ext_046_vol_intensity_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of dn vol-intensity to up vol-intensity over 21 days."""
    return _safe_div(dra_ext_044_dn_vol_intensity_21d(close, volume),
                     dra_ext_045_up_vol_intensity_21d(close, volume))


def dra_ext_047_high_vol_dn_day_ret_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean dn-day return on high-volume days (volume > 21d median) over 21 days."""
    ret = close.pct_change(1)
    med_vol = _rolling_mean(volume, _TD_MON)
    is_high_vol = volume > med_vol
    dn = (-ret).clip(lower=0.0)
    high_vol_dn = dn.where(is_high_vol & (ret < 0))
    return high_vol_dn.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def dra_ext_048_low_vol_up_day_ret_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean up-day return on low-volume days (volume <= 21d median) over 21 days.
    Low-volume up moves suggest weak recovery (vs high-volume declines)."""
    ret = close.pct_change(1)
    med_vol = _rolling_mean(volume, _TD_MON)
    is_low_vol = volume <= med_vol
    up = ret.clip(lower=0.0)
    low_vol_up = up.where(is_low_vol & (ret > 0))
    return low_vol_up.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def dra_ext_049_high_vol_dn_vs_low_vol_up_ratio_21d(close: pd.Series,
                                                      volume: pd.Series) -> pd.Series:
    """Ratio of mean high-vol dn-day return to mean low-vol up-day return (21d).
    High = heavy-volume falls dominate light-volume recoveries."""
    return _safe_div(dra_ext_047_high_vol_dn_day_ret_21d(close, volume),
                     dra_ext_048_low_vol_up_day_ret_21d(close, volume))


def dra_ext_050_dn_vol_concentration_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Concentration of dn-day volume: max_dn_day_vol / sum_dn_day_vol over 21 days."""
    ret = close.pct_change(1)
    dn_vol = volume.where(ret < 0, 0.0)
    max_dn = _rolling_max(dn_vol, _TD_MON)
    sum_dn = _rolling_sum(dn_vol, _TD_MON)
    return _safe_div(max_dn, sum_dn.replace(0, np.nan))


# --- Group F (051-060): Open-to-close vs prior-close-to-open asymmetry ---

def dra_ext_051_avg_oc_dn_move_21d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Mean open-to-close dn move (open > close) as fraction over 21 days."""
    oc = _safe_div(close - open_, open_.replace(0, np.nan))
    oc_dn = (-oc).clip(lower=0.0)
    return _rolling_mean(oc_dn.where(oc_dn > 0), _TD_MON)


def dra_ext_052_avg_oc_up_move_21d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Mean open-to-close up move (close > open) as fraction over 21 days."""
    oc = _safe_div(close - open_, open_.replace(0, np.nan))
    oc_up = oc.clip(lower=0.0)
    return _rolling_mean(oc_up.where(oc_up > 0), _TD_MON)


def dra_ext_053_oc_asymmetry_ratio_21d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Ratio of mean oc-dn to mean oc-up over 21 days (intraday directional asymmetry)."""
    return _safe_div(dra_ext_051_avg_oc_dn_move_21d(close, open_),
                     dra_ext_052_avg_oc_up_move_21d(close, open_))


def dra_ext_054_overnight_dn_count_21d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Count of days with a negative overnight gap (open < prev_close) in 21 days."""
    gap = _safe_div(open_ - close.shift(1), close.shift(1).replace(0, np.nan))
    return _rolling_sum((gap < 0).astype(float), _TD_MON)


def dra_ext_055_overnight_up_count_21d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Count of days with a positive overnight gap (open > prev_close) in 21 days."""
    gap = _safe_div(open_ - close.shift(1), close.shift(1).replace(0, np.nan))
    return _rolling_sum((gap > 0).astype(float), _TD_MON)


def dra_ext_056_overnight_dn_up_ratio_21d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Ratio of overnight-dn count to overnight-up count over 21 days."""
    return _safe_div(dra_ext_054_overnight_dn_count_21d(close, open_),
                     dra_ext_055_overnight_up_count_21d(close, open_))


def dra_ext_057_mean_overnight_gap_dn_21d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Mean magnitude of negative overnight gaps over 21 days."""
    gap = _safe_div(open_ - close.shift(1), close.shift(1).replace(0, np.nan))
    dn_gap = (-gap).clip(lower=0.0)
    return _rolling_mean(dn_gap.where(dn_gap > 0), _TD_MON)


def dra_ext_058_mean_overnight_gap_up_21d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Mean magnitude of positive overnight gaps over 21 days."""
    gap = _safe_div(open_ - close.shift(1), close.shift(1).replace(0, np.nan))
    up_gap = gap.clip(lower=0.0)
    return _rolling_mean(up_gap.where(up_gap > 0), _TD_MON)


def dra_ext_059_overnight_gap_asymmetry_21d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Ratio of mean dn overnight gap to mean up overnight gap over 21 days."""
    return _safe_div(dra_ext_057_mean_overnight_gap_dn_21d(close, open_),
                     dra_ext_058_mean_overnight_gap_up_21d(close, open_))


def dra_ext_060_close_vs_open_net_21d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Sum of daily open-to-close moves over 21 days (net intraday direction)."""
    oc = _safe_div(close - open_, open_.replace(0, np.nan))
    return _rolling_sum(oc, _TD_MON)


# --- Group G (061-070): Cross-window composite asymmetry metrics ---

def dra_ext_061_gain_loss_ratio_5d(close: pd.Series) -> pd.Series:
    """Gain/loss ratio over trailing 5 days (weekly window)."""
    ret = close.pct_change(1)
    up = _rolling_sum(ret.clip(lower=0.0), _TD_WEEK)
    dn = _rolling_sum((-ret).clip(lower=0.0), _TD_WEEK)
    return _safe_div(up, dn.replace(0, np.nan))


def dra_ext_062_gain_loss_ratio_10d(close: pd.Series) -> pd.Series:
    """Gain/loss ratio over trailing 10 days (two-week window)."""
    ret = close.pct_change(1)
    up = _rolling_sum(ret.clip(lower=0.0), 10)
    dn = _rolling_sum((-ret).clip(lower=0.0), 10)
    return _safe_div(up, dn.replace(0, np.nan))


def dra_ext_063_gain_loss_5d_vs_21d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 5d gain/loss to 21d gain/loss (recent vs short-term asymmetry)."""
    return _safe_div(dra_ext_061_gain_loss_ratio_5d(close),
                     _safe_div(_rolling_sum(close.pct_change(1).clip(lower=0.0), _TD_MON),
                                _rolling_sum((-close.pct_change(1)).clip(lower=0.0), _TD_MON)))


def dra_ext_064_gain_loss_21d_vs_63d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 21d gain/loss to 63d gain/loss (short vs medium asymmetry)."""
    ret = close.pct_change(1)
    gl21 = _safe_div(_rolling_sum(ret.clip(lower=0.0), _TD_MON),
                     _rolling_sum((-ret).clip(lower=0.0), _TD_MON) + _EPS)
    gl63 = _safe_div(_rolling_sum(ret.clip(lower=0.0), _TD_QTR),
                     _rolling_sum((-ret).clip(lower=0.0), _TD_QTR) + _EPS)
    return _safe_div(gl21, gl63.replace(0, np.nan))


def dra_ext_065_vol_asym_5d(close: pd.Series) -> pd.Series:
    """Vol-asymmetry ratio over trailing 5 days."""
    ret = close.pct_change(1)
    dn_vol = (-ret).clip(lower=0.0).rolling(_TD_WEEK, min_periods=max(1, _TD_WEEK // 2)).std()
    up_vol = ret.clip(lower=0.0).rolling(_TD_WEEK, min_periods=max(1, _TD_WEEK // 2)).std()
    return _safe_div(dn_vol, up_vol.replace(0, np.nan))


def dra_ext_066_vol_asym_5d_vs_21d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 5d vol-asymmetry to 21d vol-asymmetry (short vs short-term)."""
    ret = close.pct_change(1)
    va5 = dra_ext_065_vol_asym_5d(close)
    dn21 = (-ret).clip(lower=0.0).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).std()
    up21 = ret.clip(lower=0.0).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).std()
    va21 = _safe_div(dn21, up21.replace(0, np.nan))
    return _safe_div(va5, va21.replace(0, np.nan))


def dra_ext_067_dn_participation_5d(close: pd.Series) -> pd.Series:
    """Downside-participation rate over trailing 5 days."""
    ret = close.pct_change(1)
    dn_sq = _rolling_sum(((-ret).clip(lower=0.0)) ** 2, _TD_WEEK)
    up_sq = _rolling_sum((ret.clip(lower=0.0)) ** 2, _TD_WEEK)
    return _safe_div(dn_sq, dn_sq + up_sq + _EPS)


def dra_ext_068_dn_participation_5d_vs_21d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 5d dn-participation to 21d dn-participation (recent intensification)."""
    ret = close.pct_change(1)
    dn5 = dra_ext_067_dn_participation_5d(close)
    dn_sq21 = _rolling_sum(((-ret).clip(lower=0.0)) ** 2, _TD_MON)
    up_sq21 = _rolling_sum((ret.clip(lower=0.0)) ** 2, _TD_MON)
    dn21 = _safe_div(dn_sq21, dn_sq21 + up_sq21 + _EPS)
    return _safe_div(dn5, dn21.replace(0, np.nan))


def dra_ext_069_asymmetry_regime_bear_score(close: pd.Series) -> pd.Series:
    """Bear asymmetry score: count of bearish asymmetry flags active simultaneously.
    Checks: gl_ratio_21d < 1, vol_asym_21d > 1, speed_asym_21d > 1, dn_part_21d > 0.55.
    Range 0-4 (higher = more indicators confirming bearish path asymmetry)."""
    ret = close.pct_change(1)
    gl21 = _safe_div(_rolling_sum(ret.clip(lower=0.0), _TD_MON),
                     _rolling_sum((-ret).clip(lower=0.0), _TD_MON) + _EPS)
    dn_vol = (-ret).clip(lower=0.0).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).std()
    up_vol = ret.clip(lower=0.0).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).std()
    va21 = _safe_div(dn_vol, up_vol + _EPS)
    dn_sum = _rolling_sum((-ret).clip(lower=0.0), _TD_MON)
    up_sum = _rolling_sum(ret.clip(lower=0.0), _TD_MON)
    dn_cnt = _rolling_sum((ret < 0).astype(float), _TD_MON).replace(0, np.nan)
    up_cnt = _rolling_sum((ret > 0).astype(float), _TD_MON).replace(0, np.nan)
    sa21 = _safe_div(_safe_div(dn_sum, dn_cnt), _safe_div(up_sum, up_cnt))
    dn_sq = _rolling_sum(((-ret).clip(lower=0.0)) ** 2, _TD_MON)
    up_sq = _rolling_sum((ret.clip(lower=0.0)) ** 2, _TD_MON)
    dp21 = _safe_div(dn_sq, dn_sq + up_sq + _EPS)
    f1 = (gl21 < 1.0).astype(float)
    f2 = (va21 > 1.0).astype(float)
    f3 = (sa21 > 1.0).astype(float)
    f4 = (dp21 > 0.55).astype(float)
    return f1.fillna(0) + f2.fillna(0) + f3.fillna(0) + f4.fillna(0)


def dra_ext_070_gain_loss_ratio_vs_hist_min_63d(close: pd.Series) -> pd.Series:
    """21d gain/loss ratio as fraction of its 63-day minimum (1.0 = at the floor)."""
    ret = close.pct_change(1)
    gl21 = _safe_div(_rolling_sum(ret.clip(lower=0.0), _TD_MON),
                     _rolling_sum((-ret).clip(lower=0.0), _TD_MON) + _EPS)
    mn63 = _rolling_min(gl21, _TD_QTR)
    return _safe_div(gl21, mn63.replace(0, np.nan))


# --- Group H (071-075): Path geometry vs recovery geometry ---

def dra_ext_071_dn_path_convexity_21d(close: pd.Series) -> pd.Series:
    """Down-path convexity over 21 days: are down-moves accelerating or decelerating?
    Computed as the OLS slope of rolling 3-day dn-return magnitudes over 21 days."""
    dn3 = (-close.pct_change(1)).clip(lower=0.0).rolling(3, min_periods=1).mean()
    def slope(x):
        if len(x) < 3:
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        return num / den if den != 0 else np.nan
    return dn3.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).apply(slope, raw=True)


def dra_ext_072_up_path_convexity_21d(close: pd.Series) -> pd.Series:
    """Up-path convexity over 21 days: slope of 3-day rolling up-return mean."""
    up3 = close.pct_change(1).clip(lower=0.0).rolling(3, min_periods=1).mean()
    def slope(x):
        if len(x) < 3:
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        return num / den if den != 0 else np.nan
    return up3.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).apply(slope, raw=True)


def dra_ext_073_path_convexity_diff_21d(close: pd.Series) -> pd.Series:
    """Down-path convexity minus up-path convexity over 21 days.
    Positive = dn-moves accelerating relative to up-moves."""
    return dra_ext_071_dn_path_convexity_21d(close) - dra_ext_072_up_path_convexity_21d(close)


def dra_ext_074_dn_return_autocorrelation_21d(close: pd.Series) -> pd.Series:
    """1-lag autocorrelation of daily down-return magnitudes over 21 days.
    Positive = declining streaks are self-reinforcing."""
    dn = (-close.pct_change(1)).clip(lower=0.0)
    return dn.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).apply(
        lambda x: float(pd.Series(x).autocorr(lag=1)) if len(x) >= 3 else np.nan,
        raw=False)


def dra_ext_075_asymmetry_capitulation_composite(close: pd.Series) -> pd.Series:
    """Capitulation asymmetry composite: weighted sum of gain/loss-inverse, vol-asym,
    dn-participation, and speed-asymmetry — all normalized to [0, 1] via clipping.
    Higher = stronger signal that the price path is ratcheting down (capitulation geometry)."""
    ret = close.pct_change(1)
    # gain/loss inverse (dn/up), clipped to [0, 3], mapped to [0,1]
    up = _rolling_sum(ret.clip(lower=0.0), _TD_MON) + _EPS
    dn = _rolling_sum((-ret).clip(lower=0.0), _TD_MON) + _EPS
    gl_inv = (dn / up).clip(upper=3.0) / 3.0
    # vol asymmetry, clipped to [0, 3], mapped to [0,1]
    dv = (-ret).clip(lower=0.0).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).std()
    uv = ret.clip(lower=0.0).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).std()
    va = (_safe_div(dv, uv + _EPS)).clip(upper=3.0) / 3.0
    # dn participation [0, 1] directly
    dn_sq = _rolling_sum(((-ret).clip(lower=0.0)) ** 2, _TD_MON)
    up_sq = _rolling_sum((ret.clip(lower=0.0)) ** 2, _TD_MON)
    dp = _safe_div(dn_sq, dn_sq + up_sq + _EPS)
    # speed asymmetry, clipped to [0, 3], mapped to [0,1]
    dc = _rolling_sum((ret < 0).astype(float), _TD_MON).replace(0, np.nan)
    uc = _rolling_sum((ret > 0).astype(float), _TD_MON).replace(0, np.nan)
    ds = _safe_div(dn, dc)
    us = _safe_div(up, uc)
    sa = (_safe_div(ds, us + _EPS)).clip(upper=3.0) / 3.0
    return (gl_inv.fillna(0.5) + va.fillna(0.5) + dp.fillna(0.5) + sa.fillna(0.5)) / 4.0


# ── Registry ──────────────────────────────────────────────────────────────────

DRAWDOWN_RECOVERY_ASYMMETRY_EXTENDED_REGISTRY_001_075 = {
    "dra_ext_001_avg_dn_run_length_21d": {"inputs": ["close"], "func": dra_ext_001_avg_dn_run_length_21d},
    "dra_ext_002_avg_up_run_length_21d": {"inputs": ["close"], "func": dra_ext_002_avg_up_run_length_21d},
    "dra_ext_003_run_length_ratio_21d": {"inputs": ["close"], "func": dra_ext_003_run_length_ratio_21d},
    "dra_ext_004_avg_dn_run_length_63d": {"inputs": ["close"], "func": dra_ext_004_avg_dn_run_length_63d},
    "dra_ext_005_avg_up_run_length_63d": {"inputs": ["close"], "func": dra_ext_005_avg_up_run_length_63d},
    "dra_ext_006_run_length_ratio_63d": {"inputs": ["close"], "func": dra_ext_006_run_length_ratio_63d},
    "dra_ext_007_dn_run_magnitude_21d": {"inputs": ["close"], "func": dra_ext_007_dn_run_magnitude_21d},
    "dra_ext_008_up_run_magnitude_21d": {"inputs": ["close"], "func": dra_ext_008_up_run_magnitude_21d},
    "dra_ext_009_run_magnitude_ratio_21d": {"inputs": ["close"], "func": dra_ext_009_run_magnitude_ratio_21d},
    "dra_ext_010_num_dn_runs_21d": {"inputs": ["close"], "func": dra_ext_010_num_dn_runs_21d},
    "dra_ext_011_dn_ret_atr_norm_21d": {"inputs": ["close", "high", "low"], "func": dra_ext_011_dn_ret_atr_norm_21d},
    "dra_ext_012_up_ret_atr_norm_21d": {"inputs": ["close", "high", "low"], "func": dra_ext_012_up_ret_atr_norm_21d},
    "dra_ext_013_atr_norm_dn_up_ratio_21d": {"inputs": ["close", "high", "low"], "func": dra_ext_013_atr_norm_dn_up_ratio_21d},
    "dra_ext_014_dn_ret_atr_norm_63d": {"inputs": ["close", "high", "low"], "func": dra_ext_014_dn_ret_atr_norm_63d},
    "dra_ext_015_up_ret_atr_norm_63d": {"inputs": ["close", "high", "low"], "func": dra_ext_015_up_ret_atr_norm_63d},
    "dra_ext_016_atr_norm_dn_up_ratio_63d": {"inputs": ["close", "high", "low"], "func": dra_ext_016_atr_norm_dn_up_ratio_63d},
    "dra_ext_017_dn_range_atr_ratio_21d": {"inputs": ["close", "high", "low"], "func": dra_ext_017_dn_range_atr_ratio_21d},
    "dra_ext_018_up_range_atr_ratio_21d": {"inputs": ["close", "high", "low"], "func": dra_ext_018_up_range_atr_ratio_21d},
    "dra_ext_019_dn_up_range_ratio_21d": {"inputs": ["close", "high", "low"], "func": dra_ext_019_dn_up_range_ratio_21d},
    "dra_ext_020_intraday_dn_pressure_21d": {"inputs": ["close", "high", "low", "open"], "func": dra_ext_020_intraday_dn_pressure_21d},
    "dra_ext_021_gain_loss_ratio_expanding_min": {"inputs": ["close"], "func": dra_ext_021_gain_loss_ratio_expanding_min},
    "dra_ext_022_vol_asym_expanding_max": {"inputs": ["close"], "func": dra_ext_022_vol_asym_expanding_max},
    "dra_ext_023_gain_loss_ratio_current_vs_expanding_min": {"inputs": ["close"], "func": dra_ext_023_gain_loss_ratio_current_vs_expanding_min},
    "dra_ext_024_dn_participation_expanding_max": {"inputs": ["close"], "func": dra_ext_024_dn_participation_expanding_max},
    "dra_ext_025_speed_asym_expanding_max": {"inputs": ["close"], "func": dra_ext_025_speed_asym_expanding_max},
    "dra_ext_026_gain_loss_half_year": {"inputs": ["close"], "func": dra_ext_026_gain_loss_half_year},
    "dra_ext_027_vol_asym_half_year": {"inputs": ["close"], "func": dra_ext_027_vol_asym_half_year},
    "dra_ext_028_dn_participation_half_year": {"inputs": ["close"], "func": dra_ext_028_dn_participation_half_year},
    "dra_ext_029_gain_loss_ratio_5w": {"inputs": ["close"], "func": dra_ext_029_gain_loss_ratio_5w},
    "dra_ext_030_speed_asym_half_year": {"inputs": ["close"], "func": dra_ext_030_speed_asym_half_year},
    "dra_ext_031_top5pct_dn_ret_mean_21d": {"inputs": ["close"], "func": dra_ext_031_top5pct_dn_ret_mean_21d},
    "dra_ext_032_top5pct_up_ret_mean_21d": {"inputs": ["close"], "func": dra_ext_032_top5pct_up_ret_mean_21d},
    "dra_ext_033_tail_dn_up_ratio_21d": {"inputs": ["close"], "func": dra_ext_033_tail_dn_up_ratio_21d},
    "dra_ext_034_large_dn_count_21d": {"inputs": ["close"], "func": dra_ext_034_large_dn_count_21d},
    "dra_ext_035_large_up_count_21d": {"inputs": ["close"], "func": dra_ext_035_large_up_count_21d},
    "dra_ext_036_large_dn_vs_up_count_ratio_21d": {"inputs": ["close"], "func": dra_ext_036_large_dn_vs_up_count_ratio_21d},
    "dra_ext_037_dn_ret_p90_21d": {"inputs": ["close"], "func": dra_ext_037_dn_ret_p90_21d},
    "dra_ext_038_up_ret_p90_21d": {"inputs": ["close"], "func": dra_ext_038_up_ret_p90_21d},
    "dra_ext_039_p90_dn_up_ratio_21d": {"inputs": ["close"], "func": dra_ext_039_p90_dn_up_ratio_21d},
    "dra_ext_040_dn_ret_iqr_21d": {"inputs": ["close"], "func": dra_ext_040_dn_ret_iqr_21d},
    "dra_ext_041_vol_weighted_ratchet_21d": {"inputs": ["close", "volume"], "func": dra_ext_041_vol_weighted_ratchet_21d},
    "dra_ext_042_vol_weighted_gain_loss_21d": {"inputs": ["close", "volume"], "func": dra_ext_042_vol_weighted_gain_loss_21d},
    "dra_ext_043_vol_weighted_gain_loss_63d": {"inputs": ["close", "volume"], "func": dra_ext_043_vol_weighted_gain_loss_63d},
    "dra_ext_044_dn_vol_intensity_21d": {"inputs": ["close", "volume"], "func": dra_ext_044_dn_vol_intensity_21d},
    "dra_ext_045_up_vol_intensity_21d": {"inputs": ["close", "volume"], "func": dra_ext_045_up_vol_intensity_21d},
    "dra_ext_046_vol_intensity_ratio_21d": {"inputs": ["close", "volume"], "func": dra_ext_046_vol_intensity_ratio_21d},
    "dra_ext_047_high_vol_dn_day_ret_21d": {"inputs": ["close", "volume"], "func": dra_ext_047_high_vol_dn_day_ret_21d},
    "dra_ext_048_low_vol_up_day_ret_21d": {"inputs": ["close", "volume"], "func": dra_ext_048_low_vol_up_day_ret_21d},
    "dra_ext_049_high_vol_dn_vs_low_vol_up_ratio_21d": {"inputs": ["close", "volume"], "func": dra_ext_049_high_vol_dn_vs_low_vol_up_ratio_21d},
    "dra_ext_050_dn_vol_concentration_21d": {"inputs": ["close", "volume"], "func": dra_ext_050_dn_vol_concentration_21d},
    "dra_ext_051_avg_oc_dn_move_21d": {"inputs": ["close", "open"], "func": dra_ext_051_avg_oc_dn_move_21d},
    "dra_ext_052_avg_oc_up_move_21d": {"inputs": ["close", "open"], "func": dra_ext_052_avg_oc_up_move_21d},
    "dra_ext_053_oc_asymmetry_ratio_21d": {"inputs": ["close", "open"], "func": dra_ext_053_oc_asymmetry_ratio_21d},
    "dra_ext_054_overnight_dn_count_21d": {"inputs": ["close", "open"], "func": dra_ext_054_overnight_dn_count_21d},
    "dra_ext_055_overnight_up_count_21d": {"inputs": ["close", "open"], "func": dra_ext_055_overnight_up_count_21d},
    "dra_ext_056_overnight_dn_up_ratio_21d": {"inputs": ["close", "open"], "func": dra_ext_056_overnight_dn_up_ratio_21d},
    "dra_ext_057_mean_overnight_gap_dn_21d": {"inputs": ["close", "open"], "func": dra_ext_057_mean_overnight_gap_dn_21d},
    "dra_ext_058_mean_overnight_gap_up_21d": {"inputs": ["close", "open"], "func": dra_ext_058_mean_overnight_gap_up_21d},
    "dra_ext_059_overnight_gap_asymmetry_21d": {"inputs": ["close", "open"], "func": dra_ext_059_overnight_gap_asymmetry_21d},
    "dra_ext_060_close_vs_open_net_21d": {"inputs": ["close", "open"], "func": dra_ext_060_close_vs_open_net_21d},
    "dra_ext_061_gain_loss_ratio_5d": {"inputs": ["close"], "func": dra_ext_061_gain_loss_ratio_5d},
    "dra_ext_062_gain_loss_ratio_10d": {"inputs": ["close"], "func": dra_ext_062_gain_loss_ratio_10d},
    "dra_ext_063_gain_loss_5d_vs_21d_ratio": {"inputs": ["close"], "func": dra_ext_063_gain_loss_5d_vs_21d_ratio},
    "dra_ext_064_gain_loss_21d_vs_63d_ratio": {"inputs": ["close"], "func": dra_ext_064_gain_loss_21d_vs_63d_ratio},
    "dra_ext_065_vol_asym_5d": {"inputs": ["close"], "func": dra_ext_065_vol_asym_5d},
    "dra_ext_066_vol_asym_5d_vs_21d_ratio": {"inputs": ["close"], "func": dra_ext_066_vol_asym_5d_vs_21d_ratio},
    "dra_ext_067_dn_participation_5d": {"inputs": ["close"], "func": dra_ext_067_dn_participation_5d},
    "dra_ext_068_dn_participation_5d_vs_21d_ratio": {"inputs": ["close"], "func": dra_ext_068_dn_participation_5d_vs_21d_ratio},
    "dra_ext_069_asymmetry_regime_bear_score": {"inputs": ["close"], "func": dra_ext_069_asymmetry_regime_bear_score},
    "dra_ext_070_gain_loss_ratio_vs_hist_min_63d": {"inputs": ["close"], "func": dra_ext_070_gain_loss_ratio_vs_hist_min_63d},
    "dra_ext_071_dn_path_convexity_21d": {"inputs": ["close"], "func": dra_ext_071_dn_path_convexity_21d},
    "dra_ext_072_up_path_convexity_21d": {"inputs": ["close"], "func": dra_ext_072_up_path_convexity_21d},
    "dra_ext_073_path_convexity_diff_21d": {"inputs": ["close"], "func": dra_ext_073_path_convexity_diff_21d},
    "dra_ext_074_dn_return_autocorrelation_21d": {"inputs": ["close"], "func": dra_ext_074_dn_return_autocorrelation_21d},
    "dra_ext_075_asymmetry_capitulation_composite": {"inputs": ["close"], "func": dra_ext_075_asymmetry_capitulation_composite},
}
