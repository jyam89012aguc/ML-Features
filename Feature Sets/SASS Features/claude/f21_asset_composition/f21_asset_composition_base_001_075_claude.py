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
def _f21_share(part, whole):
    return part / whole.replace(0, np.nan)


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
# intangibles / assets level
def f21ac_f21_asset_composition_intangsh_252d_base_v001_signal(intangibles, assets):
    b = _f21_intang_share(intangibles, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles/assets z-scored vs own 252d history (de-trended composition shift)
def f21ac_f21_asset_composition_intangsh_z252_base_v002_signal(intangibles, assets):
    s = _f21_intang_share(intangibles, assets)
    b = _z(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles/assets percentile-ranked vs own 504d history
def f21ac_f21_asset_composition_intangsh_rank504_base_v003_signal(intangibles, assets):
    s = _f21_intang_share(intangibles, assets)
    b = _rank(s, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-book share (tangibles/assets) level
def f21ac_f21_asset_composition_tangsh_252d_base_v004_signal(tangibles, assets):
    b = _f21_tangible_share(tangibles, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible share z-scored vs 504d history
def f21ac_f21_asset_composition_tangsh_z504_base_v005_signal(tangibles, assets):
    s = _f21_tangible_share(tangibles, assets)
    b = _z(s, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital intensity: ppnenet/assets level
def f21ac_f21_asset_composition_capint_252d_base_v006_signal(ppnenet, assets):
    b = _f21_capint(ppnenet, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital intensity z-scored vs 252d history
def f21ac_f21_asset_composition_capint_z252_base_v007_signal(ppnenet, assets):
    s = _f21_capint(ppnenet, assets)
    b = _z(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory/assets level
def f21ac_f21_asset_composition_invsh_252d_base_v008_signal(inventory, assets):
    b = _f21_invshare(inventory, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory/assets z-scored vs 126d history
def f21ac_f21_asset_composition_invsh_z126_base_v009_signal(inventory, assets):
    s = _f21_invshare(inventory, assets)
    b = _z(s, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# investment-asset share (investments/assets) level
def f21ac_f21_asset_composition_investsh_252d_base_v010_signal(investments, assets):
    b = _f21_investshare(investments, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# investments/assets percentile-ranked vs 504d history
def f21ac_f21_asset_composition_investsh_rank504_base_v011_signal(investments, assets):
    s = _f21_investshare(investments, assets)
    b = _rank(s, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# goodwill-heavy proxy: intangibles / (intangibles + ppnenet)
def f21ac_f21_asset_composition_gwproxy_252d_base_v012_signal(intangibles, ppnenet):
    b = _f21_goodwill_proxy(intangibles, ppnenet)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# goodwill-heavy proxy z-scored vs 252d history
def f21ac_f21_asset_composition_gwproxy_z252_base_v013_signal(intangibles, ppnenet):
    s = _f21_goodwill_proxy(intangibles, ppnenet)
    b = _z(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-light score: 1 - (ppnenet+inventory)/assets
def f21ac_f21_asset_composition_assetlight_252d_base_v014_signal(ppnenet, inventory, assets):
    b = _f21_assetlight(ppnenet, inventory, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-light score z-scored vs 504d history
def f21ac_f21_asset_composition_assetlight_z504_base_v015_signal(ppnenet, inventory, assets):
    s = _f21_assetlight(ppnenet, inventory, assets)
    b = _z(s, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles vs tangibles balance (composition tilt)
def f21ac_f21_asset_composition_inttangbal_252d_base_v016_signal(intangibles, tangibles):
    b = (intangibles - tangibles) / (intangibles + tangibles).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangibles per unit of net PP&E (hard-asset breadth beyond plant)
def f21ac_f21_asset_composition_tangppne_252d_base_v017_signal(tangibles, ppnenet):
    b = tangibles / ppnenet.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory relative to net PP&E, year-over-year change (working vs fixed shift)
def f21ac_f21_asset_composition_invppne_252d_base_v018_signal(inventory, ppnenet):
    s = inventory / ppnenet.replace(0, np.nan)
    b = np.log(s.replace(0, np.nan) / s.shift(252).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# investments relative to tangibles (financial vs operating asset tilt)
def f21ac_f21_asset_composition_investtang_252d_base_v019_signal(investments, tangibles):
    b = investments / tangibles.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles per unit of inventory (brand/IP vs stock tilt), z-scored
def f21ac_f21_asset_composition_intinv_252d_base_v020_signal(intangibles, inventory):
    s = intangibles / inventory.replace(0, np.nan)
    b = _z(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating footprint trend: 63d change in (ppnenet+inventory)/assets
def f21ac_f21_asset_composition_prodsh_252d_base_v021_signal(ppnenet, inventory, assets):
    s = (ppnenet + inventory) / assets.replace(0, np.nan)
    b = s - s.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financial-asset share: investments/assets percentile rank vs 252d history
def f21ac_f21_asset_composition_finsh_rank252_base_v022_signal(investments, assets):
    s = _f21_investshare(investments, assets)
    b = _rank(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# hard-vs-soft divergence: tangibles log-growth minus intangibles log-growth
def f21ac_f21_asset_composition_hardsoft_252d_base_v023_signal(tangibles, intangibles):
    gt = np.log(tangibles.replace(0, np.nan) / tangibles.shift(126).replace(0, np.nan))
    gi = np.log(intangibles.replace(0, np.nan) / intangibles.shift(126).replace(0, np.nan))
    b = gt - gi
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles share growth: 63d change in intangibles/assets
def f21ac_f21_asset_composition_intangsh_chg63_base_v024_signal(intangibles, assets):
    s = _f21_intang_share(intangibles, assets)
    b = s - s.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital intensity change over a quarter (capex-driven shift)
def f21ac_f21_asset_composition_capint_chg63_base_v025_signal(ppnenet, assets):
    s = _f21_capint(ppnenet, assets)
    b = s - s.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory share change over a quarter (stocking/destocking)
def f21ac_f21_asset_composition_invsh_chg63_base_v026_signal(inventory, assets):
    s = _f21_invshare(inventory, assets)
    b = s - s.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# investments share year-over-year change
def f21ac_f21_asset_composition_investsh_yoy_base_v027_signal(investments, assets):
    s = _f21_investshare(investments, assets)
    b = s - s.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible share year-over-year change (hard-asset accumulation)
def f21ac_f21_asset_composition_tangsh_yoy_base_v028_signal(tangibles, assets):
    s = _f21_tangible_share(tangibles, assets)
    b = s - s.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# goodwill proxy year-over-year change (acquisition intensity)
def f21ac_f21_asset_composition_gwproxy_yoy_base_v029_signal(intangibles, ppnenet):
    s = _f21_goodwill_proxy(intangibles, ppnenet)
    b = s - s.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles log-growth (raw IP/goodwill expansion)
def f21ac_f21_asset_composition_intanggrow_252d_base_v030_signal(intangibles):
    b = np.log(intangibles.replace(0, np.nan) / intangibles.shift(252).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net PP&E log-growth (capex cycle)
def f21ac_f21_asset_composition_ppnegrow_252d_base_v031_signal(ppnenet):
    b = np.log(ppnenet.replace(0, np.nan) / ppnenet.shift(252).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-base log-growth (balance-sheet expansion)
def f21ac_f21_asset_composition_assetgrow_252d_base_v032_signal(assets):
    b = np.log(assets.replace(0, np.nan) / assets.shift(252).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles growth minus asset growth (composition drift toward soft assets)
def f21ac_f21_asset_composition_intvsasset_252d_base_v033_signal(intangibles, assets):
    gi = np.log(intangibles.replace(0, np.nan) / intangibles.shift(252).replace(0, np.nan))
    ga = np.log(assets.replace(0, np.nan) / assets.shift(252).replace(0, np.nan))
    b = gi - ga
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ppnenet growth minus asset growth (capital-deepening drift)
def f21ac_f21_asset_composition_ppnevsasset_252d_base_v034_signal(ppnenet, assets):
    gp = np.log(ppnenet.replace(0, np.nan) / ppnenet.shift(252).replace(0, np.nan))
    ga = np.log(assets.replace(0, np.nan) / assets.shift(252).replace(0, np.nan))
    b = gp - ga
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory growth minus asset growth (inventory build vs balance sheet)
def f21ac_f21_asset_composition_invvsasset_252d_base_v035_signal(inventory, assets):
    gi = np.log(inventory.replace(0, np.nan) / inventory.shift(252).replace(0, np.nan))
    ga = np.log(assets.replace(0, np.nan) / assets.shift(252).replace(0, np.nan))
    b = gi - ga
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composition entropy across {ppnenet, intangibles, inventory, investments} shares
def f21ac_f21_asset_composition_entropy_252d_base_v036_signal(ppnenet, intangibles, inventory, investments):
    tot = (ppnenet + intangibles + inventory + investments).replace(0, np.nan)
    parts = [ppnenet / tot, intangibles / tot, inventory / tot, investments / tot]
    ent = 0.0
    for p in parts:
        pc = p.clip(lower=1e-9)
        ent = ent - pc * np.log(pc)
    result = ent
    return result.replace([np.inf, -np.inf], np.nan)


# composition dispersion (std of the four component shares)
def f21ac_f21_asset_composition_dispersion_252d_base_v037_signal(ppnenet, intangibles, inventory, investments, assets):
    a = assets.replace(0, np.nan)
    stk = pd.concat([ppnenet / a, intangibles / a, inventory / a, investments / a], axis=1)
    b = stk.std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dominant-component concentration (max share of the asset mix)
def f21ac_f21_asset_composition_topshare_252d_base_v038_signal(ppnenet, intangibles, inventory, investments):
    tot = (ppnenet + intangibles + inventory + investments).replace(0, np.nan)
    stk = pd.concat([ppnenet / tot, intangibles / tot, inventory / tot, investments / tot], axis=1)
    b = stk.max(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# top-two-component gap: spread between the largest and second-largest asset weight
def f21ac_f21_asset_composition_hhi_252d_base_v039_signal(ppnenet, intangibles, inventory, investments):
    tot = (ppnenet + intangibles + inventory + investments).replace(0, np.nan)
    stk = pd.concat([ppnenet / tot, intangibles / tot, inventory / tot, investments / tot], axis=1)
    arr = np.sort(stk.values, axis=1)
    b = pd.Series(arr[:, -1] - arr[:, -2], index=stk.index)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-book share smoothed by slow EMA (persistent hard-asset base)
def f21ac_f21_asset_composition_tangsh_ema_base_v040_signal(tangibles, assets):
    s = _f21_tangible_share(tangibles, assets)
    b = _ewm(s, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles share minus its slow EMA (soft-asset displacement)
def f21ac_f21_asset_composition_intangsh_disp_base_v041_signal(intangibles, assets):
    s = _f21_intang_share(intangibles, assets)
    b = s - _ewm(s, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital intensity minus its slow EMA (capex impulse displacement)
def f21ac_f21_asset_composition_capint_disp_base_v042_signal(ppnenet, assets):
    s = _f21_capint(ppnenet, assets)
    b = s - _ewm(s, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# investments share volatility (instability of financial-asset tilt)
def f21ac_f21_asset_composition_investsh_vol_base_v043_signal(investments, assets):
    s = _f21_investshare(investments, assets)
    b = _std(s.diff(), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory share volatility (stocking instability)
def f21ac_f21_asset_composition_invsh_vol_base_v044_signal(inventory, assets):
    s = _f21_invshare(inventory, assets)
    b = _std(s.diff(), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles intensity relative to productive assets (IP per operating asset)
def f21ac_f21_asset_composition_intprod_252d_base_v045_signal(intangibles, ppnenet, inventory):
    b = intangibles / (ppnenet + inventory).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# investments per unit of net PP&E (financialization vs capex), z-scored
def f21ac_f21_asset_composition_finvscapex_252d_base_v046_signal(investments, ppnenet):
    s = investments / ppnenet.replace(0, np.nan)
    b = _z(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible share rank vs 252d history (where in its own range)
def f21ac_f21_asset_composition_tangsh_rank252_base_v047_signal(tangibles, assets):
    s = _f21_tangible_share(tangibles, assets)
    b = _rank(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital intensity rank vs 504d history
def f21ac_f21_asset_composition_capint_rank504_base_v048_signal(ppnenet, assets):
    s = _f21_capint(ppnenet, assets)
    b = _rank(s, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory share rank vs 252d history
def f21ac_f21_asset_composition_invsh_rank252_base_v049_signal(inventory, assets):
    s = _f21_invshare(inventory, assets)
    b = _rank(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# goodwill proxy rank vs 504d history (acquisition-load percentile)
def f21ac_f21_asset_composition_gwproxy_rank504_base_v050_signal(intangibles, ppnenet):
    s = _f21_goodwill_proxy(intangibles, ppnenet)
    b = _rank(s, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-light score rank vs 252d history
def f21ac_f21_asset_composition_assetlight_rank252_base_v051_signal(ppnenet, inventory, assets):
    s = _f21_assetlight(ppnenet, inventory, assets)
    b = _rank(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible vs intangible balance year-over-year change (composition rotation)
def f21ac_f21_asset_composition_inttangbal_yoy_base_v052_signal(intangibles, tangibles):
    s = (intangibles - tangibles) / (intangibles + tangibles).replace(0, np.nan)
    b = s - s.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share of assets that are neither investments nor intangibles (core operating share)
def f21ac_f21_asset_composition_coresh_252d_base_v053_signal(intangibles, investments, assets):
    b = (assets - intangibles - investments) / assets.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# investments + intangibles share (non-operating / non-productive tilt), z-scored
def f21ac_f21_asset_composition_nonopsh_252d_base_v054_signal(intangibles, investments, assets):
    s = (intangibles + investments) / assets.replace(0, np.nan)
    b = _z(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital intensity smoothed level (persistent asset-heaviness)
def f21ac_f21_asset_composition_capint_ema_base_v055_signal(ppnenet, assets):
    s = _f21_capint(ppnenet, assets)
    b = _ewm(s, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles/assets relative to its 504d max (proximity to peak soft-asset load)
def f21ac_f21_asset_composition_intangsh_peak_base_v056_signal(intangibles, assets):
    s = _f21_intang_share(intangibles, assets)
    mx = s.rolling(504, min_periods=126).max()
    b = s / mx.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital intensity relative to its 504d min (distance above trough capex base)
def f21ac_f21_asset_composition_capint_trough_base_v057_signal(ppnenet, assets):
    s = _f21_capint(ppnenet, assets)
    mn = s.rolling(504, min_periods=126).min()
    b = s / mn.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-share acceleration: difference of its 21d change vs the prior 21d change
def f21ac_f21_asset_composition_tangsh_accel_base_v058_signal(tangibles, assets):
    s = _f21_tangible_share(tangibles, assets)
    d = s - s.shift(21)
    b = d - d.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory-to-investments tilt, year-over-year change (operating-vs-financial rotation)
def f21ac_f21_asset_composition_invinvest_252d_base_v059_signal(inventory, investments):
    s = np.log((inventory / investments.replace(0, np.nan)).replace(0, np.nan))
    b = s - s.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles share interaction with capital intensity (soft x hard mix tension)
def f21ac_f21_asset_composition_softhardx_252d_base_v060_signal(intangibles, ppnenet, assets):
    si = _f21_intang_share(intangibles, assets)
    sp = _f21_capint(ppnenet, assets)
    b = si * sp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign x sqrt-magnitude of intangibles-share deviation from its long mean
def f21ac_f21_asset_composition_intangsh_smag_base_v061_signal(intangibles, assets):
    s = _f21_intang_share(intangibles, assets)
    dev = s - s.rolling(504, min_periods=126).mean()
    b = np.sign(dev) * (dev.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# real-vs-paper rotation: tangible-share momentum minus investments-share momentum
def f21ac_f21_asset_composition_tangvsinvest_base_v062_signal(tangibles, investments, assets):
    st = _f21_tangible_share(tangibles, assets)
    sv = _f21_investshare(investments, assets)
    b = (st - st.shift(63)) - (sv - sv.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory-vs-capital balance: inventory-share z minus capital-intensity z (mix tension)
def f21ac_f21_asset_composition_invcapintx_base_v063_signal(inventory, ppnenet, assets):
    zi = _z(_f21_invshare(inventory, assets), 252)
    zp = _z(_f21_capint(ppnenet, assets), 252)
    b = zi - zp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# investments share momentum over a half-year
def f21ac_f21_asset_composition_investsh_mom126_base_v064_signal(investments, assets):
    s = _f21_investshare(investments, assets)
    b = s - s.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# non-PPE hard assets share, z-scored vs 252d history (de-trended)
def f21ac_f21_asset_composition_otherhard_252d_base_v065_signal(tangibles, ppnenet, assets):
    s = (tangibles - ppnenet) / assets.replace(0, np.nan)
    b = _z(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composition stability: 1 / (1 + dispersion of intangibles-share changes)
def f21ac_f21_asset_composition_intangstab_base_v066_signal(intangibles, assets):
    s = _f21_intang_share(intangibles, assets)
    vol = _std(s.diff(), 252)
    b = 1.0 / (1.0 + vol)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acquisition-fueled expansion: intangibles growth in excess of net-PPE growth
def f21ac_f21_asset_composition_gwgrowx_base_v067_signal(intangibles, ppnenet):
    gi = np.log(intangibles.replace(0, np.nan) / intangibles.shift(126).replace(0, np.nan))
    gp = np.log(ppnenet.replace(0, np.nan) / ppnenet.shift(126).replace(0, np.nan))
    spread = gi - gp
    b = _z(spread, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financial-asset share momentum minus inventory-share momentum (mix rotation)
def f21ac_f21_asset_composition_finvsinvrot_base_v068_signal(investments, inventory, assets):
    sf = _f21_investshare(investments, assets)
    si = _f21_invshare(inventory, assets)
    b = (sf - sf.shift(126)) - (si - si.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed goodwill-proxy quarterly impulse interacted with intangible level
def f21ac_f21_asset_composition_intangsh_tanh_base_v069_signal(intangibles, assets, ppnenet):
    gw = _f21_goodwill_proxy(intangibles, ppnenet)
    si = _f21_intang_share(intangibles, assets)
    chg = gw - gw.shift(63)
    b = np.tanh(20.0 * chg) * si
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital intensity x tangible-share (asset-heavy hard-asset depth)
def f21ac_f21_asset_composition_heavyhard_base_v070_signal(ppnenet, tangibles, assets):
    sp = _f21_capint(ppnenet, assets)
    st = _f21_tangible_share(tangibles, assets)
    b = sp * st
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inventory share relative to its 252d mean (stock-build deviation)
def f21ac_f21_asset_composition_invsh_dev_base_v071_signal(inventory, assets):
    s = _f21_invshare(inventory, assets)
    b = s / s.rolling(252, min_periods=63).mean().replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-light score change over a year (de-capitalization trend)
def f21ac_f21_asset_composition_assetlight_yoy_base_v072_signal(ppnenet, inventory, assets):
    s = _f21_assetlight(ppnenet, inventory, assets)
    b = s - s.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles dominance over total productive base, ranked vs 252d (asset-light percentile)
def f21ac_f21_asset_composition_intdom_rank_base_v073_signal(intangibles, ppnenet, inventory):
    s = intangibles / (ppnenet + inventory).replace(0, np.nan)
    b = _rank(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composition tilt: investments share z minus capital-intensity z (paper vs plant)
def f21ac_f21_asset_composition_papervsplant_base_v074_signal(investments, ppnenet, assets):
    zf = _z(_f21_investshare(investments, assets), 252)
    zp = _z(_f21_capint(ppnenet, assets), 252)
    b = zf - zp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# real-asset density: (tangibles+inventory)/assets z-scored
def f21ac_f21_asset_composition_realdens_z_base_v075_signal(tangibles, inventory, assets):
    s = (tangibles + inventory) / assets.replace(0, np.nan)
    b = _z(s, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f21ac_f21_asset_composition_intangsh_252d_base_v001_signal,
    f21ac_f21_asset_composition_intangsh_z252_base_v002_signal,
    f21ac_f21_asset_composition_intangsh_rank504_base_v003_signal,
    f21ac_f21_asset_composition_tangsh_252d_base_v004_signal,
    f21ac_f21_asset_composition_tangsh_z504_base_v005_signal,
    f21ac_f21_asset_composition_capint_252d_base_v006_signal,
    f21ac_f21_asset_composition_capint_z252_base_v007_signal,
    f21ac_f21_asset_composition_invsh_252d_base_v008_signal,
    f21ac_f21_asset_composition_invsh_z126_base_v009_signal,
    f21ac_f21_asset_composition_investsh_252d_base_v010_signal,
    f21ac_f21_asset_composition_investsh_rank504_base_v011_signal,
    f21ac_f21_asset_composition_gwproxy_252d_base_v012_signal,
    f21ac_f21_asset_composition_gwproxy_z252_base_v013_signal,
    f21ac_f21_asset_composition_assetlight_252d_base_v014_signal,
    f21ac_f21_asset_composition_assetlight_z504_base_v015_signal,
    f21ac_f21_asset_composition_inttangbal_252d_base_v016_signal,
    f21ac_f21_asset_composition_tangppne_252d_base_v017_signal,
    f21ac_f21_asset_composition_invppne_252d_base_v018_signal,
    f21ac_f21_asset_composition_investtang_252d_base_v019_signal,
    f21ac_f21_asset_composition_intinv_252d_base_v020_signal,
    f21ac_f21_asset_composition_prodsh_252d_base_v021_signal,
    f21ac_f21_asset_composition_finsh_rank252_base_v022_signal,
    f21ac_f21_asset_composition_hardsoft_252d_base_v023_signal,
    f21ac_f21_asset_composition_intangsh_chg63_base_v024_signal,
    f21ac_f21_asset_composition_capint_chg63_base_v025_signal,
    f21ac_f21_asset_composition_invsh_chg63_base_v026_signal,
    f21ac_f21_asset_composition_investsh_yoy_base_v027_signal,
    f21ac_f21_asset_composition_tangsh_yoy_base_v028_signal,
    f21ac_f21_asset_composition_gwproxy_yoy_base_v029_signal,
    f21ac_f21_asset_composition_intanggrow_252d_base_v030_signal,
    f21ac_f21_asset_composition_ppnegrow_252d_base_v031_signal,
    f21ac_f21_asset_composition_assetgrow_252d_base_v032_signal,
    f21ac_f21_asset_composition_intvsasset_252d_base_v033_signal,
    f21ac_f21_asset_composition_ppnevsasset_252d_base_v034_signal,
    f21ac_f21_asset_composition_invvsasset_252d_base_v035_signal,
    f21ac_f21_asset_composition_entropy_252d_base_v036_signal,
    f21ac_f21_asset_composition_dispersion_252d_base_v037_signal,
    f21ac_f21_asset_composition_topshare_252d_base_v038_signal,
    f21ac_f21_asset_composition_hhi_252d_base_v039_signal,
    f21ac_f21_asset_composition_tangsh_ema_base_v040_signal,
    f21ac_f21_asset_composition_intangsh_disp_base_v041_signal,
    f21ac_f21_asset_composition_capint_disp_base_v042_signal,
    f21ac_f21_asset_composition_investsh_vol_base_v043_signal,
    f21ac_f21_asset_composition_invsh_vol_base_v044_signal,
    f21ac_f21_asset_composition_intprod_252d_base_v045_signal,
    f21ac_f21_asset_composition_finvscapex_252d_base_v046_signal,
    f21ac_f21_asset_composition_tangsh_rank252_base_v047_signal,
    f21ac_f21_asset_composition_capint_rank504_base_v048_signal,
    f21ac_f21_asset_composition_invsh_rank252_base_v049_signal,
    f21ac_f21_asset_composition_gwproxy_rank504_base_v050_signal,
    f21ac_f21_asset_composition_assetlight_rank252_base_v051_signal,
    f21ac_f21_asset_composition_inttangbal_yoy_base_v052_signal,
    f21ac_f21_asset_composition_coresh_252d_base_v053_signal,
    f21ac_f21_asset_composition_nonopsh_252d_base_v054_signal,
    f21ac_f21_asset_composition_capint_ema_base_v055_signal,
    f21ac_f21_asset_composition_intangsh_peak_base_v056_signal,
    f21ac_f21_asset_composition_capint_trough_base_v057_signal,
    f21ac_f21_asset_composition_tangsh_accel_base_v058_signal,
    f21ac_f21_asset_composition_invinvest_252d_base_v059_signal,
    f21ac_f21_asset_composition_softhardx_252d_base_v060_signal,
    f21ac_f21_asset_composition_intangsh_smag_base_v061_signal,
    f21ac_f21_asset_composition_tangvsinvest_base_v062_signal,
    f21ac_f21_asset_composition_invcapintx_base_v063_signal,
    f21ac_f21_asset_composition_investsh_mom126_base_v064_signal,
    f21ac_f21_asset_composition_otherhard_252d_base_v065_signal,
    f21ac_f21_asset_composition_intangstab_base_v066_signal,
    f21ac_f21_asset_composition_gwgrowx_base_v067_signal,
    f21ac_f21_asset_composition_finvsinvrot_base_v068_signal,
    f21ac_f21_asset_composition_intangsh_tanh_base_v069_signal,
    f21ac_f21_asset_composition_heavyhard_base_v070_signal,
    f21ac_f21_asset_composition_invsh_dev_base_v071_signal,
    f21ac_f21_asset_composition_assetlight_yoy_base_v072_signal,
    f21ac_f21_asset_composition_intdom_rank_base_v073_signal,
    f21ac_f21_asset_composition_papervsplant_base_v074_signal,
    f21ac_f21_asset_composition_realdens_z_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F21_ASSET_COMPOSITION_REGISTRY_001_075 = REGISTRY


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

    print("OK f21_asset_composition_base_001_075_claude: %d features pass" % n_features)
