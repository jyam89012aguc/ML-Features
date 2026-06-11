"""range_estimators_family d3 features 001-075 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__076_150.py. Theme:
range-based volatility estimators (Parkinson, Garman-Klass, Rogers-Satchell,
Yang-Zhang, GKYZ), range efficiency, range asymmetry, intraday-vs-overnight,
range-vs-return divergence, true-range/ATR extensions.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers — no cross-family
imports.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_3Y = 756
DDAYS_5Y = 1260


# ---------------------------- helpers ----------------------------

def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))


def _safe_div(num, den):
    if isinstance(den, pd.Series):
        d = den.replace(0, np.nan)
    else:
        d = np.where(den == 0, np.nan, den)
    out = num / d
    if isinstance(out, pd.Series):
        return out.replace([np.inf, -np.inf], np.nan)
    idx = num.index if hasattr(num, "index") else None
    return pd.Series(out, index=idx).replace([np.inf, -np.inf], np.nan)


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _true_range(high, low, close):
    pc = close.shift(1)
    return pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)


def _atr(high, low, close, n=21):
    return _true_range(high, low, close).rolling(n, min_periods=max(n // 3, 2)).mean()


def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _slope(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if valid.all():
            wv = w
        else:
            x = x[valid]
            wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


# ============================================================
# Bucket A — Parkinson estimator at multi horizons (001-008)
# σ²_P = (1/(4 ln 2)) * mean(log(H/L)²)
# ============================================================

def f37_rges_001_parkinson_var_5d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Parkinson variance over 5d — weekly intraday-range vol from H/L only."""
    lhl = _safe_log(high) - _safe_log(low)
    return (lhl ** 2).rolling(WDAYS, min_periods=2).mean() / (4.0 * np.log(2.0))


def f37_rges_002_parkinson_var_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Parkinson variance over 21d — monthly intraday-range vol."""
    lhl = _safe_log(high) - _safe_log(low)
    return (lhl ** 2).rolling(MDAYS, min_periods=WDAYS).mean() / (4.0 * np.log(2.0))


def f37_rges_003_parkinson_var_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Parkinson variance over 63d — quarterly range-based vol regime."""
    lhl = _safe_log(high) - _safe_log(low)
    return (lhl ** 2).rolling(QDAYS, min_periods=MDAYS).mean() / (4.0 * np.log(2.0))


def f37_rges_004_parkinson_var_126d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Parkinson variance over 126d — half-year range-vol regime."""
    lhl = _safe_log(high) - _safe_log(low)
    return (lhl ** 2).rolling(126, min_periods=QDAYS).mean() / (4.0 * np.log(2.0))


def f37_rges_005_parkinson_var_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Parkinson variance over 252d — annual range-vol baseline."""
    lhl = _safe_log(high) - _safe_log(low)
    return (lhl ** 2).rolling(YDAYS, min_periods=QDAYS).mean() / (4.0 * np.log(2.0))


def f37_rges_006_parkinson_var_504d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Parkinson variance over 504d — biennial range-vol baseline."""
    lhl = _safe_log(high) - _safe_log(low)
    return (lhl ** 2).rolling(DDAYS_2Y, min_periods=YDAYS).mean() / (4.0 * np.log(2.0))


def f37_rges_007_parkinson_sigma_annualized_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Annualized Parkinson sigma (sqrt of 21d Parkinson variance × 252) — vol units."""
    lhl = _safe_log(high) - _safe_log(low)
    var = (lhl ** 2).rolling(MDAYS, min_periods=WDAYS).mean() / (4.0 * np.log(2.0))
    return np.sqrt(var * float(YDAYS))


def f37_rges_008_parkinson_sigma_annualized_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Annualized Parkinson sigma (sqrt of 63d Parkinson variance × 252)."""
    lhl = _safe_log(high) - _safe_log(low)
    var = (lhl ** 2).rolling(QDAYS, min_periods=MDAYS).mean() / (4.0 * np.log(2.0))
    return np.sqrt(var * float(YDAYS))


# ============================================================
# Bucket B — Garman-Klass estimator at multi horizons (009-016)
# σ²_GK = 0.5*mean(log(H/L)²) − (2 ln 2 − 1)*mean(log(C/O)²)
# ============================================================

def f37_rges_009_garman_klass_var_5d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Garman-Klass variance over 5d — weekly OHLC-based vol."""
    lhl = _safe_log(high) - _safe_log(low)
    lco = _safe_log(close) - _safe_log(open_)
    a = 0.5 * (lhl ** 2).rolling(WDAYS, min_periods=2).mean()
    b = (2.0 * np.log(2.0) - 1.0) * (lco ** 2).rolling(WDAYS, min_periods=2).mean()
    return a - b


def f37_rges_010_garman_klass_var_21d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Garman-Klass variance over 21d — monthly OHLC vol."""
    lhl = _safe_log(high) - _safe_log(low)
    lco = _safe_log(close) - _safe_log(open_)
    a = 0.5 * (lhl ** 2).rolling(MDAYS, min_periods=WDAYS).mean()
    b = (2.0 * np.log(2.0) - 1.0) * (lco ** 2).rolling(MDAYS, min_periods=WDAYS).mean()
    return a - b


def f37_rges_011_garman_klass_var_63d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Garman-Klass variance over 63d — quarterly OHLC vol regime."""
    lhl = _safe_log(high) - _safe_log(low)
    lco = _safe_log(close) - _safe_log(open_)
    a = 0.5 * (lhl ** 2).rolling(QDAYS, min_periods=MDAYS).mean()
    b = (2.0 * np.log(2.0) - 1.0) * (lco ** 2).rolling(QDAYS, min_periods=MDAYS).mean()
    return a - b


def f37_rges_012_garman_klass_var_126d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Garman-Klass variance over 126d — half-year OHLC vol regime."""
    lhl = _safe_log(high) - _safe_log(low)
    lco = _safe_log(close) - _safe_log(open_)
    a = 0.5 * (lhl ** 2).rolling(126, min_periods=QDAYS).mean()
    b = (2.0 * np.log(2.0) - 1.0) * (lco ** 2).rolling(126, min_periods=QDAYS).mean()
    return a - b


def f37_rges_013_garman_klass_var_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Garman-Klass variance over 252d — annual OHLC vol baseline."""
    lhl = _safe_log(high) - _safe_log(low)
    lco = _safe_log(close) - _safe_log(open_)
    a = 0.5 * (lhl ** 2).rolling(YDAYS, min_periods=QDAYS).mean()
    b = (2.0 * np.log(2.0) - 1.0) * (lco ** 2).rolling(YDAYS, min_periods=QDAYS).mean()
    return a - b


def f37_rges_014_garman_klass_var_504d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Garman-Klass variance over 504d — biennial OHLC vol baseline."""
    lhl = _safe_log(high) - _safe_log(low)
    lco = _safe_log(close) - _safe_log(open_)
    a = 0.5 * (lhl ** 2).rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    b = (2.0 * np.log(2.0) - 1.0) * (lco ** 2).rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    return a - b


def f37_rges_015_garman_klass_sigma_annualized_21d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Annualized Garman-Klass sigma over 21d window — vol units."""
    lhl = _safe_log(high) - _safe_log(low)
    lco = _safe_log(close) - _safe_log(open_)
    a = 0.5 * (lhl ** 2).rolling(MDAYS, min_periods=WDAYS).mean()
    b = (2.0 * np.log(2.0) - 1.0) * (lco ** 2).rolling(MDAYS, min_periods=WDAYS).mean()
    return np.sqrt((a - b).clip(lower=0) * float(YDAYS))


