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
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()

# ===== folder domain primitives =====
def _f36_low_vol_signal(closeadj, w):
    rets = closeadj.pct_change()
    vol = rets.rolling(w, min_periods=max(1, w // 2)).std()
    return _safe_div(closeadj, vol.replace(0, np.nan))


def _f36_bv_growth(bvps, w):
    growth = bvps.pct_change(periods=w)
    return growth * bvps


def _f36_compounder_score(closeadj, bvps, w):
    rets = closeadj.pct_change()
    vol = rets.rolling(w, min_periods=max(1, w // 2)).std()
    bvg = bvps.pct_change(periods=w)
    return bvg * closeadj / vol.replace(0, np.nan)

def f36qbc_f36_quiet_bank_compounder_lowvol_5d_base_v001_signal(closeadj):
    result = _f36_low_vol_signal(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_lowvol_10d_base_v002_signal(closeadj):
    result = _f36_low_vol_signal(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_lowvol_21d_base_v003_signal(closeadj):
    result = _f36_low_vol_signal(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_lowvol_42d_base_v004_signal(closeadj):
    result = _f36_low_vol_signal(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_lowvol_63d_base_v005_signal(closeadj):
    result = _f36_low_vol_signal(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_lowvol_126d_base_v006_signal(closeadj):
    result = _f36_low_vol_signal(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_lowvol_189d_base_v007_signal(closeadj):
    result = _f36_low_vol_signal(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_lowvol_252d_base_v008_signal(closeadj):
    result = _f36_low_vol_signal(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_lowvol_378d_base_v009_signal(closeadj):
    result = _f36_low_vol_signal(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_lowvol_504d_base_v010_signal(closeadj):
    result = _f36_low_vol_signal(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_lowvolema_21d_base_v011_signal(closeadj):
    base = _f36_low_vol_signal(closeadj, 21)
    result = _ema(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_lowvolema_63d_base_v012_signal(closeadj):
    base = _f36_low_vol_signal(closeadj, 63)
    result = _ema(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_bvg_5d_base_v013_signal(bvps):
    result = _f36_bv_growth(bvps, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_bvg_10d_base_v014_signal(bvps):
    result = _f36_bv_growth(bvps, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_bvg_21d_base_v015_signal(bvps):
    result = _f36_bv_growth(bvps, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_bvg_42d_base_v016_signal(bvps):
    result = _f36_bv_growth(bvps, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_bvg_63d_base_v017_signal(bvps):
    result = _f36_bv_growth(bvps, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_bvg_126d_base_v018_signal(bvps):
    result = _f36_bv_growth(bvps, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_bvg_189d_base_v019_signal(bvps):
    result = _f36_bv_growth(bvps, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_bvg_252d_base_v020_signal(bvps):
    result = _f36_bv_growth(bvps, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_bvg_378d_base_v021_signal(bvps):
    result = _f36_bv_growth(bvps, 378)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_bvg_504d_base_v022_signal(bvps):
    result = _f36_bv_growth(bvps, 504)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_bvgmean_63d_base_v023_signal(bvps):
    base = _f36_bv_growth(bvps, 63)
    result = _mean(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_bvgmean_252d_base_v024_signal(bvps):
    base = _f36_bv_growth(bvps, 252)
    result = _mean(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_compscore_5d_base_v025_signal(closeadj, bvps):
    result = _f36_compounder_score(closeadj, bvps, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_compscore_10d_base_v026_signal(closeadj, bvps):
    result = _f36_compounder_score(closeadj, bvps, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_compscore_21d_base_v027_signal(closeadj, bvps):
    result = _f36_compounder_score(closeadj, bvps, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_compscore_42d_base_v028_signal(closeadj, bvps):
    result = _f36_compounder_score(closeadj, bvps, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_compscore_63d_base_v029_signal(closeadj, bvps):
    result = _f36_compounder_score(closeadj, bvps, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_compscore_126d_base_v030_signal(closeadj, bvps):
    result = _f36_compounder_score(closeadj, bvps, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_compscore_189d_base_v031_signal(closeadj, bvps):
    result = _f36_compounder_score(closeadj, bvps, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_compscore_252d_base_v032_signal(closeadj, bvps):
    result = _f36_compounder_score(closeadj, bvps, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_compscore_378d_base_v033_signal(closeadj, bvps):
    result = _f36_compounder_score(closeadj, bvps, 378)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_compscore_504d_base_v034_signal(closeadj, bvps):
    result = _f36_compounder_score(closeadj, bvps, 504)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_compscoreema_63d_base_v035_signal(closeadj, bvps):
    base = _f36_compounder_score(closeadj, bvps, 63)
    result = _ema(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_compscoreema_252d_base_v036_signal(closeadj, bvps):
    base = _f36_compounder_score(closeadj, bvps, 252)
    result = _ema(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_lowvolxvol_21d_base_v037_signal(closeadj, volume):
    base = _f36_low_vol_signal(closeadj, 21)
    result = base * _mean(volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_lowvolxvol_63d_base_v038_signal(closeadj, volume):
    base = _f36_low_vol_signal(closeadj, 63)
    result = base * _mean(volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_lowvolxvol_126d_base_v039_signal(closeadj, volume):
    base = _f36_low_vol_signal(closeadj, 126)
    result = base * _mean(volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_lowvolxvol_252d_base_v040_signal(closeadj, volume):
    base = _f36_low_vol_signal(closeadj, 252)
    result = base * _mean(volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_bvgxeq_21d_base_v041_signal(bvps, equity):
    base = _f36_bv_growth(bvps, 21)
    result = base * _safe_div(equity, equity.rolling(21, min_periods=max(1,21//2)).mean())
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_bvgxeq_63d_base_v042_signal(bvps, equity):
    base = _f36_bv_growth(bvps, 63)
    result = base * _safe_div(equity, equity.rolling(63, min_periods=max(1,63//2)).mean())
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_bvgxeq_126d_base_v043_signal(bvps, equity):
    base = _f36_bv_growth(bvps, 126)
    result = base * _safe_div(equity, equity.rolling(126, min_periods=max(1,126//2)).mean())
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_bvgxeq_252d_base_v044_signal(bvps, equity):
    base = _f36_bv_growth(bvps, 252)
    result = base * _safe_div(equity, equity.rolling(252, min_periods=max(1,252//2)).mean())
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_compxvol_21d_base_v045_signal(closeadj, bvps, volume):
    base = _f36_compounder_score(closeadj, bvps, 21)
    result = base * _mean(volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_compxvol_63d_base_v046_signal(closeadj, bvps, volume):
    base = _f36_compounder_score(closeadj, bvps, 63)
    result = base * _mean(volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_compxvol_126d_base_v047_signal(closeadj, bvps, volume):
    base = _f36_compounder_score(closeadj, bvps, 126)
    result = base * _mean(volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_compxvol_252d_base_v048_signal(closeadj, bvps, volume):
    base = _f36_compounder_score(closeadj, bvps, 252)
    result = base * _mean(volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_lowvolz_21d_base_v049_signal(closeadj):
    base = _f36_low_vol_signal(closeadj, 21)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_lowvolz_63d_base_v050_signal(closeadj):
    base = _f36_low_vol_signal(closeadj, 63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_lowvolz_126d_base_v051_signal(closeadj):
    base = _f36_low_vol_signal(closeadj, 126)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_lowvolz_252d_base_v052_signal(closeadj):
    base = _f36_low_vol_signal(closeadj, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_bvgz_21d_base_v053_signal(bvps, closeadj):
    base = _f36_bv_growth(bvps, 21)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_bvgz_63d_base_v054_signal(bvps, closeadj):
    base = _f36_bv_growth(bvps, 63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_bvgz_126d_base_v055_signal(bvps, closeadj):
    base = _f36_bv_growth(bvps, 126)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_bvgz_252d_base_v056_signal(bvps, closeadj):
    base = _f36_bv_growth(bvps, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_compz_21d_base_v057_signal(closeadj, bvps):
    base = _f36_compounder_score(closeadj, bvps, 21)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_compz_63d_base_v058_signal(closeadj, bvps):
    base = _f36_compounder_score(closeadj, bvps, 63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_compz_126d_base_v059_signal(closeadj, bvps):
    base = _f36_compounder_score(closeadj, bvps, 126)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_compz_252d_base_v060_signal(closeadj, bvps):
    base = _f36_compounder_score(closeadj, bvps, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_lowvolstd_21d_base_v061_signal(closeadj):
    base = _f36_low_vol_signal(closeadj, 21)
    result = _std(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_lowvolstd_63d_base_v062_signal(closeadj):
    base = _f36_low_vol_signal(closeadj, 63)
    result = _std(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_lowvolstd_126d_base_v063_signal(closeadj):
    base = _f36_low_vol_signal(closeadj, 126)
    result = _std(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_lowvolstd_252d_base_v064_signal(closeadj):
    base = _f36_low_vol_signal(closeadj, 252)
    result = _std(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_bvgstd_21d_base_v065_signal(bvps, closeadj):
    base = _f36_bv_growth(bvps, 21)
    result = _std(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_bvgstd_63d_base_v066_signal(bvps, closeadj):
    base = _f36_bv_growth(bvps, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_bvgstd_126d_base_v067_signal(bvps, closeadj):
    base = _f36_bv_growth(bvps, 126)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_bvgstd_252d_base_v068_signal(bvps, closeadj):
    base = _f36_bv_growth(bvps, 252)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_compstd_21d_base_v069_signal(closeadj, bvps):
    base = _f36_compounder_score(closeadj, bvps, 21)
    result = _std(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_compstd_63d_base_v070_signal(closeadj, bvps):
    base = _f36_compounder_score(closeadj, bvps, 63)
    result = _std(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_compstd_126d_base_v071_signal(closeadj, bvps):
    base = _f36_compounder_score(closeadj, bvps, 126)
    result = _std(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_compstd_252d_base_v072_signal(closeadj, bvps):
    base = _f36_compounder_score(closeadj, bvps, 252)
    result = _std(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_lowvolratio_21d_base_v073_signal(closeadj):
    base = _f36_low_vol_signal(closeadj, 21)
    result = _safe_div(base, _mean(base, 42))*closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_lowvolratio_63d_base_v074_signal(closeadj):
    base = _f36_low_vol_signal(closeadj, 63)
    result = _safe_div(base, _mean(base, 126))*closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36qbc_f36_quiet_bank_compounder_lowvolratio_126d_base_v075_signal(closeadj):
    base = _f36_low_vol_signal(closeadj, 126)
    result = _safe_div(base, _mean(base, 252))*closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f36qbc_f36_quiet_bank_compounder_lowvol_5d_base_v001_signal,
    f36qbc_f36_quiet_bank_compounder_lowvol_10d_base_v002_signal,
    f36qbc_f36_quiet_bank_compounder_lowvol_21d_base_v003_signal,
    f36qbc_f36_quiet_bank_compounder_lowvol_42d_base_v004_signal,
    f36qbc_f36_quiet_bank_compounder_lowvol_63d_base_v005_signal,
    f36qbc_f36_quiet_bank_compounder_lowvol_126d_base_v006_signal,
    f36qbc_f36_quiet_bank_compounder_lowvol_189d_base_v007_signal,
    f36qbc_f36_quiet_bank_compounder_lowvol_252d_base_v008_signal,
    f36qbc_f36_quiet_bank_compounder_lowvol_378d_base_v009_signal,
    f36qbc_f36_quiet_bank_compounder_lowvol_504d_base_v010_signal,
    f36qbc_f36_quiet_bank_compounder_lowvolema_21d_base_v011_signal,
    f36qbc_f36_quiet_bank_compounder_lowvolema_63d_base_v012_signal,
    f36qbc_f36_quiet_bank_compounder_bvg_5d_base_v013_signal,
    f36qbc_f36_quiet_bank_compounder_bvg_10d_base_v014_signal,
    f36qbc_f36_quiet_bank_compounder_bvg_21d_base_v015_signal,
    f36qbc_f36_quiet_bank_compounder_bvg_42d_base_v016_signal,
    f36qbc_f36_quiet_bank_compounder_bvg_63d_base_v017_signal,
    f36qbc_f36_quiet_bank_compounder_bvg_126d_base_v018_signal,
    f36qbc_f36_quiet_bank_compounder_bvg_189d_base_v019_signal,
    f36qbc_f36_quiet_bank_compounder_bvg_252d_base_v020_signal,
    f36qbc_f36_quiet_bank_compounder_bvg_378d_base_v021_signal,
    f36qbc_f36_quiet_bank_compounder_bvg_504d_base_v022_signal,
    f36qbc_f36_quiet_bank_compounder_bvgmean_63d_base_v023_signal,
    f36qbc_f36_quiet_bank_compounder_bvgmean_252d_base_v024_signal,
    f36qbc_f36_quiet_bank_compounder_compscore_5d_base_v025_signal,
    f36qbc_f36_quiet_bank_compounder_compscore_10d_base_v026_signal,
    f36qbc_f36_quiet_bank_compounder_compscore_21d_base_v027_signal,
    f36qbc_f36_quiet_bank_compounder_compscore_42d_base_v028_signal,
    f36qbc_f36_quiet_bank_compounder_compscore_63d_base_v029_signal,
    f36qbc_f36_quiet_bank_compounder_compscore_126d_base_v030_signal,
    f36qbc_f36_quiet_bank_compounder_compscore_189d_base_v031_signal,
    f36qbc_f36_quiet_bank_compounder_compscore_252d_base_v032_signal,
    f36qbc_f36_quiet_bank_compounder_compscore_378d_base_v033_signal,
    f36qbc_f36_quiet_bank_compounder_compscore_504d_base_v034_signal,
    f36qbc_f36_quiet_bank_compounder_compscoreema_63d_base_v035_signal,
    f36qbc_f36_quiet_bank_compounder_compscoreema_252d_base_v036_signal,
    f36qbc_f36_quiet_bank_compounder_lowvolxvol_21d_base_v037_signal,
    f36qbc_f36_quiet_bank_compounder_lowvolxvol_63d_base_v038_signal,
    f36qbc_f36_quiet_bank_compounder_lowvolxvol_126d_base_v039_signal,
    f36qbc_f36_quiet_bank_compounder_lowvolxvol_252d_base_v040_signal,
    f36qbc_f36_quiet_bank_compounder_bvgxeq_21d_base_v041_signal,
    f36qbc_f36_quiet_bank_compounder_bvgxeq_63d_base_v042_signal,
    f36qbc_f36_quiet_bank_compounder_bvgxeq_126d_base_v043_signal,
    f36qbc_f36_quiet_bank_compounder_bvgxeq_252d_base_v044_signal,
    f36qbc_f36_quiet_bank_compounder_compxvol_21d_base_v045_signal,
    f36qbc_f36_quiet_bank_compounder_compxvol_63d_base_v046_signal,
    f36qbc_f36_quiet_bank_compounder_compxvol_126d_base_v047_signal,
    f36qbc_f36_quiet_bank_compounder_compxvol_252d_base_v048_signal,
    f36qbc_f36_quiet_bank_compounder_lowvolz_21d_base_v049_signal,
    f36qbc_f36_quiet_bank_compounder_lowvolz_63d_base_v050_signal,
    f36qbc_f36_quiet_bank_compounder_lowvolz_126d_base_v051_signal,
    f36qbc_f36_quiet_bank_compounder_lowvolz_252d_base_v052_signal,
    f36qbc_f36_quiet_bank_compounder_bvgz_21d_base_v053_signal,
    f36qbc_f36_quiet_bank_compounder_bvgz_63d_base_v054_signal,
    f36qbc_f36_quiet_bank_compounder_bvgz_126d_base_v055_signal,
    f36qbc_f36_quiet_bank_compounder_bvgz_252d_base_v056_signal,
    f36qbc_f36_quiet_bank_compounder_compz_21d_base_v057_signal,
    f36qbc_f36_quiet_bank_compounder_compz_63d_base_v058_signal,
    f36qbc_f36_quiet_bank_compounder_compz_126d_base_v059_signal,
    f36qbc_f36_quiet_bank_compounder_compz_252d_base_v060_signal,
    f36qbc_f36_quiet_bank_compounder_lowvolstd_21d_base_v061_signal,
    f36qbc_f36_quiet_bank_compounder_lowvolstd_63d_base_v062_signal,
    f36qbc_f36_quiet_bank_compounder_lowvolstd_126d_base_v063_signal,
    f36qbc_f36_quiet_bank_compounder_lowvolstd_252d_base_v064_signal,
    f36qbc_f36_quiet_bank_compounder_bvgstd_21d_base_v065_signal,
    f36qbc_f36_quiet_bank_compounder_bvgstd_63d_base_v066_signal,
    f36qbc_f36_quiet_bank_compounder_bvgstd_126d_base_v067_signal,
    f36qbc_f36_quiet_bank_compounder_bvgstd_252d_base_v068_signal,
    f36qbc_f36_quiet_bank_compounder_compstd_21d_base_v069_signal,
    f36qbc_f36_quiet_bank_compounder_compstd_63d_base_v070_signal,
    f36qbc_f36_quiet_bank_compounder_compstd_126d_base_v071_signal,
    f36qbc_f36_quiet_bank_compounder_compstd_252d_base_v072_signal,
    f36qbc_f36_quiet_bank_compounder_lowvolratio_21d_base_v073_signal,
    f36qbc_f36_quiet_bank_compounder_lowvolratio_63d_base_v074_signal,
    f36qbc_f36_quiet_bank_compounder_lowvolratio_126d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F36_QUIET_BANK_COMPOUNDER_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetsc      = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsc")
    assetsnc     = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsnc")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    liabilitiesc = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesc")
    liabilitiesnc= pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesnc")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    equityusd    = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equityusd")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    debtc        = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtc")
    debtnc       = pd.Series(4.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtnc")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    intangibles  = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    tangibles    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="tangibles")
    invcap       = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")
    retearn      = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")
    sbcomp       = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="sbcomp")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    shareswadil  = pd.Series(1.02e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswadil")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    epsdil       = pd.Series(0.98 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="epsdil")
    bvps         = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="bvps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    sps          = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="sps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    pe           = pd.Series(closeadj / eps.replace(0, np.nan).abs(), name="pe")
    pb           = pd.Series(closeadj / bvps.replace(0, np.nan).abs(), name="pb")
    ps           = pd.Series(closeadj / sps.replace(0, np.nan).abs(), name="ps")
    evebit       = pd.Series(ev / ebit.replace(0, np.nan).abs(), name="evebit")
    evebitda     = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ros          = pd.Series(0.08 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ros")
    currentratio = pd.Series(1.5 + 0.3*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="currentratio")
    de           = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    divyield     = pd.Series(0.02 + 0.005*np.sin(np.arange(n)/250.0) + 0.001*np.random.randn(n), name="divyield")
    assetturnover= pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "assets": assets, "assetsc": assetsc, "assetsnc": assetsnc,
        "liabilities": liabilities, "liabilitiesc": liabilitiesc, "liabilitiesnc": liabilitiesnc,
        "equity": equity, "equityusd": equityusd,
        "debt": debt, "debtc": debtc, "debtnc": debtnc, "cashneq": cashneq,
        "inventory": inventory, "receivables": receivables, "payables": payables,
        "deferredrev": deferredrev, "workingcapital": workingcapital,
        "ppnenet": ppnenet, "intangibles": intangibles, "tangibles": tangibles,
        "invcap": invcap, "retearn": retearn, "sbcomp": sbcomp,
        "sharesbas": sharesbas, "shareswa": shareswa, "shareswadil": shareswadil,
        "eps": eps, "epsdil": epsdil, "bvps": bvps, "fcfps": fcfps, "sps": sps, "dps": dps,
        "marketcap": marketcap, "ev": ev,
        "pe": pe, "pb": pb, "ps": ps, "evebit": evebit, "evebitda": evebitda,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
        "roa": roa, "roe": roe, "roic": roic, "ros": ros,
        "currentratio": currentratio, "de": de,
        "payoutratio": payoutratio, "divyield": divyield, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f36_low_vol_signal", "_f36_bv_growth", "_f36_compounder_score")
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
    print(f"OK f36_quiet_bank_compounder_base_001_075_claude: {n_features} features pass")
