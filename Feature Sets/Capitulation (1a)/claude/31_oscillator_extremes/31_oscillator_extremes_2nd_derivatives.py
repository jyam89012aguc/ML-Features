"""
31_oscillator_extremes — 2nd Derivatives (Features osc_drv2_001-025)
Domain: rate of change of oscillator extreme base features — velocity of oversold depth
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
Covers velocity of: Stochastic, Williams %R, CCI, MFI, StochRSI, Awesome Oscillator,
CMO, TRIX, Fisher Transform, PPO, KST, Coppock, SMI, Klinger, RVI.
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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def osc_drv2_001_stoch_k_14_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 14-day Stochastic %K (velocity of oscillator movement)."""
    return _stoch_k(high, low, close, 14).diff(_TD_WEEK)


def osc_drv2_002_stoch_k_14_21d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day diff of 14-day Stochastic %K (monthly velocity)."""
    return _stoch_k(high, low, close, 14).diff(_TD_MON)


def osc_drv2_003_williams_r_14_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of Williams %R (14-day) — rate of oversold deepening."""
    return _williams_r(high, low, close, 14).diff(_TD_WEEK)


def osc_drv2_004_williams_r_14_21d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day diff of Williams %R (14-day) — monthly velocity."""
    return _williams_r(high, low, close, 14).diff(_TD_MON)


def osc_drv2_005_cci_14_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of CCI (14-day) — weekly velocity of CCI."""
    return _cci(high, low, close, 14).diff(_TD_WEEK)


def osc_drv2_006_cci_14_slope_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """OLS slope of CCI (14-day) over trailing 21 days."""
    return _linslope(_cci(high, low, close, 14), _TD_MON)


def osc_drv2_007_mfi_14_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of MFI (14-day) — rate of money-flow deterioration."""
    return _mfi(high, low, close, volume, 14).diff(_TD_WEEK)


def osc_drv2_008_mfi_14_slope_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of MFI (14-day) over trailing 21 days."""
    return _linslope(_mfi(high, low, close, volume, 14), _TD_MON)


def osc_drv2_009_stoch_rsi_14_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of StochRSI (14,14) — weekly velocity."""
    return _stoch_rsi(close, 14, 14).diff(_TD_WEEK)


def osc_drv2_010_stoch_rsi_14_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of StochRSI (14,14) over trailing 63 days."""
    return _linslope(_stoch_rsi(close, 14, 14), _TD_QTR)


def osc_drv2_011_cmo_14_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of CMO (14-day) — weekly velocity of Chande momentum."""
    return _cmo(close, 14).diff(_TD_WEEK)


def osc_drv2_012_cmo_14_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of CMO (14-day) — monthly velocity."""
    return _cmo(close, 14).diff(_TD_MON)


def osc_drv2_013_trix_14_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of TRIX (14) — velocity of triple-EMA momentum."""
    return _trix(close, 14).diff(_TD_WEEK)


def osc_drv2_014_fisher_10_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of Fisher Transform (10-day) — rate of extreme deepening."""
    return _fisher_transform(high, low, close, 10).diff(_TD_WEEK)


def osc_drv2_015_ppo_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of PPO (12/26) — velocity of percentage price oscillator."""
    return _ppo(close).diff(_TD_WEEK)


def osc_drv2_016_ppo_histogram_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of PPO histogram — velocity of histogram compression."""
    hist = _ppo(close) - _ewm_mean(_ppo(close), 9)
    return hist.diff(_TD_WEEK)


def osc_drv2_017_kst_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of KST — velocity of Know Sure Thing oscillator."""
    return _kst(close).diff(_TD_WEEK)


def osc_drv2_018_kst_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of KST over trailing 21 days."""
    return _linslope(_kst(close), _TD_MON)


def osc_drv2_019_coppock_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of Coppock Curve — velocity of long-cycle momentum."""
    return _coppock(close).diff(_TD_WEEK)


def osc_drv2_020_smi_14_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of SMI (14-day) — velocity of stochastic momentum."""
    return _smi(high, low, close, 14).diff(_TD_WEEK)


def osc_drv2_021_schaff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of Schaff Trend Cycle — velocity of cycle oscillator."""
    ema_f = _ewm_mean(close, 23)
    ema_s = _ewm_mean(close, 50)
    macd = ema_f - ema_s
    m_min = _rolling_min(macd, 10)
    m_max = _rolling_max(macd, 10)
    stoch1 = _safe_div((macd - m_min) * 100.0, m_max - m_min)
    f1 = _ewm_mean(stoch1, 2)
    f1_min = _rolling_min(f1, 10)
    f1_max = _rolling_max(f1, 10)
    stoch2 = _safe_div((f1 - f1_min) * 100.0, f1_max - f1_min)
    stc = _ewm_mean(stoch2, 2)
    return stc.diff(_TD_WEEK)


def osc_drv2_022_klinger_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of Klinger Volume Oscillator — velocity of volume force."""
    return _klinger(high, low, close, volume).diff(_TD_WEEK)


