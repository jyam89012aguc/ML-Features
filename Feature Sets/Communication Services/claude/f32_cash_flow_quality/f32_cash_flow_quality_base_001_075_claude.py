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


def _f32_accrual_gap(netinc, ncfo):
    # earnings minus cash: positive = aggressive accruals (low quality)
    return netinc - ncfo


# ============================================================
# FCF margin level, smoothed over a quarter
def f32cf_f32_cash_flow_quality_fcfmargin_63d_base_v001_signal(fcf, revenue):
    b = _mean(_f32_fcf_margin(fcf, revenue), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin level, smoothed over a year
def f32cf_f32_cash_flow_quality_fcfmargin_252d_base_v002_signal(fcf, revenue):
    b = _mean(_f32_fcf_margin(fcf, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin z-scored vs its own 252d history (de-trended margin extremity)
def f32cf_f32_cash_flow_quality_fcfmarginz_252d_base_v003_signal(fcf, revenue):
    b = _z(_f32_fcf_margin(fcf, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF margin level, smoothed over a quarter
def f32cf_f32_cash_flow_quality_ocfmargin_63d_base_v004_signal(ncfo, revenue):
    b = _mean(_f32_ocf_margin(ncfo, revenue), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF margin level, smoothed over a year
def f32cf_f32_cash_flow_quality_ocfmargin_252d_base_v005_signal(ncfo, revenue):
    b = _mean(_f32_ocf_margin(ncfo, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF margin z-scored vs its own 252d history
def f32cf_f32_cash_flow_quality_ocfmarginz_252d_base_v006_signal(ncfo, revenue):
    b = _z(_f32_ocf_margin(ncfo, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash conversion ncfo/netinc, smoothed (earnings backed by cash)
def f32cf_f32_cash_flow_quality_cashconv_63d_base_v007_signal(ncfo, netinc):
    b = _mean(_f32_cash_conv(ncfo, netinc).clip(-5, 5), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash conversion ncfo/netinc over a year (durable conversion)
def f32cf_f32_cash_flow_quality_cashconv_252d_base_v008_signal(ncfo, netinc):
    b = _mean(_f32_cash_conv(ncfo, netinc).clip(-5, 5), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual gap (netinc - ncfo) normalized by revenue (Sloan-style accruals)
def f32cf_f32_cash_flow_quality_accrual_63d_base_v009_signal(netinc, ncfo, revenue):
    raw = _f32_accrual_gap(netinc, ncfo) / revenue.replace(0, np.nan)
    b = _mean(raw, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual gap normalized by revenue, z-scored (accrual extremity)
def f32cf_f32_cash_flow_quality_accrualz_252d_base_v010_signal(netinc, ncfo, revenue):
    raw = _f32_accrual_gap(netinc, ncfo) / revenue.replace(0, np.nan)
    b = _z(raw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-to-revenue trend: slope of FCF margin over a quarter (improving cash quality)
def f32cf_f32_cash_flow_quality_fcfmgntrend_63d_base_v011_signal(fcf, revenue):
    b = _slope(_f32_fcf_margin(fcf, revenue), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-to-revenue trend: slope of FCF margin over a half-year
def f32cf_f32_cash_flow_quality_fcfmgntrend_126d_base_v012_signal(fcf, revenue):
    b = _slope(_f32_fcf_margin(fcf, revenue), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF margin trend: slope over a half-year
def f32cf_f32_cash_flow_quality_ocfmgntrend_126d_base_v013_signal(ncfo, revenue):
    b = _slope(_f32_ocf_margin(ncfo, revenue), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex coverage balance: (ncfo-capex)/(|ncfo|+capex), bounded self-funding score
def f32cf_f32_cash_flow_quality_capexcover_63d_base_v014_signal(ncfo, capex):
    bal = (ncfo - capex) / (ncfo.abs() + capex).replace(0, np.nan)
    b = _mean(bal, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex coverage deviation: ncfo/capex relative to its own 252d average (de-trended)
def f32cf_f32_cash_flow_quality_capexcover_252d_base_v015_signal(ncfo, capex):
    cov = _f32_capex_cover(ncfo, capex).clip(-15, 15)
    b = cov / _mean(cov, 252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF consistency: fraction of last year with positive FCF (count-friendly)
def f32cf_f32_cash_flow_quality_fcfposfrac_252d_base_v016_signal(fcf):
    pos = (fcf > 0).astype(float)
    b = pos.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF consistency: fraction of last year with positive operating cash flow
def f32cf_f32_cash_flow_quality_ocfposfrac_252d_base_v017_signal(ncfo):
    pos = (ncfo > 0).astype(float)
    b = pos.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF inflection: neg->pos crossings over last year + sign-momentum (count-friendly)
def f32cf_f32_cash_flow_quality_fcfflip_252d_base_v018_signal(fcf):
    pos = (fcf > 0).astype(float)
    flip = ((pos == 1) & (pos.shift(1) == 0)).astype(float)
    cnt = flip.rolling(252, min_periods=126).sum()
    drift = pos.rolling(63, min_periods=21).mean() - pos.rolling(252, min_periods=126).mean()
    b = cnt + drift
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# time since FCF last turned positive (staleness of the inflection)
def f32cf_f32_cash_flow_quality_fcfsinceflip_252d_base_v019_signal(fcf):
    pos = (fcf > 0).astype(float)

    def _f(a):
        w = np.where(a > 0)[0]
        if len(w) == 0:
            return 1.0
        return (len(a) - 1 - w[-1]) / float(len(a))

    b = pos.rolling(252, min_periods=63).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fcfps level smoothed (per-share free cash generation)
def f32cf_f32_cash_flow_quality_fcfps_63d_base_v020_signal(fcfps):
    b = _mean(fcfps, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fcfps z-scored vs its own 252d history (per-share FCF extremity)
def f32cf_f32_cash_flow_quality_fcfpsz_252d_base_v021_signal(fcfps):
    b = _z(fcfps, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fcfps trend: slope over a half-year (per-share FCF improving)
def f32cf_f32_cash_flow_quality_fcfpstrend_126d_base_v022_signal(fcfps):
    b = _slope(fcfps, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF consistency: 1 minus coefficient-of-variation of FCF margin (stability)
def f32cf_f32_cash_flow_quality_fcfstab_252d_base_v023_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue)
    sd = _std(m, 252)
    mn = _mean(m.abs(), 252)
    b = 1.0 - sd / mn.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF margin volatility-of-volatility: std of rolling 21d std (cash-margin turbulence)
def f32cf_f32_cash_flow_quality_ocfvov_252d_base_v024_signal(ncfo, revenue):
    m = _f32_ocf_margin(ncfo, revenue)
    short_vol = _std(m, 21)
    b = _std(short_vol, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin minus OCF margin spread (capex drag on cash quality)
def f32cf_f32_cash_flow_quality_capexdrag_63d_base_v025_signal(fcf, ncfo, revenue):
    spr = (fcf - ncfo) / revenue.replace(0, np.nan)
    b = _mean(spr, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity (capex/revenue), smoothed (content/platform reinvestment)
def f32cf_f32_cash_flow_quality_capexint_63d_base_v026_signal(capex, revenue):
    b = _mean(_f32_capex_intensity(capex, revenue), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity z-scored vs own history (investment surge/retreat)
def f32cf_f32_cash_flow_quality_capexintz_252d_base_v027_signal(capex, revenue):
    b = _z(_f32_capex_intensity(capex, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash conversion z-scored vs own history (conversion-quality extremity)
def f32cf_f32_cash_flow_quality_cashconvz_252d_base_v028_signal(ncfo, netinc):
    b = _z(_f32_cash_conv(ncfo, netinc).clip(-5, 5), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin year-over-year change (annual cash-quality delta)
def f32cf_f32_cash_flow_quality_fcfmgnyoy_252d_base_v029_signal(fcf, revenue):
    m = _mean(_f32_fcf_margin(fcf, revenue), 21)
    b = m - m.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF margin year-over-year change
def f32cf_f32_cash_flow_quality_ocfmgnyoy_252d_base_v030_signal(ncfo, revenue):
    m = _mean(_f32_ocf_margin(ncfo, revenue), 21)
    b = m - m.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF growth: log-ratio of smoothed FCF over a year (cash scaling, sign-aware)
def f32cf_f32_cash_flow_quality_fcfgrowth_252d_base_v031_signal(fcf):
    s = _mean(fcf, 63)
    b = np.sign(s) * np.log(s.abs().replace(0, np.nan)) - (
        np.sign(s.shift(252)) * np.log(s.shift(252).abs().replace(0, np.nan)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF growth: log-ratio of smoothed ncfo over a half-year
def f32cf_f32_cash_flow_quality_ocfgrowth_126d_base_v032_signal(ncfo):
    s = _mean(ncfo, 63)
    b = np.sign(s) * np.log(s.abs().replace(0, np.nan)) - (
        np.sign(s.shift(126)) * np.log(s.shift(126).abs().replace(0, np.nan)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex coverage trend: slope of (ncfo-capex)/(|ncfo|+capex) balance over a half-year
def f32cf_f32_cash_flow_quality_capexcovtrend_126d_base_v033_signal(ncfo, capex):
    bal = (ncfo - capex) / (ncfo.abs() + capex).replace(0, np.nan)
    b = _slope(bal, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding gap normalized by capex (how many capex-units of surplus cash), de-trended
def f32cf_f32_cash_flow_quality_selffund_63d_base_v034_signal(ncfo, capex, revenue):
    raw = (ncfo - capex) / capex.replace(0, np.nan)
    raw = raw.clip(-10, 10)
    b = _mean(raw, 63) - _mean(raw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin downside semi-deviation (how bad the bad cash quarters get)
def f32cf_f32_cash_flow_quality_fcfdownsd_252d_base_v035_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue)
    mn = _mean(m, 252)
    neg = (m - mn).clip(upper=0)
    b = (neg ** 2).rolling(252, min_periods=126).mean() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual gap streak: consecutive periods of netinc > ncfo (persistent low quality)
def f32cf_f32_cash_flow_quality_accrualstreak_base_v036_signal(netinc, ncfo):
    bad = (netinc > ncfo).astype(float)

    def _f(a):
        c = 0
        for v in a[::-1]:
            if v > 0:
                c += 1
            else:
                break
        return c / float(len(a))

    b = bad.rolling(126, min_periods=63).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-backed earnings: sign agreement of netinc and ncfo, weighted by magnitude
def f32cf_f32_cash_flow_quality_signagree_63d_base_v037_signal(netinc, ncfo):
    agree = np.sign(netinc) * np.sign(ncfo)
    mag = (netinc.abs() + ncfo.abs())
    raw = agree * mag
    b = _mean(raw, 63) / _mean(mag, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin percentile rank vs own 504d history (cross-time cash quality)
def f32cf_f32_cash_flow_quality_fcfmgnrank_504d_base_v038_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue)
    b = m.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF margin percentile rank vs own 504d history
def f32cf_f32_cash_flow_quality_ocfmgnrank_504d_base_v039_signal(ncfo, revenue):
    m = _f32_ocf_margin(ncfo, revenue)
    b = m.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash conversion clipped then ema-smoothed (robust conversion level)
def f32cf_f32_cash_flow_quality_cashconvrob_63d_base_v040_signal(ncfo, netinc):
    c = _f32_cash_conv(ncfo, netinc).clip(-3, 3)
    b = c.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin minus its slow EMA (cash-quality displacement)
def f32cf_f32_cash_flow_quality_fcfmgndisp_base_v041_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue)
    b = m - m.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# healthy-margin regime: fraction of recent quarter FCF margin above its 252d median
def f32cf_f32_cash_flow_quality_fcfhealthy_252d_base_v042_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue)
    thr = m.rolling(252, min_periods=126).median()
    healthy = (m > thr).astype(float)
    frac = healthy.rolling(63, min_periods=21).mean()
    depth = (m - thr).clip(lower=0).rolling(63, min_periods=21).mean()
    b = frac + 5.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-to-OCF conversion ratio change over a quarter (capex squeeze on cash, tanh-bounded)
def f32cf_f32_cash_flow_quality_fcfocfconvchg_63d_base_v043_signal(fcf, ncfo):
    r = (fcf / ncfo.replace(0, np.nan)).clip(-5, 5)
    chg = r - r.shift(63)
    b = np.tanh(2.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash conversion gap from 1.0 (distance from perfect cash backing), smoothed
def f32cf_f32_cash_flow_quality_convgap_63d_base_v044_signal(ncfo, netinc):
    c = _f32_cash_conv(ncfo, netinc).clip(-5, 5)
    b = _mean((c - 1.0).abs(), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex burst regime: fraction of quarter capex sits above its 252d median (invest cycle)
def f32cf_f32_cash_flow_quality_capexcovfrac_252d_base_v045_signal(capex, ncfo):
    thr = capex.rolling(252, min_periods=126).median()
    burst = (capex > thr).astype(float)
    frac = burst.rolling(63, min_periods=21).mean()
    intensity = ((capex - thr) / ncfo.abs().replace(0, np.nan)).clip(-3, 3)
    b = frac + 0.3 * intensity.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin acceleration-as-level: quarter change minus prior-quarter change
def f32cf_f32_cash_flow_quality_fcfmgnaccel_base_v046_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue)
    d1 = m - m.shift(63)
    b = d1 - d1.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF margin dispersion across 63/126/252 horizons (regime disagreement)
def f32cf_f32_cash_flow_quality_ocfmgndisp_multi_base_v047_signal(ncfo, revenue):
    m = _f32_ocf_margin(ncfo, revenue)
    a = _mean(m, 63)
    b2 = _mean(m, 126)
    c = _mean(m, 252)
    b = pd.concat([a, b2, c], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fcfps recovery off its 252d low (per-share cash bottoming)
def f32cf_f32_cash_flow_quality_fcfpsrecov_252d_base_v048_signal(fcfps):
    sm = _mean(fcfps, 21)
    lo = sm.rolling(252, min_periods=126).min()
    b = sm - lo
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF as fraction of OCF (FCF conversion of operating cash), smoothed
def f32cf_f32_cash_flow_quality_fcfofocf_63d_base_v049_signal(fcf, ncfo):
    r = fcf / ncfo.replace(0, np.nan)
    b = _mean(r.clip(-5, 5), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF burn distance: how far below zero the worst FCF margin reaches in a year
def f32cf_f32_cash_flow_quality_fcfburn_252d_base_v050_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue)
    b = m.rolling(252, min_periods=126).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF margin minus FCF margin level (capex wedge level)
def f32cf_f32_cash_flow_quality_capexwedge_252d_base_v051_signal(ncfo, fcf, revenue):
    wedge = (ncfo - fcf) / revenue.replace(0, np.nan)
    b = _mean(wedge, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity acceleration: capex/revenue quarter-change minus prior-quarter change
def f32cf_f32_cash_flow_quality_capexintaccel_base_v052_signal(capex, revenue):
    ci = _f32_capex_intensity(capex, revenue)
    d1 = ci - ci.shift(63)
    b = d1 - d1.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual gap momentum: change in (netinc-ncfo)/revenue over a quarter
def f32cf_f32_cash_flow_quality_accrualmom_63d_base_v053_signal(netinc, ncfo, revenue):
    raw = _f32_accrual_gap(netinc, ncfo) / revenue.replace(0, np.nan)
    b = raw - raw.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin tail-heaviness (kurtosis) over a year (lumpy cash-quality risk)
def f32cf_f32_cash_flow_quality_fcfmgnkurt_252d_base_v054_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue)
    b = m.rolling(252, min_periods=126).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fcfps sign x sqrt-magnitude (compressed per-share cash level)
def f32cf_f32_cash_flow_quality_fcfpssignmag_base_v055_signal(fcfps):
    sm = _mean(fcfps, 21)
    b = np.sign(sm) * (sm.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-margin distribution skew over a half-year (asymmetry of cash-quality outcomes)
def f32cf_f32_cash_flow_quality_fcfskew_126d_base_v056_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue)
    b = m.rolling(126, min_periods=63).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash conversion trend: slope of clipped conversion over a half-year
def f32cf_f32_cash_flow_quality_convtrend_126d_base_v057_signal(ncfo, netinc):
    c = _f32_cash_conv(ncfo, netinc).clip(-5, 5)
    b = _slope(c, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of year ncfo positive but netinc negative (cash-profitable, GAAP-loss)
def f32cf_f32_cash_flow_quality_cashbeforegaap_252d_base_v058_signal(ncfo, netinc):
    flag = ((ncfo > 0) & (netinc < 0)).astype(float)
    b = flag.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF inflection magnitude: latest FCF margin minus its trailing-year min (lift off bottom)
def f32cf_f32_cash_flow_quality_fcfliftoff_252d_base_v059_signal(fcf, revenue):
    m = _mean(_f32_fcf_margin(fcf, revenue), 21)
    lo = m.rolling(252, min_periods=126).min()
    b = m - lo
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF inflection: latest OCF margin minus trailing-year min
def f32cf_f32_cash_flow_quality_ocfliftoff_252d_base_v060_signal(ncfo, revenue):
    m = _mean(_f32_ocf_margin(ncfo, revenue), 21)
    lo = m.rolling(252, min_periods=126).min()
    b = m - lo
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin range position within trailing year (where in cash-quality range)
def f32cf_f32_cash_flow_quality_fcfmgnrngpos_252d_base_v061_signal(fcf, revenue):
    m = _mean(_f32_fcf_margin(fcf, revenue), 21)
    hi = m.rolling(252, min_periods=126).max()
    lo = m.rolling(252, min_periods=126).min()
    b = (m - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity trend: slope over a year (rising content reinvestment)
def f32cf_f32_cash_flow_quality_capexinttrend_252d_base_v062_signal(capex, revenue):
    b = _slope(_f32_capex_intensity(capex, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin x OCF margin interaction (joint cash strength)
def f32cf_f32_cash_flow_quality_jointcash_63d_base_v063_signal(fcf, ncfo, revenue):
    fm = _f32_fcf_margin(fcf, revenue)
    om = _f32_ocf_margin(ncfo, revenue)
    b = _mean(fm * om, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash conversion above 1 streak fraction (durable cash-over-earnings)
def f32cf_f32_cash_flow_quality_convover1_252d_base_v064_signal(ncfo, netinc):
    over = ((ncfo > netinc) & (netinc > 0)).astype(float)
    b = over.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin EMA-fast minus EMA-slow (cash-quality MACD)
def f32cf_f32_cash_flow_quality_fcfmgnmacd_base_v065_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue)
    b = m.ewm(span=42, min_periods=21).mean() - m.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding strength: fraction of quarter the ncfo-capex gap beats its 252d median
def f32cf_f32_cash_flow_quality_selffundfrac_252d_base_v066_signal(ncfo, capex):
    gap = ncfo - capex
    thr = gap.rolling(252, min_periods=126).median()
    strong = (gap > thr).astype(float)
    frac = strong.rolling(63, min_periods=21).mean()
    lift = ((gap - thr) / capex.replace(0, np.nan)).clip(-5, 5).rolling(63, min_periods=21).mean()
    b = frac + 0.2 * lift
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# co-movement of FCF and capex changes (does cash dip when investment spikes)
def f32cf_f32_cash_flow_quality_fcfcapexcorr_126d_base_v067_signal(fcf, capex):
    df = fcf.diff()
    dc = capex.diff()
    b = df.rolling(126, min_periods=63).corr(dc)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual gap relative to absolute earnings (accrual share of profit)
def f32cf_f32_cash_flow_quality_accrualshare_63d_base_v068_signal(netinc, ncfo):
    raw = _f32_accrual_gap(netinc, ncfo) / (netinc.abs() + ncfo.abs()).replace(0, np.nan)
    b = _mean(raw, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fcfps year-over-year change (per-share cash growth)
def f32cf_f32_cash_flow_quality_fcfpsyoy_252d_base_v069_signal(fcfps):
    sm = _mean(fcfps, 21)
    b = sm - sm.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OCF margin downside-only volatility (operating-cash fragility)
def f32cf_f32_cash_flow_quality_ocfdownsd_252d_base_v070_signal(ncfo, revenue):
    m = _f32_ocf_margin(ncfo, revenue)
    mn = _mean(m, 252)
    neg = (m - mn).clip(upper=0)
    b = (neg ** 2).rolling(252, min_periods=126).mean() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash conversion dispersion 63 vs 252 (short vs long conversion gap)
def f32cf_f32_cash_flow_quality_convspread_base_v071_signal(ncfo, netinc):
    c = _f32_cash_conv(ncfo, netinc).clip(-5, 5)
    b = _mean(c, 63) - _mean(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin resilience: current level scaled by downside dispersion (recovery vs pain)
def f32cf_f32_cash_flow_quality_fcfresilience_252d_base_v072_signal(fcf, revenue):
    m = _f32_fcf_margin(fcf, revenue)
    cur = _mean(m, 21)
    mn = _mean(m, 252)
    down = ((m - mn).clip(upper=0) ** 2).rolling(252, min_periods=126).mean() ** 0.5
    b = (cur - mn) / down.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capex coverage range position within trailing year
def f32cf_f32_cash_flow_quality_capexcovrngpos_252d_base_v073_signal(ncfo, capex):
    c = _mean(_f32_capex_cover(ncfo, capex).clip(-15, 15), 21)
    hi = c.rolling(252, min_periods=126).max()
    lo = c.rolling(252, min_periods=126).min()
    b = (c - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net margin minus FCF margin (paper vs cash profit gap)
def f32cf_f32_cash_flow_quality_papervscash_63d_base_v074_signal(netinc, fcf, revenue):
    nm = netinc / revenue.replace(0, np.nan)
    fm = _f32_fcf_margin(fcf, revenue)
    b = _mean(nm - fm, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite cash-quality score: accrual-quality z + self-funding balance + fcf positivity
def f32cf_f32_cash_flow_quality_qualcomposite_base_v075_signal(ncfo, fcf, revenue, capex, netinc):
    acc = -_z((netinc - ncfo) / revenue.replace(0, np.nan), 252)
    bal = (ncfo - capex) / (ncfo.abs() + capex).replace(0, np.nan)
    fp = ((fcf > 0).astype(float).rolling(126, min_periods=63).mean() - 0.5)
    b = acc + 2.0 * bal + fp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f32cf_f32_cash_flow_quality_fcfmargin_63d_base_v001_signal,
    f32cf_f32_cash_flow_quality_fcfmargin_252d_base_v002_signal,
    f32cf_f32_cash_flow_quality_fcfmarginz_252d_base_v003_signal,
    f32cf_f32_cash_flow_quality_ocfmargin_63d_base_v004_signal,
    f32cf_f32_cash_flow_quality_ocfmargin_252d_base_v005_signal,
    f32cf_f32_cash_flow_quality_ocfmarginz_252d_base_v006_signal,
    f32cf_f32_cash_flow_quality_cashconv_63d_base_v007_signal,
    f32cf_f32_cash_flow_quality_cashconv_252d_base_v008_signal,
    f32cf_f32_cash_flow_quality_accrual_63d_base_v009_signal,
    f32cf_f32_cash_flow_quality_accrualz_252d_base_v010_signal,
    f32cf_f32_cash_flow_quality_fcfmgntrend_63d_base_v011_signal,
    f32cf_f32_cash_flow_quality_fcfmgntrend_126d_base_v012_signal,
    f32cf_f32_cash_flow_quality_ocfmgntrend_126d_base_v013_signal,
    f32cf_f32_cash_flow_quality_capexcover_63d_base_v014_signal,
    f32cf_f32_cash_flow_quality_capexcover_252d_base_v015_signal,
    f32cf_f32_cash_flow_quality_fcfposfrac_252d_base_v016_signal,
    f32cf_f32_cash_flow_quality_ocfposfrac_252d_base_v017_signal,
    f32cf_f32_cash_flow_quality_fcfflip_252d_base_v018_signal,
    f32cf_f32_cash_flow_quality_fcfsinceflip_252d_base_v019_signal,
    f32cf_f32_cash_flow_quality_fcfps_63d_base_v020_signal,
    f32cf_f32_cash_flow_quality_fcfpsz_252d_base_v021_signal,
    f32cf_f32_cash_flow_quality_fcfpstrend_126d_base_v022_signal,
    f32cf_f32_cash_flow_quality_fcfstab_252d_base_v023_signal,
    f32cf_f32_cash_flow_quality_ocfvov_252d_base_v024_signal,
    f32cf_f32_cash_flow_quality_capexdrag_63d_base_v025_signal,
    f32cf_f32_cash_flow_quality_capexint_63d_base_v026_signal,
    f32cf_f32_cash_flow_quality_capexintz_252d_base_v027_signal,
    f32cf_f32_cash_flow_quality_cashconvz_252d_base_v028_signal,
    f32cf_f32_cash_flow_quality_fcfmgnyoy_252d_base_v029_signal,
    f32cf_f32_cash_flow_quality_ocfmgnyoy_252d_base_v030_signal,
    f32cf_f32_cash_flow_quality_fcfgrowth_252d_base_v031_signal,
    f32cf_f32_cash_flow_quality_ocfgrowth_126d_base_v032_signal,
    f32cf_f32_cash_flow_quality_capexcovtrend_126d_base_v033_signal,
    f32cf_f32_cash_flow_quality_selffund_63d_base_v034_signal,
    f32cf_f32_cash_flow_quality_fcfdownsd_252d_base_v035_signal,
    f32cf_f32_cash_flow_quality_accrualstreak_base_v036_signal,
    f32cf_f32_cash_flow_quality_signagree_63d_base_v037_signal,
    f32cf_f32_cash_flow_quality_fcfmgnrank_504d_base_v038_signal,
    f32cf_f32_cash_flow_quality_ocfmgnrank_504d_base_v039_signal,
    f32cf_f32_cash_flow_quality_cashconvrob_63d_base_v040_signal,
    f32cf_f32_cash_flow_quality_fcfmgndisp_base_v041_signal,
    f32cf_f32_cash_flow_quality_fcfhealthy_252d_base_v042_signal,
    f32cf_f32_cash_flow_quality_fcfocfconvchg_63d_base_v043_signal,
    f32cf_f32_cash_flow_quality_convgap_63d_base_v044_signal,
    f32cf_f32_cash_flow_quality_capexcovfrac_252d_base_v045_signal,
    f32cf_f32_cash_flow_quality_fcfmgnaccel_base_v046_signal,
    f32cf_f32_cash_flow_quality_ocfmgndisp_multi_base_v047_signal,
    f32cf_f32_cash_flow_quality_fcfpsrecov_252d_base_v048_signal,
    f32cf_f32_cash_flow_quality_fcfofocf_63d_base_v049_signal,
    f32cf_f32_cash_flow_quality_fcfburn_252d_base_v050_signal,
    f32cf_f32_cash_flow_quality_capexwedge_252d_base_v051_signal,
    f32cf_f32_cash_flow_quality_capexintaccel_base_v052_signal,
    f32cf_f32_cash_flow_quality_accrualmom_63d_base_v053_signal,
    f32cf_f32_cash_flow_quality_fcfmgnkurt_252d_base_v054_signal,
    f32cf_f32_cash_flow_quality_fcfpssignmag_base_v055_signal,
    f32cf_f32_cash_flow_quality_fcfskew_126d_base_v056_signal,
    f32cf_f32_cash_flow_quality_convtrend_126d_base_v057_signal,
    f32cf_f32_cash_flow_quality_cashbeforegaap_252d_base_v058_signal,
    f32cf_f32_cash_flow_quality_fcfliftoff_252d_base_v059_signal,
    f32cf_f32_cash_flow_quality_ocfliftoff_252d_base_v060_signal,
    f32cf_f32_cash_flow_quality_fcfmgnrngpos_252d_base_v061_signal,
    f32cf_f32_cash_flow_quality_capexinttrend_252d_base_v062_signal,
    f32cf_f32_cash_flow_quality_jointcash_63d_base_v063_signal,
    f32cf_f32_cash_flow_quality_convover1_252d_base_v064_signal,
    f32cf_f32_cash_flow_quality_fcfmgnmacd_base_v065_signal,
    f32cf_f32_cash_flow_quality_selffundfrac_252d_base_v066_signal,
    f32cf_f32_cash_flow_quality_fcfcapexcorr_126d_base_v067_signal,
    f32cf_f32_cash_flow_quality_accrualshare_63d_base_v068_signal,
    f32cf_f32_cash_flow_quality_fcfpsyoy_252d_base_v069_signal,
    f32cf_f32_cash_flow_quality_ocfdownsd_252d_base_v070_signal,
    f32cf_f32_cash_flow_quality_convspread_base_v071_signal,
    f32cf_f32_cash_flow_quality_fcfresilience_252d_base_v072_signal,
    f32cf_f32_cash_flow_quality_capexcovrngpos_252d_base_v073_signal,
    f32cf_f32_cash_flow_quality_papervscash_63d_base_v074_signal,
    f32cf_f32_cash_flow_quality_qualcomposite_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F32_CASH_FLOW_QUALITY_REGISTRY_001_075 = REGISTRY


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
    # cash/earnings series oscillate around zero (comm-services often swing neg<->pos)
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

    print("OK f32_cash_flow_quality_base_001_075_claude: %d features pass" % n_features)
