"""
26_rsi_extremes — 2nd Derivatives (Features rsi_drv2_001-025)
Domain: rate of change of base RSI extreme features — velocity of RSI oversold behavior
Includes derivatives of StochRSI, Laguerre RSI, EMA-RSI, Wilder RSI, Connors RSI
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


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _rsi(close: pd.Series, period: int) -> pd.Series:
    """Wilder smoothed RSI for a given lookback period."""
    delta = close.diff(1)
    gain = delta.clip(lower=0.0)
    loss = (-delta).clip(lower=0.0)
    avg_gain = gain.ewm(alpha=1.0 / period, min_periods=period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1.0 / period, min_periods=period, adjust=False).mean()
    rs = _safe_div(avg_gain, avg_loss)
    return 100.0 - 100.0 / (1.0 + rs)


def _rsi_ema(close: pd.Series, period: int) -> pd.Series:
    """EMA-smoothed RSI: gains/losses averaged with EMA span=period."""
    delta = close.diff(1)
    gain = delta.clip(lower=0.0)
    loss = (-delta).clip(lower=0.0)
    avg_gain = gain.ewm(span=period, min_periods=period, adjust=False).mean()
    avg_loss = loss.ewm(span=period, min_periods=period, adjust=False).mean()
    rs = _safe_div(avg_gain, avg_loss)
    return 100.0 - 100.0 / (1.0 + rs)


def _stochrsi_k(close: pd.Series, rsi_period: int, stoch_period: int) -> pd.Series:
    """StochRSI %K: (RSI - min(RSI,n)) / (max(RSI,n) - min(RSI,n)), scaled 0-100."""
    r = _rsi(close, rsi_period)
    mn = _rolling_min(r, stoch_period)
    mx = _rolling_max(r, stoch_period)
    k = _safe_div(r - mn, mx - mn)
    return k * 100.0


def _laguerre_rsi(close: pd.Series, gamma: float) -> pd.Series:
    """Ehlers Laguerre RSI using a 4-pole Laguerre filter."""
    n = len(close)
    vals = close.values.astype(float)
    g = float(gamma)
    g1 = 1.0 - g

    L0 = np.full(n, np.nan)
    L1 = np.full(n, np.nan)
    L2 = np.full(n, np.nan)
    L3 = np.full(n, np.nan)
    cu = np.full(n, np.nan)
    cd = np.full(n, np.nan)

    first = 0
    while first < n and np.isnan(vals[first]):
        first += 1
    if first >= n:
        return pd.Series(np.nan, index=close.index)

    L0[first] = vals[first]
    L1[first] = vals[first]
    L2[first] = vals[first]
    L3[first] = vals[first]

    for i in range(first + 1, n):
        if np.isnan(vals[i]):
            L0[i] = L0[i - 1]
            L1[i] = L1[i - 1]
            L2[i] = L2[i - 1]
            L3[i] = L3[i - 1]
        else:
            L0[i] = g1 * vals[i] + g * L0[i - 1]
            L1[i] = -g * L0[i] + L0[i - 1] + g * L1[i - 1]
            L2[i] = -g * L1[i] + L1[i - 1] + g * L2[i - 1]
            L3[i] = -g * L2[i] + L2[i - 1] + g * L3[i - 1]

        cu_i = 0.0
        cd_i = 0.0
        if L0[i] >= L1[i]:
            cu_i += L0[i] - L1[i]
        else:
            cd_i += L1[i] - L0[i]
        if L1[i] >= L2[i]:
            cu_i += L1[i] - L2[i]
        else:
            cd_i += L2[i] - L1[i]
        if L2[i] >= L3[i]:
            cu_i += L2[i] - L3[i]
        else:
            cd_i += L3[i] - L2[i]
        cu[i] = cu_i
        cd[i] = cd_i

    with np.errstate(invalid='ignore', divide='ignore'):
        denom = cu + cd
        lrsi = np.where(denom == 0.0, 50.0, cu / denom * 100.0)

    result = pd.Series(lrsi, index=close.index)
    result.iloc[:first] = np.nan
    return result


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

def rsi_drv2_001_rsi14_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of RSI14 (velocity of RSI14 movement)."""
    return _rsi(close, 14).diff(_TD_WEEK)


def rsi_drv2_002_rsi14_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of RSI14 (monthly velocity of RSI14)."""
    return _rsi(close, 14).diff(_TD_MON)


def rsi_drv2_003_rsi7_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of RSI7 (fast RSI velocity)."""
    return _rsi(close, 7).diff(_TD_WEEK)


def rsi_drv2_004_rsi14_depth30_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of RSI14 oversold depth (how fast depth is deepening)."""
    depth = (30.0 - _rsi(close, 14)).clip(lower=0.0)
    return depth.diff(_TD_WEEK)


def rsi_drv2_005_rsi14_depth30_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of RSI14 oversold depth below 30."""
    depth = (30.0 - _rsi(close, 14)).clip(lower=0.0)
    return depth.diff(_TD_MON)


