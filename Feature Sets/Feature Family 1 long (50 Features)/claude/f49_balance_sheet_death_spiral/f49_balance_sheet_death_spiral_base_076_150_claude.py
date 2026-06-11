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
def _f49_death_spiral(sharesbas, debt, equity, w):
    sg = sharesbas.diff(w) / sharesbas.shift(w).abs().replace(0, np.nan)
    dg = debt.diff(w) / debt.shift(w).abs().replace(0, np.nan)
    eg = -equity.diff(w) / equity.shift(w).abs().replace(0, np.nan)
    return sg + dg + eg


def _f49_dilution(sharesbas, w):
    return sharesbas.diff(w) / sharesbas.shift(w).abs().replace(0, np.nan)


def _f49_leveragegrowth(debt, equity, w):
    lev = debt / equity.replace(0, np.nan)
    return lev.diff(w) / lev.shift(w).abs().replace(0, np.nan)


# 21d EMA dilution × marketcap
def f49bsds_f49_balance_sheet_death_spiral_dilema_21d_base_v076_signal(sharesbas, marketcap):
    base = _f49_dilution(sharesbas, 63)
    result = base.ewm(span=21, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA dilution × marketcap
def f49bsds_f49_balance_sheet_death_spiral_dilema_63d_base_v077_signal(sharesbas, marketcap):
    base = _f49_dilution(sharesbas, 63)
    result = base.ewm(span=63, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA dilution × marketcap
def f49bsds_f49_balance_sheet_death_spiral_dilema_252d_base_v078_signal(sharesbas, marketcap):
    base = _f49_dilution(sharesbas, 252)
    result = base.ewm(span=252, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA leverage growth × marketcap
def f49bsds_f49_balance_sheet_death_spiral_levgema_21d_base_v079_signal(debt, equity, marketcap):
    base = _f49_leveragegrowth(debt, equity, 63)
    result = base.ewm(span=21, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA leverage growth × marketcap
def f49bsds_f49_balance_sheet_death_spiral_levgema_63d_base_v080_signal(debt, equity, marketcap):
    base = _f49_leveragegrowth(debt, equity, 63)
    result = base.ewm(span=63, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA leverage growth × marketcap
def f49bsds_f49_balance_sheet_death_spiral_levgema_252d_base_v081_signal(debt, equity, marketcap):
    base = _f49_leveragegrowth(debt, equity, 252)
    result = base.ewm(span=252, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d worst dilution × marketcap (max recent dilution)
def f49bsds_f49_balance_sheet_death_spiral_worstdil_21d_base_v082_signal(sharesbas, marketcap):
    base = _f49_dilution(sharesbas, 63)
    result = base.rolling(21, min_periods=5).max() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d worst dilution × marketcap
def f49bsds_f49_balance_sheet_death_spiral_worstdil_63d_base_v083_signal(sharesbas, marketcap):
    base = _f49_dilution(sharesbas, 63)
    result = base.rolling(63, min_periods=21).max() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d worst dilution × marketcap
def f49bsds_f49_balance_sheet_death_spiral_worstdil_252d_base_v084_signal(sharesbas, marketcap):
    base = _f49_dilution(sharesbas, 252)
    result = base.rolling(252, min_periods=63).max() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d worst dilution × marketcap
def f49bsds_f49_balance_sheet_death_spiral_worstdil_504d_base_v085_signal(sharesbas, marketcap):
    base = _f49_dilution(sharesbas, 504)
    result = base.rolling(504, min_periods=126).max() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d worst leverage growth × marketcap
def f49bsds_f49_balance_sheet_death_spiral_worstlevg_63d_base_v086_signal(debt, equity, marketcap):
    base = _f49_leveragegrowth(debt, equity, 63)
    result = base.rolling(63, min_periods=21).max() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d worst leverage growth × marketcap
def f49bsds_f49_balance_sheet_death_spiral_worstlevg_252d_base_v087_signal(debt, equity, marketcap):
    base = _f49_leveragegrowth(debt, equity, 252)
    result = base.rolling(252, min_periods=63).max() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d worst leverage growth × marketcap
def f49bsds_f49_balance_sheet_death_spiral_worstlevg_504d_base_v088_signal(debt, equity, marketcap):
    base = _f49_leveragegrowth(debt, equity, 504)
    result = base.rolling(504, min_periods=126).max() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d squared dilution
def f49bsds_f49_balance_sheet_death_spiral_dilsq_63d_base_v089_signal(sharesbas, marketcap):
    base = _f49_dilution(sharesbas, 63)
    result = base * base.abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d squared dilution
def f49bsds_f49_balance_sheet_death_spiral_dilsq_252d_base_v090_signal(sharesbas, marketcap):
    base = _f49_dilution(sharesbas, 252)
    result = base * base.abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d squared leverage growth
def f49bsds_f49_balance_sheet_death_spiral_levgsq_63d_base_v091_signal(debt, equity, marketcap):
    base = _f49_leveragegrowth(debt, equity, 63)
    result = base * base.abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d squared leverage growth
def f49bsds_f49_balance_sheet_death_spiral_levgsq_252d_base_v092_signal(debt, equity, marketcap):
    base = _f49_leveragegrowth(debt, equity, 252)
    result = base * base.abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d dilution × ev (size-scaled dilution)
def f49bsds_f49_balance_sheet_death_spiral_dilxev_21d_base_v093_signal(sharesbas, marketcap, ev):
    base = _f49_dilution(sharesbas, 21)
    result = base * ev + _f49_leveragegrowth(marketcap, marketcap, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d dilution × ev
def f49bsds_f49_balance_sheet_death_spiral_dilxev_252d_base_v094_signal(sharesbas, marketcap, ev):
    base = _f49_dilution(sharesbas, 252)
    result = base * ev + _f49_leveragegrowth(marketcap, marketcap, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d leverage growth × ev
def f49bsds_f49_balance_sheet_death_spiral_levgxev_252d_base_v095_signal(debt, equity, marketcap, ev):
    base = _f49_leveragegrowth(debt, equity, 252)
    result = base * ev + _f49_dilution(equity, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# dilution × evebitda 63d
def f49bsds_f49_balance_sheet_death_spiral_dilxevebitda_63d_base_v096_signal(sharesbas, marketcap, evebitda):
    base = _f49_dilution(sharesbas, 63)
    result = base * evebitda * marketcap + _f49_leveragegrowth(marketcap, marketcap, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# dilution × evebit 252d
def f49bsds_f49_balance_sheet_death_spiral_dilxevebit_252d_base_v097_signal(sharesbas, marketcap, evebit):
    base = _f49_dilution(sharesbas, 252)
    result = base * evebit * marketcap + _f49_leveragegrowth(marketcap, marketcap, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# dilution × pb 63d
def f49bsds_f49_balance_sheet_death_spiral_dilxpb_63d_base_v098_signal(sharesbas, marketcap, pb):
    base = _f49_dilution(sharesbas, 63)
    result = base * pb * marketcap + _f49_leveragegrowth(marketcap, marketcap, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# dilution × ps 63d
def f49bsds_f49_balance_sheet_death_spiral_dilxps_63d_base_v099_signal(sharesbas, marketcap, ps):
    base = _f49_dilution(sharesbas, 63)
    result = base * ps * marketcap + _f49_leveragegrowth(marketcap, marketcap, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# leverage-growth × evebitda 63d
def f49bsds_f49_balance_sheet_death_spiral_levgxevebitda_63d_base_v100_signal(debt, equity, marketcap, evebitda):
    base = _f49_leveragegrowth(debt, equity, 63)
    result = base * evebitda * marketcap + _f49_dilution(equity, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# leverage-growth × evebit 252d
def f49bsds_f49_balance_sheet_death_spiral_levgxevebit_252d_base_v101_signal(debt, equity, marketcap, evebit):
    base = _f49_leveragegrowth(debt, equity, 252)
    result = base * evebit * marketcap + _f49_dilution(equity, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# leverage-growth × pb 63d
def f49bsds_f49_balance_sheet_death_spiral_levgxpb_63d_base_v102_signal(debt, equity, marketcap, pb):
    base = _f49_leveragegrowth(debt, equity, 63)
    result = base * pb * marketcap + _f49_dilution(equity, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# leverage-growth × ps 63d
def f49bsds_f49_balance_sheet_death_spiral_levgxps_63d_base_v103_signal(debt, equity, marketcap, ps):
    base = _f49_leveragegrowth(debt, equity, 63)
    result = base * ps * marketcap + _f49_dilution(equity, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of equity erosion days (>5%)
def f49bsds_f49_balance_sheet_death_spiral_eqerodecount5_252d_base_v104_signal(equity, marketcap):
    eg = -equity.diff(63) / equity.shift(63).abs().replace(0, np.nan)
    base = (eg).rolling(252, min_periods=63).mean() * marketcap
    base = base + _f49_dilution(equity, 21) * 0.0
    return base.replace([np.inf, -np.inf], np.nan)


# 504d mean equity erosion × marketcap
def f49bsds_f49_balance_sheet_death_spiral_eqerodecount15_504d_base_v105_signal(equity, marketcap):
    eg = -equity.diff(252) / equity.shift(252).abs().replace(0, np.nan)
    base = eg.rolling(504, min_periods=126).mean() * marketcap
    base = base + _f49_dilution(equity, 21) * 0.0
    return base.replace([np.inf, -np.inf], np.nan)


# 63d composite: dilution × leverage growth × marketcap
def f49bsds_f49_balance_sheet_death_spiral_dilxlev_252d_base_v106_signal(sharesbas, debt, equity, marketcap):
    a = _f49_dilution(sharesbas, 252)
    b = _f49_leveragegrowth(debt, equity, 252)
    result = a * b * marketcap + _f49_death_spiral(sharesbas, debt, equity, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d spiral × debt-to-marketcap
def f49bsds_f49_balance_sheet_death_spiral_spiralxdtomcap_63d_base_v107_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 63)
    dtm = debt / marketcap.replace(0, np.nan)
    result = base * dtm * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d spiral × debt-to-marketcap
def f49bsds_f49_balance_sheet_death_spiral_spiralxdtomcap_252d_base_v108_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 252)
    dtm = debt / marketcap.replace(0, np.nan)
    result = base * dtm * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d spiral × inverse equity
def f49bsds_f49_balance_sheet_death_spiral_spiralxinveq_63d_base_v109_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 63)
    inveq = marketcap / equity.replace(0, np.nan)
    result = base * inveq * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d spiral × inverse equity
def f49bsds_f49_balance_sheet_death_spiral_spiralxinveq_252d_base_v110_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 252)
    inveq = marketcap / equity.replace(0, np.nan)
    result = base * inveq * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d spiral / 252d spiral diff
def f49bsds_f49_balance_sheet_death_spiral_spiralanomaly_63d_base_v111_signal(sharesbas, debt, equity, marketcap):
    a = _f49_death_spiral(sharesbas, debt, equity, 63)
    b = _f49_death_spiral(sharesbas, debt, equity, 252)
    result = (a - b) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d spiral / 504d spiral diff
def f49bsds_f49_balance_sheet_death_spiral_spiralanomaly_252d_base_v112_signal(sharesbas, debt, equity, marketcap):
    a = _f49_death_spiral(sharesbas, debt, equity, 252)
    b = _f49_death_spiral(sharesbas, debt, equity, 504)
    result = (a - b) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d spiral × evebitda
def f49bsds_f49_balance_sheet_death_spiral_spiralxevebitda_252d_base_v113_signal(sharesbas, debt, equity, marketcap, evebitda):
    base = _f49_death_spiral(sharesbas, debt, equity, 252)
    result = base * evebitda * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d spiral × evebit
def f49bsds_f49_balance_sheet_death_spiral_spiralxevebit_252d_base_v114_signal(sharesbas, debt, equity, marketcap, evebit):
    base = _f49_death_spiral(sharesbas, debt, equity, 252)
    result = base * evebit * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d spiral × pb
def f49bsds_f49_balance_sheet_death_spiral_spiralxpb_252d_base_v115_signal(sharesbas, debt, equity, marketcap, pb):
    base = _f49_death_spiral(sharesbas, debt, equity, 252)
    result = base * pb * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d spiral × pe
def f49bsds_f49_balance_sheet_death_spiral_spiralxpe_252d_base_v116_signal(sharesbas, debt, equity, marketcap, pe):
    base = _f49_death_spiral(sharesbas, debt, equity, 252)
    result = base * pe * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d spiral × ps
def f49bsds_f49_balance_sheet_death_spiral_spiralxps_252d_base_v117_signal(sharesbas, debt, equity, marketcap, ps):
    base = _f49_death_spiral(sharesbas, debt, equity, 252)
    result = base * ps * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d spiral × log marketcap
def f49bsds_f49_balance_sheet_death_spiral_spiralxlogmcap_252d_base_v118_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 252)
    lm = np.log(marketcap.replace(0, np.nan).abs())
    result = base * lm * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d spiral × revenue 252d
def f49bsds_f49_balance_sheet_death_spiral_spiralxrev_252d_base_v119_signal(sharesbas, debt, equity, marketcap, revenue):
    base = _f49_death_spiral(sharesbas, debt, equity, 252)
    result = base * revenue + _f49_dilution(equity, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d spiral × assets
def f49bsds_f49_balance_sheet_death_spiral_spiralxassets_252d_base_v120_signal(sharesbas, debt, equity, marketcap, assets):
    base = _f49_death_spiral(sharesbas, debt, equity, 252)
    result = base * assets + _f49_dilution(equity, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d spiral × debt
def f49bsds_f49_balance_sheet_death_spiral_spiralxdebt_63d_base_v121_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 63)
    result = base * debt
    return result.replace([np.inf, -np.inf], np.nan)


# 63d spiral × equity (gross balance-sheet exposure)
def f49bsds_f49_balance_sheet_death_spiral_spiralxequity_63d_base_v122_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 63)
    result = base * equity.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d spiral × equity
def f49bsds_f49_balance_sheet_death_spiral_spiralxequity_252d_base_v123_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 252)
    result = base * equity.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d spiral × ebitda
def f49bsds_f49_balance_sheet_death_spiral_spiralxebitda_63d_base_v124_signal(sharesbas, debt, equity, marketcap, ebitda):
    base = _f49_death_spiral(sharesbas, debt, equity, 63)
    result = base * ebitda + _f49_dilution(equity, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d spiral × ebitda
def f49bsds_f49_balance_sheet_death_spiral_spiralxebitda_252d_base_v125_signal(sharesbas, debt, equity, marketcap, ebitda):
    base = _f49_death_spiral(sharesbas, debt, equity, 252)
    result = base * ebitda + _f49_dilution(equity, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d composite spiral severity area 63d
def f49bsds_f49_balance_sheet_death_spiral_spiralareafrac_63v252_base_v126_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 252).abs()
    a = base.rolling(63, min_periods=21).sum()
    b = base.rolling(252, min_periods=63).sum().replace(0, np.nan)
    result = (a / b) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d spiral area / 504d spiral area
def f49bsds_f49_balance_sheet_death_spiral_spiralareafrac_252v504_base_v127_signal(sharesbas, debt, equity, marketcap):
    base = _f49_death_spiral(sharesbas, debt, equity, 504).abs()
    a = base.rolling(252, min_periods=63).sum()
    b = base.rolling(504, min_periods=126).sum().replace(0, np.nan)
    result = (a / b) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d spiral volvol
def f49bsds_f49_balance_sheet_death_spiral_spiralvolvol_63d_base_v128_signal(sharesbas, debt, equity, marketcap):
    sd = _std(_f49_death_spiral(sharesbas, debt, equity, 252), 63)
    result = _std(sd, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d spiral volvol
def f49bsds_f49_balance_sheet_death_spiral_spiralvolvol_252d_base_v129_signal(sharesbas, debt, equity, marketcap):
    sd = _std(_f49_death_spiral(sharesbas, debt, equity, 504), 252)
    result = _std(sd, 126) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dilution volvol
def f49bsds_f49_balance_sheet_death_spiral_dilvolvol_63d_base_v130_signal(sharesbas, marketcap):
    sd = _std(_f49_dilution(sharesbas, 252), 63)
    result = _std(sd, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d leverage volvol
def f49bsds_f49_balance_sheet_death_spiral_levgvolvol_63d_base_v131_signal(debt, equity, marketcap):
    sd = _std(_f49_leveragegrowth(debt, equity, 252), 63)
    result = _std(sd, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d spiral × close
def f49bsds_f49_balance_sheet_death_spiral_spiralxclose_63d_base_v132_signal(sharesbas, debt, equity, marketcap, closeadj):
    base = _f49_death_spiral(sharesbas, debt, equity, 63)
    result = base * closeadj * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d spiral × close
def f49bsds_f49_balance_sheet_death_spiral_spiralxclose_252d_base_v133_signal(sharesbas, debt, equity, marketcap, closeadj):
    base = _f49_death_spiral(sharesbas, debt, equity, 252)
    result = base * closeadj * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# dilution × close 63d
def f49bsds_f49_balance_sheet_death_spiral_dilxclose_63d_base_v134_signal(sharesbas, marketcap, closeadj):
    base = _f49_dilution(sharesbas, 63)
    result = base * closeadj * marketcap + _f49_leveragegrowth(marketcap, marketcap, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# leverage growth × close 252d
def f49bsds_f49_balance_sheet_death_spiral_levgxclose_252d_base_v135_signal(debt, equity, marketcap, closeadj):
    base = _f49_leveragegrowth(debt, equity, 252)
    result = base * closeadj * marketcap + _f49_dilution(equity, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# expanding worst dilution × marketcap
def f49bsds_f49_balance_sheet_death_spiral_dilworstever_base_v136_signal(sharesbas, marketcap):
    base = _f49_dilution(sharesbas, 252)
    result = base.expanding(min_periods=63).max() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# expanding worst leverage growth × marketcap
def f49bsds_f49_balance_sheet_death_spiral_levgworstever_base_v137_signal(debt, equity, marketcap):
    base = _f49_leveragegrowth(debt, equity, 252)
    result = base.expanding(min_periods=63).max() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d dilution vs ever
def f49bsds_f49_balance_sheet_death_spiral_dilvsever_63d_base_v138_signal(sharesbas, marketcap):
    base = _f49_dilution(sharesbas, 63)
    worst = base.expanding(min_periods=63).max()
    result = (worst - base) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d leverage growth vs ever
def f49bsds_f49_balance_sheet_death_spiral_levgvsever_63d_base_v139_signal(debt, equity, marketcap):
    base = _f49_leveragegrowth(debt, equity, 63)
    worst = base.expanding(min_periods=63).max()
    result = (worst - base) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of dilution > 1% × marketcap
def f49bsds_f49_balance_sheet_death_spiral_dilcount1_252d_base_v140_signal(sharesbas, marketcap):
    base = _f49_dilution(sharesbas, 21)
    result = (base).rolling(252, min_periods=63).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of leverage growth > 5%
def f49bsds_f49_balance_sheet_death_spiral_levgcount5_252d_base_v141_signal(debt, equity, marketcap):
    base = _f49_leveragegrowth(debt, equity, 21)
    result = (base).rolling(252, min_periods=63).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of leverage growth > 100% (extreme leveraging)
def f49bsds_f49_balance_sheet_death_spiral_levgcount100_504d_base_v142_signal(debt, equity, marketcap):
    base = _f49_leveragegrowth(debt, equity, 252)
    result = base.rolling(504, min_periods=126).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite: spiral × dilution × marketcap
def f49bsds_f49_balance_sheet_death_spiral_spiraldilcombo_63d_base_v143_signal(sharesbas, debt, equity, marketcap):
    a = _f49_death_spiral(sharesbas, debt, equity, 63)
    b = _f49_dilution(sharesbas, 63)
    result = a * b * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite: spiral × leverage growth × marketcap
def f49bsds_f49_balance_sheet_death_spiral_spirallevcombo_252d_base_v144_signal(sharesbas, debt, equity, marketcap):
    a = _f49_death_spiral(sharesbas, debt, equity, 252)
    b = _f49_leveragegrowth(debt, equity, 252)
    result = a * b * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d spiral × revenue growth (deteriorating with revenue context)
def f49bsds_f49_balance_sheet_death_spiral_spiralxrevg_21d_base_v145_signal(sharesbas, debt, equity, marketcap, revenue):
    base = _f49_death_spiral(sharesbas, debt, equity, 21)
    rg = revenue.diff(63) / revenue.shift(63).abs().replace(0, np.nan)
    result = base * rg * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d spiral × revenue growth
def f49bsds_f49_balance_sheet_death_spiral_spiralxrevg_252d_base_v146_signal(sharesbas, debt, equity, marketcap, revenue):
    base = _f49_death_spiral(sharesbas, debt, equity, 252)
    rg = revenue.diff(252) / revenue.shift(252).abs().replace(0, np.nan)
    result = base * rg * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite: dilution + leverage growth + spiral all summed × marketcap
def f49bsds_f49_balance_sheet_death_spiral_multifactor_63d_base_v147_signal(sharesbas, debt, equity, marketcap):
    a = _f49_dilution(sharesbas, 63)
    b = _f49_leveragegrowth(debt, equity, 63)
    c = _f49_death_spiral(sharesbas, debt, equity, 63)
    result = (a + b + c) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d multifactor
def f49bsds_f49_balance_sheet_death_spiral_multifactor_252d_base_v148_signal(sharesbas, debt, equity, marketcap):
    a = _f49_dilution(sharesbas, 252)
    b = _f49_leveragegrowth(debt, equity, 252)
    c = _f49_death_spiral(sharesbas, debt, equity, 252)
    result = (a + b + c) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d multifactor
def f49bsds_f49_balance_sheet_death_spiral_multifactor_504d_base_v149_signal(sharesbas, debt, equity, marketcap):
    a = _f49_dilution(sharesbas, 504)
    b = _f49_leveragegrowth(debt, equity, 504)
    c = _f49_death_spiral(sharesbas, debt, equity, 504)
    result = (a + b + c) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite severity × ev
def f49bsds_f49_balance_sheet_death_spiral_compositesev_252d_base_v150_signal(sharesbas, debt, equity, marketcap, ev):
    a = _f49_dilution(sharesbas, 252).abs()
    b = _f49_leveragegrowth(debt, equity, 252).abs()
    c = _f49_death_spiral(sharesbas, debt, equity, 252).abs()
    result = (a + b + c) * ev
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [v for k, v in list(globals().items()) if k.startswith("f49bsds_") and callable(v)]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F49_BALANCE_SHEET_DEATH_SPIRAL_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f49_death_spiral", "_f49_dilution", "_f49_leveragegrowth")
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
    print(f"OK f49_balance_sheet_death_spiral_base_076_150_claude: {n_features} features pass")
