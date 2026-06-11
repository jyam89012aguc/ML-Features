"""
23_dollar_volume_shock — 3rd Derivatives (Features drv3_001-025)
Domain: rate of change of 2nd-derivative dollar-volume-shock features — acceleration of velocity
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


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────

def dvs_drv3_001_dv_ratio_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day DV ratio (acceleration of DV surge velocity)."""
    dv = _dv(close, volume)
    ratio = _safe_div(dv, _rolling_mean(dv, _TD_MON))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dvs_drv3_002_dv_ratio_63d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day DV ratio."""
    dv = _dv(close, volume)
    ratio = _safe_div(dv, _rolling_mean(dv, _TD_QTR))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dvs_drv3_003_dv_ratio_63d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 63-day DV ratio."""
    dv = _dv(close, volume)
    ratio = _safe_div(dv, _rolling_mean(dv, _TD_QTR))
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dvs_drv3_004_dv_zscore_63d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day DV z-score (jerk in z-score acceleration)."""
    dv = _dv(close, volume)
    m = _rolling_mean(dv, _TD_QTR)
    s = _rolling_std(dv, _TD_QTR)
    z = _safe_div(dv - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dvs_drv3_005_dv_zscore_252d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 252-day DV z-score."""
    dv = _dv(close, volume)
    m = _rolling_mean(dv, _TD_YEAR)
    s = _rolling_std(dv, _TD_YEAR)
    z = _safe_div(dv - m, s)
    vel21 = z.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dvs_drv3_006_dv_log_ratio_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of log-DV-ratio-21d."""
    dv = _dv(close, volume)
    log_ratio = _log_safe(dv) - _log_safe(_rolling_mean(dv, _TD_MON))
    vel = log_ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dvs_drv3_007_dv_down_vs_up_ratio_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day DV down/up ratio."""
    dv = _dv(close, volume)
    ret = close.pct_change(1)
    dv_dn = dv.where(ret < 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    dv_up = dv.where(ret > 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    ratio = _safe_div(dv_dn, dv_up)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dvs_drv3_008_dv_down_vs_up_ratio_63d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 63-day DV down/up ratio."""
    dv = _dv(close, volume)
    ret = close.pct_change(1)
    dv_dn = dv.where(ret < 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    dv_up = dv.where(ret > 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    ratio = _safe_div(dv_dn, dv_up)
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dvs_drv3_009_dv_pct_rank_252d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 252-day DV percentile rank."""
    dv = _dv(close, volume)
    rank = dv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    vel = rank.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dvs_drv3_010_dv_spike_count_63d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 63-day spike count."""
    dv = _dv(close, volume)
    baseline = _rolling_mean(dv, _TD_QTR)
    spike = (dv > 2.0 * baseline).astype(float)
    count63 = _rolling_sum(spike, _TD_QTR)
    vel21 = count63.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dvs_drv3_011_dv_ewm21_vs_ewm63_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of EWM21/EWM63 DV ratio."""
    dv = _dv(close, volume)
    ratio = _safe_div(_ewm_mean(dv, _TD_MON), _ewm_mean(dv, _TD_QTR))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dvs_drv3_012_dv_cv_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day DV coefficient of variation."""
    dv = _dv(close, volume)
    cv = _safe_div(_rolling_std(dv, _TD_MON), _rolling_mean(dv, _TD_MON))
    vel = cv.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dvs_drv3_013_dv_zscore_63d_slope_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 63-day DV z-score (rate of slope change)."""
    dv = _dv(close, volume)
    m = _rolling_mean(dv, _TD_QTR)
    s = _rolling_std(dv, _TD_QTR)
    z = _safe_div(dv - m, s)
    slp = _linslope(z, _TD_MON)
    return slp.diff(_TD_WEEK)


def dvs_drv3_014_dv_ratio_21d_slope_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21-day DV ratio."""
    dv = _dv(close, volume)
    ratio = _safe_div(dv, _rolling_mean(dv, _TD_MON))
    slp = _linslope(ratio, _TD_QTR)
    return slp.diff(_TD_WEEK)


def dvs_drv3_015_dv_distress_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of DV distress index."""
    dv = _dv(close, volume)
    ratio = _safe_div(dv, _rolling_mean(dv, _TD_QTR))
    ret = close.pct_change(1)
    dn_frac = (ret < 0).astype(float).rolling(_TD_MON, min_periods=1).sum() / _TD_MON
    distress = ratio * dn_frac
    vel = distress.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dvs_drv3_016_dv_spike_recency_decay_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of EWM-decayed DV spike signal."""
    dv = _dv(close, volume)
    baseline = _rolling_mean(dv, _TD_QTR)
    spike = (dv > 2.0 * baseline).astype(float)
    decay = spike.ewm(halflife=5, min_periods=1).mean()
    vel = decay.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dvs_drv3_017_dv_log_ratio_252d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in log-DV-ratio-252d."""
    dv = _dv(close, volume)
    log_ratio = _log_safe(dv) - _log_safe(_rolling_mean(dv, _TD_YEAR))
    vel21 = log_ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dvs_drv3_018_dv_persistence_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day DV persistence score."""
    dv = _dv(close, volume)
    above = (dv > dv.shift(1)).astype(float)
    persistence = _rolling_sum(above, _TD_MON) / _TD_MON
    vel = persistence.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dvs_drv3_019_dv_hhi_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day DV concentration HHI."""
    dv = _dv(close, volume)
    sum21 = _rolling_sum(dv, _TD_MON)
    share = _safe_div(dv, sum21)
    hhi = _rolling_sum(share ** 2, _TD_MON)
    vel = hhi.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dvs_drv3_020_dv_capitulation_composite_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of DV capitulation composite score."""
    dv = _dv(close, volume)
    m = _rolling_mean(dv, _TD_QTR)
    s = _rolling_std(dv, _TD_QTR)
    z63 = _safe_div(dv - m, s)
    ret = close.pct_change(1)
    dn_frac = (ret < 0).astype(float).rolling(_TD_MON, min_periods=1).sum() / _TD_MON
    rank = dv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True).fillna(0.0)
    composite = z63 * dn_frac * (1.0 + rank)
    vel = composite.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dvs_drv3_021_dv_spike_on_down_day_63d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63d DV-spike-on-down-day count."""
    dv = _dv(close, volume)
    baseline = _rolling_mean(dv, _TD_QTR)
    ret = close.pct_change(1)
    spike_dn = ((dv > 2.0 * baseline) & (ret < 0)).astype(float)
    count63 = _rolling_sum(spike_dn, _TD_QTR)
    vel21 = count63.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dvs_drv3_022_dv_at_new_low_frac_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in fraction of DV at new-63d-low."""
    dv = _dv(close, volume)
    roll_min = close.shift(1).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    new_low = close < roll_min
    dv_nl = dv.where(new_low, 0.0)
    total = _rolling_sum(dv, _TD_QTR)
    frac = _safe_div(_rolling_sum(dv_nl, _TD_QTR), total)
    vel21 = frac.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dvs_drv3_023_dv_max_21d_vs_mean_252d_5d_diff_slope(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day diff of (21d max DV / 252d mean)."""
    dv = _dv(close, volume)
    ratio = _safe_div(dv.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).max(),
                      _rolling_mean(dv, _TD_YEAR))
    vel = ratio.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def dvs_drv3_024_dv_sum_21d_ratio_252d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of (21d DV sum / 252d DV sum) ratio."""
    dv = _dv(close, volume)
    ratio = _safe_div(_rolling_sum(dv, _TD_MON), _rolling_sum(dv, _TD_YEAR))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dvs_drv3_025_dv_spike_count_21d_zscore_252d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of z-score of 21d spike count vs 252-day distribution."""
    dv = _dv(close, volume)
    baseline = _rolling_mean(dv, _TD_QTR)
    spike = (dv > 2.0 * baseline).astype(float)
    count21 = _rolling_sum(spike, _TD_MON)
    m = _rolling_mean(count21, _TD_YEAR)
    s = _rolling_std(count21, _TD_YEAR)
    z = _safe_div(count21 - m, s)
    return z.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

DOLLAR_VOLUME_SHOCK_REGISTRY_3RD_DERIVATIVES = {
    "dvs_drv3_001_dv_ratio_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv3_001_dv_ratio_21d_5d_diff_5d_diff},
    "dvs_drv3_002_dv_ratio_63d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv3_002_dv_ratio_63d_5d_diff_5d_diff},
    "dvs_drv3_003_dv_ratio_63d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv3_003_dv_ratio_63d_21d_diff_5d_diff},
    "dvs_drv3_004_dv_zscore_63d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv3_004_dv_zscore_63d_5d_diff_5d_diff},
    "dvs_drv3_005_dv_zscore_252d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv3_005_dv_zscore_252d_21d_diff_5d_diff},
    "dvs_drv3_006_dv_log_ratio_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv3_006_dv_log_ratio_21d_5d_diff_5d_diff},
    "dvs_drv3_007_dv_down_vs_up_ratio_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv3_007_dv_down_vs_up_ratio_21d_5d_diff_5d_diff},
    "dvs_drv3_008_dv_down_vs_up_ratio_63d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv3_008_dv_down_vs_up_ratio_63d_21d_diff_5d_diff},
    "dvs_drv3_009_dv_pct_rank_252d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv3_009_dv_pct_rank_252d_5d_diff_5d_diff},
    "dvs_drv3_010_dv_spike_count_63d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv3_010_dv_spike_count_63d_21d_diff_5d_diff},
    "dvs_drv3_011_dv_ewm21_vs_ewm63_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv3_011_dv_ewm21_vs_ewm63_5d_diff_5d_diff},
    "dvs_drv3_012_dv_cv_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv3_012_dv_cv_21d_5d_diff_5d_diff},
    "dvs_drv3_013_dv_zscore_63d_slope_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv3_013_dv_zscore_63d_slope_5d_diff},
    "dvs_drv3_014_dv_ratio_21d_slope_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv3_014_dv_ratio_21d_slope_5d_diff},
    "dvs_drv3_015_dv_distress_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv3_015_dv_distress_21d_5d_diff_5d_diff},
    "dvs_drv3_016_dv_spike_recency_decay_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv3_016_dv_spike_recency_decay_5d_diff_5d_diff},
    "dvs_drv3_017_dv_log_ratio_252d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv3_017_dv_log_ratio_252d_21d_diff_5d_diff},
    "dvs_drv3_018_dv_persistence_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv3_018_dv_persistence_21d_5d_diff_5d_diff},
    "dvs_drv3_019_dv_hhi_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv3_019_dv_hhi_21d_5d_diff_5d_diff},
    "dvs_drv3_020_dv_capitulation_composite_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv3_020_dv_capitulation_composite_5d_diff_5d_diff},
    "dvs_drv3_021_dv_spike_on_down_day_63d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv3_021_dv_spike_on_down_day_63d_21d_diff_5d_diff},
    "dvs_drv3_022_dv_at_new_low_frac_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv3_022_dv_at_new_low_frac_21d_diff_5d_diff},
    "dvs_drv3_023_dv_max_21d_vs_mean_252d_5d_diff_slope": {"inputs": ["close", "volume"], "func": dvs_drv3_023_dv_max_21d_vs_mean_252d_5d_diff_slope},
    "dvs_drv3_024_dv_sum_21d_ratio_252d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv3_024_dv_sum_21d_ratio_252d_5d_diff_5d_diff},
    "dvs_drv3_025_dv_spike_count_21d_zscore_252d_5d_diff": {"inputs": ["close", "volume"], "func": dvs_drv3_025_dv_spike_count_21d_zscore_252d_5d_diff},
}
