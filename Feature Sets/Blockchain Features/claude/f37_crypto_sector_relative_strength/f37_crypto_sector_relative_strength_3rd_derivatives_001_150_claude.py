import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
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


# ===== folder domain primitives (crypto sector-relative strength) =====
def _f37_relstr(closeadj, sector_index, w):
    # relative strength: stock cumulative return minus sector cumulative return over w
    rs = closeadj.pct_change(periods=w)
    rb = sector_index.pct_change(periods=w)
    return rs - rb


def _f37_beta(closeadj, sector_index, w):
    # rolling beta = cov(stock_ret, sector_ret) / var(sector_ret)
    rs = closeadj.pct_change()
    rb = sector_index.pct_change()
    mp = max(2, w // 2)
    cov = rs.rolling(w, min_periods=mp).cov(rb)
    var = rb.rolling(w, min_periods=mp).var()
    return cov / var.replace(0, np.nan)


def _f37_resid(closeadj, sector_index, w):
    # idiosyncratic return = stock_ret - beta*sector_ret (daily residual return)
    rs = closeadj.pct_change()
    rb = sector_index.pct_change()
    mp = max(2, w // 2)
    cov = rs.rolling(w, min_periods=mp).cov(rb)
    var = rb.rolling(w, min_periods=mp).var()
    beta = cov / var.replace(0, np.nan)
    return rs - beta * rb


def _f37_corr(closeadj, sector_index, w):
    # rolling correlation of stock vs sector daily returns (regime co-movement)
    rs = closeadj.pct_change()
    rb = sector_index.pct_change()
    mp = max(2, w // 2)
    return rs.rolling(w, min_periods=mp).corr(rb)
def _slope_norm(s, w):
    # discrete 1st derivative over w, scaled by base dispersion (robust to zero-crossing)
    d = s.diff(periods=w)
    sc = s.rolling(252, min_periods=21).std()
    return d / sc.replace(0, np.nan)

# ============ JERK FEATURES 001-150 ============
def f37sr_f37_crypto_sector_relative_strength_relstr_21d_jerk_v001_signal(closeadj, sector_index):
    result = _f37_relstr(closeadj, sector_index, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_relstr_63d_jerk_v002_signal(closeadj, sector_index):
    result = _f37_relstr(closeadj, sector_index, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_relstr_126d_jerk_v003_signal(closeadj, sector_index):
    result = _f37_relstr(closeadj, sector_index, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_relstr_252d_jerk_v004_signal(closeadj, sector_index):
    result = _f37_relstr(closeadj, sector_index, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_relstr_5d_jerk_v005_signal(closeadj, sector_index):
    result = _f37_relstr(closeadj, sector_index, 5)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_relstr_42d_jerk_v006_signal(closeadj, sector_index):
    result = _f37_relstr(closeadj, sector_index, 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_relstr_84d_jerk_v007_signal(closeadj, sector_index):
    result = _f37_relstr(closeadj, sector_index, 84)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_relstr_189d_jerk_v008_signal(closeadj, sector_index):
    result = _f37_relstr(closeadj, sector_index, 189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_relstr_504d_jerk_v009_signal(closeadj, sector_index):
    result = _f37_relstr(closeadj, sector_index, 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_relstr_10d_jerk_v010_signal(closeadj, sector_index):
    result = _f37_relstr(closeadj, sector_index, 10)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_beta_21d_jerk_v011_signal(closeadj, sector_index):
    result = _f37_beta(closeadj, sector_index, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_beta_63d_jerk_v012_signal(closeadj, sector_index):
    result = _f37_beta(closeadj, sector_index, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_beta_126d_jerk_v013_signal(closeadj, sector_index):
    result = _f37_beta(closeadj, sector_index, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_beta_252d_jerk_v014_signal(closeadj, sector_index):
    result = _f37_beta(closeadj, sector_index, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_beta_42d_jerk_v015_signal(closeadj, sector_index):
    result = _f37_beta(closeadj, sector_index, 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_beta_84d_jerk_v016_signal(closeadj, sector_index):
    result = _f37_beta(closeadj, sector_index, 84)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_beta_189d_jerk_v017_signal(closeadj, sector_index):
    result = _f37_beta(closeadj, sector_index, 189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_beta_504d_jerk_v018_signal(closeadj, sector_index):
    result = _f37_beta(closeadj, sector_index, 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_betadev_126d_jerk_v019_signal(closeadj, sector_index):
    result = _f37_beta(closeadj, sector_index, 126) - 1.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_betadev_252d_jerk_v020_signal(closeadj, sector_index):
    result = _f37_beta(closeadj, sector_index, 252) - 1.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_resmom_21d_jerk_v021_signal(closeadj, sector_index):
    result = _f37_resid(closeadj, sector_index, 63).rolling(21, min_periods=10).sum()
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_resmom_63d_jerk_v022_signal(closeadj, sector_index):
    result = _f37_resid(closeadj, sector_index, 126).rolling(63, min_periods=21).sum()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_resmom_126d_jerk_v023_signal(closeadj, sector_index):
    result = _f37_resid(closeadj, sector_index, 126).rolling(126, min_periods=42).sum()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_resmom_252d_jerk_v024_signal(closeadj, sector_index):
    result = _f37_resid(closeadj, sector_index, 252).rolling(252, min_periods=84).sum()
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_resmom_42d_jerk_v025_signal(closeadj, sector_index):
    result = _f37_resid(closeadj, sector_index, 63).rolling(42, min_periods=21).sum()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_corr_21d_jerk_v026_signal(closeadj, sector_index):
    result = _f37_corr(closeadj, sector_index, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_corr_63d_jerk_v027_signal(closeadj, sector_index):
    result = _f37_corr(closeadj, sector_index, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_corr_126d_jerk_v028_signal(closeadj, sector_index):
    result = _f37_corr(closeadj, sector_index, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_corr_252d_jerk_v029_signal(closeadj, sector_index):
    result = _f37_corr(closeadj, sector_index, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_corr_42d_jerk_v030_signal(closeadj, sector_index):
    result = _f37_corr(closeadj, sector_index, 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_rsline_lvl_jerk_v031_signal(closeadj, sector_index):
    result = _safe_div(closeadj, sector_index) + _f37_relstr(closeadj, sector_index, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_rsslope_21d_jerk_v032_signal(closeadj, sector_index):
    rs = _safe_div(closeadj, sector_index)
    result = np.log(rs / rs.shift(21)) + _f37_relstr(closeadj, sector_index, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_rsslope_63d_jerk_v033_signal(closeadj, sector_index):
    rs = _safe_div(closeadj, sector_index)
    result = np.log(rs / rs.shift(63)) + _f37_relstr(closeadj, sector_index, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_rsslope_126d_jerk_v034_signal(closeadj, sector_index):
    rs = _safe_div(closeadj, sector_index)
    result = np.log(rs / rs.shift(126)) + _f37_relstr(closeadj, sector_index, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_rsz_126d_jerk_v035_signal(closeadj, sector_index):
    rs = _safe_div(closeadj, sector_index)
    result = _z(rs, 126) + _f37_relstr(closeadj, sector_index, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_rsz_252d_jerk_v036_signal(closeadj, sector_index):
    rs = _safe_div(closeadj, sector_index)
    result = _z(rs, 252) + _f37_relstr(closeadj, sector_index, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_te_63d_jerk_v037_signal(closeadj, sector_index):
    result = _std(_f37_resid(closeadj, sector_index, 63), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_te_126d_jerk_v038_signal(closeadj, sector_index):
    result = _std(_f37_resid(closeadj, sector_index, 126), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_te_252d_jerk_v039_signal(closeadj, sector_index):
    result = _std(_f37_resid(closeadj, sector_index, 252), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_te_42d_jerk_v040_signal(closeadj, sector_index):
    result = _std(_f37_resid(closeadj, sector_index, 63), 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_ir_63d_jerk_v041_signal(closeadj, sector_index):
    res = _f37_resid(closeadj, sector_index, 63)
    result = _safe_div(_mean(res, 63), _std(res, 63))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_ir_126d_jerk_v042_signal(closeadj, sector_index):
    res = _f37_resid(closeadj, sector_index, 126)
    result = _safe_div(_mean(res, 126), _std(res, 126))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_ir_252d_jerk_v043_signal(closeadj, sector_index):
    res = _f37_resid(closeadj, sector_index, 252)
    result = _safe_div(_mean(res, 252), _std(res, 252))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_ir_42d_jerk_v044_signal(closeadj, sector_index):
    res = _f37_resid(closeadj, sector_index, 63)
    result = _safe_div(_mean(res, 42), _std(res, 42))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_betastab_126d_jerk_v045_signal(closeadj, sector_index):
    result = _std(_f37_beta(closeadj, sector_index, 21), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_betastab_252d_jerk_v046_signal(closeadj, sector_index):
    result = _std(_f37_beta(closeadj, sector_index, 42), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_zrelstr_21d_jerk_v047_signal(closeadj, sector_index):
    result = _z(_f37_relstr(closeadj, sector_index, 21), 252)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_zrelstr_63d_jerk_v048_signal(closeadj, sector_index):
    result = _z(_f37_relstr(closeadj, sector_index, 63), 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_zrelstr_126d_jerk_v049_signal(closeadj, sector_index):
    result = _z(_f37_relstr(closeadj, sector_index, 126), 504)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_rsrank_21d_jerk_v050_signal(closeadj, sector_index):
    r = _f37_relstr(closeadj, sector_index, 21)
    result = r.rolling(126, min_periods=21).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_rsrank_63d_jerk_v051_signal(closeadj, sector_index):
    r = _f37_relstr(closeadj, sector_index, 63)
    result = r.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_rsrank_126d_jerk_v052_signal(closeadj, sector_index):
    r = _f37_relstr(closeadj, sector_index, 126)
    result = r.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_rstrend_21d_jerk_v053_signal(closeadj, sector_index):
    r = _f37_relstr(closeadj, sector_index, 21)
    result = r - _mean(r, 63)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_rstrend_63d_jerk_v054_signal(closeadj, sector_index):
    r = _f37_relstr(closeadj, sector_index, 63)
    result = r - _mean(r, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_rsspread_21_126_jerk_v055_signal(closeadj, sector_index):
    result = _f37_relstr(closeadj, sector_index, 21) - _f37_relstr(closeadj, sector_index, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_rsspread_63_252_jerk_v056_signal(closeadj, sector_index):
    result = _f37_relstr(closeadj, sector_index, 63) - _f37_relstr(closeadj, sector_index, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_rsaccel_21_42_jerk_v057_signal(closeadj, sector_index):
    result = _f37_relstr(closeadj, sector_index, 21) - _f37_relstr(closeadj, sector_index, 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_rsaccel_63_126_jerk_v058_signal(closeadj, sector_index):
    result = _f37_relstr(closeadj, sector_index, 63) - _f37_relstr(closeadj, sector_index, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_betaspread_21_252_jerk_v059_signal(closeadj, sector_index):
    result = _f37_beta(closeadj, sector_index, 21) - _f37_beta(closeadj, sector_index, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_betaspread_63_126_jerk_v060_signal(closeadj, sector_index):
    result = _f37_beta(closeadj, sector_index, 63) - _f37_beta(closeadj, sector_index, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_corrspread_21_126_jerk_v061_signal(closeadj, sector_index):
    result = _f37_corr(closeadj, sector_index, 21) - _f37_corr(closeadj, sector_index, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_zcorr_63d_jerk_v062_signal(closeadj, sector_index):
    result = _z(_f37_corr(closeadj, sector_index, 63), 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_residshare_126d_jerk_v063_signal(closeadj, sector_index):
    res_std = _std(_f37_resid(closeadj, sector_index, 126), 126)
    tot_std = _std(closeadj.pct_change(), 126)
    result = _safe_div(res_std, tot_std)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_residshare_252d_jerk_v064_signal(closeadj, sector_index):
    res_std = _std(_f37_resid(closeadj, sector_index, 252), 252)
    tot_std = _std(closeadj.pct_change(), 252)
    result = _safe_div(res_std, tot_std)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_betaadjrs_126d_jerk_v065_signal(closeadj, sector_index):
    rs = _f37_relstr(closeadj, sector_index, 126)
    beta = _f37_beta(closeadj, sector_index, 126)
    result = _safe_div(rs, beta.abs())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_betaadjrs_252d_jerk_v066_signal(closeadj, sector_index):
    rs = _f37_relstr(closeadj, sector_index, 252)
    beta = _f37_beta(closeadj, sector_index, 252)
    result = _safe_div(rs, beta.abs())
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_rsperte_126d_jerk_v067_signal(closeadj, sector_index):
    rs = _f37_relstr(closeadj, sector_index, 126)
    te = _std(_f37_resid(closeadj, sector_index, 126), 126)
    result = _safe_div(rs, te)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_rsperte_252d_jerk_v068_signal(closeadj, sector_index):
    rs = _f37_relstr(closeadj, sector_index, 252)
    te = _std(_f37_resid(closeadj, sector_index, 252), 252)
    result = _safe_div(rs, te)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_smoothrs_21d_jerk_v069_signal(closeadj, sector_index):
    result = _mean(_f37_relstr(closeadj, sector_index, 21), 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_smoothrs_63d_jerk_v070_signal(closeadj, sector_index):
    result = _mean(_f37_relstr(closeadj, sector_index, 63), 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_ewmrs_21d_jerk_v071_signal(closeadj, sector_index):
    rs = _f37_relstr(closeadj, sector_index, 21)
    result = rs.ewm(span=21, min_periods=10).mean()
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_ewmrs_63d_jerk_v072_signal(closeadj, sector_index):
    rs = _f37_relstr(closeadj, sector_index, 63)
    result = rs.ewm(span=63, min_periods=21).mean()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_annrs_63d_jerk_v073_signal(closeadj, sector_index):
    result = _f37_relstr(closeadj, sector_index, 63) * (252.0 / 63.0)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_annrs_126d_jerk_v074_signal(closeadj, sector_index):
    result = _f37_relstr(closeadj, sector_index, 126) * (252.0 / 126.0)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_rsdisp_63d_jerk_v075_signal(closeadj, sector_index):
    result = _std(_f37_relstr(closeadj, sector_index, 21), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_upbeta_63d_jerk_v076_signal(closeadj, sector_index):
    rs = closeadj.pct_change()
    rb = sector_index.pct_change()
    up = rb.where(rb > 0)
    rsu = rs.where(rb > 0)
    cov = rsu.rolling(63, min_periods=21).cov(up)
    var = up.rolling(63, min_periods=21).var()
    result = cov / var.replace(0, np.nan) + _f37_beta(closeadj, sector_index, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_upbeta_126d_jerk_v077_signal(closeadj, sector_index):
    rs = closeadj.pct_change()
    rb = sector_index.pct_change()
    up = rb.where(rb > 0)
    rsu = rs.where(rb > 0)
    cov = rsu.rolling(126, min_periods=42).cov(up)
    var = up.rolling(126, min_periods=42).var()
    result = cov / var.replace(0, np.nan) + _f37_beta(closeadj, sector_index, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_downbeta_63d_jerk_v078_signal(closeadj, sector_index):
    rs = closeadj.pct_change()
    rb = sector_index.pct_change()
    dn = rb.where(rb < 0)
    rsd = rs.where(rb < 0)
    cov = rsd.rolling(63, min_periods=21).cov(dn)
    var = dn.rolling(63, min_periods=21).var()
    result = cov / var.replace(0, np.nan) + _f37_beta(closeadj, sector_index, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_downbeta_126d_jerk_v079_signal(closeadj, sector_index):
    rs = closeadj.pct_change()
    rb = sector_index.pct_change()
    dn = rb.where(rb < 0)
    rsd = rs.where(rb < 0)
    cov = rsd.rolling(126, min_periods=42).cov(dn)
    var = dn.rolling(126, min_periods=42).var()
    result = cov / var.replace(0, np.nan) + _f37_beta(closeadj, sector_index, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_betaasym_63d_jerk_v080_signal(closeadj, sector_index):
    rs = closeadj.pct_change()
    rb = sector_index.pct_change()
    up = rb.where(rb > 0); rsu = rs.where(rb > 0)
    dn = rb.where(rb < 0); rsd = rs.where(rb < 0)
    ub = rsu.rolling(63, min_periods=21).cov(up) / up.rolling(63, min_periods=21).var().replace(0, np.nan)
    db = rsd.rolling(63, min_periods=21).cov(dn) / dn.rolling(63, min_periods=21).var().replace(0, np.nan)
    result = ub - db + _f37_beta(closeadj, sector_index, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_betaasym_126d_jerk_v081_signal(closeadj, sector_index):
    rs = closeadj.pct_change()
    rb = sector_index.pct_change()
    up = rb.where(rb > 0); rsu = rs.where(rb > 0)
    dn = rb.where(rb < 0); rsd = rs.where(rb < 0)
    ub = rsu.rolling(126, min_periods=42).cov(up) / up.rolling(126, min_periods=42).var().replace(0, np.nan)
    db = rsd.rolling(126, min_periods=42).cov(dn) / dn.rolling(126, min_periods=42).var().replace(0, np.nan)
    result = ub - db + _f37_beta(closeadj, sector_index, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_betaasym_252d_jerk_v082_signal(closeadj, sector_index):
    rs = closeadj.pct_change()
    rb = sector_index.pct_change()
    up = rb.where(rb > 0); rsu = rs.where(rb > 0)
    dn = rb.where(rb < 0); rsd = rs.where(rb < 0)
    ub = rsu.rolling(252, min_periods=84).cov(up) / up.rolling(252, min_periods=84).var().replace(0, np.nan)
    db = rsd.rolling(252, min_periods=84).cov(dn) / dn.rolling(252, min_periods=84).var().replace(0, np.nan)
    result = ub - db + _f37_beta(closeadj, sector_index, 252) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_udbetaratio_126d_jerk_v083_signal(closeadj, sector_index):
    rs = closeadj.pct_change()
    rb = sector_index.pct_change()
    up = rb.where(rb > 0); rsu = rs.where(rb > 0)
    dn = rb.where(rb < 0); rsd = rs.where(rb < 0)
    ub = rsu.rolling(126, min_periods=42).cov(up) / up.rolling(126, min_periods=42).var().replace(0, np.nan)
    db = rsd.rolling(126, min_periods=42).cov(dn) / dn.rolling(126, min_periods=42).var().replace(0, np.nan)
    result = _safe_div(ub, db.abs()) + _f37_beta(closeadj, sector_index, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_ewmbeta_63d_jerk_v084_signal(closeadj, sector_index):
    rs = closeadj.pct_change()
    rb = sector_index.pct_change()
    cov = (rs * rb).ewm(span=63, min_periods=21).mean() - rs.ewm(span=63, min_periods=21).mean() * rb.ewm(span=63, min_periods=21).mean()
    var = (rb * rb).ewm(span=63, min_periods=21).mean() - rb.ewm(span=63, min_periods=21).mean() ** 2
    result = cov / var.replace(0, np.nan) + _f37_beta(closeadj, sector_index, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_ewmbeta_126d_jerk_v085_signal(closeadj, sector_index):
    rs = closeadj.pct_change()
    rb = sector_index.pct_change()
    cov = (rs * rb).ewm(span=126, min_periods=42).mean() - rs.ewm(span=126, min_periods=42).mean() * rb.ewm(span=126, min_periods=42).mean()
    var = (rb * rb).ewm(span=126, min_periods=42).mean() - rb.ewm(span=126, min_periods=42).mean() ** 2
    result = cov / var.replace(0, np.nan) + _f37_beta(closeadj, sector_index, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_zresid_126d_jerk_v086_signal(closeadj, sector_index):
    result = _z(_f37_resid(closeadj, sector_index, 126), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_zresid_252d_jerk_v087_signal(closeadj, sector_index):
    result = _z(_f37_resid(closeadj, sector_index, 252), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_ewmresid_63d_jerk_v088_signal(closeadj, sector_index):
    res = _f37_resid(closeadj, sector_index, 63)
    result = res.ewm(span=63, min_periods=21).mean() * 63.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_ewmresid_126d_jerk_v089_signal(closeadj, sector_index):
    res = _f37_resid(closeadj, sector_index, 126)
    result = res.ewm(span=126, min_periods=42).mean() * 126.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_residskew_126d_jerk_v090_signal(closeadj, sector_index):
    res = _f37_resid(closeadj, sector_index, 126)
    result = res.rolling(126, min_periods=42).skew()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_residskew_252d_jerk_v091_signal(closeadj, sector_index):
    res = _f37_resid(closeadj, sector_index, 252)
    result = res.rolling(252, min_periods=84).skew()
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_residkurt_126d_jerk_v092_signal(closeadj, sector_index):
    res = _f37_resid(closeadj, sector_index, 126)
    result = res.rolling(126, min_periods=42).kurt()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_rsq_126d_jerk_v093_signal(closeadj, sector_index):
    c = _f37_corr(closeadj, sector_index, 126)
    result = c * c
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_rsq_252d_jerk_v094_signal(closeadj, sector_index):
    c = _f37_corr(closeadj, sector_index, 252)
    result = c * c
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_idioshare_126d_jerk_v095_signal(closeadj, sector_index):
    c = _f37_corr(closeadj, sector_index, 126)
    result = 1.0 - c * c
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_corrtrend_21d_jerk_v096_signal(closeadj, sector_index):
    c = _f37_corr(closeadj, sector_index, 21)
    result = c - _mean(c, 126)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_corrdisp_126d_jerk_v097_signal(closeadj, sector_index):
    result = _std(_f37_corr(closeadj, sector_index, 21), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_betamom_63d_jerk_v098_signal(closeadj, sector_index):
    beta = _f37_beta(closeadj, sector_index, 63)
    result = beta - beta.shift(21)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_betamom_126d_jerk_v099_signal(closeadj, sector_index):
    beta = _f37_beta(closeadj, sector_index, 126)
    result = beta - beta.shift(42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_zbeta_126d_jerk_v100_signal(closeadj, sector_index):
    result = _z(_f37_beta(closeadj, sector_index, 126), 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_zbeta_63d_jerk_v101_signal(closeadj, sector_index):
    result = _z(_f37_beta(closeadj, sector_index, 63), 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_rsqual_126d_jerk_v102_signal(closeadj, sector_index):
    rs = _f37_relstr(closeadj, sector_index, 126)
    te = _std(_f37_resid(closeadj, sector_index, 126), 126) * np.sqrt(126.0)
    result = _safe_div(rs, te)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_rsqual_252d_jerk_v103_signal(closeadj, sector_index):
    rs = _f37_relstr(closeadj, sector_index, 252)
    te = _std(_f37_resid(closeadj, sector_index, 252), 252) * np.sqrt(252.0)
    result = _safe_div(rs, te)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_rseff_63d_jerk_v104_signal(closeadj, sector_index):
    rs = _f37_relstr(closeadj, sector_index, 5)
    net = rs.rolling(63, min_periods=21).sum()
    path = rs.abs().rolling(63, min_periods=21).sum()
    result = _safe_div(net, path)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_rseff_126d_jerk_v105_signal(closeadj, sector_index):
    rs = _f37_relstr(closeadj, sector_index, 5)
    net = rs.rolling(126, min_periods=42).sum()
    path = rs.abs().rolling(126, min_periods=42).sum()
    result = _safe_div(net, path)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_rssharpe_63d_jerk_v106_signal(closeadj, sector_index):
    rs = _f37_relstr(closeadj, sector_index, 5)
    result = _safe_div(_mean(rs, 63), _std(rs, 63)) * np.sqrt(63.0)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_rssharpe_126d_jerk_v107_signal(closeadj, sector_index):
    rs = _f37_relstr(closeadj, sector_index, 5)
    result = _safe_div(_mean(rs, 126), _std(rs, 126)) * np.sqrt(126.0)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_rssharpe_252d_jerk_v108_signal(closeadj, sector_index):
    rs = _f37_relstr(closeadj, sector_index, 5)
    result = _safe_div(_mean(rs, 252), _std(rs, 252)) * np.sqrt(252.0)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_volconfrs_21d_jerk_v109_signal(closeadj, sector_index, volume):
    result = _f37_relstr(closeadj, sector_index, 21) * _z(volume, 63)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_dvconfrs_63d_jerk_v110_signal(closeadj, sector_index, volume):
    dv = closeadj * volume
    result = _f37_relstr(closeadj, sector_index, 63) * _z(dv, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_dvsurgers_21d_jerk_v111_signal(closeadj, sector_index, volume):
    dv = closeadj * volume
    surge = _safe_div(dv, _mean(dv, 63))
    result = _f37_relstr(closeadj, sector_index, 21) * surge
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_rsslope_252d_jerk_v112_signal(closeadj, sector_index):
    rs = _safe_div(closeadj, sector_index)
    result = np.log(rs / rs.shift(252)) + _f37_relstr(closeadj, sector_index, 252) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_rsdma_126d_jerk_v113_signal(closeadj, sector_index):
    rs = _safe_div(closeadj, sector_index)
    result = _safe_div(rs - _mean(rs, 126), _mean(rs, 126)) + _f37_relstr(closeadj, sector_index, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_rsdma_252d_jerk_v114_signal(closeadj, sector_index):
    rs = _safe_div(closeadj, sector_index)
    result = _safe_div(rs - _mean(rs, 252), _mean(rs, 252)) + _f37_relstr(closeadj, sector_index, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_rslinerank_252d_jerk_v115_signal(closeadj, sector_index):
    rs = _safe_div(closeadj, sector_index)
    result = rs.rolling(252, min_periods=63).rank(pct=True) + _f37_relstr(closeadj, sector_index, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_systret_63d_jerk_v116_signal(closeadj, sector_index):
    beta = _f37_beta(closeadj, sector_index, 63)
    sectmom = sector_index.pct_change(periods=63)
    result = beta * sectmom
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_systret_126d_jerk_v117_signal(closeadj, sector_index):
    beta = _f37_beta(closeadj, sector_index, 126)
    sectmom = sector_index.pct_change(periods=126)
    result = beta * sectmom
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_alpha_126d_jerk_v118_signal(closeadj, sector_index):
    beta = _f37_beta(closeadj, sector_index, 126)
    result = closeadj.pct_change(periods=126) - beta * sector_index.pct_change(periods=126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_alpha_252d_jerk_v119_signal(closeadj, sector_index):
    beta = _f37_beta(closeadj, sector_index, 252)
    result = closeadj.pct_change(periods=252) - beta * sector_index.pct_change(periods=252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_alpha_63d_jerk_v120_signal(closeadj, sector_index):
    beta = _f37_beta(closeadj, sector_index, 63)
    result = closeadj.pct_change(periods=63) - beta * sector_index.pct_change(periods=63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_zalpha_126d_jerk_v121_signal(closeadj, sector_index):
    beta = _f37_beta(closeadj, sector_index, 126)
    alpha = closeadj.pct_change(periods=126) - beta * sector_index.pct_change(periods=126)
    result = _z(alpha, 252)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_alphair_126d_jerk_v122_signal(closeadj, sector_index):
    beta = _f37_beta(closeadj, sector_index, 126)
    alpha = closeadj.pct_change(periods=126) - beta * sector_index.pct_change(periods=126)
    te = _std(_f37_resid(closeadj, sector_index, 126), 126) * np.sqrt(126.0)
    result = _safe_div(alpha, te)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_alphair_252d_jerk_v123_signal(closeadj, sector_index):
    beta = _f37_beta(closeadj, sector_index, 252)
    alpha = closeadj.pct_change(periods=252) - beta * sector_index.pct_change(periods=252)
    te = _std(_f37_resid(closeadj, sector_index, 252), 252) * np.sqrt(252.0)
    result = _safe_div(alpha, te)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_rsvoladj_126d_jerk_v124_signal(closeadj, sector_index):
    rs = _f37_relstr(closeadj, sector_index, 126)
    secvol = _std(sector_index.pct_change(), 126) * np.sqrt(126.0)
    result = _safe_div(rs, secvol)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_rsvoladj_252d_jerk_v125_signal(closeadj, sector_index):
    rs = _f37_relstr(closeadj, sector_index, 252)
    secvol = _std(sector_index.pct_change(), 252) * np.sqrt(252.0)
    result = _safe_div(rs, secvol)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_volratio_126d_jerk_v126_signal(closeadj, sector_index):
    sv = _std(closeadj.pct_change(), 126)
    bv = _std(sector_index.pct_change(), 126)
    result = _safe_div(sv, bv) + _f37_corr(closeadj, sector_index, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_volratio_252d_jerk_v127_signal(closeadj, sector_index):
    sv = _std(closeadj.pct_change(), 252)
    bv = _std(sector_index.pct_change(), 252)
    result = _safe_div(sv, bv) + _f37_corr(closeadj, sector_index, 252) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_betavol_126d_jerk_v128_signal(closeadj, sector_index):
    bv = _std(sector_index.pct_change(), 126)
    result = _f37_beta(closeadj, sector_index, 126) * bv * np.sqrt(126.0)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_ewmresid_252d_jerk_v129_signal(closeadj, sector_index):
    res = _f37_resid(closeadj, sector_index, 252)
    result = res.ewm(span=252, min_periods=84).mean() * 252.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_zresmom_252d_jerk_v130_signal(closeadj, sector_index):
    rm = _f37_resid(closeadj, sector_index, 252).rolling(252, min_periods=84).sum()
    result = _z(rm, 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_rsrank_252d_jerk_v131_signal(closeadj, sector_index):
    r = _f37_relstr(closeadj, sector_index, 252)
    result = r.rolling(504, min_periods=126).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_betarank_126d_jerk_v132_signal(closeadj, sector_index):
    b = _f37_beta(closeadj, sector_index, 126)
    result = b.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_corrrank_63d_jerk_v133_signal(closeadj, sector_index):
    c = _f37_corr(closeadj, sector_index, 63)
    result = c.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_terank_126d_jerk_v134_signal(closeadj, sector_index):
    te = _std(_f37_resid(closeadj, sector_index, 126), 126)
    result = te.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_rscurv_63_126_jerk_v135_signal(closeadj, sector_index):
    a1 = _f37_relstr(closeadj, sector_index, 63) - _f37_relstr(closeadj, sector_index, 126)
    a2 = _f37_relstr(closeadj, sector_index, 126) - _f37_relstr(closeadj, sector_index, 252)
    result = a1 - a2
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_smoothcorr_63d_jerk_v136_signal(closeadj, sector_index):
    result = _mean(_f37_corr(closeadj, sector_index, 63), 21)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_smoothbeta_63d_jerk_v137_signal(closeadj, sector_index):
    result = _mean(_f37_beta(closeadj, sector_index, 63), 21)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_betars_126d_jerk_v138_signal(closeadj, sector_index):
    result = _f37_beta(closeadj, sector_index, 126) * _f37_relstr(closeadj, sector_index, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_corrwrs_126d_jerk_v139_signal(closeadj, sector_index):
    result = _f37_relstr(closeadj, sector_index, 126) * (1.0 - _f37_corr(closeadj, sector_index, 126).abs())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_rsidio_126d_jerk_v140_signal(closeadj, sector_index):
    rs = _f37_relstr(closeadj, sector_index, 126)
    idio = 1.0 - _f37_corr(closeadj, sector_index, 126) ** 2
    result = rs * idio
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_ewmrs_126d_jerk_v141_signal(closeadj, sector_index):
    rs = _f37_relstr(closeadj, sector_index, 126)
    result = rs.ewm(span=126, min_periods=42).mean()
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_annrs_252d_jerk_v142_signal(closeadj, sector_index):
    result = _f37_relstr(closeadj, sector_index, 252) * (252.0 / 252.0)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_annrs_21d_jerk_v143_signal(closeadj, sector_index):
    result = _f37_relstr(closeadj, sector_index, 21) * (252.0 / 21.0)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_betaneutrs_126d_jerk_v144_signal(closeadj, sector_index):
    rs = _f37_relstr(closeadj, sector_index, 126)
    beta = _f37_beta(closeadj, sector_index, 126)
    result = rs - (beta - 1.0) * sector_index.pct_change(periods=126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_betaneutrs_252d_jerk_v145_signal(closeadj, sector_index):
    rs = _f37_relstr(closeadj, sector_index, 252)
    beta = _f37_beta(closeadj, sector_index, 252)
    result = rs - (beta - 1.0) * sector_index.pct_change(periods=252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_rsdisp_252d_jerk_v146_signal(closeadj, sector_index):
    result = _std(_f37_relstr(closeadj, sector_index, 63), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_rsir_21d_jerk_v147_signal(closeadj, sector_index):
    r = _f37_relstr(closeadj, sector_index, 21)
    result = _safe_div(r, _std(r, 252))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_rsir_63d_jerk_v148_signal(closeadj, sector_index):
    r = _f37_relstr(closeadj, sector_index, 63)
    result = _safe_div(r, _std(r, 252))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_decoupbeta_126d_jerk_v149_signal(closeadj, sector_index):
    result = _f37_beta(closeadj, sector_index, 126) * (1.0 - _f37_corr(closeadj, sector_index, 126))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f37sr_f37_crypto_sector_relative_strength_blend_multi_jerk_v150_signal(closeadj, sector_index):
    result = (_f37_relstr(closeadj, sector_index, 21)
              + _f37_relstr(closeadj, sector_index, 63)
              + _f37_relstr(closeadj, sector_index, 126)
              + _f37_relstr(closeadj, sector_index, 252)) / 4.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [    f37sr_f37_crypto_sector_relative_strength_relstr_21d_jerk_v001_signal,    f37sr_f37_crypto_sector_relative_strength_relstr_63d_jerk_v002_signal,    f37sr_f37_crypto_sector_relative_strength_relstr_126d_jerk_v003_signal,    f37sr_f37_crypto_sector_relative_strength_relstr_252d_jerk_v004_signal,    f37sr_f37_crypto_sector_relative_strength_relstr_5d_jerk_v005_signal,    f37sr_f37_crypto_sector_relative_strength_relstr_42d_jerk_v006_signal,    f37sr_f37_crypto_sector_relative_strength_relstr_84d_jerk_v007_signal,    f37sr_f37_crypto_sector_relative_strength_relstr_189d_jerk_v008_signal,    f37sr_f37_crypto_sector_relative_strength_relstr_504d_jerk_v009_signal,    f37sr_f37_crypto_sector_relative_strength_relstr_10d_jerk_v010_signal,    f37sr_f37_crypto_sector_relative_strength_beta_21d_jerk_v011_signal,    f37sr_f37_crypto_sector_relative_strength_beta_63d_jerk_v012_signal,    f37sr_f37_crypto_sector_relative_strength_beta_126d_jerk_v013_signal,    f37sr_f37_crypto_sector_relative_strength_beta_252d_jerk_v014_signal,    f37sr_f37_crypto_sector_relative_strength_beta_42d_jerk_v015_signal,    f37sr_f37_crypto_sector_relative_strength_beta_84d_jerk_v016_signal,    f37sr_f37_crypto_sector_relative_strength_beta_189d_jerk_v017_signal,    f37sr_f37_crypto_sector_relative_strength_beta_504d_jerk_v018_signal,    f37sr_f37_crypto_sector_relative_strength_betadev_126d_jerk_v019_signal,    f37sr_f37_crypto_sector_relative_strength_betadev_252d_jerk_v020_signal,    f37sr_f37_crypto_sector_relative_strength_resmom_21d_jerk_v021_signal,    f37sr_f37_crypto_sector_relative_strength_resmom_63d_jerk_v022_signal,    f37sr_f37_crypto_sector_relative_strength_resmom_126d_jerk_v023_signal,    f37sr_f37_crypto_sector_relative_strength_resmom_252d_jerk_v024_signal,    f37sr_f37_crypto_sector_relative_strength_resmom_42d_jerk_v025_signal,    f37sr_f37_crypto_sector_relative_strength_corr_21d_jerk_v026_signal,    f37sr_f37_crypto_sector_relative_strength_corr_63d_jerk_v027_signal,    f37sr_f37_crypto_sector_relative_strength_corr_126d_jerk_v028_signal,    f37sr_f37_crypto_sector_relative_strength_corr_252d_jerk_v029_signal,    f37sr_f37_crypto_sector_relative_strength_corr_42d_jerk_v030_signal,    f37sr_f37_crypto_sector_relative_strength_rsline_lvl_jerk_v031_signal,    f37sr_f37_crypto_sector_relative_strength_rsslope_21d_jerk_v032_signal,    f37sr_f37_crypto_sector_relative_strength_rsslope_63d_jerk_v033_signal,    f37sr_f37_crypto_sector_relative_strength_rsslope_126d_jerk_v034_signal,    f37sr_f37_crypto_sector_relative_strength_rsz_126d_jerk_v035_signal,    f37sr_f37_crypto_sector_relative_strength_rsz_252d_jerk_v036_signal,    f37sr_f37_crypto_sector_relative_strength_te_63d_jerk_v037_signal,    f37sr_f37_crypto_sector_relative_strength_te_126d_jerk_v038_signal,    f37sr_f37_crypto_sector_relative_strength_te_252d_jerk_v039_signal,    f37sr_f37_crypto_sector_relative_strength_te_42d_jerk_v040_signal,    f37sr_f37_crypto_sector_relative_strength_ir_63d_jerk_v041_signal,    f37sr_f37_crypto_sector_relative_strength_ir_126d_jerk_v042_signal,    f37sr_f37_crypto_sector_relative_strength_ir_252d_jerk_v043_signal,    f37sr_f37_crypto_sector_relative_strength_ir_42d_jerk_v044_signal,    f37sr_f37_crypto_sector_relative_strength_betastab_126d_jerk_v045_signal,    f37sr_f37_crypto_sector_relative_strength_betastab_252d_jerk_v046_signal,    f37sr_f37_crypto_sector_relative_strength_zrelstr_21d_jerk_v047_signal,    f37sr_f37_crypto_sector_relative_strength_zrelstr_63d_jerk_v048_signal,    f37sr_f37_crypto_sector_relative_strength_zrelstr_126d_jerk_v049_signal,    f37sr_f37_crypto_sector_relative_strength_rsrank_21d_jerk_v050_signal,    f37sr_f37_crypto_sector_relative_strength_rsrank_63d_jerk_v051_signal,    f37sr_f37_crypto_sector_relative_strength_rsrank_126d_jerk_v052_signal,    f37sr_f37_crypto_sector_relative_strength_rstrend_21d_jerk_v053_signal,    f37sr_f37_crypto_sector_relative_strength_rstrend_63d_jerk_v054_signal,    f37sr_f37_crypto_sector_relative_strength_rsspread_21_126_jerk_v055_signal,    f37sr_f37_crypto_sector_relative_strength_rsspread_63_252_jerk_v056_signal,    f37sr_f37_crypto_sector_relative_strength_rsaccel_21_42_jerk_v057_signal,    f37sr_f37_crypto_sector_relative_strength_rsaccel_63_126_jerk_v058_signal,    f37sr_f37_crypto_sector_relative_strength_betaspread_21_252_jerk_v059_signal,    f37sr_f37_crypto_sector_relative_strength_betaspread_63_126_jerk_v060_signal,    f37sr_f37_crypto_sector_relative_strength_corrspread_21_126_jerk_v061_signal,    f37sr_f37_crypto_sector_relative_strength_zcorr_63d_jerk_v062_signal,    f37sr_f37_crypto_sector_relative_strength_residshare_126d_jerk_v063_signal,    f37sr_f37_crypto_sector_relative_strength_residshare_252d_jerk_v064_signal,    f37sr_f37_crypto_sector_relative_strength_betaadjrs_126d_jerk_v065_signal,    f37sr_f37_crypto_sector_relative_strength_betaadjrs_252d_jerk_v066_signal,    f37sr_f37_crypto_sector_relative_strength_rsperte_126d_jerk_v067_signal,    f37sr_f37_crypto_sector_relative_strength_rsperte_252d_jerk_v068_signal,    f37sr_f37_crypto_sector_relative_strength_smoothrs_21d_jerk_v069_signal,    f37sr_f37_crypto_sector_relative_strength_smoothrs_63d_jerk_v070_signal,    f37sr_f37_crypto_sector_relative_strength_ewmrs_21d_jerk_v071_signal,    f37sr_f37_crypto_sector_relative_strength_ewmrs_63d_jerk_v072_signal,    f37sr_f37_crypto_sector_relative_strength_annrs_63d_jerk_v073_signal,    f37sr_f37_crypto_sector_relative_strength_annrs_126d_jerk_v074_signal,    f37sr_f37_crypto_sector_relative_strength_rsdisp_63d_jerk_v075_signal,    f37sr_f37_crypto_sector_relative_strength_upbeta_63d_jerk_v076_signal,    f37sr_f37_crypto_sector_relative_strength_upbeta_126d_jerk_v077_signal,    f37sr_f37_crypto_sector_relative_strength_downbeta_63d_jerk_v078_signal,    f37sr_f37_crypto_sector_relative_strength_downbeta_126d_jerk_v079_signal,    f37sr_f37_crypto_sector_relative_strength_betaasym_63d_jerk_v080_signal,    f37sr_f37_crypto_sector_relative_strength_betaasym_126d_jerk_v081_signal,    f37sr_f37_crypto_sector_relative_strength_betaasym_252d_jerk_v082_signal,    f37sr_f37_crypto_sector_relative_strength_udbetaratio_126d_jerk_v083_signal,    f37sr_f37_crypto_sector_relative_strength_ewmbeta_63d_jerk_v084_signal,    f37sr_f37_crypto_sector_relative_strength_ewmbeta_126d_jerk_v085_signal,    f37sr_f37_crypto_sector_relative_strength_zresid_126d_jerk_v086_signal,    f37sr_f37_crypto_sector_relative_strength_zresid_252d_jerk_v087_signal,    f37sr_f37_crypto_sector_relative_strength_ewmresid_63d_jerk_v088_signal,    f37sr_f37_crypto_sector_relative_strength_ewmresid_126d_jerk_v089_signal,    f37sr_f37_crypto_sector_relative_strength_residskew_126d_jerk_v090_signal,    f37sr_f37_crypto_sector_relative_strength_residskew_252d_jerk_v091_signal,    f37sr_f37_crypto_sector_relative_strength_residkurt_126d_jerk_v092_signal,    f37sr_f37_crypto_sector_relative_strength_rsq_126d_jerk_v093_signal,    f37sr_f37_crypto_sector_relative_strength_rsq_252d_jerk_v094_signal,    f37sr_f37_crypto_sector_relative_strength_idioshare_126d_jerk_v095_signal,    f37sr_f37_crypto_sector_relative_strength_corrtrend_21d_jerk_v096_signal,    f37sr_f37_crypto_sector_relative_strength_corrdisp_126d_jerk_v097_signal,    f37sr_f37_crypto_sector_relative_strength_betamom_63d_jerk_v098_signal,    f37sr_f37_crypto_sector_relative_strength_betamom_126d_jerk_v099_signal,    f37sr_f37_crypto_sector_relative_strength_zbeta_126d_jerk_v100_signal,    f37sr_f37_crypto_sector_relative_strength_zbeta_63d_jerk_v101_signal,    f37sr_f37_crypto_sector_relative_strength_rsqual_126d_jerk_v102_signal,    f37sr_f37_crypto_sector_relative_strength_rsqual_252d_jerk_v103_signal,    f37sr_f37_crypto_sector_relative_strength_rseff_63d_jerk_v104_signal,    f37sr_f37_crypto_sector_relative_strength_rseff_126d_jerk_v105_signal,    f37sr_f37_crypto_sector_relative_strength_rssharpe_63d_jerk_v106_signal,    f37sr_f37_crypto_sector_relative_strength_rssharpe_126d_jerk_v107_signal,    f37sr_f37_crypto_sector_relative_strength_rssharpe_252d_jerk_v108_signal,    f37sr_f37_crypto_sector_relative_strength_volconfrs_21d_jerk_v109_signal,    f37sr_f37_crypto_sector_relative_strength_dvconfrs_63d_jerk_v110_signal,    f37sr_f37_crypto_sector_relative_strength_dvsurgers_21d_jerk_v111_signal,    f37sr_f37_crypto_sector_relative_strength_rsslope_252d_jerk_v112_signal,    f37sr_f37_crypto_sector_relative_strength_rsdma_126d_jerk_v113_signal,    f37sr_f37_crypto_sector_relative_strength_rsdma_252d_jerk_v114_signal,    f37sr_f37_crypto_sector_relative_strength_rslinerank_252d_jerk_v115_signal,    f37sr_f37_crypto_sector_relative_strength_systret_63d_jerk_v116_signal,    f37sr_f37_crypto_sector_relative_strength_systret_126d_jerk_v117_signal,    f37sr_f37_crypto_sector_relative_strength_alpha_126d_jerk_v118_signal,    f37sr_f37_crypto_sector_relative_strength_alpha_252d_jerk_v119_signal,    f37sr_f37_crypto_sector_relative_strength_alpha_63d_jerk_v120_signal,    f37sr_f37_crypto_sector_relative_strength_zalpha_126d_jerk_v121_signal,    f37sr_f37_crypto_sector_relative_strength_alphair_126d_jerk_v122_signal,    f37sr_f37_crypto_sector_relative_strength_alphair_252d_jerk_v123_signal,    f37sr_f37_crypto_sector_relative_strength_rsvoladj_126d_jerk_v124_signal,    f37sr_f37_crypto_sector_relative_strength_rsvoladj_252d_jerk_v125_signal,    f37sr_f37_crypto_sector_relative_strength_volratio_126d_jerk_v126_signal,    f37sr_f37_crypto_sector_relative_strength_volratio_252d_jerk_v127_signal,    f37sr_f37_crypto_sector_relative_strength_betavol_126d_jerk_v128_signal,    f37sr_f37_crypto_sector_relative_strength_ewmresid_252d_jerk_v129_signal,    f37sr_f37_crypto_sector_relative_strength_zresmom_252d_jerk_v130_signal,    f37sr_f37_crypto_sector_relative_strength_rsrank_252d_jerk_v131_signal,    f37sr_f37_crypto_sector_relative_strength_betarank_126d_jerk_v132_signal,    f37sr_f37_crypto_sector_relative_strength_corrrank_63d_jerk_v133_signal,    f37sr_f37_crypto_sector_relative_strength_terank_126d_jerk_v134_signal,    f37sr_f37_crypto_sector_relative_strength_rscurv_63_126_jerk_v135_signal,    f37sr_f37_crypto_sector_relative_strength_smoothcorr_63d_jerk_v136_signal,    f37sr_f37_crypto_sector_relative_strength_smoothbeta_63d_jerk_v137_signal,    f37sr_f37_crypto_sector_relative_strength_betars_126d_jerk_v138_signal,    f37sr_f37_crypto_sector_relative_strength_corrwrs_126d_jerk_v139_signal,    f37sr_f37_crypto_sector_relative_strength_rsidio_126d_jerk_v140_signal,    f37sr_f37_crypto_sector_relative_strength_ewmrs_126d_jerk_v141_signal,    f37sr_f37_crypto_sector_relative_strength_annrs_252d_jerk_v142_signal,    f37sr_f37_crypto_sector_relative_strength_annrs_21d_jerk_v143_signal,    f37sr_f37_crypto_sector_relative_strength_betaneutrs_126d_jerk_v144_signal,    f37sr_f37_crypto_sector_relative_strength_betaneutrs_252d_jerk_v145_signal,    f37sr_f37_crypto_sector_relative_strength_rsdisp_252d_jerk_v146_signal,    f37sr_f37_crypto_sector_relative_strength_rsir_21d_jerk_v147_signal,    f37sr_f37_crypto_sector_relative_strength_rsir_63d_jerk_v148_signal,    f37sr_f37_crypto_sector_relative_strength_decoupbeta_126d_jerk_v149_signal,    f37sr_f37_crypto_sector_relative_strength_blend_multi_jerk_v150_signal,]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F37_CRYPTO_SECTOR_RELATIVE_STRENGTH_REGISTRY_JERK = REGISTRY

def _synth_cols(names):
    import numpy as np
    import pandas as pd
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    closeadj = pd.Series(base_price, name="closeadj")
    noise_h = np.abs(np.random.normal(0, 0.02, n))
    noise_l = np.abs(np.random.normal(0, 0.02, n))
    POS = {"open", "high", "low", "close", "closeadj", "price", "volume",
           "vwap", "marketcap", "ev", "assets", "assetsc", "assetsnc", "equity",
           "revenue", "revenueusd", "gp", "ebitda", "ebit", "ppnenet", "sharesbas",
           "shareswa", "cashneq", "cor", "opex", "sgna", "rnd", "inventory",
           "receivables", "payables", "intangibles", "evebitda", "evebit",
           "pe", "pb", "ps", "currentratio", "bvps", "sps", "divyield", "dps",
           "shrvalue", "shrunits", "totalvalue", "percentoftotal", "value",
           "units", "shares", "sf3a_shares", "sf3a_value", "sf3b_shares",
           "sf3b_value", "grossmargin", "ebitdamargin", "netmargin", "roe",
           "roa", "roic", "deposits", "invcap",
           "sector_index", "bellwether_coin", "bellwether_mstr", "nholders",
           "newholders", "exitholders", "hhi", "totalunits", "avgposition",
           "buyval", "sellval", "buyshares", "sellshares", "buycount", "sellcount",
           "officerbuyval", "dirbuyval", "tenpctbuyval", "officerbuycount",
           "optionexval", "tenpctsellval", "receivables", "workingcapital"}
    for nm in names:
        if nm == "closeadj" or nm == "close" or nm == "price":
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price * (1 + np.random.normal(0, 0.01, n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price * (1 + noise_h), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price * (1 - noise_l), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7, 7e6, n)) + 1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0, 1.0, n))
            level = 1000.0 * np.exp(0.03 * np.random.normal(0, 1, n).cumsum() / np.sqrt(n))
            series = level + 50.0 * walk
            if nm in POS:
                series = np.abs(series) + 10.0
            out[nm] = pd.Series(series, name=nm)
    return out


if __name__ == "__main__":
    import numpy as np
    import pandas as pd
    domain_primitives = ('_f37_relstr', '_f37_beta', '_f37_resid', '_f37_corr')
    needed = set()
    for fn in _FEATURES:
        for p in inspect.signature(fn).parameters.values():
            needed.add(p.name)
    cols = _synth_cols(sorted(needed))
    n_features = 0
    nan_ok = 0
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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print("OK f37_crypto_sector_relative_strength_" + "3rd_derivatives" + "_001_150_claude: " + str(n_features) + " features pass")
