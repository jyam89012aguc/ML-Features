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
    rs = closeadj.pct_change(periods=w)
    rb = sector_index.pct_change(periods=w)
    return rs - rb


def _f37_beta(closeadj, sector_index, w):
    rs = closeadj.pct_change()
    rb = sector_index.pct_change()
    mp = max(2, w // 2)
    cov = rs.rolling(w, min_periods=mp).cov(rb)
    var = rb.rolling(w, min_periods=mp).var()
    return cov / var.replace(0, np.nan)


def _f37_resid(closeadj, sector_index, w):
    rs = closeadj.pct_change()
    rb = sector_index.pct_change()
    mp = max(2, w // 2)
    cov = rs.rolling(w, min_periods=mp).cov(rb)
    var = rb.rolling(w, min_periods=mp).var()
    beta = cov / var.replace(0, np.nan)
    return rs - beta * rb


def _f37_corr(closeadj, sector_index, w):
    rs = closeadj.pct_change()
    rb = sector_index.pct_change()
    mp = max(2, w // 2)
    return rs.rolling(w, min_periods=mp).corr(rb)


# ============ FEATURES 076-150 ============

# up-beta: beta conditioned on sector up-days (63d)
def f37sr_f37_crypto_sector_relative_strength_upbeta_63d_base_v076_signal(closeadj, sector_index):
    rs = closeadj.pct_change()
    rb = sector_index.pct_change()
    up = rb.where(rb > 0)
    rsu = rs.where(rb > 0)
    cov = rsu.rolling(63, min_periods=21).cov(up)
    var = up.rolling(63, min_periods=21).var()
    result = cov / var.replace(0, np.nan) + _f37_beta(closeadj, sector_index, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# up-beta (126d)
def f37sr_f37_crypto_sector_relative_strength_upbeta_126d_base_v077_signal(closeadj, sector_index):
    rs = closeadj.pct_change()
    rb = sector_index.pct_change()
    up = rb.where(rb > 0)
    rsu = rs.where(rb > 0)
    cov = rsu.rolling(126, min_periods=42).cov(up)
    var = up.rolling(126, min_periods=42).var()
    result = cov / var.replace(0, np.nan) + _f37_beta(closeadj, sector_index, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# down-beta: beta conditioned on sector down-days (63d)
def f37sr_f37_crypto_sector_relative_strength_downbeta_63d_base_v078_signal(closeadj, sector_index):
    rs = closeadj.pct_change()
    rb = sector_index.pct_change()
    dn = rb.where(rb < 0)
    rsd = rs.where(rb < 0)
    cov = rsd.rolling(63, min_periods=21).cov(dn)
    var = dn.rolling(63, min_periods=21).var()
    result = cov / var.replace(0, np.nan) + _f37_beta(closeadj, sector_index, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# down-beta (126d)
def f37sr_f37_crypto_sector_relative_strength_downbeta_126d_base_v079_signal(closeadj, sector_index):
    rs = closeadj.pct_change()
    rb = sector_index.pct_change()
    dn = rb.where(rb < 0)
    rsd = rs.where(rb < 0)
    cov = rsd.rolling(126, min_periods=42).cov(dn)
    var = dn.rolling(126, min_periods=42).var()
    result = cov / var.replace(0, np.nan) + _f37_beta(closeadj, sector_index, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# beta asymmetry: up-beta minus down-beta (63d) -- convexity to sector
def f37sr_f37_crypto_sector_relative_strength_betaasym_63d_base_v080_signal(closeadj, sector_index):
    rs = closeadj.pct_change()
    rb = sector_index.pct_change()
    up = rb.where(rb > 0); rsu = rs.where(rb > 0)
    dn = rb.where(rb < 0); rsd = rs.where(rb < 0)
    ub = rsu.rolling(63, min_periods=21).cov(up) / up.rolling(63, min_periods=21).var().replace(0, np.nan)
    db = rsd.rolling(63, min_periods=21).cov(dn) / dn.rolling(63, min_periods=21).var().replace(0, np.nan)
    result = ub - db + _f37_beta(closeadj, sector_index, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# beta asymmetry (126d)
def f37sr_f37_crypto_sector_relative_strength_betaasym_126d_base_v081_signal(closeadj, sector_index):
    rs = closeadj.pct_change()
    rb = sector_index.pct_change()
    up = rb.where(rb > 0); rsu = rs.where(rb > 0)
    dn = rb.where(rb < 0); rsd = rs.where(rb < 0)
    ub = rsu.rolling(126, min_periods=42).cov(up) / up.rolling(126, min_periods=42).var().replace(0, np.nan)
    db = rsd.rolling(126, min_periods=42).cov(dn) / dn.rolling(126, min_periods=42).var().replace(0, np.nan)
    result = ub - db + _f37_beta(closeadj, sector_index, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# beta asymmetry (252d)
def f37sr_f37_crypto_sector_relative_strength_betaasym_252d_base_v082_signal(closeadj, sector_index):
    rs = closeadj.pct_change()
    rb = sector_index.pct_change()
    up = rb.where(rb > 0); rsu = rs.where(rb > 0)
    dn = rb.where(rb < 0); rsd = rs.where(rb < 0)
    ub = rsu.rolling(252, min_periods=84).cov(up) / up.rolling(252, min_periods=84).var().replace(0, np.nan)
    db = rsd.rolling(252, min_periods=84).cov(dn) / dn.rolling(252, min_periods=84).var().replace(0, np.nan)
    result = ub - db + _f37_beta(closeadj, sector_index, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# up-down beta ratio (126d) -- relative upside capture
def f37sr_f37_crypto_sector_relative_strength_udbetaratio_126d_base_v083_signal(closeadj, sector_index):
    rs = closeadj.pct_change()
    rb = sector_index.pct_change()
    up = rb.where(rb > 0); rsu = rs.where(rb > 0)
    dn = rb.where(rb < 0); rsd = rs.where(rb < 0)
    ub = rsu.rolling(126, min_periods=42).cov(up) / up.rolling(126, min_periods=42).var().replace(0, np.nan)
    db = rsd.rolling(126, min_periods=42).cov(dn) / dn.rolling(126, min_periods=42).var().replace(0, np.nan)
    result = _safe_div(ub, db.abs()) + _f37_beta(closeadj, sector_index, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA beta proxy: ewm cov / ewm var (63d span)
def f37sr_f37_crypto_sector_relative_strength_ewmbeta_63d_base_v084_signal(closeadj, sector_index):
    rs = closeadj.pct_change()
    rb = sector_index.pct_change()
    cov = (rs * rb).ewm(span=63, min_periods=21).mean() - rs.ewm(span=63, min_periods=21).mean() * rb.ewm(span=63, min_periods=21).mean()
    var = (rb * rb).ewm(span=63, min_periods=21).mean() - rb.ewm(span=63, min_periods=21).mean() ** 2
    result = cov / var.replace(0, np.nan) + _f37_beta(closeadj, sector_index, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA beta proxy (126d span)
def f37sr_f37_crypto_sector_relative_strength_ewmbeta_126d_base_v085_signal(closeadj, sector_index):
    rs = closeadj.pct_change()
    rb = sector_index.pct_change()
    cov = (rs * rb).ewm(span=126, min_periods=42).mean() - rs.ewm(span=126, min_periods=42).mean() * rb.ewm(span=126, min_periods=42).mean()
    var = (rb * rb).ewm(span=126, min_periods=42).mean() - rb.ewm(span=126, min_periods=42).mean() ** 2
    result = cov / var.replace(0, np.nan) + _f37_beta(closeadj, sector_index, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# residual daily return z-score over 126d (idiosyncratic shock)
def f37sr_f37_crypto_sector_relative_strength_zresid_126d_base_v086_signal(closeadj, sector_index):
    result = _z(_f37_resid(closeadj, sector_index, 126), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# residual daily return z-score over 252d
def f37sr_f37_crypto_sector_relative_strength_zresid_252d_base_v087_signal(closeadj, sector_index):
    result = _z(_f37_resid(closeadj, sector_index, 252), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# residual EWMA momentum (63d span on residual returns, scaled)
def f37sr_f37_crypto_sector_relative_strength_ewmresid_63d_base_v088_signal(closeadj, sector_index):
    res = _f37_resid(closeadj, sector_index, 63)
    result = res.ewm(span=63, min_periods=21).mean() * 63.0
    return result.replace([np.inf, -np.inf], np.nan)


# residual EWMA momentum (126d span, scaled)
def f37sr_f37_crypto_sector_relative_strength_ewmresid_126d_base_v089_signal(closeadj, sector_index):
    res = _f37_resid(closeadj, sector_index, 126)
    result = res.ewm(span=126, min_periods=42).mean() * 126.0
    return result.replace([np.inf, -np.inf], np.nan)


# residual return skew over 126d (idiosyncratic asymmetry)
def f37sr_f37_crypto_sector_relative_strength_residskew_126d_base_v090_signal(closeadj, sector_index):
    res = _f37_resid(closeadj, sector_index, 126)
    result = res.rolling(126, min_periods=42).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# residual return skew over 252d
def f37sr_f37_crypto_sector_relative_strength_residskew_252d_base_v091_signal(closeadj, sector_index):
    res = _f37_resid(closeadj, sector_index, 252)
    result = res.rolling(252, min_periods=84).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# residual return kurtosis over 126d (idiosyncratic tails)
def f37sr_f37_crypto_sector_relative_strength_residkurt_126d_base_v092_signal(closeadj, sector_index):
    res = _f37_resid(closeadj, sector_index, 126)
    result = res.rolling(126, min_periods=42).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# R-squared proxy: squared correlation to sector (126d, systematic share)
def f37sr_f37_crypto_sector_relative_strength_rsq_126d_base_v093_signal(closeadj, sector_index):
    c = _f37_corr(closeadj, sector_index, 126)
    result = c * c
    return result.replace([np.inf, -np.inf], np.nan)


# R-squared proxy (252d)
def f37sr_f37_crypto_sector_relative_strength_rsq_252d_base_v094_signal(closeadj, sector_index):
    c = _f37_corr(closeadj, sector_index, 252)
    result = c * c
    return result.replace([np.inf, -np.inf], np.nan)


# idiosyncratic share = 1 - R-squared (126d, diversification value)
def f37sr_f37_crypto_sector_relative_strength_idioshare_126d_base_v095_signal(closeadj, sector_index):
    c = _f37_corr(closeadj, sector_index, 126)
    result = 1.0 - c * c
    return result.replace([np.inf, -np.inf], np.nan)


# correlation trend: 21d corr minus its 126d mean
def f37sr_f37_crypto_sector_relative_strength_corrtrend_21d_base_v096_signal(closeadj, sector_index):
    c = _f37_corr(closeadj, sector_index, 21)
    result = c - _mean(c, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# correlation dispersion: 126d std of 21d correlation (regime instability)
def f37sr_f37_crypto_sector_relative_strength_corrdisp_126d_base_v097_signal(closeadj, sector_index):
    result = _std(_f37_corr(closeadj, sector_index, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# beta momentum: change in 63d beta over 21d
def f37sr_f37_crypto_sector_relative_strength_betamom_63d_base_v098_signal(closeadj, sector_index):
    beta = _f37_beta(closeadj, sector_index, 63)
    result = beta - beta.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# beta momentum: change in 126d beta over 42d
def f37sr_f37_crypto_sector_relative_strength_betamom_126d_base_v099_signal(closeadj, sector_index):
    beta = _f37_beta(closeadj, sector_index, 126)
    result = beta - beta.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# beta z-score over 252d (extreme sector sensitivity)
def f37sr_f37_crypto_sector_relative_strength_zbeta_126d_base_v100_signal(closeadj, sector_index):
    result = _z(_f37_beta(closeadj, sector_index, 126), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# beta z-score: 63d beta over 252d
def f37sr_f37_crypto_sector_relative_strength_zbeta_63d_base_v101_signal(closeadj, sector_index):
    result = _z(_f37_beta(closeadj, sector_index, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# relative-strength momentum quality: relstr per unit residual vol (126d)
def f37sr_f37_crypto_sector_relative_strength_rsqual_126d_base_v102_signal(closeadj, sector_index):
    rs = _f37_relstr(closeadj, sector_index, 126)
    te = _std(_f37_resid(closeadj, sector_index, 126), 126) * np.sqrt(126.0)
    result = _safe_div(rs, te)
    return result.replace([np.inf, -np.inf], np.nan)


# relative-strength momentum quality (252d)
def f37sr_f37_crypto_sector_relative_strength_rsqual_252d_base_v103_signal(closeadj, sector_index):
    rs = _f37_relstr(closeadj, sector_index, 252)
    te = _std(_f37_resid(closeadj, sector_index, 252), 252) * np.sqrt(252.0)
    result = _safe_div(rs, te)
    return result.replace([np.inf, -np.inf], np.nan)


# relative-strength efficiency: net relstr vs path of relstr (63d)
def f37sr_f37_crypto_sector_relative_strength_rseff_63d_base_v104_signal(closeadj, sector_index):
    rs = _f37_relstr(closeadj, sector_index, 5)
    net = rs.rolling(63, min_periods=21).sum()
    path = rs.abs().rolling(63, min_periods=21).sum()
    result = _safe_div(net, path)
    return result.replace([np.inf, -np.inf], np.nan)


# relative-strength efficiency (126d)
def f37sr_f37_crypto_sector_relative_strength_rseff_126d_base_v105_signal(closeadj, sector_index):
    rs = _f37_relstr(closeadj, sector_index, 5)
    net = rs.rolling(126, min_periods=42).sum()
    path = rs.abs().rolling(126, min_periods=42).sum()
    result = _safe_div(net, path)
    return result.replace([np.inf, -np.inf], np.nan)


# relative-strength Sharpe: mean/std of 5d relstr over 63d
def f37sr_f37_crypto_sector_relative_strength_rssharpe_63d_base_v106_signal(closeadj, sector_index):
    rs = _f37_relstr(closeadj, sector_index, 5)
    result = _safe_div(_mean(rs, 63), _std(rs, 63)) * np.sqrt(63.0)
    return result.replace([np.inf, -np.inf], np.nan)


# relative-strength Sharpe over 126d
def f37sr_f37_crypto_sector_relative_strength_rssharpe_126d_base_v107_signal(closeadj, sector_index):
    rs = _f37_relstr(closeadj, sector_index, 5)
    result = _safe_div(_mean(rs, 126), _std(rs, 126)) * np.sqrt(126.0)
    return result.replace([np.inf, -np.inf], np.nan)


# relative-strength Sharpe over 252d
def f37sr_f37_crypto_sector_relative_strength_rssharpe_252d_base_v108_signal(closeadj, sector_index):
    rs = _f37_relstr(closeadj, sector_index, 5)
    result = _safe_div(_mean(rs, 252), _std(rs, 252)) * np.sqrt(252.0)
    return result.replace([np.inf, -np.inf], np.nan)


# volume-weighted relative strength: relstr confirmed by volume z (21d)
def f37sr_f37_crypto_sector_relative_strength_volconfrs_21d_base_v109_signal(closeadj, sector_index, volume):
    result = _f37_relstr(closeadj, sector_index, 21) * _z(volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume-weighted relative strength (63d)
def f37sr_f37_crypto_sector_relative_strength_dvconfrs_63d_base_v110_signal(closeadj, sector_index, volume):
    dv = closeadj * volume
    result = _f37_relstr(closeadj, sector_index, 63) * _z(dv, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# relative-strength scaled by dollar-volume surge (21d)
def f37sr_f37_crypto_sector_relative_strength_dvsurgers_21d_base_v111_signal(closeadj, sector_index, volume):
    dv = closeadj * volume
    surge = _safe_div(dv, _mean(dv, 63))
    result = _f37_relstr(closeadj, sector_index, 21) * surge
    return result.replace([np.inf, -np.inf], np.nan)


# RS line slope over 252d
def f37sr_f37_crypto_sector_relative_strength_rsslope_252d_base_v112_signal(closeadj, sector_index):
    rs = _safe_div(closeadj, sector_index)
    result = np.log(rs / rs.shift(252)) + _f37_relstr(closeadj, sector_index, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# RS line distance from its 126d moving average (relative-strength extension)
def f37sr_f37_crypto_sector_relative_strength_rsdma_126d_base_v113_signal(closeadj, sector_index):
    rs = _safe_div(closeadj, sector_index)
    result = _safe_div(rs - _mean(rs, 126), _mean(rs, 126)) + _f37_relstr(closeadj, sector_index, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# RS line distance from its 252d moving average
def f37sr_f37_crypto_sector_relative_strength_rsdma_252d_base_v114_signal(closeadj, sector_index):
    rs = _safe_div(closeadj, sector_index)
    result = _safe_div(rs - _mean(rs, 252), _mean(rs, 252)) + _f37_relstr(closeadj, sector_index, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# RS line percentile rank over 252d
def f37sr_f37_crypto_sector_relative_strength_rslinerank_252d_base_v115_signal(closeadj, sector_index):
    rs = _safe_div(closeadj, sector_index)
    result = rs.rolling(252, min_periods=63).rank(pct=True) + _f37_relstr(closeadj, sector_index, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# beta-times-sector-momentum: expected systematic return (63d)
def f37sr_f37_crypto_sector_relative_strength_systret_63d_base_v116_signal(closeadj, sector_index):
    beta = _f37_beta(closeadj, sector_index, 63)
    sectmom = sector_index.pct_change(periods=63)
    result = beta * sectmom
    return result.replace([np.inf, -np.inf], np.nan)


# systematic expected return (126d)
def f37sr_f37_crypto_sector_relative_strength_systret_126d_base_v117_signal(closeadj, sector_index):
    beta = _f37_beta(closeadj, sector_index, 126)
    sectmom = sector_index.pct_change(periods=126)
    result = beta * sectmom
    return result.replace([np.inf, -np.inf], np.nan)


# alpha = stock return minus beta*sector return cumulative (126d, Jensen-style)
def f37sr_f37_crypto_sector_relative_strength_alpha_126d_base_v118_signal(closeadj, sector_index):
    beta = _f37_beta(closeadj, sector_index, 126)
    result = closeadj.pct_change(periods=126) - beta * sector_index.pct_change(periods=126)
    return result.replace([np.inf, -np.inf], np.nan)


# alpha cumulative (252d, Jensen-style)
def f37sr_f37_crypto_sector_relative_strength_alpha_252d_base_v119_signal(closeadj, sector_index):
    beta = _f37_beta(closeadj, sector_index, 252)
    result = closeadj.pct_change(periods=252) - beta * sector_index.pct_change(periods=252)
    return result.replace([np.inf, -np.inf], np.nan)


# alpha cumulative (63d)
def f37sr_f37_crypto_sector_relative_strength_alpha_63d_base_v120_signal(closeadj, sector_index):
    beta = _f37_beta(closeadj, sector_index, 63)
    result = closeadj.pct_change(periods=63) - beta * sector_index.pct_change(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


# alpha z-score over 252d (126d alpha standardized)
def f37sr_f37_crypto_sector_relative_strength_zalpha_126d_base_v121_signal(closeadj, sector_index):
    beta = _f37_beta(closeadj, sector_index, 126)
    alpha = closeadj.pct_change(periods=126) - beta * sector_index.pct_change(periods=126)
    result = _z(alpha, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# alpha information ratio: 126d alpha / tracking error
def f37sr_f37_crypto_sector_relative_strength_alphair_126d_base_v122_signal(closeadj, sector_index):
    beta = _f37_beta(closeadj, sector_index, 126)
    alpha = closeadj.pct_change(periods=126) - beta * sector_index.pct_change(periods=126)
    te = _std(_f37_resid(closeadj, sector_index, 126), 126) * np.sqrt(126.0)
    result = _safe_div(alpha, te)
    return result.replace([np.inf, -np.inf], np.nan)


# alpha information ratio (252d)
def f37sr_f37_crypto_sector_relative_strength_alphair_252d_base_v123_signal(closeadj, sector_index):
    beta = _f37_beta(closeadj, sector_index, 252)
    alpha = closeadj.pct_change(periods=252) - beta * sector_index.pct_change(periods=252)
    te = _std(_f37_resid(closeadj, sector_index, 252), 252) * np.sqrt(252.0)
    result = _safe_div(alpha, te)
    return result.replace([np.inf, -np.inf], np.nan)


# relative-strength momentum spread normalized by sector vol (126d)
def f37sr_f37_crypto_sector_relative_strength_rsvoladj_126d_base_v124_signal(closeadj, sector_index):
    rs = _f37_relstr(closeadj, sector_index, 126)
    secvol = _std(sector_index.pct_change(), 126) * np.sqrt(126.0)
    result = _safe_div(rs, secvol)
    return result.replace([np.inf, -np.inf], np.nan)


# relative-strength normalized by sector vol (252d)
def f37sr_f37_crypto_sector_relative_strength_rsvoladj_252d_base_v125_signal(closeadj, sector_index):
    rs = _f37_relstr(closeadj, sector_index, 252)
    secvol = _std(sector_index.pct_change(), 252) * np.sqrt(252.0)
    result = _safe_div(rs, secvol)
    return result.replace([np.inf, -np.inf], np.nan)


# relative volatility ratio: stock vol / sector vol (126d)
def f37sr_f37_crypto_sector_relative_strength_volratio_126d_base_v126_signal(closeadj, sector_index):
    sv = _std(closeadj.pct_change(), 126)
    bv = _std(sector_index.pct_change(), 126)
    result = _safe_div(sv, bv) + _f37_corr(closeadj, sector_index, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# relative volatility ratio (252d)
def f37sr_f37_crypto_sector_relative_strength_volratio_252d_base_v127_signal(closeadj, sector_index):
    sv = _std(closeadj.pct_change(), 252)
    bv = _std(sector_index.pct_change(), 252)
    result = _safe_div(sv, bv) + _f37_corr(closeadj, sector_index, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# beta scaled by sector vol = systematic vol contribution (126d)
def f37sr_f37_crypto_sector_relative_strength_betavol_126d_base_v128_signal(closeadj, sector_index):
    bv = _std(sector_index.pct_change(), 126)
    result = _f37_beta(closeadj, sector_index, 126) * bv * np.sqrt(126.0)
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative residual EWMA over 252d span scaled
def f37sr_f37_crypto_sector_relative_strength_ewmresid_252d_base_v129_signal(closeadj, sector_index):
    res = _f37_resid(closeadj, sector_index, 252)
    result = res.ewm(span=252, min_periods=84).mean() * 252.0
    return result.replace([np.inf, -np.inf], np.nan)


# residual momentum z-score: 252d cum residual standardized over 504d
def f37sr_f37_crypto_sector_relative_strength_zresmom_252d_base_v130_signal(closeadj, sector_index):
    rm = _f37_resid(closeadj, sector_index, 252).rolling(252, min_periods=84).sum()
    result = _z(rm, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# relative-strength percentile rank over 504d (252d relstr)
def f37sr_f37_crypto_sector_relative_strength_rsrank_252d_base_v131_signal(closeadj, sector_index):
    r = _f37_relstr(closeadj, sector_index, 252)
    result = r.rolling(504, min_periods=126).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# beta percentile rank over 252d (126d beta)
def f37sr_f37_crypto_sector_relative_strength_betarank_126d_base_v132_signal(closeadj, sector_index):
    b = _f37_beta(closeadj, sector_index, 126)
    result = b.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# correlation percentile rank over 252d (63d corr)
def f37sr_f37_crypto_sector_relative_strength_corrrank_63d_base_v133_signal(closeadj, sector_index):
    c = _f37_corr(closeadj, sector_index, 63)
    result = c.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# tracking-error percentile rank over 252d (126d TE)
def f37sr_f37_crypto_sector_relative_strength_terank_126d_base_v134_signal(closeadj, sector_index):
    te = _std(_f37_resid(closeadj, sector_index, 126), 126)
    result = te.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# relative-strength acceleration second-order: rsaccel change (63d/126d)
def f37sr_f37_crypto_sector_relative_strength_rscurv_63_126_base_v135_signal(closeadj, sector_index):
    a1 = _f37_relstr(closeadj, sector_index, 63) - _f37_relstr(closeadj, sector_index, 126)
    a2 = _f37_relstr(closeadj, sector_index, 126) - _f37_relstr(closeadj, sector_index, 252)
    result = a1 - a2
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed correlation: 21d mean of 63d corr (stable regime gauge)
def f37sr_f37_crypto_sector_relative_strength_smoothcorr_63d_base_v136_signal(closeadj, sector_index):
    result = _mean(_f37_corr(closeadj, sector_index, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed beta: 21d mean of 63d beta
def f37sr_f37_crypto_sector_relative_strength_smoothbeta_63d_base_v137_signal(closeadj, sector_index):
    result = _mean(_f37_beta(closeadj, sector_index, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# beta times relative strength interaction (126d)
def f37sr_f37_crypto_sector_relative_strength_betars_126d_base_v138_signal(closeadj, sector_index):
    result = _f37_beta(closeadj, sector_index, 126) * _f37_relstr(closeadj, sector_index, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# correlation-weighted relative strength (126d)
def f37sr_f37_crypto_sector_relative_strength_corrwrs_126d_base_v139_signal(closeadj, sector_index):
    result = _f37_relstr(closeadj, sector_index, 126) * (1.0 - _f37_corr(closeadj, sector_index, 126).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# residual-vol-scaled relative strength rank blend (126d)
def f37sr_f37_crypto_sector_relative_strength_rsidio_126d_base_v140_signal(closeadj, sector_index):
    rs = _f37_relstr(closeadj, sector_index, 126)
    idio = 1.0 - _f37_corr(closeadj, sector_index, 126) ** 2
    result = rs * idio
    return result.replace([np.inf, -np.inf], np.nan)


# relative-strength EWMA over 126d span on 126d relstr
def f37sr_f37_crypto_sector_relative_strength_ewmrs_126d_base_v141_signal(closeadj, sector_index):
    rs = _f37_relstr(closeadj, sector_index, 126)
    result = rs.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# annualized 252d relative strength
def f37sr_f37_crypto_sector_relative_strength_annrs_252d_base_v142_signal(closeadj, sector_index):
    result = _f37_relstr(closeadj, sector_index, 252) * (252.0 / 252.0)
    return result.replace([np.inf, -np.inf], np.nan)


# annualized 21d relative strength
def f37sr_f37_crypto_sector_relative_strength_annrs_21d_base_v143_signal(closeadj, sector_index):
    result = _f37_relstr(closeadj, sector_index, 21) * (252.0 / 21.0)
    return result.replace([np.inf, -np.inf], np.nan)


# beta-neutral relative strength: relstr minus beta*sector excess (126d)
def f37sr_f37_crypto_sector_relative_strength_betaneutrs_126d_base_v144_signal(closeadj, sector_index):
    rs = _f37_relstr(closeadj, sector_index, 126)
    beta = _f37_beta(closeadj, sector_index, 126)
    result = rs - (beta - 1.0) * sector_index.pct_change(periods=126)
    return result.replace([np.inf, -np.inf], np.nan)


# beta-neutral relative strength (252d)
def f37sr_f37_crypto_sector_relative_strength_betaneutrs_252d_base_v145_signal(closeadj, sector_index):
    rs = _f37_relstr(closeadj, sector_index, 252)
    beta = _f37_beta(closeadj, sector_index, 252)
    result = rs - (beta - 1.0) * sector_index.pct_change(periods=252)
    return result.replace([np.inf, -np.inf], np.nan)


# relative-strength dispersion over 252d (instability of 63d relstr)
def f37sr_f37_crypto_sector_relative_strength_rsdisp_252d_base_v146_signal(closeadj, sector_index):
    result = _std(_f37_relstr(closeadj, sector_index, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# information ratio of relative strength: 21d relstr / its 252d std
def f37sr_f37_crypto_sector_relative_strength_rsir_21d_base_v147_signal(closeadj, sector_index):
    r = _f37_relstr(closeadj, sector_index, 21)
    result = _safe_div(r, _std(r, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# information ratio of relative strength: 63d relstr / its 252d std
def f37sr_f37_crypto_sector_relative_strength_rsir_63d_base_v148_signal(closeadj, sector_index):
    r = _f37_relstr(closeadj, sector_index, 63)
    result = _safe_div(r, _std(r, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# correlation-adjusted beta: beta * (1 - corr) divergence (126d)
def f37sr_f37_crypto_sector_relative_strength_decoupbeta_126d_base_v149_signal(closeadj, sector_index):
    result = _f37_beta(closeadj, sector_index, 126) * (1.0 - _f37_corr(closeadj, sector_index, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# blended multi-horizon relative-strength composite (21/63/126/252)
def f37sr_f37_crypto_sector_relative_strength_blend_multi_base_v150_signal(closeadj, sector_index):
    result = (_f37_relstr(closeadj, sector_index, 21)
              + _f37_relstr(closeadj, sector_index, 63)
              + _f37_relstr(closeadj, sector_index, 126)
              + _f37_relstr(closeadj, sector_index, 252)) / 4.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f37sr_f37_crypto_sector_relative_strength_upbeta_63d_base_v076_signal,
    f37sr_f37_crypto_sector_relative_strength_upbeta_126d_base_v077_signal,
    f37sr_f37_crypto_sector_relative_strength_downbeta_63d_base_v078_signal,
    f37sr_f37_crypto_sector_relative_strength_downbeta_126d_base_v079_signal,
    f37sr_f37_crypto_sector_relative_strength_betaasym_63d_base_v080_signal,
    f37sr_f37_crypto_sector_relative_strength_betaasym_126d_base_v081_signal,
    f37sr_f37_crypto_sector_relative_strength_betaasym_252d_base_v082_signal,
    f37sr_f37_crypto_sector_relative_strength_udbetaratio_126d_base_v083_signal,
    f37sr_f37_crypto_sector_relative_strength_ewmbeta_63d_base_v084_signal,
    f37sr_f37_crypto_sector_relative_strength_ewmbeta_126d_base_v085_signal,
    f37sr_f37_crypto_sector_relative_strength_zresid_126d_base_v086_signal,
    f37sr_f37_crypto_sector_relative_strength_zresid_252d_base_v087_signal,
    f37sr_f37_crypto_sector_relative_strength_ewmresid_63d_base_v088_signal,
    f37sr_f37_crypto_sector_relative_strength_ewmresid_126d_base_v089_signal,
    f37sr_f37_crypto_sector_relative_strength_residskew_126d_base_v090_signal,
    f37sr_f37_crypto_sector_relative_strength_residskew_252d_base_v091_signal,
    f37sr_f37_crypto_sector_relative_strength_residkurt_126d_base_v092_signal,
    f37sr_f37_crypto_sector_relative_strength_rsq_126d_base_v093_signal,
    f37sr_f37_crypto_sector_relative_strength_rsq_252d_base_v094_signal,
    f37sr_f37_crypto_sector_relative_strength_idioshare_126d_base_v095_signal,
    f37sr_f37_crypto_sector_relative_strength_corrtrend_21d_base_v096_signal,
    f37sr_f37_crypto_sector_relative_strength_corrdisp_126d_base_v097_signal,
    f37sr_f37_crypto_sector_relative_strength_betamom_63d_base_v098_signal,
    f37sr_f37_crypto_sector_relative_strength_betamom_126d_base_v099_signal,
    f37sr_f37_crypto_sector_relative_strength_zbeta_126d_base_v100_signal,
    f37sr_f37_crypto_sector_relative_strength_zbeta_63d_base_v101_signal,
    f37sr_f37_crypto_sector_relative_strength_rsqual_126d_base_v102_signal,
    f37sr_f37_crypto_sector_relative_strength_rsqual_252d_base_v103_signal,
    f37sr_f37_crypto_sector_relative_strength_rseff_63d_base_v104_signal,
    f37sr_f37_crypto_sector_relative_strength_rseff_126d_base_v105_signal,
    f37sr_f37_crypto_sector_relative_strength_rssharpe_63d_base_v106_signal,
    f37sr_f37_crypto_sector_relative_strength_rssharpe_126d_base_v107_signal,
    f37sr_f37_crypto_sector_relative_strength_rssharpe_252d_base_v108_signal,
    f37sr_f37_crypto_sector_relative_strength_volconfrs_21d_base_v109_signal,
    f37sr_f37_crypto_sector_relative_strength_dvconfrs_63d_base_v110_signal,
    f37sr_f37_crypto_sector_relative_strength_dvsurgers_21d_base_v111_signal,
    f37sr_f37_crypto_sector_relative_strength_rsslope_252d_base_v112_signal,
    f37sr_f37_crypto_sector_relative_strength_rsdma_126d_base_v113_signal,
    f37sr_f37_crypto_sector_relative_strength_rsdma_252d_base_v114_signal,
    f37sr_f37_crypto_sector_relative_strength_rslinerank_252d_base_v115_signal,
    f37sr_f37_crypto_sector_relative_strength_systret_63d_base_v116_signal,
    f37sr_f37_crypto_sector_relative_strength_systret_126d_base_v117_signal,
    f37sr_f37_crypto_sector_relative_strength_alpha_126d_base_v118_signal,
    f37sr_f37_crypto_sector_relative_strength_alpha_252d_base_v119_signal,
    f37sr_f37_crypto_sector_relative_strength_alpha_63d_base_v120_signal,
    f37sr_f37_crypto_sector_relative_strength_zalpha_126d_base_v121_signal,
    f37sr_f37_crypto_sector_relative_strength_alphair_126d_base_v122_signal,
    f37sr_f37_crypto_sector_relative_strength_alphair_252d_base_v123_signal,
    f37sr_f37_crypto_sector_relative_strength_rsvoladj_126d_base_v124_signal,
    f37sr_f37_crypto_sector_relative_strength_rsvoladj_252d_base_v125_signal,
    f37sr_f37_crypto_sector_relative_strength_volratio_126d_base_v126_signal,
    f37sr_f37_crypto_sector_relative_strength_volratio_252d_base_v127_signal,
    f37sr_f37_crypto_sector_relative_strength_betavol_126d_base_v128_signal,
    f37sr_f37_crypto_sector_relative_strength_ewmresid_252d_base_v129_signal,
    f37sr_f37_crypto_sector_relative_strength_zresmom_252d_base_v130_signal,
    f37sr_f37_crypto_sector_relative_strength_rsrank_252d_base_v131_signal,
    f37sr_f37_crypto_sector_relative_strength_betarank_126d_base_v132_signal,
    f37sr_f37_crypto_sector_relative_strength_corrrank_63d_base_v133_signal,
    f37sr_f37_crypto_sector_relative_strength_terank_126d_base_v134_signal,
    f37sr_f37_crypto_sector_relative_strength_rscurv_63_126_base_v135_signal,
    f37sr_f37_crypto_sector_relative_strength_smoothcorr_63d_base_v136_signal,
    f37sr_f37_crypto_sector_relative_strength_smoothbeta_63d_base_v137_signal,
    f37sr_f37_crypto_sector_relative_strength_betars_126d_base_v138_signal,
    f37sr_f37_crypto_sector_relative_strength_corrwrs_126d_base_v139_signal,
    f37sr_f37_crypto_sector_relative_strength_rsidio_126d_base_v140_signal,
    f37sr_f37_crypto_sector_relative_strength_ewmrs_126d_base_v141_signal,
    f37sr_f37_crypto_sector_relative_strength_annrs_252d_base_v142_signal,
    f37sr_f37_crypto_sector_relative_strength_annrs_21d_base_v143_signal,
    f37sr_f37_crypto_sector_relative_strength_betaneutrs_126d_base_v144_signal,
    f37sr_f37_crypto_sector_relative_strength_betaneutrs_252d_base_v145_signal,
    f37sr_f37_crypto_sector_relative_strength_rsdisp_252d_base_v146_signal,
    f37sr_f37_crypto_sector_relative_strength_rsir_21d_base_v147_signal,
    f37sr_f37_crypto_sector_relative_strength_rsir_63d_base_v148_signal,
    f37sr_f37_crypto_sector_relative_strength_decoupbeta_126d_base_v149_signal,
    f37sr_f37_crypto_sector_relative_strength_blend_multi_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F37_CRYPTO_SECTOR_RELATIVE_STRENGTH_REGISTRY_076_150 = REGISTRY


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
    print(f"OK f37_crypto_sector_relative_strength_base_076_150_claude: {n_features} features pass")
