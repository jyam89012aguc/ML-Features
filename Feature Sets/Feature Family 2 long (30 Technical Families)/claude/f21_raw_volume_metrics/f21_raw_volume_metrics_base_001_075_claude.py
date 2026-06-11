"""f21_raw_volume_metrics base features 001-075.

Domain: RAW VOLUME METRICS — features built directly from the volume series
and dollar-volume aggregates. Distinct from f22 (volume-trend MA slopes),
f23 (OBV), f24 (volume-price confirmation), f25 (VWAP), f26 (A/D),
f27 (volume regime), f28 (price-volume divergence). Stays focused on
RAW STATISTICS of the volume series. Dollar volume uses closeadj*volume
when the window > 21 trading days per the guide rule (else close*volume).

NaN policy: never fillna(<value>) inside helpers / rolling computations.
Only `.replace([np.inf, -np.inf], np.nan)` at each function's final return.
Each function spells its formula inline; helpers are utility-only.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Helpers (rolling utilities). Each feature still spells its formula inline.
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


# ---------------------------------------------------------------------------
# Features 001-075
# ---------------------------------------------------------------------------


# === Raw current-vs-trailing log-volume (single representative) ============


def f21rv_f21_raw_volume_metrics_logvol_sma5_base_v001_signal(volume):
    """log(volume / SMA(volume, 5)). Short-horizon log volume excess.
    One representative ratio at the short bracket — wider windows handled by
    structurally different features (slope diffs, ranks, etc.)."""
    return np.log(volume / _sma(volume, 5)).replace([np.inf, -np.inf], np.nan)


# === Volume short-vs-long ratios (DIFFERENCE structure, decorrelates from
# === single-window level-vs-trailing features) ===========================


def f21rv_f21_raw_volume_metrics_logvol_sma5_sma50_base_v002_signal(volume):
    """log(SMA(vol,5) / SMA(vol,50)). Short-vs-mid-volume regime differential.
    Cancels common drift in volume by differencing two MAs."""
    return np.log(_sma(volume, 5) / _sma(volume, 50)).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_logvol_sma20_sma200_base_v003_signal(volume):
    """log(SMA(vol,20) / SMA(vol,200)). Mid-vs-long-volume regime differential."""
    return np.log(_sma(volume, 20) / _sma(volume, 200)).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_logvol_ema_diff_10_60_base_v004_signal(volume):
    """log(EMA(vol,10) / EMA(vol,60)). EMA short-vs-mid volume momentum."""
    return np.log(_ema(volume, 10) / _ema(volume, 60)).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_median_vol_ratio_20_120_base_v005_signal(volume):
    """log(median(vol,20) / median(vol,120)). Robust short-vs-long volume."""
    a = volume.rolling(20, min_periods=20).median()
    b = volume.rolling(120, min_periods=120).median()
    return np.log(a / b.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Volume z-scores (RAW shape) at ONE representative horizon =============


def f21rv_f21_raw_volume_metrics_volz_21d_base_v006_signal(volume):
    """Volume z-score over trailing 21 bars."""
    m = _sma(volume, 21)
    sd = volume.rolling(21, min_periods=21).std()
    return ((volume - m) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Volume percentile rank (one representative) ===========================


def f21rv_f21_raw_volume_metrics_volrank_60d_base_v007_signal(volume):
    """Volume percentile rank in trailing 60 bars."""
    return volume.rolling(60, min_periods=60).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# === Dollar-volume per-bar (just the log) =================================


def f21rv_f21_raw_volume_metrics_dv_signed_share_30d_base_v008_signal(close, closeadj, volume):
    """sum(sign(close.diff) * dv, 30) / sum(dv, 30). Net signed DOLLAR-volume share
    over 30 bars. Dollar-volume analog of signed_vol_share. Window>21 -> closeadj for dv."""
    dv = closeadj * volume
    s = np.sign(close.diff(1))
    num = (s * dv).rolling(30, min_periods=30).sum()
    den = dv.rolling(30, min_periods=30).sum()
    return (num / den.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Dollar-volume term structure (a DIFFERENCE, not a level) =============


def f21rv_f21_raw_volume_metrics_dv_termstruct_5_252_base_v009_signal(closeadj, volume):
    """log(SMA(dv,5) / SMA(dv,252)). Short vs long dollar-volume regime."""
    dv = closeadj * volume
    return np.log(_sma(dv, 5) / _sma(dv, 252)).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_dv_termstruct_20_120_base_v010_signal(closeadj, volume):
    """log(SMA(dv,20) / SMA(dv,120)). Monthly vs 6-month dollar-volume term."""
    dv = closeadj * volume
    return np.log(_sma(dv, 20) / _sma(dv, 120)).replace([np.inf, -np.inf], np.nan)


# === Volume distributional features (skew/kurt/MAD/CV/Gini) ================


def f21rv_f21_raw_volume_metrics_vol_skew_60d_base_v011_signal(volume):
    """Rolling 60d skewness of volume. Right-tail skew indicates spike regime."""
    return volume.rolling(60, min_periods=60).skew().replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_vol_kurt_180d_base_v012_signal(volume):
    """Rolling 180d kurtosis of volume. Long-horizon tail intensity — different
    horizon and shape than 60d skew, decorrelated by window separation."""
    return volume.rolling(180, min_periods=180).kurt().replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_logvol_skew_120d_base_v013_signal(volume):
    """Rolling 120d skewness of log(volume). Removes scale-induced skew."""
    lv = np.log(volume.replace(0.0, np.nan))
    return lv.rolling(120, min_periods=120).skew().replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_logvol_kurt_40d_base_v014_signal(volume):
    """Kurtosis of log(volume) over 40 bars. Log-domain tail concentration."""
    lv = np.log(volume.replace(0.0, np.nan))
    return lv.rolling(40, min_periods=40).kurt().replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_vol_mad_over_std_45d_base_v015_signal(volume):
    """MAD(volume,45) / std(volume,45). Robust-vs-L2 scale ratio of volume."""
    mad = volume.rolling(45, min_periods=45).apply(_mad, raw=True)
    sd = volume.rolling(45, min_periods=45).std()
    return (mad / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_vol_cv_60d_base_v016_signal(volume):
    """Coefficient of variation: std(vol,60) / mean(vol,60). Volume dispersion."""
    m = _sma(volume, 60)
    sd = volume.rolling(60, min_periods=60).std()
    return (sd / m.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_vol_gini_30d_base_v017_signal(volume):
    """Gini coefficient of volume in trailing 30 bars (distribution inequality)."""
    def _gini(x):
        if np.any(x < 0.0) or len(x) < 2:
            return np.nan
        y = np.sort(x); n = len(y); s = y.sum()
        if s == 0.0 or not np.isfinite(s):
            return np.nan
        cumy = np.cumsum(y)
        return float((n + 1.0 - 2.0 * cumy.sum() / s) / n)
    return volume.rolling(30, min_periods=30).apply(_gini, raw=True).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_vol_iqr_over_med_50d_base_v018_signal(volume):
    """(Q75 - Q25) / median(vol,50). Robust-scale of volume distribution."""
    q25 = volume.rolling(50, min_periods=50).quantile(0.25)
    q75 = volume.rolling(50, min_periods=50).quantile(0.75)
    med = volume.rolling(50, min_periods=50).median()
    return ((q75 - q25) / med.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Volume changes (daily) ================================================


def f21rv_f21_raw_volume_metrics_volpct_1d_base_v019_signal(volume):
    """Volume percentage change at 1 lag. Raw daily volume momentum."""
    return volume.pct_change(1).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_logvol_diff_1d_base_v020_signal(volume):
    """log(volume / volume.shift(1)). Symmetric-around-zero volume change."""
    return np.log(volume / volume.shift(1)).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_abs_logvol_diff_10d_base_v021_signal(volume):
    """Mean |log volume change| over 10 bars. Activity magnitude."""
    lvd = np.log(volume / volume.shift(1)).abs()
    return lvd.rolling(10, min_periods=10).mean().replace([np.inf, -np.inf], np.nan)


# === Volume bursts / spikes (binary, count, magnitude, days-since) =========


def f21rv_f21_raw_volume_metrics_spike_bin_21d_base_v022_signal(volume):
    """Binary: volume > 2*SMA(volume, 21). Spike indicator."""
    m = _sma(volume, 21)
    return (volume > 2.0 * m).astype(float).where(~m.isna()).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_spike_count_60d_base_v023_signal(volume):
    """Count of spike days (vol > 2x SMA21) in trailing 60 bars."""
    m = _sma(volume, 21)
    spike = (volume > 2.0 * m).astype(float).where(~m.isna())
    return spike.rolling(60, min_periods=60).sum().replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_spike_mag_60d_base_v024_signal(volume):
    """Max(volume / SMA(volume,21)) over trailing 60 bars. Largest relative spike."""
    m = _sma(volume, 21)
    rel = volume / m.replace(0.0, np.nan)
    return rel.rolling(60, min_periods=60).max().replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_dayssince_spike_80d_base_v025_signal(volume):
    """Bars since last spike day (vol > 2x SMA21), capped 80."""
    m = _sma(volume, 21)
    spike = (volume > 2.0 * m).astype(float).where(~m.isna())
    return spike.rolling(80, min_periods=80).apply(_streak_last_true, raw=True).replace([np.inf, -np.inf], np.nan)


# === Volume "dryness" (low volume) =========================================


def f21rv_f21_raw_volume_metrics_dry_bin_21d_base_v026_signal(volume):
    """Binary: volume < 0.5*SMA(volume, 21). Volume-drought indicator."""
    m = _sma(volume, 21)
    return (volume < 0.5 * m).astype(float).where(~m.isna()).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_dry_streak_60d_base_v027_signal(volume):
    """Consecutive bars where volume < 0.5*SMA21, capped 60."""
    m = _sma(volume, 21)
    dry = (volume < 0.5 * m).astype(float).where(~m.isna())
    return dry.rolling(60, min_periods=60).apply(_consec_true, raw=True).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_dry_count_120d_base_v028_signal(volume):
    """Number of dry-volume days (<0.5x SMA21) in trailing 120 bars."""
    m = _sma(volume, 21)
    dry = (volume < 0.5 * m).astype(float).where(~m.isna())
    return dry.rolling(120, min_periods=120).sum().replace([np.inf, -np.inf], np.nan)


# === Volume volatility =====================================================


def f21rv_f21_raw_volume_metrics_logvol_std_30d_base_v029_signal(volume):
    """Rolling std of log(volume) over 30 bars. Scale-free volume vol."""
    lv = np.log(volume.replace(0.0, np.nan))
    return lv.rolling(30, min_periods=30).std().replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_vol_volofvol_60d_base_v030_signal(volume):
    """Std of rolling-20 std(log vol) over 60 bars (vol-of-vol of volume)."""
    lv = np.log(volume.replace(0.0, np.nan))
    s = lv.rolling(20, min_periods=20).std()
    return s.rolling(60, min_periods=60).std().replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_vol_range_over_mean_40d_base_v031_signal(volume):
    """(max-min)/mean of volume over 40 bars. Volume range normalized."""
    mx = volume.rolling(40, min_periods=40).max()
    mn = volume.rolling(40, min_periods=40).min()
    m = _sma(volume, 40)
    return ((mx - mn) / m.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_vol_pctchg_std_45d_base_v032_signal(volume):
    """Rolling std of volume's daily pct_change over 45 bars."""
    pc = volume.pct_change(1)
    return pc.rolling(45, min_periods=45).std().replace([np.inf, -np.inf], np.nan)


