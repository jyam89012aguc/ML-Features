import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


def _f006_quick_assets(assetsc, inventory):
    return assetsc - inventory.fillna(0)


def _f006_quick_ratio(assetsc, inventory, liabilitiesc):
    qa = assetsc - inventory.fillna(0)
    return qa / liabilitiesc.replace(0, np.nan).abs()


def _f006_cash_only_quick(cashneq, liabilitiesc):
    return cashneq / liabilitiesc.replace(0, np.nan).abs()


def cg_f006_quick_liquidity_quick_ratio_mean_21d_base_v001_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_quick_ratio_mean_63d_base_v002_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_quick_ratio_mean_126d_base_v003_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_quick_ratio_mean_252d_base_v004_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_quick_ratio_mean_504d_base_v005_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_cash_only_quick_mean_21d_base_v006_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_cash_only_quick_mean_63d_base_v007_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_cash_only_quick_mean_126d_base_v008_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_cash_only_quick_mean_252d_base_v009_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_cash_only_quick_mean_504d_base_v010_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_qa_to_asset_mean_21d_base_v011_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_qa_to_asset_mean_63d_base_v012_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_qa_to_asset_mean_126d_base_v013_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_qa_to_asset_mean_252d_base_v014_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_qa_to_asset_mean_504d_base_v015_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_inv_share_curasset_mean_21d_base_v016_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_inv_share_curasset_mean_63d_base_v017_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_inv_share_curasset_mean_126d_base_v018_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_inv_share_curasset_mean_252d_base_v019_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_inv_share_curasset_mean_504d_base_v020_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_qa_to_mcap_mean_21d_base_v021_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_qa_to_mcap_mean_63d_base_v022_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_qa_to_mcap_mean_126d_base_v023_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_qa_to_mcap_mean_252d_base_v024_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_qa_to_mcap_mean_504d_base_v025_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_liabc_to_qa_mean_21d_base_v026_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_liabc_to_qa_mean_63d_base_v027_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_liabc_to_qa_mean_126d_base_v028_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_liabc_to_qa_mean_252d_base_v029_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_liabc_to_qa_mean_504d_base_v030_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_qa_to_revenue_mean_21d_base_v031_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_qa_to_revenue_mean_63d_base_v032_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_qa_to_revenue_mean_126d_base_v033_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_qa_to_revenue_mean_252d_base_v034_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_qa_to_revenue_mean_504d_base_v035_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_quick_ratio_median_63d_base_v036_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_quick_ratio_median_252d_base_v037_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_quick_ratio_median_504d_base_v038_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_cash_only_quick_median_63d_base_v039_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_cash_only_quick_median_252d_base_v040_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_cash_only_quick_median_504d_base_v041_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_qa_to_asset_median_63d_base_v042_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_qa_to_asset_median_252d_base_v043_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_qa_to_asset_median_504d_base_v044_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_inv_share_curasset_median_63d_base_v045_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_inv_share_curasset_median_252d_base_v046_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_inv_share_curasset_median_504d_base_v047_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_qa_to_mcap_median_63d_base_v048_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_qa_to_mcap_median_252d_base_v049_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_qa_to_mcap_median_504d_base_v050_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_liabc_to_qa_median_63d_base_v051_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_liabc_to_qa_median_252d_base_v052_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_liabc_to_qa_median_504d_base_v053_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_qa_to_revenue_median_63d_base_v054_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_qa_to_revenue_median_252d_base_v055_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_qa_to_revenue_median_504d_base_v056_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_quick_ratio_rmax_252d_base_v057_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_quick_ratio_rmax_504d_base_v058_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_cash_only_quick_rmax_252d_base_v059_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_cash_only_quick_rmax_504d_base_v060_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_qa_to_asset_rmax_252d_base_v061_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_qa_to_asset_rmax_504d_base_v062_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_inv_share_curasset_rmax_252d_base_v063_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_inv_share_curasset_rmax_504d_base_v064_signal(inventory, assetsc, closeadj):
    base = inventory.fillna(0) / assetsc.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_qa_to_mcap_rmax_252d_base_v065_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_qa_to_mcap_rmax_504d_base_v066_signal(assetsc, inventory, marketcap, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_liabc_to_qa_rmax_252d_base_v067_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_liabc_to_qa_rmax_504d_base_v068_signal(liabilitiesc, assetsc, inventory, closeadj):
    base = liabilitiesc / _f006_quick_assets(assetsc, inventory).replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_qa_to_revenue_rmax_252d_base_v069_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_qa_to_revenue_rmax_504d_base_v070_signal(assetsc, inventory, revenue, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / revenue.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_quick_ratio_rmin_252d_base_v071_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_quick_ratio_rmin_504d_base_v072_signal(assetsc, inventory, liabilitiesc, closeadj):
    base = _f006_quick_ratio(assetsc, inventory, liabilitiesc)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_cash_only_quick_rmin_252d_base_v073_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_cash_only_quick_rmin_504d_base_v074_signal(cashneq, liabilitiesc, closeadj):
    base = _f006_cash_only_quick(cashneq, liabilitiesc)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f006_quick_liquidity_qa_to_asset_rmin_252d_base_v075_signal(assetsc, inventory, assets, closeadj):
    base = _f006_quick_assets(assetsc, inventory) / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

