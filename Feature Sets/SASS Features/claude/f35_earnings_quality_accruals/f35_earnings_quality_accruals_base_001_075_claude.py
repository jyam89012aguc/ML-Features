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
    # OLS slope of s on time over window w (per-bar slope)
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
    # Sloan total accruals: (earnings - operating cash flow) / assets
    return (netinc - ncfo) / assets.replace(0, np.nan)


def _f35_cash_earn_spread(ncfo, netinc, assets):
    # cash-earnings spread normalized by assets (high = cash-backed earnings)
    return (ncfo - netinc) / assets.replace(0, np.nan)


def _f35_cash_conv(ncfo, netinc):
    # cash conversion ratio: operating cash flow / earnings
    return ncfo / netinc.replace(0, np.nan)


def _f35_dwc_accrual(workingcapital, assets, k):
    # change-in-working-capital accruals over k bars, scaled by assets
    dwc = workingcapital - workingcapital.shift(k)
    return dwc / assets.replace(0, np.nan)


def _f35_recv_intensity(receivables, revenue):
    # receivables relative to revenue (DSO-like, the days-sales-outstanding proxy)
    return receivables / revenue.replace(0, np.nan)


def _f35_recv_vs_rev_growth(receivables, revenue, k):
    # receivables growth minus revenue growth (manipulation tell)
    rg = receivables / receivables.shift(k).replace(0, np.nan) - 1.0
    sg = revenue / revenue.shift(k).replace(0, np.nan) - 1.0
    return rg - sg


def _f35_accrual_ratio_bs(workingcapital, assets):
    # balance-sheet accrual ratio level: working capital / assets
    return workingcapital / assets.replace(0, np.nan)


