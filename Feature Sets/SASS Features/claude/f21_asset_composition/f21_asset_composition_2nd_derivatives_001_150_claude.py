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


def _z(s, w):
    m = s.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _rank(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).rank(pct=True) - 0.5


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# slope d1 intangibles/assets [lvl]
def f21ac_f21_asset_composition_intangsh_lvl_63d_slope_v001_signal(intangibles, assets):
    s = intangibles / assets.replace(0, np.nan)
    t = s
    b = t.rolling(63, min_periods=31).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 tangible-book share [lvl]
def f21ac_f21_asset_composition_tangsh_lvl_42d_slope_v002_signal(tangibles, assets):
    s = tangibles / assets.replace(0, np.nan)
    t = s
    b = t.rolling(42, min_periods=21).mean()
    d = b - b.shift(14)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 capital intensity [lvl]
def f21ac_f21_asset_composition_capint_lvl_168d_slope_v003_signal(ppnenet, assets):
    s = ppnenet / assets.replace(0, np.nan)
    t = s
    b = t.rolling(168, min_periods=84).mean()
    d = b - b.shift(42)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 inventory/assets [lvl]
def f21ac_f21_asset_composition_invsh_lvl_252d_slope_v004_signal(inventory, assets):
    s = inventory / assets.replace(0, np.nan)
    t = s
    b = t.rolling(252, min_periods=126).mean()
    d = b - b.shift(84)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 investments/assets [lvl]
def f21ac_f21_asset_composition_investsh_lvl_105d_slope_v005_signal(investments, assets):
    s = investments / assets.replace(0, np.nan)
    t = s
    b = t.rolling(105, min_periods=52).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 goodwill proxy [lvl]
def f21ac_f21_asset_composition_gwproxy_lvl_126d_slope_v006_signal(intangibles, ppnenet):
    s = intangibles / (intangibles + ppnenet).replace(0, np.nan)
    t = s
    b = t.rolling(126, min_periods=63).mean()
    d = b - b.shift(63)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 asset-light score [lvl]
def f21ac_f21_asset_composition_assetlight_lvl_189d_slope_v007_signal(ppnenet, inventory, assets):
    s = 1.0 - (ppnenet + inventory) / assets.replace(0, np.nan)
    t = s
    b = t.rolling(189, min_periods=94).mean()
    d = b - b.shift(42)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 intangible-vs-tangible balance [lvl]
def f21ac_f21_asset_composition_inttangbal_lvl_63d_slope_v008_signal(intangibles, tangibles):
    s = (intangibles - tangibles) / (intangibles + tangibles).replace(0, np.nan)
    t = s
    b = t.rolling(63, min_periods=31).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 hard-asset coverage [lvl]
def f21ac_f21_asset_composition_hardcover_lvl_42d_slope_v009_signal(tangibles, intangibles, ppnenet):
    s = tangibles / (intangibles + ppnenet).replace(0, np.nan)
    t = s
    b = t.rolling(42, min_periods=21).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 working-vs-plant split [lvl]
def f21ac_f21_asset_composition_workplant_lvl_168d_slope_v010_signal(inventory, ppnenet):
    s = inventory / (inventory + ppnenet).replace(0, np.nan)
    t = s
    b = t.rolling(168, min_periods=84).mean()
    d = b - b.shift(63)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 productive-asset share [lvl]
def f21ac_f21_asset_composition_prodsh_lvl_252d_slope_v011_signal(ppnenet, inventory, assets):
    s = (ppnenet + inventory) / assets.replace(0, np.nan)
    t = s
    b = t.rolling(252, min_periods=126).mean()
    d = b - b.shift(42)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 soft-asset share [lvl]
def f21ac_f21_asset_composition_softsh_lvl_105d_slope_v012_signal(intangibles, investments, assets):
    s = (intangibles + investments) / assets.replace(0, np.nan)
    t = s
    b = t.rolling(105, min_periods=52).mean()
    d = b - b.shift(35)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 real-asset share [lvl]
def f21ac_f21_asset_composition_realsh_lvl_126d_slope_v013_signal(ppnenet, tangibles, assets):
    s = (ppnenet + tangibles) / assets.replace(0, np.nan)
    t = s
    b = t.rolling(126, min_periods=63).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 log intangibles-per-plant [lvl]
def f21ac_f21_asset_composition_intppne_lvl_189d_slope_v014_signal(intangibles, ppnenet):
    s = np.log((intangibles / ppnenet.replace(0, np.nan)).replace(0, np.nan))
    t = s
    b = t.rolling(189, min_periods=94).mean()
    d = b - b.shift(63)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 log investments-per-tangible [lvl]
def f21ac_f21_asset_composition_investtang_lvl_63d_slope_v015_signal(investments, tangibles):
    s = np.log((investments / tangibles.replace(0, np.nan)).replace(0, np.nan))
    t = s
    b = t.rolling(63, min_periods=31).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 log inventory-per-investments [lvl]
def f21ac_f21_asset_composition_invinvest_lvl_42d_slope_v016_signal(inventory, investments):
    s = np.log((inventory / investments.replace(0, np.nan)).replace(0, np.nan))
    t = s
    b = t.rolling(42, min_periods=21).mean()
    d = b - b.shift(14)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 core operating share [lvl]
def f21ac_f21_asset_composition_coresh_lvl_168d_slope_v017_signal(intangibles, investments, assets):
    s = (assets - intangibles - investments) / assets.replace(0, np.nan)
    t = s
    b = t.rolling(168, min_periods=84).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 intangibles per productive asset [lvl]
def f21ac_f21_asset_composition_intprod_lvl_252d_slope_v018_signal(intangibles, ppnenet, inventory):
    s = intangibles / (ppnenet + inventory).replace(0, np.nan)
    t = s
    b = t.rolling(252, min_periods=126).mean()
    d = b - b.shift(63)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 plant intensity in hard assets [lvl]
def f21ac_f21_asset_composition_plantint_lvl_105d_slope_v019_signal(ppnenet, tangibles):
    s = ppnenet / tangibles.replace(0, np.nan)
    t = s
    b = t.rolling(105, min_periods=52).mean()
    d = b - b.shift(42)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 deployable asset share [lvl]
def f21ac_f21_asset_composition_deploysh_lvl_126d_slope_v020_signal(inventory, investments, assets):
    s = (inventory + investments) / assets.replace(0, np.nan)
    t = s
    b = t.rolling(126, min_periods=63).mean()
    d = b - b.shift(42)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 fixed-minus-working tilt [lvl]
def f21ac_f21_asset_composition_fixwork_lvl_189d_slope_v021_signal(ppnenet, inventory, assets):
    s = (ppnenet - inventory) / assets.replace(0, np.nan)
    t = s
    b = t.rolling(189, min_periods=94).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 inventory per total hard asset [lvl]
def f21ac_f21_asset_composition_invreal_lvl_63d_slope_v022_signal(inventory, ppnenet, tangibles):
    s = inventory / (ppnenet + tangibles).replace(0, np.nan)
    t = s
    b = t.rolling(63, min_periods=31).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 investments share of non-current [lvl]
def f21ac_f21_asset_composition_investnoncur_lvl_42d_slope_v023_signal(investments, ppnenet, intangibles):
    s = investments / (investments + ppnenet + intangibles).replace(0, np.nan)
    t = s
    b = t.rolling(42, min_periods=21).mean()
    d = b - b.shift(14)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 soft-vs-hard balance [lvl]
def f21ac_f21_asset_composition_softhardbal_lvl_168d_slope_v024_signal(intangibles, investments, ppnenet, inventory):
    s = ((intangibles + investments) - (ppnenet + inventory)) / ((intangibles + investments) + (ppnenet + inventory)).replace(0, np.nan)
    t = s
    b = t.rolling(168, min_periods=84).mean()
    d = b - b.shift(84)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 goodwill-vs-tangible spread [lvl]
def f21ac_f21_asset_composition_gwvstang_lvl_252d_slope_v025_signal(intangibles, ppnenet, tangibles, assets):
    s = intangibles / (intangibles + ppnenet).replace(0, np.nan) - tangibles / assets.replace(0, np.nan)
    t = s
    b = t.rolling(252, min_periods=126).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 intangibles/assets [z126]
def f21ac_f21_asset_composition_intangsh_z126_126d_slope_v026_signal(intangibles, assets):
    s = intangibles / assets.replace(0, np.nan)
    t = _z(s, 126)
    b = t.rolling(126, min_periods=63).mean()
    d = b - b.shift(42)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 tangible-book share [z126]
