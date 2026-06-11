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



# revrng 63d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revrng_63d_base_v076_signal(revenue):
    x = revenue.rolling(63, min_periods=21).rank(pct=True) - 0.5
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revrng 252d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revrng_252d_base_v077_signal(revenue):
    x = revenue.rolling(252, min_periods=126).rank(pct=True) - 0.5
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revmaxg 126d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revmaxg_126d_base_v078_signal(revenue):
    lr = _f38hv_relret(revenue)
    x = lr.rolling(126, min_periods=63).quantile(0.90)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revmaxg 252d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revmaxg_252d_base_v079_signal(revenue):
    lr = _f38hv_relret(revenue)
    x = lr.rolling(252, min_periods=126).quantile(0.90)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revming 126d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revming_126d_base_v080_signal(revenue):
    lr = _f38hv_relret(revenue)
    x = lr.rolling(126, min_periods=63).quantile(0.10)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gmamp 126d hit-driven lumpiness (grossmargin)
def f38hv_f38_hit_driven_volatility_gmamp_126d_base_v081_signal(grossmargin):
    x = _f38hv_amp(grossmargin, 126)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gmamp 252d hit-driven lumpiness (grossmargin)
def f38hv_f38_hit_driven_volatility_gmamp_252d_base_v082_signal(grossmargin):
    x = _f38hv_amp(grossmargin, 252)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gmclust 126d hit-driven lumpiness (grossmargin)
def f38hv_f38_hit_driven_volatility_gmclust_126d_base_v083_signal(grossmargin):
    a = grossmargin.diff().abs()
    x = a.rolling(126, min_periods=63).corr(a.shift(1))
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# nicv 126d hit-driven lumpiness (netinc)
def f38hv_f38_hit_driven_volatility_nicv_126d_base_v084_signal(netinc):
    m = _mean(netinc, 126)
    sd = _std(netinc, 126)
    x = sd / m.abs().replace(0, np.nan)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# nicv 252d hit-driven lumpiness (netinc)
def f38hv_f38_hit_driven_volatility_nicv_252d_base_v085_signal(netinc):
    m = _mean(netinc, 252)
    sd = _std(netinc, 252)
    x = sd / m.abs().replace(0, np.nan)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ebitcv 126d hit-driven lumpiness (ebit)
def f38hv_f38_hit_driven_volatility_ebitcv_126d_base_v086_signal(ebit):
    m = _mean(ebit, 126)
    sd = _std(ebit, 126)
    x = sd / m.abs().replace(0, np.nan)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ebitcv 252d hit-driven lumpiness (ebit)
def f38hv_f38_hit_driven_volatility_ebitcv_252d_base_v087_signal(ebit):
    m = _mean(ebit, 252)
    sd = _std(ebit, 252)
    x = sd / m.abs().replace(0, np.nan)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revburstsm 126d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revburstsm_126d_base_v088_signal(revenue):
    rb = _f38hv_burst(revenue, 126)
    x = rb.ewm(span=42, min_periods=21).mean()
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revburstsm 252d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revburstsm_252d_base_v089_signal(revenue):
    rb = _f38hv_burst(revenue, 252)
    x = rb.ewm(span=63, min_periods=31).mean()
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revcvrank 252d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revcvrank_252d_base_v090_signal(revenue):
    cv = _f38hv_cv(revenue, 63)
    x = cv.rolling(252, min_periods=126).rank(pct=True) - 0.5
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revburstrank 252d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revburstrank_252d_base_v091_signal(revenue):
    rb = _f38hv_burst(revenue, 63)
    x = rb.rolling(252, min_periods=126).rank(pct=True) - 0.5
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# eargear 126d hit-driven lumpiness (netinc,revenue)
def f38hv_f38_hit_driven_volatility_eargear_126d_base_v092_signal(netinc, revenue):
    ns = _std(netinc, 126)
    x = ns / _mean(revenue, 126).replace(0, np.nan)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# eargear 252d hit-driven lumpiness (ebit,revenue)
