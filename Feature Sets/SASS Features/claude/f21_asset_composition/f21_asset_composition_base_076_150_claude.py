import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_FIVEYEAR = 1260
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


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


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


def _ewm(s, span):
    return s.ewm(span=span, min_periods=max(2, span // 2)).mean()


# ===== folder domain primitives (asset composition ratios) =====
def _f21_tangible_share(tangibles, assets):
    return tangibles / assets.replace(0, np.nan)


def _f21_intang_share(intangibles, assets):
    return intangibles / assets.replace(0, np.nan)


def _f21_capint(ppnenet, assets):
    return ppnenet / assets.replace(0, np.nan)


def _f21_invshare(inventory, assets):
    return inventory / assets.replace(0, np.nan)


def _f21_investshare(investments, assets):
    return investments / assets.replace(0, np.nan)


def _f21_goodwill_proxy(intangibles, ppnenet):
    return intangibles / (intangibles + ppnenet).replace(0, np.nan)


def _f21_assetlight(ppnenet, inventory, assets):
    return 1.0 - (ppnenet + inventory) / assets.replace(0, np.nan)


# ============================================================
# intangibles/assets slope over a half-year (soft-asset accumulation trend)
def f21ac_f21_asset_composition_intangsh_slope126_base_v076_signal(intangibles, assets):
    s = _f21_intang_share(intangibles, assets)
    b = _slope(s, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-intensity slope over a year (capex-cycle direction)
def f21ac_f21_asset_composition_capint_slope252_base_v077_signal(ppnenet, assets):
    s = _f21_capint(ppnenet, assets)
    b = _slope(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-share slope over a half-year (hard-asset accretion direction)
def f21ac_f21_asset_composition_tangsh_slope126_base_v078_signal(tangibles, assets):
    s = _f21_tangible_share(tangibles, assets)
    b = _slope(s, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory-share slope over a quarter (stocking trajectory)
def f21ac_f21_asset_composition_invsh_slope63_base_v079_signal(inventory, assets):
    s = _f21_invshare(inventory, assets)
    b = _slope(s, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# investments-share slope over a year (financialization trajectory)
def f21ac_f21_asset_composition_investsh_slope252_base_v080_signal(investments, assets):
    s = _f21_investshare(investments, assets)
    b = _slope(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# goodwill-proxy slope over a year (acquisition-load trend)
def f21ac_f21_asset_composition_gwproxy_slope252_base_v081_signal(intangibles, ppnenet):
    s = _f21_goodwill_proxy(intangibles, ppnenet)
    b = _slope(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-light-score slope over a year (de-capitalization trend)
def f21ac_f21_asset_composition_assetlight_slope252_base_v082_signal(ppnenet, inventory, assets):
    s = _f21_assetlight(ppnenet, inventory, assets)
    b = _slope(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles share dispersion: rolling std over a year (composition instability)
def f21ac_f21_asset_composition_intangsh_disp252_base_v083_signal(intangibles, assets):
    s = _f21_intang_share(intangibles, assets)
    b = _std(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-intensity dispersion: rolling std over a half-year
def f21ac_f21_asset_composition_capint_disp126_base_v084_signal(ppnenet, assets):
    s = _f21_capint(ppnenet, assets)
    b = _std(s, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-share coefficient of variation (relative composition instability)
def f21ac_f21_asset_composition_tangsh_cv252_base_v085_signal(tangibles, assets):
    s = _f21_tangible_share(tangibles, assets)
    b = _std(s, 252) / _mean(s, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles intensity relative to tangible book, z-scored (IP leverage on hard assets)
def f21ac_f21_asset_composition_intovertang_z_base_v086_signal(intangibles, tangibles):
    s = intangibles / tangibles.replace(0, np.nan)
    b = _z(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# investments per unit of assets minus its 504d median proxy (financial tilt extremity)
def f21ac_f21_asset_composition_investsh_extreme_base_v087_signal(investments, assets):
    s = _f21_investshare(investments, assets)
    med = s.rolling(504, min_periods=126).median()
    b = s - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ppnenet per unit of tangibles (plant intensity within hard assets)
def f21ac_f21_asset_composition_plantintens_base_v088_signal(ppnenet, tangibles):
    s = ppnenet / tangibles.replace(0, np.nan)
    b = _z(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory per unit of tangibles (stock weight within hard assets)
def f21ac_f21_asset_composition_invintens_base_v089_signal(inventory, tangibles):
    s = inventory / tangibles.replace(0, np.nan)
    b = _z(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles minus investments share (IP vs portfolio tilt)
def f21ac_f21_asset_composition_intminusinvest_base_v090_signal(intangibles, investments, assets):
    b = (intangibles - investments) / assets.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital intensity minus inventory share (fixed vs working hard-asset tilt)
def f21ac_f21_asset_composition_fixedminuswork_base_v091_signal(ppnenet, inventory, assets):
    b = (ppnenet - inventory) / assets.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# hard-asset coverage of intangibles: tangibles/(intangibles+ppnenet) (collateral cushion)
def f21ac_f21_asset_composition_hardcover_base_v092_signal(tangibles, intangibles, ppnenet):
    b = tangibles / (intangibles + ppnenet).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# investments coverage by tangibles (financial-asset backing), ranked
def f21ac_f21_asset_composition_investcover_rank_base_v093_signal(investments, tangibles):
    s = investments / tangibles.replace(0, np.nan)
    b = _rank(s, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles-share hit-rate: fraction of last year it rose quarter-on-quarter
def f21ac_f21_asset_composition_intangsh_hit_base_v094_signal(intangibles, assets):
    s = _f21_intang_share(intangibles, assets)
    up = (s > s.shift(63)).astype(float)
    b = up.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-intensity hit-rate: fraction of last year it rose (capex momentum breadth)
def f21ac_f21_asset_composition_capint_hit_base_v095_signal(ppnenet, assets):
    s = _f21_capint(ppnenet, assets)
    up = (s > s.shift(21)).astype(float)
    b = up.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory-share hit-rate of declines (destocking persistence)
def f21ac_f21_asset_composition_invsh_destock_base_v096_signal(inventory, assets):
    s = _f21_invshare(inventory, assets)
    dn = (s < s.shift(21)).astype(float)
    b = dn.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible accumulation streak: consecutive quarters intangibles/assets rising
def f21ac_f21_asset_composition_intangsh_streak_base_v097_signal(intangibles, assets):
    s = _f21_intang_share(intangibles, assets)
    up = (s > s.shift(63)).astype(float)

    def _streak(a):
        c = 0
        for v in a[::-1]:
            if v > 0.5:
                c += 1
            else:
                break
        return float(c)

    b = up.rolling(252, min_periods=63).apply(_streak, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-mix turnover: rolling sum of abs changes in the four shares (rebalancing churn)
def f21ac_f21_asset_composition_mixturnover_base_v098_signal(ppnenet, intangibles, inventory, investments, assets):
    a = assets.replace(0, np.nan)
    churn = (ppnenet / a).diff().abs() + (intangibles / a).diff().abs() \
        + (inventory / a).diff().abs() + (investments / a).diff().abs()
    b = churn.rolling(252, min_periods=63).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composition drift: euclidean distance of current shares from their year-ago values
def f21ac_f21_asset_composition_mixdrift_base_v099_signal(ppnenet, intangibles, inventory, investments, assets):
    a = assets.replace(0, np.nan)
    dp = (ppnenet / a) - (ppnenet / a).shift(252)
    di = (intangibles / a) - (intangibles / a).shift(252)
    dv = (inventory / a) - (inventory / a).shift(252)
    dn = (investments / a) - (investments / a).shift(252)
    b = (dp ** 2 + di ** 2 + dv ** 2 + dn ** 2) ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# soft-vs-hard balance: (intangibles+investments) vs (ppnenet+inventory)
def f21ac_f21_asset_composition_softhardbal_base_v100_signal(intangibles, investments, ppnenet, inventory):
    soft = intangibles + investments
    hard = ppnenet + inventory
    b = (soft - hard) / (soft + hard).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# soft-vs-hard balance momentum over a year
def f21ac_f21_asset_composition_softhardbal_yoy_base_v101_signal(intangibles, investments, ppnenet, inventory):
    soft = intangibles + investments
    hard = ppnenet + inventory
    s = (soft - hard) / (soft + hard).replace(0, np.nan)
    b = s - s.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital intensity convexity: sign x squared deviation from 252d mean
def f21ac_f21_asset_composition_capint_convex_base_v102_signal(ppnenet, assets):
    s = _f21_capint(ppnenet, assets)
    dev = s - s.rolling(252, min_periods=63).mean()
    b = np.sign(dev) * (dev ** 2)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles dominance ratio vs tangible book, year-over-year change
def f21ac_f21_asset_composition_intdomtang_yoy_base_v103_signal(intangibles, tangibles):
    s = intangibles / (intangibles + tangibles).replace(0, np.nan)
    b = s - s.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# investments-share acceleration (change of 21d change in financial tilt)
def f21ac_f21_asset_composition_investsh_accel_base_v104_signal(investments, assets):
    s = _f21_investshare(investments, assets)
    d = s - s.shift(21)
    b = d - d.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital intensity to investments share (real-vs-paper deployment), z-scored
def f21ac_f21_asset_composition_realpaper_z_base_v105_signal(ppnenet, investments):
    s = ppnenet / investments.replace(0, np.nan)
    b = _z(np.log(s.replace(0, np.nan)), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles per unit of net-PPE, level z-scored (IP-vs-plant deployment level)
def f21ac_f21_asset_composition_intppne_yoy_base_v106_signal(intangibles, ppnenet):
    s = intangibles / ppnenet.replace(0, np.nan)
    b = _z(np.log(s.replace(0, np.nan)), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory-share half-year momentum minus its full-year momentum (acceleration spread)
def f21ac_f21_asset_composition_invsh_momspread_base_v107_signal(inventory, assets):
    s = _f21_invshare(inventory, assets)
    b = (s - s.shift(126)) - (s - s.shift(252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-share EMA-fast minus EMA-slow (composition MACD on hard-asset weight)
def f21ac_f21_asset_composition_tangsh_macd_base_v108_signal(tangibles, assets):
    s = _f21_tangible_share(tangibles, assets)
    b = _ewm(s, 21) - _ewm(s, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles-share EMA-fast minus EMA-slow (composition MACD on soft-asset weight)
def f21ac_f21_asset_composition_intangsh_macd_base_v109_signal(intangibles, assets):
    s = _f21_intang_share(intangibles, assets)
    b = _ewm(s, 21) - _ewm(s, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financial-asset share EMA displacement (investments tilt vs its smooth trend)
def f21ac_f21_asset_composition_investsh_emadisp_base_v110_signal(investments, assets):
    s = _f21_investshare(investments, assets)
    b = s - _ewm(s, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# goodwill-proxy EMA-smoothed level (persistent acquisition load)
def f21ac_f21_asset_composition_gwproxy_ema_base_v111_signal(intangibles, ppnenet):
    s = _f21_goodwill_proxy(intangibles, ppnenet)
    b = _ewm(s, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# productive-asset share volatility (operating-footprint instability)
def f21ac_f21_asset_composition_prodsh_vol_base_v112_signal(ppnenet, inventory, assets):
    s = (ppnenet + inventory) / assets.replace(0, np.nan)
    b = _std(s.diff(), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles-share range position within its 504d range (soft-asset cycle position)
def f21ac_f21_asset_composition_intangsh_rngpos_base_v113_signal(intangibles, assets):
    s = _f21_intang_share(intangibles, assets)
    hi = s.rolling(504, min_periods=126).max()
    lo = s.rolling(504, min_periods=126).min()
    b = (s - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# investments-share range position within its 504d range (financial-asset cycle position)
def f21ac_f21_asset_composition_investsh_rngpos_base_v114_signal(investments, assets):
    s = _f21_investshare(investments, assets)
    hi = s.rolling(504, min_periods=126).max()
    lo = s.rolling(504, min_periods=126).min()
    b = (s - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital intensity distance below its 504d peak (under-investment gap)
def f21ac_f21_asset_composition_capint_peakgap_base_v115_signal(ppnenet, assets):
    s = _f21_capint(ppnenet, assets)
    mx = s.rolling(504, min_periods=126).max()
    b = s / mx.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory share distance above its 504d trough (stock-build cushion)
def f21ac_f21_asset_composition_invsh_troughgap_base_v116_signal(inventory, assets):
    s = _f21_invshare(inventory, assets)
    mn = s.rolling(504, min_periods=126).min()
    b = s / mn.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles-share x asset-growth interaction (soft-asset-led expansion)
def f21ac_f21_asset_composition_intgrowthx_base_v117_signal(intangibles, assets):
    si = _f21_intang_share(intangibles, assets)
    ga = np.log(assets.replace(0, np.nan) / assets.shift(126).replace(0, np.nan))
    b = si * np.sign(ga) * ga.abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-share x capital-intensity divergence (hard-asset quality split), z-scored
def f21ac_f21_asset_composition_tangcapint_div_base_v118_signal(tangibles, ppnenet, assets):
    zt = _z(_f21_tangible_share(tangibles, assets), 252)
    zc = _z(_f21_capint(ppnenet, assets), 252)
    b = zt - zc
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composition skew: third-moment of the four shares around their mean
def f21ac_f21_asset_composition_mixskew_base_v119_signal(ppnenet, intangibles, inventory, investments):
    tot = (ppnenet + intangibles + inventory + investments).replace(0, np.nan)
    stk = pd.concat([ppnenet / tot, intangibles / tot, inventory / tot, investments / tot], axis=1)
    m = stk.mean(axis=1)
    sd = stk.std(axis=1).replace(0, np.nan)
    cubed = ((stk.sub(m, axis=0)) ** 3).mean(axis=1)
    b = cubed / (sd ** 3)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smallest-component share (least-weighted asset class)
def f21ac_f21_asset_composition_minshare_base_v120_signal(ppnenet, intangibles, inventory, investments):
    tot = (ppnenet + intangibles + inventory + investments).replace(0, np.nan)
    stk = pd.concat([ppnenet / tot, intangibles / tot, inventory / tot, investments / tot], axis=1)
    b = stk.min(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# soft-asset share (intangibles+investments)/assets, slope over a half-year
def f21ac_f21_asset_composition_softsh_slope_base_v121_signal(intangibles, investments, assets):
    s = (intangibles + investments) / assets.replace(0, np.nan)
    b = _slope(s, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# hard-asset share (ppnenet+tangibles)/assets, rank vs 252d (real-asset percentile)
def f21ac_f21_asset_composition_realsh_rank_base_v122_signal(ppnenet, tangibles, assets):
    s = (ppnenet + tangibles) / assets.replace(0, np.nan)
    b = _rank(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles share quarterly change x its level (impulse weighted by soft-asset load)
def f21ac_f21_asset_composition_intimpulse_base_v123_signal(intangibles, assets):
    s = _f21_intang_share(intangibles, assets)
    chg = s - s.shift(63)
    b = chg * s
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital intensity reversal: deviation from 504d mean times negative momentum sign
def f21ac_f21_asset_composition_capint_reversal_base_v124_signal(ppnenet, assets):
    s = _f21_capint(ppnenet, assets)
    dev = s - s.rolling(504, min_periods=126).mean()
    mom = s - s.shift(63)
    b = -dev * np.sign(mom)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# investments share relative to inventory share (financial vs working composition), z
def f21ac_f21_asset_composition_investinvsh_z_base_v125_signal(investments, inventory, assets):
    s = (_f21_investshare(investments, assets)) - (_f21_invshare(inventory, assets))
    b = _z(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# goodwill proxy vs tangible share spread (intangible-heaviness vs collateral)
def f21ac_f21_asset_composition_gwvstang_base_v126_signal(intangibles, ppnenet, tangibles, assets):
    gw = _f21_goodwill_proxy(intangibles, ppnenet)
    st = _f21_tangible_share(tangibles, assets)
    b = gw - st
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles per asset, log-second-difference (soft-asset growth acceleration)
def f21ac_f21_asset_composition_intangsh_logaccel_base_v127_signal(intangibles, assets):
    s = _f21_intang_share(intangibles, assets)
    ls = np.log(s.replace(0, np.nan))
    d = ls - ls.shift(63)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fixed-asset weight rank: ppnenet/assets percentile vs 252d history
def f21ac_f21_asset_composition_capint_pctile_base_v128_signal(ppnenet, assets):
    s = _f21_capint(ppnenet, assets)
    b = _rank(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital asset weight: inventory/(inventory+ppnenet) z-scored (stock-vs-plant regime)
def f21ac_f21_asset_composition_workplant_base_v129_signal(inventory, ppnenet):
    s = inventory / (inventory + ppnenet).replace(0, np.nan)
    b = _z(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-vs-plant split year-over-year change
def f21ac_f21_asset_composition_workplant_yoy_base_v130_signal(inventory, ppnenet):
    s = inventory / (inventory + ppnenet).replace(0, np.nan)
    b = s - s.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible intensity vs asset base, downside semideviation (soft-asset shrink risk)
def f21ac_f21_asset_composition_intangsh_semidev_base_v131_signal(intangibles, assets):
    s = _f21_intang_share(intangibles, assets)
    d = s.diff()
    neg = d.where(d < 0, 0.0)
    b = (neg ** 2).rolling(252, min_periods=63).mean() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital intensity upside semideviation (capex-build asymmetry)
def f21ac_f21_asset_composition_capint_upsemi_base_v132_signal(ppnenet, assets):
    s = _f21_capint(ppnenet, assets)
    d = s.diff()
    pos = d.where(d > 0, 0.0)
    b = (pos ** 2).rolling(252, min_periods=63).mean() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composition concentration trend: 63d change in top-share
def f21ac_f21_asset_composition_topshare_chg_base_v133_signal(ppnenet, intangibles, inventory, investments):
    tot = (ppnenet + intangibles + inventory + investments).replace(0, np.nan)
    stk = pd.concat([ppnenet / tot, intangibles / tot, inventory / tot, investments / tot], axis=1)
    top = stk.max(axis=1)
    b = top - top.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory + investments share (non-fixed deployable assets) z-scored
def f21ac_f21_asset_composition_deployable_z_base_v134_signal(inventory, investments, assets):
    s = (inventory + investments) / assets.replace(0, np.nan)
    b = _z(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible book per net-PPE, slope (non-plant hard-asset accretion direction)
def f21ac_f21_asset_composition_tangppne_slope_base_v135_signal(tangibles, ppnenet):
    s = tangibles / ppnenet.replace(0, np.nan)
    b = _slope(np.log(s.replace(0, np.nan)), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# investments-share x goodwill-proxy interaction (financialized acquirer profile)
def f21ac_f21_asset_composition_finacq_base_v136_signal(investments, assets, intangibles, ppnenet):
    sv = _f21_investshare(investments, assets)
    gw = _f21_goodwill_proxy(intangibles, ppnenet)
    b = sv * gw
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles-share relative dispersion across 63/126/252 windows (multi-horizon spread)
def f21ac_f21_asset_composition_intangsh_multispread_base_v137_signal(intangibles, assets):
    s = _f21_intang_share(intangibles, assets)
    m1 = _mean(s, 63)
    m2 = _mean(s, 126)
    m3 = _mean(s, 252)
    b = pd.concat([m1, m2, m3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital intensity relative to its own EMA, ranked (capex regime percentile)
def f21ac_f21_asset_composition_capint_emarank_base_v138_signal(ppnenet, assets):
    s = _f21_capint(ppnenet, assets)
    rel = s / _ewm(s, 126).replace(0, np.nan) - 1.0
    b = _rank(rel, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# soft-asset share momentum minus hard-asset share momentum (composition rotation speed)
def f21ac_f21_asset_composition_rotationspeed_base_v139_signal(intangibles, investments, ppnenet, tangibles, assets):
    a = assets.replace(0, np.nan)
    soft = (intangibles + investments) / a
    hard = (ppnenet + tangibles) / a
    b = (soft - soft.shift(126)) - (hard - hard.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles-share quarter-over-quarter difference normalized by its volatility
def f21ac_f21_asset_composition_intangsh_normchg_base_v140_signal(intangibles, assets):
    s = _f21_intang_share(intangibles, assets)
    chg = s - s.shift(63)
    vol = _std(s.diff(), 252).replace(0, np.nan)
    b = chg / vol
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# investments-share to total non-current proxy: investments/(investments+ppnenet+intangibles)
def f21ac_f21_asset_composition_investnoncur_base_v141_signal(investments, ppnenet, intangibles):
    b = investments / (investments + ppnenet + intangibles).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible book share minus capital intensity (off-balance hard-asset richness)
def f21ac_f21_asset_composition_tangexcap_base_v142_signal(tangibles, ppnenet, assets):
    st = _f21_tangible_share(tangibles, assets)
    sc = _f21_capint(ppnenet, assets)
    s = st - sc
    b = _rank(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# goodwill proxy quarterly acceleration (acquisition cadence change)
def f21ac_f21_asset_composition_gwproxy_accel_base_v143_signal(intangibles, ppnenet):
    s = _f21_goodwill_proxy(intangibles, ppnenet)
    d = s - s.shift(63)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory-share x investments-share (working+financial mix interaction)
def f21ac_f21_asset_composition_workfinx_base_v144_signal(inventory, investments, assets):
    si = _f21_invshare(inventory, assets)
    sv = _f21_investshare(investments, assets)
    b = (si * sv) ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-light score x intangibles share, ranked (genuine asset-light + IP-rich percentile)
def f21ac_f21_asset_composition_lightip_base_v145_signal(ppnenet, inventory, assets, intangibles):
    al = _f21_assetlight(ppnenet, inventory, assets)
    si = _f21_intang_share(intangibles, assets)
    b = _rank(al * si, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital intensity year-over-year minus its prior-year change (capex cycle turn)
def f21ac_f21_asset_composition_capint_cycleturn_base_v146_signal(ppnenet, assets):
    s = _f21_capint(ppnenet, assets)
    d = s - s.shift(252)
    b = d - d.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# investments per net-PPE slope (financialization-vs-capex trend)
def f21ac_f21_asset_composition_finvscapex_slope_base_v147_signal(investments, ppnenet):
    s = investments / ppnenet.replace(0, np.nan)
    b = _slope(np.log(s.replace(0, np.nan)), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-share downside deviation from a year ago (hard-asset erosion)
def f21ac_f21_asset_composition_tangerosion_base_v148_signal(tangibles, assets):
    s = _f21_tangible_share(tangibles, assets)
    chg = s - s.shift(252)
    b = chg.clip(upper=0.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles share relative to the mix's average share (above/below-average soft tilt)
def f21ac_f21_asset_composition_intangsh_relmix_base_v149_signal(ppnenet, intangibles, inventory, investments):
    tot = (ppnenet + intangibles + inventory + investments).replace(0, np.nan)
    si = intangibles / tot
    avg = 0.25
    b = si - avg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dominant-component persistence: 63d autocorrelation of the top asset weight (sticky leader)
def f21ac_f21_asset_composition_mixstability_base_v150_signal(ppnenet, intangibles, inventory, investments):
    tot = (ppnenet + intangibles + inventory + investments).replace(0, np.nan)
    stk = pd.concat([ppnenet / tot, intangibles / tot, inventory / tot, investments / tot], axis=1)
    top = stk.max(axis=1)
    lag = top.shift(63)
    cov = (top * lag).rolling(252, min_periods=126).mean() \
        - top.rolling(252, min_periods=126).mean() * lag.rolling(252, min_periods=126).mean()
    v1 = top.rolling(252, min_periods=126).std()
    v2 = lag.rolling(252, min_periods=126).std()
    b = cov / (v1 * v2).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f21ac_f21_asset_composition_intangsh_slope126_base_v076_signal,
    f21ac_f21_asset_composition_capint_slope252_base_v077_signal,
    f21ac_f21_asset_composition_tangsh_slope126_base_v078_signal,
    f21ac_f21_asset_composition_invsh_slope63_base_v079_signal,
    f21ac_f21_asset_composition_investsh_slope252_base_v080_signal,
    f21ac_f21_asset_composition_gwproxy_slope252_base_v081_signal,
    f21ac_f21_asset_composition_assetlight_slope252_base_v082_signal,
    f21ac_f21_asset_composition_intangsh_disp252_base_v083_signal,
    f21ac_f21_asset_composition_capint_disp126_base_v084_signal,
    f21ac_f21_asset_composition_tangsh_cv252_base_v085_signal,
    f21ac_f21_asset_composition_intovertang_z_base_v086_signal,
    f21ac_f21_asset_composition_investsh_extreme_base_v087_signal,
    f21ac_f21_asset_composition_plantintens_base_v088_signal,
    f21ac_f21_asset_composition_invintens_base_v089_signal,
    f21ac_f21_asset_composition_intminusinvest_base_v090_signal,
    f21ac_f21_asset_composition_fixedminuswork_base_v091_signal,
    f21ac_f21_asset_composition_hardcover_base_v092_signal,
    f21ac_f21_asset_composition_investcover_rank_base_v093_signal,
    f21ac_f21_asset_composition_intangsh_hit_base_v094_signal,
    f21ac_f21_asset_composition_capint_hit_base_v095_signal,
    f21ac_f21_asset_composition_invsh_destock_base_v096_signal,
    f21ac_f21_asset_composition_intangsh_streak_base_v097_signal,
    f21ac_f21_asset_composition_mixturnover_base_v098_signal,
    f21ac_f21_asset_composition_mixdrift_base_v099_signal,
    f21ac_f21_asset_composition_softhardbal_base_v100_signal,
    f21ac_f21_asset_composition_softhardbal_yoy_base_v101_signal,
    f21ac_f21_asset_composition_capint_convex_base_v102_signal,
    f21ac_f21_asset_composition_intdomtang_yoy_base_v103_signal,
    f21ac_f21_asset_composition_investsh_accel_base_v104_signal,
    f21ac_f21_asset_composition_realpaper_z_base_v105_signal,
    f21ac_f21_asset_composition_intppne_yoy_base_v106_signal,
    f21ac_f21_asset_composition_invsh_momspread_base_v107_signal,
    f21ac_f21_asset_composition_tangsh_macd_base_v108_signal,
    f21ac_f21_asset_composition_intangsh_macd_base_v109_signal,
    f21ac_f21_asset_composition_investsh_emadisp_base_v110_signal,
    f21ac_f21_asset_composition_gwproxy_ema_base_v111_signal,
    f21ac_f21_asset_composition_prodsh_vol_base_v112_signal,
    f21ac_f21_asset_composition_intangsh_rngpos_base_v113_signal,
    f21ac_f21_asset_composition_investsh_rngpos_base_v114_signal,
    f21ac_f21_asset_composition_capint_peakgap_base_v115_signal,
    f21ac_f21_asset_composition_invsh_troughgap_base_v116_signal,
    f21ac_f21_asset_composition_intgrowthx_base_v117_signal,
    f21ac_f21_asset_composition_tangcapint_div_base_v118_signal,
    f21ac_f21_asset_composition_mixskew_base_v119_signal,
    f21ac_f21_asset_composition_minshare_base_v120_signal,
    f21ac_f21_asset_composition_softsh_slope_base_v121_signal,
    f21ac_f21_asset_composition_realsh_rank_base_v122_signal,
    f21ac_f21_asset_composition_intimpulse_base_v123_signal,
    f21ac_f21_asset_composition_capint_reversal_base_v124_signal,
    f21ac_f21_asset_composition_investinvsh_z_base_v125_signal,
    f21ac_f21_asset_composition_gwvstang_base_v126_signal,
    f21ac_f21_asset_composition_intangsh_logaccel_base_v127_signal,
    f21ac_f21_asset_composition_capint_pctile_base_v128_signal,
    f21ac_f21_asset_composition_workplant_base_v129_signal,
    f21ac_f21_asset_composition_workplant_yoy_base_v130_signal,
    f21ac_f21_asset_composition_intangsh_semidev_base_v131_signal,
    f21ac_f21_asset_composition_capint_upsemi_base_v132_signal,
    f21ac_f21_asset_composition_topshare_chg_base_v133_signal,
    f21ac_f21_asset_composition_deployable_z_base_v134_signal,
    f21ac_f21_asset_composition_tangppne_slope_base_v135_signal,
    f21ac_f21_asset_composition_finacq_base_v136_signal,
    f21ac_f21_asset_composition_intangsh_multispread_base_v137_signal,
    f21ac_f21_asset_composition_capint_emarank_base_v138_signal,
    f21ac_f21_asset_composition_rotationspeed_base_v139_signal,
    f21ac_f21_asset_composition_intangsh_normchg_base_v140_signal,
    f21ac_f21_asset_composition_investnoncur_base_v141_signal,
    f21ac_f21_asset_composition_tangexcap_base_v142_signal,
    f21ac_f21_asset_composition_gwproxy_accel_base_v143_signal,
    f21ac_f21_asset_composition_workfinx_base_v144_signal,
    f21ac_f21_asset_composition_lightip_base_v145_signal,
    f21ac_f21_asset_composition_capint_cycleturn_base_v146_signal,
    f21ac_f21_asset_composition_finvscapex_slope_base_v147_signal,
    f21ac_f21_asset_composition_tangerosion_base_v148_signal,
    f21ac_f21_asset_composition_intangsh_relmix_base_v149_signal,
    f21ac_f21_asset_composition_mixstability_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F21_ASSET_COMPOSITION_REGISTRY_076_150 = REGISTRY


def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False, n=1500):
    g = np.random.default_rng(seed)
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.3
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    assets = _fund(101, base=1.0e9, drift=0.03, vol=0.04).rename("assets")
    ppnenet = _fund(102, base=3.0e8, drift=0.02, vol=0.05).rename("ppnenet")
    intangibles = _fund(103, base=2.0e8, drift=0.025, vol=0.06).rename("intangibles")
    tangibles = _fund(104, base=5.0e8, drift=0.02, vol=0.04).rename("tangibles")
    inventory = _fund(105, base=1.5e8, drift=0.015, vol=0.07).rename("inventory")
    investments = _fund(106, base=1.0e8, drift=0.02, vol=0.08).rename("investments")

    cols = {
        "assets": assets, "ppnenet": ppnenet, "intangibles": intangibles,
        "tangibles": tangibles, "inventory": inventory, "investments": investments,
    }

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, "%s nunique=%d" % (name, q.nunique())
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

    print("OK f21_asset_composition_base_076_150_claude: %d features pass" % n_features)
