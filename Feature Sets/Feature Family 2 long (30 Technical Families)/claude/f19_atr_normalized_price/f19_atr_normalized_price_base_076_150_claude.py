"""f19_atr_normalized_price base features 076-150.

Domain: ATR-normalized price -- this file is structurally distinct from
001-075 (no shared expression up to a window change). Uses different
families: ATR(N) with N values not in file 1, alternative band-types
(Chandelier exits, ATR-trail), parabolic-style ATR distances, Donchian
in ATR units, ratios using Wilder vs simple-MA TR, OHLC-based positions
in ATR, ATR-weighted MA, Mahalanobis-like z in ATR, ATR-of-ATR ratios,
plus signed and bounded transforms unique to this file.

NaN policy: never fillna(<value>); only replace([inf,-inf], nan) at
the function's final return. Window > 21d uses closeadj; <=21d uses
close. Each feature spells its full formula inline.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Helpers (lightweight). Every feature still spells the formula inline.
# ---------------------------------------------------------------------------


def _tr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    pc = close.shift(1)
    a = (high - low).abs()
    b = (high - pc).abs()
    c = (low - pc).abs()
    return pd.concat([a, b, c], axis=1).max(axis=1)


# ---------------------------------------------------------------------------
# Features 076-150
# ---------------------------------------------------------------------------


# === ATR-normalized N-day high differentials (distinct windows) ============

def f19an_f19_atr_normalized_price_close_minus_high40_atr_25d_base_v076_signal(high, low, closeadj):
    """(closeadj - rolling_max(high,40)) / ATR(25)."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 25.0, adjust=False, min_periods=25).mean()
    hh = high.rolling(40, min_periods=40).max()
    return ((closeadj - hh) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_close_minus_low40_atr_25d_base_v077_signal(high, low, closeadj):
    """(closeadj - rolling_min(low,40)) / ATR(25)."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 25.0, adjust=False, min_periods=25).mean()
    ll = low.rolling(40, min_periods=40).min()
    return ((closeadj - ll) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Chandelier-exit ATR distance =========================================

def f19an_f19_atr_normalized_price_chandelier_exit_long_22d_base_v078_signal(high, low, closeadj):
    """((rolling_max(high,22) - 3*ATR(22)) - closeadj) / ATR(22).
    Chandelier-exit (long) distance in ATR units. Negative => price above stop."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 22.0, adjust=False, min_periods=22).mean()
    hh = high.rolling(22, min_periods=22).max()
    exit_long = hh - 3.0 * atr
    return ((exit_long - closeadj) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_chandelier_exit_short_22d_base_v079_signal(high, low, closeadj):
    """(closeadj - (rolling_min(low,22) + 3*ATR(22))) / ATR(22).
    Chandelier-exit (short) distance in ATR units. Negative => price below stop."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 22.0, adjust=False, min_periods=22).mean()
    ll = low.rolling(22, min_periods=22).min()
    exit_short = ll + 3.0 * atr
    return ((closeadj - exit_short) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === SuperTrend-style ATR offset distance ==================================

def f19an_f19_atr_normalized_price_supertrend_dist_atr_15d_base_v080_signal(high, low, close):
    """((high+low)/2 - 3*ATR(15) - close) / ATR(15). SuperTrend lower-line distance."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 15.0, adjust=False, min_periods=15).mean()
    mid = (high + low) / 2.0
    return ((mid - 3.0 * atr - close) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Donchian channel position in ATR ======================================

def f19an_f19_atr_normalized_price_donchian_pos_20d_atr_base_v081_signal(high, low, close):
    """(close - rolling_min(low,20) - 0.5*(rolling_max(high,20)-rolling_min(low,20))) / ATR(20).
    Distance from Donchian mid in ATR units."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 20.0, adjust=False, min_periods=20).mean()
    hh = high.rolling(20, min_periods=20).max()
    ll = low.rolling(20, min_periods=20).min()
    mid = 0.5 * (hh + ll)
    return ((close - mid) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_donchian_width_55d_atr_base_v082_signal(high, low, closeadj):
    """(rolling_max(high,55) - rolling_min(low,55)) / ATR(40). Donchian width in ATR units."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 40.0, adjust=False, min_periods=40).mean()
    hh = high.rolling(55, min_periods=55).max()
    ll = low.rolling(55, min_periods=55).min()
    return ((hh - ll) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === ATR-weighted MA distance ==============================================

def f19an_f19_atr_normalized_price_atr_weighted_ma_dist_30d_base_v083_signal(high, low, closeadj):
    """(closeadj - ATR-weighted-mean(closeadj, 30)) / ATR(15). Vol-weighted MA distance.
    Weights are higher when ATR(15) is small (low-vol bars carry more weight)."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 15.0, adjust=False, min_periods=15).mean()
    w = 1.0 / atr.replace(0.0, np.nan)
    num = (closeadj * w).rolling(30, min_periods=30).sum()
    den = w.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    mw = num / den
    return ((closeadj - mw) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === ATR(N) using simple-MA of TR vs Wilder ratio ==========================

def f19an_f19_atr_normalized_price_atr_smooth_diff_25d_base_v084_signal(high, low, closeadj):
    """(SimpleMA(TR,25) - WilderATR(25)) / WilderATR(25). Smoothing-method bias."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    sma_tr = tr.rolling(25, min_periods=25).mean()
    wild = tr.ewm(alpha=1.0 / 25.0, adjust=False, min_periods=25).mean()
    return ((sma_tr - wild) / wild.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Three-bar move in ATR units ==========================================

def f19an_f19_atr_normalized_price_3bar_move_atr_short_base_v085_signal(high, low, close):
    """(close - close.shift(3)) / ATR(7). 3-bar move in short-ATR units."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 7.0, adjust=False, min_periods=7).mean()
    return ((close - close.shift(3)) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_10bar_move_atr_25d_base_v086_signal(high, low, close):
    """(close - close.shift(10)) / ATR(25). 10-bar move scaled by 25-day ATR."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 25.0, adjust=False, min_periods=25).mean()
    return ((close - close.shift(10)) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Cross-ATR-window slope ===============================================

def f19an_f19_atr_normalized_price_atr_short_minus_long_pct_base_v087_signal(high, low, closeadj):
    """(ATR(7) - ATR(70)) / ATR(70). Short-vs-long ATR percent gap."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    a7 = tr.ewm(alpha=1.0 / 7.0, adjust=False, min_periods=7).mean()
    a70 = tr.ewm(alpha=1.0 / 70.0, adjust=False, min_periods=70).mean()
    return ((a7 - a70) / a70.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)




def f19an_f19_atr_normalized_price_atr_pct_close_long_base_v089_signal(high, low, closeadj):
    """ATR(60) / closeadj. Long-horizon vol-percent in ATR domain."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 60.0, adjust=False, min_periods=60).mean()
    return (atr / closeadj.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Counts of ATR thresholds w/ different windows ========================

def f19an_f19_atr_normalized_price_count_15atr_45d_base_v090_signal(high, low, closeadj):
    """count of bars in 45d where |daily ret| > 1.5*ATR(20)."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 20.0, adjust=False, min_periods=20).mean()
    flag = ((closeadj - pc).abs() > 1.5 * atr).astype(float).where(~atr.isna() & ~pc.isna())
    return flag.rolling(45, min_periods=45).sum().replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_max_5d_move_atr_252d_base_v091_signal(high, low, closeadj):
    """max(|closeadj - closeadj.shift(5)|, 252) / ATR(40). Worst 5-bar ATR-shock over 1 year.
    Continuous (replaces threshold-count). Structurally distinct from 1-day max-absret / ATR
    (uses a 5-day window inside the max, longer ATR, longer rolling)."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 40.0, adjust=False, min_periods=40).mean()
    five = (closeadj - closeadj.shift(5)).abs()
    mx = five.rolling(252, min_periods=252).max()
    return (mx / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Days since fresh ATR-high event =======================================

def f19an_f19_atr_normalized_price_max_signed_ret_atr_180d_base_v092_signal(high, low, closeadj):
    """max((closeadj-pc)/ATR(14)) over 180d. Worst signed up-shock in ATR units (continuous)."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    z = (closeadj - pc) / atr.replace(0.0, np.nan)
    return z.rolling(180, min_periods=180).max().replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_min_signed_ret_atr_180d_base_v093_signal(high, low, closeadj):
    """min((closeadj-pc)/ATR(14)) over 180d. Worst signed down-shock in ATR units (continuous)."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    z = (closeadj - pc) / atr.replace(0.0, np.nan)
    return z.rolling(180, min_periods=180).min().replace([np.inf, -np.inf], np.nan)


# === Body/range ATR features ==============================================

def f19an_f19_atr_normalized_price_avg_body_atr_30d_base_v094_signal(high, low, closeadj, open):
    """mean(|close - open|, 30) / ATR(20). Average body magnitude in ATR units."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 20.0, adjust=False, min_periods=20).mean()
    body = (closeadj - open).abs()
    return (body.rolling(30, min_periods=30).mean() / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_avg_range_atr_50d_base_v095_signal(high, low, closeadj):
    """mean(high-low, 50) / ATR(50). Average daily range in ATR(50) units."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 50.0, adjust=False, min_periods=50).mean()
    rng = (high - low).rolling(50, min_periods=50).mean()
    return (rng / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Position within HL range scaled by ATR ===============================

def f19an_f19_atr_normalized_price_williamsR_in_atr_band_30d_base_v096_signal(high, low, close):
    """Williams %R variant: (rolling_max(high,14) - close) / ATR(14). Distance to recent high in ATR units (>=0)."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    hh = high.rolling(14, min_periods=14).max()
    return ((hh - close) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Multi-window ATR-units ratio =========================================

def f19an_f19_atr_normalized_price_30d_move_vs_60d_atr_base_v097_signal(high, low, closeadj):
    """(closeadj - closeadj.shift(30)) / (sqrt(30) * ATR(60)). 30d move in 60d ATR units (sqrt-scaled)."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 60.0, adjust=False, min_periods=60).mean()
    return ((closeadj - closeadj.shift(30)) / (np.sqrt(30.0) * atr).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === ATR upper-vs-lower wick aggregate ====================================

def f19an_f19_atr_normalized_price_upwick_minus_lowwick_atr_15d_base_v098_signal(high, low, close, open):
    """5d-sum of ((high - max(o,c)) - (min(o,c) - low)) / ATR(14). Asymmetric wick bias."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    top = pd.concat([open, close], axis=1).max(axis=1)
    bot = pd.concat([open, close], axis=1).min(axis=1)
    asym = (high - top) - (bot - low)
    return (asym.rolling(15, min_periods=15).sum() / (15.0 * atr).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === ATR-z transformed close (with rolling mean of ATR-z) =================

def f19an_f19_atr_normalized_price_zscore_close_atr_15d_base_v099_signal(high, low, close):
    """(close - rolling_mean(close,15)) / (ATR(15)). 15d z in ATR units."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 15.0, adjust=False, min_periods=15).mean()
    m = close.rolling(15, min_periods=15).mean()
    return ((close - m) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Sign features around different ATR bands =============================

def f19an_f19_atr_normalized_price_above_05atr_sma8_base_v100_signal(high, low, close):
    """1 if close > SMA(8) + 0.5*ATR(8), -1 if < SMA(8) - 0.5*ATR(8), else 0. Tight band sign."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 8.0, adjust=False, min_periods=8).mean()
    sma = close.rolling(8, min_periods=8).mean()
    upper = sma + 0.5 * atr
    lower = sma - 0.5 * atr
    out = pd.Series(0.0, index=close.index, dtype=float)
    out = out.where(close <= upper, 1.0)
    out = out.where(close >= lower, -1.0)
    return out.where(~atr.isna() & ~sma.isna()).replace([np.inf, -np.inf], np.nan)


# === EMA cross magnitude in ATR ===========================================

def f19an_f19_atr_normalized_price_ema_cross_mag_atr_8_30_base_v101_signal(high, low, close):
    """(EMA(8) - EMA(30)) / ATR(15). Short-mid EMA spread in ATR units."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 15.0, adjust=False, min_periods=15).mean()
    e8 = close.ewm(span=8, adjust=False, min_periods=8).mean()
    e30 = close.ewm(span=30, adjust=False, min_periods=30).mean()
    return ((e8 - e30) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_ema_cross_mag_atr_20_80_base_v102_signal(high, low, closeadj):
    """(EMA(20) - EMA(80)) / ATR(40). Mid-long EMA spread in ATR units."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 40.0, adjust=False, min_periods=40).mean()
    e20 = closeadj.ewm(span=20, adjust=False, min_periods=20).mean()
    e80 = closeadj.ewm(span=80, adjust=False, min_periods=80).mean()
    return ((e20 - e80) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === ATR-units cross differences with different windows ===================

def f19an_f19_atr_normalized_price_atr_slope_5d_norm_base_v103_signal(high, low, close):
    """(ATR(7) - ATR(7).shift(5)) / ATR(7). Short ATR slope normalized."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    a = tr.ewm(alpha=1.0 / 7.0, adjust=False, min_periods=7).mean()
    return ((a - a.shift(5)) / a.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_atr_slope_90d_norm_base_v104_signal(high, low, closeadj):
    """(ATR(60) - ATR(60).shift(90)) / ATR(60). Very long ATR slope normalized."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    a = tr.ewm(alpha=1.0 / 60.0, adjust=False, min_periods=60).mean()
    return ((a - a.shift(90)) / a.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Median TR vs ATR =====================================================

def f19an_f19_atr_normalized_price_median_tr_atr_45d_base_v105_signal(high, low, closeadj):
    """median(TR, 45) / ATR(45). Robust-vs-Wilder vol ratio (mu-of-tr / wilder-of-tr)."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    med_tr = tr.rolling(45, min_periods=45).median()
    atr = tr.ewm(alpha=1.0 / 45.0, adjust=False, min_periods=45).mean()
    return (med_tr / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === ATR-units rolling correlation between ATR and close ==================

def f19an_f19_atr_normalized_price_atr_close_corr_60d_base_v106_signal(high, low, closeadj):
    """Rolling 60d corr(ATR(14), closeadj). Vol-up-with-trend regime detector."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    return atr.rolling(60, min_periods=60).corr(closeadj).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_atr_logret_corr_120d_base_v107_signal(high, low, closeadj):
    """Rolling 120d corr(ATR(14), abs(daily logret)). Same-direction vol-shock relationship."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    ar = np.log(closeadj / pc).abs()
    return atr.rolling(120, min_periods=120).corr(ar).replace([np.inf, -np.inf], np.nan)


# === Z-score of move in long-ATR vs short-ATR ratio ========================

def f19an_f19_atr_normalized_price_short_vs_long_move_atr_60d_base_v108_signal(high, low, closeadj):
    """((closeadj - closeadj.shift(10))/ATR(10)) - ((closeadj - closeadj.shift(60))/ATR(60)).
    Short-vs-long horizon ATR-momentum spread."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    a10 = tr.ewm(alpha=1.0 / 10.0, adjust=False, min_periods=10).mean()
    a60 = tr.ewm(alpha=1.0 / 60.0, adjust=False, min_periods=60).mean()
    z10 = (closeadj - closeadj.shift(10)) / a10.replace(0.0, np.nan)
    z60 = (closeadj - closeadj.shift(60)) / a60.replace(0.0, np.nan)
    return (z10 - z60).replace([np.inf, -np.inf], np.nan)


# === ATR-units sum of recent up-bars minus down-bars =====================

def f19an_f19_atr_normalized_price_signed_ret_atr_sum_20d_base_v109_signal(high, low, close):
    """Sum over 20d of sign(close - pc) * |close - pc| / ATR(14). Path bias in ATR units."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    z = (close - pc) / atr.replace(0.0, np.nan)
    return z.rolling(20, min_periods=20).sum().replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_signed_ret_atr_sum_80d_base_v110_signal(high, low, closeadj):
    """Sum over 80d of (close - pc)/ATR(14). Long path bias in ATR units."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    z = (closeadj - pc) / atr.replace(0.0, np.nan)
    return z.rolling(80, min_periods=80).sum().replace([np.inf, -np.inf], np.nan)


# === ATR-z autocorr at different lags =====================================

def f19an_f19_atr_normalized_price_retatr_lag5_autocorr_100d_base_v111_signal(high, low, closeadj):
    """Lag-5 autocorr of daily (ret/ATR(14)) over 100d. Mean-reversion / momentum balance."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    z = (closeadj - pc) / atr.replace(0.0, np.nan)
    return z.rolling(100, min_periods=100).corr(z.shift(5)).replace([np.inf, -np.inf], np.nan)


# === ATR-units gap variants ===============================================

def f19an_f19_atr_normalized_price_abs_gap_mean_atr_30d_base_v112_signal(high, low, close, open):
    """mean over 30d of |open - prev_close| / ATR(14). Mean unsigned overnight shock magnitude,
    structurally distinct from signed 30d move (this is always >= 0)."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    ag = (open - pc).abs() / atr.replace(0.0, np.nan)
    return ag.rolling(30, min_periods=30).mean().replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_gap_std_atr_45d_base_v113_signal(high, low, close, open):
    """std over 45d of (open - prev_close) / ATR(14). Dispersion of ATR-gaps."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    gap = (open - pc) / atr.replace(0.0, np.nan)
    return gap.rolling(45, min_periods=45).std().replace([np.inf, -np.inf], np.nan)


# === Rolling skew/kurt of ATR =============================================

def f19an_f19_atr_normalized_price_atr_skew_60d_base_v114_signal(high, low, closeadj):
    """Skew of ATR(14) over 60d. Asymmetry in vol regime."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    return atr.rolling(60, min_periods=60).skew().replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_atr_kurt_120d_base_v115_signal(high, low, closeadj):
    """Kurtosis of ATR(14) over 120d. Vol-spike fatness."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    return atr.rolling(120, min_periods=120).kurt().replace([np.inf, -np.inf], np.nan)


# === ATR variations relative to volume-weighted price ====================

def f19an_f19_atr_normalized_price_vol_weighted_atr_dispersion_base_v116_signal(high, low, closeadj, volume):
    """Volume-weighted standard deviation of (closeadj-pc)/ATR(14) over 30d, minus simple-weight std.
    Captures whether high-volume bars are MORE or LESS dispersed (in ATR-units) than average bars
    -- a microstructure / volume-conditional vol-of-ATR-move statistic, structurally distinct."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    z = (closeadj - pc) / atr.replace(0.0, np.nan)
    z2 = z * z
    wsum = volume.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    wm = (volume * z).rolling(30, min_periods=30).sum() / wsum
    wm2 = (volume * z2).rolling(30, min_periods=30).sum() / wsum
    vw_var = (wm2 - wm * wm).clip(lower=0.0)
    eq_var = z.rolling(30, min_periods=30).var()
    return (vw_var.pow(0.5) - eq_var.pow(0.5)).replace([np.inf, -np.inf], np.nan)


# === ATR-units HMA distance ===============================================

def f19an_f19_atr_normalized_price_hma_dist_atr_30d_base_v117_signal(high, low, closeadj):
    """(closeadj - HMA(30)) / ATR(20). Hull-MA distance in ATR units.
    HMA(n) = WMA(2*WMA(n/2) - WMA(n), sqrt(n))."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 20.0, adjust=False, min_periods=20).mean()
    n = 30; half = 15; sqn = 5
    w_half = np.arange(1, half + 1, dtype=float); w_half /= w_half.sum()
    w_n = np.arange(1, n + 1, dtype=float); w_n /= w_n.sum()
    w_sqn = np.arange(1, sqn + 1, dtype=float); w_sqn /= w_sqn.sum()
    wma_half = closeadj.rolling(half, min_periods=half).apply(lambda x: float(np.dot(x, w_half)), raw=True)
    wma_n = closeadj.rolling(n, min_periods=n).apply(lambda x: float(np.dot(x, w_n)), raw=True)
    raw = 2.0 * wma_half - wma_n
    hma = raw.rolling(sqn, min_periods=sqn).apply(lambda x: float(np.dot(x, w_sqn)), raw=True)
    return ((closeadj - hma) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Counting flips in ATR-band-state ====================================

def f19an_f19_atr_normalized_price_atr_state_flips_80d_base_v118_signal(high, low, closeadj):
    """Number of state changes (in 80d) of sign((closeadj-SMA(40))/ATR(40) - 0.5*sign).
    Discrete-state instability measure."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 40.0, adjust=False, min_periods=40).mean()
    sma = closeadj.rolling(40, min_periods=40).mean()
    z = (closeadj - sma) / atr.replace(0.0, np.nan)
    state = pd.Series(0.0, index=closeadj.index, dtype=float)
    state = state.where(z <= 0.5, 1.0)
    state = state.where(z >= -0.5, -1.0)
    flip = (state != state.shift(1)).astype(float).where(~state.isna() & ~state.shift(1).isna())
    return flip.rolling(80, min_periods=80).sum().replace([np.inf, -np.inf], np.nan)


# === ATR-normalized log-return mean over different windows ==============

def f19an_f19_atr_normalized_price_logret_mean_atr_15d_base_v119_signal(high, low, close):
    """mean(log_return, 15) / (ATR(15)/close). Short Sharpe in ATR units (independent window from f1)."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 15.0, adjust=False, min_periods=15).mean()
    r = np.log(close / close.shift(1))
    return (r.rolling(15, min_periods=15).mean() / (atr / close.replace(0.0, np.nan)).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_logret_mean_atr_120d_base_v120_signal(high, low, closeadj):
    """mean(log_return, 120) / (ATR(120)/closeadj). Long Sharpe in ATR units."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 120.0, adjust=False, min_periods=120).mean()
    r = np.log(closeadj / closeadj.shift(1))
    return (r.rolling(120, min_periods=120).mean() / (atr / closeadj.replace(0.0, np.nan)).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === ATR-units rolling max/min of ATR ratio ==============================

def f19an_f19_atr_normalized_price_atr_rmax_rmin_ratio_40d_base_v121_signal(high, low, closeadj):
    """rolling_max(ATR(14),40) / rolling_min(ATR(14),40). Span of vol over 40d."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    mx = atr.rolling(40, min_periods=40).max()
    mn = atr.rolling(40, min_periods=40).min().replace(0.0, np.nan)
    return (mx / mn).replace([np.inf, -np.inf], np.nan)


# === Skew of (ret/ATR) and (ret/ATR)^2 ====================================

def f19an_f19_atr_normalized_price_skew_atr_sq_ret_120d_base_v122_signal(high, low, closeadj):
    """Skew of ((ret/ATR(14))^2) over 120d. Tail asymmetry of squared returns."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    z = ((closeadj - pc) / atr.replace(0.0, np.nan)) ** 2
    return z.rolling(120, min_periods=120).skew().replace([np.inf, -np.inf], np.nan)


# === Z-score using ATR-based MAD ==========================================

def f19an_f19_atr_normalized_price_atr_z_iqr_90d_base_v123_signal(high, low, closeadj):
    """Inter-quartile range (q75-q25) of (closeadj-pc)/ATR(14) over 90d. Robust dispersion of
    daily ATR-moves. Structurally distinct from level-distance MA features."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    z = (closeadj - pc) / atr.replace(0.0, np.nan)
    q75 = z.rolling(90, min_periods=90).quantile(0.75)
    q25 = z.rolling(90, min_periods=90).quantile(0.25)
    return (q75 - q25).replace([np.inf, -np.inf], np.nan)


# === Days since ATR regime change =========================================

def f19an_f19_atr_normalized_price_days_since_high_atr_252d_base_v124_signal(high, low, closeadj):
    """Days since ATR(14) > 80th percentile of ATR(14) over 252d. Time since elevated vol."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    q80 = atr.rolling(252, min_periods=252).quantile(0.8)
    flag = (atr > q80).astype(float).where(~atr.isna() & ~q80.isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return float(len(x))
        return float(len(x) - 1 - idx[-1])
    return flag.rolling(252, min_periods=252).apply(_ds, raw=True).replace([np.inf, -np.inf], np.nan)


# === Discrete signed move classification =================================

def f19an_f19_atr_normalized_price_atr_move_bucket_base_v125_signal(high, low, close):
    """Bucket of (close - pc)/ATR(14): -2 if <-2; -1 if <-1; 0 if |z|<=1; 1 if >1; 2 if >2."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    z = (close - pc) / atr.replace(0.0, np.nan)
    out = pd.Series(0.0, index=close.index, dtype=float)
    out = out.where(z <= 1.0, 1.0)
    out = out.where(z <= 2.0, 2.0)
    out = out.where(z >= -1.0, -1.0)
    out = out.where(z >= -2.0, -2.0)
    return out.where(~z.isna()).replace([np.inf, -np.inf], np.nan)


# === ATR-units cumulative path length =====================================

def f19an_f19_atr_normalized_price_path_atr_efficiency_30d_base_v126_signal(high, low, closeadj):
    """|closeadj - closeadj.shift(30)| / sum(|daily ret|,30). Efficiency ratio; ATR domain via:
    sum of TR/ATR(30) over 30d represents cumulative ATR-units path."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 30.0, adjust=False, min_periods=30).mean()
    cum_path = (tr / atr.replace(0.0, np.nan)).rolling(30, min_periods=30).sum()
    net = (closeadj - closeadj.shift(30)).abs() / atr.replace(0.0, np.nan)
    return (net / cum_path.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Donchian breakout: distance to last week high in ATR ================

def f19an_f19_atr_normalized_price_dist_high5_atr_short_base_v127_signal(high, low, close):
    """(close - rolling_max(high,5)) / ATR(7). Distance to last week's high in short-ATR."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 7.0, adjust=False, min_periods=7).mean()
    hh = high.rolling(5, min_periods=5).max()
    return ((close - hh) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === ATR-units price acceleration ========================================

def f19an_f19_atr_normalized_price_accel_atr_15d_base_v128_signal(high, low, close):
    """(close - 2*close.shift(15) + close.shift(30)) / ATR(15). Curvature in ATR units."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 15.0, adjust=False, min_periods=15).mean()
    return ((close - 2.0 * close.shift(15) + close.shift(30)) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_accel_atr_60d_base_v129_signal(high, low, closeadj):
    """(closeadj - 2*closeadj.shift(60) + closeadj.shift(120)) / ATR(60). Long curvature."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 60.0, adjust=False, min_periods=60).mean()
    return ((closeadj - 2.0 * closeadj.shift(60) + closeadj.shift(120)) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Sigmoid of long-horizon ATR-z =======================================

def f19an_f19_atr_normalized_price_sigmoid_long_atr_z_base_v130_signal(high, low, closeadj):
    """1/(1+exp(-z)) where z = (closeadj - SMA(120))/ATR(60)."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 60.0, adjust=False, min_periods=60).mean()
    sma = closeadj.rolling(120, min_periods=120).mean()
    z = ((closeadj - sma) / atr.replace(0.0, np.nan)).clip(-50.0, 50.0)
    return (1.0 / (1.0 + np.exp(-z))).replace([np.inf, -np.inf], np.nan)


# === Days underwater in ATR units =========================================

def f19an_f19_atr_normalized_price_days_underwater_atr_120d_base_v131_signal(high, low, closeadj):
    """Frac of last 120d where (closeadj - rolling_max(closeadj,120)) / ATR(30) < -1."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 30.0, adjust=False, min_periods=30).mean()
    peak = closeadj.rolling(120, min_periods=120).max()
    z = (closeadj - peak) / atr.replace(0.0, np.nan)
    flag = (z < -1.0).astype(float).where(~z.isna())
    return flag.rolling(120, min_periods=120).mean().replace([np.inf, -np.inf], np.nan)


# === ATR-band squeeze =====================================================

def f19an_f19_atr_normalized_price_atr_squeeze_60d_base_v132_signal(high, low, closeadj):
    """ATR(14) / rolling_max(ATR(14), 60). 0..1: 1 at recent vol-peak, low at vol-squeeze."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    mx = atr.rolling(60, min_periods=60).max().replace(0.0, np.nan)
    return (atr / mx).replace([np.inf, -np.inf], np.nan)


# === ATR-band tightness ratio =============================================

def f19an_f19_atr_normalized_price_keltner_BB_tightness_base_v133_signal(high, low, closeadj):
    """ATR(20) / std(closeadj, 20). Keltner-vs-Bollinger width tightness."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 20.0, adjust=False, min_periods=20).mean()
    sd = closeadj.rolling(20, min_periods=20).std()
    return (atr / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Sign of close vs SMA over multi-windows in ATR ======================

def f19an_f19_atr_normalized_price_ma_consensus_atr_band_base_v134_signal(high, low, closeadj):
    """Count of MAs (SMA10, SMA20, SMA40, SMA80) where closeadj > MA + 0.25*ATR(20). 0..4 consensus."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 20.0, adjust=False, min_periods=20).mean()
    m10 = closeadj.rolling(10, min_periods=10).mean()
    m20 = closeadj.rolling(20, min_periods=20).mean()
    m40 = closeadj.rolling(40, min_periods=40).mean()
    m80 = closeadj.rolling(80, min_periods=80).mean()
    band = 0.25 * atr
    flags = [(closeadj > m10 + band).astype(float),
             (closeadj > m20 + band).astype(float),
             (closeadj > m40 + band).astype(float),
             (closeadj > m80 + band).astype(float)]
    mask = ~m80.isna() & ~atr.isna()
    return (sum(flags)).where(mask).replace([np.inf, -np.inf], np.nan)


# === Long ATR-units position-in-range ====================================

def f19an_f19_atr_normalized_price_close_pos_252d_atr_base_v135_signal(high, low, closeadj):
    """(closeadj - 0.5*(rolling_max(high,252) + rolling_min(low,252))) / ATR(60). Long-range position."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 60.0, adjust=False, min_periods=60).mean()
    hh = high.rolling(252, min_periods=252).max()
    ll = low.rolling(252, min_periods=252).min()
    return ((closeadj - 0.5 * (hh + ll)) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Mean of (high-close)/ATR-style "pressure" ===========================

def f19an_f19_atr_normalized_price_avg_close_to_high_atr_30d_base_v136_signal(high, low, close):
    """mean over 30d of (high - close) / ATR(14). Average upper-pressure in ATR units."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    z = (high - close) / atr.replace(0.0, np.nan)
    return z.rolling(30, min_periods=30).mean().replace([np.inf, -np.inf], np.nan)


def f19an_f19_atr_normalized_price_avg_close_to_low_atr_30d_base_v137_signal(high, low, close):
    """mean over 30d of (close - low) / ATR(14). Average lower-bounce in ATR units."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    z = (close - low) / atr.replace(0.0, np.nan)
    return z.rolling(30, min_periods=30).mean().replace([np.inf, -np.inf], np.nan)


# === ATR-units median-displacement ========================================

def f19an_f19_atr_normalized_price_median_signed_ret_atr_60d_base_v138_signal(high, low, closeadj):
    """Median over 60d of (closeadj - pc) / ATR(14). Robust ATR-units drift."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    z = (closeadj - pc) / atr.replace(0.0, np.nan)
    return z.rolling(60, min_periods=60).median().replace([np.inf, -np.inf], np.nan)


# === ATR-units mean reversion strength ===================================

def f19an_f19_atr_normalized_price_revstrength_atr_15d_base_v139_signal(high, low, close):
    """corr over 15d between (close - SMA(15))/ATR(14) and -(next_day_logret).
    But cannot look ahead; instead use lag-1 same-period corr as proxy.
    Specifically corr(z_t, -ret_{t+1}) ~ corr(z_t, -ret_t.shift(-1)). Use lag-1 negative-cor."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    sma = close.rolling(15, min_periods=15).mean()
    z = (close - sma) / atr.replace(0.0, np.nan)
    r = np.log(close / pc)
    return z.rolling(15, min_periods=15).corr(-r).replace([np.inf, -np.inf], np.nan)


# === ATR-units 20d move sign-of-trend conditional =========================

def f19an_f19_atr_normalized_price_trend_conf_atr_45d_base_v140_signal(high, low, closeadj):
    """sign(EMA(20)-EMA(50)) * (closeadj - closeadj.shift(20))/ATR(20). Trend-conditional ATR move."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 20.0, adjust=False, min_periods=20).mean()
    e20 = closeadj.ewm(span=20, adjust=False, min_periods=20).mean()
    e50 = closeadj.ewm(span=50, adjust=False, min_periods=50).mean()
    direction = np.sign(e20 - e50)
    move = (closeadj - closeadj.shift(20)) / atr.replace(0.0, np.nan)
    return (direction * move).replace([np.inf, -np.inf], np.nan)


# === ATR-units rolling regression slope ===================================

def f19an_f19_atr_normalized_price_regslope_atr_30d_base_v141_signal(high, low, closeadj):
    """OLS slope of closeadj vs t over 30d, scaled by ATR(20). Trend in ATR-units-per-bar."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 20.0, adjust=False, min_periods=20).mean()
    t = pd.Series(np.arange(len(closeadj), dtype=float), index=closeadj.index)
    def _slope(y):
        x = np.arange(len(y), dtype=float)
        if not np.all(np.isfinite(y)):
            return np.nan
        xm = x.mean(); ym = y.mean()
        den = float(((x - xm) ** 2).sum())
        if den == 0.0:
            return np.nan
        return float(((x - xm) * (y - ym)).sum() / den)
    slope = closeadj.rolling(30, min_periods=30).apply(_slope, raw=True)
    return (slope / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === ATR-trail offset: chand-lower minus chand-upper =====================

def f19an_f19_atr_normalized_price_chand_spread_15d_base_v142_signal(high, low, close):
    """(rolling_min(low,15) + 3*ATR(15)) - (rolling_max(high,15) - 3*ATR(15)) all / ATR(15)."""
    pc = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 15.0, adjust=False, min_periods=15).mean()
    upper_long = high.rolling(15, min_periods=15).max() - 3.0 * atr
    upper_short = low.rolling(15, min_periods=15).min() + 3.0 * atr
    return ((upper_short - upper_long) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === ATR-units count rolling above quantile ===============================

def f19an_f19_atr_normalized_price_pct_above_q70_atr_z_base_v143_signal(high, low, closeadj):
    """Fraction of last 60d where (closeadj - SMA(20))/ATR(20) > 70th-percentile of itself over 252d."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 20.0, adjust=False, min_periods=20).mean()
    sma = closeadj.rolling(20, min_periods=20).mean()
    z = (closeadj - sma) / atr.replace(0.0, np.nan)
    q70 = z.rolling(252, min_periods=252).quantile(0.7)
    flag = (z > q70).astype(float).where(~z.isna() & ~q70.isna())
    return flag.rolling(60, min_periods=60).mean().replace([np.inf, -np.inf], np.nan)


# === Range expansion: TR / TR.shift(N) ====================================

def f19an_f19_atr_normalized_price_tr_expansion_atr_30d_base_v144_signal(high, low, closeadj):
    """(TR - TR.shift(5)) / ATR(20). Day-over-day range expansion in ATR units."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 20.0, adjust=False, min_periods=20).mean()
    return ((tr - tr.shift(5)) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Frac time in extreme ATR-z ===========================================

def f19an_f19_atr_normalized_price_frac_extreme_atr_z_120d_base_v145_signal(high, low, closeadj):
    """Frac of last 120d where |(closeadj - SMA(30)) / ATR(30)| > 2."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 30.0, adjust=False, min_periods=30).mean()
    sma = closeadj.rolling(30, min_periods=30).mean()
    z = ((closeadj - sma) / atr.replace(0.0, np.nan)).abs()
    flag = (z > 2.0).astype(float).where(~z.isna())
    return flag.rolling(120, min_periods=120).mean().replace([np.inf, -np.inf], np.nan)


# === ATR-units volume-shock relationship =================================

def f19an_f19_atr_normalized_price_atr_vol_corr_60d_base_v146_signal(high, low, closeadj, volume):
    """corr between ATR(14) and rolling log-volume over 60d. Vol-vol relationship."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    lv = np.log(volume.replace(0.0, np.nan))
    return atr.rolling(60, min_periods=60).corr(lv).replace([np.inf, -np.inf], np.nan)


# === ATR-units regression of close on time relative to ATR ==============

def f19an_f19_atr_normalized_price_regslope_atr_long_120d_base_v147_signal(high, low, closeadj):
    """OLS slope of closeadj vs t over 120d, scaled by ATR(60)."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 60.0, adjust=False, min_periods=60).mean()
    def _slope(y):
        if not np.all(np.isfinite(y)):
            return np.nan
        x = np.arange(len(y), dtype=float)
        xm = x.mean(); ym = y.mean()
        den = float(((x - xm) ** 2).sum())
        if den == 0.0:
            return np.nan
        return float(((x - xm) * (y - ym)).sum() / den)
    slope = closeadj.rolling(120, min_periods=120).apply(_slope, raw=True)
    return (slope / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === ATR-units mean of (high-low)/ATR diff from 1 =========================

def f19an_f19_atr_normalized_price_hl_dist_from_atr_60d_base_v148_signal(high, low, closeadj):
    """mean over 60d of ((high - low) - ATR(14)) / ATR(14). Whether bars are wider/narrower than typical."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    z = ((high - low) - atr) / atr.replace(0.0, np.nan)
    return z.rolling(60, min_periods=60).mean().replace([np.inf, -np.inf], np.nan)


# === ATR vol fingerprint via rolling variance of (ret/ATR) ===============

def f19an_f19_atr_normalized_price_var_retatr_30d_base_v149_signal(high, low, closeadj):
    """Variance of (daily ret/ATR(14)) over 30d. Should be ~1 in stationary regime."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    z = (closeadj - pc) / atr.replace(0.0, np.nan)
    return z.rolling(30, min_periods=30).var().replace([np.inf, -np.inf], np.nan)


# === ATR-units max consecutive same-sign days ===========================

def f19an_f19_atr_normalized_price_max_consec_atr_up_60d_base_v150_signal(high, low, closeadj):
    """Max consecutive bars in last 60d where (closeadj - pc)/ATR(14) > 0.5. Run-length stat."""
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    z = (closeadj - pc) / atr.replace(0.0, np.nan)
    flag = (z > 0.5).astype(float).where(~z.isna())
    def _max_run(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        m = 0; c = 0
        for v in x:
            if v > 0.5:
                c += 1
                if c > m:
                    m = c
            else:
                c = 0
        return float(m)
    return flag.rolling(60, min_periods=60).apply(_max_run, raw=True).replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f19_atr_normalized_price_base_076_150_REGISTRY = {
    "f19an_f19_atr_normalized_price_close_minus_high40_atr_25d_base_v076_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_close_minus_high40_atr_25d_base_v076_signal},
    "f19an_f19_atr_normalized_price_close_minus_low40_atr_25d_base_v077_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_close_minus_low40_atr_25d_base_v077_signal},
    "f19an_f19_atr_normalized_price_chandelier_exit_long_22d_base_v078_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_chandelier_exit_long_22d_base_v078_signal},
    "f19an_f19_atr_normalized_price_chandelier_exit_short_22d_base_v079_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_chandelier_exit_short_22d_base_v079_signal},
    "f19an_f19_atr_normalized_price_supertrend_dist_atr_15d_base_v080_signal": {"inputs": ["high", "low", "close"], "func": f19an_f19_atr_normalized_price_supertrend_dist_atr_15d_base_v080_signal},
    "f19an_f19_atr_normalized_price_donchian_pos_20d_atr_base_v081_signal": {"inputs": ["high", "low", "close"], "func": f19an_f19_atr_normalized_price_donchian_pos_20d_atr_base_v081_signal},
    "f19an_f19_atr_normalized_price_donchian_width_55d_atr_base_v082_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_donchian_width_55d_atr_base_v082_signal},
    "f19an_f19_atr_normalized_price_atr_weighted_ma_dist_30d_base_v083_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_atr_weighted_ma_dist_30d_base_v083_signal},
    "f19an_f19_atr_normalized_price_atr_smooth_diff_25d_base_v084_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_atr_smooth_diff_25d_base_v084_signal},
    "f19an_f19_atr_normalized_price_3bar_move_atr_short_base_v085_signal": {"inputs": ["high", "low", "close"], "func": f19an_f19_atr_normalized_price_3bar_move_atr_short_base_v085_signal},
    "f19an_f19_atr_normalized_price_10bar_move_atr_25d_base_v086_signal": {"inputs": ["high", "low", "close"], "func": f19an_f19_atr_normalized_price_10bar_move_atr_25d_base_v086_signal},
    "f19an_f19_atr_normalized_price_atr_short_minus_long_pct_base_v087_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_atr_short_minus_long_pct_base_v087_signal},
    "f19an_f19_atr_normalized_price_atr_pct_close_long_base_v089_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_atr_pct_close_long_base_v089_signal},
    "f19an_f19_atr_normalized_price_count_15atr_45d_base_v090_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_count_15atr_45d_base_v090_signal},
    "f19an_f19_atr_normalized_price_max_5d_move_atr_252d_base_v091_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_max_5d_move_atr_252d_base_v091_signal},
    "f19an_f19_atr_normalized_price_max_signed_ret_atr_180d_base_v092_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_max_signed_ret_atr_180d_base_v092_signal},
    "f19an_f19_atr_normalized_price_min_signed_ret_atr_180d_base_v093_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_min_signed_ret_atr_180d_base_v093_signal},
    "f19an_f19_atr_normalized_price_avg_body_atr_30d_base_v094_signal": {"inputs": ["high", "low", "closeadj", "open"], "func": f19an_f19_atr_normalized_price_avg_body_atr_30d_base_v094_signal},
    "f19an_f19_atr_normalized_price_avg_range_atr_50d_base_v095_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_avg_range_atr_50d_base_v095_signal},
    "f19an_f19_atr_normalized_price_williamsR_in_atr_band_30d_base_v096_signal": {"inputs": ["high", "low", "close"], "func": f19an_f19_atr_normalized_price_williamsR_in_atr_band_30d_base_v096_signal},
    "f19an_f19_atr_normalized_price_30d_move_vs_60d_atr_base_v097_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_30d_move_vs_60d_atr_base_v097_signal},
    "f19an_f19_atr_normalized_price_upwick_minus_lowwick_atr_15d_base_v098_signal": {"inputs": ["high", "low", "close", "open"], "func": f19an_f19_atr_normalized_price_upwick_minus_lowwick_atr_15d_base_v098_signal},
    "f19an_f19_atr_normalized_price_zscore_close_atr_15d_base_v099_signal": {"inputs": ["high", "low", "close"], "func": f19an_f19_atr_normalized_price_zscore_close_atr_15d_base_v099_signal},
    "f19an_f19_atr_normalized_price_above_05atr_sma8_base_v100_signal": {"inputs": ["high", "low", "close"], "func": f19an_f19_atr_normalized_price_above_05atr_sma8_base_v100_signal},
    "f19an_f19_atr_normalized_price_ema_cross_mag_atr_8_30_base_v101_signal": {"inputs": ["high", "low", "close"], "func": f19an_f19_atr_normalized_price_ema_cross_mag_atr_8_30_base_v101_signal},
    "f19an_f19_atr_normalized_price_ema_cross_mag_atr_20_80_base_v102_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_ema_cross_mag_atr_20_80_base_v102_signal},
    "f19an_f19_atr_normalized_price_atr_slope_5d_norm_base_v103_signal": {"inputs": ["high", "low", "close"], "func": f19an_f19_atr_normalized_price_atr_slope_5d_norm_base_v103_signal},
    "f19an_f19_atr_normalized_price_atr_slope_90d_norm_base_v104_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_atr_slope_90d_norm_base_v104_signal},
    "f19an_f19_atr_normalized_price_median_tr_atr_45d_base_v105_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_median_tr_atr_45d_base_v105_signal},
    "f19an_f19_atr_normalized_price_atr_close_corr_60d_base_v106_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_atr_close_corr_60d_base_v106_signal},
    "f19an_f19_atr_normalized_price_atr_logret_corr_120d_base_v107_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_atr_logret_corr_120d_base_v107_signal},
    "f19an_f19_atr_normalized_price_short_vs_long_move_atr_60d_base_v108_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_short_vs_long_move_atr_60d_base_v108_signal},
    "f19an_f19_atr_normalized_price_signed_ret_atr_sum_20d_base_v109_signal": {"inputs": ["high", "low", "close"], "func": f19an_f19_atr_normalized_price_signed_ret_atr_sum_20d_base_v109_signal},
    "f19an_f19_atr_normalized_price_signed_ret_atr_sum_80d_base_v110_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_signed_ret_atr_sum_80d_base_v110_signal},
    "f19an_f19_atr_normalized_price_retatr_lag5_autocorr_100d_base_v111_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_retatr_lag5_autocorr_100d_base_v111_signal},
    "f19an_f19_atr_normalized_price_abs_gap_mean_atr_30d_base_v112_signal": {"inputs": ["high", "low", "close", "open"], "func": f19an_f19_atr_normalized_price_abs_gap_mean_atr_30d_base_v112_signal},
    "f19an_f19_atr_normalized_price_gap_std_atr_45d_base_v113_signal": {"inputs": ["high", "low", "close", "open"], "func": f19an_f19_atr_normalized_price_gap_std_atr_45d_base_v113_signal},
    "f19an_f19_atr_normalized_price_atr_skew_60d_base_v114_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_atr_skew_60d_base_v114_signal},
    "f19an_f19_atr_normalized_price_atr_kurt_120d_base_v115_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_atr_kurt_120d_base_v115_signal},
    "f19an_f19_atr_normalized_price_vol_weighted_atr_dispersion_base_v116_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f19an_f19_atr_normalized_price_vol_weighted_atr_dispersion_base_v116_signal},
    "f19an_f19_atr_normalized_price_hma_dist_atr_30d_base_v117_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_hma_dist_atr_30d_base_v117_signal},
    "f19an_f19_atr_normalized_price_atr_state_flips_80d_base_v118_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_atr_state_flips_80d_base_v118_signal},
    "f19an_f19_atr_normalized_price_logret_mean_atr_15d_base_v119_signal": {"inputs": ["high", "low", "close"], "func": f19an_f19_atr_normalized_price_logret_mean_atr_15d_base_v119_signal},
    "f19an_f19_atr_normalized_price_logret_mean_atr_120d_base_v120_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_logret_mean_atr_120d_base_v120_signal},
    "f19an_f19_atr_normalized_price_atr_rmax_rmin_ratio_40d_base_v121_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_atr_rmax_rmin_ratio_40d_base_v121_signal},
    "f19an_f19_atr_normalized_price_skew_atr_sq_ret_120d_base_v122_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_skew_atr_sq_ret_120d_base_v122_signal},
    "f19an_f19_atr_normalized_price_atr_z_iqr_90d_base_v123_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_atr_z_iqr_90d_base_v123_signal},
    "f19an_f19_atr_normalized_price_days_since_high_atr_252d_base_v124_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_days_since_high_atr_252d_base_v124_signal},
    "f19an_f19_atr_normalized_price_atr_move_bucket_base_v125_signal": {"inputs": ["high", "low", "close"], "func": f19an_f19_atr_normalized_price_atr_move_bucket_base_v125_signal},
    "f19an_f19_atr_normalized_price_path_atr_efficiency_30d_base_v126_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_path_atr_efficiency_30d_base_v126_signal},
    "f19an_f19_atr_normalized_price_dist_high5_atr_short_base_v127_signal": {"inputs": ["high", "low", "close"], "func": f19an_f19_atr_normalized_price_dist_high5_atr_short_base_v127_signal},
    "f19an_f19_atr_normalized_price_accel_atr_15d_base_v128_signal": {"inputs": ["high", "low", "close"], "func": f19an_f19_atr_normalized_price_accel_atr_15d_base_v128_signal},
    "f19an_f19_atr_normalized_price_accel_atr_60d_base_v129_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_accel_atr_60d_base_v129_signal},
    "f19an_f19_atr_normalized_price_sigmoid_long_atr_z_base_v130_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_sigmoid_long_atr_z_base_v130_signal},
    "f19an_f19_atr_normalized_price_days_underwater_atr_120d_base_v131_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_days_underwater_atr_120d_base_v131_signal},
    "f19an_f19_atr_normalized_price_atr_squeeze_60d_base_v132_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_atr_squeeze_60d_base_v132_signal},
    "f19an_f19_atr_normalized_price_keltner_BB_tightness_base_v133_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_keltner_BB_tightness_base_v133_signal},
    "f19an_f19_atr_normalized_price_ma_consensus_atr_band_base_v134_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_ma_consensus_atr_band_base_v134_signal},
    "f19an_f19_atr_normalized_price_close_pos_252d_atr_base_v135_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_close_pos_252d_atr_base_v135_signal},
    "f19an_f19_atr_normalized_price_avg_close_to_high_atr_30d_base_v136_signal": {"inputs": ["high", "low", "close"], "func": f19an_f19_atr_normalized_price_avg_close_to_high_atr_30d_base_v136_signal},
    "f19an_f19_atr_normalized_price_avg_close_to_low_atr_30d_base_v137_signal": {"inputs": ["high", "low", "close"], "func": f19an_f19_atr_normalized_price_avg_close_to_low_atr_30d_base_v137_signal},
    "f19an_f19_atr_normalized_price_median_signed_ret_atr_60d_base_v138_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_median_signed_ret_atr_60d_base_v138_signal},
    "f19an_f19_atr_normalized_price_revstrength_atr_15d_base_v139_signal": {"inputs": ["high", "low", "close"], "func": f19an_f19_atr_normalized_price_revstrength_atr_15d_base_v139_signal},
    "f19an_f19_atr_normalized_price_trend_conf_atr_45d_base_v140_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_trend_conf_atr_45d_base_v140_signal},
    "f19an_f19_atr_normalized_price_regslope_atr_30d_base_v141_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_regslope_atr_30d_base_v141_signal},
    "f19an_f19_atr_normalized_price_chand_spread_15d_base_v142_signal": {"inputs": ["high", "low", "close"], "func": f19an_f19_atr_normalized_price_chand_spread_15d_base_v142_signal},
    "f19an_f19_atr_normalized_price_pct_above_q70_atr_z_base_v143_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_pct_above_q70_atr_z_base_v143_signal},
    "f19an_f19_atr_normalized_price_tr_expansion_atr_30d_base_v144_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_tr_expansion_atr_30d_base_v144_signal},
    "f19an_f19_atr_normalized_price_frac_extreme_atr_z_120d_base_v145_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_frac_extreme_atr_z_120d_base_v145_signal},
    "f19an_f19_atr_normalized_price_atr_vol_corr_60d_base_v146_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f19an_f19_atr_normalized_price_atr_vol_corr_60d_base_v146_signal},
    "f19an_f19_atr_normalized_price_regslope_atr_long_120d_base_v147_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_regslope_atr_long_120d_base_v147_signal},
    "f19an_f19_atr_normalized_price_hl_dist_from_atr_60d_base_v148_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_hl_dist_from_atr_60d_base_v148_signal},
    "f19an_f19_atr_normalized_price_var_retatr_30d_base_v149_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_var_retatr_30d_base_v149_signal},
    "f19an_f19_atr_normalized_price_max_consec_atr_up_60d_base_v150_signal": {"inputs": ["high", "low", "closeadj"], "func": f19an_f19_atr_normalized_price_max_consec_atr_up_60d_base_v150_signal},
}


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------


def _synthetic_inputs(n: int = 800, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    seg = n // 4
    rest = n - 3 * seg
    ret = np.concatenate([
        rng.normal(0.0012, 0.011, seg),
        rng.normal(-0.0005, 0.018, seg),
        rng.normal(-0.0010, 0.014, seg),
        rng.normal(0.0008, 0.012, rest),
    ])
    close = 50.0 * np.exp(np.cumsum(ret))
    adj_drift = rng.normal(0.0, 0.0003, size=n).cumsum()
    closeadj = close * np.exp(adj_drift)
    intraday = rng.normal(0.0, 0.008, size=n)
    open_ = close * np.exp(-intraday * 0.5)
    high = np.maximum(close, open_) * np.exp(np.abs(rng.normal(0.0, 0.006, size=n)))
    low = np.minimum(close, open_) * np.exp(-np.abs(rng.normal(0.0, 0.006, size=n)))
    volume = rng.lognormal(mean=13.0, sigma=0.6, size=n)
    idx = pd.RangeIndex(n)
    return pd.DataFrame({
        "open": pd.Series(open_, index=idx, dtype=float),
        "high": pd.Series(high, index=idx, dtype=float),
        "low": pd.Series(low, index=idx, dtype=float),
        "close": pd.Series(close, index=idx, dtype=float),
        "closeadj": pd.Series(closeadj, index=idx, dtype=float),
        "volume": pd.Series(volume, index=idx, dtype=float),
    })


def _self_test() -> None:
    df = _synthetic_inputs(n=800, seed=42)
    results: dict[str, pd.Series] = {}
    for name, entry in f19_atr_normalized_price_base_076_150_REGISTRY.items():
        args = [df[col] for col in entry["inputs"]]
        out = entry["func"](*args)
        assert isinstance(out, pd.Series), f"{name}: not a Series"
        assert len(out) == len(df), f"{name}: length mismatch"
        clean = out.dropna()
        assert len(clean) > 0, f"{name}: all NaN"
        assert float(clean.std()) > 0.0 or clean.nunique() > 1, f"{name}: constant/all-zero"
        results[name] = out

    warm = 252
    coverage_ok = sum(1 for s in results.values() if s.iloc[warm:].isna().mean() < 0.5)
    frac = coverage_ok / len(results)
    assert frac >= 0.80, f"NaN-coverage too low: {frac:.2%} have <50% NaN after warm-up"

    aligned = pd.concat({n: results[n] for n in results}, axis=1).iloc[warm:]
    aligned = aligned.replace([np.inf, -np.inf], np.nan)
    corr = aligned.corr(min_periods=50).abs()
    np.fill_diagonal(corr.values, 0.0)
    max_corr = float(corr.max().max())
    if max_corr > 0.95:
        print(f"FAILING max |corr| = {max_corr:.4f}. Top pairs:")
        for i, a in enumerate(corr.columns):
            for j, b in enumerate(corr.columns):
                if j > i and corr.iloc[i, j] > 0.94:
                    print(f"  {a}  vs  {b}  ->  {corr.iloc[i, j]:.4f}")
    assert max_corr <= 0.95 + 1e-9, f"max pairwise |corr|={max_corr:.4f} exceeds 0.95"
    print(f"OK base_076_150: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
