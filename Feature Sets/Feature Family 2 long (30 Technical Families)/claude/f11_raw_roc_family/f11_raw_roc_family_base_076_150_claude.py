"""f11_raw_roc_family base features 076-150.

Continuation of the raw Rate-of-Change family. Every feature references
`close.pct_change(N)`, `close.diff(N)`, `log(close/close.shift(N))`,
or `close - close.shift(N)`. Structurally distinct from base 001-075:
new horizons, new transforms, new aggregates, but no duplicates with
file 1 up to a window swap.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Features 076-150
# ---------------------------------------------------------------------------


# --- short-window pure ROC variants (3) -------------------------------------


def f11rc_f11_raw_roc_family_roc_2d_base_v076_signal(close: pd.Series) -> pd.Series:
    """close.pct_change(2). 2-bar ROC — distinct horizon from file 1."""
    out = close.pct_change(2)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_roc_10d_base_v077_signal(close: pd.Series) -> pd.Series:
    """close.pct_change(10). 10-bar ROC."""
    out = close.pct_change(10)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_logret_42d_base_v078_signal(closeadj: pd.Series) -> pd.Series:
    """log(close/close.shift(42))."""
    out = np.log(closeadj / closeadj.shift(42).replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


# --- alternate ROC normalizations (5) ---------------------------------------


def f11rc_f11_raw_roc_family_logretkurt_45d_base_v079_signal(closeadj: pd.Series) -> pd.Series:
    """Kurtosis of log returns over 45 — fourth-moment shape of log returns,
    structurally distinct from pct_change-based shape features."""
    r = np.log(closeadj / closeadj.shift(1).replace(0.0, np.nan))
    out = r.rolling(45, min_periods=45).kurt()
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_rocsemi_40d_base_v080_signal(closeadj: pd.Series) -> pd.Series:
    """pct_change(40) divided by downside-std (std of pct1 when pct1<0, 40-bar)."""
    r = closeadj.pct_change(1)
    dn = r.where(r < 0)
    dnstd = dn.rolling(40, min_periods=10).std(ddof=1)
    out = closeadj.pct_change(40) / dnstd.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_updnstdratio_60d_base_v081_signal(closeadj: pd.Series) -> pd.Series:
    """upside-std / downside-std of pct1 over 60. Asymmetric-vol ratio,
    direction-agnostic — captures whether up moves are more volatile than down moves."""
    r = closeadj.pct_change(1)
    upstd = r.where(r > 0).rolling(60, min_periods=15).std(ddof=1)
    dnstd = r.where(r < 0).rolling(60, min_periods=15).std(ddof=1)
    out = upstd / dnstd.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_signsqret_30d_base_v082_signal(closeadj: pd.Series) -> pd.Series:
    """sign(pct1)*pct1^2 summed over 30: signed realized variance. Captures
    direction-weighted volatility — different shape from un-signed sums."""
    r = closeadj.pct_change(1)
    sw = np.sign(r) * (r ** 2)
    out = sw.rolling(30, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_rocsignal_30d_base_v083_signal(closeadj: pd.Series) -> pd.Series:
    """Signal-to-noise on pct_change(1): mean(pct1, 30) / (mean|pct1|, 30).
    Bounded -1..+1. Captures directional component vs total magnitude."""
    r = closeadj.pct_change(1)
    mu = r.rolling(30, min_periods=30).mean()
    am = r.abs().rolling(30, min_periods=30).mean()
    out = mu / am.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- ROC ratios / additional differentials (5) ------------------------------


def f11rc_f11_raw_roc_family_rocdf_15d_base_v084_signal(close: pd.Series) -> pd.Series:
    """pct_change(3) - pct_change(15). Very short vs short-mid ROC differential."""
    out = close.pct_change(3) - close.pct_change(15)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_rocdf_42d_base_v085_signal(closeadj: pd.Series) -> pd.Series:
    """pct_change(10) - pct_change(42)."""
    out = closeadj.pct_change(10) - closeadj.pct_change(42)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_rocdf_126d_base_v086_signal(closeadj: pd.Series) -> pd.Series:
    """pct_change(42) - pct_change(126). Mid-long differential."""
    out = closeadj.pct_change(42) - closeadj.pct_change(126)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_rocdfsign_63d_base_v087_signal(closeadj: pd.Series) -> pd.Series:
    """sign(pct21)*sign(pct63). Sign-alignment between mid and long ROC. ±1."""
    out = np.sign(closeadj.pct_change(21)) * np.sign(closeadj.pct_change(63))
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_rocdrop_63d_base_v088_signal(closeadj: pd.Series) -> pd.Series:
    """Half-life proxy: pct_change(21) - 0.5 * pct_change(63). Captures
    whether mid-term momentum is decaying relative to long-term."""
    out = closeadj.pct_change(21) - 0.5 * closeadj.pct_change(63)
    return out.replace([np.inf, -np.inf], np.nan)


# --- counts / streaks at different windows (6) ------------------------------


def f11rc_f11_raw_roc_family_uprtcnt_10d_base_v089_signal(close: pd.Series) -> pd.Series:
    """Count of positive-return days in trailing 10."""
    r = close.pct_change(1)
    out = (r > 0).astype(float).rolling(10, min_periods=10).sum()
    out[r.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_dnrtcnt_21d_base_v090_signal(close: pd.Series) -> pd.Series:
    """Count of negative-return days in trailing 21."""
    r = close.pct_change(1)
    out = (r < 0).astype(float).rolling(21, min_periods=21).sum()
    out[r.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_alterncnt_45d_base_v091_signal(closeadj: pd.Series) -> pd.Series:
    """Count of bars in trailing 45 where sign(pct1) != sign(pct1.shift(1)).
    "Alternation count" — high when chop, low when trending."""
    r = closeadj.pct_change(1)
    s = np.sign(r)
    flip = (s != s.shift(1)).astype(float)
    flip[s.isna() | s.shift(1).isna()] = 0.0
    out = flip.rolling(45, min_periods=45).sum()
    out[r.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_dssince5pct_120d_base_v092_signal(closeadj: pd.Series) -> pd.Series:
    """Days since last |pct_change(5)| > 5%. Caps at 120."""
    r = closeadj.pct_change(5).abs()
    flag = (r > 0.05).astype(float)
    def _since(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return 120.0
        return float(len(x) - 1 - idx[-1])
    out = flag.rolling(120, min_periods=120).apply(_since, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_signstreak_30d_base_v093_signal(close: pd.Series) -> pd.Series:
    """Signed streak of pct_change(1) sign: positive run-length as +, negative as -.
    Combines streak length and direction in one signal."""
    r = close.pct_change(1)
    s = np.sign(r)
    chg = (s != s.shift(1)).astype(int)
    chg[s.isna() | s.shift(1).isna()] = 0
    grp = chg.cumsum()
    cnt = s.groupby(grp).cumcount() + 1
    out = cnt.astype(float) * s
    out[r.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_bigupcnt_60d_base_v094_signal(closeadj: pd.Series) -> pd.Series:
    """Count of "big up" bars (pct1 > +1.5*std(pct1,60)) in trailing 60."""
    r = closeadj.pct_change(1)
    sd = r.rolling(60, min_periods=60).std()
    big = (r > 1.5 * sd).astype(float)
    out = big.rolling(60, min_periods=60).sum()
    out[sd.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


# --- additional distribution-shape features (5) -----------------------------


def f11rc_f11_raw_roc_family_retskew_90d_base_v095_signal(closeadj: pd.Series) -> pd.Series:
    """Skewness of pct_change(1) over 90 bars. Long-horizon shape."""
    r = closeadj.pct_change(1)
    out = r.rolling(90, min_periods=90).skew()
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_retkurt_30d_base_v096_signal(closeadj: pd.Series) -> pd.Series:
    """Kurtosis of pct_change(1) over 30 bars. Short-horizon shape."""
    r = closeadj.pct_change(1)
    out = r.rolling(30, min_periods=30).kurt()
    return out.replace([np.inf, -np.inf], np.nan)




def f11rc_f11_raw_roc_family_winratio_90d_base_v098_signal(closeadj: pd.Series) -> pd.Series:
    """Profit factor: sum(pct1>0) / |sum(pct1<0)| over 90. Longer window than
    signsqret_30 / rocsignal_30 so it does not collapse to direction."""
    r = closeadj.pct_change(1)
    pos = r.where(r > 0, 0.0).rolling(90, min_periods=90).sum()
    neg = r.where(r < 0, 0.0).rolling(90, min_periods=90).sum().abs()
    out = pos / neg.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_avgdnmag_45d_base_v099_signal(closeadj: pd.Series) -> pd.Series:
    """Average magnitude of negative bars over 45: |sum(r|r<0)|/count(r<0)."""
    r = closeadj.pct_change(1)
    neg_sum = r.where(r < 0, 0.0).rolling(45, min_periods=45).sum().abs()
    neg_cnt = (r < 0).astype(float).rolling(45, min_periods=45).sum()
    out = neg_sum / neg_cnt.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- additional autocorr / persistence (3) ----------------------------------


def f11rc_f11_raw_roc_family_retac3_50d_base_v100_signal(closeadj: pd.Series) -> pd.Series:
    """Lag-3 autocorr of pct_change(1) over 50 bars."""
    r = closeadj.pct_change(1)
    out = r.rolling(50, min_periods=50).apply(
        lambda x: float(pd.Series(x).autocorr(lag=3)) if pd.Series(x).std() > 0 else np.nan,
        raw=False,
    )
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_signac1_60d_base_v101_signal(closeadj: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of sign(pct_change(1)). Boolean-flavored persistence."""
    s = np.sign(closeadj.pct_change(1))
    out = s.rolling(60, min_periods=60).apply(
        lambda x: float(pd.Series(x).autocorr(lag=1)) if pd.Series(x).std() > 0 else np.nan,
        raw=False,
    )
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_sqrac1_45d_base_v102_signal(closeadj: pd.Series) -> pd.Series:
    """Lag-1 autocorr of (pct1)^2 over 45 — Engle-style vol-of-vol persistence."""
    r = closeadj.pct_change(1) ** 2
    out = r.rolling(45, min_periods=45).apply(
        lambda x: float(pd.Series(x).autocorr(lag=1)) if pd.Series(x).std() > 0 else np.nan,
        raw=False,
    )
    return out.replace([np.inf, -np.inf], np.nan)


