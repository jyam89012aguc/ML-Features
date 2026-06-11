"""
120_information_decay — 2nd Derivatives (Features idc_drv2_001-025)
Domain: rate of change of base information-decay features — velocity of decay-rate behavior
Includes derivatives of half-life, autocorrelation decay rate, EWM half-life,
        Hurst exponent, entropy, MI decay, and variance persistence features
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


def _returns(close: pd.Series) -> pd.Series:
    return np.log(close / close.shift(1))


def _rolling_autocorr(s: pd.Series, w: int, lag: int) -> pd.Series:
    def _ac(x):
        x = x[~np.isnan(x)]
        if len(x) < lag + 3:
            return np.nan
        x0, x1 = x[:-lag], x[lag:]
        if x0.std() < _EPS or x1.std() < _EPS:
            return np.nan
        return float(np.corrcoef(x0, x1)[0, 1])
    return s.rolling(w, min_periods=max(lag + 3, w // 2)).apply(_ac, raw=True)


def _decay_rate_63d(close: pd.Series) -> pd.Series:
    """AC decay rate from AC(1)/AC(2), 63-day window."""
    r = _returns(close)
    ac1 = _rolling_autocorr(r, _TD_QTR, 1)
    ac2 = _rolling_autocorr(r, _TD_QTR, 2)
    ratio = _safe_div(ac2.abs(), ac1.abs().clip(lower=_EPS))
    ratio_c = ratio.clip(lower=_EPS, upper=1.0 - _EPS)
    return -np.log(ratio_c)


def _halflife_63d(close: pd.Series) -> pd.Series:
    """Half-life from AC decay rate, 63-day window."""
    return np.log(2.0) / _decay_rate_63d(close).clip(lower=_EPS)


def _ewm_halflife_63d(close: pd.Series) -> pd.Series:
    """EWM half-life from AC(1) of returns, 63-day window."""
    ac1 = _rolling_autocorr(_returns(close), _TD_QTR, 1)
    alpha = (1.0 - ac1).clip(lower=_EPS, upper=1.0 - _EPS)
    return np.log(2.0) / (-np.log(1.0 - alpha))


def _hurst_63d(close: pd.Series) -> pd.Series:
    """Hurst exponent, 63-day R/S window."""
    def _hurst(x):
        x = x[~np.isnan(x)]
        n = len(x)
        if n < 10:
            return np.nan
        lags, rs_vals = [], []
        for w in [max(4, n // 4), max(5, n // 3), max(6, n // 2), n]:
            if w > n:
                continue
            seg = x[:w]
            dev = np.cumsum(seg - seg.mean())
            r_val = dev.max() - dev.min()
            s_val = seg.std()
            if s_val < _EPS:
                continue
            lags.append(np.log(w))
            rs_vals.append(np.log(r_val / s_val))
        if len(lags) < 2:
            return np.nan
        lags, rs_vals = np.array(lags), np.array(rs_vals)
        if lags.std() < _EPS:
            return np.nan
        return float(np.polyfit(lags, rs_vals, 1)[0])
    r = _returns(close).values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_QTR
    for i in range(w - 1, n):
        result[i] = _hurst(r[max(0, i - w + 1):i + 1])
    return pd.Series(result, index=close.index)


def _garch_alpha_63d(close: pd.Series) -> pd.Series:
    """GARCH alpha proxy: AC(1) of squared returns, 63-day window."""
    r2 = _returns(close) ** 2
    return _rolling_autocorr(r2, _TD_QTR, 1)


def _entropy_63d(close: pd.Series) -> pd.Series:
    """Shannon entropy of return signs, 63-day window."""
    def _ent(x):
        x = x[~np.isnan(x)]
        if len(x) < 5:
            return np.nan
        p_up = np.sum(x > 0) / len(x)
        p_dn = 1.0 - p_up
        if p_up <= 0 or p_dn <= 0:
            return 0.0
        return float(-(p_up * np.log2(p_up) + p_dn * np.log2(p_dn)))
    r = _returns(close).values
    n = len(r)
    result = np.full(n, np.nan)
    w = _TD_QTR
    for i in range(w - 1, n):
        result[i] = _ent(r[max(0, i - w + 1):i + 1])
    return pd.Series(result, index=close.index)


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

def idc_drv2_001_decay_rate_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day AC decay rate (velocity of decay rate)."""
    return _decay_rate_63d(close).diff(_TD_WEEK)


def idc_drv2_002_decay_rate_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day AC decay rate (monthly velocity of decay rate)."""
    return _decay_rate_63d(close).diff(_TD_MON)


def idc_drv2_003_halflife_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day half-life (velocity of half-life changes)."""
    return _halflife_63d(close).diff(_TD_WEEK)


