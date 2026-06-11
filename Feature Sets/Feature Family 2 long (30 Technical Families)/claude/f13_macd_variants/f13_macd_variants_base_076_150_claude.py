"""f13_macd_variants base features 076-150.

Second batch of MACD-construct features. Every feature references an MACD-like
construct (fast MA minus slow MA used as a momentum oscillator). Heavy structural
diversity: signs/streaks/ranks/z-scores/percentile-ranks/days-since/discrete-states
of MACD on alternative price/volume inputs, MACD-vs-ATR, OBV-MACD, PPO, AO,
high/low-based MACDs, returns MACDs, etc.

Each function is a fully-expanded def block, formula inline. Window > 21d uses
closeadj. NaN policy: never fillna(<value>); only replace([inf,-inf], nan) at the
function's final return.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False, min_periods=n).mean()


def _wilder(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()


def _tr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    pc = close.shift(1)
    return pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)


def _atr(high: pd.Series, low: pd.Series, close: pd.Series, n: int) -> pd.Series:
    return _wilder(_tr(high, low, close), n)


# ---------------------------------------------------------------------------
# Features 076-150
# ---------------------------------------------------------------------------


# --- MACD on alternative price series (typical, hlc3, OHLC avg, log) -----


def f13mc_f13_macd_variants_macd_hl2_12_26_base_v076_signal(high, low):
    """MACD(12,26) on HL2 mid-price — bar-midpoint MACD."""
    hl2 = (high + low) / 2.0
    return (_ema(hl2, 12) - _ema(hl2, 26)).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_macd_hlc3_19_39_base_v077_signal(high, low, closeadj):
    """MACD(19,39) on HLC3 — slow-MACD on typical price (closeadj)."""
    hlc3 = (high + low + closeadj) / 3.0
    return (_ema(hlc3, 19) - _ema(hlc3, 39)).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_macd_ohlc4_minus_close_base_v078_signal(open, high, low, close):
    """MACD(12,26) on OHLC4 MINUS MACD(12,26) on close — OHLC-shape vs close kernel diff."""
    ohlc4 = (open + high + low + close) / 4.0
    a = _ema(ohlc4, 12) - _ema(ohlc4, 26)
    b = _ema(close, 12) - _ema(close, 26)
    return (a - b).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_macd_high_minus_close_12_26_base_v079_signal(high, close):
    """MACD(12,26) on highs MINUS MACD(12,26) on close — top-vs-close MACD differential."""
    a = _ema(high, 12) - _ema(high, 26)
    b = _ema(close, 12) - _ema(close, 26)
    return (a - b).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_macdLow_streak_19_39_base_v080_signal(low):
    """Bipolar streak above/below zero of slow MACD(19,39) on lows. Cap +/-80."""
    m = _ema(low, 19) - _ema(low, 39)
    above = (m > 0.0).astype(float).where(~m.isna())
    grp = (above != above.shift(1)).cumsum()
    run = above.groupby(grp).cumcount() + 1.0
    out = np.where(above > 0.5, run, -run)
    s = pd.Series(out, index=low.index, dtype=float).clip(-80.0, 80.0)
    return s.where(~above.isna()).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_macd_highlow_diff_19_39_base_v081_signal(high, low):
    """MACD(19,39) on highs MINUS MACD(19,39) on lows — H-L MACD spread."""
    mh = _ema(high, 19) - _ema(high, 39)
    ml = _ema(low, 19) - _ema(low, 39)
    return (mh - ml).replace([np.inf, -np.inf], np.nan)


# --- PPO (Percentage Price Oscillator) — MACD/EMA_slow * 100 -------------


def f13mc_f13_macd_variants_ppo_quantile_12_26_252d_base_v082_signal(closeadj):
    """Pct quantile of PPO(12,26) over 252d — long-horizon PPO bounded percentile."""
    e12 = _ema(closeadj, 12)
    e26 = _ema(closeadj, 26)
    ppo = (e12 - e26) / e26.replace(0.0, np.nan) * 100.0
    return ppo.rolling(252, min_periods=120).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_ppo_xover_count_60d_base_v083_signal(closeadj):
    """Count of PPO(12,26) zero-line crosses in trailing 60d — PPO oscillation count."""
    e12 = _ema(closeadj, 12)
    e26 = _ema(closeadj, 26)
    ppo = (e12 - e26) / e26.replace(0.0, np.nan) * 100.0
    s = np.sign(ppo)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(60, min_periods=60).sum().replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_ppo_50_200_z_base_v084_signal(closeadj):
    """Z-score of long-term PPO(50,200) on 60d — bounded long PPO regime indicator."""
    e1 = _ema(closeadj, 50)
    e2 = _ema(closeadj, 200)
    ppo = (e1 - e2) / e2.replace(0.0, np.nan) * 100.0
    mu = ppo.rolling(60, min_periods=30).mean()
    sd = ppo.rolling(60, min_periods=30).std()
    return ((ppo - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- MACD on returns ---------------------------------------------------


def f13mc_f13_macd_variants_macd_logret_12_26_base_v085_signal(close):
    """MACD(12,26) on log returns: EMA(logret,12)-EMA(logret,26). Momentum of returns."""
    lr = np.log(close / close.shift(1).replace(0.0, np.nan))
    return (_ema(lr, 12) - _ema(lr, 26)).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_macd_absret_12_26_base_v086_signal(close):
    """MACD on absolute returns: vol-momentum oscillator."""
    ar = (np.log(close / close.shift(1).replace(0.0, np.nan))).abs()
    return (_ema(ar, 12) - _ema(ar, 26)).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_macd_squaredret_19_39_base_v087_signal(closeadj):
    """MACD(19,39) on squared log returns — slower vol-momentum oscillator."""
    sr = (np.log(closeadj / closeadj.shift(1).replace(0.0, np.nan))) ** 2.0
    return (_ema(sr, 19) - _ema(sr, 39)).replace([np.inf, -np.inf], np.nan)


# --- MACD on OBV / volume-flow series ------------------------------------


def f13mc_f13_macd_variants_obv_macd_12_26_base_v088_signal(close, volume):
    """MACD(12,26) on On-Balance Volume — OBV-MACD detects volume-momentum shifts."""
    obv = (np.sign(close.diff()) * volume).cumsum(skipna=True)
    return (_ema(obv, 12) - _ema(obv, 26)).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_obv_macd_hist_19_39_9_base_v089_signal(close, volume):
    """OBV-MACD(19,39) histogram with signal(9)."""
    obv = (np.sign(close.diff()) * volume).cumsum(skipna=True)
    m = _ema(obv, 19) - _ema(obv, 39)
    sig = _ema(m, 9)
    return (m - sig).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_pvt_macd_12_26_base_v090_signal(close, volume):
    """MACD on Price-Volume Trend: PVT = cumsum(volume * pct_change(close))."""
    pct = close.pct_change()
    pvt = (volume * pct).cumsum(skipna=True)
    return (_ema(pvt, 12) - _ema(pvt, 26)).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_volMACD_sign_12_26_base_v091_signal(volume):
    """sign of EMA(volume,12) - EMA(volume,26) — discrete volume-MACD state."""
    m = _ema(volume, 12) - _ema(volume, 26)
    return np.sign(m).where(~m.isna()).replace([np.inf, -np.inf], np.nan)


# --- MACD over ATR (vol-normalized) -------------------------------------


def f13mc_f13_macd_variants_macd_over_atr_sign_12_26_14_base_v092_signal(high, low, close):
    """sign(MACD(12,26)) AND |MACD|>ATR(14) — extreme-vol-normalized regime in {-1,0,1}."""
    m = _ema(close, 12) - _ema(close, 26)
    atr = _atr(high, low, close, 14)
    strong = (m.abs() > atr).astype(float).where(~atr.isna() & ~m.isna())
    return (np.sign(m) * strong).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_macd_over_atr_streak_50_200_50_base_v093_signal(high, low, closeadj):
    """Bipolar streak above/below zero of slow MACD/ATR(50). Cap +/-100. Persistence of vol-norm MACD."""
    m = _ema(closeadj, 50) - _ema(closeadj, 200)
    atr = _atr(high, low, closeadj, 50)
    r = m / atr.replace(0.0, np.nan)
    above = (r > 0.0).astype(float).where(~r.isna())
    grp = (above != above.shift(1)).cumsum()
    run = above.groupby(grp).cumcount() + 1.0
    out = np.where(above > 0.5, run, -run)
    s = pd.Series(out, index=closeadj.index, dtype=float).clip(-100.0, 100.0)
    return s.where(~above.isna()).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_hist_over_atr_sign_12_26_9_14_base_v094_signal(high, low, close):
    """sign(hist) AND |hist|>0.5*ATR(14) — discrete strong-histogram regime in {-1,0,1}."""
    m = _ema(close, 12) - _ema(close, 26)
    h = m - _ema(m, 9)
    atr = _atr(high, low, close, 14)
    strong = (h.abs() > 0.5 * atr).astype(float).where(~atr.isna() & ~h.isna())
    return (np.sign(h) * strong).replace([np.inf, -np.inf], np.nan)


# --- Discrete-state / sign features on alternative MACDs ---------------


def f13mc_f13_macd_variants_sign_macd_logret_12_26_base_v095_signal(close):
    """sign of MACD on log returns — discrete return-momentum regime."""
    lr = np.log(close / close.shift(1).replace(0.0, np.nan))
    m = _ema(lr, 12) - _ema(lr, 26)
    return np.sign(m).where(~m.isna()).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_sign_macd_obv_12_26_base_v096_signal(close, volume):
    """sign of OBV-MACD(12,26) — discrete volume-momentum direction."""
    obv = (np.sign(close.diff()) * volume).cumsum(skipna=True)
    m = _ema(obv, 12) - _ema(obv, 26)
    return np.sign(m).where(~m.isna()).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_dayssince_obv_x_12_26_base_v097_signal(close, volume):
    """Days since OBV-MACD(12,26) zero-cross, capped 80."""
    obv = (np.sign(close.diff()) * volume).cumsum(skipna=True)
    m = _ema(obv, 12) - _ema(obv, 26)
    s = np.sign(m)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return 80.0
        return float(len(x) - 1 - idx[-1])
    return flip.rolling(80, min_periods=20).apply(_ds, raw=True).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_streak_logretmacd_12_26_base_v098_signal(close):
    """Bipolar streak above/below zero of log-ret MACD(12,26), cap +/-50."""
    lr = np.log(close / close.shift(1).replace(0.0, np.nan))
    m = _ema(lr, 12) - _ema(lr, 26)
    above = (m > 0.0).astype(float).where(~m.isna())
    grp = (above != above.shift(1)).cumsum()
    run = above.groupby(grp).cumcount() + 1.0
    out = np.where(above > 0.5, run, -run)
    s = pd.Series(out, index=close.index, dtype=float).clip(-50.0, 50.0)
    return s.where(~above.isna()).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_macd_obv_pos_state_base_v099_signal(close, volume):
    """sign(OBV-MACD) AND sign(price-MACD) — joint indicator in {-2,0,2}."""
    obv = (np.sign(close.diff()) * volume).cumsum(skipna=True)
    mo = _ema(obv, 12) - _ema(obv, 26)
    mp = _ema(close, 12) - _ema(close, 26)
    return (np.sign(mo) + np.sign(mp)).where(~mo.isna() & ~mp.isna()).replace([np.inf, -np.inf], np.nan)


# --- Histogram variants of alt-MACDs ----------------------------------


def f13mc_f13_macd_variants_hist_hl2_z_60d_base_v100_signal(high, low):
    """Z-score of HL2-MACD histogram (12,26,9) over 60d — bounded HL2-histogram signal."""
    hl2 = (high + low) / 2.0
    m = _ema(hl2, 12) - _ema(hl2, 26)
    h = m - _ema(m, 9)
    mu = h.rolling(60, min_periods=30).mean()
    sd = h.rolling(60, min_periods=30).std()
    return ((h - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_hist_logret_8_21_5_base_v101_signal(close):
    """Histogram on log-return MACD(8,21,5)."""
    lr = np.log(close / close.shift(1).replace(0.0, np.nan))
    m = _ema(lr, 8) - _ema(lr, 21)
    sig = _ema(m, 5)
    return (m - sig).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_hist_obv_12_26_9_base_v102_signal(close, volume):
    """OBV-MACD histogram (12,26,9)."""
    obv = (np.sign(close.diff()) * volume).cumsum(skipna=True)
    m = _ema(obv, 12) - _ema(obv, 26)
    sig = _ema(m, 9)
    return (m - sig).replace([np.inf, -np.inf], np.nan)


# --- Slope/curvature features on alt-MACDs ----------------------------


def f13mc_f13_macd_variants_slope_hl2_macd_12_26_base_v103_signal(high, low):
    """5-bar diff of MACD on HL2 — HL2-MACD velocity."""
    hl2 = (high + low) / 2.0
    m = _ema(hl2, 12) - _ema(hl2, 26)
    return m.diff(5).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_curv_logret_macd_12_26_base_v104_signal(close):
    """Curvature of log-return MACD: m - 2*m.shift(5) + m.shift(10)."""
    lr = np.log(close / close.shift(1).replace(0.0, np.nan))
    m = _ema(lr, 12) - _ema(lr, 26)
    out = m - 2.0 * m.shift(5) + m.shift(10)
    return out.replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_obv_macd_z_19_39_60d_base_v105_signal(close, volume):
    """Z-score of OBV-MACD(19,39) over 60d — bounded OBV-MACD signal."""
    obv = (np.sign(close.diff()) * volume).cumsum(skipna=True)
    m = _ema(obv, 19) - _ema(obv, 39)
    mu = m.rolling(60, min_periods=30).mean()
    sd = m.rolling(60, min_periods=30).std()
    return ((m - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- MACD signal-line at different lengths -----------------------------


def f13mc_f13_macd_variants_signal_rank_12_26_9_60d_base_v106_signal(closeadj):
    """Pct rank of MACD signal (12,26,9) over 60d — bounded signal-line position."""
    m = _ema(closeadj, 12) - _ema(closeadj, 26)
    sig = _ema(m, 9)
    return sig.rolling(60, min_periods=30).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_signalslope_12_26_9_5d_base_v107_signal(closeadj):
    """5-bar diff of MACD signal line (12,26,9) — signal-line velocity."""
    m = _ema(closeadj, 12) - _ema(closeadj, 26)
    sig = _ema(m, 9)
    return sig.diff(5).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_dualsignal_diff_12_26_base_v108_signal(close):
    """Signal(9) - Signal(21): comparison of fast/slow MACD signal lines."""
    m = _ema(close, 12) - _ema(close, 26)
    return (_ema(m, 9) - _ema(m, 21)).replace([np.inf, -np.inf], np.nan)


# --- MACD-band breakout/breakdown signals -------------------------------


def f13mc_f13_macd_variants_macd_lower_band_breaks_60d_base_v109_signal(closeadj):
    """Count in trailing 30 bars of MACD breaks BELOW mu-2sd band (60d)."""
    m = _ema(closeadj, 12) - _ema(closeadj, 26)
    mu = m.rolling(60, min_periods=30).mean()
    sd = m.rolling(60, min_periods=30).std()
    lower = mu - 2.0 * sd
    flag = (m < lower).astype(float).where(~lower.isna() & ~m.isna())
    return flag.rolling(30, min_periods=15).sum().replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_macd_bandwidth_60d_base_v110_signal(closeadj):
    """Bandwidth: (mu+2sd) - (mu-2sd) = 4*sd of MACD over 60d, normalized by |mean(MACD)|+eps."""
    m = _ema(closeadj, 12) - _ema(closeadj, 26)
    sd = m.rolling(60, min_periods=30).std()
    mu = m.rolling(60, min_periods=30).mean()
    return (4.0 * sd / (mu.abs() + 1e-9)).replace([np.inf, -np.inf], np.nan)


# --- Cross-MACD pair / regime alignment --------------------------------


def f13mc_f13_macd_variants_macd_regime_align_base_v111_signal(closeadj):
    """sign(MACD(8,21)) + sign(MACD(19,39)) + sign(MACD(50,200)) — 3-config regime score in {-3..3}."""
    a = np.sign(_ema(closeadj, 8) - _ema(closeadj, 21))
    b = np.sign(_ema(closeadj, 19) - _ema(closeadj, 39))
    c = np.sign(_ema(closeadj, 50) - _ema(closeadj, 200))
    out = a + b + c
    return out.where(~a.isna() & ~b.isna() & ~c.isna()).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_macd_pair_disagree_count_60d_base_v112_signal(closeadj):
    """Count in 60d when sign(MACD(8,21)) != sign(MACD(50,200)) — pair-disagreement count."""
    a = np.sign(_ema(closeadj, 8) - _ema(closeadj, 21))
    b = np.sign(_ema(closeadj, 50) - _ema(closeadj, 200))
    dis = (a * b < 0.0).astype(float).where(~a.isna() & ~b.isna())
    return dis.rolling(60, min_periods=30).sum().replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_macd_x_signal_pair_base_v113_signal(close):
    """sign(MACD(8,21) - signal(8,21,5)) XOR sign(MACD(12,26) - signal(12,26,9)) — pair-config histogram-sign disagreement."""
    m1 = _ema(close, 8) - _ema(close, 21)
    h1 = m1 - _ema(m1, 5)
    m2 = _ema(close, 12) - _ema(close, 26)
    h2 = m2 - _ema(m2, 9)
    out = (np.sign(h1) != np.sign(h2)).astype(float).where(~h1.isna() & ~h2.isna())
    return out.replace([np.inf, -np.inf], np.nan)


# --- AO (Awesome Oscillator) — SMA-based MACD --------------------------


def f13mc_f13_macd_variants_ao_rank_5_34_60d_base_v114_signal(high, low):
    """Pct rank of Awesome Oscillator (SMA(HL2,5)-SMA(HL2,34)) over 60d."""
    hl2 = (high + low) / 2.0
    ao = hl2.rolling(5, min_periods=5).mean() - hl2.rolling(34, min_periods=34).mean()
    return ao.rolling(60, min_periods=30).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_ac_5_34_base_v115_signal(high, low):
    """Accelerator Oscillator = AO - SMA(AO,5). Histogram on top of AO."""
    hl2 = (high + low) / 2.0
    ao = hl2.rolling(5, min_periods=5).mean() - hl2.rolling(34, min_periods=34).mean()
    return (ao - ao.rolling(5, min_periods=5).mean()).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_ao_sign_5_34_base_v116_signal(high, low):
    """sign of Awesome Oscillator — discrete AO regime."""
    hl2 = (high + low) / 2.0
    ao = hl2.rolling(5, min_periods=5).mean() - hl2.rolling(34, min_periods=34).mean()
    return np.sign(ao).where(~ao.isna()).replace([np.inf, -np.inf], np.nan)


# --- KST-style multi-window MACD ---------------------------------------




def f13mc_f13_macd_variants_kst_hist_9_base_v118_signal(closeadj):
    """KST minus EMA(KST,9) — histogram of KST signal."""
    r10 = closeadj.pct_change(10).rolling(10, min_periods=10).mean()
    r15 = closeadj.pct_change(15).rolling(10, min_periods=10).mean()
    r20 = closeadj.pct_change(20).rolling(10, min_periods=10).mean()
    r30 = closeadj.pct_change(30).rolling(15, min_periods=15).mean()
    kst = (1.0 * r10 + 2.0 * r15 + 3.0 * r20 + 4.0 * r30)
    return (kst - _ema(kst, 9)).replace([np.inf, -np.inf], np.nan)


# --- MACD-vs-ATR-derived MACD signals ----------------------------------


def f13mc_f13_macd_variants_atrMACD_14_50_base_v119_signal(high, low, close):
    """MACD on ATR series: EMA(ATR14,14) - EMA(ATR14,50) — vol-momentum oscillator."""
    atr = _atr(high, low, close, 14)
    return (_ema(atr, 14) - _ema(atr, 50)).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_atrMACD_sign_14_50_base_v120_signal(high, low, closeadj):
    """sign of ATR-MACD(14,50) — discrete vol-regime."""
    atr = _atr(high, low, closeadj, 14)
    m = _ema(atr, 14) - _ema(atr, 50)
    return np.sign(m).where(~m.isna()).replace([np.inf, -np.inf], np.nan)


# --- MACD rank/z at very-long windows ----------------------------------


def f13mc_f13_macd_variants_macdrank_19_39_252d_base_v121_signal(closeadj):
    """Pct rank of MACD(19,39) over 252 trailing bars."""
    m = _ema(closeadj, 19) - _ema(closeadj, 39)
    return m.rolling(252, min_periods=120).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_macdz_50_200_120d_base_v122_signal(closeadj):
    """Z-score of slow MACD(50,200) over 120 trailing bars."""
    m = _ema(closeadj, 50) - _ema(closeadj, 200)
    mu = m.rolling(120, min_periods=60).mean()
    sd = m.rolling(120, min_periods=60).std()
    return ((m - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- MACD x volume interaction features --------------------------------


def f13mc_f13_macd_variants_macd_volconfirm_20d_base_v123_signal(close, volume):
    """Fraction of last 20 bars where sign(MACD)==sign(volume - SMA(volume,20))."""
    m = _ema(close, 12) - _ema(close, 26)
    vol_dev = volume - volume.rolling(20, min_periods=20).mean()
    agree = (np.sign(m) * np.sign(vol_dev) > 0.0).astype(float).where(~m.isna() & ~vol_dev.isna())
    return agree.rolling(20, min_periods=20).mean().replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_macd_volMACD_interact_base_v124_signal(close, volume):
    """sign(MACD(close)) * sign(MACD(log volume)) — joint interaction sign."""
    mp = _ema(close, 12) - _ema(close, 26)
    lv = np.log(volume.replace(0.0, np.nan))
    mv = _ema(lv, 12) - _ema(lv, 26)
    return (np.sign(mp) * np.sign(mv)).where(~mp.isna() & ~mv.isna()).replace([np.inf, -np.inf], np.nan)


# --- Histogram autocorrelation / momentum-of-momentum ------------------


def f13mc_f13_macd_variants_hist_autocorr1_60d_base_v125_signal(closeadj):
    """Rolling lag-1 autocorrelation of MACD histogram over 60 bars."""
    m = _ema(closeadj, 12) - _ema(closeadj, 26)
    h = m - _ema(m, 9)
    return h.rolling(60, min_periods=30).apply(
        lambda x: float(pd.Series(x).autocorr(lag=1)) if pd.Series(x).std() > 0 else np.nan,
        raw=False,
    ).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_macd_autocorr1_60d_base_v126_signal(closeadj):
    """Rolling lag-1 autocorrelation of MACD line over 60 bars — persistence of MACD."""
    m = _ema(closeadj, 12) - _ema(closeadj, 26)
    return m.rolling(60, min_periods=30).apply(
        lambda x: float(pd.Series(x).autocorr(lag=1)) if pd.Series(x).std() > 0 else np.nan,
        raw=False,
    ).replace([np.inf, -np.inf], np.nan)


# --- MACD-MA-cross-confirmation ----------------------------------------


def f13mc_f13_macd_variants_macd_above_close_state_50_200_base_v127_signal(closeadj):
    """sign(MACD(50,200)) * sign(close - EMA200) — joint MACD-sign-with-trend state."""
    m = _ema(closeadj, 50) - _ema(closeadj, 200)
    e200 = _ema(closeadj, 200)
    return (np.sign(m) * np.sign(closeadj - e200)).where(~m.isna() & ~e200.isna()).replace([np.inf, -np.inf], np.nan)


# --- Histogram sign-flip event signal at various windows ---------------


def f13mc_f13_macd_variants_histflip_50_200_30_event_60d_base_v128_signal(closeadj):
    """Count of histogram sign flips in trailing 60 bars for slow histogram (50,200,30)."""
    m = _ema(closeadj, 50) - _ema(closeadj, 200)
    h = m - _ema(m, 30)
    s = np.sign(h)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(60, min_periods=60).sum().replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_histflip_19_39_13_event_30d_base_v129_signal(closeadj):
    """Count of histogram sign flips in trailing 30 bars for slow histogram (19,39,13)."""
    m = _ema(closeadj, 19) - _ema(closeadj, 39)
    h = m - _ema(m, 13)
    s = np.sign(h)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(30, min_periods=30).sum().replace([np.inf, -np.inf], np.nan)


# --- MACD vs Bollinger %B-style on price -------------------------------


def f13mc_f13_macd_variants_macd_x_pricez_12_26_60d_base_v130_signal(closeadj):
    """sign(MACD(12,26)) * sign(z(close,60d)) — MACD aligned with z-position of price."""
    m = _ema(closeadj, 12) - _ema(closeadj, 26)
    zp = (closeadj - closeadj.rolling(60, min_periods=30).mean()) / closeadj.rolling(60, min_periods=30).std().replace(0.0, np.nan)
    return (np.sign(m) * np.sign(zp)).where(~m.isna() & ~zp.isna()).replace([np.inf, -np.inf], np.nan)


# --- MACD on smoothed-price (median-filtered) --------------------------


def f13mc_f13_macd_variants_macd_medsmoothed_minus_classic_base_v131_signal(close):
    """MACD on rolling-median(close,5) MINUS classic MACD — robust-vs-raw kernel diff."""
    med5 = close.rolling(5, min_periods=5).median()
    a = _ema(med5, 12) - _ema(med5, 26)
    b = _ema(close, 12) - _ema(close, 26)
    return (a - b).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_macd_minmaxmid_minus_classic_base_v132_signal(high, low, closeadj):
    """MACD(12,26) on channel-midpoint MINUS classic MACD on closeadj — channel-vs-close kernel diff."""
    mid = (low.rolling(5, min_periods=5).min() + high.rolling(5, min_periods=5).max()) / 2.0
    a = _ema(mid, 12) - _ema(mid, 26)
    b = _ema(closeadj, 12) - _ema(closeadj, 26)
    return (a - b).replace([np.inf, -np.inf], np.nan)


# --- Histogram statistical properties on long windows -----------------




def f13mc_f13_macd_variants_histmaxabs_12_26_9_60d_base_v134_signal(closeadj):
    """Max absolute histogram value in trailing 60 bars."""
    m = _ema(closeadj, 12) - _ema(closeadj, 26)
    h = (m - _ema(m, 9)).abs()
    return h.rolling(60, min_periods=30).max().replace([np.inf, -np.inf], np.nan)


# --- MACD long EMA pair: (12, 50), (8, 50), etc ------------------------


def f13mc_f13_macd_variants_macdrank_12_50_120d_base_v135_signal(closeadj):
    """Pct rank of MACD(12,50) over 120 bars."""
    m = _ema(closeadj, 12) - _ema(closeadj, 50)
    return m.rolling(120, min_periods=60).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_macd_sign_8_50_base_v136_signal(closeadj):
    """sign of MACD(8,50) — short-vs-medium discrete regime."""
    m = _ema(closeadj, 8) - _ema(closeadj, 50)
    return np.sign(m).where(~m.isna()).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_macdz_26_100_60d_base_v137_signal(closeadj):
    """Z-score of MACD(26,100) over 60d."""
    m = _ema(closeadj, 26) - _ema(closeadj, 100)
    mu = m.rolling(60, min_periods=30).mean()
    sd = m.rolling(60, min_periods=30).std()
    return ((m - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- MACD percentile bucket / quantized signals -----------------------


def f13mc_f13_macd_variants_macdpctbucket_12_26_60d_base_v138_signal(closeadj):
    """Floor(MACD rank * 5) — 0..4 bucket of MACD percentile over 60d (quintile of MACD)."""
    m = _ema(closeadj, 12) - _ema(closeadj, 26)
    r = m.rolling(60, min_periods=30).rank(pct=True)
    return (r * 5.0).apply(np.floor).clip(0.0, 4.0).where(~r.isna()).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_macd_pos_streak_run_50_200_base_v139_signal(closeadj):
    """Length of current MACD(50,200)-above-zero run (positive only, 0 if below). Cap 250."""
    m = _ema(closeadj, 50) - _ema(closeadj, 200)
    above = (m > 0.0).astype(float).where(~m.isna())
    grp = (above != above.shift(1)).cumsum()
    run = above.groupby(grp).cumcount() + 1.0
    out = np.where(above > 0.5, run, 0.0)
    s = pd.Series(out, index=closeadj.index, dtype=float).clip(0.0, 250.0)
    return s.where(~above.isna()).replace([np.inf, -np.inf], np.nan)


# --- Days since extreme MACD events -----------------------------------


def f13mc_f13_macd_variants_dayssince_macd_max_60d_base_v140_signal(closeadj):
    """Days since MACD(12,26) hit its rolling-60d max."""
    m = _ema(closeadj, 12) - _ema(closeadj, 26)
    def _ds(x):
        idx = int(np.argmax(x))
        return float(len(x) - 1 - idx)
    return m.rolling(60, min_periods=60).apply(_ds, raw=True).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_dayssince_hist_min_30d_base_v141_signal(closeadj):
    """Days since MACD histogram hit its 30d min."""
    m = _ema(closeadj, 12) - _ema(closeadj, 26)
    h = m - _ema(m, 9)
    def _ds(x):
        idx = int(np.argmin(x))
        return float(len(x) - 1 - idx)
    return h.rolling(30, min_periods=30).apply(_ds, raw=True).replace([np.inf, -np.inf], np.nan)


# --- MACD vs cross-pair-MACD differential states ----------------------


def f13mc_f13_macd_variants_diff_macd_pair_rank_60d_base_v142_signal(closeadj):
    """Pct rank of (MACD(8,21) - MACD(12,26)) over 60d — bounded rank-form pair-diff."""
    m1 = _ema(closeadj, 8) - _ema(closeadj, 21)
    m2 = _ema(closeadj, 12) - _ema(closeadj, 26)
    d = m1 - m2
    return d.rolling(60, min_periods=30).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# --- Histogram acceleration / deceleration zones ----------------------


def f13mc_f13_macd_variants_histaccelfrac_12_26_9_30d_base_v143_signal(closeadj):
    """Fraction of last 30 bars where hist and diff(hist,3) have same sign (accelerating histogram)."""
    m = _ema(closeadj, 12) - _ema(closeadj, 26)
    h = m - _ema(m, 9)
    accel = (np.sign(h) * np.sign(h.diff(3)) > 0.0).astype(float).where(~h.isna() & ~h.shift(3).isna())
    return accel.rolling(30, min_periods=30).mean().replace([np.inf, -np.inf], np.nan)


# --- Histogram crosses signal-of-histogram ------------------------------


def f13mc_f13_macd_variants_hist_vs_emahist_sign_12_26_9_5_base_v144_signal(close):
    """sign(hist - EMA(hist,5)) — second-derivative-like discrete signal."""
    m = _ema(close, 12) - _ema(close, 26)
    h = m - _ema(m, 9)
    return np.sign(h - _ema(h, 5)).where(~h.isna()).replace([np.inf, -np.inf], np.nan)


def f13mc_f13_macd_variants_hist_minus_emahist_12_26_9_5_base_v145_signal(close):
    """hist - EMA(hist,5) — continuous histogram-second-momentum."""
    m = _ema(close, 12) - _ema(close, 26)
    h = m - _ema(m, 9)
    return (h - _ema(h, 5)).replace([np.inf, -np.inf], np.nan)


# --- MACD bullish/bearish strength rank --------------------------------


def f13mc_f13_macd_variants_macdrelative_rank_30d_base_v146_signal(closeadj):
    """Rolling pct rank of MACD/EMA26 over 30d — normalized MACD position."""
    e1 = _ema(closeadj, 12)
    e2 = _ema(closeadj, 26)
    r = (e1 - e2) / e2.replace(0.0, np.nan)
    return r.rolling(30, min_periods=15).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# --- MACD on high vs MACD on low - asymmetry signal --------------------


def f13mc_f13_macd_variants_macdHmacdL_sign_12_26_base_v147_signal(high, low):
    """sign(MACD on high) - sign(MACD on low) — H-L MACD asymmetry in {-2,0,2}."""
    mh = _ema(high, 12) - _ema(high, 26)
    ml = _ema(low, 12) - _ema(low, 26)
    return (np.sign(mh) - np.sign(ml)).where(~mh.isna() & ~ml.isna()).replace([np.inf, -np.inf], np.nan)


# --- MACD signal-line crossover-event counter --------------------------


def f13mc_f13_macd_variants_macd_x_signal_pair2_60d_base_v148_signal(closeadj):
    """Count of MACD/signal crosses in 60d for slow MACD(19,39,13)."""
    m = _ema(closeadj, 19) - _ema(closeadj, 39)
    sig = _ema(m, 13)
    s = np.sign(m - sig)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(60, min_periods=60).sum().replace([np.inf, -np.inf], np.nan)


# --- Tanh of slow MACD bias ---------------------------------------------


def f13mc_f13_macd_variants_tanh_macdbias_50_200_60d_base_v149_signal(closeadj):
    """tanh of slow MACD(50,200) / its 60d rolling std — bounded slow MACD bias."""
    m = _ema(closeadj, 50) - _ema(closeadj, 200)
    sd = m.rolling(60, min_periods=30).std()
    return np.tanh(m / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- MACD slope rank ----------------------------------------------------


def f13mc_f13_macd_variants_macdslope_rank_12_26_60d_base_v150_signal(closeadj):
    """Pct rank of MACD-line 5-bar diff over trailing 60 bars (MACD slope rank)."""
    m = _ema(closeadj, 12) - _ema(closeadj, 26)
    sl = m.diff(5)
    return sl.rolling(60, min_periods=30).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f13_macd_variants_base_076_150_REGISTRY = {
    "f13mc_f13_macd_variants_macd_hl2_12_26_base_v076_signal": {"inputs": ["high", "low"], "func": f13mc_f13_macd_variants_macd_hl2_12_26_base_v076_signal},
    "f13mc_f13_macd_variants_macd_hlc3_19_39_base_v077_signal": {"inputs": ["high", "low", "closeadj"], "func": f13mc_f13_macd_variants_macd_hlc3_19_39_base_v077_signal},
    "f13mc_f13_macd_variants_macd_ohlc4_minus_close_base_v078_signal": {"inputs": ["open", "high", "low", "close"], "func": f13mc_f13_macd_variants_macd_ohlc4_minus_close_base_v078_signal},
    "f13mc_f13_macd_variants_macd_high_minus_close_12_26_base_v079_signal": {"inputs": ["high", "close"], "func": f13mc_f13_macd_variants_macd_high_minus_close_12_26_base_v079_signal},
    "f13mc_f13_macd_variants_macdLow_streak_19_39_base_v080_signal": {"inputs": ["low"], "func": f13mc_f13_macd_variants_macdLow_streak_19_39_base_v080_signal},
    "f13mc_f13_macd_variants_macd_highlow_diff_19_39_base_v081_signal": {"inputs": ["high", "low"], "func": f13mc_f13_macd_variants_macd_highlow_diff_19_39_base_v081_signal},
    "f13mc_f13_macd_variants_ppo_quantile_12_26_252d_base_v082_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_ppo_quantile_12_26_252d_base_v082_signal},
    "f13mc_f13_macd_variants_ppo_xover_count_60d_base_v083_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_ppo_xover_count_60d_base_v083_signal},
    "f13mc_f13_macd_variants_ppo_50_200_z_base_v084_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_ppo_50_200_z_base_v084_signal},
    "f13mc_f13_macd_variants_macd_logret_12_26_base_v085_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_macd_logret_12_26_base_v085_signal},
    "f13mc_f13_macd_variants_macd_absret_12_26_base_v086_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_macd_absret_12_26_base_v086_signal},
    "f13mc_f13_macd_variants_macd_squaredret_19_39_base_v087_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_macd_squaredret_19_39_base_v087_signal},
    "f13mc_f13_macd_variants_obv_macd_12_26_base_v088_signal": {"inputs": ["close", "volume"], "func": f13mc_f13_macd_variants_obv_macd_12_26_base_v088_signal},
    "f13mc_f13_macd_variants_obv_macd_hist_19_39_9_base_v089_signal": {"inputs": ["close", "volume"], "func": f13mc_f13_macd_variants_obv_macd_hist_19_39_9_base_v089_signal},
    "f13mc_f13_macd_variants_pvt_macd_12_26_base_v090_signal": {"inputs": ["close", "volume"], "func": f13mc_f13_macd_variants_pvt_macd_12_26_base_v090_signal},
    "f13mc_f13_macd_variants_volMACD_sign_12_26_base_v091_signal": {"inputs": ["volume"], "func": f13mc_f13_macd_variants_volMACD_sign_12_26_base_v091_signal},
    "f13mc_f13_macd_variants_macd_over_atr_sign_12_26_14_base_v092_signal": {"inputs": ["high", "low", "close"], "func": f13mc_f13_macd_variants_macd_over_atr_sign_12_26_14_base_v092_signal},
    "f13mc_f13_macd_variants_macd_over_atr_streak_50_200_50_base_v093_signal": {"inputs": ["high", "low", "closeadj"], "func": f13mc_f13_macd_variants_macd_over_atr_streak_50_200_50_base_v093_signal},
    "f13mc_f13_macd_variants_hist_over_atr_sign_12_26_9_14_base_v094_signal": {"inputs": ["high", "low", "close"], "func": f13mc_f13_macd_variants_hist_over_atr_sign_12_26_9_14_base_v094_signal},
    "f13mc_f13_macd_variants_sign_macd_logret_12_26_base_v095_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_sign_macd_logret_12_26_base_v095_signal},
    "f13mc_f13_macd_variants_sign_macd_obv_12_26_base_v096_signal": {"inputs": ["close", "volume"], "func": f13mc_f13_macd_variants_sign_macd_obv_12_26_base_v096_signal},
    "f13mc_f13_macd_variants_dayssince_obv_x_12_26_base_v097_signal": {"inputs": ["close", "volume"], "func": f13mc_f13_macd_variants_dayssince_obv_x_12_26_base_v097_signal},
    "f13mc_f13_macd_variants_streak_logretmacd_12_26_base_v098_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_streak_logretmacd_12_26_base_v098_signal},
    "f13mc_f13_macd_variants_macd_obv_pos_state_base_v099_signal": {"inputs": ["close", "volume"], "func": f13mc_f13_macd_variants_macd_obv_pos_state_base_v099_signal},
    "f13mc_f13_macd_variants_hist_hl2_z_60d_base_v100_signal": {"inputs": ["high", "low"], "func": f13mc_f13_macd_variants_hist_hl2_z_60d_base_v100_signal},
    "f13mc_f13_macd_variants_hist_logret_8_21_5_base_v101_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_hist_logret_8_21_5_base_v101_signal},
    "f13mc_f13_macd_variants_hist_obv_12_26_9_base_v102_signal": {"inputs": ["close", "volume"], "func": f13mc_f13_macd_variants_hist_obv_12_26_9_base_v102_signal},
    "f13mc_f13_macd_variants_slope_hl2_macd_12_26_base_v103_signal": {"inputs": ["high", "low"], "func": f13mc_f13_macd_variants_slope_hl2_macd_12_26_base_v103_signal},
    "f13mc_f13_macd_variants_curv_logret_macd_12_26_base_v104_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_curv_logret_macd_12_26_base_v104_signal},
    "f13mc_f13_macd_variants_obv_macd_z_19_39_60d_base_v105_signal": {"inputs": ["close", "volume"], "func": f13mc_f13_macd_variants_obv_macd_z_19_39_60d_base_v105_signal},
    "f13mc_f13_macd_variants_signal_rank_12_26_9_60d_base_v106_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_signal_rank_12_26_9_60d_base_v106_signal},
    "f13mc_f13_macd_variants_signalslope_12_26_9_5d_base_v107_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_signalslope_12_26_9_5d_base_v107_signal},
    "f13mc_f13_macd_variants_dualsignal_diff_12_26_base_v108_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_dualsignal_diff_12_26_base_v108_signal},
    "f13mc_f13_macd_variants_macd_lower_band_breaks_60d_base_v109_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_macd_lower_band_breaks_60d_base_v109_signal},
    "f13mc_f13_macd_variants_macd_bandwidth_60d_base_v110_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_macd_bandwidth_60d_base_v110_signal},
    "f13mc_f13_macd_variants_macd_regime_align_base_v111_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_macd_regime_align_base_v111_signal},
    "f13mc_f13_macd_variants_macd_pair_disagree_count_60d_base_v112_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_macd_pair_disagree_count_60d_base_v112_signal},
    "f13mc_f13_macd_variants_macd_x_signal_pair_base_v113_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_macd_x_signal_pair_base_v113_signal},
    "f13mc_f13_macd_variants_ao_rank_5_34_60d_base_v114_signal": {"inputs": ["high", "low"], "func": f13mc_f13_macd_variants_ao_rank_5_34_60d_base_v114_signal},
    "f13mc_f13_macd_variants_ac_5_34_base_v115_signal": {"inputs": ["high", "low"], "func": f13mc_f13_macd_variants_ac_5_34_base_v115_signal},
    "f13mc_f13_macd_variants_ao_sign_5_34_base_v116_signal": {"inputs": ["high", "low"], "func": f13mc_f13_macd_variants_ao_sign_5_34_base_v116_signal},
    "f13mc_f13_macd_variants_kst_hist_9_base_v118_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_kst_hist_9_base_v118_signal},
    "f13mc_f13_macd_variants_atrMACD_14_50_base_v119_signal": {"inputs": ["high", "low", "close"], "func": f13mc_f13_macd_variants_atrMACD_14_50_base_v119_signal},
    "f13mc_f13_macd_variants_atrMACD_sign_14_50_base_v120_signal": {"inputs": ["high", "low", "closeadj"], "func": f13mc_f13_macd_variants_atrMACD_sign_14_50_base_v120_signal},
    "f13mc_f13_macd_variants_macdrank_19_39_252d_base_v121_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_macdrank_19_39_252d_base_v121_signal},
    "f13mc_f13_macd_variants_macdz_50_200_120d_base_v122_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_macdz_50_200_120d_base_v122_signal},
    "f13mc_f13_macd_variants_macd_volconfirm_20d_base_v123_signal": {"inputs": ["close", "volume"], "func": f13mc_f13_macd_variants_macd_volconfirm_20d_base_v123_signal},
    "f13mc_f13_macd_variants_macd_volMACD_interact_base_v124_signal": {"inputs": ["close", "volume"], "func": f13mc_f13_macd_variants_macd_volMACD_interact_base_v124_signal},
    "f13mc_f13_macd_variants_hist_autocorr1_60d_base_v125_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_hist_autocorr1_60d_base_v125_signal},
    "f13mc_f13_macd_variants_macd_autocorr1_60d_base_v126_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_macd_autocorr1_60d_base_v126_signal},
    "f13mc_f13_macd_variants_macd_above_close_state_50_200_base_v127_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_macd_above_close_state_50_200_base_v127_signal},
    "f13mc_f13_macd_variants_histflip_50_200_30_event_60d_base_v128_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_histflip_50_200_30_event_60d_base_v128_signal},
    "f13mc_f13_macd_variants_histflip_19_39_13_event_30d_base_v129_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_histflip_19_39_13_event_30d_base_v129_signal},
    "f13mc_f13_macd_variants_macd_x_pricez_12_26_60d_base_v130_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_macd_x_pricez_12_26_60d_base_v130_signal},
    "f13mc_f13_macd_variants_macd_medsmoothed_minus_classic_base_v131_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_macd_medsmoothed_minus_classic_base_v131_signal},
    "f13mc_f13_macd_variants_macd_minmaxmid_minus_classic_base_v132_signal": {"inputs": ["high", "low", "closeadj"], "func": f13mc_f13_macd_variants_macd_minmaxmid_minus_classic_base_v132_signal},
    "f13mc_f13_macd_variants_histmaxabs_12_26_9_60d_base_v134_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_histmaxabs_12_26_9_60d_base_v134_signal},
    "f13mc_f13_macd_variants_macdrank_12_50_120d_base_v135_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_macdrank_12_50_120d_base_v135_signal},
    "f13mc_f13_macd_variants_macd_sign_8_50_base_v136_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_macd_sign_8_50_base_v136_signal},
    "f13mc_f13_macd_variants_macdz_26_100_60d_base_v137_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_macdz_26_100_60d_base_v137_signal},
    "f13mc_f13_macd_variants_macdpctbucket_12_26_60d_base_v138_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_macdpctbucket_12_26_60d_base_v138_signal},
    "f13mc_f13_macd_variants_macd_pos_streak_run_50_200_base_v139_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_macd_pos_streak_run_50_200_base_v139_signal},
    "f13mc_f13_macd_variants_dayssince_macd_max_60d_base_v140_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_dayssince_macd_max_60d_base_v140_signal},
    "f13mc_f13_macd_variants_dayssince_hist_min_30d_base_v141_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_dayssince_hist_min_30d_base_v141_signal},
    "f13mc_f13_macd_variants_diff_macd_pair_rank_60d_base_v142_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_diff_macd_pair_rank_60d_base_v142_signal},
    "f13mc_f13_macd_variants_histaccelfrac_12_26_9_30d_base_v143_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_histaccelfrac_12_26_9_30d_base_v143_signal},
    "f13mc_f13_macd_variants_hist_vs_emahist_sign_12_26_9_5_base_v144_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_hist_vs_emahist_sign_12_26_9_5_base_v144_signal},
    "f13mc_f13_macd_variants_hist_minus_emahist_12_26_9_5_base_v145_signal": {"inputs": ["close"], "func": f13mc_f13_macd_variants_hist_minus_emahist_12_26_9_5_base_v145_signal},
    "f13mc_f13_macd_variants_macdrelative_rank_30d_base_v146_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_macdrelative_rank_30d_base_v146_signal},
    "f13mc_f13_macd_variants_macdHmacdL_sign_12_26_base_v147_signal": {"inputs": ["high", "low"], "func": f13mc_f13_macd_variants_macdHmacdL_sign_12_26_base_v147_signal},
    "f13mc_f13_macd_variants_macd_x_signal_pair2_60d_base_v148_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_macd_x_signal_pair2_60d_base_v148_signal},
    "f13mc_f13_macd_variants_tanh_macdbias_50_200_60d_base_v149_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_tanh_macdbias_50_200_60d_base_v149_signal},
    "f13mc_f13_macd_variants_macdslope_rank_12_26_60d_base_v150_signal": {"inputs": ["closeadj"], "func": f13mc_f13_macd_variants_macdslope_rank_12_26_60d_base_v150_signal},
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
    for name, entry in f13_macd_variants_base_076_150_REGISTRY.items():
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
