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
def _f071_pb(marketcap, equity):
    return marketcap / equity.replace(0, np.nan).abs()


# 63d z-score of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_z_63d_base_v076_signal(pb, closeadj):
    base = pb
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_z_126d_base_v077_signal(pb, closeadj):
    base = pb
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_z_252d_base_v078_signal(pb, closeadj):
    base = pb
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_z_504d_base_v079_signal(pb, closeadj):
    base = pb
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_z_63d_base_v080_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_z_126d_base_v081_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_z_252d_base_v082_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_z_504d_base_v083_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_z_63d_base_v084_signal(bvps, closeadj):
    base = bvps
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_z_126d_base_v085_signal(bvps, closeadj):
    base = bvps
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_z_252d_base_v086_signal(bvps, closeadj):
    base = bvps
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_z_504d_base_v087_signal(bvps, closeadj):
    base = bvps
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_z_63d_base_v088_signal(tbvps, closeadj):
    base = tbvps
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_z_126d_base_v089_signal(tbvps, closeadj):
    base = tbvps
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_z_252d_base_v090_signal(tbvps, closeadj):
    base = tbvps
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_z_504d_base_v091_signal(tbvps, closeadj):
    base = tbvps
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_z_63d_base_v092_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_z_126d_base_v093_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_z_252d_base_v094_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_z_504d_base_v095_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of book_yield
def f071pbv_f071_price_book_valuation_book_yield_z_63d_base_v096_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of book_yield
def f071pbv_f071_price_book_valuation_book_yield_z_126d_base_v097_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of book_yield
def f071pbv_f071_price_book_valuation_book_yield_z_252d_base_v098_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of book_yield
def f071pbv_f071_price_book_valuation_book_yield_z_504d_base_v099_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_z_63d_base_v100_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_z_126d_base_v101_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_z_252d_base_v102_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_z_504d_base_v103_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of pb_peer_sector_dist
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_z_63d_base_v104_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of pb_peer_sector_dist
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_z_126d_base_v105_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of pb_peer_sector_dist
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_z_252d_base_v106_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of pb_peer_sector_dist
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_z_504d_base_v107_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of pb_peer_sector_z
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_z_63d_base_v108_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = (pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of pb_peer_sector_z
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_z_126d_base_v109_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = (pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of pb_peer_sector_z
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_z_252d_base_v110_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = (pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of pb_peer_sector_z
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_z_504d_base_v111_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = (pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of pb_peer_industry_dist
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_z_63d_base_v112_signal(pb, pb_industry_med, closeadj):
    base = (pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of pb_peer_industry_dist
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_z_126d_base_v113_signal(pb, pb_industry_med, closeadj):
    base = (pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of pb_peer_industry_dist
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_z_252d_base_v114_signal(pb, pb_industry_med, closeadj):
    base = (pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of pb_peer_industry_dist
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_z_504d_base_v115_signal(pb, pb_industry_med, closeadj):
    base = (pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of pb_peer_mcap_bucket_dist
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_z_63d_base_v116_signal(pb, pb_mcap_med, closeadj):
    base = (pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of pb_peer_mcap_bucket_dist
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_z_126d_base_v117_signal(pb, pb_mcap_med, closeadj):
    base = (pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of pb_peer_mcap_bucket_dist
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_z_252d_base_v118_signal(pb, pb_mcap_med, closeadj):
    base = (pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of pb_peer_mcap_bucket_dist
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_z_504d_base_v119_signal(pb, pb_mcap_med, closeadj):
    base = (pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of pb_peer_sector_pctile
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_z_63d_base_v120_signal(pb_sector_pctile, closeadj):
    base = pb_sector_pctile
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of pb_peer_sector_pctile
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_z_126d_base_v121_signal(pb_sector_pctile, closeadj):
    base = pb_sector_pctile
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of pb_peer_sector_pctile
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_z_252d_base_v122_signal(pb_sector_pctile, closeadj):
    base = pb_sector_pctile
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of pb_peer_sector_pctile
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_z_504d_base_v123_signal(pb_sector_pctile, closeadj):
    base = pb_sector_pctile
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of pb_peer_industry_pctile
def f071pbv_f071_price_book_valuation_pb_peer_industry_pctile_z_63d_base_v124_signal(pb_industry_pctile, closeadj):
    base = pb_industry_pctile
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of pb_peer_industry_pctile
def f071pbv_f071_price_book_valuation_pb_peer_industry_pctile_z_126d_base_v125_signal(pb_industry_pctile, closeadj):
    base = pb_industry_pctile
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of pb_peer_industry_pctile
def f071pbv_f071_price_book_valuation_pb_peer_industry_pctile_z_252d_base_v126_signal(pb_industry_pctile, closeadj):
    base = pb_industry_pctile
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of pb_peer_industry_pctile
def f071pbv_f071_price_book_valuation_pb_peer_industry_pctile_z_504d_base_v127_signal(pb_industry_pctile, closeadj):
    base = pb_industry_pctile
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_distmax_252d_base_v128_signal(pb, closeadj):
    base = pb
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_distmax_504d_base_v129_signal(pb, closeadj):
    base = pb
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_distmax_252d_base_v130_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_distmax_504d_base_v131_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_distmax_252d_base_v132_signal(bvps, closeadj):
    base = bvps
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_distmax_504d_base_v133_signal(bvps, closeadj):
    base = bvps
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_distmax_252d_base_v134_signal(tbvps, closeadj):
    base = tbvps
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_distmax_504d_base_v135_signal(tbvps, closeadj):
    base = tbvps
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_distmax_252d_base_v136_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_distmax_504d_base_v137_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of book_yield
def f071pbv_f071_price_book_valuation_book_yield_distmax_252d_base_v138_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of book_yield
def f071pbv_f071_price_book_valuation_book_yield_distmax_504d_base_v139_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_distmax_252d_base_v140_signal(pb, closeadj):
    base = pb.diff(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_distmax_504d_base_v141_signal(pb, closeadj):
    base = pb.diff(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of pb_peer_sector_dist
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_distmax_252d_base_v142_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of pb_peer_sector_dist
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_distmax_504d_base_v143_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of pb_peer_sector_z
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_distmax_252d_base_v144_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = (pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of pb_peer_sector_z
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_distmax_504d_base_v145_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = (pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of pb_peer_industry_dist
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_distmax_252d_base_v146_signal(pb, pb_industry_med, closeadj):
    base = (pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of pb_peer_industry_dist
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_distmax_504d_base_v147_signal(pb, pb_industry_med, closeadj):
    base = (pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of pb_peer_mcap_bucket_dist
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_distmax_252d_base_v148_signal(pb, pb_mcap_med, closeadj):
    base = (pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of pb_peer_mcap_bucket_dist
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_distmax_504d_base_v149_signal(pb, pb_mcap_med, closeadj):
    base = (pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of pb_peer_sector_pctile
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_distmax_252d_base_v150_signal(pb_sector_pctile, closeadj):
    base = pb_sector_pctile
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of pb_peer_sector_pctile
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_distmax_504d_base_v151_signal(pb_sector_pctile, closeadj):
    base = pb_sector_pctile
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of pb_peer_industry_pctile
def f071pbv_f071_price_book_valuation_pb_peer_industry_pctile_distmax_252d_base_v152_signal(pb_industry_pctile, closeadj):
    base = pb_industry_pctile
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of pb_peer_industry_pctile
def f071pbv_f071_price_book_valuation_pb_peer_industry_pctile_distmax_504d_base_v153_signal(pb_industry_pctile, closeadj):
    base = pb_industry_pctile
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_distmed_126d_base_v154_signal(pb, closeadj):
    base = pb
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_distmed_252d_base_v155_signal(pb, closeadj):
    base = pb
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_distmed_504d_base_v156_signal(pb, closeadj):
    base = pb
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_distmed_126d_base_v157_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_distmed_252d_base_v158_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_distmed_504d_base_v159_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_distmed_126d_base_v160_signal(bvps, closeadj):
    base = bvps
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_distmed_252d_base_v161_signal(bvps, closeadj):
    base = bvps
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_distmed_504d_base_v162_signal(bvps, closeadj):
    base = bvps
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_distmed_126d_base_v163_signal(tbvps, closeadj):
    base = tbvps
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_distmed_252d_base_v164_signal(tbvps, closeadj):
    base = tbvps
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_distmed_504d_base_v165_signal(tbvps, closeadj):
    base = tbvps
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_distmed_126d_base_v166_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_distmed_252d_base_v167_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_distmed_504d_base_v168_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of book_yield
def f071pbv_f071_price_book_valuation_book_yield_distmed_126d_base_v169_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of book_yield
def f071pbv_f071_price_book_valuation_book_yield_distmed_252d_base_v170_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of book_yield
def f071pbv_f071_price_book_valuation_book_yield_distmed_504d_base_v171_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_distmed_126d_base_v172_signal(pb, closeadj):
    base = pb.diff(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_distmed_252d_base_v173_signal(pb, closeadj):
    base = pb.diff(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_distmed_504d_base_v174_signal(pb, closeadj):
    base = pb.diff(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of pb_peer_sector_dist
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_distmed_126d_base_v175_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

