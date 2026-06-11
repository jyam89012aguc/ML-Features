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


def _f36_share_change(s, w):
    return (s.shift(0) - s.shift(w)) / s.abs().rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)



def _f36_buyback_intensity(s, close, w):
    delta = -(s - s.shift(w))
    base = s.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)
    return (delta / base) * close



def _f36_buyback_timing(s, close, w):
    delta = -(s - s.shift(w))
    base = s.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)
    pmean = close.rolling(w, min_periods=max(1, w // 2)).mean()
    return (delta / base) * (pmean - close)


# ===== features =====


def f36ebc_f36_energy_buyback_cycle_share_change_signxclosediff_252d_base_v076_signal(sharesbas, closeadj):
    result = (np.sign(_f36_share_change(sharesbas, 252))) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_absxclose_252d_base_v077_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 252)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_absxclose2_252d_base_v078_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 252)).abs()) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_absxclosem_252d_base_v079_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 252)).abs()) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_absxclosem63_252d_base_v080_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 252)).abs()) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_absxclosez_252d_base_v081_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 252)).abs()) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_absxclosechg_252d_base_v082_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 252)).abs()) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_absxclosediff_252d_base_v083_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 252)).abs()) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_idxclose_378d_base_v084_signal(sharesbas, closeadj):
    result = (_f36_share_change(sharesbas, 378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_idxclose2_378d_base_v085_signal(sharesbas, closeadj):
    result = (_f36_share_change(sharesbas, 378)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_idxclosem_378d_base_v086_signal(sharesbas, closeadj):
    result = (_f36_share_change(sharesbas, 378)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_idxclosem63_378d_base_v087_signal(sharesbas, closeadj):
    result = (_f36_share_change(sharesbas, 378)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_idxclosez_378d_base_v088_signal(sharesbas, closeadj):
    result = (_f36_share_change(sharesbas, 378)) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_idxclosechg_378d_base_v089_signal(sharesbas, closeadj):
    result = (_f36_share_change(sharesbas, 378)) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_idxclosediff_378d_base_v090_signal(sharesbas, closeadj):
    result = (_f36_share_change(sharesbas, 378)) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_meanxclose_378d_base_v091_signal(sharesbas, closeadj):
    result = (_mean(_f36_share_change(sharesbas, 378), 378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_meanxclose2_378d_base_v092_signal(sharesbas, closeadj):
    result = (_mean(_f36_share_change(sharesbas, 378), 378)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_meanxclosem_378d_base_v093_signal(sharesbas, closeadj):
    result = (_mean(_f36_share_change(sharesbas, 378), 378)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_meanxclosem63_378d_base_v094_signal(sharesbas, closeadj):
    result = (_mean(_f36_share_change(sharesbas, 378), 378)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_meanxclosez_378d_base_v095_signal(sharesbas, closeadj):
    result = (_mean(_f36_share_change(sharesbas, 378), 378)) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_meanxclosechg_378d_base_v096_signal(sharesbas, closeadj):
    result = (_mean(_f36_share_change(sharesbas, 378), 378)) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_meanxclosediff_378d_base_v097_signal(sharesbas, closeadj):
    result = (_mean(_f36_share_change(sharesbas, 378), 378)) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_stdxclose_378d_base_v098_signal(sharesbas, closeadj):
    result = (_std(_f36_share_change(sharesbas, 378), 378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_stdxclose2_378d_base_v099_signal(sharesbas, closeadj):
    result = (_std(_f36_share_change(sharesbas, 378), 378)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_stdxclosem_378d_base_v100_signal(sharesbas, closeadj):
    result = (_std(_f36_share_change(sharesbas, 378), 378)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_stdxclosem63_378d_base_v101_signal(sharesbas, closeadj):
    result = (_std(_f36_share_change(sharesbas, 378), 378)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_stdxclosez_378d_base_v102_signal(sharesbas, closeadj):
    result = (_std(_f36_share_change(sharesbas, 378), 378)) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_stdxclosechg_378d_base_v103_signal(sharesbas, closeadj):
    result = (_std(_f36_share_change(sharesbas, 378), 378)) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_stdxclosediff_378d_base_v104_signal(sharesbas, closeadj):
    result = (_std(_f36_share_change(sharesbas, 378), 378)) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_zxclose_378d_base_v105_signal(sharesbas, closeadj):
    result = (_z(_f36_share_change(sharesbas, 378), 378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_zxclose2_378d_base_v106_signal(sharesbas, closeadj):
    result = (_z(_f36_share_change(sharesbas, 378), 378)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_zxclosem_378d_base_v107_signal(sharesbas, closeadj):
    result = (_z(_f36_share_change(sharesbas, 378), 378)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_zxclosem63_378d_base_v108_signal(sharesbas, closeadj):
    result = (_z(_f36_share_change(sharesbas, 378), 378)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_zxclosez_378d_base_v109_signal(sharesbas, closeadj):
    result = (_z(_f36_share_change(sharesbas, 378), 378)) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_zxclosechg_378d_base_v110_signal(sharesbas, closeadj):
    result = (_z(_f36_share_change(sharesbas, 378), 378)) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_zxclosediff_378d_base_v111_signal(sharesbas, closeadj):
    result = (_z(_f36_share_change(sharesbas, 378), 378)) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_emaxclose_378d_base_v112_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 378)).ewm(span=378, adjust=False, min_periods=max(1, 378 // 2)).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_emaxclose2_378d_base_v113_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 378)).ewm(span=378, adjust=False, min_periods=max(1, 378 // 2)).mean()) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_emaxclosem_378d_base_v114_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 378)).ewm(span=378, adjust=False, min_periods=max(1, 378 // 2)).mean()) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_emaxclosem63_378d_base_v115_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 378)).ewm(span=378, adjust=False, min_periods=max(1, 378 // 2)).mean()) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_emaxclosez_378d_base_v116_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 378)).ewm(span=378, adjust=False, min_periods=max(1, 378 // 2)).mean()) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_emaxclosechg_378d_base_v117_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 378)).ewm(span=378, adjust=False, min_periods=max(1, 378 // 2)).mean()) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_emaxclosediff_378d_base_v118_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 378)).ewm(span=378, adjust=False, min_periods=max(1, 378 // 2)).mean()) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rmedianxclose_378d_base_v119_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 378)).rolling(378, min_periods=max(1, 378 // 2)).median()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rmedianxclose2_378d_base_v120_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 378)).rolling(378, min_periods=max(1, 378 // 2)).median()) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rmedianxclosem_378d_base_v121_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 378)).rolling(378, min_periods=max(1, 378 // 2)).median()) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rmedianxclosem63_378d_base_v122_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 378)).rolling(378, min_periods=max(1, 378 // 2)).median()) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rmedianxclosez_378d_base_v123_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 378)).rolling(378, min_periods=max(1, 378 // 2)).median()) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rmedianxclosechg_378d_base_v124_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 378)).rolling(378, min_periods=max(1, 378 // 2)).median()) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rmedianxclosediff_378d_base_v125_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 378)).rolling(378, min_periods=max(1, 378 // 2)).median()) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rmaxxclose_378d_base_v126_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 378)).rolling(378, min_periods=max(1, 378 // 2)).max()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rmaxxclose2_378d_base_v127_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 378)).rolling(378, min_periods=max(1, 378 // 2)).max()) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rmaxxclosem_378d_base_v128_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 378)).rolling(378, min_periods=max(1, 378 // 2)).max()) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rmaxxclosem63_378d_base_v129_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 378)).rolling(378, min_periods=max(1, 378 // 2)).max()) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rmaxxclosez_378d_base_v130_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 378)).rolling(378, min_periods=max(1, 378 // 2)).max()) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rmaxxclosechg_378d_base_v131_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 378)).rolling(378, min_periods=max(1, 378 // 2)).max()) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rmaxxclosediff_378d_base_v132_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 378)).rolling(378, min_periods=max(1, 378 // 2)).max()) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rminxclose_378d_base_v133_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 378)).rolling(378, min_periods=max(1, 378 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rminxclose2_378d_base_v134_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 378)).rolling(378, min_periods=max(1, 378 // 2)).min()) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rminxclosem_378d_base_v135_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 378)).rolling(378, min_periods=max(1, 378 // 2)).min()) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rminxclosem63_378d_base_v136_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 378)).rolling(378, min_periods=max(1, 378 // 2)).min()) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rminxclosez_378d_base_v137_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 378)).rolling(378, min_periods=max(1, 378 // 2)).min()) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rminxclosechg_378d_base_v138_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 378)).rolling(378, min_periods=max(1, 378 // 2)).min()) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_rminxclosediff_378d_base_v139_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 378)).rolling(378, min_periods=max(1, 378 // 2)).min()) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_skewxclose_378d_base_v140_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 378)).rolling(378, min_periods=max(1, 378 // 2)).skew()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_skewxclose2_378d_base_v141_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 378)).rolling(378, min_periods=max(1, 378 // 2)).skew()) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_skewxclosem_378d_base_v142_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 378)).rolling(378, min_periods=max(1, 378 // 2)).skew()) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_skewxclosem63_378d_base_v143_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 378)).rolling(378, min_periods=max(1, 378 // 2)).skew()) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_skewxclosez_378d_base_v144_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 378)).rolling(378, min_periods=max(1, 378 // 2)).skew()) * _z(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_skewxclosechg_378d_base_v145_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 378)).rolling(378, min_periods=max(1, 378 // 2)).skew()) * closeadj.pct_change(21).fillna(0.0)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_skewxclosediff_378d_base_v146_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 378)).rolling(378, min_periods=max(1, 378 // 2)).skew()) * (closeadj - _mean(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_kurtxclose_378d_base_v147_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 378)).rolling(378, min_periods=max(1, 378 // 2)).kurt()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_kurtxclose2_378d_base_v148_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 378)).rolling(378, min_periods=max(1, 378 // 2)).kurt()) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_kurtxclosem_378d_base_v149_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 378)).rolling(378, min_periods=max(1, 378 // 2)).kurt()) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36ebc_f36_energy_buyback_cycle_share_change_kurtxclosem63_378d_base_v150_signal(sharesbas, closeadj):
    result = ((_f36_share_change(sharesbas, 378)).rolling(378, min_periods=max(1, 378 // 2)).kurt()) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f36ebc_f36_energy_buyback_cycle_share_change_signxclosediff_252d_base_v076_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_absxclose_252d_base_v077_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_absxclose2_252d_base_v078_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_absxclosem_252d_base_v079_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_absxclosem63_252d_base_v080_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_absxclosez_252d_base_v081_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_absxclosechg_252d_base_v082_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_absxclosediff_252d_base_v083_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_idxclose_378d_base_v084_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_idxclose2_378d_base_v085_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_idxclosem_378d_base_v086_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_idxclosem63_378d_base_v087_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_idxclosez_378d_base_v088_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_idxclosechg_378d_base_v089_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_idxclosediff_378d_base_v090_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_meanxclose_378d_base_v091_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_meanxclose2_378d_base_v092_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_meanxclosem_378d_base_v093_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_meanxclosem63_378d_base_v094_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_meanxclosez_378d_base_v095_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_meanxclosechg_378d_base_v096_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_meanxclosediff_378d_base_v097_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_stdxclose_378d_base_v098_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_stdxclose2_378d_base_v099_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_stdxclosem_378d_base_v100_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_stdxclosem63_378d_base_v101_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_stdxclosez_378d_base_v102_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_stdxclosechg_378d_base_v103_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_stdxclosediff_378d_base_v104_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_zxclose_378d_base_v105_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_zxclose2_378d_base_v106_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_zxclosem_378d_base_v107_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_zxclosem63_378d_base_v108_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_zxclosez_378d_base_v109_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_zxclosechg_378d_base_v110_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_zxclosediff_378d_base_v111_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_emaxclose_378d_base_v112_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_emaxclose2_378d_base_v113_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_emaxclosem_378d_base_v114_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_emaxclosem63_378d_base_v115_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_emaxclosez_378d_base_v116_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_emaxclosechg_378d_base_v117_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_emaxclosediff_378d_base_v118_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rmedianxclose_378d_base_v119_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rmedianxclose2_378d_base_v120_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rmedianxclosem_378d_base_v121_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rmedianxclosem63_378d_base_v122_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rmedianxclosez_378d_base_v123_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rmedianxclosechg_378d_base_v124_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rmedianxclosediff_378d_base_v125_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rmaxxclose_378d_base_v126_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rmaxxclose2_378d_base_v127_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rmaxxclosem_378d_base_v128_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rmaxxclosem63_378d_base_v129_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rmaxxclosez_378d_base_v130_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rmaxxclosechg_378d_base_v131_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rmaxxclosediff_378d_base_v132_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rminxclose_378d_base_v133_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rminxclose2_378d_base_v134_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rminxclosem_378d_base_v135_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rminxclosem63_378d_base_v136_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rminxclosez_378d_base_v137_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rminxclosechg_378d_base_v138_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_rminxclosediff_378d_base_v139_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_skewxclose_378d_base_v140_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_skewxclose2_378d_base_v141_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_skewxclosem_378d_base_v142_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_skewxclosem63_378d_base_v143_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_skewxclosez_378d_base_v144_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_skewxclosechg_378d_base_v145_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_skewxclosediff_378d_base_v146_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_kurtxclose_378d_base_v147_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_kurtxclose2_378d_base_v148_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_kurtxclosem_378d_base_v149_signal,
    f36ebc_f36_energy_buyback_cycle_share_change_kurtxclosem63_378d_base_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F36_ENERGY_BUYBACK_CYCLE_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f36_share_change", "_f36_buyback_intensity", "_f36_buyback_timing",)
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
    print(f"OK f36_energy_buyback_cycle_base_076_150_claude: {n_features} features pass")
