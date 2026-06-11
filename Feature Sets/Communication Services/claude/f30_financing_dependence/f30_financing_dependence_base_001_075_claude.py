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


def _slope(s, w):
    return s - s.shift(w)


# ===== folder domain primitives (financing dependence) =====
# All inputs are SIGNED cash flows: ncff financing, ncfcommon equity, ncfdebt debt,
# ncfo operating, ncfi investing. Positive = inflow, negative = outflow.

def _f30_ext_reliance(ncff, ncfo, w):
    # rolling external-financing reliance: |financing| relative to total cash engine
    f = _mean(ncff, w)
    o = _mean(ncfo, w)
    return f / (f.abs() + o.abs()).replace(0, np.nan)


def _f30_burn_cover(ncff, ncfo, w):
    # how much of operating burn (-ncfo when negative) is covered by financing inflow
    burn = (-ncfo).clip(lower=0)
    inflow = ncff.clip(lower=0)
    return _mean(inflow, w) / _mean(burn, w).replace(0, np.nan)


def _f30_self_fund_gap(ncfo, ncfi, w):
    # free cash before financing = ncfo + ncfi ; negative -> funding gap
    fcf_pre = _mean(ncfo + ncfi, w)
    scale = (_mean(ncfo.abs(), w) + _mean(ncfi.abs(), w)).replace(0, np.nan)
    return fcf_pre / scale


def _f30_equity_debt_mix(ncfcommon, ncfdebt, w):
    # equity-vs-debt financing mix in [-1, 1]: +1 all equity, -1 all debt
    e = _mean(ncfcommon, w)
    d = _mean(ncfdebt, w)
    return (e - d) / (e.abs() + d.abs()).replace(0, np.nan)


def _f30_raise_intensity(ncff, w):
    # capital-raise intensity: positive financing inflows relative to financing turnover
    inflow = _mean(ncff.clip(lower=0), w)
    turn = _mean(ncff.abs(), w).replace(0, np.nan)
    return inflow / turn


