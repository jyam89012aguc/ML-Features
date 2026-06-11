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


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _slope(s, w):
    def _f(a):
        m = len(a)
        idx = np.arange(m, dtype=float)
        idx = idx - idx.mean()
        denom = (idx ** 2).sum()
        if denom == 0:
            return np.nan
        return float(np.dot(idx, a - a.mean()) / denom)
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_f, raw=True)


def _chg(s, k):
    return s - s.shift(k)


def _pctchg(s, k):
    return s / s.shift(k).replace(0, np.nan) - 1.0


# ===== folder domain primitives (earnings quality / accruals) =====
def _f35_sloan_accrual(netinc, ncfo, assets):
    return (netinc - ncfo) / assets.replace(0, np.nan)


def _f35_cash_earn_spread(ncfo, netinc, assets):
    return (ncfo - netinc) / assets.replace(0, np.nan)


def _f35_cash_conv(ncfo, netinc):
    return ncfo / netinc.replace(0, np.nan)


def _f35_dwc_accrual(workingcapital, assets, k):
    dwc = workingcapital - workingcapital.shift(k)
    return dwc / assets.replace(0, np.nan)


def _f35_recv_intensity(receivables, revenue):
    return receivables / revenue.replace(0, np.nan)


def _f35_recv_vs_rev_growth(receivables, revenue, k):
    rg = receivables / receivables.shift(k).replace(0, np.nan) - 1.0
    sg = revenue / revenue.shift(k).replace(0, np.nan) - 1.0
    return rg - sg


def _f35_accrual_ratio_bs(workingcapital, assets):
    return workingcapital / assets.replace(0, np.nan)


# ============================================================
# Sloan accrual measured over a half-year window, EMA-smoothed level
def f35eq_f35_earnings_quality_accruals_sloanhalf_126d_base_v076_signal(netinc, ncfo, assets):
    acc = _f35_sloan_accrual(netinc, ncfo, assets)
    b = -acc.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sloan accrual scaled by REVENUE instead of assets (sales-normalized accrual)
