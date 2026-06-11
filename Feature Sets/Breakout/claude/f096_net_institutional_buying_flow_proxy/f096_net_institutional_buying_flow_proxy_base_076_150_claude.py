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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f096_share_stability(sharesbas, w):
    ch = sharesbas.pct_change()
    return -ch.rolling(w, min_periods=max(1, w // 2)).std()


def _f096_volume_intensity(volume, w):
    base = volume.rolling(w, min_periods=max(1, w // 2)).mean()
    return volume / base.replace(0, np.nan)


def _f096_buying_flow_proxy(sharesbas, volume, w):
    stab = _f096_share_stability(sharesbas, w)
    inten = _f096_volume_intensity(volume, w)
    return stab * inten


def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_63d_xcstd63_base_v076_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_63d_xv_base_v077_signal(sharesbas, volume):
    base = _f096_share_stability(sharesbas, 63)
    result = base * volume / 1e6
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_63d_xvm_base_v078_signal(sharesbas, volume):
    base = _f096_share_stability(sharesbas, 63)
    result = _mean(base * volume, 21) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_63d_xvz_base_v079_signal(sharesbas, volume):
    base = _f096_share_stability(sharesbas, 63)
    result = _z(base, 252) * volume / 1e6
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_63d_xsb_base_v080_signal(sharesbas):
    base = _f096_share_stability(sharesbas, 63)
    result = base * sharesbas / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_126d_xc_base_v081_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_126d_xcm_base_v082_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 126)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_126d_xcm5_base_v083_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 126)
    result = _mean(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_126d_xcm63_base_v084_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 126)
    result = _z(_mean(base, 63), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_126d_xclog_base_v085_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 126)
    result = base * np.log(closeadj.replace(0, np.nan).abs() + 1)
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_126d_xczs_base_v086_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 126)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_126d_xczs126_base_v087_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 126)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_126d_xc2_base_v088_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 126)
    result = _z(base * closeadj, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_126d_xcret_base_v089_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 126)
    result = base * closeadj.pct_change(21).fillna(0)
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_126d_xcadd_base_v090_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 126)
    result = _z((base + 0.01), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_126d_xcstd_base_v091_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 126)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_126d_xcstd63_base_v092_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 126)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_126d_xv_base_v093_signal(sharesbas, volume):
    base = _f096_share_stability(sharesbas, 126)
    result = base * volume / 1e6
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_126d_xvm_base_v094_signal(sharesbas, volume):
    base = _f096_share_stability(sharesbas, 126)
    result = _mean(base * volume, 21) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_126d_xvz_base_v095_signal(sharesbas, volume):
    base = _f096_share_stability(sharesbas, 126)
    result = _z(base, 252) * volume / 1e6
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_126d_xsb_base_v096_signal(sharesbas):
    base = _f096_share_stability(sharesbas, 126)
    result = base * sharesbas / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_189d_xc_base_v097_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 189)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_189d_xcm_base_v098_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 189)
    result = _z(_mean(base, 21), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_189d_xcm5_base_v099_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 189)
    result = _z(_mean(base, 5), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_189d_xcm63_base_v100_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 189)
    result = _z(_mean(base, 63), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_189d_xclog_base_v101_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 189)
    result = base * np.log(closeadj.replace(0, np.nan).abs() + 1)
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_189d_xczs_base_v102_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 189)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_189d_xczs126_base_v103_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 189)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_189d_xc2_base_v104_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 189)
    result = _z(base * closeadj, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_189d_xcret_base_v105_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 189)
    result = base * closeadj.pct_change(21).fillna(0)
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_189d_xcadd_base_v106_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 189)
    result = _z((base + 0.01), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_189d_xcstd_base_v107_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 189)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_189d_xcstd63_base_v108_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 189)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_189d_xv_base_v109_signal(sharesbas, volume):
    base = _f096_share_stability(sharesbas, 189)
    result = base * volume / 1e6
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_189d_xvm_base_v110_signal(sharesbas, volume):
    base = _f096_share_stability(sharesbas, 189)
    result = _mean(base * volume, 21) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_189d_xvz_base_v111_signal(sharesbas, volume):
    base = _f096_share_stability(sharesbas, 189)
    result = _z(base, 252) * volume / 1e6
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_189d_xsb_base_v112_signal(sharesbas):
    base = _f096_share_stability(sharesbas, 189)
    result = base * sharesbas / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_252d_xc_base_v113_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 252)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_252d_xcm_base_v114_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 252)
    result = _z(_mean(base, 21), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_252d_xcm5_base_v115_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 252)
    result = _z(_mean(base, 5), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_252d_xcm63_base_v116_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 252)
    result = _z(_mean(base, 63), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_252d_xclog_base_v117_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 252)
    result = base * np.log(closeadj.replace(0, np.nan).abs() + 1)
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_252d_xczs_base_v118_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_252d_xczs126_base_v119_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_252d_xc2_base_v120_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 252)
    result = _z(base * closeadj, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_252d_xcret_base_v121_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 252)
    result = base * closeadj.pct_change(21).fillna(0)
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_252d_xcadd_base_v122_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 252)
    result = _z((base + 0.01), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_252d_xcstd_base_v123_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 252)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_252d_xcstd63_base_v124_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 252)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_252d_xv_base_v125_signal(sharesbas, volume):
    base = _f096_share_stability(sharesbas, 252)
    result = base * volume / 1e6
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_252d_xvm_base_v126_signal(sharesbas, volume):
    base = _f096_share_stability(sharesbas, 252)
    result = _mean(base * volume, 21) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_252d_xvz_base_v127_signal(sharesbas, volume):
    base = _f096_share_stability(sharesbas, 252)
    result = _z(base, 252) * volume / 1e6
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_252d_xsb_base_v128_signal(sharesbas):
    base = _f096_share_stability(sharesbas, 252)
    result = base * sharesbas / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_378d_xc_base_v129_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 378)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_378d_xcm_base_v130_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 378)
    result = _z(_mean(base, 21), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_378d_xcm5_base_v131_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 378)
    result = _z(_mean(base, 5), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_378d_xcm63_base_v132_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 378)
    result = _z(_mean(base, 63), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_378d_xclog_base_v133_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 378)
    result = base * np.log(closeadj.replace(0, np.nan).abs() + 1)
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_378d_xczs_base_v134_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 378)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_378d_xczs126_base_v135_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 378)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_378d_xc2_base_v136_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 378)
    result = _z(base * closeadj, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_378d_xcret_base_v137_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 378)
    result = base * closeadj.pct_change(21).fillna(0)
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_378d_xcadd_base_v138_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 378)
    result = _z((base + 0.01), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_378d_xcstd_base_v139_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 378)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_378d_xcstd63_base_v140_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 378)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_378d_xv_base_v141_signal(sharesbas, volume):
    base = _f096_share_stability(sharesbas, 378)
    result = base * volume / 1e6
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_378d_xvm_base_v142_signal(sharesbas, volume):
    base = _f096_share_stability(sharesbas, 378)
    result = _mean(base * volume, 21) / 1e6
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_378d_xvz_base_v143_signal(sharesbas, volume):
    base = _f096_share_stability(sharesbas, 378)
    result = _z(base, 252) * volume / 1e6
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_378d_xsb_base_v144_signal(sharesbas):
    base = _f096_share_stability(sharesbas, 378)
    result = base * sharesbas / 1e8
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_504d_xc_base_v145_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 504)
    result = _z(base, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_504d_xcm_base_v146_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 504)
    result = _z(_mean(base, 21), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_504d_xcm5_base_v147_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 504)
    result = _z(_mean(base, 5), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_504d_xcm63_base_v148_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 504)
    result = _z(_mean(base, 63), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_504d_xclog_base_v149_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 504)
    result = base * np.log(closeadj.replace(0, np.nan).abs() + 1)
    return result.replace([np.inf, -np.inf], np.nan)