def f21ac_f21_asset_composition_tangsh_z126_189d_slope_v027_signal(tangibles, assets):
    s = tangibles / assets.replace(0, np.nan)
    t = _z(s, 126)
    b = t.rolling(189, min_periods=94).mean()
    d = b - b.shift(84)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 capital intensity [z126]
def f21ac_f21_asset_composition_capint_z126_63d_slope_v028_signal(ppnenet, assets):
    s = ppnenet / assets.replace(0, np.nan)
    t = _z(s, 126)
    b = t.rolling(63, min_periods=31).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 inventory/assets [z126]
def f21ac_f21_asset_composition_invsh_z126_42d_slope_v029_signal(inventory, assets):
    s = inventory / assets.replace(0, np.nan)
    t = _z(s, 126)
    b = t.rolling(42, min_periods=21).mean()
    d = b - b.shift(14)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 investments/assets [z126]
def f21ac_f21_asset_composition_investsh_z126_168d_slope_v030_signal(investments, assets):
    s = investments / assets.replace(0, np.nan)
    t = _z(s, 126)
    b = t.rolling(168, min_periods=84).mean()
    d = b - b.shift(42)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 goodwill proxy [z126]
def f21ac_f21_asset_composition_gwproxy_z126_252d_slope_v031_signal(intangibles, ppnenet):
    s = intangibles / (intangibles + ppnenet).replace(0, np.nan)
    t = _z(s, 126)
    b = t.rolling(252, min_periods=126).mean()
    d = b - b.shift(84)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 asset-light score [z126]
def f21ac_f21_asset_composition_assetlight_z126_105d_slope_v032_signal(ppnenet, inventory, assets):
    s = 1.0 - (ppnenet + inventory) / assets.replace(0, np.nan)
    t = _z(s, 126)
    b = t.rolling(105, min_periods=52).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 intangible-vs-tangible balance [z126]
def f21ac_f21_asset_composition_inttangbal_z126_126d_slope_v033_signal(intangibles, tangibles):
    s = (intangibles - tangibles) / (intangibles + tangibles).replace(0, np.nan)
    t = _z(s, 126)
    b = t.rolling(126, min_periods=63).mean()
    d = b - b.shift(63)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 hard-asset coverage [z126]
def f21ac_f21_asset_composition_hardcover_z126_189d_slope_v034_signal(tangibles, intangibles, ppnenet):
    s = tangibles / (intangibles + ppnenet).replace(0, np.nan)
    t = _z(s, 126)
    b = t.rolling(189, min_periods=94).mean()
    d = b - b.shift(42)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 working-vs-plant split [z126]
def f21ac_f21_asset_composition_workplant_z126_63d_slope_v035_signal(inventory, ppnenet):
    s = inventory / (inventory + ppnenet).replace(0, np.nan)
    t = _z(s, 126)
    b = t.rolling(63, min_periods=31).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 productive-asset share [z126]
def f21ac_f21_asset_composition_prodsh_z126_42d_slope_v036_signal(ppnenet, inventory, assets):
    s = (ppnenet + inventory) / assets.replace(0, np.nan)
    t = _z(s, 126)
    b = t.rolling(42, min_periods=21).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 soft-asset share [z126]
def f21ac_f21_asset_composition_softsh_z126_168d_slope_v037_signal(intangibles, investments, assets):
    s = (intangibles + investments) / assets.replace(0, np.nan)
    t = _z(s, 126)
    b = t.rolling(168, min_periods=84).mean()
    d = b - b.shift(63)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 real-asset share [z126]
def f21ac_f21_asset_composition_realsh_z126_252d_slope_v038_signal(ppnenet, tangibles, assets):
    s = (ppnenet + tangibles) / assets.replace(0, np.nan)
    t = _z(s, 126)
    b = t.rolling(252, min_periods=126).mean()
    d = b - b.shift(42)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 log intangibles-per-plant [z126]
def f21ac_f21_asset_composition_intppne_z126_105d_slope_v039_signal(intangibles, ppnenet):
    s = np.log((intangibles / ppnenet.replace(0, np.nan)).replace(0, np.nan))
    t = _z(s, 126)
    b = t.rolling(105, min_periods=52).mean()
    d = b - b.shift(35)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 log investments-per-tangible [z126]
def f21ac_f21_asset_composition_investtang_z126_126d_slope_v040_signal(investments, tangibles):
    s = np.log((investments / tangibles.replace(0, np.nan)).replace(0, np.nan))
    t = _z(s, 126)
    b = t.rolling(126, min_periods=63).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 log inventory-per-investments [z126]
def f21ac_f21_asset_composition_invinvest_z126_189d_slope_v041_signal(inventory, investments):
    s = np.log((inventory / investments.replace(0, np.nan)).replace(0, np.nan))
    t = _z(s, 126)
    b = t.rolling(189, min_periods=94).mean()
    d = b - b.shift(63)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 core operating share [z126]
def f21ac_f21_asset_composition_coresh_z126_63d_slope_v042_signal(intangibles, investments, assets):
    s = (assets - intangibles - investments) / assets.replace(0, np.nan)
    t = _z(s, 126)
    b = t.rolling(63, min_periods=31).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 intangibles per productive asset [z126]
def f21ac_f21_asset_composition_intprod_z126_42d_slope_v043_signal(intangibles, ppnenet, inventory):
    s = intangibles / (ppnenet + inventory).replace(0, np.nan)
    t = _z(s, 126)
    b = t.rolling(42, min_periods=21).mean()
    d = b - b.shift(14)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 plant intensity in hard assets [z126]
def f21ac_f21_asset_composition_plantint_z126_168d_slope_v044_signal(ppnenet, tangibles):
    s = ppnenet / tangibles.replace(0, np.nan)
    t = _z(s, 126)
    b = t.rolling(168, min_periods=84).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 deployable asset share [z126]
def f21ac_f21_asset_composition_deploysh_z126_252d_slope_v045_signal(inventory, investments, assets):
    s = (inventory + investments) / assets.replace(0, np.nan)
    t = _z(s, 126)
    b = t.rolling(252, min_periods=126).mean()
    d = b - b.shift(63)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 fixed-minus-working tilt [z126]
def f21ac_f21_asset_composition_fixwork_z126_105d_slope_v046_signal(ppnenet, inventory, assets):
    s = (ppnenet - inventory) / assets.replace(0, np.nan)
    t = _z(s, 126)
    b = t.rolling(105, min_periods=52).mean()
    d = b - b.shift(42)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 inventory per total hard asset [z126]
def f21ac_f21_asset_composition_invreal_z126_126d_slope_v047_signal(inventory, ppnenet, tangibles):
    s = inventory / (ppnenet + tangibles).replace(0, np.nan)
    t = _z(s, 126)
    b = t.rolling(126, min_periods=63).mean()
    d = b - b.shift(42)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 investments share of non-current [z126]
def f21ac_f21_asset_composition_investnoncur_z126_189d_slope_v048_signal(investments, ppnenet, intangibles):
    s = investments / (investments + ppnenet + intangibles).replace(0, np.nan)
    t = _z(s, 126)
    b = t.rolling(189, min_periods=94).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 soft-vs-hard balance [z126]
def f21ac_f21_asset_composition_softhardbal_z126_63d_slope_v049_signal(intangibles, investments, ppnenet, inventory):
    s = ((intangibles + investments) - (ppnenet + inventory)) / ((intangibles + investments) + (ppnenet + inventory)).replace(0, np.nan)
    t = _z(s, 126)
    b = t.rolling(63, min_periods=31).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 goodwill-vs-tangible spread [z126]
def f21ac_f21_asset_composition_gwvstang_z126_42d_slope_v050_signal(intangibles, ppnenet, tangibles, assets):
    s = intangibles / (intangibles + ppnenet).replace(0, np.nan) - tangibles / assets.replace(0, np.nan)
    t = _z(s, 126)
    b = t.rolling(42, min_periods=21).mean()
    d = b - b.shift(14)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 intangibles/assets [rank252]
def f21ac_f21_asset_composition_intangsh_rank252_252d_slope_v051_signal(intangibles, assets):
    s = intangibles / assets.replace(0, np.nan)
    t = _rank(s, 252)
    b = t.rolling(252, min_periods=126).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 tangible-book share [rank252]
