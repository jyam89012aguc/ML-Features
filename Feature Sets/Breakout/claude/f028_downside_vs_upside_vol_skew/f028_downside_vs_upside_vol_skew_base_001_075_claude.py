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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _ema(s, w):
    return s.ewm(span=max(2, w), adjust=False, min_periods=max(1, w // 2)).mean()


def _f028_semi_vol_up(closeadj, w):
    ret = closeadj.pct_change()
    up = ret.where(ret > 0, 0.0)
    sq = up * up
    return sq.rolling(w, min_periods=max(1, w // 2)).mean().pow(0.5)


def _f028_semi_vol_down(closeadj, w):
    ret = closeadj.pct_change()
    dn = ret.where(ret < 0, 0.0)
    sq = dn * dn
    return sq.rolling(w, min_periods=max(1, w // 2)).mean().pow(0.5)


def _f028_vol_skew(closeadj, w):
    ret = closeadj.pct_change()
    up = ret.where(ret > 0, 0.0)
    dn = ret.where(ret < 0, 0.0)
    su = (up * up).rolling(w, min_periods=max(1, w // 2)).mean().pow(0.5)
    sd = (dn * dn).rolling(w, min_periods=max(1, w // 2)).mean().pow(0.5)
    return (sd - su) / (sd + su).replace(0, np.nan)


def f028dus_f028_downside_vs_upside_vol_skew_semivolupraw_5d_base_v001_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldnraw_5d_base_v002_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewraw_5d_base_v003_signal(closeadj):
    base = _f028_vol_skew(closeadj, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivolupraw_10d_base_v004_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldnraw_10d_base_v005_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewraw_10d_base_v006_signal(closeadj):
    base = _f028_vol_skew(closeadj, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivolupraw_21d_base_v007_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldnraw_21d_base_v008_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewraw_21d_base_v009_signal(closeadj):
    base = _f028_vol_skew(closeadj, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivolupraw_42d_base_v010_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldnraw_42d_base_v011_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewraw_42d_base_v012_signal(closeadj):
    base = _f028_vol_skew(closeadj, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivolupraw_63d_base_v013_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldnraw_63d_base_v014_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewraw_63d_base_v015_signal(closeadj):
    base = _f028_vol_skew(closeadj, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivolupraw_126d_base_v016_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldnraw_126d_base_v017_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewraw_126d_base_v018_signal(closeadj):
    base = _f028_vol_skew(closeadj, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivolupraw_189d_base_v019_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldnraw_189d_base_v020_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewraw_189d_base_v021_signal(closeadj):
    base = _f028_vol_skew(closeadj, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivolupraw_252d_base_v022_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldnraw_252d_base_v023_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewraw_252d_base_v024_signal(closeadj):
    base = _f028_vol_skew(closeadj, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivolupraw_378d_base_v025_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldnraw_378d_base_v026_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewraw_378d_base_v027_signal(closeadj):
    base = _f028_vol_skew(closeadj, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivolupraw_504d_base_v028_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldnraw_504d_base_v029_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewraw_504d_base_v030_signal(closeadj):
    base = _f028_vol_skew(closeadj, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivolupabs_5d_base_v031_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 5)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldnabs_5d_base_v032_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 5)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewabs_5d_base_v033_signal(closeadj):
    base = _f028_vol_skew(closeadj, 5)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivolupabs_10d_base_v034_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 10)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldnabs_10d_base_v035_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 10)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewabs_10d_base_v036_signal(closeadj):
    base = _f028_vol_skew(closeadj, 10)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivolupabs_21d_base_v037_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldnabs_21d_base_v038_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewabs_21d_base_v039_signal(closeadj):
    base = _f028_vol_skew(closeadj, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivolupabs_42d_base_v040_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldnabs_42d_base_v041_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewabs_42d_base_v042_signal(closeadj):
    base = _f028_vol_skew(closeadj, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivolupabs_63d_base_v043_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldnabs_63d_base_v044_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewabs_63d_base_v045_signal(closeadj):
    base = _f028_vol_skew(closeadj, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivolupabs_126d_base_v046_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldnabs_126d_base_v047_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewabs_126d_base_v048_signal(closeadj):
    base = _f028_vol_skew(closeadj, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivolupabs_189d_base_v049_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldnabs_189d_base_v050_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewabs_189d_base_v051_signal(closeadj):
    base = _f028_vol_skew(closeadj, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivolupabs_252d_base_v052_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldnabs_252d_base_v053_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewabs_252d_base_v054_signal(closeadj):
    base = _f028_vol_skew(closeadj, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivolupabs_378d_base_v055_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 378)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldnabs_378d_base_v056_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 378)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewabs_378d_base_v057_signal(closeadj):
    base = _f028_vol_skew(closeadj, 378)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivolupabs_504d_base_v058_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 504)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldnabs_504d_base_v059_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 504)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewabs_504d_base_v060_signal(closeadj):
    base = _f028_vol_skew(closeadj, 504)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivolupsqrt_5d_base_v061_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 5)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldnsqrt_5d_base_v062_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 5)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewsqrt_5d_base_v063_signal(closeadj):
    base = _f028_vol_skew(closeadj, 5)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivolupsqrt_10d_base_v064_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 10)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldnsqrt_10d_base_v065_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 10)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewsqrt_10d_base_v066_signal(closeadj):
    base = _f028_vol_skew(closeadj, 10)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivolupsqrt_21d_base_v067_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 21)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldnsqrt_21d_base_v068_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 21)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewsqrt_21d_base_v069_signal(closeadj):
    base = _f028_vol_skew(closeadj, 21)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivolupsqrt_42d_base_v070_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 42)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldnsqrt_42d_base_v071_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 42)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewsqrt_42d_base_v072_signal(closeadj):
    base = _f028_vol_skew(closeadj, 42)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivolupsqrt_63d_base_v073_signal(closeadj):
    base = _f028_semi_vol_up(closeadj, 63)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_semivoldnsqrt_63d_base_v074_signal(closeadj):
    base = _f028_semi_vol_down(closeadj, 63)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f028dus_f028_downside_vs_upside_vol_skew_volskewsqrt_63d_base_v075_signal(closeadj):
    base = _f028_vol_skew(closeadj, 63)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f028dus_f028_downside_vs_upside_vol_skew_semivolupraw_5d_base_v001_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldnraw_5d_base_v002_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewraw_5d_base_v003_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivolupraw_10d_base_v004_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldnraw_10d_base_v005_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewraw_10d_base_v006_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivolupraw_21d_base_v007_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldnraw_21d_base_v008_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewraw_21d_base_v009_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivolupraw_42d_base_v010_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldnraw_42d_base_v011_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewraw_42d_base_v012_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivolupraw_63d_base_v013_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldnraw_63d_base_v014_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewraw_63d_base_v015_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivolupraw_126d_base_v016_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldnraw_126d_base_v017_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewraw_126d_base_v018_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivolupraw_189d_base_v019_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldnraw_189d_base_v020_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewraw_189d_base_v021_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivolupraw_252d_base_v022_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldnraw_252d_base_v023_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewraw_252d_base_v024_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivolupraw_378d_base_v025_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldnraw_378d_base_v026_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewraw_378d_base_v027_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivolupraw_504d_base_v028_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldnraw_504d_base_v029_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewraw_504d_base_v030_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivolupabs_5d_base_v031_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldnabs_5d_base_v032_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewabs_5d_base_v033_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivolupabs_10d_base_v034_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldnabs_10d_base_v035_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewabs_10d_base_v036_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivolupabs_21d_base_v037_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldnabs_21d_base_v038_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewabs_21d_base_v039_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivolupabs_42d_base_v040_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldnabs_42d_base_v041_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewabs_42d_base_v042_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivolupabs_63d_base_v043_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldnabs_63d_base_v044_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewabs_63d_base_v045_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivolupabs_126d_base_v046_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldnabs_126d_base_v047_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewabs_126d_base_v048_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivolupabs_189d_base_v049_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldnabs_189d_base_v050_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewabs_189d_base_v051_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivolupabs_252d_base_v052_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldnabs_252d_base_v053_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewabs_252d_base_v054_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivolupabs_378d_base_v055_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldnabs_378d_base_v056_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewabs_378d_base_v057_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivolupabs_504d_base_v058_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldnabs_504d_base_v059_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewabs_504d_base_v060_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivolupsqrt_5d_base_v061_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldnsqrt_5d_base_v062_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewsqrt_5d_base_v063_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivolupsqrt_10d_base_v064_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldnsqrt_10d_base_v065_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewsqrt_10d_base_v066_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivolupsqrt_21d_base_v067_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldnsqrt_21d_base_v068_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewsqrt_21d_base_v069_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivolupsqrt_42d_base_v070_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldnsqrt_42d_base_v071_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewsqrt_42d_base_v072_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivolupsqrt_63d_base_v073_signal,
    f028dus_f028_downside_vs_upside_vol_skew_semivoldnsqrt_63d_base_v074_signal,
    f028dus_f028_downside_vs_upside_vol_skew_volskewsqrt_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F028_DOWNSIDE_VS_UPSIDE_VOL_SKEW_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high.values, name="high")
    low = pd.Series(low.values, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {"closeadj": closeadj, "high": high, "low": low, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f028_semi_vol_up', '_f028_semi_vol_down', '_f028_vol_skew')
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f028_downside_vs_upside_vol_skew_base_001_075_claude: {n_features} features pass")