def f096nif_f096_net_institutional_buying_flow_proxy_share_stability_504d_xczs_base_v150_signal(closeadj, sharesbas):
    base = _f096_share_stability(sharesbas, 504)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_63d_xcstd63_base_v076_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_63d_xv_base_v077_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_63d_xvm_base_v078_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_63d_xvz_base_v079_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_63d_xsb_base_v080_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_126d_xc_base_v081_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_126d_xcm_base_v082_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_126d_xcm5_base_v083_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_126d_xcm63_base_v084_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_126d_xclog_base_v085_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_126d_xczs_base_v086_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_126d_xczs126_base_v087_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_126d_xc2_base_v088_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_126d_xcret_base_v089_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_126d_xcadd_base_v090_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_126d_xcstd_base_v091_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_126d_xcstd63_base_v092_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_126d_xv_base_v093_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_126d_xvm_base_v094_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_126d_xvz_base_v095_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_126d_xsb_base_v096_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_189d_xc_base_v097_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_189d_xcm_base_v098_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_189d_xcm5_base_v099_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_189d_xcm63_base_v100_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_189d_xclog_base_v101_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_189d_xczs_base_v102_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_189d_xczs126_base_v103_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_189d_xc2_base_v104_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_189d_xcret_base_v105_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_189d_xcadd_base_v106_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_189d_xcstd_base_v107_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_189d_xcstd63_base_v108_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_189d_xv_base_v109_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_189d_xvm_base_v110_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_189d_xvz_base_v111_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_189d_xsb_base_v112_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_252d_xc_base_v113_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_252d_xcm_base_v114_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_252d_xcm5_base_v115_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_252d_xcm63_base_v116_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_252d_xclog_base_v117_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_252d_xczs_base_v118_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_252d_xczs126_base_v119_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_252d_xc2_base_v120_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_252d_xcret_base_v121_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_252d_xcadd_base_v122_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_252d_xcstd_base_v123_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_252d_xcstd63_base_v124_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_252d_xv_base_v125_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_252d_xvm_base_v126_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_252d_xvz_base_v127_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_252d_xsb_base_v128_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_378d_xc_base_v129_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_378d_xcm_base_v130_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_378d_xcm5_base_v131_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_378d_xcm63_base_v132_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_378d_xclog_base_v133_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_378d_xczs_base_v134_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_378d_xczs126_base_v135_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_378d_xc2_base_v136_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_378d_xcret_base_v137_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_378d_xcadd_base_v138_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_378d_xcstd_base_v139_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_378d_xcstd63_base_v140_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_378d_xv_base_v141_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_378d_xvm_base_v142_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_378d_xvz_base_v143_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_378d_xsb_base_v144_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_504d_xc_base_v145_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_504d_xcm_base_v146_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_504d_xcm5_base_v147_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_504d_xcm63_base_v148_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_504d_xclog_base_v149_signal,
    f096nif_f096_net_institutional_buying_flow_proxy_share_stability_504d_xczs_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F096_NET_INSTITUTIONAL_BUYING_FLOW_PROXY_REGISTRY_076_150 = REGISTRY

