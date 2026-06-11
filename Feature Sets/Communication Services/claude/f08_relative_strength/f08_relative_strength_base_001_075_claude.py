import inspect
import numpy as np
import pandas as pd

# f08_relative_strength (f08rs) — Communication Services SASS signal features (001-075).
# TIGHTENED DOMAIN: SELF-RELATIVE *RISK-ADJUSTED* STRENGTH ONLY. Every feature is a
# risk-adjusted return measure vs the stock's OWN history (Sharpe / Sortino / Calmar /
# MAR / Martin / ulcer-adjusted return over 63/126/252/504/1260d), a self-relative
# risk-adjusted PERCENTILE-RANK vs its own trailing distribution, a drawdown-adjusted
# strength, or a gain-to-pain ratio. Single-series, no benchmark.
#   DO NOT compute Kaufman efficiency ratio / Hurst / autocorrelation (that is f03).
#   DO NOT compute raw ROC / 12-1 momentum LEVELS or rank-of-raw-ROC (that is f02).
#   DO NOT compute price-vs-MA / RS-ratio-vs-MA (that is f01).
# Distinctness discipline: no two features share the same (measure, window, facet); facets
# decorrelate (level / rank / IQR-robust / regime-band / cross-measure-difference /
# velocity / curvature / regime-time / standalone-pain-component).
# Inputs: closeadj only. Windows >21d use closeadj (per SPEC).

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_FIVEYEAR = 1260
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rank(s, w):
    # rolling percentile rank centred at 0
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _iqr_ctr(s, w):
    # robust de-median over own IQR vs w history (decorrelates from level)
    med = s.rolling(w, min_periods=max(2, w // 2)).median()
    q1 = s.rolling(w, min_periods=max(2, w // 2)).quantile(0.25)
    q3 = s.rolling(w, min_periods=max(2, w // 2)).quantile(0.75)
    return (s - med) / (q3 - q1).replace(0, np.nan)


# ===== folder domain primitives (RISK-ADJUSTED self-relative strength) =====
def _f08rs_logret(closeadj):
    return np.log(closeadj.replace(0, np.nan)).diff()


def _f08rs_cumret(closeadj, w):
    return np.log(closeadj.replace(0, np.nan)) - np.log(closeadj.shift(w).replace(0, np.nan))


def _f08rs_sharpe(closeadj, w):
    # self-Sharpe: mean daily log-return over w divided by its own std (annualised)
    lr = _f08rs_logret(closeadj)
    mu = lr.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = lr.rolling(w, min_periods=max(2, w // 2)).std()
    return mu / sd.replace(0, np.nan) * np.sqrt(252.0)


def _f08rs_sortino(closeadj, w):
    # self-Sortino: mean daily log-return over downside semi-deviation (annualised)
    lr = _f08rs_logret(closeadj)
    mu = lr.rolling(w, min_periods=max(2, w // 2)).mean()
    down = lr.where(lr < 0, 0.0)
    dd = np.sqrt((down ** 2).rolling(w, min_periods=max(2, w // 2)).mean())
    return mu / dd.replace(0, np.nan) * np.sqrt(252.0)


def _f08rs_underwater(closeadj, w):
    peak = closeadj.rolling(w, min_periods=max(1, w // 2)).max()
    return closeadj / peak.replace(0, np.nan) - 1.0


def _f08rs_maxdd(closeadj, w):
    uw = _f08rs_underwater(closeadj, w)
    return (-uw).rolling(w, min_periods=max(1, w // 2)).max()


def _f08rs_ulcer(closeadj, w):
    # Ulcer index: RMS of underwater depth over w (downside-pain magnitude)
    uw = _f08rs_underwater(closeadj, w)
    return np.sqrt((uw ** 2).rolling(w, min_periods=max(1, w // 2)).mean())


def _f08rs_calmar(closeadj, w):
    # Calmar/MAR: net log return per unit of own max drawdown over w
    return _f08rs_cumret(closeadj, w) / _f08rs_maxdd(closeadj, w).replace(0, np.nan)


def _f08rs_martin(closeadj, w):
    # Martin ratio: net log return per unit of own Ulcer index over w
    return _f08rs_cumret(closeadj, w) / _f08rs_ulcer(closeadj, w).replace(0, np.nan)


def _f08rs_gaintopain(closeadj, w):
    # gain-to-pain: sum of returns over sum of absolute losses across w
    lr = _f08rs_logret(closeadj)
    g = lr.rolling(w, min_periods=max(2, w // 2)).sum()
    pain = lr.clip(upper=0).abs().rolling(w, min_periods=max(2, w // 2)).sum()
    return g / pain.replace(0, np.nan)


# ============================================================
# --- LEVELS: one risk-adjusted level per (measure, window), distinct windows ---
# self-Sharpe over 252d (risk-adjusted strength vs own history)
def f08rs_f08_relative_strength_sharpe_252d_base_v001_signal(closeadj):
    b = _f08rs_sharpe(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-Sortino over 504d (long-horizon downside-risk-adjusted strength)
def f08rs_f08_relative_strength_sortino_504d_base_v002_signal(closeadj):
    b = _f08rs_sortino(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Calmar/MAR over 126d: return per unit of own max drawdown (fast drawdown-adjusted)
def f08rs_f08_relative_strength_calmar_126d_base_v003_signal(closeadj):
    b = _f08rs_calmar(closeadj, 126).clip(-20, 20)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Martin ratio over 504d minus its own 252d EMA (ulcer-adj displacement, decorrelated from level)
def f08rs_f08_relative_strength_martin_1260d_base_v004_signal(closeadj):
    m = _f08rs_martin(closeadj, 504).clip(-80, 80)
    b = m - m.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gain-to-pain over 63d (fast path-quality balance)
def f08rs_f08_relative_strength_gaintopain_63d_base_v005_signal(closeadj):
    b = _f08rs_gaintopain(closeadj, 63).clip(-10, 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- RANKS vs own trailing distribution (decorrelated from levels) ---
# self-Sharpe over 126d, percentile-ranked vs own 504d distribution
def f08rs_f08_relative_strength_sharperank_126d_base_v006_signal(closeadj):
    b = _rank(_f08rs_sharpe(closeadj, 126), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-Sortino over 252d, percentile-ranked vs own 504d distribution
def f08rs_f08_relative_strength_sortinorank_252d_base_v007_signal(closeadj):
    b = _rank(_f08rs_sortino(closeadj, 252), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Calmar over 504d, percentile-ranked vs own 1260d distribution (deep drawdown-adj rank)
def f08rs_f08_relative_strength_calmarrank_504d_base_v008_signal(closeadj):
    b = _rank(_f08rs_calmar(closeadj, 504), 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Martin over 63d, percentile-ranked vs own 252d distribution (fast ulcer-adj rank)
def f08rs_f08_relative_strength_martinrank_63d_base_v009_signal(closeadj):
    b = _rank(_f08rs_martin(closeadj, 63), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gain-to-pain over 252d, percentile-ranked vs own 1260d distribution
def f08rs_f08_relative_strength_gtprank_252d_base_v010_signal(closeadj):
    b = _rank(_f08rs_gaintopain(closeadj, 252), 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- CROSS-MEASURE DIFFERENCES (numerator cancels -> capture risk-view disagreement) ---
# downside-asymmetry of risk-adjusted strength: (Sharpe - Sortino) scaled by Sharpe magnitude
def f08rs_f08_relative_strength_sharpesortinodiff_252d_base_v011_signal(closeadj):
    sh = _f08rs_sharpe(closeadj, 252)
    so = _f08rs_sortino(closeadj, 252)
    b = (sh - so) / (sh.abs() + so.abs()).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Calmar minus Sharpe rank over 252d: drawdown-view vs vol-view of strength
def f08rs_f08_relative_strength_calmarsharpediff_252d_base_v012_signal(closeadj):
    c = _rank(_f08rs_calmar(closeadj, 252), 504)
    s = _rank(_f08rs_sharpe(closeadj, 252), 504)
    b = c - s
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Martin minus Sortino rank over 252d: ulcer-pain vs semi-deviation risk-view
def f08rs_f08_relative_strength_martinsortinodiff_252d_base_v013_signal(closeadj):
    m = _rank(_f08rs_martin(closeadj, 252), 504)
    s = _rank(_f08rs_sortino(closeadj, 252), 504)
    b = m - s
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gain-to-pain minus Martin level over 126d: distributed-pain vs ulcer-pain (fast skew of pain)
def f08rs_f08_relative_strength_gtpcalmardiff_252d_base_v014_signal(closeadj):
    g = _f08rs_gaintopain(closeadj, 126).clip(-10, 10)
    m = np.tanh(_f08rs_martin(closeadj, 126) / 8.0) * 5.0
    b = g - m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sortino-over-Sharpe ratio over 504d: long-horizon downside-asymmetry multiplier
def f08rs_f08_relative_strength_sortsharperatio_504d_base_v015_signal(closeadj):
    sh = _f08rs_sharpe(closeadj, 504)
    so = _f08rs_sortino(closeadj, 504)
    b = (so / sh.replace(0, np.nan)).clip(-5, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- HORIZON SPREADS (same measure, different windows -> rotation tilt) ---
# Sharpe spread 126d minus 252d (risk-adj horizon tilt)
def f08rs_f08_relative_strength_sharpespr_126v252_base_v016_signal(closeadj):
    b = _f08rs_sharpe(closeadj, 126) - _f08rs_sharpe(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sortino spread 63d minus 252d (fast vs slow downside-risk-adj strength)
def f08rs_f08_relative_strength_sortinospr_63v252_base_v017_signal(closeadj):
    b = _f08rs_sortino(closeadj, 63) - _f08rs_sortino(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Calmar spread 252d minus 504d (medium vs long drawdown-adj strength)
def f08rs_f08_relative_strength_calmarspr_252v504_base_v018_signal(closeadj):
    c1 = _f08rs_calmar(closeadj, 252).clip(-20, 20)
    c2 = _f08rs_calmar(closeadj, 504).clip(-20, 20)
    b = c1 - c2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Martin spread 126d minus 504d (pain-horizon tilt)
def f08rs_f08_relative_strength_martinspr_126v504_base_v019_signal(closeadj):
    m1 = _f08rs_martin(closeadj, 126).clip(-80, 80)
    m2 = _f08rs_martin(closeadj, 504).clip(-80, 80)
    b = m1 - m2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gain-to-pain horizon spread 126d minus 504d, rank-based (path-quality rotation, decorrelated)
def f08rs_f08_relative_strength_gtpspr_63v252_base_v020_signal(closeadj):
    g1 = _rank(_f08rs_gaintopain(closeadj, 126), 504)
    g2 = _rank(_f08rs_gaintopain(closeadj, 504), 504)
    b = g1 - g2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- IQR-ROBUST EXTREMITY (de-median over own IQR) ---
# Sharpe robust extremity vs own 504d IQR
def f08rs_f08_relative_strength_sharpeiqr_252d_base_v021_signal(closeadj):
    b = _iqr_ctr(_f08rs_sharpe(closeadj, 252), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Calmar robust extremity vs own 504d IQR
def f08rs_f08_relative_strength_calmariqr_252d_base_v022_signal(closeadj):
    b = _iqr_ctr(_f08rs_calmar(closeadj, 252).clip(-20, 20), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Martin year-over-year change (ulcer-adjusted strength annual drift)
def f08rs_f08_relative_strength_martiniqr_252d_base_v023_signal(closeadj):
    m = _f08rs_martin(closeadj, 252).clip(-80, 80)
    b = m - m.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- REGIME BAND POSITION ---
# Calmar regime: where 126d Calmar sits within its own 504d 25-75 band (drawdown-adj positioning)
def f08rs_f08_relative_strength_sortinoregime_252d_base_v024_signal(closeadj):
    c = _f08rs_calmar(closeadj, 126).clip(-20, 20)
    q25 = c.rolling(504, min_periods=252).quantile(0.25)
    q75 = c.rolling(504, min_periods=252).quantile(0.75)
    b = (c - q25) / (q75 - q25).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gain-to-pain regime band over own 1260d (deep path-quality positioning)
def f08rs_f08_relative_strength_gtpregime_base_v025_signal(closeadj):
    g = _f08rs_gaintopain(closeadj, 252)
    q25 = g.rolling(1260, min_periods=504).quantile(0.25)
    q75 = g.rolling(1260, min_periods=504).quantile(0.75)
    b = (g - q25) / (q75 - q25).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- VELOCITY (change in measure / rank over a quarter) ---
# Sharpe change over a quarter (risk-adjusted strength acceleration)
def f08rs_f08_relative_strength_sharpemom_base_v026_signal(closeadj):
    sh = _f08rs_sharpe(closeadj, 252)
    b = sh - sh.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Calmar-rank velocity over a quarter (drawdown-adjusted leadership velocity)
def f08rs_f08_relative_strength_calmarrankvel_base_v027_signal(closeadj):
    r = _rank(_f08rs_calmar(closeadj, 252), 504)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Martin change over a quarter (ulcer-adjusted strength velocity)
def f08rs_f08_relative_strength_martinmom_base_v028_signal(closeadj):
    m = _f08rs_martin(closeadj, 252).clip(-80, 80)
    b = m - m.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gain-to-pain-rank velocity over a quarter (path-quality rotation)
def f08rs_f08_relative_strength_gtprankvel_base_v029_signal(closeadj):
    r = _rank(_f08rs_gaintopain(closeadj, 252), 504)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- CURVATURE (2nd difference) ---
# Sortino acceleration: 2nd-difference of 252d Sortino over quarters (risk-adj bend)
def f08rs_f08_relative_strength_sortinocurv_base_v030_signal(closeadj):
    so = _f08rs_sortino(closeadj, 252)
    b = so - 2.0 * so.shift(42) + so.shift(84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sharpe-rank curvature: bend of 252d Sharpe percentile rank over quarters
def f08rs_f08_relative_strength_sharperankcurv_base_v031_signal(closeadj):
    r = _rank(_f08rs_sharpe(closeadj, 252), 504)
    b = r - 2.0 * r.shift(42) + r.shift(84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- PEAK-GAP (drawdown of the risk-adjusted measure itself) ---
# Sharpe drawdown-from-best: current 126d Sharpe gap below its own trailing 252d peak (fast)
def f08rs_f08_relative_strength_sharpepeakgap_base_v032_signal(closeadj):
    sh = _f08rs_sharpe(closeadj, 126)
    peak = sh.rolling(252, min_periods=126).max()
    b = sh - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Calmar recovery-from-trough: current 252d Calmar above its own trailing 504d min
def f08rs_f08_relative_strength_calmartroughgap_base_v033_signal(closeadj):
    c = _f08rs_calmar(closeadj, 252).clip(-20, 20)
    trough = c.rolling(504, min_periods=252).min()
    b = c - trough
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- REGIME-TIME (fraction of window in a risk-adjusted state) ---
# fraction of last year 126d Sharpe stayed positive (risk-adj up-regime time)
def f08rs_f08_relative_strength_sharpeposfrac_base_v034_signal(closeadj):
    sh = _f08rs_sharpe(closeadj, 126)
    pos = (sh > 0).astype(float)
    b = pos.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year 126d Calmar above its own median (drawdown-adj up-regime)
def f08rs_f08_relative_strength_calmarposfrac_base_v035_signal(closeadj):
    c = _f08rs_calmar(closeadj, 126).clip(-20, 20)
    med = c.rolling(252, min_periods=126).median()
    above = (c > med).astype(float)
    b = above.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year 126d Martin above own 504d 75th pct (ulcer-adj leadership time)
def f08rs_f08_relative_strength_martintopfrac_base_v036_signal(closeadj):
    m = _f08rs_martin(closeadj, 126)
    q75 = m.rolling(504, min_periods=252).quantile(0.75)
    top = (m > q75).astype(float)
    b = top.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year in top-quartile 126d Sortino rank (sustained downside-adj leadership)
def f08rs_f08_relative_strength_sortinotopq_base_v037_signal(closeadj):
    r = _rank(_f08rs_sortino(closeadj, 126), 252) + 0.5
    top = (r >= 0.75).astype(float)
    b = top.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- STANDALONE PAIN COMPONENTS (denominators as features, not ratios) ---
# Ulcer index over 252d, ranked and negated (less pain = stronger), standalone risk
def f08rs_f08_relative_strength_ulcerstrength_252d_base_v038_signal(closeadj):
    b = -_rank(_f08rs_ulcer(closeadj, 252), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# max drawdown over 504d, ranked and negated (shallow worst-loss = strength), standalone
def f08rs_f08_relative_strength_maxddstrength_504d_base_v039_signal(closeadj):
    b = -_rank(_f08rs_maxdd(closeadj, 504), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside-variance share over 252d (fraction of variance that is downside, de-centred)
def f08rs_f08_relative_strength_downshare_252d_base_v040_signal(closeadj):
    lr = _f08rs_logret(closeadj)
    down = lr.where(lr < 0, 0.0)
    dvar = (down ** 2).rolling(252, min_periods=126).mean()
    tvar = (lr ** 2).rolling(252, min_periods=126).mean()
    b = dvar / tvar.replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- BLENDS / DISPERSION across measures ---
# blended multi-horizon risk-adjusted rank: mean Sharpe rank across 63/126/252/504 windows
def f08rs_f08_relative_strength_blendriskrank_base_v041_signal(closeadj):
    r1 = _rank(_f08rs_sharpe(closeadj, 63), 252)
    r2 = _rank(_f08rs_sharpe(closeadj, 126), 252)
    r3 = _rank(_f08rs_sharpe(closeadj, 252), 504)
    r4 = _rank(_f08rs_sharpe(closeadj, 504), 1260)
    b = (r1 + r2 + r3 + r4) / 4.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sharpe horizon-rank disagreement: std of Sharpe ranks across 63/126/252/504 (horizon spread)
def f08rs_f08_relative_strength_riskrankdisp_base_v042_signal(closeadj):
    r1 = _rank(_f08rs_sharpe(closeadj, 63), 252)
    r2 = _rank(_f08rs_sharpe(closeadj, 126), 252)
    r3 = _rank(_f08rs_sharpe(closeadj, 252), 504)
    r4 = _rank(_f08rs_sharpe(closeadj, 504), 1260)
    b = pd.concat([r1, r2, r3, r4], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sharpe horizon dispersion across 63/126/252/504 (risk-adj strength horizon disagreement)
def f08rs_f08_relative_strength_sharpehorizdisp_base_v043_signal(closeadj):
    cols = [_f08rs_sharpe(closeadj, w) for w in (63, 126, 252, 504)]
    b = pd.concat(cols, axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- BOUNDED (tanh) variants at distinct windows ---
# tanh-squashed self-Sharpe over 63d (bounded fast risk-adjusted strength)
def f08rs_f08_relative_strength_sharpetanh_63d_base_v044_signal(closeadj):
    b = np.tanh(_f08rs_sharpe(closeadj, 63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed Calmar over 504d (bounded long drawdown-adjusted strength)
def f08rs_f08_relative_strength_calmartanh_504d_base_v045_signal(closeadj):
    b = np.tanh(_f08rs_calmar(closeadj, 504) / 3.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- YEAR-OVER-YEAR drift ---
# Sortino year-over-year change (annual drift of downside-risk-adjusted strength)
def f08rs_f08_relative_strength_sortinoyoy_base_v046_signal(closeadj):
    so = _f08rs_sortino(closeadj, 252)
    b = so - so.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Calmar half-year change (drawdown-adjusted strength medium-horizon drift)
def f08rs_f08_relative_strength_calmaryoy_base_v047_signal(closeadj):
    c = _f08rs_calmar(closeadj, 252).clip(-20, 20)
    b = c - c.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- SMOOTHED-RANK durability ---
# Sortino smoothed and ranked over 504d (durable downside-risk-adj leadership)
def f08rs_f08_relative_strength_sortinosmrank_base_v048_signal(closeadj):
    so = _f08rs_sortino(closeadj, 252)
    sm = so.ewm(span=42, min_periods=21).mean()
    b = _rank(sm, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Martin smoothed minus own 252d median (persistent ulcer-adjusted extremity)
def f08rs_f08_relative_strength_martinctr_base_v049_signal(closeadj):
    m = _f08rs_martin(closeadj, 252).clip(-80, 80)
    sm = m.ewm(span=42, min_periods=21).mean()
    b = sm - sm.rolling(252, min_periods=126).median()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- STABILITY / CONSISTENCY ---
# Sharpe-rank stability: negative std of 126d Sharpe rank over 126d (steady leadership)
def f08rs_f08_relative_strength_sharperankstab_base_v050_signal(closeadj):
    r = _rank(_f08rs_sharpe(closeadj, 126), 252)
    b = -r.rolling(126, min_periods=63).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sharpe-of-Sharpe: mean 63d Sharpe over its own dispersion across 252d (consistency)
def f08rs_f08_relative_strength_sharpeconsist_base_v051_signal(closeadj):
    sh = _f08rs_sharpe(closeadj, 63)
    mu = sh.rolling(252, min_periods=126).mean()
    sd = sh.rolling(252, min_periods=126).std()
    b = mu / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- SLOPE-TO-NOISE / TREND-OF-MEASURE ---
# Sortino slope-to-noise: trend of 252d Sortino over its own dispersion (durable down-adj)
def f08rs_f08_relative_strength_sortinotrendnoise_base_v052_signal(closeadj):
    so = _f08rs_sortino(closeadj, 252)
    slope = so - so.shift(42)
    noise = so.diff().abs().rolling(63, min_periods=21).mean()
    b = slope / noise.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Calmar slope-to-noise: trend of 252d Calmar over its own dispersion
def f08rs_f08_relative_strength_calmartrendnoise_base_v053_signal(closeadj):
    c = _f08rs_calmar(closeadj, 252).clip(-20, 20)
    slope = c - c.shift(42)
    noise = c.diff().abs().rolling(63, min_periods=21).mean()
    b = slope / noise.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- DEEP / MULTI-YEAR risk-adjusted strength ---
# self-Sharpe over the deepest 1260d window (multi-year risk-adjusted strength)
def f08rs_f08_relative_strength_sharpe_1260d_base_v054_signal(closeadj):
    b = _f08rs_sharpe(closeadj, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sortino deep horizon spread: 504d minus 1260d (deep down-adj horizon tilt)
def f08rs_f08_relative_strength_sortinodeepspr_base_v055_signal(closeadj):
    b = _f08rs_sortino(closeadj, 504) - _f08rs_sortino(closeadj, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Martin minus Calmar deep rank (ulcer-pain vs single-worst-drawdown view, deep horizon)
def f08rs_f08_relative_strength_martindeeprank_base_v056_signal(closeadj):
    m = _rank(_f08rs_martin(closeadj, 504), 1260)
    c = _rank(_f08rs_calmar(closeadj, 504), 1260)
    b = m - c
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Calmar deep rank: 252d Calmar percentile-ranked vs own 1260d distribution (multi-year drawdown-adj)
def f08rs_f08_relative_strength_calmar_1260d_base_v057_signal(closeadj):
    b = _rank(_f08rs_calmar(closeadj, 252), 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- JOINT-CONVICTION interactions ---
# Sharpe x Calmar joint conviction: sign agreement times min bounded magnitude
def f08rs_f08_relative_strength_sharpecalmarjoint_base_v058_signal(closeadj):
    s = _f08rs_sharpe(closeadj, 252)
    c = _f08rs_calmar(closeadj, 252).clip(-20, 20)
    agree = np.sign(s) * np.sign(c)
    mag = pd.concat([s.abs(), (c / 5.0).abs()], axis=1).min(axis=1)
    b = agree * mag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sortino x gain-to-pain DISAGREEMENT: absolute rank gap (joint quality conflict, decorrelated)
def f08rs_f08_relative_strength_sortinogtpjoint_base_v059_signal(closeadj):
    sr = _rank(_f08rs_sortino(closeadj, 252), 504)
    gr = _rank(_f08rs_gaintopain(closeadj, 252), 504)
    b = (sr - gr).abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- REGIME VELOCITY ---
# Sortino regime-band velocity: change in band position over a quarter (down-adj rotation)
def f08rs_f08_relative_strength_sortinoregimevel_base_v060_signal(closeadj):
    so = _f08rs_sortino(closeadj, 252)
    q25 = so.rolling(504, min_periods=252).quantile(0.25)
    q75 = so.rolling(504, min_periods=252).quantile(0.75)
    pos = (so - q25) / (q75 - q25).replace(0, np.nan)
    b = pos - pos.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- PAIN-FAMILY blend / composites ---
# pain-family disagreement: spread between best and worst of Calmar/Martin/gtp ranks
def f08rs_f08_relative_strength_painrank_base_v061_signal(closeadj):
    r1 = _rank(_f08rs_calmar(closeadj, 252), 504)
    r2 = _rank(_f08rs_martin(closeadj, 252), 504)
    r3 = _rank(_f08rs_gaintopain(closeadj, 252), 504)
    stacked = pd.concat([r1, r2, r3], axis=1)
    b = stacked.max(axis=1) - stacked.min(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sharpe minus Martin level over 504d (vol-risk vs ulcer-risk view, long horizon)
def f08rs_f08_relative_strength_sharpemartindiff_504d_base_v062_signal(closeadj):
    b = _f08rs_sharpe(closeadj, 504) - np.tanh(_f08rs_martin(closeadj, 504) / 8.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- FAST-RANK leadership ---
# Sharpe over 21d ranked vs own 126d history (very-fast risk-adjusted leadership rank)
def f08rs_f08_relative_strength_fastsharperank_base_v063_signal(closeadj):
    b = _rank(_f08rs_sharpe(closeadj, 21), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gain-to-pain over 126d ranked vs own 252d history (fast path-quality rank)
def f08rs_f08_relative_strength_fastgtprank_base_v064_signal(closeadj):
    b = _rank(_f08rs_gaintopain(closeadj, 126), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ULCER / DRAWDOWN dynamics ---
# Ulcer index change over a quarter (deepening vs healing pain), negated for strength
def f08rs_f08_relative_strength_ulcermom_base_v065_signal(closeadj):
    ui = _f08rs_ulcer(closeadj, 126)
    b = -(ui - ui.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# max-drawdown depth over 252d in own-vol units, negated (vol-scaled drawdown strength)
def f08rs_f08_relative_strength_ddvolunits_base_v066_signal(closeadj):
    mdd = _f08rs_maxdd(closeadj, 252)
    vol = _f08rs_logret(closeadj).rolling(63, min_periods=21).std() * np.sqrt(252.0)
    b = -mdd / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ROBUST ratio variants ---
# Calmar robust extremity vs own 1260d IQR (deep drawdown-adj extremity)
def f08rs_f08_relative_strength_calmariqr_deep_base_v067_signal(closeadj):
    b = _iqr_ctr(_f08rs_calmar(closeadj, 504).clip(-20, 20), 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gain-to-pain 504d minus own 252d EMA (long path-quality displacement)
def f08rs_f08_relative_strength_sortinoiqr_252d_base_v068_signal(closeadj):
    g = _f08rs_gaintopain(closeadj, 504).clip(-10, 10)
    b = g - g.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- SHARPE-MINUS-SORTINO at distinct windows (skew of risk-adj RS) ---
# Sharpe minus Sortino over 126d (fast skew of risk-adjusted strength)
def f08rs_f08_relative_strength_sharpesortinodiff_126d_base_v069_signal(closeadj):
    b = _f08rs_sharpe(closeadj, 126) - _f08rs_sortino(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- GAIN-TO-PAIN smoothed / centred ---
# gain-to-pain smoothed minus own 252d median (persistent path-quality extremity)
def f08rs_f08_relative_strength_gtpctr_base_v070_signal(closeadj):
    g = _f08rs_gaintopain(closeadj, 252).clip(-10, 10)
    sm = g.ewm(span=42, min_periods=21).mean()
    b = sm - sm.rolling(252, min_periods=126).median()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- MARTIN year-over-year & misc ---
# Martin level velocity over a half-year (ulcer-adjusted strength medium-horizon drift)
def f08rs_f08_relative_strength_martinrankvel_base_v071_signal(closeadj):
    m = _f08rs_martin(closeadj, 504).clip(-80, 80)
    b = m - m.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Calmar consistency: longest run of consecutive days 126d Calmar stayed positive, normalised
def f08rs_f08_relative_strength_calmarposyear_base_v072_signal(closeadj):
    c = _f08rs_calmar(closeadj, 126).clip(-20, 20)
    pos = (c > 0)
    grp = (pos != pos.shift()).cumsum()
    streak = pos.groupby(grp).cumcount() + 1
    b = (streak * pos.astype(float)).rolling(252, min_periods=126).max() / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- SHARPE regime-time deep ---
# fraction of last 2y 252d Sharpe in top half of its own 1260d band (deep up-regime time)
def f08rs_f08_relative_strength_sharpedeepregimetime_base_v073_signal(closeadj):
    sh = _f08rs_sharpe(closeadj, 252)
    med = sh.rolling(1260, min_periods=504).median()
    above = (sh > med).astype(float)
    b = above.rolling(504, min_periods=252).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- SORTINO smoothed level ---
# Sortino smoothed minus own 504d median at long 504d horizon (persistent deep down-adj extremity)
def f08rs_f08_relative_strength_sortinoctr_base_v074_signal(closeadj):
    so = _f08rs_sortino(closeadj, 504)
    sm = so.ewm(span=63, min_periods=21).mean()
    b = sm - sm.rolling(504, min_periods=252).median()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- COMPOSITE self-relative risk-adjusted strength score ---
# composite: bounded multi-horizon Sharpe minus normalised ulcer pain (broad risk-adj strength)
def f08rs_f08_relative_strength_composite_base_v075_signal(closeadj):
    s1 = np.tanh(_f08rs_sharpe(closeadj, 63))
    s2 = np.tanh(_f08rs_sharpe(closeadj, 252))
    s3 = np.tanh(_f08rs_calmar(closeadj, 504) / 3.0)
    pain = -_rank(_f08rs_ulcer(closeadj, 504), 504)
    b = (s1 + s2 + s3) / 3.0 + 0.5 * pain
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f08rs_f08_relative_strength_sharpe_252d_base_v001_signal,
    f08rs_f08_relative_strength_sortino_504d_base_v002_signal,
    f08rs_f08_relative_strength_calmar_126d_base_v003_signal,
    f08rs_f08_relative_strength_martin_1260d_base_v004_signal,
    f08rs_f08_relative_strength_gaintopain_63d_base_v005_signal,
    f08rs_f08_relative_strength_sharperank_126d_base_v006_signal,
    f08rs_f08_relative_strength_sortinorank_252d_base_v007_signal,
    f08rs_f08_relative_strength_calmarrank_504d_base_v008_signal,
    f08rs_f08_relative_strength_martinrank_63d_base_v009_signal,
    f08rs_f08_relative_strength_gtprank_252d_base_v010_signal,
    f08rs_f08_relative_strength_sharpesortinodiff_252d_base_v011_signal,
    f08rs_f08_relative_strength_calmarsharpediff_252d_base_v012_signal,
    f08rs_f08_relative_strength_martinsortinodiff_252d_base_v013_signal,
    f08rs_f08_relative_strength_gtpcalmardiff_252d_base_v014_signal,
    f08rs_f08_relative_strength_sortsharperatio_504d_base_v015_signal,
    f08rs_f08_relative_strength_sharpespr_126v252_base_v016_signal,
    f08rs_f08_relative_strength_sortinospr_63v252_base_v017_signal,
    f08rs_f08_relative_strength_calmarspr_252v504_base_v018_signal,
    f08rs_f08_relative_strength_martinspr_126v504_base_v019_signal,
    f08rs_f08_relative_strength_gtpspr_63v252_base_v020_signal,
    f08rs_f08_relative_strength_sharpeiqr_252d_base_v021_signal,
    f08rs_f08_relative_strength_calmariqr_252d_base_v022_signal,
    f08rs_f08_relative_strength_martiniqr_252d_base_v023_signal,
    f08rs_f08_relative_strength_sortinoregime_252d_base_v024_signal,
    f08rs_f08_relative_strength_gtpregime_base_v025_signal,
    f08rs_f08_relative_strength_sharpemom_base_v026_signal,
    f08rs_f08_relative_strength_calmarrankvel_base_v027_signal,
    f08rs_f08_relative_strength_martinmom_base_v028_signal,
    f08rs_f08_relative_strength_gtprankvel_base_v029_signal,
    f08rs_f08_relative_strength_sortinocurv_base_v030_signal,
    f08rs_f08_relative_strength_sharperankcurv_base_v031_signal,
    f08rs_f08_relative_strength_sharpepeakgap_base_v032_signal,
    f08rs_f08_relative_strength_calmartroughgap_base_v033_signal,
    f08rs_f08_relative_strength_sharpeposfrac_base_v034_signal,
    f08rs_f08_relative_strength_calmarposfrac_base_v035_signal,
    f08rs_f08_relative_strength_martintopfrac_base_v036_signal,
    f08rs_f08_relative_strength_sortinotopq_base_v037_signal,
    f08rs_f08_relative_strength_ulcerstrength_252d_base_v038_signal,
    f08rs_f08_relative_strength_maxddstrength_504d_base_v039_signal,
    f08rs_f08_relative_strength_downshare_252d_base_v040_signal,
    f08rs_f08_relative_strength_blendriskrank_base_v041_signal,
    f08rs_f08_relative_strength_riskrankdisp_base_v042_signal,
    f08rs_f08_relative_strength_sharpehorizdisp_base_v043_signal,
    f08rs_f08_relative_strength_sharpetanh_63d_base_v044_signal,
    f08rs_f08_relative_strength_calmartanh_504d_base_v045_signal,
    f08rs_f08_relative_strength_sortinoyoy_base_v046_signal,
    f08rs_f08_relative_strength_calmaryoy_base_v047_signal,
    f08rs_f08_relative_strength_sortinosmrank_base_v048_signal,
    f08rs_f08_relative_strength_martinctr_base_v049_signal,
    f08rs_f08_relative_strength_sharperankstab_base_v050_signal,
    f08rs_f08_relative_strength_sharpeconsist_base_v051_signal,
    f08rs_f08_relative_strength_sortinotrendnoise_base_v052_signal,
    f08rs_f08_relative_strength_calmartrendnoise_base_v053_signal,
    f08rs_f08_relative_strength_sharpe_1260d_base_v054_signal,
    f08rs_f08_relative_strength_sortinodeepspr_base_v055_signal,
    f08rs_f08_relative_strength_martindeeprank_base_v056_signal,
    f08rs_f08_relative_strength_calmar_1260d_base_v057_signal,
    f08rs_f08_relative_strength_sharpecalmarjoint_base_v058_signal,
    f08rs_f08_relative_strength_sortinogtpjoint_base_v059_signal,
    f08rs_f08_relative_strength_sortinoregimevel_base_v060_signal,
    f08rs_f08_relative_strength_painrank_base_v061_signal,
    f08rs_f08_relative_strength_sharpemartindiff_504d_base_v062_signal,
    f08rs_f08_relative_strength_fastsharperank_base_v063_signal,
    f08rs_f08_relative_strength_fastgtprank_base_v064_signal,
    f08rs_f08_relative_strength_ulcermom_base_v065_signal,
    f08rs_f08_relative_strength_ddvolunits_base_v066_signal,
    f08rs_f08_relative_strength_calmariqr_deep_base_v067_signal,
    f08rs_f08_relative_strength_sortinoiqr_252d_base_v068_signal,
    f08rs_f08_relative_strength_sharpesortinodiff_126d_base_v069_signal,
    f08rs_f08_relative_strength_gtpctr_base_v070_signal,
    f08rs_f08_relative_strength_martinrankvel_base_v071_signal,
    f08rs_f08_relative_strength_calmarposyear_base_v072_signal,
    f08rs_f08_relative_strength_sharpedeepregimetime_base_v073_signal,
    f08rs_f08_relative_strength_sortinoctr_base_v074_signal,
    f08rs_f08_relative_strength_composite_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F08_RELATIVE_STRENGTH_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    ALLOW = {
        "open", "high", "low", "close", "closeadj", "volume",
        "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc", "opex",
        "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc",
        "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff",
        "ncfi", "ncfcommon", "ncfdebt", "ncfbus", "capex", "depamor", "sharesbas",
        "shareswa", "shareswadil", "assets", "assetsc", "tangibles", "intangibles",
        "ppnenet", "investments", "inventory", "receivables", "payables", "equity",
        "retearn", "workingcapital", "debt", "debtc", "debtnc", "liabilities",
        "liabilitiesc", "cashneq", "currentratio", "roic", "roe", "roa", "ros",
        "assetturnover", "invcap", "intexp", "taxexp", "ebt", "sps", "bvps", "de",
        "ncfdiv", "dps", "divyield", "payoutratio", "prefdivis",
        "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
        "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal",
        "fndholders", "undholders", "prfholders", "dbtholders", "putholders",
        "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue", "dbtvalue",
    }

    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0004, 0.032, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")

    cols = {"closeadj": closeadj}

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

    print("OK f08_relative_strength_base_001_075_claude: %d features pass" % n_features)
