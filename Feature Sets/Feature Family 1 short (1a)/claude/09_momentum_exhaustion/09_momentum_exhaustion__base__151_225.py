"""momentum_exhaustion base features 151-225 — Pipeline 1a-inverse short-side blowup family (gap-fill extension).

Extension beyond the original 150 — fills audit-identified gaps for momentum-exhaustion / overbought-short detection.
This file carries indices 151-157 (7 distinct hypotheses). Reserved range up to 225.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(-N). Self-contained — no imports across families.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5


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


def _true_range(high, low, close):
    pc = close.shift(1)
    return pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)


def _atr(high, low, close, n=21):
    return _true_range(high, low, close).rolling(n, min_periods=max(n // 3, 2)).mean()


def _wilder_rsi(close, n=14):
    """Wilder's RSI: SMMA of gains/losses with alpha=1/n."""
    delta = close.diff()
    gain = delta.clip(lower=0.0)
    loss = (-delta).clip(lower=0.0)
    avg_gain = gain.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    avg_loss = loss.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    rs = _safe_div(avg_gain, avg_loss)
    return 100.0 - 100.0 / (1.0 + rs)


# ============================================================
#                    FEATURES 151-157
# ============================================================


def f09_mexh_151_squeeze_momentum_lazybear(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """BB(20,2) inside Keltner(20, 1.5*ATR) squeeze + linreg momentum sign on close[20]."""
    n = 20
    mid = close.rolling(n, min_periods=max(n // 3, 2)).mean()
    sd = close.rolling(n, min_periods=max(n // 3, 2)).std(ddof=0)
    bb_upper = mid + 2.0 * sd
    bb_lower = mid - 2.0 * sd
    atr = _atr(high, low, close, n=n)
    kc_upper = mid + 1.5 * atr
    kc_lower = mid - 1.5 * atr
    bb_in_kc = ((bb_upper < kc_upper) & (bb_lower > kc_lower)).astype(float)

    def _slope(w):
        valid = ~np.isnan(w)
        if valid.sum() < max(n // 2, 5):
            return np.nan
        y = w[valid]
        x = np.arange(len(w), dtype=float)[valid]
        try:
            b, _ = np.polyfit(x, y, 1)
        except Exception:
            return np.nan
        return float(b)

    slope = close.rolling(n, min_periods=max(n // 2, 5)).apply(_slope, raw=True)
    sign = np.sign(slope)
    return bb_in_kc * sign


def f09_mexh_152_wave_trend_oscillator_overbought_sell_count_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """WTO overbought sell signal count (wt1>60 AND wt1 crosses below wt2) in trailing 63d."""
    hlc3 = (high + low + close) / 3.0
    esa = hlc3.ewm(span=10, adjust=False, min_periods=10).mean()
    d = (hlc3 - esa).abs().ewm(span=10, adjust=False, min_periods=10).mean()
    ci = _safe_div(hlc3 - esa, 0.015 * d)
    wt1 = ci.ewm(span=21, adjust=False, min_periods=21).mean()
    wt2 = wt1.rolling(4, min_periods=4).mean()
    cross_down = (wt1.shift(1) >= wt2.shift(1)) & (wt1 < wt2)
    fire = ((wt1 > 60.0) & cross_down).astype(float)
    return fire.rolling(QDAYS, min_periods=MDAYS).sum()


def f09_mexh_153_fisher_transform_rsi_14(close: pd.Series) -> pd.Series:
    """Fisher transform of Wilder RSI14: x=(RSI-50)/50 clipped to (-0.999,0.999); 0.5*log((1+x)/(1-x))."""
    rsi = _wilder_rsi(close, n=14)
    x = (rsi - 50.0) / 50.0
    x = x.clip(lower=-0.999, upper=0.999)
    return 0.5 * np.log(_safe_div(1.0 + x, 1.0 - x))


def f09_mexh_154_rvi_bearish_divergence_count_63d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """RVI bearish divergence count: close new 21d high AND RVI below its 21d-prior max, summed over 63d."""
    num = (close - open_).rolling(10, min_periods=10).sum()
    den = (high - low).rolling(10, min_periods=10).sum()
    rvi = _safe_div(num, den)
    close_new_high = close >= close.rolling(MDAYS, min_periods=MDAYS).max()
    rvi_prior_max = rvi.shift(1).rolling(MDAYS, min_periods=MDAYS).max()
    rvi_below = rvi < rvi_prior_max
    bar = (close_new_high & rvi_below).astype(float)
    return bar.rolling(QDAYS, min_periods=MDAYS).sum()


def f09_mexh_155_td_sequential_setup_9_count_63d(close: pd.Series) -> pd.Series:
    """DeMark sell setup completion (9 consecutive bars close > close.shift(4)) count in trailing 63d."""
    cond = (close > close.shift(4)).astype(float)
    # streak counter: increments while cond is True, resets to 0 when False.
    # Using cumulative trick: group resets at False bars.
    group = (cond == 0).cumsum()
    streak = cond.groupby(group).cumsum()
    completed = (streak == 9).astype(float)
    return completed.rolling(QDAYS, min_periods=MDAYS).sum()


def f09_mexh_156_stoch_overbought_exit_count_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars in 63d where Stoch K(14) crossed below 80 from above."""
    n = 14
    hh = high.rolling(n, min_periods=n).max()
    ll = low.rolling(n, min_periods=n).min()
    k = 100.0 * _safe_div(close - ll, hh - ll)
    exit_bar = ((k.shift(1) >= 80.0) & (k < 80.0)).astype(float)
    return exit_bar.rolling(QDAYS, min_periods=MDAYS).sum()


def f09_mexh_157_rsi_overbought_exit_count_63d(close: pd.Series) -> pd.Series:
    """Count of bars in 63d where Wilder RSI(14) crossed below 70 from above."""
    rsi = _wilder_rsi(close, n=14)
    exit_bar = ((rsi.shift(1) >= 70.0) & (rsi < 70.0)).astype(float)
    return exit_bar.rolling(QDAYS, min_periods=MDAYS).sum()


# ============================================================
#                    REGISTRY
# ============================================================

MOMENTUM_EXHAUSTION_BASE_REGISTRY_151_225 = {
    "f09_mexh_151_squeeze_momentum_lazybear": {"inputs": ["close", "high", "low"], "func": f09_mexh_151_squeeze_momentum_lazybear},
    "f09_mexh_152_wave_trend_oscillator_overbought_sell_count_63d": {"inputs": ["high", "low", "close"], "func": f09_mexh_152_wave_trend_oscillator_overbought_sell_count_63d},
    "f09_mexh_153_fisher_transform_rsi_14": {"inputs": ["close"], "func": f09_mexh_153_fisher_transform_rsi_14},
    "f09_mexh_154_rvi_bearish_divergence_count_63d": {"inputs": ["open", "high", "low", "close"], "func": f09_mexh_154_rvi_bearish_divergence_count_63d},
    "f09_mexh_155_td_sequential_setup_9_count_63d": {"inputs": ["close"], "func": f09_mexh_155_td_sequential_setup_9_count_63d},
    "f09_mexh_156_stoch_overbought_exit_count_63d": {"inputs": ["high", "low", "close"], "func": f09_mexh_156_stoch_overbought_exit_count_63d},
    "f09_mexh_157_rsi_overbought_exit_count_63d": {"inputs": ["close"], "func": f09_mexh_157_rsi_overbought_exit_count_63d},
}
