"""f16_realized_volatility_term_structure base features 076-150.

Continuation of term-structure-of-realized-vol features with heavy structural
diversity: EWMA vol at horizons, drawdown-volatility links, regime
classifications, kurtosis-percentile, intermittent vol surges, vol-rank
slopes, GARCH-style persistence proxies, RV asymmetry, term-structure
sortino, range vs realized vol ratios at multiple horizons, vol percentiles
across horizons, more bounded composites.

Each function inline. Window > 21 uses closeadj. NaN policy preserved.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Features 076-150
# ---------------------------------------------------------------------------


# --- EWMA-based vol at horizons --------------------------------------------




def f16vt_f16_realized_volatility_term_structure_ewma_sign_94_97_base_v077_signal(closeadj):
    """Sign of EWMA(lam=0.94) - EWMA(lam=0.97) — discrete fast-vs-slow EW vol direction."""
    r = np.log(closeadj).diff()
    e94 = np.sqrt((r * r).ewm(alpha=0.06, adjust=False, min_periods=20).mean())
    e97 = np.sqrt((r * r).ewm(alpha=0.03, adjust=False, min_periods=40).mean())
    d = e94 - e97
    return np.sign(d).where(~d.isna()).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_ewmaratio_94_97_base_v078_signal(closeadj):
    """EWMA(lam=0.94) / EWMA(lam=0.97) — fast/slow EW vol term-structure ratio."""
    r = np.log(closeadj).diff()
    e94 = np.sqrt((r * r).ewm(alpha=0.06, adjust=False, min_periods=20).mean())
    e97 = np.sqrt((r * r).ewm(alpha=0.03, adjust=False, min_periods=40).mean())
    return (e94 / e97.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- Garch-style vol persistence proxies ----------------------------------


def f16vt_f16_realized_volatility_term_structure_garchpersist_base_v079_signal(closeadj):
    """Lag-1 autocorr of vol(21) over 60-bar window — vol persistence (GARCH alpha+beta proxy)."""
    n = 60
    r = np.log(closeadj).diff()
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    def _ac1(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)) or x.size < 5:
            return np.nan
        a = x[:-1]; b = x[1:]
        sa = a.std(ddof=0); sb = b.std(ddof=0)
        if sa <= 0 or sb <= 0:
            return np.nan
        return float(((a - a.mean()) * (b - b.mean())).mean() / (sa * sb))
    return v21.rolling(n, min_periods=n).apply(_ac1, raw=True).replace([np.inf, -np.inf], np.nan)


# --- Drawdown-volatility relationship ------------------------------------


def f16vt_f16_realized_volatility_term_structure_volperdraw_42d_base_v080_signal(closeadj):
    """Vol(21) divided by trailing 42d max drawdown magnitude (cluster of vol around DD)."""
    n = 42
    r = np.log(closeadj).diff()
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    roll_max = closeadj.rolling(n, min_periods=n).max()
    dd = (roll_max - closeadj) / roll_max.replace(0.0, np.nan)
    return (v21 / dd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- Vol regime: high-vol regime entropy --------------------------------


def f16vt_f16_realized_volatility_term_structure_volentropy_30d_base_v081_signal(closeadj):
    """Binary entropy of vol-above-median pattern in last 30 bars (term-regime entropy)."""
    n = 30
    r = np.log(closeadj).diff()
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    med = v21.rolling(252, min_periods=252).median()
    h = (v21 > med).astype(float).where(~v21.isna() & ~med.isna())
    def _ent(x):
        p = float(np.nanmean(x))
        if not np.isfinite(p) or p <= 0.0 or p >= 1.0:
            return 0.0
        return float(-(p * np.log(p) + (1.0 - p) * np.log(1.0 - p)))
    return h.rolling(n, min_periods=n).apply(_ent, raw=True).replace([np.inf, -np.inf], np.nan)


# --- Intermittent vol surge detector ------------------------------------


def f16vt_f16_realized_volatility_term_structure_volsurge_5over63_base_v082_signal(closeadj):
    """Binary: vol(5) > 2 * vol(63) — vol surge state."""
    r = np.log(closeadj).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    return ((v5 > 2.0 * v63)).astype(float).where(~v5.isna() & ~v63.isna()).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_volsurgefrac_60d_base_v083_signal(closeadj):
    """Fraction of last 60 bars with vol(5) > 1.5 * vol(63) — surge density."""
    r = np.log(closeadj).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    s = (v5 > 1.5 * v63).astype(float).where(~v5.isna() & ~v63.isna())
    return s.rolling(60, min_periods=60).mean().replace([np.inf, -np.inf], np.nan)


# --- Vol-rank slope -----------------------------------------------------


def f16vt_f16_realized_volatility_term_structure_volrankslope_63d_base_v084_signal(closeadj):
    """Slope of vol(63) percentile rank over 21-bar diff."""
    r = np.log(closeadj).diff()
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    p = v63.rolling(252, min_periods=252).rank(pct=True)
    return p.diff(21).replace([np.inf, -np.inf], np.nan)


# --- Kurtosis percentile (term structure of moments) -------------------


def f16vt_f16_realized_volatility_term_structure_kurtpct_42d_base_v085_signal(closeadj):
    """Percentile rank of trailing 42d kurtosis vs trailing 252d distribution of 42d kurtosis."""
    n = 42
    r = np.log(closeadj).diff()
    k = r.rolling(n, min_periods=n).kurt()
    return k.rolling(252, min_periods=120).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_skewpct_42d_base_v086_signal(closeadj):
    """Percentile rank of trailing 42d skewness vs trailing 252d distribution."""
    n = 42
    r = np.log(closeadj).diff()
    k = r.rolling(n, min_periods=n).skew()
    return k.rolling(252, min_periods=120).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# --- RV asymmetry on horizons -----------------------------------------


def f16vt_f16_realized_volatility_term_structure_downvolratio_5_63_base_v087_signal(closeadj):
    """Downside semi-vol(5) / downside semi-vol(63) — short/long downside term ratio."""
    r = np.log(closeadj).diff()
    neg = r.where(r < 0)
    d5 = neg.rolling(5, min_periods=3).std(ddof=1)
    d63 = neg.rolling(63, min_periods=30).std(ddof=1)
    return (d5 / d63.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_updownratio_42d_base_v088_signal(closeadj):
    """Upside vs downside semi-vol ratio at 42d — asymmetry within horizon."""
    n = 42
    r = np.log(closeadj).diff()
    pos = r.where(r > 0)
    neg = r.where(r < 0)
    up = pos.rolling(n, min_periods=15).std(ddof=1)
    dn = neg.rolling(n, min_periods=15).std(ddof=1)
    return (up / dn.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- Range/Realized vol cross-horizon ratios -------------------------


def f16vt_f16_realized_volatility_term_structure_rangereal_5d_base_v089_signal(high, low, close):
    """Range-based RV proxy(5d): mean of log(H/L) over 5 bars / RV-return(5d)."""
    n = 5
    s = np.log(high / low.replace(0.0, np.nan))
    rng_mean = s.rolling(n, min_periods=n).mean()
    r = np.log(close).diff()
    rv = r.rolling(n, min_periods=n).std(ddof=1)
    return (rng_mean / rv.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_rangereal_63d_base_v090_signal(high, low, closeadj):
    """Range vs realized ratio at 63d horizon."""
    n = 63
    s = np.log(high / low.replace(0.0, np.nan))
    rng_mean = s.rolling(n, min_periods=n).mean()
    r = np.log(closeadj).diff()
    rv = r.rolling(n, min_periods=n).std(ddof=1)
    return (rng_mean / rv.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- Garman-Klass cross-horizon ratio --------------------------------


def f16vt_f16_realized_volatility_term_structure_gktermratio_base_v091_signal(open_, high, low, close):
    """GK vol proxy at 21d / GK vol proxy at 63d. NOTE: f18 owns GK; this is the
    cross-horizon ratio, which is term-structure specific."""
    gk = 0.5 * (np.log(high / low.replace(0.0, np.nan))) ** 2 - (2.0 * np.log(2.0) - 1.0) * (np.log(close / open_.replace(0.0, np.nan))) ** 2
    g21 = gk.rolling(21, min_periods=21).mean()
    g63 = gk.rolling(63, min_periods=63).mean()
    return (g21 / g63.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- Z-score variants ---------------------------------------------------


def f16vt_f16_realized_volatility_term_structure_volz_5on60_base_v092_signal(close):
    """Z-score of vol(5) over trailing 60d distribution — short-vol surprise."""
    n = 60
    r = np.log(close).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    mu = v5.rolling(n, min_periods=n).mean()
    sd = v5.rolling(n, min_periods=n).std(ddof=1)
    return ((v5 - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_volz_252on500_base_v093_signal(closeadj):
    """Long-run z-score: vol(252) standardized vs trailing 500 bars. Capped via available data."""
    r = np.log(closeadj).diff()
    v252 = r.rolling(252, min_periods=252).std(ddof=1)
    mu = v252.rolling(500, min_periods=300).mean()
    sd = v252.rolling(500, min_periods=300).std(ddof=1)
    return ((v252 - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- Term-structure of MAD ------------------------------------------


def f16vt_f16_realized_volatility_term_structure_madcurv_base_v094_signal(closeadj):
    """MAD(5) - 2*MAD(21) + MAD(63) — curvature using MAD-based term structure."""
    r = np.log(closeadj).diff()
    def _mad(x, n):
        mu = x.rolling(n, min_periods=n).mean()
        return (x - mu).abs().rolling(n, min_periods=n).mean()
    m5 = _mad(r, 5)
    m21 = _mad(r, 21)
    m63 = _mad(r, 63)
    return (m5 - 2.0 * m21 + m63).replace([np.inf, -np.inf], np.nan)


# --- Vol vs trailing-mean RoC -------------------------------------


def f16vt_f16_realized_volatility_term_structure_vol_aboveMA_42d_base_v095_signal(closeadj):
    """Fraction of last 42 bars where vol(5) > mean(vol(5),21). Short-vol-above-trend."""
    n = 42
    r = np.log(closeadj).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    mu = v5.rolling(21, min_periods=21).mean()
    flag = (v5 > mu).astype(float).where(~v5.isna() & ~mu.isna())
    return flag.rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


# --- Term-structure level via geometric mean ---------------------


def f16vt_f16_realized_volatility_term_structure_geomean_vols_base_v096_signal(closeadj):
    """Geometric mean of vol(5), vol(21), vol(63) — composite vol level (multiplicative)."""
    r = np.log(closeadj).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    g = np.exp((np.log(v5.replace(0.0, np.nan)) + np.log(v21.replace(0.0, np.nan)) + np.log(v63.replace(0.0, np.nan))) / 3.0)
    return g.replace([np.inf, -np.inf], np.nan)


# --- Vol ratio percentile rank ---------------------------------


def f16vt_f16_realized_volatility_term_structure_volratio_rank_21_252_base_v097_signal(closeadj):
    """Percentile rank of vol(21)/vol(252) over trailing 252d — mid-long ratio regime."""
    r = np.log(closeadj).diff()
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    v252 = r.rolling(252, min_periods=252).std(ddof=1)
    ratio = v21 / v252.replace(0.0, np.nan)
    return ratio.rolling(252, min_periods=120).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# --- Term-structure curvature percentile ----------------------


def f16vt_f16_realized_volatility_term_structure_curv_rank_base_v098_signal(closeadj):
    """Percentile rank of (vol5-2*vol21+vol63) curvature over 252d."""
    r = np.log(closeadj).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    c = v5 - 2.0 * v21 + v63
    return c.rolling(252, min_periods=120).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# --- Sortino-style vol ---------------------------------------


def f16vt_f16_realized_volatility_term_structure_sortino_vol_42d_base_v099_signal(closeadj):
    """Sortino-style: mean(r,42) / downside_std(r,42) — risk-adjusted return scaled by downside vol."""
    n = 42
    r = np.log(closeadj).diff()
    mu = r.rolling(n, min_periods=n).mean()
    neg = r.where(r < 0)
    dn = neg.rolling(n, min_periods=15).std(ddof=1)
    return (mu / dn.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- Cross-horizon: vol curve point lookup ----------------


def f16vt_f16_realized_volatility_term_structure_volgap_5_21_pct_base_v100_signal(close):
    """(vol(5) - vol(21)) / vol(21) — relative term-structure gap. Different sign than ratio."""
    r = np.log(close).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    return ((v5 - v21) / v21.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_volgap_63_252_pct_base_v101_signal(closeadj):
    """(vol(63) - vol(252)) / vol(252) — relative term-structure gap at long end."""
    r = np.log(closeadj).diff()
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    v252 = r.rolling(252, min_periods=252).std(ddof=1)
    return ((v63 - v252) / v252.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- Distributional features at multiple horizons ------------


def f16vt_f16_realized_volatility_term_structure_kurtskew_diff_42d_base_v102_signal(closeadj):
    """Kurt(r,42) minus 3 * |Skew(r,42)| — combined tail/asymmetry signature."""
    n = 42
    r = np.log(closeadj).diff()
    k = r.rolling(n, min_periods=n).kurt()
    s = r.rolling(n, min_periods=n).skew()
    return (k - 3.0 * s.abs()).replace([np.inf, -np.inf], np.nan)


# --- Discrete classification of term structure ----------


def f16vt_f16_realized_volatility_term_structure_termclass_base_v103_signal(closeadj):
    """Categorical: 0 if normal (v5<v21<v63), 1 if hump (v21>v5,v21>v63), 2 if dip (v21<v5,v21<v63),
    3 if inverted (v5>v21>v63), else 4 (other)."""
    r = np.log(closeadj).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    df = pd.concat([v5, v21, v63], axis=1)
    def _cls(row):
        a, b, c = row
        if not (np.isfinite(a) and np.isfinite(b) and np.isfinite(c)):
            return np.nan
        if a < b and b < c:
            return 0.0
        if b > a and b > c:
            return 1.0
        if b < a and b < c:
            return 2.0
        if a > b and b > c:
            return 3.0
        return 4.0
    return df.apply(_cls, axis=1).replace([np.inf, -np.inf], np.nan)


# --- Range vol slopes ------------------------------------


def f16vt_f16_realized_volatility_term_structure_hlvolslope_42d_base_v104_signal(high, low):
    """Slope of std(log(H/L), 21) over 10 bars — range-vol velocity."""
    s = np.log(high / low.replace(0.0, np.nan))
    sv21 = s.rolling(21, min_periods=21).std(ddof=1)
    return sv21.diff(10).replace([np.inf, -np.inf], np.nan)


# --- More vol-of-vol features -------------------------


def f16vt_f16_realized_volatility_term_structure_volofvol_rank_base_v105_signal(closeadj):
    """Percentile rank of vol-of-vol(21,63) over 252d — vov regime."""
    r = np.log(closeadj).diff()
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    vov = v21.rolling(63, min_periods=63).std(ddof=1)
    return vov.rolling(252, min_periods=120).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# --- Trailing min-vol streaks --------------------


def f16vt_f16_realized_volatility_term_structure_lowvol_streak_base_v106_signal(closeadj):
    """Run-length of bars with vol(21) < trailing 252d 25th percentile."""
    r = np.log(closeadj).diff()
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    q25 = v21.rolling(252, min_periods=252).quantile(0.25)
    h = (v21 < q25).astype(float).where(~v21.isna() & ~q25.isna())
    grp = (h != h.shift(1)).cumsum()
    streak = h.groupby(grp).cumsum() * h
    return streak.replace([np.inf, -np.inf], np.nan)


# --- Vol clustering via rolling variance of |r| ---------


def f16vt_f16_realized_volatility_term_structure_absretvar_30d_base_v107_signal(closeadj):
    """Variance of |log-returns| over 30 bars — secondary vol-clustering moment."""
    n = 30
    r = np.log(closeadj).diff().abs()
    return r.rolling(n, min_periods=n).var(ddof=1).replace([np.inf, -np.inf], np.nan)


# --- Tail-quantile of returns at horizon -------


def f16vt_f16_realized_volatility_term_structure_var95_42d_base_v108_signal(closeadj):
    """5th percentile of trailing 42d log-returns (VaR proxy at horizon)."""
    n = 42
    r = np.log(closeadj).diff()
    return r.rolling(n, min_periods=n).quantile(0.05).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_var95_120d_base_v109_signal(closeadj):
    """5th percentile of trailing 120d log-returns (longer-horizon VaR)."""
    n = 120
    r = np.log(closeadj).diff()
    return r.rolling(n, min_periods=n).quantile(0.05).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_es95_42d_base_v110_signal(closeadj):
    """Expected shortfall: mean of returns below 5th percentile, 42d."""
    n = 42
    r = np.log(closeadj).diff()
    def _es(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)) or x.size < 10:
            return np.nan
        q = np.quantile(x, 0.05)
        tail = x[x <= q]
        if tail.size == 0:
            return np.nan
        return float(tail.mean())
    return r.rolling(n, min_periods=n).apply(_es, raw=True).replace([np.inf, -np.inf], np.nan)


# --- Inter-quartile range of returns at horizon ---------


def f16vt_f16_realized_volatility_term_structure_iqr_21d_base_v111_signal(close):
    """IQR of log-returns over 21 bars — robust vol scale at short horizon."""
    n = 21
    r = np.log(close).diff()
    q75 = r.rolling(n, min_periods=n).quantile(0.75)
    q25 = r.rolling(n, min_periods=n).quantile(0.25)
    return (q75 - q25).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_iqr_63d_base_v112_signal(closeadj):
    """IQR of log-returns over 63 bars."""
    n = 63
    r = np.log(closeadj).diff()
    q75 = r.rolling(n, min_periods=n).quantile(0.75)
    q25 = r.rolling(n, min_periods=n).quantile(0.25)
    return (q75 - q25).replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_iqrratio_21_63_base_v113_signal(closeadj):
    """IQR(r,21) / IQR(r,63) — robust term-structure ratio."""
    r = np.log(closeadj).diff()
    q75_21 = r.rolling(21, min_periods=21).quantile(0.75)
    q25_21 = r.rolling(21, min_periods=21).quantile(0.25)
    q75_63 = r.rolling(63, min_periods=63).quantile(0.75)
    q25_63 = r.rolling(63, min_periods=63).quantile(0.25)
    iqr21 = q75_21 - q25_21
    iqr63 = q75_63 - q25_63
    return (iqr21 / iqr63.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- Median absolute deviation ------------------------


def f16vt_f16_realized_volatility_term_structure_madmed_21d_base_v114_signal(close):
    """Median absolute deviation around the median, 21d — robust vol."""
    n = 21
    r = np.log(close).diff()
    med = r.rolling(n, min_periods=n).median()
    return (r - med).abs().rolling(n, min_periods=n).median().replace([np.inf, -np.inf], np.nan)


# --- Vol-cluster: count of large moves -----------


def f16vt_f16_realized_volatility_term_structure_bigmove_3sigma_42d_base_v115_signal(closeadj):
    """Count of last 42 bars where |r| > 3 * trailing-252d-std(r)."""
    n = 42
    r = np.log(closeadj).diff()
    sd = r.rolling(252, min_periods=252).std(ddof=1)
    flag = (r.abs() > 3.0 * sd).astype(float).where(~r.isna() & ~sd.isna())
    return flag.rolling(n, min_periods=n).sum().replace([np.inf, -np.inf], np.nan)


# --- Term-structure entropy ------------------------


def f16vt_f16_realized_volatility_term_structure_termGini_base_v116_signal(closeadj):
    """Gini-style concentration index across vol curve {5,21,63,252} — 0=uniform, 1=concentrated."""
    r = np.log(closeadj).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    v252 = r.rolling(252, min_periods=252).std(ddof=1)
    df = pd.concat([v5, v21, v63, v252], axis=1)
    def _gini(row):
        y = np.asarray(row, dtype=float)
        if np.any(~np.isfinite(y)) or np.any(y <= 0):
            return np.nan
        y_sorted = np.sort(y)
        nrm = y_sorted.sum()
        if nrm <= 0:
            return np.nan
        cum = np.cumsum(y_sorted) / nrm
        n = len(y)
        return float(1.0 - 2.0 * (cum.sum() - 0.5) / n)
    return df.apply(_gini, axis=1).replace([np.inf, -np.inf], np.nan)


# --- Long-vol / short-vol percentile gap -------


def f16vt_f16_realized_volatility_term_structure_volgap_pct_5_252_base_v117_signal(closeadj):
    """Percentile(vol5,252d) minus percentile(vol252,500d) — short-vs-long regime divergence."""
    r = np.log(closeadj).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    v252 = r.rolling(252, min_periods=252).std(ddof=1)
    p5 = v5.rolling(252, min_periods=120).rank(pct=True)
    p252 = v252.rolling(500, min_periods=260).rank(pct=True)
    return (p5 - p252).replace([np.inf, -np.inf], np.nan)


# --- Vol-of-vol slope -------------------------


def f16vt_f16_realized_volatility_term_structure_vovslope_base_v118_signal(closeadj):
    """Slope of vol-of-vol(21,63) over 21 bars — vov velocity."""
    r = np.log(closeadj).diff()
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    vov = v21.rolling(63, min_periods=63).std(ddof=1)
    return vov.diff(21).replace([np.inf, -np.inf], np.nan)


# --- Vol direction agreement across horizons -----


def f16vt_f16_realized_volatility_term_structure_voldiragree_base_v119_signal(closeadj):
    """+1 if vol(5).diff(5)>0 & vol(21).diff(5)>0; -1 if both <0; 0 mixed — direction alignment."""
    r = np.log(closeadj).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    d5 = v5.diff(5); d21 = v21.diff(5)
    out = pd.Series(np.where((d5 > 0) & (d21 > 0), 1.0, np.where((d5 < 0) & (d21 < 0), -1.0, 0.0)), index=v5.index, dtype=float)
    return out.where(~d5.isna() & ~d21.isna()).replace([np.inf, -np.inf], np.nan)


# --- Vol curve smoothness ----------------------


def f16vt_f16_realized_volatility_term_structure_curvesmooth_base_v120_signal(closeadj):
    """abs((vol5-vol21)+(vol63-vol21)) — convexity magnitude, sign-independent."""
    r = np.log(closeadj).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    return ((v5 - v21).abs() + (v63 - v21).abs()).replace([np.inf, -np.inf], np.nan)


# --- Crossing count of vol(5) and vol(21) -----


def f16vt_f16_realized_volatility_term_structure_volxover_60d_base_v121_signal(closeadj):
    """Number of vol(5)-vol(21) sign crossings in trailing 60 bars — term-structure churn."""
    n = 60
    r = np.log(closeadj).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    s = np.sign(v5 - v21)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(n, min_periods=n).sum().replace([np.inf, -np.inf], np.nan)


# --- Term structure standard deviations -----


def f16vt_f16_realized_volatility_term_structure_argmaxhorizon_base_v122_signal(closeadj):
    """Discrete index (0-3) of which horizon among {5,21,63,252} has the LARGEST vol — locates peak."""
    r = np.log(closeadj).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    v252 = r.rolling(252, min_periods=252).std(ddof=1)
    df = pd.concat([v5, v21, v63, v252], axis=1)
    def _arg(row):
        y = np.asarray(row, dtype=float)
        if np.any(~np.isfinite(y)):
            return np.nan
        return float(np.argmax(y))
    return df.apply(_arg, axis=1).replace([np.inf, -np.inf], np.nan)


# --- Squared-return ratio at horizons -----


def f16vt_f16_realized_volatility_term_structure_sumr2_21on63_base_v123_signal(closeadj):
    """sum(r^2,21) / sum(r^2,63) — discrete RV term ratio (no annualization)."""
    r = np.log(closeadj).diff()
    rv21 = (r * r).rolling(21, min_periods=21).sum()
    rv63 = (r * r).rolling(63, min_periods=63).sum()
    return (rv21 / rv63.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- Half-life of volatility shocks (mean-reversion proxy) -----


def f16vt_f16_realized_volatility_term_structure_volhalflife_base_v124_signal(closeadj):
    """Estimated half-life of vol(21) shocks via lag-1 AR(1) of log(vol21).
    HL = -ln(2)/ln(rho), capped at 252. Window=120."""
    n = 120
    r = np.log(closeadj).diff()
    v21 = np.log(r.rolling(21, min_periods=21).std(ddof=1).replace(0.0, np.nan))
    def _hl(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)) or x.size < 30:
            return np.nan
        a = x[:-1]; b = x[1:]
        sa = a.std(ddof=0); sb = b.std(ddof=0)
        if sa <= 0 or sb <= 0:
            return np.nan
        rho = float(((a - a.mean()) * (b - b.mean())).mean() / (sa * sb))
        if rho >= 0.999 or rho <= -0.999:
            return 252.0
        if rho <= 0:
            return 1.0
        return float(min(252.0, -np.log(2.0) / np.log(rho)))
    return v21.rolling(n, min_periods=n).apply(_hl, raw=True).replace([np.inf, -np.inf], np.nan)


# --- Mean shift in vol regime -----


def f16vt_f16_realized_volatility_term_structure_volmeanshift_base_v125_signal(closeadj):
    """mean(vol(21), 21) - mean(vol(21), 63) — slow regime drift in vol level."""
    r = np.log(closeadj).diff()
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    m1 = v21.rolling(21, min_periods=21).mean()
    m2 = v21.rolling(63, min_periods=63).mean()
    return (m1 - m2).replace([np.inf, -np.inf], np.nan)


# --- Vol second derivative across horizons ------


def f16vt_f16_realized_volatility_term_structure_vol2derivpct_base_v126_signal(closeadj):
    """Percentile rank of |vol21 - 2*vol21.shift(5) + vol21.shift(10)| over 252d."""
    r = np.log(closeadj).diff()
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    accel = (v21 - 2.0 * v21.shift(5) + v21.shift(10)).abs()
    return accel.rolling(252, min_periods=120).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# --- Vol-rank diff between horizons -----


def f16vt_f16_realized_volatility_term_structure_volrank_diff_5_21_base_v127_signal(close):
    """Pct-rank(vol5,120d) - pct-rank(vol21,120d) — short vs mid regime divergence."""
    r = np.log(close).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    p5 = v5.rolling(120, min_periods=80).rank(pct=True)
    p21 = v21.rolling(120, min_periods=80).rank(pct=True)
    return (p5 - p21).replace([np.inf, -np.inf], np.nan)


# --- Sharpe-like signed vol indicator -----


def f16vt_f16_realized_volatility_term_structure_signedvol_21d_base_v128_signal(close):
    """sign(mean(r,21)) * vol(21) — vol with directional sign attached."""
    r = np.log(close).diff()
    mu = r.rolling(21, min_periods=21).mean()
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    return (np.sign(mu) * v21).replace([np.inf, -np.inf], np.nan)


# --- Term structure with EWMA mid-vol -----


def f16vt_f16_realized_volatility_term_structure_ewma_termratio_base_v129_signal(closeadj):
    """EWMA(lam=0.94) / vol(63) — short EWMA vs long realized term ratio."""
    r = np.log(closeadj).diff()
    e = np.sqrt((r * r).ewm(alpha=0.06, adjust=False, min_periods=20).mean())
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    return (e / v63.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- Rolling correlation of vol curves -----


def f16vt_f16_realized_volatility_term_structure_volcorr_5_63_base_v130_signal(closeadj):
    """Rolling 63-bar correlation between vol(5) and vol(63) — comovement of term ends."""
    r = np.log(closeadj).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    return v5.rolling(63, min_periods=40).corr(v63).replace([np.inf, -np.inf], np.nan)


# --- Bipower / RV ratio at horizons -----


def f16vt_f16_realized_volatility_term_structure_bvrv_diff_21_63_base_v131_signal(closeadj):
    """BV/RV at 21 minus BV/RV at 63 — jump-component term-structure differential."""
    r = np.log(closeadj).diff()
    ra = r.abs()
    bv21 = (ra * ra.shift(1)).rolling(21, min_periods=21).sum() * (np.pi / 2.0)
    rv21 = (r * r).rolling(21, min_periods=21).sum()
    bv63 = (ra * ra.shift(1)).rolling(63, min_periods=63).sum() * (np.pi / 2.0)
    rv63 = (r * r).rolling(63, min_periods=63).sum()
    return ((bv21 / rv21.replace(0.0, np.nan)) - (bv63 / rv63.replace(0.0, np.nan))).replace([np.inf, -np.inf], np.nan)


# --- Tail-asymmetry across horizons -----


def f16vt_f16_realized_volatility_term_structure_tailasym_42d_base_v132_signal(closeadj):
    """abs(min(r,42)) / max(r,42) — tail magnitude ratio at horizon."""
    n = 42
    r = np.log(closeadj).diff()
    mn = r.rolling(n, min_periods=n).min().abs()
    mx = r.rolling(n, min_periods=n).max()
    return (mn / mx.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- Range-vol level at horizons -----




def f16vt_f16_realized_volatility_term_structure_hlrange_63d_base_v134_signal(high, low, closeadj):
    """mean((high-low)/closeadj, 63) — long-horizon range-based vol level."""
    n = 63
    return ((high - low) / closeadj.replace(0.0, np.nan)).rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


def f16vt_f16_realized_volatility_term_structure_hlrange_zscore_base_v135_signal(high, low, closeadj):
    """Z-score of (HL/C,21)mean over trailing 252d — range-vol mid-horizon regime."""
    rng = (high - low) / closeadj.replace(0.0, np.nan)
    m21 = rng.rolling(21, min_periods=21).mean()
    mu = m21.rolling(252, min_periods=120).mean()
    sd = m21.rolling(252, min_periods=120).std(ddof=1)
    return ((m21 - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- Time series of vol acceleration -----


def f16vt_f16_realized_volatility_term_structure_volaccelsign_base_v136_signal(closeadj):
    """Sign of vol(21).diff(5).diff(5) — vol acceleration direction."""
    r = np.log(closeadj).diff()
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    acc = v21.diff(5).diff(5)
    return np.sign(acc).where(~acc.isna()).replace([np.inf, -np.inf], np.nan)


# --- Skewness term-structure --------


def f16vt_f16_realized_volatility_term_structure_skewratio_21_63_base_v137_signal(closeadj):
    """Skew(r,21) - Skew(r,63) — skewness term-structure differential."""
    r = np.log(closeadj).diff()
    s21 = r.rolling(21, min_periods=21).skew()
    s63 = r.rolling(63, min_periods=63).skew()
    return (s21 - s63).replace([np.inf, -np.inf], np.nan)


# --- Kurt term-structure --------


def f16vt_f16_realized_volatility_term_structure_kurtdiff_21_63_base_v138_signal(closeadj):
    """Kurt(r,21) - Kurt(r,63) — kurtosis term-structure differential."""
    r = np.log(closeadj).diff()
    k21 = r.rolling(21, min_periods=21).kurt()
    k63 = r.rolling(63, min_periods=63).kurt()
    return (k21 - k63).replace([np.inf, -np.inf], np.nan)


# --- Quantile-based term-structure --------


def f16vt_f16_realized_volatility_term_structure_q9diff_21_63_base_v139_signal(closeadj):
    """quantile(r,0.9,21) - quantile(r,0.9,63) — upper-tail term-structure differential."""
    r = np.log(closeadj).diff()
    q21 = r.rolling(21, min_periods=21).quantile(0.9)
    q63 = r.rolling(63, min_periods=63).quantile(0.9)
    return (q21 - q63).replace([np.inf, -np.inf], np.nan)


# --- Tanh of curvature normalized -------


def f16vt_f16_realized_volatility_term_structure_tanh_volvar_42d_base_v140_signal(closeadj):
    """tanh of (var(vol(5),42) / mean(vol(5),42)^2). Bounded short-vol CoV-squared."""
    r = np.log(closeadj).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    mu = v5.rolling(42, min_periods=42).mean()
    var = v5.rolling(42, min_periods=42).var(ddof=1)
    cov2 = var / (mu * mu).replace(0.0, np.nan)
    return np.tanh(cov2 * 5.0).replace([np.inf, -np.inf], np.nan)


# --- arctan of slope -------


def f16vt_f16_realized_volatility_term_structure_arctanslope_base_v141_signal(closeadj):
    """arctan of log-log curve slope across {5,63,252} — bounded power-law exponent."""
    r = np.log(closeadj).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    v252 = r.rolling(252, min_periods=252).std(ddof=1)
    x = np.log(np.array([5.0, 63.0, 252.0]))
    xm = x - x.mean()
    sxx = (xm * xm).sum()
    def _s(row):
        y = np.array(row, dtype=float)
        if np.any(~np.isfinite(y)) or np.any(y <= 0):
            return np.nan
        ly = np.log(y); lym = ly - ly.mean()
        return float(np.arctan((xm * lym).sum() / sxx))
    df = pd.concat([v5, v63, v252], axis=1)
    return df.apply(_s, axis=1).replace([np.inf, -np.inf], np.nan)


# --- Drawup-vol vs Drawdown-vol -------


def f16vt_f16_realized_volatility_term_structure_ddvolasym_42d_base_v142_signal(closeadj):
    """Max-drawdown over 42 minus max-drawup over 42 (both signed). Asym vol from path."""
    n = 42
    rm = closeadj.rolling(n, min_periods=n).max()
    rmn = closeadj.rolling(n, min_periods=n).min()
    dd = (closeadj - rm) / rm.replace(0.0, np.nan)
    du = (closeadj - rmn) / rmn.replace(0.0, np.nan)
    return (du.abs() - dd.abs()).replace([np.inf, -np.inf], np.nan)


# --- Sign-streak persistence of vol-direction -------


def f16vt_f16_realized_volatility_term_structure_volsignstreak_base_v143_signal(closeadj):
    """Run-length of sign of vol(21).diff() (positive=vol rising consecutive bars)."""
    r = np.log(closeadj).diff()
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    s = np.sign(v21.diff()).where(~v21.isna() & ~v21.diff().isna())
    grp = (s != s.shift(1)).cumsum()
    streak = s.groupby(grp).cumcount() + 1
    return (streak * np.sign(s)).replace([np.inf, -np.inf], np.nan)


# --- 5-vol rank intersected with 63-vol regime -------


def f16vt_f16_realized_volatility_term_structure_regimecombo_base_v144_signal(closeadj):
    """Binary: 1 if pct-rank(vol5,120)>0.7 AND pct-rank(vol63,252)<0.3 (short up, long calm) else 0."""
    r = np.log(closeadj).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    p5 = v5.rolling(120, min_periods=80).rank(pct=True)
    p63 = v63.rolling(252, min_periods=120).rank(pct=True)
    return ((p5 > 0.7) & (p63 < 0.3)).astype(float).where(~p5.isna() & ~p63.isna()).replace([np.inf, -np.inf], np.nan)


# --- Z-score of vol curvature -------


def f16vt_f16_realized_volatility_term_structure_curvslopediff_base_v145_signal(closeadj):
    """Slope(vol5-vol21)+slope(vol63-vol21) — curvature measured via 5-bar diffs."""
    r = np.log(closeadj).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    return ((v5 - v21).diff(5) + (v63 - v21).diff(5)).replace([np.inf, -np.inf], np.nan)


# --- arctan z-curvature -------


def f16vt_f16_realized_volatility_term_structure_arctan_volpersist_base_v146_signal(closeadj):
    """arctan of vol(21) autocorr at lag 5 over 60-bar window. Bounded vol persistence."""
    n = 60
    r = np.log(closeadj).diff()
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    def _ac5(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)) or x.size < 12:
            return np.nan
        a = x[:-5]; b = x[5:]
        sa = a.std(ddof=0); sb = b.std(ddof=0)
        if sa <= 0 or sb <= 0:
            return np.nan
        return float(((a - a.mean()) * (b - b.mean())).mean() / (sa * sb))
    ac = v21.rolling(n, min_periods=n).apply(_ac5, raw=True)
    return np.arctan(ac * 2.0).replace([np.inf, -np.inf], np.nan)


# --- Vol crash hours (count of |r| > q95(252)) at horizon -------


def f16vt_f16_realized_volatility_term_structure_tailcount_60d_base_v147_signal(closeadj):
    """Count of last 60 bars where |r| > 95th percentile of |r| over 252d."""
    n = 60
    r = np.log(closeadj).diff().abs()
    q95 = r.rolling(252, min_periods=252).quantile(0.95)
    flag = (r > q95).astype(float).where(~r.isna() & ~q95.isna())
    return flag.rolling(n, min_periods=n).sum().replace([np.inf, -np.inf], np.nan)


# --- Roughness term-structure -------


def f16vt_f16_realized_volatility_term_structure_roughratio_30_120_base_v148_signal(closeadj):
    """Roughness(30) / Roughness(120) — path-roughness term structure."""
    r = np.log(closeadj).diff()
    num30 = r.diff().abs().rolling(30, min_periods=30).sum()
    den30 = r.abs().rolling(30, min_periods=30).sum()
    num120 = r.diff().abs().rolling(120, min_periods=120).sum()
    den120 = r.abs().rolling(120, min_periods=120).sum()
    r30 = num30 / den30.replace(0.0, np.nan)
    r120 = num120 / den120.replace(0.0, np.nan)
    return (r30 / r120.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- Trend within vol -------


def f16vt_f16_realized_volatility_term_structure_volltrend_60d_base_v149_signal(closeadj):
    """Trailing 60-bar correlation of vol(21) with time index — does vol trend up or down?"""
    n = 60
    r = np.log(closeadj).diff()
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    t = pd.Series(np.arange(len(v21), dtype=float), index=v21.index)
    return v21.rolling(n, min_periods=n).corr(t).replace([np.inf, -np.inf], np.nan)


# --- Vol persistence binary -------


def f16vt_f16_realized_volatility_term_structure_volstickyabove_base_v150_signal(closeadj):
    """Fraction of last 21 bars where vol(5)>vol(21)>vol(63) (term inversion persistence)."""
    n = 21
    r = np.log(closeadj).diff()
    v5 = r.rolling(5, min_periods=5).std(ddof=1)
    v21 = r.rolling(21, min_periods=21).std(ddof=1)
    v63 = r.rolling(63, min_periods=63).std(ddof=1)
    inv = ((v5 > v21) & (v21 > v63)).astype(float).where(~v5.isna() & ~v21.isna() & ~v63.isna())
    return inv.rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f16_realized_volatility_term_structure_base_076_150_REGISTRY = {
    "f16vt_f16_realized_volatility_term_structure_ewma_sign_94_97_base_v077_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_ewma_sign_94_97_base_v077_signal},
    "f16vt_f16_realized_volatility_term_structure_ewmaratio_94_97_base_v078_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_ewmaratio_94_97_base_v078_signal},
    "f16vt_f16_realized_volatility_term_structure_garchpersist_base_v079_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_garchpersist_base_v079_signal},
    "f16vt_f16_realized_volatility_term_structure_volperdraw_42d_base_v080_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_volperdraw_42d_base_v080_signal},
    "f16vt_f16_realized_volatility_term_structure_volentropy_30d_base_v081_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_volentropy_30d_base_v081_signal},
    "f16vt_f16_realized_volatility_term_structure_volsurge_5over63_base_v082_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_volsurge_5over63_base_v082_signal},
    "f16vt_f16_realized_volatility_term_structure_volsurgefrac_60d_base_v083_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_volsurgefrac_60d_base_v083_signal},
    "f16vt_f16_realized_volatility_term_structure_volrankslope_63d_base_v084_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_volrankslope_63d_base_v084_signal},
    "f16vt_f16_realized_volatility_term_structure_kurtpct_42d_base_v085_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_kurtpct_42d_base_v085_signal},
    "f16vt_f16_realized_volatility_term_structure_skewpct_42d_base_v086_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_skewpct_42d_base_v086_signal},
    "f16vt_f16_realized_volatility_term_structure_downvolratio_5_63_base_v087_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_downvolratio_5_63_base_v087_signal},
    "f16vt_f16_realized_volatility_term_structure_updownratio_42d_base_v088_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_updownratio_42d_base_v088_signal},
    "f16vt_f16_realized_volatility_term_structure_rangereal_5d_base_v089_signal": {"inputs": ["high", "low", "close"], "func": f16vt_f16_realized_volatility_term_structure_rangereal_5d_base_v089_signal},
    "f16vt_f16_realized_volatility_term_structure_rangereal_63d_base_v090_signal": {"inputs": ["high", "low", "closeadj"], "func": f16vt_f16_realized_volatility_term_structure_rangereal_63d_base_v090_signal},
    "f16vt_f16_realized_volatility_term_structure_gktermratio_base_v091_signal": {"inputs": ["open", "high", "low", "close"], "func": f16vt_f16_realized_volatility_term_structure_gktermratio_base_v091_signal},
    "f16vt_f16_realized_volatility_term_structure_volz_5on60_base_v092_signal": {"inputs": ["close"], "func": f16vt_f16_realized_volatility_term_structure_volz_5on60_base_v092_signal},
    "f16vt_f16_realized_volatility_term_structure_volz_252on500_base_v093_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_volz_252on500_base_v093_signal},
    "f16vt_f16_realized_volatility_term_structure_madcurv_base_v094_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_madcurv_base_v094_signal},
    "f16vt_f16_realized_volatility_term_structure_vol_aboveMA_42d_base_v095_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_vol_aboveMA_42d_base_v095_signal},
    "f16vt_f16_realized_volatility_term_structure_geomean_vols_base_v096_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_geomean_vols_base_v096_signal},
    "f16vt_f16_realized_volatility_term_structure_volratio_rank_21_252_base_v097_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_volratio_rank_21_252_base_v097_signal},
    "f16vt_f16_realized_volatility_term_structure_curv_rank_base_v098_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_curv_rank_base_v098_signal},
    "f16vt_f16_realized_volatility_term_structure_sortino_vol_42d_base_v099_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_sortino_vol_42d_base_v099_signal},
    "f16vt_f16_realized_volatility_term_structure_volgap_5_21_pct_base_v100_signal": {"inputs": ["close"], "func": f16vt_f16_realized_volatility_term_structure_volgap_5_21_pct_base_v100_signal},
    "f16vt_f16_realized_volatility_term_structure_volgap_63_252_pct_base_v101_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_volgap_63_252_pct_base_v101_signal},
    "f16vt_f16_realized_volatility_term_structure_kurtskew_diff_42d_base_v102_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_kurtskew_diff_42d_base_v102_signal},
    "f16vt_f16_realized_volatility_term_structure_termclass_base_v103_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_termclass_base_v103_signal},
    "f16vt_f16_realized_volatility_term_structure_hlvolslope_42d_base_v104_signal": {"inputs": ["high", "low"], "func": f16vt_f16_realized_volatility_term_structure_hlvolslope_42d_base_v104_signal},
    "f16vt_f16_realized_volatility_term_structure_volofvol_rank_base_v105_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_volofvol_rank_base_v105_signal},
    "f16vt_f16_realized_volatility_term_structure_lowvol_streak_base_v106_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_lowvol_streak_base_v106_signal},
    "f16vt_f16_realized_volatility_term_structure_absretvar_30d_base_v107_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_absretvar_30d_base_v107_signal},
    "f16vt_f16_realized_volatility_term_structure_var95_42d_base_v108_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_var95_42d_base_v108_signal},
    "f16vt_f16_realized_volatility_term_structure_var95_120d_base_v109_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_var95_120d_base_v109_signal},
    "f16vt_f16_realized_volatility_term_structure_es95_42d_base_v110_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_es95_42d_base_v110_signal},
    "f16vt_f16_realized_volatility_term_structure_iqr_21d_base_v111_signal": {"inputs": ["close"], "func": f16vt_f16_realized_volatility_term_structure_iqr_21d_base_v111_signal},
    "f16vt_f16_realized_volatility_term_structure_iqr_63d_base_v112_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_iqr_63d_base_v112_signal},
    "f16vt_f16_realized_volatility_term_structure_iqrratio_21_63_base_v113_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_iqrratio_21_63_base_v113_signal},
    "f16vt_f16_realized_volatility_term_structure_madmed_21d_base_v114_signal": {"inputs": ["close"], "func": f16vt_f16_realized_volatility_term_structure_madmed_21d_base_v114_signal},
    "f16vt_f16_realized_volatility_term_structure_bigmove_3sigma_42d_base_v115_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_bigmove_3sigma_42d_base_v115_signal},
    "f16vt_f16_realized_volatility_term_structure_termGini_base_v116_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_termGini_base_v116_signal},
    "f16vt_f16_realized_volatility_term_structure_volgap_pct_5_252_base_v117_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_volgap_pct_5_252_base_v117_signal},
    "f16vt_f16_realized_volatility_term_structure_vovslope_base_v118_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_vovslope_base_v118_signal},
    "f16vt_f16_realized_volatility_term_structure_voldiragree_base_v119_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_voldiragree_base_v119_signal},
    "f16vt_f16_realized_volatility_term_structure_curvesmooth_base_v120_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_curvesmooth_base_v120_signal},
    "f16vt_f16_realized_volatility_term_structure_volxover_60d_base_v121_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_volxover_60d_base_v121_signal},
    "f16vt_f16_realized_volatility_term_structure_argmaxhorizon_base_v122_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_argmaxhorizon_base_v122_signal},
    "f16vt_f16_realized_volatility_term_structure_sumr2_21on63_base_v123_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_sumr2_21on63_base_v123_signal},
    "f16vt_f16_realized_volatility_term_structure_volhalflife_base_v124_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_volhalflife_base_v124_signal},
    "f16vt_f16_realized_volatility_term_structure_volmeanshift_base_v125_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_volmeanshift_base_v125_signal},
    "f16vt_f16_realized_volatility_term_structure_vol2derivpct_base_v126_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_vol2derivpct_base_v126_signal},
    "f16vt_f16_realized_volatility_term_structure_volrank_diff_5_21_base_v127_signal": {"inputs": ["close"], "func": f16vt_f16_realized_volatility_term_structure_volrank_diff_5_21_base_v127_signal},
    "f16vt_f16_realized_volatility_term_structure_signedvol_21d_base_v128_signal": {"inputs": ["close"], "func": f16vt_f16_realized_volatility_term_structure_signedvol_21d_base_v128_signal},
    "f16vt_f16_realized_volatility_term_structure_ewma_termratio_base_v129_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_ewma_termratio_base_v129_signal},
    "f16vt_f16_realized_volatility_term_structure_volcorr_5_63_base_v130_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_volcorr_5_63_base_v130_signal},
    "f16vt_f16_realized_volatility_term_structure_bvrv_diff_21_63_base_v131_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_bvrv_diff_21_63_base_v131_signal},
    "f16vt_f16_realized_volatility_term_structure_tailasym_42d_base_v132_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_tailasym_42d_base_v132_signal},
    "f16vt_f16_realized_volatility_term_structure_hlrange_63d_base_v134_signal": {"inputs": ["high", "low", "closeadj"], "func": f16vt_f16_realized_volatility_term_structure_hlrange_63d_base_v134_signal},
    "f16vt_f16_realized_volatility_term_structure_hlrange_zscore_base_v135_signal": {"inputs": ["high", "low", "closeadj"], "func": f16vt_f16_realized_volatility_term_structure_hlrange_zscore_base_v135_signal},
    "f16vt_f16_realized_volatility_term_structure_volaccelsign_base_v136_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_volaccelsign_base_v136_signal},
    "f16vt_f16_realized_volatility_term_structure_skewratio_21_63_base_v137_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_skewratio_21_63_base_v137_signal},
    "f16vt_f16_realized_volatility_term_structure_kurtdiff_21_63_base_v138_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_kurtdiff_21_63_base_v138_signal},
    "f16vt_f16_realized_volatility_term_structure_q9diff_21_63_base_v139_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_q9diff_21_63_base_v139_signal},
    "f16vt_f16_realized_volatility_term_structure_tanh_volvar_42d_base_v140_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_tanh_volvar_42d_base_v140_signal},
    "f16vt_f16_realized_volatility_term_structure_arctanslope_base_v141_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_arctanslope_base_v141_signal},
    "f16vt_f16_realized_volatility_term_structure_ddvolasym_42d_base_v142_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_ddvolasym_42d_base_v142_signal},
    "f16vt_f16_realized_volatility_term_structure_volsignstreak_base_v143_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_volsignstreak_base_v143_signal},
    "f16vt_f16_realized_volatility_term_structure_regimecombo_base_v144_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_regimecombo_base_v144_signal},
    "f16vt_f16_realized_volatility_term_structure_curvslopediff_base_v145_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_curvslopediff_base_v145_signal},
    "f16vt_f16_realized_volatility_term_structure_arctan_volpersist_base_v146_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_arctan_volpersist_base_v146_signal},
    "f16vt_f16_realized_volatility_term_structure_tailcount_60d_base_v147_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_tailcount_60d_base_v147_signal},
    "f16vt_f16_realized_volatility_term_structure_roughratio_30_120_base_v148_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_roughratio_30_120_base_v148_signal},
    "f16vt_f16_realized_volatility_term_structure_volltrend_60d_base_v149_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_volltrend_60d_base_v149_signal},
    "f16vt_f16_realized_volatility_term_structure_volstickyabove_base_v150_signal": {"inputs": ["closeadj"], "func": f16vt_f16_realized_volatility_term_structure_volstickyabove_base_v150_signal},
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
    for name, entry in f16_realized_volatility_term_structure_base_076_150_REGISTRY.items():
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
