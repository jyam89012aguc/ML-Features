"""
31_oscillator_extremes — 3rd Derivatives (Features osc_drv3_001-025)
Domain: rate of change of 2nd-derivative oscillator features — acceleration of velocity
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
Covers acceleration of: Stochastic, Williams %R, CCI, MFI, StochRSI,
CMO, TRIX, Fisher, PPO, KST, Coppock, SMI, Klinger, RVI, Awesome Oscillator.
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


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _stoch_k(high: pd.Series, low: pd.Series, close: pd.Series, w: int) -> pd.Series:
    hh = _rolling_max(high, w)
    ll = _rolling_min(low, w)
    return _safe_div((close - ll) * 100.0, hh - ll)


def _williams_r(high: pd.Series, low: pd.Series, close: pd.Series, w: int) -> pd.Series:
    hh = _rolling_max(high, w)
    ll = _rolling_min(low, w)
    return _safe_div((hh - close) * -100.0, hh - ll)


def _cci(high: pd.Series, low: pd.Series, close: pd.Series, w: int) -> pd.Series:
    tp = (high + low + close) / 3.0
    tp_mean = _rolling_mean(tp, w)
    mad = tp.rolling(w, min_periods=max(1, w // 2)).apply(
        lambda x: np.mean(np.abs(x - x.mean())), raw=True
    )
    return _safe_div(tp - tp_mean, 0.015 * mad)


def _mfi(high: pd.Series, low: pd.Series, close: pd.Series,
          volume: pd.Series, w: int) -> pd.Series:
    tp = (high + low + close) / 3.0
    mf = tp * volume
    pos_mf = mf.where(tp > tp.shift(1), 0.0)
    neg_mf = mf.where(tp < tp.shift(1), 0.0)
    pos_sum = _rolling_sum(pos_mf, w)
    neg_sum = _rolling_sum(neg_mf, w)
    mfr = _safe_div(pos_sum, neg_sum)
    return 100.0 - _safe_div(100.0, 1.0 + mfr)


def _stoch_rsi(close: pd.Series, rsi_w: int, stoch_w: int) -> pd.Series:
    delta = close.diff(1)
    gain = delta.clip(lower=0.0)
    loss = (-delta).clip(lower=0.0)
    avg_gain = gain.ewm(span=rsi_w, min_periods=max(1, rsi_w // 2)).mean()
    avg_loss = loss.ewm(span=rsi_w, min_periods=max(1, rsi_w // 2)).mean()
    rs = _safe_div(avg_gain, avg_loss)
    rsi = 100.0 - _safe_div(100.0, 1.0 + rs)
    rsi_min = _rolling_min(rsi, stoch_w)
    rsi_max = _rolling_max(rsi, stoch_w)
    return _safe_div((rsi - rsi_min) * 100.0, rsi_max - rsi_min)


def _awesome_osc(high: pd.Series, low: pd.Series, w_fast: int = 5, w_slow: int = 34) -> pd.Series:
    midpoint = (high + low) / 2.0
    return _rolling_mean(midpoint, w_fast) - _rolling_mean(midpoint, w_slow)


def _cmo(close: pd.Series, n: int) -> pd.Series:
    """Chande Momentum Oscillator."""
    delta = close.diff(1)
    up = delta.clip(lower=0.0)
    dn = (-delta).clip(lower=0.0)
    sum_up = _rolling_sum(up, n)
    sum_dn = _rolling_sum(dn, n)
    return _safe_div(100.0 * (sum_up - sum_dn), sum_up + sum_dn)


def _trix(close: pd.Series, n: int) -> pd.Series:
    """TRIX: 1-period % ROC of triple-EMA of log(close)."""
    log_c = np.log(close.replace(0, np.nan))
    ema1 = _ewm_mean(log_c, n)
    ema2 = _ewm_mean(ema1, n)
    ema3 = _ewm_mean(ema2, n)
    return _safe_div(ema3 - ema3.shift(1), ema3.shift(1)) * 100.0


def _fisher_transform(high: pd.Series, low: pd.Series, close: pd.Series, n: int) -> pd.Series:
    """Fisher Transform."""
    hh = _rolling_max(high, n)
    ll = _rolling_min(low, n)
    rng = (hh - ll).replace(0, np.nan)
    val = (2.0 * ((close - ll) / rng) - 1.0).clip(-0.999, 0.999)
    return 0.5 * np.log((1.0 + val) / (1.0 - val))


def _ppo(close: pd.Series, fast: int = 12, slow: int = 26) -> pd.Series:
    """Percentage Price Oscillator."""
    ema_f = _ewm_mean(close, fast)
    ema_s = _ewm_mean(close, slow)
    return _safe_div((ema_f - ema_s), ema_s) * 100.0


def _kst(close: pd.Series) -> pd.Series:
    """KST oscillator."""
    def _roc(c: pd.Series, n: int) -> pd.Series:
        return _safe_div(c - c.shift(n), c.shift(n)) * 100.0
    r1 = _rolling_mean(_roc(close, 10), 10)
    r2 = _rolling_mean(_roc(close, 15), 10)
    r3 = _rolling_mean(_roc(close, 20), 10)
    r4 = _rolling_mean(_roc(close, 30), 15)
    return r1 * 1.0 + r2 * 2.0 + r3 * 3.0 + r4 * 4.0


def _coppock(close: pd.Series) -> pd.Series:
    """Coppock Curve."""
    def _roc(c: pd.Series, n: int) -> pd.Series:
        return _safe_div(c - c.shift(n), c.shift(n)) * 100.0
    combined = _roc(close, 14) + _roc(close, 11)
    w = 10
    def _wma(x):
        if len(x) < w // 2:
            return np.nan
        wts = np.arange(1, len(x) + 1, dtype=float)
        return float(np.dot(x, wts) / wts.sum())
    return combined.rolling(w, min_periods=max(1, w // 2)).apply(_wma, raw=True)


def _smi(high: pd.Series, low: pd.Series, close: pd.Series, n: int,
         smooth1: int = 3, smooth2: int = 3) -> pd.Series:
    """Stochastic Momentum Index."""
    hh = _rolling_max(high, n)
    ll = _rolling_min(low, n)
    midpoint = (hh + ll) / 2.0
    diff = close - midpoint
    half_range = (hh - ll) / 2.0
    diff_sm = _ewm_mean(_ewm_mean(diff, smooth1), smooth2)
    range_sm = _ewm_mean(_ewm_mean(half_range, smooth1), smooth2)
    return _safe_div(diff_sm, range_sm) * 100.0


def _klinger(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Klinger Volume Oscillator."""
    tp = high + low + close
    trend = pd.Series(np.where(tp > tp.shift(1), 1.0, -1.0), index=close.index)
    dm = high - low
    sv = volume * trend * 2.0 * _safe_div(dm, (high - low).replace(0, np.nan))
    return _ewm_mean(sv, 34) - _ewm_mean(sv, 55)


