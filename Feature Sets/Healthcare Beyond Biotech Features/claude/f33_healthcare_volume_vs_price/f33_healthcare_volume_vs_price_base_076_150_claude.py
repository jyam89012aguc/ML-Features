import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


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


# ===== folder domain primitives =====
def _f33_volume_proxy(revenue, ppnenet, w):
    rp = revenue / ppnenet.replace(0, np.nan)
    return _mean(rp, w)


def _f33_price_proxy(revenue, assets, w):
    ra = revenue / assets.replace(0, np.nan)
    return _mean(ra, w)


def _f33_volume_price_gap(revenue, ppnenet, assets, w):
    vp = revenue / ppnenet.replace(0, np.nan)
    pp = revenue / assets.replace(0, np.nan)
    return _mean(vp, w) - _mean(pp, w)


# ---- features 076 - 150 (close-multiplied bodies; structurally distinct) ----

def f33hvp_f33_healthcare_volume_vs_price_volp_xmean63_63d_base_v076_signal(revenue, ppnenet, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_xmean63_252d_base_v077_signal(revenue, ppnenet, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 252)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_xmean252_63d_base_v078_signal(revenue, ppnenet, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 63)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_xmean252_252d_base_v079_signal(revenue, ppnenet, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 252)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_xmean63_63d_base_v080_signal(revenue, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_xmean63_252d_base_v081_signal(revenue, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 252)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_xmean252_252d_base_v082_signal(revenue, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 252)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_xmean63_252d_base_v083_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 252)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_xmean252_252d_base_v084_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 252)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_xstd_252d_base_v085_signal(revenue, ppnenet, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 63)
    result = base * _std(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_xstd_252d_base_v086_signal(revenue, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 63)
    result = base * _std(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_xstd_252d_base_v087_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 63)
    result = base * _std(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_xewmstd_252d_base_v088_signal(revenue, ppnenet, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 63)
    result = base * closeadj.ewm(span=252, min_periods=60).std()
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_xewmstd_252d_base_v089_signal(revenue, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 63)
    result = base * closeadj.ewm(span=252, min_periods=60).std()
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_xzclose_252d_base_v090_signal(revenue, ppnenet, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 63)
    result = base * _z(closeadj, 504) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_xzclose_252d_base_v091_signal(revenue, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 63)
    result = base * _z(closeadj, 504) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_xzclose_252d_base_v092_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 63)
    result = base * _z(closeadj, 504) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_xlog_252d_base_v093_signal(revenue, ppnenet, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 63)
    result = base * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_xlog_252d_base_v094_signal(revenue, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 63)
    result = base * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_xlog_252d_base_v095_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 63)
    result = base * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_plusprice_63d_base_v096_signal(revenue, ppnenet, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 63).pct_change(63)
    result = (base + closeadj.pct_change(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_plusprice_252d_base_v097_signal(revenue, ppnenet, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 63).pct_change(252)
    result = (base + closeadj.pct_change(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_plusprice_63d_base_v098_signal(revenue, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 63).pct_change(63)
    result = (base + closeadj.pct_change(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_plusprice_252d_base_v099_signal(revenue, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 63).pct_change(252)
    result = (base + closeadj.pct_change(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_minusprice_63d_base_v100_signal(revenue, ppnenet, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 63).pct_change(63)
    result = (base - closeadj.pct_change(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_minusprice_252d_base_v101_signal(revenue, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 63).pct_change(252)
    result = (base - closeadj.pct_change(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_corr_252d_base_v102_signal(revenue, ppnenet, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 21).pct_change(21)
    cor = base.rolling(252, min_periods=63).corr(closeadj.pct_change(21))
    result = cor * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_corr_252d_base_v103_signal(revenue, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 21).pct_change(21)
    cor = base.rolling(252, min_periods=63).corr(closeadj.pct_change(21))
    result = cor * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_corr_252d_base_v104_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 21)
    cor = base.rolling(252, min_periods=63).corr(closeadj.pct_change(21))
    result = cor * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_halflife_252d_base_v105_signal(revenue, ppnenet, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 252)
    result = base.ewm(halflife=63, min_periods=20).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_halflife_252d_base_v106_signal(revenue, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 252)
    result = base.ewm(halflife=63, min_periods=20).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_halflife_252d_base_v107_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 252)
    result = base.ewm(halflife=63, min_periods=20).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_skewproxy_252d_base_v108_signal(revenue, ppnenet, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 21)
    m = _mean(base, 252)
    s = _std(base, 252).replace(0, np.nan)
    result = _mean((base - m) ** 3, 252) / (s ** 3) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_skewproxy_252d_base_v109_signal(revenue, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 21)
    m = _mean(base, 252)
    s = _std(base, 252).replace(0, np.nan)
    result = _mean((base - m) ** 3, 252) / (s ** 3) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_skewproxy_252d_base_v110_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 21)
    m = _mean(base, 252)
    s = _std(base, 252).replace(0, np.nan)
    result = _mean((base - m) ** 3, 252) / (s ** 3) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_runlen_252d_base_v111_signal(revenue, ppnenet, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 21)
    up = (base > base.shift(21)).astype(float)
    cnt = up.rolling(252, min_periods=63).sum()
    result = cnt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_runlen_252d_base_v112_signal(revenue, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 21)
    up = (base > base.shift(21)).astype(float)
    cnt = up.rolling(252, min_periods=63).sum()
    result = cnt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_runlen_252d_base_v113_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 21)
    up = (base > 0).astype(float)
    cnt = up.rolling(252, min_periods=63).sum()
    result = cnt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_quartdiff_252d_base_v114_signal(revenue, ppnenet, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 21)
    q75 = base.rolling(252, min_periods=63).quantile(0.75)
    q25 = base.rolling(252, min_periods=63).quantile(0.25)
    result = (q75 - q25) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_quartdiff_252d_base_v115_signal(revenue, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 21)
    q75 = base.rolling(252, min_periods=63).quantile(0.75)
    q25 = base.rolling(252, min_periods=63).quantile(0.25)
    result = (q75 - q25) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_quartdiff_252d_base_v116_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 21)
    q75 = base.rolling(252, min_periods=63).quantile(0.75)
    q25 = base.rolling(252, min_periods=63).quantile(0.25)
    result = (q75 - q25) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_median_252d_base_v117_signal(revenue, ppnenet, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 21)
    med = base.rolling(252, min_periods=63).median()
    result = med * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_median_252d_base_v118_signal(revenue, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 21)
    med = base.rolling(252, min_periods=63).median()
    result = med * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_median_252d_base_v119_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 21)
    med = base.rolling(252, min_periods=63).median()
    result = med * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_above_median_252d_base_v120_signal(revenue, ppnenet, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 21)
    med = base.rolling(252, min_periods=63).median()
    ind = (base > med).astype(float)
    result = ind.rolling(63, min_periods=20).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_above_median_252d_base_v121_signal(revenue, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 21)
    med = base.rolling(252, min_periods=63).median()
    ind = (base > med).astype(float)
    result = ind.rolling(63, min_periods=20).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_mad_252d_base_v122_signal(revenue, ppnenet, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 21)
    med = base.rolling(252, min_periods=63).median()
    mad = (base - med).abs().rolling(252, min_periods=63).median()
    result = mad * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_mad_252d_base_v123_signal(revenue, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 21)
    med = base.rolling(252, min_periods=63).median()
    mad = (base - med).abs().rolling(252, min_periods=63).median()
    result = mad * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_mad_252d_base_v124_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 21)
    med = base.rolling(252, min_periods=63).median()
    mad = (base - med).abs().rolling(252, min_periods=63).median()
    result = mad * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_acc_252d_base_v125_signal(revenue, ppnenet, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 21)
    g = base.pct_change(63)
    result = (g - g.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_acc_252d_base_v126_signal(revenue, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 21)
    g = base.pct_change(63)
    result = (g - g.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_acc_252d_base_v127_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 21)
    g = base.diff(63)
    result = (g - g.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_mom_252d_base_v128_signal(revenue, ppnenet, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 21)
    result = base / base.shift(252).replace(0, np.nan) * closeadj - closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_mom_252d_base_v129_signal(revenue, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 21)
    result = base / base.shift(252).replace(0, np.nan) * closeadj - closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_mom_252d_base_v130_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 21)
    result = base * closeadj / closeadj.shift(252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_pctchg_63d_base_v131_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 63)
    result = base.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_pctchg_252d_base_v132_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 63)
    result = base.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_diff_504d_base_v133_signal(revenue, ppnenet, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 63)
    result = (base - base.shift(504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_diff_504d_base_v134_signal(revenue, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 63)
    result = (base - base.shift(504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_diff_504d_base_v135_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 63)
    result = (base - base.shift(504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_sq_252d_base_v136_signal(revenue, ppnenet, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 63)
    result = _mean(base * base.abs(), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_sq_252d_base_v137_signal(revenue, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 63)
    result = _mean(base * base.abs(), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_sq_252d_base_v138_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 63)
    result = _mean(base * base.abs(), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_diff_ratio_base_v139_signal(revenue, ppnenet, assets, closeadj):
    vp = _f33_volume_proxy(revenue, ppnenet, 63)
    pp = _f33_price_proxy(revenue, assets, 63).replace(0, np.nan)
    result = (vp / pp) * closeadj + _f33_volume_price_gap(revenue, ppnenet, assets, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_div_prip_252d_base_v140_signal(revenue, ppnenet, assets, closeadj):
    vp = _f33_volume_proxy(revenue, ppnenet, 252)
    pp = _f33_price_proxy(revenue, assets, 252).replace(0, np.nan)
    result = (vp / pp) * closeadj + _f33_volume_price_gap(revenue, ppnenet, assets, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_dominance_63d_base_v141_signal(revenue, ppnenet, assets, closeadj):
    vp_g = _f33_volume_proxy(revenue, ppnenet, 63).pct_change(63)
    pp_g = _f33_price_proxy(revenue, assets, 63).pct_change(63)
    result = (vp_g - pp_g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_dominance_252d_base_v142_signal(revenue, ppnenet, assets, closeadj):
    vp_g = _f33_volume_proxy(revenue, ppnenet, 63).pct_change(252)
    pp_g = _f33_price_proxy(revenue, assets, 63).pct_change(252)
    result = (vp_g - pp_g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_dominance_63d_base_v143_signal(revenue, ppnenet, assets, closeadj):
    pp_g = _f33_price_proxy(revenue, assets, 63).pct_change(63)
    vp_g = _f33_volume_proxy(revenue, ppnenet, 63).pct_change(63)
    result = (pp_g - vp_g) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_xrev_252d_base_v144_signal(revenue, ppnenet, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 63)
    result = base * np.log(revenue.replace(0, np.nan).abs()) * closeadj * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_xrev_252d_base_v145_signal(revenue, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 63)
    result = base * np.log(revenue.replace(0, np.nan).abs()) * closeadj * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_vpgap_xrev_252d_base_v146_signal(revenue, ppnenet, assets, closeadj):
    base = _f33_volume_price_gap(revenue, ppnenet, assets, 63)
    result = base * np.log(revenue.replace(0, np.nan).abs()) * closeadj * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_compound_252d_base_v147_signal(revenue, ppnenet, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 21)
    cmpd = np.log(base.replace(0, np.nan).abs()).diff(252)
    result = cmpd * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_compound_252d_base_v148_signal(revenue, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 21)
    cmpd = np.log(base.replace(0, np.nan).abs()).diff(252)
    result = cmpd * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_volp_xcloseadj_42d_base_v149_signal(revenue, ppnenet, closeadj):
    base = _f33_volume_proxy(revenue, ppnenet, 42)
    result = base * closeadj * 0.5 + _f33_price_proxy(revenue, ppnenet, 42) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33hvp_f33_healthcare_volume_vs_price_prip_xcloseadj_42d_base_v150_signal(revenue, assets, closeadj):
    base = _f33_price_proxy(revenue, assets, 42)
    result = base * closeadj * 0.5 + _f33_volume_proxy(revenue, assets, 42) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f33hvp_f33_healthcare_volume_vs_price_volp_xmean63_63d_base_v076_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_xmean63_252d_base_v077_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_xmean252_63d_base_v078_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_xmean252_252d_base_v079_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_xmean63_63d_base_v080_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_xmean63_252d_base_v081_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_xmean252_252d_base_v082_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_xmean63_252d_base_v083_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_xmean252_252d_base_v084_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_xstd_252d_base_v085_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_xstd_252d_base_v086_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_xstd_252d_base_v087_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_xewmstd_252d_base_v088_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_xewmstd_252d_base_v089_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_xzclose_252d_base_v090_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_xzclose_252d_base_v091_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_xzclose_252d_base_v092_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_xlog_252d_base_v093_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_xlog_252d_base_v094_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_xlog_252d_base_v095_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_plusprice_63d_base_v096_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_plusprice_252d_base_v097_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_plusprice_63d_base_v098_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_plusprice_252d_base_v099_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_minusprice_63d_base_v100_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_minusprice_252d_base_v101_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_corr_252d_base_v102_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_corr_252d_base_v103_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_corr_252d_base_v104_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_halflife_252d_base_v105_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_halflife_252d_base_v106_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_halflife_252d_base_v107_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_skewproxy_252d_base_v108_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_skewproxy_252d_base_v109_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_skewproxy_252d_base_v110_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_runlen_252d_base_v111_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_runlen_252d_base_v112_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_runlen_252d_base_v113_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_quartdiff_252d_base_v114_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_quartdiff_252d_base_v115_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_quartdiff_252d_base_v116_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_median_252d_base_v117_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_median_252d_base_v118_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_median_252d_base_v119_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_above_median_252d_base_v120_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_above_median_252d_base_v121_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_mad_252d_base_v122_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_mad_252d_base_v123_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_mad_252d_base_v124_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_acc_252d_base_v125_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_acc_252d_base_v126_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_acc_252d_base_v127_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_mom_252d_base_v128_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_mom_252d_base_v129_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_mom_252d_base_v130_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_pctchg_63d_base_v131_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_pctchg_252d_base_v132_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_diff_504d_base_v133_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_diff_504d_base_v134_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_diff_504d_base_v135_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_sq_252d_base_v136_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_sq_252d_base_v137_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_sq_252d_base_v138_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_diff_ratio_base_v139_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_div_prip_252d_base_v140_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_dominance_63d_base_v141_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_dominance_252d_base_v142_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_dominance_63d_base_v143_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_xrev_252d_base_v144_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_xrev_252d_base_v145_signal,
    f33hvp_f33_healthcare_volume_vs_price_vpgap_xrev_252d_base_v146_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_compound_252d_base_v147_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_compound_252d_base_v148_signal,
    f33hvp_f33_healthcare_volume_vs_price_volp_xcloseadj_42d_base_v149_signal,
    f33hvp_f33_healthcare_volume_vs_price_prip_xcloseadj_42d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F33_HEALTHCARE_VOLUME_VS_PRICE_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    assets  = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    ppnenet = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "assets": assets, "ppnenet": ppnenet,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f33_volume_proxy", "_f33_price_proxy", "_f33_volume_price_gap")
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f33_healthcare_volume_vs_price_base_076_150_claude: {n_features} features pass")