def idc_drv2_004_halflife_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day half-life (monthly velocity of half-life)."""
    return _halflife_63d(close).diff(_TD_MON)


def idc_drv2_005_ewm_halflife_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day EWM half-life (velocity of EWM half-life)."""
    return _ewm_halflife_63d(close).diff(_TD_WEEK)


def idc_drv2_006_ewm_halflife_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day EWM half-life (monthly EWM half-life velocity)."""
    return _ewm_halflife_63d(close).diff(_TD_MON)


def idc_drv2_007_hurst_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day Hurst exponent (velocity of Hurst changes)."""
    return _hurst_63d(close).diff(_TD_WEEK)


def idc_drv2_008_hurst_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day Hurst exponent (monthly Hurst velocity)."""
    return _hurst_63d(close).diff(_TD_MON)


def idc_drv2_009_garch_alpha_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of GARCH alpha proxy (velocity of variance persistence change)."""
    return _garch_alpha_63d(close).diff(_TD_WEEK)


def idc_drv2_010_garch_alpha_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of GARCH alpha proxy."""
    return _garch_alpha_63d(close).diff(_TD_MON)


def idc_drv2_011_entropy_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day return entropy (velocity of entropy change)."""
    return _entropy_63d(close).diff(_TD_WEEK)


def idc_drv2_012_entropy_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day return entropy."""
    return _entropy_63d(close).diff(_TD_MON)


def idc_drv2_013_impulse_decay_vol_5d_to_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 5d/21d vol ratio (velocity of vol shock absorption)."""
    r = _returns(close)
    vol5 = r.rolling(_TD_WEEK, min_periods=2).std()
    vol21 = r.rolling(_TD_MON, min_periods=5).std()
    ratio = _safe_div(vol5, vol21.clip(lower=_EPS))
    return ratio.diff(_TD_WEEK)


def idc_drv2_014_impulse_decay_vol_5d_to_21d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 5d/21d vol ratio."""
    r = _returns(close)
    vol5 = r.rolling(_TD_WEEK, min_periods=2).std()
    vol21 = r.rolling(_TD_MON, min_periods=5).std()
    ratio = _safe_div(vol5, vol21.clip(lower=_EPS))
    return ratio.diff(_TD_MON)


def idc_drv2_015_ewm5_ewm21_spread_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (EWM5 - EWM21)/EWM21 momentum decay spread."""
    e5 = close.ewm(span=_TD_WEEK, min_periods=2).mean()
    e21 = close.ewm(span=_TD_MON, min_periods=5).mean()
    spread = _safe_div(e5 - e21, e21.clip(lower=_EPS))
    return spread.diff(_TD_WEEK)


def idc_drv2_016_ac_lag1_returns_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of AC(1) of returns over 63-day window (velocity of AC(1) change)."""
    ac1 = _rolling_autocorr(_returns(close), _TD_QTR, 1)
    return ac1.diff(_TD_WEEK)


def idc_drv2_017_ac_lag1_returns_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of AC(1) of returns over 63-day window."""
    ac1 = _rolling_autocorr(_returns(close), _TD_QTR, 1)
    return ac1.diff(_TD_MON)


def idc_drv2_018_vol_shock_ratio_5d_ewm_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of EWM variance ratio (5d/21d EWM squared returns)."""
    r2 = _returns(close) ** 2
    ev5 = r2.ewm(span=_TD_WEEK, min_periods=2).mean()
    ev21 = r2.ewm(span=_TD_MON, min_periods=5).mean()
    ratio = _safe_div(ev5, ev21.clip(lower=_EPS))
    return ratio.diff(_TD_WEEK)


def idc_drv2_019_snr_5d_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 5d/21d signal-to-noise ratio."""
    r = _returns(close)
    signal = close.pct_change(_TD_WEEK).abs()
    noise = r.rolling(_TD_MON, min_periods=5).std()
    snr = _safe_div(signal, noise.clip(lower=_EPS))
    return snr.diff(_TD_WEEK)


def idc_drv2_020_decay_rate_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of 63-day AC decay rate (linear trend of decay rate)."""
    return _linslope(_decay_rate_63d(close), _TD_MON)


def idc_drv2_021_halflife_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of 63-day half-life (linear trend of half-life)."""
    return _linslope(_halflife_63d(close), _TD_MON)


def idc_drv2_022_hurst_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of 63-day Hurst exponent."""
    return _linslope(_hurst_63d(close), _TD_MON)


def idc_drv2_023_garch_alpha_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of GARCH alpha proxy."""
    return _linslope(_garch_alpha_63d(close), _TD_MON)


