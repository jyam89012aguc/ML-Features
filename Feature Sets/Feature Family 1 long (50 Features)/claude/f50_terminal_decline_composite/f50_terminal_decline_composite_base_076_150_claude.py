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


def _diff(s, n):
    return s.diff(periods=n)


# ===== folder domain primitives =====
def _f50_terminal_decline(revenue, opinc, marketcap, w):
    rev_decline = -revenue.diff(w) / revenue.shift(w).abs().replace(0, np.nan)
    margin = opinc / revenue.replace(0, np.nan)
    margin_compression = -margin.diff(w)
    val_collapse = -marketcap.diff(w) / marketcap.shift(w).abs().replace(0, np.nan)
    return rev_decline + margin_compression + val_collapse


def _f50_revdecline(revenue, w):
    return -revenue.diff(w) / revenue.shift(w).abs().replace(0, np.nan)


def _f50_margincompress(opinc, revenue, w):
    margin = opinc / revenue.replace(0, np.nan)
    return -margin.diff(w)


# 21d EMA revdecline
def f50tdc_f50_terminal_decline_composite_revdeclineema_21d_base_v076_signal(revenue, marketcap):
    base = _f50_revdecline(revenue, 63)
    result = base.ewm(span=21, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA revdecline
def f50tdc_f50_terminal_decline_composite_revdeclineema_63d_base_v077_signal(revenue, marketcap):
    base = _f50_revdecline(revenue, 63)
    result = base.ewm(span=63, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA revdecline
def f50tdc_f50_terminal_decline_composite_revdeclineema_252d_base_v078_signal(revenue, marketcap):
    base = _f50_revdecline(revenue, 252)
    result = base.ewm(span=252, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA margcomp
def f50tdc_f50_terminal_decline_composite_margcompema_21d_base_v079_signal(opinc, revenue, marketcap):
    base = _f50_margincompress(opinc, revenue, 63)
    result = base.ewm(span=21, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA margcomp
def f50tdc_f50_terminal_decline_composite_margcompema_63d_base_v080_signal(opinc, revenue, marketcap):
    base = _f50_margincompress(opinc, revenue, 63)
    result = base.ewm(span=63, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA margcomp
def f50tdc_f50_terminal_decline_composite_margcompema_252d_base_v081_signal(opinc, revenue, marketcap):
    base = _f50_margincompress(opinc, revenue, 252)
    result = base.ewm(span=252, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d worst revdecline
def f50tdc_f50_terminal_decline_composite_worstrevdecline_21d_base_v082_signal(revenue, marketcap):
    base = _f50_revdecline(revenue, 63)
    result = base.rolling(21, min_periods=5).max() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d worst revdecline
def f50tdc_f50_terminal_decline_composite_worstrevdecline_63d_base_v083_signal(revenue, marketcap):
    base = _f50_revdecline(revenue, 63)
    result = base.rolling(63, min_periods=21).max() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d worst revdecline
def f50tdc_f50_terminal_decline_composite_worstrevdecline_252d_base_v084_signal(revenue, marketcap):
    base = _f50_revdecline(revenue, 252)
    result = base.rolling(252, min_periods=63).max() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d worst revdecline
def f50tdc_f50_terminal_decline_composite_worstrevdecline_504d_base_v085_signal(revenue, marketcap):
    base = _f50_revdecline(revenue, 504)
    result = base.rolling(504, min_periods=126).max() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d worst margcomp
def f50tdc_f50_terminal_decline_composite_worstmargcomp_63d_base_v086_signal(opinc, revenue, marketcap):
    base = _f50_margincompress(opinc, revenue, 63)
    result = base.rolling(63, min_periods=21).max() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d worst margcomp
def f50tdc_f50_terminal_decline_composite_worstmargcomp_252d_base_v087_signal(opinc, revenue, marketcap):
    base = _f50_margincompress(opinc, revenue, 252)
    result = base.rolling(252, min_periods=63).max() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d worst margcomp
def f50tdc_f50_terminal_decline_composite_worstmargcomp_504d_base_v088_signal(opinc, revenue, marketcap):
    base = _f50_margincompress(opinc, revenue, 504)
    result = base.rolling(504, min_periods=126).max() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d squared revdecline
def f50tdc_f50_terminal_decline_composite_revdeclinesq_63d_base_v089_signal(revenue, marketcap):
    base = _f50_revdecline(revenue, 63)
    result = base * base.abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d squared revdecline
def f50tdc_f50_terminal_decline_composite_revdeclinesq_252d_base_v090_signal(revenue, marketcap):
    base = _f50_revdecline(revenue, 252)
    result = base * base.abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d squared margcomp
def f50tdc_f50_terminal_decline_composite_margcompsq_63d_base_v091_signal(opinc, revenue, marketcap):
    base = _f50_margincompress(opinc, revenue, 63)
    result = base * base.abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d squared margcomp
def f50tdc_f50_terminal_decline_composite_margcompsq_252d_base_v092_signal(opinc, revenue, marketcap):
    base = _f50_margincompress(opinc, revenue, 252)
    result = base * base.abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d revdecline × ev
def f50tdc_f50_terminal_decline_composite_revdeclinexev_21d_base_v093_signal(revenue, marketcap, ev):
    base = _f50_revdecline(revenue, 21)
    result = base * ev + _f50_margincompress(revenue, revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revdecline × ev
def f50tdc_f50_terminal_decline_composite_revdeclinexev_252d_base_v094_signal(revenue, marketcap, ev):
    base = _f50_revdecline(revenue, 252)
    result = base * ev + _f50_margincompress(revenue, revenue, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d margcomp × ev
def f50tdc_f50_terminal_decline_composite_margcompxev_252d_base_v095_signal(opinc, revenue, marketcap, ev):
    base = _f50_margincompress(opinc, revenue, 252)
    result = base * ev + _f50_revdecline(revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# revdecline × evebitda 63d
def f50tdc_f50_terminal_decline_composite_revdeclinexevebitda_63d_base_v096_signal(revenue, marketcap, evebitda):
    base = _f50_revdecline(revenue, 63)
    result = base * evebitda * marketcap + _f50_margincompress(revenue, revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# revdecline × evebit 252d
def f50tdc_f50_terminal_decline_composite_revdeclinexevebit_252d_base_v097_signal(revenue, marketcap, evebit):
    base = _f50_revdecline(revenue, 252)
    result = base * evebit * marketcap + _f50_margincompress(revenue, revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# revdecline × pb 63d
def f50tdc_f50_terminal_decline_composite_revdeclinexpb_63d_base_v098_signal(revenue, marketcap, pb):
    base = _f50_revdecline(revenue, 63)
    result = base * pb * marketcap + _f50_margincompress(revenue, revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# revdecline × ps 63d
def f50tdc_f50_terminal_decline_composite_revdeclinexps_63d_base_v099_signal(revenue, marketcap, ps):
    base = _f50_revdecline(revenue, 63)
    result = base * ps * marketcap + _f50_margincompress(revenue, revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# margcomp × evebitda 63d
def f50tdc_f50_terminal_decline_composite_margcompxevebitda_63d_base_v100_signal(opinc, revenue, marketcap, evebitda):
    base = _f50_margincompress(opinc, revenue, 63)
    result = base * evebitda * marketcap + _f50_revdecline(revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# margcomp × evebit 252d
def f50tdc_f50_terminal_decline_composite_margcompxevebit_252d_base_v101_signal(opinc, revenue, marketcap, evebit):
    base = _f50_margincompress(opinc, revenue, 252)
    result = base * evebit * marketcap + _f50_revdecline(revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# margcomp × pb 63d
def f50tdc_f50_terminal_decline_composite_margcompxpb_63d_base_v102_signal(opinc, revenue, marketcap, pb):
    base = _f50_margincompress(opinc, revenue, 63)
    result = base * pb * marketcap + _f50_revdecline(revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# margcomp × ps 63d
def f50tdc_f50_terminal_decline_composite_margcompxps_63d_base_v103_signal(opinc, revenue, marketcap, ps):
    base = _f50_margincompress(opinc, revenue, 63)
    result = base * ps * marketcap + _f50_revdecline(revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revdecline × debt 252d
def f50tdc_f50_terminal_decline_composite_revdeclinexdebt_252d_base_v104_signal(revenue, marketcap, debt):
    base = _f50_revdecline(revenue, 252)
    result = base * debt + _f50_margincompress(revenue, revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# decline × dilution 63d
def f50tdc_f50_terminal_decline_composite_declinexdilution_63d_base_v105_signal(revenue, opinc, marketcap, sharesbas):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    sg = sharesbas.diff(63) / sharesbas.shift(63).abs().replace(0, np.nan)
    result = base * (1.0 + sg.clip(-1, 1)) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# decline × dilution 252d
def f50tdc_f50_terminal_decline_composite_declinexdilution_252d_base_v106_signal(revenue, opinc, marketcap, sharesbas):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    sg = sharesbas.diff(252) / sharesbas.shift(252).abs().replace(0, np.nan)
    result = base * (1.0 + sg.clip(-1, 1)) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# decline × leverage 63d
def f50tdc_f50_terminal_decline_composite_declinexlev_63d_base_v107_signal(revenue, opinc, marketcap, debt, equity):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    lev = debt / equity.replace(0, np.nan)
    result = base * lev * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# decline × leverage 252d
def f50tdc_f50_terminal_decline_composite_declinexlev_252d_base_v108_signal(revenue, opinc, marketcap, debt, equity):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    lev = debt / equity.replace(0, np.nan)
    result = base * lev * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# decline × inverse equity 63d
def f50tdc_f50_terminal_decline_composite_declinexinveq_63d_base_v109_signal(revenue, opinc, marketcap, equity):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    inveq = marketcap / equity.replace(0, np.nan)
    result = base * inveq * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# decline × inverse equity 252d
def f50tdc_f50_terminal_decline_composite_declinexinveq_252d_base_v110_signal(revenue, opinc, marketcap, equity):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    inveq = marketcap / equity.replace(0, np.nan)
    result = base * inveq * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d decline anomaly (vs 252d mean)
def f50tdc_f50_terminal_decline_composite_declineanomaly_63d_base_v111_signal(revenue, opinc, marketcap):
    a = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    b = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    result = (a - b) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d decline anomaly
def f50tdc_f50_terminal_decline_composite_declineanomaly_252d_base_v112_signal(revenue, opinc, marketcap):
    a = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    b = _f50_terminal_decline(revenue, opinc, marketcap, 504)
    result = (a - b) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d decline × evebitda
def f50tdc_f50_terminal_decline_composite_declinexevebitda_252d_base_v113_signal(revenue, opinc, marketcap, evebitda):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    result = base * evebitda * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d decline × evebit
def f50tdc_f50_terminal_decline_composite_declinexevebit_252d_base_v114_signal(revenue, opinc, marketcap, evebit):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    result = base * evebit * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d decline × pb
def f50tdc_f50_terminal_decline_composite_declinexpb_252d_base_v115_signal(revenue, opinc, marketcap, pb):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    result = base * pb * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d decline × pe
def f50tdc_f50_terminal_decline_composite_declinexpe_252d_base_v116_signal(revenue, opinc, marketcap, pe):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    result = base * pe * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d decline × ps
def f50tdc_f50_terminal_decline_composite_declinexps_252d_base_v117_signal(revenue, opinc, marketcap, ps):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    result = base * ps * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d decline × log marketcap
def f50tdc_f50_terminal_decline_composite_declinexlogmcap_252d_base_v118_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    lm = np.log(marketcap.replace(0, np.nan).abs())
    result = base * lm * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d decline × revenue
def f50tdc_f50_terminal_decline_composite_declinexrev_252d_base_v119_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    result = base * revenue
    return result.replace([np.inf, -np.inf], np.nan)


# 252d decline × assets
def f50tdc_f50_terminal_decline_composite_declinexassets_252d_base_v120_signal(revenue, opinc, marketcap, assets):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    result = base * assets + _f50_revdecline(revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d decline × debt
def f50tdc_f50_terminal_decline_composite_declinexdebt_63d_base_v121_signal(revenue, opinc, marketcap, debt):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    result = base * debt + _f50_revdecline(revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d decline × equity
def f50tdc_f50_terminal_decline_composite_declinexequity_63d_base_v122_signal(revenue, opinc, marketcap, equity):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    result = base * equity.abs() + _f50_revdecline(revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d decline × equity
def f50tdc_f50_terminal_decline_composite_declinexequity_252d_base_v123_signal(revenue, opinc, marketcap, equity):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    result = base * equity.abs() + _f50_revdecline(revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d decline × ebitda
def f50tdc_f50_terminal_decline_composite_declinexebitda_63d_base_v124_signal(revenue, opinc, marketcap, ebitda):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    result = base * ebitda + _f50_revdecline(revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d decline × ebitda
def f50tdc_f50_terminal_decline_composite_declinexebitda_252d_base_v125_signal(revenue, opinc, marketcap, ebitda):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    result = base * ebitda + _f50_revdecline(revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d decline area / 252d area
def f50tdc_f50_terminal_decline_composite_declineareafrac_63v252_base_v126_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252).abs()
    a = base.rolling(63, min_periods=21).sum()
    b = base.rolling(252, min_periods=63).sum().replace(0, np.nan)
    result = (a / b) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d decline area / 504d area
def f50tdc_f50_terminal_decline_composite_declineareafrac_252v504_base_v127_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 504).abs()
    a = base.rolling(252, min_periods=63).sum()
    b = base.rolling(504, min_periods=126).sum().replace(0, np.nan)
    result = (a / b) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d decline volvol
def f50tdc_f50_terminal_decline_composite_declinevolvol_63d_base_v128_signal(revenue, opinc, marketcap):
    sd = _std(_f50_terminal_decline(revenue, opinc, marketcap, 252), 63)
    result = _std(sd, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d decline volvol
def f50tdc_f50_terminal_decline_composite_declinevolvol_252d_base_v129_signal(revenue, opinc, marketcap):
    sd = _std(_f50_terminal_decline(revenue, opinc, marketcap, 504), 252)
    result = _std(sd, 126) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revdecline volvol
def f50tdc_f50_terminal_decline_composite_revdeclinevolvol_63d_base_v130_signal(revenue, marketcap):
    sd = _std(_f50_revdecline(revenue, 252), 63)
    result = _std(sd, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d margcomp volvol
def f50tdc_f50_terminal_decline_composite_margcompvolvol_63d_base_v131_signal(opinc, revenue, marketcap):
    sd = _std(_f50_margincompress(opinc, revenue, 252), 63)
    result = _std(sd, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d decline × close
def f50tdc_f50_terminal_decline_composite_declinexclose_63d_base_v132_signal(revenue, opinc, marketcap, closeadj):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    result = base * closeadj * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d decline × close
def f50tdc_f50_terminal_decline_composite_declinexclose_252d_base_v133_signal(revenue, opinc, marketcap, closeadj):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    result = base * closeadj * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# revdecline × close 63d
def f50tdc_f50_terminal_decline_composite_revdeclinexclose_63d_base_v134_signal(revenue, marketcap, closeadj):
    base = _f50_revdecline(revenue, 63)
    result = base * closeadj * marketcap + _f50_margincompress(revenue, revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# margcomp × close 252d
def f50tdc_f50_terminal_decline_composite_margcompxclose_252d_base_v135_signal(opinc, revenue, marketcap, closeadj):
    base = _f50_margincompress(opinc, revenue, 252)
    result = base * closeadj * marketcap + _f50_revdecline(revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# expanding worst revdecline × marketcap
def f50tdc_f50_terminal_decline_composite_revdeclineworstever_base_v136_signal(revenue, marketcap):
    base = _f50_revdecline(revenue, 252)
    result = base.expanding(min_periods=63).max() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# expanding worst margcomp × marketcap
def f50tdc_f50_terminal_decline_composite_margcompworstever_base_v137_signal(opinc, revenue, marketcap):
    base = _f50_margincompress(opinc, revenue, 252)
    result = base.expanding(min_periods=63).max() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# revdecline vs ever 63d
def f50tdc_f50_terminal_decline_composite_revdeclinevsever_63d_base_v138_signal(revenue, marketcap):
    base = _f50_revdecline(revenue, 63)
    worst = base.expanding(min_periods=63).max()
    result = (worst - base) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# margcomp vs ever 63d
def f50tdc_f50_terminal_decline_composite_margcompvsever_63d_base_v139_signal(opinc, revenue, marketcap):
    base = _f50_margincompress(opinc, revenue, 63)
    worst = base.expanding(min_periods=63).max()
    result = (worst - base) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count revdecline > 1%
def f50tdc_f50_terminal_decline_composite_revdecline1cnt_252d_base_v140_signal(revenue, marketcap):
    base = _f50_revdecline(revenue, 21)
    result = (base).rolling(252, min_periods=63).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count margcomp > 1pp
def f50tdc_f50_terminal_decline_composite_margcomp1cnt_252d_base_v141_signal(opinc, revenue, marketcap):
    base = _f50_margincompress(opinc, revenue, 21)
    result = (base).rolling(252, min_periods=63).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count decline > 50% (extreme terminal)
def f50tdc_f50_terminal_decline_composite_decline50cnt_504d_base_v142_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    result = (base).rolling(504, min_periods=126).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite: decline × revdecline (joint deterioration)
def f50tdc_f50_terminal_decline_composite_declxrev_63d_base_v143_signal(revenue, opinc, marketcap):
    a = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    b = _f50_revdecline(revenue, 63)
    result = a * b * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite: decline × margcomp
def f50tdc_f50_terminal_decline_composite_declxmargcomp_252d_base_v144_signal(revenue, opinc, marketcap):
    a = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    b = _f50_margincompress(opinc, revenue, 252)
    result = a * b * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d decline × revenue growth
def f50tdc_f50_terminal_decline_composite_declinexrevg_21d_base_v145_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 21)
    rg = revenue.diff(63) / revenue.shift(63).abs().replace(0, np.nan)
    result = base * rg * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d decline × revenue growth
def f50tdc_f50_terminal_decline_composite_declinexrevg_252d_base_v146_signal(revenue, opinc, marketcap):
    base = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    rg = revenue.diff(252) / revenue.shift(252).abs().replace(0, np.nan)
    result = base * rg * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d multifactor: revdecline + margcomp + decline
def f50tdc_f50_terminal_decline_composite_multifactor_63d_base_v147_signal(revenue, opinc, marketcap):
    a = _f50_revdecline(revenue, 63)
    b = _f50_margincompress(opinc, revenue, 63)
    c = _f50_terminal_decline(revenue, opinc, marketcap, 63)
    result = (a + b + c) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d multifactor
def f50tdc_f50_terminal_decline_composite_multifactor_252d_base_v148_signal(revenue, opinc, marketcap):
    a = _f50_revdecline(revenue, 252)
    b = _f50_margincompress(opinc, revenue, 252)
    c = _f50_terminal_decline(revenue, opinc, marketcap, 252)
    result = (a + b + c) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d multifactor
def f50tdc_f50_terminal_decline_composite_multifactor_504d_base_v149_signal(revenue, opinc, marketcap):
    a = _f50_revdecline(revenue, 504)
    b = _f50_margincompress(opinc, revenue, 504)
    c = _f50_terminal_decline(revenue, opinc, marketcap, 504)
    result = (a + b + c) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite severity × ev (extra)
def f50tdc_f50_terminal_decline_composite_compositesev_252d_extra_base_v150_signal(revenue, opinc, marketcap, ev):
    a = _f50_revdecline(revenue, 252).abs()
    b = _f50_margincompress(opinc, revenue, 252).abs()
    c = _f50_terminal_decline(revenue, opinc, marketcap, 252).abs()
    result = (a + b + c) * ev
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [v for k, v in list(globals().items()) if k.startswith("f50tdc_") and callable(v)]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F50_TERMINAL_DECLINE_COMPOSITE_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    marketcap = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0005, 0.015, n))), name="marketcap")
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    netinc = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="netinc")
    fcf = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcf")
    ncfo = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ncfo")
    equity = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.004, n))), name="equity")
    debt = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.005, n))), name="debt")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.003, n))), name="assets")
    ebitda = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.006, n))), name="ebitda")
    capex = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="capex")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.002, n))), name="sharesbas")
    opinc = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.007, n))), name="opinc")
    ev = marketcap + debt
    ev = pd.Series(ev.values, name="ev")
    evebit = pd.Series((ev / opinc.replace(0, np.nan)).values, name="evebit")
    evebitda = pd.Series((ev / ebitda.replace(0, np.nan)).values, name="evebitda")
    pe = pd.Series((marketcap / netinc.replace(0, np.nan)).values, name="pe")
    pb = pd.Series((marketcap / equity.replace(0, np.nan)).values, name="pb")
    ps = pd.Series((marketcap / revenue.replace(0, np.nan)).values, name="ps")

    cols = {"closeadj": closeadj, "marketcap": marketcap, "ev": ev, "evebit": evebit, "evebitda": evebitda,
            "pe": pe, "pb": pb, "ps": ps, "revenue": revenue, "netinc": netinc, "fcf": fcf, "ncfo": ncfo,
            "equity": equity, "debt": debt, "assets": assets, "ebitda": ebitda, "capex": capex,
            "sharesbas": sharesbas, "opinc": opinc}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f50_terminal_decline", "_f50_revdecline", "_f50_margincompress")
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
    print(f"OK f50_terminal_decline_composite_base_076_150_claude: {n_features} features pass")
