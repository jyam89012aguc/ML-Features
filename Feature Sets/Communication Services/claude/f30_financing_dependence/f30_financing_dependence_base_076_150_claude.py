import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).std()


def _sum(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).sum()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rank(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).rank(pct=True) - 0.5


# ===== folder domain primitives (financing dependence) =====
def _f30_ext_reliance(ncff, ncfo, w):
    f = _mean(ncff, w)
    o = _mean(ncfo, w)
    return f / (f.abs() + o.abs()).replace(0, np.nan)


def _f30_burn_cover(ncff, ncfo, w):
    burn = (-ncfo).clip(lower=0)
    inflow = ncff.clip(lower=0)
    return _mean(inflow, w) / _mean(burn, w).replace(0, np.nan)


def _f30_self_fund_gap(ncfo, ncfi, w):
    fcf_pre = _mean(ncfo + ncfi, w)
    scale = (_mean(ncfo.abs(), w) + _mean(ncfi.abs(), w)).replace(0, np.nan)
    return fcf_pre / scale


def _f30_equity_debt_mix(ncfcommon, ncfdebt, w):
    e = _mean(ncfcommon, w)
    d = _mean(ncfdebt, w)
    return (e - d) / (e.abs() + d.abs()).replace(0, np.nan)


def _f30_rollcorr(a, b, w):
    am = a - _mean(a, w)
    bm = b - _mean(b, w)
    cov = _mean(am * bm, w)
    denom = (_std(a, w) * _std(b, w)).replace(0, np.nan)
    return cov / denom


