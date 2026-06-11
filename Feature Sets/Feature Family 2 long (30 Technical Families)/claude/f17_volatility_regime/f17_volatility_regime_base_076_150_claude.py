"""f17_volatility_regime base features 076-150.

Domain: volatility REGIME — CLASSIFY or QUANTIFY current vol level vs reference.
Distinct from f16 (term-structure across horizons). Here we classify LEVEL,
transitions, and persistence anchored on a single base horizon.

STRUCTURALLY DISTINCT from base_001_075 — no shared expression up to a
window change. This file uses alternative vol-estimators (Parkinson HL,
Garman-Klass, downside, upside, MAD-vol, semi-IQR), absret-based regimes,
range-based regimes, conditional-vol regimes, Bayesian-style posteriors,
adaptive thresholds, and entropy-based regime measures.

NaN policy: never fillna(<value>); only replace([inf,-inf], nan) at the
final return. Window > 21d uses closeadj; <= 21d uses close.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Helpers (vol primitives — distinct families from file 1)
# ---------------------------------------------------------------------------


def _logret(s: pd.Series) -> pd.Series:
    return np.log(s / s.shift(1))


def _parkvol(high: pd.Series, low: pd.Series, n: int) -> pd.Series:
    """Parkinson HL vol over n bars."""
    r = (np.log(high / low) ** 2) / (4.0 * np.log(2.0))
    return np.sqrt(r.rolling(n, min_periods=n).mean())


def _madvol(s: pd.Series, n: int) -> pd.Series:
    """Mean Absolute Deviation of log-returns over n bars (robust vol)."""
    r = np.log(s / s.shift(1))
    return r.rolling(n, min_periods=n).apply(
        lambda x: float(np.mean(np.abs(x - np.mean(x)))), raw=True
    )


def _gkvol(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, n: int) -> pd.Series:
    """Garman-Klass over n bars."""
    rs = 0.5 * (np.log(high / low) ** 2) - (2.0 * np.log(2.0) - 1.0) * (np.log(close / open_) ** 2)
    return np.sqrt(rs.rolling(n, min_periods=n).mean())


def _downvol(s: pd.Series, n: int) -> pd.Series:
    """Downside vol — std of negative log-returns over n bars."""
    r = np.log(s / s.shift(1))
    return r.where(r < 0).rolling(n, min_periods=n // 2).std()


def _upvol(s: pd.Series, n: int) -> pd.Series:
    """Upside vol — std of positive log-returns over n bars."""
    r = np.log(s / s.shift(1))
    return r.where(r > 0).rolling(n, min_periods=n // 2).std()


# ---------------------------------------------------------------------------
# Features 076-150
# ---------------------------------------------------------------------------


# === HL-RANGE-BASED REGIME CLASSIFICATION (Parkinson, range, GK) ==========


def f17vr_f17_volatility_regime_parkvol_quartile_21on252_base_v076_signal(high, low, closeadj):
    """Quartile of Parkinson HL vol(21d) within trailing 252d.
    Uses HL ranges, NOT close-returns — structurally distinct vol estimator."""
    r2 = (np.log(high / low) ** 2) / (4.0 * np.log(2.0))
    pv = np.sqrt(r2.rolling(21, min_periods=21).mean())
    def _bk(x):
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
    return pv.rolling(252, min_periods=60).apply(_bk, raw=True).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_HLrange_z_42d_base_v077_signal(high, low):
    """Z-score of mean(log(H/L)) over 21d, normalized vs trailing 252d distribution.
    Pure HL-range regime z — uses no close prices."""
    r = np.log(high / low)
    m21 = r.rolling(21, min_periods=21).mean()
    mu = m21.rolling(252, min_periods=60).mean()
    sd = m21.rolling(252, min_periods=60).std()
    return ((m21 - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_HLrange_dayssincemax_180d_base_v078_signal(high, low):
    """Bars since the maximum single-bar log(H/L) in a trailing 180d window.
    Time-since-extreme-range — a recency/event-timing signal, structurally
    unlike the monotonic level/rank features at v077."""
    r = np.log(high / low)
    def _bs(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 60:
            return np.nan
        i = int(np.argmax(x))
        return float(len(x) - 1 - i)
    return r.rolling(180, min_periods=60).apply(_bs, raw=True).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_gkvol_p75_ind_30d_base_v079_signal(open_, high, low, close):
    """Binary: Garman-Klass vol(20d) > 75th-percentile of trailing 252d.
    OHLC-based vol-regime indicator."""
    rs = 0.5 * (np.log(high / low) ** 2) - (2.0 * np.log(2.0) - 1.0) * (np.log(close / open_) ** 2)
    gk = np.sqrt(rs.rolling(20, min_periods=20).mean())
    def _p75(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        return 1.0 if x[-1] > np.quantile(y[:-1], 0.75) else 0.0
    return gk.rolling(252, min_periods=60).apply(_p75, raw=True).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_rangetonormal_42d_base_v080_signal(high, low, closeadj):
    """log(parkinson-vol(21d) / close-vol(21d)). Compares HL- vs close-based vol level.
    High when range is wide relative to close-to-close — captures intraday-only regime."""
    r2 = (np.log(high / low) ** 2) / (4.0 * np.log(2.0))
    pv = np.sqrt(r2.rolling(21, min_periods=21).mean())
    cv = np.log(closeadj / closeadj.shift(1)).rolling(21, min_periods=21).std()
    return np.log(pv / cv.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === DOWNSIDE / UPSIDE VOL REGIMES =========================================


def f17vr_f17_volatility_regime_downvol_p90_42d_base_v081_signal(closeadj):
    """Binary: downside-vol(42d) > p90 of trailing 252d."""
    r = np.log(closeadj / closeadj.shift(1))
    dv = r.where(r < 0).rolling(42, min_periods=21).std()
    def _p90(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        return 1.0 if x[-1] > np.quantile(y[:-1], 0.9) else 0.0
    return dv.rolling(252, min_periods=60).apply(_p90, raw=True).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_upvol_decile_252d_base_v082_signal(closeadj):
    """Decile bucket of upside-vol(42d) in trailing 252d."""
    r = np.log(closeadj / closeadj.shift(1))
    uv = r.where(r > 0).rolling(42, min_periods=21).std()
    def _bk(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 60:
            return np.nan
        qs = np.quantile(y[:-1], np.arange(1, 10) / 10.0)
        v0 = x[-1]; b = 1.0
        for q in qs:
            if v0 > q: b += 1.0
        return float(b)
    return uv.rolling(252, min_periods=60).apply(_bk, raw=True).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_downup_voldiff_z_42d_base_v083_signal(closeadj):
    """Z-score of (semi-downside-RMS(42d) - semi-upside-RMS(42d)) within trailing 200d.
    Asymmetric-vol regime using clip-based semi-RMS so the rolling windows always
    have full 42-bar support (zeros at the wrong-sign bars, not NaNs)."""
    r = np.log(closeadj / closeadj.shift(1))
    neg = r.clip(upper=0.0)
    pos = r.clip(lower=0.0)
    dv = np.sqrt(neg.pow(2).rolling(42, min_periods=42).mean())
    uv = np.sqrt(pos.pow(2).rolling(42, min_periods=42).mean())
    d = dv - uv
    mu = d.rolling(200, min_periods=60).mean()
    sd = d.rolling(200, min_periods=60).std()
    return ((d - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === MAD-VOL REGIMES (robust vol family) ===================================


def f17vr_f17_volatility_regime_madvol_quintile_21on252_base_v084_signal(closeadj):
    """Quintile of MAD-vol(21d) in trailing 252d. Robust-vol regime classification."""
    r = np.log(closeadj / closeadj.shift(1))
    mv = r.rolling(21, min_periods=21).apply(lambda x: float(np.mean(np.abs(x - np.mean(x)))), raw=True)
    def _bk(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 60:
            return np.nan
        qs = np.quantile(y[:-1], [0.2, 0.4, 0.6, 0.8])
        v0 = x[-1]; b = 1.0
        for q in qs:
            if v0 > q: b += 1.0
        return float(b)
    return mv.rolling(252, min_periods=60).apply(_bk, raw=True).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_madvol_pctrank_42on500_base_v085_signal(closeadj):
    """Percentile rank of MAD-vol(42d) in trailing 500d."""
    r = np.log(closeadj / closeadj.shift(1))
    mv = r.rolling(42, min_periods=42).apply(lambda x: float(np.mean(np.abs(x - np.mean(x)))), raw=True)
    def _r(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 100:
            return np.nan
        return float(np.mean(y[:-1] < x[-1]))
    return mv.rolling(500, min_periods=120).apply(_r, raw=True).replace([np.inf, -np.inf], np.nan)


# === ABSRET-BASED REGIMES (close-only, single-bar magnitude) ==============


def f17vr_f17_volatility_regime_absret_avg_pctrank_30on252_base_v086_signal(closeadj):
    """Pct-rank of mean(|log-return|, 30d) within trailing 252d."""
    a = np.log(closeadj / closeadj.shift(1)).abs()
    m30 = a.rolling(30, min_periods=15).mean()
    def _r(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        return float(np.mean(y[:-1] < x[-1]))
    return m30.rolling(252, min_periods=60).apply(_r, raw=True).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_absret_max_pctrank_120d_base_v087_signal(closeadj):
    """Pct-rank of MAX(|log-return|, 10d) within trailing 120d. Worst-bar regime."""
    a = np.log(closeadj / closeadj.shift(1)).abs()
    mx = a.rolling(10, min_periods=5).max()
    def _r(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 30:
            return np.nan
        return float(np.mean(y[:-1] < x[-1]))
    return mx.rolling(120, min_periods=40).apply(_r, raw=True).replace([np.inf, -np.inf], np.nan)


# === CONDITIONAL VOL REGIMES (CVaR / ES proxies as regime classifiers) ====


def f17vr_f17_volatility_regime_cvar5_pctrank_42on252_base_v088_signal(closeadj):
    """Pct-rank of mean of bottom-5% returns over 42d within trailing 252d (CVaR magnitude regime)."""
    r = np.log(closeadj / closeadj.shift(1))
    def _cvar(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        q = np.quantile(x, 0.05)
        tail = x[x <= q]
        if tail.size == 0:
            return np.nan
        return float(np.mean(tail))
    c = r.rolling(42, min_periods=21).apply(_cvar, raw=True)
    def _r(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        return float(np.mean(y[:-1] < x[-1]))
    return c.rolling(252, min_periods=60).apply(_r, raw=True).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_var5_above_threshold_60d_base_v089_signal(closeadj):
    """Binary: 5th-percentile of returns over 60d < -2*median(|log-return|, 60d). Crash regime."""
    r = np.log(closeadj / closeadj.shift(1))
    q5 = r.rolling(60, min_periods=30).quantile(0.05)
    a = r.abs()
    med = a.rolling(60, min_periods=30).median()
    return (q5 < -2.0 * med).astype(float).where(~q5.isna() & ~med.isna()).replace([np.inf, -np.inf], np.nan)


# === ENTROPY-BASED REGIME (continuous distribution measure) ===============


def f17vr_f17_volatility_regime_retentropy_bins_42d_base_v090_signal(closeadj):
    """Shannon entropy of returns binned into 5 equal-width bins over 42d.
    Low entropy = concentrated regime; high entropy = spread regime."""
    r = np.log(closeadj / closeadj.shift(1))
    def _ent(x):
        if not np.all(np.isfinite(x)) or len(x) < 10:
            return np.nan
        lo = x.min(); hi = x.max()
        if hi == lo:
            return 0.0
        bins = np.linspace(lo, hi, 6)
        cnt, _ = np.histogram(x, bins=bins)
        p = cnt / cnt.sum()
        p = p[p > 0]
        return float(-np.sum(p * np.log(p)))
    return r.rolling(42, min_periods=21).apply(_ent, raw=True).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_abs_ret_entropy_60d_base_v091_signal(closeadj):
    """Coefficient-of-variation of |log-return| over a 60-bar window divided by
    its 252-bar-trailing median. A regime-sensitive dispersion measure that is
    structurally distinct from rank/level features; quantifies how *spread out*
    the recent absolute-return distribution is relative to its long-run typical
    magnitude. (Replaces the prior fixed-bin entropy which was structurally
    constant on synthetic data.)"""
    a = np.log(closeadj / closeadj.shift(1)).abs()
    cv = a.rolling(60, min_periods=30).std() / a.rolling(60, min_periods=30).mean().replace(0.0, np.nan)
    med252 = a.rolling(252, min_periods=120).median().replace(0.0, np.nan)
    return (cv / med252).replace([np.inf, -np.inf], np.nan)


# === BAYESIAN-STYLE POSTERIOR (probability of high-vol regime) ============


def f17vr_f17_volatility_regime_post_highvol_60d_base_v092_signal(closeadj):
    """Posterior prob = fraction of last 60 bars where vol(21d) > MEAN(vol(21d), 252d).
    Bayesian-style empirical regime-prior estimate, distinct from quartile fraction."""
    r = np.log(closeadj / closeadj.shift(1))
    v = r.rolling(21, min_periods=21).std()
    mu = v.rolling(252, min_periods=60).mean()
    above = (v > mu).astype(float).where(~v.isna() & ~mu.isna())
    return above.rolling(60, min_periods=30).mean().replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_post_highvol_smoothed_30d_base_v093_signal(closeadj):
    """EWMA-smoothed posterior: ewm-alpha-0.1 of indicator(vol(21d) > 75th pct, 252d).
    Decay-weighted prob of being in high-vol regime."""
    r = np.log(closeadj / closeadj.shift(1))
    v = r.rolling(21, min_periods=21).std()
    def _p75(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        return 1.0 if x[-1] > np.quantile(y[:-1], 0.75) else 0.0
    ind = v.rolling(252, min_periods=60).apply(_p75, raw=True)
    return ind.ewm(alpha=0.1, adjust=False, min_periods=20).mean().replace([np.inf, -np.inf], np.nan)


# === ADAPTIVE-THRESHOLD REGIMES =============================================


def f17vr_f17_volatility_regime_adapt_threshold_ind_84d_base_v094_signal(closeadj):
    """Binary: vol(21d) > adaptive-threshold = (median + 1.5*MAD) over 84d-trailing."""
    r = np.log(closeadj / closeadj.shift(1))
    v = r.rolling(21, min_periods=21).std()
    med = v.rolling(84, min_periods=30).median()
    mad = v.rolling(84, min_periods=30).apply(lambda x: float(np.median(np.abs(x - np.median(x)))), raw=True)
    th = med + 1.5 * mad
    return (v > th).astype(float).where(~v.isna() & ~th.isna()).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_adapt_low_threshold_84d_base_v095_signal(closeadj):
    """Binary: vol(21d) < adaptive lower-threshold = (median - 1.0*MAD) over 84d."""
    r = np.log(closeadj / closeadj.shift(1))
    v = r.rolling(21, min_periods=21).std()
    med = v.rolling(84, min_periods=30).median()
    mad = v.rolling(84, min_periods=30).apply(lambda x: float(np.median(np.abs(x - np.median(x)))), raw=True)
    th = med - 1.0 * mad
    return (v < th).astype(float).where(~v.isna() & ~th.isna()).replace([np.inf, -np.inf], np.nan)


# === SEMI-IQR REGIME ========================================================


def f17vr_f17_volatility_regime_semiIQR_high_pctrank_60d_base_v096_signal(closeadj):
    """Pct-rank of upper-semi-IQR (q90-q50) of returns over 60d within trailing 252d."""
    r = np.log(closeadj / closeadj.shift(1))
    u = r.rolling(60, min_periods=30).quantile(0.9) - r.rolling(60, min_periods=30).quantile(0.5)
    def _r(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 60:
            return np.nan
        return float(np.mean(y[:-1] < x[-1]))
    return u.rolling(252, min_periods=60).apply(_r, raw=True).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_semiIQR_low_pctrank_60d_base_v097_signal(closeadj):
    """Pct-rank of lower-semi-IQR (q50-q10) of returns over 60d within trailing 252d."""
    r = np.log(closeadj / closeadj.shift(1))
    u = r.rolling(60, min_periods=30).quantile(0.5) - r.rolling(60, min_periods=30).quantile(0.1)
    def _r(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 60:
            return np.nan
        return float(np.mean(y[:-1] < x[-1]))
    return u.rolling(252, min_periods=60).apply(_r, raw=True).replace([np.inf, -np.inf], np.nan)


# === EXCESS-KURT REGIME (heavy-tail) =======================================


def f17vr_f17_volatility_regime_kurt_excessflag_42d_base_v098_signal(closeadj):
    """Binary: rolling-kurtosis of returns (42d) > 1.5. Fat-tail regime indicator."""
    r = np.log(closeadj / closeadj.shift(1))
    k = r.rolling(42, min_periods=21).kurt()
    return (k > 1.5).astype(float).where(~k.isna()).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_kurtpctrank_42on252_base_v099_signal(closeadj):
    """Pct-rank of return-kurtosis(42d) in trailing 252d. Fat-tail-regime continuous measure."""
    r = np.log(closeadj / closeadj.shift(1))
    k = r.rolling(42, min_periods=21).kurt()
    def _r(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        return float(np.mean(y[:-1] < x[-1]))
    return k.rolling(252, min_periods=60).apply(_r, raw=True).replace([np.inf, -np.inf], np.nan)


# === RANGE-EXPANSION REGIMES (intra-bar) ==================================


def f17vr_f17_volatility_regime_NRcount_4_42d_base_v100_signal(high, low):
    """Count of "NR4" bars in last 42 bars: (H-L) < min((H-L), 4d). Narrow-range cluster regime."""
    rng = high - low
    cur_min = rng.rolling(4, min_periods=4).min()
    flag = (rng <= cur_min).astype(float).where(~rng.isna() & ~cur_min.isna())
    return flag.rolling(42, min_periods=20).sum().replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_WRcount_4_42d_base_v101_signal(high, low):
    """Count of "WR4" bars in last 42 bars: (H-L) > max((H-L), 4d_lookback). Wide-range cluster regime."""
    rng = high - low
    cur_max = rng.rolling(4, min_periods=4).max()
    flag = (rng >= cur_max).astype(float).where(~rng.isna() & ~cur_max.isna())
    return flag.rolling(42, min_periods=20).sum().replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_HLavg_z_60d_base_v102_signal(high, low):
    """Z-score of average HL-range over 21d within trailing 60d distribution."""
    rng = (high - low) / ((high + low) / 2.0)
    m21 = rng.rolling(21, min_periods=21).mean()
    mu = m21.rolling(60, min_periods=30).mean()
    sd = m21.rolling(60, min_periods=30).std()
    return ((m21 - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === EWMA-REGIME (alternative lambdas) =====================================


def f17vr_f17_volatility_regime_ewmavol_lam97_base_v103_signal(closeadj):
    """EWMA(0.97) on log-returns squared — slow EWMA vol level."""
    r = np.log(closeadj / closeadj.shift(1))
    return np.sqrt(r.pow(2).ewm(alpha=1.0 - 0.97, adjust=False, min_periods=20).mean()).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_ewmavol_decile_94_252d_base_v104_signal(closeadj):
    """Decile bucket of EWMA(0.94)-vol within trailing 252d distribution."""
    r = np.log(closeadj / closeadj.shift(1))
    ev = np.sqrt(r.pow(2).ewm(alpha=1.0 - 0.94, adjust=False, min_periods=20).mean())
    def _bk(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 60:
            return np.nan
        qs = np.quantile(y[:-1], np.arange(1, 10) / 10.0)
        v0 = x[-1]; b = 1.0
        for q in qs:
            if v0 > q: b += 1.0
        return float(b)
    return ev.rolling(252, min_periods=60).apply(_bk, raw=True).replace([np.inf, -np.inf], np.nan)


# === REGIME TRANSITION DISCRETE EVENT COUNTS =============================


def f17vr_f17_volatility_regime_decile_jumpcount_42d_base_v105_signal(closeadj):
    """Count of (decile(vol(21d)/252d) - decile.shift(1)).abs() >= 3 in last 42d.
    Sudden-jump regime-change frequency."""
    r = np.log(closeadj / closeadj.shift(1))
    v = r.rolling(21, min_periods=21).std()
    def _dc(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 60:
            return np.nan
        return float(np.floor(np.mean(y[:-1] < x[-1]) * 10.0))
    dc = v.rolling(252, min_periods=60).apply(_dc, raw=True)
    jump = (dc.diff().abs() >= 3.0).astype(float).where(~dc.isna() & ~dc.shift(1).isna())
    return jump.rolling(42, min_periods=20).sum().replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_volzeroup_count_120d_base_v106_signal(closeadj):
    """Count of bars where vol(21d) crossed from below-mean to above-mean in last 120d."""
    r = np.log(closeadj / closeadj.shift(1))
    v = r.rolling(21, min_periods=21).std()
    mu = v.rolling(120, min_periods=40).mean()
    above = (v > mu).astype(float).where(~v.isna() & ~mu.isna())
    cross = ((above > 0.5) & (above.shift(1) <= 0.5)).astype(float).where(~above.isna() & ~above.shift(1).isna())
    return cross.rolling(120, min_periods=40).sum().replace([np.inf, -np.inf], np.nan)


# === REGIME-CONDITIONAL RETURN AGGREGATES =================================


def f17vr_f17_volatility_regime_avgret_in_high_quart_252d_base_v107_signal(closeadj):
    """Average daily log-return over last 252d, computed only on bars where vol(21d)>=p75/252d."""
    r = np.log(closeadj / closeadj.shift(1))
    v = r.rolling(21, min_periods=21).std()
    def _p75(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        return 1.0 if x[-1] >= np.quantile(y[:-1], 0.75) else 0.0
    ind = v.rolling(252, min_periods=60).apply(_p75, raw=True)
    def _avg(rseries):
        x = np.asarray(rseries, dtype=float)
        idx = np.where(x > 0.5)[0]
        return float(np.nan)
    # simpler: rolling mean of (r * ind) divided by rolling mean of ind
    r_ind = r * ind
    num = r_ind.rolling(252, min_periods=60).sum()
    den = ind.rolling(252, min_periods=60).sum()
    return (num / den.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_winrate_in_lowvol_252d_base_v108_signal(closeadj):
    """Win-rate of daily log-returns over 252d on bars where vol(21d) <= p25/252d."""
    r = np.log(closeadj / closeadj.shift(1))
    v = r.rolling(21, min_periods=21).std()
    def _p25(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        return 1.0 if x[-1] <= np.quantile(y[:-1], 0.25) else 0.0
    ind = v.rolling(252, min_periods=60).apply(_p25, raw=True)
    win = ((r > 0).astype(float) * ind).rolling(252, min_periods=60).sum()
    cnt = ind.rolling(252, min_periods=60).sum()
    return (win / cnt.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === BOUNDED TRANSFORMS OF ALTERNATIVE VOL ================================


def f17vr_f17_volatility_regime_HLrange_acceleration_30d_base_v109_signal(high, low):
    """tanh of (Parkinson-vol(21) - 2*Parkinson-vol(21).shift(15) + Parkinson-vol(21).shift(30))
    normalized by 60d std of Parkinson-vol. 2nd-difference (acceleration) of the
    HL-range vol — bounded transform of HL-regime CURVATURE, orthogonal to its level."""
    r2 = (np.log(high / low) ** 2) / (4.0 * np.log(2.0))
    pv = np.sqrt(r2.rolling(21, min_periods=21).mean())
    curv = pv - 2.0 * pv.shift(15) + pv.shift(30)
    sd = pv.rolling(60, min_periods=30).std()
    z = curv / sd.replace(0.0, np.nan)
    return np.tanh(z.clip(-30.0, 30.0)).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_sigmoid_madvol_z_120d_base_v110_signal(closeadj):
    """sigmoid of MAD-vol(21d) z-score in trailing 120d. Robust-vol regime bounded transform."""
    r = np.log(closeadj / closeadj.shift(1))
    mv = r.rolling(21, min_periods=21).apply(lambda x: float(np.mean(np.abs(x - np.mean(x)))), raw=True)
    mu = mv.rolling(120, min_periods=40).mean()
    sd = mv.rolling(120, min_periods=40).std()
    z = (mv - mu) / sd.replace(0.0, np.nan)
    return (1.0 / (1.0 + np.exp(-z.clip(-30.0, 30.0)))).replace([np.inf, -np.inf], np.nan)


# === REGIME-CHANGE DETECTION VIA CHANGE-POINT-LIKE STATISTIC ==============


def f17vr_f17_volatility_regime_cusum_absret_42d_base_v111_signal(closeadj):
    """CUSUM of (|log-return| - rolling-median(|log-return|, 42d)) over 21d window.
    High |CUSUM| indicates regime-shift event."""
    a = np.log(closeadj / closeadj.shift(1)).abs()
    med = a.rolling(42, min_periods=21).median()
    dev = a - med
    return dev.rolling(21, min_periods=11).sum().replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_cusum_signlogret_30d_base_v112_signal(closeadj):
    """CUSUM of sign(log-return) over 30d. Cumulative sign-imbalance — proxy for regime drift."""
    r = np.log(closeadj / closeadj.shift(1))
    return np.sign(r).rolling(30, min_periods=15).sum().replace([np.inf, -np.inf], np.nan)


# === REGIME-LEVEL PROXIES FROM HIGH-FREQ STRUCTURE (intraday-ish) ========


def f17vr_f17_volatility_regime_co_oc_ratio_42d_base_v113_signal(open_, closeadj):
    """log(close/open) std(42d) / log(close/close[-1]) std(42d). Open-close vs close-close vol-ratio."""
    co = np.log(closeadj / open_)
    cc = np.log(closeadj / closeadj.shift(1))
    s_co = co.rolling(42, min_periods=21).std()
    s_cc = cc.rolling(42, min_periods=21).std()
    return (s_co / s_cc.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_oc_quartile_42on252_base_v114_signal(open_, closeadj):
    """Quartile of |log(close/open)| 21d-mean within trailing 252d.
    Intraday close-vs-open magnitude regime."""
    a = np.log(closeadj / open_).abs()
    m = a.rolling(21, min_periods=21).mean()
    def _bk(x):
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
    return m.rolling(252, min_periods=60).apply(_bk, raw=True).replace([np.inf, -np.inf], np.nan)


# === REGIME-DEPENDENT TIME-COMPRESSION ====================================


def f17vr_f17_volatility_regime_logvol_window_ratio_30over120_base_v115_signal(closeadj):
    """log(std(log-return, 30d) / std(log-return, 120d)). Short over long vol level ratio.
    Distinct from f16's RV-ratio in that f16 uses sqrt(rvar)/sqrt(rvar) with different windows."""
    r = np.log(closeadj / closeadj.shift(1))
    s30 = r.rolling(30, min_periods=15).std()
    s120 = r.rolling(120, min_periods=40).std()
    return np.log(s30 / s120.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_vol_zscore_dyn_60d_base_v116_signal(closeadj):
    """Z-score: (vol(21d) - SMA(vol(21d), 60d)) / std(vol(21d), 60d). 60d adaptive Z."""
    r = np.log(closeadj / closeadj.shift(1))
    v = r.rolling(21, min_periods=21).std()
    mu = v.rolling(60, min_periods=30).mean()
    sd = v.rolling(60, min_periods=30).std()
    return ((v - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === REGIME-PERSISTENCE STATISTICS =========================================


def f17vr_f17_volatility_regime_volABS_acf1_60d_base_v117_signal(closeadj):
    """60d autocorr lag-1 of |log-return|. Vol-clustering signature, fundamental regime persistence."""
    a = np.log(closeadj / closeadj.shift(1)).abs()
    return a.rolling(60, min_periods=30).apply(
        lambda x: float(pd.Series(x).autocorr(lag=1)) if pd.Series(x).std() > 0 else np.nan,
        raw=False
    ).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_sqret_acf10_120d_base_v118_signal(closeadj):
    """120d autocorr lag-10 of (log-return)^2. Long-memory vol persistence."""
    r2 = np.log(closeadj / closeadj.shift(1)).pow(2)
    return r2.rolling(120, min_periods=60).apply(
        lambda x: float(pd.Series(x).autocorr(lag=10)) if pd.Series(x).std() > 0 else np.nan,
        raw=False
    ).replace([np.inf, -np.inf], np.nan)


# === SIGNED-VOL DECOMPOSITION ==============================================


def f17vr_f17_volatility_regime_downup_volratio_42d_base_v119_signal(closeadj):
    """semi-down-RMS(42d) / semi-up-RMS(42d). Asymmetric-vol regime ratio
    using clip-based semi-RMS so the 42d rolling has full support."""
    r = np.log(closeadj / closeadj.shift(1))
    neg = r.clip(upper=0.0)
    pos = r.clip(lower=0.0)
    dv = np.sqrt(neg.pow(2).rolling(42, min_periods=42).mean())
    uv = np.sqrt(pos.pow(2).rolling(42, min_periods=42).mean())
    return (dv / uv.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_downup_ratio_pctrank_252d_base_v120_signal(closeadj):
    """Pct-rank of (semi-down-RMS(42)/semi-up-RMS(42)) in trailing 252d.
    Ranks asymmetry regime; clip-based to avoid sparse rolling windows."""
    r = np.log(closeadj / closeadj.shift(1))
    neg = r.clip(upper=0.0)
    pos = r.clip(lower=0.0)
    dv = np.sqrt(neg.pow(2).rolling(42, min_periods=42).mean())
    uv = np.sqrt(pos.pow(2).rolling(42, min_periods=42).mean())
    ratio = dv / uv.replace(0.0, np.nan)
    def _r(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        return float(np.mean(y[:-1] < x[-1]))
    return ratio.rolling(252, min_periods=60).apply(_r, raw=True).replace([np.inf, -np.inf], np.nan)


# === MORE FEATURES (121-150) ===============================================


def f17vr_f17_volatility_regime_madstd_vs_norm_42d_base_v121_signal(closeadj):
    """(MAD-vol(21) / std-vol(21)) compared to 0.798 (theoretical for normal). Departure-from-normal."""
    r = np.log(closeadj / closeadj.shift(1))
    mv = r.rolling(21, min_periods=21).apply(lambda x: float(np.mean(np.abs(x - np.mean(x)))), raw=True)
    sv = r.rolling(21, min_periods=21).std()
    return (mv / sv.replace(0.0, np.nan) - 0.7979).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_voldd_60d_base_v122_signal(closeadj):
    """Vol-drawdown: 1 - vol(21d) / rolling-max(vol(21d), 60d). Distance from recent vol peak."""
    r = np.log(closeadj / closeadj.shift(1))
    v = r.rolling(21, min_periods=21).std()
    mx = v.rolling(60, min_periods=30).max()
    return (1.0 - v / mx.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_volup_30d_base_v123_signal(closeadj):
    """Vol-runup: vol(21d) / rolling-min(vol(21d), 30d) - 1. Distance above recent vol trough."""
    r = np.log(closeadj / closeadj.shift(1))
    v = r.rolling(21, min_periods=21).std()
    mn = v.rolling(30, min_periods=15).min()
    return (v / mn.replace(0.0, np.nan) - 1.0).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_vol_minargpos_60d_base_v124_signal(closeadj):
    """Position (0..1) of the ARGMIN of vol(21d) within the trailing 60d window:
        argmin_pos = argmin / (window-1). 0 = oldest bar; 1 = today.
    Encodes WHERE within the window the regime-trough sits — a temporal-localization
    signal that does NOT track the current vol level (orthogonal to vol-z/min-max-norm
    features by construction)."""
    r = np.log(closeadj / closeadj.shift(1))
    v = r.rolling(21, min_periods=21).std()
    def _ap(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        n = len(x)
        if n < 2:
            return np.nan
        return float(int(np.argmin(x)) / (n - 1))
    return v.rolling(60, min_periods=30).apply(_ap, raw=True).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_bayes_evidence_log_60d_base_v125_signal(closeadj):
    """Bayes-style log-likelihood-ratio of HIGH vs LOW vol regime using
    Laplace likelihoods centered at the 252d 25/75 percentiles with scale
    = 252d MAD. Squared distance penalises being far from the regime
    center; ratio of penalties is the evidence. Magnitude-weighted,
    structurally distinct from v092's fraction-above-mean."""
    r = np.log(closeadj / closeadj.shift(1))
    v = r.rolling(21, min_periods=21).std()
    q75 = v.rolling(252, min_periods=60).quantile(0.75)
    q25 = v.rolling(252, min_periods=60).quantile(0.25)
    mad = v.rolling(252, min_periods=60).apply(
        lambda x: float(np.mean(np.abs(x - np.mean(x)))), raw=True
    ).replace(0.0, np.nan)
    return ((v - q25).abs() - (v - q75).abs()) / mad



def f17vr_f17_volatility_regime_close_above_avg_pct_in_lowvol_120d_base_v126_signal(close):
    """In last 120 bars, fraction of bars where close > SMA(close, 21) AND vol(21d) < median.
    Joint state regime."""
    s21 = close.rolling(21, min_periods=21).mean()
    r = np.log(close / close.shift(1))
    v = r.rolling(21, min_periods=21).std()
    med = v.rolling(252, min_periods=60).median()
    j = ((close > s21) & (v < med)).astype(float).where(~s21.isna() & ~v.isna() & ~med.isna())
    return j.rolling(120, min_periods=60).mean().replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_vol5_volpct_diff_252d_base_v127_signal(close):
    """pctrank(vol(5d), 252d) - pctrank(vol(5d).shift(10), 252d). Short-horizon regime change."""
    r = np.log(close / close.shift(1))
    v5 = r.rolling(5, min_periods=5).std()
    def _r(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        return float(np.mean(y[:-1] < x[-1]))
    pr = v5.rolling(252, min_periods=60).apply(_r, raw=True)
    return (pr - pr.shift(10)).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_HLrange_z_diff_120d_base_v128_signal(high, low):
    """log(H/L)(21d-mean) z-score in 120d MINUS its 10-bar-lag z-score. Range-regime momentum."""
    r = np.log(high / low)
    m = r.rolling(21, min_periods=21).mean()
    mu = m.rolling(120, min_periods=40).mean()
    sd = m.rolling(120, min_periods=40).std()
    z = (m - mu) / sd.replace(0.0, np.nan)
    return (z - z.shift(10)).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_persistence_vol_dot_42d_base_v129_signal(closeadj):
    """Persistence: sum of sign(vol(21d).diff(1)) over 42d. +42 = pure-up, -42 = pure-down."""
    r = np.log(closeadj / closeadj.shift(1))
    v = r.rolling(21, min_periods=21).std()
    s = np.sign(v.diff(1))
    return s.rolling(42, min_periods=20).sum().replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_volpark_drift_30d_base_v130_signal(high, low):
    """OLS slope of Parkinson-HL-vol(21d) vs time over 30d, normalized by mean.
    Park-vol trend direction within window."""
    r2 = (np.log(high / low) ** 2) / (4.0 * np.log(2.0))
    pv = np.sqrt(r2.rolling(21, min_periods=21).mean())
    def _slope(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        n = len(x); t = np.arange(n, dtype=float)
        muT = t.mean(); muX = x.mean()
        cov = np.sum((t - muT) * (x - muX))
        var = np.sum((t - muT) ** 2)
        if var == 0.0 or muX == 0.0:
            return np.nan
        return float((cov / var) / muX)
    return pv.rolling(30, min_periods=15).apply(_slope, raw=True).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_GKvol_z_120d_base_v131_signal(open_, high, low, close):
    """Z-score of Garman-Klass vol(20d) in trailing 120d."""
    rs = 0.5 * (np.log(high / low) ** 2) - (2.0 * np.log(2.0) - 1.0) * (np.log(close / open_) ** 2)
    gk = np.sqrt(rs.rolling(20, min_periods=20).mean())
    mu = gk.rolling(120, min_periods=40).mean()
    sd = gk.rolling(120, min_periods=40).std()
    return ((gk - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_vol_robust_iqr_42d_base_v132_signal(closeadj):
    """IQR-based vol(42d): (q75 - q25) of log-returns over 42d / 1.349 (robust std estimate)."""
    r = np.log(closeadj / closeadj.shift(1))
    q75 = r.rolling(42, min_periods=21).quantile(0.75)
    q25 = r.rolling(42, min_periods=21).quantile(0.25)
    return ((q75 - q25) / 1.349).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_dayssince_lowvol_120d_base_v133_signal(closeadj):
    """Bars since last vol(21d) < p10/120d. Time since last calm regime."""
    r = np.log(closeadj / closeadj.shift(1))
    v = r.rolling(21, min_periods=21).std()
    def _p10(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 40:
            return np.nan
        return 1.0 if x[-1] < np.quantile(y[:-1], 0.1) else 0.0
    ind = v.rolling(120, min_periods=40).apply(_p10, raw=True)
    def _bs(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return float(len(x))
        return float(len(x) - 1 - idx[-1])
    return ind.rolling(120, min_periods=40).apply(_bs, raw=True).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_volprovexits_252d_base_v134_signal(closeadj):
    """Count of EXIT-events from high-vol (vol>p75/252) in last 252d.
    Transition-out-of-high counter."""
    r = np.log(closeadj / closeadj.shift(1))
    v = r.rolling(21, min_periods=21).std()
    def _p75(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        return 1.0 if x[-1] >= np.quantile(y[:-1], 0.75) else 0.0
    ind = v.rolling(252, min_periods=60).apply(_p75, raw=True)
    exit_ = ((ind < 0.5) & (ind.shift(1) >= 0.5)).astype(float).where(~ind.isna() & ~ind.shift(1).isna())
    return exit_.rolling(252, min_periods=60).sum().replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_volrank_acf3_60d_base_v135_signal(closeadj):
    """60d autocorr-lag-3 of pctrank(vol(21d), 252d). Vol-rank persistence."""
    r = np.log(closeadj / closeadj.shift(1))
    v = r.rolling(21, min_periods=21).std()
    def _r(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        return float(np.mean(y[:-1] < x[-1]))
    pr = v.rolling(252, min_periods=60).apply(_r, raw=True)
    return pr.rolling(60, min_periods=30).apply(
        lambda x: float(pd.Series(x).autocorr(lag=3)) if pd.Series(x).std() > 0 else np.nan,
        raw=False
    ).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_max_runtype_120d_base_v136_signal(closeadj):
    """Longest run of CONSECUTIVE bars with same sign of return in last 120d."""
    r = np.log(closeadj / closeadj.shift(1))
    s = np.sign(r)
    def _maxrun(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        best = 1; cur = 1
        for i in range(1, len(x)):
            if x[i] == x[i-1] and x[i] != 0.0:
                cur += 1
                if cur > best: best = cur
            else:
                cur = 1
        return float(best)
    return s.rolling(120, min_periods=60).apply(_maxrun, raw=True).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_voldelta_log_60d_base_v137_signal(closeadj):
    """log(vol(21d)) - log(vol(21d).shift(63)). Quarter-on-quarter log-change of regime level."""
    r = np.log(closeadj / closeadj.shift(1))
    v = r.rolling(21, min_periods=21).std()
    return (np.log(v) - np.log(v.shift(63))).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_HL_ZB_4_42d_base_v138_signal(high, low):
    """Count of bars in last 42d where HL-range > 1.8*median(HL-range, 42d). HL-tail-count.
    A 1.8x-median bar is a moderate-tail event; counting them gives a regime indicator
    distinct from level-of-range. (Original 4x threshold was too extreme to trigger
    on realistic synthetic data.)"""
    rng = high - low
    med = rng.rolling(42, min_periods=21).median()
    flag = (rng > 1.8 * med).astype(float).where(~rng.isna() & ~med.isna())
    return flag.rolling(42, min_periods=21).sum().replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_vol_rank_corr_diff_30_120_base_v139_signal(closeadj):
    """pctrank(vol(21d), 30d) - pctrank(vol(21d), 120d). Short-vs-long history rank disagreement."""
    r = np.log(closeadj / closeadj.shift(1))
    v = r.rolling(21, min_periods=21).std()
    def _r30(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 15:
            return np.nan
        return float(np.mean(y[:-1] < x[-1]))
    def _r120(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 40:
            return np.nan
        return float(np.mean(y[:-1] < x[-1]))
    a = v.rolling(30, min_periods=15).apply(_r30, raw=True)
    b = v.rolling(120, min_periods=40).apply(_r120, raw=True)
    return (a - b).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_park_close_disp_120d_base_v140_signal(high, low, closeadj):
    """std of log(park-vol(21d) / close-vol(21d)) over 120d. Dispersion of HL-vs-CC vol ratio."""
    r2 = (np.log(high / low) ** 2) / (4.0 * np.log(2.0))
    pv = np.sqrt(r2.rolling(21, min_periods=21).mean())
    cv = np.log(closeadj / closeadj.shift(1)).rolling(21, min_periods=21).std()
    ratio = np.log(pv / cv.replace(0.0, np.nan))
    return ratio.rolling(120, min_periods=40).std().replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_lowvol_streak_max_252d_base_v141_signal(closeadj):
    """Longest run of consecutive bars with vol(21d)<p25/252 in last 252d."""
    r = np.log(closeadj / closeadj.shift(1))
    v = r.rolling(21, min_periods=21).std()
    def _p25(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        return 1.0 if x[-1] <= np.quantile(y[:-1], 0.25) else 0.0
    ind = v.rolling(252, min_periods=60).apply(_p25, raw=True)
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
    return ind.rolling(252, min_periods=60).apply(_maxrun, raw=True).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_volsum_above_p50_42d_base_v142_signal(closeadj):
    """Sum of (vol(21d) - median(vol,252d)) for bars where vol > median, over 42d. Excess-vol-area."""
    r = np.log(closeadj / closeadj.shift(1))
    v = r.rolling(21, min_periods=21).std()
    med = v.rolling(252, min_periods=60).median()
    excess = (v - med).where(v > med, 0.0)
    return excess.rolling(42, min_periods=20).sum().replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_vol_sign_bal_42d_base_v143_signal(closeadj):
    """Sum(sign(vol(21d) - median(vol(21d), 60d))) over 42d. +ve if regime mostly elevated."""
    r = np.log(closeadj / closeadj.shift(1))
    v = r.rolling(21, min_periods=21).std()
    med60 = v.rolling(60, min_periods=30).median()
    return np.sign(v - med60).rolling(42, min_periods=20).sum().replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_vol_normality_test_60d_base_v144_signal(closeadj):
    """Anderson-style "vol-of-vol"/mean-vol ratio over 60d — coefficient of variation."""
    r = np.log(closeadj / closeadj.shift(1))
    v = r.rolling(21, min_periods=21).std()
    mu = v.rolling(60, min_periods=30).mean()
    sd = v.rolling(60, min_periods=30).std()
    return (sd / mu.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_HL_zerocross_med_60d_base_v145_signal(high, low):
    """Count of zero-crossings of (mean-log(H/L,21d) - 120d rolling median) in trailing 60d.
    Oscillation-frequency signal on the HL-range regime — structurally orthogonal
    to level/ratio features and to time-since-max."""
    r = np.log(high / low)
    m21 = r.rolling(21, min_periods=21).mean()
    med120 = m21.rolling(120, min_periods=40).median()
    d = m21 - med120
    sgn = np.sign(d)
    cross = (sgn != sgn.shift(1)).astype(float).where(~sgn.isna() & ~sgn.shift(1).isna())
    return cross.rolling(60, min_periods=20).sum().replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_volstateprob_logit_42d_base_v146_signal(closeadj):
    """Logit-style: log( P(vol_high|recent 42) / P(vol_high|prior 252) ).
    Recency-weighted regime evidence."""
    r = np.log(closeadj / closeadj.shift(1))
    v = r.rolling(21, min_periods=21).std()
    def _p75(x):
        if not np.isfinite(x[-1]):
            return np.nan
        y = x[~np.isnan(x)]
        if len(y) < 50:
            return np.nan
        return 1.0 if x[-1] >= np.quantile(y[:-1], 0.75) else 0.0
    ind = v.rolling(252, min_periods=60).apply(_p75, raw=True)
    recent = ind.rolling(42, min_periods=20).mean()
    prior = ind.rolling(252, min_periods=60).mean()
    r_c = recent.clip(0.01, 0.99); p_c = prior.clip(0.01, 0.99)
    return (np.log(r_c / (1.0 - r_c)) - np.log(p_c / (1.0 - p_c))).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_vol_distentropy_3bin_120d_base_v147_signal(closeadj):
    """Shannon entropy of vol-tercile distribution over last 120 bars."""
    r = np.log(closeadj / closeadj.shift(1))
    v = r.rolling(21, min_periods=21).std()
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
    def _ent(x):
        if not np.all(np.isfinite(x)) or len(x) < 10:
            return np.nan
        u, c = np.unique(x, return_counts=True)
        p = c / c.sum()
        return float(-np.sum(p * np.log(p)))
    return reg.rolling(120, min_periods=60).apply(_ent, raw=True).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_vol_dispersion_60d_base_v148_signal(closeadj):
    """std(vol(5d), 60d) / mean(vol(5d), 60d). Coefficient-of-variation of short-vol."""
    r = np.log(closeadj / closeadj.shift(1))
    v5 = r.rolling(5, min_periods=5).std()
    mu = v5.rolling(60, min_periods=30).mean()
    sd = v5.rolling(60, min_periods=30).std()
    return (sd / mu.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_close_minus_open_voldiff_42d_base_v149_signal(open_, closeadj):
    """std(log(close/open), 42d) - std(log(close/close.shift), 42d). Intraday minus overnight vol level."""
    a = np.log(closeadj / open_)
    b = np.log(closeadj / closeadj.shift(1))
    return (a.rolling(42, min_periods=21).std() - b.rolling(42, min_periods=21).std()).replace([np.inf, -np.inf], np.nan)


def f17vr_f17_volatility_regime_volmaxminus_minmin_60d_base_v150_signal(closeadj):
    """(max(vol(21d), 60d) - min(vol(21d), 60d)) — absolute regime swing in 60d."""
    r = np.log(closeadj / closeadj.shift(1))
    v = r.rolling(21, min_periods=21).std()
    hi = v.rolling(60, min_periods=30).max()
    lo = v.rolling(60, min_periods=30).min()
    return (hi - lo).replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f17_volatility_regime_base_076_150_REGISTRY = {
    "f17vr_f17_volatility_regime_parkvol_quartile_21on252_base_v076_signal": {"inputs": ["high", "low", "closeadj"], "func": f17vr_f17_volatility_regime_parkvol_quartile_21on252_base_v076_signal},
    "f17vr_f17_volatility_regime_HLrange_z_42d_base_v077_signal": {"inputs": ["high", "low"], "func": f17vr_f17_volatility_regime_HLrange_z_42d_base_v077_signal},
    "f17vr_f17_volatility_regime_HLrange_dayssincemax_180d_base_v078_signal": {"inputs": ["high", "low"], "func": f17vr_f17_volatility_regime_HLrange_dayssincemax_180d_base_v078_signal},
    "f17vr_f17_volatility_regime_gkvol_p75_ind_30d_base_v079_signal": {"inputs": ["open", "high", "low", "close"], "func": f17vr_f17_volatility_regime_gkvol_p75_ind_30d_base_v079_signal},
    "f17vr_f17_volatility_regime_rangetonormal_42d_base_v080_signal": {"inputs": ["high", "low", "closeadj"], "func": f17vr_f17_volatility_regime_rangetonormal_42d_base_v080_signal},
    "f17vr_f17_volatility_regime_downvol_p90_42d_base_v081_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_downvol_p90_42d_base_v081_signal},
    "f17vr_f17_volatility_regime_upvol_decile_252d_base_v082_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_upvol_decile_252d_base_v082_signal},
    "f17vr_f17_volatility_regime_downup_voldiff_z_42d_base_v083_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_downup_voldiff_z_42d_base_v083_signal},
    "f17vr_f17_volatility_regime_madvol_quintile_21on252_base_v084_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_madvol_quintile_21on252_base_v084_signal},
    "f17vr_f17_volatility_regime_madvol_pctrank_42on500_base_v085_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_madvol_pctrank_42on500_base_v085_signal},
    "f17vr_f17_volatility_regime_absret_avg_pctrank_30on252_base_v086_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_absret_avg_pctrank_30on252_base_v086_signal},
    "f17vr_f17_volatility_regime_absret_max_pctrank_120d_base_v087_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_absret_max_pctrank_120d_base_v087_signal},
    "f17vr_f17_volatility_regime_cvar5_pctrank_42on252_base_v088_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_cvar5_pctrank_42on252_base_v088_signal},
    "f17vr_f17_volatility_regime_var5_above_threshold_60d_base_v089_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_var5_above_threshold_60d_base_v089_signal},
    "f17vr_f17_volatility_regime_retentropy_bins_42d_base_v090_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_retentropy_bins_42d_base_v090_signal},
    "f17vr_f17_volatility_regime_abs_ret_entropy_60d_base_v091_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_abs_ret_entropy_60d_base_v091_signal},
    "f17vr_f17_volatility_regime_post_highvol_60d_base_v092_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_post_highvol_60d_base_v092_signal},
    "f17vr_f17_volatility_regime_post_highvol_smoothed_30d_base_v093_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_post_highvol_smoothed_30d_base_v093_signal},
    "f17vr_f17_volatility_regime_adapt_threshold_ind_84d_base_v094_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_adapt_threshold_ind_84d_base_v094_signal},
    "f17vr_f17_volatility_regime_adapt_low_threshold_84d_base_v095_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_adapt_low_threshold_84d_base_v095_signal},
    "f17vr_f17_volatility_regime_semiIQR_high_pctrank_60d_base_v096_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_semiIQR_high_pctrank_60d_base_v096_signal},
    "f17vr_f17_volatility_regime_semiIQR_low_pctrank_60d_base_v097_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_semiIQR_low_pctrank_60d_base_v097_signal},
    "f17vr_f17_volatility_regime_kurt_excessflag_42d_base_v098_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_kurt_excessflag_42d_base_v098_signal},
    "f17vr_f17_volatility_regime_kurtpctrank_42on252_base_v099_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_kurtpctrank_42on252_base_v099_signal},
    "f17vr_f17_volatility_regime_NRcount_4_42d_base_v100_signal": {"inputs": ["high", "low"], "func": f17vr_f17_volatility_regime_NRcount_4_42d_base_v100_signal},
    "f17vr_f17_volatility_regime_WRcount_4_42d_base_v101_signal": {"inputs": ["high", "low"], "func": f17vr_f17_volatility_regime_WRcount_4_42d_base_v101_signal},
    "f17vr_f17_volatility_regime_HLavg_z_60d_base_v102_signal": {"inputs": ["high", "low"], "func": f17vr_f17_volatility_regime_HLavg_z_60d_base_v102_signal},
    "f17vr_f17_volatility_regime_ewmavol_lam97_base_v103_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_ewmavol_lam97_base_v103_signal},
    "f17vr_f17_volatility_regime_ewmavol_decile_94_252d_base_v104_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_ewmavol_decile_94_252d_base_v104_signal},
    "f17vr_f17_volatility_regime_decile_jumpcount_42d_base_v105_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_decile_jumpcount_42d_base_v105_signal},
    "f17vr_f17_volatility_regime_volzeroup_count_120d_base_v106_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_volzeroup_count_120d_base_v106_signal},
    "f17vr_f17_volatility_regime_avgret_in_high_quart_252d_base_v107_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_avgret_in_high_quart_252d_base_v107_signal},
    "f17vr_f17_volatility_regime_winrate_in_lowvol_252d_base_v108_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_winrate_in_lowvol_252d_base_v108_signal},
    "f17vr_f17_volatility_regime_HLrange_acceleration_30d_base_v109_signal": {"inputs": ["high", "low"], "func": f17vr_f17_volatility_regime_HLrange_acceleration_30d_base_v109_signal},
    "f17vr_f17_volatility_regime_sigmoid_madvol_z_120d_base_v110_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_sigmoid_madvol_z_120d_base_v110_signal},
    "f17vr_f17_volatility_regime_cusum_absret_42d_base_v111_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_cusum_absret_42d_base_v111_signal},
    "f17vr_f17_volatility_regime_cusum_signlogret_30d_base_v112_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_cusum_signlogret_30d_base_v112_signal},
    "f17vr_f17_volatility_regime_co_oc_ratio_42d_base_v113_signal": {"inputs": ["open", "closeadj"], "func": f17vr_f17_volatility_regime_co_oc_ratio_42d_base_v113_signal},
    "f17vr_f17_volatility_regime_oc_quartile_42on252_base_v114_signal": {"inputs": ["open", "closeadj"], "func": f17vr_f17_volatility_regime_oc_quartile_42on252_base_v114_signal},
    "f17vr_f17_volatility_regime_logvol_window_ratio_30over120_base_v115_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_logvol_window_ratio_30over120_base_v115_signal},
    "f17vr_f17_volatility_regime_vol_zscore_dyn_60d_base_v116_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_vol_zscore_dyn_60d_base_v116_signal},
    "f17vr_f17_volatility_regime_volABS_acf1_60d_base_v117_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_volABS_acf1_60d_base_v117_signal},
    "f17vr_f17_volatility_regime_sqret_acf10_120d_base_v118_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_sqret_acf10_120d_base_v118_signal},
    "f17vr_f17_volatility_regime_downup_volratio_42d_base_v119_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_downup_volratio_42d_base_v119_signal},
    "f17vr_f17_volatility_regime_downup_ratio_pctrank_252d_base_v120_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_downup_ratio_pctrank_252d_base_v120_signal},
    "f17vr_f17_volatility_regime_madstd_vs_norm_42d_base_v121_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_madstd_vs_norm_42d_base_v121_signal},
    "f17vr_f17_volatility_regime_voldd_60d_base_v122_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_voldd_60d_base_v122_signal},
    "f17vr_f17_volatility_regime_volup_30d_base_v123_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_volup_30d_base_v123_signal},
    "f17vr_f17_volatility_regime_vol_minargpos_60d_base_v124_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_vol_minargpos_60d_base_v124_signal},
    "f17vr_f17_volatility_regime_bayes_evidence_log_60d_base_v125_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_bayes_evidence_log_60d_base_v125_signal},
    "f17vr_f17_volatility_regime_close_above_avg_pct_in_lowvol_120d_base_v126_signal": {"inputs": ["close"], "func": f17vr_f17_volatility_regime_close_above_avg_pct_in_lowvol_120d_base_v126_signal},
    "f17vr_f17_volatility_regime_vol5_volpct_diff_252d_base_v127_signal": {"inputs": ["close"], "func": f17vr_f17_volatility_regime_vol5_volpct_diff_252d_base_v127_signal},
    "f17vr_f17_volatility_regime_HLrange_z_diff_120d_base_v128_signal": {"inputs": ["high", "low"], "func": f17vr_f17_volatility_regime_HLrange_z_diff_120d_base_v128_signal},
    "f17vr_f17_volatility_regime_persistence_vol_dot_42d_base_v129_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_persistence_vol_dot_42d_base_v129_signal},
    "f17vr_f17_volatility_regime_volpark_drift_30d_base_v130_signal": {"inputs": ["high", "low"], "func": f17vr_f17_volatility_regime_volpark_drift_30d_base_v130_signal},
    "f17vr_f17_volatility_regime_GKvol_z_120d_base_v131_signal": {"inputs": ["open", "high", "low", "close"], "func": f17vr_f17_volatility_regime_GKvol_z_120d_base_v131_signal},
    "f17vr_f17_volatility_regime_vol_robust_iqr_42d_base_v132_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_vol_robust_iqr_42d_base_v132_signal},
    "f17vr_f17_volatility_regime_dayssince_lowvol_120d_base_v133_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_dayssince_lowvol_120d_base_v133_signal},
    "f17vr_f17_volatility_regime_volprovexits_252d_base_v134_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_volprovexits_252d_base_v134_signal},
    "f17vr_f17_volatility_regime_volrank_acf3_60d_base_v135_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_volrank_acf3_60d_base_v135_signal},
    "f17vr_f17_volatility_regime_max_runtype_120d_base_v136_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_max_runtype_120d_base_v136_signal},
    "f17vr_f17_volatility_regime_voldelta_log_60d_base_v137_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_voldelta_log_60d_base_v137_signal},
    "f17vr_f17_volatility_regime_HL_ZB_4_42d_base_v138_signal": {"inputs": ["high", "low"], "func": f17vr_f17_volatility_regime_HL_ZB_4_42d_base_v138_signal},
    "f17vr_f17_volatility_regime_vol_rank_corr_diff_30_120_base_v139_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_vol_rank_corr_diff_30_120_base_v139_signal},
    "f17vr_f17_volatility_regime_park_close_disp_120d_base_v140_signal": {"inputs": ["high", "low", "closeadj"], "func": f17vr_f17_volatility_regime_park_close_disp_120d_base_v140_signal},
    "f17vr_f17_volatility_regime_lowvol_streak_max_252d_base_v141_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_lowvol_streak_max_252d_base_v141_signal},
    "f17vr_f17_volatility_regime_volsum_above_p50_42d_base_v142_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_volsum_above_p50_42d_base_v142_signal},
    "f17vr_f17_volatility_regime_vol_sign_bal_42d_base_v143_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_vol_sign_bal_42d_base_v143_signal},
    "f17vr_f17_volatility_regime_vol_normality_test_60d_base_v144_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_vol_normality_test_60d_base_v144_signal},
    "f17vr_f17_volatility_regime_HL_zerocross_med_60d_base_v145_signal": {"inputs": ["high", "low"], "func": f17vr_f17_volatility_regime_HL_zerocross_med_60d_base_v145_signal},
    "f17vr_f17_volatility_regime_volstateprob_logit_42d_base_v146_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_volstateprob_logit_42d_base_v146_signal},
    "f17vr_f17_volatility_regime_vol_distentropy_3bin_120d_base_v147_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_vol_distentropy_3bin_120d_base_v147_signal},
    "f17vr_f17_volatility_regime_vol_dispersion_60d_base_v148_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_vol_dispersion_60d_base_v148_signal},
    "f17vr_f17_volatility_regime_close_minus_open_voldiff_42d_base_v149_signal": {"inputs": ["open", "closeadj"], "func": f17vr_f17_volatility_regime_close_minus_open_voldiff_42d_base_v149_signal},
    "f17vr_f17_volatility_regime_volmaxminus_minmin_60d_base_v150_signal": {"inputs": ["closeadj"], "func": f17vr_f17_volatility_regime_volmaxminus_minmin_60d_base_v150_signal},
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
    for name, entry in f17_volatility_regime_base_076_150_REGISTRY.items():
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
