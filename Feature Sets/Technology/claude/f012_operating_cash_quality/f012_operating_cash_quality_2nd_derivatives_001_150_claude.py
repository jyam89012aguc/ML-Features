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


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _accel(s, w):
    return s.diff(periods=w).diff(periods=w)


# ===== folder domain primitives =====
def _f012_ocf_ni_gap(ncfo, netinc):
    return ncfo - netinc.fillna(0)


def _f012_ocf_to_ni(ncfo, netinc):
    return ncfo / netinc.replace(0, np.nan).abs()


def _f012_noncash_share(depamor, sbcomp, opex):
    nc = depamor.fillna(0) + sbcomp.fillna(0)
    return nc / opex.abs().replace(0, np.nan)


# 21d slope of ocf_ni_gap
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_slope_21d_2d_v001_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ocf_ni_gap
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_slope_63d_2d_v002_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ocf_ni_gap
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_slope_126d_2d_v003_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ocf_ni_gap
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_slope_252d_2d_v004_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ocf_ni_gap
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_slope_504d_2d_v005_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ocf_to_ni
def f012ocq_f012_operating_cash_quality_ocf_to_ni_slope_21d_2d_v006_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ocf_to_ni
def f012ocq_f012_operating_cash_quality_ocf_to_ni_slope_63d_2d_v007_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ocf_to_ni
def f012ocq_f012_operating_cash_quality_ocf_to_ni_slope_126d_2d_v008_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ocf_to_ni
def f012ocq_f012_operating_cash_quality_ocf_to_ni_slope_252d_2d_v009_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ocf_to_ni
def f012ocq_f012_operating_cash_quality_ocf_to_ni_slope_504d_2d_v010_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of noncash_share
def f012ocq_f012_operating_cash_quality_noncash_share_slope_21d_2d_v011_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of noncash_share
def f012ocq_f012_operating_cash_quality_noncash_share_slope_63d_2d_v012_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of noncash_share
def f012ocq_f012_operating_cash_quality_noncash_share_slope_126d_2d_v013_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of noncash_share
def f012ocq_f012_operating_cash_quality_noncash_share_slope_252d_2d_v014_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of noncash_share
def f012ocq_f012_operating_cash_quality_noncash_share_slope_504d_2d_v015_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of depamor_to_ni
def f012ocq_f012_operating_cash_quality_depamor_to_ni_slope_21d_2d_v016_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of depamor_to_ni
def f012ocq_f012_operating_cash_quality_depamor_to_ni_slope_63d_2d_v017_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of depamor_to_ni
def f012ocq_f012_operating_cash_quality_depamor_to_ni_slope_126d_2d_v018_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of depamor_to_ni
def f012ocq_f012_operating_cash_quality_depamor_to_ni_slope_252d_2d_v019_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of depamor_to_ni
def f012ocq_f012_operating_cash_quality_depamor_to_ni_slope_504d_2d_v020_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sbc_to_ni
def f012ocq_f012_operating_cash_quality_sbc_to_ni_slope_21d_2d_v021_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sbc_to_ni
def f012ocq_f012_operating_cash_quality_sbc_to_ni_slope_63d_2d_v022_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sbc_to_ni
def f012ocq_f012_operating_cash_quality_sbc_to_ni_slope_126d_2d_v023_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sbc_to_ni
def f012ocq_f012_operating_cash_quality_sbc_to_ni_slope_252d_2d_v024_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sbc_to_ni
def f012ocq_f012_operating_cash_quality_sbc_to_ni_slope_504d_2d_v025_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ocf_minus_da_sbc
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_slope_21d_2d_v026_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ocf_minus_da_sbc
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_slope_63d_2d_v027_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ocf_minus_da_sbc
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_slope_126d_2d_v028_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ocf_minus_da_sbc
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_slope_252d_2d_v029_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ocf_minus_da_sbc
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_slope_504d_2d_v030_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ocf_gap_to_asset
def f012ocq_f012_operating_cash_quality_ocf_gap_to_asset_slope_21d_2d_v031_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ocf_gap_to_asset
def f012ocq_f012_operating_cash_quality_ocf_gap_to_asset_slope_63d_2d_v032_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ocf_gap_to_asset
def f012ocq_f012_operating_cash_quality_ocf_gap_to_asset_slope_126d_2d_v033_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ocf_gap_to_asset
def f012ocq_f012_operating_cash_quality_ocf_gap_to_asset_slope_252d_2d_v034_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ocf_gap_to_asset
def f012ocq_f012_operating_cash_quality_ocf_gap_to_asset_slope_504d_2d_v035_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ocf_ni_gap
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_sm21_sl21_2d_v036_signal(ncfo, netinc, closeadj):
    base = _mean(_f012_ocf_ni_gap(ncfo, netinc), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ocf_ni_gap
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_sm63_sl21_2d_v037_signal(ncfo, netinc, closeadj):
    base = _mean(_f012_ocf_ni_gap(ncfo, netinc), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ocf_ni_gap
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_sm63_sl63_2d_v038_signal(ncfo, netinc, closeadj):
    base = _mean(_f012_ocf_ni_gap(ncfo, netinc), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ocf_ni_gap
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_sm252_sl63_2d_v039_signal(ncfo, netinc, closeadj):
    base = _mean(_f012_ocf_ni_gap(ncfo, netinc), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ocf_ni_gap
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_sm252_sl126_2d_v040_signal(ncfo, netinc, closeadj):
    base = _mean(_f012_ocf_ni_gap(ncfo, netinc), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ocf_to_ni
def f012ocq_f012_operating_cash_quality_ocf_to_ni_sm21_sl21_2d_v041_signal(ncfo, netinc, closeadj):
    base = _mean(_f012_ocf_to_ni(ncfo, netinc), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ocf_to_ni
def f012ocq_f012_operating_cash_quality_ocf_to_ni_sm63_sl21_2d_v042_signal(ncfo, netinc, closeadj):
    base = _mean(_f012_ocf_to_ni(ncfo, netinc), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ocf_to_ni
def f012ocq_f012_operating_cash_quality_ocf_to_ni_sm63_sl63_2d_v043_signal(ncfo, netinc, closeadj):
    base = _mean(_f012_ocf_to_ni(ncfo, netinc), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ocf_to_ni
def f012ocq_f012_operating_cash_quality_ocf_to_ni_sm252_sl63_2d_v044_signal(ncfo, netinc, closeadj):
    base = _mean(_f012_ocf_to_ni(ncfo, netinc), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ocf_to_ni
def f012ocq_f012_operating_cash_quality_ocf_to_ni_sm252_sl126_2d_v045_signal(ncfo, netinc, closeadj):
    base = _mean(_f012_ocf_to_ni(ncfo, netinc), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of noncash_share
def f012ocq_f012_operating_cash_quality_noncash_share_sm21_sl21_2d_v046_signal(depamor, sbcomp, opex, closeadj):
    base = _mean(_f012_noncash_share(depamor, sbcomp, opex), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of noncash_share
def f012ocq_f012_operating_cash_quality_noncash_share_sm63_sl21_2d_v047_signal(depamor, sbcomp, opex, closeadj):
    base = _mean(_f012_noncash_share(depamor, sbcomp, opex), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of noncash_share
def f012ocq_f012_operating_cash_quality_noncash_share_sm63_sl63_2d_v048_signal(depamor, sbcomp, opex, closeadj):
    base = _mean(_f012_noncash_share(depamor, sbcomp, opex), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of noncash_share
def f012ocq_f012_operating_cash_quality_noncash_share_sm252_sl63_2d_v049_signal(depamor, sbcomp, opex, closeadj):
    base = _mean(_f012_noncash_share(depamor, sbcomp, opex), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of noncash_share
def f012ocq_f012_operating_cash_quality_noncash_share_sm252_sl126_2d_v050_signal(depamor, sbcomp, opex, closeadj):
    base = _mean(_f012_noncash_share(depamor, sbcomp, opex), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of depamor_to_ni
def f012ocq_f012_operating_cash_quality_depamor_to_ni_sm21_sl21_2d_v051_signal(depamor, netinc, closeadj):
    base = _mean(depamor / netinc.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of depamor_to_ni
def f012ocq_f012_operating_cash_quality_depamor_to_ni_sm63_sl21_2d_v052_signal(depamor, netinc, closeadj):
    base = _mean(depamor / netinc.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of depamor_to_ni
def f012ocq_f012_operating_cash_quality_depamor_to_ni_sm63_sl63_2d_v053_signal(depamor, netinc, closeadj):
    base = _mean(depamor / netinc.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of depamor_to_ni
def f012ocq_f012_operating_cash_quality_depamor_to_ni_sm252_sl63_2d_v054_signal(depamor, netinc, closeadj):
    base = _mean(depamor / netinc.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of depamor_to_ni
def f012ocq_f012_operating_cash_quality_depamor_to_ni_sm252_sl126_2d_v055_signal(depamor, netinc, closeadj):
    base = _mean(depamor / netinc.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sbc_to_ni
def f012ocq_f012_operating_cash_quality_sbc_to_ni_sm21_sl21_2d_v056_signal(sbcomp, netinc, closeadj):
    base = _mean(sbcomp / netinc.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sbc_to_ni
def f012ocq_f012_operating_cash_quality_sbc_to_ni_sm63_sl21_2d_v057_signal(sbcomp, netinc, closeadj):
    base = _mean(sbcomp / netinc.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sbc_to_ni
def f012ocq_f012_operating_cash_quality_sbc_to_ni_sm63_sl63_2d_v058_signal(sbcomp, netinc, closeadj):
    base = _mean(sbcomp / netinc.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sbc_to_ni
def f012ocq_f012_operating_cash_quality_sbc_to_ni_sm252_sl63_2d_v059_signal(sbcomp, netinc, closeadj):
    base = _mean(sbcomp / netinc.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sbc_to_ni
def f012ocq_f012_operating_cash_quality_sbc_to_ni_sm252_sl126_2d_v060_signal(sbcomp, netinc, closeadj):
    base = _mean(sbcomp / netinc.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ocf_minus_da_sbc
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_sm21_sl21_2d_v061_signal(ncfo, depamor, sbcomp, closeadj):
    base = _mean(ncfo - depamor.fillna(0) - sbcomp.fillna(0), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ocf_minus_da_sbc
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_sm63_sl21_2d_v062_signal(ncfo, depamor, sbcomp, closeadj):
    base = _mean(ncfo - depamor.fillna(0) - sbcomp.fillna(0), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ocf_minus_da_sbc
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_sm63_sl63_2d_v063_signal(ncfo, depamor, sbcomp, closeadj):
    base = _mean(ncfo - depamor.fillna(0) - sbcomp.fillna(0), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ocf_minus_da_sbc
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_sm252_sl63_2d_v064_signal(ncfo, depamor, sbcomp, closeadj):
    base = _mean(ncfo - depamor.fillna(0) - sbcomp.fillna(0), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ocf_minus_da_sbc
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_sm252_sl126_2d_v065_signal(ncfo, depamor, sbcomp, closeadj):
    base = _mean(ncfo - depamor.fillna(0) - sbcomp.fillna(0), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ocf_gap_to_asset
def f012ocq_f012_operating_cash_quality_ocf_gap_to_asset_sm21_sl21_2d_v066_signal(ncfo, netinc, assets, closeadj):
    base = _mean((ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ocf_gap_to_asset
def f012ocq_f012_operating_cash_quality_ocf_gap_to_asset_sm63_sl21_2d_v067_signal(ncfo, netinc, assets, closeadj):
    base = _mean((ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ocf_gap_to_asset
def f012ocq_f012_operating_cash_quality_ocf_gap_to_asset_sm63_sl63_2d_v068_signal(ncfo, netinc, assets, closeadj):
    base = _mean((ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ocf_gap_to_asset
def f012ocq_f012_operating_cash_quality_ocf_gap_to_asset_sm252_sl63_2d_v069_signal(ncfo, netinc, assets, closeadj):
    base = _mean((ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ocf_gap_to_asset
def f012ocq_f012_operating_cash_quality_ocf_gap_to_asset_sm252_sl126_2d_v070_signal(ncfo, netinc, assets, closeadj):
    base = _mean((ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ocf_ni_gap
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_pctslope_21d_2d_v071_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ocf_ni_gap
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_pctslope_63d_2d_v072_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ocf_ni_gap
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_pctslope_252d_2d_v073_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ocf_to_ni
def f012ocq_f012_operating_cash_quality_ocf_to_ni_pctslope_21d_2d_v074_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ocf_to_ni
def f012ocq_f012_operating_cash_quality_ocf_to_ni_pctslope_63d_2d_v075_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ocf_to_ni
def f012ocq_f012_operating_cash_quality_ocf_to_ni_pctslope_252d_2d_v076_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of noncash_share
def f012ocq_f012_operating_cash_quality_noncash_share_pctslope_21d_2d_v077_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of noncash_share
def f012ocq_f012_operating_cash_quality_noncash_share_pctslope_63d_2d_v078_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of noncash_share
def f012ocq_f012_operating_cash_quality_noncash_share_pctslope_252d_2d_v079_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of depamor_to_ni
def f012ocq_f012_operating_cash_quality_depamor_to_ni_pctslope_21d_2d_v080_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of depamor_to_ni
def f012ocq_f012_operating_cash_quality_depamor_to_ni_pctslope_63d_2d_v081_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of depamor_to_ni
def f012ocq_f012_operating_cash_quality_depamor_to_ni_pctslope_252d_2d_v082_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of sbc_to_ni
def f012ocq_f012_operating_cash_quality_sbc_to_ni_pctslope_21d_2d_v083_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of sbc_to_ni
def f012ocq_f012_operating_cash_quality_sbc_to_ni_pctslope_63d_2d_v084_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of sbc_to_ni
def f012ocq_f012_operating_cash_quality_sbc_to_ni_pctslope_252d_2d_v085_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ocf_minus_da_sbc
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_pctslope_21d_2d_v086_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ocf_minus_da_sbc
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_pctslope_63d_2d_v087_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ocf_minus_da_sbc
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_pctslope_252d_2d_v088_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ocf_gap_to_asset
def f012ocq_f012_operating_cash_quality_ocf_gap_to_asset_pctslope_21d_2d_v089_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ocf_gap_to_asset
def f012ocq_f012_operating_cash_quality_ocf_gap_to_asset_pctslope_63d_2d_v090_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ocf_gap_to_asset
def f012ocq_f012_operating_cash_quality_ocf_gap_to_asset_pctslope_252d_2d_v091_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ocf_ni_gap
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_sgnslope_21d_2d_v092_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ocf_ni_gap
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_sgnslope_63d_2d_v093_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ocf_ni_gap
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_sgnslope_252d_2d_v094_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ocf_to_ni
def f012ocq_f012_operating_cash_quality_ocf_to_ni_sgnslope_21d_2d_v095_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ocf_to_ni
def f012ocq_f012_operating_cash_quality_ocf_to_ni_sgnslope_63d_2d_v096_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ocf_to_ni
def f012ocq_f012_operating_cash_quality_ocf_to_ni_sgnslope_252d_2d_v097_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of noncash_share
def f012ocq_f012_operating_cash_quality_noncash_share_sgnslope_21d_2d_v098_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of noncash_share
def f012ocq_f012_operating_cash_quality_noncash_share_sgnslope_63d_2d_v099_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of noncash_share
def f012ocq_f012_operating_cash_quality_noncash_share_sgnslope_252d_2d_v100_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of depamor_to_ni
def f012ocq_f012_operating_cash_quality_depamor_to_ni_sgnslope_21d_2d_v101_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of depamor_to_ni
def f012ocq_f012_operating_cash_quality_depamor_to_ni_sgnslope_63d_2d_v102_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of depamor_to_ni
def f012ocq_f012_operating_cash_quality_depamor_to_ni_sgnslope_252d_2d_v103_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of sbc_to_ni
def f012ocq_f012_operating_cash_quality_sbc_to_ni_sgnslope_21d_2d_v104_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of sbc_to_ni
def f012ocq_f012_operating_cash_quality_sbc_to_ni_sgnslope_63d_2d_v105_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of sbc_to_ni
def f012ocq_f012_operating_cash_quality_sbc_to_ni_sgnslope_252d_2d_v106_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ocf_minus_da_sbc
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_sgnslope_21d_2d_v107_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ocf_minus_da_sbc
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_sgnslope_63d_2d_v108_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ocf_minus_da_sbc
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_sgnslope_252d_2d_v109_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ocf_gap_to_asset
def f012ocq_f012_operating_cash_quality_ocf_gap_to_asset_sgnslope_21d_2d_v110_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ocf_gap_to_asset
def f012ocq_f012_operating_cash_quality_ocf_gap_to_asset_sgnslope_63d_2d_v111_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ocf_gap_to_asset
def f012ocq_f012_operating_cash_quality_ocf_gap_to_asset_sgnslope_252d_2d_v112_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ocf_ni_gap
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_logmagslope_21d_2d_v113_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ocf_ni_gap
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_logmagslope_63d_2d_v114_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ocf_ni_gap
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_logmagslope_252d_2d_v115_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ocf_to_ni
def f012ocq_f012_operating_cash_quality_ocf_to_ni_logmagslope_21d_2d_v116_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ocf_to_ni
def f012ocq_f012_operating_cash_quality_ocf_to_ni_logmagslope_63d_2d_v117_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ocf_to_ni
def f012ocq_f012_operating_cash_quality_ocf_to_ni_logmagslope_252d_2d_v118_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of noncash_share
def f012ocq_f012_operating_cash_quality_noncash_share_logmagslope_21d_2d_v119_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of noncash_share
def f012ocq_f012_operating_cash_quality_noncash_share_logmagslope_63d_2d_v120_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of noncash_share
def f012ocq_f012_operating_cash_quality_noncash_share_logmagslope_252d_2d_v121_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of depamor_to_ni
def f012ocq_f012_operating_cash_quality_depamor_to_ni_logmagslope_21d_2d_v122_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of depamor_to_ni
def f012ocq_f012_operating_cash_quality_depamor_to_ni_logmagslope_63d_2d_v123_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of depamor_to_ni
def f012ocq_f012_operating_cash_quality_depamor_to_ni_logmagslope_252d_2d_v124_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of sbc_to_ni
def f012ocq_f012_operating_cash_quality_sbc_to_ni_logmagslope_21d_2d_v125_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of sbc_to_ni
def f012ocq_f012_operating_cash_quality_sbc_to_ni_logmagslope_63d_2d_v126_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of sbc_to_ni
def f012ocq_f012_operating_cash_quality_sbc_to_ni_logmagslope_252d_2d_v127_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ocf_minus_da_sbc
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_logmagslope_21d_2d_v128_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ocf_minus_da_sbc
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_logmagslope_63d_2d_v129_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ocf_minus_da_sbc
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_logmagslope_252d_2d_v130_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ocf_gap_to_asset
def f012ocq_f012_operating_cash_quality_ocf_gap_to_asset_logmagslope_21d_2d_v131_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ocf_gap_to_asset
def f012ocq_f012_operating_cash_quality_ocf_gap_to_asset_logmagslope_63d_2d_v132_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ocf_gap_to_asset
def f012ocq_f012_operating_cash_quality_ocf_gap_to_asset_logmagslope_252d_2d_v133_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ocf_ni_gap|
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_logslope_63d_2d_v134_signal(ncfo, netinc, closeadj):
    base = np.log((_f012_ocf_ni_gap(ncfo, netinc)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ocf_ni_gap|
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_logslope_252d_2d_v135_signal(ncfo, netinc, closeadj):
    base = np.log((_f012_ocf_ni_gap(ncfo, netinc)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ocf_to_ni|
def f012ocq_f012_operating_cash_quality_ocf_to_ni_logslope_63d_2d_v136_signal(ncfo, netinc, closeadj):
    base = np.log((_f012_ocf_to_ni(ncfo, netinc)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ocf_to_ni|
def f012ocq_f012_operating_cash_quality_ocf_to_ni_logslope_252d_2d_v137_signal(ncfo, netinc, closeadj):
    base = np.log((_f012_ocf_to_ni(ncfo, netinc)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|noncash_share|
def f012ocq_f012_operating_cash_quality_noncash_share_logslope_63d_2d_v138_signal(depamor, sbcomp, opex, closeadj):
    base = np.log((_f012_noncash_share(depamor, sbcomp, opex)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|noncash_share|
def f012ocq_f012_operating_cash_quality_noncash_share_logslope_252d_2d_v139_signal(depamor, sbcomp, opex, closeadj):
    base = np.log((_f012_noncash_share(depamor, sbcomp, opex)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|depamor_to_ni|
def f012ocq_f012_operating_cash_quality_depamor_to_ni_logslope_63d_2d_v140_signal(depamor, netinc, closeadj):
    base = np.log((depamor / netinc.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|depamor_to_ni|
def f012ocq_f012_operating_cash_quality_depamor_to_ni_logslope_252d_2d_v141_signal(depamor, netinc, closeadj):
    base = np.log((depamor / netinc.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|sbc_to_ni|
def f012ocq_f012_operating_cash_quality_sbc_to_ni_logslope_63d_2d_v142_signal(sbcomp, netinc, closeadj):
    base = np.log((sbcomp / netinc.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|sbc_to_ni|
def f012ocq_f012_operating_cash_quality_sbc_to_ni_logslope_252d_2d_v143_signal(sbcomp, netinc, closeadj):
    base = np.log((sbcomp / netinc.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ocf_minus_da_sbc|
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_logslope_63d_2d_v144_signal(ncfo, depamor, sbcomp, closeadj):
    base = np.log((ncfo - depamor.fillna(0) - sbcomp.fillna(0)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ocf_minus_da_sbc|
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_logslope_252d_2d_v145_signal(ncfo, depamor, sbcomp, closeadj):
    base = np.log((ncfo - depamor.fillna(0) - sbcomp.fillna(0)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ocf_gap_to_asset|
def f012ocq_f012_operating_cash_quality_ocf_gap_to_asset_logslope_63d_2d_v146_signal(ncfo, netinc, assets, closeadj):
    base = np.log(((ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ocf_gap_to_asset|
def f012ocq_f012_operating_cash_quality_ocf_gap_to_asset_logslope_252d_2d_v147_signal(ncfo, netinc, assets, closeadj):
    base = np.log(((ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