def f37_rges_016_garman_klass_sigma_annualized_63d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Annualized Garman-Klass sigma over 63d window."""
    lhl = _safe_log(high) - _safe_log(low)
    lco = _safe_log(close) - _safe_log(open_)
    a = 0.5 * (lhl ** 2).rolling(QDAYS, min_periods=MDAYS).mean()
    b = (2.0 * np.log(2.0) - 1.0) * (lco ** 2).rolling(QDAYS, min_periods=MDAYS).mean()
    return np.sqrt((a - b).clip(lower=0) * float(YDAYS))


# ============================================================
# Bucket C — Rogers-Satchell drift-independent estimator (017-024)
# σ²_RS = mean(log(H/C)*log(H/O) + log(L/C)*log(L/O))
# ============================================================

def f37_rges_017_rogers_satchell_var_5d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rogers-Satchell variance over 5d — drift-independent intraday vol."""
    lho = _safe_log(high) - _safe_log(open_)
    lhc = _safe_log(high) - _safe_log(close)
    llo = _safe_log(low) - _safe_log(open_)
    llc = _safe_log(low) - _safe_log(close)
    term = lhc * lho + llc * llo
    return term.rolling(WDAYS, min_periods=2).mean()


def f37_rges_018_rogers_satchell_var_21d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rogers-Satchell variance over 21d — drift-free monthly vol."""
    lho = _safe_log(high) - _safe_log(open_)
    lhc = _safe_log(high) - _safe_log(close)
    llo = _safe_log(low) - _safe_log(open_)
    llc = _safe_log(low) - _safe_log(close)
    term = lhc * lho + llc * llo
    return term.rolling(MDAYS, min_periods=WDAYS).mean()


def f37_rges_019_rogers_satchell_var_63d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rogers-Satchell variance over 63d — drift-free quarterly vol."""
    lho = _safe_log(high) - _safe_log(open_)
    lhc = _safe_log(high) - _safe_log(close)
    llo = _safe_log(low) - _safe_log(open_)
    llc = _safe_log(low) - _safe_log(close)
    term = lhc * lho + llc * llo
    return term.rolling(QDAYS, min_periods=MDAYS).mean()


def f37_rges_020_rogers_satchell_var_126d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rogers-Satchell variance over 126d — drift-free half-year vol."""
    lho = _safe_log(high) - _safe_log(open_)
    lhc = _safe_log(high) - _safe_log(close)
    llo = _safe_log(low) - _safe_log(open_)
    llc = _safe_log(low) - _safe_log(close)
    term = lhc * lho + llc * llo
    return term.rolling(126, min_periods=QDAYS).mean()


def f37_rges_021_rogers_satchell_var_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rogers-Satchell variance over 252d — annual drift-free vol baseline."""
    lho = _safe_log(high) - _safe_log(open_)
    lhc = _safe_log(high) - _safe_log(close)
    llo = _safe_log(low) - _safe_log(open_)
    llc = _safe_log(low) - _safe_log(close)
    term = lhc * lho + llc * llo
    return term.rolling(YDAYS, min_periods=QDAYS).mean()


def f37_rges_022_rogers_satchell_var_504d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rogers-Satchell variance over 504d — biennial drift-free vol baseline."""
    lho = _safe_log(high) - _safe_log(open_)
    lhc = _safe_log(high) - _safe_log(close)
    llo = _safe_log(low) - _safe_log(open_)
    llc = _safe_log(low) - _safe_log(close)
    term = lhc * lho + llc * llo
    return term.rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f37_rges_023_rogers_satchell_sigma_annualized_21d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Annualized Rogers-Satchell sigma over 21d window."""
    lho = _safe_log(high) - _safe_log(open_)
    lhc = _safe_log(high) - _safe_log(close)
    llo = _safe_log(low) - _safe_log(open_)
    llc = _safe_log(low) - _safe_log(close)
    term = lhc * lho + llc * llo
    var = term.rolling(MDAYS, min_periods=WDAYS).mean()
    return np.sqrt(var.clip(lower=0) * float(YDAYS))


def f37_rges_024_rogers_satchell_sigma_annualized_63d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Annualized Rogers-Satchell sigma over 63d window."""
    lho = _safe_log(high) - _safe_log(open_)
    lhc = _safe_log(high) - _safe_log(close)
    llo = _safe_log(low) - _safe_log(open_)
    llc = _safe_log(low) - _safe_log(close)
    term = lhc * lho + llc * llo
    var = term.rolling(QDAYS, min_periods=MDAYS).mean()
    return np.sqrt(var.clip(lower=0) * float(YDAYS))


# ============================================================
# Bucket D — Yang-Zhang estimator at multi horizons (025-032)
# σ²_YZ = σ²_overnight + k*σ²_open_close + (1-k)*σ²_RS
# k = 0.34 / (1.34 + (n+1)/(n-1))
# ============================================================

def _yang_zhang_var(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, n: int, mp: int) -> pd.Series:
    log_open = _safe_log(open_)
    log_close = _safe_log(close)
    log_high = _safe_log(high)
    log_low = _safe_log(low)
    ovn = log_open - log_close.shift(1)
    o2c = log_close - log_open
    lho = log_high - log_open
    lhc = log_high - log_close
    llo = log_low - log_open
    llc = log_low - log_close
    rs_term = lhc * lho + llc * llo
    var_ovn = ovn.rolling(n, min_periods=mp).var()
    var_o2c = o2c.rolling(n, min_periods=mp).var()
    var_rs = rs_term.rolling(n, min_periods=mp).mean()
    k = 0.34 / (1.34 + (n + 1.0) / (n - 1.0))
    return var_ovn + k * var_o2c + (1.0 - k) * var_rs


def f37_rges_025_yang_zhang_var_21d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Yang-Zhang variance over 21d — combines overnight + intraday drift + RS."""
    return _yang_zhang_var(open_, high, low, close, MDAYS, WDAYS)


def f37_rges_026_yang_zhang_var_63d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Yang-Zhang variance over 63d — quarterly composite vol estimator."""
    return _yang_zhang_var(open_, high, low, close, QDAYS, MDAYS)


def f37_rges_027_yang_zhang_var_126d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Yang-Zhang variance over 126d — half-year composite vol."""
    return _yang_zhang_var(open_, high, low, close, 126, QDAYS)


def f37_rges_028_yang_zhang_var_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Yang-Zhang variance over 252d — annual composite vol baseline."""
    return _yang_zhang_var(open_, high, low, close, YDAYS, QDAYS)


def f37_rges_029_yang_zhang_var_504d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Yang-Zhang variance over 504d — biennial composite vol baseline."""
    return _yang_zhang_var(open_, high, low, close, DDAYS_2Y, YDAYS)


def f37_rges_030_yang_zhang_sigma_annualized_63d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Annualized Yang-Zhang sigma over 63d window."""
    var = _yang_zhang_var(open_, high, low, close, QDAYS, MDAYS)
    return np.sqrt(var.clip(lower=0) * float(YDAYS))


def f37_rges_031_yang_zhang_overnight_component_63d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Overnight-return variance component of YZ — pure gap volatility 63d."""
    ovn = _safe_log(open_) - _safe_log(close).shift(1)
    return ovn.rolling(QDAYS, min_periods=MDAYS).var()


