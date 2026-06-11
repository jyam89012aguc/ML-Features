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
def _f27_revenue_floor(revenue, w):
    return revenue.rolling(w, min_periods=max(1, w // 2)).min()


def _f27_non_cyclical_share_proxy(revenue, w):
    mn = revenue.rolling(w, min_periods=max(1, w // 2)).min()
    m = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    return mn / m.replace(0, np.nan)


def _f27_durability_score(revenue, ebitdamargin, w):
    rsd = revenue.pct_change().rolling(w, min_periods=max(1, w // 2)).std()
    msd = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).std()
    return 1.0 / ((rsd.replace(0, np.nan) + 1e-6) * (msd.replace(0, np.nan) + 1e-6))


def f27rrd_f27_repair_remodel_durability_floor_10d_base_v076_signal(revenue, closeadj):
    result = _f27_revenue_floor(revenue, 10) / revenue.replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_10d_base_v077_signal(revenue, closeadj):
    result = _f27_non_cyclical_share_proxy(revenue, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_dur_10d_base_v078_signal(revenue, ebitdamargin, closeadj):
    d = np.log(_f27_durability_score(revenue, ebitdamargin, 10).replace(0, np.nan).abs() + 1.0)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_dur_378d_base_v079_signal(revenue, ebitdamargin, closeadj):
    d = np.log(_f27_durability_score(revenue, ebitdamargin, 378).replace(0, np.nan).abs() + 1.0)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorma_126d_base_v080_signal(revenue, closeadj):
    base = _f27_revenue_floor(revenue, 504) / revenue.replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorema_126d_base_v081_signal(revenue, closeadj):
    f = _f27_revenue_floor(revenue, 504) / revenue.replace(0, np.nan)
    result = f.ewm(span=126, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_shareema_126d_base_v082_signal(revenue, closeadj):
    s = _f27_non_cyclical_share_proxy(revenue, 504)
    result = s.ewm(span=126, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_durema_63d_base_v083_signal(revenue, ebitdamargin, closeadj):
    d = np.log(_f27_durability_score(revenue, ebitdamargin, 63).replace(0, np.nan).abs() + 1.0)
    result = d.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_durema_126d_base_v084_signal(revenue, ebitdamargin, closeadj):
    d = np.log(_f27_durability_score(revenue, ebitdamargin, 252).replace(0, np.nan).abs() + 1.0)
    result = d.ewm(span=126, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorrank_504d_base_v085_signal(revenue, closeadj):
    f = _f27_revenue_floor(revenue, 63) / revenue.replace(0, np.nan)
    rank = f.rolling(504, min_periods=126).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharerank_504d_base_v086_signal(revenue, closeadj):
    s = _f27_non_cyclical_share_proxy(revenue, 63)
    rank = s.rolling(504, min_periods=126).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_durrank_504d_base_v087_signal(revenue, ebitdamargin, closeadj):
    d = np.log(_f27_durability_score(revenue, ebitdamargin, 63).replace(0, np.nan).abs() + 1.0)
    rank = d.rolling(504, min_periods=126).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorxrange_252d_base_v088_signal(revenue, closeadj):
    f = _f27_revenue_floor(revenue, 252) / revenue.replace(0, np.nan)
    rng = closeadj.rolling(252, min_periods=63).max() - closeadj.rolling(252, min_periods=63).min()
    result = f * rng
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharexrange_252d_base_v089_signal(revenue, closeadj):
    s = _f27_non_cyclical_share_proxy(revenue, 252)
    rng = closeadj.rolling(252, min_periods=63).max() - closeadj.rolling(252, min_periods=63).min()
    result = s * rng
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_durxrange_252d_base_v090_signal(revenue, ebitdamargin, closeadj):
    d = np.log(_f27_durability_score(revenue, ebitdamargin, 252).replace(0, np.nan).abs() + 1.0)
    rng = closeadj.rolling(252, min_periods=63).max() - closeadj.rolling(252, min_periods=63).min()
    result = d * rng
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorxstd_252d_base_v091_signal(revenue, closeadj):
    f = _f27_revenue_floor(revenue, 252) / revenue.replace(0, np.nan)
    sd = _std(closeadj, 252)
    result = f * sd * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharexstd_252d_base_v092_signal(revenue, closeadj):
    s = _f27_non_cyclical_share_proxy(revenue, 252)
    sd = _std(closeadj, 252)
    result = s * sd * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_durxstd_252d_base_v093_signal(revenue, ebitdamargin, closeadj):
    d = np.log(_f27_durability_score(revenue, ebitdamargin, 252).replace(0, np.nan).abs() + 1.0)
    sd = _std(closeadj, 252)
    result = d * sd * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorxebmgnma_63d_base_v094_signal(revenue, ebitdamargin, closeadj):
    f = _f27_revenue_floor(revenue, 63) / revenue.replace(0, np.nan)
    em = _mean(ebitdamargin, 63)
    result = f * em * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharexebmgnma_63d_base_v095_signal(revenue, ebitdamargin, closeadj):
    s = _f27_non_cyclical_share_proxy(revenue, 63)
    em = _mean(ebitdamargin, 63)
    result = s * em * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_minusmean_63d_base_v096_signal(revenue, closeadj):
    f = _f27_revenue_floor(revenue, 63) / revenue.replace(0, np.nan)
    result = (f - _mean(f, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_minusmean_252d_base_v097_signal(revenue, closeadj):
    s = _f27_non_cyclical_share_proxy(revenue, 252)
    result = (s - _mean(s, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_dur_minusmean_252d_base_v098_signal(revenue, ebitdamargin, closeadj):
    d = np.log(_f27_durability_score(revenue, ebitdamargin, 252).replace(0, np.nan).abs() + 1.0)
    result = (d - _mean(d, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorxpx_63d_base_v099_signal(revenue, closeadj):
    f = _f27_revenue_floor(revenue, 63) / revenue.replace(0, np.nan)
    px_chg = closeadj.pct_change(63)
    result = f * px_chg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharexpx_63d_base_v100_signal(revenue, closeadj):
    s = _f27_non_cyclical_share_proxy(revenue, 63)
    px_chg = closeadj.pct_change(63)
    result = s * px_chg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_durxpx_63d_base_v101_signal(revenue, ebitdamargin, closeadj):
    d = np.log(_f27_durability_score(revenue, ebitdamargin, 63).replace(0, np.nan).abs() + 1.0)
    px_chg = closeadj.pct_change(63)
    result = d * px_chg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorinv_63d_base_v102_signal(revenue, closeadj):
    f = _f27_revenue_floor(revenue, 63) / revenue.replace(0, np.nan)
    # invert - high erosion (low floor share) becomes signal
    result = (1.0 - f) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_shareinv_252d_base_v103_signal(revenue, closeadj):
    s = _f27_non_cyclical_share_proxy(revenue, 252)
    result = (1.0 - s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorvar_63d_base_v104_signal(revenue, closeadj):
    f = _f27_revenue_floor(revenue, 63) / revenue.replace(0, np.nan)
    result = (f.rolling(63, min_periods=21).var()) * closeadj * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharevar_252d_base_v105_signal(revenue, closeadj):
    s = _f27_non_cyclical_share_proxy(revenue, 252)
    result = (s.rolling(252, min_periods=63).var()) * closeadj * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorxpxgap_63d_base_v106_signal(revenue, closeadj):
    f = _f27_revenue_floor(revenue, 63) / revenue.replace(0, np.nan)
    px_gap = closeadj - _mean(closeadj, 63)
    result = f * px_gap
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharexpxgap_63d_base_v107_signal(revenue, closeadj):
    s = _f27_non_cyclical_share_proxy(revenue, 63)
    px_gap = closeadj - _mean(closeadj, 63)
    result = s * px_gap
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_durxpxgap_252d_base_v108_signal(revenue, ebitdamargin, closeadj):
    d = np.log(_f27_durability_score(revenue, ebitdamargin, 252).replace(0, np.nan).abs() + 1.0)
    px_gap = closeadj - _mean(closeadj, 252)
    result = d * px_gap
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorxshare_42d_base_v109_signal(revenue, closeadj):
    f = _f27_revenue_floor(revenue, 42) / revenue.replace(0, np.nan)
    s = _f27_non_cyclical_share_proxy(revenue, 42)
    result = f * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorxshare_189d_base_v110_signal(revenue, closeadj):
    f = _f27_revenue_floor(revenue, 189) / revenue.replace(0, np.nan)
    s = _f27_non_cyclical_share_proxy(revenue, 189)
    result = f * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_volz_63d_base_v111_signal(revenue, closeadj):
    f = _f27_revenue_floor(revenue, 63) / revenue.replace(0, np.nan)
    result = f * _z(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_volz_63d_base_v112_signal(revenue, closeadj):
    s = _f27_non_cyclical_share_proxy(revenue, 63)
    result = s * _z(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_dur_volz_63d_base_v113_signal(revenue, ebitdamargin, closeadj):
    d = np.log(_f27_durability_score(revenue, ebitdamargin, 63).replace(0, np.nan).abs() + 1.0)
    result = d * _z(closeadj, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorvslog_252d_base_v114_signal(revenue, closeadj):
    f = _f27_revenue_floor(revenue, 252) / revenue.replace(0, np.nan)
    result = f * np.log(revenue.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharevslog_252d_base_v115_signal(revenue, closeadj):
    s = _f27_non_cyclical_share_proxy(revenue, 252)
    result = s * np.log(revenue.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_durvslog_252d_base_v116_signal(revenue, ebitdamargin, closeadj):
    d = np.log(_f27_durability_score(revenue, ebitdamargin, 252).replace(0, np.nan).abs() + 1.0)
    result = d * np.log(revenue.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorxshareratio_63d_base_v117_signal(revenue, ebitdamargin, closeadj):
    f = _f27_revenue_floor(revenue, 63) / revenue.replace(0, np.nan)
    s = _f27_non_cyclical_share_proxy(revenue, 63)
    result = f / s.replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_minusshare_63d_base_v118_signal(revenue, closeadj):
    f = _f27_revenue_floor(revenue, 63) / revenue.replace(0, np.nan)
    s = _f27_non_cyclical_share_proxy(revenue, 63)
    result = (f - s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_plusshare_252d_base_v119_signal(revenue, closeadj):
    f = _f27_revenue_floor(revenue, 252) / revenue.replace(0, np.nan)
    s = _f27_non_cyclical_share_proxy(revenue, 252)
    result = (f + s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorxdurz_252d_base_v120_signal(revenue, ebitdamargin, closeadj):
    f = _f27_revenue_floor(revenue, 252) / revenue.replace(0, np.nan)
    d = np.log(_f27_durability_score(revenue, ebitdamargin, 252).replace(0, np.nan).abs() + 1.0)
    result = f * _z(d, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_sharexdurz_252d_base_v121_signal(revenue, ebitdamargin, closeadj):
    s = _f27_non_cyclical_share_proxy(revenue, 252)
    d = np.log(_f27_durability_score(revenue, ebitdamargin, 252).replace(0, np.nan).abs() + 1.0)
    result = s * _z(d, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorinvxshare_63d_base_v122_signal(revenue, closeadj):
    f = _f27_revenue_floor(revenue, 63) / revenue.replace(0, np.nan)
    s = _f27_non_cyclical_share_proxy(revenue, 63)
    result = (1.0 - f) * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floorxinvshare_252d_base_v123_signal(revenue, closeadj):
    f = _f27_revenue_floor(revenue, 252) / revenue.replace(0, np.nan)
    s = _f27_non_cyclical_share_proxy(revenue, 252)
    result = f * (1.0 - s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_sharediff_252d_base_v124_signal(revenue, closeadj):
    f = _f27_revenue_floor(revenue, 252) / revenue.replace(0, np.nan)
    s = _f27_non_cyclical_share_proxy(revenue, 252)
    result = (f - s.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_dur_floor_252d_base_v125_signal(revenue, ebitdamargin, closeadj):
    d = np.log(_f27_durability_score(revenue, ebitdamargin, 252).replace(0, np.nan).abs() + 1.0)
    f = _f27_revenue_floor(revenue, 252) / revenue.replace(0, np.nan)
    result = (d * f) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_dur_share_252d_base_v126_signal(revenue, ebitdamargin, closeadj):
    d = np.log(_f27_durability_score(revenue, ebitdamargin, 252).replace(0, np.nan).abs() + 1.0)
    s = _f27_non_cyclical_share_proxy(revenue, 252)
    result = (d * s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_durmean_63d_base_v127_signal(revenue, ebitdamargin, closeadj):
    d = np.log(_f27_durability_score(revenue, ebitdamargin, 63).replace(0, np.nan).abs() + 1.0)
    result = _mean(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_durstd_63d_base_v128_signal(revenue, ebitdamargin, closeadj):
    d = np.log(_f27_durability_score(revenue, ebitdamargin, 63).replace(0, np.nan).abs() + 1.0)
    result = _std(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_logminus_252d_base_v129_signal(revenue, closeadj):
    f = _f27_revenue_floor(revenue, 252)
    result = (np.log(revenue.replace(0, np.nan).abs() + 1.0) - np.log(f.replace(0, np.nan).abs() + 1.0)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_revchg_63d_base_v130_signal(revenue, closeadj):
    s = _f27_non_cyclical_share_proxy(revenue, 63)
    rev_chg = revenue.pct_change(63)
    result = s * rev_chg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_revchg_252d_base_v131_signal(revenue, closeadj):
    f = _f27_revenue_floor(revenue, 252) / revenue.replace(0, np.nan)
    rev_chg = revenue.pct_change(252)
    result = f * rev_chg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_dur_revchg_252d_base_v132_signal(revenue, ebitdamargin, closeadj):
    d = np.log(_f27_durability_score(revenue, ebitdamargin, 252).replace(0, np.nan).abs() + 1.0)
    rev_chg = revenue.pct_change(252)
    result = d * rev_chg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_pxratio_252d_base_v133_signal(revenue, closeadj):
    f = _f27_revenue_floor(revenue, 252) / revenue.replace(0, np.nan)
    px_ratio = closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = f * px_ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_pxratio_252d_base_v134_signal(revenue, closeadj):
    s = _f27_non_cyclical_share_proxy(revenue, 252)
    px_ratio = closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = s * px_ratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_sigxclose_252d_base_v135_signal(revenue, closeadj):
    f = _f27_revenue_floor(revenue, 252) / revenue.replace(0, np.nan)
    result = np.sign(f - 0.5) * closeadj * (closeadj / _mean(closeadj, 252).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_sigxclose_252d_base_v136_signal(revenue, closeadj):
    s = _f27_non_cyclical_share_proxy(revenue, 252)
    result = np.sign(s - 0.5) * closeadj * (closeadj / _mean(closeadj, 252).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_x_logclose_63d_base_v137_signal(revenue, closeadj):
    f = _f27_revenue_floor(revenue, 63) / revenue.replace(0, np.nan)
    result = f * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_x_logclose_63d_base_v138_signal(revenue, closeadj):
    s = _f27_non_cyclical_share_proxy(revenue, 63)
    result = s * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_durxlogclose_252d_base_v139_signal(revenue, ebitdamargin, closeadj):
    d = np.log(_f27_durability_score(revenue, ebitdamargin, 252).replace(0, np.nan).abs() + 1.0)
    result = d * np.log(closeadj.replace(0, np.nan).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_zema_252d_base_v140_signal(revenue, closeadj):
    f = _f27_revenue_floor(revenue, 504) / revenue.replace(0, np.nan)
    result = _z(f, 504).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_zema_252d_base_v141_signal(revenue, closeadj):
    s = _f27_non_cyclical_share_proxy(revenue, 504)
    result = _z(s, 504).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_dur_zema_252d_base_v142_signal(revenue, ebitdamargin, closeadj):
    d = np.log(_f27_durability_score(revenue, ebitdamargin, 252).replace(0, np.nan).abs() + 1.0)
    result = _z(d, 504).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_dur_minus_252d_base_v143_signal(revenue, ebitdamargin, closeadj):
    f = _f27_revenue_floor(revenue, 252) / revenue.replace(0, np.nan)
    d = np.log(_f27_durability_score(revenue, ebitdamargin, 252).replace(0, np.nan).abs() + 1.0)
    result = (f - _mean(d, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_dur_minus_252d_base_v144_signal(revenue, ebitdamargin, closeadj):
    s = _f27_non_cyclical_share_proxy(revenue, 252)
    d = np.log(_f27_durability_score(revenue, ebitdamargin, 252).replace(0, np.nan).abs() + 1.0)
    result = (s - _mean(d, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_logemamean_63d_base_v145_signal(revenue, closeadj):
    f = _f27_revenue_floor(revenue, 63) / revenue.replace(0, np.nan)
    result = (np.log(f.replace(0, np.nan).abs() + 1.0).ewm(span=21, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_logemamean_63d_base_v146_signal(revenue, closeadj):
    s = _f27_non_cyclical_share_proxy(revenue, 63)
    result = (np.log(s.replace(0, np.nan).abs() + 1.0).ewm(span=21, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_floor_ebmgnchg_63d_base_v147_signal(revenue, ebitdamargin, closeadj):
    f = _f27_revenue_floor(revenue, 63) / revenue.replace(0, np.nan)
    emc = ebitdamargin.diff(63)
    result = f * emc * closeadj * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_share_ebmgnchg_63d_base_v148_signal(revenue, ebitdamargin, closeadj):
    s = _f27_non_cyclical_share_proxy(revenue, 63)
    emc = ebitdamargin.diff(63)
    result = s * emc * closeadj * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_dur_ebmgnchg_252d_base_v149_signal(revenue, ebitdamargin, closeadj):
    d = np.log(_f27_durability_score(revenue, ebitdamargin, 252).replace(0, np.nan).abs() + 1.0)
    emc = ebitdamargin.diff(252)
    result = d * emc * closeadj * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


def f27rrd_f27_repair_remodel_durability_compow2_252d_base_v150_signal(revenue, ebitdamargin, closeadj):
    f = _f27_revenue_floor(revenue, 252) / revenue.replace(0, np.nan)
    s = _f27_non_cyclical_share_proxy(revenue, 252)
    d = np.log(_f27_durability_score(revenue, ebitdamargin, 252).replace(0, np.nan).abs() + 1.0)
    result = (0.4 * f + 0.4 * s + 0.2 * d) * closeadj * (1.0 + closeadj.pct_change(63))
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f27rrd_f27_repair_remodel_durability_floor_10d_base_v076_signal,
    f27rrd_f27_repair_remodel_durability_share_10d_base_v077_signal,
    f27rrd_f27_repair_remodel_durability_dur_10d_base_v078_signal,
    f27rrd_f27_repair_remodel_durability_dur_378d_base_v079_signal,
    f27rrd_f27_repair_remodel_durability_floorma_126d_base_v080_signal,
    f27rrd_f27_repair_remodel_durability_floorema_126d_base_v081_signal,
    f27rrd_f27_repair_remodel_durability_shareema_126d_base_v082_signal,
    f27rrd_f27_repair_remodel_durability_durema_63d_base_v083_signal,
    f27rrd_f27_repair_remodel_durability_durema_126d_base_v084_signal,
    f27rrd_f27_repair_remodel_durability_floorrank_504d_base_v085_signal,
    f27rrd_f27_repair_remodel_durability_sharerank_504d_base_v086_signal,
    f27rrd_f27_repair_remodel_durability_durrank_504d_base_v087_signal,
    f27rrd_f27_repair_remodel_durability_floorxrange_252d_base_v088_signal,
    f27rrd_f27_repair_remodel_durability_sharexrange_252d_base_v089_signal,
    f27rrd_f27_repair_remodel_durability_durxrange_252d_base_v090_signal,
    f27rrd_f27_repair_remodel_durability_floorxstd_252d_base_v091_signal,
    f27rrd_f27_repair_remodel_durability_sharexstd_252d_base_v092_signal,
    f27rrd_f27_repair_remodel_durability_durxstd_252d_base_v093_signal,
    f27rrd_f27_repair_remodel_durability_floorxebmgnma_63d_base_v094_signal,
    f27rrd_f27_repair_remodel_durability_sharexebmgnma_63d_base_v095_signal,
    f27rrd_f27_repair_remodel_durability_floor_minusmean_63d_base_v096_signal,
    f27rrd_f27_repair_remodel_durability_share_minusmean_252d_base_v097_signal,
    f27rrd_f27_repair_remodel_durability_dur_minusmean_252d_base_v098_signal,
    f27rrd_f27_repair_remodel_durability_floorxpx_63d_base_v099_signal,
    f27rrd_f27_repair_remodel_durability_sharexpx_63d_base_v100_signal,
    f27rrd_f27_repair_remodel_durability_durxpx_63d_base_v101_signal,
    f27rrd_f27_repair_remodel_durability_floorinv_63d_base_v102_signal,
    f27rrd_f27_repair_remodel_durability_shareinv_252d_base_v103_signal,
    f27rrd_f27_repair_remodel_durability_floorvar_63d_base_v104_signal,
    f27rrd_f27_repair_remodel_durability_sharevar_252d_base_v105_signal,
    f27rrd_f27_repair_remodel_durability_floorxpxgap_63d_base_v106_signal,
    f27rrd_f27_repair_remodel_durability_sharexpxgap_63d_base_v107_signal,
    f27rrd_f27_repair_remodel_durability_durxpxgap_252d_base_v108_signal,
    f27rrd_f27_repair_remodel_durability_floorxshare_42d_base_v109_signal,
    f27rrd_f27_repair_remodel_durability_floorxshare_189d_base_v110_signal,
    f27rrd_f27_repair_remodel_durability_floor_volz_63d_base_v111_signal,
    f27rrd_f27_repair_remodel_durability_share_volz_63d_base_v112_signal,
    f27rrd_f27_repair_remodel_durability_dur_volz_63d_base_v113_signal,
    f27rrd_f27_repair_remodel_durability_floorvslog_252d_base_v114_signal,
    f27rrd_f27_repair_remodel_durability_sharevslog_252d_base_v115_signal,
    f27rrd_f27_repair_remodel_durability_durvslog_252d_base_v116_signal,
    f27rrd_f27_repair_remodel_durability_floorxshareratio_63d_base_v117_signal,
    f27rrd_f27_repair_remodel_durability_floor_minusshare_63d_base_v118_signal,
    f27rrd_f27_repair_remodel_durability_floor_plusshare_252d_base_v119_signal,
    f27rrd_f27_repair_remodel_durability_floorxdurz_252d_base_v120_signal,
    f27rrd_f27_repair_remodel_durability_sharexdurz_252d_base_v121_signal,
    f27rrd_f27_repair_remodel_durability_floorinvxshare_63d_base_v122_signal,
    f27rrd_f27_repair_remodel_durability_floorxinvshare_252d_base_v123_signal,
    f27rrd_f27_repair_remodel_durability_floor_sharediff_252d_base_v124_signal,
    f27rrd_f27_repair_remodel_durability_dur_floor_252d_base_v125_signal,
    f27rrd_f27_repair_remodel_durability_dur_share_252d_base_v126_signal,
    f27rrd_f27_repair_remodel_durability_durmean_63d_base_v127_signal,
    f27rrd_f27_repair_remodel_durability_durstd_63d_base_v128_signal,
    f27rrd_f27_repair_remodel_durability_floor_logminus_252d_base_v129_signal,
    f27rrd_f27_repair_remodel_durability_share_revchg_63d_base_v130_signal,
    f27rrd_f27_repair_remodel_durability_floor_revchg_252d_base_v131_signal,
    f27rrd_f27_repair_remodel_durability_dur_revchg_252d_base_v132_signal,
    f27rrd_f27_repair_remodel_durability_floor_pxratio_252d_base_v133_signal,
    f27rrd_f27_repair_remodel_durability_share_pxratio_252d_base_v134_signal,
    f27rrd_f27_repair_remodel_durability_floor_sigxclose_252d_base_v135_signal,
    f27rrd_f27_repair_remodel_durability_share_sigxclose_252d_base_v136_signal,
    f27rrd_f27_repair_remodel_durability_floor_x_logclose_63d_base_v137_signal,
    f27rrd_f27_repair_remodel_durability_share_x_logclose_63d_base_v138_signal,
    f27rrd_f27_repair_remodel_durability_durxlogclose_252d_base_v139_signal,
    f27rrd_f27_repair_remodel_durability_floor_zema_252d_base_v140_signal,
    f27rrd_f27_repair_remodel_durability_share_zema_252d_base_v141_signal,
    f27rrd_f27_repair_remodel_durability_dur_zema_252d_base_v142_signal,
    f27rrd_f27_repair_remodel_durability_floor_dur_minus_252d_base_v143_signal,
    f27rrd_f27_repair_remodel_durability_share_dur_minus_252d_base_v144_signal,
    f27rrd_f27_repair_remodel_durability_floor_logemamean_63d_base_v145_signal,
    f27rrd_f27_repair_remodel_durability_share_logemamean_63d_base_v146_signal,
    f27rrd_f27_repair_remodel_durability_floor_ebmgnchg_63d_base_v147_signal,
    f27rrd_f27_repair_remodel_durability_share_ebmgnchg_63d_base_v148_signal,
    f27rrd_f27_repair_remodel_durability_dur_ebmgnchg_252d_base_v149_signal,
    f27rrd_f27_repair_remodel_durability_compow2_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F27_REPAIR_REMODEL_DURABILITY_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f27_revenue_floor", "_f27_non_cyclical_share_proxy", "_f27_durability_score")
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
    print(f"OK f27_repair_remodel_durability_base_076_150_claude: {n_features} features pass")
