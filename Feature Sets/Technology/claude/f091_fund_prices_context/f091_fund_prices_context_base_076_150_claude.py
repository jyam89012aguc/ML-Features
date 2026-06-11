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


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f091_etf_rel(closeadj, etf_close):
    return closeadj.pct_change(periods=63) - etf_close.pct_change(periods=63)


# 63d z-score of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_z_63d_base_v076_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_z_126d_base_v077_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_z_252d_base_v078_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_z_504d_base_v079_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_z_63d_base_v080_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_z_126d_base_v081_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_z_252d_base_v082_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_z_504d_base_v083_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_z_63d_base_v084_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_z_126d_base_v085_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_z_252d_base_v086_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_z_504d_base_v087_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_z_63d_base_v088_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_z_126d_base_v089_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_z_252d_base_v090_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_z_504d_base_v091_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_z_63d_base_v092_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_z_126d_base_v093_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_z_252d_base_v094_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_z_504d_base_v095_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_z_63d_base_v096_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_z_126d_base_v097_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_z_252d_base_v098_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_z_504d_base_v099_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_z_63d_base_v100_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_z_126d_base_v101_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_z_252d_base_v102_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_z_504d_base_v103_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_distmax_252d_base_v104_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_distmax_504d_base_v105_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_distmax_252d_base_v106_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_distmax_504d_base_v107_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_distmax_252d_base_v108_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_distmax_504d_base_v109_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_distmax_252d_base_v110_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_distmax_504d_base_v111_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_distmax_252d_base_v112_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_distmax_504d_base_v113_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_distmax_252d_base_v114_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_distmax_504d_base_v115_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_distmax_252d_base_v116_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_distmax_504d_base_v117_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_distmed_126d_base_v118_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_distmed_252d_base_v119_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_distmed_504d_base_v120_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_distmed_126d_base_v121_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_distmed_252d_base_v122_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_distmed_504d_base_v123_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_distmed_126d_base_v124_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_distmed_252d_base_v125_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_distmed_504d_base_v126_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_distmed_126d_base_v127_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_distmed_252d_base_v128_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_distmed_504d_base_v129_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_distmed_126d_base_v130_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_distmed_252d_base_v131_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_distmed_504d_base_v132_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_distmed_126d_base_v133_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_distmed_252d_base_v134_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_distmed_504d_base_v135_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_distmed_126d_base_v136_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_distmed_252d_base_v137_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_distmed_504d_base_v138_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_chg_63d_base_v139_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_chg_252d_base_v140_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_chg_63d_base_v141_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_chg_252d_base_v142_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_chg_63d_base_v143_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_chg_252d_base_v144_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_chg_63d_base_v145_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_chg_252d_base_v146_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_chg_63d_base_v147_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_chg_252d_base_v148_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_chg_63d_base_v149_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_chg_252d_base_v150_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

