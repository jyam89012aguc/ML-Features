"""f07_gap_behavior slope features 001-150 (1st-derivative)."""
from __future__ import annotations

import numpy as np
import pandas as pd


def f07gb_f07_gap_behavior_gappct_1d_slope_v001_signal(open, close):
    pc = close.shift(1)
    b = (open - pc) / pc.replace(0.0, np.nan)
    return b.diff(5).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_lgapcumlong_120d_slope_v002_signal(open, closeadj):
    pc = closeadj.shift(1)
    lg = np.log(open / pc.replace(0.0, np.nan))
    b = lg.rolling(120, min_periods=120).sum()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapabsnrm_5d_slope_v003_signal(open, close):
    pc = close.shift(1)
    g = ((open - pc) / pc.replace(0.0, np.nan)).abs()
    mu = g.rolling(5, min_periods=5).mean()
    b = g / mu.replace(0.0, np.nan)
    return b.diff(5).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapsgn_1d_slope_v004_signal(open, close):
    pc = close.shift(1)
    g = open - pc
    b = np.sign(g).where(~g.isna())
    return b.diff(5).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapmean_10d_slope_v005_signal(open, close):
    pc = close.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    b = g.rolling(10, min_periods=10).mean()
    return b.diff(5).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapsum_21d_slope_v006_signal(open, close):
    pc = close.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    b = g.rolling(21, min_periods=21).sum()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapmed_50d_slope_v007_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    b = g.rolling(50, min_periods=50).median()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapsumabs_30d_slope_v008_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    b = g.abs().rolling(30, min_periods=30).sum()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapstd_20d_slope_v009_signal(open, close):
    pc = close.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    b = g.rolling(20, min_periods=20).std(ddof=1)
    return b.diff(5).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapmad_40d_slope_v010_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    mu = g.rolling(40, min_periods=40).mean()
    b = (g - mu).abs().rolling(40, min_periods=40).mean()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gaprng_30d_slope_v011_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    b = g.rolling(30, min_periods=30).max() - g.rolling(30, min_periods=30).min()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapiqr_60d_slope_v012_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    q75 = g.rolling(60, min_periods=60).quantile(0.75)
    q25 = g.rolling(60, min_periods=60).quantile(0.25)
    b = q75 - q25
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_bigfrac_30d_slope_v013_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    big = (g.abs() > 0.005).astype(float).where(~g.isna())
    b = big.rolling(30, min_periods=30).mean()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_posnegratio_120d_slope_v014_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    pmean = g.where(g > 0).rolling(120, min_periods=30).mean()
    nmean = (-g).where(g < 0).rolling(120, min_periods=30).mean()
    b = pmean / nmean.replace(0.0, np.nan)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gaprnkmed_50d_slope_v015_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    pr = g.rolling(50, min_periods=30).rank(pct=True)
    b = pr.rolling(5, min_periods=5).median()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gaprnkabs_80d_slope_v016_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    b = g.abs().rolling(80, min_periods=40).rank(pct=True)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_fillbin_1d_slope_v017_signal(open, high, low, close):
    pc = close.shift(1)
    g = open - pc
    up_fill = (low <= pc) & (g > 0)
    dn_fill = (high >= pc) & (g < 0)
    filled = (up_fill | dn_fill).astype(float)
    b = filled.where(g != 0.0)
    return b.diff(5).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_fillratio_1d_slope_v018_signal(open, high, low, close):
    pc = close.shift(1)
    g = open - pc
    up_amt = (open - low) / g.where(g > 0, np.nan)
    dn_amt = (high - open) / (-g).where(g < 0, np.nan)
    raw = up_amt.combine_first(dn_amt)
    b = raw.clip(lower=0.0, upper=1.0)
    return b.diff(5).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_fillrate_30d_slope_v019_signal(open, high, low, closeadj):
    pc = closeadj.shift(1)
    g = open - pc
    up_fill = (low <= pc) & (g > 0)
    dn_fill = (high >= pc) & (g < 0)
    has_gap = (g != 0.0).astype(float)
    filled = (up_fill | dn_fill).astype(float).where(g != 0.0)
    s_filled = filled.rolling(30, min_periods=15).sum()
    s_total = has_gap.rolling(30, min_periods=15).sum()
    b = s_filled / s_total.replace(0.0, np.nan)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_partfillmean_20d_slope_v020_signal(open, high, low, close):
    pc = close.shift(1)
    g = open - pc
    up_amt = (open - low) / g.where(g > 0, np.nan)
    dn_amt = (high - open) / (-g).where(g < 0, np.nan)
    raw = up_amt.combine_first(dn_amt).clip(lower=0.0, upper=1.0)
    b = raw.rolling(20, min_periods=10).mean()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapgo_1d_slope_v021_signal(open, close):
    pc = close.shift(1)
    g = open - pc
    cls = close - open
    val = pd.Series(np.where((g > 0) & (cls > 0), 1.0,
                   np.where((g < 0) & (cls < 0), -1.0, 0.0)),
                    index=open.index, dtype=float)
    b = val.where(~g.isna())
    return b.diff(5).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gaprev_1d_slope_v022_signal(open, close):
    pc = close.shift(1)
    g = open - pc
    cls = close - open
    val = pd.Series(np.where((g > 0) & (cls < 0), 1.0,
                   np.where((g < 0) & (cls > 0), -1.0, 0.0)),
                    index=open.index, dtype=float)
    b = val.where(~g.isna())
    return b.diff(5).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapgomean_40d_slope_v023_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = open - pc
    cls = closeadj - open
    raw = np.sign(g) * np.sign(cls)
    b = raw.rolling(40, min_periods=20).mean()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapcontinue_30d_slope_v024_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    intra = (closeadj - open) / open.replace(0.0, np.nan)
    raw = g * intra
    b = raw.rolling(30, min_periods=15).mean()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_upstrk_1d_slope_v025_signal(open, close):
    pc = close.shift(1)
    g = open - pc
    up = (g > 0).astype(float).where(~g.isna())
    grp = (up != up.shift(1)).cumsum()
    b = up.groupby(grp).cumsum() * up
    return b.diff(5).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_dnstrk_1d_slope_v026_signal(open, close):
    pc = close.shift(1)
    g = open - pc
    dn = (g < 0).astype(float).where(~g.isna())
    grp = (dn != dn.shift(1)).cumsum()
    b = dn.groupby(grp).cumsum() * dn
    return b.diff(5).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapsignstrk_1d_slope_v027_signal(open, close):
    pc = close.shift(1)
    g = open - pc
    up = (g > 0).astype(float).where(~g.isna())
    dn = (g < 0).astype(float).where(~g.isna())
    grp_u = (up != up.shift(1)).cumsum()
    grp_d = (dn != dn.shift(1)).cumsum()
    rl_u = up.groupby(grp_u).cumsum() * up
    rl_d = dn.groupby(grp_d).cumsum() * dn
    b = rl_u - rl_d
    return b.diff(5).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_upcnt_20d_slope_v028_signal(open, close):
    pc = close.shift(1)
    g = open - pc
    up = (g > 0).astype(float).where(~g.isna())
    b = up.rolling(20, min_periods=20).sum()
    return b.diff(5).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_dncnt_40d_slope_v029_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = open - pc
    dn = (g < 0).astype(float).where(~g.isna())
    b = dn.rolling(40, min_periods=40).sum()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_bigcnt_60d_slope_v030_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    big = (g.abs() > 0.01).astype(float).where(~g.isna())
    b = big.rolling(60, min_periods=60).sum()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_sigcnt_50d_slope_v031_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    sd = g.rolling(50, min_periods=50).std(ddof=1)
    big = (g.abs() > sd).astype(float).where(~g.isna() & ~sd.isna())
    b = big.rolling(50, min_periods=50).sum()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_maxup_30d_slope_v032_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    pos = g.where(g > 0)
    b = pos.rolling(30, min_periods=5).max()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_maxdn_60d_slope_v033_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    neg = (-g).where(g < 0)
    b = neg.rolling(60, min_periods=10).max()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_posneg_30d_slope_v034_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    pmean = g.where(g > 0).rolling(30, min_periods=5).mean()
    nmean = (-g).where(g < 0).rolling(30, min_periods=5).mean()
    b = pmean - nmean
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_extrme_50d_slope_v035_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    b = g.rolling(50, min_periods=50).max() + g.abs().rolling(50, min_periods=50).max()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_grtorng_1d_slope_v036_signal(open, high, low, close):
    pc = close.shift(1)
    g = (open - pc).abs()
    rng = (high - low).replace(0.0, np.nan)
    b = g / rng
    return b.diff(5).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_grtoprng_1d_slope_v037_signal(open, high, low, close):
    pc = close.shift(1)
    g = (open - pc).abs()
    prng = (high.shift(1) - low.shift(1)).replace(0.0, np.nan)
    b = g / prng
    return b.diff(5).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_grtoatrmean_14d_slope_v038_signal(open, high, low, close):
    pc = close.shift(1)
    g = (open - pc).abs()
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    r = g / atr.replace(0.0, np.nan)
    b = r.rolling(14, min_periods=14).mean()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_grbig_30d_slope_v039_signal(open, high, low, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = g / rng
    b = r.rolling(30, min_periods=15).mean()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_dayslast_60d_slope_v040_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    big = (g.abs() > 0.01).astype(float).where(~g.isna())
    n = 60
    def _last_one(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return float(n)
        return float(len(x) - 1 - idx[-1])
    b = big.rolling(n, min_periods=n).apply(_last_one, raw=True)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_dayslastup_40d_slope_v041_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = open - pc
    up = (g > 0).astype(float).where(~g.isna())
    n = 40
    def _last_one(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return float(n)
        return float(len(x) - 1 - idx[-1])
    b = up.rolling(n, min_periods=n).apply(_last_one, raw=True)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_dayslastdn_40d_slope_v042_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = open - pc
    dn = (g < 0).astype(float).where(~g.isna())
    n = 40
    def _last_one(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return float(n)
        return float(len(x) - 1 - idx[-1])
    b = dn.rolling(n, min_periods=n).apply(_last_one, raw=True)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapskew_60d_slope_v043_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    b = g.rolling(60, min_periods=60).skew()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapkurt_80d_slope_v044_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    b = g.rolling(80, min_periods=80).kurt()
    return b.diff(63).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapac1_50d_slope_v045_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    def _ac1(x):
        x = np.asarray(x, dtype=float)
        if not np.all(np.isfinite(x)):
            return np.nan
        x0 = x[:-1]; x1 = x[1:]
        m0 = x0.mean(); m1 = x1.mean()
        v0 = x0.std(ddof=1); v1 = x1.std(ddof=1)
        if v0 <= 0.0 or v1 <= 0.0:
            return np.nan
        return float(((x0 - m0) * (x1 - m1)).mean() / (v0 * v1))
    b = g.rolling(50, min_periods=50).apply(_ac1, raw=True)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapac2_70d_slope_v046_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    def _ac2(x):
        x = np.asarray(x, dtype=float)
        if not np.all(np.isfinite(x)):
            return np.nan
        x0 = x[:-2]; x1 = x[2:]
        m0 = x0.mean(); m1 = x1.mean()
        v0 = x0.std(ddof=1); v1 = x1.std(ddof=1)
        if v0 <= 0.0 or v1 <= 0.0:
            return np.nan
        return float(((x0 - m0) * (x1 - m1)).mean() / (v0 * v1))
    b = g.rolling(70, min_periods=70).apply(_ac2, raw=True)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapcls_1d_slope_v047_signal(open, close):
    pc = close.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    val = pd.Series(np.where(g.abs() < 0.001, 0.0,
                   np.where((g > 0) & (g < 0.01), 1.0,
                   np.where(g >= 0.01, 2.0,
                   np.where((g < 0) & (g > -0.01), -1.0, -2.0)))),
                    index=open.index, dtype=float)
    b = val.where(~g.isna())
    return b.diff(5).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapclsmean_30d_slope_v048_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    val = pd.Series(np.where(g.abs() < 0.001, 0.0,
                   np.where((g > 0) & (g < 0.01), 1.0,
                   np.where(g >= 0.01, 2.0,
                   np.where((g < 0) & (g > -0.01), -1.0, -2.0)))),
                    index=open.index, dtype=float)
    val = val.where(~g.isna())
    b = val.rolling(30, min_periods=30).mean()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_lgapsum_60d_slope_v049_signal(open, closeadj):
    pc = closeadj.shift(1)
    lg = np.log(open / pc.replace(0.0, np.nan))
    b = lg.rolling(60, min_periods=60).sum()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_lgapewm_30d_slope_v050_signal(open, closeadj):
    pc = closeadj.shift(1)
    lg = np.log(open / pc.replace(0.0, np.nan))
    b = lg.ewm(span=30, adjust=False, min_periods=30).mean()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_lgapewmabs_50d_slope_v051_signal(open, closeadj):
    pc = closeadj.shift(1)
    lg = np.log(open / pc.replace(0.0, np.nan)).abs()
    b = lg.ewm(span=50, adjust=False, min_periods=50).mean()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapextrnk_30d_slope_v052_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = ((open - pc) / pc.replace(0.0, np.nan)).abs()
    rmax = g.rolling(30, min_periods=30).max()
    b = rmax.rolling(120, min_periods=60).rank(pct=True)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapaccel_1d_slope_v053_signal(open, close):
    pc = close.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    b = g - 2.0 * g.shift(1) + g.shift(2)
    return b.diff(5).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapsigmoid_30d_slope_v054_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    s = 1.0 / (1.0 + np.exp(-50.0 * g))
    b = s.rolling(30, min_periods=30).mean()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapvsret_30d_slope_v055_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    pret = closeadj.pct_change(1).shift(1)
    b = g.rolling(30, min_periods=30).corr(pret)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapvsfwd_40d_slope_v056_signal(open, high, low, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    intra = (closeadj - open) / open.replace(0.0, np.nan)
    b = g.rolling(40, min_periods=40).corr(intra)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapintravar_30d_slope_v057_signal(open, high, low, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    rlog = np.log((high / low).replace(0.0, np.nan))
    gv = g.rolling(30, min_periods=30).var(ddof=1)
    rv = rlog.rolling(30, min_periods=30).var(ddof=1)
    b = gv / rv.replace(0.0, np.nan)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapvol_50d_slope_v058_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    r = closeadj.pct_change(1)
    g_sd = g.rolling(50, min_periods=50).std(ddof=1)
    r_sd = r.rolling(50, min_periods=50).std(ddof=1)
    b = g_sd / r_sd.replace(0.0, np.nan)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_closegap_1d_slope_v059_signal(open, close):
    pc = close.shift(1)
    g = open - pc
    b = (close - pc) / g.replace(0.0, np.nan)
    return b.diff(5).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_closegapmean_30d_slope_v060_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = open - pc
    ratio = (closeadj - pc) / g.replace(0.0, np.nan)
    ratio = ratio.clip(lower=-3.0, upper=3.0)
    b = ratio.rolling(30, min_periods=15).mean()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_uppct_60d_slope_v061_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = open - pc
    up = (g > 0).astype(float).where(~g.isna())
    b = up.rolling(60, min_periods=60).mean()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_dnpct_90d_slope_v062_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = open - pc
    dn = (g < 0).astype(float).where(~g.isna())
    b = dn.rolling(90, min_periods=90).mean()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_aligntrend_40d_slope_v063_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = open - pc
    trend = closeadj - closeadj.shift(20)
    raw = np.sign(g) * np.sign(trend)
    b = raw.rolling(40, min_periods=20).mean()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_aligntrendlng_80d_slope_v064_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = open - pc
    trend = closeadj - closeadj.shift(60)
    raw = np.sign(g) * np.sign(trend)
    b = raw.rolling(80, min_periods=40).mean()
    return b.diff(63).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapclust_30d_slope_v065_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    sqs = (g * g).rolling(30, min_periods=30).sum()
    abs_sum = g.abs().rolling(30, min_periods=30).sum()
    b = sqs / (abs_sum * abs_sum).replace(0.0, np.nan)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapcumabs_120d_slope_v066_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = ((open - pc) / pc.replace(0.0, np.nan)).abs()
    r = closeadj.pct_change(1).abs()
    b = g.rolling(120, min_periods=120).sum() / r.rolling(120, min_periods=120).sum().replace(0.0, np.nan)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gappgap_1d_slope_v067_signal(open, close):
    pc = close.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    b = g - g.shift(1)
    return b.diff(5).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapfollow_40d_slope_v068_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = open - pc
    s = np.sign(g)
    same = (s == s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    b = same.rolling(40, min_periods=40).sum()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapafterup_50d_slope_v069_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    rsign = np.sign(closeadj.diff())
    up3 = ((rsign.shift(1) > 0) & (rsign.shift(2) > 0) & (rsign.shift(3) > 0)).astype(float)
    masked = g.where(up3 > 0.5)
    b = masked.rolling(50, min_periods=5).mean()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapafterdn_50d_slope_v070_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    rsign = np.sign(closeadj.diff())
    dn3 = ((rsign.shift(1) < 0) & (rsign.shift(2) < 0) & (rsign.shift(3) < 0)).astype(float)
    masked = g.where(dn3 > 0.5)
    b = masked.rolling(50, min_periods=5).mean()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_unfilcnt_40d_slope_v071_signal(open, high, low, closeadj):
    pc = closeadj.shift(1)
    g = open - pc
    up_unf = ((g > 0) & (low > pc)).astype(float)
    dn_unf = ((g < 0) & (high < pc)).astype(float)
    unf = (up_unf + dn_unf).where(~g.isna())
    b = unf.rolling(40, min_periods=40).sum()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_unfilfrac_60d_slope_v072_signal(open, high, low, closeadj):
    pc = closeadj.shift(1)
    g = open - pc
    up_unf = ((g > 0) & (low > pc)).astype(float)
    dn_unf = ((g < 0) & (high < pc)).astype(float)
    unf = (up_unf + dn_unf).where(~g.isna())
    has_gap = (g != 0.0).astype(float).where(~g.isna())
    s_unf = unf.rolling(60, min_periods=30).sum()
    s_tot = has_gap.rolling(60, min_periods=30).sum()
    b = s_unf / s_tot.replace(0.0, np.nan)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapdiff_short_slope_v073_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    m10 = g.rolling(10, min_periods=10).mean()
    m60 = g.rolling(60, min_periods=60).mean()
    b = m10 - m60
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapabsdiff_60d_slope_v074_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = ((open - pc) / pc.replace(0.0, np.nan)).abs()
    m20 = g.rolling(20, min_periods=20).mean()
    m60 = g.rolling(60, min_periods=60).mean()
    b = m20 - m60
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapwgtdir_40d_slope_v075_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    w = g * g
    sg = np.sign(g) * w
    num = sg.rolling(40, min_periods=40).sum()
    den = w.rolling(40, min_periods=40).sum()
    b = num / den.replace(0.0, np.nan)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


# ----- 076-150: bases from file 2 -----------------------------------------


def f07gb_f07_gap_behavior_smallcnt_50d_slope_v076_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    sm = ((g.abs() > 0.001) & (g.abs() <= 0.005)).astype(float).where(~g.isna())
    b = sm.rolling(50, min_periods=50).sum()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_medcnt_50d_slope_v077_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    md = ((g.abs() > 0.005) & (g.abs() <= 0.015)).astype(float).where(~g.isna())
    b = md.rolling(50, min_periods=50).sum()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_lrgcnt_80d_slope_v078_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    lg = (g.abs() > 0.015).astype(float).where(~g.isna())
    b = lg.rolling(80, min_periods=80).sum()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapq90_80d_slope_v079_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    b = g.rolling(80, min_periods=80).quantile(0.90)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapq10_80d_slope_v080_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    b = g.rolling(80, min_periods=80).quantile(0.10)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapsymq_60d_slope_v081_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    q9 = g.rolling(60, min_periods=60).quantile(0.90)
    q1 = g.rolling(60, min_periods=60).quantile(0.10)
    b = q9 + q1
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapvsvol_50d_slope_v082_signal(open, closeadj, volume):
    pc = closeadj.shift(1)
    g = ((open - pc) / pc.replace(0.0, np.nan)).abs()
    lv = np.log(volume.replace(0.0, np.nan))
    b = g.rolling(50, min_periods=50).corr(lv)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapvslag_40d_slope_v083_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    b = g.rolling(40, min_periods=40).corr(g.shift(2))
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapvsrange_40d_slope_v084_signal(open, high, low, closeadj):
    pc = closeadj.shift(1)
    g = ((open - pc) / pc.replace(0.0, np.nan)).abs()
    rng = (high - low) / closeadj.replace(0.0, np.nan)
    b = g.rolling(40, min_periods=40).corr(rng)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapsdr_30d_slope_v085_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    r = closeadj.pct_change(1).abs()
    gsd = g.rolling(30, min_periods=30).std(ddof=1)
    rmu = r.rolling(30, min_periods=30).mean()
    b = gsd / rmu.replace(0.0, np.nan)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapmaxnrm_60d_slope_v086_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = ((open - pc) / pc.replace(0.0, np.nan)).abs()
    mx = g.rolling(60, min_periods=60).max()
    mu = g.rolling(60, min_periods=60).mean()
    b = mx / mu.replace(0.0, np.nan)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapdiffstd_20d_slope_v087_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    dg = g - g.shift(1)
    b = dg.rolling(20, min_periods=20).std(ddof=1)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapcounttrend_80d_slope_v088_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    has = (g.abs() > 0.002).astype(float).where(~g.isna())
    c80 = has.rolling(80, min_periods=80).sum()
    c40 = has.rolling(40, min_periods=40).sum()
    b = c80 / c40.replace(0.0, np.nan)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapcummean_200d_slope_v089_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    b = g.rolling(200, min_periods=200).mean()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapcumabs_200d_slope_v090_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = ((open - pc) / pc.replace(0.0, np.nan)).abs()
    b = g.rolling(200, min_periods=200).mean()
    return b.diff(63).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_overnightfrac_60d_slope_v091_signal(open, closeadj):
    pc = closeadj.shift(1)
    on = np.log(open / pc.replace(0.0, np.nan))
    c2c = np.log(closeadj / pc.replace(0.0, np.nan))
    b = on.rolling(60, min_periods=60).sum() / c2c.rolling(60, min_periods=60).sum().replace(0.0, np.nan)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_intradayfrac_60d_slope_v092_signal(open, closeadj):
    pc = closeadj.shift(1)
    intra = np.log(closeadj / open.replace(0.0, np.nan))
    on_abs = np.log(open / pc.replace(0.0, np.nan)).abs()
    b = intra.rolling(60, min_periods=60).sum() / on_abs.rolling(60, min_periods=60).sum().replace(0.0, np.nan)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapwdvol_30d_slope_v093_signal(open, closeadj, volume):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    gv = (g * volume).rolling(30, min_periods=30).sum()
    v = volume.rolling(30, min_periods=30).sum()
    b = gv / v.replace(0.0, np.nan)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gaplvolz_50d_slope_v094_signal(open, closeadj, volume):
    pc = closeadj.shift(1)
    g = ((open - pc) / pc.replace(0.0, np.nan)).abs()
    lv = np.log(volume.replace(0.0, np.nan))
    mu = lv.rolling(50, min_periods=50).mean()
    sd = lv.rolling(50, min_periods=50).std(ddof=1)
    z = (lv - mu) / sd.replace(0.0, np.nan)
    b = (g * z).rolling(50, min_periods=50).mean()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_maxupstrk_60d_slope_v095_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = open - pc
    up = (g > 0).astype(float).where(~g.isna())
    def _longest(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)):
            return np.nan
        best = 0; cur = 0
        for v in x:
            if v > 0.5:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)
    b = up.rolling(60, min_periods=60).apply(_longest, raw=True)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_maxdnstrk_60d_slope_v096_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = open - pc
    dn = (g < 0).astype(float).where(~g.isna())
    def _longest(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)):
            return np.nan
        best = 0; cur = 0
        for v in x:
            if v > 0.5:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)
    b = dn.rolling(60, min_periods=60).apply(_longest, raw=True)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapdownsskew_80d_slope_v097_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    neg = g.where(g < 0)
    sd = neg.rolling(80, min_periods=10).std(ddof=1)
    mu = neg.rolling(80, min_periods=10).mean()
    m3 = ((neg - mu) ** 3).rolling(80, min_periods=10).mean()
    b = m3 / (sd ** 3).replace(0.0, np.nan)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gaptaildiff_80d_slope_v098_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    q95 = g.rolling(80, min_periods=80).quantile(0.95)
    q05 = g.rolling(80, min_periods=80).quantile(0.05)
    q75 = g.rolling(80, min_periods=80).quantile(0.75)
    q25 = g.rolling(80, min_periods=80).quantile(0.25)
    b = (q95 - q05) / (q75 - q25).replace(0.0, np.nan)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_avgupgap_60d_slope_v099_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    pos = g.where(g > 0)
    b = pos.rolling(60, min_periods=10).mean()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_avgdngap_60d_slope_v100_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    neg = (-g).where(g < 0)
    b = neg.rolling(60, min_periods=10).mean()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapatop_1d_slope_v101_signal(open, high, low, close):
    pc = close.shift(1)
    g = open - pc
    span = (high.shift(1) - low.shift(1)).replace(0.0, np.nan)
    pos = (open - low.shift(1)) / span
    b = pos.where(g != 0.0)
    return b.diff(5).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapatopmean_30d_slope_v102_signal(open, high, low, closeadj):
    pc = closeadj.shift(1)
    g = open - pc
    span = (high.shift(1) - low.shift(1)).replace(0.0, np.nan)
    pos = (open - low.shift(1)) / span
    pos = pos.where(g != 0.0)
    b = pos.rolling(30, min_periods=15).mean()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_fillewm_50d_slope_v103_signal(open, high, low, closeadj):
    pc = closeadj.shift(1)
    g = open - pc
    up_fill = (low <= pc) & (g > 0)
    dn_fill = (high >= pc) & (g < 0)
    filled = (up_fill | dn_fill).astype(float).where(g != 0.0)
    b = filled.ewm(span=50, adjust=False, min_periods=20).mean()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_fillpart_80d_slope_v104_signal(open, high, low, closeadj):
    pc = closeadj.shift(1)
    g = open - pc
    up_amt = (open - low) / g.where(g > 0, np.nan)
    dn_amt = (high - open) / (-g).where(g < 0, np.nan)
    raw = up_amt.combine_first(dn_amt).clip(lower=0.0, upper=1.0)
    b = raw.rolling(80, min_periods=20).median()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_postgaprng_1d_slope_v105_signal(open, high, low, close):
    pc = close.shift(1)
    g = open - pc
    up_mv = (high - open) / g.where(g > 0, np.nan)
    dn_mv = (open - low) / (-g).where(g < 0, np.nan)
    raw = up_mv.combine_first(dn_mv)
    b = raw.clip(lower=0.0, upper=10.0)
    return b.diff(5).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_postgapbeta_50d_slope_v106_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    intra = (closeadj - open) / open.replace(0.0, np.nan)
    cov = g.rolling(50, min_periods=50).cov(intra)
    var = g.rolling(50, min_periods=50).var(ddof=1)
    b = cov / var.replace(0.0, np.nan)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapsdratio_60d_slope_v107_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    s60 = g.rolling(60, min_periods=60).std(ddof=1)
    s200 = g.rolling(200, min_periods=200).std(ddof=1)
    b = s60 / s200.replace(0.0, np.nan)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapmagchg_30d_slope_v108_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = ((open - pc) / pc.replace(0.0, np.nan)).abs()
    m30 = g.rolling(30, min_periods=30).mean()
    m90 = g.rolling(90, min_periods=90).mean()
    b = np.log(m30.replace(0.0, np.nan) / m90.replace(0.0, np.nan))
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapewmx_60d_slope_v109_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    fast = g.ewm(span=10, adjust=False, min_periods=10).mean()
    slow = g.ewm(span=40, adjust=False, min_periods=40).mean()
    s = np.sign(fast - slow)
    b = s.where(~fast.isna() & ~slow.isna())
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapewmspr_60d_slope_v110_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    f15 = g.ewm(span=15, adjust=False, min_periods=15).mean()
    s60 = g.ewm(span=60, adjust=False, min_periods=60).mean()
    b = f15 - s60
    return b.diff(63).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapintsgn_30d_slope_v111_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = open - pc
    intra = closeadj - open
    s_g = np.sign(g).where(~g.isna())
    s_i = np.sign(intra).where(~intra.isna())
    raw = s_g - s_i
    b = raw.rolling(30, min_periods=15).mean()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapfaderate_50d_slope_v112_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = open - pc
    intra = closeadj - open
    fade = ((g * intra) < 0).astype(float).where(~g.isna() & ~intra.isna() & (g != 0.0))
    b = fade.rolling(50, min_periods=25).mean()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gaprecencysum_30d_slope_v113_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = ((open - pc) / pc.replace(0.0, np.nan)).abs()
    b = g.ewm(alpha=0.1, adjust=False, min_periods=30).mean()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapdensity_60d_slope_v114_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    has = (g.abs() > 0.0005).astype(float).where(~g.isna())
    b = has.rolling(60, min_periods=60).mean()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapcondup_50d_slope_v115_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    prev_up = (closeadj.shift(1) > closeadj.shift(2)).astype(float)
    cond = g.where(prev_up > 0.5)
    b = cond.rolling(50, min_periods=10).mean()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapconddn_50d_slope_v116_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    prev_dn = (closeadj.shift(1) < closeadj.shift(2)).astype(float)
    cond = g.where(prev_dn > 0.5)
    b = cond.rolling(50, min_periods=10).mean()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapnew_high_30d_slope_v117_signal(open, high, low, closeadj):
    pc = closeadj.shift(1)
    g = open - pc
    cond = ((g > 0) & (high > high.shift(1))).astype(float).where(~g.isna())
    b = cond.rolling(30, min_periods=30).sum()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapnew_low_30d_slope_v118_signal(open, high, low, closeadj):
    pc = closeadj.shift(1)
    g = open - pc
    cond = ((g < 0) & (low < low.shift(1))).astype(float).where(~g.isna())
    b = cond.rolling(30, min_periods=30).sum()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gappxpos_50d_slope_v119_signal(open, high, low, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc).abs()
    rng = high.rolling(50, min_periods=50).max() - low.rolling(50, min_periods=50).min()
    r = g / rng.replace(0.0, np.nan)
    b = r.rolling(50, min_periods=50).mean()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapboxpos_30d_slope_v120_signal(open, high, low, closeadj):
    pc = closeadj.shift(1)
    g = open - pc
    box_top = high.shift(1).rolling(30, min_periods=30).max()
    diff = (open - box_top) / closeadj.replace(0.0, np.nan)
    b = diff.where(g > 0)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapprodint_20d_slope_v121_signal(open, close):
    pc = close.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    intra = (close - open) / open.replace(0.0, np.nan)
    b = (g * intra).rolling(20, min_periods=20).mean()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapsignsumlng_120d_slope_v122_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = open - pc
    s = np.sign(g).where(~g.isna())
    b = s.rolling(120, min_periods=120).sum()
    return b.diff(63).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapcv_60d_slope_v123_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    sd = g.rolling(60, min_periods=60).std(ddof=1)
    mu = g.abs().rolling(60, min_periods=60).mean()
    b = sd / mu.replace(0.0, np.nan)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gappnratio_30d_slope_v124_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = open - pc
    up = (g > 0).astype(float).where(~g.isna())
    dn = (g < 0).astype(float).where(~g.isna())
    su = up.rolling(30, min_periods=30).sum()
    sd = dn.rolling(30, min_periods=30).sum()
    b = su / sd.replace(0.0, np.nan)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapmom_5d_slope_v125_signal(open, close):
    pc = close.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    b = g.rolling(5, min_periods=5).sum()
    return b.diff(5).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapmomlong_90d_slope_v126_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    b = g.rolling(90, min_periods=90).sum()
    return b.diff(63).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapregslp_60d_slope_v127_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    n = 60
    t = np.arange(n, dtype=float)
    tmean = t.mean()
    tvar = ((t - tmean) ** 2).sum()
    def _slp(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        xm = x.mean()
        return float(((t - tmean) * (x - xm)).sum() / tvar)
    b = g.rolling(n, min_periods=n).apply(_slp, raw=True)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapabsregslp_80d_slope_v128_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = ((open - pc) / pc.replace(0.0, np.nan)).abs()
    n = 80
    t = np.arange(n, dtype=float)
    tmean = t.mean()
    tvar = ((t - tmean) ** 2).sum()
    def _slp(x):
        if not np.all(np.isfinite(x)):
            return np.nan
        xm = x.mean()
        return float(((t - tmean) * (x - xm)).sum() / tvar)
    b = g.rolling(n, min_periods=n).apply(_slp, raw=True)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gaphvol_40d_slope_v129_signal(open, closeadj, volume):
    pc = closeadj.shift(1)
    g = ((open - pc) / pc.replace(0.0, np.nan)).abs()
    lv = np.log(volume.replace(0.0, np.nan))
    q75 = lv.rolling(40, min_periods=40).quantile(0.75)
    big = (lv >= q75)
    cond = g.where(big)
    b = cond.rolling(40, min_periods=10).mean()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gaplvol_40d_slope_v130_signal(open, closeadj, volume):
    pc = closeadj.shift(1)
    g = ((open - pc) / pc.replace(0.0, np.nan)).abs()
    lv = np.log(volume.replace(0.0, np.nan))
    q25 = lv.rolling(40, min_periods=40).quantile(0.25)
    sm = (lv <= q25)
    cond = g.where(sm)
    b = cond.rolling(40, min_periods=10).mean()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapatropmean_30d_slope_v131_signal(open, high, low, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc).abs()
    tr = pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    raw = (g - atr) / atr.replace(0.0, np.nan)
    b = raw.rolling(30, min_periods=15).mean()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapcrosssym_60d_slope_v132_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    sk = g.rolling(60, min_periods=60).skew()
    kt = g.rolling(60, min_periods=60).kurt()
    b = sk * kt
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapabsrnk_30d_slope_v133_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = ((open - pc) / pc.replace(0.0, np.nan)).abs()
    pr = g.rolling(30, min_periods=30).rank(pct=True)
    b = pr.rolling(5, min_periods=5).mean()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gaplargefr_60d_slope_v134_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = ((open - pc) / pc.replace(0.0, np.nan)).abs()
    def _topfr(x):
        x = np.asarray(x, dtype=float)
        if not np.all(np.isfinite(x)) or x.sum() <= 0.0:
            return np.nan
        top = np.sort(x)[-5:].sum()
        return float(top / x.sum())
    b = g.rolling(60, min_periods=60).apply(_topfr, raw=True)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_unfildur_60d_slope_v135_signal(open, high, low, closeadj):
    pc = closeadj.shift(1)
    g = open - pc
    up_unf = ((g > 0) & (low > pc)).astype(float)
    dn_unf = ((g < 0) & (high < pc)).astype(float)
    unf = (up_unf + dn_unf).where(~g.isna())
    n = 60
    def _last_one(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return float(n)
        return float(len(x) - 1 - idx[-1])
    b = unf.rolling(n, min_periods=n).apply(_last_one, raw=True)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_unfilbias_50d_slope_v136_signal(open, high, low, closeadj):
    pc = closeadj.shift(1)
    g = open - pc
    up_unf = ((g > 0) & (low > pc)).astype(float)
    dn_unf = ((g < 0) & (high < pc)).astype(float)
    u = up_unf.rolling(50, min_periods=50).sum()
    d = dn_unf.rolling(50, min_periods=50).sum()
    b = (u - d) / 50.0
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapvssma_50d_slope_v137_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    s50 = closeadj.rolling(50, min_periods=50).mean()
    rel = (open - s50) / s50.replace(0.0, np.nan)
    gmu = g.rolling(50, min_periods=50).mean()
    rmu = rel.rolling(50, min_periods=50).mean()
    b = gmu - rmu
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapvsema_60d_slope_v138_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = open - pc
    ema = closeadj.ewm(span=60, adjust=False, min_periods=60).mean()
    trend = open - ema
    raw = np.sign(g) * np.sign(trend)
    b = raw.rolling(40, min_periods=20).mean()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapvolblend_30d_slope_v139_signal(open, closeadj, volume):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    vma = volume.rolling(30, min_periods=30).mean()
    vsig = np.sign(volume - vma)
    b = (g * vsig).rolling(30, min_periods=30).mean()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapextfrac_120d_slope_v140_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    sd = g.rolling(120, min_periods=120).std(ddof=1)
    ext = (g.abs() > 2.0 * sd).astype(float).where(~g.isna() & ~sd.isna())
    b = ext.rolling(120, min_periods=120).mean()
    return b.diff(63).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapfadewin_60d_slope_v141_signal(open, high, low, closeadj):
    pc = closeadj.shift(1)
    g = open - pc
    fade_up = ((g > 0) & (closeadj < pc)).astype(float)
    fade_dn = ((g < 0) & (closeadj > pc)).astype(float)
    fade = (fade_up + fade_dn).where(~g.isna() & (g != 0.0))
    b = fade.rolling(60, min_periods=30).mean()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_postupgapret_40d_slope_v142_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = open - pc
    next_ret = closeadj.pct_change(1).shift(-1)
    up_day = (g > 0).astype(float)
    cond = next_ret.where(up_day > 0.5)
    b = cond.rolling(40, min_periods=10).mean()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_postdngapret_40d_slope_v143_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = open - pc
    next_ret = closeadj.pct_change(1).shift(-1)
    dn_day = (g < 0).astype(float)
    cond = next_ret.where(dn_day > 0.5)
    b = cond.rolling(40, min_periods=10).mean()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapvssvap_50d_slope_v144_signal(open, high, low, closeadj, volume):
    pc = closeadj.shift(1)
    g = (open - pc) / pc.replace(0.0, np.nan)
    vw = (closeadj * volume).rolling(50, min_periods=50).sum() / volume.rolling(50, min_periods=50).sum().replace(0.0, np.nan)
    rel = (open - vw) / vw.replace(0.0, np.nan)
    b = g - rel
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapsignstab_30d_slope_v145_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = open - pc
    s = np.sign(g).where(~g.isna())
    b = s.rolling(30, min_periods=30).sum().abs() / 30.0
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapscaledabs_40d_slope_v146_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = ((open - pc) / pc.replace(0.0, np.nan)).abs()
    r = closeadj.pct_change(1)
    rv = r.rolling(40, min_periods=40).std(ddof=1)
    s = g / rv.replace(0.0, np.nan)
    b = s.rolling(40, min_periods=40).mean()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapinbar_60d_slope_v147_signal(open, high, low, closeadj):
    pc = closeadj.shift(1)
    g = open - pc
    inside = ((open >= low.shift(1)) & (open <= high.shift(1))).astype(float).where(~g.isna())
    b = inside.rolling(60, min_periods=60).mean()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapoutbar_60d_slope_v148_signal(open, high, low, closeadj):
    pc = closeadj.shift(1)
    g = open - pc
    up = (open > high.shift(1)).astype(float).where(~g.isna())
    dn = (open < low.shift(1)).astype(float).where(~g.isna())
    b = up.rolling(60, min_periods=60).mean() - dn.rolling(60, min_periods=60).mean()
    return b.diff(63).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapsharpeabs_60d_slope_v149_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = ((open - pc) / pc.replace(0.0, np.nan)).abs()
    med = g.rolling(60, min_periods=60).median()
    def _mad(x):
        x = np.asarray(x, dtype=float)
        if not np.all(np.isfinite(x)):
            return np.nan
        m = np.median(x)
        return float(np.median(np.abs(x - m)))
    mad = g.rolling(60, min_periods=60).apply(_mad, raw=True)
    b = med / mad.replace(0.0, np.nan)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)


def f07gb_f07_gap_behavior_gapnegac_60d_slope_v150_signal(open, closeadj):
    pc = closeadj.shift(1)
    g = ((open - pc) / pc.replace(0.0, np.nan)).abs()
    def _ac3(x):
        x = np.asarray(x, dtype=float)
        if not np.all(np.isfinite(x)):
            return np.nan
        x0 = x[:-3]; x1 = x[3:]
        m0 = x0.mean(); m1 = x1.mean()
        v0 = x0.std(ddof=1); v1 = x1.std(ddof=1)
        if v0 <= 0.0 or v1 <= 0.0:
            return np.nan
        return float(((x0 - m0) * (x1 - m1)).mean() / (v0 * v1))
    b = g.rolling(60, min_periods=60).apply(_ac3, raw=True)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


def _e(fn, *inputs):
    return fn.__name__, {"inputs": list(inputs), "func": fn}


f07_gap_behavior_slope_001_150_REGISTRY = dict([
    _e(f07gb_f07_gap_behavior_gappct_1d_slope_v001_signal, "open", "close"),
    _e(f07gb_f07_gap_behavior_lgapcumlong_120d_slope_v002_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapabsnrm_5d_slope_v003_signal, "open", "close"),
    _e(f07gb_f07_gap_behavior_gapsgn_1d_slope_v004_signal, "open", "close"),
    _e(f07gb_f07_gap_behavior_gapmean_10d_slope_v005_signal, "open", "close"),
    _e(f07gb_f07_gap_behavior_gapsum_21d_slope_v006_signal, "open", "close"),
    _e(f07gb_f07_gap_behavior_gapmed_50d_slope_v007_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapsumabs_30d_slope_v008_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapstd_20d_slope_v009_signal, "open", "close"),
    _e(f07gb_f07_gap_behavior_gapmad_40d_slope_v010_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gaprng_30d_slope_v011_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapiqr_60d_slope_v012_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_bigfrac_30d_slope_v013_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_posnegratio_120d_slope_v014_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gaprnkmed_50d_slope_v015_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gaprnkabs_80d_slope_v016_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_fillbin_1d_slope_v017_signal, "open", "high", "low", "close"),
    _e(f07gb_f07_gap_behavior_fillratio_1d_slope_v018_signal, "open", "high", "low", "close"),
    _e(f07gb_f07_gap_behavior_fillrate_30d_slope_v019_signal, "open", "high", "low", "closeadj"),
    _e(f07gb_f07_gap_behavior_partfillmean_20d_slope_v020_signal, "open", "high", "low", "close"),
    _e(f07gb_f07_gap_behavior_gapgo_1d_slope_v021_signal, "open", "close"),
    _e(f07gb_f07_gap_behavior_gaprev_1d_slope_v022_signal, "open", "close"),
    _e(f07gb_f07_gap_behavior_gapgomean_40d_slope_v023_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapcontinue_30d_slope_v024_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_upstrk_1d_slope_v025_signal, "open", "close"),
    _e(f07gb_f07_gap_behavior_dnstrk_1d_slope_v026_signal, "open", "close"),
    _e(f07gb_f07_gap_behavior_gapsignstrk_1d_slope_v027_signal, "open", "close"),
    _e(f07gb_f07_gap_behavior_upcnt_20d_slope_v028_signal, "open", "close"),
    _e(f07gb_f07_gap_behavior_dncnt_40d_slope_v029_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_bigcnt_60d_slope_v030_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_sigcnt_50d_slope_v031_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_maxup_30d_slope_v032_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_maxdn_60d_slope_v033_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_posneg_30d_slope_v034_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_extrme_50d_slope_v035_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_grtorng_1d_slope_v036_signal, "open", "high", "low", "close"),
    _e(f07gb_f07_gap_behavior_grtoprng_1d_slope_v037_signal, "open", "high", "low", "close"),
    _e(f07gb_f07_gap_behavior_grtoatrmean_14d_slope_v038_signal, "open", "high", "low", "close"),
    _e(f07gb_f07_gap_behavior_grbig_30d_slope_v039_signal, "open", "high", "low", "closeadj"),
    _e(f07gb_f07_gap_behavior_dayslast_60d_slope_v040_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_dayslastup_40d_slope_v041_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_dayslastdn_40d_slope_v042_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapskew_60d_slope_v043_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapkurt_80d_slope_v044_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapac1_50d_slope_v045_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapac2_70d_slope_v046_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapcls_1d_slope_v047_signal, "open", "close"),
    _e(f07gb_f07_gap_behavior_gapclsmean_30d_slope_v048_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_lgapsum_60d_slope_v049_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_lgapewm_30d_slope_v050_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_lgapewmabs_50d_slope_v051_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapextrnk_30d_slope_v052_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapaccel_1d_slope_v053_signal, "open", "close"),
    _e(f07gb_f07_gap_behavior_gapsigmoid_30d_slope_v054_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapvsret_30d_slope_v055_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapvsfwd_40d_slope_v056_signal, "open", "high", "low", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapintravar_30d_slope_v057_signal, "open", "high", "low", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapvol_50d_slope_v058_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_closegap_1d_slope_v059_signal, "open", "close"),
    _e(f07gb_f07_gap_behavior_closegapmean_30d_slope_v060_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_uppct_60d_slope_v061_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_dnpct_90d_slope_v062_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_aligntrend_40d_slope_v063_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_aligntrendlng_80d_slope_v064_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapclust_30d_slope_v065_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapcumabs_120d_slope_v066_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gappgap_1d_slope_v067_signal, "open", "close"),
    _e(f07gb_f07_gap_behavior_gapfollow_40d_slope_v068_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapafterup_50d_slope_v069_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapafterdn_50d_slope_v070_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_unfilcnt_40d_slope_v071_signal, "open", "high", "low", "closeadj"),
    _e(f07gb_f07_gap_behavior_unfilfrac_60d_slope_v072_signal, "open", "high", "low", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapdiff_short_slope_v073_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapabsdiff_60d_slope_v074_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapwgtdir_40d_slope_v075_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_smallcnt_50d_slope_v076_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_medcnt_50d_slope_v077_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_lrgcnt_80d_slope_v078_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapq90_80d_slope_v079_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapq10_80d_slope_v080_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapsymq_60d_slope_v081_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapvsvol_50d_slope_v082_signal, "open", "closeadj", "volume"),
    _e(f07gb_f07_gap_behavior_gapvslag_40d_slope_v083_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapvsrange_40d_slope_v084_signal, "open", "high", "low", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapsdr_30d_slope_v085_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapmaxnrm_60d_slope_v086_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapdiffstd_20d_slope_v087_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapcounttrend_80d_slope_v088_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapcummean_200d_slope_v089_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapcumabs_200d_slope_v090_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_overnightfrac_60d_slope_v091_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_intradayfrac_60d_slope_v092_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapwdvol_30d_slope_v093_signal, "open", "closeadj", "volume"),
    _e(f07gb_f07_gap_behavior_gaplvolz_50d_slope_v094_signal, "open", "closeadj", "volume"),
    _e(f07gb_f07_gap_behavior_maxupstrk_60d_slope_v095_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_maxdnstrk_60d_slope_v096_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapdownsskew_80d_slope_v097_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gaptaildiff_80d_slope_v098_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_avgupgap_60d_slope_v099_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_avgdngap_60d_slope_v100_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapatop_1d_slope_v101_signal, "open", "high", "low", "close"),
    _e(f07gb_f07_gap_behavior_gapatopmean_30d_slope_v102_signal, "open", "high", "low", "closeadj"),
    _e(f07gb_f07_gap_behavior_fillewm_50d_slope_v103_signal, "open", "high", "low", "closeadj"),
    _e(f07gb_f07_gap_behavior_fillpart_80d_slope_v104_signal, "open", "high", "low", "closeadj"),
    _e(f07gb_f07_gap_behavior_postgaprng_1d_slope_v105_signal, "open", "high", "low", "close"),
    _e(f07gb_f07_gap_behavior_postgapbeta_50d_slope_v106_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapsdratio_60d_slope_v107_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapmagchg_30d_slope_v108_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapewmx_60d_slope_v109_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapewmspr_60d_slope_v110_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapintsgn_30d_slope_v111_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapfaderate_50d_slope_v112_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gaprecencysum_30d_slope_v113_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapdensity_60d_slope_v114_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapcondup_50d_slope_v115_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapconddn_50d_slope_v116_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapnew_high_30d_slope_v117_signal, "open", "high", "low", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapnew_low_30d_slope_v118_signal, "open", "high", "low", "closeadj"),
    _e(f07gb_f07_gap_behavior_gappxpos_50d_slope_v119_signal, "open", "high", "low", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapboxpos_30d_slope_v120_signal, "open", "high", "low", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapprodint_20d_slope_v121_signal, "open", "close"),
    _e(f07gb_f07_gap_behavior_gapsignsumlng_120d_slope_v122_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapcv_60d_slope_v123_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gappnratio_30d_slope_v124_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapmom_5d_slope_v125_signal, "open", "close"),
    _e(f07gb_f07_gap_behavior_gapmomlong_90d_slope_v126_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapregslp_60d_slope_v127_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapabsregslp_80d_slope_v128_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gaphvol_40d_slope_v129_signal, "open", "closeadj", "volume"),
    _e(f07gb_f07_gap_behavior_gaplvol_40d_slope_v130_signal, "open", "closeadj", "volume"),
    _e(f07gb_f07_gap_behavior_gapatropmean_30d_slope_v131_signal, "open", "high", "low", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapcrosssym_60d_slope_v132_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapabsrnk_30d_slope_v133_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gaplargefr_60d_slope_v134_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_unfildur_60d_slope_v135_signal, "open", "high", "low", "closeadj"),
    _e(f07gb_f07_gap_behavior_unfilbias_50d_slope_v136_signal, "open", "high", "low", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapvssma_50d_slope_v137_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapvsema_60d_slope_v138_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapvolblend_30d_slope_v139_signal, "open", "closeadj", "volume"),
    _e(f07gb_f07_gap_behavior_gapextfrac_120d_slope_v140_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapfadewin_60d_slope_v141_signal, "open", "high", "low", "closeadj"),
    _e(f07gb_f07_gap_behavior_postupgapret_40d_slope_v142_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_postdngapret_40d_slope_v143_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapvssvap_50d_slope_v144_signal, "open", "high", "low", "closeadj", "volume"),
    _e(f07gb_f07_gap_behavior_gapsignstab_30d_slope_v145_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapscaledabs_40d_slope_v146_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapinbar_60d_slope_v147_signal, "open", "high", "low", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapoutbar_60d_slope_v148_signal, "open", "high", "low", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapsharpeabs_60d_slope_v149_signal, "open", "closeadj"),
    _e(f07gb_f07_gap_behavior_gapnegac_60d_slope_v150_signal, "open", "closeadj"),
])


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
    for name, entry in f07_gap_behavior_slope_001_150_REGISTRY.items():
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
        cnt = 0
        for i, a in enumerate(corr.columns):
            for j, b in enumerate(corr.columns):
                if j > i and corr.iloc[i, j] > 0.94:
                    print(f"  {a}  vs  {b}  ->  {corr.iloc[i, j]:.4f}")
                    cnt += 1
                    if cnt > 30:
                        break
            if cnt > 30:
                break
    assert max_corr <= 0.95 + 1e-9, f"max pairwise |corr|={max_corr:.4f} exceeds 0.95"
    print(f"OK slope_001_150: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