def f38hv_f38_hit_driven_volatility_eargear_252d_base_v093_signal(ebit, revenue):
    es = _std(ebit, 252)
    x = es / _mean(revenue, 252).replace(0, np.nan)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revfade 126d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revfade_126d_base_v094_signal(revenue):
    hi = _rmax(revenue, 126)
    fade = (hi - revenue) / hi.replace(0, np.nan)
    x = fade.rolling(63, min_periods=21).mean()
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revfade 252d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revfade_252d_base_v095_signal(revenue):
    hi = _rmax(revenue, 252)
    fade = (hi - revenue) / hi.replace(0, np.nan)
    x = fade.rolling(126, min_periods=63).mean()
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# opclust 126d hit-driven lumpiness (opinc)
def f38hv_f38_hit_driven_volatility_opclust_126d_base_v096_signal(opinc):
    a = opinc.diff().abs()
    x = a.rolling(126, min_periods=63).corr(a.shift(1))
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# opclust 252d hit-driven lumpiness (opinc)
def f38hv_f38_hit_driven_volatility_opclust_252d_base_v097_signal(opinc):
    a = opinc.diff().abs()
    x = a.rolling(252, min_periods=126).corr(a.shift(1))
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# niclust 126d hit-driven lumpiness (netinc)
def f38hv_f38_hit_driven_volatility_niclust_126d_base_v098_signal(netinc):
    a = netinc.diff().abs()
    x = a.rolling(126, min_periods=63).corr(a.shift(1))
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# niclust 252d hit-driven lumpiness (netinc)
def f38hv_f38_hit_driven_volatility_niclust_252d_base_v099_signal(netinc):
    a = netinc.diff().abs()
    x = a.rolling(252, min_periods=126).corr(a.shift(1))
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ebitclust 126d hit-driven lumpiness (ebit)
def f38hv_f38_hit_driven_volatility_ebitclust_126d_base_v100_signal(ebit):
    a = ebit.diff().abs()
    x = a.rolling(126, min_periods=63).corr(a.shift(1))
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ebitclust 252d hit-driven lumpiness (ebit)
def f38hv_f38_hit_driven_volatility_ebitclust_252d_base_v101_signal(ebit):
    a = ebit.diff().abs()
    x = a.rolling(252, min_periods=126).corr(a.shift(1))
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revmad 126d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revmad_126d_base_v102_signal(revenue):
    lr = _f38hv_relret(revenue)
    md = (lr - lr.rolling(126, min_periods=63).median()).abs()
    x = md.rolling(126, min_periods=63).median()
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revmad 252d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revmad_252d_base_v103_signal(revenue):
    lr = _f38hv_relret(revenue)
    md = (lr - lr.rolling(252, min_periods=126).median()).abs()
    x = md.rolling(252, min_periods=126).median()
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gmspk 252d hit-driven lumpiness (grossmargin)
def f38hv_f38_hit_driven_volatility_gmspk_252d_base_v104_signal(grossmargin):
    z = (grossmargin - _mean(grossmargin, 252)) / _std(grossmargin, 252)
    x = (z > 1.5).astype(float).rolling(252, min_periods=126).mean()
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gmz 126d hit-driven lumpiness (grossmargin)
def f38hv_f38_hit_driven_volatility_gmz_126d_base_v105_signal(grossmargin):
    x = _z(grossmargin, 126)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gmskew 252d hit-driven lumpiness (grossmargin)
def f38hv_f38_hit_driven_volatility_gmskew_252d_base_v106_signal(grossmargin):
    lr = grossmargin.diff()
    x = lr.rolling(252, min_periods=126).skew()
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revphase 126d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revphase_126d_base_v107_signal(revenue):
    rb = _f38hv_burst(revenue, 126).clip(lower=0)
    dc = (-_f38hv_decay(revenue, 126)).clip(lower=0)
    x = (rb - dc) / (rb + dc + 1e-9)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revphase 252d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revphase_252d_base_v108_signal(revenue):
    rb = _f38hv_burst(revenue, 252).clip(lower=0)
    dc = (-_f38hv_decay(revenue, 252)).clip(lower=0)
    x = (rb - dc) / (rb + dc + 1e-9)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ebitburst 63d hit-driven lumpiness (ebit)
def f38hv_f38_hit_driven_volatility_ebitburst_63d_base_v109_signal(ebit):
    x = (ebit - _mean(ebit, 63)) / _std(ebit, 63)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ebitburst 126d hit-driven lumpiness (ebit)
def f38hv_f38_hit_driven_volatility_ebitburst_126d_base_v110_signal(ebit):
    x = (ebit - _mean(ebit, 126)) / _std(ebit, 126)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# niburst 63d hit-driven lumpiness (netinc)
def f38hv_f38_hit_driven_volatility_niburst_63d_base_v111_signal(netinc):
    x = (netinc - _mean(netinc, 63)) / _std(netinc, 63)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# niburst 126d hit-driven lumpiness (netinc)
