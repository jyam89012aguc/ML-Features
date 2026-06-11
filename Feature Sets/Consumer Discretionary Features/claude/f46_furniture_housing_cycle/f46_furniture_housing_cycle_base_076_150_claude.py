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
def _f46_revenue_housing_proxy(revenue, w):
    long_mean = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    return (revenue - long_mean) / long_mean.replace(0, np.nan).abs()


def _f46_demand_seasonality(revenue, w):
    sd = revenue.rolling(w, min_periods=max(1, w // 2)).std()
    mn = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    return sd / mn.replace(0, np.nan).abs()


def _f46_housing_signal(revenue, ebitda, w):
    long_mean_r = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    rev_proxy = (revenue - long_mean_r) / long_mean_r.replace(0, np.nan).abs()
    long_mean_e = ebitda.rolling(w, min_periods=max(1, w // 2)).mean()
    eb_proxy = (ebitda - long_mean_e) / long_mean_e.replace(0, np.nan).abs()
    return rev_proxy + eb_proxy


# v076: housing signal 126d × ebitda/revenue
def f46fhc_f46_furniture_housing_cycle_hsxebmar_126d_base_v076_signal(revenue, ebitda, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 126)
    margin = ebitda / revenue.replace(0, np.nan)
    result = base * margin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v077: housing signal 252d × ebitda/revenue
def f46fhc_f46_furniture_housing_cycle_hsxebmar_252d_base_v077_signal(revenue, ebitda, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 252)
    margin = ebitda / revenue.replace(0, np.nan)
    result = base * margin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v078: housing signal 504d × ebitda/revenue
def f46fhc_f46_furniture_housing_cycle_hsxebmar_504d_base_v078_signal(revenue, ebitda, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 504)
    margin = ebitda / revenue.replace(0, np.nan)
    result = base * margin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v079: revenue proxy 63d × log capex
def f46fhc_f46_furniture_housing_cycle_revproxylogcapex_63d_base_v079_signal(revenue, capex, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 63)
    result = base * np.log(capex.abs().replace(0, np.nan)) * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# v080: revenue proxy 252d × log capex
def f46fhc_f46_furniture_housing_cycle_revproxylogcapex_252d_base_v080_signal(revenue, capex, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 252)
    result = base * np.log(capex.abs().replace(0, np.nan)) * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# v081: seasonality 63d × log capex
def f46fhc_f46_furniture_housing_cycle_seasxlogcapex_63d_base_v081_signal(revenue, capex, closeadj):
    base = _f46_demand_seasonality(revenue, 63)
    result = base * np.log(capex.abs().replace(0, np.nan)) * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# v082: seasonality 252d × log capex
def f46fhc_f46_furniture_housing_cycle_seasxlogcapex_252d_base_v082_signal(revenue, capex, closeadj):
    base = _f46_demand_seasonality(revenue, 252)
    result = base * np.log(capex.abs().replace(0, np.nan)) * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# v083: housing signal 63d × log capex
def f46fhc_f46_furniture_housing_cycle_hsxlogcapex_63d_base_v083_signal(revenue, ebitda, capex, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 63)
    result = base * np.log(capex.abs().replace(0, np.nan)) * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# v084: housing signal 252d × log capex
def f46fhc_f46_furniture_housing_cycle_hsxlogcapex_252d_base_v084_signal(revenue, ebitda, capex, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 252)
    result = base * np.log(capex.abs().replace(0, np.nan)) * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# v085: revenue proxy 63d × capex/revenue ratio
def f46fhc_f46_furniture_housing_cycle_revproxyxcaprev_63d_base_v085_signal(revenue, capex, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 63)
    capint = capex / revenue.replace(0, np.nan)
    result = base * capint * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v086: revenue proxy 252d × capex/revenue ratio
def f46fhc_f46_furniture_housing_cycle_revproxyxcaprev_252d_base_v086_signal(revenue, capex, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 252)
    capint = capex / revenue.replace(0, np.nan)
    result = base * capint * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v087: housing signal 63d × capex/revenue ratio
def f46fhc_f46_furniture_housing_cycle_hsxcaprev_63d_base_v087_signal(revenue, ebitda, capex, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 63)
    capint = capex / revenue.replace(0, np.nan)
    result = base * capint * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v088: housing signal 252d × capex/revenue ratio
def f46fhc_f46_furniture_housing_cycle_hsxcaprev_252d_base_v088_signal(revenue, ebitda, capex, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 252)
    capint = capex / revenue.replace(0, np.nan)
    result = base * capint * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v089: revenue proxy 63d ema (~)
def f46fhc_f46_furniture_housing_cycle_revproxyema_63d_base_v089_signal(revenue, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 63)
    ema = base.ewm(span=63, min_periods=10).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v090: revenue proxy 252d ema
def f46fhc_f46_furniture_housing_cycle_revproxyema_252d_base_v090_signal(revenue, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 252)
    ema = base.ewm(span=63, min_periods=10).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v091: housing signal 63d ema
def f46fhc_f46_furniture_housing_cycle_hsignalema_63d_base_v091_signal(revenue, ebitda, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 63)
    ema = base.ewm(span=63, min_periods=10).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v092: housing signal 252d ema
def f46fhc_f46_furniture_housing_cycle_hsignalema_252d_base_v092_signal(revenue, ebitda, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 252)
    ema = base.ewm(span=63, min_periods=10).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v093: revenue proxy 63d × sign closeadj change × closeadj
def f46fhc_f46_furniture_housing_cycle_revproxyxret_63d_base_v093_signal(revenue, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 63)
    ret = closeadj.pct_change(21)
    result = base * ret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v094: revenue proxy 252d × ret 63d × closeadj
def f46fhc_f46_furniture_housing_cycle_revproxyxret_252d_base_v094_signal(revenue, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 252)
    ret = closeadj.pct_change(63)
    result = base * ret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v095: housing signal 63d × ret × closeadj
def f46fhc_f46_furniture_housing_cycle_hsxret_63d_base_v095_signal(revenue, ebitda, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 63)
    ret = closeadj.pct_change(21)
    result = base * ret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v096: housing signal 252d × ret 63d × closeadj
def f46fhc_f46_furniture_housing_cycle_hsxret_252d_base_v096_signal(revenue, ebitda, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 252)
    ret = closeadj.pct_change(63)
    result = base * ret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v097: housing signal 504d × ret 126d × closeadj
def f46fhc_f46_furniture_housing_cycle_hsxret_504d_base_v097_signal(revenue, ebitda, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 504)
    ret = closeadj.pct_change(126)
    result = base * ret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v098: revenue proxy 63d × closeadj std
def f46fhc_f46_furniture_housing_cycle_revproxyxvol_63d_base_v098_signal(revenue, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 63)
    vol = closeadj.pct_change().rolling(63, min_periods=10).std()
    result = base * vol * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v099: revenue proxy 252d × closeadj std
def f46fhc_f46_furniture_housing_cycle_revproxyxvol_252d_base_v099_signal(revenue, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 252)
    vol = closeadj.pct_change().rolling(63, min_periods=10).std()
    result = base * vol * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v100: housing signal 63d × closeadj std
def f46fhc_f46_furniture_housing_cycle_hsxvol_63d_base_v100_signal(revenue, ebitda, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 63)
    vol = closeadj.pct_change().rolling(63, min_periods=10).std()
    result = base * vol * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v101: housing signal 252d × closeadj std
def f46fhc_f46_furniture_housing_cycle_hsxvol_252d_base_v101_signal(revenue, ebitda, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 252)
    vol = closeadj.pct_change().rolling(63, min_periods=10).std()
    result = base * vol * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v102: revenue proxy 63d - revenue proxy 252d
def f46fhc_f46_furniture_housing_cycle_revproxydiff_63_252_base_v102_signal(revenue, closeadj):
    short = _f46_revenue_housing_proxy(revenue, 63)
    long = _f46_revenue_housing_proxy(revenue, 252)
    result = (short - long) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v103: revenue proxy 21d - revenue proxy 126d
def f46fhc_f46_furniture_housing_cycle_revproxydiff_21_126_base_v103_signal(revenue, closeadj):
    short = _f46_revenue_housing_proxy(revenue, 21)
    long = _f46_revenue_housing_proxy(revenue, 126)
    result = (short - long) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v104: housing signal 63d - housing signal 252d
def f46fhc_f46_furniture_housing_cycle_hsdiff_63_252_base_v104_signal(revenue, ebitda, closeadj):
    short = _f46_housing_signal(revenue, ebitda, 63)
    long = _f46_housing_signal(revenue, ebitda, 252)
    result = (short - long) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v105: housing signal 21d - housing signal 126d
def f46fhc_f46_furniture_housing_cycle_hsdiff_21_126_base_v105_signal(revenue, ebitda, closeadj):
    short = _f46_housing_signal(revenue, ebitda, 21)
    long = _f46_housing_signal(revenue, ebitda, 126)
    result = (short - long) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v106: revenue proxy 63d quantile rank rolling
def f46fhc_f46_furniture_housing_cycle_revproxyqrank_63d_base_v106_signal(revenue, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 63)
    rank = base.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v107: revenue proxy 252d quantile rank rolling
def f46fhc_f46_furniture_housing_cycle_revproxyqrank_252d_base_v107_signal(revenue, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 252)
    rank = base.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v108: housing signal 63d quantile rank rolling
def f46fhc_f46_furniture_housing_cycle_hsqrank_63d_base_v108_signal(revenue, ebitda, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 63)
    rank = base.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v109: housing signal 252d quantile rank rolling
def f46fhc_f46_furniture_housing_cycle_hsqrank_252d_base_v109_signal(revenue, ebitda, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 252)
    rank = base.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v110: seasonality 63d quantile rank
def f46fhc_f46_furniture_housing_cycle_seasqrank_63d_base_v110_signal(revenue, closeadj):
    base = _f46_demand_seasonality(revenue, 63)
    rank = base.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v111: seasonality 252d quantile rank
def f46fhc_f46_furniture_housing_cycle_seasqrank_252d_base_v111_signal(revenue, closeadj):
    base = _f46_demand_seasonality(revenue, 252)
    rank = base.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v112: revenue proxy 63d × capex std
def f46fhc_f46_furniture_housing_cycle_revproxyxcapexstd_63d_base_v112_signal(revenue, capex, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 63)
    cstd = _std(capex, 63) / _mean(capex, 252).replace(0, np.nan)
    result = base * cstd * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v113: revenue proxy 252d × capex std
def f46fhc_f46_furniture_housing_cycle_revproxyxcapexstd_252d_base_v113_signal(revenue, capex, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 252)
    cstd = _std(capex, 252) / _mean(capex, 252).replace(0, np.nan)
    result = base * cstd * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v114: housing signal 63d × capex std
def f46fhc_f46_furniture_housing_cycle_hsxcapexstd_63d_base_v114_signal(revenue, ebitda, capex, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 63)
    cstd = _std(capex, 63) / _mean(capex, 252).replace(0, np.nan)
    result = base * cstd * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v115: housing signal 252d × capex std
def f46fhc_f46_furniture_housing_cycle_hsxcapexstd_252d_base_v115_signal(revenue, ebitda, capex, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 252)
    cstd = _std(capex, 252) / _mean(capex, 252).replace(0, np.nan)
    result = base * cstd * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v116: rev proxy * seasonality EMA × closeadj 63d
def f46fhc_f46_furniture_housing_cycle_revxseasema_63d_base_v116_signal(revenue, closeadj):
    rp = _f46_revenue_housing_proxy(revenue, 63)
    seas = _f46_demand_seasonality(revenue, 63)
    ema = (rp * seas).ewm(span=63, min_periods=10).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v117: rev proxy * seasonality EMA × closeadj 252d
def f46fhc_f46_furniture_housing_cycle_revxseasema_252d_base_v117_signal(revenue, closeadj):
    rp = _f46_revenue_housing_proxy(revenue, 252)
    seas = _f46_demand_seasonality(revenue, 252)
    ema = (rp * seas).ewm(span=126, min_periods=20).mean()
    result = ema * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v118: housing signal 63d × ebitda magnitude × closeadj
def f46fhc_f46_furniture_housing_cycle_hsxebmag_63d_base_v118_signal(revenue, ebitda, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 63)
    mag = ebitda / _mean(ebitda, 252).replace(0, np.nan)
    result = base * mag * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v119: housing signal 252d × ebitda magnitude × closeadj
def f46fhc_f46_furniture_housing_cycle_hsxebmag_252d_base_v119_signal(revenue, ebitda, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 252)
    mag = ebitda / _mean(ebitda, 252).replace(0, np.nan)
    result = base * mag * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v120: revenue proxy 63d × ebitda magnitude × closeadj
def f46fhc_f46_furniture_housing_cycle_revproxyxebmag_63d_base_v120_signal(revenue, ebitda, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 63)
    mag = ebitda / _mean(ebitda, 252).replace(0, np.nan)
    result = base * mag * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v121: revenue proxy 252d × ebitda magnitude × closeadj
def f46fhc_f46_furniture_housing_cycle_revproxyxebmag_252d_base_v121_signal(revenue, ebitda, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 252)
    mag = ebitda / _mean(ebitda, 252).replace(0, np.nan)
    result = base * mag * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v122: 63d revenue proxy * seasonality squared
def f46fhc_f46_furniture_housing_cycle_revxseas2_63d_base_v122_signal(revenue, closeadj):
    rp = _f46_revenue_housing_proxy(revenue, 63)
    seas = _f46_demand_seasonality(revenue, 63)
    result = rp * seas * seas * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v123: 252d revenue proxy * seasonality squared
def f46fhc_f46_furniture_housing_cycle_revxseas2_252d_base_v123_signal(revenue, closeadj):
    rp = _f46_revenue_housing_proxy(revenue, 252)
    seas = _f46_demand_seasonality(revenue, 252)
    result = rp * seas * seas * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v124: housing signal 63d squared × closeadj sign
def f46fhc_f46_furniture_housing_cycle_hsignal2_63d_base_v124_signal(revenue, ebitda, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 63)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v125: housing signal 252d squared × closeadj
def f46fhc_f46_furniture_housing_cycle_hsignal2_252d_base_v125_signal(revenue, ebitda, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 252)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v126: revenue proxy 63d squared × closeadj
def f46fhc_f46_furniture_housing_cycle_revproxy2_63d_base_v126_signal(revenue, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 63)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v127: revenue proxy 252d squared × closeadj
def f46fhc_f46_furniture_housing_cycle_revproxy2_252d_base_v127_signal(revenue, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 252)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v128: 5d revenue proxy z-score × closeadj
def f46fhc_f46_furniture_housing_cycle_revproxyz_5d_base_v128_signal(revenue, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 21)
    result = _z(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v129: 10d revenue proxy z-score × closeadj
def f46fhc_f46_furniture_housing_cycle_revproxyz_10d_base_v129_signal(revenue, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 21)
    result = _z(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v130: 21d revenue proxy z-score × closeadj
def f46fhc_f46_furniture_housing_cycle_revproxyz_21d_base_v130_signal(revenue, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v131: 42d revenue proxy z-score × closeadj
def f46fhc_f46_furniture_housing_cycle_revproxyz_42d_base_v131_signal(revenue, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 42)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v132: 189d revenue proxy z-score × closeadj
def f46fhc_f46_furniture_housing_cycle_revproxyz_189d_base_v132_signal(revenue, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 189)
    result = _z(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v133: 378d revenue proxy z-score × closeadj
def f46fhc_f46_furniture_housing_cycle_revproxyz_378d_base_v133_signal(revenue, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 378)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v134: 21d housing signal z × closeadj
def f46fhc_f46_furniture_housing_cycle_hsignalz_21d_base_v134_signal(revenue, ebitda, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v135: 42d housing signal z × closeadj
def f46fhc_f46_furniture_housing_cycle_hsignalz_42d_base_v135_signal(revenue, ebitda, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 42)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v136: 189d housing signal z × closeadj
def f46fhc_f46_furniture_housing_cycle_hsignalz_189d_base_v136_signal(revenue, ebitda, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 189)
    result = _z(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v137: 378d housing signal z × closeadj
def f46fhc_f46_furniture_housing_cycle_hsignalz_378d_base_v137_signal(revenue, ebitda, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 378)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v138: 21d seasonality z × closeadj
def f46fhc_f46_furniture_housing_cycle_seasz_21d_base_v138_signal(revenue, closeadj):
    base = _f46_demand_seasonality(revenue, 21)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v139: 63d seasonality z × closeadj
def f46fhc_f46_furniture_housing_cycle_seasz_63d_base_v139_signal(revenue, closeadj):
    base = _f46_demand_seasonality(revenue, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v140: 252d seasonality z × closeadj
def f46fhc_f46_furniture_housing_cycle_seasz_252d_base_v140_signal(revenue, closeadj):
    base = _f46_demand_seasonality(revenue, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v141: 504d seasonality z × closeadj
def f46fhc_f46_furniture_housing_cycle_seasz_504d_base_v141_signal(revenue, closeadj):
    base = _f46_demand_seasonality(revenue, 504)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v142: rev proxy 63d * housing signal 63d × closeadj
def f46fhc_f46_furniture_housing_cycle_rpxhs_63d_base_v142_signal(revenue, ebitda, closeadj):
    rp = _f46_revenue_housing_proxy(revenue, 63)
    hs = _f46_housing_signal(revenue, ebitda, 63)
    result = rp * hs * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v143: rev proxy 252d * housing signal 252d × closeadj
def f46fhc_f46_furniture_housing_cycle_rpxhs_252d_base_v143_signal(revenue, ebitda, closeadj):
    rp = _f46_revenue_housing_proxy(revenue, 252)
    hs = _f46_housing_signal(revenue, ebitda, 252)
    result = rp * hs * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v144: rev proxy 504d * housing signal 504d × closeadj
def f46fhc_f46_furniture_housing_cycle_rpxhs_504d_base_v144_signal(revenue, ebitda, closeadj):
    rp = _f46_revenue_housing_proxy(revenue, 504)
    hs = _f46_housing_signal(revenue, ebitda, 504)
    result = rp * hs * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v145: seas 63d * housing signal 63d × closeadj
def f46fhc_f46_furniture_housing_cycle_seasxhs_63d_base_v145_signal(revenue, ebitda, closeadj):
    seas = _f46_demand_seasonality(revenue, 63)
    hs = _f46_housing_signal(revenue, ebitda, 63)
    result = seas * hs * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v146: seas 252d * housing signal 252d × closeadj
def f46fhc_f46_furniture_housing_cycle_seasxhs_252d_base_v146_signal(revenue, ebitda, closeadj):
    seas = _f46_demand_seasonality(revenue, 252)
    hs = _f46_housing_signal(revenue, ebitda, 252)
    result = seas * hs * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v147: seas 504d * housing signal 504d × closeadj
def f46fhc_f46_furniture_housing_cycle_seasxhs_504d_base_v147_signal(revenue, ebitda, closeadj):
    seas = _f46_demand_seasonality(revenue, 504)
    hs = _f46_housing_signal(revenue, ebitda, 504)
    result = seas * hs * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v148: revenue proxy 63d × abs change closeadj 21d
def f46fhc_f46_furniture_housing_cycle_revxabsret_63d_base_v148_signal(revenue, closeadj):
    base = _f46_revenue_housing_proxy(revenue, 63)
    aret = closeadj.pct_change(21).abs()
    result = base * aret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v149: housing signal 252d × abs change closeadj 63d
def f46fhc_f46_furniture_housing_cycle_hsxabsret_252d_base_v149_signal(revenue, ebitda, closeadj):
    base = _f46_housing_signal(revenue, ebitda, 252)
    aret = closeadj.pct_change(63).abs()
    result = base * aret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v150: seasonality 252d × abs change closeadj 21d × closeadj
def f46fhc_f46_furniture_housing_cycle_seasxabsret_252d_base_v150_signal(revenue, closeadj):
    base = _f46_demand_seasonality(revenue, 252)
    aret = closeadj.pct_change(21).abs()
    result = base * aret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f46fhc_f46_furniture_housing_cycle_hsxebmar_126d_base_v076_signal,
    f46fhc_f46_furniture_housing_cycle_hsxebmar_252d_base_v077_signal,
    f46fhc_f46_furniture_housing_cycle_hsxebmar_504d_base_v078_signal,
    f46fhc_f46_furniture_housing_cycle_revproxylogcapex_63d_base_v079_signal,
    f46fhc_f46_furniture_housing_cycle_revproxylogcapex_252d_base_v080_signal,
    f46fhc_f46_furniture_housing_cycle_seasxlogcapex_63d_base_v081_signal,
    f46fhc_f46_furniture_housing_cycle_seasxlogcapex_252d_base_v082_signal,
    f46fhc_f46_furniture_housing_cycle_hsxlogcapex_63d_base_v083_signal,
    f46fhc_f46_furniture_housing_cycle_hsxlogcapex_252d_base_v084_signal,
    f46fhc_f46_furniture_housing_cycle_revproxyxcaprev_63d_base_v085_signal,
    f46fhc_f46_furniture_housing_cycle_revproxyxcaprev_252d_base_v086_signal,
    f46fhc_f46_furniture_housing_cycle_hsxcaprev_63d_base_v087_signal,
    f46fhc_f46_furniture_housing_cycle_hsxcaprev_252d_base_v088_signal,
    f46fhc_f46_furniture_housing_cycle_revproxyema_63d_base_v089_signal,
    f46fhc_f46_furniture_housing_cycle_revproxyema_252d_base_v090_signal,
    f46fhc_f46_furniture_housing_cycle_hsignalema_63d_base_v091_signal,
    f46fhc_f46_furniture_housing_cycle_hsignalema_252d_base_v092_signal,
    f46fhc_f46_furniture_housing_cycle_revproxyxret_63d_base_v093_signal,
    f46fhc_f46_furniture_housing_cycle_revproxyxret_252d_base_v094_signal,
    f46fhc_f46_furniture_housing_cycle_hsxret_63d_base_v095_signal,
    f46fhc_f46_furniture_housing_cycle_hsxret_252d_base_v096_signal,
    f46fhc_f46_furniture_housing_cycle_hsxret_504d_base_v097_signal,
    f46fhc_f46_furniture_housing_cycle_revproxyxvol_63d_base_v098_signal,
    f46fhc_f46_furniture_housing_cycle_revproxyxvol_252d_base_v099_signal,
    f46fhc_f46_furniture_housing_cycle_hsxvol_63d_base_v100_signal,
    f46fhc_f46_furniture_housing_cycle_hsxvol_252d_base_v101_signal,
    f46fhc_f46_furniture_housing_cycle_revproxydiff_63_252_base_v102_signal,
    f46fhc_f46_furniture_housing_cycle_revproxydiff_21_126_base_v103_signal,
    f46fhc_f46_furniture_housing_cycle_hsdiff_63_252_base_v104_signal,
    f46fhc_f46_furniture_housing_cycle_hsdiff_21_126_base_v105_signal,
    f46fhc_f46_furniture_housing_cycle_revproxyqrank_63d_base_v106_signal,
    f46fhc_f46_furniture_housing_cycle_revproxyqrank_252d_base_v107_signal,
    f46fhc_f46_furniture_housing_cycle_hsqrank_63d_base_v108_signal,
    f46fhc_f46_furniture_housing_cycle_hsqrank_252d_base_v109_signal,
    f46fhc_f46_furniture_housing_cycle_seasqrank_63d_base_v110_signal,
    f46fhc_f46_furniture_housing_cycle_seasqrank_252d_base_v111_signal,
    f46fhc_f46_furniture_housing_cycle_revproxyxcapexstd_63d_base_v112_signal,
    f46fhc_f46_furniture_housing_cycle_revproxyxcapexstd_252d_base_v113_signal,
    f46fhc_f46_furniture_housing_cycle_hsxcapexstd_63d_base_v114_signal,
    f46fhc_f46_furniture_housing_cycle_hsxcapexstd_252d_base_v115_signal,
    f46fhc_f46_furniture_housing_cycle_revxseasema_63d_base_v116_signal,
    f46fhc_f46_furniture_housing_cycle_revxseasema_252d_base_v117_signal,
    f46fhc_f46_furniture_housing_cycle_hsxebmag_63d_base_v118_signal,
    f46fhc_f46_furniture_housing_cycle_hsxebmag_252d_base_v119_signal,
    f46fhc_f46_furniture_housing_cycle_revproxyxebmag_63d_base_v120_signal,
    f46fhc_f46_furniture_housing_cycle_revproxyxebmag_252d_base_v121_signal,
    f46fhc_f46_furniture_housing_cycle_revxseas2_63d_base_v122_signal,
    f46fhc_f46_furniture_housing_cycle_revxseas2_252d_base_v123_signal,
    f46fhc_f46_furniture_housing_cycle_hsignal2_63d_base_v124_signal,
    f46fhc_f46_furniture_housing_cycle_hsignal2_252d_base_v125_signal,
    f46fhc_f46_furniture_housing_cycle_revproxy2_63d_base_v126_signal,
    f46fhc_f46_furniture_housing_cycle_revproxy2_252d_base_v127_signal,
    f46fhc_f46_furniture_housing_cycle_revproxyz_5d_base_v128_signal,
    f46fhc_f46_furniture_housing_cycle_revproxyz_10d_base_v129_signal,
    f46fhc_f46_furniture_housing_cycle_revproxyz_21d_base_v130_signal,
    f46fhc_f46_furniture_housing_cycle_revproxyz_42d_base_v131_signal,
    f46fhc_f46_furniture_housing_cycle_revproxyz_189d_base_v132_signal,
    f46fhc_f46_furniture_housing_cycle_revproxyz_378d_base_v133_signal,
    f46fhc_f46_furniture_housing_cycle_hsignalz_21d_base_v134_signal,
    f46fhc_f46_furniture_housing_cycle_hsignalz_42d_base_v135_signal,
    f46fhc_f46_furniture_housing_cycle_hsignalz_189d_base_v136_signal,
    f46fhc_f46_furniture_housing_cycle_hsignalz_378d_base_v137_signal,
    f46fhc_f46_furniture_housing_cycle_seasz_21d_base_v138_signal,
    f46fhc_f46_furniture_housing_cycle_seasz_63d_base_v139_signal,
    f46fhc_f46_furniture_housing_cycle_seasz_252d_base_v140_signal,
    f46fhc_f46_furniture_housing_cycle_seasz_504d_base_v141_signal,
    f46fhc_f46_furniture_housing_cycle_rpxhs_63d_base_v142_signal,
    f46fhc_f46_furniture_housing_cycle_rpxhs_252d_base_v143_signal,
    f46fhc_f46_furniture_housing_cycle_rpxhs_504d_base_v144_signal,
    f46fhc_f46_furniture_housing_cycle_seasxhs_63d_base_v145_signal,
    f46fhc_f46_furniture_housing_cycle_seasxhs_252d_base_v146_signal,
    f46fhc_f46_furniture_housing_cycle_seasxhs_504d_base_v147_signal,
    f46fhc_f46_furniture_housing_cycle_revxabsret_63d_base_v148_signal,
    f46fhc_f46_furniture_housing_cycle_hsxabsret_252d_base_v149_signal,
    f46fhc_f46_furniture_housing_cycle_seasxabsret_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F46_FURNITURE_HOUSING_CYCLE_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")

    cols = {"closeadj": closeadj, "revenue": revenue, "ebitda": ebitda, "capex": capex}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f46_revenue_housing_proxy", "_f46_demand_seasonality", "_f46_housing_signal")
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
    print(f"OK f46_furniture_housing_cycle_base_076_150_claude: {n_features} features pass")