def rsi_drv2_006_consec_rsi14_below30_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of consecutive-days-RSI14-below-30 streak."""
    streak = _consec_streak(_rsi(close, 14) < 30.0)
    return streak.diff(_TD_WEEK)


def rsi_drv2_007_rsi14_zscore_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of RSI14 z-score vs 252-day distribution."""
    r = _rsi(close, 14)
    m = _rolling_mean(r, _TD_YEAR)
    s = _rolling_std(r, _TD_YEAR)
    z = _safe_div(r - m, s)
    return z.diff(_TD_WEEK)


def rsi_drv2_008_rsi14_min_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of the 63-day minimum RSI14."""
    mn = _rolling_min(_rsi(close, 14), _TD_QTR)
    return mn.diff(_TD_MON)


def rsi_drv2_009_connors_rsi_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of Connors RSI composite."""
    rsi3 = _rsi(close, 3)
    delta = close.diff(1)
    sign = np.sign(delta)
    streak = _consec_streak(sign > 0) - _consec_streak(sign < 0)
    streak_rsi = _rsi(streak, 3)
    pct_rank = close.pct_change(1).rolling(100, min_periods=50).rank(pct=True) * 100.0
    crsi = (rsi3 + streak_rsi + pct_rank) / 3.0
    return crsi.diff(_TD_WEEK)


def rsi_drv2_010_rsi_composite_3periods_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 3-period RSI composite (RSI7+RSI14+RSI21)/3."""
    comp = (_rsi(close, 7) + _rsi(close, 14) + _rsi(close, _TD_MON)) / 3.0
    return comp.diff(_TD_WEEK)


def rsi_drv2_011_rsi_distress_score_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of multi-RSI distress score (RSI7+RSI14+RSI21 depths)."""
    d7 = (30.0 - _rsi(close, 7)).clip(lower=0.0)
    d14 = (30.0 - _rsi(close, 14)).clip(lower=0.0)
    d21 = (30.0 - _rsi(close, _TD_MON)).clip(lower=0.0)
    score = d7 + d14 + d21
    return score.diff(_TD_WEEK)


def rsi_drv2_012_stochrsi14_k_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of StochRSI(14) %K (velocity of StochRSI)."""
    k = _stochrsi_k(close, 14, 14)
    return k.diff(_TD_WEEK)


def rsi_drv2_013_stochrsi14_k_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of StochRSI(14) %K (monthly velocity)."""
    k = _stochrsi_k(close, 14, 14)
    return k.diff(_TD_MON)


def rsi_drv2_014_stochrsi14_k_depth20_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of StochRSI(14) %K depth below 20 (deepening oversold velocity)."""
    depth = (20.0 - _stochrsi_k(close, 14, 14)).clip(lower=0.0)
    return depth.diff(_TD_WEEK)


def rsi_drv2_015_laguerre_rsi_g05_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of Laguerre RSI (gamma=0.5) — velocity of Laguerre oversold."""
    lr = _laguerre_rsi(close, 0.5)
    return lr.diff(_TD_WEEK)


def rsi_drv2_016_laguerre_rsi_g07_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of Laguerre RSI (gamma=0.7)."""
    lr = _laguerre_rsi(close, 0.7)
    return lr.diff(_TD_WEEK)


def rsi_drv2_017_laguerre_rsi_g05_depth20_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of Laguerre RSI (gamma=0.5) depth below 20."""
    depth = (20.0 - _laguerre_rsi(close, 0.5)).clip(lower=0.0)
    return depth.diff(_TD_WEEK)


def rsi_drv2_018_ema_rsi14_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of EMA-smoothed RSI(14) — velocity of EMA-RSI movement."""
    return _rsi_ema(close, 14).diff(_TD_WEEK)


def rsi_drv2_019_ema_rsi14_depth30_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of EMA-RSI(14) depth below 30."""
    depth = (30.0 - _rsi_ema(close, 14)).clip(lower=0.0)
    return depth.diff(_TD_WEEK)


def rsi_drv2_020_ema_rsi14_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of EMA-smoothed RSI(14)."""
    return _rsi_ema(close, 14).diff(_TD_MON)


def rsi_drv2_021_rsi14_fraction_below30_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day fraction of days RSI14 < 30."""
    flag = (_rsi(close, 14) < 30.0).astype(float)
    frac = _rolling_sum(flag, _TD_QTR) / _TD_QTR
    return frac.diff(_TD_MON)


def rsi_drv2_022_rsi14_slope_5d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day OLS slope of RSI14."""
    slope5 = _linslope(_rsi(close, 14), _TD_WEEK)
    return _linslope(slope5, _TD_MON)


def rsi_drv2_023_stochrsi14_k_consec_below20_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of consecutive-days-StochRSI-K-below-20 streak."""
    streak = _consec_streak(_stochrsi_k(close, 14, 14) < 20.0)
    return streak.diff(_TD_WEEK)