# ============================================================
# --- Sloan total accruals: level scaled by assets (sign-flipped so high=quality) ---
def f35eq_f35_earnings_quality_accruals_sloan_252d_base_v001_signal(netinc, ncfo, assets):
    acc = _f35_sloan_accrual(netinc, ncfo, assets)
    b = -_mean(acc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sloan accrual z-scored vs its own 252d history (de-trended accrual extremity)
def f35eq_f35_earnings_quality_accruals_sloanz_252d_base_v002_signal(netinc, ncfo, assets):
    acc = _f35_sloan_accrual(netinc, ncfo, assets)
    b = -_z(acc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sloan accrual percentile-ranked vs its own 504d history
def f35eq_f35_earnings_quality_accruals_sloanrank_504d_base_v003_signal(netinc, ncfo, assets):
    acc = _f35_sloan_accrual(netinc, ncfo, assets)
    b = -_rank(acc, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual-ratio trend: slope of Sloan accrual over a year (rising accruals = deteriorating)
def f35eq_f35_earnings_quality_accruals_sloanslope_252d_base_v004_signal(netinc, ncfo, assets):
    acc = _f35_sloan_accrual(netinc, ncfo, assets)
    b = -_slope(acc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual change over a quarter (recent accrual build-up)
def f35eq_f35_earnings_quality_accruals_sloanchg_63d_base_v005_signal(netinc, ncfo, assets):
    acc = _f35_sloan_accrual(netinc, ncfo, assets)
    b = -_chg(_mean(acc, 63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-earnings spread scaled by REVENUE (not assets): cash backing per sales dollar
def f35eq_f35_earnings_quality_accruals_cespread_252d_base_v006_signal(ncfo, netinc, revenue):
    sp = (ncfo - netinc) / revenue.replace(0, np.nan)
    b = _mean(sp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-earnings spread (revenue-scaled) z-scored vs its 126d history
def f35eq_f35_earnings_quality_accruals_cespreadz_252d_base_v007_signal(ncfo, netinc, revenue):
    sp = (ncfo - netinc) / revenue.replace(0, np.nan)
    b = _z(sp, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-margin slope minus net-margin slope (cash backing improving faster than reported)
def f35eq_f35_earnings_quality_accruals_cespreadslope_252d_base_v008_signal(ncfo, netinc, revenue):
    cm = ncfo / revenue.replace(0, np.nan)
    nm = netinc / revenue.replace(0, np.nan)
    b = _slope(cm, 252) - _slope(nm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash conversion ratio (ncfo/netinc) smoothed level
def f35eq_f35_earnings_quality_accruals_cashconv_252d_base_v009_signal(ncfo, netinc):
    cc = _f35_cash_conv(ncfo, netinc)
    b = _mean(cc.clip(-10, 10), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash conversion ratio z-scored (de-trended conversion quality)
def f35eq_f35_earnings_quality_accruals_cashconvz_126d_base_v010_signal(ncfo, netinc):
    cc = _f35_cash_conv(ncfo, netinc).clip(-10, 10)
    b = _z(cc, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# conversion-deficit momentum: change in (ncfo-netinc) flow over half-years (turning point)
def f35eq_f35_earnings_quality_accruals_convdeficit_252d_base_v011_signal(ncfo, netinc):
    flow = ncfo - netinc
    norm = flow / (ncfo.abs() + netinc.abs()).replace(0, np.nan)
    b = _chg(_mean(norm, 21), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ΔWC accruals over a quarter scaled by assets (sign-flipped: rising WC = poor quality)
def f35eq_f35_earnings_quality_accruals_dwc_63d_base_v012_signal(workingcapital, assets):
    b = -_f35_dwc_accrual(workingcapital, assets, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ΔWC accruals over a year scaled by assets
def f35eq_f35_earnings_quality_accruals_dwc_252d_base_v013_signal(workingcapital, assets):
    b = -_f35_dwc_accrual(workingcapital, assets, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ΔWC accrual z-scored vs its 252d history
def f35eq_f35_earnings_quality_accruals_dwcz_252d_base_v014_signal(workingcapital, assets):
    wc = _f35_dwc_accrual(workingcapital, assets, 63)
    b = -_z(wc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital intensity level (WC/assets), z-scored (de-trended bloat)
def f35eq_f35_earnings_quality_accruals_wcint_z_252d_base_v015_signal(workingcapital, assets):
    ar = _f35_accrual_ratio_bs(workingcapital, assets)
    b = -_z(ar, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# balance-sheet accrual ratio trend (slope of WC/assets over a year)
def f35eq_f35_earnings_quality_accruals_wcintslope_252d_base_v016_signal(workingcapital, assets):
    ar = _f35_accrual_ratio_bs(workingcapital, assets)
    b = -_slope(ar, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables intensity (receivables/revenue) level, z-scored (DSO bloat)
def f35eq_f35_earnings_quality_accruals_dso_z_252d_base_v017_signal(receivables, revenue):
    ri = _f35_recv_intensity(receivables, revenue)
    b = -_z(ri, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables intensity slope over a year (rising DSO = aggressive revenue recognition)
def f35eq_f35_earnings_quality_accruals_dsoslope_252d_base_v018_signal(receivables, revenue):
    ri = _f35_recv_intensity(receivables, revenue)
    b = -_slope(ri, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables-growth minus revenue-growth over a quarter (channel-stuffing tell)
def f35eq_f35_earnings_quality_accruals_recvrev_63d_base_v019_signal(receivables, revenue):
    b = -_f35_recv_vs_rev_growth(receivables, revenue, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables-growth minus revenue-growth over a year
def f35eq_f35_earnings_quality_accruals_recvrev_252d_base_v020_signal(receivables, revenue):
    b = -_f35_recv_vs_rev_growth(receivables, revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables/revenue growth spread z-scored vs its 252d history
def f35eq_f35_earnings_quality_accruals_recvrevz_252d_base_v021_signal(receivables, revenue):
    g = _f35_recv_vs_rev_growth(receivables, revenue, 63)
    b = -_z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual reversal: accrual now vs accrual a year ago (mean-reversion of accruals)
def f35eq_f35_earnings_quality_accruals_reversal_252d_base_v022_signal(netinc, ncfo, assets):
    acc = _f35_sloan_accrual(netinc, ncfo, assets)
    am = _mean(acc, 63)
    b = -(am - am.shift(252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual persistence: autocorrelation-like product of consecutive accrual changes
def f35eq_f35_earnings_quality_accruals_persist_252d_base_v023_signal(netinc, ncfo, assets):
    acc = _f35_sloan_accrual(netinc, ncfo, assets)
    d = _chg(acc, 63)
    prod = d * d.shift(63)
    b = -_mean(prod, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual volatility (instability of accruals = low earnings quality)
def f35eq_f35_earnings_quality_accruals_accvol_252d_base_v024_signal(netinc, ncfo, assets):
    acc = _f35_sloan_accrual(netinc, ncfo, assets)
    b = -_std(acc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# earnings smoothness: vol of netinc vs vol of ncfo (managed earnings smoother than cash)
def f35eq_f35_earnings_quality_accruals_smooth_252d_base_v025_signal(netinc, ncfo):
    vni = _std(netinc, 252)
    vcf = _std(ncfo, 252)
    b = vni / vcf.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-flow-to-assets level (ncfo/assets) : clean cash profitability anchor
def f35eq_f35_earnings_quality_accruals_cfoa_252d_base_v026_signal(ncfo, assets):
    cfoa = ncfo / assets.replace(0, np.nan)
    b = _mean(cfoa, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables-based accrual proxy: ΔReceivables as a share of revenue (sales not yet cash)
def f35eq_f35_earnings_quality_accruals_accfrac_252d_base_v027_signal(receivables, revenue):
    drecv = _chg(receivables, 63)
    b = -_mean(drecv / revenue.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables share of assets, z-scored (receivable bloat on the balance sheet)
def f35eq_f35_earnings_quality_accruals_recvassets_z_252d_base_v028_signal(receivables, assets):
    ra = receivables / assets.replace(0, np.nan)
    b = -_z(ra, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-per-asset turnover trend (real productivity behind reported sales)
def f35eq_f35_earnings_quality_accruals_revasset_slope_252d_base_v029_signal(revenue, assets):
    rt = revenue / assets.replace(0, np.nan)
    b = _slope(rt, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual-adjusted earnings: netinc/assets minus accrual penalty (quality-tilted ROA)
def f35eq_f35_earnings_quality_accruals_qroa_252d_base_v030_signal(netinc, ncfo, assets):
    roa = netinc / assets.replace(0, np.nan)
    acc = _f35_sloan_accrual(netinc, ncfo, assets)
    b = _mean(roa - acc.abs(), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-ROA percentile rank vs cross-time (clean cash profitability standing)
def f35eq_f35_earnings_quality_accruals_cashroaspr_252d_base_v031_signal(ncfo, assets):
    croa = ncfo / assets.replace(0, np.nan)
    b = _rank(croa, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign-magnitude of Sloan accrual: bounded penalty emphasizing direction
def f35eq_f35_earnings_quality_accruals_signmag_252d_base_v032_signal(netinc, ncfo, assets):
    acc = _mean(_f35_sloan_accrual(netinc, ncfo, assets), 63)
    b = -np.sign(acc) * (acc.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed accrual change over a quarter (bounded recent accrual swing)
def f35eq_f35_earnings_quality_accruals_acctanh_63d_base_v033_signal(netinc, ncfo, assets):
    acc = _f35_sloan_accrual(netinc, ncfo, assets)
    chg = _chg(acc, 63)
    b = -np.tanh(15.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO percentile rank vs cross-time (relative collection-bloat standing)
def f35eq_f35_earnings_quality_accruals_dsochg_252d_base_v034_signal(receivables, revenue):
    ri = _f35_recv_intensity(receivables, revenue)
    b = -_rank(ri, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# WC accrual hit-rate: fraction of last year ΔWC was positive (chronic WC build)
def f35eq_f35_earnings_quality_accruals_dwchit_252d_base_v035_signal(workingcapital, assets):
    dwc = _chg(workingcapital, 63)
    flag = (dwc > 0).astype(float)
    b = -(flag.rolling(252, min_periods=126).mean() - 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual asymmetry: how negative the accrual is in down vs typical times
def f35eq_f35_earnings_quality_accruals_asym_252d_base_v036_signal(netinc, ncfo, assets):
    acc = _f35_sloan_accrual(netinc, ncfo, assets)
    mn = _mean(acc, 252)
    md = acc.rolling(252, min_periods=126).median()
    b = -(mn - md)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-conversion stability: low dispersion of ncfo/netinc = reliable quality
def f35eq_f35_earnings_quality_accruals_convstab_252d_base_v037_signal(ncfo, netinc):
    cc = _f35_cash_conv(ncfo, netinc).clip(-10, 10)
    b = -_std(cc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables-growth z-score relative to revenue growth, ranked
def f35eq_f35_earnings_quality_accruals_recvrevrank_504d_base_v038_signal(receivables, revenue):
    g = _f35_recv_vs_rev_growth(receivables, revenue, 63)
    b = -_rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual reversal speed: change in accrual minus change a quarter earlier (deceleration)
def f35eq_f35_earnings_quality_accruals_revspeed_63d_base_v039_signal(netinc, ncfo, assets):
    acc = _f35_sloan_accrual(netinc, ncfo, assets)
    d = _chg(acc, 63)
    b = -(d - d.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-backed earnings interaction: cash conversion x sign-aligned revenue growth
def f35eq_f35_earnings_quality_accruals_convroa_252d_base_v040_signal(ncfo, netinc, revenue):
    cc = (ncfo / netinc.replace(0, np.nan)).clip(-5, 5)
    sg = _pctchg(revenue, 252).clip(-2, 2)
    b = _mean((cc - 1.0) * sg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-growth vs WC-accrual interaction (growth funded by accruals = risky)
def f35eq_f35_earnings_quality_accruals_growthwc_252d_base_v041_signal(revenue, workingcapital, assets):
    sg = _pctchg(revenue, 252)
    wc = _f35_dwc_accrual(workingcapital, assets, 252)
    b = -(sg.clip(-2, 2) * wc)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual-volatility rank: where current accrual instability ranks vs its history
def f35eq_f35_earnings_quality_accruals_absrank_504d_base_v042_signal(netinc, ncfo, assets):
    acc = _f35_sloan_accrual(netinc, ncfo, assets)
    vol = _std(acc, 63)
    b = -_rank(vol, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fast-vs-slow accrual EMA crossover (accrual regime shift, momentum of bloat)
def f35eq_f35_earnings_quality_accruals_accema_126d_base_v043_signal(netinc, ncfo, assets):
    acc = _f35_sloan_accrual(netinc, ncfo, assets)
    fast = acc.ewm(span=42, min_periods=21).mean()
    slow = acc.ewm(span=189, min_periods=63).mean()
    b = -(fast - slow)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual displacement: accrual minus its slow EMA (recent accrual surprise)
def f35eq_f35_earnings_quality_accruals_accdisp_252d_base_v044_signal(netinc, ncfo, assets):
    acc = _f35_sloan_accrual(netinc, ncfo, assets)
    b = -(acc - acc.ewm(span=126, min_periods=63).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-earnings spread per unit of accrual volatility (risk-adjusted cash backing)
def f35eq_f35_earnings_quality_accruals_cespreadvol_252d_base_v045_signal(ncfo, netinc, assets):
    sp = _f35_cash_earn_spread(ncfo, netinc, assets)
    acc = _f35_sloan_accrual(netinc, ncfo, assets)
    vol = _std(acc, 252).replace(0, np.nan)
    b = _mean(sp, 63) / vol
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables intensity dispersion across 63/126/252 windows (DSO instability)
def f35eq_f35_earnings_quality_accruals_dsodisp_multi_base_v046_signal(receivables, revenue):
    ri = _f35_recv_intensity(receivables, revenue)
    a = _mean(ri, 63)
    b2 = _mean(ri, 126)
    c = _mean(ri, 252)
    b = -pd.concat([a, b2, c], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# WC accrual short vs long spread (quarterly build vs annual build)
def f35eq_f35_earnings_quality_accruals_dwcspr_63v252_base_v047_signal(workingcapital, assets):
    s = _f35_dwc_accrual(workingcapital, assets, 63)
    l = _f35_dwc_accrual(workingcapital, assets, 252) / 4.0
    b = -(s - l)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# earnings-vs-cash co-movement: rolling corr of netinc and ncfo (aligned = clean)
def f35eq_f35_earnings_quality_accruals_nicfcorr_252d_base_v048_signal(netinc, ncfo):
    dni = netinc.pct_change()
    dcf = ncfo.pct_change()
    b = dni.rolling(252, min_periods=126).corr(dcf)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual quality score: WC-accrual stability (lower instability = higher quality, BS-based)
def f35eq_f35_earnings_quality_accruals_qscore_252d_base_v049_signal(workingcapital, assets):
    dwc = _f35_dwc_accrual(workingcapital, assets, 21)
    instab = _std(dwc, 252)
    b = -_z(instab, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue acceleration vs receivables acceleration (quality of growth)
def f35eq_f35_earnings_quality_accruals_revrecvaccel_252d_base_v050_signal(revenue, receivables):
    rg = _pctchg(revenue, 63)
    rcg = _pctchg(receivables, 63)
    raccel = rg - rg.shift(63)
    rcaccel = rcg - rcg.shift(63)
    b = raccel - rcaccel
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual trend rank: percentile of accrual slope (improving vs worsening quality)
def f35eq_f35_earnings_quality_accruals_slopetrank_504d_base_v051_signal(netinc, ncfo, assets):
    acc = _f35_sloan_accrual(netinc, ncfo, assets)
    sl = _slope(acc, 126)
    b = -_rank(sl, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-flow margin (ncfo/revenue) level (cash generated per sales dollar)
def f35eq_f35_earnings_quality_accruals_cfmargin_252d_base_v052_signal(ncfo, revenue):
    cfm = ncfo / revenue.replace(0, np.nan)
    b = _mean(cfm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-quality ratio level: cash margin divided by net margin, ranked vs history
def f35eq_f35_earnings_quality_accruals_marginspr_252d_base_v053_signal(netinc, ncfo, revenue):
    nm = netinc / revenue.replace(0, np.nan)
    cm = ncfo / revenue.replace(0, np.nan)
    ratio = (cm / nm.replace(0, np.nan)).clip(-10, 10)
    b = _rank(_mean(ratio, 63), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital-to-revenue intensity z-score (WC bloat relative to sales)
def f35eq_f35_earnings_quality_accruals_wcrev_z_252d_base_v054_signal(workingcapital, revenue):
    wr = workingcapital / revenue.replace(0, np.nan)
    b = -_z(wr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual deterioration streak: consecutive quarters of rising accruals (rolling sum)
def f35eq_f35_earnings_quality_accruals_detstreak_252d_base_v055_signal(netinc, ncfo, assets):
    acc = _f35_sloan_accrual(netinc, ncfo, assets)
    rising = (_chg(acc, 21) > 0).astype(float)
    b = -(rising.rolling(252, min_periods=126).mean() - 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables intensity EMA displacement (recent collection surprise)
def f35eq_f35_earnings_quality_accruals_dsodisp_ema_252d_base_v056_signal(receivables, revenue):
    ri = _f35_recv_intensity(receivables, revenue)
    b = -(ri - ri.ewm(span=126, min_periods=63).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-conversion year-over-year change (improving cash backing)
def f35eq_f35_earnings_quality_accruals_convyoy_252d_base_v057_signal(ncfo, netinc):
    cc = _f35_cash_conv(ncfo, netinc).clip(-10, 10)
    ccm = _mean(cc, 63)
    b = ccm - ccm.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-revenue conversion trend: slope of collected-share (improving cash collection)
def f35eq_f35_earnings_quality_accruals_realrevg_252d_base_v058_signal(revenue, receivables):
    collected = revenue - _chg(receivables, 63)
    ratio = collected / revenue.replace(0, np.nan)
    b = _slope(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# WC-accrual revenue-scaled SLOPE (sustained WC-to-sales build, trend not level)
def f35eq_f35_earnings_quality_accruals_dwcrev_z_252d_base_v059_signal(workingcapital, revenue):
    wcr = workingcapital / revenue.replace(0, np.nan)
    b = -_slope(wcr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual reliability: variability of accrual relative to its own mean (coeff of variation)
def f35eq_f35_earnings_quality_accruals_reliab_252d_base_v060_signal(ncfo, netinc, assets):
    acc = _f35_sloan_accrual(netinc, ncfo, assets)
    sd = _std(acc, 252)
    lvl = _mean(acc.abs(), 252).replace(0, np.nan)
    b = -sd / lvl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual momentum normalized by accrual volatility (risk-adjusted accrual build)
def f35eq_f35_earnings_quality_accruals_accmom_126d_base_v061_signal(netinc, ncfo, assets):
    acc = _f35_sloan_accrual(netinc, ncfo, assets)
    e = acc.ewm(span=63, min_periods=21).mean()
    mom = _chg(e, 21)
    vol = _std(acc, 126).replace(0, np.nan)
    b = -mom / vol
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-quality: revenue growth minus receivables-share-of-assets growth
def f35eq_f35_earnings_quality_accruals_revqual_252d_base_v062_signal(revenue, receivables, assets):
    sg = _pctchg(revenue, 252)
    rag = _pctchg(receivables / assets.replace(0, np.nan), 252)
    b = sg - rag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual dispersion across windows (accrual estimate instability)
def f35eq_f35_earnings_quality_accruals_accdisp_multi_base_v063_signal(netinc, ncfo, assets):
    acc = _f35_sloan_accrual(netinc, ncfo, assets)
    a = _mean(acc, 63)
    b2 = _mean(acc, 126)
    c = _mean(acc, 252)
    b = -pd.concat([a, b2, c], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash conversion rank vs cross-time (relative cash backing strength)
def f35eq_f35_earnings_quality_accruals_convrank_504d_base_v064_signal(ncfo, netinc):
    cc = _f35_cash_conv(ncfo, netinc).clip(-10, 10)
    b = _rank(cc, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DSO acceleration (second-order receivables intensity build over half-years)
def f35eq_f35_earnings_quality_accruals_dsoaccel_252d_base_v065_signal(receivables, revenue):
    ri = _f35_recv_intensity(receivables, revenue)
    d = _chg(_mean(ri, 21), 126)
    b = -(d - d.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# earnings-vs-cash growth divergence: netinc growth minus ncfo growth (warning if >0)
def f35eq_f35_earnings_quality_accruals_nicfdiverge_252d_base_v066_signal(netinc, ncfo):
    nig = _pctchg(netinc, 252)
    cfg = _pctchg(ncfo, 252)
    b = -(nig - cfg).clip(-5, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per receivable trend (collection efficiency improvement)
def f35eq_f35_earnings_quality_accruals_revperrecv_slope_252d_base_v067_signal(revenue, receivables):
    rpr = revenue / receivables.replace(0, np.nan)
    b = _slope(rpr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual-quality composite: cash-margin trend minus WC-intensity trend (improving quality)
def f35eq_f35_earnings_quality_accruals_composite_252d_base_v068_signal(ncfo, revenue, workingcapital, assets):
    cm = ncfo / revenue.replace(0, np.nan)
    wi = workingcapital / assets.replace(0, np.nan)
    b = _slope(cm, 252) - _slope(wi, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual reversal-of-reversal: did a prior accrual spike unwind? (sign change rate)
def f35eq_f35_earnings_quality_accruals_unwind_252d_base_v069_signal(netinc, ncfo, assets):
    acc = _f35_sloan_accrual(netinc, ncfo, assets)
    d = _chg(acc, 21)
    signflip = ((np.sign(d) != np.sign(d.shift(21))) & (d.shift(21) != 0)).astype(float)
    b = signflip.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-earnings spread momentum z (accelerating cash backing)
def f35eq_f35_earnings_quality_accruals_cespreadmom_252d_base_v070_signal(ncfo, netinc, assets):
    sp = _f35_cash_earn_spread(ncfo, netinc, assets)
    mom = _chg(_mean(sp, 63), 63)
    b = _z(mom, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables-revenue growth gap streak (chronic divergence)
def f35eq_f35_earnings_quality_accruals_rrgapstreak_252d_base_v071_signal(receivables, revenue):
    g = _f35_recv_vs_rev_growth(receivables, revenue, 63)
    bad = (g > 0).astype(float)
    b = -(bad.rolling(252, min_periods=126).mean() - 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual-to-cashflow ratio TREND: slope of accrual/|ncfo| over a year (deteriorating mix)
def f35eq_f35_earnings_quality_accruals_acccfratio_252d_base_v072_signal(netinc, ncfo):
    acc = netinc - ncfo
    ratio = (acc / ncfo.abs().replace(0, np.nan)).clip(-10, 10)
    b = -_slope(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# WC intensity rank vs cross-time (relative balance-sheet bloat)
def f35eq_f35_earnings_quality_accruals_wcintrank_504d_base_v073_signal(workingcapital, assets):
    ar = _f35_accrual_ratio_bs(workingcapital, assets)
    b = -_rank(ar, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# earnings persistence vs cash persistence (managed-earnings smoothness gap)
def f35eq_f35_earnings_quality_accruals_persistgap_252d_base_v074_signal(netinc, ncfo):
    ni_ac = netinc.pct_change().rolling(252, min_periods=126).apply(
        lambda a: float(pd.Series(a).autocorr(lag=21)) if len(a) > 25 else np.nan, raw=False)
    cf_ac = ncfo.pct_change().rolling(252, min_periods=126).apply(
        lambda a: float(pd.Series(a).autocorr(lag=21)) if len(a) > 25 else np.nan, raw=False)
    b = ni_ac - cf_ac
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# clean-revenue quality: cash-conversion level penalized by receivable-growth excess
def f35eq_f35_earnings_quality_accruals_cleanrev_252d_base_v075_signal(ncfo, netinc, receivables, revenue):
    cc = (ncfo / netinc.replace(0, np.nan)).clip(-5, 5)
    rrg = _f35_recv_vs_rev_growth(receivables, revenue, 63)
    b = _mean(cc, 252) - 3.0 * _mean(rrg, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f35eq_f35_earnings_quality_accruals_sloan_252d_base_v001_signal,
    f35eq_f35_earnings_quality_accruals_sloanz_252d_base_v002_signal,
    f35eq_f35_earnings_quality_accruals_sloanrank_504d_base_v003_signal,
    f35eq_f35_earnings_quality_accruals_sloanslope_252d_base_v004_signal,
    f35eq_f35_earnings_quality_accruals_sloanchg_63d_base_v005_signal,
    f35eq_f35_earnings_quality_accruals_cespread_252d_base_v006_signal,
    f35eq_f35_earnings_quality_accruals_cespreadz_252d_base_v007_signal,
    f35eq_f35_earnings_quality_accruals_cespreadslope_252d_base_v008_signal,
    f35eq_f35_earnings_quality_accruals_cashconv_252d_base_v009_signal,
    f35eq_f35_earnings_quality_accruals_cashconvz_126d_base_v010_signal,
    f35eq_f35_earnings_quality_accruals_convdeficit_252d_base_v011_signal,
    f35eq_f35_earnings_quality_accruals_dwc_63d_base_v012_signal,
    f35eq_f35_earnings_quality_accruals_dwc_252d_base_v013_signal,
    f35eq_f35_earnings_quality_accruals_dwcz_252d_base_v014_signal,
    f35eq_f35_earnings_quality_accruals_wcint_z_252d_base_v015_signal,
    f35eq_f35_earnings_quality_accruals_wcintslope_252d_base_v016_signal,
    f35eq_f35_earnings_quality_accruals_dso_z_252d_base_v017_signal,
    f35eq_f35_earnings_quality_accruals_dsoslope_252d_base_v018_signal,
    f35eq_f35_earnings_quality_accruals_recvrev_63d_base_v019_signal,
    f35eq_f35_earnings_quality_accruals_recvrev_252d_base_v020_signal,
    f35eq_f35_earnings_quality_accruals_recvrevz_252d_base_v021_signal,
    f35eq_f35_earnings_quality_accruals_reversal_252d_base_v022_signal,
    f35eq_f35_earnings_quality_accruals_persist_252d_base_v023_signal,
    f35eq_f35_earnings_quality_accruals_accvol_252d_base_v024_signal,
    f35eq_f35_earnings_quality_accruals_smooth_252d_base_v025_signal,
    f35eq_f35_earnings_quality_accruals_cfoa_252d_base_v026_signal,
    f35eq_f35_earnings_quality_accruals_accfrac_252d_base_v027_signal,
    f35eq_f35_earnings_quality_accruals_recvassets_z_252d_base_v028_signal,
    f35eq_f35_earnings_quality_accruals_revasset_slope_252d_base_v029_signal,
    f35eq_f35_earnings_quality_accruals_qroa_252d_base_v030_signal,
    f35eq_f35_earnings_quality_accruals_cashroaspr_252d_base_v031_signal,
    f35eq_f35_earnings_quality_accruals_signmag_252d_base_v032_signal,
    f35eq_f35_earnings_quality_accruals_acctanh_63d_base_v033_signal,
    f35eq_f35_earnings_quality_accruals_dsochg_252d_base_v034_signal,
    f35eq_f35_earnings_quality_accruals_dwchit_252d_base_v035_signal,
    f35eq_f35_earnings_quality_accruals_asym_252d_base_v036_signal,
    f35eq_f35_earnings_quality_accruals_convstab_252d_base_v037_signal,
    f35eq_f35_earnings_quality_accruals_recvrevrank_504d_base_v038_signal,
    f35eq_f35_earnings_quality_accruals_revspeed_63d_base_v039_signal,
    f35eq_f35_earnings_quality_accruals_convroa_252d_base_v040_signal,
    f35eq_f35_earnings_quality_accruals_growthwc_252d_base_v041_signal,
    f35eq_f35_earnings_quality_accruals_absrank_504d_base_v042_signal,
    f35eq_f35_earnings_quality_accruals_accema_126d_base_v043_signal,
    f35eq_f35_earnings_quality_accruals_accdisp_252d_base_v044_signal,
    f35eq_f35_earnings_quality_accruals_cespreadvol_252d_base_v045_signal,
    f35eq_f35_earnings_quality_accruals_dsodisp_multi_base_v046_signal,
    f35eq_f35_earnings_quality_accruals_dwcspr_63v252_base_v047_signal,
    f35eq_f35_earnings_quality_accruals_nicfcorr_252d_base_v048_signal,
    f35eq_f35_earnings_quality_accruals_qscore_252d_base_v049_signal,
    f35eq_f35_earnings_quality_accruals_revrecvaccel_252d_base_v050_signal,
    f35eq_f35_earnings_quality_accruals_slopetrank_504d_base_v051_signal,
    f35eq_f35_earnings_quality_accruals_cfmargin_252d_base_v052_signal,
    f35eq_f35_earnings_quality_accruals_marginspr_252d_base_v053_signal,
    f35eq_f35_earnings_quality_accruals_wcrev_z_252d_base_v054_signal,
    f35eq_f35_earnings_quality_accruals_detstreak_252d_base_v055_signal,
    f35eq_f35_earnings_quality_accruals_dsodisp_ema_252d_base_v056_signal,
    f35eq_f35_earnings_quality_accruals_convyoy_252d_base_v057_signal,
    f35eq_f35_earnings_quality_accruals_realrevg_252d_base_v058_signal,
    f35eq_f35_earnings_quality_accruals_dwcrev_z_252d_base_v059_signal,
    f35eq_f35_earnings_quality_accruals_reliab_252d_base_v060_signal,
    f35eq_f35_earnings_quality_accruals_accmom_126d_base_v061_signal,
    f35eq_f35_earnings_quality_accruals_revqual_252d_base_v062_signal,
    f35eq_f35_earnings_quality_accruals_accdisp_multi_base_v063_signal,
    f35eq_f35_earnings_quality_accruals_convrank_504d_base_v064_signal,
    f35eq_f35_earnings_quality_accruals_dsoaccel_252d_base_v065_signal,
    f35eq_f35_earnings_quality_accruals_nicfdiverge_252d_base_v066_signal,
    f35eq_f35_earnings_quality_accruals_revperrecv_slope_252d_base_v067_signal,
    f35eq_f35_earnings_quality_accruals_composite_252d_base_v068_signal,
    f35eq_f35_earnings_quality_accruals_unwind_252d_base_v069_signal,
    f35eq_f35_earnings_quality_accruals_cespreadmom_252d_base_v070_signal,
    f35eq_f35_earnings_quality_accruals_rrgapstreak_252d_base_v071_signal,
    f35eq_f35_earnings_quality_accruals_acccfratio_252d_base_v072_signal,
    f35eq_f35_earnings_quality_accruals_wcintrank_504d_base_v073_signal,
    f35eq_f35_earnings_quality_accruals_persistgap_252d_base_v074_signal,
    f35eq_f35_earnings_quality_accruals_cleanrev_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F35_EARNINGS_QUALITY_ACCRUALS_REGISTRY_001_075 = REGISTRY


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

    print("OK f35_earnings_quality_accruals_base_001_075_claude: %d features pass" % n_features)
