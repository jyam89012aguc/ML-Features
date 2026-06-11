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
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


# ===== options / warrant positioning base primitives (slope source series) =====
def _put_call_value_skew(putvalue, cllvalue):
    return (putvalue - cllvalue) / (putvalue + cllvalue).replace(0, np.nan)


def _put_call_holder_skew(putholders, cllholders):
    return (putholders - cllholders) / (putholders + cllholders).replace(0, np.nan)


def _hedging_intensity(putvalue, marketcap):
    return putvalue / marketcap.replace(0, np.nan)


def _call_intensity(cllvalue, marketcap):
    return cllvalue / marketcap.replace(0, np.nan)


def _warrant_overhang_mcap(wntvalue, marketcap):
    return wntvalue / marketcap.replace(0, np.nan)


def _warrant_overhang_total(wntvalue, totalvalue):
    return wntvalue / totalvalue.replace(0, np.nan)


def _debt_overhang(dbtvalue, totalvalue):
    return dbtvalue / totalvalue.replace(0, np.nan)


def _deriv_share(putvalue, cllvalue, wntvalue, shrvalue):
    return (putvalue + cllvalue + wntvalue) / shrvalue.replace(0, np.nan)


def _gross_opt(putvalue, cllvalue, marketcap):
    return (putvalue + cllvalue) / marketcap.replace(0, np.nan)


def _latent_supply(wntvalue, dbtvalue, marketcap):
    return (wntvalue + dbtvalue) / marketcap.replace(0, np.nan)


def _net_bear(putvalue, cllvalue, marketcap):
    return (putvalue - cllvalue) / marketcap.replace(0, np.nan)


def _avg_ticket(value, holders):
    return value / holders.replace(0, np.nan)


def _wnt_unit_share(wntunits, putunits, cllunits):
    return wntunits / (putunits + cllunits + wntunits).replace(0, np.nan)


def _hedge_purity(putvalue, cllvalue):
    return putvalue / (putvalue + cllvalue).replace(0, np.nan)


def _dbt_dominance(dbtvalue, putvalue, cllvalue, wntvalue):
    return dbtvalue / (putvalue + cllvalue + wntvalue + dbtvalue).replace(0, np.nan)


