"""f17_volatility_regime base features 001-075.

Domain: volatility REGIME — CLASSIFY or QUANTIFY current volatility level
RELATIVE to a reference (history, regime boundaries, transitions).
Distinct from f16 (term structure across horizons) — here we focus on
LEVEL classification, transitions, and regime persistence anchored on
a single base horizon (mostly vol(21d), some vol(5/42/63)).

Feature classes used: quantile/quintile/decile buckets, percentile ranks,
binary regime indicators, regime transitions/days-since/streaks,
regime-conditional return interactions, vol shocks, vol-of-vol,
sigmoid/arctan/tanh bounded transforms of regime signals,
EWMA-vol fast vs slow, regime-persistence autocorr, regime confidence,
days since hit top decile / days in low regime, multi-window agreement.

NaN policy: never fillna(<value>); only replace([inf,-inf], nan) at the
final return. Window > 21d uses closeadj; <= 21d uses close.
Each function spells its formula inline (helpers are kernel primitives).
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Helpers (vol primitives only). Each feature spells the regime logic inline.
# ---------------------------------------------------------------------------


def _logret(s: pd.Series) -> pd.Series:
    return np.log(s / s.shift(1))


def _vol(s: pd.Series, n: int) -> pd.Series:
    """Rolling std-dev of log-returns over n trading days (annualized factor omitted)."""
    r = np.log(s / s.shift(1))
    return r.rolling(n, min_periods=n).std()


def _absret(s: pd.Series) -> pd.Series:
    return np.log(s / s.shift(1)).abs()


def _qbucket(v: float, edges) -> float:
    """Map v to bucket index 1..K where edges has K-1 thresholds."""
    if not np.isfinite(v):
        return np.nan
    out = 1.0
    for e in edges:
        if not np.isfinite(e):
            return np.nan
        if v > e:
            out += 1.0
    return out


# ---------------------------------------------------------------------------
# Features 001-075
# ---------------------------------------------------------------------------


# === REGIME CLASSIFICATION (quartile / quintile / decile buckets) ==========


def f17vr_f17_volatility_regime_volquartile_21on252_base_v001_signal(closeadj):
    """Quartile bucket (1..4) of vol(21d) within trailing 252d distribution."""
    v = _vol(closeadj, 21)
    def _bk(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        q1, q2, q3 = np.quantile(y[:-1], [0.25, 0.5, 0.75]) if len(y) > 1 else (np.nan, np.nan, np.nan)
        v0 = x[-1]
        b = 1.0
        if v0 > q1: b += 1.0
        if v0 > q2: b += 1.0
        if v0 > q3: b += 1.0
        return float(b)
    return v.rolling(252, min_periods=60).apply(_bk, raw=True).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_quintile_chg_ind_21on252_base_v002_signal(closeadj):
    """Indicator (signed: -1/0/+1) of CHANGE in quintile-of-vol(21d) since 5 bars ago.
    Discrete regime-transition direction, distinct from level-of-quintile."""
    v = _vol(closeadj, 21)
    def _qn(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 60:
            return np.nan
        qs = np.quantile(y[:-1], [0.2, 0.4, 0.6, 0.8])
        v0 = x[-1]
        b = 1.0
        for q in qs:
            if v0 > q: b += 1.0
        return float(b)
    qn = v.rolling(252, min_periods=60).apply(_qn, raw=True)
    return np.sign(qn - qn.shift(5)).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_decile_absret_120d_base_v003_signal(close):
    """Decile bucket (1..10) of |log-return(today)| within trailing 120d.
    Single-bar shock magnitude regime — fully detached from rolling-vol level features."""
    a = np.log(close / close.shift(1)).abs()
    def _bk(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 40:
            return np.nan
        qs = np.quantile(y[:-1], np.arange(1, 10) / 10.0)
        v0 = x[-1]
        b = 1.0
        for q in qs:
            if v0 > q: b += 1.0
        return float(b)
    return a.rolling(120, min_periods=40).apply(_bk, raw=True).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_volquartile1_ind_21d_base_v004_signal(closeadj):
    """Binary indicator: vol(21d) is in lowest-quartile of trailing 252d."""
    v = _vol(closeadj, 21)
    def _q1(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        q1 = np.quantile(y[:-1], 0.25)
        return 1.0 if x[-1] <= q1 else 0.0
    return v.rolling(252, min_periods=60).apply(_q1, raw=True).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_volquartile4_ind_21d_base_v005_signal(closeadj):
    """Binary indicator: vol(21d) is in highest-quartile of trailing 252d."""
    v = _vol(closeadj, 21)
    def _q4(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        q3 = np.quantile(y[:-1], 0.75)
        return 1.0 if x[-1] >= q3 else 0.0
    return v.rolling(252, min_periods=60).apply(_q4, raw=True).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_multih_quintile_5_21_63_base_v006_signal(closeadj):
    """Combined quintile (sum) of vol(5)/vol(21)/vol(63) each ranked vs 252d."""
    v5 = _vol(closeadj, 5)
    v21 = _vol(closeadj, 21)
    v63 = _vol(closeadj, 63)
    def _rk(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 60:
            return np.nan
        return float(np.mean(y[:-1] < x[-1]))
    p5 = v5.rolling(252, min_periods=60).apply(_rk, raw=True)
    p21 = v21.rolling(252, min_periods=60).apply(_rk, raw=True)
    p63 = v63.rolling(252, min_periods=60).apply(_rk, raw=True)
    def _quin(p):
        return np.floor(p * 5.0).clip(0, 4) + 1.0
    return (_quin(p5) + _quin(p21) + _quin(p63)).replace([np.inf, -np.inf], np.nan)


# === VOL LEVEL FEATURES (relative-to-median / z-score / percentile rank) ==


def f17vr_f17_volatility_regime_vol21_over_med252_base_v007_signal(closeadj):
    """vol(21d) / median(vol(21d), 252d). Regime-relative level."""
    v = _vol(closeadj, 21)
    med = v.rolling(252, min_periods=60).median()
    return (v / med.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_volz_21on252_base_v008_signal(closeadj):
    """Z-score of vol(21d) within its trailing 252d distribution."""
    v = _vol(closeadj, 21)
    mu = v.rolling(252, min_periods=60).mean()
    sd = v.rolling(252, min_periods=60).std()
    return ((v - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_volpctrank_21on120_base_v009_signal(closeadj):
    """Percentile rank of vol(21d) within trailing 120d."""
    v = _vol(closeadj, 21)
    def _r(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 30:
            return np.nan
        return float(np.mean(y[:-1] < x[-1]))
    return v.rolling(120, min_periods=40).apply(_r, raw=True).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_volpctrank_42on500_base_v010_signal(closeadj):
    """Percentile rank of vol(42d) within trailing 500d — long-memory regime rank."""
    v = _vol(closeadj, 42)
    def _r(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 100:
            return np.nan
        return float(np.mean(y[:-1] < x[-1]))
    return v.rolling(500, min_periods=120).apply(_r, raw=True).replace([np.inf, -np.inf], np.nan)


# === REGIME TRANSITION SIGNALS ============================================


def f17vr_f17_volatility_regime_volpct_largeret_42d_base_v011_signal(close):
    """Fraction of last 42 bars where |log-return| > 2 * median(|log-return|, 42d).
    Tail-frequency regime: how often outsized moves occur."""
    a = np.log(close / close.shift(1)).abs()
    med = a.rolling(42, min_periods=20).median()
    flag = (a > 2.0 * med).astype(float).where(~a.isna() & ~med.isna())
    return flag.rolling(42, min_periods=20).mean().replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_regimestab_frac_60d_base_v012_signal(closeadj):
    """Fraction of last 60 bars spent in CURRENT vol-tercile regime."""
    v = _vol(closeadj, 21)
    def _tc(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        a, b = np.quantile(y[:-1], [1/3.0, 2/3.0])
        v0 = x[-1]
        return 1.0 if v0 < a else (2.0 if v0 < b else 3.0)
    reg = v.rolling(252, min_periods=60).apply(_tc, raw=True)
    def _frac(x):
        if not np.isfinite(x[-1]):
            return np.nan
        cur = x[-1]
        return float(np.mean(x == cur))
    return reg.rolling(60, min_periods=30).apply(_frac, raw=True).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_transitioncount_90d_base_v013_signal(closeadj):
    """Count of regime transitions (tercile of vol(21d)) in trailing 90d."""
    v = _vol(closeadj, 21)
    def _tc(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        a, b = np.quantile(y[:-1], [1/3.0, 2/3.0])
        v0 = x[-1]
        return 1.0 if v0 < a else (2.0 if v0 < b else 3.0)
    reg = v.rolling(252, min_periods=60).apply(_tc, raw=True)
    chg = (reg != reg.shift(1)).astype(float).where(~reg.isna() & ~reg.shift(1).isna())
    return chg.rolling(90, min_periods=30).sum().replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_volexpansion_5m63_base_v014_signal(closeadj):
    """vol(5) - vol(63), signed expansion vs long-run. Positive when short-vol > long-vol."""
    return (_vol(closeadj, 5) - _vol(closeadj, 63)).replace([np.inf, -np.inf], np.nan)


# === REGIME PERSISTENCE ===================================================


def f17vr_f17_volatility_regime_streak_currentregime_60d_base_v015_signal(closeadj):
    """Consecutive bars in CURRENT vol-tercile regime, capped 60."""
    v = _vol(closeadj, 21)
    def _tc(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        a, b = np.quantile(y[:-1], [1/3.0, 2/3.0])
        v0 = x[-1]
        return 1.0 if v0 < a else (2.0 if v0 < b else 3.0)
    reg = v.rolling(252, min_periods=60).apply(_tc, raw=True)
    def _streak(x):
        cur = x[-1]
        if not np.isfinite(cur):
            return np.nan
        c = 0
        for w in x[::-1]:
            if w == cur:
                c += 1
            else:
                break
        return float(c)
    return reg.rolling(60, min_periods=20).apply(_streak, raw=True).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_vol_HLrange_pct_42d_base_v016_signal(closeadj):
    """(max(vol(21d), 42d) - min(vol(21d), 42d)) / max(vol(21d), 42d) — relative trading range
    of the vol-itself over 42 bars. Captures how far vol has swung within its window."""
    v = _vol(closeadj, 21)
    hi = v.rolling(42, min_periods=20).max()
    lo = v.rolling(42, min_periods=20).min()
    return ((hi - lo) / hi.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_daysinhighvol_120d_base_v017_signal(closeadj):
    """Count of bars (in last 120) where vol(21d) was in top-quartile of 252d."""
    v = _vol(closeadj, 21)
    def _q4(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        q3 = np.quantile(y[:-1], 0.75)
        return 1.0 if x[-1] >= q3 else 0.0
    ind = v.rolling(252, min_periods=60).apply(_q4, raw=True)
    return ind.rolling(120, min_periods=40).sum().replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_regime_autocorr_80d_base_v018_signal(closeadj):
    """80d autocorr-lag-5 of the vol-tercile-regime time series."""
    v = _vol(closeadj, 21)
    def _tc(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        a, b = np.quantile(y[:-1], [1/3.0, 2/3.0])
        v0 = x[-1]
        return 1.0 if v0 < a else (2.0 if v0 < b else 3.0)
    reg = v.rolling(252, min_periods=60).apply(_tc, raw=True)
    return reg.rolling(80, min_periods=30).apply(
        lambda x: float(pd.Series(x).autocorr(lag=5)) if pd.Series(x).std() > 0 else np.nan,
        raw=False
    ).replace([np.inf, -np.inf], np.nan)


# === REGIME-CONDITIONAL MOMENTUM ==========================================


def f17vr_f17_volatility_regime_ret_x_highvol_ind_base_v019_signal(closeadj):
    """log-return(21d) MULTIPLIED by indicator(vol(21d) in top-quartile of 252d).
    Captures momentum that is active only in high-vol regime."""
    r = np.log(closeadj / closeadj.shift(21))
    v = _vol(closeadj, 21)
    def _q4(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        q3 = np.quantile(y[:-1], 0.75)
        return 1.0 if x[-1] >= q3 else 0.0
    ind = v.rolling(252, min_periods=60).apply(_q4, raw=True)
    return (r * ind).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_ret_x_lowvol_ind_base_v020_signal(closeadj):
    """log-return(21d) * indicator(vol(21d) in bottom-quartile of 252d)."""
    r = np.log(closeadj / closeadj.shift(21))
    v = _vol(closeadj, 21)
    def _q1(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        q1 = np.quantile(y[:-1], 0.25)
        return 1.0 if x[-1] <= q1 else 0.0
    ind = v.rolling(252, min_periods=60).apply(_q1, raw=True)
    return (r * ind).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_sharpe_42d_currentvol_base_v021_signal(closeadj):
    """Sharpe = mean(daily-logret)/std over 42d, RESCALED by vol-quartile.
    The vol-quartile tag in the multiplication encodes a regime-conditional view."""
    r = np.log(closeadj / closeadj.shift(1))
    sr = r.rolling(42, min_periods=20).mean() / r.rolling(42, min_periods=20).std().replace(0.0, np.nan)
    v = _vol(closeadj, 21)
    def _qb(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        qs = np.quantile(y[:-1], [0.25, 0.5, 0.75])
        v0 = x[-1]; b = 1.0
        for q in qs:
            if v0 > q: b += 1.0
        return float(b)
    qb = v.rolling(252, min_periods=60).apply(_qb, raw=True)
    return (sr * qb).replace([np.inf, -np.inf], np.nan)


# === RISK-PREMIUM PROXIES (vol minus long-term mean) ======================


def f17vr_f17_volatility_regime_volresid_AR1_120d_base_v022_signal(closeadj):
    """Residual of AR(1) regression of vol(21d) on its 1-bar lag over 120d window.
    Captures unexpected vol surprise after persistence is removed — distinct from level."""
    v = _vol(closeadj, 21)
    def _res(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        y = x[1:]; yl = x[:-1]
        muY = y.mean(); muL = yl.mean()
        cov = np.sum((yl - muL) * (y - muY))
        var = np.sum((yl - muL) ** 2)
        if var == 0.0:
            return np.nan
        b = cov / var
        a = muY - b * muL
        return float(y[-1] - (a + b * yl[-1]))
    return v.rolling(120, min_periods=40).apply(_res, raw=True).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_volgap_pct_42on252_base_v023_signal(closeadj):
    """(vol(42d) - median(vol(42d), 252d)) / median(vol(42d), 252d)."""
    v = _vol(closeadj, 42)
    med = v.rolling(252, min_periods=60).median()
    return ((v - med) / med.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === DISCRETE STATE SIGNALS ===============================================


def f17vr_f17_volatility_regime_highvolon_p90_base_v024_signal(closeadj):
    """Binary: vol(21d) > 90th-percentile of trailing 252d."""
    v = _vol(closeadj, 21)
    def _p90(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        return 1.0 if x[-1] > np.quantile(y[:-1], 0.9) else 0.0
    return v.rolling(252, min_periods=60).apply(_p90, raw=True).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_lowvolon_p10_base_v025_signal(closeadj):
    """Binary: vol(21d) < 10th-percentile of trailing 252d."""
    v = _vol(closeadj, 21)
    def _p10(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        return 1.0 if x[-1] < np.quantile(y[:-1], 0.1) else 0.0
    return v.rolling(252, min_periods=60).apply(_p10, raw=True).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_expanding_state_42d_base_v026_signal(closeadj):
    """Binary: vol(21d) today > mean(vol(21d), trailing 42d)."""
    v = _vol(closeadj, 21)
    mu = v.rolling(42, min_periods=20).mean()
    return (v > mu).astype(float).where(~v.isna() & ~mu.isna()).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_extreme_state_120d_base_v027_signal(closeadj):
    """Binary: vol(21d) is in tails (top OR bottom 15% of trailing 120d).
    Tail-regime indicator, distinct from mean-comparison directional state."""
    v = _vol(closeadj, 21)
    def _ext(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 40:
            return np.nan
        lo = np.quantile(y[:-1], 0.15)
        hi = np.quantile(y[:-1], 0.85)
        return 1.0 if (x[-1] < lo or x[-1] > hi) else 0.0
    return v.rolling(120, min_periods=40).apply(_ext, raw=True).replace([np.inf, -np.inf], np.nan)


# === VOL CLUSTERING (run-length / stationarity diagnostics) ===============


def f17vr_f17_volatility_regime_highvol_clusters_120d_base_v028_signal(closeadj):
    """Count of distinct CLUSTERS of consecutive high-vol-ON bars in last 120d."""
    v = _vol(closeadj, 21)
    def _p90(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        return 1.0 if x[-1] > np.quantile(y[:-1], 0.9) else 0.0
    ind = v.rolling(252, min_periods=60).apply(_p90, raw=True)
    def _cl(x):
        c = 0; prev = 0.0
        for w in x:
            if not np.isfinite(w):
                return np.nan
            if w > 0.5 and prev <= 0.5:
                c += 1
            prev = w
        return float(c)
    return ind.rolling(120, min_periods=60).apply(_cl, raw=True).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_runlen_currentreg_120d_base_v029_signal(closeadj):
    """Average run-length of vol-tercile regimes over trailing 120d."""
    v = _vol(closeadj, 21)
    def _tc(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        a, b = np.quantile(y[:-1], [1/3.0, 2/3.0])
        v0 = x[-1]
        return 1.0 if v0 < a else (2.0 if v0 < b else 3.0)
    reg = v.rolling(252, min_periods=60).apply(_tc, raw=True)
    def _avg(x):
        runs = []; cur = x[0]; cnt = 1
        for w in x[1:]:
            if not np.isfinite(w) or not np.isfinite(cur):
                return np.nan
            if w == cur:
                cnt += 1
            else:
                runs.append(cnt); cur = w; cnt = 1
        runs.append(cnt)
        return float(np.mean(runs))
    return reg.rolling(120, min_periods=60).apply(_avg, raw=True).replace([np.inf, -np.inf], np.nan)


# === EWMA-based regime (fast vs slow vol) =================================


def f17vr_f17_volatility_regime_ewmavol_lam94_base_v030_signal(closeadj):
    """EWMA(0.94) on log-returns squared → fast vol indicator."""
    r = np.log(closeadj / closeadj.shift(1))
    return np.sqrt(r.pow(2).ewm(alpha=1.0 - 0.94, adjust=False, min_periods=20).mean()).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_ewmavoldiff_94m97_base_v031_signal(closeadj):
    """log(EWMA(0.94)/EWMA(0.97)) — fast minus slow EWMA vol differential."""
    r = np.log(closeadj / closeadj.shift(1))
    fast = np.sqrt(r.pow(2).ewm(alpha=1.0 - 0.94, adjust=False, min_periods=20).mean())
    slow = np.sqrt(r.pow(2).ewm(alpha=1.0 - 0.97, adjust=False, min_periods=20).mean())
    return np.log(fast / slow).replace([np.inf, -np.inf], np.nan)


# === VOL SHOCK DETECTION ==================================================


def f17vr_f17_volatility_regime_absret_surprise_60d_base_v032_signal(close):
    """|log-return| - SMA(|log-return|, 60). Surprise component of |r|."""
    a = np.log(close / close.shift(1)).abs()
    return (a - a.rolling(60, min_periods=60).mean()).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_voljump_ind_21d_base_v033_signal(closeadj):
    """Binary: vol(21d).diff(1) > 2 * std(vol(21d).diff(1), 60d)."""
    v = _vol(closeadj, 21)
    d = v.diff(1)
    sd = d.rolling(60, min_periods=30).std()
    return (d > 2.0 * sd).astype(float).where(~d.isna() & ~sd.isna()).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_dayssince_volspike_120d_base_v034_signal(closeadj):
    """Bars since last vol-spike (vol(21d).diff > 2*std), capped 120."""
    v = _vol(closeadj, 21)
    d = v.diff(1)
    sd = d.rolling(60, min_periods=30).std()
    flag = (d > 2.0 * sd).astype(float).where(~d.isna() & ~sd.isna())
    def _bs(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return float(len(x))
        return float(len(x) - 1 - idx[-1])
    return flag.rolling(120, min_periods=40).apply(_bs, raw=True).replace([np.inf, -np.inf], np.nan)


# === REGIME-CLASSIFIED BOUNDED TRANSFORMS =================================


def f17vr_f17_volatility_regime_sigmoid_volresid_120d_base_v035_signal(closeadj):
    """sigmoid of (vol(21d) - linear-trend-of-vol over 120d) / 120d-MAD.
    Detrends vol level then bounds — captures dev-from-vol-trend, not vol level."""
    v = _vol(closeadj, 21)
    def _detr(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        n = len(x); t = np.arange(n, dtype=float)
        muT = t.mean(); muX = x.mean()
        cov = np.sum((t - muT) * (x - muX))
        var = np.sum((t - muT) ** 2)
        if var == 0.0:
            return np.nan
        b = cov / var; a = muX - b * muT
        resid_last = x[-1] - (a + b * t[-1])
        mad = float(np.mean(np.abs(x - np.mean(x))))
        if mad == 0.0:
            return np.nan
        z = resid_last / mad
        return float(1.0 / (1.0 + np.exp(-max(min(z, 30.0), -30.0))))
    return v.rolling(120, min_periods=40).apply(_detr, raw=True).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_arctan_volcurv_60d_base_v036_signal(closeadj):
    """arctan transform of vol(21d) CURVATURE: vol(21d) - 2*vol(21d).shift(10) + vol(21d).shift(20),
    normalized by 60d rolling std of vol. Captures acceleration of regime, not level."""
    v = _vol(closeadj, 21)
    curv = v - 2.0 * v.shift(10) + v.shift(20)
    sd = v.rolling(60, min_periods=20).std()
    z = curv / sd.replace(0.0, np.nan)
    return np.arctan(3.0 * z.clip(-30.0, 30.0)).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_tanh_volsurprise_42d_base_v037_signal(closeadj):
    """tanh of (vol(21d) - SMA(vol(21d), 42)) / std(vol(21d), 42)."""
    v = _vol(closeadj, 21)
    mu = v.rolling(42, min_periods=20).mean()
    sd = v.rolling(42, min_periods=20).std()
    s = (v - mu) / sd.replace(0.0, np.nan)
    return np.tanh(s.clip(-30.0, 30.0)).replace([np.inf, -np.inf], np.nan)


# === TIME-SINCE-REGIME-ENTRY ==============================================


def f17vr_f17_volatility_regime_dayssince_enter_highvol_252d_base_v038_signal(closeadj):
    """Bars since the indicator(high-vol-on, p90/252) last transitioned from 0 to 1."""
    v = _vol(closeadj, 21)
    def _p90(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        return 1.0 if x[-1] > np.quantile(y[:-1], 0.9) else 0.0
    ind = v.rolling(252, min_periods=60).apply(_p90, raw=True)
    enter = ((ind > 0.5) & (ind.shift(1) <= 0.5)).astype(float).where(~ind.isna() & ~ind.shift(1).isna())
    def _bs(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return float(len(x))
        return float(len(x) - 1 - idx[-1])
    return enter.rolling(252, min_periods=60).apply(_bs, raw=True).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_dayssince_exit_lowvol_252d_base_v039_signal(closeadj):
    """Bars since the indicator(low-vol-on, p10/252) last transitioned from 1 to 0."""
    v = _vol(closeadj, 21)
    def _p10(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        return 1.0 if x[-1] < np.quantile(y[:-1], 0.1) else 0.0
    ind = v.rolling(252, min_periods=60).apply(_p10, raw=True)
    exit_ = ((ind < 0.5) & (ind.shift(1) >= 0.5)).astype(float).where(~ind.isna() & ~ind.shift(1).isna())
    def _bs(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return float(len(x))
        return float(len(x) - 1 - idx[-1])
    return exit_.rolling(252, min_periods=60).apply(_bs, raw=True).replace([np.inf, -np.inf], np.nan)


# === CROSS-REGIME COMPARISONS =============================================


def f17vr_f17_volatility_regime_regimewidth_p10p90_252d_base_v040_signal(closeadj):
    """(p90(vol(21d)) - p10(vol(21d))) / median(vol(21d)) over trailing 252d.
    Spread of the vol regime distribution — measures how wide the regime fan is."""
    v = _vol(closeadj, 21)
    p90 = v.rolling(252, min_periods=60).quantile(0.9)
    p10 = v.rolling(252, min_periods=60).quantile(0.1)
    med = v.rolling(252, min_periods=60).median()
    return ((p90 - p10) / med.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_volsign_consistency_42d_base_v041_signal(closeadj):
    """Fraction of 42d window where vol(21d).diff(1) had SAME sign as median of those signs.
    Captures one-sided regime drift (vol going up steadily vs back-and-forth)."""
    v = _vol(closeadj, 21)
    d = v.diff(1)
    s = np.sign(d)
    def _cons(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        if len(x) < 10:
            return np.nan
        m = float(np.sign(np.sum(x)))
        if m == 0.0:
            return 0.5
        return float(np.mean(x == m))
    return s.rolling(42, min_periods=20).apply(_cons, raw=True).replace([np.inf, -np.inf], np.nan)


# === VOL OF VOL (regime instability) ======================================


def f17vr_f17_volatility_regime_volofvol_60d_base_v042_signal(closeadj):
    """std(vol(21d), 60d) — instability of vol-level itself."""
    return _vol(closeadj, 21).rolling(60, min_periods=30).std().replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_vol_corrwith_time_60d_base_v043_signal(closeadj):
    """Pearson correlation of vol(21d) with time-index over 60d.
    Positive=vol rising linearly within window; negative=vol falling. Directional regime tilt."""
    v = _vol(closeadj, 21)
    def _ct(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        n = len(x); t = np.arange(n, dtype=float)
        muT = t.mean(); muX = x.mean()
        cov = np.sum((t - muT) * (x - muX))
        vt = np.sum((t - muT) ** 2); vx = np.sum((x - muX) ** 2)
        if vt == 0.0 or vx == 0.0:
            return np.nan
        return float(cov / np.sqrt(vt * vx))
    return v.rolling(60, min_periods=20).apply(_ct, raw=True).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_consec_vol_uptick_60d_base_v044_signal(closeadj):
    """Longest run of CONSECUTIVE bars with vol(21d).diff(1) > 0 in trailing 60d.
    Maximum sustained-uptick streak — distinct from regime-persistence streak."""
    v = _vol(closeadj, 21)
    d = v.diff(1)
    s = (d > 0).astype(float).where(~d.isna())
    def _maxrun(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        best = 0; cur = 0
        for w in x:
            if w > 0.5:
                cur += 1
                if cur > best: best = cur
            else:
                cur = 0
        return float(best)
    return s.rolling(60, min_periods=20).apply(_maxrun, raw=True).replace([np.inf, -np.inf], np.nan)


# === DECILE-BASED FEATURES ================================================


def f17vr_f17_volatility_regime_vol_zerocrossings_60d_base_v045_signal(closeadj):
    """Count of zero-crossings of (vol(21d) - 60d-trailing-median(vol)) in last 60d.
    Structurally distinct from monotonic rank measures — captures oscillation, not level."""
    v = _vol(closeadj, 21)
    med60 = v.rolling(60, min_periods=20).median()
    d = v - med60
    sgn = np.sign(d)
    cross = (sgn != sgn.shift(1)).astype(float).where(~sgn.isna() & ~sgn.shift(1).isna())
    return cross.rolling(60, min_periods=20).sum().replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_decile_transitions_90d_base_v046_signal(closeadj):
    """Count of |decile changes| > 1 in trailing 90 bars — fast regime switches."""
    v = _vol(closeadj, 21)
    def _r(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        return float(np.floor(np.mean(y[:-1] < x[-1]) * 10.0))
    dc = v.rolling(252, min_periods=60).apply(_r, raw=True)
    chg = (dc.diff().abs() > 1.0).astype(float).where(~dc.isna() & ~dc.shift(1).isna())
    return chg.rolling(90, min_periods=30).sum().replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_volcurvature_15d_base_v047_signal(closeadj):
    """vol(21d) - 2*vol(21d).shift(7) + vol(21d).shift(14). Discrete 2nd-difference of vol.
    Curvature (acceleration) of regime level. Pure 2nd-derivative — orthogonal to level/rank."""
    v = _vol(closeadj, 21)
    return (v - 2.0 * v.shift(7) + v.shift(14)).replace([np.inf, -np.inf], np.nan)


# === MULTI-WINDOW REGIME AGREEMENT ========================================


def f17vr_f17_volatility_regime_nhorizons_inhigh_5to63_base_v048_signal(closeadj):
    """Number of vol-horizons {5,10,21,42,63} in HIGH regime (>p75 of trailing 252d)."""
    def _q4(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        return 1.0 if x[-1] > np.quantile(y[:-1], 0.75) else 0.0
    out = pd.Series(0.0, index=closeadj.index, dtype=float)
    mask = pd.Series(True, index=closeadj.index)
    for h in (5, 10, 21, 42, 63):
        v = _vol(closeadj, h)
        ind = v.rolling(252, min_periods=60).apply(_q4, raw=True)
        out = out + ind.fillna(0.0)
        mask = mask & ~ind.isna()
    return out.where(mask).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_nhorizons_inlow_5to63_base_v049_signal(closeadj):
    """Number of vol-horizons {5,10,21,42,63} in LOW regime (<p25 of trailing 252d)."""
    def _q1(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        return 1.0 if x[-1] < np.quantile(y[:-1], 0.25) else 0.0
    out = pd.Series(0.0, index=closeadj.index, dtype=float)
    mask = pd.Series(True, index=closeadj.index)
    for h in (5, 10, 21, 42, 63):
        v = _vol(closeadj, h)
        ind = v.rolling(252, min_periods=60).apply(_q1, raw=True)
        out = out + ind.fillna(0.0)
        mask = mask & ~ind.isna()
    return out.where(mask).replace([np.inf, -np.inf], np.nan)


# === REGIME-AWARE COMPOSITE ===============================================


def f17vr_f17_volatility_regime_medianvol_horizons_base_v050_signal(closeadj):
    """Median across horizons of vol-percentile-rank (each ranked in own 252d)."""
    def _r(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        return float(np.mean(y[:-1] < x[-1]))
    cols = []
    for h in (10, 21, 42, 63):
        v = _vol(closeadj, h)
        cols.append(v.rolling(252, min_periods=60).apply(_r, raw=True))
    M = pd.concat(cols, axis=1)
    return M.median(axis=1).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_volpctrange_horizons_base_v051_signal(closeadj):
    """Range = max - min of vol-percentile-rank across horizons {10,21,42,63}.
    Measures agreement (small=consensus, large=disagreement) of regime signal."""
    def _r(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        return float(np.mean(y[:-1] < x[-1]))
    cols = []
    for h in (10, 21, 42, 63):
        v = _vol(closeadj, h)
        cols.append(v.rolling(252, min_periods=60).apply(_r, raw=True))
    M = pd.concat(cols, axis=1)
    return (M.max(axis=1) - M.min(axis=1)).replace([np.inf, -np.inf], np.nan)


# === MORE REGIME FEATURES (52-75) =========================================


def f17vr_f17_volatility_regime_volquartile_5on120_base_v052_signal(close):
    """Quartile bucket of vol(5d) within trailing 120d. Short-horizon regime."""
    v = _vol(close, 5)
    def _bk(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 40:
            return np.nan
        qs = np.quantile(y[:-1], [0.25, 0.5, 0.75])
        v0 = x[-1]; b = 1.0
        for q in qs:
            if v0 > q: b += 1.0
        return float(b)
    return v.rolling(120, min_periods=40).apply(_bk, raw=True).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_volquintile_63on500_base_v053_signal(closeadj):
    """Quintile bucket of vol(63d) within trailing 500d. Long-horizon regime."""
    v = _vol(closeadj, 63)
    def _bk(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 100:
            return np.nan
        qs = np.quantile(y[:-1], [0.2, 0.4, 0.6, 0.8])
        v0 = x[-1]; b = 1.0
        for q in qs:
            if v0 > q: b += 1.0
        return float(b)
    return v.rolling(500, min_periods=120).apply(_bk, raw=True).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_volupshocks_count_42d_base_v054_signal(closeadj):
    """Count of bars in last 42d where vol(21d) JUMPED UP by more than 1 unit-MAD.
    Up-move-only shock count, decoupled from net level."""
    v = _vol(closeadj, 21)
    d = v.diff(1)
    mad = d.abs().rolling(60, min_periods=20).median()
    flag = (d > mad).astype(float).where(~d.isna() & ~mad.isna())
    return flag.rolling(42, min_periods=20).sum().replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_volabsdev_med_252d_base_v055_signal(closeadj):
    """|vol(21d) - median(vol(21d), 252d)| — magnitude of regime departure."""
    v = _vol(closeadj, 21)
    med = v.rolling(252, min_periods=60).median()
    return (v - med).abs().replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_vol_skew_ratio_42d_base_v056_signal(closeadj):
    """(p90(vol(21d), 42d) - median(vol(21d), 42d)) / (median - p10).
    Upper-tail-asymmetry of the recent vol distribution. >1 = upper-heavy regime."""
    v = _vol(closeadj, 21)
    p10 = v.rolling(42, min_periods=20).quantile(0.1)
    p50 = v.rolling(42, min_periods=20).median()
    p90 = v.rolling(42, min_periods=20).quantile(0.9)
    return ((p90 - p50) / (p50 - p10).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_volentry_count_p75_120d_base_v057_signal(closeadj):
    """Count of times vol(21d) ENTERED the top-quartile state in last 120 bars."""
    v = _vol(closeadj, 21)
    def _q4(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        return 1.0 if x[-1] >= np.quantile(y[:-1], 0.75) else 0.0
    ind = v.rolling(252, min_periods=60).apply(_q4, raw=True)
    enter = ((ind > 0.5) & (ind.shift(1) <= 0.5)).astype(float).where(~ind.isna() & ~ind.shift(1).isna())
    return enter.rolling(120, min_periods=40).sum().replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_volpctrank_diff_21_42_base_v058_signal(closeadj):
    """Pct-rank(vol(21d), 252d) - Pct-rank(vol(42d), 252d). Short vs mid regime disagreement."""
    def _r(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        return float(np.mean(y[:-1] < x[-1]))
    p21 = _vol(closeadj, 21).rolling(252, min_periods=60).apply(_r, raw=True)
    p42 = _vol(closeadj, 42).rolling(252, min_periods=60).apply(_r, raw=True)
    return (p21 - p42).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_ret_x_volz_42d_base_v059_signal(closeadj):
    """log-return(21d) * vol-z-score(21d on 120d). Regime-tilted momentum."""
    r = np.log(closeadj / closeadj.shift(21))
    v = _vol(closeadj, 21)
    mu = v.rolling(120, min_periods=40).mean()
    sd = v.rolling(120, min_periods=40).std()
    z = (v - mu) / sd.replace(0.0, np.nan)
    return (r * z).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_voljump_freq_252d_base_v060_signal(closeadj):
    """Sum of vol-jump indicators (vol(21d).diff(1) > 2*std) over trailing 252d."""
    v = _vol(closeadj, 21)
    d = v.diff(1)
    sd = d.rolling(60, min_periods=30).std()
    flag = (d > 2.0 * sd).astype(float).where(~d.isna() & ~sd.isna())
    return flag.rolling(252, min_periods=80).sum().replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_signdiff_vol5_vol21_base_v061_signal(close):
    """sign(vol(5d) - vol(21d)). +1 short-vol > long-vol (expansion state)."""
    return np.sign(_vol(close, 5) - _vol(close, 21)).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_vol_drift_30d_base_v062_signal(closeadj):
    """OLS slope of vol(21d) vs time index over 30d, normalized by mean(vol)."""
    v = _vol(closeadj, 21)
    def _slope(x):
        n = len(x); t = np.arange(n, dtype=float)
        mean_t = t.mean(); mean_x = x.mean()
        cov = np.sum((t - mean_t) * (x - mean_x))
        var = np.sum((t - mean_t) ** 2)
        if var == 0.0 or not np.isfinite(mean_x) or mean_x == 0.0:
            return np.nan
        return float((cov / var) / mean_x)
    return v.rolling(30, min_periods=15).apply(_slope, raw=True).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_volupcross_med_252d_base_v063_signal(closeadj):
    """Number of times vol(21d) UP-CROSSED its 252d trailing median in last 120d."""
    v = _vol(closeadj, 21)
    med = v.rolling(252, min_periods=60).median()
    above = (v > med).astype(float).where(~v.isna() & ~med.isna())
    cross = ((above > 0.5) & (above.shift(1) <= 0.5)).astype(float).where(~above.isna() & ~above.shift(1).isna())
    return cross.rolling(120, min_periods=40).sum().replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_volstreak_above_med_60d_base_v064_signal(closeadj):
    """Consecutive bars where vol(21d) > its 252d median, capped 60."""
    v = _vol(closeadj, 21)
    med = v.rolling(252, min_periods=60).median()
    above = (v > med).astype(float).where(~v.isna() & ~med.isna())
    def _consec(x):
        c = 0
        for w in x[::-1]:
            if not np.isfinite(w):
                return np.nan
            if w > 0.5:
                c += 1
            else:
                break
        return float(c)
    return above.rolling(60, min_periods=30).apply(_consec, raw=True).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_max_time_in_currentreg_180d_base_v065_signal(closeadj):
    """Maximum run-length of CURRENT vol-tercile regime within last 180 bars."""
    v = _vol(closeadj, 21)
    def _tc(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        a, b = np.quantile(y[:-1], [1/3.0, 2/3.0])
        v0 = x[-1]
        return 1.0 if v0 < a else (2.0 if v0 < b else 3.0)
    reg = v.rolling(252, min_periods=60).apply(_tc, raw=True)
    def _maxrun(x):
        cur = x[-1]
        if not np.isfinite(cur):
            return np.nan
        runs = []; rcur = x[0]; cnt = 1
        for w in x[1:]:
            if not np.isfinite(w):
                return np.nan
            if w == rcur:
                cnt += 1
            else:
                if rcur == cur:
                    runs.append(cnt)
                rcur = w; cnt = 1
        if rcur == cur:
            runs.append(cnt)
        if not runs:
            return 0.0
        return float(max(runs))
    return reg.rolling(180, min_periods=60).apply(_maxrun, raw=True).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_kurt_vol21_60d_base_v066_signal(closeadj):
    """Rolling kurtosis of vol(21d) over 60d — fat-tailed regime instability."""
    return _vol(closeadj, 21).rolling(60, min_periods=30).kurt().replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_skew_vol21_60d_base_v067_signal(closeadj):
    """Rolling skewness of vol(21d) over 60d — asymmetric regime."""
    return _vol(closeadj, 21).rolling(60, min_periods=30).skew().replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_madstd_vol21_60d_base_v068_signal(closeadj):
    """MAD/std of vol(21d) over 60d — robustness of regime-level estimate."""
    v = _vol(closeadj, 21)
    mad = v.rolling(60, min_periods=30).apply(lambda x: float(np.mean(np.abs(x - np.mean(x)))), raw=True)
    sd = v.rolling(60, min_periods=30).std()
    return (mad / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_signagree_p75_5_21_63_base_v069_signal(closeadj):
    """Agreement: are all three horizons (5,21,63) simultaneously above p75 of their 252d?
    Returns 1 if all three high, -1 if all three low, 0 otherwise."""
    def _q4(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        return 1.0 if x[-1] > np.quantile(y[:-1], 0.75) else 0.0
    def _q1(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        return 1.0 if x[-1] < np.quantile(y[:-1], 0.25) else 0.0
    cols_hi = []; cols_lo = []
    for h in (5, 21, 63):
        v = _vol(closeadj, h)
        cols_hi.append(v.rolling(252, min_periods=60).apply(_q4, raw=True))
        cols_lo.append(v.rolling(252, min_periods=60).apply(_q1, raw=True))
    H = pd.concat(cols_hi, axis=1).sum(axis=1)
    L = pd.concat(cols_lo, axis=1).sum(axis=1)
    out = pd.Series(0.0, index=closeadj.index, dtype=float)
    out = out.where(~H.isna() & ~L.isna())
    out = out.mask(H >= 3.0, 1.0).mask(L >= 3.0, -1.0)
    return out.replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_volstability_iqr_120d_base_v070_signal(closeadj):
    """IQR of vol(21d) in trailing 120d divided by its median — relative dispersion of regime."""
    v = _vol(closeadj, 21)
    q1 = v.rolling(120, min_periods=40).quantile(0.25)
    q3 = v.rolling(120, min_periods=40).quantile(0.75)
    med = v.rolling(120, min_periods=40).median()
    return ((q3 - q1) / med.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_volz_centered_500d_base_v071_signal(closeadj):
    """vol(21d) Z-score using trailing 500d distribution. Long-history regime z."""
    v = _vol(closeadj, 21)
    mu = v.rolling(500, min_periods=120).mean()
    sd = v.rolling(500, min_periods=120).std()
    return ((v - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_volrank_diff_short_long_base_v072_signal(closeadj):
    """pct-rank(vol(5d) in 120d) - pct-rank(vol(63d) in 500d). Term-disagreement-of-RANK."""
    def _r60(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 40:
            return np.nan
        return float(np.mean(y[:-1] < x[-1]))
    def _r120(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 100:
            return np.nan
        return float(np.mean(y[:-1] < x[-1]))
    a = _vol(closeadj, 5).rolling(120, min_periods=40).apply(_r60, raw=True)
    b = _vol(closeadj, 63).rolling(500, min_periods=120).apply(_r120, raw=True)
    return (a - b).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_dayssince_minvol_252d_base_v073_signal(closeadj):
    """Bars since vol(21d) was at its 252d-trailing minimum."""
    v = _vol(closeadj, 21)
    def _bs(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        i = int(np.argmin(x))
        return float(len(x) - 1 - i)
    return v.rolling(252, min_periods=60).apply(_bs, raw=True).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_dayssince_maxvol_252d_base_v074_signal(closeadj):
    """Bars since vol(21d) was at its 252d-trailing maximum."""
    v = _vol(closeadj, 21)
    def _bs(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        i = int(np.argmax(x))
        return float(len(x) - 1 - i)
    return v.rolling(252, min_periods=60).apply(_bs, raw=True).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_volminusewma_94_base_v075_signal(closeadj):
    """log(vol(21d)) - log(sqrt(EWMA_lam94(r^2))). Sample vol vs filtered EWMA vol level."""
    v21 = _vol(closeadj, 21)
    r = np.log(closeadj / closeadj.shift(1))
    ewmav = np.sqrt(r.pow(2).ewm(alpha=1.0 - 0.94, adjust=False, min_periods=20).mean())
    return (np.log(v21) - np.log(ewmav)).replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f17_volatility_regime_base_001_075_REGISTRY = {
    "f17vr_f17_volatility_regime_volquartile_21on252_base_v001_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_volquartile_21on252_base_v001_signal},
    "f17vr_f17_volatility_regime_quintile_chg_ind_21on252_base_v002_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_quintile_chg_ind_21on252_base_v002_signal},
    "f17vr_f17_volatility_regime_decile_absret_120d_base_v003_signal": {"inputs": ["close"], "func": f17vr_f17_volatility_regime_decile_absret_120d_base_v003_signal},
    "f17vr_f17_volatility_regime_volquartile1_ind_21d_base_v004_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_volquartile1_ind_21d_base_v004_signal},
    "f17vr_f17_volatility_regime_volquartile4_ind_21d_base_v005_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_volquartile4_ind_21d_base_v005_signal},
    "f17vr_f17_volatility_regime_multih_quintile_5_21_63_base_v006_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_multih_quintile_5_21_63_base_v006_signal},
    "f17vr_f17_volatility_regime_vol21_over_med252_base_v007_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_vol21_over_med252_base_v007_signal},
    "f17vr_f17_volatility_regime_volz_21on252_base_v008_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_volz_21on252_base_v008_signal},
    "f17vr_f17_volatility_regime_volpctrank_21on120_base_v009_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_volpctrank_21on120_base_v009_signal},
    "f17vr_f17_volatility_regime_volpctrank_42on500_base_v010_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_volpctrank_42on500_base_v010_signal},
    "f17vr_f17_volatility_regime_volpct_largeret_42d_base_v011_signal": {"inputs": ["close"], "func": f17vr_f17_volatility_regime_volpct_largeret_42d_base_v011_signal},
    "f17vr_f17_volatility_regime_regimestab_frac_60d_base_v012_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_regimestab_frac_60d_base_v012_signal},
    "f17vr_f17_volatility_regime_transitioncount_90d_base_v013_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_transitioncount_90d_base_v013_signal},
    "f17vr_f17_volatility_regime_volexpansion_5m63_base_v014_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_volexpansion_5m63_base_v014_signal},
    "f17vr_f17_volatility_regime_streak_currentregime_60d_base_v015_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_streak_currentregime_60d_base_v015_signal},
    "f17vr_f17_volatility_regime_vol_HLrange_pct_42d_base_v016_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_vol_HLrange_pct_42d_base_v016_signal},
    "f17vr_f17_volatility_regime_daysinhighvol_120d_base_v017_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_daysinhighvol_120d_base_v017_signal},
    "f17vr_f17_volatility_regime_regime_autocorr_80d_base_v018_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_regime_autocorr_80d_base_v018_signal},
    "f17vr_f17_volatility_regime_ret_x_highvol_ind_base_v019_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_ret_x_highvol_ind_base_v019_signal},
    "f17vr_f17_volatility_regime_ret_x_lowvol_ind_base_v020_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_ret_x_lowvol_ind_base_v020_signal},
    "f17vr_f17_volatility_regime_sharpe_42d_currentvol_base_v021_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_sharpe_42d_currentvol_base_v021_signal},
    "f17vr_f17_volatility_regime_volresid_AR1_120d_base_v022_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_volresid_AR1_120d_base_v022_signal},
    "f17vr_f17_volatility_regime_volgap_pct_42on252_base_v023_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_volgap_pct_42on252_base_v023_signal},
    "f17vr_f17_volatility_regime_highvolon_p90_base_v024_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_highvolon_p90_base_v024_signal},
    "f17vr_f17_volatility_regime_lowvolon_p10_base_v025_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_lowvolon_p10_base_v025_signal},
    "f17vr_f17_volatility_regime_expanding_state_42d_base_v026_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_expanding_state_42d_base_v026_signal},
    "f17vr_f17_volatility_regime_extreme_state_120d_base_v027_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_extreme_state_120d_base_v027_signal},
    "f17vr_f17_volatility_regime_highvol_clusters_120d_base_v028_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_highvol_clusters_120d_base_v028_signal},
    "f17vr_f17_volatility_regime_runlen_currentreg_120d_base_v029_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_runlen_currentreg_120d_base_v029_signal},
    "f17vr_f17_volatility_regime_ewmavol_lam94_base_v030_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_ewmavol_lam94_base_v030_signal},
    "f17vr_f17_volatility_regime_ewmavoldiff_94m97_base_v031_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_ewmavoldiff_94m97_base_v031_signal},
    "f17vr_f17_volatility_regime_absret_surprise_60d_base_v032_signal": {"inputs": ["close"], "func": f17vr_f17_volatility_regime_absret_surprise_60d_base_v032_signal},
    "f17vr_f17_volatility_regime_voljump_ind_21d_base_v033_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_voljump_ind_21d_base_v033_signal},
    "f17vr_f17_volatility_regime_dayssince_volspike_120d_base_v034_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_dayssince_volspike_120d_base_v034_signal},
    "f17vr_f17_volatility_regime_sigmoid_volresid_120d_base_v035_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_sigmoid_volresid_120d_base_v035_signal},
    "f17vr_f17_volatility_regime_arctan_volcurv_60d_base_v036_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_arctan_volcurv_60d_base_v036_signal},
    "f17vr_f17_volatility_regime_tanh_volsurprise_42d_base_v037_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_tanh_volsurprise_42d_base_v037_signal},
    "f17vr_f17_volatility_regime_dayssince_enter_highvol_252d_base_v038_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_dayssince_enter_highvol_252d_base_v038_signal},
    "f17vr_f17_volatility_regime_dayssince_exit_lowvol_252d_base_v039_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_dayssince_exit_lowvol_252d_base_v039_signal},
    "f17vr_f17_volatility_regime_regimewidth_p10p90_252d_base_v040_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_regimewidth_p10p90_252d_base_v040_signal},
    "f17vr_f17_volatility_regime_volsign_consistency_42d_base_v041_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_volsign_consistency_42d_base_v041_signal},
    "f17vr_f17_volatility_regime_volofvol_60d_base_v042_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_volofvol_60d_base_v042_signal},
    "f17vr_f17_volatility_regime_vol_corrwith_time_60d_base_v043_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_vol_corrwith_time_60d_base_v043_signal},
    "f17vr_f17_volatility_regime_consec_vol_uptick_60d_base_v044_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_consec_vol_uptick_60d_base_v044_signal},
    "f17vr_f17_volatility_regime_vol_zerocrossings_60d_base_v045_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_vol_zerocrossings_60d_base_v045_signal},
    "f17vr_f17_volatility_regime_decile_transitions_90d_base_v046_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_decile_transitions_90d_base_v046_signal},
    "f17vr_f17_volatility_regime_volcurvature_15d_base_v047_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_volcurvature_15d_base_v047_signal},
    "f17vr_f17_volatility_regime_nhorizons_inhigh_5to63_base_v048_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_nhorizons_inhigh_5to63_base_v048_signal},
    "f17vr_f17_volatility_regime_nhorizons_inlow_5to63_base_v049_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_nhorizons_inlow_5to63_base_v049_signal},
    "f17vr_f17_volatility_regime_medianvol_horizons_base_v050_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_medianvol_horizons_base_v050_signal},
    "f17vr_f17_volatility_regime_volpctrange_horizons_base_v051_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_volpctrange_horizons_base_v051_signal},
    "f17vr_f17_volatility_regime_volquartile_5on120_base_v052_signal": {"inputs": ["close"], "func": f17vr_f17_volatility_regime_volquartile_5on120_base_v052_signal},
    "f17vr_f17_volatility_regime_volquintile_63on500_base_v053_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_volquintile_63on500_base_v053_signal},
    "f17vr_f17_volatility_regime_volupshocks_count_42d_base_v054_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_volupshocks_count_42d_base_v054_signal},
    "f17vr_f17_volatility_regime_volabsdev_med_252d_base_v055_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_volabsdev_med_252d_base_v055_signal},
    "f17vr_f17_volatility_regime_vol_skew_ratio_42d_base_v056_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_vol_skew_ratio_42d_base_v056_signal},
    "f17vr_f17_volatility_regime_volentry_count_p75_120d_base_v057_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_volentry_count_p75_120d_base_v057_signal},
    "f17vr_f17_volatility_regime_volpctrank_diff_21_42_base_v058_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_volpctrank_diff_21_42_base_v058_signal},
    "f17vr_f17_volatility_regime_ret_x_volz_42d_base_v059_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_ret_x_volz_42d_base_v059_signal},
    "f17vr_f17_volatility_regime_voljump_freq_252d_base_v060_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_voljump_freq_252d_base_v060_signal},
    "f17vr_f17_volatility_regime_signdiff_vol5_vol21_base_v061_signal": {"inputs": ["close"], "func": f17vr_f17_volatility_regime_signdiff_vol5_vol21_base_v061_signal},
    "f17vr_f17_volatility_regime_vol_drift_30d_base_v062_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_vol_drift_30d_base_v062_signal},
    "f17vr_f17_volatility_regime_volupcross_med_252d_base_v063_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_volupcross_med_252d_base_v063_signal},
    "f17vr_f17_volatility_regime_volstreak_above_med_60d_base_v064_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_volstreak_above_med_60d_base_v064_signal},
    "f17vr_f17_volatility_regime_max_time_in_currentreg_180d_base_v065_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_max_time_in_currentreg_180d_base_v065_signal},
    "f17vr_f17_volatility_regime_kurt_vol21_60d_base_v066_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_kurt_vol21_60d_base_v066_signal},
    "f17vr_f17_volatility_regime_skew_vol21_60d_base_v067_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_skew_vol21_60d_base_v067_signal},
    "f17vr_f17_volatility_regime_madstd_vol21_60d_base_v068_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_madstd_vol21_60d_base_v068_signal},
    "f17vr_f17_volatility_regime_signagree_p75_5_21_63_base_v069_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_signagree_p75_5_21_63_base_v069_signal},
    "f17vr_f17_volatility_regime_volstability_iqr_120d_base_v070_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_volstability_iqr_120d_base_v070_signal},
    "f17vr_f17_volatility_regime_volz_centered_500d_base_v071_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_volz_centered_500d_base_v071_signal},
    "f17vr_f17_volatility_regime_volrank_diff_short_long_base_v072_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_volrank_diff_short_long_base_v072_signal},
    "f17vr_f17_volatility_regime_dayssince_minvol_252d_base_v073_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_dayssince_minvol_252d_base_v073_signal},
    "f17vr_f17_volatility_regime_dayssince_maxvol_252d_base_v074_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_dayssince_maxvol_252d_base_v074_signal},
    "f17vr_f17_volatility_regime_volminusewma_94_base_v075_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_volminusewma_94_base_v075_signal},
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
    for name, entry in f17_volatility_regime_base_001_075_REGISTRY.items():
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