def osc_drv2_023_rvi_5d_diff(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of RVI (10-period) — velocity of relative vigor."""
    return _rvi(open_, high, low, close, 10).diff(_TD_WEEK)


def osc_drv2_024_awesome_osc_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of Awesome Oscillator (weekly velocity)."""
    return _awesome_osc(high, low).diff(_TD_WEEK)


def osc_drv2_025_stoch_k_14_slope_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """OLS slope of 14-day %K over trailing 21 days."""
    return _linslope(_stoch_k(high, low, close, 14), _TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

OSCILLATOR_EXTREMES_REGISTRY_2ND_DERIVATIVES = {
    "osc_drv2_001_stoch_k_14_5d_diff": {"inputs": ["high", "low", "close"], "func": osc_drv2_001_stoch_k_14_5d_diff},
    "osc_drv2_002_stoch_k_14_21d_diff": {"inputs": ["high", "low", "close"], "func": osc_drv2_002_stoch_k_14_21d_diff},
    "osc_drv2_003_williams_r_14_5d_diff": {"inputs": ["high", "low", "close"], "func": osc_drv2_003_williams_r_14_5d_diff},
    "osc_drv2_004_williams_r_14_21d_diff": {"inputs": ["high", "low", "close"], "func": osc_drv2_004_williams_r_14_21d_diff},
    "osc_drv2_005_cci_14_5d_diff": {"inputs": ["high", "low", "close"], "func": osc_drv2_005_cci_14_5d_diff},
    "osc_drv2_006_cci_14_slope_21d": {"inputs": ["high", "low", "close"], "func": osc_drv2_006_cci_14_slope_21d},
    "osc_drv2_007_mfi_14_5d_diff": {"inputs": ["high", "low", "close", "volume"], "func": osc_drv2_007_mfi_14_5d_diff},
    "osc_drv2_008_mfi_14_slope_21d": {"inputs": ["high", "low", "close", "volume"], "func": osc_drv2_008_mfi_14_slope_21d},
    "osc_drv2_009_stoch_rsi_14_5d_diff": {"inputs": ["close"], "func": osc_drv2_009_stoch_rsi_14_5d_diff},
    "osc_drv2_010_stoch_rsi_14_slope_63d": {"inputs": ["close"], "func": osc_drv2_010_stoch_rsi_14_slope_63d},
    "osc_drv2_011_cmo_14_5d_diff": {"inputs": ["close"], "func": osc_drv2_011_cmo_14_5d_diff},
    "osc_drv2_012_cmo_14_21d_diff": {"inputs": ["close"], "func": osc_drv2_012_cmo_14_21d_diff},
    "osc_drv2_013_trix_14_5d_diff": {"inputs": ["close"], "func": osc_drv2_013_trix_14_5d_diff},
    "osc_drv2_014_fisher_10_5d_diff": {"inputs": ["high", "low", "close"], "func": osc_drv2_014_fisher_10_5d_diff},
    "osc_drv2_015_ppo_5d_diff": {"inputs": ["close"], "func": osc_drv2_015_ppo_5d_diff},
    "osc_drv2_016_ppo_histogram_5d_diff": {"inputs": ["close"], "func": osc_drv2_016_ppo_histogram_5d_diff},
    "osc_drv2_017_kst_5d_diff": {"inputs": ["close"], "func": osc_drv2_017_kst_5d_diff},
    "osc_drv2_018_kst_slope_21d": {"inputs": ["close"], "func": osc_drv2_018_kst_slope_21d},
    "osc_drv2_019_coppock_5d_diff": {"inputs": ["close"], "func": osc_drv2_019_coppock_5d_diff},
    "osc_drv2_020_smi_14_5d_diff": {"inputs": ["high", "low", "close"], "func": osc_drv2_020_smi_14_5d_diff},
    "osc_drv2_021_schaff_5d_diff": {"inputs": ["close"], "func": osc_drv2_021_schaff_5d_diff},
    "osc_drv2_022_klinger_5d_diff": {"inputs": ["high", "low", "close", "volume"], "func": osc_drv2_022_klinger_5d_diff},
    "osc_drv2_023_rvi_5d_diff": {"inputs": ["open", "high", "low", "close"], "func": osc_drv2_023_rvi_5d_diff},
    "osc_drv2_024_awesome_osc_5d_diff": {"inputs": ["high", "low"], "func": osc_drv2_024_awesome_osc_5d_diff},
    "osc_drv2_025_stoch_k_14_slope_21d": {"inputs": ["high", "low", "close"], "func": osc_drv2_025_stoch_k_14_slope_21d},
}