def f37_rges_032_yang_zhang_open_to_close_component_63d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Open-to-close (intraday drift) variance component of YZ over 63d."""
    o2c = _safe_log(close) - _safe_log(open_)
    return o2c.rolling(QDAYS, min_periods=MDAYS).var()


# ============================================================
# Bucket E — GKYZ: GK with overnight gap added (033-037)
# ============================================================

def _gkyz_var(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, n: int, mp: int) -> pd.Series:
    ovn = _safe_log(open_) - _safe_log(close).shift(1)
    lhl = _safe_log(high) - _safe_log(low)
    lco = _safe_log(close) - _safe_log(open_)
    a = (ovn ** 2).rolling(n, min_periods=mp).mean()
    b = 0.5 * (lhl ** 2).rolling(n, min_periods=mp).mean()
    c = (2.0 * np.log(2.0) - 1.0) * (lco ** 2).rolling(n, min_periods=mp).mean()
    return a + b - c


def f37_rges_033_gkyz_var_21d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """GKYZ variance over 21d — GK + overnight gap term."""
    return _gkyz_var(open_, high, low, close, MDAYS, WDAYS)


def f37_rges_034_gkyz_var_63d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """GKYZ variance over 63d — quarterly OHLC+gap vol."""
    return _gkyz_var(open_, high, low, close, QDAYS, MDAYS)


def f37_rges_035_gkyz_var_126d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """GKYZ variance over 126d — half-year OHLC+gap vol."""
    return _gkyz_var(open_, high, low, close, 126, QDAYS)


def f37_rges_036_gkyz_var_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """GKYZ variance over 252d — annual OHLC+gap vol baseline."""
    return _gkyz_var(open_, high, low, close, YDAYS, QDAYS)


def f37_rges_037_gkyz_var_504d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """GKYZ variance over 504d — biennial OHLC+gap vol baseline."""
    return _gkyz_var(open_, high, low, close, DDAYS_2Y, YDAYS)


# ============================================================
# Bucket F — Range efficiency ratios (Parkinson / close-to-close sigma) (038-043)
# ============================================================

def f37_rges_038_parkinson_to_cc_ratio_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Parkinson sigma / close-to-close sigma over 21d — range efficiency ratio."""
    lhl = _safe_log(high) - _safe_log(low)
    par_var = (lhl ** 2).rolling(MDAYS, min_periods=WDAYS).mean() / (4.0 * np.log(2.0))
    ret = _safe_log(close).diff()
    cc_var = ret.rolling(MDAYS, min_periods=WDAYS).var()
    return _safe_div(np.sqrt(par_var.clip(lower=0)), np.sqrt(cc_var.clip(lower=0)))


def f37_rges_039_parkinson_to_cc_ratio_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Parkinson sigma / close-to-close sigma over 63d — quarterly range efficiency."""
    lhl = _safe_log(high) - _safe_log(low)
    par_var = (lhl ** 2).rolling(QDAYS, min_periods=MDAYS).mean() / (4.0 * np.log(2.0))
    ret = _safe_log(close).diff()
    cc_var = ret.rolling(QDAYS, min_periods=MDAYS).var()
    return _safe_div(np.sqrt(par_var.clip(lower=0)), np.sqrt(cc_var.clip(lower=0)))


def f37_rges_040_parkinson_to_cc_ratio_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Parkinson / close-to-close sigma over 126d — half-year range efficiency."""
    lhl = _safe_log(high) - _safe_log(low)
    par_var = (lhl ** 2).rolling(126, min_periods=QDAYS).mean() / (4.0 * np.log(2.0))
    ret = _safe_log(close).diff()
    cc_var = ret.rolling(126, min_periods=QDAYS).var()
    return _safe_div(np.sqrt(par_var.clip(lower=0)), np.sqrt(cc_var.clip(lower=0)))


def f37_rges_041_parkinson_to_cc_ratio_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Parkinson / close-to-close sigma over 252d — annual range efficiency baseline."""
    lhl = _safe_log(high) - _safe_log(low)
    par_var = (lhl ** 2).rolling(YDAYS, min_periods=QDAYS).mean() / (4.0 * np.log(2.0))
    ret = _safe_log(close).diff()
    cc_var = ret.rolling(YDAYS, min_periods=QDAYS).var()
    return _safe_div(np.sqrt(par_var.clip(lower=0)), np.sqrt(cc_var.clip(lower=0)))


def f37_rges_042_garman_klass_to_cc_ratio_63d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Garman-Klass sigma / close-to-close sigma over 63d — GK efficiency ratio."""
    lhl = _safe_log(high) - _safe_log(low)
    lco = _safe_log(close) - _safe_log(open_)
    a = 0.5 * (lhl ** 2).rolling(QDAYS, min_periods=MDAYS).mean()
    b = (2.0 * np.log(2.0) - 1.0) * (lco ** 2).rolling(QDAYS, min_periods=MDAYS).mean()
    gk_var = (a - b).clip(lower=0)
    ret = _safe_log(close).diff()
    cc_var = ret.rolling(QDAYS, min_periods=MDAYS).var()
    return _safe_div(np.sqrt(gk_var), np.sqrt(cc_var.clip(lower=0)))


def f37_rges_043_rogers_satchell_to_cc_ratio_63d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rogers-Satchell sigma / close-to-close sigma over 63d — RS efficiency ratio."""
    lho = _safe_log(high) - _safe_log(open_)
    lhc = _safe_log(high) - _safe_log(close)
    llo = _safe_log(low) - _safe_log(open_)
    llc = _safe_log(low) - _safe_log(close)
    rs_var = (lhc * lho + llc * llo).rolling(QDAYS, min_periods=MDAYS).mean()
    ret = _safe_log(close).diff()
    cc_var = ret.rolling(QDAYS, min_periods=MDAYS).var()
    return _safe_div(np.sqrt(rs_var.clip(lower=0)), np.sqrt(cc_var.clip(lower=0)))


# ============================================================
# Bucket G — Estimator divergences (044-053)
# ============================================================

def f37_rges_044_parkinson_minus_gk_var_21d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Parkinson var − Garman-Klass var, 21d — bar-shape divergence (drift impact)."""
    lhl = _safe_log(high) - _safe_log(low)
    lco = _safe_log(close) - _safe_log(open_)
    par = (lhl ** 2).rolling(MDAYS, min_periods=WDAYS).mean() / (4.0 * np.log(2.0))
    a = 0.5 * (lhl ** 2).rolling(MDAYS, min_periods=WDAYS).mean()
    b = (2.0 * np.log(2.0) - 1.0) * (lco ** 2).rolling(MDAYS, min_periods=WDAYS).mean()
    gk = a - b
    return par - gk


def f37_rges_045_parkinson_minus_gk_var_63d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Parkinson var − Garman-Klass var, 63d — quarterly bar-shape divergence."""
    lhl = _safe_log(high) - _safe_log(low)
    lco = _safe_log(close) - _safe_log(open_)
    par = (lhl ** 2).rolling(QDAYS, min_periods=MDAYS).mean() / (4.0 * np.log(2.0))
    a = 0.5 * (lhl ** 2).rolling(QDAYS, min_periods=MDAYS).mean()
    b = (2.0 * np.log(2.0) - 1.0) * (lco ** 2).rolling(QDAYS, min_periods=MDAYS).mean()
    gk = a - b
    return par - gk


def f37_rges_046_gk_minus_rs_var_21d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Garman-Klass var − Rogers-Satchell var, 21d — drift impact differential."""
    lhl = _safe_log(high) - _safe_log(low)
    lco = _safe_log(close) - _safe_log(open_)
    a = 0.5 * (lhl ** 2).rolling(MDAYS, min_periods=WDAYS).mean()
    b = (2.0 * np.log(2.0) - 1.0) * (lco ** 2).rolling(MDAYS, min_periods=WDAYS).mean()
    gk = a - b
    lho = _safe_log(high) - _safe_log(open_)
    lhc = _safe_log(high) - _safe_log(close)
    llo = _safe_log(low) - _safe_log(open_)
    llc = _safe_log(low) - _safe_log(close)
    rs = (lhc * lho + llc * llo).rolling(MDAYS, min_periods=WDAYS).mean()
    return gk - rs


