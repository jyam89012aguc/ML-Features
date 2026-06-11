import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
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


# ===== folder domain primitives (revenue growth engine) =====
def _f18_growth(s, w):
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _f18_loggrowth(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _f18_cagr(s, w, periods_per_year=252.0):
    r = s / s.shift(w).replace(0, np.nan)
    expo = periods_per_year / float(w)
    return np.power(r.clip(lower=1e-9), expo) - 1.0


def _f18_seq_growth(s, w):
    g = s / s.shift(w).replace(0, np.nan) - 1.0
    return g


def _f18_growth_accel(s, w):
    g = s / s.shift(w).replace(0, np.nan) - 1.0
    return g - g.shift(w)


def _f18_growth_stability(s, w):
    dl = np.log(s.replace(0, np.nan)).diff()
    m = dl.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = dl.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan)


# jerk (roc=10d) of base revg_21d
def f18rg_f18_revenue_growth_engine_revg_21d_jerk_v001_signal(revenue):
    b = _f18_growth(revenue, 21)
    _d1 = (b - b.shift(10)) / 10.0
    result = (_d1 - _d1.shift(10)) / 10.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=21d) of base revg_63d
def f18rg_f18_revenue_growth_engine_revg_63d_jerk_v002_signal(revenue):
    b = _f18_growth(revenue, 63)
    _d1 = (b - b.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=42d) of base revg_126d
def f18rg_f18_revenue_growth_engine_revg_126d_jerk_v003_signal(revenue):
    b = _f18_growth(revenue, 126)
    _d1 = (b - b.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base revg_252d
def f18rg_f18_revenue_growth_engine_revg_252d_jerk_v004_signal(revenue):
    b = _f18_growth(revenue, 252)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=126d) of base revg_504d
def f18rg_f18_revenue_growth_engine_revg_504d_jerk_v005_signal(revenue):
    b = _f18_growth(revenue, 504)
    _d1 = (b - b.shift(126)) / 126.0
    result = (_d1 - _d1.shift(126)) / 126.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=21d) of base revusdg_63d
def f18rg_f18_revenue_growth_engine_revusdg_63d_jerk_v006_signal(revenueusd):
    b = _f18_growth(revenueusd, 63)
    _d1 = (b - b.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base revusdg_252d
def f18rg_f18_revenue_growth_engine_revusdg_252d_jerk_v007_signal(revenueusd):
    b = _f18_growth(revenueusd, 252)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gpg_252d
def f18rg_f18_revenue_growth_engine_gpg_252d_jerk_v008_signal(gp):
    b = _f18_growth(gp, 252)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=21d) of base gpg_63d
def f18rg_f18_revenue_growth_engine_gpg_63d_jerk_v009_signal(gp):
    b = _f18_growth(gp, 63)
    _d1 = (b - b.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=42d) of base gpg_126d
def f18rg_f18_revenue_growth_engine_gpg_126d_jerk_v010_signal(gp):
    b = _f18_growth(gp, 126)
    _d1 = (b - b.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base revlg_252d
def f18rg_f18_revenue_growth_engine_revlg_252d_jerk_v011_signal(revenue):
    lg = _f18_loggrowth(revenue, 252)
    b = lg - lg.rolling(252, min_periods=126).mean()
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=42d) of base revlg_126d
def f18rg_f18_revenue_growth_engine_revlg_126d_jerk_v012_signal(revenue):
    lg = _f18_loggrowth(revenue, 126)
    b = lg - lg.rolling(126, min_periods=63).mean()
    _d1 = (b - b.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base cagr_252d
def f18rg_f18_revenue_growth_engine_cagr_252d_jerk_v013_signal(revenue):
    c = _f18_cagr(revenue, 252)
    b = c - c.shift(63)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=126d) of base cagr_504d
def f18rg_f18_revenue_growth_engine_cagr_504d_jerk_v014_signal(revenue):
    c = _f18_cagr(revenue, 504)
    b = _rank(c, 504)
    _d1 = (b - b.shift(126)) / 126.0
    result = (_d1 - _d1.shift(126)) / 126.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=42d) of base cagr_126d
def f18rg_f18_revenue_growth_engine_cagr_126d_jerk_v015_signal(revenue):
    c = _f18_cagr(revenue, 126)
    b = _rank(c, 504)
    _d1 = (b - b.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base cagrusd_252d
def f18rg_f18_revenue_growth_engine_cagrusd_252d_jerk_v016_signal(revenueusd):
    c = _f18_cagr(revenueusd, 252)
    b = c - c.shift(63)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base cagrgp_252d
def f18rg_f18_revenue_growth_engine_cagrgp_252d_jerk_v017_signal(gp):
    c = _f18_cagr(gp, 252)
    b = _z(c, 504)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=21d) of base seqg_63d
def f18rg_f18_revenue_growth_engine_seqg_63d_jerk_v018_signal(revenue):
    g = _f18_seq_growth(revenue, 63)
    b = _rank(g, 252)
    _d1 = (b - b.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=10d) of base seqg_21d
def f18rg_f18_revenue_growth_engine_seqg_21d_jerk_v019_signal(revenue):
    g = _f18_seq_growth(revenue, 21)
    b = g.rolling(21, min_periods=10).mean() - g.rolling(63, min_periods=21).mean()
    _d1 = (b - b.shift(10)) / 10.0
    result = (_d1 - _d1.shift(10)) / 10.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=21d) of base seqgpg_63d
def f18rg_f18_revenue_growth_engine_seqgpg_63d_jerk_v020_signal(gp):
    g = _f18_seq_growth(gp, 126)
    b = g - g.rolling(252, min_periods=126).mean()
    _d1 = (b - b.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=21d) of base accel_63d
def f18rg_f18_revenue_growth_engine_accel_63d_jerk_v021_signal(revenue):
    b = _f18_growth_accel(revenue, 63)
    _d1 = (b - b.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=42d) of base accel_126d
def f18rg_f18_revenue_growth_engine_accel_126d_jerk_v022_signal(revenue):
    b = _f18_growth_accel(revenue, 126)
    _d1 = (b - b.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base accel_252d
def f18rg_f18_revenue_growth_engine_accel_252d_jerk_v023_signal(revenue):
    b = _f18_growth_accel(revenue, 252)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=21d) of base accelgp_63d
def f18rg_f18_revenue_growth_engine_accelgp_63d_jerk_v024_signal(gp):
    b = _f18_growth_accel(gp, 63)
    _d1 = (b - b.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base stab_252d
def f18rg_f18_revenue_growth_engine_stab_252d_jerk_v025_signal(revenue):
    s = _f18_growth_stability(revenue, 252)
    b = s - s.rolling(252, min_periods=126).mean()
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=42d) of base stab_126d
def f18rg_f18_revenue_growth_engine_stab_126d_jerk_v026_signal(revenue):
    b = _f18_growth_stability(revenue, 126)
    _d1 = (b - b.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base stabgp_252d
def f18rg_f18_revenue_growth_engine_stabgp_252d_jerk_v027_signal(gp):
    b = _f18_growth_stability(gp, 252)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=21d) of base grank_63d