def f38hv_f38_hit_driven_volatility_niburst_126d_base_v112_signal(netinc):
    x = (netinc - _mean(netinc, 126)) / _std(netinc, 126)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revvolacc 126d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revvolacc_126d_base_v113_signal(revenue):
    lr = _f38hv_logret(revenue)
    v = lr.rolling(63, min_periods=21).std()
    x = v - v.shift(63)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revvolacc 252d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revvolacc_252d_base_v114_signal(revenue):
    lr = _f38hv_logret(revenue)
    v = lr.rolling(126, min_periods=63).std()
    x = v - v.shift(126)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# hitcomp 126d hit-driven lumpiness (revenue,netinc)
def f38hv_f38_hit_driven_volatility_hitcomp_126d_base_v115_signal(revenue, netinc):
    rc = _f38hv_cv(revenue, 126)
    ns = _f38hv_swing(netinc, 126)
    x = rc * ns
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# hitcomp 252d hit-driven lumpiness (revenue,ebit)
def f38hv_f38_hit_driven_volatility_hitcomp_252d_base_v116_signal(revenue, ebit):
    rc = _f38hv_cv(revenue, 252)
    es = _f38hv_swing(ebit, 252)
    x = rc * es
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revcliff 126d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revcliff_126d_base_v117_signal(revenue):
    lr = _f38hv_relret(revenue)
    neg = (-lr).clip(lower=0)
    x = neg.rolling(126, min_periods=63).mean()
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revcliff 252d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revcliff_252d_base_v118_signal(revenue):
    lr = _f38hv_relret(revenue)
    neg = (-lr).clip(lower=0)
    x = neg.rolling(252, min_periods=126).mean()
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# opcv 126d hit-driven lumpiness (opinc)
def f38hv_f38_hit_driven_volatility_opcv_126d_base_v119_signal(opinc):
    m = _mean(opinc, 126)
    sd = _std(opinc, 126)
    x = sd / m.abs().replace(0, np.nan)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# opcv 252d hit-driven lumpiness (opinc)
def f38hv_f38_hit_driven_volatility_opcv_252d_base_v120_signal(opinc):
    m = _mean(opinc, 252)
    sd = _std(opinc, 252)
    x = sd / m.abs().replace(0, np.nan)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revvolz 252d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revvolz_252d_base_v121_signal(revenue):
    lr = _f38hv_logret(revenue)
    v = lr.rolling(63, min_periods=21).std()
    x = _z(v, 252)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# earampratio 252d hit-driven lumpiness (netinc,ebit)
def f38hv_f38_hit_driven_volatility_earampratio_252d_base_v122_signal(netinc, ebit):
    ns = _f38hv_amp(netinc, 252)
    es = _f38hv_amp(ebit, 252)
    x = ns - es
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revhits 252d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revhits_252d_base_v123_signal(revenue):
    rb = _f38hv_burst(revenue, 63)
    amt = (rb - 0.25).clip(lower=0)
    x = amt.rolling(252, min_periods=126).mean()
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revhits 126d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revhits_126d_base_v124_signal(revenue):
    rb = _f38hv_burst(revenue, 63)
    amt = (rb - 0.25).clip(lower=0)
    x = amt.rolling(126, min_periods=63).mean()
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gmonhit 252d hit-driven lumpiness (grossmargin,revenue)
def f38hv_f38_hit_driven_volatility_gmonhit_252d_base_v125_signal(grossmargin, revenue):
    rb = _f38hv_burst(revenue, 63)
    cond = grossmargin.where(rb > 0.1)
    x = cond.rolling(252, min_periods=63).mean() - _mean(grossmargin, 252)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revlrng 126d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revlrng_126d_base_v126_signal(revenue):
    x = np.log(_rmax(revenue, 126).replace(0, np.nan) / _rmin(revenue, 126).replace(0, np.nan))
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revlrng 252d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revlrng_252d_base_v127_signal(revenue):
    x = np.log(_rmax(revenue, 252).replace(0, np.nan) / _rmin(revenue, 252).replace(0, np.nan))
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# niasym 126d hit-driven lumpiness (netinc)
def f38hv_f38_hit_driven_volatility_niasym_126d_base_v128_signal(netinc):
    d = netinc.diff()
    up = d.where(d > 0).rolling(126, min_periods=30).mean()
    dn = (-d.where(d < 0)).rolling(126, min_periods=30).mean()
    x = (up - dn) / (up + dn).replace(0, np.nan)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# niasym 252d hit-driven lumpiness (netinc)