def f46ow_f46_options_warrant_positioning_pcvalskew_63d_slope_v001_signal(putvalue, cllvalue):
    base = _put_call_value_skew(putvalue, cllvalue)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_pcvalskew_63d_slope_v002_signal(putvalue, cllvalue):
    base = _put_call_value_skew(putvalue, cllvalue)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_pcvalskew_126d_slope_v003_signal(putvalue, cllvalue):
    base = _mean(_put_call_value_skew(putvalue, cllvalue), 126)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_pcvalskew_252d_slope_v004_signal(putvalue, cllvalue):
    base = _mean(_put_call_value_skew(putvalue, cllvalue), 252)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_pcholdskew_63d_slope_v005_signal(putholders, cllholders):
    base = _put_call_holder_skew(putholders, cllholders)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_pcholdskew_63d_slope_v006_signal(putholders, cllholders):
    base = _put_call_holder_skew(putholders, cllholders)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_pcholdskew_252d_slope_v007_signal(putholders, cllholders):
    base = _mean(_put_call_holder_skew(putholders, cllholders), 252)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_hedgeint_63d_slope_v008_signal(putvalue, marketcap):
    base = _hedging_intensity(putvalue, marketcap)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_hedgeint_63d_slope_v009_signal(putvalue, marketcap):
    base = _hedging_intensity(putvalue, marketcap)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_hedgeint_126d_slope_v010_signal(putvalue, marketcap):
    base = _mean(_hedging_intensity(putvalue, marketcap), 126)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_hedgeint_252d_slope_v011_signal(putvalue, marketcap):
    base = _mean(_hedging_intensity(putvalue, marketcap), 252)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_callint_63d_slope_v012_signal(cllvalue, marketcap):
    base = _call_intensity(cllvalue, marketcap)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_callint_63d_slope_v013_signal(cllvalue, marketcap):
    base = _call_intensity(cllvalue, marketcap)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_callint_252d_slope_v014_signal(cllvalue, marketcap):
    base = _mean(_call_intensity(cllvalue, marketcap), 252)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_wntoverM_63d_slope_v015_signal(wntvalue, marketcap):
    base = _warrant_overhang_mcap(wntvalue, marketcap)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_wntoverM_63d_slope_v016_signal(wntvalue, marketcap):
    base = _warrant_overhang_mcap(wntvalue, marketcap)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_wntoverM_126d_slope_v017_signal(wntvalue, marketcap):
    base = _mean(_warrant_overhang_mcap(wntvalue, marketcap), 126)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_wntoverM_252d_slope_v018_signal(wntvalue, marketcap):
    base = _mean(_warrant_overhang_mcap(wntvalue, marketcap), 252)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_wntoverT_63d_slope_v019_signal(wntvalue, totalvalue):
    base = _warrant_overhang_total(wntvalue, totalvalue)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_wntoverT_63d_slope_v020_signal(wntvalue, totalvalue):
    base = _warrant_overhang_total(wntvalue, totalvalue)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_wntoverT_252d_slope_v021_signal(wntvalue, totalvalue):
    base = _mean(_warrant_overhang_total(wntvalue, totalvalue), 252)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_dbtover_63d_slope_v022_signal(dbtvalue, totalvalue):
    base = _debt_overhang(dbtvalue, totalvalue)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_dbtover_63d_slope_v023_signal(dbtvalue, totalvalue):
    base = _debt_overhang(dbtvalue, totalvalue)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_dbtover_252d_slope_v024_signal(dbtvalue, totalvalue):
    base = _mean(_debt_overhang(dbtvalue, totalvalue), 252)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_derivshare_63d_slope_v025_signal(putvalue, cllvalue, wntvalue, shrvalue):
    base = _deriv_share(putvalue, cllvalue, wntvalue, shrvalue)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_derivshare_63d_slope_v026_signal(putvalue, cllvalue, wntvalue, shrvalue):
    base = _deriv_share(putvalue, cllvalue, wntvalue, shrvalue)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_derivshare_252d_slope_v027_signal(putvalue, cllvalue, wntvalue, shrvalue):
    base = _mean(_deriv_share(putvalue, cllvalue, wntvalue, shrvalue), 252)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_grossopt_63d_slope_v028_signal(putvalue, cllvalue, marketcap):
    base = _gross_opt(putvalue, cllvalue, marketcap)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_grossopt_63d_slope_v029_signal(putvalue, cllvalue, marketcap):
    base = _gross_opt(putvalue, cllvalue, marketcap)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_grossopt_252d_slope_v030_signal(putvalue, cllvalue, marketcap):
    base = _mean(_gross_opt(putvalue, cllvalue, marketcap), 252)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_latentsup_63d_slope_v031_signal(wntvalue, dbtvalue, marketcap):
    base = _latent_supply(wntvalue, dbtvalue, marketcap)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_latentsup_63d_slope_v032_signal(wntvalue, dbtvalue, marketcap):
    base = _latent_supply(wntvalue, dbtvalue, marketcap)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_latentsup_252d_slope_v033_signal(wntvalue, dbtvalue, marketcap):
    base = _mean(_latent_supply(wntvalue, dbtvalue, marketcap), 252)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_netbear_63d_slope_v034_signal(putvalue, cllvalue, marketcap):
    base = _net_bear(putvalue, cllvalue, marketcap)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_netbear_63d_slope_v035_signal(putvalue, cllvalue, marketcap):
    base = _net_bear(putvalue, cllvalue, marketcap)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_netbear_252d_slope_v036_signal(putvalue, cllvalue, marketcap):
    base = _z(_net_bear(putvalue, cllvalue, marketcap), 252)
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_putbreadth_63d_slope_v037_signal(putholders):
    base = _z(putholders, 252)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_putbreadth_126d_slope_v038_signal(putholders):
    base = _z(putholders, 252)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_callbreadth_63d_slope_v039_signal(cllholders):
    base = _z(cllholders, 252)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_callbreadth_126d_slope_v040_signal(cllholders):
    base = _z(cllholders, 252)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_wntbreadth_63d_slope_v041_signal(wntholders):
    base = _z(wntholders, 252)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_wntbreadth_126d_slope_v042_signal(wntholders):
    base = _z(wntholders, 252)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_dbtbreadth_63d_slope_v043_signal(dbtholders):
    base = _z(dbtholders, 252)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_dbtbreadth_126d_slope_v044_signal(dbtholders):
    base = _z(dbtholders, 252)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_putticket_63d_slope_v045_signal(putvalue, putholders):
    base = _avg_ticket(putvalue, putholders)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_putticket_126d_slope_v046_signal(putvalue, putholders):
    base = _avg_ticket(putvalue, putholders)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_callticket_63d_slope_v047_signal(cllvalue, cllholders):
    base = _avg_ticket(cllvalue, cllholders)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_callticket_126d_slope_v048_signal(cllvalue, cllholders):
    base = _avg_ticket(cllvalue, cllholders)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_wntticket_63d_slope_v049_signal(wntvalue, wntholders):
    base = _avg_ticket(wntvalue, wntholders)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_wntticket_126d_slope_v050_signal(wntvalue, wntholders):
    base = _avg_ticket(wntvalue, wntholders)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_dbtticket_63d_slope_v051_signal(dbtvalue, dbtholders):
    base = _avg_ticket(dbtvalue, dbtholders)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_dbtticket_126d_slope_v052_signal(dbtvalue, dbtholders):
    base = _avg_ticket(dbtvalue, dbtholders)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_putvaltot_63d_slope_v053_signal(putvalue, totalvalue):
    base = putvalue / totalvalue.replace(0, np.nan)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_putvaltot_126d_slope_v054_signal(putvalue, totalvalue):
    base = putvalue / totalvalue.replace(0, np.nan)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_callvaltot_63d_slope_v055_signal(cllvalue, totalvalue):
    base = cllvalue / totalvalue.replace(0, np.nan)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_callvaltot_126d_slope_v056_signal(cllvalue, totalvalue):
    base = cllvalue / totalvalue.replace(0, np.nan)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_hedgepurity_63d_slope_v057_signal(putvalue, cllvalue):
    base = _rank(_hedge_purity(putvalue, cllvalue), 252)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_hedgepurity_126d_slope_v058_signal(putvalue, cllvalue):
    base = _rank(_hedge_purity(putvalue, cllvalue), 252)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_wntoptshare_63d_slope_v059_signal(wntvalue, putvalue, cllvalue):
    base = wntvalue / (putvalue + cllvalue + wntvalue).replace(0, np.nan)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_wntoptshare_126d_slope_v060_signal(wntvalue, putvalue, cllvalue):
    base = wntvalue / (putvalue + cllvalue + wntvalue).replace(0, np.nan)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_dbtdom_63d_slope_v061_signal(dbtvalue, putvalue, cllvalue, wntvalue):
    base = _dbt_dominance(dbtvalue, putvalue, cllvalue, wntvalue)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_dbtdom_126d_slope_v062_signal(dbtvalue, putvalue, cllvalue, wntvalue):
    base = _dbt_dominance(dbtvalue, putvalue, cllvalue, wntvalue)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_unitskew_63d_slope_v063_signal(putunits, cllunits):
    base = (putunits - cllunits) / (putunits + cllunits).replace(0, np.nan)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_unitskew_126d_slope_v064_signal(putunits, cllunits):
    base = (putunits - cllunits) / (putunits + cllunits).replace(0, np.nan)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_wntunitshare_63d_slope_v065_signal(wntunits, putunits, cllunits):
    base = _wnt_unit_share(wntunits, putunits, cllunits)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_wntunitshare_126d_slope_v066_signal(wntunits, putunits, cllunits):
    base = _wnt_unit_share(wntunits, putunits, cllunits)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_pctlevel_63d_slope_v067_signal(percentoftotal):
    base = percentoftotal
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_pctlevel_126d_slope_v068_signal(percentoftotal):
    base = _mean(percentoftotal, 63)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_pcthedge_63d_slope_v069_signal(percentoftotal, putvalue, marketcap):
    base = percentoftotal * _hedging_intensity(putvalue, marketcap)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_pcthedge_126d_slope_v070_signal(percentoftotal, putvalue, marketcap):
    base = percentoftotal * _hedging_intensity(putvalue, marketcap)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_coverage_63d_slope_v071_signal(totalvalue, marketcap):
    base = totalvalue / marketcap.replace(0, np.nan)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_coverage_126d_slope_v072_signal(totalvalue, marketcap):
    base = totalvalue / marketcap.replace(0, np.nan)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_pcvalratio_63d_slope_v073_signal(putvalue, cllvalue):
    base = _z(np.log(putvalue.replace(0, np.nan) / cllvalue.replace(0, np.nan)), 126)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_pcvalratio_126d_slope_v074_signal(putvalue, cllvalue):
    base = _rank(np.log(putvalue.replace(0, np.nan) / cllvalue.replace(0, np.nan)), 504)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_hedgevswnt_63d_slope_v075_signal(putvalue, wntvalue):
    base = np.log(putvalue.replace(0, np.nan) / wntvalue.replace(0, np.nan))
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_hedgevswnt_126d_slope_v076_signal(putvalue, wntvalue):
    base = np.log(putvalue.replace(0, np.nan) / wntvalue.replace(0, np.nan))
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_callvswnt_63d_slope_v077_signal(cllvalue, wntvalue):
    base = np.log(cllvalue.replace(0, np.nan) / wntvalue.replace(0, np.nan))
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_callvswnt_126d_slope_v078_signal(cllvalue, wntvalue):
    base = np.log(cllvalue.replace(0, np.nan) / wntvalue.replace(0, np.nan))
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_dbtwntbal_63d_slope_v079_signal(dbtvalue, wntvalue):
    base = (dbtvalue - wntvalue) / (dbtvalue + wntvalue).replace(0, np.nan)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_dbtwntbal_126d_slope_v080_signal(dbtvalue, wntvalue):
    base = (dbtvalue - wntvalue) / (dbtvalue + wntvalue).replace(0, np.nan)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_netdilution_63d_slope_v081_signal(wntvalue, dbtvalue, cllvalue, marketcap):
    base = (wntvalue + dbtvalue - cllvalue) / marketcap.replace(0, np.nan)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_netdilution_126d_slope_v082_signal(wntvalue, dbtvalue, cllvalue, marketcap):
    base = (wntvalue + dbtvalue - cllvalue) / marketcap.replace(0, np.nan)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_wntunitint_63d_slope_v083_signal(wntunits, marketcap):
    base = wntunits / marketcap.replace(0, np.nan)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_wntunitint_126d_slope_v084_signal(wntunits, marketcap):
    base = _mean(wntunits / marketcap.replace(0, np.nan), 63)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_putunitint_63d_slope_v085_signal(putunits, marketcap):
    base = putunits / marketcap.replace(0, np.nan)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_callunitint_63d_slope_v086_signal(cllunits, marketcap):
    base = cllunits / marketcap.replace(0, np.nan)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_wntpx_63d_slope_v087_signal(wntvalue, wntunits):
    base = wntvalue / wntunits.replace(0, np.nan)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_wntpx_126d_slope_v088_signal(wntvalue, wntunits):
    base = _mean(wntvalue / wntunits.replace(0, np.nan), 63)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_putpx_63d_slope_v089_signal(putvalue, putunits):
    base = putvalue / putunits.replace(0, np.nan)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_callpx_63d_slope_v090_signal(cllvalue, cllunits):
    base = cllvalue / cllunits.replace(0, np.nan)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_grossoverT_63d_slope_v091_signal(wntvalue, dbtvalue, totalvalue):
    base = (wntvalue + dbtvalue) / totalvalue.replace(0, np.nan)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_grossoverT_126d_slope_v092_signal(wntvalue, dbtvalue, totalvalue):
    base = (wntvalue + dbtvalue) / totalvalue.replace(0, np.nan)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_putoptshare_63d_slope_v093_signal(putvalue, cllvalue, wntvalue):
    base = putvalue / (putvalue + cllvalue + wntvalue).replace(0, np.nan)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_calloptshare_63d_slope_v094_signal(putvalue, cllvalue, wntvalue):
    base = _rank(cllvalue / (putvalue + cllvalue + wntvalue).replace(0, np.nan), 252)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_dbtequity_63d_slope_v095_signal(dbtvalue, shrvalue):
    base = _z(dbtvalue / shrvalue.replace(0, np.nan), 252)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_dbtequity_126d_slope_v096_signal(dbtvalue, shrvalue):
    base = _rank(dbtvalue / shrvalue.replace(0, np.nan), 504)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_wntholdshare_63d_slope_v097_signal(wntholders, putholders, cllholders, dbtholders):
    base = wntholders / (putholders + cllholders + wntholders + dbtholders).replace(0, np.nan)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_dbtholdshare_63d_slope_v098_signal(dbtholders, putholders, cllholders, wntholders):
    base = dbtholders / (putholders + cllholders + wntholders + dbtholders).replace(0, np.nan)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_breadthdiv_63d_slope_v099_signal(putholders, cllholders):
    base = _z(putholders, 252) - _z(cllholders, 252)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_breadthdiv_126d_slope_v100_signal(putholders, cllholders):
    base = _z(putholders, 252) - _z(cllholders, 252)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_wntputtilt_63d_slope_v101_signal(wntholders, putholders):
    base = (wntholders - putholders) / (wntholders + putholders).replace(0, np.nan)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_dbtwnttilt_63d_slope_v102_signal(dbtholders, wntholders):
    base = (dbtholders - wntholders) / (dbtholders + wntholders).replace(0, np.nan)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_ticketskew_63d_slope_v103_signal(putvalue, putholders, cllvalue, cllholders):
    pt = _avg_ticket(putvalue, putholders)
    ct = _avg_ticket(cllvalue, cllholders)
    base = (pt - ct) / (pt + ct).replace(0, np.nan)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_ticketskew_126d_slope_v104_signal(putvalue, putholders, cllvalue, cllholders):
    pt = _avg_ticket(putvalue, putholders)
    ct = _avg_ticket(cllvalue, cllholders)
    base = (pt - ct) / (pt + ct).replace(0, np.nan)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_wnthedgeratio_63d_slope_v105_signal(wntvalue, putvalue):
    base = _z(wntvalue / (wntvalue + putvalue).replace(0, np.nan), 252)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_wnthedgeratio_126d_slope_v106_signal(wntvalue, putvalue):
    base = _rank(wntvalue / (wntvalue + putvalue).replace(0, np.nan), 504)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_optvsequity_63d_slope_v107_signal(putvalue, cllvalue, shrvalue):
    base = _z((cllvalue + putvalue) / shrvalue.replace(0, np.nan), 252)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_optvsequity_126d_slope_v108_signal(putvalue, cllvalue, shrvalue):
    base = _rank((cllvalue + putvalue) / shrvalue.replace(0, np.nan), 504)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_bulloffset_63d_slope_v109_signal(cllvalue, putvalue, wntvalue, marketcap):
    bull = cllvalue / marketcap.replace(0, np.nan)
    bear = (putvalue + wntvalue) / marketcap.replace(0, np.nan)
    base = (bull - bear) / (bull + bear).replace(0, np.nan)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_bulloffset_126d_slope_v110_signal(cllvalue, putvalue, wntvalue, marketcap):
    bull = cllvalue / marketcap.replace(0, np.nan)
    bear = (putvalue + wntvalue) / marketcap.replace(0, np.nan)
    base = (bull - bear) / (bull + bear).replace(0, np.nan)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_skewdiverge_63d_slope_v111_signal(putholders, cllholders, putvalue, cllvalue):
    hs = _put_call_holder_skew(putholders, cllholders)
    vs = _put_call_value_skew(putvalue, cllvalue)
    base = _z(hs - vs, 252)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_skewdiverge_126d_slope_v112_signal(putholders, cllholders, putvalue, cllvalue):
    hs = _put_call_holder_skew(putholders, cllholders)
    vs = _put_call_value_skew(putvalue, cllvalue)
    base = _rank(hs - vs, 504)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_derivtot_63d_slope_v113_signal(putvalue, cllvalue, wntvalue, totalvalue):
    base = _z((putvalue + cllvalue + wntvalue) / totalvalue.replace(0, np.nan), 252)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_derivtot_126d_slope_v114_signal(putvalue, cllvalue, wntvalue, totalvalue):
    base = _rank((putvalue + cllvalue + wntvalue) / totalvalue.replace(0, np.nan), 504)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_fullclaim_63d_slope_v115_signal(putvalue, cllvalue, wntvalue, dbtvalue, shrvalue):
    base = _z(np.log((putvalue + cllvalue + wntvalue + dbtvalue).replace(0, np.nan) / shrvalue.replace(0, np.nan)), 252)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_fullclaim_126d_slope_v116_signal(putvalue, cllvalue, wntvalue, dbtvalue, shrvalue):
    base = _rank((putvalue + cllvalue + wntvalue + dbtvalue) / shrvalue.replace(0, np.nan), 504)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_pcpx_63d_slope_v117_signal(putvalue, putunits, cllvalue, cllunits):
    pp = putvalue / putunits.replace(0, np.nan)
    cp = cllvalue / cllunits.replace(0, np.nan)
    base = (pp - cp) / (pp + cp).replace(0, np.nan)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_pcpx_126d_slope_v118_signal(putvalue, putunits, cllvalue, cllunits):
    pp = putvalue / putunits.replace(0, np.nan)
    cp = cllvalue / cllunits.replace(0, np.nan)
    base = (pp - cp) / (pp + cp).replace(0, np.nan)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_putunitconc_63d_slope_v119_signal(putunits, putholders):
    base = putunits / putholders.replace(0, np.nan)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_callunitconc_63d_slope_v120_signal(cllunits, cllholders):
    base = cllunits / cllholders.replace(0, np.nan)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_wntunitconc_63d_slope_v121_signal(wntunits, wntholders):
    base = wntunits / wntholders.replace(0, np.nan)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_wntunitconc_126d_slope_v122_signal(wntunits, wntholders):
    base = wntunits / wntholders.replace(0, np.nan)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_totholders_63d_slope_v123_signal(putholders, cllholders, wntholders, dbtholders):
    base = _z(putholders + cllholders + wntholders + dbtholders, 252)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_totholders_126d_slope_v124_signal(putholders, cllholders, wntholders, dbtholders):
    base = _z(putholders + cllholders + wntholders + dbtholders, 252)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_putshr_63d_slope_v125_signal(putvalue, shrvalue):
    base = _z(putvalue / shrvalue.replace(0, np.nan), 252)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_callshr_63d_slope_v126_signal(cllvalue, shrvalue):
    base = cllvalue / shrvalue.replace(0, np.nan)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_wntshr_63d_slope_v127_signal(wntvalue, shrvalue):
    base = _z(wntvalue / shrvalue.replace(0, np.nan), 252)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_wntshr_126d_slope_v128_signal(wntvalue, shrvalue):
    base = _rank(wntvalue / shrvalue.replace(0, np.nan), 504)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_overhangpress_63d_slope_v129_signal(wntvalue, dbtvalue, putvalue, marketcap):
    base = (wntvalue + dbtvalue + putvalue) / marketcap.replace(0, np.nan)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_overhangpress_126d_slope_v130_signal(wntvalue, dbtvalue, putvalue, marketcap):
    base = (wntvalue + dbtvalue + putvalue) / marketcap.replace(0, np.nan)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_pctdilute_63d_slope_v131_signal(percentoftotal, wntvalue, totalvalue):
    base = percentoftotal * _warrant_overhang_total(wntvalue, totalvalue)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_pctdilute_126d_slope_v132_signal(percentoftotal, wntvalue, totalvalue):
    base = percentoftotal * _warrant_overhang_total(wntvalue, totalvalue)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_pctdbt_63d_slope_v133_signal(percentoftotal, dbtvalue, totalvalue):
    base = percentoftotal * _debt_overhang(dbtvalue, totalvalue)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_callvswntval_63d_slope_v134_signal(cllvalue, wntvalue, marketcap):
    base = (cllvalue - wntvalue) / marketcap.replace(0, np.nan)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_callvswntval_126d_slope_v135_signal(cllvalue, wntvalue, marketcap):
    base = (cllvalue - wntvalue) / marketcap.replace(0, np.nan)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_dbtvswnt_63d_slope_v136_signal(dbtvalue, wntvalue, marketcap):
    base = _z((dbtvalue - wntvalue) / marketcap.replace(0, np.nan), 252)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_wntunitshr_63d_slope_v137_signal(wntunits, shrvalue):
    base = wntunits / shrvalue.replace(0, np.nan)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_putunitshr_63d_slope_v138_signal(putunits, shrvalue):
    base = putunits / shrvalue.replace(0, np.nan)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_optsize_63d_slope_v139_signal(putvalue, cllvalue, putholders, cllholders):
    base = (putvalue + cllvalue) / (putholders + cllholders).replace(0, np.nan)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_optsize_126d_slope_v140_signal(putvalue, cllvalue, putholders, cllholders):
    base = (putvalue + cllvalue) / (putholders + cllholders).replace(0, np.nan)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_putfrag_63d_slope_v141_signal(putholders, putvalue):
    base = putholders / putvalue.replace(0, np.nan)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_wntfrag_63d_slope_v142_signal(wntholders, wntvalue):
    base = wntholders / wntvalue.replace(0, np.nan)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_dbtwntholdtilt_126d_slope_v143_signal(dbtholders, wntholders):
    base = (dbtholders - wntholders) / (dbtholders + wntholders).replace(0, np.nan)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_bearcomp_63d_slope_v144_signal(putvalue, cllvalue, wntvalue, dbtvalue, totalvalue):
    skew = _put_call_value_skew(putvalue, cllvalue)
    over = (wntvalue + dbtvalue) / totalvalue.replace(0, np.nan)
    base = _z(skew + 4.0 * over, 252)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_bearcomp_126d_slope_v145_signal(putvalue, cllvalue, wntvalue, dbtvalue, totalvalue):
    skew = _put_call_value_skew(putvalue, cllvalue)
    over = (wntvalue + dbtvalue) / totalvalue.replace(0, np.nan)
    base = _rank(skew + 4.0 * over, 504)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_dbtequityratio_63d_slope_v146_signal(dbtvalue, dbtholders, marketcap):
    base = (dbtvalue / dbtholders.replace(0, np.nan)) / marketcap.replace(0, np.nan)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_wntpxmcap_63d_slope_v147_signal(wntvalue, wntunits, marketcap):
    base = (wntvalue / wntunits.replace(0, np.nan)) / marketcap.replace(0, np.nan)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_callhedgebal_63d_slope_v148_signal(cllvalue, putvalue, wntvalue):
    base = _z(cllvalue / (cllvalue + putvalue + wntvalue).replace(0, np.nan), 252)
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_callhedgebal_126d_slope_v149_signal(cllvalue, putvalue, wntvalue):
    base = _rank(cllvalue / (cllvalue + putvalue + wntvalue).replace(0, np.nan), 504)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f46ow_f46_options_warrant_positioning_latentT_63d_slope_v150_signal(wntvalue, dbtvalue, totalvalue):
    base = _rank((wntvalue + dbtvalue) / totalvalue.replace(0, np.nan), 504)
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f46ow_f46_options_warrant_positioning_pcvalskew_63d_slope_v001_signal,
    f46ow_f46_options_warrant_positioning_pcvalskew_63d_slope_v002_signal,
    f46ow_f46_options_warrant_positioning_pcvalskew_126d_slope_v003_signal,
    f46ow_f46_options_warrant_positioning_pcvalskew_252d_slope_v004_signal,
    f46ow_f46_options_warrant_positioning_pcholdskew_63d_slope_v005_signal,
    f46ow_f46_options_warrant_positioning_pcholdskew_63d_slope_v006_signal,
    f46ow_f46_options_warrant_positioning_pcholdskew_252d_slope_v007_signal,
    f46ow_f46_options_warrant_positioning_hedgeint_63d_slope_v008_signal,
    f46ow_f46_options_warrant_positioning_hedgeint_63d_slope_v009_signal,
    f46ow_f46_options_warrant_positioning_hedgeint_126d_slope_v010_signal,
    f46ow_f46_options_warrant_positioning_hedgeint_252d_slope_v011_signal,
    f46ow_f46_options_warrant_positioning_callint_63d_slope_v012_signal,
    f46ow_f46_options_warrant_positioning_callint_63d_slope_v013_signal,
    f46ow_f46_options_warrant_positioning_callint_252d_slope_v014_signal,
    f46ow_f46_options_warrant_positioning_wntoverM_63d_slope_v015_signal,
    f46ow_f46_options_warrant_positioning_wntoverM_63d_slope_v016_signal,
    f46ow_f46_options_warrant_positioning_wntoverM_126d_slope_v017_signal,
    f46ow_f46_options_warrant_positioning_wntoverM_252d_slope_v018_signal,
    f46ow_f46_options_warrant_positioning_wntoverT_63d_slope_v019_signal,
    f46ow_f46_options_warrant_positioning_wntoverT_63d_slope_v020_signal,
    f46ow_f46_options_warrant_positioning_wntoverT_252d_slope_v021_signal,
    f46ow_f46_options_warrant_positioning_dbtover_63d_slope_v022_signal,
    f46ow_f46_options_warrant_positioning_dbtover_63d_slope_v023_signal,
    f46ow_f46_options_warrant_positioning_dbtover_252d_slope_v024_signal,
    f46ow_f46_options_warrant_positioning_derivshare_63d_slope_v025_signal,
    f46ow_f46_options_warrant_positioning_derivshare_63d_slope_v026_signal,
    f46ow_f46_options_warrant_positioning_derivshare_252d_slope_v027_signal,
    f46ow_f46_options_warrant_positioning_grossopt_63d_slope_v028_signal,
    f46ow_f46_options_warrant_positioning_grossopt_63d_slope_v029_signal,
    f46ow_f46_options_warrant_positioning_grossopt_252d_slope_v030_signal,
    f46ow_f46_options_warrant_positioning_latentsup_63d_slope_v031_signal,
    f46ow_f46_options_warrant_positioning_latentsup_63d_slope_v032_signal,
    f46ow_f46_options_warrant_positioning_latentsup_252d_slope_v033_signal,
    f46ow_f46_options_warrant_positioning_netbear_63d_slope_v034_signal,
    f46ow_f46_options_warrant_positioning_netbear_63d_slope_v035_signal,
    f46ow_f46_options_warrant_positioning_netbear_252d_slope_v036_signal,
    f46ow_f46_options_warrant_positioning_putbreadth_63d_slope_v037_signal,
    f46ow_f46_options_warrant_positioning_putbreadth_126d_slope_v038_signal,
    f46ow_f46_options_warrant_positioning_callbreadth_63d_slope_v039_signal,
    f46ow_f46_options_warrant_positioning_callbreadth_126d_slope_v040_signal,
    f46ow_f46_options_warrant_positioning_wntbreadth_63d_slope_v041_signal,
    f46ow_f46_options_warrant_positioning_wntbreadth_126d_slope_v042_signal,
    f46ow_f46_options_warrant_positioning_dbtbreadth_63d_slope_v043_signal,
    f46ow_f46_options_warrant_positioning_dbtbreadth_126d_slope_v044_signal,
    f46ow_f46_options_warrant_positioning_putticket_63d_slope_v045_signal,
    f46ow_f46_options_warrant_positioning_putticket_126d_slope_v046_signal,
    f46ow_f46_options_warrant_positioning_callticket_63d_slope_v047_signal,
    f46ow_f46_options_warrant_positioning_callticket_126d_slope_v048_signal,
    f46ow_f46_options_warrant_positioning_wntticket_63d_slope_v049_signal,
    f46ow_f46_options_warrant_positioning_wntticket_126d_slope_v050_signal,
    f46ow_f46_options_warrant_positioning_dbtticket_63d_slope_v051_signal,
    f46ow_f46_options_warrant_positioning_dbtticket_126d_slope_v052_signal,
    f46ow_f46_options_warrant_positioning_putvaltot_63d_slope_v053_signal,
    f46ow_f46_options_warrant_positioning_putvaltot_126d_slope_v054_signal,
    f46ow_f46_options_warrant_positioning_callvaltot_63d_slope_v055_signal,
    f46ow_f46_options_warrant_positioning_callvaltot_126d_slope_v056_signal,
    f46ow_f46_options_warrant_positioning_hedgepurity_63d_slope_v057_signal,
    f46ow_f46_options_warrant_positioning_hedgepurity_126d_slope_v058_signal,
    f46ow_f46_options_warrant_positioning_wntoptshare_63d_slope_v059_signal,
    f46ow_f46_options_warrant_positioning_wntoptshare_126d_slope_v060_signal,
    f46ow_f46_options_warrant_positioning_dbtdom_63d_slope_v061_signal,
    f46ow_f46_options_warrant_positioning_dbtdom_126d_slope_v062_signal,
    f46ow_f46_options_warrant_positioning_unitskew_63d_slope_v063_signal,
    f46ow_f46_options_warrant_positioning_unitskew_126d_slope_v064_signal,
    f46ow_f46_options_warrant_positioning_wntunitshare_63d_slope_v065_signal,
    f46ow_f46_options_warrant_positioning_wntunitshare_126d_slope_v066_signal,
    f46ow_f46_options_warrant_positioning_pctlevel_63d_slope_v067_signal,
    f46ow_f46_options_warrant_positioning_pctlevel_126d_slope_v068_signal,
    f46ow_f46_options_warrant_positioning_pcthedge_63d_slope_v069_signal,
    f46ow_f46_options_warrant_positioning_pcthedge_126d_slope_v070_signal,
    f46ow_f46_options_warrant_positioning_coverage_63d_slope_v071_signal,
    f46ow_f46_options_warrant_positioning_coverage_126d_slope_v072_signal,
    f46ow_f46_options_warrant_positioning_pcvalratio_63d_slope_v073_signal,
    f46ow_f46_options_warrant_positioning_pcvalratio_126d_slope_v074_signal,
    f46ow_f46_options_warrant_positioning_hedgevswnt_63d_slope_v075_signal,
    f46ow_f46_options_warrant_positioning_hedgevswnt_126d_slope_v076_signal,
    f46ow_f46_options_warrant_positioning_callvswnt_63d_slope_v077_signal,
    f46ow_f46_options_warrant_positioning_callvswnt_126d_slope_v078_signal,
    f46ow_f46_options_warrant_positioning_dbtwntbal_63d_slope_v079_signal,
    f46ow_f46_options_warrant_positioning_dbtwntbal_126d_slope_v080_signal,
    f46ow_f46_options_warrant_positioning_netdilution_63d_slope_v081_signal,
    f46ow_f46_options_warrant_positioning_netdilution_126d_slope_v082_signal,
    f46ow_f46_options_warrant_positioning_wntunitint_63d_slope_v083_signal,
    f46ow_f46_options_warrant_positioning_wntunitint_126d_slope_v084_signal,
    f46ow_f46_options_warrant_positioning_putunitint_63d_slope_v085_signal,
    f46ow_f46_options_warrant_positioning_callunitint_63d_slope_v086_signal,
    f46ow_f46_options_warrant_positioning_wntpx_63d_slope_v087_signal,
    f46ow_f46_options_warrant_positioning_wntpx_126d_slope_v088_signal,
    f46ow_f46_options_warrant_positioning_putpx_63d_slope_v089_signal,
    f46ow_f46_options_warrant_positioning_callpx_63d_slope_v090_signal,
    f46ow_f46_options_warrant_positioning_grossoverT_63d_slope_v091_signal,
    f46ow_f46_options_warrant_positioning_grossoverT_126d_slope_v092_signal,
    f46ow_f46_options_warrant_positioning_putoptshare_63d_slope_v093_signal,
    f46ow_f46_options_warrant_positioning_calloptshare_63d_slope_v094_signal,
    f46ow_f46_options_warrant_positioning_dbtequity_63d_slope_v095_signal,
    f46ow_f46_options_warrant_positioning_dbtequity_126d_slope_v096_signal,
    f46ow_f46_options_warrant_positioning_wntholdshare_63d_slope_v097_signal,
    f46ow_f46_options_warrant_positioning_dbtholdshare_63d_slope_v098_signal,
    f46ow_f46_options_warrant_positioning_breadthdiv_63d_slope_v099_signal,
    f46ow_f46_options_warrant_positioning_breadthdiv_126d_slope_v100_signal,
    f46ow_f46_options_warrant_positioning_wntputtilt_63d_slope_v101_signal,
    f46ow_f46_options_warrant_positioning_dbtwnttilt_63d_slope_v102_signal,
    f46ow_f46_options_warrant_positioning_ticketskew_63d_slope_v103_signal,
    f46ow_f46_options_warrant_positioning_ticketskew_126d_slope_v104_signal,
    f46ow_f46_options_warrant_positioning_wnthedgeratio_63d_slope_v105_signal,
    f46ow_f46_options_warrant_positioning_wnthedgeratio_126d_slope_v106_signal,
    f46ow_f46_options_warrant_positioning_optvsequity_63d_slope_v107_signal,
    f46ow_f46_options_warrant_positioning_optvsequity_126d_slope_v108_signal,
    f46ow_f46_options_warrant_positioning_bulloffset_63d_slope_v109_signal,
    f46ow_f46_options_warrant_positioning_bulloffset_126d_slope_v110_signal,
    f46ow_f46_options_warrant_positioning_skewdiverge_63d_slope_v111_signal,
    f46ow_f46_options_warrant_positioning_skewdiverge_126d_slope_v112_signal,
    f46ow_f46_options_warrant_positioning_derivtot_63d_slope_v113_signal,
    f46ow_f46_options_warrant_positioning_derivtot_126d_slope_v114_signal,
    f46ow_f46_options_warrant_positioning_fullclaim_63d_slope_v115_signal,
    f46ow_f46_options_warrant_positioning_fullclaim_126d_slope_v116_signal,
    f46ow_f46_options_warrant_positioning_pcpx_63d_slope_v117_signal,
    f46ow_f46_options_warrant_positioning_pcpx_126d_slope_v118_signal,
    f46ow_f46_options_warrant_positioning_putunitconc_63d_slope_v119_signal,
    f46ow_f46_options_warrant_positioning_callunitconc_63d_slope_v120_signal,
    f46ow_f46_options_warrant_positioning_wntunitconc_63d_slope_v121_signal,
    f46ow_f46_options_warrant_positioning_wntunitconc_126d_slope_v122_signal,
    f46ow_f46_options_warrant_positioning_totholders_63d_slope_v123_signal,
    f46ow_f46_options_warrant_positioning_totholders_126d_slope_v124_signal,
    f46ow_f46_options_warrant_positioning_putshr_63d_slope_v125_signal,
    f46ow_f46_options_warrant_positioning_callshr_63d_slope_v126_signal,
    f46ow_f46_options_warrant_positioning_wntshr_63d_slope_v127_signal,
    f46ow_f46_options_warrant_positioning_wntshr_126d_slope_v128_signal,
    f46ow_f46_options_warrant_positioning_overhangpress_63d_slope_v129_signal,
    f46ow_f46_options_warrant_positioning_overhangpress_126d_slope_v130_signal,
    f46ow_f46_options_warrant_positioning_pctdilute_63d_slope_v131_signal,
    f46ow_f46_options_warrant_positioning_pctdilute_126d_slope_v132_signal,
    f46ow_f46_options_warrant_positioning_pctdbt_63d_slope_v133_signal,
    f46ow_f46_options_warrant_positioning_callvswntval_63d_slope_v134_signal,
    f46ow_f46_options_warrant_positioning_callvswntval_126d_slope_v135_signal,
    f46ow_f46_options_warrant_positioning_dbtvswnt_63d_slope_v136_signal,
    f46ow_f46_options_warrant_positioning_wntunitshr_63d_slope_v137_signal,
    f46ow_f46_options_warrant_positioning_putunitshr_63d_slope_v138_signal,
    f46ow_f46_options_warrant_positioning_optsize_63d_slope_v139_signal,
    f46ow_f46_options_warrant_positioning_optsize_126d_slope_v140_signal,
    f46ow_f46_options_warrant_positioning_putfrag_63d_slope_v141_signal,
    f46ow_f46_options_warrant_positioning_wntfrag_63d_slope_v142_signal,
    f46ow_f46_options_warrant_positioning_dbtwntholdtilt_126d_slope_v143_signal,
    f46ow_f46_options_warrant_positioning_bearcomp_63d_slope_v144_signal,
    f46ow_f46_options_warrant_positioning_bearcomp_126d_slope_v145_signal,
    f46ow_f46_options_warrant_positioning_dbtequityratio_63d_slope_v146_signal,
    f46ow_f46_options_warrant_positioning_wntpxmcap_63d_slope_v147_signal,
    f46ow_f46_options_warrant_positioning_callhedgebal_63d_slope_v148_signal,
    f46ow_f46_options_warrant_positioning_callhedgebal_126d_slope_v149_signal,
    f46ow_f46_options_warrant_positioning_latentT_63d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F46_OPTIONS_WARRANT_POSITIONING_REGISTRY_2ND_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.0, vol=0.08, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.5
        return pd.Series(s, name=None)

    putholders = _fund(101, base=40.0, drift=0.01, vol=0.10).rename("putholders")
    cllholders = _fund(102, base=55.0, drift=0.012, vol=0.10).rename("cllholders")
    wntholders = _fund(103, base=18.0, drift=-0.005, vol=0.12).rename("wntholders")
    dbtholders = _fund(104, base=12.0, drift=0.004, vol=0.13).rename("dbtholders")
    putunits = _fund(105, base=2.0e6, drift=0.006, vol=0.14).rename("putunits")
    cllunits = _fund(106, base=2.6e6, drift=0.009, vol=0.14).rename("cllunits")
    wntunits = _fund(107, base=1.4e6, drift=0.002, vol=0.16).rename("wntunits")
    putvalue = _fund(108, base=9.0e6, drift=0.005, vol=0.13).rename("putvalue")
    cllvalue = _fund(109, base=1.1e7, drift=0.011, vol=0.13).rename("cllvalue")
    wntvalue = _fund(110, base=6.0e6, drift=0.003, vol=0.15).rename("wntvalue")
    dbtvalue = _fund(111, base=8.0e6, drift=0.004, vol=0.14).rename("dbtvalue")
    shrvalue = _fund(112, base=1.2e8, drift=0.010, vol=0.09).rename("shrvalue")
    totalvalue = (putvalue + cllvalue + wntvalue + dbtvalue + shrvalue).rename("totalvalue")
    marketcap = _fund(113, base=4.0e8, drift=0.008, vol=0.11).rename("marketcap")
    percentoftotal = (_fund(114, base=0.4, drift=0.0, vol=0.10)
                      .clip(0.01, 0.99)).rename("percentoftotal")

    cols = {
        "putholders": putholders, "cllholders": cllholders, "wntholders": wntholders,
        "dbtholders": dbtholders, "putunits": putunits, "cllunits": cllunits,
        "wntunits": wntunits, "putvalue": putvalue, "cllvalue": cllvalue,
        "wntvalue": wntvalue, "dbtvalue": dbtvalue, "shrvalue": shrvalue,
        "totalvalue": totalvalue, "marketcap": marketcap, "percentoftotal": percentoftotal,
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

    print("OK f46_options_warrant_positioning_2nd_derivatives_001_150_claude: %d features pass" % n_features)