def f18rg_f18_revenue_growth_engine_grank_63d_jerk_v028_signal(revenue):
    g = _f18_growth(revenue, 63)
    b = _rank(g, 504)
    _d1 = (b - b.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base grank_252d
def f18rg_f18_revenue_growth_engine_grank_252d_jerk_v029_signal(revenue):
    g = _f18_growth(revenue, 252)
    b = _rank(g, 504)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base grankgp_252d
def f18rg_f18_revenue_growth_engine_grankgp_252d_jerk_v030_signal(gp):
    g = _f18_growth(gp, 252)
    b = _rank(g, 504)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=21d) of base gz_63d
def f18rg_f18_revenue_growth_engine_gz_63d_jerk_v031_signal(revenue):
    g = _f18_growth(revenue, 63)
    b = _z(g, 252)
    _d1 = (b - b.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=42d) of base gz_126d
def f18rg_f18_revenue_growth_engine_gz_126d_jerk_v032_signal(revenue):
    g = _f18_growth(revenue, 126)
    b = _z(g, 252)
    _d1 = (b - b.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=42d) of base gzgp_126d
def f18rg_f18_revenue_growth_engine_gzgp_126d_jerk_v033_signal(gp):
    g = _f18_growth(gp, 126)
    b = _z(g, 252)
    _d1 = (b - b.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gqspr_252d
def f18rg_f18_revenue_growth_engine_gqspr_252d_jerk_v034_signal(gp, revenue):
    gg = _f18_growth(gp, 252)
    rg = _f18_growth(revenue, 252)
    b = gg - rg
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=21d) of base gqspr_63d
def f18rg_f18_revenue_growth_engine_gqspr_63d_jerk_v035_signal(gp, revenue):
    gg = _f18_growth(gp, 63)
    rg = _f18_growth(revenue, 63)
    b = gg - rg
    _d1 = (b - b.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gterm_63v252
def f18rg_f18_revenue_growth_engine_gterm_63v252_jerk_v036_signal(revenue):
    s = _f18_growth(revenue, 63)
    l = _f18_growth(revenue, 252)
    b = s - l
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gtermr_126v252
def f18rg_f18_revenue_growth_engine_gtermr_126v252_jerk_v037_signal(revenue):
    s = _f18_growth(revenue, 126)
    l = _f18_growth(revenue, 252)
    b = s / l.replace(0, np.nan)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base fxdiv_252d
def f18rg_f18_revenue_growth_engine_fxdiv_252d_jerk_v038_signal(revenueusd, revenue):
    gu = _f18_growth(revenueusd, 252)
    gr = _f18_growth(revenue, 252)
    b = gu - gr
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gdisp_252d
def f18rg_f18_revenue_growth_engine_gdisp_252d_jerk_v039_signal(revenue):
    g = _f18_growth(revenue, 63)
    b = _std(g, 252)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=42d) of base gdisp_126d
def f18rg_f18_revenue_growth_engine_gdisp_126d_jerk_v040_signal(revenue):
    g = _f18_growth(revenue, 21)
    b = _std(g, 126)
    _d1 = (b - b.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=21d) of base gema_63d
def f18rg_f18_revenue_growth_engine_gema_63d_jerk_v041_signal(revenue):
    g = _f18_growth(revenue, 63)
    b = g.ewm(span=63, min_periods=21).mean()
    _d1 = (b - b.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gdisp_ema
def f18rg_f18_revenue_growth_engine_gdisp_ema_jerk_v042_signal(revenue):
    g = _f18_growth(revenue, 63)
    b = g - g.ewm(span=126, min_periods=42).mean()
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base cagrspr
def f18rg_f18_revenue_growth_engine_cagrspr_jerk_v043_signal(revenue):
    s = _f18_cagr(revenue, 126)
    l = _f18_cagr(revenue, 504)
    b = s - l
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base cagrgpspr
def f18rg_f18_revenue_growth_engine_cagrgpspr_jerk_v044_signal(gp):
    s = _f18_cagr(gp, 126)
    l = _f18_cagr(gp, 504)
    b = s - l
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base radjg_252d
def f18rg_f18_revenue_growth_engine_radjg_252d_jerk_v045_signal(revenue):
    g = _f18_growth(revenue, 252)
    disp = _std(_f18_growth(revenue, 63), 252)
    b = g / disp.replace(0, np.nan)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gsignmag_252d
def f18rg_f18_revenue_growth_engine_gsignmag_252d_jerk_v046_signal(revenue):
    g = _f18_growth(revenue, 252)
    b = np.sign(g) * (g.abs() ** 0.5)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=21d) of base gtanh_63d
def f18rg_f18_revenue_growth_engine_gtanh_63d_jerk_v047_signal(revenue):
    g = _f18_growth(revenue, 63)
    med = g.rolling(252, min_periods=126).median()
    b = np.tanh(8.0 * (g - med))
    _d1 = (b - b.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=21d) of base accelusd_63d
def f18rg_f18_revenue_growth_engine_accelusd_63d_jerk_v048_signal(revenueusd):
    b = _f18_growth_accel(revenueusd, 63)
    _d1 = (b - b.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gconsist_252d
def f18rg_f18_revenue_growth_engine_gconsist_252d_jerk_v049_signal(revenue):
    g = _f18_growth(revenue, 21)
    pos = (g > 0).astype(float)
    b = pos.rolling(252, min_periods=126).mean()
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gpconsist_252d
def f18rg_f18_revenue_growth_engine_gpconsist_252d_jerk_v050_signal(gp):
    g = _f18_growth(gp, 63)
    pos = (g > 0).astype(float)
    b = pos.rolling(252, min_periods=126).mean()
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gbreadth
def f18rg_f18_revenue_growth_engine_gbreadth_jerk_v051_signal(revenue):
    g = _f18_growth(revenue, 63)
    consist = (g > 0).astype(float).rolling(252, min_periods=126).mean()
    b = g * consist
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base lglvl_252d
def f18rg_f18_revenue_growth_engine_lglvl_252d_jerk_v052_signal(revenue):
    lg = np.log(revenue.replace(0, np.nan))
    hi = lg.rolling(504, min_periods=252).max()
    lo = lg.rolling(504, min_periods=252).min()
    b = (lg - lo) / (hi - lo).replace(0, np.nan)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=42d) of base grankusd_126d
def f18rg_f18_revenue_growth_engine_grankusd_126d_jerk_v053_signal(revenueusd):
    g = _f18_growth(revenueusd, 126)
    b = _rank(g, 504)
    _d1 = (b - b.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=21d) of base accrank_63d