def f37_rges_047_gk_minus_rs_var_63d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Garman-Klass var − Rogers-Satchell var, 63d."""
    lhl = _safe_log(high) - _safe_log(low)
    lco = _safe_log(close) - _safe_log(open_)
    a = 0.5 * (lhl ** 2).rolling(QDAYS, min_periods=MDAYS).mean()
    b = (2.0 * np.log(2.0) - 1.0) * (lco ** 2).rolling(QDAYS, min_periods=MDAYS).mean()
    gk = a - b
    lho = _safe_log(high) - _safe_log(open_)
    lhc = _safe_log(high) - _safe_log(close)
    llo = _safe_log(low) - _safe_log(open_)
    llc = _safe_log(low) - _safe_log(close)
    rs = (lhc * lho + llc * llo).rolling(QDAYS, min_periods=MDAYS).mean()
    return gk - rs


def f37_rges_048_yz_minus_rs_var_63d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Yang-Zhang var − Rogers-Satchell var, 63d — overnight + drift contribution magnitude."""
    yz = _yang_zhang_var(open_, high, low, close, QDAYS, MDAYS)
    lho = _safe_log(high) - _safe_log(open_)
    lhc = _safe_log(high) - _safe_log(close)
    llo = _safe_log(low) - _safe_log(open_)
    llc = _safe_log(low) - _safe_log(close)
    rs = (lhc * lho + llc * llo).rolling(QDAYS, min_periods=MDAYS).mean()
    return yz - rs


def f37_rges_049_parkinson_minus_rs_var_63d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Parkinson var − Rogers-Satchell var, 63d — pure range vs drift-free range."""
    lhl = _safe_log(high) - _safe_log(low)
    par = (lhl ** 2).rolling(QDAYS, min_periods=MDAYS).mean() / (4.0 * np.log(2.0))
    lho = _safe_log(high) - _safe_log(open_)
    lhc = _safe_log(high) - _safe_log(close)
    llo = _safe_log(low) - _safe_log(open_)
    llc = _safe_log(low) - _safe_log(close)
    rs = (lhc * lho + llc * llo).rolling(QDAYS, min_periods=MDAYS).mean()
    return par - rs


def f37_rges_050_yz_minus_gk_var_63d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Yang-Zhang var − Garman-Klass var, 63d — overnight contribution highlighted."""
    yz = _yang_zhang_var(open_, high, low, close, QDAYS, MDAYS)
    lhl = _safe_log(high) - _safe_log(low)
    lco = _safe_log(close) - _safe_log(open_)
    a = 0.5 * (lhl ** 2).rolling(QDAYS, min_periods=MDAYS).mean()
    b = (2.0 * np.log(2.0) - 1.0) * (lco ** 2).rolling(QDAYS, min_periods=MDAYS).mean()
    gk = a - b
    return yz - gk


def f37_rges_051_parkinson_over_rs_ratio_63d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio: Parkinson var / Rogers-Satchell var, 63d — drift-impact diagnostic."""
    lhl = _safe_log(high) - _safe_log(low)
    par = (lhl ** 2).rolling(QDAYS, min_periods=MDAYS).mean() / (4.0 * np.log(2.0))
    lho = _safe_log(high) - _safe_log(open_)
    lhc = _safe_log(high) - _safe_log(close)
    llo = _safe_log(low) - _safe_log(open_)
    llc = _safe_log(low) - _safe_log(close)
    rs = (lhc * lho + llc * llo).rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(par, rs)


def f37_rges_052_gkyz_minus_gk_var_63d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """GKYZ var − GK var, 63d — isolates the overnight gap variance component."""
    gkyz = _gkyz_var(open_, high, low, close, QDAYS, MDAYS)
    lhl = _safe_log(high) - _safe_log(low)
    lco = _safe_log(close) - _safe_log(open_)
    a = 0.5 * (lhl ** 2).rolling(QDAYS, min_periods=MDAYS).mean()
    b = (2.0 * np.log(2.0) - 1.0) * (lco ** 2).rolling(QDAYS, min_periods=MDAYS).mean()
    gk = a - b
    return gkyz - gk


def f37_rges_053_estimator_dispersion_5way_63d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Std-dev across 5 estimator variances (P, GK, RS, YZ, GKYZ) at 63d — disagreement signal."""
    lhl = _safe_log(high) - _safe_log(low)
    lco = _safe_log(close) - _safe_log(open_)
    par = (lhl ** 2).rolling(QDAYS, min_periods=MDAYS).mean() / (4.0 * np.log(2.0))
    a = 0.5 * (lhl ** 2).rolling(QDAYS, min_periods=MDAYS).mean()
    b = (2.0 * np.log(2.0) - 1.0) * (lco ** 2).rolling(QDAYS, min_periods=MDAYS).mean()
    gk = a - b
    lho = _safe_log(high) - _safe_log(open_)
    lhc = _safe_log(high) - _safe_log(close)
    llo = _safe_log(low) - _safe_log(open_)
    llc = _safe_log(low) - _safe_log(close)
    rs = (lhc * lho + llc * llo).rolling(QDAYS, min_periods=MDAYS).mean()
    yz = _yang_zhang_var(open_, high, low, close, QDAYS, MDAYS)
    gkyz = _gkyz_var(open_, high, low, close, QDAYS, MDAYS)
    df = pd.concat([par.rename("p"), gk.rename("gk"), rs.rename("rs"), yz.rename("yz"), gkyz.rename("gkyz")], axis=1)
    return df.std(axis=1)


# ============================================================
# Bucket H — Raw daily range / close (054-059)
# ============================================================

def f37_rges_054_log_high_low_ratio_daily(high: pd.Series, low: pd.Series) -> pd.Series:
    """Daily log(H/L) — single-bar range magnitude (not squared, not averaged)."""
    return _safe_log(high) - _safe_log(low)


def f37_rges_055_high_low_over_close_daily(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Daily (H-L)/C — single-bar range normalized by close, raw scale."""
    return _safe_div(high - low, close)


def f37_rges_056_mean_log_hl_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean of daily log(H/L) over 21d — raw range magnitude regime, not squared."""
    lhl = _safe_log(high) - _safe_log(low)
    return lhl.rolling(MDAYS, min_periods=WDAYS).mean()


def f37_rges_057_mean_log_hl_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean of daily log(H/L) over 63d — quarterly raw range magnitude regime."""
    lhl = _safe_log(high) - _safe_log(low)
    return lhl.rolling(QDAYS, min_periods=MDAYS).mean()


def f37_rges_058_mean_hl_over_close_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean of (H-L)/C over 63d — non-log range/close measure (linear scale)."""
    return _safe_div(high - low, close).rolling(QDAYS, min_periods=MDAYS).mean()


def f37_rges_059_max_log_hl_in_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Max single-day log(H/L) in trailing 63d — extreme single-bar range observed."""
    lhl = _safe_log(high) - _safe_log(low)
    return lhl.rolling(QDAYS, min_periods=MDAYS).max()


# ============================================================
# Bucket I — Range percentile / rank (060-067)
# ============================================================

def _pct_rank(w):
    if np.isnan(w).all():
        return np.nan
    last = w[-1]
    if np.isnan(last):
        return np.nan
    v = w[~np.isnan(w)]
    if v.size == 0:
        return np.nan
    return float((v <= last).sum()) / float(v.size)


def f37_rges_060_pct_rank_log_hl_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's log(H/L) percentile rank in trailing 252d distribution."""
    lhl = _safe_log(high) - _safe_log(low)
    return lhl.rolling(YDAYS, min_periods=QDAYS).apply(_pct_rank, raw=True)


def f37_rges_061_pct_rank_log_hl_504d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's log(H/L) percentile rank in trailing 504d (2y) distribution."""
    lhl = _safe_log(high) - _safe_log(low)
    return lhl.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_pct_rank, raw=True)


