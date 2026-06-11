import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _align_quarterly_to_daily(x, close):
    """Forward-fill sparse Sharadar quarterly/event data to close.index."""
    return _s(x).reindex(_s(close).index).ffill()


def _safe_div(a, b):
    b = _s(b).replace(0, np.nan)
    if np.isscalar(a):
        return a / b
    return _s(a) / b


def _roc(x, periods=1):
    return _s(x).pct_change(periods)


def _z(x, window):
    x = _s(x)
    mean = x.rolling(window, min_periods=max(3, window // 4)).mean()
    std = x.rolling(window, min_periods=max(3, window // 4)).std().replace(0, np.nan)
    return (x - mean) / std


def _slope(x, window):
    x = _s(x)
    idx = np.arange(window, dtype=float)
    denom = ((idx - idx.mean()) ** 2).sum()
    def calc(v):
        return float(((v - np.nanmean(v)) * (idx - idx.mean())).sum() / denom)
    return x.rolling(window, min_periods=window).apply(calc, raw=True)



def vvh_151_vvh_001_pe_compression_z_21_roc_1(vvh_001_pe_compression_z_21):
    feature = _s(vvh_001_pe_compression_z_21)
    return (_roc(feature, 1)).reindex(feature.index)

def vvh_152_vvh_007_earnings_yield_spike_252_roc_42(vvh_007_earnings_yield_spike_252):
    feature = _s(vvh_007_earnings_yield_spike_252)
    return (_roc(feature, 42)).reindex(feature.index)

def vvh_153_vvh_013_ev_marketcap_gap_1512_roc_126(vvh_013_ev_marketcap_gap_1512):
    feature = _s(vvh_013_ev_marketcap_gap_1512)
    return (_roc(feature, 126)).reindex(feature.index)

def vvh_154_vvh_019_ps_compression_z_84_roc_378(vvh_019_ps_compression_z_84):
    feature = _s(vvh_019_ps_compression_z_84)
    return (_roc(feature, 378)).reindex(feature.index)

def vvh_155_vvh_025_pe_compression_z_756_roc_4(vvh_025_pe_compression_z_756):
    feature = _s(vvh_025_pe_compression_z_756)
    return (_roc(feature, 4)).reindex(feature.index)






















VALUATION_VS_HISTORY_REGISTRY_2ND_DERIVATIVES = {
    'vvh_151_vvh_001_pe_compression_z_21_roc_1': {'inputs': ['vvh_001_pe_compression_z_21'], 'func': vvh_151_vvh_001_pe_compression_z_21_roc_1},
    'vvh_152_vvh_007_earnings_yield_spike_252_roc_42': {'inputs': ['vvh_007_earnings_yield_spike_252'], 'func': vvh_152_vvh_007_earnings_yield_spike_252_roc_42},
    'vvh_153_vvh_013_ev_marketcap_gap_1512_roc_126': {'inputs': ['vvh_013_ev_marketcap_gap_1512'], 'func': vvh_153_vvh_013_ev_marketcap_gap_1512_roc_126},
    'vvh_154_vvh_019_ps_compression_z_84_roc_378': {'inputs': ['vvh_019_ps_compression_z_84'], 'func': vvh_154_vvh_019_ps_compression_z_84_roc_378},
    'vvh_155_vvh_025_pe_compression_z_756_roc_4': {'inputs': ['vvh_025_pe_compression_z_756'], 'func': vvh_155_vvh_025_pe_compression_z_756_roc_4},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def vvh_replacement_d2_001(vvh_025_pe_compression_z_756):
    feature = _clean(vvh_025_pe_compression_z_756)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_001'] = {'inputs': ['vvh_025_pe_compression_z_756'], 'func': vvh_replacement_d2_001}


def vvh_replacement_d2_002(vvh_replacement_001):
    feature = _clean(vvh_replacement_001)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_002'] = {'inputs': ['vvh_replacement_001'], 'func': vvh_replacement_d2_002}


def vvh_replacement_d2_003(vvh_replacement_002):
    feature = _clean(vvh_replacement_002)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_003'] = {'inputs': ['vvh_replacement_002'], 'func': vvh_replacement_d2_003}


def vvh_replacement_d2_004(vvh_replacement_003):
    feature = _clean(vvh_replacement_003)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_004'] = {'inputs': ['vvh_replacement_003'], 'func': vvh_replacement_d2_004}


def vvh_replacement_d2_005(vvh_replacement_004):
    feature = _clean(vvh_replacement_004)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_005'] = {'inputs': ['vvh_replacement_004'], 'func': vvh_replacement_d2_005}


def vvh_replacement_d2_006(vvh_replacement_005):
    feature = _clean(vvh_replacement_005)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_006'] = {'inputs': ['vvh_replacement_005'], 'func': vvh_replacement_d2_006}


def vvh_replacement_d2_007(vvh_replacement_006):
    feature = _clean(vvh_replacement_006)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_007'] = {'inputs': ['vvh_replacement_006'], 'func': vvh_replacement_d2_007}


def vvh_replacement_d2_008(vvh_replacement_007):
    feature = _clean(vvh_replacement_007)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_008'] = {'inputs': ['vvh_replacement_007'], 'func': vvh_replacement_d2_008}


def vvh_replacement_d2_009(vvh_replacement_008):
    feature = _clean(vvh_replacement_008)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_009'] = {'inputs': ['vvh_replacement_008'], 'func': vvh_replacement_d2_009}


def vvh_replacement_d2_010(vvh_replacement_009):
    feature = _clean(vvh_replacement_009)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_010'] = {'inputs': ['vvh_replacement_009'], 'func': vvh_replacement_d2_010}


def vvh_replacement_d2_011(vvh_replacement_010):
    feature = _clean(vvh_replacement_010)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_011'] = {'inputs': ['vvh_replacement_010'], 'func': vvh_replacement_d2_011}


def vvh_replacement_d2_012(vvh_replacement_011):
    feature = _clean(vvh_replacement_011)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_012'] = {'inputs': ['vvh_replacement_011'], 'func': vvh_replacement_d2_012}


def vvh_replacement_d2_013(vvh_replacement_012):
    feature = _clean(vvh_replacement_012)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_013'] = {'inputs': ['vvh_replacement_012'], 'func': vvh_replacement_d2_013}


def vvh_replacement_d2_014(vvh_replacement_013):
    feature = _clean(vvh_replacement_013)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_014'] = {'inputs': ['vvh_replacement_013'], 'func': vvh_replacement_d2_014}


def vvh_replacement_d2_015(vvh_replacement_014):
    feature = _clean(vvh_replacement_014)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_015'] = {'inputs': ['vvh_replacement_014'], 'func': vvh_replacement_d2_015}


def vvh_replacement_d2_016(vvh_replacement_015):
    feature = _clean(vvh_replacement_015)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_016'] = {'inputs': ['vvh_replacement_015'], 'func': vvh_replacement_d2_016}


def vvh_replacement_d2_017(vvh_replacement_016):
    feature = _clean(vvh_replacement_016)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_017'] = {'inputs': ['vvh_replacement_016'], 'func': vvh_replacement_d2_017}


def vvh_replacement_d2_018(vvh_replacement_017):
    feature = _clean(vvh_replacement_017)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_018'] = {'inputs': ['vvh_replacement_017'], 'func': vvh_replacement_d2_018}


def vvh_replacement_d2_019(vvh_replacement_018):
    feature = _clean(vvh_replacement_018)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_019'] = {'inputs': ['vvh_replacement_018'], 'func': vvh_replacement_d2_019}


def vvh_replacement_d2_020(vvh_replacement_019):
    feature = _clean(vvh_replacement_019)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_020'] = {'inputs': ['vvh_replacement_019'], 'func': vvh_replacement_d2_020}


def vvh_replacement_d2_021(vvh_replacement_020):
    feature = _clean(vvh_replacement_020)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_021'] = {'inputs': ['vvh_replacement_020'], 'func': vvh_replacement_d2_021}


def vvh_replacement_d2_022(vvh_replacement_021):
    feature = _clean(vvh_replacement_021)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_022'] = {'inputs': ['vvh_replacement_021'], 'func': vvh_replacement_d2_022}


def vvh_replacement_d2_023(vvh_replacement_022):
    feature = _clean(vvh_replacement_022)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_023'] = {'inputs': ['vvh_replacement_022'], 'func': vvh_replacement_d2_023}


def vvh_replacement_d2_024(vvh_replacement_023):
    feature = _clean(vvh_replacement_023)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_024'] = {'inputs': ['vvh_replacement_023'], 'func': vvh_replacement_d2_024}


def vvh_replacement_d2_025(vvh_replacement_024):
    feature = _clean(vvh_replacement_024)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_025'] = {'inputs': ['vvh_replacement_024'], 'func': vvh_replacement_d2_025}


def vvh_replacement_d2_026(vvh_replacement_025):
    feature = _clean(vvh_replacement_025)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_026'] = {'inputs': ['vvh_replacement_025'], 'func': vvh_replacement_d2_026}


def vvh_replacement_d2_027(vvh_replacement_026):
    feature = _clean(vvh_replacement_026)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_027'] = {'inputs': ['vvh_replacement_026'], 'func': vvh_replacement_d2_027}


def vvh_replacement_d2_028(vvh_replacement_027):
    feature = _clean(vvh_replacement_027)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_028'] = {'inputs': ['vvh_replacement_027'], 'func': vvh_replacement_d2_028}


def vvh_replacement_d2_029(vvh_replacement_028):
    feature = _clean(vvh_replacement_028)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_029'] = {'inputs': ['vvh_replacement_028'], 'func': vvh_replacement_d2_029}


def vvh_replacement_d2_030(vvh_replacement_029):
    feature = _clean(vvh_replacement_029)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_030'] = {'inputs': ['vvh_replacement_029'], 'func': vvh_replacement_d2_030}


def vvh_replacement_d2_031(vvh_replacement_030):
    feature = _clean(vvh_replacement_030)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_031'] = {'inputs': ['vvh_replacement_030'], 'func': vvh_replacement_d2_031}


def vvh_replacement_d2_032(vvh_replacement_031):
    feature = _clean(vvh_replacement_031)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_032'] = {'inputs': ['vvh_replacement_031'], 'func': vvh_replacement_d2_032}


def vvh_replacement_d2_033(vvh_replacement_032):
    feature = _clean(vvh_replacement_032)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_033'] = {'inputs': ['vvh_replacement_032'], 'func': vvh_replacement_d2_033}


def vvh_replacement_d2_034(vvh_replacement_033):
    feature = _clean(vvh_replacement_033)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_034'] = {'inputs': ['vvh_replacement_033'], 'func': vvh_replacement_d2_034}


def vvh_replacement_d2_035(vvh_replacement_034):
    feature = _clean(vvh_replacement_034)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_035'] = {'inputs': ['vvh_replacement_034'], 'func': vvh_replacement_d2_035}


def vvh_replacement_d2_036(vvh_replacement_035):
    feature = _clean(vvh_replacement_035)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_036'] = {'inputs': ['vvh_replacement_035'], 'func': vvh_replacement_d2_036}


def vvh_replacement_d2_037(vvh_replacement_036):
    feature = _clean(vvh_replacement_036)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_037'] = {'inputs': ['vvh_replacement_036'], 'func': vvh_replacement_d2_037}


def vvh_replacement_d2_038(vvh_replacement_037):
    feature = _clean(vvh_replacement_037)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_038'] = {'inputs': ['vvh_replacement_037'], 'func': vvh_replacement_d2_038}


def vvh_replacement_d2_039(vvh_replacement_038):
    feature = _clean(vvh_replacement_038)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_039'] = {'inputs': ['vvh_replacement_038'], 'func': vvh_replacement_d2_039}


def vvh_replacement_d2_040(vvh_replacement_039):
    feature = _clean(vvh_replacement_039)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_040'] = {'inputs': ['vvh_replacement_039'], 'func': vvh_replacement_d2_040}


def vvh_replacement_d2_041(vvh_replacement_040):
    feature = _clean(vvh_replacement_040)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_041'] = {'inputs': ['vvh_replacement_040'], 'func': vvh_replacement_d2_041}


def vvh_replacement_d2_042(vvh_replacement_041):
    feature = _clean(vvh_replacement_041)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_042'] = {'inputs': ['vvh_replacement_041'], 'func': vvh_replacement_d2_042}


def vvh_replacement_d2_043(vvh_replacement_042):
    feature = _clean(vvh_replacement_042)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_043'] = {'inputs': ['vvh_replacement_042'], 'func': vvh_replacement_d2_043}


def vvh_replacement_d2_044(vvh_replacement_043):
    feature = _clean(vvh_replacement_043)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_044'] = {'inputs': ['vvh_replacement_043'], 'func': vvh_replacement_d2_044}


def vvh_replacement_d2_045(vvh_replacement_044):
    feature = _clean(vvh_replacement_044)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_045'] = {'inputs': ['vvh_replacement_044'], 'func': vvh_replacement_d2_045}


def vvh_replacement_d2_046(vvh_replacement_045):
    feature = _clean(vvh_replacement_045)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_046'] = {'inputs': ['vvh_replacement_045'], 'func': vvh_replacement_d2_046}


def vvh_replacement_d2_047(vvh_replacement_046):
    feature = _clean(vvh_replacement_046)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_047'] = {'inputs': ['vvh_replacement_046'], 'func': vvh_replacement_d2_047}


def vvh_replacement_d2_048(vvh_replacement_047):
    feature = _clean(vvh_replacement_047)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_048'] = {'inputs': ['vvh_replacement_047'], 'func': vvh_replacement_d2_048}


def vvh_replacement_d2_049(vvh_replacement_048):
    feature = _clean(vvh_replacement_048)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_049'] = {'inputs': ['vvh_replacement_048'], 'func': vvh_replacement_d2_049}


def vvh_replacement_d2_050(vvh_replacement_049):
    feature = _clean(vvh_replacement_049)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_050'] = {'inputs': ['vvh_replacement_049'], 'func': vvh_replacement_d2_050}


def vvh_replacement_d2_051(vvh_replacement_050):
    feature = _clean(vvh_replacement_050)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_051'] = {'inputs': ['vvh_replacement_050'], 'func': vvh_replacement_d2_051}


def vvh_replacement_d2_052(vvh_replacement_051):
    feature = _clean(vvh_replacement_051)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_052'] = {'inputs': ['vvh_replacement_051'], 'func': vvh_replacement_d2_052}


def vvh_replacement_d2_053(vvh_replacement_052):
    feature = _clean(vvh_replacement_052)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_053'] = {'inputs': ['vvh_replacement_052'], 'func': vvh_replacement_d2_053}


def vvh_replacement_d2_054(vvh_replacement_053):
    feature = _clean(vvh_replacement_053)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_054'] = {'inputs': ['vvh_replacement_053'], 'func': vvh_replacement_d2_054}


def vvh_replacement_d2_055(vvh_replacement_054):
    feature = _clean(vvh_replacement_054)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_055'] = {'inputs': ['vvh_replacement_054'], 'func': vvh_replacement_d2_055}


def vvh_replacement_d2_056(vvh_replacement_055):
    feature = _clean(vvh_replacement_055)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_056'] = {'inputs': ['vvh_replacement_055'], 'func': vvh_replacement_d2_056}


def vvh_replacement_d2_057(vvh_replacement_056):
    feature = _clean(vvh_replacement_056)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_057'] = {'inputs': ['vvh_replacement_056'], 'func': vvh_replacement_d2_057}


def vvh_replacement_d2_058(vvh_replacement_057):
    feature = _clean(vvh_replacement_057)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_058'] = {'inputs': ['vvh_replacement_057'], 'func': vvh_replacement_d2_058}


def vvh_replacement_d2_059(vvh_replacement_058):
    feature = _clean(vvh_replacement_058)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_059'] = {'inputs': ['vvh_replacement_058'], 'func': vvh_replacement_d2_059}


def vvh_replacement_d2_060(vvh_replacement_059):
    feature = _clean(vvh_replacement_059)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_060'] = {'inputs': ['vvh_replacement_059'], 'func': vvh_replacement_d2_060}


def vvh_replacement_d2_061(vvh_replacement_060):
    feature = _clean(vvh_replacement_060)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_061'] = {'inputs': ['vvh_replacement_060'], 'func': vvh_replacement_d2_061}


def vvh_replacement_d2_062(vvh_replacement_061):
    feature = _clean(vvh_replacement_061)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_062'] = {'inputs': ['vvh_replacement_061'], 'func': vvh_replacement_d2_062}


def vvh_replacement_d2_063(vvh_replacement_062):
    feature = _clean(vvh_replacement_062)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_063'] = {'inputs': ['vvh_replacement_062'], 'func': vvh_replacement_d2_063}


def vvh_replacement_d2_064(vvh_replacement_063):
    feature = _clean(vvh_replacement_063)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_064'] = {'inputs': ['vvh_replacement_063'], 'func': vvh_replacement_d2_064}


def vvh_replacement_d2_065(vvh_replacement_064):
    feature = _clean(vvh_replacement_064)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_065'] = {'inputs': ['vvh_replacement_064'], 'func': vvh_replacement_d2_065}


def vvh_replacement_d2_066(vvh_replacement_065):
    feature = _clean(vvh_replacement_065)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_066'] = {'inputs': ['vvh_replacement_065'], 'func': vvh_replacement_d2_066}


def vvh_replacement_d2_067(vvh_replacement_066):
    feature = _clean(vvh_replacement_066)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_067'] = {'inputs': ['vvh_replacement_066'], 'func': vvh_replacement_d2_067}


def vvh_replacement_d2_068(vvh_replacement_067):
    feature = _clean(vvh_replacement_067)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_068'] = {'inputs': ['vvh_replacement_067'], 'func': vvh_replacement_d2_068}


def vvh_replacement_d2_069(vvh_replacement_068):
    feature = _clean(vvh_replacement_068)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_069'] = {'inputs': ['vvh_replacement_068'], 'func': vvh_replacement_d2_069}


def vvh_replacement_d2_070(vvh_replacement_069):
    feature = _clean(vvh_replacement_069)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_070'] = {'inputs': ['vvh_replacement_069'], 'func': vvh_replacement_d2_070}


def vvh_replacement_d2_071(vvh_replacement_070):
    feature = _clean(vvh_replacement_070)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_071'] = {'inputs': ['vvh_replacement_070'], 'func': vvh_replacement_d2_071}


def vvh_replacement_d2_072(vvh_replacement_071):
    feature = _clean(vvh_replacement_071)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_072'] = {'inputs': ['vvh_replacement_071'], 'func': vvh_replacement_d2_072}


def vvh_replacement_d2_073(vvh_replacement_072):
    feature = _clean(vvh_replacement_072)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_073'] = {'inputs': ['vvh_replacement_072'], 'func': vvh_replacement_d2_073}


def vvh_replacement_d2_074(vvh_replacement_073):
    feature = _clean(vvh_replacement_073)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_074'] = {'inputs': ['vvh_replacement_073'], 'func': vvh_replacement_d2_074}


def vvh_replacement_d2_075(vvh_replacement_074):
    feature = _clean(vvh_replacement_074)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_075'] = {'inputs': ['vvh_replacement_074'], 'func': vvh_replacement_d2_075}


def vvh_replacement_d2_076(vvh_replacement_075):
    feature = _clean(vvh_replacement_075)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_076'] = {'inputs': ['vvh_replacement_075'], 'func': vvh_replacement_d2_076}


def vvh_replacement_d2_077(vvh_replacement_076):
    feature = _clean(vvh_replacement_076)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_077'] = {'inputs': ['vvh_replacement_076'], 'func': vvh_replacement_d2_077}


def vvh_replacement_d2_078(vvh_replacement_077):
    feature = _clean(vvh_replacement_077)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_078'] = {'inputs': ['vvh_replacement_077'], 'func': vvh_replacement_d2_078}


def vvh_replacement_d2_079(vvh_replacement_078):
    feature = _clean(vvh_replacement_078)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_079'] = {'inputs': ['vvh_replacement_078'], 'func': vvh_replacement_d2_079}


def vvh_replacement_d2_080(vvh_replacement_079):
    feature = _clean(vvh_replacement_079)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_080'] = {'inputs': ['vvh_replacement_079'], 'func': vvh_replacement_d2_080}


def vvh_replacement_d2_081(vvh_replacement_080):
    feature = _clean(vvh_replacement_080)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_081'] = {'inputs': ['vvh_replacement_080'], 'func': vvh_replacement_d2_081}


def vvh_replacement_d2_082(vvh_replacement_081):
    feature = _clean(vvh_replacement_081)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_082'] = {'inputs': ['vvh_replacement_081'], 'func': vvh_replacement_d2_082}


def vvh_replacement_d2_083(vvh_replacement_082):
    feature = _clean(vvh_replacement_082)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_083'] = {'inputs': ['vvh_replacement_082'], 'func': vvh_replacement_d2_083}


def vvh_replacement_d2_084(vvh_replacement_083):
    feature = _clean(vvh_replacement_083)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_084'] = {'inputs': ['vvh_replacement_083'], 'func': vvh_replacement_d2_084}


def vvh_replacement_d2_085(vvh_replacement_084):
    feature = _clean(vvh_replacement_084)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_085'] = {'inputs': ['vvh_replacement_084'], 'func': vvh_replacement_d2_085}


def vvh_replacement_d2_086(vvh_replacement_085):
    feature = _clean(vvh_replacement_085)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_086'] = {'inputs': ['vvh_replacement_085'], 'func': vvh_replacement_d2_086}


def vvh_replacement_d2_087(vvh_replacement_086):
    feature = _clean(vvh_replacement_086)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_087'] = {'inputs': ['vvh_replacement_086'], 'func': vvh_replacement_d2_087}


def vvh_replacement_d2_088(vvh_replacement_087):
    feature = _clean(vvh_replacement_087)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_088'] = {'inputs': ['vvh_replacement_087'], 'func': vvh_replacement_d2_088}


def vvh_replacement_d2_089(vvh_replacement_088):
    feature = _clean(vvh_replacement_088)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_089'] = {'inputs': ['vvh_replacement_088'], 'func': vvh_replacement_d2_089}


def vvh_replacement_d2_090(vvh_replacement_089):
    feature = _clean(vvh_replacement_089)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_090'] = {'inputs': ['vvh_replacement_089'], 'func': vvh_replacement_d2_090}


def vvh_replacement_d2_091(vvh_replacement_090):
    feature = _clean(vvh_replacement_090)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_091'] = {'inputs': ['vvh_replacement_090'], 'func': vvh_replacement_d2_091}


def vvh_replacement_d2_092(vvh_replacement_091):
    feature = _clean(vvh_replacement_091)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_092'] = {'inputs': ['vvh_replacement_091'], 'func': vvh_replacement_d2_092}


def vvh_replacement_d2_093(vvh_replacement_092):
    feature = _clean(vvh_replacement_092)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_093'] = {'inputs': ['vvh_replacement_092'], 'func': vvh_replacement_d2_093}


def vvh_replacement_d2_094(vvh_replacement_093):
    feature = _clean(vvh_replacement_093)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_094'] = {'inputs': ['vvh_replacement_093'], 'func': vvh_replacement_d2_094}


def vvh_replacement_d2_095(vvh_replacement_094):
    feature = _clean(vvh_replacement_094)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_095'] = {'inputs': ['vvh_replacement_094'], 'func': vvh_replacement_d2_095}


def vvh_replacement_d2_096(vvh_replacement_095):
    feature = _clean(vvh_replacement_095)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_096'] = {'inputs': ['vvh_replacement_095'], 'func': vvh_replacement_d2_096}


def vvh_replacement_d2_097(vvh_replacement_096):
    feature = _clean(vvh_replacement_096)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_097'] = {'inputs': ['vvh_replacement_096'], 'func': vvh_replacement_d2_097}


def vvh_replacement_d2_098(vvh_replacement_097):
    feature = _clean(vvh_replacement_097)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_098'] = {'inputs': ['vvh_replacement_097'], 'func': vvh_replacement_d2_098}


def vvh_replacement_d2_099(vvh_replacement_098):
    feature = _clean(vvh_replacement_098)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_099'] = {'inputs': ['vvh_replacement_098'], 'func': vvh_replacement_d2_099}


def vvh_replacement_d2_100(vvh_replacement_099):
    feature = _clean(vvh_replacement_099)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_100'] = {'inputs': ['vvh_replacement_099'], 'func': vvh_replacement_d2_100}


def vvh_replacement_d2_101(vvh_replacement_100):
    feature = _clean(vvh_replacement_100)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_101'] = {'inputs': ['vvh_replacement_100'], 'func': vvh_replacement_d2_101}


def vvh_replacement_d2_102(vvh_replacement_101):
    feature = _clean(vvh_replacement_101)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_102'] = {'inputs': ['vvh_replacement_101'], 'func': vvh_replacement_d2_102}


def vvh_replacement_d2_103(vvh_replacement_102):
    feature = _clean(vvh_replacement_102)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_103'] = {'inputs': ['vvh_replacement_102'], 'func': vvh_replacement_d2_103}


def vvh_replacement_d2_104(vvh_replacement_103):
    feature = _clean(vvh_replacement_103)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_104'] = {'inputs': ['vvh_replacement_103'], 'func': vvh_replacement_d2_104}


def vvh_replacement_d2_105(vvh_replacement_104):
    feature = _clean(vvh_replacement_104)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_105'] = {'inputs': ['vvh_replacement_104'], 'func': vvh_replacement_d2_105}


def vvh_replacement_d2_106(vvh_replacement_105):
    feature = _clean(vvh_replacement_105)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_106'] = {'inputs': ['vvh_replacement_105'], 'func': vvh_replacement_d2_106}


def vvh_replacement_d2_107(vvh_replacement_106):
    feature = _clean(vvh_replacement_106)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_107'] = {'inputs': ['vvh_replacement_106'], 'func': vvh_replacement_d2_107}


def vvh_replacement_d2_108(vvh_replacement_107):
    feature = _clean(vvh_replacement_107)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_108'] = {'inputs': ['vvh_replacement_107'], 'func': vvh_replacement_d2_108}


def vvh_replacement_d2_109(vvh_replacement_108):
    feature = _clean(vvh_replacement_108)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_109'] = {'inputs': ['vvh_replacement_108'], 'func': vvh_replacement_d2_109}


def vvh_replacement_d2_110(vvh_replacement_109):
    feature = _clean(vvh_replacement_109)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_110'] = {'inputs': ['vvh_replacement_109'], 'func': vvh_replacement_d2_110}


def vvh_replacement_d2_111(vvh_replacement_110):
    feature = _clean(vvh_replacement_110)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_111'] = {'inputs': ['vvh_replacement_110'], 'func': vvh_replacement_d2_111}


def vvh_replacement_d2_112(vvh_replacement_111):
    feature = _clean(vvh_replacement_111)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_112'] = {'inputs': ['vvh_replacement_111'], 'func': vvh_replacement_d2_112}


def vvh_replacement_d2_113(vvh_replacement_112):
    feature = _clean(vvh_replacement_112)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_113'] = {'inputs': ['vvh_replacement_112'], 'func': vvh_replacement_d2_113}


def vvh_replacement_d2_114(vvh_replacement_113):
    feature = _clean(vvh_replacement_113)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_114'] = {'inputs': ['vvh_replacement_113'], 'func': vvh_replacement_d2_114}


def vvh_replacement_d2_115(vvh_replacement_114):
    feature = _clean(vvh_replacement_114)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_115'] = {'inputs': ['vvh_replacement_114'], 'func': vvh_replacement_d2_115}


def vvh_replacement_d2_116(vvh_replacement_115):
    feature = _clean(vvh_replacement_115)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_116'] = {'inputs': ['vvh_replacement_115'], 'func': vvh_replacement_d2_116}


def vvh_replacement_d2_117(vvh_replacement_116):
    feature = _clean(vvh_replacement_116)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_117'] = {'inputs': ['vvh_replacement_116'], 'func': vvh_replacement_d2_117}


def vvh_replacement_d2_118(vvh_replacement_117):
    feature = _clean(vvh_replacement_117)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_118'] = {'inputs': ['vvh_replacement_117'], 'func': vvh_replacement_d2_118}


def vvh_replacement_d2_119(vvh_replacement_118):
    feature = _clean(vvh_replacement_118)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_119'] = {'inputs': ['vvh_replacement_118'], 'func': vvh_replacement_d2_119}


def vvh_replacement_d2_120(vvh_replacement_119):
    feature = _clean(vvh_replacement_119)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_120'] = {'inputs': ['vvh_replacement_119'], 'func': vvh_replacement_d2_120}


def vvh_replacement_d2_121(vvh_replacement_120):
    feature = _clean(vvh_replacement_120)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_121'] = {'inputs': ['vvh_replacement_120'], 'func': vvh_replacement_d2_121}


def vvh_replacement_d2_122(vvh_replacement_121):
    feature = _clean(vvh_replacement_121)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_122'] = {'inputs': ['vvh_replacement_121'], 'func': vvh_replacement_d2_122}


def vvh_replacement_d2_123(vvh_replacement_122):
    feature = _clean(vvh_replacement_122)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_123'] = {'inputs': ['vvh_replacement_122'], 'func': vvh_replacement_d2_123}


def vvh_replacement_d2_124(vvh_replacement_123):
    feature = _clean(vvh_replacement_123)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_124'] = {'inputs': ['vvh_replacement_123'], 'func': vvh_replacement_d2_124}


def vvh_replacement_d2_125(vvh_replacement_124):
    feature = _clean(vvh_replacement_124)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_125'] = {'inputs': ['vvh_replacement_124'], 'func': vvh_replacement_d2_125}


def vvh_replacement_d2_126(vvh_replacement_125):
    feature = _clean(vvh_replacement_125)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_126'] = {'inputs': ['vvh_replacement_125'], 'func': vvh_replacement_d2_126}


def vvh_replacement_d2_127(vvh_replacement_126):
    feature = _clean(vvh_replacement_126)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_127'] = {'inputs': ['vvh_replacement_126'], 'func': vvh_replacement_d2_127}


def vvh_replacement_d2_128(vvh_replacement_127):
    feature = _clean(vvh_replacement_127)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_128'] = {'inputs': ['vvh_replacement_127'], 'func': vvh_replacement_d2_128}


def vvh_replacement_d2_129(vvh_replacement_128):
    feature = _clean(vvh_replacement_128)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_129'] = {'inputs': ['vvh_replacement_128'], 'func': vvh_replacement_d2_129}


def vvh_replacement_d2_130(vvh_replacement_129):
    feature = _clean(vvh_replacement_129)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_130'] = {'inputs': ['vvh_replacement_129'], 'func': vvh_replacement_d2_130}


def vvh_replacement_d2_131(vvh_replacement_130):
    feature = _clean(vvh_replacement_130)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_131'] = {'inputs': ['vvh_replacement_130'], 'func': vvh_replacement_d2_131}


def vvh_replacement_d2_132(vvh_replacement_131):
    feature = _clean(vvh_replacement_131)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_132'] = {'inputs': ['vvh_replacement_131'], 'func': vvh_replacement_d2_132}


def vvh_replacement_d2_133(vvh_replacement_132):
    feature = _clean(vvh_replacement_132)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_133'] = {'inputs': ['vvh_replacement_132'], 'func': vvh_replacement_d2_133}


def vvh_replacement_d2_134(vvh_replacement_133):
    feature = _clean(vvh_replacement_133)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_134'] = {'inputs': ['vvh_replacement_133'], 'func': vvh_replacement_d2_134}


def vvh_replacement_d2_135(vvh_replacement_134):
    feature = _clean(vvh_replacement_134)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_135'] = {'inputs': ['vvh_replacement_134'], 'func': vvh_replacement_d2_135}


def vvh_replacement_d2_136(vvh_replacement_135):
    feature = _clean(vvh_replacement_135)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_136'] = {'inputs': ['vvh_replacement_135'], 'func': vvh_replacement_d2_136}


def vvh_replacement_d2_137(vvh_replacement_136):
    feature = _clean(vvh_replacement_136)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_137'] = {'inputs': ['vvh_replacement_136'], 'func': vvh_replacement_d2_137}


def vvh_replacement_d2_138(vvh_replacement_137):
    feature = _clean(vvh_replacement_137)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
VVH_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvh_replacement_d2_138'] = {'inputs': ['vvh_replacement_137'], 'func': vvh_replacement_d2_138}


# Base-universe derivative extensions for repaired first-base features.
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def vvh_base_universe_d2_001_vvh_002_pb_compression_z_42(vvh_002_pb_compression_z_42):
    return _base_universe_d2(vvh_002_pb_compression_z_42, 1)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_001_vvh_002_pb_compression_z_42'] = {'inputs': ['vvh_002_pb_compression_z_42'], 'func': vvh_base_universe_d2_001_vvh_002_pb_compression_z_42}


def vvh_base_universe_d2_002_vvh_003_ps_compression_z_63(vvh_003_ps_compression_z_63):
    return _base_universe_d2(vvh_003_ps_compression_z_63, 2)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_002_vvh_003_ps_compression_z_63'] = {'inputs': ['vvh_003_ps_compression_z_63'], 'func': vvh_base_universe_d2_002_vvh_003_ps_compression_z_63}


def vvh_base_universe_d2_003_vvh_005_ev_marketcap_gap_126(vvh_005_ev_marketcap_gap_126):
    return _base_universe_d2(vvh_005_ev_marketcap_gap_126, 3)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_003_vvh_005_ev_marketcap_gap_126'] = {'inputs': ['vvh_005_ev_marketcap_gap_126'], 'func': vvh_base_universe_d2_003_vvh_005_ev_marketcap_gap_126}


def vvh_base_universe_d2_004_vvh_006_dividend_yield_spike_189(vvh_006_dividend_yield_spike_189):
    return _base_universe_d2(vvh_006_dividend_yield_spike_189, 4)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_004_vvh_006_dividend_yield_spike_189'] = {'inputs': ['vvh_006_dividend_yield_spike_189'], 'func': vvh_base_universe_d2_004_vvh_006_dividend_yield_spike_189}


def vvh_base_universe_d2_005_vvh_008_valuation_history_depth_378(vvh_008_valuation_history_depth_378):
    return _base_universe_d2(vvh_008_valuation_history_depth_378, 5)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_005_vvh_008_valuation_history_depth_378'] = {'inputs': ['vvh_008_valuation_history_depth_378'], 'func': vvh_base_universe_d2_005_vvh_008_valuation_history_depth_378}


def vvh_base_universe_d2_006_vvh_009_pe_compression_z_504(vvh_009_pe_compression_z_504):
    return _base_universe_d2(vvh_009_pe_compression_z_504, 6)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_006_vvh_009_pe_compression_z_504'] = {'inputs': ['vvh_009_pe_compression_z_504'], 'func': vvh_base_universe_d2_006_vvh_009_pe_compression_z_504}


def vvh_base_universe_d2_007_vvh_010_pb_compression_z_756(vvh_010_pb_compression_z_756):
    return _base_universe_d2(vvh_010_pb_compression_z_756, 7)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_007_vvh_010_pb_compression_z_756'] = {'inputs': ['vvh_010_pb_compression_z_756'], 'func': vvh_base_universe_d2_007_vvh_010_pb_compression_z_756}


def vvh_base_universe_d2_008_vvh_011_ps_compression_z_1008(vvh_011_ps_compression_z_1008):
    return _base_universe_d2(vvh_011_ps_compression_z_1008, 8)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_008_vvh_011_ps_compression_z_1008'] = {'inputs': ['vvh_011_ps_compression_z_1008'], 'func': vvh_base_universe_d2_008_vvh_011_ps_compression_z_1008}


def vvh_base_universe_d2_009_vvh_014_dividend_yield_spike_63(vvh_014_dividend_yield_spike_63):
    return _base_universe_d2(vvh_014_dividend_yield_spike_63, 9)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_009_vvh_014_dividend_yield_spike_63'] = {'inputs': ['vvh_014_dividend_yield_spike_63'], 'func': vvh_base_universe_d2_009_vvh_014_dividend_yield_spike_63}


def vvh_base_universe_d2_010_vvh_016_valuation_history_depth_21(vvh_016_valuation_history_depth_21):
    return _base_universe_d2(vvh_016_valuation_history_depth_21, 10)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_010_vvh_016_valuation_history_depth_21'] = {'inputs': ['vvh_016_valuation_history_depth_21'], 'func': vvh_base_universe_d2_010_vvh_016_valuation_history_depth_21}


def vvh_base_universe_d2_011_vvh_021_ev_marketcap_gap_189(vvh_021_ev_marketcap_gap_189):
    return _base_universe_d2(vvh_021_ev_marketcap_gap_189, 11)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_011_vvh_021_ev_marketcap_gap_189'] = {'inputs': ['vvh_021_ev_marketcap_gap_189'], 'func': vvh_base_universe_d2_011_vvh_021_ev_marketcap_gap_189}


def vvh_base_universe_d2_012_vvh_023_earnings_yield_spike_378(vvh_023_earnings_yield_spike_378):
    return _base_universe_d2(vvh_023_earnings_yield_spike_378, 12)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_012_vvh_023_earnings_yield_spike_378'] = {'inputs': ['vvh_023_earnings_yield_spike_378'], 'func': vvh_base_universe_d2_012_vvh_023_earnings_yield_spike_378}


def vvh_base_universe_d2_013_vvh_024_valuation_history_depth_504(vvh_024_valuation_history_depth_504):
    return _base_universe_d2(vvh_024_valuation_history_depth_504, 13)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_013_vvh_024_valuation_history_depth_504'] = {'inputs': ['vvh_024_valuation_history_depth_504'], 'func': vvh_base_universe_d2_013_vvh_024_valuation_history_depth_504}


def vvh_base_universe_d2_014_vvh_027_ps_compression_z_1260(vvh_027_ps_compression_z_1260):
    return _base_universe_d2(vvh_027_ps_compression_z_1260, 14)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_014_vvh_027_ps_compression_z_1260'] = {'inputs': ['vvh_027_ps_compression_z_1260'], 'func': vvh_base_universe_d2_014_vvh_027_ps_compression_z_1260}


def vvh_base_universe_d2_015_vvh_029_ev_marketcap_gap_63(vvh_029_ev_marketcap_gap_63):
    return _base_universe_d2(vvh_029_ev_marketcap_gap_63, 15)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_015_vvh_029_ev_marketcap_gap_63'] = {'inputs': ['vvh_029_ev_marketcap_gap_63'], 'func': vvh_base_universe_d2_015_vvh_029_ev_marketcap_gap_63}


def vvh_base_universe_d2_016_vvh_031_earnings_yield_spike_21(vvh_031_earnings_yield_spike_21):
    return _base_universe_d2(vvh_031_earnings_yield_spike_21, 16)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_016_vvh_031_earnings_yield_spike_21'] = {'inputs': ['vvh_031_earnings_yield_spike_21'], 'func': vvh_base_universe_d2_016_vvh_031_earnings_yield_spike_21}


def vvh_base_universe_d2_017_vvh_032_valuation_history_depth_42(vvh_032_valuation_history_depth_42):
    return _base_universe_d2(vvh_032_valuation_history_depth_42, 17)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_017_vvh_032_valuation_history_depth_42'] = {'inputs': ['vvh_032_valuation_history_depth_42'], 'func': vvh_base_universe_d2_017_vvh_032_valuation_history_depth_42}


def vvh_base_universe_d2_018_vvh_035_ps_compression_z_126(vvh_035_ps_compression_z_126):
    return _base_universe_d2(vvh_035_ps_compression_z_126, 18)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_018_vvh_035_ps_compression_z_126'] = {'inputs': ['vvh_035_ps_compression_z_126'], 'func': vvh_base_universe_d2_018_vvh_035_ps_compression_z_126}


def vvh_base_universe_d2_019_vvh_037_ev_marketcap_gap_252(vvh_037_ev_marketcap_gap_252):
    return _base_universe_d2(vvh_037_ev_marketcap_gap_252, 19)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_019_vvh_037_ev_marketcap_gap_252'] = {'inputs': ['vvh_037_ev_marketcap_gap_252'], 'func': vvh_base_universe_d2_019_vvh_037_ev_marketcap_gap_252}


def vvh_base_universe_d2_020_vvh_039_earnings_yield_spike_504(vvh_039_earnings_yield_spike_504):
    return _base_universe_d2(vvh_039_earnings_yield_spike_504, 20)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_020_vvh_039_earnings_yield_spike_504'] = {'inputs': ['vvh_039_earnings_yield_spike_504'], 'func': vvh_base_universe_d2_020_vvh_039_earnings_yield_spike_504}


def vvh_base_universe_d2_021_vvh_040_valuation_history_depth_756(vvh_040_valuation_history_depth_756):
    return _base_universe_d2(vvh_040_valuation_history_depth_756, 21)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_021_vvh_040_valuation_history_depth_756'] = {'inputs': ['vvh_040_valuation_history_depth_756'], 'func': vvh_base_universe_d2_021_vvh_040_valuation_history_depth_756}


def vvh_base_universe_d2_022_vvh_043_ps_compression_z_1512(vvh_043_ps_compression_z_1512):
    return _base_universe_d2(vvh_043_ps_compression_z_1512, 22)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_022_vvh_043_ps_compression_z_1512'] = {'inputs': ['vvh_043_ps_compression_z_1512'], 'func': vvh_base_universe_d2_022_vvh_043_ps_compression_z_1512}


def vvh_base_universe_d2_023_vvh_047_earnings_yield_spike_42(vvh_047_earnings_yield_spike_42):
    return _base_universe_d2(vvh_047_earnings_yield_spike_42, 23)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_023_vvh_047_earnings_yield_spike_42'] = {'inputs': ['vvh_047_earnings_yield_spike_42'], 'func': vvh_base_universe_d2_023_vvh_047_earnings_yield_spike_42}


def vvh_base_universe_d2_024_vvh_048_valuation_history_depth_63(vvh_048_valuation_history_depth_63):
    return _base_universe_d2(vvh_048_valuation_history_depth_63, 24)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_024_vvh_048_valuation_history_depth_63'] = {'inputs': ['vvh_048_valuation_history_depth_63'], 'func': vvh_base_universe_d2_024_vvh_048_valuation_history_depth_63}


def vvh_base_universe_d2_025_vvh_051_ps_compression_z_189(vvh_051_ps_compression_z_189):
    return _base_universe_d2(vvh_051_ps_compression_z_189, 25)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_025_vvh_051_ps_compression_z_189'] = {'inputs': ['vvh_051_ps_compression_z_189'], 'func': vvh_base_universe_d2_025_vvh_051_ps_compression_z_189}


def vvh_base_universe_d2_026_vvh_053_ev_marketcap_gap_378(vvh_053_ev_marketcap_gap_378):
    return _base_universe_d2(vvh_053_ev_marketcap_gap_378, 26)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_026_vvh_053_ev_marketcap_gap_378'] = {'inputs': ['vvh_053_ev_marketcap_gap_378'], 'func': vvh_base_universe_d2_026_vvh_053_ev_marketcap_gap_378}


def vvh_base_universe_d2_027_vvh_055_earnings_yield_spike_756(vvh_055_earnings_yield_spike_756):
    return _base_universe_d2(vvh_055_earnings_yield_spike_756, 27)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_027_vvh_055_earnings_yield_spike_756'] = {'inputs': ['vvh_055_earnings_yield_spike_756'], 'func': vvh_base_universe_d2_027_vvh_055_earnings_yield_spike_756}


def vvh_base_universe_d2_028_vvh_056_valuation_history_depth_1008(vvh_056_valuation_history_depth_1008):
    return _base_universe_d2(vvh_056_valuation_history_depth_1008, 28)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_028_vvh_056_valuation_history_depth_1008'] = {'inputs': ['vvh_056_valuation_history_depth_1008'], 'func': vvh_base_universe_d2_028_vvh_056_valuation_history_depth_1008}


def vvh_base_universe_d2_029_vvh_061_ev_marketcap_gap_21(vvh_061_ev_marketcap_gap_21):
    return _base_universe_d2(vvh_061_ev_marketcap_gap_21, 29)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_029_vvh_061_ev_marketcap_gap_21'] = {'inputs': ['vvh_061_ev_marketcap_gap_21'], 'func': vvh_base_universe_d2_029_vvh_061_ev_marketcap_gap_21}


def vvh_base_universe_d2_030_vvh_064_valuation_history_depth_84(vvh_064_valuation_history_depth_84):
    return _base_universe_d2(vvh_064_valuation_history_depth_84, 30)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_030_vvh_064_valuation_history_depth_84'] = {'inputs': ['vvh_064_valuation_history_depth_84'], 'func': vvh_base_universe_d2_030_vvh_064_valuation_history_depth_84}


def vvh_base_universe_d2_031_vvh_067_ps_compression_z_252(vvh_067_ps_compression_z_252):
    return _base_universe_d2(vvh_067_ps_compression_z_252, 31)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_031_vvh_067_ps_compression_z_252'] = {'inputs': ['vvh_067_ps_compression_z_252'], 'func': vvh_base_universe_d2_031_vvh_067_ps_compression_z_252}


def vvh_base_universe_d2_032_vvh_069_ev_marketcap_gap_504(vvh_069_ev_marketcap_gap_504):
    return _base_universe_d2(vvh_069_ev_marketcap_gap_504, 32)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_032_vvh_069_ev_marketcap_gap_504'] = {'inputs': ['vvh_069_ev_marketcap_gap_504'], 'func': vvh_base_universe_d2_032_vvh_069_ev_marketcap_gap_504}


def vvh_base_universe_d2_033_vvh_071_earnings_yield_spike_1008(vvh_071_earnings_yield_spike_1008):
    return _base_universe_d2(vvh_071_earnings_yield_spike_1008, 33)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_033_vvh_071_earnings_yield_spike_1008'] = {'inputs': ['vvh_071_earnings_yield_spike_1008'], 'func': vvh_base_universe_d2_033_vvh_071_earnings_yield_spike_1008}


def vvh_base_universe_d2_034_vvh_072_valuation_history_depth_1260(vvh_072_valuation_history_depth_1260):
    return _base_universe_d2(vvh_072_valuation_history_depth_1260, 34)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_034_vvh_072_valuation_history_depth_1260'] = {'inputs': ['vvh_072_valuation_history_depth_1260'], 'func': vvh_base_universe_d2_034_vvh_072_valuation_history_depth_1260}


def vvh_base_universe_d2_035_vvh_basefill_004(vvh_basefill_004):
    return _base_universe_d2(vvh_basefill_004, 35)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_035_vvh_basefill_004'] = {'inputs': ['vvh_basefill_004'], 'func': vvh_base_universe_d2_035_vvh_basefill_004}


def vvh_base_universe_d2_036_vvh_basefill_012(vvh_basefill_012):
    return _base_universe_d2(vvh_basefill_012, 36)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_036_vvh_basefill_012'] = {'inputs': ['vvh_basefill_012'], 'func': vvh_base_universe_d2_036_vvh_basefill_012}


def vvh_base_universe_d2_037_vvh_basefill_015(vvh_basefill_015):
    return _base_universe_d2(vvh_basefill_015, 37)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_037_vvh_basefill_015'] = {'inputs': ['vvh_basefill_015'], 'func': vvh_base_universe_d2_037_vvh_basefill_015}


def vvh_base_universe_d2_038_vvh_basefill_017(vvh_basefill_017):
    return _base_universe_d2(vvh_basefill_017, 38)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_038_vvh_basefill_017'] = {'inputs': ['vvh_basefill_017'], 'func': vvh_base_universe_d2_038_vvh_basefill_017}


def vvh_base_universe_d2_039_vvh_basefill_018(vvh_basefill_018):
    return _base_universe_d2(vvh_basefill_018, 39)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_039_vvh_basefill_018'] = {'inputs': ['vvh_basefill_018'], 'func': vvh_base_universe_d2_039_vvh_basefill_018}


def vvh_base_universe_d2_040_vvh_basefill_020(vvh_basefill_020):
    return _base_universe_d2(vvh_basefill_020, 40)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_040_vvh_basefill_020'] = {'inputs': ['vvh_basefill_020'], 'func': vvh_base_universe_d2_040_vvh_basefill_020}


def vvh_base_universe_d2_041_vvh_basefill_022(vvh_basefill_022):
    return _base_universe_d2(vvh_basefill_022, 41)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_041_vvh_basefill_022'] = {'inputs': ['vvh_basefill_022'], 'func': vvh_base_universe_d2_041_vvh_basefill_022}


def vvh_base_universe_d2_042_vvh_basefill_025(vvh_basefill_025):
    return _base_universe_d2(vvh_basefill_025, 42)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_042_vvh_basefill_025'] = {'inputs': ['vvh_basefill_025'], 'func': vvh_base_universe_d2_042_vvh_basefill_025}


def vvh_base_universe_d2_043_vvh_basefill_026(vvh_basefill_026):
    return _base_universe_d2(vvh_basefill_026, 43)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_043_vvh_basefill_026'] = {'inputs': ['vvh_basefill_026'], 'func': vvh_base_universe_d2_043_vvh_basefill_026}


def vvh_base_universe_d2_044_vvh_basefill_028(vvh_basefill_028):
    return _base_universe_d2(vvh_basefill_028, 44)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_044_vvh_basefill_028'] = {'inputs': ['vvh_basefill_028'], 'func': vvh_base_universe_d2_044_vvh_basefill_028}


def vvh_base_universe_d2_045_vvh_basefill_030(vvh_basefill_030):
    return _base_universe_d2(vvh_basefill_030, 45)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_045_vvh_basefill_030'] = {'inputs': ['vvh_basefill_030'], 'func': vvh_base_universe_d2_045_vvh_basefill_030}


def vvh_base_universe_d2_046_vvh_basefill_033(vvh_basefill_033):
    return _base_universe_d2(vvh_basefill_033, 46)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_046_vvh_basefill_033'] = {'inputs': ['vvh_basefill_033'], 'func': vvh_base_universe_d2_046_vvh_basefill_033}


def vvh_base_universe_d2_047_vvh_basefill_034(vvh_basefill_034):
    return _base_universe_d2(vvh_basefill_034, 47)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_047_vvh_basefill_034'] = {'inputs': ['vvh_basefill_034'], 'func': vvh_base_universe_d2_047_vvh_basefill_034}


def vvh_base_universe_d2_048_vvh_basefill_036(vvh_basefill_036):
    return _base_universe_d2(vvh_basefill_036, 48)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_048_vvh_basefill_036'] = {'inputs': ['vvh_basefill_036'], 'func': vvh_base_universe_d2_048_vvh_basefill_036}


def vvh_base_universe_d2_049_vvh_basefill_038(vvh_basefill_038):
    return _base_universe_d2(vvh_basefill_038, 49)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_049_vvh_basefill_038'] = {'inputs': ['vvh_basefill_038'], 'func': vvh_base_universe_d2_049_vvh_basefill_038}


def vvh_base_universe_d2_050_vvh_basefill_041(vvh_basefill_041):
    return _base_universe_d2(vvh_basefill_041, 50)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_050_vvh_basefill_041'] = {'inputs': ['vvh_basefill_041'], 'func': vvh_base_universe_d2_050_vvh_basefill_041}


def vvh_base_universe_d2_051_vvh_basefill_042(vvh_basefill_042):
    return _base_universe_d2(vvh_basefill_042, 51)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_051_vvh_basefill_042'] = {'inputs': ['vvh_basefill_042'], 'func': vvh_base_universe_d2_051_vvh_basefill_042}


def vvh_base_universe_d2_052_vvh_basefill_044(vvh_basefill_044):
    return _base_universe_d2(vvh_basefill_044, 52)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_052_vvh_basefill_044'] = {'inputs': ['vvh_basefill_044'], 'func': vvh_base_universe_d2_052_vvh_basefill_044}


def vvh_base_universe_d2_053_vvh_basefill_045(vvh_basefill_045):
    return _base_universe_d2(vvh_basefill_045, 53)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_053_vvh_basefill_045'] = {'inputs': ['vvh_basefill_045'], 'func': vvh_base_universe_d2_053_vvh_basefill_045}


def vvh_base_universe_d2_054_vvh_basefill_046(vvh_basefill_046):
    return _base_universe_d2(vvh_basefill_046, 54)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_054_vvh_basefill_046'] = {'inputs': ['vvh_basefill_046'], 'func': vvh_base_universe_d2_054_vvh_basefill_046}


def vvh_base_universe_d2_055_vvh_basefill_049(vvh_basefill_049):
    return _base_universe_d2(vvh_basefill_049, 55)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_055_vvh_basefill_049'] = {'inputs': ['vvh_basefill_049'], 'func': vvh_base_universe_d2_055_vvh_basefill_049}


def vvh_base_universe_d2_056_vvh_basefill_050(vvh_basefill_050):
    return _base_universe_d2(vvh_basefill_050, 56)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_056_vvh_basefill_050'] = {'inputs': ['vvh_basefill_050'], 'func': vvh_base_universe_d2_056_vvh_basefill_050}


def vvh_base_universe_d2_057_vvh_basefill_052(vvh_basefill_052):
    return _base_universe_d2(vvh_basefill_052, 57)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_057_vvh_basefill_052'] = {'inputs': ['vvh_basefill_052'], 'func': vvh_base_universe_d2_057_vvh_basefill_052}


def vvh_base_universe_d2_058_vvh_basefill_054(vvh_basefill_054):
    return _base_universe_d2(vvh_basefill_054, 58)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_058_vvh_basefill_054'] = {'inputs': ['vvh_basefill_054'], 'func': vvh_base_universe_d2_058_vvh_basefill_054}


def vvh_base_universe_d2_059_vvh_basefill_057(vvh_basefill_057):
    return _base_universe_d2(vvh_basefill_057, 59)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_059_vvh_basefill_057'] = {'inputs': ['vvh_basefill_057'], 'func': vvh_base_universe_d2_059_vvh_basefill_057}


def vvh_base_universe_d2_060_vvh_basefill_058(vvh_basefill_058):
    return _base_universe_d2(vvh_basefill_058, 60)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_060_vvh_basefill_058'] = {'inputs': ['vvh_basefill_058'], 'func': vvh_base_universe_d2_060_vvh_basefill_058}


def vvh_base_universe_d2_061_vvh_basefill_059(vvh_basefill_059):
    return _base_universe_d2(vvh_basefill_059, 61)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_061_vvh_basefill_059'] = {'inputs': ['vvh_basefill_059'], 'func': vvh_base_universe_d2_061_vvh_basefill_059}


def vvh_base_universe_d2_062_vvh_basefill_060(vvh_basefill_060):
    return _base_universe_d2(vvh_basefill_060, 62)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_062_vvh_basefill_060'] = {'inputs': ['vvh_basefill_060'], 'func': vvh_base_universe_d2_062_vvh_basefill_060}


def vvh_base_universe_d2_063_vvh_basefill_062(vvh_basefill_062):
    return _base_universe_d2(vvh_basefill_062, 63)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_063_vvh_basefill_062'] = {'inputs': ['vvh_basefill_062'], 'func': vvh_base_universe_d2_063_vvh_basefill_062}


def vvh_base_universe_d2_064_vvh_basefill_063(vvh_basefill_063):
    return _base_universe_d2(vvh_basefill_063, 64)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_064_vvh_basefill_063'] = {'inputs': ['vvh_basefill_063'], 'func': vvh_base_universe_d2_064_vvh_basefill_063}


def vvh_base_universe_d2_065_vvh_basefill_065(vvh_basefill_065):
    return _base_universe_d2(vvh_basefill_065, 65)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_065_vvh_basefill_065'] = {'inputs': ['vvh_basefill_065'], 'func': vvh_base_universe_d2_065_vvh_basefill_065}


def vvh_base_universe_d2_066_vvh_basefill_066(vvh_basefill_066):
    return _base_universe_d2(vvh_basefill_066, 66)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_066_vvh_basefill_066'] = {'inputs': ['vvh_basefill_066'], 'func': vvh_base_universe_d2_066_vvh_basefill_066}


def vvh_base_universe_d2_067_vvh_basefill_068(vvh_basefill_068):
    return _base_universe_d2(vvh_basefill_068, 67)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_067_vvh_basefill_068'] = {'inputs': ['vvh_basefill_068'], 'func': vvh_base_universe_d2_067_vvh_basefill_068}


def vvh_base_universe_d2_068_vvh_basefill_070(vvh_basefill_070):
    return _base_universe_d2(vvh_basefill_070, 68)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_068_vvh_basefill_070'] = {'inputs': ['vvh_basefill_070'], 'func': vvh_base_universe_d2_068_vvh_basefill_070}


def vvh_base_universe_d2_069_vvh_basefill_073(vvh_basefill_073):
    return _base_universe_d2(vvh_basefill_073, 69)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_069_vvh_basefill_073'] = {'inputs': ['vvh_basefill_073'], 'func': vvh_base_universe_d2_069_vvh_basefill_073}


def vvh_base_universe_d2_070_vvh_basefill_074(vvh_basefill_074):
    return _base_universe_d2(vvh_basefill_074, 70)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_070_vvh_basefill_074'] = {'inputs': ['vvh_basefill_074'], 'func': vvh_base_universe_d2_070_vvh_basefill_074}


def vvh_base_universe_d2_071_vvh_basefill_075(vvh_basefill_075):
    return _base_universe_d2(vvh_basefill_075, 71)
VVH_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvh_base_universe_d2_071_vvh_basefill_075'] = {'inputs': ['vvh_basefill_075'], 'func': vvh_base_universe_d2_071_vvh_basefill_075}