def f21ac_f21_asset_composition_tangsh_rank252_105d_slope_v052_signal(tangibles, assets):
    s = tangibles / assets.replace(0, np.nan)
    t = _rank(s, 252)
    b = t.rolling(105, min_periods=52).mean()
    d = b - b.shift(35)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 capital intensity [rank252]
def f21ac_f21_asset_composition_capint_rank252_126d_slope_v053_signal(ppnenet, assets):
    s = ppnenet / assets.replace(0, np.nan)
    t = _rank(s, 252)
    b = t.rolling(126, min_periods=63).mean()
    d = b - b.shift(42)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 inventory/assets [rank252]
def f21ac_f21_asset_composition_invsh_rank252_189d_slope_v054_signal(inventory, assets):
    s = inventory / assets.replace(0, np.nan)
    t = _rank(s, 252)
    b = t.rolling(189, min_periods=94).mean()
    d = b - b.shift(84)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 investments/assets [rank252]
def f21ac_f21_asset_composition_investsh_rank252_63d_slope_v055_signal(investments, assets):
    s = investments / assets.replace(0, np.nan)
    t = _rank(s, 252)
    b = t.rolling(63, min_periods=31).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 goodwill proxy [rank252]
def f21ac_f21_asset_composition_gwproxy_rank252_42d_slope_v056_signal(intangibles, ppnenet):
    s = intangibles / (intangibles + ppnenet).replace(0, np.nan)
    t = _rank(s, 252)
    b = t.rolling(42, min_periods=21).mean()
    d = b - b.shift(14)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 asset-light score [rank252]
def f21ac_f21_asset_composition_assetlight_rank252_168d_slope_v057_signal(ppnenet, inventory, assets):
    s = 1.0 - (ppnenet + inventory) / assets.replace(0, np.nan)
    t = _rank(s, 252)
    b = t.rolling(168, min_periods=84).mean()
    d = b - b.shift(42)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 intangible-vs-tangible balance [rank252]
def f21ac_f21_asset_composition_inttangbal_rank252_252d_slope_v058_signal(intangibles, tangibles):
    s = (intangibles - tangibles) / (intangibles + tangibles).replace(0, np.nan)
    t = _rank(s, 252)
    b = t.rolling(252, min_periods=126).mean()
    d = b - b.shift(84)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 hard-asset coverage [rank252]
def f21ac_f21_asset_composition_hardcover_rank252_105d_slope_v059_signal(tangibles, intangibles, ppnenet):
    s = tangibles / (intangibles + ppnenet).replace(0, np.nan)
    t = _rank(s, 252)
    b = t.rolling(105, min_periods=52).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 working-vs-plant split [rank252]
def f21ac_f21_asset_composition_workplant_rank252_126d_slope_v060_signal(inventory, ppnenet):
    s = inventory / (inventory + ppnenet).replace(0, np.nan)
    t = _rank(s, 252)
    b = t.rolling(126, min_periods=63).mean()
    d = b - b.shift(63)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 productive-asset share [rank252]
def f21ac_f21_asset_composition_prodsh_rank252_189d_slope_v061_signal(ppnenet, inventory, assets):
    s = (ppnenet + inventory) / assets.replace(0, np.nan)
    t = _rank(s, 252)
    b = t.rolling(189, min_periods=94).mean()
    d = b - b.shift(42)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 soft-asset share [rank252]
def f21ac_f21_asset_composition_softsh_rank252_63d_slope_v062_signal(intangibles, investments, assets):
    s = (intangibles + investments) / assets.replace(0, np.nan)
    t = _rank(s, 252)
    b = t.rolling(63, min_periods=31).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 real-asset share [rank252]
def f21ac_f21_asset_composition_realsh_rank252_42d_slope_v063_signal(ppnenet, tangibles, assets):
    s = (ppnenet + tangibles) / assets.replace(0, np.nan)
    t = _rank(s, 252)
    b = t.rolling(42, min_periods=21).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 log intangibles-per-plant [rank252]
def f21ac_f21_asset_composition_intppne_rank252_168d_slope_v064_signal(intangibles, ppnenet):
    s = np.log((intangibles / ppnenet.replace(0, np.nan)).replace(0, np.nan))
    t = _rank(s, 252)
    b = t.rolling(168, min_periods=84).mean()
    d = b - b.shift(63)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 log investments-per-tangible [rank252]
def f21ac_f21_asset_composition_investtang_rank252_252d_slope_v065_signal(investments, tangibles):
    s = np.log((investments / tangibles.replace(0, np.nan)).replace(0, np.nan))
    t = _rank(s, 252)
    b = t.rolling(252, min_periods=126).mean()
    d = b - b.shift(42)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 log inventory-per-investments [rank252]
def f21ac_f21_asset_composition_invinvest_rank252_105d_slope_v066_signal(inventory, investments):
    s = np.log((inventory / investments.replace(0, np.nan)).replace(0, np.nan))
    t = _rank(s, 252)
    b = t.rolling(105, min_periods=52).mean()
    d = b - b.shift(35)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 core operating share [rank252]
def f21ac_f21_asset_composition_coresh_rank252_126d_slope_v067_signal(intangibles, investments, assets):
    s = (assets - intangibles - investments) / assets.replace(0, np.nan)
    t = _rank(s, 252)
    b = t.rolling(126, min_periods=63).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 intangibles per productive asset [rank252]
def f21ac_f21_asset_composition_intprod_rank252_189d_slope_v068_signal(intangibles, ppnenet, inventory):
    s = intangibles / (ppnenet + inventory).replace(0, np.nan)
    t = _rank(s, 252)
    b = t.rolling(189, min_periods=94).mean()
    d = b - b.shift(63)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 plant intensity in hard assets [rank252]
def f21ac_f21_asset_composition_plantint_rank252_63d_slope_v069_signal(ppnenet, tangibles):
    s = ppnenet / tangibles.replace(0, np.nan)
    t = _rank(s, 252)
    b = t.rolling(63, min_periods=31).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 deployable asset share [rank252]
def f21ac_f21_asset_composition_deploysh_rank252_42d_slope_v070_signal(inventory, investments, assets):
    s = (inventory + investments) / assets.replace(0, np.nan)
    t = _rank(s, 252)
    b = t.rolling(42, min_periods=21).mean()
    d = b - b.shift(14)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 fixed-minus-working tilt [rank252]
def f21ac_f21_asset_composition_fixwork_rank252_168d_slope_v071_signal(ppnenet, inventory, assets):
    s = (ppnenet - inventory) / assets.replace(0, np.nan)
    t = _rank(s, 252)
    b = t.rolling(168, min_periods=84).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 inventory per total hard asset [rank252]
def f21ac_f21_asset_composition_invreal_rank252_252d_slope_v072_signal(inventory, ppnenet, tangibles):
    s = inventory / (ppnenet + tangibles).replace(0, np.nan)
    t = _rank(s, 252)
    b = t.rolling(252, min_periods=126).mean()
    d = b - b.shift(63)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 investments share of non-current [rank252]
def f21ac_f21_asset_composition_investnoncur_rank252_105d_slope_v073_signal(investments, ppnenet, intangibles):
    s = investments / (investments + ppnenet + intangibles).replace(0, np.nan)
    t = _rank(s, 252)
    b = t.rolling(105, min_periods=52).mean()
    d = b - b.shift(42)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 soft-vs-hard balance [rank252]
def f21ac_f21_asset_composition_softhardbal_rank252_126d_slope_v074_signal(intangibles, investments, ppnenet, inventory):
    s = ((intangibles + investments) - (ppnenet + inventory)) / ((intangibles + investments) + (ppnenet + inventory)).replace(0, np.nan)
    t = _rank(s, 252)
    b = t.rolling(126, min_periods=63).mean()
    d = b - b.shift(42)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 goodwill-vs-tangible spread [rank252]
def f21ac_f21_asset_composition_gwvstang_rank252_189d_slope_v075_signal(intangibles, ppnenet, tangibles, assets):
    s = intangibles / (intangibles + ppnenet).replace(0, np.nan) - tangibles / assets.replace(0, np.nan)
    t = _rank(s, 252)
    b = t.rolling(189, min_periods=94).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 intangibles/assets [qoq]
def f21ac_f21_asset_composition_intangsh_qoq_42d_slope_v076_signal(intangibles, assets):
    s = intangibles / assets.replace(0, np.nan)
    t = s - s.shift(63)
    b = t.rolling(42, min_periods=21).mean()
    d = b - b.shift(14)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 tangible-book share [qoq]
