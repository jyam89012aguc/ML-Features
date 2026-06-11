"""f15_cross_sectional_momentum base features 076-150.

Cross-sectional-style momentum (single-ticker adapted): rank/z/quintile/
streak-style features that measure momentum RELATIVE to the stock's own
trailing distribution.

Window > 21 -> closeadj. Window <= 21 -> close. Each feature is a fully
expanded def block. NaN policy: never fillna(0); only replace([inf,-inf], nan)
at return.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Features 076-150
# ---------------------------------------------------------------------------


# --- A. Time-spent-above features ------------------------------------------


def f15xm_f15_cross_sectional_momentum_aboverm_120d_base_v076_signal(closeadj):
    """Fraction of last 120d where close > trailing-120d rolling MEDIAN.
    Above-median time as cross-sectional-style rank-state count."""
    med = closeadj.rolling(120, min_periods=100).median()
    flag = (closeadj > med).astype(float).where(~med.isna())
    return flag.rolling(120, min_periods=100).mean().replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_abovemean_252d_base_v077_signal(closeadj):
    """Fraction of last 252d where 21d return > trailing-252d mean of 21d return.
    Outperformance count vs own mean."""
    r = closeadj.pct_change(21)
    mu = r.rolling(252, min_periods=200).mean()
    flag = (r > mu).astype(float).where(~mu.isna())
    return flag.rolling(252, min_periods=200).mean().replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_aboveewma_60d_base_v078_signal(closeadj):
    """Fraction of last 60d where close > 30-span EWMA. EWMA-relative
    outperformance time — different smoothing than SMA."""
    ema = closeadj.ewm(span=30, adjust=False, min_periods=25).mean()
    flag = (closeadj > ema).astype(float).where(~ema.isna())
    return flag.rolling(60, min_periods=50).mean().replace([np.inf, -np.inf], np.nan)


# --- B. Trailing distribution-shape features ------------------------------


def f15xm_f15_cross_sectional_momentum_skewlog_60d_base_v079_signal(closeadj):
    """Skewness of trailing 60d log-returns (short-horizon distributional
    asymmetry). Distinct horizon from base v020 (120d)."""
    return np.log(closeadj).diff().rolling(60, min_periods=50).skew().replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_kurtlog_60d_base_v080_signal(closeadj):
    """Excess kurtosis of trailing 60d log-returns."""
    return np.log(closeadj).diff().rolling(60, min_periods=50).kurt().replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_iqr_60d_base_v081_signal(closeadj):
    """Inter-quartile range of trailing 60d log-returns, scaled by std.
    Distributional shape distinct from sigma."""
    r = np.log(closeadj).diff()
    q75 = r.rolling(60, min_periods=50).quantile(0.75)
    q25 = r.rolling(60, min_periods=50).quantile(0.25)
    sd = r.rolling(60, min_periods=50).std(ddof=1)
    return ((q75 - q25) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- C. Conditional cumulative returns -----------------------------------


def f15xm_f15_cross_sectional_momentum_cumupret_60d_base_v082_signal(closeadj):
    """Sum of POSITIVE daily log-returns over 60d divided by total |daily
    log-return| sum. Up-side return share — bounded in (0,1)."""
    r = np.log(closeadj).diff()
    pos = r.where(r > 0.0, 0.0).rolling(60, min_periods=50).sum()
    tot = r.abs().rolling(60, min_periods=50).sum()
    return (pos / tot.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_dnconc_60d_base_v083_signal(closeadj):
    """Herfindahl concentration of negative returns over 60d: SUM(r_i^2 | r_i<0)
    / (SUM(|r_i| | r_i<0))^2. Captures whether down-side losses are concentrated
    in a few large drops vs spread out. Non-monotone in up-share."""
    r = closeadj.pct_change()
    neg = r.where(r < 0.0)
    sq = (neg ** 2).rolling(60, min_periods=15).sum()
    abs_sum = neg.abs().rolling(60, min_periods=15).sum()
    return (sq / (abs_sum ** 2).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- D. Crossing-event counts --------------------------------------------


def f15xm_f15_cross_sectional_momentum_zeroret_120d_base_v084_signal(closeadj):
    """Count of return-sign flips in 120d — a momentum-PERSISTENCE inverse.
    Distinct from rank/z features."""
    sg = np.sign(closeadj.diff())
    flip = (sg != sg.shift(1)).astype(float).where(~sg.isna() & ~sg.shift(1).isna())
    return flip.rolling(120, min_periods=100).sum().replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_medxr_252d_base_v085_signal(closeadj):
    """Count of times in trailing 252d where 21d return crossed its trailing
    252d MEDIAN — regime-instability count."""
    r = closeadj.pct_change(21)
    med = r.rolling(252, min_periods=200).median()
    sg = np.sign(r - med)
    flip = (sg != sg.shift(1)).astype(float).where(~sg.isna() & ~sg.shift(1).isna())
    return flip.rolling(252, min_periods=200).sum().replace([np.inf, -np.inf], np.nan)


# --- E. Rank-of-rank features ----------------------------------------------


def f15xm_f15_cross_sectional_momentum_rrk21_252d_base_v086_signal(closeadj):
    """Trailing-252d AVERAGE of: percentile rank of 21d return vs trailing
    252d. Time-averaged rank — captures persistent-ranking momentum."""
    r = closeadj.pct_change(21)
    rk = r.rolling(252, min_periods=200).rank(pct=True)
    return rk.rolling(252, min_periods=200).mean().replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_rrkstd_252d_base_v087_signal(closeadj):
    """Trailing-252d STD of: 21d-return percentile rank. Volatility-of-rank
    — high = rank fluctuates, low = stable bucket."""
    r = closeadj.pct_change(21)
    rk = r.rolling(252, min_periods=200).rank(pct=True)
    return rk.rolling(252, min_periods=200).std(ddof=1).replace([np.inf, -np.inf], np.nan)


# --- F. UMD variants ------------------------------------------------------


def f15xm_f15_cross_sectional_momentum_umd9_189d_base_v088_signal(closeadj):
    """9-1 momentum: log(close.shift(21)) - log(close.shift(189)). 9-month-
    minus-1-month classic Jegadeesh-Titman variant."""
    r = np.log(closeadj.shift(21)) - np.log(closeadj.shift(189))
    sd = closeadj.pct_change().rolling(189, min_periods=150).std(ddof=1) * np.sqrt(168.0)
    return (r / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_umd3_84d_base_v089_signal(closeadj):
    """3-1 momentum: log(close.shift(21)) - log(close.shift(84))."""
    r = np.log(closeadj.shift(21)) - np.log(closeadj.shift(84))
    sd = closeadj.pct_change().rolling(84, min_periods=63).std(ddof=1) * np.sqrt(63.0)
    return (r / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_umdcheap_504d_base_v090_signal(closeadj):
    """Negated 1-month return MINUS positive 12-month return: -r1m + r12m.
    Long-winner + short-loser composite — classic 'low past-1m, high past-12m'
    constructive signal."""
    r1 = np.log(closeadj).diff(21)
    r12 = np.log(closeadj).diff(252)
    return (r12 - r1).replace([np.inf, -np.inf], np.nan)


# --- G. Volatility-of-momentum --------------------------------------------


def f15xm_f15_cross_sectional_momentum_volofrnk_252d_base_v091_signal(closeadj):
    """Std of percentile rank of 5d return (vs 60d) over trailing 252d.
    Captures how variable the short-horizon-rank is — momentum stability."""
    rk = closeadj.pct_change(5).rolling(60, min_periods=50).rank(pct=True)
    return rk.rolling(252, min_periods=200).std(ddof=1).replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_volofz_120d_base_v092_signal(closeadj):
    """Std of 21d-return z-score (vs 60d) over trailing 120d."""
    r = closeadj.pct_change(21)
    z = (r - r.rolling(60, min_periods=50).mean()) / r.rolling(60, min_periods=50).std(ddof=1).replace(0.0, np.nan)
    return z.rolling(120, min_periods=100).std(ddof=1).replace([np.inf, -np.inf], np.nan)


# --- H. Negative-/positive- moment of returns -----------------------------


def f15xm_f15_cross_sectional_momentum_lpm_120d_base_v093_signal(closeadj):
    """Lower partial moment (2nd) over 120d: mean of (min(r, 0))^2.
    Downside-only second moment — captures downside vol for momentum stocks."""
    r = closeadj.pct_change()
    neg = r.where(r < 0.0, 0.0) ** 2
    return neg.rolling(120, min_periods=100).mean().replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_upmratio_120d_base_v094_signal(closeadj):
    """RATIO of upper-partial-moment to lower-partial-moment (2nd order) over
    120d. Asymmetry between up-volatility and down-volatility — non-monotone
    in q90 alone."""
    r = closeadj.pct_change()
    upm = (r.where(r > 0.0, 0.0) ** 2).rolling(120, min_periods=100).mean()
    lpm = (r.where(r < 0.0, 0.0) ** 2).rolling(120, min_periods=100).mean()
    return (upm / lpm.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- I. Skipped-month momentum lookbacks ----------------------------------


def f15xm_f15_cross_sectional_momentum_skipmo_126d_base_v095_signal(closeadj):
    """Skip-month return: log return from t-126 to t-5 (skip 5 days).
    Short-skip variant of UMD."""
    r = np.log(closeadj.shift(5)) - np.log(closeadj.shift(126))
    return r.replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_skipmovrnk_252d_base_v096_signal(closeadj):
    """Percentile rank vs trailing 504d of: log return from t-10 to t-252,
    normalized by trailing-252d volatility. Vol-normalized RANK of skip-month
    momentum (distinct from raw level in v095/v090)."""
    r = (np.log(closeadj.shift(10)) - np.log(closeadj.shift(252)))
    v = np.log(closeadj).diff().rolling(252, min_periods=200).std(ddof=1) * np.sqrt(242.0)
    sig = r / v.replace(0.0, np.nan)
    return sig.rolling(504, min_periods=300).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# --- J. EWMA-relative momentum --------------------------------------------


def f15xm_f15_cross_sectional_momentum_ewmaratio_60d_base_v097_signal(closeadj):
    """Log(close / EWMA(close, 60d-span)) — exponentially-weighted distance.
    Smooth-relative momentum. Distinct from SMA-distance (f01 territory)
    by being a percentage-position rather than level distance."""
    ema = closeadj.ewm(span=60, adjust=False, min_periods=40).mean()
    return np.log(closeadj / ema.replace(0.0, np.nan)).rolling(252, min_periods=200).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# --- K. Conditional outperformance count by quintile ----------------------


def f15xm_f15_cross_sectional_momentum_topqdays_120d_base_v098_signal(closeadj):
    """Days in last 120 where 5d-return rank (vs 60d) is in top quintile."""
    rk = closeadj.pct_change(5).rolling(60, min_periods=50).rank(pct=True)
    flag = (rk >= 0.8).astype(float).where(~rk.isna())
    return flag.rolling(120, min_periods=100).sum().replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_botqdays_120d_base_v099_signal(closeadj):
    """Days in last 120 where 5d-return rank (vs 60d) is in bottom quintile."""
    rk = closeadj.pct_change(5).rolling(60, min_periods=50).rank(pct=True)
    flag = (rk <= 0.2).astype(float).where(~rk.isna())
    return flag.rolling(120, min_periods=100).sum().replace([np.inf, -np.inf], np.nan)


# --- L. Robust trend-of-rank --------------------------------------------


def f15xm_f15_cross_sectional_momentum_rkmkscore_60d_base_v100_signal(closeadj):
    """Mann-Kendall S on trailing 60d of: percentile rank of daily return vs 60d.
    Trend of return-rank time-series — measures rank-uptrend / downtrend."""
    n = 60
    rk = closeadj.pct_change().rolling(60, min_periods=50).rank(pct=True)
    norm = n * (n - 1) / 2.0

    def _mk(x):
        if np.any(~np.isfinite(x)):
            return np.nan
        s = 0
        for i in range(n - 1):
            d = x[i + 1:] - x[i]
            s += int(np.sum(d > 0) - np.sum(d < 0))
        return s / norm
    return rk.rolling(n, min_periods=n).apply(_mk, raw=True).replace([np.inf, -np.inf], np.nan)


# --- M. ATR-normalized cumulative return ranks -----------------------------


def f15xm_f15_cross_sectional_momentum_atrnorm_63d_base_v101_signal(high, low, closeadj):
    """63d log-return divided by 63d mean of true-range / close — vol-adjusted
    momentum, ranked vs trailing 252d."""
    r = np.log(closeadj).diff(63)
    prev = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - prev).abs(), (low - prev).abs()], axis=1).max(axis=1)
    avgtr = (tr / closeadj).rolling(63, min_periods=50).mean()
    ratio = r / avgtr.replace(0.0, np.nan)
    return ratio.rolling(252, min_periods=200).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# --- N. Sign-momentum oscillator (signed CMO) ------------------------------


def f15xm_f15_cross_sectional_momentum_signmom_60d_base_v102_signal(closeadj):
    """(SUM(+returns) - SUM(|-returns|)) / SUM(|returns|) over 60d. Signed
    efficiency-style cross-sectional-styled directional momentum bounded
    in [-1, 1]. Z-scored vs trailing 252d to ensure rank-style normalization."""
    r = closeadj.pct_change()
    pos = r.where(r > 0.0, 0.0).rolling(60, min_periods=50).sum()
    neg = (-r.where(r < 0.0, 0.0)).rolling(60, min_periods=50).sum()
    tot = pos + neg
    sig = (pos - neg) / tot.replace(0.0, np.nan)
    mu = sig.rolling(252, min_periods=200).mean()
    sd = sig.rolling(252, min_periods=200).std(ddof=1)
    return ((sig - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- O. Win-magnitude ratio -----------------------------------------------


def f15xm_f15_cross_sectional_momentum_winsize_60d_base_v103_signal(closeadj):
    """Mean magnitude of UP days / mean magnitude of DOWN days, over 60d.
    Captures whether wins are larger than losses (momentum-stock trait)."""
    r = closeadj.pct_change()
    up = r.where(r > 0.0).abs().rolling(60, min_periods=15).mean()
    dn = r.where(r < 0.0).abs().rolling(60, min_periods=15).mean()
    return (up / dn.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- P. Quantile of cumulative-return path -------------------------------


def f15xm_f15_cross_sectional_momentum_pathq_252d_base_v104_signal(closeadj):
    """Fraction of trailing 252d during which trailing 21d return was > 0."""
    r = closeadj.pct_change(21)
    pos = (r > 0.0).astype(float).where(~r.isna())
    return pos.rolling(252, min_periods=200).mean().replace([np.inf, -np.inf], np.nan)


# --- Q. Discrete-state code ----------------------------------------------


def f15xm_f15_cross_sectional_momentum_state_252d_base_v105_signal(closeadj):
    """Discrete state code (1..9): combines (low/mid/high) of 21d-ret rank
    with (low/mid/high) of 252d-ret rank — joint short-long horizon bucket.
    Encodes 9 momentum regimes."""
    rk21 = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    rk252 = closeadj.pct_change(252).rolling(504, min_periods=300).rank(pct=True)
    def _bucket(x):
        b = pd.Series(0.0, index=x.index)
        b = b.where(x.isna(), 1.0)
        b = b.where(~(x >= 0.66), 3.0)
        b = b.where(~((x >= 0.33) & (x < 0.66)), 2.0)
        return b
    b1 = _bucket(rk21)
    b2 = _bucket(rk252)
    out = (b1 - 1.0) * 3.0 + b2
    return out.replace([np.inf, -np.inf], np.nan)


# --- R. Drawdown-recovery features ---------------------------------------


def f15xm_f15_cross_sectional_momentum_ddmag_252d_base_v106_signal(closeadj):
    """Magnitude of current drawdown from trailing-252d max, as fraction of
    trailing 252d log-std. Cross-sectional-style drawdown z."""
    mx = closeadj.rolling(252, min_periods=200).max()
    dd = (closeadj / mx - 1.0)
    sd = np.log(closeadj).diff().rolling(252, min_periods=200).std(ddof=1) * np.sqrt(252.0)
    return (dd / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)




# --- S. Volume-relative-momentum signals --------------------------------


def f15xm_f15_cross_sectional_momentum_volwret_21d_base_v108_signal(close, volume):
    """Volume-weighted 21d return: SUM(daily-log-ret * volume) / SUM(volume) over 21d.
    Cross-sectional-style volume-adjusted momentum."""
    r = np.log(close).diff()
    rv = (r * volume).rolling(21, min_periods=15).sum()
    v = volume.rolling(21, min_periods=15).sum()
    return (rv / v.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_volwretrnk_63d_base_v109_signal(closeadj, volume):
    """Rank vs trailing 252d of volume-weighted 63d log-return."""
    r = np.log(closeadj).diff()
    rv = (r * volume).rolling(63, min_periods=50).sum()
    v = volume.rolling(63, min_periods=50).sum()
    sig = rv / v.replace(0.0, np.nan)
    return sig.rolling(252, min_periods=200).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# --- T. Return-distribution-quantile features ----------------------------


def f15xm_f15_cross_sectional_momentum_q90_120d_base_v110_signal(closeadj):
    """90th-percentile of trailing 120d daily log-returns. Right-tail value."""
    return np.log(closeadj).diff().rolling(120, min_periods=100).quantile(0.9).replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_q10_120d_base_v111_signal(closeadj):
    """10th-percentile of trailing 120d daily log-returns. Left-tail value."""
    return np.log(closeadj).diff().rolling(120, min_periods=100).quantile(0.1).replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_q90q10_120d_base_v112_signal(closeadj):
    """Sum of 90th and 10th percentile of trailing 120d log-returns.
    Asymmetry-of-tails — momentum-signature feature."""
    r = np.log(closeadj).diff()
    q90 = r.rolling(120, min_periods=100).quantile(0.9)
    q10 = r.rolling(120, min_periods=100).quantile(0.1)
    return (q90 + q10).replace([np.inf, -np.inf], np.nan)


# --- U. Persistent-trend boolean -----------------------------------------


def f15xm_f15_cross_sectional_momentum_persisttrend_60d_base_v113_signal(closeadj):
    """Discrete: +1 if 5d return rank, 21d return rank, AND 63d return rank
    are ALL > 0.5 (all-horizons positive momentum); -1 if all < 0.5; 0 else."""
    rk5 = closeadj.pct_change(5).rolling(60, min_periods=50).rank(pct=True)
    rk21 = closeadj.pct_change(21).rolling(60, min_periods=50).rank(pct=True)
    rk63 = closeadj.pct_change(63).rolling(126, min_periods=100).rank(pct=True)
    pos = ((rk5 > 0.5) & (rk21 > 0.5) & (rk63 > 0.5)).astype(float)
    neg = ((rk5 < 0.5) & (rk21 < 0.5) & (rk63 < 0.5)).astype(float)
    mask = rk5.isna() | rk21.isna() | rk63.isna()
    return (pos - neg).where(~mask).replace([np.inf, -np.inf], np.nan)


# --- V. Maximum-drawdown rank --------------------------------------------


def f15xm_f15_cross_sectional_momentum_maxddrnk_252d_base_v114_signal(closeadj):
    """Rank vs trailing 252d of trailing-60d max-drawdown magnitude.
    Cross-sectional-style max-DD rank distinct from current-DD."""
    mx = closeadj.rolling(60, min_periods=50).max()
    dd = (closeadj / mx - 1.0)
    minDD = dd.rolling(60, min_periods=50).min().abs()
    return minDD.rolling(252, min_periods=200).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# --- W. Time-since-best-quintile features --------------------------------


def f15xm_f15_cross_sectional_momentum_dsbq_252d_base_v115_signal(closeadj):
    """Days since 21d return was last in TOP QUINTILE of trailing 252d. Cap 252."""
    rk = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    flag = (rk >= 0.8).astype(float).where(~rk.isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return 252.0
        return float(len(x) - 1 - idx[-1])
    return flag.rolling(252, min_periods=200).apply(_ds, raw=True).replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_dswq_252d_base_v116_signal(closeadj):
    """Days since 21d return was last in BOTTOM QUINTILE."""
    rk = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    flag = (rk <= 0.2).astype(float).where(~rk.isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return 252.0
        return float(len(x) - 1 - idx[-1])
    return flag.rolling(252, min_periods=200).apply(_ds, raw=True).replace([np.inf, -np.inf], np.nan)


# --- X. Cross-horizon agreement-magnitude -------------------------------


def f15xm_f15_cross_sectional_momentum_xhagree_60d_base_v117_signal(closeadj):
    """Mean over 60d of: 1 if sign(5d_ret) == sign(21d_ret) == sign(63d_ret),
    -1 if all three opposing-vs-21d, 0 partial. Captures persistent multi-
    horizon directional agreement."""
    s5 = np.sign(closeadj.pct_change(5))
    s21 = np.sign(closeadj.pct_change(21))
    s63 = np.sign(closeadj.pct_change(63))
    agree = (s5 == s21).astype(float) + (s21 == s63).astype(float) + (s5 == s63).astype(float)
    sgn_total = s5 + s21 + s63
    out = (agree - 1.5) * np.sign(sgn_total)
    mask = s5.isna() | s21.isna() | s63.isna()
    return out.where(~mask).rolling(60, min_periods=50).mean().replace([np.inf, -np.inf], np.nan)


# --- Y. Rolling Spearman-of-ranks ----------------------------------------


def f15xm_f15_cross_sectional_momentum_rcumrnk_60d_base_v118_signal(closeadj):
    """Spearman rank correlation of close vs time over 60d. Rank-monotonic
    trend strength. Different from f03 because we use this as the rank-derived
    cross-sectional analog (here rank is monotonic-time-rank, capturing
    cross-sectional rank stability)."""
    n = 60
    def _rc(x):
        if np.any(~np.isfinite(x)):
            return np.nan
        rx = pd.Series(x).rank().to_numpy()
        rt = np.arange(1, n + 1, dtype=float)
        sx = rx.std()
        if sx <= 0:
            return np.nan
        return float(np.corrcoef(rx, rt)[0, 1])
    return closeadj.rolling(n, min_periods=n).apply(_rc, raw=True).replace([np.inf, -np.inf], np.nan)


# --- Z. Tail-loss / tail-gain ratio --------------------------------------


def f15xm_f15_cross_sectional_momentum_tailloss_252d_base_v119_signal(closeadj):
    """Mean of bottom-5% returns over trailing 252d. CVaR-style tail loss."""
    r = np.log(closeadj).diff()
    def _cvar(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)):
            return np.nan
        q = np.quantile(x, 0.05)
        return float(x[x <= q].mean())
    return r.rolling(252, min_periods=200).apply(_cvar, raw=True).replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_tailgain_252d_base_v120_signal(closeadj):
    """Mean of top-5% returns over trailing 252d (right-tail mean)."""
    r = np.log(closeadj).diff()
    def _cvar(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)):
            return np.nan
        q = np.quantile(x, 0.95)
        return float(x[x >= q].mean())
    return r.rolling(252, min_periods=200).apply(_cvar, raw=True).replace([np.inf, -np.inf], np.nan)


# --- AA. Geometric vs arithmetic return spread --------------------------


def f15xm_f15_cross_sectional_momentum_geoarith_rnk_252d_base_v121_signal(closeadj):
    """RANK vs trailing 504d of: 60d-mean(daily simple ret) - 60d-mean(daily log
    ret). Vol-drag RANK at a shorter (60d) horizon — non-monotone in long-window
    tail-loss because rank scale is bounded."""
    r_simple = closeadj.pct_change()
    r_log = np.log(closeadj).diff()
    drag = r_simple.rolling(60, min_periods=50).mean() - r_log.rolling(60, min_periods=50).mean()
    return drag.rolling(504, min_periods=300).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# --- AB. Negative skew flag (regime) ------------------------------------


def f15xm_f15_cross_sectional_momentum_negskewreg_120d_base_v122_signal(closeadj):
    """sign(skew(120d log returns) - rolling median of itself over 252d).
    Discrete regime indicator: high-skew vs low-skew momentum regime."""
    sk = np.log(closeadj).diff().rolling(120, min_periods=100).skew()
    med = sk.rolling(252, min_periods=200).median()
    return np.sign(sk - med).replace([np.inf, -np.inf], np.nan)


# --- AC. Hi/Lo position rank -------------------------------------------


def f15xm_f15_cross_sectional_momentum_hilopos_252d_base_v123_signal(high, low, closeadj):
    """Position of closeadj within trailing-252d high-low range, ranked
    vs trailing 252d of itself. Cross-sectional-style hi-lo position rank."""
    hh = high.rolling(252, min_periods=200).max()
    ll = low.rolling(252, min_periods=200).min()
    pos = (closeadj - ll) / (hh - ll).replace(0.0, np.nan)
    return pos.rolling(252, min_periods=200).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# --- AD. Beta-to-trend ---------------------------------------------------


def f15xm_f15_cross_sectional_momentum_trendbeta_120d_base_v124_signal(closeadj):
    """OLS slope of close on its rolling 60d mean over 120d. Captures whether
    close moves with its trend (beta>1 momentum), less than trend (beta<1)."""
    n = 120
    sma60 = closeadj.rolling(60, min_periods=50).mean()
    def _slope(idx):
        # Apply requires raw=True over the close window
        return idx
    mu_x = sma60.rolling(n, min_periods=100).mean()
    mu_y = closeadj.rolling(n, min_periods=100).mean()
    cov = (closeadj * sma60).rolling(n, min_periods=100).mean() - mu_x * mu_y
    var = (sma60 * sma60).rolling(n, min_periods=100).mean() - mu_x * mu_x
    return (cov / var.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- AE. Acceleration-style ranks --------------------------------------


def f15xm_f15_cross_sectional_momentum_accelrnk_60d_base_v125_signal(closeadj):
    """Rank vs trailing 252d of: 21d return - 21d-ago-21d-return. Rolling
    acceleration of momentum, ranked."""
    r = closeadj.pct_change(21)
    accel = r - r.shift(21)
    return accel.rolling(252, min_periods=200).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# --- AF. Multi-horizon coherence ---------------------------------------


def f15xm_f15_cross_sectional_momentum_horizoncoh_120d_base_v126_signal(closeadj):
    """Standardized signed sum: (rk5 + rk21 + rk63 - 1.5) / std of trailing 120d
    of this sum. Composite multi-horizon momentum z."""
    rk5 = closeadj.pct_change(5).rolling(60, min_periods=50).rank(pct=True)
    rk21 = closeadj.pct_change(21).rolling(60, min_periods=50).rank(pct=True)
    rk63 = closeadj.pct_change(63).rolling(126, min_periods=100).rank(pct=True)
    comp = (rk5 + rk21 + rk63 - 1.5)
    sd = comp.rolling(120, min_periods=100).std(ddof=1)
    return (comp / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- AG. Run-length features ------------------------------------------


def f15xm_f15_cross_sectional_momentum_maxruna_120d_base_v127_signal(close):
    """Maximum consecutive up-day run length in last 120d. Discrete max-
    persistence measure."""
    r = close.pct_change()
    flag = (r > 0.0).astype(float).where(~r.isna())
    def _maxr(x):
        m = 0; c = 0
        for v in x:
            if v > 0.5:
                c += 1
                if c > m:
                    m = c
            else:
                c = 0
        return float(m)
    return flag.rolling(120, min_periods=100).apply(_maxr, raw=True).replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_maxrunb_120d_base_v128_signal(close):
    """Maximum consecutive down-day run length in last 120d."""
    r = close.pct_change()
    flag = (r < 0.0).astype(float).where(~r.isna())
    def _maxr(x):
        m = 0; c = 0
        for v in x:
            if v > 0.5:
                c += 1
                if c > m:
                    m = c
            else:
                c = 0
        return float(m)
    return flag.rolling(120, min_periods=100).apply(_maxr, raw=True).replace([np.inf, -np.inf], np.nan)


# --- AH. Sign autocorrelation (momentum persistence) ------------------




# --- AI. Weighted-rank momentum (linear weights) ----------------------


def f15xm_f15_cross_sectional_momentum_wtrnk_60d_base_v130_signal(closeadj):
    """Linearly-time-weighted mean of: rank of daily return vs trailing 60d.
    Recent ranks weight more than older. Distinct from unweighted mean (v060)."""
    rk = closeadj.pct_change().rolling(60, min_periods=50).rank(pct=True)
    w = np.arange(1, 61, dtype=float)
    wsum = w.sum()
    def _wm(x):
        if np.any(~np.isfinite(x)):
            return np.nan
        return float((x * w).sum() / wsum)
    return rk.rolling(60, min_periods=60).apply(_wm, raw=True).replace([np.inf, -np.inf], np.nan)


# --- AJ. Risk-parity-like position rank ------------------------------


def f15xm_f15_cross_sectional_momentum_riskp_120d_base_v131_signal(closeadj):
    """5d return / 5d std of daily returns. Risk-parity inversely-vol-scaled
    momentum at short horizon (uses ATR-free vol). RANK vs trailing 252d."""
    r5 = closeadj.pct_change(5)
    sd = closeadj.pct_change().rolling(5, min_periods=5).std(ddof=1)
    sig = r5 / sd.replace(0.0, np.nan)
    return sig.rolling(252, min_periods=200).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# --- AK. Conditional-return-Sharpe ratio --------------------------------


def f15xm_f15_cross_sectional_momentum_largeret_60d_base_v132_signal(closeadj):
    """Count over 60d of returns whose ABSOLUTE value > trailing-60d-90th-
    percentile of |return|. Tail-event count (non-monotone in level momentum)."""
    r = closeadj.pct_change().abs()
    q90 = r.rolling(60, min_periods=50).quantile(0.9)
    flag = (r > q90).astype(float).where(~q90.isna())
    return flag.rolling(60, min_periods=50).sum().replace([np.inf, -np.inf], np.nan)


# --- AL. Mass-of-distribution above threshold -----------------------


def f15xm_f15_cross_sectional_momentum_above2sd_120d_base_v133_signal(closeadj):
    """Fraction of trailing 120d returns that are > 2 * trailing-120d std.
    Right-tail event fraction — distinct from quantile-based features."""
    r = closeadj.pct_change()
    sd = r.rolling(120, min_periods=100).std(ddof=1)
    flag = (r > 2.0 * sd).astype(float).where(~sd.isna())
    return flag.rolling(120, min_periods=100).mean().replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_below2sd_120d_base_v134_signal(closeadj):
    """Fraction of trailing 120d returns that are < -2 * trailing-120d std.
    Left-tail event fraction."""
    r = closeadj.pct_change()
    sd = r.rolling(120, min_periods=100).std(ddof=1)
    flag = (r < -2.0 * sd).astype(float).where(~sd.isna())
    return flag.rolling(120, min_periods=100).mean().replace([np.inf, -np.inf], np.nan)


# --- AM. Bayesian-style horizon-weighted return ----------------------


def f15xm_f15_cross_sectional_momentum_geoexcess_120d_base_v135_signal(closeadj):
    """log(close/close.shift(63)) MINUS log(close.shift(63)/close.shift(126)).
    Difference between two adjacent 63d log returns — captures whether recent
    momentum exceeds prior period (acceleration in log space)."""
    return (np.log(closeadj) - 2.0 * np.log(closeadj.shift(63)) + np.log(closeadj.shift(126))).replace([np.inf, -np.inf], np.nan)


# --- AN. CAGR vs trailing CAGR ------------------------------------


def f15xm_f15_cross_sectional_momentum_cagrdiff_252d_base_v136_signal(closeadj):
    """Trailing-63d annualized CAGR MINUS trailing-252d annualized CAGR.
    Cross-horizon CAGR differential — captures whether momentum has
    accelerated or decelerated."""
    cagr63 = (np.log(closeadj) - np.log(closeadj.shift(63))) * (252.0 / 63.0)
    cagr252 = np.log(closeadj) - np.log(closeadj.shift(252))
    return (cagr63 - cagr252).replace([np.inf, -np.inf], np.nan)


# --- AO. EWMA-based z-momentum ------------------------------------


def f15xm_f15_cross_sectional_momentum_zewma_252d_base_v137_signal(closeadj):
    """Z-score of 21d return using EWMA(60-span) mean and std of returns.
    Decay-weighted z — different from rolling-mean/std z (v009)."""
    r = closeadj.pct_change(21)
    mu = r.ewm(span=60, adjust=False, min_periods=40).mean()
    sd = r.ewm(span=60, adjust=False, min_periods=40).std(bias=False)
    return ((r - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- AP. Return-vs-volatility quintile-rank ---------------------------


def f15xm_f15_cross_sectional_momentum_volqret_252d_base_v138_signal(closeadj):
    """(Rank of 21d return vs 252d) MINUS (rank of 60d vol vs 252d). High =
    'high-momentum, low-vol' cross-sectional-style anomaly."""
    rkr = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    rkv = closeadj.pct_change().rolling(60, min_periods=50).std(ddof=1).rolling(252, min_periods=200).rank(pct=True)
    return (rkr - rkv).replace([np.inf, -np.inf], np.nan)


# --- AQ. Run-of-rank-buckets ----------------------------------------


def f15xm_f15_cross_sectional_momentum_qmeanrun_60d_base_v139_signal(closeadj):
    """Mean of quintile (1..5) of 21d-return rank-bucket over last 60d.
    Average bucket score — discrete in expectation."""
    rk = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    q = np.ceil(rk * 5.0).clip(lower=1.0, upper=5.0)
    return q.rolling(60, min_periods=40).mean().replace([np.inf, -np.inf], np.nan)


# --- AR. Continuation-vs-reversal indicator -------------------------


def f15xm_f15_cross_sectional_momentum_contrev_60d_base_v140_signal(closeadj):
    """SUM over 60d of: 1 if today's 5d return rank moved closer to 0.5
    (reversion) vs 1 if it moved away (continuation). Rank-momentum-change
    sum — sign encodes continuation/reversal regime."""
    rk = closeadj.pct_change(5).rolling(60, min_periods=50).rank(pct=True)
    dist_now = (rk - 0.5).abs()
    dist_prev = (rk.shift(1) - 0.5).abs()
    inc = (dist_now > dist_prev).astype(float).where(~dist_now.isna() & ~dist_prev.isna())
    dec = (dist_now < dist_prev).astype(float).where(~dist_now.isna() & ~dist_prev.isna())
    return (inc - dec).rolling(60, min_periods=50).sum().replace([np.inf, -np.inf], np.nan)


# --- AS. Zero-crossings of return-z ---------------------------------


def f15xm_f15_cross_sectional_momentum_zerox_252d_base_v141_signal(closeadj):
    """Count over 252d of zero crossings of (21d-return - trailing-252d-mean
    21d-return). Captures momentum-regime stability vs flip count."""
    r = closeadj.pct_change(21)
    centered = r - r.rolling(252, min_periods=200).mean()
    sg = np.sign(centered)
    flip = (sg != sg.shift(1)).astype(float).where(~sg.isna() & ~sg.shift(1).isna())
    return flip.rolling(252, min_periods=200).sum().replace([np.inf, -np.inf], np.nan)


# --- AT. Return-rank deviation from 0.5 -----------------------------


def f15xm_f15_cross_sectional_momentum_rkdev_60d_base_v142_signal(closeadj):
    """|rank(daily return vs 60d) - 0.5|. Extremeness-of-rank (non-monotone in
    return sign). Captures distance from neutral momentum bucket."""
    rk = closeadj.pct_change().rolling(60, min_periods=50).rank(pct=True)
    return (rk - 0.5).abs().replace([np.inf, -np.inf], np.nan)


# --- AU. Conditional-rank-given-positive-return ---------------------


def f15xm_f15_cross_sectional_momentum_condrkpos_120d_base_v143_signal(closeadj):
    """Mean over 120d of: 21d-return rank vs 252d, GIVEN that 21d return > 0.
    Conditional mean rank during up-momentum periods."""
    r = closeadj.pct_change(21)
    rk = r.rolling(252, min_periods=200).rank(pct=True)
    masked = rk.where(r > 0.0)
    return masked.rolling(120, min_periods=20).mean().replace([np.inf, -np.inf], np.nan)


# --- AV. Cross-horizon rank correlation -----------------------------


def f15xm_f15_cross_sectional_momentum_xhcorr_60d_base_v144_signal(closeadj):
    """Pearson correlation between time-series of rk5 and rk21 over 60d.
    Whether short/mid horizon ranks move together."""
    rk5 = closeadj.pct_change(5).rolling(60, min_periods=50).rank(pct=True)
    rk21 = closeadj.pct_change(21).rolling(126, min_periods=100).rank(pct=True)
    mu5 = rk5.rolling(60, min_periods=50).mean()
    mu21 = rk21.rolling(60, min_periods=50).mean()
    cov = (rk5 * rk21).rolling(60, min_periods=50).mean() - mu5 * mu21
    s5 = rk5.rolling(60, min_periods=50).std(ddof=1)
    s21 = rk21.rolling(60, min_periods=50).std(ddof=1)
    return (cov / (s5 * s21).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- AW. Sortino-rank ------------------------------------------------


def f15xm_f15_cross_sectional_momentum_skewp_252d_base_v145_signal(closeadj):
    """Pearson-skew measure: 3*(mean - median) / std of 252d log-returns.
    Distinct from moment skew in base v020 — uses mean-median gap."""
    r = np.log(closeadj).diff()
    mu = r.rolling(252, min_periods=200).mean()
    md = r.rolling(252, min_periods=200).median()
    sd = r.rolling(252, min_periods=200).std(ddof=1)
    return (3.0 * (mu - md) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- AX. Cross-sectional rank-gap -----------------------------------


def f15xm_f15_cross_sectional_momentum_rkgap_5_21_base_v146_signal(closeadj):
    """rank(5d ret vs 60d) - rank(21d ret vs 252d). Short-horizon vs medium-
    horizon rank gap (cross-horizon disagreement)."""
    rk5 = closeadj.pct_change(5).rolling(60, min_periods=50).rank(pct=True)
    rk21 = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    return (rk5 - rk21).replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_rkgap_63_252_base_v147_signal(closeadj):
    """rank(63d ret vs 252d) - rank(252d ret vs 504d). Long-horizon rank gap."""
    rk63 = closeadj.pct_change(63).rolling(252, min_periods=200).rank(pct=True)
    rk252 = closeadj.pct_change(252).rolling(504, min_periods=300).rank(pct=True)
    return (rk63 - rk252).replace([np.inf, -np.inf], np.nan)


# --- AY. Bayesian-blend ranked -----------------------------------------


def f15xm_f15_cross_sectional_momentum_blendrk_252d_base_v148_signal(closeadj):
    """0.7 * rank(252d ret vs 504d) + 0.3 * rank(21d ret vs 252d). Long-
    biased blend rank — different weighting than v135."""
    rk252 = closeadj.pct_change(252).rolling(504, min_periods=300).rank(pct=True)
    rk21 = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    return (0.7 * rk252 + 0.3 * rk21).replace([np.inf, -np.inf], np.nan)


# --- AZ. Trail-min rank distance --------------------------------------


def f15xm_f15_cross_sectional_momentum_minrkdis_252d_base_v149_signal(closeadj):
    """Current 21d-return rank MINUS rolling-min of the 21d-return rank over
    trailing 252d. Distance from worst-rank in window."""
    rk = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    return (rk - rk.rolling(252, min_periods=200).min()).replace([np.inf, -np.inf], np.nan)


# --- BA. Trail-max rank distance --------------------------------------


def f15xm_f15_cross_sectional_momentum_rkrng_120d_base_v150_signal(closeadj):
    """Rolling-MAX MINUS rolling-MIN of 5d-return rank (vs trailing 60d) over
    trailing 120d. Range of rank — non-directional rank-volatility measure."""
    rk = closeadj.pct_change(5).rolling(60, min_periods=50).rank(pct=True)
    return (rk.rolling(120, min_periods=100).max() - rk.rolling(120, min_periods=100).min()).replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f15_cross_sectional_momentum_base_076_150_REGISTRY = {
    "f15xm_f15_cross_sectional_momentum_aboverm_120d_base_v076_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_aboverm_120d_base_v076_signal},
    "f15xm_f15_cross_sectional_momentum_abovemean_252d_base_v077_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_abovemean_252d_base_v077_signal},
    "f15xm_f15_cross_sectional_momentum_aboveewma_60d_base_v078_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_aboveewma_60d_base_v078_signal},
    "f15xm_f15_cross_sectional_momentum_skewlog_60d_base_v079_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_skewlog_60d_base_v079_signal},
    "f15xm_f15_cross_sectional_momentum_kurtlog_60d_base_v080_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_kurtlog_60d_base_v080_signal},
    "f15xm_f15_cross_sectional_momentum_iqr_60d_base_v081_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_iqr_60d_base_v081_signal},
    "f15xm_f15_cross_sectional_momentum_cumupret_60d_base_v082_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_cumupret_60d_base_v082_signal},
    "f15xm_f15_cross_sectional_momentum_dnconc_60d_base_v083_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_dnconc_60d_base_v083_signal},
    "f15xm_f15_cross_sectional_momentum_zeroret_120d_base_v084_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_zeroret_120d_base_v084_signal},
    "f15xm_f15_cross_sectional_momentum_medxr_252d_base_v085_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_medxr_252d_base_v085_signal},
    "f15xm_f15_cross_sectional_momentum_rrk21_252d_base_v086_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_rrk21_252d_base_v086_signal},
    "f15xm_f15_cross_sectional_momentum_rrkstd_252d_base_v087_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_rrkstd_252d_base_v087_signal},
    "f15xm_f15_cross_sectional_momentum_umd9_189d_base_v088_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_umd9_189d_base_v088_signal},
    "f15xm_f15_cross_sectional_momentum_umd3_84d_base_v089_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_umd3_84d_base_v089_signal},
    "f15xm_f15_cross_sectional_momentum_umdcheap_504d_base_v090_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_umdcheap_504d_base_v090_signal},
    "f15xm_f15_cross_sectional_momentum_volofrnk_252d_base_v091_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_volofrnk_252d_base_v091_signal},
    "f15xm_f15_cross_sectional_momentum_volofz_120d_base_v092_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_volofz_120d_base_v092_signal},
    "f15xm_f15_cross_sectional_momentum_lpm_120d_base_v093_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_lpm_120d_base_v093_signal},
    "f15xm_f15_cross_sectional_momentum_upmratio_120d_base_v094_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_upmratio_120d_base_v094_signal},
    "f15xm_f15_cross_sectional_momentum_skipmo_126d_base_v095_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_skipmo_126d_base_v095_signal},
    "f15xm_f15_cross_sectional_momentum_skipmovrnk_252d_base_v096_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_skipmovrnk_252d_base_v096_signal},
    "f15xm_f15_cross_sectional_momentum_ewmaratio_60d_base_v097_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_ewmaratio_60d_base_v097_signal},
    "f15xm_f15_cross_sectional_momentum_topqdays_120d_base_v098_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_topqdays_120d_base_v098_signal},
    "f15xm_f15_cross_sectional_momentum_botqdays_120d_base_v099_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_botqdays_120d_base_v099_signal},
    "f15xm_f15_cross_sectional_momentum_rkmkscore_60d_base_v100_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_rkmkscore_60d_base_v100_signal},
    "f15xm_f15_cross_sectional_momentum_atrnorm_63d_base_v101_signal": {"inputs": ["high", "low", "closeadj"], "func": f15xm_f15_cross_sectional_momentum_atrnorm_63d_base_v101_signal},
    "f15xm_f15_cross_sectional_momentum_signmom_60d_base_v102_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_signmom_60d_base_v102_signal},
    "f15xm_f15_cross_sectional_momentum_winsize_60d_base_v103_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_winsize_60d_base_v103_signal},
    "f15xm_f15_cross_sectional_momentum_pathq_252d_base_v104_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_pathq_252d_base_v104_signal},
    "f15xm_f15_cross_sectional_momentum_state_252d_base_v105_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_state_252d_base_v105_signal},
    "f15xm_f15_cross_sectional_momentum_ddmag_252d_base_v106_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_ddmag_252d_base_v106_signal},
    "f15xm_f15_cross_sectional_momentum_volwret_21d_base_v108_signal": {"inputs": ["close", "volume"], "func": f15xm_f15_cross_sectional_momentum_volwret_21d_base_v108_signal},
    "f15xm_f15_cross_sectional_momentum_volwretrnk_63d_base_v109_signal": {"inputs": ["closeadj", "volume"], "func": f15xm_f15_cross_sectional_momentum_volwretrnk_63d_base_v109_signal},
    "f15xm_f15_cross_sectional_momentum_q90_120d_base_v110_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_q90_120d_base_v110_signal},
    "f15xm_f15_cross_sectional_momentum_q10_120d_base_v111_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_q10_120d_base_v111_signal},
    "f15xm_f15_cross_sectional_momentum_q90q10_120d_base_v112_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_q90q10_120d_base_v112_signal},
    "f15xm_f15_cross_sectional_momentum_persisttrend_60d_base_v113_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_persisttrend_60d_base_v113_signal},
    "f15xm_f15_cross_sectional_momentum_maxddrnk_252d_base_v114_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_maxddrnk_252d_base_v114_signal},
    "f15xm_f15_cross_sectional_momentum_dsbq_252d_base_v115_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_dsbq_252d_base_v115_signal},
    "f15xm_f15_cross_sectional_momentum_dswq_252d_base_v116_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_dswq_252d_base_v116_signal},
    "f15xm_f15_cross_sectional_momentum_xhagree_60d_base_v117_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_xhagree_60d_base_v117_signal},
    "f15xm_f15_cross_sectional_momentum_rcumrnk_60d_base_v118_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_rcumrnk_60d_base_v118_signal},
    "f15xm_f15_cross_sectional_momentum_tailloss_252d_base_v119_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_tailloss_252d_base_v119_signal},
    "f15xm_f15_cross_sectional_momentum_tailgain_252d_base_v120_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_tailgain_252d_base_v120_signal},
    "f15xm_f15_cross_sectional_momentum_geoarith_rnk_252d_base_v121_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_geoarith_rnk_252d_base_v121_signal},
    "f15xm_f15_cross_sectional_momentum_negskewreg_120d_base_v122_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_negskewreg_120d_base_v122_signal},
    "f15xm_f15_cross_sectional_momentum_hilopos_252d_base_v123_signal": {"inputs": ["high", "low", "closeadj"], "func": f15xm_f15_cross_sectional_momentum_hilopos_252d_base_v123_signal},
    "f15xm_f15_cross_sectional_momentum_trendbeta_120d_base_v124_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_trendbeta_120d_base_v124_signal},
    "f15xm_f15_cross_sectional_momentum_accelrnk_60d_base_v125_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_accelrnk_60d_base_v125_signal},
    "f15xm_f15_cross_sectional_momentum_horizoncoh_120d_base_v126_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_horizoncoh_120d_base_v126_signal},
    "f15xm_f15_cross_sectional_momentum_maxruna_120d_base_v127_signal": {"inputs": ["close"], "func": f15xm_f15_cross_sectional_momentum_maxruna_120d_base_v127_signal},
    "f15xm_f15_cross_sectional_momentum_maxrunb_120d_base_v128_signal": {"inputs": ["close"], "func": f15xm_f15_cross_sectional_momentum_maxrunb_120d_base_v128_signal},
    "f15xm_f15_cross_sectional_momentum_wtrnk_60d_base_v130_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_wtrnk_60d_base_v130_signal},
    "f15xm_f15_cross_sectional_momentum_riskp_120d_base_v131_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_riskp_120d_base_v131_signal},
    "f15xm_f15_cross_sectional_momentum_largeret_60d_base_v132_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_largeret_60d_base_v132_signal},
    "f15xm_f15_cross_sectional_momentum_above2sd_120d_base_v133_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_above2sd_120d_base_v133_signal},
    "f15xm_f15_cross_sectional_momentum_below2sd_120d_base_v134_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_below2sd_120d_base_v134_signal},
    "f15xm_f15_cross_sectional_momentum_geoexcess_120d_base_v135_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_geoexcess_120d_base_v135_signal},
    "f15xm_f15_cross_sectional_momentum_cagrdiff_252d_base_v136_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_cagrdiff_252d_base_v136_signal},
    "f15xm_f15_cross_sectional_momentum_zewma_252d_base_v137_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_zewma_252d_base_v137_signal},
    "f15xm_f15_cross_sectional_momentum_volqret_252d_base_v138_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_volqret_252d_base_v138_signal},
    "f15xm_f15_cross_sectional_momentum_qmeanrun_60d_base_v139_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_qmeanrun_60d_base_v139_signal},
    "f15xm_f15_cross_sectional_momentum_contrev_60d_base_v140_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_contrev_60d_base_v140_signal},
    "f15xm_f15_cross_sectional_momentum_zerox_252d_base_v141_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_zerox_252d_base_v141_signal},
    "f15xm_f15_cross_sectional_momentum_rkdev_60d_base_v142_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_rkdev_60d_base_v142_signal},
    "f15xm_f15_cross_sectional_momentum_condrkpos_120d_base_v143_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_condrkpos_120d_base_v143_signal},
    "f15xm_f15_cross_sectional_momentum_xhcorr_60d_base_v144_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_xhcorr_60d_base_v144_signal},
    "f15xm_f15_cross_sectional_momentum_skewp_252d_base_v145_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_skewp_252d_base_v145_signal},
    "f15xm_f15_cross_sectional_momentum_rkgap_5_21_base_v146_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_rkgap_5_21_base_v146_signal},
    "f15xm_f15_cross_sectional_momentum_rkgap_63_252_base_v147_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_rkgap_63_252_base_v147_signal},
    "f15xm_f15_cross_sectional_momentum_blendrk_252d_base_v148_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_blendrk_252d_base_v148_signal},
    "f15xm_f15_cross_sectional_momentum_minrkdis_252d_base_v149_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_minrkdis_252d_base_v149_signal},
    "f15xm_f15_cross_sectional_momentum_rkrng_120d_base_v150_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_rkrng_120d_base_v150_signal},
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
    for name, entry in f15_cross_sectional_momentum_base_076_150_REGISTRY.items():
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
