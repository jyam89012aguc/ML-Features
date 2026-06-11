import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5

HURDLE = 0.08


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


def _spread(roic):
    return roic - HURDLE


def _aturn(revenue, assets):
    return revenue / assets.replace(0, np.nan)


def _eturn(revenue, equity):
    return revenue / equity.replace(0, np.nan)


def _icturn(revenue, invcap):
    return revenue / invcap.replace(0, np.nan)


def _disp3(a, b, c):
    return pd.concat([a, b, c], axis=1).std(axis=1)


def _comp3(a, b, c):
    return (a + b + c) / 3.0



def f35ce_f35_capital_efficiency_returns_roiclvls_63d_slope_v001_signal(roic):
    core = _mean(roic, 63)
    base = core
    d1 = base - base.shift(5)
    result = d1 / float(5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roiclvlm_63d_slope_v002_signal(roic):
    core = _mean(roic, 63)
    base = _z(core, 63)
    d1 = base - base.shift(16)
    result = d1 / float(16)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roiclvll_63d_slope_v003_signal(roic):
    core = _mean(roic, 63)
    base = core - core.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d1 = base - base.shift(42)
    result = d1 / float(42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roalvls_63d_slope_v004_signal(roa):
    core = _mean(roa, 63)
    base = core
    d1 = base - base.shift(5)
    result = d1 / float(5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roalvlm_63d_slope_v005_signal(roa):
    core = _mean(roa, 63)
    base = _z(core, 63)
    d1 = base - base.shift(16)
    result = d1 / float(16)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roalvll_63d_slope_v006_signal(roa):
    core = _mean(roa, 63)
    base = core - core.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d1 = base - base.shift(42)
    result = d1 / float(42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roslvls_63d_slope_v007_signal(ros):
    core = _mean(ros, 63)
    base = core
    d1 = base - base.shift(5)
    result = d1 / float(5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roslvlm_63d_slope_v008_signal(ros):
    core = _mean(ros, 63)
    base = _z(core, 63)
    d1 = base - base.shift(16)
    result = d1 / float(16)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roslvll_63d_slope_v009_signal(ros):
    core = _mean(ros, 63)
    base = core - core.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d1 = base - base.shift(42)
    result = d1 / float(42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_spreadshs_126d_slope_v010_signal(roic):
    core = _mean(_spread(roic), 126) / _std(roic, 126).replace(0, np.nan)
    base = core
    d1 = base - base.shift(10)
    result = d1 / float(10)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_spreadshm_126d_slope_v011_signal(roic):
    core = _mean(_spread(roic), 126) / _std(roic, 126).replace(0, np.nan)
    base = _z(core, 126)
    d1 = base - base.shift(32)
    result = d1 / float(32)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_spreadshl_126d_slope_v012_signal(roic):
    core = _mean(_spread(roic), 126) / _std(roic, 126).replace(0, np.nan)
    base = core - core.ewm(span=126, min_periods=max(2, 126 // 3)).mean()
    d1 = base - base.shift(63)
    result = d1 / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roiczs_252d_slope_v013_signal(roic):
    core = _z(roic, 252)
    base = core
    d1 = base - base.shift(21)
    result = d1 / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roiczm_252d_slope_v014_signal(roic):
    core = _z(roic, 252)
    base = _z(core, 252)
    d1 = base - base.shift(63)
    result = d1 / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roiczl_252d_slope_v015_signal(roic):
    core = _z(roic, 252)
    base = core - core.ewm(span=252, min_periods=max(2, 252 // 3)).mean()
    d1 = base - base.shift(126)
    result = d1 / float(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roazs_252d_slope_v016_signal(roa):
    core = _z(roa, 252)
    base = core
    d1 = base - base.shift(21)
    result = d1 / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roazm_252d_slope_v017_signal(roa):
    core = _z(roa, 252)
    base = _z(core, 252)
    d1 = base - base.shift(63)
    result = d1 / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roazl_252d_slope_v018_signal(roa):
    core = _z(roa, 252)
    base = core - core.ewm(span=252, min_periods=max(2, 252 // 3)).mean()
    d1 = base - base.shift(126)
    result = d1 / float(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roszs_252d_slope_v019_signal(ros):
    core = _z(ros, 252)
    base = core
    d1 = base - base.shift(21)
    result = d1 / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roszm_252d_slope_v020_signal(ros):
    core = _z(ros, 252)
    base = _z(core, 252)
    d1 = base - base.shift(63)
    result = d1 / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roszl_252d_slope_v021_signal(ros):
    core = _z(ros, 252)
    base = core - core.ewm(span=252, min_periods=max(2, 252 // 3)).mean()
    d1 = base - base.shift(126)
    result = d1 / float(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_aturnlvls_63d_slope_v022_signal(revenue, assets):
    core = _mean(_aturn(revenue, assets), 63)
    base = core
    d1 = base - base.shift(5)
    result = d1 / float(5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_aturnlvlm_63d_slope_v023_signal(revenue, assets):
    core = _mean(_aturn(revenue, assets), 63)
    base = _z(core, 63)
    d1 = base - base.shift(16)
    result = d1 / float(16)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_aturnlvll_63d_slope_v024_signal(revenue, assets):
    core = _mean(_aturn(revenue, assets), 63)
    base = core - core.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d1 = base - base.shift(42)
    result = d1 / float(42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_aturnreps_63d_slope_v025_signal(assetturnover):
    core = _mean(assetturnover, 63)
    base = core
    d1 = base - base.shift(5)
    result = d1 / float(5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_aturnrepm_63d_slope_v026_signal(assetturnover):
    core = _mean(assetturnover, 63)
    base = _z(core, 63)
    d1 = base - base.shift(16)
    result = d1 / float(16)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_aturnrepl_63d_slope_v027_signal(assetturnover):
    core = _mean(assetturnover, 63)
    base = core - core.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d1 = base - base.shift(42)
    result = d1 / float(42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_eturnlvls_63d_slope_v028_signal(revenue, equity):
    core = _mean(_eturn(revenue, equity), 63)
    base = core
    d1 = base - base.shift(5)
    result = d1 / float(5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_eturnlvlm_63d_slope_v029_signal(revenue, equity):
    core = _mean(_eturn(revenue, equity), 63)
    base = _z(core, 63)
    d1 = base - base.shift(16)
    result = d1 / float(16)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_eturnlvll_63d_slope_v030_signal(revenue, equity):
    core = _mean(_eturn(revenue, equity), 63)
    base = core - core.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d1 = base - base.shift(42)
    result = d1 / float(42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_icturnlvls_63d_slope_v031_signal(revenue, invcap):
    core = _mean(_icturn(revenue, invcap), 63)
    base = core
    d1 = base - base.shift(5)
    result = d1 / float(5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_icturnlvlm_63d_slope_v032_signal(revenue, invcap):
    core = _mean(_icturn(revenue, invcap), 63)
    base = _z(core, 63)
    d1 = base - base.shift(16)
    result = d1 / float(16)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_icturnlvll_63d_slope_v033_signal(revenue, invcap):
    core = _mean(_icturn(revenue, invcap), 63)
    base = core - core.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d1 = base - base.shift(42)
    result = d1 / float(42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_retdisps_63d_slope_v034_signal(roic, roa, ros):
    core = _mean(_disp3(roic, roa, ros), 63)
    base = core
    d1 = base - base.shift(5)
    result = d1 / float(5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_retdispm_63d_slope_v035_signal(roic, roa, ros):
    core = _mean(_disp3(roic, roa, ros), 63)
    base = _z(core, 63)
    d1 = base - base.shift(16)
    result = d1 / float(16)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_retdispl_63d_slope_v036_signal(roic, roa, ros):
    core = _mean(_disp3(roic, roa, ros), 63)
    base = core - core.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d1 = base - base.shift(42)
    result = d1 / float(42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roicroas_63d_slope_v037_signal(roic, roa):
    core = _mean(roic - roa, 63)
    base = core
    d1 = base - base.shift(5)
    result = d1 / float(5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roicroam_63d_slope_v038_signal(roic, roa):
    core = _mean(roic - roa, 63)
    base = _z(core, 63)
    d1 = base - base.shift(16)
    result = d1 / float(16)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roicroal_63d_slope_v039_signal(roic, roa):
    core = _mean(roic - roa, 63)
    base = core - core.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d1 = base - base.shift(42)
    result = d1 / float(42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roaross_63d_slope_v040_signal(roa, ros):
    core = _mean(roa - ros, 63)
    base = core
    d1 = base - base.shift(5)
    result = d1 / float(5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roarosm_63d_slope_v041_signal(roa, ros):
    core = _mean(roa - ros, 63)
    base = _z(core, 63)
    d1 = base - base.shift(16)
    result = d1 / float(16)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roarosl_63d_slope_v042_signal(roa, ros):
    core = _mean(roa - ros, 63)
    base = core - core.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d1 = base - base.shift(42)
    result = d1 / float(42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roicross_63d_slope_v043_signal(roic, ros):
    core = _mean(roic - ros, 63)
    base = core
    d1 = base - base.shift(5)
    result = d1 / float(5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roicrosm_63d_slope_v044_signal(roic, ros):
    core = _mean(roic - ros, 63)
    base = _z(core, 63)
    d1 = base - base.shift(16)
    result = d1 / float(16)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roicrosl_63d_slope_v045_signal(roic, ros):
    core = _mean(roic - ros, 63)
    base = core - core.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d1 = base - base.shift(42)
    result = d1 / float(42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_retcomps_63d_slope_v046_signal(roic, roa, ros):
    core = _mean(_comp3(roic, roa, ros), 63)
    base = core
    d1 = base - base.shift(5)
    result = d1 / float(5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_retcompm_63d_slope_v047_signal(roic, roa, ros):
    core = _mean(_comp3(roic, roa, ros), 63)
    base = _z(core, 63)
    d1 = base - base.shift(16)
    result = d1 / float(16)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_retcompl_63d_slope_v048_signal(roic, roa, ros):
    core = _mean(_comp3(roic, roa, ros), 63)
    base = core - core.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d1 = base - base.shift(42)
    result = d1 / float(42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_leverages_63d_slope_v049_signal(assets, equity):
    core = _mean(assets / equity.replace(0, np.nan), 63)
    base = core
    d1 = base - base.shift(5)
    result = d1 / float(5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_leveragem_63d_slope_v050_signal(assets, equity):
    core = _mean(assets / equity.replace(0, np.nan), 63)
    base = _z(core, 63)
    d1 = base - base.shift(16)
    result = d1 / float(16)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_leveragel_63d_slope_v051_signal(assets, equity):
    core = _mean(assets / equity.replace(0, np.nan), 63)
    base = core - core.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d1 = base - base.shift(42)
    result = d1 / float(42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_invcapscales_126d_slope_v052_signal(invcap):
    core = np.log(invcap.replace(0, np.nan)).rolling(126, min_periods=max(1, 126 // 2)).mean()
    base = core
    d1 = base - base.shift(10)
    result = d1 / float(10)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_invcapscalem_126d_slope_v053_signal(invcap):
    core = np.log(invcap.replace(0, np.nan)).rolling(126, min_periods=max(1, 126 // 2)).mean()
    base = _z(core, 126)
    d1 = base - base.shift(32)
    result = d1 / float(32)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_invcapscalel_126d_slope_v054_signal(invcap):
    core = np.log(invcap.replace(0, np.nan)).rolling(126, min_periods=max(1, 126 // 2)).mean()
    base = core - core.ewm(span=126, min_periods=max(2, 126 // 3)).mean()
    d1 = base - base.shift(63)
    result = d1 / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_equityscales_126d_slope_v055_signal(equity):
    core = np.log(equity.replace(0, np.nan)).rolling(126, min_periods=max(1, 126 // 2)).mean()
    base = core
    d1 = base - base.shift(10)
    result = d1 / float(10)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_equityscalem_126d_slope_v056_signal(equity):
    core = np.log(equity.replace(0, np.nan)).rolling(126, min_periods=max(1, 126 // 2)).mean()
    base = _z(core, 126)
    d1 = base - base.shift(32)
    result = d1 / float(32)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_equityscalel_126d_slope_v057_signal(equity):
    core = np.log(equity.replace(0, np.nan)).rolling(126, min_periods=max(1, 126 // 2)).mean()
    base = core - core.ewm(span=126, min_periods=max(2, 126 // 3)).mean()
    d1 = base - base.shift(63)
    result = d1 / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_revscales_126d_slope_v058_signal(revenue):
    core = np.log(revenue.replace(0, np.nan)).rolling(126, min_periods=max(1, 126 // 2)).mean()
    base = core
    d1 = base - base.shift(10)
    result = d1 / float(10)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_revscalem_126d_slope_v059_signal(revenue):
    core = np.log(revenue.replace(0, np.nan)).rolling(126, min_periods=max(1, 126 // 2)).mean()
    base = _z(core, 126)
    d1 = base - base.shift(32)
    result = d1 / float(32)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_revscalel_126d_slope_v060_signal(revenue):
    core = np.log(revenue.replace(0, np.nan)).rolling(126, min_periods=max(1, 126 // 2)).mean()
    base = core - core.ewm(span=126, min_periods=max(2, 126 // 3)).mean()
    d1 = base - base.shift(63)
    result = d1 / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_aturnzs_252d_slope_v061_signal(assetturnover):
    core = _z(assetturnover, 252)
    base = core
    d1 = base - base.shift(21)
    result = d1 / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_aturnzm_252d_slope_v062_signal(assetturnover):
    core = _z(assetturnover, 252)
    base = _z(core, 252)
    d1 = base - base.shift(63)
    result = d1 / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_aturnzl_252d_slope_v063_signal(assetturnover):
    core = _z(assetturnover, 252)
    base = core - core.ewm(span=252, min_periods=max(2, 252 // 3)).mean()
    d1 = base - base.shift(126)
    result = d1 / float(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_eturnzs_252d_slope_v064_signal(revenue, equity):
    core = _z(_eturn(revenue, equity), 252)
    base = core
    d1 = base - base.shift(21)
    result = d1 / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_eturnzm_252d_slope_v065_signal(revenue, equity):
    core = _z(_eturn(revenue, equity), 252)
    base = _z(core, 252)
    d1 = base - base.shift(63)
    result = d1 / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_eturnzl_252d_slope_v066_signal(revenue, equity):
    core = _z(_eturn(revenue, equity), 252)
    base = core - core.ewm(span=252, min_periods=max(2, 252 // 3)).mean()
    d1 = base - base.shift(126)
    result = d1 / float(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_icturnzs_252d_slope_v067_signal(revenue, invcap):
    core = _z(_icturn(revenue, invcap), 252)
    base = core
    d1 = base - base.shift(21)
    result = d1 / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_icturnzm_252d_slope_v068_signal(revenue, invcap):
    core = _z(_icturn(revenue, invcap), 252)
    base = _z(core, 252)
    d1 = base - base.shift(63)
    result = d1 / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_icturnzl_252d_slope_v069_signal(revenue, invcap):
    core = _z(_icturn(revenue, invcap), 252)
    base = core - core.ewm(span=252, min_periods=max(2, 252 // 3)).mean()
    d1 = base - base.shift(126)
    result = d1 / float(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_assetscales_126d_slope_v070_signal(assets):
    core = np.log(assets.replace(0, np.nan)).rolling(126, min_periods=max(1, 126 // 2)).mean()
    base = core
    d1 = base - base.shift(10)
    result = d1 / float(10)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_assetscalem_126d_slope_v071_signal(assets):
    core = np.log(assets.replace(0, np.nan)).rolling(126, min_periods=max(1, 126 // 2)).mean()
    base = _z(core, 126)
    d1 = base - base.shift(32)
    result = d1 / float(32)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_assetscalel_126d_slope_v072_signal(assets):
    core = np.log(assets.replace(0, np.nan)).rolling(126, min_periods=max(1, 126 // 2)).mean()
    base = core - core.ewm(span=126, min_periods=max(2, 126 // 3)).mean()
    d1 = base - base.shift(63)
    result = d1 / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_aturnvols_63d_slope_v073_signal(assetturnover):
    core = _std(assetturnover, 63)
    base = core
    d1 = base - base.shift(5)
    result = d1 / float(5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_aturnvolm_63d_slope_v074_signal(assetturnover):
    core = _std(assetturnover, 63)
    base = _z(core, 63)
    d1 = base - base.shift(16)
    result = d1 / float(16)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_aturnvoll_63d_slope_v075_signal(assetturnover):
    core = _std(assetturnover, 63)
    base = core - core.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d1 = base - base.shift(42)
    result = d1 / float(42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_rosaturngaps_63d_slope_v076_signal(ros, assetturnover):
    core = _mean(_z(ros, 63) - _z(assetturnover, 63), 63)
    base = core
    d1 = base - base.shift(5)
    result = d1 / float(5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_rosaturngapm_63d_slope_v077_signal(ros, assetturnover):
    core = _mean(_z(ros, 63) - _z(assetturnover, 63), 63)
    base = _z(core, 63)
    d1 = base - base.shift(16)
    result = d1 / float(16)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_rosaturngapl_63d_slope_v078_signal(ros, assetturnover):
    core = _mean(_z(ros, 63) - _z(assetturnover, 63), 63)
    base = core - core.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d1 = base - base.shift(42)
    result = d1 / float(42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_rosroagaps_63d_slope_v079_signal(ros, roa):
    core = _mean((ros - roa).abs(), 63)
    base = core
    d1 = base - base.shift(5)
    result = d1 / float(5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_rosroagapm_63d_slope_v080_signal(ros, roa):
    core = _mean((ros - roa).abs(), 63)
    base = _z(core, 63)
    d1 = base - base.shift(16)
    result = d1 / float(16)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_rosroagapl_63d_slope_v081_signal(ros, roa):
    core = _mean((ros - roa).abs(), 63)
    base = core - core.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d1 = base - base.shift(42)
    result = d1 / float(42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_compstabs_126d_slope_v082_signal(roic, roa, ros):
    core = _mean(_comp3(roic, roa, ros), 126) / _std(_comp3(roic, roa, ros), 126).replace(0, np.nan)
    base = core
    d1 = base - base.shift(10)
    result = d1 / float(10)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_compstabm_126d_slope_v083_signal(roic, roa, ros):
    core = _mean(_comp3(roic, roa, ros), 126) / _std(_comp3(roic, roa, ros), 126).replace(0, np.nan)
    base = _z(core, 126)
    d1 = base - base.shift(32)
    result = d1 / float(32)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_compstabl_126d_slope_v084_signal(roic, roa, ros):
    core = _mean(_comp3(roic, roa, ros), 126) / _std(_comp3(roic, roa, ros), 126).replace(0, np.nan)
    base = core - core.ewm(span=126, min_periods=max(2, 126 // 3)).mean()
    d1 = base - base.shift(63)
    result = d1 / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roicstabs_126d_slope_v085_signal(roic):
    core = _mean(roic, 126) / _std(roic, 126).replace(0, np.nan)
    base = core
    d1 = base - base.shift(10)
    result = d1 / float(10)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roicstabm_126d_slope_v086_signal(roic):
    core = _mean(roic, 126) / _std(roic, 126).replace(0, np.nan)
    base = _z(core, 126)
    d1 = base - base.shift(32)
    result = d1 / float(32)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roicstabl_126d_slope_v087_signal(roic):
    core = _mean(roic, 126) / _std(roic, 126).replace(0, np.nan)
    base = core - core.ewm(span=126, min_periods=max(2, 126 // 3)).mean()
    d1 = base - base.shift(63)
    result = d1 / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_rosstabs_126d_slope_v088_signal(ros):
    core = _mean(ros, 126) / _std(ros, 126).replace(0, np.nan)
    base = core
    d1 = base - base.shift(10)
    result = d1 / float(10)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_rosstabm_126d_slope_v089_signal(ros):
    core = _mean(ros, 126) / _std(ros, 126).replace(0, np.nan)
    base = _z(core, 126)
    d1 = base - base.shift(32)
    result = d1 / float(32)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_rosstabl_126d_slope_v090_signal(ros):
    core = _mean(ros, 126) / _std(ros, 126).replace(0, np.nan)
    base = core - core.ewm(span=126, min_periods=max(2, 126 // 3)).mean()
    d1 = base - base.shift(63)
    result = d1 / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_icintensitys_126d_slope_v091_signal(invcap, assets):
    core = _mean(invcap / assets.replace(0, np.nan), 126)
    base = core
    d1 = base - base.shift(10)
    result = d1 / float(10)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_icintensitym_126d_slope_v092_signal(invcap, assets):
    core = _mean(invcap / assets.replace(0, np.nan), 126)
    base = _z(core, 126)
    d1 = base - base.shift(32)
    result = d1 / float(32)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_icintensityl_126d_slope_v093_signal(invcap, assets):
    core = _mean(invcap / assets.replace(0, np.nan), 126)
    base = core - core.ewm(span=126, min_periods=max(2, 126 // 3)).mean()
    d1 = base - base.shift(63)
    result = d1 / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_turnratios_63d_slope_v094_signal(assetturnover, revenue, equity):
    core = _mean(assetturnover / _eturn(revenue, equity).replace(0, np.nan), 63)
    base = core
    d1 = base - base.shift(5)
    result = d1 / float(5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_turnratiom_63d_slope_v095_signal(assetturnover, revenue, equity):
    core = _mean(assetturnover / _eturn(revenue, equity).replace(0, np.nan), 63)
    base = _z(core, 63)
    d1 = base - base.shift(16)
    result = d1 / float(16)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_turnratiol_63d_slope_v096_signal(assetturnover, revenue, equity):
    core = _mean(assetturnover / _eturn(revenue, equity).replace(0, np.nan), 63)
    base = core - core.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d1 = base - base.shift(42)
    result = d1 / float(42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_invcapgs_252d_slope_v097_signal(invcap):
    core = invcap / invcap.shift(252).replace(0, np.nan) - 1.0
    base = core
    d1 = base - base.shift(21)
    result = d1 / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_invcapgm_252d_slope_v098_signal(invcap):
    core = invcap / invcap.shift(252).replace(0, np.nan) - 1.0
    base = _z(core, 252)
    d1 = base - base.shift(63)
    result = d1 / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_invcapgl_252d_slope_v099_signal(invcap):
    core = invcap / invcap.shift(252).replace(0, np.nan) - 1.0
    base = core - core.ewm(span=252, min_periods=max(2, 252 // 3)).mean()
    d1 = base - base.shift(126)
    result = d1 / float(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_amplifys_63d_slope_v100_signal(roic, roa, assets, equity):
    core = _mean(roic * (assets / equity.replace(0, np.nan)) - roa, 63)
    base = core
    d1 = base - base.shift(5)
    result = d1 / float(5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_amplifym_63d_slope_v101_signal(roic, roa, assets, equity):
    core = _mean(roic * (assets / equity.replace(0, np.nan)) - roa, 63)
    base = _z(core, 63)
    d1 = base - base.shift(16)
    result = d1 / float(16)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_amplifyl_63d_slope_v102_signal(roic, roa, assets, equity):
    core = _mean(roic * (assets / equity.replace(0, np.nan)) - roa, 63)
    base = core - core.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d1 = base - base.shift(42)
    result = d1 / float(42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_equitygs_252d_slope_v103_signal(equity):
    core = equity / equity.shift(252).replace(0, np.nan) - 1.0
    base = core
    d1 = base - base.shift(21)
    result = d1 / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_equitygm_252d_slope_v104_signal(equity):
    core = equity / equity.shift(252).replace(0, np.nan) - 1.0
    base = _z(core, 252)
    d1 = base - base.shift(63)
    result = d1 / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_equitygl_252d_slope_v105_signal(equity):
    core = equity / equity.shift(252).replace(0, np.nan) - 1.0
    base = core - core.ewm(span=252, min_periods=max(2, 252 // 3)).mean()
    d1 = base - base.shift(126)
    result = d1 / float(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roaicturns_63d_slope_v106_signal(roa, revenue, invcap):
    core = _mean(roa * _icturn(revenue, invcap), 63)
    base = core
    d1 = base - base.shift(5)
    result = d1 / float(5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roaicturnm_63d_slope_v107_signal(roa, revenue, invcap):
    core = _mean(roa * _icturn(revenue, invcap), 63)
    base = _z(core, 63)
    d1 = base - base.shift(16)
    result = d1 / float(16)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roaicturnl_63d_slope_v108_signal(roa, revenue, invcap):
    core = _mean(roa * _icturn(revenue, invcap), 63)
    base = core - core.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d1 = base - base.shift(42)
    result = d1 / float(42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_retmins_63d_slope_v109_signal(roic, roa, ros):
    core = _mean(pd.concat([roic, roa, ros], axis=1).min(axis=1), 63)
    base = core
    d1 = base - base.shift(5)
    result = d1 / float(5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_retminm_63d_slope_v110_signal(roic, roa, ros):
    core = _mean(pd.concat([roic, roa, ros], axis=1).min(axis=1), 63)
    base = _z(core, 63)
    d1 = base - base.shift(16)
    result = d1 / float(16)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_retminl_63d_slope_v111_signal(roic, roa, ros):
    core = _mean(pd.concat([roic, roa, ros], axis=1).min(axis=1), 63)
    base = core - core.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d1 = base - base.shift(42)
    result = d1 / float(42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_retmaxs_63d_slope_v112_signal(roic, roa, ros):
    core = _mean(pd.concat([roic, roa, ros], axis=1).max(axis=1), 63)
    base = core
    d1 = base - base.shift(5)
    result = d1 / float(5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_retmaxm_63d_slope_v113_signal(roic, roa, ros):
    core = _mean(pd.concat([roic, roa, ros], axis=1).max(axis=1), 63)
    base = _z(core, 63)
    d1 = base - base.shift(16)
    result = d1 / float(16)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_retmaxl_63d_slope_v114_signal(roic, roa, ros):
    core = _mean(pd.concat([roic, roa, ros], axis=1).max(axis=1), 63)
    base = core - core.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d1 = base - base.shift(42)
    result = d1 / float(42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_retmeds_63d_slope_v115_signal(roic, roa, ros):
    core = _mean(pd.concat([roic, roa, ros], axis=1).median(axis=1), 63)
    base = core
    d1 = base - base.shift(5)
    result = d1 / float(5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_retmedm_63d_slope_v116_signal(roic, roa, ros):
    core = _mean(pd.concat([roic, roa, ros], axis=1).median(axis=1), 63)
    base = _z(core, 63)
    d1 = base - base.shift(16)
    result = d1 / float(16)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_retmedl_63d_slope_v117_signal(roic, roa, ros):
    core = _mean(pd.concat([roic, roa, ros], axis=1).median(axis=1), 63)
    base = core - core.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d1 = base - base.shift(42)
    result = d1 / float(42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_eturnicgaps_63d_slope_v118_signal(revenue, equity, invcap):
    core = _mean(_eturn(revenue, equity) - _icturn(revenue, invcap), 63)
    base = core
    d1 = base - base.shift(5)
    result = d1 / float(5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_eturnicgapm_63d_slope_v119_signal(revenue, equity, invcap):
    core = _mean(_eturn(revenue, equity) - _icturn(revenue, invcap), 63)
    base = _z(core, 63)
    d1 = base - base.shift(16)
    result = d1 / float(16)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_eturnicgapl_63d_slope_v120_signal(revenue, equity, invcap):
    core = _mean(_eturn(revenue, equity) - _icturn(revenue, invcap), 63)
    base = core - core.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d1 = base - base.shift(42)
    result = d1 / float(42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_turngaps_63d_slope_v121_signal(revenue, equity, assets):
    core = _mean(_eturn(revenue, equity) - _aturn(revenue, assets), 63)
    base = core
    d1 = base - base.shift(5)
    result = d1 / float(5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_turngapm_63d_slope_v122_signal(revenue, equity, assets):
    core = _mean(_eturn(revenue, equity) - _aturn(revenue, assets), 63)
    base = _z(core, 63)
    d1 = base - base.shift(16)
    result = d1 / float(16)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_turngapl_63d_slope_v123_signal(revenue, equity, assets):
    core = _mean(_eturn(revenue, equity) - _aturn(revenue, assets), 63)
    base = core - core.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d1 = base - base.shift(42)
    result = d1 / float(42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_icassetgaps_63d_slope_v124_signal(revenue, invcap, assets):
    core = _mean(_icturn(revenue, invcap) - _aturn(revenue, assets), 63)
    base = core
    d1 = base - base.shift(5)
    result = d1 / float(5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_icassetgapm_63d_slope_v125_signal(revenue, invcap, assets):
    core = _mean(_icturn(revenue, invcap) - _aturn(revenue, assets), 63)
    base = _z(core, 63)
    d1 = base - base.shift(16)
    result = d1 / float(16)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_icassetgapl_63d_slope_v126_signal(revenue, invcap, assets):
    core = _mean(_icturn(revenue, invcap) - _aturn(revenue, assets), 63)
    base = core - core.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d1 = base - base.shift(42)
    result = d1 / float(42)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_marginlevers_252d_slope_v127_signal(ros, assetturnover):
    core = _z(ros, 252) - _z(assetturnover, 252)
    base = core
    d1 = base - base.shift(21)
    result = d1 / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_marginleverm_252d_slope_v128_signal(ros, assetturnover):
    core = _z(ros, 252) - _z(assetturnover, 252)
    base = _z(core, 252)
    d1 = base - base.shift(63)
    result = d1 / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_marginleverl_252d_slope_v129_signal(ros, assetturnover):
    core = _z(ros, 252) - _z(assetturnover, 252)
    base = core - core.ewm(span=252, min_periods=max(2, 252 // 3)).mean()
    d1 = base - base.shift(126)
    result = d1 / float(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roiccovs_126d_slope_v130_signal(roic):
    core = _std(roic, 126) / _mean(roic, 126).abs().replace(0, np.nan)
    base = core
    d1 = base - base.shift(10)
    result = d1 / float(10)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roiccovm_126d_slope_v131_signal(roic):
    core = _std(roic, 126) / _mean(roic, 126).abs().replace(0, np.nan)
    base = _z(core, 126)
    d1 = base - base.shift(32)
    result = d1 / float(32)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roiccovl_126d_slope_v132_signal(roic):
    core = _std(roic, 126) / _mean(roic, 126).abs().replace(0, np.nan)
    base = core - core.ewm(span=126, min_periods=max(2, 126 // 3)).mean()
    d1 = base - base.shift(63)
    result = d1 / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_epscales_126d_slope_v133_signal(roic, invcap):
    core = (_spread(roic) * invcap)
    core = np.sign(core) * np.log1p(core.abs())
    core = _mean(core, 126)
    base = core
    d1 = base - base.shift(10)
    result = d1 / float(10)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_epscalem_126d_slope_v134_signal(roic, invcap):
    core = (_spread(roic) * invcap)
    core = np.sign(core) * np.log1p(core.abs())
    core = _mean(core, 126)
    base = _z(core, 126)
    d1 = base - base.shift(32)
    result = d1 / float(32)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_epscalel_126d_slope_v135_signal(roic, invcap):
    core = (_spread(roic) * invcap)
    core = np.sign(core) * np.log1p(core.abs())
    core = _mean(core, 126)
    base = core - core.ewm(span=126, min_periods=max(2, 126 // 3)).mean()
    d1 = base - base.shift(63)
    result = d1 / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_dupontbals_252d_slope_v136_signal(assetturnover, ros):
    core = (_z(assetturnover, 252) - _z(ros, 252)) / (_z(assetturnover, 252).abs() + _z(ros, 252).abs()).replace(0, np.nan)
    base = core
    d1 = base - base.shift(21)
    result = d1 / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_dupontbalm_252d_slope_v137_signal(assetturnover, ros):
    core = (_z(assetturnover, 252) - _z(ros, 252)) / (_z(assetturnover, 252).abs() + _z(ros, 252).abs()).replace(0, np.nan)
    base = _z(core, 252)
    d1 = base - base.shift(63)
    result = d1 / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_dupontball_252d_slope_v138_signal(assetturnover, ros):
    core = (_z(assetturnover, 252) - _z(ros, 252)) / (_z(assetturnover, 252).abs() + _z(ros, 252).abs()).replace(0, np.nan)
    base = core - core.ewm(span=252, min_periods=max(2, 252 // 3)).mean()
    d1 = base - base.shift(126)
    result = d1 / float(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roicroazs_252d_slope_v139_signal(roic, roa):
    core = _z(roic - roa, 252)
    base = core
    d1 = base - base.shift(21)
    result = d1 / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roicroazm_252d_slope_v140_signal(roic, roa):
    core = _z(roic - roa, 252)
    base = _z(core, 252)
    d1 = base - base.shift(63)
    result = d1 / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roicroazl_252d_slope_v141_signal(roic, roa):
    core = _z(roic - roa, 252)
    base = core - core.ewm(span=252, min_periods=max(2, 252 // 3)).mean()
    d1 = base - base.shift(126)
    result = d1 / float(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roaroszs_252d_slope_v142_signal(roa, ros):
    core = _z(roa - ros, 252)
    base = core
    d1 = base - base.shift(21)
    result = d1 / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roaroszm_252d_slope_v143_signal(roa, ros):
    core = _z(roa - ros, 252)
    base = _z(core, 252)
    d1 = base - base.shift(63)
    result = d1 / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roaroszl_252d_slope_v144_signal(roa, ros):
    core = _z(roa - ros, 252)
    base = core - core.ewm(span=252, min_periods=max(2, 252 // 3)).mean()
    d1 = base - base.shift(126)
    result = d1 / float(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roicroszs_252d_slope_v145_signal(roic, ros):
    core = _z(roic - ros, 252)
    base = core
    d1 = base - base.shift(21)
    result = d1 / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roicroszm_252d_slope_v146_signal(roic, ros):
    core = _z(roic - ros, 252)
    base = _z(core, 252)
    d1 = base - base.shift(63)
    result = d1 / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_roicroszl_252d_slope_v147_signal(roic, ros):
    core = _z(roic - ros, 252)
    base = core - core.ewm(span=252, min_periods=max(2, 252 // 3)).mean()
    d1 = base - base.shift(126)
    result = d1 / float(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_rosroaprods_63d_slope_v148_signal(ros, roa):
    core = _mean(ros * roa, 63)
    base = core
    d1 = base - base.shift(5)
    result = d1 / float(5)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_rosroaprodm_63d_slope_v149_signal(ros, roa):
    core = _mean(ros * roa, 63)
    base = _z(core, 63)
    d1 = base - base.shift(16)
    result = d1 / float(16)
    return result.replace([np.inf, -np.inf], np.nan)


def f35ce_f35_capital_efficiency_returns_rosroaprodl_63d_slope_v150_signal(ros, roa):
    core = _mean(ros * roa, 63)
    base = core - core.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d1 = base - base.shift(42)
    result = d1 / float(42)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f35ce_f35_capital_efficiency_returns_roiclvls_63d_slope_v001_signal,
    f35ce_f35_capital_efficiency_returns_roiclvlm_63d_slope_v002_signal,
    f35ce_f35_capital_efficiency_returns_roiclvll_63d_slope_v003_signal,
    f35ce_f35_capital_efficiency_returns_roalvls_63d_slope_v004_signal,
    f35ce_f35_capital_efficiency_returns_roalvlm_63d_slope_v005_signal,
    f35ce_f35_capital_efficiency_returns_roalvll_63d_slope_v006_signal,
    f35ce_f35_capital_efficiency_returns_roslvls_63d_slope_v007_signal,
    f35ce_f35_capital_efficiency_returns_roslvlm_63d_slope_v008_signal,
    f35ce_f35_capital_efficiency_returns_roslvll_63d_slope_v009_signal,
    f35ce_f35_capital_efficiency_returns_spreadshs_126d_slope_v010_signal,
    f35ce_f35_capital_efficiency_returns_spreadshm_126d_slope_v011_signal,
    f35ce_f35_capital_efficiency_returns_spreadshl_126d_slope_v012_signal,
    f35ce_f35_capital_efficiency_returns_roiczs_252d_slope_v013_signal,
    f35ce_f35_capital_efficiency_returns_roiczm_252d_slope_v014_signal,
    f35ce_f35_capital_efficiency_returns_roiczl_252d_slope_v015_signal,
    f35ce_f35_capital_efficiency_returns_roazs_252d_slope_v016_signal,
    f35ce_f35_capital_efficiency_returns_roazm_252d_slope_v017_signal,
    f35ce_f35_capital_efficiency_returns_roazl_252d_slope_v018_signal,
    f35ce_f35_capital_efficiency_returns_roszs_252d_slope_v019_signal,
    f35ce_f35_capital_efficiency_returns_roszm_252d_slope_v020_signal,
    f35ce_f35_capital_efficiency_returns_roszl_252d_slope_v021_signal,
    f35ce_f35_capital_efficiency_returns_aturnlvls_63d_slope_v022_signal,
    f35ce_f35_capital_efficiency_returns_aturnlvlm_63d_slope_v023_signal,
    f35ce_f35_capital_efficiency_returns_aturnlvll_63d_slope_v024_signal,
    f35ce_f35_capital_efficiency_returns_aturnreps_63d_slope_v025_signal,
    f35ce_f35_capital_efficiency_returns_aturnrepm_63d_slope_v026_signal,
    f35ce_f35_capital_efficiency_returns_aturnrepl_63d_slope_v027_signal,
    f35ce_f35_capital_efficiency_returns_eturnlvls_63d_slope_v028_signal,
    f35ce_f35_capital_efficiency_returns_eturnlvlm_63d_slope_v029_signal,
    f35ce_f35_capital_efficiency_returns_eturnlvll_63d_slope_v030_signal,
    f35ce_f35_capital_efficiency_returns_icturnlvls_63d_slope_v031_signal,
    f35ce_f35_capital_efficiency_returns_icturnlvlm_63d_slope_v032_signal,
    f35ce_f35_capital_efficiency_returns_icturnlvll_63d_slope_v033_signal,
    f35ce_f35_capital_efficiency_returns_retdisps_63d_slope_v034_signal,
    f35ce_f35_capital_efficiency_returns_retdispm_63d_slope_v035_signal,
    f35ce_f35_capital_efficiency_returns_retdispl_63d_slope_v036_signal,
    f35ce_f35_capital_efficiency_returns_roicroas_63d_slope_v037_signal,
    f35ce_f35_capital_efficiency_returns_roicroam_63d_slope_v038_signal,
    f35ce_f35_capital_efficiency_returns_roicroal_63d_slope_v039_signal,
    f35ce_f35_capital_efficiency_returns_roaross_63d_slope_v040_signal,
    f35ce_f35_capital_efficiency_returns_roarosm_63d_slope_v041_signal,
    f35ce_f35_capital_efficiency_returns_roarosl_63d_slope_v042_signal,
    f35ce_f35_capital_efficiency_returns_roicross_63d_slope_v043_signal,
    f35ce_f35_capital_efficiency_returns_roicrosm_63d_slope_v044_signal,
    f35ce_f35_capital_efficiency_returns_roicrosl_63d_slope_v045_signal,
    f35ce_f35_capital_efficiency_returns_retcomps_63d_slope_v046_signal,
    f35ce_f35_capital_efficiency_returns_retcompm_63d_slope_v047_signal,
    f35ce_f35_capital_efficiency_returns_retcompl_63d_slope_v048_signal,
    f35ce_f35_capital_efficiency_returns_leverages_63d_slope_v049_signal,
    f35ce_f35_capital_efficiency_returns_leveragem_63d_slope_v050_signal,
    f35ce_f35_capital_efficiency_returns_leveragel_63d_slope_v051_signal,
    f35ce_f35_capital_efficiency_returns_invcapscales_126d_slope_v052_signal,
    f35ce_f35_capital_efficiency_returns_invcapscalem_126d_slope_v053_signal,
    f35ce_f35_capital_efficiency_returns_invcapscalel_126d_slope_v054_signal,
    f35ce_f35_capital_efficiency_returns_equityscales_126d_slope_v055_signal,
    f35ce_f35_capital_efficiency_returns_equityscalem_126d_slope_v056_signal,
    f35ce_f35_capital_efficiency_returns_equityscalel_126d_slope_v057_signal,
    f35ce_f35_capital_efficiency_returns_revscales_126d_slope_v058_signal,
    f35ce_f35_capital_efficiency_returns_revscalem_126d_slope_v059_signal,
    f35ce_f35_capital_efficiency_returns_revscalel_126d_slope_v060_signal,
    f35ce_f35_capital_efficiency_returns_aturnzs_252d_slope_v061_signal,
    f35ce_f35_capital_efficiency_returns_aturnzm_252d_slope_v062_signal,
    f35ce_f35_capital_efficiency_returns_aturnzl_252d_slope_v063_signal,
    f35ce_f35_capital_efficiency_returns_eturnzs_252d_slope_v064_signal,
    f35ce_f35_capital_efficiency_returns_eturnzm_252d_slope_v065_signal,
    f35ce_f35_capital_efficiency_returns_eturnzl_252d_slope_v066_signal,
    f35ce_f35_capital_efficiency_returns_icturnzs_252d_slope_v067_signal,
    f35ce_f35_capital_efficiency_returns_icturnzm_252d_slope_v068_signal,
    f35ce_f35_capital_efficiency_returns_icturnzl_252d_slope_v069_signal,
    f35ce_f35_capital_efficiency_returns_assetscales_126d_slope_v070_signal,
    f35ce_f35_capital_efficiency_returns_assetscalem_126d_slope_v071_signal,
    f35ce_f35_capital_efficiency_returns_assetscalel_126d_slope_v072_signal,
    f35ce_f35_capital_efficiency_returns_aturnvols_63d_slope_v073_signal,
    f35ce_f35_capital_efficiency_returns_aturnvolm_63d_slope_v074_signal,
    f35ce_f35_capital_efficiency_returns_aturnvoll_63d_slope_v075_signal,
    f35ce_f35_capital_efficiency_returns_rosaturngaps_63d_slope_v076_signal,
    f35ce_f35_capital_efficiency_returns_rosaturngapm_63d_slope_v077_signal,
    f35ce_f35_capital_efficiency_returns_rosaturngapl_63d_slope_v078_signal,
    f35ce_f35_capital_efficiency_returns_rosroagaps_63d_slope_v079_signal,
    f35ce_f35_capital_efficiency_returns_rosroagapm_63d_slope_v080_signal,
    f35ce_f35_capital_efficiency_returns_rosroagapl_63d_slope_v081_signal,
    f35ce_f35_capital_efficiency_returns_compstabs_126d_slope_v082_signal,
    f35ce_f35_capital_efficiency_returns_compstabm_126d_slope_v083_signal,
    f35ce_f35_capital_efficiency_returns_compstabl_126d_slope_v084_signal,
    f35ce_f35_capital_efficiency_returns_roicstabs_126d_slope_v085_signal,
    f35ce_f35_capital_efficiency_returns_roicstabm_126d_slope_v086_signal,
    f35ce_f35_capital_efficiency_returns_roicstabl_126d_slope_v087_signal,
    f35ce_f35_capital_efficiency_returns_rosstabs_126d_slope_v088_signal,
    f35ce_f35_capital_efficiency_returns_rosstabm_126d_slope_v089_signal,
    f35ce_f35_capital_efficiency_returns_rosstabl_126d_slope_v090_signal,
    f35ce_f35_capital_efficiency_returns_icintensitys_126d_slope_v091_signal,
    f35ce_f35_capital_efficiency_returns_icintensitym_126d_slope_v092_signal,
    f35ce_f35_capital_efficiency_returns_icintensityl_126d_slope_v093_signal,
    f35ce_f35_capital_efficiency_returns_turnratios_63d_slope_v094_signal,
    f35ce_f35_capital_efficiency_returns_turnratiom_63d_slope_v095_signal,
    f35ce_f35_capital_efficiency_returns_turnratiol_63d_slope_v096_signal,
    f35ce_f35_capital_efficiency_returns_invcapgs_252d_slope_v097_signal,
    f35ce_f35_capital_efficiency_returns_invcapgm_252d_slope_v098_signal,
    f35ce_f35_capital_efficiency_returns_invcapgl_252d_slope_v099_signal,
    f35ce_f35_capital_efficiency_returns_amplifys_63d_slope_v100_signal,
    f35ce_f35_capital_efficiency_returns_amplifym_63d_slope_v101_signal,
    f35ce_f35_capital_efficiency_returns_amplifyl_63d_slope_v102_signal,
    f35ce_f35_capital_efficiency_returns_equitygs_252d_slope_v103_signal,
    f35ce_f35_capital_efficiency_returns_equitygm_252d_slope_v104_signal,
    f35ce_f35_capital_efficiency_returns_equitygl_252d_slope_v105_signal,
    f35ce_f35_capital_efficiency_returns_roaicturns_63d_slope_v106_signal,
    f35ce_f35_capital_efficiency_returns_roaicturnm_63d_slope_v107_signal,
    f35ce_f35_capital_efficiency_returns_roaicturnl_63d_slope_v108_signal,
    f35ce_f35_capital_efficiency_returns_retmins_63d_slope_v109_signal,
    f35ce_f35_capital_efficiency_returns_retminm_63d_slope_v110_signal,
    f35ce_f35_capital_efficiency_returns_retminl_63d_slope_v111_signal,
    f35ce_f35_capital_efficiency_returns_retmaxs_63d_slope_v112_signal,
    f35ce_f35_capital_efficiency_returns_retmaxm_63d_slope_v113_signal,
    f35ce_f35_capital_efficiency_returns_retmaxl_63d_slope_v114_signal,
    f35ce_f35_capital_efficiency_returns_retmeds_63d_slope_v115_signal,
    f35ce_f35_capital_efficiency_returns_retmedm_63d_slope_v116_signal,
    f35ce_f35_capital_efficiency_returns_retmedl_63d_slope_v117_signal,
    f35ce_f35_capital_efficiency_returns_eturnicgaps_63d_slope_v118_signal,
    f35ce_f35_capital_efficiency_returns_eturnicgapm_63d_slope_v119_signal,
    f35ce_f35_capital_efficiency_returns_eturnicgapl_63d_slope_v120_signal,
    f35ce_f35_capital_efficiency_returns_turngaps_63d_slope_v121_signal,
    f35ce_f35_capital_efficiency_returns_turngapm_63d_slope_v122_signal,
    f35ce_f35_capital_efficiency_returns_turngapl_63d_slope_v123_signal,
    f35ce_f35_capital_efficiency_returns_icassetgaps_63d_slope_v124_signal,
    f35ce_f35_capital_efficiency_returns_icassetgapm_63d_slope_v125_signal,
    f35ce_f35_capital_efficiency_returns_icassetgapl_63d_slope_v126_signal,
    f35ce_f35_capital_efficiency_returns_marginlevers_252d_slope_v127_signal,
    f35ce_f35_capital_efficiency_returns_marginleverm_252d_slope_v128_signal,
    f35ce_f35_capital_efficiency_returns_marginleverl_252d_slope_v129_signal,
    f35ce_f35_capital_efficiency_returns_roiccovs_126d_slope_v130_signal,
    f35ce_f35_capital_efficiency_returns_roiccovm_126d_slope_v131_signal,
    f35ce_f35_capital_efficiency_returns_roiccovl_126d_slope_v132_signal,
    f35ce_f35_capital_efficiency_returns_epscales_126d_slope_v133_signal,
    f35ce_f35_capital_efficiency_returns_epscalem_126d_slope_v134_signal,
    f35ce_f35_capital_efficiency_returns_epscalel_126d_slope_v135_signal,
    f35ce_f35_capital_efficiency_returns_dupontbals_252d_slope_v136_signal,
    f35ce_f35_capital_efficiency_returns_dupontbalm_252d_slope_v137_signal,
    f35ce_f35_capital_efficiency_returns_dupontball_252d_slope_v138_signal,
    f35ce_f35_capital_efficiency_returns_roicroazs_252d_slope_v139_signal,
    f35ce_f35_capital_efficiency_returns_roicroazm_252d_slope_v140_signal,
    f35ce_f35_capital_efficiency_returns_roicroazl_252d_slope_v141_signal,
    f35ce_f35_capital_efficiency_returns_roaroszs_252d_slope_v142_signal,
    f35ce_f35_capital_efficiency_returns_roaroszm_252d_slope_v143_signal,
    f35ce_f35_capital_efficiency_returns_roaroszl_252d_slope_v144_signal,
    f35ce_f35_capital_efficiency_returns_roicroszs_252d_slope_v145_signal,
    f35ce_f35_capital_efficiency_returns_roicroszm_252d_slope_v146_signal,
    f35ce_f35_capital_efficiency_returns_roicroszl_252d_slope_v147_signal,
    f35ce_f35_capital_efficiency_returns_rosroaprods_63d_slope_v148_signal,
    f35ce_f35_capital_efficiency_returns_rosroaprodm_63d_slope_v149_signal,
    f35ce_f35_capital_efficiency_returns_rosroaprodl_63d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F35_CAPITAL_EFFICIENCY_RETURNS_REGISTRY_001_150 = REGISTRY


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

    print("OK f35_capital_efficiency_returns_2nd_derivatives_001_150_claude: %d features pass" % n_features)