# === Volume autocorrelation (raw, log, lag5) ===============================


def f21rv_f21_raw_volume_metrics_vol_acf_lag1_45d_base_v033_signal(volume):
    """Volume autocorrelation at lag 1 over 45-bar window."""
    def _ac(x):
        if len(x) < 3:
            return np.nan
        a = x[1:]; b = x[:-1]
        sa = a.std(); sb = b.std()
        if sa == 0.0 or sb == 0.0 or not np.isfinite(sa) or not np.isfinite(sb):
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    return volume.rolling(45, min_periods=45).apply(_ac, raw=True).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_vol_acf_lag5_80d_base_v034_signal(volume):
    """Volume autocorrelation at lag 5 over 80-bar window."""
    def _ac5(x):
        if len(x) < 10:
            return np.nan
        a = x[5:]; b = x[:-5]
        sa = a.std(); sb = b.std()
        if sa == 0.0 or sb == 0.0 or not np.isfinite(sa) or not np.isfinite(sb):
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    return volume.rolling(80, min_periods=80).apply(_ac5, raw=True).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_logvol_acf_lag1_120d_base_v035_signal(volume):
    """log(volume) autocorrelation at lag 1 over 120-bar window."""
    lv = np.log(volume.replace(0.0, np.nan))
    def _aclv(x):
        if len(x) < 3 or not np.all(np.isfinite(x)):
            return np.nan
        a = x[1:]; b = x[:-1]
        sa = a.std(); sb = b.std()
        if sa == 0.0 or sb == 0.0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    return lv.rolling(120, min_periods=120).apply(_aclv, raw=True).replace([np.inf, -np.inf], np.nan)


