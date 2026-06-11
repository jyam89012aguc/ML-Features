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
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _ewm(s, span):
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _med(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _gm(revenue, gp):
    return gp / revenue.replace(0, np.nan)


def _om(revenue, opinc):
    return opinc / revenue.replace(0, np.nan)


def _nm(revenue, netinc):
    return netinc / revenue.replace(0, np.nan)


def _em(revenue, ebitda):
    return ebitda / revenue.replace(0, np.nan)


def _ebm(revenue, ebit):
    return ebit / revenue.replace(0, np.nan)


def _roe(netinc, equity):
    return netinc / equity.replace(0, np.nan)


def _roa(netinc, assets):
    return netinc / assets.replace(0, np.nan)


def _gpa(gp, assets):
    return gp / assets.replace(0, np.nan)


def _invcap(equity, assets):
    return (equity + 0.4 * (assets - equity)).replace(0, np.nan)


def f15pq_f15_profitability_quality_gmlvl_63d_slope_v001_signal(revenue, gp):
    base = _mean(_gm(revenue, gp), 63)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_omlvl_63d_slope_v002_signal(revenue, opinc):
    base = _mean(_om(revenue, opinc), 63)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_nmlvl_63d_slope_v003_signal(revenue, netinc):
    base = _mean(_nm(revenue, netinc), 63)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_emlvl_63d_slope_v004_signal(revenue, ebitda):
    base = _mean(_em(revenue, ebitda), 63)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_ebmlvl_63d_slope_v005_signal(revenue, ebit):
    base = _mean(_ebm(revenue, ebit), 63)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_roelvl_63d_slope_v006_signal(netinc, equity):
    base = _mean(_roe(netinc, equity), 63)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_roalvl_63d_slope_v007_signal(netinc, assets):
    base = _mean(_roa(netinc, assets), 63)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_gpalvl_63d_slope_v008_signal(gp, assets):
    base = _mean(_gpa(gp, assets), 63)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_gmz_252d_slope_v009_signal(revenue, gp):
    base = _z(_gm(revenue, gp), 252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_omz_252d_slope_v010_signal(revenue, opinc):
    base = _z(_om(revenue, opinc), 252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_nmz_252d_slope_v011_signal(revenue, netinc):
    base = _z(_nm(revenue, netinc), 252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_emz_252d_slope_v012_signal(revenue, ebitda):
    base = _z(_em(revenue, ebitda), 252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_ebmz_252d_slope_v013_signal(revenue, ebit):
    base = _z(_ebm(revenue, ebit), 252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_roez_252d_slope_v014_signal(netinc, equity):
    base = _z(_roe(netinc, equity), 252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_roaz_252d_slope_v015_signal(netinc, assets):
    base = _z(_roa(netinc, assets), 252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_gpaz_252d_slope_v016_signal(gp, assets):
    base = _z(_gpa(gp, assets), 252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_gmrank_504d_slope_v017_signal(revenue, gp):
    base = _rank(_gm(revenue, gp), 504)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_omrank_504d_slope_v018_signal(revenue, opinc):
    base = _rank(_om(revenue, opinc), 504)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_nmrank_504d_slope_v019_signal(revenue, netinc):
    base = _rank(_nm(revenue, netinc), 504)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_roerank_504d_slope_v020_signal(netinc, equity):
    base = _rank(_roe(netinc, equity), 504)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_roarank_504d_slope_v021_signal(netinc, assets):
    base = _rank(_roa(netinc, assets), 504)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_gparank_504d_slope_v022_signal(gp, assets):
    base = _rank(_gpa(gp, assets), 504)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_gmewm_126d_slope_v023_signal(revenue, gp):
    base = _ewm(_gm(revenue, gp), 126)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_emewm_126d_slope_v024_signal(revenue, ebitda):
    base = _ewm(_em(revenue, ebitda), 126)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_roaewm_126d_slope_v025_signal(netinc, assets):
    base = _ewm(_roa(netinc, assets), 126)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_gmstab_252d_slope_v026_signal(revenue, gp):
    m = _gm(revenue, gp)
    base = _mean(m, 252) / _std(m, 252).replace(0, np.nan)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_omstab_252d_slope_v027_signal(revenue, opinc):
    m = _om(revenue, opinc)
    base = _mean(m, 252) / _std(m, 252).replace(0, np.nan)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_nmstab_252d_slope_v028_signal(revenue, netinc):
    m = _nm(revenue, netinc)
    base = _mean(m, 252) / _std(m, 252).replace(0, np.nan)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_emstab_252d_slope_v029_signal(revenue, ebitda):
    m = _em(revenue, ebitda)
    base = _mean(m, 252) / _std(m, 252).replace(0, np.nan)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_roestab_252d_slope_v030_signal(netinc, equity):
    m = _roe(netinc, equity)
    base = _mean(m, 252) / _std(m, 252).replace(0, np.nan)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_nmvol_126d_slope_v031_signal(revenue, netinc):
    base = _std(_nm(revenue, netinc), 126)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_roavol_126d_slope_v032_signal(netinc, assets):
    base = _std(_roa(netinc, assets), 126)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_gmvol_126d_slope_v033_signal(revenue, gp):
    base = _std(_gm(revenue, gp), 126)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_emvol_126d_slope_v034_signal(revenue, ebitda):
    base = _std(_em(revenue, ebitda), 126)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_gmnmspr_63d_slope_v035_signal(revenue, gp, netinc):
    base = (_gm(revenue, gp) - _nm(revenue, netinc)).rolling(63, min_periods=21).mean()
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_omnmspr_63d_slope_v036_signal(revenue, opinc, netinc):
    base = (_om(revenue, opinc) - _nm(revenue, netinc)).rolling(63, min_periods=21).mean()
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_gmomspr_63d_slope_v037_signal(revenue, gp, opinc):
    base = (_gm(revenue, gp) - _om(revenue, opinc)).rolling(63, min_periods=21).mean()
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_emnmspr_63d_slope_v038_signal(revenue, ebitda, netinc):
    base = (_em(revenue, ebitda) - _nm(revenue, netinc)).rolling(63, min_periods=21).mean()
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_emebmspr_63d_slope_v039_signal(revenue, ebitda, ebit):
    base = (_em(revenue, ebitda) - _ebm(revenue, ebit)).rolling(63, min_periods=21).mean()
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_mgndisp_63d_slope_v040_signal(revenue, gp, opinc, netinc):
    d = pd.concat([_gm(revenue, gp), _om(revenue, opinc), _nm(revenue, netinc)], axis=1).std(axis=1)
    base = _mean(d, 63)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_mgndisp4z_252d_slope_v041_signal(revenue, gp, opinc, ebitda):
    d = pd.concat([_gm(revenue, gp), _om(revenue, opinc), _em(revenue, ebitda)], axis=1).std(axis=1)
    base = _z(d, 252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_ebitdaroa_63d_slope_v042_signal(ebitda, assets):
    base = _mean(ebitda / assets.replace(0, np.nan), 63)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_ebitroa_63d_slope_v043_signal(ebit, assets):
    base = _mean(ebit / assets.replace(0, np.nan), 63)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_oproa_63d_slope_v044_signal(opinc, assets):
    base = _mean(opinc / assets.replace(0, np.nan), 63)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_ebitroe_63d_slope_v045_signal(ebit, equity):
    base = _mean(ebit / equity.replace(0, np.nan), 63)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_gpequ_63d_slope_v046_signal(gp, equity):
    base = _mean(gp / equity.replace(0, np.nan), 63)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_ebitdaequ_63d_slope_v047_signal(ebitda, equity):
    base = _mean(ebitda / equity.replace(0, np.nan), 63)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_revequ_63d_slope_v048_signal(revenue, equity):
    base = _mean(revenue / equity.replace(0, np.nan), 63)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_ebitroicewm_126d_slope_v049_signal(ebit, equity, assets):
    m = ebit / _invcap(equity, assets)
    base = m - _ewm(m, 126)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_ebitdaroicewm_126d_slope_v050_signal(ebitda, equity, assets):
    m = ebitda / _invcap(equity, assets)
    base = m - _ewm(m, 126)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_oproicrank_504d_slope_v051_signal(opinc, equity, assets):
    base = _rank(opinc / _invcap(equity, assets), 504)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_niroicz_252d_slope_v052_signal(netinc, equity, assets):
    base = _z(netinc / _invcap(equity, assets), 252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_opgpconv_63d_slope_v053_signal(gp, opinc):
    base = _mean(opinc / gp.replace(0, np.nan), 63)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_netopconvz_252d_slope_v054_signal(opinc, netinc):
    base = _z(netinc / opinc.replace(0, np.nan), 252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_niebitcap_63d_slope_v055_signal(netinc, ebit):
    base = _mean(netinc / ebit.replace(0, np.nan), 63)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_niebitdacap_63d_slope_v056_signal(netinc, ebitda):
    base = _mean(netinc / ebitda.replace(0, np.nan), 63)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_opebitda_63d_slope_v057_signal(opinc, ebitda):
    base = _mean(opinc / ebitda.replace(0, np.nan), 63)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_gpebitda_63d_slope_v058_signal(gp, ebitda):
    base = _mean(gp / ebitda.replace(0, np.nan), 63)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_nigpretz_252d_slope_v059_signal(gp, netinc):
    base = _z(netinc / gp.replace(0, np.nan), 252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_assetturn_63d_slope_v060_signal(revenue, assets):
    base = _mean(revenue / assets.replace(0, np.nan), 63)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_gmvskewroll_252d_slope_v061_signal(revenue, gp):
    base = _gm(revenue, gp).rolling(252, min_periods=126).skew()
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_roekurt_252d_slope_v062_signal(netinc, equity):
    base = _roe(netinc, equity).rolling(252, min_periods=126).kurt()
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_nmqtl_252d_slope_v063_signal(revenue, netinc):
    m = _nm(revenue, netinc)
    base = m.rolling(252, min_periods=126).quantile(0.9) - _med(m, 252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_dupontlev_252d_slope_v064_signal(netinc, assets, equity):
    c = (netinc / assets.replace(0, np.nan)) * (assets / equity.replace(0, np.nan) - 1.0)
    base = _z(c, 252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_levamp_252d_slope_v065_signal(netinc, equity, assets):
    base = _rank(_roe(netinc, equity) / _roa(netinc, assets).replace(0, np.nan), 252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_mgnindex_63d_slope_v066_signal(revenue, gp, opinc, netinc):
    idx = (_gm(revenue, gp) + _om(revenue, opinc) + _nm(revenue, netinc)) / 3.0
    base = _mean(idx, 63)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_mgnstrength_252d_slope_v067_signal(revenue, gp, opinc, netinc):
    base = (_z(_gm(revenue, gp), 252) + _z(_om(revenue, opinc), 252) + _z(_nm(revenue, netinc), 252)) / 3.0
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_gmqual_252d_slope_v068_signal(revenue, gp):
    m = _gm(revenue, gp)
    base = _mean(m, 252) / (1.0 + _std(m, 252).replace(0, np.nan))
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_roaqual_252d_slope_v069_signal(netinc, assets):
    m = _roa(netinc, assets)
    base = _mean(m, 252) / (1.0 + _std(m, 252).replace(0, np.nan))
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_emqual_252d_slope_v070_signal(revenue, ebitda):
    m = _em(revenue, ebitda)
    base = _mean(m, 252) / (1.0 + _std(m, 252).replace(0, np.nan))
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_gmrangepos_1260d_slope_v071_signal(revenue, gp):
    m = _gm(revenue, gp)
    hi = m.rolling(1260, min_periods=504).max()
    lo = m.rolling(1260, min_periods=504).min()
    base = (m - lo) / (hi - lo).replace(0, np.nan) - 0.5
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_nmrangepos_1260d_slope_v072_signal(revenue, netinc):
    m = _nm(revenue, netinc)
    hi = m.rolling(1260, min_periods=504).max()
    lo = m.rolling(1260, min_periods=504).min()
    base = (m - lo) / (hi - lo).replace(0, np.nan) - 0.5
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_omrangepos_1260d_slope_v073_signal(revenue, opinc):
    m = _om(revenue, opinc)
    hi = m.rolling(1260, min_periods=504).max()
    lo = m.rolling(1260, min_periods=504).min()
    base = (m - lo) / (hi - lo).replace(0, np.nan) - 0.5
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_emrangepos_504d_slope_v074_signal(revenue, ebitda):
    m = _em(revenue, ebitda)
    hi = m.rolling(504, min_periods=252).max()
    lo = m.rolling(504, min_periods=252).min()
    base = (m - lo) / (hi - lo).replace(0, np.nan) - 0.5
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_gpaiqr_252d_slope_v075_signal(gp, assets):
    m = _gpa(gp, assets)
    base = m.rolling(252, min_periods=126).quantile(0.75) - m.rolling(252, min_periods=126).quantile(0.25)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_retdispz_252d_slope_v076_signal(netinc, equity, assets, opinc):
    d = pd.concat([_roe(netinc, equity), _roa(netinc, assets), opinc / assets.replace(0, np.nan)], axis=1).std(axis=1)
    base = _z(d, 252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_gpaewm_126d_slope_v077_signal(gp, assets):
    m = _gpa(gp, assets)
    base = m - _ewm(m, 126)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_gpaminusroa_252d_slope_v078_signal(gp, assets, netinc):
    base = _z(_gpa(gp, assets) - _roa(netinc, assets), 252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_roeconvex_252d_slope_v079_signal(netinc, equity):
    m = _roe(netinc, equity)
    md = _med(m, 252)
    base = np.sign(m - md) * (m - md) ** 2
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_omconvex_252d_slope_v080_signal(revenue, opinc):
    m = _om(revenue, opinc)
    md = _med(m, 252)
    base = np.sign(m - md) * (m - md) ** 2
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_ebmconvex_252d_slope_v081_signal(revenue, ebit):
    m = _ebm(revenue, ebit)
    md = _med(m, 252)
    base = np.sign(m - md) * (m - md) ** 2
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_nmskew_252d_slope_v082_signal(revenue, netinc):
    base = _nm(revenue, netinc).rolling(252, min_periods=126).skew()
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_nmkurt_252d_slope_v083_signal(revenue, netinc):
    base = _nm(revenue, netinc).rolling(252, min_periods=126).kurt()
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_gmiqr_252d_slope_v084_signal(revenue, gp):
    m = _gm(revenue, gp)
    base = m.rolling(252, min_periods=126).quantile(0.75) - m.rolling(252, min_periods=126).quantile(0.25)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_omiqr_252d_slope_v085_signal(revenue, opinc):
    m = _om(revenue, opinc)
    base = m.rolling(252, min_periods=126).quantile(0.75) - m.rolling(252, min_periods=126).quantile(0.25)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_roeiqr_252d_slope_v086_signal(netinc, equity):
    m = _roe(netinc, equity)
    base = m.rolling(252, min_periods=126).quantile(0.8) - m.rolling(252, min_periods=126).quantile(0.2)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_nmdown_252d_slope_v087_signal(revenue, netinc):
    m = _nm(revenue, netinc)
    md = _med(m, 252)
    base = (m - md).clip(upper=0).rolling(252, min_periods=126).mean()
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_roadown_252d_slope_v088_signal(netinc, assets):
    m = _roa(netinc, assets)
    md = _med(m, 252)
    base = np.sqrt(((m - md).clip(upper=0) ** 2).rolling(252, min_periods=126).mean())
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_gmabovemed_504d_slope_v089_signal(revenue, gp):
    m = _gm(revenue, gp)
    base = (m - _med(m, 504)) / _std(m, 504).replace(0, np.nan)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_nmdiffir_252d_slope_v090_signal(revenue, netinc):
    m = _nm(revenue, netinc).diff()
    base = _mean(m, 252) / _std(m, 252).replace(0, np.nan)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_roesharpe_252d_slope_v091_signal(netinc, equity):
    m = _roe(netinc, equity).diff()
    base = _mean(m, 252) / _std(m, 252).replace(0, np.nan)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_opleakvol_126d_slope_v092_signal(revenue, gp, opinc):
    base = _std((_gm(revenue, gp) - _om(revenue, opinc)) / _gm(revenue, gp).replace(0, np.nan), 126)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_belowopstab_252d_slope_v093_signal(revenue, opinc, netinc):
    m = (_om(revenue, opinc) - _nm(revenue, netinc)) / _om(revenue, opinc).replace(0, np.nan)
    base = _mean(m, 252) / _std(m, 252).replace(0, np.nan)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_dasharerank_504d_slope_v094_signal(ebitda, ebit):
    base = _rank((ebitda - ebit) / ebitda.replace(0, np.nan), 504)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_darate_252d_slope_v095_signal(ebitda, ebit, assets):
    base = _z((ebitda - ebit) / assets.replace(0, np.nan), 252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_retcomp_504d_slope_v096_signal(netinc, equity, assets, ebitda):
    base = (_rank(_roe(netinc, equity), 504) + _rank(_roa(netinc, assets), 504) + _rank(ebitda / assets.replace(0, np.nan), 504)) / 3.0
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_qualcomp_504d_slope_v097_signal(netinc, equity, assets, gp):
    base = (_rank(_roe(netinc, equity), 504) + _rank(_roa(netinc, assets), 504) + _rank(_gpa(gp, assets), 504)) / 3.0
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_cashprof_504d_slope_v098_signal(revenue, ebitda, assets):
    base = (_rank(_em(revenue, ebitda), 504) + _rank(ebitda / assets.replace(0, np.nan), 504)) / 2.0
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_mgncurv_252d_slope_v099_signal(revenue, gp, opinc, netinc):
    base = _z(_gm(revenue, gp) - 2.0 * _om(revenue, opinc) + _nm(revenue, netinc), 252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_mgnpulse_252d_slope_v100_signal(revenue, gp, opinc, netinc):
    idx = (_gm(revenue, gp) + _om(revenue, opinc) + _nm(revenue, netinc)) / 3.0
    base = _mean(idx, 21) - _mean(idx, 252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_nmcushion_252d_slope_v101_signal(revenue, netinc):
    m = _nm(revenue, netinc)
    base = (np.sign(m) * np.log1p(m.abs())).rolling(252, min_periods=126).mean()
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_nmsemidev_252d_slope_v102_signal(revenue, netinc):
    m = _nm(revenue, netinc)
    md = _med(m, 252)
    base = np.sqrt(((m - md).clip(upper=0) ** 2).rolling(252, min_periods=126).mean())
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_gpavsnm_504d_slope_v103_signal(gp, assets, revenue, netinc):
    base = _rank(_gpa(gp, assets), 504) - _rank(_nm(revenue, netinc), 504)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_gpaturndiv_504d_slope_v104_signal(gp, assets, revenue):
    base = _rank(_gpa(gp, assets), 504) - _rank(revenue / assets.replace(0, np.nan), 504)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_roicdisp_63d_slope_v105_signal(opinc, ebit, ebitda, equity, assets):
    ic = _invcap(equity, assets)
    d = pd.concat([opinc / ic, ebit / ic, ebitda / ic], axis=1).std(axis=1)
    base = _mean(d, 63)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_roicwedge_252d_slope_v106_signal(ebit, netinc, equity, assets):
    ic = _invcap(equity, assets)
    w = (ebit / ic) / (netinc / assets.replace(0, np.nan)).replace(0, np.nan)
    base = _z(w, 252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_nmfloor_252d_slope_v107_signal(revenue, netinc):
    m = _nm(revenue, netinc)
    fl = m.rolling(252, min_periods=126).min()
    base = (m - fl) / (1.0 + m.rolling(252, min_periods=126).std())
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_omfloor_252d_slope_v108_signal(revenue, opinc):
    m = _om(revenue, opinc)
    fl = m.rolling(252, min_periods=126).min()
    base = (m - fl) / (1.0 + m.rolling(252, min_periods=126).std())
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_nmstress_252d_slope_v109_signal(revenue, netinc):
    m = _nm(revenue, netinc)
    p10 = m.rolling(252, min_periods=126).quantile(0.10)
    base = (p10 - m).clip(lower=0).rolling(63, min_periods=21).mean()
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_gmnormgap_504d_slope_v110_signal(revenue, gp):
    m = _gm(revenue, gp)
    base = (m.rolling(63, min_periods=21).mean() - m.rolling(504, min_periods=252).mean()) / m.rolling(504, min_periods=252).mean().replace(0, np.nan)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_gmvolofmean_252d_slope_v111_signal(revenue, gp):
    m = _mean(_gm(revenue, gp), 63)
    base = _std(m, 252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_nmvslag_126d_slope_v112_signal(revenue, netinc):
    m = _nm(revenue, netinc)
    base = _mean(m, 63) - _mean(m, 126).shift(126)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_roenorm_1260d_slope_v113_signal(netinc, equity):
    m = _roe(netinc, equity)
    nrm = m.rolling(1260, min_periods=504).mean()
    base = (m - nrm) / m.rolling(1260, min_periods=504).std().replace(0, np.nan)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_emdisp_126d_slope_v114_signal(revenue, ebitda):
    m = _em(revenue, ebitda)
    base = m - _ewm(m, 126)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_ebitequz_252d_slope_v115_signal(ebit, equity):
    base = _z(ebit / equity.replace(0, np.nan), 252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_gpequz_252d_slope_v116_signal(gp, equity):
    base = _z(gp / equity.replace(0, np.nan), 252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_revequz_252d_slope_v117_signal(revenue, equity):
    base = _z(revenue / equity.replace(0, np.nan), 252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_ebitdaroaz_252d_slope_v118_signal(ebitda, assets):
    base = _z(ebitda / assets.replace(0, np.nan), 252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_ebitroaz_252d_slope_v119_signal(ebit, assets):
    base = _z(ebit / assets.replace(0, np.nan), 252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_oproaz_252d_slope_v120_signal(opinc, assets):
    base = _z(opinc / assets.replace(0, np.nan), 252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_mgnorder_252d_slope_v121_signal(revenue, gp, opinc, netinc):
    o = ((_gm(revenue, gp) >= _om(revenue, opinc)).astype(float) + (_om(revenue, opinc) >= _nm(revenue, netinc)).astype(float)) - 1.0
    base = o.rolling(252, min_periods=126).mean()
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_mgndisp5_63d_slope_v122_signal(revenue, gp, opinc, ebitda, ebit):
    d = pd.concat([_gm(revenue, gp), _om(revenue, opinc), _em(revenue, ebitda), _ebm(revenue, ebit)], axis=1).std(axis=1)
    base = _mean(d, 63)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_qualscore_504d_slope_v123_signal(revenue, gp, netinc, assets):
    base = _rank(_gm(revenue, gp), 504) + _rank(_roa(netinc, assets), 504) - _rank(_std(_nm(revenue, netinc), 252), 504)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_levampshift_252d_slope_v124_signal(netinc, equity, assets):
    amp = _roe(netinc, equity) / _roa(netinc, assets).replace(0, np.nan)
    base = amp - amp.rolling(252, min_periods=126).mean()
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_omceil_252d_slope_v125_signal(revenue, opinc):
    m = _om(revenue, opinc)
    cl = m.rolling(252, min_periods=126).max()
    base = (cl - m) / (1.0 + m.rolling(252, min_periods=126).std())
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_ebmstab_252d_slope_v126_signal(revenue, ebit):
    m = _ebm(revenue, ebit)
    base = _mean(m, 252) / _std(m, 252).replace(0, np.nan)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_gpastab_252d_slope_v127_signal(gp, assets):
    m = _gpa(gp, assets)
    base = _mean(m, 252) / _std(m, 252).replace(0, np.nan)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_oproicstab_252d_slope_v128_signal(opinc, equity, assets):
    m = opinc / _invcap(equity, assets)
    base = _mean(m, 252) / _std(m, 252).replace(0, np.nan)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_omsignmag_63d_slope_v129_signal(revenue, opinc):
    m = _om(revenue, opinc)
    sm = np.sign(m) * np.sqrt(m.abs())
    base = _mean(sm, 63) - _mean(sm, 252)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_retbreadth_504d_slope_v130_signal(netinc, equity, assets, opinc):
    roe = _rank(_roe(netinc, equity), 504)
    roa = _rank(_roa(netinc, assets), 504)
    op = _rank(opinc / assets.replace(0, np.nan), 504)
    raw = (roe > 0).astype(float) + (roa > 0).astype(float) + (op > 0).astype(float) - 1.5
    base = raw.rolling(63, min_periods=21).mean()
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_mgnbreadth_252d_slope_v131_signal(revenue, gp, opinc, netinc):
    bg = (_gm(revenue, gp) > _med(_gm(revenue, gp), 252)).astype(float)
    bo = (_om(revenue, opinc) > _med(_om(revenue, opinc), 252)).astype(float)
    bn = (_nm(revenue, netinc) > _med(_nm(revenue, netinc), 252)).astype(float)
    base = ((bg + bo + bn) - 1.5).rolling(63, min_periods=21).mean()
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_gmomsprrangepos_504d_slope_v132_signal(revenue, gp, opinc):
    spr = _gm(revenue, gp) - _om(revenue, opinc)
    hi = spr.rolling(504, min_periods=252).max()
    lo = spr.rolling(504, min_periods=252).min()
    base = (spr - lo) / (hi - lo).replace(0, np.nan) - 0.5
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_roeexcess_63d_slope_v133_signal(netinc, equity, assets):
    sp = _roe(netinc, equity) - _roa(netinc, assets)
    dt = sp - sp.rolling(252, min_periods=126).mean()
    base = np.tanh(15.0 * dt)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_roadrvshift_252d_slope_v134_signal(revenue, netinc, assets):
    bal = np.log(_nm(revenue, netinc).abs().replace(0, np.nan)) - np.log((revenue / assets.replace(0, np.nan)).replace(0, np.nan))
    base = bal - bal.rolling(252, min_periods=126).mean()
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_emnmsprz_252d_slope_v135_signal(netinc, ebitda, revenue):
    base = _z(_em(revenue, ebitda) - _nm(revenue, netinc), 252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_gpebitdaz_252d_slope_v136_signal(gp, ebitda):
    base = _z(gp / ebitda.replace(0, np.nan), 252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_ebitdaroicrank_504d_slope_v137_signal(ebitda, equity, assets):
    base = _rank(ebitda / _invcap(equity, assets), 504)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_ebitroicz_252d_slope_v138_signal(ebit, equity, assets):
    base = _z(ebit / _invcap(equity, assets), 252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_gmmom_252d_slope_v139_signal(revenue, gp):
    sm = _mean(_gm(revenue, gp), 63)
    base = sm - sm.shift(252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_ommom_252d_slope_v140_signal(revenue, opinc):
    sm = _mean(_om(revenue, opinc), 63)
    base = sm - sm.shift(252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_roemom_252d_slope_v141_signal(netinc, equity):
    sm = _mean(_roe(netinc, equity), 63)
    base = sm - sm.shift(252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_roamom_252d_slope_v142_signal(netinc, assets):
    sm = _mean(_roa(netinc, assets), 63)
    base = sm - sm.shift(252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_gpamom_252d_slope_v143_signal(gp, assets):
    sm = _mean(_gpa(gp, assets), 63)
    base = sm - sm.shift(252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_emmom_252d_slope_v144_signal(revenue, ebitda):
    sm = _mean(_em(revenue, ebitda), 63)
    base = sm - sm.shift(252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_ebmmom_252d_slope_v145_signal(revenue, ebit):
    sm = _mean(_ebm(revenue, ebit), 63)
    base = sm - sm.shift(252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_ebitdaroamom_252d_slope_v146_signal(ebitda, assets):
    sm = _mean(ebitda / assets.replace(0, np.nan), 63)
    base = sm - sm.shift(252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_oproamom_252d_slope_v147_signal(opinc, assets):
    sm = _mean(opinc / assets.replace(0, np.nan), 63)
    base = sm - sm.shift(252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_ebitroicmom_252d_slope_v148_signal(ebit, equity, assets):
    sm = _mean(ebit / _invcap(equity, assets), 63)
    base = sm - sm.shift(252)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_niroicstab_252d_slope_v149_signal(netinc, equity, assets):
    m = netinc / _invcap(equity, assets)
    base = _mean(m, 252) / _std(m, 252).replace(0, np.nan)
    d = base.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f15pq_f15_profitability_quality_opgpmom_63d_slope_v150_signal(gp, opinc):
    sm = _mean(opinc / gp.replace(0, np.nan), 63)
    base = sm - sm.shift(63)
    d = base.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f15pq_f15_profitability_quality_gmlvl_63d_slope_v001_signal,
    f15pq_f15_profitability_quality_omlvl_63d_slope_v002_signal,
    f15pq_f15_profitability_quality_nmlvl_63d_slope_v003_signal,
    f15pq_f15_profitability_quality_emlvl_63d_slope_v004_signal,
    f15pq_f15_profitability_quality_ebmlvl_63d_slope_v005_signal,
    f15pq_f15_profitability_quality_roelvl_63d_slope_v006_signal,
    f15pq_f15_profitability_quality_roalvl_63d_slope_v007_signal,
    f15pq_f15_profitability_quality_gpalvl_63d_slope_v008_signal,
    f15pq_f15_profitability_quality_gmz_252d_slope_v009_signal,
    f15pq_f15_profitability_quality_omz_252d_slope_v010_signal,
    f15pq_f15_profitability_quality_nmz_252d_slope_v011_signal,
    f15pq_f15_profitability_quality_emz_252d_slope_v012_signal,
    f15pq_f15_profitability_quality_ebmz_252d_slope_v013_signal,
    f15pq_f15_profitability_quality_roez_252d_slope_v014_signal,
    f15pq_f15_profitability_quality_roaz_252d_slope_v015_signal,
    f15pq_f15_profitability_quality_gpaz_252d_slope_v016_signal,
    f15pq_f15_profitability_quality_gmrank_504d_slope_v017_signal,
    f15pq_f15_profitability_quality_omrank_504d_slope_v018_signal,
    f15pq_f15_profitability_quality_nmrank_504d_slope_v019_signal,
    f15pq_f15_profitability_quality_roerank_504d_slope_v020_signal,
    f15pq_f15_profitability_quality_roarank_504d_slope_v021_signal,
    f15pq_f15_profitability_quality_gparank_504d_slope_v022_signal,
    f15pq_f15_profitability_quality_gmewm_126d_slope_v023_signal,
    f15pq_f15_profitability_quality_emewm_126d_slope_v024_signal,
    f15pq_f15_profitability_quality_roaewm_126d_slope_v025_signal,
    f15pq_f15_profitability_quality_gmstab_252d_slope_v026_signal,
    f15pq_f15_profitability_quality_omstab_252d_slope_v027_signal,
    f15pq_f15_profitability_quality_nmstab_252d_slope_v028_signal,
    f15pq_f15_profitability_quality_emstab_252d_slope_v029_signal,
    f15pq_f15_profitability_quality_roestab_252d_slope_v030_signal,
    f15pq_f15_profitability_quality_nmvol_126d_slope_v031_signal,
    f15pq_f15_profitability_quality_roavol_126d_slope_v032_signal,
    f15pq_f15_profitability_quality_gmvol_126d_slope_v033_signal,
    f15pq_f15_profitability_quality_emvol_126d_slope_v034_signal,
    f15pq_f15_profitability_quality_gmnmspr_63d_slope_v035_signal,
    f15pq_f15_profitability_quality_omnmspr_63d_slope_v036_signal,
    f15pq_f15_profitability_quality_gmomspr_63d_slope_v037_signal,
    f15pq_f15_profitability_quality_emnmspr_63d_slope_v038_signal,
    f15pq_f15_profitability_quality_emebmspr_63d_slope_v039_signal,
    f15pq_f15_profitability_quality_mgndisp_63d_slope_v040_signal,
    f15pq_f15_profitability_quality_mgndisp4z_252d_slope_v041_signal,
    f15pq_f15_profitability_quality_ebitdaroa_63d_slope_v042_signal,
    f15pq_f15_profitability_quality_ebitroa_63d_slope_v043_signal,
    f15pq_f15_profitability_quality_oproa_63d_slope_v044_signal,
    f15pq_f15_profitability_quality_ebitroe_63d_slope_v045_signal,
    f15pq_f15_profitability_quality_gpequ_63d_slope_v046_signal,
    f15pq_f15_profitability_quality_ebitdaequ_63d_slope_v047_signal,
    f15pq_f15_profitability_quality_revequ_63d_slope_v048_signal,
    f15pq_f15_profitability_quality_ebitroicewm_126d_slope_v049_signal,
    f15pq_f15_profitability_quality_ebitdaroicewm_126d_slope_v050_signal,
    f15pq_f15_profitability_quality_oproicrank_504d_slope_v051_signal,
    f15pq_f15_profitability_quality_niroicz_252d_slope_v052_signal,
    f15pq_f15_profitability_quality_opgpconv_63d_slope_v053_signal,
    f15pq_f15_profitability_quality_netopconvz_252d_slope_v054_signal,
    f15pq_f15_profitability_quality_niebitcap_63d_slope_v055_signal,
    f15pq_f15_profitability_quality_niebitdacap_63d_slope_v056_signal,
    f15pq_f15_profitability_quality_opebitda_63d_slope_v057_signal,
    f15pq_f15_profitability_quality_gpebitda_63d_slope_v058_signal,
    f15pq_f15_profitability_quality_nigpretz_252d_slope_v059_signal,
    f15pq_f15_profitability_quality_assetturn_63d_slope_v060_signal,
    f15pq_f15_profitability_quality_gmvskewroll_252d_slope_v061_signal,
    f15pq_f15_profitability_quality_roekurt_252d_slope_v062_signal,
    f15pq_f15_profitability_quality_nmqtl_252d_slope_v063_signal,
    f15pq_f15_profitability_quality_dupontlev_252d_slope_v064_signal,
    f15pq_f15_profitability_quality_levamp_252d_slope_v065_signal,
    f15pq_f15_profitability_quality_mgnindex_63d_slope_v066_signal,
    f15pq_f15_profitability_quality_mgnstrength_252d_slope_v067_signal,
    f15pq_f15_profitability_quality_gmqual_252d_slope_v068_signal,
    f15pq_f15_profitability_quality_roaqual_252d_slope_v069_signal,
    f15pq_f15_profitability_quality_emqual_252d_slope_v070_signal,
    f15pq_f15_profitability_quality_gmrangepos_1260d_slope_v071_signal,
    f15pq_f15_profitability_quality_nmrangepos_1260d_slope_v072_signal,
    f15pq_f15_profitability_quality_omrangepos_1260d_slope_v073_signal,
    f15pq_f15_profitability_quality_emrangepos_504d_slope_v074_signal,
    f15pq_f15_profitability_quality_gpaiqr_252d_slope_v075_signal,
    f15pq_f15_profitability_quality_retdispz_252d_slope_v076_signal,
    f15pq_f15_profitability_quality_gpaewm_126d_slope_v077_signal,
    f15pq_f15_profitability_quality_gpaminusroa_252d_slope_v078_signal,
    f15pq_f15_profitability_quality_roeconvex_252d_slope_v079_signal,
    f15pq_f15_profitability_quality_omconvex_252d_slope_v080_signal,
    f15pq_f15_profitability_quality_ebmconvex_252d_slope_v081_signal,
    f15pq_f15_profitability_quality_nmskew_252d_slope_v082_signal,
    f15pq_f15_profitability_quality_nmkurt_252d_slope_v083_signal,
    f15pq_f15_profitability_quality_gmiqr_252d_slope_v084_signal,
    f15pq_f15_profitability_quality_omiqr_252d_slope_v085_signal,
    f15pq_f15_profitability_quality_roeiqr_252d_slope_v086_signal,
    f15pq_f15_profitability_quality_nmdown_252d_slope_v087_signal,
    f15pq_f15_profitability_quality_roadown_252d_slope_v088_signal,
    f15pq_f15_profitability_quality_gmabovemed_504d_slope_v089_signal,
    f15pq_f15_profitability_quality_nmdiffir_252d_slope_v090_signal,
    f15pq_f15_profitability_quality_roesharpe_252d_slope_v091_signal,
    f15pq_f15_profitability_quality_opleakvol_126d_slope_v092_signal,
    f15pq_f15_profitability_quality_belowopstab_252d_slope_v093_signal,
    f15pq_f15_profitability_quality_dasharerank_504d_slope_v094_signal,
    f15pq_f15_profitability_quality_darate_252d_slope_v095_signal,
    f15pq_f15_profitability_quality_retcomp_504d_slope_v096_signal,
    f15pq_f15_profitability_quality_qualcomp_504d_slope_v097_signal,
    f15pq_f15_profitability_quality_cashprof_504d_slope_v098_signal,
    f15pq_f15_profitability_quality_mgncurv_252d_slope_v099_signal,
    f15pq_f15_profitability_quality_mgnpulse_252d_slope_v100_signal,
    f15pq_f15_profitability_quality_nmcushion_252d_slope_v101_signal,
    f15pq_f15_profitability_quality_nmsemidev_252d_slope_v102_signal,
    f15pq_f15_profitability_quality_gpavsnm_504d_slope_v103_signal,
    f15pq_f15_profitability_quality_gpaturndiv_504d_slope_v104_signal,
    f15pq_f15_profitability_quality_roicdisp_63d_slope_v105_signal,
    f15pq_f15_profitability_quality_roicwedge_252d_slope_v106_signal,
    f15pq_f15_profitability_quality_nmfloor_252d_slope_v107_signal,
    f15pq_f15_profitability_quality_omfloor_252d_slope_v108_signal,
    f15pq_f15_profitability_quality_nmstress_252d_slope_v109_signal,
    f15pq_f15_profitability_quality_gmnormgap_504d_slope_v110_signal,
    f15pq_f15_profitability_quality_gmvolofmean_252d_slope_v111_signal,
    f15pq_f15_profitability_quality_nmvslag_126d_slope_v112_signal,
    f15pq_f15_profitability_quality_roenorm_1260d_slope_v113_signal,
    f15pq_f15_profitability_quality_emdisp_126d_slope_v114_signal,
    f15pq_f15_profitability_quality_ebitequz_252d_slope_v115_signal,
    f15pq_f15_profitability_quality_gpequz_252d_slope_v116_signal,
    f15pq_f15_profitability_quality_revequz_252d_slope_v117_signal,
    f15pq_f15_profitability_quality_ebitdaroaz_252d_slope_v118_signal,
    f15pq_f15_profitability_quality_ebitroaz_252d_slope_v119_signal,
    f15pq_f15_profitability_quality_oproaz_252d_slope_v120_signal,
    f15pq_f15_profitability_quality_mgnorder_252d_slope_v121_signal,
    f15pq_f15_profitability_quality_mgndisp5_63d_slope_v122_signal,
    f15pq_f15_profitability_quality_qualscore_504d_slope_v123_signal,
    f15pq_f15_profitability_quality_levampshift_252d_slope_v124_signal,
    f15pq_f15_profitability_quality_omceil_252d_slope_v125_signal,
    f15pq_f15_profitability_quality_ebmstab_252d_slope_v126_signal,
    f15pq_f15_profitability_quality_gpastab_252d_slope_v127_signal,
    f15pq_f15_profitability_quality_oproicstab_252d_slope_v128_signal,
    f15pq_f15_profitability_quality_omsignmag_63d_slope_v129_signal,
    f15pq_f15_profitability_quality_retbreadth_504d_slope_v130_signal,
    f15pq_f15_profitability_quality_mgnbreadth_252d_slope_v131_signal,
    f15pq_f15_profitability_quality_gmomsprrangepos_504d_slope_v132_signal,
    f15pq_f15_profitability_quality_roeexcess_63d_slope_v133_signal,
    f15pq_f15_profitability_quality_roadrvshift_252d_slope_v134_signal,
    f15pq_f15_profitability_quality_emnmsprz_252d_slope_v135_signal,
    f15pq_f15_profitability_quality_gpebitdaz_252d_slope_v136_signal,
    f15pq_f15_profitability_quality_ebitdaroicrank_504d_slope_v137_signal,
    f15pq_f15_profitability_quality_ebitroicz_252d_slope_v138_signal,
    f15pq_f15_profitability_quality_gmmom_252d_slope_v139_signal,
    f15pq_f15_profitability_quality_ommom_252d_slope_v140_signal,
    f15pq_f15_profitability_quality_roemom_252d_slope_v141_signal,
    f15pq_f15_profitability_quality_roamom_252d_slope_v142_signal,
    f15pq_f15_profitability_quality_gpamom_252d_slope_v143_signal,
    f15pq_f15_profitability_quality_emmom_252d_slope_v144_signal,
    f15pq_f15_profitability_quality_ebmmom_252d_slope_v145_signal,
    f15pq_f15_profitability_quality_ebitdaroamom_252d_slope_v146_signal,
    f15pq_f15_profitability_quality_oproamom_252d_slope_v147_signal,
    f15pq_f15_profitability_quality_ebitroicmom_252d_slope_v148_signal,
    f15pq_f15_profitability_quality_niroicstab_252d_slope_v149_signal,
    f15pq_f15_profitability_quality_opgpmom_63d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F15_PROFITABILITY_QUALITY_REGISTRY_SLOPE_001_150 = REGISTRY


def _fund(seed, n, base=1e8, drift=0.02, vol=0.05, allow_neg=False):
    g = np.random.default_rng(seed)
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.3
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    revenue = _fund(1, n, base=1e9, drift=0.02, vol=0.04).rename("revenue")
    gp = _fund(2, n, base=4e8, drift=0.02, vol=0.05).rename("gp")
    opinc = _fund(3, n, base=2e8, drift=0.02, vol=0.06, allow_neg=True).rename("opinc")
    netinc = _fund(4, n, base=1.5e8, drift=0.02, vol=0.07, allow_neg=True).rename("netinc")
    ebitda = _fund(5, n, base=3e8, drift=0.02, vol=0.05).rename("ebitda")
    ebit = _fund(6, n, base=2.2e8, drift=0.02, vol=0.06).rename("ebit")
    equity = _fund(7, n, base=2e9, drift=0.015, vol=0.04).rename("equity")
    assets = _fund(8, n, base=5e9, drift=0.015, vol=0.03).rename("assets")

    cols = {"revenue": revenue, "gp": gp, "opinc": opinc, "netinc": netinc,
            "ebitda": ebitda, "ebit": ebit, "equity": equity, "assets": assets}

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

    print("OK f15_profitability_quality_2nd_derivatives_001_150_claude: %d features pass" % n_features)
