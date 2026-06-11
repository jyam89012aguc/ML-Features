"""f18_parkinson_garman_klass_estimators base features 076-150.

Continuation file. Each feature must be structurally distinct from
base_001_075 (no shared formula up to a window change). Same domain:
Parkinson/Garman-Klass/Rogers-Satchell/Yang-Zhang/bipower/ATR vol
estimators using H/L/O/C beyond close-to-close.

NaN policy: never fillna(<value>); only final replace([inf,-inf],nan).
Window > 21d uses closeadj; <= 21d uses close.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Features 076-150 -- structurally distinct from base_001_075
# ---------------------------------------------------------------------------


def f18pg_f18_parkinson_garman_klass_estimators_park_42d_base_v076_signal(closeadj, high, low):
    """Parkinson vol at 42d (between 21 and 63 -- distinct window)."""
    _ = closeadj
    n = 42
    r = (np.log(high / low) ** 2).rolling(n, min_periods=n).mean()
    return ((r / (4.0 * np.log(2.0))) ** 0.5).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_park_120d_base_v077_signal(closeadj, high, low):
    """Parkinson vol at 120d -- semi-annual range estimator."""
    _ = closeadj
    n = 120
    r = (np.log(high / low) ** 2).rolling(n, min_periods=n).mean()
    return ((r / (4.0 * np.log(2.0))) ** 0.5).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_gk_42d_base_v078_signal(open, high, low, closeadj):
    """Garman-Klass vol 42d."""
    n = 42
    hl = 0.5 * np.log(high / low) ** 2
    co = (2.0 * np.log(2.0) - 1.0) * np.log(closeadj / open) ** 2
    var = (hl - co).rolling(n, min_periods=n).mean()
    return (var.clip(lower=0.0) ** 0.5).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_rs_120d_base_v079_signal(open, high, low, closeadj):
    """Rogers-Satchell vol 120d."""
    n = 120
    rs = np.log(high / closeadj) * np.log(high / open) + np.log(low / closeadj) * np.log(low / open)
    var = rs.rolling(n, min_periods=n).mean()
    return (var.clip(lower=0.0) ** 0.5).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_yz_42d_base_v080_signal(open, high, low, closeadj):
    """Yang-Zhang vol 42d."""
    n = 42
    on = np.log(open / closeadj.shift(1))
    oc = np.log(closeadj / open)
    var_on = on.rolling(n, min_periods=n).var(ddof=1)
    var_oc = oc.rolling(n, min_periods=n).var(ddof=1)
    rs = np.log(high / closeadj) * np.log(high / open) + np.log(low / closeadj) * np.log(low / open)
    var_rs = rs.rolling(n, min_periods=n).mean()
    k = 0.34 / (1.34 + (n + 1.0) / (n - 1.0))
    var = var_on + k * var_oc + (1.0 - k) * var_rs
    return (var.clip(lower=0.0) ** 0.5).replace([np.inf, -np.inf], np.nan)


# === Cross-estimator differentials (structurally distinct from file 1 ratios) ===


def f18pg_f18_parkinson_garman_klass_estimators_park_rs_signed_diff_60d_base_v081_signal(open, high, low, closeadj):
    """(Parkinson(60) - RS(60)) -- absolute drift bias indicator."""
    n = 60
    park = ((np.log(high / low) ** 2).rolling(n, min_periods=n).mean() / (4.0 * np.log(2.0))) ** 0.5
    rs_inner = np.log(high / closeadj) * np.log(high / open) + np.log(low / closeadj) * np.log(low / open)
    rs = rs_inner.rolling(n, min_periods=n).mean().clip(lower=0.0) ** 0.5
    return (park - rs).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_gk_rs_log_42d_base_v082_signal(open, high, low, closeadj):
    """log(GK(42) / RS(42)) -- log ratio, drift-bias proxy at 42d."""
    n = 42
    hl = 0.5 * np.log(high / low) ** 2
    co = (2.0 * np.log(2.0) - 1.0) * np.log(closeadj / open) ** 2
    gk = ((hl - co).rolling(n, min_periods=n).mean().clip(lower=0.0)) ** 0.5
    rs_inner = np.log(high / closeadj) * np.log(high / open) + np.log(low / closeadj) * np.log(low / open)
    rs = rs_inner.rolling(n, min_periods=n).mean().clip(lower=0.0) ** 0.5
    return np.log(gk / rs.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_yz_gk_diff_30d_base_v083_signal(open, high, low, closeadj):
    """YZ(30) - GK(30) -- effect of overnight + drift adjustment at 30d."""
    n = 30
    on = np.log(open / closeadj.shift(1))
    oc = np.log(closeadj / open)
    von = on.rolling(n, min_periods=n).var(ddof=1)
    voc = oc.rolling(n, min_periods=n).var(ddof=1)
    rs_inner = np.log(high / closeadj) * np.log(high / open) + np.log(low / closeadj) * np.log(low / open)
    vrs = rs_inner.rolling(n, min_periods=n).mean()
    k = 0.34 / (1.34 + (n + 1.0) / (n - 1.0))
    yz = (von + k * voc + (1.0 - k) * vrs).clip(lower=0.0) ** 0.5
    hl = 0.5 * np.log(high / low) ** 2
    co = (2.0 * np.log(2.0) - 1.0) * np.log(closeadj / open) ** 2
    gk = ((hl - co).rolling(n, min_periods=n).mean().clip(lower=0.0)) ** 0.5
    return (yz - gk).replace([np.inf, -np.inf], np.nan)


# === Different transformation classes ===


def f18pg_f18_parkinson_garman_klass_estimators_park_centered_diff_5_42_base_v084_signal(closeadj, high, low):
    """(Parkinson(5) - Parkinson(42)) / Parkinson(42) -- short-minus-medium normalized spread.

    Structurally distinct from raw 42d level: a normalized cross-window
    differential that suppresses absolute drift and emphasises term-
    structure inversion."""
    _ = closeadj
    p5 = ((np.log(high / low) ** 2).rolling(5, min_periods=5).mean() / (4.0 * np.log(2.0))) ** 0.5
    p42 = ((np.log(high / low) ** 2).rolling(42, min_periods=42).mean() / (4.0 * np.log(2.0))) ** 0.5
    return ((p5 - p42) / p42.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_park_inverse_60d_base_v085_signal(closeadj, high, low):
    """1 / Parkinson(60) -- reciprocal vol; nonlinear in level."""
    _ = closeadj
    n = 60
    r = (np.log(high / low) ** 2).rolling(n, min_periods=n).mean()
    sig = (r / (4.0 * np.log(2.0))) ** 0.5
    return (1.0 / sig.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_gk_negativity_share_42d_base_v086_signal(open, high, low, closeadj):
    """Fraction of last 42 days where GK daily contribution is negative.

    GK daily = 0.5*ln(H/L)^2 - (2ln2-1)*ln(C/O)^2 can be negative when
    intraday C/O move exceeds range (impossible mathematically but the
    sample-estimator can produce it). Captures days dominated by large
    open-to-close moves relative to intraday range -- a unique structural
    feature."""
    _ = closeadj
    gk_daily = 0.5 * np.log(high / low) ** 2 - (2.0 * np.log(2.0) - 1.0) * np.log(closeadj / open) ** 2
    flag = (gk_daily < 0.0).astype(float).where(gk_daily.notna())
    return flag.rolling(42, min_periods=42).mean().replace([np.inf, -np.inf], np.nan)


# === Term-structure differences (>2 windows) ===


def f18pg_f18_parkinson_garman_klass_estimators_park_term_21_120_base_v087_signal(closeadj, high, low):
    """Parkinson(21) - Parkinson(120) -- short-vs-long absolute spread."""
    _ = closeadj
    p21 = ((np.log(high / low) ** 2).rolling(21, min_periods=21).mean() / (4.0 * np.log(2.0))) ** 0.5
    p120 = ((np.log(high / low) ** 2).rolling(120, min_periods=120).mean() / (4.0 * np.log(2.0))) ** 0.5
    return (p21 - p120).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_gk_term_log_30_120_base_v088_signal(open, high, low, closeadj):
    """log(GK(30) / GK(120))."""
    hl = 0.5 * np.log(high / low) ** 2
    co = (2.0 * np.log(2.0) - 1.0) * np.log(closeadj / open) ** 2
    g30 = ((hl - co).rolling(30, min_periods=30).mean().clip(lower=0.0)) ** 0.5
    g120 = ((hl - co).rolling(120, min_periods=120).mean().clip(lower=0.0)) ** 0.5
    return np.log(g30 / g120.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Slope on different estimators with different lags ===


def f18pg_f18_parkinson_garman_klass_estimators_rs_slope_42d_base_v089_signal(open, high, low, closeadj):
    """RS(21) slope over 42d step."""
    n = 21
    rs_inner = np.log(high / closeadj) * np.log(high / open) + np.log(low / closeadj) * np.log(low / open)
    rs = rs_inner.rolling(n, min_periods=n).mean().clip(lower=0.0) ** 0.5
    return (rs - rs.shift(42)).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_atr_slope_30d_base_v090_signal(high, low, closeadj):
    """ATR(30)/closeadj slope over 30d -- TR-based momentum of vol."""
    n = 30
    tr = pd.concat([high - low, (high - closeadj.shift(1)).abs(), (low - closeadj.shift(1)).abs()], axis=1).max(axis=1)
    base = tr.rolling(n, min_periods=n).mean() / closeadj
    return (base - base.shift(30)).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_yz_accel_42d_base_v091_signal(open, high, low, closeadj):
    """YZ(21) acceleration over 42-day step (2nd diff)."""
    n = 21
    on = np.log(open / closeadj.shift(1))
    oc = np.log(closeadj / open)
    von = on.rolling(n, min_periods=n).var(ddof=1)
    voc = oc.rolling(n, min_periods=n).var(ddof=1)
    rs_inner = np.log(high / closeadj) * np.log(high / open) + np.log(low / closeadj) * np.log(low / open)
    vrs = rs_inner.rolling(n, min_periods=n).mean()
    k = 0.34 / (1.34 + (n + 1.0) / (n - 1.0))
    yz = (von + k * voc + (1.0 - k) * vrs).clip(lower=0.0) ** 0.5
    return (yz - 2.0 * yz.shift(21) + yz.shift(42)).replace([np.inf, -np.inf], np.nan)


# === Multi-estimator dispersion at different windows ===


def f18pg_f18_parkinson_garman_klass_estimators_gk_park_rank_diff_63d_base_v092_signal(open, high, low, closeadj):
    """63d pct-rank of GK(21) minus 63d pct-rank of Parkinson(21) -- rank-space estimator-relative regime.

    Rank-space spread of two estimators evaluated within the same window.
    Bounded in [-1, 1] and structurally distinct from absolute std-of-
    estimator dispersion."""
    park = ((np.log(high / low) ** 2).rolling(21, min_periods=21).mean() / (4.0 * np.log(2.0))) ** 0.5
    hl = 0.5 * np.log(high / low) ** 2
    co = (2.0 * np.log(2.0) - 1.0) * np.log(closeadj / open) ** 2
    gk = ((hl - co).rolling(21, min_periods=21).mean().clip(lower=0.0)) ** 0.5
    rg = gk.rolling(63, min_periods=32).rank(pct=True)
    rp = park.rolling(63, min_periods=32).rank(pct=True)
    return (rg - rp).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_estimator_cv_60d_base_v093_signal(open, high, low, closeadj):
    """Coefficient of variation: std/mean across {Park, GK, RS, ATR/close} at 60d."""
    n = 60
    park = ((np.log(high / low) ** 2).rolling(n, min_periods=n).mean() / (4.0 * np.log(2.0))) ** 0.5
    hl = 0.5 * np.log(high / low) ** 2
    co = (2.0 * np.log(2.0) - 1.0) * np.log(closeadj / open) ** 2
    gk = ((hl - co).rolling(n, min_periods=n).mean().clip(lower=0.0)) ** 0.5
    rs_inner = np.log(high / closeadj) * np.log(high / open) + np.log(low / closeadj) * np.log(low / open)
    rs = rs_inner.rolling(n, min_periods=n).mean().clip(lower=0.0) ** 0.5
    tr = pd.concat([high - low, (high - closeadj.shift(1)).abs(), (low - closeadj.shift(1)).abs()], axis=1).max(axis=1)
    atr_rel = tr.rolling(n, min_periods=n).mean() / closeadj
    stk = pd.concat([park, gk, rs, atr_rel], axis=1)
    return (stk.std(axis=1, ddof=0) / stk.mean(axis=1).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Estimator regime detection ===


def f18pg_f18_parkinson_garman_klass_estimators_park_above_long_count_60d_base_v094_signal(closeadj, high, low):
    """Count of days in last 60d where Parkinson(5) > Parkinson(60)."""
    _ = closeadj
    p5 = ((np.log(high / low) ** 2).rolling(5, min_periods=5).mean() / (4.0 * np.log(2.0))) ** 0.5
    p60 = ((np.log(high / low) ** 2).rolling(60, min_periods=60).mean() / (4.0 * np.log(2.0))) ** 0.5
    flag = (p5 > p60).astype(float).where(p5.notna() & p60.notna())
    return flag.rolling(60, min_periods=60).sum().replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_rs_high_low_streak_diff_base_v095_signal(open, high, low, closeadj):
    """High streak (RS above q90) minus low streak (RS below q10) at 252d."""
    n = 30
    rs_inner = np.log(high / closeadj) * np.log(high / open) + np.log(low / closeadj) * np.log(low / open)
    rs = rs_inner.rolling(n, min_periods=n).mean().clip(lower=0.0) ** 0.5
    q90 = rs.rolling(252, min_periods=126).quantile(0.9)
    q10 = rs.rolling(252, min_periods=126).quantile(0.1)
    fh = (rs > q90).astype(float).where(rs.notna() & q90.notna())
    fl = (rs < q10).astype(float).where(rs.notna() & q10.notna())
    out = pd.Series(np.nan, index=rs.index, dtype=float)
    sh = 0.0; sl = 0.0
    fhv = fh.values; flv = fl.values
    for i in range(len(rs)):
        if not (np.isfinite(fhv[i]) and np.isfinite(flv[i])):
            out.iat[i] = np.nan
            continue
        sh = (sh + 1.0) if fhv[i] > 0.5 else 0.0
        sl = (sl + 1.0) if flv[i] > 0.5 else 0.0
        out.iat[i] = sh - sl
    return out.replace([np.inf, -np.inf], np.nan)


# === Range vs return scatter ===


def f18pg_f18_parkinson_garman_klass_estimators_logrange_realized_corr_60d_base_v096_signal(close, high, low):
    """60d rolling correlation between ln(H/L) and |close-to-close return|."""
    lr = np.log(high / low)
    ar = np.log(close / close.shift(1)).abs()
    return lr.rolling(60, min_periods=30).corr(ar).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_park_realized_corr_120d_base_v097_signal(closeadj, high, low):
    """120d rolling correlation between log Parkinson(5) and log realized(5)."""
    park5 = ((np.log(high / low) ** 2).rolling(5, min_periods=5).mean() / (4.0 * np.log(2.0))) ** 0.5
    r2 = np.log(closeadj / closeadj.shift(1)) ** 2
    realized5 = r2.rolling(5, min_periods=5).mean() ** 0.5
    return np.log(park5.replace(0.0, np.nan)).rolling(120, min_periods=60).corr(np.log(realized5.replace(0.0, np.nan))).replace([np.inf, -np.inf], np.nan)


# === Conditional / regime features ===


def f18pg_f18_parkinson_garman_klass_estimators_overnight_share_pctrank_120d_base_v098_signal(open, high, low, closeadj):
    """120d percentile rank of overnight-variance share in YZ(30).

    Replaces a constant-on-synthetic park>yz flag with a percentile-rank
    feature: ranks the overnight component's share of total YZ variance
    against its own 120-day history."""
    n = 30
    on = np.log(open / closeadj.shift(1))
    oc = np.log(closeadj / open)
    von = on.rolling(n, min_periods=n).var(ddof=1)
    voc = oc.rolling(n, min_periods=n).var(ddof=1)
    rs_inner = np.log(high / closeadj) * np.log(high / open) + np.log(low / closeadj) * np.log(low / open)
    vrs = rs_inner.rolling(n, min_periods=n).mean()
    k = 0.34 / (1.34 + (n + 1.0) / (n - 1.0))
    yz_var = (von + k * voc + (1.0 - k) * vrs).clip(lower=0.0)
    share = von / yz_var.replace(0.0, np.nan)
    return share.rolling(120, min_periods=60).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_gk_above_park_streak_base_v099_signal(open, high, low, close):
    """Streak of consecutive days GK(21) > Parkinson(21)."""
    n = 21
    hl = 0.5 * np.log(high / low) ** 2
    co = (2.0 * np.log(2.0) - 1.0) * np.log(close / open) ** 2
    gk = ((hl - co).rolling(n, min_periods=n).mean().clip(lower=0.0)) ** 0.5
    park = ((np.log(high / low) ** 2).rolling(n, min_periods=n).mean() / (4.0 * np.log(2.0))) ** 0.5
    flag = (gk > park).astype(float).where(gk.notna() & park.notna())
    out = pd.Series(np.nan, index=gk.index, dtype=float)
    streak = np.nan
    fv = flag.values
    for i in range(len(gk)):
        if np.isnan(fv[i]):
            out.iat[i] = np.nan
            continue
        if fv[i] > 0.5:
            streak = (streak + 1.0) if np.isfinite(streak) else 1.0
        else:
            streak = 0.0
        out.iat[i] = streak
    return out.replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_dayssince_atr_high_252d_base_v100_signal(high, low, closeadj):
    """Days since ATR(21)/closeadj > 252d 90th pct."""
    tr = pd.concat([high - low, (high - closeadj.shift(1)).abs(), (low - closeadj.shift(1)).abs()], axis=1).max(axis=1)
    base = tr.rolling(21, min_periods=21).mean() / closeadj
    q = base.rolling(252, min_periods=126).quantile(0.9)
    flag = (base > q).astype(float).where(base.notna() & q.notna())
    out = pd.Series(np.nan, index=base.index, dtype=float)
    cnt = np.nan
    fv = flag.values
    for i in range(len(base)):
        if np.isnan(fv[i]):
            out.iat[i] = np.nan
            continue
        if fv[i] > 0.5:
            cnt = 0.0
        elif np.isfinite(cnt):
            cnt = cnt + 1.0
        out.iat[i] = cnt
    return out.replace([np.inf, -np.inf], np.nan)


# === Distribution moments of OHLC vol components ===


def f18pg_f18_parkinson_garman_klass_estimators_logrange_mean_252d_base_v101_signal(closeadj, high, low):
    """Mean of ln(H/L) over 252d -- annual log range."""
    _ = closeadj
    return np.log(high / low).rolling(252, min_periods=126).mean().replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_logrange_skew_120d_base_v102_signal(high, low):
    """Skew of ln(H/L) over 120d."""
    return np.log(high / low).rolling(120, min_periods=60).skew().replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_logrange_kurt_120d_base_v103_signal(high, low):
    """Kurtosis of ln(H/L) over 120d."""
    return np.log(high / low).rolling(120, min_periods=60).kurt().replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_oc_log_kurt_120d_base_v104_signal(open, closeadj):
    """Kurtosis of ln(C/O) intraday over 120d."""
    return np.log(closeadj / open).rolling(120, min_periods=60).kurt().replace([np.inf, -np.inf], np.nan)


# === Bipower / Realized variations ===


def f18pg_f18_parkinson_garman_klass_estimators_bipower_42d_base_v105_signal(closeadj):
    """Bipower variation sqrt-sum over 42d."""
    r = np.log(closeadj / closeadj.shift(1)).abs()
    bp = r * r.shift(1) * (np.pi / 2.0)
    return (bp.rolling(42, min_periods=42).sum() ** 0.5).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_jump_share_21d_base_v106_signal(close):
    """Jump share = max(0, 1 - bipower/realized) over 21d."""
    r = np.log(close / close.shift(1))
    bp = r.abs() * r.abs().shift(1) * (np.pi / 2.0)
    bp_sum = bp.rolling(21, min_periods=21).sum()
    rv_sum = (r ** 2).rolling(21, min_periods=21).sum()
    ratio = bp_sum / rv_sum.replace(0.0, np.nan)
    return (1.0 - ratio).clip(lower=0.0).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_bipower_park_diff_30d_base_v107_signal(closeadj, high, low):
    """Bipower(30) - Parkinson(30)*sqrt(30) -- absolute gap, jump-robust vs range."""
    n = 30
    r = np.log(closeadj / closeadj.shift(1)).abs()
    bp = r * r.shift(1) * (np.pi / 2.0)
    bipow = bp.rolling(n, min_periods=n).sum() ** 0.5
    park = ((np.log(high / low) ** 2).rolling(n, min_periods=n).mean() / (4.0 * np.log(2.0))) ** 0.5 * (n ** 0.5)
    return (bipow - park).replace([np.inf, -np.inf], np.nan)


# === ATR variations ===


def f18pg_f18_parkinson_garman_klass_estimators_atr_ema_60d_base_v108_signal(high, low, closeadj):
    """EMA(span=60) of true range / closeadj."""
    tr = pd.concat([high - low, (high - closeadj.shift(1)).abs(), (low - closeadj.shift(1)).abs()], axis=1).max(axis=1)
    return (tr.ewm(span=60, adjust=False, min_periods=60).mean() / closeadj).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_atr_pct_change_30d_base_v109_signal(high, low, closeadj):
    """30d percentage change in ATR(14)/closeadj."""
    tr = pd.concat([high - low, (high - closeadj.shift(1)).abs(), (low - closeadj.shift(1)).abs()], axis=1).max(axis=1)
    base = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean() / closeadj
    return ((base / base.shift(30)) - 1.0).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_truerange_gap_share_60d_base_v110_signal(high, low, closeadj):
    """Mean of max(|H-prev_C|, |L-prev_C|) / (H-L) over 60d -- overnight gap share of true range."""
    gap = pd.concat([(high - closeadj.shift(1)).abs(), (low - closeadj.shift(1)).abs()], axis=1).max(axis=1)
    return (gap / (high - low).replace(0.0, np.nan)).rolling(60, min_periods=30).mean().replace([np.inf, -np.inf], np.nan)


# === Spread between range and absolute return ===


def f18pg_f18_parkinson_garman_klass_estimators_range_vs_absret_5d_base_v111_signal(close, high, low):
    """ln(H/L) - |ln(C/C-1)| smoothed 5d -- single-bar range vs return."""
    n = 5
    diff = np.log(high / low) - np.log(close / close.shift(1)).abs()
    return diff.rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_efficiency_30d_base_v112_signal(closeadj, high, low):
    """|ln(C/C-30)| / sum(ln(H/L)) -- efficiency ratio over 30d range estimate."""
    n = 30
    net = np.log(closeadj / closeadj.shift(n)).abs()
    path = np.log(high / low).rolling(n, min_periods=n).sum()
    return (net / path.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Cross-component decompositions ===


def f18pg_f18_parkinson_garman_klass_estimators_hl_sq_share_in_gk_30d_base_v113_signal(open, high, low, closeadj):
    """0.5*ln(H/L)^2 component / GK variance -- share of GK from range part at 30d."""
    n = 30
    hl_part = (0.5 * np.log(high / low) ** 2).rolling(n, min_periods=n).mean()
    hl = 0.5 * np.log(high / low) ** 2
    co = (2.0 * np.log(2.0) - 1.0) * np.log(closeadj / open) ** 2
    gk_var = (hl - co).rolling(n, min_periods=n).mean()
    return (hl_part / gk_var.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_co_sq_in_park_42d_base_v114_signal(closeadj, open, high, low):
    """mean(ln(C/O)^2) / Parkinson(42) variance -- intraday move share."""
    n = 42
    co_sq = (np.log(closeadj / open) ** 2).rolling(n, min_periods=n).mean()
    park_var = (np.log(high / low) ** 2).rolling(n, min_periods=n).mean() / (4.0 * np.log(2.0))
    return (co_sq / park_var.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Sign / discrete indicators ===


def f18pg_f18_parkinson_garman_klass_estimators_sign_park_change_30d_base_v115_signal(closeadj, high, low):
    """sign(Parkinson(21) - Parkinson(21).shift(30))."""
    _ = closeadj
    p = ((np.log(high / low) ** 2).rolling(21, min_periods=21).mean() / (4.0 * np.log(2.0))) ** 0.5
    return np.sign(p - p.shift(30)).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_sign_gk_minus_park_42d_base_v116_signal(open, high, low, closeadj):
    """sign(GK(42) - Parkinson(42)) -- which estimator is higher."""
    n = 42
    hl = 0.5 * np.log(high / low) ** 2
    co = (2.0 * np.log(2.0) - 1.0) * np.log(closeadj / open) ** 2
    gk = ((hl - co).rolling(n, min_periods=n).mean().clip(lower=0.0)) ** 0.5
    park = ((np.log(high / low) ** 2).rolling(n, min_periods=n).mean() / (4.0 * np.log(2.0))) ** 0.5
    return np.sign(gk - park).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_atr_park_logratio_60d_base_v117_signal(high, low, closeadj):
    """60d mean of log(ATR(14)/closeadj / Parkinson(14)) -- continuous TR-vs-range gap.

    Continuous replacement for a count-of-days flag that was identically
    True on synthetic data (ATR/close picks up overnight gaps + true range
    which strictly dominate Parkinson range-only). The 60d-averaged log
    ratio preserves the same "ATR-vs-Parkinson regime" signal."""
    tr = pd.concat([high - low, (high - closeadj.shift(1)).abs(), (low - closeadj.shift(1)).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean() / closeadj
    park = ((np.log(high / low) ** 2).rolling(14, min_periods=14).mean() / (4.0 * np.log(2.0))) ** 0.5
    lr = np.log(atr.replace(0.0, np.nan)) - np.log(park.replace(0.0, np.nan))
    return lr.rolling(60, min_periods=60).mean().replace([np.inf, -np.inf], np.nan)


# === Bounded transforms (different shape than file 1) ===


def f18pg_f18_parkinson_garman_klass_estimators_park_logvol_tanh_zscore_252d_base_v118_signal(closeadj, high, low):
    """tanh of (log Parkinson(63) - 252d mean log Parkinson(63)) / 252d std.

    Bounded long-horizon log-vol z-score. Structurally different from
    cross-window spread features: emphasises absolute deviation from
    its own long-run mean."""
    _ = closeadj
    p63 = ((np.log(high / low) ** 2).rolling(63, min_periods=63).mean() / (4.0 * np.log(2.0))) ** 0.5
    lp = np.log(p63.replace(0.0, np.nan))
    m = lp.rolling(252, min_periods=126).mean()
    sd = lp.rolling(252, min_periods=126).std(ddof=0)
    z = (lp - m) / sd.replace(0.0, np.nan)
    return np.tanh(z).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_gk_sigmoid_pctrank_120d_base_v119_signal(open, high, low, closeadj):
    """Sigmoid of (GK(42) percentile rank 120d - 0.5) * 8."""
    n = 42
    hl = 0.5 * np.log(high / low) ** 2
    co = (2.0 * np.log(2.0) - 1.0) * np.log(closeadj / open) ** 2
    g = ((hl - co).rolling(n, min_periods=n).mean().clip(lower=0.0)) ** 0.5
    pct = g.rolling(120, min_periods=60).rank(pct=True)
    return (1.0 / (1.0 + np.exp(-(pct - 0.5) * 8.0))).where(pct.notna()).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_rs_arctan_pctchange_60d_base_v120_signal(open, high, low, closeadj):
    """arctan of 60d percent change in RS(30)."""
    n = 30
    rs_inner = np.log(high / closeadj) * np.log(high / open) + np.log(low / closeadj) * np.log(low / open)
    rs = rs_inner.rolling(n, min_periods=n).mean().clip(lower=0.0) ** 0.5
    pc = (rs / rs.shift(60)) - 1.0
    return np.arctan(pc).replace([np.inf, -np.inf], np.nan)


# === Regression / time-series signals ===


def f18pg_f18_parkinson_garman_klass_estimators_park_autocorr_120d_base_v121_signal(closeadj, high, low):
    """Lag-1 autocorrelation of Parkinson(5) over 120d."""
    _ = closeadj
    p = ((np.log(high / low) ** 2).rolling(5, min_periods=5).mean() / (4.0 * np.log(2.0))) ** 0.5
    n = 120
    m1 = p.rolling(n, min_periods=n).mean()
    sd = p.rolling(n, min_periods=n).std(ddof=0)
    cross = (p * p.shift(1)).rolling(n, min_periods=n).mean()
    cov = cross - m1 * m1
    return (cov / (sd * sd).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_rs_autocorr_lag5_60d_base_v122_signal(open, high, low, close):
    """Lag-5 autocorrelation of RS daily contribution over 60d."""
    rs = np.log(high / close) * np.log(high / open) + np.log(low / close) * np.log(low / open)
    n = 60
    m1 = rs.rolling(n, min_periods=n).mean()
    sd = rs.rolling(n, min_periods=n).std(ddof=0)
    cross = (rs * rs.shift(5)).rolling(n, min_periods=n).mean()
    cov = cross - m1 * m1
    return (cov / (sd * sd).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Mid-range / centered features ===


def f18pg_f18_parkinson_garman_klass_estimators_logrange_demean_42d_base_v123_signal(high, low):
    """ln(H/L) minus its 42d mean -- centered log range."""
    lr = np.log(high / low)
    return (lr - lr.rolling(42, min_periods=42).mean()).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_park_logsq_acf_lag10_60d_base_v124_signal(closeadj, high, low):
    """Lag-10 autocorrelation of log Parkinson(5) over 60d.

    Distinct structural class (autocorrelation at a lag) from the prior
    cross-window mean differential. Picks up persistence of range vol."""
    _ = closeadj
    p = ((np.log(high / low) ** 2).rolling(5, min_periods=5).mean() / (4.0 * np.log(2.0))) ** 0.5
    lp = np.log(p.replace(0.0, np.nan))
    n = 60
    m = lp.rolling(n, min_periods=n).mean()
    sd = lp.rolling(n, min_periods=n).std(ddof=0)
    cross = (lp * lp.shift(10)).rolling(n, min_periods=n).mean()
    cov = cross - m * m
    return (cov / (sd * sd).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Quantile-based features ===


def f18pg_f18_parkinson_garman_klass_estimators_park_q75_q25_ratio_120d_base_v125_signal(closeadj, high, low):
    """q75/q25 of Parkinson(5) over 120d."""
    _ = closeadj
    p = ((np.log(high / low) ** 2).rolling(5, min_periods=5).mean() / (4.0 * np.log(2.0))) ** 0.5
    q75 = p.rolling(120, min_periods=60).quantile(0.75)
    q25 = p.rolling(120, min_periods=60).quantile(0.25)
    return (q75 / q25.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_atr_median_252d_base_v126_signal(high, low, closeadj):
    """252d median of ATR(21)/closeadj."""
    tr = pd.concat([high - low, (high - closeadj.shift(1)).abs(), (low - closeadj.shift(1)).abs()], axis=1).max(axis=1)
    base = tr.rolling(21, min_periods=21).mean() / closeadj
    return base.rolling(252, min_periods=126).median().replace([np.inf, -np.inf], np.nan)


# === Long-window estimators ===


def f18pg_f18_parkinson_garman_klass_estimators_rs_252d_base_v127_signal(open, high, low, closeadj):
    """RS at 252d -- annual drift-robust estimator."""
    n = 252
    rs = np.log(high / closeadj) * np.log(high / open) + np.log(low / closeadj) * np.log(low / open)
    var = rs.rolling(n, min_periods=n).mean()
    return (var.clip(lower=0.0) ** 0.5).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_yz_120d_base_v128_signal(open, high, low, closeadj):
    """Yang-Zhang at 120d."""
    n = 120
    on = np.log(open / closeadj.shift(1))
    oc = np.log(closeadj / open)
    von = on.rolling(n, min_periods=n).var(ddof=1)
    voc = oc.rolling(n, min_periods=n).var(ddof=1)
    rs_inner = np.log(high / closeadj) * np.log(high / open) + np.log(low / closeadj) * np.log(low / open)
    vrs = rs_inner.rolling(n, min_periods=n).mean()
    k = 0.34 / (1.34 + (n + 1.0) / (n - 1.0))
    yz = (von + k * voc + (1.0 - k) * vrs).clip(lower=0.0) ** 0.5
    return yz.replace([np.inf, -np.inf], np.nan)


# === Differentials / momentum-like ===


def f18pg_f18_parkinson_garman_klass_estimators_park_log_velocity_42d_base_v129_signal(closeadj, high, low):
    """log Parkinson(42) - log Parkinson(42).shift(10) -- log-vol velocity over 10d."""
    _ = closeadj
    p = ((np.log(high / low) ** 2).rolling(42, min_periods=42).mean() / (4.0 * np.log(2.0))) ** 0.5
    lp = np.log(p.replace(0.0, np.nan))
    return (lp - lp.shift(10)).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_gk_velocity_30_5d_base_v130_signal(open, high, low, close):
    """GK(10) - GK(10).shift(5) -- short-horizon vol velocity."""
    n = 10
    hl = 0.5 * np.log(high / low) ** 2
    co = (2.0 * np.log(2.0) - 1.0) * np.log(close / open) ** 2
    g = ((hl - co).rolling(n, min_periods=n).mean().clip(lower=0.0)) ** 0.5
    return (g - g.shift(5)).replace([np.inf, -np.inf], np.nan)


# === Comparative regimes ===


def f18pg_f18_parkinson_garman_klass_estimators_park_above_120d_median_flag_base_v131_signal(closeadj, high, low):
    """Binary: Parkinson(42) > its own 120d median."""
    _ = closeadj
    p = ((np.log(high / low) ** 2).rolling(42, min_periods=42).mean() / (4.0 * np.log(2.0))) ** 0.5
    return (p > p.rolling(120, min_periods=60).median()).astype(float).where(p.notna()).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_atr_in_quintile_252d_base_v132_signal(high, low, closeadj):
    """Quintile bucket 0..4 of ATR(21)/closeadj over 252d."""
    tr = pd.concat([high - low, (high - closeadj.shift(1)).abs(), (low - closeadj.shift(1)).abs()], axis=1).max(axis=1)
    base = tr.rolling(21, min_periods=21).mean() / closeadj
    rk = base.rolling(252, min_periods=126).rank(pct=True)
    return np.floor(rk * 5.0).clip(upper=4.0).replace([np.inf, -np.inf], np.nan)


# === Long-horizon z-scores ===


def f18pg_f18_parkinson_garman_klass_estimators_yz_z_30_252_base_v133_signal(open, high, low, closeadj):
    """YZ(30) z-score over 252d."""
    n = 30
    on = np.log(open / closeadj.shift(1))
    oc = np.log(closeadj / open)
    von = on.rolling(n, min_periods=n).var(ddof=1)
    voc = oc.rolling(n, min_periods=n).var(ddof=1)
    rs_inner = np.log(high / closeadj) * np.log(high / open) + np.log(low / closeadj) * np.log(low / open)
    vrs = rs_inner.rolling(n, min_periods=n).mean()
    k = 0.34 / (1.34 + (n + 1.0) / (n - 1.0))
    yz = (von + k * voc + (1.0 - k) * vrs).clip(lower=0.0) ** 0.5
    m = yz.rolling(252, min_periods=126).mean()
    sd = yz.rolling(252, min_periods=126).std(ddof=0)
    return ((yz - m) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_rs_z_42_120_base_v134_signal(open, high, low, closeadj):
    """RS(42) z-score over 120d (file 1 uses RS(21) over 252)."""
    n = 42
    rs_inner = np.log(high / closeadj) * np.log(high / open) + np.log(low / closeadj) * np.log(low / open)
    rs = rs_inner.rolling(n, min_periods=n).mean().clip(lower=0.0) ** 0.5
    m = rs.rolling(120, min_periods=60).mean()
    sd = rs.rolling(120, min_periods=60).std(ddof=0)
    return ((rs - m) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Specialty -- estimator weighted average ===


def f18pg_f18_parkinson_garman_klass_estimators_weighted_estimator_30d_base_v135_signal(open, high, low, closeadj):
    """Weighted average: 0.4*Parkinson + 0.3*GK + 0.3*RS at 30d -- prior-weighted composite."""
    n = 30
    park = ((np.log(high / low) ** 2).rolling(n, min_periods=n).mean() / (4.0 * np.log(2.0))) ** 0.5
    hl = 0.5 * np.log(high / low) ** 2
    co = (2.0 * np.log(2.0) - 1.0) * np.log(closeadj / open) ** 2
    gk = ((hl - co).rolling(n, min_periods=n).mean().clip(lower=0.0)) ** 0.5
    rs_inner = np.log(high / closeadj) * np.log(high / open) + np.log(low / closeadj) * np.log(low / open)
    rs = rs_inner.rolling(n, min_periods=n).mean().clip(lower=0.0) ** 0.5
    return (0.4 * park + 0.3 * gk + 0.3 * rs).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_estimator_logspread_30d_base_v136_signal(open, high, low, closeadj):
    """log(max) - log(min) of {Park, GK, RS} at 30d -- log spread of estimators."""
    n = 30
    park = ((np.log(high / low) ** 2).rolling(n, min_periods=n).mean() / (4.0 * np.log(2.0))) ** 0.5
    hl = 0.5 * np.log(high / low) ** 2
    co = (2.0 * np.log(2.0) - 1.0) * np.log(closeadj / open) ** 2
    gk = ((hl - co).rolling(n, min_periods=n).mean().clip(lower=0.0)) ** 0.5
    rs_inner = np.log(high / closeadj) * np.log(high / open) + np.log(low / closeadj) * np.log(low / open)
    rs = rs_inner.rolling(n, min_periods=n).mean().clip(lower=0.0) ** 0.5
    stk = pd.concat([park, gk, rs], axis=1)
    return (np.log(stk.max(axis=1).replace(0.0, np.nan)) - np.log(stk.min(axis=1).replace(0.0, np.nan))).replace([np.inf, -np.inf], np.nan)


# === Specialty -- overnight gap features ===


def f18pg_f18_parkinson_garman_klass_estimators_overnight_skew_120d_base_v137_signal(open, closeadj):
    """Skew of overnight ln(O/prev_C) over 120d."""
    on = np.log(open / closeadj.shift(1))
    return on.rolling(120, min_periods=60).skew().replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_overnight_intraday_var_ratio_60d_base_v138_signal(open, closeadj):
    """Var(overnight) / Var(intraday) at 60d, in log-space -- bounded-shape gap-vs-intraday vol ratio.

    Distinct from raw 120d overnight variance: a 60d log ratio of overnight
    to intraday variances. Captures whether gap risk or intraday risk
    dominates at a medium horizon."""
    n = 60
    on = np.log(open / closeadj.shift(1))
    oc = np.log(closeadj / open)
    von = on.rolling(n, min_periods=n).var(ddof=1)
    voc = oc.rolling(n, min_periods=n).var(ddof=1)
    return (np.log(von.replace(0.0, np.nan)) - np.log(voc.replace(0.0, np.nan))).replace([np.inf, -np.inf], np.nan)


# === Cross-window contrasts ===


def f18pg_f18_parkinson_garman_klass_estimators_park_concavity_5_21_63_base_v139_signal(closeadj, high, low):
    """Term-structure concavity: log(p21) - 0.5*(log(p5)+log(p63)) -- belly curvature.

    Bows-up vs bows-down term-structure shape. Picks up non-linearity
    across 3 windows that any 2-window log spread cannot capture."""
    _ = closeadj
    p5 = ((np.log(high / low) ** 2).rolling(5, min_periods=5).mean() / (4.0 * np.log(2.0))) ** 0.5
    p21 = ((np.log(high / low) ** 2).rolling(21, min_periods=21).mean() / (4.0 * np.log(2.0))) ** 0.5
    p63 = ((np.log(high / low) ** 2).rolling(63, min_periods=63).mean() / (4.0 * np.log(2.0))) ** 0.5
    lp5 = np.log(p5.replace(0.0, np.nan))
    lp21 = np.log(p21.replace(0.0, np.nan))
    lp63 = np.log(p63.replace(0.0, np.nan))
    return (lp21 - 0.5 * (lp5 + lp63)).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_rs_term_30_120_base_v140_signal(open, high, low, closeadj):
    """RS(30) / RS(120) -- term structure of drift-adjusted vol."""
    rs_inner = np.log(high / closeadj) * np.log(high / open) + np.log(low / closeadj) * np.log(low / open)
    rs30 = rs_inner.rolling(30, min_periods=30).mean().clip(lower=0.0) ** 0.5
    rs120 = rs_inner.rolling(120, min_periods=120).mean().clip(lower=0.0) ** 0.5
    return (rs30 / rs120.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Statistical / dispersion of estimator pieces ===


def f18pg_f18_parkinson_garman_klass_estimators_logrange_mad_60d_base_v141_signal(high, low):
    """Median absolute deviation of ln(H/L) over 60d."""
    lr = np.log(high / low)
    med = lr.rolling(60, min_periods=60).median()
    return (lr - med).abs().rolling(60, min_periods=60).median().replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_co_logsq_mean_120d_base_v142_signal(open, closeadj):
    """Mean of ln(C/O)^2 over 120d."""
    return (np.log(closeadj / open) ** 2).rolling(120, min_periods=60).mean().replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_overnight_intraday_corr_120d_base_v143_signal(open, closeadj):
    """120d rolling correlation between overnight and intraday returns."""
    on = np.log(open / closeadj.shift(1))
    oc = np.log(closeadj / open)
    return on.rolling(120, min_periods=60).corr(oc).replace([np.inf, -np.inf], np.nan)


# === Range-based momentum ===


def f18pg_f18_parkinson_garman_klass_estimators_park_pct_change_120d_base_v144_signal(closeadj, high, low):
    """120d percent change in Parkinson(21)."""
    _ = closeadj
    p = ((np.log(high / low) ** 2).rolling(21, min_periods=21).mean() / (4.0 * np.log(2.0))) ** 0.5
    return ((p / p.shift(120)) - 1.0).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_atr_pct_change_60d_base_v145_signal(high, low, closeadj):
    """60d percent change in ATR(21)/closeadj."""
    tr = pd.concat([high - low, (high - closeadj.shift(1)).abs(), (low - closeadj.shift(1)).abs()], axis=1).max(axis=1)
    base = tr.rolling(21, min_periods=21).mean() / closeadj
    return ((base / base.shift(60)) - 1.0).replace([np.inf, -np.inf], np.nan)


# === Sigmoid / arctan transforms on different inputs ===


def f18pg_f18_parkinson_garman_klass_estimators_rs_pct_change_arctan_60d_base_v146_signal(open, high, low, closeadj):
    """arctan of 60d percent change in RS(60)."""
    rs_inner = np.log(high / closeadj) * np.log(high / open) + np.log(low / closeadj) * np.log(low / open)
    rs = rs_inner.rolling(60, min_periods=60).mean().clip(lower=0.0) ** 0.5
    pc = (rs / rs.shift(60)) - 1.0
    return np.arctan(pc * 5.0).replace([np.inf, -np.inf], np.nan)


# === Final structurally distinct features ===


def f18pg_f18_parkinson_garman_klass_estimators_yz_oc_share_42d_base_v147_signal(open, high, low, closeadj):
    """k * Var(oc) / YZ_variance(42) -- open-to-close share of YZ at 42d.

    Decomposition feature: shows the intraday open-to-close component's
    share in the total Yang-Zhang variance. Structurally distinct from
    raw YZ(42) level which would correlate with overnight_var_120d.
    """
    n = 42
    on = np.log(open / closeadj.shift(1))
    oc = np.log(closeadj / open)
    von = on.rolling(n, min_periods=n).var(ddof=1)
    voc = oc.rolling(n, min_periods=n).var(ddof=1)
    rs_inner = np.log(high / closeadj) * np.log(high / open) + np.log(low / closeadj) * np.log(low / open)
    vrs = rs_inner.rolling(n, min_periods=n).mean()
    k = 0.34 / (1.34 + (n + 1.0) / (n - 1.0))
    yz_var = (von + k * voc + (1.0 - k) * vrs).clip(lower=0.0)
    return ((k * voc) / yz_var.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_bipower_z_30_120_base_v148_signal(closeadj):
    """z-score of bipower(30) over 120d window."""
    r = np.log(closeadj / closeadj.shift(1)).abs()
    bp = r * r.shift(1) * (np.pi / 2.0)
    base = bp.rolling(30, min_periods=30).sum() ** 0.5
    m = base.rolling(120, min_periods=60).mean()
    sd = base.rolling(120, min_periods=60).std(ddof=0)
    return ((base - m) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_park_atr_log_pctrank_120d_base_v149_signal(high, low, closeadj):
    """Percentile rank over 120d of log(Parkinson(5) / ATR(14)/closeadj).

    Continuous replacement for a streak-based flag that was identically
    zero on synthetic data (Parkinson(5) never exceeded ATR(14)/closeadj
    because ATR includes overnight gaps). The 120d percentile rank of the
    log ratio still captures "Park-vs-ATR regime extremity" but without
    being collapsed to {0,1}.
    """
    p = ((np.log(high / low) ** 2).rolling(5, min_periods=5).mean() / (4.0 * np.log(2.0))) ** 0.5
    tr = pd.concat([high - low, (high - closeadj.shift(1)).abs(), (low - closeadj.shift(1)).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean() / closeadj
    lr = np.log(p.replace(0.0, np.nan)) - np.log(atr.replace(0.0, np.nan))
    return lr.rolling(120, min_periods=60).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_gk_rs_corr_120d_base_v150_signal(open, high, low, closeadj):
    """120d rolling correlation between log GK(5) and log RS(5) -- estimator co-movement."""
    hl = 0.5 * np.log(high / low) ** 2
    co = (2.0 * np.log(2.0) - 1.0) * np.log(closeadj / open) ** 2
    g5 = ((hl - co).rolling(5, min_periods=5).mean().clip(lower=0.0)) ** 0.5
    rs_inner = np.log(high / closeadj) * np.log(high / open) + np.log(low / closeadj) * np.log(low / open)
    rs5 = rs_inner.rolling(5, min_periods=5).mean().clip(lower=0.0) ** 0.5
    return np.log(g5.replace(0.0, np.nan)).rolling(120, min_periods=60).corr(np.log(rs5.replace(0.0, np.nan))).replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f18_parkinson_garman_klass_estimators_base_076_150_REGISTRY = {
    "f18pg_f18_parkinson_garman_klass_estimators_park_42d_base_v076_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_42d_base_v076_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_120d_base_v077_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_120d_base_v077_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_gk_42d_base_v078_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_gk_42d_base_v078_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_rs_120d_base_v079_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_rs_120d_base_v079_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_yz_42d_base_v080_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_yz_42d_base_v080_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_rs_signed_diff_60d_base_v081_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_rs_signed_diff_60d_base_v081_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_gk_rs_log_42d_base_v082_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_gk_rs_log_42d_base_v082_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_yz_gk_diff_30d_base_v083_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_yz_gk_diff_30d_base_v083_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_centered_diff_5_42_base_v084_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_centered_diff_5_42_base_v084_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_inverse_60d_base_v085_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_inverse_60d_base_v085_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_gk_negativity_share_42d_base_v086_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_gk_negativity_share_42d_base_v086_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_term_21_120_base_v087_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_term_21_120_base_v087_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_gk_term_log_30_120_base_v088_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_gk_term_log_30_120_base_v088_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_rs_slope_42d_base_v089_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_rs_slope_42d_base_v089_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_atr_slope_30d_base_v090_signal": {"inputs": ["high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_atr_slope_30d_base_v090_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_yz_accel_42d_base_v091_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_yz_accel_42d_base_v091_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_gk_park_rank_diff_63d_base_v092_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_gk_park_rank_diff_63d_base_v092_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_estimator_cv_60d_base_v093_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_estimator_cv_60d_base_v093_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_above_long_count_60d_base_v094_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_above_long_count_60d_base_v094_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_rs_high_low_streak_diff_base_v095_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_rs_high_low_streak_diff_base_v095_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_logrange_realized_corr_60d_base_v096_signal": {"inputs": ["close", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_logrange_realized_corr_60d_base_v096_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_realized_corr_120d_base_v097_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_realized_corr_120d_base_v097_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_overnight_share_pctrank_120d_base_v098_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_overnight_share_pctrank_120d_base_v098_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_gk_above_park_streak_base_v099_signal": {"inputs": ["open", "high", "low", "close"], "func": f18pg_f18_parkinson_garman_klass_estimators_gk_above_park_streak_base_v099_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_dayssince_atr_high_252d_base_v100_signal": {"inputs": ["high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_dayssince_atr_high_252d_base_v100_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_logrange_mean_252d_base_v101_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_logrange_mean_252d_base_v101_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_logrange_skew_120d_base_v102_signal": {"inputs": ["high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_logrange_skew_120d_base_v102_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_logrange_kurt_120d_base_v103_signal": {"inputs": ["high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_logrange_kurt_120d_base_v103_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_oc_log_kurt_120d_base_v104_signal": {"inputs": ["open", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_oc_log_kurt_120d_base_v104_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_bipower_42d_base_v105_signal": {"inputs": ["closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_bipower_42d_base_v105_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_jump_share_21d_base_v106_signal": {"inputs": ["close"], "func": f18pg_f18_parkinson_garman_klass_estimators_jump_share_21d_base_v106_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_bipower_park_diff_30d_base_v107_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_bipower_park_diff_30d_base_v107_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_atr_ema_60d_base_v108_signal": {"inputs": ["high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_atr_ema_60d_base_v108_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_atr_pct_change_30d_base_v109_signal": {"inputs": ["high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_atr_pct_change_30d_base_v109_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_truerange_gap_share_60d_base_v110_signal": {"inputs": ["high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_truerange_gap_share_60d_base_v110_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_range_vs_absret_5d_base_v111_signal": {"inputs": ["close", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_range_vs_absret_5d_base_v111_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_efficiency_30d_base_v112_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_efficiency_30d_base_v112_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_hl_sq_share_in_gk_30d_base_v113_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_hl_sq_share_in_gk_30d_base_v113_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_co_sq_in_park_42d_base_v114_signal": {"inputs": ["closeadj", "open", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_co_sq_in_park_42d_base_v114_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_sign_park_change_30d_base_v115_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_sign_park_change_30d_base_v115_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_sign_gk_minus_park_42d_base_v116_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_sign_gk_minus_park_42d_base_v116_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_atr_park_logratio_60d_base_v117_signal": {"inputs": ["high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_atr_park_logratio_60d_base_v117_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_logvol_tanh_zscore_252d_base_v118_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_logvol_tanh_zscore_252d_base_v118_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_gk_sigmoid_pctrank_120d_base_v119_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_gk_sigmoid_pctrank_120d_base_v119_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_rs_arctan_pctchange_60d_base_v120_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_rs_arctan_pctchange_60d_base_v120_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_autocorr_120d_base_v121_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_autocorr_120d_base_v121_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_rs_autocorr_lag5_60d_base_v122_signal": {"inputs": ["open", "high", "low", "close"], "func": f18pg_f18_parkinson_garman_klass_estimators_rs_autocorr_lag5_60d_base_v122_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_logrange_demean_42d_base_v123_signal": {"inputs": ["high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_logrange_demean_42d_base_v123_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_logsq_acf_lag10_60d_base_v124_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_logsq_acf_lag10_60d_base_v124_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_q75_q25_ratio_120d_base_v125_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_q75_q25_ratio_120d_base_v125_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_atr_median_252d_base_v126_signal": {"inputs": ["high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_atr_median_252d_base_v126_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_rs_252d_base_v127_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_rs_252d_base_v127_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_yz_120d_base_v128_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_yz_120d_base_v128_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_log_velocity_42d_base_v129_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_log_velocity_42d_base_v129_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_gk_velocity_30_5d_base_v130_signal": {"inputs": ["open", "high", "low", "close"], "func": f18pg_f18_parkinson_garman_klass_estimators_gk_velocity_30_5d_base_v130_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_above_120d_median_flag_base_v131_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_above_120d_median_flag_base_v131_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_atr_in_quintile_252d_base_v132_signal": {"inputs": ["high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_atr_in_quintile_252d_base_v132_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_yz_z_30_252_base_v133_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_yz_z_30_252_base_v133_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_rs_z_42_120_base_v134_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_rs_z_42_120_base_v134_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_weighted_estimator_30d_base_v135_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_weighted_estimator_30d_base_v135_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_estimator_logspread_30d_base_v136_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_estimator_logspread_30d_base_v136_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_overnight_skew_120d_base_v137_signal": {"inputs": ["open", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_overnight_skew_120d_base_v137_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_overnight_intraday_var_ratio_60d_base_v138_signal": {"inputs": ["open", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_overnight_intraday_var_ratio_60d_base_v138_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_concavity_5_21_63_base_v139_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_concavity_5_21_63_base_v139_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_rs_term_30_120_base_v140_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_rs_term_30_120_base_v140_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_logrange_mad_60d_base_v141_signal": {"inputs": ["high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_logrange_mad_60d_base_v141_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_co_logsq_mean_120d_base_v142_signal": {"inputs": ["open", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_co_logsq_mean_120d_base_v142_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_overnight_intraday_corr_120d_base_v143_signal": {"inputs": ["open", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_overnight_intraday_corr_120d_base_v143_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_pct_change_120d_base_v144_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_pct_change_120d_base_v144_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_atr_pct_change_60d_base_v145_signal": {"inputs": ["high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_atr_pct_change_60d_base_v145_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_rs_pct_change_arctan_60d_base_v146_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_rs_pct_change_arctan_60d_base_v146_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_yz_oc_share_42d_base_v147_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_yz_oc_share_42d_base_v147_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_bipower_z_30_120_base_v148_signal": {"inputs": ["closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_bipower_z_30_120_base_v148_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_atr_log_pctrank_120d_base_v149_signal": {"inputs": ["high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_atr_log_pctrank_120d_base_v149_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_gk_rs_corr_120d_base_v150_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_gk_rs_corr_120d_base_v150_signal},
}


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
    for name, entry in f18_parkinson_garman_klass_estimators_base_076_150_REGISTRY.items():
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
