"""
54_turnover_ratio — Base Features 076-150
Domain: long-horizon turnover-rate extremes via price/volume proxy
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — multi-year turnover extremes, float-proxy baseline,
  illiquidity signals, turnover-rate percentile vs years-long history.
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
_TD_2YR = 504
_TD_3YR = 756
_EPS = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    return num / den.replace(0, np.nan)


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _dollar_volume(close: pd.Series, volume: pd.Series) -> pd.Series:
    return close * volume


def _turnover_proxy(volume: pd.Series, window: int) -> pd.Series:
    baseline = _rolling_mean(volume, window)
    return _safe_div(volume, baseline)


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


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-085): Turnover vs VWAP / price-weighted vol proxies ---

def tnv_076_vol_per_unit_close_252d_norm(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-per-price-unit normalised by 252d mean (share-equivalent turnover proxy)."""
    vpu = _safe_div(volume, close)
    return _safe_div(vpu, _rolling_mean(vpu, _TD_YEAR))


def tnv_077_vol_per_unit_close_504d_norm(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-per-price-unit normalised by 504d mean."""
    vpu = _safe_div(volume, close)
    return _safe_div(vpu, _rolling_mean(vpu, _TD_2YR))


def tnv_078_vol_per_unit_close_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pct rank of volume-per-price-unit in trailing 252-day distribution."""
    vpu = _safe_div(volume, close)
    return vpu.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def tnv_079_vol_per_unit_close_pct_rank_504d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pct rank of volume-per-price-unit in trailing 504-day distribution."""
    vpu = _safe_div(volume, close)
    return vpu.rolling(_TD_2YR, min_periods=_TD_YEAR).rank(pct=True)


def tnv_080_dvol_pct_rank_756d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pct rank of dollar-volume in trailing 756-day distribution."""
    dv = _dollar_volume(close, volume)
    return dv.rolling(_TD_3YR, min_periods=_TD_2YR).rank(pct=True)


def tnv_081_dvol_expanding_pct_rank(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Expanding all-history pct rank of dollar-volume."""
    dv = _dollar_volume(close, volume)
    return dv.expanding(min_periods=_TD_QTR).rank(pct=True)


def tnv_082_dvol_zscore_756d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of dollar-volume vs 756-day distribution."""
    dv = _dollar_volume(close, volume)
    m = _rolling_mean(dv, _TD_3YR)
    s = _rolling_std(dv, _TD_3YR)
    return _safe_div(dv - m, s)


def tnv_083_log_dvol_vs_504d_mean(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Log ratio of dollar-volume to 504-day mean dollar-volume."""
    dv = _dollar_volume(close, volume)
    return _log_safe(dv) - _log_safe(_rolling_mean(dv, _TD_2YR))


def tnv_084_dvol_vs_cum_dvol_756d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Daily dollar-volume as fraction of 756-day cumulative dollar-volume."""
    dv = _dollar_volume(close, volume)
    return _safe_div(dv, _rolling_sum(dv, _TD_3YR))


def tnv_085_dvol_mean_252d_vs_504d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 252d mean dollar-volume to 504d mean (recent vs 2yr activity)."""
    dv = _dollar_volume(close, volume)
    return _safe_div(_rolling_mean(dv, _TD_YEAR), _rolling_mean(dv, _TD_2YR))


# --- Group I (086-095): Turnover vs price level — low-price illiquidity signals ---

def tnv_086_vol_times_close_pct_ret_252d_mean(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol * abs(daily pct return) as activity proxy, normalised by 252d mean."""
    act = volume * close.pct_change(1).abs()
    return _safe_div(act, _rolling_mean(act, _TD_YEAR))


def tnv_087_vol_times_close_pct_ret_504d_mean(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol * abs(daily pct return) normalised by 504d mean."""
    act = volume * close.pct_change(1).abs()
    return _safe_div(act, _rolling_mean(act, _TD_2YR))


def tnv_088_amihud_illiquidity_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Amihud illiquidity: avg(|ret|/dollar-vol) over 252 days (low dvol = illiquid)."""
    ret_abs = close.pct_change(1).abs()
    dv = _dollar_volume(close, volume).replace(0, np.nan)
    illiq = _safe_div(ret_abs, dv)
    return illiq.rolling(_TD_YEAR, min_periods=_TD_QTR).mean()


def tnv_089_amihud_illiquidity_504d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Amihud illiquidity averaged over 504 days."""
    ret_abs = close.pct_change(1).abs()
    dv = _dollar_volume(close, volume).replace(0, np.nan)
    illiq = _safe_div(ret_abs, dv)
    return illiq.rolling(_TD_2YR, min_periods=_TD_YEAR).mean()


def tnv_090_amihud_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pct rank of Amihud illiquidity in trailing 252-day distribution."""
    ret_abs = close.pct_change(1).abs()
    dv = _dollar_volume(close, volume).replace(0, np.nan)
    illiq = _safe_div(ret_abs, dv)
    return illiq.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def tnv_091_amihud_pct_rank_504d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pct rank of Amihud illiquidity in trailing 504-day distribution."""
    ret_abs = close.pct_change(1).abs()
    dv = _dollar_volume(close, volume).replace(0, np.nan)
    illiq = _safe_div(ret_abs, dv)
    return illiq.rolling(_TD_2YR, min_periods=_TD_YEAR).rank(pct=True)


def tnv_092_amihud_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of today's Amihud illiquidity vs 252-day distribution."""
    ret_abs = close.pct_change(1).abs()
    dv = _dollar_volume(close, volume).replace(0, np.nan)
    illiq = _safe_div(ret_abs, dv)
    m = illiq.rolling(_TD_YEAR, min_periods=_TD_QTR).mean()
    s = illiq.rolling(_TD_YEAR, min_periods=_TD_QTR).std()
    return _safe_div(illiq - m, s)


def tnv_093_amihud_expanding_pct_rank(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Expanding all-history pct rank of Amihud illiquidity."""
    ret_abs = close.pct_change(1).abs()
    dv = _dollar_volume(close, volume).replace(0, np.nan)
    illiq = _safe_div(ret_abs, dv)
    return illiq.expanding(min_periods=_TD_QTR).rank(pct=True)


def tnv_094_high_illiquidity_days_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days in trailing 252d where Amihud > 252d median (illiquid days)."""
    ret_abs = close.pct_change(1).abs()
    dv = _dollar_volume(close, volume).replace(0, np.nan)
    illiq = _safe_div(ret_abs, dv)
    med = _rolling_median(illiq, _TD_YEAR)
    flag = (illiq > med).astype(float)
    return flag.rolling(_TD_YEAR, min_periods=_TD_QTR).sum()


def tnv_095_amihud_mean_252d_vs_504d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 252d avg Amihud to 504d avg Amihud (recent vs long illiquidity)."""
    ret_abs = close.pct_change(1).abs()
    dv = _dollar_volume(close, volume).replace(0, np.nan)
    illiq = _safe_div(ret_abs, dv)
    return _safe_div(illiq.rolling(_TD_YEAR, min_periods=_TD_QTR).mean(),
                     illiq.rolling(_TD_2YR, min_periods=_TD_YEAR).mean())


# --- Group J (096-105): Turnover trend and regime change signals ---

def tnv_096_vol_252d_mean_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of 252-day rolling mean volume over trailing 63 days."""
    m = _rolling_mean(volume, _TD_YEAR)
    return _linslope(m, _TD_QTR)


def tnv_097_vol_504d_mean_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of 504-day rolling mean volume over trailing 63 days."""
    m = _rolling_mean(volume, _TD_2YR)
    return _linslope(m, _TD_QTR)


def tnv_098_vol_252d_mean_slope_126d(volume: pd.Series) -> pd.Series:
    """OLS slope of 252-day mean volume over trailing 126 days."""
    m = _rolling_mean(volume, _TD_YEAR)
    return _linslope(m, _TD_HALF)


def tnv_099_turnover_proxy_252d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of 252d-normalised turnover over 63 days."""
    tnv = _turnover_proxy(volume, _TD_YEAR)
    return _linslope(tnv, _TD_QTR)


def tnv_100_turnover_proxy_252d_slope_126d(volume: pd.Series) -> pd.Series:
    """OLS slope of 252d-normalised turnover over 126 days."""
    tnv = _turnover_proxy(volume, _TD_YEAR)
    return _linslope(tnv, _TD_HALF)


def tnv_101_vol_pct_rank_252d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of 252d pct-rank of volume over trailing 63 days."""
    rank = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return _linslope(rank, _TD_QTR)


def tnv_102_dvol_pct_rank_252d_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of 252d dollar-volume pct-rank over trailing 63 days."""
    dv = _dollar_volume(close, volume)
    rank = dv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return _linslope(rank, _TD_QTR)


def tnv_103_ewm_vol_126d_vs_252d_mean(volume: pd.Series) -> pd.Series:
    """EWM (span=126) of volume normalised by 252d mean (smoothed turnover)."""
    ewv = _ewm_mean(volume, _TD_HALF)
    return _safe_div(ewv, _rolling_mean(volume, _TD_YEAR))


def tnv_104_ewm_vol_63d_vs_252d_mean(volume: pd.Series) -> pd.Series:
    """EWM (span=63) of volume normalised by 252d mean."""
    ewv = _ewm_mean(volume, _TD_QTR)
    return _safe_div(ewv, _rolling_mean(volume, _TD_YEAR))


def tnv_105_ewm_vol_252d_vs_504d_mean(volume: pd.Series) -> pd.Series:
    """EWM (span=252) of volume normalised by 504d mean."""
    ewv = _ewm_mean(volume, _TD_YEAR)
    return _safe_div(ewv, _rolling_mean(volume, _TD_2YR))


# --- Group K (106-115): Multi-year extremes — how rare is today vs 3yr history ---

def tnv_106_vol_252d_pct_rank_vs_expanding_max(volume: pd.Series) -> pd.Series:
    """Trailing 252d mean as fraction of expanding all-time max mean (long decline)."""
    m = _rolling_mean(volume, _TD_YEAR)
    return _safe_div(m, m.expanding(min_periods=_TD_QTR).max())


def tnv_107_vol_expanding_zscore(volume: pd.Series) -> pd.Series:
    """Expanding z-score of today's volume (all-history extremity)."""
    m = volume.expanding(min_periods=_TD_QTR).mean()
    s = volume.expanding(min_periods=_TD_QTR).std()
    return _safe_div(volume - m, s)


def tnv_108_vol_new_3yr_high_flag(volume: pd.Series) -> pd.Series:
    """Flag: today's volume sets a new 3-year (756-day) rolling high."""
    pk = volume.shift(1).rolling(_TD_3YR, min_periods=_TD_2YR).max()
    return (volume > pk).astype(float)


def tnv_109_vol_new_2yr_high_flag(volume: pd.Series) -> pd.Series:
    """Flag: today's volume sets a new 2-year (504-day) rolling high."""
    pk = volume.shift(1).rolling(_TD_2YR, min_periods=_TD_YEAR).max()
    return (volume > pk).astype(float)


def tnv_110_vol_new_3yr_low_flag(volume: pd.Series) -> pd.Series:
    """Flag: today's volume sets a new 3-year (756-day) rolling low (illiquidity extreme)."""
    fl = volume.shift(1).rolling(_TD_3YR, min_periods=_TD_2YR).min()
    return (volume < fl).astype(float)


def tnv_111_vol_new_2yr_low_flag(volume: pd.Series) -> pd.Series:
    """Flag: today's volume sets a new 2-year (504-day) rolling low."""
    fl = volume.shift(1).rolling(_TD_2YR, min_periods=_TD_YEAR).min()
    return (volume < fl).astype(float)


def tnv_112_new_3yr_high_turnover_count_252d(volume: pd.Series) -> pd.Series:
    """Count of new-3yr-high-volume days in trailing 252 days."""
    pk = volume.shift(1).rolling(_TD_3YR, min_periods=_TD_2YR).max()
    flag = (volume > pk).astype(float)
    return flag.rolling(_TD_YEAR, min_periods=_TD_QTR).sum()


def tnv_113_new_2yr_low_turnover_count_252d(volume: pd.Series) -> pd.Series:
    """Count of new-2yr-low-volume days in trailing 252 days."""
    fl = volume.shift(1).rolling(_TD_2YR, min_periods=_TD_YEAR).min()
    flag = (volume < fl).astype(float)
    return flag.rolling(_TD_YEAR, min_periods=_TD_QTR).sum()


def tnv_114_vol_vs_3yr_min_ratio(volume: pd.Series) -> pd.Series:
    """Today's volume divided by trailing 3-year minimum (distance from illiquidity floor)."""
    fl = _rolling_min(volume, _TD_3YR)
    return _safe_div(volume, fl)


def tnv_115_vol_vs_3yr_max_ratio(volume: pd.Series) -> pd.Series:
    """Today's volume divided by trailing 3-year maximum."""
    pk = _rolling_max(volume, _TD_3YR)
    return _safe_div(volume, pk)


# --- Group L (116-125): Turnover in down vs up market regimes ---

def tnv_116_vol_on_down_days_252d_mean(close: pd.Series, volume: pd.Series) -> pd.Series:
    """252-day mean volume on down-price days (distressed turnover level)."""
    ret = close.pct_change(1)
    down_vol = volume.where(ret < 0, np.nan)
    return down_vol.rolling(_TD_YEAR, min_periods=_TD_QTR).mean()


def tnv_117_vol_on_up_days_252d_mean(close: pd.Series, volume: pd.Series) -> pd.Series:
    """252-day mean volume on up-price days."""
    ret = close.pct_change(1)
    up_vol = volume.where(ret > 0, np.nan)
    return up_vol.rolling(_TD_YEAR, min_periods=_TD_QTR).mean()


def tnv_118_down_vol_vs_up_vol_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 252d mean down-day volume to 252d mean up-day volume."""
    ret = close.pct_change(1)
    dn = volume.where(ret < 0, np.nan).rolling(_TD_YEAR, min_periods=_TD_QTR).mean()
    up = volume.where(ret > 0, np.nan).rolling(_TD_YEAR, min_periods=_TD_QTR).mean()
    return _safe_div(dn, up)


def tnv_119_down_vol_vs_up_vol_504d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 504d mean down-day volume to 504d mean up-day volume."""
    ret = close.pct_change(1)
    dn = volume.where(ret < 0, np.nan).rolling(_TD_2YR, min_periods=_TD_YEAR).mean()
    up = volume.where(ret > 0, np.nan).rolling(_TD_2YR, min_periods=_TD_YEAR).mean()
    return _safe_div(dn, up)


def tnv_120_down_dvol_vs_252d_baseline(close: pd.Series, volume: pd.Series) -> pd.Series:
    """252d mean dollar-volume on down days vs 252d mean all-day dollar-volume."""
    ret = close.pct_change(1)
    dv = _dollar_volume(close, volume)
    dn_dv = dv.where(ret < 0, np.nan).rolling(_TD_YEAR, min_periods=_TD_QTR).mean()
    all_dv = _rolling_mean(dv, _TD_YEAR)
    return _safe_div(dn_dv, all_dv)


def tnv_121_vol_on_down_days_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pct rank of today's volume (on down days) vs 252-day distribution of all volumes."""
    ret = close.pct_change(1)
    down_today = volume.where(ret < 0, np.nan)
    return down_today.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def tnv_122_vol_on_down_days_pct_rank_504d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pct rank of today's volume (on down days) vs 504-day distribution."""
    ret = close.pct_change(1)
    down_today = volume.where(ret < 0, np.nan)
    return down_today.rolling(_TD_2YR, min_periods=_TD_YEAR).rank(pct=True)


def tnv_123_turnover_down_vs_total_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 252-day cumulative volume that occurred on down-price days."""
    ret = close.pct_change(1)
    down_vol = volume.where(ret < 0, 0.0)
    cum_dn = _rolling_sum(down_vol, _TD_YEAR)
    cum_all = _rolling_sum(volume, _TD_YEAR)
    return _safe_div(cum_dn, cum_all)


def tnv_124_turnover_down_vs_total_504d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 504-day cumulative volume that occurred on down-price days."""
    ret = close.pct_change(1)
    down_vol = volume.where(ret < 0, 0.0)
    cum_dn = _rolling_sum(down_vol, _TD_2YR)
    cum_all = _rolling_sum(volume, _TD_2YR)
    return _safe_div(cum_dn, cum_all)


def tnv_125_vol_down_fraction_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pct rank of 252d down-volume fraction vs trailing 504d distribution."""
    ret = close.pct_change(1)
    down_vol = volume.where(ret < 0, 0.0)
    frac = _safe_div(_rolling_sum(down_vol, _TD_YEAR), _rolling_sum(volume, _TD_YEAR))
    return frac.rolling(_TD_2YR, min_periods=_TD_YEAR).rank(pct=True)


# --- Group M (126-135): Turnover distribution shape and skew ---

def tnv_126_vol_skew_252d(volume: pd.Series) -> pd.Series:
    """Skewness of volume distribution over trailing 252 days."""
    return volume.rolling(_TD_YEAR, min_periods=_TD_QTR).skew()


def tnv_127_vol_skew_504d(volume: pd.Series) -> pd.Series:
    """Skewness of volume distribution over trailing 504 days."""
    return volume.rolling(_TD_2YR, min_periods=_TD_YEAR).skew()


def tnv_128_vol_kurt_252d(volume: pd.Series) -> pd.Series:
    """Kurtosis of volume distribution over trailing 252 days (spike concentration)."""
    return volume.rolling(_TD_YEAR, min_periods=_TD_QTR).kurt()


def tnv_129_vol_kurt_504d(volume: pd.Series) -> pd.Series:
    """Kurtosis of volume distribution over trailing 504 days."""
    return volume.rolling(_TD_2YR, min_periods=_TD_YEAR).kurt()


def tnv_130_vol_iqr_252d(volume: pd.Series) -> pd.Series:
    """Interquartile range of volume over 252 days (spread of turnover distribution)."""
    q75 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.75)
    q25 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.25)
    return q75 - q25


def tnv_131_vol_iqr_vs_median_252d(volume: pd.Series) -> pd.Series:
    """IQR divided by median (robust coefficient of variation of turnover)."""
    q75 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.75)
    q25 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.25)
    med = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.5)
    return _safe_div(q75 - q25, med)


def tnv_132_vol_90th_pct_vs_median_252d(volume: pd.Series) -> pd.Series:
    """Ratio of 90th percentile to median volume over 252 days (tail heaviness)."""
    p90 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.9)
    med = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.5)
    return _safe_div(p90, med)


def tnv_133_vol_10th_pct_vs_median_252d(volume: pd.Series) -> pd.Series:
    """Ratio of 10th percentile to median volume over 252 days (illiquidity tail)."""
    p10 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.1)
    med = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.5)
    return _safe_div(p10, med)


def tnv_134_vol_above_90th_pct_252d_count(volume: pd.Series) -> pd.Series:
    """Count of days above 90th-pct volume threshold in trailing 252 days."""
    p90 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.9)
    flag = (volume > p90).astype(float)
    return flag.rolling(_TD_YEAR, min_periods=_TD_QTR).sum()


def tnv_135_vol_below_10th_pct_252d_count(volume: pd.Series) -> pd.Series:
    """Count of days below 10th-pct volume threshold in trailing 252 days."""
    p10 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.1)
    flag = (volume < p10).astype(float)
    return flag.rolling(_TD_YEAR, min_periods=_TD_QTR).sum()


# --- Group N (136-145): Composite and interaction features ---

def tnv_136_turnover_price_interaction_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Turnover proxy (252d) times log-price-level (low-price high-turn = panic)."""
    tnv = _safe_div(volume, _rolling_mean(volume, _TD_YEAR))
    log_px = _log_safe(close)
    log_px_norm = _safe_div(log_px, _rolling_mean(log_px, _TD_YEAR))
    return tnv * log_px_norm


def tnv_137_turnover_price_interaction_504d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Turnover proxy (504d) times normalised price level."""
    tnv = _safe_div(volume, _rolling_mean(volume, _TD_2YR))
    log_px = _log_safe(close)
    log_px_norm = _safe_div(log_px, _rolling_mean(log_px, _TD_2YR))
    return tnv * log_px_norm


def tnv_138_turnover_up_down_asymmetry_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Asymmetry: abs(down-vol fraction - 0.5) / up-vol fraction (252d)."""
    ret = close.pct_change(1)
    dn = volume.where(ret < 0, 0.0)
    up = volume.where(ret > 0, 0.0)
    dn_f = _safe_div(_rolling_sum(dn, _TD_YEAR), _rolling_sum(volume, _TD_YEAR))
    up_f = _safe_div(_rolling_sum(up, _TD_YEAR), _rolling_sum(volume, _TD_YEAR))
    return _safe_div((dn_f - 0.5).abs(), up_f)


def tnv_139_vol_autocorr_252d(volume: pd.Series) -> pd.Series:
    """Rolling 252-day lag-1 autocorrelation of volume (persistence of turnover)."""
    v1 = volume.shift(1)
    return volume.rolling(_TD_YEAR, min_periods=_TD_QTR).corr(v1)


def tnv_140_vol_autocorr_504d(volume: pd.Series) -> pd.Series:
    """Rolling 504-day lag-1 autocorrelation of volume."""
    v1 = volume.shift(1)
    return volume.rolling(_TD_2YR, min_periods=_TD_YEAR).corr(v1)


def tnv_141_turnover_vs_volatility_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """252d turnover proxy divided by 252d return volatility (turnover per unit risk)."""
    tnv = _safe_div(volume, _rolling_mean(volume, _TD_YEAR))
    vol_ret = close.pct_change(1).rolling(_TD_YEAR, min_periods=_TD_QTR).std()
    return _safe_div(tnv, vol_ret)


def tnv_142_turnover_vs_volatility_504d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """504d turnover proxy divided by 504d return volatility."""
    tnv = _safe_div(volume, _rolling_mean(volume, _TD_2YR))
    vol_ret = close.pct_change(1).rolling(_TD_2YR, min_periods=_TD_YEAR).std()
    return _safe_div(tnv, vol_ret)


def tnv_143_low_turnover_high_vol_flag_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: turnover in bottom quartile AND return volatility in top quartile (252d)."""
    tnv = _safe_div(volume, _rolling_mean(volume, _TD_YEAR))
    vol_ret = close.pct_change(1).rolling(_TD_YEAR, min_periods=_TD_QTR).std()
    tnv_low = tnv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True) <= 0.25
    vol_high = vol_ret.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True) >= 0.75
    return (tnv_low & vol_high).astype(float)


def tnv_144_dvol_vs_price_range_252d(close: pd.Series, high: pd.Series,
                                      low: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar-volume normalised by price range (high-low) as a liquidity depth proxy."""
    rng = (high - low).replace(0, np.nan)
    dv = _dollar_volume(close, volume)
    depth = _safe_div(dv, rng)
    return _safe_div(depth, _rolling_mean(depth, _TD_YEAR))


def tnv_145_dvol_vs_price_range_pct_rank_252d(close: pd.Series, high: pd.Series,
                                               low: pd.Series, volume: pd.Series) -> pd.Series:
    """Pct rank of dollar-volume/range depth proxy vs 252-day history."""
    rng = (high - low).replace(0, np.nan)
    dv = _dollar_volume(close, volume)
    depth = _safe_div(dv, rng)
    return depth.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group O (146-150): Final composite/summary signals ---

def tnv_146_composite_turnover_distress_score(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite: avg of 252d-pct-rank, 504d-pct-rank, and Amihud pct-rank (inverse)."""
    r252 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    r504 = volume.rolling(_TD_2YR, min_periods=_TD_YEAR).rank(pct=True)
    ret_abs = close.pct_change(1).abs()
    dv = _dollar_volume(close, volume).replace(0, np.nan)
    illiq = _safe_div(ret_abs, dv)
    r_ill = illiq.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return (r252 + r504 + (1.0 - r_ill)) / 3.0


def tnv_147_low_turnover_streak_504d(volume: pd.Series) -> pd.Series:
    """Consecutive days volume < 504d mean (illiquidity regime streak length)."""
    baseline = _rolling_mean(volume, _TD_2YR)
    cond = volume < baseline
    c = cond.astype(int)
    group = (~cond).cumsum()
    return c.groupby(group).cumsum().astype(float)


def tnv_148_turnover_regime_change_score(volume: pd.Series) -> pd.Series:
    """Abs change in 63d-vs-252d ratio over 63 days (regime shift in turnover)."""
    ratio = _safe_div(_rolling_mean(volume, _TD_QTR), _rolling_mean(volume, _TD_YEAR))
    return ratio.diff(_TD_QTR).abs()


def tnv_149_dvol_expanding_zscore(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Expanding all-history z-score of dollar-volume."""
    dv = _dollar_volume(close, volume)
    m = dv.expanding(min_periods=_TD_QTR).mean()
    s = dv.expanding(min_periods=_TD_QTR).std()
    return _safe_div(dv - m, s)


def tnv_150_composite_long_term_turnover_index(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite: geometric mean of 252d and 504d turnover proxies (long-term index)."""
    t252 = _safe_div(volume, _rolling_mean(volume, _TD_YEAR)).clip(lower=_EPS)
    t504 = _safe_div(volume, _rolling_mean(volume, _TD_2YR)).clip(lower=_EPS)
    return np.sqrt(t252 * t504)


# ── Registry ──────────────────────────────────────────────────────────────────

TURNOVER_RATIO_REGISTRY_076_150 = {
    "tnv_076_vol_per_unit_close_252d_norm": {"inputs": ["close", "volume"], "func": tnv_076_vol_per_unit_close_252d_norm},
    "tnv_077_vol_per_unit_close_504d_norm": {"inputs": ["close", "volume"], "func": tnv_077_vol_per_unit_close_504d_norm},
    "tnv_078_vol_per_unit_close_pct_rank_252d": {"inputs": ["close", "volume"], "func": tnv_078_vol_per_unit_close_pct_rank_252d},
    "tnv_079_vol_per_unit_close_pct_rank_504d": {"inputs": ["close", "volume"], "func": tnv_079_vol_per_unit_close_pct_rank_504d},
    "tnv_080_dvol_pct_rank_756d": {"inputs": ["close", "volume"], "func": tnv_080_dvol_pct_rank_756d},
    "tnv_081_dvol_expanding_pct_rank": {"inputs": ["close", "volume"], "func": tnv_081_dvol_expanding_pct_rank},
    "tnv_082_dvol_zscore_756d": {"inputs": ["close", "volume"], "func": tnv_082_dvol_zscore_756d},
    "tnv_083_log_dvol_vs_504d_mean": {"inputs": ["close", "volume"], "func": tnv_083_log_dvol_vs_504d_mean},
    "tnv_084_dvol_vs_cum_dvol_756d": {"inputs": ["close", "volume"], "func": tnv_084_dvol_vs_cum_dvol_756d},
    "tnv_085_dvol_mean_252d_vs_504d": {"inputs": ["close", "volume"], "func": tnv_085_dvol_mean_252d_vs_504d},
    "tnv_086_vol_times_close_pct_ret_252d_mean": {"inputs": ["close", "volume"], "func": tnv_086_vol_times_close_pct_ret_252d_mean},
    "tnv_087_vol_times_close_pct_ret_504d_mean": {"inputs": ["close", "volume"], "func": tnv_087_vol_times_close_pct_ret_504d_mean},
    "tnv_088_amihud_illiquidity_252d": {"inputs": ["close", "volume"], "func": tnv_088_amihud_illiquidity_252d},
    "tnv_089_amihud_illiquidity_504d": {"inputs": ["close", "volume"], "func": tnv_089_amihud_illiquidity_504d},
    "tnv_090_amihud_pct_rank_252d": {"inputs": ["close", "volume"], "func": tnv_090_amihud_pct_rank_252d},
    "tnv_091_amihud_pct_rank_504d": {"inputs": ["close", "volume"], "func": tnv_091_amihud_pct_rank_504d},
    "tnv_092_amihud_zscore_252d": {"inputs": ["close", "volume"], "func": tnv_092_amihud_zscore_252d},
    "tnv_093_amihud_expanding_pct_rank": {"inputs": ["close", "volume"], "func": tnv_093_amihud_expanding_pct_rank},
    "tnv_094_high_illiquidity_days_252d": {"inputs": ["close", "volume"], "func": tnv_094_high_illiquidity_days_252d},
    "tnv_095_amihud_mean_252d_vs_504d": {"inputs": ["close", "volume"], "func": tnv_095_amihud_mean_252d_vs_504d},
    "tnv_096_vol_252d_mean_slope_63d": {"inputs": ["volume"], "func": tnv_096_vol_252d_mean_slope_63d},
    "tnv_097_vol_504d_mean_slope_63d": {"inputs": ["volume"], "func": tnv_097_vol_504d_mean_slope_63d},
    "tnv_098_vol_252d_mean_slope_126d": {"inputs": ["volume"], "func": tnv_098_vol_252d_mean_slope_126d},
    "tnv_099_turnover_proxy_252d_slope_63d": {"inputs": ["volume"], "func": tnv_099_turnover_proxy_252d_slope_63d},
    "tnv_100_turnover_proxy_252d_slope_126d": {"inputs": ["volume"], "func": tnv_100_turnover_proxy_252d_slope_126d},
    "tnv_101_vol_pct_rank_252d_slope_63d": {"inputs": ["volume"], "func": tnv_101_vol_pct_rank_252d_slope_63d},
    "tnv_102_dvol_pct_rank_252d_slope_63d": {"inputs": ["close", "volume"], "func": tnv_102_dvol_pct_rank_252d_slope_63d},
    "tnv_103_ewm_vol_126d_vs_252d_mean": {"inputs": ["volume"], "func": tnv_103_ewm_vol_126d_vs_252d_mean},
    "tnv_104_ewm_vol_63d_vs_252d_mean": {"inputs": ["volume"], "func": tnv_104_ewm_vol_63d_vs_252d_mean},
    "tnv_105_ewm_vol_252d_vs_504d_mean": {"inputs": ["volume"], "func": tnv_105_ewm_vol_252d_vs_504d_mean},
    "tnv_106_vol_252d_pct_rank_vs_expanding_max": {"inputs": ["volume"], "func": tnv_106_vol_252d_pct_rank_vs_expanding_max},
    "tnv_107_vol_expanding_zscore": {"inputs": ["volume"], "func": tnv_107_vol_expanding_zscore},
    "tnv_108_vol_new_3yr_high_flag": {"inputs": ["volume"], "func": tnv_108_vol_new_3yr_high_flag},
    "tnv_109_vol_new_2yr_high_flag": {"inputs": ["volume"], "func": tnv_109_vol_new_2yr_high_flag},
    "tnv_110_vol_new_3yr_low_flag": {"inputs": ["volume"], "func": tnv_110_vol_new_3yr_low_flag},
    "tnv_111_vol_new_2yr_low_flag": {"inputs": ["volume"], "func": tnv_111_vol_new_2yr_low_flag},
    "tnv_112_new_3yr_high_turnover_count_252d": {"inputs": ["volume"], "func": tnv_112_new_3yr_high_turnover_count_252d},
    "tnv_113_new_2yr_low_turnover_count_252d": {"inputs": ["volume"], "func": tnv_113_new_2yr_low_turnover_count_252d},
    "tnv_114_vol_vs_3yr_min_ratio": {"inputs": ["volume"], "func": tnv_114_vol_vs_3yr_min_ratio},
    "tnv_115_vol_vs_3yr_max_ratio": {"inputs": ["volume"], "func": tnv_115_vol_vs_3yr_max_ratio},
    "tnv_116_vol_on_down_days_252d_mean": {"inputs": ["close", "volume"], "func": tnv_116_vol_on_down_days_252d_mean},
    "tnv_117_vol_on_up_days_252d_mean": {"inputs": ["close", "volume"], "func": tnv_117_vol_on_up_days_252d_mean},
    "tnv_118_down_vol_vs_up_vol_252d": {"inputs": ["close", "volume"], "func": tnv_118_down_vol_vs_up_vol_252d},
    "tnv_119_down_vol_vs_up_vol_504d": {"inputs": ["close", "volume"], "func": tnv_119_down_vol_vs_up_vol_504d},
    "tnv_120_down_dvol_vs_252d_baseline": {"inputs": ["close", "volume"], "func": tnv_120_down_dvol_vs_252d_baseline},
    "tnv_121_vol_on_down_days_pct_rank_252d": {"inputs": ["close", "volume"], "func": tnv_121_vol_on_down_days_pct_rank_252d},
    "tnv_122_vol_on_down_days_pct_rank_504d": {"inputs": ["close", "volume"], "func": tnv_122_vol_on_down_days_pct_rank_504d},
    "tnv_123_turnover_down_vs_total_252d": {"inputs": ["close", "volume"], "func": tnv_123_turnover_down_vs_total_252d},
    "tnv_124_turnover_down_vs_total_504d": {"inputs": ["close", "volume"], "func": tnv_124_turnover_down_vs_total_504d},
    "tnv_125_vol_down_fraction_pct_rank_252d": {"inputs": ["close", "volume"], "func": tnv_125_vol_down_fraction_pct_rank_252d},
    "tnv_126_vol_skew_252d": {"inputs": ["volume"], "func": tnv_126_vol_skew_252d},
    "tnv_127_vol_skew_504d": {"inputs": ["volume"], "func": tnv_127_vol_skew_504d},
    "tnv_128_vol_kurt_252d": {"inputs": ["volume"], "func": tnv_128_vol_kurt_252d},
    "tnv_129_vol_kurt_504d": {"inputs": ["volume"], "func": tnv_129_vol_kurt_504d},
    "tnv_130_vol_iqr_252d": {"inputs": ["volume"], "func": tnv_130_vol_iqr_252d},
    "tnv_131_vol_iqr_vs_median_252d": {"inputs": ["volume"], "func": tnv_131_vol_iqr_vs_median_252d},
    "tnv_132_vol_90th_pct_vs_median_252d": {"inputs": ["volume"], "func": tnv_132_vol_90th_pct_vs_median_252d},
    "tnv_133_vol_10th_pct_vs_median_252d": {"inputs": ["volume"], "func": tnv_133_vol_10th_pct_vs_median_252d},
    "tnv_134_vol_above_90th_pct_252d_count": {"inputs": ["volume"], "func": tnv_134_vol_above_90th_pct_252d_count},
    "tnv_135_vol_below_10th_pct_252d_count": {"inputs": ["volume"], "func": tnv_135_vol_below_10th_pct_252d_count},
    "tnv_136_turnover_price_interaction_252d": {"inputs": ["close", "volume"], "func": tnv_136_turnover_price_interaction_252d},
    "tnv_137_turnover_price_interaction_504d": {"inputs": ["close", "volume"], "func": tnv_137_turnover_price_interaction_504d},
    "tnv_138_turnover_up_down_asymmetry_252d": {"inputs": ["close", "volume"], "func": tnv_138_turnover_up_down_asymmetry_252d},
    "tnv_139_vol_autocorr_252d": {"inputs": ["volume"], "func": tnv_139_vol_autocorr_252d},
    "tnv_140_vol_autocorr_504d": {"inputs": ["volume"], "func": tnv_140_vol_autocorr_504d},
    "tnv_141_turnover_vs_volatility_252d": {"inputs": ["close", "volume"], "func": tnv_141_turnover_vs_volatility_252d},
    "tnv_142_turnover_vs_volatility_504d": {"inputs": ["close", "volume"], "func": tnv_142_turnover_vs_volatility_504d},
    "tnv_143_low_turnover_high_vol_flag_252d": {"inputs": ["close", "volume"], "func": tnv_143_low_turnover_high_vol_flag_252d},
    "tnv_144_dvol_vs_price_range_252d": {"inputs": ["close", "high", "low", "volume"], "func": tnv_144_dvol_vs_price_range_252d},
    "tnv_145_dvol_vs_price_range_pct_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": tnv_145_dvol_vs_price_range_pct_rank_252d},
    "tnv_146_composite_turnover_distress_score": {"inputs": ["close", "volume"], "func": tnv_146_composite_turnover_distress_score},
    "tnv_147_low_turnover_streak_504d": {"inputs": ["volume"], "func": tnv_147_low_turnover_streak_504d},
    "tnv_148_turnover_regime_change_score": {"inputs": ["volume"], "func": tnv_148_turnover_regime_change_score},
    "tnv_149_dvol_expanding_zscore": {"inputs": ["close", "volume"], "func": tnv_149_dvol_expanding_zscore},
    "tnv_150_composite_long_term_turnover_index": {"inputs": ["close", "volume"], "func": tnv_150_composite_long_term_turnover_index},
}
