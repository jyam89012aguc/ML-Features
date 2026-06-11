import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


# core00 mean_5d
def cg_f100_technology_f100_technology_multi_source_master_core00_mean_5d_2nd_v001_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(_pct_change(closeadj,252),_std(_pct_change(closeadj,1),63).abs()+1e-9)
    base = _mean(series,5)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core01 mean_5d
def cg_f100_technology_f100_technology_multi_source_master_core01_mean_5d_2nd_v002_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(_diff(revenue,252),revenue.abs()+1e-9)
    base = _mean(series,5)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core02 mean_5d
def cg_f100_technology_f100_technology_multi_source_master_core02_mean_5d_2nd_v003_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(fcf,revenue.abs()+1e-9)
    base = _mean(series,5)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core03 mean_5d
def cg_f100_technology_f100_technology_multi_source_master_core03_mean_5d_2nd_v004_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = roic+grossmargin
    base = _mean(series,5)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core04 mean_5d
def cg_f100_technology_f100_technology_multi_source_master_core04_mean_5d_2nd_v005_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(rnd,revenue.abs()+1e-9)
    base = _mean(series,5)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core05 mean_5d
def cg_f100_technology_f100_technology_multi_source_master_core05_mean_5d_2nd_v006_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _event_rate(action_count,252)+0.01*_z(volume,126)
    base = _mean(series,5)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core06 mean_5d
def cg_f100_technology_f100_technology_multi_source_master_core06_mean_5d_2nd_v007_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _event_rate(event_count,252)+0.01*_z(_pct_change(closeadj,21),126)
    base = _mean(series,5)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core07 mean_5d
def cg_f100_technology_f100_technology_multi_source_master_core07_mean_5d_2nd_v008_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(insider_net_value,marketcap.abs()+1e-9)
    base = _mean(series,5)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core08 mean_5d
def cg_f100_technology_f100_technology_multi_source_master_core08_mean_5d_2nd_v009_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(insider_buy_value-insider_sell_value,(insider_buy_value+insider_sell_value).abs()+1e-9) * _rank(volume,252)
    base = _mean(series,5)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core09 mean_5d
def cg_f100_technology_f100_technology_multi_source_master_core09_mean_5d_2nd_v010_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(inst_value,marketcap.abs()+1e-9)+inst_share
    base = _mean(series,5)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core00 mean_21d
def cg_f100_technology_f100_technology_multi_source_master_core00_mean_21d_2nd_v011_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(_pct_change(closeadj,252),_std(_pct_change(closeadj,1),63).abs()+1e-9)
    base = _mean(series,21)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core01 mean_21d
def cg_f100_technology_f100_technology_multi_source_master_core01_mean_21d_2nd_v012_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(_diff(revenue,252),revenue.abs()+1e-9)
    base = _mean(series,21)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core02 mean_21d
def cg_f100_technology_f100_technology_multi_source_master_core02_mean_21d_2nd_v013_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(fcf,revenue.abs()+1e-9)
    base = _mean(series,21)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core03 mean_21d
def cg_f100_technology_f100_technology_multi_source_master_core03_mean_21d_2nd_v014_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = roic+grossmargin
    base = _mean(series,21)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core04 mean_21d
def cg_f100_technology_f100_technology_multi_source_master_core04_mean_21d_2nd_v015_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(rnd,revenue.abs()+1e-9)
    base = _mean(series,21)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core05 mean_21d
def cg_f100_technology_f100_technology_multi_source_master_core05_mean_21d_2nd_v016_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _event_rate(action_count,252)+0.01*_z(volume,126)
    base = _mean(series,21)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core06 mean_21d
def cg_f100_technology_f100_technology_multi_source_master_core06_mean_21d_2nd_v017_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _event_rate(event_count,252)+0.01*_z(_pct_change(closeadj,21),126)
    base = _mean(series,21)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core07 mean_21d
def cg_f100_technology_f100_technology_multi_source_master_core07_mean_21d_2nd_v018_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(insider_net_value,marketcap.abs()+1e-9)
    base = _mean(series,21)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core08 mean_21d
def cg_f100_technology_f100_technology_multi_source_master_core08_mean_21d_2nd_v019_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(insider_buy_value-insider_sell_value,(insider_buy_value+insider_sell_value).abs()+1e-9) * _rank(volume,252)
    base = _mean(series,21)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core09 mean_21d
def cg_f100_technology_f100_technology_multi_source_master_core09_mean_21d_2nd_v020_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(inst_value,marketcap.abs()+1e-9)+inst_share
    base = _mean(series,21)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core00 mean_63d
