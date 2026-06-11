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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


def _slope(s, w):
    return s.diff(w) / float(w)


# ===== f37 producer-quality-compounder domain primitives =====
# A quality compounder = durable, profitable, cash-generative, and NON-dilutive.
# Every primitive consumes >=1 fundamental column and combines >=2 economics.

def _dilution(sharesbas, w):
    # share-count growth over window: positive = dilution (bad for compounder)
    return np.log(sharesbas.replace(0, np.nan) / sharesbas.shift(w).replace(0, np.nan))


def _antidilution(sharesbas, w):
    # low-dilution score: negative of share growth (high = disciplined)
    return -np.log(sharesbas.replace(0, np.nan) / sharesbas.shift(w).replace(0, np.nan))


def _fcf_margin(fcf, revenue):
    # FCF as a share of revenue (cash-conversion quality)
    return fcf / revenue.replace(0, np.nan)


def _fcf_per_share(fcf, sharesbas):
    return fcf / sharesbas.replace(0, np.nan)


def _roic_stability(roic, w):
    # stable-positive-ROIC: mean / volatility (high & steady = durable)
    m = roic.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = roic.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan)


def _pos_frac(s, w):
    # fraction of window the series is strictly positive (durability count)
    pos = (s > 0).astype(float)
    return pos.rolling(w, min_periods=max(1, w // 2)).mean()


def _equity_growth(equity, w):
    return np.log(equity.replace(0, np.nan) / equity.shift(w).replace(0, np.nan))


def _rev_growth(revenue, w):
    return np.log(revenue.replace(0, np.nan) / revenue.shift(w).replace(0, np.nan))


def _bvps(equity, sharesbas):
    # book value per share (per-share compounding of equity)
    return equity / sharesbas.replace(0, np.nan)


def _quality_score(roic, fcf, revenue):
    # composite quality: positive ROIC scaled by positive FCF margin
    fm = fcf / revenue.replace(0, np.nan)
    return roic.clip(lower=-1.0, upper=1.0) * fm


# ============================================================
# v001 quality-minus-dilution: stable ROIC less share-growth (core compounder thesis)
def f37pq_f37_producer_quality_compounder_qmd_252d_base_v001_signal(roic, sharesbas):
    rs = _roic_stability(roic, 252)
    dil = _dilution(sharesbas, 252)
    b = np.tanh(rs) - 5.0 * dil
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v002 positive-FCF x low-dilution composite (FCF-margin-dominant product form)
def f37pq_f37_producer_quality_compounder_fcfdil_252d_base_v002_signal(fcf, revenue, sharesbas):
    fm = _mean(_fcf_margin(fcf, revenue), 63)
    anti = _antidilution(sharesbas, 126)
    b = np.tanh(3.0 * fm) * (1.0 + np.tanh(8.0 * anti))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v003 durable-producer score: ROIC positivity-fraction x FCF positivity-fraction
def f37pq_f37_producer_quality_compounder_durable_252d_base_v003_signal(roic, fcf):
    pr = _pos_frac(roic, 252)
    pf = _pos_frac(fcf, 252)
    b = pr * pf
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v004 ROIC x FCF-margin interaction (quality cash returns)
def f37pq_f37_producer_quality_compounder_qual_252d_base_v004_signal(roic, fcf, revenue):
    b = _quality_score(roic, fcf, revenue)
    result = _mean(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# v005 book-value-per-share growth (per-share equity compounding net of dilution)
def f37pq_f37_producer_quality_compounder_bvpsg_252d_base_v005_signal(equity, sharesbas):
    bv = _bvps(equity, sharesbas)
    b = np.log(bv.replace(0, np.nan) / bv.shift(252).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v006 FCF-per-share growth (cash compounding per share)
def f37pq_f37_producer_quality_compounder_fcfpsg_252d_base_v006_signal(fcf, sharesbas):
    fps = _fcf_per_share(fcf, sharesbas)
    b = fps - fps.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v007 ROIC level z-scored vs own 504d history, gated by net-margin sign
def f37pq_f37_producer_quality_compounder_roicz_504d_base_v007_signal(roic, netmargin):
    rz = _z(roic, 504)
    gate = np.tanh(5.0 * netmargin)
    b = rz * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v008 revenue growth x FCF-margin (profitable growth, not growth-at-any-cost)
def f37pq_f37_producer_quality_compounder_profgrow_252d_base_v008_signal(revenue, fcf):
    rg = _rev_growth(revenue, 252)
    fm = _fcf_margin(fcf, revenue)
    b = rg * np.tanh(3.0 * fm)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v009 equity-build efficiency: equity growth per unit of dilution taken on
def f37pq_f37_producer_quality_compounder_eqnetdil_252d_base_v009_signal(equity, sharesbas):
    eg = _equity_growth(equity, 252)
    dil = _dilution(sharesbas, 252)
    ratio = eg / (dil.abs() + 0.02)
    b = np.tanh(ratio) * np.sign(eg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v010 net-margin stability x antidilution (steady margins + discipline)
def f37pq_f37_producer_quality_compounder_nmstabdil_252d_base_v010_signal(netmargin, sharesbas):
    m = _mean(netmargin, 252)
    sd = _std(netmargin, 252)
    stab = m / sd.replace(0, np.nan)
    anti = _antidilution(sharesbas, 252)
    b = np.tanh(stab) + 4.0 * anti
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v011 triple composite: positive ROIC AND positive FCF AND no dilution (count-friendly)
def f37pq_f37_producer_quality_compounder_triple_252d_base_v011_signal(roic, fcf, sharesbas):
    a = (roic > 0).astype(float)
    bb = (fcf > 0).astype(float)
    dil = _dilution(sharesbas, 63)
    c = (dil <= 0).astype(float)
    cnt = (a + bb + c)
    b = cnt.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v012 FCF-per-share momentum vs revenue-per-share momentum (cash gaining on sales/share)
def f37pq_f37_producer_quality_compounder_fcfmindil_252d_base_v012_signal(fcf, revenue, sharesbas):
    fps = _fcf_per_share(fcf, sharesbas)
    rps = revenue / sharesbas.replace(0, np.nan)
    fm = fps.diff(126) / rps.replace(0, np.nan)
    b = np.tanh(2.0 * fm) - 0.5 * _z(_dilution(sharesbas, 126), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v013 ROIC trend (improving returns on capital) gated by positive FCF
def f37pq_f37_producer_quality_compounder_roictrend_252d_base_v013_signal(roic, fcf):
    tr = _slope(roic, 126)
    gate = np.tanh(2.0 * _mean(fcf, 126) / _std(fcf, 252).replace(0, np.nan))
    b = tr * (0.5 + 0.5 * gate)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v014 retained-per-share build: equity/share growth weighted by ROIC level
def f37pq_f37_producer_quality_compounder_retps_252d_base_v014_signal(equity, sharesbas, roic):
    bv = _bvps(equity, sharesbas)
    g = bv.pct_change(126)
    b = g * np.tanh(3.0 * roic)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v015 compounder rank: blended FCF-margin + ROIC, percentile-ranked vs own history
def f37pq_f37_producer_quality_compounder_blendrank_252d_base_v015_signal(fcf, revenue, roic):
    fm = _fcf_margin(fcf, revenue)
    blend = np.tanh(3.0 * fm) + np.tanh(3.0 * roic)
    b = _rank(blend, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v016 share-count drawup: cumulative dilution from the 504d trough share count
def f37pq_f37_producer_quality_compounder_cumdil_504d_base_v016_signal(sharesbas, roic):
    trough = _rmin(sharesbas, 504)
    cum = np.log(sharesbas.replace(0, np.nan) / trough.replace(0, np.nan))
    b = cum * (1.0 - np.tanh(3.0 * roic))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v017 FCF consistency: positive-FCF fraction x FCF-margin level
def f37pq_f37_producer_quality_compounder_fcfcons_252d_base_v017_signal(fcf, revenue):
    pf = _pos_frac(fcf, 252)
    fm = _mean(_fcf_margin(fcf, revenue), 126)
    b = pf * np.tanh(3.0 * fm)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v018 quality-adjusted revenue scale: log-revenue level x ROIC positivity
def f37pq_f37_producer_quality_compounder_qrev_252d_base_v018_signal(revenue, roic):
    scale = np.log(revenue.replace(0, np.nan))
    sc = _z(scale, 252)
    b = sc * _pos_frac(roic, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v019 ROIC dispersion penalty against FCF margin (steady cash beats lumpy returns)
def f37pq_f37_producer_quality_compounder_steady_252d_base_v019_signal(roic, fcf, revenue):
    disp = _std(roic, 252)
    fm = _fcf_margin(fcf, revenue)
    b = np.tanh(3.0 * fm) - np.tanh(2.0 * disp)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v020 self-funding compounder: FCF margin vs equity growth (growing without raising)
def f37pq_f37_producer_quality_compounder_selffund_252d_base_v020_signal(fcf, revenue, equity):
    fm = _fcf_margin(fcf, revenue)
    eg = _equity_growth(equity, 252)
    b = np.tanh(3.0 * fm) * np.sign(eg) * (eg.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v021 durable margin breadth: net-margin positive-fraction x ROIC positive-fraction
def f37pq_f37_producer_quality_compounder_marbreadth_252d_base_v021_signal(netmargin, roic):
    pm = _pos_frac(netmargin, 252)
    pr = _pos_frac(roic, 252)
    b = pm * pr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v022 dilution-adjusted FCF yield per share, z-scored
def f37pq_f37_producer_quality_compounder_fcfyld_252d_base_v022_signal(fcf, sharesbas):
    fps = _fcf_per_share(fcf, sharesbas)
    b = _z(fps, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v023 ROIC above its own 504d median, scaled by FCF positivity
def f37pq_f37_producer_quality_compounder_roicexc_504d_base_v023_signal(roic, fcf):
    med = roic.rolling(504, min_periods=252).median()
    exc = roic - med
    b = exc * _pos_frac(fcf, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v024 compounder momentum: change in (ROIC + FCF margin) over a year
def f37pq_f37_producer_quality_compounder_qmom_252d_base_v024_signal(roic, fcf, revenue):
    fm = _fcf_margin(fcf, revenue)
    q = np.tanh(3.0 * roic) + np.tanh(3.0 * fm)
    b = q - q.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v025 anti-dilution streak: consecutive periods of flat/declining share count
def f37pq_f37_producer_quality_compounder_dilstreak_base_v025_signal(sharesbas, fcf):
    chg = sharesbas.diff(21)
    good = (chg <= 0).astype(float)
    streak = good.rolling(252, min_periods=126).sum()
    b = streak * (0.5 + 0.5 * np.tanh(2.0 * _mean(fcf, 126) / _std(fcf, 252).replace(0, np.nan)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v026 net-margin x revenue-growth (quality of the top-line ramp)
def f37pq_f37_producer_quality_compounder_nmgrow_252d_base_v026_signal(netmargin, revenue):
    rg = _rev_growth(revenue, 252)
    b = np.tanh(4.0 * netmargin) * rg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v027 capital efficiency build: ROIC x equity growth (returns on a growing base)
def f37pq_f37_producer_quality_compounder_capeff_252d_base_v027_signal(roic, equity):
    eg = _equity_growth(equity, 252)
    b = np.tanh(3.0 * _mean(roic, 126)) * eg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v028 quality minus dilution, long-horizon (504d) with margin gate
def f37pq_f37_producer_quality_compounder_qmd_504d_base_v028_signal(roic, sharesbas, netmargin):
    rs = _roic_stability(roic, 504)
    dil = _dilution(sharesbas, 504)
    gate = np.tanh(4.0 * netmargin)
    b = np.tanh(rs) * (0.5 + 0.5 * gate) - 4.0 * dil
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v029 FCF-margin trend (improving cash conversion) net of dilution trend
def f37pq_f37_producer_quality_compounder_fcftrend_252d_base_v029_signal(fcf, revenue, sharesbas):
    fm = _fcf_margin(fcf, revenue)
    ft = _slope(fm, 126)
    dt = _slope(_dilution(sharesbas, 63), 126)
    b = ft - dt
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v030 revenue-per-share growth (top-line compounding net of dilution)
def f37pq_f37_producer_quality_compounder_revps_252d_base_v030_signal(revenue, sharesbas):
    rps = revenue / sharesbas.replace(0, np.nan)
    b = np.log(rps.replace(0, np.nan) / rps.shift(252).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v031 owner-earnings proxy: FCF-per-share x ROIC, smoothed
def f37pq_f37_producer_quality_compounder_ownerearn_252d_base_v031_signal(fcf, sharesbas, roic):
    fps = _fcf_per_share(fcf, sharesbas)
    b = _mean(fps * np.tanh(3.0 * roic), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v032 margin-quality spread: net-margin minus its dispersion, scaled by FCF positivity
def f37pq_f37_producer_quality_compounder_marqual_252d_base_v032_signal(netmargin, fcf):
    m = _mean(netmargin, 252)
    sd = _std(netmargin, 252)
    b = (m - sd) * _pos_frac(fcf, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v033 compounder z-blend: z(ROIC)+z(FCF margin)-z(dilution)
def f37pq_f37_producer_quality_compounder_zblend_252d_base_v033_signal(roic, fcf, revenue, sharesbas):
    fm = _fcf_margin(fcf, revenue)
    dil = _dilution(sharesbas, 252)
    b = _z(roic, 252) + _z(fm, 252) - _z(dil, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v034 sustainable-growth gap: ROIC vs revenue-growth (returns funding the ramp)
def f37pq_f37_producer_quality_compounder_susgrow_252d_base_v034_signal(roic, revenue):
    rg = _rev_growth(revenue, 252)
    b = np.tanh(3.0 * _mean(roic, 126)) - rg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v035 quality persistence: months in last 2y with ROIC>0 & FCF>0 & no-dilution
def f37pq_f37_producer_quality_compounder_qpersist_504d_base_v035_signal(roic, fcf, sharesbas):
    allgood = ((roic > 0) & (fcf > 0) & (sharesbas.diff(21) <= 0)).astype(float)
    b = allgood.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v036 equity-compounding rate net of dilution, risk-adjusted by ROIC vol
def f37pq_f37_producer_quality_compounder_eqcomp_504d_base_v036_signal(equity, sharesbas, roic):
    bv = _bvps(equity, sharesbas)
    g = np.log(bv.replace(0, np.nan) / bv.shift(504).replace(0, np.nan))
    rv = _std(roic, 504)
    b = g / (1.0 + rv)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v037 cash-on-equity trend vs share-count trend (improving cash return per owner)
def f37pq_f37_producer_quality_compounder_fcfcov_252d_base_v037_signal(fcf, sharesbas, equity):
    coe = fcf / equity.replace(0, np.nan)
    coe_tr = _slope(_mean(coe, 63), 126)
    sh_tr = _slope(np.log(sharesbas.replace(0, np.nan)), 126)
    b = np.tanh(20.0 * coe_tr) - np.tanh(50.0 * sh_tr)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v038 ROIC-weighted revenue scale rank (big, high-return producers)
def f37pq_f37_producer_quality_compounder_scalerank_504d_base_v038_signal(revenue, roic):
    scale = np.log(revenue.replace(0, np.nan)) * np.tanh(3.0 * roic)
    b = _rank(scale, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v039 net-margin x FCF-margin agreement (earnings backed by cash)
def f37pq_f37_producer_quality_compounder_cashqual_252d_base_v039_signal(netmargin, fcf, revenue):
    fm = _fcf_margin(fcf, revenue)
    b = np.tanh(4.0 * netmargin) * np.tanh(4.0 * fm)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v040 stable-positive-ROIC index: positive-frac x (1 - normalized dispersion)
def f37pq_f37_producer_quality_compounder_stableroic_504d_base_v040_signal(roic):
    pf = _pos_frac(roic, 504)
    disp = _std(roic, 504) / _mean(roic.abs(), 504).replace(0, np.nan)
    b = pf * (1.0 - np.tanh(disp))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v041 dilution-adjusted ROIC momentum
def f37pq_f37_producer_quality_compounder_roicmomdil_252d_base_v041_signal(roic, sharesbas):
    rm = roic - roic.shift(252)
    dil = _dilution(sharesbas, 252)
    b = rm - 3.0 * dil
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v042 compounder distance-from-peak quality (current vs best 504d quality)
def f37pq_f37_producer_quality_compounder_qpeak_504d_base_v042_signal(roic, fcf, revenue):
    fm = _fcf_margin(fcf, revenue)
    q = np.tanh(3.0 * roic) + np.tanh(3.0 * fm)
    peak = _rmax(q, 504)
    b = q - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v043 high-quality regime flag (count): positive-net-margin AND positive-FCF months, depth-weighted
def f37pq_f37_producer_quality_compounder_hqregime_252d_base_v043_signal(netmargin, fcf):
    flag = ((netmargin > 0) & (fcf > 0)).astype(float)
    frac = flag.rolling(252, min_periods=126).mean()
    depth = np.tanh(4.0 * _mean(netmargin, 63))
    b = frac + 0.2 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v044 per-share FCF margin: FCF/share scaled by revenue/share (cash density)
def f37pq_f37_producer_quality_compounder_cashdens_252d_base_v044_signal(fcf, revenue, sharesbas):
    fps = _fcf_per_share(fcf, sharesbas)
    rps = revenue / sharesbas.replace(0, np.nan)
    b = _z(fps / rps.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v045 equity-return engine: ROIC x equity-to-revenue (capital intensity adj returns)
def f37pq_f37_producer_quality_compounder_eqengine_252d_base_v045_signal(roic, equity, revenue):
    intens = equity / revenue.replace(0, np.nan)
    b = np.tanh(3.0 * roic) / (1.0 + np.tanh(intens))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v046 dilution intensity vs FCF-funding capacity (raise-dependence inverse)
def f37pq_f37_producer_quality_compounder_raiseindep_252d_base_v046_signal(sharesbas, fcf, revenue):
    dil = _dilution(sharesbas, 252)
    fm = _fcf_margin(fcf, revenue)
    b = np.tanh(3.0 * fm) - np.tanh(10.0 * dil)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v047 quality trend acceleration vs level (improving compounder)
def f37pq_f37_producer_quality_compounder_qaccel_252d_base_v047_signal(roic, fcf, revenue):
    fm = _fcf_margin(fcf, revenue)
    q = np.tanh(3.0 * roic) + np.tanh(3.0 * fm)
    b = _slope(q, 63) + 0.3 * _z(q, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v048 net-margin compounding: margin level x revenue/share growth
def f37pq_f37_producer_quality_compounder_nmcompound_252d_base_v048_signal(netmargin, revenue, sharesbas):
    rps = revenue / sharesbas.replace(0, np.nan)
    g = np.log(rps.replace(0, np.nan) / rps.shift(252).replace(0, np.nan))
    b = np.tanh(4.0 * _mean(netmargin, 126)) * g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v049 survivor-compounder: positive-everything fraction minus cumulative dilution
def f37pq_f37_producer_quality_compounder_survcomp_504d_base_v049_signal(roic, fcf, sharesbas):
    good = ((roic > 0) & (fcf > 0)).astype(float).rolling(504, min_periods=252).mean()
    cumdil = _dilution(sharesbas, 504).clip(lower=0)
    b = good - 2.0 * cumdil
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v050 ROIC vs FCF-margin gap (returns not converting to cash = warning)
def f37pq_f37_producer_quality_compounder_accrualgap_252d_base_v050_signal(roic, fcf, revenue):
    fm = _fcf_margin(fcf, revenue)
    b = np.tanh(3.0 * roic) - np.tanh(3.0 * fm)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v051 book-value compounding rank vs own history
def f37pq_f37_producer_quality_compounder_bvrank_504d_base_v051_signal(equity, sharesbas):
    bv = _bvps(equity, sharesbas)
    g = bv.pct_change(126)
    b = _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v052 disciplined-growth: revenue growth gated by no-dilution and positive FCF
def f37pq_f37_producer_quality_compounder_discgrow_252d_base_v052_signal(revenue, sharesbas, fcf):
    rg = _rev_growth(revenue, 252)
    nondil = (_dilution(sharesbas, 252) <= 0.02).astype(float)
    posf = (_mean(fcf, 126) > 0).astype(float)
    b = rg * (0.25 + 0.375 * nondil + 0.375 * posf)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v053 ROIC-FCF coherence: rolling correlation of returns & cash (true quality)
def f37pq_f37_producer_quality_compounder_coher_252d_base_v053_signal(roic, fcf):
    b = roic.rolling(252, min_periods=126).corr(fcf)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v054 net-margin z minus dilution z (margin strength vs share creep)
def f37pq_f37_producer_quality_compounder_nmdilz_252d_base_v054_signal(netmargin, sharesbas):
    b = _z(netmargin, 252) - _z(_dilution(sharesbas, 252), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v055 FCF-margin level x positive-ROIC fraction (cash-rich durable)
def f37pq_f37_producer_quality_compounder_cashdurable_252d_base_v055_signal(fcf, revenue, roic):
    fm = _mean(_fcf_margin(fcf, revenue), 126)
    b = np.tanh(3.0 * fm) * _pos_frac(roic, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v056 equity-per-share trough recovery (rebuilding book after a hit)
def f37pq_f37_producer_quality_compounder_bvrecov_504d_base_v056_signal(equity, sharesbas, roic):
    bv = _bvps(equity, sharesbas)
    trough = _rmin(bv, 504)
    rec = bv / trough.replace(0, np.nan) - 1.0
    b = rec * np.tanh(3.0 * _mean(roic, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v057 quality dispersion across drivers (agreement = high conviction)
def f37pq_f37_producer_quality_compounder_qagree_252d_base_v057_signal(roic, fcf, revenue, netmargin):
    fm = _fcf_margin(fcf, revenue)
    a = np.tanh(3.0 * roic)
    b1 = np.tanh(3.0 * fm)
    c = np.tanh(4.0 * netmargin)
    stacked = pd.concat([a, b1, c], axis=1)
    b = stacked.mean(axis=1) - stacked.std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v058 sustainable per-share FCF growth, dilution-penalized
def f37pq_f37_producer_quality_compounder_susfcfps_504d_base_v058_signal(fcf, sharesbas):
    fps = _fcf_per_share(fcf, sharesbas)
    g = fps - fps.shift(504)
    dil = _dilution(sharesbas, 504)
    b = g - 0.5 * dil
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v059 margin-of-safety quality: net-margin buffer x FCF positivity
def f37pq_f37_producer_quality_compounder_marsafety_252d_base_v059_signal(netmargin, fcf):
    buf = netmargin.clip(lower=-0.5, upper=0.5)
    b = buf * _pos_frac(fcf, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v060 ROIC stability rank vs own history, dilution-gated
def f37pq_f37_producer_quality_compounder_roicstabrank_504d_base_v060_signal(roic, sharesbas):
    rs = _roic_stability(roic, 252)
    rk = _rank(rs, 504)
    anti = (_dilution(sharesbas, 252) <= 0).astype(float)
    b = rk * (0.5 + 0.5 * anti)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v061 revenue-scaled FCF growth (absolute cash generation expansion)
def f37pq_f37_producer_quality_compounder_fcfexpand_252d_base_v061_signal(fcf, revenue):
    fcf_sm = _mean(fcf, 63)
    g = fcf_sm.diff(252) / revenue.replace(0, np.nan)
    b = np.tanh(3.0 * g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v062 capital-light quality: ROIC x (revenue/equity) turnover
def f37pq_f37_producer_quality_compounder_caplight_252d_base_v062_signal(roic, revenue, equity):
    turn = revenue / equity.replace(0, np.nan)
    b = np.tanh(3.0 * _mean(roic, 126)) * np.tanh(turn)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v063 compounder breakout: quality at a new 252d high (count-friendly)
def f37pq_f37_producer_quality_compounder_qbreakout_252d_base_v063_signal(roic, fcf, revenue):
    fm = _fcf_margin(fcf, revenue)
    q = np.tanh(3.0 * roic) + np.tanh(3.0 * fm)
    hi = _rmax(q.shift(1), 252)
    flag = (q >= hi).astype(float)
    b = flag.rolling(252, min_periods=126).mean() + 0.1 * q
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v064 dilution-shock detector: large recent share jump vs FCF buffer
def f37pq_f37_producer_quality_compounder_dilshock_63d_base_v064_signal(sharesbas, fcf, revenue):
    jump = _dilution(sharesbas, 63)
    fm = _fcf_margin(fcf, revenue)
    b = -jump * (1.0 - np.tanh(3.0 * fm).clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v065 long-run quality level (504d mean of blended quality)
def f37pq_f37_producer_quality_compounder_qlevel_504d_base_v065_signal(roic, fcf, revenue, netmargin):
    fm = _fcf_margin(fcf, revenue)
    q = np.tanh(3.0 * roic) + np.tanh(3.0 * fm) + np.tanh(4.0 * netmargin)
    b = _mean(q, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v066 free-cash-funded equity growth (equity build covered by cash, not raises)
def f37pq_f37_producer_quality_compounder_fcffundeq_252d_base_v066_signal(fcf, equity, sharesbas):
    eg = _equity_growth(equity, 252)
    dil = _dilution(sharesbas, 252)
    organic = eg - dil
    b = organic * np.sign(_mean(fcf, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v067 quality vs cyclicality: ROIC level minus its own swing amplitude
def f37pq_f37_producer_quality_compounder_qvscycle_504d_base_v067_signal(roic, fcf):
    amp = (_rmax(roic, 504) - _rmin(roic, 504))
    b = np.tanh(3.0 * _mean(roic, 252)) * _pos_frac(fcf, 252) - np.tanh(amp)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v068 dilution-adjusted net-margin compounding rank
def f37pq_f37_producer_quality_compounder_nmcomprank_504d_base_v068_signal(netmargin, sharesbas):
    score = _mean(netmargin, 126) - _dilution(sharesbas, 252)
    b = _rank(score, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v069 cash-return-on-equity: FCF/equity, stability-adjusted
def f37pq_f37_producer_quality_compounder_croe_252d_base_v069_signal(fcf, equity):
    croe = fcf / equity.replace(0, np.nan)
    m = _mean(croe, 252)
    sd = _std(croe, 252)
    b = m / (1.0 + sd)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v070 quality-weighted survival distance from worst quality
def f37pq_f37_producer_quality_compounder_qsurvdist_504d_base_v070_signal(roic, fcf, revenue):
    fm = _fcf_margin(fcf, revenue)
    q = np.tanh(3.0 * roic) + np.tanh(3.0 * fm)
    worst = _rmin(q, 504)
    b = q - worst
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v071 revenue-stability x margin (predictable producer)
def f37pq_f37_producer_quality_compounder_revstabmar_252d_base_v071_signal(revenue, netmargin):
    rg = revenue.pct_change(21)
    stab = 1.0 / (1.0 + _std(rg, 252))
    b = stab * np.tanh(4.0 * _mean(netmargin, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v072 compounder composite z minus dilution streak penalty
def f37pq_f37_producer_quality_compounder_compz_252d_base_v072_signal(roic, fcf, revenue, sharesbas):
    fm = _fcf_margin(fcf, revenue)
    comp = _z(roic, 252) + _z(fm, 252)
    dilbad = (sharesbas.diff(21) > 0).astype(float).rolling(252, min_periods=126).mean()
    b = comp - 2.0 * dilbad
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v073 per-share earnings power: net-margin x revenue/share, dilution-aware
def f37pq_f37_producer_quality_compounder_eps_252d_base_v073_signal(netmargin, revenue, sharesbas):
    eps = netmargin * revenue / sharesbas.replace(0, np.nan)
    b = _z(eps, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v074 quality improvement breadth: magnitude-weighted YoY improvement across drivers
def f37pq_f37_producer_quality_compounder_qimprove_252d_base_v074_signal(roic, fcf, revenue, equity):
    fm = _fcf_margin(fcf, revenue)
    a = np.tanh(3.0 * (roic - roic.shift(252)))
    b1 = np.tanh(3.0 * (fm - fm.shift(252)))
    c = np.tanh(3.0 * _equity_growth(equity, 252))
    d = np.tanh(3.0 * _rev_growth(revenue, 252))
    b = _mean((a + b1 + c + d) / 4.0, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# v075 elite-compounder gate: high ROIC AND high FCF margin AND shrinking shares
def f37pq_f37_producer_quality_compounder_elite_252d_base_v075_signal(roic, fcf, revenue, sharesbas):
    fm = _fcf_margin(fcf, revenue)
    elite = ((roic > roic.rolling(504, min_periods=126).median())
             & (fm > 0)
             & (sharesbas.diff(63) <= 0)).astype(float)
    b = elite.rolling(252, min_periods=126).mean() + 0.1 * np.tanh(3.0 * roic)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f37pq_f37_producer_quality_compounder_qmd_252d_base_v001_signal,
    f37pq_f37_producer_quality_compounder_fcfdil_252d_base_v002_signal,
    f37pq_f37_producer_quality_compounder_durable_252d_base_v003_signal,
    f37pq_f37_producer_quality_compounder_qual_252d_base_v004_signal,
    f37pq_f37_producer_quality_compounder_bvpsg_252d_base_v005_signal,
    f37pq_f37_producer_quality_compounder_fcfpsg_252d_base_v006_signal,
    f37pq_f37_producer_quality_compounder_roicz_504d_base_v007_signal,
    f37pq_f37_producer_quality_compounder_profgrow_252d_base_v008_signal,
    f37pq_f37_producer_quality_compounder_eqnetdil_252d_base_v009_signal,
    f37pq_f37_producer_quality_compounder_nmstabdil_252d_base_v010_signal,
    f37pq_f37_producer_quality_compounder_triple_252d_base_v011_signal,
    f37pq_f37_producer_quality_compounder_fcfmindil_252d_base_v012_signal,
    f37pq_f37_producer_quality_compounder_roictrend_252d_base_v013_signal,
    f37pq_f37_producer_quality_compounder_retps_252d_base_v014_signal,
    f37pq_f37_producer_quality_compounder_blendrank_252d_base_v015_signal,
    f37pq_f37_producer_quality_compounder_cumdil_504d_base_v016_signal,
    f37pq_f37_producer_quality_compounder_fcfcons_252d_base_v017_signal,
    f37pq_f37_producer_quality_compounder_qrev_252d_base_v018_signal,
    f37pq_f37_producer_quality_compounder_steady_252d_base_v019_signal,
    f37pq_f37_producer_quality_compounder_selffund_252d_base_v020_signal,
    f37pq_f37_producer_quality_compounder_marbreadth_252d_base_v021_signal,
    f37pq_f37_producer_quality_compounder_fcfyld_252d_base_v022_signal,
    f37pq_f37_producer_quality_compounder_roicexc_504d_base_v023_signal,
    f37pq_f37_producer_quality_compounder_qmom_252d_base_v024_signal,
    f37pq_f37_producer_quality_compounder_dilstreak_base_v025_signal,
    f37pq_f37_producer_quality_compounder_nmgrow_252d_base_v026_signal,
    f37pq_f37_producer_quality_compounder_capeff_252d_base_v027_signal,
    f37pq_f37_producer_quality_compounder_qmd_504d_base_v028_signal,
    f37pq_f37_producer_quality_compounder_fcftrend_252d_base_v029_signal,
    f37pq_f37_producer_quality_compounder_revps_252d_base_v030_signal,
    f37pq_f37_producer_quality_compounder_ownerearn_252d_base_v031_signal,
    f37pq_f37_producer_quality_compounder_marqual_252d_base_v032_signal,
    f37pq_f37_producer_quality_compounder_zblend_252d_base_v033_signal,
    f37pq_f37_producer_quality_compounder_susgrow_252d_base_v034_signal,
    f37pq_f37_producer_quality_compounder_qpersist_504d_base_v035_signal,
    f37pq_f37_producer_quality_compounder_eqcomp_504d_base_v036_signal,
    f37pq_f37_producer_quality_compounder_fcfcov_252d_base_v037_signal,
    f37pq_f37_producer_quality_compounder_scalerank_504d_base_v038_signal,
    f37pq_f37_producer_quality_compounder_cashqual_252d_base_v039_signal,
    f37pq_f37_producer_quality_compounder_stableroic_504d_base_v040_signal,
    f37pq_f37_producer_quality_compounder_roicmomdil_252d_base_v041_signal,
    f37pq_f37_producer_quality_compounder_qpeak_504d_base_v042_signal,
    f37pq_f37_producer_quality_compounder_hqregime_252d_base_v043_signal,
    f37pq_f37_producer_quality_compounder_cashdens_252d_base_v044_signal,
    f37pq_f37_producer_quality_compounder_eqengine_252d_base_v045_signal,
    f37pq_f37_producer_quality_compounder_raiseindep_252d_base_v046_signal,
    f37pq_f37_producer_quality_compounder_qaccel_252d_base_v047_signal,
    f37pq_f37_producer_quality_compounder_nmcompound_252d_base_v048_signal,
    f37pq_f37_producer_quality_compounder_survcomp_504d_base_v049_signal,
    f37pq_f37_producer_quality_compounder_accrualgap_252d_base_v050_signal,
    f37pq_f37_producer_quality_compounder_bvrank_504d_base_v051_signal,
    f37pq_f37_producer_quality_compounder_discgrow_252d_base_v052_signal,
    f37pq_f37_producer_quality_compounder_coher_252d_base_v053_signal,
    f37pq_f37_producer_quality_compounder_nmdilz_252d_base_v054_signal,
    f37pq_f37_producer_quality_compounder_cashdurable_252d_base_v055_signal,
    f37pq_f37_producer_quality_compounder_bvrecov_504d_base_v056_signal,
    f37pq_f37_producer_quality_compounder_qagree_252d_base_v057_signal,
    f37pq_f37_producer_quality_compounder_susfcfps_504d_base_v058_signal,
    f37pq_f37_producer_quality_compounder_marsafety_252d_base_v059_signal,
    f37pq_f37_producer_quality_compounder_roicstabrank_504d_base_v060_signal,
    f37pq_f37_producer_quality_compounder_fcfexpand_252d_base_v061_signal,
    f37pq_f37_producer_quality_compounder_caplight_252d_base_v062_signal,
    f37pq_f37_producer_quality_compounder_qbreakout_252d_base_v063_signal,
    f37pq_f37_producer_quality_compounder_dilshock_63d_base_v064_signal,
    f37pq_f37_producer_quality_compounder_qlevel_504d_base_v065_signal,
    f37pq_f37_producer_quality_compounder_fcffundeq_252d_base_v066_signal,
    f37pq_f37_producer_quality_compounder_qvscycle_504d_base_v067_signal,
    f37pq_f37_producer_quality_compounder_nmcomprank_504d_base_v068_signal,
    f37pq_f37_producer_quality_compounder_croe_252d_base_v069_signal,
    f37pq_f37_producer_quality_compounder_qsurvdist_504d_base_v070_signal,
    f37pq_f37_producer_quality_compounder_revstabmar_252d_base_v071_signal,
    f37pq_f37_producer_quality_compounder_compz_252d_base_v072_signal,
    f37pq_f37_producer_quality_compounder_eps_252d_base_v073_signal,
    f37pq_f37_producer_quality_compounder_qimprove_252d_base_v074_signal,
    f37pq_f37_producer_quality_compounder_elite_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F37_PRODUCER_QUALITY_COMPOUNDER_REGISTRY_001_075 = REGISTRY


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

    roic = _fund(3, base=0.12, drift=-0.01, vol=0.55, allow_neg=True).rename("roic")
    fcf = _fund(5, base=5e7, drift=-0.01, vol=0.55, allow_neg=True).rename("fcf")
    sharesbas = _fund(103, base=2e8, drift=0.03, vol=0.04).rename("sharesbas")
    netmargin = _fund(14, base=0.10, drift=-0.01, vol=0.55, allow_neg=True).rename("netmargin")
    revenue = _fund(105, base=3e8, drift=0.02, vol=0.10).rename("revenue")
    equity = _fund(106, base=4e8, drift=0.02, vol=0.08).rename("equity")

    cols = {"roic": roic, "fcf": fcf, "sharesbas": sharesbas,
            "netmargin": netmargin, "revenue": revenue, "equity": equity}

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

    print("OK f37_producer_quality_compounder_base_001_075_claude: %d features pass" % n_features)