def f21ac_f21_asset_composition_tangsh_qoq_168d_slope_v077_signal(tangibles, assets):
    s = tangibles / assets.replace(0, np.nan)
    t = s - s.shift(63)
    b = t.rolling(168, min_periods=84).mean()
    d = b - b.shift(84)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 capital intensity [qoq]
def f21ac_f21_asset_composition_capint_qoq_252d_slope_v078_signal(ppnenet, assets):
    s = ppnenet / assets.replace(0, np.nan)
    t = s - s.shift(63)
    b = t.rolling(252, min_periods=126).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 inventory/assets [qoq]
def f21ac_f21_asset_composition_invsh_qoq_105d_slope_v079_signal(inventory, assets):
    s = inventory / assets.replace(0, np.nan)
    t = s - s.shift(63)
    b = t.rolling(105, min_periods=52).mean()
    d = b - b.shift(35)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 investments/assets [qoq]
def f21ac_f21_asset_composition_investsh_qoq_126d_slope_v080_signal(investments, assets):
    s = investments / assets.replace(0, np.nan)
    t = s - s.shift(63)
    b = t.rolling(126, min_periods=63).mean()
    d = b - b.shift(42)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 goodwill proxy [qoq]
def f21ac_f21_asset_composition_gwproxy_qoq_189d_slope_v081_signal(intangibles, ppnenet):
    s = intangibles / (intangibles + ppnenet).replace(0, np.nan)
    t = s - s.shift(63)
    b = t.rolling(189, min_periods=94).mean()
    d = b - b.shift(84)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 asset-light score [qoq]
def f21ac_f21_asset_composition_assetlight_qoq_63d_slope_v082_signal(ppnenet, inventory, assets):
    s = 1.0 - (ppnenet + inventory) / assets.replace(0, np.nan)
    t = s - s.shift(63)
    b = t.rolling(63, min_periods=31).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 intangible-vs-tangible balance [qoq]
def f21ac_f21_asset_composition_inttangbal_qoq_42d_slope_v083_signal(intangibles, tangibles):
    s = (intangibles - tangibles) / (intangibles + tangibles).replace(0, np.nan)
    t = s - s.shift(63)
    b = t.rolling(42, min_periods=21).mean()
    d = b - b.shift(14)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 hard-asset coverage [qoq]
def f21ac_f21_asset_composition_hardcover_qoq_168d_slope_v084_signal(tangibles, intangibles, ppnenet):
    s = tangibles / (intangibles + ppnenet).replace(0, np.nan)
    t = s - s.shift(63)
    b = t.rolling(168, min_periods=84).mean()
    d = b - b.shift(42)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 working-vs-plant split [qoq]
def f21ac_f21_asset_composition_workplant_qoq_252d_slope_v085_signal(inventory, ppnenet):
    s = inventory / (inventory + ppnenet).replace(0, np.nan)
    t = s - s.shift(63)
    b = t.rolling(252, min_periods=126).mean()
    d = b - b.shift(84)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 productive-asset share [qoq]
def f21ac_f21_asset_composition_prodsh_qoq_105d_slope_v086_signal(ppnenet, inventory, assets):
    s = (ppnenet + inventory) / assets.replace(0, np.nan)
    t = s - s.shift(63)
    b = t.rolling(105, min_periods=52).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 soft-asset share [qoq]
def f21ac_f21_asset_composition_softsh_qoq_126d_slope_v087_signal(intangibles, investments, assets):
    s = (intangibles + investments) / assets.replace(0, np.nan)
    t = s - s.shift(63)
    b = t.rolling(126, min_periods=63).mean()
    d = b - b.shift(63)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 real-asset share [qoq]
def f21ac_f21_asset_composition_realsh_qoq_189d_slope_v088_signal(ppnenet, tangibles, assets):
    s = (ppnenet + tangibles) / assets.replace(0, np.nan)
    t = s - s.shift(63)
    b = t.rolling(189, min_periods=94).mean()
    d = b - b.shift(42)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 log intangibles-per-plant [qoq]
def f21ac_f21_asset_composition_intppne_qoq_63d_slope_v089_signal(intangibles, ppnenet):
    s = np.log((intangibles / ppnenet.replace(0, np.nan)).replace(0, np.nan))
    t = s - s.shift(63)
    b = t.rolling(63, min_periods=31).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 log investments-per-tangible [qoq]
def f21ac_f21_asset_composition_investtang_qoq_42d_slope_v090_signal(investments, tangibles):
    s = np.log((investments / tangibles.replace(0, np.nan)).replace(0, np.nan))
    t = s - s.shift(63)
    b = t.rolling(42, min_periods=21).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 log inventory-per-investments [qoq]
def f21ac_f21_asset_composition_invinvest_qoq_168d_slope_v091_signal(inventory, investments):
    s = np.log((inventory / investments.replace(0, np.nan)).replace(0, np.nan))
    t = s - s.shift(63)
    b = t.rolling(168, min_periods=84).mean()
    d = b - b.shift(63)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 core operating share [qoq]
def f21ac_f21_asset_composition_coresh_qoq_252d_slope_v092_signal(intangibles, investments, assets):
    s = (assets - intangibles - investments) / assets.replace(0, np.nan)
    t = s - s.shift(63)
    b = t.rolling(252, min_periods=126).mean()
    d = b - b.shift(42)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 intangibles per productive asset [qoq]
def f21ac_f21_asset_composition_intprod_qoq_105d_slope_v093_signal(intangibles, ppnenet, inventory):
    s = intangibles / (ppnenet + inventory).replace(0, np.nan)
    t = s - s.shift(63)
    b = t.rolling(105, min_periods=52).mean()
    d = b - b.shift(35)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 plant intensity in hard assets [qoq]
def f21ac_f21_asset_composition_plantint_qoq_126d_slope_v094_signal(ppnenet, tangibles):
    s = ppnenet / tangibles.replace(0, np.nan)
    t = s - s.shift(63)
    b = t.rolling(126, min_periods=63).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 deployable asset share [qoq]
def f21ac_f21_asset_composition_deploysh_qoq_189d_slope_v095_signal(inventory, investments, assets):
    s = (inventory + investments) / assets.replace(0, np.nan)
    t = s - s.shift(63)
    b = t.rolling(189, min_periods=94).mean()
    d = b - b.shift(63)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 fixed-minus-working tilt [qoq]
def f21ac_f21_asset_composition_fixwork_qoq_63d_slope_v096_signal(ppnenet, inventory, assets):
    s = (ppnenet - inventory) / assets.replace(0, np.nan)
    t = s - s.shift(63)
    b = t.rolling(63, min_periods=31).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 inventory per total hard asset [qoq]
def f21ac_f21_asset_composition_invreal_qoq_42d_slope_v097_signal(inventory, ppnenet, tangibles):
    s = inventory / (ppnenet + tangibles).replace(0, np.nan)
    t = s - s.shift(63)
    b = t.rolling(42, min_periods=21).mean()
    d = b - b.shift(14)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 investments share of non-current [qoq]
def f21ac_f21_asset_composition_investnoncur_qoq_168d_slope_v098_signal(investments, ppnenet, intangibles):
    s = investments / (investments + ppnenet + intangibles).replace(0, np.nan)
    t = s - s.shift(63)
    b = t.rolling(168, min_periods=84).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 soft-vs-hard balance [qoq]
def f21ac_f21_asset_composition_softhardbal_qoq_252d_slope_v099_signal(intangibles, investments, ppnenet, inventory):
    s = ((intangibles + investments) - (ppnenet + inventory)) / ((intangibles + investments) + (ppnenet + inventory)).replace(0, np.nan)
    t = s - s.shift(63)
    b = t.rolling(252, min_periods=126).mean()
    d = b - b.shift(63)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 goodwill-vs-tangible spread [qoq]
def f21ac_f21_asset_composition_gwvstang_qoq_105d_slope_v100_signal(intangibles, ppnenet, tangibles, assets):
    s = intangibles / (intangibles + ppnenet).replace(0, np.nan) - tangibles / assets.replace(0, np.nan)
    t = s - s.shift(63)
    b = t.rolling(105, min_periods=52).mean()
    d = b - b.shift(42)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 intangibles/assets [relmean]
def f21ac_f21_asset_composition_intangsh_relmean_189d_slope_v101_signal(intangibles, assets):
    s = intangibles / assets.replace(0, np.nan)
    t = s / s.rolling(252, min_periods=63).mean().replace(0, np.nan) - 1.0
    b = t.rolling(189, min_periods=94).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 tangible-book share [relmean]