def cg_f100_technology_f100_technology_multi_source_master_core00_mean_63d_2nd_v021_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(_pct_change(closeadj,252),_std(_pct_change(closeadj,1),63).abs()+1e-9)
    base = _mean(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core01 mean_63d
def cg_f100_technology_f100_technology_multi_source_master_core01_mean_63d_2nd_v022_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(_diff(revenue,252),revenue.abs()+1e-9)
    base = _mean(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core02 mean_63d
def cg_f100_technology_f100_technology_multi_source_master_core02_mean_63d_2nd_v023_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(fcf,revenue.abs()+1e-9)
    base = _mean(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core03 mean_63d
def cg_f100_technology_f100_technology_multi_source_master_core03_mean_63d_2nd_v024_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = roic+grossmargin
    base = _mean(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core04 mean_63d
def cg_f100_technology_f100_technology_multi_source_master_core04_mean_63d_2nd_v025_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(rnd,revenue.abs()+1e-9)
    base = _mean(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core05 mean_63d
def cg_f100_technology_f100_technology_multi_source_master_core05_mean_63d_2nd_v026_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _event_rate(action_count,252)+0.01*_z(volume,126)
    base = _mean(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core06 mean_63d
def cg_f100_technology_f100_technology_multi_source_master_core06_mean_63d_2nd_v027_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _event_rate(event_count,252)+0.01*_z(_pct_change(closeadj,21),126)
    base = _mean(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core07 mean_63d
def cg_f100_technology_f100_technology_multi_source_master_core07_mean_63d_2nd_v028_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(insider_net_value,marketcap.abs()+1e-9)
    base = _mean(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core08 mean_63d
def cg_f100_technology_f100_technology_multi_source_master_core08_mean_63d_2nd_v029_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(insider_buy_value-insider_sell_value,(insider_buy_value+insider_sell_value).abs()+1e-9) * _rank(volume,252)
    base = _mean(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core09 mean_63d
def cg_f100_technology_f100_technology_multi_source_master_core09_mean_63d_2nd_v030_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(inst_value,marketcap.abs()+1e-9)+inst_share
    base = _mean(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core00 z_63d
def cg_f100_technology_f100_technology_multi_source_master_core00_z_63d_2nd_v031_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(_pct_change(closeadj,252),_std(_pct_change(closeadj,1),63).abs()+1e-9)
    base = _z(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core01 z_63d
def cg_f100_technology_f100_technology_multi_source_master_core01_z_63d_2nd_v032_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(_diff(revenue,252),revenue.abs()+1e-9)
    base = _z(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core02 z_63d
def cg_f100_technology_f100_technology_multi_source_master_core02_z_63d_2nd_v033_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(fcf,revenue.abs()+1e-9)
    base = _z(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core03 z_63d
def cg_f100_technology_f100_technology_multi_source_master_core03_z_63d_2nd_v034_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = roic+grossmargin
    base = _z(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core04 z_63d
def cg_f100_technology_f100_technology_multi_source_master_core04_z_63d_2nd_v035_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(rnd,revenue.abs()+1e-9)
    base = _z(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core05 z_63d
def cg_f100_technology_f100_technology_multi_source_master_core05_z_63d_2nd_v036_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _event_rate(action_count,252)+0.01*_z(volume,126)
    base = _z(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core06 z_63d
def cg_f100_technology_f100_technology_multi_source_master_core06_z_63d_2nd_v037_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _event_rate(event_count,252)+0.01*_z(_pct_change(closeadj,21),126)
    base = _z(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core07 z_63d
def cg_f100_technology_f100_technology_multi_source_master_core07_z_63d_2nd_v038_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(insider_net_value,marketcap.abs()+1e-9)
    base = _z(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core08 z_63d
def cg_f100_technology_f100_technology_multi_source_master_core08_z_63d_2nd_v039_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(insider_buy_value-insider_sell_value,(insider_buy_value+insider_sell_value).abs()+1e-9) * _rank(volume,252)
    base = _z(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core09 z_63d
def cg_f100_technology_f100_technology_multi_source_master_core09_z_63d_2nd_v040_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(inst_value,marketcap.abs()+1e-9)+inst_share
    base = _z(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core00 z_252d
def cg_f100_technology_f100_technology_multi_source_master_core00_z_252d_2nd_v041_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(_pct_change(closeadj,252),_std(_pct_change(closeadj,1),63).abs()+1e-9)
    base = _z(series,252)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core01 z_252d
def cg_f100_technology_f100_technology_multi_source_master_core01_z_252d_2nd_v042_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(_diff(revenue,252),revenue.abs()+1e-9)
    base = _z(series,252)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core02 z_252d
def cg_f100_technology_f100_technology_multi_source_master_core02_z_252d_2nd_v043_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(fcf,revenue.abs()+1e-9)
    base = _z(series,252)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core03 z_252d
def cg_f100_technology_f100_technology_multi_source_master_core03_z_252d_2nd_v044_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = roic+grossmargin
    base = _z(series,252)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core04 z_252d
def cg_f100_technology_f100_technology_multi_source_master_core04_z_252d_2nd_v045_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(rnd,revenue.abs()+1e-9)
    base = _z(series,252)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core05 z_252d
def cg_f100_technology_f100_technology_multi_source_master_core05_z_252d_2nd_v046_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _event_rate(action_count,252)+0.01*_z(volume,126)
    base = _z(series,252)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core06 z_252d
def cg_f100_technology_f100_technology_multi_source_master_core06_z_252d_2nd_v047_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _event_rate(event_count,252)+0.01*_z(_pct_change(closeadj,21),126)
    base = _z(series,252)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core07 z_252d
def cg_f100_technology_f100_technology_multi_source_master_core07_z_252d_2nd_v048_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(insider_net_value,marketcap.abs()+1e-9)
    base = _z(series,252)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core08 z_252d
def cg_f100_technology_f100_technology_multi_source_master_core08_z_252d_2nd_v049_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(insider_buy_value-insider_sell_value,(insider_buy_value+insider_sell_value).abs()+1e-9) * _rank(volume,252)
    base = _z(series,252)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core09 z_252d
def cg_f100_technology_f100_technology_multi_source_master_core09_z_252d_2nd_v050_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(inst_value,marketcap.abs()+1e-9)+inst_share
    base = _z(series,252)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core00 rank_126d
def cg_f100_technology_f100_technology_multi_source_master_core00_rank_126d_2nd_v051_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(_pct_change(closeadj,252),_std(_pct_change(closeadj,1),63).abs()+1e-9)
    base = _rank(series,126)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core01 rank_126d
def cg_f100_technology_f100_technology_multi_source_master_core01_rank_126d_2nd_v052_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(_diff(revenue,252),revenue.abs()+1e-9)
    base = _rank(series,126)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core02 rank_126d
def cg_f100_technology_f100_technology_multi_source_master_core02_rank_126d_2nd_v053_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(fcf,revenue.abs()+1e-9)
    base = _rank(series,126)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core03 rank_126d
def cg_f100_technology_f100_technology_multi_source_master_core03_rank_126d_2nd_v054_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = roic+grossmargin
    base = _rank(series,126)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core04 rank_126d
def cg_f100_technology_f100_technology_multi_source_master_core04_rank_126d_2nd_v055_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(rnd,revenue.abs()+1e-9)
    base = _rank(series,126)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core05 rank_126d
def cg_f100_technology_f100_technology_multi_source_master_core05_rank_126d_2nd_v056_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _event_rate(action_count,252)+0.01*_z(volume,126)
    base = _rank(series,126)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core06 rank_126d
def cg_f100_technology_f100_technology_multi_source_master_core06_rank_126d_2nd_v057_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _event_rate(event_count,252)+0.01*_z(_pct_change(closeadj,21),126)
    base = _rank(series,126)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core07 rank_126d
def cg_f100_technology_f100_technology_multi_source_master_core07_rank_126d_2nd_v058_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(insider_net_value,marketcap.abs()+1e-9)
    base = _rank(series,126)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core08 rank_126d
def cg_f100_technology_f100_technology_multi_source_master_core08_rank_126d_2nd_v059_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(insider_buy_value-insider_sell_value,(insider_buy_value+insider_sell_value).abs()+1e-9) * _rank(volume,252)
    base = _rank(series,126)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core09 rank_126d
def cg_f100_technology_f100_technology_multi_source_master_core09_rank_126d_2nd_v060_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(inst_value,marketcap.abs()+1e-9)+inst_share
    base = _rank(series,126)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core00 std_63d
def cg_f100_technology_f100_technology_multi_source_master_core00_std_63d_2nd_v061_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(_pct_change(closeadj,252),_std(_pct_change(closeadj,1),63).abs()+1e-9)
    base = _std(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core01 std_63d
def cg_f100_technology_f100_technology_multi_source_master_core01_std_63d_2nd_v062_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(_diff(revenue,252),revenue.abs()+1e-9)
    base = _std(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core02 std_63d
def cg_f100_technology_f100_technology_multi_source_master_core02_std_63d_2nd_v063_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(fcf,revenue.abs()+1e-9)
    base = _std(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core03 std_63d
def cg_f100_technology_f100_technology_multi_source_master_core03_std_63d_2nd_v064_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = roic+grossmargin
    base = _std(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core04 std_63d
def cg_f100_technology_f100_technology_multi_source_master_core04_std_63d_2nd_v065_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(rnd,revenue.abs()+1e-9)
    base = _std(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core05 std_63d
def cg_f100_technology_f100_technology_multi_source_master_core05_std_63d_2nd_v066_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _event_rate(action_count,252)+0.01*_z(volume,126)
    base = _std(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core06 std_63d
def cg_f100_technology_f100_technology_multi_source_master_core06_std_63d_2nd_v067_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _event_rate(event_count,252)+0.01*_z(_pct_change(closeadj,21),126)
    base = _std(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core07 std_63d
def cg_f100_technology_f100_technology_multi_source_master_core07_std_63d_2nd_v068_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(insider_net_value,marketcap.abs()+1e-9)
    base = _std(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core08 std_63d
def cg_f100_technology_f100_technology_multi_source_master_core08_std_63d_2nd_v069_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(insider_buy_value-insider_sell_value,(insider_buy_value+insider_sell_value).abs()+1e-9) * _rank(volume,252)
    base = _std(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core09 std_63d
def cg_f100_technology_f100_technology_multi_source_master_core09_std_63d_2nd_v070_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(inst_value,marketcap.abs()+1e-9)+inst_share
    base = _std(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core00 delta_21d
def cg_f100_technology_f100_technology_multi_source_master_core00_delta_21d_2nd_v071_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(_pct_change(closeadj,252),_std(_pct_change(closeadj,1),63).abs()+1e-9)
    base = _diff(series,21)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core01 delta_21d
def cg_f100_technology_f100_technology_multi_source_master_core01_delta_21d_2nd_v072_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(_diff(revenue,252),revenue.abs()+1e-9)
    base = _diff(series,21)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core02 delta_21d
def cg_f100_technology_f100_technology_multi_source_master_core02_delta_21d_2nd_v073_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(fcf,revenue.abs()+1e-9)
    base = _diff(series,21)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core03 delta_21d
def cg_f100_technology_f100_technology_multi_source_master_core03_delta_21d_2nd_v074_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = roic+grossmargin
    base = _diff(series,21)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core04 delta_21d
def cg_f100_technology_f100_technology_multi_source_master_core04_delta_21d_2nd_v075_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(rnd,revenue.abs()+1e-9)
    base = _diff(series,21)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core05 delta_21d
def cg_f100_technology_f100_technology_multi_source_master_core05_delta_21d_2nd_v076_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _event_rate(action_count,252)+0.01*_z(volume,126)
    base = _diff(series,21)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core06 delta_21d
def cg_f100_technology_f100_technology_multi_source_master_core06_delta_21d_2nd_v077_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _event_rate(event_count,252)+0.01*_z(_pct_change(closeadj,21),126)
    base = _diff(series,21)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core07 delta_21d
def cg_f100_technology_f100_technology_multi_source_master_core07_delta_21d_2nd_v078_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(insider_net_value,marketcap.abs()+1e-9)
    base = _diff(series,21)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core08 delta_21d
def cg_f100_technology_f100_technology_multi_source_master_core08_delta_21d_2nd_v079_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(insider_buy_value-insider_sell_value,(insider_buy_value+insider_sell_value).abs()+1e-9) * _rank(volume,252)
    base = _diff(series,21)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core09 delta_21d
def cg_f100_technology_f100_technology_multi_source_master_core09_delta_21d_2nd_v080_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(inst_value,marketcap.abs()+1e-9)+inst_share
    base = _diff(series,21)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core00 pct_21d
def cg_f100_technology_f100_technology_multi_source_master_core00_pct_21d_2nd_v081_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(_pct_change(closeadj,252),_std(_pct_change(closeadj,1),63).abs()+1e-9)
    base = _pct_change(series,21)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core01 pct_21d
def cg_f100_technology_f100_technology_multi_source_master_core01_pct_21d_2nd_v082_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(_diff(revenue,252),revenue.abs()+1e-9)
    base = _pct_change(series,21)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core02 pct_21d
def cg_f100_technology_f100_technology_multi_source_master_core02_pct_21d_2nd_v083_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(fcf,revenue.abs()+1e-9)
    base = _pct_change(series,21)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core03 pct_21d
def cg_f100_technology_f100_technology_multi_source_master_core03_pct_21d_2nd_v084_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = roic+grossmargin
    base = _pct_change(series,21)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core04 pct_21d
def cg_f100_technology_f100_technology_multi_source_master_core04_pct_21d_2nd_v085_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(rnd,revenue.abs()+1e-9)
    base = _pct_change(series,21)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core05 pct_21d
def cg_f100_technology_f100_technology_multi_source_master_core05_pct_21d_2nd_v086_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _event_rate(action_count,252)+0.01*_z(volume,126)
    base = _pct_change(series,21)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core06 pct_21d
def cg_f100_technology_f100_technology_multi_source_master_core06_pct_21d_2nd_v087_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _event_rate(event_count,252)+0.01*_z(_pct_change(closeadj,21),126)
    base = _pct_change(series,21)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core07 pct_21d
def cg_f100_technology_f100_technology_multi_source_master_core07_pct_21d_2nd_v088_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(insider_net_value,marketcap.abs()+1e-9)
    base = _pct_change(series,21)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core08 pct_21d
def cg_f100_technology_f100_technology_multi_source_master_core08_pct_21d_2nd_v089_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(insider_buy_value-insider_sell_value,(insider_buy_value+insider_sell_value).abs()+1e-9) * _rank(volume,252)
    base = _pct_change(series,21)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core09 pct_21d
def cg_f100_technology_f100_technology_multi_source_master_core09_pct_21d_2nd_v090_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(inst_value,marketcap.abs()+1e-9)+inst_share
    base = _pct_change(series,21)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core00 ewm_21d
def cg_f100_technology_f100_technology_multi_source_master_core00_ewm_21d_2nd_v091_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(_pct_change(closeadj,252),_std(_pct_change(closeadj,1),63).abs()+1e-9)
    base = _ewm(series,21) + 0.01*_z(_pct_change(closeadj,21),126)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core01 ewm_21d
def cg_f100_technology_f100_technology_multi_source_master_core01_ewm_21d_2nd_v092_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(_diff(revenue,252),revenue.abs()+1e-9)
    base = _ewm(series,21) + 0.01*_z(_pct_change(closeadj,21),126)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core02 ewm_21d
def cg_f100_technology_f100_technology_multi_source_master_core02_ewm_21d_2nd_v093_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(fcf,revenue.abs()+1e-9)
    base = _ewm(series,21) + 0.01*_z(_pct_change(closeadj,21),126)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core03 ewm_21d
def cg_f100_technology_f100_technology_multi_source_master_core03_ewm_21d_2nd_v094_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = roic+grossmargin
    base = _ewm(series,21) + 0.01*_z(_pct_change(closeadj,21),126)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core04 ewm_21d
def cg_f100_technology_f100_technology_multi_source_master_core04_ewm_21d_2nd_v095_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(rnd,revenue.abs()+1e-9)
    base = _ewm(series,21) + 0.01*_z(_pct_change(closeadj,21),126)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core05 ewm_21d
def cg_f100_technology_f100_technology_multi_source_master_core05_ewm_21d_2nd_v096_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _event_rate(action_count,252)+0.01*_z(volume,126)
    base = _ewm(series,21) + 0.01*_z(_pct_change(closeadj,21),126)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core06 ewm_21d
def cg_f100_technology_f100_technology_multi_source_master_core06_ewm_21d_2nd_v097_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _event_rate(event_count,252)+0.01*_z(_pct_change(closeadj,21),126)
    base = _ewm(series,21) + 0.01*_z(_pct_change(closeadj,21),126)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core07 ewm_21d
def cg_f100_technology_f100_technology_multi_source_master_core07_ewm_21d_2nd_v098_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(insider_net_value,marketcap.abs()+1e-9)
    base = _ewm(series,21) + 0.01*_z(_pct_change(closeadj,21),126)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core08 ewm_21d
def cg_f100_technology_f100_technology_multi_source_master_core08_ewm_21d_2nd_v099_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(insider_buy_value-insider_sell_value,(insider_buy_value+insider_sell_value).abs()+1e-9) * _rank(volume,252)
    base = _ewm(series,21) + 0.01*_z(_pct_change(closeadj,21),126)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core09 ewm_21d
def cg_f100_technology_f100_technology_multi_source_master_core09_ewm_21d_2nd_v100_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(inst_value,marketcap.abs()+1e-9)+inst_share
    base = _ewm(series,21) + 0.01*_z(_pct_change(closeadj,21),126)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core00 slope_63d
def cg_f100_technology_f100_technology_multi_source_master_core00_slope_63d_2nd_v101_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(_pct_change(closeadj,252),_std(_pct_change(closeadj,1),63).abs()+1e-9)
    base = _slope(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core01 slope_63d
def cg_f100_technology_f100_technology_multi_source_master_core01_slope_63d_2nd_v102_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(_diff(revenue,252),revenue.abs()+1e-9)
    base = _slope(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core02 slope_63d
def cg_f100_technology_f100_technology_multi_source_master_core02_slope_63d_2nd_v103_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(fcf,revenue.abs()+1e-9)
    base = _slope(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core03 slope_63d
def cg_f100_technology_f100_technology_multi_source_master_core03_slope_63d_2nd_v104_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = roic+grossmargin
    base = _slope(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core04 slope_63d
def cg_f100_technology_f100_technology_multi_source_master_core04_slope_63d_2nd_v105_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(rnd,revenue.abs()+1e-9)
    base = _slope(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core05 slope_63d
def cg_f100_technology_f100_technology_multi_source_master_core05_slope_63d_2nd_v106_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _event_rate(action_count,252)+0.01*_z(volume,126)
    base = _slope(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core06 slope_63d
def cg_f100_technology_f100_technology_multi_source_master_core06_slope_63d_2nd_v107_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _event_rate(event_count,252)+0.01*_z(_pct_change(closeadj,21),126)
    base = _slope(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core07 slope_63d
def cg_f100_technology_f100_technology_multi_source_master_core07_slope_63d_2nd_v108_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(insider_net_value,marketcap.abs()+1e-9)
    base = _slope(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core08 slope_63d
def cg_f100_technology_f100_technology_multi_source_master_core08_slope_63d_2nd_v109_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(insider_buy_value-insider_sell_value,(insider_buy_value+insider_sell_value).abs()+1e-9) * _rank(volume,252)
    base = _slope(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core09 slope_63d
def cg_f100_technology_f100_technology_multi_source_master_core09_slope_63d_2nd_v110_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(inst_value,marketcap.abs()+1e-9)+inst_share
    base = _slope(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core00 pos_mag_63d
def cg_f100_technology_f100_technology_multi_source_master_core00_pos_mag_63d_2nd_v111_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(_pct_change(closeadj,252),_std(_pct_change(closeadj,1),63).abs()+1e-9)
    base = _corr(series, _pct_change(closeadj,21),126) + 0.01*_z(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core01 pos_mag_63d
def cg_f100_technology_f100_technology_multi_source_master_core01_pos_mag_63d_2nd_v112_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(_diff(revenue,252),revenue.abs()+1e-9)
    base = _corr(series, _pct_change(closeadj,21),126) + 0.01*_z(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core02 pos_mag_63d
def cg_f100_technology_f100_technology_multi_source_master_core02_pos_mag_63d_2nd_v113_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(fcf,revenue.abs()+1e-9)
    base = _corr(series, _pct_change(closeadj,21),126) + 0.01*_z(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core03 pos_mag_63d
def cg_f100_technology_f100_technology_multi_source_master_core03_pos_mag_63d_2nd_v114_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = roic+grossmargin
    base = _corr(series, _pct_change(closeadj,21),126) + 0.01*_z(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core04 pos_mag_63d
def cg_f100_technology_f100_technology_multi_source_master_core04_pos_mag_63d_2nd_v115_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(rnd,revenue.abs()+1e-9)
    base = _corr(series, _pct_change(closeadj,21),126) + 0.01*_z(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core05 pos_mag_63d
def cg_f100_technology_f100_technology_multi_source_master_core05_pos_mag_63d_2nd_v116_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _event_rate(action_count,252)+0.01*_z(volume,126)
    base = _corr(series, _pct_change(closeadj,21),126) + 0.01*_z(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core06 pos_mag_63d
def cg_f100_technology_f100_technology_multi_source_master_core06_pos_mag_63d_2nd_v117_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _event_rate(event_count,252)+0.01*_z(_pct_change(closeadj,21),126)
    base = _corr(series, _pct_change(closeadj,21),126) + 0.01*_z(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core07 pos_mag_63d
def cg_f100_technology_f100_technology_multi_source_master_core07_pos_mag_63d_2nd_v118_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(insider_net_value,marketcap.abs()+1e-9)
    base = _corr(series, _pct_change(closeadj,21),126) + 0.01*_z(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core08 pos_mag_63d
def cg_f100_technology_f100_technology_multi_source_master_core08_pos_mag_63d_2nd_v119_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(insider_buy_value-insider_sell_value,(insider_buy_value+insider_sell_value).abs()+1e-9) * _rank(volume,252)
    base = _corr(series, _pct_change(closeadj,21),126) + 0.01*_z(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core09 pos_mag_63d
def cg_f100_technology_f100_technology_multi_source_master_core09_pos_mag_63d_2nd_v120_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(inst_value,marketcap.abs()+1e-9)+inst_share
    base = _corr(series, _pct_change(closeadj,21),126) + 0.01*_z(series,63)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core00 neg_mag_63d
def cg_f100_technology_f100_technology_multi_source_master_core00_neg_mag_63d_2nd_v121_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(_pct_change(closeadj,252),_std(_pct_change(closeadj,1),63).abs()+1e-9)
    base = _corr(series, _pct_change(closeadj,63),126) - 0.01*_z(series,252)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core01 neg_mag_63d
def cg_f100_technology_f100_technology_multi_source_master_core01_neg_mag_63d_2nd_v122_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(_diff(revenue,252),revenue.abs()+1e-9)
    base = _corr(series, _pct_change(closeadj,63),126) - 0.01*_z(series,252)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core02 neg_mag_63d
def cg_f100_technology_f100_technology_multi_source_master_core02_neg_mag_63d_2nd_v123_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(fcf,revenue.abs()+1e-9)
    base = _corr(series, _pct_change(closeadj,63),126) - 0.01*_z(series,252)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core03 neg_mag_63d
def cg_f100_technology_f100_technology_multi_source_master_core03_neg_mag_63d_2nd_v124_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = roic+grossmargin
    base = _corr(series, _pct_change(closeadj,63),126) - 0.01*_z(series,252)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core04 neg_mag_63d
def cg_f100_technology_f100_technology_multi_source_master_core04_neg_mag_63d_2nd_v125_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(rnd,revenue.abs()+1e-9)
    base = _corr(series, _pct_change(closeadj,63),126) - 0.01*_z(series,252)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core05 neg_mag_63d
def cg_f100_technology_f100_technology_multi_source_master_core05_neg_mag_63d_2nd_v126_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _event_rate(action_count,252)+0.01*_z(volume,126)
    base = _corr(series, _pct_change(closeadj,63),126) - 0.01*_z(series,252)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core06 neg_mag_63d
def cg_f100_technology_f100_technology_multi_source_master_core06_neg_mag_63d_2nd_v127_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _event_rate(event_count,252)+0.01*_z(_pct_change(closeadj,21),126)
    base = _corr(series, _pct_change(closeadj,63),126) - 0.01*_z(series,252)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core07 neg_mag_63d
def cg_f100_technology_f100_technology_multi_source_master_core07_neg_mag_63d_2nd_v128_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(insider_net_value,marketcap.abs()+1e-9)
    base = _corr(series, _pct_change(closeadj,63),126) - 0.01*_z(series,252)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core08 neg_mag_63d
def cg_f100_technology_f100_technology_multi_source_master_core08_neg_mag_63d_2nd_v129_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(insider_buy_value-insider_sell_value,(insider_buy_value+insider_sell_value).abs()+1e-9) * _rank(volume,252)
    base = _corr(series, _pct_change(closeadj,63),126) - 0.01*_z(series,252)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core09 neg_mag_63d
def cg_f100_technology_f100_technology_multi_source_master_core09_neg_mag_63d_2nd_v130_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(inst_value,marketcap.abs()+1e-9)+inst_share
    base = _corr(series, _pct_change(closeadj,63),126) - 0.01*_z(series,252)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core00 recent_vs_long_21_126
def cg_f100_technology_f100_technology_multi_source_master_core00_recent_vs_long_21_126_2nd_v131_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(_pct_change(closeadj,252),_std(_pct_change(closeadj,1),63).abs()+1e-9)
    base = _safe_div(_mean(series,21), _mean(series,126).abs()+1e-9)-1.0
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core01 recent_vs_long_21_126
def cg_f100_technology_f100_technology_multi_source_master_core01_recent_vs_long_21_126_2nd_v132_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(_diff(revenue,252),revenue.abs()+1e-9)
    base = _safe_div(_mean(series,21), _mean(series,126).abs()+1e-9)-1.0
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core02 recent_vs_long_21_126
def cg_f100_technology_f100_technology_multi_source_master_core02_recent_vs_long_21_126_2nd_v133_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(fcf,revenue.abs()+1e-9)
    base = _safe_div(_mean(series,21), _mean(series,126).abs()+1e-9)-1.0
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core03 recent_vs_long_21_126
def cg_f100_technology_f100_technology_multi_source_master_core03_recent_vs_long_21_126_2nd_v134_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = roic+grossmargin
    base = _safe_div(_mean(series,21), _mean(series,126).abs()+1e-9)-1.0
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core04 recent_vs_long_21_126
def cg_f100_technology_f100_technology_multi_source_master_core04_recent_vs_long_21_126_2nd_v135_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(rnd,revenue.abs()+1e-9)
    base = _safe_div(_mean(series,21), _mean(series,126).abs()+1e-9)-1.0
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core05 recent_vs_long_21_126
def cg_f100_technology_f100_technology_multi_source_master_core05_recent_vs_long_21_126_2nd_v136_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _event_rate(action_count,252)+0.01*_z(volume,126)
    base = _safe_div(_mean(series,21), _mean(series,126).abs()+1e-9)-1.0
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core06 recent_vs_long_21_126
def cg_f100_technology_f100_technology_multi_source_master_core06_recent_vs_long_21_126_2nd_v137_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _event_rate(event_count,252)+0.01*_z(_pct_change(closeadj,21),126)
    base = _safe_div(_mean(series,21), _mean(series,126).abs()+1e-9)-1.0
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core07 recent_vs_long_21_126
def cg_f100_technology_f100_technology_multi_source_master_core07_recent_vs_long_21_126_2nd_v138_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(insider_net_value,marketcap.abs()+1e-9)
    base = _safe_div(_mean(series,21), _mean(series,126).abs()+1e-9)-1.0
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core08 recent_vs_long_21_126
def cg_f100_technology_f100_technology_multi_source_master_core08_recent_vs_long_21_126_2nd_v139_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(insider_buy_value-insider_sell_value,(insider_buy_value+insider_sell_value).abs()+1e-9) * _rank(volume,252)
    base = _safe_div(_mean(series,21), _mean(series,126).abs()+1e-9)-1.0
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core09 recent_vs_long_21_126
def cg_f100_technology_f100_technology_multi_source_master_core09_recent_vs_long_21_126_2nd_v140_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(inst_value,marketcap.abs()+1e-9)+inst_share
    base = _safe_div(_mean(series,21), _mean(series,126).abs()+1e-9)-1.0
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core00 centered_range_126d
def cg_f100_technology_f100_technology_multi_source_master_core00_centered_range_126d_2nd_v141_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(_pct_change(closeadj,252),_std(_pct_change(closeadj,1),63).abs()+1e-9)
    base = _safe_div(series-_mean(series,126), (_max(series,126)-_min(series,126)).abs()+1e-9)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core01 centered_range_126d
def cg_f100_technology_f100_technology_multi_source_master_core01_centered_range_126d_2nd_v142_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(_diff(revenue,252),revenue.abs()+1e-9)
    base = _safe_div(series-_mean(series,126), (_max(series,126)-_min(series,126)).abs()+1e-9)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core02 centered_range_126d
def cg_f100_technology_f100_technology_multi_source_master_core02_centered_range_126d_2nd_v143_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(fcf,revenue.abs()+1e-9)
    base = _safe_div(series-_mean(series,126), (_max(series,126)-_min(series,126)).abs()+1e-9)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core03 centered_range_126d
def cg_f100_technology_f100_technology_multi_source_master_core03_centered_range_126d_2nd_v144_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = roic+grossmargin
    base = _safe_div(series-_mean(series,126), (_max(series,126)-_min(series,126)).abs()+1e-9)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core04 centered_range_126d
def cg_f100_technology_f100_technology_multi_source_master_core04_centered_range_126d_2nd_v145_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(rnd,revenue.abs()+1e-9)
    base = _safe_div(series-_mean(series,126), (_max(series,126)-_min(series,126)).abs()+1e-9)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core05 centered_range_126d
def cg_f100_technology_f100_technology_multi_source_master_core05_centered_range_126d_2nd_v146_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _event_rate(action_count,252)+0.01*_z(volume,126)
    base = _safe_div(series-_mean(series,126), (_max(series,126)-_min(series,126)).abs()+1e-9)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core06 centered_range_126d
def cg_f100_technology_f100_technology_multi_source_master_core06_centered_range_126d_2nd_v147_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _event_rate(event_count,252)+0.01*_z(_pct_change(closeadj,21),126)
    base = _safe_div(series-_mean(series,126), (_max(series,126)-_min(series,126)).abs()+1e-9)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core07 centered_range_126d
def cg_f100_technology_f100_technology_multi_source_master_core07_centered_range_126d_2nd_v148_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(insider_net_value,marketcap.abs()+1e-9)
    base = _safe_div(series-_mean(series,126), (_max(series,126)-_min(series,126)).abs()+1e-9)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core08 centered_range_126d
def cg_f100_technology_f100_technology_multi_source_master_core08_centered_range_126d_2nd_v149_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(insider_buy_value-insider_sell_value,(insider_buy_value+insider_sell_value).abs()+1e-9) * _rank(volume,252)
    base = _safe_div(series-_mean(series,126), (_max(series,126)-_min(series,126)).abs()+1e-9)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

# core09 centered_range_126d
def cg_f100_technology_f100_technology_multi_source_master_core09_centered_range_126d_2nd_v150_signal(closeadj, volume, marketcap, revenue, fcf, roic, grossmargin, rnd, action_count, event_count, insider_net_value, insider_buy_value, insider_sell_value, inst_share, inst_value):
    series = _safe_div(inst_value,marketcap.abs()+1e-9)+inst_share
    base = _safe_div(series-_mean(series,126), (_max(series,126)-_min(series,126)).abs()+1e-9)
    result = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    return _clean(result)

