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


def _f40_payout_floor(payoutratio, w):
    return payoutratio.rolling(w, min_periods=max(1, w // 2)).min()



def _f40_payout_durability(payoutratio, eps, w):
    cap = 1.0 - payoutratio
    eps_g = eps.pct_change(periods=w).fillna(0.0)
    return cap.rolling(w, min_periods=max(1, w // 2)).mean() + eps_g



def _f40_payout_sustainability(payoutratio, fcfps, w):
    cover = fcfps / payoutratio.replace(0, np.nan).abs()
    return cover.rolling(w, min_periods=max(1, w // 2)).mean()


# ===== features =====


def f40epd_f40_energy_payout_durability_payout_floor_signxclosediff_252d_base_v076_signal(payoutratio, closeadj):
    result = (np.sign(_f40_payout_floor(payoutratio, 252))) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_absxclose_252d_base_v077_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 252)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_absxclose2_252d_base_v078_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 252)).abs()) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_absxclosem_252d_base_v079_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 252)).abs()) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_absxclosem63_252d_base_v080_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 252)).abs()) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_absxclosez_252d_base_v081_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 252)).abs()) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_absxclosechg_252d_base_v082_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 252)).abs()) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_absxclosediff_252d_base_v083_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 252)).abs()) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_idxclose_378d_base_v084_signal(payoutratio, closeadj):
    result = (_f40_payout_floor(payoutratio, 378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_idxclose2_378d_base_v085_signal(payoutratio, closeadj):
    result = (_f40_payout_floor(payoutratio, 378)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_idxclosem_378d_base_v086_signal(payoutratio, closeadj):
    result = (_f40_payout_floor(payoutratio, 378)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_idxclosem63_378d_base_v087_signal(payoutratio, closeadj):
    result = (_f40_payout_floor(payoutratio, 378)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_idxclosez_378d_base_v088_signal(payoutratio, closeadj):
    result = (_f40_payout_floor(payoutratio, 378)) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_idxclosechg_378d_base_v089_signal(payoutratio, closeadj):
    result = (_f40_payout_floor(payoutratio, 378)) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_idxclosediff_378d_base_v090_signal(payoutratio, closeadj):
    result = (_f40_payout_floor(payoutratio, 378)) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_meanxclose_378d_base_v091_signal(payoutratio, closeadj):
    result = (_mean(_f40_payout_floor(payoutratio, 378), 378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_meanxclose2_378d_base_v092_signal(payoutratio, closeadj):
    result = (_mean(_f40_payout_floor(payoutratio, 378), 378)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_meanxclosem_378d_base_v093_signal(payoutratio, closeadj):
    result = (_mean(_f40_payout_floor(payoutratio, 378), 378)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_meanxclosem63_378d_base_v094_signal(payoutratio, closeadj):
    result = (_mean(_f40_payout_floor(payoutratio, 378), 378)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_meanxclosez_378d_base_v095_signal(payoutratio, closeadj):
    result = (_mean(_f40_payout_floor(payoutratio, 378), 378)) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_meanxclosechg_378d_base_v096_signal(payoutratio, closeadj):
    result = (_mean(_f40_payout_floor(payoutratio, 378), 378)) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_meanxclosediff_378d_base_v097_signal(payoutratio, closeadj):
    result = (_mean(_f40_payout_floor(payoutratio, 378), 378)) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_stdxclose_378d_base_v098_signal(payoutratio, closeadj):
    result = (_std(_f40_payout_floor(payoutratio, 378), 378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_stdxclose2_378d_base_v099_signal(payoutratio, closeadj):
    result = (_std(_f40_payout_floor(payoutratio, 378), 378)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_stdxclosem_378d_base_v100_signal(payoutratio, closeadj):
    result = (_std(_f40_payout_floor(payoutratio, 378), 378)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_stdxclosem63_378d_base_v101_signal(payoutratio, closeadj):
    result = (_std(_f40_payout_floor(payoutratio, 378), 378)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_stdxclosez_378d_base_v102_signal(payoutratio, closeadj):
    result = (_std(_f40_payout_floor(payoutratio, 378), 378)) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_stdxclosechg_378d_base_v103_signal(payoutratio, closeadj):
    result = (_std(_f40_payout_floor(payoutratio, 378), 378)) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_stdxclosediff_378d_base_v104_signal(payoutratio, closeadj):
    result = (_std(_f40_payout_floor(payoutratio, 378), 378)) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_zxclose_378d_base_v105_signal(payoutratio, closeadj):
    result = (_z(_f40_payout_floor(payoutratio, 378), 378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_zxclose2_378d_base_v106_signal(payoutratio, closeadj):
    result = (_z(_f40_payout_floor(payoutratio, 378), 378)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_zxclosem_378d_base_v107_signal(payoutratio, closeadj):
    result = (_z(_f40_payout_floor(payoutratio, 378), 378)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_zxclosem63_378d_base_v108_signal(payoutratio, closeadj):
    result = (_z(_f40_payout_floor(payoutratio, 378), 378)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_zxclosez_378d_base_v109_signal(payoutratio, closeadj):
    result = (_z(_f40_payout_floor(payoutratio, 378), 378)) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_zxclosechg_378d_base_v110_signal(payoutratio, closeadj):
    result = (_z(_f40_payout_floor(payoutratio, 378), 378)) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_zxclosediff_378d_base_v111_signal(payoutratio, closeadj):
    result = (_z(_f40_payout_floor(payoutratio, 378), 378)) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_emaxclose_378d_base_v112_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 378)).ewm(span=378, adjust=False, min_periods=max(1, 378 // 2)).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_emaxclose2_378d_base_v113_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 378)).ewm(span=378, adjust=False, min_periods=max(1, 378 // 2)).mean()) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_emaxclosem_378d_base_v114_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 378)).ewm(span=378, adjust=False, min_periods=max(1, 378 // 2)).mean()) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_emaxclosem63_378d_base_v115_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 378)).ewm(span=378, adjust=False, min_periods=max(1, 378 // 2)).mean()) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_emaxclosez_378d_base_v116_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 378)).ewm(span=378, adjust=False, min_periods=max(1, 378 // 2)).mean()) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_emaxclosechg_378d_base_v117_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 378)).ewm(span=378, adjust=False, min_periods=max(1, 378 // 2)).mean()) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_emaxclosediff_378d_base_v118_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 378)).ewm(span=378, adjust=False, min_periods=max(1, 378 // 2)).mean()) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rmedianxclose_378d_base_v119_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 378)).rolling(378, min_periods=max(1, 378 // 2)).median()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rmedianxclose2_378d_base_v120_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 378)).rolling(378, min_periods=max(1, 378 // 2)).median()) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rmedianxclosem_378d_base_v121_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 378)).rolling(378, min_periods=max(1, 378 // 2)).median()) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rmedianxclosem63_378d_base_v122_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 378)).rolling(378, min_periods=max(1, 378 // 2)).median()) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rmedianxclosez_378d_base_v123_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 378)).rolling(378, min_periods=max(1, 378 // 2)).median()) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rmedianxclosechg_378d_base_v124_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 378)).rolling(378, min_periods=max(1, 378 // 2)).median()) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rmedianxclosediff_378d_base_v125_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 378)).rolling(378, min_periods=max(1, 378 // 2)).median()) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rmaxxclose_378d_base_v126_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 378)).rolling(378, min_periods=max(1, 378 // 2)).max()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rmaxxclose2_378d_base_v127_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 378)).rolling(378, min_periods=max(1, 378 // 2)).max()) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rmaxxclosem_378d_base_v128_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 378)).rolling(378, min_periods=max(1, 378 // 2)).max()) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rmaxxclosem63_378d_base_v129_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 378)).rolling(378, min_periods=max(1, 378 // 2)).max()) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rmaxxclosez_378d_base_v130_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 378)).rolling(378, min_periods=max(1, 378 // 2)).max()) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rmaxxclosechg_378d_base_v131_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 378)).rolling(378, min_periods=max(1, 378 // 2)).max()) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rmaxxclosediff_378d_base_v132_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 378)).rolling(378, min_periods=max(1, 378 // 2)).max()) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rminxclose_378d_base_v133_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 378)).rolling(378, min_periods=max(1, 378 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rminxclose2_378d_base_v134_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 378)).rolling(378, min_periods=max(1, 378 // 2)).min()) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rminxclosem_378d_base_v135_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 378)).rolling(378, min_periods=max(1, 378 // 2)).min()) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rminxclosem63_378d_base_v136_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 378)).rolling(378, min_periods=max(1, 378 // 2)).min()) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rminxclosez_378d_base_v137_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 378)).rolling(378, min_periods=max(1, 378 // 2)).min()) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rminxclosechg_378d_base_v138_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 378)).rolling(378, min_periods=max(1, 378 // 2)).min()) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_rminxclosediff_378d_base_v139_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 378)).rolling(378, min_periods=max(1, 378 // 2)).min()) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_skewxclose_378d_base_v140_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 378)).rolling(378, min_periods=max(1, 378 // 2)).skew()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_skewxclose2_378d_base_v141_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 378)).rolling(378, min_periods=max(1, 378 // 2)).skew()) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_skewxclosem_378d_base_v142_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 378)).rolling(378, min_periods=max(1, 378 // 2)).skew()) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_skewxclosem63_378d_base_v143_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 378)).rolling(378, min_periods=max(1, 378 // 2)).skew()) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_skewxclosez_378d_base_v144_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 378)).rolling(378, min_periods=max(1, 378 // 2)).skew()) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_skewxclosechg_378d_base_v145_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 378)).rolling(378, min_periods=max(1, 378 // 2)).skew()) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_skewxclosediff_378d_base_v146_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 378)).rolling(378, min_periods=max(1, 378 // 2)).skew()) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_kurtxclose_378d_base_v147_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 378)).rolling(378, min_periods=max(1, 378 // 2)).kurt()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_kurtxclose2_378d_base_v148_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 378)).rolling(378, min_periods=max(1, 378 // 2)).kurt()) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_kurtxclosem_378d_base_v149_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 378)).rolling(378, min_periods=max(1, 378 // 2)).kurt()) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f40epd_f40_energy_payout_durability_payout_floor_kurtxclosem63_378d_base_v150_signal(payoutratio, closeadj):
    result = ((_f40_payout_floor(payoutratio, 378)).rolling(378, min_periods=max(1, 378 // 2)).kurt()) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f40epd_f40_energy_payout_durability_payout_floor_signxclosediff_252d_base_v076_signal,
    f40epd_f40_energy_payout_durability_payout_floor_absxclose_252d_base_v077_signal,
    f40epd_f40_energy_payout_durability_payout_floor_absxclose2_252d_base_v078_signal,
    f40epd_f40_energy_payout_durability_payout_floor_absxclosem_252d_base_v079_signal,
    f40epd_f40_energy_payout_durability_payout_floor_absxclosem63_252d_base_v080_signal,
    f40epd_f40_energy_payout_durability_payout_floor_absxclosez_252d_base_v081_signal,
    f40epd_f40_energy_payout_durability_payout_floor_absxclosechg_252d_base_v082_signal,
    f40epd_f40_energy_payout_durability_payout_floor_absxclosediff_252d_base_v083_signal,
    f40epd_f40_energy_payout_durability_payout_floor_idxclose_378d_base_v084_signal,
    f40epd_f40_energy_payout_durability_payout_floor_idxclose2_378d_base_v085_signal,
    f40epd_f40_energy_payout_durability_payout_floor_idxclosem_378d_base_v086_signal,
    f40epd_f40_energy_payout_durability_payout_floor_idxclosem63_378d_base_v087_signal,
    f40epd_f40_energy_payout_durability_payout_floor_idxclosez_378d_base_v088_signal,
    f40epd_f40_energy_payout_durability_payout_floor_idxclosechg_378d_base_v089_signal,
    f40epd_f40_energy_payout_durability_payout_floor_idxclosediff_378d_base_v090_signal,
    f40epd_f40_energy_payout_durability_payout_floor_meanxclose_378d_base_v091_signal,
    f40epd_f40_energy_payout_durability_payout_floor_meanxclose2_378d_base_v092_signal,
    f40epd_f40_energy_payout_durability_payout_floor_meanxclosem_378d_base_v093_signal,
    f40epd_f40_energy_payout_durability_payout_floor_meanxclosem63_378d_base_v094_signal,
    f40epd_f40_energy_payout_durability_payout_floor_meanxclosez_378d_base_v095_signal,
    f40epd_f40_energy_payout_durability_payout_floor_meanxclosechg_378d_base_v096_signal,
    f40epd_f40_energy_payout_durability_payout_floor_meanxclosediff_378d_base_v097_signal,
    f40epd_f40_energy_payout_durability_payout_floor_stdxclose_378d_base_v098_signal,
    f40epd_f40_energy_payout_durability_payout_floor_stdxclose2_378d_base_v099_signal,
    f40epd_f40_energy_payout_durability_payout_floor_stdxclosem_378d_base_v100_signal,
    f40epd_f40_energy_payout_durability_payout_floor_stdxclosem63_378d_base_v101_signal,
    f40epd_f40_energy_payout_durability_payout_floor_stdxclosez_378d_base_v102_signal,
    f40epd_f40_energy_payout_durability_payout_floor_stdxclosechg_378d_base_v103_signal,
    f40epd_f40_energy_payout_durability_payout_floor_stdxclosediff_378d_base_v104_signal,
    f40epd_f40_energy_payout_durability_payout_floor_zxclose_378d_base_v105_signal,
    f40epd_f40_energy_payout_durability_payout_floor_zxclose2_378d_base_v106_signal,
    f40epd_f40_energy_payout_durability_payout_floor_zxclosem_378d_base_v107_signal,
    f40epd_f40_energy_payout_durability_payout_floor_zxclosem63_378d_base_v108_signal,
    f40epd_f40_energy_payout_durability_payout_floor_zxclosez_378d_base_v109_signal,
    f40epd_f40_energy_payout_durability_payout_floor_zxclosechg_378d_base_v110_signal,
    f40epd_f40_energy_payout_durability_payout_floor_zxclosediff_378d_base_v111_signal,
    f40epd_f40_energy_payout_durability_payout_floor_emaxclose_378d_base_v112_signal,
    f40epd_f40_energy_payout_durability_payout_floor_emaxclose2_378d_base_v113_signal,
    f40epd_f40_energy_payout_durability_payout_floor_emaxclosem_378d_base_v114_signal,
    f40epd_f40_energy_payout_durability_payout_floor_emaxclosem63_378d_base_v115_signal,
    f40epd_f40_energy_payout_durability_payout_floor_emaxclosez_378d_base_v116_signal,
    f40epd_f40_energy_payout_durability_payout_floor_emaxclosechg_378d_base_v117_signal,
    f40epd_f40_energy_payout_durability_payout_floor_emaxclosediff_378d_base_v118_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rmedianxclose_378d_base_v119_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rmedianxclose2_378d_base_v120_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rmedianxclosem_378d_base_v121_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rmedianxclosem63_378d_base_v122_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rmedianxclosez_378d_base_v123_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rmedianxclosechg_378d_base_v124_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rmedianxclosediff_378d_base_v125_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rmaxxclose_378d_base_v126_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rmaxxclose2_378d_base_v127_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rmaxxclosem_378d_base_v128_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rmaxxclosem63_378d_base_v129_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rmaxxclosez_378d_base_v130_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rmaxxclosechg_378d_base_v131_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rmaxxclosediff_378d_base_v132_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rminxclose_378d_base_v133_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rminxclose2_378d_base_v134_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rminxclosem_378d_base_v135_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rminxclosem63_378d_base_v136_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rminxclosez_378d_base_v137_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rminxclosechg_378d_base_v138_signal,
    f40epd_f40_energy_payout_durability_payout_floor_rminxclosediff_378d_base_v139_signal,
    f40epd_f40_energy_payout_durability_payout_floor_skewxclose_378d_base_v140_signal,
    f40epd_f40_energy_payout_durability_payout_floor_skewxclose2_378d_base_v141_signal,
    f40epd_f40_energy_payout_durability_payout_floor_skewxclosem_378d_base_v142_signal,
    f40epd_f40_energy_payout_durability_payout_floor_skewxclosem63_378d_base_v143_signal,
    f40epd_f40_energy_payout_durability_payout_floor_skewxclosez_378d_base_v144_signal,
    f40epd_f40_energy_payout_durability_payout_floor_skewxclosechg_378d_base_v145_signal,
    f40epd_f40_energy_payout_durability_payout_floor_skewxclosediff_378d_base_v146_signal,
    f40epd_f40_energy_payout_durability_payout_floor_kurtxclose_378d_base_v147_signal,
    f40epd_f40_energy_payout_durability_payout_floor_kurtxclose2_378d_base_v148_signal,
    f40epd_f40_energy_payout_durability_payout_floor_kurtxclosem_378d_base_v149_signal,
    f40epd_f40_energy_payout_durability_payout_floor_kurtxclosem63_378d_base_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F40_ENERGY_PAYOUT_DURABILITY_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")

    cols = {
        "closeadj": closeadj,
        "revenue": revenue, "fcf": fcf, "capex": capex,
        "sharesbas": sharesbas, "shareswa": shareswa,
        "eps": eps, "fcfps": fcfps, "dps": dps,
        "payoutratio": payoutratio,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f40_payout_floor", "_f40_payout_durability", "_f40_payout_sustainability",)
    import hashlib
    seen_bodies = set()
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
        body_lines = [l.strip() for l in src.splitlines()
                      if l.strip() and not l.strip().startswith("#") and not l.strip().startswith("def ")]
        body = "\n".join(body_lines)
        h = hashlib.sha1(body.encode()).hexdigest()
        assert h not in seen_bodies, f"DUP body in {name}"
        seen_bodies.add(h)
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f40_energy_payout_durability_base_076_150_claude: {n_features} features pass")
