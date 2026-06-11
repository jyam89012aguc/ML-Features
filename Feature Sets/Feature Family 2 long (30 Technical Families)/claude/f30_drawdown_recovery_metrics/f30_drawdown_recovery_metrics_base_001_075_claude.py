"""f30_drawdown_recovery_metrics base features 001-075.

Domain: DRAWDOWN, RECOVERY, UNDERWATER dynamics. Every feature references a
drawdown construct (DD from rolling-high, underwater duration, recovery
slope, Ulcer Index, Pain Ratio, Calmar, Sterling, drawup symmetric
variants).  NaN policy: never fillna(<value>); only replace([inf,-inf], nan)
at the final return. Window > 21d uses closeadj. Each feature spells its
DD formula inline.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Helpers (drawdown / underwater primitives). Each feature spells its own
# DD formula inline.
# ---------------------------------------------------------------------------


def _dd(s: pd.Series, n: int) -> pd.Series:
    """Drawdown from rolling-N high: close / rolling_max - 1 (<= 0)."""
    return s / s.rolling(n, min_periods=n).max() - 1.0


def _du(s: pd.Series, n: int) -> pd.Series:
    """Drawup from rolling-N low: close / rolling_min - 1 (>= 0)."""
    return s / s.rolling(n, min_periods=n).min() - 1.0


def _underwater_days(s: pd.Series, n: int) -> pd.Series:
    """Bars since last N-window high. 0 at new highs, increases underwater."""
    rmax = s.rolling(n, min_periods=n).max()
    at_high = (s >= rmax).astype(float).where(~rmax.isna())
    out = pd.Series(np.nan, index=s.index, dtype=float)
    cnt = np.nan
    av = at_high.values
    for i in range(len(s)):
        if not np.isfinite(av[i]):
            continue
        if av[i] >= 0.5:
            cnt = 0.0
        else:
            cnt = (cnt + 1.0) if np.isfinite(cnt) else np.nan
        out.iat[i] = cnt
    return out


def _drawup_days(s: pd.Series, n: int) -> pd.Series:
    """Bars since last N-window low."""
    rmin = s.rolling(n, min_periods=n).min()
    at_low = (s <= rmin).astype(float).where(~rmin.isna())
    out = pd.Series(np.nan, index=s.index, dtype=float)
    cnt = np.nan
    av = at_low.values
    for i in range(len(s)):
        if not np.isfinite(av[i]):
            continue
        if av[i] >= 0.5:
            cnt = 0.0
        else:
            cnt = (cnt + 1.0) if np.isfinite(cnt) else np.nan
        out.iat[i] = cnt
    return out


def _atr(h: pd.Series, l: pd.Series, c: pd.Series, n: int) -> pd.Series:
    pc = c.shift(1)
    tr = pd.concat([h - l, (h - pc).abs(), (l - pc).abs()], axis=1).max(axis=1)
    return tr.rolling(n, min_periods=n).mean()


# ---------------------------------------------------------------------------
# Features 001-075
# ---------------------------------------------------------------------------


# === Raw drawdown levels at varied lookbacks (widely spaced) ===============


def f30dr_f30_drawdown_recovery_metrics_dd_20d_base_v001_signal(close):
    """DD from 20d rolling high: close/rmax20 - 1 (<=0). Short-horizon DD level."""
    n = 20
    return (close / close.rolling(n, min_periods=n).max() - 1.0).replace([np.inf, -np.inf], np.nan)


def f30dr_f30_drawdown_recovery_metrics_dd_63d_base_v002_signal(closeadj):
    """DD from 63d rolling high. Quarter-horizon DD level."""
    n = 63
    return (closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0).replace([np.inf, -np.inf], np.nan)


def f30dr_f30_drawdown_recovery_metrics_dd_252d_base_v003_signal(closeadj):
    """DD from 252d rolling high. Annual DD level."""
    n = 252
    return (closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0).replace([np.inf, -np.inf], np.nan)


def f30dr_f30_drawdown_recovery_metrics_dd_504d_base_v004_signal(closeadj):
    """DD from 504d rolling high. Bi-annual DD level."""
    n = 504
    return (closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0).replace([np.inf, -np.inf], np.nan)


# === Maximum drawdown observed inside rolling N ============================


def f30dr_f30_drawdown_recovery_metrics_maxdd_30d_base_v005_signal(closeadj):
    """Min (most-negative) DD-curve over last 30 bars, where DD is from 30d rmax."""
    n = 30
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    return dd.rolling(n, min_periods=n).min().replace([np.inf, -np.inf], np.nan)


def f30dr_f30_drawdown_recovery_metrics_maxdd_126d_base_v006_signal(closeadj):
    """Min (most-negative) DD-curve over last 126 bars (DD from 126d rmax)."""
    n = 126
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    return dd.rolling(n, min_periods=n).min().replace([np.inf, -np.inf], np.nan)


# === Average drawdown over N ===============================================


def f30dr_f30_drawdown_recovery_metrics_avgdd_60d_base_v007_signal(closeadj):
    """Mean DD over 60d rolling window (DD measured against 60d rmax)."""
    n = 60
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    return dd.rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


# === Underwater duration (bars since last high) ============================


def f30dr_f30_drawdown_recovery_metrics_uw_days_50d_base_v008_signal(closeadj):
    """Bars since last 50d high. Underwater duration count."""
    n = 50
    rmax = closeadj.rolling(n, min_periods=n).max()
    at_high = (closeadj >= rmax).astype(float).where(~rmax.isna())
    out = pd.Series(np.nan, index=closeadj.index, dtype=float)
    cnt = np.nan
    av = at_high.values
    for i in range(len(closeadj)):
        if not np.isfinite(av[i]):
            continue
        if av[i] >= 0.5:
            cnt = 0.0
        else:
            cnt = (cnt + 1.0) if np.isfinite(cnt) else np.nan
        out.iat[i] = cnt
    return out.replace([np.inf, -np.inf], np.nan)


def f30dr_f30_drawdown_recovery_metrics_uw_days_200d_base_v009_signal(closeadj):
    """Bars since last 200d high. Long underwater duration."""
    n = 200
    rmax = closeadj.rolling(n, min_periods=n).max()
    at_high = (closeadj >= rmax).astype(float).where(~rmax.isna())
    out = pd.Series(np.nan, index=closeadj.index, dtype=float)
    cnt = np.nan
    av = at_high.values
    for i in range(len(closeadj)):
        if not np.isfinite(av[i]):
            continue
        if av[i] >= 0.5:
            cnt = 0.0
        else:
            cnt = (cnt + 1.0) if np.isfinite(cnt) else np.nan
        out.iat[i] = cnt
    return out.replace([np.inf, -np.inf], np.nan)


# === Underwater integral: sum of |DD| over N ===============================


def f30dr_f30_drawdown_recovery_metrics_uw_integral_40d_base_v010_signal(closeadj):
    """Sum of |DD| over 40 bars (DD against 40d rmax). Pain area."""
    n = 40
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    return dd.abs().rolling(n, min_periods=n).sum().replace([np.inf, -np.inf], np.nan)


def f30dr_f30_drawdown_recovery_metrics_uw_integral_120d_base_v011_signal(closeadj):
    """Sum of |DD| over 120 bars. Cumulative pain over half-year horizon."""
    n = 120
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    return dd.abs().rolling(n, min_periods=n).sum().replace([np.inf, -np.inf], np.nan)


# === Time-weighted DD (linearly down-weighted older bars) ==================


def f30dr_f30_drawdown_recovery_metrics_dd_emerge_decay_45d_base_v012_signal(closeadj):
    """DD emergence-vs-decay asymmetry: corr between current |DD(45)| and prior bar's
    DD-direction (negative if recovering, positive if deepening). 45d window."""
    n = 45
    dd_abs = (closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0).abs()
    sign_chg = np.sign(dd_abs.diff())
    return dd_abs.rolling(n, min_periods=n).corr(sign_chg).replace([np.inf, -np.inf], np.nan)


# === Recovery features =====================================================


def f30dr_f30_drawdown_recovery_metrics_recovery_ratio_60d_base_v013_signal(closeadj):
    """How much of trailing-60d max DD has been recovered.
    1 - |current_dd_from_60d_max| / |min_dd_over_60d|."""
    n = 60
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    mindd = dd.rolling(n, min_periods=n).min()
    return (1.0 - dd.abs() / mindd.abs().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f30dr_f30_drawdown_recovery_metrics_recovery_slope_30d_base_v014_signal(closeadj):
    """Slope of recovery from trailing 30d low: (close - rmin30) / 30."""
    n = 30
    rmin = closeadj.rolling(n, min_periods=n).min()
    return ((closeadj - rmin) / float(n)).replace([np.inf, -np.inf], np.nan)


def f30dr_f30_drawdown_recovery_metrics_bars_since_trough_90d_base_v015_signal(closeadj):
    """Bars since trailing 90d low (argmax of rmin-touch within window)."""
    n = 90
    rmin = closeadj.rolling(n, min_periods=n).min()
    at_low = (closeadj <= rmin).astype(float).where(~rmin.isna())
    out = pd.Series(np.nan, index=closeadj.index, dtype=float)
    cnt = np.nan
    av = at_low.values
    for i in range(len(closeadj)):
        if not np.isfinite(av[i]):
            continue
        if av[i] >= 0.5:
            cnt = 0.0
        else:
            cnt = (cnt + 1.0) if np.isfinite(cnt) else np.nan
        out.iat[i] = cnt
    return out.replace([np.inf, -np.inf], np.nan)


# === DD statistics in trailing N ===========================================


def f30dr_f30_drawdown_recovery_metrics_dd_std_45d_base_v016_signal(closeadj):
    """Std of DD series over 45 bars (DD measured against 45d rmax)."""
    n = 45
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    return dd.rolling(n, min_periods=n).std().replace([np.inf, -np.inf], np.nan)


def f30dr_f30_drawdown_recovery_metrics_dd_count_5pct_100d_base_v017_signal(closeadj):
    """Count of bars in trailing 100d where |DD from 100d rmax| > 5%."""
    n = 100
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    flag = (dd.abs() > 0.05).astype(float).where(~dd.isna())
    return flag.rolling(n, min_periods=n).sum().replace([np.inf, -np.inf], np.nan)


def f30dr_f30_drawdown_recovery_metrics_dd_rank_120d_base_v018_signal(closeadj):
    """Percentile rank of current DD (vs 30d-rmax) within trailing 120d."""
    n_dd = 30; n_rank = 120
    dd = closeadj / closeadj.rolling(n_dd, min_periods=n_dd).max() - 1.0
    return dd.rolling(n_rank, min_periods=n_rank).apply(
        lambda x: float((np.sum(x <= x[-1]) - 1) / max(1, (len(x) - 1))), raw=True
    ).replace([np.inf, -np.inf], np.nan)


# === Drawup features (symmetric) ===========================================


def f30dr_f30_drawdown_recovery_metrics_drawup_20d_base_v019_signal(close):
    """Drawup from 20d rolling low: close/rmin20 - 1 (>=0)."""
    n = 20
    return (close / close.rolling(n, min_periods=n).min() - 1.0).replace([np.inf, -np.inf], np.nan)


def f30dr_f30_drawdown_recovery_metrics_drawup_120d_base_v020_signal(closeadj):
    """Drawup from 120d rolling low. Long-horizon recovery extent."""
    n = 120
    return (closeadj / closeadj.rolling(n, min_periods=n).min() - 1.0).replace([np.inf, -np.inf], np.nan)


def f30dr_f30_drawdown_recovery_metrics_max_drawup_50d_base_v021_signal(closeadj):
    """Max drawup observed over 50 bars (drawup from 50d rmin)."""
    n = 50
    du = closeadj / closeadj.rolling(n, min_periods=n).min() - 1.0
    return du.rolling(n, min_periods=n).max().replace([np.inf, -np.inf], np.nan)


def f30dr_f30_drawdown_recovery_metrics_drawup_to_drawdown_ratio_80d_base_v022_signal(closeadj):
    """Ratio of max-drawup to |min-drawdown| within trailing 80d window. Asymmetry of bounce vs slide."""
    n = 80
    du = closeadj / closeadj.rolling(n, min_periods=n).min() - 1.0
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    return (du.rolling(n, min_periods=n).max() / dd.rolling(n, min_periods=n).min().abs().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === DD distribution stats =================================================


def f30dr_f30_drawdown_recovery_metrics_dd_skew_75d_base_v023_signal(closeadj):
    """Skew of DD series (DD vs 75d rmax) over trailing 75 bars."""
    n = 75
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    return dd.rolling(n, min_periods=n).skew().replace([np.inf, -np.inf], np.nan)


def f30dr_f30_drawdown_recovery_metrics_dd_kurt_150d_base_v024_signal(closeadj):
    """Kurt of DD series (DD vs 150d rmax) over trailing 150 bars."""
    n = 150
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    return dd.rolling(n, min_periods=n).kurt().replace([np.inf, -np.inf], np.nan)


def f30dr_f30_drawdown_recovery_metrics_dd_mad_std_60d_base_v025_signal(closeadj):
    """MAD/std of DD series over 60 bars. Tail-heaviness proxy."""
    n = 60
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    mad = dd.rolling(n, min_periods=n).apply(lambda x: float(np.mean(np.abs(x - np.mean(x)))), raw=True)
    sig = dd.rolling(n, min_periods=n).std()
    return (mad / sig.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Pain metrics ==========================================================


def f30dr_f30_drawdown_recovery_metrics_ulcer_30d_base_v026_signal(closeadj):
    """Ulcer Index over 30 bars: sqrt(mean(DD^2)), DD vs 30d rmax."""
    n = 30
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    return np.sqrt((dd ** 2).rolling(n, min_periods=n).mean()).replace([np.inf, -np.inf], np.nan)


def f30dr_f30_drawdown_recovery_metrics_ulcer_pain_ratio_30_120_base_v027_signal(closeadj):
    """Ratio of short-Ulcer(30) to long-Ulcer(120) — DD-volatility regime relative metric.
    Differential structure decorrelates from raw integrals."""
    dd_s = closeadj / closeadj.rolling(30, min_periods=30).max() - 1.0
    dd_l = closeadj / closeadj.rolling(120, min_periods=120).max() - 1.0
    us = np.sqrt((dd_s ** 2).rolling(30, min_periods=30).mean())
    ul = np.sqrt((dd_l ** 2).rolling(120, min_periods=120).mean())
    return (us / ul.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f30dr_f30_drawdown_recovery_metrics_pain_ratio_60d_base_v028_signal(closeadj):
    """Pain Ratio: 60d mean log-return / Ulcer60. Higher = better risk-adjusted."""
    n = 60
    r = np.log(closeadj / closeadj.shift(1))
    avg_r = r.rolling(n, min_periods=n).mean()
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    ulcer = np.sqrt((dd ** 2).rolling(n, min_periods=n).mean())
    return (avg_r / ulcer.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f30dr_f30_drawdown_recovery_metrics_calmar_252d_base_v029_signal(closeadj):
    """Calmar-like: 252d log-return / |max DD over 252d|."""
    n = 252
    ret = np.log(closeadj / closeadj.shift(n))
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    mdd = dd.rolling(n, min_periods=n).min().abs()
    return (ret / mdd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f30dr_f30_drawdown_recovery_metrics_sterling_120d_base_v030_signal(closeadj):
    """Sterling-like: 120d log-return / |avg DD over 120d|."""
    n = 120
    ret = np.log(closeadj / closeadj.shift(n))
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    avgdd = dd.rolling(n, min_periods=n).mean().abs()
    return (ret / avgdd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Underwater fraction (% bars below recent high) ========================


def f30dr_f30_drawdown_recovery_metrics_uw_frac_40d_base_v031_signal(closeadj):
    """Fraction of trailing 40 bars where close < 40d-trailing rmax (strictly)."""
    n = 40
    rmax = closeadj.rolling(n, min_periods=n).max()
    below = (closeadj < rmax - 1e-12).astype(float).where(~rmax.isna())
    return below.rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


def f30dr_f30_drawdown_recovery_metrics_uw_frac_180d_base_v032_signal(closeadj):
    """Fraction of trailing 180 bars where close < 180d rmax."""
    n = 180
    rmax = closeadj.rolling(n, min_periods=n).max()
    below = (closeadj < rmax - 1e-12).astype(float).where(~rmax.isna())
    return below.rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


# === DD vs volatility ======================================================


def f30dr_f30_drawdown_recovery_metrics_dd_over_atr_30d_base_v033_signal(high, low, closeadj):
    """|DD30| / ATR(14) -- DD severity in ATR units."""
    n = 30
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    pc = closeadj.shift(1)
    tr = pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.rolling(14, min_periods=14).mean()
    return (dd.abs() * closeadj / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f30dr_f30_drawdown_recovery_metrics_dd_over_realvol_90d_base_v034_signal(closeadj):
    """|DD90| / (90d realized vol of log-returns)."""
    n = 90
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    rv = np.log(closeadj / closeadj.shift(1)).rolling(n, min_periods=n).std()
    return (dd.abs() / rv.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Discrete DD states ====================================================


def f30dr_f30_drawdown_recovery_metrics_in_dd_5pct_30d_base_v035_signal(closeadj):
    """Indicator: DD vs 30d rmax exceeds 5% (in moderate DD)."""
    n = 30
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    return (dd <= -0.05).astype(float).where(~dd.isna()).replace([np.inf, -np.inf], np.nan)


def f30dr_f30_drawdown_recovery_metrics_severe_dd_20pct_252d_base_v036_signal(closeadj):
    """Indicator: DD vs 252d rmax exceeds 20% (severe DD)."""
    n = 252
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    return (dd <= -0.20).astype(float).where(~dd.isna()).replace([np.inf, -np.inf], np.nan)


def f30dr_f30_drawdown_recovery_metrics_at_new_high_45d_base_v037_signal(closeadj):
    """Indicator: close at 45d new high (DD == 0)."""
    n = 45
    rmax = closeadj.rolling(n, min_periods=n).max()
    return ((closeadj >= rmax - 1e-12).astype(float)).where(~rmax.isna()).replace([np.inf, -np.inf], np.nan)


# === Bounded transforms of DD ==============================================


def f30dr_f30_drawdown_recovery_metrics_arctan_dd_50d_base_v038_signal(closeadj):
    """arctan(10 * DD vs 50d rmax). Bounded DD signal."""
    n = 50
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    return np.arctan(10.0 * dd).replace([np.inf, -np.inf], np.nan)


def f30dr_f30_drawdown_recovery_metrics_tanh_uw_frac_80d_base_v039_signal(closeadj):
    """tanh of (2 * underwater_fraction - 1) over 80d. Bounded UW-frac."""
    n = 80
    rmax = closeadj.rolling(n, min_periods=n).max()
    below = (closeadj < rmax - 1e-12).astype(float).where(~rmax.isna())
    f = below.rolling(n, min_periods=n).mean()
    return np.tanh(2.0 * f - 1.0).replace([np.inf, -np.inf], np.nan)


def f30dr_f30_drawdown_recovery_metrics_sigmoid_dd_rank_60d_base_v040_signal(closeadj):
    """sigmoid((rank(DD20) - 0.5) * 6) over 60d rank window."""
    n_dd = 20; n_rank = 60
    dd = closeadj / closeadj.rolling(n_dd, min_periods=n_dd).max() - 1.0
    rk = dd.rolling(n_rank, min_periods=n_rank).apply(
        lambda x: float((np.sum(x <= x[-1]) - 1) / max(1, (len(x) - 1))), raw=True
    )
    return (1.0 / (1.0 + np.exp(-6.0 * (rk - 0.5)))).replace([np.inf, -np.inf], np.nan)


# === DD slope (deepening vs recovering) ====================================


def f30dr_f30_drawdown_recovery_metrics_dd_slope_30d_base_v041_signal(closeadj):
    """5d diff of (DD vs 30d rmax). Positive = recovering, negative = deepening."""
    n = 30
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    return dd.diff(5).replace([np.inf, -np.inf], np.nan)


def f30dr_f30_drawdown_recovery_metrics_dd_curvature_90d_base_v042_signal(closeadj):
    """Curvature of (DD vs 90d rmax): dd - 2*dd.shift(10) + dd.shift(20)."""
    n = 90
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    return (dd - 2.0 * dd.shift(10) + dd.shift(20)).replace([np.inf, -np.inf], np.nan)


# === Multi-window DD comparison ============================================


def f30dr_f30_drawdown_recovery_metrics_shortdd_longdd_ratio_base_v043_signal(closeadj):
    """|DD20| / |DD120|. Short-DD vs long-DD magnitude ratio."""
    dd_s = closeadj / closeadj.rolling(20, min_periods=20).max() - 1.0
    dd_l = closeadj / closeadj.rolling(120, min_periods=120).max() - 1.0
    return (dd_s.abs() / dd_l.abs().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f30dr_f30_drawdown_recovery_metrics_dd_diff_45_180d_base_v044_signal(closeadj):
    """DD(45) - DD(180). Cross-window DD differential."""
    dd_a = closeadj / closeadj.rolling(45, min_periods=45).max() - 1.0
    dd_b = closeadj / closeadj.rolling(180, min_periods=180).max() - 1.0
    return (dd_a - dd_b).replace([np.inf, -np.inf], np.nan)


# === Recovery quality ======================================================


def f30dr_f30_drawdown_recovery_metrics_recovery_efficiency_60d_base_v045_signal(closeadj):
    """Recovery efficiency: (close - rmin60) / (rmax60 - rmin60). Stochastic-style
    but framed as: how far we've recovered from trough back toward 60d peak.
    Specifically a DD-recovery metric, NOT a raw channel position because it is
    explicitly used in DD/recovery framework here."""
    n = 60
    rmax = closeadj.rolling(n, min_periods=n).max()
    rmin = closeadj.rolling(n, min_periods=n).min()
    return ((closeadj - rmin) / (rmax - rmin).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f30dr_f30_drawdown_recovery_metrics_recovery_speed_30d_base_v046_signal(closeadj):
    """Log return from 30d-low to current bar, divided by bars since that low."""
    n = 30
    rmin = closeadj.rolling(n, min_periods=n).min()
    at_low = (closeadj <= rmin).astype(float).where(~rmin.isna())
    bars = pd.Series(np.nan, index=closeadj.index, dtype=float)
    cnt = np.nan
    av = at_low.values
    for i in range(len(closeadj)):
        if not np.isfinite(av[i]):
            continue
        if av[i] >= 0.5:
            cnt = 0.0
        else:
            cnt = (cnt + 1.0) if np.isfinite(cnt) else np.nan
        bars.iat[i] = cnt
    return (np.log(closeadj / rmin.replace(0.0, np.nan)) / (bars + 1.0)).replace([np.inf, -np.inf], np.nan)


# === Cumulative DD =========================================================


def f30dr_f30_drawdown_recovery_metrics_cum_dd_50d_base_v047_signal(closeadj):
    """Sum of all DDs (negative-only) over 50d. Cumulative-pain sum."""
    n = 50
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    return dd.rolling(n, min_periods=n).sum().replace([np.inf, -np.inf], np.nan)


def f30dr_f30_drawdown_recovery_metrics_dd_weighted_return_75d_base_v048_signal(closeadj):
    """DD-weighted return: sum(log_ret * |DD|) / sum(|DD|) over 75 bars."""
    n = 75
    dd_abs = (closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0).abs()
    r = np.log(closeadj / closeadj.shift(1))
    num = (r * dd_abs).rolling(n, min_periods=n).sum()
    den = dd_abs.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return (num / den).replace([np.inf, -np.inf], np.nan)


# === Max underwater length spanning N ======================================


def f30dr_f30_drawdown_recovery_metrics_max_uw_length_120d_base_v049_signal(closeadj):
    """Max consecutive underwater length in trailing 120d (vs 120d rmax)."""
    n = 120
    rmax = closeadj.rolling(n, min_periods=n).max()
    below = (closeadj < rmax - 1e-12).astype(float).where(~rmax.isna())

    def _maxrun(x):
        best = 0; cur = 0
        for v in x:
            if v >= 0.5:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)
    return below.rolling(n, min_periods=n).apply(_maxrun, raw=True).replace([np.inf, -np.inf], np.nan)


def f30dr_f30_drawdown_recovery_metrics_avg_uw_length_180d_base_v050_signal(closeadj):
    """Avg length of underwater runs in trailing 180d (DD>0 streaks)."""
    n = 180
    rmax = closeadj.rolling(n, min_periods=n).max()
    below = (closeadj < rmax - 1e-12).astype(float).where(~rmax.isna())

    def _avgrun(x):
        runs = []; cur = 0
        for v in x:
            if v >= 0.5:
                cur += 1
            else:
                if cur > 0:
                    runs.append(cur); cur = 0
        if cur > 0:
            runs.append(cur)
        return float(np.mean(runs)) if runs else 0.0
    return below.rolling(n, min_periods=n).apply(_avgrun, raw=True).replace([np.inf, -np.inf], np.nan)


# === DD/ATR magnitude (rolling ATR-normalized) =============================


def f30dr_f30_drawdown_recovery_metrics_maxdd_atr_60d_base_v051_signal(high, low, closeadj):
    """|min DD over 60d| * close / ATR(21). DD scale in ATR units."""
    n = 60
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    mdd = dd.rolling(n, min_periods=n).min().abs()
    pc = closeadj.shift(1)
    tr = pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.rolling(21, min_periods=21).mean()
    return (mdd * closeadj / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Drawup symmetric stats ================================================


def f30dr_f30_drawdown_recovery_metrics_drawup_skew_100d_base_v052_signal(closeadj):
    """Skew of drawup series (DU vs 100d rmin) over 100 bars."""
    n = 100
    du = closeadj / closeadj.rolling(n, min_periods=n).min() - 1.0
    return du.rolling(n, min_periods=n).skew().replace([np.inf, -np.inf], np.nan)


def f30dr_f30_drawdown_recovery_metrics_drawup_kurt_60d_base_v053_signal(closeadj):
    """Kurt of drawup series (DU vs 60d rmin) over 60 bars."""
    n = 60
    du = closeadj / closeadj.rolling(n, min_periods=n).min() - 1.0
    return du.rolling(n, min_periods=n).kurt().replace([np.inf, -np.inf], np.nan)


def f30dr_f30_drawdown_recovery_metrics_drawup_recovery_30d_base_v054_signal(closeadj):
    """Symmetric to recovery: how much of trailing 30d max drawup has been
    given back. 1 - DU / max(DU over 30d) (DU vs 30d rmin)."""
    n = 30
    du = closeadj / closeadj.rolling(n, min_periods=n).min() - 1.0
    maxdu = du.rolling(n, min_periods=n).max()
    return (1.0 - du / maxdu.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Bars in current DD ====================================================


def f30dr_f30_drawdown_recovery_metrics_uw_streak_now_70d_base_v055_signal(closeadj):
    """Length of current consecutive underwater streak (below 70d rmax)."""
    n = 70
    rmax = closeadj.rolling(n, min_periods=n).max()
    below = (closeadj < rmax - 1e-12).astype(float).where(~rmax.isna())
    out = pd.Series(np.nan, index=closeadj.index, dtype=float)
    cnt = np.nan
    bv = below.values
    for i in range(len(closeadj)):
        if not np.isfinite(bv[i]):
            continue
        if bv[i] >= 0.5:
            cnt = (cnt + 1.0) if np.isfinite(cnt) else 1.0
        else:
            cnt = 0.0
        out.iat[i] = cnt
    return out.replace([np.inf, -np.inf], np.nan)


# === DD/realized-vol Z-score ===============================================


def f30dr_f30_drawdown_recovery_metrics_dd_zscore_45d_base_v056_signal(closeadj):
    """Z-score of (DD vs 45d rmax) within trailing 45d window."""
    n = 45
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    mu = dd.rolling(n, min_periods=n).mean()
    sd = dd.rolling(n, min_periods=n).std()
    return ((dd - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === V-shape / U-shape recovery indicator ==================================


def f30dr_f30_drawdown_recovery_metrics_v_shape_30d_base_v057_signal(closeadj):
    """V-shape indicator: |DD30 - prior DD30(10d ago)| / (sum |DD30 changes| over 10d).
    High = sharp V-recovery; low = gradual U."""
    n = 30
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    direct = (dd - dd.shift(10)).abs()
    path = dd.diff().abs().rolling(10, min_periods=10).sum()
    return (direct / path.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === DD-correlation with vol ===============================================


def f30dr_f30_drawdown_recovery_metrics_corr_dd_vol_90d_base_v058_signal(closeadj):
    """90d rolling corr between |DD vs 90d rmax| and 10d realized vol."""
    n = 90
    dd_abs = (closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0).abs()
    rv = np.log(closeadj / closeadj.shift(1)).rolling(10, min_periods=10).std()
    return dd_abs.rolling(n, min_periods=n).corr(rv).replace([np.inf, -np.inf], np.nan)


# === Ulcer-style with normalized squared underwater ========================


def f30dr_f30_drawdown_recovery_metrics_uw_recovery_asymmetry_75d_base_v059_signal(closeadj):
    """Underwater-vs-recovery asymmetry: (UW-bars - recovery-bars) / 75
    where recovery-bars = bars in trailing 75 where DD(20) is increasing toward 0."""
    n = 75
    rmax = closeadj.rolling(n, min_periods=n).max()
    below = (closeadj < rmax - 1e-12).astype(float).where(~rmax.isna())
    dd = closeadj / closeadj.rolling(20, min_periods=20).max() - 1.0
    rec = ((dd.diff() > 0) & (dd < 0)).astype(float).where(~dd.diff().isna())
    return ((below.rolling(n, min_periods=n).sum() - rec.rolling(n, min_periods=n).sum()) / float(n)).replace([np.inf, -np.inf], np.nan)


# === Number of distinct DD episodes ========================================


def f30dr_f30_drawdown_recovery_metrics_dd_episode_count_120d_base_v060_signal(closeadj):
    """Count of distinct underwater episodes in trailing 120 bars
    (each contiguous below-high run = one episode)."""
    n = 120
    rmax = closeadj.rolling(n, min_periods=n).max()
    below = (closeadj < rmax - 1e-12).astype(float).where(~rmax.isna())

    def _episodes(x):
        c = 0; in_ep = False
        for v in x:
            if v >= 0.5:
                if not in_ep:
                    c += 1
                    in_ep = True
            else:
                in_ep = False
        return float(c)
    return below.rolling(n, min_periods=n).apply(_episodes, raw=True).replace([np.inf, -np.inf], np.nan)


# === DD percentile / rank within recent history ============================


def f30dr_f30_drawdown_recovery_metrics_dd_rank_252d_base_v061_signal(closeadj):
    """Percentile rank of current DD (vs 60d rmax) within trailing 252d."""
    n_dd = 60; n_rank = 252
    dd = closeadj / closeadj.rolling(n_dd, min_periods=n_dd).max() - 1.0
    return dd.rolling(n_rank, min_periods=n_rank).apply(
        lambda x: float((np.sum(x <= x[-1]) - 1) / max(1, (len(x) - 1))), raw=True
    ).replace([np.inf, -np.inf], np.nan)


# === Time-to-recovery dynamic / cyclical ====================================


def f30dr_f30_drawdown_recovery_metrics_recovery_lag_corr_80d_base_v062_signal(closeadj):
    """80d corr between DD(20) and DD(20) lagged 10d. Recovery serial correlation."""
    n_dd = 20; n_corr = 80
    dd = closeadj / closeadj.rolling(n_dd, min_periods=n_dd).max() - 1.0
    return dd.rolling(n_corr, min_periods=n_corr).corr(dd.shift(10)).replace([np.inf, -np.inf], np.nan)


# === DD-magnitude vs duration ratio ========================================


def f30dr_f30_drawdown_recovery_metrics_dd_per_uw_day_60d_base_v063_signal(closeadj):
    """|min DD over 60d| / (avg UW-bars-count over 60d). DD per day of pain."""
    n = 60
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    mdd = dd.rolling(n, min_periods=n).min().abs()
    rmax = closeadj.rolling(n, min_periods=n).max()
    below = (closeadj < rmax - 1e-12).astype(float).where(~rmax.isna())
    avg_below = below.rolling(n, min_periods=n).mean() * n
    return (mdd / avg_below.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Sigmoid of underwater days =============================================


def f30dr_f30_drawdown_recovery_metrics_sig_uw_days_100d_base_v064_signal(closeadj):
    """sigmoid((uw_days - 25) / 15). Bounded UW-duration signal vs 100d rmax."""
    n = 100
    rmax = closeadj.rolling(n, min_periods=n).max()
    at_high = (closeadj >= rmax).astype(float).where(~rmax.isna())
    out = pd.Series(np.nan, index=closeadj.index, dtype=float)
    cnt = np.nan
    av = at_high.values
    for i in range(len(closeadj)):
        if not np.isfinite(av[i]):
            continue
        if av[i] >= 0.5:
            cnt = 0.0
        else:
            cnt = (cnt + 1.0) if np.isfinite(cnt) else np.nan
        out.iat[i] = cnt
    return (1.0 / (1.0 + np.exp(-(out - 25.0) / 15.0))).replace([np.inf, -np.inf], np.nan)


# === Volume-weighted DD (volume during DD vs total volume) =================


def f30dr_f30_drawdown_recovery_metrics_uw_vol_frac_60d_base_v065_signal(closeadj, volume):
    """Fraction of trailing 60d volume that occurred while underwater (close<60d rmax)."""
    n = 60
    rmax = closeadj.rolling(n, min_periods=n).max()
    below = (closeadj < rmax - 1e-12).astype(float).where(~rmax.isna())
    uv = (below * volume).rolling(n, min_periods=n).sum()
    tv = volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return (uv / tv).replace([np.inf, -np.inf], np.nan)


# === DD-shape mean / median ratio ==========================================


def f30dr_f30_drawdown_recovery_metrics_dd_mean_median_ratio_75d_base_v066_signal(closeadj):
    """Mean(DD) / median(DD) over 75d. Skewness proxy of DD distribution."""
    n = 75
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    mn = dd.rolling(n, min_periods=n).mean()
    md = dd.rolling(n, min_periods=n).median()
    return (mn / md.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Drawup integral over N ================================================


def f30dr_f30_drawdown_recovery_metrics_drawup_integral_50d_base_v067_signal(closeadj):
    """Sum of drawups (DU vs 50d rmin) over 50 bars. Positive 'recovery area'."""
    n = 50
    du = closeadj / closeadj.rolling(n, min_periods=n).min() - 1.0
    return du.rolling(n, min_periods=n).sum().replace([np.inf, -np.inf], np.nan)


# === DD slope acceleration =================================================


def f30dr_f30_drawdown_recovery_metrics_dd_slope_streak_60d_base_v068_signal(closeadj):
    """Consecutive bars where DD(20) is increasing toward 0 (recovering streak)."""
    n_dd = 20
    dd = closeadj / closeadj.rolling(n_dd, min_periods=n_dd).max() - 1.0
    inc = (dd.diff() > 0).astype(float).where(~dd.diff().isna())
    out = pd.Series(np.nan, index=closeadj.index, dtype=float)
    cnt = np.nan
    iv = inc.values
    for i in range(len(closeadj)):
        if not np.isfinite(iv[i]):
            continue
        if iv[i] >= 0.5:
            cnt = (cnt + 1.0) if np.isfinite(cnt) else 1.0
        else:
            cnt = 0.0
        out.iat[i] = cnt
    return out.replace([np.inf, -np.inf], np.nan)


# === DD-magnitude scaled by elapsed time since trough ======================


def f30dr_f30_drawdown_recovery_metrics_dd_per_bar_since_trough_90d_base_v069_signal(closeadj):
    """|DD(90)| / (1 + bars since 90d-low). DD-magnitude / time elapsed since trough."""
    n = 90
    dd_abs = (closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0).abs()
    rmin = closeadj.rolling(n, min_periods=n).min()
    at_low = (closeadj <= rmin).astype(float).where(~rmin.isna())
    bars = pd.Series(np.nan, index=closeadj.index, dtype=float)
    cnt = np.nan
    av = at_low.values
    for i in range(len(closeadj)):
        if not np.isfinite(av[i]):
            continue
        if av[i] >= 0.5:
            cnt = 0.0
        else:
            cnt = (cnt + 1.0) if np.isfinite(cnt) else np.nan
        bars.iat[i] = cnt
    return (dd_abs / (bars + 1.0)).replace([np.inf, -np.inf], np.nan)


# === Sign-flips of DD-curve (oscillation between recovery/deepening) =======


def f30dr_f30_drawdown_recovery_metrics_dd_flip_rate_50d_base_v070_signal(closeadj):
    """Count of sign-flips of DD(30).diff() in trailing 50d / 50. Choppiness of DD curve."""
    n_dd = 30; n_rng = 50
    dd_d = (closeadj / closeadj.rolling(n_dd, min_periods=n_dd).max() - 1.0).diff()
    s = np.sign(dd_d)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return (flip.rolling(n_rng, min_periods=n_rng).sum() / float(n_rng)).replace([np.inf, -np.inf], np.nan)


# === DD-shape: arctan of slope =============================================


def f30dr_f30_drawdown_recovery_metrics_arctan_recovery_slope_45d_base_v071_signal(closeadj):
    """arctan of recovery slope per-bar: arctan((close - rmin45) / rmin45 / 45 * 100)."""
    n = 45
    rmin = closeadj.rolling(n, min_periods=n).min()
    sl = (closeadj - rmin) / rmin.replace(0.0, np.nan) / float(n) * 100.0
    return np.arctan(sl).replace([np.inf, -np.inf], np.nan)


# === Frequency of severe DDs ===============================================


def f30dr_f30_drawdown_recovery_metrics_severe_dd_count_252d_base_v072_signal(closeadj):
    """Count bars in 252d where DD(60) <= -10%."""
    n_dd = 60; n_rng = 252
    dd = closeadj / closeadj.rolling(n_dd, min_periods=n_dd).max() - 1.0
    flag = (dd <= -0.10).astype(float).where(~dd.isna())
    return flag.rolling(n_rng, min_periods=n_rng).sum().replace([np.inf, -np.inf], np.nan)


# === Days at new high inside N =============================================


def f30dr_f30_drawdown_recovery_metrics_dd_recoverability_index_140d_base_v073_signal(closeadj):
    """Mean per-bar recovery rate from local DD-trough: average of (close - 60d-rmin) / |DD(60)|
    over trailing 140d. Higher = better recoverability profile."""
    n_rng = 140
    rmin = closeadj.rolling(60, min_periods=60).min()
    rmax = closeadj.rolling(60, min_periods=60).max()
    dd_abs = (closeadj / rmax - 1.0).abs()
    rec = (closeadj - rmin) / (rmax - rmin).replace(0.0, np.nan) * (dd_abs > 0.001).astype(float)
    return rec.rolling(n_rng, min_periods=n_rng).mean().replace([np.inf, -np.inf], np.nan)


# === DD curvature norm (acceleration) =====================================


def f30dr_f30_drawdown_recovery_metrics_dd_accel_norm_60d_base_v074_signal(closeadj):
    """DD(60) curvature / (10d std of DD(60))."""
    n = 60
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    c = dd - 2.0 * dd.shift(5) + dd.shift(10)
    sig = dd.rolling(10, min_periods=10).std()
    return (c / sig.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Last DD severity vs current ==========================================


def f30dr_f30_drawdown_recovery_metrics_dd_now_vs_max_120d_base_v075_signal(closeadj):
    """Current DD(120) / |min DD(120) over 120d|. How close to worst-historical-DD."""
    n = 120
    dd = closeadj / closeadj.rolling(n, min_periods=n).max() - 1.0
    mdd = dd.rolling(n, min_periods=n).min()
    return (dd / mdd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f30_drawdown_recovery_metrics_base_001_075_REGISTRY = {
    "f30dr_f30_drawdown_recovery_metrics_dd_20d_base_v001_signal": {"inputs": ["close"], "func": f30dr_f30_drawdown_recovery_metrics_dd_20d_base_v001_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_63d_base_v002_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_63d_base_v002_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_252d_base_v003_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_252d_base_v003_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_504d_base_v004_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_504d_base_v004_signal},
    "f30dr_f30_drawdown_recovery_metrics_maxdd_30d_base_v005_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_maxdd_30d_base_v005_signal},
    "f30dr_f30_drawdown_recovery_metrics_maxdd_126d_base_v006_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_maxdd_126d_base_v006_signal},
    "f30dr_f30_drawdown_recovery_metrics_avgdd_60d_base_v007_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_avgdd_60d_base_v007_signal},
    "f30dr_f30_drawdown_recovery_metrics_uw_days_50d_base_v008_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_uw_days_50d_base_v008_signal},
    "f30dr_f30_drawdown_recovery_metrics_uw_days_200d_base_v009_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_uw_days_200d_base_v009_signal},
    "f30dr_f30_drawdown_recovery_metrics_uw_integral_40d_base_v010_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_uw_integral_40d_base_v010_signal},
    "f30dr_f30_drawdown_recovery_metrics_uw_integral_120d_base_v011_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_uw_integral_120d_base_v011_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_emerge_decay_45d_base_v012_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_emerge_decay_45d_base_v012_signal},
    "f30dr_f30_drawdown_recovery_metrics_recovery_ratio_60d_base_v013_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_recovery_ratio_60d_base_v013_signal},
    "f30dr_f30_drawdown_recovery_metrics_recovery_slope_30d_base_v014_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_recovery_slope_30d_base_v014_signal},
    "f30dr_f30_drawdown_recovery_metrics_bars_since_trough_90d_base_v015_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_bars_since_trough_90d_base_v015_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_std_45d_base_v016_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_std_45d_base_v016_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_count_5pct_100d_base_v017_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_count_5pct_100d_base_v017_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_rank_120d_base_v018_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_rank_120d_base_v018_signal},
    "f30dr_f30_drawdown_recovery_metrics_drawup_20d_base_v019_signal": {"inputs": ["close"], "func": f30dr_f30_drawdown_recovery_metrics_drawup_20d_base_v019_signal},
    "f30dr_f30_drawdown_recovery_metrics_drawup_120d_base_v020_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_drawup_120d_base_v020_signal},
    "f30dr_f30_drawdown_recovery_metrics_max_drawup_50d_base_v021_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_max_drawup_50d_base_v021_signal},
    "f30dr_f30_drawdown_recovery_metrics_drawup_to_drawdown_ratio_80d_base_v022_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_drawup_to_drawdown_ratio_80d_base_v022_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_skew_75d_base_v023_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_skew_75d_base_v023_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_kurt_150d_base_v024_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_kurt_150d_base_v024_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_mad_std_60d_base_v025_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_mad_std_60d_base_v025_signal},
    "f30dr_f30_drawdown_recovery_metrics_ulcer_30d_base_v026_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_ulcer_30d_base_v026_signal},
    "f30dr_f30_drawdown_recovery_metrics_ulcer_pain_ratio_30_120_base_v027_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_ulcer_pain_ratio_30_120_base_v027_signal},
    "f30dr_f30_drawdown_recovery_metrics_pain_ratio_60d_base_v028_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_pain_ratio_60d_base_v028_signal},
    "f30dr_f30_drawdown_recovery_metrics_calmar_252d_base_v029_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_calmar_252d_base_v029_signal},
    "f30dr_f30_drawdown_recovery_metrics_sterling_120d_base_v030_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_sterling_120d_base_v030_signal},
    "f30dr_f30_drawdown_recovery_metrics_uw_frac_40d_base_v031_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_uw_frac_40d_base_v031_signal},
    "f30dr_f30_drawdown_recovery_metrics_uw_frac_180d_base_v032_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_uw_frac_180d_base_v032_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_over_atr_30d_base_v033_signal": {"inputs": ["high", "low", "closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_over_atr_30d_base_v033_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_over_realvol_90d_base_v034_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_over_realvol_90d_base_v034_signal},
    "f30dr_f30_drawdown_recovery_metrics_in_dd_5pct_30d_base_v035_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_in_dd_5pct_30d_base_v035_signal},
    "f30dr_f30_drawdown_recovery_metrics_severe_dd_20pct_252d_base_v036_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_severe_dd_20pct_252d_base_v036_signal},
    "f30dr_f30_drawdown_recovery_metrics_at_new_high_45d_base_v037_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_at_new_high_45d_base_v037_signal},
    "f30dr_f30_drawdown_recovery_metrics_arctan_dd_50d_base_v038_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_arctan_dd_50d_base_v038_signal},
    "f30dr_f30_drawdown_recovery_metrics_tanh_uw_frac_80d_base_v039_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_tanh_uw_frac_80d_base_v039_signal},
    "f30dr_f30_drawdown_recovery_metrics_sigmoid_dd_rank_60d_base_v040_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_sigmoid_dd_rank_60d_base_v040_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_slope_30d_base_v041_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_slope_30d_base_v041_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_curvature_90d_base_v042_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_curvature_90d_base_v042_signal},
    "f30dr_f30_drawdown_recovery_metrics_shortdd_longdd_ratio_base_v043_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_shortdd_longdd_ratio_base_v043_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_diff_45_180d_base_v044_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_diff_45_180d_base_v044_signal},
    "f30dr_f30_drawdown_recovery_metrics_recovery_efficiency_60d_base_v045_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_recovery_efficiency_60d_base_v045_signal},
    "f30dr_f30_drawdown_recovery_metrics_recovery_speed_30d_base_v046_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_recovery_speed_30d_base_v046_signal},
    "f30dr_f30_drawdown_recovery_metrics_cum_dd_50d_base_v047_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_cum_dd_50d_base_v047_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_weighted_return_75d_base_v048_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_weighted_return_75d_base_v048_signal},
    "f30dr_f30_drawdown_recovery_metrics_max_uw_length_120d_base_v049_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_max_uw_length_120d_base_v049_signal},
    "f30dr_f30_drawdown_recovery_metrics_avg_uw_length_180d_base_v050_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_avg_uw_length_180d_base_v050_signal},
    "f30dr_f30_drawdown_recovery_metrics_maxdd_atr_60d_base_v051_signal": {"inputs": ["high", "low", "closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_maxdd_atr_60d_base_v051_signal},
    "f30dr_f30_drawdown_recovery_metrics_drawup_skew_100d_base_v052_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_drawup_skew_100d_base_v052_signal},
    "f30dr_f30_drawdown_recovery_metrics_drawup_kurt_60d_base_v053_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_drawup_kurt_60d_base_v053_signal},
    "f30dr_f30_drawdown_recovery_metrics_drawup_recovery_30d_base_v054_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_drawup_recovery_30d_base_v054_signal},
    "f30dr_f30_drawdown_recovery_metrics_uw_streak_now_70d_base_v055_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_uw_streak_now_70d_base_v055_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_zscore_45d_base_v056_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_zscore_45d_base_v056_signal},
    "f30dr_f30_drawdown_recovery_metrics_v_shape_30d_base_v057_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_v_shape_30d_base_v057_signal},
    "f30dr_f30_drawdown_recovery_metrics_corr_dd_vol_90d_base_v058_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_corr_dd_vol_90d_base_v058_signal},
    "f30dr_f30_drawdown_recovery_metrics_uw_recovery_asymmetry_75d_base_v059_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_uw_recovery_asymmetry_75d_base_v059_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_episode_count_120d_base_v060_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_episode_count_120d_base_v060_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_rank_252d_base_v061_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_rank_252d_base_v061_signal},
    "f30dr_f30_drawdown_recovery_metrics_recovery_lag_corr_80d_base_v062_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_recovery_lag_corr_80d_base_v062_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_per_uw_day_60d_base_v063_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_per_uw_day_60d_base_v063_signal},
    "f30dr_f30_drawdown_recovery_metrics_sig_uw_days_100d_base_v064_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_sig_uw_days_100d_base_v064_signal},
    "f30dr_f30_drawdown_recovery_metrics_uw_vol_frac_60d_base_v065_signal": {"inputs": ["closeadj", "volume"], "func": f30dr_f30_drawdown_recovery_metrics_uw_vol_frac_60d_base_v065_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_mean_median_ratio_75d_base_v066_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_mean_median_ratio_75d_base_v066_signal},
    "f30dr_f30_drawdown_recovery_metrics_drawup_integral_50d_base_v067_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_drawup_integral_50d_base_v067_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_slope_streak_60d_base_v068_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_slope_streak_60d_base_v068_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_per_bar_since_trough_90d_base_v069_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_per_bar_since_trough_90d_base_v069_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_flip_rate_50d_base_v070_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_flip_rate_50d_base_v070_signal},
    "f30dr_f30_drawdown_recovery_metrics_arctan_recovery_slope_45d_base_v071_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_arctan_recovery_slope_45d_base_v071_signal},
    "f30dr_f30_drawdown_recovery_metrics_severe_dd_count_252d_base_v072_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_severe_dd_count_252d_base_v072_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_recoverability_index_140d_base_v073_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_recoverability_index_140d_base_v073_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_accel_norm_60d_base_v074_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_accel_norm_60d_base_v074_signal},
    "f30dr_f30_drawdown_recovery_metrics_dd_now_vs_max_120d_base_v075_signal": {"inputs": ["closeadj"], "func": f30dr_f30_drawdown_recovery_metrics_dd_now_vs_max_120d_base_v075_signal},
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
    for name, entry in f30_drawdown_recovery_metrics_base_001_075_REGISTRY.items():
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
