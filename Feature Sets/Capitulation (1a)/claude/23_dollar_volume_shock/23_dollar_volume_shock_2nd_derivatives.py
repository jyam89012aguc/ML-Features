"""
23_dollar_volume_shock — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change of base dollar-volume-shock features — velocity of DV shock
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
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _dv(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar volume: close * volume."""
    return close * volume


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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def dvs_drv2_001_dv_ratio_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day DV ratio (velocity of short-term DV surge)."""
    dv = _dv(close, volume)
    ratio = _safe_div(dv, _rolling_mean(dv, _TD_MON))
    return ratio.diff(_TD_WEEK)


def dvs_drv2_002_dv_ratio_63d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the 63-day DV ratio (velocity of quarterly DV level)."""
    dv = _dv(close, volume)
    ratio = _safe_div(dv, _rolling_mean(dv, _TD_QTR))
    return ratio.diff(_TD_WEEK)


def dvs_drv2_003_dv_ratio_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of the 63-day DV ratio (monthly change in quarterly DV ratio)."""
    dv = _dv(close, volume)
    ratio = _safe_div(dv, _rolling_mean(dv, _TD_QTR))
    return ratio.diff(_TD_MON)


def dvs_drv2_004_dv_zscore_63d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the 63-day DV z-score (acceleration of DV extremity)."""
    dv = _dv(close, volume)
    m = _rolling_mean(dv, _TD_QTR)
    s = _rolling_std(dv, _TD_QTR)
    z = _safe_div(dv - m, s)
    return z.diff(_TD_WEEK)


def dvs_drv2_005_dv_zscore_252d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of the 252-day DV z-score."""
    dv = _dv(close, volume)
    m = _rolling_mean(dv, _TD_YEAR)
    s = _rolling_std(dv, _TD_YEAR)
    z = _safe_div(dv - m, s)
    return z.diff(_TD_MON)


def dvs_drv2_006_dv_log_ratio_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of log-DV-ratio-21d."""
    dv = _dv(close, volume)
    log_ratio = _log_safe(dv) - _log_safe(_rolling_mean(dv, _TD_MON))
    return log_ratio.diff(_TD_WEEK)


def dvs_drv2_007_dv_spike_count_2x_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day 2x-DV spike count."""
    dv = _dv(close, volume)
    baseline = _rolling_mean(dv, _TD_QTR)
    spike = (dv > 2.0 * baseline).astype(float)
    count21 = _rolling_sum(spike, _TD_MON)
    return count21.diff(_TD_WEEK)


def dvs_drv2_008_dv_spike_count_2x_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day 2x-DV spike count."""
    dv = _dv(close, volume)
    baseline = _rolling_mean(dv, _TD_QTR)
    spike = (dv > 2.0 * baseline).astype(float)
    count63 = _rolling_sum(spike, _TD_QTR)
    return count63.diff(_TD_MON)


