"""f15_cross_sectional_momentum base features 001-075.

Domain: cross-sectional-style momentum, adapted to single-ticker testing
by ranking each return/momentum signal against the SAME stock's trailing
distribution. Each feature computes a percentile rank, z-score, quintile
bucket, win-rate, streak, distributional moment, or relative-momentum
metric on returns relative to a trailing window. This is the
single-ticker analog of cross-sectional ranking (which normally compares
ONE stock to a universe).

Distinct from f11_raw_roc_family: there we output RAW ROC values. Here
all outputs are normalized / ranked / bounded / discretized relative to
a trailing distribution.

Window > 21 trading days -> use closeadj. Windows <= 21 use close.
Each feature is a fully expanded def. NaN policy: never fillna(0); only
replace([inf,-inf], nan) at return.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _zroll(s: pd.Series, n: int) -> pd.Series:
    mu = s.rolling(n, min_periods=n).mean()
    sd = s.rolling(n, min_periods=n).std(ddof=1)
    return (s - mu) / sd.replace(0.0, np.nan)


def _pct_rank(s: pd.Series, n: int) -> pd.Series:
    return s.rolling(n, min_periods=n).rank(pct=True)


# ---------------------------------------------------------------------------
# Features 001-075
# ---------------------------------------------------------------------------


# --- A. Percentile-rank momentum (single-horizon) ---------------------------


def f15xm_f15_cross_sectional_momentum_pctrnk_252d_base_v001_signal(closeadj):
    """Percentile rank of 21d return vs trailing 252d distribution.
    Cross-sectional-style: how high is current momentum within own history."""
    r = closeadj.pct_change(21)
    return r.rolling(252, min_periods=200).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_pctrnk_126d_base_v002_signal(closeadj):
    """Percentile rank of 5d return vs trailing 126d distribution."""
    r = closeadj.pct_change(5)
    return r.rolling(126, min_periods=100).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_pctrnk_504d_base_v003_signal(closeadj):
    """Percentile rank of 63d return vs trailing 504d distribution.
    Long-horizon momentum rank."""
    r = closeadj.pct_change(63)
    return r.rolling(504, min_periods=300).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_pctrnk_60d_base_v004_signal(close):
    """Percentile rank of 1d return vs trailing 60d. Daily-return rank."""
    r = close.pct_change(1)
    return r.rolling(60, min_periods=50).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_pctrnk_252b_base_v005_signal(closeadj):
    """Percentile rank of 126d return vs trailing 252d. Mid-long-horizon."""
    r = closeadj.pct_change(126)
    return r.rolling(252, min_periods=200).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# --- B. Z-score momentum (vs trailing) --------------------------------------


def f15xm_f15_cross_sectional_momentum_zmom_42d_base_v006_signal(closeadj):
    """Z-score of 42d cumulative log return vs trailing 504d. Mid-long horizon
    z-score — structurally different lookback than v001."""
    r = np.log(closeadj).diff(42)
    mu = r.rolling(504, min_periods=300).mean()
    sd = r.rolling(504, min_periods=300).std(ddof=1)
    return ((r - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_zmom_10d_base_v007_signal(closeadj):
    """Z-score of 10d return vs trailing 60d. Short horizon, short lookback —
    structurally different from v001/v002."""
    r = closeadj.pct_change(10)
    mu = r.rolling(60, min_periods=50).mean()
    sd = r.rolling(60, min_periods=50).std(ddof=1)
    return ((r - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_zmom_189d_base_v008_signal(closeadj):
    """Z-score of 189d return vs trailing 504d (mid-long over long)."""
    r = closeadj.pct_change(189)
    mu = r.rolling(504, min_periods=300).mean()
    sd = r.rolling(504, min_periods=300).std(ddof=1)
    return ((r - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_zlogm_30d_base_v009_signal(closeadj):
    """Z-score of 30d LOG-return vs 90d lookback (different short-long pair)."""
    r = np.log(closeadj).diff(30)
    mu = r.rolling(90, min_periods=70).mean()
    sd = r.rolling(90, min_periods=70).std(ddof=1)
    return ((r - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- C. Quintile / decile / top-bucket flags --------------------------------


def f15xm_f15_cross_sectional_momentum_quint_42d_base_v010_signal(closeadj):
    """Quintile (1..5) of 42d return within trailing 504d distribution.
    Discrete rank — five-bucket momentum score. Mid-horizon return ranked
    against long lookback."""
    r = closeadj.pct_change(42)
    rk = r.rolling(504, min_periods=300).rank(pct=True)
    q = np.ceil(rk * 5.0).clip(lower=1.0, upper=5.0)
    return q.replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_topdec_252d_base_v011_signal(closeadj):
    """Flag: is 21d return in TOP DECILE of trailing 252d (1.0 else 0.0)."""
    r = closeadj.pct_change(21)
    rk = r.rolling(252, min_periods=200).rank(pct=True)
    flag = (rk >= 0.9).astype(float).where(~rk.isna())
    return flag.replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_botdec_252d_base_v012_signal(closeadj):
    """Flag: 21d return in BOTTOM DECILE of trailing 252d."""
    r = closeadj.pct_change(21)
    rk = r.rolling(252, min_periods=200).rank(pct=True)
    flag = (rk <= 0.1).astype(float).where(~rk.isna())
    return flag.replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_topqnt_30d_base_v013_signal(closeadj):
    """Quintile bucket of 30d return vs trailing 360d. Mid-horizon quintile
    at a window not used by other rank features."""
    r = closeadj.pct_change(30)
    rk = r.rolling(360, min_periods=250).rank(pct=True)
    q = np.ceil(rk * 5.0).clip(lower=1.0, upper=5.0)
    return q.replace([np.inf, -np.inf], np.nan)


# --- D. 12-1 momentum (classic UMD style, skip recent month) ----------------


def f15xm_f15_cross_sectional_momentum_umd_252d_base_v014_signal(closeadj):
    """12-1 (UMD) momentum: log return from t-252 to t-21, skipping recent month.
    Classic Jegadeesh-Titman cross-sectional momentum construction.
    Normalized by trailing 252d return std for cross-sectional comparability."""
    r = np.log(closeadj.shift(21)) - np.log(closeadj.shift(252))
    sd = closeadj.pct_change().rolling(252, min_periods=200).std(ddof=1) * np.sqrt(231.0)
    return (r / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_umdrnk_252d_base_v015_signal(closeadj):
    """Rank of 12-1 UMD return vs trailing 252d of UMD values."""
    r = np.log(closeadj.shift(21)) - np.log(closeadj.shift(252))
    return r.rolling(252, min_periods=200).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_umd6_126d_base_v016_signal(closeadj):
    """6-1 momentum: log return from t-126 to t-21. Mid-horizon UMD analog."""
    r = np.log(closeadj.shift(21)) - np.log(closeadj.shift(126))
    sd = closeadj.pct_change().rolling(126, min_periods=100).std(ddof=1) * np.sqrt(105.0)
    return (r / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- E. Risk-adjusted relative strength -------------------------------------


def f15xm_f15_cross_sectional_momentum_sharpe_63d_base_v017_signal(closeadj):
    """Sharpe-like: 63d cumulative log return / 63d log-return stdev.
    Risk-adjusted momentum — distinct from raw ROC."""
    r = np.log(closeadj).diff()
    mu = r.rolling(63, min_periods=50).sum()
    sd = r.rolling(63, min_periods=50).std(ddof=1)
    return (mu / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_sharpe_252d_base_v018_signal(closeadj):
    """Annualized Sharpe-like at 252d: mean return / std on daily log returns."""
    r = np.log(closeadj).diff()
    mu = r.rolling(252, min_periods=200).mean()
    sd = r.rolling(252, min_periods=200).std(ddof=1)
    return (np.sqrt(252.0) * mu / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_sharprng_252d_base_v019_signal(closeadj):
    """Rolling 252d MAX of 20d Sharpe MINUS rolling 252d MIN of 20d Sharpe.
    Range of trailing Sharpe values — captures momentum-regime instability
    distinct from any signed momentum level."""
    r = np.log(closeadj).diff()
    sh20 = r.rolling(20, min_periods=15).sum() / r.rolling(20, min_periods=15).std(ddof=1).replace(0.0, np.nan)
    rng = sh20.rolling(252, min_periods=200).max() - sh20.rolling(252, min_periods=200).min()
    return rng.replace([np.inf, -np.inf], np.nan)


# --- F. Skew / kurt of trailing returns (distributional momentum) -----------


def f15xm_f15_cross_sectional_momentum_skew_120d_base_v020_signal(closeadj):
    """Skewness of trailing 120d log returns. Positive skew is a known
    momentum-related anomaly (lottery-like winners)."""
    r = np.log(closeadj).diff()
    return r.rolling(120, min_periods=100).skew().replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_kurt_120d_base_v021_signal(closeadj):
    """Excess kurtosis of trailing 120d log returns (fat tails)."""
    r = np.log(closeadj).diff()
    return r.rolling(120, min_periods=100).kurt().replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_tailrat_252d_base_v022_signal(closeadj):
    """Tail ratio: mean of top-decile returns / |mean of bottom-decile returns|.
    Captures asymmetry of trailing return distribution."""
    r = np.log(closeadj).diff()
    def _tr(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)):
            return np.nan
        q1 = np.quantile(x, 0.9)
        q2 = np.quantile(x, 0.1)
        top = x[x >= q1].mean()
        bot = x[x <= q2].mean()
        if bot == 0:
            return np.nan
        return float(top / abs(bot))
    return r.rolling(252, min_periods=200).apply(_tr, raw=True).replace([np.inf, -np.inf], np.nan)


# --- G. Win rate / fraction-of-positive features ----------------------------


def f15xm_f15_cross_sectional_momentum_winfrac_60d_base_v023_signal(close):
    """Fraction of last 60 days with positive 1d return. Win rate."""
    r = close.pct_change()
    w = (r > 0.0).astype(float).where(~r.isna())
    return w.rolling(60, min_periods=50).mean().replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_outperf_120d_base_v024_signal(closeadj):
    """Fraction of last 120d where 5d return exceeded its trailing-120d mean.
    Outperformance days vs own average."""
    r = closeadj.pct_change(5)
    mu = r.rolling(120, min_periods=100).mean()
    flag = (r > mu).astype(float).where(~mu.isna())
    return flag.rolling(120, min_periods=100).mean().replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_netwins_252d_base_v025_signal(closeadj):
    """Net winning days: (wins - losses) / total over trailing 252d."""
    r = closeadj.pct_change()
    sg = np.sign(r)
    return sg.rolling(252, min_periods=200).mean().replace([np.inf, -np.inf], np.nan)


# --- H. Streak features -----------------------------------------------------


def f15xm_f15_cross_sectional_momentum_topqstrk_252d_base_v026_signal(closeadj):
    """Length of current consecutive-day streak in top quintile of trailing 252d
    21d-return distribution. Capped at 100."""
    r = closeadj.pct_change(21)
    rk = r.rolling(252, min_periods=200).rank(pct=True)
    flag = (rk >= 0.8).astype(float).where(~rk.isna())
    def _strk(x):
        c = 0
        for v in x[::-1]:
            if v > 0.5:
                c += 1
            else:
                break
        return float(c)
    return flag.rolling(100, min_periods=20).apply(_strk, raw=True).replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_botqstrk_252d_base_v027_signal(closeadj):
    """Length of current bottom-quintile streak of 21d-return percentile.
    Persistent loser indicator."""
    r = closeadj.pct_change(21)
    rk = r.rolling(252, min_periods=200).rank(pct=True)
    flag = (rk <= 0.2).astype(float).where(~rk.isna())
    def _strk(x):
        c = 0
        for v in x[::-1]:
            if v > 0.5:
                c += 1
            else:
                break
        return float(c)
    return flag.rolling(100, min_periods=20).apply(_strk, raw=True).replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_qtrans_60d_base_v028_signal(closeadj):
    """Count of quintile-bucket transitions in last 60 days (instability of
    momentum bucket)."""
    r = closeadj.pct_change(21)
    rk = r.rolling(252, min_periods=200).rank(pct=True)
    q = np.ceil(rk * 5.0).clip(lower=1.0, upper=5.0)
    chg = (q != q.shift(1)).astype(float).where(~q.isna() & ~q.shift(1).isna())
    return chg.rolling(60, min_periods=40).sum().replace([np.inf, -np.inf], np.nan)


# --- I. Excess return over trailing window ----------------------------------


def f15xm_f15_cross_sectional_momentum_exret_3d_base_v029_signal(close):
    """Excess return: current 3d return MINUS trailing-21d-mean 3d-return.
    Very-short-horizon de-meaned momentum — uses `close` (window<=21)."""
    r = close.pct_change(3)
    mu = r.rolling(21, min_periods=15).mean()
    return (r - mu).replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_exretpath_60d_base_v030_signal(closeadj):
    """Current 7d return minus average 7d return over a 60d window — short-horizon
    path-position momentum, on a horizon pair not used elsewhere."""
    r = closeadj.pct_change(7)
    mu = r.rolling(60, min_periods=50).mean()
    return (r - mu).replace([np.inf, -np.inf], np.nan)


# --- J. Long-short return spread (multi-horizon) ----------------------------


def f15xm_f15_cross_sectional_momentum_spread_5_63_base_v031_signal(closeadj):
    """5d return MINUS 63d-average 5d-return. Short minus long-mean spread
    — captures cross-sectional-like deviation of fresh momentum from own mean."""
    r = closeadj.pct_change(5)
    return (r - r.rolling(63, min_periods=50).mean()).replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_spread_q1q5_60d_base_v032_signal(closeadj):
    """Indicator: 1 if 5d-return rank > 0.8 AND 252d-return rank < 0.2,
    -1 if reverse, 0 else. Discrete short-strong / long-weak (or vice versa)
    cross-horizon disagreement state."""
    rk5 = closeadj.pct_change(5).rolling(60, min_periods=50).rank(pct=True)
    rk252 = closeadj.pct_change(252).rolling(504, min_periods=300).rank(pct=True)
    out = pd.Series(0.0, index=closeadj.index)
    out = out.where(rk5.notna() & rk252.notna())
    cond_pos = (rk5 > 0.8) & (rk252 < 0.2)
    cond_neg = (rk5 < 0.2) & (rk252 > 0.8)
    out = out.where(~cond_pos, 1.0)
    out = out.where(~cond_neg, -1.0)
    return out.replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_spread_rnk_252d_base_v033_signal(closeadj):
    """Rank(5d return) MINUS Rank(63d return) — rank-spread reversal/continuation."""
    r5 = closeadj.pct_change(5)
    r63 = closeadj.pct_change(63)
    rk5 = r5.rolling(252, min_periods=200).rank(pct=True)
    rk63 = r63.rolling(252, min_periods=200).rank(pct=True)
    return (rk5 - rk63).replace([np.inf, -np.inf], np.nan)


# --- K. Reversal / continuation -------------------------------------------


def f15xm_f15_cross_sectional_momentum_revdis_252d_base_v034_signal(closeadj):
    """Sign disagreement: sign(5d return) * sign(252d return).
    +1 continuation, -1 reversal regime. Discrete state."""
    s_short = np.sign(closeadj.pct_change(5))
    s_long = np.sign(closeadj.pct_change(252))
    out = s_short * s_long
    return out.where(~s_short.isna() & ~s_long.isna()).replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_strev_zdif_15d_base_v035_signal(close):
    """Short-term reversal: NEGATED z-score of 1d return vs trailing 15d MINUS
    NEGATED z-score of 1d return vs trailing 5d. Cross-window short-reversal
    differential — structurally distinct from any single-window rank."""
    r = close.pct_change(1)
    z15 = (r - r.rolling(15, min_periods=15).mean()) / r.rolling(15, min_periods=15).std(ddof=1).replace(0.0, np.nan)
    z5 = (r - r.rolling(5, min_periods=5).mean()) / r.rolling(5, min_periods=5).std(ddof=1).replace(0.0, np.nan)
    return (-(z15 - z5)).replace([np.inf, -np.inf], np.nan)


# --- L. Bounded transforms --------------------------------------------------


def f15xm_f15_cross_sectional_momentum_arctan_15d_base_v036_signal(close):
    """arctan of (sum of sign(daily ret)) over 15d / sqrt(15). Bounded sign-sum
    transform — short-horizon win-rate signed proxy distinct from any return
    z-score above."""
    r = close.pct_change()
    s = np.sign(r).rolling(15, min_periods=15).sum() / np.sqrt(15.0)
    return np.arctan(s).replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_tanh_top_60d_base_v037_signal(closeadj):
    """tanh of (top-decile flag count over 60d MINUS bottom-decile flag count
    over 60d) using 5d-return rank vs trailing 60d. Sign-asymmetric tail-event
    count — non-monotone in level-momentum, structurally distinct from Sharpe."""
    r = closeadj.pct_change(5)
    rk = r.rolling(60, min_periods=50).rank(pct=True)
    top = (rk >= 0.9).astype(float).where(~rk.isna())
    bot = (rk <= 0.1).astype(float).where(~rk.isna())
    diff = top.rolling(60, min_periods=50).sum() - bot.rolling(60, min_periods=50).sum()
    return np.tanh(diff / 6.0).replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_sigm_rkjmp_252d_base_v038_signal(closeadj):
    """Sigmoid of (rank(21d return vs 252d) - rank(63d return vs 252d)).
    Captures cross-horizon rank disagreement, squashed by sigmoid. Bounded in
    (0,1). Structurally distinct from any single-horizon z/rank."""
    rk21 = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    rk63 = closeadj.pct_change(63).rolling(252, min_periods=200).rank(pct=True)
    d = rk21 - rk63
    return (1.0 / (1.0 + np.exp(-5.0 * d))).replace([np.inf, -np.inf], np.nan)


# --- M. Path / drawdown rank features --------------------------------------


def f15xm_f15_cross_sectional_momentum_drawup_252d_base_v039_signal(closeadj):
    """Maximum drawup over trailing 252d: ratio of close to trailing min.
    Standardized within own trailing distribution by percentile rank."""
    mn = closeadj.rolling(252, min_periods=200).min()
    du = closeadj / mn.replace(0.0, np.nan) - 1.0
    return du.rolling(252, min_periods=200).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_drawdn_252d_base_v040_signal(closeadj):
    """Drawdown rank: (close/trailing-max - 1) ranked within own trailing 252d."""
    mx = closeadj.rolling(252, min_periods=200).max()
    dd = closeadj / mx.replace(0.0, np.nan) - 1.0
    return dd.rolling(252, min_periods=200).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_athgap_120d_base_v041_signal(closeadj):
    """Days since trailing-120d ALL-TIME-HIGH. Path-feature distinct from
    drawup magnitude (v039) — counts the position of the maximum in the window,
    not how far we've recovered. Capped at 120."""
    def _dsah(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)):
            return np.nan
        return float(len(x) - 1 - int(np.argmax(x)))
    return closeadj.rolling(120, min_periods=100).apply(_dsah, raw=True).replace([np.inf, -np.inf], np.nan)


