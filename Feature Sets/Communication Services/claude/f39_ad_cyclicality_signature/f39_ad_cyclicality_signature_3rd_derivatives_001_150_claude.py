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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _roc(s, w):
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 3)).rank(pct=True) - 0.5


# ===== folder domain primitives (ad-cyclicality signature) =====
def _f39_cyc_amp(s, w):
    hi = s.rolling(w, min_periods=max(1, w // 2)).max()
    lo = s.rolling(w, min_periods=max(1, w // 2)).min()
    mid = (hi + lo) / 2.0
    return (hi - lo) / mid.replace(0, np.nan)


def _f39_cyc_phase(s, w):
    hi = s.rolling(w, min_periods=max(1, w // 2)).max()
    lo = s.rolling(w, min_periods=max(1, w // 2)).min()
    return (s - lo) / (hi - lo).replace(0, np.nan)


def _f39_detrend(s, w):
    return s - s.rolling(w, min_periods=max(1, w // 2)).mean()


def _f39_op_margin(opinc, revenue):
    return opinc / revenue.replace(0, np.nan)


def _f39_gross_margin(gp, revenue):
    return gp / revenue.replace(0, np.nan)


def _f39_sales_intensity(sgna, revenue):
    return sgna / revenue.replace(0, np.nan)


def _f39_swing(s, w):
    d = s - s.rolling(w, min_periods=max(1, w // 2)).mean()
    return d.rolling(w, min_periods=max(1, w // 2)).std()


# jerk (2nd derivative) of revenue cyclic amplitude
def f39ac_f39_ad_cyclicality_signature_revamp_252d_jerk_v001_signal(revenue):
    base = _f39_cyc_amp(revenue, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of revenue cycle phase
def f39ac_f39_ad_cyclicality_signature_revphase_252d_jerk_v002_signal(revenue):
    base = _f39_cyc_phase(revenue, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of op-margin swing
def f39ac_f39_ad_cyclicality_signature_opmswing_252d_jerk_v003_signal(opinc, revenue):
    om = _f39_op_margin(opinc, revenue)
    base = _f39_swing(om, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ad-sales intensity z
def f39ac_f39_ad_cyclicality_signature_salesint_252d_jerk_v004_signal(sgna, revenue):
    si = _f39_sales_intensity(sgna, revenue)
    base = _z(si, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of gross-margin compression from peak
def f39ac_f39_ad_cyclicality_signature_gmcompress_252d_jerk_v005_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    peak = gm.rolling(252, min_periods=126).max()
    base = gm / peak.replace(0, np.nan) - 1.0
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ebitda-margin cyclic amplitude
def f39ac_f39_ad_cyclicality_signature_ebmamp_252d_jerk_v006_signal(ebitdamargin):
    base = _f39_cyc_amp(ebitdamargin, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of revenue detrended cyclical / trend
def f39ac_f39_ad_cyclicality_signature_revcyc_252d_jerk_v007_signal(revenue):
    trend = _mean(revenue, 252)
    base = _f39_detrend(revenue, 252) / trend.replace(0, np.nan)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of gross-profit cyclic amplitude
def f39ac_f39_ad_cyclicality_signature_gpamp_252d_jerk_v008_signal(gp):
    base = _f39_cyc_amp(gp, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of op-margin cycle phase
def f39ac_f39_ad_cyclicality_signature_opmphase_252d_jerk_v009_signal(opinc, revenue):
    om = _f39_op_margin(opinc, revenue)
    base = _f39_cyc_phase(om, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ad-sales intensity swing
def f39ac_f39_ad_cyclicality_signature_salesswing_252d_jerk_v010_signal(sgna, revenue):
    si = _f39_sales_intensity(sgna, revenue)
    base = _f39_swing(si, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of gross-margin swing
def f39ac_f39_ad_cyclicality_signature_gmswing_504d_jerk_v011_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    base = _f39_swing(gm, 504)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of op-margin compression from peak
def f39ac_f39_ad_cyclicality_signature_opmcompress_252d_jerk_v012_signal(opinc, revenue):
    om = _f39_op_margin(opinc, revenue)
    peak = om.rolling(252, min_periods=126).max()
    base = om - peak
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ad-sales intensity amplitude
def f39ac_f39_ad_cyclicality_signature_salesamp_504d_jerk_v013_signal(sgna, revenue):
    si = _f39_sales_intensity(sgna, revenue)
    base = _f39_cyc_amp(si, 504)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ebitda-margin detrended cyclical
def f39ac_f39_ad_cyclicality_signature_ebmcyc_252d_jerk_v014_signal(ebitdamargin):
    base = _f39_detrend(ebitdamargin, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of gross-margin cycle phase
def f39ac_f39_ad_cyclicality_signature_gmphase_252d_jerk_v015_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    base = _f39_cyc_phase(gm, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of revenue drawdown from peak
def f39ac_f39_ad_cyclicality_signature_revdd_252d_jerk_v016_signal(revenue):
    peak = revenue.rolling(252, min_periods=126).max()
    base = revenue / peak.replace(0, np.nan) - 1.0
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of sales-intensity minus gross-margin z
def f39ac_f39_ad_cyclicality_signature_salesgmspr_252d_jerk_v017_signal(sgna, revenue, gp):
    si = _f39_sales_intensity(sgna, revenue)
    gm = _f39_gross_margin(gp, revenue)
    base = _z(si, 252) - _z(gm, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of op-margin cyclic amplitude
def f39ac_f39_ad_cyclicality_signature_opmamp_252d_jerk_v018_signal(opinc, revenue):
    om = _f39_op_margin(opinc, revenue)
    base = _f39_cyc_amp(om, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of gross-margin recovery off trough
def f39ac_f39_ad_cyclicality_signature_gmrecov_252d_jerk_v019_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    trough = gm.rolling(252, min_periods=126).min()
    base = gm / trough.replace(0, np.nan) - 1.0
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ad-sales intensity phase
def f39ac_f39_ad_cyclicality_signature_salesphase_504d_jerk_v020_signal(sgna, revenue):
    si = _f39_sales_intensity(sgna, revenue)
    base = _f39_cyc_phase(si, 504)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of gross-margin cyclic amplitude
def f39ac_f39_ad_cyclicality_signature_gmamp_252d_jerk_v021_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    base = _f39_cyc_amp(gm, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of revenue growth dispersion
def f39ac_f39_ad_cyclicality_signature_revgdisp_252d_jerk_v022_signal(revenue):
    g = _roc(revenue, 21)
    base = _std(g, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of op-margin trough distance
def f39ac_f39_ad_cyclicality_signature_opmtrough_252d_jerk_v023_signal(opinc, revenue):
    om = _f39_op_margin(opinc, revenue)
    trough = om.rolling(252, min_periods=126).min()
    base = om - trough
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of gp amplitude / revenue amplitude
def f39ac_f39_ad_cyclicality_signature_gprevsens_252d_jerk_v024_signal(gp, revenue):
    ga = _f39_cyc_amp(gp, 252)
    ra = _f39_cyc_amp(revenue, 252)
    base = ga / ra.replace(0, np.nan)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of gross-margin below-trend duration
def f39ac_f39_ad_cyclicality_signature_gmdowndur_252d_jerk_v025_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    below = (gm < _mean(gm, 252)).astype(float)
    base = below.rolling(252, min_periods=126).mean()
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of revenue phase minus ad-sales-intensity phase
def f39ac_f39_ad_cyclicality_signature_revtilt_252d_jerk_v026_signal(revenue, sgna):
    pr = _f39_cyc_phase(revenue, 252)
    si = _f39_sales_intensity(sgna, revenue)
    base = pr - _f39_cyc_phase(si, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ad-sales intensity off trough
def f39ac_f39_ad_cyclicality_signature_salescut_252d_jerk_v027_signal(sgna, revenue):
    si = _f39_sales_intensity(sgna, revenue)
    trough = si.rolling(252, min_periods=126).min()
    base = si / trough.replace(0, np.nan) - 1.0
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ebitda-margin cyclical x revenue z
def f39ac_f39_ad_cyclicality_signature_ebmcycz_252d_jerk_v028_signal(ebitdamargin, revenue):
    d = _f39_detrend(ebitdamargin, 252)
    base = d * _z(revenue, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of joint revenue/op-margin amplitude
def f39ac_f39_ad_cyclicality_signature_jointamp_252d_jerk_v029_signal(revenue, opinc):
    ra = _f39_cyc_amp(revenue, 252)
    oa = _f39_cyc_amp(_f39_op_margin(opinc, revenue), 252)
    base = (ra + oa) / 2.0
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of revenue above-trend strength
def f39ac_f39_ad_cyclicality_signature_revupturn_252d_jerk_v030_signal(revenue):
    above = (revenue > _mean(revenue, 252)).astype(float)
    excess = (revenue / _mean(revenue, 252).replace(0, np.nan) - 1.0).clip(lower=0)
    base = above.rolling(252, min_periods=126).mean() * 0.5 + excess.rolling(63, min_periods=21).mean()
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ad-sales intensity vs slow EMA
def f39ac_f39_ad_cyclicality_signature_salesdisp_252d_jerk_v031_signal(sgna, revenue):
    si = _f39_sales_intensity(sgna, revenue)
    base = si - si.ewm(span=63, min_periods=21).mean()
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of revenue amplitude z
def f39ac_f39_ad_cyclicality_signature_revampz_252d_jerk_v032_signal(revenue):
    amp = _f39_cyc_amp(revenue, 252)
    base = _z(amp, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of revenue distance past peak x time-since-peak
def f39ac_f39_ad_cyclicality_signature_peakdist_252d_jerk_v033_signal(revenue):
    def _dsh(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    hi = _rmax(revenue, 252)
    gap = np.log(revenue.replace(0, np.nan) / hi.replace(0, np.nan))
    dsh = revenue.rolling(252, min_periods=126).apply(_dsh, raw=True)
    base = gap * dsh
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ebitda-margin phase minus ad-sales phase
def f39ac_f39_ad_cyclicality_signature_ebmphase_252d_jerk_v034_signal(ebitdamargin, sgna, revenue):
    pe = _f39_cyc_phase(ebitdamargin, 252)
    ps = _f39_cyc_phase(_f39_sales_intensity(sgna, revenue), 252)
    base = pe - ps
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of gross-profit detrended / trend
def f39ac_f39_ad_cyclicality_signature_gpcyc_252d_jerk_v035_signal(gp):
    trend = _mean(gp, 252)
    base = _f39_detrend(gp, 252) / trend.replace(0, np.nan)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of revenue recovery off trough
def f39ac_f39_ad_cyclicality_signature_revrecov_252d_jerk_v036_signal(revenue):
    trough = revenue.rolling(252, min_periods=126).min()
    base = revenue / trough.replace(0, np.nan) - 1.0
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of op-margin vs trend ratio smoothed
def f39ac_f39_ad_cyclicality_signature_opmtilt_252d_jerk_v037_signal(opinc, revenue):
    om = _f39_op_margin(opinc, revenue)
    base = (om - _mean(om, 252)).ewm(span=42, min_periods=21).mean()
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ad-spend amplitude / revenue amplitude
def f39ac_f39_ad_cyclicality_signature_salesprocyc_252d_jerk_v038_signal(sgna, revenue):
    si = _f39_sales_intensity(sgna, revenue)
    sa = _f39_cyc_amp(si, 252)
    ra = _f39_cyc_amp(revenue, 252)
    base = sa / ra.replace(0, np.nan)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of gross-margin level z
def f39ac_f39_ad_cyclicality_signature_gmcyclz_504d_jerk_v039_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    base = _z(gm, 504)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ebitda-margin minus op-margin detrended
def f39ac_f39_ad_cyclicality_signature_ebmtrough_252d_jerk_v040_signal(ebitdamargin, opinc, revenue):
    om = _f39_op_margin(opinc, revenue)
    base = _f39_detrend(ebitdamargin, 252) - _f39_detrend(om, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of revenue fast-vs-slow trend gap
def f39ac_f39_ad_cyclicality_signature_revcycgap_252d_jerk_v041_signal(revenue):
    fast = revenue / _mean(revenue, 63).replace(0, np.nan) - 1.0
    slow = revenue / _mean(revenue, 252).replace(0, np.nan) - 1.0
    base = fast - slow
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of op vs gross margin cyclical divergence
def f39ac_f39_ad_cyclicality_signature_opgmdiv_252d_jerk_v042_signal(opinc, revenue, gp):
    om = _f39_op_margin(opinc, revenue)
    gm = _f39_gross_margin(gp, revenue)
    base = _f39_detrend(om, 252) - _f39_detrend(gm, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of revenue amplitude minus sales-intensity amplitude
def f39ac_f39_ad_cyclicality_signature_ampperint_252d_jerk_v043_signal(revenue, sgna):
    amp = _f39_cyc_amp(revenue, 252)
    si = sgna / revenue.replace(0, np.nan)
    base = amp - _f39_cyc_amp(si, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of gp vs revenue phase sync
def f39ac_f39_ad_cyclicality_signature_phasesync_252d_jerk_v044_signal(gp, revenue):
    pg = _f39_cyc_phase(gp, 252)
    pr = _f39_cyc_phase(revenue, 252)
    base = (pg - 0.5) * (pr - 0.5) * 4.0
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ebitda-margin vs revenue phase gap
def f39ac_f39_ad_cyclicality_signature_marginlag_252d_jerk_v045_signal(ebitdamargin, revenue):
    pe = _f39_cyc_phase(ebitdamargin, 252)
    pr = _f39_cyc_phase(revenue, 252)
    base = pe - pr
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of revenue amplitude x growth dispersion
def f39ac_f39_ad_cyclicality_signature_cyccomp_252d_jerk_v046_signal(revenue):
    amp = _f39_cyc_amp(revenue, 252)
    disp = _std(_roc(revenue, 21), 252)
    base = amp * disp
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ad-sales intensity rising-streak
def f39ac_f39_ad_cyclicality_signature_salesstreak_252d_jerk_v047_signal(sgna, revenue):
    si = _f39_sales_intensity(sgna, revenue)
    up = (si.diff() > 0).astype(float)
    base = up.rolling(252, min_periods=126).mean() - 0.5
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ebitda-margin level z
def f39ac_f39_ad_cyclicality_signature_ebmcyclz_504d_jerk_v048_signal(ebitdamargin):
    base = _z(ebitdamargin, 504)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of revenue detrended cyclical / trend (504)
def f39ac_f39_ad_cyclicality_signature_revcyc504_504d_jerk_v049_signal(revenue):
    trend = _mean(revenue, 504)
    base = _f39_detrend(revenue, 504) / trend.replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of gross-margin compression (504)
def f39ac_f39_ad_cyclicality_signature_gmcompress504_504d_jerk_v050_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    peak = gm.rolling(504, min_periods=252).max()
    base = gm / peak.replace(0, np.nan) - 1.0
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of op-margin amplitude (504)
def f39ac_f39_ad_cyclicality_signature_opmamp504_504d_jerk_v051_signal(opinc, revenue):
    om = _f39_op_margin(opinc, revenue)
    base = _f39_cyc_amp(om, 504)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of revenue amplitude (126)
def f39ac_f39_ad_cyclicality_signature_revamp126_126d_jerk_v052_signal(revenue):
    base = _f39_cyc_amp(revenue, 126)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ad-sales intensity z (504)
def f39ac_f39_ad_cyclicality_signature_salesint504_504d_jerk_v053_signal(sgna, revenue):
    si = _f39_sales_intensity(sgna, revenue)
    base = _z(si, 504)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of gross-profit amplitude (126)
def f39ac_f39_ad_cyclicality_signature_gpamp126_126d_jerk_v054_signal(gp):
    base = _f39_cyc_amp(gp, 126)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ebitda-margin swing
def f39ac_f39_ad_cyclicality_signature_ebmswing_252d_jerk_v055_signal(ebitdamargin):
    base = _f39_swing(ebitdamargin, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of op-margin phase (504)
def f39ac_f39_ad_cyclicality_signature_opmphase504_504d_jerk_v056_signal(opinc, revenue):
    om = _f39_op_margin(opinc, revenue)
    base = _f39_cyc_phase(om, 504)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of revenue phase (504)
def f39ac_f39_ad_cyclicality_signature_revphase504_504d_jerk_v057_signal(revenue):
    base = _f39_cyc_phase(revenue, 504)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of gross-margin phase (504)
def f39ac_f39_ad_cyclicality_signature_gmphase504_504d_jerk_v058_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    base = _f39_cyc_phase(gm, 504)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ad-sales intensity detrended
def f39ac_f39_ad_cyclicality_signature_salescyc_252d_jerk_v059_signal(sgna, revenue):
    si = _f39_sales_intensity(sgna, revenue)
    base = _f39_detrend(si, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of revenue below-trend depth
def f39ac_f39_ad_cyclicality_signature_revdowndepth_252d_jerk_v060_signal(revenue):
    trend = _mean(revenue, 252)
    base = (trend - revenue).clip(lower=0) / trend.replace(0, np.nan)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of gross-profit phase
def f39ac_f39_ad_cyclicality_signature_gpphase_252d_jerk_v061_signal(gp):
    base = _f39_cyc_phase(gp, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of op-margin vs revenue phase spread
def f39ac_f39_ad_cyclicality_signature_opmrevspr_252d_jerk_v062_signal(opinc, revenue):
    pom = _f39_cyc_phase(_f39_op_margin(opinc, revenue), 252)
    pr = _f39_cyc_phase(revenue, 252)
    base = pom - pr
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of sales-intensity + op-margin detrended
def f39ac_f39_ad_cyclicality_signature_salesopspr_252d_jerk_v063_signal(sgna, revenue, opinc):
    si = _f39_sales_intensity(sgna, revenue)
    om = _f39_op_margin(opinc, revenue)
    base = _f39_detrend(si, 252) + _f39_detrend(om, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ebitda-margin minus gross-margin detrended (504)
def f39ac_f39_ad_cyclicality_signature_ebmdetr504_504d_jerk_v064_signal(ebitdamargin, gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    base = _f39_detrend(ebitdamargin, 504) - _f39_detrend(gm, 504)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of revenue 63d-mean roc
def f39ac_f39_ad_cyclicality_signature_revtrendslope_252d_jerk_v065_signal(revenue):
    base = _roc(_mean(revenue, 63), 63)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of gross-margin below-trend depth weighted by revenue downturn
def f39ac_f39_ad_cyclicality_signature_gmtrough_252d_jerk_v066_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    gmcomp = (_mean(gm, 252) - gm).clip(lower=0)
    revdd = (_mean(revenue, 252) - revenue).clip(lower=0) / _mean(revenue, 252).replace(0, np.nan)
    base = gmcomp * revdd
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ad-sales intensity amplitude (126)
def f39ac_f39_ad_cyclicality_signature_salesamp126_126d_jerk_v067_signal(sgna, revenue):
    si = _f39_sales_intensity(sgna, revenue)
    base = _f39_cyc_amp(si, 126)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of op-margin level z
def f39ac_f39_ad_cyclicality_signature_opmcyclz_252d_jerk_v068_signal(opinc, revenue):
    om = _f39_op_margin(opinc, revenue)
    base = _z(om, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of gross-profit growth swing
def f39ac_f39_ad_cyclicality_signature_gpswing_252d_jerk_v069_signal(gp):
    base = _f39_swing(_roc(gp, 21), 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of revenue acceleration dispersion
def f39ac_f39_ad_cyclicality_signature_revaccel_252d_jerk_v070_signal(revenue):
    acc = _roc(revenue, 21) - _roc(revenue.shift(21), 21)
    base = _std(acc, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ebitda-margin amplitude (504)
def f39ac_f39_ad_cyclicality_signature_ebmamp504_504d_jerk_v071_signal(ebitdamargin):
    base = _f39_cyc_amp(ebitdamargin, 504)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of gross-margin rank vs history (504)
def f39ac_f39_ad_cyclicality_signature_gmcyc504_504d_jerk_v072_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    base = _rank(gm, 504)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ad-sales intensity vs trend smoothed
def f39ac_f39_ad_cyclicality_signature_salestilt_252d_jerk_v073_signal(sgna, revenue):
    si = _f39_sales_intensity(sgna, revenue)
    base = (si - _mean(si, 252)).ewm(span=42, min_periods=21).mean()
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of revenue range position (126)
def f39ac_f39_ad_cyclicality_signature_revrng126_126d_jerk_v074_signal(revenue):
    base = _f39_cyc_phase(revenue, 126)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of op-margin x ad-sales-intensity cyclical co-move
def f39ac_f39_ad_cyclicality_signature_opmdetr504_504d_jerk_v075_signal(opinc, revenue, sgna):
    om = _z(_f39_op_margin(opinc, revenue), 504)
    si = _z(_f39_sales_intensity(sgna, revenue), 504)
    base = (om * si).rolling(252, min_periods=126).mean()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of gross-profit acceleration dispersion
def f39ac_f39_ad_cyclicality_signature_gpdisp_252d_jerk_v076_signal(gp):
    acc = _roc(gp, 21) - _roc(gp.shift(21), 21)
    base = _std(acc, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ebitda-margin vs trend smoothed
def f39ac_f39_ad_cyclicality_signature_ebmtilt_252d_jerk_v077_signal(ebitdamargin):
    base = (ebitdamargin - _mean(ebitdamargin, 252)).ewm(span=42, min_periods=21).mean()
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of sgna vs gp ratio detrended
def f39ac_f39_ad_cyclicality_signature_salesgp_252d_jerk_v078_signal(sgna, gp):
    r = sgna / gp.replace(0, np.nan)
    base = _f39_detrend(r, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of revenue amplitude / gp amplitude
def f39ac_f39_ad_cyclicality_signature_revgmratio_252d_jerk_v079_signal(revenue, gp):
    ra = _f39_cyc_amp(revenue, 252)
    ga = _f39_cyc_amp(gp, 252)
    base = ra / ga.replace(0, np.nan)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of op-margin swing (126)
def f39ac_f39_ad_cyclicality_signature_opmswing126_126d_jerk_v080_signal(opinc, revenue):
    om = _f39_op_margin(opinc, revenue)
    base = _f39_swing(om, 126)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of gross-margin compression (126)
def f39ac_f39_ad_cyclicality_signature_gmcompr126_126d_jerk_v081_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    peak = gm.rolling(126, min_periods=63).max()
    base = gm / peak.replace(0, np.nan) - 1.0
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of revenue vs long trend ratio smoothed
def f39ac_f39_ad_cyclicality_signature_revtiltlong_504d_jerk_v082_signal(revenue):
    ratio = revenue / _mean(revenue, 504).replace(0, np.nan)
    base = ratio.ewm(span=84, min_periods=42).mean() - 1.0
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ad-sales intensity phase (126)
def f39ac_f39_ad_cyclicality_signature_salesphase126_126d_jerk_v083_signal(sgna, revenue):
    si = _f39_sales_intensity(sgna, revenue)
    base = _f39_cyc_phase(si, 126)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ebitda-margin phase (126)
def f39ac_f39_ad_cyclicality_signature_ebmphase126_126d_jerk_v084_signal(ebitdamargin):
    base = _f39_cyc_phase(ebitdamargin, 126)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of gross-profit phase z
def f39ac_f39_ad_cyclicality_signature_gpphasez_252d_jerk_v085_signal(gp):
    ph = _f39_cyc_phase(gp, 252)
    base = _z(ph, 126)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of op-margin trough distance (504)
def f39ac_f39_ad_cyclicality_signature_opmtrough504_504d_jerk_v086_signal(opinc, revenue):
    om = _f39_op_margin(opinc, revenue)
    trough = om.rolling(504, min_periods=252).min()
    base = om - trough
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of revenue below-trend duration (504)
def f39ac_f39_ad_cyclicality_signature_revdd504_504d_jerk_v087_signal(revenue):
    below = (revenue < _mean(revenue, 504)).astype(float)
    base = below.rolling(504, min_periods=252).mean()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of gross-margin recovery off trough (504)
def f39ac_f39_ad_cyclicality_signature_gmrecov504_504d_jerk_v088_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    trough = gm.rolling(504, min_periods=252).min()
    base = gm / trough.replace(0, np.nan) - 1.0
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ad-sales intensity off trough (504)
def f39ac_f39_ad_cyclicality_signature_salescut504_504d_jerk_v089_signal(sgna, revenue):
    si = _f39_sales_intensity(sgna, revenue)
    trough = si.rolling(504, min_periods=252).min()
    base = si / trough.replace(0, np.nan) - 1.0
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ebitda-margin compression weighted by revenue downturn (504)
def f39ac_f39_ad_cyclicality_signature_ebmcompr504_504d_jerk_v090_signal(ebitdamargin, revenue):
    peak = ebitdamargin.rolling(504, min_periods=252).max()
    revdd = revenue / revenue.rolling(504, min_periods=252).max().replace(0, np.nan)
    base = (ebitdamargin - peak) * revdd
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of revenue growth dispersion (126)
def f39ac_f39_ad_cyclicality_signature_revgdisp126_126d_jerk_v091_signal(revenue):
    base = _std(_roc(revenue, 21), 126)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of gross-margin level z (252)
def f39ac_f39_ad_cyclicality_signature_gmcyclz252_252d_jerk_v092_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    base = _z(gm, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of op-margin compression (504)
def f39ac_f39_ad_cyclicality_signature_opmcompr504_504d_jerk_v093_signal(opinc, revenue):
    om = _f39_op_margin(opinc, revenue)
    peak = om.rolling(504, min_periods=252).max()
    base = om - peak
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ad-sales intensity swing (504)
def f39ac_f39_ad_cyclicality_signature_salesswing504_504d_jerk_v094_signal(sgna, revenue):
    si = _f39_sales_intensity(sgna, revenue)
    base = _f39_swing(si, 504)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of revenue detrended / trend (126)
def f39ac_f39_ad_cyclicality_signature_revcyc126_126d_jerk_v095_signal(revenue):
    trend = _mean(revenue, 126)
    base = _f39_detrend(revenue, 126) / trend.replace(0, np.nan)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of gross-profit detrended / trend (504)
def f39ac_f39_ad_cyclicality_signature_gpcyc504_504d_jerk_v096_signal(gp):
    trend = _mean(gp, 504)
    base = _f39_detrend(gp, 504) / trend.replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ebitda-margin swing (504)
def f39ac_f39_ad_cyclicality_signature_ebmswing504_504d_jerk_v097_signal(ebitdamargin):
    base = _f39_swing(ebitdamargin, 504)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of op-margin vs revenue phase gap (504)
def f39ac_f39_ad_cyclicality_signature_opmrevlag504_504d_jerk_v098_signal(opinc, revenue):
    pom = _f39_cyc_phase(_f39_op_margin(opinc, revenue), 504)
    pr = _f39_cyc_phase(revenue, 504)
    base = pom - pr
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of revenue amplitude x trend-slope sign
def f39ac_f39_ad_cyclicality_signature_revsensdir_252d_jerk_v099_signal(revenue):
    amp = _f39_cyc_amp(revenue, 252)
    slope = _roc(_mean(revenue, 63), 63)
    base = amp * np.sign(slope)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of gross-margin amplitude (504)
def f39ac_f39_ad_cyclicality_signature_gmamp504_504d_jerk_v100_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    base = _f39_cyc_amp(gm, 504)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of sales-intensity minus gm z (504)
def f39ac_f39_ad_cyclicality_signature_salesgmspr504_504d_jerk_v101_signal(sgna, revenue, gp):
    si = _f39_sales_intensity(sgna, revenue)
    gm = _f39_gross_margin(gp, revenue)
    base = _z(si, 504) - _z(gm, 504)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of revenue above-trend strength (504)
def f39ac_f39_ad_cyclicality_signature_revupturn504_504d_jerk_v102_signal(revenue):
    above = (revenue > _mean(revenue, 504)).astype(float)
    excess = (revenue / _mean(revenue, 504).replace(0, np.nan) - 1.0).clip(lower=0)
    base = above.rolling(504, min_periods=252).mean() * 0.5 + excess.rolling(126, min_periods=63).mean()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ebitda-margin range-position rank
def f39ac_f39_ad_cyclicality_signature_ebmtrough252_252d_jerk_v103_signal(ebitdamargin):
    base = _rank(_f39_cyc_phase(ebitdamargin, 252), 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of op-margin vs long trend smoothed
def f39ac_f39_ad_cyclicality_signature_opmtiltlong_504d_jerk_v104_signal(opinc, revenue):
    om = _f39_op_margin(opinc, revenue)
    base = (om - _mean(om, 504)).ewm(span=84, min_periods=42).mean()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of gross-profit amplitude z
def f39ac_f39_ad_cyclicality_signature_gpampz_252d_jerk_v105_signal(gp):
    amp = _f39_cyc_amp(gp, 252)
    base = _z(amp, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of revenue range position smoothed (504)
def f39ac_f39_ad_cyclicality_signature_revrng504pos_504d_jerk_v106_signal(revenue):
    rp = _f39_cyc_phase(revenue, 504)
    base = rp.ewm(span=42, min_periods=21).mean()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ad-sales intensity amplitude (252)
def f39ac_f39_ad_cyclicality_signature_salesintamp252_252d_jerk_v107_signal(sgna, revenue):
    si = _f39_sales_intensity(sgna, revenue)
    base = _f39_cyc_amp(si, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ebitda-margin phase z
def f39ac_f39_ad_cyclicality_signature_ebmphasez_252d_jerk_v108_signal(ebitdamargin):
    ph = _f39_cyc_phase(ebitdamargin, 252)
    base = _z(ph, 126)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of gross-margin downturn duration (504)
def f39ac_f39_ad_cyclicality_signature_gmtrough504_504d_jerk_v109_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    below = (gm < _mean(gm, 504)).astype(float)
    base = below.rolling(504, min_periods=252).mean()
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of op-margin smoothed change
def f39ac_f39_ad_cyclicality_signature_opmgrowth_252d_jerk_v110_signal(opinc, revenue):
    om = _f39_op_margin(opinc, revenue)
    base = (om - om.shift(63)).ewm(span=21, min_periods=10).mean()
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of revenue level z minus long z
def f39ac_f39_ad_cyclicality_signature_revscalez_252d_jerk_v111_signal(revenue):
    base = _z(revenue, 63) - _z(revenue, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of gross-profit level z
def f39ac_f39_ad_cyclicality_signature_gpscalez_252d_jerk_v112_signal(gp):
    base = _z(gp, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of sgna level z
def f39ac_f39_ad_cyclicality_signature_salesscalez_252d_jerk_v113_signal(sgna):
    base = _z(sgna, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of revenue minus gp detrended ratio
def f39ac_f39_ad_cyclicality_signature_revgppair_252d_jerk_v114_signal(revenue, gp):
    rz = _z(revenue, 252)
    gz = _z(gp, 252)
    base = rz - gz
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of op-margin amplitude minus revenue amplitude
def f39ac_f39_ad_cyclicality_signature_opmrevamp_252d_jerk_v115_signal(opinc, revenue):
    oa = _f39_cyc_amp(_f39_op_margin(opinc, revenue), 252)
    ra = _f39_cyc_amp(revenue, 252)
    base = oa - ra
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ad-sales intensity phase z
def f39ac_f39_ad_cyclicality_signature_salesphasez_252d_jerk_v116_signal(sgna, revenue):
    ph = _f39_cyc_phase(_f39_sales_intensity(sgna, revenue), 252)
    base = _z(ph, 126)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ebitda-margin smoothed change
def f39ac_f39_ad_cyclicality_signature_ebmgrowth_252d_jerk_v117_signal(ebitdamargin):
    base = (ebitdamargin - ebitdamargin.shift(63)).ewm(span=21, min_periods=10).mean()
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of gross-margin smoothed change
def f39ac_f39_ad_cyclicality_signature_gmgrowth_252d_jerk_v118_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    base = (gm - gm.shift(63)).ewm(span=21, min_periods=10).mean()
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of revenue below-trend duration
def f39ac_f39_ad_cyclicality_signature_revdowndur_252d_jerk_v119_signal(revenue):
    below = (revenue < _mean(revenue, 252)).astype(float)
    base = below.rolling(252, min_periods=126).mean()
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ad-sales intensity above-trend duration
def f39ac_f39_ad_cyclicality_signature_salesupdur_252d_jerk_v120_signal(sgna, revenue):
    si = _f39_sales_intensity(sgna, revenue)
    above = (si > _mean(si, 252)).astype(float)
    base = above.rolling(252, min_periods=126).mean()
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of op-margin above-trend duration
def f39ac_f39_ad_cyclicality_signature_opmupdur_252d_jerk_v121_signal(opinc, revenue):
    om = _f39_op_margin(opinc, revenue)
    above = (om > _mean(om, 252)).astype(float)
    base = above.rolling(252, min_periods=126).mean()
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ebitda-margin phase minus revenue phase (504)
def f39ac_f39_ad_cyclicality_signature_ebmrng504_504d_jerk_v122_signal(ebitdamargin, revenue):
    pe = _f39_cyc_phase(ebitdamargin, 504)
    pr = _f39_cyc_phase(revenue, 504)
    base = pe - pr
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of gross-profit range position (504)
def f39ac_f39_ad_cyclicality_signature_gprng504_504d_jerk_v123_signal(gp):
    base = _f39_cyc_phase(gp, 504)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of revenue range position z
def f39ac_f39_ad_cyclicality_signature_revrng252z_252d_jerk_v124_signal(revenue):
    rp = _f39_cyc_phase(revenue, 252)
    base = _z(rp, 126)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ad-sales intensity rank vs history
def f39ac_f39_ad_cyclicality_signature_salescycnorm_252d_jerk_v125_signal(sgna, revenue):
    si = _f39_sales_intensity(sgna, revenue)
    base = _rank(si, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of op-margin rank vs history
def f39ac_f39_ad_cyclicality_signature_opmcycnorm_252d_jerk_v126_signal(opinc, revenue):
    om = _f39_op_margin(opinc, revenue)
    base = _rank(om, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of gross-margin rank vs history
def f39ac_f39_ad_cyclicality_signature_gmcycnorm_252d_jerk_v127_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    base = _rank(gm, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of revenue amplitude ratio 252 vs 504
def f39ac_f39_ad_cyclicality_signature_revampratio_252d_jerk_v128_signal(revenue):
    s = _f39_cyc_amp(revenue, 252)
    l = _f39_cyc_amp(revenue, 504)
    base = s / l.replace(0, np.nan)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of gross-margin range-position rank
def f39ac_f39_ad_cyclicality_signature_gmprice_252d_jerk_v129_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    base = _rank(_f39_cyc_phase(gm, 252), 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ad-sales intensity minus gross-margin smoothed
def f39ac_f39_ad_cyclicality_signature_salesintlevel_252d_jerk_v130_signal(sgna, revenue, gp):
    si = _f39_sales_intensity(sgna, revenue)
    gm = _f39_gross_margin(gp, revenue)
    base = (si - gm).ewm(span=42, min_periods=21).mean()
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of op-margin minus gross-margin smoothed
def f39ac_f39_ad_cyclicality_signature_opmlevel_252d_jerk_v131_signal(opinc, revenue, gp):
    om = _f39_op_margin(opinc, revenue)
    gm = _f39_gross_margin(gp, revenue)
    base = (om - gm).ewm(span=42, min_periods=21).mean()
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ebitda-margin x gross-margin cyclical co-move
def f39ac_f39_ad_cyclicality_signature_ebmlevel_252d_jerk_v132_signal(ebitdamargin, gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    base = _z(ebitdamargin, 252) * _z(gm, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of gross-margin level smoothed
def f39ac_f39_ad_cyclicality_signature_gmlevel_252d_jerk_v133_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    base = gm.ewm(span=42, min_periods=21).mean()
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of revenue rank vs history
def f39ac_f39_ad_cyclicality_signature_revcyclic_252d_jerk_v134_signal(revenue):
    base = _rank(revenue, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of gross-profit rank vs history
def f39ac_f39_ad_cyclicality_signature_gpdetr_252d_jerk_v135_signal(gp):
    base = _rank(gp, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ad-sales intensity rank vs history (long)
def f39ac_f39_ad_cyclicality_signature_salesintdetr_252d_jerk_v136_signal(sgna, revenue):
    si = _f39_sales_intensity(sgna, revenue)
    base = _rank(si, 504)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of op-margin phase smoothed
def f39ac_f39_ad_cyclicality_signature_opmphasemom_252d_jerk_v137_signal(opinc, revenue):
    om = _f39_op_margin(opinc, revenue)
    ph = _f39_cyc_phase(om, 252)
    base = ph.ewm(span=21, min_periods=10).mean()
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ebitda-margin amplitude z (504)
def f39ac_f39_ad_cyclicality_signature_ebmampz504_504d_jerk_v138_signal(ebitdamargin):
    amp = _f39_cyc_amp(ebitdamargin, 504)
    base = _z(amp, 504)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of revenue phase rank vs history
def f39ac_f39_ad_cyclicality_signature_revphasez_252d_jerk_v139_signal(revenue):
    ph = _f39_cyc_phase(revenue, 252)
    base = _rank(ph, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of gross-margin phase z
def f39ac_f39_ad_cyclicality_signature_gmphasez_252d_jerk_v140_signal(gp, revenue):
    ph = _f39_cyc_phase(_f39_gross_margin(gp, revenue), 252)
    base = _z(ph, 126)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ad-sales intensity amplitude z
def f39ac_f39_ad_cyclicality_signature_salesampz_252d_jerk_v141_signal(sgna, revenue):
    si = _f39_sales_intensity(sgna, revenue)
    amp = _f39_cyc_amp(si, 252)
    base = _z(amp, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of op-margin amplitude z
def f39ac_f39_ad_cyclicality_signature_opmampz_252d_jerk_v142_signal(opinc, revenue):
    om = _f39_op_margin(opinc, revenue)
    amp = _f39_cyc_amp(om, 252)
    base = _z(amp, 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of revenue 126d-mean roc
def f39ac_f39_ad_cyclicality_signature_revscaleroc_252d_jerk_v143_signal(revenue):
    base = _roc(_mean(revenue, 126), 126)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of gross-profit 126d-mean roc
def f39ac_f39_ad_cyclicality_signature_gpscaleroc_252d_jerk_v144_signal(gp):
    base = _roc(_mean(gp, 126), 126)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of sgna 126d-mean roc
def f39ac_f39_ad_cyclicality_signature_salesscaleroc_252d_jerk_v145_signal(sgna):
    base = _roc(_mean(sgna, 126), 126)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of revenue-gross-margin cyclical co-move
def f39ac_f39_ad_cyclicality_signature_revgmco_252d_jerk_v146_signal(revenue, gp):
    rz = _z(revenue, 252)
    gz = _z(_f39_gross_margin(gp, revenue), 252)
    base = (rz * gz).rolling(126, min_periods=63).mean()
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of sales-intensity vs op-margin co-move
def f39ac_f39_ad_cyclicality_signature_salesopco_252d_jerk_v147_signal(sgna, revenue, opinc):
    si = _z(_f39_sales_intensity(sgna, revenue), 252)
    om = _z(_f39_op_margin(opinc, revenue), 252)
    base = (si * om).rolling(126, min_periods=63).mean()
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of ebitda-margin vs revenue cyclical co-move
def f39ac_f39_ad_cyclicality_signature_ebmrevco_252d_jerk_v148_signal(ebitdamargin, revenue):
    ez = _z(ebitdamargin, 252)
    rz = _z(revenue, 252)
    base = (ez * rz).rolling(126, min_periods=63).mean()
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of gross-margin expansion off trough scaled
def f39ac_f39_ad_cyclicality_signature_gmexpand_252d_jerk_v149_signal(gp, revenue):
    gm = _f39_gross_margin(gp, revenue)
    trough = gm.rolling(252, min_periods=126).min()
    base = (gm - trough) / _std(gm, 252).replace(0, np.nan)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

# jerk (2nd derivative) of revenue absolute swing std
def f39ac_f39_ad_cyclicality_signature_revampabs_252d_jerk_v150_signal(revenue):
    base = _std(_f39_detrend(revenue, 252), 252)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f39ac_f39_ad_cyclicality_signature_revamp_252d_jerk_v001_signal,
    f39ac_f39_ad_cyclicality_signature_revphase_252d_jerk_v002_signal,
    f39ac_f39_ad_cyclicality_signature_opmswing_252d_jerk_v003_signal,
    f39ac_f39_ad_cyclicality_signature_salesint_252d_jerk_v004_signal,
    f39ac_f39_ad_cyclicality_signature_gmcompress_252d_jerk_v005_signal,
    f39ac_f39_ad_cyclicality_signature_ebmamp_252d_jerk_v006_signal,
    f39ac_f39_ad_cyclicality_signature_revcyc_252d_jerk_v007_signal,
    f39ac_f39_ad_cyclicality_signature_gpamp_252d_jerk_v008_signal,
    f39ac_f39_ad_cyclicality_signature_opmphase_252d_jerk_v009_signal,
    f39ac_f39_ad_cyclicality_signature_salesswing_252d_jerk_v010_signal,
    f39ac_f39_ad_cyclicality_signature_gmswing_504d_jerk_v011_signal,
    f39ac_f39_ad_cyclicality_signature_opmcompress_252d_jerk_v012_signal,
    f39ac_f39_ad_cyclicality_signature_salesamp_504d_jerk_v013_signal,
    f39ac_f39_ad_cyclicality_signature_ebmcyc_252d_jerk_v014_signal,
    f39ac_f39_ad_cyclicality_signature_gmphase_252d_jerk_v015_signal,
    f39ac_f39_ad_cyclicality_signature_revdd_252d_jerk_v016_signal,
    f39ac_f39_ad_cyclicality_signature_salesgmspr_252d_jerk_v017_signal,
    f39ac_f39_ad_cyclicality_signature_opmamp_252d_jerk_v018_signal,
    f39ac_f39_ad_cyclicality_signature_gmrecov_252d_jerk_v019_signal,
    f39ac_f39_ad_cyclicality_signature_salesphase_504d_jerk_v020_signal,
    f39ac_f39_ad_cyclicality_signature_gmamp_252d_jerk_v021_signal,
    f39ac_f39_ad_cyclicality_signature_revgdisp_252d_jerk_v022_signal,
    f39ac_f39_ad_cyclicality_signature_opmtrough_252d_jerk_v023_signal,
    f39ac_f39_ad_cyclicality_signature_gprevsens_252d_jerk_v024_signal,
    f39ac_f39_ad_cyclicality_signature_gmdowndur_252d_jerk_v025_signal,
    f39ac_f39_ad_cyclicality_signature_revtilt_252d_jerk_v026_signal,
    f39ac_f39_ad_cyclicality_signature_salescut_252d_jerk_v027_signal,
    f39ac_f39_ad_cyclicality_signature_ebmcycz_252d_jerk_v028_signal,
    f39ac_f39_ad_cyclicality_signature_jointamp_252d_jerk_v029_signal,
    f39ac_f39_ad_cyclicality_signature_revupturn_252d_jerk_v030_signal,
    f39ac_f39_ad_cyclicality_signature_salesdisp_252d_jerk_v031_signal,
    f39ac_f39_ad_cyclicality_signature_revampz_252d_jerk_v032_signal,
    f39ac_f39_ad_cyclicality_signature_peakdist_252d_jerk_v033_signal,
    f39ac_f39_ad_cyclicality_signature_ebmphase_252d_jerk_v034_signal,
    f39ac_f39_ad_cyclicality_signature_gpcyc_252d_jerk_v035_signal,
    f39ac_f39_ad_cyclicality_signature_revrecov_252d_jerk_v036_signal,
    f39ac_f39_ad_cyclicality_signature_opmtilt_252d_jerk_v037_signal,
    f39ac_f39_ad_cyclicality_signature_salesprocyc_252d_jerk_v038_signal,
    f39ac_f39_ad_cyclicality_signature_gmcyclz_504d_jerk_v039_signal,
    f39ac_f39_ad_cyclicality_signature_ebmtrough_252d_jerk_v040_signal,
    f39ac_f39_ad_cyclicality_signature_revcycgap_252d_jerk_v041_signal,
    f39ac_f39_ad_cyclicality_signature_opgmdiv_252d_jerk_v042_signal,
    f39ac_f39_ad_cyclicality_signature_ampperint_252d_jerk_v043_signal,
    f39ac_f39_ad_cyclicality_signature_phasesync_252d_jerk_v044_signal,
    f39ac_f39_ad_cyclicality_signature_marginlag_252d_jerk_v045_signal,
    f39ac_f39_ad_cyclicality_signature_cyccomp_252d_jerk_v046_signal,
    f39ac_f39_ad_cyclicality_signature_salesstreak_252d_jerk_v047_signal,
    f39ac_f39_ad_cyclicality_signature_ebmcyclz_504d_jerk_v048_signal,
    f39ac_f39_ad_cyclicality_signature_revcyc504_504d_jerk_v049_signal,
    f39ac_f39_ad_cyclicality_signature_gmcompress504_504d_jerk_v050_signal,
    f39ac_f39_ad_cyclicality_signature_opmamp504_504d_jerk_v051_signal,
    f39ac_f39_ad_cyclicality_signature_revamp126_126d_jerk_v052_signal,
    f39ac_f39_ad_cyclicality_signature_salesint504_504d_jerk_v053_signal,
    f39ac_f39_ad_cyclicality_signature_gpamp126_126d_jerk_v054_signal,
    f39ac_f39_ad_cyclicality_signature_ebmswing_252d_jerk_v055_signal,
    f39ac_f39_ad_cyclicality_signature_opmphase504_504d_jerk_v056_signal,
    f39ac_f39_ad_cyclicality_signature_revphase504_504d_jerk_v057_signal,
    f39ac_f39_ad_cyclicality_signature_gmphase504_504d_jerk_v058_signal,
    f39ac_f39_ad_cyclicality_signature_salescyc_252d_jerk_v059_signal,
    f39ac_f39_ad_cyclicality_signature_revdowndepth_252d_jerk_v060_signal,
    f39ac_f39_ad_cyclicality_signature_gpphase_252d_jerk_v061_signal,
    f39ac_f39_ad_cyclicality_signature_opmrevspr_252d_jerk_v062_signal,
    f39ac_f39_ad_cyclicality_signature_salesopspr_252d_jerk_v063_signal,
    f39ac_f39_ad_cyclicality_signature_ebmdetr504_504d_jerk_v064_signal,
    f39ac_f39_ad_cyclicality_signature_revtrendslope_252d_jerk_v065_signal,
    f39ac_f39_ad_cyclicality_signature_gmtrough_252d_jerk_v066_signal,
    f39ac_f39_ad_cyclicality_signature_salesamp126_126d_jerk_v067_signal,
    f39ac_f39_ad_cyclicality_signature_opmcyclz_252d_jerk_v068_signal,
    f39ac_f39_ad_cyclicality_signature_gpswing_252d_jerk_v069_signal,
    f39ac_f39_ad_cyclicality_signature_revaccel_252d_jerk_v070_signal,
    f39ac_f39_ad_cyclicality_signature_ebmamp504_504d_jerk_v071_signal,
    f39ac_f39_ad_cyclicality_signature_gmcyc504_504d_jerk_v072_signal,
    f39ac_f39_ad_cyclicality_signature_salestilt_252d_jerk_v073_signal,
    f39ac_f39_ad_cyclicality_signature_revrng126_126d_jerk_v074_signal,
    f39ac_f39_ad_cyclicality_signature_opmdetr504_504d_jerk_v075_signal,
    f39ac_f39_ad_cyclicality_signature_gpdisp_252d_jerk_v076_signal,
    f39ac_f39_ad_cyclicality_signature_ebmtilt_252d_jerk_v077_signal,
    f39ac_f39_ad_cyclicality_signature_salesgp_252d_jerk_v078_signal,
    f39ac_f39_ad_cyclicality_signature_revgmratio_252d_jerk_v079_signal,
    f39ac_f39_ad_cyclicality_signature_opmswing126_126d_jerk_v080_signal,
    f39ac_f39_ad_cyclicality_signature_gmcompr126_126d_jerk_v081_signal,
    f39ac_f39_ad_cyclicality_signature_revtiltlong_504d_jerk_v082_signal,
    f39ac_f39_ad_cyclicality_signature_salesphase126_126d_jerk_v083_signal,
    f39ac_f39_ad_cyclicality_signature_ebmphase126_126d_jerk_v084_signal,
    f39ac_f39_ad_cyclicality_signature_gpphasez_252d_jerk_v085_signal,
    f39ac_f39_ad_cyclicality_signature_opmtrough504_504d_jerk_v086_signal,
    f39ac_f39_ad_cyclicality_signature_revdd504_504d_jerk_v087_signal,
    f39ac_f39_ad_cyclicality_signature_gmrecov504_504d_jerk_v088_signal,
    f39ac_f39_ad_cyclicality_signature_salescut504_504d_jerk_v089_signal,
    f39ac_f39_ad_cyclicality_signature_ebmcompr504_504d_jerk_v090_signal,
    f39ac_f39_ad_cyclicality_signature_revgdisp126_126d_jerk_v091_signal,
    f39ac_f39_ad_cyclicality_signature_gmcyclz252_252d_jerk_v092_signal,
    f39ac_f39_ad_cyclicality_signature_opmcompr504_504d_jerk_v093_signal,
    f39ac_f39_ad_cyclicality_signature_salesswing504_504d_jerk_v094_signal,
    f39ac_f39_ad_cyclicality_signature_revcyc126_126d_jerk_v095_signal,
    f39ac_f39_ad_cyclicality_signature_gpcyc504_504d_jerk_v096_signal,
    f39ac_f39_ad_cyclicality_signature_ebmswing504_504d_jerk_v097_signal,
    f39ac_f39_ad_cyclicality_signature_opmrevlag504_504d_jerk_v098_signal,
    f39ac_f39_ad_cyclicality_signature_revsensdir_252d_jerk_v099_signal,
    f39ac_f39_ad_cyclicality_signature_gmamp504_504d_jerk_v100_signal,
    f39ac_f39_ad_cyclicality_signature_salesgmspr504_504d_jerk_v101_signal,
    f39ac_f39_ad_cyclicality_signature_revupturn504_504d_jerk_v102_signal,
    f39ac_f39_ad_cyclicality_signature_ebmtrough252_252d_jerk_v103_signal,
    f39ac_f39_ad_cyclicality_signature_opmtiltlong_504d_jerk_v104_signal,
    f39ac_f39_ad_cyclicality_signature_gpampz_252d_jerk_v105_signal,
    f39ac_f39_ad_cyclicality_signature_revrng504pos_504d_jerk_v106_signal,
    f39ac_f39_ad_cyclicality_signature_salesintamp252_252d_jerk_v107_signal,
    f39ac_f39_ad_cyclicality_signature_ebmphasez_252d_jerk_v108_signal,
    f39ac_f39_ad_cyclicality_signature_gmtrough504_504d_jerk_v109_signal,
    f39ac_f39_ad_cyclicality_signature_opmgrowth_252d_jerk_v110_signal,
    f39ac_f39_ad_cyclicality_signature_revscalez_252d_jerk_v111_signal,
    f39ac_f39_ad_cyclicality_signature_gpscalez_252d_jerk_v112_signal,
    f39ac_f39_ad_cyclicality_signature_salesscalez_252d_jerk_v113_signal,
    f39ac_f39_ad_cyclicality_signature_revgppair_252d_jerk_v114_signal,
    f39ac_f39_ad_cyclicality_signature_opmrevamp_252d_jerk_v115_signal,
    f39ac_f39_ad_cyclicality_signature_salesphasez_252d_jerk_v116_signal,
    f39ac_f39_ad_cyclicality_signature_ebmgrowth_252d_jerk_v117_signal,
    f39ac_f39_ad_cyclicality_signature_gmgrowth_252d_jerk_v118_signal,
    f39ac_f39_ad_cyclicality_signature_revdowndur_252d_jerk_v119_signal,
    f39ac_f39_ad_cyclicality_signature_salesupdur_252d_jerk_v120_signal,
    f39ac_f39_ad_cyclicality_signature_opmupdur_252d_jerk_v121_signal,
    f39ac_f39_ad_cyclicality_signature_ebmrng504_504d_jerk_v122_signal,
    f39ac_f39_ad_cyclicality_signature_gprng504_504d_jerk_v123_signal,
    f39ac_f39_ad_cyclicality_signature_revrng252z_252d_jerk_v124_signal,
    f39ac_f39_ad_cyclicality_signature_salescycnorm_252d_jerk_v125_signal,
    f39ac_f39_ad_cyclicality_signature_opmcycnorm_252d_jerk_v126_signal,
    f39ac_f39_ad_cyclicality_signature_gmcycnorm_252d_jerk_v127_signal,
    f39ac_f39_ad_cyclicality_signature_revampratio_252d_jerk_v128_signal,
    f39ac_f39_ad_cyclicality_signature_gmprice_252d_jerk_v129_signal,
    f39ac_f39_ad_cyclicality_signature_salesintlevel_252d_jerk_v130_signal,
    f39ac_f39_ad_cyclicality_signature_opmlevel_252d_jerk_v131_signal,
    f39ac_f39_ad_cyclicality_signature_ebmlevel_252d_jerk_v132_signal,
    f39ac_f39_ad_cyclicality_signature_gmlevel_252d_jerk_v133_signal,
    f39ac_f39_ad_cyclicality_signature_revcyclic_252d_jerk_v134_signal,
    f39ac_f39_ad_cyclicality_signature_gpdetr_252d_jerk_v135_signal,
    f39ac_f39_ad_cyclicality_signature_salesintdetr_252d_jerk_v136_signal,
    f39ac_f39_ad_cyclicality_signature_opmphasemom_252d_jerk_v137_signal,
    f39ac_f39_ad_cyclicality_signature_ebmampz504_504d_jerk_v138_signal,
    f39ac_f39_ad_cyclicality_signature_revphasez_252d_jerk_v139_signal,
    f39ac_f39_ad_cyclicality_signature_gmphasez_252d_jerk_v140_signal,
    f39ac_f39_ad_cyclicality_signature_salesampz_252d_jerk_v141_signal,
    f39ac_f39_ad_cyclicality_signature_opmampz_252d_jerk_v142_signal,
    f39ac_f39_ad_cyclicality_signature_revscaleroc_252d_jerk_v143_signal,
    f39ac_f39_ad_cyclicality_signature_gpscaleroc_252d_jerk_v144_signal,
    f39ac_f39_ad_cyclicality_signature_salesscaleroc_252d_jerk_v145_signal,
    f39ac_f39_ad_cyclicality_signature_revgmco_252d_jerk_v146_signal,
    f39ac_f39_ad_cyclicality_signature_salesopco_252d_jerk_v147_signal,
    f39ac_f39_ad_cyclicality_signature_ebmrevco_252d_jerk_v148_signal,
    f39ac_f39_ad_cyclicality_signature_gmexpand_252d_jerk_v149_signal,
    f39ac_f39_ad_cyclicality_signature_revampabs_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F39_AD_CYCLICALITY_SIGNATURE_REGISTRY_001_150 = REGISTRY



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

    cyc = pd.Series(np.sin(np.arange(n) * 2.0 * np.pi / 252.0)
                    + 0.4 * np.sin(np.arange(n) * 2.0 * np.pi / 110.0), name=None)
    revenue = (_fund(101, base=1.2e8, drift=0.025, vol=0.06)
               * (1.0 + 0.22 * cyc)).rename("revenue")
    gp = (_fund(102, base=6.0e7, drift=0.024, vol=0.06)
          * (1.0 + 0.18 * cyc)).rename("gp")
    sgna = (_fund(103, base=3.5e7, drift=0.02, vol=0.05)
            * (1.0 + 0.15 * cyc.shift(20).fillna(0.0))).rename("sgna")
    opinc = (_fund(104, base=1.5e7, drift=0.02, vol=0.10, allow_neg=True)
             * (1.0 + 0.30 * cyc)).rename("opinc")
    ebitdamargin = (0.12 + 0.05 * cyc
                    + pd.Series(np.random.normal(0, 0.01, n))).clip(0.01, 0.6).rename("ebitdamargin")

    cols = {
        "revenue": revenue, "gp": gp, "sgna": sgna,
        "opinc": opinc, "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs not in allowlist: %s" % (name, meta["inputs"])
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

    assert n_features == 150, n_features
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

    print("OK f39_ad_cyclicality_signature_3rd_derivatives_001_150_claude: %d features pass" % n_features)