def dvs_drv2_009_dv_down_vs_up_ratio_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day DV down/up ratio."""
    dv = _dv(close, volume)
    ret = close.pct_change(1)
    dv_dn = dv.where(ret < 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    dv_up = dv.where(ret > 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    ratio = _safe_div(dv_dn, dv_up)
    return ratio.diff(_TD_WEEK)


def dvs_drv2_010_dv_down_vs_up_ratio_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day DV down/up ratio."""
    dv = _dv(close, volume)
    ret = close.pct_change(1)
    dv_dn = dv.where(ret < 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    dv_up = dv.where(ret > 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    ratio = _safe_div(dv_dn, dv_up)
    return ratio.diff(_TD_MON)


def dvs_drv2_011_dv_pct_rank_252d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 252-day DV percentile rank."""
    dv = _dv(close, volume)
    rank = dv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return rank.diff(_TD_WEEK)


def dvs_drv2_012_dv_sum_21d_ratio_252d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of ratio (21d DV sum / 252d DV sum)."""
    dv = _dv(close, volume)
    ratio = _safe_div(_rolling_sum(dv, _TD_MON), _rolling_sum(dv, _TD_YEAR))
    return ratio.diff(_TD_WEEK)


def dvs_drv2_013_dv_ewm21_vs_ewm63_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of EWM21/EWM63 ratio of DV."""
    dv = _dv(close, volume)
    ratio = _safe_div(_ewm_mean(dv, _TD_MON), _ewm_mean(dv, _TD_QTR))
    return ratio.diff(_TD_WEEK)


def dvs_drv2_014_dv_cv_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day DV coefficient of variation."""
    dv = _dv(close, volume)
    cv = _safe_div(_rolling_std(dv, _TD_MON), _rolling_mean(dv, _TD_MON))
    return cv.diff(_TD_WEEK)


def dvs_drv2_015_dv_ratio_21d_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope over 63 days of the 21-day DV ratio."""
    dv = _dv(close, volume)
    ratio = _safe_div(dv, _rolling_mean(dv, _TD_MON))
    return _linslope(ratio, _TD_QTR)


def dvs_drv2_016_dv_zscore_63d_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 63-day DV z-score."""
    dv = _dv(close, volume)
    m = _rolling_mean(dv, _TD_QTR)
    s = _rolling_std(dv, _TD_QTR)
    z = _safe_div(dv - m, s)
    return _linslope(z, _TD_MON)


def dvs_drv2_017_dv_spike_on_down_day_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day DV-spike-on-down-day count."""
    dv = _dv(close, volume)
    baseline = _rolling_mean(dv, _TD_QTR)
    ret = close.pct_change(1)
    spike_dn = ((dv > 2.0 * baseline) & (ret < 0)).astype(float)
    count63 = _rolling_sum(spike_dn, _TD_QTR)
    return count63.diff(_TD_MON)


def dvs_drv2_018_dv_at_new_low_fraction_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of fraction of 63d DV at new-63d-low days."""
    dv = _dv(close, volume)
    roll_min = close.shift(1).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    new_low = close < roll_min
    dv_nl = dv.where(new_low, 0.0)
    total = _rolling_sum(dv, _TD_QTR)
    frac = _safe_div(_rolling_sum(dv_nl, _TD_QTR), total)
    return frac.diff(_TD_MON)


def dvs_drv2_019_dv_distress_index_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of DV distress index (dv ratio * down-frac)."""
    dv = _dv(close, volume)
    ratio = _safe_div(dv, _rolling_mean(dv, _TD_QTR))
    ret = close.pct_change(1)
    dn_frac = (ret < 0).astype(float).rolling(_TD_MON, min_periods=1).sum() / _TD_MON
    distress = ratio * dn_frac
    return distress.diff(_TD_WEEK)


def dvs_drv2_020_dv_log_ratio_252d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of log-DV-ratio-252d."""
    dv = _dv(close, volume)
    log_ratio = _log_safe(dv) - _log_safe(_rolling_mean(dv, _TD_YEAR))
    return log_ratio.diff(_TD_MON)


def dvs_drv2_021_dv_max_21d_vs_mean_252d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of (21d max DV / 252d mean DV)."""
    dv = _dv(close, volume)
    ratio = _safe_div(dv.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).max(),
                      _rolling_mean(dv, _TD_YEAR))
    return ratio.diff(_TD_WEEK)


def dvs_drv2_022_dv_persistence_score_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day DV persistence score."""
    dv = _dv(close, volume)
    above = (dv > dv.shift(1)).astype(float)
    persistence = _rolling_sum(above, _TD_MON) / _TD_MON
    return persistence.diff(_TD_WEEK)


def dvs_drv2_023_dv_hhi_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day DV concentration HHI."""
    dv = _dv(close, volume)
    sum21 = _rolling_sum(dv, _TD_MON)
    share = _safe_div(dv, sum21)
    hhi = _rolling_sum(share ** 2, _TD_MON)
    return hhi.diff(_TD_WEEK)


def dvs_drv2_024_dv_spike_recency_decay_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of EWM-decayed DV spike signal."""
    dv = _dv(close, volume)
    baseline = _rolling_mean(dv, _TD_QTR)
    spike = (dv > 2.0 * baseline).astype(float)
    decay = spike.ewm(halflife=5, min_periods=1).mean()
    return decay.diff(_TD_WEEK)


def dvs_drv2_025_dv_capitulation_composite_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the capitulation composite score."""
    dv = _dv(close, volume)
    m = _rolling_mean(dv, _TD_QTR)
    s = _rolling_std(dv, _TD_QTR)
    z63 = _safe_div(dv - m, s)
    ret = close.pct_change(1)
    dn_frac = (ret < 0).astype(float).rolling(_TD_MON, min_periods=1).sum() / _TD_MON
    rank = dv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True).fillna(0.0)
    composite = z63 * dn_frac * (1.0 + rank)
    return composite.diff(_TD_WEEK)


# ── 2nd-Derivative Feature Functions (026-075) ────────────────────────────────

def dvs_drv2_026_dv_ratio_126d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the 126-day DV ratio (velocity of half-year DV level)."""
    dv = _dv(close, volume)
    ratio = _safe_div(dv, _rolling_mean(dv, 126))
    return ratio.diff(_TD_WEEK)


def dvs_drv2_027_dv_ratio_252d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of the 252-day DV ratio (monthly change in annual DV ratio)."""
    dv = _dv(close, volume)
    ratio = _safe_div(dv, _rolling_mean(dv, _TD_YEAR))
    return ratio.diff(_TD_MON)


def dvs_drv2_028_dv_zscore_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day DV z-score (velocity of short-term DV extremity)."""
    dv = _dv(close, volume)
    m = _rolling_mean(dv, _TD_MON)
    s = _rolling_std(dv, _TD_MON)
    z = _safe_div(dv - m, s)
    return z.diff(_TD_WEEK)


def dvs_drv2_029_dv_log_zscore_63d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 63-day log-DV z-score."""
    dv = _log_safe(_dv(close, volume))
    m = _rolling_mean(dv, _TD_QTR)
    s = _rolling_std(dv, _TD_QTR)
    z = _safe_div(dv - m, s)
    return z.diff(_TD_WEEK)


def dvs_drv2_030_dv_log_zscore_252d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 252-day log-DV z-score."""
    dv = _log_safe(_dv(close, volume))
    m = _rolling_mean(dv, _TD_YEAR)
    s = _rolling_std(dv, _TD_YEAR)
    z = _safe_div(dv - m, s)
    return z.diff(_TD_MON)


def dvs_drv2_031_dv_spike_count_3x_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day 3x-DV spike count."""
    dv = _dv(close, volume)
    baseline = _rolling_mean(dv, _TD_QTR)
    spike = (dv > 3.0 * baseline).astype(float)
    count21 = _rolling_sum(spike, _TD_MON)
    return count21.diff(_TD_WEEK)


def dvs_drv2_032_dv_spike_fraction_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of fraction of 63-day 2x-DV spike days."""
    dv = _dv(close, volume)
    baseline = _rolling_mean(dv, _TD_QTR)
    spike = (dv > 2.0 * baseline).astype(float)
    frac = _rolling_sum(spike, _TD_QTR) / _TD_QTR
    return frac.diff(_TD_MON)


def dvs_drv2_033_dv_pct_rank_63d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 63-day DV percentile rank."""
    dv = _dv(close, volume)
    rank = dv.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)
    return rank.diff(_TD_WEEK)


def dvs_drv2_034_dv_pct_rank_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day DV percentile rank."""
    dv = _dv(close, volume)
    rank = dv.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).rank(pct=True)
    return rank.diff(_TD_WEEK)


def dvs_drv2_035_dv_cumsum_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day cumulative dollar volume."""
    dv = _dv(close, volume)
    cs = _rolling_sum(dv, _TD_MON)
    return cs.diff(_TD_WEEK)


def dvs_drv2_036_dv_cumsum_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day cumulative dollar volume."""
    dv = _dv(close, volume)
    cs = _rolling_sum(dv, _TD_QTR)
    return cs.diff(_TD_MON)


def dvs_drv2_037_dv_daily_change_pct_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of day-over-day DV percent change (acceleration of DV momentum)."""
    dv = _dv(close, volume)
    chg = dv.pct_change(1)
    return chg.diff(_TD_WEEK)


def dvs_drv2_038_dv_5d_change_pct_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 5-day DV percent change."""
    dv = _dv(close, volume)
    chg = dv.pct_change(_TD_WEEK)
    return chg.diff(_TD_WEEK)


def dvs_drv2_039_dv_21d_change_pct_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 21-day DV percent change."""
    dv = _dv(close, volume)
    chg = dv.pct_change(_TD_MON)
    return chg.diff(_TD_MON)


def dvs_drv2_040_dv_max_63d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 63-day maximum dollar volume."""
    dv = _dv(close, volume)
    mx = _rolling_max(dv, _TD_QTR)
    return mx.diff(_TD_WEEK)


def dvs_drv2_041_dv_current_vs_max_63d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of ratio of current DV to 63-day maximum."""
    dv = _dv(close, volume)
    ratio = _safe_div(dv, _rolling_max(dv, _TD_QTR))
    return ratio.diff(_TD_WEEK)


def dvs_drv2_042_dv_current_vs_expanding_max_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of ratio of current DV to all-time expanding maximum."""
    dv = _dv(close, volume)
    ratio = _safe_div(dv, dv.expanding(min_periods=1).max())
    return ratio.diff(_TD_WEEK)


def dvs_drv2_043_dv_on_down_days_sum_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day down-day DV sum."""
    dv = _dv(close, volume)
    ret = close.pct_change(1)
    dv_dn = dv.where(ret < 0, 0.0)
    cs = _rolling_sum(dv_dn, _TD_QTR)
    return cs.diff(_TD_MON)


def dvs_drv2_044_dv_down_vs_up_ratio_252d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 252-day DV down/up ratio."""
    dv = _dv(close, volume)
    ret = close.pct_change(1)
    dv_dn = dv.where(ret < 0, np.nan).rolling(_TD_YEAR, min_periods=1).mean()
    dv_up = dv.where(ret > 0, np.nan).rolling(_TD_YEAR, min_periods=1).mean()
    ratio = _safe_div(dv_dn, dv_up)
    return ratio.diff(_TD_MON)


def dvs_drv2_045_dv_price_ret_product_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day sum of (DV * daily return) — change in signed dollar pressure."""
    dv = _dv(close, volume)
    ret = close.pct_change(1)
    signed = _rolling_sum(dv * ret, _TD_QTR)
    return signed.diff(_TD_MON)


def dvs_drv2_046_dv_weighted_negative_return_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of DV-weighted average negative return over 63 days."""
    dv = _dv(close, volume)
    ret = close.pct_change(1)
    neg_ret = ret.where(ret < 0, 0.0)
    wnr = _safe_div(_rolling_sum(dv * neg_ret, _TD_QTR), _rolling_sum(dv, _TD_QTR))
    return wnr.diff(_TD_MON)


def dvs_drv2_047_dv_sum_21d_vs_252d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of ratio of 21d sum DV to 252d sum DV."""
    dv = _dv(close, volume)
    ratio = _safe_div(_rolling_sum(dv, _TD_MON), _rolling_sum(dv, _TD_YEAR))
    return ratio.diff(_TD_WEEK)


def dvs_drv2_048_dv_ewm5_vs_ewm63_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of EWM5/EWM63 ratio of DV."""
    dv = _dv(close, volume)
    ratio = _safe_div(_ewm_mean(dv, _TD_WEEK), _ewm_mean(dv, _TD_QTR))
    return ratio.diff(_TD_WEEK)


def dvs_drv2_049_dv_ewm21_vs_ewm126_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of EWM21/EWM126 ratio of DV."""
    dv = _dv(close, volume)
    ratio = _safe_div(_ewm_mean(dv, _TD_MON), _ewm_mean(dv, 126))
    return ratio.diff(_TD_WEEK)


def dvs_drv2_050_dv_slope_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of OLS slope of DV over 63 days."""
    dv = _dv(close, volume)
    slp = _linslope(dv, _TD_QTR)
    return slp.diff(_TD_MON)


def dvs_drv2_051_dv_log_slope_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of OLS slope of log-DV over 63 days."""
    dv = _log_safe(_dv(close, volume))
    slp = _linslope(dv, _TD_QTR)
    return slp.diff(_TD_MON)


def dvs_drv2_052_dv_slope_norm_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of normalized OLS slope of DV over 21 days."""
    dv = _dv(close, volume)
    norm = _safe_div(dv, _rolling_mean(dv, _TD_MON))
    slp = _linslope(norm, _TD_MON)
    return slp.diff(_TD_WEEK)


def dvs_drv2_053_dv_at_new_low_fraction_252d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of fraction of 252d DV at new-252d-low days."""
    dv = _dv(close, volume)
    roll_min = close.shift(1).rolling(_TD_YEAR, min_periods=126).min()
    new_low = close < roll_min
    dv_nl = dv.where(new_low, 0.0)
    frac = _safe_div(_rolling_sum(dv_nl, _TD_YEAR), _rolling_sum(dv, _TD_YEAR))
    return frac.diff(_TD_MON)


def dvs_drv2_054_dv_bottom_decile_price_sum_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of DV sum at bottom-decile price days."""
    from numpy import arange
    dv = _dv(close, volume)
    roll_min = _rolling_mean(close, _TD_YEAR) - 2 * _rolling_std(close, _TD_YEAR)
    at_bottom = close <= roll_min
    cs = _rolling_sum(dv.where(at_bottom, 0.0), _TD_QTR)
    return cs.diff(_TD_MON)


def dvs_drv2_055_dv_acceleration_5d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 5-day acceleration of 21d average DV."""
    dv = _dv(close, volume)
    avg21 = _rolling_mean(dv, _TD_MON)
    acc = avg21.pct_change(_TD_WEEK)
    return acc.diff(_TD_WEEK)


def dvs_drv2_056_dv_std_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day DV standard deviation (velocity of DV volatility)."""
    dv = _dv(close, volume)
    std = _rolling_std(dv, _TD_MON)
    return std.diff(_TD_WEEK)


def dvs_drv2_057_dv_std_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day DV standard deviation."""
    dv = _dv(close, volume)
    std = _rolling_std(dv, _TD_QTR)
    return std.diff(_TD_MON)


def dvs_drv2_058_dv_cv_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day DV coefficient of variation."""
    dv = _dv(close, volume)
    cv = _safe_div(_rolling_std(dv, _TD_QTR), _rolling_mean(dv, _TD_QTR))
    return cv.diff(_TD_MON)


def dvs_drv2_059_dv_cv_252d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 252-day DV coefficient of variation."""
    dv = _dv(close, volume)
    cv = _safe_div(_rolling_std(dv, _TD_YEAR), _rolling_mean(dv, _TD_YEAR))
    return cv.diff(_TD_MON)


def dvs_drv2_060_dv_distress_index_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63d DV distress index."""
    dv = _dv(close, volume)
    m = _rolling_mean(dv, _TD_QTR)
    s = _rolling_std(dv, _TD_QTR)
    z = _safe_div(dv - m, s)
    ret = close.pct_change(1)
    dn_frac = (ret < 0).astype(float).rolling(_TD_QTR, min_periods=1).sum() / _TD_QTR
    distress = z * dn_frac
    return distress.diff(_TD_MON)


def dvs_drv2_061_dv_composite_score_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of blended DV composite score (ratio + rank)."""
    dv = _dv(close, volume)
    ratio = _safe_div(dv, _rolling_mean(dv, _TD_QTR))
    rank = dv.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)
    composite = (ratio + rank) / 2.0
    return composite.diff(_TD_MON)


def dvs_drv2_062_dv_tail_risk_score_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day DV tail risk score."""
    dv = _dv(close, volume)
    ratio = _safe_div(dv, _rolling_mean(dv, _TD_MON))
    cv = _safe_div(_rolling_std(dv, _TD_MON), _rolling_mean(dv, _TD_MON))
    tail = ratio * cv
    return tail.diff(_TD_WEEK)


def dvs_drv2_063_dv_hhi_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day DV concentration HHI."""
    dv = _dv(close, volume)
    sum63 = _rolling_sum(dv, _TD_QTR)
    share = _safe_div(dv, sum63)
    hhi = _rolling_sum(share ** 2, _TD_QTR)
    return hhi.diff(_TD_MON)


def dvs_drv2_064_dv_high_low_range_ratio_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of (21d max DV - 21d min DV) / 21d mean DV."""
    dv = _dv(close, volume)
    mx = _rolling_max(dv, _TD_MON)
    mn = _rolling_min(dv, _TD_MON)
    mean = _rolling_mean(dv, _TD_MON)
    rng_ratio = _safe_div(mx - mn, mean)
    return rng_ratio.diff(_TD_WEEK)


def dvs_drv2_065_dv_spike_count_2x_252d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 252-day 2x-DV spike count."""
    dv = _dv(close, volume)
    baseline = _rolling_mean(dv, _TD_QTR)
    spike = (dv > 2.0 * baseline).astype(float)
    count252 = _rolling_sum(spike, _TD_YEAR)
    return count252.diff(_TD_MON)


def dvs_drv2_066_dv_ratio_21d_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 21-day DV ratio."""
    dv = _dv(close, volume)
    ratio = _safe_div(dv, _rolling_mean(dv, _TD_MON))
    return _linslope(ratio, _TD_MON)


def dvs_drv2_067_dv_zscore_252d_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope over 63 days of the 252-day DV z-score."""
    dv = _dv(close, volume)
    m = _rolling_mean(dv, _TD_YEAR)
    s = _rolling_std(dv, _TD_YEAR)
    z = _safe_div(dv - m, s)
    return _linslope(z, _TD_QTR)


def dvs_drv2_068_dv_pct_rank_252d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 252-day DV percentile rank."""
    dv = _dv(close, volume)
    rank = dv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return rank.diff(_TD_MON)


def dvs_drv2_069_dv_ewm21_vs_ewm252_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of EWM21/EWM252 ratio of DV."""
    dv = _dv(close, volume)
    ratio = _safe_div(_ewm_mean(dv, _TD_MON), _ewm_mean(dv, _TD_YEAR))
    return ratio.diff(_TD_WEEK)


def dvs_drv2_070_dv_spike_on_down_day_252d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 252-day DV-spike-on-down-day count."""
    dv = _dv(close, volume)
    baseline = _rolling_mean(dv, _TD_QTR)
    ret = close.pct_change(1)
    spike_dn = ((dv > 2.0 * baseline) & (ret < 0)).astype(float)
    count252 = _rolling_sum(spike_dn, _TD_YEAR)
    return count252.diff(_TD_MON)


def dvs_drv2_071_dv_down_day_dv_fraction_252d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of fraction of 252d DV on down-price days."""
    dv = _dv(close, volume)
    ret = close.pct_change(1)
    dv_dn = dv.where(ret < 0, 0.0)
    frac = _safe_div(_rolling_sum(dv_dn, _TD_YEAR), _rolling_sum(dv, _TD_YEAR))
    return frac.diff(_TD_MON)


def dvs_drv2_072_dv_persistence_score_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day DV persistence score."""
    dv = _dv(close, volume)
    above = (dv > dv.shift(1)).astype(float)
    persistence = _rolling_sum(above, _TD_QTR) / _TD_QTR
    return persistence.diff(_TD_MON)


def dvs_drv2_073_dv_log_ratio_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of log-DV-ratio-63d."""
    dv = _dv(close, volume)
    log_ratio = _log_safe(dv) - _log_safe(_rolling_mean(dv, _TD_QTR))
    return log_ratio.diff(_TD_MON)


def dvs_drv2_074_dv_max_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day rolling maximum dollar volume."""
    dv = _dv(close, volume)
    mx = _rolling_max(dv, _TD_MON)
    return mx.diff(_TD_WEEK)


def dvs_drv2_075_dv_concentration_hhi_21d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 21-day DV concentration HHI (changing concentration speed)."""
    dv = _dv(close, volume)
    sum21 = _rolling_sum(dv, _TD_MON)
    share = _safe_div(dv, sum21)
    hhi = _rolling_sum(share ** 2, _TD_MON)
    return hhi.diff(_TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

DOLLAR_VOLUME_SHOCK_REGISTRY_2ND_DERIVATIVES = {
    "dvs_drv2_001_dv_ratio_21d_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_001_dv_ratio_21d_5d_diff},
    "dvs_drv2_002_dv_ratio_63d_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_002_dv_ratio_63d_5d_diff},
    "dvs_drv2_003_dv_ratio_63d_21d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_003_dv_ratio_63d_21d_diff},
    "dvs_drv2_004_dv_zscore_63d_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_004_dv_zscore_63d_5d_diff},
    "dvs_drv2_005_dv_zscore_252d_21d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_005_dv_zscore_252d_21d_diff},
    "dvs_drv2_006_dv_log_ratio_21d_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_006_dv_log_ratio_21d_5d_diff},
    "dvs_drv2_007_dv_spike_count_2x_21d_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_007_dv_spike_count_2x_21d_5d_diff},
    "dvs_drv2_008_dv_spike_count_2x_63d_21d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_008_dv_spike_count_2x_63d_21d_diff},
    "dvs_drv2_009_dv_down_vs_up_ratio_21d_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_009_dv_down_vs_up_ratio_21d_5d_diff},
    "dvs_drv2_010_dv_down_vs_up_ratio_63d_21d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_010_dv_down_vs_up_ratio_63d_21d_diff},
    "dvs_drv2_011_dv_pct_rank_252d_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_011_dv_pct_rank_252d_5d_diff},
    "dvs_drv2_012_dv_sum_21d_ratio_252d_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_012_dv_sum_21d_ratio_252d_5d_diff},
    "dvs_drv2_013_dv_ewm21_vs_ewm63_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_013_dv_ewm21_vs_ewm63_5d_diff},
    "dvs_drv2_014_dv_cv_21d_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_014_dv_cv_21d_5d_diff},
    "dvs_drv2_015_dv_ratio_21d_slope_63d": {"inputs": ["close", "volume"], "func": dvs_drv2_015_dv_ratio_21d_slope_63d},
    "dvs_drv2_016_dv_zscore_63d_slope_21d": {"inputs": ["close", "volume"], "func": dvs_drv2_016_dv_zscore_63d_slope_21d},
    "dvs_drv2_017_dv_spike_on_down_day_63d_21d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_017_dv_spike_on_down_day_63d_21d_diff},
    "dvs_drv2_018_dv_at_new_low_fraction_63d_21d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_018_dv_at_new_low_fraction_63d_21d_diff},
    "dvs_drv2_019_dv_distress_index_21d_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_019_dv_distress_index_21d_5d_diff},
    "dvs_drv2_020_dv_log_ratio_252d_21d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_020_dv_log_ratio_252d_21d_diff},
    "dvs_drv2_021_dv_max_21d_vs_mean_252d_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_021_dv_max_21d_vs_mean_252d_5d_diff},
    "dvs_drv2_022_dv_persistence_score_21d_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_022_dv_persistence_score_21d_5d_diff},
    "dvs_drv2_023_dv_hhi_21d_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_023_dv_hhi_21d_5d_diff},
    "dvs_drv2_024_dv_spike_recency_decay_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_024_dv_spike_recency_decay_5d_diff},
    "dvs_drv2_025_dv_capitulation_composite_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_025_dv_capitulation_composite_5d_diff},
    "dvs_drv2_026_dv_ratio_126d_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_026_dv_ratio_126d_5d_diff},
    "dvs_drv2_027_dv_ratio_252d_21d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_027_dv_ratio_252d_21d_diff},
    "dvs_drv2_028_dv_zscore_21d_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_028_dv_zscore_21d_5d_diff},
    "dvs_drv2_029_dv_log_zscore_63d_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_029_dv_log_zscore_63d_5d_diff},
    "dvs_drv2_030_dv_log_zscore_252d_21d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_030_dv_log_zscore_252d_21d_diff},
    "dvs_drv2_031_dv_spike_count_3x_21d_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_031_dv_spike_count_3x_21d_5d_diff},
    "dvs_drv2_032_dv_spike_fraction_63d_21d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_032_dv_spike_fraction_63d_21d_diff},
    "dvs_drv2_033_dv_pct_rank_63d_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_033_dv_pct_rank_63d_5d_diff},
    "dvs_drv2_034_dv_pct_rank_21d_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_034_dv_pct_rank_21d_5d_diff},
    "dvs_drv2_035_dv_cumsum_21d_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_035_dv_cumsum_21d_5d_diff},
    "dvs_drv2_036_dv_cumsum_63d_21d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_036_dv_cumsum_63d_21d_diff},
    "dvs_drv2_037_dv_daily_change_pct_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_037_dv_daily_change_pct_5d_diff},
    "dvs_drv2_038_dv_5d_change_pct_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_038_dv_5d_change_pct_5d_diff},
    "dvs_drv2_039_dv_21d_change_pct_21d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_039_dv_21d_change_pct_21d_diff},
    "dvs_drv2_040_dv_max_63d_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_040_dv_max_63d_5d_diff},
    "dvs_drv2_041_dv_current_vs_max_63d_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_041_dv_current_vs_max_63d_5d_diff},
    "dvs_drv2_042_dv_current_vs_expanding_max_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_042_dv_current_vs_expanding_max_5d_diff},
    "dvs_drv2_043_dv_on_down_days_sum_63d_21d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_043_dv_on_down_days_sum_63d_21d_diff},
    "dvs_drv2_044_dv_down_vs_up_ratio_252d_21d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_044_dv_down_vs_up_ratio_252d_21d_diff},
    "dvs_drv2_045_dv_price_ret_product_63d_21d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_045_dv_price_ret_product_63d_21d_diff},
    "dvs_drv2_046_dv_weighted_negative_return_63d_21d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_046_dv_weighted_negative_return_63d_21d_diff},
    "dvs_drv2_047_dv_sum_21d_vs_252d_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_047_dv_sum_21d_vs_252d_5d_diff},
    "dvs_drv2_048_dv_ewm5_vs_ewm63_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_048_dv_ewm5_vs_ewm63_5d_diff},
    "dvs_drv2_049_dv_ewm21_vs_ewm126_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_049_dv_ewm21_vs_ewm126_5d_diff},
    "dvs_drv2_050_dv_slope_63d_21d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_050_dv_slope_63d_21d_diff},
    "dvs_drv2_051_dv_log_slope_63d_21d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_051_dv_log_slope_63d_21d_diff},
    "dvs_drv2_052_dv_slope_norm_21d_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_052_dv_slope_norm_21d_5d_diff},
    "dvs_drv2_053_dv_at_new_low_fraction_252d_21d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_053_dv_at_new_low_fraction_252d_21d_diff},
    "dvs_drv2_054_dv_bottom_decile_price_sum_63d_21d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_054_dv_bottom_decile_price_sum_63d_21d_diff},
    "dvs_drv2_055_dv_acceleration_5d_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_055_dv_acceleration_5d_5d_diff},
    "dvs_drv2_056_dv_std_21d_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_056_dv_std_21d_5d_diff},
    "dvs_drv2_057_dv_std_63d_21d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_057_dv_std_63d_21d_diff},
    "dvs_drv2_058_dv_cv_63d_21d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_058_dv_cv_63d_21d_diff},
    "dvs_drv2_059_dv_cv_252d_21d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_059_dv_cv_252d_21d_diff},
    "dvs_drv2_060_dv_distress_index_63d_21d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_060_dv_distress_index_63d_21d_diff},
    "dvs_drv2_061_dv_composite_score_63d_21d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_061_dv_composite_score_63d_21d_diff},
    "dvs_drv2_062_dv_tail_risk_score_21d_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_062_dv_tail_risk_score_21d_5d_diff},
    "dvs_drv2_063_dv_hhi_63d_21d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_063_dv_hhi_63d_21d_diff},
    "dvs_drv2_064_dv_high_low_range_ratio_21d_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_064_dv_high_low_range_ratio_21d_5d_diff},
    "dvs_drv2_065_dv_spike_count_2x_252d_21d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_065_dv_spike_count_2x_252d_21d_diff},
    "dvs_drv2_066_dv_ratio_21d_slope_21d": {"inputs": ["close", "volume"], "func": dvs_drv2_066_dv_ratio_21d_slope_21d},
    "dvs_drv2_067_dv_zscore_252d_slope_63d": {"inputs": ["close", "volume"], "func": dvs_drv2_067_dv_zscore_252d_slope_63d},
    "dvs_drv2_068_dv_pct_rank_252d_21d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_068_dv_pct_rank_252d_21d_diff},
    "dvs_drv2_069_dv_ewm21_vs_ewm252_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_069_dv_ewm21_vs_ewm252_5d_diff},
    "dvs_drv2_070_dv_spike_on_down_day_252d_21d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_070_dv_spike_on_down_day_252d_21d_diff},
    "dvs_drv2_071_dv_down_day_dv_fraction_252d_21d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_071_dv_down_day_dv_fraction_252d_21d_diff},
    "dvs_drv2_072_dv_persistence_score_63d_21d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_072_dv_persistence_score_63d_21d_diff},
    "dvs_drv2_073_dv_log_ratio_63d_21d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_073_dv_log_ratio_63d_21d_diff},
    "dvs_drv2_074_dv_max_21d_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_074_dv_max_21d_5d_diff},
    "dvs_drv2_075_dv_concentration_hhi_21d_21d_diff": {"inputs": ["close", "volume"], "func": dvs_drv2_075_dv_concentration_hhi_21d_21d_diff},
}
