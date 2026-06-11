"""
59_market_impact_proxy -- 2nd Derivatives (Features drv2_001-025)
Domain: rate of change of base market-impact concepts -- velocity/acceleration
  of Kyle lambda, Amivest ratio, return-per-dollar-volume, impact elasticity,
  Pastor-Stambaugh reversal coefficient, and impact asymmetry measures.
Asset class: US equities | Daily OHLCV (price/volume ONLY -- SEP folder)
Target context: capitulation -- impact sensitivity worsening rapidly
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

def _safe_div(num, den):
    """Element-wise division; zero denominator becomes NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_sum(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s, span):
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s):
    return np.log(s.clip(lower=_EPS))


def _zscore(s, w):
    """Rolling z-score of s over window w."""
    mu  = _rolling_mean(s, w)
    sig = _rolling_std(s, w)
    return _safe_div(s - mu, sig)


def _pct_rank(s, w):
    """Rolling percentile rank of s within trailing w periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


def _ret_per_dolvol(close, volume):
    """Daily return-per-dollar-volume: |return| / dollar_volume."""
    ret    = close.pct_change(1).abs()
    dolvol = close * volume
    return _safe_div(ret, dolvol)


def _amivest(close, volume):
    """Daily Amivest liquidity ratio: dollar_volume / |return|."""
    ret    = close.pct_change(1).abs()
    dolvol = close * volume
    return _safe_div(dolvol, ret.replace(0, np.nan))


def _sqrt_impact(close, volume):
    """Square-root impact proxy: |return| / sqrt(dollar_volume)."""
    ret    = close.pct_change(1).abs()
    dolvol = (close * volume).clip(lower=_EPS)
    return ret / np.sqrt(dolvol)


def _ols_slope_xy(x_vals, y_vals, min_p):
    """OLS slope on two numpy arrays."""
    if len(x_vals) < min_p:
        return np.nan
    xm = x_vals.mean()
    ym = y_vals.mean()
    num = ((x_vals - xm) * (y_vals - ym)).sum()
    den = ((x_vals - xm) ** 2).sum()
    return num / den if abs(den) > _EPS else np.nan


def _rolling_ols_slope(x_ser, y_ser, w):
    """Rolling OLS slope of y on x over window w."""
    df     = pd.DataFrame({"x": x_ser, "y": y_ser}).dropna()
    x_vals = df["x"].values
    y_vals = df["y"].values
    idx    = df.index
    min_p  = max(2, w // 2)
    out    = pd.Series(np.nan, index=x_ser.index, dtype=float)
    for i in range(len(x_vals)):
        start = max(0, i - w + 1)
        xs = x_vals[start: i + 1]
        ys = y_vals[start: i + 1]
        out.loc[idx[i]] = _ols_slope_xy(xs, ys, min_p)
    return out


def _kyle_lambda_fast(close, volume, w):
    """Efficient rolling Kyle lambda: OLS slope of daily return on signed dollar volume."""
    ret      = close.pct_change(1)
    dolvol   = close * volume
    sign_vol = np.sign(ret) * dolvol
    df     = pd.DataFrame({"sv": sign_vol, "rt": ret}).dropna()
    x_vals = df["sv"].values
    y_vals = df["rt"].values
    idx    = df.index
    min_p  = max(2, w // 2)
    out    = pd.Series(np.nan, index=close.index, dtype=float)
    for i in range(len(x_vals)):
        start = max(0, i - w + 1)
        xs = x_vals[start: i + 1]
        ys = y_vals[start: i + 1]
        out.loc[idx[i]] = _ols_slope_xy(xs, ys, min_p)
    return out


def _ps_reversal(close, volume, w):
    """Pastor-Stambaugh signed-volume return reversal coefficient (rolling OLS)."""
    ret      = close.pct_change(1)
    sign_vol = np.sign(ret) * volume
    sv_lag   = sign_vol.shift(1)
    return _rolling_ols_slope(sv_lag, ret, w)


def _impact_elasticity(close, volume, w):
    """Rolling OLS slope of |return| on log(dollar_volume)."""
    abs_ret = close.pct_change(1).abs()
    log_dv  = _log_safe(close * volume)
    return _rolling_ols_slope(log_dv, abs_ret, w)


def _linslope(s, w):
    """Rolling OLS slope of s on time index over w periods (rate of change via regression)."""
    def slope(x):
        n = len(x)
        if n < max(2, w // 2):
            return np.nan
        xi = np.arange(n, dtype=float)
        xm = xi.mean()
        ym = x.mean()
        num = ((xi - xm) * (x - ym)).sum()
        den = ((xi - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=True)

# -- 2nd-derivative feature functions drv2_001-025 ----------------------------

# --- Group A (drv2_001-008): Rate of change of Kyle lambda ---

def mip_drv2_001_kyle_lambda_21d_5d_diff(close, volume):
    """5-day diff of 21d Kyle lambda (velocity of short-run impact sensitivity)."""
    return _kyle_lambda_fast(close, volume, _TD_MON).diff(_TD_WEEK)


def mip_drv2_002_kyle_lambda_21d_21d_diff(close, volume):
    """21-day diff of 21d Kyle lambda (month-over-month impact change)."""
    return _kyle_lambda_fast(close, volume, _TD_MON).diff(_TD_MON)


def mip_drv2_003_kyle_lambda_63d_21d_diff(close, volume):
    """21-day diff of 63d Kyle lambda (quarterly impact trend acceleration)."""
    return _kyle_lambda_fast(close, volume, _TD_QTR).diff(_TD_MON)


def mip_drv2_004_kyle_lambda_21d_ols_slope_21d(close, volume):
    """OLS slope of 21d Kyle lambda over trailing 21-day window."""
    return _linslope(_kyle_lambda_fast(close, volume, _TD_MON), _TD_MON)


def mip_drv2_005_kyle_lambda_21d_ols_slope_63d(close, volume):
    """OLS slope of 21d Kyle lambda over trailing 63-day window."""
    return _linslope(_kyle_lambda_fast(close, volume, _TD_MON), _TD_QTR)


def mip_drv2_006_kyle_lambda_zscore_5d_diff(close, volume):
    """5-day diff of 63d z-score of 21d Kyle lambda (velocity of z-score)."""
    return _zscore(_kyle_lambda_fast(close, volume, _TD_MON), _TD_QTR).diff(_TD_WEEK)


def mip_drv2_007_kyle_lambda_zscore_21d_diff(close, volume):
    """21-day diff of 63d z-score of 21d Kyle lambda (monthly z-score acceleration)."""
    return _zscore(_kyle_lambda_fast(close, volume, _TD_MON), _TD_QTR).diff(_TD_MON)


def mip_drv2_008_kyle_lambda_pct_rank_5d_diff(close, volume):
    """5-day diff of 252d percentile rank of 21d Kyle lambda."""
    return _pct_rank(_kyle_lambda_fast(close, volume, _TD_MON), _TD_YEAR).diff(_TD_WEEK)


# --- Group B (drv2_009-016): Rate of change of Amivest and return-per-dolvol ---

def mip_drv2_009_amivest_21d_mean_5d_diff(close, volume):
    """5-day diff of 21d Amivest mean (velocity of monthly liquidity depth)."""
    return _rolling_mean(_amivest(close, volume), _TD_MON).diff(_TD_WEEK)


def mip_drv2_010_amivest_21d_mean_21d_diff(close, volume):
    """21-day diff of 21d Amivest mean (month-over-month depth change)."""
    return _rolling_mean(_amivest(close, volume), _TD_MON).diff(_TD_MON)


def mip_drv2_011_amivest_63d_mean_21d_diff(close, volume):
    """21-day diff of 63d Amivest mean (acceleration of quarterly depth trend)."""
    return _rolling_mean(_amivest(close, volume), _TD_QTR).diff(_TD_MON)


def mip_drv2_012_amivest_ols_slope_21d(close, volume):
    """OLS slope of daily Amivest ratio over trailing 21 days."""
    return _linslope(_amivest(close, volume), _TD_MON)


def mip_drv2_013_amivest_ols_slope_63d(close, volume):
    """OLS slope of daily Amivest ratio over trailing 63 days."""
    return _linslope(_amivest(close, volume), _TD_QTR)


def mip_drv2_014_ret_per_dolvol_5d_mean_5d_diff(close, volume):
    """5-day diff of 5d ret-per-dolvol mean (velocity of short-run impact level)."""
    return _rolling_mean(_ret_per_dolvol(close, volume), _TD_WEEK).diff(_TD_WEEK)


def mip_drv2_015_ret_per_dolvol_21d_mean_5d_diff(close, volume):
    """5-day diff of 21d ret-per-dolvol mean (velocity of monthly impact level)."""
    return _rolling_mean(_ret_per_dolvol(close, volume), _TD_MON).diff(_TD_WEEK)


def mip_drv2_016_ret_per_dolvol_zscore_5d_diff(close, volume):
    """5-day diff of 63d z-score of ret-per-dolvol (velocity of impact z-score)."""
    return _zscore(_ret_per_dolvol(close, volume), _TD_QTR).diff(_TD_WEEK)


# --- Group C (drv2_017-021): Rate of change of impact elasticity ---

def mip_drv2_017_impact_elasticity_21d_5d_diff(close, volume):
    """5-day diff of 21d impact elasticity (velocity of elasticity)."""
    return _impact_elasticity(close, volume, _TD_MON).diff(_TD_WEEK)


def mip_drv2_018_impact_elasticity_21d_21d_diff(close, volume):
    """21-day diff of 21d impact elasticity (monthly elasticity acceleration)."""
    return _impact_elasticity(close, volume, _TD_MON).diff(_TD_MON)


def mip_drv2_019_impact_elasticity_ols_slope_63d(close, volume):
    """OLS slope of 21d impact elasticity over trailing 63 days."""
    return _linslope(_impact_elasticity(close, volume, _TD_MON), _TD_QTR)


def mip_drv2_020_ps_reversal_21d_5d_diff(close, volume):
    """5-day diff of 21d PS reversal coeff (velocity of reversal sensitivity)."""
    return _ps_reversal(close, volume, _TD_MON).diff(_TD_WEEK)


def mip_drv2_021_ps_reversal_ols_slope_63d(close, volume):
    """OLS slope of 21d PS reversal coeff over trailing 63 days."""
    return _linslope(_ps_reversal(close, volume, _TD_MON), _TD_QTR)


# --- Group D (drv2_022-025): Rate of change of composite and sqrt-impact measures ---

def mip_drv2_022_sqrt_impact_21d_mean_5d_diff(close, volume):
    """5-day diff of 21d sqrt-impact mean (velocity of square-root impact level)."""
    return _rolling_mean(_sqrt_impact(close, volume), _TD_MON).diff(_TD_WEEK)


def mip_drv2_023_sqrt_impact_zscore_5d_diff(close, volume):
    """5-day diff of 63d z-score of sqrt-impact (velocity of sqrt-impact z-score)."""
    return _zscore(_sqrt_impact(close, volume), _TD_QTR).diff(_TD_WEEK)


def mip_drv2_024_amivest_zscore_5d_diff(close, volume):
    """5-day diff of 63d z-score of Amivest ratio (velocity of depth z-score)."""
    return _zscore(_amivest(close, volume), _TD_QTR).diff(_TD_WEEK)


def mip_drv2_025_ret_per_dolvol_spike_ratio_5d_diff(close, volume):
    """5-day diff of ret-per-dolvol/21d-mean spike ratio (velocity of spike intensity)."""
    r     = _ret_per_dolvol(close, volume)
    ratio = _safe_div(r, _rolling_mean(r, _TD_MON))
    return ratio.diff(_TD_WEEK)


# -- Registry ------------------------------------------------------------------

MARKET_IMPACT_PROXY_REGISTRY_2ND_DERIVATIVES = {
    "mip_drv2_001_kyle_lambda_21d_5d_diff": {"inputs": ["close", "volume"], "func": mip_drv2_001_kyle_lambda_21d_5d_diff},
    "mip_drv2_002_kyle_lambda_21d_21d_diff": {"inputs": ["close", "volume"], "func": mip_drv2_002_kyle_lambda_21d_21d_diff},
    "mip_drv2_003_kyle_lambda_63d_21d_diff": {"inputs": ["close", "volume"], "func": mip_drv2_003_kyle_lambda_63d_21d_diff},
    "mip_drv2_004_kyle_lambda_21d_ols_slope_21d": {"inputs": ["close", "volume"], "func": mip_drv2_004_kyle_lambda_21d_ols_slope_21d},
    "mip_drv2_005_kyle_lambda_21d_ols_slope_63d": {"inputs": ["close", "volume"], "func": mip_drv2_005_kyle_lambda_21d_ols_slope_63d},
    "mip_drv2_006_kyle_lambda_zscore_5d_diff": {"inputs": ["close", "volume"], "func": mip_drv2_006_kyle_lambda_zscore_5d_diff},
    "mip_drv2_007_kyle_lambda_zscore_21d_diff": {"inputs": ["close", "volume"], "func": mip_drv2_007_kyle_lambda_zscore_21d_diff},
    "mip_drv2_008_kyle_lambda_pct_rank_5d_diff": {"inputs": ["close", "volume"], "func": mip_drv2_008_kyle_lambda_pct_rank_5d_diff},
    "mip_drv2_009_amivest_21d_mean_5d_diff": {"inputs": ["close", "volume"], "func": mip_drv2_009_amivest_21d_mean_5d_diff},
    "mip_drv2_010_amivest_21d_mean_21d_diff": {"inputs": ["close", "volume"], "func": mip_drv2_010_amivest_21d_mean_21d_diff},
    "mip_drv2_011_amivest_63d_mean_21d_diff": {"inputs": ["close", "volume"], "func": mip_drv2_011_amivest_63d_mean_21d_diff},
    "mip_drv2_012_amivest_ols_slope_21d": {"inputs": ["close", "volume"], "func": mip_drv2_012_amivest_ols_slope_21d},
    "mip_drv2_013_amivest_ols_slope_63d": {"inputs": ["close", "volume"], "func": mip_drv2_013_amivest_ols_slope_63d},
    "mip_drv2_014_ret_per_dolvol_5d_mean_5d_diff": {"inputs": ["close", "volume"], "func": mip_drv2_014_ret_per_dolvol_5d_mean_5d_diff},
    "mip_drv2_015_ret_per_dolvol_21d_mean_5d_diff": {"inputs": ["close", "volume"], "func": mip_drv2_015_ret_per_dolvol_21d_mean_5d_diff},
    "mip_drv2_016_ret_per_dolvol_zscore_5d_diff": {"inputs": ["close", "volume"], "func": mip_drv2_016_ret_per_dolvol_zscore_5d_diff},
    "mip_drv2_017_impact_elasticity_21d_5d_diff": {"inputs": ["close", "volume"], "func": mip_drv2_017_impact_elasticity_21d_5d_diff},
    "mip_drv2_018_impact_elasticity_21d_21d_diff": {"inputs": ["close", "volume"], "func": mip_drv2_018_impact_elasticity_21d_21d_diff},
    "mip_drv2_019_impact_elasticity_ols_slope_63d": {"inputs": ["close", "volume"], "func": mip_drv2_019_impact_elasticity_ols_slope_63d},
    "mip_drv2_020_ps_reversal_21d_5d_diff": {"inputs": ["close", "volume"], "func": mip_drv2_020_ps_reversal_21d_5d_diff},
    "mip_drv2_021_ps_reversal_ols_slope_63d": {"inputs": ["close", "volume"], "func": mip_drv2_021_ps_reversal_ols_slope_63d},
    "mip_drv2_022_sqrt_impact_21d_mean_5d_diff": {"inputs": ["close", "volume"], "func": mip_drv2_022_sqrt_impact_21d_mean_5d_diff},
    "mip_drv2_023_sqrt_impact_zscore_5d_diff": {"inputs": ["close", "volume"], "func": mip_drv2_023_sqrt_impact_zscore_5d_diff},
    "mip_drv2_024_amivest_zscore_5d_diff": {"inputs": ["close", "volume"], "func": mip_drv2_024_amivest_zscore_5d_diff},
    "mip_drv2_025_ret_per_dolvol_spike_ratio_5d_diff": {"inputs": ["close", "volume"], "func": mip_drv2_025_ret_per_dolvol_spike_ratio_5d_diff},
}