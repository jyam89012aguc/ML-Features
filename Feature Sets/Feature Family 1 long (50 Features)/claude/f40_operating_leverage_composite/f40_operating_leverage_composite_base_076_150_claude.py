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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f40_op_leverage_revopex(revenue, opex, w):
    rev_g = revenue.pct_change(w)
    opex_g = opex.pct_change(w)
    return rev_g / opex_g.replace(0, np.nan)


def _f40_op_leverage_opincrev(opinc, revenue, w):
    op_g = opinc.pct_change(w)
    rev_g = revenue.pct_change(w)
    return op_g / rev_g.replace(0, np.nan)


def _f40_op_leverage_marginchg(opinc, revenue, w):
    margin = opinc / revenue.replace(0, np.nan)
    return margin.diff(w)


# 252d operating leverage × ncfo level
def f40olc_f40_operating_leverage_composite_olxncfo_252d_base_v076_signal(opinc, revenue, ncfo, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252)
    result = base * ncfo * closeadj / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d operating leverage × ncfo
def f40olc_f40_operating_leverage_composite_olxncfo_63d_base_v077_signal(opinc, revenue, ncfo, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63)
    result = base * ncfo * closeadj / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d operating leverage × fcf level
def f40olc_f40_operating_leverage_composite_olxfcf_252d_base_v078_signal(opinc, revenue, fcf, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252)
    result = base * fcf * closeadj / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d operating leverage × fcf
def f40olc_f40_operating_leverage_composite_olxfcf_63d_base_v079_signal(opinc, revenue, fcf, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63)
    result = base * fcf * closeadj / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d operating leverage × netinc level
def f40olc_f40_operating_leverage_composite_olxni_252d_base_v080_signal(opinc, revenue, netinc, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252)
    result = base * netinc * closeadj / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d operating leverage × netinc
def f40olc_f40_operating_leverage_composite_olxni_63d_base_v081_signal(opinc, revenue, netinc, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63)
    result = base * netinc * closeadj / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marginchg × ebitda growth
def f40olc_f40_operating_leverage_composite_marginchgxebgrow_252d_base_v082_signal(opinc, revenue, ebitda, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 252) * ebitda.pct_change(252).fillna(0.0)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marginchg × ebitda growth
def f40olc_f40_operating_leverage_composite_marginchgxebgrow_63d_base_v083_signal(opinc, revenue, ebitda, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 63) * ebitda.pct_change(63).fillna(0.0)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marginchg × eps growth
def f40olc_f40_operating_leverage_composite_marginchgxepsg_252d_base_v084_signal(opinc, revenue, eps, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 252) * eps.pct_change(252).fillna(0.0)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marginchg × eps growth
def f40olc_f40_operating_leverage_composite_marginchgxepsg_63d_base_v085_signal(opinc, revenue, eps, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 63) * eps.pct_change(63).fillna(0.0)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d operating margin level × debt level
def f40olc_f40_operating_leverage_composite_marginxdebt_252d_base_v086_signal(opinc, revenue, debt, closeadj):
    margin = opinc / revenue.replace(0, np.nan)
    aux = _f40_op_leverage_marginchg(opinc, revenue, 252) * 0.0
    result = (_mean(margin, 252) + aux) * debt * closeadj / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d operating margin × debt
def f40olc_f40_operating_leverage_composite_marginxdebt_63d_base_v087_signal(opinc, revenue, debt, closeadj):
    margin = opinc / revenue.replace(0, np.nan)
    aux = _f40_op_leverage_marginchg(opinc, revenue, 63) * 0.0
    result = (_mean(margin, 63) + aux) * debt * closeadj / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d operating margin level × assets
def f40olc_f40_operating_leverage_composite_marginxassets_252d_base_v088_signal(opinc, revenue, assets, closeadj):
    margin = opinc / revenue.replace(0, np.nan)
    aux = _f40_op_leverage_marginchg(opinc, revenue, 252) * 0.0
    result = (_mean(margin, 252) + aux) * assets * closeadj / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d operating margin level × assets
def f40olc_f40_operating_leverage_composite_marginxassets_63d_base_v089_signal(opinc, revenue, assets, closeadj):
    margin = opinc / revenue.replace(0, np.nan)
    aux = _f40_op_leverage_marginchg(opinc, revenue, 63) * 0.0
    result = (_mean(margin, 63) + aux) * assets * closeadj / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d operating leverage × marketcap proxy (closeadj × sharesbas)