def f38hv_f38_hit_driven_volatility_niasym_252d_base_v129_signal(netinc):
    d = netinc.diff()
    up = d.where(d > 0).rolling(252, min_periods=60).mean()
    dn = (-d.where(d < 0)).rolling(252, min_periods=60).mean()
    x = (up - dn) / (up + dn).replace(0, np.nan)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ebitdown 252d hit-driven lumpiness (ebit)
def f38hv_f38_hit_driven_volatility_ebitdown_252d_base_v130_signal(ebit):
    x = (_mean(ebit, 252) - _rmin(ebit, 252)) / _std(ebit, 252)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revdsemi 252d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revdsemi_252d_base_v131_signal(revenue):
    lr = _f38hv_relret(revenue)
    x = lr.where(lr < 0).rolling(252, min_periods=63).std()
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revusemi 252d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revusemi_252d_base_v132_signal(revenue):
    lr = _f38hv_relret(revenue)
    x = lr.where(lr > 0).rolling(252, min_periods=63).std()
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revlife 252d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revlife_252d_base_v133_signal(revenue):
    rb = _f38hv_burst(revenue, 126).clip(lower=0)
    dc = (-_f38hv_decay(revenue, 126)).clip(lower=0)
    raw = (rb - dc) / (rb + dc + 1e-9)
    x = raw.ewm(span=63, min_periods=31).mean()
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# earvolr 252d hit-driven lumpiness (netinc,opinc)
def f38hv_f38_hit_driven_volatility_earvolr_252d_base_v134_signal(netinc, opinc):
    nv = _std(netinc, 252)
    ov = _std(opinc, 252)
    x = nv / ov.replace(0, np.nan)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revspkpers 252d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revspkpers_252d_base_v135_signal(revenue):
    a = _f38hv_relret(revenue).abs()
    x = a.rolling(252, min_periods=126).corr(a.shift(5))
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gmrevco 252d hit-driven lumpiness (grossmargin,revenue)
def f38hv_f38_hit_driven_volatility_gmrevco_252d_base_v136_signal(grossmargin, revenue):
    rr = _f38hv_relret(revenue)
    gd = grossmargin.diff()
    x = rr.rolling(252, min_periods=126).corr(gd)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revampz 252d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revampz_252d_base_v137_signal(revenue):
    ap = _f38hv_amp(revenue, 63)
    x = _z(ap, 252)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# niswingz 252d hit-driven lumpiness (netinc)
def f38hv_f38_hit_driven_volatility_niswingz_252d_base_v138_signal(netinc):
    sw = _f38hv_swing(netinc, 63)
    x = _z(sw, 252)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# opburstrank 252d hit-driven lumpiness (opinc)
def f38hv_f38_hit_driven_volatility_opburstrank_252d_base_v139_signal(opinc):
    ob = (opinc - _mean(opinc, 63)) / _std(opinc, 63)
    x = ob.rolling(252, min_periods=126).rank(pct=True) - 0.5
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ebitburstrank 252d hit-driven lumpiness (ebit)
def f38hv_f38_hit_driven_volatility_ebitburstrank_252d_base_v140_signal(ebit):
    eb = (ebit - _mean(ebit, 63)) / _std(ebit, 63)
    x = eb.rolling(252, min_periods=126).rank(pct=True) - 0.5
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revampvol 252d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revampvol_252d_base_v141_signal(revenue):
    ap = _f38hv_amp(revenue, 21)
    x = ap.rolling(252, min_periods=126).std()
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revampvol 126d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revampvol_126d_base_v142_signal(revenue):
    ap = _f38hv_amp(revenue, 21)
    x = ap.rolling(126, min_periods=63).std()
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gmchgskew 126d hit-driven lumpiness (grossmargin)
def f38hv_f38_hit_driven_volatility_gmchgskew_126d_base_v143_signal(grossmargin):
    d = grossmargin.diff()
    x = d.rolling(126, min_periods=63).skew()
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# gmchgvol 252d hit-driven lumpiness (grossmargin)
def f38hv_f38_hit_driven_volatility_gmchgvol_252d_base_v144_signal(grossmargin):
    d = grossmargin.diff()
    x = d.abs().rolling(252, min_periods=126).mean()
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revtail 252d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revtail_252d_base_v145_signal(revenue):
    lr = _f38hv_relret(revenue)
    q95 = lr.rolling(252, min_periods=126).quantile(0.95)
    q50 = lr.rolling(252, min_periods=126).quantile(0.50)
    x = q95 - q50
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# earswingmix 252d hit-driven lumpiness (netinc,ebit)
def f38hv_f38_hit_driven_volatility_earswingmix_252d_base_v146_signal(netinc, ebit):
    ns = _f38hv_swing(netinc, 126)
    es = _f38hv_swing(ebit, 126)
    x = (ns + es) / 2.0
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revqspr 252d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revqspr_252d_base_v147_signal(revenue):
    lr = _f38hv_relret(revenue)
    q90 = lr.rolling(252, min_periods=126).quantile(0.90)
    q10 = lr.rolling(252, min_periods=126).quantile(0.10)
    x = q90 - q10
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# opgear 252d hit-driven lumpiness (opinc,revenue)
def f38hv_f38_hit_driven_volatility_opgear_252d_base_v148_signal(opinc, revenue):
    os = _std(opinc, 252)
    x = os / _mean(revenue, 252).replace(0, np.nan)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# nidown 252d hit-driven lumpiness (netinc)
