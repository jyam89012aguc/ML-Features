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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _f12_gap(openp, close):
    pc = close.shift(1)
    return openp / pc.replace(0, np.nan) - 1.0


def _f12_intraday(openp, close):
    return close / openp.replace(0, np.nan) - 1.0


def _f12_overnight_ret(openp, close):
    pc = close.shift(1)
    return openp / pc.replace(0, np.nan) - 1.0


def _f12_abs_gap(openp, close):
    return (_f12_gap(openp, close)).abs()


def f12gn_f12_gap_news_shock_gaplvlrate_5d_slope_v001_signal(open, close):
    base = _f12_gap(open, close)
    result = (base - base.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gaplvlsnr_10d_slope_v002_signal(open, close):
    base = _f12_gap(open, close)
    chg = base - base.shift(10)
    result = chg / _std(base, 30).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gaplvlsmdf_5d_slope_v003_signal(open, close):
    base = _f12_gap(open, close)
    sm = base.ewm(span=5, min_periods=2).mean()
    result = (sm - sm.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_absgaprate_5d_slope_v004_signal(open, close):
    base = _f12_abs_gap(open, close)
    result = (base - base.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_absgapsnr_10d_slope_v005_signal(open, close):
    base = _f12_abs_gap(open, close)
    chg = base - base.shift(10)
    result = chg / _std(base, 30).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_absgapsmdf_5d_slope_v006_signal(open, close):
    base = _f12_abs_gap(open, close)
    sm = base.ewm(span=5, min_periods=2).mean()
    result = (sm - sm.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_intradayrate_5d_slope_v007_signal(open, close):
    base = _f12_intraday(open, close)
    result = (base - base.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_intradaysnr_10d_slope_v008_signal(open, close):
    base = _f12_intraday(open, close)
    chg = base - base.shift(10)
    result = chg / _std(base, 30).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_intradaysmdf_5d_slope_v009_signal(open, close):
    base = _f12_intraday(open, close)
    sm = base.ewm(span=5, min_periods=2).mean()
    result = (sm - sm.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_onvsintrarate_5d_slope_v010_signal(open, close):
    on = _f12_overnight_ret(open, close)
    intra = _f12_intraday(open, close)
    base = (on - intra) / (on.abs() + intra.abs()).replace(0, np.nan)
    result = (base - base.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_onvsintrasnr_10d_slope_v011_signal(open, close):
    on = _f12_overnight_ret(open, close)
    intra = _f12_intraday(open, close)
    base = (on - intra) / (on.abs() + intra.abs()).replace(0, np.nan)
    chg = base - base.shift(10)
    result = chg / _std(base, 30).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_onvsintrasmdf_5d_slope_v012_signal(open, close):
    on = _f12_overnight_ret(open, close)
    intra = _f12_intraday(open, close)
    base = (on - intra) / (on.abs() + intra.abs()).replace(0, np.nan)
    sm = base.ewm(span=5, min_periods=2).mean()
    result = (sm - sm.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_loggaprate_5d_slope_v013_signal(open, high, low, close):
    ag = _f12_abs_gap(open, close)
    rng = (high - low) / close.shift(1).replace(0, np.nan)
    base = ag / rng.replace(0, np.nan)
    result = (base - base.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_loggapsnr_10d_slope_v014_signal(open, high, low, close):
    ag = _f12_abs_gap(open, close)
    rng = (high - low) / close.shift(1).replace(0, np.nan)
    base = ag / rng.replace(0, np.nan)
    chg = base - base.shift(10)
    result = chg / _std(base, 30).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_loggapsmdf_5d_slope_v015_signal(open, high, low, close):
    ag = _f12_abs_gap(open, close)
    rng = (high - low) / close.shift(1).replace(0, np.nan)
    base = ag / rng.replace(0, np.nan)
    sm = base.ewm(span=5, min_periods=2).mean()
    result = (sm - sm.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapvsrangerate_5d_slope_v016_signal(open, high, low, close):
    pc = close.shift(1)
    pr = (high.shift(1) - low.shift(1))
    base = (open - pc) / pr.replace(0, np.nan)
    result = (base - base.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapvsrangesnr_10d_slope_v017_signal(open, high, low, close):
    pc = close.shift(1)
    pr = (high.shift(1) - low.shift(1))
    base = (open - pc) / pr.replace(0, np.nan)
    chg = base - base.shift(10)
    result = chg / _std(base, 30).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapvsrangesmdf_5d_slope_v018_signal(open, high, low, close):
    pc = close.shift(1)
    pr = (high.shift(1) - low.shift(1))
    base = (open - pc) / pr.replace(0, np.nan)
    sm = base.ewm(span=5, min_periods=2).mean()
    result = (sm - sm.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_truegaprate_5d_slope_v019_signal(open, high, low, close):
    ph = high.shift(1)
    pl = low.shift(1)
    up = (open - ph).clip(lower=0.0)
    dn = (pl - open).clip(lower=0.0)
    base = (up - dn) / close.shift(1).replace(0, np.nan)
    result = (base - base.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_truegapsnr_10d_slope_v020_signal(open, high, low, close):
    ph = high.shift(1)
    pl = low.shift(1)
    up = (open - ph).clip(lower=0.0)
    dn = (pl - open).clip(lower=0.0)
    base = (up - dn) / close.shift(1).replace(0, np.nan)
    chg = base - base.shift(10)
    result = chg / _std(base, 30).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_truegapsmdf_5d_slope_v021_signal(open, high, low, close):
    ph = high.shift(1)
    pl = low.shift(1)
    up = (open - ph).clip(lower=0.0)
    dn = (pl - open).clip(lower=0.0)
    base = (up - dn) / close.shift(1).replace(0, np.nan)
    sm = base.ewm(span=5, min_periods=2).mean()
    result = (sm - sm.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_openinrangerate_5d_slope_v022_signal(open, high, low, close):
    ph = high.shift(1)
    pl = low.shift(1)
    base = (open - pl) / (ph - pl).replace(0, np.nan)
    result = (base - base.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_openinrangesnr_10d_slope_v023_signal(open, high, low, close):
    ph = high.shift(1)
    pl = low.shift(1)
    base = (open - pl) / (ph - pl).replace(0, np.nan)
    chg = base - base.shift(10)
    result = chg / _std(base, 30).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_openinrangesmdf_5d_slope_v024_signal(open, high, low, close):
    ph = high.shift(1)
    pl = low.shift(1)
    base = (open - pl) / (ph - pl).replace(0, np.nan)
    sm = base.ewm(span=5, min_periods=2).mean()
    result = (sm - sm.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapsigrate_5d_slope_v025_signal(open, close):
    on = _f12_overnight_ret(open, close).abs()
    intra = _f12_intraday(open, close).abs()
    base = np.log((on.rolling(5, min_periods=3).sum() + 1e-6) / (intra.rolling(5, min_periods=3).sum() + 1e-6))
    result = (base - base.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapsigsnr_10d_slope_v026_signal(open, close):
    on = _f12_overnight_ret(open, close).abs()
    intra = _f12_intraday(open, close).abs()
    base = np.log((on.rolling(5, min_periods=3).sum() + 1e-6) / (intra.rolling(5, min_periods=3).sum() + 1e-6))
    chg = base - base.shift(10)
    result = chg / _std(base, 30).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapsigsmdf_5d_slope_v027_signal(open, close):
    on = _f12_overnight_ret(open, close).abs()
    intra = _f12_intraday(open, close).abs()
    base = np.log((on.rolling(5, min_periods=3).sum() + 1e-6) / (intra.rolling(5, min_periods=3).sum() + 1e-6))
    sm = base.ewm(span=5, min_periods=2).mean()
    result = (sm - sm.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_breakawayrate_5d_slope_v028_signal(open, high, close):
    ph = high.shift(1)
    pc = close.shift(1)
    base = (open - ph).clip(lower=0) / pc.replace(0, np.nan)
    result = (base - base.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_breakawaysnr_10d_slope_v029_signal(open, high, close):
    ph = high.shift(1)
    pc = close.shift(1)
    base = (open - ph).clip(lower=0) / pc.replace(0, np.nan)
    chg = base - base.shift(10)
    result = chg / _std(base, 30).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_breakawaysmdf_5d_slope_v030_signal(open, high, close):
    ph = high.shift(1)
    pc = close.shift(1)
    base = (open - ph).clip(lower=0) / pc.replace(0, np.nan)
    sm = base.ewm(span=5, min_periods=2).mean()
    result = (sm - sm.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_cumgap21rate_5d_slope_v031_signal(open, close):
    g = _f12_gap(open, close)
    base = g.rolling(21, min_periods=10).sum()
    result = (base - base.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_cumgap21snr_21d_slope_v032_signal(open, close):
    g = _f12_gap(open, close)
    base = g.rolling(21, min_periods=10).sum()
    chg = base - base.shift(21)
    result = chg / _std(base, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_cumgap21smdf_5d_slope_v033_signal(open, close):
    g = _f12_gap(open, close)
    base = g.rolling(21, min_periods=10).sum()
    sm = base.ewm(span=5, min_periods=2).mean()
    result = (sm - sm.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapstd21rate_5d_slope_v034_signal(open, close):
    g = _f12_gap(open, close)
    base = _std(g, 21)
    result = (base - base.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapstd21snr_21d_slope_v035_signal(open, close):
    g = _f12_gap(open, close)
    base = _std(g, 21)
    chg = base - base.shift(21)
    result = chg / _std(base, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapstd21smdf_5d_slope_v036_signal(open, close):
    g = _f12_gap(open, close)
    base = _std(g, 21)
    sm = base.ewm(span=5, min_periods=2).mean()
    result = (sm - sm.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapz21rate_5d_slope_v037_signal(open, close):
    g = _f12_gap(open, close)
    g3 = g.rolling(3, min_periods=2).sum()
    base = _z(g3, 21)
    result = (base - base.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapz21snr_21d_slope_v038_signal(open, close):
    g = _f12_gap(open, close)
    g3 = g.rolling(3, min_periods=2).sum()
    base = _z(g3, 21)
    chg = base - base.shift(21)
    result = chg / _std(base, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapz21smdf_5d_slope_v039_signal(open, close):
    g = _f12_gap(open, close)
    g3 = g.rolling(3, min_periods=2).sum()
    base = _z(g3, 21)
    sm = base.ewm(span=5, min_periods=2).mean()
    result = (sm - sm.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_absgapema21rate_5d_slope_v040_signal(open, close):
    ag = _f12_abs_gap(open, close)
    base = ag.ewm(span=21, min_periods=10).mean()
    result = (base - base.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_absgapema21snr_21d_slope_v041_signal(open, close):
    ag = _f12_abs_gap(open, close)
    base = ag.ewm(span=21, min_periods=10).mean()
    chg = base - base.shift(21)
    result = chg / _std(base, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_absgapema21smdf_5d_slope_v042_signal(open, close):
    ag = _f12_abs_gap(open, close)
    base = ag.ewm(span=21, min_periods=10).mean()
    sm = base.ewm(span=5, min_periods=2).mean()
    result = (sm - sm.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_onvol21rate_5d_slope_v043_signal(open, close):
    on = _f12_overnight_ret(open, close)
    intra = _f12_intraday(open, close)
    base = _std(on, 21) - _std(intra, 21)
    result = (base - base.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_onvol21snr_21d_slope_v044_signal(open, close):
    on = _f12_overnight_ret(open, close)
    intra = _f12_intraday(open, close)
    base = _std(on, 21) - _std(intra, 21)
    chg = base - base.shift(21)
    result = chg / _std(base, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_onvol21smdf_5d_slope_v045_signal(open, close):
    on = _f12_overnight_ret(open, close)
    intra = _f12_intraday(open, close)
    base = _std(on, 21) - _std(intra, 21)
    sm = base.ewm(span=5, min_periods=2).mean()
    result = (sm - sm.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapqv21rate_5d_slope_v046_signal(open, close):
    g = _f12_gap(open, close)
    base = g.abs().rolling(21, min_periods=10).mean() / g.abs().rolling(126, min_periods=63).mean().replace(0, np.nan)
    result = (base - base.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapqv21snr_21d_slope_v047_signal(open, close):
    g = _f12_gap(open, close)
    base = g.abs().rolling(21, min_periods=10).mean() / g.abs().rolling(126, min_periods=63).mean().replace(0, np.nan)
    chg = base - base.shift(21)
    result = chg / _std(base, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapqv21smdf_5d_slope_v048_signal(open, close):
    g = _f12_gap(open, close)
    base = g.abs().rolling(21, min_periods=10).mean() / g.abs().rolling(126, min_periods=63).mean().replace(0, np.nan)
    sm = base.ewm(span=5, min_periods=2).mean()
    result = (sm - sm.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_vwgap21rate_5d_slope_v049_signal(open, close, volume):
    g = _f12_gap(open, close)
    num = (g * volume).rolling(21, min_periods=10).sum()
    den = volume.rolling(21, min_periods=10).sum()
    base = num / den.replace(0, np.nan)
    result = (base - base.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_vwgap21snr_21d_slope_v050_signal(open, close, volume):
    g = _f12_gap(open, close)
    num = (g * volume).rolling(21, min_periods=10).sum()
    den = volume.rolling(21, min_periods=10).sum()
    base = num / den.replace(0, np.nan)
    chg = base - base.shift(21)
    result = chg / _std(base, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_vwgap21smdf_5d_slope_v051_signal(open, close, volume):
    g = _f12_gap(open, close)
    num = (g * volume).rolling(21, min_periods=10).sum()
    den = volume.rolling(21, min_periods=10).sum()
    base = num / den.replace(0, np.nan)
    sm = base.ewm(span=5, min_periods=2).mean()
    result = (sm - sm.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_upgapsum21rate_5d_slope_v052_signal(open, close):
    g = _f12_gap(open, close)
    base = g.clip(lower=0).rolling(21, min_periods=10).sum()
    result = (base - base.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_upgapsum21snr_21d_slope_v053_signal(open, close):
    g = _f12_gap(open, close)
    base = g.clip(lower=0).rolling(21, min_periods=10).sum()
    chg = base - base.shift(21)
    result = chg / _std(base, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_upgapsum21smdf_5d_slope_v054_signal(open, close):
    g = _f12_gap(open, close)
    base = g.clip(lower=0).rolling(21, min_periods=10).sum()
    sm = base.ewm(span=5, min_periods=2).mean()
    result = (sm - sm.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_dngapsum21rate_5d_slope_v055_signal(open, close):
    g = _f12_gap(open, close)
    base = g.clip(upper=0).rolling(21, min_periods=10).sum()
    result = (base - base.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_dngapsum21snr_21d_slope_v056_signal(open, close):
    g = _f12_gap(open, close)
    base = g.clip(upper=0).rolling(21, min_periods=10).sum()
    chg = base - base.shift(21)
    result = chg / _std(base, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_dngapsum21smdf_5d_slope_v057_signal(open, close):
    g = _f12_gap(open, close)
    base = g.clip(upper=0).rolling(21, min_periods=10).sum()
    sm = base.ewm(span=5, min_periods=2).mean()
    result = (sm - sm.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_maxgap21rate_5d_slope_v058_signal(open, close):
    ag = _f12_abs_gap(open, close)
    base = ag.rolling(21, min_periods=10).max()
    result = (base - base.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_maxgap21snr_21d_slope_v059_signal(open, close):
    ag = _f12_abs_gap(open, close)
    base = ag.rolling(21, min_periods=10).max()
    chg = base - base.shift(21)
    result = chg / _std(base, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_maxgap21smdf_5d_slope_v060_signal(open, close):
    ag = _f12_abs_gap(open, close)
    base = ag.rolling(21, min_periods=10).max()
    sm = base.ewm(span=5, min_periods=2).mean()
    result = (sm - sm.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gappurity21rate_5d_slope_v061_signal(open, close):
    g = _f12_gap(open, close)
    flip = (np.sign(g) != np.sign(g.shift(1))).astype(float)
    base = (flip * g.abs()).rolling(21, min_periods=10).mean()
    result = (base - base.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gappurity21snr_21d_slope_v062_signal(open, close):
    g = _f12_gap(open, close)
    flip = (np.sign(g) != np.sign(g.shift(1))).astype(float)
    base = (flip * g.abs()).rolling(21, min_periods=10).mean()
    chg = base - base.shift(21)
    result = chg / _std(base, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gappurity21smdf_5d_slope_v063_signal(open, close):
    g = _f12_gap(open, close)
    flip = (np.sign(g) != np.sign(g.shift(1))).astype(float)
    base = (flip * g.abs()).rolling(21, min_periods=10).mean()
    sm = base.ewm(span=5, min_periods=2).mean()
    result = (sm - sm.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_qvshare21rate_5d_slope_v064_signal(open, close):
    on = _f12_overnight_ret(open, close)
    intra = _f12_intraday(open, close)
    onqv = (on ** 2).rolling(21, min_periods=10).sum()
    inqv = (intra ** 2).rolling(21, min_periods=10).sum()
    base = onqv / (onqv + inqv).replace(0, np.nan)
    result = (base - base.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_qvshare21snr_21d_slope_v065_signal(open, close):
    on = _f12_overnight_ret(open, close)
    intra = _f12_intraday(open, close)
    onqv = (on ** 2).rolling(21, min_periods=10).sum()
    inqv = (intra ** 2).rolling(21, min_periods=10).sum()
    base = onqv / (onqv + inqv).replace(0, np.nan)
    chg = base - base.shift(21)
    result = chg / _std(base, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_qvshare21smdf_5d_slope_v066_signal(open, close):
    on = _f12_overnight_ret(open, close)
    intra = _f12_intraday(open, close)
    onqv = (on ** 2).rolling(21, min_periods=10).sum()
    inqv = (intra ** 2).rolling(21, min_periods=10).sum()
    base = onqv / (onqv + inqv).replace(0, np.nan)
    sm = base.ewm(span=5, min_periods=2).mean()
    result = (sm - sm.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_onintraspr21rate_5d_slope_v067_signal(open, close):
    on = _f12_overnight_ret(open, close)
    intra = _f12_intraday(open, close)
    base = on.rolling(21, min_periods=10).sum() - intra.rolling(21, min_periods=10).sum()
    result = (base - base.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_onintraspr21snr_21d_slope_v068_signal(open, close):
    on = _f12_overnight_ret(open, close)
    intra = _f12_intraday(open, close)
    base = on.rolling(21, min_periods=10).sum() - intra.rolling(21, min_periods=10).sum()
    chg = base - base.shift(21)
    result = chg / _std(base, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_onintraspr21smdf_5d_slope_v069_signal(open, close):
    on = _f12_overnight_ret(open, close)
    intra = _f12_intraday(open, close)
    base = on.rolling(21, min_periods=10).sum() - intra.rolling(21, min_periods=10).sum()
    sm = base.ewm(span=5, min_periods=2).mean()
    result = (sm - sm.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_acuteburstrate_5d_slope_v070_signal(open, close):
    on2 = _f12_overnight_ret(open, close) ** 2
    recent = on2.rolling(5, min_periods=3).mean()
    base = recent / on2.rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = (base - base.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_acuteburstsnr_21d_slope_v071_signal(open, close):
    on2 = _f12_overnight_ret(open, close) ** 2
    recent = on2.rolling(5, min_periods=3).mean()
    base = recent / on2.rolling(63, min_periods=21).mean().replace(0, np.nan)
    chg = base - base.shift(21)
    result = chg / _std(base, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_acuteburstsmdf_5d_slope_v072_signal(open, close):
    on2 = _f12_overnight_ret(open, close) ** 2
    recent = on2.rolling(5, min_periods=3).mean()
    base = recent / on2.rolling(63, min_periods=21).mean().replace(0, np.nan)
    sm = base.ewm(span=5, min_periods=2).mean()
    result = (sm - sm.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_signbal21rate_5d_slope_v073_signal(open, close):
    g = _f12_gap(open, close)
    base = np.tanh(g / g.abs().rolling(63, min_periods=21).mean().replace(0, np.nan)).rolling(21, min_periods=10).mean()
    result = (base - base.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_signbal21snr_21d_slope_v074_signal(open, close):
    g = _f12_gap(open, close)
    base = np.tanh(g / g.abs().rolling(63, min_periods=21).mean().replace(0, np.nan)).rolling(21, min_periods=10).mean()
    chg = base - base.shift(21)
    result = chg / _std(base, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_signbal21smdf_5d_slope_v075_signal(open, close):
    g = _f12_gap(open, close)
    base = np.tanh(g / g.abs().rolling(63, min_periods=21).mean().replace(0, np.nan)).rolling(21, min_periods=10).mean()
    sm = base.ewm(span=5, min_periods=2).mean()
    result = (sm - sm.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_cumgap63rate_21d_slope_v076_signal(open, close):
    g = _f12_gap(open, close)
    base = g.rolling(63, min_periods=21).sum()
    result = (base - base.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_cumgap63snr_63d_slope_v077_signal(open, close):
    g = _f12_gap(open, close)
    base = g.rolling(63, min_periods=21).sum()
    chg = base - base.shift(63)
    result = chg / _std(base, 189).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_cumgap63smdf_21d_slope_v078_signal(open, close):
    g = _f12_gap(open, close)
    base = g.rolling(63, min_periods=21).sum()
    sm = base.ewm(span=21, min_periods=10).mean()
    result = (sm - sm.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapstd63rate_21d_slope_v079_signal(open, close):
    g = _f12_gap(open, close)
    base = _std(g, 63)
    result = (base - base.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapstd63snr_63d_slope_v080_signal(open, close):
    g = _f12_gap(open, close)
    base = _std(g, 63)
    chg = base - base.shift(63)
    result = chg / _std(base, 189).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapstd63smdf_21d_slope_v081_signal(open, close):
    g = _f12_gap(open, close)
    base = _std(g, 63)
    sm = base.ewm(span=21, min_periods=10).mean()
    result = (sm - sm.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapskew63rate_21d_slope_v082_signal(open, close):
    g = _f12_gap(open, close)
    base = g.rolling(63, min_periods=21).skew()
    result = (base - base.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapskew63snr_63d_slope_v083_signal(open, close):
    g = _f12_gap(open, close)
    base = g.rolling(63, min_periods=21).skew()
    chg = base - base.shift(63)
    result = chg / _std(base, 189).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapskew63smdf_21d_slope_v084_signal(open, close):
    g = _f12_gap(open, close)
    base = g.rolling(63, min_periods=21).skew()
    sm = base.ewm(span=21, min_periods=10).mean()
    result = (sm - sm.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapasym63rate_21d_slope_v085_signal(open, close):
    g = _f12_gap(open, close)
    up = g.where(g > 0).rolling(63, min_periods=15).mean()
    dn = (-g.where(g < 0)).rolling(63, min_periods=15).mean()
    base = up / dn.replace(0, np.nan) - 1.0
    result = (base - base.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapasym63snr_63d_slope_v086_signal(open, close):
    g = _f12_gap(open, close)
    up = g.where(g > 0).rolling(63, min_periods=15).mean()
    dn = (-g.where(g < 0)).rolling(63, min_periods=15).mean()
    base = up / dn.replace(0, np.nan) - 1.0
    chg = base - base.shift(63)
    result = chg / _std(base, 189).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapasym63smdf_21d_slope_v087_signal(open, close):
    g = _f12_gap(open, close)
    up = g.where(g > 0).rolling(63, min_periods=15).mean()
    dn = (-g.where(g < 0)).rolling(63, min_periods=15).mean()
    base = up / dn.replace(0, np.nan) - 1.0
    sm = base.ewm(span=21, min_periods=10).mean()
    result = (sm - sm.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_ondrift63rate_21d_slope_v088_signal(open, close):
    g = _f12_gap(open, close)
    v = _std(g, 21)
    base = _std(v, 63)
    result = (base - base.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_ondrift63snr_63d_slope_v089_signal(open, close):
    g = _f12_gap(open, close)
    v = _std(g, 21)
    base = _std(v, 63)
    chg = base - base.shift(63)
    result = chg / _std(base, 189).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_ondrift63smdf_21d_slope_v090_signal(open, close):
    g = _f12_gap(open, close)
    v = _std(g, 21)
    base = _std(v, 63)
    sm = base.ewm(span=21, min_periods=10).mean()
    result = (sm - sm.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapbal63rate_21d_slope_v091_signal(open, close):
    g = _f12_gap(open, close)
    thr = g.abs().rolling(126, min_periods=63).quantile(0.80)
    up = (g >= thr).astype(float).rolling(63, min_periods=21).sum()
    dn = (g <= -thr).astype(float).rolling(63, min_periods=21).sum()
    base = (up - dn) / (up + dn).replace(0, np.nan)
    result = (base - base.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapbal63snr_63d_slope_v092_signal(open, close):
    g = _f12_gap(open, close)
    thr = g.abs().rolling(126, min_periods=63).quantile(0.80)
    up = (g >= thr).astype(float).rolling(63, min_periods=21).sum()
    dn = (g <= -thr).astype(float).rolling(63, min_periods=21).sum()
    base = (up - dn) / (up + dn).replace(0, np.nan)
    chg = base - base.shift(63)
    result = chg / _std(base, 189).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapbal63smdf_21d_slope_v093_signal(open, close):
    g = _f12_gap(open, close)
    thr = g.abs().rolling(126, min_periods=63).quantile(0.80)
    up = (g >= thr).astype(float).rolling(63, min_periods=21).sum()
    dn = (g <= -thr).astype(float).rolling(63, min_periods=21).sum()
    base = (up - dn) / (up + dn).replace(0, np.nan)
    sm = base.ewm(span=21, min_periods=10).mean()
    result = (sm - sm.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_onintravolr63rate_21d_slope_v094_signal(open, close):
    on = _f12_overnight_ret(open, close)
    intra = _f12_intraday(open, close)
    base = _std(on, 63) / _std(intra, 63).replace(0, np.nan)
    result = (base - base.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_onintravolr63snr_63d_slope_v095_signal(open, close):
    on = _f12_overnight_ret(open, close)
    intra = _f12_intraday(open, close)
    base = _std(on, 63) / _std(intra, 63).replace(0, np.nan)
    chg = base - base.shift(63)
    result = chg / _std(base, 189).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_onintravolr63smdf_21d_slope_v096_signal(open, close):
    on = _f12_overnight_ret(open, close)
    intra = _f12_intraday(open, close)
    base = _std(on, 63) / _std(intra, 63).replace(0, np.nan)
    sm = base.ewm(span=21, min_periods=10).mean()
    result = (sm - sm.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapvolratio63rate_21d_slope_v097_signal(open, close):
    g = _f12_gap(open, close)
    tot = close.pct_change()
    base = _std(g, 63) / _std(tot, 63).replace(0, np.nan)
    result = (base - base.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapvolratio63snr_63d_slope_v098_signal(open, close):
    g = _f12_gap(open, close)
    tot = close.pct_change()
    base = _std(g, 63) / _std(tot, 63).replace(0, np.nan)
    chg = base - base.shift(63)
    result = chg / _std(base, 189).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapvolratio63smdf_21d_slope_v099_signal(open, close):
    g = _f12_gap(open, close)
    tot = close.pct_change()
    base = _std(g, 63) / _std(tot, 63).replace(0, np.nan)
    sm = base.ewm(span=21, min_periods=10).mean()
    result = (sm - sm.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_worstgap63rate_21d_slope_v100_signal(open, close):
    g = _f12_gap(open, close)
    base = g.rolling(63, min_periods=21).min()
    result = (base - base.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_worstgap63snr_63d_slope_v101_signal(open, close):
    g = _f12_gap(open, close)
    base = g.rolling(63, min_periods=21).min()
    chg = base - base.shift(63)
    result = chg / _std(base, 189).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_worstgap63smdf_21d_slope_v102_signal(open, close):
    g = _f12_gap(open, close)
    base = g.rolling(63, min_periods=21).min()
    sm = base.ewm(span=21, min_periods=10).mean()
    result = (sm - sm.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_bestgap63rate_21d_slope_v103_signal(open, close):
    g = _f12_gap(open, close)
    base = g.rolling(63, min_periods=21).max()
    result = (base - base.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_bestgap63snr_63d_slope_v104_signal(open, close):
    g = _f12_gap(open, close)
    base = g.rolling(63, min_periods=21).max()
    chg = base - base.shift(63)
    result = chg / _std(base, 189).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_bestgap63smdf_21d_slope_v105_signal(open, close):
    g = _f12_gap(open, close)
    base = g.rolling(63, min_periods=21).max()
    sm = base.ewm(span=21, min_periods=10).mean()
    result = (sm - sm.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gaprange63rate_21d_slope_v106_signal(open, close):
    g = _f12_gap(open, close)
    base = g.rolling(63, min_periods=21).max() - g.rolling(63, min_periods=21).min()
    result = (base - base.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gaprange63snr_63d_slope_v107_signal(open, close):
    g = _f12_gap(open, close)
    base = g.rolling(63, min_periods=21).max() - g.rolling(63, min_periods=21).min()
    chg = base - base.shift(63)
    result = chg / _std(base, 189).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gaprange63smdf_21d_slope_v108_signal(open, close):
    g = _f12_gap(open, close)
    base = g.rolling(63, min_periods=21).max() - g.rolling(63, min_periods=21).min()
    sm = base.ewm(span=21, min_periods=10).mean()
    result = (sm - sm.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_eqdivergerate_21d_slope_v109_signal(open, close):
    on = _f12_overnight_ret(open, close)
    intra = _f12_intraday(open, close)
    base = on.rolling(126, min_periods=63).sum() - intra.rolling(126, min_periods=63).sum()
    result = (base - base.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_eqdivergesnr_63d_slope_v110_signal(open, close):
    on = _f12_overnight_ret(open, close)
    intra = _f12_intraday(open, close)
    base = on.rolling(126, min_periods=63).sum() - intra.rolling(126, min_periods=63).sum()
    chg = base - base.shift(63)
    result = chg / _std(base, 189).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_eqdivergesmdf_21d_slope_v111_signal(open, close):
    on = _f12_overnight_ret(open, close)
    intra = _f12_intraday(open, close)
    base = on.rolling(126, min_periods=63).sum() - intra.rolling(126, min_periods=63).sum()
    sm = base.ewm(span=21, min_periods=10).mean()
    result = (sm - sm.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapvolexprate_21d_slope_v112_signal(open, close):
    g = _f12_gap(open, close)
    base = _std(g, 21) / _std(g, 126).replace(0, np.nan)
    result = (base - base.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapvolexpsnr_63d_slope_v113_signal(open, close):
    g = _f12_gap(open, close)
    base = _std(g, 21) / _std(g, 126).replace(0, np.nan)
    chg = base - base.shift(63)
    result = chg / _std(base, 189).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapvolexpsmdf_21d_slope_v114_signal(open, close):
    g = _f12_gap(open, close)
    base = _std(g, 21) / _std(g, 126).replace(0, np.nan)
    sm = base.ewm(span=21, min_periods=10).mean()
    result = (sm - sm.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gaphhi63rate_21d_slope_v115_signal(open, close):
    g2 = _f12_gap(open, close) ** 2
    tot = g2.rolling(63, min_periods=21).sum()
    share = g2 / tot.replace(0, np.nan)
    base = (share ** 2).rolling(63, min_periods=21).sum()
    result = (base - base.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gaphhi63snr_63d_slope_v116_signal(open, close):
    g2 = _f12_gap(open, close) ** 2
    tot = g2.rolling(63, min_periods=21).sum()
    share = g2 / tot.replace(0, np.nan)
    base = (share ** 2).rolling(63, min_periods=21).sum()
    chg = base - base.shift(63)
    result = chg / _std(base, 189).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gaphhi63smdf_21d_slope_v117_signal(open, close):
    g2 = _f12_gap(open, close) ** 2
    tot = g2.rolling(63, min_periods=21).sum()
    share = g2 / tot.replace(0, np.nan)
    base = (share ** 2).rolling(63, min_periods=21).sum()
    sm = base.ewm(span=21, min_periods=10).mean()
    result = (sm - sm.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_onsharpe63rate_21d_slope_v118_signal(open, close):
    g = _f12_gap(open, close)
    base = g.rolling(63, min_periods=21).kurt()
    result = (base - base.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_onsharpe63snr_63d_slope_v119_signal(open, close):
    g = _f12_gap(open, close)
    base = g.rolling(63, min_periods=21).kurt()
    chg = base - base.shift(63)
    result = chg / _std(base, 189).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_onsharpe63smdf_21d_slope_v120_signal(open, close):
    g = _f12_gap(open, close)
    base = g.rolling(63, min_periods=21).kurt()
    sm = base.ewm(span=21, min_periods=10).mean()
    result = (sm - sm.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_absgaprankrate_21d_slope_v121_signal(open, close):
    ag = _f12_abs_gap(open, close)
    base = ag.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = (base - base.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_absgapranksnr_63d_slope_v122_signal(open, close):
    ag = _f12_abs_gap(open, close)
    base = ag.rolling(252, min_periods=63).rank(pct=True) - 0.5
    chg = base - base.shift(63)
    result = chg / _std(base, 189).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_absgapranksmdf_21d_slope_v123_signal(open, close):
    ag = _f12_abs_gap(open, close)
    base = ag.rolling(252, min_periods=63).rank(pct=True) - 0.5
    sm = base.ewm(span=21, min_periods=10).mean()
    result = (sm - sm.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapledhighrate_21d_slope_v124_signal(open, close):
    g = _f12_gap(open, close)
    at_high = (close >= close.rolling(63, min_periods=21).max() * 0.999).astype(float)
    base = (g * at_high).rolling(63, min_periods=21).sum()
    result = (base - base.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapledhighsnr_63d_slope_v125_signal(open, close):
    g = _f12_gap(open, close)
    at_high = (close >= close.rolling(63, min_periods=21).max() * 0.999).astype(float)
    base = (g * at_high).rolling(63, min_periods=21).sum()
    chg = base - base.shift(63)
    result = chg / _std(base, 189).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapledhighsmdf_21d_slope_v126_signal(open, close):
    g = _f12_gap(open, close)
    at_high = (close >= close.rolling(63, min_periods=21).max() * 0.999).astype(float)
    base = (g * at_high).rolling(63, min_periods=21).sum()
    sm = base.ewm(span=21, min_periods=10).mean()
    result = (sm - sm.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_vwdrift21rate_5d_slope_v127_signal(open, close, volume):
    ag = _f12_abs_gap(open, close)
    base = ag.rolling(21, min_periods=10).corr(volume)
    result = (base - base.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_vwdrift21snr_21d_slope_v128_signal(open, close, volume):
    ag = _f12_abs_gap(open, close)
    base = ag.rolling(21, min_periods=10).corr(volume)
    chg = base - base.shift(21)
    result = chg / _std(base, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_vwdrift21smdf_5d_slope_v129_signal(open, close, volume):
    ag = _f12_abs_gap(open, close)
    base = ag.rolling(21, min_periods=10).corr(volume)
    sm = base.ewm(span=5, min_periods=2).mean()
    result = (sm - sm.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_newsintensityrate_21d_slope_v130_signal(open, close, volume):
    agz = _z(_f12_abs_gap(open, close), 63)
    vz = _z(volume, 63)
    base = (agz * vz).rolling(21, min_periods=10).mean()
    result = (base - base.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_newsintensitysnr_63d_slope_v131_signal(open, close, volume):
    agz = _z(_f12_abs_gap(open, close), 63)
    vz = _z(volume, 63)
    base = (agz * vz).rolling(21, min_periods=10).mean()
    chg = base - base.shift(63)
    result = chg / _std(base, 189).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_newsintensitysmdf_21d_slope_v132_signal(open, close, volume):
    agz = _z(_f12_abs_gap(open, close), 63)
    vz = _z(volume, 63)
    base = (agz * vz).rolling(21, min_periods=10).mean()
    sm = base.ewm(span=21, min_periods=10).mean()
    result = (sm - sm.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapvolcorr63rate_21d_slope_v133_signal(open, close, volume):
    g = _f12_gap(open, close)
    peakvol = (volume == volume.rolling(21, min_periods=10).max()).astype(float)
    base = (g * peakvol).rolling(21, min_periods=10).sum()
    result = (base - base.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapvolcorr63snr_63d_slope_v134_signal(open, close, volume):
    g = _f12_gap(open, close)
    peakvol = (volume == volume.rolling(21, min_periods=10).max()).astype(float)
    base = (g * peakvol).rolling(21, min_periods=10).sum()
    chg = base - base.shift(63)
    result = chg / _std(base, 189).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapvolcorr63smdf_21d_slope_v135_signal(open, close, volume):
    g = _f12_gap(open, close)
    peakvol = (volume == volume.rolling(21, min_periods=10).max()).astype(float)
    base = (g * peakvol).rolling(21, min_periods=10).sum()
    sm = base.ewm(span=21, min_periods=10).mean()
    result = (sm - sm.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_decaygaprate_5d_slope_v136_signal(open, close):
    g = _f12_gap(open, close)
    base = g.ewm(halflife=5, min_periods=5).mean()
    result = (base - base.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_decaygapsnr_21d_slope_v137_signal(open, close):
    g = _f12_gap(open, close)
    base = g.ewm(halflife=5, min_periods=5).mean()
    chg = base - base.shift(21)
    result = chg / _std(base, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_decaygapsmdf_5d_slope_v138_signal(open, close):
    g = _f12_gap(open, close)
    base = g.ewm(halflife=5, min_periods=5).mean()
    sm = base.ewm(span=5, min_periods=2).mean()
    result = (sm - sm.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_absgapdisprate_5d_slope_v139_signal(open, high, low, close):
    pc = close.shift(1)
    gap = open - pc
    filled = (open - low).clip(lower=0.0)
    uf = (filled / gap.replace(0, np.nan)).where(gap > 0, np.nan)
    base = uf.rolling(21, min_periods=5).mean()
    result = (base - base.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_absgapdispsnr_21d_slope_v140_signal(open, high, low, close):
    pc = close.shift(1)
    gap = open - pc
    filled = (open - low).clip(lower=0.0)
    uf = (filled / gap.replace(0, np.nan)).where(gap > 0, np.nan)
    base = uf.rolling(21, min_periods=5).mean()
    chg = base - base.shift(21)
    result = chg / _std(base, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_absgapdispsmdf_5d_slope_v141_signal(open, high, low, close):
    pc = close.shift(1)
    gap = open - pc
    filled = (open - low).clip(lower=0.0)
    uf = (filled / gap.replace(0, np.nan)).where(gap > 0, np.nan)
    base = uf.rolling(21, min_periods=5).mean()
    sm = base.ewm(span=5, min_periods=2).mean()
    result = (sm - sm.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapzpos126rate_21d_slope_v142_signal(open, close):
    g = _f12_gap(open, close)
    gmax = g.rolling(126, min_periods=63).max()
    gmin = g.rolling(126, min_periods=63).min()
    base = (g - gmin) / (gmax - gmin).replace(0, np.nan) - 0.5
    result = (base - base.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapzpos126snr_63d_slope_v143_signal(open, close):
    g = _f12_gap(open, close)
    gmax = g.rolling(126, min_periods=63).max()
    gmin = g.rolling(126, min_periods=63).min()
    base = (g - gmin) / (gmax - gmin).replace(0, np.nan) - 0.5
    chg = base - base.shift(63)
    result = chg / _std(base, 189).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapzpos126smdf_21d_slope_v144_signal(open, close):
    g = _f12_gap(open, close)
    gmax = g.rolling(126, min_periods=63).max()
    gmin = g.rolling(126, min_periods=63).min()
    base = (g - gmin) / (gmax - gmin).replace(0, np.nan) - 0.5
    sm = base.ewm(span=21, min_periods=10).mean()
    result = (sm - sm.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_recentgap21rate_5d_slope_v145_signal(open, high, low, close):
    pc = close.shift(1)
    loc = (close - low) / (high - low).replace(0, np.nan)
    base = loc.rolling(21, min_periods=10).mean() - 0.5
    result = (base - base.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_recentgap21snr_21d_slope_v146_signal(open, high, low, close):
    pc = close.shift(1)
    loc = (close - low) / (high - low).replace(0, np.nan)
    base = loc.rolling(21, min_periods=10).mean() - 0.5
    chg = base - base.shift(21)
    result = chg / _std(base, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_recentgap21smdf_5d_slope_v147_signal(open, high, low, close):
    pc = close.shift(1)
    loc = (close - low) / (high - low).replace(0, np.nan)
    base = loc.rolling(21, min_periods=10).mean() - 0.5
    sm = base.ewm(span=5, min_periods=2).mean()
    result = (sm - sm.shift(5)) / float(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapmedian63rate_21d_slope_v148_signal(open, close):
    ag = _f12_abs_gap(open, close)
    base = ag.rolling(63, min_periods=21).median()
    result = (base - base.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapmedian63snr_63d_slope_v149_signal(open, close):
    ag = _f12_abs_gap(open, close)
    base = ag.rolling(63, min_periods=21).median()
    chg = base - base.shift(63)
    result = chg / _std(base, 189).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

def f12gn_f12_gap_news_shock_gapmedian63smdf_21d_slope_v150_signal(open, close):
    ag = _f12_abs_gap(open, close)
    base = ag.rolling(63, min_periods=21).median()
    sm = base.ewm(span=21, min_periods=10).mean()
    result = (sm - sm.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f12gn_f12_gap_news_shock_gaplvlrate_5d_slope_v001_signal,
    f12gn_f12_gap_news_shock_gaplvlsnr_10d_slope_v002_signal,
    f12gn_f12_gap_news_shock_gaplvlsmdf_5d_slope_v003_signal,
    f12gn_f12_gap_news_shock_absgaprate_5d_slope_v004_signal,
    f12gn_f12_gap_news_shock_absgapsnr_10d_slope_v005_signal,
    f12gn_f12_gap_news_shock_absgapsmdf_5d_slope_v006_signal,
    f12gn_f12_gap_news_shock_intradayrate_5d_slope_v007_signal,
    f12gn_f12_gap_news_shock_intradaysnr_10d_slope_v008_signal,
    f12gn_f12_gap_news_shock_intradaysmdf_5d_slope_v009_signal,
    f12gn_f12_gap_news_shock_onvsintrarate_5d_slope_v010_signal,
    f12gn_f12_gap_news_shock_onvsintrasnr_10d_slope_v011_signal,
    f12gn_f12_gap_news_shock_onvsintrasmdf_5d_slope_v012_signal,
    f12gn_f12_gap_news_shock_loggaprate_5d_slope_v013_signal,
    f12gn_f12_gap_news_shock_loggapsnr_10d_slope_v014_signal,
    f12gn_f12_gap_news_shock_loggapsmdf_5d_slope_v015_signal,
    f12gn_f12_gap_news_shock_gapvsrangerate_5d_slope_v016_signal,
    f12gn_f12_gap_news_shock_gapvsrangesnr_10d_slope_v017_signal,
    f12gn_f12_gap_news_shock_gapvsrangesmdf_5d_slope_v018_signal,
    f12gn_f12_gap_news_shock_truegaprate_5d_slope_v019_signal,
    f12gn_f12_gap_news_shock_truegapsnr_10d_slope_v020_signal,
    f12gn_f12_gap_news_shock_truegapsmdf_5d_slope_v021_signal,
    f12gn_f12_gap_news_shock_openinrangerate_5d_slope_v022_signal,
    f12gn_f12_gap_news_shock_openinrangesnr_10d_slope_v023_signal,
    f12gn_f12_gap_news_shock_openinrangesmdf_5d_slope_v024_signal,
    f12gn_f12_gap_news_shock_gapsigrate_5d_slope_v025_signal,
    f12gn_f12_gap_news_shock_gapsigsnr_10d_slope_v026_signal,
    f12gn_f12_gap_news_shock_gapsigsmdf_5d_slope_v027_signal,
    f12gn_f12_gap_news_shock_breakawayrate_5d_slope_v028_signal,
    f12gn_f12_gap_news_shock_breakawaysnr_10d_slope_v029_signal,
    f12gn_f12_gap_news_shock_breakawaysmdf_5d_slope_v030_signal,
    f12gn_f12_gap_news_shock_cumgap21rate_5d_slope_v031_signal,
    f12gn_f12_gap_news_shock_cumgap21snr_21d_slope_v032_signal,
    f12gn_f12_gap_news_shock_cumgap21smdf_5d_slope_v033_signal,
    f12gn_f12_gap_news_shock_gapstd21rate_5d_slope_v034_signal,
    f12gn_f12_gap_news_shock_gapstd21snr_21d_slope_v035_signal,
    f12gn_f12_gap_news_shock_gapstd21smdf_5d_slope_v036_signal,
    f12gn_f12_gap_news_shock_gapz21rate_5d_slope_v037_signal,
    f12gn_f12_gap_news_shock_gapz21snr_21d_slope_v038_signal,
    f12gn_f12_gap_news_shock_gapz21smdf_5d_slope_v039_signal,
    f12gn_f12_gap_news_shock_absgapema21rate_5d_slope_v040_signal,
    f12gn_f12_gap_news_shock_absgapema21snr_21d_slope_v041_signal,
    f12gn_f12_gap_news_shock_absgapema21smdf_5d_slope_v042_signal,
    f12gn_f12_gap_news_shock_onvol21rate_5d_slope_v043_signal,
    f12gn_f12_gap_news_shock_onvol21snr_21d_slope_v044_signal,
    f12gn_f12_gap_news_shock_onvol21smdf_5d_slope_v045_signal,
    f12gn_f12_gap_news_shock_gapqv21rate_5d_slope_v046_signal,
    f12gn_f12_gap_news_shock_gapqv21snr_21d_slope_v047_signal,
    f12gn_f12_gap_news_shock_gapqv21smdf_5d_slope_v048_signal,
    f12gn_f12_gap_news_shock_vwgap21rate_5d_slope_v049_signal,
    f12gn_f12_gap_news_shock_vwgap21snr_21d_slope_v050_signal,
    f12gn_f12_gap_news_shock_vwgap21smdf_5d_slope_v051_signal,
    f12gn_f12_gap_news_shock_upgapsum21rate_5d_slope_v052_signal,
    f12gn_f12_gap_news_shock_upgapsum21snr_21d_slope_v053_signal,
    f12gn_f12_gap_news_shock_upgapsum21smdf_5d_slope_v054_signal,
    f12gn_f12_gap_news_shock_dngapsum21rate_5d_slope_v055_signal,
    f12gn_f12_gap_news_shock_dngapsum21snr_21d_slope_v056_signal,
    f12gn_f12_gap_news_shock_dngapsum21smdf_5d_slope_v057_signal,
    f12gn_f12_gap_news_shock_maxgap21rate_5d_slope_v058_signal,
    f12gn_f12_gap_news_shock_maxgap21snr_21d_slope_v059_signal,
    f12gn_f12_gap_news_shock_maxgap21smdf_5d_slope_v060_signal,
    f12gn_f12_gap_news_shock_gappurity21rate_5d_slope_v061_signal,
    f12gn_f12_gap_news_shock_gappurity21snr_21d_slope_v062_signal,
    f12gn_f12_gap_news_shock_gappurity21smdf_5d_slope_v063_signal,
    f12gn_f12_gap_news_shock_qvshare21rate_5d_slope_v064_signal,
    f12gn_f12_gap_news_shock_qvshare21snr_21d_slope_v065_signal,
    f12gn_f12_gap_news_shock_qvshare21smdf_5d_slope_v066_signal,
    f12gn_f12_gap_news_shock_onintraspr21rate_5d_slope_v067_signal,
    f12gn_f12_gap_news_shock_onintraspr21snr_21d_slope_v068_signal,
    f12gn_f12_gap_news_shock_onintraspr21smdf_5d_slope_v069_signal,
    f12gn_f12_gap_news_shock_acuteburstrate_5d_slope_v070_signal,
    f12gn_f12_gap_news_shock_acuteburstsnr_21d_slope_v071_signal,
    f12gn_f12_gap_news_shock_acuteburstsmdf_5d_slope_v072_signal,
    f12gn_f12_gap_news_shock_signbal21rate_5d_slope_v073_signal,
    f12gn_f12_gap_news_shock_signbal21snr_21d_slope_v074_signal,
    f12gn_f12_gap_news_shock_signbal21smdf_5d_slope_v075_signal,
    f12gn_f12_gap_news_shock_cumgap63rate_21d_slope_v076_signal,
    f12gn_f12_gap_news_shock_cumgap63snr_63d_slope_v077_signal,
    f12gn_f12_gap_news_shock_cumgap63smdf_21d_slope_v078_signal,
    f12gn_f12_gap_news_shock_gapstd63rate_21d_slope_v079_signal,
    f12gn_f12_gap_news_shock_gapstd63snr_63d_slope_v080_signal,
    f12gn_f12_gap_news_shock_gapstd63smdf_21d_slope_v081_signal,
    f12gn_f12_gap_news_shock_gapskew63rate_21d_slope_v082_signal,
    f12gn_f12_gap_news_shock_gapskew63snr_63d_slope_v083_signal,
    f12gn_f12_gap_news_shock_gapskew63smdf_21d_slope_v084_signal,
    f12gn_f12_gap_news_shock_gapasym63rate_21d_slope_v085_signal,
    f12gn_f12_gap_news_shock_gapasym63snr_63d_slope_v086_signal,
    f12gn_f12_gap_news_shock_gapasym63smdf_21d_slope_v087_signal,
    f12gn_f12_gap_news_shock_ondrift63rate_21d_slope_v088_signal,
    f12gn_f12_gap_news_shock_ondrift63snr_63d_slope_v089_signal,
    f12gn_f12_gap_news_shock_ondrift63smdf_21d_slope_v090_signal,
    f12gn_f12_gap_news_shock_gapbal63rate_21d_slope_v091_signal,
    f12gn_f12_gap_news_shock_gapbal63snr_63d_slope_v092_signal,
    f12gn_f12_gap_news_shock_gapbal63smdf_21d_slope_v093_signal,
    f12gn_f12_gap_news_shock_onintravolr63rate_21d_slope_v094_signal,
    f12gn_f12_gap_news_shock_onintravolr63snr_63d_slope_v095_signal,
    f12gn_f12_gap_news_shock_onintravolr63smdf_21d_slope_v096_signal,
    f12gn_f12_gap_news_shock_gapvolratio63rate_21d_slope_v097_signal,
    f12gn_f12_gap_news_shock_gapvolratio63snr_63d_slope_v098_signal,
    f12gn_f12_gap_news_shock_gapvolratio63smdf_21d_slope_v099_signal,
    f12gn_f12_gap_news_shock_worstgap63rate_21d_slope_v100_signal,
    f12gn_f12_gap_news_shock_worstgap63snr_63d_slope_v101_signal,
    f12gn_f12_gap_news_shock_worstgap63smdf_21d_slope_v102_signal,
    f12gn_f12_gap_news_shock_bestgap63rate_21d_slope_v103_signal,
    f12gn_f12_gap_news_shock_bestgap63snr_63d_slope_v104_signal,
    f12gn_f12_gap_news_shock_bestgap63smdf_21d_slope_v105_signal,
    f12gn_f12_gap_news_shock_gaprange63rate_21d_slope_v106_signal,
    f12gn_f12_gap_news_shock_gaprange63snr_63d_slope_v107_signal,
    f12gn_f12_gap_news_shock_gaprange63smdf_21d_slope_v108_signal,
    f12gn_f12_gap_news_shock_eqdivergerate_21d_slope_v109_signal,
    f12gn_f12_gap_news_shock_eqdivergesnr_63d_slope_v110_signal,
    f12gn_f12_gap_news_shock_eqdivergesmdf_21d_slope_v111_signal,
    f12gn_f12_gap_news_shock_gapvolexprate_21d_slope_v112_signal,
    f12gn_f12_gap_news_shock_gapvolexpsnr_63d_slope_v113_signal,
    f12gn_f12_gap_news_shock_gapvolexpsmdf_21d_slope_v114_signal,
    f12gn_f12_gap_news_shock_gaphhi63rate_21d_slope_v115_signal,
    f12gn_f12_gap_news_shock_gaphhi63snr_63d_slope_v116_signal,
    f12gn_f12_gap_news_shock_gaphhi63smdf_21d_slope_v117_signal,
    f12gn_f12_gap_news_shock_onsharpe63rate_21d_slope_v118_signal,
    f12gn_f12_gap_news_shock_onsharpe63snr_63d_slope_v119_signal,
    f12gn_f12_gap_news_shock_onsharpe63smdf_21d_slope_v120_signal,
    f12gn_f12_gap_news_shock_absgaprankrate_21d_slope_v121_signal,
    f12gn_f12_gap_news_shock_absgapranksnr_63d_slope_v122_signal,
    f12gn_f12_gap_news_shock_absgapranksmdf_21d_slope_v123_signal,
    f12gn_f12_gap_news_shock_gapledhighrate_21d_slope_v124_signal,
    f12gn_f12_gap_news_shock_gapledhighsnr_63d_slope_v125_signal,
    f12gn_f12_gap_news_shock_gapledhighsmdf_21d_slope_v126_signal,
    f12gn_f12_gap_news_shock_vwdrift21rate_5d_slope_v127_signal,
    f12gn_f12_gap_news_shock_vwdrift21snr_21d_slope_v128_signal,
    f12gn_f12_gap_news_shock_vwdrift21smdf_5d_slope_v129_signal,
    f12gn_f12_gap_news_shock_newsintensityrate_21d_slope_v130_signal,
    f12gn_f12_gap_news_shock_newsintensitysnr_63d_slope_v131_signal,
    f12gn_f12_gap_news_shock_newsintensitysmdf_21d_slope_v132_signal,
    f12gn_f12_gap_news_shock_gapvolcorr63rate_21d_slope_v133_signal,
    f12gn_f12_gap_news_shock_gapvolcorr63snr_63d_slope_v134_signal,
    f12gn_f12_gap_news_shock_gapvolcorr63smdf_21d_slope_v135_signal,
    f12gn_f12_gap_news_shock_decaygaprate_5d_slope_v136_signal,
    f12gn_f12_gap_news_shock_decaygapsnr_21d_slope_v137_signal,
    f12gn_f12_gap_news_shock_decaygapsmdf_5d_slope_v138_signal,
    f12gn_f12_gap_news_shock_absgapdisprate_5d_slope_v139_signal,
    f12gn_f12_gap_news_shock_absgapdispsnr_21d_slope_v140_signal,
    f12gn_f12_gap_news_shock_absgapdispsmdf_5d_slope_v141_signal,
    f12gn_f12_gap_news_shock_gapzpos126rate_21d_slope_v142_signal,
    f12gn_f12_gap_news_shock_gapzpos126snr_63d_slope_v143_signal,
    f12gn_f12_gap_news_shock_gapzpos126smdf_21d_slope_v144_signal,
    f12gn_f12_gap_news_shock_recentgap21rate_5d_slope_v145_signal,
    f12gn_f12_gap_news_shock_recentgap21snr_21d_slope_v146_signal,
    f12gn_f12_gap_news_shock_recentgap21smdf_5d_slope_v147_signal,
    f12gn_f12_gap_news_shock_gapmedian63rate_21d_slope_v148_signal,
    f12gn_f12_gap_news_shock_gapmedian63snr_63d_slope_v149_signal,
    f12gn_f12_gap_news_shock_gapmedian63smdf_21d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F12_GAP_NEWS_SHOCK_REGISTRY_2ND_001_150 = REGISTRY


if __name__ == "__main__":  # noqa
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

    print("OK f12_gap_news_shock_2nd_derivatives_001_150_claude: %d features pass" % n_features)