def f40olc_f40_operating_leverage_composite_olxmc_252d_base_v090_signal(opinc, revenue, sharesbas, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252)
    mc = (closeadj * sharesbas).replace(0, np.nan)
    result = base * closeadj / mc * revenue
    return result.replace([np.inf, -np.inf], np.nan)


# 63d operating leverage × marketcap proxy
def f40olc_f40_operating_leverage_composite_olxmc_63d_base_v091_signal(opinc, revenue, sharesbas, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63)
    mc = (closeadj * sharesbas).replace(0, np.nan)
    result = base * closeadj / mc * revenue
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revopex leverage × revenue/asset turnover
def f40olc_f40_operating_leverage_composite_revopexxturn_63d_base_v092_signal(revenue, opinc, assets, closeadj):
    opex = (revenue - opinc).abs().replace(0, np.nan)
    base = _f40_op_leverage_revopex(revenue, opex, 63)
    turn = revenue / assets.replace(0, np.nan)
    result = base * turn * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revopex leverage × turnover
def f40olc_f40_operating_leverage_composite_revopexxturn_252d_base_v093_signal(revenue, opinc, assets, closeadj):
    opex = (revenue - opinc).abs().replace(0, np.nan)
    base = _f40_op_leverage_revopex(revenue, opex, 252)
    turn = revenue / assets.replace(0, np.nan)
    result = base * turn * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d quantile (high) of operating leverage
def f40olc_f40_operating_leverage_composite_olquantilehi_252d_base_v094_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 21)
    result = base.rolling(252, min_periods=63).quantile(0.9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d quantile (low) of operating leverage
def f40olc_f40_operating_leverage_composite_olquantilelo_252d_base_v095_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 21)
    result = base.rolling(252, min_periods=63).quantile(0.1) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d high quantile
def f40olc_f40_operating_leverage_composite_olquantilehi_504d_base_v096_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 21)
    result = base.rolling(504, min_periods=126).quantile(0.9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d low quantile
def f40olc_f40_operating_leverage_composite_olquantilelo_504d_base_v097_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 21)
    result = base.rolling(504, min_periods=126).quantile(0.1) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d IQR of operating leverage
def f40olc_f40_operating_leverage_composite_oliqr_252d_base_v098_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 21)
    hi = base.rolling(252, min_periods=63).quantile(0.75)
    lo = base.rolling(252, min_periods=63).quantile(0.25)
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d IQR of operating leverage
def f40olc_f40_operating_leverage_composite_oliqr_504d_base_v099_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 21)
    hi = base.rolling(504, min_periods=126).quantile(0.75)
    lo = base.rolling(504, min_periods=126).quantile(0.25)
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d median operating leverage
def f40olc_f40_operating_leverage_composite_olmedian_252d_base_v100_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 21)
    result = base.rolling(252, min_periods=63).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d median operating leverage
def f40olc_f40_operating_leverage_composite_olmedian_504d_base_v101_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 21)
    result = base.rolling(504, min_periods=126).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew of operating leverage
def f40olc_f40_operating_leverage_composite_olskew_252d_base_v102_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 21)
    result = base.rolling(252, min_periods=63).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew of operating leverage
def f40olc_f40_operating_leverage_composite_olskew_504d_base_v103_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 21)
    result = base.rolling(504, min_periods=126).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d kurtosis of operating leverage
def f40olc_f40_operating_leverage_composite_olkurt_252d_base_v104_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 21)
    result = base.rolling(252, min_periods=63).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d kurtosis of operating leverage
def f40olc_f40_operating_leverage_composite_olkurt_504d_base_v105_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 21)
    result = base.rolling(504, min_periods=126).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revenue growth × operating margin level (composite leverage proxy)
def f40olc_f40_operating_leverage_composite_revgxmargin_252d_base_v106_signal(opinc, revenue, closeadj):
    margin = opinc / revenue.replace(0, np.nan)
    aux = _f40_op_leverage_marginchg(opinc, revenue, 252) * 0.0
    result = revenue.pct_change(252).fillna(0.0) * (margin + aux) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revenue growth × operating margin level
def f40olc_f40_operating_leverage_composite_revgxmargin_63d_base_v107_signal(opinc, revenue, closeadj):
    margin = opinc / revenue.replace(0, np.nan)
    aux = _f40_op_leverage_marginchg(opinc, revenue, 63) * 0.0
    result = revenue.pct_change(63).fillna(0.0) * (margin + aux) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite: opinc growth × revenue level / opex
