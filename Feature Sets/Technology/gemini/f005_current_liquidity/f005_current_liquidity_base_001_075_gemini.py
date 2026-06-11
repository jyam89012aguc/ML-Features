import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


def _f005_current_ratio(assetsc, liabilitiesc):
    return assetsc / liabilitiesc.replace(0, np.nan).abs()


def _f005_qac(assetsc, inventory):
    return (assetsc - inventory.fillna(0))


def _f005_cash_quick(cashneq, investmentsc, liabilitiesc):
    return (cashneq.fillna(0) + investmentsc.fillna(0)) / liabilitiesc.replace(0, np.nan).abs()


def cg_f005_current_liquidity_curratio_mean_21d_base_v001_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_curratio_mean_63d_base_v002_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_curratio_mean_126d_base_v003_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_curratio_mean_252d_base_v004_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_curratio_mean_504d_base_v005_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_qac_ratio_mean_21d_base_v006_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_qac_ratio_mean_63d_base_v007_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_qac_ratio_mean_126d_base_v008_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_qac_ratio_mean_252d_base_v009_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_qac_ratio_mean_504d_base_v010_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_cashquick_mean_21d_base_v011_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_cashquick_mean_63d_base_v012_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_cashquick_mean_126d_base_v013_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_cashquick_mean_252d_base_v014_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_cashquick_mean_504d_base_v015_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_asset_mean_21d_base_v016_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_asset_mean_63d_base_v017_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_asset_mean_126d_base_v018_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_asset_mean_252d_base_v019_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_asset_mean_504d_base_v020_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_mcap_mean_21d_base_v021_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_mcap_mean_63d_base_v022_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_mcap_mean_126d_base_v023_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_mcap_mean_252d_base_v024_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_mcap_mean_504d_base_v025_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_liabc_to_asset_mean_21d_base_v026_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_liabc_to_asset_mean_63d_base_v027_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_liabc_to_asset_mean_126d_base_v028_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_liabc_to_asset_mean_252d_base_v029_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_liabc_to_asset_mean_504d_base_v030_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_curratio_minus_1_mean_21d_base_v031_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_curratio_minus_1_mean_63d_base_v032_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_curratio_minus_1_mean_126d_base_v033_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_curratio_minus_1_mean_252d_base_v034_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_curratio_minus_1_mean_504d_base_v035_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_curratio_median_63d_base_v036_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_curratio_median_252d_base_v037_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_curratio_median_504d_base_v038_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_qac_ratio_median_63d_base_v039_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_qac_ratio_median_252d_base_v040_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_qac_ratio_median_504d_base_v041_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_cashquick_median_63d_base_v042_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_cashquick_median_252d_base_v043_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_cashquick_median_504d_base_v044_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_asset_median_63d_base_v045_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_asset_median_252d_base_v046_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_asset_median_504d_base_v047_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_mcap_median_63d_base_v048_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_mcap_median_252d_base_v049_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_mcap_median_504d_base_v050_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_liabc_to_asset_median_63d_base_v051_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_liabc_to_asset_median_252d_base_v052_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_liabc_to_asset_median_504d_base_v053_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_curratio_minus_1_median_63d_base_v054_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_curratio_minus_1_median_252d_base_v055_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_curratio_minus_1_median_504d_base_v056_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_curratio_rmax_252d_base_v057_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_curratio_rmax_504d_base_v058_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_qac_ratio_rmax_252d_base_v059_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_qac_ratio_rmax_504d_base_v060_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_cashquick_rmax_252d_base_v061_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_cashquick_rmax_504d_base_v062_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_asset_rmax_252d_base_v063_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_asset_rmax_504d_base_v064_signal(assetsc, liabilitiesc, assets, closeadj):
    base = (assetsc - liabilitiesc) / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_mcap_rmax_252d_base_v065_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_netwc_to_mcap_rmax_504d_base_v066_signal(assetsc, liabilitiesc, marketcap, closeadj):
    base = (assetsc - liabilitiesc) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_liabc_to_asset_rmax_252d_base_v067_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_liabc_to_asset_rmax_504d_base_v068_signal(liabilitiesc, assets, closeadj):
    base = liabilitiesc / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_curratio_minus_1_rmax_252d_base_v069_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_curratio_minus_1_rmax_504d_base_v070_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc) - 1.0
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_curratio_rmin_252d_base_v071_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_curratio_rmin_504d_base_v072_signal(assetsc, liabilitiesc, closeadj):
    base = _f005_current_ratio(assetsc, liabilitiesc)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_qac_ratio_rmin_252d_base_v073_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_qac_ratio_rmin_504d_base_v074_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f005_qac(assetsc, inventory) / liabilitiesc.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f005_current_liquidity_cashquick_rmin_252d_base_v075_signal(cashneq, investmentsc, liabilitiesc, closeadj):
    base = _f005_cash_quick(cashneq, investmentsc, liabilitiesc)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

