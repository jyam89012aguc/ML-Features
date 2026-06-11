"""
114_overnight_intraday_split — Extended Features 001-075
Domain: overnight vs intraday return decomposition — deeper variants including
        high-low range decomposition, cross-window session comparisons, EWM-based
        gap metrics, multi-window distress composites, session-weighted indicators,
        tail-risk session metrics, and regime-conditioned session features
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


def _overnight_ret(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Overnight return: prior close -> today open."""
    return open_ / close.shift(1) - 1.0


def _intraday_ret(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Intraday return: today open -> today close."""
    return close / open_ - 1.0


def _total_ret(close: pd.Series) -> pd.Series:
    """Total daily return: prior close -> today close."""
    return close.pct_change(1)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


# ── Extended Feature Functions 001-075 ───────────────────────────────────────

# --- Group A (001-010): Log-return variants ---

def ois_ext_001_overnight_log_ret(close: pd.Series, open: pd.Series) -> pd.Series:
    """Log overnight return: log(open_t / close_{t-1})."""
    return (open / close.shift(1)).apply(np.log)


def ois_ext_002_intraday_log_ret(open: pd.Series, close: pd.Series) -> pd.Series:
    """Log intraday return: log(close_t / open_t)."""
    return (close / open).apply(np.log)


def ois_ext_003_cum_log_overnight_ret_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Cumulative log overnight return over 21 days."""
    log_on = (open / close.shift(1)).apply(np.log)
    return _rolling_sum(log_on, _TD_MON)


def ois_ext_004_cum_log_intraday_ret_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Cumulative log intraday return over 21 days."""
    log_intra = (close / open).apply(np.log)
    return _rolling_sum(log_intra, _TD_MON)


def ois_ext_005_overnight_log_ret_vol_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Volatility of log overnight returns over 21 days."""
    log_on = (open / close.shift(1)).apply(np.log)
    return _rolling_std(log_on, _TD_MON)


def ois_ext_006_intraday_log_ret_vol_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Volatility of log intraday returns over 21 days."""
    log_intra = (close / open).apply(np.log)
    return _rolling_std(log_intra, _TD_MON)


def ois_ext_007_overnight_log_ret_zscore_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Z-score of log overnight return vs 63-day distribution."""
    log_on = (open / close.shift(1)).apply(np.log)
    m = _rolling_mean(log_on, _TD_QTR)
    s = _rolling_std(log_on, _TD_QTR)
    return _safe_div(log_on - m, s)


def ois_ext_008_intraday_log_ret_zscore_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of log intraday return vs 63-day distribution."""
    log_intra = (close / open).apply(np.log)
    m = _rolling_mean(log_intra, _TD_QTR)
    s = _rolling_std(log_intra, _TD_QTR)
    return _safe_div(log_intra - m, s)


def ois_ext_009_overnight_log_ret_pct_rank_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of log overnight return within 252-day distribution."""
    log_on = (open / close.shift(1)).apply(np.log)
    return log_on.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def ois_ext_010_intraday_log_ret_pct_rank_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of log intraday return within 252-day distribution."""
    log_intra = (close / open).apply(np.log)
    return log_intra.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group B (011-020): High-low open-close decomposition ---

def ois_ext_011_open_to_high_ret(open: pd.Series, high: pd.Series) -> pd.Series:
    """Intraday upside: open-to-high return."""
    return (high - open) / open


def ois_ext_012_open_to_low_ret(open: pd.Series, low: pd.Series) -> pd.Series:
    """Intraday downside: open-to-low return (negative)."""
    return (low - open) / open


def ois_ext_013_close_to_high_frac(open: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    """Close location within intraday upside range: (close-open)/(high-open)."""
    num = close - open
    den = high - open
    return _safe_div(num, den.replace(0, np.nan))


def ois_ext_014_open_to_low_frac_21d_mean(open: pd.Series, low: pd.Series) -> pd.Series:
    """Mean open-to-low return over 21 days (average intraday downside depth)."""
    otl = (low - open) / open
    return _rolling_mean(otl, _TD_MON)


def ois_ext_015_overnight_gap_vs_prior_hl_range(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Overnight gap size relative to prior day's high-low range."""
    gap = (open - close.shift(1)).abs()
    hl_prior = (high - low).shift(1)
    return _safe_div(gap, hl_prior.replace(0, np.nan))


def ois_ext_016_intraday_range_vs_hl_range(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Intraday return magnitude vs total H-L range: abs(close-open)/(high-low)."""
    intra = (close - open).abs()
    hl = high - low
    return _safe_div(intra, hl.replace(0, np.nan))


def ois_ext_017_open_position_in_hl_range(open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Where open sits within the day's H-L range: (open-low)/(high-low)."""
    return _safe_div(open - low, (high - low).replace(0, np.nan))


def ois_ext_018_close_position_in_hl_range(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Where close sits within the day's H-L range: (close-low)/(high-low)."""
    return _safe_div(close - low, (high - low).replace(0, np.nan))


def ois_ext_019_open_below_prior_low_flag(open: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: today open is below prior day's low (gap below prior low)."""
    return (open < low.shift(1)).astype(float)


def ois_ext_020_open_below_prior_low_frac_21d(open: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of days where open gapped below prior low (21d)."""
    flag = (open < low.shift(1)).astype(float)
    return _rolling_sum(flag, _TD_MON) / _TD_MON


# --- Group C (021-030): Multi-window cumulative session return percentile ranks ---

def ois_ext_021_cum_overnight_ret_5d_pct_rank_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of 5d cumulative overnight return within 252-day distribution."""
    cum = _rolling_sum(_overnight_ret(close, open), _TD_WEEK)
    return cum.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def ois_ext_022_cum_intraday_ret_5d_pct_rank_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of 5d cumulative intraday return within 252-day distribution."""
    cum = _rolling_sum(_intraday_ret(open, close), _TD_WEEK)
    return cum.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def ois_ext_023_cum_overnight_ret_21d_pct_rank_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of 21d cumulative overnight return within 252-day distribution."""
    cum = _rolling_sum(_overnight_ret(close, open), _TD_MON)
    return cum.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def ois_ext_024_cum_intraday_ret_21d_pct_rank_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of 21d cumulative intraday return within 252-day distribution."""
    cum = _rolling_sum(_intraday_ret(open, close), _TD_MON)
    return cum.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def ois_ext_025_overnight_vol_21d_pct_rank_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of 21d overnight vol within 252-day distribution."""
    vol = _rolling_std(_overnight_ret(close, open), _TD_MON)
    return vol.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def ois_ext_026_intraday_vol_21d_pct_rank_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of 21d intraday vol within 252-day distribution."""
    vol = _rolling_std(_intraday_ret(open, close), _TD_MON)
    return vol.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def ois_ext_027_overnight_distress_21d_pct_rank_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of 21d overnight distress score within 252-day distribution."""
    dist = _rolling_sum(_overnight_ret(close, open).clip(upper=0.0), _TD_MON)
    return dist.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def ois_ext_028_intraday_distress_21d_pct_rank_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of 21d intraday distress score within 252-day distribution."""
    dist = _rolling_sum(_intraday_ret(open, close).clip(upper=0.0), _TD_MON)
    return dist.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def ois_ext_029_overnight_gap_down_frac_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of gap-down days over trailing 252 days."""
    return _rolling_sum((open < close.shift(1)).astype(float), _TD_YEAR) / _TD_YEAR


def ois_ext_030_reversal_frac_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of intraday reversal days over trailing 252 days."""
    on = _overnight_ret(close, open)
    intra = _intraday_ret(open, close)
    rev = ((np.sign(on) != np.sign(intra)) & (on != 0) & (intra != 0)).astype(float)
    return _rolling_sum(rev, _TD_YEAR) / _TD_YEAR


# --- Group D (031-040): EWM-based deeper session features ---

def ois_ext_031_ewm_overnight_distress_span21(close: pd.Series, open: pd.Series) -> pd.Series:
    """EWM (span=21) of clipped-negative overnight return (EWM overnight distress)."""
    return _ewm_mean(_overnight_ret(close, open).clip(upper=0.0), _TD_MON)


def ois_ext_032_ewm_intraday_distress_span21(open: pd.Series, close: pd.Series) -> pd.Series:
    """EWM (span=21) of clipped-negative intraday return."""
    return _ewm_mean(_intraday_ret(open, close).clip(upper=0.0), _TD_MON)


def ois_ext_033_ewm_overnight_vol_span63(close: pd.Series, open: pd.Series) -> pd.Series:
    """EWM (span=63) of abs(overnight return) as vol proxy."""
    return _ewm_mean(_overnight_ret(close, open).abs(), _TD_QTR)


def ois_ext_034_ewm_intraday_vol_span63(open: pd.Series, close: pd.Series) -> pd.Series:
    """EWM (span=63) of abs(intraday return) as vol proxy."""
    return _ewm_mean(_intraday_ret(open, close).abs(), _TD_QTR)


def ois_ext_035_overnight_ret_ewm_span5(close: pd.Series, open: pd.Series) -> pd.Series:
    """EWM (span=5) of overnight return (weekly EWM gap signal)."""
    return _ewm_mean(_overnight_ret(close, open), _TD_WEEK)


def ois_ext_036_intraday_ret_ewm_span5(open: pd.Series, close: pd.Series) -> pd.Series:
    """EWM (span=5) of intraday return."""
    return _ewm_mean(_intraday_ret(open, close), _TD_WEEK)


def ois_ext_037_ewm_overnight_negative_flag_span21(close: pd.Series, open: pd.Series) -> pd.Series:
    """EWM (span=21) of binary overnight-negative flag (smoothed gap-down probability)."""
    flag = (_overnight_ret(close, open) < 0).astype(float)
    return _ewm_mean(flag, _TD_MON)


def ois_ext_038_ewm_intraday_negative_flag_span21(open: pd.Series, close: pd.Series) -> pd.Series:
    """EWM (span=21) of binary intraday-negative flag."""
    flag = (_intraday_ret(open, close) < 0).astype(float)
    return _ewm_mean(flag, _TD_MON)


def ois_ext_039_ewm_reversal_flag_span21(close: pd.Series, open: pd.Series) -> pd.Series:
    """EWM (span=21) of intraday reversal flag (smoothed reversal probability)."""
    on = _overnight_ret(close, open)
    intra = _intraday_ret(open, close)
    rev = ((np.sign(on) != np.sign(intra)) & (on != 0) & (intra != 0)).astype(float)
    return _ewm_mean(rev, _TD_MON)


def ois_ext_040_ewm_gap_persistence_flag_span21(close: pd.Series, open: pd.Series) -> pd.Series:
    """EWM (span=21) of gap persistence flag (gap-down + intraday-down)."""
    on = _overnight_ret(close, open)
    intra = _intraday_ret(open, close)
    pers = ((on < 0) & (intra < 0)).astype(float)
    return _ewm_mean(pers, _TD_MON)


# --- Group E (041-050): Tail/downside risk by session ---

def ois_ext_041_overnight_ret_5th_pctile_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """5th percentile of overnight return over trailing 21 days (tail downside)."""
    on = _overnight_ret(close, open)
    return on.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.05)


def ois_ext_042_intraday_ret_5th_pctile_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """5th percentile of intraday return over trailing 21 days."""
    intra = _intraday_ret(open, close)
    return intra.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.05)


def ois_ext_043_overnight_ret_10th_pctile_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """10th percentile of overnight return over trailing 63 days."""
    on = _overnight_ret(close, open)
    return on.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.10)


def ois_ext_044_intraday_ret_10th_pctile_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """10th percentile of intraday return over trailing 63 days."""
    intra = _intraday_ret(open, close)
    return intra.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.10)


def ois_ext_045_overnight_cvar_5pct_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """CVaR (conditional on bottom 5%) of overnight return over 21 days."""
    on = _overnight_ret(close, open)
    q05 = on.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.05)
    tail = on.where(on <= q05, np.nan)
    return _rolling_mean(tail, _TD_MON)


def ois_ext_046_intraday_cvar_5pct_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """CVaR (conditional on bottom 5%) of intraday return over 21 days."""
    intra = _intraday_ret(open, close)
    q05 = intra.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.05)
    tail = intra.where(intra <= q05, np.nan)
    return _rolling_mean(tail, _TD_MON)


def ois_ext_047_overnight_semi_deviation_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Downside semi-deviation of overnight returns over 21 days."""
    on = _overnight_ret(close, open)
    neg_on = on.where(on < 0, 0.0)
    sq = neg_on ** 2
    return _rolling_mean(sq, _TD_MON).apply(np.sqrt)


def ois_ext_048_intraday_semi_deviation_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Downside semi-deviation of intraday returns over 21 days."""
    intra = _intraday_ret(open, close)
    neg_intra = intra.where(intra < 0, 0.0)
    sq = neg_intra ** 2
    return _rolling_mean(sq, _TD_MON).apply(np.sqrt)


def ois_ext_049_overnight_gain_to_pain_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Overnight gain-to-pain ratio: sum(pos) / abs(sum(neg)) over 21d."""
    on = _overnight_ret(close, open)
    gain = _rolling_sum(on.clip(lower=0.0), _TD_MON)
    pain = _rolling_sum(on.clip(upper=0.0).abs(), _TD_MON)
    return _safe_div(gain, pain.replace(0, np.nan))


def ois_ext_050_intraday_gain_to_pain_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Intraday gain-to-pain ratio: sum(pos) / abs(sum(neg)) over 21d."""
    intra = _intraday_ret(open, close)
    gain = _rolling_sum(intra.clip(lower=0.0), _TD_MON)
    pain = _rolling_sum(intra.clip(upper=0.0).abs(), _TD_MON)
    return _safe_div(gain, pain.replace(0, np.nan))


# --- Group F (051-060): Volume-conditioned session depth ---

def ois_ext_051_largest_overnight_gap_vol_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume on the worst overnight gap-down day over 21 days."""
    on = _overnight_ret(close, open)
    worst_idx = on.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda x: np.nanargmin(x), raw=True
    )
    vol_vals = volume.values
    result = pd.Series(np.nan, index=on.index)
    for i in range(len(on)):
        w_start = max(0, i - _TD_MON + 1)
        window_on = on.iloc[w_start:i + 1]
        if len(window_on.dropna()) >= max(1, _TD_MON // 2):
            idx_in_window = int(window_on.values[~np.isnan(window_on.values)].argmin())
            abs_idx = w_start + idx_in_window
            result.iloc[i] = vol_vals[abs_idx]
    return result


def ois_ext_052_overnight_down_day_avg_volume_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume on overnight-down days over 21 days."""
    on = _overnight_ret(close, open)
    neg_vol = volume.where(on < 0, np.nan)
    return _rolling_mean(neg_vol, _TD_MON)


def ois_ext_053_intraday_down_day_avg_volume_21d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume on intraday-down days over 21 days."""
    intra = _intraday_ret(open, close)
    neg_vol = volume.where(intra < 0, np.nan)
    return _rolling_mean(neg_vol, _TD_MON)


def ois_ext_054_overnight_down_vol_vs_up_vol_ratio_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of average volume on gap-down days to average on gap-up days (21d)."""
    on = _overnight_ret(close, open)
    down_vol = _rolling_sum(volume.where(on < 0, 0.0), _TD_MON)
    down_cnt = _rolling_sum((on < 0).astype(float), _TD_MON)
    up_vol = _rolling_sum(volume.where(on > 0, 0.0), _TD_MON)
    up_cnt = _rolling_sum((on > 0).astype(float), _TD_MON)
    avg_down = _safe_div(down_vol, down_cnt.replace(0, np.nan))
    avg_up = _safe_div(up_vol, up_cnt.replace(0, np.nan))
    return _safe_div(avg_down, avg_up.replace(0, np.nan))


def ois_ext_055_intraday_down_vol_vs_up_vol_ratio_21d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of average volume on intraday-down days to average on up-days (21d)."""
    intra = _intraday_ret(open, close)
    down_vol = _rolling_sum(volume.where(intra < 0, 0.0), _TD_MON)
    down_cnt = _rolling_sum((intra < 0).astype(float), _TD_MON)
    up_vol = _rolling_sum(volume.where(intra > 0, 0.0), _TD_MON)
    up_cnt = _rolling_sum((intra > 0).astype(float), _TD_MON)
    avg_down = _safe_div(down_vol, down_cnt.replace(0, np.nan))
    avg_up = _safe_div(up_vol, up_cnt.replace(0, np.nan))
    return _safe_div(avg_down, avg_up.replace(0, np.nan))


def ois_ext_056_both_down_vol_share_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Share of volume on days where both sessions are negative (21d)."""
    on = _overnight_ret(close, open)
    intra = _intraday_ret(open, close)
    both_vol = _rolling_sum(volume.where((on < 0) & (intra < 0), 0.0), _TD_MON)
    total_vol = _rolling_sum(volume, _TD_MON)
    return _safe_div(both_vol, total_vol.replace(0, np.nan))


def ois_ext_057_overnight_distress_volume_intensity_63d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of volume * abs(overnight_ret) on overnight-down days over 63 days."""
    on = _overnight_ret(close, open)
    intensity = (on < 0).astype(float) * volume * on.abs()
    return _rolling_sum(intensity, _TD_QTR)


def ois_ext_058_intraday_distress_volume_intensity_63d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of volume * abs(intraday_ret) on intraday-down days over 63 days."""
    intra = _intraday_ret(open, close)
    intensity = (intra < 0).astype(float) * volume * intra.abs()
    return _rolling_sum(intensity, _TD_QTR)


def ois_ext_059_vol_weighted_gap_down_depth_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted mean of negative overnight returns over 21 days."""
    on = _overnight_ret(close, open)
    neg_on = on.clip(upper=0.0)
    wt_neg = _rolling_sum(neg_on * volume, _TD_MON)
    total_vol = _rolling_sum(volume, _TD_MON)
    return _safe_div(wt_neg, total_vol.replace(0, np.nan))


def ois_ext_060_vol_weighted_intraday_down_depth_21d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted mean of negative intraday returns over 21 days."""
    intra = _intraday_ret(open, close)
    neg_intra = intra.clip(upper=0.0)
    wt_neg = _rolling_sum(neg_intra * volume, _TD_MON)
    total_vol = _rolling_sum(volume, _TD_MON)
    return _safe_div(wt_neg, total_vol.replace(0, np.nan))


# --- Group G (061-075): Multi-window and regime cross-checks ---

def ois_ext_061_overnight_distress_21d_vs_252d_ratio(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day overnight distress score normalized by 252-day avg (stress spike ratio)."""
    on_clipped = _overnight_ret(close, open).clip(upper=0.0)
    dist21 = _rolling_sum(on_clipped, _TD_MON)
    avg252 = _rolling_mean(dist21, _TD_YEAR)
    return _safe_div(dist21, avg252.clip(upper=-_EPS))


def ois_ext_062_intraday_distress_21d_vs_252d_ratio(open: pd.Series, close: pd.Series) -> pd.Series:
    """21-day intraday distress score normalized by 252-day avg."""
    intra_clipped = _intraday_ret(open, close).clip(upper=0.0)
    dist21 = _rolling_sum(intra_clipped, _TD_MON)
    avg252 = _rolling_mean(dist21, _TD_YEAR)
    return _safe_div(dist21, avg252.clip(upper=-_EPS))


def ois_ext_063_overnight_vol_21d_vs_252d_normalized(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day overnight vol normalized by 252-day overnight vol."""
    on = _overnight_ret(close, open)
    vol21 = _rolling_std(on, _TD_MON)
    vol252 = _rolling_std(on, _TD_YEAR)
    return _safe_div(vol21, vol252.replace(0, np.nan))


def ois_ext_064_intraday_vol_21d_vs_252d_normalized(open: pd.Series, close: pd.Series) -> pd.Series:
    """21-day intraday vol normalized by 252-day intraday vol."""
    intra = _intraday_ret(open, close)
    vol21 = _rolling_std(intra, _TD_MON)
    vol252 = _rolling_std(intra, _TD_YEAR)
    return _safe_div(vol21, vol252.replace(0, np.nan))


def ois_ext_065_overnight_kurt_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rolling 63-day kurtosis of overnight returns."""
    on = _overnight_ret(close, open)
    return on.rolling(_TD_QTR, min_periods=max(4, _TD_QTR // 2)).kurt()


def ois_ext_066_intraday_kurt_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63-day kurtosis of intraday returns."""
    intra = _intraday_ret(open, close)
    return intra.rolling(_TD_QTR, min_periods=max(4, _TD_QTR // 2)).kurt()


def ois_ext_067_overnight_downside_sharpe_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Overnight downside Sharpe: mean(on) / semi_deviation(on) over 21 days."""
    on = _overnight_ret(close, open)
    mean = _rolling_mean(on, _TD_MON)
    neg = on.where(on < 0, 0.0)
    semi = _rolling_mean(neg ** 2, _TD_MON).apply(np.sqrt)
    return _safe_div(mean, semi.replace(0, np.nan))


def ois_ext_068_intraday_downside_sharpe_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Intraday downside Sharpe: mean(intra) / semi_deviation(intra) over 21 days."""
    intra = _intraday_ret(open, close)
    mean = _rolling_mean(intra, _TD_MON)
    neg = intra.where(intra < 0, 0.0)
    semi = _rolling_mean(neg ** 2, _TD_MON).apply(np.sqrt)
    return _safe_div(mean, semi.replace(0, np.nan))


def ois_ext_069_overnight_ret_slope_5d(close: pd.Series, open: pd.Series) -> pd.Series:
    """OLS slope of overnight return over 5 days (ultra-short trend in gaps)."""
    return _linslope(_overnight_ret(close, open), _TD_WEEK)


def ois_ext_070_intraday_ret_slope_5d(open: pd.Series, close: pd.Series) -> pd.Series:
    """OLS slope of intraday return over 5 days."""
    return _linslope(_intraday_ret(open, close), _TD_WEEK)


def ois_ext_071_overnight_gap_down_consec_max_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Maximum consecutive gap-down streak within trailing 252 days."""
    neg = (_overnight_ret(close, open) < 0)

    def _max_run(arr):
        mx, cur = 0, 0
        for v in arr:
            if v:
                cur += 1
                if cur > mx:
                    mx = cur
            else:
                cur = 0
        return float(mx)

    return neg.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_max_run, raw=True)


def ois_ext_072_intraday_down_consec_max_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Maximum consecutive intraday-down streak within trailing 252 days."""
    neg = (_intraday_ret(open, close) < 0)

    def _max_run(arr):
        mx, cur = 0, 0
        for v in arr:
            if v:
                cur += 1
                if cur > mx:
                    mx = cur
            else:
                cur = 0
        return float(mx)

    return neg.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_max_run, raw=True)


def ois_ext_073_session_distress_composite_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Combined session distress: sum of overnight + intraday negative cum returns (63d)."""
    on_dist = _rolling_sum(_overnight_ret(close, open).clip(upper=0.0), _TD_QTR)
    intra_dist = _rolling_sum(_intraday_ret(open, close).clip(upper=0.0), _TD_QTR)
    return on_dist + intra_dist


def ois_ext_074_session_distress_composite_pct_rank_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of 21d session distress composite within 252-day distribution."""
    on_dist = _rolling_sum(_overnight_ret(close, open).clip(upper=0.0), _TD_MON)
    intra_dist = _rolling_sum(_intraday_ret(open, close).clip(upper=0.0), _TD_MON)
    composite = on_dist + intra_dist
    return composite.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def ois_ext_075_overnight_intraday_distress_balance_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Balance: overnight_distress / (overnight_distress + intraday_distress) over 21d."""
    on_dist = _rolling_sum(_overnight_ret(close, open).clip(upper=0.0).abs(), _TD_MON)
    intra_dist = _rolling_sum(_intraday_ret(open, close).clip(upper=0.0).abs(), _TD_MON)
    total = on_dist + intra_dist
    return _safe_div(on_dist, total.replace(0, np.nan))


# ── Registry ──────────────────────────────────────────────────────────────────

OVERNIGHT_INTRADAY_SPLIT_EXTENDED_REGISTRY_001_075 = {
    "ois_ext_001_overnight_log_ret": {"inputs": ["close", "open"], "func": ois_ext_001_overnight_log_ret},
    "ois_ext_002_intraday_log_ret": {"inputs": ["open", "close"], "func": ois_ext_002_intraday_log_ret},
    "ois_ext_003_cum_log_overnight_ret_21d": {"inputs": ["close", "open"], "func": ois_ext_003_cum_log_overnight_ret_21d},
    "ois_ext_004_cum_log_intraday_ret_21d": {"inputs": ["open", "close"], "func": ois_ext_004_cum_log_intraday_ret_21d},
    "ois_ext_005_overnight_log_ret_vol_21d": {"inputs": ["close", "open"], "func": ois_ext_005_overnight_log_ret_vol_21d},
    "ois_ext_006_intraday_log_ret_vol_21d": {"inputs": ["open", "close"], "func": ois_ext_006_intraday_log_ret_vol_21d},
    "ois_ext_007_overnight_log_ret_zscore_63d": {"inputs": ["close", "open"], "func": ois_ext_007_overnight_log_ret_zscore_63d},
    "ois_ext_008_intraday_log_ret_zscore_63d": {"inputs": ["open", "close"], "func": ois_ext_008_intraday_log_ret_zscore_63d},
    "ois_ext_009_overnight_log_ret_pct_rank_252d": {"inputs": ["close", "open"], "func": ois_ext_009_overnight_log_ret_pct_rank_252d},
    "ois_ext_010_intraday_log_ret_pct_rank_252d": {"inputs": ["open", "close"], "func": ois_ext_010_intraday_log_ret_pct_rank_252d},
    "ois_ext_011_open_to_high_ret": {"inputs": ["open", "high"], "func": ois_ext_011_open_to_high_ret},
    "ois_ext_012_open_to_low_ret": {"inputs": ["open", "low"], "func": ois_ext_012_open_to_low_ret},
    "ois_ext_013_close_to_high_frac": {"inputs": ["open", "high", "close"], "func": ois_ext_013_close_to_high_frac},
    "ois_ext_014_open_to_low_frac_21d_mean": {"inputs": ["open", "low"], "func": ois_ext_014_open_to_low_frac_21d_mean},
    "ois_ext_015_overnight_gap_vs_prior_hl_range": {"inputs": ["close", "open", "high", "low"], "func": ois_ext_015_overnight_gap_vs_prior_hl_range},
    "ois_ext_016_intraday_range_vs_hl_range": {"inputs": ["open", "close", "high", "low"], "func": ois_ext_016_intraday_range_vs_hl_range},
    "ois_ext_017_open_position_in_hl_range": {"inputs": ["open", "high", "low"], "func": ois_ext_017_open_position_in_hl_range},
    "ois_ext_018_close_position_in_hl_range": {"inputs": ["close", "high", "low"], "func": ois_ext_018_close_position_in_hl_range},
    "ois_ext_019_open_below_prior_low_flag": {"inputs": ["open", "low"], "func": ois_ext_019_open_below_prior_low_flag},
    "ois_ext_020_open_below_prior_low_frac_21d": {"inputs": ["open", "low"], "func": ois_ext_020_open_below_prior_low_frac_21d},
    "ois_ext_021_cum_overnight_ret_5d_pct_rank_252d": {"inputs": ["close", "open"], "func": ois_ext_021_cum_overnight_ret_5d_pct_rank_252d},
    "ois_ext_022_cum_intraday_ret_5d_pct_rank_252d": {"inputs": ["open", "close"], "func": ois_ext_022_cum_intraday_ret_5d_pct_rank_252d},
    "ois_ext_023_cum_overnight_ret_21d_pct_rank_252d": {"inputs": ["close", "open"], "func": ois_ext_023_cum_overnight_ret_21d_pct_rank_252d},
    "ois_ext_024_cum_intraday_ret_21d_pct_rank_252d": {"inputs": ["open", "close"], "func": ois_ext_024_cum_intraday_ret_21d_pct_rank_252d},
    "ois_ext_025_overnight_vol_21d_pct_rank_252d": {"inputs": ["close", "open"], "func": ois_ext_025_overnight_vol_21d_pct_rank_252d},
    "ois_ext_026_intraday_vol_21d_pct_rank_252d": {"inputs": ["open", "close"], "func": ois_ext_026_intraday_vol_21d_pct_rank_252d},
    "ois_ext_027_overnight_distress_21d_pct_rank_252d": {"inputs": ["close", "open"], "func": ois_ext_027_overnight_distress_21d_pct_rank_252d},
    "ois_ext_028_intraday_distress_21d_pct_rank_252d": {"inputs": ["open", "close"], "func": ois_ext_028_intraday_distress_21d_pct_rank_252d},
    "ois_ext_029_overnight_gap_down_frac_252d": {"inputs": ["close", "open"], "func": ois_ext_029_overnight_gap_down_frac_252d},
    "ois_ext_030_reversal_frac_252d": {"inputs": ["close", "open"], "func": ois_ext_030_reversal_frac_252d},
    "ois_ext_031_ewm_overnight_distress_span21": {"inputs": ["close", "open"], "func": ois_ext_031_ewm_overnight_distress_span21},
    "ois_ext_032_ewm_intraday_distress_span21": {"inputs": ["open", "close"], "func": ois_ext_032_ewm_intraday_distress_span21},
    "ois_ext_033_ewm_overnight_vol_span63": {"inputs": ["close", "open"], "func": ois_ext_033_ewm_overnight_vol_span63},
    "ois_ext_034_ewm_intraday_vol_span63": {"inputs": ["open", "close"], "func": ois_ext_034_ewm_intraday_vol_span63},
    "ois_ext_035_overnight_ret_ewm_span5": {"inputs": ["close", "open"], "func": ois_ext_035_overnight_ret_ewm_span5},
    "ois_ext_036_intraday_ret_ewm_span5": {"inputs": ["open", "close"], "func": ois_ext_036_intraday_ret_ewm_span5},
    "ois_ext_037_ewm_overnight_negative_flag_span21": {"inputs": ["close", "open"], "func": ois_ext_037_ewm_overnight_negative_flag_span21},
    "ois_ext_038_ewm_intraday_negative_flag_span21": {"inputs": ["open", "close"], "func": ois_ext_038_ewm_intraday_negative_flag_span21},
    "ois_ext_039_ewm_reversal_flag_span21": {"inputs": ["close", "open"], "func": ois_ext_039_ewm_reversal_flag_span21},
    "ois_ext_040_ewm_gap_persistence_flag_span21": {"inputs": ["close", "open"], "func": ois_ext_040_ewm_gap_persistence_flag_span21},
    "ois_ext_041_overnight_ret_5th_pctile_21d": {"inputs": ["close", "open"], "func": ois_ext_041_overnight_ret_5th_pctile_21d},
    "ois_ext_042_intraday_ret_5th_pctile_21d": {"inputs": ["open", "close"], "func": ois_ext_042_intraday_ret_5th_pctile_21d},
    "ois_ext_043_overnight_ret_10th_pctile_63d": {"inputs": ["close", "open"], "func": ois_ext_043_overnight_ret_10th_pctile_63d},
    "ois_ext_044_intraday_ret_10th_pctile_63d": {"inputs": ["open", "close"], "func": ois_ext_044_intraday_ret_10th_pctile_63d},
    "ois_ext_045_overnight_cvar_5pct_21d": {"inputs": ["close", "open"], "func": ois_ext_045_overnight_cvar_5pct_21d},
    "ois_ext_046_intraday_cvar_5pct_21d": {"inputs": ["open", "close"], "func": ois_ext_046_intraday_cvar_5pct_21d},
    "ois_ext_047_overnight_semi_deviation_21d": {"inputs": ["close", "open"], "func": ois_ext_047_overnight_semi_deviation_21d},
    "ois_ext_048_intraday_semi_deviation_21d": {"inputs": ["open", "close"], "func": ois_ext_048_intraday_semi_deviation_21d},
    "ois_ext_049_overnight_gain_to_pain_21d": {"inputs": ["close", "open"], "func": ois_ext_049_overnight_gain_to_pain_21d},
    "ois_ext_050_intraday_gain_to_pain_21d": {"inputs": ["open", "close"], "func": ois_ext_050_intraday_gain_to_pain_21d},
    "ois_ext_051_largest_overnight_gap_vol_21d": {"inputs": ["close", "open", "volume"], "func": ois_ext_051_largest_overnight_gap_vol_21d},
    "ois_ext_052_overnight_down_day_avg_volume_21d": {"inputs": ["close", "open", "volume"], "func": ois_ext_052_overnight_down_day_avg_volume_21d},
    "ois_ext_053_intraday_down_day_avg_volume_21d": {"inputs": ["open", "close", "volume"], "func": ois_ext_053_intraday_down_day_avg_volume_21d},
    "ois_ext_054_overnight_down_vol_vs_up_vol_ratio_21d": {"inputs": ["close", "open", "volume"], "func": ois_ext_054_overnight_down_vol_vs_up_vol_ratio_21d},
    "ois_ext_055_intraday_down_vol_vs_up_vol_ratio_21d": {"inputs": ["open", "close", "volume"], "func": ois_ext_055_intraday_down_vol_vs_up_vol_ratio_21d},
    "ois_ext_056_both_down_vol_share_21d": {"inputs": ["close", "open", "volume"], "func": ois_ext_056_both_down_vol_share_21d},
    "ois_ext_057_overnight_distress_volume_intensity_63d": {"inputs": ["close", "open", "volume"], "func": ois_ext_057_overnight_distress_volume_intensity_63d},
    "ois_ext_058_intraday_distress_volume_intensity_63d": {"inputs": ["open", "close", "volume"], "func": ois_ext_058_intraday_distress_volume_intensity_63d},
    "ois_ext_059_vol_weighted_gap_down_depth_21d": {"inputs": ["close", "open", "volume"], "func": ois_ext_059_vol_weighted_gap_down_depth_21d},
    "ois_ext_060_vol_weighted_intraday_down_depth_21d": {"inputs": ["open", "close", "volume"], "func": ois_ext_060_vol_weighted_intraday_down_depth_21d},
    "ois_ext_061_overnight_distress_21d_vs_252d_ratio": {"inputs": ["close", "open"], "func": ois_ext_061_overnight_distress_21d_vs_252d_ratio},
    "ois_ext_062_intraday_distress_21d_vs_252d_ratio": {"inputs": ["open", "close"], "func": ois_ext_062_intraday_distress_21d_vs_252d_ratio},
    "ois_ext_063_overnight_vol_21d_vs_252d_normalized": {"inputs": ["close", "open"], "func": ois_ext_063_overnight_vol_21d_vs_252d_normalized},
    "ois_ext_064_intraday_vol_21d_vs_252d_normalized": {"inputs": ["open", "close"], "func": ois_ext_064_intraday_vol_21d_vs_252d_normalized},
    "ois_ext_065_overnight_kurt_63d": {"inputs": ["close", "open"], "func": ois_ext_065_overnight_kurt_63d},
    "ois_ext_066_intraday_kurt_63d": {"inputs": ["open", "close"], "func": ois_ext_066_intraday_kurt_63d},
    "ois_ext_067_overnight_downside_sharpe_21d": {"inputs": ["close", "open"], "func": ois_ext_067_overnight_downside_sharpe_21d},
    "ois_ext_068_intraday_downside_sharpe_21d": {"inputs": ["open", "close"], "func": ois_ext_068_intraday_downside_sharpe_21d},
    "ois_ext_069_overnight_ret_slope_5d": {"inputs": ["close", "open"], "func": ois_ext_069_overnight_ret_slope_5d},
    "ois_ext_070_intraday_ret_slope_5d": {"inputs": ["open", "close"], "func": ois_ext_070_intraday_ret_slope_5d},
    "ois_ext_071_overnight_gap_down_consec_max_252d": {"inputs": ["close", "open"], "func": ois_ext_071_overnight_gap_down_consec_max_252d},
    "ois_ext_072_intraday_down_consec_max_252d": {"inputs": ["open", "close"], "func": ois_ext_072_intraday_down_consec_max_252d},
    "ois_ext_073_session_distress_composite_63d": {"inputs": ["close", "open"], "func": ois_ext_073_session_distress_composite_63d},
    "ois_ext_074_session_distress_composite_pct_rank_252d": {"inputs": ["close", "open"], "func": ois_ext_074_session_distress_composite_pct_rank_252d},
    "ois_ext_075_overnight_intraday_distress_balance_21d": {"inputs": ["close", "open"], "func": ois_ext_075_overnight_intraday_distress_balance_21d},
}