def f37_rges_062_pct_rank_parkinson_21d_in_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Parkinson 21d variance percentile rank within 252d cone — range-vol cone position."""
    lhl = _safe_log(high) - _safe_log(low)
    par = (lhl ** 2).rolling(MDAYS, min_periods=WDAYS).mean() / (4.0 * np.log(2.0))
    return par.rolling(YDAYS, min_periods=QDAYS).apply(_pct_rank, raw=True)


def f37_rges_063_pct_rank_parkinson_63d_in_504d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Parkinson 63d variance percentile rank within 504d cone — long-cone position."""
    lhl = _safe_log(high) - _safe_log(low)
    par = (lhl ** 2).rolling(QDAYS, min_periods=MDAYS).mean() / (4.0 * np.log(2.0))
    return par.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_pct_rank, raw=True)


def f37_rges_064_zscore_log_hl_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of today's log(H/L) in 252d distribution — standardized range extremity."""
    lhl = _safe_log(high) - _safe_log(low)
    return _rolling_zscore(lhl, YDAYS, min_periods=QDAYS)


def f37_rges_065_zscore_parkinson_21d_in_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of Parkinson 21d variance vs its own 252d distribution."""
    lhl = _safe_log(high) - _safe_log(low)
    par = (lhl ** 2).rolling(MDAYS, min_periods=WDAYS).mean() / (4.0 * np.log(2.0))
    return _rolling_zscore(par, YDAYS, min_periods=QDAYS)


def f37_rges_066_pct_rank_rs_var_63d_in_252d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rogers-Satchell 63d variance percentile rank in 252d — drift-free vol cone."""
    lho = _safe_log(high) - _safe_log(open_)
    lhc = _safe_log(high) - _safe_log(close)
    llo = _safe_log(low) - _safe_log(open_)
    llc = _safe_log(low) - _safe_log(close)
    rs = (lhc * lho + llc * llo).rolling(QDAYS, min_periods=MDAYS).mean()
    return rs.rolling(YDAYS, min_periods=QDAYS).apply(_pct_rank, raw=True)


def f37_rges_067_pct_rank_yz_var_63d_in_504d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Yang-Zhang 63d variance percentile rank in 504d — composite vol cone position."""
    yz = _yang_zhang_var(open_, high, low, close, QDAYS, MDAYS)
    return yz.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_pct_rank, raw=True)


# ============================================================
# Bucket J — Range expansion regimes (068-075)
# ============================================================

def f37_rges_068_today_log_hl_over_mean_log_hl_5d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's log(H/L) divided by mean log(H/L) over trailing 5d — micro expansion."""
    lhl = _safe_log(high) - _safe_log(low)
    return _safe_div(lhl, lhl.rolling(WDAYS, min_periods=2).mean())


def f37_rges_069_today_log_hl_over_mean_log_hl_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's log(H/L) divided by mean log(H/L) over trailing 21d — monthly expansion."""
    lhl = _safe_log(high) - _safe_log(low)
    return _safe_div(lhl, lhl.rolling(MDAYS, min_periods=WDAYS).mean())


def f37_rges_070_today_log_hl_over_mean_log_hl_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's log(H/L) divided by mean log(H/L) over trailing 63d — quarterly expansion."""
    lhl = _safe_log(high) - _safe_log(low)
    return _safe_div(lhl, lhl.rolling(QDAYS, min_periods=MDAYS).mean())


def f37_rges_071_today_log_hl_over_mean_log_hl_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's log(H/L) divided by mean log(H/L) over trailing 252d — annual baseline expansion."""
    lhl = _safe_log(high) - _safe_log(low)
    return _safe_div(lhl, lhl.rolling(YDAYS, min_periods=QDAYS).mean())


def f37_rges_072_parkinson_21d_over_parkinson_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Parkinson 21d / Parkinson 252d — short-term range-vol expansion vs annual base."""
    lhl = _safe_log(high) - _safe_log(low)
    p21 = (lhl ** 2).rolling(MDAYS, min_periods=WDAYS).mean() / (4.0 * np.log(2.0))
    p252 = (lhl ** 2).rolling(YDAYS, min_periods=QDAYS).mean() / (4.0 * np.log(2.0))
    return _safe_div(p21, p252)


def f37_rges_073_parkinson_63d_over_parkinson_504d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Parkinson 63d / Parkinson 504d — quarterly vs biennial range expansion."""
    lhl = _safe_log(high) - _safe_log(low)
    p63 = (lhl ** 2).rolling(QDAYS, min_periods=MDAYS).mean() / (4.0 * np.log(2.0))
    p504 = (lhl ** 2).rolling(DDAYS_2Y, min_periods=YDAYS).mean() / (4.0 * np.log(2.0))
    return _safe_div(p63, p504)


def f37_rges_074_count_bars_log_hl_above_2x_21d_mean_in_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of bars in last 21d where log(H/L) > 2 × trailing-21d mean — expansion event count."""
    lhl = _safe_log(high) - _safe_log(low)
    base = lhl.rolling(MDAYS, min_periods=WDAYS).mean()
    big = (lhl > 2.0 * base).astype(float)
    return big.rolling(MDAYS, min_periods=WDAYS).sum()


def f37_rges_075_mean_log_hl_5d_over_mean_log_hl_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean log(H/L) 5d / mean log(H/L) 63d — fast-vs-slow range expansion ratio."""
    lhl = _safe_log(high) - _safe_log(low)
    return _safe_div(lhl.rolling(WDAYS, min_periods=2).mean(), lhl.rolling(QDAYS, min_periods=MDAYS).mean())


# ============================================================
#                         REGISTRY 001-075
# ============================================================



def f37_rges_001_parkinson_var_5d_d3(high, low):
    return f37_rges_001_parkinson_var_5d(high, low).diff().diff().diff()


def f37_rges_002_parkinson_var_21d_d3(high, low):
    return f37_rges_002_parkinson_var_21d(high, low).diff().diff().diff()


def f37_rges_003_parkinson_var_63d_d3(high, low):
    return f37_rges_003_parkinson_var_63d(high, low).diff().diff().diff()


def f37_rges_004_parkinson_var_126d_d3(high, low):
    return f37_rges_004_parkinson_var_126d(high, low).diff().diff().diff()


def f37_rges_005_parkinson_var_252d_d3(high, low):
    return f37_rges_005_parkinson_var_252d(high, low).diff().diff().diff()


def f37_rges_006_parkinson_var_504d_d3(high, low):
    return f37_rges_006_parkinson_var_504d(high, low).diff().diff().diff()


def f37_rges_007_parkinson_sigma_annualized_21d_d3(high, low):
    return f37_rges_007_parkinson_sigma_annualized_21d(high, low).diff().diff().diff()


def f37_rges_008_parkinson_sigma_annualized_63d_d3(high, low):
    return f37_rges_008_parkinson_sigma_annualized_63d(high, low).diff().diff().diff()


def f37_rges_009_garman_klass_var_5d_d3(open_, high, low, close):
    return f37_rges_009_garman_klass_var_5d(open_, high, low, close).diff().diff().diff()


def f37_rges_010_garman_klass_var_21d_d3(open_, high, low, close):
    return f37_rges_010_garman_klass_var_21d(open_, high, low, close).diff().diff().diff()


def f37_rges_011_garman_klass_var_63d_d3(open_, high, low, close):
    return f37_rges_011_garman_klass_var_63d(open_, high, low, close).diff().diff().diff()


def f37_rges_012_garman_klass_var_126d_d3(open_, high, low, close):
    return f37_rges_012_garman_klass_var_126d(open_, high, low, close).diff().diff().diff()