def f18rg_f18_revenue_growth_engine_accrank_63d_jerk_v054_signal(revenue):
    a = _f18_growth_accel(revenue, 63)
    b = _rank(a, 504)
    _d1 = (b - b.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base compgap
def f18rg_f18_revenue_growth_engine_compgap_jerk_v055_signal(gp, revenue):
    cg = (gp / gp.shift(126).replace(0, np.nan))
    cr = (revenue / revenue.shift(126).replace(0, np.nan))
    b = cg / cr.replace(0, np.nan) - 1.0
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=42d) of base gpleverage_126d
def f18rg_f18_revenue_growth_engine_gpleverage_126d_jerk_v056_signal(gp, revenue):
    gg = _f18_growth(gp, 126)
    rg = _f18_growth(revenue, 126)
    b = gg / rg.replace(0, np.nan)
    _d1 = (b - b.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gzspr
def f18rg_f18_revenue_growth_engine_gzspr_jerk_v057_signal(revenue, gp):
    rz = _z(_f18_growth(revenue, 63), 252)
    gz = _z(_f18_growth(gp, 63), 252)
    b = rz - gz
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gdd_252d
def f18rg_f18_revenue_growth_engine_gdd_252d_jerk_v058_signal(revenue):
    g = _f18_growth(revenue, 63)
    peak = g.rolling(252, min_periods=126).max()
    b = g - peak
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base grec_252d
def f18rg_f18_revenue_growth_engine_grec_252d_jerk_v059_signal(revenue):
    g = _f18_growth(revenue, 63)
    trough = g.rolling(252, min_periods=126).min()
    b = g - trough
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gpos_252d
def f18rg_f18_revenue_growth_engine_gpos_252d_jerk_v060_signal(revenue):
    g = _f18_growth(revenue, 63)
    hi = g.rolling(252, min_periods=126).max()
    lo = g.rolling(252, min_periods=126).min()
    b = (g - lo) / (hi - lo).replace(0, np.nan)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base stabusd_252d
def f18rg_f18_revenue_growth_engine_stabusd_252d_jerk_v061_signal(revenueusd):
    b = _f18_growth_stability(revenueusd, 252)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=42d) of base g2_126d
def f18rg_f18_revenue_growth_engine_g2_126d_jerk_v062_signal(revenue):
    g = _f18_growth(revenue, 126)
    b = (g - g.shift(63)).ewm(span=42, min_periods=21).mean()
    _d1 = (b - b.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=42d) of base gpmom_126d
def f18rg_f18_revenue_growth_engine_gpmom_126d_jerk_v063_signal(gp):
    g = _f18_growth(gp, 126)
    b = g - g.shift(63)
    _d1 = (b - b.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base lvlmean_252d
def f18rg_f18_revenue_growth_engine_lvlmean_252d_jerk_v064_signal(revenue):
    b = revenue / _mean(revenue, 252).replace(0, np.nan) - 1.0
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gplvlmean_252d
def f18rg_f18_revenue_growth_engine_gplvlmean_252d_jerk_v065_signal(gp):
    b = gp / _mean(gp, 252).replace(0, np.nan) - 1.0
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gyoy2
def f18rg_f18_revenue_growth_engine_gyoy2_jerk_v066_signal(revenue):
    g = _f18_growth(revenue, 252)
    b = _std(g, 504)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=42d) of base ginteract_126d
def f18rg_f18_revenue_growth_engine_ginteract_126d_jerk_v067_signal(revenue, gp):
    rg = _f18_growth(revenue, 126)
    gg = _f18_growth(gp, 126)
    b = np.sign(rg) * np.sqrt((rg.abs() * gg.abs()).clip(lower=0))
    _d1 = (b - b.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gstreak
def f18rg_f18_revenue_growth_engine_gstreak_jerk_v068_signal(revenue):
    g = _f18_growth(revenue, 21)
    pos = (g > 0).astype(float)
    grp = (pos != pos.shift(1)).cumsum()
    streak = pos.groupby(grp).cumsum()
    b = (streak * pos).clip(upper=126) / 126.0
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base cagradj_252d
def f18rg_f18_revenue_growth_engine_cagradj_252d_jerk_v069_signal(revenue):
    c = _f18_cagr(revenue, 504)
    disp = _std(_f18_growth(revenue, 21), 126)
    b = c / disp.replace(0, np.nan)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gpranktilt
def f18rg_f18_revenue_growth_engine_gpranktilt_jerk_v070_signal(gp):
    g = _f18_growth(gp, 126)
    r = _rank(g, 504)
    b = r * np.sign(g)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gmultidisp
def f18rg_f18_revenue_growth_engine_gmultidisp_jerk_v071_signal(revenue):
    g1 = _f18_growth(revenue, 63)
    g2 = _f18_growth(revenue, 126)
    g3 = _f18_growth(revenue, 252)
    b = pd.concat([g1, g2, g3], axis=1).std(axis=1)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gmultispr
def f18rg_f18_revenue_growth_engine_gmultispr_jerk_v072_signal(revenue):
    near = (1.0 + _f18_growth(revenue, 126)).clip(lower=1e-9) ** 2 - 1.0
    longp = _f18_cagr(revenue, 504)
    b = _rank(near - longp, 252)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=126d) of base cagrusdadj_504d
def f18rg_f18_revenue_growth_engine_cagrusdadj_504d_jerk_v073_signal(revenueusd):
    c = _f18_cagr(revenueusd, 504)
    disp = _std(_f18_growth(revenueusd, 63), 252)
    b = c / disp.replace(0, np.nan)
    _d1 = (b - b.shift(126)) / 126.0
    result = (_d1 - _d1.shift(126)) / 126.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=42d) of base accelsm_126d
def f18rg_f18_revenue_growth_engine_accelsm_126d_jerk_v074_signal(gp):
    a = _f18_growth_accel(gp, 126)
    b = np.sign(a) * (a.abs() ** 0.5)
    _d1 = (b - b.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base durable
def f18rg_f18_revenue_growth_engine_durable_jerk_v075_signal(revenue):
    stab = _f18_growth_stability(revenue, 252)
    rnk = _rank(_f18_growth(revenue, 252), 504)
    b = np.tanh(stab) * rnk
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=10d) of base gz_21d
def f18rg_f18_revenue_growth_engine_gz_21d_jerk_v076_signal(revenue):
    g = _f18_growth(revenue, 21)
    b = _z(g, 126)
    _d1 = (b - b.shift(10)) / 10.0
    result = (_d1 - _d1.shift(10)) / 10.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=10d) of base grank_21d
def f18rg_f18_revenue_growth_engine_grank_21d_jerk_v077_signal(revenue):
    g = _f18_growth(revenue, 21)
    b = _rank(g, 252)
    _d1 = (b - b.shift(10)) / 10.0
    result = (_d1 - _d1.shift(10)) / 10.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=21d) of base gzusd_63d
def f18rg_f18_revenue_growth_engine_gzusd_63d_jerk_v078_signal(revenueusd):
    g = _f18_growth(revenueusd, 63)
    b = _z(g, 252)
    _d1 = (b - b.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=21d) of base grankgp_63d
def f18rg_f18_revenue_growth_engine_grankgp_63d_jerk_v079_signal(gp):
    g = _f18_growth(gp, 63)
    b = _rank(g, 504)
    _d1 = (b - b.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=42d) of base accelusd_126d
def f18rg_f18_revenue_growth_engine_accelusd_126d_jerk_v080_signal(revenueusd):
    b = _f18_growth_accel(revenueusd, 126)
    _d1 = (b - b.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=42d) of base accelgp_126d