def _rvi(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series,
         n: int = 10) -> pd.Series:
    """Relative Vigor Index."""
    num = close - open_
    den = high - low
    def _sym4(s: pd.Series) -> pd.Series:
        return (s + 2.0 * s.shift(1) + 2.0 * s.shift(2) + s.shift(3)) / 6.0
    ratio = _safe_div(_sym4(num), _sym4(den).replace(0, np.nan))
    return _rolling_mean(ratio, n)


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
# Each 3rd-derivative = diff/slope applied to a 2nd-derivative concept

def osc_drv3_001_stoch_k_14_5d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of 14-day %K (acceleration of oscillator velocity)."""
    vel = _stoch_k(high, low, close, 14).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def osc_drv3_002_stoch_k_14_21d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of 14-day %K (jerk in monthly change)."""
    vel21 = _stoch_k(high, low, close, 14).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def osc_drv3_003_williams_r_14_5d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of Williams %R (14-day) (acceleration of deepening)."""
    vel = _williams_r(high, low, close, 14).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def osc_drv3_004_cci_14_5d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of CCI (14-day) (jerk in CCI movement)."""
    vel = _cci(high, low, close, 14).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def osc_drv3_005_mfi_14_5d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of MFI (14-day) (acceleration of money-flow deterioration)."""
    vel = _mfi(high, low, close, volume, 14).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def osc_drv3_006_stoch_rsi_14_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of StochRSI (14,14) (acceleration)."""
    vel = _stoch_rsi(close, 14, 14).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def osc_drv3_007_cmo_14_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of CMO (14-day) — acceleration of Chande momentum."""
    vel = _cmo(close, 14).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def osc_drv3_008_cmo_14_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of CMO (14-day)."""
    vel21 = _cmo(close, 14).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def osc_drv3_009_trix_14_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of TRIX (14) — acceleration of triple-EMA momentum."""
    vel = _trix(close, 14).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def osc_drv3_010_fisher_10_5d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of Fisher Transform (10-day) — acceleration of extremity."""
    vel = _fisher_transform(high, low, close, 10).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def osc_drv3_011_ppo_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of PPO (12/26) — acceleration of percentage price oscillator."""
    vel = _ppo(close).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def osc_drv3_012_kst_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of KST — acceleration of Know Sure Thing."""
    vel = _kst(close).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def osc_drv3_013_coppock_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of Coppock Curve — jerk in long-cycle momentum."""
    vel = _coppock(close).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def osc_drv3_014_smi_14_5d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of SMI (14-day) — acceleration of stochastic momentum."""
    vel = _smi(high, low, close, 14).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def osc_drv3_015_klinger_5d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of Klinger Volume Oscillator — acceleration of volume force."""
    vel = _klinger(high, low, close, volume).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def osc_drv3_016_rvi_5d_diff_5d_diff(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of RVI — acceleration of relative vigor."""
    vel = _rvi(open_, high, low, close, 10).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def osc_drv3_017_awesome_osc_5d_diff_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of Awesome Oscillator (acceleration of AO momentum)."""
    vel = _awesome_osc(high, low).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def osc_drv3_018_stoch_k_14_slope_21d_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day OLS slope of %K (rate of slope change)."""
    slp = _linslope(_stoch_k(high, low, close, 14), _TD_MON)
    return slp.diff(_TD_WEEK)


