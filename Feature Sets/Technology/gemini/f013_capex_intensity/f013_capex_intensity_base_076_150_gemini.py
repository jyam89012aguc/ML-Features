import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


def _f013_capex_abs(capex):
    return capex.abs()


def _f013_capex_to_rev(capex, revenue):
    return capex.abs() / revenue.abs().replace(0, np.nan)


def _f013_capex_to_ocf(capex, ncfo):
    return capex.abs() / ncfo.abs().replace(0, np.nan)


def cg_f013_capex_intensity_capex_lvl_z_63d_base_v076_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_lvl_z_126d_base_v077_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_lvl_z_252d_base_v078_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_lvl_z_504d_base_v079_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_rev_z_63d_base_v080_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_rev_z_126d_base_v081_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_rev_z_252d_base_v082_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_rev_z_504d_base_v083_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_asset_z_63d_base_v084_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_asset_z_126d_base_v085_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_asset_z_252d_base_v086_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_asset_z_504d_base_v087_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_ocf_z_63d_base_v088_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_ocf_z_126d_base_v089_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_ocf_z_252d_base_v090_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_ocf_z_504d_base_v091_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_mcap_z_63d_base_v092_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_mcap_z_126d_base_v093_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_mcap_z_252d_base_v094_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_mcap_z_504d_base_v095_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_ppne_z_63d_base_v096_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_ppne_z_126d_base_v097_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_ppne_z_252d_base_v098_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_ppne_z_504d_base_v099_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_ppne_to_asset_z_63d_base_v100_signal(ppnenet, assets, closeadj):
    base = ppnenet / assets.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_ppne_to_asset_z_126d_base_v101_signal(ppnenet, assets, closeadj):
    base = ppnenet / assets.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_ppne_to_asset_z_252d_base_v102_signal(ppnenet, assets, closeadj):
    base = ppnenet / assets.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_ppne_to_asset_z_504d_base_v103_signal(ppnenet, assets, closeadj):
    base = ppnenet / assets.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_dep_z_63d_base_v104_signal(capex, depamor, closeadj):
    base = _f013_capex_abs(capex) / depamor.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_dep_z_126d_base_v105_signal(capex, depamor, closeadj):
    base = _f013_capex_abs(capex) / depamor.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_dep_z_252d_base_v106_signal(capex, depamor, closeadj):
    base = _f013_capex_abs(capex) / depamor.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_dep_z_504d_base_v107_signal(capex, depamor, closeadj):
    base = _f013_capex_abs(capex) / depamor.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capint_peer_sector_dist_z_63d_base_v108_signal(capex, revenue, capint_sector_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capint_peer_sector_dist_z_126d_base_v109_signal(capex, revenue, capint_sector_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capint_peer_sector_dist_z_252d_base_v110_signal(capex, revenue, capint_sector_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capint_peer_sector_dist_z_504d_base_v111_signal(capex, revenue, capint_sector_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capint_peer_sector_z_z_63d_base_v112_signal(capex, revenue, capint_sector_med, capint_sector_std, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_std.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capint_peer_sector_z_z_126d_base_v113_signal(capex, revenue, capint_sector_med, capint_sector_std, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_std.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capint_peer_sector_z_z_252d_base_v114_signal(capex, revenue, capint_sector_med, capint_sector_std, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_std.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capint_peer_sector_z_z_504d_base_v115_signal(capex, revenue, capint_sector_med, capint_sector_std, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_std.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capint_peer_industry_dist_z_63d_base_v116_signal(capex, revenue, capint_industry_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_industry_med) / capint_industry_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capint_peer_industry_dist_z_126d_base_v117_signal(capex, revenue, capint_industry_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_industry_med) / capint_industry_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capint_peer_industry_dist_z_252d_base_v118_signal(capex, revenue, capint_industry_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_industry_med) / capint_industry_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capint_peer_industry_dist_z_504d_base_v119_signal(capex, revenue, capint_industry_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_industry_med) / capint_industry_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capint_peer_mcap_bucket_dist_z_63d_base_v120_signal(capex, revenue, capint_mcap_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_mcap_med) / capint_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capint_peer_mcap_bucket_dist_z_126d_base_v121_signal(capex, revenue, capint_mcap_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_mcap_med) / capint_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capint_peer_mcap_bucket_dist_z_252d_base_v122_signal(capex, revenue, capint_mcap_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_mcap_med) / capint_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capint_peer_mcap_bucket_dist_z_504d_base_v123_signal(capex, revenue, capint_mcap_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_mcap_med) / capint_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capint_peer_sector_pctile_z_63d_base_v124_signal(capint_sector_pctile, closeadj):
    base = capint_sector_pctile
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capint_peer_sector_pctile_z_126d_base_v125_signal(capint_sector_pctile, closeadj):
    base = capint_sector_pctile
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capint_peer_sector_pctile_z_252d_base_v126_signal(capint_sector_pctile, closeadj):
    base = capint_sector_pctile
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capint_peer_sector_pctile_z_504d_base_v127_signal(capint_sector_pctile, closeadj):
    base = capint_sector_pctile
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capint_peer_industry_pctile_z_63d_base_v128_signal(capint_industry_pctile, closeadj):
    base = capint_industry_pctile
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capint_peer_industry_pctile_z_126d_base_v129_signal(capint_industry_pctile, closeadj):
    base = capint_industry_pctile
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capint_peer_industry_pctile_z_252d_base_v130_signal(capint_industry_pctile, closeadj):
    base = capint_industry_pctile
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capint_peer_industry_pctile_z_504d_base_v131_signal(capint_industry_pctile, closeadj):
    base = capint_industry_pctile
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_lvl_distmax_252d_base_v132_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_lvl_distmax_504d_base_v133_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_rev_distmax_252d_base_v134_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_rev_distmax_504d_base_v135_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_asset_distmax_252d_base_v136_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_asset_distmax_504d_base_v137_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_ocf_distmax_252d_base_v138_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_ocf_distmax_504d_base_v139_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_mcap_distmax_252d_base_v140_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_mcap_distmax_504d_base_v141_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_ppne_distmax_252d_base_v142_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_ppne_distmax_504d_base_v143_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_ppne_to_asset_distmax_252d_base_v144_signal(ppnenet, assets, closeadj):
    base = ppnenet / assets.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_ppne_to_asset_distmax_504d_base_v145_signal(ppnenet, assets, closeadj):
    base = ppnenet / assets.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_dep_distmax_252d_base_v146_signal(capex, depamor, closeadj):
    base = _f013_capex_abs(capex) / depamor.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_dep_distmax_504d_base_v147_signal(capex, depamor, closeadj):
    base = _f013_capex_abs(capex) / depamor.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capint_peer_sector_dist_distmax_252d_base_v148_signal(capex, revenue, capint_sector_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capint_peer_sector_dist_distmax_504d_base_v149_signal(capex, revenue, capint_sector_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capint_peer_sector_z_distmax_252d_base_v150_signal(capex, revenue, capint_sector_med, capint_sector_std, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_std.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capint_peer_sector_z_distmax_504d_base_v151_signal(capex, revenue, capint_sector_med, capint_sector_std, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_std.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capint_peer_industry_dist_distmax_252d_base_v152_signal(capex, revenue, capint_industry_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_industry_med) / capint_industry_med.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capint_peer_industry_dist_distmax_504d_base_v153_signal(capex, revenue, capint_industry_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_industry_med) / capint_industry_med.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capint_peer_mcap_bucket_dist_distmax_252d_base_v154_signal(capex, revenue, capint_mcap_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_mcap_med) / capint_mcap_med.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capint_peer_mcap_bucket_dist_distmax_504d_base_v155_signal(capex, revenue, capint_mcap_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_mcap_med) / capint_mcap_med.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capint_peer_sector_pctile_distmax_252d_base_v156_signal(capint_sector_pctile, closeadj):
    base = capint_sector_pctile
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capint_peer_sector_pctile_distmax_504d_base_v157_signal(capint_sector_pctile, closeadj):
    base = capint_sector_pctile
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capint_peer_industry_pctile_distmax_252d_base_v158_signal(capint_industry_pctile, closeadj):
    base = capint_industry_pctile
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capint_peer_industry_pctile_distmax_504d_base_v159_signal(capint_industry_pctile, closeadj):
    base = capint_industry_pctile
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_lvl_distmed_126d_base_v160_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_lvl_distmed_252d_base_v161_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_lvl_distmed_504d_base_v162_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_rev_distmed_126d_base_v163_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_rev_distmed_252d_base_v164_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_rev_distmed_504d_base_v165_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_asset_distmed_126d_base_v166_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_asset_distmed_252d_base_v167_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_asset_distmed_504d_base_v168_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_ocf_distmed_126d_base_v169_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_ocf_distmed_252d_base_v170_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_ocf_distmed_504d_base_v171_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_mcap_distmed_126d_base_v172_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_mcap_distmed_252d_base_v173_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_mcap_distmed_504d_base_v174_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f013_capex_intensity_capex_to_ppne_distmed_126d_base_v175_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

