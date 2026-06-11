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



# revvol 21d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revvol_21d_base_v001_signal(revenue):
    lr = _f38hv_logret(revenue)
    x = lr.rolling(21, min_periods=10).std()
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revvol 63d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revvol_63d_base_v002_signal(revenue):
    lr = _f38hv_logret(revenue)
    x = lr.rolling(63, min_periods=21).std()
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revvol 126d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revvol_126d_base_v003_signal(revenue):
    lr = _f38hv_logret(revenue)
    x = lr.rolling(126, min_periods=63).std()
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revvol 252d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revvol_252d_base_v004_signal(revenue):
    lr = _f38hv_logret(revenue)
    x = lr.rolling(252, min_periods=126).std()
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revcv 63d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revcv_63d_base_v005_signal(revenue):
    x = _f38hv_cv(revenue, 63)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revcv 126d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revcv_126d_base_v006_signal(revenue):
    x = _f38hv_cv(revenue, 126)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revcv 252d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revcv_252d_base_v007_signal(revenue):
    x = _f38hv_cv(revenue, 252)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revburst 63d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revburst_63d_base_v008_signal(revenue):
    x = _f38hv_burst(revenue, 63)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revburst 126d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revburst_126d_base_v009_signal(revenue):
    x = _f38hv_burst(revenue, 126)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revburst 252d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revburst_252d_base_v010_signal(revenue):
    x = _f38hv_burst(revenue, 252)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revdecay 63d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revdecay_63d_base_v011_signal(revenue):
    x = _f38hv_decay(revenue, 63)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revdecay 126d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revdecay_126d_base_v012_signal(revenue):
    x = _f38hv_decay(revenue, 126)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revdecay 252d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revdecay_252d_base_v013_signal(revenue):
    x = _f38hv_decay(revenue, 252)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revamp 63d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revamp_63d_base_v014_signal(revenue):
    x = _f38hv_amp(revenue, 63)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revamp 126d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revamp_126d_base_v015_signal(revenue):
    x = _f38hv_amp(revenue, 126)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revamp 252d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revamp_252d_base_v016_signal(revenue):
    x = _f38hv_amp(revenue, 252)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revherf 63d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revherf_63d_base_v017_signal(revenue):
    g = _f38hv_relret(revenue).clip(lower=0)
    tot = g.rolling(63, min_periods=21).sum()
    sq = (g * g).rolling(63, min_periods=21).sum()
    x = sq / (tot * tot).replace(0, np.nan)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revherf 126d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revherf_126d_base_v018_signal(revenue):
    g = _f38hv_relret(revenue).clip(lower=0)
    tot = g.rolling(126, min_periods=63).sum()
    sq = (g * g).rolling(126, min_periods=63).sum()
    x = sq / (tot * tot).replace(0, np.nan)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revherf 252d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revherf_252d_base_v019_signal(revenue):
    g = _f38hv_relret(revenue).clip(lower=0)
    tot = g.rolling(252, min_periods=126).sum()
    sq = (g * g).rolling(252, min_periods=126).sum()
    x = sq / (tot * tot).replace(0, np.nan)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# niswing 63d hit-driven lumpiness (netinc)
def f38hv_f38_hit_driven_volatility_niswing_63d_base_v020_signal(netinc):
    x = _f38hv_swing(netinc, 63)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# niswing 126d hit-driven lumpiness (netinc)
def f38hv_f38_hit_driven_volatility_niswing_126d_base_v021_signal(netinc):
    x = _f38hv_swing(netinc, 126)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# niswing 252d hit-driven lumpiness (netinc)
def f38hv_f38_hit_driven_volatility_niswing_252d_base_v022_signal(netinc):
    x = _f38hv_swing(netinc, 252)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# niamp 63d hit-driven lumpiness (netinc)
def f38hv_f38_hit_driven_volatility_niamp_63d_base_v023_signal(netinc):
    x = _f38hv_amp(netinc, 63)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# niamp 126d hit-driven lumpiness (netinc)
