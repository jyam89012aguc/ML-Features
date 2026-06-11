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
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _slope(s, w):
    # ordinary-least-squares slope of s over a trailing window of length w
    idx = np.arange(w, dtype=float)
    idx = idx - idx.mean()
    denom = float((idx * idx).sum())

    def _f(a):
        if np.isnan(a).any():
            return np.nan
        return float((idx * (a - a.mean())).sum() / denom)

    return s.rolling(w, min_periods=w).apply(_f, raw=True)


# ===== folder domain primitives (FCF trajectory) =====
def _f25_growth(s, w):
    # log-like growth of a (possibly negative) fundamental level over w days, sign-safe
    base = s.shift(w)
    return np.sign(base) * (s - base) / base.abs().replace(0, np.nan)


def _f25_fcf_margin(fcf, revenue):
    return fcf / revenue.replace(0, np.nan)


def _f25_margin_trend(fcf, revenue, w):
    return _slope(_f25_fcf_margin(fcf, revenue), w)


def _f25_pos_streak(s):
    # running positive-streak length (in days)
    pos = (s > 0).astype(float)
    grp = (pos == 0).cumsum()
    streak = pos.groupby(grp).cumsum()
    return streak


def _f25_consistency(s, w):
    # fraction of days in window with a positive level
    return (s > 0).astype(float).rolling(w, min_periods=max(1, w // 2)).mean()


def _f25_inflection(s, w):
    # short trend minus long trend: change of direction
    short = _slope(s, max(5, w // 3))
    long = _slope(s, w)
    return short - long


# ============================================================
# FCF year-over-year growth (252d)
def f25ft_f25_fcf_trajectory_fcfgr_252d_base_v001_signal(fcf):
    b = _f25_growth(fcf, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF half-year growth (126d)
def f25ft_f25_fcf_trajectory_fcfgr_126d_base_v002_signal(fcf):
    b = _f25_growth(fcf, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF two-year growth, z-scored vs its own 252d history (de-trended growth level)
def f25ft_f25_fcf_trajectory_fcfgr_504d_base_v003_signal(fcf):
    g = _f25_growth(fcf, 504)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo (operating cash flow) year-over-year growth
def f25ft_f25_fcf_trajectory_ncfogr_252d_base_v004_signal(ncfo):
    b = _f25_growth(ncfo, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo quarterly growth, percentile-ranked vs its own 252d history
def f25ft_f25_fcf_trajectory_ncfogr_63d_base_v005_signal(ncfo):
    g = _f25_growth(ncfo, 63)
    b = _rank(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-per-share growth (252d)
def f25ft_f25_fcf_trajectory_fcfpsgr_252d_base_v006_signal(fcfps):
    b = _f25_growth(fcfps, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-per-share growth (126d), smoothed
def f25ft_f25_fcf_trajectory_fcfpsgr_126d_base_v007_signal(fcfps):
    g = _f25_growth(fcfps, 126)
    b = g.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin level (fcf/revenue) — anchor of the trajectory
def f25ft_f25_fcf_trajectory_fcfmargin_base_v008_signal(fcf, revenue):
    b = _f25_fcf_margin(fcf, revenue)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin trend: slope of fcf/revenue over a year
def f25ft_f25_fcf_trajectory_fcfmargtrend_252d_base_v009_signal(fcf, revenue):
    b = _f25_margin_trend(fcf, revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin trend over a half year
def f25ft_f25_fcf_trajectory_fcfmargtrend_126d_base_v010_signal(fcf, revenue):
    b = _f25_margin_trend(fcf, revenue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin change vs its level one year ago
def f25ft_f25_fcf_trajectory_fcfmargchg_252d_base_v011_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    b = m - m.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin change vs its level one quarter ago
def f25ft_f25_fcf_trajectory_fcfmargchg_63d_base_v012_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    b = m - m.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF positivity consistency: fraction of last year with positive FCF
def f25ft_f25_fcf_trajectory_fcfconsist_252d_base_v013_signal(fcf):
    b = _f25_consistency(fcf, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF positivity consistency over a half year
def f25ft_f25_fcf_trajectory_fcfconsist_126d_base_v014_signal(fcf):
    b = _f25_consistency(fcf, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF positive-streak length (days), normalized by a year
def f25ft_f25_fcf_trajectory_fcfstreak_base_v015_signal(fcf):
    b = _f25_pos_streak(fcf) / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo positive-streak length, normalized
def f25ft_f25_fcf_trajectory_ncfostreak_base_v016_signal(ncfo):
    b = _f25_pos_streak(ncfo) / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF inflection (252d): short trend minus long trend of the FCF level
def f25ft_f25_fcf_trajectory_fcfinflect_252d_base_v017_signal(fcf):
    b = _f25_inflection(fcf, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo inflection (126d)
def f25ft_f25_fcf_trajectory_ncfoinflect_126d_base_v018_signal(ncfo):
    b = _f25_inflection(ncfo, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF/revenue change z-scored vs its own 252d history (re-rating of margin)
def f25ft_f25_fcf_trajectory_fcfrevchgz_252d_base_v019_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    chg = m - m.shift(126)
    b = _z(chg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo trend: slope of ncfo over a year, normalized by its own mean (scale-free)
def f25ft_f25_fcf_trajectory_ncfotrend_252d_base_v020_signal(ncfo):
    sl = _slope(ncfo, 252)
    b = sl / _mean(ncfo, 252).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF trend normalized by its own level (scale-free FCF slope)
def f25ft_f25_fcf_trajectory_fcftrendnorm_252d_base_v021_signal(fcf):
    sl = _slope(fcf, 252)
    b = sl / _mean(fcf, 252).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF growth stability: negative dispersion of trailing FCF growth (higher=steadier)
def f25ft_f25_fcf_trajectory_fcfgrstab_252d_base_v022_signal(fcf):
    g = _f25_growth(fcf, 63)
    b = -_std(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo growth stability over two years
def f25ft_f25_fcf_trajectory_ncfogrstab_504d_base_v023_signal(ncfo):
    g = _f25_growth(ncfo, 63)
    b = -_std(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF conversion trend: trend of (fcf/ncfo) — cash conversion quality over time
def f25ft_f25_fcf_trajectory_convtrend_252d_base_v024_signal(fcf, ncfo):
    conv = fcf / ncfo.replace(0, np.nan)
    b = _slope(conv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF conversion change vs a year ago
def f25ft_f25_fcf_trajectory_convchg_252d_base_v025_signal(fcf, ncfo):
    conv = fcf / ncfo.replace(0, np.nan)
    b = conv - conv.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin acceleration: change in the FCF-margin slope over a quarter
def f25ft_f25_fcf_trajectory_fcfmargaccel_252d_base_v026_signal(fcf, revenue):
    tr = _f25_margin_trend(fcf, revenue, 126)
    b = tr - tr.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF growth rank vs its own two-year history
def f25ft_f25_fcf_trajectory_fcfgrrank_504d_base_v027_signal(fcf):
    g = _f25_growth(fcf, 252)
    b = _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo growth rank vs its own two-year history
def f25ft_f25_fcf_trajectory_ncfogrrank_504d_base_v028_signal(ncfo):
    g = _f25_growth(ncfo, 252)
    b = _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-per-share trend normalized by its own typical magnitude
def f25ft_f25_fcf_trajectory_fcfpstrend_252d_base_v029_signal(fcfps):
    sl = _slope(fcfps, 252)
    b = sl / _mean(fcfps, 252).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF acceleration: YoY growth now minus YoY growth a quarter ago
def f25ft_f25_fcf_trajectory_fcfaccel_252d_base_v030_signal(fcf):
    g = _f25_growth(fcf, 252)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo acceleration: YoY growth now minus YoY growth a quarter ago
def f25ft_f25_fcf_trajectory_ncfoaccel_252d_base_v031_signal(ncfo):
    g = _f25_growth(ncfo, 252)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin upper-band time: fraction of last year with margin above its own median
def f25ft_f25_fcf_trajectory_fcfmargabovemed_252d_base_v032_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    med = m.rolling(252, min_periods=126).median()
    b = (m > med).astype(float).rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF directional persistence: fraction of last year FCF rose day-over-day
def f25ft_f25_fcf_trajectory_fcfuprate_252d_base_v033_signal(fcf):
    up = (fcf.diff() > 0).astype(float)
    b = up.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo directional persistence over a half year
def f25ft_f25_fcf_trajectory_ncfouprate_126d_base_v034_signal(ncfo):
    up = (ncfo.diff() > 0).astype(float)
    b = up.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin slope per unit of margin volatility (risk-adjusted trend)
def f25ft_f25_fcf_trajectory_fcfmargtrendvol_252d_base_v035_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    sl = _slope(m, 252)
    vol = _std(m, 252)
    b = sl / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF growth relative to revenue growth as a ratio (cash-flow operating leverage)
def f25ft_f25_fcf_trajectory_fcfvsrevgr_252d_base_v036_signal(fcf, revenue):
    gf = _f25_growth(fcf, 252)
    gr = _f25_growth(revenue, 252)
    b = np.tanh(3.0 * gf) - 2.0 * np.tanh(3.0 * gr)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo growth relative to revenue growth, ranked (relative cash-conversion leverage)
def f25ft_f25_fcf_trajectory_ncfovsrevgr_252d_base_v037_signal(ncfo, revenue):
    gn = _f25_growth(ncfo, 252)
    gr = _f25_growth(revenue, 252)
    spread = gn - 1.5 * gr
    b = _rank(spread, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin inflection: short margin trend minus long margin trend
def f25ft_f25_fcf_trajectory_fcfmarginflect_252d_base_v038_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    b = _f25_inflection(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF half-year growth minus its own year-ago half-year growth (growth momentum)
def f25ft_f25_fcf_trajectory_fcfgrmom_126d_base_v039_signal(fcf):
    g = _f25_growth(fcf, 126)
    b = g - g.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF level z-score vs its own two-year trajectory (where in its own range)
def f25ft_f25_fcf_trajectory_fcflevelz_504d_base_v040_signal(fcf):
    b = _z(fcf, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo level percentile rank vs its own two-year trajectory
def f25ft_f25_fcf_trajectory_ncfolevelrank_504d_base_v041_signal(ncfo):
    b = _rank(ncfo, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin range position within its own trailing two-year band
def f25ft_f25_fcf_trajectory_fcfmargrngpos_504d_base_v042_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    hi = m.rolling(504, min_periods=252).max()
    lo = m.rolling(504, min_periods=252).min()
    b = (m - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF trough recovery momentum: change over a quarter in FCF-vs-trailing-trough gap
def f25ft_f25_fcf_trajectory_fcftroughrecov_504d_base_v043_signal(fcf):
    lo = fcf.rolling(504, min_periods=252).min()
    gap = (fcf - lo) / lo.abs().replace(0, np.nan)
    b = gap - gap.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF drawdown: FCF relative to its own trailing two-year peak
def f25ft_f25_fcf_trajectory_fcfdrawdown_504d_base_v044_signal(fcf):
    hi = fcf.rolling(504, min_periods=252).max()
    b = (fcf - hi) / hi.abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin trend conviction: signed margin trend de-meaned by its own slow average
def f25ft_f25_fcf_trajectory_fcfmargconv_252d_base_v045_signal(fcf, revenue):
    tr = _f25_margin_trend(fcf, revenue, 252)
    sq = np.sign(tr) * (tr.abs() ** 0.5)
    b = sq - sq.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF consistency weighted by average margin (consistent AND high)
def f25ft_f25_fcf_trajectory_fcfconsistwt_252d_base_v046_signal(fcf, revenue):
    cons = _f25_consistency(fcf, 252)
    m = _mean(_f25_fcf_margin(fcf, revenue), 252)
    b = cons * m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo trend minus FCF trend (capex-drag trajectory proxy)
def f25ft_f25_fcf_trajectory_capexdrag_252d_base_v047_signal(ncfo, fcf):
    sn = _slope(ncfo, 252) / _mean(ncfo, 252).abs().replace(0, np.nan)
    sf = _slope(fcf, 252) / _mean(fcf, 252).abs().replace(0, np.nan)
    b = sn - sf
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin year-over-year acceleration (margin change now vs a year ago)
def f25ft_f25_fcf_trajectory_fcfmargyoyacc_252d_base_v048_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    chg = m - m.shift(126)
    b = chg - chg.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-per-share consistency (positive-fraction over a year)
def f25ft_f25_fcf_trajectory_fcfpsconsist_252d_base_v049_signal(fcfps):
    b = _f25_consistency(fcfps, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin volatility trend (is margin getting more stable over time?)
def f25ft_f25_fcf_trajectory_fcfmargvoltrend_base_v050_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    vol = _std(m, 63)
    b = -_slope(vol, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF growth breadth: net fraction of up vs down quarters in the FCF series
def f25ft_f25_fcf_trajectory_fcfbreadth_504d_base_v051_signal(fcf):
    chg = fcf - fcf.shift(63)
    up = (chg > 0).astype(float)
    dn = (chg < 0).astype(float)
    b = (up - dn).rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin smoothed deviation from its slow trend (margin displacement)
def f25ft_f25_fcf_trajectory_fcfmargdisp_252d_base_v052_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    b = m - m.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo cumulative drift: growth of ncfo over two years, smoothed
def f25ft_f25_fcf_trajectory_ncfodrift_504d_base_v053_signal(ncfo):
    g = _f25_growth(ncfo, 504)
    b = g.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF/revenue spread vs ncfo/revenue, change over a year (capex-intensity drift)
def f25ft_f25_fcf_trajectory_fcfncfomarg_base_v054_signal(fcf, ncfo, revenue):
    fm = fcf / revenue.replace(0, np.nan)
    nm = ncfo / revenue.replace(0, np.nan)
    spread = fm - nm
    b = spread - spread.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF turnaround flag strength: recent positivity vs prior-year positivity
def f25ft_f25_fcf_trajectory_fcfturn_252d_base_v055_signal(fcf):
    recent = _f25_consistency(fcf, 63)
    prior = _f25_consistency(fcf, 252).shift(63)
    b = recent - prior
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF growth tanh-squashed (bounded YoY growth signal)
def f25ft_f25_fcf_trajectory_fcfgrtanh_252d_base_v056_signal(fcf):
    g = _f25_growth(fcf, 252)
    b = np.tanh(2.0 * g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin trend rank vs its own history (relative strength of improvement)
def f25ft_f25_fcf_trajectory_fcfmargtrendrank_base_v057_signal(fcf, revenue):
    tr = _f25_margin_trend(fcf, revenue, 126)
    b = _rank(tr, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF half-year vs two-year growth spread (short vs long trajectory)
def f25ft_f25_fcf_trajectory_fcfgrspread_base_v058_signal(fcf):
    gs = _f25_growth(fcf, 126)
    gl = _f25_growth(fcf, 504)
    b = gs - gl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo half-year vs two-year growth spread
def f25ft_f25_fcf_trajectory_ncfogrspread_base_v059_signal(ncfo):
    gs = _f25_growth(ncfo, 126)
    gl = _f25_growth(ncfo, 504)
    b = gs - gl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin level interacted with its trend direction (improving high-margin biz)
def f25ft_f25_fcf_trajectory_fcfmarglvltrend_base_v060_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    lvl = _mean(m, 63)
    tr = _slope(m, 252)
    b = lvl * np.sign(tr)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF positive-streak interacted with growth (durable AND growing)
def f25ft_f25_fcf_trajectory_fcfstreakgr_base_v061_signal(fcf):
    streak = _f25_pos_streak(fcf) / 252.0
    g = _f25_growth(fcf, 126)
    b = streak * np.tanh(g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin long-run trajectory: 504d margin slope minus its own one-quarter-ago value
def f25ft_f25_fcf_trajectory_fcfmargtrendd_504d_base_v062_signal(fcf, revenue):
    tr = _f25_margin_trend(fcf, revenue, 504)
    b = tr - tr.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF two-year growth minus one-year growth (long-horizon compounding acceleration)
def f25ft_f25_fcf_trajectory_fcfgracc_504d_base_v063_signal(fcf):
    g2 = _f25_growth(fcf, 504)
    g1 = _f25_growth(fcf, 252)
    b = g2 - 2.0 * g1
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo two-year growth, percentile-ranked vs its own 252d history
def f25ft_f25_fcf_trajectory_ncfogrrk_504d_base_v064_signal(ncfo):
    g = _f25_growth(ncfo, 504)
    b = _rank(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF conversion (fcf/ncfo) consistency above 0.5 over a year
def f25ft_f25_fcf_trajectory_convconsist_252d_base_v065_signal(fcf, ncfo):
    conv = fcf / ncfo.replace(0, np.nan)
    b = (conv > 0.5).astype(float).rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin curvature: second difference of the margin level (accel as level)
def f25ft_f25_fcf_trajectory_fcfmargcurv_252d_base_v066_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    b = (m - m.shift(126)) - (m.shift(126) - m.shift(252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF growth dispersion across windows (trajectory disagreement)
def f25ft_f25_fcf_trajectory_fcfgrdisp_base_v067_signal(fcf):
    g1 = _f25_growth(fcf, 63)
    g2 = _f25_growth(fcf, 126)
    g3 = _f25_growth(fcf, 252)
    b = pd.concat([g1, g2, g3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-per-share level rank vs its own two-year history
def f25ft_f25_fcf_trajectory_fcfpsrank_504d_base_v068_signal(fcfps):
    b = _rank(fcfps, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin improvement streak: consecutive days margin above year-ago margin
def f25ft_f25_fcf_trajectory_fcfmargimprstreak_base_v069_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    impr = (m > m.shift(252)).astype(float)
    grp = (impr == 0).cumsum()
    streak = impr.groupby(grp).cumsum()
    b = streak / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo trend per unit of revenue scale (cash-trend intensity)
def f25ft_f25_fcf_trajectory_ncfotrendrev_252d_base_v070_signal(ncfo, revenue):
    sl = _slope(ncfo, 252)
    b = sl / _mean(revenue, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin trend interacted with consistency (clean improving cash margin)
def f25ft_f25_fcf_trajectory_fcfmargcleantr_base_v071_signal(fcf, revenue):
    tr = _f25_margin_trend(fcf, revenue, 252)
    cons = _f25_consistency(fcf, 252)
    b = np.tanh(50.0 * tr) * cons
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF/revenue change ranked vs its own history (relative margin re-rating)
def f25ft_f25_fcf_trajectory_fcfrevchgrank_base_v072_signal(fcf, revenue):
    m = _f25_fcf_margin(fcf, revenue)
    chg = m - m.shift(252)
    b = _rank(chg, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF inflection over two years, smoothed (long-run direction change of FCF)
def f25ft_f25_fcf_trajectory_fcfinflect_504d_base_v073_signal(fcf):
    b = _f25_inflection(fcf, 504).ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF quarterly sequential growth, exponentially weighted (recent-cash momentum)
def f25ft_f25_fcf_trajectory_fcfseqgr_63d_base_v074_signal(fcf):
    g = _f25_growth(fcf, 63)
    b = g.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Composite cash-trajectory: blended scale-free trend of FCF, ncfo and margin
def f25ft_f25_fcf_trajectory_cashtrajcomp_base_v075_signal(fcf, ncfo, revenue):
    tf = _slope(fcf, 252) / _mean(fcf, 252).abs().replace(0, np.nan)
    tn = _slope(ncfo, 252) / _mean(ncfo, 252).abs().replace(0, np.nan)
    tm = _f25_margin_trend(fcf, revenue, 252)
    b = np.tanh(tf) + np.tanh(tn) + np.tanh(200.0 * tm)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f25ft_f25_fcf_trajectory_fcfgr_252d_base_v001_signal,
    f25ft_f25_fcf_trajectory_fcfgr_126d_base_v002_signal,
    f25ft_f25_fcf_trajectory_fcfgr_504d_base_v003_signal,
    f25ft_f25_fcf_trajectory_ncfogr_252d_base_v004_signal,
    f25ft_f25_fcf_trajectory_ncfogr_63d_base_v005_signal,
    f25ft_f25_fcf_trajectory_fcfpsgr_252d_base_v006_signal,
    f25ft_f25_fcf_trajectory_fcfpsgr_126d_base_v007_signal,
    f25ft_f25_fcf_trajectory_fcfmargin_base_v008_signal,
    f25ft_f25_fcf_trajectory_fcfmargtrend_252d_base_v009_signal,
    f25ft_f25_fcf_trajectory_fcfmargtrend_126d_base_v010_signal,
    f25ft_f25_fcf_trajectory_fcfmargchg_252d_base_v011_signal,
    f25ft_f25_fcf_trajectory_fcfmargchg_63d_base_v012_signal,
    f25ft_f25_fcf_trajectory_fcfconsist_252d_base_v013_signal,
    f25ft_f25_fcf_trajectory_fcfconsist_126d_base_v014_signal,
    f25ft_f25_fcf_trajectory_fcfstreak_base_v015_signal,
    f25ft_f25_fcf_trajectory_ncfostreak_base_v016_signal,
    f25ft_f25_fcf_trajectory_fcfinflect_252d_base_v017_signal,
    f25ft_f25_fcf_trajectory_ncfoinflect_126d_base_v018_signal,
    f25ft_f25_fcf_trajectory_fcfrevchgz_252d_base_v019_signal,
    f25ft_f25_fcf_trajectory_ncfotrend_252d_base_v020_signal,
    f25ft_f25_fcf_trajectory_fcftrendnorm_252d_base_v021_signal,
    f25ft_f25_fcf_trajectory_fcfgrstab_252d_base_v022_signal,
    f25ft_f25_fcf_trajectory_ncfogrstab_504d_base_v023_signal,
    f25ft_f25_fcf_trajectory_convtrend_252d_base_v024_signal,
    f25ft_f25_fcf_trajectory_convchg_252d_base_v025_signal,
    f25ft_f25_fcf_trajectory_fcfmargaccel_252d_base_v026_signal,
    f25ft_f25_fcf_trajectory_fcfgrrank_504d_base_v027_signal,
    f25ft_f25_fcf_trajectory_ncfogrrank_504d_base_v028_signal,
    f25ft_f25_fcf_trajectory_fcfpstrend_252d_base_v029_signal,
    f25ft_f25_fcf_trajectory_fcfaccel_252d_base_v030_signal,
    f25ft_f25_fcf_trajectory_ncfoaccel_252d_base_v031_signal,
    f25ft_f25_fcf_trajectory_fcfmargabovemed_252d_base_v032_signal,
    f25ft_f25_fcf_trajectory_fcfuprate_252d_base_v033_signal,
    f25ft_f25_fcf_trajectory_ncfouprate_126d_base_v034_signal,
    f25ft_f25_fcf_trajectory_fcfmargtrendvol_252d_base_v035_signal,
    f25ft_f25_fcf_trajectory_fcfvsrevgr_252d_base_v036_signal,
    f25ft_f25_fcf_trajectory_ncfovsrevgr_252d_base_v037_signal,
    f25ft_f25_fcf_trajectory_fcfmarginflect_252d_base_v038_signal,
    f25ft_f25_fcf_trajectory_fcfgrmom_126d_base_v039_signal,
    f25ft_f25_fcf_trajectory_fcflevelz_504d_base_v040_signal,
    f25ft_f25_fcf_trajectory_ncfolevelrank_504d_base_v041_signal,
    f25ft_f25_fcf_trajectory_fcfmargrngpos_504d_base_v042_signal,
    f25ft_f25_fcf_trajectory_fcftroughrecov_504d_base_v043_signal,
    f25ft_f25_fcf_trajectory_fcfdrawdown_504d_base_v044_signal,
    f25ft_f25_fcf_trajectory_fcfmargconv_252d_base_v045_signal,
    f25ft_f25_fcf_trajectory_fcfconsistwt_252d_base_v046_signal,
    f25ft_f25_fcf_trajectory_capexdrag_252d_base_v047_signal,
    f25ft_f25_fcf_trajectory_fcfmargyoyacc_252d_base_v048_signal,
    f25ft_f25_fcf_trajectory_fcfpsconsist_252d_base_v049_signal,
    f25ft_f25_fcf_trajectory_fcfmargvoltrend_base_v050_signal,
    f25ft_f25_fcf_trajectory_fcfbreadth_504d_base_v051_signal,
    f25ft_f25_fcf_trajectory_fcfmargdisp_252d_base_v052_signal,
    f25ft_f25_fcf_trajectory_ncfodrift_504d_base_v053_signal,
    f25ft_f25_fcf_trajectory_fcfncfomarg_base_v054_signal,
    f25ft_f25_fcf_trajectory_fcfturn_252d_base_v055_signal,
    f25ft_f25_fcf_trajectory_fcfgrtanh_252d_base_v056_signal,
    f25ft_f25_fcf_trajectory_fcfmargtrendrank_base_v057_signal,
    f25ft_f25_fcf_trajectory_fcfgrspread_base_v058_signal,
    f25ft_f25_fcf_trajectory_ncfogrspread_base_v059_signal,
    f25ft_f25_fcf_trajectory_fcfmarglvltrend_base_v060_signal,
    f25ft_f25_fcf_trajectory_fcfstreakgr_base_v061_signal,
    f25ft_f25_fcf_trajectory_fcfmargtrendd_504d_base_v062_signal,
    f25ft_f25_fcf_trajectory_fcfgracc_504d_base_v063_signal,
    f25ft_f25_fcf_trajectory_ncfogrrk_504d_base_v064_signal,
    f25ft_f25_fcf_trajectory_convconsist_252d_base_v065_signal,
    f25ft_f25_fcf_trajectory_fcfmargcurv_252d_base_v066_signal,
    f25ft_f25_fcf_trajectory_fcfgrdisp_base_v067_signal,
    f25ft_f25_fcf_trajectory_fcfpsrank_504d_base_v068_signal,
    f25ft_f25_fcf_trajectory_fcfmargimprstreak_base_v069_signal,
    f25ft_f25_fcf_trajectory_ncfotrendrev_252d_base_v070_signal,
    f25ft_f25_fcf_trajectory_fcfmargcleantr_base_v071_signal,
    f25ft_f25_fcf_trajectory_fcfrevchgrank_base_v072_signal,
    f25ft_f25_fcf_trajectory_fcfinflect_504d_base_v073_signal,
    f25ft_f25_fcf_trajectory_fcfseqgr_63d_base_v074_signal,
    f25ft_f25_fcf_trajectory_cashtrajcomp_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F25_FCF_TRAJECTORY_REGISTRY_001_075 = REGISTRY


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
    fcf = _fund(3, n, base=8e7, drift=0.0, vol=0.55, allow_neg=True).rename("fcf")
    fcfps = _fund(5, n, base=3.0, drift=0.0, vol=0.55, allow_neg=True).rename("fcfps")
    ncfo = _fund(7, n, base=1.2e8, drift=0.0, vol=0.55, allow_neg=True).rename("ncfo")
    revenue = _fund(4, n, base=5e8, drift=0.01, vol=0.30).rename("revenue")

    cols = {"fcf": fcf, "fcfps": fcfps, "ncfo": ncfo, "revenue": revenue}

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

    print("OK f25_fcf_trajectory_base_001_075_claude: %d features pass" % n_features)