def f18rg_f18_revenue_growth_engine_accelgp_126d_jerk_v081_signal(gp):
    b = _f18_growth_accel(gp, 126)
    _d1 = (b - b.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base accelgp_252d
def f18rg_f18_revenue_growth_engine_accelgp_252d_jerk_v082_signal(gp):
    b = _f18_growth_accel(gp, 252)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gdispusd_252d
def f18rg_f18_revenue_growth_engine_gdispusd_252d_jerk_v083_signal(revenueusd):
    g = _f18_growth(revenueusd, 63)
    b = _std(g, 252)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gdispgp_252d
def f18rg_f18_revenue_growth_engine_gdispgp_252d_jerk_v084_signal(gp):
    g = _f18_growth(gp, 63)
    b = _std(g, 252)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base revcv_252d
def f18rg_f18_revenue_growth_engine_revcv_252d_jerk_v085_signal(revenue):
    b = _std(revenue, 252) / _mean(revenue, 252).replace(0, np.nan)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gpcv_252d
def f18rg_f18_revenue_growth_engine_gpcv_252d_jerk_v086_signal(gp):
    b = _std(gp, 252) / _mean(gp, 252).replace(0, np.nan)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=42d) of base lvlmean_126d
def f18rg_f18_revenue_growth_engine_lvlmean_126d_jerk_v087_signal(revenue):
    b = revenue / _mean(revenue, 126).replace(0, np.nan) - 1.0
    _d1 = (b - b.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base lvlmeanusd_252d
def f18rg_f18_revenue_growth_engine_lvlmeanusd_252d_jerk_v088_signal(revenueusd):
    b = revenueusd / _mean(revenueusd, 252).replace(0, np.nan) - 1.0
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base lvlpos_252d
def f18rg_f18_revenue_growth_engine_lvlpos_252d_jerk_v089_signal(revenue):
    hi = revenue.rolling(252, min_periods=126).max()
    lo = revenue.rolling(252, min_periods=126).min()
    b = (revenue - lo) / (hi - lo).replace(0, np.nan)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gplvlpos_252d
def f18rg_f18_revenue_growth_engine_gplvlpos_252d_jerk_v090_signal(gp):
    hi = gp.rolling(252, min_periods=126).max()
    lo = gp.rolling(252, min_periods=126).min()
    b = (gp - lo) / (hi - lo).replace(0, np.nan)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base newhi_252d
def f18rg_f18_revenue_growth_engine_newhi_252d_jerk_v091_signal(revenue):
    hi = revenue.rolling(252, min_periods=126).max()
    is_hi = (revenue >= hi * 0.99999).astype(float)
    b = is_hi.rolling(63, min_periods=21).mean()
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base dsrh_252d
def f18rg_f18_revenue_growth_engine_dsrh_252d_jerk_v092_signal(revenue):
    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    b = revenue.rolling(252, min_periods=126).apply(_f, raw=True)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base revdd_252d
def f18rg_f18_revenue_growth_engine_revdd_252d_jerk_v093_signal(revenue):
    peak = revenue.rolling(252, min_periods=126).max()
    b = revenue / peak.replace(0, np.nan) - 1.0
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gpdd_252d
def f18rg_f18_revenue_growth_engine_gpdd_252d_jerk_v094_signal(gp):
    peak = gp.rolling(252, min_periods=126).max()
    b = gp / peak.replace(0, np.nan) - 1.0
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base revrec_252d
def f18rg_f18_revenue_growth_engine_revrec_252d_jerk_v095_signal(revenue):
    trough = revenue.rolling(252, min_periods=126).min()
    b = revenue / trough.replace(0, np.nan) - 1.0
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=42d) of base accrank_126d
def f18rg_f18_revenue_growth_engine_accrank_126d_jerk_v096_signal(revenue):
    a = _f18_growth_accel(revenue, 126)
    b = _rank(a, 504)
    _d1 = (b - b.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base accz_252d
def f18rg_f18_revenue_growth_engine_accz_252d_jerk_v097_signal(revenue):
    a = _f18_growth_accel(revenue, 252)
    b = _z(a, 504)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base fxlvl
def f18rg_f18_revenue_growth_engine_fxlvl_jerk_v098_signal(revenueusd, revenue):
    b = revenueusd / revenue.replace(0, np.nan) - 1.0
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=21d) of base fxmom_63d
def f18rg_f18_revenue_growth_engine_fxmom_63d_jerk_v099_signal(revenueusd, revenue):
    ratio = revenueusd / revenue.replace(0, np.nan)
    b = ratio / ratio.shift(63).replace(0, np.nan) - 1.0
    _d1 = (b - b.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gpmargin
def f18rg_f18_revenue_growth_engine_gpmargin_jerk_v100_signal(gp, revenue):
    b = gp / revenue.replace(0, np.nan)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=42d) of base gpmargmom_126d
def f18rg_f18_revenue_growth_engine_gpmargmom_126d_jerk_v101_signal(gp, revenue):
    m = gp / revenue.replace(0, np.nan)
    b = m - m.shift(126)
    _d1 = (b - b.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gpmargz_252d
def f18rg_f18_revenue_growth_engine_gpmargz_252d_jerk_v102_signal(gp, revenue):
    m = gp / revenue.replace(0, np.nan)
    b = _z(m, 252)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=21d) of base gqual_63d
def f18rg_f18_revenue_growth_engine_gqual_63d_jerk_v103_signal(revenue, gp):
    g = _f18_growth(revenue, 126)
    m = gp / revenue.replace(0, np.nan)
    b = g * _z(m, 252)
    _d1 = (b - b.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=126d) of base poscount_504d
def f18rg_f18_revenue_growth_engine_poscount_504d_jerk_v104_signal(revenue):
    g = _f18_growth(revenue, 63)
    pos = (g > 0).astype(float)
    b = pos.rolling(504, min_periods=252).sum() / 504.0
    _d1 = (b - b.shift(126)) / 126.0
    result = (_d1 - _d1.shift(126)) / 126.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base accpos_252d
def f18rg_f18_revenue_growth_engine_accpos_252d_jerk_v105_signal(revenue):
    a = _f18_growth_accel(revenue, 63)
    pos = (a > 0).astype(float)
    b = pos.rolling(252, min_periods=126).mean()
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gskew_252d
def f18rg_f18_revenue_growth_engine_gskew_252d_jerk_v106_signal(revenue):
    g = _f18_growth(revenue, 21)
    m = g.rolling(252, min_periods=126).mean()
    med = g.rolling(252, min_periods=126).median()
    b = (m - med) / _std(g, 252).replace(0, np.nan)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gpskew_252d
def f18rg_f18_revenue_growth_engine_gpskew_252d_jerk_v107_signal(gp):
    g = _f18_growth(gp, 21)
    m = g.rolling(252, min_periods=126).mean()
    med = g.rolling(252, min_periods=126).median()
    b = (m - med) / _std(g, 252).replace(0, np.nan)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gupsemi_252d
