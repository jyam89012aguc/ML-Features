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


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


# ===== folder domain primitives (revenue growth engine) =====
def _f23_growth(rev, w):
    return rev / rev.shift(w).replace(0, np.nan) - 1.0


def _f23_log_growth(rev, w):
    return np.log(rev.replace(0, np.nan) / rev.shift(w).replace(0, np.nan))


def _f23_cagr(rev, w, periods_per_year=252.0):
    r = rev / rev.shift(w).replace(0, np.nan)
    return r.clip(lower=1e-9) ** (periods_per_year / float(w)) - 1.0


def _f23_growth_std(rev, w, gw):
    g = _f23_growth(rev, gw)
    return g.rolling(w, min_periods=max(1, w // 2)).std()


def _f23_logslope(rev, w):
    lr = np.log(rev.replace(0, np.nan))

    def _sl(a):
        x = np.arange(len(a), dtype=float)
        d = x - x.mean()
        den = (d * d).sum()
        if den == 0:
            return np.nan
        return (d * (a - a.mean())).sum() / den

    return lr.rolling(w, min_periods=max(2, w // 2)).apply(_sl, raw=True)


def f23rg_f23_revenue_growth_engine_grw_63d_slope_v001_signal(revenue):
    base = _f23_growth(revenue, 63)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_grw_126d_slope_v002_signal(revenue):
    base = _f23_growth(revenue, 126)
    deriv = base - base.shift(42)
    result = deriv.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_grw_252d_slope_v003_signal(revenue):
    base = _f23_growth(revenue, 252)
    deriv = base - base.shift(63)
    sd = deriv.rolling(252, min_periods=126).std()
    result = deriv / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_grw_504d_slope_v004_signal(revenue):
    base = _f23_growth(revenue, 504)
    deriv = base - base.shift(126)
    result = deriv.rolling(504, min_periods=252).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_grw_315d_slope_v005_signal(revenue):
    base = _f23_growth(revenue, 315)
    deriv = base - base.shift(63)
    sc = deriv.abs().rolling(315, min_periods=157).mean()
    result = np.tanh(deriv / sc.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_lgrw_63d_slope_v006_signal(revenueusd):
    base = _f23_log_growth(revenueusd, 63)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_lgrw_126d_slope_v007_signal(revenueusd):
    base = _f23_log_growth(revenueusd, 126)
    deriv = base - base.shift(42)
    result = deriv.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_lgrw_252d_slope_v008_signal(revenueusd):
    base = _f23_log_growth(revenueusd, 252)
    deriv = base - base.shift(63)
    sd = deriv.rolling(252, min_periods=126).std()
    result = deriv / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_lgrw_504d_slope_v009_signal(revenueusd):
    base = _f23_log_growth(revenueusd, 504)
    deriv = base - base.shift(126)
    result = deriv.rolling(504, min_periods=252).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_lgrw_315d_slope_v010_signal(revenueusd):
    base = _f23_log_growth(revenueusd, 315)
    deriv = base - base.shift(63)
    sc = deriv.abs().rolling(315, min_periods=157).mean()
    result = np.tanh(deriv / sc.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_autocorr_63d_slope_v011_signal(revenue):
    g = _f23_growth(revenue, 21)
    gl = g.shift(21)
    base = g.rolling(63, min_periods=31).corr(gl)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_autocorr_126d_slope_v012_signal(revenue):
    g = _f23_growth(revenue, 21)
    gl = g.shift(21)
    base = g.rolling(126, min_periods=63).corr(gl)
    deriv = base - base.shift(42)
    result = deriv.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_autocorr_252d_slope_v013_signal(revenue):
    g = _f23_growth(revenue, 21)
    gl = g.shift(21)
    base = g.rolling(252, min_periods=126).corr(gl)
    deriv = base - base.shift(63)
    sd = deriv.rolling(252, min_periods=126).std()
    result = deriv / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_autocorr_504d_slope_v014_signal(revenue):
    g = _f23_growth(revenue, 21)
    gl = g.shift(21)
    base = g.rolling(504, min_periods=252).corr(gl)
    deriv = base - base.shift(126)
    result = deriv.rolling(504, min_periods=252).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_autocorr_315d_slope_v015_signal(revenue):
    g = _f23_growth(revenue, 21)
    gl = g.shift(21)
    base = g.rolling(315, min_periods=157).corr(gl)
    deriv = base - base.shift(63)
    sc = deriv.abs().rolling(315, min_periods=157).mean()
    result = np.tanh(deriv / sc.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_levtrend_63d_slope_v016_signal(revenue):
    mn = _mean(revenue, 63)
    base = revenue / mn.replace(0, np.nan) - 1.0
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_levtrend_126d_slope_v017_signal(revenue):
    mn = _mean(revenue, 126)
    base = revenue / mn.replace(0, np.nan) - 1.0
    deriv = base - base.shift(42)
    result = deriv.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_levtrend_252d_slope_v018_signal(revenue):
    mn = _mean(revenue, 252)
    base = revenue / mn.replace(0, np.nan) - 1.0
    deriv = base - base.shift(63)
    sd = deriv.rolling(252, min_periods=126).std()
    result = deriv / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_levtrend_504d_slope_v019_signal(revenue):
    mn = _mean(revenue, 504)
    base = revenue / mn.replace(0, np.nan) - 1.0
    deriv = base - base.shift(126)
    result = deriv.rolling(504, min_periods=252).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_levtrend_315d_slope_v020_signal(revenue):
    mn = _mean(revenue, 315)
    base = revenue / mn.replace(0, np.nan) - 1.0
    deriv = base - base.shift(63)
    sc = deriv.abs().rolling(315, min_periods=157).mean()
    result = np.tanh(deriv / sc.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_revhi_63d_slope_v021_signal(revenue):
    hi = _rmax(revenue, 63)
    base = revenue / hi.replace(0, np.nan)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_revhi_126d_slope_v022_signal(revenue):
    hi = _rmax(revenue, 126)
    base = revenue / hi.replace(0, np.nan)
    deriv = base - base.shift(42)
    result = deriv.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_revhi_252d_slope_v023_signal(revenue):
    hi = _rmax(revenue, 252)
    base = revenue / hi.replace(0, np.nan)
    deriv = base - base.shift(63)
    sd = deriv.rolling(252, min_periods=126).std()
    result = deriv / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_revhi_504d_slope_v024_signal(revenue):
    hi = _rmax(revenue, 504)
    base = revenue / hi.replace(0, np.nan)
    deriv = base - base.shift(126)
    result = deriv.rolling(504, min_periods=252).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_revhi_315d_slope_v025_signal(revenue):
    hi = _rmax(revenue, 315)
    base = revenue / hi.replace(0, np.nan)
    deriv = base - base.shift(63)
    sc = deriv.abs().rolling(315, min_periods=157).mean()
    result = np.tanh(deriv / sc.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_revlo_63d_slope_v026_signal(revenueusd):
    lo = _rmin(revenueusd, 63)
    base = revenueusd / lo.replace(0, np.nan) - 1.0
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_revlo_126d_slope_v027_signal(revenueusd):
    lo = _rmin(revenueusd, 126)
    base = revenueusd / lo.replace(0, np.nan) - 1.0
    deriv = base - base.shift(42)
    result = deriv.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_revlo_252d_slope_v028_signal(revenueusd):
    lo = _rmin(revenueusd, 252)
    base = revenueusd / lo.replace(0, np.nan) - 1.0
    deriv = base - base.shift(63)
    sd = deriv.rolling(252, min_periods=126).std()
    result = deriv / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_revlo_504d_slope_v029_signal(revenueusd):
    lo = _rmin(revenueusd, 504)
    base = revenueusd / lo.replace(0, np.nan) - 1.0
    deriv = base - base.shift(126)
    result = deriv.rolling(504, min_periods=252).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_revlo_315d_slope_v030_signal(revenueusd):
    lo = _rmin(revenueusd, 315)
    base = revenueusd / lo.replace(0, np.nan) - 1.0
    deriv = base - base.shift(63)
    sc = deriv.abs().rolling(315, min_periods=157).mean()
    result = np.tanh(deriv / sc.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gstd_63d_slope_v031_signal(revenue):
    base = _f23_growth_std(revenue, 63, 21)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gstd_126d_slope_v032_signal(revenue):
    base = _f23_growth_std(revenue, 126, 21)
    deriv = base - base.shift(42)
    result = deriv.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gstd_252d_slope_v033_signal(revenue):
    base = _f23_growth_std(revenue, 252, 21)
    deriv = base - base.shift(63)
    sd = deriv.rolling(252, min_periods=126).std()
    result = deriv / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gstd_504d_slope_v034_signal(revenue):
    base = _f23_growth_std(revenue, 504, 21)
    deriv = base - base.shift(126)
    result = deriv.rolling(504, min_periods=252).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gstd_315d_slope_v035_signal(revenue):
    base = _f23_growth_std(revenue, 315, 21)
    deriv = base - base.shift(63)
    sc = deriv.abs().rolling(315, min_periods=157).mean()
    result = np.tanh(deriv / sc.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gz_63d_slope_v036_signal(revenue):
    g = _f23_growth(revenue, 63)
    base = _z(g, 63)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gz_126d_slope_v037_signal(revenue):
    g = _f23_growth(revenue, 63)
    base = _z(g, 126)
    deriv = base - base.shift(42)
    result = deriv.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gz_252d_slope_v038_signal(revenue):
    g = _f23_growth(revenue, 63)
    base = _z(g, 252)
    deriv = base - base.shift(63)
    sd = deriv.rolling(252, min_periods=126).std()
    result = deriv / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gz_504d_slope_v039_signal(revenue):
    g = _f23_growth(revenue, 63)
    base = _z(g, 504)
    deriv = base - base.shift(126)
    result = deriv.rolling(504, min_periods=252).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gz_315d_slope_v040_signal(revenue):
    g = _f23_growth(revenue, 63)
    base = _z(g, 315)
    deriv = base - base.shift(63)
    sc = deriv.abs().rolling(315, min_periods=157).mean()
    result = np.tanh(deriv / sc.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_grank_63d_slope_v041_signal(revenueusd):
    g = _f23_growth(revenueusd, 63)
    base = _rank(g, 63)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_grank_126d_slope_v042_signal(revenueusd):
    g = _f23_growth(revenueusd, 63)
    base = _rank(g, 126)
    deriv = base - base.shift(42)
    result = deriv.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_grank_252d_slope_v043_signal(revenueusd):
    g = _f23_growth(revenueusd, 63)
    base = _rank(g, 252)
    deriv = base - base.shift(63)
    sd = deriv.rolling(252, min_periods=126).std()
    result = deriv / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_grank_504d_slope_v044_signal(revenueusd):
    g = _f23_growth(revenueusd, 63)
    base = _rank(g, 504)
    deriv = base - base.shift(126)
    result = deriv.rolling(504, min_periods=252).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_grank_315d_slope_v045_signal(revenueusd):
    g = _f23_growth(revenueusd, 63)
    base = _rank(g, 315)
    deriv = base - base.shift(63)
    sc = deriv.abs().rolling(315, min_periods=157).mean()
    result = np.tanh(deriv / sc.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_levz_63d_slope_v046_signal(revenueusd):
    base = _z(revenueusd, 63)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_levz_126d_slope_v047_signal(revenueusd):
    base = _z(revenueusd, 126)
    deriv = base - base.shift(42)
    result = deriv.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_levz_252d_slope_v048_signal(revenueusd):
    base = _z(revenueusd, 252)
    deriv = base - base.shift(63)
    sd = deriv.rolling(252, min_periods=126).std()
    result = deriv / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_levz_504d_slope_v049_signal(revenueusd):
    base = _z(revenueusd, 504)
    deriv = base - base.shift(126)
    result = deriv.rolling(504, min_periods=252).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_levz_315d_slope_v050_signal(revenueusd):
    base = _z(revenueusd, 315)
    deriv = base - base.shift(63)
    sc = deriv.abs().rolling(315, min_periods=157).mean()
    result = np.tanh(deriv / sc.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_qdisp_63d_slope_v051_signal(revenue):
    q = revenue / revenue.shift(63).replace(0, np.nan)
    stacked = pd.concat([q, q.shift(63), q.shift(126), q.shift(189)], axis=1)
    sp = stacked.std(axis=1)
    base = sp.rolling(63, min_periods=31).mean()
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_qdisp_126d_slope_v052_signal(revenue):
    q = revenue / revenue.shift(63).replace(0, np.nan)
    stacked = pd.concat([q, q.shift(63), q.shift(126), q.shift(189)], axis=1)
    sp = stacked.std(axis=1)
    base = sp.rolling(126, min_periods=63).mean()
    deriv = base - base.shift(42)
    result = deriv.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_qdisp_252d_slope_v053_signal(revenue):
    q = revenue / revenue.shift(63).replace(0, np.nan)
    stacked = pd.concat([q, q.shift(63), q.shift(126), q.shift(189)], axis=1)
    sp = stacked.std(axis=1)
    base = sp.rolling(252, min_periods=126).mean()
    deriv = base - base.shift(63)
    sd = deriv.rolling(252, min_periods=126).std()
    result = deriv / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_qdisp_504d_slope_v054_signal(revenue):
    q = revenue / revenue.shift(63).replace(0, np.nan)
    stacked = pd.concat([q, q.shift(63), q.shift(126), q.shift(189)], axis=1)
    sp = stacked.std(axis=1)
    base = sp.rolling(504, min_periods=252).mean()
    deriv = base - base.shift(126)
    result = deriv.rolling(504, min_periods=252).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_qdisp_315d_slope_v055_signal(revenue):
    q = revenue / revenue.shift(63).replace(0, np.nan)
    stacked = pd.concat([q, q.shift(63), q.shift(126), q.shift(189)], axis=1)
    sp = stacked.std(axis=1)
    base = sp.rolling(315, min_periods=157).mean()
    deriv = base - base.shift(63)
    sc = deriv.abs().rolling(315, min_periods=157).mean()
    result = np.tanh(deriv / sc.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gsharpe_63d_slope_v056_signal(revenueusd):
    g = _f23_growth(revenueusd, 126)
    sd = _f23_growth_std(revenueusd, 63, 63)
    base = g / sd.replace(0, np.nan)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gsharpe_126d_slope_v057_signal(revenueusd):
    g = _f23_growth(revenueusd, 126)
    sd = _f23_growth_std(revenueusd, 126, 63)
    base = g / sd.replace(0, np.nan)
    deriv = base - base.shift(42)
    result = deriv.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gsharpe_252d_slope_v058_signal(revenueusd):
    g = _f23_growth(revenueusd, 126)
    sd = _f23_growth_std(revenueusd, 252, 63)
    base = g / sd.replace(0, np.nan)
    deriv = base - base.shift(63)
    sd = deriv.rolling(252, min_periods=126).std()
    result = deriv / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gsharpe_504d_slope_v059_signal(revenueusd):
    g = _f23_growth(revenueusd, 126)
    sd = _f23_growth_std(revenueusd, 504, 63)
    base = g / sd.replace(0, np.nan)
    deriv = base - base.shift(126)
    result = deriv.rolling(504, min_periods=252).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gsharpe_315d_slope_v060_signal(revenueusd):
    g = _f23_growth(revenueusd, 126)
    sd = _f23_growth_std(revenueusd, 315, 63)
    base = g / sd.replace(0, np.nan)
    deriv = base - base.shift(63)
    sc = deriv.abs().rolling(315, min_periods=157).mean()
    result = np.tanh(deriv / sc.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gmed_63d_slope_v061_signal(revenue):
    g = _f23_growth(revenue, 21)
    base = g.rolling(63, min_periods=31).median()
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gmed_126d_slope_v062_signal(revenue):
    g = _f23_growth(revenue, 21)
    base = g.rolling(126, min_periods=63).median()
    deriv = base - base.shift(42)
    result = deriv.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gmed_252d_slope_v063_signal(revenue):
    g = _f23_growth(revenue, 21)
    base = g.rolling(252, min_periods=126).median()
    deriv = base - base.shift(63)
    sd = deriv.rolling(252, min_periods=126).std()
    result = deriv / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gmed_504d_slope_v064_signal(revenue):
    g = _f23_growth(revenue, 21)
    base = g.rolling(504, min_periods=252).median()
    deriv = base - base.shift(126)
    result = deriv.rolling(504, min_periods=252).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gmed_315d_slope_v065_signal(revenue):
    g = _f23_growth(revenue, 21)
    base = g.rolling(315, min_periods=157).median()
    deriv = base - base.shift(63)
    sc = deriv.abs().rolling(315, min_periods=157).mean()
    result = np.tanh(deriv / sc.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gpos_63d_slope_v066_signal(revenue):
    g = _f23_growth(revenue, 21)
    mu = g.rolling(63, min_periods=31).mean()
    above = (g > mu).astype(float)
    base = above.rolling(63, min_periods=21).mean()
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gpos_126d_slope_v067_signal(revenue):
    g = _f23_growth(revenue, 21)
    mu = g.rolling(126, min_periods=63).mean()
    above = (g > mu).astype(float)
    base = above.rolling(63, min_periods=21).mean()
    deriv = base - base.shift(42)
    result = deriv.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gpos_252d_slope_v068_signal(revenue):
    g = _f23_growth(revenue, 21)
    mu = g.rolling(252, min_periods=126).mean()
    above = (g > mu).astype(float)
    base = above.rolling(63, min_periods=21).mean()
    deriv = base - base.shift(63)
    sd = deriv.rolling(252, min_periods=126).std()
    result = deriv / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gpos_504d_slope_v069_signal(revenue):
    g = _f23_growth(revenue, 21)
    mu = g.rolling(504, min_periods=252).mean()
    above = (g > mu).astype(float)
    base = above.rolling(63, min_periods=21).mean()
    deriv = base - base.shift(126)
    result = deriv.rolling(504, min_periods=252).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gpos_315d_slope_v070_signal(revenue):
    g = _f23_growth(revenue, 21)
    mu = g.rolling(315, min_periods=157).mean()
    above = (g > mu).astype(float)
    base = above.rolling(63, min_periods=21).mean()
    deriv = base - base.shift(63)
    sc = deriv.abs().rolling(315, min_periods=157).mean()
    result = np.tanh(deriv / sc.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_omega_63d_slope_v071_signal(revenue):
    g = _f23_growth(revenue, 5)
    up = g.clip(lower=0).rolling(126, min_periods=63).sum()
    dn = (-g.clip(upper=0)).rolling(126, min_periods=63).sum()
    om = np.log((up + 1e-9) / (dn + 1e-9))
    base = om.rolling(63, min_periods=31).rank(pct=True) - 0.5
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_omega_126d_slope_v072_signal(revenue):
    g = _f23_growth(revenue, 5)
    up = g.clip(lower=0).rolling(126, min_periods=63).sum()
    dn = (-g.clip(upper=0)).rolling(126, min_periods=63).sum()
    om = np.log((up + 1e-9) / (dn + 1e-9))
    base = om.rolling(126, min_periods=63).rank(pct=True) - 0.5
    deriv = base - base.shift(42)
    result = deriv.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_omega_252d_slope_v073_signal(revenue):
    g = _f23_growth(revenue, 5)
    up = g.clip(lower=0).rolling(126, min_periods=63).sum()
    dn = (-g.clip(upper=0)).rolling(126, min_periods=63).sum()
    om = np.log((up + 1e-9) / (dn + 1e-9))
    base = om.rolling(252, min_periods=126).rank(pct=True) - 0.5
    deriv = base - base.shift(63)
    sd = deriv.rolling(252, min_periods=126).std()
    result = deriv / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_omega_504d_slope_v074_signal(revenue):
    g = _f23_growth(revenue, 5)
    up = g.clip(lower=0).rolling(126, min_periods=63).sum()
    dn = (-g.clip(upper=0)).rolling(126, min_periods=63).sum()
    om = np.log((up + 1e-9) / (dn + 1e-9))
    base = om.rolling(504, min_periods=252).rank(pct=True) - 0.5
    deriv = base - base.shift(126)
    result = deriv.rolling(504, min_periods=252).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_omega_315d_slope_v075_signal(revenue):
    g = _f23_growth(revenue, 5)
    up = g.clip(lower=0).rolling(126, min_periods=63).sum()
    dn = (-g.clip(upper=0)).rolling(126, min_periods=63).sum()
    om = np.log((up + 1e-9) / (dn + 1e-9))
    base = om.rolling(315, min_periods=157).rank(pct=True) - 0.5
    deriv = base - base.shift(63)
    sc = deriv.abs().rolling(315, min_periods=157).mean()
    result = np.tanh(deriv / sc.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_seqacc_63d_slope_v076_signal(revenueusd):
    g = _f23_growth(revenueusd, 63)
    base = g - g.shift(max(21, 63 // 2))
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_seqacc_126d_slope_v077_signal(revenueusd):
    g = _f23_growth(revenueusd, 63)
    base = g - g.shift(max(21, 126 // 2))
    deriv = base - base.shift(42)
    result = deriv.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_seqacc_252d_slope_v078_signal(revenueusd):
    g = _f23_growth(revenueusd, 63)
    base = g - g.shift(max(21, 252 // 2))
    deriv = base - base.shift(63)
    sd = deriv.rolling(252, min_periods=126).std()
    result = deriv / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_seqacc_504d_slope_v079_signal(revenueusd):
    g = _f23_growth(revenueusd, 63)
    base = g - g.shift(max(21, 504 // 2))
    deriv = base - base.shift(126)
    result = deriv.rolling(504, min_periods=252).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_seqacc_315d_slope_v080_signal(revenueusd):
    g = _f23_growth(revenueusd, 63)
    base = g - g.shift(max(21, 315 // 2))
    deriv = base - base.shift(63)
    sc = deriv.abs().rolling(315, min_periods=157).mean()
    result = np.tanh(deriv / sc.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gsignmag_63d_slope_v081_signal(revenue):
    g = _f23_growth(revenue, 63)
    base = np.sign(g) * (g.abs() ** 0.5)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gsignmag_126d_slope_v082_signal(revenue):
    g = _f23_growth(revenue, 126)
    base = np.sign(g) * (g.abs() ** 0.5)
    deriv = base - base.shift(42)
    result = deriv.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gsignmag_252d_slope_v083_signal(revenue):
    g = _f23_growth(revenue, 252)
    base = np.sign(g) * (g.abs() ** 0.5)
    deriv = base - base.shift(63)
    sd = deriv.rolling(252, min_periods=126).std()
    result = deriv / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gsignmag_504d_slope_v084_signal(revenue):
    g = _f23_growth(revenue, 504)
    base = np.sign(g) * (g.abs() ** 0.5)
    deriv = base - base.shift(126)
    result = deriv.rolling(504, min_periods=252).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gsignmag_315d_slope_v085_signal(revenue):
    g = _f23_growth(revenue, 315)
    base = np.sign(g) * (g.abs() ** 0.5)
    deriv = base - base.shift(63)
    sc = deriv.abs().rolling(315, min_periods=157).mean()
    result = np.tanh(deriv / sc.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gexcess_63d_slope_v086_signal(revenueusd):
    g = _f23_growth(revenueusd, 21)
    med = g.rolling(63, min_periods=31).median()
    q75 = g.rolling(63, min_periods=31).quantile(0.75)
    q25 = g.rolling(63, min_periods=31).quantile(0.25)
    base = (g - med) / (q75 - q25).replace(0, np.nan)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gexcess_126d_slope_v087_signal(revenueusd):
    g = _f23_growth(revenueusd, 21)
    med = g.rolling(126, min_periods=63).median()
    q75 = g.rolling(126, min_periods=63).quantile(0.75)
    q25 = g.rolling(126, min_periods=63).quantile(0.25)
    base = (g - med) / (q75 - q25).replace(0, np.nan)
    deriv = base - base.shift(42)
    result = deriv.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gexcess_252d_slope_v088_signal(revenueusd):
    g = _f23_growth(revenueusd, 21)
    med = g.rolling(252, min_periods=126).median()
    q75 = g.rolling(252, min_periods=126).quantile(0.75)
    q25 = g.rolling(252, min_periods=126).quantile(0.25)
    base = (g - med) / (q75 - q25).replace(0, np.nan)
    deriv = base - base.shift(63)
    sd = deriv.rolling(252, min_periods=126).std()
    result = deriv / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gexcess_504d_slope_v089_signal(revenueusd):
    g = _f23_growth(revenueusd, 21)
    med = g.rolling(504, min_periods=252).median()
    q75 = g.rolling(504, min_periods=252).quantile(0.75)
    q25 = g.rolling(504, min_periods=252).quantile(0.25)
    base = (g - med) / (q75 - q25).replace(0, np.nan)
    deriv = base - base.shift(126)
    result = deriv.rolling(504, min_periods=252).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gexcess_315d_slope_v090_signal(revenueusd):
    g = _f23_growth(revenueusd, 21)
    med = g.rolling(315, min_periods=157).median()
    q75 = g.rolling(315, min_periods=157).quantile(0.75)
    q25 = g.rolling(315, min_periods=157).quantile(0.25)
    base = (g - med) / (q75 - q25).replace(0, np.nan)
    deriv = base - base.shift(63)
    sc = deriv.abs().rolling(315, min_periods=157).mean()
    result = np.tanh(deriv / sc.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_slopelr_63d_slope_v091_signal(revenue):
    base = _f23_logslope(revenue, 63)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_slopelr_126d_slope_v092_signal(revenue):
    base = _f23_logslope(revenue, 126)
    deriv = base - base.shift(42)
    result = deriv.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_slopelr_252d_slope_v093_signal(revenue):
    base = _f23_logslope(revenue, 252)
    deriv = base - base.shift(63)
    sd = deriv.rolling(252, min_periods=126).std()
    result = deriv / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_slopelr_504d_slope_v094_signal(revenue):
    base = _f23_logslope(revenue, 504)
    deriv = base - base.shift(126)
    result = deriv.rolling(504, min_periods=252).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_slopelr_315d_slope_v095_signal(revenue):
    base = _f23_logslope(revenue, 315)
    deriv = base - base.shift(63)
    sc = deriv.abs().rolling(315, min_periods=157).mean()
    result = np.tanh(deriv / sc.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gcv_63d_slope_v096_signal(revenue):
    g = _f23_growth(revenue, 63)
    mu = g.rolling(63, min_periods=31).mean()
    sd = g.rolling(63, min_periods=31).std()
    base = sd / mu.abs().replace(0, np.nan)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gcv_126d_slope_v097_signal(revenue):
    g = _f23_growth(revenue, 63)
    mu = g.rolling(126, min_periods=63).mean()
    sd = g.rolling(126, min_periods=63).std()
    base = sd / mu.abs().replace(0, np.nan)
    deriv = base - base.shift(42)
    result = deriv.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gcv_252d_slope_v098_signal(revenue):
    g = _f23_growth(revenue, 63)
    mu = g.rolling(252, min_periods=126).mean()
    sd = g.rolling(252, min_periods=126).std()
    base = sd / mu.abs().replace(0, np.nan)
    deriv = base - base.shift(63)
    sd = deriv.rolling(252, min_periods=126).std()
    result = deriv / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gcv_504d_slope_v099_signal(revenue):
    g = _f23_growth(revenue, 63)
    mu = g.rolling(504, min_periods=252).mean()
    sd = g.rolling(504, min_periods=252).std()
    base = sd / mu.abs().replace(0, np.nan)
    deriv = base - base.shift(126)
    result = deriv.rolling(504, min_periods=252).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gcv_315d_slope_v100_signal(revenue):
    g = _f23_growth(revenue, 63)
    mu = g.rolling(315, min_periods=157).mean()
    sd = g.rolling(315, min_periods=157).std()
    base = sd / mu.abs().replace(0, np.nan)
    deriv = base - base.shift(63)
    sc = deriv.abs().rolling(315, min_periods=157).mean()
    result = np.tanh(deriv / sc.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gupcap_63d_slope_v101_signal(revenueusd):
    g = _f23_growth(revenueusd, 21)
    up = g.clip(lower=0)
    base = up.rolling(63, min_periods=31).mean()
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gupcap_126d_slope_v102_signal(revenueusd):
    g = _f23_growth(revenueusd, 21)
    up = g.clip(lower=0)
    base = up.rolling(126, min_periods=63).mean()
    deriv = base - base.shift(42)
    result = deriv.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gupcap_252d_slope_v103_signal(revenueusd):
    g = _f23_growth(revenueusd, 21)
    up = g.clip(lower=0)
    base = up.rolling(252, min_periods=126).mean()
    deriv = base - base.shift(63)
    sd = deriv.rolling(252, min_periods=126).std()
    result = deriv / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gupcap_504d_slope_v104_signal(revenueusd):
    g = _f23_growth(revenueusd, 21)
    up = g.clip(lower=0)
    base = up.rolling(504, min_periods=252).mean()
    deriv = base - base.shift(126)
    result = deriv.rolling(504, min_periods=252).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gupcap_315d_slope_v105_signal(revenueusd):
    g = _f23_growth(revenueusd, 21)
    up = g.clip(lower=0)
    base = up.rolling(315, min_periods=157).mean()
    deriv = base - base.shift(63)
    sc = deriv.abs().rolling(315, min_periods=157).mean()
    result = np.tanh(deriv / sc.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gdncap_63d_slope_v106_signal(revenue):
    g = _f23_growth(revenue, 21)
    dn = g.clip(upper=0)
    base = dn.rolling(63, min_periods=31).mean()
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gdncap_126d_slope_v107_signal(revenue):
    g = _f23_growth(revenue, 21)
    dn = g.clip(upper=0)
    base = dn.rolling(126, min_periods=63).mean()
    deriv = base - base.shift(42)
    result = deriv.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gdncap_252d_slope_v108_signal(revenue):
    g = _f23_growth(revenue, 21)
    dn = g.clip(upper=0)
    base = dn.rolling(252, min_periods=126).mean()
    deriv = base - base.shift(63)
    sd = deriv.rolling(252, min_periods=126).std()
    result = deriv / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gdncap_504d_slope_v109_signal(revenue):
    g = _f23_growth(revenue, 21)
    dn = g.clip(upper=0)
    base = dn.rolling(504, min_periods=252).mean()
    deriv = base - base.shift(126)
    result = deriv.rolling(504, min_periods=252).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gdncap_315d_slope_v110_signal(revenue):
    g = _f23_growth(revenue, 21)
    dn = g.clip(upper=0)
    base = dn.rolling(315, min_periods=157).mean()
    deriv = base - base.shift(63)
    sc = deriv.abs().rolling(315, min_periods=157).mean()
    result = np.tanh(deriv / sc.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_giqr_63d_slope_v111_signal(revenue):
    g = _f23_growth(revenue, 21)
    q75 = g.rolling(63, min_periods=31).quantile(0.75)
    q25 = g.rolling(63, min_periods=31).quantile(0.25)
    base = q75 - q25
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_giqr_126d_slope_v112_signal(revenue):
    g = _f23_growth(revenue, 21)
    q75 = g.rolling(126, min_periods=63).quantile(0.75)
    q25 = g.rolling(126, min_periods=63).quantile(0.25)
    base = q75 - q25
    deriv = base - base.shift(42)
    result = deriv.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_giqr_252d_slope_v113_signal(revenue):
    g = _f23_growth(revenue, 21)
    q75 = g.rolling(252, min_periods=126).quantile(0.75)
    q25 = g.rolling(252, min_periods=126).quantile(0.25)
    base = q75 - q25
    deriv = base - base.shift(63)
    sd = deriv.rolling(252, min_periods=126).std()
    result = deriv / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_giqr_504d_slope_v114_signal(revenue):
    g = _f23_growth(revenue, 21)
    q75 = g.rolling(504, min_periods=252).quantile(0.75)
    q25 = g.rolling(504, min_periods=252).quantile(0.25)
    base = q75 - q25
    deriv = base - base.shift(126)
    result = deriv.rolling(504, min_periods=252).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_giqr_315d_slope_v115_signal(revenue):
    g = _f23_growth(revenue, 21)
    q75 = g.rolling(315, min_periods=157).quantile(0.75)
    q25 = g.rolling(315, min_periods=157).quantile(0.25)
    base = q75 - q25
    deriv = base - base.shift(63)
    sc = deriv.abs().rolling(315, min_periods=157).mean()
    result = np.tanh(deriv / sc.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_levrank_63d_slope_v116_signal(revenueusd):
    base = _rank(revenueusd, 63)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_levrank_126d_slope_v117_signal(revenueusd):
    base = _rank(revenueusd, 126)
    deriv = base - base.shift(42)
    result = deriv.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_levrank_252d_slope_v118_signal(revenueusd):
    base = _rank(revenueusd, 252)
    deriv = base - base.shift(63)
    sd = deriv.rolling(252, min_periods=126).std()
    result = deriv / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_levrank_504d_slope_v119_signal(revenueusd):
    base = _rank(revenueusd, 504)
    deriv = base - base.shift(126)
    result = deriv.rolling(504, min_periods=252).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_levrank_315d_slope_v120_signal(revenueusd):
    base = _rank(revenueusd, 315)
    deriv = base - base.shift(63)
    sc = deriv.abs().rolling(315, min_periods=157).mean()
    result = np.tanh(deriv / sc.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gdisp_63d_slope_v121_signal(revenue):
    g1 = _f23_growth(revenue, 21)
    g2 = _f23_growth(revenue, 63)
    g3 = _f23_growth(revenue, 126)
    disp = pd.concat([g1, g2, g3], axis=1).std(axis=1)
    base = disp.rolling(63, min_periods=31).mean()
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gdisp_126d_slope_v122_signal(revenue):
    g1 = _f23_growth(revenue, 21)
    g2 = _f23_growth(revenue, 63)
    g3 = _f23_growth(revenue, 126)
    disp = pd.concat([g1, g2, g3], axis=1).std(axis=1)
    base = disp.rolling(126, min_periods=63).mean()
    deriv = base - base.shift(42)
    result = deriv.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gdisp_252d_slope_v123_signal(revenue):
    g1 = _f23_growth(revenue, 21)
    g2 = _f23_growth(revenue, 63)
    g3 = _f23_growth(revenue, 126)
    disp = pd.concat([g1, g2, g3], axis=1).std(axis=1)
    base = disp.rolling(252, min_periods=126).mean()
    deriv = base - base.shift(63)
    sd = deriv.rolling(252, min_periods=126).std()
    result = deriv / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gdisp_504d_slope_v124_signal(revenue):
    g1 = _f23_growth(revenue, 21)
    g2 = _f23_growth(revenue, 63)
    g3 = _f23_growth(revenue, 126)
    disp = pd.concat([g1, g2, g3], axis=1).std(axis=1)
    base = disp.rolling(504, min_periods=252).mean()
    deriv = base - base.shift(126)
    result = deriv.rolling(504, min_periods=252).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gdisp_315d_slope_v125_signal(revenue):
    g1 = _f23_growth(revenue, 21)
    g2 = _f23_growth(revenue, 63)
    g3 = _f23_growth(revenue, 126)
    disp = pd.concat([g1, g2, g3], axis=1).std(axis=1)
    base = disp.rolling(315, min_periods=157).mean()
    deriv = base - base.shift(63)
    sc = deriv.abs().rolling(315, min_periods=157).mean()
    result = np.tanh(deriv / sc.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gmom_63d_slope_v126_signal(revenueusd):
    g = _f23_growth(revenueusd, 21)
    base = g - g.shift(63)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gmom_126d_slope_v127_signal(revenueusd):
    g = _f23_growth(revenueusd, 21)
    base = g - g.shift(126)
    deriv = base - base.shift(42)
    result = deriv.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gmom_252d_slope_v128_signal(revenueusd):
    g = _f23_growth(revenueusd, 21)
    base = g - g.shift(252)
    deriv = base - base.shift(63)
    sd = deriv.rolling(252, min_periods=126).std()
    result = deriv / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gmom_504d_slope_v129_signal(revenueusd):
    g = _f23_growth(revenueusd, 21)
    base = g - g.shift(504)
    deriv = base - base.shift(126)
    result = deriv.rolling(504, min_periods=252).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gmom_315d_slope_v130_signal(revenueusd):
    g = _f23_growth(revenueusd, 21)
    base = g - g.shift(315)
    deriv = base - base.shift(63)
    sc = deriv.abs().rolling(315, min_periods=157).mean()
    result = np.tanh(deriv / sc.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_geff_63d_slope_v131_signal(revenue):
    lr = np.log(revenue.replace(0, np.nan))
    net = (lr - lr.shift(63)).abs()
    path = lr.diff(21).abs().rolling(63, min_periods=31).sum()
    base = net / path.replace(0, np.nan)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_geff_126d_slope_v132_signal(revenue):
    lr = np.log(revenue.replace(0, np.nan))
    net = (lr - lr.shift(126)).abs()
    path = lr.diff(21).abs().rolling(126, min_periods=63).sum()
    base = net / path.replace(0, np.nan)
    deriv = base - base.shift(42)
    result = deriv.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_geff_252d_slope_v133_signal(revenue):
    lr = np.log(revenue.replace(0, np.nan))
    net = (lr - lr.shift(252)).abs()
    path = lr.diff(21).abs().rolling(252, min_periods=126).sum()
    base = net / path.replace(0, np.nan)
    deriv = base - base.shift(63)
    sd = deriv.rolling(252, min_periods=126).std()
    result = deriv / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_geff_504d_slope_v134_signal(revenue):
    lr = np.log(revenue.replace(0, np.nan))
    net = (lr - lr.shift(504)).abs()
    path = lr.diff(21).abs().rolling(504, min_periods=252).sum()
    base = net / path.replace(0, np.nan)
    deriv = base - base.shift(126)
    result = deriv.rolling(504, min_periods=252).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_geff_315d_slope_v135_signal(revenue):
    lr = np.log(revenue.replace(0, np.nan))
    net = (lr - lr.shift(315)).abs()
    path = lr.diff(21).abs().rolling(315, min_periods=157).sum()
    base = net / path.replace(0, np.nan)
    deriv = base - base.shift(63)
    sc = deriv.abs().rolling(315, min_periods=157).mean()
    result = np.tanh(deriv / sc.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gtailhi_63d_slope_v136_signal(revenueusd):
    g = _f23_growth(revenueusd, 21)
    base = g.rolling(63, min_periods=31).quantile(0.9)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gtailhi_126d_slope_v137_signal(revenueusd):
    g = _f23_growth(revenueusd, 21)
    base = g.rolling(126, min_periods=63).quantile(0.9)
    deriv = base - base.shift(42)
    result = deriv.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gtailhi_252d_slope_v138_signal(revenueusd):
    g = _f23_growth(revenueusd, 21)
    base = g.rolling(252, min_periods=126).quantile(0.9)
    deriv = base - base.shift(63)
    sd = deriv.rolling(252, min_periods=126).std()
    result = deriv / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gtailhi_504d_slope_v139_signal(revenueusd):
    g = _f23_growth(revenueusd, 21)
    base = g.rolling(504, min_periods=252).quantile(0.9)
    deriv = base - base.shift(126)
    result = deriv.rolling(504, min_periods=252).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gtailhi_315d_slope_v140_signal(revenueusd):
    g = _f23_growth(revenueusd, 21)
    base = g.rolling(315, min_periods=157).quantile(0.9)
    deriv = base - base.shift(63)
    sc = deriv.abs().rolling(315, min_periods=157).mean()
    result = np.tanh(deriv / sc.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gtaillo_63d_slope_v141_signal(revenue):
    g = _f23_growth(revenue, 21)
    base = g.rolling(63, min_periods=31).quantile(0.1)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gtaillo_126d_slope_v142_signal(revenue):
    g = _f23_growth(revenue, 21)
    base = g.rolling(126, min_periods=63).quantile(0.1)
    deriv = base - base.shift(42)
    result = deriv.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gtaillo_252d_slope_v143_signal(revenue):
    g = _f23_growth(revenue, 21)
    base = g.rolling(252, min_periods=126).quantile(0.1)
    deriv = base - base.shift(63)
    sd = deriv.rolling(252, min_periods=126).std()
    result = deriv / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gtaillo_504d_slope_v144_signal(revenue):
    g = _f23_growth(revenue, 21)
    base = g.rolling(504, min_periods=252).quantile(0.1)
    deriv = base - base.shift(126)
    result = deriv.rolling(504, min_periods=252).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_gtaillo_315d_slope_v145_signal(revenue):
    g = _f23_growth(revenue, 21)
    base = g.rolling(315, min_periods=157).quantile(0.1)
    deriv = base - base.shift(63)
    sc = deriv.abs().rolling(315, min_periods=157).mean()
    result = np.tanh(deriv / sc.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_breadthtanh_63d_slope_v146_signal(revenue):
    g1 = _f23_growth(revenue, 21)
    g2 = _f23_growth(revenue, 63)
    g3 = _f23_growth(revenue, 126)
    a = (np.tanh(g1 * 12.0) + np.tanh(g2 * 4.0) + np.tanh(g3 * 2.0)) / 3.0
    base = a.rolling(63, min_periods=31).mean()
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_breadthtanh_126d_slope_v147_signal(revenue):
    g1 = _f23_growth(revenue, 21)
    g2 = _f23_growth(revenue, 63)
    g3 = _f23_growth(revenue, 126)
    a = (np.tanh(g1 * 12.0) + np.tanh(g2 * 4.0) + np.tanh(g3 * 2.0)) / 3.0
    base = a.rolling(126, min_periods=63).mean()
    deriv = base - base.shift(42)
    result = deriv.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_breadthtanh_252d_slope_v148_signal(revenue):
    g1 = _f23_growth(revenue, 21)
    g2 = _f23_growth(revenue, 63)
    g3 = _f23_growth(revenue, 126)
    a = (np.tanh(g1 * 12.0) + np.tanh(g2 * 4.0) + np.tanh(g3 * 2.0)) / 3.0
    base = a.rolling(252, min_periods=126).mean()
    deriv = base - base.shift(63)
    sd = deriv.rolling(252, min_periods=126).std()
    result = deriv / sd.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_breadthtanh_504d_slope_v149_signal(revenue):
    g1 = _f23_growth(revenue, 21)
    g2 = _f23_growth(revenue, 63)
    g3 = _f23_growth(revenue, 126)
    a = (np.tanh(g1 * 12.0) + np.tanh(g2 * 4.0) + np.tanh(g3 * 2.0)) / 3.0
    base = a.rolling(504, min_periods=252).mean()
    deriv = base - base.shift(126)
    result = deriv.rolling(504, min_periods=252).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)

def f23rg_f23_revenue_growth_engine_breadthtanh_315d_slope_v150_signal(revenue):
    g1 = _f23_growth(revenue, 21)
    g2 = _f23_growth(revenue, 63)
    g3 = _f23_growth(revenue, 126)
    a = (np.tanh(g1 * 12.0) + np.tanh(g2 * 4.0) + np.tanh(g3 * 2.0)) / 3.0
    base = a.rolling(315, min_periods=157).mean()
    deriv = base - base.shift(63)
    sc = deriv.abs().rolling(315, min_periods=157).mean()
    result = np.tanh(deriv / sc.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f23rg_f23_revenue_growth_engine_grw_63d_slope_v001_signal,
    f23rg_f23_revenue_growth_engine_grw_126d_slope_v002_signal,
    f23rg_f23_revenue_growth_engine_grw_252d_slope_v003_signal,
    f23rg_f23_revenue_growth_engine_grw_504d_slope_v004_signal,
    f23rg_f23_revenue_growth_engine_grw_315d_slope_v005_signal,
    f23rg_f23_revenue_growth_engine_lgrw_63d_slope_v006_signal,
    f23rg_f23_revenue_growth_engine_lgrw_126d_slope_v007_signal,
    f23rg_f23_revenue_growth_engine_lgrw_252d_slope_v008_signal,
    f23rg_f23_revenue_growth_engine_lgrw_504d_slope_v009_signal,
    f23rg_f23_revenue_growth_engine_lgrw_315d_slope_v010_signal,
    f23rg_f23_revenue_growth_engine_autocorr_63d_slope_v011_signal,
    f23rg_f23_revenue_growth_engine_autocorr_126d_slope_v012_signal,
    f23rg_f23_revenue_growth_engine_autocorr_252d_slope_v013_signal,
    f23rg_f23_revenue_growth_engine_autocorr_504d_slope_v014_signal,
    f23rg_f23_revenue_growth_engine_autocorr_315d_slope_v015_signal,
    f23rg_f23_revenue_growth_engine_levtrend_63d_slope_v016_signal,
    f23rg_f23_revenue_growth_engine_levtrend_126d_slope_v017_signal,
    f23rg_f23_revenue_growth_engine_levtrend_252d_slope_v018_signal,
    f23rg_f23_revenue_growth_engine_levtrend_504d_slope_v019_signal,
    f23rg_f23_revenue_growth_engine_levtrend_315d_slope_v020_signal,
    f23rg_f23_revenue_growth_engine_revhi_63d_slope_v021_signal,
    f23rg_f23_revenue_growth_engine_revhi_126d_slope_v022_signal,
    f23rg_f23_revenue_growth_engine_revhi_252d_slope_v023_signal,
    f23rg_f23_revenue_growth_engine_revhi_504d_slope_v024_signal,
    f23rg_f23_revenue_growth_engine_revhi_315d_slope_v025_signal,
    f23rg_f23_revenue_growth_engine_revlo_63d_slope_v026_signal,
    f23rg_f23_revenue_growth_engine_revlo_126d_slope_v027_signal,
    f23rg_f23_revenue_growth_engine_revlo_252d_slope_v028_signal,
    f23rg_f23_revenue_growth_engine_revlo_504d_slope_v029_signal,
    f23rg_f23_revenue_growth_engine_revlo_315d_slope_v030_signal,
    f23rg_f23_revenue_growth_engine_gstd_63d_slope_v031_signal,
    f23rg_f23_revenue_growth_engine_gstd_126d_slope_v032_signal,
    f23rg_f23_revenue_growth_engine_gstd_252d_slope_v033_signal,
    f23rg_f23_revenue_growth_engine_gstd_504d_slope_v034_signal,
    f23rg_f23_revenue_growth_engine_gstd_315d_slope_v035_signal,
    f23rg_f23_revenue_growth_engine_gz_63d_slope_v036_signal,
    f23rg_f23_revenue_growth_engine_gz_126d_slope_v037_signal,
    f23rg_f23_revenue_growth_engine_gz_252d_slope_v038_signal,
    f23rg_f23_revenue_growth_engine_gz_504d_slope_v039_signal,
    f23rg_f23_revenue_growth_engine_gz_315d_slope_v040_signal,
    f23rg_f23_revenue_growth_engine_grank_63d_slope_v041_signal,
    f23rg_f23_revenue_growth_engine_grank_126d_slope_v042_signal,
    f23rg_f23_revenue_growth_engine_grank_252d_slope_v043_signal,
    f23rg_f23_revenue_growth_engine_grank_504d_slope_v044_signal,
    f23rg_f23_revenue_growth_engine_grank_315d_slope_v045_signal,
    f23rg_f23_revenue_growth_engine_levz_63d_slope_v046_signal,
    f23rg_f23_revenue_growth_engine_levz_126d_slope_v047_signal,
    f23rg_f23_revenue_growth_engine_levz_252d_slope_v048_signal,
    f23rg_f23_revenue_growth_engine_levz_504d_slope_v049_signal,
    f23rg_f23_revenue_growth_engine_levz_315d_slope_v050_signal,
    f23rg_f23_revenue_growth_engine_qdisp_63d_slope_v051_signal,
    f23rg_f23_revenue_growth_engine_qdisp_126d_slope_v052_signal,
    f23rg_f23_revenue_growth_engine_qdisp_252d_slope_v053_signal,
    f23rg_f23_revenue_growth_engine_qdisp_504d_slope_v054_signal,
    f23rg_f23_revenue_growth_engine_qdisp_315d_slope_v055_signal,
    f23rg_f23_revenue_growth_engine_gsharpe_63d_slope_v056_signal,
    f23rg_f23_revenue_growth_engine_gsharpe_126d_slope_v057_signal,
    f23rg_f23_revenue_growth_engine_gsharpe_252d_slope_v058_signal,
    f23rg_f23_revenue_growth_engine_gsharpe_504d_slope_v059_signal,
    f23rg_f23_revenue_growth_engine_gsharpe_315d_slope_v060_signal,
    f23rg_f23_revenue_growth_engine_gmed_63d_slope_v061_signal,
    f23rg_f23_revenue_growth_engine_gmed_126d_slope_v062_signal,
    f23rg_f23_revenue_growth_engine_gmed_252d_slope_v063_signal,
    f23rg_f23_revenue_growth_engine_gmed_504d_slope_v064_signal,
    f23rg_f23_revenue_growth_engine_gmed_315d_slope_v065_signal,
    f23rg_f23_revenue_growth_engine_gpos_63d_slope_v066_signal,
    f23rg_f23_revenue_growth_engine_gpos_126d_slope_v067_signal,
    f23rg_f23_revenue_growth_engine_gpos_252d_slope_v068_signal,
    f23rg_f23_revenue_growth_engine_gpos_504d_slope_v069_signal,
    f23rg_f23_revenue_growth_engine_gpos_315d_slope_v070_signal,
    f23rg_f23_revenue_growth_engine_omega_63d_slope_v071_signal,
    f23rg_f23_revenue_growth_engine_omega_126d_slope_v072_signal,
    f23rg_f23_revenue_growth_engine_omega_252d_slope_v073_signal,
    f23rg_f23_revenue_growth_engine_omega_504d_slope_v074_signal,
    f23rg_f23_revenue_growth_engine_omega_315d_slope_v075_signal,
    f23rg_f23_revenue_growth_engine_seqacc_63d_slope_v076_signal,
    f23rg_f23_revenue_growth_engine_seqacc_126d_slope_v077_signal,
    f23rg_f23_revenue_growth_engine_seqacc_252d_slope_v078_signal,
    f23rg_f23_revenue_growth_engine_seqacc_504d_slope_v079_signal,
    f23rg_f23_revenue_growth_engine_seqacc_315d_slope_v080_signal,
    f23rg_f23_revenue_growth_engine_gsignmag_63d_slope_v081_signal,
    f23rg_f23_revenue_growth_engine_gsignmag_126d_slope_v082_signal,
    f23rg_f23_revenue_growth_engine_gsignmag_252d_slope_v083_signal,
    f23rg_f23_revenue_growth_engine_gsignmag_504d_slope_v084_signal,
    f23rg_f23_revenue_growth_engine_gsignmag_315d_slope_v085_signal,
    f23rg_f23_revenue_growth_engine_gexcess_63d_slope_v086_signal,
    f23rg_f23_revenue_growth_engine_gexcess_126d_slope_v087_signal,
    f23rg_f23_revenue_growth_engine_gexcess_252d_slope_v088_signal,
    f23rg_f23_revenue_growth_engine_gexcess_504d_slope_v089_signal,
    f23rg_f23_revenue_growth_engine_gexcess_315d_slope_v090_signal,
    f23rg_f23_revenue_growth_engine_slopelr_63d_slope_v091_signal,
    f23rg_f23_revenue_growth_engine_slopelr_126d_slope_v092_signal,
    f23rg_f23_revenue_growth_engine_slopelr_252d_slope_v093_signal,
    f23rg_f23_revenue_growth_engine_slopelr_504d_slope_v094_signal,
    f23rg_f23_revenue_growth_engine_slopelr_315d_slope_v095_signal,
    f23rg_f23_revenue_growth_engine_gcv_63d_slope_v096_signal,
    f23rg_f23_revenue_growth_engine_gcv_126d_slope_v097_signal,
    f23rg_f23_revenue_growth_engine_gcv_252d_slope_v098_signal,
    f23rg_f23_revenue_growth_engine_gcv_504d_slope_v099_signal,
    f23rg_f23_revenue_growth_engine_gcv_315d_slope_v100_signal,
    f23rg_f23_revenue_growth_engine_gupcap_63d_slope_v101_signal,
    f23rg_f23_revenue_growth_engine_gupcap_126d_slope_v102_signal,
    f23rg_f23_revenue_growth_engine_gupcap_252d_slope_v103_signal,
    f23rg_f23_revenue_growth_engine_gupcap_504d_slope_v104_signal,
    f23rg_f23_revenue_growth_engine_gupcap_315d_slope_v105_signal,
    f23rg_f23_revenue_growth_engine_gdncap_63d_slope_v106_signal,
    f23rg_f23_revenue_growth_engine_gdncap_126d_slope_v107_signal,
    f23rg_f23_revenue_growth_engine_gdncap_252d_slope_v108_signal,
    f23rg_f23_revenue_growth_engine_gdncap_504d_slope_v109_signal,
    f23rg_f23_revenue_growth_engine_gdncap_315d_slope_v110_signal,
    f23rg_f23_revenue_growth_engine_giqr_63d_slope_v111_signal,
    f23rg_f23_revenue_growth_engine_giqr_126d_slope_v112_signal,
    f23rg_f23_revenue_growth_engine_giqr_252d_slope_v113_signal,
    f23rg_f23_revenue_growth_engine_giqr_504d_slope_v114_signal,
    f23rg_f23_revenue_growth_engine_giqr_315d_slope_v115_signal,
    f23rg_f23_revenue_growth_engine_levrank_63d_slope_v116_signal,
    f23rg_f23_revenue_growth_engine_levrank_126d_slope_v117_signal,
    f23rg_f23_revenue_growth_engine_levrank_252d_slope_v118_signal,
    f23rg_f23_revenue_growth_engine_levrank_504d_slope_v119_signal,
    f23rg_f23_revenue_growth_engine_levrank_315d_slope_v120_signal,
    f23rg_f23_revenue_growth_engine_gdisp_63d_slope_v121_signal,
    f23rg_f23_revenue_growth_engine_gdisp_126d_slope_v122_signal,
    f23rg_f23_revenue_growth_engine_gdisp_252d_slope_v123_signal,
    f23rg_f23_revenue_growth_engine_gdisp_504d_slope_v124_signal,
    f23rg_f23_revenue_growth_engine_gdisp_315d_slope_v125_signal,
    f23rg_f23_revenue_growth_engine_gmom_63d_slope_v126_signal,
    f23rg_f23_revenue_growth_engine_gmom_126d_slope_v127_signal,
    f23rg_f23_revenue_growth_engine_gmom_252d_slope_v128_signal,
    f23rg_f23_revenue_growth_engine_gmom_504d_slope_v129_signal,
    f23rg_f23_revenue_growth_engine_gmom_315d_slope_v130_signal,
    f23rg_f23_revenue_growth_engine_geff_63d_slope_v131_signal,
    f23rg_f23_revenue_growth_engine_geff_126d_slope_v132_signal,
    f23rg_f23_revenue_growth_engine_geff_252d_slope_v133_signal,
    f23rg_f23_revenue_growth_engine_geff_504d_slope_v134_signal,
    f23rg_f23_revenue_growth_engine_geff_315d_slope_v135_signal,
    f23rg_f23_revenue_growth_engine_gtailhi_63d_slope_v136_signal,
    f23rg_f23_revenue_growth_engine_gtailhi_126d_slope_v137_signal,
    f23rg_f23_revenue_growth_engine_gtailhi_252d_slope_v138_signal,
    f23rg_f23_revenue_growth_engine_gtailhi_504d_slope_v139_signal,
    f23rg_f23_revenue_growth_engine_gtailhi_315d_slope_v140_signal,
    f23rg_f23_revenue_growth_engine_gtaillo_63d_slope_v141_signal,
    f23rg_f23_revenue_growth_engine_gtaillo_126d_slope_v142_signal,
    f23rg_f23_revenue_growth_engine_gtaillo_252d_slope_v143_signal,
    f23rg_f23_revenue_growth_engine_gtaillo_504d_slope_v144_signal,
    f23rg_f23_revenue_growth_engine_gtaillo_315d_slope_v145_signal,
    f23rg_f23_revenue_growth_engine_breadthtanh_63d_slope_v146_signal,
    f23rg_f23_revenue_growth_engine_breadthtanh_126d_slope_v147_signal,
    f23rg_f23_revenue_growth_engine_breadthtanh_252d_slope_v148_signal,
    f23rg_f23_revenue_growth_engine_breadthtanh_504d_slope_v149_signal,
    f23rg_f23_revenue_growth_engine_breadthtanh_315d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F23_REVENUE_GROWTH_ENGINE_REGISTRY_001_150 = REGISTRY


def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False, n=1500):
    g = np.random.default_rng(seed)
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.3
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    revenue = _fund(101, base=8e7, drift=0.025, vol=0.06, n=n).rename("revenue")
    revenueusd = _fund(102, base=1.0e8, drift=0.022, vol=0.07, n=n).rename("revenueusd")

    cols = {"revenue": revenue, "revenueusd": revenueusd}

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

    assert n_features == 150, n_features
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

    print("OK f23_revenue_growth_engine_2nd_derivatives_001_150_claude: %d features pass" % n_features)
