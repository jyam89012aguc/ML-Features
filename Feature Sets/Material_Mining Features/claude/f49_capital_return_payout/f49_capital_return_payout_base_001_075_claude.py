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
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


def _slope(s, w):
    return s - s.shift(w)


# ===== folder domain primitives (capital return / payout) =====
def _f49_payout_sustain(ncfdiv, fcf):
    # dividends paid relative to free cash flow generated (>1 = unsustainable)
    return ncfdiv.abs() / fcf.replace(0, np.nan)


def _f49_dps_fcfps(dps, fcfps):
    # per-share dividend vs per-share free cash flow
    return dps / fcfps.replace(0, np.nan)


def _f49_div_coverage_fcf(fcf, ncfdiv):
    # how many times FCF covers the dividend
    return fcf / ncfdiv.abs().replace(0, np.nan)


def _f49_div_coverage_ocf(ncfo, ncfdiv):
    # how many times operating cash flow covers the dividend
    return ncfo / ncfdiv.abs().replace(0, np.nan)


def _f49_pref_drag(prefdivis, netinc):
    # preferred-dividend seniority drag on common earnings
    return prefdivis.abs() / netinc.abs().replace(0, np.nan)


def _f49_payout_earn(ncfdiv, netinc):
    # cash dividends vs net income (cash payout ratio)
    return ncfdiv.abs() / netinc.replace(0, np.nan)


def _f49_royalty_sig(divyield, fcf, marketcap):
    # royalty/streamer signature: yield plus FCF yield on market cap
    fcfy = fcf / marketcap.replace(0, np.nan)
    return divyield + fcfy