if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetsc      = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsc")
    assetsnc     = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsnc")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    liabilitiesc = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesc")
    liabilitiesnc= pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesnc")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    equityusd    = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equityusd")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    debtc        = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtc")
    debtnc       = pd.Series(4.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtnc")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    intangibles  = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    tangibles    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="tangibles")
    invcap       = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")
    retearn      = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")
    sbcomp       = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="sbcomp")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    shareswadil  = pd.Series(1.02e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswadil")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    epsdil       = pd.Series(0.98 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="epsdil")
    bvps         = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="bvps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    sps          = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="sps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    pe           = pd.Series(closeadj / eps.replace(0, np.nan).abs(), name="pe")
    pb           = pd.Series(closeadj / bvps.replace(0, np.nan).abs(), name="pb")
    ps           = pd.Series(closeadj / sps.replace(0, np.nan).abs(), name="ps")
    evebit       = pd.Series(ev / ebit.replace(0, np.nan).abs(), name="evebit")
    evebitda     = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ros          = pd.Series(0.08 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ros")
    currentratio = pd.Series(1.5 + 0.3*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="currentratio")
    de           = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    divyield     = pd.Series(0.02 + 0.005*np.sin(np.arange(n)/250.0) + 0.001*np.random.randn(n), name="divyield")
    assetturnover= pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "assets": assets, "assetsc": assetsc, "assetsnc": assetsnc,
        "liabilities": liabilities, "liabilitiesc": liabilitiesc, "liabilitiesnc": liabilitiesnc,
        "equity": equity, "equityusd": equityusd,
        "debt": debt, "debtc": debtc, "debtnc": debtnc, "cashneq": cashneq,
        "inventory": inventory, "receivables": receivables, "payables": payables,
        "deferredrev": deferredrev, "workingcapital": workingcapital,
        "ppnenet": ppnenet, "intangibles": intangibles, "tangibles": tangibles,
        "invcap": invcap, "retearn": retearn, "sbcomp": sbcomp,
        "sharesbas": sharesbas, "shareswa": shareswa, "shareswadil": shareswadil,
        "eps": eps, "epsdil": epsdil, "bvps": bvps, "fcfps": fcfps, "sps": sps, "dps": dps,
        "marketcap": marketcap, "ev": ev,
        "pe": pe, "pb": pb, "ps": ps, "evebit": evebit, "evebitda": evebitda,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
        "roa": roa, "roe": roe, "roic": roic, "ros": ros,
        "currentratio": currentratio, "de": de,
        "payoutratio": payoutratio, "divyield": divyield, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f096_share_stability", "_f096_volume_intensity", "_f096_buying_flow_proxy")
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f096_net_institutional_buying_flow_proxy_base_076_150_claude: {n_features} features pass")
