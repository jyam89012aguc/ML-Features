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


def _slope(s, w):
    # 1st math derivative: rate of change over w trading days
    return (s - s.shift(w)) / float(w)


def _accel(s, w):
    # 2nd math derivative (jerk): change of the slope over w trading days
    sl = (s - s.shift(w)) / float(w)
    return (sl - sl.shift(w)) / float(w)


# ===== folder domain primitives (margin cyclicality) =====
def _amplitude(s, w):
    return _rmax(s, w) - _rmin(s, w)


def _range_pos(s, w):
    hi = _rmax(s, w)
    lo = _rmin(s, w)
    return (s - lo) / (hi - lo).replace(0, np.nan)


# jerk of gmlevel (63d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmlevel_21d_jerk_v001_signal(grossmargin):
    base = grossmargin.rolling(63, min_periods=21).mean()
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmlevel (126d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmlevel_21d_jerk_v002_signal(netmargin):
    base = netmargin.rolling(126, min_periods=42).mean()
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of emlevel (63d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_emlevel_21d_jerk_v003_signal(ebitdamargin):
    base = ebitdamargin.rolling(63, min_periods=21).mean()
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of omlevel (63d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_omlevel_21d_jerk_v004_signal(opinc, revenue):
    om = (opinc / revenue.replace(0, np.nan))
    base = om.rolling(63, min_periods=21).mean()
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gpmlevel (126d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gpmlevel_21d_jerk_v005_signal(gp, revenue):
    gm = (gp / revenue.replace(0, np.nan))
    base = gm.rolling(126, min_periods=42).mean()
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmlevelz (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmlevelz_63d_jerk_v006_signal(grossmargin):
    m = grossmargin.rolling(252, min_periods=84).mean()
    sd = grossmargin.rolling(252, min_periods=84).std()
    base = (grossmargin - m) / sd.replace(0, np.nan)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmlevelz (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmlevelz_63d_jerk_v007_signal(netmargin):
    m = netmargin.rolling(252, min_periods=84).mean()
    sd = netmargin.rolling(252, min_periods=84).std()
    base = (netmargin - m) / sd.replace(0, np.nan)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of emlevelz (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_emlevelz_63d_jerk_v008_signal(ebitdamargin):
    m = ebitdamargin.rolling(252, min_periods=84).mean()
    sd = ebitdamargin.rolling(252, min_periods=84).std()
    base = (ebitdamargin - m) / sd.replace(0, np.nan)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmmidgap (504d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmmidgap_63d_jerk_v009_signal(grossmargin):
    base = grossmargin - grossmargin.rolling(504, min_periods=168).mean()
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmmidgap (504d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmmidgap_63d_jerk_v010_signal(netmargin):
    base = netmargin - netmargin.rolling(504, min_periods=168).mean()
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmvol (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmvol_63d_jerk_v011_signal(grossmargin):
    base = grossmargin.rolling(252, min_periods=84).std()
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmvol (126d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmvol_21d_jerk_v012_signal(netmargin):
    base = netmargin.rolling(126, min_periods=42).std()
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of emvol (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_emvol_63d_jerk_v013_signal(ebitdamargin):
    base = ebitdamargin.rolling(252, min_periods=84).std()
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of omvol (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_omvol_63d_jerk_v014_signal(opinc, revenue):
    om = (opinc / revenue.replace(0, np.nan))
    base = om.rolling(252, min_periods=84).std()
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmvol (63d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmvol_21d_jerk_v015_signal(grossmargin):
    base = grossmargin.rolling(63, min_periods=21).std()
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmsemidev (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmsemidev_63d_jerk_v016_signal(netmargin):
    mu = netmargin.rolling(252, min_periods=84).mean()
    dev = (netmargin - mu).clip(upper=0.0)
    base = (dev * dev).rolling(252, min_periods=84).mean() ** 0.5
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmvolterm (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmvolterm_63d_jerk_v017_signal(grossmargin):
    vs = grossmargin.rolling(63, min_periods=21).std()
    vl = grossmargin.rolling(252, min_periods=84).std()
    base = vs / vl.replace(0, np.nan)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmvov (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmvov_63d_jerk_v018_signal(grossmargin):
    v = grossmargin.rolling(63, min_periods=21).std()
    base = v.rolling(252, min_periods=84).std()
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmmad (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmmad_63d_jerk_v019_signal(netmargin):
    mu = netmargin.rolling(252, min_periods=84).mean()
    base = (netmargin - mu).abs().rolling(252, min_periods=84).mean()
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of emvolterm (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_emvolterm_63d_jerk_v020_signal(ebitdamargin):
    vs = ebitdamargin.rolling(63, min_periods=21).std()
    vl = ebitdamargin.rolling(252, min_periods=84).std()
    base = vs / vl.replace(0, np.nan)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmamp (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmamp_63d_jerk_v021_signal(grossmargin):
    base = _amplitude(grossmargin, 252)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmamp (504d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmamp_63d_jerk_v022_signal(netmargin):
    base = _amplitude(netmargin, 504)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of emamp (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_emamp_63d_jerk_v023_signal(ebitdamargin):
    base = _amplitude(ebitdamargin, 252)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of omamp (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_omamp_63d_jerk_v024_signal(opinc, revenue):
    om = (opinc / revenue.replace(0, np.nan))
    base = _amplitude(om, 252)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmamprel (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmamprel_63d_jerk_v025_signal(grossmargin):
    amp = _amplitude(grossmargin, 252)
    sd = grossmargin.rolling(63, min_periods=21).std()
    base = amp / sd.replace(0, np.nan)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmampexp (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmampexp_63d_jerk_v026_signal(netmargin):
    amp = _amplitude(netmargin, 252)
    base = amp - amp.shift(126)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmampratio (504d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmampratio_63d_jerk_v027_signal(grossmargin):
    short = _amplitude(grossmargin, 126)
    long = _amplitude(grossmargin, 504)
    base = short / long.replace(0, np.nan)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmenergy (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmenergy_63d_jerk_v028_signal(grossmargin):
    d = grossmargin.diff()
    base = (d * d).rolling(252, min_periods=84).sum()
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmampskew (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmampskew_63d_jerk_v029_signal(netmargin):
    hi = _rmax(netmargin, 252)
    lo = _rmin(netmargin, 252)
    med = netmargin.rolling(252, min_periods=84).median()
    base = (hi - med) - (med - lo)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmrangecrush (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmrangecrush_63d_jerk_v030_signal(grossmargin):
    short = _amplitude(grossmargin, 63)
    long = _amplitude(grossmargin, 252)
    base = short / long.replace(0, np.nan)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gnspread (63d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gnspread_21d_jerk_v031_signal(grossmargin, netmargin):
    sp = grossmargin - netmargin
    base = sp.rolling(63, min_periods=21).mean()
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gnspreadz (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gnspreadz_63d_jerk_v032_signal(grossmargin, netmargin):
    sp = grossmargin - netmargin
    m = sp.rolling(252, min_periods=84).mean()
    sd = sp.rolling(252, min_periods=84).std()
    base = (sp - m) / sd.replace(0, np.nan)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gespread (63d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gespread_21d_jerk_v033_signal(grossmargin, ebitdamargin):
    sp = grossmargin - ebitdamargin
    base = sp.rolling(63, min_periods=21).mean()
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of enspread (63d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_enspread_21d_jerk_v034_signal(ebitdamargin, netmargin):
    sp = ebitdamargin - netmargin
    base = sp.rolling(63, min_periods=21).mean()
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gnspreadfrac (63d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gnspreadfrac_21d_jerk_v035_signal(grossmargin, netmargin):
    sp = grossmargin - netmargin
    frac = sp / grossmargin.abs().replace(0, np.nan)
    base = frac.rolling(63, min_periods=21).mean()
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gnspreadvol (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gnspreadvol_63d_jerk_v036_signal(grossmargin, netmargin):
    sp = grossmargin - netmargin
    base = sp.rolling(252, min_periods=84).std()
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of onspread (63d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_onspread_21d_jerk_v037_signal(opinc, revenue, netmargin):
    om = (opinc / revenue.replace(0, np.nan))
    sp = om - netmargin
    base = sp.rolling(63, min_periods=21).mean()
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gnspreadamp (504d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gnspreadamp_63d_jerk_v038_signal(grossmargin, netmargin):
    sp = grossmargin - netmargin
    base = _amplitude(sp, 504)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of enspreadvol (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_enspreadvol_63d_jerk_v039_signal(ebitdamargin, netmargin):
    sp = ebitdamargin - netmargin
    base = sp.rolling(252, min_periods=84).std()
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gnspreadpos (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gnspreadpos_63d_jerk_v040_signal(grossmargin, netmargin):
    sp = grossmargin - netmargin
    base = _range_pos(sp, 252)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmtrend (126d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmtrend_21d_jerk_v041_signal(grossmargin):
    base = _slope(grossmargin, 126)
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmtrend (63d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmtrend_21d_jerk_v042_signal(netmargin):
    base = _slope(netmargin, 63)
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of emtrend (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_emtrend_63d_jerk_v043_signal(ebitdamargin):
    base = _slope(ebitdamargin, 252)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of omtrend (126d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_omtrend_21d_jerk_v044_signal(opinc, revenue):
    om = (opinc / revenue.replace(0, np.nan))
    base = _slope(om, 126)
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmmacross (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmmacross_63d_jerk_v045_signal(grossmargin):
    fast = grossmargin.rolling(63, min_periods=21).mean()
    slow = grossmargin.rolling(252, min_periods=84).mean()
    base = fast - slow
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmmacross (168d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmmacross_21d_jerk_v046_signal(netmargin):
    fast = netmargin.rolling(42, min_periods=14).mean()
    slow = netmargin.rolling(168, min_periods=56).mean()
    base = fast - slow
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmtrendstr (126d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmtrendstr_21d_jerk_v047_signal(grossmargin):
    sl = _slope(grossmargin, 126)
    vol = grossmargin.rolling(126, min_periods=42).std()
    base = sl / vol.replace(0, np.nan)
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmyoy (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmyoy_63d_jerk_v048_signal(netmargin):
    base = netmargin - netmargin.shift(252)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmemadisp (126d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmemadisp_21d_jerk_v049_signal(grossmargin):
    base = grossmargin - grossmargin.ewm(span=126, min_periods=42).mean()
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmhytanh (126d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmhytanh_21d_jerk_v050_signal(grossmargin):
    chg = grossmargin - grossmargin.shift(126)
    base = np.tanh(10.0 * chg)
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmtrough (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmtrough_63d_jerk_v051_signal(grossmargin):
    base = grossmargin - _rmin(grossmargin, 252)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmpeak (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmpeak_63d_jerk_v052_signal(netmargin):
    base = _rmax(netmargin, 252) - netmargin
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmrangepos (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmrangepos_63d_jerk_v053_signal(grossmargin):
    base = _range_pos(grossmargin, 252)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmrangepos (126d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmrangepos_21d_jerk_v054_signal(netmargin):
    base = _range_pos(netmargin, 126)
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of emrangepos (504d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_emrangepos_63d_jerk_v055_signal(ebitdamargin):
    base = _range_pos(ebitdamargin, 504)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmtroughrelH (504d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmtroughrelH_63d_jerk_v056_signal(grossmargin):
    tr = grossmargin - _rmin(grossmargin, 504)
    sd = grossmargin.rolling(126, min_periods=42).std()
    base = tr / sd.replace(0, np.nan)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmpeakrel (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmpeakrel_63d_jerk_v057_signal(netmargin):
    pk = _rmax(netmargin, 504) - netmargin
    sd = netmargin.rolling(63, min_periods=21).std()
    base = pk / sd.replace(0, np.nan)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmpeakrel (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmpeakrel_63d_jerk_v058_signal(grossmargin):
    pk = _rmax(grossmargin, 252) - grossmargin
    sd = grossmargin.rolling(63, min_periods=21).std()
    base = pk / sd.replace(0, np.nan)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmmidskew (504d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmmidskew_63d_jerk_v059_signal(grossmargin):
    hi = _rmax(grossmargin, 504)
    lo = _rmin(grossmargin, 504)
    mid = (hi + lo) / 2.0
    base = (grossmargin - mid) / (hi - lo).replace(0, np.nan)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmvshape (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmvshape_63d_jerk_v060_signal(netmargin):
    rec = netmargin - _rmin(netmargin, 252)
    comp = _rmax(netmargin, 252) - netmargin
    base = (rec - comp) / (rec + comp).replace(0, np.nan)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmuppertime (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmuppertime_63d_jerk_v061_signal(grossmargin):
    pos = _range_pos(grossmargin, 252)
    upper = (pos >= 0.6667).astype(float)
    base = upper.rolling(252, min_periods=84).mean()
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmtroughtouch (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmtroughtouch_63d_jerk_v062_signal(netmargin):
    lo = _rmin(netmargin, 126)
    hi = _rmax(netmargin, 126)
    near = (hi - netmargin) / (hi - lo).replace(0, np.nan)
    base = near.rolling(252, min_periods=84).mean()
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmregimebal (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmregimebal_63d_jerk_v063_signal(grossmargin):
    mu = grossmargin.rolling(252, min_periods=84).mean()
    dev = grossmargin - mu
    up = dev.clip(lower=0.0).rolling(252, min_periods=84).sum()
    dn = (-dev).clip(lower=0.0).rolling(252, min_periods=84).sum()
    base = (up - dn) / (up + dn).replace(0, np.nan)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmskew (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmskew_63d_jerk_v064_signal(netmargin):
    base = netmargin.rolling(252, min_periods=84).skew()
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmkurt (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmkurt_63d_jerk_v065_signal(grossmargin):
    base = grossmargin.rolling(252, min_periods=84).kurt()
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmdd (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmdd_63d_jerk_v066_signal(grossmargin):
    pk = _rmax(grossmargin, 252)
    amp = _amplitude(grossmargin, 252)
    uw = (pk - grossmargin) / amp.replace(0, np.nan)
    deep = (uw >= 0.20).astype(float)
    base = deep.rolling(252, min_periods=84).mean()
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gncorr (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gncorr_63d_jerk_v067_signal(grossmargin, netmargin):
    base = grossmargin.rolling(252, min_periods=84).corr(netmargin)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmbeta (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmbeta_63d_jerk_v068_signal(grossmargin, netmargin):
    cov = grossmargin.rolling(252, min_periods=84).cov(netmargin)
    var = grossmargin.rolling(252, min_periods=84).var()
    base = cov / var.replace(0, np.nan)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of margindisp (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_margindisp_63d_jerk_v069_signal(grossmargin, netmargin, ebitdamargin):
    stacked = pd.concat([grossmargin, netmargin, ebitdamargin], axis=1)
    base = stacked.std(axis=1)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of phasespread (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_phasespread_63d_jerk_v070_signal(grossmargin, netmargin):
    base = _range_pos(netmargin, 252) - _range_pos(grossmargin, 252)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gpstab (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gpstab_63d_jerk_v071_signal(gp, revenue):
    gm = (gp / revenue.replace(0, np.nan))
    mu = gm.rolling(252, min_periods=84).mean()
    sd = gm.rolling(252, min_periods=84).std()
    base = mu / sd.replace(0, np.nan)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmswingeff (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmswingeff_63d_jerk_v072_signal(grossmargin):
    net = (grossmargin - grossmargin.shift(252)).abs()
    path = grossmargin.diff().abs().rolling(252, min_periods=84).sum()
    base = net / path.replace(0, np.nan)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmcov (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmcov_63d_jerk_v073_signal(netmargin):
    sd = netmargin.rolling(252, min_periods=84).std()
    mu = netmargin.rolling(252, min_periods=84).mean()
    base = sd / mu.abs().replace(0, np.nan)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gecorr (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gecorr_63d_jerk_v074_signal(grossmargin, ebitdamargin):
    base = grossmargin.rolling(252, min_periods=84).corr(ebitdamargin)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of swingreten (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_swingreten_63d_jerk_v075_signal(grossmargin, netmargin):
    ga = _amplitude(grossmargin, 252)
    na = _amplitude(netmargin, 252)
    base = na / ga.replace(0, np.nan)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmlevel (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmlevel_63d_jerk_v076_signal(grossmargin):
    base = grossmargin.rolling(252, min_periods=84).mean()
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmlevel (63d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmlevel_21d_jerk_v077_signal(netmargin):
    base = netmargin.rolling(63, min_periods=21).mean()
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of emlevel (126d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_emlevel_21d_jerk_v078_signal(ebitdamargin):
    base = ebitdamargin.rolling(126, min_periods=42).mean()
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of emlevelz (504d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_emlevelz_63d_jerk_v079_signal(ebitdamargin):
    m = ebitdamargin.rolling(504, min_periods=168).mean()
    sd = ebitdamargin.rolling(504, min_periods=168).std()
    base = (ebitdamargin - m) / sd.replace(0, np.nan)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmrank (504d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmrank_63d_jerk_v080_signal(netmargin):
    base = _rank(netmargin, 504)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of omlevelz (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_omlevelz_63d_jerk_v081_signal(opinc, revenue):
    om = (opinc / revenue.replace(0, np.nan))
    m = om.rolling(252, min_periods=84).mean()
    sd = om.rolling(252, min_periods=84).std()
    base = (om - m) / sd.replace(0, np.nan)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmmidz (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmmidz_63d_jerk_v082_signal(grossmargin):
    b2 = grossmargin.rolling(252, min_periods=84).mean()
    sd = grossmargin.rolling(126, min_periods=42).std()
    base = (grossmargin - b2) / sd.replace(0, np.nan)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of emvfill (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_emvfill_63d_jerk_v083_signal(ebitdamargin):
    sd = ebitdamargin.rolling(252, min_periods=84).std()
    amp = _amplitude(ebitdamargin, 252)
    base = sd / amp.replace(0, np.nan)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmrangepM (126d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmrangepM_21d_jerk_v084_signal(grossmargin):
    base = _range_pos(grossmargin, 126)
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gpmlevel (63d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gpmlevel_21d_jerk_v085_signal(gp, revenue):
    gm = (gp / revenue.replace(0, np.nan))
    base = gm.rolling(63, min_periods=21).mean()
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmvol (504d base, 126d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmvol_126d_jerk_v086_signal(grossmargin):
    base = grossmargin.rolling(504, min_periods=168).std()
    b = _accel(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmvol (504d base, 126d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmvol_126d_jerk_v087_signal(netmargin):
    base = netmargin.rolling(504, min_periods=168).std()
    b = _accel(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of emvol (126d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_emvol_21d_jerk_v088_signal(ebitdamargin):
    base = ebitdamargin.rolling(126, min_periods=42).std()
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmsemiratio (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmsemiratio_63d_jerk_v089_signal(netmargin):
    mu = netmargin.rolling(252, min_periods=84).mean()
    dn = (netmargin - mu).clip(upper=0.0)
    up = (netmargin - mu).clip(lower=0.0)
    dv = (dn * dn).rolling(252, min_periods=84).mean() ** 0.5
    uv = (up * up).rolling(252, min_periods=84).mean() ** 0.5
    base = dv / uv.replace(0, np.nan)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmupsemidev (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmupsemidev_63d_jerk_v090_signal(grossmargin):
    mu = grossmargin.rolling(252, min_periods=84).mean()
    dev = (grossmargin - mu).clip(lower=0.0)
    base = (dev * dev).rolling(252, min_periods=84).mean() ** 0.5
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmvolchg (63d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmvolchg_21d_jerk_v091_signal(grossmargin):
    v = grossmargin.rolling(63, min_periods=21).std()
    base = v - v.shift(63)
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmvolz (504d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmvolz_63d_jerk_v092_signal(grossmargin):
    v = grossmargin.rolling(126, min_periods=42).std()
    m = v.rolling(504, min_periods=168).mean()
    sd = v.rolling(504, min_periods=168).std()
    base = (v - m) / sd.replace(0, np.nan)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of emstab (504d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_emstab_63d_jerk_v093_signal(ebitdamargin):
    mu = ebitdamargin.rolling(504, min_periods=168).mean()
    sd = ebitdamargin.rolling(504, min_periods=168).std()
    base = mu / sd.replace(0, np.nan)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmvolterm (504d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmvolterm_63d_jerk_v094_signal(netmargin):
    vs = netmargin.rolling(63, min_periods=21).std()
    vl = netmargin.rolling(504, min_periods=168).std()
    base = vs / vl.replace(0, np.nan)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmvov (504d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmvov_63d_jerk_v095_signal(grossmargin):
    v = grossmargin.rolling(126, min_periods=42).std()
    base = v.rolling(504, min_periods=168).std()
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmamp (504d base, 126d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmamp_126d_jerk_v096_signal(grossmargin):
    base = _amplitude(grossmargin, 504)
    b = _accel(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmamp (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmamp_63d_jerk_v097_signal(netmargin):
    base = _amplitude(netmargin, 252)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of emamp (504d base, 126d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_emamp_126d_jerk_v098_signal(ebitdamargin):
    base = _amplitude(ebitdamargin, 504)
    b = _accel(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmampexp (504d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmampexp_63d_jerk_v099_signal(grossmargin):
    amp = _amplitude(grossmargin, 252)
    base = amp - amp.shift(252)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmamprel (504d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmamprel_63d_jerk_v100_signal(netmargin):
    amp = _amplitude(netmargin, 504)
    sd = netmargin.rolling(126, min_periods=42).std()
    base = amp / sd.replace(0, np.nan)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of omenergy (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_omenergy_63d_jerk_v101_signal(opinc, revenue):
    om = (opinc / revenue.replace(0, np.nan))
    d = om.diff()
    base = (d * d).rolling(252, min_periods=84).sum()
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmpathlen (504d base, 126d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmpathlen_126d_jerk_v102_signal(netmargin):
    base = netmargin.diff().abs().rolling(504, min_periods=168).sum()
    b = _accel(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmampskew (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmampskew_63d_jerk_v103_signal(grossmargin):
    hi = _rmax(grossmargin, 252)
    lo = _rmin(grossmargin, 252)
    med = grossmargin.rolling(252, min_periods=84).median()
    base = (hi - med) - (med - lo)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmrangecrush (504d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmrangecrush_63d_jerk_v104_signal(netmargin):
    short = _amplitude(netmargin, 126)
    long = _amplitude(netmargin, 504)
    base = short / long.replace(0, np.nan)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gnspreadamp (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gnspreadamp_63d_jerk_v105_signal(grossmargin, netmargin):
    sp = grossmargin - netmargin
    base = _amplitude(sp, 252)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of omconvex (126d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_omconvex_21d_jerk_v106_signal(opinc, revenue):
    om = (opinc / revenue.replace(0, np.nan))
    d2 = om.diff().diff()
    base = d2.rolling(126, min_periods=42).mean()
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gnspreadtrend (126d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gnspreadtrend_21d_jerk_v107_signal(grossmargin, netmargin):
    sp = grossmargin - netmargin
    base = _slope(sp, 126)
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gespreadz (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gespreadz_63d_jerk_v108_signal(grossmargin, ebitdamargin):
    sp = grossmargin - ebitdamargin
    m = sp.rolling(252, min_periods=84).mean()
    sd = sp.rolling(252, min_periods=84).std()
    base = (sp - m) / sd.replace(0, np.nan)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gnspreadcompress (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gnspreadcompress_63d_jerk_v109_signal(grossmargin, netmargin):
    sp = grossmargin - netmargin
    bb = sp.rolling(252, min_periods=84).mean()
    base = sp / bb.replace(0, np.nan) - 1.0
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of passthru (63d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_passthru_21d_jerk_v110_signal(grossmargin, netmargin):
    dn = netmargin - netmargin.shift(63)
    dg = grossmargin - grossmargin.shift(63)
    base = (dn / dg.replace(0, np.nan)).clip(-5.0, 5.0)
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gnspreadmac (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gnspreadmac_63d_jerk_v111_signal(grossmargin, netmargin):
    sp = grossmargin - netmargin
    fast = sp.rolling(63, min_periods=21).mean()
    slow = sp.rolling(252, min_periods=84).mean()
    base = fast - slow
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of enspreadpos (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_enspreadpos_63d_jerk_v112_signal(ebitdamargin, netmargin):
    sp = ebitdamargin - netmargin
    base = _range_pos(sp, 252)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gospreadvol (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gospreadvol_63d_jerk_v113_signal(grossmargin, opinc, revenue):
    om = (opinc / revenue.replace(0, np.nan))
    sp = grossmargin - om
    base = sp.rolling(252, min_periods=84).std()
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of onspread (126d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_onspread_21d_jerk_v114_signal(opinc, revenue, netmargin):
    om = (opinc / revenue.replace(0, np.nan))
    sp = om - netmargin
    base = sp.rolling(126, min_periods=42).mean()
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gespreadtr (126d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gespreadtr_21d_jerk_v115_signal(grossmargin, ebitdamargin):
    sp = grossmargin - ebitdamargin
    base = _slope(sp, 126)
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmtrend (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmtrend_63d_jerk_v116_signal(grossmargin):
    base = _slope(grossmargin, 252)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmtrend (126d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmtrend_21d_jerk_v117_signal(netmargin):
    base = _slope(netmargin, 126)
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of emtrend (126d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_emtrend_21d_jerk_v118_signal(ebitdamargin):
    base = _slope(ebitdamargin, 126)
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmmacrosslong (504d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmmacrosslong_63d_jerk_v119_signal(grossmargin):
    fast = grossmargin.rolling(126, min_periods=42).mean()
    slow = grossmargin.rolling(504, min_periods=168).mean()
    base = fast - slow
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmtrendstr (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmtrendstr_63d_jerk_v120_signal(netmargin):
    sl = _slope(netmargin, 252)
    vol = netmargin.rolling(252, min_periods=84).std()
    base = sl / vol.replace(0, np.nan)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmeff (126d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmeff_21d_jerk_v121_signal(grossmargin):
    net = (grossmargin - grossmargin.shift(126)).abs()
    path = grossmargin.diff().abs().rolling(126, min_periods=42).sum()
    base = net / path.replace(0, np.nan)
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of emtrendaccel (126d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_emtrendaccel_21d_jerk_v122_signal(ebitdamargin):
    sl = _slope(ebitdamargin, 63)
    base = sl - sl.shift(63)
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmtrendstrH (126d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmtrendstrH_21d_jerk_v123_signal(netmargin):
    sl = _slope(netmargin, 126)
    vol = netmargin.rolling(126, min_periods=42).std()
    base = sl / vol.replace(0, np.nan)
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmtrendaccel (126d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmtrendaccel_21d_jerk_v124_signal(grossmargin):
    sl = _slope(grossmargin, 63)
    base = sl - sl.shift(63)
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmtrendpersist (63d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmtrendpersist_21d_jerk_v125_signal(netmargin):
    up = (netmargin.diff() > 0).astype(float)
    base = up.rolling(63, min_periods=21).mean() - 0.5
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmpeakd (504d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmpeakd_63d_jerk_v126_signal(grossmargin):
    base = _rmax(grossmargin, 504) - grossmargin
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmpeak (504d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmpeak_63d_jerk_v127_signal(netmargin):
    base = _rmax(netmargin, 504) - netmargin
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmpeakrelL (504d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmpeakrelL_63d_jerk_v128_signal(grossmargin):
    pk = _rmax(grossmargin, 504) - grossmargin
    sd = grossmargin.rolling(126, min_periods=42).std()
    base = pk / sd.replace(0, np.nan)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmrangepos (504d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmrangepos_63d_jerk_v129_signal(netmargin):
    base = _range_pos(netmargin, 504)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of emrangepos (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_emrangepos_63d_jerk_v130_signal(ebitdamargin):
    base = _range_pos(ebitdamargin, 252)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmrunup (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmrunup_63d_jerk_v131_signal(grossmargin):
    ru = grossmargin - _rmin(grossmargin, 252)
    base = ru - ru.shift(63)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmtroughtouch (504d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmtroughtouch_63d_jerk_v132_signal(netmargin):
    lo = _rmin(netmargin, 252)
    hi = _rmax(netmargin, 252)
    near = (hi - netmargin) / (hi - lo).replace(0, np.nan)
    base = near.rolling(504, min_periods=168).mean()
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmpeak (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmpeak_63d_jerk_v133_signal(grossmargin):
    base = _rmax(grossmargin, 252) - grossmargin
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmconvex (126d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmconvex_21d_jerk_v134_signal(netmargin):
    d2 = netmargin.diff().diff()
    base = d2.rolling(126, min_periods=42).mean()
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmuppertimeL (504d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmuppertimeL_63d_jerk_v135_signal(grossmargin):
    pos = _range_pos(grossmargin, 252)
    upper = (pos >= 0.6667).astype(float)
    base = upper.rolling(504, min_periods=168).mean()
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmexpandfreq (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmexpandfreq_63d_jerk_v136_signal(grossmargin):
    sm = grossmargin.rolling(21, min_periods=7).mean()
    up = (sm.diff() > 0).astype(float)
    base = up.rolling(252, min_periods=84).mean() - 0.5
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmregimebalL (504d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmregimebalL_63d_jerk_v137_signal(grossmargin):
    mu = grossmargin.rolling(504, min_periods=168).mean()
    dev = grossmargin - mu
    up = dev.clip(lower=0.0).rolling(504, min_periods=168).sum()
    dn = (-dev).clip(lower=0.0).rolling(504, min_periods=168).sum()
    base = (up - dn) / (up + dn).replace(0, np.nan)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmskewL (504d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmskewL_63d_jerk_v138_signal(netmargin):
    base = netmargin.rolling(504, min_periods=168).skew()
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmkurtL (504d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmkurtL_63d_jerk_v139_signal(grossmargin):
    base = grossmargin.rolling(504, min_periods=168).kurt()
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gmconvex (126d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gmconvex_21d_jerk_v140_signal(grossmargin):
    d2 = grossmargin.diff().diff()
    base = d2.rolling(126, min_periods=42).mean()
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of emconvex (126d base, 21d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_emconvex_21d_jerk_v141_signal(ebitdamargin):
    d2 = ebitdamargin.diff().diff()
    base = d2.rolling(126, min_periods=42).mean()
    b = _accel(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gncorrL (504d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gncorrL_63d_jerk_v142_signal(grossmargin, netmargin):
    base = grossmargin.rolling(504, min_periods=168).corr(netmargin)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nebeta (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nebeta_63d_jerk_v143_signal(ebitdamargin, netmargin):
    cov = ebitdamargin.rolling(252, min_periods=84).cov(netmargin)
    var = ebitdamargin.rolling(252, min_periods=84).var()
    base = cov / var.replace(0, np.nan)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of margindisp4 (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_margindisp4_63d_jerk_v144_signal(grossmargin, netmargin, ebitdamargin, opinc, revenue):
    om = (opinc / revenue.replace(0, np.nan))
    stacked = pd.concat([grossmargin, netmargin, ebitdamargin, om], axis=1)
    base = stacked.std(axis=1)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of phaselag (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_phaselag_63d_jerk_v145_signal(grossmargin, netmargin):
    gpp = _range_pos(grossmargin, 252)
    npp = _range_pos(netmargin, 252)
    base = (gpp - gpp.shift(63)) - (npp - npp.shift(63))
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmswingeff (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmswingeff_63d_jerk_v146_signal(netmargin):
    net = (netmargin - netmargin.shift(252)).abs()
    path = netmargin.diff().abs().rolling(252, min_periods=84).sum()
    base = net / path.replace(0, np.nan)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmrebound (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmrebound_63d_jerk_v147_signal(netmargin):
    ru = netmargin - _rmin(netmargin, 252)
    base = ru - ru.shift(63)
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmlowband (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmlowband_63d_jerk_v148_signal(netmargin):
    lo = _rmin(netmargin, 252)
    amp = _amplitude(netmargin, 252)
    near = ((netmargin - lo) / amp.replace(0, np.nan) <= 0.20).astype(float)
    base = near.rolling(252, min_periods=84).mean()
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of gpmskew (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_gpmskew_63d_jerk_v149_signal(gp, revenue):
    gm = (gp / revenue.replace(0, np.nan))
    base = gm.rolling(252, min_periods=84).skew()
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of nmworstdip (252d base, 63d) -> margin-cyclicality jerk
def f25mc_f25_margin_cyclicality_nmworstdip_63d_jerk_v150_signal(grossmargin):
    med = grossmargin.rolling(126, min_periods=42).median()
    dip = (med - grossmargin).clip(lower=0.0) / med.abs().replace(0, np.nan)
    base = dip.rolling(252, min_periods=84).max()
    b = _accel(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f25mc_f25_margin_cyclicality_gmlevel_21d_jerk_v001_signal,
    f25mc_f25_margin_cyclicality_nmlevel_21d_jerk_v002_signal,
    f25mc_f25_margin_cyclicality_emlevel_21d_jerk_v003_signal,
    f25mc_f25_margin_cyclicality_omlevel_21d_jerk_v004_signal,
    f25mc_f25_margin_cyclicality_gpmlevel_21d_jerk_v005_signal,
    f25mc_f25_margin_cyclicality_gmlevelz_63d_jerk_v006_signal,
    f25mc_f25_margin_cyclicality_nmlevelz_63d_jerk_v007_signal,
    f25mc_f25_margin_cyclicality_emlevelz_63d_jerk_v008_signal,
    f25mc_f25_margin_cyclicality_gmmidgap_63d_jerk_v009_signal,
    f25mc_f25_margin_cyclicality_nmmidgap_63d_jerk_v010_signal,
    f25mc_f25_margin_cyclicality_gmvol_63d_jerk_v011_signal,
    f25mc_f25_margin_cyclicality_nmvol_21d_jerk_v012_signal,
    f25mc_f25_margin_cyclicality_emvol_63d_jerk_v013_signal,
    f25mc_f25_margin_cyclicality_omvol_63d_jerk_v014_signal,
    f25mc_f25_margin_cyclicality_gmvol_21d_jerk_v015_signal,
    f25mc_f25_margin_cyclicality_nmsemidev_63d_jerk_v016_signal,
    f25mc_f25_margin_cyclicality_gmvolterm_63d_jerk_v017_signal,
    f25mc_f25_margin_cyclicality_gmvov_63d_jerk_v018_signal,
    f25mc_f25_margin_cyclicality_nmmad_63d_jerk_v019_signal,
    f25mc_f25_margin_cyclicality_emvolterm_63d_jerk_v020_signal,
    f25mc_f25_margin_cyclicality_gmamp_63d_jerk_v021_signal,
    f25mc_f25_margin_cyclicality_nmamp_63d_jerk_v022_signal,
    f25mc_f25_margin_cyclicality_emamp_63d_jerk_v023_signal,
    f25mc_f25_margin_cyclicality_omamp_63d_jerk_v024_signal,
    f25mc_f25_margin_cyclicality_gmamprel_63d_jerk_v025_signal,
    f25mc_f25_margin_cyclicality_nmampexp_63d_jerk_v026_signal,
    f25mc_f25_margin_cyclicality_gmampratio_63d_jerk_v027_signal,
    f25mc_f25_margin_cyclicality_gmenergy_63d_jerk_v028_signal,
    f25mc_f25_margin_cyclicality_nmampskew_63d_jerk_v029_signal,
    f25mc_f25_margin_cyclicality_gmrangecrush_63d_jerk_v030_signal,
    f25mc_f25_margin_cyclicality_gnspread_21d_jerk_v031_signal,
    f25mc_f25_margin_cyclicality_gnspreadz_63d_jerk_v032_signal,
    f25mc_f25_margin_cyclicality_gespread_21d_jerk_v033_signal,
    f25mc_f25_margin_cyclicality_enspread_21d_jerk_v034_signal,
    f25mc_f25_margin_cyclicality_gnspreadfrac_21d_jerk_v035_signal,
    f25mc_f25_margin_cyclicality_gnspreadvol_63d_jerk_v036_signal,
    f25mc_f25_margin_cyclicality_onspread_21d_jerk_v037_signal,
    f25mc_f25_margin_cyclicality_gnspreadamp_63d_jerk_v038_signal,
    f25mc_f25_margin_cyclicality_enspreadvol_63d_jerk_v039_signal,
    f25mc_f25_margin_cyclicality_gnspreadpos_63d_jerk_v040_signal,
    f25mc_f25_margin_cyclicality_gmtrend_21d_jerk_v041_signal,
    f25mc_f25_margin_cyclicality_nmtrend_21d_jerk_v042_signal,
    f25mc_f25_margin_cyclicality_emtrend_63d_jerk_v043_signal,
    f25mc_f25_margin_cyclicality_omtrend_21d_jerk_v044_signal,
    f25mc_f25_margin_cyclicality_gmmacross_63d_jerk_v045_signal,
    f25mc_f25_margin_cyclicality_nmmacross_21d_jerk_v046_signal,
    f25mc_f25_margin_cyclicality_gmtrendstr_21d_jerk_v047_signal,
    f25mc_f25_margin_cyclicality_nmyoy_63d_jerk_v048_signal,
    f25mc_f25_margin_cyclicality_gmemadisp_21d_jerk_v049_signal,
    f25mc_f25_margin_cyclicality_gmhytanh_21d_jerk_v050_signal,
    f25mc_f25_margin_cyclicality_gmtrough_63d_jerk_v051_signal,
    f25mc_f25_margin_cyclicality_nmpeak_63d_jerk_v052_signal,
    f25mc_f25_margin_cyclicality_gmrangepos_63d_jerk_v053_signal,
    f25mc_f25_margin_cyclicality_nmrangepos_21d_jerk_v054_signal,
    f25mc_f25_margin_cyclicality_emrangepos_63d_jerk_v055_signal,
    f25mc_f25_margin_cyclicality_gmtroughrelH_63d_jerk_v056_signal,
    f25mc_f25_margin_cyclicality_nmpeakrel_63d_jerk_v057_signal,
    f25mc_f25_margin_cyclicality_gmpeakrel_63d_jerk_v058_signal,
    f25mc_f25_margin_cyclicality_gmmidskew_63d_jerk_v059_signal,
    f25mc_f25_margin_cyclicality_nmvshape_63d_jerk_v060_signal,
    f25mc_f25_margin_cyclicality_gmuppertime_63d_jerk_v061_signal,
    f25mc_f25_margin_cyclicality_nmtroughtouch_63d_jerk_v062_signal,
    f25mc_f25_margin_cyclicality_gmregimebal_63d_jerk_v063_signal,
    f25mc_f25_margin_cyclicality_nmskew_63d_jerk_v064_signal,
    f25mc_f25_margin_cyclicality_gmkurt_63d_jerk_v065_signal,
    f25mc_f25_margin_cyclicality_gmdd_63d_jerk_v066_signal,
    f25mc_f25_margin_cyclicality_gncorr_63d_jerk_v067_signal,
    f25mc_f25_margin_cyclicality_nmbeta_63d_jerk_v068_signal,
    f25mc_f25_margin_cyclicality_margindisp_63d_jerk_v069_signal,
    f25mc_f25_margin_cyclicality_phasespread_63d_jerk_v070_signal,
    f25mc_f25_margin_cyclicality_gpstab_63d_jerk_v071_signal,
    f25mc_f25_margin_cyclicality_gmswingeff_63d_jerk_v072_signal,
    f25mc_f25_margin_cyclicality_nmcov_63d_jerk_v073_signal,
    f25mc_f25_margin_cyclicality_gecorr_63d_jerk_v074_signal,
    f25mc_f25_margin_cyclicality_swingreten_63d_jerk_v075_signal,
    f25mc_f25_margin_cyclicality_gmlevel_63d_jerk_v076_signal,
    f25mc_f25_margin_cyclicality_nmlevel_21d_jerk_v077_signal,
    f25mc_f25_margin_cyclicality_emlevel_21d_jerk_v078_signal,
    f25mc_f25_margin_cyclicality_emlevelz_63d_jerk_v079_signal,
    f25mc_f25_margin_cyclicality_nmrank_63d_jerk_v080_signal,
    f25mc_f25_margin_cyclicality_omlevelz_63d_jerk_v081_signal,
    f25mc_f25_margin_cyclicality_gmmidz_63d_jerk_v082_signal,
    f25mc_f25_margin_cyclicality_emvfill_63d_jerk_v083_signal,
    f25mc_f25_margin_cyclicality_gmrangepM_21d_jerk_v084_signal,
    f25mc_f25_margin_cyclicality_gpmlevel_21d_jerk_v085_signal,
    f25mc_f25_margin_cyclicality_gmvol_126d_jerk_v086_signal,
    f25mc_f25_margin_cyclicality_nmvol_126d_jerk_v087_signal,
    f25mc_f25_margin_cyclicality_emvol_21d_jerk_v088_signal,
    f25mc_f25_margin_cyclicality_nmsemiratio_63d_jerk_v089_signal,
    f25mc_f25_margin_cyclicality_gmupsemidev_63d_jerk_v090_signal,
    f25mc_f25_margin_cyclicality_gmvolchg_21d_jerk_v091_signal,
    f25mc_f25_margin_cyclicality_gmvolz_63d_jerk_v092_signal,
    f25mc_f25_margin_cyclicality_emstab_63d_jerk_v093_signal,
    f25mc_f25_margin_cyclicality_nmvolterm_63d_jerk_v094_signal,
    f25mc_f25_margin_cyclicality_gmvov_63d_jerk_v095_signal,
    f25mc_f25_margin_cyclicality_gmamp_126d_jerk_v096_signal,
    f25mc_f25_margin_cyclicality_nmamp_63d_jerk_v097_signal,
    f25mc_f25_margin_cyclicality_emamp_126d_jerk_v098_signal,
    f25mc_f25_margin_cyclicality_gmampexp_63d_jerk_v099_signal,
    f25mc_f25_margin_cyclicality_nmamprel_63d_jerk_v100_signal,
    f25mc_f25_margin_cyclicality_omenergy_63d_jerk_v101_signal,
    f25mc_f25_margin_cyclicality_nmpathlen_126d_jerk_v102_signal,
    f25mc_f25_margin_cyclicality_gmampskew_63d_jerk_v103_signal,
    f25mc_f25_margin_cyclicality_nmrangecrush_63d_jerk_v104_signal,
    f25mc_f25_margin_cyclicality_gnspreadamp_63d_jerk_v105_signal,
    f25mc_f25_margin_cyclicality_omconvex_21d_jerk_v106_signal,
    f25mc_f25_margin_cyclicality_gnspreadtrend_21d_jerk_v107_signal,
    f25mc_f25_margin_cyclicality_gespreadz_63d_jerk_v108_signal,
    f25mc_f25_margin_cyclicality_gnspreadcompress_63d_jerk_v109_signal,
    f25mc_f25_margin_cyclicality_passthru_21d_jerk_v110_signal,
    f25mc_f25_margin_cyclicality_gnspreadmac_63d_jerk_v111_signal,
    f25mc_f25_margin_cyclicality_enspreadpos_63d_jerk_v112_signal,
    f25mc_f25_margin_cyclicality_gospreadvol_63d_jerk_v113_signal,
    f25mc_f25_margin_cyclicality_onspread_21d_jerk_v114_signal,
    f25mc_f25_margin_cyclicality_gespreadtr_21d_jerk_v115_signal,
    f25mc_f25_margin_cyclicality_gmtrend_63d_jerk_v116_signal,
    f25mc_f25_margin_cyclicality_nmtrend_21d_jerk_v117_signal,
    f25mc_f25_margin_cyclicality_emtrend_21d_jerk_v118_signal,
    f25mc_f25_margin_cyclicality_gmmacrosslong_63d_jerk_v119_signal,
    f25mc_f25_margin_cyclicality_nmtrendstr_63d_jerk_v120_signal,
    f25mc_f25_margin_cyclicality_gmeff_21d_jerk_v121_signal,
    f25mc_f25_margin_cyclicality_emtrendaccel_21d_jerk_v122_signal,
    f25mc_f25_margin_cyclicality_nmtrendstrH_21d_jerk_v123_signal,
    f25mc_f25_margin_cyclicality_gmtrendaccel_21d_jerk_v124_signal,
    f25mc_f25_margin_cyclicality_nmtrendpersist_21d_jerk_v125_signal,
    f25mc_f25_margin_cyclicality_gmpeakd_63d_jerk_v126_signal,
    f25mc_f25_margin_cyclicality_nmpeak_63d_jerk_v127_signal,
    f25mc_f25_margin_cyclicality_gmpeakrelL_63d_jerk_v128_signal,
    f25mc_f25_margin_cyclicality_nmrangepos_63d_jerk_v129_signal,
    f25mc_f25_margin_cyclicality_emrangepos_63d_jerk_v130_signal,
    f25mc_f25_margin_cyclicality_gmrunup_63d_jerk_v131_signal,
    f25mc_f25_margin_cyclicality_nmtroughtouch_63d_jerk_v132_signal,
    f25mc_f25_margin_cyclicality_gmpeak_63d_jerk_v133_signal,
    f25mc_f25_margin_cyclicality_nmconvex_21d_jerk_v134_signal,
    f25mc_f25_margin_cyclicality_gmuppertimeL_63d_jerk_v135_signal,
    f25mc_f25_margin_cyclicality_gmexpandfreq_63d_jerk_v136_signal,
    f25mc_f25_margin_cyclicality_gmregimebalL_63d_jerk_v137_signal,
    f25mc_f25_margin_cyclicality_nmskewL_63d_jerk_v138_signal,
    f25mc_f25_margin_cyclicality_gmkurtL_63d_jerk_v139_signal,
    f25mc_f25_margin_cyclicality_gmconvex_21d_jerk_v140_signal,
    f25mc_f25_margin_cyclicality_emconvex_21d_jerk_v141_signal,
    f25mc_f25_margin_cyclicality_gncorrL_63d_jerk_v142_signal,
    f25mc_f25_margin_cyclicality_nebeta_63d_jerk_v143_signal,
    f25mc_f25_margin_cyclicality_margindisp4_63d_jerk_v144_signal,
    f25mc_f25_margin_cyclicality_phaselag_63d_jerk_v145_signal,
    f25mc_f25_margin_cyclicality_nmswingeff_63d_jerk_v146_signal,
    f25mc_f25_margin_cyclicality_nmrebound_63d_jerk_v147_signal,
    f25mc_f25_margin_cyclicality_nmlowband_63d_jerk_v148_signal,
    f25mc_f25_margin_cyclicality_gpmskew_63d_jerk_v149_signal,
    f25mc_f25_margin_cyclicality_nmworstdip_63d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F25_MARGIN_CYCLICALITY_3RD_DERIV_REGISTRY_001_150 = REGISTRY


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

    grossmargin = _fund(2501, base=0.32, drift=0.0, vol=0.16).rename("grossmargin")
    netmargin = _fund(2502, base=0.12, drift=0.0, vol=0.30, allow_neg=False).rename("netmargin")
    ebitdamargin = _fund(2503, base=0.22, drift=0.0, vol=0.22).rename("ebitdamargin")
    opinc = _fund(2504, base=8e7, drift=0.0, vol=0.26, allow_neg=True).rename("opinc")
    revenue = _fund(2505, base=6e8, drift=0.01, vol=0.12).rename("revenue")
    gp = _fund(2506, base=2e8, drift=0.0, vol=0.16).rename("gp")

    cols = {"grossmargin": grossmargin, "netmargin": netmargin,
            "ebitdamargin": ebitdamargin, "opinc": opinc,
            "revenue": revenue, "gp": gp}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        assert any(c in ("grossmargin", "netmargin", "ebitdamargin",
                         "opinc", "revenue", "gp")
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

    print("OK f25_margin_cyclicality_3rd_derivatives_001_150_claude: %d features pass" % n_features)
