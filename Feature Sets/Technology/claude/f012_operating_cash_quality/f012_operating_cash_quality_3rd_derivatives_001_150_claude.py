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


# 21d acceleration of ocf_ni_gap
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_accel_21d_3d_v001_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_ni_gap
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_accel_63d_3d_v002_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ocf_ni_gap
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_accel_126d_3d_v003_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_ni_gap
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_accel_252d_3d_v004_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ocf_to_ni
def f012ocq_f012_operating_cash_quality_ocf_to_ni_accel_21d_3d_v005_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_to_ni
def f012ocq_f012_operating_cash_quality_ocf_to_ni_accel_63d_3d_v006_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ocf_to_ni
def f012ocq_f012_operating_cash_quality_ocf_to_ni_accel_126d_3d_v007_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_to_ni
def f012ocq_f012_operating_cash_quality_ocf_to_ni_accel_252d_3d_v008_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of noncash_share
def f012ocq_f012_operating_cash_quality_noncash_share_accel_21d_3d_v009_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of noncash_share
def f012ocq_f012_operating_cash_quality_noncash_share_accel_63d_3d_v010_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of noncash_share
def f012ocq_f012_operating_cash_quality_noncash_share_accel_126d_3d_v011_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of noncash_share
def f012ocq_f012_operating_cash_quality_noncash_share_accel_252d_3d_v012_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of depamor_to_ni
def f012ocq_f012_operating_cash_quality_depamor_to_ni_accel_21d_3d_v013_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of depamor_to_ni
def f012ocq_f012_operating_cash_quality_depamor_to_ni_accel_63d_3d_v014_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of depamor_to_ni
def f012ocq_f012_operating_cash_quality_depamor_to_ni_accel_126d_3d_v015_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of depamor_to_ni
def f012ocq_f012_operating_cash_quality_depamor_to_ni_accel_252d_3d_v016_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sbc_to_ni
def f012ocq_f012_operating_cash_quality_sbc_to_ni_accel_21d_3d_v017_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sbc_to_ni
def f012ocq_f012_operating_cash_quality_sbc_to_ni_accel_63d_3d_v018_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sbc_to_ni
def f012ocq_f012_operating_cash_quality_sbc_to_ni_accel_126d_3d_v019_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sbc_to_ni
def f012ocq_f012_operating_cash_quality_sbc_to_ni_accel_252d_3d_v020_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ocf_minus_da_sbc
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_accel_21d_3d_v021_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_minus_da_sbc
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_accel_63d_3d_v022_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ocf_minus_da_sbc
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_accel_126d_3d_v023_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_minus_da_sbc
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_accel_252d_3d_v024_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ocf_gap_to_asset
def f012ocq_f012_operating_cash_quality_ocf_gap_to_asset_accel_21d_3d_v025_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_gap_to_asset
def f012ocq_f012_operating_cash_quality_ocf_gap_to_asset_accel_63d_3d_v026_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ocf_gap_to_asset
def f012ocq_f012_operating_cash_quality_ocf_gap_to_asset_accel_126d_3d_v027_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_gap_to_asset
def f012ocq_f012_operating_cash_quality_ocf_gap_to_asset_accel_252d_3d_v028_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ocf_ni_gap
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_slopez_21d_z126_3d_v029_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ocf_ni_gap
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_slopez_63d_z252_3d_v030_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ocf_ni_gap
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_slopez_126d_z252_3d_v031_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ocf_ni_gap
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_slopez_252d_z504_3d_v032_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ocf_to_ni
def f012ocq_f012_operating_cash_quality_ocf_to_ni_slopez_21d_z126_3d_v033_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ocf_to_ni
def f012ocq_f012_operating_cash_quality_ocf_to_ni_slopez_63d_z252_3d_v034_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ocf_to_ni
def f012ocq_f012_operating_cash_quality_ocf_to_ni_slopez_126d_z252_3d_v035_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ocf_to_ni
def f012ocq_f012_operating_cash_quality_ocf_to_ni_slopez_252d_z504_3d_v036_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of noncash_share
def f012ocq_f012_operating_cash_quality_noncash_share_slopez_21d_z126_3d_v037_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of noncash_share
def f012ocq_f012_operating_cash_quality_noncash_share_slopez_63d_z252_3d_v038_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of noncash_share
def f012ocq_f012_operating_cash_quality_noncash_share_slopez_126d_z252_3d_v039_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of noncash_share
def f012ocq_f012_operating_cash_quality_noncash_share_slopez_252d_z504_3d_v040_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of depamor_to_ni
def f012ocq_f012_operating_cash_quality_depamor_to_ni_slopez_21d_z126_3d_v041_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of depamor_to_ni
def f012ocq_f012_operating_cash_quality_depamor_to_ni_slopez_63d_z252_3d_v042_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of depamor_to_ni
def f012ocq_f012_operating_cash_quality_depamor_to_ni_slopez_126d_z252_3d_v043_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of depamor_to_ni
def f012ocq_f012_operating_cash_quality_depamor_to_ni_slopez_252d_z504_3d_v044_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sbc_to_ni
def f012ocq_f012_operating_cash_quality_sbc_to_ni_slopez_21d_z126_3d_v045_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sbc_to_ni
def f012ocq_f012_operating_cash_quality_sbc_to_ni_slopez_63d_z252_3d_v046_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sbc_to_ni
def f012ocq_f012_operating_cash_quality_sbc_to_ni_slopez_126d_z252_3d_v047_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sbc_to_ni
def f012ocq_f012_operating_cash_quality_sbc_to_ni_slopez_252d_z504_3d_v048_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ocf_minus_da_sbc
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_slopez_21d_z126_3d_v049_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ocf_minus_da_sbc
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_slopez_63d_z252_3d_v050_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ocf_minus_da_sbc
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_slopez_126d_z252_3d_v051_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ocf_minus_da_sbc
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_slopez_252d_z504_3d_v052_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ocf_gap_to_asset
def f012ocq_f012_operating_cash_quality_ocf_gap_to_asset_slopez_21d_z126_3d_v053_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ocf_gap_to_asset
def f012ocq_f012_operating_cash_quality_ocf_gap_to_asset_slopez_63d_z252_3d_v054_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ocf_gap_to_asset
def f012ocq_f012_operating_cash_quality_ocf_gap_to_asset_slopez_126d_z252_3d_v055_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ocf_gap_to_asset
def f012ocq_f012_operating_cash_quality_ocf_gap_to_asset_slopez_252d_z504_3d_v056_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ocf_ni_gap
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_jerk_21d_3d_v057_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ocf_ni_gap
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_jerk_63d_3d_v058_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ocf_ni_gap
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_jerk_126d_3d_v059_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ocf_to_ni
def f012ocq_f012_operating_cash_quality_ocf_to_ni_jerk_21d_3d_v060_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ocf_to_ni
def f012ocq_f012_operating_cash_quality_ocf_to_ni_jerk_63d_3d_v061_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ocf_to_ni
def f012ocq_f012_operating_cash_quality_ocf_to_ni_jerk_126d_3d_v062_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of noncash_share
def f012ocq_f012_operating_cash_quality_noncash_share_jerk_21d_3d_v063_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of noncash_share
def f012ocq_f012_operating_cash_quality_noncash_share_jerk_63d_3d_v064_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of noncash_share
def f012ocq_f012_operating_cash_quality_noncash_share_jerk_126d_3d_v065_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of depamor_to_ni
def f012ocq_f012_operating_cash_quality_depamor_to_ni_jerk_21d_3d_v066_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of depamor_to_ni
def f012ocq_f012_operating_cash_quality_depamor_to_ni_jerk_63d_3d_v067_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of depamor_to_ni
def f012ocq_f012_operating_cash_quality_depamor_to_ni_jerk_126d_3d_v068_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sbc_to_ni
def f012ocq_f012_operating_cash_quality_sbc_to_ni_jerk_21d_3d_v069_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sbc_to_ni
def f012ocq_f012_operating_cash_quality_sbc_to_ni_jerk_63d_3d_v070_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sbc_to_ni
def f012ocq_f012_operating_cash_quality_sbc_to_ni_jerk_126d_3d_v071_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ocf_minus_da_sbc
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_jerk_21d_3d_v072_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ocf_minus_da_sbc
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_jerk_63d_3d_v073_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ocf_minus_da_sbc
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_jerk_126d_3d_v074_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ocf_gap_to_asset
def f012ocq_f012_operating_cash_quality_ocf_gap_to_asset_jerk_21d_3d_v075_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ocf_gap_to_asset
def f012ocq_f012_operating_cash_quality_ocf_gap_to_asset_jerk_63d_3d_v076_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ocf_gap_to_asset
def f012ocq_f012_operating_cash_quality_ocf_gap_to_asset_jerk_126d_3d_v077_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ocf_ni_gap smoothed over 252d
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_smoothaccel_63d_sm252_3d_v078_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ocf_ni_gap smoothed over 504d
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_smoothaccel_252d_sm504_3d_v079_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ocf_to_ni smoothed over 252d
def f012ocq_f012_operating_cash_quality_ocf_to_ni_smoothaccel_63d_sm252_3d_v080_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ocf_to_ni smoothed over 504d
def f012ocq_f012_operating_cash_quality_ocf_to_ni_smoothaccel_252d_sm504_3d_v081_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of noncash_share smoothed over 252d
def f012ocq_f012_operating_cash_quality_noncash_share_smoothaccel_63d_sm252_3d_v082_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of noncash_share smoothed over 504d
def f012ocq_f012_operating_cash_quality_noncash_share_smoothaccel_252d_sm504_3d_v083_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of depamor_to_ni smoothed over 252d
def f012ocq_f012_operating_cash_quality_depamor_to_ni_smoothaccel_63d_sm252_3d_v084_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of depamor_to_ni smoothed over 504d
def f012ocq_f012_operating_cash_quality_depamor_to_ni_smoothaccel_252d_sm504_3d_v085_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of sbc_to_ni smoothed over 252d
def f012ocq_f012_operating_cash_quality_sbc_to_ni_smoothaccel_63d_sm252_3d_v086_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of sbc_to_ni smoothed over 504d
def f012ocq_f012_operating_cash_quality_sbc_to_ni_smoothaccel_252d_sm504_3d_v087_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ocf_minus_da_sbc smoothed over 252d
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_smoothaccel_63d_sm252_3d_v088_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ocf_minus_da_sbc smoothed over 504d
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_smoothaccel_252d_sm504_3d_v089_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ocf_gap_to_asset smoothed over 252d
def f012ocq_f012_operating_cash_quality_ocf_gap_to_asset_smoothaccel_63d_sm252_3d_v090_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ocf_gap_to_asset smoothed over 504d
def f012ocq_f012_operating_cash_quality_ocf_gap_to_asset_smoothaccel_252d_sm504_3d_v091_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ocf_ni_gap
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_accelz_21d_z252_3d_v092_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ocf_ni_gap
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_accelz_63d_z504_3d_v093_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ocf_to_ni
def f012ocq_f012_operating_cash_quality_ocf_to_ni_accelz_21d_z252_3d_v094_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ocf_to_ni
def f012ocq_f012_operating_cash_quality_ocf_to_ni_accelz_63d_z504_3d_v095_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of noncash_share
def f012ocq_f012_operating_cash_quality_noncash_share_accelz_21d_z252_3d_v096_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of noncash_share
def f012ocq_f012_operating_cash_quality_noncash_share_accelz_63d_z504_3d_v097_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of depamor_to_ni
def f012ocq_f012_operating_cash_quality_depamor_to_ni_accelz_21d_z252_3d_v098_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of depamor_to_ni
def f012ocq_f012_operating_cash_quality_depamor_to_ni_accelz_63d_z504_3d_v099_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of sbc_to_ni
def f012ocq_f012_operating_cash_quality_sbc_to_ni_accelz_21d_z252_3d_v100_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of sbc_to_ni
def f012ocq_f012_operating_cash_quality_sbc_to_ni_accelz_63d_z504_3d_v101_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ocf_minus_da_sbc
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_accelz_21d_z252_3d_v102_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ocf_minus_da_sbc
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_accelz_63d_z504_3d_v103_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ocf_gap_to_asset
def f012ocq_f012_operating_cash_quality_ocf_gap_to_asset_accelz_21d_z252_3d_v104_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ocf_gap_to_asset
def f012ocq_f012_operating_cash_quality_ocf_gap_to_asset_accelz_63d_z504_3d_v105_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ocf_ni_gap (raw count, no price scaling)
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_signflip_63d_3d_v106_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ocf_ni_gap (raw count, no price scaling)
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_signflip_252d_3d_v107_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ocf_to_ni (raw count, no price scaling)
def f012ocq_f012_operating_cash_quality_ocf_to_ni_signflip_63d_3d_v108_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ocf_to_ni (raw count, no price scaling)
def f012ocq_f012_operating_cash_quality_ocf_to_ni_signflip_252d_3d_v109_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in noncash_share (raw count, no price scaling)
def f012ocq_f012_operating_cash_quality_noncash_share_signflip_63d_3d_v110_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in noncash_share (raw count, no price scaling)
def f012ocq_f012_operating_cash_quality_noncash_share_signflip_252d_3d_v111_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in depamor_to_ni (raw count, no price scaling)
def f012ocq_f012_operating_cash_quality_depamor_to_ni_signflip_63d_3d_v112_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in depamor_to_ni (raw count, no price scaling)
def f012ocq_f012_operating_cash_quality_depamor_to_ni_signflip_252d_3d_v113_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in sbc_to_ni (raw count, no price scaling)
def f012ocq_f012_operating_cash_quality_sbc_to_ni_signflip_63d_3d_v114_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in sbc_to_ni (raw count, no price scaling)
def f012ocq_f012_operating_cash_quality_sbc_to_ni_signflip_252d_3d_v115_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ocf_minus_da_sbc (raw count, no price scaling)
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_signflip_63d_3d_v116_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ocf_minus_da_sbc (raw count, no price scaling)
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_signflip_252d_3d_v117_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ocf_gap_to_asset (raw count, no price scaling)
def f012ocq_f012_operating_cash_quality_ocf_gap_to_asset_signflip_63d_3d_v118_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ocf_gap_to_asset (raw count, no price scaling)
def f012ocq_f012_operating_cash_quality_ocf_gap_to_asset_signflip_252d_3d_v119_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_ni_gap normalized by 252d range
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_rngaccel_63d_r252_3d_v120_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_ni_gap normalized by 504d range
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_rngaccel_252d_r504_3d_v121_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_to_ni normalized by 252d range
def f012ocq_f012_operating_cash_quality_ocf_to_ni_rngaccel_63d_r252_3d_v122_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_to_ni normalized by 504d range
def f012ocq_f012_operating_cash_quality_ocf_to_ni_rngaccel_252d_r504_3d_v123_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of noncash_share normalized by 252d range
def f012ocq_f012_operating_cash_quality_noncash_share_rngaccel_63d_r252_3d_v124_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of noncash_share normalized by 504d range
def f012ocq_f012_operating_cash_quality_noncash_share_rngaccel_252d_r504_3d_v125_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of depamor_to_ni normalized by 252d range
def f012ocq_f012_operating_cash_quality_depamor_to_ni_rngaccel_63d_r252_3d_v126_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of depamor_to_ni normalized by 504d range
def f012ocq_f012_operating_cash_quality_depamor_to_ni_rngaccel_252d_r504_3d_v127_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sbc_to_ni normalized by 252d range
def f012ocq_f012_operating_cash_quality_sbc_to_ni_rngaccel_63d_r252_3d_v128_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sbc_to_ni normalized by 504d range
def f012ocq_f012_operating_cash_quality_sbc_to_ni_rngaccel_252d_r504_3d_v129_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_minus_da_sbc normalized by 252d range
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_rngaccel_63d_r252_3d_v130_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_minus_da_sbc normalized by 504d range
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_rngaccel_252d_r504_3d_v131_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_gap_to_asset normalized by 252d range
def f012ocq_f012_operating_cash_quality_ocf_gap_to_asset_rngaccel_63d_r252_3d_v132_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_gap_to_asset normalized by 504d range
def f012ocq_f012_operating_cash_quality_ocf_gap_to_asset_rngaccel_252d_r504_3d_v133_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ocf_ni_gap
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_cumslope_21d_3d_v134_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ocf_ni_gap
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_cumslope_63d_3d_v135_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ocf_ni_gap
def f012ocq_f012_operating_cash_quality_ocf_ni_gap_cumslope_252d_3d_v136_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ocf_to_ni
def f012ocq_f012_operating_cash_quality_ocf_to_ni_cumslope_21d_3d_v137_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ocf_to_ni
def f012ocq_f012_operating_cash_quality_ocf_to_ni_cumslope_63d_3d_v138_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ocf_to_ni
def f012ocq_f012_operating_cash_quality_ocf_to_ni_cumslope_252d_3d_v139_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of noncash_share
def f012ocq_f012_operating_cash_quality_noncash_share_cumslope_21d_3d_v140_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of noncash_share
def f012ocq_f012_operating_cash_quality_noncash_share_cumslope_63d_3d_v141_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of noncash_share
def f012ocq_f012_operating_cash_quality_noncash_share_cumslope_252d_3d_v142_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of depamor_to_ni
def f012ocq_f012_operating_cash_quality_depamor_to_ni_cumslope_21d_3d_v143_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of depamor_to_ni
def f012ocq_f012_operating_cash_quality_depamor_to_ni_cumslope_63d_3d_v144_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of depamor_to_ni
def f012ocq_f012_operating_cash_quality_depamor_to_ni_cumslope_252d_3d_v145_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of sbc_to_ni
def f012ocq_f012_operating_cash_quality_sbc_to_ni_cumslope_21d_3d_v146_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of sbc_to_ni
def f012ocq_f012_operating_cash_quality_sbc_to_ni_cumslope_63d_3d_v147_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of sbc_to_ni
def f012ocq_f012_operating_cash_quality_sbc_to_ni_cumslope_252d_3d_v148_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ocf_minus_da_sbc
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_cumslope_21d_3d_v149_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ocf_minus_da_sbc
def f012ocq_f012_operating_cash_quality_ocf_minus_da_sbc_cumslope_63d_3d_v150_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

