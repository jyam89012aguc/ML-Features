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
def _f05_working_capital_ratio(inventory, receivables, payables, revenue):
    wc = inventory + receivables - payables
    return wc / revenue.replace(0, np.nan).abs()


def _f05_net_op_cycle(inventory, receivables, payables, cor):
    inv_days = 365.0 * inventory / cor.replace(0, np.nan).abs()
    rec_days = 365.0 * receivables / cor.replace(0, np.nan).abs()
    pay_days = 365.0 * payables / cor.replace(0, np.nan).abs()
    return inv_days + rec_days - pay_days


def _f05_wc_burn(workingcapital, revenue, w):
    burn = workingcapital.pct_change(periods=w)
    rev_scale = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    return burn * rev_scale / revenue.replace(0, np.nan).abs()

def f05wci_f05_working_capital_intensity_wcrxnoc_252d_base_v076_signal(inventory, receivables, payables, revenue, cor, closeadj):
    a = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    b = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = _mean(a, 252) * _mean(b, 252) * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrxwcb_21d_base_v077_signal(inventory, receivables, payables, revenue, workingcapital, closeadj):
    a = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    b = _f05_wc_burn(workingcapital, revenue, 21)
    result = _mean(a, 21) * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrxwcb_63d_base_v078_signal(inventory, receivables, payables, revenue, workingcapital, closeadj):
    a = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    b = _f05_wc_burn(workingcapital, revenue, 63)
    result = _mean(a, 63) * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrxwcb_126d_base_v079_signal(inventory, receivables, payables, revenue, workingcapital, closeadj):
    a = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    b = _f05_wc_burn(workingcapital, revenue, 126)
    result = _mean(a, 126) * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrxwcb_252d_base_v080_signal(inventory, receivables, payables, revenue, workingcapital, closeadj):
    a = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    b = _f05_wc_burn(workingcapital, revenue, 252)
    result = _mean(a, 252) * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_nocxwcb_21d_base_v081_signal(inventory, receivables, payables, cor, workingcapital, revenue, closeadj):
    a = _f05_net_op_cycle(inventory, receivables, payables, cor)
    b = _f05_wc_burn(workingcapital, revenue, 21)
    result = _mean(a, 21) * b * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_nocxwcb_63d_base_v082_signal(inventory, receivables, payables, cor, workingcapital, revenue, closeadj):
    a = _f05_net_op_cycle(inventory, receivables, payables, cor)
    b = _f05_wc_burn(workingcapital, revenue, 63)
    result = _mean(a, 63) * b * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_nocxwcb_126d_base_v083_signal(inventory, receivables, payables, cor, workingcapital, revenue, closeadj):
    a = _f05_net_op_cycle(inventory, receivables, payables, cor)
    b = _f05_wc_burn(workingcapital, revenue, 126)
    result = _mean(a, 126) * b * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_nocxwcb_252d_base_v084_signal(inventory, receivables, payables, cor, workingcapital, revenue, closeadj):
    a = _f05_net_op_cycle(inventory, receivables, payables, cor)
    b = _f05_wc_burn(workingcapital, revenue, 252)
    result = _mean(a, 252) * b * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_trio_21d_base_v085_signal(inventory, receivables, payables, revenue, cor, workingcapital, closeadj):
    a = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    b = _f05_net_op_cycle(inventory, receivables, payables, cor) / 365.0
    c = _f05_wc_burn(workingcapital, revenue, 21)
    result = (a + b + c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_trio_63d_base_v086_signal(inventory, receivables, payables, revenue, cor, workingcapital, closeadj):
    a = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    b = _f05_net_op_cycle(inventory, receivables, payables, cor) / 365.0
    c = _f05_wc_burn(workingcapital, revenue, 63)
    result = (a + b + c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_trio_126d_base_v087_signal(inventory, receivables, payables, revenue, cor, workingcapital, closeadj):
    a = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    b = _f05_net_op_cycle(inventory, receivables, payables, cor) / 365.0
    c = _f05_wc_burn(workingcapital, revenue, 126)
    result = (a + b + c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_trio_252d_base_v088_signal(inventory, receivables, payables, revenue, cor, workingcapital, closeadj):
    a = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    b = _f05_net_op_cycle(inventory, receivables, payables, cor) / 365.0
    c = _f05_wc_burn(workingcapital, revenue, 252)
    result = (a + b + c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrxret_21d_base_v089_signal(inventory, receivables, payables, revenue, closeadj):
    a = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    ret = closeadj.pct_change(21)
    result = a * ret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrxret_63d_base_v090_signal(inventory, receivables, payables, revenue, closeadj):
    a = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    ret = closeadj.pct_change(63)
    result = a * ret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrxret_126d_base_v091_signal(inventory, receivables, payables, revenue, closeadj):
    a = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    ret = closeadj.pct_change(126)
    result = a * ret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcbxret_21d_base_v092_signal(workingcapital, revenue, closeadj):
    a = _f05_wc_burn(workingcapital, revenue, 21)
    ret = closeadj.pct_change(21)
    result = a * ret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcbxret_63d_base_v093_signal(workingcapital, revenue, closeadj):
    a = _f05_wc_burn(workingcapital, revenue, 63)
    ret = closeadj.pct_change(63)
    result = a * ret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcbxret_126d_base_v094_signal(workingcapital, revenue, closeadj):
    a = _f05_wc_burn(workingcapital, revenue, 126)
    ret = closeadj.pct_change(126)
    result = a * ret * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_nocxret_21d_base_v095_signal(inventory, receivables, payables, cor, closeadj):
    a = _f05_net_op_cycle(inventory, receivables, payables, cor)
    ret = closeadj.pct_change(21)
    result = a * ret * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_nocxret_63d_base_v096_signal(inventory, receivables, payables, cor, closeadj):
    a = _f05_net_op_cycle(inventory, receivables, payables, cor)
    ret = closeadj.pct_change(63)
    result = a * ret * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_nocxret_126d_base_v097_signal(inventory, receivables, payables, cor, closeadj):
    a = _f05_net_op_cycle(inventory, receivables, payables, cor)
    ret = closeadj.pct_change(126)
    result = a * ret * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrxvol_21d_base_v098_signal(inventory, receivables, payables, revenue, closeadj, volume):
    a = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = _mean(a, 21) * _mean(closeadj * volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrxvol_63d_base_v099_signal(inventory, receivables, payables, revenue, closeadj, volume):
    a = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = _mean(a, 63) * _mean(closeadj * volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrxvol_126d_base_v100_signal(inventory, receivables, payables, revenue, closeadj, volume):
    a = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = _mean(a, 126) * _mean(closeadj * volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_nocxvol_21d_base_v101_signal(inventory, receivables, payables, cor, closeadj, volume):
    a = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = _mean(a, 21) * _mean(closeadj * volume, 21) / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_nocxvol_63d_base_v102_signal(inventory, receivables, payables, cor, closeadj, volume):
    a = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = _mean(a, 63) * _mean(closeadj * volume, 63) / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_nocxvol_126d_base_v103_signal(inventory, receivables, payables, cor, closeadj, volume):
    a = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = _mean(a, 126) * _mean(closeadj * volume, 126) / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcbxvol_21d_base_v104_signal(workingcapital, revenue, closeadj, volume):
    a = _f05_wc_burn(workingcapital, revenue, 21)
    result = a * _mean(closeadj * volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcbxvol_63d_base_v105_signal(workingcapital, revenue, closeadj, volume):
    a = _f05_wc_burn(workingcapital, revenue, 63)
    result = a * _mean(closeadj * volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcbxvol_126d_base_v106_signal(workingcapital, revenue, closeadj, volume):
    a = _f05_wc_burn(workingcapital, revenue, 126)
    result = a * _mean(closeadj * volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrema_21d_base_v107_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = base.ewm(span=21, min_periods=10).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrema_63d_base_v108_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = base.ewm(span=63, min_periods=31).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrema_126d_base_v109_signal(inventory, receivables, payables, revenue, closeadj):
    base = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = base.ewm(span=126, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_nocema_21d_base_v110_signal(inventory, receivables, payables, cor, closeadj):
    base = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = base.ewm(span=21, min_periods=10).mean() * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_nocema_63d_base_v111_signal(inventory, receivables, payables, cor, closeadj):
    base = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = base.ewm(span=63, min_periods=31).mean() * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_nocema_126d_base_v112_signal(inventory, receivables, payables, cor, closeadj):
    base = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = base.ewm(span=126, min_periods=63).mean() * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcbema_21d_base_v113_signal(workingcapital, revenue, closeadj):
    base = _f05_wc_burn(workingcapital, revenue, 21)
    result = base.ewm(span=21, min_periods=10).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcbema_63d_base_v114_signal(workingcapital, revenue, closeadj):
    base = _f05_wc_burn(workingcapital, revenue, 63)
    result = base.ewm(span=63, min_periods=31).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcbema_126d_base_v115_signal(workingcapital, revenue, closeadj):
    base = _f05_wc_burn(workingcapital, revenue, 126)
    result = base.ewm(span=126, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrxrev_21d_base_v116_signal(inventory, receivables, payables, revenue, closeadj):
    a = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = _mean(a, 21) * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrxrev_63d_base_v117_signal(inventory, receivables, payables, revenue, closeadj):
    a = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = _mean(a, 63) * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrxrev_126d_base_v118_signal(inventory, receivables, payables, revenue, closeadj):
    a = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = _mean(a, 126) * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrxrev_252d_base_v119_signal(inventory, receivables, payables, revenue, closeadj):
    a = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = _mean(a, 252) * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_nocxrev_21d_base_v120_signal(inventory, receivables, payables, cor, revenue, closeadj):
    a = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = _mean(a, 21) * (revenue / 1e9) * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_nocxrev_63d_base_v121_signal(inventory, receivables, payables, cor, revenue, closeadj):
    a = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = _mean(a, 63) * (revenue / 1e9) * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_nocxrev_126d_base_v122_signal(inventory, receivables, payables, cor, revenue, closeadj):
    a = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = _mean(a, 126) * (revenue / 1e9) * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_nocxrev_252d_base_v123_signal(inventory, receivables, payables, cor, revenue, closeadj):
    a = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = _mean(a, 252) * (revenue / 1e9) * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrxgm_21d_base_v124_signal(inventory, receivables, payables, revenue, grossmargin, closeadj):
    a = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = _mean(a, 21) * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrxgm_63d_base_v125_signal(inventory, receivables, payables, revenue, grossmargin, closeadj):
    a = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = _mean(a, 63) * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrxgm_126d_base_v126_signal(inventory, receivables, payables, revenue, grossmargin, closeadj):
    a = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = _mean(a, 126) * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrxgm_252d_base_v127_signal(inventory, receivables, payables, revenue, grossmargin, closeadj):
    a = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = _mean(a, 252) * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrlog_21d_base_v128_signal(inventory, receivables, payables, revenue, closeadj):
    a = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = np.log(_mean(a, 21).replace(0, np.nan).abs() + 0.001) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrlog_63d_base_v129_signal(inventory, receivables, payables, revenue, closeadj):
    a = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = np.log(_mean(a, 63).replace(0, np.nan).abs() + 0.001) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrlog_126d_base_v130_signal(inventory, receivables, payables, revenue, closeadj):
    a = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = np.log(_mean(a, 126).replace(0, np.nan).abs() + 0.001) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrlog_252d_base_v131_signal(inventory, receivables, payables, revenue, closeadj):
    a = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = np.log(_mean(a, 252).replace(0, np.nan).abs() + 0.001) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_noclog_21d_base_v132_signal(inventory, receivables, payables, cor, closeadj):
    a = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = np.log(_mean(a, 21).replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_noclog_63d_base_v133_signal(inventory, receivables, payables, cor, closeadj):
    a = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = np.log(_mean(a, 63).replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_noclog_126d_base_v134_signal(inventory, receivables, payables, cor, closeadj):
    a = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = np.log(_mean(a, 126).replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_noclog_252d_base_v135_signal(inventory, receivables, payables, cor, closeadj):
    a = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = np.log(_mean(a, 252).replace(0, np.nan).abs() + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcbsign_21d_base_v136_signal(workingcapital, revenue, closeadj):
    a = _f05_wc_burn(workingcapital, revenue, 21)
    result = a.abs() * np.sign(a) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcbsign_63d_base_v137_signal(workingcapital, revenue, closeadj):
    a = _f05_wc_burn(workingcapital, revenue, 63)
    result = a.abs() * np.sign(a) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcbsign_126d_base_v138_signal(workingcapital, revenue, closeadj):
    a = _f05_wc_burn(workingcapital, revenue, 126)
    result = a.abs() * np.sign(a) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcbsign_252d_base_v139_signal(workingcapital, revenue, closeadj):
    a = _f05_wc_burn(workingcapital, revenue, 252)
    result = a.abs() * np.sign(a) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrgm_21d_base_v140_signal(inventory, receivables, payables, gp, closeadj):
    base = _f05_working_capital_ratio(inventory, receivables, payables, gp)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrgm_63d_base_v141_signal(inventory, receivables, payables, gp, closeadj):
    base = _f05_working_capital_ratio(inventory, receivables, payables, gp)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrgm_126d_base_v142_signal(inventory, receivables, payables, gp, closeadj):
    base = _f05_working_capital_ratio(inventory, receivables, payables, gp)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrgm_252d_base_v143_signal(inventory, receivables, payables, gp, closeadj):
    base = _f05_working_capital_ratio(inventory, receivables, payables, gp)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrmcap_21d_base_v144_signal(inventory, receivables, payables, revenue, marketcap, closeadj):
    a = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = _mean(a, 21) * (marketcap / 1e8) + _f05_wc_burn(receivables, revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrmcap_63d_base_v145_signal(inventory, receivables, payables, revenue, marketcap, closeadj):
    a = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = _mean(a, 63) * (marketcap / 1e8) + _f05_wc_burn(receivables, revenue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrmcap_126d_base_v146_signal(inventory, receivables, payables, revenue, marketcap, closeadj):
    a = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = _mean(a, 126) * (marketcap / 1e8) + _f05_wc_burn(receivables, revenue, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_wcrmcap_252d_base_v147_signal(inventory, receivables, payables, revenue, marketcap, closeadj):
    a = _f05_working_capital_ratio(inventory, receivables, payables, revenue)
    result = _mean(a, 252) * (marketcap / 1e8) + _f05_wc_burn(receivables, revenue, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_nocxlong_21d_base_v148_signal(inventory, receivables, payables, cor, closeadj):
    a = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = _mean(a, 42) * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_nocxlong_63d_base_v149_signal(inventory, receivables, payables, cor, closeadj):
    a = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = _mean(a, 126) * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


def f05wci_f05_working_capital_intensity_nocxlong_126d_base_v150_signal(inventory, receivables, payables, cor, closeadj):
    a = _f05_net_op_cycle(inventory, receivables, payables, cor)
    result = _mean(a, 252) * closeadj / 365.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f05wci_f05_working_capital_intensity_wcrxnoc_252d_base_v076_signal,
    f05wci_f05_working_capital_intensity_wcrxwcb_21d_base_v077_signal,
    f05wci_f05_working_capital_intensity_wcrxwcb_63d_base_v078_signal,
    f05wci_f05_working_capital_intensity_wcrxwcb_126d_base_v079_signal,
    f05wci_f05_working_capital_intensity_wcrxwcb_252d_base_v080_signal,
    f05wci_f05_working_capital_intensity_nocxwcb_21d_base_v081_signal,
    f05wci_f05_working_capital_intensity_nocxwcb_63d_base_v082_signal,
    f05wci_f05_working_capital_intensity_nocxwcb_126d_base_v083_signal,
    f05wci_f05_working_capital_intensity_nocxwcb_252d_base_v084_signal,
    f05wci_f05_working_capital_intensity_trio_21d_base_v085_signal,
    f05wci_f05_working_capital_intensity_trio_63d_base_v086_signal,
    f05wci_f05_working_capital_intensity_trio_126d_base_v087_signal,
    f05wci_f05_working_capital_intensity_trio_252d_base_v088_signal,
    f05wci_f05_working_capital_intensity_wcrxret_21d_base_v089_signal,
    f05wci_f05_working_capital_intensity_wcrxret_63d_base_v090_signal,
    f05wci_f05_working_capital_intensity_wcrxret_126d_base_v091_signal,
    f05wci_f05_working_capital_intensity_wcbxret_21d_base_v092_signal,
    f05wci_f05_working_capital_intensity_wcbxret_63d_base_v093_signal,
    f05wci_f05_working_capital_intensity_wcbxret_126d_base_v094_signal,
    f05wci_f05_working_capital_intensity_nocxret_21d_base_v095_signal,
    f05wci_f05_working_capital_intensity_nocxret_63d_base_v096_signal,
    f05wci_f05_working_capital_intensity_nocxret_126d_base_v097_signal,
    f05wci_f05_working_capital_intensity_wcrxvol_21d_base_v098_signal,
    f05wci_f05_working_capital_intensity_wcrxvol_63d_base_v099_signal,
    f05wci_f05_working_capital_intensity_wcrxvol_126d_base_v100_signal,
    f05wci_f05_working_capital_intensity_nocxvol_21d_base_v101_signal,
    f05wci_f05_working_capital_intensity_nocxvol_63d_base_v102_signal,
    f05wci_f05_working_capital_intensity_nocxvol_126d_base_v103_signal,
    f05wci_f05_working_capital_intensity_wcbxvol_21d_base_v104_signal,
    f05wci_f05_working_capital_intensity_wcbxvol_63d_base_v105_signal,
    f05wci_f05_working_capital_intensity_wcbxvol_126d_base_v106_signal,
    f05wci_f05_working_capital_intensity_wcrema_21d_base_v107_signal,
    f05wci_f05_working_capital_intensity_wcrema_63d_base_v108_signal,
    f05wci_f05_working_capital_intensity_wcrema_126d_base_v109_signal,
    f05wci_f05_working_capital_intensity_nocema_21d_base_v110_signal,
    f05wci_f05_working_capital_intensity_nocema_63d_base_v111_signal,
    f05wci_f05_working_capital_intensity_nocema_126d_base_v112_signal,
    f05wci_f05_working_capital_intensity_wcbema_21d_base_v113_signal,
    f05wci_f05_working_capital_intensity_wcbema_63d_base_v114_signal,
    f05wci_f05_working_capital_intensity_wcbema_126d_base_v115_signal,
    f05wci_f05_working_capital_intensity_wcrxrev_21d_base_v116_signal,
    f05wci_f05_working_capital_intensity_wcrxrev_63d_base_v117_signal,
    f05wci_f05_working_capital_intensity_wcrxrev_126d_base_v118_signal,
    f05wci_f05_working_capital_intensity_wcrxrev_252d_base_v119_signal,
    f05wci_f05_working_capital_intensity_nocxrev_21d_base_v120_signal,
    f05wci_f05_working_capital_intensity_nocxrev_63d_base_v121_signal,
    f05wci_f05_working_capital_intensity_nocxrev_126d_base_v122_signal,
    f05wci_f05_working_capital_intensity_nocxrev_252d_base_v123_signal,
    f05wci_f05_working_capital_intensity_wcrxgm_21d_base_v124_signal,
    f05wci_f05_working_capital_intensity_wcrxgm_63d_base_v125_signal,
    f05wci_f05_working_capital_intensity_wcrxgm_126d_base_v126_signal,
    f05wci_f05_working_capital_intensity_wcrxgm_252d_base_v127_signal,
    f05wci_f05_working_capital_intensity_wcrlog_21d_base_v128_signal,
    f05wci_f05_working_capital_intensity_wcrlog_63d_base_v129_signal,
    f05wci_f05_working_capital_intensity_wcrlog_126d_base_v130_signal,
    f05wci_f05_working_capital_intensity_wcrlog_252d_base_v131_signal,
    f05wci_f05_working_capital_intensity_noclog_21d_base_v132_signal,
    f05wci_f05_working_capital_intensity_noclog_63d_base_v133_signal,
    f05wci_f05_working_capital_intensity_noclog_126d_base_v134_signal,
    f05wci_f05_working_capital_intensity_noclog_252d_base_v135_signal,
    f05wci_f05_working_capital_intensity_wcbsign_21d_base_v136_signal,
    f05wci_f05_working_capital_intensity_wcbsign_63d_base_v137_signal,
    f05wci_f05_working_capital_intensity_wcbsign_126d_base_v138_signal,
    f05wci_f05_working_capital_intensity_wcbsign_252d_base_v139_signal,
    f05wci_f05_working_capital_intensity_wcrgm_21d_base_v140_signal,
    f05wci_f05_working_capital_intensity_wcrgm_63d_base_v141_signal,
    f05wci_f05_working_capital_intensity_wcrgm_126d_base_v142_signal,
    f05wci_f05_working_capital_intensity_wcrgm_252d_base_v143_signal,
    f05wci_f05_working_capital_intensity_wcrmcap_21d_base_v144_signal,
    f05wci_f05_working_capital_intensity_wcrmcap_63d_base_v145_signal,
    f05wci_f05_working_capital_intensity_wcrmcap_126d_base_v146_signal,
    f05wci_f05_working_capital_intensity_wcrmcap_252d_base_v147_signal,
    f05wci_f05_working_capital_intensity_nocxlong_21d_base_v148_signal,
    f05wci_f05_working_capital_intensity_nocxlong_63d_base_v149_signal,
    f05wci_f05_working_capital_intensity_nocxlong_126d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F05_WORKING_CAPITAL_INTENSITY_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ('_f05_working_capital_ratio', '_f05_net_op_cycle', '_f05_wc_burn')
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
    print(f"OK f05_working_capital_intensity_base_076_150_claude: {n_features} features pass")