def f18rg_f18_revenue_growth_engine_gupsemi_252d_jerk_v108_signal(revenue):
    g = _f18_growth(revenue, 21)
    m = g.rolling(252, min_periods=126).mean()
    dev = (g - m).clip(lower=0)
    b = (dev ** 2).rolling(252, min_periods=126).mean() ** 0.5
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gdnsemi_252d
def f18rg_f18_revenue_growth_engine_gdnsemi_252d_jerk_v109_signal(revenue):
    g = _f18_growth(revenue, 21)
    m = g.rolling(252, min_periods=126).mean()
    dev = (g - m).clip(upper=0)
    b = (dev ** 2).rolling(252, min_periods=126).mean() ** 0.5
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gsemiskew_252d
def f18rg_f18_revenue_growth_engine_gsemiskew_252d_jerk_v110_signal(revenue):
    g = _f18_growth(revenue, 21)
    m = g.rolling(252, min_periods=126).mean()
    up = ((g - m).clip(lower=0) ** 2).rolling(252, min_periods=126).mean() ** 0.5
    dn = ((g - m).clip(upper=0) ** 2).rolling(252, min_periods=126).mean() ** 0.5
    b = up - dn
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gvov
def f18rg_f18_revenue_growth_engine_gvov_jerk_v111_signal(revenue):
    g = _f18_growth(revenue, 21)
    disp = _std(g, 63)
    b = _std(disp, 126)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base geff_252d
def f18rg_f18_revenue_growth_engine_geff_252d_jerk_v112_signal(revenue):
    net = (revenue - revenue.shift(252)).abs()
    path = (revenue - revenue.shift(21)).abs().rolling(252, min_periods=126).sum()
    b = net / path.replace(0, np.nan)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gpeff_252d
def f18rg_f18_revenue_growth_engine_gpeff_252d_jerk_v113_signal(gp):
    net = (gp - gp.shift(252)).abs()
    path = (gp - gp.shift(21)).abs().rolling(252, min_periods=126).sum()
    b = net / path.replace(0, np.nan)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gautoc_252d
def f18rg_f18_revenue_growth_engine_gautoc_252d_jerk_v114_signal(revenue):
    g = _f18_growth(revenue, 21)
    b = g.rolling(252, min_periods=126).corr(g.shift(21))
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base revgpcorr_252d
def f18rg_f18_revenue_growth_engine_revgpcorr_252d_jerk_v115_signal(revenue, gp):
    gr = _f18_growth(revenue, 21)
    gg = _f18_growth(gp, 21)
    b = gr.rolling(252, min_periods=126).corr(gg)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gtermr_21v252
def f18rg_f18_revenue_growth_engine_gtermr_21v252_jerk_v116_signal(revenue):
    near = (1.0 + _f18_growth(revenue, 21)).clip(lower=1e-9) ** 12 - 1.0
    longg = _f18_growth(revenue, 252)
    b = near - longg
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gtermusd
def f18rg_f18_revenue_growth_engine_gtermusd_jerk_v117_signal(revenueusd):
    s = _f18_growth(revenueusd, 63)
    l = _f18_growth(revenueusd, 252)
    b = s - l
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gtermgp
def f18rg_f18_revenue_growth_engine_gtermgp_jerk_v118_signal(gp):
    s = _f18_growth(gp, 63)
    l = _f18_growth(gp, 252)
    b = s - l
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=42d) of base gema_126d
def f18rg_f18_revenue_growth_engine_gema_126d_jerk_v119_signal(revenue):
    g = _f18_growth(revenue, 126)
    b = g.ewm(span=42, min_periods=21).mean()
    _d1 = (b - b.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gpemadisp
def f18rg_f18_revenue_growth_engine_gpemadisp_jerk_v120_signal(gp):
    g = _f18_growth(gp, 63)
    b = g - g.ewm(span=126, min_periods=42).mean()
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=21d) of base gztanh_63d
def f18rg_f18_revenue_growth_engine_gztanh_63d_jerk_v121_signal(revenue):
    z = _z(_f18_growth(revenue, 63), 252)
    b = np.tanh(z)
    _d1 = (b - b.shift(21)) / 21.0
    result = (_d1 - _d1.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=42d) of base gsignmag_126d