def osc_drv3_019_cmo_14_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day OLS slope of CMO (14-day)."""
    slp = _linslope(_cmo(close, 14), _TD_MON)
    return slp.diff(_TD_WEEK)


def osc_drv3_020_fisher_10_slope_21d_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day OLS slope of Fisher Transform (10-day)."""
    slp = _linslope(_fisher_transform(high, low, close, 10), _TD_MON)
    return slp.diff(_TD_WEEK)


def osc_drv3_021_ppo_histogram_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of PPO histogram — jerk in histogram compression."""
    hist = _ppo(close) - _ewm_mean(_ppo(close), 9)
    vel = hist.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def osc_drv3_022_kst_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day OLS slope of KST."""
    slp = _linslope(_kst(close), _TD_MON)
    return slp.diff(_TD_WEEK)


def osc_drv3_023_smi_14_21d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of SMI (14-day)."""
    vel21 = _smi(high, low, close, 14).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def osc_drv3_024_trix_14_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day OLS slope of TRIX (14)."""
    slp = _linslope(_trix(close, 14), _TD_MON)
    return slp.diff(_TD_WEEK)


def osc_drv3_025_mfi_14_slope_21d_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day OLS slope of MFI (14-day)."""
    slp = _linslope(_mfi(high, low, close, volume, 14), _TD_MON)
    return slp.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

OSCILLATOR_EXTREMES_REGISTRY_3RD_DERIVATIVES = {
    "osc_drv3_001_stoch_k_14_5d_diff_5d_diff": {"inputs": ["high", "low", "close"], "func": osc_drv3_001_stoch_k_14_5d_diff_5d_diff},
    "osc_drv3_002_stoch_k_14_21d_diff_5d_diff": {"inputs": ["high", "low", "close"], "func": osc_drv3_002_stoch_k_14_21d_diff_5d_diff},
    "osc_drv3_003_williams_r_14_5d_diff_5d_diff": {"inputs": ["high", "low", "close"], "func": osc_drv3_003_williams_r_14_5d_diff_5d_diff},
    "osc_drv3_004_cci_14_5d_diff_5d_diff": {"inputs": ["high", "low", "close"], "func": osc_drv3_004_cci_14_5d_diff_5d_diff},
    "osc_drv3_005_mfi_14_5d_diff_5d_diff": {"inputs": ["high", "low", "close", "volume"], "func": osc_drv3_005_mfi_14_5d_diff_5d_diff},
    "osc_drv3_006_stoch_rsi_14_5d_diff_5d_diff": {"inputs": ["close"], "func": osc_drv3_006_stoch_rsi_14_5d_diff_5d_diff},
    "osc_drv3_007_cmo_14_5d_diff_5d_diff": {"inputs": ["close"], "func": osc_drv3_007_cmo_14_5d_diff_5d_diff},
    "osc_drv3_008_cmo_14_21d_diff_5d_diff": {"inputs": ["close"], "func": osc_drv3_008_cmo_14_21d_diff_5d_diff},
    "osc_drv3_009_trix_14_5d_diff_5d_diff": {"inputs": ["close"], "func": osc_drv3_009_trix_14_5d_diff_5d_diff},
    "osc_drv3_010_fisher_10_5d_diff_5d_diff": {"inputs": ["high", "low", "close"], "func": osc_drv3_010_fisher_10_5d_diff_5d_diff},
    "osc_drv3_011_ppo_5d_diff_5d_diff": {"inputs": ["close"], "func": osc_drv3_011_ppo_5d_diff_5d_diff},
    "osc_drv3_012_kst_5d_diff_5d_diff": {"inputs": ["close"], "func": osc_drv3_012_kst_5d_diff_5d_diff},
    "osc_drv3_013_coppock_5d_diff_5d_diff": {"inputs": ["close"], "func": osc_drv3_013_coppock_5d_diff_5d_diff},
    "osc_drv3_014_smi_14_5d_diff_5d_diff": {"inputs": ["high", "low", "close"], "func": osc_drv3_014_smi_14_5d_diff_5d_diff},
    "osc_drv3_015_klinger_5d_diff_5d_diff": {"inputs": ["high", "low", "close", "volume"], "func": osc_drv3_015_klinger_5d_diff_5d_diff},
    "osc_drv3_016_rvi_5d_diff_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": osc_drv3_016_rvi_5d_diff_5d_diff},
    "osc_drv3_017_awesome_osc_5d_diff_5d_diff": {"inputs": ["high", "low"], "func": osc_drv3_017_awesome_osc_5d_diff_5d_diff},
    "osc_drv3_018_stoch_k_14_slope_21d_5d_diff": {"inputs": ["high", "low", "close"], "func": osc_drv3_018_stoch_k_14_slope_21d_5d_diff},
    "osc_drv3_019_cmo_14_slope_21d_5d_diff": {"inputs": ["close"], "func": osc_drv3_019_cmo_14_slope_21d_5d_diff},
    "osc_drv3_020_fisher_10_slope_21d_5d_diff": {"inputs": ["high", "low", "close"], "func": osc_drv3_020_fisher_10_slope_21d_5d_diff},
    "osc_drv3_021_ppo_histogram_5d_diff_5d_diff": {"inputs": ["close"], "func": osc_drv3_021_ppo_histogram_5d_diff_5d_diff},
    "osc_drv3_022_kst_slope_21d_5d_diff": {"inputs": ["close"], "func": osc_drv3_022_kst_slope_21d_5d_diff},
    "osc_drv3_023_smi_14_21d_diff_5d_diff": {"inputs": ["high", "low", "close"], "func": osc_drv3_023_smi_14_21d_diff_5d_diff},
    "osc_drv3_024_trix_14_slope_21d_5d_diff": {"inputs": ["close"], "func": osc_drv3_024_trix_14_slope_21d_5d_diff},
    "osc_drv3_025_mfi_14_slope_21d_5d_diff": {"inputs": ["high", "low", "close", "volume"], "func": osc_drv3_025_mfi_14_slope_21d_5d_diff},
}
