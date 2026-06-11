import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
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


def _ewm(s, span):
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _rng(high, low):
    return (high - low)


def _body_ratio(open, high, low, close):
    r = (high - low).replace(0, np.nan)
    return (close - open).abs() / r


def _upper_ratio(open, high, low, close):
    r = (high - low).replace(0, np.nan)
    return (high - np.maximum(open, close)) / r


def _lower_ratio(open, high, low, close):
    r = (high - low).replace(0, np.nan)
    return (np.minimum(open, close) - low) / r


def _close_pos(high, low, close):
    r = (high - low).replace(0, np.nan)
    return (close - low) / r


def _open_pos(open, high, low):
    r = (high - low).replace(0, np.nan)
    return (open - low) / r


def _true_range(high, low, close):
    pc = close.shift(1)
    a = high - low
    b = (high - pc).abs()
    c = (low - pc).abs()
    return pd.concat([a, b, c], axis=1).max(axis=1)


def f08cr_f08_candle_range_structure_bodyrat_21d_jerk_v001_signal(open, high, low, close):
    m = _mean(_body_ratio(open, high, low, close), 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_uwick_21d_jerk_v002_signal(open, high, low, close):
    m = _mean(_upper_ratio(open, high, low, close), 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_lwick_21d_jerk_v003_signal(open, high, low, close):
    m = _mean(_lower_ratio(open, high, low, close), 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_wickasym_21d_jerk_v004_signal(open, high, low, close):
    m = _mean(_lower_ratio(open, high, low, close) - _upper_ratio(open, high, low, close), 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_closepos_21d_jerk_v005_signal(open, high, low, close):
    m = _mean(_close_pos(high, low, close), 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_openpos_21d_jerk_v006_signal(open, high, low, close):
    m = _mean(_open_pos(open, high, low), 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_hlrng_21d_jerk_v007_signal(open, high, low, close):
    m = _mean(_rng(high, low) / close.replace(0, np.nan), 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_rngvsbody_21d_jerk_v008_signal(open, high, low, close):
    m = _mean(_rng(high, low) / (close - open).abs().replace(0, np.nan), 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_bodyamp_21d_jerk_v009_signal(open, high, low, close):
    m = _mean((close - open) / close.replace(0, np.nan), 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_closebias_63d_jerk_v010_signal(open, high, low, close):
    cp = _close_pos(high, low, close)
    m = (cp.rolling(63, min_periods=21).mean() - cp.rolling(63, min_periods=21).median())
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_convdir_21d_jerk_v011_signal(open, high, low, close):
    m = _mean(np.sign(close - open) * _body_ratio(open, high, low, close), 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_netpress_21d_jerk_v012_signal(open, high, low, close):
    m = _mean((2.0 * _close_pos(high, low, close) - 1.0) * _body_ratio(open, high, low, close), 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_upexplorestd_63d_jerk_v013_signal(open, high, low, close):
    v = (high - open) / _rng(high, low).replace(0, np.nan)
    m = v.rolling(63, min_periods=21).std()
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_c2cvbody_21d_jerk_v014_signal(open, high, low, close):
    c2c = (close - close.shift(1)).abs()
    body = (close - open).abs()
    m = _mean(body / (body + c2c).replace(0, np.nan), 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_uwickbody_21d_jerk_v015_signal(open, high, low, close):
    m = _mean(np.log1p((high - np.maximum(open, close)).clip(lower=0) / (close - open).abs().replace(0, np.nan)), 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_bodyratz_63d_jerk_v016_signal(open, high, low, close):
    m = _z(_body_ratio(open, high, low, close), 63)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_closeposz_63d_jerk_v017_signal(open, high, low, close):
    m = _z(_close_pos(high, low, close), 63)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_uwickz_63d_jerk_v018_signal(open, high, low, close):
    m = _z(_upper_ratio(open, high, low, close), 63)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_lwickz_63d_jerk_v019_signal(open, high, low, close):
    m = _z(_lower_ratio(open, high, low, close), 63)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_bodyz_63d_jerk_v020_signal(open, high, low, close):
    m = _z((close - open).abs(), 63)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_rngz_63d_jerk_v021_signal(open, high, low, close):
    m = _z(_rng(high, low), 63)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_wickasymz_63d_jerk_v022_signal(open, high, low, close):
    m = _z(_lower_ratio(open, high, low, close) - _upper_ratio(open, high, low, close), 63)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_bodyratdisp_63d_jerk_v023_signal(open, high, low, close):
    m = _std(_body_ratio(open, high, low, close), 63)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_closeposdisp_63d_jerk_v024_signal(open, high, low, close):
    m = _std(_close_pos(high, low, close), 63)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_rngcv_63d_jerk_v025_signal(open, high, low, close):
    m = _std(_rng(high, low), 63) / _mean(_rng(high, low), 63).replace(0, np.nan)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_bodycv_63d_jerk_v026_signal(open, high, low, close):
    m = _std((close - open).abs(), 63) / _mean((close - open).abs(), 63).replace(0, np.nan)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_dircohesion_63d_jerk_v027_signal(open, high, low, close):
    m = _mean(np.sign(close - open), 63).abs()
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_bigdayclose_63d_jerk_v028_signal(open, high, low, close):
    m = _mean((_close_pos(high, low, close) - 0.5) * _z(_rng(high, low), 63), 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_updnbodyasym_63d_jerk_v029_signal(open, high, low, close):
    br = _body_ratio(open, high, low, close)
    up = (close > open)
    m = _mean(br.where(up), 63) - _mean(br.where(~up), 63)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_churn_63d_jerk_v030_signal(open, high, low, close):
    m = _mean(_z(_rng(high, low), 63) * (1.0 - _body_ratio(open, high, low, close)), 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_gapshare_21d_jerk_v031_signal(open, high, low, close):
    tr = _true_range(high, low, close)
    m = _mean((tr - _rng(high, low)) / tr.replace(0, np.nan), 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_overnshare_21d_jerk_v032_signal(open, high, low, close):
    ov = (open - close.shift(1)).abs()
    intr = _rng(high, low)
    m = _mean(ov / (ov + intr).replace(0, np.nan), 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_bodyharm_21d_jerk_v033_signal(open, high, low, close):
    br = _body_ratio(open, high, low, close).clip(lower=1e-4)
    m = 1.0 / _mean(1.0 / br, 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_wicksym_21d_jerk_v034_signal(open, high, low, close):
    m = _mean(4.0 * _upper_ratio(open, high, low, close) * _lower_ratio(open, high, low, close), 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_trendbar_63d_jerk_v035_signal(open, high, low, close):
    m = (_body_ratio(open, high, low, close) - 0.5).clip(lower=0).rolling(63, min_periods=21).mean()
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_marubozu_63d_jerk_v036_signal(open, high, low, close):
    m = (_body_ratio(open, high, low, close) - 0.8).clip(lower=0).rolling(63, min_periods=21).mean()
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_dojisoft_63d_jerk_v037_signal(open, high, low, close):
    m = ((0.25 - _body_ratio(open, high, low, close)).clip(lower=0) / 0.25).rolling(63, min_periods=21).mean()
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_rngconc_21d_jerk_v038_signal(open, high, low, close):
    rng = _rng(high, low)
    m = _mean(rng / rng.rolling(5, min_periods=3).sum().replace(0, np.nan), 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_bodyconc_21d_jerk_v039_signal(open, high, low, close):
    ba = (close - open).abs()
    m = _mean(ba / ba.rolling(5, min_periods=3).sum().replace(0, np.nan), 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_topbody_63d_jerk_v040_signal(open, high, low, close):
    rng = _rng(high, low).replace(0, np.nan)
    pos = ((open + close) / 2.0 - low) / rng
    m = (pos - 0.5).clip(lower=0).rolling(63, min_periods=21).mean()
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_wclosepos_21d_jerk_v041_signal(open, high, low, close):
    rng = _rng(high, low).replace(0, np.nan)
    wc = (open + high + low + 2.0 * close) / 5.0
    m = _mean((wc - low) / rng - 0.5, 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_bodymidabs_63d_jerk_v042_signal(open, high, low, close):
    rng = _rng(high, low).replace(0, np.nan)
    v = (((open + close) / 2.0 - (high + low) / 2.0) / rng).abs()
    m = _mean(v, 63)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_strongup_63d_jerk_v043_signal(open, high, low, close):
    cp = _close_pos(high, low, close)
    up = (close > open)
    m = (cp - 0.75).clip(lower=0).where(up, 0.0).rolling(63, min_periods=21).mean()
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_strongdn_63d_jerk_v044_signal(open, high, low, close):
    cp = _close_pos(high, low, close)
    dn = (close < open)
    m = (0.25 - cp).clip(lower=0).where(dn, 0.0).rolling(63, min_periods=21).mean()
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_uprejtail_63d_jerk_v045_signal(open, high, low, close):
    uw = _upper_ratio(open, high, low, close)
    lw = _lower_ratio(open, high, low, close)
    up = (close > open)
    m = _mean((uw - lw).where(up), 63)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_dnsupptail_63d_jerk_v046_signal(open, high, low, close):
    uw = _upper_ratio(open, high, low, close)
    lw = _lower_ratio(open, high, low, close)
    dn = (close < open)
    m = _mean((lw - uw).where(dn), 63)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_riskadjbody_63d_jerk_v047_signal(open, high, low, close):
    amp = (close - open) / close.replace(0, np.nan)
    m = _ewm(amp, 21) / _std(amp, 63).replace(0, np.nan)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_gapmag_21d_jerk_v048_signal(open, high, low, close):
    ov = (open - close.shift(1)).abs() / close.shift(1).replace(0, np.nan)
    m = _mean(ov, 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_candlestr_21d_jerk_v049_signal(open, high, low, close):
    br = _body_ratio(open, high, low, close)
    uw = _upper_ratio(open, high, low, close)
    lw = _lower_ratio(open, high, low, close)
    raw = np.sign(close - open) * br - (uw - lw)
    m = _ewm(_mean(raw, 5), 11)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_bodyratema_21d_jerk_v050_signal(open, high, low, close):
    m = _ewm(_body_ratio(open, high, low, close), 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_closeposema_21d_jerk_v051_signal(open, high, low, close):
    m = _ewm(_close_pos(high, low, close), 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_uwickema_21d_jerk_v052_signal(open, high, low, close):
    m = _ewm(_upper_ratio(open, high, low, close), 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_lwickema_21d_jerk_v053_signal(open, high, low, close):
    m = _ewm(_lower_ratio(open, high, low, close), 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_rngema_21d_jerk_v054_signal(open, high, low, close):
    m = _ewm(_rng(high, low) / close.replace(0, np.nan), 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_bodyratmed_21d_jerk_v055_signal(open, high, low, close):
    m = _body_ratio(open, high, low, close).rolling(21, min_periods=10).median()
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_closeposmed_21d_jerk_v056_signal(open, high, low, close):
    m = _close_pos(high, low, close).rolling(21, min_periods=10).median()
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_rngmed_21d_jerk_v057_signal(open, high, low, close):
    m = (_rng(high, low) / close.replace(0, np.nan)).rolling(21, min_periods=10).median()
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_uptopfreq_63d_jerk_v058_signal(open, high, low, close):
    cp = _close_pos(high, low, close)
    f = (cp >= 0.9).astype(float)
    m = _ewm(f.rolling(63, min_periods=21).mean(), 8)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_dnbotfreq_63d_jerk_v059_signal(open, high, low, close):
    cp = _close_pos(high, low, close)
    f = (cp <= 0.1).astype(float)
    m = _ewm(f.rolling(63, min_periods=21).mean(), 8)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_uwexcess_63d_jerk_v060_signal(open, high, low, close):
    m = (_upper_ratio(open, high, low, close) - 0.5).clip(lower=0).rolling(63, min_periods=21).mean()
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_lwexcess_63d_jerk_v061_signal(open, high, low, close):
    m = (_lower_ratio(open, high, low, close) - 0.5).clip(lower=0).rolling(63, min_periods=21).mean()
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_rngexpand_21d_jerk_v062_signal(open, high, low, close):
    rng = _rng(high, low)
    m = rng / _mean(rng, 21).replace(0, np.nan) - 1.0
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_rngexpand63_63d_jerk_v063_signal(open, high, low, close):
    rng = _rng(high, low)
    m = _mean(rng / _mean(rng, 63).replace(0, np.nan), 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_bodyexpand_21d_jerk_v064_signal(open, high, low, close):
    ba = (close - open).abs()
    m = ba / _mean(ba, 21).replace(0, np.nan) - 1.0
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_signrngexp_21d_jerk_v065_signal(open, high, low, close):
    rng = _rng(high, low)
    exp = rng / _mean(rng, 21).replace(0, np.nan) - 1.0
    m = _mean(np.sign(close - open) * exp, 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_convrngz_21d_jerk_v066_signal(open, high, low, close):
    m = _mean(np.sign(close - open) * _z(_rng(high, low), 63), 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_bodyatr_21d_jerk_v067_signal(open, high, low, close):
    tr = _true_range(high, low, close)
    m = _mean((close - open).abs() / _mean(tr, 21).replace(0, np.nan), 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_atrslope_63d_jerk_v068_signal(open, high, low, close):
    tr = _true_range(high, low, close)
    atr = _mean(tr / close.replace(0, np.nan), 21)
    m = atr / atr.shift(21) - 1.0
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_cleaneff_63d_jerk_v069_signal(open, high, low, close):
    body = (close - open)
    rng = _rng(high, low)
    m = body.rolling(63, min_periods=21).sum().abs() / rng.rolling(63, min_periods=21).sum().replace(0, np.nan)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_typpos2_63d_jerk_v070_signal(open, high, low, close):
    rng = _rng(high, low).replace(0, np.nan)
    typ = (high + low + close) / 3.0
    m = _mean((typ - low) / rng, 63)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_hhhl_63d_jerk_v071_signal(open, high, low, close):
    both = ((high > high.shift(1)) & (low > low.shift(1))).astype(float)
    m = _ewm(both.rolling(63, min_periods=21).mean(), 10)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_lhll_63d_jerk_v072_signal(open, high, low, close):
    both = ((high < high.shift(1)) & (low < low.shift(1))).astype(float)
    m = _ewm(both.rolling(63, min_periods=21).mean(), 10)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_insidebar_63d_jerk_v073_signal(open, high, low, close):
    ins = ((high <= high.shift(1)) & (low >= low.shift(1))).astype(float)
    m = _ewm(ins.rolling(63, min_periods=21).mean(), 8)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_outsidebar_63d_jerk_v074_signal(open, high, low, close):
    out = ((high >= high.shift(1)) & (low <= low.shift(1))).astype(float)
    m = _ewm(out.rolling(63, min_periods=21).mean(), 8)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_closeoverph_63d_jerk_v075_signal(open, high, low, close):
    ov = (close > high.shift(1)).astype(float)
    m = _ewm(ov.rolling(63, min_periods=21).mean(), 8)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_closeunderpl_63d_jerk_v076_signal(open, high, low, close):
    un = (close < low.shift(1)).astype(float)
    m = _ewm(un.rolling(63, min_periods=21).mean(), 8)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_bodyescalate_63d_jerk_v077_signal(open, high, low, close):
    ba = (close - open).abs()
    esc = (ba > ba.shift(1)).astype(float)
    m = _ewm(esc.rolling(63, min_periods=21).mean() - 0.5, 8)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_rngescalate_63d_jerk_v078_signal(open, high, low, close):
    rng = _rng(high, low)
    esc = (rng > rng.shift(1)).astype(float)
    m = _ewm(esc.rolling(63, min_periods=21).mean() - 0.5, 8)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_explorebal_21d_jerk_v079_signal(open, high, low, close):
    rng = _rng(high, low).replace(0, np.nan)
    m = _mean(4.0 * (high - open) / rng * (open - low) / rng, 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_openposextreme_63d_jerk_v080_signal(open, high, low, close):
    rng = _rng(high, low).replace(0, np.nan)
    op = (open - low) / rng
    ext = ((op - 0.5).abs() >= 0.4).astype(float)
    m = _ewm(ext.rolling(63, min_periods=21).mean(), 8)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_exploreasymrank_126d_jerk_v081_signal(open, high, low, close):
    rng = _rng(high, low).replace(0, np.nan)
    v = (high - open) / rng - (open - low) / rng
    m = _mean(v, 21).rolling(126, min_periods=63).rank(pct=True) - 0.5
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_bodycloseprod63_63d_jerk_v082_signal(open, high, low, close):
    v = _body_ratio(open, high, low, close) * (_close_pos(high, low, close) - 0.5)
    m = v.rolling(63, min_periods=21).std()
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_uwlwlog_21d_jerk_v083_signal(open, high, low, close):
    uw = (high - np.maximum(open, close)).clip(lower=0) + 1e-6
    lw = (np.minimum(open, close) - low).clip(lower=0) + 1e-6
    m = _mean(np.log(uw / lw), 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_lwickbody_21d_jerk_v084_signal(open, high, low, close):
    lw = (np.minimum(open, close) - low).clip(lower=0)
    ba = (close - open).abs().replace(0, np.nan)
    m = _mean(np.log1p(lw / ba), 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_contmag_63d_jerk_v085_signal(open, high, low, close):
    amp = (close - open) / close.replace(0, np.nan)
    ag = np.sign(amp) * np.sign(amp.shift(1)) * (amp.abs() + amp.shift(1).abs())
    m = _mean(ag, 63)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_trendcont_63d_jerk_v086_signal(open, high, low, close):
    cont = (np.sign(close - close.shift(1)) == np.sign(close - open)).astype(float)
    m = _ewm(cont.rolling(63, min_periods=21).mean() - 0.5, 8)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_gapfade_63d_jerk_v087_signal(open, high, low, close):
    gap = open - close.shift(1)
    intr = close - open
    fade = (np.sign(gap) * np.sign(intr) < 0).astype(float)
    m = _ewm(fade.rolling(63, min_periods=21).mean() - 0.5, 8)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_gapcontmag_63d_jerk_v088_signal(open, high, low, close):
    gap = (open - close.shift(1)) / close.shift(1).replace(0, np.nan)
    intr = (close - open) / open.replace(0, np.nan)
    m = _mean(np.sign(gap) * intr, 63)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_uphit_63d_jerk_v089_signal(open, high, low, close):
    up = (close > open).astype(float)
    m = _ewm(up.rolling(63, min_periods=21).mean() - 0.5, 10)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_dirpersist_63d_jerk_v090_signal(open, high, low, close):
    d = np.sign(close - open)
    same = (d * d.shift(1) > 0).astype(float)
    m = _ewm(same.rolling(63, min_periods=21).mean() - 0.5, 8)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_upstreak_63d_jerk_v091_signal(open, high, low, close):
    up = (close > open).astype(float)
    grp = (up == 0).cumsum()
    st = up.groupby(grp).cumsum()
    m = _ewm(st, 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_downstreak_63d_jerk_v092_signal(open, high, low, close):
    dn = (close < open).astype(float)
    grp = (dn == 0).cumsum()
    st = dn.groupby(grp).cumsum()
    m = _ewm(st, 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_rngexpstreak_63d_jerk_v093_signal(open, high, low, close):
    rng = _rng(high, low)
    exp = (rng > _mean(rng, 21)).astype(float)
    grp = (exp == 0).cumsum()
    st = exp.groupby(grp).cumsum()
    m = _ewm(st, 15)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_bodyautocorr_63d_jerk_v094_signal(open, high, low, close):
    br = _body_ratio(open, high, low, close)
    m = _ewm(br, 5).rolling(63, min_periods=30).corr(_ewm(br, 5).shift(1))
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_rngautocorr_63d_jerk_v095_signal(open, high, low, close):
    rng = _ewm(_rng(high, low) / close.replace(0, np.nan), 5)
    m = rng.rolling(63, min_periods=30).corr(rng.shift(1))
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_bodyfat_63d_jerk_v096_signal(open, high, low, close):
    amp = (close - open) / close.replace(0, np.nan)
    m = amp.rolling(63, min_periods=21).kurt()
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_rngskew_63d_jerk_v097_signal(open, high, low, close):
    rng = _rng(high, low) / close.replace(0, np.nan)
    m = rng.rolling(63, min_periods=21).skew()
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_closeposskew_63d_jerk_v098_signal(open, high, low, close):
    m = _close_pos(high, low, close).rolling(63, min_periods=21).skew()
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_bodyratskew_63d_jerk_v099_signal(open, high, low, close):
    m = _body_ratio(open, high, low, close).rolling(63, min_periods=21).skew()
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_whipsaw_63d_jerk_v100_signal(open, high, low, close):
    amp = (close - open) / close.replace(0, np.nan)
    big = amp.abs() > _std(amp, 63)
    opp = (np.sign(amp) * np.sign(amp.shift(1)) < 0)
    w = (big & big.shift(1) & opp).astype(float)
    m = _ewm(w.rolling(63, min_periods=21).mean(), 8)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_rngmaxrel_63d_jerk_v101_signal(open, high, low, close):
    rng = _rng(high, low) / close.replace(0, np.nan)
    m = rng.rolling(63, min_periods=21).max() / _mean(rng, 63).replace(0, np.nan)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_rngminrel_63d_jerk_v102_signal(open, high, low, close):
    rng = _rng(high, low) / close.replace(0, np.nan)
    m = rng.rolling(63, min_periods=21).min() / _mean(rng, 63).replace(0, np.nan)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_bodyrange5_21d_jerk_v103_signal(open, high, low, close):
    ba = (close - open).abs()
    m = _mean(ba / ba.rolling(5, min_periods=3).max().replace(0, np.nan), 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_rngrange5_21d_jerk_v104_signal(open, high, low, close):
    rng = _rng(high, low)
    m = _mean(rng / rng.rolling(5, min_periods=3).max().replace(0, np.nan), 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_netpressew_21d_jerk_v105_signal(open, high, low, close):
    cp = _close_pos(high, low, close)
    br = _body_ratio(open, high, low, close)
    m = _ewm((2.0 * cp - 1.0) * br, 12)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_convdirew_21d_jerk_v106_signal(open, high, low, close):
    m = _ewm(np.sign(close - open) * _body_ratio(open, high, low, close), 12)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_wicknetstd_63d_jerk_v107_signal(open, high, low, close):
    uw = _upper_ratio(open, high, low, close)
    lw = _lower_ratio(open, high, low, close)
    m = (lw - uw).rolling(63, min_periods=21).std()
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_bodysignmag_21d_jerk_v108_signal(open, high, low, close):
    amp = (close - open) / close.replace(0, np.nan)
    m = _mean(np.sign(amp) * amp.abs() ** 0.5, 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_closeposextreme_63d_jerk_v109_signal(open, high, low, close):
    cp = _close_pos(high, low, close)
    ext = ((cp - 0.5).abs() >= 0.4).astype(float)
    m = _ewm(ext.rolling(63, min_periods=21).mean(), 8)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_rngspike_63d_jerk_v110_signal(open, high, low, close):
    rng = _rng(high, low)
    spike = (rng > 1.5 * _mean(rng, 21)).astype(float)
    m = _ewm(spike.rolling(63, min_periods=21).mean(), 8)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_parkinson_63d_jerk_v111_signal(open, high, low, close):
    lr = np.log(high.replace(0, np.nan) / low.replace(0, np.nan)) ** 2
    m = (lr.rolling(63, min_periods=21).mean() / (4.0 * np.log(2.0))) ** 0.5
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_bodyratmax_63d_jerk_v112_signal(open, high, low, close):
    v = _body_ratio(open, high, low, close)
    m = _ewm(v.rolling(63, min_periods=21).max(), 8)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_highclose_21d_jerk_v113_signal(open, high, low, close):
    m = _mean((high - close) / close.replace(0, np.nan), 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_closelow_21d_jerk_v114_signal(open, high, low, close):
    m = _mean((close - low) / close.replace(0, np.nan), 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_ocstd_63d_jerk_v115_signal(open, high, low, close):
    v = (close - open) / open.replace(0, np.nan)
    m = v.rolling(63, min_periods=21).std()
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_bodyrng126_126d_jerk_v116_signal(open, high, low, close):
    m = _mean(_body_ratio(open, high, low, close), 126)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_closepos126_126d_jerk_v117_signal(open, high, low, close):
    m = _mean(_close_pos(high, low, close), 126)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_uwick126_126d_jerk_v118_signal(open, high, low, close):
    m = _mean(_upper_ratio(open, high, low, close), 126)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_lwick126_126d_jerk_v119_signal(open, high, low, close):
    m = _mean(_lower_ratio(open, high, low, close), 126)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_rng126_126d_jerk_v120_signal(open, high, low, close):
    m = _mean(_rng(high, low) / close.replace(0, np.nan), 126)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_wickasym126_126d_jerk_v121_signal(open, high, low, close):
    m = _mean(_lower_ratio(open, high, low, close) - _upper_ratio(open, high, low, close), 126)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_bodyrng5_5d_jerk_v122_signal(open, high, low, close):
    m = _mean(_body_ratio(open, high, low, close), 5)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_closepos5_5d_jerk_v123_signal(open, high, low, close):
    m = _mean(_close_pos(high, low, close), 5)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_rng5_5d_jerk_v124_signal(open, high, low, close):
    m = _mean(_rng(high, low) / close.replace(0, np.nan), 5)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_wickasym5_5d_jerk_v125_signal(open, high, low, close):
    m = _mean(_lower_ratio(open, high, low, close) - _upper_ratio(open, high, low, close), 5)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_bodyamp5_5d_jerk_v126_signal(open, high, low, close):
    m = _mean((close - open) / close.replace(0, np.nan), 5)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_uwbig_63d_jerk_v127_signal(open, high, low, close):
    uw = _upper_ratio(open, high, low, close)
    m = _ewm(uw.rolling(63, min_periods=21).max(), 10)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_lwbig_63d_jerk_v128_signal(open, high, low, close):
    lw = _lower_ratio(open, high, low, close)
    m = _ewm(lw.rolling(63, min_periods=21).max(), 10)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_bigrngclose_63d_jerk_v129_signal(open, high, low, close):
    cp = _close_pos(high, low, close)
    rng = _rng(high, low)
    big = (rng >= _mean(rng, 63))
    m = _mean((cp - 0.5).where(big), 63)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_smallrngclose_63d_jerk_v130_signal(open, high, low, close):
    cp = _close_pos(high, low, close)
    rng = _rng(high, low)
    small = (rng < _mean(rng, 63))
    m = _mean((cp - 0.5).where(small), 63)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_updnrngasym_63d_jerk_v131_signal(open, high, low, close):
    rng = _rng(high, low) / close.replace(0, np.nan)
    up = (close > open)
    m = _mean(rng.where(up), 63) - _mean(rng.where(~up), 63)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_dojibreak_63d_jerk_v132_signal(open, high, low, close):
    br = _body_ratio(open, high, low, close)
    tr = ((br.shift(1) <= 0.2) & (br >= 0.6)).astype(float)
    m = _ewm(tr.rolling(63, min_periods=21).mean(), 8)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_wclosehilo_63d_jerk_v133_signal(open, high, low, close):
    rng = _rng(high, low).replace(0, np.nan)
    typ = (high + low + 2.0 * close) / 4.0
    pos = (typ - low) / rng
    m = _ewm(pos.rolling(63, min_periods=21).max() - pos.rolling(63, min_periods=21).min(), 8)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_bodyposrange_63d_jerk_v134_signal(open, high, low, close):
    rng = _rng(high, low).replace(0, np.nan)
    m = _mean(((open + close) / 2.0 - low) / rng - 0.5, 63)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_rngvov_63d_jerk_v135_signal(open, high, low, close):
    rng = _rng(high, low) / close.replace(0, np.nan)
    dev = (rng - _ewm(rng, 21)).abs()
    m = _ewm(dev, 21) / _ewm(rng, 21).replace(0, np.nan)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_bodyvov_63d_jerk_v136_signal(open, high, low, close):
    br = _body_ratio(open, high, low, close)
    dev = (br - _ewm(br, 21)).abs()
    m = _ewm(dev, 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_closetypprem_63d_jerk_v137_signal(open, high, low, close):
    rng = _rng(high, low).replace(0, np.nan)
    cp = (close - low) / rng
    bm = ((open + close) / 2.0 - low) / rng
    m = (cp - bm).rolling(63, min_periods=21).std()
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_rngconvz_63d_jerk_v138_signal(open, high, low, close):
    br = _body_ratio(open, high, low, close)
    rng = _rng(high, low)
    rr = rng / _mean(rng, 63).replace(0, np.nan)
    m = _z(_mean(br * rr, 5), 63)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_intraeff_21d_jerk_v139_signal(open, high, low, close):
    rng = _rng(high, low).replace(0, np.nan)
    up = (close >= open)
    uw = high - np.maximum(open, close)
    lw = np.minimum(open, close) - low
    opp = uw.where(up, lw)
    m = _mean(opp / rng, 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_hlrnglog_63d_jerk_v140_signal(open, high, low, close):
    m = _mean(np.log1p(_rng(high, low) / close.replace(0, np.nan)), 63)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_closeposiqr_63d_jerk_v141_signal(open, high, low, close):
    cp = _close_pos(high, low, close)
    m = cp.rolling(63, min_periods=21).quantile(0.8) - cp.rolling(63, min_periods=21).quantile(0.2)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_bodyiqr_63d_jerk_v142_signal(open, high, low, close):
    br = _body_ratio(open, high, low, close)
    m = br.rolling(63, min_periods=21).quantile(0.8) - br.rolling(63, min_periods=21).quantile(0.2)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_upmove_21d_jerk_v143_signal(open, high, low, close):
    m = _mean((high - np.maximum(open, close)) / close.replace(0, np.nan), 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_dnmove_21d_jerk_v144_signal(open, high, low, close):
    m = _mean((np.minimum(open, close) - low) / close.replace(0, np.nan), 21)
    m = _ewm(m, 7)
    d1 = m - m.shift(5)
    d = d1 - d1.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_rngmeanmed_63d_jerk_v145_signal(open, high, low, close):
    rng = _rng(high, low) / close.replace(0, np.nan)
    m = _mean(rng, 63) - rng.rolling(63, min_periods=21).median()
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_bodysignedrank_126d_jerk_v146_signal(open, high, low, close):
    v = (close - open) / (high - low).replace(0, np.nan)
    m = _mean(v, 21).rolling(126, min_periods=63).rank(pct=True) - 0.5
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_closeposkurt_63d_jerk_v147_signal(open, high, low, close):
    cp = _close_pos(high, low, close)
    m = cp.rolling(63, min_periods=21).kurt()
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_bodyratmin_63d_jerk_v148_signal(open, high, low, close):
    v = _body_ratio(open, high, low, close)
    m = _ewm(v.rolling(63, min_periods=21).min(), 8)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_rngzpos_63d_jerk_v149_signal(open, high, low, close):
    m = _z(_rng(high, low) / close.replace(0, np.nan), 63)
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f08cr_f08_candle_range_structure_bodyrng126skew_126d_jerk_v150_signal(open, high, low, close):
    v = (close - open).abs() / close.replace(0, np.nan)
    m = v.rolling(126, min_periods=63).skew()
    m = _ewm(m, 7)
    d1 = m - m.shift(21)
    d = d1 - d1.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f08cr_f08_candle_range_structure_bodyrat_21d_jerk_v001_signal,
    f08cr_f08_candle_range_structure_uwick_21d_jerk_v002_signal,
    f08cr_f08_candle_range_structure_lwick_21d_jerk_v003_signal,
    f08cr_f08_candle_range_structure_wickasym_21d_jerk_v004_signal,
    f08cr_f08_candle_range_structure_closepos_21d_jerk_v005_signal,
    f08cr_f08_candle_range_structure_openpos_21d_jerk_v006_signal,
    f08cr_f08_candle_range_structure_hlrng_21d_jerk_v007_signal,
    f08cr_f08_candle_range_structure_rngvsbody_21d_jerk_v008_signal,
    f08cr_f08_candle_range_structure_bodyamp_21d_jerk_v009_signal,
    f08cr_f08_candle_range_structure_closebias_63d_jerk_v010_signal,
    f08cr_f08_candle_range_structure_convdir_21d_jerk_v011_signal,
    f08cr_f08_candle_range_structure_netpress_21d_jerk_v012_signal,
    f08cr_f08_candle_range_structure_upexplorestd_63d_jerk_v013_signal,
    f08cr_f08_candle_range_structure_c2cvbody_21d_jerk_v014_signal,
    f08cr_f08_candle_range_structure_uwickbody_21d_jerk_v015_signal,
    f08cr_f08_candle_range_structure_bodyratz_63d_jerk_v016_signal,
    f08cr_f08_candle_range_structure_closeposz_63d_jerk_v017_signal,
    f08cr_f08_candle_range_structure_uwickz_63d_jerk_v018_signal,
    f08cr_f08_candle_range_structure_lwickz_63d_jerk_v019_signal,
    f08cr_f08_candle_range_structure_bodyz_63d_jerk_v020_signal,
    f08cr_f08_candle_range_structure_rngz_63d_jerk_v021_signal,
    f08cr_f08_candle_range_structure_wickasymz_63d_jerk_v022_signal,
    f08cr_f08_candle_range_structure_bodyratdisp_63d_jerk_v023_signal,
    f08cr_f08_candle_range_structure_closeposdisp_63d_jerk_v024_signal,
    f08cr_f08_candle_range_structure_rngcv_63d_jerk_v025_signal,
    f08cr_f08_candle_range_structure_bodycv_63d_jerk_v026_signal,
    f08cr_f08_candle_range_structure_dircohesion_63d_jerk_v027_signal,
    f08cr_f08_candle_range_structure_bigdayclose_63d_jerk_v028_signal,
    f08cr_f08_candle_range_structure_updnbodyasym_63d_jerk_v029_signal,
    f08cr_f08_candle_range_structure_churn_63d_jerk_v030_signal,
    f08cr_f08_candle_range_structure_gapshare_21d_jerk_v031_signal,
    f08cr_f08_candle_range_structure_overnshare_21d_jerk_v032_signal,
    f08cr_f08_candle_range_structure_bodyharm_21d_jerk_v033_signal,
    f08cr_f08_candle_range_structure_wicksym_21d_jerk_v034_signal,
    f08cr_f08_candle_range_structure_trendbar_63d_jerk_v035_signal,
    f08cr_f08_candle_range_structure_marubozu_63d_jerk_v036_signal,
    f08cr_f08_candle_range_structure_dojisoft_63d_jerk_v037_signal,
    f08cr_f08_candle_range_structure_rngconc_21d_jerk_v038_signal,
    f08cr_f08_candle_range_structure_bodyconc_21d_jerk_v039_signal,
    f08cr_f08_candle_range_structure_topbody_63d_jerk_v040_signal,
    f08cr_f08_candle_range_structure_wclosepos_21d_jerk_v041_signal,
    f08cr_f08_candle_range_structure_bodymidabs_63d_jerk_v042_signal,
    f08cr_f08_candle_range_structure_strongup_63d_jerk_v043_signal,
    f08cr_f08_candle_range_structure_strongdn_63d_jerk_v044_signal,
    f08cr_f08_candle_range_structure_uprejtail_63d_jerk_v045_signal,
    f08cr_f08_candle_range_structure_dnsupptail_63d_jerk_v046_signal,
    f08cr_f08_candle_range_structure_riskadjbody_63d_jerk_v047_signal,
    f08cr_f08_candle_range_structure_gapmag_21d_jerk_v048_signal,
    f08cr_f08_candle_range_structure_candlestr_21d_jerk_v049_signal,
    f08cr_f08_candle_range_structure_bodyratema_21d_jerk_v050_signal,
    f08cr_f08_candle_range_structure_closeposema_21d_jerk_v051_signal,
    f08cr_f08_candle_range_structure_uwickema_21d_jerk_v052_signal,
    f08cr_f08_candle_range_structure_lwickema_21d_jerk_v053_signal,
    f08cr_f08_candle_range_structure_rngema_21d_jerk_v054_signal,
    f08cr_f08_candle_range_structure_bodyratmed_21d_jerk_v055_signal,
    f08cr_f08_candle_range_structure_closeposmed_21d_jerk_v056_signal,
    f08cr_f08_candle_range_structure_rngmed_21d_jerk_v057_signal,
    f08cr_f08_candle_range_structure_uptopfreq_63d_jerk_v058_signal,
    f08cr_f08_candle_range_structure_dnbotfreq_63d_jerk_v059_signal,
    f08cr_f08_candle_range_structure_uwexcess_63d_jerk_v060_signal,
    f08cr_f08_candle_range_structure_lwexcess_63d_jerk_v061_signal,
    f08cr_f08_candle_range_structure_rngexpand_21d_jerk_v062_signal,
    f08cr_f08_candle_range_structure_rngexpand63_63d_jerk_v063_signal,
    f08cr_f08_candle_range_structure_bodyexpand_21d_jerk_v064_signal,
    f08cr_f08_candle_range_structure_signrngexp_21d_jerk_v065_signal,
    f08cr_f08_candle_range_structure_convrngz_21d_jerk_v066_signal,
    f08cr_f08_candle_range_structure_bodyatr_21d_jerk_v067_signal,
    f08cr_f08_candle_range_structure_atrslope_63d_jerk_v068_signal,
    f08cr_f08_candle_range_structure_cleaneff_63d_jerk_v069_signal,
    f08cr_f08_candle_range_structure_typpos2_63d_jerk_v070_signal,
    f08cr_f08_candle_range_structure_hhhl_63d_jerk_v071_signal,
    f08cr_f08_candle_range_structure_lhll_63d_jerk_v072_signal,
    f08cr_f08_candle_range_structure_insidebar_63d_jerk_v073_signal,
    f08cr_f08_candle_range_structure_outsidebar_63d_jerk_v074_signal,
    f08cr_f08_candle_range_structure_closeoverph_63d_jerk_v075_signal,
    f08cr_f08_candle_range_structure_closeunderpl_63d_jerk_v076_signal,
    f08cr_f08_candle_range_structure_bodyescalate_63d_jerk_v077_signal,
    f08cr_f08_candle_range_structure_rngescalate_63d_jerk_v078_signal,
    f08cr_f08_candle_range_structure_explorebal_21d_jerk_v079_signal,
    f08cr_f08_candle_range_structure_openposextreme_63d_jerk_v080_signal,
    f08cr_f08_candle_range_structure_exploreasymrank_126d_jerk_v081_signal,
    f08cr_f08_candle_range_structure_bodycloseprod63_63d_jerk_v082_signal,
    f08cr_f08_candle_range_structure_uwlwlog_21d_jerk_v083_signal,
    f08cr_f08_candle_range_structure_lwickbody_21d_jerk_v084_signal,
    f08cr_f08_candle_range_structure_contmag_63d_jerk_v085_signal,
    f08cr_f08_candle_range_structure_trendcont_63d_jerk_v086_signal,
    f08cr_f08_candle_range_structure_gapfade_63d_jerk_v087_signal,
    f08cr_f08_candle_range_structure_gapcontmag_63d_jerk_v088_signal,
    f08cr_f08_candle_range_structure_uphit_63d_jerk_v089_signal,
    f08cr_f08_candle_range_structure_dirpersist_63d_jerk_v090_signal,
    f08cr_f08_candle_range_structure_upstreak_63d_jerk_v091_signal,
    f08cr_f08_candle_range_structure_downstreak_63d_jerk_v092_signal,
    f08cr_f08_candle_range_structure_rngexpstreak_63d_jerk_v093_signal,
    f08cr_f08_candle_range_structure_bodyautocorr_63d_jerk_v094_signal,
    f08cr_f08_candle_range_structure_rngautocorr_63d_jerk_v095_signal,
    f08cr_f08_candle_range_structure_bodyfat_63d_jerk_v096_signal,
    f08cr_f08_candle_range_structure_rngskew_63d_jerk_v097_signal,
    f08cr_f08_candle_range_structure_closeposskew_63d_jerk_v098_signal,
    f08cr_f08_candle_range_structure_bodyratskew_63d_jerk_v099_signal,
    f08cr_f08_candle_range_structure_whipsaw_63d_jerk_v100_signal,
    f08cr_f08_candle_range_structure_rngmaxrel_63d_jerk_v101_signal,
    f08cr_f08_candle_range_structure_rngminrel_63d_jerk_v102_signal,
    f08cr_f08_candle_range_structure_bodyrange5_21d_jerk_v103_signal,
    f08cr_f08_candle_range_structure_rngrange5_21d_jerk_v104_signal,
    f08cr_f08_candle_range_structure_netpressew_21d_jerk_v105_signal,
    f08cr_f08_candle_range_structure_convdirew_21d_jerk_v106_signal,
    f08cr_f08_candle_range_structure_wicknetstd_63d_jerk_v107_signal,
    f08cr_f08_candle_range_structure_bodysignmag_21d_jerk_v108_signal,
    f08cr_f08_candle_range_structure_closeposextreme_63d_jerk_v109_signal,
    f08cr_f08_candle_range_structure_rngspike_63d_jerk_v110_signal,
    f08cr_f08_candle_range_structure_parkinson_63d_jerk_v111_signal,
    f08cr_f08_candle_range_structure_bodyratmax_63d_jerk_v112_signal,
    f08cr_f08_candle_range_structure_highclose_21d_jerk_v113_signal,
    f08cr_f08_candle_range_structure_closelow_21d_jerk_v114_signal,
    f08cr_f08_candle_range_structure_ocstd_63d_jerk_v115_signal,
    f08cr_f08_candle_range_structure_bodyrng126_126d_jerk_v116_signal,
    f08cr_f08_candle_range_structure_closepos126_126d_jerk_v117_signal,
    f08cr_f08_candle_range_structure_uwick126_126d_jerk_v118_signal,
    f08cr_f08_candle_range_structure_lwick126_126d_jerk_v119_signal,
    f08cr_f08_candle_range_structure_rng126_126d_jerk_v120_signal,
    f08cr_f08_candle_range_structure_wickasym126_126d_jerk_v121_signal,
    f08cr_f08_candle_range_structure_bodyrng5_5d_jerk_v122_signal,
    f08cr_f08_candle_range_structure_closepos5_5d_jerk_v123_signal,
    f08cr_f08_candle_range_structure_rng5_5d_jerk_v124_signal,
    f08cr_f08_candle_range_structure_wickasym5_5d_jerk_v125_signal,
    f08cr_f08_candle_range_structure_bodyamp5_5d_jerk_v126_signal,
    f08cr_f08_candle_range_structure_uwbig_63d_jerk_v127_signal,
    f08cr_f08_candle_range_structure_lwbig_63d_jerk_v128_signal,
    f08cr_f08_candle_range_structure_bigrngclose_63d_jerk_v129_signal,
    f08cr_f08_candle_range_structure_smallrngclose_63d_jerk_v130_signal,
    f08cr_f08_candle_range_structure_updnrngasym_63d_jerk_v131_signal,
    f08cr_f08_candle_range_structure_dojibreak_63d_jerk_v132_signal,
    f08cr_f08_candle_range_structure_wclosehilo_63d_jerk_v133_signal,
    f08cr_f08_candle_range_structure_bodyposrange_63d_jerk_v134_signal,
    f08cr_f08_candle_range_structure_rngvov_63d_jerk_v135_signal,
    f08cr_f08_candle_range_structure_bodyvov_63d_jerk_v136_signal,
    f08cr_f08_candle_range_structure_closetypprem_63d_jerk_v137_signal,
    f08cr_f08_candle_range_structure_rngconvz_63d_jerk_v138_signal,
    f08cr_f08_candle_range_structure_intraeff_21d_jerk_v139_signal,
    f08cr_f08_candle_range_structure_hlrnglog_63d_jerk_v140_signal,
    f08cr_f08_candle_range_structure_closeposiqr_63d_jerk_v141_signal,
    f08cr_f08_candle_range_structure_bodyiqr_63d_jerk_v142_signal,
    f08cr_f08_candle_range_structure_upmove_21d_jerk_v143_signal,
    f08cr_f08_candle_range_structure_dnmove_21d_jerk_v144_signal,
    f08cr_f08_candle_range_structure_rngmeanmed_63d_jerk_v145_signal,
    f08cr_f08_candle_range_structure_bodysignedrank_126d_jerk_v146_signal,
    f08cr_f08_candle_range_structure_closeposkurt_63d_jerk_v147_signal,
    f08cr_f08_candle_range_structure_bodyratmin_63d_jerk_v148_signal,
    f08cr_f08_candle_range_structure_rngzpos_63d_jerk_v149_signal,
    f08cr_f08_candle_range_structure_bodyrng126skew_126d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F08_CANDLE_RANGE_STRUCTURE_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.005, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.01, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.01, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)) + 1e5, name="volume")

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
        assert q.nunique() > 50, "%s nunique=%d" % (name, q.nunique())
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

    print("OK f08_candle_range_structure_3rd_derivatives_001_150_claude: %d features pass" % n_features)
