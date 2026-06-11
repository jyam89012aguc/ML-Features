import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_FIVEYEAR = 1260
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
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


def _rsum(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 3)).rank(pct=True) - 0.5


# ===== folder domain primitives (financing dependence) =====
def _f20_burn(ncfo):
    return (-ncfo).clip(lower=0)


def _f20_raise(ncff):
    return ncff.clip(lower=0)


def _f20_fin_cover(ncff, ncfo, w):
    burn = _rsum(_f20_burn(ncfo), w)
    fin = _rsum(_f20_raise(ncff), w)
    return fin / burn.replace(0, np.nan)


def _f20_dependence(ncff, ncfo, w):
    a = _rsum(ncff.abs(), w)
    b = _rsum(ncfo.abs(), w)
    return a / b.replace(0, np.nan)


def _f20_eqdebt_mix(ncfcommon, ncfdebt, w):
    eq = _rsum(ncfcommon.clip(lower=0), w)
    dt = _rsum(ncfdebt.clip(lower=0), w)
    return (eq - dt) / (eq + dt).replace(0, np.nan)


def _f20_selffund_gap(ncfo, ncfi, ncff, w):
    internal = _rsum(ncfo + ncfi, w)
    external = _rsum(ncff, w)
    return external / (internal.abs() + external.abs()).replace(0, np.nan)


# ============================================================
# external reliance using net (signed) financing over gross operating flow (252d)
def f20fd_f20_financing_dependence_netrelin_252d_base_v076_signal(ncff, ncfo):
    nf = _rsum(ncff, 252)
    op = _rsum(ncfo.abs(), 252)
    b = nf / op.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing inflow concentration: largest quarterly raise vs annual raises (252d)
def f20fd_f20_financing_dependence_raiseconc_252d_base_v077_signal(ncff):
    q = _f20_raise(ncff).rolling(63, min_periods=21).sum()
    biggest = q.rolling(252, min_periods=126).max()
    total = _rsum(_f20_raise(ncff), 252)
    b = biggest / total.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Herfindahl of financing source mix (equity vs debt concentration) 252d
def f20fd_f20_financing_dependence_srchhi_252d_base_v078_signal(ncfcommon, ncfdebt):
    eq = _rsum(ncfcommon.clip(lower=0), 252)
    dt = _rsum(ncfdebt.clip(lower=0), 252)
    tot = (eq + dt).replace(0, np.nan)
    b = (eq / tot) ** 2 + (dt / tot) ** 2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing cover gap z-scored over a deep cycle window (1260d standardization)
