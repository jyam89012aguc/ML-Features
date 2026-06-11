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
    # least-squares slope of s over a trailing window (per-step)
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
    # ROIC minus hurdle (economic-profit spread)
    return roic - HURDLE


def _f35_assetturn(revenue, assets):
    # revenue / assets (asset turnover from raw inputs)
    return revenue / assets.replace(0, np.nan)


def _f35_equityturn(revenue, equity):
    # revenue / equity (equity turnover)
    return revenue / equity.replace(0, np.nan)


def _f35_disp3(a, b, c):
    # cross-sectional (per-row) dispersion of three returns series
    return pd.concat([a, b, c], axis=1).std(axis=1)


def _f35_capsink(roic, invcap, w):
    # persistent negative ROIC AND rising invested capital
    neg = (roic < 0).astype(float).rolling(w, min_periods=max(1, w // 2)).mean()
    inv_g = invcap / invcap.shift(w).replace(0, np.nan) - 1.0
    return neg * inv_g.clip(lower=0)


# ============================================================
# ROIC level smoothed over a quarter (durable return on capital)
def f35ce_f35_capital_efficiency_returns_roiclvl_63d_base_v001_signal(roic):
    b = _mean(roic, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA level smoothed over a quarter
def f35ce_f35_capital_efficiency_returns_roalvl_63d_base_v002_signal(roa):
    b = _mean(roa, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS level smoothed over a quarter
def f35ce_f35_capital_efficiency_returns_roslvl_63d_base_v003_signal(ros):
    b = _mean(ros, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC-hurdle spread normalized by trailing return dispersion (risk-scaled spread)
def f35ce_f35_capital_efficiency_returns_spread_63d_base_v004_signal(roic):
    sp = _f35_spread(roic)
    sd = _std(roic, 63)
    b = sp / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC z-scored vs its own 252d history (de-trended return level)
def f35ce_f35_capital_efficiency_returns_roicz_252d_base_v005_signal(roic):
    b = _z(roic, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA z-scored vs its own 252d history
def f35ce_f35_capital_efficiency_returns_roaz_252d_base_v006_signal(roa):
    b = _z(roa, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS z-scored vs its own 252d history
def f35ce_f35_capital_efficiency_returns_rosz_252d_base_v007_signal(ros):
    b = _z(ros, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC trend: least-squares slope over 126d (improving return on capital)
def f35ce_f35_capital_efficiency_returns_roictrend_126d_base_v008_signal(roic):
    b = _slope(roic, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA trend over 126d
def f35ce_f35_capital_efficiency_returns_roatrend_126d_base_v009_signal(roa):
    b = _slope(roa, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS trend over 126d
def f35ce_f35_capital_efficiency_returns_rostrend_126d_base_v010_signal(ros):
    b = _slope(ros, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset turnover from raw revenue/assets (capital productivity)
def f35ce_f35_capital_efficiency_returns_aturn_63d_base_v011_signal(revenue, assets):
    b = _mean(_f35_assetturn(revenue, assets), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reported assetturnover column, smoothed over a quarter
def f35ce_f35_capital_efficiency_returns_aturnrep_63d_base_v012_signal(assetturnover):
    b = _mean(assetturnover, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity turnover (revenue/equity), smoothed
def f35ce_f35_capital_efficiency_returns_eturn_63d_base_v013_signal(revenue, equity):
    b = _mean(_f35_equityturn(revenue, equity), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invested-capital turnover (revenue/invcap)
def f35ce_f35_capital_efficiency_returns_icturn_63d_base_v014_signal(revenue, invcap):
    b = _mean(revenue / invcap.replace(0, np.nan), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-sink flag: persistent ROIC<0 AND rising invested capital over a year
def f35ce_f35_capital_efficiency_returns_capsink_252d_base_v015_signal(roic, invcap):
    b = _f35_capsink(roic, invcap, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# returns dispersion across roic/roa/ros (how aligned the three returns are)
def f35ce_f35_capital_efficiency_returns_retdisp_base_v016_signal(roic, roa, ros):
    b = _f35_disp3(roic, roa, ros)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC minus ROA gap (capital-structure leverage on returns)
def f35ce_f35_capital_efficiency_returns_roicroa_base_v017_signal(roic, roa):
    b = _mean(roic - roa, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA minus ROS gap (turnover contribution: DuPont decomposition residue)
def f35ce_f35_capital_efficiency_returns_roaros_base_v018_signal(roa, ros):
    b = _mean(roa - ros, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC minus ROS gap (full leverage-plus-turnover effect)
def f35ce_f35_capital_efficiency_returns_roicros_base_v019_signal(roic, ros):
    b = _mean(roic - ros, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC fraction of the year above the hurdle (value-creation persistence)
def f35ce_f35_capital_efficiency_returns_abovehurdle_252d_base_v020_signal(roic):
    above = (roic > HURDLE).astype(float)
    b = above.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of the year with positive ROA (profitability persistence)
def f35ce_f35_capital_efficiency_returns_posroa_252d_base_v021_signal(roa):
    pos = (roa > 0).astype(float)
    b = pos.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of the year with positive ROS
def f35ce_f35_capital_efficiency_returns_posros_252d_base_v022_signal(ros):
    pos = (ros > 0).astype(float)
    b = pos.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC stability: inverse coefficient-of-variation (high return AND steady)
def f35ce_f35_capital_efficiency_returns_roicstab_126d_base_v023_signal(roic):
    m = _mean(roic, 126)
    sd = _std(roic, 126)
    b = m / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA stability: inverse coefficient-of-variation
def f35ce_f35_capital_efficiency_returns_roastab_126d_base_v024_signal(roa):
    m = _mean(roa, 126)
    sd = _std(roa, 126)
    b = m / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-turnover trend (rising capital productivity)
def f35ce_f35_capital_efficiency_returns_aturntrend_126d_base_v025_signal(assetturnover):
    b = _slope(assetturnover, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-turnover trend from raw revenue/equity
def f35ce_f35_capital_efficiency_returns_eturntrend_126d_base_v026_signal(revenue, equity):
    b = _slope(_f35_equityturn(revenue, equity), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DuPont reconstruction error sign-rate: how often reported ROA exceeds ROSxturn
def f35ce_f35_capital_efficiency_returns_dupontresid_base_v027_signal(ros, assetturnover, roa):
    recon = ros * assetturnover
    beat = (roa > recon).astype(float)
    b = beat.rolling(126, min_periods=63).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread momentum: change in ROIC-hurdle spread over a quarter
def f35ce_f35_capital_efficiency_returns_spreadmom_63d_base_v028_signal(roic):
    sp = _f35_spread(roic)
    b = sp - sp.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC year-over-year change (annual return inflection)
def f35ce_f35_capital_efficiency_returns_roicyoy_252d_base_v029_signal(roic):
    b = roic - roic.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA year-over-year change
def f35ce_f35_capital_efficiency_returns_roayoy_252d_base_v030_signal(roa):
    b = roa - roa.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-light profitability rank: ROS divided by invcap-intensity, percentile-ranked
def f35ce_f35_capital_efficiency_returns_rosinvcap_base_v031_signal(ros, revenue, invcap):
    intensity = invcap / revenue.replace(0, np.nan)
    ratio = ros / intensity.replace(0, np.nan)
    b = ratio.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC percentile-rank vs its own 504d history (where current return sits)
def f35ce_f35_capital_efficiency_returns_roicrank_504d_base_v032_signal(roic):
    b = roic.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA percentile-rank vs its own 504d history
def f35ce_f35_capital_efficiency_returns_roarank_504d_base_v033_signal(roa):
    b = roa.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-weighted productivity momentum: change in (turnover x ROS) over a quarter
def f35ce_f35_capital_efficiency_returns_turnmargin_base_v034_signal(assetturnover, ros):
    prod = assetturnover * ros
    b = prod - prod.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financial-leverage proxy: assets / equity (return amplification)
def f35ce_f35_capital_efficiency_returns_leverage_63d_base_v035_signal(assets, equity):
    b = _mean(assets / equity.replace(0, np.nan), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage-helps-returns regime: fraction of year ROIC exceeds ROA while levered
def f35ce_f35_capital_efficiency_returns_levquality_base_v036_signal(roic, roa, assets, equity):
    lev = assets / equity.replace(0, np.nan)
    helps = ((roic > roa) & (lev > 1.0)).astype(float)
    b = helps.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invested capital growth (capital deployment pace)
def f35ce_f35_capital_efficiency_returns_invcapg_252d_base_v037_signal(invcap):
    b = invcap / invcap.shift(252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity growth (book-value build)
def f35ce_f35_capital_efficiency_returns_equityg_252d_base_v038_signal(equity):
    b = equity / equity.shift(252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# incremental ROIC: change in operating return relative to change in capital
def f35ce_f35_capital_efficiency_returns_incroic_base_v039_signal(roic, invcap):
    d_inv = (invcap - invcap.shift(63)) / invcap.shift(63).replace(0, np.nan)
    d_roic = roic - roic.shift(63)
    b = d_roic / d_inv.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# returns-dispersion trend (are the three returns converging or diverging)
def f35ce_f35_capital_efficiency_returns_disptrend_126d_base_v040_signal(roic, roa, ros):
    disp = _f35_disp3(roic, roa, ros)
    b = _slope(disp, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread sign-magnitude: signed sqrt of ROIC-hurdle spread (compresses extremes)
def f35ce_f35_capital_efficiency_returns_spreadsm_63d_base_v041_signal(roic):
    sp = _mean(_f35_spread(roic), 63)
    b = np.sign(sp) * (sp.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROS minus ROA divergence rank (margin vs asset-efficiency disagreement)
def f35ce_f35_capital_efficiency_returns_marginassetrank_base_v042_signal(ros, roa):
    d = ros - roa
    b = d.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset turnover z vs own history (de-trended capital productivity)
def f35ce_f35_capital_efficiency_returns_aturnz_252d_base_v043_signal(assetturnover):
    b = _z(assetturnover, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-turnover z (de-trended)
def f35ce_f35_capital_efficiency_returns_eturnz_252d_base_v044_signal(revenue, equity):
    et = _f35_equityturn(revenue, equity)
    b = _z(et, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue per unit of assets growth (productivity improvement)
def f35ce_f35_capital_efficiency_returns_aturng_252d_base_v045_signal(revenue, assets):
    at = _f35_assetturn(revenue, assets)
    b = at / at.shift(252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-sink depth over two years (long-horizon value destruction)
def f35ce_f35_capital_efficiency_returns_capsink_504d_base_v046_signal(roic, invcap):
    b = _f35_capsink(roic, invcap, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC drawdown from its own 252d peak (return erosion)
def f35ce_f35_capital_efficiency_returns_roicdd_252d_base_v047_signal(roic):
    peak = roic.rolling(252, min_periods=126).max()
    b = roic - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA underwater duration: fraction of last year spent >2pp below its 252d peak
def f35ce_f35_capital_efficiency_returns_roadd_252d_base_v048_signal(roa):
    peak = roa.rolling(252, min_periods=126).max()
    underwater = (roa < peak - 0.02).astype(float)
    b = underwater.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC recovery off its own 252d trough (return rebound)
def f35ce_f35_capital_efficiency_returns_roicrecov_252d_base_v049_signal(roic):
    trough = roic.rolling(252, min_periods=126).min()
    b = roic - trough
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite returns level: equal-weight average of roic/roa/ros, smoothed
def f35ce_f35_capital_efficiency_returns_retcomp_63d_base_v050_signal(roic, roa, ros):
    comp = (roic + roa + ros) / 3.0
    b = _mean(comp, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite returns trend
def f35ce_f35_capital_efficiency_returns_retcomptrend_126d_base_v051_signal(roic, roa, ros):
    comp = (roic + roa + ros) / 3.0
    b = _slope(comp, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# economic-profit growth: YoY change in (spread x invested capital), log-scaled
def f35ce_f35_capital_efficiency_returns_econprofit_base_v052_signal(roic, invcap):
    sp = _f35_spread(roic)
    ep = sp * invcap
    b = np.sign(ep) * np.log1p(ep.abs()) - (
        np.sign(ep.shift(252)) * np.log1p(ep.shift(252).abs()))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA volatility (return instability) over a half-year
def f35ce_f35_capital_efficiency_returns_roavol_126d_base_v053_signal(roa):
    b = _std(roa, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC volatility over a half-year
def f35ce_f35_capital_efficiency_returns_roicvol_126d_base_v054_signal(roic):
    b = _std(roic, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover-vs-margin balance: which DuPont lever dominates (signed ratio)
def f35ce_f35_capital_efficiency_returns_dupontbal_base_v055_signal(assetturnover, ros):
    at = _z(assetturnover, 252)
    ms = _z(ros, 252)
    b = (at - ms) / (at.abs() + ms.abs()).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity turnover minus asset turnover (leverage-implied turnover gap)
def f35ce_f35_capital_efficiency_returns_turngap_base_v056_signal(revenue, equity, assets):
    et = _f35_equityturn(revenue, equity)
    at = revenue / assets.replace(0, np.nan)
    b = _mean(et - at, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC consistency: fraction of quarters where ROIC rose vs prior quarter
def f35ce_f35_capital_efficiency_returns_roicconsist_252d_base_v057_signal(roic):
    up = (roic > roic.shift(63)).astype(float)
    b = up.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# invested-capital vs asset turnover gap (how much capital sits outside operating assets)
def f35ce_f35_capital_efficiency_returns_icefficiency_base_v058_signal(revenue, invcap, assets):
    ict = revenue / invcap.replace(0, np.nan)
    at = revenue / assets.replace(0, np.nan)
    b = _mean(ict - at, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# risk-scaled spread regime: percentile-rank of spread-per-unit-volatility
def f35ce_f35_capital_efficiency_returns_spreadrank_504d_base_v059_signal(roic):
    sp = _f35_spread(roic)
    vol = _std(roic, 63)
    rs = sp / vol.replace(0, np.nan)
    b = rs.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset turnover EMA displacement (productivity vs its own smooth trend)
def f35ce_f35_capital_efficiency_returns_aturndisp_base_v060_signal(assetturnover):
    sm = assetturnover.ewm(span=63, min_periods=21).mean()
    b = assetturnover - sm
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC tanh-squashed acceleration (bounded change-of-change over a quarter)
def f35ce_f35_capital_efficiency_returns_roictanh_63d_base_v061_signal(roic):
    chg_now = roic - roic.shift(63)
    chg_prev = roic.shift(63) - roic.shift(126)
    b = np.tanh(8.0 * (chg_now - chg_prev))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return-on-equity proxy (ros x equity-turnover) z-scored vs own history
def f35ce_f35_capital_efficiency_returns_roeproxy_base_v062_signal(ros, revenue, equity):
    et = _f35_equityturn(revenue, equity)
    b = _z(ros * et, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread-to-volatility: economic-profit spread per unit of ROIC volatility
def f35ce_f35_capital_efficiency_returns_spreadsharpe_base_v063_signal(roic):
    sp = _f35_spread(roic)
    vol = _std(roic, 126)
    b = _mean(sp, 126) / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital deployment vs return: invcap growth minus ROIC change (over-deployment)
def f35ce_f35_capital_efficiency_returns_overdeploy_base_v064_signal(invcap, roic):
    inv_g = invcap / invcap.shift(252).replace(0, np.nan) - 1.0
    roic_chg = roic - roic.shift(252)
    b = inv_g - 5.0 * roic_chg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-to-equity acceleration (equity productivity inflection)
def f35ce_f35_capital_efficiency_returns_eturnaccel_base_v065_signal(revenue, equity):
    et = _f35_equityturn(revenue, equity)
    chg_now = et - et.shift(63)
    chg_prev = et.shift(63) - et.shift(126)
    b = chg_now - chg_prev
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# min of the three returns (worst-case capital efficiency floor), smoothed
def f35ce_f35_capital_efficiency_returns_retmin_base_v066_signal(roic, roa, ros):
    mn = pd.concat([roic, roa, ros], axis=1).min(axis=1)
    b = _mean(mn, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# best-minus-median return spread (how far the top return leads the pack)
def f35ce_f35_capital_efficiency_returns_retmax_base_v067_signal(roic, roa, ros):
    stacked = pd.concat([roic, roa, ros], axis=1)
    lead = stacked.max(axis=1) - stacked.median(axis=1)
    b = _mean(lead, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset turnover relative to equity turnover (capital-structure turnover ratio)
def f35ce_f35_capital_efficiency_returns_turnratio_base_v068_signal(assetturnover, revenue, equity):
    et = _f35_equityturn(revenue, equity)
    b = _mean(assetturnover / et.replace(0, np.nan), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROIC above hurdle streak: consecutive days spread positive, normalized
def f35ce_f35_capital_efficiency_returns_hurdlestreak_base_v069_signal(roic):
    pos = (roic > HURDLE).astype(float)
    grp = (pos == 0).cumsum()
    streak = pos.groupby(grp).cumsum()
    b = streak / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# falling-ROIC streak: consecutive days ROIC declines vs the prior quarter, normalized
def f35ce_f35_capital_efficiency_returns_sinkstreak_base_v070_signal(roic):
    down = (roic < roic.shift(63)).astype(float)
    grp = (down == 0).cumsum()
    streak = down.groupby(grp).cumsum()
    b = streak / 126.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DuPont margin lever isolated: ROS z minus turnover z (margin-driven returns)
def f35ce_f35_capital_efficiency_returns_marginlever_base_v071_signal(ros, assetturnover):
    b = _z(ros, 252) - _z(assetturnover, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-light return rank: ROA x invcap-turnover, percentile-ranked vs own history
def f35ce_f35_capital_efficiency_returns_roaicturn_base_v072_signal(roa, revenue, invcap):
    ict = revenue / invcap.replace(0, np.nan)
    raw = roa * ict
    b = raw.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread half-year mean minus two-year mean (return regime shift)
def f35ce_f35_capital_efficiency_returns_spreadshift_base_v073_signal(roic):
    sp = _f35_spread(roic)
    b = _mean(sp, 126) - _mean(sp, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-vs-asset return amplification: ROIC scaled by leverage minus ROA
def f35ce_f35_capital_efficiency_returns_amplify_base_v074_signal(roic, roa, assets, equity):
    lev = assets / equity.replace(0, np.nan)
    b = _mean(roic * lev - roa, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# returns-dispersion z (unusual disagreement among roic/roa/ros)
def f35ce_f35_capital_efficiency_returns_dispz_252d_base_v075_signal(roic, roa, ros):
    disp = _f35_disp3(roic, roa, ros)
    b = _z(disp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f35ce_f35_capital_efficiency_returns_roiclvl_63d_base_v001_signal,
    f35ce_f35_capital_efficiency_returns_roalvl_63d_base_v002_signal,
    f35ce_f35_capital_efficiency_returns_roslvl_63d_base_v003_signal,
    f35ce_f35_capital_efficiency_returns_spread_63d_base_v004_signal,
    f35ce_f35_capital_efficiency_returns_roicz_252d_base_v005_signal,
    f35ce_f35_capital_efficiency_returns_roaz_252d_base_v006_signal,
    f35ce_f35_capital_efficiency_returns_rosz_252d_base_v007_signal,
    f35ce_f35_capital_efficiency_returns_roictrend_126d_base_v008_signal,
    f35ce_f35_capital_efficiency_returns_roatrend_126d_base_v009_signal,
    f35ce_f35_capital_efficiency_returns_rostrend_126d_base_v010_signal,
    f35ce_f35_capital_efficiency_returns_aturn_63d_base_v011_signal,
    f35ce_f35_capital_efficiency_returns_aturnrep_63d_base_v012_signal,
    f35ce_f35_capital_efficiency_returns_eturn_63d_base_v013_signal,
    f35ce_f35_capital_efficiency_returns_icturn_63d_base_v014_signal,
    f35ce_f35_capital_efficiency_returns_capsink_252d_base_v015_signal,
    f35ce_f35_capital_efficiency_returns_retdisp_base_v016_signal,
    f35ce_f35_capital_efficiency_returns_roicroa_base_v017_signal,
    f35ce_f35_capital_efficiency_returns_roaros_base_v018_signal,
    f35ce_f35_capital_efficiency_returns_roicros_base_v019_signal,
    f35ce_f35_capital_efficiency_returns_abovehurdle_252d_base_v020_signal,
    f35ce_f35_capital_efficiency_returns_posroa_252d_base_v021_signal,
    f35ce_f35_capital_efficiency_returns_posros_252d_base_v022_signal,
    f35ce_f35_capital_efficiency_returns_roicstab_126d_base_v023_signal,
    f35ce_f35_capital_efficiency_returns_roastab_126d_base_v024_signal,
    f35ce_f35_capital_efficiency_returns_aturntrend_126d_base_v025_signal,
    f35ce_f35_capital_efficiency_returns_eturntrend_126d_base_v026_signal,
    f35ce_f35_capital_efficiency_returns_dupontresid_base_v027_signal,
    f35ce_f35_capital_efficiency_returns_spreadmom_63d_base_v028_signal,
    f35ce_f35_capital_efficiency_returns_roicyoy_252d_base_v029_signal,
    f35ce_f35_capital_efficiency_returns_roayoy_252d_base_v030_signal,
    f35ce_f35_capital_efficiency_returns_rosinvcap_base_v031_signal,
    f35ce_f35_capital_efficiency_returns_roicrank_504d_base_v032_signal,
    f35ce_f35_capital_efficiency_returns_roarank_504d_base_v033_signal,
    f35ce_f35_capital_efficiency_returns_turnmargin_base_v034_signal,
    f35ce_f35_capital_efficiency_returns_leverage_63d_base_v035_signal,
    f35ce_f35_capital_efficiency_returns_levquality_base_v036_signal,
    f35ce_f35_capital_efficiency_returns_invcapg_252d_base_v037_signal,
    f35ce_f35_capital_efficiency_returns_equityg_252d_base_v038_signal,
    f35ce_f35_capital_efficiency_returns_incroic_base_v039_signal,
    f35ce_f35_capital_efficiency_returns_disptrend_126d_base_v040_signal,
    f35ce_f35_capital_efficiency_returns_spreadsm_63d_base_v041_signal,
    f35ce_f35_capital_efficiency_returns_marginassetrank_base_v042_signal,
    f35ce_f35_capital_efficiency_returns_aturnz_252d_base_v043_signal,
    f35ce_f35_capital_efficiency_returns_eturnz_252d_base_v044_signal,
    f35ce_f35_capital_efficiency_returns_aturng_252d_base_v045_signal,
    f35ce_f35_capital_efficiency_returns_capsink_504d_base_v046_signal,
    f35ce_f35_capital_efficiency_returns_roicdd_252d_base_v047_signal,
    f35ce_f35_capital_efficiency_returns_roadd_252d_base_v048_signal,
    f35ce_f35_capital_efficiency_returns_roicrecov_252d_base_v049_signal,
    f35ce_f35_capital_efficiency_returns_retcomp_63d_base_v050_signal,
    f35ce_f35_capital_efficiency_returns_retcomptrend_126d_base_v051_signal,
    f35ce_f35_capital_efficiency_returns_econprofit_base_v052_signal,
    f35ce_f35_capital_efficiency_returns_roavol_126d_base_v053_signal,
    f35ce_f35_capital_efficiency_returns_roicvol_126d_base_v054_signal,
    f35ce_f35_capital_efficiency_returns_dupontbal_base_v055_signal,
    f35ce_f35_capital_efficiency_returns_turngap_base_v056_signal,
    f35ce_f35_capital_efficiency_returns_roicconsist_252d_base_v057_signal,
    f35ce_f35_capital_efficiency_returns_icefficiency_base_v058_signal,
    f35ce_f35_capital_efficiency_returns_spreadrank_504d_base_v059_signal,
    f35ce_f35_capital_efficiency_returns_aturndisp_base_v060_signal,
    f35ce_f35_capital_efficiency_returns_roictanh_63d_base_v061_signal,
    f35ce_f35_capital_efficiency_returns_roeproxy_base_v062_signal,
    f35ce_f35_capital_efficiency_returns_spreadsharpe_base_v063_signal,
    f35ce_f35_capital_efficiency_returns_overdeploy_base_v064_signal,
    f35ce_f35_capital_efficiency_returns_eturnaccel_base_v065_signal,
    f35ce_f35_capital_efficiency_returns_retmin_base_v066_signal,
    f35ce_f35_capital_efficiency_returns_retmax_base_v067_signal,
    f35ce_f35_capital_efficiency_returns_turnratio_base_v068_signal,
    f35ce_f35_capital_efficiency_returns_hurdlestreak_base_v069_signal,
    f35ce_f35_capital_efficiency_returns_sinkstreak_base_v070_signal,
    f35ce_f35_capital_efficiency_returns_marginlever_base_v071_signal,
    f35ce_f35_capital_efficiency_returns_roaicturn_base_v072_signal,
    f35ce_f35_capital_efficiency_returns_spreadshift_base_v073_signal,
    f35ce_f35_capital_efficiency_returns_amplify_base_v074_signal,
    f35ce_f35_capital_efficiency_returns_dispz_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F35_CAPITAL_EFFICIENCY_RETURNS_REGISTRY_001_075 = REGISTRY


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

    print("OK f35_capital_efficiency_returns_base_001_075_claude: %d features pass" % n_features)
