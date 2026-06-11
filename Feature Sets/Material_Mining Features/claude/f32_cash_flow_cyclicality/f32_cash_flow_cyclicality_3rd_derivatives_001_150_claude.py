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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


def _jerk(s, w):
    # 2nd math derivative: acceleration = second difference over window w
    d1 = s - s.shift(w)
    return (d1 - d1.shift(w)) / float(w * w)


# ===== folder domain primitives (cash-flow cyclicality) =====
def _fcf_margin(fcf, revenue):
    return fcf / revenue.replace(0, np.nan)


def _ocf_margin(ncfo, revenue):
    return ncfo / revenue.replace(0, np.nan)


def _fcf_after_capex(ncfo, capex):
    return ncfo - capex


def _capex_cover(ncfo, capex):
    return ncfo / capex.replace(0, np.nan)


def _fcf_conversion(fcf, ncfo):
    return fcf / ncfo.replace(0, np.nan)


def _sign_sqrt(s):
    return np.sign(s) * (s.abs() ** 0.5)


def _capex_intensity(capex, revenue):
    return capex / revenue.replace(0, np.nan)


# ============================================================
# Each feature builds a cash-flow base series inline, then returns its 2nd math
# derivative (jerk / acceleration) over a window matched to the base.

# jerk of FCF margin (cash-margin acceleration), 21d
def f32cf_f32_cash_flow_cyclicality_fcfmargin_21d_jerk_v001_signal(fcf, revenue):
    base = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin, 63d (slower cash-margin acceleration)
def f32cf_f32_cash_flow_cyclicality_fcfmargin_63d_jerk_v002_signal(fcf, revenue):
    base = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of smoothed FCF margin, 21d (de-noised cash-margin acceleration)
def f32cf_f32_cash_flow_cyclicality_fcfmarginsm_21d_jerk_v003_signal(fcf, revenue):
    base = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0).rolling(21, min_periods=10).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of OCF margin (operating-cash-margin acceleration), 21d
def f32cf_f32_cash_flow_cyclicality_ocfmargin_21d_jerk_v004_signal(ncfo, revenue):
    base = _ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of OCF margin, 63d
def f32cf_f32_cash_flow_cyclicality_ocfmargin_63d_jerk_v005_signal(ncfo, revenue):
    base = _ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of OCF-minus-FCF margin spread (capex-drag acceleration), 21d
def f32cf_f32_cash_flow_cyclicality_marginspread_21d_jerk_v006_signal(ncfo, fcf, revenue):
    base = (_ocf_margin(ncfo, revenue) - _fcf_margin(fcf, revenue)).clip(lower=-3.0, upper=3.0)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-after-capex (signed-root), 21d (free-cash acceleration)
def f32cf_f32_cash_flow_cyclicality_fcfac_21d_jerk_v007_signal(ncfo, capex):
    base = _sign_sqrt(_fcf_after_capex(ncfo, capex))
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-after-capex (signed-root), 63d
def f32cf_f32_cash_flow_cyclicality_fcfac_63d_jerk_v008_signal(ncfo, capex):
    base = _sign_sqrt(_fcf_after_capex(ncfo, capex))
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of capex coverage (self-funding acceleration), 21d
def f32cf_f32_cash_flow_cyclicality_cover_21d_jerk_v009_signal(ncfo, capex):
    base = _capex_cover(ncfo, capex).clip(lower=-10.0, upper=10.0)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of capex coverage, 63d
def f32cf_f32_cash_flow_cyclicality_cover_63d_jerk_v010_signal(ncfo, capex):
    base = _capex_cover(ncfo, capex).clip(lower=-10.0, upper=10.0)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF conversion (cash-retention acceleration), 21d
def f32cf_f32_cash_flow_cyclicality_conv_21d_jerk_v011_signal(fcf, ncfo):
    base = _fcf_conversion(fcf, ncfo).clip(lower=-5.0, upper=5.0)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF conversion, 63d
def f32cf_f32_cash_flow_cyclicality_conv_63d_jerk_v012_signal(fcf, ncfo):
    base = _fcf_conversion(fcf, ncfo).clip(lower=-5.0, upper=5.0)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-per-share (signed-root), 21d (per-share cash acceleration)
def f32cf_f32_cash_flow_cyclicality_fcfps_21d_jerk_v013_signal(fcfps):
    base = _sign_sqrt(fcfps)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-per-share (signed-root), 63d
def f32cf_f32_cash_flow_cyclicality_fcfps_63d_jerk_v014_signal(fcfps):
    base = _sign_sqrt(fcfps)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of capex intensity (investment-phase acceleration), 21d
def f32cf_f32_cash_flow_cyclicality_capexint_21d_jerk_v015_signal(capex, revenue):
    base = _capex_intensity(capex, revenue)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of capex intensity, 63d
def f32cf_f32_cash_flow_cyclicality_capexint_63d_jerk_v016_signal(capex, revenue):
    base = _capex_intensity(capex, revenue)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin z-score (de-trended cash-margin acceleration), 21d
def f32cf_f32_cash_flow_cyclicality_fcfmarginz_21d_jerk_v017_signal(fcf, revenue):
    m = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    base = _z(m, 252)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of OCF-margin z-score, 63d
def f32cf_f32_cash_flow_cyclicality_ocfmarginz_63d_jerk_v018_signal(ncfo, revenue):
    m = _ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    base = _z(m, 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin cyclical position in 252d range (cash-phase acceleration), 21d
def f32cf_f32_cash_flow_cyclicality_fcfpos_21d_jerk_v019_signal(fcf, revenue):
    m = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    hi = _rmax(m, 252)
    lo = _rmin(m, 252)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of OCF cyclical position in 252d range, 63d
def f32cf_f32_cash_flow_cyclicality_ocfpos_63d_jerk_v020_signal(ncfo):
    s = _sign_sqrt(ncfo)
    hi = _rmax(s, 252)
    lo = _rmin(s, 252)
    base = (s - lo) / (hi - lo).replace(0, np.nan)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin volatility (cash-instability acceleration), 21d
def f32cf_f32_cash_flow_cyclicality_fcfvol_21d_jerk_v021_signal(fcf, revenue):
    m = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    base = m.rolling(126, min_periods=63).std()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of OCF-margin volatility, 63d
def f32cf_f32_cash_flow_cyclicality_ocfvol_63d_jerk_v022_signal(ncfo, revenue):
    m = _ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    base = m.rolling(126, min_periods=63).std()
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin swing amplitude (cyclical-span acceleration), 21d
def f32cf_f32_cash_flow_cyclicality_fcfswing_21d_jerk_v023_signal(fcf, revenue):
    m = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    base = _rmax(m, 252) - _rmin(m, 252)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of capex-coverage cyclical position in 252d range, 21d
def f32cf_f32_cash_flow_cyclicality_coverpos_21d_jerk_v024_signal(ncfo, capex):
    c = _capex_cover(ncfo, capex).clip(lower=-10.0, upper=10.0)
    hi = _rmax(c, 252)
    lo = _rmin(c, 252)
    base = (c - lo) / (hi - lo).replace(0, np.nan)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-after-capex revenue yield z-scored (de-trended free-cash accel), 21d
def f32cf_f32_cash_flow_cyclicality_fcfyieldz_21d_jerk_v025_signal(ncfo, capex, revenue):
    y = (_fcf_after_capex(ncfo, capex) / revenue.replace(0, np.nan)).clip(lower=-3.0, upper=3.0)
    base = _z(y, 252)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of OCF margin smoothed half-year (structural OCF-margin acceleration), 63d
def f32cf_f32_cash_flow_cyclicality_ocfmargin126_63d_jerk_v026_signal(ncfo, revenue):
    base = _ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0).rolling(126, min_periods=63).mean()
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of OCF level (signed-root, raw cash acceleration), 21d
def f32cf_f32_cash_flow_cyclicality_ocf_21d_jerk_v027_signal(ncfo):
    base = _sign_sqrt(ncfo)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF level (signed-root, raw free-cash acceleration), 63d
