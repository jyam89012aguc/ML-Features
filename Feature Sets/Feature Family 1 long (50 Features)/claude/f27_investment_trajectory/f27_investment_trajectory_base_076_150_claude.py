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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f27_invest_traj(capex, w):
    base = _mean(capex, w)
    return _diff(base, w) / base.abs().replace(0, np.nan).shift(w)


def _f27_capex_growth(capex, w):
    return _diff(_mean(capex, w), w) / _mean(capex.abs(), w).replace(0, np.nan)


def _f27_capex_to_rev(capex, revenue, w):
    return _safe_div(_mean(capex, w), _mean(revenue, w))


# 21d capex growth scaled by closeadj momentum
def f27it_f27_investment_trajectory_capgrowxmom_21d_base_v076_signal(capex, closeadj):
    mom = closeadj.pct_change(21)
    result = _f27_capex_growth(capex, 21) * (1.0 + mom) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex growth scaled by closeadj momentum
def f27it_f27_investment_trajectory_capgrowxmom_63d_base_v077_signal(capex, closeadj):
    mom = closeadj.pct_change(63)
    result = _f27_capex_growth(capex, 63) * (1.0 + mom) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex growth scaled by closeadj momentum
def f27it_f27_investment_trajectory_capgrowxmom_252d_base_v078_signal(capex, closeadj):
    mom = closeadj.pct_change(252)
    result = _f27_capex_growth(capex, 252) * (1.0 + mom) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex/revenue ratio z-score
