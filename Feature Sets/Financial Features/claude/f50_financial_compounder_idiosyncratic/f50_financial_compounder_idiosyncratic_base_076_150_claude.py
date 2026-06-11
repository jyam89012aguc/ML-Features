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
def _f50_quality_composite(roe, bvps, w):
    rq = roe.rolling(w, min_periods=max(1, w // 2)).mean()
    bg = bvps.pct_change(periods=w)
    return rq + bg


def _f50_idiosyncratic_alpha(roe, eps, w):
    r = roe.rolling(w, min_periods=max(1, w // 2)).mean()
    eg = eps.pct_change(periods=w)
    sd = r.rolling(w, min_periods=max(1, w // 2)).std()
    return (r + eg) / sd.replace(0, np.nan)


def _f50_terminal_quality(roe, bvps, eps, w):
    r = roe.rolling(w, min_periods=max(1, w // 2)).mean()
    bg = bvps.pct_change(periods=w)
    eg = eps.pct_change(periods=w)
    return r * (1.0 + bg) * (1.0 + eg)


def fci_f50_financial_compounder_idiosyncratic_qc_close_log_raw_126d_base_v076_signal(roe, bvps, closeadj):
    result = (_f50_quality_composite(roe, bvps, 126)) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_ia_close_log_raw_126d_base_v077_signal(roe, eps, closeadj):
    result = (_f50_idiosyncratic_alpha(roe, eps, 126)) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_tq_close_log_raw_126d_base_v078_signal(roe, bvps, eps, closeadj):
    result = (_f50_terminal_quality(roe, bvps, eps, 126)) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_qc_close_log_raw_189d_base_v079_signal(roe, bvps, closeadj):
    result = (_f50_quality_composite(roe, bvps, 189)) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_ia_close_log_raw_189d_base_v080_signal(roe, eps, closeadj):
    result = (_f50_idiosyncratic_alpha(roe, eps, 189)) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_tq_close_log_raw_189d_base_v081_signal(roe, bvps, eps, closeadj):
    result = (_f50_terminal_quality(roe, bvps, eps, 189)) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_qc_close_log_raw_252d_base_v082_signal(roe, bvps, closeadj):
    result = (_f50_quality_composite(roe, bvps, 252)) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_ia_close_log_raw_252d_base_v083_signal(roe, eps, closeadj):
    result = (_f50_idiosyncratic_alpha(roe, eps, 252)) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_tq_close_log_raw_252d_base_v084_signal(roe, bvps, eps, closeadj):
    result = (_f50_terminal_quality(roe, bvps, eps, 252)) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_qc_close_log_raw_378d_base_v085_signal(roe, bvps, closeadj):
    result = (_f50_quality_composite(roe, bvps, 378)) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_ia_close_log_raw_378d_base_v086_signal(roe, eps, closeadj):
    result = (_f50_idiosyncratic_alpha(roe, eps, 378)) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_tq_close_log_raw_378d_base_v087_signal(roe, bvps, eps, closeadj):
    result = (_f50_terminal_quality(roe, bvps, eps, 378)) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_qc_close_log_raw_504d_base_v088_signal(roe, bvps, closeadj):
    result = (_f50_quality_composite(roe, bvps, 504)) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_ia_close_log_raw_504d_base_v089_signal(roe, eps, closeadj):
    result = (_f50_idiosyncratic_alpha(roe, eps, 504)) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_tq_close_log_raw_504d_base_v090_signal(roe, bvps, eps, closeadj):
    result = (_f50_terminal_quality(roe, bvps, eps, 504)) * np.log(closeadj.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_qc_close_mean21_raw_5d_base_v091_signal(roe, bvps, closeadj):
    result = (_f50_quality_composite(roe, bvps, 5)) * closeadj.rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_ia_close_mean21_raw_5d_base_v092_signal(roe, eps, closeadj):
    result = (_f50_idiosyncratic_alpha(roe, eps, 5)) * closeadj.rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_tq_close_mean21_raw_5d_base_v093_signal(roe, bvps, eps, closeadj):
    result = (_f50_terminal_quality(roe, bvps, eps, 5)) * closeadj.rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_qc_close_mean21_raw_10d_base_v094_signal(roe, bvps, closeadj):
    result = (_f50_quality_composite(roe, bvps, 10)) * closeadj.rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_ia_close_mean21_raw_10d_base_v095_signal(roe, eps, closeadj):
    result = (_f50_idiosyncratic_alpha(roe, eps, 10)) * closeadj.rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_tq_close_mean21_raw_10d_base_v096_signal(roe, bvps, eps, closeadj):
    result = (_f50_terminal_quality(roe, bvps, eps, 10)) * closeadj.rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_qc_close_mean21_raw_21d_base_v097_signal(roe, bvps, closeadj):
    result = (_f50_quality_composite(roe, bvps, 21)) * closeadj.rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_ia_close_mean21_raw_21d_base_v098_signal(roe, eps, closeadj):
    result = (_f50_idiosyncratic_alpha(roe, eps, 21)) * closeadj.rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_tq_close_mean21_raw_21d_base_v099_signal(roe, bvps, eps, closeadj):
    result = (_f50_terminal_quality(roe, bvps, eps, 21)) * closeadj.rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_qc_close_mean21_raw_42d_base_v100_signal(roe, bvps, closeadj):
    result = (_f50_quality_composite(roe, bvps, 42)) * closeadj.rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_ia_close_mean21_raw_42d_base_v101_signal(roe, eps, closeadj):
    result = (_f50_idiosyncratic_alpha(roe, eps, 42)) * closeadj.rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_tq_close_mean21_raw_42d_base_v102_signal(roe, bvps, eps, closeadj):
    result = (_f50_terminal_quality(roe, bvps, eps, 42)) * closeadj.rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_qc_close_mean21_raw_63d_base_v103_signal(roe, bvps, closeadj):
    result = (_f50_quality_composite(roe, bvps, 63)) * closeadj.rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_ia_close_mean21_raw_63d_base_v104_signal(roe, eps, closeadj):
    result = (_f50_idiosyncratic_alpha(roe, eps, 63)) * closeadj.rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_tq_close_mean21_raw_63d_base_v105_signal(roe, bvps, eps, closeadj):
    result = (_f50_terminal_quality(roe, bvps, eps, 63)) * closeadj.rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_qc_close_mean21_raw_126d_base_v106_signal(roe, bvps, closeadj):
    result = (_f50_quality_composite(roe, bvps, 126)) * closeadj.rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_ia_close_mean21_raw_126d_base_v107_signal(roe, eps, closeadj):
    result = (_f50_idiosyncratic_alpha(roe, eps, 126)) * closeadj.rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_tq_close_mean21_raw_126d_base_v108_signal(roe, bvps, eps, closeadj):
    result = (_f50_terminal_quality(roe, bvps, eps, 126)) * closeadj.rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_qc_close_mean21_raw_189d_base_v109_signal(roe, bvps, closeadj):
    result = (_f50_quality_composite(roe, bvps, 189)) * closeadj.rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_ia_close_mean21_raw_189d_base_v110_signal(roe, eps, closeadj):
    result = (_f50_idiosyncratic_alpha(roe, eps, 189)) * closeadj.rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_tq_close_mean21_raw_189d_base_v111_signal(roe, bvps, eps, closeadj):
    result = (_f50_terminal_quality(roe, bvps, eps, 189)) * closeadj.rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_qc_close_mean21_raw_252d_base_v112_signal(roe, bvps, closeadj):
    result = (_f50_quality_composite(roe, bvps, 252)) * closeadj.rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_ia_close_mean21_raw_252d_base_v113_signal(roe, eps, closeadj):
    result = (_f50_idiosyncratic_alpha(roe, eps, 252)) * closeadj.rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_tq_close_mean21_raw_252d_base_v114_signal(roe, bvps, eps, closeadj):
    result = (_f50_terminal_quality(roe, bvps, eps, 252)) * closeadj.rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_qc_close_mean21_raw_378d_base_v115_signal(roe, bvps, closeadj):
    result = (_f50_quality_composite(roe, bvps, 378)) * closeadj.rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_ia_close_mean21_raw_378d_base_v116_signal(roe, eps, closeadj):
    result = (_f50_idiosyncratic_alpha(roe, eps, 378)) * closeadj.rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_tq_close_mean21_raw_378d_base_v117_signal(roe, bvps, eps, closeadj):
    result = (_f50_terminal_quality(roe, bvps, eps, 378)) * closeadj.rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_qc_close_mean21_raw_504d_base_v118_signal(roe, bvps, closeadj):
    result = (_f50_quality_composite(roe, bvps, 504)) * closeadj.rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_ia_close_mean21_raw_504d_base_v119_signal(roe, eps, closeadj):
    result = (_f50_idiosyncratic_alpha(roe, eps, 504)) * closeadj.rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_tq_close_mean21_raw_504d_base_v120_signal(roe, bvps, eps, closeadj):
    result = (_f50_terminal_quality(roe, bvps, eps, 504)) * closeadj.rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_qc_close_mean63_raw_5d_base_v121_signal(roe, bvps, closeadj):
    result = (_f50_quality_composite(roe, bvps, 5)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_ia_close_mean63_raw_5d_base_v122_signal(roe, eps, closeadj):
    result = (_f50_idiosyncratic_alpha(roe, eps, 5)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_tq_close_mean63_raw_5d_base_v123_signal(roe, bvps, eps, closeadj):
    result = (_f50_terminal_quality(roe, bvps, eps, 5)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_qc_close_mean63_raw_10d_base_v124_signal(roe, bvps, closeadj):
    result = (_f50_quality_composite(roe, bvps, 10)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_ia_close_mean63_raw_10d_base_v125_signal(roe, eps, closeadj):
    result = (_f50_idiosyncratic_alpha(roe, eps, 10)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_tq_close_mean63_raw_10d_base_v126_signal(roe, bvps, eps, closeadj):
    result = (_f50_terminal_quality(roe, bvps, eps, 10)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_qc_close_mean63_raw_21d_base_v127_signal(roe, bvps, closeadj):
    result = (_f50_quality_composite(roe, bvps, 21)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_ia_close_mean63_raw_21d_base_v128_signal(roe, eps, closeadj):
    result = (_f50_idiosyncratic_alpha(roe, eps, 21)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_tq_close_mean63_raw_21d_base_v129_signal(roe, bvps, eps, closeadj):
    result = (_f50_terminal_quality(roe, bvps, eps, 21)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_qc_close_mean63_raw_42d_base_v130_signal(roe, bvps, closeadj):
    result = (_f50_quality_composite(roe, bvps, 42)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_ia_close_mean63_raw_42d_base_v131_signal(roe, eps, closeadj):
    result = (_f50_idiosyncratic_alpha(roe, eps, 42)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_tq_close_mean63_raw_42d_base_v132_signal(roe, bvps, eps, closeadj):
    result = (_f50_terminal_quality(roe, bvps, eps, 42)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_qc_close_mean63_raw_63d_base_v133_signal(roe, bvps, closeadj):
    result = (_f50_quality_composite(roe, bvps, 63)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_ia_close_mean63_raw_63d_base_v134_signal(roe, eps, closeadj):
    result = (_f50_idiosyncratic_alpha(roe, eps, 63)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_tq_close_mean63_raw_63d_base_v135_signal(roe, bvps, eps, closeadj):
    result = (_f50_terminal_quality(roe, bvps, eps, 63)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_qc_close_mean63_raw_126d_base_v136_signal(roe, bvps, closeadj):
    result = (_f50_quality_composite(roe, bvps, 126)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_ia_close_mean63_raw_126d_base_v137_signal(roe, eps, closeadj):
    result = (_f50_idiosyncratic_alpha(roe, eps, 126)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_tq_close_mean63_raw_126d_base_v138_signal(roe, bvps, eps, closeadj):
    result = (_f50_terminal_quality(roe, bvps, eps, 126)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_qc_close_mean63_raw_189d_base_v139_signal(roe, bvps, closeadj):
    result = (_f50_quality_composite(roe, bvps, 189)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_ia_close_mean63_raw_189d_base_v140_signal(roe, eps, closeadj):
    result = (_f50_idiosyncratic_alpha(roe, eps, 189)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_tq_close_mean63_raw_189d_base_v141_signal(roe, bvps, eps, closeadj):
    result = (_f50_terminal_quality(roe, bvps, eps, 189)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_qc_close_mean63_raw_252d_base_v142_signal(roe, bvps, closeadj):
    result = (_f50_quality_composite(roe, bvps, 252)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_ia_close_mean63_raw_252d_base_v143_signal(roe, eps, closeadj):
    result = (_f50_idiosyncratic_alpha(roe, eps, 252)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_tq_close_mean63_raw_252d_base_v144_signal(roe, bvps, eps, closeadj):
    result = (_f50_terminal_quality(roe, bvps, eps, 252)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_qc_close_mean63_raw_378d_base_v145_signal(roe, bvps, closeadj):
    result = (_f50_quality_composite(roe, bvps, 378)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_ia_close_mean63_raw_378d_base_v146_signal(roe, eps, closeadj):
    result = (_f50_idiosyncratic_alpha(roe, eps, 378)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_tq_close_mean63_raw_378d_base_v147_signal(roe, bvps, eps, closeadj):
    result = (_f50_terminal_quality(roe, bvps, eps, 378)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_qc_close_mean63_raw_504d_base_v148_signal(roe, bvps, closeadj):
    result = (_f50_quality_composite(roe, bvps, 504)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_ia_close_mean63_raw_504d_base_v149_signal(roe, eps, closeadj):
    result = (_f50_idiosyncratic_alpha(roe, eps, 504)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def fci_f50_financial_compounder_idiosyncratic_tq_close_mean63_raw_504d_base_v150_signal(roe, bvps, eps, closeadj):
    result = (_f50_terminal_quality(roe, bvps, eps, 504)) * closeadj.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    fci_f50_financial_compounder_idiosyncratic_qc_close_log_raw_126d_base_v076_signal,
    fci_f50_financial_compounder_idiosyncratic_ia_close_log_raw_126d_base_v077_signal,
    fci_f50_financial_compounder_idiosyncratic_tq_close_log_raw_126d_base_v078_signal,
    fci_f50_financial_compounder_idiosyncratic_qc_close_log_raw_189d_base_v079_signal,
    fci_f50_financial_compounder_idiosyncratic_ia_close_log_raw_189d_base_v080_signal,
    fci_f50_financial_compounder_idiosyncratic_tq_close_log_raw_189d_base_v081_signal,
    fci_f50_financial_compounder_idiosyncratic_qc_close_log_raw_252d_base_v082_signal,
    fci_f50_financial_compounder_idiosyncratic_ia_close_log_raw_252d_base_v083_signal,
    fci_f50_financial_compounder_idiosyncratic_tq_close_log_raw_252d_base_v084_signal,
    fci_f50_financial_compounder_idiosyncratic_qc_close_log_raw_378d_base_v085_signal,
    fci_f50_financial_compounder_idiosyncratic_ia_close_log_raw_378d_base_v086_signal,
    fci_f50_financial_compounder_idiosyncratic_tq_close_log_raw_378d_base_v087_signal,
    fci_f50_financial_compounder_idiosyncratic_qc_close_log_raw_504d_base_v088_signal,
    fci_f50_financial_compounder_idiosyncratic_ia_close_log_raw_504d_base_v089_signal,
    fci_f50_financial_compounder_idiosyncratic_tq_close_log_raw_504d_base_v090_signal,
    fci_f50_financial_compounder_idiosyncratic_qc_close_mean21_raw_5d_base_v091_signal,
    fci_f50_financial_compounder_idiosyncratic_ia_close_mean21_raw_5d_base_v092_signal,
    fci_f50_financial_compounder_idiosyncratic_tq_close_mean21_raw_5d_base_v093_signal,
    fci_f50_financial_compounder_idiosyncratic_qc_close_mean21_raw_10d_base_v094_signal,
    fci_f50_financial_compounder_idiosyncratic_ia_close_mean21_raw_10d_base_v095_signal,
    fci_f50_financial_compounder_idiosyncratic_tq_close_mean21_raw_10d_base_v096_signal,
    fci_f50_financial_compounder_idiosyncratic_qc_close_mean21_raw_21d_base_v097_signal,
    fci_f50_financial_compounder_idiosyncratic_ia_close_mean21_raw_21d_base_v098_signal,
    fci_f50_financial_compounder_idiosyncratic_tq_close_mean21_raw_21d_base_v099_signal,
    fci_f50_financial_compounder_idiosyncratic_qc_close_mean21_raw_42d_base_v100_signal,
    fci_f50_financial_compounder_idiosyncratic_ia_close_mean21_raw_42d_base_v101_signal,
    fci_f50_financial_compounder_idiosyncratic_tq_close_mean21_raw_42d_base_v102_signal,
    fci_f50_financial_compounder_idiosyncratic_qc_close_mean21_raw_63d_base_v103_signal,
    fci_f50_financial_compounder_idiosyncratic_ia_close_mean21_raw_63d_base_v104_signal,
    fci_f50_financial_compounder_idiosyncratic_tq_close_mean21_raw_63d_base_v105_signal,
    fci_f50_financial_compounder_idiosyncratic_qc_close_mean21_raw_126d_base_v106_signal,
    fci_f50_financial_compounder_idiosyncratic_ia_close_mean21_raw_126d_base_v107_signal,
    fci_f50_financial_compounder_idiosyncratic_tq_close_mean21_raw_126d_base_v108_signal,
    fci_f50_financial_compounder_idiosyncratic_qc_close_mean21_raw_189d_base_v109_signal,
    fci_f50_financial_compounder_idiosyncratic_ia_close_mean21_raw_189d_base_v110_signal,
    fci_f50_financial_compounder_idiosyncratic_tq_close_mean21_raw_189d_base_v111_signal,
    fci_f50_financial_compounder_idiosyncratic_qc_close_mean21_raw_252d_base_v112_signal,
    fci_f50_financial_compounder_idiosyncratic_ia_close_mean21_raw_252d_base_v113_signal,
    fci_f50_financial_compounder_idiosyncratic_tq_close_mean21_raw_252d_base_v114_signal,
    fci_f50_financial_compounder_idiosyncratic_qc_close_mean21_raw_378d_base_v115_signal,
    fci_f50_financial_compounder_idiosyncratic_ia_close_mean21_raw_378d_base_v116_signal,
    fci_f50_financial_compounder_idiosyncratic_tq_close_mean21_raw_378d_base_v117_signal,
    fci_f50_financial_compounder_idiosyncratic_qc_close_mean21_raw_504d_base_v118_signal,
    fci_f50_financial_compounder_idiosyncratic_ia_close_mean21_raw_504d_base_v119_signal,
    fci_f50_financial_compounder_idiosyncratic_tq_close_mean21_raw_504d_base_v120_signal,
    fci_f50_financial_compounder_idiosyncratic_qc_close_mean63_raw_5d_base_v121_signal,
    fci_f50_financial_compounder_idiosyncratic_ia_close_mean63_raw_5d_base_v122_signal,
    fci_f50_financial_compounder_idiosyncratic_tq_close_mean63_raw_5d_base_v123_signal,
    fci_f50_financial_compounder_idiosyncratic_qc_close_mean63_raw_10d_base_v124_signal,
    fci_f50_financial_compounder_idiosyncratic_ia_close_mean63_raw_10d_base_v125_signal,
    fci_f50_financial_compounder_idiosyncratic_tq_close_mean63_raw_10d_base_v126_signal,
    fci_f50_financial_compounder_idiosyncratic_qc_close_mean63_raw_21d_base_v127_signal,
    fci_f50_financial_compounder_idiosyncratic_ia_close_mean63_raw_21d_base_v128_signal,
    fci_f50_financial_compounder_idiosyncratic_tq_close_mean63_raw_21d_base_v129_signal,
    fci_f50_financial_compounder_idiosyncratic_qc_close_mean63_raw_42d_base_v130_signal,
    fci_f50_financial_compounder_idiosyncratic_ia_close_mean63_raw_42d_base_v131_signal,
    fci_f50_financial_compounder_idiosyncratic_tq_close_mean63_raw_42d_base_v132_signal,
    fci_f50_financial_compounder_idiosyncratic_qc_close_mean63_raw_63d_base_v133_signal,
    fci_f50_financial_compounder_idiosyncratic_ia_close_mean63_raw_63d_base_v134_signal,
    fci_f50_financial_compounder_idiosyncratic_tq_close_mean63_raw_63d_base_v135_signal,
    fci_f50_financial_compounder_idiosyncratic_qc_close_mean63_raw_126d_base_v136_signal,
    fci_f50_financial_compounder_idiosyncratic_ia_close_mean63_raw_126d_base_v137_signal,
    fci_f50_financial_compounder_idiosyncratic_tq_close_mean63_raw_126d_base_v138_signal,
    fci_f50_financial_compounder_idiosyncratic_qc_close_mean63_raw_189d_base_v139_signal,
    fci_f50_financial_compounder_idiosyncratic_ia_close_mean63_raw_189d_base_v140_signal,
    fci_f50_financial_compounder_idiosyncratic_tq_close_mean63_raw_189d_base_v141_signal,
    fci_f50_financial_compounder_idiosyncratic_qc_close_mean63_raw_252d_base_v142_signal,
    fci_f50_financial_compounder_idiosyncratic_ia_close_mean63_raw_252d_base_v143_signal,
    fci_f50_financial_compounder_idiosyncratic_tq_close_mean63_raw_252d_base_v144_signal,
    fci_f50_financial_compounder_idiosyncratic_qc_close_mean63_raw_378d_base_v145_signal,
    fci_f50_financial_compounder_idiosyncratic_ia_close_mean63_raw_378d_base_v146_signal,
    fci_f50_financial_compounder_idiosyncratic_tq_close_mean63_raw_378d_base_v147_signal,
    fci_f50_financial_compounder_idiosyncratic_qc_close_mean63_raw_504d_base_v148_signal,
    fci_f50_financial_compounder_idiosyncratic_ia_close_mean63_raw_504d_base_v149_signal,
    fci_f50_financial_compounder_idiosyncratic_tq_close_mean63_raw_504d_base_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F50_FINANCIAL_COMPOUNDER_IDIOSYNCRATIC_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ('_f50_quality_composite', '_f50_idiosyncratic_alpha', '_f50_terminal_quality')
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
    print(f"OK f50_financial_compounder_idiosyncratic_base_076_150_claude: {n_features} features pass")