def f32cf_f32_cash_flow_cyclicality_fcf_63d_jerk_v028_signal(fcf):
    base = _sign_sqrt(fcf)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of capex/OCF ratio (investment-vs-cash acceleration), 21d
def f32cf_f32_cash_flow_cyclicality_capexocf_21d_jerk_v029_signal(capex, ncfo):
    base = (capex / ncfo.replace(0, np.nan)).clip(lower=-10.0, upper=10.0)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin EMA oscillator (fast minus slow), 21d
def f32cf_f32_cash_flow_cyclicality_fcfosc_21d_jerk_v030_signal(fcf, revenue):
    m = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    base = m.ewm(span=42, min_periods=21).mean() - m.ewm(span=126, min_periods=63).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin percentile-rank (rank acceleration), 21d
def f32cf_f32_cash_flow_cyclicality_fcfrank_21d_jerk_v031_signal(fcf, revenue):
    m = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    base = _rank(m, 504)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of capex-coverage rank, 63d
def f32cf_f32_cash_flow_cyclicality_coverrank_63d_jerk_v032_signal(ncfo, capex):
    c = _capex_cover(ncfo, capex).clip(lower=-10.0, upper=10.0)
    base = _rank(c, 504)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-positivity time (cash-positive-prevalence acceleration), 21d
def f32cf_f32_cash_flow_cyclicality_postime_21d_jerk_v033_signal(ncfo, capex):
    f = _fcf_after_capex(ncfo, capex)
    base = (f > 0).astype(float).rolling(252, min_periods=126).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of OCF-margin minus capex intensity (net-cash-margin acceleration), 21d
def f32cf_f32_cash_flow_cyclicality_netmargin_21d_jerk_v034_signal(ncfo, capex, revenue):
    base = (_ocf_margin(ncfo, revenue) - _capex_intensity(capex, revenue)).clip(lower=-3.0, upper=3.0)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin downside semideviation, 63d
def f32cf_f32_cash_flow_cyclicality_downsemi_63d_jerk_v035_signal(fcf, revenue):
    m = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    mu = _mean(m, 252)
    down = (m - mu).clip(upper=0.0)
    base = (down ** 2).rolling(252, min_periods=126).mean() ** 0.5
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-per-share cyclical position in 252d range, 21d
def f32cf_f32_cash_flow_cyclicality_fcfpspos_21d_jerk_v036_signal(fcfps):
    hi = _rmax(fcfps, 252)
    lo = _rmin(fcfps, 252)
    base = (fcfps - lo) / (hi - lo).replace(0, np.nan)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of capex intensity cyclical position in 252d range, 63d
def f32cf_f32_cash_flow_cyclicality_capexpos_63d_jerk_v037_signal(capex, revenue):
    r = _capex_intensity(capex, revenue)
    hi = _rmax(r, 252)
    lo = _rmin(r, 252)
    base = (r - lo) / (hi - lo).replace(0, np.nan)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-after-capex revenue yield smoothed, 21d
def f32cf_f32_cash_flow_cyclicality_fcfyield_21d_jerk_v038_signal(ncfo, capex, revenue):
    base = (_fcf_after_capex(ncfo, capex) / revenue.replace(0, np.nan)).clip(lower=-3.0, upper=3.0).rolling(21, min_periods=10).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of OCF-margin EMA oscillator, 63d
def f32cf_f32_cash_flow_cyclicality_ocfosc_63d_jerk_v039_signal(ncfo, revenue):
    m = _ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    base = m.ewm(span=42, min_periods=21).mean() - m.ewm(span=126, min_periods=63).mean()
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-conversion rank, 21d
def f32cf_f32_cash_flow_cyclicality_convrank_21d_jerk_v040_signal(fcf, ncfo):
    c = _fcf_conversion(fcf, ncfo).clip(lower=-5.0, upper=5.0)
    base = _rank(c, 504)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of capex-coverage minimum over a quarter (worst self-funding accel), 21d
def f32cf_f32_cash_flow_cyclicality_covermin63_21d_jerk_v041_signal(ncfo, capex):
    c = _capex_cover(ncfo, capex).clip(lower=-10.0, upper=10.0)
    base = _rmin(c, 63)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin minus 252d median (anomaly acceleration), 63d
def f32cf_f32_cash_flow_cyclicality_fcfanom_63d_jerk_v042_signal(fcf, revenue):
    m = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    base = m - m.rolling(252, min_periods=126).median()
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin displacement from slow EMA, 21d
def f32cf_f32_cash_flow_cyclicality_fcfdisp_21d_jerk_v043_signal(fcf, revenue):
    m = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    base = m - m.ewm(span=126, min_periods=42).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of OCF-margin coefficient of variation, 63d
def f32cf_f32_cash_flow_cyclicality_ocfcv_63d_jerk_v044_signal(ncfo, revenue):
    m = _ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    sd = m.rolling(252, min_periods=126).std()
    mu = m.abs().rolling(252, min_periods=126).mean()
    base = sd / mu.replace(0, np.nan)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of capex/OCF smoothed (investment-vs-cash trend accel), 63d
