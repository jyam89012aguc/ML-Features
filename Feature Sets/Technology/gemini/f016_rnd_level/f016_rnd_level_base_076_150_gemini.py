import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


def _f016_rnd_log(rnd):
    return np.log(rnd.abs().replace(0, np.nan))


def _f016_rnd_per_share(rnd, sharesbas):
    return rnd / sharesbas.replace(0, np.nan).abs()


def cg_f016_rnd_level_rnd_lvl_z_63d_base_v076_signal(rnd, closeadj):
    base = rnd
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_lvl_z_126d_base_v077_signal(rnd, closeadj):
    base = rnd
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_lvl_z_252d_base_v078_signal(rnd, closeadj):
    base = rnd
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_lvl_z_504d_base_v079_signal(rnd, closeadj):
    base = rnd
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_log_rnd_z_63d_base_v080_signal(rnd, closeadj):
    base = _f016_rnd_log(rnd)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_log_rnd_z_126d_base_v081_signal(rnd, closeadj):
    base = _f016_rnd_log(rnd)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_log_rnd_z_252d_base_v082_signal(rnd, closeadj):
    base = _f016_rnd_log(rnd)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_log_rnd_z_504d_base_v083_signal(rnd, closeadj):
    base = _f016_rnd_log(rnd)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_per_share_z_63d_base_v084_signal(rnd, sharesbas, closeadj):
    base = _f016_rnd_per_share(rnd, sharesbas)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_per_share_z_126d_base_v085_signal(rnd, sharesbas, closeadj):
    base = _f016_rnd_per_share(rnd, sharesbas)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_per_share_z_252d_base_v086_signal(rnd, sharesbas, closeadj):
    base = _f016_rnd_per_share(rnd, sharesbas)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_per_share_z_504d_base_v087_signal(rnd, sharesbas, closeadj):
    base = _f016_rnd_per_share(rnd, sharesbas)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_per_dilshare_z_63d_base_v088_signal(rnd, shareswadil, closeadj):
    base = rnd / shareswadil.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_per_dilshare_z_126d_base_v089_signal(rnd, shareswadil, closeadj):
    base = rnd / shareswadil.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_per_dilshare_z_252d_base_v090_signal(rnd, shareswadil, closeadj):
    base = rnd / shareswadil.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_per_dilshare_z_504d_base_v091_signal(rnd, shareswadil, closeadj):
    base = rnd / shareswadil.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_log_expand_z_63d_base_v092_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)).expanding(21).mean()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_log_expand_z_126d_base_v093_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)).expanding(21).mean()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_log_expand_z_252d_base_v094_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)).expanding(21).mean()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_log_expand_z_504d_base_v095_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)).expanding(21).mean()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_log_minus_5y_z_63d_base_v096_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(1260).abs().replace(0, np.nan))
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_log_minus_5y_z_126d_base_v097_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(1260).abs().replace(0, np.nan))
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_log_minus_5y_z_252d_base_v098_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(1260).abs().replace(0, np.nan))
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_log_minus_5y_z_504d_base_v099_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(1260).abs().replace(0, np.nan))
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_yoy_log_z_63d_base_v100_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_yoy_log_z_126d_base_v101_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_yoy_log_z_252d_base_v102_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_yoy_log_z_504d_base_v103_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_peer_sector_dist_z_63d_base_v104_signal(rnd, rnd_sector_med, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_peer_sector_dist_z_126d_base_v105_signal(rnd, rnd_sector_med, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_peer_sector_dist_z_252d_base_v106_signal(rnd, rnd_sector_med, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_peer_sector_dist_z_504d_base_v107_signal(rnd, rnd_sector_med, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_peer_sector_z_z_63d_base_v108_signal(rnd, rnd_sector_med, rnd_sector_std, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_std.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_peer_sector_z_z_126d_base_v109_signal(rnd, rnd_sector_med, rnd_sector_std, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_std.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_peer_sector_z_z_252d_base_v110_signal(rnd, rnd_sector_med, rnd_sector_std, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_std.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_peer_sector_z_z_504d_base_v111_signal(rnd, rnd_sector_med, rnd_sector_std, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_std.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_peer_industry_dist_z_63d_base_v112_signal(rnd, rnd_industry_med, closeadj):
    base = (rnd - rnd_industry_med) / rnd_industry_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_peer_industry_dist_z_126d_base_v113_signal(rnd, rnd_industry_med, closeadj):
    base = (rnd - rnd_industry_med) / rnd_industry_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_peer_industry_dist_z_252d_base_v114_signal(rnd, rnd_industry_med, closeadj):
    base = (rnd - rnd_industry_med) / rnd_industry_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_peer_industry_dist_z_504d_base_v115_signal(rnd, rnd_industry_med, closeadj):
    base = (rnd - rnd_industry_med) / rnd_industry_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_peer_mcap_bucket_dist_z_63d_base_v116_signal(rnd, rnd_mcap_med, closeadj):
    base = (rnd - rnd_mcap_med) / rnd_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_peer_mcap_bucket_dist_z_126d_base_v117_signal(rnd, rnd_mcap_med, closeadj):
    base = (rnd - rnd_mcap_med) / rnd_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_peer_mcap_bucket_dist_z_252d_base_v118_signal(rnd, rnd_mcap_med, closeadj):
    base = (rnd - rnd_mcap_med) / rnd_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_peer_mcap_bucket_dist_z_504d_base_v119_signal(rnd, rnd_mcap_med, closeadj):
    base = (rnd - rnd_mcap_med) / rnd_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_peer_sector_pctile_z_63d_base_v120_signal(rnd_sector_pctile, closeadj):
    base = rnd_sector_pctile
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_peer_sector_pctile_z_126d_base_v121_signal(rnd_sector_pctile, closeadj):
    base = rnd_sector_pctile
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_peer_sector_pctile_z_252d_base_v122_signal(rnd_sector_pctile, closeadj):
    base = rnd_sector_pctile
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_peer_sector_pctile_z_504d_base_v123_signal(rnd_sector_pctile, closeadj):
    base = rnd_sector_pctile
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_peer_industry_pctile_z_63d_base_v124_signal(rnd_industry_pctile, closeadj):
    base = rnd_industry_pctile
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_peer_industry_pctile_z_126d_base_v125_signal(rnd_industry_pctile, closeadj):
    base = rnd_industry_pctile
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_peer_industry_pctile_z_252d_base_v126_signal(rnd_industry_pctile, closeadj):
    base = rnd_industry_pctile
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_peer_industry_pctile_z_504d_base_v127_signal(rnd_industry_pctile, closeadj):
    base = rnd_industry_pctile
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_lvl_distmax_252d_base_v128_signal(rnd, closeadj):
    base = rnd
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_lvl_distmax_504d_base_v129_signal(rnd, closeadj):
    base = rnd
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_log_rnd_distmax_252d_base_v130_signal(rnd, closeadj):
    base = _f016_rnd_log(rnd)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_log_rnd_distmax_504d_base_v131_signal(rnd, closeadj):
    base = _f016_rnd_log(rnd)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_per_share_distmax_252d_base_v132_signal(rnd, sharesbas, closeadj):
    base = _f016_rnd_per_share(rnd, sharesbas)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_per_share_distmax_504d_base_v133_signal(rnd, sharesbas, closeadj):
    base = _f016_rnd_per_share(rnd, sharesbas)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_per_dilshare_distmax_252d_base_v134_signal(rnd, shareswadil, closeadj):
    base = rnd / shareswadil.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_per_dilshare_distmax_504d_base_v135_signal(rnd, shareswadil, closeadj):
    base = rnd / shareswadil.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_log_expand_distmax_252d_base_v136_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)).expanding(21).mean()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_log_expand_distmax_504d_base_v137_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)).expanding(21).mean()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_log_minus_5y_distmax_252d_base_v138_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(1260).abs().replace(0, np.nan))
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_log_minus_5y_distmax_504d_base_v139_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(1260).abs().replace(0, np.nan))
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_yoy_log_distmax_252d_base_v140_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_yoy_log_distmax_504d_base_v141_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_peer_sector_dist_distmax_252d_base_v142_signal(rnd, rnd_sector_med, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_med.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_peer_sector_dist_distmax_504d_base_v143_signal(rnd, rnd_sector_med, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_med.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_peer_sector_z_distmax_252d_base_v144_signal(rnd, rnd_sector_med, rnd_sector_std, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_std.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_peer_sector_z_distmax_504d_base_v145_signal(rnd, rnd_sector_med, rnd_sector_std, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_std.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_peer_industry_dist_distmax_252d_base_v146_signal(rnd, rnd_industry_med, closeadj):
    base = (rnd - rnd_industry_med) / rnd_industry_med.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_peer_industry_dist_distmax_504d_base_v147_signal(rnd, rnd_industry_med, closeadj):
    base = (rnd - rnd_industry_med) / rnd_industry_med.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_peer_mcap_bucket_dist_distmax_252d_base_v148_signal(rnd, rnd_mcap_med, closeadj):
    base = (rnd - rnd_mcap_med) / rnd_mcap_med.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_peer_mcap_bucket_dist_distmax_504d_base_v149_signal(rnd, rnd_mcap_med, closeadj):
    base = (rnd - rnd_mcap_med) / rnd_mcap_med.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_peer_sector_pctile_distmax_252d_base_v150_signal(rnd_sector_pctile, closeadj):
    base = rnd_sector_pctile
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_peer_sector_pctile_distmax_504d_base_v151_signal(rnd_sector_pctile, closeadj):
    base = rnd_sector_pctile
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_peer_industry_pctile_distmax_252d_base_v152_signal(rnd_industry_pctile, closeadj):
    base = rnd_industry_pctile
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_peer_industry_pctile_distmax_504d_base_v153_signal(rnd_industry_pctile, closeadj):
    base = rnd_industry_pctile
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_lvl_distmed_126d_base_v154_signal(rnd, closeadj):
    base = rnd
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_lvl_distmed_252d_base_v155_signal(rnd, closeadj):
    base = rnd
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_lvl_distmed_504d_base_v156_signal(rnd, closeadj):
    base = rnd
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_log_rnd_distmed_126d_base_v157_signal(rnd, closeadj):
    base = _f016_rnd_log(rnd)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_log_rnd_distmed_252d_base_v158_signal(rnd, closeadj):
    base = _f016_rnd_log(rnd)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_log_rnd_distmed_504d_base_v159_signal(rnd, closeadj):
    base = _f016_rnd_log(rnd)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_per_share_distmed_126d_base_v160_signal(rnd, sharesbas, closeadj):
    base = _f016_rnd_per_share(rnd, sharesbas)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_per_share_distmed_252d_base_v161_signal(rnd, sharesbas, closeadj):
    base = _f016_rnd_per_share(rnd, sharesbas)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_per_share_distmed_504d_base_v162_signal(rnd, sharesbas, closeadj):
    base = _f016_rnd_per_share(rnd, sharesbas)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_per_dilshare_distmed_126d_base_v163_signal(rnd, shareswadil, closeadj):
    base = rnd / shareswadil.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_per_dilshare_distmed_252d_base_v164_signal(rnd, shareswadil, closeadj):
    base = rnd / shareswadil.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_per_dilshare_distmed_504d_base_v165_signal(rnd, shareswadil, closeadj):
    base = rnd / shareswadil.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_log_expand_distmed_126d_base_v166_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)).expanding(21).mean()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_log_expand_distmed_252d_base_v167_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)).expanding(21).mean()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_log_expand_distmed_504d_base_v168_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)).expanding(21).mean()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_log_minus_5y_distmed_126d_base_v169_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(1260).abs().replace(0, np.nan))
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_log_minus_5y_distmed_252d_base_v170_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(1260).abs().replace(0, np.nan))
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_log_minus_5y_distmed_504d_base_v171_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(1260).abs().replace(0, np.nan))
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_yoy_log_distmed_126d_base_v172_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_yoy_log_distmed_252d_base_v173_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_yoy_log_distmed_504d_base_v174_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f016_rnd_level_rnd_peer_sector_dist_distmed_126d_base_v175_signal(rnd, rnd_sector_med, closeadj):
    base = (rnd - rnd_sector_med) / rnd_sector_med.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