# ============================================================
# external-financing reliance over 504d (two-year structural dependence)
def f30fd_f30_financing_dependence_extrel_504d_base_v076_signal(ncff, ncfo):
    b = _f30_ext_reliance(ncff, ncfo, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# external reliance long-vs-short spread (504d minus 126d): structural drift
def f30fd_f30_financing_dependence_relspread_504v126_base_v077_signal(ncff, ncfo):
    long = _f30_ext_reliance(ncff, ncfo, 504)
    short = _f30_ext_reliance(ncff, ncfo, 126)
    b = long - short
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing burn-cover over 504d (long-horizon funded-burn coverage)
def f30fd_f30_financing_dependence_burncov_504d_base_v078_signal(ncff, ncfo):
    b = _f30_burn_cover(ncff, ncfo, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding gap over 504d (two-year free-cash-before-financing)
def f30fd_f30_financing_dependence_selffund_504d_base_v079_signal(ncfo, ncfi):
    b = _f30_self_fund_gap(ncfo, ncfi, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-vs-debt mix over 504d (structural funding-source tilt)
def f30fd_f30_financing_dependence_eqdebtmix_504d_base_v080_signal(ncfcommon, ncfdebt):
    b = _f30_equity_debt_mix(ncfcommon, ncfdebt, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing-operating countercyclicality over 252d (financing offsets operating)
def f30fd_f30_financing_dependence_finopcorr_252d_base_v081_signal(ncff, ncfo):
    b = _f30_rollcorr(ncff, ncfo, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-debt substitution: 252d correlation between equity and debt flows
# (negative = one lever substitutes for the other)
def f30fd_f30_financing_dependence_eqdebtcorr_252d_base_v082_signal(ncfcommon, ncfdebt):
    b = _f30_rollcorr(ncfcommon, ncfdebt, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing-investing co-movement over 252d (raise-to-spend coupling)
def f30fd_f30_financing_dependence_fininvcorr_252d_base_v083_signal(ncff, ncfi):
    b = -_f30_rollcorr(ncff, ncfi, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-investing coupling over 252d (self-funded investment regime)
def f30fd_f30_financing_dependence_opinvcorr_252d_base_v084_signal(ncfo, ncfi):
    b = _f30_rollcorr(ncfo, ncfi, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing dependence z vs 504d history (de-trended long structural reliance)
def f30fd_f30_financing_dependence_extrelz_504d_base_v085_signal(ncff, ncfo):
    r = _f30_ext_reliance(ncff, ncfo, 126)
    b = _z(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share of external funding from EQUITY vs total raises over 504d
def f30fd_f30_financing_dependence_eqshare_504d_base_v086_signal(ncfcommon, ncfdebt):
    e = _mean(ncfcommon.clip(lower=0), 504)
    tot = (e + _mean(ncfdebt.clip(lower=0), 504)).replace(0, np.nan)
    b = e / tot - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share of external funding from DEBT vs total raises over 252d
def f30fd_f30_financing_dependence_debtshare_252d_base_v087_signal(ncfdebt, ncfcommon):
    d = _mean(ncfdebt.clip(lower=0), 252)
    tot = (d + _mean(ncfcommon.clip(lower=0), 252)).replace(0, np.nan)
    b = d / tot - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-raise dependence vs investing need: raises over investing outflow, 504d
def f30fd_f30_financing_dependence_raisevinv_504d_base_v088_signal(ncfcommon, ncfdebt, ncfi):
    raises = _mean(ncfcommon.clip(lower=0) + ncfdebt.clip(lower=0), 504)
    inv = _mean((-ncfi).clip(lower=0), 504).replace(0, np.nan)
    b = np.tanh(raises / inv)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing flow level z over 252d (unusually large net financing episodes)
def f30fd_f30_financing_dependence_finz_252d_base_v089_signal(ncff):
    b = _z(_mean(ncff, 21), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding gap volatility: instability of pre-financing free cash, 252d
def f30fd_f30_financing_dependence_gapvol_252d_base_v090_signal(ncfo, ncfi):
    g = _f30_self_fund_gap(ncfo, ncfi, 21)
    b = _std(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# raise-to-burn timing: raises concentrated in the same window as operating burn, 252d
def f30fd_f30_financing_dependence_raiseburnsync_252d_base_v091_signal(ncff, ncfo):
    raise_ = ncff.clip(lower=0)
    burn = (-ncfo).clip(lower=0)
    b = _f30_rollcorr(raise_, burn, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last two years free-cash-before-financing was negative (chronic gap)
def f30fd_f30_financing_dependence_gapstreak_504d_base_v092_signal(ncfo, ncfi):
    gap = (ncfo + ncfi < 0).astype(float)
    b = gap.rolling(504, min_periods=252).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net external dependence over 504d: financing vs free cash before financing
def f30fd_f30_financing_dependence_netextdep_504d_base_v093_signal(ncff, ncfo, ncfi):
    fcf_pre = _mean(ncfo + ncfi, 504)
    fin = _mean(ncff, 504)
    b = (fin - fcf_pre) / (fin.abs() + fcf_pre.abs()).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity issuance acceleration: 63d change in equity inflow normalized, 252d
def f30fd_f30_financing_dependence_eqaccel_base_v094_signal(ncfcommon):
    m = _mean(ncfcommon.clip(lower=0), 63)
    sc = _mean(ncfcommon.abs(), 252).replace(0, np.nan)
    b = (m - m.shift(63)) / sc
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt draw acceleration: 63d change in debt inflow normalized, 252d
def f30fd_f30_financing_dependence_debtaccel_base_v095_signal(ncfdebt):
    m = _mean(ncfdebt.clip(lower=0), 63)
    sc = _mean(ncfdebt.abs(), 252).replace(0, np.nan)
    b = (m - m.shift(63)) / sc
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing reliance percentile vs 504d history (long-horizon regime rank)
def f30fd_f30_financing_dependence_relrank_504d_base_v096_signal(ncff, ncfo):
    r = _f30_ext_reliance(ncff, ncfo, 63)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-debt mix percentile vs 504d history
def f30fd_f30_financing_dependence_mixrank_504d_base_v097_signal(ncfcommon, ncfdebt):
    m = _f30_equity_debt_mix(ncfcommon, ncfdebt, 63)
    b = _rank(m, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# external-funding fraction (inflows): financing inflow / total inflows, 504d
def f30fd_f30_financing_dependence_extfrac_504d_base_v098_signal(ncff, ncfo):
    fin = _mean(ncff.clip(lower=0), 504)
    op = _mean(ncfo.clip(lower=0), 504)
    b = fin / (fin + op).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# three-way cash mix entropy over 504d: how evenly cash activity is spread across
# operating / investing / financing (low = one channel dominates the cash story)
def f30fd_f30_financing_dependence_opsuff_504d_base_v099_signal(ncfo, ncfi, ncff):
    a = _mean(ncfo.abs(), 504)
    b_ = _mean(ncfi.abs(), 504)
    c = _mean(ncff.abs(), 504)
    tot = (a + b_ + c).replace(0, np.nan)
    pa = (a / tot).clip(lower=1e-9)
    pb = (b_ / tot).clip(lower=1e-9)
    pc = (c / tot).clip(lower=1e-9)
    ent = -(pa * np.log(pa) + pb * np.log(pb) + pc * np.log(pc))
    b = ent
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn-cover regime distance: 63d burn-cover minus its 252d median
def f30fd_f30_financing_dependence_burncovdist_252d_base_v100_signal(ncff, ncfo):
    c = _f30_burn_cover(ncff, ncfo, 63)
    med = c.rolling(252, min_periods=126).median()
    b = c - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity raise concentration over 504d: peak vs average monthly equity inflow
def f30fd_f30_financing_dependence_eqconc_504d_base_v101_signal(ncfcommon):
    monthly = _mean(ncfcommon.clip(lower=0), 21)
    peak = monthly.rolling(504, min_periods=252).max()
    avg = monthly.rolling(504, min_periods=252).mean().replace(0, np.nan)
    b = peak / avg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt draw concentration over 504d
def f30fd_f30_financing_dependence_debtconc_504d_base_v102_signal(ncfdebt):
    monthly = _mean(ncfdebt.clip(lower=0), 21)
    peak = monthly.rolling(504, min_periods=252).max()
    avg = monthly.rolling(504, min_periods=252).mean().replace(0, np.nan)
    b = peak / avg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing dependence momentum: 252d reliance change over a half-year
def f30fd_f30_financing_dependence_relmom_126d_base_v103_signal(ncff, ncfo):
    r = _f30_ext_reliance(ncff, ncfo, 252)
    b = r - r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total raises vs operating over 504d (long-horizon raise dependence)
def f30fd_f30_financing_dependence_totraise_504d_base_v104_signal(ncfcommon, ncfdebt, ncfo):
    raises = _mean(ncfcommon.clip(lower=0) + ncfdebt.clip(lower=0), 504)
    eng = (raises.abs() + _mean(ncfo.abs(), 504)).replace(0, np.nan)
    b = raises / eng
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding strength over 504d: operating covering investing+financing outflow days
def f30fd_f30_financing_dependence_selfstr_504d_base_v105_signal(ncfo, ncff, ncfi):
    outflow = (-ncfi).clip(lower=0) + (-ncff).clip(lower=0)
    covered = (ncfo.clip(lower=0) >= outflow).astype(float)
    b = covered.rolling(504, min_periods=252).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing inflow skewness over 252d (a few large raises vs steady drip)
def f30fd_f30_financing_dependence_finskew_252d_base_v106_signal(ncff):
    sc = _std(ncff, 252).replace(0, np.nan)
    centered = ncff - _mean(ncff, 252)
    b = _mean((centered / sc) ** 3, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-flow kurtosis-style tail: heavy debt-flow episodes over 252d
def f30fd_f30_financing_dependence_debttail_252d_base_v107_signal(ncfdebt):
    sc = _std(ncfdebt, 252).replace(0, np.nan)
    centered = ncfdebt - _mean(ncfdebt, 252)
    b = _mean((centered / sc) ** 4, 252) - 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing reliance dispersion over 504d (variability of monthly reliance)
def f30fd_f30_financing_dependence_reldisp_504d_base_v108_signal(ncff, ncfo):
    r = _f30_ext_reliance(ncff, ncfo, 21)
    b = _std(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-vs-debt mix smoothed (persistent funding-source regime)
def f30fd_f30_financing_dependence_mixema_252d_base_v109_signal(ncfcommon, ncfdebt):
    m = _f30_equity_debt_mix(ncfcommon, ncfdebt, 63)
    b = m.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# mix displacement: short mix minus its own slow EMA (lever-rotation impulse)
def f30fd_f30_financing_dependence_mixdisp2_base_v110_signal(ncfcommon, ncfdebt):
    m = _f30_equity_debt_mix(ncfcommon, ncfdebt, 63)
    b = m - m.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative net raises over 504d normalized by turnover (structural issuance)
def f30fd_f30_financing_dependence_cumraise_504d_base_v111_signal(ncfcommon, ncfdebt, ncff):
    net = _sum(ncfcommon.clip(lower=0) + ncfdebt.clip(lower=0), 504)
    turn = _sum(ncff.abs(), 504).replace(0, np.nan)
    b = net / turn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-vs-financing inflow gap z-scored over 504d: how unusual the current
# self-source-vs-external-source balance is relative to its own two-year history
def f30fd_f30_financing_dependence_opinflowsh_504d_base_v112_signal(ncfo, ncff):
    gap = _mean(ncfo.clip(lower=0), 63) - _mean(ncff.clip(lower=0), 63)
    sc = _mean(ncfo.abs() + ncff.abs(), 504).replace(0, np.nan)
    b = _z(gap / sc, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing-funded investing over 504d: financing inflow vs investing outflow
def f30fd_f30_financing_dependence_invfund_504d_base_v113_signal(ncff, ncfi):
    invest = _mean((-ncfi).clip(lower=0), 504)
    fin = _mean(ncff.clip(lower=0), 504).replace(0, np.nan)
    b = np.tanh(invest / fin)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-issuance sign x magnitude over 504d (long-horizon capital posture)
def f30fd_f30_financing_dependence_issuesignmag_504d_base_v114_signal(ncfcommon, ncfdebt):
    net = _mean(ncfcommon + ncfdebt, 504)
    sc = (_mean(ncfcommon.abs(), 504) + _mean(ncfdebt.abs(), 504)).replace(0, np.nan)
    r = net / sc
    b = np.sign(r) * (r.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-return tilt over 252d: net returns (buybacks+repay) vs operating
def f30fd_f30_financing_dependence_returntilt_252d_base_v115_signal(ncfcommon, ncfdebt, ncfo):
    returns = _mean((-ncfcommon).clip(lower=0) + (-ncfdebt).clip(lower=0), 252)
    op = _mean(ncfo.abs(), 252).replace(0, np.nan)
    b = returns / op
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing-flow YoY change over 252d (structural shift in dependence direction)
def f30fd_f30_financing_dependence_finyoy_252d_base_v116_signal(ncff, ncfo):
    r = _safe_div(_mean(ncff, 252), _mean(ncfo.abs(), 252))
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-funded-burn over 504d: equity inflow over operating burn
def f30fd_f30_financing_dependence_eqburn_504d_base_v117_signal(ncfcommon, ncfo):
    eq = _mean(ncfcommon.clip(lower=0), 504)
    burn = _mean((-ncfo).clip(lower=0), 504).replace(0, np.nan)
    b = np.tanh(eq / burn)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-funded-burn momentum over 504d: change in debt-draw-over-burn coverage
# (is the company leaning MORE on debt to cover operating losses over time?)
def f30fd_f30_financing_dependence_debtburn_504d_base_v118_signal(ncfdebt, ncfo):
    dr = _mean(ncfdebt.clip(lower=0), 126)
    burn = _mean((-ncfo).clip(lower=0), 126).replace(0, np.nan)
    cov = np.tanh(dr / burn)
    b = cov - cov.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# external-dependence interaction: reliance x chronic-gap streak (entrenched need)
def f30fd_f30_financing_dependence_entrenched_252d_base_v119_signal(ncff, ncfo, ncfi):
    rel = _f30_ext_reliance(ncff, ncfo, 252).clip(lower=0)
    gap = (ncfo + ncfi < 0).astype(float).rolling(252, min_periods=126).mean()
    b = rel * gap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing-vs-investing net balance over 504d (draw vs deploy)
def f30fd_f30_financing_dependence_fininvnet_504d_base_v120_signal(ncff, ncfi):
    net = _mean(ncff + ncfi, 504)
    sc = (_mean(ncff.abs(), 504) + _mean(ncfi.abs(), 504)).replace(0, np.nan)
    b = net / sc
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# raise frequency over 504d: count of months with equity OR debt inflow
def f30fd_f30_financing_dependence_raisefreq_504d_base_v121_signal(ncfcommon, ncfdebt):
    raised = ((ncfcommon > 0) | (ncfdebt > 0)).astype(float)
    b = raised.rolling(504, min_periods=252).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing inflow vs combined deficit over 504d (long funded-burn coverage)
def f30fd_f30_financing_dependence_totburncov_504d_base_v122_signal(ncff, ncfo, ncfi):
    deficit = (-(ncfo + ncfi)).clip(lower=0)
    fin = _mean(ncff.clip(lower=0), 504)
    b = np.tanh(fin / _mean(deficit, 504).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing volatility over 504d scaled by operating scale (lumpy capital access)
def f30fd_f30_financing_dependence_finvol_504d_base_v123_signal(ncff, ncfo):
    v = _std(ncff, 63)
    sc = _mean(ncfo.abs(), 504).replace(0, np.nan)
    b = _mean(v, 504) / sc
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-vs-operating countercyclicality over 504d (defensive leverage, long horizon)
def f30fd_f30_financing_dependence_debtopcorr_504d_base_v124_signal(ncfo, ncfdebt):
    b = _f30_rollcorr(ncfo, ncfdebt, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-vs-operating coupling over 252d (dilution timed to operating weakness)
def f30fd_f30_financing_dependence_eqopcorr_252d_base_v125_signal(ncfo, ncfcommon):
    b = _f30_rollcorr(ncfo, ncfcommon, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing reliance smoothed over 504d (slow structural dependence trend)
def f30fd_f30_financing_dependence_relema_504d_base_v126_signal(ncff, ncfo):
    r = _f30_ext_reliance(ncff, ncfo, 126)
    b = r.ewm(span=252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding gap regime distance over 504d (deep chronic deficit flag)
def f30fd_f30_financing_dependence_gapdist_504d_base_v127_signal(ncfo, ncfi):
    g = _f30_self_fund_gap(ncfo, ncfi, 63)
    med = g.rolling(504, min_periods=252).median()
    b = g - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year financing alone exceeded operating inflow (financing-led cash)
def f30fd_f30_financing_dependence_finled_252d_base_v128_signal(ncff, ncfo):
    led = (ncff.clip(lower=0) > ncfo.clip(lower=0)).astype(float)
    b = led.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-issuance vs buyback net balance over 252d (dilution vs return)
def f30fd_f30_financing_dependence_eqnetbal_252d_base_v129_signal(ncfcommon):
    iss = _mean(ncfcommon.clip(lower=0), 252)
    bb = _mean((-ncfcommon).clip(lower=0), 252)
    b = (iss - bb) / (iss + bb).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt net-flow momentum: 63d change in net debt balance normalized (levering up
# vs paying down trend), over its own 252d turnover scale
def f30fd_f30_financing_dependence_debtnetbal_252d_base_v130_signal(ncfdebt):
    net = _mean(ncfdebt, 63)
    sc = _mean(ncfdebt.abs(), 252).replace(0, np.nan)
    b = (net - net.shift(63)) / sc
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing-flow trend slope over 252d via 63d minus 252d mean (rising dependence)
def f30fd_f30_financing_dependence_fintrend_base_v131_signal(ncff, ncfo):
    short = _safe_div(_mean(ncff, 63), _mean(ncfo.abs(), 63))
    long = _safe_div(_mean(ncff, 252), _mean(ncfo.abs(), 252))
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-debt mix change over a year (structural rotation between levers)
def f30fd_f30_financing_dependence_mixyoy_base_v132_signal(ncfcommon, ncfdebt):
    m = _f30_equity_debt_mix(ncfcommon, ncfdebt, 126)
    b = m - m.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-raise dependence interaction with self-funding gap over 504d
def f30fd_f30_financing_dependence_raisegap_504d_base_v133_signal(ncff, ncfo, ncfi):
    raise_ = _safe_div(_mean(ncff.clip(lower=0), 504), _mean(ncff.abs(), 504))
    gap = (-(ncfo + ncfi)).clip(lower=0)
    gnorm = _safe_div(_mean(gap, 504), _mean((ncfo + ncfi).abs(), 504))
    b = raise_ * gnorm
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# investing self-funding ratio over 252d: operating covering investing outflow
def f30fd_f30_financing_dependence_invselffund_252d_base_v134_signal(ncfo, ncfi):
    o = _mean(ncfo.clip(lower=0), 252)
    inv = _mean((-ncfi).clip(lower=0), 252).replace(0, np.nan)
    b = np.tanh(o / inv) - 0.3
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing inflow persistence: lag-21 autocorrelation of financing flow, 252d
def f30fd_f30_financing_dependence_finpersist_252d_base_v135_signal(ncff):
    x = ncff - _mean(ncff, 252)
    xl = x.shift(21)
    cov = _mean(x * xl, 252)
    denom = _std(ncff, 252).replace(0, np.nan) ** 2
    b = cov / denom
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-flow persistence: lag-21 autocorrelation of operating cash, 252d
def f30fd_f30_financing_dependence_oppersist_252d_base_v136_signal(ncfo):
    x = ncfo - _mean(ncfo, 252)
    xl = x.shift(21)
    cov = _mean(x * xl, 252)
    denom = _std(ncfo, 252).replace(0, np.nan) ** 2
    b = cov / denom
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-program reversal: fraction of last two years debt SWITCHED between net draw
# and net repayment quarter-over-quarter (unstable leverage management)
def f30fd_f30_financing_dependence_repaycov_504d_base_v137_signal(ncfdebt, ncfo):
    q = _mean(ncfdebt, 63)
    flip = (np.sign(q) != np.sign(q.shift(63))).astype(float)
    rate = flip.rolling(504, min_periods=252).mean()
    mag = _safe_div(_std(ncfdebt, 252), _mean(ncfo.abs(), 252))
    b = rate * np.tanh(mag) - 0.2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback vs operating coverage over 504d: operating-funded shareholder return
def f30fd_f30_financing_dependence_bbcov_504d_base_v138_signal(ncfcommon, ncfo):
    bb = _mean((-ncfcommon).clip(lower=0), 504)
    o = _mean(ncfo.clip(lower=0), 504).replace(0, np.nan)
    b = np.tanh(bb / o)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing inflow vs investing+operating combined need ranked vs 504d history
def f30fd_f30_financing_dependence_extdeprank_504d_base_v139_signal(ncff, ncfo, ncfi):
    need = (_mean((-ncfo).clip(lower=0), 63) + _mean((-ncfi).clip(lower=0), 63)).replace(0, np.nan)
    inflow = _mean(ncff.clip(lower=0), 63)
    r = inflow / need
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net financing minus net pre-financing cash, ranked vs 504d (dependence percentile)
def f30fd_f30_financing_dependence_netdeprank_504d_base_v140_signal(ncff, ncfo, ncfi):
    fin = _mean(ncff, 63)
    pre = _mean(ncfo + ncfi, 63)
    r = (fin - pre) / (fin.abs() + pre.abs()).replace(0, np.nan)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-issuance share of total financing inflow over 252d (dilution channel)
def f30fd_f30_financing_dependence_eqchannel_252d_base_v141_signal(ncfcommon, ncff):
    eq = _mean(ncfcommon.clip(lower=0), 252)
    fin = _mean(ncff.clip(lower=0), 252).replace(0, np.nan)
    b = (eq / fin).clip(upper=3.0) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-draw share of total financing inflow over 252d (leverage channel)
def f30fd_f30_financing_dependence_debtchannel_252d_base_v142_signal(ncfdebt, ncff):
    dr = _mean(ncfdebt.clip(lower=0), 252)
    fin = _mean(ncff.clip(lower=0), 252).replace(0, np.nan)
    b = (dr / fin).clip(upper=3.0) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing-flow volatility regime change: 63d fin-vol now vs a year ago
def f30fd_f30_financing_dependence_finvolchg_base_v143_signal(ncff, ncfo):
    v = _safe_div(_std(ncff, 63), _mean(ncfo.abs(), 252))
    b = v - v.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding crossover over 504d: reliance minus operating self-sufficiency
def f30fd_f30_financing_dependence_crossover_504d_base_v144_signal(ncff, ncfo, ncfi):
    rel = _f30_ext_reliance(ncff, ncfo, 504)
    o = _mean(ncfo, 504)
    tot = (_mean(ncfo.abs(), 504) + _mean(ncfi.abs(), 504)).replace(0, np.nan)
    suff = o / tot
    b = rel - suff
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# raise co-occurrence over 504d: months both levers tapped, magnitude-weighted
def f30fd_f30_financing_dependence_bothraise_504d_base_v145_signal(ncfcommon, ncfdebt):
    both = ((ncfcommon > 0) & (ncfdebt > 0)).astype(float)
    rate = both.rolling(504, min_periods=252).mean()
    mag = _mean(ncfcommon.clip(lower=0) + ncfdebt.clip(lower=0), 126)
    sc = _mean(ncfcommon.abs() + ncfdebt.abs(), 504).replace(0, np.nan)
    b = rate * (mag / sc)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing-engine balance z: net raises-minus-returns over 504d, z-scored vs its
# own history (unusual swings between capital intake and capital return)
def f30fd_f30_financing_dependence_balance_504d_base_v146_signal(ncfcommon, ncfdebt, ncfo):
    net = _mean(ncfcommon + ncfdebt, 126)
    op = _mean(ncfo.abs(), 252).replace(0, np.nan)
    b = _z(net / op, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing dependence curvature: second difference of 126d reliance (acceleration
# of the dependence trend, not just its slope)
def f30fd_f30_financing_dependence_relaccel_base_v147_signal(ncff, ncfo):
    r = _f30_ext_reliance(ncff, ncfo, 126)
    b = r - 2.0 * r.shift(63) + r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# investing-funded-by-financing streak over 504d (chronic raise-to-spend)
def f30fd_f30_financing_dependence_finivstreak_504d_base_v148_signal(ncff, ncfi):
    co = ((ncff > 0) & (ncfi < 0)).astype(float)
    b = co.rolling(504, min_periods=252).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net external draw plug-rate over 504d (financing covering operating holes, long)
def f30fd_f30_financing_dependence_plugrate_504d_base_v149_signal(ncff, ncfo):
    plug = ((ncff > 0) & (ncfo < 0)).astype(float)
    rate = plug.rolling(504, min_periods=252).mean()
    depth = _safe_div(_sum(ncff.clip(lower=0), 504), _sum((-ncfo).clip(lower=0), 504))
    b = rate * np.tanh(depth)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# all-source dependence composite over 252d: blends external reliance, equity-debt
# diversification of sources, and net raise posture (multi-facet funding-stress score)
def f30fd_f30_financing_dependence_composite_252d_base_v150_signal(ncff, ncfo, ncfi, ncfcommon, ncfdebt):
    rel = _f30_ext_reliance(ncff, ncfo, 252)
    e = _mean(ncfcommon.clip(lower=0), 252)
    d = _mean(ncfdebt.clip(lower=0), 252)
    diversify = 1.0 - (e - d).abs() / (e + d).replace(0, np.nan)
    invneed = _safe_div(_mean((-ncfi).clip(lower=0), 252), _mean(ncff.abs(), 252))
    b = np.tanh(rel) + 0.5 * diversify - 0.5 * np.tanh(invneed)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f30fd_f30_financing_dependence_extrel_504d_base_v076_signal,
    f30fd_f30_financing_dependence_relspread_504v126_base_v077_signal,
    f30fd_f30_financing_dependence_burncov_504d_base_v078_signal,
    f30fd_f30_financing_dependence_selffund_504d_base_v079_signal,
    f30fd_f30_financing_dependence_eqdebtmix_504d_base_v080_signal,
    f30fd_f30_financing_dependence_finopcorr_252d_base_v081_signal,
    f30fd_f30_financing_dependence_eqdebtcorr_252d_base_v082_signal,
    f30fd_f30_financing_dependence_fininvcorr_252d_base_v083_signal,
    f30fd_f30_financing_dependence_opinvcorr_252d_base_v084_signal,
    f30fd_f30_financing_dependence_extrelz_504d_base_v085_signal,
    f30fd_f30_financing_dependence_eqshare_504d_base_v086_signal,
    f30fd_f30_financing_dependence_debtshare_252d_base_v087_signal,
    f30fd_f30_financing_dependence_raisevinv_504d_base_v088_signal,
    f30fd_f30_financing_dependence_finz_252d_base_v089_signal,
    f30fd_f30_financing_dependence_gapvol_252d_base_v090_signal,
    f30fd_f30_financing_dependence_raiseburnsync_252d_base_v091_signal,
    f30fd_f30_financing_dependence_gapstreak_504d_base_v092_signal,
    f30fd_f30_financing_dependence_netextdep_504d_base_v093_signal,
    f30fd_f30_financing_dependence_eqaccel_base_v094_signal,
    f30fd_f30_financing_dependence_debtaccel_base_v095_signal,
    f30fd_f30_financing_dependence_relrank_504d_base_v096_signal,
    f30fd_f30_financing_dependence_mixrank_504d_base_v097_signal,
    f30fd_f30_financing_dependence_extfrac_504d_base_v098_signal,
    f30fd_f30_financing_dependence_opsuff_504d_base_v099_signal,
    f30fd_f30_financing_dependence_burncovdist_252d_base_v100_signal,
    f30fd_f30_financing_dependence_eqconc_504d_base_v101_signal,
    f30fd_f30_financing_dependence_debtconc_504d_base_v102_signal,
    f30fd_f30_financing_dependence_relmom_126d_base_v103_signal,
    f30fd_f30_financing_dependence_totraise_504d_base_v104_signal,
    f30fd_f30_financing_dependence_selfstr_504d_base_v105_signal,
    f30fd_f30_financing_dependence_finskew_252d_base_v106_signal,
    f30fd_f30_financing_dependence_debttail_252d_base_v107_signal,
    f30fd_f30_financing_dependence_reldisp_504d_base_v108_signal,
    f30fd_f30_financing_dependence_mixema_252d_base_v109_signal,
    f30fd_f30_financing_dependence_mixdisp2_base_v110_signal,
    f30fd_f30_financing_dependence_cumraise_504d_base_v111_signal,
    f30fd_f30_financing_dependence_opinflowsh_504d_base_v112_signal,
    f30fd_f30_financing_dependence_invfund_504d_base_v113_signal,
    f30fd_f30_financing_dependence_issuesignmag_504d_base_v114_signal,
    f30fd_f30_financing_dependence_returntilt_252d_base_v115_signal,
    f30fd_f30_financing_dependence_finyoy_252d_base_v116_signal,
    f30fd_f30_financing_dependence_eqburn_504d_base_v117_signal,
    f30fd_f30_financing_dependence_debtburn_504d_base_v118_signal,
    f30fd_f30_financing_dependence_entrenched_252d_base_v119_signal,
    f30fd_f30_financing_dependence_fininvnet_504d_base_v120_signal,
    f30fd_f30_financing_dependence_raisefreq_504d_base_v121_signal,
    f30fd_f30_financing_dependence_totburncov_504d_base_v122_signal,
    f30fd_f30_financing_dependence_finvol_504d_base_v123_signal,
    f30fd_f30_financing_dependence_debtopcorr_504d_base_v124_signal,
    f30fd_f30_financing_dependence_eqopcorr_252d_base_v125_signal,
    f30fd_f30_financing_dependence_relema_504d_base_v126_signal,
    f30fd_f30_financing_dependence_gapdist_504d_base_v127_signal,
    f30fd_f30_financing_dependence_finled_252d_base_v128_signal,
    f30fd_f30_financing_dependence_eqnetbal_252d_base_v129_signal,
    f30fd_f30_financing_dependence_debtnetbal_252d_base_v130_signal,
    f30fd_f30_financing_dependence_fintrend_base_v131_signal,
    f30fd_f30_financing_dependence_mixyoy_base_v132_signal,
    f30fd_f30_financing_dependence_raisegap_504d_base_v133_signal,
    f30fd_f30_financing_dependence_invselffund_252d_base_v134_signal,
    f30fd_f30_financing_dependence_finpersist_252d_base_v135_signal,
    f30fd_f30_financing_dependence_oppersist_252d_base_v136_signal,
    f30fd_f30_financing_dependence_repaycov_504d_base_v137_signal,
    f30fd_f30_financing_dependence_bbcov_504d_base_v138_signal,
    f30fd_f30_financing_dependence_extdeprank_504d_base_v139_signal,
    f30fd_f30_financing_dependence_netdeprank_504d_base_v140_signal,
    f30fd_f30_financing_dependence_eqchannel_252d_base_v141_signal,
    f30fd_f30_financing_dependence_debtchannel_252d_base_v142_signal,
    f30fd_f30_financing_dependence_finvolchg_base_v143_signal,
    f30fd_f30_financing_dependence_crossover_504d_base_v144_signal,
    f30fd_f30_financing_dependence_bothraise_504d_base_v145_signal,
    f30fd_f30_financing_dependence_balance_504d_base_v146_signal,
    f30fd_f30_financing_dependence_relaccel_base_v147_signal,
    f30fd_f30_financing_dependence_finivstreak_504d_base_v148_signal,
    f30fd_f30_financing_dependence_plugrate_504d_base_v149_signal,
    f30fd_f30_financing_dependence_composite_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F30_FINANCING_DEPENDENCE_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    ALLOW = {
        "open", "high", "low", "close", "closeadj", "volume",
        "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc", "opex",
        "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc",
        "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff",
        "ncfi", "ncfcommon", "ncfdebt", "ncfbus", "capex", "depamor", "sharesbas",
        "shareswa", "shareswadil", "assets", "assetsc", "tangibles", "intangibles",
        "ppnenet", "investments", "inventory", "receivables", "payables", "equity",
        "retearn", "workingcapital", "debt", "debtc", "debtnc", "liabilities",
        "liabilitiesc", "cashneq", "currentratio", "roic", "roe", "roa", "ros",
        "assetturnover", "invcap", "intexp", "taxexp", "ebt", "sps", "bvps", "de",
        "ncfdiv", "dps", "divyield", "payoutratio", "prefdivis",
        "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
        "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal",
        "fndholders", "undholders", "prfholders", "dbtholders", "putholders",
        "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue", "dbtvalue",
    }

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    # Signed cash flows built via _fund (ALL of ncff/ncfcommon/ncfdebt/ncfo/ncfi,
    # allow_neg=True), made to GENUINELY swing sign: each _fund level is centered by
    # its own rolling mean (net issuance vs repayment) plus a funding-cycle sinusoid.
    def _signed(seed, base, phase, amp, period):
        raw = _fund(seed, base=base, drift=0.0, vol=0.08, allow_neg=True)
        centered = raw - raw.rolling(252, min_periods=1).mean()
        gn = np.random.default_rng(seed + 9000)
        cyc = amp * base * 0.4 * np.sin(np.arange(n) / period * 2 * np.pi + phase)
        jitter = gn.normal(0.0, base * 0.10, n)
        return (centered + pd.Series(cyc) + pd.Series(jitter))

    ncfo = _signed(101, 8e7, 0.0, 1.0, 71.0).rename("ncfo")
    ncff = _signed(102, 9e7, 1.0, 1.1, 53.0).rename("ncff")
    ncfi = _signed(103, 6e7, 2.0, 0.9, 89.0).rename("ncfi")
    ncfcommon = _signed(104, 7e7, 3.0, 1.0, 47.0).rename("ncfcommon")
    ncfdebt = _signed(105, 5e7, 4.0, 1.2, 101.0).rename("ncfdebt")

    cols = {"ncfo": ncfo, "ncff": ncff, "ncfi": ncfi,
            "ncfcommon": ncfcommon, "ncfdebt": ncfdebt}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "BADCOL %s: %s" % (name, meta["inputs"])
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 20, "%s nunique=%d" % (name, q.nunique())
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        results[name] = y1.iloc[504:]
        n_features += 1

    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), "nan_ok=%d/%d" % (nan_ok, n_features)

    items = list(results.items())
    for i in range(len(items)):
        ni, si = items[i]
        ai = si.dropna()
        for j in range(i + 1, len(items)):
            nj, sj = items[j]
            aj = sj.dropna()
            idx = ai.index.intersection(aj.index)
            if len(idx) < 30:
                continue
            c = ai.loc[idx].corr(aj.loc[idx])
            if c is None or np.isnan(c):
                continue
            assert abs(c) <= 0.97, "CORR %s vs %s = %.4f" % (ni, nj, c)

    print("OK f30_financing_dependence_base_076_150_claude: %d features pass" % n_features)
