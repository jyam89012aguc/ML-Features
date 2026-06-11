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


# ===== folder domain primitives =====
def _f30_mix_proxy(grossmargin, revenue, w):
    # Mix proxy: gross margin × revenue growth (high-margin commercial vs low-margin residential)
    return grossmargin * revenue.pct_change(periods=w)


def _f30_segment_growth_divergence(revenue, ebitda, w):
    # Divergence between revenue growth and ebitda growth — segment mix shift indicator
    return revenue.pct_change(periods=w) - ebitda.pct_change(periods=w)


def _f30_mix_quality(grossmargin, ebitdamargin, w):
    # Mix quality: gross margin minus its trailing mean × ebitda margin
    gm_dev = grossmargin - grossmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    return gm_dev * ebitdamargin


def f30rcm_residential_commercial_mix_segdiv_zema252_base_v076_signal(revenue, ebitda, closeadj):
    result = (_z(_f30_segment_growth_divergence(revenue, ebitda, 252), 504).ewm(span=63, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_xlogrev_252_base_v077_signal(revenue, ebitda, closeadj):
    result = (_f30_segment_growth_divergence(revenue, ebitda, 252) * np.log(revenue.replace(0, np.nan).abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_xlogebitda_252_base_v078_signal(revenue, ebitda, closeadj):
    result = (_f30_segment_growth_divergence(revenue, ebitda, 252) * np.log(ebitda.replace(0, np.nan).abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_xstd_252_base_v079_signal(revenue, ebitda, closeadj):
    result = (_f30_segment_growth_divergence(revenue, ebitda, 252) * _std(closeadj, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_xebitda_growth_base_v080_signal(revenue, ebitda, closeadj):
    result = (_f30_segment_growth_divergence(revenue, ebitda, 252) * ebitda.pct_change(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_5d_base_v081_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f30_mix_quality(grossmargin, ebitdamargin, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_10d_base_v082_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f30_mix_quality(grossmargin, ebitdamargin, 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_21d_base_v083_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f30_mix_quality(grossmargin, ebitdamargin, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_42d_base_v084_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f30_mix_quality(grossmargin, ebitdamargin, 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_63d_base_v085_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f30_mix_quality(grossmargin, ebitdamargin, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_126d_base_v086_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f30_mix_quality(grossmargin, ebitdamargin, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_189d_base_v087_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f30_mix_quality(grossmargin, ebitdamargin, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_252d_base_v088_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f30_mix_quality(grossmargin, ebitdamargin, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_378d_base_v089_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f30_mix_quality(grossmargin, ebitdamargin, 378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_504d_base_v090_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f30_mix_quality(grossmargin, ebitdamargin, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_ma21d_base_v091_signal(grossmargin, ebitdamargin, closeadj):
    result = (_mean(_f30_mix_quality(grossmargin, ebitdamargin, 21), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_ma63d_base_v092_signal(grossmargin, ebitdamargin, closeadj):
    result = (_mean(_f30_mix_quality(grossmargin, ebitdamargin, 63), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_ma252d_base_v093_signal(grossmargin, ebitdamargin, closeadj):
    result = (_mean(_f30_mix_quality(grossmargin, ebitdamargin, 252), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_std63d_base_v094_signal(grossmargin, ebitdamargin, closeadj):
    result = (_std(_f30_mix_quality(grossmargin, ebitdamargin, 63), 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_std252d_base_v095_signal(grossmargin, ebitdamargin, closeadj):
    result = (_std(_f30_mix_quality(grossmargin, ebitdamargin, 252), 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_z63d_base_v096_signal(grossmargin, ebitdamargin, closeadj):
    result = (_z(_f30_mix_quality(grossmargin, ebitdamargin, 63), 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_z252d_base_v097_signal(grossmargin, ebitdamargin, closeadj):
    result = (_z(_f30_mix_quality(grossmargin, ebitdamargin, 252), 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_ema21d_base_v098_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f30_mix_quality(grossmargin, ebitdamargin, 21).ewm(span=21, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_ema63d_base_v099_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f30_mix_quality(grossmargin, ebitdamargin, 63).ewm(span=63, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_ema252d_base_v100_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f30_mix_quality(grossmargin, ebitdamargin, 252).ewm(span=252, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_rank252d_base_v101_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f30_mix_quality(grossmargin, ebitdamargin, 63).rolling(252, min_periods=63).rank(pct=True)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_rank504d_base_v102_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f30_mix_quality(grossmargin, ebitdamargin, 63).rolling(504, min_periods=126).rank(pct=True)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_abs_base_v103_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f30_mix_quality(grossmargin, ebitdamargin, 63).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_sq_base_v104_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f30_mix_quality(grossmargin, ebitdamargin, 63) * _f30_mix_quality(grossmargin, ebitdamargin, 63).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_dev252_base_v105_signal(grossmargin, ebitdamargin, closeadj):
    result = ((_f30_mix_quality(grossmargin, ebitdamargin, 252) - _mean(_f30_mix_quality(grossmargin, ebitdamargin, 252), 252))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_var252_base_v106_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f30_mix_quality(grossmargin, ebitdamargin, 252).rolling(252, min_periods=63).var() * 100.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_xlogpx_252_base_v107_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f30_mix_quality(grossmargin, ebitdamargin, 252) * np.log(closeadj.replace(0, np.nan).abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_xpxgap_252_base_v108_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f30_mix_quality(grossmargin, ebitdamargin, 252) * (closeadj - _mean(closeadj, 252))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_xpxdet_252_base_v109_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f30_mix_quality(grossmargin, ebitdamargin, 252) * (closeadj / _mean(closeadj, 252).replace(0, np.nan) - 1.0)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_xpkgap_252_base_v110_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f30_mix_quality(grossmargin, ebitdamargin, 252) * ((closeadj - closeadj.rolling(252, min_periods=63).max()) / closeadj.rolling(252, min_periods=63).max().replace(0, np.nan).abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_xrange_252_base_v111_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f30_mix_quality(grossmargin, ebitdamargin, 252) * (closeadj.rolling(252, min_periods=63).max() - closeadj.rolling(252, min_periods=63).min()) / closeadj) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_xvolz_252_base_v112_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f30_mix_quality(grossmargin, ebitdamargin, 252) * _z(closeadj, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_xpxchg_63_base_v113_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f30_mix_quality(grossmargin, ebitdamargin, 63) * closeadj.pct_change(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_diff63_base_v114_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f30_mix_quality(grossmargin, ebitdamargin, 63).diff(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_sign_base_v115_signal(grossmargin, ebitdamargin, closeadj):
    result = (np.sign(_f30_mix_quality(grossmargin, ebitdamargin, 63)) * closeadj.pct_change(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_zema252_base_v116_signal(grossmargin, ebitdamargin, closeadj):
    result = (_z(_f30_mix_quality(grossmargin, ebitdamargin, 252), 504).ewm(span=63, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_xgrossmargin_base_v117_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f30_mix_quality(grossmargin, ebitdamargin, 252) * grossmargin) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_xebitdamargin_base_v118_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f30_mix_quality(grossmargin, ebitdamargin, 252) * ebitdamargin) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_xstd_252_base_v119_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f30_mix_quality(grossmargin, ebitdamargin, 252) * _std(closeadj, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_x_gmdiff_252_base_v120_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f30_mix_quality(grossmargin, ebitdamargin, 252) * grossmargin.diff(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_x_segdiv_63_base_v121_signal(grossmargin, revenue, ebitda, closeadj):
    result = (_f30_mix_proxy(grossmargin, revenue, 63) * _f30_segment_growth_divergence(revenue, ebitda, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_x_segdiv_252_base_v122_signal(grossmargin, revenue, ebitda, closeadj):
    result = (_f30_mix_proxy(grossmargin, revenue, 252) * _f30_segment_growth_divergence(revenue, ebitda, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_x_mixq_63_base_v123_signal(grossmargin, ebitdamargin, revenue, closeadj):
    result = (_f30_mix_proxy(grossmargin, revenue, 63) * _f30_mix_quality(grossmargin, ebitdamargin, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_x_mixq_252_base_v124_signal(grossmargin, ebitdamargin, revenue, ebitda, closeadj):
    result = (_f30_segment_growth_divergence(revenue, ebitda, 252) * _f30_mix_quality(grossmargin, ebitdamargin, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_plus_mixq_63_base_v125_signal(grossmargin, ebitdamargin, revenue, closeadj):
    result = ((_f30_mix_proxy(grossmargin, revenue, 63) + _f30_mix_quality(grossmargin, ebitdamargin, 63))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_compo_all_252_base_v126_signal(grossmargin, ebitdamargin, revenue, ebitda, closeadj):
    result = ((_f30_mix_proxy(grossmargin, revenue, 252) + _f30_segment_growth_divergence(revenue, ebitda, 252) + _f30_mix_quality(grossmargin, ebitdamargin, 252))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_compow_all_252_base_v127_signal(grossmargin, ebitdamargin, revenue, ebitda, closeadj):
    result = ((0.5 * _f30_mix_proxy(grossmargin, revenue, 252) + 0.3 * _f30_segment_growth_divergence(revenue, ebitda, 252) + 0.2 * _f30_mix_quality(grossmargin, ebitdamargin, 252))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_compo_all_63_base_v128_signal(grossmargin, ebitdamargin, revenue, ebitda, closeadj):
    result = ((_f30_mix_proxy(grossmargin, revenue, 63) + _f30_segment_growth_divergence(revenue, ebitda, 63) + _f30_mix_quality(grossmargin, ebitdamargin, 63))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_minus_segdiv_63_base_v129_signal(grossmargin, revenue, ebitda, closeadj):
    result = ((_f30_mix_proxy(grossmargin, revenue, 63) - _f30_segment_growth_divergence(revenue, ebitda, 63))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_minus_segdiv_252_base_v130_signal(grossmargin, ebitdamargin, revenue, ebitda, closeadj):
    result = ((_f30_mix_quality(grossmargin, ebitdamargin, 252) - _f30_segment_growth_divergence(revenue, ebitda, 252))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_x_segdiv_x_close_base_v131_signal(grossmargin, revenue, ebitda, closeadj):
    result = (_f30_mix_proxy(grossmargin, revenue, 63) * _f30_segment_growth_divergence(revenue, ebitda, 63) * closeadj.pct_change(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_x_segdiv_x_close_base_v132_signal(grossmargin, ebitdamargin, revenue, ebitda, closeadj):
    result = (_f30_mix_quality(grossmargin, ebitdamargin, 63) * _f30_segment_growth_divergence(revenue, ebitda, 63) * closeadj.pct_change(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_compow3_63_base_v133_signal(grossmargin, ebitdamargin, revenue, ebitda, closeadj):
    result = ((0.4 * _f30_mix_proxy(grossmargin, revenue, 63) + 0.3 * _f30_segment_growth_divergence(revenue, ebitda, 63) + 0.3 * _f30_mix_quality(grossmargin, ebitdamargin, 63))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_x_gp_base_v134_signal(grossmargin, revenue, closeadj):
    result = (_f30_mix_proxy(grossmargin, revenue, 252) * grossmargin) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_x_revg_252_base_v135_signal(revenue, ebitda, closeadj):
    result = (_f30_segment_growth_divergence(revenue, ebitda, 252) * revenue.pct_change(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_x_revg_252_base_v136_signal(grossmargin, ebitdamargin, revenue, closeadj):
    result = (_f30_mix_quality(grossmargin, ebitdamargin, 252) * revenue.pct_change(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_x_ebitda_growth_base_v137_signal(grossmargin, revenue, ebitda, closeadj):
    result = (_f30_mix_proxy(grossmargin, revenue, 252) * ebitda.pct_change(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_x_emargdiff_252_base_v138_signal(revenue, ebitda, closeadj):
    result = (_f30_segment_growth_divergence(revenue, ebitda, 252) * ebitda.diff(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_x_emarg_252_base_v139_signal(grossmargin, ebitdamargin, closeadj):
    result = (_f30_mix_quality(grossmargin, ebitdamargin, 252) * ebitdamargin.diff(252) * 100.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_logema_63_base_v140_signal(grossmargin, revenue, closeadj):
    result = (np.log(_f30_mix_proxy(grossmargin, revenue, 63).abs() + 1e-6).ewm(span=21, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_logema_252_base_v141_signal(grossmargin, revenue, closeadj):
    result = (np.log(_f30_mix_proxy(grossmargin, revenue, 252).abs() + 1e-6).ewm(span=63, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_logema_63_base_v142_signal(revenue, ebitda, closeadj):
    result = (np.log(_f30_segment_growth_divergence(revenue, ebitda, 63).abs() + 1e-6).ewm(span=21, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_logema_252_base_v143_signal(grossmargin, ebitdamargin, closeadj):
    result = (np.log(_f30_mix_quality(grossmargin, ebitdamargin, 252).abs() + 1e-6).ewm(span=63, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_x_segdiv_504_base_v144_signal(grossmargin, revenue, ebitda, closeadj):
    result = (_f30_mix_proxy(grossmargin, revenue, 504) * _f30_segment_growth_divergence(revenue, ebitda, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_x_mixq_504_base_v145_signal(grossmargin, ebitdamargin, revenue, closeadj):
    result = (_f30_mix_proxy(grossmargin, revenue, 504) * _f30_mix_quality(grossmargin, ebitdamargin, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_x_mixq_504_base_v146_signal(grossmargin, ebitdamargin, revenue, ebitda, closeadj):
    result = (_f30_segment_growth_divergence(revenue, ebitda, 504) * _f30_mix_quality(grossmargin, ebitdamargin, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixp_emadiff_63_base_v147_signal(grossmargin, revenue, closeadj):
    result = ((_f30_mix_proxy(grossmargin, revenue, 63).ewm(span=21, adjust=False).mean() - _f30_mix_proxy(grossmargin, revenue, 63).ewm(span=63, adjust=False).mean())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_segdiv_emadiff_63_base_v148_signal(revenue, ebitda, closeadj):
    result = ((_f30_segment_growth_divergence(revenue, ebitda, 63).ewm(span=21, adjust=False).mean() - _f30_segment_growth_divergence(revenue, ebitda, 63).ewm(span=63, adjust=False).mean())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_mixq_emadiff_63_base_v149_signal(grossmargin, ebitdamargin, closeadj):
    result = ((_f30_mix_quality(grossmargin, ebitdamargin, 63).ewm(span=21, adjust=False).mean() - _f30_mix_quality(grossmargin, ebitdamargin, 63).ewm(span=63, adjust=False).mean())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f30rcm_residential_commercial_mix_compo_all_504_base_v150_signal(grossmargin, ebitdamargin, revenue, ebitda, closeadj):
    result = ((_f30_mix_proxy(grossmargin, revenue, 504) + _f30_segment_growth_divergence(revenue, ebitda, 504) + _f30_mix_quality(grossmargin, ebitdamargin, 504))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f30rcm_residential_commercial_mix_segdiv_zema252_base_v076_signal,
    f30rcm_residential_commercial_mix_segdiv_xlogrev_252_base_v077_signal,
    f30rcm_residential_commercial_mix_segdiv_xlogebitda_252_base_v078_signal,
    f30rcm_residential_commercial_mix_segdiv_xstd_252_base_v079_signal,
    f30rcm_residential_commercial_mix_segdiv_xebitda_growth_base_v080_signal,
    f30rcm_residential_commercial_mix_mixq_5d_base_v081_signal,
    f30rcm_residential_commercial_mix_mixq_10d_base_v082_signal,
    f30rcm_residential_commercial_mix_mixq_21d_base_v083_signal,
    f30rcm_residential_commercial_mix_mixq_42d_base_v084_signal,
    f30rcm_residential_commercial_mix_mixq_63d_base_v085_signal,
    f30rcm_residential_commercial_mix_mixq_126d_base_v086_signal,
    f30rcm_residential_commercial_mix_mixq_189d_base_v087_signal,
    f30rcm_residential_commercial_mix_mixq_252d_base_v088_signal,
    f30rcm_residential_commercial_mix_mixq_378d_base_v089_signal,
    f30rcm_residential_commercial_mix_mixq_504d_base_v090_signal,
    f30rcm_residential_commercial_mix_mixq_ma21d_base_v091_signal,
    f30rcm_residential_commercial_mix_mixq_ma63d_base_v092_signal,
    f30rcm_residential_commercial_mix_mixq_ma252d_base_v093_signal,
    f30rcm_residential_commercial_mix_mixq_std63d_base_v094_signal,
    f30rcm_residential_commercial_mix_mixq_std252d_base_v095_signal,
    f30rcm_residential_commercial_mix_mixq_z63d_base_v096_signal,
    f30rcm_residential_commercial_mix_mixq_z252d_base_v097_signal,
    f30rcm_residential_commercial_mix_mixq_ema21d_base_v098_signal,
    f30rcm_residential_commercial_mix_mixq_ema63d_base_v099_signal,
    f30rcm_residential_commercial_mix_mixq_ema252d_base_v100_signal,
    f30rcm_residential_commercial_mix_mixq_rank252d_base_v101_signal,
    f30rcm_residential_commercial_mix_mixq_rank504d_base_v102_signal,
    f30rcm_residential_commercial_mix_mixq_abs_base_v103_signal,
    f30rcm_residential_commercial_mix_mixq_sq_base_v104_signal,
    f30rcm_residential_commercial_mix_mixq_dev252_base_v105_signal,
    f30rcm_residential_commercial_mix_mixq_var252_base_v106_signal,
    f30rcm_residential_commercial_mix_mixq_xlogpx_252_base_v107_signal,
    f30rcm_residential_commercial_mix_mixq_xpxgap_252_base_v108_signal,
    f30rcm_residential_commercial_mix_mixq_xpxdet_252_base_v109_signal,
    f30rcm_residential_commercial_mix_mixq_xpkgap_252_base_v110_signal,
    f30rcm_residential_commercial_mix_mixq_xrange_252_base_v111_signal,
    f30rcm_residential_commercial_mix_mixq_xvolz_252_base_v112_signal,
    f30rcm_residential_commercial_mix_mixq_xpxchg_63_base_v113_signal,
    f30rcm_residential_commercial_mix_mixq_diff63_base_v114_signal,
    f30rcm_residential_commercial_mix_mixq_sign_base_v115_signal,
    f30rcm_residential_commercial_mix_mixq_zema252_base_v116_signal,
    f30rcm_residential_commercial_mix_mixq_xgrossmargin_base_v117_signal,
    f30rcm_residential_commercial_mix_mixq_xebitdamargin_base_v118_signal,
    f30rcm_residential_commercial_mix_mixq_xstd_252_base_v119_signal,
    f30rcm_residential_commercial_mix_mixq_x_gmdiff_252_base_v120_signal,
    f30rcm_residential_commercial_mix_mixp_x_segdiv_63_base_v121_signal,
    f30rcm_residential_commercial_mix_mixp_x_segdiv_252_base_v122_signal,
    f30rcm_residential_commercial_mix_mixp_x_mixq_63_base_v123_signal,
    f30rcm_residential_commercial_mix_segdiv_x_mixq_252_base_v124_signal,
    f30rcm_residential_commercial_mix_mixp_plus_mixq_63_base_v125_signal,
    f30rcm_residential_commercial_mix_compo_all_252_base_v126_signal,
    f30rcm_residential_commercial_mix_compow_all_252_base_v127_signal,
    f30rcm_residential_commercial_mix_compo_all_63_base_v128_signal,
    f30rcm_residential_commercial_mix_mixp_minus_segdiv_63_base_v129_signal,
    f30rcm_residential_commercial_mix_mixq_minus_segdiv_252_base_v130_signal,
    f30rcm_residential_commercial_mix_mixp_x_segdiv_x_close_base_v131_signal,
    f30rcm_residential_commercial_mix_mixq_x_segdiv_x_close_base_v132_signal,
    f30rcm_residential_commercial_mix_compow3_63_base_v133_signal,
    f30rcm_residential_commercial_mix_mixp_x_gp_base_v134_signal,
    f30rcm_residential_commercial_mix_segdiv_x_revg_252_base_v135_signal,
    f30rcm_residential_commercial_mix_mixq_x_revg_252_base_v136_signal,
    f30rcm_residential_commercial_mix_mixp_x_ebitda_growth_base_v137_signal,
    f30rcm_residential_commercial_mix_segdiv_x_emargdiff_252_base_v138_signal,
    f30rcm_residential_commercial_mix_mixq_x_emarg_252_base_v139_signal,
    f30rcm_residential_commercial_mix_mixp_logema_63_base_v140_signal,
    f30rcm_residential_commercial_mix_mixp_logema_252_base_v141_signal,
    f30rcm_residential_commercial_mix_segdiv_logema_63_base_v142_signal,
    f30rcm_residential_commercial_mix_mixq_logema_252_base_v143_signal,
    f30rcm_residential_commercial_mix_mixp_x_segdiv_504_base_v144_signal,
    f30rcm_residential_commercial_mix_mixp_x_mixq_504_base_v145_signal,
    f30rcm_residential_commercial_mix_segdiv_x_mixq_504_base_v146_signal,
    f30rcm_residential_commercial_mix_mixp_emadiff_63_base_v147_signal,
    f30rcm_residential_commercial_mix_segdiv_emadiff_63_base_v148_signal,
    f30rcm_residential_commercial_mix_mixq_emadiff_63_base_v149_signal,
    f30rcm_residential_commercial_mix_compo_all_504_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F30_RESIDENTIAL_COMMERCIAL_MIX_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    grossmargin = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "ebitda": ebitda, "grossmargin": grossmargin, "ebitdamargin": ebitdamargin,
    }


    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f30_mix_proxy", "_f30_segment_growth_divergence", "_f30_mix_quality")
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
    print(f"OK f30_residential_commercial_mix_base_076_150_claude: {n_features} features pass")