def f38hv_f38_hit_driven_volatility_niamp_126d_base_v024_signal(netinc):
    x = _f38hv_amp(netinc, 126)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# niamp 252d hit-driven lumpiness (netinc)
def f38hv_f38_hit_driven_volatility_niamp_252d_base_v025_signal(netinc):
    x = _f38hv_amp(netinc, 252)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ebitswing 63d hit-driven lumpiness (ebit)
def f38hv_f38_hit_driven_volatility_ebitswing_63d_base_v026_signal(ebit):
    x = _f38hv_swing(ebit, 63)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ebitswing 126d hit-driven lumpiness (ebit)
def f38hv_f38_hit_driven_volatility_ebitswing_126d_base_v027_signal(ebit):
    x = _f38hv_swing(ebit, 126)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ebitswing 252d hit-driven lumpiness (ebit)
def f38hv_f38_hit_driven_volatility_ebitswing_252d_base_v028_signal(ebit):
    x = _f38hv_swing(ebit, 252)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ebitamp 63d hit-driven lumpiness (ebit)
def f38hv_f38_hit_driven_volatility_ebitamp_63d_base_v029_signal(ebit):
    x = _f38hv_amp(ebit, 63)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ebitamp 126d hit-driven lumpiness (ebit)
def f38hv_f38_hit_driven_volatility_ebitamp_126d_base_v030_signal(ebit):
    x = _f38hv_amp(ebit, 126)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ebitamp 252d hit-driven lumpiness (ebit)
def f38hv_f38_hit_driven_volatility_ebitamp_252d_base_v031_signal(ebit):
    x = _f38hv_amp(ebit, 252)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# opswing 63d hit-driven lumpiness (opinc)
def f38hv_f38_hit_driven_volatility_opswing_63d_base_v032_signal(opinc):
    x = _f38hv_swing(opinc, 63)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# opswing 126d hit-driven lumpiness (opinc)
def f38hv_f38_hit_driven_volatility_opswing_126d_base_v033_signal(opinc):
    x = _f38hv_swing(opinc, 126)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# opswing 252d hit-driven lumpiness (opinc)
def f38hv_f38_hit_driven_volatility_opswing_252d_base_v034_signal(opinc):
    x = _f38hv_swing(opinc, 252)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# opamp 63d hit-driven lumpiness (opinc)
def f38hv_f38_hit_driven_volatility_opamp_63d_base_v035_signal(opinc):
    x = _f38hv_amp(opinc, 63)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# opamp 126d hit-driven lumpiness (opinc)
def f38hv_f38_hit_driven_volatility_opamp_126d_base_v036_signal(opinc):
    x = _f38hv_amp(opinc, 126)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gmburst 63d hit-driven lumpiness (grossmargin)
def f38hv_f38_hit_driven_volatility_gmburst_63d_base_v037_signal(grossmargin):
    x = grossmargin - _mean(grossmargin, 63)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gmburst 126d hit-driven lumpiness (grossmargin)
def f38hv_f38_hit_driven_volatility_gmburst_126d_base_v038_signal(grossmargin):
    x = grossmargin - _mean(grossmargin, 126)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gmburst 252d hit-driven lumpiness (grossmargin)
def f38hv_f38_hit_driven_volatility_gmburst_252d_base_v039_signal(grossmargin):
    x = grossmargin - _mean(grossmargin, 252)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gmvol 63d hit-driven lumpiness (grossmargin)
def f38hv_f38_hit_driven_volatility_gmvol_63d_base_v040_signal(grossmargin):
    x = _std(grossmargin, 63)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gmvol 126d hit-driven lumpiness (grossmargin)
def f38hv_f38_hit_driven_volatility_gmvol_126d_base_v041_signal(grossmargin):
    x = _std(grossmargin, 126)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gmvol 252d hit-driven lumpiness (grossmargin)
