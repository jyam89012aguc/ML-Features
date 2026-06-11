import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_FIVEYEAR = 1260
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 3)).rank(pct=True) - 0.5


# ===== folder domain primitives (margin TRAJECTORY: trend/change/stability/spread) =====
def _f24_slope(s, w):
    # OLS slope of s over a trailing window of length w (per-step trend)
    def _f(a):
        m = len(a)
        x = np.arange(m, dtype=float)
        x = x - x.mean()
        denom = (x ** 2).sum()
        if denom == 0.0:
            return np.nan
        return float(np.dot(x, a) / denom)

    return s.rolling(w, min_periods=max(2, w // 2)).apply(_f, raw=True)


def _f24_chg(s, w):
    # absolute change of a margin over w days
    return s - s.shift(w)


def _f24_pctchg(s, w):
    # relative change of a margin over w days
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _f24_stab(s, w):
    # stability = inverse coefficient of variation of the margin over w
    m = s.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    return m.abs() / sd.replace(0, np.nan)


def _f24_streak(s):
    # signed expansion streak: consecutive count of same-direction margin moves
    d = np.sign(s.diff())
    out = np.zeros(len(s), dtype=float)
    run = 0.0
    prev = 0.0
    vals = d.values
    for i in range(len(vals)):
        v = vals[i]
        if np.isnan(v):
            out[i] = np.nan
            run = 0.0
            prev = 0.0
            continue
        if v == prev and v != 0.0:
            run += v
        else:
            run = v
        prev = v
        out[i] = run
    return pd.Series(out, index=s.index)


def _f24_hitrate(s, w):
    # fraction of up-moves of the margin over w (expansion frequency)
    up = (s.diff() > 0).astype(float)
    return up.rolling(w, min_periods=max(2, w // 2)).mean()


# ============================================================
# gross-margin trend (OLS slope over a quarter)
def f24mt_f24_margin_trajectory_gmslope_63d_base_v001_signal(grossmargin):
    b = _f24_slope(grossmargin, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin trend over a half-year, normalized by the margin level
def f24mt_f24_margin_trajectory_gmslopen_126d_base_v002_signal(grossmargin):
    sl = _f24_slope(grossmargin, 126)
    b = sl / _mean(grossmargin, 126).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin trend over a year, z-scored vs its own history (de-trended trajectory)
def f24mt_f24_margin_trajectory_gmslopez_252d_base_v003_signal(grossmargin):
    sl = _f24_slope(grossmargin, 252)
    b = _z(sl, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin trend (OLS slope over a quarter)
def f24mt_f24_margin_trajectory_nmslope_63d_base_v004_signal(netmargin):
    b = _f24_slope(netmargin, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin trend over a half-year, normalized by level
def f24mt_f24_margin_trajectory_nmslopen_126d_base_v005_signal(netmargin):
    sl = _f24_slope(netmargin, 126)
    b = sl / _mean(netmargin, 126).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin trend (OLS slope over a half-year)
def f24mt_f24_margin_trajectory_emslope_126d_base_v006_signal(ebitdamargin):
    b = _f24_slope(ebitdamargin, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin trend over a year, percentile-ranked vs own history
def f24mt_f24_margin_trajectory_emsloperank_252d_base_v007_signal(ebitdamargin):
    sl = _f24_slope(ebitdamargin, 252)
    b = _rank(sl, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating margin (opinc/revenue) trend over a quarter
def f24mt_f24_margin_trajectory_omslope_63d_base_v008_signal(opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    b = _f24_slope(om, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating margin trend over a year, normalized by level
def f24mt_f24_margin_trajectory_omslopen_252d_base_v009_signal(opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    sl = _f24_slope(om, 252)
    b = sl / _mean(om, 252).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp/revenue gross-margin trend per unit of its own volatility (risk-adjusted GM trajectory)
def f24mt_f24_margin_trajectory_gpmslope_126d_base_v010_signal(gp, revenue):
    gm = gp / revenue.replace(0, np.nan)
    sl = _f24_slope(gm, 126)
    sd = _std(gm.diff(), 126)
    b = sl / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin quarter-change percentile-ranked vs its own 1-year history (relative expansion)
def f24mt_f24_margin_trajectory_gmchg_63d_base_v011_signal(grossmargin):
    c = _f24_chg(grossmargin, 63)
    b = _rank(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin change over a year
def f24mt_f24_margin_trajectory_gmchg_252d_base_v012_signal(grossmargin):
    b = _f24_chg(grossmargin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin change vs a half-year ago
def f24mt_f24_margin_trajectory_nmchg_126d_base_v013_signal(netmargin):
    b = _f24_chg(netmargin, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin year-over-year change scaled by its dispersion (standardized swing)
def f24mt_f24_margin_trajectory_nmchgz_252d_base_v014_signal(netmargin):
    chg = _f24_chg(netmargin, 252)
    sd = _std(netmargin, 252)
    b = chg / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin change vs a quarter ago
def f24mt_f24_margin_trajectory_emchg_63d_base_v015_signal(ebitdamargin):
    b = _f24_chg(ebitdamargin, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-margin change vs a half-year ago
def f24mt_f24_margin_trajectory_omchg_126d_base_v016_signal(opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    b = _f24_chg(om, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin log-ratio over a year minus its half-year log-ratio (front-vs-back-loaded expansion)
def f24mt_f24_margin_trajectory_gmpctchg_252d_base_v017_signal(grossmargin):
    g = grossmargin.replace(0, np.nan)
    full = np.log(g / g.shift(252))
    half = np.log(g.shift(126) / g.shift(252))
    b = full - 2.0 * half
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin quarter change minus half-year-prior quarter change (trajectory bend)
def f24mt_f24_margin_trajectory_nmpctchg_63d_base_v018_signal(netmargin):
    c = _f24_pctchg(netmargin, 63)
    b = c - c.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin relative change over a half-year
def f24mt_f24_margin_trajectory_empctchg_126d_base_v019_signal(ebitdamargin):
    b = _f24_pctchg(ebitdamargin, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin change vs its own multi-year baseline level (gross)
def f24mt_f24_margin_trajectory_gmvsbase_252d_base_v020_signal(grossmargin):
    base = _mean(grossmargin, 504)
    b = grossmargin - base
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin deviation from its long baseline, standardized
def f24mt_f24_margin_trajectory_nmvsbase_504d_base_v021_signal(netmargin):
    b = _z(netmargin, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin current vs trailing-year baseline (expansion above norm)
def f24mt_f24_margin_trajectory_emvsbase_252d_base_v022_signal(ebitdamargin):
    base = _mean(ebitdamargin, 252)
    b = ebitdamargin / base.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-margin vs its 252d baseline (level relative to norm)
def f24mt_f24_margin_trajectory_omvsbase_252d_base_v023_signal(opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    base = _mean(om, 252)
    b = om - base
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin stability (inverse CV) over a year
def f24mt_f24_margin_trajectory_gmstab_252d_base_v024_signal(grossmargin):
    b = _f24_stab(grossmargin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin stability over a half-year
def f24mt_f24_margin_trajectory_nmstab_126d_base_v025_signal(netmargin):
    b = _f24_stab(netmargin, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin volatility (raw dispersion) over a year
def f24mt_f24_margin_trajectory_emvol_252d_base_v026_signal(ebitdamargin):
    b = _std(ebitdamargin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-margin stability over a year
def f24mt_f24_margin_trajectory_omstab_252d_base_v027_signal(opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    b = _f24_stab(om, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in gross-margin volatility (stabilizing vs destabilizing)
def f24mt_f24_margin_trajectory_gmvolchg_126d_base_v028_signal(grossmargin):
    v = _std(grossmargin, 126)
    b = v - v.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-minus-net margin spread (operating-cost burden) level
def f24mt_f24_margin_trajectory_gnspread_base_v029_signal(grossmargin, netmargin):
    b = grossmargin - netmargin
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend in the gross-minus-net spread over a half-year (cost leverage trajectory)
def f24mt_f24_margin_trajectory_gnspreadslope_126d_base_v030_signal(grossmargin, netmargin):
    spr = grossmargin - netmargin
    b = _f24_slope(spr, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in gross-minus-net spread over a year (margin compression source)
def f24mt_f24_margin_trajectory_gnspreadchg_252d_base_v031_signal(grossmargin, netmargin):
    spr = grossmargin - netmargin
    b = _f24_chg(spr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-minus-ebitda spread trend (SG&A absorption trajectory)
def f24mt_f24_margin_trajectory_gespreadslope_126d_base_v032_signal(grossmargin, ebitdamargin):
    spr = grossmargin - ebitdamargin
    b = _f24_slope(spr, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-minus-net spread (D&A + interest + tax burden) change over a year
def f24mt_f24_margin_trajectory_enspreadchg_252d_base_v033_signal(ebitdamargin, netmargin):
    spr = ebitdamargin - netmargin
    b = _f24_chg(spr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-vs-gross conversion ratio trend (how much GM converts to OM)
def f24mt_f24_margin_trajectory_omgmconv_126d_base_v034_signal(opinc, revenue, grossmargin):
    om = opinc / revenue.replace(0, np.nan)
    conv = om / grossmargin.replace(0, np.nan)
    b = _f24_slope(conv, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-margin direction sign smoothed over a quarter (persistent direction)
def f24mt_f24_margin_trajectory_omdir_63d_base_v035_signal(opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    d = np.sign(om.diff())
    b = d.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin expansion streak (signed run length of same-direction moves)
def f24mt_f24_margin_trajectory_gmstreak_base_v036_signal(grossmargin):
    b = _f24_streak(grossmargin)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin expansion hit-rate over a half-year (fraction of up-moves)
def f24mt_f24_margin_trajectory_nmhit_126d_base_v037_signal(netmargin):
    b = _f24_hitrate(netmargin, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin expansion hit-rate minus 0.5 over a year (net expansion tilt)
def f24mt_f24_margin_trajectory_emhit_252d_base_v038_signal(ebitdamargin):
    b = _f24_hitrate(ebitdamargin, 252) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin acceleration as level: slope-now minus slope-a-quarter-ago
def f24mt_f24_margin_trajectory_gmaccel_63d_base_v039_signal(grossmargin):
    sl = _f24_slope(grossmargin, 63)
    b = sl - sl.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin acceleration as level over a half-year window
def f24mt_f24_margin_trajectory_nmaccel_126d_base_v040_signal(netmargin):
    sl = _f24_slope(netmargin, 126)
    b = sl - sl.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin trend-to-noise ratio (slope vs dispersion = signal quality)
def f24mt_f24_margin_trajectory_gmtnr_252d_base_v041_signal(grossmargin):
    sl = _f24_slope(grossmargin, 252)
    sd = _std(grossmargin, 252)
    b = sl * 252.0 / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin trend-to-noise ratio over a half-year
def f24mt_f24_margin_trajectory_nmtnr_126d_base_v042_signal(netmargin):
    sl = _f24_slope(netmargin, 126)
    sd = _std(netmargin, 126)
    b = sl * 126.0 / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-expansion breadth: smoothed fraction of the four margins rising day-to-day
def f24mt_f24_margin_trajectory_breadth_63d_base_v043_signal(grossmargin, netmargin, ebitdamargin, opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    up = (grossmargin.diff() > 0).astype(float) \
        + (netmargin.diff() > 0).astype(float) \
        + (ebitdamargin.diff() > 0).astype(float) \
        + (om.diff() > 0).astype(float)
    frac = up / 4.0
    b = frac.rolling(63, min_periods=21).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-trend dispersion across the four margins (agreement of trajectories)
def f24mt_f24_margin_trajectory_trenddisp_126d_base_v044_signal(grossmargin, netmargin, ebitdamargin, opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    g = _f24_slope(grossmargin, 126)
    nn = _f24_slope(netmargin, 126)
    e = _f24_slope(ebitdamargin, 126)
    o = _f24_slope(om, 126)
    b = pd.concat([g, nn, e, o], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin level x its own trend (expanding-while-profitable composite)
def f24mt_f24_margin_trajectory_nmlevtrend_126d_base_v045_signal(netmargin):
    sl = _f24_slope(netmargin, 126)
    lev = _mean(netmargin, 126)
    b = lev * np.sign(sl) * sl.abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin trend ranked cross-time (relative trajectory strength)
def f24mt_f24_margin_trajectory_gmtrendrank_252d_base_v046_signal(grossmargin):
    sl = _f24_slope(grossmargin, 252)
    b = _rank(sl, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin change ranked cross-time over a year
def f24mt_f24_margin_trajectory_nmchgrank_252d_base_v047_signal(netmargin):
    chg = _f24_chg(netmargin, 252)
    b = _rank(chg, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin deviation from baseline ranked (rich/cheap trajectory percentile)
def f24mt_f24_margin_trajectory_emdevrank_252d_base_v048_signal(ebitdamargin):
    dev = ebitdamargin - _mean(ebitdamargin, 252)
    b = _rank(dev, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-margin MACD-histogram: (fast-slow EMA) minus its own signal line (trajectory acceleration)
def f24mt_f24_margin_trajectory_ommacd_base_v049_signal(opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    fast = om.ewm(span=42, min_periods=21).mean()
    slow = om.ewm(span=126, min_periods=63).mean()
    macd = fast - slow
    signal = macd.ewm(span=42, min_periods=21).mean()
    b = macd - signal
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin EMA-displacement (current vs slow EMA = expansion signal)
def f24mt_f24_margin_trajectory_gmdisp_base_v050_signal(grossmargin):
    b = grossmargin - grossmargin.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin convexity: second-difference proxy (curvature of trajectory)
def f24mt_f24_margin_trajectory_nmcurv_126d_base_v051_signal(netmargin):
    m = _mean(netmargin, 21)
    b = m - 2.0 * m.shift(63) + m.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin trajectory asymmetry: up-move avg minus down-move avg (skew)
def f24mt_f24_margin_trajectory_emasym_252d_base_v052_signal(ebitdamargin):
    d = ebitdamargin.diff()
    up = d.where(d > 0)
    dn = d.where(d < 0)
    b = up.rolling(252, min_periods=63).mean() + dn.rolling(252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross vs net trajectory divergence: correlation-of-direction proxy via product of trend signs x magnitude gap
def f24mt_f24_margin_trajectory_gnslopespr_126d_base_v053_signal(grossmargin, netmargin):
    g = _f24_slope(grossmargin, 63)
    nn = _f24_slope(netmargin, 63)
    align = np.sign(g) * np.sign(nn)
    b = align.rolling(126, min_periods=42).mean() * (g.abs() + nn.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin expansion concurrent with revenue growth: sign-agreement of GM-trend and revenue-trend
def f24mt_f24_margin_trajectory_gmrevw_252d_base_v054_signal(grossmargin, revenue):
    gm_sl = _f24_slope(grossmargin, 126)
    rev_g = np.log(revenue.replace(0, np.nan)).diff(63)
    same = (np.sign(gm_sl) == np.sign(rev_g)).astype(float)
    b = same.rolling(126, min_periods=42).mean() * gm_sl.abs() - 0.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp-derived gross margin minus reported grossmargin spread trend (quality check)
def f24mt_f24_margin_trajectory_gmconsist_126d_base_v055_signal(gp, revenue, grossmargin):
    gm2 = gp / revenue.replace(0, np.nan)
    spr = gm2 - grossmargin
    b = _f24_slope(spr, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin range-position within its own 504d range (where in cycle)
def f24mt_f24_margin_trajectory_nmrngpos_504d_base_v056_signal(netmargin):
    hi = netmargin.rolling(504, min_periods=126).max()
    lo = netmargin.rolling(504, min_periods=126).min()
    b = (netmargin - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin proximity to its trailing peak (off-peak margin compression)
def f24mt_f24_margin_trajectory_gmpeakprox_252d_base_v057_signal(grossmargin):
    pk = grossmargin.rolling(252, min_periods=63).max()
    b = grossmargin / pk.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin recovery off trailing trough (margin rebound)
def f24mt_f24_margin_trajectory_emtroughrec_252d_base_v058_signal(ebitdamargin):
    tr = ebitdamargin.rolling(252, min_periods=63).min()
    b = ebitdamargin / tr.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-margin streak (signed run of same-direction OM moves)
def f24mt_f24_margin_trajectory_omstreak_base_v059_signal(opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    b = _f24_streak(om)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year net margin spent above its baseline (durable expansion)
def f24mt_f24_margin_trajectory_nmabovebase_252d_base_v060_signal(netmargin):
    base = _mean(netmargin, 504)
    above = (netmargin > base).astype(float)
    b = above.rolling(252, min_periods=63).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin short-trend minus long-trend (trajectory acceleration spread)
def f24mt_f24_margin_trajectory_gmtrendspr_base_v061_signal(grossmargin):
    s = _f24_slope(grossmargin, 63)
    l = _f24_slope(grossmargin, 252)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin short vs long trend ratio (trajectory regime)
def f24mt_f24_margin_trajectory_nmtrendratio_base_v062_signal(netmargin):
    s = _f24_slope(netmargin, 63)
    l = _f24_slope(netmargin, 252)
    b = np.sign(l) * s / l.abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin half-year change minus prior half-year change (sequential delta)
def f24mt_f24_margin_trajectory_emseqdelta_126d_base_v063_signal(ebitdamargin):
    c1 = _f24_chg(ebitdamargin, 126)
    b = c1 - c1.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating margin trend interacted with margin stability (high-conviction trend)
def f24mt_f24_margin_trajectory_omtrendstab_126d_base_v064_signal(opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    sl = _f24_slope(om, 126)
    stab = _f24_stab(om, 126)
    b = sl * np.log1p(stab.clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin downside dispersion of trajectory (semi-deviation of decreases)
def f24mt_f24_margin_trajectory_gmdownvol_252d_base_v065_signal(grossmargin):
    d = grossmargin.diff()
    neg = d.where(d < 0)
    b = neg.rolling(252, min_periods=63).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin trajectory consistency: |mean change| / vol of changes
def f24mt_f24_margin_trajectory_nmconsist_252d_base_v066_signal(netmargin):
    d = netmargin.diff()
    mc = d.rolling(252, min_periods=63).mean()
    vc = d.rolling(252, min_periods=63).std()
    b = mc.abs() / vc.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-vs-ebitda margin spread level (overhead intensity) z-scored
def f24mt_f24_margin_trajectory_gespreadz_252d_base_v067_signal(grossmargin, ebitdamargin):
    spr = grossmargin - ebitdamargin
    b = _z(spr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-vs-net spread trend ranked (below-the-line burden trajectory)
def f24mt_f24_margin_trajectory_enslopernk_252d_base_v068_signal(ebitdamargin, netmargin):
    spr = ebitdamargin - netmargin
    sl = _f24_slope(spr, 252)
    b = _rank(sl, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-quartet average trend (composite trajectory) over a half-year
def f24mt_f24_margin_trajectory_avgtrend_126d_base_v069_signal(grossmargin, netmargin, ebitdamargin, opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    g = _f24_slope(grossmargin, 126)
    nn = _f24_slope(netmargin, 126)
    e = _f24_slope(ebitdamargin, 126)
    o = _f24_slope(om, 126)
    b = pd.concat([g, nn, e, o], axis=1).mean(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin inflection: slope-sign reversal smoothed over a quarter (turn frequency x magnitude)
def f24mt_f24_margin_trajectory_nminflect_base_v070_signal(netmargin):
    sl = _f24_slope(netmargin, 63)
    flip = (np.sign(sl) - np.sign(sl.shift(21))).abs()
    freq = flip.rolling(63, min_periods=21).mean()
    b = freq * sl.abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin trend per unit of revenue growth (margin efficiency of growth)
def f24mt_f24_margin_trajectory_gmpergrowth_252d_base_v071_signal(grossmargin, revenue):
    gm_sl = _f24_slope(grossmargin, 252)
    rev_g = revenue / revenue.shift(252).replace(0, np.nan) - 1.0
    b = gm_sl / rev_g.abs().replace(0, np.nan) * np.sign(rev_g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin YoY change relative to its prior-year YoY change (acceleration of YoY trajectory)
def f24mt_f24_margin_trajectory_emyoy_252d_base_v072_signal(ebitdamargin):
    yoy = ebitdamargin - ebitdamargin.shift(252)
    b = yoy - yoy.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-margin minus net-margin spread trend (tax/interest drift)
def f24mt_f24_margin_trajectory_omnmspr_126d_base_v073_signal(opinc, revenue, netmargin):
    om = opinc / revenue.replace(0, np.nan)
    spr = om - netmargin
    b = _f24_slope(spr, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin trajectory tanh-bounded change (saturated expansion signal)
def f24mt_f24_margin_trajectory_gmtanh_126d_base_v074_signal(grossmargin):
    chg = _f24_chg(grossmargin, 126)
    b = np.tanh(25.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin expansion streak weighted by latest change magnitude
def f24mt_f24_margin_trajectory_nmstreakmag_base_v075_signal(netmargin):
    st = _f24_streak(netmargin)
    mag = netmargin.diff().abs()
    b = st * mag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f24mt_f24_margin_trajectory_gmslope_63d_base_v001_signal,
    f24mt_f24_margin_trajectory_gmslopen_126d_base_v002_signal,
    f24mt_f24_margin_trajectory_gmslopez_252d_base_v003_signal,
    f24mt_f24_margin_trajectory_nmslope_63d_base_v004_signal,
    f24mt_f24_margin_trajectory_nmslopen_126d_base_v005_signal,
    f24mt_f24_margin_trajectory_emslope_126d_base_v006_signal,
    f24mt_f24_margin_trajectory_emsloperank_252d_base_v007_signal,
    f24mt_f24_margin_trajectory_omslope_63d_base_v008_signal,
    f24mt_f24_margin_trajectory_omslopen_252d_base_v009_signal,
    f24mt_f24_margin_trajectory_gpmslope_126d_base_v010_signal,
    f24mt_f24_margin_trajectory_gmchg_63d_base_v011_signal,
    f24mt_f24_margin_trajectory_gmchg_252d_base_v012_signal,
    f24mt_f24_margin_trajectory_nmchg_126d_base_v013_signal,
    f24mt_f24_margin_trajectory_nmchgz_252d_base_v014_signal,
    f24mt_f24_margin_trajectory_emchg_63d_base_v015_signal,
    f24mt_f24_margin_trajectory_omchg_126d_base_v016_signal,
    f24mt_f24_margin_trajectory_gmpctchg_252d_base_v017_signal,
    f24mt_f24_margin_trajectory_nmpctchg_63d_base_v018_signal,
    f24mt_f24_margin_trajectory_empctchg_126d_base_v019_signal,
    f24mt_f24_margin_trajectory_gmvsbase_252d_base_v020_signal,
    f24mt_f24_margin_trajectory_nmvsbase_504d_base_v021_signal,
    f24mt_f24_margin_trajectory_emvsbase_252d_base_v022_signal,
    f24mt_f24_margin_trajectory_omvsbase_252d_base_v023_signal,
    f24mt_f24_margin_trajectory_gmstab_252d_base_v024_signal,
    f24mt_f24_margin_trajectory_nmstab_126d_base_v025_signal,
    f24mt_f24_margin_trajectory_emvol_252d_base_v026_signal,
    f24mt_f24_margin_trajectory_omstab_252d_base_v027_signal,
    f24mt_f24_margin_trajectory_gmvolchg_126d_base_v028_signal,
    f24mt_f24_margin_trajectory_gnspread_base_v029_signal,
    f24mt_f24_margin_trajectory_gnspreadslope_126d_base_v030_signal,
    f24mt_f24_margin_trajectory_gnspreadchg_252d_base_v031_signal,
    f24mt_f24_margin_trajectory_gespreadslope_126d_base_v032_signal,
    f24mt_f24_margin_trajectory_enspreadchg_252d_base_v033_signal,
    f24mt_f24_margin_trajectory_omgmconv_126d_base_v034_signal,
    f24mt_f24_margin_trajectory_omdir_63d_base_v035_signal,
    f24mt_f24_margin_trajectory_gmstreak_base_v036_signal,
    f24mt_f24_margin_trajectory_nmhit_126d_base_v037_signal,
    f24mt_f24_margin_trajectory_emhit_252d_base_v038_signal,
    f24mt_f24_margin_trajectory_gmaccel_63d_base_v039_signal,
    f24mt_f24_margin_trajectory_nmaccel_126d_base_v040_signal,
    f24mt_f24_margin_trajectory_gmtnr_252d_base_v041_signal,
    f24mt_f24_margin_trajectory_nmtnr_126d_base_v042_signal,
    f24mt_f24_margin_trajectory_breadth_63d_base_v043_signal,
    f24mt_f24_margin_trajectory_trenddisp_126d_base_v044_signal,
    f24mt_f24_margin_trajectory_nmlevtrend_126d_base_v045_signal,
    f24mt_f24_margin_trajectory_gmtrendrank_252d_base_v046_signal,
    f24mt_f24_margin_trajectory_nmchgrank_252d_base_v047_signal,
    f24mt_f24_margin_trajectory_emdevrank_252d_base_v048_signal,
    f24mt_f24_margin_trajectory_ommacd_base_v049_signal,
    f24mt_f24_margin_trajectory_gmdisp_base_v050_signal,
    f24mt_f24_margin_trajectory_nmcurv_126d_base_v051_signal,
    f24mt_f24_margin_trajectory_emasym_252d_base_v052_signal,
    f24mt_f24_margin_trajectory_gnslopespr_126d_base_v053_signal,
    f24mt_f24_margin_trajectory_gmrevw_252d_base_v054_signal,
    f24mt_f24_margin_trajectory_gmconsist_126d_base_v055_signal,
    f24mt_f24_margin_trajectory_nmrngpos_504d_base_v056_signal,
    f24mt_f24_margin_trajectory_gmpeakprox_252d_base_v057_signal,
    f24mt_f24_margin_trajectory_emtroughrec_252d_base_v058_signal,
    f24mt_f24_margin_trajectory_omstreak_base_v059_signal,
    f24mt_f24_margin_trajectory_nmabovebase_252d_base_v060_signal,
    f24mt_f24_margin_trajectory_gmtrendspr_base_v061_signal,
    f24mt_f24_margin_trajectory_nmtrendratio_base_v062_signal,
    f24mt_f24_margin_trajectory_emseqdelta_126d_base_v063_signal,
    f24mt_f24_margin_trajectory_omtrendstab_126d_base_v064_signal,
    f24mt_f24_margin_trajectory_gmdownvol_252d_base_v065_signal,
    f24mt_f24_margin_trajectory_nmconsist_252d_base_v066_signal,
    f24mt_f24_margin_trajectory_gespreadz_252d_base_v067_signal,
    f24mt_f24_margin_trajectory_enslopernk_252d_base_v068_signal,
    f24mt_f24_margin_trajectory_avgtrend_126d_base_v069_signal,
    f24mt_f24_margin_trajectory_nminflect_base_v070_signal,
    f24mt_f24_margin_trajectory_gmpergrowth_252d_base_v071_signal,
    f24mt_f24_margin_trajectory_emyoy_252d_base_v072_signal,
    f24mt_f24_margin_trajectory_omnmspr_126d_base_v073_signal,
    f24mt_f24_margin_trajectory_gmtanh_126d_base_v074_signal,
    f24mt_f24_margin_trajectory_nmstreakmag_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F24_MARGIN_TRAJECTORY_REGISTRY_001_075 = REGISTRY


def _fund(seed, n, base=1e8, drift=0.02, vol=0.05, allow_neg=False):
    g = np.random.default_rng(seed)
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.3
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    revenue = _fund(101, n, base=1e9, drift=0.03, vol=0.04).rename("revenue")
    grossmargin = _fund(102, n, base=0.35, drift=0.005, vol=0.03).clip(0.02, 0.9).rename("grossmargin")
    netmargin = _fund(103, n, base=0.12, drift=0.004, vol=0.04).clip(-0.2, 0.6).rename("netmargin")
    ebitdamargin = _fund(104, n, base=0.20, drift=0.004, vol=0.035).clip(-0.1, 0.7).rename("ebitdamargin")
    opinc = _fund(105, n, base=1.5e8, drift=0.02, vol=0.05, allow_neg=True).rename("opinc")
    gp = (revenue * _fund(106, n, base=0.33, drift=0.005, vol=0.03).clip(0.02, 0.9)).rename("gp")

    cols = {
        "grossmargin": grossmargin, "netmargin": netmargin,
        "ebitdamargin": ebitdamargin, "opinc": opinc,
        "revenue": revenue, "gp": gp,
    }

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, "%s nunique=%d" % (name, q.nunique())
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        results[name] = y1.iloc[504:]
        n_features += 1

    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), "nan_ok=%d/%d" % (nan_ok, n_features)

    items = list(results.items())
    for i in range(len(items)):
        ni, si = items[i]
        ai = si.dropna()
        for j in range(i + 1, len(items)):
            nj, sj = items[j]
            aj = sj.dropna()
            idx = ai.index.intersection(aj.index)
            if len(idx) < 30:
                continue
            c = ai.loc[idx].corr(aj.loc[idx])
            if c is None or np.isnan(c):
                continue
            assert abs(c) <= 0.97, "CORR %s vs %s = %.4f" % (ni, nj, c)

    print("OK f24_margin_trajectory_base_001_075_claude: %d features pass" % n_features)