def f20fd_f20_financing_dependence_coverdeepz_252d_base_v079_signal(ncff, ncfo):
    c = _f20_fin_cover(ncff, ncfo, 252)
    b = _z(c, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# external dependence acceleration: dependence delta over a quarter (252d)
def f20fd_f20_financing_dependence_depaccel_252d_base_v080_signal(ncff, ncfo):
    d = _f20_dependence(ncff, ncfo, 252)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net debt issuance relative to operating cash generated (debt-on-ops) 252d
def f20fd_f20_financing_dependence_dtops_252d_base_v081_signal(ncfdebt, ncfo):
    nd = _rsum(ncfdebt, 252)
    op = _rsum(ncfo.abs(), 252)
    b = nd / op.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net equity issuance relative to operating cash generated (equity-on-ops) 252d
def f20fd_f20_financing_dependence_eqops_252d_base_v082_signal(ncfcommon, ncfo):
    ne = _rsum(ncfcommon, 252)
    op = _rsum(ncfo.abs(), 252)
    b = ne / op.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing-funded total spend: raises vs (burn + investing outflow) 504d
def f20fd_f20_financing_dependence_fundspend_504d_base_v083_signal(ncff, ncfo, ncfi):
    raise_ = _rsum(_f20_raise(ncff), 504)
    spend = _rsum(_f20_burn(ncfo) + (-ncfi).clip(lower=0), 504)
    b = raise_ / spend.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding gap short-vs-long spread (dependence term structure)
def f20fd_f20_financing_dependence_gapterm_base_v084_signal(ncfo, ncfi, ncff):
    s = _f20_selffund_gap(ncfo, ncfi, ncff, 126)
    l = _f20_selffund_gap(ncfo, ncfi, ncff, 504)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing reliance smoothed and ranked vs cycle (504d rank of 252d EMA dependence)
def f20fd_f20_financing_dependence_relismrank_252d_base_v085_signal(ncff, ncfo):
    d = _f20_dependence(ncff, ncfo, 126).ewm(span=63, min_periods=21).mean()
    b = d.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt repayment intensity: gross debt outflows vs operating burn (deleverage need)
def f20fd_f20_financing_dependence_dtrepay_252d_base_v086_signal(ncfdebt, ncfo):
    repay = _rsum((-ncfdebt).clip(lower=0), 252)
    burn = _rsum(_f20_burn(ncfo), 252)
    b = repay / (repay + burn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity buyback-vs-issue net direction (positive=net issue) scaled by turnover 252d
def f20fd_f20_financing_dependence_eqnetdir_252d_base_v087_signal(ncfcommon):
    ne = _rsum(ncfcommon, 252)
    gross = _rsum(ncfcommon.abs(), 252)
    b = ne / gross.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing cover surplus log-ratio (raises over burn, symmetric log) 252d
def f20fd_f20_financing_dependence_coverlog_252d_base_v088_signal(ncff, ncfo):
    fin = _rsum(_f20_raise(ncff), 252)
    burn = _rsum(_f20_burn(ncfo), 252)
    b = np.log((fin + 1.0) / (burn + 1.0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# investing intensity funded externally vs internally (capex funding split) 252d
def f20fd_f20_financing_dependence_capexfund_252d_base_v089_signal(ncff, ncfo, ncfi):
    inv = _rsum((-ncfi).clip(lower=0), 252)
    ext = _rsum(_f20_raise(ncff), 252)
    intl = _rsum(ncfo.clip(lower=0), 252)
    b = (ext - intl) / inv.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dependence-volatility: how unstable external reliance is over the cycle (252d)
def f20fd_f20_financing_dependence_depinstab_252d_base_v090_signal(ncff, ncfo):
    d = _f20_dependence(ncff, ncfo, 63)
    b = _std(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net financing flow as fraction of total cash needs (external-need coverage) 252d
def f20fd_f20_financing_dependence_extneedcov_252d_base_v091_signal(ncff, ncfo, ncfi):
    nf = _rsum(ncff, 252)
    need = _rsum(_f20_burn(ncfo) + (-ncfi).clip(lower=0), 252)
    b = nf / need.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# mix tilt vs its own long EMA (equity/debt rotation displacement) 252d
def f20fd_f20_financing_dependence_mixdisp_252d_base_v092_signal(ncfcommon, ncfdebt):
    m = _f20_eqdebt_mix(ncfcommon, ncfdebt, 252)
    b = m - m.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing self-sufficiency improving streak: quarters of rising op-cover (252d)
def f20fd_f20_financing_dependence_coverstreak_252d_base_v093_signal(ncfo, ncff):
    op = _rsum(ncfo, 63)
    ext = _rsum(_f20_raise(ncff), 63)
    selfcover = op - ext
    up = (selfcover > selfcover.shift(63)).astype(float)
    streak = up.groupby((up != up.shift()).cumsum()).cumsum() * up
    b = streak.rolling(252, min_periods=63).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# external reliance vs prior-cycle reliance (year-over-year dependence change) 252d
def f20fd_f20_financing_dependence_depyoy_252d_base_v094_signal(ncff, ncfo):
    d = _f20_dependence(ncff, ncfo, 252)
    b = d - d.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net financing per net operating (signed coverage of ops by financing) 504d
def f20fd_f20_financing_dependence_finperop_504d_base_v095_signal(ncff, ncfo):
    nf = _rsum(ncff, 504)
    op = _rsum(ncfo, 504)
    b = nf / (nf.abs() + op.abs()).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-funded investing share vs equity-funded investing share (cap structure) 252d
def f20fd_f20_financing_dependence_dtveq_inv_252d_base_v096_signal(ncfdebt, ncfcommon, ncfi):
    inv = _rsum((-ncfi).clip(lower=0), 252).replace(0, np.nan)
    dt = _rsum(ncfdebt.clip(lower=0), 252) / inv
    eq = _rsum(ncfcommon.clip(lower=0), 252) / inv
    b = (dt - eq) / (dt + eq).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing footprint change over a quarter (rising financing activity) 252d
def f20fd_f20_financing_dependence_footmom_252d_base_v097_signal(ncff, ncfo, ncfi):
    fin = _rsum(ncff.abs(), 252)
    tot = _rsum(ncff.abs() + ncfo.abs() + ncfi.abs(), 252)
    foot = fin / tot.replace(0, np.nan)
    b = foot - foot.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# external dependence sign-magnitude on net financing vs investing (growth-fund)
def f20fd_f20_financing_dependence_growsignmag_252d_base_v098_signal(ncff, ncfi):
    nf = _rsum(ncff, 252)
    inv = _rsum(ncfi.abs(), 252).replace(0, np.nan)
    r = nf / inv
    b = np.sign(r) * np.log1p(r.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding gap percentile vs deep history, smoothed (chronic-dependence) 504d
def f20fd_f20_financing_dependence_gapchron_504d_base_v099_signal(ncfo, ncfi, ncff):
    g = _f20_selffund_gap(ncfo, ncfi, ncff, 252)
    b = (g.rolling(1260, min_periods=252).rank(pct=True) - 0.5).ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing dependence interaction with mix concentration (concentrated reliance)
def f20fd_f20_financing_dependence_depxconc_252d_base_v100_signal(ncff, ncfo, ncfcommon, ncfdebt):
    d = _z(_f20_dependence(ncff, ncfo, 252), 252)
    eq = _rsum(ncfcommon.clip(lower=0), 252)
    dt = _rsum(ncfdebt.clip(lower=0), 252)
    tot = (eq + dt).replace(0, np.nan)
    hhi = (eq / tot) ** 2 + (dt / tot) ** 2
    b = d * hhi
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross financing activity per gross operating activity (financing churn) 252d
def f20fd_f20_financing_dependence_finchurn_252d_base_v101_signal(ncff, ncfo):
    gf = _rsum(ncff.abs(), 252)
    go = _rsum(ncfo.abs(), 252)
    b = np.log((gf + 1.0) / (go + 1.0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net debt minus net equity financing balance scaled by needs (leverage tilt) 252d
def f20fd_f20_financing_dependence_levtilt_252d_base_v102_signal(ncfdebt, ncfcommon, ncfo):
    nd = _rsum(ncfdebt, 252)
    ne = _rsum(ncfcommon, 252)
    need = _rsum(_f20_burn(ncfo), 252).replace(0, np.nan)
    b = (nd - ne) / need
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing-funded-burn regime persistence: fraction of 504d with raises>burn
def f20fd_f20_financing_dependence_covregime_504d_base_v103_signal(ncff, ncfo):
    fin = _rsum(_f20_raise(ncff), 63)
    burn = _rsum(_f20_burn(ncfo), 63)
    cov = (fin > burn).astype(float)
    b = cov.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dependence dispersion across 126/252/504 windows (term disagreement)
def f20fd_f20_financing_dependence_depdisp_base_v104_signal(ncff, ncfo):
    d1 = _f20_dependence(ncff, ncfo, 126)
    d2 = _f20_dependence(ncff, ncfo, 252)
    d3 = _f20_dependence(ncff, ncfo, 504)
    b = pd.concat([d1, d2, d3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-raise momentum normalized by operating scale (rising equity dependence)
def f20fd_f20_financing_dependence_eqraisemom_252d_base_v105_signal(ncfcommon, ncfo):
    eq = _rsum(ncfcommon.clip(lower=0), 126)
    scale = _rsum(ncfo.abs(), 252).replace(0, np.nan)
    r = eq / scale
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-raise momentum normalized by operating scale (rising debt dependence)
def f20fd_f20_financing_dependence_dtraisemom_252d_base_v106_signal(ncfdebt, ncfo):
    dt = _rsum(ncfdebt.clip(lower=0), 126)
    scale = _rsum(ncfo.abs(), 252).replace(0, np.nan)
    r = dt / scale
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# internal funding ratio: ops cash vs total cash inflows (self-funding share) 252d
def f20fd_f20_financing_dependence_intfundshare_252d_base_v107_signal(ncfo, ncff, ncfi):
    op_in = _rsum(ncfo.clip(lower=0), 252)
    tot_in = _rsum(ncfo.clip(lower=0) + ncff.clip(lower=0) + ncfi.clip(lower=0), 252)
    b = op_in / tot_in.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing reliance per unit investing outflow z-scored (growth-funding extremity)
def f20fd_f20_financing_dependence_growrelz_252d_base_v108_signal(ncff, ncfi):
    fin = _rsum(_f20_raise(ncff), 252)
    inv = _rsum((-ncfi).clip(lower=0), 252)
    r = fin / inv.replace(0, np.nan)
    b = _z(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net financing flow tanh of cycle-z (bounded financing-pressure regime) 252d
def f20fd_f20_financing_dependence_finpresstanh_252d_base_v109_signal(ncff):
    f = _rsum(ncff, 126)
    b = np.tanh(_z(f, 504))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# external pull vs internal generation log-balance (self-funding log gap) 252d
def f20fd_f20_financing_dependence_selfloggap_252d_base_v110_signal(ncfo, ncfi, ncff):
    internal = _rsum((ncfo + ncfi).clip(lower=0), 252)
    external = _rsum(_f20_raise(ncff), 252)
    b = np.log((external + 1.0) / (internal + 1.0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dependence rank-of-rank momentum: change in cycle percentile over a quarter 252d
def f20fd_f20_financing_dependence_deprankmom_252d_base_v111_signal(ncff, ncfo):
    d = _f20_dependence(ncff, ncfo, 252)
    pr = d.rolling(1260, min_periods=252).rank(pct=True)
    b = pr - pr.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rolling correlation of equity and debt raise flows (joint-financing regime) 252d
def f20fd_f20_financing_dependence_jointraise_252d_base_v112_signal(ncfcommon, ncfdebt):
    eq = ncfcommon.clip(lower=0).rolling(21, min_periods=10).sum()
    dt = ncfdebt.clip(lower=0).rolling(21, min_periods=10).sum()
    b = eq.rolling(252, min_periods=126).corr(dt)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn covered by net financing minus investing drain (true external cushion) 504d
def f20fd_f20_financing_dependence_extcushion_504d_base_v113_signal(ncff, ncfo, ncfi):
    cushion = _rsum(ncff + ncfi, 504)
    burn = _rsum(_f20_burn(ncfo), 504).replace(0, np.nan)
    b = cushion / burn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing inflow vs outflow asymmetry (raise-heavy vs repay-heavy) 252d
def f20fd_f20_financing_dependence_finasym_252d_base_v114_signal(ncff):
    inflow = _rsum(ncff.clip(lower=0), 252)
    outflow = _rsum((-ncff).clip(lower=0), 252)
    b = (inflow - outflow) / (inflow + outflow).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding gap acceleration (second difference of gap over quarters) 252d
def f20fd_f20_financing_dependence_gapaccel_252d_base_v115_signal(ncfo, ncfi, ncff):
    g = _f20_selffund_gap(ncfo, ncfi, ncff, 252)
    b = (g - g.shift(63)) - (g.shift(63) - g.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity reliance vs debt reliance crossover rank (financing-source dominance) 252d
def f20fd_f20_financing_dependence_srcdomrank_252d_base_v116_signal(ncfcommon, ncfdebt, ncfo):
    base = _rsum(ncfo.abs(), 252).replace(0, np.nan)
    eq = _rsum(ncfcommon.abs(), 252) / base
    dt = _rsum(ncfdebt.abs(), 252) / base
    diff = eq - dt
    b = diff.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing cover momentum smoothed (trend in burn coverage) 252d
def f20fd_f20_financing_dependence_covtrend_252d_base_v117_signal(ncff, ncfo):
    c = _f20_fin_cover(ncff, ncfo, 126)
    b = (c - c.shift(21)).ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total raises vs prior-year total raises (capital-raise growth) 252d
def f20fd_f20_financing_dependence_raisegrowth_252d_base_v118_signal(ncff):
    cur = _rsum(_f20_raise(ncff), 252)
    prior = cur.shift(252)
    b = (cur - prior) / (cur + prior).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net investing funded by financing vs operating (investing-fund source) 504d
def f20fd_f20_financing_dependence_invsrc_504d_base_v119_signal(ncff, ncfo, ncfi):
    inv = _rsum((-ncfi).clip(lower=0), 504).replace(0, np.nan)
    fin = _rsum(ncff, 504) / inv
    op = _rsum(ncfo, 504) / inv
    b = (fin - op) / (fin.abs() + op.abs() + 1e-9)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# external dependence vs cash-flow dispersion (dependence amid volatility) 252d
def f20fd_f20_financing_dependence_depvoladj_252d_base_v120_signal(ncff, ncfo, ncfi):
    d = _f20_dependence(ncff, ncfo, 252)
    disp = _std(ncfi, 252) / (_mean(ncfi.abs(), 252).replace(0, np.nan))
    b = d * disp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing mix tilt cycle-rank (debt-heavy vs equity-heavy regime distance) 252d
def f20fd_f20_financing_dependence_mixcyc_252d_base_v121_signal(ncfcommon, ncfdebt):
    m = _f20_eqdebt_mix(ncfcommon, ncfdebt, 252)
    b = m.rolling(1260, min_periods=252).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating self-coverage of investing, smoothed (internal growth funding) 252d
def f20fd_f20_financing_dependence_opinvcov_252d_base_v122_signal(ncfo, ncfi):
    op = _rsum(ncfo.clip(lower=0), 126)
    inv = _rsum((-ncfi).clip(lower=0), 126)
    cov = op / (op + inv).replace(0, np.nan)
    b = cov.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing dependence breadth across burn & investing needs (multi-need reliance)
def f20fd_f20_financing_dependence_multineed_252d_base_v123_signal(ncff, ncfo, ncfi):
    fin = _rsum(_f20_raise(ncff), 252)
    burn = _rsum(_f20_burn(ncfo), 252)
    inv = _rsum((-ncfi).clip(lower=0), 252)
    cover_burn = (fin >= burn).astype(float)
    cover_inv = (fin >= inv).astype(float)
    cover_both = (fin >= burn + inv).astype(float)
    raw = (cover_burn + cover_inv + cover_both) / 3.0
    cont = (fin - (burn + inv)) / (fin + burn + inv).replace(0, np.nan)
    b = raw + 0.3 * cont
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net financing direction vs investing direction agreement (raise-to-invest sync)
def f20fd_f20_financing_dependence_findirinv_252d_base_v124_signal(ncff, ncfi):
    f = _rsum(ncff, 252)
    i = _rsum(-ncfi, 252)
    b = np.sign(f) * np.sign(i) * (f.abs() / (f.abs() + i.abs()).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing cover excess vs investing-adjusted need (post-capex cushion) 252d
def f20fd_f20_financing_dependence_postcapexcush_252d_base_v125_signal(ncff, ncfo, ncfi):
    fin = _rsum(ncff, 252)
    need = _rsum(_f20_burn(ncfo) + (-ncfi).clip(lower=0), 252)
    b = np.tanh((fin - need) / (fin.abs() + need + 1.0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dependence per cash-flow turnover (financing intensity of all flows) 252d
def f20fd_f20_financing_dependence_finintensity_252d_base_v126_signal(ncff, ncfo, ncfi):
    nf = _rsum(ncff, 252)
    turn = _rsum(ncff.abs() + ncfo.abs() + ncfi.abs(), 252)
    b = _z(nf / turn.replace(0, np.nan), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity issuance share of financing inflows (equity-tilt of raises) 504d
def f20fd_f20_financing_dependence_eqinshare_504d_base_v127_signal(ncfcommon, ncff):
    eq = _rsum(ncfcommon.clip(lower=0), 504)
    fin = _rsum(_f20_raise(ncff), 504)
    b = eq / fin.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt issuance share of financing inflows (debt-tilt of raises) 504d
def f20fd_f20_financing_dependence_dtinshare_504d_base_v128_signal(ncfdebt, ncff):
    dt = _rsum(ncfdebt.clip(lower=0), 504)
    fin = _rsum(_f20_raise(ncff), 504)
    b = dt / fin.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding deficit count: number of net-external-reliant quarters (504d) blended
def f20fd_f20_financing_dependence_deficitcnt_504d_base_v129_signal(ncfo, ncfi, ncff):
    internal = ncfo.rolling(63, min_periods=21).sum() + ncfi.rolling(63, min_periods=21).sum()
    ext = ncff.rolling(63, min_periods=21).sum()
    reliant = ((internal < 0) & (ext > 0)).astype(float)
    cnt = reliant.rolling(504, min_periods=252).sum()
    depth = (ext - internal.abs()) / (ext.abs() + internal.abs()).replace(0, np.nan)
    b = cnt + depth.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing reliance interaction with deteriorating ops (rising burn + raises)
def f20fd_f20_financing_dependence_distressfin_252d_base_v130_signal(ncff, ncfo):
    burn = _rsum(_f20_burn(ncfo), 252)
    burn_mom = burn - burn.shift(63)
    raise_ = _rsum(_f20_raise(ncff), 252)
    raise_mom = raise_ - raise_.shift(63)
    b = np.sign(burn_mom) * np.sign(raise_mom) * np.log1p((raise_.abs()) / (burn + 1.0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net financing per gross flows ranked vs cycle (financing-direction extremity) 504d
def f20fd_f20_financing_dependence_findirrank_504d_base_v131_signal(ncff):
    nf = _rsum(ncff, 504)
    gf = _rsum(ncff.abs(), 504)
    r = nf / gf.replace(0, np.nan)
    b = r.rolling(1260, min_periods=252).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt-cover minus net-equity-cover of burn, z-scored (signed funding source)
def f20fd_f20_financing_dependence_coversrcspr_252d_base_v132_signal(ncfdebt, ncfcommon, ncfo):
    burn = _rsum(_f20_burn(ncfo), 252).replace(0, np.nan)
    dtc = _rsum(ncfdebt, 252) / burn
    eqc = _rsum(ncfcommon, 252) / burn
    b = _z(dtc - eqc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# external financing as fraction of all cash raised (vs operating receipts) 252d
def f20fd_f20_financing_dependence_extofraised_252d_base_v133_signal(ncff, ncfo):
    ext = _rsum(_f20_raise(ncff), 252)
    op_in = _rsum(ncfo.clip(lower=0), 252)
    b = ext / (ext + op_in).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding gap volatility (instability of dependence) 504d
def f20fd_f20_financing_dependence_gapvol_504d_base_v134_signal(ncfo, ncfi, ncff):
    g = _f20_selffund_gap(ncfo, ncfi, ncff, 126)
    b = _std(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-financing flow z vs equity-financing flow z spread (source momentum gap) 252d
def f20fd_f20_financing_dependence_srcmomgap_252d_base_v135_signal(ncfdebt, ncfcommon):
    dz = _z(_rsum(ncfdebt, 126), 252)
    ez = _z(_rsum(ncfcommon, 126), 252)
    b = dz - ez
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing cover deep-cycle percentile, sign-flipped (chronic burn-reliance) 252d
def f20fd_f20_financing_dependence_coverchron_252d_base_v136_signal(ncff, ncfo):
    c = _f20_fin_cover(ncff, ncfo, 252)
    b = -(c.rolling(1260, min_periods=252).rank(pct=True) - 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net financing minus net operating minus net investing (residual external) 252d
def f20fd_f20_financing_dependence_residext_252d_base_v137_signal(ncff, ncfo, ncfi):
    resid = _rsum(ncff + ncfo + ncfi, 252)
    scale = _rsum(ncff.abs() + ncfo.abs() + ncfi.abs(), 252).replace(0, np.nan)
    b = resid / scale
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# external-reliance entropy of three sources (op/equity/debt) inflows 252d
def f20fd_f20_financing_dependence_srcentropy_252d_base_v138_signal(ncfo, ncfcommon, ncfdebt):
    op = _rsum(ncfo.clip(lower=0), 252)
    eq = _rsum(ncfcommon.clip(lower=0), 252)
    dt = _rsum(ncfdebt.clip(lower=0), 252)
    tot = (op + eq + dt).replace(0, np.nan)
    p1 = (op / tot).clip(1e-6, 1)
    p2 = (eq / tot).clip(1e-6, 1)
    p3 = (dt / tot).clip(1e-6, 1)
    b = -(p1 * np.log(p1) + p2 * np.log(p2) + p3 * np.log(p3))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing-funded-burn surplus smoothed and ranked (durable cushion) 252d
def f20fd_f20_financing_dependence_cushrank_252d_base_v139_signal(ncff, ncfo):
    fin = _rsum(_f20_raise(ncff), 252)
    burn = _rsum(_f20_burn(ncfo), 252)
    surplus = (fin - burn) / (fin + burn).replace(0, np.nan)
    b = surplus.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dependence growth vs investing growth divergence (raise-led vs grow-led) 252d
def f20fd_f20_financing_dependence_raisevsgrow_252d_base_v140_signal(ncff, ncfi):
    raise_g = _rsum(_f20_raise(ncff), 126)
    inv_g = _rsum((-ncfi).clip(lower=0), 126)
    rg = raise_g.pct_change(63)
    ig = inv_g.pct_change(63)
    b = rg - ig
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net financing vs net investing balance smoothed (external growth-funding bias)
def f20fd_f20_financing_dependence_growbias_504d_base_v141_signal(ncff, ncfi):
    nf = _rsum(ncff, 504)
    ni = _rsum(ncfi, 504)
    bal = (nf + ni) / (nf.abs() + ni.abs()).replace(0, np.nan)
    b = bal.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-issuance acceleration relative to burn (leverage ramp into distress) 252d
def f20fd_f20_financing_dependence_levramp_252d_base_v142_signal(ncfdebt, ncfo):
    dt = _rsum(ncfdebt.clip(lower=0), 252)
    burn = _rsum(_f20_burn(ncfo), 252).replace(0, np.nan)
    r = dt / burn
    b = (r - r.shift(63)) - (r.shift(63) - r.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-cash share of covering total outflows (internal sufficiency) 252d
def f20fd_f20_financing_dependence_intsuffic_252d_base_v143_signal(ncfo, ncfi, ncff):
    op = _rsum(ncfo.clip(lower=0), 252)
    outflows = _rsum(_f20_burn(ncfo) + (-ncfi).clip(lower=0) + (-ncff).clip(lower=0), 252)
    b = op / (op + outflows).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing reliance level minus its cross-window median (relative dependence) 252d
def f20fd_f20_financing_dependence_reldevmed_252d_base_v144_signal(ncff, ncfo):
    d = _f20_dependence(ncff, ncfo, 252)
    med = d.rolling(504, min_periods=126).median()
    b = (d - med) / (med.abs() + 1e-9)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net equity issuance vs net debt issuance log balance (funding preference) 504d
def f20fd_f20_financing_dependence_netfundpref_504d_base_v145_signal(ncfcommon, ncfdebt):
    ne = _rsum(ncfcommon, 504)
    nd = _rsum(ncfdebt, 504)
    b = np.arctan(ne / (nd.abs() + 1e6)) - np.arctan(nd / (ne.abs() + 1e6))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-raise dependence smoothed cycle-z (chronic external reliance) 252d
def f20fd_f20_financing_dependence_raisechron_252d_base_v146_signal(ncff, ncfo, ncfi):
    raise_ = _rsum(_f20_raise(ncff), 252)
    inflow = _rsum(ncfo.clip(lower=0) + ncfi.clip(lower=0), 252)
    share = raise_ / (raise_ + inflow).replace(0, np.nan)
    b = _z(share, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing cover vs self-funding gap composite (dual dependence score) 252d
def f20fd_f20_financing_dependence_dualdep_252d_base_v147_signal(ncff, ncfo, ncfi):
    cov = np.tanh(_f20_fin_cover(ncff, ncfo, 252) - 1.0)
    gap = _f20_selffund_gap(ncfo, ncfi, ncff, 252)
    b = 0.5 * gap - 0.5 * cov
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# external financing flow skew over the cycle (lumpy raise pattern) 252d
def f20fd_f20_financing_dependence_finskew_252d_base_v148_signal(ncff):
    q = _f20_raise(ncff).rolling(21, min_periods=10).sum()
    b = q.rolling(252, min_periods=126).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-reliance minus equity-reliance smoothed (net source dependence) 252d
def f20fd_f20_financing_dependence_netsrcdep_252d_base_v149_signal(ncfdebt, ncfcommon, ncfo):
    base = _rsum(ncfo.abs(), 252).replace(0, np.nan)
    dt = _rsum(ncfdebt.abs(), 252) / base
    eq = _rsum(ncfcommon.abs(), 252) / base
    b = (dt - eq).ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite financing-dependence severity: gap x cover-deficit x footprint 252d
def f20fd_f20_financing_dependence_severity_252d_base_v150_signal(ncff, ncfo, ncfi):
    gap = _f20_selffund_gap(ncfo, ncfi, ncff, 252)
    cov = _f20_fin_cover(ncff, ncfo, 252)
    deficit = (1.0 / (1.0 + cov.clip(lower=0)))
    fin = _rsum(ncff.abs(), 252)
    tot = _rsum(ncff.abs() + ncfo.abs() + ncfi.abs(), 252)
    foot = fin / tot.replace(0, np.nan)
    b = gap * deficit * foot
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f20fd_f20_financing_dependence_netrelin_252d_base_v076_signal,
    f20fd_f20_financing_dependence_raiseconc_252d_base_v077_signal,
    f20fd_f20_financing_dependence_srchhi_252d_base_v078_signal,
    f20fd_f20_financing_dependence_coverdeepz_252d_base_v079_signal,
    f20fd_f20_financing_dependence_depaccel_252d_base_v080_signal,
    f20fd_f20_financing_dependence_dtops_252d_base_v081_signal,
    f20fd_f20_financing_dependence_eqops_252d_base_v082_signal,
    f20fd_f20_financing_dependence_fundspend_504d_base_v083_signal,
    f20fd_f20_financing_dependence_gapterm_base_v084_signal,
    f20fd_f20_financing_dependence_relismrank_252d_base_v085_signal,
    f20fd_f20_financing_dependence_dtrepay_252d_base_v086_signal,
    f20fd_f20_financing_dependence_eqnetdir_252d_base_v087_signal,
    f20fd_f20_financing_dependence_coverlog_252d_base_v088_signal,
    f20fd_f20_financing_dependence_capexfund_252d_base_v089_signal,
    f20fd_f20_financing_dependence_depinstab_252d_base_v090_signal,
    f20fd_f20_financing_dependence_extneedcov_252d_base_v091_signal,
    f20fd_f20_financing_dependence_mixdisp_252d_base_v092_signal,
    f20fd_f20_financing_dependence_coverstreak_252d_base_v093_signal,
    f20fd_f20_financing_dependence_depyoy_252d_base_v094_signal,
    f20fd_f20_financing_dependence_finperop_504d_base_v095_signal,
    f20fd_f20_financing_dependence_dtveq_inv_252d_base_v096_signal,
    f20fd_f20_financing_dependence_footmom_252d_base_v097_signal,
    f20fd_f20_financing_dependence_growsignmag_252d_base_v098_signal,
    f20fd_f20_financing_dependence_gapchron_504d_base_v099_signal,
    f20fd_f20_financing_dependence_depxconc_252d_base_v100_signal,
    f20fd_f20_financing_dependence_finchurn_252d_base_v101_signal,
    f20fd_f20_financing_dependence_levtilt_252d_base_v102_signal,
    f20fd_f20_financing_dependence_covregime_504d_base_v103_signal,
    f20fd_f20_financing_dependence_depdisp_base_v104_signal,
    f20fd_f20_financing_dependence_eqraisemom_252d_base_v105_signal,
    f20fd_f20_financing_dependence_dtraisemom_252d_base_v106_signal,
    f20fd_f20_financing_dependence_intfundshare_252d_base_v107_signal,
    f20fd_f20_financing_dependence_growrelz_252d_base_v108_signal,
    f20fd_f20_financing_dependence_finpresstanh_252d_base_v109_signal,
    f20fd_f20_financing_dependence_selfloggap_252d_base_v110_signal,
    f20fd_f20_financing_dependence_deprankmom_252d_base_v111_signal,
    f20fd_f20_financing_dependence_jointraise_252d_base_v112_signal,
    f20fd_f20_financing_dependence_extcushion_504d_base_v113_signal,
    f20fd_f20_financing_dependence_finasym_252d_base_v114_signal,
    f20fd_f20_financing_dependence_gapaccel_252d_base_v115_signal,
    f20fd_f20_financing_dependence_srcdomrank_252d_base_v116_signal,
    f20fd_f20_financing_dependence_covtrend_252d_base_v117_signal,
    f20fd_f20_financing_dependence_raisegrowth_252d_base_v118_signal,
    f20fd_f20_financing_dependence_invsrc_504d_base_v119_signal,
    f20fd_f20_financing_dependence_depvoladj_252d_base_v120_signal,
    f20fd_f20_financing_dependence_mixcyc_252d_base_v121_signal,
    f20fd_f20_financing_dependence_opinvcov_252d_base_v122_signal,
    f20fd_f20_financing_dependence_multineed_252d_base_v123_signal,
    f20fd_f20_financing_dependence_findirinv_252d_base_v124_signal,
    f20fd_f20_financing_dependence_postcapexcush_252d_base_v125_signal,
    f20fd_f20_financing_dependence_finintensity_252d_base_v126_signal,
    f20fd_f20_financing_dependence_eqinshare_504d_base_v127_signal,
    f20fd_f20_financing_dependence_dtinshare_504d_base_v128_signal,
    f20fd_f20_financing_dependence_deficitcnt_504d_base_v129_signal,
    f20fd_f20_financing_dependence_distressfin_252d_base_v130_signal,
    f20fd_f20_financing_dependence_findirrank_504d_base_v131_signal,
    f20fd_f20_financing_dependence_coversrcspr_252d_base_v132_signal,
    f20fd_f20_financing_dependence_extofraised_252d_base_v133_signal,
    f20fd_f20_financing_dependence_gapvol_504d_base_v134_signal,
    f20fd_f20_financing_dependence_srcmomgap_252d_base_v135_signal,
    f20fd_f20_financing_dependence_coverchron_252d_base_v136_signal,
    f20fd_f20_financing_dependence_residext_252d_base_v137_signal,
    f20fd_f20_financing_dependence_srcentropy_252d_base_v138_signal,
    f20fd_f20_financing_dependence_cushrank_252d_base_v139_signal,
    f20fd_f20_financing_dependence_raisevsgrow_252d_base_v140_signal,
    f20fd_f20_financing_dependence_growbias_504d_base_v141_signal,
    f20fd_f20_financing_dependence_levramp_252d_base_v142_signal,
    f20fd_f20_financing_dependence_intsuffic_252d_base_v143_signal,
    f20fd_f20_financing_dependence_reldevmed_252d_base_v144_signal,
    f20fd_f20_financing_dependence_netfundpref_504d_base_v145_signal,
    f20fd_f20_financing_dependence_raisechron_252d_base_v146_signal,
    f20fd_f20_financing_dependence_dualdep_252d_base_v147_signal,
    f20fd_f20_financing_dependence_finskew_252d_base_v148_signal,
    f20fd_f20_financing_dependence_netsrcdep_252d_base_v149_signal,
    f20fd_f20_financing_dependence_severity_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F20_FINANCING_DEPENDENCE_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.0, vol=0.08, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.5
        return pd.Series(s, name=None)

    def _flow(seed, center, amp=1.0, vol=0.09):
        f = _fund(seed, base=1e8, drift=0.0, vol=vol, allow_neg=False)
        osc = f - f.rolling(189, min_periods=20).mean()
        osc = osc.bfill()
        return center + amp * osc

    ncff = _flow(201, 8e6, 1.0).rename("ncff")
    ncfcommon = _flow(202, 0.0, 1.1).rename("ncfcommon")
    ncfdebt = _flow(203, 4e6, 0.9).rename("ncfdebt")
    ncfo = _flow(204, -6e6, 1.2).rename("ncfo")
    ncfi = _flow(205, -10e6, 1.3).rename("ncfi")

    cols = {"ncff": ncff, "ncfcommon": ncfcommon, "ncfdebt": ncfdebt,
            "ncfo": ncfo, "ncfi": ncfi}

    fundamental_cols = set(cols.keys())
    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        ins = meta["inputs"]
        assert any(c in fundamental_cols for c in ins), "no fundamental input: %s" % name
        fn = meta["func"]
        args = [cols[c] for c in ins]
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

    print("OK f20_financing_dependence_base_076_150_claude: %d features pass" % n_features)