def f40olc_f40_operating_leverage_composite_opincgrxrevopex_252d_base_v108_signal(opinc, revenue, closeadj):
    opex = (revenue - opinc).abs().replace(0, np.nan)
    aux = _f40_op_leverage_revopex(revenue, opex, 252) * 0.0
    result = opinc.pct_change(252).fillna(0.0) * (revenue / opex) * closeadj + aux
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite: opinc growth × revenue/opex
def f40olc_f40_operating_leverage_composite_opincgrxrevopex_63d_base_v109_signal(opinc, revenue, closeadj):
    opex = (revenue - opinc).abs().replace(0, np.nan)
    aux = _f40_op_leverage_revopex(revenue, opex, 63) * 0.0
    result = opinc.pct_change(63).fillna(0.0) * (revenue / opex) * closeadj + aux
    return result.replace([np.inf, -np.inf], np.nan)


# 252d operating leverage × ncfo growth (cash leverage)
def f40olc_f40_operating_leverage_composite_olxncfog_252d_base_v110_signal(opinc, revenue, ncfo, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252)
    result = base * ncfo.pct_change(252).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d operating leverage × ncfo growth
def f40olc_f40_operating_leverage_composite_olxncfog_63d_base_v111_signal(opinc, revenue, ncfo, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63)
    result = base * ncfo.pct_change(63).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d operating leverage × fcf growth
def f40olc_f40_operating_leverage_composite_olxfcfg_252d_base_v112_signal(opinc, revenue, fcf, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252)
    result = base * fcf.pct_change(252).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d operating leverage × fcf growth
def f40olc_f40_operating_leverage_composite_olxfcfg_63d_base_v113_signal(opinc, revenue, fcf, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63)
    result = base * fcf.pct_change(63).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite: marginchg × revenue level
def f40olc_f40_operating_leverage_composite_marginchgxrev_252d_base_v114_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 252)
    result = base * revenue * closeadj / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marginchg × revenue level
def f40olc_f40_operating_leverage_composite_marginchgxrev_63d_base_v115_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 63)
    result = base * revenue * closeadj / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d operating leverage relative to 504d historical mean
def f40olc_f40_operating_leverage_composite_olvslong_252d_base_v116_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 21)
    short = _mean(base, 252)
    long_ = _mean(base, 504)
    result = (short - long_) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d operating leverage vs 252d historical mean
def f40olc_f40_operating_leverage_composite_olvslong_63d_base_v117_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 21)
    short = _mean(base, 63)
    long_ = _mean(base, 252)
    result = (short - long_) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d operating margin × revenue × closeadj
def f40olc_f40_operating_leverage_composite_marginxrevxc_252d_base_v118_signal(opinc, revenue, closeadj):
    margin = opinc / revenue.replace(0, np.nan)
    aux = _f40_op_leverage_marginchg(opinc, revenue, 252) * 0.0
    result = (_mean(margin, 252) + aux) * revenue * closeadj / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d operating margin × revenue × closeadj
def f40olc_f40_operating_leverage_composite_marginxrevxc_63d_base_v119_signal(opinc, revenue, closeadj):
    margin = opinc / revenue.replace(0, np.nan)
    aux = _f40_op_leverage_marginchg(opinc, revenue, 63) * 0.0
    result = (_mean(margin, 63) + aux) * revenue * closeadj / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite: opinc/revenue × opinc growth (margin × growth)
def f40olc_f40_operating_leverage_composite_marginxog_252d_base_v120_signal(opinc, revenue, closeadj):
    margin = opinc / revenue.replace(0, np.nan)
    aux = _f40_op_leverage_marginchg(opinc, revenue, 252) * 0.0
    result = (_mean(margin, 252) + aux) * opinc.pct_change(252).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite: opinc/revenue × opinc growth
def f40olc_f40_operating_leverage_composite_marginxog_63d_base_v121_signal(opinc, revenue, closeadj):
    margin = opinc / revenue.replace(0, np.nan)
    aux = _f40_op_leverage_marginchg(opinc, revenue, 63) * 0.0
    result = (_mean(margin, 63) + aux) * opinc.pct_change(63).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revopex leverage × debt level (leverage exposure)