def f38hv_f38_hit_driven_volatility_gmvol_252d_base_v042_signal(grossmargin):
    x = _std(grossmargin, 252)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revrz 63d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revrz_63d_base_v043_signal(revenue):
    med = revenue.rolling(63, min_periods=21).median()
    iqr = (revenue.rolling(63, min_periods=21).quantile(0.75) - revenue.rolling(63, min_periods=21).quantile(0.25))
    x = (revenue - med) / iqr.replace(0, np.nan)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revrz 126d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revrz_126d_base_v044_signal(revenue):
    med = revenue.rolling(126, min_periods=63).median()
    iqr = (revenue.rolling(126, min_periods=63).quantile(0.75) - revenue.rolling(126, min_periods=63).quantile(0.25))
    x = (revenue - med) / iqr.replace(0, np.nan)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revrz 252d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revrz_252d_base_v045_signal(revenue):
    med = revenue.rolling(252, min_periods=126).median()
    iqr = (revenue.rolling(252, min_periods=126).quantile(0.75) - revenue.rolling(252, min_periods=126).quantile(0.25))
    x = (revenue - med) / iqr.replace(0, np.nan)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revsemi 63d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revsemi_63d_base_v046_signal(revenue):
    lr = _f38hv_relret(revenue)
    up = lr.where(lr > 0).rolling(63, min_periods=15).std()
    dn = lr.where(lr < 0).rolling(63, min_periods=15).std()
    x = up - dn
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revsemi 126d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revsemi_126d_base_v047_signal(revenue):
    lr = _f38hv_relret(revenue)
    up = lr.where(lr > 0).rolling(126, min_periods=30).std()
    dn = lr.where(lr < 0).rolling(126, min_periods=30).std()
    x = up - dn
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revvov 126d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revvov_126d_base_v048_signal(revenue):
    lr = _f38hv_logret(revenue)
    v = lr.rolling(21, min_periods=10).std()
    x = v.rolling(126, min_periods=63).std()
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revvov 252d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revvov_252d_base_v049_signal(revenue):
    lr = _f38hv_logret(revenue)
    v = lr.rolling(21, min_periods=10).std()
    x = v.rolling(252, min_periods=126).std()
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revterm 63d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revterm_63d_base_v050_signal(revenue):
    lr = _f38hv_logret(revenue)
    vs = lr.rolling(21, min_periods=10).std()
    vl = lr.rolling(126, min_periods=63).std()
    x = vs / vl.replace(0, np.nan)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revterm 126d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revterm_126d_base_v051_signal(revenue):
    lr = _f38hv_logret(revenue)
    vs = lr.rolling(63, min_periods=21).std()
    vl = lr.rolling(252, min_periods=126).std()
    x = vs / vl.replace(0, np.nan)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revspk 126d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revspk_126d_base_v052_signal(revenue):
    lr = _f38hv_logret(revenue)
    z = (lr - lr.rolling(126, min_periods=63).mean()) / lr.rolling(126, min_periods=63).std().replace(0, np.nan)
    exc = (z.abs() - 1.5).clip(lower=0) ** 2
    x = exc.rolling(126, min_periods=63).mean()
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revspk 252d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revspk_252d_base_v053_signal(revenue):
    lr = _f38hv_logret(revenue)
    z = (lr - lr.rolling(252, min_periods=126).mean()) / lr.rolling(252, min_periods=126).std().replace(0, np.nan)
    exc = (z.abs() - 1.5).clip(lower=0) ** 2
    x = exc.rolling(252, min_periods=126).mean()
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# niflip 126d hit-driven lumpiness (netinc)
def f38hv_f38_hit_driven_volatility_niflip_126d_base_v054_signal(netinc):
    sg = np.sign(netinc)
    fl = (sg != sg.shift(1)).astype(float)
    w = fl * netinc.diff().abs()
    x = w.rolling(126, min_periods=63).mean()
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# niflip 252d hit-driven lumpiness (netinc)
def f38hv_f38_hit_driven_volatility_niflip_252d_base_v055_signal(netinc):
    sg = np.sign(netinc)
    fl = (sg != sg.shift(1)).astype(float)
    w = fl * netinc.diff().abs()
    x = w.rolling(252, min_periods=126).mean()
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ebitloss 126d hit-driven lumpiness (ebit)
def f38hv_f38_hit_driven_volatility_ebitloss_126d_base_v056_signal(ebit):
    x = (ebit < 0).astype(float).rolling(126, min_periods=63).mean()
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ebitloss 252d hit-driven lumpiness (ebit)
def f38hv_f38_hit_driven_volatility_ebitloss_252d_base_v057_signal(ebit):
    x = (ebit < 0).astype(float).rolling(252, min_periods=126).mean()
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revac 126d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revac_126d_base_v058_signal(revenue):
    lr = _f38hv_relret(revenue)
    x = lr.rolling(126, min_periods=63).corr(lr.shift(1))
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revac 252d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revac_252d_base_v059_signal(revenue):
    lr = _f38hv_relret(revenue)
    x = lr.rolling(252, min_periods=126).corr(lr.shift(1))
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revkurt 126d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revkurt_126d_base_v060_signal(revenue):
    lr = _f38hv_logret(revenue)
    x = lr.rolling(126, min_periods=63).kurt()
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revkurt 252d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revkurt_252d_base_v061_signal(revenue):
    lr = _f38hv_logret(revenue)
    x = lr.rolling(252, min_periods=126).kurt()
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revskew 126d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revskew_126d_base_v062_signal(revenue):
    lr = _f38hv_logret(revenue)
    x = lr.rolling(126, min_periods=63).skew()
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revskew 252d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revskew_252d_base_v063_signal(revenue):
    lr = _f38hv_logret(revenue)
    x = lr.rolling(252, min_periods=126).skew()
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# nikurt 126d hit-driven lumpiness (netinc)
def f38hv_f38_hit_driven_volatility_nikurt_126d_base_v064_signal(netinc):
    d = netinc.diff()
    x = d.rolling(126, min_periods=63).kurt()
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# niskew 252d hit-driven lumpiness (netinc)
def f38hv_f38_hit_driven_volatility_niskew_252d_base_v065_signal(netinc):
    d = netinc.diff()
    x = d.rolling(252, min_periods=126).skew()
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# hitmarg 63d hit-driven lumpiness (revenue,grossmargin)
def f38hv_f38_hit_driven_volatility_hitmarg_63d_base_v066_signal(revenue, grossmargin):
    rb = _f38hv_burst(revenue, 63)
    gd = grossmargin - _mean(grossmargin, 63)
    x = rb * gd
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# hitmarg 126d hit-driven lumpiness (revenue,grossmargin)
def f38hv_f38_hit_driven_volatility_hitmarg_126d_base_v067_signal(revenue, grossmargin):
    rb = _f38hv_burst(revenue, 126)
    gd = grossmargin - _mean(grossmargin, 126)
    x = rb * gd
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# opleva 126d hit-driven lumpiness (ebit,revenue)
def f38hv_f38_hit_driven_volatility_opleva_126d_base_v068_signal(ebit, revenue):
    es = _f38hv_amp(ebit, 126)
    rs = _f38hv_amp(revenue, 126)
    x = es / rs.replace(0, np.nan)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# opleva 252d hit-driven lumpiness (ebit,revenue)
