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
    return s.ewm(span=w, min_periods=max(1, w // 2)).mean()


# ===== folder domain primitives =====
def _f43_asset_equity_leverage(assets, equity):
    """Asset / equity leverage ratio (instantaneous)."""
    return assets / equity.replace(0, np.nan)


def _f43_leverage_dynamics(assets, equity, w):
    """Rolling change of leverage = assets/equity over window w."""
    lev = assets / equity.replace(0, np.nan)
    return lev - lev.rolling(w, min_periods=max(1, w // 2)).mean()


def _f43_leverage_risk_score(assets, equity, debt, w):
    """Leverage risk score: (assets + debt) / equity smoothed over w."""
    raw = (assets + debt) / equity.replace(0, np.nan)
    return raw.rolling(w, min_periods=max(1, w // 2)).mean()

def f43lrb_f43_leverage_risk_bank_lev_x_close_5d_base_v001_signal(assets, equity, closeadj):
    base = _f43_asset_equity_leverage(assets, equity)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_lev_mean_close_5d_base_v002_signal(assets, equity, closeadj):
    base = _mean(_f43_asset_equity_leverage(assets, equity), 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_lev_mean_close_p21_5d_base_v003_signal(assets, equity, closeadj):
    base = _mean(_f43_asset_equity_leverage(assets, equity), 5)
    result = base * closeadj * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_lev_std_close_5d_base_v004_signal(assets, equity, closeadj):
    base = _std(_f43_asset_equity_leverage(assets, equity), 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_lev_z_close_5d_base_v005_signal(assets, equity, closeadj):
    base = _z(_f43_asset_equity_leverage(assets, equity), 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_lev_z_close_p21_5d_base_v006_signal(assets, equity, closeadj):
    base = _z(_f43_asset_equity_leverage(assets, equity), 5)
    result = base * closeadj * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_lev_ema_close_5d_base_v007_signal(assets, equity, closeadj):
    base = _ema(_f43_asset_equity_leverage(assets, equity), 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_lev_ema_close_p63_5d_base_v008_signal(assets, equity, closeadj):
    base = _ema(_f43_asset_equity_leverage(assets, equity), 5)
    result = base * closeadj * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_lev_log_close_5d_base_v009_signal(assets, equity, closeadj):
    base = _f43_asset_equity_leverage(assets, equity)
    result = np.log(base.abs().replace(0, np.nan)) * closeadj * closeadj.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_lev_sqrt_close_5d_base_v010_signal(assets, equity, closeadj):
    base = _f43_asset_equity_leverage(assets, equity)
    result = np.sqrt(base.abs()) * closeadj * closeadj.pct_change(5)
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_lev_pct_close_5d_base_v011_signal(assets, equity, closeadj):
    base = _f43_asset_equity_leverage(assets, equity)
    result = base.pct_change(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_lev_diff_close_5d_base_v012_signal(assets, equity, closeadj):
    base = _f43_asset_equity_leverage(assets, equity)
    result = base.diff(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_lev_sign_close_5d_base_v013_signal(assets, equity, closeadj):
    base = _f43_asset_equity_leverage(assets, equity)
    result = np.sign(base - 10.0) * closeadj * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_dyn_x_close_5d_base_v014_signal(assets, equity, closeadj):
    base = _f43_leverage_dynamics(assets, equity, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_dyn_mean21_close_5d_base_v015_signal(assets, equity, closeadj):
    base = _mean(_f43_leverage_dynamics(assets, equity, 5), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_dyn_mean63_close_5d_base_v016_signal(assets, equity, closeadj):
    base = _mean(_f43_leverage_dynamics(assets, equity, 5), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_dyn_std21_close_5d_base_v017_signal(assets, equity, closeadj):
    base = _std(_f43_leverage_dynamics(assets, equity, 5), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_dyn_std63_close_5d_base_v018_signal(assets, equity, closeadj):
    base = _std(_f43_leverage_dynamics(assets, equity, 5), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_dyn_z63_close_5d_base_v019_signal(assets, equity, closeadj):
    base = _z(_f43_leverage_dynamics(assets, equity, 5), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_dyn_z252_close_5d_base_v020_signal(assets, equity, closeadj):
    base = _z(_f43_leverage_dynamics(assets, equity, 5), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_dyn_ema21_close_5d_base_v021_signal(assets, equity, closeadj):
    base = _ema(_f43_leverage_dynamics(assets, equity, 5), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_dyn_ema63_close_5d_base_v022_signal(assets, equity, closeadj):
    base = _ema(_f43_leverage_dynamics(assets, equity, 5), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_dyn_pct21_close_5d_base_v023_signal(assets, equity, closeadj):
    base = _f43_leverage_dynamics(assets, equity, 5)
    result = base.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_risk_x_close_5d_base_v024_signal(assets, equity, debt, closeadj):
    base = _f43_leverage_risk_score(assets, equity, debt, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_risk_mean21_5d_base_v025_signal(assets, equity, debt, closeadj):
    base = _mean(_f43_leverage_risk_score(assets, equity, debt, 5), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_risk_mean63_5d_base_v026_signal(assets, equity, debt, closeadj):
    base = _mean(_f43_leverage_risk_score(assets, equity, debt, 5), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_risk_std21_5d_base_v027_signal(assets, equity, debt, closeadj):
    base = _std(_f43_leverage_risk_score(assets, equity, debt, 5), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_risk_std63_5d_base_v028_signal(assets, equity, debt, closeadj):
    base = _std(_f43_leverage_risk_score(assets, equity, debt, 5), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_risk_z63_5d_base_v029_signal(assets, equity, debt, closeadj):
    base = _z(_f43_leverage_risk_score(assets, equity, debt, 5), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_risk_z252_5d_base_v030_signal(assets, equity, debt, closeadj):
    base = _z(_f43_leverage_risk_score(assets, equity, debt, 5), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_risk_ema21_5d_base_v031_signal(assets, equity, debt, closeadj):
    base = _ema(_f43_leverage_risk_score(assets, equity, debt, 5), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_risk_ema63_5d_base_v032_signal(assets, equity, debt, closeadj):
    base = _ema(_f43_leverage_risk_score(assets, equity, debt, 5), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_risk_log_5d_base_v033_signal(assets, equity, debt, closeadj):
    base = _f43_leverage_risk_score(assets, equity, debt, 5)
    result = np.log(base.abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_risk_sqrt_5d_base_v034_signal(assets, equity, debt, closeadj):
    base = _f43_leverage_risk_score(assets, equity, debt, 5)
    result = np.sqrt(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_risk_pct21_5d_base_v035_signal(assets, equity, debt, closeadj):
    base = _f43_leverage_risk_score(assets, equity, debt, 5)
    result = base.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_risk_pct63_5d_base_v036_signal(assets, equity, debt, closeadj):
    base = _f43_leverage_risk_score(assets, equity, debt, 5)
    result = base.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_risk_diff21_5d_base_v037_signal(assets, equity, debt, closeadj):
    base = _f43_leverage_risk_score(assets, equity, debt, 5)
    result = base.diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_risk_diff63_5d_base_v038_signal(assets, equity, debt, closeadj):
    base = _f43_leverage_risk_score(assets, equity, debt, 5)
    result = base.diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_lev_x_dyn_5d_base_v039_signal(assets, equity, closeadj):
    a = _f43_asset_equity_leverage(assets, equity)
    b = _f43_leverage_dynamics(assets, equity, 5)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_lev_x_risk_5d_base_v040_signal(assets, equity, debt, closeadj):
    a = _f43_asset_equity_leverage(assets, equity)
    b = _f43_leverage_risk_score(assets, equity, debt, 5)
    result = a * b * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_dyn_x_risk_5d_base_v041_signal(assets, equity, debt, closeadj):
    a = _f43_leverage_dynamics(assets, equity, 5)
    b = _f43_leverage_risk_score(assets, equity, debt, 5)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_lev_minus_risk_5d_base_v042_signal(assets, equity, debt, closeadj):
    a = _f43_asset_equity_leverage(assets, equity)
    b = _f43_leverage_risk_score(assets, equity, debt, 5)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_lev_mean_close_10d_base_v043_signal(assets, equity, closeadj):
    base = _mean(_f43_asset_equity_leverage(assets, equity), 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_lev_mean_close_p21_10d_base_v044_signal(assets, equity, closeadj):
    base = _mean(_f43_asset_equity_leverage(assets, equity), 10)
    result = base * closeadj * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_lev_std_close_10d_base_v045_signal(assets, equity, closeadj):
    base = _std(_f43_asset_equity_leverage(assets, equity), 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_lev_z_close_10d_base_v046_signal(assets, equity, closeadj):
    base = _z(_f43_asset_equity_leverage(assets, equity), 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_lev_z_close_p21_10d_base_v047_signal(assets, equity, closeadj):
    base = _z(_f43_asset_equity_leverage(assets, equity), 10)
    result = base * closeadj * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_lev_ema_close_10d_base_v048_signal(assets, equity, closeadj):
    base = _ema(_f43_asset_equity_leverage(assets, equity), 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_lev_ema_close_p63_10d_base_v049_signal(assets, equity, closeadj):
    base = _ema(_f43_asset_equity_leverage(assets, equity), 10)
    result = base * closeadj * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_lev_log_close_10d_base_v050_signal(assets, equity, closeadj):
    base = _f43_asset_equity_leverage(assets, equity)
    result = np.log(base.abs().replace(0, np.nan)) * closeadj * closeadj.pct_change(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_lev_sqrt_close_10d_base_v051_signal(assets, equity, closeadj):
    base = _f43_asset_equity_leverage(assets, equity)
    result = np.sqrt(base.abs()) * closeadj * closeadj.pct_change(10)
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_lev_pct_close_10d_base_v052_signal(assets, equity, closeadj):
    base = _f43_asset_equity_leverage(assets, equity)
    result = base.pct_change(10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_lev_diff_close_10d_base_v053_signal(assets, equity, closeadj):
    base = _f43_asset_equity_leverage(assets, equity)
    result = base.diff(10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_dyn_x_close_10d_base_v054_signal(assets, equity, closeadj):
    base = _f43_leverage_dynamics(assets, equity, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_dyn_mean21_close_10d_base_v055_signal(assets, equity, closeadj):
    base = _mean(_f43_leverage_dynamics(assets, equity, 10), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_dyn_mean63_close_10d_base_v056_signal(assets, equity, closeadj):
    base = _mean(_f43_leverage_dynamics(assets, equity, 10), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_dyn_std21_close_10d_base_v057_signal(assets, equity, closeadj):
    base = _std(_f43_leverage_dynamics(assets, equity, 10), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_dyn_std63_close_10d_base_v058_signal(assets, equity, closeadj):
    base = _std(_f43_leverage_dynamics(assets, equity, 10), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_dyn_z63_close_10d_base_v059_signal(assets, equity, closeadj):
    base = _z(_f43_leverage_dynamics(assets, equity, 10), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_dyn_z252_close_10d_base_v060_signal(assets, equity, closeadj):
    base = _z(_f43_leverage_dynamics(assets, equity, 10), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_dyn_ema21_close_10d_base_v061_signal(assets, equity, closeadj):
    base = _ema(_f43_leverage_dynamics(assets, equity, 10), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_dyn_ema63_close_10d_base_v062_signal(assets, equity, closeadj):
    base = _ema(_f43_leverage_dynamics(assets, equity, 10), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_dyn_pct21_close_10d_base_v063_signal(assets, equity, closeadj):
    base = _f43_leverage_dynamics(assets, equity, 10)
    result = base.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_risk_x_close_10d_base_v064_signal(assets, equity, debt, closeadj):
    base = _f43_leverage_risk_score(assets, equity, debt, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_risk_mean21_10d_base_v065_signal(assets, equity, debt, closeadj):
    base = _mean(_f43_leverage_risk_score(assets, equity, debt, 10), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_risk_mean63_10d_base_v066_signal(assets, equity, debt, closeadj):
    base = _mean(_f43_leverage_risk_score(assets, equity, debt, 10), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_risk_std21_10d_base_v067_signal(assets, equity, debt, closeadj):
    base = _std(_f43_leverage_risk_score(assets, equity, debt, 10), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_risk_std63_10d_base_v068_signal(assets, equity, debt, closeadj):
    base = _std(_f43_leverage_risk_score(assets, equity, debt, 10), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_risk_z63_10d_base_v069_signal(assets, equity, debt, closeadj):
    base = _z(_f43_leverage_risk_score(assets, equity, debt, 10), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_risk_z252_10d_base_v070_signal(assets, equity, debt, closeadj):
    base = _z(_f43_leverage_risk_score(assets, equity, debt, 10), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_risk_ema21_10d_base_v071_signal(assets, equity, debt, closeadj):
    base = _ema(_f43_leverage_risk_score(assets, equity, debt, 10), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_risk_ema63_10d_base_v072_signal(assets, equity, debt, closeadj):
    base = _ema(_f43_leverage_risk_score(assets, equity, debt, 10), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_risk_log_10d_base_v073_signal(assets, equity, debt, closeadj):
    base = _f43_leverage_risk_score(assets, equity, debt, 10)
    result = np.log(base.abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_risk_sqrt_10d_base_v074_signal(assets, equity, debt, closeadj):
    base = _f43_leverage_risk_score(assets, equity, debt, 10)
    result = np.sqrt(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f43lrb_f43_leverage_risk_bank_risk_pct21_10d_base_v075_signal(assets, equity, debt, closeadj):
    base = _f43_leverage_risk_score(assets, equity, debt, 10)
    result = base.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f43lrb_f43_leverage_risk_bank_lev_x_close_5d_base_v001_signal,
    f43lrb_f43_leverage_risk_bank_lev_mean_close_5d_base_v002_signal,
    f43lrb_f43_leverage_risk_bank_lev_mean_close_p21_5d_base_v003_signal,
    f43lrb_f43_leverage_risk_bank_lev_std_close_5d_base_v004_signal,
    f43lrb_f43_leverage_risk_bank_lev_z_close_5d_base_v005_signal,
    f43lrb_f43_leverage_risk_bank_lev_z_close_p21_5d_base_v006_signal,
    f43lrb_f43_leverage_risk_bank_lev_ema_close_5d_base_v007_signal,
    f43lrb_f43_leverage_risk_bank_lev_ema_close_p63_5d_base_v008_signal,
    f43lrb_f43_leverage_risk_bank_lev_log_close_5d_base_v009_signal,
    f43lrb_f43_leverage_risk_bank_lev_sqrt_close_5d_base_v010_signal,
    f43lrb_f43_leverage_risk_bank_lev_pct_close_5d_base_v011_signal,
    f43lrb_f43_leverage_risk_bank_lev_diff_close_5d_base_v012_signal,
    f43lrb_f43_leverage_risk_bank_lev_sign_close_5d_base_v013_signal,
    f43lrb_f43_leverage_risk_bank_dyn_x_close_5d_base_v014_signal,
    f43lrb_f43_leverage_risk_bank_dyn_mean21_close_5d_base_v015_signal,
    f43lrb_f43_leverage_risk_bank_dyn_mean63_close_5d_base_v016_signal,
    f43lrb_f43_leverage_risk_bank_dyn_std21_close_5d_base_v017_signal,
    f43lrb_f43_leverage_risk_bank_dyn_std63_close_5d_base_v018_signal,
    f43lrb_f43_leverage_risk_bank_dyn_z63_close_5d_base_v019_signal,
    f43lrb_f43_leverage_risk_bank_dyn_z252_close_5d_base_v020_signal,
    f43lrb_f43_leverage_risk_bank_dyn_ema21_close_5d_base_v021_signal,
    f43lrb_f43_leverage_risk_bank_dyn_ema63_close_5d_base_v022_signal,
    f43lrb_f43_leverage_risk_bank_dyn_pct21_close_5d_base_v023_signal,
    f43lrb_f43_leverage_risk_bank_risk_x_close_5d_base_v024_signal,
    f43lrb_f43_leverage_risk_bank_risk_mean21_5d_base_v025_signal,
    f43lrb_f43_leverage_risk_bank_risk_mean63_5d_base_v026_signal,
    f43lrb_f43_leverage_risk_bank_risk_std21_5d_base_v027_signal,
    f43lrb_f43_leverage_risk_bank_risk_std63_5d_base_v028_signal,
    f43lrb_f43_leverage_risk_bank_risk_z63_5d_base_v029_signal,
    f43lrb_f43_leverage_risk_bank_risk_z252_5d_base_v030_signal,
    f43lrb_f43_leverage_risk_bank_risk_ema21_5d_base_v031_signal,
    f43lrb_f43_leverage_risk_bank_risk_ema63_5d_base_v032_signal,
    f43lrb_f43_leverage_risk_bank_risk_log_5d_base_v033_signal,
    f43lrb_f43_leverage_risk_bank_risk_sqrt_5d_base_v034_signal,
    f43lrb_f43_leverage_risk_bank_risk_pct21_5d_base_v035_signal,
    f43lrb_f43_leverage_risk_bank_risk_pct63_5d_base_v036_signal,
    f43lrb_f43_leverage_risk_bank_risk_diff21_5d_base_v037_signal,
    f43lrb_f43_leverage_risk_bank_risk_diff63_5d_base_v038_signal,
    f43lrb_f43_leverage_risk_bank_lev_x_dyn_5d_base_v039_signal,
    f43lrb_f43_leverage_risk_bank_lev_x_risk_5d_base_v040_signal,
    f43lrb_f43_leverage_risk_bank_dyn_x_risk_5d_base_v041_signal,
    f43lrb_f43_leverage_risk_bank_lev_minus_risk_5d_base_v042_signal,
    f43lrb_f43_leverage_risk_bank_lev_mean_close_10d_base_v043_signal,
    f43lrb_f43_leverage_risk_bank_lev_mean_close_p21_10d_base_v044_signal,
    f43lrb_f43_leverage_risk_bank_lev_std_close_10d_base_v045_signal,
    f43lrb_f43_leverage_risk_bank_lev_z_close_10d_base_v046_signal,
    f43lrb_f43_leverage_risk_bank_lev_z_close_p21_10d_base_v047_signal,
    f43lrb_f43_leverage_risk_bank_lev_ema_close_10d_base_v048_signal,
    f43lrb_f43_leverage_risk_bank_lev_ema_close_p63_10d_base_v049_signal,
    f43lrb_f43_leverage_risk_bank_lev_log_close_10d_base_v050_signal,
    f43lrb_f43_leverage_risk_bank_lev_sqrt_close_10d_base_v051_signal,
    f43lrb_f43_leverage_risk_bank_lev_pct_close_10d_base_v052_signal,
    f43lrb_f43_leverage_risk_bank_lev_diff_close_10d_base_v053_signal,
    f43lrb_f43_leverage_risk_bank_dyn_x_close_10d_base_v054_signal,
    f43lrb_f43_leverage_risk_bank_dyn_mean21_close_10d_base_v055_signal,
    f43lrb_f43_leverage_risk_bank_dyn_mean63_close_10d_base_v056_signal,
    f43lrb_f43_leverage_risk_bank_dyn_std21_close_10d_base_v057_signal,
    f43lrb_f43_leverage_risk_bank_dyn_std63_close_10d_base_v058_signal,
    f43lrb_f43_leverage_risk_bank_dyn_z63_close_10d_base_v059_signal,
    f43lrb_f43_leverage_risk_bank_dyn_z252_close_10d_base_v060_signal,
    f43lrb_f43_leverage_risk_bank_dyn_ema21_close_10d_base_v061_signal,
    f43lrb_f43_leverage_risk_bank_dyn_ema63_close_10d_base_v062_signal,
    f43lrb_f43_leverage_risk_bank_dyn_pct21_close_10d_base_v063_signal,
    f43lrb_f43_leverage_risk_bank_risk_x_close_10d_base_v064_signal,
    f43lrb_f43_leverage_risk_bank_risk_mean21_10d_base_v065_signal,
    f43lrb_f43_leverage_risk_bank_risk_mean63_10d_base_v066_signal,
    f43lrb_f43_leverage_risk_bank_risk_std21_10d_base_v067_signal,
    f43lrb_f43_leverage_risk_bank_risk_std63_10d_base_v068_signal,
    f43lrb_f43_leverage_risk_bank_risk_z63_10d_base_v069_signal,
    f43lrb_f43_leverage_risk_bank_risk_z252_10d_base_v070_signal,
    f43lrb_f43_leverage_risk_bank_risk_ema21_10d_base_v071_signal,
    f43lrb_f43_leverage_risk_bank_risk_ema63_10d_base_v072_signal,
    f43lrb_f43_leverage_risk_bank_risk_log_10d_base_v073_signal,
    f43lrb_f43_leverage_risk_bank_risk_sqrt_10d_base_v074_signal,
    f43lrb_f43_leverage_risk_bank_risk_pct21_10d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F43_LEVERAGE_RISK_BANK_REGISTRY_001_075 = REGISTRY

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
    domain_primitives = ('_f43_asset_equity_leverage', '_f43_leverage_dynamics', '_f43_leverage_risk_score')
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
    print(f"OK f43_leverage_risk_bank_base_001_075_claude: {n_features} features pass")
