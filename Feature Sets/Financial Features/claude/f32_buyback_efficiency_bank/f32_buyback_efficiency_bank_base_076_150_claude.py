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


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2)).mean()


def _qrank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


# ===== folder domain primitives =====

def _f32_share_change(sharesbas, w):
    return sharesbas.pct_change(periods=w)


def _f32_buyback_intensity(sharesbas, closeadj, w):
    ch = sharesbas.pct_change(periods=w)
    return (-ch) * closeadj


def _f32_buyback_timing(sharesbas, closeadj, pb, w):
    ch = sharesbas.pct_change(periods=w)
    return (-ch) * (1.0 / pb.replace(0, np.nan).abs()) * closeadj


# ===== features =====
def f32beb_f32_buyback_efficiency_bank_bbintensxpb_5d_base_v076_signal(sharesbas, closeadj, pb):
    base = _f32_buyback_intensity(sharesbas, closeadj, 5)
    result = base * (1.0 / (pb.abs() + 0.01))
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintensxpb_10d_base_v077_signal(sharesbas, closeadj, pb):
    base = _f32_buyback_intensity(sharesbas, closeadj, 10)
    result = base * (1.0 / (pb.abs() + 0.01))
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintensxpb_21d_base_v078_signal(sharesbas, closeadj, pb):
    base = _f32_buyback_intensity(sharesbas, closeadj, 21)
    result = base * (1.0 / (pb.abs() + 0.01))
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintensxpb_42d_base_v079_signal(sharesbas, closeadj, pb):
    base = _f32_buyback_intensity(sharesbas, closeadj, 42)
    result = base * (1.0 / (pb.abs() + 0.01))
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintensxpb_63d_base_v080_signal(sharesbas, closeadj, pb):
    base = _f32_buyback_intensity(sharesbas, closeadj, 63)
    result = base * (1.0 / (pb.abs() + 0.01))
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintensxpb_126d_base_v081_signal(sharesbas, closeadj, pb):
    base = _f32_buyback_intensity(sharesbas, closeadj, 126)
    result = base * (1.0 / (pb.abs() + 0.01))
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintensxpb_189d_base_v082_signal(sharesbas, closeadj, pb):
    base = _f32_buyback_intensity(sharesbas, closeadj, 189)
    result = base * (1.0 / (pb.abs() + 0.01))
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintensxpb_252d_base_v083_signal(sharesbas, closeadj, pb):
    base = _f32_buyback_intensity(sharesbas, closeadj, 252)
    result = base * (1.0 / (pb.abs() + 0.01))
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintensxpb_378d_base_v084_signal(sharesbas, closeadj, pb):
    base = _f32_buyback_intensity(sharesbas, closeadj, 378)
    result = base * (1.0 / (pb.abs() + 0.01))
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintensxpb_504d_base_v085_signal(sharesbas, closeadj, pb):
    base = _f32_buyback_intensity(sharesbas, closeadj, 504)
    result = base * (1.0 / (pb.abs() + 0.01))
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbtimingz_21d_base_v086_signal(sharesbas, closeadj, pb):
    base = _f32_buyback_timing(sharesbas, closeadj, pb, 21)
    result = _z(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbtimingz_42d_base_v087_signal(sharesbas, closeadj, pb):
    base = _f32_buyback_timing(sharesbas, closeadj, pb, 42)
    result = _z(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbtimingz_63d_base_v088_signal(sharesbas, closeadj, pb):
    base = _f32_buyback_timing(sharesbas, closeadj, pb, 63)
    result = _z(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbtimingz_126d_base_v089_signal(sharesbas, closeadj, pb):
    base = _f32_buyback_timing(sharesbas, closeadj, pb, 126)
    result = _z(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbtimingz_189d_base_v090_signal(sharesbas, closeadj, pb):
    base = _f32_buyback_timing(sharesbas, closeadj, pb, 189)
    result = _z(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbtimingz_252d_base_v091_signal(sharesbas, closeadj, pb):
    base = _f32_buyback_timing(sharesbas, closeadj, pb, 252)
    result = _z(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbtimingz_378d_base_v092_signal(sharesbas, closeadj, pb):
    base = _f32_buyback_timing(sharesbas, closeadj, pb, 378)
    result = _z(base, 378)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbtimingz_504d_base_v093_signal(sharesbas, closeadj, pb):
    base = _f32_buyback_timing(sharesbas, closeadj, pb, 504)
    result = _z(base, 504)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintensqrank_63d_base_v094_signal(sharesbas, closeadj):
    base = _f32_buyback_intensity(sharesbas, closeadj, 63)
    result = _qrank(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintensqrank_126d_base_v095_signal(sharesbas, closeadj):
    base = _f32_buyback_intensity(sharesbas, closeadj, 126)
    result = _qrank(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintensqrank_252d_base_v096_signal(sharesbas, closeadj):
    base = _f32_buyback_intensity(sharesbas, closeadj, 252)
    result = _qrank(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintensqrank_504d_base_v097_signal(sharesbas, closeadj):
    base = _f32_buyback_intensity(sharesbas, closeadj, 504)
    result = _qrank(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintensqrank_21d_base_v098_signal(sharesbas, closeadj):
    base = _f32_buyback_intensity(sharesbas, closeadj, 21)
    result = _qrank(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintensqrank_42d_base_v099_signal(sharesbas, closeadj):
    base = _f32_buyback_intensity(sharesbas, closeadj, 42)
    result = _qrank(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangexc2_21d_base_v100_signal(sharesbas, closeadj):
    g = _f32_share_change(sharesbas, 21)
    result = g * closeadj * _mean(closeadj, 7)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangexc2_63d_base_v101_signal(sharesbas, closeadj):
    g = _f32_share_change(sharesbas, 63)
    result = g * closeadj * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangexc2_126d_base_v102_signal(sharesbas, closeadj):
    g = _f32_share_change(sharesbas, 126)
    result = g * closeadj * _mean(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangexc2_252d_base_v103_signal(sharesbas, closeadj):
    g = _f32_share_change(sharesbas, 252)
    result = g * closeadj * _mean(closeadj, 84)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangexc2_504d_base_v104_signal(sharesbas, closeadj):
    g = _f32_share_change(sharesbas, 504)
    result = g * closeadj * _mean(closeadj, 168)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangexc2_42d_base_v105_signal(sharesbas, closeadj):
    g = _f32_share_change(sharesbas, 42)
    result = g * closeadj * _mean(closeadj, 14)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbtimingmean_21d_base_v106_signal(sharesbas, closeadj, pb):
    base = _f32_buyback_timing(sharesbas, closeadj, pb, 21)
    result = _mean(base, 7)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbtimingmean_63d_base_v107_signal(sharesbas, closeadj, pb):
    base = _f32_buyback_timing(sharesbas, closeadj, pb, 63)
    result = _mean(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbtimingmean_126d_base_v108_signal(sharesbas, closeadj, pb):
    base = _f32_buyback_timing(sharesbas, closeadj, pb, 126)
    result = _mean(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbtimingmean_252d_base_v109_signal(sharesbas, closeadj, pb):
    base = _f32_buyback_timing(sharesbas, closeadj, pb, 252)
    result = _mean(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbtimingmean_504d_base_v110_signal(sharesbas, closeadj, pb):
    base = _f32_buyback_timing(sharesbas, closeadj, pb, 504)
    result = _mean(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbtimingmean_42d_base_v111_signal(sharesbas, closeadj, pb):
    base = _f32_buyback_timing(sharesbas, closeadj, pb, 42)
    result = _mean(base, 14)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintensstd_21d_base_v112_signal(sharesbas, closeadj):
    base = _f32_buyback_intensity(sharesbas, closeadj, 21)
    result = _std(base, 7)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintensstd_63d_base_v113_signal(sharesbas, closeadj):
    base = _f32_buyback_intensity(sharesbas, closeadj, 63)
    result = _std(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintensstd_126d_base_v114_signal(sharesbas, closeadj):
    base = _f32_buyback_intensity(sharesbas, closeadj, 126)
    result = _std(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintensstd_252d_base_v115_signal(sharesbas, closeadj):
    base = _f32_buyback_intensity(sharesbas, closeadj, 252)
    result = _std(base, 84)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintensstd_504d_base_v116_signal(sharesbas, closeadj):
    base = _f32_buyback_intensity(sharesbas, closeadj, 504)
    result = _std(base, 168)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintensstd_42d_base_v117_signal(sharesbas, closeadj):
    base = _f32_buyback_intensity(sharesbas, closeadj, 42)
    result = _std(base, 14)
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangeinvpb_21d_base_v118_signal(sharesbas, closeadj, pb):
    g = _f32_share_change(sharesbas, 21)
    result = g * (1.0 / (pb.abs() + 0.01)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangeinvpb_63d_base_v119_signal(sharesbas, closeadj, pb):
    g = _f32_share_change(sharesbas, 63)
    result = g * (1.0 / (pb.abs() + 0.01)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangeinvpb_126d_base_v120_signal(sharesbas, closeadj, pb):
    g = _f32_share_change(sharesbas, 126)
    result = g * (1.0 / (pb.abs() + 0.01)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangeinvpb_252d_base_v121_signal(sharesbas, closeadj, pb):
    g = _f32_share_change(sharesbas, 252)
    result = g * (1.0 / (pb.abs() + 0.01)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangeinvpb_504d_base_v122_signal(sharesbas, closeadj, pb):
    g = _f32_share_change(sharesbas, 504)
    result = g * (1.0 / (pb.abs() + 0.01)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangeinvpb_42d_base_v123_signal(sharesbas, closeadj, pb):
    g = _f32_share_change(sharesbas, 42)
    result = g * (1.0 / (pb.abs() + 0.01)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintensxsw_21d_base_v124_signal(sharesbas, shareswa, closeadj):
    base = _f32_buyback_intensity(sharesbas, closeadj, 21)
    result = base * (shareswa / sharesbas.replace(0, np.nan)).abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintensxsw_63d_base_v125_signal(sharesbas, shareswa, closeadj):
    base = _f32_buyback_intensity(sharesbas, closeadj, 63)
    result = base * (shareswa / sharesbas.replace(0, np.nan)).abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintensxsw_126d_base_v126_signal(sharesbas, shareswa, closeadj):
    base = _f32_buyback_intensity(sharesbas, closeadj, 126)
    result = base * (shareswa / sharesbas.replace(0, np.nan)).abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintensxsw_252d_base_v127_signal(sharesbas, shareswa, closeadj):
    base = _f32_buyback_intensity(sharesbas, closeadj, 252)
    result = base * (shareswa / sharesbas.replace(0, np.nan)).abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintensxsw_504d_base_v128_signal(sharesbas, shareswa, closeadj):
    base = _f32_buyback_intensity(sharesbas, closeadj, 504)
    result = base * (shareswa / sharesbas.replace(0, np.nan)).abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbtimingabs_21d_base_v129_signal(sharesbas, closeadj, pb):
    base = _f32_buyback_timing(sharesbas, closeadj, pb, 21)
    result = base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbtimingabs_63d_base_v130_signal(sharesbas, closeadj, pb):
    base = _f32_buyback_timing(sharesbas, closeadj, pb, 63)
    result = base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbtimingabs_126d_base_v131_signal(sharesbas, closeadj, pb):
    base = _f32_buyback_timing(sharesbas, closeadj, pb, 126)
    result = base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbtimingabs_252d_base_v132_signal(sharesbas, closeadj, pb):
    base = _f32_buyback_timing(sharesbas, closeadj, pb, 252)
    result = base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbtimingabs_504d_base_v133_signal(sharesbas, closeadj, pb):
    base = _f32_buyback_timing(sharesbas, closeadj, pb, 504)
    result = base.abs()
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangeema_21d_base_v134_signal(sharesbas, closeadj):
    g = _f32_share_change(sharesbas, 21)
    result = _ema(g, 7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangeema_63d_base_v135_signal(sharesbas, closeadj):
    g = _f32_share_change(sharesbas, 63)
    result = _ema(g, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangeema_126d_base_v136_signal(sharesbas, closeadj):
    g = _f32_share_change(sharesbas, 126)
    result = _ema(g, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangeema_252d_base_v137_signal(sharesbas, closeadj):
    g = _f32_share_change(sharesbas, 252)
    result = _ema(g, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangeema_504d_base_v138_signal(sharesbas, closeadj):
    g = _f32_share_change(sharesbas, 504)
    result = _ema(g, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintensxpb2_21d_base_v139_signal(sharesbas, closeadj, pb):
    base = _f32_buyback_intensity(sharesbas, closeadj, 21)
    result = base * pb * pb
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintensxpb2_63d_base_v140_signal(sharesbas, closeadj, pb):
    base = _f32_buyback_intensity(sharesbas, closeadj, 63)
    result = base * pb * pb
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintensxpb2_126d_base_v141_signal(sharesbas, closeadj, pb):
    base = _f32_buyback_intensity(sharesbas, closeadj, 126)
    result = base * pb * pb
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintensxpb2_252d_base_v142_signal(sharesbas, closeadj, pb):
    base = _f32_buyback_intensity(sharesbas, closeadj, 252)
    result = base * pb * pb
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintensxpb2_504d_base_v143_signal(sharesbas, closeadj, pb):
    base = _f32_buyback_intensity(sharesbas, closeadj, 504)
    result = base * pb * pb
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_bbintensxpb2_42d_base_v144_signal(sharesbas, closeadj, pb):
    base = _f32_buyback_intensity(sharesbas, closeadj, 42)
    result = base * pb * pb
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangeqrankinv_21d_base_v145_signal(sharesbas, closeadj):
    g = _f32_share_change(sharesbas, 21)
    result = (1.0 - _qrank(g, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangeqrankinv_63d_base_v146_signal(sharesbas, closeadj):
    g = _f32_share_change(sharesbas, 63)
    result = (1.0 - _qrank(g, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangeqrankinv_126d_base_v147_signal(sharesbas, closeadj):
    g = _f32_share_change(sharesbas, 126)
    result = (1.0 - _qrank(g, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangeqrankinv_252d_base_v148_signal(sharesbas, closeadj):
    g = _f32_share_change(sharesbas, 252)
    result = (1.0 - _qrank(g, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangeqrankinv_504d_base_v149_signal(sharesbas, closeadj):
    g = _f32_share_change(sharesbas, 504)
    result = (1.0 - _qrank(g, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f32beb_f32_buyback_efficiency_bank_sharechangeqrankinv_42d_base_v150_signal(sharesbas, closeadj):
    g = _f32_share_change(sharesbas, 42)
    result = (1.0 - _qrank(g, 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f32beb_f32_buyback_efficiency_bank_bbintensxpb_5d_base_v076_signal,
    f32beb_f32_buyback_efficiency_bank_bbintensxpb_10d_base_v077_signal,
    f32beb_f32_buyback_efficiency_bank_bbintensxpb_21d_base_v078_signal,
    f32beb_f32_buyback_efficiency_bank_bbintensxpb_42d_base_v079_signal,
    f32beb_f32_buyback_efficiency_bank_bbintensxpb_63d_base_v080_signal,
    f32beb_f32_buyback_efficiency_bank_bbintensxpb_126d_base_v081_signal,
    f32beb_f32_buyback_efficiency_bank_bbintensxpb_189d_base_v082_signal,
    f32beb_f32_buyback_efficiency_bank_bbintensxpb_252d_base_v083_signal,
    f32beb_f32_buyback_efficiency_bank_bbintensxpb_378d_base_v084_signal,
    f32beb_f32_buyback_efficiency_bank_bbintensxpb_504d_base_v085_signal,
    f32beb_f32_buyback_efficiency_bank_bbtimingz_21d_base_v086_signal,
    f32beb_f32_buyback_efficiency_bank_bbtimingz_42d_base_v087_signal,
    f32beb_f32_buyback_efficiency_bank_bbtimingz_63d_base_v088_signal,
    f32beb_f32_buyback_efficiency_bank_bbtimingz_126d_base_v089_signal,
    f32beb_f32_buyback_efficiency_bank_bbtimingz_189d_base_v090_signal,
    f32beb_f32_buyback_efficiency_bank_bbtimingz_252d_base_v091_signal,
    f32beb_f32_buyback_efficiency_bank_bbtimingz_378d_base_v092_signal,
    f32beb_f32_buyback_efficiency_bank_bbtimingz_504d_base_v093_signal,
    f32beb_f32_buyback_efficiency_bank_bbintensqrank_63d_base_v094_signal,
    f32beb_f32_buyback_efficiency_bank_bbintensqrank_126d_base_v095_signal,
    f32beb_f32_buyback_efficiency_bank_bbintensqrank_252d_base_v096_signal,
    f32beb_f32_buyback_efficiency_bank_bbintensqrank_504d_base_v097_signal,
    f32beb_f32_buyback_efficiency_bank_bbintensqrank_21d_base_v098_signal,
    f32beb_f32_buyback_efficiency_bank_bbintensqrank_42d_base_v099_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangexc2_21d_base_v100_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangexc2_63d_base_v101_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangexc2_126d_base_v102_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangexc2_252d_base_v103_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangexc2_504d_base_v104_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangexc2_42d_base_v105_signal,
    f32beb_f32_buyback_efficiency_bank_bbtimingmean_21d_base_v106_signal,
    f32beb_f32_buyback_efficiency_bank_bbtimingmean_63d_base_v107_signal,
    f32beb_f32_buyback_efficiency_bank_bbtimingmean_126d_base_v108_signal,
    f32beb_f32_buyback_efficiency_bank_bbtimingmean_252d_base_v109_signal,
    f32beb_f32_buyback_efficiency_bank_bbtimingmean_504d_base_v110_signal,
    f32beb_f32_buyback_efficiency_bank_bbtimingmean_42d_base_v111_signal,
    f32beb_f32_buyback_efficiency_bank_bbintensstd_21d_base_v112_signal,
    f32beb_f32_buyback_efficiency_bank_bbintensstd_63d_base_v113_signal,
    f32beb_f32_buyback_efficiency_bank_bbintensstd_126d_base_v114_signal,
    f32beb_f32_buyback_efficiency_bank_bbintensstd_252d_base_v115_signal,
    f32beb_f32_buyback_efficiency_bank_bbintensstd_504d_base_v116_signal,
    f32beb_f32_buyback_efficiency_bank_bbintensstd_42d_base_v117_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangeinvpb_21d_base_v118_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangeinvpb_63d_base_v119_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangeinvpb_126d_base_v120_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangeinvpb_252d_base_v121_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangeinvpb_504d_base_v122_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangeinvpb_42d_base_v123_signal,
    f32beb_f32_buyback_efficiency_bank_bbintensxsw_21d_base_v124_signal,
    f32beb_f32_buyback_efficiency_bank_bbintensxsw_63d_base_v125_signal,
    f32beb_f32_buyback_efficiency_bank_bbintensxsw_126d_base_v126_signal,
    f32beb_f32_buyback_efficiency_bank_bbintensxsw_252d_base_v127_signal,
    f32beb_f32_buyback_efficiency_bank_bbintensxsw_504d_base_v128_signal,
    f32beb_f32_buyback_efficiency_bank_bbtimingabs_21d_base_v129_signal,
    f32beb_f32_buyback_efficiency_bank_bbtimingabs_63d_base_v130_signal,
    f32beb_f32_buyback_efficiency_bank_bbtimingabs_126d_base_v131_signal,
    f32beb_f32_buyback_efficiency_bank_bbtimingabs_252d_base_v132_signal,
    f32beb_f32_buyback_efficiency_bank_bbtimingabs_504d_base_v133_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangeema_21d_base_v134_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangeema_63d_base_v135_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangeema_126d_base_v136_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangeema_252d_base_v137_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangeema_504d_base_v138_signal,
    f32beb_f32_buyback_efficiency_bank_bbintensxpb2_21d_base_v139_signal,
    f32beb_f32_buyback_efficiency_bank_bbintensxpb2_63d_base_v140_signal,
    f32beb_f32_buyback_efficiency_bank_bbintensxpb2_126d_base_v141_signal,
    f32beb_f32_buyback_efficiency_bank_bbintensxpb2_252d_base_v142_signal,
    f32beb_f32_buyback_efficiency_bank_bbintensxpb2_504d_base_v143_signal,
    f32beb_f32_buyback_efficiency_bank_bbintensxpb2_42d_base_v144_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangeqrankinv_21d_base_v145_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangeqrankinv_63d_base_v146_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangeqrankinv_126d_base_v147_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangeqrankinv_252d_base_v148_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangeqrankinv_504d_base_v149_signal,
    f32beb_f32_buyback_efficiency_bank_sharechangeqrankinv_42d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F32_BUYBACK_EFFICIENCY_BANK_REGISTRY_076_150 = REGISTRY



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
    domain_primitives = ("_f32_share_change", "_f32_buyback_intensity", "_f32_buyback_timing",)
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
    print(f"OK f32_buyback_efficiency_bank_base_076_150_claude: {n_features} features pass")