def f18rg_f18_revenue_growth_engine_gsignmag_126d_jerk_v122_signal(revenue):
    g = _f18_growth(revenue, 126)
    b = np.sign(g) * (g.abs() ** 0.5)
    _d1 = (b - b.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gsignmagusd_252d
def f18rg_f18_revenue_growth_engine_gsignmagusd_252d_jerk_v123_signal(revenueusd):
    g = _f18_growth(revenueusd, 252)
    b = np.sign(g) * (g.abs() ** 0.5)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base radjgp_252d
def f18rg_f18_revenue_growth_engine_radjgp_252d_jerk_v124_signal(gp):
    g = _f18_growth(gp, 252)
    disp = _std(_f18_growth(gp, 63), 252)
    b = g / disp.replace(0, np.nan)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base radjusd_252d
def f18rg_f18_revenue_growth_engine_radjusd_252d_jerk_v125_signal(revenueusd):
    g = _f18_growth(revenueusd, 252)
    disp = _std(_f18_growth(revenueusd, 63), 252)
    b = g / disp.replace(0, np.nan)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gqsprusdgp
def f18rg_f18_revenue_growth_engine_gqsprusdgp_jerk_v126_signal(revenueusd, gp):
    gu = _f18_growth(revenueusd, 126)
    gg = _f18_growth(gp, 126)
    b = gg - gu
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gconcav
def f18rg_f18_revenue_growth_engine_gconcav_jerk_v127_signal(revenue):
    g63 = _f18_growth(revenue, 63)
    g126 = _f18_growth(revenue, 126)
    b = (1.0 + g126) - (1.0 + g63) ** 2
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gpconcav
def f18rg_f18_revenue_growth_engine_gpconcav_jerk_v128_signal(gp):
    g63 = _f18_growth(gp, 63)
    g126 = _f18_growth(gp, 126)
    b = (1.0 + g126) - (1.0 + g63) ** 2
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gmom_21lag
def f18rg_f18_revenue_growth_engine_gmom_21lag_jerk_v129_signal(revenue):
    g = _f18_growth(revenue, 21).rolling(21, min_periods=10).mean()
    b = g - g.shift(21)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gmomusd_63lag
def f18rg_f18_revenue_growth_engine_gmomusd_63lag_jerk_v130_signal(revenueusd):
    g = _f18_growth(revenueusd, 126)
    b = g - g.shift(63)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gdisprat
def f18rg_f18_revenue_growth_engine_gdisprat_jerk_v131_signal(revenue):
    g = _f18_growth(revenue, 21)
    recent = _std(g, 63)
    prior = _std(g, 63).shift(63)
    b = recent / prior.replace(0, np.nan) - 1.0
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base logaccel
def f18rg_f18_revenue_growth_engine_logaccel_jerk_v132_signal(revenue):
    lg = np.log(revenue.replace(0, np.nan))
    accel = (lg - lg.shift(126)) - (lg.shift(126) - lg.shift(252))
    b = accel.ewm(span=63, min_periods=21).mean()
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gplogaccel
def f18rg_f18_revenue_growth_engine_gplogaccel_jerk_v133_signal(gp):
    lg = np.log(gp.replace(0, np.nan))
    accel = (lg - lg.shift(126)) - (lg.shift(126) - lg.shift(252))
    b = _z(accel, 504)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base grankspr
def f18rg_f18_revenue_growth_engine_grankspr_jerk_v134_signal(revenue):
    r1 = _rank(_f18_growth(revenue, 63), 504)
    r2 = _rank(_f18_growth(revenue, 252), 504)
    b = r1 - r2
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base stabspr
def f18rg_f18_revenue_growth_engine_stabspr_jerk_v135_signal(revenue, gp):
    sr = _f18_growth_stability(revenue, 252)
    sg = _f18_growth_stability(gp, 252)
    b = sr - sg
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gzfxspr
def f18rg_f18_revenue_growth_engine_gzfxspr_jerk_v136_signal(revenue, revenueusd):
    zr = _z(_f18_growth(revenue, 63), 252)
    zu = _z(_f18_growth(revenueusd, 63), 252)
    b = zr - zu
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gabovestreak
def f18rg_f18_revenue_growth_engine_gabovestreak_jerk_v137_signal(revenue):
    g = _f18_growth(revenue, 21)
    med = g.rolling(252, min_periods=126).median()
    above = (g > med).astype(float)
    grp = (above != above.shift(1)).cumsum()
    streak = above.groupby(grp).cumsum()
    b = (streak * above).clip(upper=126) / 126.0
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gpnewhi
def f18rg_f18_revenue_growth_engine_gpnewhi_jerk_v138_signal(gp):
    hi = gp.rolling(252, min_periods=126).max()
    is_hi = (gp >= hi * 0.99999).astype(float)
    b = is_hi.rolling(63, min_periods=21).mean()
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=42d) of base acc2g_126d
def f18rg_f18_revenue_growth_engine_acc2g_126d_jerk_v139_signal(revenue):
    g = _f18_growth(revenue, 126)
    a = _f18_growth_accel(revenue, 126)
    b = a / (g.abs() + 0.01)
    _d1 = (b - b.shift(42)) / 42.0
    result = (_d1 - _d1.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base marggrow
def f18rg_f18_revenue_growth_engine_marggrow_jerk_v140_signal(gp, revenue):
    m = gp / revenue.replace(0, np.nan)
    mtrend = m - m.shift(63)
    g = _f18_growth(revenue, 63)
    b = mtrend * np.sign(g) * (g.abs() ** 0.5)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gcompcons
def f18rg_f18_revenue_growth_engine_gcompcons_jerk_v141_signal(revenue):
    dl = np.log(revenue.replace(0, np.nan)).diff(21)
    b = dl.rolling(252, min_periods=126).std() / dl.rolling(252, min_periods=126).mean().abs().replace(0, np.nan)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base cagrusdrank
def f18rg_f18_revenue_growth_engine_cagrusdrank_jerk_v142_signal(revenueusd):
    c = _f18_cagr(revenueusd, 252)
    b = _rank(c, 504)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base cagrgpz
def f18rg_f18_revenue_growth_engine_cagrgpz_jerk_v143_signal(gp):
    c = _f18_cagr(gp, 126)
    b = c - c.shift(63)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base grange_252d
def f18rg_f18_revenue_growth_engine_grange_252d_jerk_v144_signal(revenue):
    g = _f18_growth(revenue, 63)
    hi = g.rolling(252, min_periods=126).max()
    lo = g.rolling(252, min_periods=126).min()
    b = hi - lo
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gprange_252d
def f18rg_f18_revenue_growth_engine_gprange_252d_jerk_v145_signal(gp):
    g = _f18_growth(gp, 63)
    hi = g.rolling(252, min_periods=126).max()
    lo = g.rolling(252, min_periods=126).min()
    b = hi - lo
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gpeakdist
def f18rg_f18_revenue_growth_engine_gpeakdist_jerk_v146_signal(revenue):
    g = _f18_growth(revenue, 63)
    hi = g.rolling(252, min_periods=126).max()
    b = (g - hi) / (hi.abs() + 0.01)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base gqualcomp
def f18rg_f18_revenue_growth_engine_gqualcomp_jerk_v147_signal(revenue, gp):
    rnk = _rank(_f18_growth(revenue, 63), 504)
    m = gp / revenue.replace(0, np.nan)
    b = rnk * m
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base durcomp
def f18rg_f18_revenue_growth_engine_durcomp_jerk_v148_signal(revenue):
    g = _f18_growth(revenue, 63)
    frac = (g > 0).astype(float).rolling(252, min_periods=126).mean()
    b = frac * _mean(g, 252)
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base accqual
def f18rg_f18_revenue_growth_engine_accqual_jerk_v149_signal(revenue, gp):
    a = _f18_growth_accel(revenue, 63)
    m = gp / revenue.replace(0, np.nan)
    b = np.sign(a) * (a.abs() ** 0.5) * m
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (roc=63d) of base engine
def f18rg_f18_revenue_growth_engine_engine_jerk_v150_signal(revenue, gp):
    stab = np.tanh(_f18_growth_stability(revenue, 252))
    rnk = _rank(_f18_growth(revenue, 126), 504)
    m = gp / revenue.replace(0, np.nan)
    b = stab * rnk * m
    _d1 = (b - b.shift(63)) / 63.0
    result = (_d1 - _d1.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f18rg_f18_revenue_growth_engine_revg_21d_jerk_v001_signal,
    f18rg_f18_revenue_growth_engine_revg_63d_jerk_v002_signal,
    f18rg_f18_revenue_growth_engine_revg_126d_jerk_v003_signal,
    f18rg_f18_revenue_growth_engine_revg_252d_jerk_v004_signal,
    f18rg_f18_revenue_growth_engine_revg_504d_jerk_v005_signal,
    f18rg_f18_revenue_growth_engine_revusdg_63d_jerk_v006_signal,
    f18rg_f18_revenue_growth_engine_revusdg_252d_jerk_v007_signal,
    f18rg_f18_revenue_growth_engine_gpg_252d_jerk_v008_signal,
    f18rg_f18_revenue_growth_engine_gpg_63d_jerk_v009_signal,
    f18rg_f18_revenue_growth_engine_gpg_126d_jerk_v010_signal,
    f18rg_f18_revenue_growth_engine_revlg_252d_jerk_v011_signal,
    f18rg_f18_revenue_growth_engine_revlg_126d_jerk_v012_signal,
    f18rg_f18_revenue_growth_engine_cagr_252d_jerk_v013_signal,
    f18rg_f18_revenue_growth_engine_cagr_504d_jerk_v014_signal,
    f18rg_f18_revenue_growth_engine_cagr_126d_jerk_v015_signal,
    f18rg_f18_revenue_growth_engine_cagrusd_252d_jerk_v016_signal,
    f18rg_f18_revenue_growth_engine_cagrgp_252d_jerk_v017_signal,
    f18rg_f18_revenue_growth_engine_seqg_63d_jerk_v018_signal,
    f18rg_f18_revenue_growth_engine_seqg_21d_jerk_v019_signal,
    f18rg_f18_revenue_growth_engine_seqgpg_63d_jerk_v020_signal,
    f18rg_f18_revenue_growth_engine_accel_63d_jerk_v021_signal,
    f18rg_f18_revenue_growth_engine_accel_126d_jerk_v022_signal,
    f18rg_f18_revenue_growth_engine_accel_252d_jerk_v023_signal,
    f18rg_f18_revenue_growth_engine_accelgp_63d_jerk_v024_signal,
    f18rg_f18_revenue_growth_engine_stab_252d_jerk_v025_signal,
    f18rg_f18_revenue_growth_engine_stab_126d_jerk_v026_signal,
    f18rg_f18_revenue_growth_engine_stabgp_252d_jerk_v027_signal,
    f18rg_f18_revenue_growth_engine_grank_63d_jerk_v028_signal,
    f18rg_f18_revenue_growth_engine_grank_252d_jerk_v029_signal,
    f18rg_f18_revenue_growth_engine_grankgp_252d_jerk_v030_signal,
    f18rg_f18_revenue_growth_engine_gz_63d_jerk_v031_signal,
    f18rg_f18_revenue_growth_engine_gz_126d_jerk_v032_signal,
    f18rg_f18_revenue_growth_engine_gzgp_126d_jerk_v033_signal,
    f18rg_f18_revenue_growth_engine_gqspr_252d_jerk_v034_signal,
    f18rg_f18_revenue_growth_engine_gqspr_63d_jerk_v035_signal,
    f18rg_f18_revenue_growth_engine_gterm_63v252_jerk_v036_signal,
    f18rg_f18_revenue_growth_engine_gtermr_126v252_jerk_v037_signal,
    f18rg_f18_revenue_growth_engine_fxdiv_252d_jerk_v038_signal,
    f18rg_f18_revenue_growth_engine_gdisp_252d_jerk_v039_signal,
    f18rg_f18_revenue_growth_engine_gdisp_126d_jerk_v040_signal,
    f18rg_f18_revenue_growth_engine_gema_63d_jerk_v041_signal,
    f18rg_f18_revenue_growth_engine_gdisp_ema_jerk_v042_signal,
    f18rg_f18_revenue_growth_engine_cagrspr_jerk_v043_signal,
    f18rg_f18_revenue_growth_engine_cagrgpspr_jerk_v044_signal,
    f18rg_f18_revenue_growth_engine_radjg_252d_jerk_v045_signal,
    f18rg_f18_revenue_growth_engine_gsignmag_252d_jerk_v046_signal,
    f18rg_f18_revenue_growth_engine_gtanh_63d_jerk_v047_signal,
    f18rg_f18_revenue_growth_engine_accelusd_63d_jerk_v048_signal,
    f18rg_f18_revenue_growth_engine_gconsist_252d_jerk_v049_signal,
    f18rg_f18_revenue_growth_engine_gpconsist_252d_jerk_v050_signal,
    f18rg_f18_revenue_growth_engine_gbreadth_jerk_v051_signal,
    f18rg_f18_revenue_growth_engine_lglvl_252d_jerk_v052_signal,
    f18rg_f18_revenue_growth_engine_grankusd_126d_jerk_v053_signal,
    f18rg_f18_revenue_growth_engine_accrank_63d_jerk_v054_signal,
    f18rg_f18_revenue_growth_engine_compgap_jerk_v055_signal,
    f18rg_f18_revenue_growth_engine_gpleverage_126d_jerk_v056_signal,
    f18rg_f18_revenue_growth_engine_gzspr_jerk_v057_signal,
    f18rg_f18_revenue_growth_engine_gdd_252d_jerk_v058_signal,
    f18rg_f18_revenue_growth_engine_grec_252d_jerk_v059_signal,
    f18rg_f18_revenue_growth_engine_gpos_252d_jerk_v060_signal,
    f18rg_f18_revenue_growth_engine_stabusd_252d_jerk_v061_signal,
    f18rg_f18_revenue_growth_engine_g2_126d_jerk_v062_signal,
    f18rg_f18_revenue_growth_engine_gpmom_126d_jerk_v063_signal,
    f18rg_f18_revenue_growth_engine_lvlmean_252d_jerk_v064_signal,
    f18rg_f18_revenue_growth_engine_gplvlmean_252d_jerk_v065_signal,
    f18rg_f18_revenue_growth_engine_gyoy2_jerk_v066_signal,
    f18rg_f18_revenue_growth_engine_ginteract_126d_jerk_v067_signal,
    f18rg_f18_revenue_growth_engine_gstreak_jerk_v068_signal,
    f18rg_f18_revenue_growth_engine_cagradj_252d_jerk_v069_signal,
    f18rg_f18_revenue_growth_engine_gpranktilt_jerk_v070_signal,
    f18rg_f18_revenue_growth_engine_gmultidisp_jerk_v071_signal,
    f18rg_f18_revenue_growth_engine_gmultispr_jerk_v072_signal,
    f18rg_f18_revenue_growth_engine_cagrusdadj_504d_jerk_v073_signal,
    f18rg_f18_revenue_growth_engine_accelsm_126d_jerk_v074_signal,
    f18rg_f18_revenue_growth_engine_durable_jerk_v075_signal,
    f18rg_f18_revenue_growth_engine_gz_21d_jerk_v076_signal,
    f18rg_f18_revenue_growth_engine_grank_21d_jerk_v077_signal,
    f18rg_f18_revenue_growth_engine_gzusd_63d_jerk_v078_signal,
    f18rg_f18_revenue_growth_engine_grankgp_63d_jerk_v079_signal,
    f18rg_f18_revenue_growth_engine_accelusd_126d_jerk_v080_signal,
    f18rg_f18_revenue_growth_engine_accelgp_126d_jerk_v081_signal,
    f18rg_f18_revenue_growth_engine_accelgp_252d_jerk_v082_signal,
    f18rg_f18_revenue_growth_engine_gdispusd_252d_jerk_v083_signal,
    f18rg_f18_revenue_growth_engine_gdispgp_252d_jerk_v084_signal,
    f18rg_f18_revenue_growth_engine_revcv_252d_jerk_v085_signal,
    f18rg_f18_revenue_growth_engine_gpcv_252d_jerk_v086_signal,
    f18rg_f18_revenue_growth_engine_lvlmean_126d_jerk_v087_signal,
    f18rg_f18_revenue_growth_engine_lvlmeanusd_252d_jerk_v088_signal,
    f18rg_f18_revenue_growth_engine_lvlpos_252d_jerk_v089_signal,
    f18rg_f18_revenue_growth_engine_gplvlpos_252d_jerk_v090_signal,
    f18rg_f18_revenue_growth_engine_newhi_252d_jerk_v091_signal,
    f18rg_f18_revenue_growth_engine_dsrh_252d_jerk_v092_signal,
    f18rg_f18_revenue_growth_engine_revdd_252d_jerk_v093_signal,
    f18rg_f18_revenue_growth_engine_gpdd_252d_jerk_v094_signal,
    f18rg_f18_revenue_growth_engine_revrec_252d_jerk_v095_signal,
    f18rg_f18_revenue_growth_engine_accrank_126d_jerk_v096_signal,
    f18rg_f18_revenue_growth_engine_accz_252d_jerk_v097_signal,
    f18rg_f18_revenue_growth_engine_fxlvl_jerk_v098_signal,
    f18rg_f18_revenue_growth_engine_fxmom_63d_jerk_v099_signal,
    f18rg_f18_revenue_growth_engine_gpmargin_jerk_v100_signal,
    f18rg_f18_revenue_growth_engine_gpmargmom_126d_jerk_v101_signal,
    f18rg_f18_revenue_growth_engine_gpmargz_252d_jerk_v102_signal,
    f18rg_f18_revenue_growth_engine_gqual_63d_jerk_v103_signal,
    f18rg_f18_revenue_growth_engine_poscount_504d_jerk_v104_signal,
    f18rg_f18_revenue_growth_engine_accpos_252d_jerk_v105_signal,
    f18rg_f18_revenue_growth_engine_gskew_252d_jerk_v106_signal,
    f18rg_f18_revenue_growth_engine_gpskew_252d_jerk_v107_signal,
    f18rg_f18_revenue_growth_engine_gupsemi_252d_jerk_v108_signal,
    f18rg_f18_revenue_growth_engine_gdnsemi_252d_jerk_v109_signal,
    f18rg_f18_revenue_growth_engine_gsemiskew_252d_jerk_v110_signal,
    f18rg_f18_revenue_growth_engine_gvov_jerk_v111_signal,
    f18rg_f18_revenue_growth_engine_geff_252d_jerk_v112_signal,
    f18rg_f18_revenue_growth_engine_gpeff_252d_jerk_v113_signal,
    f18rg_f18_revenue_growth_engine_gautoc_252d_jerk_v114_signal,
    f18rg_f18_revenue_growth_engine_revgpcorr_252d_jerk_v115_signal,
    f18rg_f18_revenue_growth_engine_gtermr_21v252_jerk_v116_signal,
    f18rg_f18_revenue_growth_engine_gtermusd_jerk_v117_signal,
    f18rg_f18_revenue_growth_engine_gtermgp_jerk_v118_signal,
    f18rg_f18_revenue_growth_engine_gema_126d_jerk_v119_signal,
    f18rg_f18_revenue_growth_engine_gpemadisp_jerk_v120_signal,
    f18rg_f18_revenue_growth_engine_gztanh_63d_jerk_v121_signal,
    f18rg_f18_revenue_growth_engine_gsignmag_126d_jerk_v122_signal,
    f18rg_f18_revenue_growth_engine_gsignmagusd_252d_jerk_v123_signal,
    f18rg_f18_revenue_growth_engine_radjgp_252d_jerk_v124_signal,
    f18rg_f18_revenue_growth_engine_radjusd_252d_jerk_v125_signal,
    f18rg_f18_revenue_growth_engine_gqsprusdgp_jerk_v126_signal,
    f18rg_f18_revenue_growth_engine_gconcav_jerk_v127_signal,
    f18rg_f18_revenue_growth_engine_gpconcav_jerk_v128_signal,
    f18rg_f18_revenue_growth_engine_gmom_21lag_jerk_v129_signal,
    f18rg_f18_revenue_growth_engine_gmomusd_63lag_jerk_v130_signal,
    f18rg_f18_revenue_growth_engine_gdisprat_jerk_v131_signal,
    f18rg_f18_revenue_growth_engine_logaccel_jerk_v132_signal,
    f18rg_f18_revenue_growth_engine_gplogaccel_jerk_v133_signal,
    f18rg_f18_revenue_growth_engine_grankspr_jerk_v134_signal,
    f18rg_f18_revenue_growth_engine_stabspr_jerk_v135_signal,
    f18rg_f18_revenue_growth_engine_gzfxspr_jerk_v136_signal,
    f18rg_f18_revenue_growth_engine_gabovestreak_jerk_v137_signal,
    f18rg_f18_revenue_growth_engine_gpnewhi_jerk_v138_signal,
    f18rg_f18_revenue_growth_engine_acc2g_126d_jerk_v139_signal,
    f18rg_f18_revenue_growth_engine_marggrow_jerk_v140_signal,
    f18rg_f18_revenue_growth_engine_gcompcons_jerk_v141_signal,
    f18rg_f18_revenue_growth_engine_cagrusdrank_jerk_v142_signal,
    f18rg_f18_revenue_growth_engine_cagrgpz_jerk_v143_signal,
    f18rg_f18_revenue_growth_engine_grange_252d_jerk_v144_signal,
    f18rg_f18_revenue_growth_engine_gprange_252d_jerk_v145_signal,
    f18rg_f18_revenue_growth_engine_gpeakdist_jerk_v146_signal,
    f18rg_f18_revenue_growth_engine_gqualcomp_jerk_v147_signal,
    f18rg_f18_revenue_growth_engine_durcomp_jerk_v148_signal,
    f18rg_f18_revenue_growth_engine_accqual_jerk_v149_signal,
    f18rg_f18_revenue_growth_engine_engine_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F18_REVENUE_GROWTH_ENGINE_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    ALLOW = {
        "open", "high", "low", "close", "closeadj", "volume",
        "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc",
        "opex", "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin",
        "netinc", "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps",
        "ncfo", "ncff", "ncfi", "ncfcommon", "ncfdebt", "ncfbus", "capex",
        "depamor", "sharesbas", "shareswa", "shareswadil", "assets", "assetsc",
        "tangibles", "intangibles", "ppnenet", "investments", "inventory",
        "receivables", "payables", "equity", "retearn", "workingcapital", "debt",
        "debtc", "debtnc", "liabilities", "liabilitiesc", "cashneq", "currentratio",
        "roic", "roe", "roa", "ros", "assetturnover", "invcap", "intexp", "taxexp",
        "ebt", "sps", "bvps", "de", "ncfdiv", "dps", "divyield", "payoutratio",
        "prefdivis", "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
        "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal",
        "fndholders", "undholders", "prfholders", "dbtholders", "putholders",
        "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue", "dbtvalue",
    }

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    revenue = _fund(101, base=1.5e8, drift=0.035, vol=0.08).rename("revenue")
    revenueusd = _fund(102, base=1.5e8, drift=0.033, vol=0.085).rename("revenueusd")
    gp = _fund(103, base=6.0e7, drift=0.040, vol=0.10).rename("gp")

    cols = {"revenue": revenue, "revenueusd": revenueusd, "gp": gp}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs %s" % (name, meta["inputs"])
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 20, "%s nunique=%d" % (name, q.nunique())
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

    print("OK f18_revenue_growth_engine_3rd_derivatives_001_150_claude: %d features pass" % n_features)