def f37_rges_013_garman_klass_var_252d_d3(open_, high, low, close):
    return f37_rges_013_garman_klass_var_252d(open_, high, low, close).diff().diff().diff()


def f37_rges_014_garman_klass_var_504d_d3(open_, high, low, close):
    return f37_rges_014_garman_klass_var_504d(open_, high, low, close).diff().diff().diff()


def f37_rges_015_garman_klass_sigma_annualized_21d_d3(open_, high, low, close):
    return f37_rges_015_garman_klass_sigma_annualized_21d(open_, high, low, close).diff().diff().diff()


def f37_rges_016_garman_klass_sigma_annualized_63d_d3(open_, high, low, close):
    return f37_rges_016_garman_klass_sigma_annualized_63d(open_, high, low, close).diff().diff().diff()


def f37_rges_017_rogers_satchell_var_5d_d3(open_, high, low, close):
    return f37_rges_017_rogers_satchell_var_5d(open_, high, low, close).diff().diff().diff()


def f37_rges_018_rogers_satchell_var_21d_d3(open_, high, low, close):
    return f37_rges_018_rogers_satchell_var_21d(open_, high, low, close).diff().diff().diff()


def f37_rges_019_rogers_satchell_var_63d_d3(open_, high, low, close):
    return f37_rges_019_rogers_satchell_var_63d(open_, high, low, close).diff().diff().diff()


def f37_rges_020_rogers_satchell_var_126d_d3(open_, high, low, close):
    return f37_rges_020_rogers_satchell_var_126d(open_, high, low, close).diff().diff().diff()


def f37_rges_021_rogers_satchell_var_252d_d3(open_, high, low, close):
    return f37_rges_021_rogers_satchell_var_252d(open_, high, low, close).diff().diff().diff()


def f37_rges_022_rogers_satchell_var_504d_d3(open_, high, low, close):
    return f37_rges_022_rogers_satchell_var_504d(open_, high, low, close).diff().diff().diff()


def f37_rges_023_rogers_satchell_sigma_annualized_21d_d3(open_, high, low, close):
    return f37_rges_023_rogers_satchell_sigma_annualized_21d(open_, high, low, close).diff().diff().diff()


def f37_rges_024_rogers_satchell_sigma_annualized_63d_d3(open_, high, low, close):
    return f37_rges_024_rogers_satchell_sigma_annualized_63d(open_, high, low, close).diff().diff().diff()


def f37_rges_025_yang_zhang_var_21d_d3(open_, high, low, close):
    return f37_rges_025_yang_zhang_var_21d(open_, high, low, close).diff().diff().diff()


def f37_rges_026_yang_zhang_var_63d_d3(open_, high, low, close):
    return f37_rges_026_yang_zhang_var_63d(open_, high, low, close).diff().diff().diff()


def f37_rges_027_yang_zhang_var_126d_d3(open_, high, low, close):
    return f37_rges_027_yang_zhang_var_126d(open_, high, low, close).diff().diff().diff()


def f37_rges_028_yang_zhang_var_252d_d3(open_, high, low, close):
    return f37_rges_028_yang_zhang_var_252d(open_, high, low, close).diff().diff().diff()


def f37_rges_029_yang_zhang_var_504d_d3(open_, high, low, close):
    return f37_rges_029_yang_zhang_var_504d(open_, high, low, close).diff().diff().diff()


def f37_rges_030_yang_zhang_sigma_annualized_63d_d3(open_, high, low, close):
    return f37_rges_030_yang_zhang_sigma_annualized_63d(open_, high, low, close).diff().diff().diff()


def f37_rges_031_yang_zhang_overnight_component_63d_d3(open_, close):
    return f37_rges_031_yang_zhang_overnight_component_63d(open_, close).diff().diff().diff()


def f37_rges_032_yang_zhang_open_to_close_component_63d_d3(open_, close):
    return f37_rges_032_yang_zhang_open_to_close_component_63d(open_, close).diff().diff().diff()


def f37_rges_033_gkyz_var_21d_d3(open_, high, low, close):
    return f37_rges_033_gkyz_var_21d(open_, high, low, close).diff().diff().diff()


def f37_rges_034_gkyz_var_63d_d3(open_, high, low, close):
    return f37_rges_034_gkyz_var_63d(open_, high, low, close).diff().diff().diff()


def f37_rges_035_gkyz_var_126d_d3(open_, high, low, close):
    return f37_rges_035_gkyz_var_126d(open_, high, low, close).diff().diff().diff()


def f37_rges_036_gkyz_var_252d_d3(open_, high, low, close):
    return f37_rges_036_gkyz_var_252d(open_, high, low, close).diff().diff().diff()


def f37_rges_037_gkyz_var_504d_d3(open_, high, low, close):
    return f37_rges_037_gkyz_var_504d(open_, high, low, close).diff().diff().diff()


def f37_rges_038_parkinson_to_cc_ratio_21d_d3(high, low, close):
    return f37_rges_038_parkinson_to_cc_ratio_21d(high, low, close).diff().diff().diff()


def f37_rges_039_parkinson_to_cc_ratio_63d_d3(high, low, close):
    return f37_rges_039_parkinson_to_cc_ratio_63d(high, low, close).diff().diff().diff()


def f37_rges_040_parkinson_to_cc_ratio_126d_d3(high, low, close):
    return f37_rges_040_parkinson_to_cc_ratio_126d(high, low, close).diff().diff().diff()


def f37_rges_041_parkinson_to_cc_ratio_252d_d3(high, low, close):
    return f37_rges_041_parkinson_to_cc_ratio_252d(high, low, close).diff().diff().diff()


def f37_rges_042_garman_klass_to_cc_ratio_63d_d3(open_, high, low, close):
    return f37_rges_042_garman_klass_to_cc_ratio_63d(open_, high, low, close).diff().diff().diff()


def f37_rges_043_rogers_satchell_to_cc_ratio_63d_d3(open_, high, low, close):
    return f37_rges_043_rogers_satchell_to_cc_ratio_63d(open_, high, low, close).diff().diff().diff()


def f37_rges_044_parkinson_minus_gk_var_21d_d3(open_, high, low, close):
    return f37_rges_044_parkinson_minus_gk_var_21d(open_, high, low, close).diff().diff().diff()


def f37_rges_045_parkinson_minus_gk_var_63d_d3(open_, high, low, close):
    return f37_rges_045_parkinson_minus_gk_var_63d(open_, high, low, close).diff().diff().diff()


def f37_rges_046_gk_minus_rs_var_21d_d3(open_, high, low, close):
    return f37_rges_046_gk_minus_rs_var_21d(open_, high, low, close).diff().diff().diff()


def f37_rges_047_gk_minus_rs_var_63d_d3(open_, high, low, close):
    return f37_rges_047_gk_minus_rs_var_63d(open_, high, low, close).diff().diff().diff()


def f37_rges_048_yz_minus_rs_var_63d_d3(open_, high, low, close):
    return f37_rges_048_yz_minus_rs_var_63d(open_, high, low, close).diff().diff().diff()


def f37_rges_049_parkinson_minus_rs_var_63d_d3(open_, high, low, close):
    return f37_rges_049_parkinson_minus_rs_var_63d(open_, high, low, close).diff().diff().diff()


def f37_rges_050_yz_minus_gk_var_63d_d3(open_, high, low, close):
    return f37_rges_050_yz_minus_gk_var_63d(open_, high, low, close).diff().diff().diff()


def f37_rges_051_parkinson_over_rs_ratio_63d_d3(open_, high, low, close):
    return f37_rges_051_parkinson_over_rs_ratio_63d(open_, high, low, close).diff().diff().diff()


def f37_rges_052_gkyz_minus_gk_var_63d_d3(open_, high, low, close):
    return f37_rges_052_gkyz_minus_gk_var_63d(open_, high, low, close).diff().diff().diff()


