"""
22_volume_price_divergence — Base Features 001-075
Domain: volume rising while price falls — correlation/covariance of volume vs price,
signed interaction terms (down-return x volume), divergence flags (new low + rising vol),
regression of volume on price, count of falling-price + rising-volume days,
volume-weighted price decline metrics.
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


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    """Count of True values in trailing w periods."""
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


def _log_ret(s: pd.Series) -> pd.Series:
    return _log_safe(s) - _log_safe(s.shift(1))


def _rolling_corr(x: pd.Series, y: pd.Series, w: int) -> pd.Series:
    """Rolling Pearson correlation between x and y."""
    return x.rolling(w, min_periods=max(2, w // 2)).corr(y)


def _rolling_cov(x: pd.Series, y: pd.Series, w: int) -> pd.Series:
    """Rolling covariance between x and y."""
    return x.rolling(w, min_periods=max(2, w // 2)).cov(y)


def _vol_chg(volume: pd.Series) -> pd.Series:
    """Day-over-day volume change (raw difference)."""
    return volume.diff(1)


def _vol_ret(volume: pd.Series) -> pd.Series:
    """Day-over-day volume percent change."""
    return volume.pct_change(1)


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


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): Rolling correlation of volume vs price/returns ---

def vpd_001_corr_vol_close_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 21-day Pearson correlation between volume and close price."""
    return _rolling_corr(volume, close, _TD_MON)


def vpd_002_corr_vol_close_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63-day Pearson correlation between volume and close price."""
    return _rolling_corr(volume, close, _TD_QTR)


def vpd_003_corr_vol_close_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 126-day Pearson correlation between volume and close price."""
    return _rolling_corr(volume, close, _TD_HALF)


def vpd_004_corr_vol_close_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 252-day Pearson correlation between volume and close price."""
    return _rolling_corr(volume, close, _TD_YEAR)


def vpd_005_corr_vol_ret_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 5-day correlation between volume and daily return."""
    ret = _daily_ret(close)
    return _rolling_corr(volume, ret, _TD_WEEK)


def vpd_006_corr_vol_ret_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 21-day correlation between volume and daily return."""
    ret = _daily_ret(close)
    return _rolling_corr(volume, ret, _TD_MON)


def vpd_007_corr_vol_ret_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63-day correlation between volume and daily return."""
    ret = _daily_ret(close)
    return _rolling_corr(volume, ret, _TD_QTR)


def vpd_008_corr_vol_ret_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 252-day correlation between volume and daily return."""
    ret = _daily_ret(close)
    return _rolling_corr(volume, ret, _TD_YEAR)


def vpd_009_corr_vol_logret_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 21-day correlation between volume and log return."""
    lret = _log_ret(close)
    return _rolling_corr(volume, lret, _TD_MON)


def vpd_010_corr_vol_logret_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63-day correlation between volume and log return."""
    lret = _log_ret(close)
    return _rolling_corr(volume, lret, _TD_QTR)


def vpd_011_corr_volchg_ret_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 21-day correlation between volume change and daily return."""
    vchg = _vol_ret(volume)
    ret = _daily_ret(close)
    return _rolling_corr(vchg, ret, _TD_MON)


def vpd_012_corr_volchg_ret_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63-day correlation between volume change and daily return."""
    vchg = _vol_ret(volume)
    ret = _daily_ret(close)
    return _rolling_corr(vchg, ret, _TD_QTR)


def vpd_013_corr_volchg_ret_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 126-day correlation between volume pct-change and daily return."""
    vchg = _vol_ret(volume)
    ret = _daily_ret(close)
    return _rolling_corr(vchg, ret, _TD_HALF)


