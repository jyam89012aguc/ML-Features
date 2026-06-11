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



def vvp_176_vvp_001_pe_peer_discount_21_accel_1(vvp_151_vvp_001_pe_peer_discount_21_roc_1):
    feature = _s(vvp_151_vvp_001_pe_peer_discount_21_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def vvp_177_vvp_007_pe_peer_discount_252_accel_42(vvp_152_vvp_007_pe_peer_discount_252_roc_42):
    feature = _s(vvp_152_vvp_007_pe_peer_discount_252_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def vvp_178_vvp_013_pe_peer_discount_1512_accel_126(vvp_153_vvp_013_pe_peer_discount_1512_roc_126):
    feature = _s(vvp_153_vvp_013_pe_peer_discount_1512_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def vvp_179_vvp_019_pe_peer_discount_84_accel_378(vvp_154_vvp_019_pe_peer_discount_84_roc_378):
    feature = _s(vvp_154_vvp_019_pe_peer_discount_84_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)

def vvp_180_vvp_025_pe_peer_discount_756_accel_4(vvp_155_vvp_025_pe_peer_discount_756_roc_4):
    feature = _s(vvp_155_vvp_025_pe_peer_discount_756_roc_4)
    return (_roc(feature, 4).diff(1)).reindex(feature.index)






















VALUATION_VS_PEERS_REGISTRY_3RD_DERIVATIVES = {
    'vvp_176_vvp_001_pe_peer_discount_21_accel_1': {'inputs': ['vvp_151_vvp_001_pe_peer_discount_21_roc_1'], 'func': vvp_176_vvp_001_pe_peer_discount_21_accel_1},
    'vvp_177_vvp_007_pe_peer_discount_252_accel_42': {'inputs': ['vvp_152_vvp_007_pe_peer_discount_252_roc_42'], 'func': vvp_177_vvp_007_pe_peer_discount_252_accel_42},
    'vvp_178_vvp_013_pe_peer_discount_1512_accel_126': {'inputs': ['vvp_153_vvp_013_pe_peer_discount_1512_roc_126'], 'func': vvp_178_vvp_013_pe_peer_discount_1512_accel_126},
    'vvp_179_vvp_019_pe_peer_discount_84_accel_378': {'inputs': ['vvp_154_vvp_019_pe_peer_discount_84_roc_378'], 'func': vvp_179_vvp_019_pe_peer_discount_84_accel_378},
    'vvp_180_vvp_025_pe_peer_discount_756_accel_4': {'inputs': ['vvp_155_vvp_025_pe_peer_discount_756_roc_4'], 'func': vvp_180_vvp_025_pe_peer_discount_756_accel_4},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def vvp_replacement_d3_001(vvp_replacement_d2_001):
    feature = _clean(vvp_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_001'] = {'inputs': ['vvp_replacement_d2_001'], 'func': vvp_replacement_d3_001}


def vvp_replacement_d3_002(vvp_replacement_d2_002):
    feature = _clean(vvp_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_002'] = {'inputs': ['vvp_replacement_d2_002'], 'func': vvp_replacement_d3_002}


def vvp_replacement_d3_003(vvp_replacement_d2_003):
    feature = _clean(vvp_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_003'] = {'inputs': ['vvp_replacement_d2_003'], 'func': vvp_replacement_d3_003}


def vvp_replacement_d3_004(vvp_replacement_d2_004):
    feature = _clean(vvp_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_004'] = {'inputs': ['vvp_replacement_d2_004'], 'func': vvp_replacement_d3_004}


def vvp_replacement_d3_005(vvp_replacement_d2_005):
    feature = _clean(vvp_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_005'] = {'inputs': ['vvp_replacement_d2_005'], 'func': vvp_replacement_d3_005}


def vvp_replacement_d3_006(vvp_replacement_d2_006):
    feature = _clean(vvp_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_006'] = {'inputs': ['vvp_replacement_d2_006'], 'func': vvp_replacement_d3_006}


def vvp_replacement_d3_007(vvp_replacement_d2_007):
    feature = _clean(vvp_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_007'] = {'inputs': ['vvp_replacement_d2_007'], 'func': vvp_replacement_d3_007}


def vvp_replacement_d3_008(vvp_replacement_d2_008):
    feature = _clean(vvp_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_008'] = {'inputs': ['vvp_replacement_d2_008'], 'func': vvp_replacement_d3_008}


def vvp_replacement_d3_009(vvp_replacement_d2_009):
    feature = _clean(vvp_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_009'] = {'inputs': ['vvp_replacement_d2_009'], 'func': vvp_replacement_d3_009}


def vvp_replacement_d3_010(vvp_replacement_d2_010):
    feature = _clean(vvp_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_010'] = {'inputs': ['vvp_replacement_d2_010'], 'func': vvp_replacement_d3_010}


def vvp_replacement_d3_011(vvp_replacement_d2_011):
    feature = _clean(vvp_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_011'] = {'inputs': ['vvp_replacement_d2_011'], 'func': vvp_replacement_d3_011}


def vvp_replacement_d3_012(vvp_replacement_d2_012):
    feature = _clean(vvp_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_012'] = {'inputs': ['vvp_replacement_d2_012'], 'func': vvp_replacement_d3_012}


def vvp_replacement_d3_013(vvp_replacement_d2_013):
    feature = _clean(vvp_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_013'] = {'inputs': ['vvp_replacement_d2_013'], 'func': vvp_replacement_d3_013}


def vvp_replacement_d3_014(vvp_replacement_d2_014):
    feature = _clean(vvp_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_014'] = {'inputs': ['vvp_replacement_d2_014'], 'func': vvp_replacement_d3_014}


def vvp_replacement_d3_015(vvp_replacement_d2_015):
    feature = _clean(vvp_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_015'] = {'inputs': ['vvp_replacement_d2_015'], 'func': vvp_replacement_d3_015}


def vvp_replacement_d3_016(vvp_replacement_d2_016):
    feature = _clean(vvp_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_016'] = {'inputs': ['vvp_replacement_d2_016'], 'func': vvp_replacement_d3_016}


def vvp_replacement_d3_017(vvp_replacement_d2_017):
    feature = _clean(vvp_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_017'] = {'inputs': ['vvp_replacement_d2_017'], 'func': vvp_replacement_d3_017}


def vvp_replacement_d3_018(vvp_replacement_d2_018):
    feature = _clean(vvp_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_018'] = {'inputs': ['vvp_replacement_d2_018'], 'func': vvp_replacement_d3_018}


def vvp_replacement_d3_019(vvp_replacement_d2_019):
    feature = _clean(vvp_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_019'] = {'inputs': ['vvp_replacement_d2_019'], 'func': vvp_replacement_d3_019}


def vvp_replacement_d3_020(vvp_replacement_d2_020):
    feature = _clean(vvp_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_020'] = {'inputs': ['vvp_replacement_d2_020'], 'func': vvp_replacement_d3_020}


def vvp_replacement_d3_021(vvp_replacement_d2_021):
    feature = _clean(vvp_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_021'] = {'inputs': ['vvp_replacement_d2_021'], 'func': vvp_replacement_d3_021}


def vvp_replacement_d3_022(vvp_replacement_d2_022):
    feature = _clean(vvp_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_022'] = {'inputs': ['vvp_replacement_d2_022'], 'func': vvp_replacement_d3_022}


def vvp_replacement_d3_023(vvp_replacement_d2_023):
    feature = _clean(vvp_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_023'] = {'inputs': ['vvp_replacement_d2_023'], 'func': vvp_replacement_d3_023}


def vvp_replacement_d3_024(vvp_replacement_d2_024):
    feature = _clean(vvp_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_024'] = {'inputs': ['vvp_replacement_d2_024'], 'func': vvp_replacement_d3_024}


def vvp_replacement_d3_025(vvp_replacement_d2_025):
    feature = _clean(vvp_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_025'] = {'inputs': ['vvp_replacement_d2_025'], 'func': vvp_replacement_d3_025}


def vvp_replacement_d3_026(vvp_replacement_d2_026):
    feature = _clean(vvp_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_026'] = {'inputs': ['vvp_replacement_d2_026'], 'func': vvp_replacement_d3_026}


def vvp_replacement_d3_027(vvp_replacement_d2_027):
    feature = _clean(vvp_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_027'] = {'inputs': ['vvp_replacement_d2_027'], 'func': vvp_replacement_d3_027}


def vvp_replacement_d3_028(vvp_replacement_d2_028):
    feature = _clean(vvp_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_028'] = {'inputs': ['vvp_replacement_d2_028'], 'func': vvp_replacement_d3_028}


def vvp_replacement_d3_029(vvp_replacement_d2_029):
    feature = _clean(vvp_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_029'] = {'inputs': ['vvp_replacement_d2_029'], 'func': vvp_replacement_d3_029}


def vvp_replacement_d3_030(vvp_replacement_d2_030):
    feature = _clean(vvp_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_030'] = {'inputs': ['vvp_replacement_d2_030'], 'func': vvp_replacement_d3_030}


def vvp_replacement_d3_031(vvp_replacement_d2_031):
    feature = _clean(vvp_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_031'] = {'inputs': ['vvp_replacement_d2_031'], 'func': vvp_replacement_d3_031}


def vvp_replacement_d3_032(vvp_replacement_d2_032):
    feature = _clean(vvp_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_032'] = {'inputs': ['vvp_replacement_d2_032'], 'func': vvp_replacement_d3_032}


def vvp_replacement_d3_033(vvp_replacement_d2_033):
    feature = _clean(vvp_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_033'] = {'inputs': ['vvp_replacement_d2_033'], 'func': vvp_replacement_d3_033}


def vvp_replacement_d3_034(vvp_replacement_d2_034):
    feature = _clean(vvp_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_034'] = {'inputs': ['vvp_replacement_d2_034'], 'func': vvp_replacement_d3_034}


def vvp_replacement_d3_035(vvp_replacement_d2_035):
    feature = _clean(vvp_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_035'] = {'inputs': ['vvp_replacement_d2_035'], 'func': vvp_replacement_d3_035}


def vvp_replacement_d3_036(vvp_replacement_d2_036):
    feature = _clean(vvp_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_036'] = {'inputs': ['vvp_replacement_d2_036'], 'func': vvp_replacement_d3_036}


def vvp_replacement_d3_037(vvp_replacement_d2_037):
    feature = _clean(vvp_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_037'] = {'inputs': ['vvp_replacement_d2_037'], 'func': vvp_replacement_d3_037}


def vvp_replacement_d3_038(vvp_replacement_d2_038):
    feature = _clean(vvp_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_038'] = {'inputs': ['vvp_replacement_d2_038'], 'func': vvp_replacement_d3_038}


def vvp_replacement_d3_039(vvp_replacement_d2_039):
    feature = _clean(vvp_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_039'] = {'inputs': ['vvp_replacement_d2_039'], 'func': vvp_replacement_d3_039}


def vvp_replacement_d3_040(vvp_replacement_d2_040):
    feature = _clean(vvp_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_040'] = {'inputs': ['vvp_replacement_d2_040'], 'func': vvp_replacement_d3_040}


def vvp_replacement_d3_041(vvp_replacement_d2_041):
    feature = _clean(vvp_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_041'] = {'inputs': ['vvp_replacement_d2_041'], 'func': vvp_replacement_d3_041}


def vvp_replacement_d3_042(vvp_replacement_d2_042):
    feature = _clean(vvp_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_042'] = {'inputs': ['vvp_replacement_d2_042'], 'func': vvp_replacement_d3_042}


def vvp_replacement_d3_043(vvp_replacement_d2_043):
    feature = _clean(vvp_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_043'] = {'inputs': ['vvp_replacement_d2_043'], 'func': vvp_replacement_d3_043}


def vvp_replacement_d3_044(vvp_replacement_d2_044):
    feature = _clean(vvp_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_044'] = {'inputs': ['vvp_replacement_d2_044'], 'func': vvp_replacement_d3_044}


def vvp_replacement_d3_045(vvp_replacement_d2_045):
    feature = _clean(vvp_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_045'] = {'inputs': ['vvp_replacement_d2_045'], 'func': vvp_replacement_d3_045}


def vvp_replacement_d3_046(vvp_replacement_d2_046):
    feature = _clean(vvp_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_046'] = {'inputs': ['vvp_replacement_d2_046'], 'func': vvp_replacement_d3_046}


def vvp_replacement_d3_047(vvp_replacement_d2_047):
    feature = _clean(vvp_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_047'] = {'inputs': ['vvp_replacement_d2_047'], 'func': vvp_replacement_d3_047}


def vvp_replacement_d3_048(vvp_replacement_d2_048):
    feature = _clean(vvp_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_048'] = {'inputs': ['vvp_replacement_d2_048'], 'func': vvp_replacement_d3_048}


def vvp_replacement_d3_049(vvp_replacement_d2_049):
    feature = _clean(vvp_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_049'] = {'inputs': ['vvp_replacement_d2_049'], 'func': vvp_replacement_d3_049}


def vvp_replacement_d3_050(vvp_replacement_d2_050):
    feature = _clean(vvp_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_050'] = {'inputs': ['vvp_replacement_d2_050'], 'func': vvp_replacement_d3_050}


def vvp_replacement_d3_051(vvp_replacement_d2_051):
    feature = _clean(vvp_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_051'] = {'inputs': ['vvp_replacement_d2_051'], 'func': vvp_replacement_d3_051}


def vvp_replacement_d3_052(vvp_replacement_d2_052):
    feature = _clean(vvp_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_052'] = {'inputs': ['vvp_replacement_d2_052'], 'func': vvp_replacement_d3_052}


def vvp_replacement_d3_053(vvp_replacement_d2_053):
    feature = _clean(vvp_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_053'] = {'inputs': ['vvp_replacement_d2_053'], 'func': vvp_replacement_d3_053}


def vvp_replacement_d3_054(vvp_replacement_d2_054):
    feature = _clean(vvp_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_054'] = {'inputs': ['vvp_replacement_d2_054'], 'func': vvp_replacement_d3_054}


def vvp_replacement_d3_055(vvp_replacement_d2_055):
    feature = _clean(vvp_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_055'] = {'inputs': ['vvp_replacement_d2_055'], 'func': vvp_replacement_d3_055}


def vvp_replacement_d3_056(vvp_replacement_d2_056):
    feature = _clean(vvp_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_056'] = {'inputs': ['vvp_replacement_d2_056'], 'func': vvp_replacement_d3_056}


def vvp_replacement_d3_057(vvp_replacement_d2_057):
    feature = _clean(vvp_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_057'] = {'inputs': ['vvp_replacement_d2_057'], 'func': vvp_replacement_d3_057}


def vvp_replacement_d3_058(vvp_replacement_d2_058):
    feature = _clean(vvp_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_058'] = {'inputs': ['vvp_replacement_d2_058'], 'func': vvp_replacement_d3_058}


def vvp_replacement_d3_059(vvp_replacement_d2_059):
    feature = _clean(vvp_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_059'] = {'inputs': ['vvp_replacement_d2_059'], 'func': vvp_replacement_d3_059}


def vvp_replacement_d3_060(vvp_replacement_d2_060):
    feature = _clean(vvp_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_060'] = {'inputs': ['vvp_replacement_d2_060'], 'func': vvp_replacement_d3_060}


def vvp_replacement_d3_061(vvp_replacement_d2_061):
    feature = _clean(vvp_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_061'] = {'inputs': ['vvp_replacement_d2_061'], 'func': vvp_replacement_d3_061}


def vvp_replacement_d3_062(vvp_replacement_d2_062):
    feature = _clean(vvp_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_062'] = {'inputs': ['vvp_replacement_d2_062'], 'func': vvp_replacement_d3_062}


def vvp_replacement_d3_063(vvp_replacement_d2_063):
    feature = _clean(vvp_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_063'] = {'inputs': ['vvp_replacement_d2_063'], 'func': vvp_replacement_d3_063}


def vvp_replacement_d3_064(vvp_replacement_d2_064):
    feature = _clean(vvp_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_064'] = {'inputs': ['vvp_replacement_d2_064'], 'func': vvp_replacement_d3_064}


def vvp_replacement_d3_065(vvp_replacement_d2_065):
    feature = _clean(vvp_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_065'] = {'inputs': ['vvp_replacement_d2_065'], 'func': vvp_replacement_d3_065}


def vvp_replacement_d3_066(vvp_replacement_d2_066):
    feature = _clean(vvp_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_066'] = {'inputs': ['vvp_replacement_d2_066'], 'func': vvp_replacement_d3_066}


def vvp_replacement_d3_067(vvp_replacement_d2_067):
    feature = _clean(vvp_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_067'] = {'inputs': ['vvp_replacement_d2_067'], 'func': vvp_replacement_d3_067}


def vvp_replacement_d3_068(vvp_replacement_d2_068):
    feature = _clean(vvp_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_068'] = {'inputs': ['vvp_replacement_d2_068'], 'func': vvp_replacement_d3_068}


def vvp_replacement_d3_069(vvp_replacement_d2_069):
    feature = _clean(vvp_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_069'] = {'inputs': ['vvp_replacement_d2_069'], 'func': vvp_replacement_d3_069}


def vvp_replacement_d3_070(vvp_replacement_d2_070):
    feature = _clean(vvp_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_070'] = {'inputs': ['vvp_replacement_d2_070'], 'func': vvp_replacement_d3_070}


def vvp_replacement_d3_071(vvp_replacement_d2_071):
    feature = _clean(vvp_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_071'] = {'inputs': ['vvp_replacement_d2_071'], 'func': vvp_replacement_d3_071}


def vvp_replacement_d3_072(vvp_replacement_d2_072):
    feature = _clean(vvp_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_072'] = {'inputs': ['vvp_replacement_d2_072'], 'func': vvp_replacement_d3_072}


def vvp_replacement_d3_073(vvp_replacement_d2_073):
    feature = _clean(vvp_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_073'] = {'inputs': ['vvp_replacement_d2_073'], 'func': vvp_replacement_d3_073}


def vvp_replacement_d3_074(vvp_replacement_d2_074):
    feature = _clean(vvp_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_074'] = {'inputs': ['vvp_replacement_d2_074'], 'func': vvp_replacement_d3_074}


def vvp_replacement_d3_075(vvp_replacement_d2_075):
    feature = _clean(vvp_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_075'] = {'inputs': ['vvp_replacement_d2_075'], 'func': vvp_replacement_d3_075}


def vvp_replacement_d3_076(vvp_replacement_d2_076):
    feature = _clean(vvp_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_076'] = {'inputs': ['vvp_replacement_d2_076'], 'func': vvp_replacement_d3_076}


def vvp_replacement_d3_077(vvp_replacement_d2_077):
    feature = _clean(vvp_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_077'] = {'inputs': ['vvp_replacement_d2_077'], 'func': vvp_replacement_d3_077}


def vvp_replacement_d3_078(vvp_replacement_d2_078):
    feature = _clean(vvp_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_078'] = {'inputs': ['vvp_replacement_d2_078'], 'func': vvp_replacement_d3_078}


def vvp_replacement_d3_079(vvp_replacement_d2_079):
    feature = _clean(vvp_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_079'] = {'inputs': ['vvp_replacement_d2_079'], 'func': vvp_replacement_d3_079}


def vvp_replacement_d3_080(vvp_replacement_d2_080):
    feature = _clean(vvp_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_080'] = {'inputs': ['vvp_replacement_d2_080'], 'func': vvp_replacement_d3_080}


def vvp_replacement_d3_081(vvp_replacement_d2_081):
    feature = _clean(vvp_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_081'] = {'inputs': ['vvp_replacement_d2_081'], 'func': vvp_replacement_d3_081}


def vvp_replacement_d3_082(vvp_replacement_d2_082):
    feature = _clean(vvp_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_082'] = {'inputs': ['vvp_replacement_d2_082'], 'func': vvp_replacement_d3_082}


def vvp_replacement_d3_083(vvp_replacement_d2_083):
    feature = _clean(vvp_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_083'] = {'inputs': ['vvp_replacement_d2_083'], 'func': vvp_replacement_d3_083}


def vvp_replacement_d3_084(vvp_replacement_d2_084):
    feature = _clean(vvp_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_084'] = {'inputs': ['vvp_replacement_d2_084'], 'func': vvp_replacement_d3_084}


def vvp_replacement_d3_085(vvp_replacement_d2_085):
    feature = _clean(vvp_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_085'] = {'inputs': ['vvp_replacement_d2_085'], 'func': vvp_replacement_d3_085}


def vvp_replacement_d3_086(vvp_replacement_d2_086):
    feature = _clean(vvp_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_086'] = {'inputs': ['vvp_replacement_d2_086'], 'func': vvp_replacement_d3_086}


def vvp_replacement_d3_087(vvp_replacement_d2_087):
    feature = _clean(vvp_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_087'] = {'inputs': ['vvp_replacement_d2_087'], 'func': vvp_replacement_d3_087}


def vvp_replacement_d3_088(vvp_replacement_d2_088):
    feature = _clean(vvp_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_088'] = {'inputs': ['vvp_replacement_d2_088'], 'func': vvp_replacement_d3_088}


def vvp_replacement_d3_089(vvp_replacement_d2_089):
    feature = _clean(vvp_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_089'] = {'inputs': ['vvp_replacement_d2_089'], 'func': vvp_replacement_d3_089}


def vvp_replacement_d3_090(vvp_replacement_d2_090):
    feature = _clean(vvp_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_090'] = {'inputs': ['vvp_replacement_d2_090'], 'func': vvp_replacement_d3_090}


def vvp_replacement_d3_091(vvp_replacement_d2_091):
    feature = _clean(vvp_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_091'] = {'inputs': ['vvp_replacement_d2_091'], 'func': vvp_replacement_d3_091}


def vvp_replacement_d3_092(vvp_replacement_d2_092):
    feature = _clean(vvp_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_092'] = {'inputs': ['vvp_replacement_d2_092'], 'func': vvp_replacement_d3_092}


def vvp_replacement_d3_093(vvp_replacement_d2_093):
    feature = _clean(vvp_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_093'] = {'inputs': ['vvp_replacement_d2_093'], 'func': vvp_replacement_d3_093}


def vvp_replacement_d3_094(vvp_replacement_d2_094):
    feature = _clean(vvp_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_094'] = {'inputs': ['vvp_replacement_d2_094'], 'func': vvp_replacement_d3_094}


def vvp_replacement_d3_095(vvp_replacement_d2_095):
    feature = _clean(vvp_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_095'] = {'inputs': ['vvp_replacement_d2_095'], 'func': vvp_replacement_d3_095}


def vvp_replacement_d3_096(vvp_replacement_d2_096):
    feature = _clean(vvp_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_096'] = {'inputs': ['vvp_replacement_d2_096'], 'func': vvp_replacement_d3_096}


def vvp_replacement_d3_097(vvp_replacement_d2_097):
    feature = _clean(vvp_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_097'] = {'inputs': ['vvp_replacement_d2_097'], 'func': vvp_replacement_d3_097}


def vvp_replacement_d3_098(vvp_replacement_d2_098):
    feature = _clean(vvp_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_098'] = {'inputs': ['vvp_replacement_d2_098'], 'func': vvp_replacement_d3_098}


def vvp_replacement_d3_099(vvp_replacement_d2_099):
    feature = _clean(vvp_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_099'] = {'inputs': ['vvp_replacement_d2_099'], 'func': vvp_replacement_d3_099}


def vvp_replacement_d3_100(vvp_replacement_d2_100):
    feature = _clean(vvp_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_100'] = {'inputs': ['vvp_replacement_d2_100'], 'func': vvp_replacement_d3_100}


def vvp_replacement_d3_101(vvp_replacement_d2_101):
    feature = _clean(vvp_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_101'] = {'inputs': ['vvp_replacement_d2_101'], 'func': vvp_replacement_d3_101}


def vvp_replacement_d3_102(vvp_replacement_d2_102):
    feature = _clean(vvp_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_102'] = {'inputs': ['vvp_replacement_d2_102'], 'func': vvp_replacement_d3_102}


def vvp_replacement_d3_103(vvp_replacement_d2_103):
    feature = _clean(vvp_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_103'] = {'inputs': ['vvp_replacement_d2_103'], 'func': vvp_replacement_d3_103}


def vvp_replacement_d3_104(vvp_replacement_d2_104):
    feature = _clean(vvp_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_104'] = {'inputs': ['vvp_replacement_d2_104'], 'func': vvp_replacement_d3_104}


def vvp_replacement_d3_105(vvp_replacement_d2_105):
    feature = _clean(vvp_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_105'] = {'inputs': ['vvp_replacement_d2_105'], 'func': vvp_replacement_d3_105}


def vvp_replacement_d3_106(vvp_replacement_d2_106):
    feature = _clean(vvp_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_106'] = {'inputs': ['vvp_replacement_d2_106'], 'func': vvp_replacement_d3_106}


def vvp_replacement_d3_107(vvp_replacement_d2_107):
    feature = _clean(vvp_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_107'] = {'inputs': ['vvp_replacement_d2_107'], 'func': vvp_replacement_d3_107}


def vvp_replacement_d3_108(vvp_replacement_d2_108):
    feature = _clean(vvp_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_108'] = {'inputs': ['vvp_replacement_d2_108'], 'func': vvp_replacement_d3_108}


def vvp_replacement_d3_109(vvp_replacement_d2_109):
    feature = _clean(vvp_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_109'] = {'inputs': ['vvp_replacement_d2_109'], 'func': vvp_replacement_d3_109}


def vvp_replacement_d3_110(vvp_replacement_d2_110):
    feature = _clean(vvp_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_110'] = {'inputs': ['vvp_replacement_d2_110'], 'func': vvp_replacement_d3_110}


def vvp_replacement_d3_111(vvp_replacement_d2_111):
    feature = _clean(vvp_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_111'] = {'inputs': ['vvp_replacement_d2_111'], 'func': vvp_replacement_d3_111}


def vvp_replacement_d3_112(vvp_replacement_d2_112):
    feature = _clean(vvp_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_112'] = {'inputs': ['vvp_replacement_d2_112'], 'func': vvp_replacement_d3_112}


def vvp_replacement_d3_113(vvp_replacement_d2_113):
    feature = _clean(vvp_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_113'] = {'inputs': ['vvp_replacement_d2_113'], 'func': vvp_replacement_d3_113}


def vvp_replacement_d3_114(vvp_replacement_d2_114):
    feature = _clean(vvp_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_114'] = {'inputs': ['vvp_replacement_d2_114'], 'func': vvp_replacement_d3_114}


def vvp_replacement_d3_115(vvp_replacement_d2_115):
    feature = _clean(vvp_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_115'] = {'inputs': ['vvp_replacement_d2_115'], 'func': vvp_replacement_d3_115}


def vvp_replacement_d3_116(vvp_replacement_d2_116):
    feature = _clean(vvp_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_116'] = {'inputs': ['vvp_replacement_d2_116'], 'func': vvp_replacement_d3_116}


def vvp_replacement_d3_117(vvp_replacement_d2_117):
    feature = _clean(vvp_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_117'] = {'inputs': ['vvp_replacement_d2_117'], 'func': vvp_replacement_d3_117}


def vvp_replacement_d3_118(vvp_replacement_d2_118):
    feature = _clean(vvp_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_118'] = {'inputs': ['vvp_replacement_d2_118'], 'func': vvp_replacement_d3_118}


def vvp_replacement_d3_119(vvp_replacement_d2_119):
    feature = _clean(vvp_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_119'] = {'inputs': ['vvp_replacement_d2_119'], 'func': vvp_replacement_d3_119}


def vvp_replacement_d3_120(vvp_replacement_d2_120):
    feature = _clean(vvp_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_120'] = {'inputs': ['vvp_replacement_d2_120'], 'func': vvp_replacement_d3_120}


def vvp_replacement_d3_121(vvp_replacement_d2_121):
    feature = _clean(vvp_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_121'] = {'inputs': ['vvp_replacement_d2_121'], 'func': vvp_replacement_d3_121}


def vvp_replacement_d3_122(vvp_replacement_d2_122):
    feature = _clean(vvp_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_122'] = {'inputs': ['vvp_replacement_d2_122'], 'func': vvp_replacement_d3_122}


def vvp_replacement_d3_123(vvp_replacement_d2_123):
    feature = _clean(vvp_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_123'] = {'inputs': ['vvp_replacement_d2_123'], 'func': vvp_replacement_d3_123}


def vvp_replacement_d3_124(vvp_replacement_d2_124):
    feature = _clean(vvp_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_124'] = {'inputs': ['vvp_replacement_d2_124'], 'func': vvp_replacement_d3_124}


def vvp_replacement_d3_125(vvp_replacement_d2_125):
    feature = _clean(vvp_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_125'] = {'inputs': ['vvp_replacement_d2_125'], 'func': vvp_replacement_d3_125}


def vvp_replacement_d3_126(vvp_replacement_d2_126):
    feature = _clean(vvp_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_126'] = {'inputs': ['vvp_replacement_d2_126'], 'func': vvp_replacement_d3_126}


def vvp_replacement_d3_127(vvp_replacement_d2_127):
    feature = _clean(vvp_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_127'] = {'inputs': ['vvp_replacement_d2_127'], 'func': vvp_replacement_d3_127}


def vvp_replacement_d3_128(vvp_replacement_d2_128):
    feature = _clean(vvp_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_128'] = {'inputs': ['vvp_replacement_d2_128'], 'func': vvp_replacement_d3_128}


def vvp_replacement_d3_129(vvp_replacement_d2_129):
    feature = _clean(vvp_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_129'] = {'inputs': ['vvp_replacement_d2_129'], 'func': vvp_replacement_d3_129}


def vvp_replacement_d3_130(vvp_replacement_d2_130):
    feature = _clean(vvp_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_130'] = {'inputs': ['vvp_replacement_d2_130'], 'func': vvp_replacement_d3_130}


def vvp_replacement_d3_131(vvp_replacement_d2_131):
    feature = _clean(vvp_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_131'] = {'inputs': ['vvp_replacement_d2_131'], 'func': vvp_replacement_d3_131}


def vvp_replacement_d3_132(vvp_replacement_d2_132):
    feature = _clean(vvp_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_132'] = {'inputs': ['vvp_replacement_d2_132'], 'func': vvp_replacement_d3_132}


def vvp_replacement_d3_133(vvp_replacement_d2_133):
    feature = _clean(vvp_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_133'] = {'inputs': ['vvp_replacement_d2_133'], 'func': vvp_replacement_d3_133}


def vvp_replacement_d3_134(vvp_replacement_d2_134):
    feature = _clean(vvp_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_134'] = {'inputs': ['vvp_replacement_d2_134'], 'func': vvp_replacement_d3_134}


def vvp_replacement_d3_135(vvp_replacement_d2_135):
    feature = _clean(vvp_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_135'] = {'inputs': ['vvp_replacement_d2_135'], 'func': vvp_replacement_d3_135}


def vvp_replacement_d3_136(vvp_replacement_d2_136):
    feature = _clean(vvp_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_136'] = {'inputs': ['vvp_replacement_d2_136'], 'func': vvp_replacement_d3_136}


def vvp_replacement_d3_137(vvp_replacement_d2_137):
    feature = _clean(vvp_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_137'] = {'inputs': ['vvp_replacement_d2_137'], 'func': vvp_replacement_d3_137}


def vvp_replacement_d3_138(vvp_replacement_d2_138):
    feature = _clean(vvp_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_138'] = {'inputs': ['vvp_replacement_d2_138'], 'func': vvp_replacement_d3_138}


def vvp_replacement_d3_139(vvp_replacement_d2_139):
    feature = _clean(vvp_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_139'] = {'inputs': ['vvp_replacement_d2_139'], 'func': vvp_replacement_d3_139}


def vvp_replacement_d3_140(vvp_replacement_d2_140):
    feature = _clean(vvp_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_140'] = {'inputs': ['vvp_replacement_d2_140'], 'func': vvp_replacement_d3_140}


def vvp_replacement_d3_141(vvp_replacement_d2_141):
    feature = _clean(vvp_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_141'] = {'inputs': ['vvp_replacement_d2_141'], 'func': vvp_replacement_d3_141}


def vvp_replacement_d3_142(vvp_replacement_d2_142):
    feature = _clean(vvp_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_142'] = {'inputs': ['vvp_replacement_d2_142'], 'func': vvp_replacement_d3_142}


def vvp_replacement_d3_143(vvp_replacement_d2_143):
    feature = _clean(vvp_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_143'] = {'inputs': ['vvp_replacement_d2_143'], 'func': vvp_replacement_d3_143}


def vvp_replacement_d3_144(vvp_replacement_d2_144):
    feature = _clean(vvp_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_144'] = {'inputs': ['vvp_replacement_d2_144'], 'func': vvp_replacement_d3_144}


def vvp_replacement_d3_145(vvp_replacement_d2_145):
    feature = _clean(vvp_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_145'] = {'inputs': ['vvp_replacement_d2_145'], 'func': vvp_replacement_d3_145}


def vvp_replacement_d3_146(vvp_replacement_d2_146):
    feature = _clean(vvp_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_146'] = {'inputs': ['vvp_replacement_d2_146'], 'func': vvp_replacement_d3_146}


def vvp_replacement_d3_147(vvp_replacement_d2_147):
    feature = _clean(vvp_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_147'] = {'inputs': ['vvp_replacement_d2_147'], 'func': vvp_replacement_d3_147}


def vvp_replacement_d3_148(vvp_replacement_d2_148):
    feature = _clean(vvp_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_148'] = {'inputs': ['vvp_replacement_d2_148'], 'func': vvp_replacement_d3_148}


def vvp_replacement_d3_149(vvp_replacement_d2_149):
    feature = _clean(vvp_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_149'] = {'inputs': ['vvp_replacement_d2_149'], 'func': vvp_replacement_d3_149}


def vvp_replacement_d3_150(vvp_replacement_d2_150):
    feature = _clean(vvp_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_150'] = {'inputs': ['vvp_replacement_d2_150'], 'func': vvp_replacement_d3_150}


def vvp_replacement_d3_151(vvp_replacement_d2_151):
    feature = _clean(vvp_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_151'] = {'inputs': ['vvp_replacement_d2_151'], 'func': vvp_replacement_d3_151}


def vvp_replacement_d3_152(vvp_replacement_d2_152):
    feature = _clean(vvp_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_152'] = {'inputs': ['vvp_replacement_d2_152'], 'func': vvp_replacement_d3_152}


def vvp_replacement_d3_153(vvp_replacement_d2_153):
    feature = _clean(vvp_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_153'] = {'inputs': ['vvp_replacement_d2_153'], 'func': vvp_replacement_d3_153}


def vvp_replacement_d3_154(vvp_replacement_d2_154):
    feature = _clean(vvp_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_154'] = {'inputs': ['vvp_replacement_d2_154'], 'func': vvp_replacement_d3_154}


def vvp_replacement_d3_155(vvp_replacement_d2_155):
    feature = _clean(vvp_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_155'] = {'inputs': ['vvp_replacement_d2_155'], 'func': vvp_replacement_d3_155}


def vvp_replacement_d3_156(vvp_replacement_d2_156):
    feature = _clean(vvp_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_156'] = {'inputs': ['vvp_replacement_d2_156'], 'func': vvp_replacement_d3_156}


def vvp_replacement_d3_157(vvp_replacement_d2_157):
    feature = _clean(vvp_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_157'] = {'inputs': ['vvp_replacement_d2_157'], 'func': vvp_replacement_d3_157}


def vvp_replacement_d3_158(vvp_replacement_d2_158):
    feature = _clean(vvp_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_158'] = {'inputs': ['vvp_replacement_d2_158'], 'func': vvp_replacement_d3_158}


def vvp_replacement_d3_159(vvp_replacement_d2_159):
    feature = _clean(vvp_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_159'] = {'inputs': ['vvp_replacement_d2_159'], 'func': vvp_replacement_d3_159}


def vvp_replacement_d3_160(vvp_replacement_d2_160):
    feature = _clean(vvp_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_160'] = {'inputs': ['vvp_replacement_d2_160'], 'func': vvp_replacement_d3_160}


def vvp_replacement_d3_161(vvp_replacement_d2_161):
    feature = _clean(vvp_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_161'] = {'inputs': ['vvp_replacement_d2_161'], 'func': vvp_replacement_d3_161}


def vvp_replacement_d3_162(vvp_replacement_d2_162):
    feature = _clean(vvp_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_162'] = {'inputs': ['vvp_replacement_d2_162'], 'func': vvp_replacement_d3_162}


def vvp_replacement_d3_163(vvp_replacement_d2_163):
    feature = _clean(vvp_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_163'] = {'inputs': ['vvp_replacement_d2_163'], 'func': vvp_replacement_d3_163}


def vvp_replacement_d3_164(vvp_replacement_d2_164):
    feature = _clean(vvp_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_164'] = {'inputs': ['vvp_replacement_d2_164'], 'func': vvp_replacement_d3_164}


def vvp_replacement_d3_165(vvp_replacement_d2_165):
    feature = _clean(vvp_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_165'] = {'inputs': ['vvp_replacement_d2_165'], 'func': vvp_replacement_d3_165}


def vvp_replacement_d3_166(vvp_replacement_d2_166):
    feature = _clean(vvp_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_166'] = {'inputs': ['vvp_replacement_d2_166'], 'func': vvp_replacement_d3_166}


def vvp_replacement_d3_167(vvp_replacement_d2_167):
    feature = _clean(vvp_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_167'] = {'inputs': ['vvp_replacement_d2_167'], 'func': vvp_replacement_d3_167}


def vvp_replacement_d3_168(vvp_replacement_d2_168):
    feature = _clean(vvp_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_168'] = {'inputs': ['vvp_replacement_d2_168'], 'func': vvp_replacement_d3_168}


def vvp_replacement_d3_169(vvp_replacement_d2_169):
    feature = _clean(vvp_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_169'] = {'inputs': ['vvp_replacement_d2_169'], 'func': vvp_replacement_d3_169}


def vvp_replacement_d3_170(vvp_replacement_d2_170):
    feature = _clean(vvp_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_170'] = {'inputs': ['vvp_replacement_d2_170'], 'func': vvp_replacement_d3_170}


def vvp_replacement_d3_171(vvp_replacement_d2_171):
    feature = _clean(vvp_replacement_d2_171)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_171'] = {'inputs': ['vvp_replacement_d2_171'], 'func': vvp_replacement_d3_171}


def vvp_replacement_d3_172(vvp_replacement_d2_172):
    feature = _clean(vvp_replacement_d2_172)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_172'] = {'inputs': ['vvp_replacement_d2_172'], 'func': vvp_replacement_d3_172}


def vvp_replacement_d3_173(vvp_replacement_d2_173):
    feature = _clean(vvp_replacement_d2_173)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_173'] = {'inputs': ['vvp_replacement_d2_173'], 'func': vvp_replacement_d3_173}


def vvp_replacement_d3_174(vvp_replacement_d2_174):
    feature = _clean(vvp_replacement_d2_174)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_174'] = {'inputs': ['vvp_replacement_d2_174'], 'func': vvp_replacement_d3_174}


def vvp_replacement_d3_175(vvp_replacement_d2_175):
    feature = _clean(vvp_replacement_d2_175)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_175'] = {'inputs': ['vvp_replacement_d2_175'], 'func': vvp_replacement_d3_175}


def vvp_replacement_d3_176(vvp_replacement_d2_176):
    feature = _clean(vvp_replacement_d2_176)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00088000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_176'] = {'inputs': ['vvp_replacement_d2_176'], 'func': vvp_replacement_d3_176}


def vvp_replacement_d3_177(vvp_replacement_d2_177):
    feature = _clean(vvp_replacement_d2_177)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00088500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_177'] = {'inputs': ['vvp_replacement_d2_177'], 'func': vvp_replacement_d3_177}


def vvp_replacement_d3_178(vvp_replacement_d2_178):
    feature = _clean(vvp_replacement_d2_178)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00089000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_178'] = {'inputs': ['vvp_replacement_d2_178'], 'func': vvp_replacement_d3_178}


def vvp_replacement_d3_179(vvp_replacement_d2_179):
    feature = _clean(vvp_replacement_d2_179)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00089500).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_179'] = {'inputs': ['vvp_replacement_d2_179'], 'func': vvp_replacement_d3_179}


def vvp_replacement_d3_180(vvp_replacement_d2_180):
    feature = _clean(vvp_replacement_d2_180)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00090000).reindex(feature.index)
VVP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vvp_replacement_d3_180'] = {'inputs': ['vvp_replacement_d2_180'], 'func': vvp_replacement_d3_180}


# Third-derivative extensions for repaired first-base features.
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def vvp_base_universe_d3_001_vvp_005_peer_relative_pe_z_126(vvp_base_universe_d2_001_vvp_005_peer_relative_pe_z_126):
    return _base_universe_d3(vvp_base_universe_d2_001_vvp_005_peer_relative_pe_z_126, 1)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_001_vvp_005_peer_relative_pe_z_126'] = {'inputs': ['vvp_base_universe_d2_001_vvp_005_peer_relative_pe_z_126'], 'func': vvp_base_universe_d3_001_vvp_005_peer_relative_pe_z_126}


def vvp_base_universe_d3_002_vvp_006_peer_relative_pb_z_189(vvp_base_universe_d2_002_vvp_006_peer_relative_pb_z_189):
    return _base_universe_d3(vvp_base_universe_d2_002_vvp_006_peer_relative_pb_z_189, 2)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_002_vvp_006_peer_relative_pb_z_189'] = {'inputs': ['vvp_base_universe_d2_002_vvp_006_peer_relative_pb_z_189'], 'func': vvp_base_universe_d3_002_vvp_006_peer_relative_pb_z_189}


def vvp_base_universe_d3_003_vvp_011_peer_relative_pe_z_1008(vvp_base_universe_d2_003_vvp_011_peer_relative_pe_z_1008):
    return _base_universe_d3(vvp_base_universe_d2_003_vvp_011_peer_relative_pe_z_1008, 3)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_003_vvp_011_peer_relative_pe_z_1008'] = {'inputs': ['vvp_base_universe_d2_003_vvp_011_peer_relative_pe_z_1008'], 'func': vvp_base_universe_d3_003_vvp_011_peer_relative_pe_z_1008}


def vvp_base_universe_d3_004_vvp_012_peer_relative_pb_z_1260(vvp_base_universe_d2_004_vvp_012_peer_relative_pb_z_1260):
    return _base_universe_d3(vvp_base_universe_d2_004_vvp_012_peer_relative_pb_z_1260, 4)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_004_vvp_012_peer_relative_pb_z_1260'] = {'inputs': ['vvp_base_universe_d2_004_vvp_012_peer_relative_pb_z_1260'], 'func': vvp_base_universe_d3_004_vvp_012_peer_relative_pb_z_1260}


def vvp_base_universe_d3_005_vvp_017_peer_relative_pe_z_42(vvp_base_universe_d2_005_vvp_017_peer_relative_pe_z_42):
    return _base_universe_d3(vvp_base_universe_d2_005_vvp_017_peer_relative_pe_z_42, 5)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_005_vvp_017_peer_relative_pe_z_42'] = {'inputs': ['vvp_base_universe_d2_005_vvp_017_peer_relative_pe_z_42'], 'func': vvp_base_universe_d3_005_vvp_017_peer_relative_pe_z_42}


def vvp_base_universe_d3_006_vvp_018_peer_relative_pb_z_63(vvp_base_universe_d2_006_vvp_018_peer_relative_pb_z_63):
    return _base_universe_d3(vvp_base_universe_d2_006_vvp_018_peer_relative_pb_z_63, 6)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_006_vvp_018_peer_relative_pb_z_63'] = {'inputs': ['vvp_base_universe_d2_006_vvp_018_peer_relative_pb_z_63'], 'func': vvp_base_universe_d3_006_vvp_018_peer_relative_pb_z_63}


def vvp_base_universe_d3_007_vvp_023_peer_relative_pe_z_378(vvp_base_universe_d2_007_vvp_023_peer_relative_pe_z_378):
    return _base_universe_d3(vvp_base_universe_d2_007_vvp_023_peer_relative_pe_z_378, 7)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_007_vvp_023_peer_relative_pe_z_378'] = {'inputs': ['vvp_base_universe_d2_007_vvp_023_peer_relative_pe_z_378'], 'func': vvp_base_universe_d3_007_vvp_023_peer_relative_pe_z_378}


def vvp_base_universe_d3_008_vvp_024_peer_relative_pb_z_504(vvp_base_universe_d2_008_vvp_024_peer_relative_pb_z_504):
    return _base_universe_d3(vvp_base_universe_d2_008_vvp_024_peer_relative_pb_z_504, 8)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_008_vvp_024_peer_relative_pb_z_504'] = {'inputs': ['vvp_base_universe_d2_008_vvp_024_peer_relative_pb_z_504'], 'func': vvp_base_universe_d3_008_vvp_024_peer_relative_pb_z_504}


def vvp_base_universe_d3_009_vvp_030_peer_relative_pb_z_252(vvp_base_universe_d2_009_vvp_030_peer_relative_pb_z_252):
    return _base_universe_d3(vvp_base_universe_d2_009_vvp_030_peer_relative_pb_z_252, 9)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_009_vvp_030_peer_relative_pb_z_252'] = {'inputs': ['vvp_base_universe_d2_009_vvp_030_peer_relative_pb_z_252'], 'func': vvp_base_universe_d3_009_vvp_030_peer_relative_pb_z_252}


def vvp_base_universe_d3_010_vvp_basefill_002(vvp_base_universe_d2_010_vvp_basefill_002):
    return _base_universe_d3(vvp_base_universe_d2_010_vvp_basefill_002, 10)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_010_vvp_basefill_002'] = {'inputs': ['vvp_base_universe_d2_010_vvp_basefill_002'], 'func': vvp_base_universe_d3_010_vvp_basefill_002}


def vvp_base_universe_d3_011_vvp_basefill_003(vvp_base_universe_d2_011_vvp_basefill_003):
    return _base_universe_d3(vvp_base_universe_d2_011_vvp_basefill_003, 11)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_011_vvp_basefill_003'] = {'inputs': ['vvp_base_universe_d2_011_vvp_basefill_003'], 'func': vvp_base_universe_d3_011_vvp_basefill_003}


def vvp_base_universe_d3_012_vvp_basefill_004(vvp_base_universe_d2_012_vvp_basefill_004):
    return _base_universe_d3(vvp_base_universe_d2_012_vvp_basefill_004, 12)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_012_vvp_basefill_004'] = {'inputs': ['vvp_base_universe_d2_012_vvp_basefill_004'], 'func': vvp_base_universe_d3_012_vvp_basefill_004}


def vvp_base_universe_d3_013_vvp_basefill_007(vvp_base_universe_d2_013_vvp_basefill_007):
    return _base_universe_d3(vvp_base_universe_d2_013_vvp_basefill_007, 13)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_013_vvp_basefill_007'] = {'inputs': ['vvp_base_universe_d2_013_vvp_basefill_007'], 'func': vvp_base_universe_d3_013_vvp_basefill_007}


def vvp_base_universe_d3_014_vvp_basefill_008(vvp_base_universe_d2_014_vvp_basefill_008):
    return _base_universe_d3(vvp_base_universe_d2_014_vvp_basefill_008, 14)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_014_vvp_basefill_008'] = {'inputs': ['vvp_base_universe_d2_014_vvp_basefill_008'], 'func': vvp_base_universe_d3_014_vvp_basefill_008}


def vvp_base_universe_d3_015_vvp_basefill_009(vvp_base_universe_d2_015_vvp_basefill_009):
    return _base_universe_d3(vvp_base_universe_d2_015_vvp_basefill_009, 15)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_015_vvp_basefill_009'] = {'inputs': ['vvp_base_universe_d2_015_vvp_basefill_009'], 'func': vvp_base_universe_d3_015_vvp_basefill_009}


def vvp_base_universe_d3_016_vvp_basefill_010(vvp_base_universe_d2_016_vvp_basefill_010):
    return _base_universe_d3(vvp_base_universe_d2_016_vvp_basefill_010, 16)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_016_vvp_basefill_010'] = {'inputs': ['vvp_base_universe_d2_016_vvp_basefill_010'], 'func': vvp_base_universe_d3_016_vvp_basefill_010}


def vvp_base_universe_d3_017_vvp_basefill_013(vvp_base_universe_d2_017_vvp_basefill_013):
    return _base_universe_d3(vvp_base_universe_d2_017_vvp_basefill_013, 17)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_017_vvp_basefill_013'] = {'inputs': ['vvp_base_universe_d2_017_vvp_basefill_013'], 'func': vvp_base_universe_d3_017_vvp_basefill_013}


def vvp_base_universe_d3_018_vvp_basefill_014(vvp_base_universe_d2_018_vvp_basefill_014):
    return _base_universe_d3(vvp_base_universe_d2_018_vvp_basefill_014, 18)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_018_vvp_basefill_014'] = {'inputs': ['vvp_base_universe_d2_018_vvp_basefill_014'], 'func': vvp_base_universe_d3_018_vvp_basefill_014}


def vvp_base_universe_d3_019_vvp_basefill_015(vvp_base_universe_d2_019_vvp_basefill_015):
    return _base_universe_d3(vvp_base_universe_d2_019_vvp_basefill_015, 19)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_019_vvp_basefill_015'] = {'inputs': ['vvp_base_universe_d2_019_vvp_basefill_015'], 'func': vvp_base_universe_d3_019_vvp_basefill_015}


def vvp_base_universe_d3_020_vvp_basefill_016(vvp_base_universe_d2_020_vvp_basefill_016):
    return _base_universe_d3(vvp_base_universe_d2_020_vvp_basefill_016, 20)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_020_vvp_basefill_016'] = {'inputs': ['vvp_base_universe_d2_020_vvp_basefill_016'], 'func': vvp_base_universe_d3_020_vvp_basefill_016}


def vvp_base_universe_d3_021_vvp_basefill_019(vvp_base_universe_d2_021_vvp_basefill_019):
    return _base_universe_d3(vvp_base_universe_d2_021_vvp_basefill_019, 21)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_021_vvp_basefill_019'] = {'inputs': ['vvp_base_universe_d2_021_vvp_basefill_019'], 'func': vvp_base_universe_d3_021_vvp_basefill_019}


def vvp_base_universe_d3_022_vvp_basefill_020(vvp_base_universe_d2_022_vvp_basefill_020):
    return _base_universe_d3(vvp_base_universe_d2_022_vvp_basefill_020, 22)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_022_vvp_basefill_020'] = {'inputs': ['vvp_base_universe_d2_022_vvp_basefill_020'], 'func': vvp_base_universe_d3_022_vvp_basefill_020}


def vvp_base_universe_d3_023_vvp_basefill_021(vvp_base_universe_d2_023_vvp_basefill_021):
    return _base_universe_d3(vvp_base_universe_d2_023_vvp_basefill_021, 23)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_023_vvp_basefill_021'] = {'inputs': ['vvp_base_universe_d2_023_vvp_basefill_021'], 'func': vvp_base_universe_d3_023_vvp_basefill_021}


def vvp_base_universe_d3_024_vvp_basefill_022(vvp_base_universe_d2_024_vvp_basefill_022):
    return _base_universe_d3(vvp_base_universe_d2_024_vvp_basefill_022, 24)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_024_vvp_basefill_022'] = {'inputs': ['vvp_base_universe_d2_024_vvp_basefill_022'], 'func': vvp_base_universe_d3_024_vvp_basefill_022}


def vvp_base_universe_d3_025_vvp_basefill_025(vvp_base_universe_d2_025_vvp_basefill_025):
    return _base_universe_d3(vvp_base_universe_d2_025_vvp_basefill_025, 25)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_025_vvp_basefill_025'] = {'inputs': ['vvp_base_universe_d2_025_vvp_basefill_025'], 'func': vvp_base_universe_d3_025_vvp_basefill_025}


def vvp_base_universe_d3_026_vvp_basefill_026(vvp_base_universe_d2_026_vvp_basefill_026):
    return _base_universe_d3(vvp_base_universe_d2_026_vvp_basefill_026, 26)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_026_vvp_basefill_026'] = {'inputs': ['vvp_base_universe_d2_026_vvp_basefill_026'], 'func': vvp_base_universe_d3_026_vvp_basefill_026}


def vvp_base_universe_d3_027_vvp_basefill_027(vvp_base_universe_d2_027_vvp_basefill_027):
    return _base_universe_d3(vvp_base_universe_d2_027_vvp_basefill_027, 27)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_027_vvp_basefill_027'] = {'inputs': ['vvp_base_universe_d2_027_vvp_basefill_027'], 'func': vvp_base_universe_d3_027_vvp_basefill_027}


def vvp_base_universe_d3_028_vvp_basefill_028(vvp_base_universe_d2_028_vvp_basefill_028):
    return _base_universe_d3(vvp_base_universe_d2_028_vvp_basefill_028, 28)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_028_vvp_basefill_028'] = {'inputs': ['vvp_base_universe_d2_028_vvp_basefill_028'], 'func': vvp_base_universe_d3_028_vvp_basefill_028}


def vvp_base_universe_d3_029_vvp_basefill_029(vvp_base_universe_d2_029_vvp_basefill_029):
    return _base_universe_d3(vvp_base_universe_d2_029_vvp_basefill_029, 29)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_029_vvp_basefill_029'] = {'inputs': ['vvp_base_universe_d2_029_vvp_basefill_029'], 'func': vvp_base_universe_d3_029_vvp_basefill_029}


def vvp_base_universe_d3_030_vvp_basefill_031(vvp_base_universe_d2_030_vvp_basefill_031):
    return _base_universe_d3(vvp_base_universe_d2_030_vvp_basefill_031, 30)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_030_vvp_basefill_031'] = {'inputs': ['vvp_base_universe_d2_030_vvp_basefill_031'], 'func': vvp_base_universe_d3_030_vvp_basefill_031}


def vvp_base_universe_d3_031_vvp_basefill_032(vvp_base_universe_d2_031_vvp_basefill_032):
    return _base_universe_d3(vvp_base_universe_d2_031_vvp_basefill_032, 31)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_031_vvp_basefill_032'] = {'inputs': ['vvp_base_universe_d2_031_vvp_basefill_032'], 'func': vvp_base_universe_d3_031_vvp_basefill_032}


def vvp_base_universe_d3_032_vvp_basefill_033(vvp_base_universe_d2_032_vvp_basefill_033):
    return _base_universe_d3(vvp_base_universe_d2_032_vvp_basefill_033, 32)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_032_vvp_basefill_033'] = {'inputs': ['vvp_base_universe_d2_032_vvp_basefill_033'], 'func': vvp_base_universe_d3_032_vvp_basefill_033}


def vvp_base_universe_d3_033_vvp_basefill_034(vvp_base_universe_d2_033_vvp_basefill_034):
    return _base_universe_d3(vvp_base_universe_d2_033_vvp_basefill_034, 33)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_033_vvp_basefill_034'] = {'inputs': ['vvp_base_universe_d2_033_vvp_basefill_034'], 'func': vvp_base_universe_d3_033_vvp_basefill_034}


def vvp_base_universe_d3_034_vvp_basefill_035(vvp_base_universe_d2_034_vvp_basefill_035):
    return _base_universe_d3(vvp_base_universe_d2_034_vvp_basefill_035, 34)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_034_vvp_basefill_035'] = {'inputs': ['vvp_base_universe_d2_034_vvp_basefill_035'], 'func': vvp_base_universe_d3_034_vvp_basefill_035}


def vvp_base_universe_d3_035_vvp_basefill_036(vvp_base_universe_d2_035_vvp_basefill_036):
    return _base_universe_d3(vvp_base_universe_d2_035_vvp_basefill_036, 35)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_035_vvp_basefill_036'] = {'inputs': ['vvp_base_universe_d2_035_vvp_basefill_036'], 'func': vvp_base_universe_d3_035_vvp_basefill_036}


def vvp_base_universe_d3_036_vvp_basefill_037(vvp_base_universe_d2_036_vvp_basefill_037):
    return _base_universe_d3(vvp_base_universe_d2_036_vvp_basefill_037, 36)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_036_vvp_basefill_037'] = {'inputs': ['vvp_base_universe_d2_036_vvp_basefill_037'], 'func': vvp_base_universe_d3_036_vvp_basefill_037}


def vvp_base_universe_d3_037_vvp_basefill_038(vvp_base_universe_d2_037_vvp_basefill_038):
    return _base_universe_d3(vvp_base_universe_d2_037_vvp_basefill_038, 37)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_037_vvp_basefill_038'] = {'inputs': ['vvp_base_universe_d2_037_vvp_basefill_038'], 'func': vvp_base_universe_d3_037_vvp_basefill_038}


def vvp_base_universe_d3_038_vvp_basefill_039(vvp_base_universe_d2_038_vvp_basefill_039):
    return _base_universe_d3(vvp_base_universe_d2_038_vvp_basefill_039, 38)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_038_vvp_basefill_039'] = {'inputs': ['vvp_base_universe_d2_038_vvp_basefill_039'], 'func': vvp_base_universe_d3_038_vvp_basefill_039}


def vvp_base_universe_d3_039_vvp_basefill_040(vvp_base_universe_d2_039_vvp_basefill_040):
    return _base_universe_d3(vvp_base_universe_d2_039_vvp_basefill_040, 39)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_039_vvp_basefill_040'] = {'inputs': ['vvp_base_universe_d2_039_vvp_basefill_040'], 'func': vvp_base_universe_d3_039_vvp_basefill_040}


def vvp_base_universe_d3_040_vvp_basefill_041(vvp_base_universe_d2_040_vvp_basefill_041):
    return _base_universe_d3(vvp_base_universe_d2_040_vvp_basefill_041, 40)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_040_vvp_basefill_041'] = {'inputs': ['vvp_base_universe_d2_040_vvp_basefill_041'], 'func': vvp_base_universe_d3_040_vvp_basefill_041}


def vvp_base_universe_d3_041_vvp_basefill_042(vvp_base_universe_d2_041_vvp_basefill_042):
    return _base_universe_d3(vvp_base_universe_d2_041_vvp_basefill_042, 41)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_041_vvp_basefill_042'] = {'inputs': ['vvp_base_universe_d2_041_vvp_basefill_042'], 'func': vvp_base_universe_d3_041_vvp_basefill_042}


def vvp_base_universe_d3_042_vvp_basefill_043(vvp_base_universe_d2_042_vvp_basefill_043):
    return _base_universe_d3(vvp_base_universe_d2_042_vvp_basefill_043, 42)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_042_vvp_basefill_043'] = {'inputs': ['vvp_base_universe_d2_042_vvp_basefill_043'], 'func': vvp_base_universe_d3_042_vvp_basefill_043}


def vvp_base_universe_d3_043_vvp_basefill_044(vvp_base_universe_d2_043_vvp_basefill_044):
    return _base_universe_d3(vvp_base_universe_d2_043_vvp_basefill_044, 43)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_043_vvp_basefill_044'] = {'inputs': ['vvp_base_universe_d2_043_vvp_basefill_044'], 'func': vvp_base_universe_d3_043_vvp_basefill_044}


def vvp_base_universe_d3_044_vvp_basefill_045(vvp_base_universe_d2_044_vvp_basefill_045):
    return _base_universe_d3(vvp_base_universe_d2_044_vvp_basefill_045, 44)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_044_vvp_basefill_045'] = {'inputs': ['vvp_base_universe_d2_044_vvp_basefill_045'], 'func': vvp_base_universe_d3_044_vvp_basefill_045}


def vvp_base_universe_d3_045_vvp_basefill_046(vvp_base_universe_d2_045_vvp_basefill_046):
    return _base_universe_d3(vvp_base_universe_d2_045_vvp_basefill_046, 45)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_045_vvp_basefill_046'] = {'inputs': ['vvp_base_universe_d2_045_vvp_basefill_046'], 'func': vvp_base_universe_d3_045_vvp_basefill_046}


def vvp_base_universe_d3_046_vvp_basefill_047(vvp_base_universe_d2_046_vvp_basefill_047):
    return _base_universe_d3(vvp_base_universe_d2_046_vvp_basefill_047, 46)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_046_vvp_basefill_047'] = {'inputs': ['vvp_base_universe_d2_046_vvp_basefill_047'], 'func': vvp_base_universe_d3_046_vvp_basefill_047}


def vvp_base_universe_d3_047_vvp_basefill_048(vvp_base_universe_d2_047_vvp_basefill_048):
    return _base_universe_d3(vvp_base_universe_d2_047_vvp_basefill_048, 47)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_047_vvp_basefill_048'] = {'inputs': ['vvp_base_universe_d2_047_vvp_basefill_048'], 'func': vvp_base_universe_d3_047_vvp_basefill_048}


def vvp_base_universe_d3_048_vvp_basefill_049(vvp_base_universe_d2_048_vvp_basefill_049):
    return _base_universe_d3(vvp_base_universe_d2_048_vvp_basefill_049, 48)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_048_vvp_basefill_049'] = {'inputs': ['vvp_base_universe_d2_048_vvp_basefill_049'], 'func': vvp_base_universe_d3_048_vvp_basefill_049}


def vvp_base_universe_d3_049_vvp_basefill_050(vvp_base_universe_d2_049_vvp_basefill_050):
    return _base_universe_d3(vvp_base_universe_d2_049_vvp_basefill_050, 49)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_049_vvp_basefill_050'] = {'inputs': ['vvp_base_universe_d2_049_vvp_basefill_050'], 'func': vvp_base_universe_d3_049_vvp_basefill_050}


def vvp_base_universe_d3_050_vvp_basefill_051(vvp_base_universe_d2_050_vvp_basefill_051):
    return _base_universe_d3(vvp_base_universe_d2_050_vvp_basefill_051, 50)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_050_vvp_basefill_051'] = {'inputs': ['vvp_base_universe_d2_050_vvp_basefill_051'], 'func': vvp_base_universe_d3_050_vvp_basefill_051}


def vvp_base_universe_d3_051_vvp_basefill_052(vvp_base_universe_d2_051_vvp_basefill_052):
    return _base_universe_d3(vvp_base_universe_d2_051_vvp_basefill_052, 51)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_051_vvp_basefill_052'] = {'inputs': ['vvp_base_universe_d2_051_vvp_basefill_052'], 'func': vvp_base_universe_d3_051_vvp_basefill_052}


def vvp_base_universe_d3_052_vvp_basefill_053(vvp_base_universe_d2_052_vvp_basefill_053):
    return _base_universe_d3(vvp_base_universe_d2_052_vvp_basefill_053, 52)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_052_vvp_basefill_053'] = {'inputs': ['vvp_base_universe_d2_052_vvp_basefill_053'], 'func': vvp_base_universe_d3_052_vvp_basefill_053}


def vvp_base_universe_d3_053_vvp_basefill_054(vvp_base_universe_d2_053_vvp_basefill_054):
    return _base_universe_d3(vvp_base_universe_d2_053_vvp_basefill_054, 53)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_053_vvp_basefill_054'] = {'inputs': ['vvp_base_universe_d2_053_vvp_basefill_054'], 'func': vvp_base_universe_d3_053_vvp_basefill_054}


def vvp_base_universe_d3_054_vvp_basefill_055(vvp_base_universe_d2_054_vvp_basefill_055):
    return _base_universe_d3(vvp_base_universe_d2_054_vvp_basefill_055, 54)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_054_vvp_basefill_055'] = {'inputs': ['vvp_base_universe_d2_054_vvp_basefill_055'], 'func': vvp_base_universe_d3_054_vvp_basefill_055}


def vvp_base_universe_d3_055_vvp_basefill_056(vvp_base_universe_d2_055_vvp_basefill_056):
    return _base_universe_d3(vvp_base_universe_d2_055_vvp_basefill_056, 55)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_055_vvp_basefill_056'] = {'inputs': ['vvp_base_universe_d2_055_vvp_basefill_056'], 'func': vvp_base_universe_d3_055_vvp_basefill_056}


def vvp_base_universe_d3_056_vvp_basefill_057(vvp_base_universe_d2_056_vvp_basefill_057):
    return _base_universe_d3(vvp_base_universe_d2_056_vvp_basefill_057, 56)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_056_vvp_basefill_057'] = {'inputs': ['vvp_base_universe_d2_056_vvp_basefill_057'], 'func': vvp_base_universe_d3_056_vvp_basefill_057}


def vvp_base_universe_d3_057_vvp_basefill_058(vvp_base_universe_d2_057_vvp_basefill_058):
    return _base_universe_d3(vvp_base_universe_d2_057_vvp_basefill_058, 57)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_057_vvp_basefill_058'] = {'inputs': ['vvp_base_universe_d2_057_vvp_basefill_058'], 'func': vvp_base_universe_d3_057_vvp_basefill_058}


def vvp_base_universe_d3_058_vvp_basefill_059(vvp_base_universe_d2_058_vvp_basefill_059):
    return _base_universe_d3(vvp_base_universe_d2_058_vvp_basefill_059, 58)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_058_vvp_basefill_059'] = {'inputs': ['vvp_base_universe_d2_058_vvp_basefill_059'], 'func': vvp_base_universe_d3_058_vvp_basefill_059}


def vvp_base_universe_d3_059_vvp_basefill_060(vvp_base_universe_d2_059_vvp_basefill_060):
    return _base_universe_d3(vvp_base_universe_d2_059_vvp_basefill_060, 59)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_059_vvp_basefill_060'] = {'inputs': ['vvp_base_universe_d2_059_vvp_basefill_060'], 'func': vvp_base_universe_d3_059_vvp_basefill_060}


def vvp_base_universe_d3_060_vvp_basefill_061(vvp_base_universe_d2_060_vvp_basefill_061):
    return _base_universe_d3(vvp_base_universe_d2_060_vvp_basefill_061, 60)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_060_vvp_basefill_061'] = {'inputs': ['vvp_base_universe_d2_060_vvp_basefill_061'], 'func': vvp_base_universe_d3_060_vvp_basefill_061}


def vvp_base_universe_d3_061_vvp_basefill_062(vvp_base_universe_d2_061_vvp_basefill_062):
    return _base_universe_d3(vvp_base_universe_d2_061_vvp_basefill_062, 61)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_061_vvp_basefill_062'] = {'inputs': ['vvp_base_universe_d2_061_vvp_basefill_062'], 'func': vvp_base_universe_d3_061_vvp_basefill_062}


def vvp_base_universe_d3_062_vvp_basefill_063(vvp_base_universe_d2_062_vvp_basefill_063):
    return _base_universe_d3(vvp_base_universe_d2_062_vvp_basefill_063, 62)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_062_vvp_basefill_063'] = {'inputs': ['vvp_base_universe_d2_062_vvp_basefill_063'], 'func': vvp_base_universe_d3_062_vvp_basefill_063}


def vvp_base_universe_d3_063_vvp_basefill_064(vvp_base_universe_d2_063_vvp_basefill_064):
    return _base_universe_d3(vvp_base_universe_d2_063_vvp_basefill_064, 63)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_063_vvp_basefill_064'] = {'inputs': ['vvp_base_universe_d2_063_vvp_basefill_064'], 'func': vvp_base_universe_d3_063_vvp_basefill_064}


def vvp_base_universe_d3_064_vvp_basefill_065(vvp_base_universe_d2_064_vvp_basefill_065):
    return _base_universe_d3(vvp_base_universe_d2_064_vvp_basefill_065, 64)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_064_vvp_basefill_065'] = {'inputs': ['vvp_base_universe_d2_064_vvp_basefill_065'], 'func': vvp_base_universe_d3_064_vvp_basefill_065}


def vvp_base_universe_d3_065_vvp_basefill_066(vvp_base_universe_d2_065_vvp_basefill_066):
    return _base_universe_d3(vvp_base_universe_d2_065_vvp_basefill_066, 65)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_065_vvp_basefill_066'] = {'inputs': ['vvp_base_universe_d2_065_vvp_basefill_066'], 'func': vvp_base_universe_d3_065_vvp_basefill_066}


def vvp_base_universe_d3_066_vvp_basefill_067(vvp_base_universe_d2_066_vvp_basefill_067):
    return _base_universe_d3(vvp_base_universe_d2_066_vvp_basefill_067, 66)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_066_vvp_basefill_067'] = {'inputs': ['vvp_base_universe_d2_066_vvp_basefill_067'], 'func': vvp_base_universe_d3_066_vvp_basefill_067}


def vvp_base_universe_d3_067_vvp_basefill_068(vvp_base_universe_d2_067_vvp_basefill_068):
    return _base_universe_d3(vvp_base_universe_d2_067_vvp_basefill_068, 67)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_067_vvp_basefill_068'] = {'inputs': ['vvp_base_universe_d2_067_vvp_basefill_068'], 'func': vvp_base_universe_d3_067_vvp_basefill_068}


def vvp_base_universe_d3_068_vvp_basefill_069(vvp_base_universe_d2_068_vvp_basefill_069):
    return _base_universe_d3(vvp_base_universe_d2_068_vvp_basefill_069, 68)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_068_vvp_basefill_069'] = {'inputs': ['vvp_base_universe_d2_068_vvp_basefill_069'], 'func': vvp_base_universe_d3_068_vvp_basefill_069}


def vvp_base_universe_d3_069_vvp_basefill_070(vvp_base_universe_d2_069_vvp_basefill_070):
    return _base_universe_d3(vvp_base_universe_d2_069_vvp_basefill_070, 69)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_069_vvp_basefill_070'] = {'inputs': ['vvp_base_universe_d2_069_vvp_basefill_070'], 'func': vvp_base_universe_d3_069_vvp_basefill_070}


def vvp_base_universe_d3_070_vvp_basefill_071(vvp_base_universe_d2_070_vvp_basefill_071):
    return _base_universe_d3(vvp_base_universe_d2_070_vvp_basefill_071, 70)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_070_vvp_basefill_071'] = {'inputs': ['vvp_base_universe_d2_070_vvp_basefill_071'], 'func': vvp_base_universe_d3_070_vvp_basefill_071}


def vvp_base_universe_d3_071_vvp_basefill_072(vvp_base_universe_d2_071_vvp_basefill_072):
    return _base_universe_d3(vvp_base_universe_d2_071_vvp_basefill_072, 71)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_071_vvp_basefill_072'] = {'inputs': ['vvp_base_universe_d2_071_vvp_basefill_072'], 'func': vvp_base_universe_d3_071_vvp_basefill_072}


def vvp_base_universe_d3_072_vvp_basefill_073(vvp_base_universe_d2_072_vvp_basefill_073):
    return _base_universe_d3(vvp_base_universe_d2_072_vvp_basefill_073, 72)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_072_vvp_basefill_073'] = {'inputs': ['vvp_base_universe_d2_072_vvp_basefill_073'], 'func': vvp_base_universe_d3_072_vvp_basefill_073}


def vvp_base_universe_d3_073_vvp_basefill_074(vvp_base_universe_d2_073_vvp_basefill_074):
    return _base_universe_d3(vvp_base_universe_d2_073_vvp_basefill_074, 73)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_073_vvp_basefill_074'] = {'inputs': ['vvp_base_universe_d2_073_vvp_basefill_074'], 'func': vvp_base_universe_d3_073_vvp_basefill_074}


def vvp_base_universe_d3_074_vvp_basefill_075(vvp_base_universe_d2_074_vvp_basefill_075):
    return _base_universe_d3(vvp_base_universe_d2_074_vvp_basefill_075, 74)
VVP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vvp_base_universe_d3_074_vvp_basefill_075'] = {'inputs': ['vvp_base_universe_d2_074_vvp_basefill_075'], 'func': vvp_base_universe_d3_074_vvp_basefill_075}
