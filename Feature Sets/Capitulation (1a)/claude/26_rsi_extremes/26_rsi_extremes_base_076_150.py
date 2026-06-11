"""
26_rsi_extremes — Base Features 076-150
Domain: RSI oversold readings — depth and duration of RSI extremes
Includes: StochRSI, Laguerre RSI, EMA-smoothed RSI, Connors RSI, RSI composites
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


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


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


def _rsi_sma(close: pd.Series, period: int) -> pd.Series:
    """Cutler (simple-average) RSI for a given lookback."""
    delta = close.diff(1)
    gain = delta.clip(lower=0.0)
    loss = (-delta).clip(lower=0.0)
    avg_gain = _rolling_mean(gain, period)
    avg_loss = _rolling_mean(loss, period)
    rs = _safe_div(avg_gain, avg_loss)
    return 100.0 - 100.0 / (1.0 + rs)


def _rsi_ema(close: pd.Series, period: int) -> pd.Series:
    """EMA-smoothed RSI: gains/losses smoothed with EMA (not Wilder's SMMA).
    Uses standard EMA (span=period) instead of Wilder's alpha=1/period.
    """
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


def _stochrsi_d(close: pd.Series, rsi_period: int, stoch_period: int, smooth: int = 3) -> pd.Series:
    """StochRSI %D: smooth-day SMA of %K."""
    k = _stochrsi_k(close, rsi_period, stoch_period)
    return _rolling_mean(k, smooth)


def _laguerre_rsi(close: pd.Series, gamma: float) -> pd.Series:
    """Ehlers Laguerre RSI using a 4-pole Laguerre filter.

    Each pole: L[n] = (1-gamma)*src + gamma*L[n-1]
    RSI = (up_sum) / (up_sum + dn_sum) * 100
    Fully vectorised using iterative pandas-compatible loop (no .rolling().apply).
    """
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

    # Seed first non-nan
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


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-090): StochRSI — stochastic of RSI line ---

def rsi_076_stochrsi14_k(close: pd.Series) -> pd.Series:
    """StochRSI(14,14) %K: position of RSI14 within its own 14-day range, 0-100."""
    return _stochrsi_k(close, 14, 14)


def rsi_077_stochrsi14_d(close: pd.Series) -> pd.Series:
    """StochRSI(14,14) %D: 3-day SMA of %K (signal line)."""
    return _stochrsi_d(close, 14, 14, smooth=3)


def rsi_078_stochrsi21_k(close: pd.Series) -> pd.Series:
    """StochRSI(21,21) %K: position of RSI21 within its own 21-day range."""
    return _stochrsi_k(close, 21, 21)


def rsi_079_stochrsi21_d(close: pd.Series) -> pd.Series:
    """StochRSI(21,21) %D: 3-day SMA of %K."""
    return _stochrsi_d(close, 21, 21, smooth=3)


def rsi_080_stochrsi14_k_below20_flag(close: pd.Series) -> pd.Series:
    """Binary flag: StochRSI(14) %K < 20 (oversold StochRSI)."""
    return (_stochrsi_k(close, 14, 14) < 20.0).astype(float)


def rsi_081_stochrsi14_k_depth_below20(close: pd.Series) -> pd.Series:
    """Depth of StochRSI(14) %K below 20 oversold threshold."""
    return (20.0 - _stochrsi_k(close, 14, 14)).clip(lower=0.0)


def rsi_082_stochrsi14_k_consec_below20(close: pd.Series) -> pd.Series:
    """Consecutive days StochRSI(14) %K has been below 20."""
    return _consec_streak(_stochrsi_k(close, 14, 14) < 20.0)


def rsi_083_stochrsi21_k_below20_flag(close: pd.Series) -> pd.Series:
    """Binary flag: StochRSI(21) %K < 20."""
    return (_stochrsi_k(close, 21, 21) < 20.0).astype(float)


def rsi_084_stochrsi21_k_depth_below20(close: pd.Series) -> pd.Series:
    """Depth of StochRSI(21) %K below 20."""
    return (20.0 - _stochrsi_k(close, 21, 21)).clip(lower=0.0)


def rsi_085_stochrsi14_k_min_21d(close: pd.Series) -> pd.Series:
    """Minimum StochRSI(14) %K over trailing 21 days."""
    return _rolling_min(_stochrsi_k(close, 14, 14), _TD_MON)


def rsi_086_stochrsi14_k_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of StochRSI(14) %K within trailing 252-day distribution."""
    k = _stochrsi_k(close, 14, 14)
    return k.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rsi_087_stochrsi14_k_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of StochRSI(14) %K vs 252-day distribution."""
    k = _stochrsi_k(close, 14, 14)
    m = _rolling_mean(k, _TD_YEAR)
    s = _rolling_std(k, _TD_YEAR)
    return _safe_div(k - m, s)


def rsi_088_stochrsi14_d_below20_flag(close: pd.Series) -> pd.Series:
    """Binary flag: StochRSI(14) %D signal line < 20."""
    return (_stochrsi_d(close, 14, 14, 3) < 20.0).astype(float)


def rsi_089_stochrsi14_d_depth_below20(close: pd.Series) -> pd.Series:
    """Depth of StochRSI(14) %D below 20."""
    return (20.0 - _stochrsi_d(close, 14, 14, 3)).clip(lower=0.0)


def rsi_090_stochrsi14_kd_spread(close: pd.Series) -> pd.Series:
    """StochRSI(14) %K minus %D spread (momentum of StochRSI)."""
    k = _stochrsi_k(close, 14, 14)
    d = _stochrsi_d(close, 14, 14, 3)
    return k - d


# --- Group I (091-102): Laguerre RSI (Ehlers) ---

def rsi_091_laguerre_rsi_g05(close: pd.Series) -> pd.Series:
    """Laguerre RSI with gamma=0.5 (responsive Ehlers filter)."""
    return _laguerre_rsi(close, 0.5)


def rsi_092_laguerre_rsi_g07(close: pd.Series) -> pd.Series:
    """Laguerre RSI with gamma=0.7 (smoother Ehlers filter)."""
    return _laguerre_rsi(close, 0.7)


def rsi_093_laguerre_rsi_g05_below20_flag(close: pd.Series) -> pd.Series:
    """Binary flag: Laguerre RSI (gamma=0.5) < 20 (oversold)."""
    return (_laguerre_rsi(close, 0.5) < 20.0).astype(float)


def rsi_094_laguerre_rsi_g07_below20_flag(close: pd.Series) -> pd.Series:
    """Binary flag: Laguerre RSI (gamma=0.7) < 20."""
    return (_laguerre_rsi(close, 0.7) < 20.0).astype(float)


def rsi_095_laguerre_rsi_g05_depth_below20(close: pd.Series) -> pd.Series:
    """Depth of Laguerre RSI (gamma=0.5) below 20 oversold threshold."""
    return (20.0 - _laguerre_rsi(close, 0.5)).clip(lower=0.0)


def rsi_096_laguerre_rsi_g07_depth_below20(close: pd.Series) -> pd.Series:
    """Depth of Laguerre RSI (gamma=0.7) below 20."""
    return (20.0 - _laguerre_rsi(close, 0.7)).clip(lower=0.0)


def rsi_097_laguerre_rsi_g05_consec_below20(close: pd.Series) -> pd.Series:
    """Consecutive days Laguerre RSI (gamma=0.5) has been below 20."""
    return _consec_streak(_laguerre_rsi(close, 0.5) < 20.0)


def rsi_098_laguerre_rsi_g07_consec_below20(close: pd.Series) -> pd.Series:
    """Consecutive days Laguerre RSI (gamma=0.7) has been below 20."""
    return _consec_streak(_laguerre_rsi(close, 0.7) < 20.0)


def rsi_099_laguerre_rsi_g05_min_21d(close: pd.Series) -> pd.Series:
    """Minimum Laguerre RSI (gamma=0.5) over trailing 21 days."""
    return _rolling_min(_laguerre_rsi(close, 0.5), _TD_MON)


def rsi_100_laguerre_rsi_g07_min_21d(close: pd.Series) -> pd.Series:
    """Minimum Laguerre RSI (gamma=0.7) over trailing 21 days."""
    return _rolling_min(_laguerre_rsi(close, 0.7), _TD_MON)


def rsi_101_laguerre_rsi_g05_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of Laguerre RSI (gamma=0.5) within 252-day distribution."""
    lr = _laguerre_rsi(close, 0.5)
    return lr.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rsi_102_laguerre_rsi_g05_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of Laguerre RSI (gamma=0.5) vs 252-day distribution."""
    lr = _laguerre_rsi(close, 0.5)
    m = _rolling_mean(lr, _TD_YEAR)
    s = _rolling_std(lr, _TD_YEAR)
    return _safe_div(lr - m, s)


# --- Group J (103-115): EMA-smoothed RSI ---

def rsi_103_ema_rsi14(close: pd.Series) -> pd.Series:
    """EMA-smoothed RSI (14): gains/losses averaged with EMA span=14."""
    return _rsi_ema(close, 14)


def rsi_104_ema_rsi7(close: pd.Series) -> pd.Series:
    """EMA-smoothed RSI (7): gains/losses averaged with EMA span=7."""
    return _rsi_ema(close, 7)


def rsi_105_ema_rsi21(close: pd.Series) -> pd.Series:
    """EMA-smoothed RSI (21): gains/losses averaged with EMA span=21."""
    return _rsi_ema(close, 21)


def rsi_106_ema_rsi14_below30_flag(close: pd.Series) -> pd.Series:
    """Binary flag: EMA-RSI(14) < 30 (oversold)."""
    return (_rsi_ema(close, 14) < 30.0).astype(float)


def rsi_107_ema_rsi7_below30_flag(close: pd.Series) -> pd.Series:
    """Binary flag: EMA-RSI(7) < 30."""
    return (_rsi_ema(close, 7) < 30.0).astype(float)


def rsi_108_ema_rsi14_depth_below30(close: pd.Series) -> pd.Series:
    """Depth of EMA-RSI(14) below 30."""
    return (30.0 - _rsi_ema(close, 14)).clip(lower=0.0)


def rsi_109_ema_rsi7_depth_below30(close: pd.Series) -> pd.Series:
    """Depth of EMA-RSI(7) below 30."""
    return (30.0 - _rsi_ema(close, 7)).clip(lower=0.0)


def rsi_110_ema_rsi14_consec_below30(close: pd.Series) -> pd.Series:
    """Consecutive days EMA-RSI(14) has been below 30."""
    return _consec_streak(_rsi_ema(close, 14) < 30.0)


def rsi_111_ema_rsi14_min_21d(close: pd.Series) -> pd.Series:
    """Minimum EMA-RSI(14) over trailing 21 days."""
    return _rolling_min(_rsi_ema(close, 14), _TD_MON)


def rsi_112_ema_rsi14_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of EMA-RSI(14) vs 252-day distribution."""
    r = _rsi_ema(close, 14)
    m = _rolling_mean(r, _TD_YEAR)
    s = _rolling_std(r, _TD_YEAR)
    return _safe_div(r - m, s)


def rsi_113_ema_rsi14_smoothed_line(close: pd.Series) -> pd.Series:
    """EMA-RSI(14) further smoothed by a 3-day EMA (double smoothing)."""
    r = _rsi_ema(close, 14)
    return _ewm_mean(r, 3)


def rsi_114_wilder_vs_ema_rsi14_diff(close: pd.Series) -> pd.Series:
    """Difference between Wilder RSI14 and EMA-RSI14 (method divergence)."""
    return _rsi(close, 14) - _rsi_ema(close, 14)


def rsi_115_ema_rsi14_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of EMA-RSI(14) within trailing 252-day distribution."""
    r = _rsi_ema(close, 14)
    return r.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group K (116-125): Connors RSI components and composite ---

def rsi_116_connors_rsi_streak_rsi(close: pd.Series) -> pd.Series:
    """Connors RSI component 1: RSI3 of the current up/down streak length."""
    delta = close.diff(1)
    sign = np.sign(delta)
    streak = _consec_streak(sign > 0) - _consec_streak(sign < 0)
    return _rsi(streak, 3)


def rsi_117_connors_rsi_pct_rank(close: pd.Series) -> pd.Series:
    """Connors RSI component 2: 100-day percentile rank of daily return."""
    ret = close.pct_change(1)
    return ret.rolling(100, min_periods=50).rank(pct=True) * 100.0


def rsi_118_connors_rsi_composite(close: pd.Series) -> pd.Series:
    """Full Connors RSI: average of RSI3, streak-RSI3, and 100d pct-rank."""
    rsi3 = _rsi(close, 3)
    streak_rsi = rsi_116_connors_rsi_streak_rsi(close)
    pct_rank = rsi_117_connors_rsi_pct_rank(close)
    return (rsi3 + streak_rsi + pct_rank) / 3.0


def rsi_119_connors_rsi_below20_flag(close: pd.Series) -> pd.Series:
    """Binary flag: Connors RSI composite is below 20."""
    return (rsi_118_connors_rsi_composite(close) < 20.0).astype(float)


def rsi_120_connors_rsi_depth_below30(close: pd.Series) -> pd.Series:
    """Depth of Connors RSI below 30."""
    return (30.0 - rsi_118_connors_rsi_composite(close)).clip(lower=0.0)


def rsi_121_connors_rsi_consec_below30(close: pd.Series) -> pd.Series:
    """Consecutive days Connors RSI is below 30."""
    return _consec_streak(rsi_118_connors_rsi_composite(close) < 30.0)


def rsi_122_connors_rsi_min_21d(close: pd.Series) -> pd.Series:
    """Minimum Connors RSI over trailing 21 days."""
    return _rolling_min(rsi_118_connors_rsi_composite(close), _TD_MON)


def rsi_123_connors_rsi_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of Connors RSI within trailing 252-day distribution."""
    crsi = rsi_118_connors_rsi_composite(close)
    return crsi.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rsi_124_connors_rsi_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of Connors RSI relative to 252-day distribution."""
    crsi = rsi_118_connors_rsi_composite(close)
    m = _rolling_mean(crsi, _TD_YEAR)
    s = _rolling_std(crsi, _TD_YEAR)
    return _safe_div(crsi - m, s)


def rsi_125_connors_rsi_oversold_intensity_21d(close: pd.Series) -> pd.Series:
    """Sum of (30 - Connors RSI) clipped to 0 over trailing 21 days."""
    depth = (30.0 - rsi_118_connors_rsi_composite(close)).clip(lower=0.0)
    return _rolling_sum(depth, _TD_MON)


# --- Group L (126-135): RSI divergence and cross-lookback relationships ---

def rsi_126_rsi7_minus_rsi14(close: pd.Series) -> pd.Series:
    """RSI7 minus RSI14 (fast vs slow momentum divergence)."""
    return _rsi(close, 7) - _rsi(close, 14)


def rsi_127_rsi14_minus_rsi63(close: pd.Series) -> pd.Series:
    """RSI14 minus RSI63 (short vs quarterly momentum spread)."""
    return _rsi(close, 14) - _rsi(close, _TD_QTR)


def rsi_128_rsi_composite_3periods(close: pd.Series) -> pd.Series:
    """Simple average of RSI7, RSI14, RSI21 (multi-period composite)."""
    return (_rsi(close, 7) + _rsi(close, 14) + _rsi(close, _TD_MON)) / 3.0


def rsi_129_rsi_composite_below30_flag(close: pd.Series) -> pd.Series:
    """Flag: the 3-period RSI composite is below 30."""
    return (rsi_128_rsi_composite_3periods(close) < 30.0).astype(float)


def rsi_130_rsi_composite_depth_below30(close: pd.Series) -> pd.Series:
    """Depth of 3-period RSI composite below 30."""
    return (30.0 - rsi_128_rsi_composite_3periods(close)).clip(lower=0.0)


def rsi_131_rsi_distress_score(close: pd.Series) -> pd.Series:
    """Distress score: sum of depth-below-30 across RSI7, RSI14, RSI21."""
    d7 = (30.0 - _rsi(close, 7)).clip(lower=0.0)
    d14 = (30.0 - _rsi(close, 14)).clip(lower=0.0)
    d21 = (30.0 - _rsi(close, _TD_MON)).clip(lower=0.0)
    return d7 + d14 + d21


def rsi_132_rsi_distress_score_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of RSI distress score within trailing 252 days."""
    score = rsi_131_rsi_distress_score(close)
    return score.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rsi_133_rsi14_declining_streak(close: pd.Series) -> pd.Series:
    """Consecutive days RSI14 is lower than prior day."""
    r = _rsi(close, 14)
    return _consec_streak(r < r.shift(1))


def rsi_134_all_rsi_declining_flag(close: pd.Series) -> pd.Series:
    """Flag: RSI7, RSI14, RSI21 all declined from prior day simultaneously."""
    r7 = _rsi(close, 7)
    r14 = _rsi(close, 14)
    r21 = _rsi(close, _TD_MON)
    return ((r7 < r7.shift(1)) & (r14 < r14.shift(1)) & (r21 < r21.shift(1))).astype(float)


def rsi_135_rsi14_below_rsi63_flag(close: pd.Series) -> pd.Series:
    """Flag: RSI14 < RSI63 (short-term weaker than long-term — bearish divergence)."""
    return (_rsi(close, 14) < _rsi(close, _TD_QTR)).astype(float)


# --- Group M (136-142): Price-series RSI variants (high, low, typical) ---

def rsi_136_rsi14_on_low(low: pd.Series) -> pd.Series:
    """Wilder RSI14 computed on intraday low prices."""
    return _rsi(low, 14)


def rsi_137_rsi14_low_below30_flag(low: pd.Series) -> pd.Series:
    """Flag: RSI14 of the low series is below 30."""
    return (_rsi(low, 14) < 30.0).astype(float)


def rsi_138_rsi14_low_depth_below30(low: pd.Series) -> pd.Series:
    """Depth of RSI14-of-lows below 30."""
    return (30.0 - _rsi(low, 14)).clip(lower=0.0)


def rsi_139_rsi14_typical_price(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """RSI14 of typical price (H+L+C)/3."""
    tp = (high + low + close) / 3.0
    return _rsi(tp, 14)


def rsi_140_rsi14_typical_below30_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: RSI14 of typical price is below 30."""
    return (rsi_139_rsi14_typical_price(close, high, low) < 30.0).astype(float)


def rsi_141_rsi14_typical_depth_below30(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Depth of RSI14-of-typical-price below 30."""
    return (30.0 - rsi_139_rsi14_typical_price(close, high, low)).clip(lower=0.0)


def rsi_142_rsi_cutler14(close: pd.Series) -> pd.Series:
    """Cutler RSI (simple-average) at 14-day lookback."""
    return _rsi_sma(close, 14)


# --- Group N (143-150): Distress composites, normalized, entry counts ---

def rsi_143_rsi14_oversold_intensity_252d(close: pd.Series) -> pd.Series:
    """Sum of RSI14 oversold depth (30-RSI, clipped) over trailing 252 days."""
    depth = (30.0 - _rsi(close, 14)).clip(lower=0.0)
    return _rolling_sum(depth, _TD_YEAR)


def rsi_144_rsi14_max_consecutive_below30_252d(close: pd.Series) -> pd.Series:
    """Maximum consecutive days RSI14 below 30 within trailing 252 days."""
    below = _rsi(close, 14) < 30.0

    def _max_run(arr):
        mx = 0
        cur = 0
        for v in arr:
            if v:
                cur += 1
                if cur > mx:
                    mx = cur
            else:
                cur = 0
        return float(mx)

    return below.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_max_run, raw=True)


def rsi_145_rsi14_oversold_entry_count_252d(close: pd.Series) -> pd.Series:
    """Count of distinct oversold entry events (RSI14 crosses below 30) in trailing 252 days."""
    r = _rsi(close, 14)
    entry = ((r < 30.0) & (r.shift(1) >= 30.0)).astype(float)
    return _rolling_sum(entry, _TD_YEAR)


def rsi_146_rsi14_expanding_zscore(close: pd.Series) -> pd.Series:
    """Expanding all-history z-score of RSI14."""
    r = _rsi(close, 14)
    m = r.expanding(min_periods=14).mean()
    s = r.expanding(min_periods=14).std()
    return _safe_div(r - m, s)


def rsi_147_stochrsi14_both_below20_flag(close: pd.Series) -> pd.Series:
    """Flag: both StochRSI(14) %K and %D are below 20 (double oversold confirmation)."""
    k = _stochrsi_k(close, 14, 14)
    d = _stochrsi_d(close, 14, 14, 3)
    return ((k < 20.0) & (d < 20.0)).astype(float)


def rsi_148_laguerre_g05_and_wilder14_both_below30(close: pd.Series) -> pd.Series:
    """Flag: both Laguerre RSI (gamma=0.5) and Wilder RSI14 are below 30."""
    lr = _laguerre_rsi(close, 0.5)
    wr = _rsi(close, 14)
    return ((lr < 30.0) & (wr < 30.0)).astype(float)


def rsi_149_ema_rsi14_and_wilder14_both_below30(close: pd.Series) -> pd.Series:
    """Flag: both EMA-RSI(14) and Wilder RSI14 are below 30 (cross-method oversold)."""
    return ((_rsi_ema(close, 14) < 30.0) & (_rsi(close, 14) < 30.0)).astype(float)


def rsi_150_stochrsi_laguerre_wilder_all_oversold(close: pd.Series) -> pd.Series:
    """Flag: StochRSI %K, Laguerre RSI, and Wilder RSI14 are ALL below oversold thresholds.
    (StochRSI K<20, Laguerre<30, Wilder<30) — maximum multi-method oversold signal.
    """
    k = _stochrsi_k(close, 14, 14)
    lr = _laguerre_rsi(close, 0.5)
    wr = _rsi(close, 14)
    return ((k < 20.0) & (lr < 30.0) & (wr < 30.0)).astype(float)


# ── Registry ──────────────────────────────────────────────────────────────────

RSI_EXTREMES_REGISTRY_076_150 = {
    "rsi_076_stochrsi14_k": {"inputs": ["close"], "func": rsi_076_stochrsi14_k},
    "rsi_077_stochrsi14_d": {"inputs": ["close"], "func": rsi_077_stochrsi14_d},
    "rsi_078_stochrsi21_k": {"inputs": ["close"], "func": rsi_078_stochrsi21_k},
    "rsi_079_stochrsi21_d": {"inputs": ["close"], "func": rsi_079_stochrsi21_d},
    "rsi_080_stochrsi14_k_below20_flag": {"inputs": ["close"], "func": rsi_080_stochrsi14_k_below20_flag},
    "rsi_081_stochrsi14_k_depth_below20": {"inputs": ["close"], "func": rsi_081_stochrsi14_k_depth_below20},
    "rsi_082_stochrsi14_k_consec_below20": {"inputs": ["close"], "func": rsi_082_stochrsi14_k_consec_below20},
    "rsi_083_stochrsi21_k_below20_flag": {"inputs": ["close"], "func": rsi_083_stochrsi21_k_below20_flag},
    "rsi_084_stochrsi21_k_depth_below20": {"inputs": ["close"], "func": rsi_084_stochrsi21_k_depth_below20},
    "rsi_085_stochrsi14_k_min_21d": {"inputs": ["close"], "func": rsi_085_stochrsi14_k_min_21d},
    "rsi_086_stochrsi14_k_pct_rank_252d": {"inputs": ["close"], "func": rsi_086_stochrsi14_k_pct_rank_252d},
    "rsi_087_stochrsi14_k_zscore_252d": {"inputs": ["close"], "func": rsi_087_stochrsi14_k_zscore_252d},
    "rsi_088_stochrsi14_d_below20_flag": {"inputs": ["close"], "func": rsi_088_stochrsi14_d_below20_flag},
    "rsi_089_stochrsi14_d_depth_below20": {"inputs": ["close"], "func": rsi_089_stochrsi14_d_depth_below20},
    "rsi_090_stochrsi14_kd_spread": {"inputs": ["close"], "func": rsi_090_stochrsi14_kd_spread},
    "rsi_091_laguerre_rsi_g05": {"inputs": ["close"], "func": rsi_091_laguerre_rsi_g05},
    "rsi_092_laguerre_rsi_g07": {"inputs": ["close"], "func": rsi_092_laguerre_rsi_g07},
    "rsi_093_laguerre_rsi_g05_below20_flag": {"inputs": ["close"], "func": rsi_093_laguerre_rsi_g05_below20_flag},
    "rsi_094_laguerre_rsi_g07_below20_flag": {"inputs": ["close"], "func": rsi_094_laguerre_rsi_g07_below20_flag},
    "rsi_095_laguerre_rsi_g05_depth_below20": {"inputs": ["close"], "func": rsi_095_laguerre_rsi_g05_depth_below20},
    "rsi_096_laguerre_rsi_g07_depth_below20": {"inputs": ["close"], "func": rsi_096_laguerre_rsi_g07_depth_below20},
    "rsi_097_laguerre_rsi_g05_consec_below20": {"inputs": ["close"], "func": rsi_097_laguerre_rsi_g05_consec_below20},
    "rsi_098_laguerre_rsi_g07_consec_below20": {"inputs": ["close"], "func": rsi_098_laguerre_rsi_g07_consec_below20},
    "rsi_099_laguerre_rsi_g05_min_21d": {"inputs": ["close"], "func": rsi_099_laguerre_rsi_g05_min_21d},
    "rsi_100_laguerre_rsi_g07_min_21d": {"inputs": ["close"], "func": rsi_100_laguerre_rsi_g07_min_21d},
    "rsi_101_laguerre_rsi_g05_pct_rank_252d": {"inputs": ["close"], "func": rsi_101_laguerre_rsi_g05_pct_rank_252d},
    "rsi_102_laguerre_rsi_g05_zscore_252d": {"inputs": ["close"], "func": rsi_102_laguerre_rsi_g05_zscore_252d},
    "rsi_103_ema_rsi14": {"inputs": ["close"], "func": rsi_103_ema_rsi14},
    "rsi_104_ema_rsi7": {"inputs": ["close"], "func": rsi_104_ema_rsi7},
    "rsi_105_ema_rsi21": {"inputs": ["close"], "func": rsi_105_ema_rsi21},
    "rsi_106_ema_rsi14_below30_flag": {"inputs": ["close"], "func": rsi_106_ema_rsi14_below30_flag},
    "rsi_107_ema_rsi7_below30_flag": {"inputs": ["close"], "func": rsi_107_ema_rsi7_below30_flag},
    "rsi_108_ema_rsi14_depth_below30": {"inputs": ["close"], "func": rsi_108_ema_rsi14_depth_below30},
    "rsi_109_ema_rsi7_depth_below30": {"inputs": ["close"], "func": rsi_109_ema_rsi7_depth_below30},
    "rsi_110_ema_rsi14_consec_below30": {"inputs": ["close"], "func": rsi_110_ema_rsi14_consec_below30},
    "rsi_111_ema_rsi14_min_21d": {"inputs": ["close"], "func": rsi_111_ema_rsi14_min_21d},
    "rsi_112_ema_rsi14_zscore_252d": {"inputs": ["close"], "func": rsi_112_ema_rsi14_zscore_252d},
    "rsi_113_ema_rsi14_smoothed_line": {"inputs": ["close"], "func": rsi_113_ema_rsi14_smoothed_line},
    "rsi_114_wilder_vs_ema_rsi14_diff": {"inputs": ["close"], "func": rsi_114_wilder_vs_ema_rsi14_diff},
    "rsi_115_ema_rsi14_pct_rank_252d": {"inputs": ["close"], "func": rsi_115_ema_rsi14_pct_rank_252d},
    "rsi_116_connors_rsi_streak_rsi": {"inputs": ["close"], "func": rsi_116_connors_rsi_streak_rsi},
    "rsi_117_connors_rsi_pct_rank": {"inputs": ["close"], "func": rsi_117_connors_rsi_pct_rank},
    "rsi_118_connors_rsi_composite": {"inputs": ["close"], "func": rsi_118_connors_rsi_composite},
    "rsi_119_connors_rsi_below20_flag": {"inputs": ["close"], "func": rsi_119_connors_rsi_below20_flag},
    "rsi_120_connors_rsi_depth_below30": {"inputs": ["close"], "func": rsi_120_connors_rsi_depth_below30},
    "rsi_121_connors_rsi_consec_below30": {"inputs": ["close"], "func": rsi_121_connors_rsi_consec_below30},
    "rsi_122_connors_rsi_min_21d": {"inputs": ["close"], "func": rsi_122_connors_rsi_min_21d},
    "rsi_123_connors_rsi_pct_rank_252d": {"inputs": ["close"], "func": rsi_123_connors_rsi_pct_rank_252d},
    "rsi_124_connors_rsi_zscore_252d": {"inputs": ["close"], "func": rsi_124_connors_rsi_zscore_252d},
    "rsi_125_connors_rsi_oversold_intensity_21d": {"inputs": ["close"], "func": rsi_125_connors_rsi_oversold_intensity_21d},
    "rsi_126_rsi7_minus_rsi14": {"inputs": ["close"], "func": rsi_126_rsi7_minus_rsi14},
    "rsi_127_rsi14_minus_rsi63": {"inputs": ["close"], "func": rsi_127_rsi14_minus_rsi63},
    "rsi_128_rsi_composite_3periods": {"inputs": ["close"], "func": rsi_128_rsi_composite_3periods},
    "rsi_129_rsi_composite_below30_flag": {"inputs": ["close"], "func": rsi_129_rsi_composite_below30_flag},
    "rsi_130_rsi_composite_depth_below30": {"inputs": ["close"], "func": rsi_130_rsi_composite_depth_below30},
    "rsi_131_rsi_distress_score": {"inputs": ["close"], "func": rsi_131_rsi_distress_score},
    "rsi_132_rsi_distress_score_pct_rank_252d": {"inputs": ["close"], "func": rsi_132_rsi_distress_score_pct_rank_252d},
    "rsi_133_rsi14_declining_streak": {"inputs": ["close"], "func": rsi_133_rsi14_declining_streak},
    "rsi_134_all_rsi_declining_flag": {"inputs": ["close"], "func": rsi_134_all_rsi_declining_flag},
    "rsi_135_rsi14_below_rsi63_flag": {"inputs": ["close"], "func": rsi_135_rsi14_below_rsi63_flag},
    "rsi_136_rsi14_on_low": {"inputs": ["low"], "func": rsi_136_rsi14_on_low},
    "rsi_137_rsi14_low_below30_flag": {"inputs": ["low"], "func": rsi_137_rsi14_low_below30_flag},
    "rsi_138_rsi14_low_depth_below30": {"inputs": ["low"], "func": rsi_138_rsi14_low_depth_below30},
    "rsi_139_rsi14_typical_price": {"inputs": ["close", "high", "low"], "func": rsi_139_rsi14_typical_price},
    "rsi_140_rsi14_typical_below30_flag": {"inputs": ["close", "high", "low"], "func": rsi_140_rsi14_typical_below30_flag},
    "rsi_141_rsi14_typical_depth_below30": {"inputs": ["close", "high", "low"], "func": rsi_141_rsi14_typical_depth_below30},
    "rsi_142_rsi_cutler14": {"inputs": ["close"], "func": rsi_142_rsi_cutler14},
    "rsi_143_rsi14_oversold_intensity_252d": {"inputs": ["close"], "func": rsi_143_rsi14_oversold_intensity_252d},
    "rsi_144_rsi14_max_consecutive_below30_252d": {"inputs": ["close"], "func": rsi_144_rsi14_max_consecutive_below30_252d},
    "rsi_145_rsi14_oversold_entry_count_252d": {"inputs": ["close"], "func": rsi_145_rsi14_oversold_entry_count_252d},
    "rsi_146_rsi14_expanding_zscore": {"inputs": ["close"], "func": rsi_146_rsi14_expanding_zscore},
    "rsi_147_stochrsi14_both_below20_flag": {"inputs": ["close"], "func": rsi_147_stochrsi14_both_below20_flag},
    "rsi_148_laguerre_g05_and_wilder14_both_below30": {"inputs": ["close"], "func": rsi_148_laguerre_g05_and_wilder14_both_below30},
    "rsi_149_ema_rsi14_and_wilder14_both_below30": {"inputs": ["close"], "func": rsi_149_ema_rsi14_and_wilder14_both_below30},
    "rsi_150_stochrsi_laguerre_wilder_all_oversold": {"inputs": ["close"], "func": rsi_150_stochrsi_laguerre_wilder_all_oversold},
}