def f21ac_f21_asset_composition_tangsh_relmean_63d_slope_v102_signal(tangibles, assets):
    s = tangibles / assets.replace(0, np.nan)
    t = s / s.rolling(252, min_periods=63).mean().replace(0, np.nan) - 1.0
    b = t.rolling(63, min_periods=31).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 capital intensity [relmean]
def f21ac_f21_asset_composition_capint_relmean_42d_slope_v103_signal(ppnenet, assets):
    s = ppnenet / assets.replace(0, np.nan)
    t = s / s.rolling(252, min_periods=63).mean().replace(0, np.nan) - 1.0
    b = t.rolling(42, min_periods=21).mean()
    d = b - b.shift(14)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 inventory/assets [relmean]
def f21ac_f21_asset_composition_invsh_relmean_168d_slope_v104_signal(inventory, assets):
    s = inventory / assets.replace(0, np.nan)
    t = s / s.rolling(252, min_periods=63).mean().replace(0, np.nan) - 1.0
    b = t.rolling(168, min_periods=84).mean()
    d = b - b.shift(84)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 investments/assets [relmean]
def f21ac_f21_asset_composition_investsh_relmean_252d_slope_v105_signal(investments, assets):
    s = investments / assets.replace(0, np.nan)
    t = s / s.rolling(252, min_periods=63).mean().replace(0, np.nan) - 1.0
    b = t.rolling(252, min_periods=126).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 goodwill proxy [relmean]
def f21ac_f21_asset_composition_gwproxy_relmean_105d_slope_v106_signal(intangibles, ppnenet):
    s = intangibles / (intangibles + ppnenet).replace(0, np.nan)
    t = s / s.rolling(252, min_periods=63).mean().replace(0, np.nan) - 1.0
    b = t.rolling(105, min_periods=52).mean()
    d = b - b.shift(35)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 asset-light score [relmean]
def f21ac_f21_asset_composition_assetlight_relmean_126d_slope_v107_signal(ppnenet, inventory, assets):
    s = 1.0 - (ppnenet + inventory) / assets.replace(0, np.nan)
    t = s / s.rolling(252, min_periods=63).mean().replace(0, np.nan) - 1.0
    b = t.rolling(126, min_periods=63).mean()
    d = b - b.shift(42)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 intangible-vs-tangible balance [relmean]
def f21ac_f21_asset_composition_inttangbal_relmean_189d_slope_v108_signal(intangibles, tangibles):
    s = (intangibles - tangibles) / (intangibles + tangibles).replace(0, np.nan)
    t = s / s.rolling(252, min_periods=63).mean().replace(0, np.nan) - 1.0
    b = t.rolling(189, min_periods=94).mean()
    d = b - b.shift(84)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 hard-asset coverage [relmean]
def f21ac_f21_asset_composition_hardcover_relmean_63d_slope_v109_signal(tangibles, intangibles, ppnenet):
    s = tangibles / (intangibles + ppnenet).replace(0, np.nan)
    t = s / s.rolling(252, min_periods=63).mean().replace(0, np.nan) - 1.0
    b = t.rolling(63, min_periods=31).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 working-vs-plant split [relmean]
def f21ac_f21_asset_composition_workplant_relmean_42d_slope_v110_signal(inventory, ppnenet):
    s = inventory / (inventory + ppnenet).replace(0, np.nan)
    t = s / s.rolling(252, min_periods=63).mean().replace(0, np.nan) - 1.0
    b = t.rolling(42, min_periods=21).mean()
    d = b - b.shift(14)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 productive-asset share [relmean]
def f21ac_f21_asset_composition_prodsh_relmean_168d_slope_v111_signal(ppnenet, inventory, assets):
    s = (ppnenet + inventory) / assets.replace(0, np.nan)
    t = s / s.rolling(252, min_periods=63).mean().replace(0, np.nan) - 1.0
    b = t.rolling(168, min_periods=84).mean()
    d = b - b.shift(42)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 soft-asset share [relmean]
def f21ac_f21_asset_composition_softsh_relmean_252d_slope_v112_signal(intangibles, investments, assets):
    s = (intangibles + investments) / assets.replace(0, np.nan)
    t = s / s.rolling(252, min_periods=63).mean().replace(0, np.nan) - 1.0
    b = t.rolling(252, min_periods=126).mean()
    d = b - b.shift(84)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 real-asset share [relmean]
def f21ac_f21_asset_composition_realsh_relmean_105d_slope_v113_signal(ppnenet, tangibles, assets):
    s = (ppnenet + tangibles) / assets.replace(0, np.nan)
    t = s / s.rolling(252, min_periods=63).mean().replace(0, np.nan) - 1.0
    b = t.rolling(105, min_periods=52).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 log intangibles-per-plant [relmean]
def f21ac_f21_asset_composition_intppne_relmean_126d_slope_v114_signal(intangibles, ppnenet):
    s = np.log((intangibles / ppnenet.replace(0, np.nan)).replace(0, np.nan))
    t = s / s.rolling(252, min_periods=63).mean().replace(0, np.nan) - 1.0
    b = t.rolling(126, min_periods=63).mean()
    d = b - b.shift(63)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 log investments-per-tangible [relmean]
def f21ac_f21_asset_composition_investtang_relmean_189d_slope_v115_signal(investments, tangibles):
    s = np.log((investments / tangibles.replace(0, np.nan)).replace(0, np.nan))
    t = s / s.rolling(252, min_periods=63).mean().replace(0, np.nan) - 1.0
    b = t.rolling(189, min_periods=94).mean()
    d = b - b.shift(42)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 log inventory-per-investments [relmean]
def f21ac_f21_asset_composition_invinvest_relmean_63d_slope_v116_signal(inventory, investments):
    s = np.log((inventory / investments.replace(0, np.nan)).replace(0, np.nan))
    t = s / s.rolling(252, min_periods=63).mean().replace(0, np.nan) - 1.0
    b = t.rolling(63, min_periods=31).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 core operating share [relmean]
def f21ac_f21_asset_composition_coresh_relmean_42d_slope_v117_signal(intangibles, investments, assets):
    s = (assets - intangibles - investments) / assets.replace(0, np.nan)
    t = s / s.rolling(252, min_periods=63).mean().replace(0, np.nan) - 1.0
    b = t.rolling(42, min_periods=21).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 intangibles per productive asset [relmean]
def f21ac_f21_asset_composition_intprod_relmean_168d_slope_v118_signal(intangibles, ppnenet, inventory):
    s = intangibles / (ppnenet + inventory).replace(0, np.nan)
    t = s / s.rolling(252, min_periods=63).mean().replace(0, np.nan) - 1.0
    b = t.rolling(168, min_periods=84).mean()
    d = b - b.shift(63)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 plant intensity in hard assets [relmean]
def f21ac_f21_asset_composition_plantint_relmean_252d_slope_v119_signal(ppnenet, tangibles):
    s = ppnenet / tangibles.replace(0, np.nan)
    t = s / s.rolling(252, min_periods=63).mean().replace(0, np.nan) - 1.0
    b = t.rolling(252, min_periods=126).mean()
    d = b - b.shift(42)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 deployable asset share [relmean]
def f21ac_f21_asset_composition_deploysh_relmean_105d_slope_v120_signal(inventory, investments, assets):
    s = (inventory + investments) / assets.replace(0, np.nan)
    t = s / s.rolling(252, min_periods=63).mean().replace(0, np.nan) - 1.0
    b = t.rolling(105, min_periods=52).mean()
    d = b - b.shift(35)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 fixed-minus-working tilt [relmean]
def f21ac_f21_asset_composition_fixwork_relmean_126d_slope_v121_signal(ppnenet, inventory, assets):
    s = (ppnenet - inventory) / assets.replace(0, np.nan)
    t = s / s.rolling(252, min_periods=63).mean().replace(0, np.nan) - 1.0
    b = t.rolling(126, min_periods=63).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 inventory per total hard asset [relmean]
def f21ac_f21_asset_composition_invreal_relmean_189d_slope_v122_signal(inventory, ppnenet, tangibles):
    s = inventory / (ppnenet + tangibles).replace(0, np.nan)
    t = s / s.rolling(252, min_periods=63).mean().replace(0, np.nan) - 1.0
    b = t.rolling(189, min_periods=94).mean()
    d = b - b.shift(63)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 investments share of non-current [relmean]
