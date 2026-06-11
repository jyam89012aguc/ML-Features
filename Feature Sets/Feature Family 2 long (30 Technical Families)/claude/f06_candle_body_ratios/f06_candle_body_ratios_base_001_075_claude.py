"""f06_candle_body_ratios base features 001-075.

Domain: candle body ratios -- geometric relationships of OHLC
WITHIN a single bar (and small-window aggregations thereof).
body   = |close - open|
upper  = high - max(open, close)
lower  = min(open, close) - low
range  = high - low

Every function is a fully expanded def: formula inline, no _core(),
no factory loops. NaN policy: never fillna(0) inside rolling code;
only replace([inf,-inf], nan) at the final return.

On synthetic GBM-like data, body/range typically clusters near 0.25
and rarely exceeds 0.9 or drops below 0.05. Strict discrete pattern
criteria (marubozu>0.95, doji<0.05, engulfing, ...) therefore tend
to produce constant zero. This file prefers CONTINUOUS variants:
rolling means / maxes / percentile-ranks / soft-thresholds of the
underlying body/range, shadow asymmetry, close-position, etc.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Features 001-075
# ---------------------------------------------------------------------------


# --- Group A: body/range -- raw + rolling stats ----------------------------


def f06cb_f06_candle_body_ratios_brrat_1d_base_v001_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Per-bar body/range = |close-open|/(high-low). 0..1."""
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    out = body / rng
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_brmean_10d_base_v002_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """10-bar mean of body/range."""
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    out = r.rolling(10, min_periods=10).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_brmed_21d_base_v003_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-bar median of body/range -- robust mid-term body fullness."""
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    out = r.rolling(21, min_periods=21).median()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_brstd_21d_base_v004_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-bar std of body/range -- variability of body fullness."""
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    out = r.rolling(21, min_periods=21).std()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_br_q25_30d_base_v005_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar 25th-percentile (lower quartile) of body/range -- lower tail of body fullness."""
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    out = r.rolling(30, min_periods=30).quantile(0.25)
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_brskew_30d_base_v006_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar skewness of body/range distribution."""
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    out = r.rolling(30, min_periods=30).skew()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_brmax_10d_base_v007_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max body/range over 10 bars -- continuous marubozu-strength proxy."""
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    out = r.rolling(10, min_periods=10).max()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_brmin_10d_base_v008_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Min body/range over 10 bars -- continuous doji-strength proxy."""
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    out = r.rolling(10, min_periods=10).min()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group B: shadows (upper/lower) ----------------------------------------


