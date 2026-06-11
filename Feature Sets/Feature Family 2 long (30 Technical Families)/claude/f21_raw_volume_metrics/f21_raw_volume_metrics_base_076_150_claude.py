"""f21_raw_volume_metrics base features 076-150.

Domain: RAW VOLUME METRICS — features built directly from the volume series
and dollar-volume aggregates. Distinct from f22/f23/f24/f25/f26/f27/f28.
Stays focused on RAW STATISTICS of the volume series. Dollar volume uses
closeadj*volume when the window > 21 trading days per the guide rule.

These features are structurally distinct from base_001_075 (no shared
expression up to a window change). NaN policy: never fillna(<value>);
only replace([inf,-inf], nan) at the final return. Each function spells
its formula inline.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _sma(s: pd.Series, n: int) -> pd.Series:
    return s.rolling(n, min_periods=n).mean()


def _ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False, min_periods=n).mean()


def _mad(x):
    return float(np.mean(np.abs(x - np.mean(x))))


def _streak_last_true(x):
    idx = np.where(x > 0.5)[0]
    if idx.size == 0:
        return float(len(x))
    return float(len(x) - 1 - idx[-1])


def _consec_true(x):
    c = 0
    for v in x[::-1]:
        if v > 0.5:
            c += 1
        else:
            break
    return float(c)


def _hurst_rs(x):
    n = len(x)
    if n < 16 or not np.all(np.isfinite(x)):
        return np.nan
    y = np.asarray(x, dtype=float)
    mean = y.mean()
    dev = y - mean
    z = np.cumsum(dev)
    R = z.max() - z.min()
    S = y.std(ddof=0)
    if S == 0.0 or not np.isfinite(R / S) or R / S <= 0.0:
        return np.nan
    return float(np.log(R / S) / np.log(n))


# ---------------------------------------------------------------------------
# Features 076-150
# ---------------------------------------------------------------------------


# === Volume "drawdown" / gain class ========================================




def f21rv_f21_raw_volume_metrics_vol_gain_from_min_60d_base_v077_signal(volume):
    """log(volume / rolling-60d min(volume)). Volume's log gain above recent trough."""
    mn = volume.rolling(60, min_periods=60).min()
    return np.log(volume / mn.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_vol_dd_from_max_200d_base_v078_signal(volume):
    """log(volume / 200d max). Long-horizon volume drawdown."""
    mx = volume.rolling(200, min_periods=200).max()
    return np.log(volume / mx.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Volume Hurst exponent =================================================


def f21rv_f21_raw_volume_metrics_logvol_hurst_60d_base_v079_signal(volume):
    """Hurst R/S exponent of log(volume) over 60 bars. Persistence/anti-persistence
    of volume regimes; close to 0.5 = random walk, > 0.5 = trending."""
    lv = np.log(volume.replace(0.0, np.nan))
    return lv.rolling(60, min_periods=60).apply(_hurst_rs, raw=True).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_logvol_hurst_180d_base_v080_signal(volume):
    """Hurst R/S exponent of log(volume) over 180 bars."""
    lv = np.log(volume.replace(0.0, np.nan))
    return lv.rolling(180, min_periods=180).apply(_hurst_rs, raw=True).replace([np.inf, -np.inf], np.nan)


# === Volume Fisher transform ===============================================


def f21rv_f21_raw_volume_metrics_vol_fisher_50d_base_v081_signal(volume):
    """Fisher transform of rescaled volume rank: 0.5*log((1+r)/(1-r)) where
    r is 2*rank(vol, 50) - 1 clipped to (-0.999,0.999). Heavy-tailed bounded form."""
    r = 2.0 * volume.rolling(50, min_periods=50).rank(pct=True) - 1.0
    r = r.clip(-0.999, 0.999)
    return (0.5 * np.log((1.0 + r) / (1.0 - r))).replace([np.inf, -np.inf], np.nan)


# === Volume Bollinger %B (own bands) =======================================


def f21rv_f21_raw_volume_metrics_vol_pctB_30d_base_v082_signal(volume):
    """%B of volume vs SMA(30)+/-2*std(30) bands. Where the current vol sits
    in its own dynamic band; clipped softly in [0,1] usually."""
    n = 30
    m = _sma(volume, n)
    sd = volume.rolling(n, min_periods=n).std()
    up = m + 2.0 * sd; lo = m - 2.0 * sd
    return ((volume - lo) / (up - lo).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_vol_bandwidth_90d_base_v083_signal(volume):
    """4*std(vol,90) / SMA(vol,90). Bollinger bandwidth on volume — width-only."""
    n = 90
    m = _sma(volume, n)
    sd = volume.rolling(n, min_periods=n).std()
    return (4.0 * sd / m.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Distance from quantile ================================================


def f21rv_f21_raw_volume_metrics_vol_streak_above_med_120d_base_v084_signal(volume):
    """Longest consecutive-bar streak of (vol > rolling-120 median) within a trailing
    120-bar window. Discrete count of regime persistence — structurally distinct
    from log-distance/level features (integer streak vs continuous level)."""
    med = volume.rolling(120, min_periods=120).median()
    above = (volume > med).astype(float).where(~med.isna())
    def _longest(x):
        if len(x) == 0 or not np.all(np.isfinite(x)):
            return np.nan
        best = 0; cur = 0
        for v in x:
            if v > 0.5:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)
    return above.rolling(120, min_periods=120).apply(_longest, raw=True).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_vol_peak_count_120d_base_v085_signal(volume):
    """Number of local-maximum bars (vol[i] > vol[i-1] and vol[i] > vol[i+1]) in a
    trailing 120-bar window divided by 120. Count-of-peaks density — structurally
    distinct from level-distance features (count rather than magnitude)."""
    a = volume.shift(1); b = volume.shift(-1)
    peak = ((volume > a) & (volume > b)).astype(float).where(~a.isna() & ~b.isna())
    return (peak.rolling(120, min_periods=120).sum() / 120.0).replace([np.inf, -np.inf], np.nan)


# === Volume oscillator (own-cross variant) =================================


def f21rv_f21_raw_volume_metrics_vol_osc_ema5_sma20_base_v086_signal(volume):
    """(EMA(vol,5) - SMA(vol,20)) / SMA(vol,20). Klinger-style volume oscillator
    spread, normalized. Different from f22 (volume-trend MA slopes class)."""
    e = _ema(volume, 5); s = _sma(volume, 20)
    return ((e - s) / s.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_vol_osc_sma10_sma40_base_v087_signal(volume):
    """(SMA(vol,10) - SMA(vol,40)) / SMA(vol,40). Classic Chaikin-style volume osc."""
    a = _sma(volume, 10); b = _sma(volume, 40)
    return ((a - b) / b.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === MFI-style applied to volume itself (signed volume RSI variant) ========


def f21rv_f21_raw_volume_metrics_vol_mfi_14d_base_v088_signal(close, volume):
    """RSI on signed volume: classify each bar's volume as positive/negative
    by sign(close.diff). Sum 14-bar positive vs negative, build RSI-style 0..100.
    Distinct from v061 (RSI on raw volume series)."""
    s = np.sign(close.diff(1))
    pos = (volume * (s > 0).astype(float)).rolling(14, min_periods=14).sum()
    neg = (volume * (s < 0).astype(float)).rolling(14, min_periods=14).sum()
    rs = pos / neg.replace(0.0, np.nan)
    return (100.0 - 100.0 / (1.0 + rs)).replace([np.inf, -np.inf], np.nan)


# === Cumulative vol ranks ==================================================


def f21rv_f21_raw_volume_metrics_vol_rank_quartile_252d_base_v089_signal(volume):
    """Discrete quartile bucket {0..3} of volume vs trailing 252-bar quantiles."""
    q25 = volume.rolling(252, min_periods=252).quantile(0.25)
    q50 = volume.rolling(252, min_periods=252).quantile(0.50)
    q75 = volume.rolling(252, min_periods=252).quantile(0.75)
    b = (volume > q25).astype(float) + (volume > q50).astype(float) + (volume > q75).astype(float)
    return b.where(~q25.isna()).replace([np.inf, -np.inf], np.nan)


# === Two-volume-MA divergence (volume only) ================================


def f21rv_f21_raw_volume_metrics_vol_med_ratio_15_90_base_v090_signal(volume):
    """log(median(vol,15) / median(vol,90)). Robust short-vs-mid volume regime
    differential using medians. Distinct from EMA/SMA log ratios (median-based,
    different short-window 15 vs 5/20 already used) and distinct from v005 (20/120)."""
    a = volume.rolling(15, min_periods=15).median()
    b = volume.rolling(90, min_periods=90).median()
    return np.log(a / b.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_vol_macd_signal_25_75_base_v091_signal(volume):
    """[EMA(vol,25) - EMA(vol,75)] - EMA of that, 35 — MACD histogram on volume."""
    m = _ema(volume, 25) - _ema(volume, 75)
    sig = m.ewm(span=35, adjust=False, min_periods=35).mean()
    return ((m - sig) / _sma(volume, 252).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Dollar-volume specific structural features ============================


def f21rv_f21_raw_volume_metrics_dv_gini_60d_base_v092_signal(closeadj, volume):
    """Gini coefficient of dollar volume in trailing 60 bars. Concentration of dv."""
    dv = closeadj * volume
    def _gini(x):
        if np.any(x < 0.0) or len(x) < 2 or not np.all(np.isfinite(x)):
            return np.nan
        y = np.sort(x); n = len(y); s = y.sum()
        if s == 0.0:
            return np.nan
        cumy = np.cumsum(y)
        return float((n + 1.0 - 2.0 * cumy.sum() / s) / n)
    return dv.rolling(60, min_periods=60).apply(_gini, raw=True).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_dv_pctchg_std_60d_base_v093_signal(closeadj, volume):
    """Std of dollar-volume.pct_change(1) over 60 bars."""
    dv = closeadj * volume
    pc = dv.pct_change(1)
    return pc.rolling(60, min_periods=60).std().replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_dv_extreme_count_60d_base_v094_signal(closeadj, volume):
    """Count of bars in trailing 60 where dollar-volume > 2*SMA(dv,60).
    Dollar-volume spike count — distinct from raw-vol spike count."""
    dv = closeadj * volume
    m = _sma(dv, 60)
    spike = (dv > 2.0 * m).astype(float).where(~m.isna())
    return spike.rolling(60, min_periods=60).sum().replace([np.inf, -np.inf], np.nan)


# === Volume reversion features (mean-reverting score) ======================


def f21rv_f21_raw_volume_metrics_vol_reversion_score_30d_base_v095_signal(volume):
    """Number of times volume crosses its SMA(10) within 30 bars (volatility-of-mean
    crossings — distinct from up/down streaks)."""
    m = _sma(volume, 10)
    s = np.sign(volume - m)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(30, min_periods=30).sum().replace([np.inf, -np.inf], np.nan)


# === Bars-since features at varied targets =================================


def f21rv_f21_raw_volume_metrics_dayssince_q75_cross_120d_base_v096_signal(volume):
    """Bars since last vol-above-Q75(120) cross, capped 120."""
    q = volume.rolling(120, min_periods=120).quantile(0.75)
    hi = (volume > q).astype(float).where(~q.isna())
    return hi.rolling(120, min_periods=120).apply(_streak_last_true, raw=True).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_dayssince_dry_120d_base_v097_signal(volume):
    """Bars since last dry day (vol < 0.5*SMA21), capped 120."""
    m = _sma(volume, 21)
    dry = (volume < 0.5 * m).astype(float).where(~m.isna())
    return dry.rolling(120, min_periods=120).apply(_streak_last_true, raw=True).replace([np.inf, -np.inf], np.nan)


# === Median-based normalizations at different window combos ================


def f21rv_f21_raw_volume_metrics_vol_med_ratio_5_50_base_v098_signal(volume):
    """log(median(vol,5) / median(vol,50)). Robust short-vs-long volume regime."""
    a = volume.rolling(5, min_periods=5).median()
    b = volume.rolling(50, min_periods=50).median()
    return np.log(a / b.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_vol_med_diff_q_20d_base_v099_signal(volume):
    """median(vol,20) - Q25(vol,20) relative to (Q75-Q25). Median's position in IQR.
    Bounded structural shape indicator."""
    med = volume.rolling(20, min_periods=20).median()
    q25 = volume.rolling(20, min_periods=20).quantile(0.25)
    q75 = volume.rolling(20, min_periods=20).quantile(0.75)
    return ((med - q25) / (q75 - q25).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === High-frequency vs low-frequency vol diff ==============================


def f21rv_f21_raw_volume_metrics_vol_hf_lf_diff_base_v100_signal(volume):
    """SMA(vol, 3) - SMA(vol, 100), normalized by SMA(vol,100). Microstructure
    excess vol vs ambient. Different window pair than v002/v003/v004."""
    a = _sma(volume, 3); b = _sma(volume, 100)
    return ((a - b) / b.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Tail measures =========================================================


def f21rv_f21_raw_volume_metrics_vol_uppertail_share_45d_base_v101_signal(volume):
    """sum(vol[vol>Q75]) / sum(vol) over 45 bars. Share of volume contributed by
    upper-quartile-volume days."""
    def _us(x):
        if len(x) < 5 or not np.all(np.isfinite(x)):
            return np.nan
        q = np.quantile(x, 0.75)
        s = x.sum()
        if s == 0.0:
            return np.nan
        return float(x[x > q].sum() / s)
    return volume.rolling(45, min_periods=45).apply(_us, raw=True).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_vol_lowertail_share_45d_base_v102_signal(volume):
    """sum(vol[vol<Q25]) / sum(vol) over 45 bars. Share of volume from
    lower-quartile-volume days."""
    def _ls(x):
        if len(x) < 5 or not np.all(np.isfinite(x)):
            return np.nan
        q = np.quantile(x, 0.25)
        s = x.sum()
        if s == 0.0:
            return np.nan
        return float(x[x < q].sum() / s)
    return volume.rolling(45, min_periods=45).apply(_ls, raw=True).replace([np.inf, -np.inf], np.nan)


# === Higher-order moments on volume changes ================================


def f21rv_f21_raw_volume_metrics_logvol_diff_skew_60d_base_v103_signal(volume):
    """Skew of log(volume).diff(1) over 60 bars. Asymmetry of log volume changes."""
    return np.log(volume.replace(0.0, np.nan)).diff(1).rolling(60, min_periods=60).skew().replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_logvol_diff_kurt_90d_base_v104_signal(volume):
    """Kurt of log(volume).diff(1) over 90 bars. Tail intensity of log changes."""
    return np.log(volume.replace(0.0, np.nan)).diff(1).rolling(90, min_periods=90).kurt().replace([np.inf, -np.inf], np.nan)


# === Cross-window vol-vol correlation ======================================


def f21rv_f21_raw_volume_metrics_vol_corr_with_lag10_60d_base_v105_signal(volume):
    """Rolling correlation of volume with volume.shift(10) over 60 bars.
    Distinct from acf_lag1 — much longer lag captures different memory scale."""
    a = volume; b = volume.shift(10)
    return a.rolling(60, min_periods=60).corr(b).replace([np.inf, -np.inf], np.nan)


# === EMA-based volume z ====================================================


def f21rv_f21_raw_volume_metrics_vol_kl_halves_60d_base_v106_signal(volume):
    """Symmetric KL divergence between the empirical 8-bin histograms of the
    earlier and later halves of a trailing 60-bar window of log(volume).
    Distributional regime-change measure — structurally distinct from level-distance
    or z-score features (compares two histograms within the same window)."""
    lv = np.log(volume.replace(0.0, np.nan))
    def _kl(x):
        if len(x) < 20 or not np.all(np.isfinite(x)):
            return np.nan
        half = len(x) // 2
        a = x[:half]; b = x[half:]
        lo = float(min(a.min(), b.min())); hi = float(max(a.max(), b.max()))
        if hi <= lo:
            return np.nan
        edges = np.linspace(lo, hi, 9)
        ha, _ = np.histogram(a, bins=edges)
        hb, _ = np.histogram(b, bins=edges)
        eps = 1e-6
        pa = (ha + eps) / (ha.sum() + 8.0 * eps)
        pb = (hb + eps) / (hb.sum() + 8.0 * eps)
        return float(np.sum(pa * np.log(pa / pb)) + np.sum(pb * np.log(pb / pa)))
    return lv.rolling(60, min_periods=60).apply(_kl, raw=True).replace([np.inf, -np.inf], np.nan)


# === Volume "doji" / unchanged days =======================================


def f21rv_f21_raw_volume_metrics_vol_near_unchanged_30d_base_v107_signal(volume):
    """Fraction of bars in 30 where |log(vol/vol.shift)| < 0.05.
    Frequency of near-unchanged volume — distinct shape from pct_change std."""
    flag = (np.log(volume / volume.shift(1)).abs() < 0.05).astype(float).where(~volume.shift(1).isna())
    return flag.rolling(30, min_periods=30).mean().replace([np.inf, -np.inf], np.nan)


# === Volume "expansion" ratio (vol now vs vol earlier) =====================


def f21rv_f21_raw_volume_metrics_vol_expansion_5_to_30_base_v108_signal(volume):
    """sum(vol, 5) / sum(vol[5:30]). Recent 5d total relative to preceding 25d total."""
    a = volume.rolling(5, min_periods=5).sum()
    b = (volume.shift(5)).rolling(25, min_periods=25).sum()
    return (a / b.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Volume cumulative profile percentile =================================


def f21rv_f21_raw_volume_metrics_vol_q_skew_60d_base_v109_signal(volume):
    """Quantile-based skewness of volume in 60-bar window:
    ((Q75 - Q50) - (Q50 - Q25)) / (Q75 - Q25). Bowley skew — bounded [-1,1] and
    structurally distinct from level/rank percentile features."""
    n = 60
    q25 = volume.rolling(n, min_periods=n).quantile(0.25)
    q50 = volume.rolling(n, min_periods=n).quantile(0.50)
    q75 = volume.rolling(n, min_periods=n).quantile(0.75)
    num = (q75 - q50) - (q50 - q25)
    den = (q75 - q25).replace(0.0, np.nan)
    return (num / den).replace([np.inf, -np.inf], np.nan)


# === Signed volume diversifiers ===========================================


def f21rv_f21_raw_volume_metrics_signed_vol_zscore_30d_base_v110_signal(close, volume):
    """z-score of (sign(dC) * volume) over 30 bars. Standardized signed volume."""
    s = np.sign(close.diff(1))
    sv = s * volume
    m = _sma(sv, 30); sd = sv.rolling(30, min_periods=30).std()
    return ((sv - m) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_signed_vol_skew_60d_base_v111_signal(close, volume):
    """Skew of signed volume over 60 bars."""
    s = np.sign(close.diff(1))
    sv = s * volume
    return sv.rolling(60, min_periods=60).skew().replace([np.inf, -np.inf], np.nan)


# === Volume drawdown duration ==============================================


def f21rv_f21_raw_volume_metrics_vol_dd_dur_50d_base_v112_signal(volume):
    """Bars since the most recent 50-bar rolling-max of volume was set."""
    def _ago(x):
        if len(x) == 0 or not np.all(np.isfinite(x)):
            return np.nan
        return float(len(x) - 1 - int(np.argmax(x)))
    return volume.rolling(50, min_periods=50).apply(_ago, raw=True).replace([np.inf, -np.inf], np.nan)


# === Volume entropy at longer horizon =====================================


def f21rv_f21_raw_volume_metrics_vol_entropy_100d_base_v113_signal(volume):
    """Shannon entropy of volume distribution within 100-bar window (10 bins)."""
    def _ent(x):
        if len(x) < 5 or not np.all(np.isfinite(x)) or np.all(x == x[0]):
            return np.nan
        h, _ = np.histogram(x, bins=10)
        p = h / h.sum()
        p = p[p > 0.0]
        return float(-np.sum(p * np.log(p)))
    return volume.rolling(100, min_periods=100).apply(_ent, raw=True).replace([np.inf, -np.inf], np.nan)


# === Volume "compression" =================================================


def f21rv_f21_raw_volume_metrics_vol_compression_45d_base_v114_signal(volume):
    """std(vol,45) / std(vol,180). Short-vs-long vol-of-volume ratio. Compression
    indicator — high when recent vol is squeezed compared to long-horizon."""
    a = volume.rolling(45, min_periods=45).std()
    b = volume.rolling(180, min_periods=180).std()
    return (a / b.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Number of contiguous spike clusters ==================================


def f21rv_f21_raw_volume_metrics_vol_spike_cluster_50d_base_v115_signal(volume):
    """Number of distinct spike clusters (vol > 1.5*SMA21) in 50 bars (count of
    rising edges of the spike-flag series)."""
    m = _sma(volume, 21)
    spike = (volume > 1.5 * m).astype(float).where(~m.isna())
    rise = ((spike > 0.5) & (spike.shift(1) < 0.5)).astype(float).where(~spike.isna() & ~spike.shift(1).isna())
    return rise.rolling(50, min_periods=50).sum().replace([np.inf, -np.inf], np.nan)


# === Volume "regression coefficient" between two halves ===================


def f21rv_f21_raw_volume_metrics_vol_halfreg_60d_base_v116_signal(volume):
    """Difference between mean of last 30 bars and mean of preceding 30 bars,
    normalized by combined std. Discrete "halves" t-statistic style."""
    a = volume.rolling(30, min_periods=30).mean()
    b = volume.shift(30).rolling(30, min_periods=30).mean()
    sd = volume.rolling(60, min_periods=60).std()
    return ((a - b) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Volume "rank of std" =================================================


def f21rv_f21_raw_volume_metrics_vol_std_rank_120d_base_v117_signal(volume):
    """Percentile rank of std(vol, 20) within trailing 120 of its own values."""
    s = volume.rolling(20, min_periods=20).std()
    return s.rolling(120, min_periods=120).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# === Volume "Gaussian-like" diagnostics ===================================


def f21rv_f21_raw_volume_metrics_vol_jb_50d_base_v118_signal(volume):
    """Jarque-Bera-like statistic on log volume: n/6 * (skew^2 + (kurt-3)^2/4) / 50.
    Distance-from-normal diagnostic over 50 bars."""
    lv = np.log(volume.replace(0.0, np.nan))
    sk = lv.rolling(50, min_periods=50).skew()
    ku = lv.rolling(50, min_periods=50).kurt()
    return ((sk ** 2 + (ku) ** 2 / 4.0)).replace([np.inf, -np.inf], np.nan)


# === Volume "ROC" (vs trailing N average not start) =======================




def f21rv_f21_raw_volume_metrics_vol_roc_today_vs_25d_ago_base_v120_signal(volume):
    """log(volume / volume.shift(25)). 25-day volume ROC."""
    return np.log(volume / volume.shift(25)).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_vol_roc_today_vs_100d_ago_base_v121_signal(volume):
    """log(volume / volume.shift(100)). 100-day volume ROC."""
    return np.log(volume / volume.shift(100)).replace([np.inf, -np.inf], np.nan)


# === Rolling kurtosis of log dollar-volume changes ========================


def f21rv_f21_raw_volume_metrics_dv_pctchg_skew_60d_base_v122_signal(closeadj, volume):
    """Skew of (closeadj*volume).pct_change(1) over 60 bars."""
    dv = closeadj * volume
    return dv.pct_change(1).rolling(60, min_periods=60).skew().replace([np.inf, -np.inf], np.nan)


# === Volume "drawdown depth" max over window ==============================


def f21rv_f21_raw_volume_metrics_vol_dd_max_depth_60d_base_v123_signal(volume):
    """Most negative log(vol / running max) within the trailing 60 bars."""
    mx = volume.rolling(60, min_periods=60).max()
    dd = np.log(volume / mx.replace(0.0, np.nan))
    return dd.rolling(60, min_periods=60).min().replace([np.inf, -np.inf], np.nan)


# === Skew of dollar volume distribution ===================================


def f21rv_f21_raw_volume_metrics_logdv_skew_90d_base_v124_signal(closeadj, volume):
    """Skew of log(dollar volume) over 90 bars."""
    ldv = np.log((closeadj * volume).replace(0.0, np.nan))
    return ldv.rolling(90, min_periods=90).skew().replace([np.inf, -np.inf], np.nan)


# === Volume "EMA distance" ratios =========================================


def f21rv_f21_raw_volume_metrics_vol_ema30_ema90_log_base_v125_signal(volume):
    """log(EMA(vol,30) / EMA(vol,90)). Mid-vs-long EMA volume regime differential."""
    return np.log(_ema(volume, 30) / _ema(volume, 90)).replace([np.inf, -np.inf], np.nan)


# === Volume Bollinger-position normalized for tails =======================


def f21rv_f21_raw_volume_metrics_vol_com_50d_base_v126_signal(volume):
    """Triangular center-of-mass of volume within a trailing 50-bar window:
    sum(i*vol_i) / sum(vol_i) for i in [0..49], normalized to [0,1].
    Recent-vs-distant volume weighting. Structurally distinct from
    z/level/distance features (weighted-time first moment, not a level)."""
    n = 50
    def _com(x):
        if len(x) == 0 or not np.all(np.isfinite(x)) or np.any(x < 0.0):
            return np.nan
        s = x.sum()
        if s == 0.0:
            return np.nan
        t = np.arange(len(x), dtype=float)
        return float(np.sum(t * x) / s / max(1.0, len(x) - 1.0))
    return volume.rolling(n, min_periods=n).apply(_com, raw=True).replace([np.inf, -np.inf], np.nan)


# === Long-horizon volume z =================================================


def f21rv_f21_raw_volume_metrics_logvol_detrended_std_180d_base_v127_signal(volume):
    """Standard deviation of OLS-detrended log(volume) over a 180-bar window.
    Captures dispersion AFTER removing linear trend, structurally distinct from
    raw z-score (no current-vs-mean direction) and from level-distance features."""
    lv = np.log(volume.replace(0.0, np.nan))
    n = 180
    def _detr_std(x):
        if len(x) < 30 or not np.all(np.isfinite(x)):
            return np.nan
        t = np.arange(len(x), dtype=float)
        mt = t.mean(); mx = x.mean()
        cov = np.sum((t - mt) * (x - mx))
        var = np.sum((t - mt) ** 2)
        if var == 0.0:
            return np.nan
        slope = cov / var
        intercept = mx - slope * mt
        resid = x - (slope * t + intercept)
        return float(resid.std())
    return lv.rolling(n, min_periods=n).apply(_detr_std, raw=True).replace([np.inf, -np.inf], np.nan)


# === Volume "average true range" analog ===================================


def f21rv_f21_raw_volume_metrics_vol_atr_like_30d_base_v128_signal(volume):
    """SMA(|vol - vol.shift(1)|, 30) / SMA(vol, 30). Volume "ATR" — average absolute
    change normalized by level. Structural distinct from std-based vol vol."""
    chg = volume.diff(1).abs()
    return (_sma(chg, 30) / _sma(volume, 30).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Volume signed-momentum streak ========================================


def f21rv_f21_raw_volume_metrics_vol_signed_streak_40d_base_v129_signal(volume):
    """Consecutive bars of same-sign volume.diff (positive OR negative), capped 40."""
    s = np.sign(volume.diff(1))
    def _ss(x):
        if len(x) == 0:
            return np.nan
        last = x[-1]
        if last == 0.0:
            return 0.0
        c = 0
        for v in x[::-1]:
            if v == last:
                c += 1
            else:
                break
        return float(c) * float(np.sign(last))
    return s.rolling(40, min_periods=40).apply(_ss, raw=True).replace([np.inf, -np.inf], np.nan)


# === Volume "intensity" — relative volume vs short median + spike count ===


def f21rv_f21_raw_volume_metrics_vol_intensity_index_40d_base_v130_signal(volume):
    """sum(vol/median(vol,20)) over 40 bars / 40. Average relative volume intensity.
    Distinct from spike-count: continuous, not threshold-binary."""
    med = volume.rolling(20, min_periods=20).median()
    rel = volume / med.replace(0.0, np.nan)
    return rel.rolling(40, min_periods=40).mean().replace([np.inf, -np.inf], np.nan)


# === Volume "tail asymmetry" (top vs bottom decile means ratio) ===========


def f21rv_f21_raw_volume_metrics_vol_tail_asym_120d_base_v131_signal(volume):
    """log(mean(top-10% vol days) / mean(bottom-10% vol days)) in 120 bars."""
    def _ta(x):
        if len(x) < 20 or not np.all(np.isfinite(x)):
            return np.nan
        y = np.sort(x)
        k = max(1, int(0.1 * len(y)))
        top = y[-k:].mean(); bot = y[:k].mean()
        if bot == 0.0 or top == 0.0:
            return np.nan
        return float(np.log(top / bot))
    return volume.rolling(120, min_periods=120).apply(_ta, raw=True).replace([np.inf, -np.inf], np.nan)


# === Signed dollar-volume z (long horizon, closeadj rule) =================


def f21rv_f21_raw_volume_metrics_signed_dv_flip_rate_60d_base_v132_signal(close, closeadj, volume):
    """Mean of (sign(signed_dv) != sign(signed_dv.shift(1))) over a 60-bar window,
    where signed_dv = sign(close.diff)*closeadj*volume. Frequency of direction
    reversal in signed dollar volume — bounded [0,1] structural rate measure,
    distinct from z-scores (no centring/scaling, no level)."""
    s = np.sign(close.diff(1))
    sdv = s * closeadj * volume
    ssign = np.sign(sdv)
    flip = (ssign != ssign.shift(1)).astype(float).where(~ssign.isna() & ~ssign.shift(1).isna())
    return flip.rolling(60, min_periods=60).mean().replace([np.inf, -np.inf], np.nan)


# === Volume periodicity (log-vol DFT-style amplitude ratio of 2 lags) =====


def f21rv_f21_raw_volume_metrics_vol_dft_short_long_60d_base_v133_signal(volume):
    """Ratio of |Fourier coeff at period 5| to |Fourier coeff at period 30| over
    60-bar window of log vol. Captures short-cycle vs long-cycle energy."""
    lv = np.log(volume.replace(0.0, np.nan))
    def _df(x):
        if not np.all(np.isfinite(x)) or len(x) < 30:
            return np.nan
        x0 = x - x.mean()
        n = len(x0)
        k_short = max(1, int(round(n / 5.0)))
        k_long = max(1, int(round(n / 30.0)))
        if k_short >= n or k_long >= n or k_short == k_long:
            return np.nan
        fft = np.fft.rfft(x0)
        a = float(np.abs(fft[k_short])); b = float(np.abs(fft[k_long]))
        if b == 0.0:
            return np.nan
        return float(a / b)
    return lv.rolling(60, min_periods=60).apply(_df, raw=True).replace([np.inf, -np.inf], np.nan)


# === Volume "Theil index" =================================================


def f21rv_f21_raw_volume_metrics_vol_theil_45d_base_v134_signal(volume):
    """Theil entropy index of volume over 45 bars: sum((x/mean)*log(x/mean)) / n.
    Alternative inequality measure to Gini."""
    def _theil(x):
        if len(x) < 5 or not np.all(np.isfinite(x)) or np.any(x <= 0.0):
            return np.nan
        m = x.mean()
        if m == 0.0:
            return np.nan
        r = x / m
        return float(np.sum(r * np.log(r)) / len(x))
    return volume.rolling(45, min_periods=45).apply(_theil, raw=True).replace([np.inf, -np.inf], np.nan)


# === Volume "second peak ratio" ============================================


def f21rv_f21_raw_volume_metrics_vol_second_peak_60d_base_v135_signal(volume):
    """log(second-largest vol in 60 / max vol in 60). How far the second peak is
    from the highest — concentration tail indicator."""
    def _sp(x):
        if len(x) < 5 or not np.all(np.isfinite(x)):
            return np.nan
        y = np.sort(x)[::-1]
        if y[0] == 0.0:
            return np.nan
        return float(np.log(y[1] / y[0]))
    return volume.rolling(60, min_periods=60).apply(_sp, raw=True).replace([np.inf, -np.inf], np.nan)


# === Volume daily-change Sharpe ===========================================


def f21rv_f21_raw_volume_metrics_vol_change_sharpe_60d_base_v136_signal(volume):
    """mean(volume.diff(1)) / std(volume.diff(1)) over 60 bars. Sharpe of changes."""
    d = volume.diff(1)
    return (_sma(d, 60) / d.rolling(60, min_periods=60).std().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Above/below median count ratio (asymmetry of distribution) ===========


def f21rv_f21_raw_volume_metrics_vol_med_asym_80d_base_v137_signal(volume):
    """(count(vol>median) - count(vol<median)) / 80 in trailing 80 bars."""
    med = volume.rolling(80, min_periods=80).median()
    over = (volume > med).astype(float).where(~med.isna())
    under = (volume < med).astype(float).where(~med.isna())
    return ((over.rolling(80, min_periods=80).sum() - under.rolling(80, min_periods=80).sum()) / 80.0).replace([np.inf, -np.inf], np.nan)


# === Volume "consecutive above SMA20" ratio ===============================


def f21rv_f21_raw_volume_metrics_vol_persistence_40d_base_v138_signal(volume):
    """Mean of (1 if (vol-SMA20) has same sign as (vol-SMA20).shift(1)) in 40 bars.
    Persistence rate of above/below-typical regime."""
    d = volume - _sma(volume, 20)
    same = (np.sign(d) == np.sign(d.shift(1))).astype(float).where(~d.isna() & ~d.shift(1).isna())
    return same.rolling(40, min_periods=40).mean().replace([np.inf, -np.inf], np.nan)


# === Dollar volume Z at different long-horizon window =====================


def f21rv_f21_raw_volume_metrics_dv_max_gap_top10_252d_base_v139_signal(closeadj, volume):
    """Max gap (in bars) between consecutive top-10% dollar-volume days within a
    trailing 252-bar window. Captures temporal clustering of large dv days —
    structurally distinct from z-scores or level distances (gap-statistic on
    rank-1 dv days). Uses closeadj (>21d rule)."""
    dv = closeadj * volume
    def _gap(x):
        if len(x) < 20 or not np.all(np.isfinite(x)):
            return np.nan
        thr = np.quantile(x, 0.90)
        hits = np.where(x >= thr)[0]
        if hits.size < 2:
            return float(len(x))
        gaps = np.diff(hits)
        return float(gaps.max())
    return dv.rolling(252, min_periods=252).apply(_gap, raw=True).replace([np.inf, -np.inf], np.nan)


# === Volume "winsor mean" vs raw mean differential =========================


def f21rv_f21_raw_volume_metrics_vol_winsor_diff_60d_base_v140_signal(volume):
    """log(WinsorMean(vol,60,10%) / SMA(vol,60)). Robust-vs-raw mean differential
    on volume — quantifies how much tail mass distorts mean."""
    n = 60
    def _wm(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        lo = np.quantile(x, 0.10); hi = np.quantile(x, 0.90)
        return float(np.mean(np.clip(x, lo, hi)))
    w = volume.rolling(n, min_periods=n).apply(_wm, raw=True)
    return np.log(w / _sma(volume, n).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Trimmed mean of volume vs raw mean ===================================


def f21rv_f21_raw_volume_metrics_vol_trimmed_diff_80d_base_v141_signal(volume):
    """log(TrimmedMean(vol,80,10%) / SMA(vol,80)). Trimmed-vs-raw mean differential."""
    n = 80
    def _tm(x):
        if not np.all(np.isfinite(x)) or len(x) < 5:
            return np.nan
        k = int(np.floor(0.1 * len(x)))
        if k * 2 >= len(x):
            return np.nan
        y = np.sort(x)
        return float(np.mean(y[k:len(y) - k]))
    t = volume.rolling(n, min_periods=n).apply(_tm, raw=True)
    return np.log(t / _sma(volume, n).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Volume "lull index" — count of days within 0.5x to 1.5x of mean =====


def f21rv_f21_raw_volume_metrics_vol_lull_count_60d_base_v142_signal(volume):
    """Count of bars in trailing 60 where 0.5*SMA21 < vol < 1.5*SMA21.
    Number of "ordinary-volume" days — distinct from spike/dry binaries."""
    m = _sma(volume, 21)
    lull = ((volume > 0.5 * m) & (volume < 1.5 * m)).astype(float).where(~m.isna())
    return lull.rolling(60, min_periods=60).sum().replace([np.inf, -np.inf], np.nan)


# === Argmin of volume in long window ======================================


def f21rv_f21_raw_volume_metrics_vol_argmin_120d_base_v143_signal(volume):
    """Bars since trailing 120-bar volume MIN, normalized to [0,1]."""
    def _ax(x):
        if len(x) == 0 or not np.all(np.isfinite(x)):
            return np.nan
        return float((len(x) - 1 - int(np.argmin(x))) / max(1, len(x) - 1))
    return volume.rolling(120, min_periods=120).apply(_ax, raw=True).replace([np.inf, -np.inf], np.nan)


# === Volume "spike intensity index" - rolling spike-mag avg ===============


def f21rv_f21_raw_volume_metrics_vol_spike_intensity_45d_base_v144_signal(volume):
    """Average of (volume/SMA21) on spike days within 45 bars. Avg spike magnitude."""
    m = _sma(volume, 21)
    rel = volume / m.replace(0.0, np.nan)
    spike = (rel > 2.0).astype(float).where(~m.isna())
    rel_on_spike = rel.where(spike > 0.5)
    return rel_on_spike.rolling(45, min_periods=1).mean().replace([np.inf, -np.inf], np.nan)


# === Volume "max bar growth" within window ================================


def f21rv_f21_raw_volume_metrics_vol_max_1d_growth_40d_base_v145_signal(volume):
    """Max log(volume / volume.shift(1)) over 40 bars. Largest single-bar
    volume growth — extreme jump indicator."""
    return np.log(volume / volume.shift(1)).rolling(40, min_periods=40).max().replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_vol_min_1d_growth_40d_base_v146_signal(volume):
    """Min log(volume / volume.shift(1)) over 40 bars. Largest single-bar
    volume drop."""
    return np.log(volume / volume.shift(1)).rolling(40, min_periods=40).min().replace([np.inf, -np.inf], np.nan)


# === Volume "doji-vol" ratio — small change but high level ================


def f21rv_f21_raw_volume_metrics_vol_dispersion_lag_60d_base_v147_signal(volume):
    """std(vol, 60) / std(vol.shift(20), 60). Compares current vs 20-bar-ago vol
    volatility. Captures whether vol-of-vol is rising or falling."""
    a = volume.rolling(60, min_periods=60).std()
    b = volume.shift(20).rolling(60, min_periods=60).std()
    return (a / b.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Volume "Sharpe" using log vol ratio ==================================


def f21rv_f21_raw_volume_metrics_logvol_diff_signaling_70d_base_v148_signal(volume):
    """Mean of log(vol).diff over 70 / std of log(vol).diff. t-stat for vol drift."""
    d = np.log(volume.replace(0.0, np.nan)).diff(1)
    return (_sma(d, 70) / d.rolling(70, min_periods=70).std().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Volume "rank of MAD" ==================================================


def f21rv_f21_raw_volume_metrics_vol_mad_rank_120d_base_v149_signal(volume):
    """Percentile rank of MAD(vol,30) within trailing 120 of its own values.
    Where is current volume's robust scale relative to recent regime."""
    mad = volume.rolling(30, min_periods=30).apply(_mad, raw=True)
    return mad.rolling(120, min_periods=120).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# === Geometric mean of volume vs arithmetic ===============================


def f21rv_f21_raw_volume_metrics_vol_geom_arith_diff_60d_base_v150_signal(volume):
    """log(geometric_mean(vol,60) / arith_mean(vol,60)). Always <= 0 by AM-GM;
    measures distribution dispersion (more negative = more dispersed)."""
    lv = np.log(volume.replace(0.0, np.nan))
    geo = np.exp(lv.rolling(60, min_periods=60).mean())
    ari = _sma(volume, 60)
    return np.log(geo / ari.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f21_raw_volume_metrics_base_076_150_REGISTRY = {
    "f21rv_f21_raw_volume_metrics_vol_gain_from_min_60d_base_v077_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_gain_from_min_60d_base_v077_signal},
    "f21rv_f21_raw_volume_metrics_vol_dd_from_max_200d_base_v078_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_dd_from_max_200d_base_v078_signal},
    "f21rv_f21_raw_volume_metrics_logvol_hurst_60d_base_v079_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_logvol_hurst_60d_base_v079_signal},
    "f21rv_f21_raw_volume_metrics_logvol_hurst_180d_base_v080_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_logvol_hurst_180d_base_v080_signal},
    "f21rv_f21_raw_volume_metrics_vol_fisher_50d_base_v081_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_fisher_50d_base_v081_signal},
    "f21rv_f21_raw_volume_metrics_vol_pctB_30d_base_v082_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_pctB_30d_base_v082_signal},
    "f21rv_f21_raw_volume_metrics_vol_bandwidth_90d_base_v083_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_bandwidth_90d_base_v083_signal},
    "f21rv_f21_raw_volume_metrics_vol_streak_above_med_120d_base_v084_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_streak_above_med_120d_base_v084_signal},
    "f21rv_f21_raw_volume_metrics_vol_peak_count_120d_base_v085_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_peak_count_120d_base_v085_signal},
    "f21rv_f21_raw_volume_metrics_vol_osc_ema5_sma20_base_v086_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_osc_ema5_sma20_base_v086_signal},
    "f21rv_f21_raw_volume_metrics_vol_osc_sma10_sma40_base_v087_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_osc_sma10_sma40_base_v087_signal},
    "f21rv_f21_raw_volume_metrics_vol_mfi_14d_base_v088_signal": {"inputs": ["close", "volume"], "func": f21rv_f21_raw_volume_metrics_vol_mfi_14d_base_v088_signal},
    "f21rv_f21_raw_volume_metrics_vol_rank_quartile_252d_base_v089_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_rank_quartile_252d_base_v089_signal},
    "f21rv_f21_raw_volume_metrics_vol_med_ratio_15_90_base_v090_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_med_ratio_15_90_base_v090_signal},
    "f21rv_f21_raw_volume_metrics_vol_macd_signal_25_75_base_v091_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_macd_signal_25_75_base_v091_signal},
    "f21rv_f21_raw_volume_metrics_dv_gini_60d_base_v092_signal": {"inputs": ["closeadj", "volume"], "func": f21rv_f21_raw_volume_metrics_dv_gini_60d_base_v092_signal},
    "f21rv_f21_raw_volume_metrics_dv_pctchg_std_60d_base_v093_signal": {"inputs": ["closeadj", "volume"], "func": f21rv_f21_raw_volume_metrics_dv_pctchg_std_60d_base_v093_signal},
    "f21rv_f21_raw_volume_metrics_dv_extreme_count_60d_base_v094_signal": {"inputs": ["closeadj", "volume"], "func": f21rv_f21_raw_volume_metrics_dv_extreme_count_60d_base_v094_signal},
    "f21rv_f21_raw_volume_metrics_vol_reversion_score_30d_base_v095_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_reversion_score_30d_base_v095_signal},
    "f21rv_f21_raw_volume_metrics_dayssince_q75_cross_120d_base_v096_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_dayssince_q75_cross_120d_base_v096_signal},
    "f21rv_f21_raw_volume_metrics_dayssince_dry_120d_base_v097_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_dayssince_dry_120d_base_v097_signal},
    "f21rv_f21_raw_volume_metrics_vol_med_ratio_5_50_base_v098_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_med_ratio_5_50_base_v098_signal},
    "f21rv_f21_raw_volume_metrics_vol_med_diff_q_20d_base_v099_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_med_diff_q_20d_base_v099_signal},
    "f21rv_f21_raw_volume_metrics_vol_hf_lf_diff_base_v100_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_hf_lf_diff_base_v100_signal},
    "f21rv_f21_raw_volume_metrics_vol_uppertail_share_45d_base_v101_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_uppertail_share_45d_base_v101_signal},
    "f21rv_f21_raw_volume_metrics_vol_lowertail_share_45d_base_v102_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_lowertail_share_45d_base_v102_signal},
    "f21rv_f21_raw_volume_metrics_logvol_diff_skew_60d_base_v103_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_logvol_diff_skew_60d_base_v103_signal},
    "f21rv_f21_raw_volume_metrics_logvol_diff_kurt_90d_base_v104_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_logvol_diff_kurt_90d_base_v104_signal},
    "f21rv_f21_raw_volume_metrics_vol_corr_with_lag10_60d_base_v105_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_corr_with_lag10_60d_base_v105_signal},
    "f21rv_f21_raw_volume_metrics_vol_kl_halves_60d_base_v106_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_kl_halves_60d_base_v106_signal},
    "f21rv_f21_raw_volume_metrics_vol_near_unchanged_30d_base_v107_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_near_unchanged_30d_base_v107_signal},
    "f21rv_f21_raw_volume_metrics_vol_expansion_5_to_30_base_v108_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_expansion_5_to_30_base_v108_signal},
    "f21rv_f21_raw_volume_metrics_vol_q_skew_60d_base_v109_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_q_skew_60d_base_v109_signal},
    "f21rv_f21_raw_volume_metrics_signed_vol_zscore_30d_base_v110_signal": {"inputs": ["close", "volume"], "func": f21rv_f21_raw_volume_metrics_signed_vol_zscore_30d_base_v110_signal},
    "f21rv_f21_raw_volume_metrics_signed_vol_skew_60d_base_v111_signal": {"inputs": ["close", "volume"], "func": f21rv_f21_raw_volume_metrics_signed_vol_skew_60d_base_v111_signal},
    "f21rv_f21_raw_volume_metrics_vol_dd_dur_50d_base_v112_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_dd_dur_50d_base_v112_signal},
    "f21rv_f21_raw_volume_metrics_vol_entropy_100d_base_v113_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_entropy_100d_base_v113_signal},
    "f21rv_f21_raw_volume_metrics_vol_compression_45d_base_v114_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_compression_45d_base_v114_signal},
    "f21rv_f21_raw_volume_metrics_vol_spike_cluster_50d_base_v115_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_spike_cluster_50d_base_v115_signal},
    "f21rv_f21_raw_volume_metrics_vol_halfreg_60d_base_v116_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_halfreg_60d_base_v116_signal},
    "f21rv_f21_raw_volume_metrics_vol_std_rank_120d_base_v117_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_std_rank_120d_base_v117_signal},
    "f21rv_f21_raw_volume_metrics_vol_jb_50d_base_v118_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_jb_50d_base_v118_signal},
    "f21rv_f21_raw_volume_metrics_vol_roc_today_vs_25d_ago_base_v120_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_roc_today_vs_25d_ago_base_v120_signal},
    "f21rv_f21_raw_volume_metrics_vol_roc_today_vs_100d_ago_base_v121_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_roc_today_vs_100d_ago_base_v121_signal},
    "f21rv_f21_raw_volume_metrics_dv_pctchg_skew_60d_base_v122_signal": {"inputs": ["closeadj", "volume"], "func": f21rv_f21_raw_volume_metrics_dv_pctchg_skew_60d_base_v122_signal},
    "f21rv_f21_raw_volume_metrics_vol_dd_max_depth_60d_base_v123_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_dd_max_depth_60d_base_v123_signal},
    "f21rv_f21_raw_volume_metrics_logdv_skew_90d_base_v124_signal": {"inputs": ["closeadj", "volume"], "func": f21rv_f21_raw_volume_metrics_logdv_skew_90d_base_v124_signal},
    "f21rv_f21_raw_volume_metrics_vol_ema30_ema90_log_base_v125_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_ema30_ema90_log_base_v125_signal},
    "f21rv_f21_raw_volume_metrics_vol_com_50d_base_v126_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_com_50d_base_v126_signal},
    "f21rv_f21_raw_volume_metrics_logvol_detrended_std_180d_base_v127_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_logvol_detrended_std_180d_base_v127_signal},
    "f21rv_f21_raw_volume_metrics_vol_atr_like_30d_base_v128_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_atr_like_30d_base_v128_signal},
    "f21rv_f21_raw_volume_metrics_vol_signed_streak_40d_base_v129_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_signed_streak_40d_base_v129_signal},
    "f21rv_f21_raw_volume_metrics_vol_intensity_index_40d_base_v130_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_intensity_index_40d_base_v130_signal},
    "f21rv_f21_raw_volume_metrics_vol_tail_asym_120d_base_v131_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_tail_asym_120d_base_v131_signal},
    "f21rv_f21_raw_volume_metrics_signed_dv_flip_rate_60d_base_v132_signal": {"inputs": ["close", "closeadj", "volume"], "func": f21rv_f21_raw_volume_metrics_signed_dv_flip_rate_60d_base_v132_signal},
    "f21rv_f21_raw_volume_metrics_vol_dft_short_long_60d_base_v133_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_dft_short_long_60d_base_v133_signal},
    "f21rv_f21_raw_volume_metrics_vol_theil_45d_base_v134_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_theil_45d_base_v134_signal},
    "f21rv_f21_raw_volume_metrics_vol_second_peak_60d_base_v135_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_second_peak_60d_base_v135_signal},
    "f21rv_f21_raw_volume_metrics_vol_change_sharpe_60d_base_v136_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_change_sharpe_60d_base_v136_signal},
    "f21rv_f21_raw_volume_metrics_vol_med_asym_80d_base_v137_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_med_asym_80d_base_v137_signal},
    "f21rv_f21_raw_volume_metrics_vol_persistence_40d_base_v138_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_persistence_40d_base_v138_signal},
    "f21rv_f21_raw_volume_metrics_dv_max_gap_top10_252d_base_v139_signal": {"inputs": ["closeadj", "volume"], "func": f21rv_f21_raw_volume_metrics_dv_max_gap_top10_252d_base_v139_signal},
    "f21rv_f21_raw_volume_metrics_vol_winsor_diff_60d_base_v140_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_winsor_diff_60d_base_v140_signal},
    "f21rv_f21_raw_volume_metrics_vol_trimmed_diff_80d_base_v141_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_trimmed_diff_80d_base_v141_signal},
    "f21rv_f21_raw_volume_metrics_vol_lull_count_60d_base_v142_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_lull_count_60d_base_v142_signal},
    "f21rv_f21_raw_volume_metrics_vol_argmin_120d_base_v143_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_argmin_120d_base_v143_signal},
    "f21rv_f21_raw_volume_metrics_vol_spike_intensity_45d_base_v144_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_spike_intensity_45d_base_v144_signal},
    "f21rv_f21_raw_volume_metrics_vol_max_1d_growth_40d_base_v145_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_max_1d_growth_40d_base_v145_signal},
    "f21rv_f21_raw_volume_metrics_vol_min_1d_growth_40d_base_v146_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_min_1d_growth_40d_base_v146_signal},
    "f21rv_f21_raw_volume_metrics_vol_dispersion_lag_60d_base_v147_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_dispersion_lag_60d_base_v147_signal},
    "f21rv_f21_raw_volume_metrics_logvol_diff_signaling_70d_base_v148_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_logvol_diff_signaling_70d_base_v148_signal},
    "f21rv_f21_raw_volume_metrics_vol_mad_rank_120d_base_v149_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_mad_rank_120d_base_v149_signal},
    "f21rv_f21_raw_volume_metrics_vol_geom_arith_diff_60d_base_v150_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_geom_arith_diff_60d_base_v150_signal},
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
    for name, entry in f21_raw_volume_metrics_base_076_150_REGISTRY.items():
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