# --- additional cumulative-path features (5) --------------------------------


def f11rc_f11_raw_roc_family_pathlen_60d_base_v103_signal(closeadj: pd.Series) -> pd.Series:
    """sum(|pct1|, 60). Path length at longer horizon."""
    r = closeadj.pct_change(1).abs()
    out = r.rolling(60, min_periods=60).sum()
    return out.replace([np.inf, -np.inf], np.nan)




def f11rc_f11_raw_roc_family_pathvsstd_30d_base_v105_signal(closeadj: pd.Series) -> pd.Series:
    """sum(|pct1|,30) / (std(pct1,30) * sqrt(30)). Ratio of L1 path length
    to L2-expected path; near 1 for Gaussian, deviates with shape. Bounded."""
    r = closeadj.pct_change(1)
    path = r.abs().rolling(30, min_periods=30).sum()
    sd = r.rolling(30, min_periods=30).std()
    out = path / (sd * (30.0 ** 0.5)).replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_maxdd_120d_base_v106_signal(closeadj: pd.Series) -> pd.Series:
    """Max drawdown of close in trailing 120."""
    def _mdd(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)) or x.size == 0:
            return np.nan
        cm = np.maximum.accumulate(x)
        dd = (x - cm) / cm
        return float(dd.min())
    out = closeadj.rolling(120, min_periods=120).apply(_mdd, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_drwdwn_30d_base_v107_signal(closeadj: pd.Series) -> pd.Series:
    """Current drawdown from trailing-30 max: (close - max(close,30))/max(close,30)."""
    hi = closeadj.rolling(30, min_periods=30).max()
    out = (closeadj - hi) / hi.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- additional extreme/asymmetric returns (4) ------------------------------


def f11rc_f11_raw_roc_family_topbotrng_45d_base_v108_signal(closeadj: pd.Series) -> pd.Series:
    """Max(pct1,45) - min(pct1,45). Range of per-bar returns."""
    r = closeadj.pct_change(1)
    out = r.rolling(45, min_periods=45).max() - r.rolling(45, min_periods=45).min()
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_avgtop3_30d_base_v109_signal(closeadj: pd.Series) -> pd.Series:
    """Average of top-3 returns in trailing 30 bars."""
    r = closeadj.pct_change(1)
    def _top3(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)) or x.size < 3:
            return np.nan
        return float(np.mean(np.sort(x)[-3:]))
    out = r.rolling(30, min_periods=30).apply(_top3, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_avgbot3_30d_base_v110_signal(closeadj: pd.Series) -> pd.Series:
    """Average of bottom-3 returns in trailing 30 bars."""
    r = closeadj.pct_change(1)
    def _bot3(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)) or x.size < 3:
            return np.nan
        return float(np.mean(np.sort(x)[:3]))
    out = r.rolling(30, min_periods=30).apply(_bot3, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_iqrret_60d_base_v111_signal(closeadj: pd.Series) -> pd.Series:
    """IQR of pct_change(1): Q75-Q25 over 60 bars. Robust-spread analog of std."""
    r = closeadj.pct_change(1)
    q75 = r.rolling(60, min_periods=60).quantile(0.75)
    q25 = r.rolling(60, min_periods=60).quantile(0.25)
    out = q75 - q25
    return out.replace([np.inf, -np.inf], np.nan)


# --- additional bounded transforms (5) --------------------------------------


def f11rc_f11_raw_roc_family_tanharctan_30d_base_v112_signal(closeadj: pd.Series) -> pd.Series:
    """tanh(z-score of pct_change(10) over 30). Different combination of bounded
    pipeline than tanhzsc_40d in file 1."""
    r = closeadj.pct_change(10)
    z = (r - r.rolling(30, min_periods=30).mean()) / r.rolling(30, min_periods=30).std().replace(0.0, np.nan)
    out = np.tanh(z)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_arctan_long_v113_signal(closeadj: pd.Series) -> pd.Series:
    """arctan(3*pct_change(252)). Bounded annual ROC."""
    out = np.arctan(3.0 * closeadj.pct_change(252))
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_rkdf_60d_base_v114_signal(closeadj: pd.Series) -> pd.Series:
    """Rank(pct21,120) - Rank(pct63,120) — differential rank between mid/long ROC."""
    rk21 = closeadj.pct_change(21).rolling(120, min_periods=60).rank(pct=True)
    rk63 = closeadj.pct_change(63).rolling(120, min_periods=60).rank(pct=True)
    out = rk21 - rk63
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_pctrnk21_60d_base_v115_signal(closeadj: pd.Series) -> pd.Series:
    """Percentile rank of pct_change(21) in trailing 60 (short reference window)."""
    r = closeadj.pct_change(21)
    out = r.rolling(60, min_periods=30).rank(pct=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_sigsharpe_90d_base_v116_signal(closeadj: pd.Series) -> pd.Series:
    """Sigmoid of mean/std of pct_change(1) over 90: bounded "trend significance"."""
    r = closeadj.pct_change(1)
    mu = r.rolling(90, min_periods=90).mean()
    sd = r.rolling(90, min_periods=90).std()
    z = mu / sd.replace(0.0, np.nan)
    out = 1.0 / (1.0 + np.exp(-50.0 * z))
    return out.replace([np.inf, -np.inf], np.nan)


# --- additional composite / agreement scores (4) ----------------------------


def f11rc_f11_raw_roc_family_signalign3_42d_base_v117_signal(closeadj: pd.Series) -> pd.Series:
    """sign(pct10)*sign(pct21)*sign(pct42). +1 all-aligned, -1 not. Triple-product."""
    out = np.sign(closeadj.pct_change(10)) * np.sign(closeadj.pct_change(21)) * np.sign(closeadj.pct_change(42))
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_signsum5_84d_base_v118_signal(closeadj: pd.Series) -> pd.Series:
    """sign(pct7)+sign(pct14)+sign(pct28)+sign(pct56)+sign(pct84). Discrete
    breadth -5..+5 across geometric horizons. Distinct from continuous geomavg."""
    s7 = np.sign(closeadj.pct_change(7))
    s14 = np.sign(closeadj.pct_change(14))
    s28 = np.sign(closeadj.pct_change(28))
    s56 = np.sign(closeadj.pct_change(56))
    s84 = np.sign(closeadj.pct_change(84))
    out = s7 + s14 + s28 + s56 + s84
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_minabs5_30d_base_v119_signal(close: pd.Series) -> pd.Series:
    """min(|pct1|,30) — calmest single-day return in trailing 30. Discrete-like
    bounded-from-below feature."""
    r = close.pct_change(1).abs()
    out = r.rolling(30, min_periods=30).min()
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_centmin_pct_60d_base_v120_signal(closeadj: pd.Series) -> pd.Series:
    """Number of bars in trailing 60 with |pct1|<0.5*std(pct1,60). "Calm-bar"
    fraction — discrete."""
    r = closeadj.pct_change(1)
    sd = r.rolling(60, min_periods=60).std()
    flag = (r.abs() < 0.5 * sd).astype(float)
    out = flag.rolling(60, min_periods=60).sum()
    out[sd.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


# --- additional statistical tests / variance ratios (3) ----------------------


def f11rc_f11_raw_roc_family_vrq5_60d_base_v121_signal(closeadj: pd.Series) -> pd.Series:
    """Variance-ratio at q=5: var(pct_change(5))/(5*var(pct_change(1))) - 1, 60 bar."""
    r1 = closeadj.pct_change(1)
    r5 = closeadj.pct_change(5)
    v1 = r1.rolling(60, min_periods=60).var(ddof=1)
    v5 = r5.rolling(60, min_periods=60).var(ddof=1)
    out = v5 / (5.0 * v1.replace(0.0, np.nan)) - 1.0
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_vrq20_120d_base_v122_signal(closeadj: pd.Series) -> pd.Series:
    """Variance-ratio at q=20: var(pct_change(20))/(20*var(pct_change(1))) - 1, 120 bar."""
    r1 = closeadj.pct_change(1)
    r20 = closeadj.pct_change(20)
    v1 = r1.rolling(120, min_periods=120).var(ddof=1)
    v20 = r20.rolling(120, min_periods=120).var(ddof=1)
    out = v20 / (20.0 * v1.replace(0.0, np.nan)) - 1.0
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_tstat_21d_base_v123_signal(close: pd.Series) -> pd.Series:
    """t-stat of mean(pct1,21) — shorter-window analog."""
    r = close.pct_change(1)
    mu = r.rolling(21, min_periods=21).mean()
    se = r.rolling(21, min_periods=21).std() / (21.0 ** 0.5)
    out = mu / se.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- OHLC-flavored ROC variants (4) -----------------------------------------


def f11rc_f11_raw_roc_family_clcldiff_5d_base_v124_signal(open_: pd.Series, close: pd.Series) -> pd.Series:
    """close.pct_change(5) - 5*((close-open)/open).rolling(5).mean() — separates
    pure close-to-close ROC from average intra-bar ROC."""
    intra = (close - open_) / open_.replace(0.0, np.nan)
    out = close.pct_change(5) - 5.0 * intra.rolling(5, min_periods=5).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_loretdiff_21d_base_v125_signal(low: pd.Series, close: pd.Series) -> pd.Series:
    """close.pct_change(21) - low.pct_change(21). Diff of close-ROC vs low-ROC —
    captures whether closes are outperforming lows."""
    out = close.pct_change(21) - low.pct_change(21)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_hiretdiff_21d_base_v126_signal(high: pd.Series, close: pd.Series) -> pd.Series:
    """close.pct_change(21) - high.pct_change(21). Close ROC vs high ROC."""
    out = close.pct_change(21) - high.pct_change(21)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_openrocstk_42d_base_v127_signal(open_: pd.Series) -> pd.Series:
    """Streak of consecutive bars where open.diff(1) > 0. Discrete count using
    open-to-open changes."""
    d = open_.diff(1)
    up = (d > 0).astype(int)
    grp = (up == 0).cumsum()
    cnt = up.groupby(grp).cumcount() + 1
    out = cnt.where(up == 1, 0).astype(float)
    out[d.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


# --- additional smoothed ROCs (3) -------------------------------------------


def f11rc_f11_raw_roc_family_emaabsdf_42d_base_v128_signal(closeadj: pd.Series) -> pd.Series:
    """EMA(5) of |pct_change(42)| minus EMA(5) of |pct_change(10)|. Captures
    long-horizon-absolute minus short-horizon-absolute return — orthogonal
    to direction."""
    a42 = closeadj.pct_change(42).abs()
    a10 = closeadj.pct_change(10).abs()
    out = a42.ewm(span=5, adjust=False, min_periods=5).mean() - a10.ewm(span=5, adjust=False, min_periods=5).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_medroc_63d_base_v129_signal(closeadj: pd.Series) -> pd.Series:
    """Rolling-median(7) of pct_change(63). Robust mid-term ROC."""
    r = closeadj.pct_change(63)
    out = r.rolling(7, min_periods=7).median()
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_emaabsret_30d_base_v130_signal(closeadj: pd.Series) -> pd.Series:
    """EMA(10) of |pct_change(1)|. Smoothed volatility-of-returns."""
    r = closeadj.pct_change(1).abs()
    out = r.ewm(span=10, adjust=False, min_periods=10).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- additional discrete / sign-based (5) -----------------------------------


def f11rc_f11_raw_roc_family_signdiff_30d_base_v131_signal(closeadj: pd.Series) -> pd.Series:
    """Diff of sign(pct_change(21)): captures regime-flip days. Values in {-2,-1,0,1,2}."""
    out = np.sign(closeadj.pct_change(21)).diff(1)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_signmean_15d_base_v132_signal(close: pd.Series) -> pd.Series:
    """Mean of sign(pct1) over 15 bars. Discrete-flavored win-rate, centered around 0."""
    s = np.sign(close.pct_change(1))
    out = s.rolling(15, min_periods=15).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_signagree2_21d_base_v133_signal(close: pd.Series) -> pd.Series:
    """sign(pct5)+sign(pct21) — discrete -2..+2."""
    out = np.sign(close.pct_change(5)) + np.sign(close.pct_change(21))
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_signlongdiff_252d_base_v134_signal(closeadj: pd.Series) -> pd.Series:
    """sign(pct63) - sign(pct252). 5-state signed differential across horizons."""
    out = np.sign(closeadj.pct_change(63)) - np.sign(closeadj.pct_change(252))
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_bigdncnt_60d_base_v135_signal(closeadj: pd.Series) -> pd.Series:
    """Count of "big down" bars (pct1 < -1.5*std(pct1,60)) in trailing 60."""
    r = closeadj.pct_change(1)
    sd = r.rolling(60, min_periods=60).std()
    big = (r < -1.5 * sd).astype(float)
    out = big.rolling(60, min_periods=60).sum()
    out[sd.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


# --- additional cross-window / long-horizon (5) ------------------------------


def f11rc_f11_raw_roc_family_wgtroc6_180d_base_v136_signal(closeadj: pd.Series) -> pd.Series:
    """Equally-weighted average of {pct_change(7),14,21,42,84,180}."""
    p1 = closeadj.pct_change(7)
    p2 = closeadj.pct_change(14)
    p3 = closeadj.pct_change(21)
    p4 = closeadj.pct_change(42)
    p5 = closeadj.pct_change(84)
    p6 = closeadj.pct_change(180)
    out = (p1 + p2 + p3 + p4 + p5 + p6) / 6.0
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_difflogvar_60d_base_v137_signal(closeadj: pd.Series) -> pd.Series:
    """var(log return, 30) - var(log return, 60). Vol short minus long."""
    r = np.log(closeadj / closeadj.shift(1).replace(0.0, np.nan))
    v30 = r.rolling(30, min_periods=30).var(ddof=1)
    v60 = r.rolling(60, min_periods=60).var(ddof=1)
    out = v30 - v60
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_kurtdiff_60d_base_v138_signal(closeadj: pd.Series) -> pd.Series:
    """kurt(pct1,30) - kurt(pct1,60). Short minus long kurtosis differential."""
    r = closeadj.pct_change(1)
    k30 = r.rolling(30, min_periods=30).kurt()
    k60 = r.rolling(60, min_periods=60).kurt()
    out = k30 - k60
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_skewdiff_60d_base_v139_signal(closeadj: pd.Series) -> pd.Series:
    """skew(pct1,30) - skew(pct1,60). Skewness differential."""
    r = closeadj.pct_change(1)
    s30 = r.rolling(30, min_periods=30).skew()
    s60 = r.rolling(60, min_periods=60).skew()
    out = s30 - s60
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_normmaxmin_45d_base_v140_signal(closeadj: pd.Series) -> pd.Series:
    """max(pct1,45) + min(pct1,45). Sum of tail extremes; near zero if symmetric."""
    r = closeadj.pct_change(1)
    out = r.rolling(45, min_periods=45).max() + r.rolling(45, min_periods=45).min()
    return out.replace([np.inf, -np.inf], np.nan)


# --- additional path / drawdown variants (4) --------------------------------


def f11rc_f11_raw_roc_family_dnpathlen_45d_base_v141_signal(closeadj: pd.Series) -> pd.Series:
    """sum(|pct1| where pct1<0, 45). Total downside path length."""
    r = closeadj.pct_change(1)
    dn = r.where(r < 0, 0.0).abs()
    out = dn.rolling(45, min_periods=45).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_uppathlen_45d_base_v142_signal(closeadj: pd.Series) -> pd.Series:
    """sum(pct1 where pct1>0, 45). Total upside path length."""
    r = closeadj.pct_change(1)
    up = r.where(r > 0, 0.0)
    out = up.rolling(45, min_periods=45).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_rallyrecov_60d_base_v143_signal(closeadj: pd.Series) -> pd.Series:
    """(close - close.shift(60)) / (max(close,60) - min(close,60)).
    Position of net move inside the price range."""
    num = closeadj - closeadj.shift(60)
    rng = closeadj.rolling(60, min_periods=60).max() - closeadj.rolling(60, min_periods=60).min()
    out = num / rng.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_drawdepth_120d_base_v144_signal(closeadj: pd.Series) -> pd.Series:
    """Drawdown depth: (min(close,120) - max(close,120))/max(close,120). Always ≤ 0."""
    hi = closeadj.rolling(120, min_periods=120).max()
    lo = closeadj.rolling(120, min_periods=120).min()
    out = (lo - hi) / hi.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# --- additional ratios and structural blends (6) ----------------------------


def f11rc_f11_raw_roc_family_rocsq_30d_base_v145_signal(closeadj: pd.Series) -> pd.Series:
    """Sum of squared returns over 30 (realized variance, raw, not annualized)."""
    r = closeadj.pct_change(1)
    out = (r ** 2).rolling(30, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_medabsret_30d_base_v146_signal(closeadj: pd.Series) -> pd.Series:
    """Rolling median of |pct1| over 30 — robust scale, very different shape
    from sum-of-squares."""
    r = closeadj.pct_change(1).abs()
    out = r.rolling(30, min_periods=30).median()
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_tailwt_50d_base_v147_signal(closeadj: pd.Series) -> pd.Series:
    """Sum of |pct1|^3 over 50 bars / sum of |pct1| over 50 bars.
    Weighted average where bigger moves dominate — captures tail-heaviness."""
    r = closeadj.pct_change(1).abs()
    num = (r ** 3).rolling(50, min_periods=50).sum()
    den = r.rolling(50, min_periods=50).sum()
    out = num / den.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_corretrng_60d_base_v148_signal(closeadj: pd.Series) -> pd.Series:
    """Correlation between pct_change(1) and |pct_change(1)| over 60 bars
    (leverage / asymmetric-vol effect)."""
    r = closeadj.pct_change(1)
    out = r.rolling(60, min_periods=60).corr(r.abs())
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_logvol_120d_base_v149_signal(closeadj: pd.Series) -> pd.Series:
    """Std of log returns over 120 bars."""
    r = np.log(closeadj / closeadj.shift(1).replace(0.0, np.nan))
    out = r.rolling(120, min_periods=120).std(ddof=1)
    return out.replace([np.inf, -np.inf], np.nan)


def f11rc_f11_raw_roc_family_normret_45d_base_v150_signal(closeadj: pd.Series) -> pd.Series:
    """(close - close.shift(45)) divided by (max(close,45) - min(close,45)).
    Bounded position of net move inside price range — distinct from rallyrecov_60."""
    num = closeadj - closeadj.shift(45)
    rng = closeadj.rolling(45, min_periods=45).max() - closeadj.rolling(45, min_periods=45).min()
    out = num / rng.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f11_raw_roc_family_base_076_150_REGISTRY = {
    "f11rc_f11_raw_roc_family_roc_2d_base_v076_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_roc_2d_base_v076_signal},
    "f11rc_f11_raw_roc_family_roc_10d_base_v077_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_roc_10d_base_v077_signal},
    "f11rc_f11_raw_roc_family_logret_42d_base_v078_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_logret_42d_base_v078_signal},
    "f11rc_f11_raw_roc_family_logretkurt_45d_base_v079_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_logretkurt_45d_base_v079_signal},
    "f11rc_f11_raw_roc_family_rocsemi_40d_base_v080_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_rocsemi_40d_base_v080_signal},
    "f11rc_f11_raw_roc_family_updnstdratio_60d_base_v081_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_updnstdratio_60d_base_v081_signal},
    "f11rc_f11_raw_roc_family_signsqret_30d_base_v082_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_signsqret_30d_base_v082_signal},
    "f11rc_f11_raw_roc_family_rocsignal_30d_base_v083_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_rocsignal_30d_base_v083_signal},
    "f11rc_f11_raw_roc_family_rocdf_15d_base_v084_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_rocdf_15d_base_v084_signal},
    "f11rc_f11_raw_roc_family_rocdf_42d_base_v085_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_rocdf_42d_base_v085_signal},
    "f11rc_f11_raw_roc_family_rocdf_126d_base_v086_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_rocdf_126d_base_v086_signal},
    "f11rc_f11_raw_roc_family_rocdfsign_63d_base_v087_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_rocdfsign_63d_base_v087_signal},
    "f11rc_f11_raw_roc_family_rocdrop_63d_base_v088_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_rocdrop_63d_base_v088_signal},
    "f11rc_f11_raw_roc_family_uprtcnt_10d_base_v089_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_uprtcnt_10d_base_v089_signal},
    "f11rc_f11_raw_roc_family_dnrtcnt_21d_base_v090_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_dnrtcnt_21d_base_v090_signal},
    "f11rc_f11_raw_roc_family_alterncnt_45d_base_v091_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_alterncnt_45d_base_v091_signal},
    "f11rc_f11_raw_roc_family_dssince5pct_120d_base_v092_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_dssince5pct_120d_base_v092_signal},
    "f11rc_f11_raw_roc_family_signstreak_30d_base_v093_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_signstreak_30d_base_v093_signal},
    "f11rc_f11_raw_roc_family_bigupcnt_60d_base_v094_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_bigupcnt_60d_base_v094_signal},
    "f11rc_f11_raw_roc_family_retskew_90d_base_v095_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_retskew_90d_base_v095_signal},
    "f11rc_f11_raw_roc_family_retkurt_30d_base_v096_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_retkurt_30d_base_v096_signal},
    "f11rc_f11_raw_roc_family_winratio_90d_base_v098_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_winratio_90d_base_v098_signal},
    "f11rc_f11_raw_roc_family_avgdnmag_45d_base_v099_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_avgdnmag_45d_base_v099_signal},
    "f11rc_f11_raw_roc_family_retac3_50d_base_v100_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_retac3_50d_base_v100_signal},
    "f11rc_f11_raw_roc_family_signac1_60d_base_v101_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_signac1_60d_base_v101_signal},
    "f11rc_f11_raw_roc_family_sqrac1_45d_base_v102_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_sqrac1_45d_base_v102_signal},
    "f11rc_f11_raw_roc_family_pathlen_60d_base_v103_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_pathlen_60d_base_v103_signal},
    "f11rc_f11_raw_roc_family_pathvsstd_30d_base_v105_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_pathvsstd_30d_base_v105_signal},
    "f11rc_f11_raw_roc_family_maxdd_120d_base_v106_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_maxdd_120d_base_v106_signal},
    "f11rc_f11_raw_roc_family_drwdwn_30d_base_v107_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_drwdwn_30d_base_v107_signal},
    "f11rc_f11_raw_roc_family_topbotrng_45d_base_v108_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_topbotrng_45d_base_v108_signal},
    "f11rc_f11_raw_roc_family_avgtop3_30d_base_v109_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_avgtop3_30d_base_v109_signal},
    "f11rc_f11_raw_roc_family_avgbot3_30d_base_v110_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_avgbot3_30d_base_v110_signal},
    "f11rc_f11_raw_roc_family_iqrret_60d_base_v111_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_iqrret_60d_base_v111_signal},
    "f11rc_f11_raw_roc_family_tanharctan_30d_base_v112_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_tanharctan_30d_base_v112_signal},
    "f11rc_f11_raw_roc_family_arctan_long_v113_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_arctan_long_v113_signal},
    "f11rc_f11_raw_roc_family_rkdf_60d_base_v114_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_rkdf_60d_base_v114_signal},
    "f11rc_f11_raw_roc_family_pctrnk21_60d_base_v115_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_pctrnk21_60d_base_v115_signal},
    "f11rc_f11_raw_roc_family_sigsharpe_90d_base_v116_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_sigsharpe_90d_base_v116_signal},
    "f11rc_f11_raw_roc_family_signalign3_42d_base_v117_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_signalign3_42d_base_v117_signal},
    "f11rc_f11_raw_roc_family_signsum5_84d_base_v118_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_signsum5_84d_base_v118_signal},
    "f11rc_f11_raw_roc_family_minabs5_30d_base_v119_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_minabs5_30d_base_v119_signal},
    "f11rc_f11_raw_roc_family_centmin_pct_60d_base_v120_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_centmin_pct_60d_base_v120_signal},
    "f11rc_f11_raw_roc_family_vrq5_60d_base_v121_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_vrq5_60d_base_v121_signal},
    "f11rc_f11_raw_roc_family_vrq20_120d_base_v122_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_vrq20_120d_base_v122_signal},
    "f11rc_f11_raw_roc_family_tstat_21d_base_v123_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_tstat_21d_base_v123_signal},
    "f11rc_f11_raw_roc_family_clcldiff_5d_base_v124_signal": {"inputs": ["open", "close"], "func": f11rc_f11_raw_roc_family_clcldiff_5d_base_v124_signal},
    "f11rc_f11_raw_roc_family_loretdiff_21d_base_v125_signal": {"inputs": ["low", "close"], "func": f11rc_f11_raw_roc_family_loretdiff_21d_base_v125_signal},
    "f11rc_f11_raw_roc_family_hiretdiff_21d_base_v126_signal": {"inputs": ["high", "close"], "func": f11rc_f11_raw_roc_family_hiretdiff_21d_base_v126_signal},
    "f11rc_f11_raw_roc_family_openrocstk_42d_base_v127_signal": {"inputs": ["open"], "func": f11rc_f11_raw_roc_family_openrocstk_42d_base_v127_signal},
    "f11rc_f11_raw_roc_family_emaabsdf_42d_base_v128_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_emaabsdf_42d_base_v128_signal},
    "f11rc_f11_raw_roc_family_medroc_63d_base_v129_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_medroc_63d_base_v129_signal},
    "f11rc_f11_raw_roc_family_emaabsret_30d_base_v130_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_emaabsret_30d_base_v130_signal},
    "f11rc_f11_raw_roc_family_signdiff_30d_base_v131_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_signdiff_30d_base_v131_signal},
    "f11rc_f11_raw_roc_family_signmean_15d_base_v132_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_signmean_15d_base_v132_signal},
    "f11rc_f11_raw_roc_family_signagree2_21d_base_v133_signal": {"inputs": ["close"], "func": f11rc_f11_raw_roc_family_signagree2_21d_base_v133_signal},
    "f11rc_f11_raw_roc_family_signlongdiff_252d_base_v134_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_signlongdiff_252d_base_v134_signal},
    "f11rc_f11_raw_roc_family_bigdncnt_60d_base_v135_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_bigdncnt_60d_base_v135_signal},
    "f11rc_f11_raw_roc_family_wgtroc6_180d_base_v136_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_wgtroc6_180d_base_v136_signal},
    "f11rc_f11_raw_roc_family_difflogvar_60d_base_v137_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_difflogvar_60d_base_v137_signal},
    "f11rc_f11_raw_roc_family_kurtdiff_60d_base_v138_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_kurtdiff_60d_base_v138_signal},
    "f11rc_f11_raw_roc_family_skewdiff_60d_base_v139_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_skewdiff_60d_base_v139_signal},
    "f11rc_f11_raw_roc_family_normmaxmin_45d_base_v140_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_normmaxmin_45d_base_v140_signal},
    "f11rc_f11_raw_roc_family_dnpathlen_45d_base_v141_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_dnpathlen_45d_base_v141_signal},
    "f11rc_f11_raw_roc_family_uppathlen_45d_base_v142_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_uppathlen_45d_base_v142_signal},
    "f11rc_f11_raw_roc_family_rallyrecov_60d_base_v143_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_rallyrecov_60d_base_v143_signal},
    "f11rc_f11_raw_roc_family_drawdepth_120d_base_v144_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_drawdepth_120d_base_v144_signal},
    "f11rc_f11_raw_roc_family_rocsq_30d_base_v145_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_rocsq_30d_base_v145_signal},
    "f11rc_f11_raw_roc_family_medabsret_30d_base_v146_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_medabsret_30d_base_v146_signal},
    "f11rc_f11_raw_roc_family_tailwt_50d_base_v147_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_tailwt_50d_base_v147_signal},
    "f11rc_f11_raw_roc_family_corretrng_60d_base_v148_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_corretrng_60d_base_v148_signal},
    "f11rc_f11_raw_roc_family_logvol_120d_base_v149_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_logvol_120d_base_v149_signal},
    "f11rc_f11_raw_roc_family_normret_45d_base_v150_signal": {"inputs": ["closeadj"], "func": f11rc_f11_raw_roc_family_normret_45d_base_v150_signal},
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
    for name, entry in f11_raw_roc_family_base_076_150_REGISTRY.items():
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
    print(f"OK base_076_150: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