def vpd_014_corr_vol_low_21d(close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 21-day correlation between volume and intraday low (low = distress proxy)."""
    return _rolling_corr(volume, low, _TD_MON)


def vpd_015_corr_vol_low_63d(close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63-day correlation between volume and intraday low."""
    return _rolling_corr(volume, low, _TD_QTR)


# --- Group B (016-030): Covariance-based volume-price divergence ---

def vpd_016_cov_vol_ret_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 21-day covariance between volume and daily return."""
    ret = _daily_ret(close)
    return _rolling_cov(volume, ret, _TD_MON)


def vpd_017_cov_vol_ret_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63-day covariance between volume and daily return."""
    ret = _daily_ret(close)
    return _rolling_cov(volume, ret, _TD_QTR)


def vpd_018_cov_vol_ret_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 252-day covariance between volume and daily return."""
    ret = _daily_ret(close)
    return _rolling_cov(volume, ret, _TD_YEAR)


def vpd_019_cov_volchg_ret_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 21-day covariance between volume pct-change and daily return."""
    vchg = _vol_ret(volume)
    ret = _daily_ret(close)
    return _rolling_cov(vchg, ret, _TD_MON)


def vpd_020_cov_volchg_ret_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63-day covariance between volume pct-change and daily return."""
    vchg = _vol_ret(volume)
    ret = _daily_ret(close)
    return _rolling_cov(vchg, ret, _TD_QTR)


def vpd_021_cov_vol_logret_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 21-day covariance between volume and log return."""
    lret = _log_ret(close)
    return _rolling_cov(volume, lret, _TD_MON)


def vpd_022_cov_vol_logret_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63-day covariance between volume and log return."""
    lret = _log_ret(close)
    return _rolling_cov(volume, lret, _TD_QTR)


def vpd_023_neg_corr_vol_ret_flag_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: 21-day corr(volume, return) < 0 (volume-price divergence regime)."""
    corr = vpd_006_corr_vol_ret_21d(close, volume)
    return (corr < 0).astype(float)


def vpd_024_neg_corr_vol_ret_flag_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: 63-day corr(volume, return) < 0 (sustained divergence)."""
    corr = vpd_007_corr_vol_ret_63d(close, volume)
    return (corr < 0).astype(float)


def vpd_025_corr_vol_ret_21d_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day corr(vol, ret) within trailing 252-day distribution."""
    corr = vpd_006_corr_vol_ret_21d(close, volume)
    return corr.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vpd_026_corr_vol_ret_63d_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 63-day corr(vol, ret) within trailing 252-day distribution."""
    corr = vpd_007_corr_vol_ret_63d(close, volume)
    return corr.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vpd_027_corr_vol_close_21d_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 21-day vol-close correlation relative to 252-day distribution."""
    corr = vpd_001_corr_vol_close_21d(close, volume)
    m = _rolling_mean(corr, _TD_YEAR)
    s = _rolling_std(corr, _TD_YEAR)
    return _safe_div(corr - m, s)


def vpd_028_cov_vol_ret_21d_norm_by_vol_std(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day cov(vol, ret) normalized by rolling volume std (scale-free divergence)."""
    ret = _daily_ret(close)
    cov = _rolling_cov(volume, ret, _TD_MON)
    vstd = _rolling_std(volume, _TD_MON)
    return _safe_div(cov, vstd)


def vpd_029_cov_vol_ret_63d_norm_by_vol_std(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day cov(vol, ret) normalized by rolling volume std."""
    ret = _daily_ret(close)
    cov = _rolling_cov(volume, ret, _TD_QTR)
    vstd = _rolling_std(volume, _TD_QTR)
    return _safe_div(cov, vstd)


def vpd_030_corr_vol_ret_ewm21_vs_ewm63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Difference between EWM-21 and EWM-63 of daily vol*ret product (divergence speed)."""
    ret = _daily_ret(close)
    prod = volume * ret
    fast = _ewm_mean(prod, _TD_MON)
    slow = _ewm_mean(prod, _TD_QTR)
    return fast - slow


# --- Group C (031-045): Signed interaction: down-return × volume ---

def vpd_031_down_ret_x_vol_raw_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (return * volume) on down days over 21 days (negative = large down-vol)."""
    ret = _daily_ret(close)
    interaction = ret.where(ret < 0, 0.0) * volume
    return _rolling_sum(interaction, _TD_MON)


def vpd_032_down_ret_x_vol_raw_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (return * volume) on down days over 63 days."""
    ret = _daily_ret(close)
    interaction = ret.where(ret < 0, 0.0) * volume
    return _rolling_sum(interaction, _TD_QTR)


def vpd_033_down_ret_x_vol_raw_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (return * volume) on down days over 252 days."""
    ret = _daily_ret(close)
    interaction = ret.where(ret < 0, 0.0) * volume
    return _rolling_sum(interaction, _TD_YEAR)


def vpd_034_down_ret_x_volnorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (return * vol_norm) on down days, 21-day window."""
    ret = _daily_ret(close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    interaction = ret.where(ret < 0, 0.0) * vol_norm
    return _rolling_sum(interaction, _TD_MON)


def vpd_035_down_ret_x_volnorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (return * vol_norm) on down days, 63-day window."""
    ret = _daily_ret(close)
    avg_vol = _rolling_mean(volume, _TD_QTR)
    vol_norm = _safe_div(volume, avg_vol)
    interaction = ret.where(ret < 0, 0.0) * vol_norm
    return _rolling_sum(interaction, _TD_QTR)


def vpd_036_down_ret_x_volnorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (return * vol_norm) on down days, 252-day window."""
    ret = _daily_ret(close)
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    vol_norm = _safe_div(volume, avg_vol)
    interaction = ret.where(ret < 0, 0.0) * vol_norm
    return _rolling_sum(interaction, _TD_YEAR)


def vpd_037_down_logret_x_vol_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (log_return * volume) on down days over 21 days."""
    lret = _log_ret(close)
    interaction = lret.where(lret < 0, 0.0) * volume
    return _rolling_sum(interaction, _TD_MON)


def vpd_038_down_logret_x_vol_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (log_return * volume) on down days over 63 days."""
    lret = _log_ret(close)
    interaction = lret.where(lret < 0, 0.0) * volume
    return _rolling_sum(interaction, _TD_QTR)


def vpd_039_avg_down_ret_x_volnorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average (return * vol_norm) on down days over 21 days."""
    ret = _daily_ret(close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    interaction = (ret * vol_norm).where(ret < 0, np.nan)
    return interaction.rolling(_TD_MON, min_periods=1).mean()


def vpd_040_avg_down_ret_x_volnorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average (return * vol_norm) on down days over 63 days."""
    ret = _daily_ret(close)
    avg_vol = _rolling_mean(volume, _TD_QTR)
    vol_norm = _safe_div(volume, avg_vol)
    interaction = (ret * vol_norm).where(ret < 0, np.nan)
    return interaction.rolling(_TD_QTR, min_periods=1).mean()


def vpd_041_down_ret_x_vol_minus_up_ret_x_vol_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Signed imbalance: sum(down_ret*vol) minus sum(up_ret*vol) over 21 days."""
    ret = _daily_ret(close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    down_int = _rolling_sum((ret * vol_norm).where(ret < 0, 0.0), _TD_MON)
    up_int = _rolling_sum((ret * vol_norm).where(ret > 0, 0.0), _TD_MON)
    return down_int - up_int


def vpd_042_down_ret_x_vol_minus_up_ret_x_vol_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Signed imbalance: sum(down_ret*vol) minus sum(up_ret*vol) over 63 days."""
    ret = _daily_ret(close)
    avg_vol = _rolling_mean(volume, _TD_QTR)
    vol_norm = _safe_div(volume, avg_vol)
    down_int = _rolling_sum((ret * vol_norm).where(ret < 0, 0.0), _TD_QTR)
    up_int = _rolling_sum((ret * vol_norm).where(ret > 0, 0.0), _TD_QTR)
    return down_int - up_int


def vpd_043_down_ret_x_vol_21d_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pct rank of 21-day signed down-vol interaction in 252-day history."""
    feat = vpd_031_down_ret_x_vol_raw_21d(close, volume)
    return feat.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vpd_044_down_ret_x_vol_63d_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pct rank of 63-day signed down-vol interaction in 252-day history."""
    feat = vpd_032_down_ret_x_vol_raw_63d(close, volume)
    return feat.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vpd_045_ewm_down_ret_x_vol_21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """EWM-21 of daily (down_ret * vol_norm) interaction (fast-decaying signal)."""
    ret = _daily_ret(close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    interaction = (ret * vol_norm).where(ret < 0, 0.0)
    return _ewm_mean(interaction, _TD_MON)


# --- Group D (046-060): Divergence flags (price new-low + volume rising) ---

def vpd_046_newlow21_vol_rising_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: close makes 21-day low AND volume above 21-day avg (classic divergence)."""
    roll_min = close.shift(1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min()
    avg_vol = _rolling_mean(volume, _TD_MON)
    return ((close < roll_min) & (volume > avg_vol)).astype(float)


def vpd_047_newlow63_vol_rising_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: close makes 63-day low AND volume above 21-day avg."""
    roll_min = close.shift(1).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    avg_vol = _rolling_mean(volume, _TD_MON)
    return ((close < roll_min) & (volume > avg_vol)).astype(float)


def vpd_048_newlow252_vol_rising_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: close makes 252-day low AND volume above 21-day avg."""
    roll_min = close.shift(1).rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).min()
    avg_vol = _rolling_mean(volume, _TD_MON)
    return ((close < roll_min) & (volume > avg_vol)).astype(float)


def vpd_049_newlow21_vol_rising_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of 21-day-new-low + high-volume days in trailing 63 days."""
    flag = vpd_046_newlow21_vol_rising_flag(close, volume)
    return _rolling_sum(flag, _TD_QTR)


def vpd_050_newlow63_vol_rising_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of 63-day-new-low + high-volume days in trailing 252 days."""
    flag = vpd_047_newlow63_vol_rising_flag(close, volume)
    return _rolling_sum(flag, _TD_YEAR)


def vpd_051_price_down_vol_up_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: close < prior close AND volume > prior volume (basic daily divergence)."""
    return ((close < close.shift(1)) & (volume > volume.shift(1))).astype(float)


def vpd_052_price_down_vol_up_count_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of price-down + volume-up days in trailing 21 days."""
    flag = vpd_051_price_down_vol_up_flag(close, volume)
    return _rolling_sum(flag, _TD_MON)


def vpd_053_price_down_vol_up_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of price-down + volume-up days in trailing 63 days."""
    flag = vpd_051_price_down_vol_up_flag(close, volume)
    return _rolling_sum(flag, _TD_QTR)


def vpd_054_price_down_vol_up_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of price-down + volume-up days in trailing 252 days."""
    flag = vpd_051_price_down_vol_up_flag(close, volume)
    return _rolling_sum(flag, _TD_YEAR)


def vpd_055_price_down_vol_up_frac_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 21 days with price-down + volume-up divergence."""
    return vpd_052_price_down_vol_up_count_21d(close, volume) / _TD_MON


def vpd_056_price_down_vol_up_frac_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 63 days with price-down + volume-up divergence."""
    return vpd_053_price_down_vol_up_count_63d(close, volume) / _TD_QTR


def vpd_057_price_down_vol_up_frac_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 252 days with price-down + volume-up divergence."""
    return vpd_054_price_down_vol_up_count_252d(close, volume) / _TD_YEAR


def vpd_058_price_dn_vol_up_vs_price_dn_vol_dn_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of divergence days (price down & vol up) to non-divergence down days, 21d."""
    ret = _daily_ret(close)
    div_cnt = _rolling_count_true((ret < 0) & (volume > volume.shift(1)), _TD_MON)
    non_div_cnt = _rolling_count_true((ret < 0) & (volume <= volume.shift(1)), _TD_MON)
    return _safe_div(div_cnt, non_div_cnt)


def vpd_059_price_dn_vol_up_vs_price_dn_vol_dn_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of divergence days to non-divergence down days, 63-day window."""
    ret = _daily_ret(close)
    div_cnt = _rolling_count_true((ret < 0) & (volume > volume.shift(1)), _TD_QTR)
    non_div_cnt = _rolling_count_true((ret < 0) & (volume <= volume.shift(1)), _TD_QTR)
    return _safe_div(div_cnt, non_div_cnt)


def vpd_060_newlow_vol_surge_intensity_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg vol-to-avg ratio on 21-day-new-low days over trailing 63 days."""
    roll_min = close.shift(1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min()
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    is_newlow = (close < roll_min).astype(float)
    vol_on_newlow = vol_norm.where(is_newlow.astype(bool), np.nan)
    return vol_on_newlow.rolling(_TD_QTR, min_periods=1).mean()


# --- Group E (061-075): Regression of volume on price / returns ---

def vpd_061_vol_price_beta_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS beta of volume regressed on close price over 21-day window."""
    cov = _rolling_cov(volume, close, _TD_MON)
    var_p = _rolling_std(close, _TD_MON) ** 2
    return _safe_div(cov, var_p)


def vpd_062_vol_price_beta_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS beta of volume regressed on close price over 63-day window."""
    cov = _rolling_cov(volume, close, _TD_QTR)
    var_p = _rolling_std(close, _TD_QTR) ** 2
    return _safe_div(cov, var_p)


def vpd_063_vol_ret_beta_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS beta of volume regressed on daily return over 21 days."""
    ret = _daily_ret(close)
    cov = _rolling_cov(volume, ret, _TD_MON)
    var_r = _rolling_std(ret, _TD_MON) ** 2
    return _safe_div(cov, var_r)


def vpd_064_vol_ret_beta_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS beta of volume regressed on daily return over 63 days."""
    ret = _daily_ret(close)
    cov = _rolling_cov(volume, ret, _TD_QTR)
    var_r = _rolling_std(ret, _TD_QTR) ** 2
    return _safe_div(cov, var_r)


def vpd_065_vol_ret_beta_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS beta of volume regressed on daily return over 252 days."""
    ret = _daily_ret(close)
    cov = _rolling_cov(volume, ret, _TD_YEAR)
    var_r = _rolling_std(ret, _TD_YEAR) ** 2
    return _safe_div(cov, var_r)


def vpd_066_volnorm_price_beta_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS beta of normalized volume on close price, 21-day window."""
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    cov = _rolling_cov(vol_norm, close, _TD_MON)
    var_p = _rolling_std(close, _TD_MON) ** 2
    return _safe_div(cov, var_p)


def vpd_067_volnorm_ret_beta_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS beta of normalized volume on daily return, 21-day window."""
    ret = _daily_ret(close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    cov = _rolling_cov(vol_norm, ret, _TD_MON)
    var_r = _rolling_std(ret, _TD_MON) ** 2
    return _safe_div(cov, var_r)


def vpd_068_volnorm_ret_beta_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS beta of normalized volume on daily return, 63-day window."""
    ret = _daily_ret(close)
    avg_vol = _rolling_mean(volume, _TD_QTR)
    vol_norm = _safe_div(volume, avg_vol)
    cov = _rolling_cov(vol_norm, ret, _TD_QTR)
    var_r = _rolling_std(ret, _TD_QTR) ** 2
    return _safe_div(cov, var_r)


def vpd_069_vol_ret_beta_21d_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pct rank of 21-day vol-return beta in 252-day history."""
    beta = vpd_063_vol_ret_beta_21d(close, volume)
    return beta.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vpd_070_vol_ret_beta_63d_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 63-day vol-return beta relative to 252-day distribution."""
    beta = vpd_064_vol_ret_beta_63d(close, volume)
    m = _rolling_mean(beta, _TD_YEAR)
    s = _rolling_std(beta, _TD_YEAR)
    return _safe_div(beta - m, s)


def vpd_071_vol_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of volume over 21-day window (rising = capitulation candidate)."""
    return _linslope(volume, _TD_MON)


def vpd_072_vol_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of volume over 63-day window."""
    return _linslope(volume, _TD_QTR)


def vpd_073_price_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of close price over 21-day window (falling = distress)."""
    return _linslope(close, _TD_MON)


def vpd_074_vol_slope_minus_price_slope_norm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Normalized vol slope minus normalized price slope over 21 days (divergence)."""
    vol_slope = _linslope(volume, _TD_MON)
    price_slope = _linslope(close, _TD_MON)
    vol_std = _rolling_std(volume, _TD_MON).clip(lower=_EPS)
    price_std = _rolling_std(close, _TD_MON).clip(lower=_EPS)
    return _safe_div(vol_slope, vol_std) - _safe_div(price_slope, price_std)


def vpd_075_vol_slope_minus_price_slope_norm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Normalized vol slope minus normalized price slope over 63 days (divergence)."""
    vol_slope = _linslope(volume, _TD_QTR)
    price_slope = _linslope(close, _TD_QTR)
    vol_std = _rolling_std(volume, _TD_QTR).clip(lower=_EPS)
    price_std = _rolling_std(close, _TD_QTR).clip(lower=_EPS)
    return _safe_div(vol_slope, vol_std) - _safe_div(price_slope, price_std)


# --- Group F-ext (151-175): New base features ---

def vpd_151_corr_vol_high_21d(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 21-day correlation between volume and intraday high (supply-side distress)."""
    return _rolling_corr(volume, high, _TD_MON)


def vpd_152_corr_vol_high_63d(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63-day correlation between volume and intraday high."""
    return _rolling_corr(volume, high, _TD_QTR)


def vpd_153_down_open_to_close_x_vol_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (open-to-close decline * volume) on days close < open, 21-day window."""
    oc_ret = (close - open) / open.replace(0, np.nan)
    interaction = oc_ret.where(oc_ret < 0, 0.0) * volume
    return _rolling_sum(interaction, _TD_MON)


def vpd_154_down_open_to_close_x_vol_63d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (open-to-close decline * volume) on down days, 63-day window."""
    oc_ret = (close - open) / open.replace(0, np.nan)
    interaction = oc_ret.where(oc_ret < 0, 0.0) * volume
    return _rolling_sum(interaction, _TD_QTR)


def vpd_155_vol_weighted_open_close_decline_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol-weighted avg open-to-close return over 21 days (negative = distribution)."""
    oc_ret = (close - open) / open.replace(0, np.nan)
    num = _rolling_sum(oc_ret * volume, _TD_MON)
    den = _rolling_sum(volume, _TD_MON)
    return _safe_div(num, den)


def vpd_156_vol_weighted_open_close_decline_63d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol-weighted avg open-to-close return over 63 days."""
    oc_ret = (close - open) / open.replace(0, np.nan)
    num = _rolling_sum(oc_ret * volume, _TD_QTR)
    den = _rolling_sum(volume, _TD_QTR)
    return _safe_div(num, den)


def vpd_157_corr_vol_open_close_range_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 21-day correlation between volume and abs(close-open) range."""
    rng = (close - open).abs()
    return _rolling_corr(volume, rng, _TD_MON)


def vpd_158_corr_vol_open_close_range_63d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63-day correlation between volume and abs(close-open) range."""
    rng = (close - open).abs()
    return _rolling_corr(volume, rng, _TD_QTR)


def vpd_159_high_low_range_x_vol_down_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (high-low range * vol_norm) on down-close days over 21 days."""
    ret = _daily_ret(close)
    rng = high - low
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    interaction = (rng * vol_norm).where(ret < 0, 0.0)
    return _rolling_sum(interaction, _TD_MON)


def vpd_160_high_low_range_x_vol_down_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (high-low range * vol_norm) on down-close days over 63 days."""
    ret = _daily_ret(close)
    rng = high - low
    avg_vol = _rolling_mean(volume, _TD_QTR)
    vol_norm = _safe_div(volume, avg_vol)
    interaction = (rng * vol_norm).where(ret < 0, 0.0)
    return _rolling_sum(interaction, _TD_QTR)


def vpd_161_newlow63_vol_surge_2x_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: 63-day new low AND volume > 2x 21-day avg (extreme divergence signal)."""
    roll_min = close.shift(1).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    avg_vol = _rolling_mean(volume, _TD_MON)
    return ((close < roll_min) & (volume > 2.0 * avg_vol)).astype(float)


def vpd_162_newlow252_vol_surge_2x_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: 252-day new low AND volume > 2x 21-day avg (capitulation extreme)."""
    roll_min = close.shift(1).rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).min()
    avg_vol = _rolling_mean(volume, _TD_MON)
    return ((close < roll_min) & (volume > 2.0 * avg_vol)).astype(float)


def vpd_163_newlow63_vol_surge_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of (63-day new low + vol > 2x avg) events in trailing 252 days."""
    flag = vpd_161_newlow63_vol_surge_2x_flag(close, volume)
    return _rolling_sum(flag, _TD_YEAR)


def vpd_164_down_ret_logvol_interaction_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (down_ret * log(volume)) on down days over 21 days."""
    ret = _daily_ret(close)
    logvol = _log_safe(volume)
    interaction = (ret * logvol).where(ret < 0, 0.0)
    return _rolling_sum(interaction, _TD_MON)


def vpd_165_down_ret_logvol_interaction_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (down_ret * log(volume)) on down days over 63 days."""
    ret = _daily_ret(close)
    logvol = _log_safe(volume)
    interaction = (ret * logvol).where(ret < 0, 0.0)
    return _rolling_sum(interaction, _TD_QTR)


def vpd_166_corr_logvol_ret_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 21-day correlation between log(volume) and daily return."""
    logvol = _log_safe(volume)
    ret = _daily_ret(close)
    return _rolling_corr(logvol, ret, _TD_MON)


def vpd_167_corr_logvol_ret_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63-day correlation between log(volume) and daily return."""
    logvol = _log_safe(volume)
    ret = _daily_ret(close)
    return _rolling_corr(logvol, ret, _TD_QTR)


def vpd_168_vol_ret_beta_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS beta of volume regressed on daily return over 126-day window."""
    ret = _daily_ret(close)
    cov = _rolling_cov(volume, ret, _TD_HALF)
    var_r = _rolling_std(ret, _TD_HALF) ** 2
    return _safe_div(cov, var_r)


def vpd_169_vol_price_beta_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS beta of volume regressed on close price over 126-day window."""
    cov = _rolling_cov(volume, close, _TD_HALF)
    var_p = _rolling_std(close, _TD_HALF) ** 2
    return _safe_div(cov, var_p)


def vpd_170_down_ret_x_vol_raw_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (return * volume) on down days over 126-day window."""
    ret = _daily_ret(close)
    interaction = ret.where(ret < 0, 0.0) * volume
    return _rolling_sum(interaction, _TD_HALF)


def vpd_171_vol_on_down_days_vs_total_vol_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 126-day total volume occurring on down-price days."""
    ret = _daily_ret(close)
    down_vol = _rolling_sum(volume.where(ret < 0, 0.0), _TD_HALF)
    total_vol = _rolling_sum(volume, _TD_HALF)
    return _safe_div(down_vol, total_vol)


def vpd_172_corr_vol_ret_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 126-day Pearson correlation between volume and daily return."""
    ret = _daily_ret(close)
    return _rolling_corr(volume, ret, _TD_HALF)


def vpd_173_vol_slope_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of volume over 126-day window."""
    return _linslope(volume, _TD_HALF)


def vpd_174_price_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of close price over 63-day window (medium-term price trend)."""
    return _linslope(close, _TD_QTR)


def vpd_175_vol_slope_minus_price_slope_norm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Normalized vol slope minus normalized price slope over 126 days (divergence)."""
    vol_slope = _linslope(volume, _TD_HALF)
    price_slope = _linslope(close, _TD_HALF)
    vol_std = _rolling_std(volume, _TD_HALF).clip(lower=_EPS)
    price_std = _rolling_std(close, _TD_HALF).clip(lower=_EPS)
    return _safe_div(vol_slope, vol_std) - _safe_div(price_slope, price_std)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_PRICE_DIVERGENCE_REGISTRY_001_075 = {
    "vpd_001_corr_vol_close_21d": {"inputs": ["close", "volume"], "func": vpd_001_corr_vol_close_21d},
    "vpd_002_corr_vol_close_63d": {"inputs": ["close", "volume"], "func": vpd_002_corr_vol_close_63d},
    "vpd_003_corr_vol_close_126d": {"inputs": ["close", "volume"], "func": vpd_003_corr_vol_close_126d},
    "vpd_004_corr_vol_close_252d": {"inputs": ["close", "volume"], "func": vpd_004_corr_vol_close_252d},
    "vpd_005_corr_vol_ret_5d": {"inputs": ["close", "volume"], "func": vpd_005_corr_vol_ret_5d},
    "vpd_006_corr_vol_ret_21d": {"inputs": ["close", "volume"], "func": vpd_006_corr_vol_ret_21d},
    "vpd_007_corr_vol_ret_63d": {"inputs": ["close", "volume"], "func": vpd_007_corr_vol_ret_63d},
    "vpd_008_corr_vol_ret_252d": {"inputs": ["close", "volume"], "func": vpd_008_corr_vol_ret_252d},
    "vpd_009_corr_vol_logret_21d": {"inputs": ["close", "volume"], "func": vpd_009_corr_vol_logret_21d},
    "vpd_010_corr_vol_logret_63d": {"inputs": ["close", "volume"], "func": vpd_010_corr_vol_logret_63d},
    "vpd_011_corr_volchg_ret_21d": {"inputs": ["close", "volume"], "func": vpd_011_corr_volchg_ret_21d},
    "vpd_012_corr_volchg_ret_63d": {"inputs": ["close", "volume"], "func": vpd_012_corr_volchg_ret_63d},
    "vpd_013_corr_volchg_ret_126d": {"inputs": ["close", "volume"], "func": vpd_013_corr_volchg_ret_126d},
    "vpd_014_corr_vol_low_21d": {"inputs": ["close", "low", "volume"], "func": vpd_014_corr_vol_low_21d},
    "vpd_015_corr_vol_low_63d": {"inputs": ["close", "low", "volume"], "func": vpd_015_corr_vol_low_63d},
    "vpd_016_cov_vol_ret_21d": {"inputs": ["close", "volume"], "func": vpd_016_cov_vol_ret_21d},
    "vpd_017_cov_vol_ret_63d": {"inputs": ["close", "volume"], "func": vpd_017_cov_vol_ret_63d},
    "vpd_018_cov_vol_ret_252d": {"inputs": ["close", "volume"], "func": vpd_018_cov_vol_ret_252d},
    "vpd_019_cov_volchg_ret_21d": {"inputs": ["close", "volume"], "func": vpd_019_cov_volchg_ret_21d},
    "vpd_020_cov_volchg_ret_63d": {"inputs": ["close", "volume"], "func": vpd_020_cov_volchg_ret_63d},
    "vpd_021_cov_vol_logret_21d": {"inputs": ["close", "volume"], "func": vpd_021_cov_vol_logret_21d},
    "vpd_022_cov_vol_logret_63d": {"inputs": ["close", "volume"], "func": vpd_022_cov_vol_logret_63d},
    "vpd_023_neg_corr_vol_ret_flag_21d": {"inputs": ["close", "volume"], "func": vpd_023_neg_corr_vol_ret_flag_21d},
    "vpd_024_neg_corr_vol_ret_flag_63d": {"inputs": ["close", "volume"], "func": vpd_024_neg_corr_vol_ret_flag_63d},
    "vpd_025_corr_vol_ret_21d_pct_rank_252d": {"inputs": ["close", "volume"], "func": vpd_025_corr_vol_ret_21d_pct_rank_252d},
    "vpd_026_corr_vol_ret_63d_pct_rank_252d": {"inputs": ["close", "volume"], "func": vpd_026_corr_vol_ret_63d_pct_rank_252d},
    "vpd_027_corr_vol_close_21d_zscore_252d": {"inputs": ["close", "volume"], "func": vpd_027_corr_vol_close_21d_zscore_252d},
    "vpd_028_cov_vol_ret_21d_norm_by_vol_std": {"inputs": ["close", "volume"], "func": vpd_028_cov_vol_ret_21d_norm_by_vol_std},
    "vpd_029_cov_vol_ret_63d_norm_by_vol_std": {"inputs": ["close", "volume"], "func": vpd_029_cov_vol_ret_63d_norm_by_vol_std},
    "vpd_030_corr_vol_ret_ewm21_vs_ewm63": {"inputs": ["close", "volume"], "func": vpd_030_corr_vol_ret_ewm21_vs_ewm63},
    "vpd_031_down_ret_x_vol_raw_21d": {"inputs": ["close", "volume"], "func": vpd_031_down_ret_x_vol_raw_21d},
    "vpd_032_down_ret_x_vol_raw_63d": {"inputs": ["close", "volume"], "func": vpd_032_down_ret_x_vol_raw_63d},
    "vpd_033_down_ret_x_vol_raw_252d": {"inputs": ["close", "volume"], "func": vpd_033_down_ret_x_vol_raw_252d},
    "vpd_034_down_ret_x_volnorm_21d": {"inputs": ["close", "volume"], "func": vpd_034_down_ret_x_volnorm_21d},
    "vpd_035_down_ret_x_volnorm_63d": {"inputs": ["close", "volume"], "func": vpd_035_down_ret_x_volnorm_63d},
    "vpd_036_down_ret_x_volnorm_252d": {"inputs": ["close", "volume"], "func": vpd_036_down_ret_x_volnorm_252d},
    "vpd_037_down_logret_x_vol_21d": {"inputs": ["close", "volume"], "func": vpd_037_down_logret_x_vol_21d},
    "vpd_038_down_logret_x_vol_63d": {"inputs": ["close", "volume"], "func": vpd_038_down_logret_x_vol_63d},
    "vpd_039_avg_down_ret_x_volnorm_21d": {"inputs": ["close", "volume"], "func": vpd_039_avg_down_ret_x_volnorm_21d},
    "vpd_040_avg_down_ret_x_volnorm_63d": {"inputs": ["close", "volume"], "func": vpd_040_avg_down_ret_x_volnorm_63d},
    "vpd_041_down_ret_x_vol_minus_up_ret_x_vol_21d": {"inputs": ["close", "volume"], "func": vpd_041_down_ret_x_vol_minus_up_ret_x_vol_21d},
    "vpd_042_down_ret_x_vol_minus_up_ret_x_vol_63d": {"inputs": ["close", "volume"], "func": vpd_042_down_ret_x_vol_minus_up_ret_x_vol_63d},
    "vpd_043_down_ret_x_vol_21d_pct_rank_252d": {"inputs": ["close", "volume"], "func": vpd_043_down_ret_x_vol_21d_pct_rank_252d},
    "vpd_044_down_ret_x_vol_63d_pct_rank_252d": {"inputs": ["close", "volume"], "func": vpd_044_down_ret_x_vol_63d_pct_rank_252d},
    "vpd_045_ewm_down_ret_x_vol_21": {"inputs": ["close", "volume"], "func": vpd_045_ewm_down_ret_x_vol_21},
    "vpd_046_newlow21_vol_rising_flag": {"inputs": ["close", "volume"], "func": vpd_046_newlow21_vol_rising_flag},
    "vpd_047_newlow63_vol_rising_flag": {"inputs": ["close", "volume"], "func": vpd_047_newlow63_vol_rising_flag},
    "vpd_048_newlow252_vol_rising_flag": {"inputs": ["close", "volume"], "func": vpd_048_newlow252_vol_rising_flag},
    "vpd_049_newlow21_vol_rising_count_63d": {"inputs": ["close", "volume"], "func": vpd_049_newlow21_vol_rising_count_63d},
    "vpd_050_newlow63_vol_rising_count_252d": {"inputs": ["close", "volume"], "func": vpd_050_newlow63_vol_rising_count_252d},
    "vpd_051_price_down_vol_up_flag": {"inputs": ["close", "volume"], "func": vpd_051_price_down_vol_up_flag},
    "vpd_052_price_down_vol_up_count_21d": {"inputs": ["close", "volume"], "func": vpd_052_price_down_vol_up_count_21d},
    "vpd_053_price_down_vol_up_count_63d": {"inputs": ["close", "volume"], "func": vpd_053_price_down_vol_up_count_63d},
    "vpd_054_price_down_vol_up_count_252d": {"inputs": ["close", "volume"], "func": vpd_054_price_down_vol_up_count_252d},
    "vpd_055_price_down_vol_up_frac_21d": {"inputs": ["close", "volume"], "func": vpd_055_price_down_vol_up_frac_21d},
    "vpd_056_price_down_vol_up_frac_63d": {"inputs": ["close", "volume"], "func": vpd_056_price_down_vol_up_frac_63d},
    "vpd_057_price_down_vol_up_frac_252d": {"inputs": ["close", "volume"], "func": vpd_057_price_down_vol_up_frac_252d},
    "vpd_058_price_dn_vol_up_vs_price_dn_vol_dn_ratio_21d": {"inputs": ["close", "volume"], "func": vpd_058_price_dn_vol_up_vs_price_dn_vol_dn_ratio_21d},
    "vpd_059_price_dn_vol_up_vs_price_dn_vol_dn_ratio_63d": {"inputs": ["close", "volume"], "func": vpd_059_price_dn_vol_up_vs_price_dn_vol_dn_ratio_63d},
    "vpd_060_newlow_vol_surge_intensity_21d": {"inputs": ["close", "volume"], "func": vpd_060_newlow_vol_surge_intensity_21d},
    "vpd_061_vol_price_beta_21d": {"inputs": ["close", "volume"], "func": vpd_061_vol_price_beta_21d},
    "vpd_062_vol_price_beta_63d": {"inputs": ["close", "volume"], "func": vpd_062_vol_price_beta_63d},
    "vpd_063_vol_ret_beta_21d": {"inputs": ["close", "volume"], "func": vpd_063_vol_ret_beta_21d},
    "vpd_064_vol_ret_beta_63d": {"inputs": ["close", "volume"], "func": vpd_064_vol_ret_beta_63d},
    "vpd_065_vol_ret_beta_252d": {"inputs": ["close", "volume"], "func": vpd_065_vol_ret_beta_252d},
    "vpd_066_volnorm_price_beta_21d": {"inputs": ["close", "volume"], "func": vpd_066_volnorm_price_beta_21d},
    "vpd_067_volnorm_ret_beta_21d": {"inputs": ["close", "volume"], "func": vpd_067_volnorm_ret_beta_21d},
    "vpd_068_volnorm_ret_beta_63d": {"inputs": ["close", "volume"], "func": vpd_068_volnorm_ret_beta_63d},
    "vpd_069_vol_ret_beta_21d_pct_rank_252d": {"inputs": ["close", "volume"], "func": vpd_069_vol_ret_beta_21d_pct_rank_252d},
    "vpd_070_vol_ret_beta_63d_zscore_252d": {"inputs": ["close", "volume"], "func": vpd_070_vol_ret_beta_63d_zscore_252d},
    "vpd_071_vol_slope_21d": {"inputs": ["close", "volume"], "func": vpd_071_vol_slope_21d},
    "vpd_072_vol_slope_63d": {"inputs": ["close", "volume"], "func": vpd_072_vol_slope_63d},
    "vpd_073_price_slope_21d": {"inputs": ["close", "volume"], "func": vpd_073_price_slope_21d},
    "vpd_074_vol_slope_minus_price_slope_norm_21d": {"inputs": ["close", "volume"], "func": vpd_074_vol_slope_minus_price_slope_norm_21d},
    "vpd_075_vol_slope_minus_price_slope_norm_63d": {"inputs": ["close", "volume"], "func": vpd_075_vol_slope_minus_price_slope_norm_63d},
    # --- new 151-175 ---
    "vpd_151_corr_vol_high_21d": {"inputs": ["high", "volume"], "func": vpd_151_corr_vol_high_21d},
    "vpd_152_corr_vol_high_63d": {"inputs": ["high", "volume"], "func": vpd_152_corr_vol_high_63d},
    "vpd_153_down_open_to_close_x_vol_21d": {"inputs": ["close", "open", "volume"], "func": vpd_153_down_open_to_close_x_vol_21d},
    "vpd_154_down_open_to_close_x_vol_63d": {"inputs": ["close", "open", "volume"], "func": vpd_154_down_open_to_close_x_vol_63d},
    "vpd_155_vol_weighted_open_close_decline_21d": {"inputs": ["close", "open", "volume"], "func": vpd_155_vol_weighted_open_close_decline_21d},
    "vpd_156_vol_weighted_open_close_decline_63d": {"inputs": ["close", "open", "volume"], "func": vpd_156_vol_weighted_open_close_decline_63d},
    "vpd_157_corr_vol_open_close_range_21d": {"inputs": ["close", "open", "volume"], "func": vpd_157_corr_vol_open_close_range_21d},
    "vpd_158_corr_vol_open_close_range_63d": {"inputs": ["close", "open", "volume"], "func": vpd_158_corr_vol_open_close_range_63d},
    "vpd_159_high_low_range_x_vol_down_21d": {"inputs": ["close", "high", "low", "volume"], "func": vpd_159_high_low_range_x_vol_down_21d},
    "vpd_160_high_low_range_x_vol_down_63d": {"inputs": ["close", "high", "low", "volume"], "func": vpd_160_high_low_range_x_vol_down_63d},
    "vpd_161_newlow63_vol_surge_2x_flag": {"inputs": ["close", "volume"], "func": vpd_161_newlow63_vol_surge_2x_flag},
    "vpd_162_newlow252_vol_surge_2x_flag": {"inputs": ["close", "volume"], "func": vpd_162_newlow252_vol_surge_2x_flag},
    "vpd_163_newlow63_vol_surge_count_252d": {"inputs": ["close", "volume"], "func": vpd_163_newlow63_vol_surge_count_252d},
    "vpd_164_down_ret_logvol_interaction_21d": {"inputs": ["close", "volume"], "func": vpd_164_down_ret_logvol_interaction_21d},
    "vpd_165_down_ret_logvol_interaction_63d": {"inputs": ["close", "volume"], "func": vpd_165_down_ret_logvol_interaction_63d},
    "vpd_166_corr_logvol_ret_21d": {"inputs": ["close", "volume"], "func": vpd_166_corr_logvol_ret_21d},
    "vpd_167_corr_logvol_ret_63d": {"inputs": ["close", "volume"], "func": vpd_167_corr_logvol_ret_63d},
    "vpd_168_vol_ret_beta_126d": {"inputs": ["close", "volume"], "func": vpd_168_vol_ret_beta_126d},
    "vpd_169_vol_price_beta_126d": {"inputs": ["close", "volume"], "func": vpd_169_vol_price_beta_126d},
    "vpd_170_down_ret_x_vol_raw_126d": {"inputs": ["close", "volume"], "func": vpd_170_down_ret_x_vol_raw_126d},
    "vpd_171_vol_on_down_days_vs_total_vol_126d": {"inputs": ["close", "volume"], "func": vpd_171_vol_on_down_days_vs_total_vol_126d},
    "vpd_172_corr_vol_ret_126d": {"inputs": ["close", "volume"], "func": vpd_172_corr_vol_ret_126d},
    "vpd_173_vol_slope_126d": {"inputs": ["close", "volume"], "func": vpd_173_vol_slope_126d},
    "vpd_174_price_slope_63d": {"inputs": ["close", "volume"], "func": vpd_174_price_slope_63d},
    "vpd_175_vol_slope_minus_price_slope_norm_126d": {"inputs": ["close", "volume"], "func": vpd_175_vol_slope_minus_price_slope_norm_126d},
}
