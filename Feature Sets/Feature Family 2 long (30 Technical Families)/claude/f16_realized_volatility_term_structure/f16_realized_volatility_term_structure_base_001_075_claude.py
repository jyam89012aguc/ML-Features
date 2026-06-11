"""f16_realized_volatility_term_structure base features 001-075.

Domain: realized-volatility TERM STRUCTURE — how realized vol varies across
horizons (5d, 21d, 63d, 252d). Features: single-horizon RV, term-structure
ratios, curvature, slopes-of-vol, vol regime ranks, OHLC-range vs returns
vol, distributional skew/kurt, vol-of-vol, term-structure shape fits,
discrete states, composites, bounded transforms, vol-clustering autocorr,
Hurst on vol, quadratic variation, roughness.

Every feature must reference horizon term-structure: either a single-horizon
RV, a multi-horizon ratio/curvature, or a within-horizon vol regime stat.

Each function is a fully-expanded def block. Window > 21 uses closeadj.
NaN policy: never fillna(value); only replace([inf,-inf], nan) at return.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _logret(s: pd.Series) -> pd.Series:
    return np.log(s).diff()


def _rv(s: pd.Series, n: int) -> pd.Series:
    """Annualized realized vol = std(log_returns, N) * sqrt(252)."""
    r = np.log(s).diff()
    return r.rolling(n, min_periods=n).std(ddof=1) * np.sqrt(252.0)


def _rvar(s: pd.Series, n: int) -> pd.Series:
    """Realized variance = mean(r^2, N) (annualized)."""
    r = np.log(s).diff()
    return (r * r).rolling(n, min_periods=n).mean() * 252.0


def _mad_logret(s: pd.Series, n: int) -> pd.Series:
    r = np.log(s).diff()
    mu = r.rolling(n, min_periods=n).mean()
    return (r - mu).abs().rolling(n, min_periods=n).mean()


# ---------------------------------------------------------------------------
# Features 001-075
# ---------------------------------------------------------------------------


# --- Single-horizon RV (FEW raw vols, widely spread windows) ---------------


def f16vt_f16_realized_volatility_term_structure_rv_5d_base_v001_signal(close):
    """Realized vol (annualized) at 5d horizon — short end of term structure."""
    n = 5
    r = np.log(close).diff()
    return (r.rolling(n, min_periods=n).std(ddof=1) * np.sqrt(252.0)).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_rv_63d_base_v002_signal(closeadj):
    """Realized vol (annualized) at 63d — mid-long end."""
    n = 63
    r = np.log(closeadj).diff()
    return (r.rolling(n, min_periods=n).std(ddof=1) * np.sqrt(252.0)).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_rv_252d_base_v003_signal(closeadj):
    """Realized vol (annualized) at 252d — long end."""
    n = 252
    r = np.log(closeadj).diff()
    return (r.rolling(n, min_periods=n).std(ddof=1) * np.sqrt(252.0)).replace([np.inf, -np.inf], np.nan)


# --- Term-structure ratios -------------------------------------------------


def f16vt_f16_realized_volatility_term_structure_rvratio_5_21_base_v004_signal(close):
    """vol(5)/vol(21) — short/medium term-structure ratio."""
    r = np.log(close).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    return (v5 / v21.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_rvratio_21_63_base_v005_signal(closeadj):
    """vol(21)/vol(63) — medium/long term-structure ratio."""
    r = np.log(closeadj).diff()
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    return (v21 / v63.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_rvratio_63_252_base_v006_signal(closeadj):
    """vol(63)/vol(252) — long/very-long term-structure ratio."""
    r = np.log(closeadj).diff()
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    v252 = r.rolling(252, min_periods=252).std(ddof=1)
    return (v63 / v252.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_termpctrank_5_252_base_v007_signal(closeadj):
    """Percentile rank of (vol(5)/vol(252)) over trailing 120d — relative ratio regime."""
    r = np.log(closeadj).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    v252 = r.rolling(252, min_periods=252).std(ddof=1)
    ratio = v5 / v252.replace(0.0, np.nan)
    return ratio.rolling(120, min_periods=80).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_invertcount_5_21_base_v008_signal(close):
    """Count of bars in last 30d with vol(5) > vol(21) — inverted short-mid term-structure persistence."""
    r = np.log(close).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    inv = (v5 > v21).astype(float).where(~v5.isna() & ~v21.isna())
    return inv.rolling(30, min_periods=30).sum().replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_logslope_21_252_base_v009_signal(closeadj):
    """Sign of log(vol(21)/vol(252)) — discrete contango/backwardation indicator."""
    r = np.log(closeadj).diff()
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    v252 = r.rolling(252, min_periods=252).std(ddof=1)
    ls = np.log(v21 / v252.replace(0.0, np.nan))
    return np.sign(ls).where(~ls.isna()).replace([np.inf, -np.inf], np.nan)


# --- Curvature across horizons --------------------------------------------


def f16vt_f16_realized_volatility_term_structure_curv_5_21_63_base_v010_signal(closeadj):
    """vol(5) - 2*vol(21) + vol(63) — vol curvature across 3 horizons."""
    r = np.log(closeadj).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    return (v5 - 2.0 * v21 + v63).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_curv_21_63_252_base_v011_signal(closeadj):
    """vol(21) - 2*vol(63) + vol(252) — long-end vol curvature."""
    r = np.log(closeadj).diff()
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    v252 = r.rolling(252, min_periods=252).std(ddof=1)
    return (v21 - 2.0 * v63 + v252).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_convexity_base_v012_signal(closeadj):
    """Sign of term-structure convexity ((vol5+vol63)/2 - vol21). Discrete -1/0/+1."""
    r = np.log(closeadj).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    cx = 0.5 * (v5 + v63) - v21
    return np.sign(cx).where(~cx.isna()).replace([np.inf, -np.inf], np.nan)


# --- Vol slopes (intra-vol time series diffs) -----------------------------


def f16vt_f16_realized_volatility_term_structure_vol21slope_5d_base_v013_signal(closeadj):
    """vol(21).diff(5) — slope of mid-horizon vol over 5 bars."""
    r = np.log(closeadj).diff()
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    return v21.diff(5).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_vol63slope_21d_base_v014_signal(closeadj):
    """vol(63).diff(21) — slope of long-horizon vol over 21 bars."""
    r = np.log(closeadj).diff()
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    return v63.diff(21).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_vol21accel_base_v015_signal(closeadj):
    """vol(21) - 2*vol(21).shift(5) + vol(21).shift(10) — acceleration of mid-vol."""
    r = np.log(closeadj).diff()
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    return (v21 - 2.0 * v21.shift(5) + v21.shift(10)).replace([np.inf, -np.inf], np.nan)


# --- Vol regime: rank / quantile / z-score ---------------------------------


def f16vt_f16_realized_volatility_term_structure_volpct_21on252_base_v016_signal(closeadj):
    """Percentile rank of current vol(21) within trailing 252d distribution."""
    r = np.log(closeadj).diff()
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    return v21.rolling(252, min_periods=252).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_volz_21on120_base_v017_signal(closeadj):
    """Z-score of current vol(21) vs trailing 120d distribution of vol(21)."""
    r = np.log(closeadj).diff()
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    mu = v21.rolling(120, min_periods=120).mean()
    sd = v21.rolling(120, min_periods=120).std(ddof=1)
    return ((v21 - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_volquint_5d_base_v018_signal(closeadj):
    """Vol(5) quintile (1-5) relative to trailing 252d distribution — short-end regime."""
    r = np.log(closeadj).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    p = v5.rolling(252, min_periods=252).rank(pct=True)
    q = (p * 5.0).apply(np.ceil).clip(lower=1.0, upper=5.0)
    return q.replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_dayssince_volp90_base_v019_signal(closeadj):
    """Days since vol(21) was > 90th-percentile of trailing 252d. Capped at 100."""
    r = np.log(closeadj).diff()
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    p90 = v21.rolling(252, min_periods=252).quantile(0.9)
    hit = (v21 > p90).astype(float).where(~v21.isna() & ~p90.isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return 100.0
        return float(len(x) - 1 - idx[-1])
    return hit.rolling(100, min_periods=100).apply(_ds, raw=True).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_streakhighvol_base_v020_signal(closeadj):
    """Current run-length of bars with vol(21) > 252d median (trailing)."""
    r = np.log(closeadj).diff()
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    med = v21.rolling(252, min_periods=252).median()
    h = (v21 > med).astype(float).where(~v21.isna() & ~med.isna())
    grp = (h != h.shift(1)).cumsum()
    streak = h.groupby(grp).cumsum() * h
    return streak.replace([np.inf, -np.inf], np.nan)


# --- Hi-Lo range vol vs return vol (cross-source) --------------------------


def f16vt_f16_realized_volatility_term_structure_hlrvratio_21d_base_v021_signal(high, low, close):
    """(high-low)/close range vol(21) divided by return-based vol(21). Cross-source ratio."""
    n = 21
    rng = ((high - low) / close.replace(0.0, np.nan))
    rv_rng = rng.rolling(n, min_periods=n).std(ddof=1)
    r = np.log(close).diff()
    rv_ret = r.rolling(n, min_periods=n).std(ddof=1)
    return (rv_rng / rv_ret.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_hlrvratio_63d_base_v022_signal(high, low, closeadj):
    """Cross-source HL-vol / return-vol ratio at 63d horizon."""
    n = 63
    rng = ((high - low) / closeadj.replace(0.0, np.nan))
    rv_rng = rng.rolling(n, min_periods=n).std(ddof=1)
    r = np.log(closeadj).diff()
    rv_ret = r.rolling(n, min_periods=n).std(ddof=1)
    return (rv_rng / rv_ret.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- Distributional skew / kurt of returns at horizon ---------------------


def f16vt_f16_realized_volatility_term_structure_retskew_21d_base_v023_signal(close):
    """Skew of log-returns over 21d — distributional asymmetry within horizon."""
    r = np.log(close).diff()
    return r.rolling(21, min_periods=21).skew().replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_retskew_63d_base_v024_signal(closeadj):
    """Skew of log-returns at 63d horizon."""
    r = np.log(closeadj).diff()
    return r.rolling(63, min_periods=63).skew().replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_retkurt_21d_base_v025_signal(close):
    """Kurtosis of log-returns at 21d — fat-tail measure (term-structure of moments)."""
    r = np.log(close).diff()
    return r.rolling(21, min_periods=21).kurt().replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_retkurt_63d_base_v026_signal(closeadj):
    """Kurtosis of log-returns at 63d horizon."""
    r = np.log(closeadj).diff()
    return r.rolling(63, min_periods=63).kurt().replace([np.inf, -np.inf], np.nan)


# --- Downside vs upside vol asymmetry --------------------------------------


def f16vt_f16_realized_volatility_term_structure_downvol_21d_base_v027_signal(close):
    """Downside semi-vol(21): std of negative log-returns only."""
    r = np.log(close).diff()
    neg = r.where(r < 0)
    return (neg.rolling(21, min_periods=10).std(ddof=1) * np.sqrt(252.0)).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_upvol_63d_base_v028_signal(closeadj):
    """Upside semi-vol(63): std of positive log-returns only."""
    r = np.log(closeadj).diff()
    pos = r.where(r > 0)
    return (pos.rolling(63, min_periods=30).std(ddof=1) * np.sqrt(252.0)).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_varasym_42d_base_v029_signal(closeadj):
    """Variance asymmetry: var(positive r) - var(negative r) at 42d."""
    n = 42
    r = np.log(closeadj).diff()
    pos = r.where(r > 0)
    neg = r.where(r < 0)
    vp = pos.rolling(n, min_periods=15).var(ddof=1)
    vn = neg.rolling(n, min_periods=15).var(ddof=1)
    return (vp - vn).replace([np.inf, -np.inf], np.nan)


# --- Vol clustering / autocorrelation -------------------------------------


def f16vt_f16_realized_volatility_term_structure_absretacf1_30d_base_v030_signal(closeadj):
    """Lag-1 autocorr of |log-returns| over 30d — vol-clustering signature."""
    n = 30
    r = np.log(closeadj).diff().abs()
    def _ac1(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)) or x.size < 5:
            return np.nan
        a = x[:-1]; b = x[1:]
        sa = a.std(ddof=0); sb = b.std(ddof=0)
        if sa <= 0 or sb <= 0:
            return np.nan
        return float(((a - a.mean()) * (b - b.mean())).mean() / (sa * sb))
    return r.rolling(n, min_periods=n).apply(_ac1, raw=True).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_sqretacf1_60d_base_v031_signal(closeadj):
    """Lag-1 autocorr of squared log-returns over 60d — ARCH-effect signature."""
    n = 60
    r = (np.log(closeadj).diff()) ** 2
    def _ac1(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)) or x.size < 5:
            return np.nan
        a = x[:-1]; b = x[1:]
        sa = a.std(ddof=0); sb = b.std(ddof=0)
        if sa <= 0 or sb <= 0:
            return np.nan
        return float(((a - a.mean()) * (b - b.mean())).mean() / (sa * sb))
    return r.rolling(n, min_periods=n).apply(_ac1, raw=True).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_volpersist_30d_base_v032_signal(closeadj):
    """Persistence of vol regime: fraction of last 30 bars where vol(21) stays above 252d median."""
    r = np.log(closeadj).diff()
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    med = v21.rolling(252, min_periods=252).median()
    above = (v21 > med).astype(float).where(~v21.isna() & ~med.isna())
    return above.rolling(30, min_periods=30).mean().replace([np.inf, -np.inf], np.nan)


# --- Term-structure shape fit (linear log-log) ----------------------------


def f16vt_f16_realized_volatility_term_structure_curveR2_4pt_base_v033_signal(closeadj):
    """R^2 of linear fit of (log_horizon, log_vol) using horizons {5,21,63,252}.
    Measures how well term-structure follows power-law shape today."""
    r = np.log(closeadj).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    v252 = r.rolling(252, min_periods=252).std(ddof=1)
    x = np.log(np.array([5.0, 21.0, 63.0, 252.0]))
    xm = x - x.mean()
    sxx = (xm * xm).sum()
    def _r2(row):
        y = np.array(row, dtype=float)
        if np.any(~np.isfinite(y)) or np.any(y <= 0):
            return np.nan
        ly = np.log(y); lym = ly - ly.mean()
        syy = (lym * lym).sum()
        if syy <= 0:
            return np.nan
        b = (xm * lym).sum() / sxx
        rss = ((lym - b * xm) ** 2).sum()
        return float(1.0 - rss / syy)
    df = pd.concat([v5, v21, v63, v252], axis=1)
    return df.apply(_r2, axis=1).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_curveslopesign_base_v034_signal(closeadj):
    """Sign of log-log fit slope over horizons {5,21,63,252}. Discrete normal(-1)/inverted(+1)."""
    r = np.log(closeadj).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    v252 = r.rolling(252, min_periods=252).std(ddof=1)
    x = np.log(np.array([5.0, 21.0, 63.0, 252.0]))
    xm = x - x.mean()
    sxx = (xm * xm).sum()
    def _slope(row):
        y = np.array(row, dtype=float)
        if np.any(~np.isfinite(y)) or np.any(y <= 0):
            return np.nan
        ly = np.log(y); lym = ly - ly.mean()
        slope = (xm * lym).sum() / sxx
        if slope > 0: return 1.0
        if slope < 0: return -1.0
        return 0.0
    df = pd.concat([v5, v21, v63, v252], axis=1)
    return df.apply(_slope, axis=1).replace([np.inf, -np.inf], np.nan)


# --- Inverted vs normal term structure (discrete) -------------------------


def f16vt_f16_realized_volatility_term_structure_invertedsign_base_v035_signal(closeadj):
    """Sign indicator: +1 if vol(5) > vol(63) (inverted), -1 if vol(5) < vol(63), 0 else."""
    r = np.log(closeadj).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    return np.sign(v5 - v63).where(~v5.isna() & ~v63.isna()).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_invertedfrac_60d_base_v036_signal(closeadj):
    """Fraction of last 60 bars with inverted term-structure (vol(5) > vol(63))."""
    r = np.log(closeadj).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    inv = (v5 > v63).astype(float).where(~v5.isna() & ~v63.isna())
    return inv.rolling(60, min_periods=60).mean().replace([np.inf, -np.inf], np.nan)


# --- Vol cone: where today's vol sits within trailing min/max -------------


def f16vt_f16_realized_volatility_term_structure_volconeshort_5on120_base_v037_signal(close):
    """(vol(5) - min) / (max - min) over trailing 120d — short-vol cone position."""
    r = np.log(close).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    lo = v5.rolling(120, min_periods=120).min()
    hi = v5.rolling(120, min_periods=120).max()
    return ((v5 - lo) / (hi - lo).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_volconedelta_base_v038_signal(closeadj):
    """vol-cone-position(vol5,120) minus vol-cone-position(vol63,252) — short-vs-long cone gap."""
    r = np.log(closeadj).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    lo5 = v5.rolling(120, min_periods=120).min()
    hi5 = v5.rolling(120, min_periods=120).max()
    lo63 = v63.rolling(252, min_periods=252).min()
    hi63 = v63.rolling(252, min_periods=252).max()
    c5 = (v5 - lo5) / (hi5 - lo5).replace(0.0, np.nan)
    c63 = (v63 - lo63) / (hi63 - lo63).replace(0.0, np.nan)
    return (c5 - c63).replace([np.inf, -np.inf], np.nan)


# --- Discrete vol states ---------------------------------------------------


def f16vt_f16_realized_volatility_term_structure_voldirsign_21d_base_v039_signal(closeadj):
    """Sign of vol(21).diff(5) — vol up/down direction."""
    r = np.log(closeadj).diff()
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    return np.sign(v21.diff(5)).where(~v21.isna()).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_volcontract_30d_base_v040_signal(closeadj):
    """Binary: vol(21) < trailing 30d-min of vol(21). Vol contraction signal."""
    r = np.log(closeadj).diff()
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    mn = v21.rolling(30, min_periods=30).min()
    return (v21 <= mn).astype(float).where(~v21.isna() & ~mn.isna()).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_volexpand_30d_base_v041_signal(closeadj):
    """Binary: vol(21) > trailing 30d-max of vol(21).shift(1). Vol expansion (NBNR)."""
    r = np.log(closeadj).diff()
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    mx = v21.shift(1).rolling(30, min_periods=30).max()
    return (v21 > mx).astype(float).where(~v21.isna() & ~mx.isna()).replace([np.inf, -np.inf], np.nan)


# --- Composites across horizons --------------------------------------------


def f16vt_f16_realized_volatility_term_structure_avgvol_3h_base_v042_signal(closeadj):
    """Average of vol(5), vol(21), vol(63) — composite mid-term-structure level."""
    r = np.log(closeadj).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    return ((v5 + v21 + v63) / 3.0).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_volhdisp_3h_base_v043_signal(closeadj):
    """Std-dev across horizons {vol(5), vol(21), vol(63)} — dispersion of term-structure."""
    r = np.log(closeadj).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    df = pd.concat([v5, v21, v63], axis=1)
    return df.std(axis=1, ddof=1).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_medianvol_4h_base_v044_signal(closeadj):
    """Median across horizons {5,21,63,252} of annualized vol."""
    r = np.log(closeadj).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    v252 = r.rolling(252, min_periods=252).std(ddof=1)
    df = pd.concat([v5, v21, v63, v252], axis=1)
    return df.median(axis=1).replace([np.inf, -np.inf], np.nan)


# --- Bounded transforms ----------------------------------------------------


def f16vt_f16_realized_volatility_term_structure_arctanlogvol_21d_base_v045_signal(closeadj):
    """arctan( log( vol(21) ) ) — bounded transform of mid-vol level."""
    r = np.log(closeadj).diff()
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    lv = np.log(v21.replace(0.0, np.nan))
    return np.arctan(lv).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_tanhvolzdelta_base_v046_signal(closeadj):
    """tanh of (z-score(vol(5),120d) minus z-score(vol(63),120d)) — bounded term-z gap."""
    r = np.log(closeadj).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    z5 = (v5 - v5.rolling(120, min_periods=80).mean()) / v5.rolling(120, min_periods=80).std(ddof=1).replace(0.0, np.nan)
    z63 = (v63 - v63.rolling(120, min_periods=80).mean()) / v63.rolling(120, min_periods=80).std(ddof=1).replace(0.0, np.nan)
    return np.tanh(z5 - z63).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_sigmoidvolpct_base_v047_signal(closeadj):
    """Sigmoid centered on 0.5 of vol(63) trailing 252d percentile — smooth long-vol regime."""
    r = np.log(closeadj).diff()
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    p = v63.rolling(252, min_periods=252).rank(pct=True)
    return (1.0 / (1.0 + np.exp(-6.0 * (p - 0.5)))).replace([np.inf, -np.inf], np.nan)


# --- MAD / realized variance / RMS variants -------------------------------


def f16vt_f16_realized_volatility_term_structure_madstd_ratio_21d_base_v048_signal(close):
    """MAD(21) / std(21) of log-returns — Gaussian-deviation diagnostic at 21d horizon."""
    n = 21
    r = np.log(close).diff()
    mu = r.rolling(n, min_periods=n).mean()
    mad = (r - mu).abs().rolling(n, min_periods=n).mean()
    sd = r.rolling(n, min_periods=n).std(ddof=1)
    return (mad / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_rms_42d_base_v049_signal(closeadj):
    """Root-mean-square of log-returns at 42d (vol proxy without mean centering)."""
    n = 42
    r = np.log(closeadj).diff()
    return np.sqrt((r * r).rolling(n, min_periods=n).mean()).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_rvarratio_5_63_base_v050_signal(closeadj):
    """Realized variance ratio var(5)/var(63) — squared term-structure ratio."""
    r = np.log(closeadj).diff()
    rv5 = (r * r).rolling(5, min_periods=5).mean()
    rv63 = (r * r).rolling(63, min_periods=63).mean()
    return (rv5 / rv63.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- Hurst / roughness on returns (term-structure scaling) ----------------




def f16vt_f16_realized_volatility_term_structure_qvariation_30d_base_v052_signal(closeadj):
    """Quadratic variation: sum of r^2 over 30 bars — direct discrete RV."""
    n = 30
    r = np.log(closeadj).diff()
    return (r * r).rolling(n, min_periods=n).sum().replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_roughness_30d_base_v053_signal(closeadj):
    """Roughness: sum of |r.diff()| over 30 bars / sum of |r| — vol-path roughness."""
    n = 30
    r = np.log(closeadj).diff()
    num = r.diff().abs().rolling(n, min_periods=n).sum()
    den = r.abs().rolling(n, min_periods=n).sum()
    return (num / den.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- Term-structure slope using diff of vols at two horizons -------------


def f16vt_f16_realized_volatility_term_structure_voldiffsign_21m63_base_v054_signal(closeadj):
    """Sign of (vol(21) - vol(63)) — backwardation/contango bit at mid-long horizons."""
    r = np.log(closeadj).diff()
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    d = v21 - v63
    return np.sign(d).where(~d.isna()).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_voldiffz_5m63_base_v055_signal(closeadj):
    """Z-score of (vol(5) - vol(63)) over trailing 120d — normalized short-mid spread."""
    r = np.log(closeadj).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    d = v5 - v63
    mu = d.rolling(120, min_periods=80).mean()
    sd = d.rolling(120, min_periods=80).std(ddof=1)
    return ((d - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- Vol-of-vol -----------------------------------------------------------


def f16vt_f16_realized_volatility_term_structure_volofvol_21d_base_v056_signal(closeadj):
    """Std-dev of vol(21) over trailing 63 bars — vol-of-vol."""
    r = np.log(closeadj).diff()
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    return v21.rolling(63, min_periods=63).std(ddof=1).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_volofvol_long_base_v057_signal(closeadj):
    """Std-dev of vol(63) over trailing 126 bars / mean(vol63,126). Long-horizon vol-of-vol CoV."""
    r = np.log(closeadj).diff()
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    sd = v63.rolling(126, min_periods=126).std(ddof=1)
    mu = v63.rolling(126, min_periods=126).mean()
    return (sd / mu.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- Term-structure linear fit residual ----------------------------------


def f16vt_f16_realized_volatility_term_structure_curvres21_base_v058_signal(closeadj):
    """Residual at horizon 21 from linear log-log fit of {5,63,252} term structure.
    Detects whether 21d sits above/below straight line through other horizons."""
    r = np.log(closeadj).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    v252 = r.rolling(252, min_periods=252).std(ddof=1)
    # log-log fit using 5,63,252 to predict 21
    x_pts = np.log(np.array([5.0, 63.0, 252.0]))
    xm = x_pts - x_pts.mean()
    sxx = (xm * xm).sum()
    x21 = np.log(21.0)
    def _res(row):
        a, b, c, t = row
        ys = np.array([a, b, c], dtype=float)
        if np.any(~np.isfinite(ys)) or np.any(ys <= 0) or not np.isfinite(t) or t <= 0:
            return np.nan
        ly = np.log(ys); lym = ly - ly.mean()
        slope = (xm * lym).sum() / sxx
        intercept = ly.mean() - slope * x_pts.mean()
        pred = intercept + slope * x21
        return float(np.log(t) - pred)
    df = pd.concat([v5, v63, v252, v21], axis=1)
    return df.apply(_res, axis=1).replace([np.inf, -np.inf], np.nan)


# --- More slopes-of-vol with mixed normalization --------------------------


def f16vt_f16_realized_volatility_term_structure_volpctslope_21d_base_v059_signal(closeadj):
    """Slope of vol(21) percentile rank over 10 bars — regime-shift speed."""
    r = np.log(closeadj).diff()
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    p = v21.rolling(252, min_periods=252).rank(pct=True)
    return p.diff(10).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_logvolslope_63d_base_v060_signal(closeadj):
    """Sign of log(vol(63)).diff(21) — discrete long-vol direction over 21d."""
    r = np.log(closeadj).diff()
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    d = np.log(v63.replace(0.0, np.nan)).diff(21)
    return np.sign(d).where(~d.isna()).replace([np.inf, -np.inf], np.nan)


# --- Bi-power variation / jump-robust vol --------------------------------


def f16vt_f16_realized_volatility_term_structure_bipower_ratio_42d_base_v061_signal(closeadj):
    """Bi-power variation / quadratic variation at 42d (Pi/2 factor cancels). Tail-robustness ratio."""
    n = 42
    r = np.log(closeadj).diff()
    ra = r.abs()
    bv = (ra * ra.shift(1)).rolling(n, min_periods=n).sum() * (np.pi / 2.0)
    qv = (r * r).rolling(n, min_periods=n).sum()
    return (bv / qv.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_jumpcomp_42d_base_v062_signal(closeadj):
    """Jump component: max(0, RV(42) - BipowerVar(42)) / RV(42) — fraction from jumps."""
    n = 42
    r = np.log(closeadj).diff()
    rv = (r * r).rolling(n, min_periods=n).sum()
    bv = (r.abs() * r.abs().shift(1)).rolling(n, min_periods=n).sum() * (np.pi / 2.0)
    jump = (rv - bv).clip(lower=0.0)
    return (jump / rv.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- Term-structure dispersion / skew across horizons --------------------


def f16vt_f16_realized_volatility_term_structure_curveskew_4h_base_v063_signal(closeadj):
    """Skewness of the 4 horizon vols {5,21,63,252} treated as a sample at each bar."""
    r = np.log(closeadj).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    v252 = r.rolling(252, min_periods=252).std(ddof=1)
    df = pd.concat([v5, v21, v63, v252], axis=1)
    return df.skew(axis=1).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_curvekurt_4h_base_v064_signal(closeadj):
    """Kurtosis across 4 horizon vols — shape of vol term curve."""
    r = np.log(closeadj).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    v252 = r.rolling(252, min_periods=252).std(ddof=1)
    df = pd.concat([v5, v21, v63, v252], axis=1)
    return df.kurt(axis=1).replace([np.inf, -np.inf], np.nan)


# --- Days-since vol extremes (event timing) ------------------------------


def f16vt_f16_realized_volatility_term_structure_daystrough_60d_base_v065_signal(closeadj):
    """Days since vol(21) hit its 60d trailing minimum. Capped at 60."""
    r = np.log(closeadj).diff()
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    mn = v21.rolling(60, min_periods=60).min()
    hit = (v21 <= mn * 1.0001).astype(float).where(~v21.isna() & ~mn.isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return 60.0
        return float(len(x) - 1 - idx[-1])
    return hit.rolling(60, min_periods=60).apply(_ds, raw=True).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_dayspeak_120d_base_v066_signal(closeadj):
    """Days since vol(21) hit its 120d trailing maximum."""
    r = np.log(closeadj).diff()
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    mx = v21.rolling(120, min_periods=120).max()
    hit = (v21 >= mx * 0.9999).astype(float).where(~v21.isna() & ~mx.isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return 120.0
        return float(len(x) - 1 - idx[-1])
    return hit.rolling(120, min_periods=120).apply(_ds, raw=True).replace([np.inf, -np.inf], np.nan)


# --- Sign-agreement of vol direction across horizons --------------------


def f16vt_f16_realized_volatility_term_structure_volsigncnt_3h_base_v067_signal(closeadj):
    """Count among {sign(vol5.diff5), sign(vol21.diff5), sign(vol63.diff5)} that are positive (0-3)."""
    r = np.log(closeadj).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    s5 = (v5.diff(5) > 0).astype(float).where(~v5.isna())
    s21 = (v21.diff(5) > 0).astype(float).where(~v21.isna())
    s63 = (v63.diff(5) > 0).astype(float).where(~v63.isna())
    return (s5 + s21 + s63).replace([np.inf, -np.inf], np.nan)


# --- Range-based vol term structure (Parkinson-style at horizons) -------


def f16vt_f16_realized_volatility_term_structure_logHLstd_5d_base_v068_signal(high, low):
    """Std of log(high/low) at 5d — short-horizon range-based vol."""
    n = 5
    s = np.log(high / low.replace(0.0, np.nan))
    return s.rolling(n, min_periods=n).std(ddof=1).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_logHLstd_63d_base_v069_signal(high, low):
    """Std of log(high/low) at 63d — long-horizon range-based vol."""
    n = 63
    s = np.log(high / low.replace(0.0, np.nan))
    return s.rolling(n, min_periods=n).std(ddof=1).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_HLcurvature_base_v070_signal(high, low):
    """Curvature in log(H/L) stds: HLstd5 - 2*HLstd21 + HLstd63. Range-vol curvature."""
    s = np.log(high / low.replace(0.0, np.nan))
    sv5 = s.rolling(5, min_periods=5).std(ddof=1)
    sv21 = s.rolling(21, min_periods=21).std(ddof=1)
    sv63 = s.rolling(63, min_periods=63).std(ddof=1)
    return (sv5 - 2.0 * sv21 + sv63).replace([np.inf, -np.inf], np.nan)


# --- Compositional: short vol vs long vol-of-vol -----------------------


def f16vt_f16_realized_volatility_term_structure_vol5_volofvol_base_v071_signal(closeadj):
    """vol(5) divided by vol-of-vol(21,63). Tail-stress signature."""
    r = np.log(closeadj).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    vov = v21.rolling(63, min_periods=63).std(ddof=1)
    return (v5 / vov.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- Mean absolute deviation across horizons -------------------------


def f16vt_f16_realized_volatility_term_structure_madratio_5_63_base_v072_signal(closeadj):
    """MAD(5) / MAD(63) of log-returns — robust term-structure ratio."""
    r = np.log(closeadj).diff()
    mu5 = r.rolling(5, min_periods=5).mean()
    mu63 = r.rolling(63, min_periods=63).mean()
    mad5 = (r - mu5).abs().rolling(5, min_periods=5).mean()
    mad63 = (r - mu63).abs().rolling(63, min_periods=63).mean()
    return (mad5 / mad63.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- Term-structure level normalized (current vs LTavg) ---------------


def f16vt_f16_realized_volatility_term_structure_volzdiff_5_63_base_v073_signal(closeadj):
    """Difference of vol(5) percentile vs vol(63) percentile — term-structure regime gap."""
    r = np.log(closeadj).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    p5 = v5.rolling(252, min_periods=252).rank(pct=True)
    p63 = v63.rolling(252, min_periods=252).rank(pct=True)
    return (p5 - p63).replace([np.inf, -np.inf], np.nan)


# --- Vol clustering at horizon: streak of high-vol days -----------------


def f16vt_f16_realized_volatility_term_structure_highvolstreak_42d_base_v074_signal(closeadj):
    """Trailing 42d count of bars with |r| > 252d-90th percentile of |r|."""
    n = 42
    r = np.log(closeadj).diff().abs()
    q90 = r.rolling(252, min_periods=252).quantile(0.9)
    hit = (r > q90).astype(float).where(~r.isna() & ~q90.isna())
    return hit.rolling(n, min_periods=n).sum().replace([np.inf, -np.inf], np.nan)


# --- Term-structure sign (normal vs inverted) over horizons -----------


def f16vt_f16_realized_volatility_term_structure_normterm_60d_base_v075_signal(closeadj):
    """Fraction of last 60 bars with normal term structure: vol(5) < vol(21) AND vol(21) < vol(63)."""
    r = np.log(closeadj).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    norm = ((v5 < v21) & (v21 < v63)).astype(float).where(~v5.isna() & ~v21.isna() & ~v63.isna())
    return norm.rolling(60, min_periods=60).mean().replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f16_realized_volatility_term_structure_base_001_075_REGISTRY = {
    "f16vt_f16_realized_volatility_term_structure_rv_5d_base_v001_signal": {"inputs": ["close"], "func": f16vt_f16_realized_volatility_term_structure_rv_5d_base_v001_signal},
    "f16vt_f16_realized_volatility_term_structure_rv_63d_base_v002_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_rv_63d_base_v002_signal},
    "f16vt_f16_realized_volatility_term_structure_rv_252d_base_v003_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_rv_252d_base_v003_signal},
    "f16vt_f16_realized_volatility_term_structure_rvratio_5_21_base_v004_signal": {"inputs": ["close"], "func": f16vt_f16_realized_volatility_term_structure_rvratio_5_21_base_v004_signal},
    "f16vt_f16_realized_volatility_term_structure_rvratio_21_63_base_v005_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_rvratio_21_63_base_v005_signal},
    "f16vt_f16_realized_volatility_term_structure_rvratio_63_252_base_v006_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_rvratio_63_252_base_v006_signal},
    "f16vt_f16_realized_volatility_term_structure_termpctrank_5_252_base_v007_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_termpctrank_5_252_base_v007_signal},
    "f16vt_f16_realized_volatility_term_structure_invertcount_5_21_base_v008_signal": {"inputs": ["close"], "func": f16vt_f16_realized_volatility_term_structure_invertcount_5_21_base_v008_signal},
    "f16vt_f16_realized_volatility_term_structure_logslope_21_252_base_v009_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_logslope_21_252_base_v009_signal},
    "f16vt_f16_realized_volatility_term_structure_curv_5_21_63_base_v010_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_curv_5_21_63_base_v010_signal},
    "f16vt_f16_realized_volatility_term_structure_curv_21_63_252_base_v011_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_curv_21_63_252_base_v011_signal},
    "f16vt_f16_realized_volatility_term_structure_convexity_base_v012_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_convexity_base_v012_signal},
    "f16vt_f16_realized_volatility_term_structure_vol21slope_5d_base_v013_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_vol21slope_5d_base_v013_signal},
    "f16vt_f16_realized_volatility_term_structure_vol63slope_21d_base_v014_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_vol63slope_21d_base_v014_signal},
    "f16vt_f16_realized_volatility_term_structure_vol21accel_base_v015_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_vol21accel_base_v015_signal},
    "f16vt_f16_realized_volatility_term_structure_volpct_21on252_base_v016_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_volpct_21on252_base_v016_signal},
    "f16vt_f16_realized_volatility_term_structure_volz_21on120_base_v017_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_volz_21on120_base_v017_signal},
    "f16vt_f16_realized_volatility_term_structure_volquint_5d_base_v018_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_volquint_5d_base_v018_signal},
    "f16vt_f16_realized_volatility_term_structure_dayssince_volp90_base_v019_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_dayssince_volp90_base_v019_signal},
    "f16vt_f16_realized_volatility_term_structure_streakhighvol_base_v020_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_streakhighvol_base_v020_signal},
    "f16vt_f16_realized_volatility_term_structure_hlrvratio_21d_base_v021_signal": {"inputs": ["high", "low", "close"], "func": f16vt_f16_realized_volatility_term_structure_hlrvratio_21d_base_v021_signal},
    "f16vt_f16_realized_volatility_term_structure_hlrvratio_63d_base_v022_signal": {"inputs": ["high", "low", "closeadj"], "func": f16vt_f16_realized_volatility_term_structure_hlrvratio_63d_base_v022_signal},
    "f16vt_f16_realized_volatility_term_structure_retskew_21d_base_v023_signal": {"inputs": ["close"], "func": f16vt_f16_realized_volatility_term_structure_retskew_21d_base_v023_signal},
    "f16vt_f16_realized_volatility_term_structure_retskew_63d_base_v024_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_retskew_63d_base_v024_signal},
    "f16vt_f16_realized_volatility_term_structure_retkurt_21d_base_v025_signal": {"inputs": ["close"], "func": f16vt_f16_realized_volatility_term_structure_retkurt_21d_base_v025_signal},
    "f16vt_f16_realized_volatility_term_structure_retkurt_63d_base_v026_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_retkurt_63d_base_v026_signal},
    "f16vt_f16_realized_volatility_term_structure_downvol_21d_base_v027_signal": {"inputs": ["close"], "func": f16vt_f16_realized_volatility_term_structure_downvol_21d_base_v027_signal},
    "f16vt_f16_realized_volatility_term_structure_upvol_63d_base_v028_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_upvol_63d_base_v028_signal},
    "f16vt_f16_realized_volatility_term_structure_varasym_42d_base_v029_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_varasym_42d_base_v029_signal},
    "f16vt_f16_realized_volatility_term_structure_absretacf1_30d_base_v030_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_absretacf1_30d_base_v030_signal},
    "f16vt_f16_realized_volatility_term_structure_sqretacf1_60d_base_v031_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_sqretacf1_60d_base_v031_signal},
    "f16vt_f16_realized_volatility_term_structure_volpersist_30d_base_v032_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_volpersist_30d_base_v032_signal},
    "f16vt_f16_realized_volatility_term_structure_curveR2_4pt_base_v033_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_curveR2_4pt_base_v033_signal},
    "f16vt_f16_realized_volatility_term_structure_curveslopesign_base_v034_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_curveslopesign_base_v034_signal},
    "f16vt_f16_realized_volatility_term_structure_invertedsign_base_v035_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_invertedsign_base_v035_signal},
    "f16vt_f16_realized_volatility_term_structure_invertedfrac_60d_base_v036_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_invertedfrac_60d_base_v036_signal},
    "f16vt_f16_realized_volatility_term_structure_volconeshort_5on120_base_v037_signal": {"inputs": ["close"], "func": f16vt_f16_realized_volatility_term_structure_volconeshort_5on120_base_v037_signal},
    "f16vt_f16_realized_volatility_term_structure_volconedelta_base_v038_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_volconedelta_base_v038_signal},
    "f16vt_f16_realized_volatility_term_structure_voldirsign_21d_base_v039_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_voldirsign_21d_base_v039_signal},
    "f16vt_f16_realized_volatility_term_structure_volcontract_30d_base_v040_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_volcontract_30d_base_v040_signal},
    "f16vt_f16_realized_volatility_term_structure_volexpand_30d_base_v041_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_volexpand_30d_base_v041_signal},
    "f16vt_f16_realized_volatility_term_structure_avgvol_3h_base_v042_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_avgvol_3h_base_v042_signal},
    "f16vt_f16_realized_volatility_term_structure_volhdisp_3h_base_v043_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_volhdisp_3h_base_v043_signal},
    "f16vt_f16_realized_volatility_term_structure_medianvol_4h_base_v044_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_medianvol_4h_base_v044_signal},
    "f16vt_f16_realized_volatility_term_structure_arctanlogvol_21d_base_v045_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_arctanlogvol_21d_base_v045_signal},
    "f16vt_f16_realized_volatility_term_structure_tanhvolzdelta_base_v046_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_tanhvolzdelta_base_v046_signal},
    "f16vt_f16_realized_volatility_term_structure_sigmoidvolpct_base_v047_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_sigmoidvolpct_base_v047_signal},
    "f16vt_f16_realized_volatility_term_structure_madstd_ratio_21d_base_v048_signal": {"inputs": ["close"], "func": f16vt_f16_realized_volatility_term_structure_madstd_ratio_21d_base_v048_signal},
    "f16vt_f16_realized_volatility_term_structure_rms_42d_base_v049_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_rms_42d_base_v049_signal},
    "f16vt_f16_realized_volatility_term_structure_rvarratio_5_63_base_v050_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_rvarratio_5_63_base_v050_signal},
    "f16vt_f16_realized_volatility_term_structure_qvariation_30d_base_v052_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_qvariation_30d_base_v052_signal},
    "f16vt_f16_realized_volatility_term_structure_roughness_30d_base_v053_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_roughness_30d_base_v053_signal},
    "f16vt_f16_realized_volatility_term_structure_voldiffsign_21m63_base_v054_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_voldiffsign_21m63_base_v054_signal},
    "f16vt_f16_realized_volatility_term_structure_voldiffz_5m63_base_v055_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_voldiffz_5m63_base_v055_signal},
    "f16vt_f16_realized_volatility_term_structure_volofvol_21d_base_v056_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_volofvol_21d_base_v056_signal},
    "f16vt_f16_realized_volatility_term_structure_volofvol_long_base_v057_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_volofvol_long_base_v057_signal},
    "f16vt_f16_realized_volatility_term_structure_curvres21_base_v058_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_curvres21_base_v058_signal},
    "f16vt_f16_realized_volatility_term_structure_volpctslope_21d_base_v059_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_volpctslope_21d_base_v059_signal},
    "f16vt_f16_realized_volatility_term_structure_logvolslope_63d_base_v060_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_logvolslope_63d_base_v060_signal},
    "f16vt_f16_realized_volatility_term_structure_bipower_ratio_42d_base_v061_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_bipower_ratio_42d_base_v061_signal},
    "f16vt_f16_realized_volatility_term_structure_jumpcomp_42d_base_v062_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_jumpcomp_42d_base_v062_signal},
    "f16vt_f16_realized_volatility_term_structure_curveskew_4h_base_v063_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_curveskew_4h_base_v063_signal},
    "f16vt_f16_realized_volatility_term_structure_curvekurt_4h_base_v064_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_curvekurt_4h_base_v064_signal},
    "f16vt_f16_realized_volatility_term_structure_daystrough_60d_base_v065_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_daystrough_60d_base_v065_signal},
    "f16vt_f16_realized_volatility_term_structure_dayspeak_120d_base_v066_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_dayspeak_120d_base_v066_signal},
    "f16vt_f16_realized_volatility_term_structure_volsigncnt_3h_base_v067_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_volsigncnt_3h_base_v067_signal},
    "f16vt_f16_realized_volatility_term_structure_logHLstd_5d_base_v068_signal": {"inputs": ["high", "low"], "func": f16vt_f16_realized_volatility_term_structure_logHLstd_5d_base_v068_signal},
    "f16vt_f16_realized_volatility_term_structure_logHLstd_63d_base_v069_signal": {"inputs": ["high", "low"], "func": f16vt_f16_realized_volatility_term_structure_logHLstd_63d_base_v069_signal},
    "f16vt_f16_realized_volatility_term_structure_HLcurvature_base_v070_signal": {"inputs": ["high", "low"], "func": f16vt_f16_realized_volatility_term_structure_HLcurvature_base_v070_signal},
    "f16vt_f16_realized_volatility_term_structure_vol5_volofvol_base_v071_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_vol5_volofvol_base_v071_signal},
    "f16vt_f16_realized_volatility_term_structure_madratio_5_63_base_v072_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_madratio_5_63_base_v072_signal},
    "f16vt_f16_realized_volatility_term_structure_volzdiff_5_63_base_v073_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_volzdiff_5_63_base_v073_signal},
    "f16vt_f16_realized_volatility_term_structure_highvolstreak_42d_base_v074_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_highvolstreak_42d_base_v074_signal},
    "f16vt_f16_realized_volatility_term_structure_normterm_60d_base_v075_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_normterm_60d_base_v075_signal},
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
    for name, entry in f16_realized_volatility_term_structure_base_001_075_REGISTRY.items():
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