def f21ac_f21_asset_composition_investnoncur_relmean_63d_slope_v123_signal(investments, ppnenet, intangibles):
    s = investments / (investments + ppnenet + intangibles).replace(0, np.nan)
    t = s / s.rolling(252, min_periods=63).mean().replace(0, np.nan) - 1.0
    b = t.rolling(63, min_periods=31).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 soft-vs-hard balance [relmean]
def f21ac_f21_asset_composition_softhardbal_relmean_42d_slope_v124_signal(intangibles, investments, ppnenet, inventory):
    s = ((intangibles + investments) - (ppnenet + inventory)) / ((intangibles + investments) + (ppnenet + inventory)).replace(0, np.nan)
    t = s / s.rolling(252, min_periods=63).mean().replace(0, np.nan) - 1.0
    b = t.rolling(42, min_periods=21).mean()
    d = b - b.shift(14)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 goodwill-vs-tangible spread [relmean]
def f21ac_f21_asset_composition_gwvstang_relmean_168d_slope_v125_signal(intangibles, ppnenet, tangibles, assets):
    s = intangibles / (intangibles + ppnenet).replace(0, np.nan) - tangibles / assets.replace(0, np.nan)
    t = s / s.rolling(252, min_periods=63).mean().replace(0, np.nan) - 1.0
    b = t.rolling(168, min_periods=84).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 intangibles/assets [relema]
def f21ac_f21_asset_composition_intangsh_relema_105d_slope_v126_signal(intangibles, assets):
    s = intangibles / assets.replace(0, np.nan)
    t = s / s.ewm(span=84, min_periods=42).mean().replace(0, np.nan) - 1.0
    b = t.rolling(105, min_periods=52).mean()
    d = b - b.shift(42)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 tangible-book share [relema]
def f21ac_f21_asset_composition_tangsh_relema_126d_slope_v127_signal(tangibles, assets):
    s = tangibles / assets.replace(0, np.nan)
    t = s / s.ewm(span=84, min_periods=42).mean().replace(0, np.nan) - 1.0
    b = t.rolling(126, min_periods=63).mean()
    d = b - b.shift(42)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 capital intensity [relema]
def f21ac_f21_asset_composition_capint_relema_189d_slope_v128_signal(ppnenet, assets):
    s = ppnenet / assets.replace(0, np.nan)
    t = s / s.ewm(span=84, min_periods=42).mean().replace(0, np.nan) - 1.0
    b = t.rolling(189, min_periods=94).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 inventory/assets [relema]
def f21ac_f21_asset_composition_invsh_relema_63d_slope_v129_signal(inventory, assets):
    s = inventory / assets.replace(0, np.nan)
    t = s / s.ewm(span=84, min_periods=42).mean().replace(0, np.nan) - 1.0
    b = t.rolling(63, min_periods=31).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 investments/assets [relema]
def f21ac_f21_asset_composition_investsh_relema_42d_slope_v130_signal(investments, assets):
    s = investments / assets.replace(0, np.nan)
    t = s / s.ewm(span=84, min_periods=42).mean().replace(0, np.nan) - 1.0
    b = t.rolling(42, min_periods=21).mean()
    d = b - b.shift(14)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 goodwill proxy [relema]
def f21ac_f21_asset_composition_gwproxy_relema_168d_slope_v131_signal(intangibles, ppnenet):
    s = intangibles / (intangibles + ppnenet).replace(0, np.nan)
    t = s / s.ewm(span=84, min_periods=42).mean().replace(0, np.nan) - 1.0
    b = t.rolling(168, min_periods=84).mean()
    d = b - b.shift(84)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 asset-light score [relema]
def f21ac_f21_asset_composition_assetlight_relema_252d_slope_v132_signal(ppnenet, inventory, assets):
    s = 1.0 - (ppnenet + inventory) / assets.replace(0, np.nan)
    t = s / s.ewm(span=84, min_periods=42).mean().replace(0, np.nan) - 1.0
    b = t.rolling(252, min_periods=126).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 intangible-vs-tangible balance [relema]
def f21ac_f21_asset_composition_inttangbal_relema_105d_slope_v133_signal(intangibles, tangibles):
    s = (intangibles - tangibles) / (intangibles + tangibles).replace(0, np.nan)
    t = s / s.ewm(span=84, min_periods=42).mean().replace(0, np.nan) - 1.0
    b = t.rolling(105, min_periods=52).mean()
    d = b - b.shift(35)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 hard-asset coverage [relema]
def f21ac_f21_asset_composition_hardcover_relema_126d_slope_v134_signal(tangibles, intangibles, ppnenet):
    s = tangibles / (intangibles + ppnenet).replace(0, np.nan)
    t = s / s.ewm(span=84, min_periods=42).mean().replace(0, np.nan) - 1.0
    b = t.rolling(126, min_periods=63).mean()
    d = b - b.shift(42)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 working-vs-plant split [relema]
def f21ac_f21_asset_composition_workplant_relema_189d_slope_v135_signal(inventory, ppnenet):
    s = inventory / (inventory + ppnenet).replace(0, np.nan)
    t = s / s.ewm(span=84, min_periods=42).mean().replace(0, np.nan) - 1.0
    b = t.rolling(189, min_periods=94).mean()
    d = b - b.shift(84)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 productive-asset share [relema]
def f21ac_f21_asset_composition_prodsh_relema_63d_slope_v136_signal(ppnenet, inventory, assets):
    s = (ppnenet + inventory) / assets.replace(0, np.nan)
    t = s / s.ewm(span=84, min_periods=42).mean().replace(0, np.nan) - 1.0
    b = t.rolling(63, min_periods=31).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 soft-asset share [relema]
def f21ac_f21_asset_composition_softsh_relema_42d_slope_v137_signal(intangibles, investments, assets):
    s = (intangibles + investments) / assets.replace(0, np.nan)
    t = s / s.ewm(span=84, min_periods=42).mean().replace(0, np.nan) - 1.0
    b = t.rolling(42, min_periods=21).mean()
    d = b - b.shift(14)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 real-asset share [relema]
def f21ac_f21_asset_composition_realsh_relema_168d_slope_v138_signal(ppnenet, tangibles, assets):
    s = (ppnenet + tangibles) / assets.replace(0, np.nan)
    t = s / s.ewm(span=84, min_periods=42).mean().replace(0, np.nan) - 1.0
    b = t.rolling(168, min_periods=84).mean()
    d = b - b.shift(42)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 log intangibles-per-plant [relema]
def f21ac_f21_asset_composition_intppne_relema_252d_slope_v139_signal(intangibles, ppnenet):
    s = np.log((intangibles / ppnenet.replace(0, np.nan)).replace(0, np.nan))
    t = s / s.ewm(span=84, min_periods=42).mean().replace(0, np.nan) - 1.0
    b = t.rolling(252, min_periods=126).mean()
    d = b - b.shift(84)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 log investments-per-tangible [relema]
def f21ac_f21_asset_composition_investtang_relema_105d_slope_v140_signal(investments, tangibles):
    s = np.log((investments / tangibles.replace(0, np.nan)).replace(0, np.nan))
    t = s / s.ewm(span=84, min_periods=42).mean().replace(0, np.nan) - 1.0
    b = t.rolling(105, min_periods=52).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 log inventory-per-investments [relema]
def f21ac_f21_asset_composition_invinvest_relema_126d_slope_v141_signal(inventory, investments):
    s = np.log((inventory / investments.replace(0, np.nan)).replace(0, np.nan))
    t = s / s.ewm(span=84, min_periods=42).mean().replace(0, np.nan) - 1.0
    b = t.rolling(126, min_periods=63).mean()
    d = b - b.shift(63)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 core operating share [relema]
def f21ac_f21_asset_composition_coresh_relema_189d_slope_v142_signal(intangibles, investments, assets):
    s = (assets - intangibles - investments) / assets.replace(0, np.nan)
    t = s / s.ewm(span=84, min_periods=42).mean().replace(0, np.nan) - 1.0
    b = t.rolling(189, min_periods=94).mean()
    d = b - b.shift(42)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 intangibles per productive asset [relema]
def f21ac_f21_asset_composition_intprod_relema_63d_slope_v143_signal(intangibles, ppnenet, inventory):
    s = intangibles / (ppnenet + inventory).replace(0, np.nan)
    t = s / s.ewm(span=84, min_periods=42).mean().replace(0, np.nan) - 1.0
    b = t.rolling(63, min_periods=31).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 plant intensity in hard assets [relema]
