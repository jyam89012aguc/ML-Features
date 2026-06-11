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


def _f38_capex_to_fcf(capex, fcf):
    base = fcf.abs().rolling(21, min_periods=5).mean().replace(0, np.nan)
    return capex / base



def _f38_capex_discipline(capex, fcf, w):
    ratio = capex / fcf.abs().rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)
    return -ratio.rolling(w, min_periods=max(1, w // 2)).mean()



def _f38_discipline_score(capex, fcf, revenue, w):
    ratio = capex / fcf.abs().rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)
    rev_g = revenue.pct_change(periods=w).fillna(0.0)
    return (-ratio + rev_g).rolling(w, min_periods=max(1, w // 2)).mean()


# ===== features =====


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_signxclosediff_252d_base_v076_signal(fcf, capex, closeadj):
    result = (np.sign(_f38_capex_to_fcf(capex, fcf))) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_absxclose_252d_base_v077_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_absxclose2_252d_base_v078_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).abs()) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_absxclosem_252d_base_v079_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).abs()) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_absxclosem63_252d_base_v080_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).abs()) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_absxclosez_252d_base_v081_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).abs()) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_absxclosechg_252d_base_v082_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).abs()) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_absxclosediff_252d_base_v083_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).abs()) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclose_378d_base_v084_signal(fcf, capex, closeadj):
    result = (_mean(_f38_capex_to_fcf(capex, fcf), 378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclose2_378d_base_v085_signal(fcf, capex, closeadj):
    result = (_mean(_f38_capex_to_fcf(capex, fcf), 378)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclosem_378d_base_v086_signal(fcf, capex, closeadj):
    result = (_mean(_f38_capex_to_fcf(capex, fcf), 378)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclosem63_378d_base_v087_signal(fcf, capex, closeadj):
    result = (_mean(_f38_capex_to_fcf(capex, fcf), 378)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclosez_378d_base_v088_signal(fcf, capex, closeadj):
    result = (_mean(_f38_capex_to_fcf(capex, fcf), 378)) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclosechg_378d_base_v089_signal(fcf, capex, closeadj):
    result = (_mean(_f38_capex_to_fcf(capex, fcf), 378)) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclosediff_378d_base_v090_signal(fcf, capex, closeadj):
    result = (_mean(_f38_capex_to_fcf(capex, fcf), 378)) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclose_378d_base_v091_signal(fcf, capex, closeadj):
    result = (_std(_f38_capex_to_fcf(capex, fcf), 378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclose2_378d_base_v092_signal(fcf, capex, closeadj):
    result = (_std(_f38_capex_to_fcf(capex, fcf), 378)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclosem_378d_base_v093_signal(fcf, capex, closeadj):
    result = (_std(_f38_capex_to_fcf(capex, fcf), 378)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclosem63_378d_base_v094_signal(fcf, capex, closeadj):
    result = (_std(_f38_capex_to_fcf(capex, fcf), 378)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclosez_378d_base_v095_signal(fcf, capex, closeadj):
    result = (_std(_f38_capex_to_fcf(capex, fcf), 378)) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclosechg_378d_base_v096_signal(fcf, capex, closeadj):
    result = (_std(_f38_capex_to_fcf(capex, fcf), 378)) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclosediff_378d_base_v097_signal(fcf, capex, closeadj):
    result = (_std(_f38_capex_to_fcf(capex, fcf), 378)) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclose_378d_base_v098_signal(fcf, capex, closeadj):
    result = (_z(_f38_capex_to_fcf(capex, fcf), 378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclose2_378d_base_v099_signal(fcf, capex, closeadj):
    result = (_z(_f38_capex_to_fcf(capex, fcf), 378)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclosem_378d_base_v100_signal(fcf, capex, closeadj):
    result = (_z(_f38_capex_to_fcf(capex, fcf), 378)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclosem63_378d_base_v101_signal(fcf, capex, closeadj):
    result = (_z(_f38_capex_to_fcf(capex, fcf), 378)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclosez_378d_base_v102_signal(fcf, capex, closeadj):
    result = (_z(_f38_capex_to_fcf(capex, fcf), 378)) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclosechg_378d_base_v103_signal(fcf, capex, closeadj):
    result = (_z(_f38_capex_to_fcf(capex, fcf), 378)) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclosediff_378d_base_v104_signal(fcf, capex, closeadj):
    result = (_z(_f38_capex_to_fcf(capex, fcf), 378)) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclose_378d_base_v105_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).ewm(span=378, adjust=False, min_periods=max(1, 378 // 2)).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclose2_378d_base_v106_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).ewm(span=378, adjust=False, min_periods=max(1, 378 // 2)).mean()) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclosem_378d_base_v107_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).ewm(span=378, adjust=False, min_periods=max(1, 378 // 2)).mean()) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclosem63_378d_base_v108_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).ewm(span=378, adjust=False, min_periods=max(1, 378 // 2)).mean()) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclosez_378d_base_v109_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).ewm(span=378, adjust=False, min_periods=max(1, 378 // 2)).mean()) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclosechg_378d_base_v110_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).ewm(span=378, adjust=False, min_periods=max(1, 378 // 2)).mean()) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclosediff_378d_base_v111_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).ewm(span=378, adjust=False, min_periods=max(1, 378 // 2)).mean()) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclose_378d_base_v112_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(378, min_periods=max(1, 378 // 2)).median()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclose2_378d_base_v113_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(378, min_periods=max(1, 378 // 2)).median()) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclosem_378d_base_v114_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(378, min_periods=max(1, 378 // 2)).median()) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclosem63_378d_base_v115_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(378, min_periods=max(1, 378 // 2)).median()) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclosez_378d_base_v116_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(378, min_periods=max(1, 378 // 2)).median()) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclosechg_378d_base_v117_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(378, min_periods=max(1, 378 // 2)).median()) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclosediff_378d_base_v118_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(378, min_periods=max(1, 378 // 2)).median()) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclose_378d_base_v119_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(378, min_periods=max(1, 378 // 2)).max()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclose2_378d_base_v120_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(378, min_periods=max(1, 378 // 2)).max()) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclosem_378d_base_v121_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(378, min_periods=max(1, 378 // 2)).max()) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclosem63_378d_base_v122_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(378, min_periods=max(1, 378 // 2)).max()) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclosez_378d_base_v123_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(378, min_periods=max(1, 378 // 2)).max()) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclosechg_378d_base_v124_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(378, min_periods=max(1, 378 // 2)).max()) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclosediff_378d_base_v125_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(378, min_periods=max(1, 378 // 2)).max()) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclose_378d_base_v126_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(378, min_periods=max(1, 378 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclose2_378d_base_v127_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(378, min_periods=max(1, 378 // 2)).min()) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclosem_378d_base_v128_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(378, min_periods=max(1, 378 // 2)).min()) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclosem63_378d_base_v129_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(378, min_periods=max(1, 378 // 2)).min()) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclosez_378d_base_v130_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(378, min_periods=max(1, 378 // 2)).min()) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclosechg_378d_base_v131_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(378, min_periods=max(1, 378 // 2)).min()) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclosediff_378d_base_v132_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(378, min_periods=max(1, 378 // 2)).min()) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclose_378d_base_v133_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(378, min_periods=max(1, 378 // 2)).skew()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclose2_378d_base_v134_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(378, min_periods=max(1, 378 // 2)).skew()) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclosem_378d_base_v135_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(378, min_periods=max(1, 378 // 2)).skew()) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclosem63_378d_base_v136_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(378, min_periods=max(1, 378 // 2)).skew()) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclosez_378d_base_v137_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(378, min_periods=max(1, 378 // 2)).skew()) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclosechg_378d_base_v138_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(378, min_periods=max(1, 378 // 2)).skew()) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclosediff_378d_base_v139_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(378, min_periods=max(1, 378 // 2)).skew()) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclose_378d_base_v140_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(378, min_periods=max(1, 378 // 2)).kurt()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclose2_378d_base_v141_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(378, min_periods=max(1, 378 // 2)).kurt()) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclosem_378d_base_v142_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(378, min_periods=max(1, 378 // 2)).kurt()) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclosem63_378d_base_v143_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(378, min_periods=max(1, 378 // 2)).kurt()) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclosez_378d_base_v144_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(378, min_periods=max(1, 378 // 2)).kurt()) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclosechg_378d_base_v145_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(378, min_periods=max(1, 378 // 2)).kurt()) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclosediff_378d_base_v146_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(378, min_periods=max(1, 378 // 2)).kurt()) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_qhixclose_378d_base_v147_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(378, min_periods=max(1, 378 // 2)).quantile(0.75)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_qhixclose2_378d_base_v148_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(378, min_periods=max(1, 378 // 2)).quantile(0.75)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_qhixclosem_378d_base_v149_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(378, min_periods=max(1, 378 // 2)).quantile(0.75)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f38ecd_f38_energy_capex_discipline_capex_to_fcf_qhixclosem63_378d_base_v150_signal(fcf, capex, closeadj):
    result = ((_f38_capex_to_fcf(capex, fcf)).rolling(378, min_periods=max(1, 378 // 2)).quantile(0.75)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_signxclosediff_252d_base_v076_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_absxclose_252d_base_v077_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_absxclose2_252d_base_v078_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_absxclosem_252d_base_v079_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_absxclosem63_252d_base_v080_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_absxclosez_252d_base_v081_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_absxclosechg_252d_base_v082_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_absxclosediff_252d_base_v083_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclose_378d_base_v084_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclose2_378d_base_v085_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclosem_378d_base_v086_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclosem63_378d_base_v087_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclosez_378d_base_v088_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclosechg_378d_base_v089_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_meanxclosediff_378d_base_v090_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclose_378d_base_v091_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclose2_378d_base_v092_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclosem_378d_base_v093_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclosem63_378d_base_v094_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclosez_378d_base_v095_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclosechg_378d_base_v096_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_stdxclosediff_378d_base_v097_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclose_378d_base_v098_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclose2_378d_base_v099_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclosem_378d_base_v100_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclosem63_378d_base_v101_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclosez_378d_base_v102_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclosechg_378d_base_v103_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_zxclosediff_378d_base_v104_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclose_378d_base_v105_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclose2_378d_base_v106_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclosem_378d_base_v107_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclosem63_378d_base_v108_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclosez_378d_base_v109_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclosechg_378d_base_v110_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_emaxclosediff_378d_base_v111_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclose_378d_base_v112_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclose2_378d_base_v113_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclosem_378d_base_v114_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclosem63_378d_base_v115_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclosez_378d_base_v116_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclosechg_378d_base_v117_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmedianxclosediff_378d_base_v118_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclose_378d_base_v119_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclose2_378d_base_v120_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclosem_378d_base_v121_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclosem63_378d_base_v122_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclosez_378d_base_v123_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclosechg_378d_base_v124_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rmaxxclosediff_378d_base_v125_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclose_378d_base_v126_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclose2_378d_base_v127_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclosem_378d_base_v128_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclosem63_378d_base_v129_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclosez_378d_base_v130_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclosechg_378d_base_v131_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_rminxclosediff_378d_base_v132_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclose_378d_base_v133_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclose2_378d_base_v134_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclosem_378d_base_v135_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclosem63_378d_base_v136_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclosez_378d_base_v137_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclosechg_378d_base_v138_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_skewxclosediff_378d_base_v139_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclose_378d_base_v140_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclose2_378d_base_v141_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclosem_378d_base_v142_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclosem63_378d_base_v143_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclosez_378d_base_v144_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclosechg_378d_base_v145_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_kurtxclosediff_378d_base_v146_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_qhixclose_378d_base_v147_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_qhixclose2_378d_base_v148_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_qhixclosem_378d_base_v149_signal,
    f38ecd_f38_energy_capex_discipline_capex_to_fcf_qhixclosem63_378d_base_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F38_ENERGY_CAPEX_DISCIPLINE_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f38_capex_to_fcf", "_f38_capex_discipline", "_f38_discipline_score",)
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
    print(f"OK f38_energy_capex_discipline_base_076_150_claude: {n_features} features pass")
