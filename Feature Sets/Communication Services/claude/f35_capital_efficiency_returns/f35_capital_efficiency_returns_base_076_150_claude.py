import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5

HURDLE = 0.08  # cost-of-capital hurdle for ROIC spread


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


def _slope(s, w):
    def _f(a):
        m = len(a)
        idx = np.arange(m, dtype=float)
        idx = idx - idx.mean()
        denom = (idx ** 2).sum()
        if denom == 0:
            return np.nan
        return float(np.dot(idx, a - a.mean()) / denom)
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_f, raw=True)


# ===== folder domain primitives (capital efficiency / returns) =====
def _f35_spread(roic):
    return roic - HURDLE


def _f35_assetturn(revenue, assets):
    return revenue / assets.replace(0, np.nan)


def _f35_equityturn(revenue, equity):
    return revenue / equity.replace(0, np.nan)


def _f35_disp3(a, b, c):
    return pd.concat([a, b, c], axis=1).std(axis=1)


def _f35_capsink(roic, invcap, w):
    neg = (roic < 0).astype(float).rolling(w, min_periods=max(1, w // 2)).mean()
    inv_g = invcap / invcap.shift(w).replace(0, np.nan) - 1.0
    return neg * inv_g.clip(lower=0)


# ============================================================
# ROIC level over a half-year (slower durable return)
def f35ce_f35_capital_efficiency_returns_roiclvl_126d_base_v076_signal(roic):
    b = _mean(roic, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA level over a half-year
def f35ce_f35_capital_efficiency_returns_roalvl_126d_base_v077_signal(roa):
    b = _mean(roa, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS level over a half-year
def f35ce_f35_capital_efficiency_returns_roslvl_126d_base_v078_signal(ros):
    b = _mean(ros, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread sign-rate: fraction of half-year ROIC above hurdle minus 0.5 (regime)
def f35ce_f35_capital_efficiency_returns_spreadsign_126d_base_v079_signal(roic):
    above = (roic > HURDLE).astype(float)
    b = above.rolling(126, min_periods=63).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC z vs its own 504d history (long de-trended level)
def f35ce_f35_capital_efficiency_returns_roicz_504d_base_v080_signal(roic):
    b = _z(roic, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA z vs its own 504d history
def f35ce_f35_capital_efficiency_returns_roaz_504d_base_v081_signal(roa):
    b = _z(roa, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS z vs its own 504d history
def f35ce_f35_capital_efficiency_returns_rosz_504d_base_v082_signal(ros):
    b = _z(ros, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC trend over 252d (annual return trajectory)
def f35ce_f35_capital_efficiency_returns_roictrend_252d_base_v083_signal(roic):
    b = _slope(roic, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA trend over 252d
def f35ce_f35_capital_efficiency_returns_roatrend_252d_base_v084_signal(roa):
    b = _slope(roa, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS trend over 252d
def f35ce_f35_capital_efficiency_returns_rostrend_252d_base_v085_signal(ros):
    b = _slope(ros, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset turnover over a half-year (slower capital productivity)
def f35ce_f35_capital_efficiency_returns_aturn_126d_base_v086_signal(revenue, assets):
    b = _mean(_f35_assetturn(revenue, assets), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reported asset-turnover percentile-rank (productivity regime)
def f35ce_f35_capital_efficiency_returns_aturnrank_504d_base_v087_signal(assetturnover):
    b = assetturnover.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity turnover over a half-year
def f35ce_f35_capital_efficiency_returns_eturn_126d_base_v088_signal(revenue, equity):
    b = _mean(_f35_equityturn(revenue, equity), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invested-capital turnover z (de-trended capital productivity)
def f35ce_f35_capital_efficiency_returns_icturnz_252d_base_v089_signal(revenue, invcap):
    ict = revenue / invcap.replace(0, np.nan)
    b = _z(ict, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-sink flag over a half-year horizon (faster value-destruction detector)
def f35ce_f35_capital_efficiency_returns_capsink_126d_base_v090_signal(roic, invcap):
    b = _f35_capsink(roic, invcap, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# returns dispersion smoothed over a quarter (steady disagreement among returns)
def f35ce_f35_capital_efficiency_returns_retdispsm_63d_base_v091_signal(roic, roa, ros):
    disp = _f35_disp3(roic, roa, ros)
    b = _mean(disp, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC-minus-ROA spread z (de-trended leverage effect)
def f35ce_f35_capital_efficiency_returns_roicroaz_252d_base_v092_signal(roic, roa):
    b = _z(roic - roa, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA-minus-ROS spread z (de-trended turnover effect)
def f35ce_f35_capital_efficiency_returns_roarosz_252d_base_v093_signal(roa, ros):
    b = _z(roa - ros, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC-minus-ROS spread trend over a half-year
def f35ce_f35_capital_efficiency_returns_roicrostrend_126d_base_v094_signal(roic, ros):
    b = _slope(roic - ros, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of two years ROIC above hurdle (long value-creation persistence)
def f35ce_f35_capital_efficiency_returns_abovehurdle_504d_base_v095_signal(roic):
    above = (roic > HURDLE).astype(float)
    b = above.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of two years ROIC below zero (capital-sink persistence)
def f35ce_f35_capital_efficiency_returns_belowzero_504d_base_v096_signal(roic):
    below = (roic < 0).astype(float)
    b = below.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of two years ROS below zero (margin-loss persistence)
def f35ce_f35_capital_efficiency_returns_rosbelowzero_504d_base_v097_signal(ros):
    below = (ros < 0).astype(float)
    b = below.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS stability: inverse coefficient-of-variation over a half-year
def f35ce_f35_capital_efficiency_returns_rosstab_126d_base_v098_signal(ros):
    m = _mean(ros, 126)
    sd = _std(ros, 126)
    b = m / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite-returns stability (steady overall capital efficiency)
def f35ce_f35_capital_efficiency_returns_compstab_126d_base_v099_signal(roic, roa, ros):
    comp = (roic + roa + ros) / 3.0
    b = _mean(comp, 126) / _std(comp, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-turnover trend over 252d
def f35ce_f35_capital_efficiency_returns_aturntrend_252d_base_v100_signal(assetturnover):
    b = _slope(assetturnover, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-turnover trend over 252d (from raw inputs)
def f35ce_f35_capital_efficiency_returns_eturntrend_252d_base_v101_signal(revenue, equity):
    b = _slope(_f35_equityturn(revenue, equity), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DuPont decomposition residual z: reported ROA vs ROSxturn, de-trended
def f35ce_f35_capital_efficiency_returns_dupontz_252d_base_v102_signal(ros, assetturnover, roa):
    resid = roa - ros * assetturnover
    b = _z(resid, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread mean-reversion: current spread vs its own half-year average (over/undershoot)
def f35ce_f35_capital_efficiency_returns_spreadmom_126d_base_v103_signal(roic):
    sp = _f35_spread(roic)
    b = sp - _mean(sp, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC half-year-over-half-year change (semi-annual inflection)
def f35ce_f35_capital_efficiency_returns_roichoh_126d_base_v104_signal(roic):
    b = roic - roic.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS year-over-year change
def f35ce_f35_capital_efficiency_returns_rosyoy_252d_base_v105_signal(ros):
    b = ros - ros.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-light profitability: ROS times revenue-to-invcap (return per capital dollar)
def f35ce_f35_capital_efficiency_returns_roscapital_base_v106_signal(ros, revenue, invcap):
    ict = revenue / invcap.replace(0, np.nan)
    raw = ros * ict
    b = _z(raw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS percentile-rank vs its own 504d history
def f35ce_f35_capital_efficiency_returns_rosrank_504d_base_v107_signal(ros):
    b = ros.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite-returns percentile-rank vs 504d history
def f35ce_f35_capital_efficiency_returns_comprank_504d_base_v108_signal(roic, roa, ros):
    comp = (roic + roa + ros) / 3.0
    b = comp.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover-margin product momentum over a half-year
def f35ce_f35_capital_efficiency_returns_turnmargmom_126d_base_v109_signal(assetturnover, ros):
    prod = assetturnover * ros
    b = prod - prod.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financial leverage trend (rising/falling assets-to-equity)
def f35ce_f35_capital_efficiency_returns_levtrend_126d_base_v110_signal(assets, equity):
    lev = assets / equity.replace(0, np.nan)
    b = _slope(lev, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage-decomposition: ROIC minus (ROA x leverage) residual (DuPont leverage gap)
def f35ce_f35_capital_efficiency_returns_levdecomp_base_v111_signal(roic, roa, assets, equity):
    lev = assets / equity.replace(0, np.nan)
    b = _mean(roic - roa * lev, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invested-capital growth over a half-year (faster deployment pace)
def f35ce_f35_capital_efficiency_returns_invcapg_126d_base_v112_signal(invcap):
    b = invcap / invcap.shift(126).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity growth over a half-year
def f35ce_f35_capital_efficiency_returns_equityg_126d_base_v113_signal(equity):
    b = equity / equity.shift(126).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# incremental ROA: change in ROA relative to change in assets (marginal efficiency)
def f35ce_f35_capital_efficiency_returns_incroa_base_v114_signal(roa, assets):
    d_assets = (assets - assets.shift(63)) / assets.shift(63).replace(0, np.nan)
    d_roa = roa - roa.shift(63)
    b = d_roa / d_assets.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# returns-dispersion percentile-rank (unusual disagreement regime)
def f35ce_f35_capital_efficiency_returns_disprank_504d_base_v115_signal(roic, roa, ros):
    disp = _f35_disp3(roic, roa, ros)
    b = disp.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread sign-magnitude over a half-year (compressed value-creation level)
def f35ce_f35_capital_efficiency_returns_spreadsm_126d_base_v116_signal(roic):
    sp = _mean(_f35_spread(roic), 126)
    b = np.sign(sp) * (sp.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC-minus-ROS divergence rank (leverage+turnover combined disagreement)
def f35ce_f35_capital_efficiency_returns_roicrosrank_base_v117_signal(roic, ros):
    d = roic - ros
    b = d.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset turnover EMA vs slow EMA crossover (productivity momentum)
def f35ce_f35_capital_efficiency_returns_aturnxover_base_v118_signal(assetturnover):
    fast = assetturnover.ewm(span=21, min_periods=10).mean()
    slow = assetturnover.ewm(span=126, min_periods=42).mean()
    b = (fast - slow) / slow.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-turnover EMA vs slow EMA crossover
def f35ce_f35_capital_efficiency_returns_eturnxover_base_v119_signal(revenue, equity):
    et = _f35_equityturn(revenue, equity)
    fast = et.ewm(span=21, min_periods=10).mean()
    slow = et.ewm(span=126, min_periods=42).mean()
    b = (fast - slow) / slow.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-turnover growth over a half-year
def f35ce_f35_capital_efficiency_returns_aturng_126d_base_v120_signal(revenue, assets):
    at = _f35_assetturn(revenue, assets)
    b = at / at.shift(126).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-sink magnitude weighted by negative-spread depth
def f35ce_f35_capital_efficiency_returns_sinkdepth_252d_base_v121_signal(roic, invcap):
    neg_depth = (-_f35_spread(roic)).clip(lower=0).rolling(252, min_periods=126).mean()
    inv_g = (invcap / invcap.shift(252).replace(0, np.nan) - 1.0).clip(lower=0)
    b = neg_depth * inv_g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS drawdown from its own 252d peak (margin erosion)
def f35ce_f35_capital_efficiency_returns_rosdd_252d_base_v122_signal(ros):
    peak = ros.rolling(252, min_periods=126).max()
    b = ros - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC underwater duration: fraction of year >2pp below its 252d peak
def f35ce_f35_capital_efficiency_returns_roicunder_252d_base_v123_signal(roic):
    peak = roic.rolling(252, min_periods=126).max()
    under = (roic < peak - 0.02).astype(float)
    b = under.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA recovery off its own 252d trough (profitability rebound)
def f35ce_f35_capital_efficiency_returns_roarecov_252d_base_v124_signal(roa):
    trough = roa.rolling(252, min_periods=126).min()
    b = roa - trough
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite returns drawdown from 252d peak
def f35ce_f35_capital_efficiency_returns_compdd_252d_base_v125_signal(roic, roa, ros):
    comp = (roic + roa + ros) / 3.0
    peak = comp.rolling(252, min_periods=126).max()
    b = comp - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# economic-profit sign persistence: fraction of year spread positive (value regime)
def f35ce_f35_capital_efficiency_returns_epsign_252d_base_v126_signal(roic, invcap):
    ep = _f35_spread(roic) * invcap
    pos = (ep > 0).astype(float)
    b = pos.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC volatility over two years (long return instability)
def f35ce_f35_capital_efficiency_returns_roicvol_504d_base_v127_signal(roic):
    b = _std(roic, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS volatility over a half-year (margin instability)
def f35ce_f35_capital_efficiency_returns_rosvol_126d_base_v128_signal(ros):
    b = _std(ros, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DuPont lever balance over a half-year (turnover z minus margin z, slow)
def f35ce_f35_capital_efficiency_returns_dupontbal_126d_base_v129_signal(assetturnover, ros):
    at = _z(assetturnover, 126)
    ms = _z(ros, 126)
    b = (at - ms) / (at.abs() + ms.abs()).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-turnover minus invested-capital-turnover gap (financing-structure turnover)
def f35ce_f35_capital_efficiency_returns_eturnicgap_base_v130_signal(revenue, equity, invcap):
    et = _f35_equityturn(revenue, equity)
    ict = revenue / invcap.replace(0, np.nan)
    b = _mean(et - ict, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA consistency: fraction of half-years ROA rose vs prior half-year
def f35ce_f35_capital_efficiency_returns_roaconsist_252d_base_v131_signal(roa):
    up = (roa > roa.shift(126)).astype(float)
    b = up.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invested-capital intensity (invcap/assets) trend (capital concentration shift)
def f35ce_f35_capital_efficiency_returns_icintensity_126d_base_v132_signal(invcap, assets):
    intensity = invcap / assets.replace(0, np.nan)
    b = _slope(intensity, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread percentile-rank over two years vs one-year mean (long value regime)
def f35ce_f35_capital_efficiency_returns_spreadregime_base_v133_signal(roic):
    sp = _f35_spread(roic)
    b = _mean(sp, 252) - _mean(sp, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-turnover EMA displacement (productivity vs smooth trend)
def f35ce_f35_capital_efficiency_returns_eturndisp_base_v134_signal(revenue, equity):
    et = _f35_equityturn(revenue, equity)
    sm = et.ewm(span=63, min_periods=21).mean()
    b = et - sm
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA tanh-squashed momentum (bounded profitability change over a quarter)
def f35ce_f35_capital_efficiency_returns_roatanh_63d_base_v135_signal(roa):
    chg = roa - roa.shift(63)
    b = np.tanh(8.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return-on-equity proxy trend: slope of ros x equity-turnover
def f35ce_f35_capital_efficiency_returns_roeproxytrend_base_v136_signal(ros, revenue, equity):
    et = _f35_equityturn(revenue, equity)
    b = _slope(ros * et, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread-to-volatility over two years (long risk-adjusted value creation)
def f35ce_f35_capital_efficiency_returns_spreadsharpe_504d_base_v137_signal(roic):
    sp = _f35_spread(roic)
    vol = _std(roic, 252)
    b = _mean(sp, 252) / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# over-deployment over a half-year: invcap growth minus scaled ROIC change
def f35ce_f35_capital_efficiency_returns_overdeploy_126d_base_v138_signal(invcap, roic):
    inv_g = invcap / invcap.shift(126).replace(0, np.nan) - 1.0
    roic_chg = roic - roic.shift(126)
    b = inv_g - 5.0 * roic_chg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-turnover acceleration (productivity change-of-change)
def f35ce_f35_capital_efficiency_returns_aturnaccel_base_v139_signal(assetturnover):
    chg_now = assetturnover - assetturnover.shift(63)
    chg_prev = assetturnover.shift(63) - assetturnover.shift(126)
    b = chg_now - chg_prev
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# returns skew balance: upside lead vs downside lag among the three returns (signed)
def f35ce_f35_capital_efficiency_returns_retrange_base_v140_signal(roic, roa, ros):
    stacked = pd.concat([roic, roa, ros], axis=1)
    mid = stacked.median(axis=1)
    up = stacked.max(axis=1) - mid
    dn = mid - stacked.min(axis=1)
    bal = (up - dn) / (up + dn).replace(0, np.nan)
    b = _mean(bal, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# median-of-three returns z-scored vs own history (robust central efficiency, de-trended)
def f35ce_f35_capital_efficiency_returns_retmed_base_v141_signal(roic, roa, ros):
    med = pd.concat([roic, roa, ros], axis=1).median(axis=1)
    b = _z(med, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-vs-equity turnover ratio trend (leverage-implied turnover shift)
def f35ce_f35_capital_efficiency_returns_turnratiotrend_base_v142_signal(assetturnover, revenue, equity):
    et = _f35_equityturn(revenue, equity)
    ratio = assetturnover / et.replace(0, np.nan)
    b = _slope(ratio, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# above-hurdle streak weighted by spread depth (strong-value persistence)
def f35ce_f35_capital_efficiency_returns_hurdledepth_base_v143_signal(roic):
    sp = _f35_spread(roic)
    pos = (sp > 0).astype(float)
    grp = (pos == 0).cumsum()
    streak = pos.groupby(grp).cumsum()
    depth = sp.clip(lower=0)
    b = (streak / 126.0) * (1.0 + 4.0 * depth)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# falling-ROS streak: consecutive days ROS declines vs prior quarter, normalized
def f35ce_f35_capital_efficiency_returns_roalossstreak_base_v144_signal(ros):
    down = (ros < ros.shift(63)).astype(float)
    grp = (down == 0).cumsum()
    streak = down.groupby(grp).cumsum()
    b = streak / 126.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin lever isolated (slow): ROS z minus turnover z over a half-year
def f35ce_f35_capital_efficiency_returns_marginlever_126d_base_v145_signal(ros, assetturnover):
    b = _z(ros, 126) - _z(assetturnover, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-light return: ROIC times revenue-to-invcap turnover, ranked
def f35ce_f35_capital_efficiency_returns_roicicturn_base_v146_signal(roic, revenue, invcap):
    ict = revenue / invcap.replace(0, np.nan)
    raw = roic * ict
    b = raw.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread regime shift over short vs medium horizon
def f35ce_f35_capital_efficiency_returns_spreadshift63_base_v147_signal(roic):
    sp = _f35_spread(roic)
    b = _mean(sp, 63) - _mean(sp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return amplification: (ROIC x leverage) minus ROA over a half-year
def f35ce_f35_capital_efficiency_returns_amplify_126d_base_v148_signal(roic, roa, assets, equity):
    lev = assets / equity.replace(0, np.nan)
    b = _mean(roic * lev - roa, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# returns-dispersion momentum (change in disagreement over a quarter)
def f35ce_f35_capital_efficiency_returns_dispmom_63d_base_v149_signal(roic, roa, ros):
    disp = _f35_disp3(roic, roa, ros)
    b = disp - disp.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# all-three-positive regime: fraction of year roic, roa, ros all above zero
def f35ce_f35_capital_efficiency_returns_allpos_252d_base_v150_signal(roic, roa, ros):
    allpos = ((roic > 0) & (roa > 0) & (ros > 0)).astype(float)
    b = allpos.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f35ce_f35_capital_efficiency_returns_roiclvl_126d_base_v076_signal,
    f35ce_f35_capital_efficiency_returns_roalvl_126d_base_v077_signal,
    f35ce_f35_capital_efficiency_returns_roslvl_126d_base_v078_signal,
    f35ce_f35_capital_efficiency_returns_spreadsign_126d_base_v079_signal,
    f35ce_f35_capital_efficiency_returns_roicz_504d_base_v080_signal,
    f35ce_f35_capital_efficiency_returns_roaz_504d_base_v081_signal,
    f35ce_f35_capital_efficiency_returns_rosz_504d_base_v082_signal,
    f35ce_f35_capital_efficiency_returns_roictrend_252d_base_v083_signal,
    f35ce_f35_capital_efficiency_returns_roatrend_252d_base_v084_signal,
    f35ce_f35_capital_efficiency_returns_rostrend_252d_base_v085_signal,
    f35ce_f35_capital_efficiency_returns_aturn_126d_base_v086_signal,
    f35ce_f35_capital_efficiency_returns_aturnrank_504d_base_v087_signal,
    f35ce_f35_capital_efficiency_returns_eturn_126d_base_v088_signal,
    f35ce_f35_capital_efficiency_returns_icturnz_252d_base_v089_signal,
    f35ce_f35_capital_efficiency_returns_capsink_126d_base_v090_signal,
    f35ce_f35_capital_efficiency_returns_retdispsm_63d_base_v091_signal,
    f35ce_f35_capital_efficiency_returns_roicroaz_252d_base_v092_signal,
    f35ce_f35_capital_efficiency_returns_roarosz_252d_base_v093_signal,
    f35ce_f35_capital_efficiency_returns_roicrostrend_126d_base_v094_signal,
    f35ce_f35_capital_efficiency_returns_abovehurdle_504d_base_v095_signal,
    f35ce_f35_capital_efficiency_returns_belowzero_504d_base_v096_signal,
    f35ce_f35_capital_efficiency_returns_rosbelowzero_504d_base_v097_signal,
    f35ce_f35_capital_efficiency_returns_rosstab_126d_base_v098_signal,
    f35ce_f35_capital_efficiency_returns_compstab_126d_base_v099_signal,
    f35ce_f35_capital_efficiency_returns_aturntrend_252d_base_v100_signal,
    f35ce_f35_capital_efficiency_returns_eturntrend_252d_base_v101_signal,
    f35ce_f35_capital_efficiency_returns_dupontz_252d_base_v102_signal,
    f35ce_f35_capital_efficiency_returns_spreadmom_126d_base_v103_signal,
    f35ce_f35_capital_efficiency_returns_roichoh_126d_base_v104_signal,
    f35ce_f35_capital_efficiency_returns_rosyoy_252d_base_v105_signal,
    f35ce_f35_capital_efficiency_returns_roscapital_base_v106_signal,
    f35ce_f35_capital_efficiency_returns_rosrank_504d_base_v107_signal,
    f35ce_f35_capital_efficiency_returns_comprank_504d_base_v108_signal,
    f35ce_f35_capital_efficiency_returns_turnmargmom_126d_base_v109_signal,
    f35ce_f35_capital_efficiency_returns_levtrend_126d_base_v110_signal,
    f35ce_f35_capital_efficiency_returns_levdecomp_base_v111_signal,
    f35ce_f35_capital_efficiency_returns_invcapg_126d_base_v112_signal,
    f35ce_f35_capital_efficiency_returns_equityg_126d_base_v113_signal,
    f35ce_f35_capital_efficiency_returns_incroa_base_v114_signal,
    f35ce_f35_capital_efficiency_returns_disprank_504d_base_v115_signal,
    f35ce_f35_capital_efficiency_returns_spreadsm_126d_base_v116_signal,
    f35ce_f35_capital_efficiency_returns_roicrosrank_base_v117_signal,
    f35ce_f35_capital_efficiency_returns_aturnxover_base_v118_signal,
    f35ce_f35_capital_efficiency_returns_eturnxover_base_v119_signal,
    f35ce_f35_capital_efficiency_returns_aturng_126d_base_v120_signal,
    f35ce_f35_capital_efficiency_returns_sinkdepth_252d_base_v121_signal,
    f35ce_f35_capital_efficiency_returns_rosdd_252d_base_v122_signal,
    f35ce_f35_capital_efficiency_returns_roicunder_252d_base_v123_signal,
    f35ce_f35_capital_efficiency_returns_roarecov_252d_base_v124_signal,
    f35ce_f35_capital_efficiency_returns_compdd_252d_base_v125_signal,
    f35ce_f35_capital_efficiency_returns_epsign_252d_base_v126_signal,
    f35ce_f35_capital_efficiency_returns_roicvol_504d_base_v127_signal,
    f35ce_f35_capital_efficiency_returns_rosvol_126d_base_v128_signal,
    f35ce_f35_capital_efficiency_returns_dupontbal_126d_base_v129_signal,
    f35ce_f35_capital_efficiency_returns_eturnicgap_base_v130_signal,
    f35ce_f35_capital_efficiency_returns_roaconsist_252d_base_v131_signal,
    f35ce_f35_capital_efficiency_returns_icintensity_126d_base_v132_signal,
    f35ce_f35_capital_efficiency_returns_spreadregime_base_v133_signal,
    f35ce_f35_capital_efficiency_returns_eturndisp_base_v134_signal,
    f35ce_f35_capital_efficiency_returns_roatanh_63d_base_v135_signal,
    f35ce_f35_capital_efficiency_returns_roeproxytrend_base_v136_signal,
    f35ce_f35_capital_efficiency_returns_spreadsharpe_504d_base_v137_signal,
    f35ce_f35_capital_efficiency_returns_overdeploy_126d_base_v138_signal,
    f35ce_f35_capital_efficiency_returns_aturnaccel_base_v139_signal,
    f35ce_f35_capital_efficiency_returns_retrange_base_v140_signal,
    f35ce_f35_capital_efficiency_returns_retmed_base_v141_signal,
    f35ce_f35_capital_efficiency_returns_turnratiotrend_base_v142_signal,
    f35ce_f35_capital_efficiency_returns_hurdledepth_base_v143_signal,
    f35ce_f35_capital_efficiency_returns_roalossstreak_base_v144_signal,
    f35ce_f35_capital_efficiency_returns_marginlever_126d_base_v145_signal,
    f35ce_f35_capital_efficiency_returns_roicicturn_base_v146_signal,
    f35ce_f35_capital_efficiency_returns_spreadshift63_base_v147_signal,
    f35ce_f35_capital_efficiency_returns_amplify_126d_base_v148_signal,
    f35ce_f35_capital_efficiency_returns_dispmom_63d_base_v149_signal,
    f35ce_f35_capital_efficiency_returns_allpos_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F35_CAPITAL_EFFICIENCY_RETURNS_REGISTRY_076_150 = REGISTRY


ALLOW = {
    "open", "high", "low", "close", "closeadj", "volume",
    "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc", "opex",
    "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc",
    "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff",
    "ncfi", "ncfcommon", "ncfdebt", "ncfbus", "capex", "depamor", "sharesbas",
    "shareswa", "shareswadil", "assets", "assetsc", "tangibles", "intangibles",
    "ppnenet", "investments", "inventory", "receivables", "payables", "equity",
    "retearn", "workingcapital", "debt", "debtc", "debtnc", "liabilities",
    "liabilitiesc", "cashneq", "currentratio", "roic", "roe", "roa", "ros",
    "assetturnover", "invcap", "intexp", "taxexp", "ebt", "sps", "bvps", "de",
    "ncfdiv", "dps", "divyield", "payoutratio", "prefdivis",
    "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
    "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal",
    "fndholders", "undholders", "prfholders", "dbtholders", "putholders",
    "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue", "dbtvalue",
}


def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
    g = np.random.default_rng(seed)
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.6
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    roic = _fund(5, base=0.25, drift=-0.005, vol=0.16, allow_neg=True).rename("roic")
    roa = _fund(20, base=0.22, drift=-0.005, vol=0.16, allow_neg=True).rename("roa")
    ros = _fund(27, base=0.26, drift=-0.005, vol=0.16, allow_neg=True).rename("ros")
    assetturnover = (_fund(11, base=0.8, drift=0.01, vol=0.08).clip(lower=0.05)
                     ).rename("assetturnover")
    invcap = _fund(12, base=2e8, drift=0.03, vol=0.07).rename("invcap")
    equity = _fund(13, base=1.5e8, drift=0.025, vol=0.06).rename("equity")
    revenue = _fund(14, base=3e8, drift=0.03, vol=0.07).rename("revenue")
    assets = _fund(15, base=4e8, drift=0.025, vol=0.06).rename("assets")

    cols = {
        "roic": roic, "roa": roa, "ros": ros, "assetturnover": assetturnover,
        "invcap": invcap, "equity": equity, "revenue": revenue, "assets": assets,
    }

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "BAD INPUTS %s: %s" % (name, meta["inputs"])
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

    assert n_features == 75, n_features
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

    print("OK f35_capital_efficiency_returns_base_076_150_claude: %d features pass" % n_features)