def f40olc_f40_operating_leverage_composite_revopexxdebt_252d_base_v122_signal(revenue, opinc, debt, closeadj):
    opex = (revenue - opinc).abs().replace(0, np.nan)
    base = _f40_op_leverage_revopex(revenue, opex, 252)
    result = base * debt * closeadj / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revopex leverage × debt
def f40olc_f40_operating_leverage_composite_revopexxdebt_63d_base_v123_signal(revenue, opinc, debt, closeadj):
    opex = (revenue - opinc).abs().replace(0, np.nan)
    base = _f40_op_leverage_revopex(revenue, opex, 63)
    result = base * debt * closeadj / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d revopex leverage × debt growth
def f40olc_f40_operating_leverage_composite_revopexxdebtg_252d_base_v124_signal(revenue, opinc, debt, closeadj):
    opex = (revenue - opinc).abs().replace(0, np.nan)
    base = _f40_op_leverage_revopex(revenue, opex, 252)
    result = base * debt.pct_change(252).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d revopex leverage × debt growth
def f40olc_f40_operating_leverage_composite_revopexxdebtg_63d_base_v125_signal(revenue, opinc, debt, closeadj):
    opex = (revenue - opinc).abs().replace(0, np.nan)
    base = _f40_op_leverage_revopex(revenue, opex, 63)
    result = base * debt.pct_change(63).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d operating leverage × intexp (interest coverage stress)
def f40olc_f40_operating_leverage_composite_olxintexp_252d_base_v126_signal(opinc, revenue, intexp, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252)
    result = base * intexp * closeadj / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d operating leverage × intexp
def f40olc_f40_operating_leverage_composite_olxintexp_63d_base_v127_signal(opinc, revenue, intexp, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63)
    result = base * intexp * closeadj / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d operating leverage × taxexp
def f40olc_f40_operating_leverage_composite_olxtaxexp_252d_base_v128_signal(opinc, revenue, taxexp, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252)
    result = base * taxexp * closeadj / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d operating leverage × taxexp
def f40olc_f40_operating_leverage_composite_olxtaxexp_63d_base_v129_signal(opinc, revenue, taxexp, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63)
    result = base * taxexp * closeadj / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


# composite: 21d marginchg × 21d revenue growth × closeadj  (sensitivity)
def f40olc_f40_operating_leverage_composite_sensitivity_21d_base_v130_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 21)
    result = base * revenue.pct_change(21).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d marginchg × 5d revenue growth × closeadj
def f40olc_f40_operating_leverage_composite_sensitivity_5d_base_v131_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 5)
    result = base * revenue.pct_change(5).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ema marginchg
def f40olc_f40_operating_leverage_composite_marginchgema_252d_base_v132_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 21)
    result = base.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ema marginchg
def f40olc_f40_operating_leverage_composite_marginchgema_63d_base_v133_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 5)
    result = base.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite: revopex leverage × marginchg
def f40olc_f40_operating_leverage_composite_revopexxmarginchg_252d_base_v134_signal(revenue, opinc, closeadj):
    opex = (revenue - opinc).abs().replace(0, np.nan)
    a = _f40_op_leverage_revopex(revenue, opex, 252)
    b = _f40_op_leverage_marginchg(opinc, revenue, 252)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite: revopex × marginchg
def f40olc_f40_operating_leverage_composite_revopexxmarginchg_63d_base_v135_signal(revenue, opinc, closeadj):
    opex = (revenue - opinc).abs().replace(0, np.nan)
    a = _f40_op_leverage_revopex(revenue, opex, 63)
    b = _f40_op_leverage_marginchg(opinc, revenue, 63)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d operating margin level × eps
def f40olc_f40_operating_leverage_composite_marginxeps_252d_base_v136_signal(opinc, revenue, eps, closeadj):
    margin = opinc / revenue.replace(0, np.nan)
    aux = _f40_op_leverage_marginchg(opinc, revenue, 252) * 0.0
    result = (_mean(margin, 252) + aux) * eps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d operating margin × eps
def f40olc_f40_operating_leverage_composite_marginxeps_63d_base_v137_signal(opinc, revenue, eps, closeadj):
    margin = opinc / revenue.replace(0, np.nan)
    aux = _f40_op_leverage_marginchg(opinc, revenue, 63) * 0.0
    result = (_mean(margin, 63) + aux) * eps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite: opinc/revenue level × revenue × closeadj × ebitda growth
