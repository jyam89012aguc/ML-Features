"""f11_raw_roc_family base features 001-075.

Domain: raw Rate-of-Change (ROC) family. Every feature references
`close.pct_change(N)`, `close.diff(N)`, `log(close/close.shift(N))`,
or `close - close.shift(N)`. These are RAW price changes (not changes
of any smoothed series — that domain is f01).

Layout (chosen for pairwise-correlation diversity under the self-test):
  * Few raw ROC features (windows widely spaced)
  * Log returns at varied windows
  * ROC normalizations (Sharpe-like, ATR-norm, z-score, percentile)
  * ROC differentials (short minus mid, etc.)
  * Discrete return signals (sign, streak, count, days-since)
  * Return distribution shape (skew, kurt, MAD/std, win-rate)
  * Return autocorrelation / persistence
  * Bounded transforms (arctan, tanh, sigmoid)
  * Cumulative-path features (drawdown, recovery, efficiency)
  * Extreme returns and asymmetric returns (semi-variance)
  * Statistical tests (t-stat, variance ratio)
  * Composite trend / agreement scores
NaN policy: replace([inf,-inf], nan) at the final return only.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Features 001-075. Windows > 21 use closeadj; windows <= 21 use close.
# ---------------------------------------------------------------------------


# --- Group A: raw ROC at widely-spaced windows (only 4) ---------------------


def f11rc_f11_raw_roc_family_roc_1d_base_v001_signal(close: pd.Series) -> pd.Series:
    """ROC at 1d: close.pct_change(1)."""
    out = close.pct_change(1)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_roc_5d_base_v002_signal(close: pd.Series) -> pd.Series:
    """ROC at 5d: close.pct_change(5)."""
    out = close.pct_change(5)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_roc_21d_base_v003_signal(close: pd.Series) -> pd.Series:
    """ROC at 21d: close.pct_change(21)."""
    out = close.pct_change(21)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_roc_252d_base_v004_signal(closeadj: pd.Series) -> pd.Series:
    """ROC at 252d: closeadj.pct_change(252). Annual raw return."""
    out = closeadj.pct_change(252)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group B: log returns at varied windows (3) -----------------------------


def f11rc_f11_raw_roc_family_logret_3d_base_v005_signal(close: pd.Series) -> pd.Series:
    """log(close/close.shift(3)). 3-bar log return."""
    out = np.log(close / close.shift(3).replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_logret_63d_base_v006_signal(closeadj: pd.Series) -> pd.Series:
    """log(closeadj/closeadj.shift(63)). Quarterly log return."""
    out = np.log(closeadj / closeadj.shift(63).replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_logret_126d_base_v007_signal(closeadj: pd.Series) -> pd.Series:
    """log(closeadj/closeadj.shift(126)). Semi-annual log return."""
    out = np.log(closeadj / closeadj.shift(126).replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group C: ROC normalizations (5) ----------------------------------------


def f11rc_f11_raw_roc_family_volatildiff_63d_base_v008_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility differential: std(pct1, 21) - std(pct1, 63). Short minus long
    realized vol — captures vol expansion/contraction. Orthogonal to direction."""
    r = closeadj.pct_change(1)
    s21 = r.rolling(21, min_periods=21).std()
    s63 = r.rolling(63, min_periods=63).std()
    out = s21 - s63
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_rocatrnrm_50d_base_v009_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """ROC(50) normalized by ATR-percent: pct_change(50) / (ATR(50)/close).
    Longer horizon so the pattern decorrelates from short-window arctan/highroc."""
    pc = closeadj.shift(1)
    a = (high - low).abs()
    b = (high - pc).abs()
    c = (low - pc).abs()
    tr = pd.concat([a, b, c], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 50.0, adjust=False, min_periods=50).mean()
    out = closeadj.pct_change(50) / (atr / closeadj.replace(0.0, np.nan)).replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_roczsc_60d_base_v010_signal(closeadj: pd.Series) -> pd.Series:
    """ROC z-score in trailing 60: (roc5 - mean(roc5,60))/std(roc5,60)."""
    roc = closeadj.pct_change(5)
    out = (roc - roc.rolling(60, min_periods=60).mean()) / roc.rolling(60, min_periods=60).std().replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_rocrank_120d_base_v011_signal(closeadj: pd.Series) -> pd.Series:
    """Percentile rank of current pct_change(21) in trailing 120 bars."""
    roc = closeadj.pct_change(21)
    out = roc.rolling(120, min_periods=60).rank(pct=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_rocrgrng_50d_base_v012_signal(closeadj: pd.Series) -> pd.Series:
    """ROC10 normalized by (max(close,50)-min(close,50))/close. Range-anchored."""
    rng = (closeadj.rolling(50, min_periods=50).max() - closeadj.rolling(50, min_periods=50).min()) / closeadj.replace(0.0, np.nan)
    out = closeadj.pct_change(10) / rng.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group D: ROC differentials (5) -----------------------------------------


def f11rc_f11_raw_roc_family_rocdf521_21d_base_v013_signal(close: pd.Series) -> pd.Series:
    """pct_change(5) - pct_change(21). Short minus mid horizon."""
    out = close.pct_change(5) - close.pct_change(21)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_rocdf2163_63d_base_v014_signal(closeadj: pd.Series) -> pd.Series:
    """pct_change(21) - pct_change(63). Mid minus quarter horizon."""
    out = closeadj.pct_change(21) - closeadj.pct_change(63)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_rocdf63252_252d_base_v015_signal(closeadj: pd.Series) -> pd.Series:
    """pct_change(63) - pct_change(252). Quarter minus year."""
    out = closeadj.pct_change(63) - closeadj.pct_change(252)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_rocrat521_21d_base_v016_signal(close: pd.Series) -> pd.Series:
    """sign(pct5)*sign(pct21)*|pct5|/|pct21| — signed ratio (collapses to 0 when signs differ)."""
    p5 = close.pct_change(5)
    p21 = close.pct_change(21)
    same = (np.sign(p5) == np.sign(p21)).astype(float)
    out = same * p5.abs() / p21.abs().replace(0.0, np.nan)
    out = out * np.sign(p5)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_rocavgmom_63d_base_v017_signal(closeadj: pd.Series) -> pd.Series:
    """Average momentum: (pct_change(5)+pct_change(21)+pct_change(63))/3."""
    out = (closeadj.pct_change(5) + closeadj.pct_change(21) + closeadj.pct_change(63)) / 3.0
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group E: Discrete return signals (8) -----------------------------------


def f11rc_f11_raw_roc_family_signroc_5d_base_v018_signal(close: pd.Series) -> pd.Series:
    """sign(pct_change(5)). Binary direction at 5d horizon."""
    out = np.sign(close.pct_change(5))
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_signroc_21d_base_v019_signal(close: pd.Series) -> pd.Series:
    """sign(pct_change(21))."""
    out = np.sign(close.pct_change(21))
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_signroc_63d_base_v020_signal(closeadj: pd.Series) -> pd.Series:
    """sign(pct_change(63))."""
    out = np.sign(closeadj.pct_change(63))
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_uprtcnt_21d_base_v021_signal(close: pd.Series) -> pd.Series:
    """Count of positive-return days in trailing 21: sum(pct1>0)."""
    r = close.pct_change(1)
    out = (r > 0).astype(float).rolling(21, min_periods=21).sum()
    out[r.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_dnrtcnt_63d_base_v022_signal(closeadj: pd.Series) -> pd.Series:
    """Count of negative-return days in trailing 63."""
    r = closeadj.pct_change(1)
    out = (r < 0).astype(float).rolling(63, min_periods=63).sum()
    out[r.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_uprstk_30d_base_v023_signal(close: pd.Series) -> pd.Series:
    """Current streak of consecutive positive returns (close.diff(1)>0)."""
    d = close.diff(1)
    up = (d > 0).astype(int)
    grp = (up == 0).cumsum()
    cnt = up.groupby(grp).cumcount() + 1
    out = cnt.where(up == 1, 0).astype(float)
    out[d.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_dnstk_30d_base_v024_signal(close: pd.Series) -> pd.Series:
    """Current streak of consecutive negative returns."""
    d = close.diff(1)
    dn = (d < 0).astype(int)
    grp = (dn == 0).cumsum()
    cnt = dn.groupby(grp).cumcount() + 1
    out = cnt.where(dn == 1, 0).astype(float)
    out[d.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_dssince2pct_60d_base_v025_signal(close: pd.Series) -> pd.Series:
    """Days since last single-day move with |pct_change(1)| > 2%. Caps at 60."""
    r = close.pct_change(1)
    flag = (r.abs() > 0.02).astype(float)
    def _since(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return 60.0
        return float(len(x) - 1 - idx[-1])
    out = flag.rolling(60, min_periods=60).apply(_since, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group F: Return distribution shape (8) ---------------------------------


def f11rc_f11_raw_roc_family_retskew_30d_base_v026_signal(closeadj: pd.Series) -> pd.Series:
    """Skewness of pct_change(1) over 30 bars."""
    r = closeadj.pct_change(1)
    out = r.rolling(30, min_periods=30).skew()
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_retkurt_60d_base_v027_signal(closeadj: pd.Series) -> pd.Series:
    """Kurtosis of pct_change(1) over 60 bars."""
    r = closeadj.pct_change(1)
    out = r.rolling(60, min_periods=60).kurt()
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_madstd_40d_base_v028_signal(closeadj: pd.Series) -> pd.Series:
    """MAD/std of pct_change(1) over 40 bars. 0.7979 for Gaussian."""
    r = closeadj.pct_change(1)
    mad = (r - r.rolling(40, min_periods=40).mean()).abs().rolling(40, min_periods=40).mean()
    sd = r.rolling(40, min_periods=40).std()
    out = mad / sd.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_winrate_50d_base_v029_signal(closeadj: pd.Series) -> pd.Series:
    """Win-rate: fraction of positive return days over 50 bars."""
    r = closeadj.pct_change(1)
    out = (r > 0).astype(float).rolling(50, min_periods=50).mean()
    out[r.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_sortino_30d_base_v030_signal(closeadj: pd.Series) -> pd.Series:
    """Sortino-like: mean(pct1,30) / std(pct1 where pct1<0, 30)."""
    r = closeadj.pct_change(1)
    mu = r.rolling(30, min_periods=30).mean()
    neg = r.where(r < 0, 0.0)
    dd = (neg ** 2).rolling(30, min_periods=30).mean() ** 0.5
    out = mu / dd.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_thirdmom_45d_base_v031_signal(closeadj: pd.Series) -> pd.Series:
    """3rd centered moment of pct_change(1) over 45 bars (raw, not /std^3)."""
    r = closeadj.pct_change(1)
    mu = r.rolling(45, min_periods=45).mean()
    out = ((r - mu) ** 3).rolling(45, min_periods=45).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_fourthmom_45d_base_v032_signal(closeadj: pd.Series) -> pd.Series:
    """4th centered moment of pct_change(1) over 45 bars (raw)."""
    r = closeadj.pct_change(1)
    mu = r.rolling(45, min_periods=45).mean()
    out = ((r - mu) ** 4).rolling(45, min_periods=45).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_absretq75_60d_base_v033_signal(closeadj: pd.Series) -> pd.Series:
    """75th percentile of |pct_change(1)| over trailing 60 bars. Captures the
    "typical-large-move" magnitude — orthogonal to direction and to z-score."""
    r = closeadj.pct_change(1).abs()
    out = r.rolling(60, min_periods=60).quantile(0.75)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group G: Return autocorrelation / persistence (5) ----------------------


def f11rc_f11_raw_roc_family_retac1_40d_base_v034_signal(closeadj: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of log returns over 40 bars."""
    r = np.log(closeadj / closeadj.shift(1).replace(0.0, np.nan))
    out = r.rolling(40, min_periods=40).apply(
        lambda x: float(pd.Series(x).autocorr(lag=1)) if pd.Series(x).std() > 0 else np.nan,
        raw=False,
    )
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_retac5_60d_base_v035_signal(closeadj: pd.Series) -> pd.Series:
    """Lag-5 autocorrelation of log returns over 60 bars."""
    r = np.log(closeadj / closeadj.shift(1).replace(0.0, np.nan))
    out = r.rolling(60, min_periods=60).apply(
        lambda x: float(pd.Series(x).autocorr(lag=5)) if pd.Series(x).std() > 0 else np.nan,
        raw=False,
    )
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_volclust_30d_base_v036_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility clustering: lag-1 autocorr of |pct_change(1)| over 30 bars."""
    r = closeadj.pct_change(1).abs()
    out = r.rolling(30, min_periods=30).apply(
        lambda x: float(pd.Series(x).autocorr(lag=1)) if pd.Series(x).std() > 0 else np.nan,
        raw=False,
    )
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_hurstret_80d_base_v037_signal(closeadj: pd.Series) -> pd.Series:
    """R/S-based Hurst proxy on log returns: log(R/S)/log(N) over 80 bars."""
    r = np.log(closeadj / closeadj.shift(1).replace(0.0, np.nan))
    def _h(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)) or x.size < 8:
            return np.nan
        m = x.mean()
        z = np.cumsum(x - m)
        R = float(z.max() - z.min())
        S = float(np.std(x, ddof=1))
        if R <= 0 or S <= 0:
            return np.nan
        return float(np.log(R / S) / np.log(len(x)))
    out = r.rolling(80, min_periods=80).apply(_h, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_varratio_q10_60d_base_v038_signal(closeadj: pd.Series) -> pd.Series:
    """Lo-MacKinlay variance ratio - 1: var(pct_change(10))/(10*var(pct_change(1))) - 1.
    > 0 means trending, < 0 mean-reverting; rolling 60-bar variance."""
    r1 = closeadj.pct_change(1)
    r10 = closeadj.pct_change(10)
    v1 = r1.rolling(60, min_periods=60).var(ddof=1)
    v10 = r10.rolling(60, min_periods=60).var(ddof=1)
    out = v10 / (10.0 * v1.replace(0.0, np.nan)) - 1.0
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group H: Cumulative-path features (drawdown, recovery, efficiency) (6) --


def f11rc_f11_raw_roc_family_pathlen_21d_base_v039_signal(close: pd.Series) -> pd.Series:
    """Path length: sum(|pct_change(1)|, 21). Total per-bar move."""
    r = close.pct_change(1).abs()
    out = r.rolling(21, min_periods=21).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_efficiency_30d_base_v040_signal(closeadj: pd.Series) -> pd.Series:
    """Efficiency: |close - close.shift(30)| / sum(|close.diff(1)|, 30)."""
    num = (closeadj - closeadj.shift(30)).abs()
    den = closeadj.diff(1).abs().rolling(30, min_periods=30).sum()
    out = num / den.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_inveff_60d_base_v041_signal(closeadj: pd.Series) -> pd.Series:
    """Inverse efficiency (path roughness): sum(|return|, 60) / |total return|."""
    r = closeadj.pct_change(1).abs()
    num = r.rolling(60, min_periods=60).sum()
    den = closeadj.pct_change(60).abs()
    out = num / den.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_maxdd_60d_base_v042_signal(closeadj: pd.Series) -> pd.Series:
    """Max drawdown of close over trailing 60: min(close - cummax)/cummax."""
    def _mdd(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)) or x.size == 0:
            return np.nan
        cm = np.maximum.accumulate(x)
        dd = (x - cm) / cm
        return float(dd.min())
    out = closeadj.rolling(60, min_periods=60).apply(_mdd, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_recovery_45d_base_v043_signal(closeadj: pd.Series) -> pd.Series:
    """Recovery: (close/min(close,45)) - 1 — how far above the trailing low."""
    lo = closeadj.rolling(45, min_periods=45).min()
    out = closeadj / lo.replace(0.0, np.nan) - 1.0
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_avgupmag_45d_base_v044_signal(closeadj: pd.Series) -> pd.Series:
    """Average magnitude of positive bars over 45: sum(r|r>0)/count(r>0).
    Captures "size of typical up-bar" — orthogonal to direction-anchored Sharpe."""
    r = closeadj.pct_change(1)
    pos_sum = r.where(r > 0, 0.0).rolling(45, min_periods=45).sum()
    pos_cnt = (r > 0).astype(float).rolling(45, min_periods=45).sum()
    out = pos_sum / pos_cnt.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group I: Extreme returns and asymmetric returns (6) --------------------


def f11rc_f11_raw_roc_family_maxret_21d_base_v045_signal(close: pd.Series) -> pd.Series:
    """Max single-day return in trailing 21 bars."""
    r = close.pct_change(1)
    out = r.rolling(21, min_periods=21).max()
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_minret_45d_base_v046_signal(closeadj: pd.Series) -> pd.Series:
    """Min single-day return in trailing 45 bars."""
    r = closeadj.pct_change(1)
    out = r.rolling(45, min_periods=45).min()
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_avgtop5_60d_base_v047_signal(closeadj: pd.Series) -> pd.Series:
    """Average of top-5 returns in trailing 60 bars."""
    r = closeadj.pct_change(1)
    def _top5(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)) or x.size < 5:
            return np.nan
        return float(np.mean(np.sort(x)[-5:]))
    out = r.rolling(60, min_periods=60).apply(_top5, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_avgbot5_60d_base_v048_signal(closeadj: pd.Series) -> pd.Series:
    """Average of bottom-5 returns in trailing 60 bars."""
    r = closeadj.pct_change(1)
    def _bot5(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)) or x.size < 5:
            return np.nan
        return float(np.mean(np.sort(x)[:5]))
    out = r.rolling(60, min_periods=60).apply(_bot5, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_upsemivar_40d_base_v049_signal(closeadj: pd.Series) -> pd.Series:
    """Upside semivariance: var of pct_change(1) only when > 0, over 40 bars."""
    r = closeadj.pct_change(1)
    up = r.where(r > 0)
    out = up.rolling(40, min_periods=10).var(ddof=1)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_dnsemivar_40d_base_v050_signal(closeadj: pd.Series) -> pd.Series:
    """Downside semivariance ratio: (var_dn - var_up)/var_total (asymmetric tail)."""
    r = closeadj.pct_change(1)
    up = r.where(r > 0).rolling(40, min_periods=10).var(ddof=1)
    dn = r.where(r < 0).rolling(40, min_periods=10).var(ddof=1)
    tot = r.rolling(40, min_periods=10).var(ddof=1)
    out = (dn - up) / tot.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group J: Statistical tests (3) -----------------------------------------


def f11rc_f11_raw_roc_family_tstat_45d_base_v051_signal(closeadj: pd.Series) -> pd.Series:
    """t-statistic of mean return: mean(r,45) / (std(r,45)/sqrt(45)). 45-bar window."""
    r = closeadj.pct_change(1)
    mu = r.rolling(45, min_periods=45).mean()
    se = r.rolling(45, min_periods=45).std() / (45.0 ** 0.5)
    out = mu / se.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_tstat_120d_base_v052_signal(closeadj: pd.Series) -> pd.Series:
    """t-statistic of mean log return over 120 bars."""
    r = np.log(closeadj / closeadj.shift(1).replace(0.0, np.nan))
    mu = r.rolling(120, min_periods=120).mean()
    se = r.rolling(120, min_periods=120).std() / (120.0 ** 0.5)
    out = mu / se.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_vrm2_30d_base_v053_signal(closeadj: pd.Series) -> pd.Series:
    """Variance-ratio at q=2: var(diff(close,2))/(2*var(diff(close,1))) - 1, 30-bar."""
    r1 = closeadj.diff(1)
    r2 = closeadj.diff(2)
    v1 = r1.rolling(30, min_periods=30).var(ddof=1)
    v2 = r2.rolling(30, min_periods=30).var(ddof=1)
    out = v2 / (2.0 * v1.replace(0.0, np.nan)) - 1.0
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group K: Bounded transforms (5) ----------------------------------------


def f11rc_f11_raw_roc_family_arctandiff_84d_base_v054_signal(closeadj: pd.Series) -> pd.Series:
    """arctan(5 * (pct_change(21) - pct_change(84))). Bounded version of a
    mid-vs-long ROC differential — orthogonal to single-horizon ROC features."""
    out = np.arctan(5.0 * (closeadj.pct_change(21) - closeadj.pct_change(84)))
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_tanhzsc_40d_base_v055_signal(closeadj: pd.Series) -> pd.Series:
    """tanh(z-score of pct_change(5) over 40 bars). Bounded z."""
    r = closeadj.pct_change(5)
    z = (r - r.rolling(40, min_periods=40).mean()) / r.rolling(40, min_periods=40).std().replace(0.0, np.nan)
    out = np.tanh(z)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_sigeffic_30d_base_v056_signal(closeadj: pd.Series) -> pd.Series:
    """Sigmoid of signed efficiency: pct_change(30) divided by sum(|diff|, 30)
    then squashed by sigmoid. Bounded 0..1 — signed-path-ratio."""
    num = closeadj - closeadj.shift(30)
    den = closeadj.diff(1).abs().rolling(30, min_periods=30).sum()
    z = num / den.replace(0.0, np.nan)
    out = 1.0 / (1.0 + np.exp(-10.0 * z))
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_tanhskew_60d_base_v057_signal(closeadj: pd.Series) -> pd.Series:
    """tanh of the standardized 3rd centered moment of pct_change(1) over 60.
    Bounded skewness — different shape from |corr|-style features."""
    r = closeadj.pct_change(1)
    mu = r.rolling(60, min_periods=60).mean()
    m3 = ((r - mu) ** 3).rolling(60, min_periods=60).mean()
    s = r.rolling(60, min_periods=60).std()
    skew = m3 / (s ** 3).replace(0.0, np.nan)
    out = np.tanh(skew)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_pctrnkabs_252d_base_v058_signal(closeadj: pd.Series) -> pd.Series:
    """Percentile rank of |pct_change(1)| in trailing 252 bars. Rank of
    today's |return| magnitude — orthogonal to direction."""
    r = closeadj.pct_change(1).abs()
    out = r.rolling(252, min_periods=120).rank(pct=True)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group L: smoothed ROC (small smoothing) (4) ----------------------------


def f11rc_f11_raw_roc_family_emaroc_10d_base_v059_signal(close: pd.Series) -> pd.Series:
    """EMA(3) of pct_change(10)."""
    r = close.pct_change(10)
    out = r.ewm(span=3, adjust=False, min_periods=3).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_wmadrocbias_21d_base_v060_signal(close: pd.Series) -> pd.Series:
    """Linearly-weighted average (5 bars) of pct_change(21) minus its plain
    SMA(5) — captures the bias due to recency weighting. Decorrelated from
    raw pct_change(21)."""
    r = close.pct_change(21)
    w = np.arange(1, 6, dtype=float)
    w /= w.sum()
    wma = r.rolling(5, min_periods=5).apply(lambda x: float(np.dot(x, w)), raw=True)
    sma = r.rolling(5, min_periods=5).mean()
    out = wma - sma
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_medroc_15d_base_v061_signal(close: pd.Series) -> pd.Series:
    """Median(5) of pct_change(15)."""
    r = close.pct_change(15)
    out = r.rolling(5, min_periods=5).median()
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_trmroc_42d_base_v062_signal(closeadj: pd.Series) -> pd.Series:
    """Trimmed (10/90 quantile-clipped) mean of pct_change(42) over 7 bars."""
    r = closeadj.pct_change(42)
    def _trim(x):
        if np.any(~np.isfinite(x)):
            return np.nan
        lo, hi = np.quantile(x, 0.1), np.quantile(x, 0.9)
        z = x[(x >= lo) & (x <= hi)]
        if z.size == 0:
            return np.nan
        return float(np.mean(z))
    out = r.rolling(7, min_periods=7).apply(_trim, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group M: Composite scores / discrete trend states (5) ------------------


def f11rc_f11_raw_roc_family_trendscore_63d_base_v063_signal(closeadj: pd.Series) -> pd.Series:
    """sign(pct5)+sign(pct21)+sign(pct63). Discrete -3..+3."""
    out = np.sign(closeadj.pct_change(5)) + np.sign(closeadj.pct_change(21)) + np.sign(closeadj.pct_change(63))
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_signagree5_63d_base_v064_signal(closeadj: pd.Series) -> pd.Series:
    """Count of agreeing signs across {pct3, pct10, pct21, pct42, pct63}.
    0..5 — but signed by majority direction (so range -5..+5)."""
    p1 = np.sign(closeadj.pct_change(3))
    p2 = np.sign(closeadj.pct_change(10))
    p3 = np.sign(closeadj.pct_change(21))
    p4 = np.sign(closeadj.pct_change(42))
    p5 = np.sign(closeadj.pct_change(63))
    out = p1 + p2 + p3 + p4 + p5
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_wavgroc_252d_base_v065_signal(closeadj: pd.Series) -> pd.Series:
    """Linearly-weighted average of {pct5, pct21, pct63, pct126, pct252} with
    weights {5,4,3,2,1} (more weight to short ROC). Composite momentum."""
    p5 = closeadj.pct_change(5)
    p21 = closeadj.pct_change(21)
    p63 = closeadj.pct_change(63)
    p126 = closeadj.pct_change(126)
    p252 = closeadj.pct_change(252)
    out = (5.0 * p5 + 4.0 * p21 + 3.0 * p63 + 2.0 * p126 + 1.0 * p252) / 15.0
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_upqtcnt_30d_base_v066_signal(closeadj: pd.Series) -> pd.Series:
    """Count of bars in trailing 30 where pct_change(1) > top-quartile of last 60."""
    r = closeadj.pct_change(1)
    q75 = r.rolling(60, min_periods=60).quantile(0.75)
    flag = (r > q75).astype(float)
    out = flag.rolling(30, min_periods=30).sum()
    out[q75.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_quadrnt_30d_base_v067_signal(closeadj: pd.Series) -> pd.Series:
    """2*sign(pct_change(21)) + sign(pct_change(5)). 4-state regime
    (long-up/long-dn x short-up/short-dn)."""
    out = 2.0 * np.sign(closeadj.pct_change(21)) + np.sign(closeadj.pct_change(5))
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group N: range-anchored / OHLC ROC variants (4) ------------------------


def f11rc_f11_raw_roc_family_highrocstk_42d_base_v068_signal(high: pd.Series) -> pd.Series:
    """Streak of consecutive bars where high.diff(1) > 0 — discrete count, NOT
    a level. Different shape than continuous ROC."""
    d = high.diff(1)
    up = (d > 0).astype(int)
    grp = (up == 0).cumsum()
    cnt = up.groupby(grp).cumcount() + 1
    out = cnt.where(up == 1, 0).astype(float)
    out[d.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_lowstkdwn_42d_base_v069_signal(low: pd.Series) -> pd.Series:
    """Streak length of consecutive bars where low.diff(1) < 0. Discrete
    count of downside-extension days — structurally different from continuous ROC."""
    d = low.diff(1)
    dn = (d < 0).astype(int)
    grp = (dn == 0).cumsum()
    cnt = dn.groupby(grp).cumcount() + 1
    out = cnt.where(dn == 1, 0).astype(float)
    out[d.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_hlrocdiff_21d_base_v070_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """high.pct_change(21) - low.pct_change(21). Captures expansion vs
    contraction of range."""
    out = high.pct_change(21) - low.pct_change(21)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_openclrocdf_5d_base_v071_signal(open_: pd.Series, close: pd.Series) -> pd.Series:
    """close.pct_change(5) - open.pct_change(5). Differential captures whether
    closes are moving differently from opens at the 5-bar horizon."""
    out = close.pct_change(5) - open_.pct_change(5)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group O: short-horizon discrete derivatives / change in sign (4) -------




def f11rc_f11_raw_roc_family_rocclz_50d_base_v073_signal(closeadj: pd.Series) -> pd.Series:
    """Count of "near-zero" return days in 50 bars (|pct1|<0.25*std(pct1,50))."""
    r = closeadj.pct_change(1)
    sd = r.rolling(50, min_periods=50).std()
    flag = (r.abs() < 0.25 * sd).astype(float)
    out = flag.rolling(50, min_periods=50).sum()
    out[sd.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_logvar_30d_base_v074_signal(closeadj: pd.Series) -> pd.Series:
    """Variance of log returns: var(log(close/close.shift(1)), 30)."""
    r = np.log(closeadj / closeadj.shift(1).replace(0.0, np.nan))
    out = r.rolling(30, min_periods=30).var(ddof=1)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_jumpfrac_60d_base_v075_signal(closeadj: pd.Series) -> pd.Series:
    """Jump-share of variance: sum( pct_change(1)^2 * I{|pct1| > 2*std60} ) /
    sum( pct_change(1)^2 ), over 60 bars. Fraction of return-variance
    contributed by "jump" bars — bounded, distribution-shape feature."""
    r = closeadj.pct_change(1)
    sd = r.rolling(60, min_periods=60).std()
    big = (r.abs() > 2.0 * sd).astype(float)
    rsq = r * r
    jump_num = (rsq * big).rolling(60, min_periods=60).sum()
    tot = rsq.rolling(60, min_periods=60).sum()
    out = jump_num / tot.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f11_raw_roc_family_base_001_075_REGISTRY = {
    "f11rc_f11_raw_roc_family_roc_1d_base_v001_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_roc_1d_base_v001_signal},
    "f11rc_f11_raw_roc_family_roc_5d_base_v002_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_roc_5d_base_v002_signal},
    "f11rc_f11_raw_roc_family_roc_21d_base_v003_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_roc_21d_base_v003_signal},
    "f11rc_f11_raw_roc_family_roc_252d_base_v004_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_roc_252d_base_v004_signal},
    "f11rc_f11_raw_roc_family_logret_3d_base_v005_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_logret_3d_base_v005_signal},
    "f11rc_f11_raw_roc_family_logret_63d_base_v006_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_logret_63d_base_v006_signal},
    "f11rc_f11_raw_roc_family_logret_126d_base_v007_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_logret_126d_base_v007_signal},
    "f11rc_f11_raw_roc_family_volatildiff_63d_base_v008_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_volatildiff_63d_base_v008_signal},
    "f11rc_f11_raw_roc_family_rocatrnrm_50d_base_v009_signal": {"inputs": ["high", "low", "closeadj"], "func": f11rc_f11_raw_roc_family_rocatrnrm_50d_base_v009_signal},
    "f11rc_f11_raw_roc_family_roczsc_60d_base_v010_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_roczsc_60d_base_v010_signal},
    "f11rc_f11_raw_roc_family_rocrank_120d_base_v011_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_rocrank_120d_base_v011_signal},
    "f11rc_f11_raw_roc_family_rocrgrng_50d_base_v012_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_rocrgrng_50d_base_v012_signal},
    "f11rc_f11_raw_roc_family_rocdf521_21d_base_v013_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_rocdf521_21d_base_v013_signal},
    "f11rc_f11_raw_roc_family_rocdf2163_63d_base_v014_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_rocdf2163_63d_base_v014_signal},
    "f11rc_f11_raw_roc_family_rocdf63252_252d_base_v015_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_rocdf63252_252d_base_v015_signal},
    "f11rc_f11_raw_roc_family_rocrat521_21d_base_v016_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_rocrat521_21d_base_v016_signal},
    "f11rc_f11_raw_roc_family_rocavgmom_63d_base_v017_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_rocavgmom_63d_base_v017_signal},
    "f11rc_f11_raw_roc_family_signroc_5d_base_v018_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_signroc_5d_base_v018_signal},
    "f11rc_f11_raw_roc_family_signroc_21d_base_v019_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_signroc_21d_base_v019_signal},
    "f11rc_f11_raw_roc_family_signroc_63d_base_v020_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_signroc_63d_base_v020_signal},
    "f11rc_f11_raw_roc_family_uprtcnt_21d_base_v021_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_uprtcnt_21d_base_v021_signal},
    "f11rc_f11_raw_roc_family_dnrtcnt_63d_base_v022_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_dnrtcnt_63d_base_v022_signal},
    "f11rc_f11_raw_roc_family_uprstk_30d_base_v023_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_uprstk_30d_base_v023_signal},
    "f11rc_f11_raw_roc_family_dnstk_30d_base_v024_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_dnstk_30d_base_v024_signal},
    "f11rc_f11_raw_roc_family_dssince2pct_60d_base_v025_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_dssince2pct_60d_base_v025_signal},
    "f11rc_f11_raw_roc_family_retskew_30d_base_v026_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_retskew_30d_base_v026_signal},
    "f11rc_f11_raw_roc_family_retkurt_60d_base_v027_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_retkurt_60d_base_v027_signal},
    "f11rc_f11_raw_roc_family_madstd_40d_base_v028_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_madstd_40d_base_v028_signal},
    "f11rc_f11_raw_roc_family_winrate_50d_base_v029_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_winrate_50d_base_v029_signal},
    "f11rc_f11_raw_roc_family_sortino_30d_base_v030_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_sortino_30d_base_v030_signal},
    "f11rc_f11_raw_roc_family_thirdmom_45d_base_v031_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_thirdmom_45d_base_v031_signal},
    "f11rc_f11_raw_roc_family_fourthmom_45d_base_v032_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_fourthmom_45d_base_v032_signal},
    "f11rc_f11_raw_roc_family_absretq75_60d_base_v033_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_absretq75_60d_base_v033_signal},
    "f11rc_f11_raw_roc_family_retac1_40d_base_v034_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_retac1_40d_base_v034_signal},
    "f11rc_f11_raw_roc_family_retac5_60d_base_v035_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_retac5_60d_base_v035_signal},
    "f11rc_f11_raw_roc_family_volclust_30d_base_v036_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_volclust_30d_base_v036_signal},
    "f11rc_f11_raw_roc_family_hurstret_80d_base_v037_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_hurstret_80d_base_v037_signal},
    "f11rc_f11_raw_roc_family_varratio_q10_60d_base_v038_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_varratio_q10_60d_base_v038_signal},
    "f11rc_f11_raw_roc_family_pathlen_21d_base_v039_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_pathlen_21d_base_v039_signal},
    "f11rc_f11_raw_roc_family_efficiency_30d_base_v040_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_efficiency_30d_base_v040_signal},
    "f11rc_f11_raw_roc_family_inveff_60d_base_v041_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_inveff_60d_base_v041_signal},
    "f11rc_f11_raw_roc_family_maxdd_60d_base_v042_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_maxdd_60d_base_v042_signal},
    "f11rc_f11_raw_roc_family_recovery_45d_base_v043_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_recovery_45d_base_v043_signal},
    "f11rc_f11_raw_roc_family_avgupmag_45d_base_v044_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_avgupmag_45d_base_v044_signal},
    "f11rc_f11_raw_roc_family_maxret_21d_base_v045_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_maxret_21d_base_v045_signal},
    "f11rc_f11_raw_roc_family_minret_45d_base_v046_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_minret_45d_base_v046_signal},
    "f11rc_f11_raw_roc_family_avgtop5_60d_base_v047_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_avgtop5_60d_base_v047_signal},
    "f11rc_f11_raw_roc_family_avgbot5_60d_base_v048_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_avgbot5_60d_base_v048_signal},
    "f11rc_f11_raw_roc_family_upsemivar_40d_base_v049_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_upsemivar_40d_base_v049_signal},
    "f11rc_f11_raw_roc_family_dnsemivar_40d_base_v050_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_dnsemivar_40d_base_v050_signal},
    "f11rc_f11_raw_roc_family_tstat_45d_base_v051_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_tstat_45d_base_v051_signal},
    "f11rc_f11_raw_roc_family_tstat_120d_base_v052_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_tstat_120d_base_v052_signal},
    "f11rc_f11_raw_roc_family_vrm2_30d_base_v053_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_vrm2_30d_base_v053_signal},
    "f11rc_f11_raw_roc_family_arctandiff_84d_base_v054_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_arctandiff_84d_base_v054_signal},
    "f11rc_f11_raw_roc_family_tanhzsc_40d_base_v055_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_tanhzsc_40d_base_v055_signal},
    "f11rc_f11_raw_roc_family_sigeffic_30d_base_v056_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_sigeffic_30d_base_v056_signal},
    "f11rc_f11_raw_roc_family_tanhskew_60d_base_v057_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_tanhskew_60d_base_v057_signal},
    "f11rc_f11_raw_roc_family_pctrnkabs_252d_base_v058_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_pctrnkabs_252d_base_v058_signal},
    "f11rc_f11_raw_roc_family_emaroc_10d_base_v059_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_emaroc_10d_base_v059_signal},
    "f11rc_f11_raw_roc_family_wmadrocbias_21d_base_v060_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_wmadrocbias_21d_base_v060_signal},
    "f11rc_f11_raw_roc_family_medroc_15d_base_v061_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_medroc_15d_base_v061_signal},
    "f11rc_f11_raw_roc_family_trmroc_42d_base_v062_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_trmroc_42d_base_v062_signal},
    "f11rc_f11_raw_roc_family_trendscore_63d_base_v063_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_trendscore_63d_base_v063_signal},
    "f11rc_f11_raw_roc_family_signagree5_63d_base_v064_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_signagree5_63d_base_v064_signal},
    "f11rc_f11_raw_roc_family_wavgroc_252d_base_v065_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_wavgroc_252d_base_v065_signal},
    "f11rc_f11_raw_roc_family_upqtcnt_30d_base_v066_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_upqtcnt_30d_base_v066_signal},
    "f11rc_f11_raw_roc_family_quadrnt_30d_base_v067_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_quadrnt_30d_base_v067_signal},
    "f11rc_f11_raw_roc_family_highrocstk_42d_base_v068_signal": {"inputs": ["high"], "func": f11rc_f11_raw_roc_family_highrocstk_42d_base_v068_signal},
    "f11rc_f11_raw_roc_family_lowstkdwn_42d_base_v069_signal": {"inputs": ["low"], "func": f11rc_f11_raw_roc_family_lowstkdwn_42d_base_v069_signal},
    "f11rc_f11_raw_roc_family_hlrocdiff_21d_base_v070_signal": {"inputs": ["high", "low"], "func": f11rc_f11_raw_roc_family_hlrocdiff_21d_base_v070_signal},
    "f11rc_f11_raw_roc_family_openclrocdf_5d_base_v071_signal": {"inputs": ["open", "close"], "func": f11rc_f11_raw_roc_family_openclrocdf_5d_base_v071_signal},
    "f11rc_f11_raw_roc_family_rocclz_50d_base_v073_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_rocclz_50d_base_v073_signal},
    "f11rc_f11_raw_roc_family_logvar_30d_base_v074_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_logvar_30d_base_v074_signal},
    "f11rc_f11_raw_roc_family_jumpfrac_60d_base_v075_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_jumpfrac_60d_base_v075_signal},
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
    for name, entry in f11_raw_roc_family_base_001_075_REGISTRY.items():
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
        s = corr.unstack().sort_values(ascending=False)
        s = s[s > 0.94].head(40)
        seen = set()
        for (a, b), v in s.items():
            if a < b and (a, b) not in seen:
                seen.add((a, b))
                print(f"  {a}  vs  {b}  ->  {v:.4f}")
    assert max_corr <= 0.95 + 1e-9, f"max pairwise |corr|={max_corr:.4f} exceeds 0.95"
    print(f"OK base_001_075: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