def idc_drv2_024_entropy_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of 63-day return entropy."""
    return _linslope(_entropy_63d(close), _TD_MON)


def idc_drv2_025_decay_composite_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of composite (decay rate z-score + entropy z-score) / 2."""
    rate = _decay_rate_63d(close)
    rate_z = _safe_div(rate - _rolling_mean(rate, _TD_YEAR),
                       _rolling_std(rate, _TD_YEAR).clip(lower=_EPS))
    ent = _entropy_63d(close)
    ent_z = _safe_div(ent - _rolling_mean(ent, _TD_YEAR),
                      _rolling_std(ent, _TD_YEAR).clip(lower=_EPS))
    composite = (rate_z.fillna(0.0) + ent_z.fillna(0.0)) / 2.0
    return composite.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

INFORMATION_DECAY_REGISTRY_2ND_DERIVATIVES = {
    "idc_drv2_001_decay_rate_5d_diff": {"inputs": ["close"], "func": idc_drv2_001_decay_rate_5d_diff},
    "idc_drv2_002_decay_rate_21d_diff": {"inputs": ["close"], "func": idc_drv2_002_decay_rate_21d_diff},
    "idc_drv2_003_halflife_5d_diff": {"inputs": ["close"], "func": idc_drv2_003_halflife_5d_diff},
    "idc_drv2_004_halflife_21d_diff": {"inputs": ["close"], "func": idc_drv2_004_halflife_21d_diff},
    "idc_drv2_005_ewm_halflife_5d_diff": {"inputs": ["close"], "func": idc_drv2_005_ewm_halflife_5d_diff},
    "idc_drv2_006_ewm_halflife_21d_diff": {"inputs": ["close"], "func": idc_drv2_006_ewm_halflife_21d_diff},
    "idc_drv2_007_hurst_5d_diff": {"inputs": ["close"], "func": idc_drv2_007_hurst_5d_diff},
    "idc_drv2_008_hurst_21d_diff": {"inputs": ["close"], "func": idc_drv2_008_hurst_21d_diff},
    "idc_drv2_009_garch_alpha_5d_diff": {"inputs": ["close"], "func": idc_drv2_009_garch_alpha_5d_diff},
    "idc_drv2_010_garch_alpha_21d_diff": {"inputs": ["close"], "func": idc_drv2_010_garch_alpha_21d_diff},
    "idc_drv2_011_entropy_5d_diff": {"inputs": ["close"], "func": idc_drv2_011_entropy_5d_diff},
    "idc_drv2_012_entropy_21d_diff": {"inputs": ["close"], "func": idc_drv2_012_entropy_21d_diff},
    "idc_drv2_013_impulse_decay_vol_5d_to_21d_5d_diff": {"inputs": ["close"], "func": idc_drv2_013_impulse_decay_vol_5d_to_21d_5d_diff},
    "idc_drv2_014_impulse_decay_vol_5d_to_21d_21d_diff": {"inputs": ["close"], "func": idc_drv2_014_impulse_decay_vol_5d_to_21d_21d_diff},
    "idc_drv2_015_ewm5_ewm21_spread_5d_diff": {"inputs": ["close"], "func": idc_drv2_015_ewm5_ewm21_spread_5d_diff},
    "idc_drv2_016_ac_lag1_returns_63d_5d_diff": {"inputs": ["close"], "func": idc_drv2_016_ac_lag1_returns_63d_5d_diff},
    "idc_drv2_017_ac_lag1_returns_63d_21d_diff": {"inputs": ["close"], "func": idc_drv2_017_ac_lag1_returns_63d_21d_diff},
    "idc_drv2_018_vol_shock_ratio_5d_ewm_5d_diff": {"inputs": ["close"], "func": idc_drv2_018_vol_shock_ratio_5d_ewm_5d_diff},
    "idc_drv2_019_snr_5d_21d_5d_diff": {"inputs": ["close"], "func": idc_drv2_019_snr_5d_21d_5d_diff},
    "idc_drv2_020_decay_rate_slope_21d": {"inputs": ["close"], "func": idc_drv2_020_decay_rate_slope_21d},
    "idc_drv2_021_halflife_slope_21d": {"inputs": ["close"], "func": idc_drv2_021_halflife_slope_21d},
    "idc_drv2_022_hurst_slope_21d": {"inputs": ["close"], "func": idc_drv2_022_hurst_slope_21d},
    "idc_drv2_023_garch_alpha_slope_21d": {"inputs": ["close"], "func": idc_drv2_023_garch_alpha_slope_21d},
    "idc_drv2_024_entropy_slope_21d": {"inputs": ["close"], "func": idc_drv2_024_entropy_slope_21d},
    "idc_drv2_025_decay_composite_5d_diff": {"inputs": ["close"], "func": idc_drv2_025_decay_composite_5d_diff},
}
