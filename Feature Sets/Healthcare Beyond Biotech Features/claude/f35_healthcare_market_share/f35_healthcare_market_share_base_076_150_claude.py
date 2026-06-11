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
def _f35_self_growth(revenue, w):
    return revenue.pct_change(w)


def _f35_share_gain_proxy(revenue, w):
    g = revenue.pct_change(w)
    return g - _mean(g, w * 2)


def _f35_relative_growth_score(revenue, ebitda, w):
    rg = revenue.pct_change(w)
    eg = ebitda.pct_change(w)
    return _mean(rg + eg, w) - _mean(rg, w * 2)


# ---- features 076 - 150 (close-multiplied bodies; structurally distinct) ----

def f35hms_f35_healthcare_market_share_selfg_xmean63_63d_base_v076_signal(revenue, closeadj):
    result = _f35_self_growth(revenue, 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfg_xmean63_252d_base_v077_signal(revenue, closeadj):
    result = _f35_self_growth(revenue, 252) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfg_xmean252_252d_base_v078_signal(revenue, closeadj):
    result = _f35_self_growth(revenue, 252) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegain_xmean63_63d_base_v079_signal(revenue, closeadj):
    result = _f35_share_gain_proxy(revenue, 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegain_xmean63_252d_base_v080_signal(revenue, closeadj):
    result = _f35_share_gain_proxy(revenue, 252) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegain_xmean252_252d_base_v081_signal(revenue, closeadj):
    result = _f35_share_gain_proxy(revenue, 252) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativeg_xmean63_63d_base_v082_signal(revenue, ebitda, closeadj):
    result = _f35_relative_growth_score(revenue, ebitda, 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativeg_xmean252_252d_base_v083_signal(revenue, ebitda, closeadj):
    result = _f35_relative_growth_score(revenue, ebitda, 252) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfg_xstd_252d_base_v084_signal(revenue, closeadj):
    result = _f35_self_growth(revenue, 63) * _std(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegain_xstd_252d_base_v085_signal(revenue, closeadj):
    result = _f35_share_gain_proxy(revenue, 63) * _std(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativeg_xstd_252d_base_v086_signal(revenue, ebitda, closeadj):
    result = _f35_relative_growth_score(revenue, ebitda, 63) * _std(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfg_xewmstd_252d_base_v087_signal(revenue, closeadj):
    result = _f35_self_growth(revenue, 63) * closeadj.ewm(span=252, min_periods=60).std()
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegain_xewmstd_252d_base_v088_signal(revenue, closeadj):
    result = _f35_share_gain_proxy(revenue, 63) * closeadj.ewm(span=252, min_periods=60).std()
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativeg_xewmstd_252d_base_v089_signal(revenue, ebitda, closeadj):
    result = _f35_relative_growth_score(revenue, ebitda, 63) * closeadj.ewm(span=252, min_periods=60).std()
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfg_xzclose_252d_base_v090_signal(revenue, closeadj):
    result = _f35_self_growth(revenue, 63) * _z(closeadj, 504) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegain_xzclose_252d_base_v091_signal(revenue, closeadj):
    result = _f35_share_gain_proxy(revenue, 63) * _z(closeadj, 504) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativeg_xzclose_252d_base_v092_signal(revenue, ebitda, closeadj):
    result = _f35_relative_growth_score(revenue, ebitda, 63) * _z(closeadj, 504) * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfg_xlog_252d_base_v093_signal(revenue, closeadj):
    result = _f35_self_growth(revenue, 63) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegain_xlog_252d_base_v094_signal(revenue, closeadj):
    result = _f35_share_gain_proxy(revenue, 63) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativeg_xlog_252d_base_v095_signal(revenue, ebitda, closeadj):
    result = _f35_relative_growth_score(revenue, ebitda, 63) * np.log(closeadj.replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfg_plusprice_63d_base_v096_signal(revenue, closeadj):
    base = _f35_self_growth(revenue, 63)
    result = (base + closeadj.pct_change(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfg_minusprice_63d_base_v097_signal(revenue, closeadj):
    base = _f35_self_growth(revenue, 63)
    result = (base - closeadj.pct_change(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegain_plusprice_63d_base_v098_signal(revenue, closeadj):
    base = _f35_share_gain_proxy(revenue, 63)
    result = (base + closeadj.pct_change(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegain_minusprice_63d_base_v099_signal(revenue, closeadj):
    base = _f35_share_gain_proxy(revenue, 63)
    result = (base - closeadj.pct_change(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativeg_plusprice_252d_base_v100_signal(revenue, ebitda, closeadj):
    base = _f35_relative_growth_score(revenue, ebitda, 252)
    result = (base + closeadj.pct_change(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfg_corr_252d_base_v101_signal(revenue, closeadj):
    base = _f35_self_growth(revenue, 21)
    cor = base.rolling(252, min_periods=63).corr(closeadj.pct_change(21))
    result = cor * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegain_corr_252d_base_v102_signal(revenue, closeadj):
    base = _f35_share_gain_proxy(revenue, 21)
    cor = base.rolling(252, min_periods=63).corr(closeadj.pct_change(21))
    result = cor * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativeg_corr_252d_base_v103_signal(revenue, ebitda, closeadj):
    base = _f35_relative_growth_score(revenue, ebitda, 21)
    cor = base.rolling(252, min_periods=63).corr(closeadj.pct_change(21))
    result = cor * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfg_halflife_252d_base_v104_signal(revenue, closeadj):
    base = _f35_self_growth(revenue, 252)
    result = base.ewm(halflife=63, min_periods=20).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegain_halflife_252d_base_v105_signal(revenue, closeadj):
    base = _f35_share_gain_proxy(revenue, 252)
    result = base.ewm(halflife=63, min_periods=20).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativeg_halflife_252d_base_v106_signal(revenue, ebitda, closeadj):
    base = _f35_relative_growth_score(revenue, ebitda, 252)
    result = base.ewm(halflife=63, min_periods=20).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfg_skewproxy_252d_base_v107_signal(revenue, closeadj):
    base = _f35_self_growth(revenue, 21)
    m = _mean(base, 252)
    s = _std(base, 252).replace(0, np.nan)
    result = _mean((base - m) ** 3, 252) / (s ** 3) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegain_skewproxy_252d_base_v108_signal(revenue, closeadj):
    base = _f35_share_gain_proxy(revenue, 21)
    m = _mean(base, 252)
    s = _std(base, 252).replace(0, np.nan)
    result = _mean((base - m) ** 3, 252) / (s ** 3) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativeg_skewproxy_252d_base_v109_signal(revenue, ebitda, closeadj):
    base = _f35_relative_growth_score(revenue, ebitda, 21)
    m = _mean(base, 252)
    s = _std(base, 252).replace(0, np.nan)
    result = _mean((base - m) ** 3, 252) / (s ** 3) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfg_runlen_252d_base_v110_signal(revenue, closeadj):
    base = _f35_self_growth(revenue, 21)
    up = (base > 0).astype(float)
    cnt = up.rolling(252, min_periods=63).sum()
    result = cnt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegain_runlen_252d_base_v111_signal(revenue, closeadj):
    base = _f35_share_gain_proxy(revenue, 21)
    up = (base > 0).astype(float)
    cnt = up.rolling(252, min_periods=63).sum()
    result = cnt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativeg_runlen_252d_base_v112_signal(revenue, ebitda, closeadj):
    base = _f35_relative_growth_score(revenue, ebitda, 21)
    up = (base > 0).astype(float)
    cnt = up.rolling(252, min_periods=63).sum()
    result = cnt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfg_quartdiff_252d_base_v113_signal(revenue, closeadj):
    base = _f35_self_growth(revenue, 21)
    q75 = base.rolling(252, min_periods=63).quantile(0.75)
    q25 = base.rolling(252, min_periods=63).quantile(0.25)
    result = (q75 - q25) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegain_quartdiff_252d_base_v114_signal(revenue, closeadj):
    base = _f35_share_gain_proxy(revenue, 21)
    q75 = base.rolling(252, min_periods=63).quantile(0.75)
    q25 = base.rolling(252, min_periods=63).quantile(0.25)
    result = (q75 - q25) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativeg_quartdiff_252d_base_v115_signal(revenue, ebitda, closeadj):
    base = _f35_relative_growth_score(revenue, ebitda, 21)
    q75 = base.rolling(252, min_periods=63).quantile(0.75)
    q25 = base.rolling(252, min_periods=63).quantile(0.25)
    result = (q75 - q25) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfg_median_252d_base_v116_signal(revenue, closeadj):
    base = _f35_self_growth(revenue, 21)
    med = base.rolling(252, min_periods=63).median()
    result = med * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegain_median_252d_base_v117_signal(revenue, closeadj):
    base = _f35_share_gain_proxy(revenue, 21)
    med = base.rolling(252, min_periods=63).median()
    result = med * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativeg_median_252d_base_v118_signal(revenue, ebitda, closeadj):
    base = _f35_relative_growth_score(revenue, ebitda, 21)
    med = base.rolling(252, min_periods=63).median()
    result = med * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfg_mad_252d_base_v119_signal(revenue, closeadj):
    base = _f35_self_growth(revenue, 21)
    med = base.rolling(252, min_periods=63).median()
    mad = (base - med).abs().rolling(252, min_periods=63).median()
    result = mad * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegain_mad_252d_base_v120_signal(revenue, closeadj):
    base = _f35_share_gain_proxy(revenue, 21)
    med = base.rolling(252, min_periods=63).median()
    mad = (base - med).abs().rolling(252, min_periods=63).median()
    result = mad * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativeg_mad_252d_base_v121_signal(revenue, ebitda, closeadj):
    base = _f35_relative_growth_score(revenue, ebitda, 21)
    med = base.rolling(252, min_periods=63).median()
    mad = (base - med).abs().rolling(252, min_periods=63).median()
    result = mad * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfg_acc_252d_base_v122_signal(revenue, closeadj):
    base = _f35_self_growth(revenue, 63)
    result = (base - base.shift(63)) * closeadj * (1.0 + base.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegain_acc_252d_base_v123_signal(revenue, closeadj):
    base = _f35_share_gain_proxy(revenue, 63)
    result = (base - base.shift(63)) * closeadj * (1.0 + base.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativeg_acc_252d_base_v124_signal(revenue, ebitda, closeadj):
    base = _f35_relative_growth_score(revenue, ebitda, 63)
    result = (base - base.shift(63)) * closeadj * (1.0 + base.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfg_diff_504d_base_v125_signal(revenue, closeadj):
    base = _f35_self_growth(revenue, 63)
    result = (base - base.shift(504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegain_diff_504d_base_v126_signal(revenue, closeadj):
    base = _f35_share_gain_proxy(revenue, 63)
    result = (base - base.shift(504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativeg_diff_504d_base_v127_signal(revenue, ebitda, closeadj):
    base = _f35_relative_growth_score(revenue, ebitda, 63)
    result = (base - base.shift(504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfg_above_median_252d_base_v128_signal(revenue, closeadj):
    base = _f35_self_growth(revenue, 21)
    med = base.rolling(252, min_periods=63).median()
    ind = (base > med).astype(float)
    result = ind.rolling(63, min_periods=20).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegain_above_median_252d_base_v129_signal(revenue, closeadj):
    base = _f35_share_gain_proxy(revenue, 21)
    med = base.rolling(252, min_periods=63).median()
    ind = (base > med).astype(float)
    result = ind.rolling(63, min_periods=20).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfg_lognorm_252d_base_v130_signal(revenue, closeadj):
    base = _f35_self_growth(revenue, 63)
    sg = np.sign(base)
    result = sg * np.log1p(base.abs() * 100.0) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegain_lognorm_252d_base_v131_signal(revenue, closeadj):
    base = _f35_share_gain_proxy(revenue, 63)
    sg = np.sign(base)
    result = sg * np.log1p(base.abs() * 100.0) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativeg_lognorm_252d_base_v132_signal(revenue, ebitda, closeadj):
    base = _f35_relative_growth_score(revenue, ebitda, 63)
    sg = np.sign(base)
    result = sg * np.log1p(base.abs() * 100.0) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfg_xmom_252d_base_v133_signal(revenue, closeadj):
    base = _f35_self_growth(revenue, 63)
    mom = closeadj / closeadj.shift(252).replace(0, np.nan) - 1.0
    result = base * mom * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegain_xmom_252d_base_v134_signal(revenue, closeadj):
    base = _f35_share_gain_proxy(revenue, 63)
    mom = closeadj / closeadj.shift(252).replace(0, np.nan) - 1.0
    result = base * mom * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativeg_xmom_252d_base_v135_signal(revenue, ebitda, closeadj):
    base = _f35_relative_growth_score(revenue, ebitda, 63)
    mom = closeadj / closeadj.shift(252).replace(0, np.nan) - 1.0
    result = base * mom * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfg_rangeprice_252d_base_v136_signal(revenue, closeadj):
    base = _f35_self_growth(revenue, 63)
    rng = closeadj.rolling(252, min_periods=63).max() - closeadj.rolling(252, min_periods=63).min()
    result = base * rng
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegain_rangeprice_252d_base_v137_signal(revenue, closeadj):
    base = _f35_share_gain_proxy(revenue, 63)
    rng = closeadj.rolling(252, min_periods=63).max() - closeadj.rolling(252, min_periods=63).min()
    result = base * rng
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativeg_rangeprice_252d_base_v138_signal(revenue, ebitda, closeadj):
    base = _f35_relative_growth_score(revenue, ebitda, 63)
    rng = closeadj.rolling(252, min_periods=63).max() - closeadj.rolling(252, min_periods=63).min()
    result = base * rng
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfg_xebitda_252d_base_v139_signal(revenue, ebitda, closeadj):
    base = _f35_self_growth(revenue, 63)
    result = base * np.log(ebitda.replace(0, np.nan).abs()) * closeadj * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegain_xebitda_252d_base_v140_signal(revenue, ebitda, closeadj):
    base = _f35_share_gain_proxy(revenue, 63)
    result = base * np.log(ebitda.replace(0, np.nan).abs()) * closeadj * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativeg_xebitda_252d_base_v141_signal(revenue, ebitda, closeadj):
    base = _f35_relative_growth_score(revenue, ebitda, 63)
    result = base * np.log(ebitda.replace(0, np.nan).abs()) * closeadj * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfg_pearson_252d_base_v142_signal(revenue, closeadj):
    base = _f35_self_growth(revenue, 21)
    cor = base.rolling(252, min_periods=63).corr(closeadj.pct_change(21))
    result = cor * closeadj * (1.0 + base.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfg_pearson_504d_base_v143_signal(revenue, closeadj):
    base = _f35_self_growth(revenue, 63)
    cor = base.rolling(504, min_periods=126).corr(closeadj.pct_change(63))
    result = cor * closeadj * (1.0 + base.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegain_xewmmean_252d_base_v144_signal(revenue, closeadj):
    base = _f35_share_gain_proxy(revenue, 63)
    result = base * closeadj.ewm(span=252, min_periods=60).mean() * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativeg_xewmmean_252d_base_v145_signal(revenue, ebitda, closeadj):
    base = _f35_relative_growth_score(revenue, ebitda, 63)
    result = base * closeadj.ewm(span=252, min_periods=60).mean() * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_selfg_velocity_252d_base_v146_signal(revenue, closeadj):
    base = _f35_self_growth(revenue, 63).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegain_velocity_252d_base_v147_signal(revenue, closeadj):
    base = _f35_share_gain_proxy(revenue, 63).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativeg_velocity_252d_base_v148_signal(revenue, ebitda, closeadj):
    base = _f35_relative_growth_score(revenue, ebitda, 63).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_sharegain_xratio_252d_base_v149_signal(revenue, closeadj):
    base = _f35_share_gain_proxy(revenue, 63)
    pr = closeadj.pct_change(63).replace(0, np.nan)
    result = (base / pr) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f35hms_f35_healthcare_market_share_relativeg_xratio_252d_base_v150_signal(revenue, ebitda, closeadj):
    base = _f35_relative_growth_score(revenue, ebitda, 63)
    pr = closeadj.pct_change(63).replace(0, np.nan)
    result = (base / pr) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f35hms_f35_healthcare_market_share_selfg_xmean63_63d_base_v076_signal,
    f35hms_f35_healthcare_market_share_selfg_xmean63_252d_base_v077_signal,
    f35hms_f35_healthcare_market_share_selfg_xmean252_252d_base_v078_signal,
    f35hms_f35_healthcare_market_share_sharegain_xmean63_63d_base_v079_signal,
    f35hms_f35_healthcare_market_share_sharegain_xmean63_252d_base_v080_signal,
    f35hms_f35_healthcare_market_share_sharegain_xmean252_252d_base_v081_signal,
    f35hms_f35_healthcare_market_share_relativeg_xmean63_63d_base_v082_signal,
    f35hms_f35_healthcare_market_share_relativeg_xmean252_252d_base_v083_signal,
    f35hms_f35_healthcare_market_share_selfg_xstd_252d_base_v084_signal,
    f35hms_f35_healthcare_market_share_sharegain_xstd_252d_base_v085_signal,
    f35hms_f35_healthcare_market_share_relativeg_xstd_252d_base_v086_signal,
    f35hms_f35_healthcare_market_share_selfg_xewmstd_252d_base_v087_signal,
    f35hms_f35_healthcare_market_share_sharegain_xewmstd_252d_base_v088_signal,
    f35hms_f35_healthcare_market_share_relativeg_xewmstd_252d_base_v089_signal,
    f35hms_f35_healthcare_market_share_selfg_xzclose_252d_base_v090_signal,
    f35hms_f35_healthcare_market_share_sharegain_xzclose_252d_base_v091_signal,
    f35hms_f35_healthcare_market_share_relativeg_xzclose_252d_base_v092_signal,
    f35hms_f35_healthcare_market_share_selfg_xlog_252d_base_v093_signal,
    f35hms_f35_healthcare_market_share_sharegain_xlog_252d_base_v094_signal,
    f35hms_f35_healthcare_market_share_relativeg_xlog_252d_base_v095_signal,
    f35hms_f35_healthcare_market_share_selfg_plusprice_63d_base_v096_signal,
    f35hms_f35_healthcare_market_share_selfg_minusprice_63d_base_v097_signal,
    f35hms_f35_healthcare_market_share_sharegain_plusprice_63d_base_v098_signal,
    f35hms_f35_healthcare_market_share_sharegain_minusprice_63d_base_v099_signal,
    f35hms_f35_healthcare_market_share_relativeg_plusprice_252d_base_v100_signal,
    f35hms_f35_healthcare_market_share_selfg_corr_252d_base_v101_signal,
    f35hms_f35_healthcare_market_share_sharegain_corr_252d_base_v102_signal,
    f35hms_f35_healthcare_market_share_relativeg_corr_252d_base_v103_signal,
    f35hms_f35_healthcare_market_share_selfg_halflife_252d_base_v104_signal,
    f35hms_f35_healthcare_market_share_sharegain_halflife_252d_base_v105_signal,
    f35hms_f35_healthcare_market_share_relativeg_halflife_252d_base_v106_signal,
    f35hms_f35_healthcare_market_share_selfg_skewproxy_252d_base_v107_signal,
    f35hms_f35_healthcare_market_share_sharegain_skewproxy_252d_base_v108_signal,
    f35hms_f35_healthcare_market_share_relativeg_skewproxy_252d_base_v109_signal,
    f35hms_f35_healthcare_market_share_selfg_runlen_252d_base_v110_signal,
    f35hms_f35_healthcare_market_share_sharegain_runlen_252d_base_v111_signal,
    f35hms_f35_healthcare_market_share_relativeg_runlen_252d_base_v112_signal,
    f35hms_f35_healthcare_market_share_selfg_quartdiff_252d_base_v113_signal,
    f35hms_f35_healthcare_market_share_sharegain_quartdiff_252d_base_v114_signal,
    f35hms_f35_healthcare_market_share_relativeg_quartdiff_252d_base_v115_signal,
    f35hms_f35_healthcare_market_share_selfg_median_252d_base_v116_signal,
    f35hms_f35_healthcare_market_share_sharegain_median_252d_base_v117_signal,
    f35hms_f35_healthcare_market_share_relativeg_median_252d_base_v118_signal,
    f35hms_f35_healthcare_market_share_selfg_mad_252d_base_v119_signal,
    f35hms_f35_healthcare_market_share_sharegain_mad_252d_base_v120_signal,
    f35hms_f35_healthcare_market_share_relativeg_mad_252d_base_v121_signal,
    f35hms_f35_healthcare_market_share_selfg_acc_252d_base_v122_signal,
    f35hms_f35_healthcare_market_share_sharegain_acc_252d_base_v123_signal,
    f35hms_f35_healthcare_market_share_relativeg_acc_252d_base_v124_signal,
    f35hms_f35_healthcare_market_share_selfg_diff_504d_base_v125_signal,
    f35hms_f35_healthcare_market_share_sharegain_diff_504d_base_v126_signal,
    f35hms_f35_healthcare_market_share_relativeg_diff_504d_base_v127_signal,
    f35hms_f35_healthcare_market_share_selfg_above_median_252d_base_v128_signal,
    f35hms_f35_healthcare_market_share_sharegain_above_median_252d_base_v129_signal,
    f35hms_f35_healthcare_market_share_selfg_lognorm_252d_base_v130_signal,
    f35hms_f35_healthcare_market_share_sharegain_lognorm_252d_base_v131_signal,
    f35hms_f35_healthcare_market_share_relativeg_lognorm_252d_base_v132_signal,
    f35hms_f35_healthcare_market_share_selfg_xmom_252d_base_v133_signal,
    f35hms_f35_healthcare_market_share_sharegain_xmom_252d_base_v134_signal,
    f35hms_f35_healthcare_market_share_relativeg_xmom_252d_base_v135_signal,
    f35hms_f35_healthcare_market_share_selfg_rangeprice_252d_base_v136_signal,
    f35hms_f35_healthcare_market_share_sharegain_rangeprice_252d_base_v137_signal,
    f35hms_f35_healthcare_market_share_relativeg_rangeprice_252d_base_v138_signal,
    f35hms_f35_healthcare_market_share_selfg_xebitda_252d_base_v139_signal,
    f35hms_f35_healthcare_market_share_sharegain_xebitda_252d_base_v140_signal,
    f35hms_f35_healthcare_market_share_relativeg_xebitda_252d_base_v141_signal,
    f35hms_f35_healthcare_market_share_selfg_pearson_252d_base_v142_signal,
    f35hms_f35_healthcare_market_share_selfg_pearson_504d_base_v143_signal,
    f35hms_f35_healthcare_market_share_sharegain_xewmmean_252d_base_v144_signal,
    f35hms_f35_healthcare_market_share_relativeg_xewmmean_252d_base_v145_signal,
    f35hms_f35_healthcare_market_share_selfg_velocity_252d_base_v146_signal,
    f35hms_f35_healthcare_market_share_sharegain_velocity_252d_base_v147_signal,
    f35hms_f35_healthcare_market_share_relativeg_velocity_252d_base_v148_signal,
    f35hms_f35_healthcare_market_share_sharegain_xratio_252d_base_v149_signal,
    f35hms_f35_healthcare_market_share_relativeg_xratio_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F35_HEALTHCARE_MARKET_SHARE_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "ebitda": ebitda,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f35_self_growth", "_f35_share_gain_proxy", "_f35_relative_growth_score")
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
    print(f"OK f35_healthcare_market_share_base_076_150_claude: {n_features} features pass")
