"""
59_market_impact_proxy -- 3rd Derivatives (Features drv3_001-025)
Domain: rate of change of 2nd-derivative market-impact concepts -- exhaustion/inflection
  of acceleration in Kyle lambda, Amivest, return-per-dollar-volume, impact elasticity,
  Pastor-Stambaugh reversal, and composite impact sensitivity measures.
Asset class: US equities | Daily OHLCV (price/volume ONLY -- SEP folder)
Target context: capitulation -- inflection/exhaustion of impact sensitivity acceleration
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
    """Rolling OLS slope of s on time index over w periods."""
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

# -- 3rd-derivative feature functions drv3_001-025 ----------------------------

# --- Group A (drv3_001-008): Rate of change of Kyle lambda 2nd-derivative signals ---

def mip_drv3_001_kyle_lambda_21d_5d_diff_5d_diff(close, volume):
    """5-day diff of (5d diff of 21d Kyle lambda) -- acceleration of impact velocity."""
    return _kyle_lambda_fast(close, volume, _TD_MON).diff(_TD_WEEK).diff(_TD_WEEK)


def mip_drv3_002_kyle_lambda_21d_5d_diff_21d_diff(close, volume):
    """21-day diff of (5d diff of 21d Kyle lambda) -- monthly accel of impact velocity."""
    return _kyle_lambda_fast(close, volume, _TD_MON).diff(_TD_WEEK).diff(_TD_MON)


def mip_drv3_003_kyle_lambda_ols_slope_21d_5d_diff(close, volume):
    """5-day diff of OLS slope of 21d Kyle lambda over 21d -- inflection of slope trend."""
    return _linslope(_kyle_lambda_fast(close, volume, _TD_MON), _TD_MON).diff(_TD_WEEK)


def mip_drv3_004_kyle_lambda_ols_slope_63d_5d_diff(close, volume):
    """5-day diff of OLS slope of 21d Kyle lambda over 63d -- inflection of quarterly slope."""
    return _linslope(_kyle_lambda_fast(close, volume, _TD_MON), _TD_QTR).diff(_TD_WEEK)


def mip_drv3_005_kyle_lambda_zscore_5d_diff_5d_diff(close, volume):
    """5-day diff of (5d diff of Kyle z-score) -- acceleration of z-score velocity."""
    return _zscore(_kyle_lambda_fast(close, volume, _TD_MON), _TD_QTR).diff(_TD_WEEK).diff(_TD_WEEK)


def mip_drv3_006_kyle_lambda_21d_mean_ols_slope_21d(close, volume):
    """OLS slope of (21d rolling mean of 21d Kyle lambda) over trailing 21d."""
    kl_mean = _rolling_mean(_kyle_lambda_fast(close, volume, _TD_MON), _TD_MON)
    return _linslope(kl_mean, _TD_MON)


def mip_drv3_007_kyle_lambda_21d_mean_ols_slope_63d(close, volume):
    """OLS slope of (21d rolling mean of 21d Kyle lambda) over trailing 63d."""
    kl_mean = _rolling_mean(_kyle_lambda_fast(close, volume, _TD_MON), _TD_MON)
    return _linslope(kl_mean, _TD_QTR)


def mip_drv3_008_kyle_lambda_63d_mean_5d_diff(close, volume):
    """5-day diff of (21d mean of 63d Kyle lambda) -- inflection of smoothed impact."""
    return _rolling_mean(_kyle_lambda_fast(close, volume, _TD_QTR), _TD_MON).diff(_TD_WEEK)


# --- Group B (drv3_009-016): Rate of change of Amivest/ret-per-dolvol 2nd deriv ---

def mip_drv3_009_amivest_5d_diff_5d_diff(close, volume):
    """5-day diff of (5d diff of Amivest ratio) -- acceleration of depth velocity."""
    return _amivest(close, volume).diff(_TD_WEEK).diff(_TD_WEEK)


def mip_drv3_010_amivest_ols_slope_21d_5d_diff(close, volume):
    """5-day diff of OLS slope of Amivest over 21d -- inflection of depth slope."""
    return _linslope(_amivest(close, volume), _TD_MON).diff(_TD_WEEK)


def mip_drv3_011_amivest_ols_slope_63d_5d_diff(close, volume):
    """5-day diff of OLS slope of Amivest over 63d -- inflection of quarterly depth slope."""
    return _linslope(_amivest(close, volume), _TD_QTR).diff(_TD_WEEK)


def mip_drv3_012_amivest_21d_mean_5d_diff_5d_diff(close, volume):
    """5d diff of (5d diff of 21d Amivest mean) -- second accel of monthly depth."""
    return _rolling_mean(_amivest(close, volume), _TD_MON).diff(_TD_WEEK).diff(_TD_WEEK)


def mip_drv3_013_ret_per_dolvol_5d_diff_5d_diff(close, volume):
    """5d diff of (5d diff of ret-per-dolvol) -- acceleration of impact velocity."""
    return _ret_per_dolvol(close, volume).diff(_TD_WEEK).diff(_TD_WEEK)


def mip_drv3_014_ret_per_dolvol_ols_slope_21d_5d_diff(close, volume):
    """5d diff of OLS slope of ret-per-dolvol over 21d -- inflection of impact slope."""
    return _linslope(_ret_per_dolvol(close, volume), _TD_MON).diff(_TD_WEEK)


def mip_drv3_015_ret_per_dolvol_ols_slope_63d_5d_diff(close, volume):
    """5d diff of OLS slope of ret-per-dolvol over 63d -- quarterly inflection."""
    return _linslope(_ret_per_dolvol(close, volume), _TD_QTR).diff(_TD_WEEK)


def mip_drv3_016_ret_per_dolvol_zscore_5d_diff_5d_diff(close, volume):
    """5d diff of (5d diff of ret-per-dolvol z-score) -- acceleration of z-score."""
    return _zscore(_ret_per_dolvol(close, volume), _TD_QTR).diff(_TD_WEEK).diff(_TD_WEEK)


# --- Group C (drv3_017-021): Rate of change of impact elasticity 2nd deriv ---

def mip_drv3_017_impact_elasticity_5d_diff_5d_diff(close, volume):
    """5d diff of (5d diff of 21d impact elasticity) -- acceleration of elasticity velocity."""
    return _impact_elasticity(close, volume, _TD_MON).diff(_TD_WEEK).diff(_TD_WEEK)


def mip_drv3_018_impact_elasticity_ols_slope_21d_5d_diff(close, volume):
    """5d diff of OLS slope of impact elasticity over 21d -- inflection of elasticity trend."""
    return _linslope(_impact_elasticity(close, volume, _TD_MON), _TD_MON).diff(_TD_WEEK)


def mip_drv3_019_impact_elasticity_ols_slope_63d_5d_diff(close, volume):
    """5d diff of OLS slope of impact elasticity over 63d -- quarterly inflection."""
    return _linslope(_impact_elasticity(close, volume, _TD_MON), _TD_QTR).diff(_TD_WEEK)


def mip_drv3_020_ps_reversal_5d_diff_5d_diff(close, volume):
    """5d diff of (5d diff of 21d PS reversal coeff) -- acceleration of reversal velocity."""
    return _ps_reversal(close, volume, _TD_MON).diff(_TD_WEEK).diff(_TD_WEEK)


def mip_drv3_021_ps_reversal_ols_slope_21d_5d_diff(close, volume):
    """5d diff of OLS slope of PS reversal over 21d -- inflection of reversal trend."""
    return _linslope(_ps_reversal(close, volume, _TD_MON), _TD_MON).diff(_TD_WEEK)


# --- Group D (drv3_022-025): Rate of change of composite 2nd-derivative signals ---

def mip_drv3_022_sqrt_impact_ols_slope_21d_5d_diff(close, volume):
    """5d diff of OLS slope of sqrt-impact over 21d -- inflection of sqrt-impact trend."""
    return _linslope(_sqrt_impact(close, volume), _TD_MON).diff(_TD_WEEK)


def mip_drv3_023_sqrt_impact_5d_diff_5d_diff(close, volume):
    """5d diff of (5d diff of sqrt-impact) -- acceleration of sqrt-impact velocity."""
    return _sqrt_impact(close, volume).diff(_TD_WEEK).diff(_TD_WEEK)


def mip_drv3_024_amivest_zscore_5d_diff_5d_diff(close, volume):
    """5d diff of (5d diff of 63d Amivest z-score) -- acceleration of depth z-score vel."""
    return _zscore(_amivest(close, volume), _TD_QTR).diff(_TD_WEEK).diff(_TD_WEEK)


def mip_drv3_025_composite_impact_vel_5d_diff(close, volume):
    """5d diff of composite impact velocity (mean of Kyle lambda and ret-per-dolvol 5d diffs)."""
    kl_vel = _kyle_lambda_fast(close, volume, _TD_MON).diff(_TD_WEEK)
    ri_vel = _ret_per_dolvol(close, volume).diff(_TD_WEEK)
    comp   = (kl_vel + ri_vel) / 2.0
    return comp.diff(_TD_WEEK)


# -- Registry ------------------------------------------------------------------

MARKET_IMPACT_PROXY_REGISTRY_3RD_DERIVATIVES = {
    "mip_drv3_001_kyle_lambda_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": mip_drv3_001_kyle_lambda_21d_5d_diff_5d_diff},
    "mip_drv3_002_kyle_lambda_21d_5d_diff_21d_diff": {"inputs": ["close", "volume"], "func": mip_drv3_002_kyle_lambda_21d_5d_diff_21d_diff},
    "mip_drv3_003_kyle_lambda_ols_slope_21d_5d_diff": {"inputs": ["close", "volume"], "func": mip_drv3_003_kyle_lambda_ols_slope_21d_5d_diff},
    "mip_drv3_004_kyle_lambda_ols_slope_63d_5d_diff": {"inputs": ["close", "volume"], "func": mip_drv3_004_kyle_lambda_ols_slope_63d_5d_diff},
    "mip_drv3_005_kyle_lambda_zscore_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": mip_drv3_005_kyle_lambda_zscore_5d_diff_5d_diff},
    "mip_drv3_006_kyle_lambda_21d_mean_ols_slope_21d": {"inputs": ["close", "volume"], "func": mip_drv3_006_kyle_lambda_21d_mean_ols_slope_21d},
    "mip_drv3_007_kyle_lambda_21d_mean_ols_slope_63d": {"inputs": ["close", "volume"], "func": mip_drv3_007_kyle_lambda_21d_mean_ols_slope_63d},
    "mip_drv3_008_kyle_lambda_63d_mean_5d_diff": {"inputs": ["close", "volume"], "func": mip_drv3_008_kyle_lambda_63d_mean_5d_diff},
    "mip_drv3_009_amivest_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": mip_drv3_009_amivest_5d_diff_5d_diff},
    "mip_drv3_010_amivest_ols_slope_21d_5d_diff": {"inputs": ["close", "volume"], "func": mip_drv3_010_amivest_ols_slope_21d_5d_diff},
    "mip_drv3_011_amivest_ols_slope_63d_5d_diff": {"inputs": ["close", "volume"], "func": mip_drv3_011_amivest_ols_slope_63d_5d_diff},
    "mip_drv3_012_amivest_21d_mean_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": mip_drv3_012_amivest_21d_mean_5d_diff_5d_diff},
    "mip_drv3_013_ret_per_dolvol_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": mip_drv3_013_ret_per_dolvol_5d_diff_5d_diff},
    "mip_drv3_014_ret_per_dolvol_ols_slope_21d_5d_diff": {"inputs": ["close", "volume"], "func": mip_drv3_014_ret_per_dolvol_ols_slope_21d_5d_diff},
    "mip_drv3_015_ret_per_dolvol_ols_slope_63d_5d_diff": {"inputs": ["close", "volume"], "func": mip_drv3_015_ret_per_dolvol_ols_slope_63d_5d_diff},
    "mip_drv3_016_ret_per_dolvol_zscore_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": mip_drv3_016_ret_per_dolvol_zscore_5d_diff_5d_diff},
    "mip_drv3_017_impact_elasticity_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": mip_drv3_017_impact_elasticity_5d_diff_5d_diff},
    "mip_drv3_018_impact_elasticity_ols_slope_21d_5d_diff": {"inputs": ["close", "volume"], "func": mip_drv3_018_impact_elasticity_ols_slope_21d_5d_diff},
    "mip_drv3_019_impact_elasticity_ols_slope_63d_5d_diff": {"inputs": ["close", "volume"], "func": mip_drv3_019_impact_elasticity_ols_slope_63d_5d_diff},
    "mip_drv3_020_ps_reversal_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": mip_drv3_020_ps_reversal_5d_diff_5d_diff},
    "mip_drv3_021_ps_reversal_ols_slope_21d_5d_diff": {"inputs": ["close", "volume"], "func": mip_drv3_021_ps_reversal_ols_slope_21d_5d_diff},
    "mip_drv3_022_sqrt_impact_ols_slope_21d_5d_diff": {"inputs": ["close", "volume"], "func": mip_drv3_022_sqrt_impact_ols_slope_21d_5d_diff},
    "mip_drv3_023_sqrt_impact_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": mip_drv3_023_sqrt_impact_5d_diff_5d_diff},
    "mip_drv3_024_amivest_zscore_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": mip_drv3_024_amivest_zscore_5d_diff_5d_diff},
    "mip_drv3_025_composite_impact_vel_5d_diff": {"inputs": ["close", "volume"], "func": mip_drv3_025_composite_impact_vel_5d_diff},
}