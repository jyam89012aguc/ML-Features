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
def _f37_hypergrowth_growth_strength(revenue, w):
    g = revenue.pct_change(w)
    return (g - 0.30) * (g > -0.5).astype(float)


def _f37_hypergrowth_margin_expansion(netinc, revenue, w):
    m = _safe_div(netinc, revenue.abs())
    return _diff(m, w)


def _f37_hypergrowth_fcf_positivity(fcf, revenue, w):
    fm = _safe_div(fcf, revenue.abs())
    return fm * _mean(fm, w).clip(lower=-1.0, upper=1.0)


def _f37_hypergrowth_signature(revenue, netinc, fcf, w):
    g = _f37_hypergrowth_growth_strength(revenue, w)
    me = _f37_hypergrowth_margin_expansion(netinc, revenue, w)
    fp = _f37_hypergrowth_fcf_positivity(fcf, revenue, w)
    return g + me * 5.0 + fp


# 5d short hypergrowth growth strength × close
def f37hgs_f37_hypergrowth_signature_growthstrength_5d_base_v076_signal(revenue, closeadj):
    result = _f37_hypergrowth_growth_strength(revenue, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 10d short hypergrowth growth strength × close
def f37hgs_f37_hypergrowth_signature_growthstrength_10d_base_v077_signal(revenue, closeadj):
    result = _f37_hypergrowth_growth_strength(revenue, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d hypergrowth growth strength × close
def f37hgs_f37_hypergrowth_signature_growthstrength_42d_base_v078_signal(revenue, closeadj):
    result = _f37_hypergrowth_growth_strength(revenue, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d hypergrowth growth strength × close
def f37hgs_f37_hypergrowth_signature_growthstrength_189d_base_v079_signal(revenue, closeadj):
    result = _f37_hypergrowth_growth_strength(revenue, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d hypergrowth growth strength × close
def f37hgs_f37_hypergrowth_signature_growthstrength_504d_base_v080_signal(revenue, closeadj):
    result = _f37_hypergrowth_growth_strength(revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d margin expansion (op) × close
def f37hgs_f37_hypergrowth_signature_marginexpansion_op_5d_base_v081_signal(opinc, revenue, closeadj):
    result = _f37_hypergrowth_margin_expansion(opinc, revenue, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d margin expansion (op) × close
def f37hgs_f37_hypergrowth_signature_marginexpansion_op_21d_base_v082_signal(opinc, revenue, closeadj):
    result = _f37_hypergrowth_margin_expansion(opinc, revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d margin expansion (op) × close
def f37hgs_f37_hypergrowth_signature_marginexpansion_op_63d_base_v083_signal(opinc, revenue, closeadj):
    result = _f37_hypergrowth_margin_expansion(opinc, revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d margin expansion (op) × close
def f37hgs_f37_hypergrowth_signature_marginexpansion_op_252d_base_v084_signal(opinc, revenue, closeadj):
    result = _f37_hypergrowth_margin_expansion(opinc, revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d margin expansion (gp) × close
def f37hgs_f37_hypergrowth_signature_marginexpansion_gp_21d_base_v085_signal(gp, revenue, closeadj):
    result = _f37_hypergrowth_margin_expansion(gp, revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d margin expansion (gp) × close
def f37hgs_f37_hypergrowth_signature_marginexpansion_gp_252d_base_v086_signal(gp, revenue, closeadj):
    result = _f37_hypergrowth_margin_expansion(gp, revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d margin expansion (ebitda) × close
def f37hgs_f37_hypergrowth_signature_marginexpansion_ebitda_63d_base_v087_signal(ebitda, revenue, closeadj):
    result = _f37_hypergrowth_margin_expansion(ebitda, revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d margin expansion (ebitda) × close
def f37hgs_f37_hypergrowth_signature_marginexpansion_ebitda_252d_base_v088_signal(ebitda, revenue, closeadj):
    result = _f37_hypergrowth_margin_expansion(ebitda, revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d FCF positivity × close
def f37hgs_f37_hypergrowth_signature_fcfpositivity_5d_base_v089_signal(fcf, revenue, closeadj):
    result = _f37_hypergrowth_fcf_positivity(fcf, revenue, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d FCF positivity × close
def f37hgs_f37_hypergrowth_signature_fcfpositivity_42d_base_v090_signal(fcf, revenue, closeadj):
    result = _f37_hypergrowth_fcf_positivity(fcf, revenue, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d FCF positivity × close
def f37hgs_f37_hypergrowth_signature_fcfpositivity_504d_base_v091_signal(fcf, revenue, closeadj):
    result = _f37_hypergrowth_fcf_positivity(fcf, revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d signature with op-margin expansion × close
def f37hgs_f37_hypergrowth_signature_signature_op_21d_base_v092_signal(revenue, opinc, fcf, closeadj):
    result = _f37_hypergrowth_signature(revenue, opinc, fcf, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signature with op-margin expansion × close
def f37hgs_f37_hypergrowth_signature_signature_op_252d_base_v093_signal(revenue, opinc, fcf, closeadj):
    result = _f37_hypergrowth_signature(revenue, opinc, fcf, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signature with gp × close
def f37hgs_f37_hypergrowth_signature_signature_gp_252d_base_v094_signal(revenue, gp, fcf, closeadj):
    result = _f37_hypergrowth_signature(revenue, gp, fcf, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signature with ebitda margin × close
def f37hgs_f37_hypergrowth_signature_signature_ebitda_252d_base_v095_signal(revenue, ebitda, fcf, closeadj):
    result = _f37_hypergrowth_signature(revenue, ebitda, fcf, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signature with ncfo as cash proxy × close
def f37hgs_f37_hypergrowth_signature_signature_ncfo_63d_base_v096_signal(revenue, netinc, ncfo, closeadj):
    result = _f37_hypergrowth_signature(revenue, netinc, ncfo, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signature with ncfo × close
def f37hgs_f37_hypergrowth_signature_signature_ncfo_252d_base_v097_signal(revenue, netinc, ncfo, closeadj):
    result = _f37_hypergrowth_signature(revenue, netinc, ncfo, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite-style: growth × margin × FCFpos all multiplied
def f37hgs_f37_hypergrowth_signature_tripleproduct_63d_base_v098_signal(revenue, netinc, fcf, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 63)
    me = _f37_hypergrowth_margin_expansion(netinc, revenue, 63)
    fp = _f37_hypergrowth_fcf_positivity(fcf, revenue, 63)
    result = g * me * fp * closeadj * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d triple product
def f37hgs_f37_hypergrowth_signature_tripleproduct_252d_base_v099_signal(revenue, netinc, fcf, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 252)
    me = _f37_hypergrowth_margin_expansion(netinc, revenue, 252)
    fp = _f37_hypergrowth_fcf_positivity(fcf, revenue, 252)
    result = g * me * fp * closeadj * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d triple product
def f37hgs_f37_hypergrowth_signature_tripleproduct_504d_base_v100_signal(revenue, netinc, fcf, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 504)
    me = _f37_hypergrowth_margin_expansion(netinc, revenue, 504)
    fp = _f37_hypergrowth_fcf_positivity(fcf, revenue, 504)
    result = g * me * fp * closeadj * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signature × log(revenue) × close
def f37hgs_f37_hypergrowth_signature_signature_xlogrev_252d_base_v101_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    lr = np.log(revenue.abs() + 1.0)
    result = s * lr * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d growth × dollar volume sum
def f37hgs_f37_hypergrowth_signature_growthstrength_xdvsum_63d_base_v102_signal(revenue, closeadj, volume):
    g = _f37_hypergrowth_growth_strength(revenue, 63)
    dvs = (closeadj * volume).rolling(21, min_periods=5).sum()
    result = g * dvs * 1e-3
    return result.replace([np.inf, -np.inf], np.nan)


# 252d growth × dollar volume sum
def f37hgs_f37_hypergrowth_signature_growthstrength_xdvsum_252d_base_v103_signal(revenue, closeadj, volume):
    g = _f37_hypergrowth_growth_strength(revenue, 252)
    dvs = (closeadj * volume).rolling(63, min_periods=21).sum()
    result = g * dvs * 1e-3
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signature × tax expense × close
def f37hgs_f37_hypergrowth_signature_signature_xtaxexp_63d_base_v104_signal(revenue, netinc, fcf, taxexp, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    result = s * taxexp.abs() * closeadj * 1e-5
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signature × interest expense × close
def f37hgs_f37_hypergrowth_signature_signature_xintexp_252d_base_v105_signal(revenue, netinc, fcf, intexp, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    result = s * intexp.abs() * closeadj * 1e-5
    return result.replace([np.inf, -np.inf], np.nan)


# 21d signature * close-momentum × close
def f37hgs_f37_hypergrowth_signature_signature_xshortmom_21d_base_v106_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 21)
    mom = closeadj.pct_change(21)
    result = s * mom * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signature * 252d close-momentum × close
def f37hgs_f37_hypergrowth_signature_signature_xlongmom_252d_base_v107_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    mom = closeadj.pct_change(252)
    result = s * mom * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signature × close zscore (already-rich growth)
def f37hgs_f37_hypergrowth_signature_signature_xclosez_63d_base_v108_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    cz = _z(closeadj, 252)
    result = s * cz * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signature × close zscore
def f37hgs_f37_hypergrowth_signature_signature_xclosez_252d_base_v109_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    cz = _z(closeadj, 504)
    result = s * cz * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d growth × ebitda growth × close
def f37hgs_f37_hypergrowth_signature_growthxebitdagrowth_63d_base_v110_signal(revenue, ebitda, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 63)
    eg = ebitda.pct_change(63)
    result = g * eg * closeadj * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d growth × ebitda growth × close
def f37hgs_f37_hypergrowth_signature_growthxebitdagrowth_252d_base_v111_signal(revenue, ebitda, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 252)
    eg = ebitda.pct_change(252)
    result = g * eg * closeadj * 10.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signature × volume sum × close
def f37hgs_f37_hypergrowth_signature_signature_xvolsum_252d_base_v112_signal(revenue, netinc, fcf, closeadj, volume):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    vs = volume.rolling(63, min_periods=21).sum()
    result = s * vs * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signature × ATR-style range × close
def f37hgs_f37_hypergrowth_signature_signature_xrange_63d_base_v113_signal(revenue, netinc, fcf, closeadj, high, low):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    rng = (high - low).rolling(21, min_periods=5).mean()
    result = s * rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d growth × close × ATR-style range
def f37hgs_f37_hypergrowth_signature_growthxrange_21d_base_v114_signal(revenue, closeadj, high, low):
    g = _f37_hypergrowth_growth_strength(revenue, 21)
    rng = (high - low).rolling(21, min_periods=5).mean()
    result = g * rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signature × log(assets)
def f37hgs_f37_hypergrowth_signature_signature_xlogassets_252d_base_v115_signal(revenue, netinc, fcf, assets, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    la = np.log(assets.abs() + 1.0)
    result = s * la * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d|growth + |margin expansion| + FCF positivity (normalized magnitude)
def f37hgs_f37_hypergrowth_signature_magnitudesum_21d_base_v116_signal(revenue, netinc, fcf, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 21).abs()
    me = _f37_hypergrowth_margin_expansion(netinc, revenue, 21).abs() * 5.0
    fp = _f37_hypergrowth_fcf_positivity(fcf, revenue, 21).abs()
    result = (g + me + fp) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d magnitudesum
def f37hgs_f37_hypergrowth_signature_magnitudesum_252d_base_v117_signal(revenue, netinc, fcf, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 252).abs()
    me = _f37_hypergrowth_margin_expansion(netinc, revenue, 252).abs() * 5.0
    fp = _f37_hypergrowth_fcf_positivity(fcf, revenue, 252).abs()
    result = (g + me + fp) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signature × current ratio
def f37hgs_f37_hypergrowth_signature_signature_xcr_63d_base_v118_signal(revenue, netinc, fcf, currentratio, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    result = s * currentratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signature × asset turnover
def f37hgs_f37_hypergrowth_signature_signature_xato_252d_base_v119_signal(revenue, netinc, fcf, assets, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    ato = _safe_div(revenue, assets.abs())
    result = s * ato * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d signature dispersion (std over 63d) × close
def f37hgs_f37_hypergrowth_signature_signature_dispersion_63d_base_v120_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 21)
    result = _std(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signature dispersion × close
def f37hgs_f37_hypergrowth_signature_signature_dispersion_252d_base_v121_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    result = _std(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range of signature (max-min) × close
def f37hgs_f37_hypergrowth_signature_signature_range_252d_base_v122_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 21)
    rng = s.rolling(252, min_periods=63).max() - s.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signature × eps × close
def f37hgs_f37_hypergrowth_signature_signature_xepslevel_63d_base_v123_signal(revenue, netinc, fcf, eps, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    result = s * eps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signature × retained earnings
def f37hgs_f37_hypergrowth_signature_signature_xretearn_252d_base_v124_signal(revenue, netinc, fcf, retearn, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    result = s * retearn.abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 21d signature × short-return × close
def f37hgs_f37_hypergrowth_signature_signature_xshortret_21d_base_v125_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 21)
    r = closeadj.pct_change(5)
    result = s * r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d growth × current ratio
def f37hgs_f37_hypergrowth_signature_growthxcr_21d_base_v126_signal(revenue, currentratio, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 21)
    result = g * currentratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d growth × workingcapital
def f37hgs_f37_hypergrowth_signature_growthxwc_63d_base_v127_signal(revenue, workingcapital, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 63)
    result = g * workingcapital.abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d margin expansion × workingcapital
def f37hgs_f37_hypergrowth_signature_marginxwc_63d_base_v128_signal(netinc, revenue, workingcapital, closeadj):
    me = _f37_hypergrowth_margin_expansion(netinc, revenue, 63)
    result = me * workingcapital.abs() * closeadj * 1e-5
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF positivity × log(assets) × close
def f37hgs_f37_hypergrowth_signature_fcfposxlogassets_252d_base_v129_signal(fcf, revenue, assets, closeadj):
    fp = _f37_hypergrowth_fcf_positivity(fcf, revenue, 252)
    la = np.log(assets.abs() + 1.0)
    result = fp * la * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d growth + 252d signature (short-recent + persistent)
def f37hgs_f37_hypergrowth_signature_shortplus_long_252d_base_v130_signal(revenue, netinc, fcf, closeadj):
    g_short = _f37_hypergrowth_growth_strength(revenue, 21)
    s_long = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    result = (g_short + s_long) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signature × revenue level scaled
def f37hgs_f37_hypergrowth_signature_signature_xrevscale_63d_base_v131_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    rs = revenue.abs() ** 0.5
    result = s * rs * closeadj * 1e-3
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signature × revenue level
def f37hgs_f37_hypergrowth_signature_signature_xrevscale_252d_base_v132_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    rs = revenue.abs() ** 0.5
    result = s * rs * closeadj * 1e-3
    return result.replace([np.inf, -np.inf], np.nan)


# 63d growth × FCF margin × close
def f37hgs_f37_hypergrowth_signature_growthxfcfmargin_63d_base_v133_signal(revenue, fcf, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 63)
    fm = _safe_div(fcf, revenue.abs())
    result = g * fm * closeadj * _f37_hypergrowth_fcf_positivity(fcf, revenue, 63).clip(-1.0, 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d growth × FCF margin × close
def f37hgs_f37_hypergrowth_signature_growthxfcfmargin_252d_base_v134_signal(revenue, fcf, closeadj):
    g = _f37_hypergrowth_growth_strength(revenue, 252)
    fm = _safe_div(fcf, revenue.abs())
    result = g * fm * closeadj * _f37_hypergrowth_fcf_positivity(fcf, revenue, 252).clip(-1.0, 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signature × ncfi (capex investment proxy) × close
def f37hgs_f37_hypergrowth_signature_signature_xncfi_252d_base_v135_signal(revenue, netinc, fcf, ncfi, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    result = s * ncfi.abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signature × ncff (financing) × close
def f37hgs_f37_hypergrowth_signature_signature_xncff_63d_base_v136_signal(revenue, netinc, fcf, ncff, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    result = s * ncff.abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signature × log(equity)
def f37hgs_f37_hypergrowth_signature_signature_xlogequity_252d_base_v137_signal(revenue, netinc, fcf, equity, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    le = np.log(equity.abs() + 1.0)
    result = s * le * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d hypergrowth signature × volume × close
def f37hgs_f37_hypergrowth_signature_signature_xvol_21d_base_v138_signal(revenue, netinc, fcf, closeadj, volume):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 21)
    result = s * volume * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signature × revenue growth (compounding)
def f37hgs_f37_hypergrowth_signature_signature_xrevgrowth_252d_base_v139_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    rg = revenue.pct_change(252)
    result = s * rg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d momentum-amplified signature
def f37hgs_f37_hypergrowth_signature_signature_xrv_21d_base_v140_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 21)
    rv = _std(closeadj.pct_change(), 21)
    result = s * rv * closeadj * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d momentum-amplified signature
def f37hgs_f37_hypergrowth_signature_signature_xrv_63d_base_v141_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    rv = _std(closeadj.pct_change(), 63)
    result = s * rv * closeadj * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF positivity × ebitda
def f37hgs_f37_hypergrowth_signature_fcfposxebitda_21d_base_v142_signal(fcf, revenue, ebitda, closeadj):
    fp = _f37_hypergrowth_fcf_positivity(fcf, revenue, 21)
    result = fp * ebitda.abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF positivity × netinc
def f37hgs_f37_hypergrowth_signature_fcfposxnetinc_252d_base_v143_signal(fcf, revenue, netinc, closeadj):
    fp = _f37_hypergrowth_fcf_positivity(fcf, revenue, 252)
    result = fp * netinc.abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite: growth × FCF margin × volume zscore × close
def f37hgs_f37_hypergrowth_signature_composite_growth_fcf_vol_63d_base_v144_signal(revenue, fcf, closeadj, volume):
    g = _f37_hypergrowth_growth_strength(revenue, 63)
    fp = _f37_hypergrowth_fcf_positivity(fcf, revenue, 63)
    vz = _z(volume, 63)
    result = g * fp * vz * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite: signature × dollar volume sum
def f37hgs_f37_hypergrowth_signature_signature_xdvsum_252d_base_v145_signal(revenue, netinc, fcf, closeadj, volume):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 252)
    dvs = (closeadj * volume).rolling(63, min_periods=21).sum()
    result = s * dvs * 1e-9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signature EMA × close
def f37hgs_f37_hypergrowth_signature_signature_ema_63d_base_v146_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    result = s.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d signature EMA × close
def f37hgs_f37_hypergrowth_signature_signature_ema_126d_base_v147_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 126)
    result = s.ewm(span=126, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew of signature × close
def f37hgs_f37_hypergrowth_signature_signature_skew_252d_base_v148_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 21)
    result = s.rolling(252, min_periods=63).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d kurtosis of signature × close
def f37hgs_f37_hypergrowth_signature_signature_kurt_252d_base_v149_signal(revenue, netinc, fcf, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 21)
    result = s.rolling(252, min_periods=63).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signature × debt-to-equity proxy
def f37hgs_f37_hypergrowth_signature_signature_xde_63d_base_v150_signal(revenue, netinc, fcf, debt, equity, closeadj):
    s = _f37_hypergrowth_signature(revenue, netinc, fcf, 63)
    de = _safe_div(debt, equity.abs())
    result = s * de * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f37hgs_f37_hypergrowth_signature_growthstrength_5d_base_v076_signal,
    f37hgs_f37_hypergrowth_signature_growthstrength_10d_base_v077_signal,
    f37hgs_f37_hypergrowth_signature_growthstrength_42d_base_v078_signal,
    f37hgs_f37_hypergrowth_signature_growthstrength_189d_base_v079_signal,
    f37hgs_f37_hypergrowth_signature_growthstrength_504d_base_v080_signal,
    f37hgs_f37_hypergrowth_signature_marginexpansion_op_5d_base_v081_signal,
    f37hgs_f37_hypergrowth_signature_marginexpansion_op_21d_base_v082_signal,
    f37hgs_f37_hypergrowth_signature_marginexpansion_op_63d_base_v083_signal,
    f37hgs_f37_hypergrowth_signature_marginexpansion_op_252d_base_v084_signal,
    f37hgs_f37_hypergrowth_signature_marginexpansion_gp_21d_base_v085_signal,
    f37hgs_f37_hypergrowth_signature_marginexpansion_gp_252d_base_v086_signal,
    f37hgs_f37_hypergrowth_signature_marginexpansion_ebitda_63d_base_v087_signal,
    f37hgs_f37_hypergrowth_signature_marginexpansion_ebitda_252d_base_v088_signal,
    f37hgs_f37_hypergrowth_signature_fcfpositivity_5d_base_v089_signal,
    f37hgs_f37_hypergrowth_signature_fcfpositivity_42d_base_v090_signal,
    f37hgs_f37_hypergrowth_signature_fcfpositivity_504d_base_v091_signal,
    f37hgs_f37_hypergrowth_signature_signature_op_21d_base_v092_signal,
    f37hgs_f37_hypergrowth_signature_signature_op_252d_base_v093_signal,
    f37hgs_f37_hypergrowth_signature_signature_gp_252d_base_v094_signal,
    f37hgs_f37_hypergrowth_signature_signature_ebitda_252d_base_v095_signal,
    f37hgs_f37_hypergrowth_signature_signature_ncfo_63d_base_v096_signal,
    f37hgs_f37_hypergrowth_signature_signature_ncfo_252d_base_v097_signal,
    f37hgs_f37_hypergrowth_signature_tripleproduct_63d_base_v098_signal,
    f37hgs_f37_hypergrowth_signature_tripleproduct_252d_base_v099_signal,
    f37hgs_f37_hypergrowth_signature_tripleproduct_504d_base_v100_signal,
    f37hgs_f37_hypergrowth_signature_signature_xlogrev_252d_base_v101_signal,
    f37hgs_f37_hypergrowth_signature_growthstrength_xdvsum_63d_base_v102_signal,
    f37hgs_f37_hypergrowth_signature_growthstrength_xdvsum_252d_base_v103_signal,
    f37hgs_f37_hypergrowth_signature_signature_xtaxexp_63d_base_v104_signal,
    f37hgs_f37_hypergrowth_signature_signature_xintexp_252d_base_v105_signal,
    f37hgs_f37_hypergrowth_signature_signature_xshortmom_21d_base_v106_signal,
    f37hgs_f37_hypergrowth_signature_signature_xlongmom_252d_base_v107_signal,
    f37hgs_f37_hypergrowth_signature_signature_xclosez_63d_base_v108_signal,
    f37hgs_f37_hypergrowth_signature_signature_xclosez_252d_base_v109_signal,
    f37hgs_f37_hypergrowth_signature_growthxebitdagrowth_63d_base_v110_signal,
    f37hgs_f37_hypergrowth_signature_growthxebitdagrowth_252d_base_v111_signal,
    f37hgs_f37_hypergrowth_signature_signature_xvolsum_252d_base_v112_signal,
    f37hgs_f37_hypergrowth_signature_signature_xrange_63d_base_v113_signal,
    f37hgs_f37_hypergrowth_signature_growthxrange_21d_base_v114_signal,
    f37hgs_f37_hypergrowth_signature_signature_xlogassets_252d_base_v115_signal,
    f37hgs_f37_hypergrowth_signature_magnitudesum_21d_base_v116_signal,
    f37hgs_f37_hypergrowth_signature_magnitudesum_252d_base_v117_signal,
    f37hgs_f37_hypergrowth_signature_signature_xcr_63d_base_v118_signal,
    f37hgs_f37_hypergrowth_signature_signature_xato_252d_base_v119_signal,
    f37hgs_f37_hypergrowth_signature_signature_dispersion_63d_base_v120_signal,
    f37hgs_f37_hypergrowth_signature_signature_dispersion_252d_base_v121_signal,
    f37hgs_f37_hypergrowth_signature_signature_range_252d_base_v122_signal,
    f37hgs_f37_hypergrowth_signature_signature_xepslevel_63d_base_v123_signal,
    f37hgs_f37_hypergrowth_signature_signature_xretearn_252d_base_v124_signal,
    f37hgs_f37_hypergrowth_signature_signature_xshortret_21d_base_v125_signal,
    f37hgs_f37_hypergrowth_signature_growthxcr_21d_base_v126_signal,
    f37hgs_f37_hypergrowth_signature_growthxwc_63d_base_v127_signal,
    f37hgs_f37_hypergrowth_signature_marginxwc_63d_base_v128_signal,
    f37hgs_f37_hypergrowth_signature_fcfposxlogassets_252d_base_v129_signal,
    f37hgs_f37_hypergrowth_signature_shortplus_long_252d_base_v130_signal,
    f37hgs_f37_hypergrowth_signature_signature_xrevscale_63d_base_v131_signal,
    f37hgs_f37_hypergrowth_signature_signature_xrevscale_252d_base_v132_signal,
    f37hgs_f37_hypergrowth_signature_growthxfcfmargin_63d_base_v133_signal,
    f37hgs_f37_hypergrowth_signature_growthxfcfmargin_252d_base_v134_signal,
    f37hgs_f37_hypergrowth_signature_signature_xncfi_252d_base_v135_signal,
    f37hgs_f37_hypergrowth_signature_signature_xncff_63d_base_v136_signal,
    f37hgs_f37_hypergrowth_signature_signature_xlogequity_252d_base_v137_signal,
    f37hgs_f37_hypergrowth_signature_signature_xvol_21d_base_v138_signal,
    f37hgs_f37_hypergrowth_signature_signature_xrevgrowth_252d_base_v139_signal,
    f37hgs_f37_hypergrowth_signature_signature_xrv_21d_base_v140_signal,
    f37hgs_f37_hypergrowth_signature_signature_xrv_63d_base_v141_signal,
    f37hgs_f37_hypergrowth_signature_fcfposxebitda_21d_base_v142_signal,
    f37hgs_f37_hypergrowth_signature_fcfposxnetinc_252d_base_v143_signal,
    f37hgs_f37_hypergrowth_signature_composite_growth_fcf_vol_63d_base_v144_signal,
    f37hgs_f37_hypergrowth_signature_signature_xdvsum_252d_base_v145_signal,
    f37hgs_f37_hypergrowth_signature_signature_ema_63d_base_v146_signal,
    f37hgs_f37_hypergrowth_signature_signature_ema_126d_base_v147_signal,
    f37hgs_f37_hypergrowth_signature_signature_skew_252d_base_v148_signal,
    f37hgs_f37_hypergrowth_signature_signature_kurt_252d_base_v149_signal,
    f37hgs_f37_hypergrowth_signature_signature_xde_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F37_HYPERGROWTH_SIGNATURE_REGISTRY_076_150 = REGISTRY


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
    revenue = pd.Series(1e7 * np.exp(np.cumsum(np.random.normal(0.0008, 0.01, n))), name="revenue")
    netinc = pd.Series(1e6 * np.exp(np.cumsum(np.random.normal(0.0006, 0.012, n))) * np.sign(np.random.normal(0.5, 1.0, n)), name="netinc")
    opinc = pd.Series(1.5e6 * np.exp(np.cumsum(np.random.normal(0.0006, 0.011, n))) * np.sign(np.random.normal(0.6, 1.0, n)), name="opinc")
    gp = pd.Series(3e6 * np.exp(np.cumsum(np.random.normal(0.0007, 0.009, n))), name="gp")
    ebitda = pd.Series(2e6 * np.exp(np.cumsum(np.random.normal(0.0006, 0.01, n))) * np.sign(np.random.normal(0.7, 1.0, n)), name="ebitda")
    eps = pd.Series(np.cumsum(np.random.normal(0.001, 0.05, n)) + 1.0, name="eps")
    fcf = pd.Series(8e5 * np.exp(np.cumsum(np.random.normal(0.0005, 0.013, n))) * np.sign(np.random.normal(0.6, 1.0, n)), name="fcf")
    ncfo = pd.Series(1.2e6 * np.exp(np.cumsum(np.random.normal(0.0006, 0.012, n))) * np.sign(np.random.normal(0.8, 1.0, n)), name="ncfo")
    ncfi = pd.Series(7e5 * np.exp(np.cumsum(np.random.normal(0.0003, 0.011, n))) * np.sign(np.random.normal(0.4, 1.0, n)), name="ncfi")
    ncff = pd.Series(6e5 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))) * np.sign(np.random.normal(0.3, 1.0, n)), name="ncff")
    capex = pd.Series(9e5 * np.exp(np.cumsum(np.random.normal(0.0004, 0.011, n))), name="capex")
    intexp = pd.Series(2e5 * np.exp(np.cumsum(np.random.normal(0.0003, 0.008, n))), name="intexp")
    taxexp = pd.Series(3e5 * np.exp(np.cumsum(np.random.normal(0.0004, 0.009, n))), name="taxexp")
    sharesbas = pd.Series(1e7 + np.cumsum(np.random.normal(1e3, 5e3, n)), name="sharesbas")
    assets = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0004, 0.006, n))), name="assets")
    debt = pd.Series(1e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.008, n))), name="debt")
    equity = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0005, 0.007, n))), name="equity")
    workingcapital = pd.Series(8e6 * np.exp(np.cumsum(np.random.normal(0.0004, 0.01, n))) * np.sign(np.random.normal(0.7, 1.0, n)), name="workingcapital")
    currentratio = pd.Series(1.5 + np.cumsum(np.random.normal(0.0, 0.01, n)) * 0.1, name="currentratio")
    retearn = pd.Series(1e7 * np.exp(np.cumsum(np.random.normal(0.0004, 0.009, n))) * np.sign(np.random.normal(0.7, 1.0, n)), name="retearn")
    liabilities = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.007, n))), name="liabilities")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "netinc": netinc, "opinc": opinc, "gp": gp, "ebitda": ebitda,
        "eps": eps, "fcf": fcf, "ncfo": ncfo, "ncfi": ncfi, "ncff": ncff, "capex": capex,
        "intexp": intexp, "taxexp": taxexp, "sharesbas": sharesbas,
        "assets": assets, "debt": debt, "equity": equity,
        "workingcapital": workingcapital, "currentratio": currentratio,
        "retearn": retearn, "liabilities": liabilities,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f37_hypergrowth_growth_strength", "_f37_hypergrowth_margin_expansion", "_f37_hypergrowth_fcf_positivity", "_f37_hypergrowth_signature")
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
    print(f"OK f37_hypergrowth_signature_base_076_150_claude: {n_features} features pass")
