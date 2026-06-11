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
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _slope(s, w):
    # OLS slope of s vs time over a rolling window (per-step); handles partial windows
    def _f(a):
        m = len(a)
        idx = np.arange(m, dtype=float)
        idx = idx - idx.mean()
        denom = (idx ** 2).sum()
        if denom == 0:
            return np.nan
        return float(np.dot(idx, a) / denom)

    return s.rolling(w, min_periods=max(2, w // 2)).apply(_f, raw=True)


# ===== folder domain primitives (cash flow quality) =====
def _f32_fcf_margin(fcf, revenue):
    return fcf / revenue.replace(0, np.nan)


def _f32_ocf_margin(ncfo, revenue):
    return ncfo / revenue.replace(0, np.nan)


def _f32_cash_conv(ncfo, netinc):
    return ncfo / netinc.replace(0, np.nan)


def _f32_capex_cover(ncfo, capex):
    return ncfo / capex.replace(0, np.nan)


def _f32_capex_intensity(capex, revenue):
    return capex / revenue.replace(0, np.nan)


def _f32_selffund_balance(ncfo, capex):
    return (ncfo - capex) / (ncfo.abs() + capex).replace(0, np.nan)


# ============================================================
# FCF margin level over a half-year (mid-horizon cash quality)
def f32cf_f32_cash_flow_quality_fcfmargin_126d_base_v076_signal(fcf, revenue):
    b = _mean(_f32_fcf_margin(fcf, revenue), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin z-scored vs its own 126d history (mid-horizon extremity)
def f32cf_f32_cash_flow_quality_fcfmarginz_126d_base_v077_signal(fcf, revenue):
    b = _z(_f32_fcf_margin(fcf, revenue), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF margin over a half-year
def f32cf_f32_cash_flow_quality_ocfmargin_126d_base_v078_signal(ncfo, revenue):
    b = _mean(_f32_ocf_margin(ncfo, revenue), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin short minus long horizon (cash-quality term structure)
def f32cf_f32_cash_flow_quality_fcfmgnterm_base_v079_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue)
    b = _mean(m, 63) - _mean(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF margin short minus long horizon (operating-cash term structure)
def f32cf_f32_cash_flow_quality_ocfmgnterm_base_v080_signal(ncfo, revenue):
    m = _f32_ocf_margin(ncfo, revenue)
    b = _mean(m, 63) - _mean(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash conversion (ncfo/netinc) over a half-year
def f32cf_f32_cash_flow_quality_cashconv_126d_base_v081_signal(ncfo, netinc):
    b = _mean(_f32_cash_conv(ncfo, netinc).clip(-5, 5), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash conversion deviation from its own 252d mean (conversion drift)
def f32cf_f32_cash_flow_quality_convdev_252d_base_v082_signal(ncfo, netinc):
    c = _f32_cash_conv(ncfo, netinc).clip(-5, 5)
    b = c - _mean(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual gap (netinc-ncfo) normalized by revenue over a half-year
def f32cf_f32_cash_flow_quality_accrual_126d_base_v083_signal(netinc, ncfo, revenue):
    raw = (netinc - ncfo) / revenue.replace(0, np.nan)
    b = _mean(raw, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual gap trend: slope of (netinc-ncfo)/revenue over a half-year (worsening quality)
def f32cf_f32_cash_flow_quality_accrualtrend_126d_base_v084_signal(netinc, ncfo, revenue):
    raw = (netinc - ncfo) / revenue.replace(0, np.nan)
    b = _slope(raw, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual gap percentile rank vs 504d history (cross-time accrual extremity)
def f32cf_f32_cash_flow_quality_accrualrank_504d_base_v085_signal(netinc, ncfo, revenue):
    raw = (netinc - ncfo) / revenue.replace(0, np.nan)
    b = raw.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin slope over a year (long-horizon cash-quality trend)
def f32cf_f32_cash_flow_quality_fcfmgntrend_252d_base_v086_signal(fcf, revenue):
    b = _slope(_f32_fcf_margin(fcf, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF margin slope over a year
def f32cf_f32_cash_flow_quality_ocfmgntrend_252d_base_v087_signal(ncfo, revenue):
    b = _slope(_f32_ocf_margin(ncfo, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding balance level over a year (durable FCF generation)
def f32cf_f32_cash_flow_quality_selffundbal_252d_base_v088_signal(ncfo, capex):
    b = _mean(_f32_selffund_balance(ncfo, capex), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding balance z-scored vs own history
def f32cf_f32_cash_flow_quality_selffundbalz_252d_base_v089_signal(ncfo, capex):
    b = _z(_f32_selffund_balance(ncfo, capex), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF consistency: fraction of half-year with positive FCF
def f32cf_f32_cash_flow_quality_fcfposfrac_126d_base_v090_signal(fcf):
    pos = (fcf > 0).astype(float)
    frac = pos.rolling(126, min_periods=63).mean()
    drift = pos.rolling(21, min_periods=10).mean() - frac
    b = frac + 0.25 * drift
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF positive-streak length (consecutive positive operating-cash periods)
def f32cf_f32_cash_flow_quality_ocfstreak_base_v091_signal(ncfo):
    pos = (ncfo > 0).astype(float)

    def _f(a):
        c = 0
        for v in a[::-1]:
            if v > 0:
                c += 1
            else:
                break
        return c / float(len(a))

    b = pos.rolling(126, min_periods=63).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin minus its 252d median (cash-quality vs own normal level)
def f32cf_f32_cash_flow_quality_fcfmgnmed_252d_base_v092_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue)
    b = m - m.rolling(252, min_periods=126).median()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fcfps slope over a year (long-horizon per-share cash trend)
def f32cf_f32_cash_flow_quality_fcfpstrend_252d_base_v093_signal(fcfps):
    b = _slope(fcfps, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fcfps range position within trailing year
def f32cf_f32_cash_flow_quality_fcfpsrngpos_252d_base_v094_signal(fcfps):
    sm = _mean(fcfps, 21)
    hi = sm.rolling(252, min_periods=126).max()
    lo = sm.rolling(252, min_periods=126).min()
    b = (sm - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fcfps z-scored vs 126d history (mid-horizon per-share extremity)
def f32cf_f32_cash_flow_quality_fcfpsz_126d_base_v095_signal(fcfps):
    b = _z(fcfps, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity over a year (long-horizon content/platform reinvestment)
def f32cf_f32_cash_flow_quality_capexint_252d_base_v096_signal(capex, revenue):
    b = _mean(_f32_capex_intensity(capex, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity short minus long horizon (reinvestment acceleration regime)
def f32cf_f32_cash_flow_quality_capexintterm_base_v097_signal(capex, revenue):
    ci = _f32_capex_intensity(capex, revenue)
    b = _mean(ci, 63) - _mean(ci, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex growth: log-ratio of smoothed capex over a half-year
def f32cf_f32_cash_flow_quality_capexgrowth_126d_base_v098_signal(capex):
    s = _mean(capex, 63)
    b = np.log(s.replace(0, np.nan)) - np.log(s.shift(126).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin x revenue-growth interaction (cash-backed growth quality)
def f32cf_f32_cash_flow_quality_cashgrowth_base_v099_signal(fcf, revenue):
    fm = _f32_fcf_margin(fcf, revenue)
    rg = np.log(_mean(revenue, 21).replace(0, np.nan)) - np.log(
        _mean(revenue, 21).shift(252).replace(0, np.nan))
    b = _mean(fm, 63) * rg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF margin x cash conversion interaction (joint operating-cash quality)
def f32cf_f32_cash_flow_quality_ocfconvjoint_base_v100_signal(ncfo, revenue, netinc):
    om = _f32_ocf_margin(ncfo, revenue)
    cc = _f32_cash_conv(ncfo, netinc).clip(-5, 5)
    b = _mean(om * cc, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin downside frequency: fraction of half-year FCF margin below its mean
def f32cf_f32_cash_flow_quality_fcfdownfreq_126d_base_v101_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue)
    below = (m < _mean(m, 126)).astype(float)
    frac = below.rolling(126, min_periods=63).mean()
    depth = (_mean(m, 126) - m).clip(lower=0).rolling(63, min_periods=21).mean()
    b = frac + 5.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual gap absolute magnitude smoothed (overall earnings-cash divergence)
def f32cf_f32_cash_flow_quality_accrualmag_63d_base_v102_signal(netinc, ncfo, revenue):
    raw = ((netinc - ncfo) / revenue.replace(0, np.nan)).abs()
    b = _mean(raw, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign of cash conversion (positive ncfo with positive netinc share)
def f32cf_f32_cash_flow_quality_convsign_252d_base_v103_signal(ncfo, netinc):
    both_pos = ((ncfo > 0) & (netinc > 0)).astype(float)
    frac = both_pos.rolling(252, min_periods=126).mean()
    drift = both_pos.rolling(63, min_periods=21).mean() - frac
    b = frac + 0.5 * drift
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin EMA displacement (price-style oscillator on cash quality)
def f32cf_f32_cash_flow_quality_fcfmgnosc_base_v104_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue)
    fast = m.ewm(span=21, min_periods=10).mean()
    slow = m.ewm(span=84, min_periods=42).mean()
    b = (fast - slow) / _std(m, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF margin EMA displacement oscillator
def f32cf_f32_cash_flow_quality_ocfmgnosc_base_v105_signal(ncfo, revenue):
    m = _f32_ocf_margin(ncfo, revenue)
    fast = m.ewm(span=21, min_periods=10).mean()
    slow = m.ewm(span=84, min_periods=42).mean()
    b = (fast - slow) / _std(m, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin year-over-year acceleration (annual change of annual change)
def f32cf_f32_cash_flow_quality_fcfmgnyoyaccel_base_v106_signal(fcf, revenue):
    m = _mean(_f32_fcf_margin(fcf, revenue), 21)
    yoy = m - m.shift(252)
    b = yoy - yoy.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex coverage balance rank vs 504d history (cross-time self-funding)
def f32cf_f32_cash_flow_quality_selffundrank_504d_base_v107_signal(ncfo, capex):
    bal = _f32_selffund_balance(ncfo, capex)
    b = bal.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin worst-quarter (min) over trailing year (downside cash floor)
def f32cf_f32_cash_flow_quality_fcfmgnfloor_252d_base_v108_signal(fcf, revenue):
    m = _mean(_f32_fcf_margin(fcf, revenue), 21)
    b = m.rolling(252, min_periods=126).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin best-quarter (max) over trailing year (upside cash ceiling)
def f32cf_f32_cash_flow_quality_fcfmgnceil_252d_base_v109_signal(fcf, revenue):
    m = _mean(_f32_fcf_margin(fcf, revenue), 21)
    b = m.rolling(252, min_periods=126).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin amplitude: ceiling minus floor over trailing year (cash-quality range)
def f32cf_f32_cash_flow_quality_fcfmgnamp_252d_base_v110_signal(fcf, revenue):
    m = _mean(_f32_fcf_margin(fcf, revenue), 21)
    hi = m.rolling(252, min_periods=126).max()
    lo = m.rolling(252, min_periods=126).min()
    b = hi - lo
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash conversion within-year amplitude (lumpiness of conversion)
def f32cf_f32_cash_flow_quality_convamp_252d_base_v111_signal(ncfo, netinc):
    c = _mean(_f32_cash_conv(ncfo, netinc).clip(-5, 5), 21)
    hi = c.rolling(252, min_periods=126).max()
    lo = c.rolling(252, min_periods=126).min()
    b = hi - lo
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF margin autocorrelation over a half-year (persistence of cash margin)
def f32cf_f32_cash_flow_quality_ocfmgnac_126d_base_v112_signal(ncfo, revenue):
    m = _f32_ocf_margin(ncfo, revenue)
    b = m.rolling(126, min_periods=63).apply(
        lambda a: pd.Series(a).autocorr(lag=21) if len(a) > 22 else np.nan, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-to-OCF conversion ratio level (how much OCF survives capex), smoothed
def f32cf_f32_cash_flow_quality_fcfofocf_126d_base_v113_signal(fcf, ncfo):
    r = (fcf / ncfo.replace(0, np.nan)).clip(-5, 5)
    b = _mean(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-to-OCF conversion trend over a half-year
def f32cf_f32_cash_flow_quality_fcfofocftrend_126d_base_v114_signal(fcf, ncfo):
    r = (fcf / ncfo.replace(0, np.nan)).clip(-5, 5)
    b = _slope(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net margin (netinc/revenue) smoothed (paper-profit baseline for cash comparison)
def f32cf_f32_cash_flow_quality_netmgn_63d_base_v115_signal(netinc, revenue):
    nm = netinc / revenue.replace(0, np.nan)
    b = _mean(nm, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# paper-vs-cash gap trend: slope of (netmargin - fcfmargin) over a half-year
def f32cf_f32_cash_flow_quality_papercashtrend_126d_base_v116_signal(netinc, fcf, revenue):
    gap = (netinc - fcf) / revenue.replace(0, np.nan)
    b = _slope(gap, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash conversion stability via range (high-low of conversion normalized)
def f32cf_f32_cash_flow_quality_convstabrng_252d_base_v117_signal(ncfo, netinc):
    c = _f32_cash_conv(ncfo, netinc).clip(-5, 5)
    rng = c.rolling(252, min_periods=126).max() - c.rolling(252, min_periods=126).min()
    lvl = _mean(c.abs(), 252)
    b = rng / lvl.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin sign-magnitude (compressed signed level)
def f32cf_f32_cash_flow_quality_fcfmgnsignmag_base_v118_signal(fcf, revenue):
    m = _mean(_f32_fcf_margin(fcf, revenue), 63)
    b = np.sign(m) * (m.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding balance momentum (quarter change)
def f32cf_f32_cash_flow_quality_selffundmom_63d_base_v119_signal(ncfo, capex):
    bal = _f32_selffund_balance(ncfo, capex)
    b = bal - bal.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin half-year change minus year change (cash-quality curvature)
def f32cf_f32_cash_flow_quality_fcfmgncurv_base_v120_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue)
    b = (m - m.shift(126)) - (m.shift(126) - m.shift(252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity z vs own 126d history (mid-horizon reinvestment extremity)
def f32cf_f32_cash_flow_quality_capexintz_126d_base_v121_signal(capex, revenue):
    b = _z(_f32_capex_intensity(capex, revenue), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual gap EMA displacement (accrual oscillator)
def f32cf_f32_cash_flow_quality_accrualosc_base_v122_signal(netinc, ncfo, revenue):
    raw = (netinc - ncfo) / revenue.replace(0, np.nan)
    fast = raw.ewm(span=21, min_periods=10).mean()
    slow = raw.ewm(span=84, min_periods=42).mean()
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin percentile rank vs 252d history (mid-horizon cross-time position)
def f32cf_f32_cash_flow_quality_fcfmgnrank_252d_base_v123_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue)
    b = m.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF margin minus net margin (cash superiority over paper profit)
def f32cf_f32_cash_flow_quality_ocfsupr_63d_base_v124_signal(ncfo, netinc, revenue):
    spr = (ncfo - netinc) / revenue.replace(0, np.nan)
    b = _mean(spr, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF superiority trend over a year (cash quality vs earnings improving)
def f32cf_f32_cash_flow_quality_ocfsuprtrend_252d_base_v125_signal(ncfo, netinc, revenue):
    spr = (ncfo - netinc) / revenue.replace(0, np.nan)
    b = _slope(spr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of year FCF improving quarter-over-quarter (momentum consistency)
def f32cf_f32_cash_flow_quality_fcfimprfrac_252d_base_v126_signal(fcf, revenue):
    m = _mean(_f32_fcf_margin(fcf, revenue), 21)
    impr = (m > m.shift(21)).astype(float)
    frac = impr.rolling(252, min_periods=126).mean()
    mag = (m - m.shift(21)).rolling(63, min_periods=21).mean()
    b = frac + 5.0 * mag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex coverage balance downside semi-deviation (self-funding fragility)
def f32cf_f32_cash_flow_quality_selffunddownsd_252d_base_v127_signal(ncfo, capex):
    bal = _f32_selffund_balance(ncfo, capex)
    mn = _mean(bal, 252)
    neg = (bal - mn).clip(upper=0)
    b = (neg ** 2).rolling(252, min_periods=126).mean() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF burn depth scaled by capex (how deep cash deficit relative to investment)
def f32cf_f32_cash_flow_quality_fcfburncapex_base_v128_signal(fcf, capex):
    deficit = (-fcf).clip(lower=0) / capex.replace(0, np.nan)
    b = _mean(deficit.clip(0, 20), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash conversion above-1 magnitude (excess cash backing of earnings)
def f32cf_f32_cash_flow_quality_convexcess_63d_base_v129_signal(ncfo, netinc):
    c = _f32_cash_conv(ncfo, netinc).clip(-5, 5)
    excess = (c - 1.0).clip(lower=0)
    b = _mean(excess, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin vs OCF margin ratio (capex-retention efficiency), smoothed
def f32cf_f32_cash_flow_quality_capexreten_63d_base_v130_signal(fcf, ncfo, revenue):
    fm = _f32_fcf_margin(fcf, revenue)
    om = _f32_ocf_margin(ncfo, revenue)
    r = (fm / om.replace(0, np.nan)).clip(-5, 5)
    b = _mean(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fcfps acceleration (quarter change minus prior-quarter change)
def f32cf_f32_cash_flow_quality_fcfpsaccel_base_v131_signal(fcfps):
    sm = _mean(fcfps, 21)
    d1 = sm - sm.shift(63)
    b = d1 - d1.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF margin floor over trailing year (worst operating-cash margin)
def f32cf_f32_cash_flow_quality_ocfmgnfloor_252d_base_v132_signal(ncfo, revenue):
    m = _mean(_f32_ocf_margin(ncfo, revenue), 21)
    b = m.rolling(252, min_periods=126).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual gap volatility over a year (instability of earnings-cash divergence)
def f32cf_f32_cash_flow_quality_accrualvol_252d_base_v133_signal(netinc, ncfo, revenue):
    raw = (netinc - ncfo) / revenue.replace(0, np.nan)
    b = _std(raw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin Sharpe-style: mean over std (risk-adjusted cash quality)
def f32cf_f32_cash_flow_quality_fcfmgnsharpe_252d_base_v134_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue)
    b = _mean(m, 252) / _std(m, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF margin Sharpe-style (risk-adjusted operating-cash quality)
def f32cf_f32_cash_flow_quality_ocfmgnsharpe_252d_base_v135_signal(ncfo, revenue):
    m = _f32_ocf_margin(ncfo, revenue)
    b = _mean(m, 252) / _std(m, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding balance Sharpe (risk-adjusted self-funding)
def f32cf_f32_cash_flow_quality_selffundsharpe_252d_base_v136_signal(ncfo, capex):
    bal = _f32_selffund_balance(ncfo, capex)
    b = _mean(bal, 252) / _std(bal, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF inflection persistence: fraction of year FCF margin above its trailing-year mean
def f32cf_f32_cash_flow_quality_fcfabovemean_252d_base_v137_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue)
    above = (m > _mean(m, 252)).astype(float)
    frac = above.rolling(126, min_periods=63).mean()
    drift = above.rolling(21, min_periods=10).mean() - frac
    b = frac + 0.25 * drift
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity range position within trailing year (investment-cycle position)
def f32cf_f32_cash_flow_quality_capexintrngpos_252d_base_v138_signal(capex, revenue):
    ci = _mean(_f32_capex_intensity(capex, revenue), 21)
    hi = ci.rolling(252, min_periods=126).max()
    lo = ci.rolling(252, min_periods=126).min()
    b = (ci - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash conversion vs FCF-margin interaction (quality breadth)
def f32cf_f32_cash_flow_quality_qualbreadth_base_v139_signal(ncfo, netinc, fcf, revenue):
    cc = np.sign(_f32_cash_conv(ncfo, netinc).clip(-5, 5) - 1.0)
    fm = np.sign(_f32_fcf_margin(fcf, revenue))
    b = _mean(cc + fm, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin distance from its 504d max (drawdown of cash quality)
def f32cf_f32_cash_flow_quality_fcfmgndd_504d_base_v140_signal(fcf, revenue):
    m = _mean(_f32_fcf_margin(fcf, revenue), 21)
    hi = m.rolling(504, min_periods=252).max()
    b = m - hi
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF margin distance from its 504d max (operating-cash drawdown)
def f32cf_f32_cash_flow_quality_ocfmgndd_504d_base_v141_signal(ncfo, revenue):
    m = _mean(_f32_ocf_margin(ncfo, revenue), 21)
    hi = m.rolling(504, min_periods=252).max()
    b = m - hi
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fcfps drawdown from its 504d peak (per-share cash drawdown)
def f32cf_f32_cash_flow_quality_fcfpsdd_504d_base_v142_signal(fcfps):
    sm = _mean(fcfps, 21)
    hi = sm.rolling(504, min_periods=252).max()
    b = sm - hi
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual gap sign flips count over a year (erratic earnings-cash relationship)
def f32cf_f32_cash_flow_quality_accrualflip_252d_base_v143_signal(netinc, ncfo, revenue):
    raw = (netinc - ncfo) / revenue.replace(0, np.nan)
    sgn = np.sign(raw)
    flip = (sgn != sgn.shift(1)).astype(float)
    cnt = flip.rolling(252, min_periods=126).sum()
    mag = raw.abs().rolling(63, min_periods=21).mean()
    b = cnt + 50.0 * mag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin entropy-style dispersion: std of quarterly margins over 2y
def f32cf_f32_cash_flow_quality_fcfmgndisp_504d_base_v144_signal(fcf, revenue):
    m = _mean(_f32_fcf_margin(fcf, revenue), 21)
    b = _std(m, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite: ocf-margin trend + self-funding trend (improving-cash-quality score)
def f32cf_f32_cash_flow_quality_improvecomposite_base_v145_signal(ncfo, revenue, capex):
    ot = _slope(_f32_ocf_margin(ncfo, revenue), 126)
    st = _slope(_f32_selffund_balance(ncfo, capex), 126)
    b = _z(ot, 252) + _z(st, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF generation per share scaled by FCF margin (combined per-share + efficiency)
def f32cf_f32_cash_flow_quality_perfcfeff_base_v146_signal(fcfps, fcf, revenue):
    fm = _f32_fcf_margin(fcf, revenue)
    b = _z(fcfps, 252) * np.sign(_mean(fm, 63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash conversion mean-reversion: deviation from 252d median, tanh-bounded
def f32cf_f32_cash_flow_quality_convrevert_base_v147_signal(ncfo, netinc):
    c = _f32_cash_conv(ncfo, netinc).clip(-5, 5)
    dev = c - c.rolling(252, min_periods=126).median()
    b = np.tanh(dev)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF margin acceleration (quarter change minus prior-quarter change)
def f32cf_f32_cash_flow_quality_ocfmgnaccel_base_v148_signal(ncfo, revenue):
    m = _f32_ocf_margin(ncfo, revenue)
    d1 = m - m.shift(63)
    b = d1 - d1.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding balance fraction-of-year positive + recent lift (regime, count-friendly)
def f32cf_f32_cash_flow_quality_selffundregime_252d_base_v149_signal(ncfo, capex):
    bal = _f32_selffund_balance(ncfo, capex)
    pos = (bal > 0).astype(float)
    frac = pos.rolling(252, min_periods=126).mean()
    lift = bal.rolling(63, min_periods=21).mean()
    b = frac + lift
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overall cash-quality composite: fcf-margin z + ocf-sharpe + low-accrual (capstone)
def f32cf_f32_cash_flow_quality_capstone_base_v150_signal(fcf, ncfo, revenue, netinc):
    fmz = _z(_f32_fcf_margin(fcf, revenue), 252)
    om = _f32_ocf_margin(ncfo, revenue)
    osharpe = _mean(om, 252) / _std(om, 252).replace(0, np.nan)
    acc = -_z((netinc - ncfo) / revenue.replace(0, np.nan), 252)
    b = fmz + np.tanh(osharpe) + acc
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f32cf_f32_cash_flow_quality_fcfmargin_126d_base_v076_signal,
    f32cf_f32_cash_flow_quality_fcfmarginz_126d_base_v077_signal,
    f32cf_f32_cash_flow_quality_ocfmargin_126d_base_v078_signal,
    f32cf_f32_cash_flow_quality_fcfmgnterm_base_v079_signal,
    f32cf_f32_cash_flow_quality_ocfmgnterm_base_v080_signal,
    f32cf_f32_cash_flow_quality_cashconv_126d_base_v081_signal,
    f32cf_f32_cash_flow_quality_convdev_252d_base_v082_signal,
    f32cf_f32_cash_flow_quality_accrual_126d_base_v083_signal,
    f32cf_f32_cash_flow_quality_accrualtrend_126d_base_v084_signal,
    f32cf_f32_cash_flow_quality_accrualrank_504d_base_v085_signal,
    f32cf_f32_cash_flow_quality_fcfmgntrend_252d_base_v086_signal,
    f32cf_f32_cash_flow_quality_ocfmgntrend_252d_base_v087_signal,
    f32cf_f32_cash_flow_quality_selffundbal_252d_base_v088_signal,
    f32cf_f32_cash_flow_quality_selffundbalz_252d_base_v089_signal,
    f32cf_f32_cash_flow_quality_fcfposfrac_126d_base_v090_signal,
    f32cf_f32_cash_flow_quality_ocfstreak_base_v091_signal,
    f32cf_f32_cash_flow_quality_fcfmgnmed_252d_base_v092_signal,
    f32cf_f32_cash_flow_quality_fcfpstrend_252d_base_v093_signal,
    f32cf_f32_cash_flow_quality_fcfpsrngpos_252d_base_v094_signal,
    f32cf_f32_cash_flow_quality_fcfpsz_126d_base_v095_signal,
    f32cf_f32_cash_flow_quality_capexint_252d_base_v096_signal,
    f32cf_f32_cash_flow_quality_capexintterm_base_v097_signal,
    f32cf_f32_cash_flow_quality_capexgrowth_126d_base_v098_signal,
    f32cf_f32_cash_flow_quality_cashgrowth_base_v099_signal,
    f32cf_f32_cash_flow_quality_ocfconvjoint_base_v100_signal,
    f32cf_f32_cash_flow_quality_fcfdownfreq_126d_base_v101_signal,
    f32cf_f32_cash_flow_quality_accrualmag_63d_base_v102_signal,
    f32cf_f32_cash_flow_quality_convsign_252d_base_v103_signal,
    f32cf_f32_cash_flow_quality_fcfmgnosc_base_v104_signal,
    f32cf_f32_cash_flow_quality_ocfmgnosc_base_v105_signal,
    f32cf_f32_cash_flow_quality_fcfmgnyoyaccel_base_v106_signal,
    f32cf_f32_cash_flow_quality_selffundrank_504d_base_v107_signal,
    f32cf_f32_cash_flow_quality_fcfmgnfloor_252d_base_v108_signal,
    f32cf_f32_cash_flow_quality_fcfmgnceil_252d_base_v109_signal,
    f32cf_f32_cash_flow_quality_fcfmgnamp_252d_base_v110_signal,
    f32cf_f32_cash_flow_quality_convamp_252d_base_v111_signal,
    f32cf_f32_cash_flow_quality_ocfmgnac_126d_base_v112_signal,
    f32cf_f32_cash_flow_quality_fcfofocf_126d_base_v113_signal,
    f32cf_f32_cash_flow_quality_fcfofocftrend_126d_base_v114_signal,
    f32cf_f32_cash_flow_quality_netmgn_63d_base_v115_signal,
    f32cf_f32_cash_flow_quality_papercashtrend_126d_base_v116_signal,
    f32cf_f32_cash_flow_quality_convstabrng_252d_base_v117_signal,
    f32cf_f32_cash_flow_quality_fcfmgnsignmag_base_v118_signal,
    f32cf_f32_cash_flow_quality_selffundmom_63d_base_v119_signal,
    f32cf_f32_cash_flow_quality_fcfmgncurv_base_v120_signal,
    f32cf_f32_cash_flow_quality_capexintz_126d_base_v121_signal,
    f32cf_f32_cash_flow_quality_accrualosc_base_v122_signal,
    f32cf_f32_cash_flow_quality_fcfmgnrank_252d_base_v123_signal,
    f32cf_f32_cash_flow_quality_ocfsupr_63d_base_v124_signal,
    f32cf_f32_cash_flow_quality_ocfsuprtrend_252d_base_v125_signal,
    f32cf_f32_cash_flow_quality_fcfimprfrac_252d_base_v126_signal,
    f32cf_f32_cash_flow_quality_selffunddownsd_252d_base_v127_signal,
    f32cf_f32_cash_flow_quality_fcfburncapex_base_v128_signal,
    f32cf_f32_cash_flow_quality_convexcess_63d_base_v129_signal,
    f32cf_f32_cash_flow_quality_capexreten_63d_base_v130_signal,
    f32cf_f32_cash_flow_quality_fcfpsaccel_base_v131_signal,
    f32cf_f32_cash_flow_quality_ocfmgnfloor_252d_base_v132_signal,
    f32cf_f32_cash_flow_quality_accrualvol_252d_base_v133_signal,
    f32cf_f32_cash_flow_quality_fcfmgnsharpe_252d_base_v134_signal,
    f32cf_f32_cash_flow_quality_ocfmgnsharpe_252d_base_v135_signal,
    f32cf_f32_cash_flow_quality_selffundsharpe_252d_base_v136_signal,
    f32cf_f32_cash_flow_quality_fcfabovemean_252d_base_v137_signal,
    f32cf_f32_cash_flow_quality_capexintrngpos_252d_base_v138_signal,
    f32cf_f32_cash_flow_quality_qualbreadth_base_v139_signal,
    f32cf_f32_cash_flow_quality_fcfmgndd_504d_base_v140_signal,
    f32cf_f32_cash_flow_quality_ocfmgndd_504d_base_v141_signal,
    f32cf_f32_cash_flow_quality_fcfpsdd_504d_base_v142_signal,
    f32cf_f32_cash_flow_quality_accrualflip_252d_base_v143_signal,
    f32cf_f32_cash_flow_quality_fcfmgndisp_504d_base_v144_signal,
    f32cf_f32_cash_flow_quality_improvecomposite_base_v145_signal,
    f32cf_f32_cash_flow_quality_perfcfeff_base_v146_signal,
    f32cf_f32_cash_flow_quality_convrevert_base_v147_signal,
    f32cf_f32_cash_flow_quality_ocfmgnaccel_base_v148_signal,
    f32cf_f32_cash_flow_quality_selffundregime_252d_base_v149_signal,
    f32cf_f32_cash_flow_quality_capstone_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F32_CASH_FLOW_QUALITY_REGISTRY_076_150 = REGISTRY


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
    }

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    revenue = _fund(1, base=5e8, drift=0.04, vol=0.06).rename("revenue")
    capex = _fund(2, base=4e7, drift=0.03, vol=0.10).rename("capex")
    fcf = _fund(3, base=6e7, drift=0.0, vol=0.34, allow_neg=True).rename("fcf")
    ncfo = _fund(7, base=9e7, drift=0.0, vol=0.34, allow_neg=True).rename("ncfo")
    netinc = _fund(5, base=5e7, drift=0.0, vol=0.34, allow_neg=True).rename("netinc")
    fcfps = _fund(10, base=2.0, drift=0.0, vol=0.34, allow_neg=True).rename("fcfps")

    cols = {
        "revenue": revenue, "capex": capex, "fcf": fcf, "ncfo": ncfo,
        "netinc": netinc, "fcfps": fcfps,
    }

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs %s not subset of allowlist" % (
            name, meta["inputs"])
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

    print("OK f32_cash_flow_quality_base_076_150_claude: %d features pass" % n_features)
