"""f20_volatility_compression_expansion base features 076-150.

Continued domain: vol compression vs expansion (TRANSITION direction).
This file avoids the formulas in base_001_075 (no shared expression up to a
window-size change). Uses different structural classes:
  - Keltner-width measures (instead of BB-width-as-primary)
  - Squared-return-based vol (instead of std-of-returns)
  - Garman-Klass partial range estimators (compression of OHLC dispersion)
  - Compression/expansion using HIGH-LOW envelope dispersion
  - Distance-from-band features (Keltner / Donchian / Chandelier proxy)
  - Vol-of-vol / vol-of-range cross signals
  - True-range to high-low ratio (gap-induced expansion)
  - Mean reversion of vol (regression slope of vol on time)
  - Distance to historical squeeze episode
  - Long-window expansion z-scores
  - Median-of-range based compression
  - Range-cluster statistics (count of small ranges in short window)
  - Hi-vs-Lo asymmetric expansion (upside vol vs downside vol)

NaN policy: never fillna(<value>); only replace([inf,-inf],nan) at the
final return. Window > 21d -> closeadj; <= 21d -> close. Intra-bar uses
unadjusted high/low/open/close.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _sma(s, n):
    return s.rolling(n, min_periods=n).mean()


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=n).mean()


def _tr(high, low, close):
    pc = close.shift(1)
    return pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)


def _atr(high, low, close, n):
    return _tr(high, low, close).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()


# ---------------------------------------------------------------------------
# Features 076-150
# ---------------------------------------------------------------------------


# === Keltner-channel width based features (NOT BB-width) ===================


def f20ce_f20_volatility_compression_expansion_kc_width_div_close_20d_base_v076_signal(high, low, close):
    """Keltner Channel (1.5 ATR) width / SMA(close,20). Compression of vol envelope."""
    n = 20
    atr = _tr(high, low, close).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    mid = close.rolling(n, min_periods=n).mean()
    w = (3.0 * atr) / mid.replace(0.0, np.nan)
    return w.replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_kc_width_rank_120d_base_v077_signal(high, low, closeadj):
    """Pctile rank of Keltner(40, 1.5 ATR) width over 120d. Low = compressed env."""
    n = 40
    atr = _tr(high, low, closeadj).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    mid = closeadj.rolling(n, min_periods=n).mean()
    w = (3.0 * atr) / mid.replace(0.0, np.nan)
    return w.rolling(120, min_periods=60).apply(
        lambda x: float((x < x[-1]).sum()) / float(len(x) - 1) if len(x) > 1 else np.nan,
        raw=True,
    ).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_kc_vs_bbw_v078_signal(high, low, closeadj):
    """KC(20,1.5) - BB(20,2) (normalized by close). Positive when BB is inside KC
    (squeeze); negative when BB expands beyond KC."""
    n = 20
    atr = _tr(high, low, closeadj).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    mid = closeadj.rolling(n, min_periods=n).mean()
    sd = closeadj.rolling(n, min_periods=n).std(ddof=0)
    kc_w = 3.0 * atr
    bb_w = 4.0 * sd
    return ((kc_w - bb_w) / mid.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Squared-return-based vol contraction (Parkinson-like but scoped) ======


def f20ce_f20_volatility_compression_expansion_sqret_short_long_30_120_v079_signal(closeadj):
    """SMA(squared returns, 30) / SMA(squared returns, 120). Vol contraction ratio."""
    r2 = closeadj.pct_change() ** 2
    return (r2.rolling(30, min_periods=30).mean() / r2.rolling(120, min_periods=60).mean().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_sqret_zscore_60d_v080_signal(closeadj):
    """Z-score of squared returns vs 60d mean/std. Positive = expansion shock."""
    r2 = closeadj.pct_change() ** 2
    mu = r2.rolling(60, min_periods=30).mean()
    sd = r2.rolling(60, min_periods=30).std(ddof=0)
    return ((r2 - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_sqret_decline_streak_20d_v081_signal(closeadj):
    """Consecutive days SMA(r^2, 20) is declining. Compression streak."""
    r2 = closeadj.pct_change() ** 2
    v = r2.rolling(20, min_periods=20).mean()
    cond = (v.diff() < 0.0).astype(float).where(~v.diff().isna())
    out = pd.Series(np.nan, index=closeadj.index, dtype=float)
    cnt = 0.0
    for i in range(len(cond)):
        x = cond.iat[i]
        if not np.isfinite(x):
            out.iat[i] = np.nan
            continue
        if x > 0.5:
            cnt += 1.0
        else:
            cnt = 0.0
        out.iat[i] = cnt
    return out.where(out.notna()).replace([np.inf, -np.inf], np.nan)


# === Garman-Klass partial range compression (uses OHLC log differences) ===


def f20ce_f20_volatility_compression_expansion_log_hl_sq_rank_60d_v082_signal(high, low):
    """Pctile rank of (log(high/low))^2 over 60d. Low = compressed intraday."""
    x = (np.log(high / low.replace(0.0, np.nan))) ** 2
    return x.rolling(60, min_periods=30).apply(
        lambda x: float((x < x[-1]).sum()) / float(len(x) - 1) if len(x) > 1 else np.nan,
        raw=True,
    ).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_log_co_sq_short_long_v083_signal(open_, closeadj):
    """SMA((log(close/open))^2, 20) / SMA(., 80). Close-to-open vol contraction."""
    x = (np.log(closeadj / open_.replace(0.0, np.nan))) ** 2
    return (x.rolling(20, min_periods=20).mean() / x.rolling(80, min_periods=40).mean().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Distance-from-Keltner-band (close penetrates band as expansion sign) ==


def f20ce_f20_volatility_compression_expansion_close_vs_kc_upper_norm_v084_signal(high, low, closeadj):
    """(closeadj - KC_upper(20, 2 ATR)) / ATR(20). Positive => above-upper-band breakout."""
    n = 20
    atr = _tr(high, low, closeadj).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    mid = closeadj.rolling(n, min_periods=n).mean()
    kc_up = mid + 2.0 * atr
    return ((closeadj - kc_up) / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_close_outside_kc_count_30d_v085_signal(high, low, closeadj):
    """Count of bars in trailing 30d where close was outside KC(40, 2 ATR)."""
    n = 40
    atr = _tr(high, low, closeadj).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    mid = closeadj.rolling(n, min_periods=n).mean()
    kc_up = mid + 2.0 * atr
    kc_lo = mid - 2.0 * atr
    flag = ((closeadj > kc_up) | (closeadj < kc_lo)).astype(float).where(~mid.isna())
    return flag.rolling(30, min_periods=20).sum().replace([np.inf, -np.inf], np.nan)


# === Vol-of-vol and vol-of-range cross indicators ==========================


def f20ce_f20_volatility_compression_expansion_volofrange_30d_v086_signal(high, low):
    """Std of (high - low) over 30d divided by mean(high - low, 30). Coefficient of
    variation of range. Low = stable, compressed; high = unstable range."""
    rng = high - low
    return (rng.rolling(30, min_periods=15).std(ddof=0) / rng.rolling(30, min_periods=15).mean().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_volofrange_zscore_v087_signal(high, low, closeadj):
    """Z-score of CV-of-range vs 100d. High = unstable expansion regime."""
    rng = high - low
    cv = rng.rolling(20, min_periods=20).std(ddof=0) / rng.rolling(20, min_periods=20).mean().replace(0.0, np.nan)
    mu = cv.rolling(100, min_periods=50).mean()
    sd = cv.rolling(100, min_periods=50).std(ddof=0)
    return ((cv - mu) / sd.replace(0.0, np.nan)).where(~closeadj.isna()).replace([np.inf, -np.inf], np.nan)


# === True-range vs intraday range (gap-induced expansion) =================


def f20ce_f20_volatility_compression_expansion_tr_vs_hl_ratio_20d_v088_signal(high, low, close):
    """SMA(TR / (high - low), 20). >1 => gap-driven expansion regime."""
    rng = (high - low).replace(0.0, np.nan)
    tr = _tr(high, low, close)
    return (tr / rng).rolling(20, min_periods=10).mean().replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_gap_jump_count_60d_v089_signal(high, low, closeadj):
    """Count over 60d of bars where TR > 1.3*(high-low). Gap-driven expansion count."""
    rng = (high - low).replace(0.0, np.nan)
    tr = _tr(high, low, closeadj)
    flag = (tr > 1.3 * rng).astype(float).where(~rng.isna())
    return flag.rolling(60, min_periods=30).sum().replace([np.inf, -np.inf], np.nan)


# === Mean reversion of vol via regression slope =============================


def f20ce_f20_volatility_compression_expansion_vol_regslope_40d_v090_signal(closeadj):
    """OLS slope of vol(15) on time over trailing 40d. Negative = compressing."""
    v = closeadj.pct_change().rolling(15, min_periods=15).std(ddof=0)
    def _slope(x):
        n = len(x); t = np.arange(n, dtype=float); xm = x.mean(); tm = t.mean()
        num = np.dot(x - xm, t - tm); den = np.dot(t - tm, t - tm)
        return float(num / den) if den != 0.0 else np.nan
    return v.rolling(40, min_periods=25).apply(_slope, raw=True).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_atr_regslope_80d_v091_signal(high, low, closeadj):
    """OLS slope of ATR(20) on time over 80d. Negative = compressing ATR."""
    atr = _tr(high, low, closeadj).ewm(alpha=1.0 / 20.0, adjust=False, min_periods=20).mean()
    def _slope(x):
        n = len(x); t = np.arange(n, dtype=float); xm = x.mean(); tm = t.mean()
        num = np.dot(x - xm, t - tm); den = np.dot(t - tm, t - tm)
        return float(num / den) if den != 0.0 else np.nan
    return atr.rolling(80, min_periods=40).apply(_slope, raw=True).replace([np.inf, -np.inf], np.nan)


# === Distance to historical minimum of width =================================


def f20ce_f20_volatility_compression_expansion_bbw_zdist_to_min_v092_signal(closeadj):
    """(BBW(30) - 200d-min BBW) / 200d-std BBW. ~0 = at compression floor."""
    n = 30
    m = closeadj.rolling(n, min_periods=n).mean()
    sd = closeadj.rolling(n, min_periods=n).std(ddof=0)
    bbw = (4.0 * sd) / m.replace(0.0, np.nan)
    mn = bbw.rolling(200, min_periods=100).min()
    sigma = bbw.rolling(200, min_periods=100).std(ddof=0)
    return ((bbw - mn) / sigma.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_atr_dist_to_max_60d_v093_signal(high, low, closeadj):
    """(ATR(20) - 60d-max ATR) / 60d-mean ATR. <0 = below expansion ceiling."""
    atr = _tr(high, low, closeadj).ewm(alpha=1.0 / 20.0, adjust=False, min_periods=20).mean()
    mx = atr.rolling(60, min_periods=30).max()
    mu = atr.rolling(60, min_periods=30).mean()
    return ((atr - mx) / mu.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Long-window expansion ratios ==========================================


def f20ce_f20_volatility_compression_expansion_vol_long_horizon_ratio_v094_signal(closeadj):
    """vol(252) / vol(63) - 1. Annual-vs-quarterly vol gap. >0 = compression at
    quarterly horizon; <0 = sustained expansion."""
    vy = closeadj.pct_change().rolling(252, min_periods=126).std(ddof=0)
    vq = closeadj.pct_change().rolling(63, min_periods=63).std(ddof=0)
    return (vy / vq.replace(0.0, np.nan) - 1.0).replace([np.inf, -np.inf], np.nan)


# === Median-of-range based compression =====================================


def f20ce_f20_volatility_compression_expansion_med_range_rank_80d_v095_signal(high, low):
    """Pctile rank of MEDIAN(range, 20) over 80d. Low = compressed central range."""
    rng = high - low
    med = rng.rolling(20, min_periods=20).median()
    return med.rolling(80, min_periods=40).apply(
        lambda x: float((x < x[-1]).sum()) / float(len(x) - 1) if len(x) > 1 else np.nan,
        raw=True,
    ).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_p10_range_rel_p90_v096_signal(high, low):
    """10th percentile range / 90th percentile range over 50d. ~1 = compressed range
    distribution; small = expanded asymmetric distribution."""
    rng = high - low
    q10 = rng.rolling(50, min_periods=25).quantile(0.10)
    q90 = rng.rolling(50, min_periods=25).quantile(0.90)
    return (q10 / q90.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Cluster of small ranges in trailing window ============================


def f20ce_f20_volatility_compression_expansion_small_range_cluster_10d_v097_signal(high, low):
    """Count over 10d of bars with range < 30th percentile (over 60d). Sustained
    small-range cluster = strong compression."""
    rng = high - low
    q30 = rng.rolling(60, min_periods=30).quantile(0.30)
    flag = (rng < q30).astype(float).where(~q30.isna())
    return flag.rolling(10, min_periods=5).sum().replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_large_range_cluster_10d_v098_signal(high, low):
    """Count over 10d of bars with range > 70th percentile (over 60d). Expansion cluster."""
    rng = high - low
    q70 = rng.rolling(60, min_periods=30).quantile(0.70)
    flag = (rng > q70).astype(float).where(~q70.isna())
    return flag.rolling(10, min_periods=5).sum().replace([np.inf, -np.inf], np.nan)


# === Hi-vs-Lo asymmetric expansion (upside vol vs downside vol) ============


def f20ce_f20_volatility_compression_expansion_up_down_vol_ratio_30d_v099_signal(closeadj):
    """sqrt(SMA(r^2 where r>0, 30)) / sqrt(SMA(r^2 where r<0, 30)). >1 = upside expansion."""
    r = closeadj.pct_change()
    pos_sq = (r ** 2).where(r > 0.0, 0.0).where(~r.isna())
    neg_sq = (r ** 2).where(r < 0.0, 0.0).where(~r.isna())
    upv = pos_sq.rolling(30, min_periods=30).mean() ** 0.5
    dnv = neg_sq.rolling(30, min_periods=30).mean() ** 0.5
    return (upv / dnv.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_up_minus_down_vol_z_v100_signal(closeadj):
    """Z-score of (up_vol - down_vol)(20) vs 80d mean/std. Asymmetric expansion direction."""
    r = closeadj.pct_change()
    pos_sq = (r ** 2).where(r > 0.0, 0.0).where(~r.isna())
    neg_sq = (r ** 2).where(r < 0.0, 0.0).where(~r.isna())
    upv = pos_sq.rolling(20, min_periods=20).mean() ** 0.5
    dnv = neg_sq.rolling(20, min_periods=20).mean() ** 0.5
    diff = upv - dnv
    mu = diff.rolling(80, min_periods=40).mean()
    sd = diff.rolling(80, min_periods=40).std(ddof=0)
    return ((diff - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Gap-down expansion vs gap-up expansion ===============================


def f20ce_f20_volatility_compression_expansion_gap_abs_30d_avg_v101_signal(open_, closeadj):
    """SMA(|open - prev_close| / prev_close, 30). Gap magnitude vol component."""
    pc = closeadj.shift(1)
    gap = (open_ - pc).abs() / pc.replace(0.0, np.nan)
    return gap.rolling(30, min_periods=15).mean().replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_gap_zscore_60d_v102_signal(open_, closeadj):
    """Z-score of today's gap abs vs 60d mean/std. Compression in overnight vol."""
    pc = closeadj.shift(1)
    gap = (open_ - pc).abs() / pc.replace(0.0, np.nan)
    mu = gap.rolling(60, min_periods=30).mean()
    sd = gap.rolling(60, min_periods=30).std(ddof=0)
    return ((gap - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Time fraction in compression / expansion regime =======================


def f20ce_f20_volatility_compression_expansion_frac_below_p25_vol_60d_v103_signal(closeadj):
    """Fraction over 60d where vol(10) is below 25th percentile (computed over 100d)."""
    v = closeadj.pct_change().rolling(10, min_periods=10).std(ddof=0)
    q25 = v.rolling(100, min_periods=50).quantile(0.25)
    flag = (v < q25).astype(float).where(~q25.isna())
    return flag.rolling(60, min_periods=30).mean().replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_frac_above_p75_vol_60d_v104_signal(closeadj):
    """Fraction over 60d where vol(10) is above 75th percentile. Expansion regime fraction."""
    v = closeadj.pct_change().rolling(10, min_periods=10).std(ddof=0)
    q75 = v.rolling(100, min_periods=50).quantile(0.75)
    flag = (v > q75).astype(float).where(~q75.isna())
    return flag.rolling(60, min_periods=30).mean().replace([np.inf, -np.inf], np.nan)


# === Sign-of-vol-momentum ==================================================


def f20ce_f20_volatility_compression_expansion_vol_mom_sign_short_long_v105_signal(closeadj):
    """sign(vol(10).diff(20) - vol(40).diff(20)). Cross of short and long vol momentum."""
    v10 = closeadj.pct_change().rolling(10, min_periods=10).std(ddof=0)
    v40 = closeadj.pct_change().rolling(40, min_periods=40).std(ddof=0)
    return np.sign(v10.diff(20) - v40.diff(20)).replace([np.inf, -np.inf], np.nan)


# === Range-percentile crossover events =====================================


def f20ce_f20_volatility_compression_expansion_range_pctile_cross_event_v106_signal(high, low):
    """+1 if range rank crosses above 0.75; -1 below 0.25; 0 otherwise. Discrete
    regime-transition event."""
    rng = high - low
    rank = rng.rolling(60, min_periods=30).apply(
        lambda x: float((x < x[-1]).sum()) / float(len(x) - 1) if len(x) > 1 else np.nan,
        raw=True,
    )
    up = ((rank > 0.75) & (rank.shift(1) <= 0.75)).astype(float)
    dn = ((rank < 0.25) & (rank.shift(1) >= 0.25)).astype(float)
    return (up - dn).where(~rank.isna() & ~rank.shift(1).isna()).replace([np.inf, -np.inf], np.nan)


# === Concentration of vol in recent bars ==================================


def f20ce_f20_volatility_compression_expansion_recent_vol_concentration_v107_signal(closeadj):
    """SUM(r^2, last 5) / SUM(r^2, last 30). High value = vol concentrated in
    recent bars (expansion phase). Low = spread out (compression)."""
    r2 = closeadj.pct_change() ** 2
    return (r2.rolling(5, min_periods=5).sum() / r2.rolling(30, min_periods=15).sum().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Ratio of returns above/below 1-stdev =================================


def f20ce_f20_volatility_compression_expansion_tailshare_60d_v108_signal(closeadj):
    """Fraction of trailing 60d returns with |r| > 1 std (computed on same window).
    > 0.32 = fat tails, < 0.32 = compressed."""
    r = closeadj.pct_change()
    sd = r.rolling(60, min_periods=30).std(ddof=0)
    flag = (r.abs() > sd).astype(float).where(~sd.isna())
    return flag.rolling(60, min_periods=30).mean().replace([np.inf, -np.inf], np.nan)


# === Vol mean reversion: distance from long-run mean =======================


def f20ce_f20_volatility_compression_expansion_vol_dist_from_252d_mean_v109_signal(closeadj):
    """(vol(30) / SMA(vol(30), 252)) - 1. Positive = above long-run mean (expansion)."""
    v = closeadj.pct_change().rolling(30, min_periods=30).std(ddof=0)
    avg = v.rolling(252, min_periods=126).mean()
    return (v / avg.replace(0.0, np.nan) - 1.0).replace([np.inf, -np.inf], np.nan)


# === Compression depth (drawdown of vol from its trailing max) ============


def f20ce_f20_volatility_compression_expansion_vol_drawdown_60d_v110_signal(closeadj):
    """(vol(20) - max(vol(20), 60)) / max(vol(20), 60). <0 = pulled below recent max."""
    v = closeadj.pct_change().rolling(20, min_periods=20).std(ddof=0)
    mx = v.rolling(60, min_periods=30).max()
    return ((v - mx) / mx.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_vol_runup_60d_v111_signal(closeadj):
    """(vol(20) - min(vol(20), 60)) / min(vol(20), 60). >0 = run up from compression floor."""
    v = closeadj.pct_change().rolling(20, min_periods=20).std(ddof=0)
    mn = v.rolling(60, min_periods=30).min()
    return ((v - mn) / mn.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Sequential triple-bar contraction =====================================


def f20ce_f20_volatility_compression_expansion_3bar_contraction_v112_signal(high, low):
    """Binary: today range < yesterday range < day-before range (3-bar contraction)."""
    rng = high - low
    cond = (rng < rng.shift(1)) & (rng.shift(1) < rng.shift(2))
    return cond.astype(float).where(~rng.shift(2).isna()).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_3bar_expansion_v113_signal(high, low):
    """Binary: today range > yesterday range > day-before range (3-bar expansion)."""
    rng = high - low
    cond = (rng > rng.shift(1)) & (rng.shift(1) > rng.shift(2))
    return cond.astype(float).where(~rng.shift(2).isna()).replace([np.inf, -np.inf], np.nan)


# === Vol of close-price acceleration =======================================


def f20ce_f20_volatility_compression_expansion_pricecurv_vol_30d_v114_signal(closeadj):
    """std of (close - 2*close.shift(5) + close.shift(10)) / close, over 30d.
    Compression of price curvature."""
    curv = (closeadj - 2.0 * closeadj.shift(5) + closeadj.shift(10)) / closeadj.replace(0.0, np.nan)
    return curv.rolling(30, min_periods=15).std(ddof=0).replace([np.inf, -np.inf], np.nan)


# === Compression breadth (how many short-term measures show compression) ==


def f20ce_f20_volatility_compression_expansion_compression_breadth_v115_signal(high, low, closeadj):
    """Number TRUE of: vol(5)<vol(20), vol(10)<vol(40), range<SMA(range,30),
    ATR(5)<ATR(20). Range 0..4."""
    r = closeadj.pct_change()
    v5 = r.rolling(5, min_periods=5).std(ddof=0)
    v10 = r.rolling(10, min_periods=10).std(ddof=0)
    v20 = r.rolling(20, min_periods=20).std(ddof=0)
    v40 = r.rolling(40, min_periods=40).std(ddof=0)
    rng = high - low
    rng_avg = rng.rolling(30, min_periods=15).mean()
    a5 = _tr(high, low, closeadj).ewm(alpha=1.0 / 5.0, adjust=False, min_periods=5).mean()
    a20 = _tr(high, low, closeadj).ewm(alpha=1.0 / 20.0, adjust=False, min_periods=20).mean()
    c = (v5 < v20).astype(float) + (v10 < v40).astype(float) + (rng < rng_avg).astype(float) + (a5 < a20).astype(float)
    return c.where(~v40.isna() & ~rng_avg.isna()).replace([np.inf, -np.inf], np.nan)


# === Compression duration percentile rank ==================================


def f20ce_f20_volatility_compression_expansion_compress_streak_rank_v116_signal(closeadj):
    """Pctile rank (over 200d) of current consecutive-days-below-median vol streak."""
    v = closeadj.pct_change().rolling(20, min_periods=20).std(ddof=0)
    med = v.rolling(60, min_periods=30).median()
    cond = (v < med).astype(float).where(~med.isna())
    out = pd.Series(np.nan, index=closeadj.index, dtype=float)
    cnt = 0.0
    for i in range(len(cond)):
        x = cond.iat[i]
        if not np.isfinite(x):
            out.iat[i] = np.nan
            continue
        if x > 0.5:
            cnt += 1.0
        else:
            cnt = 0.0
        out.iat[i] = cnt
    return out.rolling(200, min_periods=100).apply(
        lambda x: float((x < x[-1]).sum()) / float(len(x) - 1) if len(x) > 1 else np.nan,
        raw=True,
    ).replace([np.inf, -np.inf], np.nan)


# === Reversal-of-vol-direction count ======================================


def f20ce_f20_volatility_compression_expansion_vol_dir_reversals_60d_v117_signal(closeadj):
    """Count over 60d of bars where sign of vol(20).diff(5) flips. High = unstable
    transition zone."""
    v = closeadj.pct_change().rolling(20, min_periods=20).std(ddof=0)
    s = np.sign(v.diff(5))
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(60, min_periods=30).sum().replace([np.inf, -np.inf], np.nan)


# === Vol residual after AR(1) (mean-reversion strength) ====================


def f20ce_f20_volatility_compression_expansion_vol_ar1_residual_v118_signal(closeadj):
    """vol(20) - rolling_corr(vol, vol.shift(1), 60) * vol.shift(1). Approx AR(1) residual."""
    v = closeadj.pct_change().rolling(20, min_periods=20).std(ddof=0)
    rho = v.rolling(60, min_periods=30).corr(v.shift(1))
    pred = rho * v.shift(1)
    return (v - pred).replace([np.inf, -np.inf], np.nan)


# === Compression detection via Hurst-like exponent on |returns| ===========


def f20ce_f20_volatility_compression_expansion_absret_persistence_60d_v119_signal(closeadj):
    """corr(|r|, |r|.shift(1)) over 60d. High = persistent abs-return regime."""
    ar = closeadj.pct_change().abs()
    return ar.rolling(60, min_periods=30).corr(ar.shift(1)).replace([np.inf, -np.inf], np.nan)


# === Skew of vol (regime asymmetry) ========================================


def f20ce_f20_volatility_compression_expansion_vol_skew_80d_v120_signal(closeadj):
    """Skew of vol(10) over 80d. Positive = expansion shocks above baseline; negative
    = compression-heavy distribution."""
    v = closeadj.pct_change().rolling(10, min_periods=10).std(ddof=0)
    return v.rolling(80, min_periods=40).skew().replace([np.inf, -np.inf], np.nan)


# === Volume-weighted vol expansion ratio ===================================


def f20ce_f20_volatility_compression_expansion_vw_volatility_ratio_v121_signal(closeadj, volume):
    """SMA(|r| * v, 20) / SMA(|r|, 20) / SMA(v, 20). >1 when vol clusters on high-volume."""
    r = closeadj.pct_change().abs()
    num = (r * volume).rolling(20, min_periods=20).sum()
    den_r = r.rolling(20, min_periods=20).sum().replace(0.0, np.nan)
    den_v = volume.rolling(20, min_periods=20).sum().replace(0.0, np.nan) / 20.0
    return (num / (den_r * den_v)).replace([np.inf, -np.inf], np.nan)


# === Range entropy =========================================================


def f20ce_f20_volatility_compression_expansion_range_entropy_50d_v122_signal(high, low):
    """Shannon-ish entropy proxy of range bucket counts over 50d. Low = compressed
    around one bucket; high = diffuse."""
    rng = high - low
    def _ent(x):
        q = np.quantile(x, [0.25, 0.5, 0.75])
        buckets = np.array([(x <= q[0]).sum(), ((x > q[0]) & (x <= q[1])).sum(),
                            ((x > q[1]) & (x <= q[2])).sum(), (x > q[2]).sum()], dtype=float)
        p = buckets / buckets.sum()
        p = p[p > 0]
        return float(-(p * np.log(p)).sum())
    return rng.rolling(50, min_periods=25).apply(_ent, raw=True).replace([np.inf, -np.inf], np.nan)


# === Bollinger %B as compression diagnostic (close at extremes) ===========


def f20ce_f20_volatility_compression_expansion_pctb_extreme_freq_30d_v123_signal(closeadj):
    """Fraction of last 30 days where Bollinger %B(20) is outside [0.05, 0.95].
    High freq => sustained band-walks (expansion)."""
    n = 20
    m = closeadj.rolling(n, min_periods=n).mean()
    sd = closeadj.rolling(n, min_periods=n).std(ddof=0)
    pctb = (closeadj - (m - 2.0 * sd)) / (4.0 * sd).replace(0.0, np.nan)
    flag = ((pctb < 0.05) | (pctb > 0.95)).astype(float).where(~pctb.isna())
    return flag.rolling(30, min_periods=15).mean().replace([np.inf, -np.inf], np.nan)


# === Compression-Expansion Index (composite signed score) =================


def f20ce_f20_volatility_compression_expansion_cei_composite_v124_signal(high, low, closeadj):
    """Compression-Expansion Index: tanh of (ATR(5)/ATR(40) - 1) + tanh of (vol(10) z-score
    vs 60d). Sum gives signed compression(-)/expansion(+) magnitude in (-2, 2)."""
    a5 = _tr(high, low, closeadj).ewm(alpha=1.0 / 5.0, adjust=False, min_periods=5).mean()
    a40 = _tr(high, low, closeadj).ewm(alpha=1.0 / 40.0, adjust=False, min_periods=40).mean()
    t1 = np.tanh(a5 / a40.replace(0.0, np.nan) - 1.0)
    v = closeadj.pct_change().rolling(10, min_periods=10).std(ddof=0)
    mu = v.rolling(60, min_periods=30).mean()
    sd = v.rolling(60, min_periods=30).std(ddof=0)
    z = (v - mu) / sd.replace(0.0, np.nan)
    t2 = np.tanh(z)
    return (t1 + t2).replace([np.inf, -np.inf], np.nan)


# === Days since 60d vol low ================================================


def f20ce_f20_volatility_compression_expansion_days_since_60d_vol_min_v125_signal(closeadj):
    """Bars since vol(20) hit its 60d rolling minimum. Time since deepest compression."""
    v = closeadj.pct_change().rolling(20, min_periods=20).std(ddof=0)
    mn = v.rolling(60, min_periods=30).min()
    at_min = (v <= mn + 1e-12).astype(float).where(~mn.isna())
    out = pd.Series(np.nan, index=closeadj.index, dtype=float)
    cnt = np.nan
    for i in range(len(at_min)):
        x = at_min.iat[i]
        if not np.isfinite(x):
            out.iat[i] = cnt
            continue
        if x > 0.5:
            cnt = 0.0
        elif np.isfinite(cnt):
            cnt += 1.0
        out.iat[i] = cnt
    return out.clip(upper=60.0).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_days_since_60d_vol_max_v126_signal(closeadj):
    """Bars since vol(20) hit its 60d rolling maximum. Time since peak expansion."""
    v = closeadj.pct_change().rolling(20, min_periods=20).std(ddof=0)
    mx = v.rolling(60, min_periods=30).max()
    at_max = (v >= mx - 1e-12).astype(float).where(~mx.isna())
    out = pd.Series(np.nan, index=closeadj.index, dtype=float)
    cnt = np.nan
    for i in range(len(at_max)):
        x = at_max.iat[i]
        if not np.isfinite(x):
            out.iat[i] = cnt
            continue
        if x > 0.5:
            cnt = 0.0
        elif np.isfinite(cnt):
            cnt += 1.0
        out.iat[i] = cnt
    return out.clip(upper=60.0).replace([np.inf, -np.inf], np.nan)


# === Compression/expansion entry/exit transitions =========================


def f20ce_f20_volatility_compression_expansion_entries_to_compression_v127_signal(closeadj):
    """Count over 90d of bars where compression flag (vol < 25th pctile of 100d)
    transitioned from False to True. Compression-entry events."""
    v = closeadj.pct_change().rolling(10, min_periods=10).std(ddof=0)
    q = v.rolling(100, min_periods=50).quantile(0.25)
    flag = (v < q).astype(float).where(~q.isna())
    entries = ((flag > 0.5) & (flag.shift(1) < 0.5)).astype(float).where(~flag.shift(1).isna())
    return entries.rolling(90, min_periods=45).sum().replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_exits_from_compression_v128_signal(closeadj):
    """Count over 90d of bars where compression flag went True->False. Compression-exit."""
    v = closeadj.pct_change().rolling(10, min_periods=10).std(ddof=0)
    q = v.rolling(100, min_periods=50).quantile(0.25)
    flag = (v < q).astype(float).where(~q.isna())
    exits = ((flag < 0.5) & (flag.shift(1) > 0.5)).astype(float).where(~flag.shift(1).isna())
    return exits.rolling(90, min_periods=45).sum().replace([np.inf, -np.inf], np.nan)


# === Body-to-range ratio (compression of directional move) ================


def f20ce_f20_volatility_compression_expansion_body_to_range_30d_v129_signal(open_, high, low, closeadj):
    """SMA(|close - open| / (high - low), 30). High = decisive bars (expansion);
    low = indecisive bars (compression)."""
    rng = (high - low).replace(0.0, np.nan)
    body = (closeadj - open_).abs() / rng
    return body.rolling(30, min_periods=15).mean().replace([np.inf, -np.inf], np.nan)


# === Wick share (compression of true directional move) ====================


def f20ce_f20_volatility_compression_expansion_wick_share_50d_v130_signal(open_, high, low, closeadj):
    """SMA( (range - |close - open|) / range, 50). High = wicks dominate (vol with
    no direction, expansion indecisive)."""
    rng = (high - low).replace(0.0, np.nan)
    wick = (rng - (closeadj - open_).abs()) / rng
    return wick.rolling(50, min_periods=25).mean().replace([np.inf, -np.inf], np.nan)


# === Vol bands ratio: (long-vol band) / (short-vol band) ===================


def f20ce_f20_volatility_compression_expansion_vol_band_ratio_long_short_v131_signal(closeadj):
    """vol(40) / vol(10) - 1. Sign indicates which horizon is more vol-expanded."""
    vs = closeadj.pct_change().rolling(10, min_periods=10).std(ddof=0)
    vl = closeadj.pct_change().rolling(40, min_periods=40).std(ddof=0)
    return (vl / vs.replace(0.0, np.nan) - 1.0).replace([np.inf, -np.inf], np.nan)


# === Sum of squared log returns (RV proxy) compression =====================


def f20ce_f20_volatility_compression_expansion_log_range_sma_diff_v132_signal(high, low):
    """log( SMA(log(high/low), 25) / SMA(log(high/low), 100) ). Log-range compression
    expressed as log-ratio of short to long-window log-range averages."""
    lr = np.log(high / low.replace(0.0, np.nan))
    s = lr.rolling(25, min_periods=25).mean()
    L = lr.rolling(100, min_periods=50).mean()
    return np.log(s / L.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Decline ratio of vol over horizon =====================================


def f20ce_f20_volatility_compression_expansion_vol_pct_decline_30d_v133_signal(closeadj):
    """(vol(20).shift(30) - vol(20)) / vol(20).shift(30). Positive = 30d compression."""
    v = closeadj.pct_change().rolling(20, min_periods=20).std(ddof=0)
    return ((v.shift(30) - v) / v.shift(30).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Vol convexity (range distortion of price returns) ====================


def f20ce_f20_volatility_compression_expansion_realized_vol_min_v134_signal(closeadj):
    """Rolling min of vol(20) over 100d normalized by current vol(20). 1 = at floor."""
    v = closeadj.pct_change().rolling(20, min_periods=20).std(ddof=0)
    mn = v.rolling(100, min_periods=50).min()
    return (mn / v.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f20ce_f20_volatility_compression_expansion_realized_vol_max_v135_signal(closeadj):
    """Rolling max of vol(20) over 100d normalized by current vol(20). >1 = below ceiling."""
    v = closeadj.pct_change().rolling(20, min_periods=20).std(ddof=0)
    mx = v.rolling(100, min_periods=50).max()
    return (mx / v.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Range expansion-of-expansion =========================================


def f20ce_f20_volatility_compression_expansion_range_acceleration_v136_signal(high, low):
    """((high-low) - (high-low).shift(5)) - ((high-low).shift(5) - (high-low).shift(10)).
    2nd derivative of range, identifying accelerating expansion."""
    rng = high - low
    return ((rng - rng.shift(5)) - (rng.shift(5) - rng.shift(10))).replace([np.inf, -np.inf], np.nan)


# === Vol second-derivative sign ===========================================


def f20ce_f20_volatility_compression_expansion_vol_2deriv_sign_30d_v137_signal(closeadj):
    """sign(vol(15) - 2*vol(15).shift(10) + vol(15).shift(20)). Discrete curvature sign."""
    v = closeadj.pct_change().rolling(15, min_periods=15).std(ddof=0)
    return np.sign(v - 2.0 * v.shift(10) + v.shift(20)).replace([np.inf, -np.inf], np.nan)


# === Sum of (sign-changes in return) per window (mean-reversion at high freq) ==


def f20ce_f20_volatility_compression_expansion_signflip_count_30d_v138_signal(closeadj):
    """Count of return sign flips in trailing 30d. High = choppy/reverting expansion
    vs low = trending compression."""
    s = np.sign(closeadj.pct_change())
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(30, min_periods=15).sum().replace([np.inf, -np.inf], np.nan)


# === Vol delta over consistent direction (trending compression) ============


def f20ce_f20_volatility_compression_expansion_vol_change_consistent_v139_signal(closeadj):
    """SMA(sign(vol.diff(5)), 30). Persistent positive => sustained expansion;
    persistent negative => sustained compression."""
    v = closeadj.pct_change().rolling(15, min_periods=15).std(ddof=0)
    s = np.sign(v.diff(5))
    return s.rolling(30, min_periods=15).mean().replace([np.inf, -np.inf], np.nan)


# === Range correlation with prior range ====================================


def f20ce_f20_volatility_compression_expansion_range_corr_lag5_60d_v140_signal(high, low):
    """corr(range, range.shift(5)) over 60d. High = persistent regime."""
    rng = high - low
    return rng.rolling(60, min_periods=30).corr(rng.shift(5)).replace([np.inf, -np.inf], np.nan)


# === Smoothness of recent vol (low entropy => stable compression) =========


def f20ce_f20_volatility_compression_expansion_vol_smoothness_30d_v141_signal(closeadj):
    """std(vol(10).diff(1)) / mean(vol(10)) over 30d. Low = smooth (compression
    plateau); high = jagged (transitions)."""
    v = closeadj.pct_change().rolling(10, min_periods=10).std(ddof=0)
    d = v.diff(1)
    return (d.rolling(30, min_periods=15).std(ddof=0) / v.rolling(30, min_periods=15).mean().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Combined OHLC dispersion ==============================================


def f20ce_f20_volatility_compression_expansion_ohlc_dispersion_zscore_v142_signal(open_, high, low, closeadj):
    """Z-score of std([open, high, low, close]) / close over 100d. Within-bar
    dispersion expressed as a continuous z-score rather than rank."""
    disp = pd.concat([open_, high, low, closeadj], axis=1).std(axis=1) / closeadj.replace(0.0, np.nan)
    mu = disp.rolling(100, min_periods=50).mean()
    sd = disp.rolling(100, min_periods=50).std(ddof=0)
    return ((disp - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Vol regime stability index ============================================


def f20ce_f20_volatility_compression_expansion_regime_stability_v143_signal(closeadj):
    """1 - (transitions over 60d / 60). High = stable regime, low = many transitions.
    Uses (vol > 50th pctile) flag from 60d window."""
    v = closeadj.pct_change().rolling(20, min_periods=20).std(ddof=0)
    med = v.rolling(60, min_periods=30).median()
    flag = (v > med).astype(float).where(~med.isna())
    flips = (flag != flag.shift(1)).astype(float).where(~flag.shift(1).isna() & ~flag.isna())
    return (1.0 - flips.rolling(60, min_periods=30).sum() / 60.0).replace([np.inf, -np.inf], np.nan)


# === Vol percentile gap (short vs long horizon ranks) =====================


def f20ce_f20_volatility_compression_expansion_vol_rank_gap_v144_signal(closeadj):
    """rank(vol(10) in 60d) - rank(vol(40) in 120d). >0 = short-horizon vol elevated
    relative to long-horizon."""
    v10 = closeadj.pct_change().rolling(10, min_periods=10).std(ddof=0)
    v40 = closeadj.pct_change().rolling(40, min_periods=40).std(ddof=0)
    r10 = v10.rolling(60, min_periods=30).apply(
        lambda x: float((x < x[-1]).sum()) / float(len(x) - 1) if len(x) > 1 else np.nan,
        raw=True,
    )
    r40 = v40.rolling(120, min_periods=60).apply(
        lambda x: float((x < x[-1]).sum()) / float(len(x) - 1) if len(x) > 1 else np.nan,
        raw=True,
    )
    return (r10 - r40).replace([np.inf, -np.inf], np.nan)


# === Range above a percentile threshold (sustained expansion) =============


def f20ce_f20_volatility_compression_expansion_range_above_p80_30d_v145_signal(high, low):
    """Fraction of last 30 bars where range > 80th percentile of trailing 120d range."""
    rng = high - low
    q = rng.rolling(120, min_periods=60).quantile(0.80)
    flag = (rng > q).astype(float).where(~q.isna())
    return flag.rolling(30, min_periods=15).mean().replace([np.inf, -np.inf], np.nan)


# === Range slope over short vs long horizon ===============================


def f20ce_f20_volatility_compression_expansion_range_slope_gap_v146_signal(high, low):
    """SMA(range,10).diff(10) - SMA(range,40).diff(10). Differential of short and long
    range slopes — detects diverging vol horizons."""
    rng = high - low
    s10 = rng.rolling(10, min_periods=10).mean()
    s40 = rng.rolling(40, min_periods=40).mean()
    return (s10.diff(10) - s40.diff(10)).replace([np.inf, -np.inf], np.nan)


# === Bollinger Width rate-of-change z-score ===============================


def f20ce_f20_volatility_compression_expansion_bbw_roc_zscore_v147_signal(closeadj):
    """Z-score (60d) of BBW(20) 5d ROC. Positive z = abnormally fast expansion."""
    n = 20
    m = closeadj.rolling(n, min_periods=n).mean()
    sd = closeadj.rolling(n, min_periods=n).std(ddof=0)
    bbw = (4.0 * sd) / m.replace(0.0, np.nan)
    roc = bbw / bbw.shift(5).replace(0.0, np.nan) - 1.0
    mu = roc.rolling(60, min_periods=30).mean()
    sigma = roc.rolling(60, min_periods=30).std(ddof=0)
    return ((roc - mu) / sigma.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Sequential vol differentials (cross-window vol gap dynamics) =========


def f20ce_f20_volatility_compression_expansion_volgap_5_60_change_v148_signal(closeadj):
    """(vol(5)/vol(60) - 1) - its own 30d-mean. Detrended short/long vol gap.
    Positive = unusually high short-term vol vs long-term."""
    vs = closeadj.pct_change().rolling(5, min_periods=5).std(ddof=0)
    vl = closeadj.pct_change().rolling(60, min_periods=60).std(ddof=0)
    gap = vs / vl.replace(0.0, np.nan) - 1.0
    mu = gap.rolling(30, min_periods=15).mean()
    return (gap - mu).replace([np.inf, -np.inf], np.nan)


# === Vol curvature normalized by long-run vol =============================


def f20ce_f20_volatility_compression_expansion_vol_curv_normalized_v149_signal(closeadj):
    """(vol(20) - 2*vol(20).shift(10) + vol(20).shift(20)) / vol(20).shift(10).
    Normalized curvature."""
    v = closeadj.pct_change().rolling(20, min_periods=20).std(ddof=0)
    curv = v - 2.0 * v.shift(10) + v.shift(20)
    return (curv / v.shift(10).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Composite compression score (weighted average of three normalized signals) ==


def f20ce_f20_volatility_compression_expansion_composite_squeeze_v150_signal(high, low, closeadj):
    """Composite squeeze = arctan( -(ATR(5)/ATR(40) - 1) ) + arctan( -(BBW(20)/SMA(BBW,60) - 1) )
    + arctan( -(vol(10) zscore vs 60d) ). Positive = compressed."""
    a5 = _tr(high, low, closeadj).ewm(alpha=1.0 / 5.0, adjust=False, min_periods=5).mean()
    a40 = _tr(high, low, closeadj).ewm(alpha=1.0 / 40.0, adjust=False, min_periods=40).mean()
    t1 = np.arctan(-(a5 / a40.replace(0.0, np.nan) - 1.0))
    n = 20
    m = closeadj.rolling(n, min_periods=n).mean()
    sd = closeadj.rolling(n, min_periods=n).std(ddof=0)
    bbw = (4.0 * sd) / m.replace(0.0, np.nan)
    bbw_avg = bbw.rolling(60, min_periods=30).mean()
    t2 = np.arctan(-(bbw / bbw_avg.replace(0.0, np.nan) - 1.0))
    v = closeadj.pct_change().rolling(10, min_periods=10).std(ddof=0)
    mu = v.rolling(60, min_periods=30).mean()
    sigma = v.rolling(60, min_periods=30).std(ddof=0)
    z = (v - mu) / sigma.replace(0.0, np.nan)
    t3 = np.arctan(-z)
    return (t1 + t2 + t3).replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f20_volatility_compression_expansion_base_076_150_REGISTRY = {
    "f20ce_f20_volatility_compression_expansion_kc_width_div_close_20d_base_v076_signal": {"inputs": ["high", "low", "close"], "func": f20ce_f20_volatility_compression_expansion_kc_width_div_close_20d_base_v076_signal},
    "f20ce_f20_volatility_compression_expansion_kc_width_rank_120d_base_v077_signal": {"inputs": ["high", "low", "closeadj"], "func": f20ce_f20_volatility_compression_expansion_kc_width_rank_120d_base_v077_signal},
    "f20ce_f20_volatility_compression_expansion_kc_vs_bbw_v078_signal": {"inputs": ["high", "low", "closeadj"], "func": f20ce_f20_volatility_compression_expansion_kc_vs_bbw_v078_signal},
    "f20ce_f20_volatility_compression_expansion_sqret_short_long_30_120_v079_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_sqret_short_long_30_120_v079_signal},
    "f20ce_f20_volatility_compression_expansion_sqret_zscore_60d_v080_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_sqret_zscore_60d_v080_signal},
    "f20ce_f20_volatility_compression_expansion_sqret_decline_streak_20d_v081_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_sqret_decline_streak_20d_v081_signal},
    "f20ce_f20_volatility_compression_expansion_log_hl_sq_rank_60d_v082_signal": {"inputs": ["high", "low"], "func": f20ce_f20_volatility_compression_expansion_log_hl_sq_rank_60d_v082_signal},
    "f20ce_f20_volatility_compression_expansion_log_co_sq_short_long_v083_signal": {"inputs": ["open", "closeadj"], "func": f20ce_f20_volatility_compression_expansion_log_co_sq_short_long_v083_signal},
    "f20ce_f20_volatility_compression_expansion_close_vs_kc_upper_norm_v084_signal": {"inputs": ["high", "low", "closeadj"], "func": f20ce_f20_volatility_compression_expansion_close_vs_kc_upper_norm_v084_signal},
    "f20ce_f20_volatility_compression_expansion_close_outside_kc_count_30d_v085_signal": {"inputs": ["high", "low", "closeadj"], "func": f20ce_f20_volatility_compression_expansion_close_outside_kc_count_30d_v085_signal},
    "f20ce_f20_volatility_compression_expansion_volofrange_30d_v086_signal": {"inputs": ["high", "low"], "func": f20ce_f20_volatility_compression_expansion_volofrange_30d_v086_signal},
    "f20ce_f20_volatility_compression_expansion_volofrange_zscore_v087_signal": {"inputs": ["high", "low", "closeadj"], "func": f20ce_f20_volatility_compression_expansion_volofrange_zscore_v087_signal},
    "f20ce_f20_volatility_compression_expansion_tr_vs_hl_ratio_20d_v088_signal": {"inputs": ["high", "low", "close"], "func": f20ce_f20_volatility_compression_expansion_tr_vs_hl_ratio_20d_v088_signal},
    "f20ce_f20_volatility_compression_expansion_gap_jump_count_60d_v089_signal": {"inputs": ["high", "low", "closeadj"], "func": f20ce_f20_volatility_compression_expansion_gap_jump_count_60d_v089_signal},
    "f20ce_f20_volatility_compression_expansion_vol_regslope_40d_v090_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_vol_regslope_40d_v090_signal},
    "f20ce_f20_volatility_compression_expansion_atr_regslope_80d_v091_signal": {"inputs": ["high", "low", "closeadj"], "func": f20ce_f20_volatility_compression_expansion_atr_regslope_80d_v091_signal},
    "f20ce_f20_volatility_compression_expansion_bbw_zdist_to_min_v092_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_bbw_zdist_to_min_v092_signal},
    "f20ce_f20_volatility_compression_expansion_atr_dist_to_max_60d_v093_signal": {"inputs": ["high", "low", "closeadj"], "func": f20ce_f20_volatility_compression_expansion_atr_dist_to_max_60d_v093_signal},
    "f20ce_f20_volatility_compression_expansion_vol_long_horizon_ratio_v094_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_vol_long_horizon_ratio_v094_signal},
    "f20ce_f20_volatility_compression_expansion_med_range_rank_80d_v095_signal": {"inputs": ["high", "low"], "func": f20ce_f20_volatility_compression_expansion_med_range_rank_80d_v095_signal},
    "f20ce_f20_volatility_compression_expansion_p10_range_rel_p90_v096_signal": {"inputs": ["high", "low"], "func": f20ce_f20_volatility_compression_expansion_p10_range_rel_p90_v096_signal},
    "f20ce_f20_volatility_compression_expansion_small_range_cluster_10d_v097_signal": {"inputs": ["high", "low"], "func": f20ce_f20_volatility_compression_expansion_small_range_cluster_10d_v097_signal},
    "f20ce_f20_volatility_compression_expansion_large_range_cluster_10d_v098_signal": {"inputs": ["high", "low"], "func": f20ce_f20_volatility_compression_expansion_large_range_cluster_10d_v098_signal},
    "f20ce_f20_volatility_compression_expansion_up_down_vol_ratio_30d_v099_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_up_down_vol_ratio_30d_v099_signal},
    "f20ce_f20_volatility_compression_expansion_up_minus_down_vol_z_v100_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_up_minus_down_vol_z_v100_signal},
    "f20ce_f20_volatility_compression_expansion_gap_abs_30d_avg_v101_signal": {"inputs": ["open", "closeadj"], "func": f20ce_f20_volatility_compression_expansion_gap_abs_30d_avg_v101_signal},
    "f20ce_f20_volatility_compression_expansion_gap_zscore_60d_v102_signal": {"inputs": ["open", "closeadj"], "func": f20ce_f20_volatility_compression_expansion_gap_zscore_60d_v102_signal},
    "f20ce_f20_volatility_compression_expansion_frac_below_p25_vol_60d_v103_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_frac_below_p25_vol_60d_v103_signal},
    "f20ce_f20_volatility_compression_expansion_frac_above_p75_vol_60d_v104_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_frac_above_p75_vol_60d_v104_signal},
    "f20ce_f20_volatility_compression_expansion_vol_mom_sign_short_long_v105_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_vol_mom_sign_short_long_v105_signal},
    "f20ce_f20_volatility_compression_expansion_range_pctile_cross_event_v106_signal": {"inputs": ["high", "low"], "func": f20ce_f20_volatility_compression_expansion_range_pctile_cross_event_v106_signal},
    "f20ce_f20_volatility_compression_expansion_recent_vol_concentration_v107_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_recent_vol_concentration_v107_signal},
    "f20ce_f20_volatility_compression_expansion_tailshare_60d_v108_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_tailshare_60d_v108_signal},
    "f20ce_f20_volatility_compression_expansion_vol_dist_from_252d_mean_v109_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_vol_dist_from_252d_mean_v109_signal},
    "f20ce_f20_volatility_compression_expansion_vol_drawdown_60d_v110_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_vol_drawdown_60d_v110_signal},
    "f20ce_f20_volatility_compression_expansion_vol_runup_60d_v111_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_vol_runup_60d_v111_signal},
    "f20ce_f20_volatility_compression_expansion_3bar_contraction_v112_signal": {"inputs": ["high", "low"], "func": f20ce_f20_volatility_compression_expansion_3bar_contraction_v112_signal},
    "f20ce_f20_volatility_compression_expansion_3bar_expansion_v113_signal": {"inputs": ["high", "low"], "func": f20ce_f20_volatility_compression_expansion_3bar_expansion_v113_signal},
    "f20ce_f20_volatility_compression_expansion_pricecurv_vol_30d_v114_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_pricecurv_vol_30d_v114_signal},
    "f20ce_f20_volatility_compression_expansion_compression_breadth_v115_signal": {"inputs": ["high", "low", "closeadj"], "func": f20ce_f20_volatility_compression_expansion_compression_breadth_v115_signal},
    "f20ce_f20_volatility_compression_expansion_compress_streak_rank_v116_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_compress_streak_rank_v116_signal},
    "f20ce_f20_volatility_compression_expansion_vol_dir_reversals_60d_v117_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_vol_dir_reversals_60d_v117_signal},
    "f20ce_f20_volatility_compression_expansion_vol_ar1_residual_v118_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_vol_ar1_residual_v118_signal},
    "f20ce_f20_volatility_compression_expansion_absret_persistence_60d_v119_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_absret_persistence_60d_v119_signal},
    "f20ce_f20_volatility_compression_expansion_vol_skew_80d_v120_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_vol_skew_80d_v120_signal},
    "f20ce_f20_volatility_compression_expansion_vw_volatility_ratio_v121_signal": {"inputs": ["closeadj", "volume"], "func": f20ce_f20_volatility_compression_expansion_vw_volatility_ratio_v121_signal},
    "f20ce_f20_volatility_compression_expansion_range_entropy_50d_v122_signal": {"inputs": ["high", "low"], "func": f20ce_f20_volatility_compression_expansion_range_entropy_50d_v122_signal},
    "f20ce_f20_volatility_compression_expansion_pctb_extreme_freq_30d_v123_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_pctb_extreme_freq_30d_v123_signal},
    "f20ce_f20_volatility_compression_expansion_cei_composite_v124_signal": {"inputs": ["high", "low", "closeadj"], "func": f20ce_f20_volatility_compression_expansion_cei_composite_v124_signal},
    "f20ce_f20_volatility_compression_expansion_days_since_60d_vol_min_v125_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_days_since_60d_vol_min_v125_signal},
    "f20ce_f20_volatility_compression_expansion_days_since_60d_vol_max_v126_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_days_since_60d_vol_max_v126_signal},
    "f20ce_f20_volatility_compression_expansion_entries_to_compression_v127_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_entries_to_compression_v127_signal},
    "f20ce_f20_volatility_compression_expansion_exits_from_compression_v128_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_exits_from_compression_v128_signal},
    "f20ce_f20_volatility_compression_expansion_body_to_range_30d_v129_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f20ce_f20_volatility_compression_expansion_body_to_range_30d_v129_signal},
    "f20ce_f20_volatility_compression_expansion_wick_share_50d_v130_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f20ce_f20_volatility_compression_expansion_wick_share_50d_v130_signal},
    "f20ce_f20_volatility_compression_expansion_vol_band_ratio_long_short_v131_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_vol_band_ratio_long_short_v131_signal},
    "f20ce_f20_volatility_compression_expansion_log_range_sma_diff_v132_signal": {"inputs": ["high", "low"], "func": f20ce_f20_volatility_compression_expansion_log_range_sma_diff_v132_signal},
    "f20ce_f20_volatility_compression_expansion_vol_pct_decline_30d_v133_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_vol_pct_decline_30d_v133_signal},
    "f20ce_f20_volatility_compression_expansion_realized_vol_min_v134_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_realized_vol_min_v134_signal},
    "f20ce_f20_volatility_compression_expansion_realized_vol_max_v135_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_realized_vol_max_v135_signal},
    "f20ce_f20_volatility_compression_expansion_range_acceleration_v136_signal": {"inputs": ["high", "low"], "func": f20ce_f20_volatility_compression_expansion_range_acceleration_v136_signal},
    "f20ce_f20_volatility_compression_expansion_vol_2deriv_sign_30d_v137_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_vol_2deriv_sign_30d_v137_signal},
    "f20ce_f20_volatility_compression_expansion_signflip_count_30d_v138_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_signflip_count_30d_v138_signal},
    "f20ce_f20_volatility_compression_expansion_vol_change_consistent_v139_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_vol_change_consistent_v139_signal},
    "f20ce_f20_volatility_compression_expansion_range_corr_lag5_60d_v140_signal": {"inputs": ["high", "low"], "func": f20ce_f20_volatility_compression_expansion_range_corr_lag5_60d_v140_signal},
    "f20ce_f20_volatility_compression_expansion_vol_smoothness_30d_v141_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_vol_smoothness_30d_v141_signal},
    "f20ce_f20_volatility_compression_expansion_ohlc_dispersion_zscore_v142_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f20ce_f20_volatility_compression_expansion_ohlc_dispersion_zscore_v142_signal},
    "f20ce_f20_volatility_compression_expansion_regime_stability_v143_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_regime_stability_v143_signal},
    "f20ce_f20_volatility_compression_expansion_vol_rank_gap_v144_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_vol_rank_gap_v144_signal},
    "f20ce_f20_volatility_compression_expansion_range_above_p80_30d_v145_signal": {"inputs": ["high", "low"], "func": f20ce_f20_volatility_compression_expansion_range_above_p80_30d_v145_signal},
    "f20ce_f20_volatility_compression_expansion_range_slope_gap_v146_signal": {"inputs": ["high", "low"], "func": f20ce_f20_volatility_compression_expansion_range_slope_gap_v146_signal},
    "f20ce_f20_volatility_compression_expansion_bbw_roc_zscore_v147_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_bbw_roc_zscore_v147_signal},
    "f20ce_f20_volatility_compression_expansion_volgap_5_60_change_v148_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_volgap_5_60_change_v148_signal},
    "f20ce_f20_volatility_compression_expansion_vol_curv_normalized_v149_signal": {"inputs": ["closeadj"], "func": f20ce_f20_volatility_compression_expansion_vol_curv_normalized_v149_signal},
    "f20ce_f20_volatility_compression_expansion_composite_squeeze_v150_signal": {"inputs": ["high", "low", "closeadj"], "func": f20ce_f20_volatility_compression_expansion_composite_squeeze_v150_signal},
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
    for name, entry in f20_volatility_compression_expansion_base_076_150_REGISTRY.items():
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