def f38hv_f38_hit_driven_volatility_opleva_252d_base_v069_signal(ebit, revenue):
    es = _f38hv_amp(ebit, 252)
    rs = _f38hv_amp(revenue, 252)
    x = es / rs.replace(0, np.nan)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# nileva 126d hit-driven lumpiness (netinc,revenue)
def f38hv_f38_hit_driven_volatility_nileva_126d_base_v070_signal(netinc, revenue):
    ns = _f38hv_amp(netinc, 126)
    rs = _f38hv_amp(revenue, 126)
    x = ns / rs.replace(0, np.nan)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# nileva 252d hit-driven lumpiness (netinc,revenue)
def f38hv_f38_hit_driven_volatility_nileva_252d_base_v071_signal(netinc, revenue):
    ns = _f38hv_amp(netinc, 252)
    rs = _f38hv_amp(revenue, 252)
    x = ns / rs.replace(0, np.nan)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# opburst 63d hit-driven lumpiness (opinc)
def f38hv_f38_hit_driven_volatility_opburst_63d_base_v072_signal(opinc):
    x = (opinc - _mean(opinc, 63)) / _std(opinc, 63)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# opburst 126d hit-driven lumpiness (opinc)
def f38hv_f38_hit_driven_volatility_opburst_126d_base_v073_signal(opinc):
    x = (opinc - _mean(opinc, 126)) / _std(opinc, 126)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revuw 126d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revuw_126d_base_v074_signal(revenue):
    hi = _rmax(revenue, 126)
    uw = (1.0 - revenue / hi.replace(0, np.nan)).clip(lower=0)
    x = uw.rolling(126, min_periods=63).mean()
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revuw 252d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revuw_252d_base_v075_signal(revenue):
    hi = _rmax(revenue, 252)
    uw = (1.0 - revenue / hi.replace(0, np.nan)).clip(lower=0)
    x = uw.rolling(252, min_periods=126).mean()
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f38hv_f38_hit_driven_volatility_revvol_21d_base_v001_signal,
    f38hv_f38_hit_driven_volatility_revvol_63d_base_v002_signal,
    f38hv_f38_hit_driven_volatility_revvol_126d_base_v003_signal,
    f38hv_f38_hit_driven_volatility_revvol_252d_base_v004_signal,
    f38hv_f38_hit_driven_volatility_revcv_63d_base_v005_signal,
    f38hv_f38_hit_driven_volatility_revcv_126d_base_v006_signal,
    f38hv_f38_hit_driven_volatility_revcv_252d_base_v007_signal,
    f38hv_f38_hit_driven_volatility_revburst_63d_base_v008_signal,
    f38hv_f38_hit_driven_volatility_revburst_126d_base_v009_signal,
    f38hv_f38_hit_driven_volatility_revburst_252d_base_v010_signal,
    f38hv_f38_hit_driven_volatility_revdecay_63d_base_v011_signal,
    f38hv_f38_hit_driven_volatility_revdecay_126d_base_v012_signal,
    f38hv_f38_hit_driven_volatility_revdecay_252d_base_v013_signal,
    f38hv_f38_hit_driven_volatility_revamp_63d_base_v014_signal,
    f38hv_f38_hit_driven_volatility_revamp_126d_base_v015_signal,
    f38hv_f38_hit_driven_volatility_revamp_252d_base_v016_signal,
    f38hv_f38_hit_driven_volatility_revherf_63d_base_v017_signal,
    f38hv_f38_hit_driven_volatility_revherf_126d_base_v018_signal,
    f38hv_f38_hit_driven_volatility_revherf_252d_base_v019_signal,
    f38hv_f38_hit_driven_volatility_niswing_63d_base_v020_signal,
    f38hv_f38_hit_driven_volatility_niswing_126d_base_v021_signal,
    f38hv_f38_hit_driven_volatility_niswing_252d_base_v022_signal,
    f38hv_f38_hit_driven_volatility_niamp_63d_base_v023_signal,
    f38hv_f38_hit_driven_volatility_niamp_126d_base_v024_signal,
    f38hv_f38_hit_driven_volatility_niamp_252d_base_v025_signal,
    f38hv_f38_hit_driven_volatility_ebitswing_63d_base_v026_signal,
    f38hv_f38_hit_driven_volatility_ebitswing_126d_base_v027_signal,
    f38hv_f38_hit_driven_volatility_ebitswing_252d_base_v028_signal,
    f38hv_f38_hit_driven_volatility_ebitamp_63d_base_v029_signal,
    f38hv_f38_hit_driven_volatility_ebitamp_126d_base_v030_signal,
    f38hv_f38_hit_driven_volatility_ebitamp_252d_base_v031_signal,
    f38hv_f38_hit_driven_volatility_opswing_63d_base_v032_signal,
    f38hv_f38_hit_driven_volatility_opswing_126d_base_v033_signal,
    f38hv_f38_hit_driven_volatility_opswing_252d_base_v034_signal,
    f38hv_f38_hit_driven_volatility_opamp_63d_base_v035_signal,
    f38hv_f38_hit_driven_volatility_opamp_126d_base_v036_signal,
    f38hv_f38_hit_driven_volatility_gmburst_63d_base_v037_signal,
    f38hv_f38_hit_driven_volatility_gmburst_126d_base_v038_signal,
    f38hv_f38_hit_driven_volatility_gmburst_252d_base_v039_signal,
    f38hv_f38_hit_driven_volatility_gmvol_63d_base_v040_signal,
    f38hv_f38_hit_driven_volatility_gmvol_126d_base_v041_signal,
    f38hv_f38_hit_driven_volatility_gmvol_252d_base_v042_signal,
    f38hv_f38_hit_driven_volatility_revrz_63d_base_v043_signal,
    f38hv_f38_hit_driven_volatility_revrz_126d_base_v044_signal,
    f38hv_f38_hit_driven_volatility_revrz_252d_base_v045_signal,
    f38hv_f38_hit_driven_volatility_revsemi_63d_base_v046_signal,
    f38hv_f38_hit_driven_volatility_revsemi_126d_base_v047_signal,
    f38hv_f38_hit_driven_volatility_revvov_126d_base_v048_signal,
    f38hv_f38_hit_driven_volatility_revvov_252d_base_v049_signal,
    f38hv_f38_hit_driven_volatility_revterm_63d_base_v050_signal,
    f38hv_f38_hit_driven_volatility_revterm_126d_base_v051_signal,
    f38hv_f38_hit_driven_volatility_revspk_126d_base_v052_signal,
    f38hv_f38_hit_driven_volatility_revspk_252d_base_v053_signal,
    f38hv_f38_hit_driven_volatility_niflip_126d_base_v054_signal,
    f38hv_f38_hit_driven_volatility_niflip_252d_base_v055_signal,
    f38hv_f38_hit_driven_volatility_ebitloss_126d_base_v056_signal,
    f38hv_f38_hit_driven_volatility_ebitloss_252d_base_v057_signal,
    f38hv_f38_hit_driven_volatility_revac_126d_base_v058_signal,
    f38hv_f38_hit_driven_volatility_revac_252d_base_v059_signal,
    f38hv_f38_hit_driven_volatility_revkurt_126d_base_v060_signal,
    f38hv_f38_hit_driven_volatility_revkurt_252d_base_v061_signal,
    f38hv_f38_hit_driven_volatility_revskew_126d_base_v062_signal,
    f38hv_f38_hit_driven_volatility_revskew_252d_base_v063_signal,
    f38hv_f38_hit_driven_volatility_nikurt_126d_base_v064_signal,
    f38hv_f38_hit_driven_volatility_niskew_252d_base_v065_signal,
    f38hv_f38_hit_driven_volatility_hitmarg_63d_base_v066_signal,
    f38hv_f38_hit_driven_volatility_hitmarg_126d_base_v067_signal,
    f38hv_f38_hit_driven_volatility_opleva_126d_base_v068_signal,
    f38hv_f38_hit_driven_volatility_opleva_252d_base_v069_signal,
    f38hv_f38_hit_driven_volatility_nileva_126d_base_v070_signal,
    f38hv_f38_hit_driven_volatility_nileva_252d_base_v071_signal,
    f38hv_f38_hit_driven_volatility_opburst_63d_base_v072_signal,
    f38hv_f38_hit_driven_volatility_opburst_126d_base_v073_signal,
    f38hv_f38_hit_driven_volatility_revuw_126d_base_v074_signal,
    f38hv_f38_hit_driven_volatility_revuw_252d_base_v075_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]

REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F38_HIT_DRIVEN_VOLATILITY_REGISTRY_001_075 = REGISTRY

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

    print("OK f38_hit_driven_volatility_base_001_075_claude: %d features pass" % n_features)