def f37_rges_053_estimator_dispersion_5way_63d_d3(open_, high, low, close):
    return f37_rges_053_estimator_dispersion_5way_63d(open_, high, low, close).diff().diff().diff()


def f37_rges_054_log_high_low_ratio_daily_d3(high, low):
    return f37_rges_054_log_high_low_ratio_daily(high, low).diff().diff().diff()


def f37_rges_055_high_low_over_close_daily_d3(high, low, close):
    return f37_rges_055_high_low_over_close_daily(high, low, close).diff().diff().diff()


def f37_rges_056_mean_log_hl_21d_d3(high, low):
    return f37_rges_056_mean_log_hl_21d(high, low).diff().diff().diff()


def f37_rges_057_mean_log_hl_63d_d3(high, low):
    return f37_rges_057_mean_log_hl_63d(high, low).diff().diff().diff()


def f37_rges_058_mean_hl_over_close_63d_d3(high, low, close):
    return f37_rges_058_mean_hl_over_close_63d(high, low, close).diff().diff().diff()


def f37_rges_059_max_log_hl_in_63d_d3(high, low):
    return f37_rges_059_max_log_hl_in_63d(high, low).diff().diff().diff()


def f37_rges_060_pct_rank_log_hl_252d_d3(high, low):
    return f37_rges_060_pct_rank_log_hl_252d(high, low).diff().diff().diff()


def f37_rges_061_pct_rank_log_hl_504d_d3(high, low):
    return f37_rges_061_pct_rank_log_hl_504d(high, low).diff().diff().diff()


def f37_rges_062_pct_rank_parkinson_21d_in_252d_d3(high, low):
    return f37_rges_062_pct_rank_parkinson_21d_in_252d(high, low).diff().diff().diff()


def f37_rges_063_pct_rank_parkinson_63d_in_504d_d3(high, low):
    return f37_rges_063_pct_rank_parkinson_63d_in_504d(high, low).diff().diff().diff()


def f37_rges_064_zscore_log_hl_252d_d3(high, low):
    return f37_rges_064_zscore_log_hl_252d(high, low).diff().diff().diff()


def f37_rges_065_zscore_parkinson_21d_in_252d_d3(high, low):
    return f37_rges_065_zscore_parkinson_21d_in_252d(high, low).diff().diff().diff()


def f37_rges_066_pct_rank_rs_var_63d_in_252d_d3(open_, high, low, close):
    return f37_rges_066_pct_rank_rs_var_63d_in_252d(open_, high, low, close).diff().diff().diff()


def f37_rges_067_pct_rank_yz_var_63d_in_504d_d3(open_, high, low, close):
    return f37_rges_067_pct_rank_yz_var_63d_in_504d(open_, high, low, close).diff().diff().diff()


def f37_rges_068_today_log_hl_over_mean_log_hl_5d_d3(high, low):
    return f37_rges_068_today_log_hl_over_mean_log_hl_5d(high, low).diff().diff().diff()


def f37_rges_069_today_log_hl_over_mean_log_hl_21d_d3(high, low):
    return f37_rges_069_today_log_hl_over_mean_log_hl_21d(high, low).diff().diff().diff()


def f37_rges_070_today_log_hl_over_mean_log_hl_63d_d3(high, low):
    return f37_rges_070_today_log_hl_over_mean_log_hl_63d(high, low).diff().diff().diff()


def f37_rges_071_today_log_hl_over_mean_log_hl_252d_d3(high, low):
    return f37_rges_071_today_log_hl_over_mean_log_hl_252d(high, low).diff().diff().diff()


def f37_rges_072_parkinson_21d_over_parkinson_252d_d3(high, low):
    return f37_rges_072_parkinson_21d_over_parkinson_252d(high, low).diff().diff().diff()


def f37_rges_073_parkinson_63d_over_parkinson_504d_d3(high, low):
    return f37_rges_073_parkinson_63d_over_parkinson_504d(high, low).diff().diff().diff()


def f37_rges_074_count_bars_log_hl_above_2x_21d_mean_in_21d_d3(high, low):
    return f37_rges_074_count_bars_log_hl_above_2x_21d_mean_in_21d(high, low).diff().diff().diff()


def f37_rges_075_mean_log_hl_5d_over_mean_log_hl_63d_d3(high, low):
    return f37_rges_075_mean_log_hl_5d_over_mean_log_hl_63d(high, low).diff().diff().diff()