def f06cb_f06_candle_body_ratios_upsh_1d_base_v009_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Upper-shadow / range = (high - max(o,c)) / (high - low)."""
    upper = high - np.maximum(open, close)
    rng = (high - low).replace(0.0, np.nan)
    out = upper / rng
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_losh_1d_base_v010_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Lower-shadow / range = (min(o,c) - low) / (high - low)."""
    lower = np.minimum(open, close) - low
    rng = (high - low).replace(0.0, np.nan)
    out = lower / rng
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_shasym_1d_base_v011_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Shadow asymmetry (upper - lower)/(upper + lower)."""
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    den = (upper + lower).replace(0.0, np.nan)
    out = (upper - lower) / den
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_shprod_1d_base_v012_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(upper*lower)/range^2 -- shadow product, nonlinear in shasym.
    Large when both shadows are present (rejection on both sides)."""
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    rng = (high - low).replace(0.0, np.nan)
    out = (upper * lower) / (rng * rng)
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_upbody_1d_base_v013_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """log((upper+eps)/(body+eps)) -- upper-shadow vs body."""
    upper = high - np.maximum(open, close)
    body = (close - open).abs()
    eps = (high - low).abs() * 0.01 + 1e-12
    out = np.log((upper + eps) / (body + eps))
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_lobody_1d_base_v014_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """log((lower+eps)/(body+eps)) -- lower-shadow vs body."""
    lower = np.minimum(open, close) - low
    body = (close - open).abs()
    eps = (high - low).abs() * 0.01 + 1e-12
    out = np.log((lower + eps) / (body + eps))
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_upsh_mean_21d_base_v015_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-bar mean of upper-shadow/range."""
    upper = high - np.maximum(open, close)
    rng = (high - low).replace(0.0, np.nan)
    s = upper / rng
    out = s.rolling(21, min_periods=21).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_losh_mean_21d_base_v016_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-bar mean of lower-shadow/range."""
    lower = np.minimum(open, close) - low
    rng = (high - low).replace(0.0, np.nan)
    s = lower / rng
    out = s.rolling(21, min_periods=21).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_shasym_mean_20d_base_v017_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """20-bar mean of shadow asymmetry -- smoothed wick-bias direction."""
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    den = (upper + lower).replace(0.0, np.nan)
    sa = (upper - lower) / den
    out = sa.rolling(20, min_periods=20).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_shdom_10d_base_v018_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Shadow dominance: max(upper,lower)/(upper+lower), 10-bar mean."""
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    mx = np.maximum(upper, lower)
    den = (upper + lower).replace(0.0, np.nan)
    r = mx / den
    out = r.rolling(10, min_periods=10).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group C: body color / sign / streaks ----------------------------------


def f06cb_f06_candle_body_ratios_bodysign_1d_base_v019_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """sign(close - open). +1/0/-1."""
    out = np.sign(close - open)
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bullstrk_20d_base_v020_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Consecutive bullish-bar streak length (resets on non-bull)."""
    bull = (close > open).astype(int)
    grp = (bull == 0).cumsum()
    cnt = bull.groupby(grp).cumcount() + 1
    out = cnt.where(bull == 1, 0).astype(float)
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bearstrk_20d_base_v021_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Consecutive bearish-bar streak length."""
    bear = (close < open).astype(int)
    grp = (bear == 0).cumsum()
    cnt = bear.groupby(grp).cumcount() + 1
    out = cnt.where(bear == 1, 0).astype(float)
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bullcnt_21d_base_v022_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bullish bars in trailing 21."""
    bull = (close > open).astype(float)
    out = bull.rolling(21, min_periods=21).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bullfrac_63d_base_v023_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Fraction of bullish bars in trailing 63 (window > 21 -> closeadj)."""
    bull = (closeadj > open).astype(float)
    out = bull.rolling(63, min_periods=63).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_colorhom_30d_base_v024_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """|sum(sign(close-open))|/30 -- absolute color homogeneity."""
    s = np.sign(close - open)
    out = s.rolling(30, min_periods=30).sum().abs() / 30.0
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodyalt_30d_base_v025_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Count of body-color flips (sign changes) over 30 bars."""
    s = np.sign(close - open)
    flip = (s.diff().abs() > 0).astype(float)
    out = flip.rolling(30, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bullbearstrkdiff_30d_base_v026_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """(max bull-streak in 30) - (max bear-streak in 30)."""
    bull = (close > open).astype(int)
    bear = (close < open).astype(int)
    grp_bu = (bull == 0).cumsum()
    bu_run = bull.groupby(grp_bu).cumcount() + 1
    bu_run = bu_run.where(bull == 1, 0)
    grp_be = (bear == 0).cumsum()
    be_run = bear.groupby(grp_be).cumcount() + 1
    be_run = be_run.where(bear == 1, 0)
    mx_bu = bu_run.rolling(30, min_periods=30).max()
    mx_be = be_run.rolling(30, min_periods=30).max()
    out = (mx_bu - mx_be).astype(float)
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_3bar_str_3d_base_v027_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """3-bar bull/bear sum of sign(close-open). Range -3..+3."""
    s = np.sign(close - open)
    out = s.rolling(3, min_periods=3).sum()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group D: close-position-in-bar -----------------------------------------






def f06cb_f06_candle_body_ratios_clpos_mean_10d_base_v030_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """10-bar mean of close-position-in-bar."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = cp.rolling(10, min_periods=10).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_clpos_var_30d_base_v031_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar variance of close-position-in-bar. Dispersion statistic
    structurally orthogonal to current level."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = cp.rolling(30, min_periods=30).var()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_clpos_skew_30d_base_v032_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Skewness of close-position-in-bar over 30 bars."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = cp.rolling(30, min_periods=30).skew()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_clpos_asym_30d_base_v033_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(#close>0.7 - #close<0.3)/30 -- close-bias signed."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    hi = (cp > 0.7).astype(float).rolling(30, min_periods=30).sum()
    lo = (cp < 0.3).astype(float).rolling(30, min_periods=30).sum()
    out = (hi - lo) / 30.0
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_clpos_iqr_30d_base_v034_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """IQR (q75 - q25) of close-position-in-bar over 30 bars."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    q75 = cp.rolling(30, min_periods=30).quantile(0.75)
    q25 = cp.rolling(30, min_periods=30).quantile(0.25)
    out = q75 - q25
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_oppos_var_30d_base_v035_signal(open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """30-bar variance of open-position-in-bar. Open-position dispersion."""
    rng = (high - low).replace(0.0, np.nan)
    op = (open - low) / rng
    out = op.rolling(30, min_periods=30).var()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group E: body size dynamics -------------------------------------------


def f06cb_f06_candle_body_ratios_bodysz_1d_base_v036_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Normalized body size: |close-open|/close (per bar)."""
    body = (close - open).abs()
    out = body / close.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodysz_avg_21d_base_v037_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """21-bar mean of |closeadj-open|/closeadj."""
    body = (closeadj - open).abs()
    n = body / closeadj.replace(0.0, np.nan)
    out = n.rolling(21, min_periods=21).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodysz_ema_diff_30d_base_v038_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """log(EMA5(body)/EMA30(body)) -- short-vs-long body magnitude ratio (signed).
    Distinct in structure from rolling-z (mean-and-std based)."""
    body = (closeadj - open).abs()
    e5 = body.ewm(span=5, adjust=False, min_periods=5).mean().replace(0.0, np.nan)
    e30 = body.ewm(span=30, adjust=False, min_periods=30).mean().replace(0.0, np.nan)
    out = np.log(e5 / e30)
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodysz_rnk_60d_base_v039_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Percentile rank of body magnitude in trailing 60 bars."""
    body = (closeadj - open).abs()
    out = body.rolling(60, min_periods=30).rank(pct=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodysz_z_30d_base_v040_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Z-score of body magnitude over 30 bars."""
    body = (closeadj - open).abs()
    mu = body.rolling(30, min_periods=30).mean()
    sd = body.rolling(30, min_periods=30).std().replace(0.0, np.nan)
    out = (body - mu) / sd
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodysz_slp_10d_base_v041_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """10-bar slope of body magnitude: body.diff(5)/mean(body,10)."""
    body = (close - open).abs()
    mu = body.rolling(10, min_periods=10).mean().replace(0.0, np.nan)
    out = body.diff(5) / mu
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_signbody_30d_base_v042_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar mean of signed body (close-open)/close."""
    sb = (close - open) / close.replace(0.0, np.nan)
    out = sb.rolling(30, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_sgnbody_z_30d_base_v043_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of signed body (close-open)/close over 30 bars."""
    sb = (close - open) / close.replace(0.0, np.nan)
    mu = sb.rolling(30, min_periods=30).mean()
    sd = sb.rolling(30, min_periods=30).std().replace(0.0, np.nan)
    out = (sb - mu) / sd
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodyslp_20d_base_v044_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """OLS slope of body magnitudes over last 20 bars (body trend)."""
    body = (close - open).abs()
    n = 20
    x = np.arange(n, dtype=float)
    xm = x.mean()
    xv = ((x - xm) ** 2).sum()
    def _slope(y):
        ym = y.mean()
        return float(((x - xm) * (y - ym)).sum() / xv)
    out = body.rolling(n, min_periods=n).apply(_slope, raw=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodyvar_30d_base_v045_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Coefficient of variation of body magnitude over 30 bars."""
    body = (close - open).abs()
    mu = body.rolling(30, min_periods=30).mean().replace(0.0, np.nan)
    sd = body.rolling(30, min_periods=30).std()
    out = sd / mu
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group F: discrete-pattern proxies as CONTINUOUS scores ----------------


def f06cb_f06_candle_body_ratios_hammer_sc_1d_base_v046_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Discrete hammer score: 1 when lower/range > 2*upper/range AND body/range < 0.5,
    0 otherwise. A pattern indicator distinct from raw shadow ratios.
    On synthetic GBM this captures a small but non-zero fraction of bars."""
    body = (close - open).abs()
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    rng = (high - low).replace(0.0, np.nan)
    cond = (lower > 2.0 * upper) & ((body / rng) < 0.5)
    out = cond.astype(float)
    out[rng.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_invhammer_sc_1d_base_v047_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Discrete inverted-hammer score: 1 when upper > 2*lower AND body/range < 0.5,
    0 otherwise."""
    body = (close - open).abs()
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    rng = (high - low).replace(0.0, np.nan)
    cond = (upper > 2.0 * lower) & ((body / rng) < 0.5)
    out = cond.astype(float)
    out[rng.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_doji_sc_1d_base_v048_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Continuous doji-strength = -log(body/range + 0.01). Large when body small."""
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    out = -np.log(r + 0.01)
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_spintop_sc_1d_base_v049_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Spinning-top continuous: balanced shadows * small body =
    (1 - |upper-lower|/(upper+lower)) * (1 - body/range)."""
    body = (close - open).abs()
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    rng = (high - low).replace(0.0, np.nan)
    den = (upper + lower).replace(0.0, np.nan)
    balance = 1.0 - (upper - lower).abs() / den
    smallbody = 1.0 - body / rng
    out = balance * smallbody
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_engulf_sc_1d_base_v050_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Continuous engulfing strength: signed log(body / prev body) where
    today and yesterday have OPPOSITE colors, else 0. Positive = bull-engulf."""
    body = (close - open).abs()
    pb = body.shift(1)
    sign_today = np.sign(close - open)
    sign_prev = np.sign((close - open).shift(1))
    opp = (sign_today * sign_prev) < 0
    eps = body.rolling(20, min_periods=10).mean() * 0.05 + 1e-12
    score = sign_today * np.log((body + eps) / (pb + eps))
    out = score.where(opp, 0.0)
    out[pb.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_piercing_sc_1d_base_v051_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Piercing/darkcloud continuous: how deep today's close penetrates
    prev body, signed by color reversal.
    score = (close - prev_mid) / |prev_body|, masked to color reversal."""
    prev_open = open.shift(1)
    prev_close = close.shift(1)
    prev_mid = (prev_open + prev_close) * 0.5
    prev_body = (prev_close - prev_open).abs()
    sign_today = np.sign(close - open)
    sign_prev = np.sign(prev_close - prev_open)
    opp = (sign_today * sign_prev) < 0
    pb = prev_body.replace(0.0, np.nan)
    score = (close - prev_mid) / pb
    out = score.where(opp, 0.0)
    out[prev_open.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_engulfnet_30d_base_v052_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar sum of continuous engulfing score (Group F's v050 aggregated)."""
    body = (close - open).abs()
    pb = body.shift(1)
    sign_today = np.sign(close - open)
    sign_prev = np.sign((close - open).shift(1))
    opp = (sign_today * sign_prev) < 0
    eps = body.rolling(20, min_periods=10).mean() * 0.05 + 1e-12
    score = sign_today * np.log((body + eps) / (pb + eps))
    sc = score.where(opp, 0.0)
    sc[pb.isna()] = np.nan
    out = sc.rolling(30, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group G: range dynamics -----------------------------------------------


def f06cb_f06_candle_body_ratios_rngprev_1d_base_v053_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """log(range / prior range)."""
    rng = (high - low)
    pr = rng.shift(1).replace(0.0, np.nan)
    out = np.log((rng + 1e-12) / (pr + 1e-12))
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_rngexp_20d_base_v054_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """range / 20d-mean range. >1 = expanding."""
    rng = (high - low)
    mu = rng.rolling(20, min_periods=20).mean().replace(0.0, np.nan)
    out = rng / mu
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_rngrnk_60d_base_v055_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of current range in trailing 60 bars."""
    rng = (high - low)
    out = rng.rolling(60, min_periods=30).rank(pct=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_rngnorm_30d_base_v056_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar mean of (range/close). Typical normalized range size."""
    rng = (high - low) / close.replace(0.0, np.nan)
    out = rng.rolling(30, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_rngprev_mean_21d_base_v057_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """21-bar mean of log(range/prior range). Mean expand/contract bias."""
    rng = (high - low)
    pr = rng.shift(1).replace(0.0, np.nan)
    lr = np.log((rng + 1e-12) / (pr + 1e-12))
    out = lr.rolling(21, min_periods=21).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_rng_logvar_30d_base_v058_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """log(30-bar variance of range/closeadj). Scale-statistic, structurally distinct
    from range-vs-baseline ratio."""
    rng = (high - low) / closeadj.replace(0.0, np.nan)
    v = rng.rolling(30, min_periods=30).var().replace(0.0, np.nan)
    out = np.log(v)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group H: shape index / bounded transforms / asymmetries ---------------


def f06cb_f06_candle_body_ratios_shape_idx_1d_base_v059_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """arctan((upper - lower) / (body + 0.001*range)). Bounded shadow imbalance scaled by body."""
    rng = (high - low)
    body = (close - open).abs() + rng * 0.001
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    out = np.arctan((upper - lower) / body.replace(0.0, np.nan))
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_br_ac1_30d_base_v060_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar lag-1 autocorrelation of body/range -- tests persistence of body-fullness regime,
    structurally orthogonal to brrat level/dispersion."""
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    out = r.rolling(30, min_periods=30).corr(r.shift(1))
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_brsig_30d_base_v061_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Body/range signal-to-noise: mean / std over 30 bars."""
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    mu = r.rolling(30, min_periods=30).mean()
    sd = r.rolling(30, min_periods=30).std().replace(0.0, np.nan)
    out = mu / sd
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_wickbody_30d_base_v062_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar mean of (upper+lower-body)/range -- wick-vs-body bias."""
    body = (close - open).abs()
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    rng = (high - low).replace(0.0, np.nan)
    s = (upper + lower - body) / rng
    out = s.rolling(30, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_wickbody_iqr_30d_base_v063_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """IQR (q75-q25) of body/range over 30 bars."""
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    q75 = r.rolling(30, min_periods=30).quantile(0.75)
    q25 = r.rolling(30, min_periods=30).quantile(0.25)
    out = q75 - q25
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_brkurt_60d_base_v064_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Kurtosis of body/range over 60 bars."""
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    out = r.rolling(60, min_periods=60).kurt()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodyup_dom_30d_base_v065_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of bars in 30 where upper > lower."""
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    cond = (upper > lower).astype(float)
    out = cond.rolling(30, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group I: open-gap-vs-prior-close internals (intra-bar context) --------


def f06cb_f06_candle_body_ratios_openpos_pc_1d_base_v066_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(open - prev_close)/range -- how far today's open is from prev close, relative to today's range."""
    rng = (high - low).replace(0.0, np.nan)
    pc = close.shift(1)
    out = (open - pc) / rng
    out[pc.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_clvopen_pc_1d_base_v067_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """(close - open) / (|close - prev_close| + eps). Intra-bar share of total move."""
    pc = close.shift(1)
    tot = (close - pc).abs()
    eps = close.rolling(10, min_periods=5).std() * 0.01 + 1e-12
    out = (close - open) / (tot + eps)
    return out.replace([np.inf, -np.inf], np.nan)


# --- Group J: extra differentiators ---------------------------------------


def f06cb_f06_candle_body_ratios_brspread_60d_base_v068_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(short brmean - long brmean): 5-bar minus 60-bar mean of body/range.
    Differential of body fullness across timescales."""
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    s5 = r.rolling(5, min_periods=5).mean()
    s60 = r.rolling(60, min_periods=60).mean()
    out = s5 - s60
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_shasym_var_30d_base_v069_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar variance of shadow-asymmetry. Variability statistic orthogonal to level."""
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    den = (upper + lower).replace(0.0, np.nan)
    sa = (upper - lower) / den
    out = sa.rolling(30, min_periods=30).var()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_avgshlen_21d_base_v070_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-bar mean of (upper+lower)/close -- total shadow length normalized."""
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    s = (upper + lower) / close.replace(0.0, np.nan)
    out = s.rolling(21, min_periods=21).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_hammer_cnt_60d_base_v071_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """60-bar count of discrete hammers (lower > 2*upper AND body/range < 0.5)."""
    body = (close - open).abs()
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    rng = (high - low).replace(0.0, np.nan)
    cond = ((lower > 2.0 * upper) & ((body / rng) < 0.5)).astype(float)
    out = cond.rolling(60, min_periods=60).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_dojistr_30d_base_v072_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar mean of doji-strength score -log(body/range + 0.01)."""
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    ds = -np.log(r + 0.01)
    out = ds.rolling(30, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_upshmlosh_30d_base_v073_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar mean of (upper - lower)/close -- net wick-direction in price units."""
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    s = (upper - lower) / close.replace(0.0, np.nan)
    out = s.rolling(30, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodyrng_corr_30d_base_v074_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar rolling corr between body magnitude and total range.
    Captures whether wide bars also have big bodies (a strong-conviction regime)."""
    body = (close - open).abs()
    rng = (high - low)
    out = body.rolling(30, min_periods=30).corr(rng)
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_signbodyrng_50d_base_v075_signal(open: pd.Series, high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """50-bar mean of (close - open)/range -- signed body-over-range, smoothed.
    (window > 21 -> closeadj for the close side)."""
    rng = (high - low).replace(0.0, np.nan)
    sbr = (closeadj - open) / rng
    out = sbr.rolling(50, min_periods=50).mean()
    return out.replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


def _e(fn, *inputs):
    return fn.__name__, {"inputs": list(inputs), "func": fn}


f06_candle_body_ratios_base_001_075_REGISTRY = dict([
    _e(f06cb_f06_candle_body_ratios_brrat_1d_base_v001_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_brmean_10d_base_v002_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_brmed_21d_base_v003_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_brstd_21d_base_v004_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_br_q25_30d_base_v005_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_brskew_30d_base_v006_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_brmax_10d_base_v007_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_brmin_10d_base_v008_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_upsh_1d_base_v009_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_losh_1d_base_v010_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_shasym_1d_base_v011_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_shprod_1d_base_v012_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_upbody_1d_base_v013_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_lobody_1d_base_v014_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_upsh_mean_21d_base_v015_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_losh_mean_21d_base_v016_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_shasym_mean_20d_base_v017_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_shdom_10d_base_v018_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_bodysign_1d_base_v019_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_bullstrk_20d_base_v020_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_bearstrk_20d_base_v021_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_bullcnt_21d_base_v022_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_bullfrac_63d_base_v023_signal, "open", "closeadj"),
    _e(f06cb_f06_candle_body_ratios_colorhom_30d_base_v024_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_bodyalt_30d_base_v025_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_bullbearstrkdiff_30d_base_v026_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_3bar_str_3d_base_v027_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_clpos_mean_10d_base_v030_signal, "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_clpos_var_30d_base_v031_signal, "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_clpos_skew_30d_base_v032_signal, "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_clpos_asym_30d_base_v033_signal, "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_clpos_iqr_30d_base_v034_signal, "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_oppos_var_30d_base_v035_signal, "open", "high", "low"),
    _e(f06cb_f06_candle_body_ratios_bodysz_1d_base_v036_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_bodysz_avg_21d_base_v037_signal, "open", "closeadj"),
    _e(f06cb_f06_candle_body_ratios_bodysz_ema_diff_30d_base_v038_signal, "open", "closeadj"),
    _e(f06cb_f06_candle_body_ratios_bodysz_rnk_60d_base_v039_signal, "open", "closeadj"),
    _e(f06cb_f06_candle_body_ratios_bodysz_z_30d_base_v040_signal, "open", "closeadj"),
    _e(f06cb_f06_candle_body_ratios_bodysz_slp_10d_base_v041_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_signbody_30d_base_v042_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_sgnbody_z_30d_base_v043_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_bodyslp_20d_base_v044_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_bodyvar_30d_base_v045_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_hammer_sc_1d_base_v046_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_invhammer_sc_1d_base_v047_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_doji_sc_1d_base_v048_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_spintop_sc_1d_base_v049_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_engulf_sc_1d_base_v050_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_piercing_sc_1d_base_v051_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_engulfnet_30d_base_v052_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_rngprev_1d_base_v053_signal, "high", "low"),
    _e(f06cb_f06_candle_body_ratios_rngexp_20d_base_v054_signal, "high", "low"),
    _e(f06cb_f06_candle_body_ratios_rngrnk_60d_base_v055_signal, "high", "low"),
    _e(f06cb_f06_candle_body_ratios_rngnorm_30d_base_v056_signal, "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_rngprev_mean_21d_base_v057_signal, "high", "low"),
    _e(f06cb_f06_candle_body_ratios_rng_logvar_30d_base_v058_signal, "high", "low", "closeadj"),
    _e(f06cb_f06_candle_body_ratios_shape_idx_1d_base_v059_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_br_ac1_30d_base_v060_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_brsig_30d_base_v061_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_wickbody_30d_base_v062_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_wickbody_iqr_30d_base_v063_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_brkurt_60d_base_v064_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_bodyup_dom_30d_base_v065_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_openpos_pc_1d_base_v066_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_clvopen_pc_1d_base_v067_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_brspread_60d_base_v068_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_shasym_var_30d_base_v069_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_avgshlen_21d_base_v070_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_hammer_cnt_60d_base_v071_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_dojistr_30d_base_v072_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_upshmlosh_30d_base_v073_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_bodyrng_corr_30d_base_v074_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_signbodyrng_50d_base_v075_signal, "open", "high", "low", "closeadj"),
])


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
    for name, entry in f06_candle_body_ratios_base_001_075_REGISTRY.items():
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