# --- N. Roughness / efficiency relative ratios -----------------------------


def f15xm_f15_cross_sectional_momentum_rough_120d_base_v042_signal(closeadj):
    """Path roughness: sum|return| over 120d / |net return|. Higher = noisier
    path. Inverse of efficiency. Distinct from f01 efficiency by being a RATIO
    structure with rolling sum in numerator."""
    r = closeadj.pct_change()
    num = r.abs().rolling(120, min_periods=100).sum()
    den = (closeadj / closeadj.shift(120) - 1.0).abs()
    return (num / den.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- O. Multi-horizon slope of returns -------------------------------------


def f15xm_f15_cross_sectional_momentum_horizonslp_252d_base_v043_signal(closeadj):
    """Slope of [5,21,63,126,252]-day return RANKS (each ranked vs trailing 252d)
    vs log(horizon). Captures whether SHORT-horizon ranks differ from LONG-horizon
    ranks — a rank-of-rank cross-horizon slope rather than raw return slope."""
    rk5 = closeadj.pct_change(5).rolling(252, min_periods=200).rank(pct=True)
    rk21 = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    rk63 = closeadj.pct_change(63).rolling(252, min_periods=200).rank(pct=True)
    rk126 = closeadj.pct_change(126).rolling(252, min_periods=200).rank(pct=True)
    rk252 = closeadj.pct_change(252).rolling(252, min_periods=200).rank(pct=True)
    lw = np.log(np.array([5.0, 21.0, 63.0, 126.0, 252.0]))
    lw_m = lw.mean()
    den = float(((lw - lw_m) ** 2).sum())
    df = pd.concat([rk5, rk21, rk63, rk126, rk252], axis=1)

    def _row(arr):
        if np.any(~np.isfinite(arr)):
            return np.nan
        y = arr
        ym = y.mean()
        num = float(((lw - lw_m) * (y - ym)).sum())
        return num / den
    out = df.apply(lambda row: _row(row.to_numpy(dtype=float)), axis=1)
    return out.replace([np.inf, -np.inf], np.nan)


# --- P. Volatility-adjusted momentum ---------------------------------------


def f15xm_f15_cross_sectional_momentum_avgabsret_30d_base_v044_signal(closeadj):
    """30d mean of |daily log return| divided by trailing-252d mean of |daily
    log return|. Volatility-of-momentum RATIO (not directional) — captures
    momentum CROWD-trading via abnormal activity, ranked against own normal."""
    r = np.log(closeadj).diff().abs()
    cur = r.rolling(30, min_periods=25).mean()
    base = r.rolling(252, min_periods=200).mean()
    return (cur / base.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_volnormatr_30d_base_v045_signal(high, low, closeadj):
    """30d cumulative log return divided by 30d ATR-normalized vol (sum of |H-L|).
    Path-adjusted momentum using OHLC range."""
    r = np.log(closeadj).diff(30)
    atr = (high - low).rolling(30, min_periods=25).mean() / closeadj
    return (r / atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- Q. Rolling Mann-Kendall S of returns (rank-based trend) ----------------


def f15xm_f15_cross_sectional_momentum_mks_60d_base_v046_signal(closeadj):
    """Mann-Kendall S statistic on 60d log-return series, normalized.
    Rank-style monotonic trend strength on relative-return path."""
    n = 60
    r = np.log(closeadj).diff()
    norm = n * (n - 1) / 2.0

    def _mk(x):
        if np.any(~np.isfinite(x)):
            return np.nan
        s = 0
        for i in range(n - 1):
            d = x[i + 1:] - x[i]
            s += int(np.sum(d > 0) - np.sum(d < 0))
        return s / norm
    return r.rolling(n, min_periods=n).apply(_mk, raw=True).replace([np.inf, -np.inf], np.nan)


# --- R. Maximum / minimum of rolling rank streaks --------------------------


def f15xm_f15_cross_sectional_momentum_timeintop_252d_base_v047_signal(closeadj):
    """Fraction of last 252 days where 21d return was in TOP DECILE of own
    trailing 252d distribution. Persistence of top-rank status."""
    r = closeadj.pct_change(21)
    rk = r.rolling(252, min_periods=200).rank(pct=True)
    flag = (rk >= 0.9).astype(float).where(~rk.isna())
    return flag.rolling(252, min_periods=200).mean().replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_timeinbot_252d_base_v048_signal(closeadj):
    """Fraction of last 252d where 21d return was in BOTTOM DECILE."""
    r = closeadj.pct_change(21)
    rk = r.rolling(252, min_periods=200).rank(pct=True)
    flag = (rk <= 0.1).astype(float).where(~rk.isna())
    return flag.rolling(252, min_periods=200).mean().replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_decnet_252d_base_v049_signal(closeadj):
    """Top-decile-days MINUS bottom-decile-days over 252d (net persistence)."""
    r = closeadj.pct_change(21)
    rk = r.rolling(252, min_periods=200).rank(pct=True)
    top = (rk >= 0.9).astype(float).where(~rk.isna())
    bot = (rk <= 0.1).astype(float).where(~rk.isna())
    return (top - bot).rolling(252, min_periods=200).sum().replace([np.inf, -np.inf], np.nan)


# --- S. Days-since features --------------------------------------------------


def f15xm_f15_cross_sectional_momentum_dssup_252d_base_v050_signal(closeadj):
    """Days since 21d-return percentile was last in TOP DECILE, capped at 252."""
    r = closeadj.pct_change(21)
    rk = r.rolling(252, min_periods=200).rank(pct=True)
    flag = (rk >= 0.9).astype(float).where(~rk.isna())
    def _dsince(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return 252.0
        return float(len(x) - 1 - idx[-1])
    return flag.rolling(252, min_periods=200).apply(_dsince, raw=True).replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_dssdn_252d_base_v051_signal(closeadj):
    """Days since 21d-return percentile was last in BOTTOM DECILE."""
    r = closeadj.pct_change(21)
    rk = r.rolling(252, min_periods=200).rank(pct=True)
    flag = (rk <= 0.1).astype(float).where(~rk.isna())
    def _dsince(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return 252.0
        return float(len(x) - 1 - idx[-1])
    return flag.rolling(252, min_periods=200).apply(_dsince, raw=True).replace([np.inf, -np.inf], np.nan)


# --- T. Risk-adjusted relative strength ratios -----------------------------


def f15xm_f15_cross_sectional_momentum_rkretvol_252d_base_v052_signal(closeadj):
    """Rank(21d return) divided by Rank(60d return-vol). Both ranks vs trailing 252d.
    High = strong, low-vol momentum (relative-strength-like)."""
    r = closeadj.pct_change(21)
    v = closeadj.pct_change().rolling(60, min_periods=50).std(ddof=1)
    rkr = r.rolling(252, min_periods=200).rank(pct=True)
    rkv = v.rolling(252, min_periods=200).rank(pct=True)
    return (rkr / (rkv + 0.05)).replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_idiosig_252d_base_v053_signal(closeadj):
    """Idio-momentum proxy: residual from log(closeadj) regressed on time over 252d,
    standardized by residual std. Captures price drift NOT explained by linear time."""
    def _calc(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)):
            return np.nan
        n = len(x)
        t = np.arange(n, dtype=float)
        tm = t.mean(); xm = x.mean()
        slp = float(((t - tm) * (x - xm)).sum() / ((t - tm) ** 2).sum())
        resid = x - (xm + slp * (t - tm))
        sd = resid.std(ddof=1)
        if sd <= 0:
            return np.nan
        return float(resid[-1] / sd)
    return np.log(closeadj).rolling(252, min_periods=200).apply(_calc, raw=True).replace([np.inf, -np.inf], np.nan)


# --- U. Persistent winner/loser state encoding -----------------------------


def f15xm_f15_cross_sectional_momentum_perswinr_252d_base_v054_signal(closeadj):
    """+1 if last 60d had top-quintile-bucket more often than bottom, -1 else,
    0 in transitions. Discrete persistent winner indicator."""
    r = closeadj.pct_change(21)
    rk = r.rolling(252, min_periods=200).rank(pct=True)
    q = np.ceil(rk * 5.0).clip(lower=1.0, upper=5.0)
    top = (q >= 5.0).astype(float).where(~q.isna())
    bot = (q <= 1.0).astype(float).where(~q.isna())
    t60 = top.rolling(60, min_periods=50).sum()
    b60 = bot.rolling(60, min_periods=50).sum()
    return np.sign(t60 - b60).replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_qjump_60d_base_v055_signal(closeadj):
    """Mean |quintile change| per 60d. Uses absolute change in quintile bucket
    — measures MAGNITUDE of bucket jumps (1 vs 4 = 3) not just count. Structurally
    distinct from binary qtrans count in v028."""
    r = closeadj.pct_change(21)
    rk = r.rolling(252, min_periods=200).rank(pct=True)
    q = np.ceil(rk * 5.0).clip(lower=1.0, upper=5.0)
    jmp = (q - q.shift(1)).abs()
    return jmp.rolling(60, min_periods=50).mean().replace([np.inf, -np.inf], np.nan)


# --- V. Multi-horizon rank summaries ---------------------------------------


def f15xm_f15_cross_sectional_momentum_avgrnk_252d_base_v056_signal(closeadj):
    """Average of [5d, 21d, 63d, 252d] return percentile ranks (vs trailing 252d).
    Composite cross-sectional-style score across horizons."""
    rk5 = closeadj.pct_change(5).rolling(252, min_periods=200).rank(pct=True)
    rk21 = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    rk63 = closeadj.pct_change(63).rolling(252, min_periods=200).rank(pct=True)
    rk252 = closeadj.pct_change(252).rolling(252, min_periods=200).rank(pct=True)
    return ((rk5 + rk21 + rk63 + rk252) / 4.0).replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_minrnk_252d_base_v057_signal(closeadj):
    """MIN of [5,21,63,252]-day return ranks. Weakest-horizon rank."""
    rk5 = closeadj.pct_change(5).rolling(252, min_periods=200).rank(pct=True)
    rk21 = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    rk63 = closeadj.pct_change(63).rolling(252, min_periods=200).rank(pct=True)
    rk252 = closeadj.pct_change(252).rolling(252, min_periods=200).rank(pct=True)
    return pd.concat([rk5, rk21, rk63, rk252], axis=1).min(axis=1).replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_maxrnk_252d_base_v058_signal(closeadj):
    """MAX of [5,21,63,252]-day return ranks. Strongest-horizon rank."""
    rk5 = closeadj.pct_change(5).rolling(252, min_periods=200).rank(pct=True)
    rk21 = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    rk63 = closeadj.pct_change(63).rolling(252, min_periods=200).rank(pct=True)
    rk252 = closeadj.pct_change(252).rolling(252, min_periods=200).rank(pct=True)
    return pd.concat([rk5, rk21, rk63, rk252], axis=1).max(axis=1).replace([np.inf, -np.inf], np.nan)


# --- W. Rank dispersion / disagreement -------------------------------------


def f15xm_f15_cross_sectional_momentum_rkdisp_252d_base_v059_signal(closeadj):
    """Std across [5,21,63,252]-day return ranks. High = horizons disagree."""
    rk5 = closeadj.pct_change(5).rolling(252, min_periods=200).rank(pct=True)
    rk21 = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    rk63 = closeadj.pct_change(63).rolling(252, min_periods=200).rank(pct=True)
    rk252 = closeadj.pct_change(252).rolling(252, min_periods=200).rank(pct=True)
    return pd.concat([rk5, rk21, rk63, rk252], axis=1).std(axis=1, ddof=1).replace([np.inf, -np.inf], np.nan)


# --- X. Cumulative return rank features ------------------------------------


def f15xm_f15_cross_sectional_momentum_cumrkmean_60d_base_v060_signal(closeadj):
    """Mean over last 60d of: rank(daily return vs trailing 60d).
    Average daily-return rank — cross-sectional-like average position."""
    r = closeadj.pct_change()
    rk = r.rolling(60, min_periods=50).rank(pct=True)
    return rk.rolling(60, min_periods=50).mean().replace([np.inf, -np.inf], np.nan)


# --- Y. ATR-normalized momentum and ATR-rank ------------------------------


def f15xm_f15_cross_sectional_momentum_matrnk_85d_base_v061_signal(high, low, closeadj):
    """Rank vs trailing 252d of: 85d-return / 85d-ATR. Vol-adjusted momentum rank
    at a unique 85d/252d horizon pair."""
    r = closeadj.pct_change(85)
    prev = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - prev).abs(), (low - prev).abs()], axis=1).max(axis=1)
    atr = tr.rolling(85, min_periods=60).mean()
    ratio = r / atr.replace(0.0, np.nan) * closeadj
    return ratio.rolling(252, min_periods=200).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# --- Z. Win/loss streak counts ---------------------------------------------


def f15xm_f15_cross_sectional_momentum_winstrk_60d_base_v062_signal(close):
    """Current consecutive up-day streak length, capped at 60. Recent-win
    micro-momentum streak (relative to neutral)."""
    r = close.pct_change()
    flag = (r > 0.0).astype(float).where(~r.isna())
    def _strk(x):
        c = 0
        for v in x[::-1]:
            if v > 0.5:
                c += 1
            else:
                break
        return float(c)
    return flag.rolling(60, min_periods=10).apply(_strk, raw=True).replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_losstrk_60d_base_v063_signal(close):
    """Current consecutive down-day streak length, capped at 60."""
    r = close.pct_change()
    flag = (r < 0.0).astype(float).where(~r.isna())
    def _strk(x):
        c = 0
        for v in x[::-1]:
            if v > 0.5:
                c += 1
            else:
                break
        return float(c)
    return flag.rolling(60, min_periods=10).apply(_strk, raw=True).replace([np.inf, -np.inf], np.nan)


# --- AA. Median deviation / robust z -------------------------------------


def f15xm_f15_cross_sectional_momentum_madz_36d_base_v064_signal(closeadj):
    """Robust z-score: (15d return - median 15d return over 36d window) / MAD (36d).
    Outlier-robust standardized momentum at a non-standard 15d/36d pair."""
    r = closeadj.pct_change(15)
    med = r.rolling(36, min_periods=30).median()
    mad = (r - med).abs().rolling(36, min_periods=30).median()
    return ((r - med) / (1.4826 * mad).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f15xm_f15_cross_sectional_momentum_skewret_60d_base_v065_signal(closeadj):
    """Skewness of the trailing distribution of 5d returns over 60d (rolling 60
    of pct_change(5)). Distinct from skew of daily returns (v020). Captures
    distributional asymmetry of overlapping multi-day returns."""
    r5 = closeadj.pct_change(5)
    return r5.rolling(60, min_periods=50).skew().replace([np.inf, -np.inf], np.nan)


# --- AB. Trimmed mean / winsorized momentum --------------------------------


def f15xm_f15_cross_sectional_momentum_trimrnk_170d_base_v066_signal(closeadj):
    """Trimmed (5%-95%) winsorized 170d return percentile rank within 252d.
    Robust ranked momentum at long-mid horizon (different from any other rank
    feature)."""
    r = closeadj.pct_change(170)
    def _wrnk(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)):
            return np.nan
        q05, q95 = np.quantile(x, 0.05), np.quantile(x, 0.95)
        xw = np.clip(x, q05, q95)
        v = xw[-1]
        return float((xw < v).sum() / len(xw))
    return r.rolling(252, min_periods=200).apply(_wrnk, raw=True).replace([np.inf, -np.inf], np.nan)


# --- AC. Sortino-style downside-vol-adjusted return ----------------------


def f15xm_f15_cross_sectional_momentum_sortino_120d_base_v067_signal(closeadj):
    """Sortino-style: 120d cumulative log return / downside std (returns < 0).
    Downside-vol-adjusted momentum."""
    r = np.log(closeadj).diff()
    num = r.rolling(120, min_periods=100).sum()
    neg = r.where(r < 0.0)
    dsd = neg.rolling(120, min_periods=50).std(ddof=1)
    return (num / dsd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- AD. Calmar-style ----------------------------------------------------


def f15xm_f15_cross_sectional_momentum_calmar_252d_base_v068_signal(closeadj):
    """Calmar: 252d log return / 252d max drawdown magnitude.
    Cross-sectional-ranking-style return/drawdown ratio."""
    r = np.log(closeadj).diff(252)
    mx = closeadj.rolling(252, min_periods=200).max()
    dd = (closeadj / mx - 1.0).rolling(252, min_periods=200).min().abs()
    return (r / dd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- AE. Skew-rank (distributional) -----------------------------------------


def f15xm_f15_cross_sectional_momentum_skewrnk_252d_base_v069_signal(closeadj):
    """Percentile rank of 120d skew vs its trailing 252d distribution.
    Captures unusual skew regimes that drive momentum anomalies."""
    r = np.log(closeadj).diff()
    sk = r.rolling(120, min_periods=100).skew()
    return sk.rolling(252, min_periods=200).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# --- AF. Standard-error-of-the-mean adjusted momentum --------------------


def f15xm_f15_cross_sectional_momentum_tstatdiff_120d_base_v070_signal(closeadj):
    """t-stat of 30d daily log-returns MINUS t-stat of 120d daily log-returns.
    Cross-horizon t-stat difference — captures whether SHORT-horizon momentum
    is statistically separating from LONG-horizon momentum."""
    r = np.log(closeadj).diff()
    t30 = np.sqrt(30.0) * r.rolling(30, min_periods=25).mean() / r.rolling(30, min_periods=25).std(ddof=1).replace(0.0, np.nan)
    t120 = np.sqrt(120.0) * r.rolling(120, min_periods=100).mean() / r.rolling(120, min_periods=100).std(ddof=1).replace(0.0, np.nan)
    return (t30 - t120).replace([np.inf, -np.inf], np.nan)


# --- AG. Up/down volatility ratio ----------------------------------------


def f15xm_f15_cross_sectional_momentum_updnvol_252d_base_v071_signal(closeadj):
    """RANK vs trailing 252d of: std(positive 5d-returns)/std(negative 5d-returns)
    over 252d. Asymmetric vol of multi-day returns at a different horizon and
    wrapped by rolling rank — distinct from skew of daily returns (v020)."""
    r = closeadj.pct_change(5)
    up = r.where(r > 0.0)
    dn = r.where(r < 0.0)
    su = up.rolling(252, min_periods=100).std(ddof=1)
    sd = dn.rolling(252, min_periods=100).std(ddof=1)
    ratio = (su / sd.replace(0.0, np.nan))
    return ratio.rolling(252, min_periods=200).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# --- AH. CMO-rank --------------------------------------------------------


def f15xm_f15_cross_sectional_momentum_cmomag_120d_base_v072_signal(closeadj):
    """|CMO(40)| ranked vs trailing 120d of itself. Magnitude (unsigned) of CMO
    captures STRENGTH not direction — non-monotonic in 21d return. Distinct
    from signed-rank-based features above."""
    r = closeadj.diff()
    g = r.where(r > 0.0, 0.0).rolling(40, min_periods=30).sum()
    l = (-r.where(r < 0.0, 0.0)).rolling(40, min_periods=30).sum()
    cmo = 100.0 * (g - l) / (g + l).replace(0.0, np.nan)
    return cmo.abs().rolling(120, min_periods=100).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# --- AI. Beta to lagged self (autocorr-based persistence) ----------------


def f15xm_f15_cross_sectional_momentum_selfbeta_120d_base_v073_signal(closeadj):
    """OLS slope of r_t on r_{t-1} over 120d. Lag-1 autocorr-like beta;
    >0 = momentum-persistent, <0 = mean-revert."""
    r = closeadj.pct_change()
    lr = r.shift(1)
    def _b(arr):
        if np.any(~np.isfinite(arr)):
            return np.nan
        return float(arr[-1])
    # Compute via rolling cov / var:
    mu_x = lr.rolling(120, min_periods=100).mean()
    mu_y = r.rolling(120, min_periods=100).mean()
    cov = (r * lr).rolling(120, min_periods=100).mean() - mu_x * mu_y
    var = (lr * lr).rolling(120, min_periods=100).mean() - mu_x * mu_x
    return (cov / var.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- AJ. Decile sign agreement count -------------------------------------


def f15xm_f15_cross_sectional_momentum_decagree_252d_base_v074_signal(closeadj):
    """Count over 60d of: rank(5d return) and rank(21d return) BOTH in top quintile,
    minus count of BOTH in bottom quintile (signed agreement count)."""
    rk5 = closeadj.pct_change(5).rolling(252, min_periods=200).rank(pct=True)
    rk21 = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    bothtop = ((rk5 >= 0.8) & (rk21 >= 0.8)).astype(float).where(~rk5.isna() & ~rk21.isna())
    bothbot = ((rk5 <= 0.2) & (rk21 <= 0.2)).astype(float).where(~rk5.isna() & ~rk21.isna())
    return (bothtop - bothbot).rolling(60, min_periods=40).sum().replace([np.inf, -np.inf], np.nan)


# --- AK. Bayesian shrinkage of momentum estimate -------------------------


def f15xm_f15_cross_sectional_momentum_shrink_q5q1_252d_base_v075_signal(closeadj):
    """Shrinkage of UMD: (top-quintile flag) - (bottom-quintile flag) applied to
    63d log return, then shrunk by vol weight 252/(252+5*ann_vol). Discrete-flag-
    weighted return — structurally distinct from raw or rank-only features."""
    r = np.log(closeadj).diff(63)
    rk = r.rolling(252, min_periods=200).rank(pct=True)
    flag = (rk >= 0.8).astype(float).where(~rk.isna()) - (rk <= 0.2).astype(float).where(~rk.isna())
    v = closeadj.pct_change().rolling(63, min_periods=50).std(ddof=1) * np.sqrt(252.0)
    w = 252.0 / (252.0 + 5.0 * v)
    return (flag * r * w).replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f15_cross_sectional_momentum_base_001_075_REGISTRY = {
    "f15xm_f15_cross_sectional_momentum_pctrnk_252d_base_v001_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_pctrnk_252d_base_v001_signal},
    "f15xm_f15_cross_sectional_momentum_pctrnk_126d_base_v002_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_pctrnk_126d_base_v002_signal},
    "f15xm_f15_cross_sectional_momentum_pctrnk_504d_base_v003_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_pctrnk_504d_base_v003_signal},
    "f15xm_f15_cross_sectional_momentum_pctrnk_60d_base_v004_signal": {"inputs": ["close"], "func": f15xm_f15_cross_sectional_momentum_pctrnk_60d_base_v004_signal},
    "f15xm_f15_cross_sectional_momentum_pctrnk_252b_base_v005_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_pctrnk_252b_base_v005_signal},
    "f15xm_f15_cross_sectional_momentum_zmom_42d_base_v006_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_zmom_42d_base_v006_signal},
    "f15xm_f15_cross_sectional_momentum_zmom_10d_base_v007_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_zmom_10d_base_v007_signal},
    "f15xm_f15_cross_sectional_momentum_zmom_189d_base_v008_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_zmom_189d_base_v008_signal},
    "f15xm_f15_cross_sectional_momentum_zlogm_30d_base_v009_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_zlogm_30d_base_v009_signal},
    "f15xm_f15_cross_sectional_momentum_quint_42d_base_v010_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_quint_42d_base_v010_signal},
    "f15xm_f15_cross_sectional_momentum_topdec_252d_base_v011_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_topdec_252d_base_v011_signal},
    "f15xm_f15_cross_sectional_momentum_botdec_252d_base_v012_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_botdec_252d_base_v012_signal},
    "f15xm_f15_cross_sectional_momentum_topqnt_30d_base_v013_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_topqnt_30d_base_v013_signal},
    "f15xm_f15_cross_sectional_momentum_umd_252d_base_v014_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_umd_252d_base_v014_signal},
    "f15xm_f15_cross_sectional_momentum_umdrnk_252d_base_v015_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_umdrnk_252d_base_v015_signal},
    "f15xm_f15_cross_sectional_momentum_umd6_126d_base_v016_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_umd6_126d_base_v016_signal},
    "f15xm_f15_cross_sectional_momentum_sharpe_63d_base_v017_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_sharpe_63d_base_v017_signal},
    "f15xm_f15_cross_sectional_momentum_sharpe_252d_base_v018_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_sharpe_252d_base_v018_signal},
    "f15xm_f15_cross_sectional_momentum_sharprng_252d_base_v019_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_sharprng_252d_base_v019_signal},
    "f15xm_f15_cross_sectional_momentum_skew_120d_base_v020_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_skew_120d_base_v020_signal},
    "f15xm_f15_cross_sectional_momentum_kurt_120d_base_v021_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_kurt_120d_base_v021_signal},
    "f15xm_f15_cross_sectional_momentum_tailrat_252d_base_v022_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_tailrat_252d_base_v022_signal},
    "f15xm_f15_cross_sectional_momentum_winfrac_60d_base_v023_signal": {"inputs": ["close"], "func": f15xm_f15_cross_sectional_momentum_winfrac_60d_base_v023_signal},
    "f15xm_f15_cross_sectional_momentum_outperf_120d_base_v024_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_outperf_120d_base_v024_signal},
    "f15xm_f15_cross_sectional_momentum_netwins_252d_base_v025_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_netwins_252d_base_v025_signal},
    "f15xm_f15_cross_sectional_momentum_topqstrk_252d_base_v026_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_topqstrk_252d_base_v026_signal},
    "f15xm_f15_cross_sectional_momentum_botqstrk_252d_base_v027_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_botqstrk_252d_base_v027_signal},
    "f15xm_f15_cross_sectional_momentum_qtrans_60d_base_v028_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_qtrans_60d_base_v028_signal},
    "f15xm_f15_cross_sectional_momentum_exret_3d_base_v029_signal": {"inputs": ["close"], "func": f15xm_f15_cross_sectional_momentum_exret_3d_base_v029_signal},
    "f15xm_f15_cross_sectional_momentum_exretpath_60d_base_v030_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_exretpath_60d_base_v030_signal},
    "f15xm_f15_cross_sectional_momentum_spread_5_63_base_v031_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_spread_5_63_base_v031_signal},
    "f15xm_f15_cross_sectional_momentum_spread_q1q5_60d_base_v032_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_spread_q1q5_60d_base_v032_signal},
    "f15xm_f15_cross_sectional_momentum_spread_rnk_252d_base_v033_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_spread_rnk_252d_base_v033_signal},
    "f15xm_f15_cross_sectional_momentum_revdis_252d_base_v034_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_revdis_252d_base_v034_signal},
    "f15xm_f15_cross_sectional_momentum_strev_zdif_15d_base_v035_signal": {"inputs": ["close"], "func": f15xm_f15_cross_sectional_momentum_strev_zdif_15d_base_v035_signal},
    "f15xm_f15_cross_sectional_momentum_arctan_15d_base_v036_signal": {"inputs": ["close"], "func": f15xm_f15_cross_sectional_momentum_arctan_15d_base_v036_signal},
    "f15xm_f15_cross_sectional_momentum_tanh_top_60d_base_v037_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_tanh_top_60d_base_v037_signal},
    "f15xm_f15_cross_sectional_momentum_sigm_rkjmp_252d_base_v038_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_sigm_rkjmp_252d_base_v038_signal},
    "f15xm_f15_cross_sectional_momentum_drawup_252d_base_v039_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_drawup_252d_base_v039_signal},
    "f15xm_f15_cross_sectional_momentum_drawdn_252d_base_v040_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_drawdn_252d_base_v040_signal},
    "f15xm_f15_cross_sectional_momentum_athgap_120d_base_v041_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_athgap_120d_base_v041_signal},
    "f15xm_f15_cross_sectional_momentum_rough_120d_base_v042_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_rough_120d_base_v042_signal},
    "f15xm_f15_cross_sectional_momentum_horizonslp_252d_base_v043_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_horizonslp_252d_base_v043_signal},
    "f15xm_f15_cross_sectional_momentum_avgabsret_30d_base_v044_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_avgabsret_30d_base_v044_signal},
    "f15xm_f15_cross_sectional_momentum_volnormatr_30d_base_v045_signal": {"inputs": ["high", "low", "closeadj"], "func": f15xm_f15_cross_sectional_momentum_volnormatr_30d_base_v045_signal},
    "f15xm_f15_cross_sectional_momentum_mks_60d_base_v046_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_mks_60d_base_v046_signal},
    "f15xm_f15_cross_sectional_momentum_timeintop_252d_base_v047_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_timeintop_252d_base_v047_signal},
    "f15xm_f15_cross_sectional_momentum_timeinbot_252d_base_v048_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_timeinbot_252d_base_v048_signal},
    "f15xm_f15_cross_sectional_momentum_decnet_252d_base_v049_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_decnet_252d_base_v049_signal},
    "f15xm_f15_cross_sectional_momentum_dssup_252d_base_v050_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_dssup_252d_base_v050_signal},
    "f15xm_f15_cross_sectional_momentum_dssdn_252d_base_v051_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_dssdn_252d_base_v051_signal},
    "f15xm_f15_cross_sectional_momentum_rkretvol_252d_base_v052_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_rkretvol_252d_base_v052_signal},
    "f15xm_f15_cross_sectional_momentum_idiosig_252d_base_v053_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_idiosig_252d_base_v053_signal},
    "f15xm_f15_cross_sectional_momentum_perswinr_252d_base_v054_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_perswinr_252d_base_v054_signal},
    "f15xm_f15_cross_sectional_momentum_qjump_60d_base_v055_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_qjump_60d_base_v055_signal},
    "f15xm_f15_cross_sectional_momentum_avgrnk_252d_base_v056_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_avgrnk_252d_base_v056_signal},
    "f15xm_f15_cross_sectional_momentum_minrnk_252d_base_v057_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_minrnk_252d_base_v057_signal},
    "f15xm_f15_cross_sectional_momentum_maxrnk_252d_base_v058_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_maxrnk_252d_base_v058_signal},
    "f15xm_f15_cross_sectional_momentum_rkdisp_252d_base_v059_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_rkdisp_252d_base_v059_signal},
    "f15xm_f15_cross_sectional_momentum_cumrkmean_60d_base_v060_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_cumrkmean_60d_base_v060_signal},
    "f15xm_f15_cross_sectional_momentum_matrnk_85d_base_v061_signal": {"inputs": ["high", "low", "closeadj"], "func": f15xm_f15_cross_sectional_momentum_matrnk_85d_base_v061_signal},
    "f15xm_f15_cross_sectional_momentum_winstrk_60d_base_v062_signal": {"inputs": ["close"], "func": f15xm_f15_cross_sectional_momentum_winstrk_60d_base_v062_signal},
    "f15xm_f15_cross_sectional_momentum_losstrk_60d_base_v063_signal": {"inputs": ["close"], "func": f15xm_f15_cross_sectional_momentum_losstrk_60d_base_v063_signal},
    "f15xm_f15_cross_sectional_momentum_madz_36d_base_v064_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_madz_36d_base_v064_signal},
    "f15xm_f15_cross_sectional_momentum_skewret_60d_base_v065_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_skewret_60d_base_v065_signal},
    "f15xm_f15_cross_sectional_momentum_trimrnk_170d_base_v066_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_trimrnk_170d_base_v066_signal},
    "f15xm_f15_cross_sectional_momentum_sortino_120d_base_v067_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_sortino_120d_base_v067_signal},
    "f15xm_f15_cross_sectional_momentum_calmar_252d_base_v068_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_calmar_252d_base_v068_signal},
    "f15xm_f15_cross_sectional_momentum_skewrnk_252d_base_v069_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_skewrnk_252d_base_v069_signal},
    "f15xm_f15_cross_sectional_momentum_tstatdiff_120d_base_v070_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_tstatdiff_120d_base_v070_signal},
    "f15xm_f15_cross_sectional_momentum_updnvol_252d_base_v071_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_updnvol_252d_base_v071_signal},
    "f15xm_f15_cross_sectional_momentum_cmomag_120d_base_v072_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_cmomag_120d_base_v072_signal},
    "f15xm_f15_cross_sectional_momentum_selfbeta_120d_base_v073_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_selfbeta_120d_base_v073_signal},
    "f15xm_f15_cross_sectional_momentum_decagree_252d_base_v074_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_decagree_252d_base_v074_signal},
    "f15xm_f15_cross_sectional_momentum_shrink_q5q1_252d_base_v075_signal": {"inputs": ["closeadj"], "func": f15xm_f15_cross_sectional_momentum_shrink_q5q1_252d_base_v075_signal},
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
    for name, entry in f15_cross_sectional_momentum_base_001_075_REGISTRY.items():
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