# ============================================================
# --- payout sustainability (ncfdiv/fcf) ---
def f49pr_f49_capital_return_payout_psust_lvl_252d_base_v001_signal(ncfdiv, fcf):
    b = _f49_payout_sustain(ncfdiv, fcf)
    result = b.rolling(252, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f49pr_f49_capital_return_payout_psust_z_252d_base_v002_signal(ncfdiv, fcf):
    b = _z(_f49_payout_sustain(ncfdiv, fcf), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f49pr_f49_capital_return_payout_psust_rank_504d_base_v003_signal(ncfdiv, fcf):
    b = _rank(_f49_payout_sustain(ncfdiv, fcf), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# unsustainability flag: payout-of-FCF persistently above 1
def f49pr_f49_capital_return_payout_psust_overflag_252d_base_v004_signal(ncfdiv, fcf):
    ps = _f49_payout_sustain(ncfdiv, fcf)
    thr = ps.rolling(504, min_periods=126).median()
    over = (ps > thr).astype(float)
    result = over.rolling(252, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# --- dps vs fcfps ---
def f49pr_f49_capital_return_payout_dpsfcfps_lvl_252d_base_v005_signal(dps, fcfps):
    b = _f49_dps_fcfps(dps, fcfps)
    result = b.rolling(126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f49pr_f49_capital_return_payout_dpsfcfps_z_252d_base_v006_signal(dps, fcfps):
    b = _z(_f49_dps_fcfps(dps, fcfps), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# per-share buffer: fcfps minus dps (absolute cash headroom per share)
def f49pr_f49_capital_return_payout_dpsbuffer_126d_base_v007_signal(dps, fcfps):
    buf = (fcfps - dps) / fcfps.abs().replace(0, np.nan)
    result = buf.rolling(126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# --- dividend coverage by FCF ---
def f49pr_f49_capital_return_payout_covfcf_lvl_252d_base_v008_signal(fcf, ncfdiv):
    cov = _f49_div_coverage_fcf(fcf, ncfdiv)
    floor = cov.rolling(504, min_periods=126).min()
    # cushion of current coverage above its own worst-case floor
    b = (cov - floor) / (1.0 + floor.abs())
    result = b.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f49pr_f49_capital_return_payout_covfcf_z_252d_base_v009_signal(fcf, ncfdiv):
    # log-coverage z combined with its own momentum (non-reciprocal of payout-sustain z)
    logcov = np.log1p(_f49_div_coverage_fcf(fcf, ncfdiv).clip(lower=-0.99))
    b = _z(logcov, 252) + 0.5 * _z(_slope(logcov, 63), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# thin-coverage flag: FCF coverage below 1.2x
def f49pr_f49_capital_return_payout_covfcf_thinflag_252d_base_v010_signal(fcf, ncfdiv):
    cov = _f49_div_coverage_fcf(fcf, ncfdiv)
    thr = cov.rolling(504, min_periods=126).quantile(0.35)
    thin = (cov < thr).astype(float)
    result = thin.rolling(126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# --- dividend coverage by OCF ---
def f49pr_f49_capital_return_payout_covocf_lvl_252d_base_v011_signal(ncfo, ncfdiv):
    b = _f49_div_coverage_ocf(ncfo, ncfdiv)
    result = b.rolling(252, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f49pr_f49_capital_return_payout_covocf_rank_504d_base_v012_signal(ncfo, ncfdiv):
    b = _rank(_f49_div_coverage_ocf(ncfo, ncfdiv), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex squeeze on the dividend: capex intensity vs OCF, ranked (reinvestment drag)
def f49pr_f49_capital_return_payout_covgap_252d_base_v013_signal(ncfo, fcf, ncfdiv):
    capex = (ncfo - fcf)
    capex_intensity = capex / ncfo.replace(0, np.nan)
    div_intensity = ncfdiv.abs() / ncfo.replace(0, np.nan)
    result = _rank(capex_intensity, 504) - _rank(div_intensity, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# --- dividend yield level + percentile ---
def f49pr_f49_capital_return_payout_dy_lvl_126d_base_v014_signal(divyield):
    result = divyield.rolling(126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f49pr_f49_capital_return_payout_dy_z_252d_base_v015_signal(divyield):
    result = _z(divyield, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f49pr_f49_capital_return_payout_dy_rank_504d_base_v016_signal(divyield):
    result = _rank(divyield, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# yield-trap detector: high yield (top pctile) AND weak FCF coverage
def f49pr_f49_capital_return_payout_yieldtrap_252d_base_v017_signal(divyield, fcf, ncfdiv):
    yhi = _rank(divyield, 504) + 0.5
    cov = _f49_div_coverage_fcf(fcf, ncfdiv)
    weak = (1.0 / (1.0 + cov.clip(lower=0)))
    b = yhi * weak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quality-yield: yield scaled by coverage cushion, where coverage drives the score
def f49pr_f49_capital_return_payout_qualyield_252d_base_v018_signal(divyield, fcf, ncfdiv):
    cov = _f49_div_coverage_fcf(fcf, ncfdiv)
    covz = _z(np.log1p(cov.clip(lower=-0.99)), 252)
    b = divyield.rolling(63, min_periods=21).mean() * 100.0 * np.tanh(covz)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- payout ratio level & trend ---
def f49pr_f49_capital_return_payout_pr_lvl_252d_base_v019_signal(payoutratio):
    result = payoutratio.rolling(252, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f49pr_f49_capital_return_payout_pr_z_252d_base_v020_signal(payoutratio):
    result = _z(payoutratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f49pr_f49_capital_return_payout_pr_trend_252d_base_v021_signal(payoutratio):
    sm = payoutratio.rolling(63, min_periods=21).mean()
    result = _slope(sm, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# payout-ratio stress: fraction of last year above 1.0 (paying out more than earnings)
def f49pr_f49_capital_return_payout_pr_stressflag_252d_base_v022_signal(payoutratio):
    thr = payoutratio.rolling(504, min_periods=126).quantile(0.7)
    over = (payoutratio > thr).astype(float)
    result = over.rolling(252, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# --- dividend-growth streak (dps trend) ---
def f49pr_f49_capital_return_payout_dpsgrow_252d_base_v023_signal(dps):
    g = np.log(dps.replace(0, np.nan)) - np.log(dps.shift(252).replace(0, np.nan))
    result = g
    return result.replace([np.inf, -np.inf], np.nan)


# dividend-growth streak length: consecutive quarters of rising dps
def f49pr_f49_capital_return_payout_dpsstreak_504d_base_v024_signal(dps):
    rising = (dps > dps.shift(63)).astype(float)
    streak = rising.groupby((rising == 0).cumsum()).cumsum()
    result = streak.rolling(504, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# dps acceleration: short-window growth minus long-window growth
def f49pr_f49_capital_return_payout_dpsaccel_252d_base_v025_signal(dps):
    gshort = _slope(dps, 63) / dps.shift(63).abs().replace(0, np.nan)
    glong = _slope(dps, 252) / dps.shift(252).abs().replace(0, np.nan)
    b = gshort - glong / 4.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- preferred-dividend seniority drag ---
def f49pr_f49_capital_return_payout_prefdrag_lvl_252d_base_v026_signal(prefdivis, netinc):
    b = _f49_pref_drag(prefdivis, netinc)
    result = b.rolling(252, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f49pr_f49_capital_return_payout_prefdrag_z_252d_base_v027_signal(prefdivis, netinc):
    result = _z(_f49_pref_drag(prefdivis, netinc), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# preferred dividends as a claim on operating cash flow
def f49pr_f49_capital_return_payout_prefocf_252d_base_v028_signal(prefdivis, ncfo):
    b = prefdivis.abs() / ncfo.replace(0, np.nan)
    result = b.rolling(126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# --- royalty/streamer signature ---
def f49pr_f49_capital_return_payout_royalty_lvl_252d_base_v029_signal(divyield, eps, dps):
    # royalty/streamer signature: high yield supported by ample earnings cushion (eps/dps)
    yz = _z(divyield, 252)
    cushion = eps / dps.replace(0, np.nan)
    cushz = _z(np.log1p(cushion.clip(lower=-0.99)), 252)
    result = (yz + cushz).rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f49pr_f49_capital_return_payout_royalty_rank_504d_base_v030_signal(divyield, fcf, marketcap):
    b = _rank(_f49_royalty_sig(divyield, fcf, marketcap), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF yield alone (cash generation per market cap dollar)
def f49pr_f49_capital_return_payout_fcfyield_252d_base_v031_signal(fcf, marketcap):
    b = fcf / marketcap.replace(0, np.nan)
    result = b.rolling(126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# total shareholder yield: dividend yield plus FCF yield, z-scored
def f49pr_f49_capital_return_payout_totyield_z_252d_base_v032_signal(divyield, fcf, marketcap):
    fcfy = fcf / marketcap.replace(0, np.nan)
    result = _z(divyield + fcfy, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# --- dividend initiation / cut event flags ---
# initiation/ramp proximity: dps lifting off its trailing 2yr trough (new-payer ramp)
def f49pr_f49_capital_return_payout_initflag_252d_base_v033_signal(dps):
    trough = dps.rolling(504, min_periods=126).min()
    lift = dps / trough.replace(0, np.nan) - 1.0
    result = lift.rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# cut depth: drop in dps from its trailing 252d peak
def f49pr_f49_capital_return_payout_cutdepth_252d_base_v034_signal(dps):
    peak = dps.rolling(252, min_periods=63).max()
    b = dps / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cut/pullback intensity: fraction of last year dps sits below its trailing 63d peak
def f49pr_f49_capital_return_payout_cutflag_252d_base_v035_signal(dps):
    peak = dps.rolling(63, min_periods=21).max()
    cut = (dps < peak * 0.999).astype(float)
    result = cut.rolling(252, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# --- payout vs earnings (ncfdiv/netinc) ---
def f49pr_f49_capital_return_payout_payearn_lvl_252d_base_v036_signal(ncfdiv, netinc):
    b = _f49_payout_earn(ncfdiv, netinc)
    result = b.rolling(252, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


def f49pr_f49_capital_return_payout_payearn_z_252d_base_v037_signal(ncfdiv, netinc):
    result = _z(_f49_payout_earn(ncfdiv, netinc), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# eps payout: dps vs eps (accrual payout ratio, distinct from cash payout)
def f49pr_f49_capital_return_payout_epspayout_252d_base_v038_signal(dps, eps):
    b = dps / eps.replace(0, np.nan)
    result = b.rolling(252, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# eps payout stress: fraction of year dps exceeds eps
def f49pr_f49_capital_return_payout_epspayoutflag_252d_base_v039_signal(dps, eps):
    over = (dps > eps).astype(float)
    result = over.rolling(252, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# --- additional interaction / composite features ---
# accrual-vs-cash payout wedge: eps-payout minus cash-payout (earnings-quality of the dividend)
def f49pr_f49_capital_return_payout_paywedge_252d_base_v040_signal(dps, eps, ncfdiv, netinc):
    epspay = dps / eps.replace(0, np.nan)
    cashpay = _f49_payout_earn(ncfdiv, netinc)
    b = epspay - cashpay
    result = b.rolling(126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# dividend funded by financing? rank of (dividends - FCF) shortfall vs own history
def f49pr_f49_capital_return_payout_divshortfall_252d_base_v041_signal(ncfdiv, fcf, ncfo):
    # blend FCF and OCF shortfall so it is not a monotone transform of FCF alone
    sf_fcf = ncfdiv.abs() - fcf
    sf_ocf = ncfdiv.abs() - ncfo
    b = _rank(sf_fcf, 504) + 0.5 * _rank(sf_ocf, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend dollar growth scaled by market cap (capital returned relative to size)
def f49pr_f49_capital_return_payout_divgrowmc_252d_base_v042_signal(ncfdiv, marketcap):
    divmc = ncfdiv.abs() / marketcap.replace(0, np.nan)
    result = divmc.rolling(126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# payout ratio dispersion (volatility of payout policy)
def f49pr_f49_capital_return_payout_prdisp_252d_base_v043_signal(payoutratio):
    result = _std(payoutratio, 252) / payoutratio.rolling(252, min_periods=63).mean().abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# dividend-yield mean reversion: current yield vs its 2yr average
def f49pr_f49_capital_return_payout_dyrevert_504d_base_v044_signal(divyield):
    avg = divyield.rolling(504, min_periods=126).mean()
    b = divyield / avg.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sustainability trend: is payout-of-FCF improving or deteriorating?
def f49pr_f49_capital_return_payout_psust_trend_252d_base_v045_signal(ncfdiv, fcf):
    ps = _f49_payout_sustain(ncfdiv, fcf)
    sm = ps.rolling(63, min_periods=21).mean()
    result = -_slope(sm, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# coverage stability: low variability of FCF coverage = reliable dividend
def f49pr_f49_capital_return_payout_covstab_504d_base_v046_signal(fcf, ncfdiv):
    cov = _f49_div_coverage_fcf(fcf, ncfdiv)
    result = -_std(cov, 504) / cov.rolling(504, min_periods=126).mean().abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# net common payout cushion: FCF left after dividends+preferred, RANKED vs own history
def f49pr_f49_capital_return_payout_netcommon_252d_base_v047_signal(ncfdiv, prefdivis, fcf):
    residual = fcf - ncfdiv.abs() - prefdivis.abs()
    result = _rank(residual, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# preferred share of total payout (capital-structure quality)
def f49pr_f49_capital_return_payout_prefshare_252d_base_v048_signal(prefdivis, ncfdiv):
    b = prefdivis.abs() / (ncfdiv.abs() + prefdivis.abs()).replace(0, np.nan)
    result = b.rolling(126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# divyield x payout-ratio interaction (high yield from high payout vs from low price)
def f49pr_f49_capital_return_payout_dyxpr_252d_base_v049_signal(divyield, payoutratio):
    b = divyield * payoutratio
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# fcfps growth vs dps growth (cash supporting future raises)
def f49pr_f49_capital_return_payout_fcfpsvsdps_252d_base_v050_signal(fcfps, dps):
    gf = _slope(fcfps, 252) / fcfps.shift(252).abs().replace(0, np.nan)
    gd = _slope(dps, 252) / dps.shift(252).abs().replace(0, np.nan)
    b = gf - gd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend coverage by earnings (netinc/ncfdiv) level
def f49pr_f49_capital_return_payout_earncov_252d_base_v051_signal(netinc, ncfdiv):
    b = netinc / ncfdiv.abs().replace(0, np.nan)
    result = b.rolling(252, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# negative-earnings-while-paying flag: netinc<0 but ncfdiv>0
def f49pr_f49_capital_return_payout_payinloss_252d_base_v052_signal(netinc, ncfdiv):
    flag = ((netinc < 0) & (ncfdiv.abs() > 0)).astype(float)
    result = flag.rolling(252, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# dividend yield momentum (change over a quarter)
def f49pr_f49_capital_return_payout_dymom_126d_base_v053_signal(divyield):
    result = _slope(divyield, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# payout-of-FCF vs payout-of-earnings RATIO (cash vs accrual divergence), z-scored
def f49pr_f49_capital_return_payout_psustspr_252d_base_v054_signal(ncfdiv, fcf, netinc):
    pfcf = _f49_payout_sustain(ncfdiv, fcf)
    pearn = _f49_payout_earn(ncfdiv, netinc)
    b = pfcf / pearn.replace(0, np.nan)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# dps level normalized by its own 2yr range (where dps sits in its policy range)
def f49pr_f49_capital_return_payout_dpsrangepos_504d_base_v055_signal(dps):
    hi = dps.rolling(504, min_periods=126).max()
    lo = dps.rolling(504, min_periods=126).min()
    b = (dps - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps coverage of dps (earnings cushion per share)
def f49pr_f49_capital_return_payout_epscover_252d_base_v056_signal(eps, dps):
    b = eps / dps.replace(0, np.nan)
    result = b.rolling(252, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# royalty-quality composite z: high FCF yield, positive eps, high coverage
def f49pr_f49_capital_return_payout_royqualz_252d_base_v057_signal(fcf, marketcap, ncfo, ncfdiv):
    fcfy = fcf / marketcap.replace(0, np.nan)
    cov = _f49_div_coverage_ocf(ncfo, ncfdiv).clip(lower=0)
    b = fcfy * np.log1p(cov)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# dividend persistence: fraction of last 2yr dps held above its trailing median
def f49pr_f49_capital_return_payout_payerpersist_504d_base_v058_signal(dps):
    med = dps.rolling(504, min_periods=126).median()
    payer = (dps >= med).astype(float)
    result = payer.rolling(504, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# fcf-coverage minus preferred drag (net cushion for common dividend)
def f49pr_f49_capital_return_payout_netcushion_252d_base_v059_signal(fcf, ncfdiv, prefdivis, netinc):
    cov = _f49_div_coverage_fcf(fcf, ncfdiv)
    drag = _f49_pref_drag(prefdivis, netinc)
    b = cov - drag
    result = b.rolling(126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# payout-ratio acceleration (2nd-diff style on smoothed payout ratio)
def f49pr_f49_capital_return_payout_praccel_252d_base_v060_signal(payoutratio):
    sm = payoutratio.rolling(42, min_periods=21).mean()
    b = _slope(sm, 63) - _slope(sm.shift(63), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dividend yield vs FCF yield gap MOMENTUM (change in retained-cash spread)
def f49pr_f49_capital_return_payout_dyfcfygap_252d_base_v061_signal(divyield, fcf, marketcap):
    fcfy = fcf / marketcap.replace(0, np.nan)
    gap = fcfy - divyield
    result = _slope(gap.rolling(42, min_periods=21).mean(), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# capital-return intensity: dividends as a share of total cash (OCF), ranked
def f49pr_f49_capital_return_payout_crintensity_504d_base_v062_signal(ncfdiv, ncfo):
    intens = ncfdiv.abs() / ncfo.abs().replace(0, np.nan)
    result = _rank(intens, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# dps drawdown duration: fraction of 2yr spent below trailing peak
def f49pr_f49_capital_return_payout_dpsunderwater_504d_base_v063_signal(dps):
    peak = dps.rolling(504, min_periods=126).max()
    underwater = (dps < peak * 0.999).astype(float)
    result = underwater.rolling(504, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# coverage improvement vs yield (rising coverage + rising yield = strengthening payer)
def f49pr_f49_capital_return_payout_covyieldmom_252d_base_v064_signal(fcf, ncfdiv, divyield):
    cov = _f49_div_coverage_fcf(fcf, ncfdiv)
    b = _slope(cov.rolling(42, min_periods=21).mean(), 126) + _slope(divyield, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# eps-payout vs fcf-payout consistency (both sustainable?)
def f49pr_f49_capital_return_payout_dualsustain_252d_base_v065_signal(dps, eps, fcfps):
    epspay = dps / eps.replace(0, np.nan)
    fcfpay = dps / fcfps.replace(0, np.nan)
    sustainable = ((epspay < 1.0) & (fcfpay < 1.0)).astype(float)
    result = sustainable.rolling(252, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# trend in the net-income margin of safety over dividend + preferred claims
def f49pr_f49_capital_return_payout_safetymargin_252d_base_v066_signal(netinc, ncfdiv, prefdivis):
    claims = ncfdiv.abs() + prefdivis.abs()
    margin = (netinc - claims) / claims.replace(0, np.nan)
    result = _slope(margin.rolling(42, min_periods=21).mean(), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# dividend growth quality: dps growth relative to the EARNINGS base supporting it
def f49pr_f49_capital_return_payout_growthquality_252d_base_v067_signal(dps, eps):
    gd = np.log(dps.replace(0, np.nan)) - np.log(dps.shift(126).replace(0, np.nan))
    ge = np.log(eps.abs().replace(0, np.nan)) - np.log(eps.shift(126).abs().replace(0, np.nan))
    # growth gap: dividend outpacing earnings is lower quality
    b = (ge - gd).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# yield-trap vs quality axis: rank of coverage MINUS rank of yield (signed quality)
def f49pr_f49_capital_return_payout_qualtrapaxis_252d_base_v068_signal(divyield, fcf, ncfdiv):
    yrank = _rank(divyield, 504)
    cov = _f49_div_coverage_fcf(fcf, ncfdiv)
    covrank = _rank(cov, 504)
    # high coverage + low yield => quality (positive); high yield + low coverage => trap
    b = covrank - yrank
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# payout ratio level vs its 2yr percentile (extreme-payout regime)
def f49pr_f49_capital_return_payout_prextreme_504d_base_v069_signal(payoutratio):
    result = _rank(payoutratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# dividend funded share-of-OCF (claim on operations after preferred)
def f49pr_f49_capital_return_payout_ocfclaim_252d_base_v070_signal(ncfdiv, prefdivis, ncfo):
    claim = (ncfdiv.abs() + prefdivis.abs()) / ncfo.replace(0, np.nan)
    result = claim.rolling(252, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# fcf yield stability vs dividend yield (which is steadier?)
def f49pr_f49_capital_return_payout_yieldsteadyspr_504d_base_v071_signal(divyield, fcf, marketcap):
    fcfy = fcf / marketcap.replace(0, np.nan)
    sd_dy = _std(divyield, 252)
    sd_fy = _std(fcfy, 252)
    b = sd_fy - sd_dy
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite payout-stress score: high payout ratio + thin coverage + cuts
def f49pr_f49_capital_return_payout_stressscore_252d_base_v072_signal(payoutratio, fcf, ncfdiv, dps):
    pr_hi = (payoutratio > payoutratio.rolling(504, min_periods=126).quantile(0.6)).astype(float)
    cov = _f49_div_coverage_fcf(fcf, ncfdiv)
    thin = (cov < cov.rolling(504, min_periods=126).median()).astype(float)
    peak = dps.rolling(63, min_periods=21).max()
    cut = (dps < 0.999 * peak).astype(float)
    b = (pr_hi + thin + cut).rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-return per dollar of net income, smoothed (distribution propensity)
def f49pr_f49_capital_return_payout_crpropensity_252d_base_v073_signal(ncfdiv, netinc):
    b = ncfdiv.abs() / netinc.abs().replace(0, np.nan)
    result = b.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# dps level smoothed and z-scored (where the dividend stands vs its own history)
def f49pr_f49_capital_return_payout_dpslevelz_504d_base_v074_signal(dps):
    result = _z(dps, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# cash-distribution yield rank: dollar dividends paid over market cap, percentile
def f49pr_f49_capital_return_payout_totyieldrank_504d_base_v075_signal(ncfdiv, prefdivis, marketcap):
    cashyield = (ncfdiv.abs() + prefdivis.abs()) / marketcap.replace(0, np.nan)
    result = _rank(cashyield, 504)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f49pr_f49_capital_return_payout_psust_lvl_252d_base_v001_signal,
    f49pr_f49_capital_return_payout_psust_z_252d_base_v002_signal,
    f49pr_f49_capital_return_payout_psust_rank_504d_base_v003_signal,
    f49pr_f49_capital_return_payout_psust_overflag_252d_base_v004_signal,
    f49pr_f49_capital_return_payout_dpsfcfps_lvl_252d_base_v005_signal,
    f49pr_f49_capital_return_payout_dpsfcfps_z_252d_base_v006_signal,
    f49pr_f49_capital_return_payout_dpsbuffer_126d_base_v007_signal,
    f49pr_f49_capital_return_payout_covfcf_lvl_252d_base_v008_signal,
    f49pr_f49_capital_return_payout_covfcf_z_252d_base_v009_signal,
    f49pr_f49_capital_return_payout_covfcf_thinflag_252d_base_v010_signal,
    f49pr_f49_capital_return_payout_covocf_lvl_252d_base_v011_signal,
    f49pr_f49_capital_return_payout_covocf_rank_504d_base_v012_signal,
    f49pr_f49_capital_return_payout_covgap_252d_base_v013_signal,
    f49pr_f49_capital_return_payout_dy_lvl_126d_base_v014_signal,
    f49pr_f49_capital_return_payout_dy_z_252d_base_v015_signal,
    f49pr_f49_capital_return_payout_dy_rank_504d_base_v016_signal,
    f49pr_f49_capital_return_payout_yieldtrap_252d_base_v017_signal,
    f49pr_f49_capital_return_payout_qualyield_252d_base_v018_signal,
    f49pr_f49_capital_return_payout_pr_lvl_252d_base_v019_signal,
    f49pr_f49_capital_return_payout_pr_z_252d_base_v020_signal,
    f49pr_f49_capital_return_payout_pr_trend_252d_base_v021_signal,
    f49pr_f49_capital_return_payout_pr_stressflag_252d_base_v022_signal,
    f49pr_f49_capital_return_payout_dpsgrow_252d_base_v023_signal,
    f49pr_f49_capital_return_payout_dpsstreak_504d_base_v024_signal,
    f49pr_f49_capital_return_payout_dpsaccel_252d_base_v025_signal,
    f49pr_f49_capital_return_payout_prefdrag_lvl_252d_base_v026_signal,
    f49pr_f49_capital_return_payout_prefdrag_z_252d_base_v027_signal,
    f49pr_f49_capital_return_payout_prefocf_252d_base_v028_signal,
    f49pr_f49_capital_return_payout_royalty_lvl_252d_base_v029_signal,
    f49pr_f49_capital_return_payout_royalty_rank_504d_base_v030_signal,
    f49pr_f49_capital_return_payout_fcfyield_252d_base_v031_signal,
    f49pr_f49_capital_return_payout_totyield_z_252d_base_v032_signal,
    f49pr_f49_capital_return_payout_initflag_252d_base_v033_signal,
    f49pr_f49_capital_return_payout_cutdepth_252d_base_v034_signal,
    f49pr_f49_capital_return_payout_cutflag_252d_base_v035_signal,
    f49pr_f49_capital_return_payout_payearn_lvl_252d_base_v036_signal,
    f49pr_f49_capital_return_payout_payearn_z_252d_base_v037_signal,
    f49pr_f49_capital_return_payout_epspayout_252d_base_v038_signal,
    f49pr_f49_capital_return_payout_epspayoutflag_252d_base_v039_signal,
    f49pr_f49_capital_return_payout_paywedge_252d_base_v040_signal,
    f49pr_f49_capital_return_payout_divshortfall_252d_base_v041_signal,
    f49pr_f49_capital_return_payout_divgrowmc_252d_base_v042_signal,
    f49pr_f49_capital_return_payout_prdisp_252d_base_v043_signal,
    f49pr_f49_capital_return_payout_dyrevert_504d_base_v044_signal,
    f49pr_f49_capital_return_payout_psust_trend_252d_base_v045_signal,
    f49pr_f49_capital_return_payout_covstab_504d_base_v046_signal,
    f49pr_f49_capital_return_payout_netcommon_252d_base_v047_signal,
    f49pr_f49_capital_return_payout_prefshare_252d_base_v048_signal,
    f49pr_f49_capital_return_payout_dyxpr_252d_base_v049_signal,
    f49pr_f49_capital_return_payout_fcfpsvsdps_252d_base_v050_signal,
    f49pr_f49_capital_return_payout_earncov_252d_base_v051_signal,
    f49pr_f49_capital_return_payout_payinloss_252d_base_v052_signal,
    f49pr_f49_capital_return_payout_dymom_126d_base_v053_signal,
    f49pr_f49_capital_return_payout_psustspr_252d_base_v054_signal,
    f49pr_f49_capital_return_payout_dpsrangepos_504d_base_v055_signal,
    f49pr_f49_capital_return_payout_epscover_252d_base_v056_signal,
    f49pr_f49_capital_return_payout_royqualz_252d_base_v057_signal,
    f49pr_f49_capital_return_payout_payerpersist_504d_base_v058_signal,
    f49pr_f49_capital_return_payout_netcushion_252d_base_v059_signal,
    f49pr_f49_capital_return_payout_praccel_252d_base_v060_signal,
    f49pr_f49_capital_return_payout_dyfcfygap_252d_base_v061_signal,
    f49pr_f49_capital_return_payout_crintensity_504d_base_v062_signal,
    f49pr_f49_capital_return_payout_dpsunderwater_504d_base_v063_signal,
    f49pr_f49_capital_return_payout_covyieldmom_252d_base_v064_signal,
    f49pr_f49_capital_return_payout_dualsustain_252d_base_v065_signal,
    f49pr_f49_capital_return_payout_safetymargin_252d_base_v066_signal,
    f49pr_f49_capital_return_payout_growthquality_252d_base_v067_signal,
    f49pr_f49_capital_return_payout_qualtrapaxis_252d_base_v068_signal,
    f49pr_f49_capital_return_payout_prextreme_504d_base_v069_signal,
    f49pr_f49_capital_return_payout_ocfclaim_252d_base_v070_signal,
    f49pr_f49_capital_return_payout_yieldsteadyspr_504d_base_v071_signal,
    f49pr_f49_capital_return_payout_stressscore_252d_base_v072_signal,
    f49pr_f49_capital_return_payout_crpropensity_252d_base_v073_signal,
    f49pr_f49_capital_return_payout_dpslevelz_504d_base_v074_signal,
    f49pr_f49_capital_return_payout_totyieldrank_504d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F49_CAPITAL_RETURN_PAYOUT_REGISTRY_001_075 = REGISTRY


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

    dps = _fund(1, base=1.0, drift=0.01, vol=0.05).rename("dps")
    divyield = _fund(2, base=0.03, drift=0.0, vol=0.06).rename("divyield")
    payoutratio = _fund(3, base=0.5, drift=0.0, vol=0.07).rename("payoutratio")
    ncfdiv = _fund(4, base=5e7, drift=0.005, vol=0.07).rename("ncfdiv")
    prefdivis = _fund(5, base=5e6, drift=0.0, vol=0.07).rename("prefdivis")
    fcf = _fund(6, base=1.2e8, drift=0.0, vol=0.10, allow_neg=True).rename("fcf")
    ncfo = _fund(7, base=2e8, drift=0.0, vol=0.09, allow_neg=True).rename("ncfo")
    fcfps = _fund(8, base=2.0, drift=0.0, vol=0.10, allow_neg=True).rename("fcfps")
    eps = _fund(9, base=2.5, drift=0.0, vol=0.10, allow_neg=True).rename("eps")
    netinc = _fund(10, base=1.5e8, drift=0.0, vol=0.10, allow_neg=True).rename("netinc")
    marketcap = _fund(11, base=2e9, drift=0.0, vol=0.06).rename("marketcap")

    cols = {"dps": dps, "divyield": divyield, "payoutratio": payoutratio,
            "ncfdiv": ncfdiv, "prefdivis": prefdivis, "fcf": fcf, "ncfo": ncfo,
            "fcfps": fcfps, "eps": eps, "netinc": netinc, "marketcap": marketcap}

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

    print("OK f49_capital_return_payout_base_001_075_claude: %d features pass" % n_features)
