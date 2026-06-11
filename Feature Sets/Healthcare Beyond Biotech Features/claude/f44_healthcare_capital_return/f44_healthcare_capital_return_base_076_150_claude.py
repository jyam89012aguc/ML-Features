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
def _f44_dps_growth(dps, w):
    base = _mean(dps, max(2, w // 4))
    return base.pct_change(periods=w)


def _f44_share_buyback_intensity(sharesbas, w):
    base = _mean(sharesbas, max(2, w // 4))
    return -base.pct_change(periods=w)


def _f44_total_return_quality(dps, sharesbas, w):
    dg = _mean(dps, max(2, w // 4)).pct_change(periods=w)
    bb = -_mean(sharesbas, max(2, w // 4)).pct_change(periods=w)
    return dg + bb

# v076: dpsg_5d_alt
def f44hcr_f44_healthcare_capital_return_dpsg_5d_alt_base_v076_signal(dps, closeadj):
    result = _f44_dps_growth(dps, 5) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v077: dpsg_10d_alt
def f44hcr_f44_healthcare_capital_return_dpsg_10d_alt_base_v077_signal(dps, closeadj):
    result = _f44_dps_growth(dps, 10) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v078: dpsg_42d_alt
def f44hcr_f44_healthcare_capital_return_dpsg_42d_alt_base_v078_signal(dps, closeadj):
    result = _f44_dps_growth(dps, 42) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v079: dpsg_189d_alt
def f44hcr_f44_healthcare_capital_return_dpsg_189d_alt_base_v079_signal(dps, closeadj):
    result = _f44_dps_growth(dps, 189) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v080: dpsg_378d_alt
def f44hcr_f44_healthcare_capital_return_dpsg_378d_alt_base_v080_signal(dps, closeadj):
    result = _f44_dps_growth(dps, 378) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v081: bb_5d_alt
def f44hcr_f44_healthcare_capital_return_bb_5d_alt_base_v081_signal(sharesbas, closeadj):
    result = _f44_share_buyback_intensity(sharesbas, 5) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v082: bb_10d_alt
def f44hcr_f44_healthcare_capital_return_bb_10d_alt_base_v082_signal(sharesbas, closeadj):
    result = _f44_share_buyback_intensity(sharesbas, 10) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v083: bb_42d_alt
def f44hcr_f44_healthcare_capital_return_bb_42d_alt_base_v083_signal(sharesbas, closeadj):
    result = _f44_share_buyback_intensity(sharesbas, 42) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v084: bb_189d_alt
def f44hcr_f44_healthcare_capital_return_bb_189d_alt_base_v084_signal(sharesbas, closeadj):
    result = _f44_share_buyback_intensity(sharesbas, 189) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v085: dpsglog_21d
def f44hcr_f44_healthcare_capital_return_dpsglog_21d_base_v085_signal(dps, closeadj):
    result = np.sign(_f44_dps_growth(dps, 21)) * np.log1p(_f44_dps_growth(dps, 21).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v086: dpsglog_63d
def f44hcr_f44_healthcare_capital_return_dpsglog_63d_base_v086_signal(dps, closeadj):
    result = np.sign(_f44_dps_growth(dps, 63)) * np.log1p(_f44_dps_growth(dps, 63).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v087: dpsglog_252d
def f44hcr_f44_healthcare_capital_return_dpsglog_252d_base_v087_signal(dps, closeadj):
    result = np.sign(_f44_dps_growth(dps, 252)) * np.log1p(_f44_dps_growth(dps, 252).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v088: bblog_21d
def f44hcr_f44_healthcare_capital_return_bblog_21d_base_v088_signal(sharesbas, closeadj):
    result = np.sign(_f44_share_buyback_intensity(sharesbas, 21)) * np.log1p(_f44_share_buyback_intensity(sharesbas, 21).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v089: bblog_63d
def f44hcr_f44_healthcare_capital_return_bblog_63d_base_v089_signal(sharesbas, closeadj):
    result = np.sign(_f44_share_buyback_intensity(sharesbas, 63)) * np.log1p(_f44_share_buyback_intensity(sharesbas, 63).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v090: bblog_252d
def f44hcr_f44_healthcare_capital_return_bblog_252d_base_v090_signal(sharesbas, closeadj):
    result = np.sign(_f44_share_buyback_intensity(sharesbas, 252)) * np.log1p(_f44_share_buyback_intensity(sharesbas, 252).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v091: trqlog_21d
def f44hcr_f44_healthcare_capital_return_trqlog_21d_base_v091_signal(dps, sharesbas, closeadj):
    result = np.sign(_f44_total_return_quality(dps, sharesbas, 21)) * np.log1p(_f44_total_return_quality(dps, sharesbas, 21).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v092: trqlog_63d
def f44hcr_f44_healthcare_capital_return_trqlog_63d_base_v092_signal(dps, sharesbas, closeadj):
    result = np.sign(_f44_total_return_quality(dps, sharesbas, 63)) * np.log1p(_f44_total_return_quality(dps, sharesbas, 63).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v093: trqlog_252d
def f44hcr_f44_healthcare_capital_return_trqlog_252d_base_v093_signal(dps, sharesbas, closeadj):
    result = np.sign(_f44_total_return_quality(dps, sharesbas, 252)) * np.log1p(_f44_total_return_quality(dps, sharesbas, 252).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v094: dpsgx_21x63
def f44hcr_f44_healthcare_capital_return_dpsgx_21x63_base_v094_signal(dps, closeadj):
    result = _f44_dps_growth(dps, 21) * _f44_dps_growth(dps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v095: dpsgx_21x252
def f44hcr_f44_healthcare_capital_return_dpsgx_21x252_base_v095_signal(dps, closeadj):
    result = _f44_dps_growth(dps, 21) * _f44_dps_growth(dps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v096: dpsgx_63x252
def f44hcr_f44_healthcare_capital_return_dpsgx_63x252_base_v096_signal(dps, closeadj):
    result = _f44_dps_growth(dps, 63) * _f44_dps_growth(dps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v097: dpsgx_63x504
def f44hcr_f44_healthcare_capital_return_dpsgx_63x504_base_v097_signal(dps, closeadj):
    result = _f44_dps_growth(dps, 63) * _f44_dps_growth(dps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v098: dpsgx_126x504
def f44hcr_f44_healthcare_capital_return_dpsgx_126x504_base_v098_signal(dps, closeadj):
    result = _f44_dps_growth(dps, 126) * _f44_dps_growth(dps, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v099: bbx_21x63
def f44hcr_f44_healthcare_capital_return_bbx_21x63_base_v099_signal(sharesbas, closeadj):
    result = _f44_share_buyback_intensity(sharesbas, 21) * _f44_share_buyback_intensity(sharesbas, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v100: bbx_21x252
def f44hcr_f44_healthcare_capital_return_bbx_21x252_base_v100_signal(sharesbas, closeadj):
    result = _f44_share_buyback_intensity(sharesbas, 21) * _f44_share_buyback_intensity(sharesbas, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v101: bbx_63x252
def f44hcr_f44_healthcare_capital_return_bbx_63x252_base_v101_signal(sharesbas, closeadj):
    result = _f44_share_buyback_intensity(sharesbas, 63) * _f44_share_buyback_intensity(sharesbas, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v102: bbx_63x504
def f44hcr_f44_healthcare_capital_return_bbx_63x504_base_v102_signal(sharesbas, closeadj):
    result = _f44_share_buyback_intensity(sharesbas, 63) * _f44_share_buyback_intensity(sharesbas, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v103: bbx_126x504
def f44hcr_f44_healthcare_capital_return_bbx_126x504_base_v103_signal(sharesbas, closeadj):
    result = _f44_share_buyback_intensity(sharesbas, 126) * _f44_share_buyback_intensity(sharesbas, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v104: trqx_21x63
def f44hcr_f44_healthcare_capital_return_trqx_21x63_base_v104_signal(dps, sharesbas, closeadj):
    result = _f44_total_return_quality(dps, sharesbas, 21) * _f44_total_return_quality(dps, sharesbas, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v105: trqx_21x252
def f44hcr_f44_healthcare_capital_return_trqx_21x252_base_v105_signal(dps, sharesbas, closeadj):
    result = _f44_total_return_quality(dps, sharesbas, 21) * _f44_total_return_quality(dps, sharesbas, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v106: trqx_63x252
def f44hcr_f44_healthcare_capital_return_trqx_63x252_base_v106_signal(dps, sharesbas, closeadj):
    result = _f44_total_return_quality(dps, sharesbas, 63) * _f44_total_return_quality(dps, sharesbas, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v107: trqx_63x504
def f44hcr_f44_healthcare_capital_return_trqx_63x504_base_v107_signal(dps, sharesbas, closeadj):
    result = _f44_total_return_quality(dps, sharesbas, 63) * _f44_total_return_quality(dps, sharesbas, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v108: trqx_126x504
def f44hcr_f44_healthcare_capital_return_trqx_126x504_base_v108_signal(dps, sharesbas, closeadj):
    result = _f44_total_return_quality(dps, sharesbas, 126) * _f44_total_return_quality(dps, sharesbas, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v109: dpsgtri_2163252
def f44hcr_f44_healthcare_capital_return_dpsgtri_2163252_base_v109_signal(dps, closeadj):
    result = (_f44_dps_growth(dps, 21) + _f44_dps_growth(dps, 63) + _f44_dps_growth(dps, 252)) * closeadj / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# v110: dpsgtri_63126252
def f44hcr_f44_healthcare_capital_return_dpsgtri_63126252_base_v110_signal(dps, closeadj):
    result = (_f44_dps_growth(dps, 63) + _f44_dps_growth(dps, 126) + _f44_dps_growth(dps, 252)) * closeadj / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# v111: dpsgtri_126252504
def f44hcr_f44_healthcare_capital_return_dpsgtri_126252504_base_v111_signal(dps, closeadj):
    result = (_f44_dps_growth(dps, 126) + _f44_dps_growth(dps, 252) + _f44_dps_growth(dps, 504)) * closeadj / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# v112: bbtri_2163252
def f44hcr_f44_healthcare_capital_return_bbtri_2163252_base_v112_signal(sharesbas, closeadj):
    result = (_f44_share_buyback_intensity(sharesbas, 21) + _f44_share_buyback_intensity(sharesbas, 63) + _f44_share_buyback_intensity(sharesbas, 252)) * closeadj / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# v113: bbtri_63126252
def f44hcr_f44_healthcare_capital_return_bbtri_63126252_base_v113_signal(sharesbas, closeadj):
    result = (_f44_share_buyback_intensity(sharesbas, 63) + _f44_share_buyback_intensity(sharesbas, 126) + _f44_share_buyback_intensity(sharesbas, 252)) * closeadj / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# v114: bbtri_126252504
def f44hcr_f44_healthcare_capital_return_bbtri_126252504_base_v114_signal(sharesbas, closeadj):
    result = (_f44_share_buyback_intensity(sharesbas, 126) + _f44_share_buyback_intensity(sharesbas, 252) + _f44_share_buyback_intensity(sharesbas, 504)) * closeadj / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# v115: trqtri_2163252
def f44hcr_f44_healthcare_capital_return_trqtri_2163252_base_v115_signal(dps, sharesbas, closeadj):
    result = (_f44_total_return_quality(dps, sharesbas, 21) + _f44_total_return_quality(dps, sharesbas, 63) + _f44_total_return_quality(dps, sharesbas, 252)) * closeadj / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# v116: trqtri_63126252
def f44hcr_f44_healthcare_capital_return_trqtri_63126252_base_v116_signal(dps, sharesbas, closeadj):
    result = (_f44_total_return_quality(dps, sharesbas, 63) + _f44_total_return_quality(dps, sharesbas, 126) + _f44_total_return_quality(dps, sharesbas, 252)) * closeadj / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# v117: trqtri_126252504
def f44hcr_f44_healthcare_capital_return_trqtri_126252504_base_v117_signal(dps, sharesbas, closeadj):
    result = (_f44_total_return_quality(dps, sharesbas, 126) + _f44_total_return_quality(dps, sharesbas, 252) + _f44_total_return_quality(dps, sharesbas, 504)) * closeadj / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# v118: dpsgdiff_21_21
def f44hcr_f44_healthcare_capital_return_dpsgdiff_21_21_base_v118_signal(dps, closeadj):
    result = (_f44_dps_growth(dps, 21) - _f44_dps_growth(dps, 21).shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v119: dpsgdiff_63_63
def f44hcr_f44_healthcare_capital_return_dpsgdiff_63_63_base_v119_signal(dps, closeadj):
    result = (_f44_dps_growth(dps, 63) - _f44_dps_growth(dps, 63).shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v120: dpsgdiff_252_63
def f44hcr_f44_healthcare_capital_return_dpsgdiff_252_63_base_v120_signal(dps, closeadj):
    result = (_f44_dps_growth(dps, 252) - _f44_dps_growth(dps, 252).shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v121: bbdiff_21_21
def f44hcr_f44_healthcare_capital_return_bbdiff_21_21_base_v121_signal(sharesbas, closeadj):
    result = (_f44_share_buyback_intensity(sharesbas, 21) - _f44_share_buyback_intensity(sharesbas, 21).shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v122: bbdiff_63_63
def f44hcr_f44_healthcare_capital_return_bbdiff_63_63_base_v122_signal(sharesbas, closeadj):
    result = (_f44_share_buyback_intensity(sharesbas, 63) - _f44_share_buyback_intensity(sharesbas, 63).shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v123: bbdiff_252_63
def f44hcr_f44_healthcare_capital_return_bbdiff_252_63_base_v123_signal(sharesbas, closeadj):
    result = (_f44_share_buyback_intensity(sharesbas, 252) - _f44_share_buyback_intensity(sharesbas, 252).shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v124: trqdiff_21_21
def f44hcr_f44_healthcare_capital_return_trqdiff_21_21_base_v124_signal(dps, sharesbas, closeadj):
    result = (_f44_total_return_quality(dps, sharesbas, 21) - _f44_total_return_quality(dps, sharesbas, 21).shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v125: trqdiff_63_63
def f44hcr_f44_healthcare_capital_return_trqdiff_63_63_base_v125_signal(dps, sharesbas, closeadj):
    result = (_f44_total_return_quality(dps, sharesbas, 63) - _f44_total_return_quality(dps, sharesbas, 63).shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v126: trqdiff_252_63
def f44hcr_f44_healthcare_capital_return_trqdiff_252_63_base_v126_signal(dps, sharesbas, closeadj):
    result = (_f44_total_return_quality(dps, sharesbas, 252) - _f44_total_return_quality(dps, sharesbas, 252).shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v127: dpsgxprice2_21d
def f44hcr_f44_healthcare_capital_return_dpsgxprice2_21d_base_v127_signal(dps, closeadj):
    result = _f44_dps_growth(dps, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v128: dpsgxprice2_63d
def f44hcr_f44_healthcare_capital_return_dpsgxprice2_63d_base_v128_signal(dps, closeadj):
    result = _f44_dps_growth(dps, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v129: dpsgxprice2_252d
def f44hcr_f44_healthcare_capital_return_dpsgxprice2_252d_base_v129_signal(dps, closeadj):
    result = _f44_dps_growth(dps, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v130: bbxprice2_21d
def f44hcr_f44_healthcare_capital_return_bbxprice2_21d_base_v130_signal(sharesbas, closeadj):
    result = _f44_share_buyback_intensity(sharesbas, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v131: bbxprice2_63d
def f44hcr_f44_healthcare_capital_return_bbxprice2_63d_base_v131_signal(sharesbas, closeadj):
    result = _f44_share_buyback_intensity(sharesbas, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v132: bbxprice2_252d
def f44hcr_f44_healthcare_capital_return_bbxprice2_252d_base_v132_signal(sharesbas, closeadj):
    result = _f44_share_buyback_intensity(sharesbas, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v133: trqxprice2_21d
def f44hcr_f44_healthcare_capital_return_trqxprice2_21d_base_v133_signal(dps, sharesbas, closeadj):
    result = _f44_total_return_quality(dps, sharesbas, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v134: trqxprice2_63d
def f44hcr_f44_healthcare_capital_return_trqxprice2_63d_base_v134_signal(dps, sharesbas, closeadj):
    result = _f44_total_return_quality(dps, sharesbas, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v135: trqxprice2_252d
def f44hcr_f44_healthcare_capital_return_trqxprice2_252d_base_v135_signal(dps, sharesbas, closeadj):
    result = _f44_total_return_quality(dps, sharesbas, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v136: dpsgshift_21d
def f44hcr_f44_healthcare_capital_return_dpsgshift_21d_base_v136_signal(dps, closeadj):
    result = _f44_dps_growth(dps, 21).shift(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v137: dpsgshift_63d
def f44hcr_f44_healthcare_capital_return_dpsgshift_63d_base_v137_signal(dps, closeadj):
    result = _f44_dps_growth(dps, 63).shift(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v138: dpsgshift_252d
def f44hcr_f44_healthcare_capital_return_dpsgshift_252d_base_v138_signal(dps, closeadj):
    result = _f44_dps_growth(dps, 252).shift(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v139: trq_5d_alt
def f44hcr_f44_healthcare_capital_return_trq_5d_alt_base_v139_signal(dps, sharesbas, closeadj):
    result = _f44_total_return_quality(dps, sharesbas, 5) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v140: trq_10d_alt
def f44hcr_f44_healthcare_capital_return_trq_10d_alt_base_v140_signal(dps, sharesbas, closeadj):
    result = _f44_total_return_quality(dps, sharesbas, 10) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v141: trq_42d_alt
def f44hcr_f44_healthcare_capital_return_trq_42d_alt_base_v141_signal(dps, sharesbas, closeadj):
    result = _f44_total_return_quality(dps, sharesbas, 42) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v142: trq_189d_alt
def f44hcr_f44_healthcare_capital_return_trq_189d_alt_base_v142_signal(dps, sharesbas, closeadj):
    result = _f44_total_return_quality(dps, sharesbas, 189) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v143: trq_378d_alt
def f44hcr_f44_healthcare_capital_return_trq_378d_alt_base_v143_signal(dps, sharesbas, closeadj):
    result = _f44_total_return_quality(dps, sharesbas, 378) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v144: dpsgpos_21d
def f44hcr_f44_healthcare_capital_return_dpsgpos_21d_base_v144_signal(dps, closeadj):
    result = _f44_dps_growth(dps, 21).clip(lower=0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v145: dpsgpos_63d
def f44hcr_f44_healthcare_capital_return_dpsgpos_63d_base_v145_signal(dps, closeadj):
    result = _f44_dps_growth(dps, 63).clip(lower=0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v146: dpsgpos_252d
def f44hcr_f44_healthcare_capital_return_dpsgpos_252d_base_v146_signal(dps, closeadj):
    result = _f44_dps_growth(dps, 252).clip(lower=0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v147: bbpos_21d
def f44hcr_f44_healthcare_capital_return_bbpos_21d_base_v147_signal(sharesbas, closeadj):
    result = _f44_share_buyback_intensity(sharesbas, 21).clip(lower=0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v148: bbpos_63d
def f44hcr_f44_healthcare_capital_return_bbpos_63d_base_v148_signal(sharesbas, closeadj):
    result = _f44_share_buyback_intensity(sharesbas, 63).clip(lower=0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v149: bbpos_252d
def f44hcr_f44_healthcare_capital_return_bbpos_252d_base_v149_signal(sharesbas, closeadj):
    result = _f44_share_buyback_intensity(sharesbas, 252).clip(lower=0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v150: dpsxbb_504d
def f44hcr_f44_healthcare_capital_return_dpsxbb_504d_base_v150_signal(dps, sharesbas, closeadj):
    result = _f44_dps_growth(dps, 504) * _f44_share_buyback_intensity(sharesbas, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f44hcr_f44_healthcare_capital_return_dpsg_5d_alt_base_v076_signal,
    f44hcr_f44_healthcare_capital_return_dpsg_10d_alt_base_v077_signal,
    f44hcr_f44_healthcare_capital_return_dpsg_42d_alt_base_v078_signal,
    f44hcr_f44_healthcare_capital_return_dpsg_189d_alt_base_v079_signal,
    f44hcr_f44_healthcare_capital_return_dpsg_378d_alt_base_v080_signal,
    f44hcr_f44_healthcare_capital_return_bb_5d_alt_base_v081_signal,
    f44hcr_f44_healthcare_capital_return_bb_10d_alt_base_v082_signal,
    f44hcr_f44_healthcare_capital_return_bb_42d_alt_base_v083_signal,
    f44hcr_f44_healthcare_capital_return_bb_189d_alt_base_v084_signal,
    f44hcr_f44_healthcare_capital_return_dpsglog_21d_base_v085_signal,
    f44hcr_f44_healthcare_capital_return_dpsglog_63d_base_v086_signal,
    f44hcr_f44_healthcare_capital_return_dpsglog_252d_base_v087_signal,
    f44hcr_f44_healthcare_capital_return_bblog_21d_base_v088_signal,
    f44hcr_f44_healthcare_capital_return_bblog_63d_base_v089_signal,
    f44hcr_f44_healthcare_capital_return_bblog_252d_base_v090_signal,
    f44hcr_f44_healthcare_capital_return_trqlog_21d_base_v091_signal,
    f44hcr_f44_healthcare_capital_return_trqlog_63d_base_v092_signal,
    f44hcr_f44_healthcare_capital_return_trqlog_252d_base_v093_signal,
    f44hcr_f44_healthcare_capital_return_dpsgx_21x63_base_v094_signal,
    f44hcr_f44_healthcare_capital_return_dpsgx_21x252_base_v095_signal,
    f44hcr_f44_healthcare_capital_return_dpsgx_63x252_base_v096_signal,
    f44hcr_f44_healthcare_capital_return_dpsgx_63x504_base_v097_signal,
    f44hcr_f44_healthcare_capital_return_dpsgx_126x504_base_v098_signal,
    f44hcr_f44_healthcare_capital_return_bbx_21x63_base_v099_signal,
    f44hcr_f44_healthcare_capital_return_bbx_21x252_base_v100_signal,
    f44hcr_f44_healthcare_capital_return_bbx_63x252_base_v101_signal,
    f44hcr_f44_healthcare_capital_return_bbx_63x504_base_v102_signal,
    f44hcr_f44_healthcare_capital_return_bbx_126x504_base_v103_signal,
    f44hcr_f44_healthcare_capital_return_trqx_21x63_base_v104_signal,
    f44hcr_f44_healthcare_capital_return_trqx_21x252_base_v105_signal,
    f44hcr_f44_healthcare_capital_return_trqx_63x252_base_v106_signal,
    f44hcr_f44_healthcare_capital_return_trqx_63x504_base_v107_signal,
    f44hcr_f44_healthcare_capital_return_trqx_126x504_base_v108_signal,
    f44hcr_f44_healthcare_capital_return_dpsgtri_2163252_base_v109_signal,
    f44hcr_f44_healthcare_capital_return_dpsgtri_63126252_base_v110_signal,
    f44hcr_f44_healthcare_capital_return_dpsgtri_126252504_base_v111_signal,
    f44hcr_f44_healthcare_capital_return_bbtri_2163252_base_v112_signal,
    f44hcr_f44_healthcare_capital_return_bbtri_63126252_base_v113_signal,
    f44hcr_f44_healthcare_capital_return_bbtri_126252504_base_v114_signal,
    f44hcr_f44_healthcare_capital_return_trqtri_2163252_base_v115_signal,
    f44hcr_f44_healthcare_capital_return_trqtri_63126252_base_v116_signal,
    f44hcr_f44_healthcare_capital_return_trqtri_126252504_base_v117_signal,
    f44hcr_f44_healthcare_capital_return_dpsgdiff_21_21_base_v118_signal,
    f44hcr_f44_healthcare_capital_return_dpsgdiff_63_63_base_v119_signal,
    f44hcr_f44_healthcare_capital_return_dpsgdiff_252_63_base_v120_signal,
    f44hcr_f44_healthcare_capital_return_bbdiff_21_21_base_v121_signal,
    f44hcr_f44_healthcare_capital_return_bbdiff_63_63_base_v122_signal,
    f44hcr_f44_healthcare_capital_return_bbdiff_252_63_base_v123_signal,
    f44hcr_f44_healthcare_capital_return_trqdiff_21_21_base_v124_signal,
    f44hcr_f44_healthcare_capital_return_trqdiff_63_63_base_v125_signal,
    f44hcr_f44_healthcare_capital_return_trqdiff_252_63_base_v126_signal,
    f44hcr_f44_healthcare_capital_return_dpsgxprice2_21d_base_v127_signal,
    f44hcr_f44_healthcare_capital_return_dpsgxprice2_63d_base_v128_signal,
    f44hcr_f44_healthcare_capital_return_dpsgxprice2_252d_base_v129_signal,
    f44hcr_f44_healthcare_capital_return_bbxprice2_21d_base_v130_signal,
    f44hcr_f44_healthcare_capital_return_bbxprice2_63d_base_v131_signal,
    f44hcr_f44_healthcare_capital_return_bbxprice2_252d_base_v132_signal,
    f44hcr_f44_healthcare_capital_return_trqxprice2_21d_base_v133_signal,
    f44hcr_f44_healthcare_capital_return_trqxprice2_63d_base_v134_signal,
    f44hcr_f44_healthcare_capital_return_trqxprice2_252d_base_v135_signal,
    f44hcr_f44_healthcare_capital_return_dpsgshift_21d_base_v136_signal,
    f44hcr_f44_healthcare_capital_return_dpsgshift_63d_base_v137_signal,
    f44hcr_f44_healthcare_capital_return_dpsgshift_252d_base_v138_signal,
    f44hcr_f44_healthcare_capital_return_trq_5d_alt_base_v139_signal,
    f44hcr_f44_healthcare_capital_return_trq_10d_alt_base_v140_signal,
    f44hcr_f44_healthcare_capital_return_trq_42d_alt_base_v141_signal,
    f44hcr_f44_healthcare_capital_return_trq_189d_alt_base_v142_signal,
    f44hcr_f44_healthcare_capital_return_trq_378d_alt_base_v143_signal,
    f44hcr_f44_healthcare_capital_return_dpsgpos_21d_base_v144_signal,
    f44hcr_f44_healthcare_capital_return_dpsgpos_63d_base_v145_signal,
    f44hcr_f44_healthcare_capital_return_dpsgpos_252d_base_v146_signal,
    f44hcr_f44_healthcare_capital_return_bbpos_21d_base_v147_signal,
    f44hcr_f44_healthcare_capital_return_bbpos_63d_base_v148_signal,
    f44hcr_f44_healthcare_capital_return_bbpos_252d_base_v149_signal,
    f44hcr_f44_healthcare_capital_return_dpsxbb_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F44_HEALTHCARE_CAPITAL_RETURN_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    dps = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    eps = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")

    cols = {
        "closeadj": closeadj,
        "dps": dps,
        "eps": eps,
        "sharesbas": sharesbas,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f44_dps_growth', '_f44_share_buyback_intensity', '_f44_total_return_quality',)
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
    print(f"OK f44_healthcare_capital_return_base_076_150_claude: {n_features} features pass")
