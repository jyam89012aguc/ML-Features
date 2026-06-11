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



def vvh_176_vvh_001_pe_compression_z_21_accel_1(vvh_151_vvh_001_pe_compression_z_21_roc_1):
    feature = _s(vvh_151_vvh_001_pe_compression_z_21_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def vvh_177_vvh_007_earnings_yield_spike_252_accel_42(vvh_152_vvh_007_earnings_yield_spike_252_roc_42):
    feature = _s(vvh_152_vvh_007_earnings_yield_spike_252_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def vvh_178_vvh_013_ev_marketcap_gap_1512_accel_126(vvh_153_vvh_013_ev_marketcap_gap_1512_roc_126):
    feature = _s(vvh_153_vvh_013_ev_marketcap_gap_1512_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def vvh_179_vvh_019_ps_compression_z_84_accel_378(vvh_154_vvh_019_ps_compression_z_84_roc_378):
    feature = _s(vvh_154_vvh_019_ps_compression_z_84_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)

def vvh_180_vvh_025_pe_compression_z_756_accel_4(vvh_155_vvh_025_pe_compression_z_756_roc_4):
    feature = _s(vvh_155_vvh_025_pe_compression_z_756_roc_4)
    return (_roc(feature, 4).diff(1)).reindex(feature.index)






















VALUATION_VS_HISTORY_REGISTRY_3RD_DERIVATIVES = {
    'vvh_176_vvh_001_pe_compression_z_21_accel_1': {'inputs': ['vvh_151_vvh_001_pe_compression_z_21_roc_1'], 'func': vvh_176_vvh_001_pe_compression_z_21_accel_1},
    'vvh_177_vvh_007_earnings_yield_spike_252_accel_42': {'inputs': ['vvh_152_vvh_007_earnings_yield_spike_252_roc_42'], 'func': vvh_177_vvh_007_earnings_yield_spike_252_accel_42},
    'vvh_178_vvh_013_ev_marketcap_gap_1512_accel_126': {'inputs': ['vvh_153_vvh_013_ev_marketcap_gap_1512_roc_126'], 'func': vvh_178_vvh_013_ev_marketcap_gap_1512_accel_126},
    'vvh_179_vvh_019_ps_compression_z_84_accel_378': {'inputs': ['vvh_154_vvh_019_ps_compression_z_84_roc_378'], 'func': vvh_179_vvh_019_ps_compression_z_84_accel_378},
    'vvh_180_vvh_025_pe_compression_z_756_accel_4': {'inputs': ['vvh_155_vvh_025_pe_compression_z_756_roc_4'], 'func': vvh_180_vvh_025_pe_compression_z_756_accel_4},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def vvh_replacement_d3_001(vvh_replacement_d2_001):
    feature = _clean(vvh_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_001'] = {'inputs': ['vvh_replacement_d2_001'], 'func': vvh_replacement_d3_001}


def vvh_replacement_d3_002(vvh_replacement_d2_002):
    feature = _clean(vvh_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_002'] = {'inputs': ['vvh_replacement_d2_002'], 'func': vvh_replacement_d3_002}


def vvh_replacement_d3_003(vvh_replacement_d2_003):
    feature = _clean(vvh_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_003'] = {'inputs': ['vvh_replacement_d2_003'], 'func': vvh_replacement_d3_003}


def vvh_replacement_d3_004(vvh_replacement_d2_004):
    feature = _clean(vvh_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_004'] = {'inputs': ['vvh_replacement_d2_004'], 'func': vvh_replacement_d3_004}


def vvh_replacement_d3_005(vvh_replacement_d2_005):
    feature = _clean(vvh_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_005'] = {'inputs': ['vvh_replacement_d2_005'], 'func': vvh_replacement_d3_005}


def vvh_replacement_d3_006(vvh_replacement_d2_006):
    feature = _clean(vvh_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_006'] = {'inputs': ['vvh_replacement_d2_006'], 'func': vvh_replacement_d3_006}


def vvh_replacement_d3_007(vvh_replacement_d2_007):
    feature = _clean(vvh_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_007'] = {'inputs': ['vvh_replacement_d2_007'], 'func': vvh_replacement_d3_007}


def vvh_replacement_d3_008(vvh_replacement_d2_008):
    feature = _clean(vvh_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_008'] = {'inputs': ['vvh_replacement_d2_008'], 'func': vvh_replacement_d3_008}


def vvh_replacement_d3_009(vvh_replacement_d2_009):
    feature = _clean(vvh_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_009'] = {'inputs': ['vvh_replacement_d2_009'], 'func': vvh_replacement_d3_009}


def vvh_replacement_d3_010(vvh_replacement_d2_010):
    feature = _clean(vvh_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_010'] = {'inputs': ['vvh_replacement_d2_010'], 'func': vvh_replacement_d3_010}


def vvh_replacement_d3_011(vvh_replacement_d2_011):
    feature = _clean(vvh_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_011'] = {'inputs': ['vvh_replacement_d2_011'], 'func': vvh_replacement_d3_011}


def vvh_replacement_d3_012(vvh_replacement_d2_012):
    feature = _clean(vvh_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_012'] = {'inputs': ['vvh_replacement_d2_012'], 'func': vvh_replacement_d3_012}


def vvh_replacement_d3_013(vvh_replacement_d2_013):
    feature = _clean(vvh_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_013'] = {'inputs': ['vvh_replacement_d2_013'], 'func': vvh_replacement_d3_013}


def vvh_replacement_d3_014(vvh_replacement_d2_014):
    feature = _clean(vvh_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_014'] = {'inputs': ['vvh_replacement_d2_014'], 'func': vvh_replacement_d3_014}


def vvh_replacement_d3_015(vvh_replacement_d2_015):
    feature = _clean(vvh_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_015'] = {'inputs': ['vvh_replacement_d2_015'], 'func': vvh_replacement_d3_015}


def vvh_replacement_d3_016(vvh_replacement_d2_016):
    feature = _clean(vvh_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_016'] = {'inputs': ['vvh_replacement_d2_016'], 'func': vvh_replacement_d3_016}


def vvh_replacement_d3_017(vvh_replacement_d2_017):
    feature = _clean(vvh_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_017'] = {'inputs': ['vvh_replacement_d2_017'], 'func': vvh_replacement_d3_017}


def vvh_replacement_d3_018(vvh_replacement_d2_018):
    feature = _clean(vvh_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_018'] = {'inputs': ['vvh_replacement_d2_018'], 'func': vvh_replacement_d3_018}


def vvh_replacement_d3_019(vvh_replacement_d2_019):
    feature = _clean(vvh_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_019'] = {'inputs': ['vvh_replacement_d2_019'], 'func': vvh_replacement_d3_019}


def vvh_replacement_d3_020(vvh_replacement_d2_020):
    feature = _clean(vvh_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_020'] = {'inputs': ['vvh_replacement_d2_020'], 'func': vvh_replacement_d3_020}


def vvh_replacement_d3_021(vvh_replacement_d2_021):
    feature = _clean(vvh_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_021'] = {'inputs': ['vvh_replacement_d2_021'], 'func': vvh_replacement_d3_021}


def vvh_replacement_d3_022(vvh_replacement_d2_022):
    feature = _clean(vvh_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_022'] = {'inputs': ['vvh_replacement_d2_022'], 'func': vvh_replacement_d3_022}


def vvh_replacement_d3_023(vvh_replacement_d2_023):
    feature = _clean(vvh_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_023'] = {'inputs': ['vvh_replacement_d2_023'], 'func': vvh_replacement_d3_023}


def vvh_replacement_d3_024(vvh_replacement_d2_024):
    feature = _clean(vvh_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_024'] = {'inputs': ['vvh_replacement_d2_024'], 'func': vvh_replacement_d3_024}


def vvh_replacement_d3_025(vvh_replacement_d2_025):
    feature = _clean(vvh_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_025'] = {'inputs': ['vvh_replacement_d2_025'], 'func': vvh_replacement_d3_025}


def vvh_replacement_d3_026(vvh_replacement_d2_026):
    feature = _clean(vvh_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_026'] = {'inputs': ['vvh_replacement_d2_026'], 'func': vvh_replacement_d3_026}


def vvh_replacement_d3_027(vvh_replacement_d2_027):
    feature = _clean(vvh_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_027'] = {'inputs': ['vvh_replacement_d2_027'], 'func': vvh_replacement_d3_027}


def vvh_replacement_d3_028(vvh_replacement_d2_028):
    feature = _clean(vvh_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_028'] = {'inputs': ['vvh_replacement_d2_028'], 'func': vvh_replacement_d3_028}


def vvh_replacement_d3_029(vvh_replacement_d2_029):
    feature = _clean(vvh_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_029'] = {'inputs': ['vvh_replacement_d2_029'], 'func': vvh_replacement_d3_029}


def vvh_replacement_d3_030(vvh_replacement_d2_030):
    feature = _clean(vvh_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_030'] = {'inputs': ['vvh_replacement_d2_030'], 'func': vvh_replacement_d3_030}


def vvh_replacement_d3_031(vvh_replacement_d2_031):
    feature = _clean(vvh_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_031'] = {'inputs': ['vvh_replacement_d2_031'], 'func': vvh_replacement_d3_031}


def vvh_replacement_d3_032(vvh_replacement_d2_032):
    feature = _clean(vvh_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_032'] = {'inputs': ['vvh_replacement_d2_032'], 'func': vvh_replacement_d3_032}


def vvh_replacement_d3_033(vvh_replacement_d2_033):
    feature = _clean(vvh_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_033'] = {'inputs': ['vvh_replacement_d2_033'], 'func': vvh_replacement_d3_033}


def vvh_replacement_d3_034(vvh_replacement_d2_034):
    feature = _clean(vvh_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_034'] = {'inputs': ['vvh_replacement_d2_034'], 'func': vvh_replacement_d3_034}


def vvh_replacement_d3_035(vvh_replacement_d2_035):
    feature = _clean(vvh_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_035'] = {'inputs': ['vvh_replacement_d2_035'], 'func': vvh_replacement_d3_035}


def vvh_replacement_d3_036(vvh_replacement_d2_036):
    feature = _clean(vvh_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_036'] = {'inputs': ['vvh_replacement_d2_036'], 'func': vvh_replacement_d3_036}


def vvh_replacement_d3_037(vvh_replacement_d2_037):
    feature = _clean(vvh_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_037'] = {'inputs': ['vvh_replacement_d2_037'], 'func': vvh_replacement_d3_037}


def vvh_replacement_d3_038(vvh_replacement_d2_038):
    feature = _clean(vvh_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_038'] = {'inputs': ['vvh_replacement_d2_038'], 'func': vvh_replacement_d3_038}


def vvh_replacement_d3_039(vvh_replacement_d2_039):
    feature = _clean(vvh_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_039'] = {'inputs': ['vvh_replacement_d2_039'], 'func': vvh_replacement_d3_039}


def vvh_replacement_d3_040(vvh_replacement_d2_040):
    feature = _clean(vvh_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_040'] = {'inputs': ['vvh_replacement_d2_040'], 'func': vvh_replacement_d3_040}


def vvh_replacement_d3_041(vvh_replacement_d2_041):
    feature = _clean(vvh_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_041'] = {'inputs': ['vvh_replacement_d2_041'], 'func': vvh_replacement_d3_041}


def vvh_replacement_d3_042(vvh_replacement_d2_042):
    feature = _clean(vvh_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_042'] = {'inputs': ['vvh_replacement_d2_042'], 'func': vvh_replacement_d3_042}


def vvh_replacement_d3_043(vvh_replacement_d2_043):
    feature = _clean(vvh_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_043'] = {'inputs': ['vvh_replacement_d2_043'], 'func': vvh_replacement_d3_043}


def vvh_replacement_d3_044(vvh_replacement_d2_044):
    feature = _clean(vvh_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_044'] = {'inputs': ['vvh_replacement_d2_044'], 'func': vvh_replacement_d3_044}


def vvh_replacement_d3_045(vvh_replacement_d2_045):
    feature = _clean(vvh_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_045'] = {'inputs': ['vvh_replacement_d2_045'], 'func': vvh_replacement_d3_045}


def vvh_replacement_d3_046(vvh_replacement_d2_046):
    feature = _clean(vvh_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_046'] = {'inputs': ['vvh_replacement_d2_046'], 'func': vvh_replacement_d3_046}


def vvh_replacement_d3_047(vvh_replacement_d2_047):
    feature = _clean(vvh_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_047'] = {'inputs': ['vvh_replacement_d2_047'], 'func': vvh_replacement_d3_047}


def vvh_replacement_d3_048(vvh_replacement_d2_048):
    feature = _clean(vvh_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_048'] = {'inputs': ['vvh_replacement_d2_048'], 'func': vvh_replacement_d3_048}


def vvh_replacement_d3_049(vvh_replacement_d2_049):
    feature = _clean(vvh_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_049'] = {'inputs': ['vvh_replacement_d2_049'], 'func': vvh_replacement_d3_049}


def vvh_replacement_d3_050(vvh_replacement_d2_050):
    feature = _clean(vvh_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_050'] = {'inputs': ['vvh_replacement_d2_050'], 'func': vvh_replacement_d3_050}


def vvh_replacement_d3_051(vvh_replacement_d2_051):
    feature = _clean(vvh_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_051'] = {'inputs': ['vvh_replacement_d2_051'], 'func': vvh_replacement_d3_051}


def vvh_replacement_d3_052(vvh_replacement_d2_052):
    feature = _clean(vvh_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_052'] = {'inputs': ['vvh_replacement_d2_052'], 'func': vvh_replacement_d3_052}


def vvh_replacement_d3_053(vvh_replacement_d2_053):
    feature = _clean(vvh_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_053'] = {'inputs': ['vvh_replacement_d2_053'], 'func': vvh_replacement_d3_053}


def vvh_replacement_d3_054(vvh_replacement_d2_054):
    feature = _clean(vvh_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_054'] = {'inputs': ['vvh_replacement_d2_054'], 'func': vvh_replacement_d3_054}


def vvh_replacement_d3_055(vvh_replacement_d2_055):
    feature = _clean(vvh_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_055'] = {'inputs': ['vvh_replacement_d2_055'], 'func': vvh_replacement_d3_055}


def vvh_replacement_d3_056(vvh_replacement_d2_056):
    feature = _clean(vvh_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_056'] = {'inputs': ['vvh_replacement_d2_056'], 'func': vvh_replacement_d3_056}


def vvh_replacement_d3_057(vvh_replacement_d2_057):
    feature = _clean(vvh_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_057'] = {'inputs': ['vvh_replacement_d2_057'], 'func': vvh_replacement_d3_057}


def vvh_replacement_d3_058(vvh_replacement_d2_058):
    feature = _clean(vvh_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_058'] = {'inputs': ['vvh_replacement_d2_058'], 'func': vvh_replacement_d3_058}


def vvh_replacement_d3_059(vvh_replacement_d2_059):
    feature = _clean(vvh_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_059'] = {'inputs': ['vvh_replacement_d2_059'], 'func': vvh_replacement_d3_059}


def vvh_replacement_d3_060(vvh_replacement_d2_060):
    feature = _clean(vvh_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_060'] = {'inputs': ['vvh_replacement_d2_060'], 'func': vvh_replacement_d3_060}


def vvh_replacement_d3_061(vvh_replacement_d2_061):
    feature = _clean(vvh_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_061'] = {'inputs': ['vvh_replacement_d2_061'], 'func': vvh_replacement_d3_061}


def vvh_replacement_d3_062(vvh_replacement_d2_062):
    feature = _clean(vvh_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_062'] = {'inputs': ['vvh_replacement_d2_062'], 'func': vvh_replacement_d3_062}


def vvh_replacement_d3_063(vvh_replacement_d2_063):
    feature = _clean(vvh_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_063'] = {'inputs': ['vvh_replacement_d2_063'], 'func': vvh_replacement_d3_063}


def vvh_replacement_d3_064(vvh_replacement_d2_064):
    feature = _clean(vvh_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_064'] = {'inputs': ['vvh_replacement_d2_064'], 'func': vvh_replacement_d3_064}


def vvh_replacement_d3_065(vvh_replacement_d2_065):
    feature = _clean(vvh_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_065'] = {'inputs': ['vvh_replacement_d2_065'], 'func': vvh_replacement_d3_065}


def vvh_replacement_d3_066(vvh_replacement_d2_066):
    feature = _clean(vvh_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_066'] = {'inputs': ['vvh_replacement_d2_066'], 'func': vvh_replacement_d3_066}


def vvh_replacement_d3_067(vvh_replacement_d2_067):
    feature = _clean(vvh_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_067'] = {'inputs': ['vvh_replacement_d2_067'], 'func': vvh_replacement_d3_067}


def vvh_replacement_d3_068(vvh_replacement_d2_068):
    feature = _clean(vvh_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_068'] = {'inputs': ['vvh_replacement_d2_068'], 'func': vvh_replacement_d3_068}


def vvh_replacement_d3_069(vvh_replacement_d2_069):
    feature = _clean(vvh_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_069'] = {'inputs': ['vvh_replacement_d2_069'], 'func': vvh_replacement_d3_069}


def vvh_replacement_d3_070(vvh_replacement_d2_070):
    feature = _clean(vvh_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_070'] = {'inputs': ['vvh_replacement_d2_070'], 'func': vvh_replacement_d3_070}


def vvh_replacement_d3_071(vvh_replacement_d2_071):
    feature = _clean(vvh_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_071'] = {'inputs': ['vvh_replacement_d2_071'], 'func': vvh_replacement_d3_071}


def vvh_replacement_d3_072(vvh_replacement_d2_072):
    feature = _clean(vvh_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_072'] = {'inputs': ['vvh_replacement_d2_072'], 'func': vvh_replacement_d3_072}


def vvh_replacement_d3_073(vvh_replacement_d2_073):
    feature = _clean(vvh_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_073'] = {'inputs': ['vvh_replacement_d2_073'], 'func': vvh_replacement_d3_073}


def vvh_replacement_d3_074(vvh_replacement_d2_074):
    feature = _clean(vvh_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_074'] = {'inputs': ['vvh_replacement_d2_074'], 'func': vvh_replacement_d3_074}


def vvh_replacement_d3_075(vvh_replacement_d2_075):
    feature = _clean(vvh_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_075'] = {'inputs': ['vvh_replacement_d2_075'], 'func': vvh_replacement_d3_075}


def vvh_replacement_d3_076(vvh_replacement_d2_076):
    feature = _clean(vvh_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_076'] = {'inputs': ['vvh_replacement_d2_076'], 'func': vvh_replacement_d3_076}


def vvh_replacement_d3_077(vvh_replacement_d2_077):
    feature = _clean(vvh_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_077'] = {'inputs': ['vvh_replacement_d2_077'], 'func': vvh_replacement_d3_077}


def vvh_replacement_d3_078(vvh_replacement_d2_078):
    feature = _clean(vvh_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_078'] = {'inputs': ['vvh_replacement_d2_078'], 'func': vvh_replacement_d3_078}


def vvh_replacement_d3_079(vvh_replacement_d2_079):
    feature = _clean(vvh_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_079'] = {'inputs': ['vvh_replacement_d2_079'], 'func': vvh_replacement_d3_079}


def vvh_replacement_d3_080(vvh_replacement_d2_080):
    feature = _clean(vvh_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_080'] = {'inputs': ['vvh_replacement_d2_080'], 'func': vvh_replacement_d3_080}


def vvh_replacement_d3_081(vvh_replacement_d2_081):
    feature = _clean(vvh_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_081'] = {'inputs': ['vvh_replacement_d2_081'], 'func': vvh_replacement_d3_081}


def vvh_replacement_d3_082(vvh_replacement_d2_082):
    feature = _clean(vvh_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_082'] = {'inputs': ['vvh_replacement_d2_082'], 'func': vvh_replacement_d3_082}


def vvh_replacement_d3_083(vvh_replacement_d2_083):
    feature = _clean(vvh_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_083'] = {'inputs': ['vvh_replacement_d2_083'], 'func': vvh_replacement_d3_083}


def vvh_replacement_d3_084(vvh_replacement_d2_084):
    feature = _clean(vvh_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_084'] = {'inputs': ['vvh_replacement_d2_084'], 'func': vvh_replacement_d3_084}


def vvh_replacement_d3_085(vvh_replacement_d2_085):
    feature = _clean(vvh_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_085'] = {'inputs': ['vvh_replacement_d2_085'], 'func': vvh_replacement_d3_085}


def vvh_replacement_d3_086(vvh_replacement_d2_086):
    feature = _clean(vvh_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_086'] = {'inputs': ['vvh_replacement_d2_086'], 'func': vvh_replacement_d3_086}


def vvh_replacement_d3_087(vvh_replacement_d2_087):
    feature = _clean(vvh_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_087'] = {'inputs': ['vvh_replacement_d2_087'], 'func': vvh_replacement_d3_087}


def vvh_replacement_d3_088(vvh_replacement_d2_088):
    feature = _clean(vvh_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_088'] = {'inputs': ['vvh_replacement_d2_088'], 'func': vvh_replacement_d3_088}


def vvh_replacement_d3_089(vvh_replacement_d2_089):
    feature = _clean(vvh_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_089'] = {'inputs': ['vvh_replacement_d2_089'], 'func': vvh_replacement_d3_089}


def vvh_replacement_d3_090(vvh_replacement_d2_090):
    feature = _clean(vvh_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_090'] = {'inputs': ['vvh_replacement_d2_090'], 'func': vvh_replacement_d3_090}


def vvh_replacement_d3_091(vvh_replacement_d2_091):
    feature = _clean(vvh_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_091'] = {'inputs': ['vvh_replacement_d2_091'], 'func': vvh_replacement_d3_091}


def vvh_replacement_d3_092(vvh_replacement_d2_092):
    feature = _clean(vvh_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_092'] = {'inputs': ['vvh_replacement_d2_092'], 'func': vvh_replacement_d3_092}


def vvh_replacement_d3_093(vvh_replacement_d2_093):
    feature = _clean(vvh_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_093'] = {'inputs': ['vvh_replacement_d2_093'], 'func': vvh_replacement_d3_093}


def vvh_replacement_d3_094(vvh_replacement_d2_094):
    feature = _clean(vvh_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_094'] = {'inputs': ['vvh_replacement_d2_094'], 'func': vvh_replacement_d3_094}


def vvh_replacement_d3_095(vvh_replacement_d2_095):
    feature = _clean(vvh_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_095'] = {'inputs': ['vvh_replacement_d2_095'], 'func': vvh_replacement_d3_095}


def vvh_replacement_d3_096(vvh_replacement_d2_096):
    feature = _clean(vvh_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_096'] = {'inputs': ['vvh_replacement_d2_096'], 'func': vvh_replacement_d3_096}


def vvh_replacement_d3_097(vvh_replacement_d2_097):
    feature = _clean(vvh_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_097'] = {'inputs': ['vvh_replacement_d2_097'], 'func': vvh_replacement_d3_097}


def vvh_replacement_d3_098(vvh_replacement_d2_098):
    feature = _clean(vvh_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_098'] = {'inputs': ['vvh_replacement_d2_098'], 'func': vvh_replacement_d3_098}


def vvh_replacement_d3_099(vvh_replacement_d2_099):
    feature = _clean(vvh_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_099'] = {'inputs': ['vvh_replacement_d2_099'], 'func': vvh_replacement_d3_099}


def vvh_replacement_d3_100(vvh_replacement_d2_100):
    feature = _clean(vvh_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_100'] = {'inputs': ['vvh_replacement_d2_100'], 'func': vvh_replacement_d3_100}


def vvh_replacement_d3_101(vvh_replacement_d2_101):
    feature = _clean(vvh_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_101'] = {'inputs': ['vvh_replacement_d2_101'], 'func': vvh_replacement_d3_101}


def vvh_replacement_d3_102(vvh_replacement_d2_102):
    feature = _clean(vvh_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_102'] = {'inputs': ['vvh_replacement_d2_102'], 'func': vvh_replacement_d3_102}


def vvh_replacement_d3_103(vvh_replacement_d2_103):
    feature = _clean(vvh_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_103'] = {'inputs': ['vvh_replacement_d2_103'], 'func': vvh_replacement_d3_103}


def vvh_replacement_d3_104(vvh_replacement_d2_104):
    feature = _clean(vvh_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_104'] = {'inputs': ['vvh_replacement_d2_104'], 'func': vvh_replacement_d3_104}


def vvh_replacement_d3_105(vvh_replacement_d2_105):
    feature = _clean(vvh_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_105'] = {'inputs': ['vvh_replacement_d2_105'], 'func': vvh_replacement_d3_105}


def vvh_replacement_d3_106(vvh_replacement_d2_106):
    feature = _clean(vvh_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_106'] = {'inputs': ['vvh_replacement_d2_106'], 'func': vvh_replacement_d3_106}


def vvh_replacement_d3_107(vvh_replacement_d2_107):
    feature = _clean(vvh_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_107'] = {'inputs': ['vvh_replacement_d2_107'], 'func': vvh_replacement_d3_107}


def vvh_replacement_d3_108(vvh_replacement_d2_108):
    feature = _clean(vvh_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_108'] = {'inputs': ['vvh_replacement_d2_108'], 'func': vvh_replacement_d3_108}


def vvh_replacement_d3_109(vvh_replacement_d2_109):
    feature = _clean(vvh_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_109'] = {'inputs': ['vvh_replacement_d2_109'], 'func': vvh_replacement_d3_109}


def vvh_replacement_d3_110(vvh_replacement_d2_110):
    feature = _clean(vvh_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_110'] = {'inputs': ['vvh_replacement_d2_110'], 'func': vvh_replacement_d3_110}


def vvh_replacement_d3_111(vvh_replacement_d2_111):
    feature = _clean(vvh_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_111'] = {'inputs': ['vvh_replacement_d2_111'], 'func': vvh_replacement_d3_111}


def vvh_replacement_d3_112(vvh_replacement_d2_112):
    feature = _clean(vvh_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_112'] = {'inputs': ['vvh_replacement_d2_112'], 'func': vvh_replacement_d3_112}


def vvh_replacement_d3_113(vvh_replacement_d2_113):
    feature = _clean(vvh_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_113'] = {'inputs': ['vvh_replacement_d2_113'], 'func': vvh_replacement_d3_113}


def vvh_replacement_d3_114(vvh_replacement_d2_114):
    feature = _clean(vvh_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_114'] = {'inputs': ['vvh_replacement_d2_114'], 'func': vvh_replacement_d3_114}


def vvh_replacement_d3_115(vvh_replacement_d2_115):
    feature = _clean(vvh_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_115'] = {'inputs': ['vvh_replacement_d2_115'], 'func': vvh_replacement_d3_115}


def vvh_replacement_d3_116(vvh_replacement_d2_116):
    feature = _clean(vvh_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_116'] = {'inputs': ['vvh_replacement_d2_116'], 'func': vvh_replacement_d3_116}


def vvh_replacement_d3_117(vvh_replacement_d2_117):
    feature = _clean(vvh_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_117'] = {'inputs': ['vvh_replacement_d2_117'], 'func': vvh_replacement_d3_117}


def vvh_replacement_d3_118(vvh_replacement_d2_118):
    feature = _clean(vvh_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_118'] = {'inputs': ['vvh_replacement_d2_118'], 'func': vvh_replacement_d3_118}


def vvh_replacement_d3_119(vvh_replacement_d2_119):
    feature = _clean(vvh_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_119'] = {'inputs': ['vvh_replacement_d2_119'], 'func': vvh_replacement_d3_119}


def vvh_replacement_d3_120(vvh_replacement_d2_120):
    feature = _clean(vvh_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_120'] = {'inputs': ['vvh_replacement_d2_120'], 'func': vvh_replacement_d3_120}


def vvh_replacement_d3_121(vvh_replacement_d2_121):
    feature = _clean(vvh_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_121'] = {'inputs': ['vvh_replacement_d2_121'], 'func': vvh_replacement_d3_121}


def vvh_replacement_d3_122(vvh_replacement_d2_122):
    feature = _clean(vvh_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_122'] = {'inputs': ['vvh_replacement_d2_122'], 'func': vvh_replacement_d3_122}


def vvh_replacement_d3_123(vvh_replacement_d2_123):
    feature = _clean(vvh_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_123'] = {'inputs': ['vvh_replacement_d2_123'], 'func': vvh_replacement_d3_123}


def vvh_replacement_d3_124(vvh_replacement_d2_124):
    feature = _clean(vvh_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_124'] = {'inputs': ['vvh_replacement_d2_124'], 'func': vvh_replacement_d3_124}


def vvh_replacement_d3_125(vvh_replacement_d2_125):
    feature = _clean(vvh_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_125'] = {'inputs': ['vvh_replacement_d2_125'], 'func': vvh_replacement_d3_125}


def vvh_replacement_d3_126(vvh_replacement_d2_126):
    feature = _clean(vvh_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_126'] = {'inputs': ['vvh_replacement_d2_126'], 'func': vvh_replacement_d3_126}


def vvh_replacement_d3_127(vvh_replacement_d2_127):
    feature = _clean(vvh_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_127'] = {'inputs': ['vvh_replacement_d2_127'], 'func': vvh_replacement_d3_127}


def vvh_replacement_d3_128(vvh_replacement_d2_128):
    feature = _clean(vvh_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_128'] = {'inputs': ['vvh_replacement_d2_128'], 'func': vvh_replacement_d3_128}


def vvh_replacement_d3_129(vvh_replacement_d2_129):
    feature = _clean(vvh_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_129'] = {'inputs': ['vvh_replacement_d2_129'], 'func': vvh_replacement_d3_129}


def vvh_replacement_d3_130(vvh_replacement_d2_130):
    feature = _clean(vvh_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_130'] = {'inputs': ['vvh_replacement_d2_130'], 'func': vvh_replacement_d3_130}


def vvh_replacement_d3_131(vvh_replacement_d2_131):
    feature = _clean(vvh_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_131'] = {'inputs': ['vvh_replacement_d2_131'], 'func': vvh_replacement_d3_131}


def vvh_replacement_d3_132(vvh_replacement_d2_132):
    feature = _clean(vvh_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_132'] = {'inputs': ['vvh_replacement_d2_132'], 'func': vvh_replacement_d3_132}


def vvh_replacement_d3_133(vvh_replacement_d2_133):
    feature = _clean(vvh_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_133'] = {'inputs': ['vvh_replacement_d2_133'], 'func': vvh_replacement_d3_133}


def vvh_replacement_d3_134(vvh_replacement_d2_134):
    feature = _clean(vvh_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_134'] = {'inputs': ['vvh_replacement_d2_134'], 'func': vvh_replacement_d3_134}


def vvh_replacement_d3_135(vvh_replacement_d2_135):
    feature = _clean(vvh_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_135'] = {'inputs': ['vvh_replacement_d2_135'], 'func': vvh_replacement_d3_135}


def vvh_replacement_d3_136(vvh_replacement_d2_136):
    feature = _clean(vvh_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_136'] = {'inputs': ['vvh_replacement_d2_136'], 'func': vvh_replacement_d3_136}


def vvh_replacement_d3_137(vvh_replacement_d2_137):
    feature = _clean(vvh_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_137'] = {'inputs': ['vvh_replacement_d2_137'], 'func': vvh_replacement_d3_137}


def vvh_replacement_d3_138(vvh_replacement_d2_138):
    feature = _clean(vvh_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
VVH_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvh_replacement_d3_138'] = {'inputs': ['vvh_replacement_d2_138'], 'func': vvh_replacement_d3_138}


# Third-derivative extensions for repaired first-base features.
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def vvh_base_universe_d3_001_vvh_002_pb_compression_z_42(vvh_base_universe_d2_001_vvh_002_pb_compression_z_42):
    return _base_universe_d3(vvh_base_universe_d2_001_vvh_002_pb_compression_z_42, 1)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_001_vvh_002_pb_compression_z_42'] = {'inputs': ['vvh_base_universe_d2_001_vvh_002_pb_compression_z_42'], 'func': vvh_base_universe_d3_001_vvh_002_pb_compression_z_42}


def vvh_base_universe_d3_002_vvh_003_ps_compression_z_63(vvh_base_universe_d2_002_vvh_003_ps_compression_z_63):
    return _base_universe_d3(vvh_base_universe_d2_002_vvh_003_ps_compression_z_63, 2)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_002_vvh_003_ps_compression_z_63'] = {'inputs': ['vvh_base_universe_d2_002_vvh_003_ps_compression_z_63'], 'func': vvh_base_universe_d3_002_vvh_003_ps_compression_z_63}


def vvh_base_universe_d3_003_vvh_005_ev_marketcap_gap_126(vvh_base_universe_d2_003_vvh_005_ev_marketcap_gap_126):
    return _base_universe_d3(vvh_base_universe_d2_003_vvh_005_ev_marketcap_gap_126, 3)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_003_vvh_005_ev_marketcap_gap_126'] = {'inputs': ['vvh_base_universe_d2_003_vvh_005_ev_marketcap_gap_126'], 'func': vvh_base_universe_d3_003_vvh_005_ev_marketcap_gap_126}


def vvh_base_universe_d3_004_vvh_006_dividend_yield_spike_189(vvh_base_universe_d2_004_vvh_006_dividend_yield_spike_189):
    return _base_universe_d3(vvh_base_universe_d2_004_vvh_006_dividend_yield_spike_189, 4)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_004_vvh_006_dividend_yield_spike_189'] = {'inputs': ['vvh_base_universe_d2_004_vvh_006_dividend_yield_spike_189'], 'func': vvh_base_universe_d3_004_vvh_006_dividend_yield_spike_189}


def vvh_base_universe_d3_005_vvh_008_valuation_history_depth_378(vvh_base_universe_d2_005_vvh_008_valuation_history_depth_378):
    return _base_universe_d3(vvh_base_universe_d2_005_vvh_008_valuation_history_depth_378, 5)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_005_vvh_008_valuation_history_depth_378'] = {'inputs': ['vvh_base_universe_d2_005_vvh_008_valuation_history_depth_378'], 'func': vvh_base_universe_d3_005_vvh_008_valuation_history_depth_378}


def vvh_base_universe_d3_006_vvh_009_pe_compression_z_504(vvh_base_universe_d2_006_vvh_009_pe_compression_z_504):
    return _base_universe_d3(vvh_base_universe_d2_006_vvh_009_pe_compression_z_504, 6)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_006_vvh_009_pe_compression_z_504'] = {'inputs': ['vvh_base_universe_d2_006_vvh_009_pe_compression_z_504'], 'func': vvh_base_universe_d3_006_vvh_009_pe_compression_z_504}


def vvh_base_universe_d3_007_vvh_010_pb_compression_z_756(vvh_base_universe_d2_007_vvh_010_pb_compression_z_756):
    return _base_universe_d3(vvh_base_universe_d2_007_vvh_010_pb_compression_z_756, 7)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_007_vvh_010_pb_compression_z_756'] = {'inputs': ['vvh_base_universe_d2_007_vvh_010_pb_compression_z_756'], 'func': vvh_base_universe_d3_007_vvh_010_pb_compression_z_756}


def vvh_base_universe_d3_008_vvh_011_ps_compression_z_1008(vvh_base_universe_d2_008_vvh_011_ps_compression_z_1008):
    return _base_universe_d3(vvh_base_universe_d2_008_vvh_011_ps_compression_z_1008, 8)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_008_vvh_011_ps_compression_z_1008'] = {'inputs': ['vvh_base_universe_d2_008_vvh_011_ps_compression_z_1008'], 'func': vvh_base_universe_d3_008_vvh_011_ps_compression_z_1008}


def vvh_base_universe_d3_009_vvh_014_dividend_yield_spike_63(vvh_base_universe_d2_009_vvh_014_dividend_yield_spike_63):
    return _base_universe_d3(vvh_base_universe_d2_009_vvh_014_dividend_yield_spike_63, 9)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_009_vvh_014_dividend_yield_spike_63'] = {'inputs': ['vvh_base_universe_d2_009_vvh_014_dividend_yield_spike_63'], 'func': vvh_base_universe_d3_009_vvh_014_dividend_yield_spike_63}


def vvh_base_universe_d3_010_vvh_016_valuation_history_depth_21(vvh_base_universe_d2_010_vvh_016_valuation_history_depth_21):
    return _base_universe_d3(vvh_base_universe_d2_010_vvh_016_valuation_history_depth_21, 10)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_010_vvh_016_valuation_history_depth_21'] = {'inputs': ['vvh_base_universe_d2_010_vvh_016_valuation_history_depth_21'], 'func': vvh_base_universe_d3_010_vvh_016_valuation_history_depth_21}


def vvh_base_universe_d3_011_vvh_021_ev_marketcap_gap_189(vvh_base_universe_d2_011_vvh_021_ev_marketcap_gap_189):
    return _base_universe_d3(vvh_base_universe_d2_011_vvh_021_ev_marketcap_gap_189, 11)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_011_vvh_021_ev_marketcap_gap_189'] = {'inputs': ['vvh_base_universe_d2_011_vvh_021_ev_marketcap_gap_189'], 'func': vvh_base_universe_d3_011_vvh_021_ev_marketcap_gap_189}


def vvh_base_universe_d3_012_vvh_023_earnings_yield_spike_378(vvh_base_universe_d2_012_vvh_023_earnings_yield_spike_378):
    return _base_universe_d3(vvh_base_universe_d2_012_vvh_023_earnings_yield_spike_378, 12)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_012_vvh_023_earnings_yield_spike_378'] = {'inputs': ['vvh_base_universe_d2_012_vvh_023_earnings_yield_spike_378'], 'func': vvh_base_universe_d3_012_vvh_023_earnings_yield_spike_378}


def vvh_base_universe_d3_013_vvh_024_valuation_history_depth_504(vvh_base_universe_d2_013_vvh_024_valuation_history_depth_504):
    return _base_universe_d3(vvh_base_universe_d2_013_vvh_024_valuation_history_depth_504, 13)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_013_vvh_024_valuation_history_depth_504'] = {'inputs': ['vvh_base_universe_d2_013_vvh_024_valuation_history_depth_504'], 'func': vvh_base_universe_d3_013_vvh_024_valuation_history_depth_504}


def vvh_base_universe_d3_014_vvh_027_ps_compression_z_1260(vvh_base_universe_d2_014_vvh_027_ps_compression_z_1260):
    return _base_universe_d3(vvh_base_universe_d2_014_vvh_027_ps_compression_z_1260, 14)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_014_vvh_027_ps_compression_z_1260'] = {'inputs': ['vvh_base_universe_d2_014_vvh_027_ps_compression_z_1260'], 'func': vvh_base_universe_d3_014_vvh_027_ps_compression_z_1260}


def vvh_base_universe_d3_015_vvh_029_ev_marketcap_gap_63(vvh_base_universe_d2_015_vvh_029_ev_marketcap_gap_63):
    return _base_universe_d3(vvh_base_universe_d2_015_vvh_029_ev_marketcap_gap_63, 15)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_015_vvh_029_ev_marketcap_gap_63'] = {'inputs': ['vvh_base_universe_d2_015_vvh_029_ev_marketcap_gap_63'], 'func': vvh_base_universe_d3_015_vvh_029_ev_marketcap_gap_63}


def vvh_base_universe_d3_016_vvh_031_earnings_yield_spike_21(vvh_base_universe_d2_016_vvh_031_earnings_yield_spike_21):
    return _base_universe_d3(vvh_base_universe_d2_016_vvh_031_earnings_yield_spike_21, 16)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_016_vvh_031_earnings_yield_spike_21'] = {'inputs': ['vvh_base_universe_d2_016_vvh_031_earnings_yield_spike_21'], 'func': vvh_base_universe_d3_016_vvh_031_earnings_yield_spike_21}


def vvh_base_universe_d3_017_vvh_032_valuation_history_depth_42(vvh_base_universe_d2_017_vvh_032_valuation_history_depth_42):
    return _base_universe_d3(vvh_base_universe_d2_017_vvh_032_valuation_history_depth_42, 17)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_017_vvh_032_valuation_history_depth_42'] = {'inputs': ['vvh_base_universe_d2_017_vvh_032_valuation_history_depth_42'], 'func': vvh_base_universe_d3_017_vvh_032_valuation_history_depth_42}


def vvh_base_universe_d3_018_vvh_035_ps_compression_z_126(vvh_base_universe_d2_018_vvh_035_ps_compression_z_126):
    return _base_universe_d3(vvh_base_universe_d2_018_vvh_035_ps_compression_z_126, 18)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_018_vvh_035_ps_compression_z_126'] = {'inputs': ['vvh_base_universe_d2_018_vvh_035_ps_compression_z_126'], 'func': vvh_base_universe_d3_018_vvh_035_ps_compression_z_126}


def vvh_base_universe_d3_019_vvh_037_ev_marketcap_gap_252(vvh_base_universe_d2_019_vvh_037_ev_marketcap_gap_252):
    return _base_universe_d3(vvh_base_universe_d2_019_vvh_037_ev_marketcap_gap_252, 19)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_019_vvh_037_ev_marketcap_gap_252'] = {'inputs': ['vvh_base_universe_d2_019_vvh_037_ev_marketcap_gap_252'], 'func': vvh_base_universe_d3_019_vvh_037_ev_marketcap_gap_252}


def vvh_base_universe_d3_020_vvh_039_earnings_yield_spike_504(vvh_base_universe_d2_020_vvh_039_earnings_yield_spike_504):
    return _base_universe_d3(vvh_base_universe_d2_020_vvh_039_earnings_yield_spike_504, 20)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_020_vvh_039_earnings_yield_spike_504'] = {'inputs': ['vvh_base_universe_d2_020_vvh_039_earnings_yield_spike_504'], 'func': vvh_base_universe_d3_020_vvh_039_earnings_yield_spike_504}


def vvh_base_universe_d3_021_vvh_040_valuation_history_depth_756(vvh_base_universe_d2_021_vvh_040_valuation_history_depth_756):
    return _base_universe_d3(vvh_base_universe_d2_021_vvh_040_valuation_history_depth_756, 21)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_021_vvh_040_valuation_history_depth_756'] = {'inputs': ['vvh_base_universe_d2_021_vvh_040_valuation_history_depth_756'], 'func': vvh_base_universe_d3_021_vvh_040_valuation_history_depth_756}


def vvh_base_universe_d3_022_vvh_043_ps_compression_z_1512(vvh_base_universe_d2_022_vvh_043_ps_compression_z_1512):
    return _base_universe_d3(vvh_base_universe_d2_022_vvh_043_ps_compression_z_1512, 22)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_022_vvh_043_ps_compression_z_1512'] = {'inputs': ['vvh_base_universe_d2_022_vvh_043_ps_compression_z_1512'], 'func': vvh_base_universe_d3_022_vvh_043_ps_compression_z_1512}


def vvh_base_universe_d3_023_vvh_047_earnings_yield_spike_42(vvh_base_universe_d2_023_vvh_047_earnings_yield_spike_42):
    return _base_universe_d3(vvh_base_universe_d2_023_vvh_047_earnings_yield_spike_42, 23)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_023_vvh_047_earnings_yield_spike_42'] = {'inputs': ['vvh_base_universe_d2_023_vvh_047_earnings_yield_spike_42'], 'func': vvh_base_universe_d3_023_vvh_047_earnings_yield_spike_42}


def vvh_base_universe_d3_024_vvh_048_valuation_history_depth_63(vvh_base_universe_d2_024_vvh_048_valuation_history_depth_63):
    return _base_universe_d3(vvh_base_universe_d2_024_vvh_048_valuation_history_depth_63, 24)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_024_vvh_048_valuation_history_depth_63'] = {'inputs': ['vvh_base_universe_d2_024_vvh_048_valuation_history_depth_63'], 'func': vvh_base_universe_d3_024_vvh_048_valuation_history_depth_63}


def vvh_base_universe_d3_025_vvh_051_ps_compression_z_189(vvh_base_universe_d2_025_vvh_051_ps_compression_z_189):
    return _base_universe_d3(vvh_base_universe_d2_025_vvh_051_ps_compression_z_189, 25)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_025_vvh_051_ps_compression_z_189'] = {'inputs': ['vvh_base_universe_d2_025_vvh_051_ps_compression_z_189'], 'func': vvh_base_universe_d3_025_vvh_051_ps_compression_z_189}


def vvh_base_universe_d3_026_vvh_053_ev_marketcap_gap_378(vvh_base_universe_d2_026_vvh_053_ev_marketcap_gap_378):
    return _base_universe_d3(vvh_base_universe_d2_026_vvh_053_ev_marketcap_gap_378, 26)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_026_vvh_053_ev_marketcap_gap_378'] = {'inputs': ['vvh_base_universe_d2_026_vvh_053_ev_marketcap_gap_378'], 'func': vvh_base_universe_d3_026_vvh_053_ev_marketcap_gap_378}


def vvh_base_universe_d3_027_vvh_055_earnings_yield_spike_756(vvh_base_universe_d2_027_vvh_055_earnings_yield_spike_756):
    return _base_universe_d3(vvh_base_universe_d2_027_vvh_055_earnings_yield_spike_756, 27)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_027_vvh_055_earnings_yield_spike_756'] = {'inputs': ['vvh_base_universe_d2_027_vvh_055_earnings_yield_spike_756'], 'func': vvh_base_universe_d3_027_vvh_055_earnings_yield_spike_756}


def vvh_base_universe_d3_028_vvh_056_valuation_history_depth_1008(vvh_base_universe_d2_028_vvh_056_valuation_history_depth_1008):
    return _base_universe_d3(vvh_base_universe_d2_028_vvh_056_valuation_history_depth_1008, 28)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_028_vvh_056_valuation_history_depth_1008'] = {'inputs': ['vvh_base_universe_d2_028_vvh_056_valuation_history_depth_1008'], 'func': vvh_base_universe_d3_028_vvh_056_valuation_history_depth_1008}


def vvh_base_universe_d3_029_vvh_061_ev_marketcap_gap_21(vvh_base_universe_d2_029_vvh_061_ev_marketcap_gap_21):
    return _base_universe_d3(vvh_base_universe_d2_029_vvh_061_ev_marketcap_gap_21, 29)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_029_vvh_061_ev_marketcap_gap_21'] = {'inputs': ['vvh_base_universe_d2_029_vvh_061_ev_marketcap_gap_21'], 'func': vvh_base_universe_d3_029_vvh_061_ev_marketcap_gap_21}


def vvh_base_universe_d3_030_vvh_064_valuation_history_depth_84(vvh_base_universe_d2_030_vvh_064_valuation_history_depth_84):
    return _base_universe_d3(vvh_base_universe_d2_030_vvh_064_valuation_history_depth_84, 30)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_030_vvh_064_valuation_history_depth_84'] = {'inputs': ['vvh_base_universe_d2_030_vvh_064_valuation_history_depth_84'], 'func': vvh_base_universe_d3_030_vvh_064_valuation_history_depth_84}


def vvh_base_universe_d3_031_vvh_067_ps_compression_z_252(vvh_base_universe_d2_031_vvh_067_ps_compression_z_252):
    return _base_universe_d3(vvh_base_universe_d2_031_vvh_067_ps_compression_z_252, 31)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_031_vvh_067_ps_compression_z_252'] = {'inputs': ['vvh_base_universe_d2_031_vvh_067_ps_compression_z_252'], 'func': vvh_base_universe_d3_031_vvh_067_ps_compression_z_252}


def vvh_base_universe_d3_032_vvh_069_ev_marketcap_gap_504(vvh_base_universe_d2_032_vvh_069_ev_marketcap_gap_504):
    return _base_universe_d3(vvh_base_universe_d2_032_vvh_069_ev_marketcap_gap_504, 32)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_032_vvh_069_ev_marketcap_gap_504'] = {'inputs': ['vvh_base_universe_d2_032_vvh_069_ev_marketcap_gap_504'], 'func': vvh_base_universe_d3_032_vvh_069_ev_marketcap_gap_504}


def vvh_base_universe_d3_033_vvh_071_earnings_yield_spike_1008(vvh_base_universe_d2_033_vvh_071_earnings_yield_spike_1008):
    return _base_universe_d3(vvh_base_universe_d2_033_vvh_071_earnings_yield_spike_1008, 33)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_033_vvh_071_earnings_yield_spike_1008'] = {'inputs': ['vvh_base_universe_d2_033_vvh_071_earnings_yield_spike_1008'], 'func': vvh_base_universe_d3_033_vvh_071_earnings_yield_spike_1008}


def vvh_base_universe_d3_034_vvh_072_valuation_history_depth_1260(vvh_base_universe_d2_034_vvh_072_valuation_history_depth_1260):
    return _base_universe_d3(vvh_base_universe_d2_034_vvh_072_valuation_history_depth_1260, 34)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_034_vvh_072_valuation_history_depth_1260'] = {'inputs': ['vvh_base_universe_d2_034_vvh_072_valuation_history_depth_1260'], 'func': vvh_base_universe_d3_034_vvh_072_valuation_history_depth_1260}


def vvh_base_universe_d3_035_vvh_basefill_004(vvh_base_universe_d2_035_vvh_basefill_004):
    return _base_universe_d3(vvh_base_universe_d2_035_vvh_basefill_004, 35)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_035_vvh_basefill_004'] = {'inputs': ['vvh_base_universe_d2_035_vvh_basefill_004'], 'func': vvh_base_universe_d3_035_vvh_basefill_004}


def vvh_base_universe_d3_036_vvh_basefill_012(vvh_base_universe_d2_036_vvh_basefill_012):
    return _base_universe_d3(vvh_base_universe_d2_036_vvh_basefill_012, 36)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_036_vvh_basefill_012'] = {'inputs': ['vvh_base_universe_d2_036_vvh_basefill_012'], 'func': vvh_base_universe_d3_036_vvh_basefill_012}


def vvh_base_universe_d3_037_vvh_basefill_015(vvh_base_universe_d2_037_vvh_basefill_015):
    return _base_universe_d3(vvh_base_universe_d2_037_vvh_basefill_015, 37)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_037_vvh_basefill_015'] = {'inputs': ['vvh_base_universe_d2_037_vvh_basefill_015'], 'func': vvh_base_universe_d3_037_vvh_basefill_015}


def vvh_base_universe_d3_038_vvh_basefill_017(vvh_base_universe_d2_038_vvh_basefill_017):
    return _base_universe_d3(vvh_base_universe_d2_038_vvh_basefill_017, 38)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_038_vvh_basefill_017'] = {'inputs': ['vvh_base_universe_d2_038_vvh_basefill_017'], 'func': vvh_base_universe_d3_038_vvh_basefill_017}


def vvh_base_universe_d3_039_vvh_basefill_018(vvh_base_universe_d2_039_vvh_basefill_018):
    return _base_universe_d3(vvh_base_universe_d2_039_vvh_basefill_018, 39)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_039_vvh_basefill_018'] = {'inputs': ['vvh_base_universe_d2_039_vvh_basefill_018'], 'func': vvh_base_universe_d3_039_vvh_basefill_018}


def vvh_base_universe_d3_040_vvh_basefill_020(vvh_base_universe_d2_040_vvh_basefill_020):
    return _base_universe_d3(vvh_base_universe_d2_040_vvh_basefill_020, 40)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_040_vvh_basefill_020'] = {'inputs': ['vvh_base_universe_d2_040_vvh_basefill_020'], 'func': vvh_base_universe_d3_040_vvh_basefill_020}


def vvh_base_universe_d3_041_vvh_basefill_022(vvh_base_universe_d2_041_vvh_basefill_022):
    return _base_universe_d3(vvh_base_universe_d2_041_vvh_basefill_022, 41)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_041_vvh_basefill_022'] = {'inputs': ['vvh_base_universe_d2_041_vvh_basefill_022'], 'func': vvh_base_universe_d3_041_vvh_basefill_022}


def vvh_base_universe_d3_042_vvh_basefill_025(vvh_base_universe_d2_042_vvh_basefill_025):
    return _base_universe_d3(vvh_base_universe_d2_042_vvh_basefill_025, 42)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_042_vvh_basefill_025'] = {'inputs': ['vvh_base_universe_d2_042_vvh_basefill_025'], 'func': vvh_base_universe_d3_042_vvh_basefill_025}


def vvh_base_universe_d3_043_vvh_basefill_026(vvh_base_universe_d2_043_vvh_basefill_026):
    return _base_universe_d3(vvh_base_universe_d2_043_vvh_basefill_026, 43)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_043_vvh_basefill_026'] = {'inputs': ['vvh_base_universe_d2_043_vvh_basefill_026'], 'func': vvh_base_universe_d3_043_vvh_basefill_026}


def vvh_base_universe_d3_044_vvh_basefill_028(vvh_base_universe_d2_044_vvh_basefill_028):
    return _base_universe_d3(vvh_base_universe_d2_044_vvh_basefill_028, 44)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_044_vvh_basefill_028'] = {'inputs': ['vvh_base_universe_d2_044_vvh_basefill_028'], 'func': vvh_base_universe_d3_044_vvh_basefill_028}


def vvh_base_universe_d3_045_vvh_basefill_030(vvh_base_universe_d2_045_vvh_basefill_030):
    return _base_universe_d3(vvh_base_universe_d2_045_vvh_basefill_030, 45)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_045_vvh_basefill_030'] = {'inputs': ['vvh_base_universe_d2_045_vvh_basefill_030'], 'func': vvh_base_universe_d3_045_vvh_basefill_030}


def vvh_base_universe_d3_046_vvh_basefill_033(vvh_base_universe_d2_046_vvh_basefill_033):
    return _base_universe_d3(vvh_base_universe_d2_046_vvh_basefill_033, 46)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_046_vvh_basefill_033'] = {'inputs': ['vvh_base_universe_d2_046_vvh_basefill_033'], 'func': vvh_base_universe_d3_046_vvh_basefill_033}


def vvh_base_universe_d3_047_vvh_basefill_034(vvh_base_universe_d2_047_vvh_basefill_034):
    return _base_universe_d3(vvh_base_universe_d2_047_vvh_basefill_034, 47)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_047_vvh_basefill_034'] = {'inputs': ['vvh_base_universe_d2_047_vvh_basefill_034'], 'func': vvh_base_universe_d3_047_vvh_basefill_034}


def vvh_base_universe_d3_048_vvh_basefill_036(vvh_base_universe_d2_048_vvh_basefill_036):
    return _base_universe_d3(vvh_base_universe_d2_048_vvh_basefill_036, 48)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_048_vvh_basefill_036'] = {'inputs': ['vvh_base_universe_d2_048_vvh_basefill_036'], 'func': vvh_base_universe_d3_048_vvh_basefill_036}


def vvh_base_universe_d3_049_vvh_basefill_038(vvh_base_universe_d2_049_vvh_basefill_038):
    return _base_universe_d3(vvh_base_universe_d2_049_vvh_basefill_038, 49)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_049_vvh_basefill_038'] = {'inputs': ['vvh_base_universe_d2_049_vvh_basefill_038'], 'func': vvh_base_universe_d3_049_vvh_basefill_038}


def vvh_base_universe_d3_050_vvh_basefill_041(vvh_base_universe_d2_050_vvh_basefill_041):
    return _base_universe_d3(vvh_base_universe_d2_050_vvh_basefill_041, 50)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_050_vvh_basefill_041'] = {'inputs': ['vvh_base_universe_d2_050_vvh_basefill_041'], 'func': vvh_base_universe_d3_050_vvh_basefill_041}


def vvh_base_universe_d3_051_vvh_basefill_042(vvh_base_universe_d2_051_vvh_basefill_042):
    return _base_universe_d3(vvh_base_universe_d2_051_vvh_basefill_042, 51)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_051_vvh_basefill_042'] = {'inputs': ['vvh_base_universe_d2_051_vvh_basefill_042'], 'func': vvh_base_universe_d3_051_vvh_basefill_042}


def vvh_base_universe_d3_052_vvh_basefill_044(vvh_base_universe_d2_052_vvh_basefill_044):
    return _base_universe_d3(vvh_base_universe_d2_052_vvh_basefill_044, 52)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_052_vvh_basefill_044'] = {'inputs': ['vvh_base_universe_d2_052_vvh_basefill_044'], 'func': vvh_base_universe_d3_052_vvh_basefill_044}


def vvh_base_universe_d3_053_vvh_basefill_045(vvh_base_universe_d2_053_vvh_basefill_045):
    return _base_universe_d3(vvh_base_universe_d2_053_vvh_basefill_045, 53)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_053_vvh_basefill_045'] = {'inputs': ['vvh_base_universe_d2_053_vvh_basefill_045'], 'func': vvh_base_universe_d3_053_vvh_basefill_045}


def vvh_base_universe_d3_054_vvh_basefill_046(vvh_base_universe_d2_054_vvh_basefill_046):
    return _base_universe_d3(vvh_base_universe_d2_054_vvh_basefill_046, 54)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_054_vvh_basefill_046'] = {'inputs': ['vvh_base_universe_d2_054_vvh_basefill_046'], 'func': vvh_base_universe_d3_054_vvh_basefill_046}


def vvh_base_universe_d3_055_vvh_basefill_049(vvh_base_universe_d2_055_vvh_basefill_049):
    return _base_universe_d3(vvh_base_universe_d2_055_vvh_basefill_049, 55)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_055_vvh_basefill_049'] = {'inputs': ['vvh_base_universe_d2_055_vvh_basefill_049'], 'func': vvh_base_universe_d3_055_vvh_basefill_049}


def vvh_base_universe_d3_056_vvh_basefill_050(vvh_base_universe_d2_056_vvh_basefill_050):
    return _base_universe_d3(vvh_base_universe_d2_056_vvh_basefill_050, 56)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_056_vvh_basefill_050'] = {'inputs': ['vvh_base_universe_d2_056_vvh_basefill_050'], 'func': vvh_base_universe_d3_056_vvh_basefill_050}


def vvh_base_universe_d3_057_vvh_basefill_052(vvh_base_universe_d2_057_vvh_basefill_052):
    return _base_universe_d3(vvh_base_universe_d2_057_vvh_basefill_052, 57)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_057_vvh_basefill_052'] = {'inputs': ['vvh_base_universe_d2_057_vvh_basefill_052'], 'func': vvh_base_universe_d3_057_vvh_basefill_052}


def vvh_base_universe_d3_058_vvh_basefill_054(vvh_base_universe_d2_058_vvh_basefill_054):
    return _base_universe_d3(vvh_base_universe_d2_058_vvh_basefill_054, 58)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_058_vvh_basefill_054'] = {'inputs': ['vvh_base_universe_d2_058_vvh_basefill_054'], 'func': vvh_base_universe_d3_058_vvh_basefill_054}


def vvh_base_universe_d3_059_vvh_basefill_057(vvh_base_universe_d2_059_vvh_basefill_057):
    return _base_universe_d3(vvh_base_universe_d2_059_vvh_basefill_057, 59)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_059_vvh_basefill_057'] = {'inputs': ['vvh_base_universe_d2_059_vvh_basefill_057'], 'func': vvh_base_universe_d3_059_vvh_basefill_057}


def vvh_base_universe_d3_060_vvh_basefill_058(vvh_base_universe_d2_060_vvh_basefill_058):
    return _base_universe_d3(vvh_base_universe_d2_060_vvh_basefill_058, 60)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_060_vvh_basefill_058'] = {'inputs': ['vvh_base_universe_d2_060_vvh_basefill_058'], 'func': vvh_base_universe_d3_060_vvh_basefill_058}


def vvh_base_universe_d3_061_vvh_basefill_059(vvh_base_universe_d2_061_vvh_basefill_059):
    return _base_universe_d3(vvh_base_universe_d2_061_vvh_basefill_059, 61)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_061_vvh_basefill_059'] = {'inputs': ['vvh_base_universe_d2_061_vvh_basefill_059'], 'func': vvh_base_universe_d3_061_vvh_basefill_059}


def vvh_base_universe_d3_062_vvh_basefill_060(vvh_base_universe_d2_062_vvh_basefill_060):
    return _base_universe_d3(vvh_base_universe_d2_062_vvh_basefill_060, 62)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_062_vvh_basefill_060'] = {'inputs': ['vvh_base_universe_d2_062_vvh_basefill_060'], 'func': vvh_base_universe_d3_062_vvh_basefill_060}


def vvh_base_universe_d3_063_vvh_basefill_062(vvh_base_universe_d2_063_vvh_basefill_062):
    return _base_universe_d3(vvh_base_universe_d2_063_vvh_basefill_062, 63)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_063_vvh_basefill_062'] = {'inputs': ['vvh_base_universe_d2_063_vvh_basefill_062'], 'func': vvh_base_universe_d3_063_vvh_basefill_062}


def vvh_base_universe_d3_064_vvh_basefill_063(vvh_base_universe_d2_064_vvh_basefill_063):
    return _base_universe_d3(vvh_base_universe_d2_064_vvh_basefill_063, 64)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_064_vvh_basefill_063'] = {'inputs': ['vvh_base_universe_d2_064_vvh_basefill_063'], 'func': vvh_base_universe_d3_064_vvh_basefill_063}


def vvh_base_universe_d3_065_vvh_basefill_065(vvh_base_universe_d2_065_vvh_basefill_065):
    return _base_universe_d3(vvh_base_universe_d2_065_vvh_basefill_065, 65)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_065_vvh_basefill_065'] = {'inputs': ['vvh_base_universe_d2_065_vvh_basefill_065'], 'func': vvh_base_universe_d3_065_vvh_basefill_065}


def vvh_base_universe_d3_066_vvh_basefill_066(vvh_base_universe_d2_066_vvh_basefill_066):
    return _base_universe_d3(vvh_base_universe_d2_066_vvh_basefill_066, 66)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_066_vvh_basefill_066'] = {'inputs': ['vvh_base_universe_d2_066_vvh_basefill_066'], 'func': vvh_base_universe_d3_066_vvh_basefill_066}


def vvh_base_universe_d3_067_vvh_basefill_068(vvh_base_universe_d2_067_vvh_basefill_068):
    return _base_universe_d3(vvh_base_universe_d2_067_vvh_basefill_068, 67)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_067_vvh_basefill_068'] = {'inputs': ['vvh_base_universe_d2_067_vvh_basefill_068'], 'func': vvh_base_universe_d3_067_vvh_basefill_068}


def vvh_base_universe_d3_068_vvh_basefill_070(vvh_base_universe_d2_068_vvh_basefill_070):
    return _base_universe_d3(vvh_base_universe_d2_068_vvh_basefill_070, 68)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_068_vvh_basefill_070'] = {'inputs': ['vvh_base_universe_d2_068_vvh_basefill_070'], 'func': vvh_base_universe_d3_068_vvh_basefill_070}


def vvh_base_universe_d3_069_vvh_basefill_073(vvh_base_universe_d2_069_vvh_basefill_073):
    return _base_universe_d3(vvh_base_universe_d2_069_vvh_basefill_073, 69)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_069_vvh_basefill_073'] = {'inputs': ['vvh_base_universe_d2_069_vvh_basefill_073'], 'func': vvh_base_universe_d3_069_vvh_basefill_073}


def vvh_base_universe_d3_070_vvh_basefill_074(vvh_base_universe_d2_070_vvh_basefill_074):
    return _base_universe_d3(vvh_base_universe_d2_070_vvh_basefill_074, 70)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_070_vvh_basefill_074'] = {'inputs': ['vvh_base_universe_d2_070_vvh_basefill_074'], 'func': vvh_base_universe_d3_070_vvh_basefill_074}


def vvh_base_universe_d3_071_vvh_basefill_075(vvh_base_universe_d2_071_vvh_basefill_075):
    return _base_universe_d3(vvh_base_universe_d2_071_vvh_basefill_075, 71)
VVH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvh_base_universe_d3_071_vvh_basefill_075'] = {'inputs': ['vvh_base_universe_d2_071_vvh_basefill_075'], 'func': vvh_base_universe_d3_071_vvh_basefill_075}
