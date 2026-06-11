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


# 21d mean of pb_lvl scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_lvl_mean_21d_base_v001_signal(pb, closeadj):
    base = pb
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of pb_lvl scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_lvl_mean_63d_base_v002_signal(pb, closeadj):
    base = pb
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of pb_lvl scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_lvl_mean_126d_base_v003_signal(pb, closeadj):
    base = pb
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of pb_lvl scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_lvl_mean_252d_base_v004_signal(pb, closeadj):
    base = pb
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of pb_lvl scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_lvl_mean_504d_base_v005_signal(pb, closeadj):
    base = pb
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of pb_calc scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_calc_mean_21d_base_v006_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of pb_calc scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_calc_mean_63d_base_v007_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of pb_calc scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_calc_mean_126d_base_v008_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of pb_calc scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_calc_mean_252d_base_v009_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of pb_calc scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_calc_mean_504d_base_v010_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of bvps_lvl scaled by closeadj
def f071pbv_f071_price_book_valuation_bvps_lvl_mean_21d_base_v011_signal(bvps, closeadj):
    base = bvps
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of bvps_lvl scaled by closeadj
def f071pbv_f071_price_book_valuation_bvps_lvl_mean_63d_base_v012_signal(bvps, closeadj):
    base = bvps
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of bvps_lvl scaled by closeadj
def f071pbv_f071_price_book_valuation_bvps_lvl_mean_126d_base_v013_signal(bvps, closeadj):
    base = bvps
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of bvps_lvl scaled by closeadj
def f071pbv_f071_price_book_valuation_bvps_lvl_mean_252d_base_v014_signal(bvps, closeadj):
    base = bvps
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of bvps_lvl scaled by closeadj
def f071pbv_f071_price_book_valuation_bvps_lvl_mean_504d_base_v015_signal(bvps, closeadj):
    base = bvps
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of tbvps_lvl scaled by closeadj
def f071pbv_f071_price_book_valuation_tbvps_lvl_mean_21d_base_v016_signal(tbvps, closeadj):
    base = tbvps
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of tbvps_lvl scaled by closeadj
def f071pbv_f071_price_book_valuation_tbvps_lvl_mean_63d_base_v017_signal(tbvps, closeadj):
    base = tbvps
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of tbvps_lvl scaled by closeadj
def f071pbv_f071_price_book_valuation_tbvps_lvl_mean_126d_base_v018_signal(tbvps, closeadj):
    base = tbvps
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of tbvps_lvl scaled by closeadj
def f071pbv_f071_price_book_valuation_tbvps_lvl_mean_252d_base_v019_signal(tbvps, closeadj):
    base = tbvps
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of tbvps_lvl scaled by closeadj
def f071pbv_f071_price_book_valuation_tbvps_lvl_mean_504d_base_v020_signal(tbvps, closeadj):
    base = tbvps
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of p_to_tbv scaled by closeadj
def f071pbv_f071_price_book_valuation_p_to_tbv_mean_21d_base_v021_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of p_to_tbv scaled by closeadj
def f071pbv_f071_price_book_valuation_p_to_tbv_mean_63d_base_v022_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of p_to_tbv scaled by closeadj
def f071pbv_f071_price_book_valuation_p_to_tbv_mean_126d_base_v023_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of p_to_tbv scaled by closeadj
def f071pbv_f071_price_book_valuation_p_to_tbv_mean_252d_base_v024_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of p_to_tbv scaled by closeadj
def f071pbv_f071_price_book_valuation_p_to_tbv_mean_504d_base_v025_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of book_yield scaled by closeadj
def f071pbv_f071_price_book_valuation_book_yield_mean_21d_base_v026_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of book_yield scaled by closeadj
def f071pbv_f071_price_book_valuation_book_yield_mean_63d_base_v027_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of book_yield scaled by closeadj
def f071pbv_f071_price_book_valuation_book_yield_mean_126d_base_v028_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of book_yield scaled by closeadj
def f071pbv_f071_price_book_valuation_book_yield_mean_252d_base_v029_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of book_yield scaled by closeadj
def f071pbv_f071_price_book_valuation_book_yield_mean_504d_base_v030_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of pb_yoy scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_yoy_mean_21d_base_v031_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of pb_yoy scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_yoy_mean_63d_base_v032_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of pb_yoy scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_yoy_mean_126d_base_v033_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of pb_yoy scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_yoy_mean_252d_base_v034_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of pb_yoy scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_yoy_mean_504d_base_v035_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of pb_peer_sector_dist scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_mean_21d_base_v036_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of pb_peer_sector_dist scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_mean_63d_base_v037_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of pb_peer_sector_dist scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_mean_126d_base_v038_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of pb_peer_sector_dist scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_mean_252d_base_v039_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of pb_peer_sector_dist scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_mean_504d_base_v040_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of pb_peer_sector_z scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_mean_21d_base_v041_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = (pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of pb_peer_sector_z scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_mean_63d_base_v042_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = (pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of pb_peer_sector_z scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_mean_126d_base_v043_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = (pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of pb_peer_sector_z scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_mean_252d_base_v044_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = (pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of pb_peer_sector_z scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_mean_504d_base_v045_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = (pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of pb_peer_industry_dist scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_mean_21d_base_v046_signal(pb, pb_industry_med, closeadj):
    base = (pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of pb_peer_industry_dist scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_mean_63d_base_v047_signal(pb, pb_industry_med, closeadj):
    base = (pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of pb_peer_industry_dist scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_mean_126d_base_v048_signal(pb, pb_industry_med, closeadj):
    base = (pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of pb_peer_industry_dist scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_mean_252d_base_v049_signal(pb, pb_industry_med, closeadj):
    base = (pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of pb_peer_industry_dist scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_mean_504d_base_v050_signal(pb, pb_industry_med, closeadj):
    base = (pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of pb_peer_mcap_bucket_dist scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_mean_21d_base_v051_signal(pb, pb_mcap_med, closeadj):
    base = (pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of pb_peer_mcap_bucket_dist scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_mean_63d_base_v052_signal(pb, pb_mcap_med, closeadj):
    base = (pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of pb_peer_mcap_bucket_dist scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_mean_126d_base_v053_signal(pb, pb_mcap_med, closeadj):
    base = (pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of pb_peer_mcap_bucket_dist scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_mean_252d_base_v054_signal(pb, pb_mcap_med, closeadj):
    base = (pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of pb_peer_mcap_bucket_dist scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_mean_504d_base_v055_signal(pb, pb_mcap_med, closeadj):
    base = (pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of pb_peer_sector_pctile scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_mean_21d_base_v056_signal(pb_sector_pctile, closeadj):
    base = pb_sector_pctile
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of pb_peer_sector_pctile scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_mean_63d_base_v057_signal(pb_sector_pctile, closeadj):
    base = pb_sector_pctile
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of pb_peer_sector_pctile scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_mean_126d_base_v058_signal(pb_sector_pctile, closeadj):
    base = pb_sector_pctile
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of pb_peer_sector_pctile scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_mean_252d_base_v059_signal(pb_sector_pctile, closeadj):
    base = pb_sector_pctile
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of pb_peer_sector_pctile scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_mean_504d_base_v060_signal(pb_sector_pctile, closeadj):
    base = pb_sector_pctile
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of pb_peer_industry_pctile scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_peer_industry_pctile_mean_21d_base_v061_signal(pb_industry_pctile, closeadj):
    base = pb_industry_pctile
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of pb_peer_industry_pctile scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_peer_industry_pctile_mean_63d_base_v062_signal(pb_industry_pctile, closeadj):
    base = pb_industry_pctile
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of pb_peer_industry_pctile scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_peer_industry_pctile_mean_126d_base_v063_signal(pb_industry_pctile, closeadj):
    base = pb_industry_pctile
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of pb_peer_industry_pctile scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_peer_industry_pctile_mean_252d_base_v064_signal(pb_industry_pctile, closeadj):
    base = pb_industry_pctile
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of pb_peer_industry_pctile scaled by closeadj
def f071pbv_f071_price_book_valuation_pb_peer_industry_pctile_mean_504d_base_v065_signal(pb_industry_pctile, closeadj):
    base = pb_industry_pctile
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_median_63d_base_v066_signal(pb, closeadj):
    base = pb
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_median_252d_base_v067_signal(pb, closeadj):
    base = pb
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of pb_lvl
def f071pbv_f071_price_book_valuation_pb_lvl_median_504d_base_v068_signal(pb, closeadj):
    base = pb
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_median_63d_base_v069_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_median_252d_base_v070_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of pb_calc
def f071pbv_f071_price_book_valuation_pb_calc_median_504d_base_v071_signal(marketcap, equity, closeadj):
    base = _f071_pb(marketcap, equity)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_median_63d_base_v072_signal(bvps, closeadj):
    base = bvps
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_median_252d_base_v073_signal(bvps, closeadj):
    base = bvps
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of bvps_lvl
def f071pbv_f071_price_book_valuation_bvps_lvl_median_504d_base_v074_signal(bvps, closeadj):
    base = bvps
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_median_63d_base_v075_signal(tbvps, closeadj):
    base = tbvps
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_median_252d_base_v076_signal(tbvps, closeadj):
    base = tbvps
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of tbvps_lvl
def f071pbv_f071_price_book_valuation_tbvps_lvl_median_504d_base_v077_signal(tbvps, closeadj):
    base = tbvps
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_median_63d_base_v078_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_median_252d_base_v079_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of p_to_tbv
def f071pbv_f071_price_book_valuation_p_to_tbv_median_504d_base_v080_signal(close, tbvps, closeadj):
    base = close / tbvps.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of book_yield
def f071pbv_f071_price_book_valuation_book_yield_median_63d_base_v081_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of book_yield
def f071pbv_f071_price_book_valuation_book_yield_median_252d_base_v082_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of book_yield
def f071pbv_f071_price_book_valuation_book_yield_median_504d_base_v083_signal(equity, marketcap, closeadj):
    base = equity / marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_median_63d_base_v084_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_median_252d_base_v085_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of pb_yoy
def f071pbv_f071_price_book_valuation_pb_yoy_median_504d_base_v086_signal(pb, closeadj):
    base = pb.diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of pb_peer_sector_dist
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_median_63d_base_v087_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of pb_peer_sector_dist
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_median_252d_base_v088_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of pb_peer_sector_dist
def f071pbv_f071_price_book_valuation_pb_peer_sector_dist_median_504d_base_v089_signal(pb, pb_sector_med, closeadj):
    base = (pb - pb_sector_med) / pb_sector_med.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of pb_peer_sector_z
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_median_63d_base_v090_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = (pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of pb_peer_sector_z
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_median_252d_base_v091_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = (pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of pb_peer_sector_z
def f071pbv_f071_price_book_valuation_pb_peer_sector_z_median_504d_base_v092_signal(pb, pb_sector_med, pb_sector_std, closeadj):
    base = (pb - pb_sector_med) / pb_sector_std.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of pb_peer_industry_dist
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_median_63d_base_v093_signal(pb, pb_industry_med, closeadj):
    base = (pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of pb_peer_industry_dist
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_median_252d_base_v094_signal(pb, pb_industry_med, closeadj):
    base = (pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of pb_peer_industry_dist
def f071pbv_f071_price_book_valuation_pb_peer_industry_dist_median_504d_base_v095_signal(pb, pb_industry_med, closeadj):
    base = (pb - pb_industry_med) / pb_industry_med.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of pb_peer_mcap_bucket_dist
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_median_63d_base_v096_signal(pb, pb_mcap_med, closeadj):
    base = (pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of pb_peer_mcap_bucket_dist
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_median_252d_base_v097_signal(pb, pb_mcap_med, closeadj):
    base = (pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of pb_peer_mcap_bucket_dist
def f071pbv_f071_price_book_valuation_pb_peer_mcap_bucket_dist_median_504d_base_v098_signal(pb, pb_mcap_med, closeadj):
    base = (pb - pb_mcap_med) / pb_mcap_med.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of pb_peer_sector_pctile
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_median_63d_base_v099_signal(pb_sector_pctile, closeadj):
    base = pb_sector_pctile
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of pb_peer_sector_pctile
def f071pbv_f071_price_book_valuation_pb_peer_sector_pctile_median_252d_base_v100_signal(pb_sector_pctile, closeadj):
    base = pb_sector_pctile
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

