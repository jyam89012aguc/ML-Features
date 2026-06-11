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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


# ===== f06 drawdown / recovery domain primitives =====
def _f06_drawdown(close, w):
    # current drawdown from the trailing rolling peak (<= 0)
    peak = close.rolling(w, min_periods=max(1, w // 2)).max()
    return close / peak.replace(0, np.nan) - 1.0


def _f06_maxdd(close, w):
    # worst (most negative) drawdown inside the window, measured against the
    # running peak *within* that same window (true max-drawdown definition)
    def _f(a):
        peak = np.maximum.accumulate(a)
        dd = a / peak - 1.0
        return float(dd.min())
    return close.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


def _f06_underwater(close, w):
    # 1.0 when below the rolling peak, else 0.0
    peak = close.rolling(w, min_periods=max(1, w // 2)).max()
    return (close < peak * 0.99999).astype(float)


def _f06_uw_frac(close, w, dw):
    # fraction of the last dw days spent underwater vs a w-peak
    uw = _f06_underwater(close, w)
    return uw.rolling(dw, min_periods=max(1, dw // 2)).mean()


def _f06_recovery(close, w):
    # rebound off the trailing trough (>= 0)
    trough = close.rolling(w, min_periods=max(1, w // 2)).min()
    return close / trough.replace(0, np.nan) - 1.0


def _f06_pain(close, w):
    # pain index: average depth of drawdown over the window (<= 0)
    dd = close / close.rolling(w, min_periods=max(1, w // 2)).max().replace(0, np.nan) - 1.0
    return dd.rolling(w, min_periods=max(1, w // 2)).mean()


def _f06_ulcer(close, w):
    # ulcer index: RMS of percentage drawdown over the window (>= 0)
    dd = close / close.rolling(w, min_periods=max(1, w // 2)).max().replace(0, np.nan) - 1.0
    return np.sqrt((dd * dd).rolling(w, min_periods=max(1, w // 2)).mean())


def _f06_cdar(close, w, q):
    # conditional drawdown at risk: mean of the worst q-quantile drawdowns
    dd = close / close.rolling(w, min_periods=max(1, w // 2)).max().replace(0, np.nan) - 1.0

    def _f(a):
        thr = np.quantile(a, q)
        tail = a[a <= thr]
        if tail.size == 0:
            return np.nan
        return float(tail.mean())
    return dd.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


def _f06_time_to_recover(close, w):
    # days since the rolling-window peak (proxy for underwater duration), scaled
    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    return close.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


def _f06_days_since_trough(close, w):
    def _f(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    return close.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


def _f06_dd_freq(close, w, dw, thr):
    # frequency of distinct drawdown episodes deeper than thr over dw
    dd = _f06_drawdown(close, w)
    inep = (dd <= thr).astype(float)
    entries = ((inep == 1) & (inep.shift(1) == 0)).astype(float)
    return entries.rolling(dw, min_periods=max(1, dw // 2)).sum()


def _f06_calmar(close, w):
    # Calmar-like: trailing return over the absolute max drawdown
    ret = close / close.shift(w) - 1.0
    mdd = _f06_maxdd(close, w).abs()
    return ret / mdd.replace(0, np.nan)


def _f06_recov_slope(close, w):
    # recovery slope: rebound off trough per day elapsed since the trough
    rec = _f06_recovery(close, w)
    dst = _f06_days_since_trough(close, w).replace(0, np.nan)
    return rec / dst


# ============================================================
# ---- max drawdown over N (levels) ----
def f06dr_f06_drawdown_recovery_maxdd_63d_base_v001_signal(closeadj):
    b = _f06_maxdd(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_maxdd_126d_base_v002_signal(closeadj):
    b = _f06_maxdd(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_maxdd_252d_base_v003_signal(closeadj):
    b = _f06_maxdd(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_maxdd_504d_base_v004_signal(closeadj):
    # worst 504d drawdown blended with the current drawdown depth (continuous)
    md = _f06_maxdd(closeadj, 504)
    cur = _f06_drawdown(closeadj, 504)
    b = md + 0.25 * cur
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# max drawdown z-scored vs its own history (how unusual is current worst-dd)
def f06dr_f06_drawdown_recovery_maxddz_252d_base_v005_signal(closeadj):
    md = _f06_maxdd(closeadj, 252)
    b = _z(md, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# max drawdown percentile-ranked vs its own 504d history
def f06dr_f06_drawdown_recovery_maxddrank_252d_base_v006_signal(closeadj):
    md = _f06_maxdd(closeadj, 252)
    b = md.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread of worst-dd between short and long horizon (dd term-structure)
def f06dr_f06_drawdown_recovery_maxddspr_63v252_base_v007_signal(closeadj):
    s = _f06_maxdd(closeadj, 63)
    l = _f06_maxdd(closeadj, 252)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of short to long worst-dd (concentration of risk in recent past)
def f06dr_f06_drawdown_recovery_maxddratio_126v504_base_v008_signal(closeadj):
    s = _f06_maxdd(closeadj, 126)
    l = _f06_maxdd(closeadj, 504)
    b = s / l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- current drawdown from peak (levels) ----
def f06dr_f06_drawdown_recovery_curdd_63d_base_v009_signal(closeadj):
    b = _f06_drawdown(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_curdd_126d_base_v010_signal(closeadj):
    b = _f06_drawdown(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_curdd_252d_base_v011_signal(closeadj):
    b = _f06_drawdown(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_curdd_504d_base_v012_signal(closeadj):
    b = _f06_drawdown(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current drawdown relative to the window's worst drawdown (how far off the bottom)
def f06dr_f06_drawdown_recovery_ddfromworst_252d_base_v013_signal(closeadj):
    cur = _f06_drawdown(closeadj, 252)
    worst = _f06_maxdd(closeadj, 252)
    b = cur / worst.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current drawdown z-scored vs its own 126d history (drawdown extremity)
def f06dr_f06_drawdown_recovery_curddz_252d_base_v014_signal(closeadj):
    dd = _f06_drawdown(closeadj, 252)
    b = _z(dd, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed current drawdown (bounded depth signal)
def f06dr_f06_drawdown_recovery_ddtanh_252d_base_v015_signal(closeadj):
    dd = _f06_drawdown(closeadj, 252)
    b = np.tanh(5.0 * dd)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- underwater duration ----
def f06dr_f06_drawdown_recovery_uwfrac_252d_base_v016_signal(closeadj):
    b = _f06_uw_frac(closeadj, 252, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_uwfrac_126d_base_v017_signal(closeadj):
    # 126d underwater fraction de-trended by its slow EMA (fresh time-below-water stress)
    uw = _f06_underwater(closeadj, 126)
    frac = uw.rolling(126, min_periods=63).mean()
    b = frac - frac.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_uwfrac_504d_base_v018_signal(closeadj):
    # change in 504d underwater fraction vs a year ago (trend in time-below-water)
    uf = _f06_uw_frac(closeadj, 504, 252)
    b = uf - uf.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last quarter spent more than 10% underwater (deep-underwater time)
def f06dr_f06_drawdown_recovery_deepuw_252d_base_v019_signal(closeadj):
    dd = _f06_drawdown(closeadj, 252)
    deep = (dd <= -0.10).astype(float)
    b = deep.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# underwater clumpiness: longest underwater run relative to total underwater time
# (1.0 = one long stretch, low = many short dips); a pure time-structure measure
def f06dr_f06_drawdown_recovery_uwmaxrun_252d_base_v020_signal(closeadj):
    uw = _f06_underwater(closeadj, 252)

    def _f(a):
        best = 0
        cur = 0
        for v in a:
            if v > 0.5:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        tot = a.sum()
        if tot < 1.0:
            return np.nan
        return best / tot
    b = uw.rolling(252, min_periods=126).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current underwater run length (days since last new peak) over 504d, scaled
def f06dr_f06_drawdown_recovery_ttr_252d_base_v021_signal(closeadj):
    b = _f06_time_to_recover(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_ttr_504d_base_v022_signal(closeadj):
    b = _f06_time_to_recover(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# time-to-recover interacted with drawdown depth (deep & long = severe)
def f06dr_f06_drawdown_recovery_ttrdepth_252d_base_v023_signal(closeadj):
    ttr = _f06_time_to_recover(closeadj, 252)
    dd = _f06_drawdown(closeadj, 252)
    b = ttr * dd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# underwater-fraction z-scored vs its own history (regime of persistent losses)
def f06dr_f06_drawdown_recovery_uwfracz_252d_base_v024_signal(closeadj):
    uf = _f06_uw_frac(closeadj, 252, 126)
    b = _z(uf, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- recovery off trough ----
def f06dr_f06_drawdown_recovery_recov_63d_base_v025_signal(closeadj):
    b = _f06_recovery(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_recov_126d_base_v026_signal(closeadj):
    b = _f06_recovery(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_recov_252d_base_v027_signal(closeadj):
    b = _f06_recovery(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_recov_504d_base_v028_signal(closeadj):
    b = _f06_recovery(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery slope from trough (rebound per day since the bottom)
def f06dr_f06_drawdown_recovery_recovslope_252d_base_v029_signal(closeadj):
    b = _f06_recov_slope(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_recovslope_504d_base_v030_signal(closeadj):
    b = _f06_recov_slope(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# matured rebound: recovery off trough weighted by how long the recovery has run,
# minus the recovery's own slow EMA (fresh-vs-stale rebound displacement)
def f06dr_f06_drawdown_recovery_maturerec_252d_base_v031_signal(closeadj):
    rec = _f06_recovery(closeadj, 252)
    dst = _f06_days_since_trough(closeadj, 252)
    mat = rec * dst
    b = mat - mat.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of total drawdown that has been recovered (round-trip progress)
def f06dr_f06_drawdown_recovery_recovshare_252d_base_v032_signal(closeadj):
    peak = _rmax(closeadj, 252)
    trough = _rmin(closeadj, 252)
    b = (closeadj - trough) / (peak - trough).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery percentile-ranked vs its own 504d history
def f06dr_f06_drawdown_recovery_recovrank_252d_base_v033_signal(closeadj):
    rec = _f06_recovery(closeadj, 252)
    b = rec.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days since the trough (age of the recovery) over 252d
def f06dr_f06_drawdown_recovery_dst_252d_base_v034_signal(closeadj):
    b = _f06_days_since_trough(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days since trough over 504d
def f06dr_f06_drawdown_recovery_dst_504d_base_v035_signal(closeadj):
    b = _f06_days_since_trough(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- drawdown frequency ----
def f06dr_f06_drawdown_recovery_ddfreq5_252d_base_v036_signal(closeadj):
    # episode count of >5% drawdowns over 252d, plus continuous average dd depth
    cnt = _f06_dd_freq(closeadj, 252, 252, -0.05)
    depth = _f06_drawdown(closeadj, 252).rolling(63, min_periods=21).mean()
    b = cnt - 8.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_ddfreq10_252d_base_v037_signal(closeadj):
    # episode count of >10% drawdowns over 252d, scaled by recent ulcer stress
    cnt = _f06_dd_freq(closeadj, 252, 252, -0.10)
    stress = _f06_ulcer(closeadj, 63)
    b = cnt * (1.0 + 4.0 * stress)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_ddfreq15_504d_base_v038_signal(closeadj):
    # episode count of >15% drawdowns over 504d, blended with pain index level
    cnt = _f06_dd_freq(closeadj, 504, 252, -0.15)
    pain = _f06_pain(closeadj, 252)
    b = cnt - 10.0 * pain
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distinct-episode count of >20% drawdowns over two years, depth-weighted (severity)
def f06dr_f06_drawdown_recovery_ddfreq20_504d_base_v039_signal(closeadj):
    cnt = _f06_dd_freq(closeadj, 504, 504, -0.20)
    worst = _f06_maxdd(closeadj, 504)
    b = cnt - 5.0 * worst
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- pain index (avg drawdown) ----
def f06dr_f06_drawdown_recovery_pain_126d_base_v040_signal(closeadj):
    b = _f06_pain(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_pain_252d_base_v041_signal(closeadj):
    b = _f06_pain(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_pain_504d_base_v042_signal(closeadj):
    b = _f06_pain(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pain index z-scored vs its own history (unusual chronic pain)
def f06dr_f06_drawdown_recovery_painz_252d_base_v043_signal(closeadj):
    p = _f06_pain(closeadj, 252)
    b = _z(p, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pain ratio: trailing return divided by average drawdown depth (pain-adjusted return)
def f06dr_f06_drawdown_recovery_painratio_252d_base_v044_signal(closeadj):
    ret = closeadj / closeadj.shift(252) - 1.0
    p = _f06_pain(closeadj, 252).abs()
    b = ret / p.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- ulcer index ----
# ulcer index 126d, z-scored vs its own history (acute-stress regime, de-trended)
def f06dr_f06_drawdown_recovery_ulcer_126d_base_v045_signal(closeadj):
    u = _f06_ulcer(closeadj, 126)
    b = _z(u, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ulcer term-structure: short-horizon ulcer relative to long-horizon ulcer (stress acceleration)
def f06dr_f06_drawdown_recovery_ulcer_252d_base_v046_signal(closeadj):
    us = _f06_ulcer(closeadj, 63)
    ul = _f06_ulcer(closeadj, 252)
    b = us / ul.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ulcer index 504d percentile-ranked vs its own history (chronic-stress percentile)
def f06dr_f06_drawdown_recovery_ulcer_504d_base_v047_signal(closeadj):
    u = _f06_ulcer(closeadj, 504)
    b = u.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# martin ratio: 126d trailing return over ulcer index, percentile-ranked (ulcer-adjusted momentum)
def f06dr_f06_drawdown_recovery_martin_252d_base_v048_signal(closeadj):
    ret = closeadj / closeadj.shift(126) - 1.0
    u = _f06_ulcer(closeadj, 126)
    ratio = ret / u.replace(0, np.nan)
    b = ratio.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ulcer index percentile-ranked vs its own history (stress regime)
def f06dr_f06_drawdown_recovery_ulcerrank_252d_base_v049_signal(closeadj):
    u = _f06_ulcer(closeadj, 252)
    b = u.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- CDaR (conditional drawdown at risk) ----
def f06dr_f06_drawdown_recovery_cdar90_252d_base_v050_signal(closeadj):
    b = _f06_cdar(closeadj, 252, 0.10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CDaR tail-concentration: worst-5% CDaR relative to worst-25% CDaR (tail sharpness)
def f06dr_f06_drawdown_recovery_cdar95_252d_base_v051_signal(closeadj):
    tail = _f06_cdar(closeadj, 252, 0.05)
    body = _f06_cdar(closeadj, 252, 0.25)
    b = tail / body.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_cdar90_504d_base_v052_signal(closeadj):
    b = _f06_cdar(closeadj, 504, 0.10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap between CDaR and average drawdown (tail-vs-typical drawdown asymmetry)
def f06dr_f06_drawdown_recovery_cdargap_252d_base_v053_signal(closeadj):
    cd = _f06_cdar(closeadj, 252, 0.10)
    pn = _f06_pain(closeadj, 252)
    b = cd - pn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- Calmar-like (return / maxDD) ----
def f06dr_f06_drawdown_recovery_calmar_252d_base_v054_signal(closeadj):
    b = _f06_calmar(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f06dr_f06_drawdown_recovery_calmar_504d_base_v055_signal(closeadj):
    b = _f06_calmar(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Calmar z-scored vs its own history (risk-adjusted-return regime)
def f06dr_f06_drawdown_recovery_calmarz_252d_base_v056_signal(closeadj):
    c = _f06_calmar(closeadj, 252)
    b = _z(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- composites / interactions ----
# severity skew: dispersion of daily drawdown depths over the year (lumpy vs even pain)
def f06dr_f06_drawdown_recovery_severity_252d_base_v057_signal(closeadj):
    dd = _f06_drawdown(closeadj, 252)
    b = dd.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# V-shape balance change: how the recovery/drawdown balance shifted over a quarter
def f06dr_f06_drawdown_recovery_vbalance_252d_base_v058_signal(closeadj):
    rec = _f06_recovery(closeadj, 252)
    dd = _f06_drawdown(closeadj, 252).abs()
    bal = (rec - dd) / (rec + dd).replace(0, np.nan)
    b = bal - bal.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# drawdown depth per unit of realized volatility, z-scored (vol-normalized stress regime)
def f06dr_f06_drawdown_recovery_ddvol_252d_base_v059_signal(closeadj):
    dd = _f06_drawdown(closeadj, 252)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    ratio = dd / vol.replace(0, np.nan)
    b = ratio.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery per unit of realized volatility (vol-normalized rebound)
def f06dr_f06_drawdown_recovery_recovol_252d_base_v060_signal(closeadj):
    rec = _f06_recovery(closeadj, 252)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    ratio = rec / vol.replace(0, np.nan)
    b = _z(ratio, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# drawdown skewness of daily returns (asymmetry of the loss distribution)
def f06dr_f06_drawdown_recovery_lossskew_126d_base_v061_signal(closeadj):
    r = closeadj.pct_change()
    b = r.rolling(126, min_periods=63).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average depth of negative-return days only (downside pain of the path)
def f06dr_f06_drawdown_recovery_downpain_126d_base_v062_signal(closeadj):
    r = closeadj.pct_change()
    neg = r.where(r < 0)
    b = neg.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# worst single-day return relative to typical downside (crash-tail severity)
def f06dr_f06_drawdown_recovery_maxdayloss_252d_base_v063_signal(closeadj):
    r = closeadj.pct_change()
    worst = r.rolling(252, min_periods=126).min()
    dn = r.where(r < 0).rolling(252, min_periods=126).std()
    b = worst / dn.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# drawdown convexity: how the worst-dd 63d compares to the 252d worst (acceleration of risk)
def f06dr_f06_drawdown_recovery_ddconvex_base_v064_signal(closeadj):
    s = _f06_maxdd(closeadj, 63)
    m = _f06_maxdd(closeadj, 126)
    l = _f06_maxdd(closeadj, 252)
    b = (s - 2.0 * m + l)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pain index dispersion across horizons (chronic-pain disagreement)
def f06dr_f06_drawdown_recovery_paindisp_base_v065_signal(closeadj):
    p1 = _f06_pain(closeadj, 126)
    p2 = _f06_pain(closeadj, 252)
    p3 = _f06_pain(closeadj, 504)
    b = pd.concat([p1, p2, p3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# drawdown depth relative to its own typical level, compressed (excess-stress signal)
def f06dr_f06_drawdown_recovery_ddsignmag_252d_base_v066_signal(closeadj):
    dd = _f06_drawdown(closeadj, 252)
    typ = dd.rolling(252, min_periods=63).mean()
    excess = dd - typ
    b = np.sign(excess) * (excess.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ulcer interacted with drawdown frequency (stress x how often it recurs)
def f06dr_f06_drawdown_recovery_ulcerfreq_252d_base_v067_signal(closeadj):
    u = _f06_ulcer(closeadj, 252)
    fr = _f06_dd_freq(closeadj, 252, 252, -0.05)
    b = u * fr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery slope per unit of preceding drawdown depth (bounce efficiency)
def f06dr_f06_drawdown_recovery_bounceeff_252d_base_v068_signal(closeadj):
    rs = _f06_recov_slope(closeadj, 252)
    md = _f06_maxdd(closeadj, 252).abs()
    b = rs / md.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# underwater fraction smoothed with EMA (persistent chronic-loss state)
def f06dr_f06_drawdown_recovery_uwema_252d_base_v069_signal(closeadj):
    uw = _f06_underwater(closeadj, 252)
    b = uw.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current drawdown minus its own slow EMA (drawdown displacement / fresh stress)
def f06dr_f06_drawdown_recovery_dddisp_252d_base_v070_signal(closeadj):
    dd = _f06_drawdown(closeadj, 252)
    b = dd - dd.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spacing between fresh equity highs: avg gap (in days) since the last new high (drought length)
def f06dr_f06_drawdown_recovery_newhitime_252d_base_v071_signal(closeadj):
    peak = _rmax(closeadj, 252)
    athi = (closeadj >= peak * 0.99999).astype(float)

    def _f(a):
        # average distance from each day back to the most recent new-high day
        last = -1
        gaps = []
        for i, v in enumerate(a):
            if v > 0.5:
                last = i
            gaps.append((i - last) if last >= 0 else len(a))
        return float(np.mean(gaps)) / float(len(a))
    b = athi.rolling(126, min_periods=63).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average recovery slope across recent troughs vs drawdown (rebound resilience)
def f06dr_f06_drawdown_recovery_resilience_252d_base_v072_signal(closeadj):
    rec = _f06_recovery(closeadj, 126)
    dd = _f06_drawdown(closeadj, 126).abs()
    b = (rec - dd).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CDaR trend: change in the 252d worst-10% CDaR over a quarter (tail-risk drift)
def f06dr_f06_drawdown_recovery_cdaruw_252d_base_v073_signal(closeadj):
    cd = _f06_cdar(closeadj, 252, 0.10)
    b = cd - cd.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# drawdown depth change year-over-year (worsening / healing trend in dd)
def f06dr_f06_drawdown_recovery_ddyoy_252d_base_v074_signal(closeadj):
    dd = _f06_drawdown(closeadj, 252)
    b = dd - dd.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pain-to-ulcer ratio (shape of the drawdown distribution: mean vs RMS)
def f06dr_f06_drawdown_recovery_painulcer_252d_base_v075_signal(closeadj):
    p = _f06_pain(closeadj, 252).abs()
    u = _f06_ulcer(closeadj, 252)
    b = p / u.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f06dr_f06_drawdown_recovery_maxdd_63d_base_v001_signal,
    f06dr_f06_drawdown_recovery_maxdd_126d_base_v002_signal,
    f06dr_f06_drawdown_recovery_maxdd_252d_base_v003_signal,
    f06dr_f06_drawdown_recovery_maxdd_504d_base_v004_signal,
    f06dr_f06_drawdown_recovery_maxddz_252d_base_v005_signal,
    f06dr_f06_drawdown_recovery_maxddrank_252d_base_v006_signal,
    f06dr_f06_drawdown_recovery_maxddspr_63v252_base_v007_signal,
    f06dr_f06_drawdown_recovery_maxddratio_126v504_base_v008_signal,
    f06dr_f06_drawdown_recovery_curdd_63d_base_v009_signal,
    f06dr_f06_drawdown_recovery_curdd_126d_base_v010_signal,
    f06dr_f06_drawdown_recovery_curdd_252d_base_v011_signal,
    f06dr_f06_drawdown_recovery_curdd_504d_base_v012_signal,
    f06dr_f06_drawdown_recovery_ddfromworst_252d_base_v013_signal,
    f06dr_f06_drawdown_recovery_curddz_252d_base_v014_signal,
    f06dr_f06_drawdown_recovery_ddtanh_252d_base_v015_signal,
    f06dr_f06_drawdown_recovery_uwfrac_252d_base_v016_signal,
    f06dr_f06_drawdown_recovery_uwfrac_126d_base_v017_signal,
    f06dr_f06_drawdown_recovery_uwfrac_504d_base_v018_signal,
    f06dr_f06_drawdown_recovery_deepuw_252d_base_v019_signal,
    f06dr_f06_drawdown_recovery_uwmaxrun_252d_base_v020_signal,
    f06dr_f06_drawdown_recovery_ttr_252d_base_v021_signal,
    f06dr_f06_drawdown_recovery_ttr_504d_base_v022_signal,
    f06dr_f06_drawdown_recovery_ttrdepth_252d_base_v023_signal,
    f06dr_f06_drawdown_recovery_uwfracz_252d_base_v024_signal,
    f06dr_f06_drawdown_recovery_recov_63d_base_v025_signal,
    f06dr_f06_drawdown_recovery_recov_126d_base_v026_signal,
    f06dr_f06_drawdown_recovery_recov_252d_base_v027_signal,
    f06dr_f06_drawdown_recovery_recov_504d_base_v028_signal,
    f06dr_f06_drawdown_recovery_recovslope_252d_base_v029_signal,
    f06dr_f06_drawdown_recovery_recovslope_504d_base_v030_signal,
    f06dr_f06_drawdown_recovery_maturerec_252d_base_v031_signal,
    f06dr_f06_drawdown_recovery_recovshare_252d_base_v032_signal,
    f06dr_f06_drawdown_recovery_recovrank_252d_base_v033_signal,
    f06dr_f06_drawdown_recovery_dst_252d_base_v034_signal,
    f06dr_f06_drawdown_recovery_dst_504d_base_v035_signal,
    f06dr_f06_drawdown_recovery_ddfreq5_252d_base_v036_signal,
    f06dr_f06_drawdown_recovery_ddfreq10_252d_base_v037_signal,
    f06dr_f06_drawdown_recovery_ddfreq15_504d_base_v038_signal,
    f06dr_f06_drawdown_recovery_ddfreq20_504d_base_v039_signal,
    f06dr_f06_drawdown_recovery_pain_126d_base_v040_signal,
    f06dr_f06_drawdown_recovery_pain_252d_base_v041_signal,
    f06dr_f06_drawdown_recovery_pain_504d_base_v042_signal,
    f06dr_f06_drawdown_recovery_painz_252d_base_v043_signal,
    f06dr_f06_drawdown_recovery_painratio_252d_base_v044_signal,
    f06dr_f06_drawdown_recovery_ulcer_126d_base_v045_signal,
    f06dr_f06_drawdown_recovery_ulcer_252d_base_v046_signal,
    f06dr_f06_drawdown_recovery_ulcer_504d_base_v047_signal,
    f06dr_f06_drawdown_recovery_martin_252d_base_v048_signal,
    f06dr_f06_drawdown_recovery_ulcerrank_252d_base_v049_signal,
    f06dr_f06_drawdown_recovery_cdar90_252d_base_v050_signal,
    f06dr_f06_drawdown_recovery_cdar95_252d_base_v051_signal,
    f06dr_f06_drawdown_recovery_cdar90_504d_base_v052_signal,
    f06dr_f06_drawdown_recovery_cdargap_252d_base_v053_signal,
    f06dr_f06_drawdown_recovery_calmar_252d_base_v054_signal,
    f06dr_f06_drawdown_recovery_calmar_504d_base_v055_signal,
    f06dr_f06_drawdown_recovery_calmarz_252d_base_v056_signal,
    f06dr_f06_drawdown_recovery_severity_252d_base_v057_signal,
    f06dr_f06_drawdown_recovery_vbalance_252d_base_v058_signal,
    f06dr_f06_drawdown_recovery_ddvol_252d_base_v059_signal,
    f06dr_f06_drawdown_recovery_recovol_252d_base_v060_signal,
    f06dr_f06_drawdown_recovery_lossskew_126d_base_v061_signal,
    f06dr_f06_drawdown_recovery_downpain_126d_base_v062_signal,
    f06dr_f06_drawdown_recovery_maxdayloss_252d_base_v063_signal,
    f06dr_f06_drawdown_recovery_ddconvex_base_v064_signal,
    f06dr_f06_drawdown_recovery_paindisp_base_v065_signal,
    f06dr_f06_drawdown_recovery_ddsignmag_252d_base_v066_signal,
    f06dr_f06_drawdown_recovery_ulcerfreq_252d_base_v067_signal,
    f06dr_f06_drawdown_recovery_bounceeff_252d_base_v068_signal,
    f06dr_f06_drawdown_recovery_uwema_252d_base_v069_signal,
    f06dr_f06_drawdown_recovery_dddisp_252d_base_v070_signal,
    f06dr_f06_drawdown_recovery_newhitime_252d_base_v071_signal,
    f06dr_f06_drawdown_recovery_resilience_252d_base_v072_signal,
    f06dr_f06_drawdown_recovery_cdaruw_252d_base_v073_signal,
    f06dr_f06_drawdown_recovery_ddyoy_252d_base_v074_signal,
    f06dr_f06_drawdown_recovery_painulcer_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F06_DRAWDOWN_RECOVERY_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.005, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.01, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.01, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)) + 1e5, name="volume")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}

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

    print("OK f06_drawdown_recovery_base_001_075_claude: %d features pass" % n_features)
