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
def _f32_rev_per_asset(revenue, assets):
    return revenue / assets.replace(0, np.nan)


def _f32_pricing_uplift(revenue, ppnenet, w):
    rpa = revenue / ppnenet.replace(0, np.nan)
    return rpa - rpa.shift(w)


def _f32_unit_economics_lift(revenue, assets, w):
    rpa = revenue / assets.replace(0, np.nan)
    return _mean(rpa, w) - _mean(rpa, w).shift(w)


# ---- features 076 - 150 ----

def f32hpp_f32_healthcare_pricing_power_rpaxmean63_base_v076_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpaxmean252_base_v077_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    result = base * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_pp_base_v078_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan)
    result = base * closeadj + _f32_rev_per_asset(revenue, ppnenet) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_pp_21d_base_v079_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan)
    result = _mean(base, 21) * closeadj + _f32_rev_per_asset(revenue, ppnenet) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_pp_63d_base_v080_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan)
    result = _mean(base, 63) * closeadj + _f32_rev_per_asset(revenue, ppnenet) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_pp_252d_base_v081_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan)
    result = _mean(base, 252) * closeadj + _f32_rev_per_asset(revenue, ppnenet) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_pp_504d_base_v082_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan)
    result = _mean(base, 504) * closeadj + _f32_rev_per_asset(revenue, ppnenet) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpapp_std_63d_base_v083_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan)
    result = _std(base, 63) * closeadj + _f32_rev_per_asset(revenue, ppnenet) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpapp_std_252d_base_v084_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan)
    result = _std(base, 252) * closeadj + _f32_rev_per_asset(revenue, ppnenet) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpapp_z_252d_base_v085_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan)
    result = _z(base, 252) * closeadj + _f32_rev_per_asset(revenue, ppnenet) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpapp_z_504d_base_v086_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan)
    result = _z(base, 504) * closeadj + _f32_rev_per_asset(revenue, ppnenet) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpapp_ema_63d_base_v087_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan)
    result = base.ewm(span=63, min_periods=20).mean() * closeadj + _f32_rev_per_asset(revenue, ppnenet) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpapp_ema_252d_base_v088_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan)
    result = base.ewm(span=252, min_periods=60).mean() * closeadj + _f32_rev_per_asset(revenue, ppnenet) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpapp_rank_252d_base_v089_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan)
    rank = base.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj + _f32_rev_per_asset(revenue, ppnenet) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpapp_rank_504d_base_v090_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan)
    rank = base.rolling(504, min_periods=126).rank(pct=True)
    result = rank * closeadj + _f32_rev_per_asset(revenue, ppnenet) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpapp_sq_252d_base_v091_signal(revenue, ppnenet, closeadj):
    base = revenue / ppnenet.replace(0, np.nan)
    result = _mean(base * base.abs(), 252) * closeadj + _f32_rev_per_asset(revenue, ppnenet) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_diff_504d_base_v092_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    result = (base - base.shift(504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_pctchg_504d_base_v093_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    result = base.pct_change(504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_xstd_63d_base_v094_signal(revenue, ppnenet, closeadj):
    result = _f32_pricing_uplift(revenue, ppnenet, 63) * _std(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_xstd_252d_base_v095_signal(revenue, ppnenet, closeadj):
    result = _f32_pricing_uplift(revenue, ppnenet, 252) * _std(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_xzclose_252d_base_v096_signal(revenue, ppnenet, closeadj):
    result = _f32_pricing_uplift(revenue, ppnenet, 252) * _z(closeadj, 504) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_xlog_252d_base_v097_signal(revenue, ppnenet, closeadj):
    result = _f32_pricing_uplift(revenue, ppnenet, 252) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_xewmstd_252d_base_v098_signal(revenue, ppnenet, closeadj):
    result = _f32_pricing_uplift(revenue, ppnenet, 252) * closeadj.ewm(span=252, min_periods=60).std()
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_xcorr_252d_base_v099_signal(revenue, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 63)
    cor = base.rolling(252, min_periods=63).corr(closeadj.pct_change(63))
    result = cor * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_halflife_252d_base_v100_signal(revenue, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 252)
    result = base.ewm(halflife=63, min_periods=20).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitl_xstd_252d_base_v101_signal(revenue, assets, closeadj):
    result = _f32_unit_economics_lift(revenue, assets, 252) * _std(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitl_xzclose_252d_base_v102_signal(revenue, assets, closeadj):
    result = _f32_unit_economics_lift(revenue, assets, 252) * _z(closeadj, 504) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitl_xlog_252d_base_v103_signal(revenue, assets, closeadj):
    result = _f32_unit_economics_lift(revenue, assets, 252) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitl_xewmstd_252d_base_v104_signal(revenue, assets, closeadj):
    result = _f32_unit_economics_lift(revenue, assets, 252) * closeadj.ewm(span=252, min_periods=60).std()
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitl_halflife_252d_base_v105_signal(revenue, assets, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 252)
    result = base.ewm(halflife=63, min_periods=20).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitl_xprice_42d_base_v106_signal(revenue, assets, closeadj):
    result = _f32_unit_economics_lift(revenue, assets, 42) * _mean(closeadj, 42) * closeadj * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitl_xprice_189d_base_v107_signal(revenue, assets, closeadj):
    result = _f32_unit_economics_lift(revenue, assets, 189) * _mean(closeadj, 189) * closeadj * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitl_xprice_378d_base_v108_signal(revenue, assets, closeadj):
    result = _f32_unit_economics_lift(revenue, assets, 378) * _mean(closeadj, 252) * closeadj * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_compound_63d_base_v109_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    cmpd = np.log(base.replace(0, np.nan).abs()).diff(63)
    result = cmpd * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_compound_252d_base_v110_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    cmpd = np.log(base.replace(0, np.nan).abs()).diff(252)
    result = cmpd * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_acc_252d_base_v111_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    g = base.pct_change(63)
    result = (g - g.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_acc_504d_base_v112_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    g = base.pct_change(126)
    result = (g - g.shift(126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_signminusrev_63d_base_v113_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    s1 = np.sign(base.pct_change(63))
    s2 = np.sign(revenue.pct_change(63))
    result = (s1 - s2) * _mean(closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_signminusrev_252d_base_v114_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    s1 = np.sign(base.pct_change(252))
    s2 = np.sign(revenue.pct_change(252))
    result = (s1 - s2) * _mean(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_minusrpapp_63d_base_v115_signal(revenue, assets, ppnenet, closeadj):
    a = _f32_rev_per_asset(revenue, assets)
    b = revenue / ppnenet.replace(0, np.nan)
    result = _mean(a - b * 0.001, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_minusrpapp_252d_base_v116_signal(revenue, assets, ppnenet, closeadj):
    a = _f32_rev_per_asset(revenue, assets)
    b = revenue / ppnenet.replace(0, np.nan)
    result = _mean(a - b * 0.001, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_cumsum_252d_base_v117_signal(revenue, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 21)
    result = base.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_cumsum_504d_base_v118_signal(revenue, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 63)
    result = base.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitl_cumsum_252d_base_v119_signal(revenue, assets, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 21)
    result = base.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitl_cumsum_504d_base_v120_signal(revenue, assets, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 63)
    result = base.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_skewproxy_252d_base_v121_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    m = _mean(base, 252)
    s = _std(base, 252).replace(0, np.nan)
    result = _mean((base - m) ** 3, 252) / (s ** 3) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_skewproxy_504d_base_v122_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    m = _mean(base, 504)
    s = _std(base, 504).replace(0, np.nan)
    result = _mean((base - m) ** 3, 504) / (s ** 3) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_kurt_252d_base_v123_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    m = _mean(base, 252)
    s = _std(base, 252).replace(0, np.nan)
    result = _mean((base - m) ** 4, 252) / (s ** 4) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_skewproxy_252d_base_v124_signal(revenue, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 63)
    m = _mean(base, 252)
    s = _std(base, 252).replace(0, np.nan)
    result = _mean((base - m) ** 3, 252) / (s ** 3) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_kurt_252d_base_v125_signal(revenue, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 63)
    m = _mean(base, 252)
    s = _std(base, 252).replace(0, np.nan)
    result = _mean((base - m) ** 4, 252) / (s ** 4) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_plusprice_63d_base_v126_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets).pct_change(63)
    result = (base + closeadj.pct_change(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_plusprice_252d_base_v127_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets).pct_change(252)
    result = (base + closeadj.pct_change(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_minusprice_63d_base_v128_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets).pct_change(63)
    result = (base - closeadj.pct_change(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_minusprice_252d_base_v129_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets).pct_change(252)
    result = (base - closeadj.pct_change(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_pearson_252d_base_v130_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets).pct_change(21)
    cor = base.rolling(252, min_periods=63).corr(closeadj.pct_change(21))
    result = cor * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_pearson_504d_base_v131_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets).pct_change(63)
    cor = base.rolling(504, min_periods=126).corr(closeadj.pct_change(63))
    result = cor * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_pearson_252d_base_v132_signal(revenue, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 21)
    cor = base.rolling(252, min_periods=63).corr(closeadj.pct_change(21))
    result = cor * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitl_pearson_252d_base_v133_signal(revenue, assets, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 21)
    cor = base.rolling(252, min_periods=63).corr(closeadj.pct_change(21))
    result = cor * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_mom_63d_base_v134_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    result = base / base.shift(63).replace(0, np.nan) * closeadj - closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_mom_252d_base_v135_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    result = base / base.shift(252).replace(0, np.nan) * closeadj - closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_mom_252d_base_v136_signal(revenue, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 63)
    result = base * closeadj / closeadj.shift(252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_runlen_252d_base_v137_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    up = (base > base.shift(21)).astype(float)
    cnt = up.rolling(252, min_periods=63).sum()
    result = cnt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_runlen_504d_base_v138_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    up = (base > base.shift(63)).astype(float)
    cnt = up.rolling(504, min_periods=126).sum()
    result = cnt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_runlen_252d_base_v139_signal(revenue, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 21)
    up = (base > 0).astype(float)
    cnt = up.rolling(252, min_periods=63).sum()
    result = cnt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_runlen_504d_base_v140_signal(revenue, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 63)
    up = (base > 0).astype(float)
    cnt = up.rolling(504, min_periods=126).sum()
    result = cnt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitl_runlen_252d_base_v141_signal(revenue, assets, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 21)
    up = (base > 0).astype(float)
    cnt = up.rolling(252, min_periods=63).sum()
    result = cnt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_quartdiff_252d_base_v142_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    q75 = base.rolling(252, min_periods=63).quantile(0.75)
    q25 = base.rolling(252, min_periods=63).quantile(0.25)
    result = (q75 - q25) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_quartdiff_504d_base_v143_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    q75 = base.rolling(504, min_periods=126).quantile(0.75)
    q25 = base.rolling(504, min_periods=126).quantile(0.25)
    result = (q75 - q25) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_quartdiff_252d_base_v144_signal(revenue, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 63)
    q75 = base.rolling(252, min_periods=63).quantile(0.75)
    q25 = base.rolling(252, min_periods=63).quantile(0.25)
    result = (q75 - q25) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_medabsdev_252d_base_v145_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    med = base.rolling(252, min_periods=63).median()
    mad = (base - med).abs().rolling(252, min_periods=63).median()
    result = mad * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_medabsdev_252d_base_v146_signal(revenue, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 21)
    med = base.rolling(252, min_periods=63).median()
    mad = (base - med).abs().rolling(252, min_periods=63).median()
    result = mad * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_unitl_medabsdev_252d_base_v147_signal(revenue, assets, closeadj):
    base = _f32_unit_economics_lift(revenue, assets, 21)
    med = base.rolling(252, min_periods=63).median()
    mad = (base - med).abs().rolling(252, min_periods=63).median()
    result = mad * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_above_median_252d_base_v148_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    med = base.rolling(252, min_periods=63).median()
    ind = (base > med).astype(float)
    result = ind.rolling(63, min_periods=20).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_rpa_median_252d_base_v149_signal(revenue, assets, closeadj):
    base = _f32_rev_per_asset(revenue, assets)
    med = base.rolling(252, min_periods=63).median()
    result = med * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32hpp_f32_healthcare_pricing_power_uplift_xmedian_504d_base_v150_signal(revenue, ppnenet, closeadj):
    base = _f32_pricing_uplift(revenue, ppnenet, 63)
    med = base.rolling(504, min_periods=126).median()
    result = med * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f32hpp_f32_healthcare_pricing_power_rpaxmean63_base_v076_signal,
    f32hpp_f32_healthcare_pricing_power_rpaxmean252_base_v077_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_pp_base_v078_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_pp_21d_base_v079_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_pp_63d_base_v080_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_pp_252d_base_v081_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_pp_504d_base_v082_signal,
    f32hpp_f32_healthcare_pricing_power_rpapp_std_63d_base_v083_signal,
    f32hpp_f32_healthcare_pricing_power_rpapp_std_252d_base_v084_signal,
    f32hpp_f32_healthcare_pricing_power_rpapp_z_252d_base_v085_signal,
    f32hpp_f32_healthcare_pricing_power_rpapp_z_504d_base_v086_signal,
    f32hpp_f32_healthcare_pricing_power_rpapp_ema_63d_base_v087_signal,
    f32hpp_f32_healthcare_pricing_power_rpapp_ema_252d_base_v088_signal,
    f32hpp_f32_healthcare_pricing_power_rpapp_rank_252d_base_v089_signal,
    f32hpp_f32_healthcare_pricing_power_rpapp_rank_504d_base_v090_signal,
    f32hpp_f32_healthcare_pricing_power_rpapp_sq_252d_base_v091_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_diff_504d_base_v092_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_pctchg_504d_base_v093_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_xstd_63d_base_v094_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_xstd_252d_base_v095_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_xzclose_252d_base_v096_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_xlog_252d_base_v097_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_xewmstd_252d_base_v098_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_xcorr_252d_base_v099_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_halflife_252d_base_v100_signal,
    f32hpp_f32_healthcare_pricing_power_unitl_xstd_252d_base_v101_signal,
    f32hpp_f32_healthcare_pricing_power_unitl_xzclose_252d_base_v102_signal,
    f32hpp_f32_healthcare_pricing_power_unitl_xlog_252d_base_v103_signal,
    f32hpp_f32_healthcare_pricing_power_unitl_xewmstd_252d_base_v104_signal,
    f32hpp_f32_healthcare_pricing_power_unitl_halflife_252d_base_v105_signal,
    f32hpp_f32_healthcare_pricing_power_unitl_xprice_42d_base_v106_signal,
    f32hpp_f32_healthcare_pricing_power_unitl_xprice_189d_base_v107_signal,
    f32hpp_f32_healthcare_pricing_power_unitl_xprice_378d_base_v108_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_compound_63d_base_v109_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_compound_252d_base_v110_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_acc_252d_base_v111_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_acc_504d_base_v112_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_signminusrev_63d_base_v113_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_signminusrev_252d_base_v114_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_minusrpapp_63d_base_v115_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_minusrpapp_252d_base_v116_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_cumsum_252d_base_v117_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_cumsum_504d_base_v118_signal,
    f32hpp_f32_healthcare_pricing_power_unitl_cumsum_252d_base_v119_signal,
    f32hpp_f32_healthcare_pricing_power_unitl_cumsum_504d_base_v120_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_skewproxy_252d_base_v121_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_skewproxy_504d_base_v122_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_kurt_252d_base_v123_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_skewproxy_252d_base_v124_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_kurt_252d_base_v125_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_plusprice_63d_base_v126_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_plusprice_252d_base_v127_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_minusprice_63d_base_v128_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_minusprice_252d_base_v129_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_pearson_252d_base_v130_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_pearson_504d_base_v131_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_pearson_252d_base_v132_signal,
    f32hpp_f32_healthcare_pricing_power_unitl_pearson_252d_base_v133_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_mom_63d_base_v134_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_mom_252d_base_v135_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_mom_252d_base_v136_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_runlen_252d_base_v137_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_runlen_504d_base_v138_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_runlen_252d_base_v139_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_runlen_504d_base_v140_signal,
    f32hpp_f32_healthcare_pricing_power_unitl_runlen_252d_base_v141_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_quartdiff_252d_base_v142_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_quartdiff_504d_base_v143_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_quartdiff_252d_base_v144_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_medabsdev_252d_base_v145_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_medabsdev_252d_base_v146_signal,
    f32hpp_f32_healthcare_pricing_power_unitl_medabsdev_252d_base_v147_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_above_median_252d_base_v148_signal,
    f32hpp_f32_healthcare_pricing_power_rpa_median_252d_base_v149_signal,
    f32hpp_f32_healthcare_pricing_power_uplift_xmedian_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F32_HEALTHCARE_PRICING_POWER_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f32_rev_per_asset", "_f32_pricing_uplift", "_f32_unit_economics_lift")
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
    print(f"OK f32_healthcare_pricing_power_base_076_150_claude: {n_features} features pass")