# === Cumulative volume features (share of window) ==========================


def f21rv_f21_raw_volume_metrics_vol_share_top5_30d_base_v036_signal(volume):
    """Sum of top-5 volume days in trailing 30 / sum of trailing 30 volume.
    Concentration ratio: how much of monthly volume comes from 5 biggest days."""
    def _t5(x):
        if len(x) < 6 or not np.all(np.isfinite(x)):
            return np.nan
        y = np.sort(x)[::-1]
        s = x.sum()
        if s == 0.0:
            return np.nan
        return float(y[:5].sum() / s)
    return volume.rolling(30, min_periods=30).apply(_t5, raw=True).replace([np.inf, -np.inf], np.nan)


# === Volume cone (position within own range) ===============================


def f21rv_f21_raw_volume_metrics_vol_cone_45d_base_v037_signal(volume):
    """(vol - min(vol,45)) / (max(vol,45) - min(vol,45)). Volume's position in own range."""
    mn = volume.rolling(45, min_periods=45).min()
    mx = volume.rolling(45, min_periods=45).max()
    return ((volume - mn) / (mx - mn).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Bounded transforms (structurally different from raw z) ================


def f21rv_f21_raw_volume_metrics_vol_change_streak_40d_base_v038_signal(volume):
    """Net sign-streak: cum count of consecutive positive minus negative volume
    changes within last 40 bars (windowed). Direction persistence — distinct from
    level z-scores by being a sign-only structural measure."""
    s = np.sign(volume.diff(1))
    def _net(x):
        if len(x) == 0:
            return np.nan
        return float(x.sum())
    return s.rolling(40, min_periods=40).apply(_net, raw=True).replace([np.inf, -np.inf], np.nan)


# === Statistical: volume mean reversion / Sharpe ===========================


def f21rv_f21_raw_volume_metrics_vol_meanrev_rate_50d_base_v039_signal(volume):
    """OLS slope of (log vol) regressed on lag(log vol) over 50 bars — AR(1) coef
    measuring mean-reversion strength of volume."""
    lv = np.log(volume.replace(0.0, np.nan))
    def _ar1(x):
        if len(x) < 4 or not np.all(np.isfinite(x)):
            return np.nan
        a = x[1:]; b = x[:-1]
        mb = b.mean(); ma = a.mean()
        var = np.sum((b - mb) ** 2)
        if var == 0.0:
            return np.nan
        cov = np.sum((b - mb) * (a - ma))
        return float(cov / var)
    return lv.rolling(50, min_periods=50).apply(_ar1, raw=True).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_vol_sharpe_45d_base_v040_signal(volume):
    """Volume "Sharpe": SMA(vol,45) / std(vol,45). Information-ratio analog."""
    m = _sma(volume, 45)
    sd = volume.rolling(45, min_periods=45).std()
    return (m / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Discrete states =======================================================


def f21rv_f21_raw_volume_metrics_high_vol_top25_60d_base_v041_signal(volume):
    """Binary: volume > 60d-rolling Q75. Top-quartile-volume day flag."""
    q = volume.rolling(60, min_periods=60).quantile(0.75)
    return (volume > q).astype(float).where(~q.isna()).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_low_vol_bot25_60d_base_v042_signal(volume):
    """Binary: volume < 60d-rolling Q25. Bottom-quartile-volume day flag."""
    q = volume.rolling(60, min_periods=60).quantile(0.25)
    return (volume < q).astype(float).where(~q.isna()).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_dayssince_highvol_100d_base_v043_signal(volume):
    """Bars since last top-decile volume day (rolling 100-bar quantile), capped 100."""
    q = volume.rolling(100, min_periods=100).quantile(0.90)
    hi = (volume > q).astype(float).where(~q.isna())
    return hi.rolling(100, min_periods=100).apply(_streak_last_true, raw=True).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_dayssince_lowvol_100d_base_v044_signal(volume):
    """Bars since last bottom-decile volume day (rolling 100-bar quantile)."""
    q = volume.rolling(100, min_periods=100).quantile(0.10)
    lo = (volume < q).astype(float).where(~q.isna())
    return lo.rolling(100, min_periods=100).apply(_streak_last_true, raw=True).replace([np.inf, -np.inf], np.nan)


# === Volume Stochastic (oscillator on volume) ==============================


def f21rv_f21_raw_volume_metrics_vol_stoch_30d_base_v045_signal(volume):
    """Stochastic of volume over 30 bars: (vol - L30) / (H30 - L30) * 100."""
    mn = volume.rolling(30, min_periods=30).min()
    mx = volume.rolling(30, min_periods=30).max()
    return (100.0 * (volume - mn) / (mx - mn).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Signed volume (volume-only — no direct price comparison; tick direction
# === weights the volume series — distinct from f23 OBV / f24 confirmation) =


def f21rv_f21_raw_volume_metrics_signed_vol_norm_20d_base_v046_signal(close, volume):
    """sign(close.diff(1)) * volume / SMA(volume, 20). Normalized signed volume.
    SIGNED-VOLUME statistic of the volume series weighted by tick direction;
    distinct from f23 OBV (cumulative running total) and f24 (correlation)."""
    s = np.sign(close.diff(1))
    m = _sma(volume, 20)
    return (s * volume / m.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_signed_vol_share_40d_base_v047_signal(close, volume):
    """sum(sign(dC) * vol, 40) / sum(vol, 40). Net signed-volume share. Bounded [-1,1]."""
    s = np.sign(close.diff(1))
    num = (s * volume).rolling(40, min_periods=40).sum()
    den = volume.rolling(40, min_periods=40).sum()
    return (num / den.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Volume cumulative-vs-realized (cum vs windowed avg) ===================


def f21rv_f21_raw_volume_metrics_vol_acf_sign_flips_50d_base_v048_signal(volume):
    """Count of sign-flips in vol.diff(1) over 50 bars / 50. Measures
    high-frequency oscillation of volume. Distinct from cumulative ratios."""
    s = np.sign(volume.diff(1))
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(50, min_periods=50).mean().replace([np.inf, -np.inf], np.nan)


# === Additional structural volume features =================================


def f21rv_f21_raw_volume_metrics_vol_max_to_min_30d_base_v049_signal(volume):
    """log(max(vol,30) / min(vol,30)). Log spread of volume range."""
    mx = volume.rolling(30, min_periods=30).max()
    mn = volume.rolling(30, min_periods=30).min()
    return np.log(mx / mn.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_signed_logvol_diff_25d_base_v050_signal(volume):
    """sum(sign(d log vol), 25). Net direction of volume changes — distribution-free."""
    s = np.sign(np.log(volume / volume.shift(1)))
    return s.rolling(25, min_periods=25).sum().replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_vol_streak_up_30d_base_v051_signal(volume):
    """Consecutive bars of strictly increasing volume, capped 30."""
    up = (volume.diff(1) > 0.0).astype(float).where(~volume.diff(1).isna())
    return up.rolling(30, min_periods=30).apply(_consec_true, raw=True).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_vol_streak_down_30d_base_v052_signal(volume):
    """Consecutive bars of strictly decreasing volume, capped 30."""
    dn = (volume.diff(1) < 0.0).astype(float).where(~volume.diff(1).isna())
    return dn.rolling(30, min_periods=30).apply(_consec_true, raw=True).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_vol_entropy_30d_base_v053_signal(volume):
    """Shannon entropy of the volume distribution within 30-bar window.
    Computed on a histogram normalized to a 10-bin pdf."""
    def _ent(x):
        if len(x) < 5 or not np.all(np.isfinite(x)) or np.all(x == x[0]):
            return np.nan
        h, _ = np.histogram(x, bins=10)
        p = h / h.sum()
        p = p[p > 0.0]
        return float(-np.sum(p * np.log(p)))
    return volume.rolling(30, min_periods=30).apply(_ent, raw=True).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_vol_logslope_60d_base_v054_signal(volume):
    """OLS slope of log(volume) vs time over 60 bars. Volume-only trend slope."""
    lv = np.log(volume.replace(0.0, np.nan))
    def _slope(x):
        n = len(x); t = np.arange(n, dtype=float)
        if not np.all(np.isfinite(x)):
            return np.nan
        mt = t.mean(); mx = x.mean()
        cov = np.sum((t - mt) * (x - mx))
        var = np.sum((t - mt) ** 2)
        if var == 0.0:
            return np.nan
        return float(cov / var)
    return lv.rolling(60, min_periods=60).apply(_slope, raw=True).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_vol_logslope_r2_80d_base_v055_signal(volume):
    """R^2 of OLS fit log(volume) vs time over 80 bars. Trend strength of volume."""
    lv = np.log(volume.replace(0.0, np.nan))
    def _r2(x):
        n = len(x); t = np.arange(n, dtype=float)
        if not np.all(np.isfinite(x)):
            return np.nan
        mt = t.mean(); mx = x.mean()
        cov = np.sum((t - mt) * (x - mx))
        var_t = np.sum((t - mt) ** 2); var_x = np.sum((x - mx) ** 2)
        if var_t == 0.0 or var_x == 0.0:
            return np.nan
        return float((cov * cov) / (var_t * var_x))
    return lv.rolling(80, min_periods=80).apply(_r2, raw=True).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_vol_max_argmax_50d_base_v056_signal(volume):
    """Argmax position within 50-bar window — bars since the trailing volume max,
    normalized to [0,1]. Distinct shape from days-since-spike (different threshold)."""
    def _ax(x):
        if len(x) == 0 or not np.all(np.isfinite(x)):
            return np.nan
        return float((len(x) - 1 - int(np.argmax(x))) / max(1, len(x) - 1))
    return volume.rolling(50, min_periods=50).apply(_ax, raw=True).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_vol_min_argmin_50d_base_v057_signal(volume):
    """Argmin position within 50-bar window — bars since the trailing volume min."""
    def _ax(x):
        if len(x) == 0 or not np.all(np.isfinite(x)):
            return np.nan
        return float((len(x) - 1 - int(np.argmin(x))) / max(1, len(x) - 1))
    return volume.rolling(50, min_periods=50).apply(_ax, raw=True).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_vol_pct_up_days_120d_base_v058_signal(volume):
    """Fraction of bars in trailing 120 with volume.diff(1) > 0. Distribution-free
    direction-frequency of volume changes, anchored at long horizon."""
    up = (volume.diff(1) > 0.0).astype(float).where(~volume.diff(1).isna())
    return up.rolling(120, min_periods=120).mean().replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_vol_acf_change_lag1_60d_base_v059_signal(volume):
    """Autocorrelation of volume.pct_change(1) at lag 1 over 60 bars.
    Measures persistence of change direction. Distinct from level autocorr."""
    pc = volume.pct_change(1)
    def _ac(x):
        if len(x) < 3 or not np.all(np.isfinite(x)):
            return np.nan
        a = x[1:]; b = x[:-1]
        sa = a.std(); sb = b.std()
        if sa == 0.0 or sb == 0.0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    return pc.rolling(60, min_periods=60).apply(_ac, raw=True).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_vol_pctchg_skew_60d_base_v060_signal(volume):
    """Rolling 60-bar skew of volume.pct_change(1)."""
    return volume.pct_change(1).rolling(60, min_periods=60).skew().replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_dv_iqr_over_med_140d_base_v061_signal(closeadj, volume):
    """(Q75-Q25)/median of dollar-volume over 140 bars. Long-horizon dollar-volume
    relative spread — distinct from raw-vol IQR (different series, different N)."""
    dv = closeadj * volume
    q25 = dv.rolling(140, min_periods=140).quantile(0.25)
    q75 = dv.rolling(140, min_periods=140).quantile(0.75)
    med = dv.rolling(140, min_periods=140).median()
    return ((q75 - q25) / med.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_dv_cv_90d_base_v062_signal(closeadj, volume):
    """std(dv,90) / mean(dv,90). Dollar-volume coefficient of variation,
    long-horizon (>21d -> closeadj). Distinct from raw-vol CV by including price."""
    dv = closeadj * volume
    m = _sma(dv, 90)
    sd = dv.rolling(90, min_periods=90).std()
    return (sd / m.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_dv_volofvol_80d_base_v063_signal(closeadj, volume):
    """Std of rolling-20 std(log dv) over 80 bars (vol-of-vol of dollar volume)."""
    ldv = np.log((closeadj * volume).replace(0.0, np.nan))
    s = ldv.rolling(20, min_periods=20).std()
    return s.rolling(80, min_periods=80).std().replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_vol_pct_extreme_30d_base_v064_signal(volume):
    """Fraction of bars in trailing 30 where |volume z-21| > 1.5. Tail concentration."""
    m = _sma(volume, 21)
    sd = volume.rolling(21, min_periods=21).std()
    z = (volume - m) / sd.replace(0.0, np.nan)
    flag = (z.abs() > 1.5).astype(float).where(~z.isna())
    return flag.rolling(30, min_periods=30).mean().replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_vol_dispnorm_70d_base_v065_signal(volume):
    """(Q90 - Q10) / (Q90 + Q10) over 70 bars. Symmetric volume dispersion."""
    q10 = volume.rolling(70, min_periods=70).quantile(0.10)
    q90 = volume.rolling(70, min_periods=70).quantile(0.90)
    return ((q90 - q10) / (q90 + q10).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_volume_zero_streak_50d_base_v066_signal(volume):
    """Mean log-vol within an inner 5-bar rolling vs trailing 50-bar mean diff,
    averaged. Captures persistence of low/high regimes."""
    lv = np.log(volume.replace(0.0, np.nan))
    inner = lv.rolling(5, min_periods=5).mean()
    outer = lv.rolling(50, min_periods=50).mean()
    return (inner - outer).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_vol_acf_lag2_60d_base_v067_signal(volume):
    """Volume autocorrelation at lag 2 over 60 bars — different lag than lag1/lag5."""
    def _ac2(x):
        if len(x) < 5:
            return np.nan
        a = x[2:]; b = x[:-2]
        sa = a.std(); sb = b.std()
        if sa == 0.0 or sb == 0.0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    return volume.rolling(60, min_periods=60).apply(_ac2, raw=True).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_vol_logsharpe_120d_base_v068_signal(volume):
    """mean(log vol, 120) / std(log vol, 120). Log-domain Sharpe ratio of volume,
    long-horizon. Distinct functional form from short Sharpe v040."""
    lv = np.log(volume.replace(0.0, np.nan))
    m = lv.rolling(120, min_periods=120).mean()
    sd = lv.rolling(120, min_periods=120).std()
    return (m / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_vol_above_below_ratio_45d_base_v069_signal(volume):
    """count(vol > SMA21)/45 minus 0.5 over a 45-bar window. Frequency-bias of being
    above typical, scaled around zero. Discrete-count based, structurally distinct."""
    m = _sma(volume, 21)
    flag = (volume > m).astype(float).where(~m.isna())
    return (flag.rolling(45, min_periods=45).mean() - 0.5).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_vol_pctchg_abs_45d_base_v070_signal(volume):
    """Mean of |volume.pct_change(1)| over 45 bars. Activity magnitude using
    pct change (not log change). Distinct from rank/level features."""
    return volume.pct_change(1).abs().rolling(45, min_periods=45).mean().replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_vol_streak_high_50d_base_v071_signal(volume):
    """Consecutive bars where volume > SMA(volume,21), capped 50. Persistence
    streak of above-average volume — discrete-count class."""
    m = _sma(volume, 21)
    flag = (volume > m).astype(float).where(~m.isna())
    return flag.rolling(50, min_periods=50).apply(_consec_true, raw=True).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_dv_acf_lag1_70d_base_v072_signal(closeadj, volume):
    """Dollar-volume autocorrelation at lag 1 over 70 bars."""
    dv = closeadj * volume
    def _ac(x):
        if len(x) < 3 or not np.all(np.isfinite(x)):
            return np.nan
        a = x[1:]; b = x[:-1]
        sa = a.std(); sb = b.std()
        if sa == 0.0 or sb == 0.0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    return dv.rolling(70, min_periods=70).apply(_ac, raw=True).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_vol_zerocenter_norm_15d_base_v073_signal(volume):
    """(vol - median(vol,15)) / IQR(vol,15). Robust normalized, short-horizon."""
    med = volume.rolling(15, min_periods=15).median()
    q25 = volume.rolling(15, min_periods=15).quantile(0.25)
    q75 = volume.rolling(15, min_periods=15).quantile(0.75)
    return ((volume - med) / (q75 - q25).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_vol_runs_test_60d_base_v074_signal(volume):
    """Wald-Wolfowitz-style runs count of (vol > median) over 60 bars,
    normalized by expected runs ~ n/2. Tests for randomness in volume sequence."""
    def _runs(x):
        if len(x) < 10 or not np.all(np.isfinite(x)):
            return np.nan
        med = np.median(x)
        b = (x > med).astype(int)
        if b.sum() == 0 or b.sum() == len(b):
            return np.nan
        flips = int(np.sum(b[1:] != b[:-1])) + 1
        return float(flips / (len(b) / 2.0))
    return volume.rolling(60, min_periods=60).apply(_runs, raw=True).replace([np.inf, -np.inf], np.nan)


def f21rv_f21_raw_volume_metrics_vol_extreme_tail_75d_base_v075_signal(volume):
    """Mean of top-10% volume / mean of remaining 90% over 75 bars.
    Ratio measures concentration of large volume."""
    def _tail(x):
        if len(x) < 10 or not np.all(np.isfinite(x)):
            return np.nan
        y = np.sort(x)[::-1]
        k = max(1, int(0.1 * len(y)))
        top = y[:k].mean(); rest = y[k:].mean()
        if rest == 0.0:
            return np.nan
        return float(top / rest)
    return volume.rolling(75, min_periods=75).apply(_tail, raw=True).replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f21_raw_volume_metrics_base_001_075_REGISTRY = {
    "f21rv_f21_raw_volume_metrics_logvol_sma5_base_v001_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_logvol_sma5_base_v001_signal},
    "f21rv_f21_raw_volume_metrics_logvol_sma5_sma50_base_v002_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_logvol_sma5_sma50_base_v002_signal},
    "f21rv_f21_raw_volume_metrics_logvol_sma20_sma200_base_v003_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_logvol_sma20_sma200_base_v003_signal},
    "f21rv_f21_raw_volume_metrics_logvol_ema_diff_10_60_base_v004_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_logvol_ema_diff_10_60_base_v004_signal},
    "f21rv_f21_raw_volume_metrics_median_vol_ratio_20_120_base_v005_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_median_vol_ratio_20_120_base_v005_signal},
    "f21rv_f21_raw_volume_metrics_volz_21d_base_v006_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_volz_21d_base_v006_signal},
    "f21rv_f21_raw_volume_metrics_volrank_60d_base_v007_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_volrank_60d_base_v007_signal},
    "f21rv_f21_raw_volume_metrics_dv_signed_share_30d_base_v008_signal": {"inputs": ["close", "closeadj", "volume"], "func": f21rv_f21_raw_volume_metrics_dv_signed_share_30d_base_v008_signal},
    "f21rv_f21_raw_volume_metrics_dv_termstruct_5_252_base_v009_signal": {"inputs": ["closeadj", "volume"], "func": f21rv_f21_raw_volume_metrics_dv_termstruct_5_252_base_v009_signal},
    "f21rv_f21_raw_volume_metrics_dv_termstruct_20_120_base_v010_signal": {"inputs": ["closeadj", "volume"], "func": f21rv_f21_raw_volume_metrics_dv_termstruct_20_120_base_v010_signal},
    "f21rv_f21_raw_volume_metrics_vol_skew_60d_base_v011_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_skew_60d_base_v011_signal},
    "f21rv_f21_raw_volume_metrics_vol_kurt_180d_base_v012_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_kurt_180d_base_v012_signal},
    "f21rv_f21_raw_volume_metrics_logvol_skew_120d_base_v013_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_logvol_skew_120d_base_v013_signal},
    "f21rv_f21_raw_volume_metrics_logvol_kurt_40d_base_v014_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_logvol_kurt_40d_base_v014_signal},
    "f21rv_f21_raw_volume_metrics_vol_mad_over_std_45d_base_v015_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_mad_over_std_45d_base_v015_signal},
    "f21rv_f21_raw_volume_metrics_vol_cv_60d_base_v016_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_cv_60d_base_v016_signal},
    "f21rv_f21_raw_volume_metrics_vol_gini_30d_base_v017_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_gini_30d_base_v017_signal},
    "f21rv_f21_raw_volume_metrics_vol_iqr_over_med_50d_base_v018_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_iqr_over_med_50d_base_v018_signal},
    "f21rv_f21_raw_volume_metrics_volpct_1d_base_v019_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_volpct_1d_base_v019_signal},
    "f21rv_f21_raw_volume_metrics_logvol_diff_1d_base_v020_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_logvol_diff_1d_base_v020_signal},
    "f21rv_f21_raw_volume_metrics_abs_logvol_diff_10d_base_v021_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_abs_logvol_diff_10d_base_v021_signal},
    "f21rv_f21_raw_volume_metrics_spike_bin_21d_base_v022_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_spike_bin_21d_base_v022_signal},
    "f21rv_f21_raw_volume_metrics_spike_count_60d_base_v023_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_spike_count_60d_base_v023_signal},
    "f21rv_f21_raw_volume_metrics_spike_mag_60d_base_v024_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_spike_mag_60d_base_v024_signal},
    "f21rv_f21_raw_volume_metrics_dayssince_spike_80d_base_v025_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_dayssince_spike_80d_base_v025_signal},
    "f21rv_f21_raw_volume_metrics_dry_bin_21d_base_v026_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_dry_bin_21d_base_v026_signal},
    "f21rv_f21_raw_volume_metrics_dry_streak_60d_base_v027_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_dry_streak_60d_base_v027_signal},
    "f21rv_f21_raw_volume_metrics_dry_count_120d_base_v028_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_dry_count_120d_base_v028_signal},
    "f21rv_f21_raw_volume_metrics_logvol_std_30d_base_v029_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_logvol_std_30d_base_v029_signal},
    "f21rv_f21_raw_volume_metrics_vol_volofvol_60d_base_v030_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_volofvol_60d_base_v030_signal},
    "f21rv_f21_raw_volume_metrics_vol_range_over_mean_40d_base_v031_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_range_over_mean_40d_base_v031_signal},
    "f21rv_f21_raw_volume_metrics_vol_pctchg_std_45d_base_v032_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_pctchg_std_45d_base_v032_signal},
    "f21rv_f21_raw_volume_metrics_vol_acf_lag1_45d_base_v033_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_acf_lag1_45d_base_v033_signal},
    "f21rv_f21_raw_volume_metrics_vol_acf_lag5_80d_base_v034_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_acf_lag5_80d_base_v034_signal},
    "f21rv_f21_raw_volume_metrics_logvol_acf_lag1_120d_base_v035_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_logvol_acf_lag1_120d_base_v035_signal},
    "f21rv_f21_raw_volume_metrics_vol_share_top5_30d_base_v036_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_share_top5_30d_base_v036_signal},
    "f21rv_f21_raw_volume_metrics_vol_cone_45d_base_v037_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_cone_45d_base_v037_signal},
    "f21rv_f21_raw_volume_metrics_vol_change_streak_40d_base_v038_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_change_streak_40d_base_v038_signal},
    "f21rv_f21_raw_volume_metrics_vol_meanrev_rate_50d_base_v039_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_meanrev_rate_50d_base_v039_signal},
    "f21rv_f21_raw_volume_metrics_vol_sharpe_45d_base_v040_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_sharpe_45d_base_v040_signal},
    "f21rv_f21_raw_volume_metrics_high_vol_top25_60d_base_v041_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_high_vol_top25_60d_base_v041_signal},
    "f21rv_f21_raw_volume_metrics_low_vol_bot25_60d_base_v042_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_low_vol_bot25_60d_base_v042_signal},
    "f21rv_f21_raw_volume_metrics_dayssince_highvol_100d_base_v043_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_dayssince_highvol_100d_base_v043_signal},
    "f21rv_f21_raw_volume_metrics_dayssince_lowvol_100d_base_v044_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_dayssince_lowvol_100d_base_v044_signal},
    "f21rv_f21_raw_volume_metrics_vol_stoch_30d_base_v045_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_stoch_30d_base_v045_signal},
    "f21rv_f21_raw_volume_metrics_signed_vol_norm_20d_base_v046_signal": {"inputs": ["close", "volume"], "func": f21rv_f21_raw_volume_metrics_signed_vol_norm_20d_base_v046_signal},
    "f21rv_f21_raw_volume_metrics_signed_vol_share_40d_base_v047_signal": {"inputs": ["close", "volume"], "func": f21rv_f21_raw_volume_metrics_signed_vol_share_40d_base_v047_signal},
    "f21rv_f21_raw_volume_metrics_vol_acf_sign_flips_50d_base_v048_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_acf_sign_flips_50d_base_v048_signal},
    "f21rv_f21_raw_volume_metrics_vol_max_to_min_30d_base_v049_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_max_to_min_30d_base_v049_signal},
    "f21rv_f21_raw_volume_metrics_signed_logvol_diff_25d_base_v050_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_signed_logvol_diff_25d_base_v050_signal},
    "f21rv_f21_raw_volume_metrics_vol_streak_up_30d_base_v051_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_streak_up_30d_base_v051_signal},
    "f21rv_f21_raw_volume_metrics_vol_streak_down_30d_base_v052_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_streak_down_30d_base_v052_signal},
    "f21rv_f21_raw_volume_metrics_vol_entropy_30d_base_v053_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_entropy_30d_base_v053_signal},
    "f21rv_f21_raw_volume_metrics_vol_logslope_60d_base_v054_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_logslope_60d_base_v054_signal},
    "f21rv_f21_raw_volume_metrics_vol_logslope_r2_80d_base_v055_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_logslope_r2_80d_base_v055_signal},
    "f21rv_f21_raw_volume_metrics_vol_max_argmax_50d_base_v056_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_max_argmax_50d_base_v056_signal},
    "f21rv_f21_raw_volume_metrics_vol_min_argmin_50d_base_v057_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_min_argmin_50d_base_v057_signal},
    "f21rv_f21_raw_volume_metrics_vol_pct_up_days_120d_base_v058_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_pct_up_days_120d_base_v058_signal},
    "f21rv_f21_raw_volume_metrics_vol_acf_change_lag1_60d_base_v059_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_acf_change_lag1_60d_base_v059_signal},
    "f21rv_f21_raw_volume_metrics_vol_pctchg_skew_60d_base_v060_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_pctchg_skew_60d_base_v060_signal},
    "f21rv_f21_raw_volume_metrics_dv_iqr_over_med_140d_base_v061_signal": {"inputs": ["closeadj", "volume"], "func": f21rv_f21_raw_volume_metrics_dv_iqr_over_med_140d_base_v061_signal},
    "f21rv_f21_raw_volume_metrics_dv_cv_90d_base_v062_signal": {"inputs": ["closeadj", "volume"], "func": f21rv_f21_raw_volume_metrics_dv_cv_90d_base_v062_signal},
    "f21rv_f21_raw_volume_metrics_dv_volofvol_80d_base_v063_signal": {"inputs": ["closeadj", "volume"], "func": f21rv_f21_raw_volume_metrics_dv_volofvol_80d_base_v063_signal},
    "f21rv_f21_raw_volume_metrics_vol_pct_extreme_30d_base_v064_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_pct_extreme_30d_base_v064_signal},
    "f21rv_f21_raw_volume_metrics_vol_dispnorm_70d_base_v065_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_dispnorm_70d_base_v065_signal},
    "f21rv_f21_raw_volume_metrics_volume_zero_streak_50d_base_v066_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_volume_zero_streak_50d_base_v066_signal},
    "f21rv_f21_raw_volume_metrics_vol_acf_lag2_60d_base_v067_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_acf_lag2_60d_base_v067_signal},
    "f21rv_f21_raw_volume_metrics_vol_logsharpe_120d_base_v068_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_logsharpe_120d_base_v068_signal},
    "f21rv_f21_raw_volume_metrics_vol_above_below_ratio_45d_base_v069_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_above_below_ratio_45d_base_v069_signal},
    "f21rv_f21_raw_volume_metrics_vol_pctchg_abs_45d_base_v070_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_pctchg_abs_45d_base_v070_signal},
    "f21rv_f21_raw_volume_metrics_vol_streak_high_50d_base_v071_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_streak_high_50d_base_v071_signal},
    "f21rv_f21_raw_volume_metrics_dv_acf_lag1_70d_base_v072_signal": {"inputs": ["closeadj", "volume"], "func": f21rv_f21_raw_volume_metrics_dv_acf_lag1_70d_base_v072_signal},
    "f21rv_f21_raw_volume_metrics_vol_zerocenter_norm_15d_base_v073_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_zerocenter_norm_15d_base_v073_signal},
    "f21rv_f21_raw_volume_metrics_vol_runs_test_60d_base_v074_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_runs_test_60d_base_v074_signal},
    "f21rv_f21_raw_volume_metrics_vol_extreme_tail_75d_base_v075_signal": {"inputs": ["volume"], "func": f21rv_f21_raw_volume_metrics_vol_extreme_tail_75d_base_v075_signal},
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
    for name, entry in f21_raw_volume_metrics_base_001_075_REGISTRY.items():
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
    print(f"OK base_001_075: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
