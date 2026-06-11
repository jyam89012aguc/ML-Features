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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


# ===== folder domain primitives (hit-driven volatility / lumpiness) =====
def _f38hv_cv(s, w):
    # coefficient of variation of level: dispersion / mean (level spikiness)
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return sd / m.replace(0, np.nan)


def _f38hv_logret(s):
    return np.log(s.replace(0, np.nan)).diff()


def _f38hv_relret(s):
    return s / s.shift(1).replace(0, np.nan) - 1.0


def _f38hv_burst(s, w):
    # current level vs trailing-window mean (burst above baseline)
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    return s / m.replace(0, np.nan) - 1.0


def _f38hv_amp(s, w):
    # amplitude: rolling (max-min) normalized by mean of |level|
    hi = s.rolling(w, min_periods=max(1, w // 2)).max()
    lo = s.rolling(w, min_periods=max(1, w // 2)).min()
    sc = s.abs().rolling(w, min_periods=max(1, w // 2)).mean()
    return (hi - lo) / sc.replace(0, np.nan)


def _f38hv_swing(s, w):
    # peak-to-trough swing of a signed series scaled by its rolling std
    hi = s.rolling(w, min_periods=max(1, w // 2)).max()
    lo = s.rolling(w, min_periods=max(1, w // 2)).min()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (hi - lo) / sd.replace(0, np.nan)


def _f38hv_decay(s, w):
    # post-hit decay: how far below the trailing peak the level has fallen
    hi = s.rolling(w, min_periods=max(1, w // 2)).max()
    return s / hi.replace(0, np.nan) - 1.0


def _f38hv_conc(s, w):
    # concentration: share of window |total| contributed by the single max day
    tot = s.abs().rolling(w, min_periods=max(1, w // 2)).sum()
    mx = s.abs().rolling(w, min_periods=max(1, w // 2)).max()
    return mx / tot.replace(0, np.nan)



# revvol 21d slope (1st derivative, ROC 7d)
def f38hv_f38_hit_driven_volatility_revvol_21d_slope_v001_signal(revenue):
    lr = _f38hv_logret(revenue)
    x = lr.rolling(21, min_periods=10).std()
    d1 = x - x.shift(7)
    b = d1 / 7.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revvol 63d slope (1st derivative, ROC 21d)
def f38hv_f38_hit_driven_volatility_revvol_63d_slope_v002_signal(revenue):
    lr = _f38hv_logret(revenue)
    x = lr.rolling(63, min_periods=21).std()
    d1 = x - x.shift(21)
    b = d1 / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revvol 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_revvol_126d_slope_v003_signal(revenue):
    lr = _f38hv_logret(revenue)
    x = lr.rolling(126, min_periods=63).std()
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revvol 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_revvol_252d_slope_v004_signal(revenue):
    lr = _f38hv_logret(revenue)
    x = lr.rolling(252, min_periods=126).std()
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revcv 63d slope (1st derivative, ROC 21d)
def f38hv_f38_hit_driven_volatility_revcv_63d_slope_v005_signal(revenue):
    x = _f38hv_cv(revenue, 63)
    d1 = x - x.shift(21)
    b = d1 / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revcv 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_revcv_126d_slope_v006_signal(revenue):
    x = _f38hv_cv(revenue, 126)
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revcv 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_revcv_252d_slope_v007_signal(revenue):
    x = _f38hv_cv(revenue, 252)
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revburst 63d slope (1st derivative, ROC 21d)
def f38hv_f38_hit_driven_volatility_revburst_63d_slope_v008_signal(revenue):
    x = _f38hv_burst(revenue, 63)
    d1 = x - x.shift(21)
    b = d1 / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revburst 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_revburst_126d_slope_v009_signal(revenue):
    x = _f38hv_burst(revenue, 126)
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revburst 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_revburst_252d_slope_v010_signal(revenue):
    x = _f38hv_burst(revenue, 252)
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revdecay 63d slope (1st derivative, ROC 21d)
def f38hv_f38_hit_driven_volatility_revdecay_63d_slope_v011_signal(revenue):
    x = _f38hv_decay(revenue, 63)
    d1 = x - x.shift(21)
    b = d1 / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revdecay 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_revdecay_126d_slope_v012_signal(revenue):
    x = _f38hv_decay(revenue, 126)
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revdecay 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_revdecay_252d_slope_v013_signal(revenue):
    x = _f38hv_decay(revenue, 252)
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revamp 63d slope (1st derivative, ROC 21d)
def f38hv_f38_hit_driven_volatility_revamp_63d_slope_v014_signal(revenue):
    x = _f38hv_amp(revenue, 63)
    d1 = x - x.shift(21)
    b = d1 / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revamp 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_revamp_126d_slope_v015_signal(revenue):
    x = _f38hv_amp(revenue, 126)
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revamp 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_revamp_252d_slope_v016_signal(revenue):
    x = _f38hv_amp(revenue, 252)
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revherf 63d slope (1st derivative, ROC 21d)
def f38hv_f38_hit_driven_volatility_revherf_63d_slope_v017_signal(revenue):
    g = _f38hv_relret(revenue).clip(lower=0)
    tot = g.rolling(63, min_periods=21).sum()
    sq = (g * g).rolling(63, min_periods=21).sum()
    x = sq / (tot * tot).replace(0, np.nan)
    d1 = x - x.shift(21)
    b = d1 / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revherf 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_revherf_126d_slope_v018_signal(revenue):
    g = _f38hv_relret(revenue).clip(lower=0)
    tot = g.rolling(126, min_periods=63).sum()
    sq = (g * g).rolling(126, min_periods=63).sum()
    x = sq / (tot * tot).replace(0, np.nan)
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revherf 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_revherf_252d_slope_v019_signal(revenue):
    g = _f38hv_relret(revenue).clip(lower=0)
    tot = g.rolling(252, min_periods=126).sum()
    sq = (g * g).rolling(252, min_periods=126).sum()
    x = sq / (tot * tot).replace(0, np.nan)
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# niswing 63d slope (1st derivative, ROC 21d)
def f38hv_f38_hit_driven_volatility_niswing_63d_slope_v020_signal(netinc):
    x = _f38hv_swing(netinc, 63)
    d1 = x - x.shift(21)
    b = d1 / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# niswing 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_niswing_126d_slope_v021_signal(netinc):
    x = _f38hv_swing(netinc, 126)
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# niswing 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_niswing_252d_slope_v022_signal(netinc):
    x = _f38hv_swing(netinc, 252)
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# niamp 63d slope (1st derivative, ROC 21d)
def f38hv_f38_hit_driven_volatility_niamp_63d_slope_v023_signal(netinc):
    x = _f38hv_amp(netinc, 63)
    d1 = x - x.shift(21)
    b = d1 / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# niamp 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_niamp_126d_slope_v024_signal(netinc):
    x = _f38hv_amp(netinc, 126)
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# niamp 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_niamp_252d_slope_v025_signal(netinc):
    x = _f38hv_amp(netinc, 252)
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ebitswing 63d slope (1st derivative, ROC 21d)
def f38hv_f38_hit_driven_volatility_ebitswing_63d_slope_v026_signal(ebit):
    x = _f38hv_swing(ebit, 63)
    d1 = x - x.shift(21)
    b = d1 / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ebitswing 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_ebitswing_126d_slope_v027_signal(ebit):
    x = _f38hv_swing(ebit, 126)
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ebitswing 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_ebitswing_252d_slope_v028_signal(ebit):
    x = _f38hv_swing(ebit, 252)
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ebitamp 63d slope (1st derivative, ROC 21d)
def f38hv_f38_hit_driven_volatility_ebitamp_63d_slope_v029_signal(ebit):
    x = _f38hv_amp(ebit, 63)
    d1 = x - x.shift(21)
    b = d1 / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ebitamp 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_ebitamp_126d_slope_v030_signal(ebit):
    x = _f38hv_amp(ebit, 126)
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ebitamp 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_ebitamp_252d_slope_v031_signal(ebit):
    x = _f38hv_amp(ebit, 252)
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# opswing 63d slope (1st derivative, ROC 21d)
def f38hv_f38_hit_driven_volatility_opswing_63d_slope_v032_signal(opinc):
    x = _f38hv_swing(opinc, 63)
    d1 = x - x.shift(21)
    b = d1 / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# opswing 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_opswing_126d_slope_v033_signal(opinc):
    x = _f38hv_swing(opinc, 126)
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# opswing 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_opswing_252d_slope_v034_signal(opinc):
    x = _f38hv_swing(opinc, 252)
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# opamp 63d slope (1st derivative, ROC 21d)
def f38hv_f38_hit_driven_volatility_opamp_63d_slope_v035_signal(opinc):
    x = _f38hv_amp(opinc, 63)
    d1 = x - x.shift(21)
    b = d1 / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# opamp 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_opamp_126d_slope_v036_signal(opinc):
    x = _f38hv_amp(opinc, 126)
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gmburst 63d slope (1st derivative, ROC 21d)
def f38hv_f38_hit_driven_volatility_gmburst_63d_slope_v037_signal(grossmargin):
    x = grossmargin - _mean(grossmargin, 63)
    d1 = x - x.shift(21)
    b = d1 / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gmburst 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_gmburst_126d_slope_v038_signal(grossmargin):
    x = grossmargin - _mean(grossmargin, 126)
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gmburst 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_gmburst_252d_slope_v039_signal(grossmargin):
    x = grossmargin - _mean(grossmargin, 252)
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gmvol 63d slope (1st derivative, ROC 21d)
def f38hv_f38_hit_driven_volatility_gmvol_63d_slope_v040_signal(grossmargin):
    x = _std(grossmargin, 63)
    d1 = x - x.shift(21)
    b = d1 / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gmvol 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_gmvol_126d_slope_v041_signal(grossmargin):
    x = _std(grossmargin, 126)
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gmvol 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_gmvol_252d_slope_v042_signal(grossmargin):
    x = _std(grossmargin, 252)
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revrz 63d slope (1st derivative, ROC 21d)
def f38hv_f38_hit_driven_volatility_revrz_63d_slope_v043_signal(revenue):
    med = revenue.rolling(63, min_periods=21).median()
    iqr = (revenue.rolling(63, min_periods=21).quantile(0.75) - revenue.rolling(63, min_periods=21).quantile(0.25))
    x = (revenue - med) / iqr.replace(0, np.nan)
    d1 = x - x.shift(21)
    b = d1 / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revrz 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_revrz_126d_slope_v044_signal(revenue):
    med = revenue.rolling(126, min_periods=63).median()
    iqr = (revenue.rolling(126, min_periods=63).quantile(0.75) - revenue.rolling(126, min_periods=63).quantile(0.25))
    x = (revenue - med) / iqr.replace(0, np.nan)
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revrz 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_revrz_252d_slope_v045_signal(revenue):
    med = revenue.rolling(252, min_periods=126).median()
    iqr = (revenue.rolling(252, min_periods=126).quantile(0.75) - revenue.rolling(252, min_periods=126).quantile(0.25))
    x = (revenue - med) / iqr.replace(0, np.nan)
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revsemi 63d slope (1st derivative, ROC 21d)
def f38hv_f38_hit_driven_volatility_revsemi_63d_slope_v046_signal(revenue):
    lr = _f38hv_relret(revenue)
    up = lr.where(lr > 0).rolling(63, min_periods=15).std()
    dn = lr.where(lr < 0).rolling(63, min_periods=15).std()
    x = up - dn
    d1 = x - x.shift(21)
    b = d1 / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revsemi 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_revsemi_126d_slope_v047_signal(revenue):
    lr = _f38hv_relret(revenue)
    up = lr.where(lr > 0).rolling(126, min_periods=30).std()
    dn = lr.where(lr < 0).rolling(126, min_periods=30).std()
    x = up - dn
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revvov 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_revvov_126d_slope_v048_signal(revenue):
    lr = _f38hv_logret(revenue)
    v = lr.rolling(21, min_periods=10).std()
    x = v.rolling(126, min_periods=63).std()
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revvov 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_revvov_252d_slope_v049_signal(revenue):
    lr = _f38hv_logret(revenue)
    v = lr.rolling(21, min_periods=10).std()
    x = v.rolling(252, min_periods=126).std()
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revterm 63d slope (1st derivative, ROC 21d)
def f38hv_f38_hit_driven_volatility_revterm_63d_slope_v050_signal(revenue):
    lr = _f38hv_logret(revenue)
    vs = lr.rolling(21, min_periods=10).std()
    vl = lr.rolling(126, min_periods=63).std()
    x = vs / vl.replace(0, np.nan)
    d1 = x - x.shift(21)
    b = d1 / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revterm 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_revterm_126d_slope_v051_signal(revenue):
    lr = _f38hv_logret(revenue)
    vs = lr.rolling(63, min_periods=21).std()
    vl = lr.rolling(252, min_periods=126).std()
    x = vs / vl.replace(0, np.nan)
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revspk 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_revspk_126d_slope_v052_signal(revenue):
    lr = _f38hv_logret(revenue)
    z = (lr - lr.rolling(126, min_periods=63).mean()) / lr.rolling(126, min_periods=63).std().replace(0, np.nan)
    exc = (z.abs() - 1.5).clip(lower=0) ** 2
    x = exc.rolling(126, min_periods=63).mean()
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revspk 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_revspk_252d_slope_v053_signal(revenue):
    lr = _f38hv_logret(revenue)
    z = (lr - lr.rolling(252, min_periods=126).mean()) / lr.rolling(252, min_periods=126).std().replace(0, np.nan)
    exc = (z.abs() - 1.5).clip(lower=0) ** 2
    x = exc.rolling(252, min_periods=126).mean()
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# niflip 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_niflip_126d_slope_v054_signal(netinc):
    sg = np.sign(netinc)
    fl = (sg != sg.shift(1)).astype(float)
    w = fl * netinc.diff().abs()
    x = w.rolling(126, min_periods=63).mean()
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# niflip 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_niflip_252d_slope_v055_signal(netinc):
    sg = np.sign(netinc)
    fl = (sg != sg.shift(1)).astype(float)
    w = fl * netinc.diff().abs()
    x = w.rolling(252, min_periods=126).mean()
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ebitloss 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_ebitloss_126d_slope_v056_signal(ebit):
    x = (ebit < 0).astype(float).rolling(126, min_periods=63).mean()
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ebitloss 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_ebitloss_252d_slope_v057_signal(ebit):
    x = (ebit < 0).astype(float).rolling(252, min_periods=126).mean()
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revac 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_revac_126d_slope_v058_signal(revenue):
    lr = _f38hv_relret(revenue)
    x = lr.rolling(126, min_periods=63).corr(lr.shift(1))
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revac 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_revac_252d_slope_v059_signal(revenue):
    lr = _f38hv_relret(revenue)
    x = lr.rolling(252, min_periods=126).corr(lr.shift(1))
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revkurt 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_revkurt_126d_slope_v060_signal(revenue):
    lr = _f38hv_logret(revenue)
    x = lr.rolling(126, min_periods=63).kurt()
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revkurt 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_revkurt_252d_slope_v061_signal(revenue):
    lr = _f38hv_logret(revenue)
    x = lr.rolling(252, min_periods=126).kurt()
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revskew 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_revskew_126d_slope_v062_signal(revenue):
    lr = _f38hv_logret(revenue)
    x = lr.rolling(126, min_periods=63).skew()
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revskew 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_revskew_252d_slope_v063_signal(revenue):
    lr = _f38hv_logret(revenue)
    x = lr.rolling(252, min_periods=126).skew()
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# nikurt 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_nikurt_126d_slope_v064_signal(netinc):
    d = netinc.diff()
    x = d.rolling(126, min_periods=63).kurt()
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# niskew 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_niskew_252d_slope_v065_signal(netinc):
    d = netinc.diff()
    x = d.rolling(252, min_periods=126).skew()
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# hitmarg 63d slope (1st derivative, ROC 21d)
def f38hv_f38_hit_driven_volatility_hitmarg_63d_slope_v066_signal(revenue, grossmargin):
    rb = _f38hv_burst(revenue, 63)
    gd = grossmargin - _mean(grossmargin, 63)
    x = rb * gd
    d1 = x - x.shift(21)
    b = d1 / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# hitmarg 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_hitmarg_126d_slope_v067_signal(revenue, grossmargin):
    rb = _f38hv_burst(revenue, 126)
    gd = grossmargin - _mean(grossmargin, 126)
    x = rb * gd
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# opleva 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_opleva_126d_slope_v068_signal(ebit, revenue):
    es = _f38hv_amp(ebit, 126)
    rs = _f38hv_amp(revenue, 126)
    x = es / rs.replace(0, np.nan)
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# opleva 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_opleva_252d_slope_v069_signal(ebit, revenue):
    es = _f38hv_amp(ebit, 252)
    rs = _f38hv_amp(revenue, 252)
    x = es / rs.replace(0, np.nan)
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# nileva 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_nileva_126d_slope_v070_signal(netinc, revenue):
    ns = _f38hv_amp(netinc, 126)
    rs = _f38hv_amp(revenue, 126)
    x = ns / rs.replace(0, np.nan)
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# nileva 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_nileva_252d_slope_v071_signal(netinc, revenue):
    ns = _f38hv_amp(netinc, 252)
    rs = _f38hv_amp(revenue, 252)
    x = ns / rs.replace(0, np.nan)
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# opburst 63d slope (1st derivative, ROC 21d)
def f38hv_f38_hit_driven_volatility_opburst_63d_slope_v072_signal(opinc):
    x = (opinc - _mean(opinc, 63)) / _std(opinc, 63)
    d1 = x - x.shift(21)
    b = d1 / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# opburst 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_opburst_126d_slope_v073_signal(opinc):
    x = (opinc - _mean(opinc, 126)) / _std(opinc, 126)
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revuw 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_revuw_126d_slope_v074_signal(revenue):
    hi = _rmax(revenue, 126)
    uw = (1.0 - revenue / hi.replace(0, np.nan)).clip(lower=0)
    x = uw.rolling(126, min_periods=63).mean()
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revuw 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_revuw_252d_slope_v075_signal(revenue):
    hi = _rmax(revenue, 252)
    uw = (1.0 - revenue / hi.replace(0, np.nan)).clip(lower=0)
    x = uw.rolling(252, min_periods=126).mean()
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revrng 63d slope (1st derivative, ROC 21d)
def f38hv_f38_hit_driven_volatility_revrng_63d_slope_v076_signal(revenue):
    x = revenue.rolling(63, min_periods=21).rank(pct=True) - 0.5
    d1 = x - x.shift(21)
    b = d1 / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revrng 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_revrng_252d_slope_v077_signal(revenue):
    x = revenue.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revmaxg 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_revmaxg_126d_slope_v078_signal(revenue):
    lr = _f38hv_relret(revenue)
    x = lr.rolling(126, min_periods=63).quantile(0.90)
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revmaxg 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_revmaxg_252d_slope_v079_signal(revenue):
    lr = _f38hv_relret(revenue)
    x = lr.rolling(252, min_periods=126).quantile(0.90)
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revming 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_revming_126d_slope_v080_signal(revenue):
    lr = _f38hv_relret(revenue)
    x = lr.rolling(126, min_periods=63).quantile(0.10)
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gmamp 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_gmamp_126d_slope_v081_signal(grossmargin):
    x = _f38hv_amp(grossmargin, 126)
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gmamp 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_gmamp_252d_slope_v082_signal(grossmargin):
    x = _f38hv_amp(grossmargin, 252)
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gmclust 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_gmclust_126d_slope_v083_signal(grossmargin):
    a = grossmargin.diff().abs()
    x = a.rolling(126, min_periods=63).corr(a.shift(1))
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# nicv 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_nicv_126d_slope_v084_signal(netinc):
    m = _mean(netinc, 126)
    sd = _std(netinc, 126)
    x = sd / m.abs().replace(0, np.nan)
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# nicv 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_nicv_252d_slope_v085_signal(netinc):
    m = _mean(netinc, 252)
    sd = _std(netinc, 252)
    x = sd / m.abs().replace(0, np.nan)
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ebitcv 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_ebitcv_126d_slope_v086_signal(ebit):
    m = _mean(ebit, 126)
    sd = _std(ebit, 126)
    x = sd / m.abs().replace(0, np.nan)
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ebitcv 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_ebitcv_252d_slope_v087_signal(ebit):
    m = _mean(ebit, 252)
    sd = _std(ebit, 252)
    x = sd / m.abs().replace(0, np.nan)
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revburstsm 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_revburstsm_126d_slope_v088_signal(revenue):
    rb = _f38hv_burst(revenue, 126)
    x = rb.ewm(span=42, min_periods=21).mean()
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revburstsm 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_revburstsm_252d_slope_v089_signal(revenue):
    rb = _f38hv_burst(revenue, 252)
    x = rb.ewm(span=63, min_periods=31).mean()
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revcvrank 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_revcvrank_252d_slope_v090_signal(revenue):
    cv = _f38hv_cv(revenue, 63)
    x = cv.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revburstrank 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_revburstrank_252d_slope_v091_signal(revenue):
    rb = _f38hv_burst(revenue, 63)
    x = rb.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# eargear 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_eargear_126d_slope_v092_signal(netinc, revenue):
    ns = _std(netinc, 126)
    x = ns / _mean(revenue, 126).replace(0, np.nan)
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# eargear 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_eargear_252d_slope_v093_signal(ebit, revenue):
    es = _std(ebit, 252)
    x = es / _mean(revenue, 252).replace(0, np.nan)
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revfade 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_revfade_126d_slope_v094_signal(revenue):
    hi = _rmax(revenue, 126)
    fade = (hi - revenue) / hi.replace(0, np.nan)
    x = fade.rolling(63, min_periods=21).mean()
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revfade 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_revfade_252d_slope_v095_signal(revenue):
    hi = _rmax(revenue, 252)
    fade = (hi - revenue) / hi.replace(0, np.nan)
    x = fade.rolling(126, min_periods=63).mean()
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# opclust 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_opclust_126d_slope_v096_signal(opinc):
    a = opinc.diff().abs()
    x = a.rolling(126, min_periods=63).corr(a.shift(1))
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# opclust 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_opclust_252d_slope_v097_signal(opinc):
    a = opinc.diff().abs()
    x = a.rolling(252, min_periods=126).corr(a.shift(1))
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# niclust 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_niclust_126d_slope_v098_signal(netinc):
    a = netinc.diff().abs()
    x = a.rolling(126, min_periods=63).corr(a.shift(1))
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# niclust 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_niclust_252d_slope_v099_signal(netinc):
    a = netinc.diff().abs()
    x = a.rolling(252, min_periods=126).corr(a.shift(1))
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ebitclust 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_ebitclust_126d_slope_v100_signal(ebit):
    a = ebit.diff().abs()
    x = a.rolling(126, min_periods=63).corr(a.shift(1))
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ebitclust 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_ebitclust_252d_slope_v101_signal(ebit):
    a = ebit.diff().abs()
    x = a.rolling(252, min_periods=126).corr(a.shift(1))
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revmad 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_revmad_126d_slope_v102_signal(revenue):
    lr = _f38hv_relret(revenue)
    md = (lr - lr.rolling(126, min_periods=63).median()).abs()
    x = md.rolling(126, min_periods=63).median()
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revmad 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_revmad_252d_slope_v103_signal(revenue):
    lr = _f38hv_relret(revenue)
    md = (lr - lr.rolling(252, min_periods=126).median()).abs()
    x = md.rolling(252, min_periods=126).median()
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gmspk 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_gmspk_252d_slope_v104_signal(grossmargin):
    z = (grossmargin - _mean(grossmargin, 252)) / _std(grossmargin, 252)
    x = (z > 1.5).astype(float).rolling(252, min_periods=126).mean()
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gmz 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_gmz_126d_slope_v105_signal(grossmargin):
    x = _z(grossmargin, 126)
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gmskew 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_gmskew_252d_slope_v106_signal(grossmargin):
    lr = grossmargin.diff()
    x = lr.rolling(252, min_periods=126).skew()
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revphase 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_revphase_126d_slope_v107_signal(revenue):
    rb = _f38hv_burst(revenue, 126).clip(lower=0)
    dc = (-_f38hv_decay(revenue, 126)).clip(lower=0)
    x = (rb - dc) / (rb + dc + 1e-9)
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revphase 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_revphase_252d_slope_v108_signal(revenue):
    rb = _f38hv_burst(revenue, 252).clip(lower=0)
    dc = (-_f38hv_decay(revenue, 252)).clip(lower=0)
    x = (rb - dc) / (rb + dc + 1e-9)
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ebitburst 63d slope (1st derivative, ROC 21d)
def f38hv_f38_hit_driven_volatility_ebitburst_63d_slope_v109_signal(ebit):
    x = (ebit - _mean(ebit, 63)) / _std(ebit, 63)
    d1 = x - x.shift(21)
    b = d1 / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ebitburst 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_ebitburst_126d_slope_v110_signal(ebit):
    x = (ebit - _mean(ebit, 126)) / _std(ebit, 126)
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# niburst 63d slope (1st derivative, ROC 21d)
def f38hv_f38_hit_driven_volatility_niburst_63d_slope_v111_signal(netinc):
    x = (netinc - _mean(netinc, 63)) / _std(netinc, 63)
    d1 = x - x.shift(21)
    b = d1 / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# niburst 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_niburst_126d_slope_v112_signal(netinc):
    x = (netinc - _mean(netinc, 126)) / _std(netinc, 126)
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revvolacc 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_revvolacc_126d_slope_v113_signal(revenue):
    lr = _f38hv_logret(revenue)
    v = lr.rolling(63, min_periods=21).std()
    x = v - v.shift(63)
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revvolacc 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_revvolacc_252d_slope_v114_signal(revenue):
    lr = _f38hv_logret(revenue)
    v = lr.rolling(126, min_periods=63).std()
    x = v - v.shift(126)
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# hitcomp 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_hitcomp_126d_slope_v115_signal(revenue, netinc):
    rc = _f38hv_cv(revenue, 126)
    ns = _f38hv_swing(netinc, 126)
    x = rc * ns
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# hitcomp 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_hitcomp_252d_slope_v116_signal(revenue, ebit):
    rc = _f38hv_cv(revenue, 252)
    es = _f38hv_swing(ebit, 252)
    x = rc * es
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revcliff 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_revcliff_126d_slope_v117_signal(revenue):
    lr = _f38hv_relret(revenue)
    neg = (-lr).clip(lower=0)
    x = neg.rolling(126, min_periods=63).mean()
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revcliff 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_revcliff_252d_slope_v118_signal(revenue):
    lr = _f38hv_relret(revenue)
    neg = (-lr).clip(lower=0)
    x = neg.rolling(252, min_periods=126).mean()
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# opcv 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_opcv_126d_slope_v119_signal(opinc):
    m = _mean(opinc, 126)
    sd = _std(opinc, 126)
    x = sd / m.abs().replace(0, np.nan)
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# opcv 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_opcv_252d_slope_v120_signal(opinc):
    m = _mean(opinc, 252)
    sd = _std(opinc, 252)
    x = sd / m.abs().replace(0, np.nan)
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revvolz 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_revvolz_252d_slope_v121_signal(revenue):
    lr = _f38hv_logret(revenue)
    v = lr.rolling(63, min_periods=21).std()
    x = _z(v, 252)
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# earampratio 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_earampratio_252d_slope_v122_signal(netinc, ebit):
    ns = _f38hv_amp(netinc, 252)
    es = _f38hv_amp(ebit, 252)
    x = ns - es
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revhits 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_revhits_252d_slope_v123_signal(revenue):
    rb = _f38hv_burst(revenue, 63)
    amt = (rb - 0.25).clip(lower=0)
    x = amt.rolling(252, min_periods=126).mean()
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revhits 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_revhits_126d_slope_v124_signal(revenue):
    rb = _f38hv_burst(revenue, 63)
    amt = (rb - 0.25).clip(lower=0)
    x = amt.rolling(126, min_periods=63).mean()
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gmonhit 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_gmonhit_252d_slope_v125_signal(grossmargin, revenue):
    rb = _f38hv_burst(revenue, 63)
    cond = grossmargin.where(rb > 0.1)
    x = cond.rolling(252, min_periods=63).mean() - _mean(grossmargin, 252)
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revlrng 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_revlrng_126d_slope_v126_signal(revenue):
    x = np.log(_rmax(revenue, 126).replace(0, np.nan) / _rmin(revenue, 126).replace(0, np.nan))
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revlrng 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_revlrng_252d_slope_v127_signal(revenue):
    x = np.log(_rmax(revenue, 252).replace(0, np.nan) / _rmin(revenue, 252).replace(0, np.nan))
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# niasym 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_niasym_126d_slope_v128_signal(netinc):
    d = netinc.diff()
    up = d.where(d > 0).rolling(126, min_periods=30).mean()
    dn = (-d.where(d < 0)).rolling(126, min_periods=30).mean()
    x = (up - dn) / (up + dn).replace(0, np.nan)
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# niasym 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_niasym_252d_slope_v129_signal(netinc):
    d = netinc.diff()
    up = d.where(d > 0).rolling(252, min_periods=60).mean()
    dn = (-d.where(d < 0)).rolling(252, min_periods=60).mean()
    x = (up - dn) / (up + dn).replace(0, np.nan)
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ebitdown 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_ebitdown_252d_slope_v130_signal(ebit):
    x = (_mean(ebit, 252) - _rmin(ebit, 252)) / _std(ebit, 252)
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revdsemi 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_revdsemi_252d_slope_v131_signal(revenue):
    lr = _f38hv_relret(revenue)
    x = lr.where(lr < 0).rolling(252, min_periods=63).std()
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revusemi 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_revusemi_252d_slope_v132_signal(revenue):
    lr = _f38hv_relret(revenue)
    x = lr.where(lr > 0).rolling(252, min_periods=63).std()
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revlife 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_revlife_252d_slope_v133_signal(revenue):
    rb = _f38hv_burst(revenue, 126).clip(lower=0)
    dc = (-_f38hv_decay(revenue, 126)).clip(lower=0)
    raw = (rb - dc) / (rb + dc + 1e-9)
    x = raw.ewm(span=63, min_periods=31).mean()
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# earvolr 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_earvolr_252d_slope_v134_signal(netinc, opinc):
    nv = _std(netinc, 252)
    ov = _std(opinc, 252)
    x = nv / ov.replace(0, np.nan)
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revspkpers 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_revspkpers_252d_slope_v135_signal(revenue):
    a = _f38hv_relret(revenue).abs()
    x = a.rolling(252, min_periods=126).corr(a.shift(5))
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gmrevco 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_gmrevco_252d_slope_v136_signal(grossmargin, revenue):
    rr = _f38hv_relret(revenue)
    gd = grossmargin.diff()
    x = rr.rolling(252, min_periods=126).corr(gd)
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revampz 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_revampz_252d_slope_v137_signal(revenue):
    ap = _f38hv_amp(revenue, 63)
    x = _z(ap, 252)
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# niswingz 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_niswingz_252d_slope_v138_signal(netinc):
    sw = _f38hv_swing(netinc, 63)
    x = _z(sw, 252)
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# opburstrank 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_opburstrank_252d_slope_v139_signal(opinc):
    ob = (opinc - _mean(opinc, 63)) / _std(opinc, 63)
    x = ob.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ebitburstrank 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_ebitburstrank_252d_slope_v140_signal(ebit):
    eb = (ebit - _mean(ebit, 63)) / _std(ebit, 63)
    x = eb.rolling(252, min_periods=126).rank(pct=True) - 0.5
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revampvol 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_revampvol_252d_slope_v141_signal(revenue):
    ap = _f38hv_amp(revenue, 21)
    x = ap.rolling(252, min_periods=126).std()
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revampvol 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_revampvol_126d_slope_v142_signal(revenue):
    ap = _f38hv_amp(revenue, 21)
    x = ap.rolling(126, min_periods=63).std()
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gmchgskew 126d slope (1st derivative, ROC 42d)
def f38hv_f38_hit_driven_volatility_gmchgskew_126d_slope_v143_signal(grossmargin):
    d = grossmargin.diff()
    x = d.rolling(126, min_periods=63).skew()
    d1 = x - x.shift(42)
    b = d1 / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gmchgvol 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_gmchgvol_252d_slope_v144_signal(grossmargin):
    d = grossmargin.diff()
    x = d.abs().rolling(252, min_periods=126).mean()
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revtail 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_revtail_252d_slope_v145_signal(revenue):
    lr = _f38hv_relret(revenue)
    q95 = lr.rolling(252, min_periods=126).quantile(0.95)
    q50 = lr.rolling(252, min_periods=126).quantile(0.50)
    x = q95 - q50
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# earswingmix 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_earswingmix_252d_slope_v146_signal(netinc, ebit):
    ns = _f38hv_swing(netinc, 126)
    es = _f38hv_swing(ebit, 126)
    x = (ns + es) / 2.0
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revqspr 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_revqspr_252d_slope_v147_signal(revenue):
    lr = _f38hv_relret(revenue)
    q90 = lr.rolling(252, min_periods=126).quantile(0.90)
    q10 = lr.rolling(252, min_periods=126).quantile(0.10)
    x = q90 - q10
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# opgear 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_opgear_252d_slope_v148_signal(opinc, revenue):
    os = _std(opinc, 252)
    x = os / _mean(revenue, 252).replace(0, np.nan)
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# nidown 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_nidown_252d_slope_v149_signal(netinc):
    x = (_mean(netinc, 252) - _rmin(netinc, 252)) / _std(netinc, 252)
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revrngspr 252d slope (1st derivative, ROC 84d)
def f38hv_f38_hit_driven_volatility_revrngspr_252d_slope_v150_signal(revenue):
    hi_s = _rmax(revenue, 63)
    lo_s = _rmin(revenue, 63)
    ps = (revenue - lo_s) / (hi_s - lo_s).replace(0, np.nan)
    hi_l = _rmax(revenue, 252)
    lo_l = _rmin(revenue, 252)
    pl = (revenue - lo_l) / (hi_l - lo_l).replace(0, np.nan)
    x = ps - pl
    d1 = x - x.shift(84)
    b = d1 / 84.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f38hv_f38_hit_driven_volatility_revvol_21d_slope_v001_signal,
    f38hv_f38_hit_driven_volatility_revvol_63d_slope_v002_signal,
    f38hv_f38_hit_driven_volatility_revvol_126d_slope_v003_signal,
    f38hv_f38_hit_driven_volatility_revvol_252d_slope_v004_signal,
    f38hv_f38_hit_driven_volatility_revcv_63d_slope_v005_signal,
    f38hv_f38_hit_driven_volatility_revcv_126d_slope_v006_signal,
    f38hv_f38_hit_driven_volatility_revcv_252d_slope_v007_signal,
    f38hv_f38_hit_driven_volatility_revburst_63d_slope_v008_signal,
    f38hv_f38_hit_driven_volatility_revburst_126d_slope_v009_signal,
    f38hv_f38_hit_driven_volatility_revburst_252d_slope_v010_signal,
    f38hv_f38_hit_driven_volatility_revdecay_63d_slope_v011_signal,
    f38hv_f38_hit_driven_volatility_revdecay_126d_slope_v012_signal,
    f38hv_f38_hit_driven_volatility_revdecay_252d_slope_v013_signal,
    f38hv_f38_hit_driven_volatility_revamp_63d_slope_v014_signal,
    f38hv_f38_hit_driven_volatility_revamp_126d_slope_v015_signal,
    f38hv_f38_hit_driven_volatility_revamp_252d_slope_v016_signal,
    f38hv_f38_hit_driven_volatility_revherf_63d_slope_v017_signal,
    f38hv_f38_hit_driven_volatility_revherf_126d_slope_v018_signal,
    f38hv_f38_hit_driven_volatility_revherf_252d_slope_v019_signal,
    f38hv_f38_hit_driven_volatility_niswing_63d_slope_v020_signal,
    f38hv_f38_hit_driven_volatility_niswing_126d_slope_v021_signal,
    f38hv_f38_hit_driven_volatility_niswing_252d_slope_v022_signal,
    f38hv_f38_hit_driven_volatility_niamp_63d_slope_v023_signal,
    f38hv_f38_hit_driven_volatility_niamp_126d_slope_v024_signal,
    f38hv_f38_hit_driven_volatility_niamp_252d_slope_v025_signal,
    f38hv_f38_hit_driven_volatility_ebitswing_63d_slope_v026_signal,
    f38hv_f38_hit_driven_volatility_ebitswing_126d_slope_v027_signal,
    f38hv_f38_hit_driven_volatility_ebitswing_252d_slope_v028_signal,
    f38hv_f38_hit_driven_volatility_ebitamp_63d_slope_v029_signal,
    f38hv_f38_hit_driven_volatility_ebitamp_126d_slope_v030_signal,
    f38hv_f38_hit_driven_volatility_ebitamp_252d_slope_v031_signal,
    f38hv_f38_hit_driven_volatility_opswing_63d_slope_v032_signal,
    f38hv_f38_hit_driven_volatility_opswing_126d_slope_v033_signal,
    f38hv_f38_hit_driven_volatility_opswing_252d_slope_v034_signal,
    f38hv_f38_hit_driven_volatility_opamp_63d_slope_v035_signal,
    f38hv_f38_hit_driven_volatility_opamp_126d_slope_v036_signal,
    f38hv_f38_hit_driven_volatility_gmburst_63d_slope_v037_signal,
    f38hv_f38_hit_driven_volatility_gmburst_126d_slope_v038_signal,
    f38hv_f38_hit_driven_volatility_gmburst_252d_slope_v039_signal,
    f38hv_f38_hit_driven_volatility_gmvol_63d_slope_v040_signal,
    f38hv_f38_hit_driven_volatility_gmvol_126d_slope_v041_signal,
    f38hv_f38_hit_driven_volatility_gmvol_252d_slope_v042_signal,
    f38hv_f38_hit_driven_volatility_revrz_63d_slope_v043_signal,
    f38hv_f38_hit_driven_volatility_revrz_126d_slope_v044_signal,
    f38hv_f38_hit_driven_volatility_revrz_252d_slope_v045_signal,
    f38hv_f38_hit_driven_volatility_revsemi_63d_slope_v046_signal,
    f38hv_f38_hit_driven_volatility_revsemi_126d_slope_v047_signal,
    f38hv_f38_hit_driven_volatility_revvov_126d_slope_v048_signal,
    f38hv_f38_hit_driven_volatility_revvov_252d_slope_v049_signal,
    f38hv_f38_hit_driven_volatility_revterm_63d_slope_v050_signal,
    f38hv_f38_hit_driven_volatility_revterm_126d_slope_v051_signal,
    f38hv_f38_hit_driven_volatility_revspk_126d_slope_v052_signal,
    f38hv_f38_hit_driven_volatility_revspk_252d_slope_v053_signal,
    f38hv_f38_hit_driven_volatility_niflip_126d_slope_v054_signal,
    f38hv_f38_hit_driven_volatility_niflip_252d_slope_v055_signal,
    f38hv_f38_hit_driven_volatility_ebitloss_126d_slope_v056_signal,
    f38hv_f38_hit_driven_volatility_ebitloss_252d_slope_v057_signal,
    f38hv_f38_hit_driven_volatility_revac_126d_slope_v058_signal,
    f38hv_f38_hit_driven_volatility_revac_252d_slope_v059_signal,
    f38hv_f38_hit_driven_volatility_revkurt_126d_slope_v060_signal,
    f38hv_f38_hit_driven_volatility_revkurt_252d_slope_v061_signal,
    f38hv_f38_hit_driven_volatility_revskew_126d_slope_v062_signal,
    f38hv_f38_hit_driven_volatility_revskew_252d_slope_v063_signal,
    f38hv_f38_hit_driven_volatility_nikurt_126d_slope_v064_signal,
    f38hv_f38_hit_driven_volatility_niskew_252d_slope_v065_signal,
    f38hv_f38_hit_driven_volatility_hitmarg_63d_slope_v066_signal,
    f38hv_f38_hit_driven_volatility_hitmarg_126d_slope_v067_signal,
    f38hv_f38_hit_driven_volatility_opleva_126d_slope_v068_signal,
    f38hv_f38_hit_driven_volatility_opleva_252d_slope_v069_signal,
    f38hv_f38_hit_driven_volatility_nileva_126d_slope_v070_signal,
    f38hv_f38_hit_driven_volatility_nileva_252d_slope_v071_signal,
    f38hv_f38_hit_driven_volatility_opburst_63d_slope_v072_signal,
    f38hv_f38_hit_driven_volatility_opburst_126d_slope_v073_signal,
    f38hv_f38_hit_driven_volatility_revuw_126d_slope_v074_signal,
    f38hv_f38_hit_driven_volatility_revuw_252d_slope_v075_signal,
    f38hv_f38_hit_driven_volatility_revrng_63d_slope_v076_signal,
    f38hv_f38_hit_driven_volatility_revrng_252d_slope_v077_signal,
    f38hv_f38_hit_driven_volatility_revmaxg_126d_slope_v078_signal,
    f38hv_f38_hit_driven_volatility_revmaxg_252d_slope_v079_signal,
    f38hv_f38_hit_driven_volatility_revming_126d_slope_v080_signal,
    f38hv_f38_hit_driven_volatility_gmamp_126d_slope_v081_signal,
    f38hv_f38_hit_driven_volatility_gmamp_252d_slope_v082_signal,
    f38hv_f38_hit_driven_volatility_gmclust_126d_slope_v083_signal,
    f38hv_f38_hit_driven_volatility_nicv_126d_slope_v084_signal,
    f38hv_f38_hit_driven_volatility_nicv_252d_slope_v085_signal,
    f38hv_f38_hit_driven_volatility_ebitcv_126d_slope_v086_signal,
    f38hv_f38_hit_driven_volatility_ebitcv_252d_slope_v087_signal,
    f38hv_f38_hit_driven_volatility_revburstsm_126d_slope_v088_signal,
    f38hv_f38_hit_driven_volatility_revburstsm_252d_slope_v089_signal,
    f38hv_f38_hit_driven_volatility_revcvrank_252d_slope_v090_signal,
    f38hv_f38_hit_driven_volatility_revburstrank_252d_slope_v091_signal,
    f38hv_f38_hit_driven_volatility_eargear_126d_slope_v092_signal,
    f38hv_f38_hit_driven_volatility_eargear_252d_slope_v093_signal,
    f38hv_f38_hit_driven_volatility_revfade_126d_slope_v094_signal,
    f38hv_f38_hit_driven_volatility_revfade_252d_slope_v095_signal,
    f38hv_f38_hit_driven_volatility_opclust_126d_slope_v096_signal,
    f38hv_f38_hit_driven_volatility_opclust_252d_slope_v097_signal,
    f38hv_f38_hit_driven_volatility_niclust_126d_slope_v098_signal,
    f38hv_f38_hit_driven_volatility_niclust_252d_slope_v099_signal,
    f38hv_f38_hit_driven_volatility_ebitclust_126d_slope_v100_signal,
    f38hv_f38_hit_driven_volatility_ebitclust_252d_slope_v101_signal,
    f38hv_f38_hit_driven_volatility_revmad_126d_slope_v102_signal,
    f38hv_f38_hit_driven_volatility_revmad_252d_slope_v103_signal,
    f38hv_f38_hit_driven_volatility_gmspk_252d_slope_v104_signal,
    f38hv_f38_hit_driven_volatility_gmz_126d_slope_v105_signal,
    f38hv_f38_hit_driven_volatility_gmskew_252d_slope_v106_signal,
    f38hv_f38_hit_driven_volatility_revphase_126d_slope_v107_signal,
    f38hv_f38_hit_driven_volatility_revphase_252d_slope_v108_signal,
    f38hv_f38_hit_driven_volatility_ebitburst_63d_slope_v109_signal,
    f38hv_f38_hit_driven_volatility_ebitburst_126d_slope_v110_signal,
    f38hv_f38_hit_driven_volatility_niburst_63d_slope_v111_signal,
    f38hv_f38_hit_driven_volatility_niburst_126d_slope_v112_signal,
    f38hv_f38_hit_driven_volatility_revvolacc_126d_slope_v113_signal,
    f38hv_f38_hit_driven_volatility_revvolacc_252d_slope_v114_signal,
    f38hv_f38_hit_driven_volatility_hitcomp_126d_slope_v115_signal,
    f38hv_f38_hit_driven_volatility_hitcomp_252d_slope_v116_signal,
    f38hv_f38_hit_driven_volatility_revcliff_126d_slope_v117_signal,
    f38hv_f38_hit_driven_volatility_revcliff_252d_slope_v118_signal,
    f38hv_f38_hit_driven_volatility_opcv_126d_slope_v119_signal,
    f38hv_f38_hit_driven_volatility_opcv_252d_slope_v120_signal,
    f38hv_f38_hit_driven_volatility_revvolz_252d_slope_v121_signal,
    f38hv_f38_hit_driven_volatility_earampratio_252d_slope_v122_signal,
    f38hv_f38_hit_driven_volatility_revhits_252d_slope_v123_signal,
    f38hv_f38_hit_driven_volatility_revhits_126d_slope_v124_signal,
    f38hv_f38_hit_driven_volatility_gmonhit_252d_slope_v125_signal,
    f38hv_f38_hit_driven_volatility_revlrng_126d_slope_v126_signal,
    f38hv_f38_hit_driven_volatility_revlrng_252d_slope_v127_signal,
    f38hv_f38_hit_driven_volatility_niasym_126d_slope_v128_signal,
    f38hv_f38_hit_driven_volatility_niasym_252d_slope_v129_signal,
    f38hv_f38_hit_driven_volatility_ebitdown_252d_slope_v130_signal,
    f38hv_f38_hit_driven_volatility_revdsemi_252d_slope_v131_signal,
    f38hv_f38_hit_driven_volatility_revusemi_252d_slope_v132_signal,
    f38hv_f38_hit_driven_volatility_revlife_252d_slope_v133_signal,
    f38hv_f38_hit_driven_volatility_earvolr_252d_slope_v134_signal,
    f38hv_f38_hit_driven_volatility_revspkpers_252d_slope_v135_signal,
    f38hv_f38_hit_driven_volatility_gmrevco_252d_slope_v136_signal,
    f38hv_f38_hit_driven_volatility_revampz_252d_slope_v137_signal,
    f38hv_f38_hit_driven_volatility_niswingz_252d_slope_v138_signal,
    f38hv_f38_hit_driven_volatility_opburstrank_252d_slope_v139_signal,
    f38hv_f38_hit_driven_volatility_ebitburstrank_252d_slope_v140_signal,
    f38hv_f38_hit_driven_volatility_revampvol_252d_slope_v141_signal,
    f38hv_f38_hit_driven_volatility_revampvol_126d_slope_v142_signal,
    f38hv_f38_hit_driven_volatility_gmchgskew_126d_slope_v143_signal,
    f38hv_f38_hit_driven_volatility_gmchgvol_252d_slope_v144_signal,
    f38hv_f38_hit_driven_volatility_revtail_252d_slope_v145_signal,
    f38hv_f38_hit_driven_volatility_earswingmix_252d_slope_v146_signal,
    f38hv_f38_hit_driven_volatility_revqspr_252d_slope_v147_signal,
    f38hv_f38_hit_driven_volatility_opgear_252d_slope_v148_signal,
    f38hv_f38_hit_driven_volatility_nidown_252d_slope_v149_signal,
    f38hv_f38_hit_driven_volatility_revrngspr_252d_slope_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]

REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F38_HIT_DRIVEN_VOLATILITY_REGISTRY_001_150 = REGISTRY

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

    def _spiky(seed, base, drift=0.02, vol=0.06, hit_rate=0.10, hit_amp=1.6):
        # hit-driven lumpy series: a backbone punctuated by random release
        # "hits" that spike the level and then decay back toward baseline.
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        backbone = base * np.exp(np.cumsum(steps / 63))
        mult = np.ones(n)
        i = 0
        while i < n:
            if g.random() < hit_rate:
                amp = 1.0 + abs(g.normal(hit_amp, 0.8))
                length = int(abs(g.normal(45, 20))) + 5
                decay = g.uniform(0.90, 0.985)
                for k in range(length):
                    if i + k >= n:
                        break
                    mult[i + k] = max(mult[i + k], 1.0 + (amp - 1.0) * (decay ** k))
                i += length
            else:
                i += 1
        # idiosyncratic daily noise so rolling extremes/counts are not piecewise
        # constant; preserves the hit/decay lumpiness in the backbone*mult signal.
        noise = np.exp(g.normal(0.0, 0.02, n))
        return pd.Series(backbone * mult * noise, name=None)

    revenue = _spiky(3801, base=1.4e8, drift=0.02, vol=0.06,
                     hit_rate=0.11, hit_amp=1.7).rename("revenue")
    netinc = (_spiky(3802, base=4.0e7, drift=0.015, vol=0.09,
                     hit_rate=0.10, hit_amp=2.1) - 5.5e7).rename("netinc")
    ebit = (_spiky(3803, base=4.5e7, drift=0.018, vol=0.085,
                   hit_rate=0.10, hit_amp=1.9) - 5.0e7).rename("ebit")
    opinc = (_spiky(3804, base=4.2e7, drift=0.017, vol=0.088,
                    hit_rate=0.10, hit_amp=2.0) - 5.2e7).rename("opinc")
    _gmraw = _spiky(3805, base=0.30, drift=0.004, vol=0.05,
                    hit_rate=0.09, hit_amp=0.9)
    grossmargin = pd.Series(np.clip(_gmraw.values, 0.05, 0.85), name="grossmargin")

    cols = {"revenue": revenue, "netinc": netinc, "ebit": ebit,
            "opinc": opinc, "grossmargin": grossmargin}

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

    print("OK f38_hit_driven_volatility_2nd_derivatives_001_150_claude: %d features pass" % n_features)
