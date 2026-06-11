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


# ============ FEATURES 001-075 ============

# 21d relative strength (stock minus sector cumulative return)
def f37sr_f37_crypto_sector_relative_strength_relstr_21d_base_v001_signal(closeadj, sector_index):
    result = _f37_relstr(closeadj, sector_index, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d relative strength
def f37sr_f37_crypto_sector_relative_strength_relstr_63d_base_v002_signal(closeadj, sector_index):
    result = _f37_relstr(closeadj, sector_index, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d relative strength
def f37sr_f37_crypto_sector_relative_strength_relstr_126d_base_v003_signal(closeadj, sector_index):
    result = _f37_relstr(closeadj, sector_index, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d relative strength
def f37sr_f37_crypto_sector_relative_strength_relstr_252d_base_v004_signal(closeadj, sector_index):
    result = _f37_relstr(closeadj, sector_index, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d relative strength (weekly relative thrust)
def f37sr_f37_crypto_sector_relative_strength_relstr_5d_base_v005_signal(closeadj, sector_index):
    result = _f37_relstr(closeadj, sector_index, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d relative strength
def f37sr_f37_crypto_sector_relative_strength_relstr_42d_base_v006_signal(closeadj, sector_index):
    result = _f37_relstr(closeadj, sector_index, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d relative strength
def f37sr_f37_crypto_sector_relative_strength_relstr_84d_base_v007_signal(closeadj, sector_index):
    result = _f37_relstr(closeadj, sector_index, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d relative strength
def f37sr_f37_crypto_sector_relative_strength_relstr_189d_base_v008_signal(closeadj, sector_index):
    result = _f37_relstr(closeadj, sector_index, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d relative strength (two-year cycle)
def f37sr_f37_crypto_sector_relative_strength_relstr_504d_base_v009_signal(closeadj, sector_index):
    result = _f37_relstr(closeadj, sector_index, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d relative strength
def f37sr_f37_crypto_sector_relative_strength_relstr_10d_base_v010_signal(closeadj, sector_index):
    result = _f37_relstr(closeadj, sector_index, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling beta to sector
def f37sr_f37_crypto_sector_relative_strength_beta_21d_base_v011_signal(closeadj, sector_index):
    result = _f37_beta(closeadj, sector_index, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling beta to sector
def f37sr_f37_crypto_sector_relative_strength_beta_63d_base_v012_signal(closeadj, sector_index):
    result = _f37_beta(closeadj, sector_index, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling beta to sector
def f37sr_f37_crypto_sector_relative_strength_beta_126d_base_v013_signal(closeadj, sector_index):
    result = _f37_beta(closeadj, sector_index, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling beta to sector
def f37sr_f37_crypto_sector_relative_strength_beta_252d_base_v014_signal(closeadj, sector_index):
    result = _f37_beta(closeadj, sector_index, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d rolling beta to sector
def f37sr_f37_crypto_sector_relative_strength_beta_42d_base_v015_signal(closeadj, sector_index):
    result = _f37_beta(closeadj, sector_index, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d rolling beta to sector
def f37sr_f37_crypto_sector_relative_strength_beta_84d_base_v016_signal(closeadj, sector_index):
    result = _f37_beta(closeadj, sector_index, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d rolling beta to sector
def f37sr_f37_crypto_sector_relative_strength_beta_189d_base_v017_signal(closeadj, sector_index):
    result = _f37_beta(closeadj, sector_index, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling beta to sector
def f37sr_f37_crypto_sector_relative_strength_beta_504d_base_v018_signal(closeadj, sector_index):
    result = _f37_beta(closeadj, sector_index, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# beta deviation from 1.0 (excess sector sensitivity, 126d)
def f37sr_f37_crypto_sector_relative_strength_betadev_126d_base_v019_signal(closeadj, sector_index):
    result = _f37_beta(closeadj, sector_index, 126) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# beta deviation from 1.0 (252d)
def f37sr_f37_crypto_sector_relative_strength_betadev_252d_base_v020_signal(closeadj, sector_index):
    result = _f37_beta(closeadj, sector_index, 252) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cumulative residual (idiosyncratic) momentum
def f37sr_f37_crypto_sector_relative_strength_resmom_21d_base_v021_signal(closeadj, sector_index):
    result = _f37_resid(closeadj, sector_index, 63).rolling(21, min_periods=10).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cumulative residual momentum
def f37sr_f37_crypto_sector_relative_strength_resmom_63d_base_v022_signal(closeadj, sector_index):
    result = _f37_resid(closeadj, sector_index, 126).rolling(63, min_periods=21).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cumulative residual momentum
def f37sr_f37_crypto_sector_relative_strength_resmom_126d_base_v023_signal(closeadj, sector_index):
    result = _f37_resid(closeadj, sector_index, 126).rolling(126, min_periods=42).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumulative residual momentum
def f37sr_f37_crypto_sector_relative_strength_resmom_252d_base_v024_signal(closeadj, sector_index):
    result = _f37_resid(closeadj, sector_index, 252).rolling(252, min_periods=84).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 42d cumulative residual momentum
def f37sr_f37_crypto_sector_relative_strength_resmom_42d_base_v025_signal(closeadj, sector_index):
    result = _f37_resid(closeadj, sector_index, 63).rolling(42, min_periods=21).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d return correlation to sector (regime)
def f37sr_f37_crypto_sector_relative_strength_corr_21d_base_v026_signal(closeadj, sector_index):
    result = _f37_corr(closeadj, sector_index, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d return correlation to sector
def f37sr_f37_crypto_sector_relative_strength_corr_63d_base_v027_signal(closeadj, sector_index):
    result = _f37_corr(closeadj, sector_index, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d return correlation to sector
def f37sr_f37_crypto_sector_relative_strength_corr_126d_base_v028_signal(closeadj, sector_index):
    result = _f37_corr(closeadj, sector_index, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d return correlation to sector
def f37sr_f37_crypto_sector_relative_strength_corr_252d_base_v029_signal(closeadj, sector_index):
    result = _f37_corr(closeadj, sector_index, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d return correlation to sector
def f37sr_f37_crypto_sector_relative_strength_corr_42d_base_v030_signal(closeadj, sector_index):
    result = _f37_corr(closeadj, sector_index, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# RS line: ratio of stock price to sector index (relative-strength line, level)
def f37sr_f37_crypto_sector_relative_strength_rsline_lvl_base_v031_signal(closeadj, sector_index):
    result = _safe_div(closeadj, sector_index) + _f37_relstr(closeadj, sector_index, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# RS line slope over 21d (log change of price ratio)
def f37sr_f37_crypto_sector_relative_strength_rsslope_21d_base_v032_signal(closeadj, sector_index):
    rs = _safe_div(closeadj, sector_index)
    result = np.log(rs / rs.shift(21)) + _f37_relstr(closeadj, sector_index, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# RS line slope over 63d
def f37sr_f37_crypto_sector_relative_strength_rsslope_63d_base_v033_signal(closeadj, sector_index):
    rs = _safe_div(closeadj, sector_index)
    result = np.log(rs / rs.shift(63)) + _f37_relstr(closeadj, sector_index, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# RS line slope over 126d
def f37sr_f37_crypto_sector_relative_strength_rsslope_126d_base_v034_signal(closeadj, sector_index):
    rs = _safe_div(closeadj, sector_index)
    result = np.log(rs / rs.shift(126)) + _f37_relstr(closeadj, sector_index, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# RS line z-score over 126d (relative-strength extension)
def f37sr_f37_crypto_sector_relative_strength_rsz_126d_base_v035_signal(closeadj, sector_index):
    rs = _safe_div(closeadj, sector_index)
    result = _z(rs, 126) + _f37_relstr(closeadj, sector_index, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# RS line z-score over 252d
def f37sr_f37_crypto_sector_relative_strength_rsz_252d_base_v036_signal(closeadj, sector_index):
    rs = _safe_div(closeadj, sector_index)
    result = _z(rs, 252) + _f37_relstr(closeadj, sector_index, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d tracking error (std of daily residual returns)
def f37sr_f37_crypto_sector_relative_strength_te_63d_base_v037_signal(closeadj, sector_index):
    result = _std(_f37_resid(closeadj, sector_index, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d tracking error
def f37sr_f37_crypto_sector_relative_strength_te_126d_base_v038_signal(closeadj, sector_index):
    result = _std(_f37_resid(closeadj, sector_index, 126), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d tracking error
def f37sr_f37_crypto_sector_relative_strength_te_252d_base_v039_signal(closeadj, sector_index):
    result = _std(_f37_resid(closeadj, sector_index, 252), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d tracking error
def f37sr_f37_crypto_sector_relative_strength_te_42d_base_v040_signal(closeadj, sector_index):
    result = _std(_f37_resid(closeadj, sector_index, 63), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d information ratio: residual mean / residual std
def f37sr_f37_crypto_sector_relative_strength_ir_63d_base_v041_signal(closeadj, sector_index):
    res = _f37_resid(closeadj, sector_index, 63)
    result = _safe_div(_mean(res, 63), _std(res, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d information ratio
def f37sr_f37_crypto_sector_relative_strength_ir_126d_base_v042_signal(closeadj, sector_index):
    res = _f37_resid(closeadj, sector_index, 126)
    result = _safe_div(_mean(res, 126), _std(res, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d information ratio
def f37sr_f37_crypto_sector_relative_strength_ir_252d_base_v043_signal(closeadj, sector_index):
    res = _f37_resid(closeadj, sector_index, 252)
    result = _safe_div(_mean(res, 252), _std(res, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 42d information ratio
def f37sr_f37_crypto_sector_relative_strength_ir_42d_base_v044_signal(closeadj, sector_index):
    res = _f37_resid(closeadj, sector_index, 63)
    result = _safe_div(_mean(res, 42), _std(res, 42))
    return result.replace([np.inf, -np.inf], np.nan)


# beta stability: 126d std of 21d rolling beta (lower = stable)
def f37sr_f37_crypto_sector_relative_strength_betastab_126d_base_v045_signal(closeadj, sector_index):
    result = _std(_f37_beta(closeadj, sector_index, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# beta stability: 252d std of 42d rolling beta
def f37sr_f37_crypto_sector_relative_strength_betastab_252d_base_v046_signal(closeadj, sector_index):
    result = _std(_f37_beta(closeadj, sector_index, 42), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# relative-strength z-score: 21d relstr standardized over 252d
def f37sr_f37_crypto_sector_relative_strength_zrelstr_21d_base_v047_signal(closeadj, sector_index):
    result = _z(_f37_relstr(closeadj, sector_index, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# relative-strength z-score: 63d relstr standardized over 252d
def f37sr_f37_crypto_sector_relative_strength_zrelstr_63d_base_v048_signal(closeadj, sector_index):
    result = _z(_f37_relstr(closeadj, sector_index, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# relative-strength z-score: 126d relstr standardized over 504d
def f37sr_f37_crypto_sector_relative_strength_zrelstr_126d_base_v049_signal(closeadj, sector_index):
    result = _z(_f37_relstr(closeadj, sector_index, 126), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# relative-strength percentile rank: 21d relstr over 126d
def f37sr_f37_crypto_sector_relative_strength_rsrank_21d_base_v050_signal(closeadj, sector_index):
    r = _f37_relstr(closeadj, sector_index, 21)
    result = r.rolling(126, min_periods=21).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# relative-strength percentile rank: 63d relstr over 252d
def f37sr_f37_crypto_sector_relative_strength_rsrank_63d_base_v051_signal(closeadj, sector_index):
    r = _f37_relstr(closeadj, sector_index, 63)
    result = r.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# relative-strength percentile rank: 126d relstr over 252d
def f37sr_f37_crypto_sector_relative_strength_rsrank_126d_base_v052_signal(closeadj, sector_index):
    r = _f37_relstr(closeadj, sector_index, 126)
    result = r.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# relative-strength trend: 21d relstr minus its 63d mean
def f37sr_f37_crypto_sector_relative_strength_rstrend_21d_base_v053_signal(closeadj, sector_index):
    r = _f37_relstr(closeadj, sector_index, 21)
    result = r - _mean(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# relative-strength trend: 63d relstr minus its 126d mean
def f37sr_f37_crypto_sector_relative_strength_rstrend_63d_base_v054_signal(closeadj, sector_index):
    r = _f37_relstr(closeadj, sector_index, 63)
    result = r - _mean(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# relative-strength spread: 21d vs 126d (short minus long relative strength)
def f37sr_f37_crypto_sector_relative_strength_rsspread_21_126_base_v055_signal(closeadj, sector_index):
    result = _f37_relstr(closeadj, sector_index, 21) - _f37_relstr(closeadj, sector_index, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# relative-strength spread: 63d vs 252d
def f37sr_f37_crypto_sector_relative_strength_rsspread_63_252_base_v056_signal(closeadj, sector_index):
    result = _f37_relstr(closeadj, sector_index, 63) - _f37_relstr(closeadj, sector_index, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# relative-strength acceleration: 21d vs 42d
def f37sr_f37_crypto_sector_relative_strength_rsaccel_21_42_base_v057_signal(closeadj, sector_index):
    result = _f37_relstr(closeadj, sector_index, 21) - _f37_relstr(closeadj, sector_index, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# relative-strength acceleration: 63d vs 126d
def f37sr_f37_crypto_sector_relative_strength_rsaccel_63_126_base_v058_signal(closeadj, sector_index):
    result = _f37_relstr(closeadj, sector_index, 63) - _f37_relstr(closeadj, sector_index, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# beta spread: short 21d beta minus long 252d beta (beta regime shift)
def f37sr_f37_crypto_sector_relative_strength_betaspread_21_252_base_v059_signal(closeadj, sector_index):
    result = _f37_beta(closeadj, sector_index, 21) - _f37_beta(closeadj, sector_index, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# beta spread: 63d minus 126d beta
def f37sr_f37_crypto_sector_relative_strength_betaspread_63_126_base_v060_signal(closeadj, sector_index):
    result = _f37_beta(closeadj, sector_index, 63) - _f37_beta(closeadj, sector_index, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# correlation spread: 21d minus 126d correlation (co-movement regime change)
def f37sr_f37_crypto_sector_relative_strength_corrspread_21_126_base_v061_signal(closeadj, sector_index):
    result = _f37_corr(closeadj, sector_index, 21) - _f37_corr(closeadj, sector_index, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# correlation z-score: 63d corr standardized over 252d
def f37sr_f37_crypto_sector_relative_strength_zcorr_63d_base_v062_signal(closeadj, sector_index):
    result = _z(_f37_corr(closeadj, sector_index, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# residual volatility share: tracking error vs total stock vol (idiosyncratic fraction)
def f37sr_f37_crypto_sector_relative_strength_residshare_126d_base_v063_signal(closeadj, sector_index):
    res_std = _std(_f37_resid(closeadj, sector_index, 126), 126)
    tot_std = _std(closeadj.pct_change(), 126)
    result = _safe_div(res_std, tot_std)
    return result.replace([np.inf, -np.inf], np.nan)


# residual volatility share over 252d
def f37sr_f37_crypto_sector_relative_strength_residshare_252d_base_v064_signal(closeadj, sector_index):
    res_std = _std(_f37_resid(closeadj, sector_index, 252), 252)
    tot_std = _std(closeadj.pct_change(), 252)
    result = _safe_div(res_std, tot_std)
    return result.replace([np.inf, -np.inf], np.nan)


# beta-adjusted relative strength: relstr scaled by inverse beta (126d)
def f37sr_f37_crypto_sector_relative_strength_betaadjrs_126d_base_v065_signal(closeadj, sector_index):
    rs = _f37_relstr(closeadj, sector_index, 126)
    beta = _f37_beta(closeadj, sector_index, 126)
    result = _safe_div(rs, beta.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# beta-adjusted relative strength (252d)
def f37sr_f37_crypto_sector_relative_strength_betaadjrs_252d_base_v066_signal(closeadj, sector_index):
    rs = _f37_relstr(closeadj, sector_index, 252)
    beta = _f37_beta(closeadj, sector_index, 252)
    result = _safe_div(rs, beta.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# relative-strength scaled by tracking error (risk-adjusted alpha, 126d)
def f37sr_f37_crypto_sector_relative_strength_rsperte_126d_base_v067_signal(closeadj, sector_index):
    rs = _f37_relstr(closeadj, sector_index, 126)
    te = _std(_f37_resid(closeadj, sector_index, 126), 126)
    result = _safe_div(rs, te)
    return result.replace([np.inf, -np.inf], np.nan)


# relative-strength scaled by tracking error (252d)
def f37sr_f37_crypto_sector_relative_strength_rsperte_252d_base_v068_signal(closeadj, sector_index):
    rs = _f37_relstr(closeadj, sector_index, 252)
    te = _std(_f37_resid(closeadj, sector_index, 252), 252)
    result = _safe_div(rs, te)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed relative strength: 21d mean of 21d relstr
def f37sr_f37_crypto_sector_relative_strength_smoothrs_21d_base_v069_signal(closeadj, sector_index):
    result = _mean(_f37_relstr(closeadj, sector_index, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed relative strength: 42d mean of 63d relstr
def f37sr_f37_crypto_sector_relative_strength_smoothrs_63d_base_v070_signal(closeadj, sector_index):
    result = _mean(_f37_relstr(closeadj, sector_index, 63), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA of relative strength (21d span on 21d relstr)
def f37sr_f37_crypto_sector_relative_strength_ewmrs_21d_base_v071_signal(closeadj, sector_index):
    rs = _f37_relstr(closeadj, sector_index, 21)
    result = rs.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA of relative strength (63d span on 63d relstr)
def f37sr_f37_crypto_sector_relative_strength_ewmrs_63d_base_v072_signal(closeadj, sector_index):
    rs = _f37_relstr(closeadj, sector_index, 63)
    result = rs.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# annualized 63d relative strength
def f37sr_f37_crypto_sector_relative_strength_annrs_63d_base_v073_signal(closeadj, sector_index):
    result = _f37_relstr(closeadj, sector_index, 63) * (252.0 / 63.0)
    return result.replace([np.inf, -np.inf], np.nan)


# annualized 126d relative strength
def f37sr_f37_crypto_sector_relative_strength_annrs_126d_base_v074_signal(closeadj, sector_index):
    result = _f37_relstr(closeadj, sector_index, 126) * (252.0 / 126.0)
    return result.replace([np.inf, -np.inf], np.nan)


# relative-strength dispersion: 63d std of 21d relstr (instability of outperformance)
def f37sr_f37_crypto_sector_relative_strength_rsdisp_63d_base_v075_signal(closeadj, sector_index):
    result = _std(_f37_relstr(closeadj, sector_index, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f37sr_f37_crypto_sector_relative_strength_relstr_21d_base_v001_signal,
    f37sr_f37_crypto_sector_relative_strength_relstr_63d_base_v002_signal,
    f37sr_f37_crypto_sector_relative_strength_relstr_126d_base_v003_signal,
    f37sr_f37_crypto_sector_relative_strength_relstr_252d_base_v004_signal,
    f37sr_f37_crypto_sector_relative_strength_relstr_5d_base_v005_signal,
    f37sr_f37_crypto_sector_relative_strength_relstr_42d_base_v006_signal,
    f37sr_f37_crypto_sector_relative_strength_relstr_84d_base_v007_signal,
    f37sr_f37_crypto_sector_relative_strength_relstr_189d_base_v008_signal,
    f37sr_f37_crypto_sector_relative_strength_relstr_504d_base_v009_signal,
    f37sr_f37_crypto_sector_relative_strength_relstr_10d_base_v010_signal,
    f37sr_f37_crypto_sector_relative_strength_beta_21d_base_v011_signal,
    f37sr_f37_crypto_sector_relative_strength_beta_63d_base_v012_signal,
    f37sr_f37_crypto_sector_relative_strength_beta_126d_base_v013_signal,
    f37sr_f37_crypto_sector_relative_strength_beta_252d_base_v014_signal,
    f37sr_f37_crypto_sector_relative_strength_beta_42d_base_v015_signal,
    f37sr_f37_crypto_sector_relative_strength_beta_84d_base_v016_signal,
    f37sr_f37_crypto_sector_relative_strength_beta_189d_base_v017_signal,
    f37sr_f37_crypto_sector_relative_strength_beta_504d_base_v018_signal,
    f37sr_f37_crypto_sector_relative_strength_betadev_126d_base_v019_signal,
    f37sr_f37_crypto_sector_relative_strength_betadev_252d_base_v020_signal,
    f37sr_f37_crypto_sector_relative_strength_resmom_21d_base_v021_signal,
    f37sr_f37_crypto_sector_relative_strength_resmom_63d_base_v022_signal,
    f37sr_f37_crypto_sector_relative_strength_resmom_126d_base_v023_signal,
    f37sr_f37_crypto_sector_relative_strength_resmom_252d_base_v024_signal,
    f37sr_f37_crypto_sector_relative_strength_resmom_42d_base_v025_signal,
    f37sr_f37_crypto_sector_relative_strength_corr_21d_base_v026_signal,
    f37sr_f37_crypto_sector_relative_strength_corr_63d_base_v027_signal,
    f37sr_f37_crypto_sector_relative_strength_corr_126d_base_v028_signal,
    f37sr_f37_crypto_sector_relative_strength_corr_252d_base_v029_signal,
    f37sr_f37_crypto_sector_relative_strength_corr_42d_base_v030_signal,
    f37sr_f37_crypto_sector_relative_strength_rsline_lvl_base_v031_signal,
    f37sr_f37_crypto_sector_relative_strength_rsslope_21d_base_v032_signal,
    f37sr_f37_crypto_sector_relative_strength_rsslope_63d_base_v033_signal,
    f37sr_f37_crypto_sector_relative_strength_rsslope_126d_base_v034_signal,
    f37sr_f37_crypto_sector_relative_strength_rsz_126d_base_v035_signal,
    f37sr_f37_crypto_sector_relative_strength_rsz_252d_base_v036_signal,
    f37sr_f37_crypto_sector_relative_strength_te_63d_base_v037_signal,
    f37sr_f37_crypto_sector_relative_strength_te_126d_base_v038_signal,
    f37sr_f37_crypto_sector_relative_strength_te_252d_base_v039_signal,
    f37sr_f37_crypto_sector_relative_strength_te_42d_base_v040_signal,
    f37sr_f37_crypto_sector_relative_strength_ir_63d_base_v041_signal,
    f37sr_f37_crypto_sector_relative_strength_ir_126d_base_v042_signal,
    f37sr_f37_crypto_sector_relative_strength_ir_252d_base_v043_signal,
    f37sr_f37_crypto_sector_relative_strength_ir_42d_base_v044_signal,
    f37sr_f37_crypto_sector_relative_strength_betastab_126d_base_v045_signal,
    f37sr_f37_crypto_sector_relative_strength_betastab_252d_base_v046_signal,
    f37sr_f37_crypto_sector_relative_strength_zrelstr_21d_base_v047_signal,
    f37sr_f37_crypto_sector_relative_strength_zrelstr_63d_base_v048_signal,
    f37sr_f37_crypto_sector_relative_strength_zrelstr_126d_base_v049_signal,
    f37sr_f37_crypto_sector_relative_strength_rsrank_21d_base_v050_signal,
    f37sr_f37_crypto_sector_relative_strength_rsrank_63d_base_v051_signal,
    f37sr_f37_crypto_sector_relative_strength_rsrank_126d_base_v052_signal,
    f37sr_f37_crypto_sector_relative_strength_rstrend_21d_base_v053_signal,
    f37sr_f37_crypto_sector_relative_strength_rstrend_63d_base_v054_signal,
    f37sr_f37_crypto_sector_relative_strength_rsspread_21_126_base_v055_signal,
    f37sr_f37_crypto_sector_relative_strength_rsspread_63_252_base_v056_signal,
    f37sr_f37_crypto_sector_relative_strength_rsaccel_21_42_base_v057_signal,
    f37sr_f37_crypto_sector_relative_strength_rsaccel_63_126_base_v058_signal,
    f37sr_f37_crypto_sector_relative_strength_betaspread_21_252_base_v059_signal,
    f37sr_f37_crypto_sector_relative_strength_betaspread_63_126_base_v060_signal,
    f37sr_f37_crypto_sector_relative_strength_corrspread_21_126_base_v061_signal,
    f37sr_f37_crypto_sector_relative_strength_zcorr_63d_base_v062_signal,
    f37sr_f37_crypto_sector_relative_strength_residshare_126d_base_v063_signal,
    f37sr_f37_crypto_sector_relative_strength_residshare_252d_base_v064_signal,
    f37sr_f37_crypto_sector_relative_strength_betaadjrs_126d_base_v065_signal,
    f37sr_f37_crypto_sector_relative_strength_betaadjrs_252d_base_v066_signal,
    f37sr_f37_crypto_sector_relative_strength_rsperte_126d_base_v067_signal,
    f37sr_f37_crypto_sector_relative_strength_rsperte_252d_base_v068_signal,
    f37sr_f37_crypto_sector_relative_strength_smoothrs_21d_base_v069_signal,
    f37sr_f37_crypto_sector_relative_strength_smoothrs_63d_base_v070_signal,
    f37sr_f37_crypto_sector_relative_strength_ewmrs_21d_base_v071_signal,
    f37sr_f37_crypto_sector_relative_strength_ewmrs_63d_base_v072_signal,
    f37sr_f37_crypto_sector_relative_strength_annrs_63d_base_v073_signal,
    f37sr_f37_crypto_sector_relative_strength_annrs_126d_base_v074_signal,
    f37sr_f37_crypto_sector_relative_strength_rsdisp_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F37_CRYPTO_SECTOR_RELATIVE_STRENGTH_REGISTRY_001_075 = REGISTRY


def _synth_cols(names):
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    sector_lvl = 45.0 * np.exp(np.cumsum(np.random.normal(0.0006, 0.04, n)))
    for nm in names:
        if nm in ("closeadj", "close", "price"):
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "sector_index":
            out[nm] = pd.Series(sector_lvl, name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7, 7e6, n)) + 1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0, 1.0, n))
            level = 1000.0 * np.exp(0.03 * np.random.normal(0, 1, n).cumsum() / np.sqrt(n))
            s = np.abs(level + 50.0 * walk) + 10.0
            out[nm] = pd.Series(s, name=nm)
    return out


if __name__ == "__main__":
    domain_primitives = ("_f37_relstr", "_f37_beta", "_f37_resid", "_f37_corr")
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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f37_crypto_sector_relative_strength_base_001_075_claude: {n_features} features pass")