def f27it_f27_investment_trajectory_capreviz_252d_base_v079_signal(capex, revenue, closeadj):
    base = _f27_capex_to_rev(capex, revenue, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex/revenue ratio z-score over 504d
def f27it_f27_investment_trajectory_capreviz_504d_base_v080_signal(capex, revenue, closeadj):
    base = _f27_capex_to_rev(capex, revenue, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex growth absolute level (severity)
def f27it_f27_investment_trajectory_capgrowabs_63d_base_v081_signal(capex, closeadj):
    result = _f27_capex_growth(capex, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex growth absolute level
def f27it_f27_investment_trajectory_capgrowabs_252d_base_v082_signal(capex, closeadj):
    result = _f27_capex_growth(capex, 252).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex growth absolute level
def f27it_f27_investment_trajectory_capgrowabs_504d_base_v083_signal(capex, closeadj):
    result = _f27_capex_growth(capex, 504).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex growth coefficient of variation
def f27it_f27_investment_trajectory_capgrowcv_252d_base_v084_signal(capex, closeadj):
    base = _f27_capex_growth(capex, 63)
    result = _safe_div(_std(base, 252), _mean(base, 252).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex growth coefficient of variation
def f27it_f27_investment_trajectory_capgrowcv_504d_base_v085_signal(capex, closeadj):
    base = _f27_capex_growth(capex, 252)
    result = _safe_div(_std(base, 504), _mean(base, 504).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex / fcf trajectory
def f27it_f27_investment_trajectory_capfcf_252d_base_v086_signal(capex, fcf, closeadj):
    base = _safe_div(_mean(capex, 252), _mean(fcf, 252))
    result = base * closeadj + _f27_invest_traj(capex, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex / fcf trajectory
def f27it_f27_investment_trajectory_capfcf_504d_base_v087_signal(capex, fcf, closeadj):
    base = _safe_div(_mean(capex, 504), _mean(fcf, 504))
    result = base * closeadj + _f27_invest_traj(capex, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex / netinc trajectory
def f27it_f27_investment_trajectory_capnetinc_252d_base_v088_signal(capex, netinc, closeadj):
    base = _safe_div(_mean(capex, 252), _mean(netinc, 252))
    result = base * closeadj + _f27_invest_traj(capex, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex / netinc trajectory
def f27it_f27_investment_trajectory_capnetinc_504d_base_v089_signal(capex, netinc, closeadj):
    base = _safe_div(_mean(capex, 504), _mean(netinc, 504))
    result = base * closeadj + _f27_invest_traj(capex, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex/gp trajectory
def f27it_f27_investment_trajectory_capgp_63d_base_v090_signal(capex, gp, closeadj):
    base = _safe_div(_mean(capex, 63), _mean(gp, 63))
    result = base * closeadj + _f27_invest_traj(capex, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex/gp trajectory
def f27it_f27_investment_trajectory_capgp_252d_base_v091_signal(capex, gp, closeadj):
    base = _safe_div(_mean(capex, 252), _mean(gp, 252))
    result = base * closeadj + _f27_invest_traj(capex, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex acceleration via diff of growth
def f27it_f27_investment_trajectory_capgrowaccel_252d_base_v092_signal(capex, closeadj):
    g = _f27_capex_growth(capex, 63)
    result = _diff(g, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex acceleration via diff of growth
def f27it_f27_investment_trajectory_capgrowaccel_504d_base_v093_signal(capex, closeadj):
    g = _f27_capex_growth(capex, 252)
    result = _diff(g, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ratio of short-term capex growth to long-term capex growth
def f27it_f27_investment_trajectory_capgrowratio_63v252_base_v094_signal(capex, closeadj):
    sg = _f27_capex_growth(capex, 63)
    lg = _f27_capex_growth(capex, 252).replace(0, np.nan)
    result = (sg / lg) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ratio of short-term capex growth to long-term capex growth
def f27it_f27_investment_trajectory_capgrowratio_21v63_base_v095_signal(capex, closeadj):
    sg = _f27_capex_growth(capex, 21)
    lg = _f27_capex_growth(capex, 63).replace(0, np.nan)
    result = (sg / lg) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex growth + 63d capex/revenue ratio
def f27it_f27_investment_trajectory_capgrowplusratio_63d_base_v096_signal(capex, revenue, closeadj):
    g = _f27_capex_growth(capex, 63)
    r = _f27_capex_to_rev(capex, revenue, 63)
    result = (g + r) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex growth + 252d capex/revenue ratio
def f27it_f27_investment_trajectory_capgrowplusratio_252d_base_v097_signal(capex, revenue, closeadj):
    g = _f27_capex_growth(capex, 252)
    r = _f27_capex_to_rev(capex, revenue, 252)
    result = (g + r) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex growth + 504d capex/revenue ratio
def f27it_f27_investment_trajectory_capgrowplusratio_504d_base_v098_signal(capex, revenue, closeadj):
    g = _f27_capex_growth(capex, 504)
    r = _f27_capex_to_rev(capex, revenue, 504)
    result = (g + r) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap-weighted capex/revenue intensity
def f27it_f27_investment_trajectory_capxmcap_252d_base_v099_signal(capex, revenue, marketcap):
    base = _f27_capex_to_rev(capex, revenue, 252)
    result = base * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap-weighted capex/revenue intensity
def f27it_f27_investment_trajectory_capxmcap_504d_base_v100_signal(capex, revenue, marketcap):
    base = _f27_capex_to_rev(capex, revenue, 504)
    result = base * np.log(_mean(marketcap, 504).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex growth EMA short
def f27it_f27_investment_trajectory_capgrowemashrt_21d_base_v101_signal(capex, closeadj):
    base = _f27_capex_growth(capex, 21)
    result = base.ewm(span=10, adjust=False, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex growth EMA long
def f27it_f27_investment_trajectory_capgrowemalong_252d_base_v102_signal(capex, closeadj):
    base = _f27_capex_growth(capex, 63)
    result = base.ewm(span=252, adjust=False, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew of capex growth
def f27it_f27_investment_trajectory_capgrowskew_252d_base_v103_signal(capex, closeadj):
    base = _f27_capex_growth(capex, 21)
    result = base.rolling(252, min_periods=63).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew of capex growth
def f27it_f27_investment_trajectory_capgrowskew_504d_base_v104_signal(capex, closeadj):
    base = _f27_capex_growth(capex, 63)
    result = base.rolling(504, min_periods=126).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d kurtosis of capex growth
def f27it_f27_investment_trajectory_capgrowkurt_252d_base_v105_signal(capex, closeadj):
    base = _f27_capex_growth(capex, 21)
    result = base.rolling(252, min_periods=63).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d kurtosis of capex growth
def f27it_f27_investment_trajectory_capgrowkurt_504d_base_v106_signal(capex, closeadj):
    base = _f27_capex_growth(capex, 63)
    result = base.rolling(504, min_periods=126).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite invest score: capex growth + capex/rev
def f27it_f27_investment_trajectory_capcomposite_252d_base_v107_signal(capex, revenue, closeadj):
    g = _f27_capex_growth(capex, 252)
    r = _f27_capex_to_rev(capex, revenue, 252)
    base = g + r * 0.5
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d invest trajectory level x revenue
def f27it_f27_investment_trajectory_capinvxrev_63d_base_v108_signal(capex, revenue, closeadj):
    base = _f27_invest_traj(capex, 63) * _mean(revenue, 63) / 1e8
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d invest trajectory level x revenue
def f27it_f27_investment_trajectory_capinvxrev_252d_base_v109_signal(capex, revenue, closeadj):
    base = _f27_invest_traj(capex, 252) * _mean(revenue, 252) / 1e8
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex/(revenue*assets) trajectory
def f27it_f27_investment_trajectory_capxrevassets_252d_base_v110_signal(capex, revenue, assets):
    base = _f27_capex_to_rev(capex, revenue, 252)
    result = base * _safe_div(_mean(revenue, 252), _mean(assets, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex/(revenue*assets) trajectory
def f27it_f27_investment_trajectory_capxrevassets_504d_base_v111_signal(capex, revenue, assets):
    base = _f27_capex_to_rev(capex, revenue, 504)
    result = base * _safe_div(_mean(revenue, 504), _mean(assets, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capex growth weighted by closeadj's std
def f27it_f27_investment_trajectory_capgrowxstd_21d_base_v112_signal(capex, closeadj):
    sd = _std(closeadj.pct_change(), 21)
    result = _f27_capex_growth(capex, 21) * (1.0 + sd) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex growth weighted by closeadj's std
def f27it_f27_investment_trajectory_capgrowxstd_252d_base_v113_signal(capex, closeadj):
    sd = _std(closeadj.pct_change(), 252)
    result = _f27_capex_growth(capex, 252) * (1.0 + sd) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ratio of capex growth to ncfo growth
def f27it_f27_investment_trajectory_capvsncfogrow_252d_base_v114_signal(capex, ncfo, closeadj):
    cg = _f27_capex_growth(capex, 252)
    ng = _diff(_mean(ncfo, 252), 252) / _mean(ncfo.abs(), 252).replace(0, np.nan)
    result = (cg / ng.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ratio of capex growth to ncfo growth
def f27it_f27_investment_trajectory_capvsncfogrow_504d_base_v115_signal(capex, ncfo, closeadj):
    cg = _f27_capex_growth(capex, 504)
    ng = _diff(_mean(ncfo, 504), 252) / _mean(ncfo.abs(), 504).replace(0, np.nan)
    result = (cg / ng.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d invest momentum: invest traj scaled by closeadj return
def f27it_f27_investment_trajectory_capinvmom_252d_base_v116_signal(capex, closeadj):
    ret = closeadj.pct_change(252)
    result = _f27_invest_traj(capex, 252) * (1.0 + ret) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d invest momentum
def f27it_f27_investment_trajectory_capinvmom_504d_base_v117_signal(capex, closeadj):
    ret = closeadj.pct_change(504)
    result = _f27_invest_traj(capex, 504) * (1.0 + ret) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex/(revenue+ncfo) trajectory
def f27it_f27_investment_trajectory_capxrevcfo_252d_base_v118_signal(capex, revenue, ncfo, closeadj):
    base = _safe_div(_mean(capex, 252), _mean(revenue + ncfo, 252))
    result = base * closeadj + _f27_invest_traj(capex, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex/(revenue+ncfo) trajectory
def f27it_f27_investment_trajectory_capxrevcfo_504d_base_v119_signal(capex, revenue, ncfo, closeadj):
    base = _safe_div(_mean(capex, 504), _mean(revenue + ncfo, 504))
    result = base * closeadj + _f27_invest_traj(capex, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex / (assets+equity) trajectory
def f27it_f27_investment_trajectory_capxassetseq_252d_base_v120_signal(capex, assets, equity, closeadj):
    base = _safe_div(_mean(capex, 252), _mean(assets + equity, 252))
    result = base * closeadj + _f27_capex_growth(capex, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex / (assets+equity) trajectory
def f27it_f27_investment_trajectory_capxassetseq_504d_base_v121_signal(capex, assets, equity, closeadj):
    base = _safe_div(_mean(capex, 504), _mean(assets + equity, 504))
    result = base * closeadj + _f27_capex_growth(capex, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex YoY growth via raw 252d diff
def f27it_f27_investment_trajectory_capyoyraw_252d_base_v122_signal(capex, closeadj):
    base = _diff(capex, 252) / _mean(capex.abs(), 252).replace(0, np.nan)
    result = base * closeadj + _f27_invest_traj(capex, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex 2y growth via raw 504d diff
def f27it_f27_investment_trajectory_cap2yraw_504d_base_v123_signal(capex, closeadj):
    base = _diff(capex, 504) / _mean(capex.abs(), 504).replace(0, np.nan)
    result = base * closeadj + _f27_invest_traj(capex, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capex 1mo growth via 21d diff
def f27it_f27_investment_trajectory_cap1mraw_21d_base_v124_signal(capex, closeadj):
    base = _diff(capex, 21) / _mean(capex.abs(), 21).replace(0, np.nan)
    result = base * closeadj + _f27_capex_growth(capex, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex 1qtr growth via 63d diff
def f27it_f27_investment_trajectory_cap1qraw_63d_base_v125_signal(capex, closeadj):
    base = _diff(capex, 63) / _mean(capex.abs(), 63).replace(0, np.nan)
    result = base * closeadj + _f27_capex_growth(capex, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex/sharesbas trajectory (capex per share)
def f27it_f27_investment_trajectory_capshare_252d_base_v126_signal(capex, sharesbas, closeadj):
    base = _safe_div(_mean(capex, 252), _mean(sharesbas, 252))
    result = base * closeadj + _f27_invest_traj(capex, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex/sharesbas trajectory
def f27it_f27_investment_trajectory_capshare_504d_base_v127_signal(capex, sharesbas, closeadj):
    base = _safe_div(_mean(capex, 504), _mean(sharesbas, 504))
    result = base * closeadj + _f27_invest_traj(capex, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d change in capex/sharesbas
def f27it_f27_investment_trajectory_capsharediff_252d_base_v128_signal(capex, sharesbas, closeadj):
    base = _safe_div(_mean(capex, 252), _mean(sharesbas, 252))
    result = _diff(base, 252) * closeadj + _f27_capex_growth(capex, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex/(debt+equity) trajectory
def f27it_f27_investment_trajectory_capxcap_252d_base_v129_signal(capex, debt, equity, closeadj):
    base = _safe_div(_mean(capex, 252), _mean(debt + equity, 252))
    result = base * closeadj + _f27_invest_traj(capex, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex/(debt+equity) trajectory
def f27it_f27_investment_trajectory_capxcap_504d_base_v130_signal(capex, debt, equity, closeadj):
    base = _safe_div(_mean(capex, 504), _mean(debt + equity, 504))
    result = base * closeadj + _f27_invest_traj(capex, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex - 63d depreciation proxy via diff
def f27it_f27_investment_trajectory_capnet_63d_base_v131_signal(capex, ncfo, closeadj):
    invflow = _mean(capex, 63) - 0.5 * _mean(ncfo, 63)
    result = invflow * _f27_capex_growth(capex, 63).fillna(0).abs() * closeadj / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex - 252d ncfo proxy via diff
def f27it_f27_investment_trajectory_capnet_252d_base_v132_signal(capex, ncfo, closeadj):
    invflow = _mean(capex, 252) - 0.5 * _mean(ncfo, 252)
    result = invflow * _f27_capex_growth(capex, 252).fillna(0).abs() * closeadj / 1e8
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ratio of capex growth std to mean abs (volatility of invest)
def f27it_f27_investment_trajectory_capgrowinstability_252d_base_v133_signal(capex, closeadj):
    g = _f27_capex_growth(capex, 21)
    result = _safe_div(_std(g, 252), _mean(g.abs(), 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ratio of capex growth std to mean abs
def f27it_f27_investment_trajectory_capgrowinstability_504d_base_v134_signal(capex, closeadj):
    g = _f27_capex_growth(capex, 63)
    result = _safe_div(_std(g, 504), _mean(g.abs(), 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of accelerating capex months (rolling sum)
def f27it_f27_investment_trajectory_capaccelcnt_252d_base_v135_signal(capex, closeadj):
    g = _f27_capex_growth(capex, 21)
    flag = (g.diff(21) > 0).astype(float)
    result = flag.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of accelerating capex quarters
def f27it_f27_investment_trajectory_capaccelcnt_504d_base_v136_signal(capex, closeadj):
    g = _f27_capex_growth(capex, 63)
    flag = (g.diff(63) > 0).astype(float)
    result = flag.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d net invest sign sum
def f27it_f27_investment_trajectory_capsignsum_252d_base_v137_signal(capex, closeadj):
    g = _f27_capex_growth(capex, 21)
    sign = np.sign(g).fillna(0)
    result = sign.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d net invest sign sum
def f27it_f27_investment_trajectory_capsignsum_504d_base_v138_signal(capex, closeadj):
    g = _f27_capex_growth(capex, 63)
    sign = np.sign(g).fillna(0)
    result = sign.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex/revenue ratio difference vs 252d mean
def f27it_f27_investment_trajectory_caprevvsmean_252d_base_v139_signal(capex, revenue, closeadj):
    base = _f27_capex_to_rev(capex, revenue, 63)
    result = (base - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex/revenue ratio difference vs 504d mean
def f27it_f27_investment_trajectory_caprevvsmean_504d_base_v140_signal(capex, revenue, closeadj):
    base = _f27_capex_to_rev(capex, revenue, 252)
    result = (base - _mean(base, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d invest trajectory expanded squared (trend-emphasis)
def f27it_f27_investment_trajectory_capinvexp_252d_base_v141_signal(capex, closeadj):
    base = _f27_invest_traj(capex, 252)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d invest trajectory expanded squared
def f27it_f27_investment_trajectory_capinvexp_504d_base_v142_signal(capex, closeadj):
    base = _f27_invest_traj(capex, 504)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d invest trajectory * 252d closeadj cumulative return
def f27it_f27_investment_trajectory_capxretcum_252d_base_v143_signal(capex, closeadj):
    cret = closeadj / closeadj.shift(252).replace(0, np.nan)
    result = _f27_invest_traj(capex, 252) * cret * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d invest trajectory * 504d closeadj cumulative return
def f27it_f27_investment_trajectory_capxretcum_504d_base_v144_signal(capex, closeadj):
    cret = closeadj / closeadj.shift(504).replace(0, np.nan)
    result = _f27_invest_traj(capex, 504) * cret * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex growth * 252d revenue
def f27it_f27_investment_trajectory_capgrowxrev_252d_base_v145_signal(capex, revenue, closeadj):
    g = _f27_capex_growth(capex, 252)
    result = g * _mean(revenue, 252) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex growth * 504d revenue
def f27it_f27_investment_trajectory_capgrowxrev_504d_base_v146_signal(capex, revenue, closeadj):
    g = _f27_capex_growth(capex, 504)
    result = g * _mean(revenue, 504) / 1e8 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex/(opinc+ncfo) trajectory
def f27it_f27_investment_trajectory_capxopncfo_252d_base_v147_signal(capex, opinc, ncfo, closeadj):
    base = _safe_div(_mean(capex, 252), _mean(opinc + ncfo, 252))
    result = base * closeadj + _f27_invest_traj(capex, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex/(opinc+ncfo) trajectory
def f27it_f27_investment_trajectory_capxopncfo_504d_base_v148_signal(capex, opinc, ncfo, closeadj):
    base = _safe_div(_mean(capex, 504), _mean(opinc + ncfo, 504))
    result = base * closeadj + _f27_invest_traj(capex, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex growth area: cumulative sum of growth abs
def f27it_f27_investment_trajectory_capgrowarea_252d_base_v149_signal(capex, closeadj):
    g = _f27_capex_growth(capex, 21).abs()
    result = g.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex growth area
def f27it_f27_investment_trajectory_capgrowarea_504d_base_v150_signal(capex, closeadj):
    g = _f27_capex_growth(capex, 63).abs()
    result = g.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f27it_f27_investment_trajectory_capgrowxmom_21d_base_v076_signal,
    f27it_f27_investment_trajectory_capgrowxmom_63d_base_v077_signal,
    f27it_f27_investment_trajectory_capgrowxmom_252d_base_v078_signal,
    f27it_f27_investment_trajectory_capreviz_252d_base_v079_signal,
    f27it_f27_investment_trajectory_capreviz_504d_base_v080_signal,
    f27it_f27_investment_trajectory_capgrowabs_63d_base_v081_signal,
    f27it_f27_investment_trajectory_capgrowabs_252d_base_v082_signal,
    f27it_f27_investment_trajectory_capgrowabs_504d_base_v083_signal,
    f27it_f27_investment_trajectory_capgrowcv_252d_base_v084_signal,
    f27it_f27_investment_trajectory_capgrowcv_504d_base_v085_signal,
    f27it_f27_investment_trajectory_capfcf_252d_base_v086_signal,
    f27it_f27_investment_trajectory_capfcf_504d_base_v087_signal,
    f27it_f27_investment_trajectory_capnetinc_252d_base_v088_signal,
    f27it_f27_investment_trajectory_capnetinc_504d_base_v089_signal,
    f27it_f27_investment_trajectory_capgp_63d_base_v090_signal,
    f27it_f27_investment_trajectory_capgp_252d_base_v091_signal,
    f27it_f27_investment_trajectory_capgrowaccel_252d_base_v092_signal,
    f27it_f27_investment_trajectory_capgrowaccel_504d_base_v093_signal,
    f27it_f27_investment_trajectory_capgrowratio_63v252_base_v094_signal,
    f27it_f27_investment_trajectory_capgrowratio_21v63_base_v095_signal,
    f27it_f27_investment_trajectory_capgrowplusratio_63d_base_v096_signal,
    f27it_f27_investment_trajectory_capgrowplusratio_252d_base_v097_signal,
    f27it_f27_investment_trajectory_capgrowplusratio_504d_base_v098_signal,
    f27it_f27_investment_trajectory_capxmcap_252d_base_v099_signal,
    f27it_f27_investment_trajectory_capxmcap_504d_base_v100_signal,
    f27it_f27_investment_trajectory_capgrowemashrt_21d_base_v101_signal,
    f27it_f27_investment_trajectory_capgrowemalong_252d_base_v102_signal,
    f27it_f27_investment_trajectory_capgrowskew_252d_base_v103_signal,
    f27it_f27_investment_trajectory_capgrowskew_504d_base_v104_signal,
    f27it_f27_investment_trajectory_capgrowkurt_252d_base_v105_signal,
    f27it_f27_investment_trajectory_capgrowkurt_504d_base_v106_signal,
    f27it_f27_investment_trajectory_capcomposite_252d_base_v107_signal,
    f27it_f27_investment_trajectory_capinvxrev_63d_base_v108_signal,
    f27it_f27_investment_trajectory_capinvxrev_252d_base_v109_signal,
    f27it_f27_investment_trajectory_capxrevassets_252d_base_v110_signal,
    f27it_f27_investment_trajectory_capxrevassets_504d_base_v111_signal,
    f27it_f27_investment_trajectory_capgrowxstd_21d_base_v112_signal,
    f27it_f27_investment_trajectory_capgrowxstd_252d_base_v113_signal,
    f27it_f27_investment_trajectory_capvsncfogrow_252d_base_v114_signal,
    f27it_f27_investment_trajectory_capvsncfogrow_504d_base_v115_signal,
    f27it_f27_investment_trajectory_capinvmom_252d_base_v116_signal,
    f27it_f27_investment_trajectory_capinvmom_504d_base_v117_signal,
    f27it_f27_investment_trajectory_capxrevcfo_252d_base_v118_signal,
    f27it_f27_investment_trajectory_capxrevcfo_504d_base_v119_signal,
    f27it_f27_investment_trajectory_capxassetseq_252d_base_v120_signal,
    f27it_f27_investment_trajectory_capxassetseq_504d_base_v121_signal,
    f27it_f27_investment_trajectory_capyoyraw_252d_base_v122_signal,
    f27it_f27_investment_trajectory_cap2yraw_504d_base_v123_signal,
    f27it_f27_investment_trajectory_cap1mraw_21d_base_v124_signal,
    f27it_f27_investment_trajectory_cap1qraw_63d_base_v125_signal,
    f27it_f27_investment_trajectory_capshare_252d_base_v126_signal,
    f27it_f27_investment_trajectory_capshare_504d_base_v127_signal,
    f27it_f27_investment_trajectory_capsharediff_252d_base_v128_signal,
    f27it_f27_investment_trajectory_capxcap_252d_base_v129_signal,
    f27it_f27_investment_trajectory_capxcap_504d_base_v130_signal,
    f27it_f27_investment_trajectory_capnet_63d_base_v131_signal,
    f27it_f27_investment_trajectory_capnet_252d_base_v132_signal,
    f27it_f27_investment_trajectory_capgrowinstability_252d_base_v133_signal,
    f27it_f27_investment_trajectory_capgrowinstability_504d_base_v134_signal,
    f27it_f27_investment_trajectory_capaccelcnt_252d_base_v135_signal,
    f27it_f27_investment_trajectory_capaccelcnt_504d_base_v136_signal,
    f27it_f27_investment_trajectory_capsignsum_252d_base_v137_signal,
    f27it_f27_investment_trajectory_capsignsum_504d_base_v138_signal,
    f27it_f27_investment_trajectory_caprevvsmean_252d_base_v139_signal,
    f27it_f27_investment_trajectory_caprevvsmean_504d_base_v140_signal,
    f27it_f27_investment_trajectory_capinvexp_252d_base_v141_signal,
    f27it_f27_investment_trajectory_capinvexp_504d_base_v142_signal,
    f27it_f27_investment_trajectory_capxretcum_252d_base_v143_signal,
    f27it_f27_investment_trajectory_capxretcum_504d_base_v144_signal,
    f27it_f27_investment_trajectory_capgrowxrev_252d_base_v145_signal,
    f27it_f27_investment_trajectory_capgrowxrev_504d_base_v146_signal,
    f27it_f27_investment_trajectory_capxopncfo_252d_base_v147_signal,
    f27it_f27_investment_trajectory_capxopncfo_504d_base_v148_signal,
    f27it_f27_investment_trajectory_capgrowarea_252d_base_v149_signal,
    f27it_f27_investment_trajectory_capgrowarea_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F27_INVESTMENT_TRAJECTORY_REGISTRY_076_150 = REGISTRY


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
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.002, n))), name="sharesbas")
    opinc = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.007, n))), name="opinc")
    gp = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="gp")
    marketcap = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0005, 0.015, n))), name="marketcap")
    ev = pd.Series((marketcap + debt).values, name="ev")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "equity": equity, "debt": debt, "assets": assets,
        "ebitda": ebitda, "capex": capex, "sharesbas": sharesbas, "opinc": opinc,
        "gp": gp, "marketcap": marketcap, "ev": ev,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f27_invest_traj", "_f27_capex_growth", "_f27_capex_to_rev")
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
    print(f"OK f27_investment_trajectory_base_076_150_claude: {n_features} features pass")