def f21ac_f21_asset_composition_plantint_relema_42d_slope_v144_signal(ppnenet, tangibles):
    s = ppnenet / tangibles.replace(0, np.nan)
    t = s / s.ewm(span=84, min_periods=42).mean().replace(0, np.nan) - 1.0
    b = t.rolling(42, min_periods=21).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 deployable asset share [relema]
def f21ac_f21_asset_composition_deploysh_relema_168d_slope_v145_signal(inventory, investments, assets):
    s = (inventory + investments) / assets.replace(0, np.nan)
    t = s / s.ewm(span=84, min_periods=42).mean().replace(0, np.nan) - 1.0
    b = t.rolling(168, min_periods=84).mean()
    d = b - b.shift(63)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 fixed-minus-working tilt [relema]
def f21ac_f21_asset_composition_fixwork_relema_252d_slope_v146_signal(ppnenet, inventory, assets):
    s = (ppnenet - inventory) / assets.replace(0, np.nan)
    t = s / s.ewm(span=84, min_periods=42).mean().replace(0, np.nan) - 1.0
    b = t.rolling(252, min_periods=126).mean()
    d = b - b.shift(42)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 inventory per total hard asset [relema]
def f21ac_f21_asset_composition_invreal_relema_105d_slope_v147_signal(inventory, ppnenet, tangibles):
    s = inventory / (ppnenet + tangibles).replace(0, np.nan)
    t = s / s.ewm(span=84, min_periods=42).mean().replace(0, np.nan) - 1.0
    b = t.rolling(105, min_periods=52).mean()
    d = b - b.shift(35)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 investments share of non-current [relema]
def f21ac_f21_asset_composition_investnoncur_relema_126d_slope_v148_signal(investments, ppnenet, intangibles):
    s = investments / (investments + ppnenet + intangibles).replace(0, np.nan)
    t = s / s.ewm(span=84, min_periods=42).mean().replace(0, np.nan) - 1.0
    b = t.rolling(126, min_periods=63).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 soft-vs-hard balance [relema]
def f21ac_f21_asset_composition_softhardbal_relema_189d_slope_v149_signal(intangibles, investments, ppnenet, inventory):
    s = ((intangibles + investments) - (ppnenet + inventory)) / ((intangibles + investments) + (ppnenet + inventory)).replace(0, np.nan)
    t = s / s.ewm(span=84, min_periods=42).mean().replace(0, np.nan) - 1.0
    b = t.rolling(189, min_periods=94).mean()
    d = b - b.shift(63)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