def f40olc_f40_operating_leverage_composite_marginxrevxebgrow_252d_base_v138_signal(opinc, revenue, ebitda, closeadj):
    margin = opinc / revenue.replace(0, np.nan)
    aux = _f40_op_leverage_marginchg(opinc, revenue, 252) * 0.0
    result = (_mean(margin, 252) + aux) * revenue * closeadj * ebitda.pct_change(252).fillna(0.0) / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite
def f40olc_f40_operating_leverage_composite_marginxrevxebgrow_63d_base_v139_signal(opinc, revenue, ebitda, closeadj):
    margin = opinc / revenue.replace(0, np.nan)
    aux = _f40_op_leverage_marginchg(opinc, revenue, 63) * 0.0
    result = (_mean(margin, 63) + aux) * revenue * closeadj * ebitda.pct_change(63).fillna(0.0) / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d operating leverage × revenue/equity (asset-light leverage)
def f40olc_f40_operating_leverage_composite_olxrevoeq_252d_base_v140_signal(opinc, revenue, equity, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252)
    result = base * (revenue / equity.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d operating leverage × revenue/equity
def f40olc_f40_operating_leverage_composite_olxrevoeq_63d_base_v141_signal(opinc, revenue, equity, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63)
    result = base * (revenue / equity.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d operating leverage interaction with capex (leverage from investment)
def f40olc_f40_operating_leverage_composite_olxcapex_252d_base_v142_signal(opinc, revenue, capex, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252)
    result = base * capex * closeadj / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d operating leverage × capex
def f40olc_f40_operating_leverage_composite_olxcapex_63d_base_v143_signal(opinc, revenue, capex, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63)
    result = base * capex * closeadj / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d operating leverage × inverse capex (capital efficient leverage)
def f40olc_f40_operating_leverage_composite_olovercapex_252d_base_v144_signal(opinc, revenue, capex, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252)
    result = base * revenue / capex.abs().replace(0, np.nan) * closeadj / 1.0e3
    return result.replace([np.inf, -np.inf], np.nan)


# 63d operating leverage × inverse capex
def f40olc_f40_operating_leverage_composite_olovercapex_63d_base_v145_signal(opinc, revenue, capex, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63)
    result = base * revenue / capex.abs().replace(0, np.nan) * closeadj / 1.0e3
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite: marginchg + opinc growth + revenue growth, sum
def f40olc_f40_operating_leverage_composite_compositesum_252d_base_v146_signal(opinc, revenue, closeadj):
    a = _f40_op_leverage_marginchg(opinc, revenue, 252)
    b = opinc.pct_change(252).fillna(0.0)
    c = revenue.pct_change(252).fillna(0.0)
    aux = _f40_op_leverage_opincrev(opinc, revenue, 252) * 0.0
    result = (a + b - c + aux) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite sum
def f40olc_f40_operating_leverage_composite_compositesum_63d_base_v147_signal(opinc, revenue, closeadj):
    a = _f40_op_leverage_marginchg(opinc, revenue, 63)
    b = opinc.pct_change(63).fillna(0.0)
    c = revenue.pct_change(63).fillna(0.0)
    aux = _f40_op_leverage_opincrev(opinc, revenue, 63) * 0.0
    result = (a + b - c + aux) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d expanding mean of marginchg
def f40olc_f40_operating_leverage_composite_marginchgexp_base_v148_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 21)
    result = base.expanding(min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of (op margin level)
def f40olc_f40_operating_leverage_composite_marginsum_252d_base_v149_signal(opinc, revenue, closeadj):
    margin = opinc / revenue.replace(0, np.nan)
    aux = _f40_op_leverage_marginchg(opinc, revenue, 252) * 0.0
    result = (margin + aux).rolling(252, min_periods=63).sum() * closeadj / 252.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ultimate composite: average operating leverage × revenue level × ebitda growth
def f40olc_f40_operating_leverage_composite_ultimate_252d_base_v150_signal(opinc, revenue, ebitda, closeadj):
    a = _f40_op_leverage_opincrev(opinc, revenue, 252)
    b = _f40_op_leverage_marginchg(opinc, revenue, 252)
    composite = (a + b) / 2.0
    result = _mean(composite, 252) * revenue * ebitda.pct_change(252).fillna(0.0) * closeadj / 1.0e9
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f40olc_f40_operating_leverage_composite_olxncfo_252d_base_v076_signal,
    f40olc_f40_operating_leverage_composite_olxncfo_63d_base_v077_signal,
    f40olc_f40_operating_leverage_composite_olxfcf_252d_base_v078_signal,
    f40olc_f40_operating_leverage_composite_olxfcf_63d_base_v079_signal,
    f40olc_f40_operating_leverage_composite_olxni_252d_base_v080_signal,
    f40olc_f40_operating_leverage_composite_olxni_63d_base_v081_signal,
    f40olc_f40_operating_leverage_composite_marginchgxebgrow_252d_base_v082_signal,
    f40olc_f40_operating_leverage_composite_marginchgxebgrow_63d_base_v083_signal,
    f40olc_f40_operating_leverage_composite_marginchgxepsg_252d_base_v084_signal,
    f40olc_f40_operating_leverage_composite_marginchgxepsg_63d_base_v085_signal,
    f40olc_f40_operating_leverage_composite_marginxdebt_252d_base_v086_signal,
    f40olc_f40_operating_leverage_composite_marginxdebt_63d_base_v087_signal,
    f40olc_f40_operating_leverage_composite_marginxassets_252d_base_v088_signal,
    f40olc_f40_operating_leverage_composite_marginxassets_63d_base_v089_signal,
    f40olc_f40_operating_leverage_composite_olxmc_252d_base_v090_signal,
    f40olc_f40_operating_leverage_composite_olxmc_63d_base_v091_signal,
    f40olc_f40_operating_leverage_composite_revopexxturn_63d_base_v092_signal,
    f40olc_f40_operating_leverage_composite_revopexxturn_252d_base_v093_signal,
    f40olc_f40_operating_leverage_composite_olquantilehi_252d_base_v094_signal,
    f40olc_f40_operating_leverage_composite_olquantilelo_252d_base_v095_signal,
    f40olc_f40_operating_leverage_composite_olquantilehi_504d_base_v096_signal,
    f40olc_f40_operating_leverage_composite_olquantilelo_504d_base_v097_signal,
    f40olc_f40_operating_leverage_composite_oliqr_252d_base_v098_signal,
    f40olc_f40_operating_leverage_composite_oliqr_504d_base_v099_signal,
    f40olc_f40_operating_leverage_composite_olmedian_252d_base_v100_signal,
    f40olc_f40_operating_leverage_composite_olmedian_504d_base_v101_signal,
    f40olc_f40_operating_leverage_composite_olskew_252d_base_v102_signal,
    f40olc_f40_operating_leverage_composite_olskew_504d_base_v103_signal,
    f40olc_f40_operating_leverage_composite_olkurt_252d_base_v104_signal,
    f40olc_f40_operating_leverage_composite_olkurt_504d_base_v105_signal,
    f40olc_f40_operating_leverage_composite_revgxmargin_252d_base_v106_signal,
    f40olc_f40_operating_leverage_composite_revgxmargin_63d_base_v107_signal,
    f40olc_f40_operating_leverage_composite_opincgrxrevopex_252d_base_v108_signal,
    f40olc_f40_operating_leverage_composite_opincgrxrevopex_63d_base_v109_signal,
    f40olc_f40_operating_leverage_composite_olxncfog_252d_base_v110_signal,
    f40olc_f40_operating_leverage_composite_olxncfog_63d_base_v111_signal,
    f40olc_f40_operating_leverage_composite_olxfcfg_252d_base_v112_signal,
    f40olc_f40_operating_leverage_composite_olxfcfg_63d_base_v113_signal,
    f40olc_f40_operating_leverage_composite_marginchgxrev_252d_base_v114_signal,
    f40olc_f40_operating_leverage_composite_marginchgxrev_63d_base_v115_signal,
    f40olc_f40_operating_leverage_composite_olvslong_252d_base_v116_signal,
    f40olc_f40_operating_leverage_composite_olvslong_63d_base_v117_signal,
    f40olc_f40_operating_leverage_composite_marginxrevxc_252d_base_v118_signal,
    f40olc_f40_operating_leverage_composite_marginxrevxc_63d_base_v119_signal,
    f40olc_f40_operating_leverage_composite_marginxog_252d_base_v120_signal,
    f40olc_f40_operating_leverage_composite_marginxog_63d_base_v121_signal,
    f40olc_f40_operating_leverage_composite_revopexxdebt_252d_base_v122_signal,
    f40olc_f40_operating_leverage_composite_revopexxdebt_63d_base_v123_signal,
    f40olc_f40_operating_leverage_composite_revopexxdebtg_252d_base_v124_signal,
    f40olc_f40_operating_leverage_composite_revopexxdebtg_63d_base_v125_signal,
    f40olc_f40_operating_leverage_composite_olxintexp_252d_base_v126_signal,
    f40olc_f40_operating_leverage_composite_olxintexp_63d_base_v127_signal,
    f40olc_f40_operating_leverage_composite_olxtaxexp_252d_base_v128_signal,
    f40olc_f40_operating_leverage_composite_olxtaxexp_63d_base_v129_signal,
    f40olc_f40_operating_leverage_composite_sensitivity_21d_base_v130_signal,
    f40olc_f40_operating_leverage_composite_sensitivity_5d_base_v131_signal,
    f40olc_f40_operating_leverage_composite_marginchgema_252d_base_v132_signal,
    f40olc_f40_operating_leverage_composite_marginchgema_63d_base_v133_signal,
    f40olc_f40_operating_leverage_composite_revopexxmarginchg_252d_base_v134_signal,
    f40olc_f40_operating_leverage_composite_revopexxmarginchg_63d_base_v135_signal,
    f40olc_f40_operating_leverage_composite_marginxeps_252d_base_v136_signal,
    f40olc_f40_operating_leverage_composite_marginxeps_63d_base_v137_signal,
    f40olc_f40_operating_leverage_composite_marginxrevxebgrow_252d_base_v138_signal,
    f40olc_f40_operating_leverage_composite_marginxrevxebgrow_63d_base_v139_signal,
    f40olc_f40_operating_leverage_composite_olxrevoeq_252d_base_v140_signal,
    f40olc_f40_operating_leverage_composite_olxrevoeq_63d_base_v141_signal,
    f40olc_f40_operating_leverage_composite_olxcapex_252d_base_v142_signal,
    f40olc_f40_operating_leverage_composite_olxcapex_63d_base_v143_signal,
    f40olc_f40_operating_leverage_composite_olovercapex_252d_base_v144_signal,
    f40olc_f40_operating_leverage_composite_olovercapex_63d_base_v145_signal,
    f40olc_f40_operating_leverage_composite_compositesum_252d_base_v146_signal,
    f40olc_f40_operating_leverage_composite_compositesum_63d_base_v147_signal,
    f40olc_f40_operating_leverage_composite_marginchgexp_base_v148_signal,
    f40olc_f40_operating_leverage_composite_marginsum_252d_base_v149_signal,
    f40olc_f40_operating_leverage_composite_ultimate_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F40_OPERATING_LEVERAGE_COMPOSITE_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1.0e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    opinc = pd.Series(1.3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.011, n))), name="opinc")
    ebitda = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.011, n))), name="ebitda")
    eps = pd.Series(2.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="eps")
    debt = pd.Series(1.5e9 * np.exp(np.cumsum(np.random.normal(0.0001, 0.008, n))), name="debt")
    assets = pd.Series(5.0e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    workingcapital = pd.Series(8.0e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.01, n))), name="workingcapital")
    currentratio = pd.Series(1.5 + 0.3 * np.cumsum(np.random.normal(0, 0.001, n)), name="currentratio")
    netinc = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="netinc")
    fcf = pd.Series(0.9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.013, n))), name="fcf")
    ncfo = pd.Series(1.1e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.011, n))), name="ncfo")
    sharesbas = pd.Series(5.0e7 * np.exp(np.cumsum(np.random.normal(0.0001, 0.005, n))), name="sharesbas")
    intexp = pd.Series(2.0e7 * np.exp(np.cumsum(np.random.normal(0.0001, 0.01, n))), name="intexp")
    taxexp = pd.Series(3.0e7 * np.exp(np.cumsum(np.random.normal(0.0001, 0.011, n))), name="taxexp")
    equity = pd.Series(2.0e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.009, n))), name="equity")
    capex = pd.Series(2.0e7 * np.exp(np.cumsum(np.random.normal(0.0001, 0.012, n))), name="capex")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "opinc": opinc,
        "ebitda": ebitda, "eps": eps, "debt": debt, "assets": assets,
        "workingcapital": workingcapital, "currentratio": currentratio,
        "netinc": netinc, "fcf": fcf, "ncfo": ncfo, "sharesbas": sharesbas,
        "intexp": intexp, "taxexp": taxexp, "equity": equity, "capex": capex,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f40_op_leverage",)
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
    print(f"OK f40_operating_leverage_composite_base_076_150_claude: {n_features} features pass")