def f38hv_f38_hit_driven_volatility_nidown_252d_base_v149_signal(netinc):
    x = (_mean(netinc, 252) - _rmin(netinc, 252)) / _std(netinc, 252)
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# revrngspr 252d hit-driven lumpiness (revenue)
def f38hv_f38_hit_driven_volatility_revrngspr_252d_base_v150_signal(revenue):
    hi_s = _rmax(revenue, 63)
    lo_s = _rmin(revenue, 63)
    ps = (revenue - lo_s) / (hi_s - lo_s).replace(0, np.nan)
    hi_l = _rmax(revenue, 252)
    lo_l = _rmin(revenue, 252)
    pl = (revenue - lo_l) / (hi_l - lo_l).replace(0, np.nan)
    x = ps - pl
    b = x
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f38hv_f38_hit_driven_volatility_revrng_63d_base_v076_signal,
    f38hv_f38_hit_driven_volatility_revrng_252d_base_v077_signal,
    f38hv_f38_hit_driven_volatility_revmaxg_126d_base_v078_signal,
    f38hv_f38_hit_driven_volatility_revmaxg_252d_base_v079_signal,
    f38hv_f38_hit_driven_volatility_revming_126d_base_v080_signal,
    f38hv_f38_hit_driven_volatility_gmamp_126d_base_v081_signal,
    f38hv_f38_hit_driven_volatility_gmamp_252d_base_v082_signal,
    f38hv_f38_hit_driven_volatility_gmclust_126d_base_v083_signal,
    f38hv_f38_hit_driven_volatility_nicv_126d_base_v084_signal,
    f38hv_f38_hit_driven_volatility_nicv_252d_base_v085_signal,
    f38hv_f38_hit_driven_volatility_ebitcv_126d_base_v086_signal,
    f38hv_f38_hit_driven_volatility_ebitcv_252d_base_v087_signal,
    f38hv_f38_hit_driven_volatility_revburstsm_126d_base_v088_signal,
    f38hv_f38_hit_driven_volatility_revburstsm_252d_base_v089_signal,
    f38hv_f38_hit_driven_volatility_revcvrank_252d_base_v090_signal,
    f38hv_f38_hit_driven_volatility_revburstrank_252d_base_v091_signal,
    f38hv_f38_hit_driven_volatility_eargear_126d_base_v092_signal,
    f38hv_f38_hit_driven_volatility_eargear_252d_base_v093_signal,
    f38hv_f38_hit_driven_volatility_revfade_126d_base_v094_signal,
    f38hv_f38_hit_driven_volatility_revfade_252d_base_v095_signal,
    f38hv_f38_hit_driven_volatility_opclust_126d_base_v096_signal,
    f38hv_f38_hit_driven_volatility_opclust_252d_base_v097_signal,
    f38hv_f38_hit_driven_volatility_niclust_126d_base_v098_signal,
    f38hv_f38_hit_driven_volatility_niclust_252d_base_v099_signal,
    f38hv_f38_hit_driven_volatility_ebitclust_126d_base_v100_signal,
    f38hv_f38_hit_driven_volatility_ebitclust_252d_base_v101_signal,
    f38hv_f38_hit_driven_volatility_revmad_126d_base_v102_signal,
    f38hv_f38_hit_driven_volatility_revmad_252d_base_v103_signal,
    f38hv_f38_hit_driven_volatility_gmspk_252d_base_v104_signal,
    f38hv_f38_hit_driven_volatility_gmz_126d_base_v105_signal,
    f38hv_f38_hit_driven_volatility_gmskew_252d_base_v106_signal,
    f38hv_f38_hit_driven_volatility_revphase_126d_base_v107_signal,
    f38hv_f38_hit_driven_volatility_revphase_252d_base_v108_signal,
    f38hv_f38_hit_driven_volatility_ebitburst_63d_base_v109_signal,
    f38hv_f38_hit_driven_volatility_ebitburst_126d_base_v110_signal,
    f38hv_f38_hit_driven_volatility_niburst_63d_base_v111_signal,
    f38hv_f38_hit_driven_volatility_niburst_126d_base_v112_signal,
    f38hv_f38_hit_driven_volatility_revvolacc_126d_base_v113_signal,
    f38hv_f38_hit_driven_volatility_revvolacc_252d_base_v114_signal,
    f38hv_f38_hit_driven_volatility_hitcomp_126d_base_v115_signal,
    f38hv_f38_hit_driven_volatility_hitcomp_252d_base_v116_signal,
    f38hv_f38_hit_driven_volatility_revcliff_126d_base_v117_signal,
    f38hv_f38_hit_driven_volatility_revcliff_252d_base_v118_signal,
    f38hv_f38_hit_driven_volatility_opcv_126d_base_v119_signal,
    f38hv_f38_hit_driven_volatility_opcv_252d_base_v120_signal,
    f38hv_f38_hit_driven_volatility_revvolz_252d_base_v121_signal,
    f38hv_f38_hit_driven_volatility_earampratio_252d_base_v122_signal,
    f38hv_f38_hit_driven_volatility_revhits_252d_base_v123_signal,
    f38hv_f38_hit_driven_volatility_revhits_126d_base_v124_signal,
    f38hv_f38_hit_driven_volatility_gmonhit_252d_base_v125_signal,
    f38hv_f38_hit_driven_volatility_revlrng_126d_base_v126_signal,
    f38hv_f38_hit_driven_volatility_revlrng_252d_base_v127_signal,
    f38hv_f38_hit_driven_volatility_niasym_126d_base_v128_signal,
    f38hv_f38_hit_driven_volatility_niasym_252d_base_v129_signal,
    f38hv_f38_hit_driven_volatility_ebitdown_252d_base_v130_signal,
    f38hv_f38_hit_driven_volatility_revdsemi_252d_base_v131_signal,
    f38hv_f38_hit_driven_volatility_revusemi_252d_base_v132_signal,
    f38hv_f38_hit_driven_volatility_revlife_252d_base_v133_signal,
    f38hv_f38_hit_driven_volatility_earvolr_252d_base_v134_signal,
    f38hv_f38_hit_driven_volatility_revspkpers_252d_base_v135_signal,
    f38hv_f38_hit_driven_volatility_gmrevco_252d_base_v136_signal,
    f38hv_f38_hit_driven_volatility_revampz_252d_base_v137_signal,
    f38hv_f38_hit_driven_volatility_niswingz_252d_base_v138_signal,
    f38hv_f38_hit_driven_volatility_opburstrank_252d_base_v139_signal,
    f38hv_f38_hit_driven_volatility_ebitburstrank_252d_base_v140_signal,
    f38hv_f38_hit_driven_volatility_revampvol_252d_base_v141_signal,
    f38hv_f38_hit_driven_volatility_revampvol_126d_base_v142_signal,
    f38hv_f38_hit_driven_volatility_gmchgskew_126d_base_v143_signal,
    f38hv_f38_hit_driven_volatility_gmchgvol_252d_base_v144_signal,
    f38hv_f38_hit_driven_volatility_revtail_252d_base_v145_signal,
    f38hv_f38_hit_driven_volatility_earswingmix_252d_base_v146_signal,
    f38hv_f38_hit_driven_volatility_revqspr_252d_base_v147_signal,
    f38hv_f38_hit_driven_volatility_opgear_252d_base_v148_signal,
    f38hv_f38_hit_driven_volatility_nidown_252d_base_v149_signal,
    f38hv_f38_hit_driven_volatility_revrngspr_252d_base_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]

REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F38_HIT_DRIVEN_VOLATILITY_REGISTRY_076_150 = REGISTRY

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

    print("OK f38_hit_driven_volatility_base_076_150_claude: %d features pass" % n_features)
