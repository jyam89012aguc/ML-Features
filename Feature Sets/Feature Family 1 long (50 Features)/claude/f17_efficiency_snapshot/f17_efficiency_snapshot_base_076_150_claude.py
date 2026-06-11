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


def _diff(s, n):
    return s.diff(periods=n)


# ===== folder domain primitives =====
def _f17_efficiency_ratio(numerator, denominator, w):
    n = _mean(numerator, w)
    d = _mean(denominator, w)
    return n / d.replace(0, np.nan).abs()


def _f17_turnover_rate(flow, stock, w):
    f = _mean(flow, w)
    s = _mean(stock, w)
    return f / s.replace(0, np.nan).abs()


# zscore of 21d ROA over 252d
def f17es_f17_efficiency_snapshot_roaz_252d_base_v076_signal(netinc, assets, marketcap):
    base = _f17_efficiency_ratio(netinc, assets, 21)
    result = _z(base, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of 63d ROA over 504d
def f17es_f17_efficiency_snapshot_roaz_504d_base_v077_signal(netinc, assets, marketcap):
    base = _f17_efficiency_ratio(netinc, assets, 63)
    result = _z(base, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of 21d ROE over 252d
def f17es_f17_efficiency_snapshot_roez_252d_base_v078_signal(netinc, equity, marketcap):
    base = _f17_efficiency_ratio(netinc, equity, 21)
    result = _z(base, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of 21d asset turnover
def f17es_f17_efficiency_snapshot_atz_252d_base_v079_signal(revenue, assets, marketcap):
    base = _f17_turnover_rate(revenue, assets, 21)
    result = _z(base, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of 21d gross margin
def f17es_f17_efficiency_snapshot_gmz_252d_base_v080_signal(gp, revenue, marketcap):
    base = _f17_efficiency_ratio(gp, revenue, 21)
    result = _z(base, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of 21d operating margin
def f17es_f17_efficiency_snapshot_omz_252d_base_v081_signal(opinc, revenue, marketcap):
    base = _f17_efficiency_ratio(opinc, revenue, 21)
    result = _z(base, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of fcf margin 252d
def f17es_f17_efficiency_snapshot_fcfmarginz_252d_base_v082_signal(fcf, revenue, marketcap):
    base = _f17_efficiency_ratio(fcf, revenue, 21)
    result = _z(base, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of CCC 252d
def f17es_f17_efficiency_snapshot_cccz_252d_base_v083_signal(ncfo, netinc, marketcap):
    base = _f17_efficiency_ratio(ncfo, netinc, 21)
    result = _z(base, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# zscore of ROIC 252d
def f17es_f17_efficiency_snapshot_roicz_252d_base_v084_signal(opinc, equity, debt, marketcap):
    cap = equity + debt
    base = _f17_efficiency_ratio(opinc, cap, 21)
    result = _z(base, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of ROA
def f17es_f17_efficiency_snapshot_roastd_252d_base_v085_signal(netinc, assets, marketcap):
    base = _f17_efficiency_ratio(netinc, assets, 21)
    result = _std(base, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of OM
def f17es_f17_efficiency_snapshot_omstd_252d_base_v086_signal(opinc, revenue, marketcap):
    base = _f17_efficiency_ratio(opinc, revenue, 21)
    result = _std(base, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of asset turnover
def f17es_f17_efficiency_snapshot_atstd_252d_base_v087_signal(revenue, assets, marketcap):
    base = _f17_turnover_rate(revenue, assets, 21)
    result = _std(base, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of high-ROA days
def f17es_f17_efficiency_snapshot_highroa_count_252d_base_v088_signal(netinc, assets, marketcap):
    base = _f17_efficiency_ratio(netinc, assets, 21)
    avg = _mean(base, 252)
    flag = (base > avg).astype(float)
    result = flag.rolling(252, min_periods=63).sum() * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of high-OM days
def f17es_f17_efficiency_snapshot_highom_count_252d_base_v089_signal(opinc, revenue, marketcap):
    base = _f17_efficiency_ratio(opinc, revenue, 21)
    avg = _mean(base, 252)
    flag = (base > avg).astype(float)
    result = flag.rolling(252, min_periods=63).sum() * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of low-asset-turnover days
def f17es_f17_efficiency_snapshot_lowat_count_504d_base_v090_signal(revenue, assets, marketcap):
    base = _f17_turnover_rate(revenue, assets, 21)
    avg = _mean(base, 504)
    flag = (base < avg).astype(float)
    result = flag.rolling(504, min_periods=126).sum() * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# ROA - 252d mean (deviation)
def f17es_f17_efficiency_snapshot_roadev_252d_base_v091_signal(netinc, assets, marketcap):
    base = _f17_efficiency_ratio(netinc, assets, 21)
    avg = _mean(base, 252)
    result = (base - avg) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# OM - 252d mean
def f17es_f17_efficiency_snapshot_omdev_252d_base_v092_signal(opinc, revenue, marketcap):
    base = _f17_efficiency_ratio(opinc, revenue, 21)
    avg = _mean(base, 252)
    result = (base - avg) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# Asset turnover - 252d mean
def f17es_f17_efficiency_snapshot_atdev_252d_base_v093_signal(revenue, assets, marketcap):
    base = _f17_turnover_rate(revenue, assets, 21)
    avg = _mean(base, 252)
    result = (base - avg) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# GP margin - 252d mean
def f17es_f17_efficiency_snapshot_gmdev_252d_base_v094_signal(gp, revenue, marketcap):
    base = _f17_efficiency_ratio(gp, revenue, 21)
    avg = _mean(base, 252)
    result = (base - avg) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# ROA relative to 504d hi
def f17es_f17_efficiency_snapshot_roarelhi_504d_base_v095_signal(netinc, assets, marketcap):
    base = _f17_efficiency_ratio(netinc, assets, 63)
    hi = base.rolling(504, min_periods=126).max()
    result = (base / hi.replace(0, np.nan)) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# OM relative to 504d hi
def f17es_f17_efficiency_snapshot_omrelhi_504d_base_v096_signal(opinc, revenue, marketcap):
    base = _f17_efficiency_ratio(opinc, revenue, 63)
    hi = base.rolling(504, min_periods=126).max()
    result = (base / hi.replace(0, np.nan)) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# Asset turnover relative to 504d hi
def f17es_f17_efficiency_snapshot_atrelhi_504d_base_v097_signal(revenue, assets, marketcap):
    base = _f17_turnover_rate(revenue, assets, 63)
    hi = base.rolling(504, min_periods=126).max()
    result = (base / hi.replace(0, np.nan)) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# ROA position in 504d range
def f17es_f17_efficiency_snapshot_roapos_504d_base_v098_signal(netinc, assets, marketcap):
    base = _f17_efficiency_ratio(netinc, assets, 63)
    hi = base.rolling(504, min_periods=126).max()
    lo = base.rolling(504, min_periods=126).min()
    pos = (base - lo) / (hi - lo).replace(0, np.nan)
    result = pos * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# OM position in 504d range
def f17es_f17_efficiency_snapshot_ompos_504d_base_v099_signal(opinc, revenue, marketcap):
    base = _f17_efficiency_ratio(opinc, revenue, 63)
    hi = base.rolling(504, min_periods=126).max()
    lo = base.rolling(504, min_periods=126).min()
    pos = (base - lo) / (hi - lo).replace(0, np.nan)
    result = pos * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# Asset turnover position in 504d range
def f17es_f17_efficiency_snapshot_atpos_504d_base_v100_signal(revenue, assets, marketcap):
    base = _f17_turnover_rate(revenue, assets, 63)
    hi = base.rolling(504, min_periods=126).max()
    lo = base.rolling(504, min_periods=126).min()
    pos = (base - lo) / (hi - lo).replace(0, np.nan)
    result = pos * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# blended profitability efficiency: ROA + ROE + ROIC
def f17es_f17_efficiency_snapshot_blendedeff_252d_base_v101_signal(netinc, assets, equity, opinc, debt, marketcap):
    a = _f17_efficiency_ratio(netinc, assets, 252)
    b = _f17_efficiency_ratio(netinc, equity, 252)
    cap = equity + debt
    c = _f17_efficiency_ratio(opinc, cap, 252)
    result = (a + b + c) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# blended margin: GM + OM + FCF margin
def f17es_f17_efficiency_snapshot_blendedmargin_252d_base_v102_signal(gp, opinc, fcf, revenue, marketcap):
    a = _f17_efficiency_ratio(gp, revenue, 252)
    b = _f17_efficiency_ratio(opinc, revenue, 252)
    c = _f17_efficiency_ratio(fcf, revenue, 252)
    result = (a + b + c) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROA recent vs trend
def f17es_f17_efficiency_snapshot_roa_recent_vs_trend_base_v103_signal(netinc, assets, marketcap):
    a = _f17_efficiency_ratio(netinc, assets, 63)
    b = _f17_efficiency_ratio(netinc, assets, 252)
    result = (a / b.replace(0, np.nan)) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d OM recent vs trend
def f17es_f17_efficiency_snapshot_om_recent_vs_trend_base_v104_signal(opinc, revenue, marketcap):
    a = _f17_efficiency_ratio(opinc, revenue, 63)
    b = _f17_efficiency_ratio(opinc, revenue, 252)
    result = (a / b.replace(0, np.nan)) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset turnover recent vs trend
def f17es_f17_efficiency_snapshot_at_recent_vs_trend_base_v105_signal(revenue, assets, marketcap):
    a = _f17_turnover_rate(revenue, assets, 63)
    b = _f17_turnover_rate(revenue, assets, 252)
    result = (a / b.replace(0, np.nan)) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log ROA
def f17es_f17_efficiency_snapshot_logroa_21d_base_v106_signal(netinc, assets, marketcap):
    base = _f17_efficiency_ratio(netinc, assets, 21)
    result = np.log(base.replace(0, np.nan).abs() + 1.0) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log ROA
def f17es_f17_efficiency_snapshot_logroa_252d_base_v107_signal(netinc, assets, marketcap):
    base = _f17_efficiency_ratio(netinc, assets, 252)
    result = np.log(base.replace(0, np.nan).abs() + 1.0) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log OM
def f17es_f17_efficiency_snapshot_logom_252d_base_v108_signal(opinc, revenue, marketcap):
    base = _f17_efficiency_ratio(opinc, revenue, 252)
    result = np.log(base.replace(0, np.nan).abs() + 1.0) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log asset turnover
def f17es_f17_efficiency_snapshot_logat_252d_base_v109_signal(revenue, assets, marketcap):
    base = _f17_turnover_rate(revenue, assets, 252)
    result = np.log(base.replace(0, np.nan).abs() + 1.0) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROA squared
def f17es_f17_efficiency_snapshot_roasq_252d_base_v110_signal(netinc, assets, marketcap):
    base = _f17_efficiency_ratio(netinc, assets, 252)
    result = base * base.abs() * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d OM squared
def f17es_f17_efficiency_snapshot_omsq_252d_base_v111_signal(opinc, revenue, marketcap):
    base = _f17_efficiency_ratio(opinc, revenue, 252)
    result = base * base.abs() * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROA EMA
def f17es_f17_efficiency_snapshot_roa_ema_21d_base_v112_signal(netinc, assets, marketcap):
    base = _f17_efficiency_ratio(netinc, assets, 21).ewm(span=21, adjust=False).mean()
    result = base * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROA EMA
def f17es_f17_efficiency_snapshot_roa_ema_252d_base_v113_signal(netinc, assets, marketcap):
    base = _f17_efficiency_ratio(netinc, assets, 252).ewm(span=252, adjust=False).mean()
    result = base * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d OM EMA
def f17es_f17_efficiency_snapshot_om_ema_252d_base_v114_signal(opinc, revenue, marketcap):
    base = _f17_efficiency_ratio(opinc, revenue, 252).ewm(span=252, adjust=False).mean()
    result = base * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d AT EMA
def f17es_f17_efficiency_snapshot_at_ema_252d_base_v115_signal(revenue, assets, marketcap):
    base = _f17_turnover_rate(revenue, assets, 252).ewm(span=252, adjust=False).mean()
    result = base * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d (ebitda - capex) / assets - cash productivity
def f17es_f17_efficiency_snapshot_cashprod_21d_base_v116_signal(ebitda, capex, assets, marketcap):
    num = ebitda - capex
    result = _f17_efficiency_ratio(num, assets, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d (ebitda - capex) / assets
def f17es_f17_efficiency_snapshot_cashprod_252d_base_v117_signal(ebitda, capex, assets, marketcap):
    num = ebitda - capex
    result = _f17_efficiency_ratio(num, assets, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d (ncfo - capex) / revenue - core efficiency
def f17es_f17_efficiency_snapshot_coreeff_21d_base_v118_signal(ncfo, capex, revenue, marketcap):
    num = ncfo - capex
    result = _f17_efficiency_ratio(num, revenue, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d (ncfo - capex) / revenue
def f17es_f17_efficiency_snapshot_coreeff_252d_base_v119_signal(ncfo, capex, revenue, marketcap):
    num = ncfo - capex
    result = _f17_efficiency_ratio(num, revenue, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d (ncfo - capex) / assets
def f17es_f17_efficiency_snapshot_coreeff_504d_base_v120_signal(ncfo, capex, assets, marketcap):
    num = ncfo - capex
    result = _f17_efficiency_ratio(num, assets, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d retearn / revenue (retention efficiency)
def f17es_f17_efficiency_snapshot_retentionrev_21d_base_v121_signal(retearn, revenue, marketcap):
    result = _f17_efficiency_ratio(retearn, revenue, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d retearn / revenue
def f17es_f17_efficiency_snapshot_retentionrev_252d_base_v122_signal(retearn, revenue, marketcap):
    result = _f17_efficiency_ratio(retearn, revenue, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d retearn / netinc
def f17es_f17_efficiency_snapshot_retentionni_21d_base_v123_signal(retearn, netinc, marketcap):
    result = _f17_efficiency_ratio(retearn, netinc, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d retearn / netinc
def f17es_f17_efficiency_snapshot_retentionni_252d_base_v124_signal(retearn, netinc, marketcap):
    result = _f17_efficiency_ratio(retearn, netinc, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revenue / wc - working capital turnover
def f17es_f17_efficiency_snapshot_revwc_21d_base_v125_signal(revenue, workingcapital, marketcap):
    result = _f17_turnover_rate(revenue, workingcapital, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue / wc
def f17es_f17_efficiency_snapshot_revwc_252d_base_v126_signal(revenue, workingcapital, marketcap):
    result = _f17_turnover_rate(revenue, workingcapital, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d revenue / wc
def f17es_f17_efficiency_snapshot_revwc_504d_base_v127_signal(revenue, workingcapital, marketcap):
    result = _f17_turnover_rate(revenue, workingcapital, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ebitda / opinc - cash margin uplift
def f17es_f17_efficiency_snapshot_ebitdaopinc_21d_base_v128_signal(ebitda, opinc, marketcap):
    result = _f17_efficiency_ratio(ebitda, opinc, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ebitda / opinc
def f17es_f17_efficiency_snapshot_ebitdaopinc_252d_base_v129_signal(ebitda, opinc, marketcap):
    result = _f17_efficiency_ratio(ebitda, opinc, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ncfo / fcf - operating to free conversion
def f17es_f17_efficiency_snapshot_ncfofcf_21d_base_v130_signal(ncfo, fcf, marketcap):
    result = _f17_efficiency_ratio(ncfo, fcf, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo / fcf
def f17es_f17_efficiency_snapshot_ncfofcf_252d_base_v131_signal(ncfo, fcf, marketcap):
    result = _f17_efficiency_ratio(ncfo, fcf, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capex / ncfo - reinvestment ratio
def f17es_f17_efficiency_snapshot_capncfo_21d_base_v132_signal(capex, ncfo, marketcap):
    result = _f17_efficiency_ratio(capex, ncfo, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex / ncfo
def f17es_f17_efficiency_snapshot_capncfo_252d_base_v133_signal(capex, ncfo, marketcap):
    result = _f17_efficiency_ratio(capex, ncfo, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex / ncfo
def f17es_f17_efficiency_snapshot_capncfo_504d_base_v134_signal(capex, ncfo, marketcap):
    result = _f17_efficiency_ratio(capex, ncfo, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gp / equity (gross-equity efficiency)
def f17es_f17_efficiency_snapshot_gpequity_21d_base_v135_signal(gp, equity, marketcap):
    result = _f17_efficiency_ratio(gp, equity, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gp / equity
def f17es_f17_efficiency_snapshot_gpequity_252d_base_v136_signal(gp, equity, marketcap):
    result = _f17_efficiency_ratio(gp, equity, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d gp / equity
def f17es_f17_efficiency_snapshot_gpequity_504d_base_v137_signal(gp, equity, marketcap):
    result = _f17_efficiency_ratio(gp, equity, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d opinc / assets (operating ROA)
def f17es_f17_efficiency_snapshot_opincassets_252d_base_v138_signal(opinc, assets, marketcap):
    result = _f17_efficiency_ratio(opinc, assets, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d opinc / assets
def f17es_f17_efficiency_snapshot_opincassets_504d_base_v139_signal(opinc, assets, marketcap):
    result = _f17_efficiency_ratio(opinc, assets, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d opinc / equity
def f17es_f17_efficiency_snapshot_opincequity_252d_base_v140_signal(opinc, equity, marketcap):
    result = _f17_efficiency_ratio(opinc, equity, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ebitda / equity
def f17es_f17_efficiency_snapshot_ebitdaequity_504d_base_v141_signal(ebitda, equity, marketcap):
    result = _f17_efficiency_ratio(ebitda, equity, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue / liabilities (sales per liability)
def f17es_f17_efficiency_snapshot_revliab_252d_base_v142_signal(revenue, liabilities, marketcap):
    result = _f17_turnover_rate(revenue, liabilities, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ebitda / liabilities
def f17es_f17_efficiency_snapshot_ebitdaliab_252d_base_v143_signal(ebitda, liabilities, marketcap):
    result = _f17_efficiency_ratio(ebitda, liabilities, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo / liabilities
def f17es_f17_efficiency_snapshot_ncfoliab_252d_base_v144_signal(ncfo, liabilities, marketcap):
    result = _f17_efficiency_ratio(ncfo, liabilities, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex / wc - investment vs operating capital
def f17es_f17_efficiency_snapshot_capwc_252d_base_v145_signal(capex, workingcapital, marketcap):
    result = _f17_efficiency_ratio(capex, workingcapital, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite efficiency: GM * AT (DuPont-like)
def f17es_f17_efficiency_snapshot_dupont_252d_base_v146_signal(gp, revenue, assets, marketcap):
    gm = _f17_efficiency_ratio(gp, revenue, 252)
    at = _f17_turnover_rate(revenue, assets, 252)
    result = (gm * at) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite efficiency: OM * AT
def f17es_f17_efficiency_snapshot_dupontom_252d_base_v147_signal(opinc, revenue, assets, marketcap):
    om = _f17_efficiency_ratio(opinc, revenue, 252)
    at = _f17_turnover_rate(revenue, assets, 252)
    result = (om * at) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d full DuPont: NM * AT * EM (margin * turnover * leverage)
def f17es_f17_efficiency_snapshot_fulldupont_252d_base_v148_signal(netinc, revenue, assets, equity, marketcap):
    nm = _f17_efficiency_ratio(netinc, revenue, 252)
    at = _f17_turnover_rate(revenue, assets, 252)
    em = _f17_efficiency_ratio(assets, equity, 252)
    result = (nm * at * em) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d effciency (ROA / capex/assets) - efficiency of investment
def f17es_f17_efficiency_snapshot_invest_eff_252d_base_v149_signal(netinc, capex, assets, marketcap):
    roa = _f17_efficiency_ratio(netinc, assets, 252)
    ci = _f17_efficiency_ratio(capex, assets, 252)
    result = (roa / ci.replace(0, np.nan)) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d (ROA - capex/assets) - net surplus efficiency
def f17es_f17_efficiency_snapshot_net_surplus_252d_base_v150_signal(netinc, capex, assets, marketcap):
    roa = _f17_efficiency_ratio(netinc, assets, 252)
    ci = _f17_efficiency_ratio(capex, assets, 252)
    result = (roa - ci) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f17es_f17_efficiency_snapshot_roaz_252d_base_v076_signal,
    f17es_f17_efficiency_snapshot_roaz_504d_base_v077_signal,
    f17es_f17_efficiency_snapshot_roez_252d_base_v078_signal,
    f17es_f17_efficiency_snapshot_atz_252d_base_v079_signal,
    f17es_f17_efficiency_snapshot_gmz_252d_base_v080_signal,
    f17es_f17_efficiency_snapshot_omz_252d_base_v081_signal,
    f17es_f17_efficiency_snapshot_fcfmarginz_252d_base_v082_signal,
    f17es_f17_efficiency_snapshot_cccz_252d_base_v083_signal,
    f17es_f17_efficiency_snapshot_roicz_252d_base_v084_signal,
    f17es_f17_efficiency_snapshot_roastd_252d_base_v085_signal,
    f17es_f17_efficiency_snapshot_omstd_252d_base_v086_signal,
    f17es_f17_efficiency_snapshot_atstd_252d_base_v087_signal,
    f17es_f17_efficiency_snapshot_highroa_count_252d_base_v088_signal,
    f17es_f17_efficiency_snapshot_highom_count_252d_base_v089_signal,
    f17es_f17_efficiency_snapshot_lowat_count_504d_base_v090_signal,
    f17es_f17_efficiency_snapshot_roadev_252d_base_v091_signal,
    f17es_f17_efficiency_snapshot_omdev_252d_base_v092_signal,
    f17es_f17_efficiency_snapshot_atdev_252d_base_v093_signal,
    f17es_f17_efficiency_snapshot_gmdev_252d_base_v094_signal,
    f17es_f17_efficiency_snapshot_roarelhi_504d_base_v095_signal,
    f17es_f17_efficiency_snapshot_omrelhi_504d_base_v096_signal,
    f17es_f17_efficiency_snapshot_atrelhi_504d_base_v097_signal,
    f17es_f17_efficiency_snapshot_roapos_504d_base_v098_signal,
    f17es_f17_efficiency_snapshot_ompos_504d_base_v099_signal,
    f17es_f17_efficiency_snapshot_atpos_504d_base_v100_signal,
    f17es_f17_efficiency_snapshot_blendedeff_252d_base_v101_signal,
    f17es_f17_efficiency_snapshot_blendedmargin_252d_base_v102_signal,
    f17es_f17_efficiency_snapshot_roa_recent_vs_trend_base_v103_signal,
    f17es_f17_efficiency_snapshot_om_recent_vs_trend_base_v104_signal,
    f17es_f17_efficiency_snapshot_at_recent_vs_trend_base_v105_signal,
    f17es_f17_efficiency_snapshot_logroa_21d_base_v106_signal,
    f17es_f17_efficiency_snapshot_logroa_252d_base_v107_signal,
    f17es_f17_efficiency_snapshot_logom_252d_base_v108_signal,
    f17es_f17_efficiency_snapshot_logat_252d_base_v109_signal,
    f17es_f17_efficiency_snapshot_roasq_252d_base_v110_signal,
    f17es_f17_efficiency_snapshot_omsq_252d_base_v111_signal,
    f17es_f17_efficiency_snapshot_roa_ema_21d_base_v112_signal,
    f17es_f17_efficiency_snapshot_roa_ema_252d_base_v113_signal,
    f17es_f17_efficiency_snapshot_om_ema_252d_base_v114_signal,
    f17es_f17_efficiency_snapshot_at_ema_252d_base_v115_signal,
    f17es_f17_efficiency_snapshot_cashprod_21d_base_v116_signal,
    f17es_f17_efficiency_snapshot_cashprod_252d_base_v117_signal,
    f17es_f17_efficiency_snapshot_coreeff_21d_base_v118_signal,
    f17es_f17_efficiency_snapshot_coreeff_252d_base_v119_signal,
    f17es_f17_efficiency_snapshot_coreeff_504d_base_v120_signal,
    f17es_f17_efficiency_snapshot_retentionrev_21d_base_v121_signal,
    f17es_f17_efficiency_snapshot_retentionrev_252d_base_v122_signal,
    f17es_f17_efficiency_snapshot_retentionni_21d_base_v123_signal,
    f17es_f17_efficiency_snapshot_retentionni_252d_base_v124_signal,
    f17es_f17_efficiency_snapshot_revwc_21d_base_v125_signal,
    f17es_f17_efficiency_snapshot_revwc_252d_base_v126_signal,
    f17es_f17_efficiency_snapshot_revwc_504d_base_v127_signal,
    f17es_f17_efficiency_snapshot_ebitdaopinc_21d_base_v128_signal,
    f17es_f17_efficiency_snapshot_ebitdaopinc_252d_base_v129_signal,
    f17es_f17_efficiency_snapshot_ncfofcf_21d_base_v130_signal,
    f17es_f17_efficiency_snapshot_ncfofcf_252d_base_v131_signal,
    f17es_f17_efficiency_snapshot_capncfo_21d_base_v132_signal,
    f17es_f17_efficiency_snapshot_capncfo_252d_base_v133_signal,
    f17es_f17_efficiency_snapshot_capncfo_504d_base_v134_signal,
    f17es_f17_efficiency_snapshot_gpequity_21d_base_v135_signal,
    f17es_f17_efficiency_snapshot_gpequity_252d_base_v136_signal,
    f17es_f17_efficiency_snapshot_gpequity_504d_base_v137_signal,
    f17es_f17_efficiency_snapshot_opincassets_252d_base_v138_signal,
    f17es_f17_efficiency_snapshot_opincassets_504d_base_v139_signal,
    f17es_f17_efficiency_snapshot_opincequity_252d_base_v140_signal,
    f17es_f17_efficiency_snapshot_ebitdaequity_504d_base_v141_signal,
    f17es_f17_efficiency_snapshot_revliab_252d_base_v142_signal,
    f17es_f17_efficiency_snapshot_ebitdaliab_252d_base_v143_signal,
    f17es_f17_efficiency_snapshot_ncfoliab_252d_base_v144_signal,
    f17es_f17_efficiency_snapshot_capwc_252d_base_v145_signal,
    f17es_f17_efficiency_snapshot_dupont_252d_base_v146_signal,
    f17es_f17_efficiency_snapshot_dupontom_252d_base_v147_signal,
    f17es_f17_efficiency_snapshot_fulldupont_252d_base_v148_signal,
    f17es_f17_efficiency_snapshot_invest_eff_252d_base_v149_signal,
    f17es_f17_efficiency_snapshot_net_surplus_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F17_EFFICIENCY_SNAPSHOT_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    netinc = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="netinc")
    fcf = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcf")
    ncfo = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ncfo")
    equity = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.004, n))), name="equity")
    debt = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.005, n))), name="debt")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.003, n))), name="assets")
    ebitda = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.006, n))), name="ebitda")
    capex = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="capex")
    eps = pd.Series(1.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="eps")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.002, n))), name="sharesbas")
    opinc = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.007, n))), name="opinc")
    gp = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="gp")
    workingcapital = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.006, n))), name="workingcapital")
    currentratio = pd.Series(1.8 * np.exp(np.cumsum(np.random.normal(0.0, 0.003, n))), name="currentratio")
    intexp = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0001, 0.004, n))), name="intexp")
    liabilities = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.004, n))), name="liabilities")
    retearn = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="retearn")
    marketcap = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0005, 0.015, n))), name="marketcap")
    ev = marketcap + debt - 0.3 * marketcap
    ev = pd.Series(ev.values, name="ev")
    evebit = ev / opinc.replace(0, np.nan)
    evebit = pd.Series(evebit.values, name="evebit")
    evebitda = ev / ebitda.replace(0, np.nan)
    evebitda = pd.Series(evebitda.values, name="evebitda")
    pe = marketcap / netinc.replace(0, np.nan)
    pe = pd.Series(pe.values, name="pe")
    pb = marketcap / equity.replace(0, np.nan)
    pb = pd.Series(pb.values, name="pb")
    ps = marketcap / revenue.replace(0, np.nan)
    ps = pd.Series(ps.values, name="ps")
    cols = {"closeadj": closeadj, "revenue": revenue, "netinc": netinc, "fcf": fcf, "ncfo": ncfo,
            "equity": equity, "debt": debt, "assets": assets, "ebitda": ebitda, "capex": capex,
            "eps": eps, "sharesbas": sharesbas, "opinc": opinc, "gp": gp, "workingcapital": workingcapital,
            "currentratio": currentratio, "intexp": intexp, "liabilities": liabilities, "retearn": retearn,
            "marketcap": marketcap, "ev": ev, "evebit": evebit, "evebitda": evebitda,
            "pe": pe, "pb": pb, "ps": ps}
    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f17_efficiency", "_f17_turnover")
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
        if y1.iloc[504:].isna().mean() < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f17_efficiency_snapshot_base_076_150_claude: {n_features} features pass")