RANGE_ESTIMATORS_FAMILY_D3_REGISTRY_001_075 = {
    "f37_rges_001_parkinson_var_5d_d3": {"inputs": ["high", "low"], "func": f37_rges_001_parkinson_var_5d_d3},
    "f37_rges_002_parkinson_var_21d_d3": {"inputs": ["high", "low"], "func": f37_rges_002_parkinson_var_21d_d3},
    "f37_rges_003_parkinson_var_63d_d3": {"inputs": ["high", "low"], "func": f37_rges_003_parkinson_var_63d_d3},
    "f37_rges_004_parkinson_var_126d_d3": {"inputs": ["high", "low"], "func": f37_rges_004_parkinson_var_126d_d3},
    "f37_rges_005_parkinson_var_252d_d3": {"inputs": ["high", "low"], "func": f37_rges_005_parkinson_var_252d_d3},
    "f37_rges_006_parkinson_var_504d_d3": {"inputs": ["high", "low"], "func": f37_rges_006_parkinson_var_504d_d3},
    "f37_rges_007_parkinson_sigma_annualized_21d_d3": {"inputs": ["high", "low"], "func": f37_rges_007_parkinson_sigma_annualized_21d_d3},
    "f37_rges_008_parkinson_sigma_annualized_63d_d3": {"inputs": ["high", "low"], "func": f37_rges_008_parkinson_sigma_annualized_63d_d3},
    "f37_rges_009_garman_klass_var_5d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_009_garman_klass_var_5d_d3},
    "f37_rges_010_garman_klass_var_21d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_010_garman_klass_var_21d_d3},
    "f37_rges_011_garman_klass_var_63d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_011_garman_klass_var_63d_d3},
    "f37_rges_012_garman_klass_var_126d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_012_garman_klass_var_126d_d3},
    "f37_rges_013_garman_klass_var_252d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_013_garman_klass_var_252d_d3},
    "f37_rges_014_garman_klass_var_504d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_014_garman_klass_var_504d_d3},
    "f37_rges_015_garman_klass_sigma_annualized_21d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_015_garman_klass_sigma_annualized_21d_d3},
    "f37_rges_016_garman_klass_sigma_annualized_63d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_016_garman_klass_sigma_annualized_63d_d3},
    "f37_rges_017_rogers_satchell_var_5d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_017_rogers_satchell_var_5d_d3},
    "f37_rges_018_rogers_satchell_var_21d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_018_rogers_satchell_var_21d_d3},
    "f37_rges_019_rogers_satchell_var_63d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_019_rogers_satchell_var_63d_d3},
    "f37_rges_020_rogers_satchell_var_126d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_020_rogers_satchell_var_126d_d3},
    "f37_rges_021_rogers_satchell_var_252d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_021_rogers_satchell_var_252d_d3},
    "f37_rges_022_rogers_satchell_var_504d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_022_rogers_satchell_var_504d_d3},
    "f37_rges_023_rogers_satchell_sigma_annualized_21d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_023_rogers_satchell_sigma_annualized_21d_d3},
    "f37_rges_024_rogers_satchell_sigma_annualized_63d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_024_rogers_satchell_sigma_annualized_63d_d3},
    "f37_rges_025_yang_zhang_var_21d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_025_yang_zhang_var_21d_d3},
    "f37_rges_026_yang_zhang_var_63d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_026_yang_zhang_var_63d_d3},
    "f37_rges_027_yang_zhang_var_126d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_027_yang_zhang_var_126d_d3},
    "f37_rges_028_yang_zhang_var_252d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_028_yang_zhang_var_252d_d3},
    "f37_rges_029_yang_zhang_var_504d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_029_yang_zhang_var_504d_d3},
    "f37_rges_030_yang_zhang_sigma_annualized_63d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_030_yang_zhang_sigma_annualized_63d_d3},
    "f37_rges_031_yang_zhang_overnight_component_63d_d3": {"inputs": ["open", "close"], "func": f37_rges_031_yang_zhang_overnight_component_63d_d3},
    "f37_rges_032_yang_zhang_open_to_close_component_63d_d3": {"inputs": ["open", "close"], "func": f37_rges_032_yang_zhang_open_to_close_component_63d_d3},
    "f37_rges_033_gkyz_var_21d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_033_gkyz_var_21d_d3},
    "f37_rges_034_gkyz_var_63d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_034_gkyz_var_63d_d3},
    "f37_rges_035_gkyz_var_126d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_035_gkyz_var_126d_d3},
    "f37_rges_036_gkyz_var_252d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_036_gkyz_var_252d_d3},
    "f37_rges_037_gkyz_var_504d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_037_gkyz_var_504d_d3},
    "f37_rges_038_parkinson_to_cc_ratio_21d_d3": {"inputs": ["high", "low", "close"], "func": f37_rges_038_parkinson_to_cc_ratio_21d_d3},
    "f37_rges_039_parkinson_to_cc_ratio_63d_d3": {"inputs": ["high", "low", "close"], "func": f37_rges_039_parkinson_to_cc_ratio_63d_d3},
    "f37_rges_040_parkinson_to_cc_ratio_126d_d3": {"inputs": ["high", "low", "close"], "func": f37_rges_040_parkinson_to_cc_ratio_126d_d3},
    "f37_rges_041_parkinson_to_cc_ratio_252d_d3": {"inputs": ["high", "low", "close"], "func": f37_rges_041_parkinson_to_cc_ratio_252d_d3},
    "f37_rges_042_garman_klass_to_cc_ratio_63d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_042_garman_klass_to_cc_ratio_63d_d3},
    "f37_rges_043_rogers_satchell_to_cc_ratio_63d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_043_rogers_satchell_to_cc_ratio_63d_d3},
    "f37_rges_044_parkinson_minus_gk_var_21d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_044_parkinson_minus_gk_var_21d_d3},
    "f37_rges_045_parkinson_minus_gk_var_63d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_045_parkinson_minus_gk_var_63d_d3},
    "f37_rges_046_gk_minus_rs_var_21d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_046_gk_minus_rs_var_21d_d3},
    "f37_rges_047_gk_minus_rs_var_63d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_047_gk_minus_rs_var_63d_d3},
    "f37_rges_048_yz_minus_rs_var_63d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_048_yz_minus_rs_var_63d_d3},
    "f37_rges_049_parkinson_minus_rs_var_63d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_049_parkinson_minus_rs_var_63d_d3},
    "f37_rges_050_yz_minus_gk_var_63d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_050_yz_minus_gk_var_63d_d3},
    "f37_rges_051_parkinson_over_rs_ratio_63d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_051_parkinson_over_rs_ratio_63d_d3},
    "f37_rges_052_gkyz_minus_gk_var_63d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_052_gkyz_minus_gk_var_63d_d3},
    "f37_rges_053_estimator_dispersion_5way_63d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_053_estimator_dispersion_5way_63d_d3},
    "f37_rges_054_log_high_low_ratio_daily_d3": {"inputs": ["high", "low"], "func": f37_rges_054_log_high_low_ratio_daily_d3},
    "f37_rges_055_high_low_over_close_daily_d3": {"inputs": ["high", "low", "close"], "func": f37_rges_055_high_low_over_close_daily_d3},
    "f37_rges_056_mean_log_hl_21d_d3": {"inputs": ["high", "low"], "func": f37_rges_056_mean_log_hl_21d_d3},
    "f37_rges_057_mean_log_hl_63d_d3": {"inputs": ["high", "low"], "func": f37_rges_057_mean_log_hl_63d_d3},
    "f37_rges_058_mean_hl_over_close_63d_d3": {"inputs": ["high", "low", "close"], "func": f37_rges_058_mean_hl_over_close_63d_d3},
    "f37_rges_059_max_log_hl_in_63d_d3": {"inputs": ["high", "low"], "func": f37_rges_059_max_log_hl_in_63d_d3},
    "f37_rges_060_pct_rank_log_hl_252d_d3": {"inputs": ["high", "low"], "func": f37_rges_060_pct_rank_log_hl_252d_d3},
    "f37_rges_061_pct_rank_log_hl_504d_d3": {"inputs": ["high", "low"], "func": f37_rges_061_pct_rank_log_hl_504d_d3},
    "f37_rges_062_pct_rank_parkinson_21d_in_252d_d3": {"inputs": ["high", "low"], "func": f37_rges_062_pct_rank_parkinson_21d_in_252d_d3},
    "f37_rges_063_pct_rank_parkinson_63d_in_504d_d3": {"inputs": ["high", "low"], "func": f37_rges_063_pct_rank_parkinson_63d_in_504d_d3},
    "f37_rges_064_zscore_log_hl_252d_d3": {"inputs": ["high", "low"], "func": f37_rges_064_zscore_log_hl_252d_d3},
    "f37_rges_065_zscore_parkinson_21d_in_252d_d3": {"inputs": ["high", "low"], "func": f37_rges_065_zscore_parkinson_21d_in_252d_d3},
    "f37_rges_066_pct_rank_rs_var_63d_in_252d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_066_pct_rank_rs_var_63d_in_252d_d3},
    "f37_rges_067_pct_rank_yz_var_63d_in_504d_d3": {"inputs": ["open", "high", "low", "close"], "func": f37_rges_067_pct_rank_yz_var_63d_in_504d_d3},
    "f37_rges_068_today_log_hl_over_mean_log_hl_5d_d3": {"inputs": ["high", "low"], "func": f37_rges_068_today_log_hl_over_mean_log_hl_5d_d3},
    "f37_rges_069_today_log_hl_over_mean_log_hl_21d_d3": {"inputs": ["high", "low"], "func": f37_rges_069_today_log_hl_over_mean_log_hl_21d_d3},
    "f37_rges_070_today_log_hl_over_mean_log_hl_63d_d3": {"inputs": ["high", "low"], "func": f37_rges_070_today_log_hl_over_mean_log_hl_63d_d3},
    "f37_rges_071_today_log_hl_over_mean_log_hl_252d_d3": {"inputs": ["high", "low"], "func": f37_rges_071_today_log_hl_over_mean_log_hl_252d_d3},
    "f37_rges_072_parkinson_21d_over_parkinson_252d_d3": {"inputs": ["high", "low"], "func": f37_rges_072_parkinson_21d_over_parkinson_252d_d3},
    "f37_rges_073_parkinson_63d_over_parkinson_504d_d3": {"inputs": ["high", "low"], "func": f37_rges_073_parkinson_63d_over_parkinson_504d_d3},
    "f37_rges_074_count_bars_log_hl_above_2x_21d_mean_in_21d_d3": {"inputs": ["high", "low"], "func": f37_rges_074_count_bars_log_hl_above_2x_21d_mean_in_21d_d3},
    "f37_rges_075_mean_log_hl_5d_over_mean_log_hl_63d_d3": {"inputs": ["high", "low"], "func": f37_rges_075_mean_log_hl_5d_over_mean_log_hl_63d_d3},
}
