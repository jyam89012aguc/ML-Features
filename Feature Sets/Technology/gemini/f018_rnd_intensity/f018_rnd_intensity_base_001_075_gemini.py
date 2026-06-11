import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


def _f018_rnd_to_rev(rnd, revenue):
    return rnd / revenue.abs().replace(0, np.nan)


def _f018_rnd_to_opex(rnd, opex):
    return rnd / opex.abs().replace(0, np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_mean_21d_base_v001_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_mean_63d_base_v002_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_mean_126d_base_v003_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_mean_252d_base_v004_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_mean_504d_base_v005_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_opex_mean_21d_base_v006_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_opex_mean_63d_base_v007_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_opex_mean_126d_base_v008_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_opex_mean_252d_base_v009_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_opex_mean_504d_base_v010_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_gp_mean_21d_base_v011_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_gp_mean_63d_base_v012_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_gp_mean_126d_base_v013_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_gp_mean_252d_base_v014_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_gp_mean_504d_base_v015_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_cash_balance_mean_21d_base_v016_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_cash_balance_mean_63d_base_v017_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_cash_balance_mean_126d_base_v018_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_cash_balance_mean_252d_base_v019_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_cash_balance_mean_504d_base_v020_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_asset_mean_21d_base_v021_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_asset_mean_63d_base_v022_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_asset_mean_126d_base_v023_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_asset_mean_252d_base_v024_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_asset_mean_504d_base_v025_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_ebit_mean_21d_base_v026_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_ebit_mean_63d_base_v027_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_ebit_mean_126d_base_v028_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_ebit_mean_252d_base_v029_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_ebit_mean_504d_base_v030_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_share_of_loss_mean_21d_base_v031_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_share_of_loss_mean_63d_base_v032_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_share_of_loss_mean_126d_base_v033_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_share_of_loss_mean_252d_base_v034_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_share_of_loss_mean_504d_base_v035_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_mean_21d_base_v036_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_mean_63d_base_v037_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_mean_126d_base_v038_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_mean_252d_base_v039_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_mean_504d_base_v040_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_sector_z_mean_21d_base_v041_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_sector_z_mean_63d_base_v042_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_sector_z_mean_126d_base_v043_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_sector_z_mean_252d_base_v044_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_sector_z_mean_504d_base_v045_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_mean_21d_base_v046_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_mean_63d_base_v047_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_mean_126d_base_v048_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_mean_252d_base_v049_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_mean_504d_base_v050_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_mean_21d_base_v051_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_mean_63d_base_v052_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_mean_126d_base_v053_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_mean_252d_base_v054_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_mean_504d_base_v055_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_mean_21d_base_v056_signal(rnd_to_rev_sector_pctile, closeadj):
    base = rnd_to_rev_sector_pctile
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_mean_63d_base_v057_signal(rnd_to_rev_sector_pctile, closeadj):
    base = rnd_to_rev_sector_pctile
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_mean_126d_base_v058_signal(rnd_to_rev_sector_pctile, closeadj):
    base = rnd_to_rev_sector_pctile
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_mean_252d_base_v059_signal(rnd_to_rev_sector_pctile, closeadj):
    base = rnd_to_rev_sector_pctile
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_mean_504d_base_v060_signal(rnd_to_rev_sector_pctile, closeadj):
    base = rnd_to_rev_sector_pctile
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_industry_pctile_mean_21d_base_v061_signal(rnd_to_rev_industry_pctile, closeadj):
    base = rnd_to_rev_industry_pctile
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_industry_pctile_mean_63d_base_v062_signal(rnd_to_rev_industry_pctile, closeadj):
    base = rnd_to_rev_industry_pctile
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_industry_pctile_mean_126d_base_v063_signal(rnd_to_rev_industry_pctile, closeadj):
    base = rnd_to_rev_industry_pctile
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_industry_pctile_mean_252d_base_v064_signal(rnd_to_rev_industry_pctile, closeadj):
    base = rnd_to_rev_industry_pctile
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_industry_pctile_mean_504d_base_v065_signal(rnd_to_rev_industry_pctile, closeadj):
    base = rnd_to_rev_industry_pctile
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_median_63d_base_v066_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_median_252d_base_v067_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_median_504d_base_v068_signal(rnd, revenue, closeadj):
    base = _f018_rnd_to_rev(rnd, revenue)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_opex_median_63d_base_v069_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_opex_median_252d_base_v070_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_opex_median_504d_base_v071_signal(rnd, opex, closeadj):
    base = _f018_rnd_to_opex(rnd, opex)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_gp_median_63d_base_v072_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_gp_median_252d_base_v073_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_gp_median_504d_base_v074_signal(rnd, gp, closeadj):
    base = rnd / gp.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_cash_balance_median_63d_base_v075_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_cash_balance_median_252d_base_v076_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_cash_balance_median_504d_base_v077_signal(rnd, cashneq, closeadj):
    base = rnd / cashneq.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_asset_median_63d_base_v078_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_asset_median_252d_base_v079_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_asset_median_504d_base_v080_signal(rnd, assets, closeadj):
    base = rnd / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_ebit_median_63d_base_v081_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_ebit_median_252d_base_v082_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_ebit_median_504d_base_v083_signal(rnd, ebit, closeadj):
    base = rnd / ebit.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_share_of_loss_median_63d_base_v084_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_share_of_loss_median_252d_base_v085_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_share_of_loss_median_504d_base_v086_signal(rnd, netinc, closeadj):
    base = rnd / (-netinc).clip(lower=0).replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_median_63d_base_v087_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_median_252d_base_v088_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_sector_dist_median_504d_base_v089_signal(rnd, revenue, rnd_to_rev_sector_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_med.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_sector_z_median_63d_base_v090_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_sector_z_median_252d_base_v091_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_sector_z_median_504d_base_v092_signal(rnd, revenue, rnd_to_rev_sector_med, rnd_to_rev_sector_std, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_sector_med) / rnd_to_rev_sector_std.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_median_63d_base_v093_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_median_252d_base_v094_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_industry_dist_median_504d_base_v095_signal(rnd, revenue, rnd_to_rev_industry_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_industry_med) / rnd_to_rev_industry_med.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_median_63d_base_v096_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_median_252d_base_v097_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_mcap_bucket_dist_median_504d_base_v098_signal(rnd, revenue, rnd_to_rev_mcap_med, closeadj):
    base = (_f018_rnd_to_rev(rnd, revenue) - rnd_to_rev_mcap_med) / rnd_to_rev_mcap_med.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_median_63d_base_v099_signal(rnd_to_rev_sector_pctile, closeadj):
    base = rnd_to_rev_sector_pctile
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f018_rnd_intensity_rnd_to_rev_peer_sector_pctile_median_252d_base_v100_signal(rnd_to_rev_sector_pctile, closeadj):
    base = rnd_to_rev_sector_pctile
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

