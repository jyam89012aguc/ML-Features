import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _roc(s, w):
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _logroc(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _rank(s, w):
    return s.rolling(w, min_periods=max(2, w // 4)).rank(pct=True) - 0.5


def _sd(a, b):
    return a / b.replace(0, np.nan)


def _f37_growth(revenue, w):
    return _roc(revenue, w)


def _f37_gp_growth(gp, w):
    return _roc(gp, w)


def _f37_ocf_margin(ncfo, revenue):
    return ncfo / revenue.replace(0, np.nan)


def _f37_rnd_intensity(rnd, revenue):
    return rnd / revenue.replace(0, np.nan)


def _f37_rule40(revenue, ncfo, w):
    g = _roc(revenue, w)
    m = ncfo / revenue.replace(0, np.nan)
    return g + m


def _f37_durable(revenue, grossmargin, w):
    return _roc(revenue, w) * grossmargin


def f37hg_f37_hypergrowth_signature_durriq_dz252d_jerk_d63_v001_signal(revenue, grossmargin, rnd):
    base = 1.00 * _z(_f37_durable(revenue, grossmargin, 252), 252) + 0.55 * _z(_f37_rnd_intensity(rnd, revenue) * grossmargin, 252)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_r40ocf_dzs126d_jerk_d42_v002_signal(revenue, ncfo):
    base = 1.07 * _z(_f37_rule40(revenue, ncfo, 126), 252) + 0.61 * _z(_sd(ncfo, revenue), 252)
    d = (base - 2.0 * base.shift(42) + base.shift(84)) / 1764.0
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_reislf_dtanh252d_jerk_d84_v003_signal(revenue, rnd, ncfo):
    base = 1.14 * _z(_f37_growth(revenue, 252) - _roc(rnd, 252), 252) + 0.67 * _z(_f37_growth(revenue, 63) * _sd(ncfo, revenue), 252)
    d = base.diff(84) - base.diff(84).shift(84)
    b = np.tanh(1.5 * _z(d, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_slfgpg_dsm63d_jerk_d21_v004_signal(revenue, gp, ncfo):
    base = 1.21 * _z(_f37_growth(revenue, 63) * _sd(ncfo, revenue), 252) + 0.73 * _z(_f37_gp_growth(gp, 504), 252)
    d = base - 2.0 * base.shift(21) + base.shift(42)
    b = _z(d.ewm(span=42, min_periods=21).mean(), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gpmr40_dsq504d_jerk_d78_v005_signal(revenue, grossmargin, gp, ncfo):
    base = 1.28 * _z(_f37_gp_growth(gp, 504) * grossmargin, 252) + 0.79 * _z(_f37_rule40(revenue, ncfo, 126), 252)
    d = (base - 2.0 * base.shift(78) + base.shift(156)) / 6084.0
    b = np.sign(_z(d, 252)) * (_z(d, 252).abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_riqcov_dzl126d_jerk_d63_v006_signal(revenue, grossmargin, rnd, ncfo):
    base = 1.35 * _z(_f37_rnd_intensity(rnd, revenue) * grossmargin, 252) + 0.85 * _z(_sd(ncfo, rnd), 252)
    d = base.diff(63) - base.diff(63).shift(63)
    b = _z(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_blnr4n_dmix252d_jerk_d21_v007_signal(revenue, grossmargin, rnd, ncfo):
    base = 1.42 * _z(_f37_growth(revenue, 252) * (grossmargin + _sd(ncfo, revenue)), 252) + 0.91 * _z(_f37_rule40(revenue, ncfo, 504) - _f37_rnd_intensity(rnd, revenue), 252)
    d = base - 2.0 * base.shift(21) + base.shift(42)
    b = 0.5 * _z(d, 252) + 0.5 * _z(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gpsbln_dz63d_jerk_d42_v008_signal(revenue, grossmargin, gp, ncfo):
    base = 1.00 * _z(_sd(gp, revenue) * _f37_growth(revenue, 63), 252) + 0.97 * _z(_f37_growth(revenue, 126) * (grossmargin + _sd(ncfo, revenue)), 252)
    d = (base - 2.0 * base.shift(42) + base.shift(84)) / 1764.0
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_covrni_dzs504d_jerk_d63_v009_signal(revenue, rnd, ncfo):
    base = 1.07 * _z(_sd(ncfo, rnd), 252) + 1.03 * _z(_f37_rnd_intensity(rnd, revenue), 252)
    d = base.diff(63) - base.diff(63).shift(63)
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gpogpm_dtanh126d_jerk_d21_v010_signal(revenue, grossmargin, gp, ncfo):
    base = 1.14 * _z(_f37_growth(revenue, 126), 252) + _z(_sd(ncfo, revenue), 252) + 0.55 * _z(_f37_gp_growth(gp, 252) * grossmargin, 252)
    d = base - 2.0 * base.shift(21) + base.shift(42)
    b = np.tanh(1.5 * _z(d, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gpggms_dsm252d_jerk_d42_v011_signal(grossmargin, gp):
    base = 1.21 * _z(_f37_gp_growth(gp, 252), 252) + 0.61 * _z(grossmargin, 252)
    d = (base - 2.0 * base.shift(42) + base.shift(84)) / 1764.0
    b = _z(d.ewm(span=42, min_periods=21).mean(), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gmsrei_dsq504d_jerk_d93_v012_signal(revenue, grossmargin, rnd):
    base = 1.28 * _z(grossmargin, 252) + 0.67 * _z(_f37_growth(revenue, 126) - _roc(rnd, 126), 252)
    d = base.diff(93) - base.diff(93).shift(93)
    b = np.sign(_z(d, 252)) * (_z(d, 252).abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_ocfgpo_dzl126d_jerk_d63_v013_signal(revenue, ncfo):
    base = 1.35 * _z(_sd(ncfo, revenue), 252) + 0.73 * _z(_f37_growth(revenue, 252), 252) + _z(_sd(ncfo, revenue), 252)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    b = _z(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_rnidur_dmix63d_jerk_d31_v014_signal(revenue, grossmargin, rnd):
    base = 1.42 * _z(_f37_rnd_intensity(rnd, revenue), 252) + 0.79 * _z(_f37_durable(revenue, grossmargin, 63), 252)
    d = (base - 2.0 * base.shift(31) + base.shift(62)) / 961.0
    b = 0.5 * _z(d, 252) + 0.5 * _z(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_cvxgps_dz252d_jerk_d93_v015_signal(revenue, grossmargin, gp):
    base = 1.00 * _z(_f37_growth(revenue, 252) * grossmargin * grossmargin, 252) + 0.85 * _z(_sd(gp, revenue) * _f37_growth(revenue, 504), 252)
    d = base.diff(93) - base.diff(93).shift(93)
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_r4ncvx_dzs252d_jerk_d63_v016_signal(revenue, grossmargin, rnd, ncfo):
    base = 1.07 * _z(_f37_rule40(revenue, ncfo, 252) - _f37_rnd_intensity(rnd, revenue), 252) + 0.91 * _z(_f37_growth(revenue, 126) * grossmargin * grossmargin, 252)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_durcov_dtanh126d_jerk_d42_v017_signal(revenue, grossmargin, rnd, ncfo):
    base = 1.14 * _z(_f37_durable(revenue, grossmargin, 126), 252) + 0.97 * _z(_sd(ncfo, rnd), 252)
    d = (base - 2.0 * base.shift(42) + base.shift(84)) / 1764.0
    b = np.tanh(1.5 * _z(d, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_r40r4n_dsm252d_jerk_d84_v018_signal(revenue, rnd, ncfo):
    base = 1.21 * _z(_f37_rule40(revenue, ncfo, 252), 252) + 1.03 * _z(_f37_rule40(revenue, ncfo, 63) - _f37_rnd_intensity(rnd, revenue), 252)
    d = base.diff(84) - base.diff(84).shift(84)
    b = _z(d.ewm(span=42, min_periods=21).mean(), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_reibln_dsq63d_jerk_d21_v019_signal(revenue, grossmargin, rnd, ncfo):
    base = 1.28 * _z(_f37_growth(revenue, 63) - _roc(rnd, 63), 252) + 0.55 * _z(_f37_growth(revenue, 504) * (grossmargin + _sd(ncfo, revenue)), 252)
    d = base - 2.0 * base.shift(21) + base.shift(42)
    b = np.sign(_z(d, 252)) * (_z(d, 252).abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_slfrni_dzl504d_jerk_d78_v020_signal(revenue, rnd, ncfo):
    base = 1.35 * _z(_f37_growth(revenue, 504) * _sd(ncfo, revenue), 252) + 0.61 * _z(_f37_rnd_intensity(rnd, revenue), 252)
    d = (base - 2.0 * base.shift(78) + base.shift(156)) / 6084.0
    b = _z(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gpmgps_dmix126d_jerk_d63_v021_signal(revenue, grossmargin, gp):
    base = 1.42 * _z(_f37_gp_growth(gp, 126) * grossmargin, 252) + 0.67 * _z(_sd(gp, revenue) * _f37_growth(revenue, 252), 252)
    d = base.diff(63) - base.diff(63).shift(63)
    b = 0.5 * _z(d, 252) + 0.5 * _z(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_riqgms_dz252d_jerk_d21_v022_signal(revenue, grossmargin, rnd):
    base = 1.00 * _z(_f37_rnd_intensity(rnd, revenue) * grossmargin, 252) + 0.73 * _z(grossmargin, 252)
    d = base - 2.0 * base.shift(21) + base.shift(42)
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_blnrei_dzs63d_jerk_d42_v023_signal(revenue, grossmargin, rnd, ncfo):
    base = 1.07 * _z(_f37_growth(revenue, 63) * (grossmargin + _sd(ncfo, revenue)), 252) + 0.79 * _z(_f37_growth(revenue, 126) - _roc(rnd, 126), 252)
    d = (base - 2.0 * base.shift(42) + base.shift(84)) / 1764.0
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gpsgpo_dtanh504d_jerk_d63_v024_signal(revenue, gp, ncfo):
    base = 1.14 * _z(_sd(gp, revenue) * _f37_growth(revenue, 504), 252) + 0.85 * _z(_f37_growth(revenue, 63), 252) + _z(_sd(ncfo, revenue), 252)
    d = base.diff(63) - base.diff(63).shift(63)
    b = np.tanh(1.5 * _z(d, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_covdur_dsm126d_jerk_d21_v025_signal(revenue, grossmargin, rnd, ncfo):
    base = 1.21 * _z(_sd(ncfo, rnd), 252) + 0.91 * _z(_f37_durable(revenue, grossmargin, 252), 252)
    d = base - 2.0 * base.shift(21) + base.shift(42)
    b = _z(d.ewm(span=42, min_periods=21).mean(), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gpogps_dsq252d_jerk_d42_v026_signal(revenue, gp, ncfo):
    base = 1.28 * _z(_f37_growth(revenue, 252), 252) + _z(_sd(ncfo, revenue), 252) + 0.97 * _z(_sd(gp, revenue) * _f37_growth(revenue, 252), 252)
    d = (base - 2.0 * base.shift(42) + base.shift(84)) / 1764.0
    b = np.sign(_z(d, 252)) * (_z(d, 252).abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gpgcvx_dzl504d_jerk_d93_v027_signal(revenue, grossmargin, gp):
    base = 1.35 * _z(_f37_gp_growth(gp, 504), 252) + 1.03 * _z(_f37_growth(revenue, 126) * grossmargin * grossmargin, 252)
    d = base.diff(93) - base.diff(93).shift(93)
    b = _z(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gmsriq_dmix126d_jerk_d63_v028_signal(revenue, grossmargin, rnd):
    base = 1.42 * _z(grossmargin, 252) + 0.55 * _z(_f37_rnd_intensity(rnd, revenue) * grossmargin, 252)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    b = 0.5 * _z(d, 252) + 0.5 * _z(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_ocfr4n_dz63d_jerk_d31_v029_signal(revenue, rnd, ncfo):
    base = 1.00 * _z(_sd(ncfo, revenue), 252) + 0.61 * _z(_f37_rule40(revenue, ncfo, 63) - _f37_rnd_intensity(rnd, revenue), 252)
    d = (base - 2.0 * base.shift(31) + base.shift(62)) / 961.0
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_rnislf_dzs252d_jerk_d93_v030_signal(revenue, rnd, ncfo):
    base = 1.07 * _z(_f37_rnd_intensity(rnd, revenue), 252) + 0.67 * _z(_f37_growth(revenue, 504) * _sd(ncfo, revenue), 252)
    d = base.diff(93) - base.diff(93).shift(93)
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_cvxgpg_dtanh252d_jerk_d63_v031_signal(revenue, grossmargin, gp):
    base = 1.14 * _z(_f37_growth(revenue, 252) * grossmargin * grossmargin, 252) + 0.73 * _z(_f37_gp_growth(gp, 126), 252)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    b = np.tanh(1.5 * _z(d, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_r4nr40_dsm126d_jerk_d42_v032_signal(revenue, rnd, ncfo):
    base = 1.21 * _z(_f37_rule40(revenue, ncfo, 126) - _f37_rnd_intensity(rnd, revenue), 252) + 0.79 * _z(_f37_rule40(revenue, ncfo, 252), 252)
    d = (base - 2.0 * base.shift(42) + base.shift(84)) / 1764.0
    b = _z(d.ewm(span=42, min_periods=21).mean(), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_durgms_dsq252d_jerk_d84_v033_signal(revenue, grossmargin):
    base = 1.28 * _z(_f37_durable(revenue, grossmargin, 252), 252) + 0.85 * _z(grossmargin, 252)
    d = base.diff(84) - base.diff(84).shift(84)
    b = np.sign(_z(d, 252)) * (_z(d, 252).abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_r40rei_dzl63d_jerk_d21_v034_signal(revenue, rnd, ncfo):
    base = 1.35 * _z(_f37_rule40(revenue, ncfo, 63), 252) + 0.91 * _z(_f37_growth(revenue, 504) - _roc(rnd, 504), 252)
    d = base - 2.0 * base.shift(21) + base.shift(42)
    b = _z(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_reigpo_dmix504d_jerk_d78_v035_signal(revenue, rnd, ncfo):
    base = 1.42 * _z(_f37_growth(revenue, 504) - _roc(rnd, 504), 252) + 0.97 * _z(_f37_growth(revenue, 126), 252) + _z(_sd(ncfo, revenue), 252)
    d = (base - 2.0 * base.shift(78) + base.shift(156)) / 6084.0
    b = 0.5 * _z(d, 252) + 0.5 * _z(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_slfdur_dz126d_jerk_d63_v036_signal(revenue, grossmargin, ncfo):
    base = 1.00 * _z(_f37_growth(revenue, 126) * _sd(ncfo, revenue), 252) + 1.03 * _z(_f37_durable(revenue, grossmargin, 252), 252)
    d = base.diff(63) - base.diff(63).shift(63)
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gpmgps_dzs252d_jerk_d21_v037_signal(revenue, grossmargin, gp):
    base = 1.07 * _z(_f37_gp_growth(gp, 252) * grossmargin, 252) + 0.55 * _z(_sd(gp, revenue) * _f37_growth(revenue, 504), 252)
    d = base - 2.0 * base.shift(21) + base.shift(42)
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_riqcvx_dtanh63d_jerk_d42_v038_signal(revenue, grossmargin, rnd):
    base = 1.14 * _z(_f37_rnd_intensity(rnd, revenue) * grossmargin, 252) + 0.61 * _z(_f37_growth(revenue, 126) * grossmargin * grossmargin, 252)
    d = (base - 2.0 * base.shift(42) + base.shift(84)) / 1764.0
    b = np.tanh(1.5 * _z(d, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_blnriq_dsm504d_jerk_d63_v039_signal(revenue, grossmargin, rnd, ncfo):
    base = 1.21 * _z(_f37_growth(revenue, 504) * (grossmargin + _sd(ncfo, revenue)), 252) + 0.67 * _z(_f37_rnd_intensity(rnd, revenue) * grossmargin, 252)
    d = base.diff(63) - base.diff(63).shift(63)
    b = _z(d.ewm(span=42, min_periods=21).mean(), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gpsocf_dsq126d_jerk_d21_v040_signal(revenue, gp, ncfo):
    base = 1.28 * _z(_sd(gp, revenue) * _f37_growth(revenue, 126), 252) + 0.73 * _z(_sd(ncfo, revenue), 252)
    d = base - 2.0 * base.shift(21) + base.shift(42)
    b = np.sign(_z(d, 252)) * (_z(d, 252).abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_covslf_dzl252d_jerk_d42_v041_signal(revenue, rnd, ncfo):
    base = 1.35 * _z(_sd(ncfo, rnd), 252) + 0.79 * _z(_f37_growth(revenue, 252) * _sd(ncfo, revenue), 252)
    d = (base - 2.0 * base.shift(42) + base.shift(84)) / 1764.0
    b = _z(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gpogpg_dmix504d_jerk_d93_v042_signal(revenue, gp, ncfo):
    base = 1.42 * _z(_f37_growth(revenue, 504), 252) + _z(_sd(ncfo, revenue), 252) + 0.85 * _z(_f37_gp_growth(gp, 126), 252)
    d = base.diff(93) - base.diff(93).shift(93)
    b = 0.5 * _z(d, 252) + 0.5 * _z(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gpgr40_dz126d_jerk_d63_v043_signal(revenue, gp, ncfo):
    base = 1.00 * _z(_f37_gp_growth(gp, 126), 252) + 0.91 * _z(_f37_rule40(revenue, ncfo, 252), 252)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gmscov_dzs63d_jerk_d31_v044_signal(grossmargin, rnd, ncfo):
    base = 1.07 * _z(grossmargin, 252) + 0.97 * _z(_sd(ncfo, rnd), 252)
    d = (base - 2.0 * base.shift(31) + base.shift(62)) / 961.0
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_ocfr4n_dtanh252d_jerk_d93_v045_signal(revenue, rnd, ncfo):
    base = 1.14 * _z(_sd(ncfo, revenue), 252) + 1.03 * _z(_f37_rule40(revenue, ncfo, 504) - _f37_rnd_intensity(rnd, revenue), 252)
    d = base.diff(93) - base.diff(93).shift(93)
    b = np.tanh(1.5 * _z(d, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_rnibln_dsm252d_jerk_d63_v046_signal(revenue, grossmargin, rnd, ncfo):
    base = 1.21 * _z(_f37_rnd_intensity(rnd, revenue), 252) + 0.55 * _z(_f37_growth(revenue, 126) * (grossmargin + _sd(ncfo, revenue)), 252)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    b = _z(d.ewm(span=42, min_periods=21).mean(), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_cvxrni_dsq126d_jerk_d42_v047_signal(revenue, grossmargin, rnd):
    base = 1.28 * _z(_f37_growth(revenue, 126) * grossmargin * grossmargin, 252) + 0.61 * _z(_f37_rnd_intensity(rnd, revenue), 252)
    d = (base - 2.0 * base.shift(42) + base.shift(84)) / 1764.0
    b = np.sign(_z(d, 252)) * (_z(d, 252).abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_r4ngpm_dzl252d_jerk_d84_v048_signal(revenue, grossmargin, gp, rnd, ncfo):
    base = 1.35 * _z(_f37_rule40(revenue, ncfo, 252) - _f37_rnd_intensity(rnd, revenue), 252) + 0.67 * _z(_f37_gp_growth(gp, 63) * grossmargin, 252)
    d = base.diff(84) - base.diff(84).shift(84)
    b = _z(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_durcvx_dmix63d_jerk_d21_v049_signal(revenue, grossmargin):
    base = 1.42 * _z(_f37_durable(revenue, grossmargin, 63), 252) + 0.73 * _z(_f37_growth(revenue, 504) * grossmargin * grossmargin, 252)
    d = base - 2.0 * base.shift(21) + base.shift(42)
    b = 0.5 * _z(d, 252) + 0.5 * _z(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_r40riq_dz504d_jerk_d78_v050_signal(revenue, grossmargin, rnd, ncfo):
    base = 1.00 * _z(_f37_rule40(revenue, ncfo, 504), 252) + 0.79 * _z(_f37_rnd_intensity(rnd, revenue) * grossmargin, 252)
    d = (base - 2.0 * base.shift(78) + base.shift(156)) / 6084.0
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_reiocf_dzs126d_jerk_d63_v051_signal(revenue, rnd, ncfo):
    base = 1.07 * _z(_f37_growth(revenue, 126) - _roc(rnd, 126), 252) + 0.85 * _z(_sd(ncfo, revenue), 252)
    d = base.diff(63) - base.diff(63).shift(63)
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_slfbln_dtanh252d_jerk_d21_v052_signal(revenue, grossmargin, ncfo):
    base = 1.14 * _z(_f37_growth(revenue, 252) * _sd(ncfo, revenue), 252) + 0.91 * _z(_f37_growth(revenue, 504) * (grossmargin + _sd(ncfo, revenue)), 252)
    d = base - 2.0 * base.shift(21) + base.shift(42)
    b = np.tanh(1.5 * _z(d, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gpmgpg_dsm63d_jerk_d42_v053_signal(grossmargin, gp):
    base = 1.21 * _z(_f37_gp_growth(gp, 63) * grossmargin, 252) + 0.97 * _z(_f37_gp_growth(gp, 126), 252)
    d = (base - 2.0 * base.shift(42) + base.shift(84)) / 1764.0
    b = _z(d.ewm(span=42, min_periods=21).mean(), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_riqr40_dsq504d_jerk_d63_v054_signal(revenue, grossmargin, rnd, ncfo):
    base = 1.28 * _z(_f37_rnd_intensity(rnd, revenue) * grossmargin, 252) + 1.03 * _z(_f37_rule40(revenue, ncfo, 63), 252)
    d = base.diff(63) - base.diff(63).shift(63)
    b = np.sign(_z(d, 252)) * (_z(d, 252).abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_blncov_dzl126d_jerk_d21_v055_signal(revenue, grossmargin, rnd, ncfo):
    base = 1.35 * _z(_f37_growth(revenue, 126) * (grossmargin + _sd(ncfo, revenue)), 252) + 0.55 * _z(_sd(ncfo, rnd), 252)
    d = base - 2.0 * base.shift(21) + base.shift(42)
    b = _z(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gpsr4n_dmix252d_jerk_d42_v056_signal(revenue, gp, rnd, ncfo):
    base = 1.42 * _z(_sd(gp, revenue) * _f37_growth(revenue, 252), 252) + 0.61 * _z(_f37_rule40(revenue, ncfo, 252) - _f37_rnd_intensity(rnd, revenue), 252)
    d = (base - 2.0 * base.shift(42) + base.shift(84)) / 1764.0
    b = 0.5 * _z(d, 252) + 0.5 * _z(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_covbln_dz504d_jerk_d93_v057_signal(revenue, grossmargin, rnd, ncfo):
    base = 1.00 * _z(_sd(ncfo, rnd), 252) + 0.67 * _z(_f37_growth(revenue, 126) * (grossmargin + _sd(ncfo, revenue)), 252)
    d = base.diff(93) - base.diff(93).shift(93)
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gporni_dzs126d_jerk_d63_v058_signal(revenue, rnd, ncfo):
    base = 1.07 * _z(_f37_growth(revenue, 126), 252) + _z(_sd(ncfo, revenue), 252) + 0.73 * _z(_f37_rnd_intensity(rnd, revenue), 252)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gpggpm_dtanh63d_jerk_d31_v059_signal(grossmargin, gp):
    base = 1.14 * _z(_f37_gp_growth(gp, 63), 252) + 0.79 * _z(_f37_gp_growth(gp, 63) * grossmargin, 252)
    d = (base - 2.0 * base.shift(31) + base.shift(62)) / 961.0
    b = np.tanh(1.5 * _z(d, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gmscvx_dsm252d_jerk_d93_v060_signal(revenue, grossmargin):
    base = 1.21 * _z(grossmargin, 252) + 0.85 * _z(_f37_growth(revenue, 504) * grossmargin * grossmargin, 252)
    d = base.diff(93) - base.diff(93).shift(93)
    b = _z(d.ewm(span=42, min_periods=21).mean(), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_ocfrei_dsq252d_jerk_d63_v061_signal(revenue, rnd, ncfo):
    base = 1.28 * _z(_sd(ncfo, revenue), 252) + 0.91 * _z(_f37_growth(revenue, 126) - _roc(rnd, 126), 252)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    b = np.sign(_z(d, 252)) * (_z(d, 252).abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_rnigpo_dzl126d_jerk_d42_v062_signal(revenue, rnd, ncfo):
    base = 1.35 * _z(_f37_rnd_intensity(rnd, revenue), 252) + 0.97 * _z(_f37_growth(revenue, 252), 252) + _z(_sd(ncfo, revenue), 252)
    d = (base - 2.0 * base.shift(42) + base.shift(84)) / 1764.0
    b = _z(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_cvxdur_dmix252d_jerk_d84_v063_signal(revenue, grossmargin):
    base = 1.42 * _z(_f37_growth(revenue, 252) * grossmargin * grossmargin, 252) + 1.03 * _z(_f37_durable(revenue, grossmargin, 63), 252)
    d = base.diff(84) - base.diff(84).shift(84)
    b = 0.5 * _z(d, 252) + 0.5 * _z(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_r4ngps_dz63d_jerk_d21_v064_signal(revenue, gp, rnd, ncfo):
    base = 1.00 * _z(_f37_rule40(revenue, ncfo, 63) - _f37_rnd_intensity(rnd, revenue), 252) + 0.55 * _z(_sd(gp, revenue) * _f37_growth(revenue, 504), 252)
    d = base - 2.0 * base.shift(21) + base.shift(42)
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_durr40_dzs504d_jerk_d78_v065_signal(revenue, grossmargin, ncfo):
    base = 1.07 * _z(_f37_durable(revenue, grossmargin, 504), 252) + 0.61 * _z(_f37_rule40(revenue, ncfo, 126), 252)
    d = (base - 2.0 * base.shift(78) + base.shift(156)) / 6084.0
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_r40cov_dtanh126d_jerk_d63_v066_signal(revenue, rnd, ncfo):
    base = 1.14 * _z(_f37_rule40(revenue, ncfo, 126), 252) + 0.67 * _z(_sd(ncfo, rnd), 252)
    d = base.diff(63) - base.diff(63).shift(63)
    b = np.tanh(1.5 * _z(d, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_reir4n_dsm252d_jerk_d21_v067_signal(revenue, rnd, ncfo):
    base = 1.21 * _z(_f37_growth(revenue, 252) - _roc(rnd, 252), 252) + 0.73 * _z(_f37_rule40(revenue, ncfo, 504) - _f37_rnd_intensity(rnd, revenue), 252)
    d = base - 2.0 * base.shift(21) + base.shift(42)
    b = _z(d.ewm(span=42, min_periods=21).mean(), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_slfbln_dsq63d_jerk_d42_v068_signal(revenue, grossmargin, ncfo):
    base = 1.28 * _z(_f37_growth(revenue, 63) * _sd(ncfo, revenue), 252) + 0.79 * _z(_f37_growth(revenue, 126) * (grossmargin + _sd(ncfo, revenue)), 252)
    d = (base - 2.0 * base.shift(42) + base.shift(84)) / 1764.0
    b = np.sign(_z(d, 252)) * (_z(d, 252).abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gpmrni_dzl504d_jerk_d63_v069_signal(revenue, grossmargin, gp, rnd):
    base = 1.35 * _z(_f37_gp_growth(gp, 504) * grossmargin, 252) + 0.85 * _z(_f37_rnd_intensity(rnd, revenue), 252)
    d = base.diff(63) - base.diff(63).shift(63)
    b = _z(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_riqgpm_dmix126d_jerk_d21_v070_signal(revenue, grossmargin, gp, rnd):
    base = 1.42 * _z(_f37_rnd_intensity(rnd, revenue) * grossmargin, 252) + 0.91 * _z(_f37_gp_growth(gp, 252) * grossmargin, 252)
    d = base - 2.0 * base.shift(21) + base.shift(42)
    b = 0.5 * _z(d, 252) + 0.5 * _z(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_blngms_dz252d_jerk_d42_v071_signal(revenue, grossmargin, ncfo):
    base = 1.00 * _z(_f37_growth(revenue, 252) * (grossmargin + _sd(ncfo, revenue)), 252) + 0.97 * _z(grossmargin, 252)
    d = (base - 2.0 * base.shift(42) + base.shift(84)) / 1764.0
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gpsrei_dzs504d_jerk_d93_v072_signal(revenue, gp, rnd):
    base = 1.07 * _z(_sd(gp, revenue) * _f37_growth(revenue, 504), 252) + 1.03 * _z(_f37_growth(revenue, 126) - _roc(rnd, 126), 252)
    d = base.diff(93) - base.diff(93).shift(93)
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_covgpo_dtanh126d_jerk_d63_v073_signal(revenue, rnd, ncfo):
    base = 1.14 * _z(_sd(ncfo, rnd), 252) + 0.55 * _z(_f37_growth(revenue, 252), 252) + _z(_sd(ncfo, revenue), 252)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    b = np.tanh(1.5 * _z(d, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gpodur_dsm63d_jerk_d31_v074_signal(revenue, grossmargin, ncfo):
    base = 1.21 * _z(_f37_growth(revenue, 63), 252) + _z(_sd(ncfo, revenue), 252) + 0.61 * _z(_f37_durable(revenue, grossmargin, 63), 252)
    d = (base - 2.0 * base.shift(31) + base.shift(62)) / 961.0
    b = _z(d.ewm(span=42, min_periods=21).mean(), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gpggps_dsq252d_jerk_d93_v075_signal(revenue, gp):
    base = 1.28 * _z(_f37_gp_growth(gp, 252), 252) + 0.67 * _z(_sd(gp, revenue) * _f37_growth(revenue, 504), 252)
    d = base.diff(93) - base.diff(93).shift(93)
    b = np.sign(_z(d, 252)) * (_z(d, 252).abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gmscvx_dzl252d_jerk_d63_v076_signal(revenue, grossmargin):
    base = 1.35 * _z(grossmargin, 252) + 0.73 * _z(_f37_growth(revenue, 126) * grossmargin * grossmargin, 252)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    b = _z(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_ocfriq_dmix126d_jerk_d42_v077_signal(revenue, grossmargin, rnd, ncfo):
    base = 1.42 * _z(_sd(ncfo, revenue), 252) + 0.79 * _z(_f37_rnd_intensity(rnd, revenue) * grossmargin, 252)
    d = (base - 2.0 * base.shift(42) + base.shift(84)) / 1764.0
    b = 0.5 * _z(d, 252) + 0.5 * _z(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_rniocf_dz252d_jerk_d84_v078_signal(revenue, rnd, ncfo):
    base = 1.00 * _z(_f37_rnd_intensity(rnd, revenue), 252) + 0.85 * _z(_sd(ncfo, revenue), 252)
    d = base.diff(84) - base.diff(84).shift(84)
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_cvxslf_dzs63d_jerk_d21_v079_signal(revenue, grossmargin, ncfo):
    base = 1.07 * _z(_f37_growth(revenue, 63) * grossmargin * grossmargin, 252) + 0.91 * _z(_f37_growth(revenue, 504) * _sd(ncfo, revenue), 252)
    d = base - 2.0 * base.shift(21) + base.shift(42)
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_r4ngpg_dtanh504d_jerk_d78_v080_signal(revenue, gp, rnd, ncfo):
    base = 1.14 * _z(_f37_rule40(revenue, ncfo, 504) - _f37_rnd_intensity(rnd, revenue), 252) + 0.97 * _z(_f37_gp_growth(gp, 126), 252)
    d = (base - 2.0 * base.shift(78) + base.shift(156)) / 6084.0
    b = np.tanh(1.5 * _z(d, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_durgpm_dsm126d_jerk_d63_v081_signal(revenue, grossmargin, gp):
    base = 1.21 * _z(_f37_durable(revenue, grossmargin, 126), 252) + 1.03 * _z(_f37_gp_growth(gp, 252) * grossmargin, 252)
    d = base.diff(63) - base.diff(63).shift(63)
    b = _z(d.ewm(span=42, min_periods=21).mean(), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_r40gms_dsq252d_jerk_d21_v082_signal(revenue, grossmargin, ncfo):
    base = 1.28 * _z(_f37_rule40(revenue, ncfo, 252), 252) + 0.55 * _z(grossmargin, 252)
    d = base - 2.0 * base.shift(21) + base.shift(42)
    b = np.sign(_z(d, 252)) * (_z(d, 252).abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_reiriq_dzl63d_jerk_d42_v083_signal(revenue, grossmargin, rnd):
    base = 1.35 * _z(_f37_growth(revenue, 63) - _roc(rnd, 63), 252) + 0.61 * _z(_f37_rnd_intensity(rnd, revenue) * grossmargin, 252)
    d = (base - 2.0 * base.shift(42) + base.shift(84)) / 1764.0
    b = _z(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_slfgpo_dmix504d_jerk_d63_v084_signal(revenue, ncfo):
    base = 1.42 * _z(_f37_growth(revenue, 504) * _sd(ncfo, revenue), 252) + 0.67 * _z(_f37_growth(revenue, 63), 252) + _z(_sd(ncfo, revenue), 252)
    d = base.diff(63) - base.diff(63).shift(63)
    b = 0.5 * _z(d, 252) + 0.5 * _z(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gpmdur_dz126d_jerk_d21_v085_signal(revenue, grossmargin, gp):
    base = 1.00 * _z(_f37_gp_growth(gp, 126) * grossmargin, 252) + 0.73 * _z(_f37_durable(revenue, grossmargin, 252), 252)
    d = base - 2.0 * base.shift(21) + base.shift(42)
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_riqgps_dzs252d_jerk_d42_v086_signal(revenue, grossmargin, gp, rnd):
    base = 1.07 * _z(_f37_rnd_intensity(rnd, revenue) * grossmargin, 252) + 0.79 * _z(_sd(gp, revenue) * _f37_growth(revenue, 252), 252)
    d = (base - 2.0 * base.shift(42) + base.shift(84)) / 1764.0
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_blncvx_dtanh504d_jerk_d93_v087_signal(revenue, grossmargin, ncfo):
    base = 1.14 * _z(_f37_growth(revenue, 504) * (grossmargin + _sd(ncfo, revenue)), 252) + 0.85 * _z(_f37_growth(revenue, 126) * grossmargin * grossmargin, 252)
    d = base.diff(93) - base.diff(93).shift(93)
    b = np.tanh(1.5 * _z(d, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gpsriq_dsm126d_jerk_d63_v088_signal(revenue, grossmargin, gp, rnd):
    base = 1.21 * _z(_sd(gp, revenue) * _f37_growth(revenue, 126), 252) + 0.91 * _z(_f37_rnd_intensity(rnd, revenue) * grossmargin, 252)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    b = _z(d.ewm(span=42, min_periods=21).mean(), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_covocf_dsq63d_jerk_d31_v089_signal(revenue, rnd, ncfo):
    base = 1.28 * _z(_sd(ncfo, rnd), 252) + 0.97 * _z(_sd(ncfo, revenue), 252)
    d = (base - 2.0 * base.shift(31) + base.shift(62)) / 961.0
    b = np.sign(_z(d, 252)) * (_z(d, 252).abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gposlf_dzl252d_jerk_d93_v090_signal(revenue, ncfo):
    base = 1.35 * _z(_f37_growth(revenue, 252), 252) + _z(_sd(ncfo, revenue), 252) + 1.03 * _z(_f37_growth(revenue, 504) * _sd(ncfo, revenue), 252)
    d = base.diff(93) - base.diff(93).shift(93)
    b = _z(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gpgrni_dmix252d_jerk_d63_v091_signal(revenue, gp, rnd):
    base = 1.42 * _z(_f37_gp_growth(gp, 252), 252) + 0.55 * _z(_f37_rnd_intensity(rnd, revenue), 252)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    b = 0.5 * _z(d, 252) + 0.5 * _z(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gmsr40_dz126d_jerk_d42_v092_signal(revenue, grossmargin, ncfo):
    base = 1.00 * _z(grossmargin, 252) + 0.61 * _z(_f37_rule40(revenue, ncfo, 252), 252)
    d = (base - 2.0 * base.shift(42) + base.shift(84)) / 1764.0
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_ocfcov_dzs252d_jerk_d84_v093_signal(revenue, rnd, ncfo):
    base = 1.07 * _z(_sd(ncfo, revenue), 252) + 0.67 * _z(_sd(ncfo, rnd), 252)
    d = base.diff(84) - base.diff(84).shift(84)
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_rnir4n_dtanh63d_jerk_d21_v094_signal(revenue, rnd, ncfo):
    base = 1.14 * _z(_f37_rnd_intensity(rnd, revenue), 252) + 0.73 * _z(_f37_rule40(revenue, ncfo, 504) - _f37_rnd_intensity(rnd, revenue), 252)
    d = base - 2.0 * base.shift(21) + base.shift(42)
    b = np.tanh(1.5 * _z(d, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_cvxbln_dsm504d_jerk_d78_v095_signal(revenue, grossmargin, ncfo):
    base = 1.21 * _z(_f37_growth(revenue, 504) * grossmargin * grossmargin, 252) + 0.79 * _z(_f37_growth(revenue, 126) * (grossmargin + _sd(ncfo, revenue)), 252)
    d = (base - 2.0 * base.shift(78) + base.shift(156)) / 6084.0
    b = _z(d.ewm(span=42, min_periods=21).mean(), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_r4nrni_dsq126d_jerk_d63_v096_signal(revenue, rnd, ncfo):
    base = 1.28 * _z(_f37_rule40(revenue, ncfo, 126) - _f37_rnd_intensity(rnd, revenue), 252) + 0.85 * _z(_f37_rnd_intensity(rnd, revenue), 252)
    d = base.diff(63) - base.diff(63).shift(63)
    b = np.sign(_z(d, 252)) * (_z(d, 252).abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_durgps_dzl252d_jerk_d21_v097_signal(revenue, grossmargin, gp):
    base = 1.35 * _z(_f37_durable(revenue, grossmargin, 252), 252) + 0.91 * _z(_sd(gp, revenue) * _f37_growth(revenue, 504), 252)
    d = base - 2.0 * base.shift(21) + base.shift(42)
    b = _z(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_r40cvx_dmix63d_jerk_d42_v098_signal(revenue, grossmargin, ncfo):
    base = 1.42 * _z(_f37_rule40(revenue, ncfo, 63), 252) + 0.97 * _z(_f37_growth(revenue, 126) * grossmargin * grossmargin, 252)
    d = (base - 2.0 * base.shift(42) + base.shift(84)) / 1764.0
    b = 0.5 * _z(d, 252) + 0.5 * _z(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_reiriq_dz504d_jerk_d63_v099_signal(revenue, grossmargin, rnd):
    base = 1.00 * _z(_f37_growth(revenue, 504) - _roc(rnd, 504), 252) + 1.03 * _z(_f37_rnd_intensity(rnd, revenue) * grossmargin, 252)
    d = base.diff(63) - base.diff(63).shift(63)
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_slfocf_dzs126d_jerk_d21_v100_signal(revenue, ncfo):
    base = 1.07 * _z(_f37_growth(revenue, 126) * _sd(ncfo, revenue), 252) + 0.55 * _z(_sd(ncfo, revenue), 252)
    d = base - 2.0 * base.shift(21) + base.shift(42)
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gpmslf_dtanh252d_jerk_d42_v101_signal(revenue, grossmargin, gp, ncfo):
    base = 1.14 * _z(_f37_gp_growth(gp, 252) * grossmargin, 252) + 0.61 * _z(_f37_growth(revenue, 252) * _sd(ncfo, revenue), 252)
    d = (base - 2.0 * base.shift(42) + base.shift(84)) / 1764.0
    b = np.tanh(1.5 * _z(d, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_riqgpg_dsm504d_jerk_d93_v102_signal(revenue, grossmargin, gp, rnd):
    base = 1.21 * _z(_f37_rnd_intensity(rnd, revenue) * grossmargin, 252) + 0.67 * _z(_f37_gp_growth(gp, 126), 252)
    d = base.diff(93) - base.diff(93).shift(93)
    b = _z(d.ewm(span=42, min_periods=21).mean(), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_blnr40_dsq126d_jerk_d63_v103_signal(revenue, grossmargin, ncfo):
    base = 1.28 * _z(_f37_growth(revenue, 126) * (grossmargin + _sd(ncfo, revenue)), 252) + 0.73 * _z(_f37_rule40(revenue, ncfo, 252), 252)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    b = np.sign(_z(d, 252)) * (_z(d, 252).abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gpscov_dzl63d_jerk_d31_v104_signal(revenue, gp, rnd, ncfo):
    base = 1.35 * _z(_sd(gp, revenue) * _f37_growth(revenue, 63), 252) + 0.79 * _z(_sd(ncfo, rnd), 252)
    d = (base - 2.0 * base.shift(31) + base.shift(62)) / 961.0
    b = _z(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_covr4n_dmix252d_jerk_d93_v105_signal(revenue, rnd, ncfo):
    base = 1.42 * _z(_sd(ncfo, rnd), 252) + 0.85 * _z(_f37_rule40(revenue, ncfo, 504) - _f37_rnd_intensity(rnd, revenue), 252)
    d = base.diff(93) - base.diff(93).shift(93)
    b = 0.5 * _z(d, 252) + 0.5 * _z(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gpobln_dz252d_jerk_d63_v106_signal(revenue, grossmargin, ncfo):
    base = 1.00 * _z(_f37_growth(revenue, 252), 252) + _z(_sd(ncfo, revenue), 252) + 0.91 * _z(_f37_growth(revenue, 126) * (grossmargin + _sd(ncfo, revenue)), 252)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gpgrni_dzs126d_jerk_d42_v107_signal(revenue, gp, rnd):
    base = 1.07 * _z(_f37_gp_growth(gp, 126), 252) + 0.97 * _z(_f37_rnd_intensity(rnd, revenue), 252)
    d = (base - 2.0 * base.shift(42) + base.shift(84)) / 1764.0
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gmsgpm_dtanh252d_jerk_d84_v108_signal(grossmargin, gp):
    base = 1.14 * _z(grossmargin, 252) + 1.03 * _z(_f37_gp_growth(gp, 63) * grossmargin, 252)
    d = base.diff(84) - base.diff(84).shift(84)
    b = np.tanh(1.5 * _z(d, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_ocfgms_dsm63d_jerk_d21_v109_signal(revenue, grossmargin, ncfo):
    base = 1.21 * _z(_sd(ncfo, revenue), 252) + 0.55 * _z(grossmargin, 252)
    d = base - 2.0 * base.shift(21) + base.shift(42)
    b = _z(d.ewm(span=42, min_periods=21).mean(), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_rnirei_dsq504d_jerk_d78_v110_signal(revenue, rnd):
    base = 1.28 * _z(_f37_rnd_intensity(rnd, revenue), 252) + 0.61 * _z(_f37_growth(revenue, 126) - _roc(rnd, 126), 252)
    d = (base - 2.0 * base.shift(78) + base.shift(156)) / 6084.0
    b = np.sign(_z(d, 252)) * (_z(d, 252).abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_cvxgpo_dzl126d_jerk_d63_v111_signal(revenue, grossmargin, ncfo):
    base = 1.35 * _z(_f37_growth(revenue, 126) * grossmargin * grossmargin, 252) + 0.67 * _z(_f37_growth(revenue, 252), 252) + _z(_sd(ncfo, revenue), 252)
    d = base.diff(63) - base.diff(63).shift(63)
    b = _z(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_r4ndur_dmix252d_jerk_d21_v112_signal(revenue, grossmargin, rnd, ncfo):
    base = 1.42 * _z(_f37_rule40(revenue, ncfo, 252) - _f37_rnd_intensity(rnd, revenue), 252) + 0.73 * _z(_f37_durable(revenue, grossmargin, 504), 252)
    d = base - 2.0 * base.shift(21) + base.shift(42)
    b = 0.5 * _z(d, 252) + 0.5 * _z(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_durgpg_dz63d_jerk_d42_v113_signal(revenue, grossmargin, gp):
    base = 1.00 * _z(_f37_durable(revenue, grossmargin, 63), 252) + 0.79 * _z(_f37_gp_growth(gp, 126), 252)
    d = (base - 2.0 * base.shift(42) + base.shift(84)) / 1764.0
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_r40gpm_dzs504d_jerk_d63_v114_signal(revenue, grossmargin, gp, ncfo):
    base = 1.07 * _z(_f37_rule40(revenue, ncfo, 504), 252) + 0.85 * _z(_f37_gp_growth(gp, 63) * grossmargin, 252)
    d = base.diff(63) - base.diff(63).shift(63)
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_reicov_dtanh126d_jerk_d21_v115_signal(revenue, rnd, ncfo):
    base = 1.14 * _z(_f37_growth(revenue, 126) - _roc(rnd, 126), 252) + 0.91 * _z(_sd(ncfo, rnd), 252)
    d = base - 2.0 * base.shift(21) + base.shift(42)
    b = np.tanh(1.5 * _z(d, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_slfr4n_dsm252d_jerk_d42_v116_signal(revenue, rnd, ncfo):
    base = 1.21 * _z(_f37_growth(revenue, 252) * _sd(ncfo, revenue), 252) + 0.97 * _z(_f37_rule40(revenue, ncfo, 252) - _f37_rnd_intensity(rnd, revenue), 252)
    d = (base - 2.0 * base.shift(42) + base.shift(84)) / 1764.0
    b = _z(d.ewm(span=42, min_periods=21).mean(), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gpmbln_dsq504d_jerk_d93_v117_signal(revenue, grossmargin, gp, ncfo):
    base = 1.28 * _z(_f37_gp_growth(gp, 504) * grossmargin, 252) + 1.03 * _z(_f37_growth(revenue, 126) * (grossmargin + _sd(ncfo, revenue)), 252)
    d = base.diff(93) - base.diff(93).shift(93)
    b = np.sign(_z(d, 252)) * (_z(d, 252).abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_riqrni_dzl126d_jerk_d63_v118_signal(revenue, grossmargin, rnd):
    base = 1.35 * _z(_f37_rnd_intensity(rnd, revenue) * grossmargin, 252) + 0.55 * _z(_f37_rnd_intensity(rnd, revenue), 252)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    b = _z(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_blngpm_dmix63d_jerk_d31_v119_signal(revenue, grossmargin, gp, ncfo):
    base = 1.42 * _z(_f37_growth(revenue, 63) * (grossmargin + _sd(ncfo, revenue)), 252) + 0.61 * _z(_f37_gp_growth(gp, 63) * grossmargin, 252)
    d = (base - 2.0 * base.shift(31) + base.shift(62)) / 961.0
    b = 0.5 * _z(d, 252) + 0.5 * _z(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gpsgms_dz252d_jerk_d93_v120_signal(revenue, grossmargin, gp):
    base = 1.00 * _z(_sd(gp, revenue) * _f37_growth(revenue, 252), 252) + 0.67 * _z(grossmargin, 252)
    d = base.diff(93) - base.diff(93).shift(93)
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_covrei_dzs252d_jerk_d63_v121_signal(revenue, rnd, ncfo):
    base = 1.07 * _z(_sd(ncfo, rnd), 252) + 0.73 * _z(_f37_growth(revenue, 126) - _roc(rnd, 126), 252)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gpoocf_dtanh126d_jerk_d42_v122_signal(revenue, ncfo):
    base = 1.14 * _z(_f37_growth(revenue, 126), 252) + _z(_sd(ncfo, revenue), 252) + 0.79 * _z(_sd(ncfo, revenue), 252)
    d = (base - 2.0 * base.shift(42) + base.shift(84)) / 1764.0
    b = np.tanh(1.5 * _z(d, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gpgdur_dsm252d_jerk_d84_v123_signal(revenue, grossmargin, gp):
    base = 1.21 * _z(_f37_gp_growth(gp, 252), 252) + 0.85 * _z(_f37_durable(revenue, grossmargin, 63), 252)
    d = base.diff(84) - base.diff(84).shift(84)
    b = _z(d.ewm(span=42, min_periods=21).mean(), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gmsgps_dsq63d_jerk_d21_v124_signal(revenue, grossmargin, gp):
    base = 1.28 * _z(grossmargin, 252) + 0.91 * _z(_sd(gp, revenue) * _f37_growth(revenue, 504), 252)
    d = base - 2.0 * base.shift(21) + base.shift(42)
    b = np.sign(_z(d, 252)) * (_z(d, 252).abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_ocfcvx_dzl504d_jerk_d78_v125_signal(revenue, grossmargin, ncfo):
    base = 1.35 * _z(_sd(ncfo, revenue), 252) + 0.97 * _z(_f37_growth(revenue, 126) * grossmargin * grossmargin, 252)
    d = (base - 2.0 * base.shift(78) + base.shift(156)) / 6084.0
    b = _z(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_rniriq_dmix126d_jerk_d63_v126_signal(revenue, grossmargin, rnd):
    base = 1.42 * _z(_f37_rnd_intensity(rnd, revenue), 252) + 1.03 * _z(_f37_rnd_intensity(rnd, revenue) * grossmargin, 252)
    d = base.diff(63) - base.diff(63).shift(63)
    b = 0.5 * _z(d, 252) + 0.5 * _z(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_cvxocf_dz252d_jerk_d21_v127_signal(revenue, grossmargin, ncfo):
    base = 1.00 * _z(_f37_growth(revenue, 252) * grossmargin * grossmargin, 252) + 0.55 * _z(_sd(ncfo, revenue), 252)
    d = base - 2.0 * base.shift(21) + base.shift(42)
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_r4nslf_dzs63d_jerk_d42_v128_signal(revenue, rnd, ncfo):
    base = 1.07 * _z(_f37_rule40(revenue, ncfo, 63) - _f37_rnd_intensity(rnd, revenue), 252) + 0.61 * _z(_f37_growth(revenue, 126) * _sd(ncfo, revenue), 252)
    d = (base - 2.0 * base.shift(42) + base.shift(84)) / 1764.0
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_durrni_dtanh504d_jerk_d63_v129_signal(revenue, grossmargin, rnd):
    base = 1.14 * _z(_f37_durable(revenue, grossmargin, 504), 252) + 0.67 * _z(_f37_rnd_intensity(rnd, revenue), 252)
    d = base.diff(63) - base.diff(63).shift(63)
    b = np.tanh(1.5 * _z(d, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_r40gpm_dsm126d_jerk_d21_v130_signal(revenue, grossmargin, gp, ncfo):
    base = 1.21 * _z(_f37_rule40(revenue, ncfo, 126), 252) + 0.73 * _z(_f37_gp_growth(gp, 252) * grossmargin, 252)
    d = base - 2.0 * base.shift(21) + base.shift(42)
    b = _z(d.ewm(span=42, min_periods=21).mean(), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_reigms_dsq252d_jerk_d42_v131_signal(revenue, grossmargin, rnd):
    base = 1.28 * _z(_f37_growth(revenue, 252) - _roc(rnd, 252), 252) + 0.79 * _z(grossmargin, 252)
    d = (base - 2.0 * base.shift(42) + base.shift(84)) / 1764.0
    b = np.sign(_z(d, 252)) * (_z(d, 252).abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_slfrei_dzl504d_jerk_d93_v132_signal(revenue, rnd, ncfo):
    base = 1.35 * _z(_f37_growth(revenue, 504) * _sd(ncfo, revenue), 252) + 0.85 * _z(_f37_growth(revenue, 126) - _roc(rnd, 126), 252)
    d = base.diff(93) - base.diff(93).shift(93)
    b = _z(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gpmgpo_dmix126d_jerk_d63_v133_signal(revenue, grossmargin, gp, ncfo):
    base = 1.42 * _z(_f37_gp_growth(gp, 126) * grossmargin, 252) + 0.91 * _z(_f37_growth(revenue, 252), 252) + _z(_sd(ncfo, revenue), 252)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    b = 0.5 * _z(d, 252) + 0.5 * _z(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_riqdur_dz63d_jerk_d31_v134_signal(revenue, grossmargin, rnd):
    base = 1.00 * _z(_f37_rnd_intensity(rnd, revenue) * grossmargin, 252) + 0.97 * _z(_f37_durable(revenue, grossmargin, 63), 252)
    d = (base - 2.0 * base.shift(31) + base.shift(62)) / 961.0
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_blngps_dzs252d_jerk_d93_v135_signal(revenue, grossmargin, gp, ncfo):
    base = 1.07 * _z(_f37_growth(revenue, 252) * (grossmargin + _sd(ncfo, revenue)), 252) + 1.03 * _z(_sd(gp, revenue) * _f37_growth(revenue, 504), 252)
    d = base.diff(93) - base.diff(93).shift(93)
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gpscvx_dtanh252d_jerk_d63_v136_signal(revenue, grossmargin, gp):
    base = 1.14 * _z(_sd(gp, revenue) * _f37_growth(revenue, 252), 252) + 0.55 * _z(_f37_growth(revenue, 126) * grossmargin * grossmargin, 252)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    b = np.tanh(1.5 * _z(d, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_covriq_dsm126d_jerk_d42_v137_signal(revenue, grossmargin, rnd, ncfo):
    base = 1.21 * _z(_sd(ncfo, rnd), 252) + 0.61 * _z(_f37_rnd_intensity(rnd, revenue) * grossmargin, 252)
    d = (base - 2.0 * base.shift(42) + base.shift(84)) / 1764.0
    b = _z(d.ewm(span=42, min_periods=21).mean(), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gpoocf_dsq252d_jerk_d84_v138_signal(revenue, ncfo):
    base = 1.28 * _z(_f37_growth(revenue, 252), 252) + _z(_sd(ncfo, revenue), 252) + 0.67 * _z(_sd(ncfo, revenue), 252)
    d = base.diff(84) - base.diff(84).shift(84)
    b = np.sign(_z(d, 252)) * (_z(d, 252).abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gpgslf_dzl63d_jerk_d21_v139_signal(revenue, gp, ncfo):
    base = 1.35 * _z(_f37_gp_growth(gp, 63), 252) + 0.73 * _z(_f37_growth(revenue, 504) * _sd(ncfo, revenue), 252)
    d = base - 2.0 * base.shift(21) + base.shift(42)
    b = _z(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gmsgpg_dmix504d_jerk_d78_v140_signal(grossmargin, gp):
    base = 1.42 * _z(grossmargin, 252) + 0.79 * _z(_f37_gp_growth(gp, 126), 252)
    d = (base - 2.0 * base.shift(78) + base.shift(156)) / 6084.0
    b = 0.5 * _z(d, 252) + 0.5 * _z(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_ocfr40_dz126d_jerk_d63_v141_signal(revenue, ncfo):
    base = 1.00 * _z(_sd(ncfo, revenue), 252) + 0.85 * _z(_f37_rule40(revenue, ncfo, 252), 252)
    d = base.diff(63) - base.diff(63).shift(63)
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_rnicov_dzs252d_jerk_d21_v142_signal(revenue, rnd, ncfo):
    base = 1.07 * _z(_f37_rnd_intensity(rnd, revenue), 252) + 0.91 * _z(_sd(ncfo, rnd), 252)
    d = base - 2.0 * base.shift(21) + base.shift(42)
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_cvxr4n_dtanh63d_jerk_d42_v143_signal(revenue, grossmargin, rnd, ncfo):
    base = 1.14 * _z(_f37_growth(revenue, 63) * grossmargin * grossmargin, 252) + 0.97 * _z(_f37_rule40(revenue, ncfo, 126) - _f37_rnd_intensity(rnd, revenue), 252)
    d = (base - 2.0 * base.shift(42) + base.shift(84)) / 1764.0
    b = np.tanh(1.5 * _z(d, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_r4nbln_dsm504d_jerk_d63_v144_signal(revenue, grossmargin, rnd, ncfo):
    base = 1.21 * _z(_f37_rule40(revenue, ncfo, 504) - _f37_rnd_intensity(rnd, revenue), 252) + 1.03 * _z(_f37_growth(revenue, 63) * (grossmargin + _sd(ncfo, revenue)), 252)
    d = base.diff(63) - base.diff(63).shift(63)
    b = _z(d.ewm(span=42, min_periods=21).mean(), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_durslf_dsq126d_jerk_d21_v145_signal(revenue, grossmargin, ncfo):
    base = 1.28 * _z(_f37_durable(revenue, grossmargin, 126), 252) + 0.55 * _z(_f37_growth(revenue, 252) * _sd(ncfo, revenue), 252)
    d = base - 2.0 * base.shift(21) + base.shift(42)
    b = np.sign(_z(d, 252)) * (_z(d, 252).abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_r40gps_dzl252d_jerk_d42_v146_signal(revenue, gp, ncfo):
    base = 1.35 * _z(_f37_rule40(revenue, ncfo, 252), 252) + 0.61 * _z(_sd(gp, revenue) * _f37_growth(revenue, 252), 252)
    d = (base - 2.0 * base.shift(42) + base.shift(84)) / 1764.0
    b = _z(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_reicvx_dmix504d_jerk_d93_v147_signal(revenue, grossmargin, rnd):
    base = 1.42 * _z(_f37_growth(revenue, 504) - _roc(rnd, 504), 252) + 0.67 * _z(_f37_growth(revenue, 126) * grossmargin * grossmargin, 252)
    d = base.diff(93) - base.diff(93).shift(93)
    b = 0.5 * _z(d, 252) + 0.5 * _z(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_slfriq_dz126d_jerk_d63_v148_signal(revenue, grossmargin, rnd, ncfo):
    base = 1.00 * _z(_f37_growth(revenue, 126) * _sd(ncfo, revenue), 252) + 0.73 * _z(_f37_rnd_intensity(rnd, revenue) * grossmargin, 252)
    d = base - 2.0 * base.shift(63) + base.shift(126)
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_gpmocf_dzs63d_jerk_d31_v149_signal(revenue, grossmargin, gp, ncfo):
    base = 1.07 * _z(_f37_gp_growth(gp, 63) * grossmargin, 252) + 0.79 * _z(_sd(ncfo, revenue), 252)
    d = (base - 2.0 * base.shift(31) + base.shift(62)) / 961.0
    b = _z(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

def f37hg_f37_hypergrowth_signature_riqslf_dtanh252d_jerk_d93_v150_signal(revenue, grossmargin, rnd, ncfo):
    base = 1.14 * _z(_f37_rnd_intensity(rnd, revenue) * grossmargin, 252) + 0.85 * _z(_f37_growth(revenue, 504) * _sd(ncfo, revenue), 252)
    d = base.diff(93) - base.diff(93).shift(93)
    b = np.tanh(1.5 * _z(d, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f37hg_f37_hypergrowth_signature_durriq_dz252d_jerk_d63_v001_signal,
    f37hg_f37_hypergrowth_signature_r40ocf_dzs126d_jerk_d42_v002_signal,
    f37hg_f37_hypergrowth_signature_reislf_dtanh252d_jerk_d84_v003_signal,
    f37hg_f37_hypergrowth_signature_slfgpg_dsm63d_jerk_d21_v004_signal,
    f37hg_f37_hypergrowth_signature_gpmr40_dsq504d_jerk_d78_v005_signal,
    f37hg_f37_hypergrowth_signature_riqcov_dzl126d_jerk_d63_v006_signal,
    f37hg_f37_hypergrowth_signature_blnr4n_dmix252d_jerk_d21_v007_signal,
    f37hg_f37_hypergrowth_signature_gpsbln_dz63d_jerk_d42_v008_signal,
    f37hg_f37_hypergrowth_signature_covrni_dzs504d_jerk_d63_v009_signal,
    f37hg_f37_hypergrowth_signature_gpogpm_dtanh126d_jerk_d21_v010_signal,
    f37hg_f37_hypergrowth_signature_gpggms_dsm252d_jerk_d42_v011_signal,
    f37hg_f37_hypergrowth_signature_gmsrei_dsq504d_jerk_d93_v012_signal,
    f37hg_f37_hypergrowth_signature_ocfgpo_dzl126d_jerk_d63_v013_signal,
    f37hg_f37_hypergrowth_signature_rnidur_dmix63d_jerk_d31_v014_signal,
    f37hg_f37_hypergrowth_signature_cvxgps_dz252d_jerk_d93_v015_signal,
    f37hg_f37_hypergrowth_signature_r4ncvx_dzs252d_jerk_d63_v016_signal,
    f37hg_f37_hypergrowth_signature_durcov_dtanh126d_jerk_d42_v017_signal,
    f37hg_f37_hypergrowth_signature_r40r4n_dsm252d_jerk_d84_v018_signal,
    f37hg_f37_hypergrowth_signature_reibln_dsq63d_jerk_d21_v019_signal,
    f37hg_f37_hypergrowth_signature_slfrni_dzl504d_jerk_d78_v020_signal,
    f37hg_f37_hypergrowth_signature_gpmgps_dmix126d_jerk_d63_v021_signal,
    f37hg_f37_hypergrowth_signature_riqgms_dz252d_jerk_d21_v022_signal,
    f37hg_f37_hypergrowth_signature_blnrei_dzs63d_jerk_d42_v023_signal,
    f37hg_f37_hypergrowth_signature_gpsgpo_dtanh504d_jerk_d63_v024_signal,
    f37hg_f37_hypergrowth_signature_covdur_dsm126d_jerk_d21_v025_signal,
    f37hg_f37_hypergrowth_signature_gpogps_dsq252d_jerk_d42_v026_signal,
    f37hg_f37_hypergrowth_signature_gpgcvx_dzl504d_jerk_d93_v027_signal,
    f37hg_f37_hypergrowth_signature_gmsriq_dmix126d_jerk_d63_v028_signal,
    f37hg_f37_hypergrowth_signature_ocfr4n_dz63d_jerk_d31_v029_signal,
    f37hg_f37_hypergrowth_signature_rnislf_dzs252d_jerk_d93_v030_signal,
    f37hg_f37_hypergrowth_signature_cvxgpg_dtanh252d_jerk_d63_v031_signal,
    f37hg_f37_hypergrowth_signature_r4nr40_dsm126d_jerk_d42_v032_signal,
    f37hg_f37_hypergrowth_signature_durgms_dsq252d_jerk_d84_v033_signal,
    f37hg_f37_hypergrowth_signature_r40rei_dzl63d_jerk_d21_v034_signal,
    f37hg_f37_hypergrowth_signature_reigpo_dmix504d_jerk_d78_v035_signal,
    f37hg_f37_hypergrowth_signature_slfdur_dz126d_jerk_d63_v036_signal,
    f37hg_f37_hypergrowth_signature_gpmgps_dzs252d_jerk_d21_v037_signal,
    f37hg_f37_hypergrowth_signature_riqcvx_dtanh63d_jerk_d42_v038_signal,
    f37hg_f37_hypergrowth_signature_blnriq_dsm504d_jerk_d63_v039_signal,
    f37hg_f37_hypergrowth_signature_gpsocf_dsq126d_jerk_d21_v040_signal,
    f37hg_f37_hypergrowth_signature_covslf_dzl252d_jerk_d42_v041_signal,
    f37hg_f37_hypergrowth_signature_gpogpg_dmix504d_jerk_d93_v042_signal,
    f37hg_f37_hypergrowth_signature_gpgr40_dz126d_jerk_d63_v043_signal,
    f37hg_f37_hypergrowth_signature_gmscov_dzs63d_jerk_d31_v044_signal,
    f37hg_f37_hypergrowth_signature_ocfr4n_dtanh252d_jerk_d93_v045_signal,
    f37hg_f37_hypergrowth_signature_rnibln_dsm252d_jerk_d63_v046_signal,
    f37hg_f37_hypergrowth_signature_cvxrni_dsq126d_jerk_d42_v047_signal,
    f37hg_f37_hypergrowth_signature_r4ngpm_dzl252d_jerk_d84_v048_signal,
    f37hg_f37_hypergrowth_signature_durcvx_dmix63d_jerk_d21_v049_signal,
    f37hg_f37_hypergrowth_signature_r40riq_dz504d_jerk_d78_v050_signal,
    f37hg_f37_hypergrowth_signature_reiocf_dzs126d_jerk_d63_v051_signal,
    f37hg_f37_hypergrowth_signature_slfbln_dtanh252d_jerk_d21_v052_signal,
    f37hg_f37_hypergrowth_signature_gpmgpg_dsm63d_jerk_d42_v053_signal,
    f37hg_f37_hypergrowth_signature_riqr40_dsq504d_jerk_d63_v054_signal,
    f37hg_f37_hypergrowth_signature_blncov_dzl126d_jerk_d21_v055_signal,
    f37hg_f37_hypergrowth_signature_gpsr4n_dmix252d_jerk_d42_v056_signal,
    f37hg_f37_hypergrowth_signature_covbln_dz504d_jerk_d93_v057_signal,
    f37hg_f37_hypergrowth_signature_gporni_dzs126d_jerk_d63_v058_signal,
    f37hg_f37_hypergrowth_signature_gpggpm_dtanh63d_jerk_d31_v059_signal,
    f37hg_f37_hypergrowth_signature_gmscvx_dsm252d_jerk_d93_v060_signal,
    f37hg_f37_hypergrowth_signature_ocfrei_dsq252d_jerk_d63_v061_signal,
    f37hg_f37_hypergrowth_signature_rnigpo_dzl126d_jerk_d42_v062_signal,
    f37hg_f37_hypergrowth_signature_cvxdur_dmix252d_jerk_d84_v063_signal,
    f37hg_f37_hypergrowth_signature_r4ngps_dz63d_jerk_d21_v064_signal,
    f37hg_f37_hypergrowth_signature_durr40_dzs504d_jerk_d78_v065_signal,
    f37hg_f37_hypergrowth_signature_r40cov_dtanh126d_jerk_d63_v066_signal,
    f37hg_f37_hypergrowth_signature_reir4n_dsm252d_jerk_d21_v067_signal,
    f37hg_f37_hypergrowth_signature_slfbln_dsq63d_jerk_d42_v068_signal,
    f37hg_f37_hypergrowth_signature_gpmrni_dzl504d_jerk_d63_v069_signal,
    f37hg_f37_hypergrowth_signature_riqgpm_dmix126d_jerk_d21_v070_signal,
    f37hg_f37_hypergrowth_signature_blngms_dz252d_jerk_d42_v071_signal,
    f37hg_f37_hypergrowth_signature_gpsrei_dzs504d_jerk_d93_v072_signal,
    f37hg_f37_hypergrowth_signature_covgpo_dtanh126d_jerk_d63_v073_signal,
    f37hg_f37_hypergrowth_signature_gpodur_dsm63d_jerk_d31_v074_signal,
    f37hg_f37_hypergrowth_signature_gpggps_dsq252d_jerk_d93_v075_signal,
    f37hg_f37_hypergrowth_signature_gmscvx_dzl252d_jerk_d63_v076_signal,
    f37hg_f37_hypergrowth_signature_ocfriq_dmix126d_jerk_d42_v077_signal,
    f37hg_f37_hypergrowth_signature_rniocf_dz252d_jerk_d84_v078_signal,
    f37hg_f37_hypergrowth_signature_cvxslf_dzs63d_jerk_d21_v079_signal,
    f37hg_f37_hypergrowth_signature_r4ngpg_dtanh504d_jerk_d78_v080_signal,
    f37hg_f37_hypergrowth_signature_durgpm_dsm126d_jerk_d63_v081_signal,
    f37hg_f37_hypergrowth_signature_r40gms_dsq252d_jerk_d21_v082_signal,
    f37hg_f37_hypergrowth_signature_reiriq_dzl63d_jerk_d42_v083_signal,
    f37hg_f37_hypergrowth_signature_slfgpo_dmix504d_jerk_d63_v084_signal,
    f37hg_f37_hypergrowth_signature_gpmdur_dz126d_jerk_d21_v085_signal,
    f37hg_f37_hypergrowth_signature_riqgps_dzs252d_jerk_d42_v086_signal,
    f37hg_f37_hypergrowth_signature_blncvx_dtanh504d_jerk_d93_v087_signal,
    f37hg_f37_hypergrowth_signature_gpsriq_dsm126d_jerk_d63_v088_signal,
    f37hg_f37_hypergrowth_signature_covocf_dsq63d_jerk_d31_v089_signal,
    f37hg_f37_hypergrowth_signature_gposlf_dzl252d_jerk_d93_v090_signal,
    f37hg_f37_hypergrowth_signature_gpgrni_dmix252d_jerk_d63_v091_signal,
    f37hg_f37_hypergrowth_signature_gmsr40_dz126d_jerk_d42_v092_signal,
    f37hg_f37_hypergrowth_signature_ocfcov_dzs252d_jerk_d84_v093_signal,
    f37hg_f37_hypergrowth_signature_rnir4n_dtanh63d_jerk_d21_v094_signal,
    f37hg_f37_hypergrowth_signature_cvxbln_dsm504d_jerk_d78_v095_signal,
    f37hg_f37_hypergrowth_signature_r4nrni_dsq126d_jerk_d63_v096_signal,
    f37hg_f37_hypergrowth_signature_durgps_dzl252d_jerk_d21_v097_signal,
    f37hg_f37_hypergrowth_signature_r40cvx_dmix63d_jerk_d42_v098_signal,
    f37hg_f37_hypergrowth_signature_reiriq_dz504d_jerk_d63_v099_signal,
    f37hg_f37_hypergrowth_signature_slfocf_dzs126d_jerk_d21_v100_signal,
    f37hg_f37_hypergrowth_signature_gpmslf_dtanh252d_jerk_d42_v101_signal,
    f37hg_f37_hypergrowth_signature_riqgpg_dsm504d_jerk_d93_v102_signal,
    f37hg_f37_hypergrowth_signature_blnr40_dsq126d_jerk_d63_v103_signal,
    f37hg_f37_hypergrowth_signature_gpscov_dzl63d_jerk_d31_v104_signal,
    f37hg_f37_hypergrowth_signature_covr4n_dmix252d_jerk_d93_v105_signal,
    f37hg_f37_hypergrowth_signature_gpobln_dz252d_jerk_d63_v106_signal,
    f37hg_f37_hypergrowth_signature_gpgrni_dzs126d_jerk_d42_v107_signal,
    f37hg_f37_hypergrowth_signature_gmsgpm_dtanh252d_jerk_d84_v108_signal,
    f37hg_f37_hypergrowth_signature_ocfgms_dsm63d_jerk_d21_v109_signal,
    f37hg_f37_hypergrowth_signature_rnirei_dsq504d_jerk_d78_v110_signal,
    f37hg_f37_hypergrowth_signature_cvxgpo_dzl126d_jerk_d63_v111_signal,
    f37hg_f37_hypergrowth_signature_r4ndur_dmix252d_jerk_d21_v112_signal,
    f37hg_f37_hypergrowth_signature_durgpg_dz63d_jerk_d42_v113_signal,
    f37hg_f37_hypergrowth_signature_r40gpm_dzs504d_jerk_d63_v114_signal,
    f37hg_f37_hypergrowth_signature_reicov_dtanh126d_jerk_d21_v115_signal,
    f37hg_f37_hypergrowth_signature_slfr4n_dsm252d_jerk_d42_v116_signal,
    f37hg_f37_hypergrowth_signature_gpmbln_dsq504d_jerk_d93_v117_signal,
    f37hg_f37_hypergrowth_signature_riqrni_dzl126d_jerk_d63_v118_signal,
    f37hg_f37_hypergrowth_signature_blngpm_dmix63d_jerk_d31_v119_signal,
    f37hg_f37_hypergrowth_signature_gpsgms_dz252d_jerk_d93_v120_signal,
    f37hg_f37_hypergrowth_signature_covrei_dzs252d_jerk_d63_v121_signal,
    f37hg_f37_hypergrowth_signature_gpoocf_dtanh126d_jerk_d42_v122_signal,
    f37hg_f37_hypergrowth_signature_gpgdur_dsm252d_jerk_d84_v123_signal,
    f37hg_f37_hypergrowth_signature_gmsgps_dsq63d_jerk_d21_v124_signal,
    f37hg_f37_hypergrowth_signature_ocfcvx_dzl504d_jerk_d78_v125_signal,
    f37hg_f37_hypergrowth_signature_rniriq_dmix126d_jerk_d63_v126_signal,
    f37hg_f37_hypergrowth_signature_cvxocf_dz252d_jerk_d21_v127_signal,
    f37hg_f37_hypergrowth_signature_r4nslf_dzs63d_jerk_d42_v128_signal,
    f37hg_f37_hypergrowth_signature_durrni_dtanh504d_jerk_d63_v129_signal,
    f37hg_f37_hypergrowth_signature_r40gpm_dsm126d_jerk_d21_v130_signal,
    f37hg_f37_hypergrowth_signature_reigms_dsq252d_jerk_d42_v131_signal,
    f37hg_f37_hypergrowth_signature_slfrei_dzl504d_jerk_d93_v132_signal,
    f37hg_f37_hypergrowth_signature_gpmgpo_dmix126d_jerk_d63_v133_signal,
    f37hg_f37_hypergrowth_signature_riqdur_dz63d_jerk_d31_v134_signal,
    f37hg_f37_hypergrowth_signature_blngps_dzs252d_jerk_d93_v135_signal,
    f37hg_f37_hypergrowth_signature_gpscvx_dtanh252d_jerk_d63_v136_signal,
    f37hg_f37_hypergrowth_signature_covriq_dsm126d_jerk_d42_v137_signal,
    f37hg_f37_hypergrowth_signature_gpoocf_dsq252d_jerk_d84_v138_signal,
    f37hg_f37_hypergrowth_signature_gpgslf_dzl63d_jerk_d21_v139_signal,
    f37hg_f37_hypergrowth_signature_gmsgpg_dmix504d_jerk_d78_v140_signal,
    f37hg_f37_hypergrowth_signature_ocfr40_dz126d_jerk_d63_v141_signal,
    f37hg_f37_hypergrowth_signature_rnicov_dzs252d_jerk_d21_v142_signal,
    f37hg_f37_hypergrowth_signature_cvxr4n_dtanh63d_jerk_d42_v143_signal,
    f37hg_f37_hypergrowth_signature_r4nbln_dsm504d_jerk_d63_v144_signal,
    f37hg_f37_hypergrowth_signature_durslf_dsq126d_jerk_d21_v145_signal,
    f37hg_f37_hypergrowth_signature_r40gps_dzl252d_jerk_d42_v146_signal,
    f37hg_f37_hypergrowth_signature_reicvx_dmix504d_jerk_d93_v147_signal,
    f37hg_f37_hypergrowth_signature_slfriq_dz126d_jerk_d63_v148_signal,
    f37hg_f37_hypergrowth_signature_gpmocf_dzs63d_jerk_d31_v149_signal,
    f37hg_f37_hypergrowth_signature_riqslf_dtanh252d_jerk_d93_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F37_HYPERGROWTH_SIGNATURE_REGISTRY_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    ALLOW = {
        "open", "high", "low", "close", "closeadj", "volume",
        "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc", "opex",
        "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc",
        "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff", "ncfi",
        "ncfcommon", "ncfdebt", "ncfbus", "capex", "depamor", "sharesbas", "shareswa",
        "shareswadil", "assets", "assetsc", "tangibles", "intangibles", "ppnenet",
        "investments", "inventory", "receivables", "payables", "equity", "retearn",
        "workingcapital", "debt", "debtc", "debtnc", "liabilities", "liabilitiesc",
        "cashneq", "currentratio", "roic", "roe", "roa", "ros", "assetturnover", "invcap",
        "intexp", "taxexp", "ebt", "sps", "bvps", "de", "ncfdiv", "dps", "divyield",
        "payoutratio", "prefdivis", "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
        "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal", "fndholders",
        "undholders", "prfholders", "dbtholders", "putholders", "putvalue", "cllholders",
        "cllvalue", "wntholders", "wntvalue", "dbtvalue",
    }

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    revenue = _fund(101, base=1.0e8, drift=0.05, vol=0.06).rename("revenue")
    gp = _fund(102, base=0.55e8, drift=0.05, vol=0.09).rename("gp")
    rnd = _fund(103, base=0.18e8, drift=0.04, vol=0.11).rename("rnd")
    grossmargin = (0.42 + 0.12 * _fund(104, base=1.0, drift=0.0, vol=0.18)).rename("grossmargin")
    ncfo = _fund(105, base=0.12e8, drift=0.02, vol=0.16, allow_neg=True).rename("ncfo")

    cols = {"revenue": revenue, "gp": gp, "rnd": rnd,
            "grossmargin": grossmargin, "ncfo": ncfo}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs %s" % (name, meta["inputs"])
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

    print("OK f37_hypergrowth_signature_3rd_derivatives_001_150_claude: %d features pass" % n_features)