def rsi_drv2_024_laguerre_rsi_g05_consec_below20_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of consecutive-days-Laguerre-RSI(g05)-below-20 streak."""
    streak = _consec_streak(_laguerre_rsi(close, 0.5) < 20.0)
    return streak.diff(_TD_WEEK)


def rsi_drv2_025_rsi14_oversold_intensity_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day RSI14 oversold intensity sum."""
    depth = (30.0 - _rsi(close, 14)).clip(lower=0.0)
    intensity = _rolling_sum(depth, _TD_MON)
    return intensity.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

RSI_EXTREMES_REGISTRY_2ND_DERIVATIVES = {
    "rsi_drv2_001_rsi14_5d_diff": {"inputs": ["close"], "func": rsi_drv2_001_rsi14_5d_diff},
    "rsi_drv2_002_rsi14_21d_diff": {"inputs": ["close"], "func": rsi_drv2_002_rsi14_21d_diff},
    "rsi_drv2_003_rsi7_5d_diff": {"inputs": ["close"], "func": rsi_drv2_003_rsi7_5d_diff},
    "rsi_drv2_004_rsi14_depth30_5d_diff": {"inputs": ["close"], "func": rsi_drv2_004_rsi14_depth30_5d_diff},
    "rsi_drv2_005_rsi14_depth30_21d_diff": {"inputs": ["close"], "func": rsi_drv2_005_rsi14_depth30_21d_diff},
    "rsi_drv2_006_consec_rsi14_below30_5d_diff": {"inputs": ["close"], "func": rsi_drv2_006_consec_rsi14_below30_5d_diff},
    "rsi_drv2_007_rsi14_zscore_5d_diff": {"inputs": ["close"], "func": rsi_drv2_007_rsi14_zscore_5d_diff},
    "rsi_drv2_008_rsi14_min_63d_21d_diff": {"inputs": ["close"], "func": rsi_drv2_008_rsi14_min_63d_21d_diff},
    "rsi_drv2_009_connors_rsi_5d_diff": {"inputs": ["close"], "func": rsi_drv2_009_connors_rsi_5d_diff},
    "rsi_drv2_010_rsi_composite_3periods_5d_diff": {"inputs": ["close"], "func": rsi_drv2_010_rsi_composite_3periods_5d_diff},
    "rsi_drv2_011_rsi_distress_score_5d_diff": {"inputs": ["close"], "func": rsi_drv2_011_rsi_distress_score_5d_diff},
    "rsi_drv2_012_stochrsi14_k_5d_diff": {"inputs": ["close"], "func": rsi_drv2_012_stochrsi14_k_5d_diff},
    "rsi_drv2_013_stochrsi14_k_21d_diff": {"inputs": ["close"], "func": rsi_drv2_013_stochrsi14_k_21d_diff},
    "rsi_drv2_014_stochrsi14_k_depth20_5d_diff": {"inputs": ["close"], "func": rsi_drv2_014_stochrsi14_k_depth20_5d_diff},
    "rsi_drv2_015_laguerre_rsi_g05_5d_diff": {"inputs": ["close"], "func": rsi_drv2_015_laguerre_rsi_g05_5d_diff},
    "rsi_drv2_016_laguerre_rsi_g07_5d_diff": {"inputs": ["close"], "func": rsi_drv2_016_laguerre_rsi_g07_5d_diff},
    "rsi_drv2_017_laguerre_rsi_g05_depth20_5d_diff": {"inputs": ["close"], "func": rsi_drv2_017_laguerre_rsi_g05_depth20_5d_diff},
    "rsi_drv2_018_ema_rsi14_5d_diff": {"inputs": ["close"], "func": rsi_drv2_018_ema_rsi14_5d_diff},
    "rsi_drv2_019_ema_rsi14_depth30_5d_diff": {"inputs": ["close"], "func": rsi_drv2_019_ema_rsi14_depth30_5d_diff},
    "rsi_drv2_020_ema_rsi14_21d_diff": {"inputs": ["close"], "func": rsi_drv2_020_ema_rsi14_21d_diff},
    "rsi_drv2_021_rsi14_fraction_below30_63d_21d_diff": {"inputs": ["close"], "func": rsi_drv2_021_rsi14_fraction_below30_63d_21d_diff},
    "rsi_drv2_022_rsi14_slope_5d_slope_21d": {"inputs": ["close"], "func": rsi_drv2_022_rsi14_slope_5d_slope_21d},
    "rsi_drv2_023_stochrsi14_k_consec_below20_5d_diff": {"inputs": ["close"], "func": rsi_drv2_023_stochrsi14_k_consec_below20_5d_diff},
    "rsi_drv2_024_laguerre_rsi_g05_consec_below20_5d_diff": {"inputs": ["close"], "func": rsi_drv2_024_laguerre_rsi_g05_consec_below20_5d_diff},
    "rsi_drv2_025_rsi14_oversold_intensity_21d_5d_diff": {"inputs": ["close"], "func": rsi_drv2_025_rsi14_oversold_intensity_21d_5d_diff},
}