def f35eq_f35_earnings_quality_accruals_sloanrev_252d_base_v077_signal(netinc, ncfo, revenue):
    acc = (netinc - ncfo) / revenue.replace(0, np.nan)
    b = -_mean(acc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-scaled Sloan accrual slope (sales-normalized accrual trend)
def f35eq_f35_earnings_quality_accruals_sloanrevslope_252d_base_v078_signal(netinc, ncfo, revenue):
    acc = (netinc - ncfo) / revenue.replace(0, np.nan)
    b = -_slope(acc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-scaled accrual rank vs cross-time
def f35eq_f35_earnings_quality_accruals_sloanrevrank_504d_base_v079_signal(netinc, ncfo, revenue):
    acc = (netinc - ncfo) / revenue.replace(0, np.nan)
    b = -_rank(acc, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual quarter-over-quarter acceleration (second difference of accrual)
def f35eq_f35_earnings_quality_accruals_accaccel_63d_base_v080_signal(netinc, ncfo, assets):
    acc = _f35_sloan_accrual(netinc, ncfo, assets)
    d = _chg(acc, 63)
    b = -(d - d.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-conversion gap from 1.0 (how far ncfo/netinc deviates from full conversion)
def f35eq_f35_earnings_quality_accruals_convgap_252d_base_v081_signal(ncfo, netinc):
    cc = _f35_cash_conv(ncfo, netinc).clip(-10, 10)
    b = -_mean((cc - 1.0).abs(), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-conversion slope (improving conversion over a year)
def f35eq_f35_earnings_quality_accruals_convslope_252d_base_v082_signal(ncfo, netinc):
    cc = _f35_cash_conv(ncfo, netinc).clip(-10, 10)
    b = _slope(cc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-income volatility relative to assets (earnings instability per asset base)
def f35eq_f35_earnings_quality_accruals_nivol_252d_base_v083_signal(netinc, assets):
    roa = netinc / assets.replace(0, np.nan)
    b = -_std(roa, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-flow volatility relative to assets (cash instability)
def f35eq_f35_earnings_quality_accruals_cfvol_252d_base_v084_signal(ncfo, assets):
    cfoa = ncfo / assets.replace(0, np.nan)
    b = -_std(cfoa, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ΔWC accrual over a month, scaled by assets (short-horizon WC build)
def f35eq_f35_earnings_quality_accruals_dwc_21d_base_v085_signal(workingcapital, assets):
    b = -_f35_dwc_accrual(workingcapital, assets, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ΔWC accrual rank vs cross-time (relative WC-build extremity)
def f35eq_f35_earnings_quality_accruals_dwcrank_504d_base_v086_signal(workingcapital, assets):
    dwc = _f35_dwc_accrual(workingcapital, assets, 63)
    b = -_rank(dwc, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# WC intensity EMA displacement (recent balance-sheet bloat surprise)
def f35eq_f35_earnings_quality_accruals_wcdisp_252d_base_v087_signal(workingcapital, assets):
    ar = _f35_accrual_ratio_bs(workingcapital, assets)
    b = -(ar - ar.ewm(span=126, min_periods=63).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO intensity slope over half-year (faster collection deterioration)
def f35eq_f35_earnings_quality_accruals_dsoslopeh_126d_base_v088_signal(receivables, revenue):
    ri = _f35_recv_intensity(receivables, revenue)
    b = -_slope(ri, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO intensity EMA crossover (collection-bloat regime shift, fast vs slow)
def f35eq_f35_earnings_quality_accruals_dsoema_126d_base_v089_signal(receivables, revenue):
    ri = _f35_recv_intensity(receivables, revenue)
    fast = ri.ewm(span=42, min_periods=21).mean()
    slow = ri.ewm(span=189, min_periods=63).mean()
    b = -(fast - slow)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables-growth minus revenue-growth over a month (recent channel divergence)
def f35eq_f35_earnings_quality_accruals_recvrev_21d_base_v090_signal(receivables, revenue):
    b = -_f35_recv_vs_rev_growth(receivables, revenue, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables-growth vs revenue-growth gap slope (worsening divergence trend)
def f35eq_f35_earnings_quality_accruals_recvrevslope_252d_base_v091_signal(receivables, revenue):
    g = _f35_recv_vs_rev_growth(receivables, revenue, 63)
    b = -_slope(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual reversal over two years (long-horizon mean-reversion of accruals)
def f35eq_f35_earnings_quality_accruals_reversal_504d_base_v092_signal(netinc, ncfo, assets):
    acc = _f35_sloan_accrual(netinc, ncfo, assets)
    am = _mean(acc, 126)
    b = -(am - am.shift(504))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual half-life proxy: ratio of recent to lagged accrual magnitude (persistence)
def f35eq_f35_earnings_quality_accruals_halflife_252d_base_v093_signal(netinc, ncfo, assets):
    acc = _f35_sloan_accrual(netinc, ncfo, assets).abs()
    recent = _mean(acc, 63)
    lagged = _mean(acc, 63).shift(189).replace(0, np.nan)
    b = -(recent / lagged).clip(0, 20)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sloan accrual cross-window spread (quarter accrual vs year accrual)
def f35eq_f35_earnings_quality_accruals_accspr_63v252_base_v094_signal(netinc, ncfo, assets):
    acc = _f35_sloan_accrual(netinc, ncfo, assets)
    b = -(_mean(acc, 63) - _mean(acc, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-earnings co-movement over half-year (short-horizon alignment)
def f35eq_f35_earnings_quality_accruals_nicfcorr_126d_base_v095_signal(netinc, ncfo):
    dni = netinc.pct_change()
    dcf = ncfo.pct_change()
    b = dni.rolling(126, min_periods=63).corr(dcf)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# earnings-smoothness ratio over half-year (managed vs cash variability)
def f35eq_f35_earnings_quality_accruals_smooth_126d_base_v096_signal(netinc, ncfo):
    vni = _std(netinc.pct_change(), 126)
    vcf = _std(ncfo.pct_change(), 126).replace(0, np.nan)
    b = vni / vcf
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables share of assets slope (balance-sheet receivable build trend)
def f35eq_f35_earnings_quality_accruals_recvassetslope_252d_base_v097_signal(receivables, assets):
    ra = receivables / assets.replace(0, np.nan)
    b = -_slope(ra, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-turnover quality: revenue/assets z-scored (productivity standing)
def f35eq_f35_earnings_quality_accruals_turnz_252d_base_v098_signal(revenue, assets):
    rt = revenue / assets.replace(0, np.nan)
    b = _z(rt, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual-adjusted ROA trend: cash ROA slope minus accrual penalty slope
def f35eq_f35_earnings_quality_accruals_qroaslope_252d_base_v099_signal(netinc, ncfo, assets):
    croa = ncfo / assets.replace(0, np.nan)
    acc = _f35_sloan_accrual(netinc, ncfo, assets).abs()
    b = _slope(croa, 252) - _slope(acc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-ROA-vs-accrual-ROA rank gap, EMA-smoothed (persistent relative quality gap)
def f35eq_f35_earnings_quality_accruals_roagapema_252d_base_v100_signal(ncfo, netinc, assets):
    croa = ncfo / assets.replace(0, np.nan)
    aroa = netinc / assets.replace(0, np.nan)
    gap = _rank(croa, 252) - _rank(aroa, 252)
    b = gap.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed accrual level (bounded accrual penalty)
def f35eq_f35_earnings_quality_accruals_acctanhlvl_252d_base_v101_signal(netinc, ncfo, assets):
    acc = _mean(_f35_sloan_accrual(netinc, ncfo, assets), 252)
    b = -np.tanh(10.0 * acc)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign-magnitude of cash-earnings spread CHANGE (bounded recent cash-backing swing)
def f35eq_f35_earnings_quality_accruals_cesignmag_252d_base_v102_signal(ncfo, netinc, assets):
    sp = _f35_cash_earn_spread(ncfo, netinc, assets)
    chg = _chg(sp, 63)
    b = np.sign(chg) * (chg.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO change month-over-month bounded (recent collection swing)
def f35eq_f35_earnings_quality_accruals_dsotanh_63d_base_v103_signal(receivables, revenue):
    ri = _f35_recv_intensity(receivables, revenue)
    chg = _chg(ri, 63)
    b = -np.tanh(5.0 * chg / ri.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# WC-accrual deterioration share via continuous positive-build magnitude
def f35eq_f35_earnings_quality_accruals_wcbuild_252d_base_v104_signal(workingcapital, assets):
    dwc = _f35_dwc_accrual(workingcapital, assets, 21)
    build = dwc.clip(lower=0)
    b = -_mean(build, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual skewness proxy: mean minus median of accrual (asymmetry of accrual distribution)
def f35eq_f35_earnings_quality_accruals_accskew_252d_base_v105_signal(netinc, ncfo, assets):
    acc = _f35_sloan_accrual(netinc, ncfo, assets)
    mn = _mean(acc, 252)
    md = acc.rolling(252, min_periods=126).median()
    sd = _std(acc, 252).replace(0, np.nan)
    b = -(mn - md) / sd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# conversion-stability rank (relative reliability of cash backing)
def f35eq_f35_earnings_quality_accruals_convstabrank_504d_base_v106_signal(ncfo, netinc):
    cc = _f35_cash_conv(ncfo, netinc).clip(-10, 10)
    instab = _std(cc, 63)
    b = -_rank(instab, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables/revenue growth gap, EMA-smoothed (persistent divergence)
def f35eq_f35_earnings_quality_accruals_recvrevema_252d_base_v107_signal(receivables, revenue):
    g = _f35_recv_vs_rev_growth(receivables, revenue, 63)
    b = -g.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual change acceleration normalized by accrual scale (relative jerk-like build)
def f35eq_f35_earnings_quality_accruals_accchgnorm_63d_base_v108_signal(netinc, ncfo, assets):
    acc = _f35_sloan_accrual(netinc, ncfo, assets)
    d = _chg(acc, 63)
    scale = _mean(acc.abs(), 252).replace(0, np.nan)
    b = -d / scale
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-conversion x revenue-growth interaction over a year (cash-funded growth)
def f35eq_f35_earnings_quality_accruals_convgrowth_252d_base_v109_signal(ncfo, netinc, revenue):
    cc = (ncfo / netinc.replace(0, np.nan)).clip(-5, 5)
    sg = _pctchg(revenue, 252).clip(-2, 2)
    b = _mean(cc * (1.0 + sg), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-growth funded by receivables: revenue growth x DSO change (low quality if both up)
def f35eq_f35_earnings_quality_accruals_growthdso_252d_base_v110_signal(revenue, receivables):
    sg = _pctchg(revenue, 252).clip(-2, 2)
    dso = _f35_recv_intensity(receivables, revenue)
    ddso = _chg(dso, 63)
    b = -(sg * ddso)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual level percentile within a 252d window (anomaly flag, short memory)
def f35eq_f35_earnings_quality_accruals_accrank_252d_base_v111_signal(netinc, ncfo, assets):
    acc = _f35_sloan_accrual(netinc, ncfo, assets)
    b = -_rank(acc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-earnings spread EMA displacement (recent cash-backing surprise)
def f35eq_f35_earnings_quality_accruals_cespreaddisp_252d_base_v112_signal(ncfo, netinc, assets):
    sp = _f35_cash_earn_spread(ncfo, netinc, assets)
    b = sp - sp.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO dispersion via rolling range (collection-period instability)
def f35eq_f35_earnings_quality_accruals_dsorange_252d_base_v113_signal(receivables, revenue):
    ri = _f35_recv_intensity(receivables, revenue)
    rng = ri.rolling(252, min_periods=126).max() - ri.rolling(252, min_periods=126).min()
    b = -rng / _mean(ri, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# WC-accrual cross-window spread (month build vs quarter build)
def f35eq_f35_earnings_quality_accruals_dwcspr_21v63_base_v114_signal(workingcapital, assets):
    s = _f35_dwc_accrual(workingcapital, assets, 21)
    l = _f35_dwc_accrual(workingcapital, assets, 63) / 3.0
    b = -(s - l)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-income-to-cash lead-lag corr (earnings leading cash = potential management)
def f35eq_f35_earnings_quality_accruals_leadlag_252d_base_v115_signal(netinc, ncfo):
    dni = netinc.pct_change()
    dcf = ncfo.pct_change().shift(-21)
    b = -dni.rolling(252, min_periods=126).corr(dcf)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual-reliability composite: cash margin minus accrual-volatility penalty
def f35eq_f35_earnings_quality_accruals_relcomp_252d_base_v116_signal(ncfo, revenue, netinc, assets):
    cm = ncfo / revenue.replace(0, np.nan)
    accvol = _std(_f35_sloan_accrual(netinc, ncfo, assets), 252)
    b = _mean(cm, 252) - 2.0 * accvol
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# real revenue growth (cash-collected sales growth) vs reported revenue growth
def f35eq_f35_earnings_quality_accruals_realrev_252d_base_v117_signal(revenue, receivables):
    cash_rev = revenue - _chg(receivables, 63)
    crg = _pctchg(cash_rev, 252)
    rrg = _pctchg(revenue, 252)
    b = (crg - rrg).clip(-3, 3)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# WC-to-revenue intensity slope (sales-normalized WC build trend)
def f35eq_f35_earnings_quality_accruals_wcrevslope_252d_base_v118_signal(workingcapital, revenue):
    wr = workingcapital / revenue.replace(0, np.nan)
    b = -_slope(wr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual quality score over two years: stable low accrual = high (rank of -|acc| dispersion)
def f35eq_f35_earnings_quality_accruals_qscore2_504d_base_v119_signal(netinc, ncfo, assets):
    acc = _f35_sloan_accrual(netinc, ncfo, assets)
    disp = _std(acc, 126)
    b = -_rank(disp, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-flow margin slope (operating cash per sales improving)
def f35eq_f35_earnings_quality_accruals_cfmarginslope_252d_base_v120_signal(ncfo, revenue):
    cfm = ncfo / revenue.replace(0, np.nan)
    b = _slope(cfm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-flow margin z-scored (de-trended cash generation per sales)
def f35eq_f35_earnings_quality_accruals_cfmarginz_252d_base_v121_signal(ncfo, revenue):
    cfm = ncfo / revenue.replace(0, np.nan)
    b = _z(cfm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin minus cash-margin EMA crossover (accrual content regime shift)
def f35eq_f35_earnings_quality_accruals_marginxover_252d_base_v122_signal(netinc, ncfo, revenue):
    spread = (netinc - ncfo) / revenue.replace(0, np.nan)
    fast = spread.ewm(span=42, min_periods=21).mean()
    slow = spread.ewm(span=189, min_periods=63).mean()
    b = -(fast - slow)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# convergence: |accrual| shrinking over time (quality improvement via accrual decay)
def f35eq_f35_earnings_quality_accruals_accdecay_252d_base_v123_signal(netinc, ncfo, assets):
    acc = _f35_sloan_accrual(netinc, ncfo, assets).abs()
    b = -_slope(acc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivable-collection efficiency: revenue/receivables level z-scored
def f35eq_f35_earnings_quality_accruals_collz_252d_base_v124_signal(revenue, receivables):
    coll = revenue / receivables.replace(0, np.nan)
    b = _z(coll, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual momentum spread: short-window accrual change minus long-window change
def f35eq_f35_earnings_quality_accruals_accmomspr_252d_base_v125_signal(netinc, ncfo, assets):
    acc = _f35_sloan_accrual(netinc, ncfo, assets)
    sm = _chg(acc, 21)
    lm = _chg(acc, 126) / 6.0
    b = -(sm - lm)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash conversion x asset turnover (cash-efficient capital deployment)
def f35eq_f35_earnings_quality_accruals_convturn_252d_base_v126_signal(ncfo, netinc, revenue, assets):
    cc = (ncfo / netinc.replace(0, np.nan)).clip(-5, 5)
    turn = revenue / assets.replace(0, np.nan)
    b = _mean(cc * turn, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual instability relative to cash-flow instability (managed-earnings tell)
def f35eq_f35_earnings_quality_accruals_accvscfvol_252d_base_v127_signal(netinc, ncfo, assets):
    accvol = _std(_f35_sloan_accrual(netinc, ncfo, assets), 252)
    cfvol = _std(ncfo / assets.replace(0, np.nan), 252).replace(0, np.nan)
    b = -accvol / cfvol
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO acceleration bounded (collection deterioration jerk)
def f35eq_f35_earnings_quality_accruals_dsoaccel_126d_base_v128_signal(receivables, revenue):
    ri = _f35_recv_intensity(receivables, revenue)
    d = _chg(ri, 63)
    accel = d - d.shift(63)
    b = -np.tanh(8.0 * accel / ri.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-earnings spread per unit revenue-growth (cash backing of growth)
def f35eq_f35_earnings_quality_accruals_cespergrow_252d_base_v129_signal(ncfo, netinc, revenue):
    sp = (ncfo - netinc) / revenue.replace(0, np.nan)
    sg = _pctchg(revenue, 252).abs() + 0.05
    b = _mean(sp, 63) / sg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# WC intensity year-over-year change (balance-sheet bloat YoY)
def f35eq_f35_earnings_quality_accruals_wcintyoy_252d_base_v130_signal(workingcapital, assets):
    ar = _f35_accrual_ratio_bs(workingcapital, assets)
    arm = _mean(ar, 63)
    b = -(arm - arm.shift(252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual sign-consistency: fraction of quarter accrual stays same sign (continuous proxy)
def f35eq_f35_earnings_quality_accruals_accconsist_252d_base_v131_signal(netinc, ncfo, assets):
    acc = _f35_sloan_accrual(netinc, ncfo, assets)
    mn = _mean(acc, 63)
    sd = _std(acc, 63).replace(0, np.nan)
    b = -(mn.abs() / sd)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-conversion deviation z (extreme conversion regime, de-trended)
def f35eq_f35_earnings_quality_accruals_convz_252d_base_v132_signal(ncfo, netinc):
    cc = _f35_cash_conv(ncfo, netinc).clip(-10, 10)
    b = _z(cc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables vs assets growth divergence (receivable bloat relative to asset base)
def f35eq_f35_earnings_quality_accruals_recvassetdiv_252d_base_v133_signal(receivables, assets):
    rg = _pctchg(receivables, 252)
    ag = _pctchg(assets, 252)
    b = -(rg - ag).clip(-3, 3)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual reversal asymmetry: positive-build vs negative-reversal magnitude
def f35eq_f35_earnings_quality_accruals_revasym_252d_base_v134_signal(netinc, ncfo, assets):
    acc = _f35_sloan_accrual(netinc, ncfo, assets)
    d = _chg(acc, 21)
    up = d.clip(lower=0).rolling(252, min_periods=126).mean()
    dn = (-d).clip(lower=0).rolling(252, min_periods=126).mean()
    b = -(up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-margin minus net-margin, slope of the spread (accrual content trend)
def f35eq_f35_earnings_quality_accruals_marginrank_504d_base_v135_signal(ncfo, netinc, revenue):
    cm = ncfo / revenue.replace(0, np.nan)
    nm = netinc / revenue.replace(0, np.nan)
    b = _slope(cm - nm, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual quality trend rank (improving vs worsening accruals, percentile of slope)
def f35eq_f35_earnings_quality_accruals_acctrendrank_504d_base_v136_signal(netinc, ncfo, assets):
    acc = _f35_sloan_accrual(netinc, ncfo, assets)
    sl = _slope(acc, 63)
    b = -_rank(sl, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-cash-to-WC: cash generated relative to working capital committed
def f35eq_f35_earnings_quality_accruals_cfowc_252d_base_v137_signal(ncfo, workingcapital):
    ratio = ncfo / workingcapital.replace(0, np.nan)
    b = _mean(ratio.clip(-20, 20), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual displacement vs revenue scale (growth-normalized accrual surprise)
def f35eq_f35_earnings_quality_accruals_accdisprev_252d_base_v138_signal(netinc, ncfo, revenue):
    acc = (netinc - ncfo) / revenue.replace(0, np.nan)
    b = -(acc - acc.ewm(span=126, min_periods=63).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-conversion stability over two years (long-horizon reliability)
def f35eq_f35_earnings_quality_accruals_convstab2_504d_base_v139_signal(ncfo, netinc):
    cc = _f35_cash_conv(ncfo, netinc).clip(-10, 10)
    b = -_std(cc, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables intensity acceleration normalized (collection-deterioration jerk, revenue-scaled)
def f35eq_f35_earnings_quality_accruals_dsoaccelz_252d_base_v140_signal(receivables, revenue):
    ri = _f35_recv_intensity(receivables, revenue)
    d = _chg(ri, 63)
    accel = d - d.shift(63)
    b = -_z(accel, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash earnings vs accrual earnings rank gap (cash-quality standing minus accrual standing)
def f35eq_f35_earnings_quality_accruals_qualgaprank_504d_base_v141_signal(ncfo, netinc, assets):
    croa = ncfo / assets.replace(0, np.nan)
    aroa = netinc / assets.replace(0, np.nan)
    b = _rank(croa, 504) - _rank(aroa, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-income growth minus operating-cash growth, ranked (warning-divergence standing)
def f35eq_f35_earnings_quality_accruals_growthdivrank_504d_base_v142_signal(netinc, ncfo):
    nig = _pctchg(netinc, 252)
    cfg = _pctchg(ncfo, 252)
    b = -_rank((nig - cfg).clip(-5, 5), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# WC-accrual EMA momentum (accelerating balance-sheet build)
def f35eq_f35_earnings_quality_accruals_wcmom_126d_base_v143_signal(workingcapital, assets):
    ar = _f35_accrual_ratio_bs(workingcapital, assets)
    e = ar.ewm(span=63, min_periods=21).mean()
    b = -_chg(e, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual-to-asset-growth: are accruals growing faster than the asset base?
def f35eq_f35_earnings_quality_accruals_accvsasset_252d_base_v144_signal(netinc, ncfo, assets):
    acc = (netinc - ncfo)
    accg = _pctchg(acc.abs(), 252)
    ag = _pctchg(assets, 252)
    b = -(accg - ag).clip(-5, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-flow coverage of accruals: slope of ncfo/|accrual| coverage (improving cushion)
def f35eq_f35_earnings_quality_accruals_cfcover_252d_base_v145_signal(ncfo, netinc):
    acc = (netinc - ncfo).abs()
    cover = (ncfo.abs() / acc.replace(0, np.nan)).clip(0, 50)
    b = _slope(cover, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO bloat interaction with accrual level (compounding revenue-recognition risk)
def f35eq_f35_earnings_quality_accruals_dsoxacc_252d_base_v146_signal(receivables, revenue, netinc, ncfo, assets):
    dsoz = _z(_f35_recv_intensity(receivables, revenue), 252)
    accz = _z(_f35_sloan_accrual(netinc, ncfo, assets), 252)
    b = -_mean(dsoz * accz, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-quality: cash margin minus DSO-intensity (sales backed by cash, not receivables)
def f35eq_f35_earnings_quality_accruals_revqual2_252d_base_v147_signal(ncfo, revenue, receivables):
    cm = ncfo / revenue.replace(0, np.nan)
    dso = _f35_recv_intensity(receivables, revenue)
    b = _mean(cm, 252) - _z(dso, 252) * _std(cm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual percentile gap: short-window rank minus long-window rank (regime shift)
def f35eq_f35_earnings_quality_accruals_rankgap_252d_base_v148_signal(netinc, ncfo, assets):
    acc = _f35_sloan_accrual(netinc, ncfo, assets)
    rshort = acc.rolling(126, min_periods=63).rank(pct=True)
    rlong = acc.rolling(504, min_periods=252).rank(pct=True)
    b = -(rshort - rlong)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite quality: cash conversion centered, plus cash margin, minus WC bloat (multi-factor)
def f35eq_f35_earnings_quality_accruals_multicomp_252d_base_v149_signal(ncfo, netinc, revenue, workingcapital, assets):
    cc = (ncfo / netinc.replace(0, np.nan)).clip(-5, 5)
    cm = ncfo / revenue.replace(0, np.nan)
    wi = workingcapital / assets.replace(0, np.nan)
    raw = (cc - 1.0) + 5.0 * cm - 0.5 * wi
    b = _mean(raw, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual reversal half-year momentum normalized by accrual scale (mean-reversion strength)
def f35eq_f35_earnings_quality_accruals_revmomnorm_252d_base_v150_signal(netinc, ncfo, assets):
    acc = _f35_sloan_accrual(netinc, ncfo, assets)
    am = _mean(acc, 63)
    mom = am - am.shift(126)
    scale = _std(acc, 252).replace(0, np.nan)
    b = -mom / scale
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f35eq_f35_earnings_quality_accruals_sloanhalf_126d_base_v076_signal,
    f35eq_f35_earnings_quality_accruals_sloanrev_252d_base_v077_signal,
    f35eq_f35_earnings_quality_accruals_sloanrevslope_252d_base_v078_signal,
    f35eq_f35_earnings_quality_accruals_sloanrevrank_504d_base_v079_signal,
    f35eq_f35_earnings_quality_accruals_accaccel_63d_base_v080_signal,
    f35eq_f35_earnings_quality_accruals_convgap_252d_base_v081_signal,
    f35eq_f35_earnings_quality_accruals_convslope_252d_base_v082_signal,
    f35eq_f35_earnings_quality_accruals_nivol_252d_base_v083_signal,
    f35eq_f35_earnings_quality_accruals_cfvol_252d_base_v084_signal,
    f35eq_f35_earnings_quality_accruals_dwc_21d_base_v085_signal,
    f35eq_f35_earnings_quality_accruals_dwcrank_504d_base_v086_signal,
    f35eq_f35_earnings_quality_accruals_wcdisp_252d_base_v087_signal,
    f35eq_f35_earnings_quality_accruals_dsoslopeh_126d_base_v088_signal,
    f35eq_f35_earnings_quality_accruals_dsoema_126d_base_v089_signal,
    f35eq_f35_earnings_quality_accruals_recvrev_21d_base_v090_signal,
    f35eq_f35_earnings_quality_accruals_recvrevslope_252d_base_v091_signal,
    f35eq_f35_earnings_quality_accruals_reversal_504d_base_v092_signal,
    f35eq_f35_earnings_quality_accruals_halflife_252d_base_v093_signal,
    f35eq_f35_earnings_quality_accruals_accspr_63v252_base_v094_signal,
    f35eq_f35_earnings_quality_accruals_nicfcorr_126d_base_v095_signal,
    f35eq_f35_earnings_quality_accruals_smooth_126d_base_v096_signal,
    f35eq_f35_earnings_quality_accruals_recvassetslope_252d_base_v097_signal,
    f35eq_f35_earnings_quality_accruals_turnz_252d_base_v098_signal,
    f35eq_f35_earnings_quality_accruals_qroaslope_252d_base_v099_signal,
    f35eq_f35_earnings_quality_accruals_roagapema_252d_base_v100_signal,
    f35eq_f35_earnings_quality_accruals_acctanhlvl_252d_base_v101_signal,
    f35eq_f35_earnings_quality_accruals_cesignmag_252d_base_v102_signal,
    f35eq_f35_earnings_quality_accruals_dsotanh_63d_base_v103_signal,
    f35eq_f35_earnings_quality_accruals_wcbuild_252d_base_v104_signal,
    f35eq_f35_earnings_quality_accruals_accskew_252d_base_v105_signal,
    f35eq_f35_earnings_quality_accruals_convstabrank_504d_base_v106_signal,
    f35eq_f35_earnings_quality_accruals_recvrevema_252d_base_v107_signal,
    f35eq_f35_earnings_quality_accruals_accchgnorm_63d_base_v108_signal,
    f35eq_f35_earnings_quality_accruals_convgrowth_252d_base_v109_signal,
    f35eq_f35_earnings_quality_accruals_growthdso_252d_base_v110_signal,
    f35eq_f35_earnings_quality_accruals_accrank_252d_base_v111_signal,
    f35eq_f35_earnings_quality_accruals_cespreaddisp_252d_base_v112_signal,
    f35eq_f35_earnings_quality_accruals_dsorange_252d_base_v113_signal,
    f35eq_f35_earnings_quality_accruals_dwcspr_21v63_base_v114_signal,
    f35eq_f35_earnings_quality_accruals_leadlag_252d_base_v115_signal,
    f35eq_f35_earnings_quality_accruals_relcomp_252d_base_v116_signal,
    f35eq_f35_earnings_quality_accruals_realrev_252d_base_v117_signal,
    f35eq_f35_earnings_quality_accruals_wcrevslope_252d_base_v118_signal,
    f35eq_f35_earnings_quality_accruals_qscore2_504d_base_v119_signal,
    f35eq_f35_earnings_quality_accruals_cfmarginslope_252d_base_v120_signal,
    f35eq_f35_earnings_quality_accruals_cfmarginz_252d_base_v121_signal,
    f35eq_f35_earnings_quality_accruals_marginxover_252d_base_v122_signal,
    f35eq_f35_earnings_quality_accruals_accdecay_252d_base_v123_signal,
    f35eq_f35_earnings_quality_accruals_collz_252d_base_v124_signal,
    f35eq_f35_earnings_quality_accruals_accmomspr_252d_base_v125_signal,
    f35eq_f35_earnings_quality_accruals_convturn_252d_base_v126_signal,
    f35eq_f35_earnings_quality_accruals_accvscfvol_252d_base_v127_signal,
    f35eq_f35_earnings_quality_accruals_dsoaccel_126d_base_v128_signal,
    f35eq_f35_earnings_quality_accruals_cespergrow_252d_base_v129_signal,
    f35eq_f35_earnings_quality_accruals_wcintyoy_252d_base_v130_signal,
    f35eq_f35_earnings_quality_accruals_accconsist_252d_base_v131_signal,
    f35eq_f35_earnings_quality_accruals_convz_252d_base_v132_signal,
    f35eq_f35_earnings_quality_accruals_recvassetdiv_252d_base_v133_signal,
    f35eq_f35_earnings_quality_accruals_revasym_252d_base_v134_signal,
    f35eq_f35_earnings_quality_accruals_marginrank_504d_base_v135_signal,
    f35eq_f35_earnings_quality_accruals_acctrendrank_504d_base_v136_signal,
    f35eq_f35_earnings_quality_accruals_cfowc_252d_base_v137_signal,
    f35eq_f35_earnings_quality_accruals_accdisprev_252d_base_v138_signal,
    f35eq_f35_earnings_quality_accruals_convstab2_504d_base_v139_signal,
    f35eq_f35_earnings_quality_accruals_dsoaccelz_252d_base_v140_signal,
    f35eq_f35_earnings_quality_accruals_qualgaprank_504d_base_v141_signal,
    f35eq_f35_earnings_quality_accruals_growthdivrank_504d_base_v142_signal,
    f35eq_f35_earnings_quality_accruals_wcmom_126d_base_v143_signal,
    f35eq_f35_earnings_quality_accruals_accvsasset_252d_base_v144_signal,
    f35eq_f35_earnings_quality_accruals_cfcover_252d_base_v145_signal,
    f35eq_f35_earnings_quality_accruals_dsoxacc_252d_base_v146_signal,
    f35eq_f35_earnings_quality_accruals_revqual2_252d_base_v147_signal,
    f35eq_f35_earnings_quality_accruals_rankgap_252d_base_v148_signal,
    f35eq_f35_earnings_quality_accruals_multicomp_252d_base_v149_signal,
    f35eq_f35_earnings_quality_accruals_revmomnorm_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F35_EARNINGS_QUALITY_ACCRUALS_REGISTRY_076_150 = REGISTRY


def _fund(seed, n, base=1e8, drift=0.02, vol=0.05, allow_neg=False):
    g = np.random.default_rng(seed)
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.3
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    netinc = _fund(101, n, base=2e7, drift=0.02, vol=0.06, allow_neg=True).rename("netinc")
    ncfo = _fund(102, n, base=2.5e7, drift=0.02, vol=0.05, allow_neg=True).rename("ncfo")
    assets = _fund(103, n, base=5e8, drift=0.015, vol=0.03).rename("assets")
    receivables = _fund(104, n, base=8e7, drift=0.02, vol=0.05).rename("receivables")
    revenue = _fund(105, n, base=3e8, drift=0.02, vol=0.04).rename("revenue")
    workingcapital = _fund(106, n, base=6e7, drift=0.015, vol=0.06, allow_neg=True).rename("workingcapital")

    cols = {"netinc": netinc, "ncfo": ncfo, "assets": assets,
            "receivables": receivables, "revenue": revenue,
            "workingcapital": workingcapital}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, "%s nunique=%d" % (name, q.nunique())
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

    print("OK f35_earnings_quality_accruals_base_076_150_claude: %d features pass" % n_features)