# slope d1 goodwill-vs-tangible spread [relema]
def f21ac_f21_asset_composition_gwvstang_relema_63d_slope_v150_signal(intangibles, ppnenet, tangibles, assets):
    s = intangibles / (intangibles + ppnenet).replace(0, np.nan) - tangibles / assets.replace(0, np.nan)
    t = s / s.ewm(span=84, min_periods=42).mean().replace(0, np.nan) - 1.0
    b = t.rolling(63, min_periods=31).mean()
    d = b - b.shift(21)
    r = d
    return r.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f21ac_f21_asset_composition_intangsh_lvl_63d_slope_v001_signal,
    f21ac_f21_asset_composition_tangsh_lvl_42d_slope_v002_signal,
    f21ac_f21_asset_composition_capint_lvl_168d_slope_v003_signal,
    f21ac_f21_asset_composition_invsh_lvl_252d_slope_v004_signal,
    f21ac_f21_asset_composition_investsh_lvl_105d_slope_v005_signal,
    f21ac_f21_asset_composition_gwproxy_lvl_126d_slope_v006_signal,
    f21ac_f21_asset_composition_assetlight_lvl_189d_slope_v007_signal,
    f21ac_f21_asset_composition_inttangbal_lvl_63d_slope_v008_signal,
    f21ac_f21_asset_composition_hardcover_lvl_42d_slope_v009_signal,
    f21ac_f21_asset_composition_workplant_lvl_168d_slope_v010_signal,
    f21ac_f21_asset_composition_prodsh_lvl_252d_slope_v011_signal,
    f21ac_f21_asset_composition_softsh_lvl_105d_slope_v012_signal,
    f21ac_f21_asset_composition_realsh_lvl_126d_slope_v013_signal,
    f21ac_f21_asset_composition_intppne_lvl_189d_slope_v014_signal,
    f21ac_f21_asset_composition_investtang_lvl_63d_slope_v015_signal,
    f21ac_f21_asset_composition_invinvest_lvl_42d_slope_v016_signal,
    f21ac_f21_asset_composition_coresh_lvl_168d_slope_v017_signal,
    f21ac_f21_asset_composition_intprod_lvl_252d_slope_v018_signal,
    f21ac_f21_asset_composition_plantint_lvl_105d_slope_v019_signal,
    f21ac_f21_asset_composition_deploysh_lvl_126d_slope_v020_signal,
    f21ac_f21_asset_composition_fixwork_lvl_189d_slope_v021_signal,
    f21ac_f21_asset_composition_invreal_lvl_63d_slope_v022_signal,
    f21ac_f21_asset_composition_investnoncur_lvl_42d_slope_v023_signal,
    f21ac_f21_asset_composition_softhardbal_lvl_168d_slope_v024_signal,
    f21ac_f21_asset_composition_gwvstang_lvl_252d_slope_v025_signal,
    f21ac_f21_asset_composition_intangsh_z126_126d_slope_v026_signal,
    f21ac_f21_asset_composition_tangsh_z126_189d_slope_v027_signal,
    f21ac_f21_asset_composition_capint_z126_63d_slope_v028_signal,
    f21ac_f21_asset_composition_invsh_z126_42d_slope_v029_signal,
    f21ac_f21_asset_composition_investsh_z126_168d_slope_v030_signal,
    f21ac_f21_asset_composition_gwproxy_z126_252d_slope_v031_signal,
    f21ac_f21_asset_composition_assetlight_z126_105d_slope_v032_signal,
    f21ac_f21_asset_composition_inttangbal_z126_126d_slope_v033_signal,
    f21ac_f21_asset_composition_hardcover_z126_189d_slope_v034_signal,
    f21ac_f21_asset_composition_workplant_z126_63d_slope_v035_signal,
    f21ac_f21_asset_composition_prodsh_z126_42d_slope_v036_signal,
    f21ac_f21_asset_composition_softsh_z126_168d_slope_v037_signal,
    f21ac_f21_asset_composition_realsh_z126_252d_slope_v038_signal,
    f21ac_f21_asset_composition_intppne_z126_105d_slope_v039_signal,
    f21ac_f21_asset_composition_investtang_z126_126d_slope_v040_signal,
    f21ac_f21_asset_composition_invinvest_z126_189d_slope_v041_signal,
    f21ac_f21_asset_composition_coresh_z126_63d_slope_v042_signal,
    f21ac_f21_asset_composition_intprod_z126_42d_slope_v043_signal,
    f21ac_f21_asset_composition_plantint_z126_168d_slope_v044_signal,
    f21ac_f21_asset_composition_deploysh_z126_252d_slope_v045_signal,
    f21ac_f21_asset_composition_fixwork_z126_105d_slope_v046_signal,
    f21ac_f21_asset_composition_invreal_z126_126d_slope_v047_signal,
    f21ac_f21_asset_composition_investnoncur_z126_189d_slope_v048_signal,
    f21ac_f21_asset_composition_softhardbal_z126_63d_slope_v049_signal,
    f21ac_f21_asset_composition_gwvstang_z126_42d_slope_v050_signal,
    f21ac_f21_asset_composition_intangsh_rank252_252d_slope_v051_signal,
    f21ac_f21_asset_composition_tangsh_rank252_105d_slope_v052_signal,
    f21ac_f21_asset_composition_capint_rank252_126d_slope_v053_signal,
    f21ac_f21_asset_composition_invsh_rank252_189d_slope_v054_signal,
    f21ac_f21_asset_composition_investsh_rank252_63d_slope_v055_signal,
    f21ac_f21_asset_composition_gwproxy_rank252_42d_slope_v056_signal,
    f21ac_f21_asset_composition_assetlight_rank252_168d_slope_v057_signal,
    f21ac_f21_asset_composition_inttangbal_rank252_252d_slope_v058_signal,
    f21ac_f21_asset_composition_hardcover_rank252_105d_slope_v059_signal,
    f21ac_f21_asset_composition_workplant_rank252_126d_slope_v060_signal,
    f21ac_f21_asset_composition_prodsh_rank252_189d_slope_v061_signal,
    f21ac_f21_asset_composition_softsh_rank252_63d_slope_v062_signal,
    f21ac_f21_asset_composition_realsh_rank252_42d_slope_v063_signal,
    f21ac_f21_asset_composition_intppne_rank252_168d_slope_v064_signal,
    f21ac_f21_asset_composition_investtang_rank252_252d_slope_v065_signal,
    f21ac_f21_asset_composition_invinvest_rank252_105d_slope_v066_signal,
    f21ac_f21_asset_composition_coresh_rank252_126d_slope_v067_signal,
    f21ac_f21_asset_composition_intprod_rank252_189d_slope_v068_signal,
    f21ac_f21_asset_composition_plantint_rank252_63d_slope_v069_signal,
    f21ac_f21_asset_composition_deploysh_rank252_42d_slope_v070_signal,
    f21ac_f21_asset_composition_fixwork_rank252_168d_slope_v071_signal,
    f21ac_f21_asset_composition_invreal_rank252_252d_slope_v072_signal,
    f21ac_f21_asset_composition_investnoncur_rank252_105d_slope_v073_signal,
    f21ac_f21_asset_composition_softhardbal_rank252_126d_slope_v074_signal,
    f21ac_f21_asset_composition_gwvstang_rank252_189d_slope_v075_signal,
    f21ac_f21_asset_composition_intangsh_qoq_42d_slope_v076_signal,
    f21ac_f21_asset_composition_tangsh_qoq_168d_slope_v077_signal,
    f21ac_f21_asset_composition_capint_qoq_252d_slope_v078_signal,
    f21ac_f21_asset_composition_invsh_qoq_105d_slope_v079_signal,
    f21ac_f21_asset_composition_investsh_qoq_126d_slope_v080_signal,
    f21ac_f21_asset_composition_gwproxy_qoq_189d_slope_v081_signal,
    f21ac_f21_asset_composition_assetlight_qoq_63d_slope_v082_signal,
    f21ac_f21_asset_composition_inttangbal_qoq_42d_slope_v083_signal,
    f21ac_f21_asset_composition_hardcover_qoq_168d_slope_v084_signal,
    f21ac_f21_asset_composition_workplant_qoq_252d_slope_v085_signal,
    f21ac_f21_asset_composition_prodsh_qoq_105d_slope_v086_signal,
    f21ac_f21_asset_composition_softsh_qoq_126d_slope_v087_signal,
    f21ac_f21_asset_composition_realsh_qoq_189d_slope_v088_signal,
    f21ac_f21_asset_composition_intppne_qoq_63d_slope_v089_signal,
    f21ac_f21_asset_composition_investtang_qoq_42d_slope_v090_signal,
    f21ac_f21_asset_composition_invinvest_qoq_168d_slope_v091_signal,
    f21ac_f21_asset_composition_coresh_qoq_252d_slope_v092_signal,
    f21ac_f21_asset_composition_intprod_qoq_105d_slope_v093_signal,
    f21ac_f21_asset_composition_plantint_qoq_126d_slope_v094_signal,
    f21ac_f21_asset_composition_deploysh_qoq_189d_slope_v095_signal,
    f21ac_f21_asset_composition_fixwork_qoq_63d_slope_v096_signal,
    f21ac_f21_asset_composition_invreal_qoq_42d_slope_v097_signal,
    f21ac_f21_asset_composition_investnoncur_qoq_168d_slope_v098_signal,
    f21ac_f21_asset_composition_softhardbal_qoq_252d_slope_v099_signal,
    f21ac_f21_asset_composition_gwvstang_qoq_105d_slope_v100_signal,
    f21ac_f21_asset_composition_intangsh_relmean_189d_slope_v101_signal,
    f21ac_f21_asset_composition_tangsh_relmean_63d_slope_v102_signal,
    f21ac_f21_asset_composition_capint_relmean_42d_slope_v103_signal,
    f21ac_f21_asset_composition_invsh_relmean_168d_slope_v104_signal,
    f21ac_f21_asset_composition_investsh_relmean_252d_slope_v105_signal,
    f21ac_f21_asset_composition_gwproxy_relmean_105d_slope_v106_signal,
    f21ac_f21_asset_composition_assetlight_relmean_126d_slope_v107_signal,
    f21ac_f21_asset_composition_inttangbal_relmean_189d_slope_v108_signal,
    f21ac_f21_asset_composition_hardcover_relmean_63d_slope_v109_signal,
    f21ac_f21_asset_composition_workplant_relmean_42d_slope_v110_signal,
    f21ac_f21_asset_composition_prodsh_relmean_168d_slope_v111_signal,
    f21ac_f21_asset_composition_softsh_relmean_252d_slope_v112_signal,
    f21ac_f21_asset_composition_realsh_relmean_105d_slope_v113_signal,
    f21ac_f21_asset_composition_intppne_relmean_126d_slope_v114_signal,
    f21ac_f21_asset_composition_investtang_relmean_189d_slope_v115_signal,
    f21ac_f21_asset_composition_invinvest_relmean_63d_slope_v116_signal,
    f21ac_f21_asset_composition_coresh_relmean_42d_slope_v117_signal,
    f21ac_f21_asset_composition_intprod_relmean_168d_slope_v118_signal,
    f21ac_f21_asset_composition_plantint_relmean_252d_slope_v119_signal,
    f21ac_f21_asset_composition_deploysh_relmean_105d_slope_v120_signal,
    f21ac_f21_asset_composition_fixwork_relmean_126d_slope_v121_signal,
    f21ac_f21_asset_composition_invreal_relmean_189d_slope_v122_signal,
    f21ac_f21_asset_composition_investnoncur_relmean_63d_slope_v123_signal,
    f21ac_f21_asset_composition_softhardbal_relmean_42d_slope_v124_signal,
    f21ac_f21_asset_composition_gwvstang_relmean_168d_slope_v125_signal,
    f21ac_f21_asset_composition_intangsh_relema_105d_slope_v126_signal,
    f21ac_f21_asset_composition_tangsh_relema_126d_slope_v127_signal,
    f21ac_f21_asset_composition_capint_relema_189d_slope_v128_signal,
    f21ac_f21_asset_composition_invsh_relema_63d_slope_v129_signal,
    f21ac_f21_asset_composition_investsh_relema_42d_slope_v130_signal,
    f21ac_f21_asset_composition_gwproxy_relema_168d_slope_v131_signal,
    f21ac_f21_asset_composition_assetlight_relema_252d_slope_v132_signal,
    f21ac_f21_asset_composition_inttangbal_relema_105d_slope_v133_signal,
    f21ac_f21_asset_composition_hardcover_relema_126d_slope_v134_signal,
    f21ac_f21_asset_composition_workplant_relema_189d_slope_v135_signal,
    f21ac_f21_asset_composition_prodsh_relema_63d_slope_v136_signal,
    f21ac_f21_asset_composition_softsh_relema_42d_slope_v137_signal,
    f21ac_f21_asset_composition_realsh_relema_168d_slope_v138_signal,
    f21ac_f21_asset_composition_intppne_relema_252d_slope_v139_signal,
    f21ac_f21_asset_composition_investtang_relema_105d_slope_v140_signal,
    f21ac_f21_asset_composition_invinvest_relema_126d_slope_v141_signal,
    f21ac_f21_asset_composition_coresh_relema_189d_slope_v142_signal,
    f21ac_f21_asset_composition_intprod_relema_63d_slope_v143_signal,
    f21ac_f21_asset_composition_plantint_relema_42d_slope_v144_signal,
    f21ac_f21_asset_composition_deploysh_relema_168d_slope_v145_signal,
    f21ac_f21_asset_composition_fixwork_relema_252d_slope_v146_signal,
    f21ac_f21_asset_composition_invreal_relema_105d_slope_v147_signal,
    f21ac_f21_asset_composition_investnoncur_relema_126d_slope_v148_signal,
    f21ac_f21_asset_composition_softhardbal_relema_189d_slope_v149_signal,
    f21ac_f21_asset_composition_gwvstang_relema_63d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F21_ASSET_COMPOSITION_REGISTRY_001_150 = REGISTRY


def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False, n=1500):
    g = np.random.default_rng(seed)
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.3
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500  # noqa

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

    assert n_features == 150, n_features
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

    print("OK f21_asset_composition_2nd_derivatives_001_150_claude.py: %d features pass" % n_features)
