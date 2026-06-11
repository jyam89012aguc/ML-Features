"""f06_candle_body_ratios slope features 001-150 (1st derivative).

Each slope feature is the 1st mathematical derivative of its base
counterpart: B(t) -> B.diff(k). ROC bracket rule:
  base window <= 5d   -> k = 5
  base window 6-21d   -> k = 5 or 10
  base window 22-63d  -> k = 10 or 21
  base window 64-200d -> k = 21 or 63
  base window > 200d  -> k = 63

Every function is a fully expanded def: base formula re-computed inline
(no calls into the base file), then .diff(k) at the end. NaN policy:
never fillna(0); only replace([inf,-inf], nan) at return. Windows > 21d
use closeadj (matching the base counterpart). 1:1 mapping with v001..v150.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# -- v001..v018: body/range and shadow primitives (single-bar, k=5) ----------


def f06cb_f06_candle_body_ratios_brrat_1d_slope_v001_signal(open, high, low, close):
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    base = body / rng
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_brmean_10d_slope_v002_signal(open, high, low, close):
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    base = r.rolling(10, min_periods=10).mean()
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_brmed_21d_slope_v003_signal(open, high, low, close):
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    base = r.rolling(21, min_periods=21).median()
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_brstd_21d_slope_v004_signal(open, high, low, close):
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    base = r.rolling(21, min_periods=21).std()
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_br_q25_30d_slope_v005_signal(open, high, low, close):
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    base = r.rolling(30, min_periods=30).quantile(0.25)
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_brskew_30d_slope_v006_signal(open, high, low, close):
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    base = r.rolling(30, min_periods=30).skew()
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_brmax_10d_slope_v007_signal(open, high, low, close):
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    base = r.rolling(10, min_periods=10).max()
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_brmin_10d_slope_v008_signal(open, high, low, close):
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    base = r.rolling(10, min_periods=10).min()
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_upsh_1d_slope_v009_signal(open, high, low, close):
    upper = high - np.maximum(open, close)
    rng = (high - low).replace(0.0, np.nan)
    base = upper / rng
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_losh_1d_slope_v010_signal(open, high, low, close):
    lower = np.minimum(open, close) - low
    rng = (high - low).replace(0.0, np.nan)
    base = lower / rng
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_shasym_1d_slope_v011_signal(open, high, low, close):
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    den = (upper + lower).replace(0.0, np.nan)
    base = (upper - lower) / den
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_shprod_1d_slope_v012_signal(open, high, low, close):
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    rng = (high - low).replace(0.0, np.nan)
    base = (upper * lower) / (rng * rng)
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_upbody_1d_slope_v013_signal(open, high, low, close):
    upper = high - np.maximum(open, close)
    body = (close - open).abs()
    eps = (high - low).abs() * 0.01 + 1e-12
    base = np.log((upper + eps) / (body + eps))
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_lobody_1d_slope_v014_signal(open, high, low, close):
    lower = np.minimum(open, close) - low
    body = (close - open).abs()
    eps = (high - low).abs() * 0.01 + 1e-12
    base = np.log((lower + eps) / (body + eps))
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_upsh_mean_21d_slope_v015_signal(open, high, low, close):
    upper = high - np.maximum(open, close)
    rng = (high - low).replace(0.0, np.nan)
    s = upper / rng
    base = s.rolling(21, min_periods=21).mean()
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_losh_mean_21d_slope_v016_signal(open, high, low, close):
    lower = np.minimum(open, close) - low
    rng = (high - low).replace(0.0, np.nan)
    s = lower / rng
    base = s.rolling(21, min_periods=21).mean()
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_shasym_mean_20d_slope_v017_signal(open, high, low, close):
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    den = (upper + lower).replace(0.0, np.nan)
    sa = (upper - lower) / den
    base = sa.rolling(20, min_periods=20).mean()
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_shdom_10d_slope_v018_signal(open, high, low, close):
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    mx = np.maximum(upper, lower)
    den = (upper + lower).replace(0.0, np.nan)
    r = mx / den
    base = r.rolling(10, min_periods=10).mean()
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


# -- v019..v027: body color / sign / streaks --------------------------------


def f06cb_f06_candle_body_ratios_bodysign_1d_slope_v019_signal(open, close):
    base = np.sign(close - open)
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bullstrk_20d_slope_v020_signal(open, close):
    bull = (close > open).astype(int)
    grp = (bull == 0).cumsum()
    cnt = bull.groupby(grp).cumcount() + 1
    base = cnt.where(bull == 1, 0).astype(float)
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bearstrk_20d_slope_v021_signal(open, close):
    bear = (close < open).astype(int)
    grp = (bear == 0).cumsum()
    cnt = bear.groupby(grp).cumcount() + 1
    base = cnt.where(bear == 1, 0).astype(float)
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bullcnt_21d_slope_v022_signal(open, close):
    bull = (close > open).astype(float)
    base = bull.rolling(21, min_periods=21).sum()
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bullfrac_63d_slope_v023_signal(open, closeadj):
    bull = (closeadj > open).astype(float)
    base = bull.rolling(63, min_periods=63).mean()
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_colorhom_30d_slope_v024_signal(open, close):
    s = np.sign(close - open)
    base = s.rolling(30, min_periods=30).sum().abs() / 30.0
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodyalt_30d_slope_v025_signal(open, close):
    s = np.sign(close - open)
    flip = (s.diff().abs() > 0).astype(float)
    base = flip.rolling(30, min_periods=30).sum()
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bullbearstrkdiff_30d_slope_v026_signal(open, close):
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
    base = (mx_bu - mx_be).astype(float)
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_3bar_str_3d_slope_v027_signal(open, close):
    s = np.sign(close - open)
    base = s.rolling(3, min_periods=3).sum()
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


# -- v028..v035: close-position-in-bar --------------------------------------






def f06cb_f06_candle_body_ratios_clpos_mean_10d_slope_v030_signal(high, low, close):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    base = cp.rolling(10, min_periods=10).mean()
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_clpos_var_30d_slope_v031_signal(high, low, close):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    base = cp.rolling(30, min_periods=30).var()
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_clpos_skew_30d_slope_v032_signal(high, low, close):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    base = cp.rolling(30, min_periods=30).skew()
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_clpos_asym_30d_slope_v033_signal(high, low, close):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    hi = (cp > 0.7).astype(float).rolling(30, min_periods=30).sum()
    lo = (cp < 0.3).astype(float).rolling(30, min_periods=30).sum()
    base = (hi - lo) / 30.0
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_clpos_iqr_30d_slope_v034_signal(high, low, close):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    q75 = cp.rolling(30, min_periods=30).quantile(0.75)
    q25 = cp.rolling(30, min_periods=30).quantile(0.25)
    base = q75 - q25
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_oppos_var_30d_slope_v035_signal(open, high, low):
    rng = (high - low).replace(0.0, np.nan)
    op = (open - low) / rng
    base = op.rolling(30, min_periods=30).var()
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


# -- v036..v045: body size dynamics -----------------------------------------


def f06cb_f06_candle_body_ratios_bodysz_1d_slope_v036_signal(open, close):
    body = (close - open).abs()
    base = body / close.replace(0.0, np.nan)
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodysz_avg_21d_slope_v037_signal(open, closeadj):
    body = (closeadj - open).abs()
    n = body / closeadj.replace(0.0, np.nan)
    base = n.rolling(21, min_periods=21).mean()
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodysz_ema_diff_30d_slope_v038_signal(open, closeadj):
    body = (closeadj - open).abs()
    e5 = body.ewm(span=5, adjust=False, min_periods=5).mean().replace(0.0, np.nan)
    e30 = body.ewm(span=30, adjust=False, min_periods=30).mean().replace(0.0, np.nan)
    base = np.log(e5 / e30)
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodysz_rnk_60d_slope_v039_signal(open, closeadj):
    body = (closeadj - open).abs()
    base = body.rolling(60, min_periods=30).rank(pct=True)
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodysz_z_30d_slope_v040_signal(open, closeadj):
    body = (closeadj - open).abs()
    mu = body.rolling(30, min_periods=30).mean()
    sd = body.rolling(30, min_periods=30).std().replace(0.0, np.nan)
    base = (body - mu) / sd
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodysz_slp_10d_slope_v041_signal(open, close):
    body = (close - open).abs()
    mu = body.rolling(10, min_periods=10).mean().replace(0.0, np.nan)
    base = body.diff(5) / mu
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_signbody_30d_slope_v042_signal(open, close):
    sb = (close - open) / close.replace(0.0, np.nan)
    base = sb.rolling(30, min_periods=30).mean()
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_sgnbody_z_30d_slope_v043_signal(open, close):
    sb = (close - open) / close.replace(0.0, np.nan)
    mu = sb.rolling(30, min_periods=30).mean()
    sd = sb.rolling(30, min_periods=30).std().replace(0.0, np.nan)
    base = (sb - mu) / sd
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodyslp_20d_slope_v044_signal(open, close):
    body = (close - open).abs()
    n = 20
    x = np.arange(n, dtype=float)
    xm = x.mean()
    xv = ((x - xm) ** 2).sum()
    def _slope(y):
        ym = y.mean()
        return float(((x - xm) * (y - ym)).sum() / xv)
    base = body.rolling(n, min_periods=n).apply(_slope, raw=True)
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodyvar_30d_slope_v045_signal(open, close):
    body = (close - open).abs()
    mu = body.rolling(30, min_periods=30).mean().replace(0.0, np.nan)
    sd = body.rolling(30, min_periods=30).std()
    base = sd / mu
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


# -- v046..v052: pattern-strength continuous (1d, k=5) ----------------------


def f06cb_f06_candle_body_ratios_hammer_sc_1d_slope_v046_signal(open, high, low, close):
    body = (close - open).abs()
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    rng = (high - low).replace(0.0, np.nan)
    cond = (lower > 2.0 * upper) & ((body / rng) < 0.5)
    base = cond.astype(float)
    base[rng.isna()] = np.nan
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_invhammer_sc_1d_slope_v047_signal(open, high, low, close):
    body = (close - open).abs()
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    rng = (high - low).replace(0.0, np.nan)
    cond = (upper > 2.0 * lower) & ((body / rng) < 0.5)
    base = cond.astype(float)
    base[rng.isna()] = np.nan
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_doji_sc_1d_slope_v048_signal(open, high, low, close):
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    base = -np.log(r + 0.01)
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_spintop_sc_1d_slope_v049_signal(open, high, low, close):
    body = (close - open).abs()
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    rng = (high - low).replace(0.0, np.nan)
    den = (upper + lower).replace(0.0, np.nan)
    balance = 1.0 - (upper - lower).abs() / den
    smallbody = 1.0 - body / rng
    base = balance * smallbody
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_engulf_sc_1d_slope_v050_signal(open, close):
    body = (close - open).abs()
    pb = body.shift(1)
    sign_today = np.sign(close - open)
    sign_prev = np.sign((close - open).shift(1))
    opp = (sign_today * sign_prev) < 0
    eps = body.rolling(20, min_periods=10).mean() * 0.05 + 1e-12
    score = sign_today * np.log((body + eps) / (pb + eps))
    base = score.where(opp, 0.0)
    base[pb.isna()] = np.nan
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_piercing_sc_1d_slope_v051_signal(open, close):
    prev_open = open.shift(1)
    prev_close = close.shift(1)
    prev_mid = (prev_open + prev_close) * 0.5
    prev_body = (prev_close - prev_open).abs()
    sign_today = np.sign(close - open)
    sign_prev = np.sign(prev_close - prev_open)
    opp = (sign_today * sign_prev) < 0
    pb = prev_body.replace(0.0, np.nan)
    score = (close - prev_mid) / pb
    base = score.where(opp, 0.0)
    base[prev_open.isna()] = np.nan
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_engulfnet_30d_slope_v052_signal(open, close):
    body = (close - open).abs()
    pb = body.shift(1)
    sign_today = np.sign(close - open)
    sign_prev = np.sign((close - open).shift(1))
    opp = (sign_today * sign_prev) < 0
    eps = body.rolling(20, min_periods=10).mean() * 0.05 + 1e-12
    score = sign_today * np.log((body + eps) / (pb + eps))
    sc = score.where(opp, 0.0)
    sc[pb.isna()] = np.nan
    base = sc.rolling(30, min_periods=30).sum()
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


# -- v053..v058: range dynamics ---------------------------------------------


def f06cb_f06_candle_body_ratios_rngprev_1d_slope_v053_signal(high, low):
    rng = (high - low)
    pr = rng.shift(1).replace(0.0, np.nan)
    base = np.log((rng + 1e-12) / (pr + 1e-12))
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_rngexp_20d_slope_v054_signal(high, low):
    rng = (high - low)
    mu = rng.rolling(20, min_periods=20).mean().replace(0.0, np.nan)
    base = rng / mu
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_rngrnk_60d_slope_v055_signal(high, low):
    rng = (high - low)
    base = rng.rolling(60, min_periods=30).rank(pct=True)
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_rngnorm_30d_slope_v056_signal(high, low, close):
    rng = (high - low) / close.replace(0.0, np.nan)
    base = rng.rolling(30, min_periods=30).mean()
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_rngprev_mean_21d_slope_v057_signal(high, low):
    rng = (high - low)
    pr = rng.shift(1).replace(0.0, np.nan)
    lr = np.log((rng + 1e-12) / (pr + 1e-12))
    base = lr.rolling(21, min_periods=21).mean()
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_rng_logvar_30d_slope_v058_signal(high, low, closeadj):
    rng = (high - low) / closeadj.replace(0.0, np.nan)
    v = rng.rolling(30, min_periods=30).var().replace(0.0, np.nan)
    base = np.log(v)
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


# -- v059..v065: shape / bounded transforms / asymmetries -------------------


def f06cb_f06_candle_body_ratios_shape_idx_1d_slope_v059_signal(open, high, low, close):
    rng = (high - low)
    body = (close - open).abs() + rng * 0.001
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    base = np.arctan((upper - lower) / body.replace(0.0, np.nan))
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_br_ac1_30d_slope_v060_signal(open, high, low, close):
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    base = r.rolling(30, min_periods=30).corr(r.shift(1))
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_brsig_30d_slope_v061_signal(open, high, low, close):
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    mu = r.rolling(30, min_periods=30).mean()
    sd = r.rolling(30, min_periods=30).std().replace(0.0, np.nan)
    base = mu / sd
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_wickbody_30d_slope_v062_signal(open, high, low, close):
    body = (close - open).abs()
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    rng = (high - low).replace(0.0, np.nan)
    s = (upper + lower - body) / rng
    base = s.rolling(30, min_periods=30).mean()
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_wickbody_iqr_30d_slope_v063_signal(open, high, low, close):
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    q75 = r.rolling(30, min_periods=30).quantile(0.75)
    q25 = r.rolling(30, min_periods=30).quantile(0.25)
    base = q75 - q25
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_brkurt_60d_slope_v064_signal(open, high, low, close):
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    base = r.rolling(60, min_periods=60).kurt()
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodyup_dom_30d_slope_v065_signal(open, high, low, close):
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    cond = (upper > lower).astype(float)
    base = cond.rolling(30, min_periods=30).mean()
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


# -- v066..v075: open-gap-vs-prev-close + extras ----------------------------


def f06cb_f06_candle_body_ratios_openpos_pc_1d_slope_v066_signal(open, high, low, close):
    rng = (high - low).replace(0.0, np.nan)
    pc = close.shift(1)
    base = (open - pc) / rng
    base[pc.isna()] = np.nan
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_clvopen_pc_1d_slope_v067_signal(open, close):
    pc = close.shift(1)
    tot = (close - pc).abs()
    eps = close.rolling(10, min_periods=5).std() * 0.01 + 1e-12
    base = (close - open) / (tot + eps)
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_brspread_60d_slope_v068_signal(open, high, low, close):
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    s5 = r.rolling(5, min_periods=5).mean()
    s60 = r.rolling(60, min_periods=60).mean()
    base = s5 - s60
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_shasym_var_30d_slope_v069_signal(open, high, low, close):
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    den = (upper + lower).replace(0.0, np.nan)
    sa = (upper - lower) / den
    base = sa.rolling(30, min_periods=30).var()
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_avgshlen_21d_slope_v070_signal(open, high, low, close):
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    s = (upper + lower) / close.replace(0.0, np.nan)
    base = s.rolling(21, min_periods=21).mean()
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_hammer_cnt_60d_slope_v071_signal(open, high, low, close):
    body = (close - open).abs()
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    rng = (high - low).replace(0.0, np.nan)
    cond = ((lower > 2.0 * upper) & ((body / rng) < 0.5)).astype(float)
    base = cond.rolling(60, min_periods=60).sum()
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_dojistr_30d_slope_v072_signal(open, high, low, close):
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    ds = -np.log(r + 0.01)
    base = ds.rolling(30, min_periods=30).mean()
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_upshmlosh_30d_slope_v073_signal(open, high, low, close):
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    s = (upper - lower) / close.replace(0.0, np.nan)
    base = s.rolling(30, min_periods=30).mean()
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodyrng_corr_30d_slope_v074_signal(open, high, low, close):
    body = (close - open).abs()
    rng = (high - low)
    base = body.rolling(30, min_periods=30).corr(rng)
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_signbodyrng_50d_slope_v075_signal(open, high, low, closeadj):
    rng = (high - low).replace(0.0, np.nan)
    sbr = (closeadj - open) / rng
    base = sbr.rolling(50, min_periods=50).mean()
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


# -- v076..v098: base 2 first half ------------------------------------------


def f06cb_f06_candle_body_ratios_bodydir_align_1d_slope_v076_signal(open, high, low, close):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng - 0.5
    sb = np.sign(close - open)
    base = sb * cp
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_dayret_abs_rng_1d_slope_v077_signal(high, low, close):
    rng = (high - low).replace(0.0, np.nan)
    base = (close - close.shift(1)).abs() / rng
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodysz_std_50d_slope_v078_signal(open, closeadj):
    body = (closeadj - open).abs()
    n = body / closeadj.replace(0.0, np.nan)
    base = n.rolling(50, min_periods=50).std()
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_pcoutside_1d_slope_v079_signal(high, low, close):
    pc = close.shift(1)
    cond = ((pc > high) | (pc < low)).astype(float)
    base = cond
    base[pc.isna()] = np.nan
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodyac1_30d_slope_v080_signal(open, close):
    body = (close - open).abs()
    base = body.rolling(30, min_periods=30).corr(body.shift(1))
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_rngmean_50d_slope_v081_signal(high, low):
    rng = (high - low)
    base = rng.rolling(50, min_periods=50).mean()
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodysz_max_5d_slope_v082_signal(open, close):
    body = (close - open).abs() / close.replace(0.0, np.nan)
    base = body.rolling(5, min_periods=5).max()
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_upsh_max_5d_slope_v083_signal(open, high, low, close):
    upper = high - np.maximum(open, close)
    rng = (high - low).replace(0.0, np.nan)
    s = upper / rng
    base = s.rolling(5, min_periods=5).max()
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_losh_max_5d_slope_v084_signal(open, high, low, close):
    lower = np.minimum(open, close) - low
    rng = (high - low).replace(0.0, np.nan)
    s = lower / rng
    base = s.rolling(5, min_periods=5).max()
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_doji_soft_30d_slope_v085_signal(open, high, low, close):
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    doji = (r < 0.15).astype(float)
    base = doji.rolling(30, min_periods=30).mean()
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_marub_soft_30d_slope_v086_signal(open, high, low, close):
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    m = (r > 0.6).astype(float)
    base = m.rolling(30, min_periods=30).mean()
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_3bar_brprod_3d_slope_v087_signal(open, high, low, close):
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    log_r = np.log(r + 1e-9)
    log_mean = log_r.rolling(3, min_periods=3).mean()
    base = np.exp(log_mean)
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_clhi_strk_5d_slope_v088_signal(high, low, close):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    near = (cp > 0.6).astype(int)
    grp = (near == 0).cumsum()
    cnt = near.groupby(grp).cumcount() + 1
    base = cnt.where(near == 1, 0).astype(float)
    base[rng.isna()] = np.nan
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_cllo_strk_5d_slope_v089_signal(high, low, close):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    near = (cp < 0.4).astype(int)
    grp = (near == 0).cumsum()
    cnt = near.groupby(grp).cumcount() + 1
    base = cnt.where(near == 1, 0).astype(float)
    base[rng.isna()] = np.nan
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_atr_iqr_30d_slope_v090_signal(high, low, close):
    pc = close.shift(1)
    tr1 = (high - low).abs()
    tr2 = (high - pc).abs()
    tr3 = (low - pc).abs()
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    norm = tr / close.replace(0.0, np.nan)
    q75 = norm.rolling(30, min_periods=30).quantile(0.75)
    q25 = norm.rolling(30, min_periods=30).quantile(0.25)
    base = q75 - q25
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_brslope_5d_slope_v091_signal(open, high, low, close):
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    mu = r.rolling(10, min_periods=5).mean().replace(0.0, np.nan)
    base = r.diff(3) / mu
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_clpos_q90_30d_slope_v092_signal(high, low, close):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    base = cp.rolling(30, min_periods=30).quantile(0.9)
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_clhi_frac_20d_slope_v093_signal(high, low, close):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    base = (cp > 0.5).astype(float).rolling(20, min_periods=20).mean()
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodymid_up_30d_slope_v094_signal(open, high, low, close):
    bmid = (open + close) * 0.5
    bar_mid = (high + low) * 0.5
    cond = (bmid > bar_mid).astype(float)
    base = cond.rolling(30, min_periods=30).mean()
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_shabsdiff_sq_1d_slope_v095_signal(open, high, low, close):
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    rng = (high - low).replace(0.0, np.nan)
    diff = (upper - lower) / rng
    base = diff * diff
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_hammer_skew_30d_slope_v096_signal(open, high, low, close):
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    rng = (high - low).replace(0.0, np.nan)
    diff = (lower - upper) / rng
    base = diff.rolling(30, min_periods=30).skew()
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_invhammer_max_10d_slope_v097_signal(open, high, low, close):
    body = (close - open).abs()
    upper = high - np.maximum(open, close)
    rng = (high - low).replace(0.0, np.nan)
    s = (upper / rng) * (1.0 - body / rng)
    base = s.rolling(10, min_periods=10).max()
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_uplodiff_sd_30d_slope_v098_signal(open, high, low, close):
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    rng = (high - low).replace(0.0, np.nan)
    diff = (upper - lower) / rng
    base = diff.rolling(30, min_periods=30).std()
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


# -- v099..v124: base 2 second half - 1 -------------------------------------


def f06cb_f06_candle_body_ratios_hi_step_1d_slope_v099_signal(high):
    ph = high.shift(1).replace(0.0, np.nan)
    base = np.log(high / ph)
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_lo_step_1d_slope_v100_signal(low):
    pl = low.shift(1).replace(0.0, np.nan)
    base = np.log(low / pl)
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_hi_overshoot_30d_slope_v101_signal(high, close):
    pc = close.shift(1)
    cond = (high > pc * 1.005).astype(float)
    base = cond.rolling(30, min_periods=30).sum()
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_lo_undershoot_30d_slope_v102_signal(low, close):
    pc = close.shift(1)
    cond = (low < pc * 0.995).astype(float)
    base = cond.rolling(30, min_periods=30).sum()
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bar_overlap_1d_slope_v103_signal(high, low):
    ph = high.shift(1)
    pl = low.shift(1)
    overlap = np.minimum(high, ph) - np.maximum(low, pl)
    overlap = overlap.where(overlap > 0.0, 0.0)
    rng = (high - low).replace(0.0, np.nan)
    base = overlap / rng
    base[ph.isna()] = np.nan
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_shasym_iqr_30d_slope_v104_signal(open, high, low, close):
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    den = (upper + lower).replace(0.0, np.nan)
    sa = (upper - lower) / den
    q75 = sa.rolling(30, min_periods=30).quantile(0.75)
    q25 = sa.rolling(30, min_periods=30).quantile(0.25)
    base = q75 - q25
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_upsh_corr_prev_30d_slope_v105_signal(open, high, low, close):
    upper = high - np.maximum(open, close)
    rng = (high - low).replace(0.0, np.nan)
    s = upper / rng
    base = s.rolling(30, min_periods=30).corr(s.shift(1))
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_rng3sum_3d_slope_v106_signal(high, low):
    h3 = high.rolling(3, min_periods=3).max()
    l3 = low.rolling(3, min_periods=3).min()
    rng = (high - low).replace(0.0, np.nan)
    base = (h3 - l3) / rng
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_sbodysum_5d_slope_v107_signal(open, high, low, close):
    sbody = (close - open)
    rng = (high - low)
    sb_sum = sbody.rolling(5, min_periods=5).sum()
    rng_sum = rng.rolling(5, min_periods=5).sum().replace(0.0, np.nan)
    base = sb_sum / rng_sum
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_rngsum_5d_slope_v108_signal(high, low, close):
    rng = (high - low)
    rs = rng.rolling(5, min_periods=5).sum()
    base = rs / close.replace(0.0, np.nan)
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_largbody_cnt_21d_slope_v109_signal(open, close):
    body = (close - open).abs()
    mu = body.rolling(21, min_periods=21).mean()
    cond = (body > mu).astype(float)
    base = cond.rolling(21, min_periods=21).sum()
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodydiv_dret_30d_slope_v110_signal(open, close):
    body = (close - open).abs()
    dret = (close - close.shift(1)).abs().replace(0.0, np.nan)
    r = body / dret
    base = r.rolling(30, min_periods=30).mean()
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_body_in_50dh_50d_slope_v111_signal(high, low, open, close):
    bmid = (open + close) * 0.5
    h50 = high.rolling(50, min_periods=50).max()
    l50 = low.rolling(50, min_periods=50).min()
    den = (h50 - l50).replace(0.0, np.nan)
    base = (bmid - l50) / den
    return base.diff(21).replace([np.inf, -np.inf], np.nan)




def f06cb_f06_candle_body_ratios_sbodysq_30d_slope_v113_signal(open, close):
    sb = np.sign(close - open) * ((close - open) ** 2) / (close.replace(0.0, np.nan) ** 2)
    base = sb.rolling(30, min_periods=30).mean()
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_body_ema_5d_slope_v114_signal(open, close):
    body = (close - open).abs() / close.replace(0.0, np.nan)
    base = body.ewm(span=5, adjust=False, min_periods=5).mean()
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_br_ema_21d_slope_v115_signal(open, high, low, close):
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    base = r.ewm(span=21, adjust=False, min_periods=21).mean()
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_clpos_ema_30d_slope_v116_signal(high, low, close):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    base = cp.ewm(span=30, adjust=False, min_periods=30).mean()
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_rng_ac1_30d_slope_v117_signal(high, low):
    rng = (high - low)
    base = rng.rolling(30, min_periods=30).corr(rng.shift(1))
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodysharpe_50d_slope_v118_signal(open, closeadj):
    body = (closeadj - open).abs()
    mu = body.rolling(50, min_periods=50).mean()
    sd = body.rolling(50, min_periods=50).std().replace(0.0, np.nan)
    base = mu / sd
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_shasym_rnk_30d_slope_v119_signal(open, high, low, close):
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    den = (upper + lower).replace(0.0, np.nan)
    sa = (upper - lower) / den
    base = sa.rolling(30, min_periods=15).rank(pct=True)
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodyac_pos_30d_slope_v120_signal(open, close):
    sb = (close - open) / close.replace(0.0, np.nan)
    base = sb.rolling(30, min_periods=30).corr(sb.shift(1))
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_brclpos_corr_30d_slope_v121_signal(open, high, low, close):
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    br = body / rng
    cp = (close - low) / rng
    base = br.rolling(30, min_periods=30).corr(cp)
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_rng_consist_30d_slope_v122_signal(high, low):
    rng = (high - low)
    exp = (rng > rng.shift(1)).astype(float)
    base = exp.rolling(30, min_periods=30).mean()
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_brhalf_strk_5d_slope_v123_signal(open, high, low, close):
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    near = (r > 0.5).astype(int)
    grp = (near == 0).cumsum()
    cnt = near.groupby(grp).cumcount() + 1
    base = cnt.where(near == 1, 0).astype(float)
    base[rng.isna()] = np.nan
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodysum_5d_slope_v124_signal(open, high, low, close):
    body = (close - open).abs()
    rng = (high - low)
    bs = body.rolling(5, min_periods=5).sum()
    rs = rng.rolling(5, min_periods=5).sum().replace(0.0, np.nan)
    base = bs / rs
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


# -- v125..v150: base 2 second half - 2 -------------------------------------


def f06cb_f06_candle_body_ratios_clop_vol_norm_1d_slope_v125_signal(open, high, low, close):
    sbody = close - open
    rng = high - low
    base = (sbody * rng) / (close.replace(0.0, np.nan) ** 2)
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodyrng_q90_30d_slope_v126_signal(open, high, low, close):
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    base = r.rolling(30, min_periods=30).quantile(0.9)
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_body_mad_30d_slope_v127_signal(open, close):
    body = (close - open).abs()
    mu = body.rolling(30, min_periods=30).mean()
    abs_dev = (body - mu).abs()
    base = abs_dev.rolling(30, min_periods=30).mean()
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_br_mad_30d_slope_v128_signal(open, high, low, close):
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    mu = r.rolling(30, min_periods=30).mean()
    abs_dev = (r - mu).abs()
    base = abs_dev.rolling(30, min_periods=30).mean()
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_color_entropy_30d_slope_v129_signal(open, close):
    bull = (close > open).astype(float)
    p = bull.rolling(30, min_periods=30).mean()
    p_safe = p.clip(lower=1e-6, upper=1.0 - 1e-6)
    base = -(p_safe * np.log(p_safe) + (1.0 - p_safe) * np.log(1.0 - p_safe))
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bullfrac_spread_60d_slope_v130_signal(open, closeadj):
    bull = (closeadj > open).astype(float)
    s5 = bull.rolling(5, min_periods=5).mean()
    s60 = bull.rolling(60, min_periods=60).mean()
    base = s5 - s60
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodybull_disagree_30d_slope_v131_signal(open, close):
    sb = (close - open) / close.replace(0.0, np.nan)
    med = sb.rolling(30, min_periods=30).median()
    disagree = (np.sign(sb) * np.sign(med) < 0).astype(float)
    base = disagree.rolling(30, min_periods=30).sum()
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_clpos_rnk_50d_slope_v132_signal(open, high, low, closeadj):
    rng = (high - low).replace(0.0, np.nan)
    cp = (closeadj - low) / rng
    base = cp.rolling(50, min_periods=25).rank(pct=True)
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_clhi06_strk_7d_slope_v133_signal(high, low, close):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    near = (cp > 0.6).astype(float)
    base = near.rolling(7, min_periods=7).sum()
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bigrng_cnt_30d_slope_v134_signal(high, low):
    rng = (high - low)
    mu = rng.rolling(30, min_periods=30).mean()
    cond = (rng > 1.5 * mu).astype(float)
    base = cond.rolling(30, min_periods=30).sum()
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_smallrng_cnt_30d_slope_v135_signal(high, low):
    rng = (high - low)
    mu = rng.rolling(30, min_periods=30).mean()
    cond = (rng < 0.5 * mu).astype(float)
    base = cond.rolling(30, min_periods=30).sum()
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodyalign_30d_slope_v136_signal(open, close):
    sb = np.sign(close - open)
    sd = np.sign(close - close.shift(1))
    cond = ((sb * sd) > 0).astype(float)
    base = cond.rolling(30, min_periods=30).sum()
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_shape_std_50d_slope_v137_signal(open, high, low, close):
    rng = (high - low)
    body = (close - open).abs() + rng * 0.001
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    si = np.arctan((upper - lower) / body.replace(0.0, np.nan))
    base = si.rolling(50, min_periods=50).std()
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_br_diff_7d_slope_v138_signal(open, high, low, close):
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    base = r - r.shift(7)
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_upbody_kurt_30d_slope_v139_signal(open, high, low, close):
    upper = high - np.maximum(open, close)
    body = (close - open).abs()
    eps = (high - low).abs() * 0.01 + 1e-12
    s = np.log((upper + eps) / (body + eps))
    base = s.rolling(30, min_periods=30).kurt()
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_clpos_kurt_30d_slope_v140_signal(high, low, close):
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    base = cp.rolling(30, min_periods=30).kurt()
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bullbear_emadiff_30d_slope_v141_signal(open, close):
    sb = np.sign(close - open).astype(float)
    e7 = sb.ewm(span=7, adjust=False, min_periods=7).mean()
    e30 = sb.ewm(span=30, adjust=False, min_periods=30).mean()
    base = e7 - e30
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_openpos_std_30d_slope_v142_signal(open, high, low, close):
    rng = (high - low).replace(0.0, np.nan)
    pc = close.shift(1)
    s = (open - pc) / rng
    base = s.rolling(30, min_periods=30).std()
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_rng_z_7d_slope_v143_signal(high, low):
    rng = (high - low)
    mu = rng.rolling(7, min_periods=7).mean()
    sd = rng.rolling(7, min_periods=7).std().replace(0.0, np.nan)
    base = (rng - mu) / sd
    return base.diff(5).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_sgnbrrat_30d_slope_v144_signal(open, high, low, close):
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    sb = np.sign(close - open)
    r = (1.0 - body / rng) * sb
    base = r.rolling(30, min_periods=30).mean()
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_shasym_rngcorr_50d_slope_v145_signal(open, high, low, closeadj):
    upper = high - np.maximum(open, closeadj)
    lower = np.minimum(open, closeadj) - low
    den = (upper + lower).replace(0.0, np.nan)
    sa = (upper - lower) / den
    rng = (high - low) / closeadj.replace(0.0, np.nan)
    base = sa.rolling(50, min_periods=50).corr(rng)
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_no_upsh_30d_slope_v146_signal(open, high, low, close):
    upper = high - np.maximum(open, close)
    rng = (high - low).replace(0.0, np.nan)
    s = upper / rng
    cond = (s < 0.1).astype(float)
    base = cond.rolling(30, min_periods=30).mean()
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_no_losh_30d_slope_v147_signal(open, high, low, close):
    lower = np.minimum(open, close) - low
    rng = (high - low).replace(0.0, np.nan)
    s = lower / rng
    cond = (s < 0.1).astype(float)
    base = cond.rolling(30, min_periods=30).mean()
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodymad_robz_60d_slope_v148_signal(open, closeadj):
    body = (closeadj - open).abs()
    med = body.rolling(60, min_periods=60).median()
    mad = (body - med).abs().rolling(60, min_periods=60).median().replace(0.0, np.nan)
    base = (body - med) / mad
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_shimbal_kurt_30d_slope_v149_signal(open, high, low, close):
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    s = (upper - lower) / close.replace(0.0, np.nan)
    base = s.rolling(30, min_periods=30).kurt()
    return base.diff(10).replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodymom_ema_diff_30d_slope_v150_signal(open, close):
    sb = (close - open) / close.replace(0.0, np.nan)
    e5 = sb.ewm(span=5, adjust=False, min_periods=5).mean()
    e30 = sb.ewm(span=30, adjust=False, min_periods=30).mean()
    base = e5 - e30
    return base.diff(21).replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


def _e(fn, *inputs):
    return fn.__name__, {"inputs": list(inputs), "func": fn}


f06_candle_body_ratios_slope_001_150_REGISTRY = dict([
    _e(f06cb_f06_candle_body_ratios_brrat_1d_slope_v001_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_brmean_10d_slope_v002_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_brmed_21d_slope_v003_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_brstd_21d_slope_v004_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_br_q25_30d_slope_v005_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_brskew_30d_slope_v006_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_brmax_10d_slope_v007_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_brmin_10d_slope_v008_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_upsh_1d_slope_v009_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_losh_1d_slope_v010_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_shasym_1d_slope_v011_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_shprod_1d_slope_v012_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_upbody_1d_slope_v013_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_lobody_1d_slope_v014_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_upsh_mean_21d_slope_v015_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_losh_mean_21d_slope_v016_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_shasym_mean_20d_slope_v017_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_shdom_10d_slope_v018_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_bodysign_1d_slope_v019_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_bullstrk_20d_slope_v020_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_bearstrk_20d_slope_v021_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_bullcnt_21d_slope_v022_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_bullfrac_63d_slope_v023_signal, "open", "closeadj"),
    _e(f06cb_f06_candle_body_ratios_colorhom_30d_slope_v024_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_bodyalt_30d_slope_v025_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_bullbearstrkdiff_30d_slope_v026_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_3bar_str_3d_slope_v027_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_clpos_mean_10d_slope_v030_signal, "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_clpos_var_30d_slope_v031_signal, "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_clpos_skew_30d_slope_v032_signal, "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_clpos_asym_30d_slope_v033_signal, "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_clpos_iqr_30d_slope_v034_signal, "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_oppos_var_30d_slope_v035_signal, "open", "high", "low"),
    _e(f06cb_f06_candle_body_ratios_bodysz_1d_slope_v036_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_bodysz_avg_21d_slope_v037_signal, "open", "closeadj"),
    _e(f06cb_f06_candle_body_ratios_bodysz_ema_diff_30d_slope_v038_signal, "open", "closeadj"),
    _e(f06cb_f06_candle_body_ratios_bodysz_rnk_60d_slope_v039_signal, "open", "closeadj"),
    _e(f06cb_f06_candle_body_ratios_bodysz_z_30d_slope_v040_signal, "open", "closeadj"),
    _e(f06cb_f06_candle_body_ratios_bodysz_slp_10d_slope_v041_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_signbody_30d_slope_v042_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_sgnbody_z_30d_slope_v043_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_bodyslp_20d_slope_v044_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_bodyvar_30d_slope_v045_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_hammer_sc_1d_slope_v046_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_invhammer_sc_1d_slope_v047_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_doji_sc_1d_slope_v048_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_spintop_sc_1d_slope_v049_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_engulf_sc_1d_slope_v050_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_piercing_sc_1d_slope_v051_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_engulfnet_30d_slope_v052_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_rngprev_1d_slope_v053_signal, "high", "low"),
    _e(f06cb_f06_candle_body_ratios_rngexp_20d_slope_v054_signal, "high", "low"),
    _e(f06cb_f06_candle_body_ratios_rngrnk_60d_slope_v055_signal, "high", "low"),
    _e(f06cb_f06_candle_body_ratios_rngnorm_30d_slope_v056_signal, "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_rngprev_mean_21d_slope_v057_signal, "high", "low"),
    _e(f06cb_f06_candle_body_ratios_rng_logvar_30d_slope_v058_signal, "high", "low", "closeadj"),
    _e(f06cb_f06_candle_body_ratios_shape_idx_1d_slope_v059_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_br_ac1_30d_slope_v060_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_brsig_30d_slope_v061_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_wickbody_30d_slope_v062_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_wickbody_iqr_30d_slope_v063_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_brkurt_60d_slope_v064_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_bodyup_dom_30d_slope_v065_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_openpos_pc_1d_slope_v066_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_clvopen_pc_1d_slope_v067_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_brspread_60d_slope_v068_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_shasym_var_30d_slope_v069_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_avgshlen_21d_slope_v070_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_hammer_cnt_60d_slope_v071_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_dojistr_30d_slope_v072_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_upshmlosh_30d_slope_v073_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_bodyrng_corr_30d_slope_v074_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_signbodyrng_50d_slope_v075_signal, "open", "high", "low", "closeadj"),
    _e(f06cb_f06_candle_body_ratios_bodydir_align_1d_slope_v076_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_dayret_abs_rng_1d_slope_v077_signal, "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_bodysz_std_50d_slope_v078_signal, "open", "closeadj"),
    _e(f06cb_f06_candle_body_ratios_pcoutside_1d_slope_v079_signal, "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_bodyac1_30d_slope_v080_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_rngmean_50d_slope_v081_signal, "high", "low"),
    _e(f06cb_f06_candle_body_ratios_bodysz_max_5d_slope_v082_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_upsh_max_5d_slope_v083_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_losh_max_5d_slope_v084_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_doji_soft_30d_slope_v085_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_marub_soft_30d_slope_v086_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_3bar_brprod_3d_slope_v087_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_clhi_strk_5d_slope_v088_signal, "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_cllo_strk_5d_slope_v089_signal, "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_atr_iqr_30d_slope_v090_signal, "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_brslope_5d_slope_v091_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_clpos_q90_30d_slope_v092_signal, "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_clhi_frac_20d_slope_v093_signal, "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_bodymid_up_30d_slope_v094_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_shabsdiff_sq_1d_slope_v095_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_hammer_skew_30d_slope_v096_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_invhammer_max_10d_slope_v097_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_uplodiff_sd_30d_slope_v098_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_hi_step_1d_slope_v099_signal, "high"),
    _e(f06cb_f06_candle_body_ratios_lo_step_1d_slope_v100_signal, "low"),
    _e(f06cb_f06_candle_body_ratios_hi_overshoot_30d_slope_v101_signal, "high", "close"),
    _e(f06cb_f06_candle_body_ratios_lo_undershoot_30d_slope_v102_signal, "low", "close"),
    _e(f06cb_f06_candle_body_ratios_bar_overlap_1d_slope_v103_signal, "high", "low"),
    _e(f06cb_f06_candle_body_ratios_shasym_iqr_30d_slope_v104_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_upsh_corr_prev_30d_slope_v105_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_rng3sum_3d_slope_v106_signal, "high", "low"),
    _e(f06cb_f06_candle_body_ratios_sbodysum_5d_slope_v107_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_rngsum_5d_slope_v108_signal, "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_largbody_cnt_21d_slope_v109_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_bodydiv_dret_30d_slope_v110_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_body_in_50dh_50d_slope_v111_signal, "high", "low", "open", "close"),
    _e(f06cb_f06_candle_body_ratios_sbodysq_30d_slope_v113_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_body_ema_5d_slope_v114_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_br_ema_21d_slope_v115_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_clpos_ema_30d_slope_v116_signal, "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_rng_ac1_30d_slope_v117_signal, "high", "low"),
    _e(f06cb_f06_candle_body_ratios_bodysharpe_50d_slope_v118_signal, "open", "closeadj"),
    _e(f06cb_f06_candle_body_ratios_shasym_rnk_30d_slope_v119_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_bodyac_pos_30d_slope_v120_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_brclpos_corr_30d_slope_v121_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_rng_consist_30d_slope_v122_signal, "high", "low"),
    _e(f06cb_f06_candle_body_ratios_brhalf_strk_5d_slope_v123_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_bodysum_5d_slope_v124_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_clop_vol_norm_1d_slope_v125_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_bodyrng_q90_30d_slope_v126_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_body_mad_30d_slope_v127_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_br_mad_30d_slope_v128_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_color_entropy_30d_slope_v129_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_bullfrac_spread_60d_slope_v130_signal, "open", "closeadj"),
    _e(f06cb_f06_candle_body_ratios_bodybull_disagree_30d_slope_v131_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_clpos_rnk_50d_slope_v132_signal, "open", "high", "low", "closeadj"),
    _e(f06cb_f06_candle_body_ratios_clhi06_strk_7d_slope_v133_signal, "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_bigrng_cnt_30d_slope_v134_signal, "high", "low"),
    _e(f06cb_f06_candle_body_ratios_smallrng_cnt_30d_slope_v135_signal, "high", "low"),
    _e(f06cb_f06_candle_body_ratios_bodyalign_30d_slope_v136_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_shape_std_50d_slope_v137_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_br_diff_7d_slope_v138_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_upbody_kurt_30d_slope_v139_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_clpos_kurt_30d_slope_v140_signal, "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_bullbear_emadiff_30d_slope_v141_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_openpos_std_30d_slope_v142_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_rng_z_7d_slope_v143_signal, "high", "low"),
    _e(f06cb_f06_candle_body_ratios_sgnbrrat_30d_slope_v144_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_shasym_rngcorr_50d_slope_v145_signal, "open", "high", "low", "closeadj"),
    _e(f06cb_f06_candle_body_ratios_no_upsh_30d_slope_v146_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_no_losh_30d_slope_v147_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_bodymad_robz_60d_slope_v148_signal, "open", "closeadj"),
    _e(f06cb_f06_candle_body_ratios_shimbal_kurt_30d_slope_v149_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_bodymom_ema_diff_30d_slope_v150_signal, "open", "close"),
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
    for name, entry in f06_candle_body_ratios_slope_001_150_REGISTRY.items():
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
    print(f"OK slope_001_150: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
