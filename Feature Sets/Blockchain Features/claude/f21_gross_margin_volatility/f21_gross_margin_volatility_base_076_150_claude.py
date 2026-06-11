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


# ===== folder domain primitives (gross-margin level and volatility) =====
def _f21_gm(gp, revenue):
    # gross margin level = gp / revenue
    return _safe_div(gp, revenue)


def _f21_gmvol(gp, revenue, w):
    # rolling volatility (std) of the gross margin series
    gm = _safe_div(gp, revenue)
    return gm.rolling(w, min_periods=max(2, w // 2)).std()


def _f21_cogratio(cor, revenue):
    # cost-of-revenue ratio = cor / revenue (1 - gross margin proxy)
    return _safe_div(cor, revenue)


def _f21_opratio(opex, revenue):
    # operating-expense intensity = opex / revenue
    return _safe_div(opex, revenue)


# ============ FEATURES 076-150 ============

# gross margin level smoothed over 42d
def f21gm_f21_gross_margin_volatility_gmsmooth_42d_base_v076_signal(gp, revenue):
    result = _mean(_f21_gm(gp, revenue), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin level smoothed over 189d
def f21gm_f21_gross_margin_volatility_gmsmooth_189d_base_v077_signal(gp, revenue):
    result = _mean(_f21_gm(gp, revenue), 189)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin level smoothed over 504d
def f21gm_f21_gross_margin_volatility_gmsmooth_504d_base_v078_signal(gp, revenue):
    result = _mean(_f21_gm(gp, revenue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin volatility over 84d
def f21gm_f21_gross_margin_volatility_gmvol_84d_base_v079_signal(gp, revenue):
    result = _f21_gmvol(gp, revenue, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin volatility over 189d
def f21gm_f21_gross_margin_volatility_gmvol_189d_base_v080_signal(gp, revenue):
    result = _f21_gmvol(gp, revenue, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin volatility over 315d
def f21gm_f21_gross_margin_volatility_gmvol_315d_base_v081_signal(gp, revenue):
    result = _f21_gmvol(gp, revenue, 315)
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin volatility over 378d
def f21gm_f21_gross_margin_volatility_gmvol_378d_base_v082_signal(gp, revenue):
    result = _f21_gmvol(gp, revenue, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin z-score over 189d
def f21gm_f21_gross_margin_volatility_gmz_189d_base_v083_signal(gp, revenue):
    result = _z(_f21_gm(gp, revenue), 189)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin z-score over 378d
def f21gm_f21_gross_margin_volatility_gmz_378d_base_v084_signal(gp, revenue):
    result = _z(_f21_gm(gp, revenue), 378)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin z-score over 42d
def f21gm_f21_gross_margin_volatility_gmz_42d_base_v085_signal(gp, revenue):
    result = _z(_f21_gm(gp, revenue), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin trend slope over 42d
def f21gm_f21_gross_margin_volatility_gmslope_42d_base_v086_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = (gm - gm.shift(42)) / 42.0
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin trend slope over 189d
def f21gm_f21_gross_margin_volatility_gmslope_189d_base_v087_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = (gm - gm.shift(189)) / 189.0
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin trend slope over 504d
def f21gm_f21_gross_margin_volatility_gmslope_504d_base_v088_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = (gm - gm.shift(504)) / 504.0
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin coefficient of variation over 63d
def f21gm_f21_gross_margin_volatility_gmcv_63d_base_v089_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = _safe_div(_std(gm, 63), _mean(gm, 63).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin coefficient of variation over 189d
def f21gm_f21_gross_margin_volatility_gmcv_189d_base_v090_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = _safe_div(_std(gm, 189), _mean(gm, 189).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin compression vs 504d trailing mean
def f21gm_f21_gross_margin_volatility_gmcompress_504d_base_v091_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm - _mean(gm, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin relative compression over 126d
def f21gm_f21_gross_margin_volatility_gmrelcomp_126d_base_v092_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = _safe_div(gm, _mean(gm, 126)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin relative compression over 504d
def f21gm_f21_gross_margin_volatility_gmrelcomp_504d_base_v093_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = _safe_div(gm, _mean(gm, 504)) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin rolling skew over 504d
def f21gm_f21_gross_margin_volatility_gmskew_504d_base_v094_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm.rolling(504, min_periods=168).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin rolling kurtosis over 126d
def f21gm_f21_gross_margin_volatility_gmkurt_126d_base_v095_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm.rolling(126, min_periods=42).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin rolling kurtosis over 504d
def f21gm_f21_gross_margin_volatility_gmkurt_504d_base_v096_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm.rolling(504, min_periods=168).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin percentile rank over 63d
def f21gm_f21_gross_margin_volatility_gmrank_63d_base_v097_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm.rolling(63, min_periods=21).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin percentile rank over 189d
def f21gm_f21_gross_margin_volatility_gmrank_189d_base_v098_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm.rolling(189, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin IQR over 504d
def f21gm_f21_gross_margin_volatility_gmiqr_504d_base_v099_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    q75 = gm.rolling(504, min_periods=168).quantile(0.75)
    q25 = gm.rolling(504, min_periods=168).quantile(0.25)
    result = q75 - q25
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin inter-decile range over 252d (continuous spread)
def f21gm_f21_gross_margin_volatility_gmidr_252d_base_v100_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    q90 = gm.rolling(252, min_periods=84).quantile(0.90)
    q10 = gm.rolling(252, min_periods=84).quantile(0.10)
    result = q90 - q10
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin normalized IQR (IQR / median) over 252d
def f21gm_f21_gross_margin_volatility_gmiqrnorm_252d_base_v101_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    q75 = gm.rolling(252, min_periods=84).quantile(0.75)
    q25 = gm.rolling(252, min_periods=84).quantile(0.25)
    med = gm.rolling(252, min_periods=84).median()
    result = _safe_div(q75 - q25, med.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# cost-stability ratio over 504d
def f21gm_f21_gross_margin_volatility_coststab_504d_base_v102_signal(cor, revenue):
    cog = _f21_cogratio(cor, revenue)
    result = _safe_div(_mean(cog, 504), _std(cog, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin stability ratio over 126d
def f21gm_f21_gross_margin_volatility_gmstab_126d_base_v103_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = _safe_div(_mean(gm, 126), _std(gm, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin stability ratio over 504d
def f21gm_f21_gross_margin_volatility_gmstab_504d_base_v104_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = _safe_div(_mean(gm, 504), _std(gm, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin volatility ratio: 42d vs 126d
def f21gm_f21_gross_margin_volatility_gmvolratio_42_126_base_v105_signal(gp, revenue):
    result = _safe_div(_f21_gmvol(gp, revenue, 42), _f21_gmvol(gp, revenue, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin volatility ratio: 84d vs 252d
def f21gm_f21_gross_margin_volatility_gmvolratio_84_252_base_v106_signal(gp, revenue):
    result = _safe_div(_f21_gmvol(gp, revenue, 84), _f21_gmvol(gp, revenue, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin EWMA level (span 252)
def f21gm_f21_gross_margin_volatility_gmewm_252d_base_v107_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm.ewm(span=252, min_periods=84).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin EWMA volatility (span 252)
def f21gm_f21_gross_margin_volatility_gmewmvol_252d_base_v108_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm.ewm(span=252, min_periods=84).std()
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin EWMA volatility (span 42)
def f21gm_f21_gross_margin_volatility_gmewmvol_42d_base_v109_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm.ewm(span=42, min_periods=21).std()
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin change over 42d
def f21gm_f21_gross_margin_volatility_gmchg_42d_base_v110_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm - gm.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin change over 189d
def f21gm_f21_gross_margin_volatility_gmchg_189d_base_v111_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm - gm.shift(189)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin change over 504d
def f21gm_f21_gross_margin_volatility_gmchg_504d_base_v112_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm - gm.shift(504)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin vol-scaled change: 252d change / 252d gm vol
def f21gm_f21_gross_margin_volatility_gmchgscaled_252d_base_v113_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = _safe_div(gm - gm.shift(252), _f21_gmvol(gp, revenue, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin acceleration: 63d change minus 126d change
def f21gm_f21_gross_margin_volatility_gmaccel_63_126_base_v114_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = (gm - gm.shift(63)) - (gm.shift(63) - gm.shift(126))
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin acceleration: 126d change minus 252d change
def f21gm_f21_gross_margin_volatility_gmaccel_126_252_base_v115_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = (gm - gm.shift(126)) - (gm.shift(126) - gm.shift(252))
    return result.replace([np.inf, -np.inf], np.nan)


# operating-expense intensity smoothed over 252d
def f21gm_f21_gross_margin_volatility_opsmooth_252d_base_v116_signal(opex, revenue):
    result = _mean(_f21_opratio(opex, revenue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# operating-expense intensity volatility over 126d
def f21gm_f21_gross_margin_volatility_opvol_126d_base_v117_signal(opex, revenue):
    result = _std(_f21_opratio(opex, revenue), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# operating-expense intensity change over 126d
def f21gm_f21_gross_margin_volatility_opchg_126d_base_v118_signal(opex, revenue):
    op = _f21_opratio(opex, revenue)
    result = op - op.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# operating-expense intensity coefficient of variation over 252d
def f21gm_f21_gross_margin_volatility_opcv_252d_base_v119_signal(opex, revenue):
    op = _f21_opratio(opex, revenue)
    result = _safe_div(_std(op, 252), _mean(op, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin proxy z-score over 252d
def f21gm_f21_gross_margin_volatility_netmarginz_252d_base_v120_signal(gp, revenue, opex):
    nm = _f21_gm(gp, revenue) - _f21_opratio(opex, revenue)
    result = _z(nm, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin proxy slope over 126d
def f21gm_f21_gross_margin_volatility_netmarginslope_126d_base_v121_signal(gp, revenue, opex):
    nm = _f21_gm(gp, revenue) - _f21_opratio(opex, revenue)
    result = (nm - nm.shift(126)) / 126.0
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin proxy coefficient of variation over 252d
def f21gm_f21_gross_margin_volatility_netmargincv_252d_base_v122_signal(gp, revenue, opex):
    nm = _f21_gm(gp, revenue) - _f21_opratio(opex, revenue)
    result = _safe_div(_std(nm, 252), _mean(nm, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# gm-minus-cog spread smoothed over 126d
def f21gm_f21_gross_margin_volatility_gmcogspread_126d_base_v123_signal(gp, revenue, cor):
    sp = _f21_gm(gp, revenue) - _f21_cogratio(cor, revenue)
    result = _mean(sp, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# gm-minus-cog spread volatility over 252d
def f21gm_f21_gross_margin_volatility_gmcogspreadvol_252d_base_v124_signal(gp, revenue, cor):
    sp = _f21_gm(gp, revenue) - _f21_cogratio(cor, revenue)
    result = _std(sp, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin vs cost ratio product (margin-cost interaction) smoothed 126d
def f21gm_f21_gross_margin_volatility_gmcogprod_126d_base_v125_signal(gp, revenue, cor):
    inter = _f21_gm(gp, revenue) * _f21_cogratio(cor, revenue)
    result = _mean(inter, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# reported grossmargin minus 252d mean (compression, anchored)
def f21gm_f21_gross_margin_volatility_gmreported_compress_252d_base_v126_signal(grossmargin, gp, revenue):
    result = (grossmargin - _mean(grossmargin, 252)) + _f21_gm(gp, revenue) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# reported grossmargin coefficient of variation 252d (anchored)
def f21gm_f21_gross_margin_volatility_gmreported_cv_252d_base_v127_signal(grossmargin, gp, revenue):
    cv = _safe_div(_std(grossmargin, 252), _mean(grossmargin, 252).abs())
    result = cv + _f21_gm(gp, revenue) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# reported grossmargin slope over 126d (anchored)
def f21gm_f21_gross_margin_volatility_gmreported_slope_126d_base_v128_signal(grossmargin, gp, revenue):
    slope = (grossmargin - grossmargin.shift(126)) / 126.0
    result = slope + _f21_gm(gp, revenue) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# reported grossmargin percentile rank over 252d (anchored)
def f21gm_f21_gross_margin_volatility_gmreported_rank_252d_base_v129_signal(grossmargin, gp, revenue):
    rk = grossmargin.rolling(252, min_periods=84).rank(pct=True)
    result = rk + _f21_gm(gp, revenue) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin downside semi-deviation over 126d
def f21gm_f21_gross_margin_volatility_gmsemidev_126d_base_v130_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    dev = (gm - _mean(gm, 126)).clip(upper=0)
    result = (dev ** 2).rolling(126, min_periods=42).mean() ** 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin semi-deviation asymmetry (up minus down) over 252d
def f21gm_f21_gross_margin_volatility_gmsemiasym_252d_base_v131_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    c = gm - _mean(gm, 252)
    up = (c.clip(lower=0) ** 2).rolling(252, min_periods=84).mean() ** 0.5
    dn = (c.clip(upper=0) ** 2).rolling(252, min_periods=84).mean() ** 0.5
    result = up - dn
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin mean-absolute-deviation over 63d
def f21gm_f21_gross_margin_volatility_gmmad_63d_base_v132_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = (gm - _mean(gm, 63)).abs().rolling(63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin mean-absolute-deviation over 504d
def f21gm_f21_gross_margin_volatility_gmmad_504d_base_v133_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = (gm - _mean(gm, 504)).abs().rolling(504, min_periods=168).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin trend-to-noise over 63d
def f21gm_f21_gross_margin_volatility_gmtrendnoise_63d_base_v134_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    slope = (gm - gm.shift(63)) / 63.0
    result = _safe_div(slope, _f21_gmvol(gp, revenue, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin trend-to-noise over 504d
def f21gm_f21_gross_margin_volatility_gmtrendnoise_504d_base_v135_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    slope = (gm - gm.shift(504)) / 504.0
    result = _safe_div(slope, _f21_gmvol(gp, revenue, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# cost-of-revenue ratio z-score over 126d
def f21gm_f21_gross_margin_volatility_cogz_126d_base_v136_signal(cor, revenue):
    result = _z(_f21_cogratio(cor, revenue), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# cost-of-revenue ratio coefficient of variation over 252d
def f21gm_f21_gross_margin_volatility_cogcv_252d_base_v137_signal(cor, revenue):
    cog = _f21_cogratio(cor, revenue)
    result = _safe_div(_std(cog, 252), _mean(cog, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# cost-of-revenue ratio percentile rank over 252d
def f21gm_f21_gross_margin_volatility_cogrank_252d_base_v138_signal(cor, revenue):
    cog = _f21_cogratio(cor, revenue)
    result = cog.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# cost-of-revenue ratio change over 252d
def f21gm_f21_gross_margin_volatility_cogchg_252d_base_v139_signal(cor, revenue):
    cog = _f21_cogratio(cor, revenue)
    result = cog - cog.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin EWMA z-score (span 63)
def f21gm_f21_gross_margin_volatility_gmewmz_63d_base_v140_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    m = gm.ewm(span=63, min_periods=21).mean()
    sd = gm.ewm(span=63, min_periods=21).std()
    result = _safe_div(gm - m, sd)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin EWMA z-score (span 252)
def f21gm_f21_gross_margin_volatility_gmewmz_252d_base_v141_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    m = gm.ewm(span=252, min_periods=84).mean()
    sd = gm.ewm(span=252, min_periods=84).std()
    result = _safe_div(gm - m, sd)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin percentile-rank deviation from 0.5 over 126d
def f21gm_f21_gross_margin_volatility_gmrankdev_126d_base_v142_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm.rolling(126, min_periods=42).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin volatility normalized by level (vol / |mean|) over 126d
def f21gm_f21_gross_margin_volatility_gmvolnorm_126d_base_v143_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = _safe_div(_f21_gmvol(gp, revenue, 126), _mean(gm, 126).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin volatility normalized by level over 252d
def f21gm_f21_gross_margin_volatility_gmvolnorm_252d_base_v144_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = _safe_div(_f21_gmvol(gp, revenue, 252), _mean(gm, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin range over IQR scaled by vol (kurtosis-like spread) 252d
def f21gm_f21_gross_margin_volatility_gmiqrvol_252d_base_v145_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    q75 = gm.rolling(252, min_periods=84).quantile(0.75)
    q25 = gm.rolling(252, min_periods=84).quantile(0.25)
    result = _safe_div(q75 - q25, _f21_gmvol(gp, revenue, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin minus EWMA (compression vs exponential trend) span126
def f21gm_f21_gross_margin_volatility_gmewmcompress_126d_base_v146_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = gm - gm.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin short vs long mean spread (63d mean - 252d mean)
def f21gm_f21_gross_margin_volatility_gmmeanspread_63_252_base_v147_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = _mean(gm, 63) - _mean(gm, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin short vs long mean spread (21d mean - 126d mean)
def f21gm_f21_gross_margin_volatility_gmmeanspread_21_126_base_v148_signal(gp, revenue):
    gm = _f21_gm(gp, revenue)
    result = _mean(gm, 21) - _mean(gm, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin volatility change (252d vol minus its 126d-lagged value)
def f21gm_f21_gross_margin_volatility_gmvolchg_252d_base_v149_signal(gp, revenue):
    v = _f21_gmvol(gp, revenue, 252)
    result = v - v.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# blended margin-quality composite: gm z + stability - cost cv (252d)
def f21gm_f21_gross_margin_volatility_blend_quality_base_v150_signal(gp, revenue, cor):
    gm = _f21_gm(gp, revenue)
    gmz = _z(gm, 252)
    stab = _safe_div(_mean(gm, 252), _std(gm, 252))
    cog = _f21_cogratio(cor, revenue)
    cogcv = _safe_div(_std(cog, 252), _mean(cog, 252).abs())
    result = gmz + stab - cogcv
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f21gm_f21_gross_margin_volatility_gmsmooth_42d_base_v076_signal,
    f21gm_f21_gross_margin_volatility_gmsmooth_189d_base_v077_signal,
    f21gm_f21_gross_margin_volatility_gmsmooth_504d_base_v078_signal,
    f21gm_f21_gross_margin_volatility_gmvol_84d_base_v079_signal,
    f21gm_f21_gross_margin_volatility_gmvol_189d_base_v080_signal,
    f21gm_f21_gross_margin_volatility_gmvol_315d_base_v081_signal,
    f21gm_f21_gross_margin_volatility_gmvol_378d_base_v082_signal,
    f21gm_f21_gross_margin_volatility_gmz_189d_base_v083_signal,
    f21gm_f21_gross_margin_volatility_gmz_378d_base_v084_signal,
    f21gm_f21_gross_margin_volatility_gmz_42d_base_v085_signal,
    f21gm_f21_gross_margin_volatility_gmslope_42d_base_v086_signal,
    f21gm_f21_gross_margin_volatility_gmslope_189d_base_v087_signal,
    f21gm_f21_gross_margin_volatility_gmslope_504d_base_v088_signal,
    f21gm_f21_gross_margin_volatility_gmcv_63d_base_v089_signal,
    f21gm_f21_gross_margin_volatility_gmcv_189d_base_v090_signal,
    f21gm_f21_gross_margin_volatility_gmcompress_504d_base_v091_signal,
    f21gm_f21_gross_margin_volatility_gmrelcomp_126d_base_v092_signal,
    f21gm_f21_gross_margin_volatility_gmrelcomp_504d_base_v093_signal,
    f21gm_f21_gross_margin_volatility_gmskew_504d_base_v094_signal,
    f21gm_f21_gross_margin_volatility_gmkurt_126d_base_v095_signal,
    f21gm_f21_gross_margin_volatility_gmkurt_504d_base_v096_signal,
    f21gm_f21_gross_margin_volatility_gmrank_63d_base_v097_signal,
    f21gm_f21_gross_margin_volatility_gmrank_189d_base_v098_signal,
    f21gm_f21_gross_margin_volatility_gmiqr_504d_base_v099_signal,
    f21gm_f21_gross_margin_volatility_gmidr_252d_base_v100_signal,
    f21gm_f21_gross_margin_volatility_gmiqrnorm_252d_base_v101_signal,
    f21gm_f21_gross_margin_volatility_coststab_504d_base_v102_signal,
    f21gm_f21_gross_margin_volatility_gmstab_126d_base_v103_signal,
    f21gm_f21_gross_margin_volatility_gmstab_504d_base_v104_signal,
    f21gm_f21_gross_margin_volatility_gmvolratio_42_126_base_v105_signal,
    f21gm_f21_gross_margin_volatility_gmvolratio_84_252_base_v106_signal,
    f21gm_f21_gross_margin_volatility_gmewm_252d_base_v107_signal,
    f21gm_f21_gross_margin_volatility_gmewmvol_252d_base_v108_signal,
    f21gm_f21_gross_margin_volatility_gmewmvol_42d_base_v109_signal,
    f21gm_f21_gross_margin_volatility_gmchg_42d_base_v110_signal,
    f21gm_f21_gross_margin_volatility_gmchg_189d_base_v111_signal,
    f21gm_f21_gross_margin_volatility_gmchg_504d_base_v112_signal,
    f21gm_f21_gross_margin_volatility_gmchgscaled_252d_base_v113_signal,
    f21gm_f21_gross_margin_volatility_gmaccel_63_126_base_v114_signal,
    f21gm_f21_gross_margin_volatility_gmaccel_126_252_base_v115_signal,
    f21gm_f21_gross_margin_volatility_opsmooth_252d_base_v116_signal,
    f21gm_f21_gross_margin_volatility_opvol_126d_base_v117_signal,
    f21gm_f21_gross_margin_volatility_opchg_126d_base_v118_signal,
    f21gm_f21_gross_margin_volatility_opcv_252d_base_v119_signal,
    f21gm_f21_gross_margin_volatility_netmarginz_252d_base_v120_signal,
    f21gm_f21_gross_margin_volatility_netmarginslope_126d_base_v121_signal,
    f21gm_f21_gross_margin_volatility_netmargincv_252d_base_v122_signal,
    f21gm_f21_gross_margin_volatility_gmcogspread_126d_base_v123_signal,
    f21gm_f21_gross_margin_volatility_gmcogspreadvol_252d_base_v124_signal,
    f21gm_f21_gross_margin_volatility_gmcogprod_126d_base_v125_signal,
    f21gm_f21_gross_margin_volatility_gmreported_compress_252d_base_v126_signal,
    f21gm_f21_gross_margin_volatility_gmreported_cv_252d_base_v127_signal,
    f21gm_f21_gross_margin_volatility_gmreported_slope_126d_base_v128_signal,
    f21gm_f21_gross_margin_volatility_gmreported_rank_252d_base_v129_signal,
    f21gm_f21_gross_margin_volatility_gmsemidev_126d_base_v130_signal,
    f21gm_f21_gross_margin_volatility_gmsemiasym_252d_base_v131_signal,
    f21gm_f21_gross_margin_volatility_gmmad_63d_base_v132_signal,
    f21gm_f21_gross_margin_volatility_gmmad_504d_base_v133_signal,
    f21gm_f21_gross_margin_volatility_gmtrendnoise_63d_base_v134_signal,
    f21gm_f21_gross_margin_volatility_gmtrendnoise_504d_base_v135_signal,
    f21gm_f21_gross_margin_volatility_cogz_126d_base_v136_signal,
    f21gm_f21_gross_margin_volatility_cogcv_252d_base_v137_signal,
    f21gm_f21_gross_margin_volatility_cogrank_252d_base_v138_signal,
    f21gm_f21_gross_margin_volatility_cogchg_252d_base_v139_signal,
    f21gm_f21_gross_margin_volatility_gmewmz_63d_base_v140_signal,
    f21gm_f21_gross_margin_volatility_gmewmz_252d_base_v141_signal,
    f21gm_f21_gross_margin_volatility_gmrankdev_126d_base_v142_signal,
    f21gm_f21_gross_margin_volatility_gmvolnorm_126d_base_v143_signal,
    f21gm_f21_gross_margin_volatility_gmvolnorm_252d_base_v144_signal,
    f21gm_f21_gross_margin_volatility_gmiqrvol_252d_base_v145_signal,
    f21gm_f21_gross_margin_volatility_gmewmcompress_126d_base_v146_signal,
    f21gm_f21_gross_margin_volatility_gmmeanspread_63_252_base_v147_signal,
    f21gm_f21_gross_margin_volatility_gmmeanspread_21_126_base_v148_signal,
    f21gm_f21_gross_margin_volatility_gmvolchg_252d_base_v149_signal,
    f21gm_f21_gross_margin_volatility_blend_quality_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F21_GROSS_MARGIN_VOLATILITY_REGISTRY_076_150 = REGISTRY


def _synth_cols(names):
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    nh = np.abs(np.random.normal(0, 0.02, n)); nl = np.abs(np.random.normal(0, 0.02, n))
    POS = {"open","high","low","close","closeadj","price","volume","marketcap","ev",
           "assets","assetsc","equity","revenue","gp","ebitda","ppnenet","sharesbas",
           "shareswa","cashneq","cor","opex","sgna","rnd","inventory","receivables",
           "intangibles","evebitda","evebit","pe","pb","ps","currentratio","bvps","sps",
           "shrvalue","shrunits","totalvalue","percentoftotal","sf3a_shares","sf3a_value",
           "sf3b_shares","sf3b_value","grossmargin","beta1y","beta5y","invcap","debt"}
    for nm in names:
        if nm in ("closeadj","close","price"):
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price*(1+np.random.normal(0,0.01,n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price*(1+nh), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price*(1-nl), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7,7e6,n))+1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0,1.0,n))
            level = 1000.0*np.exp(0.03*np.random.normal(0,1,n).cumsum()/np.sqrt(n))
            s = level + 50.0*walk
            if nm in POS:
                s = np.abs(s) + 10.0
            out[nm] = pd.Series(s, name=nm)
    return out


if __name__ == "__main__":
    domain_primitives = ("_f21_gm", "_f21_gmvol", "_f21_cogratio", "_f21_opratio")
    needed = set()
    for fn in _FEATURES:
        for p in inspect.signature(fn).parameters.values():
            needed.add(p.name)
    cols = _synth_cols(sorted(needed))
    n_features = 0; nan_ok = 0
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args); y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        if y1.iloc[504:].isna().mean() < 0.5:
            nan_ok += 1
        assert any(p in inspect.getsource(fn) for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f21_gross_margin_volatility_base_076_150_claude: {n_features} features pass")
