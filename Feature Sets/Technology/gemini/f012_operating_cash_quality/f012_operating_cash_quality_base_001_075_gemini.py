import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


def _f012_ocf_ni_gap(ncfo, netinc):
    return ncfo - netinc.fillna(0)


def _f012_ocf_to_ni(ncfo, netinc):
    return ncfo / netinc.replace(0, np.nan).abs()


def _f012_noncash_share(depamor, sbcomp, opex):
    nc = depamor.fillna(0) + sbcomp.fillna(0)
    return nc / opex.abs().replace(0, np.nan)


def cg_f012_operating_cash_quality_ocf_ni_gap_mean_21d_base_v001_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_ni_gap_mean_63d_base_v002_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_ni_gap_mean_126d_base_v003_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_ni_gap_mean_252d_base_v004_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_ni_gap_mean_504d_base_v005_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_to_ni_mean_21d_base_v006_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_to_ni_mean_63d_base_v007_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_to_ni_mean_126d_base_v008_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_to_ni_mean_252d_base_v009_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_to_ni_mean_504d_base_v010_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_noncash_share_mean_21d_base_v011_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_noncash_share_mean_63d_base_v012_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_noncash_share_mean_126d_base_v013_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_noncash_share_mean_252d_base_v014_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_noncash_share_mean_504d_base_v015_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_depamor_to_ni_mean_21d_base_v016_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_depamor_to_ni_mean_63d_base_v017_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_depamor_to_ni_mean_126d_base_v018_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_depamor_to_ni_mean_252d_base_v019_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_depamor_to_ni_mean_504d_base_v020_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_sbc_to_ni_mean_21d_base_v021_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_sbc_to_ni_mean_63d_base_v022_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_sbc_to_ni_mean_126d_base_v023_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_sbc_to_ni_mean_252d_base_v024_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_sbc_to_ni_mean_504d_base_v025_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_minus_da_sbc_mean_21d_base_v026_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_minus_da_sbc_mean_63d_base_v027_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_minus_da_sbc_mean_126d_base_v028_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_minus_da_sbc_mean_252d_base_v029_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_minus_da_sbc_mean_504d_base_v030_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_gap_to_asset_mean_21d_base_v031_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_gap_to_asset_mean_63d_base_v032_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_gap_to_asset_mean_126d_base_v033_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_gap_to_asset_mean_252d_base_v034_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_gap_to_asset_mean_504d_base_v035_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_ni_gap_median_63d_base_v036_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_ni_gap_median_252d_base_v037_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_ni_gap_median_504d_base_v038_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_to_ni_median_63d_base_v039_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_to_ni_median_252d_base_v040_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_to_ni_median_504d_base_v041_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_noncash_share_median_63d_base_v042_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_noncash_share_median_252d_base_v043_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_noncash_share_median_504d_base_v044_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_depamor_to_ni_median_63d_base_v045_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_depamor_to_ni_median_252d_base_v046_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_depamor_to_ni_median_504d_base_v047_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_sbc_to_ni_median_63d_base_v048_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_sbc_to_ni_median_252d_base_v049_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_sbc_to_ni_median_504d_base_v050_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_minus_da_sbc_median_63d_base_v051_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_minus_da_sbc_median_252d_base_v052_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_minus_da_sbc_median_504d_base_v053_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_gap_to_asset_median_63d_base_v054_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_gap_to_asset_median_252d_base_v055_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_gap_to_asset_median_504d_base_v056_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_ni_gap_rmax_252d_base_v057_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_ni_gap_rmax_504d_base_v058_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_to_ni_rmax_252d_base_v059_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_to_ni_rmax_504d_base_v060_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_noncash_share_rmax_252d_base_v061_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_noncash_share_rmax_504d_base_v062_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_depamor_to_ni_rmax_252d_base_v063_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_depamor_to_ni_rmax_504d_base_v064_signal(depamor, netinc, closeadj):
    base = depamor / netinc.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_sbc_to_ni_rmax_252d_base_v065_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_sbc_to_ni_rmax_504d_base_v066_signal(sbcomp, netinc, closeadj):
    base = sbcomp / netinc.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_minus_da_sbc_rmax_252d_base_v067_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_minus_da_sbc_rmax_504d_base_v068_signal(ncfo, depamor, sbcomp, closeadj):
    base = ncfo - depamor.fillna(0) - sbcomp.fillna(0)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_gap_to_asset_rmax_252d_base_v069_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_gap_to_asset_rmax_504d_base_v070_signal(ncfo, netinc, assets, closeadj):
    base = (ncfo - netinc.fillna(0)) / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_ni_gap_rmin_252d_base_v071_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_ni_gap_rmin_504d_base_v072_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_ni_gap(ncfo, netinc)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_to_ni_rmin_252d_base_v073_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_ocf_to_ni_rmin_504d_base_v074_signal(ncfo, netinc, closeadj):
    base = _f012_ocf_to_ni(ncfo, netinc)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f012_operating_cash_quality_noncash_share_rmin_252d_base_v075_signal(depamor, sbcomp, opex, closeadj):
    base = _f012_noncash_share(depamor, sbcomp, opex)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