def f32cf_f32_cash_flow_cyclicality_capexocfsm_63d_jerk_v045_signal(capex, ncfo):
    base = (capex / ncfo.replace(0, np.nan)).clip(lower=-10.0, upper=10.0).rolling(63, min_periods=21).mean()
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin minus revenue-growth (cash-margin vs top-line accel), 21d
def f32cf_f32_cash_flow_cyclicality_fcfvsrev_21d_jerk_v046_signal(fcf, revenue):
    m = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    revg = np.log(revenue.replace(0, np.nan)) - np.log(revenue.shift(63).replace(0, np.nan))
    base = m - 3.0 * revg
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-after-capex z-score, 63d
def f32cf_f32_cash_flow_cyclicality_fcfacz_63d_jerk_v047_signal(ncfo, capex):
    f = _fcf_after_capex(ncfo, capex)
    base = _z(f, 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-per-share z-score, 21d
def f32cf_f32_cash_flow_cyclicality_fcfpsz_21d_jerk_v048_signal(fcfps):
    base = _z(fcfps, 252)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of capex drawdown from 252d peak (investment-pullback accel), 21d
def f32cf_f32_cash_flow_cyclicality_capexdd_21d_jerk_v049_signal(capex):
    peak = _rmax(capex, 252)
    base = capex / peak.replace(0, np.nan) - 1.0
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of OCF drawdown from 252d peak (cash-strength-loss accel), 63d
def f32cf_f32_cash_flow_cyclicality_ocfdd_63d_jerk_v050_signal(ncfo):
    s = _sign_sqrt(ncfo)
    peak = _rmax(s, 252)
    base = s - peak
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin half-year mean (medium cash-margin accel), 42d
def f32cf_f32_cash_flow_cyclicality_fcfmarginhy_42d_jerk_v051_signal(fcf, revenue):
    base = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0).rolling(126, min_periods=63).mean()
    b = _jerk(base, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of OCF-margin smoothed-quarter, 42d
def f32cf_f32_cash_flow_cyclicality_ocfmarginsm_42d_jerk_v052_signal(ncfo, revenue):
    base = _ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0).rolling(63, min_periods=21).mean()
    b = _jerk(base, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of capex-coverage z-scored vs 126d (shorter self-funding regime accel), 21d
def f32cf_f32_cash_flow_cyclicality_coverz126_21d_jerk_v053_signal(ncfo, capex):
    c = _capex_cover(ncfo, capex).clip(lower=-10.0, upper=10.0)
    base = _z(c, 126)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin recovery off 252d trough, 21d
def f32cf_f32_cash_flow_cyclicality_fcfrec_21d_jerk_v054_signal(fcf, revenue):
    m = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    base = m - _rmin(m, 252)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin distance below 252d peak (downcycle-depth accel), 63d
def f32cf_f32_cash_flow_cyclicality_fcfpeak_63d_jerk_v055_signal(fcf, revenue):
    m = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    base = m - _rmax(m, 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-per-share swing amplitude, 21d
def f32cf_f32_cash_flow_cyclicality_fcfpsswing_21d_jerk_v056_signal(fcfps):
    base = _rmax(fcfps, 252) - _rmin(fcfps, 252)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of OCF-minus-FCF margin spread rank, 63d
def f32cf_f32_cash_flow_cyclicality_dragrank_63d_jerk_v057_signal(ncfo, fcf, revenue):
    drag = (_ocf_margin(ncfo, revenue) - _fcf_margin(fcf, revenue)).clip(lower=-3.0, upper=3.0)
    base = _rank(drag, 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of capex intensity smoothed half-year, 42d
def f32cf_f32_cash_flow_cyclicality_capexinthy_42d_jerk_v058_signal(capex, revenue):
    base = _capex_intensity(capex, revenue).rolling(126, min_periods=63).mean()
    b = _jerk(base, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-conversion displacement from slow EMA (acute retention accel), 21d
def f32cf_f32_cash_flow_cyclicality_convdisp_21d_jerk_v059_signal(fcf, ncfo):
    c = _fcf_conversion(fcf, ncfo).clip(lower=-5.0, upper=5.0)
    base = c - c.ewm(span=126, min_periods=42).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin year-over-year change (cyclical-shift accel), 63d
def f32cf_f32_cash_flow_cyclicality_fcfyoy_63d_jerk_v060_signal(fcf, revenue):
    m = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    base = m - m.shift(252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of OCF risk-adjusted margin (cash Sharpe accel), 21d
def f32cf_f32_cash_flow_cyclicality_ocfrisadj_21d_jerk_v061_signal(ncfo, revenue):
    m = _ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    vol = m.rolling(126, min_periods=63).std()
    base = m.rolling(63, min_periods=21).mean() / vol.replace(0, np.nan)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin skewness, 63d
def f32cf_f32_cash_flow_cyclicality_fcfskew_63d_jerk_v062_signal(fcf, revenue):
    m = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    base = m.rolling(252, min_periods=126).skew()
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin deep-recovery (distance from 1260d trough std-normalized), 21d
def f32cf_f32_cash_flow_cyclicality_deeprec_21d_jerk_v063_signal(fcf, revenue):
    m = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    sd = m.rolling(252, min_periods=126).std().replace(0, np.nan)
    base = (m - _rmin(m, 1260)) / sd
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of capex coverage minus FCF margin (mixed cash-quality accel), 63d
def f32cf_f32_cash_flow_cyclicality_mix_63d_jerk_v064_signal(ncfo, capex, fcf, revenue):
    cov = np.tanh((_capex_cover(ncfo, capex) - 1.0).clip(lower=-10.0, upper=10.0))
    fm = np.tanh(_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0))
    base = cov - fm
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-per-share momentum (per-share cash 3rd-order base), 21d
def f32cf_f32_cash_flow_cyclicality_fcfpsmom_21d_jerk_v065_signal(fcfps):
    s = _sign_sqrt(fcfps)
    base = s - s.shift(63)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of revenue-FCF sync, 63d
def f32cf_f32_cash_flow_cyclicality_sync_63d_jerk_v066_signal(fcf, revenue):
    dfcf = np.sign(fcf - fcf.shift(63))
    drev = np.sign(revenue - revenue.shift(63))
    base = (dfcf * drev).rolling(126, min_periods=63).mean()
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin downcycle-time, 21d
def f32cf_f32_cash_flow_cyclicality_downtime_21d_jerk_v067_signal(fcf, revenue):
    m = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    med = m.rolling(252, min_periods=126).median()
    base = (m < med).astype(float).rolling(252, min_periods=126).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin slope-persistence fraction (trend-quality accel), 21d
def f32cf_f32_cash_flow_cyclicality_persistvel_21d_jerk_v068_signal(fcf, revenue):
    m = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    base = (m > m.shift(5)).astype(float).rolling(63, min_periods=21).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of OCF EMA fast (signed-root), 63d
def f32cf_f32_cash_flow_cyclicality_ocfema_63d_jerk_v069_signal(ncfo):
    s = _sign_sqrt(ncfo)
    base = s.ewm(span=63, min_periods=21).mean()
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of capex coverage z-score, 21d
def f32cf_f32_cash_flow_cyclicality_coverz_21d_jerk_v070_signal(ncfo, capex):
    c = _capex_cover(ncfo, capex).clip(lower=-10.0, upper=10.0)
    base = _z(c, 252)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin minus capex intensity tanh (free-cash-spread accel), 63d
def f32cf_f32_cash_flow_cyclicality_spread2_63d_jerk_v071_signal(fcf, capex, revenue):
    base = np.tanh(_fcf_margin(fcf, revenue).clip(lower=-3, upper=3)) - np.tanh(_capex_intensity(capex, revenue).clip(upper=3))
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-after-capex rank vs 252d, 21d
def f32cf_f32_cash_flow_cyclicality_fcfacrank_21d_jerk_v072_signal(ncfo, capex):
    f = _fcf_after_capex(ncfo, capex)
    base = _rank(f, 252)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of OCF-margin rolling skewness (cash-cycle-shape accel), 63d
def f32cf_f32_cash_flow_cyclicality_ocfskew_63d_jerk_v073_signal(ncfo, revenue):
    m = _ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    base = m.rolling(252, min_periods=126).skew()
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-per-share drawdown, 21d
def f32cf_f32_cash_flow_cyclicality_fcfpsdd_21d_jerk_v074_signal(fcfps):
    s = _sign_sqrt(fcfps)
    peak = _rmax(s, 252)
    base = s - peak
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of capex growth (log) (investment-momentum accel), 21d
def f32cf_f32_cash_flow_cyclicality_capexgrow_21d_jerk_v075_signal(capex):
    lc = np.log(capex.replace(0, np.nan))
    base = lc - lc.shift(63)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin minus per-share blend (cash vs per-share accel), 5d
def f32cf_f32_cash_flow_cyclicality_fcfvsps_5d_jerk_v076_signal(fcf, revenue, fcfps):
    m = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    base = (m - np.tanh(fcfps)).rolling(21, min_periods=10).mean()
    b = _jerk(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of OCF-margin short-window coefficient-of-variation, 5d
def f32cf_f32_cash_flow_cyclicality_ocfcvshort_5d_jerk_v077_signal(ncfo, revenue):
    m = _ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    sd = m.rolling(63, min_periods=21).std()
    mu = m.abs().rolling(63, min_periods=21).mean()
    base = sd / mu.replace(0, np.nan)
    b = _jerk(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of capex-coverage range-width over 63d (self-funding-span accel), 5d
def f32cf_f32_cash_flow_cyclicality_coverspan_5d_jerk_v078_signal(ncfo, capex):
    c = _capex_cover(ncfo, capex).clip(lower=-10.0, upper=10.0)
    base = _rmax(c, 63) - _rmin(c, 63)
    b = _jerk(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-after-capex revenue yield, 63d
def f32cf_f32_cash_flow_cyclicality_fcfyield_63d_jerk_v079_signal(ncfo, capex, revenue):
    base = (_fcf_after_capex(ncfo, capex) / revenue.replace(0, np.nan)).clip(lower=-3.0, upper=3.0)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin within-504d range position, 63d
def f32cf_f32_cash_flow_cyclicality_fcfpos504_63d_jerk_v080_signal(fcf, revenue):
    m = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    hi = _rmax(m, 504)
    lo = _rmin(m, 504)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin volatility 252d, 63d
def f32cf_f32_cash_flow_cyclicality_fcfvol252_63d_jerk_v081_signal(fcf, revenue):
    m = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    base = m.rolling(252, min_periods=126).std()
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of capex-coverage volatility 252d, 21d
def f32cf_f32_cash_flow_cyclicality_covervol_21d_jerk_v082_signal(ncfo, capex):
    c = _capex_cover(ncfo, capex).clip(lower=-10.0, upper=10.0)
    base = c.rolling(252, min_periods=126).std()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF conversion z-score, 63d
def f32cf_f32_cash_flow_cyclicality_convz_63d_jerk_v083_signal(fcf, ncfo):
    c = _fcf_conversion(fcf, ncfo).clip(lower=-5.0, upper=5.0)
    base = _z(c, 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-per-share rank vs 504d, 21d
def f32cf_f32_cash_flow_cyclicality_fcfpsrank_21d_jerk_v084_signal(fcfps):
    base = _rank(fcfps, 504)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of OCF-margin distance below 252d peak std-normalized (downcycle accel), 63d
def f32cf_f32_cash_flow_cyclicality_ocfpeakgap_63d_jerk_v085_signal(ncfo, revenue):
    m = _ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    sd = m.rolling(252, min_periods=126).std().replace(0, np.nan)
    base = (m - _rmax(m, 252)) / sd
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin x capex-coverage interaction smoothed, 42d
def f32cf_f32_cash_flow_cyclicality_fcfcovx_42d_jerk_v086_signal(fcf, ncfo, capex, revenue):
    fm = np.tanh(_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0))
    cov = np.tanh((_capex_cover(ncfo, capex) - 1.0).clip(lower=-10.0, upper=10.0))
    base = (fm * cov).rolling(63, min_periods=21).mean()
    b = _jerk(base, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of capex intensity z-score, 63d
def f32cf_f32_cash_flow_cyclicality_capexintz_63d_jerk_v087_signal(capex, revenue):
    base = _z(_capex_intensity(capex, revenue), 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of capex-drag relative to OCF-margin (drag share of cash), 21d
def f32cf_f32_cash_flow_cyclicality_dragshare_21d_jerk_v088_signal(fcf, ncfo, revenue):
    om = _ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    fm = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    base = ((om - fm) / (om.abs() + 0.05)).clip(lower=-5.0, upper=5.0)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin top-third time, 63d
def f32cf_f32_cash_flow_cyclicality_toptime_63d_jerk_v089_signal(fcf, revenue):
    m = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    hi = _rmax(m, 252)
    lo = _rmin(m, 252)
    pos = (m - lo) / (hi - lo).replace(0, np.nan)
    base = (pos >= 0.6667).astype(float).rolling(252, min_periods=126).mean()
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of OCF-margin minus its 252d median (cash-margin anomaly accel), 21d
def f32cf_f32_cash_flow_cyclicality_ocfanomshort_21d_jerk_v090_signal(ncfo, revenue):
    m = _ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    base = m - m.rolling(252, min_periods=126).median()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin coefficient of variation, 63d
def f32cf_f32_cash_flow_cyclicality_fcfcv_63d_jerk_v091_signal(fcf, revenue):
    m = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    sd = m.rolling(252, min_periods=126).std()
    mu = m.abs().rolling(252, min_periods=126).mean()
    base = sd / mu.replace(0, np.nan)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of capex/OCF rank, 21d
def f32cf_f32_cash_flow_cyclicality_capexocfrank_21d_jerk_v092_signal(capex, ncfo):
    base = _rank((capex / ncfo.replace(0, np.nan)).clip(lower=-10.0, upper=10.0), 252)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin recovery normalized by swing, 63d
def f32cf_f32_cash_flow_cyclicality_fcfrecnorm_63d_jerk_v093_signal(fcf, revenue):
    m = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    base = (m - _rmin(m, 252)) / (_rmax(m, 252) - _rmin(m, 252)).replace(0, np.nan)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-after-capex coefficient of variation, 21d
def f32cf_f32_cash_flow_cyclicality_fcfaccv_21d_jerk_v094_signal(ncfo, capex):
    f = _fcf_after_capex(ncfo, capex)
    sd = _std(f, 126)
    mu = _mean(f.abs(), 126)
    base = sd / mu.replace(0, np.nan)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin EMA oscillator (longer spans), 63d
def f32cf_f32_cash_flow_cyclicality_fcfosc2_63d_jerk_v095_signal(fcf, revenue):
    m = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    base = m.ewm(span=63, min_periods=21).mean() - m.ewm(span=189, min_periods=63).mean()
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of OCF-margin recovery off 252d trough, 21d
def f32cf_f32_cash_flow_cyclicality_ocfrec_21d_jerk_v096_signal(ncfo, revenue):
    m = _ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    base = m - _rmin(m, 252)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of self-funding time (coverage>=1 fraction), 63d
def f32cf_f32_cash_flow_cyclicality_selffund_63d_jerk_v097_signal(ncfo, capex):
    base = (ncfo >= capex).astype(float).rolling(252, min_periods=126).mean()
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin rank vs 252d (cash-margin percentile accel), 42d
def f32cf_f32_cash_flow_cyclicality_fcfrank252_42d_jerk_v098_signal(fcf, revenue):
    m = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    base = _rank(m, 252)
    b = _jerk(base, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of OCF margin (raw), 42d
def f32cf_f32_cash_flow_cyclicality_ocfmargin_42d_jerk_v099_signal(ncfo, revenue):
    base = _ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    b = _jerk(base, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of capex coverage (raw), 42d
def f32cf_f32_cash_flow_cyclicality_cover_42d_jerk_v100_signal(ncfo, capex):
    base = _capex_cover(ncfo, capex).clip(lower=-10.0, upper=10.0)
    b = _jerk(base, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-after-capex (signed-root), 42d
def f32cf_f32_cash_flow_cyclicality_fcfac_42d_jerk_v101_signal(ncfo, capex):
    base = _sign_sqrt(_fcf_after_capex(ncfo, capex))
    b = _jerk(base, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF conversion (raw), 42d
def f32cf_f32_cash_flow_cyclicality_conv_42d_jerk_v102_signal(fcf, ncfo):
    base = _fcf_conversion(fcf, ncfo).clip(lower=-5.0, upper=5.0)
    b = _jerk(base, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-per-share (signed-root), 42d
def f32cf_f32_cash_flow_cyclicality_fcfps_42d_jerk_v103_signal(fcfps):
    base = _sign_sqrt(fcfps)
    b = _jerk(base, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of capex intensity (raw), 42d
def f32cf_f32_cash_flow_cyclicality_capexint_42d_jerk_v104_signal(capex, revenue):
    base = _capex_intensity(capex, revenue)
    b = _jerk(base, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin z (126d window), 42d
def f32cf_f32_cash_flow_cyclicality_fcfmarginz126_42d_jerk_v105_signal(fcf, revenue):
    m = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    base = _z(m, 126)
    b = _jerk(base, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of OCF momentum-diff (cash-accel base), 21d
def f32cf_f32_cash_flow_cyclicality_ocfmomdiff_21d_jerk_v106_signal(ncfo):
    s = _sign_sqrt(ncfo)
    base = (s - s.shift(63)) - (s - s.shift(252)) / 4.0
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin oscillator smoothed, 21d
def f32cf_f32_cash_flow_cyclicality_fcfoscsm_21d_jerk_v107_signal(fcf, revenue):
    m = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    osc = m.ewm(span=42, min_periods=21).mean() - m.ewm(span=126, min_periods=63).mean()
    base = osc.rolling(21, min_periods=10).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of capex-coverage half-year vs full-year tilt, 42d
def f32cf_f32_cash_flow_cyclicality_covertilt_42d_jerk_v108_signal(ncfo, capex):
    c = _capex_cover(ncfo, capex).clip(lower=-10.0, upper=10.0)
    base = c.rolling(126, min_periods=63).mean() - c.rolling(252, min_periods=126).mean()
    b = _jerk(base, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin downside semideviation half-year, 21d
def f32cf_f32_cash_flow_cyclicality_downsemi_21d_jerk_v109_signal(fcf, revenue):
    m = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    mu = _mean(m, 126)
    down = (m - mu).clip(upper=0.0)
    base = (down ** 2).rolling(126, min_periods=63).mean() ** 0.5
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of OCF-margin upside semideviation, 63d
def f32cf_f32_cash_flow_cyclicality_upsemi_63d_jerk_v110_signal(ncfo, revenue):
    m = _ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    mu = _mean(m, 252)
    up = (m - mu).clip(lower=0.0)
    base = (up ** 2).rolling(252, min_periods=126).mean() ** 0.5
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin slope-persistence, 21d
def f32cf_f32_cash_flow_cyclicality_slopepersist_21d_jerk_v111_signal(fcf, revenue):
    m = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    base = (m > m.shift(21)).astype(float).rolling(126, min_periods=63).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of capex-coverage minimum half-year, 21d
def f32cf_f32_cash_flow_cyclicality_covermin_21d_jerk_v112_signal(ncfo, capex):
    c = _capex_cover(ncfo, capex).clip(lower=-10.0, upper=10.0)
    base = _rmin(c, 126)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin asymmetry (peak vs trough distance), 63d
def f32cf_f32_cash_flow_cyclicality_fcfasym_63d_jerk_v113_signal(fcf, revenue):
    m = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    mid = _mean(m, 252)
    base = (_rmax(m, 252) - mid) - (mid - _rmin(m, 252))
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin near-zero chop time, 21d
def f32cf_f32_cash_flow_cyclicality_chop_21d_jerk_v114_signal(fcf, revenue):
    m = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    band = m.rolling(252, min_periods=126).std() * 0.5
    base = (m.abs() <= band).astype(float).rolling(252, min_periods=126).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of OCF swing over revenue, 63d
def f32cf_f32_cash_flow_cyclicality_ocfswing_63d_jerk_v115_signal(ncfo, revenue):
    base = ((_rmax(ncfo, 252) - _rmin(ncfo, 252)) / _mean(revenue, 252).replace(0, np.nan)).clip(upper=5.0)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-per-share coefficient of variation, 63d
def f32cf_f32_cash_flow_cyclicality_fcfpscv_63d_jerk_v116_signal(fcfps):
    sd = _std(fcfps, 252)
    mu = _mean(fcfps.abs(), 252)
    base = sd / mu.replace(0, np.nan)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin bottom-score (cycle-bottom accel), 21d
def f32cf_f32_cash_flow_cyclicality_bottom_21d_jerk_v117_signal(fcf, revenue):
    m = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    med = m.rolling(252, min_periods=126).median()
    depth = (med - m).clip(lower=0)
    rising = (m - m.shift(63)).clip(lower=0)
    base = np.tanh(depth) * np.tanh(rising)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of capex spike prevalence, 63d
def f32cf_f32_cash_flow_cyclicality_capexspike_63d_jerk_v118_signal(capex):
    mu = _mean(capex, 252)
    sd = _std(capex, 252)
    base = (capex > (mu + sd)).astype(float).rolling(252, min_periods=126).mean()
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of OCF-margin minus FCF-margin (drag) smoothed, 21d
def f32cf_f32_cash_flow_cyclicality_dragsm_21d_jerk_v119_signal(ncfo, fcf, revenue):
    base = (_ocf_margin(ncfo, revenue) - _fcf_margin(fcf, revenue)).clip(lower=-3.0, upper=3.0).rolling(63, min_periods=21).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF conversion EMA, 63d
def f32cf_f32_cash_flow_cyclicality_convema_63d_jerk_v120_signal(fcf, ncfo):
    c = _fcf_conversion(fcf, ncfo).clip(lower=-5.0, upper=5.0)
    base = c.ewm(span=63, min_periods=21).mean()
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of deep cash-margin percentile vs 1260d (full-cycle percentile accel), 63d
def f32cf_f32_cash_flow_cyclicality_deeprank_63d_jerk_v121_signal(fcf, revenue):
    m = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    base = _rank(m, 1260)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-after-capex displacement from slow EMA (acute free-cash accel), 21d
def f32cf_f32_cash_flow_cyclicality_fcfacdisp_21d_jerk_v122_signal(ncfo, capex):
    s = _sign_sqrt(_fcf_after_capex(ncfo, capex))
    base = s - s.ewm(span=126, min_periods=42).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of OCF-margin minus capex/OCF (cash net of investment-intensity mix), 63d
def f32cf_f32_cash_flow_cyclicality_ocfnetinv_63d_jerk_v123_signal(ncfo, capex, revenue):
    om = _ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    inv = (capex / ncfo.replace(0, np.nan)).clip(lower=-5.0, upper=5.0)
    base = om - 0.3 * inv
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of capex coverage displacement from EMA, 21d
def f32cf_f32_cash_flow_cyclicality_coverdisp_21d_jerk_v124_signal(ncfo, capex):
    c = _capex_cover(ncfo, capex).clip(lower=-10.0, upper=10.0)
    base = c - c.ewm(span=126, min_periods=42).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin durability (positivity x conversion), 63d
def f32cf_f32_cash_flow_cyclicality_durability_63d_jerk_v125_signal(fcf, ncfo):
    postime = (fcf > 0).astype(float).rolling(252, min_periods=126).mean()
    conv = _fcf_conversion(fcf, ncfo).clip(lower=-5.0, upper=5.0).rolling(63, min_periods=21).mean()
    base = postime * np.tanh(conv)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin top-score (cycle-top accel), 21d
def f32cf_f32_cash_flow_cyclicality_top_21d_jerk_v126_signal(ncfo, revenue):
    m = _ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    med = m.rolling(252, min_periods=126).median()
    height = (m - med).clip(lower=0)
    falling = (m.shift(63) - m).clip(lower=0)
    base = np.tanh(height) * np.tanh(falling)
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin within-504d range position smoothed, 21d
def f32cf_f32_cash_flow_cyclicality_fcfpos504sm_21d_jerk_v127_signal(fcf, revenue):
    m = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    hi = _rmax(m, 504)
    lo = _rmin(m, 504)
    base = ((m - lo) / (hi - lo).replace(0, np.nan)).rolling(21, min_periods=10).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of capex/OCF year-over-year change, 63d
def f32cf_f32_cash_flow_cyclicality_capexocfyoy_63d_jerk_v128_signal(capex, ncfo):
    r = (capex / ncfo.replace(0, np.nan)).clip(lower=-10.0, upper=10.0)
    base = r - r.shift(252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin short-mean minus its median (recent-vs-typical accel), 21d
def f32cf_f32_cash_flow_cyclicality_fcftermmed_21d_jerk_v129_signal(fcf, revenue):
    m = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    base = m.rolling(42, min_periods=21).mean() - m.rolling(252, min_periods=126).median()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of OCF-margin term spread, 63d
def f32cf_f32_cash_flow_cyclicality_ocfterm_63d_jerk_v130_signal(ncfo, revenue):
    m = _ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    base = m.rolling(63, min_periods=21).mean() - m.rolling(252, min_periods=126).mean()
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-per-share within-504d range position, 63d
def f32cf_f32_cash_flow_cyclicality_fcfpspos504_63d_jerk_v131_signal(fcfps):
    hi = _rmax(fcfps, 504)
    lo = _rmin(fcfps, 504)
    base = (fcfps - lo) / (hi - lo).replace(0, np.nan)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of capex-coverage minus its 252d median (self-funding anomaly), 21d
def f32cf_f32_cash_flow_cyclicality_coveranom_21d_jerk_v132_signal(ncfo, capex):
    c = _capex_cover(ncfo, capex).clip(lower=-10.0, upper=10.0)
    base = c - c.rolling(252, min_periods=126).median()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF margin (signed-root yield) smoothed half-year, 42d
def f32cf_f32_cash_flow_cyclicality_fcfsrhy_42d_jerk_v133_signal(fcf, revenue):
    base = _sign_sqrt(_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)).rolling(126, min_periods=63).mean()
    b = _jerk(base, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of OCF-margin half-year vs full-year tilt, 21d
def f32cf_f32_cash_flow_cyclicality_ocftilt_21d_jerk_v134_signal(ncfo, revenue):
    m = _ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    base = m.rolling(126, min_periods=63).mean() - m.rolling(252, min_periods=126).median()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin vol-of-vol, 63d
def f32cf_f32_cash_flow_cyclicality_volofvol_63d_jerk_v135_signal(fcf, revenue):
    m = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    v = m.rolling(63, min_periods=21).std()
    base = v.rolling(252, min_periods=126).std()
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF conversion rank, 63d
def f32cf_f32_cash_flow_cyclicality_convrank2_63d_jerk_v136_signal(fcf, ncfo):
    c = _fcf_conversion(fcf, ncfo).clip(lower=-5.0, upper=5.0)
    base = _rank(c, 252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of capex intensity within-252d range smoothed, 21d
def f32cf_f32_cash_flow_cyclicality_capexpossm_21d_jerk_v137_signal(capex, revenue):
    r = _capex_intensity(capex, revenue)
    hi = _rmax(r, 252)
    lo = _rmin(r, 252)
    base = ((r - lo) / (hi - lo).replace(0, np.nan)).rolling(21, min_periods=10).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin minus capex-intensity (net free cash) signed-root, 63d
def f32cf_f32_cash_flow_cyclicality_netfreesr_63d_jerk_v138_signal(fcf, capex, revenue):
    base = _sign_sqrt((_fcf_margin(fcf, revenue) - _capex_intensity(capex, revenue)).clip(lower=-3.0, upper=3.0))
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of OCF-margin within-252d range position smoothed, 42d
def f32cf_f32_cash_flow_cyclicality_ocfpossm_42d_jerk_v139_signal(ncfo, revenue):
    m = _ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    hi = _rmax(m, 252)
    lo = _rmin(m, 252)
    base = ((m - lo) / (hi - lo).replace(0, np.nan)).rolling(42, min_periods=21).mean()
    b = _jerk(base, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin x capex-coverage blend EMA (cash-quality blend accel), 63d
def f32cf_f32_cash_flow_cyclicality_qualblend_63d_jerk_v140_signal(fcf, ncfo, capex, revenue):
    fm = np.tanh(_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0))
    cov = np.tanh((_capex_cover(ncfo, capex) - 1.0).clip(lower=-10.0, upper=10.0))
    base = (fm + cov).ewm(span=63, min_periods=21).mean()
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-after-capex YoY change (free-cash cyclical-shift accel), 63d
def f32cf_f32_cash_flow_cyclicality_fcfacyoy_63d_jerk_v141_signal(ncfo, capex):
    f = _sign_sqrt(_fcf_after_capex(ncfo, capex))
    base = f - f.shift(252)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of capex coverage minus revenue-growth (cash-vs-growth), 21d
def f32cf_f32_cash_flow_cyclicality_covgrow_21d_jerk_v142_signal(ncfo, capex, revenue):
    cov = np.tanh((_capex_cover(ncfo, capex) - 1.0).clip(lower=-10.0, upper=10.0))
    revg = np.log(revenue.replace(0, np.nan)) - np.log(revenue.shift(63).replace(0, np.nan))
    base = cov - 5.0 * revg
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin downside-vol minus upside-vol (semivol skew), 63d
def f32cf_f32_cash_flow_cyclicality_semiskew_63d_jerk_v143_signal(fcf, revenue):
    m = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    mu = _mean(m, 252)
    down = ((m - mu).clip(upper=0.0) ** 2).rolling(252, min_periods=126).mean() ** 0.5
    up = ((m - mu).clip(lower=0.0) ** 2).rolling(252, min_periods=126).mean() ** 0.5
    base = down - up
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of OCF-margin short-window volatility (cash-margin instability accel), 21d
def f32cf_f32_cash_flow_cyclicality_ocfvolshort_21d_jerk_v144_signal(ncfo, revenue):
    m = _ocf_margin(ncfo, revenue).clip(lower=-3.0, upper=3.0)
    base = m.rolling(63, min_periods=21).std()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin x coverage quality product, 63d
def f32cf_f32_cash_flow_cyclicality_quality_63d_jerk_v145_signal(fcf, ncfo, capex, revenue):
    fm = np.tanh(_fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0))
    cov = np.tanh((_capex_cover(ncfo, capex) - 1.0).clip(lower=-10.0, upper=10.0))
    base = fm * (0.5 + 0.5 * cov)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-per-share half-year vs full-year tilt, 21d
def f32cf_f32_cash_flow_cyclicality_fcfpstilt_21d_jerk_v146_signal(fcfps):
    s = _sign_sqrt(fcfps)
    base = s.rolling(126, min_periods=63).mean() - s.rolling(252, min_periods=126).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of capex coverage within-252d range position smoothed, 42d
def f32cf_f32_cash_flow_cyclicality_coverpossm_42d_jerk_v147_signal(ncfo, capex):
    c = _capex_cover(ncfo, capex).clip(lower=-10.0, upper=10.0)
    hi = _rmax(c, 252)
    lo = _rmin(c, 252)
    base = ((c - lo) / (hi - lo).replace(0, np.nan)).rolling(42, min_periods=21).mean()
    b = _jerk(base, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin within-1260d range position smoothed, 63d
def f32cf_f32_cash_flow_cyclicality_fcfpos1260sm_63d_jerk_v148_signal(fcf, revenue):
    m = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    hi = _rmax(m, 1260)
    lo = _rmin(m, 1260)
    base = ((m - lo) / (hi - lo).replace(0, np.nan)).rolling(63, min_periods=21).mean()
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of FCF-margin EMA oscillator histogram (osc minus its EMA), 21d
def f32cf_f32_cash_flow_cyclicality_oschist_21d_jerk_v149_signal(fcf, revenue):
    m = _fcf_margin(fcf, revenue).clip(lower=-3.0, upper=3.0)
    osc = m.ewm(span=42, min_periods=21).mean() - m.ewm(span=126, min_periods=63).mean()
    base = osc - osc.ewm(span=21, min_periods=10).mean()
    b = _jerk(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of whole-cycle cash quality (momentum over jaggedness), 63d
def f32cf_f32_cash_flow_cyclicality_cyclequal_63d_jerk_v150_signal(ncfo, capex, revenue):
    f = _fcf_after_capex(ncfo, capex)
    y = (f / revenue.replace(0, np.nan)).clip(lower=-3.0, upper=3.0)
    mom = y.rolling(63, min_periods=21).mean() - y.rolling(252, min_periods=126).mean()
    jag = (y - y.shift(21)).abs().rolling(252, min_periods=126).mean()
    base = mom / (jag + jag.rolling(252, min_periods=126).mean()).replace(0, np.nan)
    b = _jerk(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f32cf_f32_cash_flow_cyclicality_fcfmargin_21d_jerk_v001_signal,
    f32cf_f32_cash_flow_cyclicality_fcfmargin_63d_jerk_v002_signal,
    f32cf_f32_cash_flow_cyclicality_fcfmarginsm_21d_jerk_v003_signal,
    f32cf_f32_cash_flow_cyclicality_ocfmargin_21d_jerk_v004_signal,
    f32cf_f32_cash_flow_cyclicality_ocfmargin_63d_jerk_v005_signal,
    f32cf_f32_cash_flow_cyclicality_marginspread_21d_jerk_v006_signal,
    f32cf_f32_cash_flow_cyclicality_fcfac_21d_jerk_v007_signal,
    f32cf_f32_cash_flow_cyclicality_fcfac_63d_jerk_v008_signal,
    f32cf_f32_cash_flow_cyclicality_cover_21d_jerk_v009_signal,
    f32cf_f32_cash_flow_cyclicality_cover_63d_jerk_v010_signal,
    f32cf_f32_cash_flow_cyclicality_conv_21d_jerk_v011_signal,
    f32cf_f32_cash_flow_cyclicality_conv_63d_jerk_v012_signal,
    f32cf_f32_cash_flow_cyclicality_fcfps_21d_jerk_v013_signal,
    f32cf_f32_cash_flow_cyclicality_fcfps_63d_jerk_v014_signal,
    f32cf_f32_cash_flow_cyclicality_capexint_21d_jerk_v015_signal,
    f32cf_f32_cash_flow_cyclicality_capexint_63d_jerk_v016_signal,
    f32cf_f32_cash_flow_cyclicality_fcfmarginz_21d_jerk_v017_signal,
    f32cf_f32_cash_flow_cyclicality_ocfmarginz_63d_jerk_v018_signal,
    f32cf_f32_cash_flow_cyclicality_fcfpos_21d_jerk_v019_signal,
    f32cf_f32_cash_flow_cyclicality_ocfpos_63d_jerk_v020_signal,
    f32cf_f32_cash_flow_cyclicality_fcfvol_21d_jerk_v021_signal,
    f32cf_f32_cash_flow_cyclicality_ocfvol_63d_jerk_v022_signal,
    f32cf_f32_cash_flow_cyclicality_fcfswing_21d_jerk_v023_signal,
    f32cf_f32_cash_flow_cyclicality_coverpos_21d_jerk_v024_signal,
    f32cf_f32_cash_flow_cyclicality_fcfyieldz_21d_jerk_v025_signal,
    f32cf_f32_cash_flow_cyclicality_ocfmargin126_63d_jerk_v026_signal,
    f32cf_f32_cash_flow_cyclicality_ocf_21d_jerk_v027_signal,
    f32cf_f32_cash_flow_cyclicality_fcf_63d_jerk_v028_signal,
    f32cf_f32_cash_flow_cyclicality_capexocf_21d_jerk_v029_signal,
    f32cf_f32_cash_flow_cyclicality_fcfosc_21d_jerk_v030_signal,
    f32cf_f32_cash_flow_cyclicality_fcfrank_21d_jerk_v031_signal,
    f32cf_f32_cash_flow_cyclicality_coverrank_63d_jerk_v032_signal,
    f32cf_f32_cash_flow_cyclicality_postime_21d_jerk_v033_signal,
    f32cf_f32_cash_flow_cyclicality_netmargin_21d_jerk_v034_signal,
    f32cf_f32_cash_flow_cyclicality_downsemi_63d_jerk_v035_signal,
    f32cf_f32_cash_flow_cyclicality_fcfpspos_21d_jerk_v036_signal,
    f32cf_f32_cash_flow_cyclicality_capexpos_63d_jerk_v037_signal,
    f32cf_f32_cash_flow_cyclicality_fcfyield_21d_jerk_v038_signal,
    f32cf_f32_cash_flow_cyclicality_ocfosc_63d_jerk_v039_signal,
    f32cf_f32_cash_flow_cyclicality_convrank_21d_jerk_v040_signal,
    f32cf_f32_cash_flow_cyclicality_covermin63_21d_jerk_v041_signal,
    f32cf_f32_cash_flow_cyclicality_fcfanom_63d_jerk_v042_signal,
    f32cf_f32_cash_flow_cyclicality_fcfdisp_21d_jerk_v043_signal,
    f32cf_f32_cash_flow_cyclicality_ocfcv_63d_jerk_v044_signal,
    f32cf_f32_cash_flow_cyclicality_capexocfsm_63d_jerk_v045_signal,
    f32cf_f32_cash_flow_cyclicality_fcfvsrev_21d_jerk_v046_signal,
    f32cf_f32_cash_flow_cyclicality_fcfacz_63d_jerk_v047_signal,
    f32cf_f32_cash_flow_cyclicality_fcfpsz_21d_jerk_v048_signal,
    f32cf_f32_cash_flow_cyclicality_capexdd_21d_jerk_v049_signal,
    f32cf_f32_cash_flow_cyclicality_ocfdd_63d_jerk_v050_signal,
    f32cf_f32_cash_flow_cyclicality_fcfmarginhy_42d_jerk_v051_signal,
    f32cf_f32_cash_flow_cyclicality_ocfmarginsm_42d_jerk_v052_signal,
    f32cf_f32_cash_flow_cyclicality_coverz126_21d_jerk_v053_signal,
    f32cf_f32_cash_flow_cyclicality_fcfrec_21d_jerk_v054_signal,
    f32cf_f32_cash_flow_cyclicality_fcfpeak_63d_jerk_v055_signal,
    f32cf_f32_cash_flow_cyclicality_fcfpsswing_21d_jerk_v056_signal,
    f32cf_f32_cash_flow_cyclicality_dragrank_63d_jerk_v057_signal,
    f32cf_f32_cash_flow_cyclicality_capexinthy_42d_jerk_v058_signal,
    f32cf_f32_cash_flow_cyclicality_convdisp_21d_jerk_v059_signal,
    f32cf_f32_cash_flow_cyclicality_fcfyoy_63d_jerk_v060_signal,
    f32cf_f32_cash_flow_cyclicality_ocfrisadj_21d_jerk_v061_signal,
    f32cf_f32_cash_flow_cyclicality_fcfskew_63d_jerk_v062_signal,
    f32cf_f32_cash_flow_cyclicality_deeprec_21d_jerk_v063_signal,
    f32cf_f32_cash_flow_cyclicality_mix_63d_jerk_v064_signal,
    f32cf_f32_cash_flow_cyclicality_fcfpsmom_21d_jerk_v065_signal,
    f32cf_f32_cash_flow_cyclicality_sync_63d_jerk_v066_signal,
    f32cf_f32_cash_flow_cyclicality_downtime_21d_jerk_v067_signal,
    f32cf_f32_cash_flow_cyclicality_persistvel_21d_jerk_v068_signal,
    f32cf_f32_cash_flow_cyclicality_ocfema_63d_jerk_v069_signal,
    f32cf_f32_cash_flow_cyclicality_coverz_21d_jerk_v070_signal,
    f32cf_f32_cash_flow_cyclicality_spread2_63d_jerk_v071_signal,
    f32cf_f32_cash_flow_cyclicality_fcfacrank_21d_jerk_v072_signal,
    f32cf_f32_cash_flow_cyclicality_ocfskew_63d_jerk_v073_signal,
    f32cf_f32_cash_flow_cyclicality_fcfpsdd_21d_jerk_v074_signal,
    f32cf_f32_cash_flow_cyclicality_capexgrow_21d_jerk_v075_signal,
    f32cf_f32_cash_flow_cyclicality_fcfvsps_5d_jerk_v076_signal,
    f32cf_f32_cash_flow_cyclicality_ocfcvshort_5d_jerk_v077_signal,
    f32cf_f32_cash_flow_cyclicality_coverspan_5d_jerk_v078_signal,
    f32cf_f32_cash_flow_cyclicality_fcfyield_63d_jerk_v079_signal,
    f32cf_f32_cash_flow_cyclicality_fcfpos504_63d_jerk_v080_signal,
    f32cf_f32_cash_flow_cyclicality_fcfvol252_63d_jerk_v081_signal,
    f32cf_f32_cash_flow_cyclicality_covervol_21d_jerk_v082_signal,
    f32cf_f32_cash_flow_cyclicality_convz_63d_jerk_v083_signal,
    f32cf_f32_cash_flow_cyclicality_fcfpsrank_21d_jerk_v084_signal,
    f32cf_f32_cash_flow_cyclicality_ocfpeakgap_63d_jerk_v085_signal,
    f32cf_f32_cash_flow_cyclicality_fcfcovx_42d_jerk_v086_signal,
    f32cf_f32_cash_flow_cyclicality_capexintz_63d_jerk_v087_signal,
    f32cf_f32_cash_flow_cyclicality_dragshare_21d_jerk_v088_signal,
    f32cf_f32_cash_flow_cyclicality_toptime_63d_jerk_v089_signal,
    f32cf_f32_cash_flow_cyclicality_ocfanomshort_21d_jerk_v090_signal,
    f32cf_f32_cash_flow_cyclicality_fcfcv_63d_jerk_v091_signal,
    f32cf_f32_cash_flow_cyclicality_capexocfrank_21d_jerk_v092_signal,
    f32cf_f32_cash_flow_cyclicality_fcfrecnorm_63d_jerk_v093_signal,
    f32cf_f32_cash_flow_cyclicality_fcfaccv_21d_jerk_v094_signal,
    f32cf_f32_cash_flow_cyclicality_fcfosc2_63d_jerk_v095_signal,
    f32cf_f32_cash_flow_cyclicality_ocfrec_21d_jerk_v096_signal,
    f32cf_f32_cash_flow_cyclicality_selffund_63d_jerk_v097_signal,
    f32cf_f32_cash_flow_cyclicality_fcfrank252_42d_jerk_v098_signal,
    f32cf_f32_cash_flow_cyclicality_ocfmargin_42d_jerk_v099_signal,
    f32cf_f32_cash_flow_cyclicality_cover_42d_jerk_v100_signal,
    f32cf_f32_cash_flow_cyclicality_fcfac_42d_jerk_v101_signal,
    f32cf_f32_cash_flow_cyclicality_conv_42d_jerk_v102_signal,
    f32cf_f32_cash_flow_cyclicality_fcfps_42d_jerk_v103_signal,
    f32cf_f32_cash_flow_cyclicality_capexint_42d_jerk_v104_signal,
    f32cf_f32_cash_flow_cyclicality_fcfmarginz126_42d_jerk_v105_signal,
    f32cf_f32_cash_flow_cyclicality_ocfmomdiff_21d_jerk_v106_signal,
    f32cf_f32_cash_flow_cyclicality_fcfoscsm_21d_jerk_v107_signal,
    f32cf_f32_cash_flow_cyclicality_covertilt_42d_jerk_v108_signal,
    f32cf_f32_cash_flow_cyclicality_downsemi_21d_jerk_v109_signal,
    f32cf_f32_cash_flow_cyclicality_upsemi_63d_jerk_v110_signal,
    f32cf_f32_cash_flow_cyclicality_slopepersist_21d_jerk_v111_signal,
    f32cf_f32_cash_flow_cyclicality_covermin_21d_jerk_v112_signal,
    f32cf_f32_cash_flow_cyclicality_fcfasym_63d_jerk_v113_signal,
    f32cf_f32_cash_flow_cyclicality_chop_21d_jerk_v114_signal,
    f32cf_f32_cash_flow_cyclicality_ocfswing_63d_jerk_v115_signal,
    f32cf_f32_cash_flow_cyclicality_fcfpscv_63d_jerk_v116_signal,
    f32cf_f32_cash_flow_cyclicality_bottom_21d_jerk_v117_signal,
    f32cf_f32_cash_flow_cyclicality_capexspike_63d_jerk_v118_signal,
    f32cf_f32_cash_flow_cyclicality_dragsm_21d_jerk_v119_signal,
    f32cf_f32_cash_flow_cyclicality_convema_63d_jerk_v120_signal,
    f32cf_f32_cash_flow_cyclicality_deeprank_63d_jerk_v121_signal,
    f32cf_f32_cash_flow_cyclicality_fcfacdisp_21d_jerk_v122_signal,
    f32cf_f32_cash_flow_cyclicality_ocfnetinv_63d_jerk_v123_signal,
    f32cf_f32_cash_flow_cyclicality_coverdisp_21d_jerk_v124_signal,
    f32cf_f32_cash_flow_cyclicality_durability_63d_jerk_v125_signal,
    f32cf_f32_cash_flow_cyclicality_top_21d_jerk_v126_signal,
    f32cf_f32_cash_flow_cyclicality_fcfpos504sm_21d_jerk_v127_signal,
    f32cf_f32_cash_flow_cyclicality_capexocfyoy_63d_jerk_v128_signal,
    f32cf_f32_cash_flow_cyclicality_fcftermmed_21d_jerk_v129_signal,
    f32cf_f32_cash_flow_cyclicality_ocfterm_63d_jerk_v130_signal,
    f32cf_f32_cash_flow_cyclicality_fcfpspos504_63d_jerk_v131_signal,
    f32cf_f32_cash_flow_cyclicality_coveranom_21d_jerk_v132_signal,
    f32cf_f32_cash_flow_cyclicality_fcfsrhy_42d_jerk_v133_signal,
    f32cf_f32_cash_flow_cyclicality_ocftilt_21d_jerk_v134_signal,
    f32cf_f32_cash_flow_cyclicality_volofvol_63d_jerk_v135_signal,
    f32cf_f32_cash_flow_cyclicality_convrank2_63d_jerk_v136_signal,
    f32cf_f32_cash_flow_cyclicality_capexpossm_21d_jerk_v137_signal,
    f32cf_f32_cash_flow_cyclicality_netfreesr_63d_jerk_v138_signal,
    f32cf_f32_cash_flow_cyclicality_ocfpossm_42d_jerk_v139_signal,
    f32cf_f32_cash_flow_cyclicality_qualblend_63d_jerk_v140_signal,
    f32cf_f32_cash_flow_cyclicality_fcfacyoy_63d_jerk_v141_signal,
    f32cf_f32_cash_flow_cyclicality_covgrow_21d_jerk_v142_signal,
    f32cf_f32_cash_flow_cyclicality_semiskew_63d_jerk_v143_signal,
    f32cf_f32_cash_flow_cyclicality_ocfvolshort_21d_jerk_v144_signal,
    f32cf_f32_cash_flow_cyclicality_quality_63d_jerk_v145_signal,
    f32cf_f32_cash_flow_cyclicality_fcfpstilt_21d_jerk_v146_signal,
    f32cf_f32_cash_flow_cyclicality_coverpossm_42d_jerk_v147_signal,
    f32cf_f32_cash_flow_cyclicality_fcfpos1260sm_63d_jerk_v148_signal,
    f32cf_f32_cash_flow_cyclicality_oschist_21d_jerk_v149_signal,
    f32cf_f32_cash_flow_cyclicality_cyclequal_63d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F32_CASH_FLOW_CYCLICALITY_REGISTRY_3RD_001_150 = REGISTRY


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

    fcf = _fund(3201, base=1.0e8, drift=-0.01, vol=0.24, allow_neg=True).rename("fcf")
    ncfo = _fund(3202, base=1.2e8, drift=0.0, vol=0.20, allow_neg=True).rename("ncfo")
    fcfps = _fund(3203, base=4.0, drift=-0.005, vol=0.26, allow_neg=True).rename("fcfps")
    revenue = _fund(3204, base=3.0e8, drift=0.015, vol=0.07).rename("revenue")
    capex = _fund(3205, base=7.0e7, drift=0.01, vol=0.16).rename("capex")

    cols = {"fcf": fcf, "ncfo": ncfo, "fcfps": fcfps,
            "revenue": revenue, "capex": capex}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        assert any(c in ("fcf", "ncfo", "fcfps", "revenue", "capex")
                   for c in meta["inputs"]), name
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

    print("OK f32_cash_flow_cyclicality_3rd_derivatives_001_150_claude: %d features pass" % n_features)
