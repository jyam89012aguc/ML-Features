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


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _dollar_vol(closeadj, volume):
    return (closeadj * volume).replace(0, np.nan)


def _amihud(closeadj, volume, w):
    ret = closeadj.pct_change().abs()
    dv = (closeadj * volume).replace(0, np.nan)
    return (ret / dv).rolling(w, min_periods=max(2, w // 2)).mean()


def _turnover(volume, w):
    typ = volume.rolling(w, min_periods=max(2, w // 2)).median()
    return volume / typ.replace(0, np.nan)


def _corwin_schultz(high, low, w):
    hl = (np.log(high.replace(0, np.nan) / low.replace(0, np.nan))) ** 2
    beta = hl + hl.shift(1)
    h2 = pd.concat([high, high.shift(1)], axis=1).max(axis=1)
    l2 = pd.concat([low, low.shift(1)], axis=1).min(axis=1)
    gamma = (np.log(h2.replace(0, np.nan) / l2.replace(0, np.nan))) ** 2
    den = 3.0 - 2.0 * np.sqrt(2.0)
    alpha = (np.sqrt(2.0 * beta) - np.sqrt(beta)) / den - np.sqrt(gamma / den)
    spread = 2.0 * (np.exp(alpha) - 1.0) / (1.0 + np.exp(alpha))
    return spread.clip(lower=0).rolling(w, min_periods=max(2, w // 2)).mean()


def _kyle(closeadj, volume, w):
    ret = closeadj.pct_change()
    dv = (closeadj * volume).replace(0, np.nan)
    signed_dv = np.sign(ret) * np.sqrt(dv)
    cov = ret.rolling(w, min_periods=max(2, w // 2)).cov(signed_dv)
    var = signed_dv.rolling(w, min_periods=max(2, w // 2)).var()
    return cov / var.replace(0, np.nan)


def f16lq_f16_liquidity_illiquidity_profile_amihud21r21_21d_slope_v001_signal(closeadj, volume):
    base = np.log(_amihud(closeadj, volume, 21).replace(0, np.nan) * 1e12 + 1.0)
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_amihud21r63_63d_slope_v002_signal(closeadj, volume):
    base = np.log(_amihud(closeadj, volume, 21).replace(0, np.nan) * 1e12 + 1.0)
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_amihud21r5_5d_slope_v003_signal(closeadj, volume):
    base = np.log(_amihud(closeadj, volume, 21).replace(0, np.nan) * 1e12 + 1.0)
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_amihud63r21_21d_slope_v004_signal(closeadj, volume):
    base = np.log(_amihud(closeadj, volume, 63).replace(0, np.nan) * 1e12 + 1.0)
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_amihud63r63_63d_slope_v005_signal(closeadj, volume):
    base = np.log(_amihud(closeadj, volume, 63).replace(0, np.nan) * 1e12 + 1.0)
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_amihud63r5_5d_slope_v006_signal(closeadj, volume):
    base = np.log(_amihud(closeadj, volume, 63).replace(0, np.nan) * 1e12 + 1.0)
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_amihud126r21_21d_slope_v007_signal(closeadj, volume):
    base = np.log(_amihud(closeadj, volume, 126).replace(0, np.nan) * 1e12 + 1.0)
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_amihud126r63_63d_slope_v008_signal(closeadj, volume):
    base = np.log(_amihud(closeadj, volume, 126).replace(0, np.nan) * 1e12 + 1.0)
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_amihud126r5_5d_slope_v009_signal(closeadj, volume):
    base = np.log(_amihud(closeadj, volume, 126).replace(0, np.nan) * 1e12 + 1.0)
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_amihudtermr21_21d_slope_v010_signal(closeadj, volume):
    s = _amihud(closeadj, volume, 63)
    l = _amihud(closeadj, volume, 252)
    base = np.log(s.replace(0, np.nan) / l.replace(0, np.nan))
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_amihudtermr63_63d_slope_v011_signal(closeadj, volume):
    s = _amihud(closeadj, volume, 63)
    l = _amihud(closeadj, volume, 252)
    base = np.log(s.replace(0, np.nan) / l.replace(0, np.nan))
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_amihudtermr5_5d_slope_v012_signal(closeadj, volume):
    s = _amihud(closeadj, volume, 63)
    l = _amihud(closeadj, volume, 252)
    base = np.log(s.replace(0, np.nan) / l.replace(0, np.nan))
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_amihud5dr21_21d_slope_v013_signal(closeadj, volume):
    ret5 = (closeadj / closeadj.shift(5) - 1.0).abs()
    dv5 = (closeadj * volume).replace(0, np.nan).rolling(5).sum()
    illiq = (ret5 / dv5).rolling(63, min_periods=21).mean()
    base = np.log(illiq.replace(0, np.nan) * 1e12 + 1.0)
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_amihud5dr63_63d_slope_v014_signal(closeadj, volume):
    ret5 = (closeadj / closeadj.shift(5) - 1.0).abs()
    dv5 = (closeadj * volume).replace(0, np.nan).rolling(5).sum()
    illiq = (ret5 / dv5).rolling(63, min_periods=21).mean()
    base = np.log(illiq.replace(0, np.nan) * 1e12 + 1.0)
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_amihud5dr5_5d_slope_v015_signal(closeadj, volume):
    ret5 = (closeadj / closeadj.shift(5) - 1.0).abs()
    dv5 = (closeadj * volume).replace(0, np.nan).rolling(5).sum()
    illiq = (ret5 / dv5).rolling(63, min_periods=21).mean()
    base = np.log(illiq.replace(0, np.nan) * 1e12 + 1.0)
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_amihudrankr21_21d_slope_v016_signal(closeadj, volume):
    base = _rank(_amihud(closeadj, volume, 63), 252)
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_amihudrankr63_63d_slope_v017_signal(closeadj, volume):
    base = _rank(_amihud(closeadj, volume, 63), 252)
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_amihudrankr5_5d_slope_v018_signal(closeadj, volume):
    base = _rank(_amihud(closeadj, volume, 63), 252)
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_turnover63r21_21d_slope_v019_signal(volume):
    base = np.log(_turnover(volume, 63).replace(0, np.nan))
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_turnover63r63_63d_slope_v020_signal(volume):
    base = np.log(_turnover(volume, 63).replace(0, np.nan))
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_turnover63r5_5d_slope_v021_signal(volume):
    base = np.log(_turnover(volume, 63).replace(0, np.nan))
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_turndispr21_21d_slope_v022_signal(volume):
    lt = np.log(_turnover(volume, 63).replace(0, np.nan))
    base = _std(lt, 63)
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_turndispr63_63d_slope_v023_signal(volume):
    lt = np.log(_turnover(volume, 63).replace(0, np.nan))
    base = _std(lt, 63)
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_turndispr5_5d_slope_v024_signal(volume):
    lt = np.log(_turnover(volume, 63).replace(0, np.nan))
    base = _std(lt, 63)
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_turnskewr21_21d_slope_v025_signal(volume):
    lt = np.log(_turnover(volume, 63).replace(0, np.nan))
    base = lt.rolling(126, min_periods=63).skew()
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_turnskewr63_63d_slope_v026_signal(volume):
    lt = np.log(_turnover(volume, 63).replace(0, np.nan))
    base = lt.rolling(126, min_periods=63).skew()
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_turnskewr5_5d_slope_v027_signal(volume):
    lt = np.log(_turnover(volume, 63).replace(0, np.nan))
    base = lt.rolling(126, min_periods=63).skew()
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_turnoverrankr21_21d_slope_v028_signal(volume):
    base = _rank(_turnover(volume, 63), 252)
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_turnoverrankr63_63d_slope_v029_signal(volume):
    base = _rank(_turnover(volume, 63), 252)
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_turnoverrankr5_5d_slope_v030_signal(volume):
    base = _rank(_turnover(volume, 63), 252)
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_csspread21r21_21d_slope_v031_signal(high, low):
    base = _corwin_schultz(high, low, 21)
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_csspread21r63_63d_slope_v032_signal(high, low):
    base = _corwin_schultz(high, low, 21)
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_csspread21r5_5d_slope_v033_signal(high, low):
    base = _corwin_schultz(high, low, 21)
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_csspread63r21_21d_slope_v034_signal(high, low):
    base = _corwin_schultz(high, low, 63)
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_csspread63r63_63d_slope_v035_signal(high, low):
    base = _corwin_schultz(high, low, 63)
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_csspread63r5_5d_slope_v036_signal(high, low):
    base = _corwin_schultz(high, low, 63)
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_csspread126r21_21d_slope_v037_signal(high, low):
    base = _corwin_schultz(high, low, 126)
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_csspread126r63_63d_slope_v038_signal(high, low):
    base = _corwin_schultz(high, low, 126)
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_csspread126r5_5d_slope_v039_signal(high, low):
    base = _corwin_schultz(high, low, 126)
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_csdispr21_21d_slope_v040_signal(high, low):
    cs2 = _corwin_schultz(high, low, 2)
    base = _std(cs2, 126)
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_csdispr63_63d_slope_v041_signal(high, low):
    cs2 = _corwin_schultz(high, low, 2)
    base = _std(cs2, 126)
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_csdispr5_5d_slope_v042_signal(high, low):
    cs2 = _corwin_schultz(high, low, 2)
    base = _std(cs2, 126)
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_cscurvr21_21d_slope_v043_signal(high, low):
    c21 = _corwin_schultz(high, low, 21)
    c63 = _corwin_schultz(high, low, 63)
    c126 = _corwin_schultz(high, low, 126)
    base = c63 - 0.5 * (c21 + c126)
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_cscurvr63_63d_slope_v044_signal(high, low):
    c21 = _corwin_schultz(high, low, 21)
    c63 = _corwin_schultz(high, low, 63)
    c126 = _corwin_schultz(high, low, 126)
    base = c63 - 0.5 * (c21 + c126)
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_cscurvr5_5d_slope_v045_signal(high, low):
    c21 = _corwin_schultz(high, low, 21)
    c63 = _corwin_schultz(high, low, 63)
    c126 = _corwin_schultz(high, low, 126)
    base = c63 - 0.5 * (c21 + c126)
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_dvlevelr21_21d_slope_v046_signal(closeadj, volume):
    base = np.log(_dollar_vol(closeadj, volume)).rolling(63, min_periods=21).mean()
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_dvlevelr63_63d_slope_v047_signal(closeadj, volume):
    base = np.log(_dollar_vol(closeadj, volume)).rolling(63, min_periods=21).mean()
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_dvlevelr5_5d_slope_v048_signal(closeadj, volume):
    base = np.log(_dollar_vol(closeadj, volume)).rolling(63, min_periods=21).mean()
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_dvgapr21_21d_slope_v049_signal(closeadj, volume):
    dv = np.log(_dollar_vol(closeadj, volume))
    base = dv.rolling(21, min_periods=10).mean() - dv.rolling(252, min_periods=126).mean()
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_dvgapr63_63d_slope_v050_signal(closeadj, volume):
    dv = np.log(_dollar_vol(closeadj, volume))
    base = dv.rolling(21, min_periods=10).mean() - dv.rolling(252, min_periods=126).mean()
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_dvgapr5_5d_slope_v051_signal(closeadj, volume):
    dv = np.log(_dollar_vol(closeadj, volume))
    base = dv.rolling(21, min_periods=10).mean() - dv.rolling(252, min_periods=126).mean()
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_dvdrawdownr21_21d_slope_v052_signal(closeadj, volume):
    dv = _dollar_vol(closeadj, volume).rolling(21, min_periods=10).mean()
    peak = dv.rolling(252, min_periods=126).max()
    base = np.log(dv.replace(0, np.nan) / peak.replace(0, np.nan))
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_dvdrawdownr63_63d_slope_v053_signal(closeadj, volume):
    dv = _dollar_vol(closeadj, volume).rolling(21, min_periods=10).mean()
    peak = dv.rolling(252, min_periods=126).max()
    base = np.log(dv.replace(0, np.nan) / peak.replace(0, np.nan))
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_dvdrawdownr5_5d_slope_v054_signal(closeadj, volume):
    dv = _dollar_vol(closeadj, volume).rolling(21, min_periods=10).mean()
    peak = dv.rolling(252, min_periods=126).max()
    base = np.log(dv.replace(0, np.nan) / peak.replace(0, np.nan))
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_dvrankr21_21d_slope_v055_signal(closeadj, volume):
    dv = np.log(_dollar_vol(closeadj, volume)).rolling(21, min_periods=10).mean()
    base = _rank(dv, 504)
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_dvrankr63_63d_slope_v056_signal(closeadj, volume):
    dv = np.log(_dollar_vol(closeadj, volume)).rolling(21, min_periods=10).mean()
    base = _rank(dv, 504)
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_dvrankr5_5d_slope_v057_signal(closeadj, volume):
    dv = np.log(_dollar_vol(closeadj, volume)).rolling(21, min_periods=10).mean()
    base = _rank(dv, 504)
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_amivestr21_21d_slope_v058_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    dv = _dollar_vol(closeadj, volume)
    num = dv.rolling(63, min_periods=21).sum()
    den = ret.rolling(63, min_periods=21).sum().replace(0, np.nan)
    base = _z(np.log((num / den).replace(0, np.nan)), 252)
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_amivestr63_63d_slope_v059_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    dv = _dollar_vol(closeadj, volume)
    num = dv.rolling(63, min_periods=21).sum()
    den = ret.rolling(63, min_periods=21).sum().replace(0, np.nan)
    base = _z(np.log((num / den).replace(0, np.nan)), 252)
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_amivestr5_5d_slope_v060_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    dv = _dollar_vol(closeadj, volume)
    num = dv.rolling(63, min_periods=21).sum()
    den = ret.rolling(63, min_periods=21).sum().replace(0, np.nan)
    base = _z(np.log((num / den).replace(0, np.nan)), 252)
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_rollspreadr21_21d_slope_v061_signal(closeadj):
    ret = closeadj.pct_change()
    cov = ret.rolling(63, min_periods=21).cov(ret.shift(1))
    base = 2.0 * np.sqrt((-cov).clip(lower=0))
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_rollspreadr63_63d_slope_v062_signal(closeadj):
    ret = closeadj.pct_change()
    cov = ret.rolling(63, min_periods=21).cov(ret.shift(1))
    base = 2.0 * np.sqrt((-cov).clip(lower=0))
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_rollspreadr5_5d_slope_v063_signal(closeadj):
    ret = closeadj.pct_change()
    cov = ret.rolling(63, min_periods=21).cov(ret.shift(1))
    base = 2.0 * np.sqrt((-cov).clip(lower=0))
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_rollspread126r21_21d_slope_v064_signal(closeadj):
    ret = closeadj.pct_change()
    cov = ret.rolling(126, min_periods=63).cov(ret.shift(1))
    base = 2.0 * np.sqrt((-cov).clip(lower=0))
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_rollspread126r63_63d_slope_v065_signal(closeadj):
    ret = closeadj.pct_change()
    cov = ret.rolling(126, min_periods=63).cov(ret.shift(1))
    base = 2.0 * np.sqrt((-cov).clip(lower=0))
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_rollspread126r5_5d_slope_v066_signal(closeadj):
    ret = closeadj.pct_change()
    cov = ret.rolling(126, min_periods=63).cov(ret.shift(1))
    base = 2.0 * np.sqrt((-cov).clip(lower=0))
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_retac1r21_21d_slope_v067_signal(closeadj):
    ret = closeadj.pct_change()
    base = ret.rolling(63, min_periods=21).corr(ret.shift(1))
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_retac1r63_63d_slope_v068_signal(closeadj):
    ret = closeadj.pct_change()
    base = ret.rolling(63, min_periods=21).corr(ret.shift(1))
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_retac1r5_5d_slope_v069_signal(closeadj):
    ret = closeadj.pct_change()
    base = ret.rolling(63, min_periods=21).corr(ret.shift(1))
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_varratior21_21d_slope_v070_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    v1 = lr.rolling(126, min_periods=63).var()
    v5 = lr.rolling(5).sum().rolling(126, min_periods=63).var()
    base = v5 / (5.0 * v1).replace(0, np.nan) - 1.0
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_varratior63_63d_slope_v071_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    v1 = lr.rolling(126, min_periods=63).var()
    v5 = lr.rolling(5).sum().rolling(126, min_periods=63).var()
    base = v5 / (5.0 * v1).replace(0, np.nan) - 1.0
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_varratior5_5d_slope_v072_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    v1 = lr.rolling(126, min_periods=63).var()
    v5 = lr.rolling(5).sum().rolling(126, min_periods=63).var()
    base = v5 / (5.0 * v1).replace(0, np.nan) - 1.0
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_kyle63r21_21d_slope_v073_signal(closeadj, volume):
    base = np.log(_kyle(closeadj, volume, 63).abs().replace(0, np.nan) * 1e6 + 1.0)
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_kyle63r63_63d_slope_v074_signal(closeadj, volume):
    base = np.log(_kyle(closeadj, volume, 63).abs().replace(0, np.nan) * 1e6 + 1.0)
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_kyle63r5_5d_slope_v075_signal(closeadj, volume):
    base = np.log(_kyle(closeadj, volume, 63).abs().replace(0, np.nan) * 1e6 + 1.0)
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_kylerankr21_21d_slope_v076_signal(closeadj, volume):
    base = _rank(_kyle(closeadj, volume, 63).abs(), 252)
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_kylerankr63_63d_slope_v077_signal(closeadj, volume):
    base = _rank(_kyle(closeadj, volume, 63).abs(), 252)
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_kylerankr5_5d_slope_v078_signal(closeadj, volume):
    base = _rank(_kyle(closeadj, volume, 63).abs(), 252)
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_volcvr21_21d_slope_v079_signal(volume):
    m = _mean(volume, 63)
    sd = _std(volume, 63)
    base = sd / m.replace(0, np.nan)
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_volcvr63_63d_slope_v080_signal(volume):
    m = _mean(volume, 63)
    sd = _std(volume, 63)
    base = sd / m.replace(0, np.nan)
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_volcvr5_5d_slope_v081_signal(volume):
    m = _mean(volume, 63)
    sd = _std(volume, 63)
    base = sd / m.replace(0, np.nan)
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_volherfr21_21d_slope_v082_signal(volume):
    s = volume.rolling(21, min_periods=10).sum()
    share = volume / s.replace(0, np.nan)
    base = (share ** 2).rolling(21, min_periods=10).sum()
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_volherfr63_63d_slope_v083_signal(volume):
    s = volume.rolling(21, min_periods=10).sum()
    share = volume / s.replace(0, np.nan)
    base = (share ** 2).rolling(21, min_periods=10).sum()
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_volherfr5_5d_slope_v084_signal(volume):
    s = volume.rolling(21, min_periods=10).sum()
    share = volume / s.replace(0, np.nan)
    base = (share ** 2).rolling(21, min_periods=10).sum()
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_dvherfr21_21d_slope_v085_signal(closeadj, volume):
    dv = _dollar_vol(closeadj, volume)
    s = dv.rolling(63, min_periods=21).sum()
    share = dv / s.replace(0, np.nan)
    base = (share ** 2).rolling(63, min_periods=21).sum()
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_dvherfr63_63d_slope_v086_signal(closeadj, volume):
    dv = _dollar_vol(closeadj, volume)
    s = dv.rolling(63, min_periods=21).sum()
    share = dv / s.replace(0, np.nan)
    base = (share ** 2).rolling(63, min_periods=21).sum()
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_dvherfr5_5d_slope_v087_signal(closeadj, volume):
    dv = _dollar_vol(closeadj, volume)
    s = dv.rolling(63, min_periods=21).sum()
    share = dv / s.replace(0, np.nan)
    base = (share ** 2).rolling(63, min_periods=21).sum()
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_volentropyr21_21d_slope_v088_signal(volume):
    s = volume.rolling(21, min_periods=10).sum()
    p = volume / s.replace(0, np.nan)
    base = (-(p * np.log(p.replace(0, np.nan)))).rolling(21, min_periods=10).sum()
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_volentropyr63_63d_slope_v089_signal(volume):
    s = volume.rolling(21, min_periods=10).sum()
    p = volume / s.replace(0, np.nan)
    base = (-(p * np.log(p.replace(0, np.nan)))).rolling(21, min_periods=10).sum()
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_volentropyr5_5d_slope_v090_signal(volume):
    s = volume.rolling(21, min_periods=10).sum()
    p = volume / s.replace(0, np.nan)
    base = (-(p * np.log(p.replace(0, np.nan)))).rolling(21, min_periods=10).sum()
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_logvoldispr21_21d_slope_v091_signal(volume):
    base = _std(np.log(volume.replace(0, np.nan)), 126)
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_logvoldispr63_63d_slope_v092_signal(volume):
    base = _std(np.log(volume.replace(0, np.nan)), 126)
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_logvoldispr5_5d_slope_v093_signal(volume):
    base = _std(np.log(volume.replace(0, np.nan)), 126)
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_illiqofilliqr21_21d_slope_v094_signal(closeadj, volume):
    lg = np.log(_amihud(closeadj, volume, 21).replace(0, np.nan) * 1e12 + 1.0)
    base = _std(lg, 126)
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_illiqofilliqr63_63d_slope_v095_signal(closeadj, volume):
    lg = np.log(_amihud(closeadj, volume, 21).replace(0, np.nan) * 1e12 + 1.0)
    base = _std(lg, 126)
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_illiqofilliqr5_5d_slope_v096_signal(closeadj, volume):
    lg = np.log(_amihud(closeadj, volume, 21).replace(0, np.nan) * 1e12 + 1.0)
    base = _std(lg, 126)
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_retperturnr21_21d_slope_v097_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    t = _turnover(volume, 63)
    impact = ret / t.replace(0, np.nan)
    base = np.log(impact.rolling(63, min_periods=21).mean().replace(0, np.nan) * 1e4 + 1.0)
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_retperturnr63_63d_slope_v098_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    t = _turnover(volume, 63)
    impact = ret / t.replace(0, np.nan)
    base = np.log(impact.rolling(63, min_periods=21).mean().replace(0, np.nan) * 1e4 + 1.0)
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_retperturnr5_5d_slope_v099_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    t = _turnover(volume, 63)
    impact = ret / t.replace(0, np.nan)
    base = np.log(impact.rolling(63, min_periods=21).mean().replace(0, np.nan) * 1e4 + 1.0)
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_rangedvr21_21d_slope_v100_signal(closeadj, high, low, volume):
    rng = (high - low) / closeadj.replace(0, np.nan)
    dv = _dollar_vol(closeadj, volume)
    illiq = (rng / dv).rolling(63, min_periods=21).mean()
    base = _z(np.log(illiq.replace(0, np.nan) * 1e12 + 1.0), 252)
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_rangedvr63_63d_slope_v101_signal(closeadj, high, low, volume):
    rng = (high - low) / closeadj.replace(0, np.nan)
    dv = _dollar_vol(closeadj, volume)
    illiq = (rng / dv).rolling(63, min_periods=21).mean()
    base = _z(np.log(illiq.replace(0, np.nan) * 1e12 + 1.0), 252)
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_rangedvr5_5d_slope_v102_signal(closeadj, high, low, volume):
    rng = (high - low) / closeadj.replace(0, np.nan)
    dv = _dollar_vol(closeadj, volume)
    illiq = (rng / dv).rolling(63, min_periods=21).mean()
    base = _z(np.log(illiq.replace(0, np.nan) * 1e12 + 1.0), 252)
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_hlspreadr21_21d_slope_v103_signal(high, low):
    sp = 2.0 * (high - low) / (high + low).replace(0, np.nan)
    base = sp.rolling(21, min_periods=10).mean()
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_hlspreadr63_63d_slope_v104_signal(high, low):
    sp = 2.0 * (high - low) / (high + low).replace(0, np.nan)
    base = sp.rolling(21, min_periods=10).mean()
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_hlspreadr5_5d_slope_v105_signal(high, low):
    sp = 2.0 * (high - low) / (high + low).replace(0, np.nan)
    base = sp.rolling(21, min_periods=10).mean()
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_closepinr21_21d_slope_v106_signal(close, high, low):
    mid = (high + low) / 2.0
    pin = (close - mid).abs() / (high - low).replace(0, np.nan)
    base = pin.rolling(21, min_periods=10).mean()
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_closepinr63_63d_slope_v107_signal(close, high, low):
    mid = (high + low) / 2.0
    pin = (close - mid).abs() / (high - low).replace(0, np.nan)
    base = pin.rolling(21, min_periods=10).mean()
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_closepinr5_5d_slope_v108_signal(close, high, low):
    mid = (high + low) / 2.0
    pin = (close - mid).abs() / (high - low).replace(0, np.nan)
    base = pin.rolling(21, min_periods=10).mean()
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_amihudfloorr21_21d_slope_v109_signal(closeadj, volume):
    illiq = _amihud(closeadj, volume, 63)
    lo = illiq.rolling(252, min_periods=126).min()
    base = np.log(illiq.replace(0, np.nan) / lo.replace(0, np.nan))
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_amihudfloorr63_63d_slope_v110_signal(closeadj, volume):
    illiq = _amihud(closeadj, volume, 63)
    lo = illiq.rolling(252, min_periods=126).min()
    base = np.log(illiq.replace(0, np.nan) / lo.replace(0, np.nan))
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_amihudfloorr5_5d_slope_v111_signal(closeadj, volume):
    illiq = _amihud(closeadj, volume, 63)
    lo = illiq.rolling(252, min_periods=126).min()
    base = np.log(illiq.replace(0, np.nan) / lo.replace(0, np.nan))
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_spreadpervolr21_21d_slope_v112_signal(closeadj, high, low):
    cs = _corwin_schultz(high, low, 63)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    base = cs / vol.replace(0, np.nan)
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_spreadpervolr63_63d_slope_v113_signal(closeadj, high, low):
    cs = _corwin_schultz(high, low, 63)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    base = cs / vol.replace(0, np.nan)
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_spreadpervolr5_5d_slope_v114_signal(closeadj, high, low):
    cs = _corwin_schultz(high, low, 63)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    base = cs / vol.replace(0, np.nan)
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_costcompoundr21_21d_slope_v115_signal(closeadj, high, low, volume):
    cs = _corwin_schultz(high, low, 63)
    lg = np.log(_amihud(closeadj, volume, 63).replace(0, np.nan) * 1e12 + 1.0)
    base = cs * lg
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_costcompoundr63_63d_slope_v116_signal(closeadj, high, low, volume):
    cs = _corwin_schultz(high, low, 63)
    lg = np.log(_amihud(closeadj, volume, 63).replace(0, np.nan) * 1e12 + 1.0)
    base = cs * lg
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_costcompoundr5_5d_slope_v117_signal(closeadj, high, low, volume):
    cs = _corwin_schultz(high, low, 63)
    lg = np.log(_amihud(closeadj, volume, 63).replace(0, np.nan) * 1e12 + 1.0)
    base = cs * lg
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_dvcvr21_21d_slope_v118_signal(closeadj, volume):
    dv = _dollar_vol(closeadj, volume)
    base = _std(dv, 126) / _mean(dv, 126).replace(0, np.nan)
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_dvcvr63_63d_slope_v119_signal(closeadj, volume):
    dv = _dollar_vol(closeadj, volume)
    base = _std(dv, 126) / _mean(dv, 126).replace(0, np.nan)
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_dvcvr5_5d_slope_v120_signal(closeadj, volume):
    dv = _dollar_vol(closeadj, volume)
    base = _std(dv, 126) / _mean(dv, 126).replace(0, np.nan)
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_volretcorrr21_21d_slope_v121_signal(closeadj, volume):
    ar = closeadj.pct_change().abs()
    lv = np.log(volume.replace(0, np.nan))
    base = lv.rolling(63, min_periods=21).corr(ar)
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_volretcorrr63_63d_slope_v122_signal(closeadj, volume):
    ar = closeadj.pct_change().abs()
    lv = np.log(volume.replace(0, np.nan))
    base = lv.rolling(63, min_periods=21).corr(ar)
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_volretcorrr5_5d_slope_v123_signal(closeadj, volume):
    ar = closeadj.pct_change().abs()
    lv = np.log(volume.replace(0, np.nan))
    base = lv.rolling(63, min_periods=21).corr(ar)
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_medamihudr21_21d_slope_v124_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    dv = _dollar_vol(closeadj, volume)
    raw = ret / dv
    base = np.log(raw.rolling(63, min_periods=21).median().replace(0, np.nan) * 1e12 + 1.0)
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_medamihudr63_63d_slope_v125_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    dv = _dollar_vol(closeadj, volume)
    raw = ret / dv
    base = np.log(raw.rolling(63, min_periods=21).median().replace(0, np.nan) * 1e12 + 1.0)
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_medamihudr5_5d_slope_v126_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    dv = _dollar_vol(closeadj, volume)
    raw = ret / dv
    base = np.log(raw.rolling(63, min_periods=21).median().replace(0, np.nan) * 1e12 + 1.0)
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_tailamihudr21_21d_slope_v127_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    dv = _dollar_vol(closeadj, volume)
    raw = ret / dv
    base = np.log(raw.rolling(63, min_periods=21).quantile(0.90).replace(0, np.nan) * 1e12 + 1.0)
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_tailamihudr63_63d_slope_v128_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    dv = _dollar_vol(closeadj, volume)
    raw = ret / dv
    base = np.log(raw.rolling(63, min_periods=21).quantile(0.90).replace(0, np.nan) * 1e12 + 1.0)
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_tailamihudr5_5d_slope_v129_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    dv = _dollar_vol(closeadj, volume)
    raw = ret / dv
    base = np.log(raw.rolling(63, min_periods=21).quantile(0.90).replace(0, np.nan) * 1e12 + 1.0)
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_dvskewr21_21d_slope_v130_signal(closeadj, volume):
    ldv = np.log(_dollar_vol(closeadj, volume))
    base = ldv.rolling(126, min_periods=63).skew()
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_dvskewr63_63d_slope_v131_signal(closeadj, volume):
    ldv = np.log(_dollar_vol(closeadj, volume))
    base = ldv.rolling(126, min_periods=63).skew()
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_dvskewr5_5d_slope_v132_signal(closeadj, volume):
    ldv = np.log(_dollar_vol(closeadj, volume))
    base = ldv.rolling(126, min_periods=63).skew()
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_arspreadr21_21d_slope_v133_signal(close, high, low):
    eta = (np.log(high.replace(0, np.nan)) + np.log(low.replace(0, np.nan))) / 2.0
    c = np.log(close.replace(0, np.nan))
    s2 = (-(4.0 * (c - eta) * (c - eta.shift(-1)))).clip(lower=0)
    base = np.sqrt(s2).rolling(63, min_periods=21).mean()
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_arspreadr63_63d_slope_v134_signal(close, high, low):
    eta = (np.log(high.replace(0, np.nan)) + np.log(low.replace(0, np.nan))) / 2.0
    c = np.log(close.replace(0, np.nan))
    s2 = (-(4.0 * (c - eta) * (c - eta.shift(-1)))).clip(lower=0)
    base = np.sqrt(s2).rolling(63, min_periods=21).mean()
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_arspreadr5_5d_slope_v135_signal(close, high, low):
    eta = (np.log(high.replace(0, np.nan)) + np.log(low.replace(0, np.nan))) / 2.0
    c = np.log(close.replace(0, np.nan))
    s2 = (-(4.0 * (c - eta) * (c - eta.shift(-1)))).clip(lower=0)
    base = np.sqrt(s2).rolling(63, min_periods=21).mean()
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_csperparkr21_21d_slope_v136_signal(high, low):
    cs = _corwin_schultz(high, low, 63)
    park = ((np.log(high.replace(0, np.nan) / low.replace(0, np.nan))) ** 2).rolling(63, min_periods=21).mean()
    base = cs / np.sqrt(park).replace(0, np.nan)
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_csperparkr63_63d_slope_v137_signal(high, low):
    cs = _corwin_schultz(high, low, 63)
    park = ((np.log(high.replace(0, np.nan) / low.replace(0, np.nan))) ** 2).rolling(63, min_periods=21).mean()
    base = cs / np.sqrt(park).replace(0, np.nan)
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_csperparkr5_5d_slope_v138_signal(high, low):
    cs = _corwin_schultz(high, low, 63)
    park = ((np.log(high.replace(0, np.nan) / low.replace(0, np.nan))) ** 2).rolling(63, min_periods=21).mean()
    base = cs / np.sqrt(park).replace(0, np.nan)
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_liqstressr21_21d_slope_v139_signal(closeadj, high, low, volume):
    illiq = np.log(_amihud(closeadj, volume, 63).replace(0, np.nan) * 1e12 + 1.0)
    cs = _corwin_schultz(high, low, 63)
    dv = np.log(_dollar_vol(closeadj, volume)).rolling(63, min_periods=21).mean()
    base = _z(illiq, 252) + _z(cs, 252) - _z(dv, 252)
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_liqstressr63_63d_slope_v140_signal(closeadj, high, low, volume):
    illiq = np.log(_amihud(closeadj, volume, 63).replace(0, np.nan) * 1e12 + 1.0)
    cs = _corwin_schultz(high, low, 63)
    dv = np.log(_dollar_vol(closeadj, volume)).rolling(63, min_periods=21).mean()
    base = _z(illiq, 252) + _z(cs, 252) - _z(dv, 252)
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_liqstressr5_5d_slope_v141_signal(closeadj, high, low, volume):
    illiq = np.log(_amihud(closeadj, volume, 63).replace(0, np.nan) * 1e12 + 1.0)
    cs = _corwin_schultz(high, low, 63)
    dv = np.log(_dollar_vol(closeadj, volume)).rolling(63, min_periods=21).mean()
    base = _z(illiq, 252) + _z(cs, 252) - _z(dv, 252)
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_illiqcompositer21_21d_slope_v142_signal(closeadj, high, low, volume):
    a_r = _rank(_amihud(closeadj, volume, 63), 252)
    cs_r = _rank(_corwin_schultz(high, low, 63), 252)
    base = (a_r + cs_r) / 2.0
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_illiqcompositer63_63d_slope_v143_signal(closeadj, high, low, volume):
    a_r = _rank(_amihud(closeadj, volume, 63), 252)
    cs_r = _rank(_corwin_schultz(high, low, 63), 252)
    base = (a_r + cs_r) / 2.0
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_illiqcompositer5_5d_slope_v144_signal(closeadj, high, low, volume):
    a_r = _rank(_amihud(closeadj, volume, 63), 252)
    cs_r = _rank(_corwin_schultz(high, low, 63), 252)
    base = (a_r + cs_r) / 2.0
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_turnregimer21_21d_slope_v145_signal(volume):
    s = np.log(_turnover(volume, 63).replace(0, np.nan)).rolling(63, min_periods=21).mean()
    l = np.log(_turnover(volume, 252).replace(0, np.nan)).rolling(252, min_periods=126).mean()
    base = s - l
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_turnregimer63_63d_slope_v146_signal(volume):
    s = np.log(_turnover(volume, 63).replace(0, np.nan)).rolling(63, min_periods=21).mean()
    l = np.log(_turnover(volume, 252).replace(0, np.nan)).rolling(252, min_periods=126).mean()
    base = s - l
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_turnregimer5_5d_slope_v147_signal(volume):
    s = np.log(_turnover(volume, 63).replace(0, np.nan)).rolling(63, min_periods=21).mean()
    l = np.log(_turnover(volume, 252).replace(0, np.nan)).rolling(252, min_periods=126).mean()
    base = s - l
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_dvexpandr21_21d_slope_v148_signal(closeadj, volume):
    dv = _dollar_vol(closeadj, volume)
    base = np.log(_mean(dv, 21).replace(0, np.nan) / _mean(dv, 126).replace(0, np.nan))
    w = base
    deriv = w - w.shift(21)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_dvexpandr63_63d_slope_v149_signal(closeadj, volume):
    dv = _dollar_vol(closeadj, volume)
    base = np.log(_mean(dv, 21).replace(0, np.nan) / _mean(dv, 126).replace(0, np.nan))
    w = base.ewm(span=21, min_periods=10).mean()
    deriv = w - w.shift(63)
    return deriv.replace([np.inf, -np.inf], np.nan)

def f16lq_f16_liquidity_illiquidity_profile_dvexpandr5_5d_slope_v150_signal(closeadj, volume):
    dv = _dollar_vol(closeadj, volume)
    base = np.log(_mean(dv, 21).replace(0, np.nan) / _mean(dv, 126).replace(0, np.nan))
    w = base
    deriv = (w - w.shift(5)) / w.rolling(63, min_periods=21).std().replace(0, np.nan)
    return deriv.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f16lq_f16_liquidity_illiquidity_profile_amihud21r21_21d_slope_v001_signal,
    f16lq_f16_liquidity_illiquidity_profile_amihud21r63_63d_slope_v002_signal,
    f16lq_f16_liquidity_illiquidity_profile_amihud21r5_5d_slope_v003_signal,
    f16lq_f16_liquidity_illiquidity_profile_amihud63r21_21d_slope_v004_signal,
    f16lq_f16_liquidity_illiquidity_profile_amihud63r63_63d_slope_v005_signal,
    f16lq_f16_liquidity_illiquidity_profile_amihud63r5_5d_slope_v006_signal,
    f16lq_f16_liquidity_illiquidity_profile_amihud126r21_21d_slope_v007_signal,
    f16lq_f16_liquidity_illiquidity_profile_amihud126r63_63d_slope_v008_signal,
    f16lq_f16_liquidity_illiquidity_profile_amihud126r5_5d_slope_v009_signal,
    f16lq_f16_liquidity_illiquidity_profile_amihudtermr21_21d_slope_v010_signal,
    f16lq_f16_liquidity_illiquidity_profile_amihudtermr63_63d_slope_v011_signal,
    f16lq_f16_liquidity_illiquidity_profile_amihudtermr5_5d_slope_v012_signal,
    f16lq_f16_liquidity_illiquidity_profile_amihud5dr21_21d_slope_v013_signal,
    f16lq_f16_liquidity_illiquidity_profile_amihud5dr63_63d_slope_v014_signal,
    f16lq_f16_liquidity_illiquidity_profile_amihud5dr5_5d_slope_v015_signal,
    f16lq_f16_liquidity_illiquidity_profile_amihudrankr21_21d_slope_v016_signal,
    f16lq_f16_liquidity_illiquidity_profile_amihudrankr63_63d_slope_v017_signal,
    f16lq_f16_liquidity_illiquidity_profile_amihudrankr5_5d_slope_v018_signal,
    f16lq_f16_liquidity_illiquidity_profile_turnover63r21_21d_slope_v019_signal,
    f16lq_f16_liquidity_illiquidity_profile_turnover63r63_63d_slope_v020_signal,
    f16lq_f16_liquidity_illiquidity_profile_turnover63r5_5d_slope_v021_signal,
    f16lq_f16_liquidity_illiquidity_profile_turndispr21_21d_slope_v022_signal,
    f16lq_f16_liquidity_illiquidity_profile_turndispr63_63d_slope_v023_signal,
    f16lq_f16_liquidity_illiquidity_profile_turndispr5_5d_slope_v024_signal,
    f16lq_f16_liquidity_illiquidity_profile_turnskewr21_21d_slope_v025_signal,
    f16lq_f16_liquidity_illiquidity_profile_turnskewr63_63d_slope_v026_signal,
    f16lq_f16_liquidity_illiquidity_profile_turnskewr5_5d_slope_v027_signal,
    f16lq_f16_liquidity_illiquidity_profile_turnoverrankr21_21d_slope_v028_signal,
    f16lq_f16_liquidity_illiquidity_profile_turnoverrankr63_63d_slope_v029_signal,
    f16lq_f16_liquidity_illiquidity_profile_turnoverrankr5_5d_slope_v030_signal,
    f16lq_f16_liquidity_illiquidity_profile_csspread21r21_21d_slope_v031_signal,
    f16lq_f16_liquidity_illiquidity_profile_csspread21r63_63d_slope_v032_signal,
    f16lq_f16_liquidity_illiquidity_profile_csspread21r5_5d_slope_v033_signal,
    f16lq_f16_liquidity_illiquidity_profile_csspread63r21_21d_slope_v034_signal,
    f16lq_f16_liquidity_illiquidity_profile_csspread63r63_63d_slope_v035_signal,
    f16lq_f16_liquidity_illiquidity_profile_csspread63r5_5d_slope_v036_signal,
    f16lq_f16_liquidity_illiquidity_profile_csspread126r21_21d_slope_v037_signal,
    f16lq_f16_liquidity_illiquidity_profile_csspread126r63_63d_slope_v038_signal,
    f16lq_f16_liquidity_illiquidity_profile_csspread126r5_5d_slope_v039_signal,
    f16lq_f16_liquidity_illiquidity_profile_csdispr21_21d_slope_v040_signal,
    f16lq_f16_liquidity_illiquidity_profile_csdispr63_63d_slope_v041_signal,
    f16lq_f16_liquidity_illiquidity_profile_csdispr5_5d_slope_v042_signal,
    f16lq_f16_liquidity_illiquidity_profile_cscurvr21_21d_slope_v043_signal,
    f16lq_f16_liquidity_illiquidity_profile_cscurvr63_63d_slope_v044_signal,
    f16lq_f16_liquidity_illiquidity_profile_cscurvr5_5d_slope_v045_signal,
    f16lq_f16_liquidity_illiquidity_profile_dvlevelr21_21d_slope_v046_signal,
    f16lq_f16_liquidity_illiquidity_profile_dvlevelr63_63d_slope_v047_signal,
    f16lq_f16_liquidity_illiquidity_profile_dvlevelr5_5d_slope_v048_signal,
    f16lq_f16_liquidity_illiquidity_profile_dvgapr21_21d_slope_v049_signal,
    f16lq_f16_liquidity_illiquidity_profile_dvgapr63_63d_slope_v050_signal,
    f16lq_f16_liquidity_illiquidity_profile_dvgapr5_5d_slope_v051_signal,
    f16lq_f16_liquidity_illiquidity_profile_dvdrawdownr21_21d_slope_v052_signal,
    f16lq_f16_liquidity_illiquidity_profile_dvdrawdownr63_63d_slope_v053_signal,
    f16lq_f16_liquidity_illiquidity_profile_dvdrawdownr5_5d_slope_v054_signal,
    f16lq_f16_liquidity_illiquidity_profile_dvrankr21_21d_slope_v055_signal,
    f16lq_f16_liquidity_illiquidity_profile_dvrankr63_63d_slope_v056_signal,
    f16lq_f16_liquidity_illiquidity_profile_dvrankr5_5d_slope_v057_signal,
    f16lq_f16_liquidity_illiquidity_profile_amivestr21_21d_slope_v058_signal,
    f16lq_f16_liquidity_illiquidity_profile_amivestr63_63d_slope_v059_signal,
    f16lq_f16_liquidity_illiquidity_profile_amivestr5_5d_slope_v060_signal,
    f16lq_f16_liquidity_illiquidity_profile_rollspreadr21_21d_slope_v061_signal,
    f16lq_f16_liquidity_illiquidity_profile_rollspreadr63_63d_slope_v062_signal,
    f16lq_f16_liquidity_illiquidity_profile_rollspreadr5_5d_slope_v063_signal,
    f16lq_f16_liquidity_illiquidity_profile_rollspread126r21_21d_slope_v064_signal,
    f16lq_f16_liquidity_illiquidity_profile_rollspread126r63_63d_slope_v065_signal,
    f16lq_f16_liquidity_illiquidity_profile_rollspread126r5_5d_slope_v066_signal,
    f16lq_f16_liquidity_illiquidity_profile_retac1r21_21d_slope_v067_signal,
    f16lq_f16_liquidity_illiquidity_profile_retac1r63_63d_slope_v068_signal,
    f16lq_f16_liquidity_illiquidity_profile_retac1r5_5d_slope_v069_signal,
    f16lq_f16_liquidity_illiquidity_profile_varratior21_21d_slope_v070_signal,
    f16lq_f16_liquidity_illiquidity_profile_varratior63_63d_slope_v071_signal,
    f16lq_f16_liquidity_illiquidity_profile_varratior5_5d_slope_v072_signal,
    f16lq_f16_liquidity_illiquidity_profile_kyle63r21_21d_slope_v073_signal,
    f16lq_f16_liquidity_illiquidity_profile_kyle63r63_63d_slope_v074_signal,
    f16lq_f16_liquidity_illiquidity_profile_kyle63r5_5d_slope_v075_signal,
    f16lq_f16_liquidity_illiquidity_profile_kylerankr21_21d_slope_v076_signal,
    f16lq_f16_liquidity_illiquidity_profile_kylerankr63_63d_slope_v077_signal,
    f16lq_f16_liquidity_illiquidity_profile_kylerankr5_5d_slope_v078_signal,
    f16lq_f16_liquidity_illiquidity_profile_volcvr21_21d_slope_v079_signal,
    f16lq_f16_liquidity_illiquidity_profile_volcvr63_63d_slope_v080_signal,
    f16lq_f16_liquidity_illiquidity_profile_volcvr5_5d_slope_v081_signal,
    f16lq_f16_liquidity_illiquidity_profile_volherfr21_21d_slope_v082_signal,
    f16lq_f16_liquidity_illiquidity_profile_volherfr63_63d_slope_v083_signal,
    f16lq_f16_liquidity_illiquidity_profile_volherfr5_5d_slope_v084_signal,
    f16lq_f16_liquidity_illiquidity_profile_dvherfr21_21d_slope_v085_signal,
    f16lq_f16_liquidity_illiquidity_profile_dvherfr63_63d_slope_v086_signal,
    f16lq_f16_liquidity_illiquidity_profile_dvherfr5_5d_slope_v087_signal,
    f16lq_f16_liquidity_illiquidity_profile_volentropyr21_21d_slope_v088_signal,
    f16lq_f16_liquidity_illiquidity_profile_volentropyr63_63d_slope_v089_signal,
    f16lq_f16_liquidity_illiquidity_profile_volentropyr5_5d_slope_v090_signal,
    f16lq_f16_liquidity_illiquidity_profile_logvoldispr21_21d_slope_v091_signal,
    f16lq_f16_liquidity_illiquidity_profile_logvoldispr63_63d_slope_v092_signal,
    f16lq_f16_liquidity_illiquidity_profile_logvoldispr5_5d_slope_v093_signal,
    f16lq_f16_liquidity_illiquidity_profile_illiqofilliqr21_21d_slope_v094_signal,
    f16lq_f16_liquidity_illiquidity_profile_illiqofilliqr63_63d_slope_v095_signal,
    f16lq_f16_liquidity_illiquidity_profile_illiqofilliqr5_5d_slope_v096_signal,
    f16lq_f16_liquidity_illiquidity_profile_retperturnr21_21d_slope_v097_signal,
    f16lq_f16_liquidity_illiquidity_profile_retperturnr63_63d_slope_v098_signal,
    f16lq_f16_liquidity_illiquidity_profile_retperturnr5_5d_slope_v099_signal,
    f16lq_f16_liquidity_illiquidity_profile_rangedvr21_21d_slope_v100_signal,
    f16lq_f16_liquidity_illiquidity_profile_rangedvr63_63d_slope_v101_signal,
    f16lq_f16_liquidity_illiquidity_profile_rangedvr5_5d_slope_v102_signal,
    f16lq_f16_liquidity_illiquidity_profile_hlspreadr21_21d_slope_v103_signal,
    f16lq_f16_liquidity_illiquidity_profile_hlspreadr63_63d_slope_v104_signal,
    f16lq_f16_liquidity_illiquidity_profile_hlspreadr5_5d_slope_v105_signal,
    f16lq_f16_liquidity_illiquidity_profile_closepinr21_21d_slope_v106_signal,
    f16lq_f16_liquidity_illiquidity_profile_closepinr63_63d_slope_v107_signal,
    f16lq_f16_liquidity_illiquidity_profile_closepinr5_5d_slope_v108_signal,
    f16lq_f16_liquidity_illiquidity_profile_amihudfloorr21_21d_slope_v109_signal,
    f16lq_f16_liquidity_illiquidity_profile_amihudfloorr63_63d_slope_v110_signal,
    f16lq_f16_liquidity_illiquidity_profile_amihudfloorr5_5d_slope_v111_signal,
    f16lq_f16_liquidity_illiquidity_profile_spreadpervolr21_21d_slope_v112_signal,
    f16lq_f16_liquidity_illiquidity_profile_spreadpervolr63_63d_slope_v113_signal,
    f16lq_f16_liquidity_illiquidity_profile_spreadpervolr5_5d_slope_v114_signal,
    f16lq_f16_liquidity_illiquidity_profile_costcompoundr21_21d_slope_v115_signal,
    f16lq_f16_liquidity_illiquidity_profile_costcompoundr63_63d_slope_v116_signal,
    f16lq_f16_liquidity_illiquidity_profile_costcompoundr5_5d_slope_v117_signal,
    f16lq_f16_liquidity_illiquidity_profile_dvcvr21_21d_slope_v118_signal,
    f16lq_f16_liquidity_illiquidity_profile_dvcvr63_63d_slope_v119_signal,
    f16lq_f16_liquidity_illiquidity_profile_dvcvr5_5d_slope_v120_signal,
    f16lq_f16_liquidity_illiquidity_profile_volretcorrr21_21d_slope_v121_signal,
    f16lq_f16_liquidity_illiquidity_profile_volretcorrr63_63d_slope_v122_signal,
    f16lq_f16_liquidity_illiquidity_profile_volretcorrr5_5d_slope_v123_signal,
    f16lq_f16_liquidity_illiquidity_profile_medamihudr21_21d_slope_v124_signal,
    f16lq_f16_liquidity_illiquidity_profile_medamihudr63_63d_slope_v125_signal,
    f16lq_f16_liquidity_illiquidity_profile_medamihudr5_5d_slope_v126_signal,
    f16lq_f16_liquidity_illiquidity_profile_tailamihudr21_21d_slope_v127_signal,
    f16lq_f16_liquidity_illiquidity_profile_tailamihudr63_63d_slope_v128_signal,
    f16lq_f16_liquidity_illiquidity_profile_tailamihudr5_5d_slope_v129_signal,
    f16lq_f16_liquidity_illiquidity_profile_dvskewr21_21d_slope_v130_signal,
    f16lq_f16_liquidity_illiquidity_profile_dvskewr63_63d_slope_v131_signal,
    f16lq_f16_liquidity_illiquidity_profile_dvskewr5_5d_slope_v132_signal,
    f16lq_f16_liquidity_illiquidity_profile_arspreadr21_21d_slope_v133_signal,
    f16lq_f16_liquidity_illiquidity_profile_arspreadr63_63d_slope_v134_signal,
    f16lq_f16_liquidity_illiquidity_profile_arspreadr5_5d_slope_v135_signal,
    f16lq_f16_liquidity_illiquidity_profile_csperparkr21_21d_slope_v136_signal,
    f16lq_f16_liquidity_illiquidity_profile_csperparkr63_63d_slope_v137_signal,
    f16lq_f16_liquidity_illiquidity_profile_csperparkr5_5d_slope_v138_signal,
    f16lq_f16_liquidity_illiquidity_profile_liqstressr21_21d_slope_v139_signal,
    f16lq_f16_liquidity_illiquidity_profile_liqstressr63_63d_slope_v140_signal,
    f16lq_f16_liquidity_illiquidity_profile_liqstressr5_5d_slope_v141_signal,
    f16lq_f16_liquidity_illiquidity_profile_illiqcompositer21_21d_slope_v142_signal,
    f16lq_f16_liquidity_illiquidity_profile_illiqcompositer63_63d_slope_v143_signal,
    f16lq_f16_liquidity_illiquidity_profile_illiqcompositer5_5d_slope_v144_signal,
    f16lq_f16_liquidity_illiquidity_profile_turnregimer21_21d_slope_v145_signal,
    f16lq_f16_liquidity_illiquidity_profile_turnregimer63_63d_slope_v146_signal,
    f16lq_f16_liquidity_illiquidity_profile_turnregimer5_5d_slope_v147_signal,
    f16lq_f16_liquidity_illiquidity_profile_dvexpandr21_21d_slope_v148_signal,
    f16lq_f16_liquidity_illiquidity_profile_dvexpandr63_63d_slope_v149_signal,
    f16lq_f16_liquidity_illiquidity_profile_dvexpandr5_5d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F16_LIQUIDITY_ILLIQUIDITY_PROFILE_REGISTRY_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0003, 0.035, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.01, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(8e5, 5e5, n)) + 1e4, name="volume")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}

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

    print("OK f16_liquidity_illiquidity_profile_2nd_derivatives_001_150_claude: %d features pass" % n_features)