# ============================================================
# external-financing reliance over 252d (financing vs operating engine)
def f30fd_f30_financing_dependence_extrel_252d_base_v001_signal(ncff, ncfo):
    b = _f30_ext_reliance(ncff, ncfo, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# external-financing reliance over 126d
def f30fd_f30_financing_dependence_extrel_126d_base_v002_signal(ncff, ncfo):
    b = _f30_ext_reliance(ncff, ncfo, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# external-financing reliance over 63d, z-scored vs 252d history (de-trended)
def f30fd_f30_financing_dependence_extrelz_63d_base_v003_signal(ncff, ncfo):
    r = _f30_ext_reliance(ncff, ncfo, 63)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing-to-operating ratio (signed): how big financing flow is vs operating flow
def f30fd_f30_financing_dependence_ncffovncfo_252d_base_v004_signal(ncff, ncfo):
    b = _safe_div(_mean(ncff, 252), _mean(ncfo.abs(), 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing-funded-burn coverage: financing inflow over operating burn, 252d
def f30fd_f30_financing_dependence_burncov_252d_base_v005_signal(ncff, ncfo):
    b = _f30_burn_cover(ncff, ncfo, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing-funded-burn coverage over 126d
def f30fd_f30_financing_dependence_burncov_126d_base_v006_signal(ncff, ncfo):
    b = _f30_burn_cover(ncff, ncfo, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding gap (free cash before financing) over 252d
def f30fd_f30_financing_dependence_selffund_252d_base_v007_signal(ncfo, ncfi):
    b = _f30_self_fund_gap(ncfo, ncfi, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding gap over 126d
def f30fd_f30_financing_dependence_selffund_126d_base_v008_signal(ncfo, ncfi):
    b = _f30_self_fund_gap(ncfo, ncfi, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-vs-debt financing mix over 252d (+1 equity-funded, -1 debt-funded)
def f30fd_f30_financing_dependence_eqdebtmix_252d_base_v009_signal(ncfcommon, ncfdebt):
    b = _f30_equity_debt_mix(ncfcommon, ncfdebt, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-vs-debt financing mix over 126d
def f30fd_f30_financing_dependence_eqdebtmix_126d_base_v010_signal(ncfcommon, ncfdebt):
    b = _f30_equity_debt_mix(ncfcommon, ncfdebt, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# raise persistence: current consecutive-inflow run length weighted by inflow size,
# smoothed -- how durably financing has been a net source of cash
def f30fd_f30_financing_dependence_raiseint_252d_base_v011_signal(ncff):
    pos = (ncff > 0).astype(float)
    grp = (pos != pos.shift()).cumsum()
    run = pos.groupby(grp).cumsum()
    sc = _mean(ncff.abs(), 252).replace(0, np.nan)
    weighted = run * (ncff.clip(lower=0) / sc)
    b = weighted.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-raise intensity over 63d
def f30fd_f30_financing_dependence_raiseint_63d_base_v012_signal(ncff):
    b = _f30_raise_intensity(ncff, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity issuance reliance: positive ncfcommon (raises) vs operating engine, 252d
def f30fd_f30_financing_dependence_eqraise_252d_base_v013_signal(ncfcommon, ncfo):
    raise_ = _mean(ncfcommon.clip(lower=0), 252)
    eng = (_mean(ncfcommon.abs(), 252) + _mean(ncfo.abs(), 252)).replace(0, np.nan)
    b = raise_ / eng
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt issuance reliance: positive ncfdebt (draws) vs operating engine, 252d
def f30fd_f30_financing_dependence_debtdraw_252d_base_v014_signal(ncfdebt, ncfo):
    draw = _mean(ncfdebt.clip(lower=0), 252)
    eng = (_mean(ncfdebt.abs(), 252) + _mean(ncfo.abs(), 252)).replace(0, np.nan)
    b = draw / eng
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing impulse asymmetry: skewness-style tilt of daily financing over 252d
# (are financing days dominated by a few big inflows vs steady outflows?)
def f30fd_f30_financing_dependence_ncfflevel_252d_base_v015_signal(ncff):
    sc = _std(ncff, 252).replace(0, np.nan)
    centered = ncff - _mean(ncff, 252)
    b = _mean((centered / sc) ** 3, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# investing intensity vs financing: how much financing funds investing (-ncfi)
def f30fd_f30_financing_dependence_invfund_252d_base_v016_signal(ncff, ncfi):
    invest = _mean((-ncfi).clip(lower=0), 252)
    fin = _mean(ncff.clip(lower=0), 252).replace(0, np.nan)
    b = invest / fin
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# external dependence composite: (financing inflow) over (burn + investing need), 252d
def f30fd_f30_financing_dependence_extdep_252d_base_v017_signal(ncff, ncfo, ncfi):
    need = (_mean((-ncfo).clip(lower=0), 252) + _mean((-ncfi).clip(lower=0), 252)).replace(0, np.nan)
    inflow = _mean(ncff.clip(lower=0), 252)
    b = inflow / need
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding gap z-scored vs its own 252d history (de-trended funding stress)
def f30fd_f30_financing_dependence_selffundz_126d_base_v018_signal(ncfo, ncfi):
    g = _f30_self_fund_gap(ncfo, ncfi, 126)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-debt mix z-scored vs 252d history (shifting funding regime)
def f30fd_f30_financing_dependence_eqdebtmixz_126d_base_v019_signal(ncfcommon, ncfdebt):
    m = _f30_equity_debt_mix(ncfcommon, ncfdebt, 126)
    b = _z(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reliance rank: external reliance percentile vs its own 252d history
def f30fd_f30_financing_dependence_extrelrank_252d_base_v020_signal(ncff, ncfo):
    r = _f30_ext_reliance(ncff, ncfo, 63)
    b = _rank(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net external financing dependence: ncff vs free cash before financing, 252d
def f30fd_f30_financing_dependence_netextdep_252d_base_v021_signal(ncff, ncfo, ncfi):
    fcf_pre = _mean(ncfo + ncfi, 252)
    fin = _mean(ncff, 252)
    b = (fin - fcf_pre) / (fin.abs() + fcf_pre.abs()).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing flow momentum: change in 63d-mean financing over a quarter
def f30fd_f30_financing_dependence_ncffmom_63d_base_v022_signal(ncff):
    m = _mean(ncff, 63)
    sc = _mean(ncff.abs(), 252).replace(0, np.nan)
    b = (m - m.shift(63)) / sc
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-self-sufficiency: operating cash vs total cash needs (signed), 252d
def f30fd_f30_financing_dependence_opsuff_252d_base_v023_signal(ncfo, ncfi, ncff):
    o = _mean(ncfo, 252)
    tot = (_mean(ncfo.abs(), 252) + _mean(ncfi.abs(), 252) + _mean(ncff.abs(), 252)).replace(0, np.nan)
    b = o / tot
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-issuance lumpiness: peak monthly equity inflow vs median monthly, 252d
# (one-off secondary offerings vs steady ATM issuance)
def f30fd_f30_financing_dependence_eqraisestreak_252d_base_v024_signal(ncfcommon):
    monthly = _mean(ncfcommon.clip(lower=0), 21)
    peak = monthly.rolling(252, min_periods=126).max()
    med = monthly.rolling(252, min_periods=126).median().replace(0, np.nan)
    b = np.log1p(peak / med)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-flow persistence: lag-21 autocorrelation of debt cash flow over 252d
# (sticky borrowing programs vs one-off draws that quickly reverse)
def f30fd_f30_financing_dependence_debtdrawstreak_252d_base_v025_signal(ncfdebt):
    x = ncfdebt - _mean(ncfdebt, 252)
    xl = x.shift(21)
    cov = _mean(x * xl, 252)
    denom = _std(ncfdebt, 252).replace(0, np.nan) ** 2
    b = cov / denom
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing-regime instability: sign flips in financing flow weighted by the size
# of the swing across each flip, smoothed (magnitude-aware toggling), 252d
def f30fd_f30_financing_dependence_finposstreak_252d_base_v026_signal(ncff):
    sgn = np.sign(ncff)
    flip = (sgn != sgn.shift(1)).astype(float)
    sc = _mean(ncff.abs(), 252).replace(0, np.nan)
    swing = (ncff - ncff.shift(1)).abs() / sc
    b = (flip * swing).rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# funding-gap streak: fraction of last year free-cash-before-financing was negative
def f30fd_f30_financing_dependence_gapstreak_252d_base_v027_signal(ncfo, ncfi):
    gap = (ncfo + ncfi < 0).astype(float)
    b = gap.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing inflow-vs-outflow magnitude asymmetry: signed sqrt of (raise minus
# return) scaled by total financing turnover -- net capital posture, 63d short window
def f30fd_f30_financing_dependence_finsignmag_252d_base_v028_signal(ncff, ncfo):
    raise_ = _mean(ncff.clip(lower=0), 63)
    ret = _mean((-ncff).clip(lower=0), 63)
    sc = _mean(ncff.abs() + ncfo.abs(), 63).replace(0, np.nan)
    r = (raise_ - ret) / sc
    b = np.sign(r) * (r.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# raise co-occurrence: fraction of months BOTH equity and debt were tapped together
# (multi-source funding scramble) weighted by combined magnitude, 252d
def f30fd_f30_financing_dependence_raisespread_252d_base_v029_signal(ncfcommon, ncfdebt):
    both = ((ncfcommon > 0) & (ncfdebt > 0)).astype(float)
    rate = both.rolling(252, min_periods=126).mean()
    mag = _mean(ncfcommon.clip(lower=0) + ncfdebt.clip(lower=0), 63)
    sc = _mean(ncfcommon.abs() + ncfdebt.abs(), 252).replace(0, np.nan)
    b = rate * (mag / sc)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dependence dispersion: variability of monthly financing reliance over a year
def f30fd_f30_financing_dependence_reldisp_252d_base_v030_signal(ncff, ncfo):
    r = _f30_ext_reliance(ncff, ncfo, 21)
    b = _std(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative net external draw: how many of the last 252 days were financing-positive
# while operating was negative (financing actively plugging operating holes)
def f30fd_f30_financing_dependence_cumextdep_252d_base_v031_signal(ncff, ncfo):
    plug = ((ncff > 0) & (ncfo < 0)).astype(float)
    rate = plug.rolling(252, min_periods=126).mean()
    depth = _safe_div(_sum(ncff.clip(lower=0), 252), _sum((-ncfo).clip(lower=0), 252))
    b = rate * np.tanh(depth)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-vs-equity activity tilt: which lever shows MORE gross turnover (not net), 252d
def f30fd_f30_financing_dependence_debttilt_252d_base_v032_signal(ncfdebt, ncfcommon):
    dturn = _mean(ncfdebt.abs(), 252)
    eturn = _mean(ncfcommon.abs(), 252)
    b = (dturn - eturn) / (dturn + eturn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn-cover momentum: change in financing burn-coverage over a quarter
def f30fd_f30_financing_dependence_burncovmom_126d_base_v033_signal(ncff, ncfo):
    c = _f30_burn_cover(ncff, ncfo, 126)
    b = c - c.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing reliance regime distance: current reliance minus its 252d median proxy
def f30fd_f30_financing_dependence_reldist_252d_base_v034_signal(ncff, ncfo):
    r = _f30_ext_reliance(ncff, ncfo, 63)
    med = r.rolling(252, min_periods=126).median()
    b = r - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total external capital pulled (equity+debt raises) vs operating, 252d
def f30fd_f30_financing_dependence_totraise_252d_base_v035_signal(ncfcommon, ncfdebt, ncfo):
    raises = _mean(ncfcommon.clip(lower=0) + ncfdebt.clip(lower=0), 252)
    eng = (raises.abs() + _mean(ncfo.abs(), 252)).replace(0, np.nan)
    b = raises / eng
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing offset of investing: does financing track investing outflows? 252d ratio
def f30fd_f30_financing_dependence_finvsinv_252d_base_v036_signal(ncff, ncfi):
    f = _mean(ncff, 252)
    i = _mean(-ncfi, 252)
    b = f / (f.abs() + i.abs()).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding gap interaction with raise intensity (gap-while-raising = dependence)
def f30fd_f30_financing_dependence_gapraise_252d_base_v037_signal(ncfo, ncfi, ncff):
    gap = (-(ncfo + ncfi)).clip(lower=0)
    raise_ = ncff.clip(lower=0)
    b = _safe_div(_mean(gap, 252), _mean(gap, 252) + _mean(raise_, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity raise magnitude z vs own 252d history (issuance spikes)
def f30fd_f30_financing_dependence_eqraisez_63d_base_v038_signal(ncfcommon):
    m = _mean(ncfcommon.clip(lower=0), 63)
    b = _z(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt draw magnitude z vs own 252d history (borrowing spikes)
def f30fd_f30_financing_dependence_debtdrawz_63d_base_v039_signal(ncfdebt):
    m = _mean(ncfdebt.clip(lower=0), 63)
    b = _z(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net financing vs net pre-financing cash: dependence sign over 126d
def f30fd_f30_financing_dependence_netdep_126d_base_v040_signal(ncff, ncfo, ncfi):
    fin = _mean(ncff, 126)
    pre = _mean(ncfo + ncfi, 126)
    b = np.tanh(_safe_div(fin, pre.abs() + _mean(ncff.abs(), 126)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing turnover (gross activity) normalized, 252d
def f30fd_f30_financing_dependence_finturn_252d_base_v041_signal(ncff, ncfo):
    turn = _mean(ncff.abs(), 252)
    base = _mean(ncfo.abs(), 252).replace(0, np.nan)
    b = turn / base
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-funded burn: equity inflow over operating burn, 252d
def f30fd_f30_financing_dependence_eqburn_252d_base_v042_signal(ncfcommon, ncfo):
    eq = _mean(ncfcommon.clip(lower=0), 252)
    burn = _mean((-ncfo).clip(lower=0), 252).replace(0, np.nan)
    b = eq / burn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-funded burn: debt draw over operating burn, 252d
def f30fd_f30_financing_dependence_debtburn_252d_base_v043_signal(ncfdebt, ncfo):
    dr = _mean(ncfdebt.clip(lower=0), 252)
    burn = _mean((-ncfo).clip(lower=0), 252).replace(0, np.nan)
    b = dr / burn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing reliance acceleration-as-level: 63d reliance minus 252d reliance
def f30fd_f30_financing_dependence_relshift_base_v044_signal(ncff, ncfo):
    short = _f30_ext_reliance(ncff, ncfo, 63)
    long = _f30_ext_reliance(ncff, ncfo, 252)
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-debt mix dispersion: variability of mix over a year (funding indecision)
def f30fd_f30_financing_dependence_mixdisp_252d_base_v045_signal(ncfcommon, ncfdebt):
    m = _f30_equity_debt_mix(ncfcommon, ncfdebt, 21)
    b = _std(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-raise dependence rank vs 504d history (long-horizon percentile)
def f30fd_f30_financing_dependence_raiserank_504d_base_v046_signal(ncff):
    r = _f30_raise_intensity(ncff, 63)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-vs-investing balance dispersion: how variable the (ncfo+ncfi) net is
# relative to its level -- coefficient-of-variation of pre-financing free cash, 252d
def f30fd_f30_financing_dependence_opcovinv_252d_base_v047_signal(ncfo, ncfi):
    pre = ncfo + ncfi
    sd = _std(pre, 252)
    sc = _mean(pre.abs(), 252).replace(0, np.nan)
    b = sd / sc
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing inflow concentration: largest-month inflow vs annual inflow (lumpy raises)
def f30fd_f30_financing_dependence_raiseconc_252d_base_v048_signal(ncff):
    monthly = _mean(ncff.clip(lower=0), 21)
    peak = monthly.rolling(252, min_periods=126).max()
    avg = monthly.rolling(252, min_periods=126).mean().replace(0, np.nan)
    b = peak / avg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net debt-flow momentum: 63d change in debt share of financing turnover, 252d
# (rotation toward/away from debt as the marginal lever)
def f30fd_f30_financing_dependence_netdebtflow_252d_base_v049_signal(ncfdebt, ncff):
    share = _safe_div(_mean(ncfdebt, 63), _mean(ncff.abs(), 63))
    b = share - share.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-flow lead vs total financing: 63d change in equity share of financing
# (rotation INTO or OUT OF equity as the marginal funding source)
def f30fd_f30_financing_dependence_neteqflow_252d_base_v050_signal(ncfcommon, ncff):
    share = _safe_div(_mean(ncfcommon, 63), _mean(ncff.abs(), 63))
    b = share - share.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dependence vs self-funding crossover: reliance minus operating self-sufficiency
def f30fd_f30_financing_dependence_crossover_252d_base_v051_signal(ncff, ncfo, ncfi):
    rel = _f30_ext_reliance(ncff, ncfo, 252)
    o = _mean(ncfo, 252)
    tot = (_mean(ncfo.abs(), 252) + _mean(ncfi.abs(), 252)).replace(0, np.nan)
    suff = o / tot
    b = rel - suff
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing flow yoy change: 63d-mean financing now vs a year ago
def f30fd_f30_financing_dependence_finyoy_base_v052_signal(ncff):
    m = _mean(ncff, 63)
    sc = _mean(ncff.abs(), 252).replace(0, np.nan)
    b = (m - m.shift(252)) / sc
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-debt mix slope: how mix shifted over a quarter (rotating toward equity/debt)
def f30fd_f30_financing_dependence_mixslope_126d_base_v053_signal(ncfcommon, ncfdebt):
    m = _f30_equity_debt_mix(ncfcommon, ncfdebt, 126)
    b = m - m.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stressed-reliance regime distance: how far current funding-gap-weighted reliance
# sits above its own 252d 75th-percentile (tail dependence flag)
def f30fd_f30_financing_dependence_reldepgap_252d_base_v054_signal(ncff, ncfo, ncfi):
    gap = (-(ncfo + ncfi)).clip(lower=0)
    gnorm = _safe_div(_mean(gap, 63), _mean((ncfo + ncfi).abs(), 63))
    raise_ = _safe_div(_mean(ncff.clip(lower=0), 63), _mean(ncff.abs(), 63))
    stress = gnorm * raise_
    hi = stress.rolling(252, min_periods=126).quantile(0.75)
    b = stress - hi
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of cash needs met externally: financing inflow / (financing + operating inflow)
def f30fd_f30_financing_dependence_extfrac_252d_base_v055_signal(ncff, ncfo):
    fin = _mean(ncff.clip(lower=0), 252)
    op = _mean(ncfo.clip(lower=0), 252)
    b = fin / (fin + op).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# repayment-vs-draw imbalance: net debt repayment days minus draw days, 252d
# (deleveraging regime when negative-flow days dominate)
def f30fd_f30_financing_dependence_repay_252d_base_v056_signal(ncfdebt, ncfo):
    repay_d = (ncfdebt < 0).astype(float).rolling(252, min_periods=126).mean()
    draw_d = (ncfdebt > 0).astype(float).rolling(252, min_periods=126).mean()
    intensity = _safe_div(_mean((-ncfdebt).clip(lower=0), 252), _mean(ncfo.abs(), 63))
    b = (repay_d - draw_d) * np.tanh(intensity)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback intensity: net equity outflow (negative ncfcommon) vs operating, 252d
def f30fd_f30_financing_dependence_buyback_252d_base_v057_signal(ncfcommon, ncfo):
    bb = _mean((-ncfcommon).clip(lower=0), 252)
    op = _mean(ncfo.abs(), 252).replace(0, np.nan)
    b = bb / op
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding gap momentum over 126d (improving/worsening funding position)
def f30fd_f30_financing_dependence_gapmom_126d_base_v058_signal(ncfo, ncfi):
    g = _f30_self_fund_gap(ncfo, ncfi, 126)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing-investing synchrony: 252d rolling correlation between financing inflow
# bursts and investing outflow bursts (raising right when spending = funded growth)
def f30fd_f30_financing_dependence_invcov_252d_base_v059_signal(ncff, ncfi):
    f = ncff.clip(lower=0)
    sp = (-ncfi).clip(lower=0)
    fc = f - _mean(f, 252)
    sc = sp - _mean(sp, 252)
    cov = _mean(fc * sc, 252)
    denom = (_std(f, 252) * _std(sp, 252)).replace(0, np.nan)
    b = cov / denom
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# raise frequency: count of months with material equity OR debt inflow over a year
def f30fd_f30_financing_dependence_raisefreq_252d_base_v060_signal(ncfcommon, ncfdebt):
    raised = ((ncfcommon > 0) | (ncfdebt > 0)).astype(float)
    b = raised.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dependence stability: 126d reliance smoothed (persistent funding regime)
def f30fd_f30_financing_dependence_relema_126d_base_v061_signal(ncff, ncfo):
    r = _f30_ext_reliance(ncff, ncfo, 63)
    b = r.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reliance displacement: short reliance minus its own slow EMA
def f30fd_f30_financing_dependence_reldisp2_base_v062_signal(ncff, ncfo):
    r = _f30_ext_reliance(ncff, ncfo, 63)
    b = r - r.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-vs-financing lead/lag: 63d correlation between operating and financing
# flows (negative = financing offsets operating swings -> dependence; positive = co-move)
def f30fd_f30_financing_dependence_opsharein_252d_base_v063_signal(ncfo, ncff):
    o = ncfo - _mean(ncfo, 63)
    f = ncff - _mean(ncff, 63)
    cov = _mean(o * f, 252)
    denom = (_std(ncfo, 252) * _std(ncff, 252)).replace(0, np.nan)
    b = cov / denom
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing draw vs investing build: net (ncff + ncfi) normalized, 252d
def f30fd_f30_financing_dependence_fininvnet_252d_base_v064_signal(ncff, ncfi):
    net = _mean(ncff + ncfi, 252)
    sc = (_mean(ncff.abs(), 252) + _mean(ncfi.abs(), 252)).replace(0, np.nan)
    b = net / sc
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-raise dependence rank vs 504d (how unusual current equity reliance is)
def f30fd_f30_financing_dependence_eqdeprank_504d_base_v065_signal(ncfcommon, ncfo):
    raise_ = _mean(ncfcommon.clip(lower=0), 63)
    eng = _mean(ncfo.abs(), 63).replace(0, np.nan)
    r = raise_ / eng
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-flow countercyclicality: 252d correlation between debt cash flow and operating
# cash flow -- negative = borrowing rises when operations weaken (defensive leverage)
def f30fd_f30_financing_dependence_debtopcov_252d_base_v066_signal(ncfo, ncfdebt):
    o = ncfo - _mean(ncfo, 252)
    d = ncfdebt - _mean(ncfdebt, 252)
    cov = _mean(o * d, 252)
    denom = (_std(ncfo, 252) * _std(ncfdebt, 252)).replace(0, np.nan)
    b = cov / denom
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# war-chest build: net overfunding (financing inflow minus pre-financing deficit)
# z-scored vs its own 252d history -- unusual raise-ahead-of-need episodes
def f30fd_f30_financing_dependence_totburncov_252d_base_v067_signal(ncff, ncfo, ncfi):
    deficit = (-(ncfo + ncfi)).clip(lower=0)
    over = _mean(ncff.clip(lower=0), 63) - _mean(deficit, 63)
    b = _z(over, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing volatility: 63d financing flow vol scaled by operating scale (lumpy raises)
def f30fd_f30_financing_dependence_finvol_252d_base_v068_signal(ncff, ncfo):
    v = _std(ncff, 63)
    sc = _mean(ncfo.abs(), 252).replace(0, np.nan)
    b = _mean(v, 252) / sc
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding gap percentile rank vs 504d history (deep-deficit regime flag)
def f30fd_f30_financing_dependence_gaprank_504d_base_v069_signal(ncfo, ncfi):
    g = _f30_self_fund_gap(ncfo, ncfi, 63)
    b = _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-debt mix regime distance: mix minus 504d median (structural funding tilt)
def f30fd_f30_financing_dependence_mixdist_504d_base_v070_signal(ncfcommon, ncfdebt):
    m = _f30_equity_debt_mix(ncfcommon, ncfdebt, 63)
    med = m.rolling(504, min_periods=252).median()
    b = m - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing reliance YoY change (structural increase in external dependence)
def f30fd_f30_financing_dependence_relyoy_base_v071_signal(ncff, ncfo):
    r = _f30_ext_reliance(ncff, ncfo, 126)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-issuance sign x magnitude across both levers, 252d
def f30fd_f30_financing_dependence_issuesignmag_252d_base_v072_signal(ncfcommon, ncfdebt):
    net = _mean(ncfcommon + ncfdebt, 252)
    sc = (_mean(ncfcommon.abs(), 252) + _mean(ncfdebt.abs(), 252)).replace(0, np.nan)
    r = net / sc
    b = np.sign(r) * (r.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# investing-funded-by-financing streak: fraction of year financing+investing co-move
def f30fd_f30_financing_dependence_finivstreak_252d_base_v073_signal(ncff, ncfi):
    co = ((ncff > 0) & (ncfi < 0)).astype(float)
    b = co.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding strength regime: fraction of last year operating ALONE covered both
# investing and financing outflows (truly self-sufficient days), minus baseline
def f30fd_f30_financing_dependence_selfstr_252d_base_v074_signal(ncfo, ncff, ncfi):
    outflow = (-ncfi).clip(lower=0) + (-ncff).clip(lower=0)
    covered = (ncfo.clip(lower=0) >= outflow).astype(float)
    b = covered.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dependence composite balance: (raises - buybacks/repay) vs operating, 252d signed
def f30fd_f30_financing_dependence_balance_252d_base_v075_signal(ncfcommon, ncfdebt, ncfo):
    raises = _mean(ncfcommon.clip(lower=0) + ncfdebt.clip(lower=0), 252)
    returns = _mean((-ncfcommon).clip(lower=0) + (-ncfdebt).clip(lower=0), 252)
    net = raises - returns
    op = _mean(ncfo.abs(), 252).replace(0, np.nan)
    b = net / op
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f30fd_f30_financing_dependence_extrel_252d_base_v001_signal,
    f30fd_f30_financing_dependence_extrel_126d_base_v002_signal,
    f30fd_f30_financing_dependence_extrelz_63d_base_v003_signal,
    f30fd_f30_financing_dependence_ncffovncfo_252d_base_v004_signal,
    f30fd_f30_financing_dependence_burncov_252d_base_v005_signal,
    f30fd_f30_financing_dependence_burncov_126d_base_v006_signal,
    f30fd_f30_financing_dependence_selffund_252d_base_v007_signal,
    f30fd_f30_financing_dependence_selffund_126d_base_v008_signal,
    f30fd_f30_financing_dependence_eqdebtmix_252d_base_v009_signal,
    f30fd_f30_financing_dependence_eqdebtmix_126d_base_v010_signal,
    f30fd_f30_financing_dependence_raiseint_252d_base_v011_signal,
    f30fd_f30_financing_dependence_raiseint_63d_base_v012_signal,
    f30fd_f30_financing_dependence_eqraise_252d_base_v013_signal,
    f30fd_f30_financing_dependence_debtdraw_252d_base_v014_signal,
    f30fd_f30_financing_dependence_ncfflevel_252d_base_v015_signal,
    f30fd_f30_financing_dependence_invfund_252d_base_v016_signal,
    f30fd_f30_financing_dependence_extdep_252d_base_v017_signal,
    f30fd_f30_financing_dependence_selffundz_126d_base_v018_signal,
    f30fd_f30_financing_dependence_eqdebtmixz_126d_base_v019_signal,
    f30fd_f30_financing_dependence_extrelrank_252d_base_v020_signal,
    f30fd_f30_financing_dependence_netextdep_252d_base_v021_signal,
    f30fd_f30_financing_dependence_ncffmom_63d_base_v022_signal,
    f30fd_f30_financing_dependence_opsuff_252d_base_v023_signal,
    f30fd_f30_financing_dependence_eqraisestreak_252d_base_v024_signal,
    f30fd_f30_financing_dependence_debtdrawstreak_252d_base_v025_signal,
    f30fd_f30_financing_dependence_finposstreak_252d_base_v026_signal,
    f30fd_f30_financing_dependence_gapstreak_252d_base_v027_signal,
    f30fd_f30_financing_dependence_finsignmag_252d_base_v028_signal,
    f30fd_f30_financing_dependence_raisespread_252d_base_v029_signal,
    f30fd_f30_financing_dependence_reldisp_252d_base_v030_signal,
    f30fd_f30_financing_dependence_cumextdep_252d_base_v031_signal,
    f30fd_f30_financing_dependence_debttilt_252d_base_v032_signal,
    f30fd_f30_financing_dependence_burncovmom_126d_base_v033_signal,
    f30fd_f30_financing_dependence_reldist_252d_base_v034_signal,
    f30fd_f30_financing_dependence_totraise_252d_base_v035_signal,
    f30fd_f30_financing_dependence_finvsinv_252d_base_v036_signal,
    f30fd_f30_financing_dependence_gapraise_252d_base_v037_signal,
    f30fd_f30_financing_dependence_eqraisez_63d_base_v038_signal,
    f30fd_f30_financing_dependence_debtdrawz_63d_base_v039_signal,
    f30fd_f30_financing_dependence_netdep_126d_base_v040_signal,
    f30fd_f30_financing_dependence_finturn_252d_base_v041_signal,
    f30fd_f30_financing_dependence_eqburn_252d_base_v042_signal,
    f30fd_f30_financing_dependence_debtburn_252d_base_v043_signal,
    f30fd_f30_financing_dependence_relshift_base_v044_signal,
    f30fd_f30_financing_dependence_mixdisp_252d_base_v045_signal,
    f30fd_f30_financing_dependence_raiserank_504d_base_v046_signal,
    f30fd_f30_financing_dependence_opcovinv_252d_base_v047_signal,
    f30fd_f30_financing_dependence_raiseconc_252d_base_v048_signal,
    f30fd_f30_financing_dependence_netdebtflow_252d_base_v049_signal,
    f30fd_f30_financing_dependence_neteqflow_252d_base_v050_signal,
    f30fd_f30_financing_dependence_crossover_252d_base_v051_signal,
    f30fd_f30_financing_dependence_finyoy_base_v052_signal,
    f30fd_f30_financing_dependence_mixslope_126d_base_v053_signal,
    f30fd_f30_financing_dependence_reldepgap_252d_base_v054_signal,
    f30fd_f30_financing_dependence_extfrac_252d_base_v055_signal,
    f30fd_f30_financing_dependence_repay_252d_base_v056_signal,
    f30fd_f30_financing_dependence_buyback_252d_base_v057_signal,
    f30fd_f30_financing_dependence_gapmom_126d_base_v058_signal,
    f30fd_f30_financing_dependence_invcov_252d_base_v059_signal,
    f30fd_f30_financing_dependence_raisefreq_252d_base_v060_signal,
    f30fd_f30_financing_dependence_relema_126d_base_v061_signal,
    f30fd_f30_financing_dependence_reldisp2_base_v062_signal,
    f30fd_f30_financing_dependence_opsharein_252d_base_v063_signal,
    f30fd_f30_financing_dependence_fininvnet_252d_base_v064_signal,
    f30fd_f30_financing_dependence_eqdeprank_504d_base_v065_signal,
    f30fd_f30_financing_dependence_debtopcov_252d_base_v066_signal,
    f30fd_f30_financing_dependence_totburncov_252d_base_v067_signal,
    f30fd_f30_financing_dependence_finvol_252d_base_v068_signal,
    f30fd_f30_financing_dependence_gaprank_504d_base_v069_signal,
    f30fd_f30_financing_dependence_mixdist_504d_base_v070_signal,
    f30fd_f30_financing_dependence_relyoy_base_v071_signal,
    f30fd_f30_financing_dependence_issuesignmag_252d_base_v072_signal,
    f30fd_f30_financing_dependence_finivstreak_252d_base_v073_signal,
    f30fd_f30_financing_dependence_selfstr_252d_base_v074_signal,
    f30fd_f30_financing_dependence_balance_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F30_FINANCING_DEPENDENCE_REGISTRY_001_075 = REGISTRY


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
    # allow_neg=True) and made to GENUINELY swing sign: each _fund level is centered
    # by its own rolling mean (net issuance vs repayment) plus a cyclical funding-cycle
    # component, so positive inflows and negative outflows both occur ~half the time.
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

    print("OK f30_financing_dependence_base_001_075_claude: %d features pass" % n_features)
