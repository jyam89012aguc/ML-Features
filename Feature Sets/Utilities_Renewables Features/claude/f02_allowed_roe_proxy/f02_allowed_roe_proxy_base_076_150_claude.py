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


def _f02_roe_proxy(netinc, equity):
    return netinc / equity.replace(0, np.nan)


def _f02_roe_dynamics(netinc, equity, w):
    roe = netinc / equity.replace(0, np.nan)
    return roe - roe.rolling(w, min_periods=max(1, w // 2)).mean()


def _f02_roe_durability(roe, w):
    m = roe.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = roe.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan)


# 63d ROE proxy × close pct change scaled
def f02arp_f02_allowed_roe_proxy_proxyxretpct_63d_base_v076_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    p = closeadj.pct_change(21)
    result = base * p * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROE proxy × close pct
def f02arp_f02_allowed_roe_proxy_proxyxretpct_252d_base_v077_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    p = closeadj.pct_change(63)
    result = base * p * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROE proxy gap (cur vs 504d mean) × close
def f02arp_f02_allowed_roe_proxy_proxygap_252d_base_v078_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    result = (base - _mean(base, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROE proxy gap × close
def f02arp_f02_allowed_roe_proxy_proxygap_63d_base_v079_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    result = (base - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ROE proxy × inverse close × scale
def f02arp_f02_allowed_roe_proxy_proxyxinvprice_63d_base_v080_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    result = _mean(base, 63) * _mean(closeadj, 21) * _mean(closeadj, 21) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROE proxy × inv close × scale
def f02arp_f02_allowed_roe_proxy_proxyxinvprice_252d_base_v081_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    result = _mean(base, 252) * _mean(closeadj, 63) * _mean(closeadj, 63) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# ROE proxy × close z × close
def f02arp_f02_allowed_roe_proxy_proxyxclosez_63d_base_v082_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    result = base * _z(closeadj, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ROE proxy × close z × close (252d)
def f02arp_f02_allowed_roe_proxy_proxyxclosez_252d_base_v083_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    result = base * _z(closeadj, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ROE proxy × volume z × close
def f02arp_f02_allowed_roe_proxy_proxyxvolz_63d_base_v084_signal(netinc, equity, closeadj, volume):
    base = _f02_roe_proxy(netinc, equity)
    result = base * _z(volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ROE proxy × volume z × close (252d)
def f02arp_f02_allowed_roe_proxy_proxyxvolz_252d_base_v085_signal(netinc, equity, closeadj, volume):
    base = _f02_roe_proxy(netinc, equity)
    result = base * _z(volume, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ROE proxy × sign × close × volume
def f02arp_f02_allowed_roe_proxy_proxysign_63d_base_v086_signal(netinc, equity, closeadj, volume):
    base = _f02_roe_proxy(netinc, equity)
    result = np.sign(base - _mean(base, 63)) * _mean(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ROE proxy × abs × close
def f02arp_f02_allowed_roe_proxy_proxyabs_63d_base_v087_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ROE proxy × close pct (5d) × close
def f02arp_f02_allowed_roe_proxy_proxyxret5_63d_base_v088_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    result = base * closeadj.pct_change(5) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ROE proxy × close pct (10d) × close
def f02arp_f02_allowed_roe_proxy_proxyxret10_63d_base_v089_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    result = base * closeadj.pct_change(10) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ROE proxy × roe × close
def f02arp_f02_allowed_roe_proxy_proxyxroe_63d_base_v090_signal(netinc, equity, roe, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    result = base * roe * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ROE proxy × roe × close (252d)
def f02arp_f02_allowed_roe_proxy_proxyxroe_252d_base_v091_signal(netinc, equity, roe, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    result = _mean(base, 252) * _mean(roe, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROE dynamics × ATR
def f02arp_f02_allowed_roe_proxy_dynxatr_63d_base_v092_signal(netinc, equity, closeadj, high, low):
    base = _f02_roe_dynamics(netinc, equity, 63)
    atr = (high - low).rolling(21, min_periods=5).mean()
    result = base * atr
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROE dynamics × ATR
def f02arp_f02_allowed_roe_proxy_dynxatr_252d_base_v093_signal(netinc, equity, closeadj, high, low):
    base = _f02_roe_dynamics(netinc, equity, 252)
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = base * atr
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROE dynamics × dollar volume
def f02arp_f02_allowed_roe_proxy_dynxdv_63d_base_v094_signal(netinc, equity, closeadj, volume):
    base = _f02_roe_dynamics(netinc, equity, 63)
    dv = closeadj * volume
    result = base * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROE dynamics × dollar volume
def f02arp_f02_allowed_roe_proxy_dynxdv_252d_base_v095_signal(netinc, equity, closeadj, volume):
    base = _f02_roe_dynamics(netinc, equity, 252)
    dv = closeadj * volume
    result = base * _mean(dv, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROE dynamics × inv close × scale
def f02arp_f02_allowed_roe_proxy_dynxinvprice_63d_base_v096_signal(netinc, equity, closeadj):
    base = _f02_roe_dynamics(netinc, equity, 63)
    result = base * _mean(closeadj, 21) * _mean(closeadj, 21) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROE dynamics × inv close × scale
def f02arp_f02_allowed_roe_proxy_dynxinvprice_252d_base_v097_signal(netinc, equity, closeadj):
    base = _f02_roe_dynamics(netinc, equity, 252)
    result = base * _mean(closeadj, 63) * _mean(closeadj, 63) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROE dynamics × close z × close
def f02arp_f02_allowed_roe_proxy_dynxclosez_63d_base_v098_signal(netinc, equity, closeadj):
    base = _f02_roe_dynamics(netinc, equity, 63)
    result = base * _z(closeadj, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROE dynamics × close z × close
def f02arp_f02_allowed_roe_proxy_dynxclosez_252d_base_v099_signal(netinc, equity, closeadj):
    base = _f02_roe_dynamics(netinc, equity, 252)
    result = base * _z(closeadj, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROE dynamics × abs return × close
def f02arp_f02_allowed_roe_proxy_dynxabsret_63d_base_v100_signal(netinc, equity, closeadj):
    base = _f02_roe_dynamics(netinc, equity, 63)
    p = closeadj.pct_change(21).abs()
    result = base * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROE dynamics × abs return × close
def f02arp_f02_allowed_roe_proxy_dynxabsret_252d_base_v101_signal(netinc, equity, closeadj):
    base = _f02_roe_dynamics(netinc, equity, 252)
    p = closeadj.pct_change(63).abs()
    result = base * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROE dynamics × log netinc × close
def f02arp_f02_allowed_roe_proxy_dynxsize_63d_base_v102_signal(netinc, equity, closeadj):
    base = _f02_roe_dynamics(netinc, equity, 63)
    s = np.log(netinc.abs().replace(0, np.nan))
    result = base * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROE dynamics × log netinc × close
def f02arp_f02_allowed_roe_proxy_dynxsize_252d_base_v103_signal(netinc, equity, closeadj):
    base = _f02_roe_dynamics(netinc, equity, 252)
    s = np.log(netinc.abs().replace(0, np.nan))
    result = base * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROE dynamics × log equity × close
def f02arp_f02_allowed_roe_proxy_dynxeqsize_63d_base_v104_signal(netinc, equity, closeadj):
    base = _f02_roe_dynamics(netinc, equity, 63)
    s = np.log(equity.replace(0, np.nan))
    result = base * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROE dynamics × log equity × close
def f02arp_f02_allowed_roe_proxy_dynxeqsize_252d_base_v105_signal(netinc, equity, closeadj):
    base = _f02_roe_dynamics(netinc, equity, 252)
    s = np.log(equity.replace(0, np.nan))
    result = base * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roe durability × volume z × close
def f02arp_f02_allowed_roe_proxy_durxvolz_63d_base_v106_signal(roe, closeadj, volume):
    base = _f02_roe_durability(roe, 63)
    result = base * _z(volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roe durability × volume z × close
def f02arp_f02_allowed_roe_proxy_durxvolz_252d_base_v107_signal(roe, closeadj, volume):
    base = _f02_roe_durability(roe, 252)
    result = base * _z(volume, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roe durability × close z × close
def f02arp_f02_allowed_roe_proxy_durxclosez_63d_base_v108_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 63)
    result = base * _z(closeadj, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roe durability × close z × close
def f02arp_f02_allowed_roe_proxy_durxclosez_252d_base_v109_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 252)
    result = base * _z(closeadj, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roe durability × close pct × close
def f02arp_f02_allowed_roe_proxy_durxretpct_63d_base_v110_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 63)
    result = base * closeadj.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roe durability × close pct × close
def f02arp_f02_allowed_roe_proxy_durxretpct_252d_base_v111_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 252)
    result = base * closeadj.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roe durability × abs return × close
def f02arp_f02_allowed_roe_proxy_durxabsret_63d_base_v112_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 63)
    p = closeadj.pct_change(21).abs()
    result = base * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roe durability × abs return × close
def f02arp_f02_allowed_roe_proxy_durxabsret_252d_base_v113_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 252)
    p = closeadj.pct_change(63).abs()
    result = base * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roe durability × inv close × scale
def f02arp_f02_allowed_roe_proxy_durxinvprice_63d_base_v114_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 63)
    result = base * _mean(closeadj, 21) * _mean(closeadj, 21) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roe durability × inv close × scale
def f02arp_f02_allowed_roe_proxy_durxinvprice_252d_base_v115_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 252)
    result = base * _mean(closeadj, 63) * _mean(closeadj, 63) / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roe durability rolling sum × close
def f02arp_f02_allowed_roe_proxy_dursum_63d_base_v116_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 63)
    result = base.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roe durability rolling sum × close
def f02arp_f02_allowed_roe_proxy_dursum_252d_base_v117_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 252)
    result = base.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roe durability rank × close
def f02arp_f02_allowed_roe_proxy_durrank_63d_base_v118_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 63)
    result = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roe durability rank × close
def f02arp_f02_allowed_roe_proxy_durrank_252d_base_v119_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 252)
    result = base.rolling(504, min_periods=126).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roe durability gap (current vs 504d) × close
def f02arp_f02_allowed_roe_proxy_durgap_63d_base_v120_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 63)
    result = (base - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roe durability gap × close
def f02arp_f02_allowed_roe_proxy_durgap_252d_base_v121_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 252)
    result = (base - _mean(base, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roe durability EMA × close
def f02arp_f02_allowed_roe_proxy_durema_63d_base_v122_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 63)
    result = base.ewm(span=21, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roe durability EMA × close
def f02arp_f02_allowed_roe_proxy_durema_252d_base_v123_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 252)
    result = base.ewm(span=63, min_periods=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roe durability squared × close
def f02arp_f02_allowed_roe_proxy_dursq_63d_base_v124_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roe durability squared × close
def f02arp_f02_allowed_roe_proxy_dursq_252d_base_v125_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 252)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roe durability × roe gap × close
def f02arp_f02_allowed_roe_proxy_durxroegap_63d_base_v126_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 63)
    gap = roe - _mean(roe, 252)
    result = base * gap * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roe durability × roe gap × close
def f02arp_f02_allowed_roe_proxy_durxroegap_252d_base_v127_signal(roe, closeadj):
    base = _f02_roe_durability(roe, 252)
    gap = roe - _mean(roe, 504)
    result = base * gap * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ROE proxy × ROE durability × close (combined quality)
def f02arp_f02_allowed_roe_proxy_proxydur_63d_base_v128_signal(netinc, equity, roe, closeadj):
    p = _f02_roe_proxy(netinc, equity)
    d = _f02_roe_durability(roe, 63)
    result = p * d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ROE proxy × ROE durability × close (252d)
def f02arp_f02_allowed_roe_proxy_proxydur_252d_base_v129_signal(netinc, equity, roe, closeadj):
    p = _f02_roe_proxy(netinc, equity)
    d = _f02_roe_durability(roe, 252)
    result = _mean(p, 252) * d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ROE proxy × ROE dynamics × close
def f02arp_f02_allowed_roe_proxy_proxydyn_63d_base_v130_signal(netinc, equity, closeadj):
    p = _f02_roe_proxy(netinc, equity)
    d = _f02_roe_dynamics(netinc, equity, 63)
    result = p * d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ROE proxy × ROE dynamics × close (252d)
def f02arp_f02_allowed_roe_proxy_proxydyn_252d_base_v131_signal(netinc, equity, closeadj):
    p = _f02_roe_proxy(netinc, equity)
    d = _f02_roe_dynamics(netinc, equity, 252)
    result = _mean(p, 252) * d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ROE dynamics × ROE durability × close
def f02arp_f02_allowed_roe_proxy_dyndur_63d_base_v132_signal(netinc, equity, roe, closeadj):
    d1 = _f02_roe_dynamics(netinc, equity, 63)
    d2 = _f02_roe_durability(roe, 63)
    result = d1 * d2 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ROE dynamics × ROE durability × close (252d)
def f02arp_f02_allowed_roe_proxy_dyndur_252d_base_v133_signal(netinc, equity, roe, closeadj):
    d1 = _f02_roe_dynamics(netinc, equity, 252)
    d2 = _f02_roe_durability(roe, 252)
    result = d1 * d2 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ROE proxy difference (5d-252d cross) × close
def f02arp_f02_allowed_roe_proxy_proxyxdiff_5_252_base_v134_signal(netinc, equity, closeadj):
    p = _f02_roe_proxy(netinc, equity)
    short = _mean(p, 5)
    long = _mean(p, 252)
    result = (short - long) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ROE proxy MA cross (21d-63d) × close
def f02arp_f02_allowed_roe_proxy_proxyxdiff_21_63_base_v135_signal(netinc, equity, closeadj):
    p = _f02_roe_proxy(netinc, equity)
    short = _mean(p, 21)
    long = _mean(p, 63)
    result = (short - long) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ROE proxy MA cross (63d-252d) × close
def f02arp_f02_allowed_roe_proxy_proxyxdiff_63_252_base_v136_signal(netinc, equity, closeadj):
    p = _f02_roe_proxy(netinc, equity)
    short = _mean(p, 63)
    long = _mean(p, 252)
    result = (short - long) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ROE proxy MA cross (126d-504d) × close
def f02arp_f02_allowed_roe_proxy_proxyxdiff_126_504_base_v137_signal(netinc, equity, closeadj):
    p = _f02_roe_proxy(netinc, equity)
    short = _mean(p, 126)
    long = _mean(p, 504)
    result = (short - long) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROE dynamics × volume z × close
def f02arp_f02_allowed_roe_proxy_dynxvolz_63d_base_v138_signal(netinc, equity, closeadj, volume):
    base = _f02_roe_dynamics(netinc, equity, 63)
    result = base * _z(volume, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROE dynamics × volume z × close
def f02arp_f02_allowed_roe_proxy_dynxvolz_252d_base_v139_signal(netinc, equity, closeadj, volume):
    base = _f02_roe_dynamics(netinc, equity, 252)
    result = base * _z(volume, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ROE proxy z × volume × close
def f02arp_f02_allowed_roe_proxy_proxyzxvol_63d_base_v140_signal(netinc, equity, closeadj, volume):
    base = _f02_roe_proxy(netinc, equity)
    result = _z(base, 252) * _mean(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ROE proxy z × volume × close (252d)
def f02arp_f02_allowed_roe_proxy_proxyzxvol_252d_base_v141_signal(netinc, equity, closeadj, volume):
    base = _f02_roe_proxy(netinc, equity)
    result = _z(base, 504) * _mean(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ROE proxy × payout proxy × close (dividend interaction)
def f02arp_f02_allowed_roe_proxy_proxyxnetscale_63d_base_v142_signal(netinc, equity, closeadj):
    base = _f02_roe_proxy(netinc, equity)
    scale = _mean(netinc, 21) / _mean(netinc, 252).replace(0, np.nan)
    result = base * scale * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ROE proxy × volume × ATR
def f02arp_f02_allowed_roe_proxy_proxyxvolxatr_63d_base_v143_signal(netinc, equity, closeadj, volume, high, low):
    base = _f02_roe_proxy(netinc, equity)
    atr = (high - low).rolling(21, min_periods=5).mean()
    result = base * _mean(volume, 21) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# ROE proxy × volume × ATR (252d)
def f02arp_f02_allowed_roe_proxy_proxyxvolxatr_252d_base_v144_signal(netinc, equity, closeadj, volume, high, low):
    base = _f02_roe_proxy(netinc, equity)
    atr = (high - low).rolling(63, min_periods=21).mean()
    result = base * _mean(volume, 63) * atr
    return result.replace([np.inf, -np.inf], np.nan)


# ROE proxy × ATR × close
def f02arp_f02_allowed_roe_proxy_proxyxatrxret_63d_base_v145_signal(netinc, equity, closeadj, high, low):
    base = _f02_roe_proxy(netinc, equity)
    atr = (high - low).rolling(21, min_periods=5).mean()
    p = closeadj.pct_change(21)
    result = base * atr * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# ROE proxy × ATR × close (252d)
def f02arp_f02_allowed_roe_proxy_proxyxatrxret_252d_base_v146_signal(netinc, equity, closeadj, high, low):
    base = _f02_roe_proxy(netinc, equity)
    atr = (high - low).rolling(63, min_periods=21).mean()
    p = closeadj.pct_change(63)
    result = base * atr * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d roe durability × log netinc × close
def f02arp_f02_allowed_roe_proxy_durxsize_63d_base_v147_signal(netinc, roe, closeadj):
    base = _f02_roe_durability(roe, 63)
    s = np.log(netinc.abs().replace(0, np.nan))
    result = base * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d roe durability × log netinc × close
def f02arp_f02_allowed_roe_proxy_durxsize_252d_base_v148_signal(netinc, roe, closeadj):
    base = _f02_roe_durability(roe, 252)
    s = np.log(netinc.abs().replace(0, np.nan))
    result = base * s * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROE proxy × roe × volume × close
def f02arp_f02_allowed_roe_proxy_proxyxroexvol_252d_base_v149_signal(netinc, equity, roe, closeadj, volume):
    base = _f02_roe_proxy(netinc, equity)
    result = _mean(base, 252) * _mean(roe, 252) * _mean(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROE proxy × roe × volume × close
def f02arp_f02_allowed_roe_proxy_proxyxroexvol_63d_base_v150_signal(netinc, equity, roe, closeadj, volume):
    base = _f02_roe_proxy(netinc, equity)
    result = _mean(base, 63) * _mean(roe, 63) * _mean(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f02arp_f02_allowed_roe_proxy_proxyxretpct_63d_base_v076_signal,
    f02arp_f02_allowed_roe_proxy_proxyxretpct_252d_base_v077_signal,
    f02arp_f02_allowed_roe_proxy_proxygap_252d_base_v078_signal,
    f02arp_f02_allowed_roe_proxy_proxygap_63d_base_v079_signal,
    f02arp_f02_allowed_roe_proxy_proxyxinvprice_63d_base_v080_signal,
    f02arp_f02_allowed_roe_proxy_proxyxinvprice_252d_base_v081_signal,
    f02arp_f02_allowed_roe_proxy_proxyxclosez_63d_base_v082_signal,
    f02arp_f02_allowed_roe_proxy_proxyxclosez_252d_base_v083_signal,
    f02arp_f02_allowed_roe_proxy_proxyxvolz_63d_base_v084_signal,
    f02arp_f02_allowed_roe_proxy_proxyxvolz_252d_base_v085_signal,
    f02arp_f02_allowed_roe_proxy_proxysign_63d_base_v086_signal,
    f02arp_f02_allowed_roe_proxy_proxyabs_63d_base_v087_signal,
    f02arp_f02_allowed_roe_proxy_proxyxret5_63d_base_v088_signal,
    f02arp_f02_allowed_roe_proxy_proxyxret10_63d_base_v089_signal,
    f02arp_f02_allowed_roe_proxy_proxyxroe_63d_base_v090_signal,
    f02arp_f02_allowed_roe_proxy_proxyxroe_252d_base_v091_signal,
    f02arp_f02_allowed_roe_proxy_dynxatr_63d_base_v092_signal,
    f02arp_f02_allowed_roe_proxy_dynxatr_252d_base_v093_signal,
    f02arp_f02_allowed_roe_proxy_dynxdv_63d_base_v094_signal,
    f02arp_f02_allowed_roe_proxy_dynxdv_252d_base_v095_signal,
    f02arp_f02_allowed_roe_proxy_dynxinvprice_63d_base_v096_signal,
    f02arp_f02_allowed_roe_proxy_dynxinvprice_252d_base_v097_signal,
    f02arp_f02_allowed_roe_proxy_dynxclosez_63d_base_v098_signal,
    f02arp_f02_allowed_roe_proxy_dynxclosez_252d_base_v099_signal,
    f02arp_f02_allowed_roe_proxy_dynxabsret_63d_base_v100_signal,
    f02arp_f02_allowed_roe_proxy_dynxabsret_252d_base_v101_signal,
    f02arp_f02_allowed_roe_proxy_dynxsize_63d_base_v102_signal,
    f02arp_f02_allowed_roe_proxy_dynxsize_252d_base_v103_signal,
    f02arp_f02_allowed_roe_proxy_dynxeqsize_63d_base_v104_signal,
    f02arp_f02_allowed_roe_proxy_dynxeqsize_252d_base_v105_signal,
    f02arp_f02_allowed_roe_proxy_durxvolz_63d_base_v106_signal,
    f02arp_f02_allowed_roe_proxy_durxvolz_252d_base_v107_signal,
    f02arp_f02_allowed_roe_proxy_durxclosez_63d_base_v108_signal,
    f02arp_f02_allowed_roe_proxy_durxclosez_252d_base_v109_signal,
    f02arp_f02_allowed_roe_proxy_durxretpct_63d_base_v110_signal,
    f02arp_f02_allowed_roe_proxy_durxretpct_252d_base_v111_signal,
    f02arp_f02_allowed_roe_proxy_durxabsret_63d_base_v112_signal,
    f02arp_f02_allowed_roe_proxy_durxabsret_252d_base_v113_signal,
    f02arp_f02_allowed_roe_proxy_durxinvprice_63d_base_v114_signal,
    f02arp_f02_allowed_roe_proxy_durxinvprice_252d_base_v115_signal,
    f02arp_f02_allowed_roe_proxy_dursum_63d_base_v116_signal,
    f02arp_f02_allowed_roe_proxy_dursum_252d_base_v117_signal,
    f02arp_f02_allowed_roe_proxy_durrank_63d_base_v118_signal,
    f02arp_f02_allowed_roe_proxy_durrank_252d_base_v119_signal,
    f02arp_f02_allowed_roe_proxy_durgap_63d_base_v120_signal,
    f02arp_f02_allowed_roe_proxy_durgap_252d_base_v121_signal,
    f02arp_f02_allowed_roe_proxy_durema_63d_base_v122_signal,
    f02arp_f02_allowed_roe_proxy_durema_252d_base_v123_signal,
    f02arp_f02_allowed_roe_proxy_dursq_63d_base_v124_signal,
    f02arp_f02_allowed_roe_proxy_dursq_252d_base_v125_signal,
    f02arp_f02_allowed_roe_proxy_durxroegap_63d_base_v126_signal,
    f02arp_f02_allowed_roe_proxy_durxroegap_252d_base_v127_signal,
    f02arp_f02_allowed_roe_proxy_proxydur_63d_base_v128_signal,
    f02arp_f02_allowed_roe_proxy_proxydur_252d_base_v129_signal,
    f02arp_f02_allowed_roe_proxy_proxydyn_63d_base_v130_signal,
    f02arp_f02_allowed_roe_proxy_proxydyn_252d_base_v131_signal,
    f02arp_f02_allowed_roe_proxy_dyndur_63d_base_v132_signal,
    f02arp_f02_allowed_roe_proxy_dyndur_252d_base_v133_signal,
    f02arp_f02_allowed_roe_proxy_proxyxdiff_5_252_base_v134_signal,
    f02arp_f02_allowed_roe_proxy_proxyxdiff_21_63_base_v135_signal,
    f02arp_f02_allowed_roe_proxy_proxyxdiff_63_252_base_v136_signal,
    f02arp_f02_allowed_roe_proxy_proxyxdiff_126_504_base_v137_signal,
    f02arp_f02_allowed_roe_proxy_dynxvolz_63d_base_v138_signal,
    f02arp_f02_allowed_roe_proxy_dynxvolz_252d_base_v139_signal,
    f02arp_f02_allowed_roe_proxy_proxyzxvol_63d_base_v140_signal,
    f02arp_f02_allowed_roe_proxy_proxyzxvol_252d_base_v141_signal,
    f02arp_f02_allowed_roe_proxy_proxyxnetscale_63d_base_v142_signal,
    f02arp_f02_allowed_roe_proxy_proxyxvolxatr_63d_base_v143_signal,
    f02arp_f02_allowed_roe_proxy_proxyxvolxatr_252d_base_v144_signal,
    f02arp_f02_allowed_roe_proxy_proxyxatrxret_63d_base_v145_signal,
    f02arp_f02_allowed_roe_proxy_proxyxatrxret_252d_base_v146_signal,
    f02arp_f02_allowed_roe_proxy_durxsize_63d_base_v147_signal,
    f02arp_f02_allowed_roe_proxy_durxsize_252d_base_v148_signal,
    f02arp_f02_allowed_roe_proxy_proxyxroexvol_252d_base_v149_signal,
    f02arp_f02_allowed_roe_proxy_proxyxroexvol_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F02_ALLOWED_ROE_PROXY_REGISTRY_076_150 = REGISTRY


def _build_cols():
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = pd.Series(closeadj.values * (1.0 + np.abs(np.random.normal(0, 0.01, n))), name="high")
    low = pd.Series(closeadj.values * (1.0 - np.abs(np.random.normal(0, 0.01, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    netinc = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    equity = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    roe = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    return {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "netinc": netinc, "equity": equity, "roe": roe,
    }


if __name__ == "__main__":
    cols = _build_cols()
    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f02_roe_proxy", "_f02_roe_dynamics", "_f02_roe_durability")
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
    print(f"OK f02_allowed_roe_proxy_base_076_150_claude: {n_features} features pass")
