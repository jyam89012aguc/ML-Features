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



def vvp_151_vvp_001_pe_peer_discount_21_roc_1(vvp_001_pe_peer_discount_21):
    feature = _s(vvp_001_pe_peer_discount_21)
    return (_roc(feature, 1)).reindex(feature.index)

def vvp_152_vvp_007_pe_peer_discount_252_roc_42(vvp_007_pe_peer_discount_252):
    feature = _s(vvp_007_pe_peer_discount_252)
    return (_roc(feature, 42)).reindex(feature.index)

def vvp_153_vvp_013_pe_peer_discount_1512_roc_126(vvp_013_pe_peer_discount_1512):
    feature = _s(vvp_013_pe_peer_discount_1512)
    return (_roc(feature, 126)).reindex(feature.index)

def vvp_154_vvp_019_pe_peer_discount_84_roc_378(vvp_019_pe_peer_discount_84):
    feature = _s(vvp_019_pe_peer_discount_84)
    return (_roc(feature, 378)).reindex(feature.index)

def vvp_155_vvp_025_pe_peer_discount_756_roc_4(vvp_025_pe_peer_discount_756):
    feature = _s(vvp_025_pe_peer_discount_756)
    return (_roc(feature, 4)).reindex(feature.index)






















VALUATION_VS_PEERS_REGISTRY_2ND_DERIVATIVES = {
    'vvp_151_vvp_001_pe_peer_discount_21_roc_1': {'inputs': ['vvp_001_pe_peer_discount_21'], 'func': vvp_151_vvp_001_pe_peer_discount_21_roc_1},
    'vvp_152_vvp_007_pe_peer_discount_252_roc_42': {'inputs': ['vvp_007_pe_peer_discount_252'], 'func': vvp_152_vvp_007_pe_peer_discount_252_roc_42},
    'vvp_153_vvp_013_pe_peer_discount_1512_roc_126': {'inputs': ['vvp_013_pe_peer_discount_1512'], 'func': vvp_153_vvp_013_pe_peer_discount_1512_roc_126},
    'vvp_154_vvp_019_pe_peer_discount_84_roc_378': {'inputs': ['vvp_019_pe_peer_discount_84'], 'func': vvp_154_vvp_019_pe_peer_discount_84_roc_378},
    'vvp_155_vvp_025_pe_peer_discount_756_roc_4': {'inputs': ['vvp_025_pe_peer_discount_756'], 'func': vvp_155_vvp_025_pe_peer_discount_756_roc_4},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def vvp_replacement_d2_001(vvp_007_pe_peer_discount_252):
    feature = _clean(vvp_007_pe_peer_discount_252)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_001'] = {'inputs': ['vvp_007_pe_peer_discount_252'], 'func': vvp_replacement_d2_001}


def vvp_replacement_d2_002(vvp_013_pe_peer_discount_1512):
    feature = _clean(vvp_013_pe_peer_discount_1512)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_002'] = {'inputs': ['vvp_013_pe_peer_discount_1512'], 'func': vvp_replacement_d2_002}


def vvp_replacement_d2_003(vvp_019_pe_peer_discount_84):
    feature = _clean(vvp_019_pe_peer_discount_84)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_003'] = {'inputs': ['vvp_019_pe_peer_discount_84'], 'func': vvp_replacement_d2_003}


def vvp_replacement_d2_004(vvp_025_pe_peer_discount_756):
    feature = _clean(vvp_025_pe_peer_discount_756)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_004'] = {'inputs': ['vvp_025_pe_peer_discount_756'], 'func': vvp_replacement_d2_004}


def vvp_replacement_d2_005(vvp_replacement_001):
    feature = _clean(vvp_replacement_001)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_005'] = {'inputs': ['vvp_replacement_001'], 'func': vvp_replacement_d2_005}


def vvp_replacement_d2_006(vvp_replacement_002):
    feature = _clean(vvp_replacement_002)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_006'] = {'inputs': ['vvp_replacement_002'], 'func': vvp_replacement_d2_006}


def vvp_replacement_d2_007(vvp_replacement_003):
    feature = _clean(vvp_replacement_003)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_007'] = {'inputs': ['vvp_replacement_003'], 'func': vvp_replacement_d2_007}


def vvp_replacement_d2_008(vvp_replacement_004):
    feature = _clean(vvp_replacement_004)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_008'] = {'inputs': ['vvp_replacement_004'], 'func': vvp_replacement_d2_008}


def vvp_replacement_d2_009(vvp_replacement_005):
    feature = _clean(vvp_replacement_005)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_009'] = {'inputs': ['vvp_replacement_005'], 'func': vvp_replacement_d2_009}


def vvp_replacement_d2_010(vvp_replacement_006):
    feature = _clean(vvp_replacement_006)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_010'] = {'inputs': ['vvp_replacement_006'], 'func': vvp_replacement_d2_010}


def vvp_replacement_d2_011(vvp_replacement_007):
    feature = _clean(vvp_replacement_007)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_011'] = {'inputs': ['vvp_replacement_007'], 'func': vvp_replacement_d2_011}


def vvp_replacement_d2_012(vvp_replacement_008):
    feature = _clean(vvp_replacement_008)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_012'] = {'inputs': ['vvp_replacement_008'], 'func': vvp_replacement_d2_012}


def vvp_replacement_d2_013(vvp_replacement_009):
    feature = _clean(vvp_replacement_009)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_013'] = {'inputs': ['vvp_replacement_009'], 'func': vvp_replacement_d2_013}


def vvp_replacement_d2_014(vvp_replacement_010):
    feature = _clean(vvp_replacement_010)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_014'] = {'inputs': ['vvp_replacement_010'], 'func': vvp_replacement_d2_014}


def vvp_replacement_d2_015(vvp_replacement_011):
    feature = _clean(vvp_replacement_011)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_015'] = {'inputs': ['vvp_replacement_011'], 'func': vvp_replacement_d2_015}


def vvp_replacement_d2_016(vvp_replacement_012):
    feature = _clean(vvp_replacement_012)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_016'] = {'inputs': ['vvp_replacement_012'], 'func': vvp_replacement_d2_016}


def vvp_replacement_d2_017(vvp_replacement_013):
    feature = _clean(vvp_replacement_013)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_017'] = {'inputs': ['vvp_replacement_013'], 'func': vvp_replacement_d2_017}


def vvp_replacement_d2_018(vvp_replacement_014):
    feature = _clean(vvp_replacement_014)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_018'] = {'inputs': ['vvp_replacement_014'], 'func': vvp_replacement_d2_018}


def vvp_replacement_d2_019(vvp_replacement_015):
    feature = _clean(vvp_replacement_015)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_019'] = {'inputs': ['vvp_replacement_015'], 'func': vvp_replacement_d2_019}


def vvp_replacement_d2_020(vvp_replacement_016):
    feature = _clean(vvp_replacement_016)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_020'] = {'inputs': ['vvp_replacement_016'], 'func': vvp_replacement_d2_020}


def vvp_replacement_d2_021(vvp_replacement_017):
    feature = _clean(vvp_replacement_017)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_021'] = {'inputs': ['vvp_replacement_017'], 'func': vvp_replacement_d2_021}


def vvp_replacement_d2_022(vvp_replacement_018):
    feature = _clean(vvp_replacement_018)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_022'] = {'inputs': ['vvp_replacement_018'], 'func': vvp_replacement_d2_022}


def vvp_replacement_d2_023(vvp_replacement_019):
    feature = _clean(vvp_replacement_019)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_023'] = {'inputs': ['vvp_replacement_019'], 'func': vvp_replacement_d2_023}


def vvp_replacement_d2_024(vvp_replacement_020):
    feature = _clean(vvp_replacement_020)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_024'] = {'inputs': ['vvp_replacement_020'], 'func': vvp_replacement_d2_024}


def vvp_replacement_d2_025(vvp_replacement_021):
    feature = _clean(vvp_replacement_021)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_025'] = {'inputs': ['vvp_replacement_021'], 'func': vvp_replacement_d2_025}


def vvp_replacement_d2_026(vvp_replacement_022):
    feature = _clean(vvp_replacement_022)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_026'] = {'inputs': ['vvp_replacement_022'], 'func': vvp_replacement_d2_026}


def vvp_replacement_d2_027(vvp_replacement_023):
    feature = _clean(vvp_replacement_023)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_027'] = {'inputs': ['vvp_replacement_023'], 'func': vvp_replacement_d2_027}


def vvp_replacement_d2_028(vvp_replacement_024):
    feature = _clean(vvp_replacement_024)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_028'] = {'inputs': ['vvp_replacement_024'], 'func': vvp_replacement_d2_028}


def vvp_replacement_d2_029(vvp_replacement_025):
    feature = _clean(vvp_replacement_025)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_029'] = {'inputs': ['vvp_replacement_025'], 'func': vvp_replacement_d2_029}


def vvp_replacement_d2_030(vvp_replacement_026):
    feature = _clean(vvp_replacement_026)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_030'] = {'inputs': ['vvp_replacement_026'], 'func': vvp_replacement_d2_030}


def vvp_replacement_d2_031(vvp_replacement_027):
    feature = _clean(vvp_replacement_027)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_031'] = {'inputs': ['vvp_replacement_027'], 'func': vvp_replacement_d2_031}


def vvp_replacement_d2_032(vvp_replacement_028):
    feature = _clean(vvp_replacement_028)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_032'] = {'inputs': ['vvp_replacement_028'], 'func': vvp_replacement_d2_032}


def vvp_replacement_d2_033(vvp_replacement_029):
    feature = _clean(vvp_replacement_029)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_033'] = {'inputs': ['vvp_replacement_029'], 'func': vvp_replacement_d2_033}


def vvp_replacement_d2_034(vvp_replacement_030):
    feature = _clean(vvp_replacement_030)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_034'] = {'inputs': ['vvp_replacement_030'], 'func': vvp_replacement_d2_034}


def vvp_replacement_d2_035(vvp_replacement_031):
    feature = _clean(vvp_replacement_031)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_035'] = {'inputs': ['vvp_replacement_031'], 'func': vvp_replacement_d2_035}


def vvp_replacement_d2_036(vvp_replacement_032):
    feature = _clean(vvp_replacement_032)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_036'] = {'inputs': ['vvp_replacement_032'], 'func': vvp_replacement_d2_036}


def vvp_replacement_d2_037(vvp_replacement_033):
    feature = _clean(vvp_replacement_033)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_037'] = {'inputs': ['vvp_replacement_033'], 'func': vvp_replacement_d2_037}


def vvp_replacement_d2_038(vvp_replacement_034):
    feature = _clean(vvp_replacement_034)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_038'] = {'inputs': ['vvp_replacement_034'], 'func': vvp_replacement_d2_038}


def vvp_replacement_d2_039(vvp_replacement_035):
    feature = _clean(vvp_replacement_035)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_039'] = {'inputs': ['vvp_replacement_035'], 'func': vvp_replacement_d2_039}


def vvp_replacement_d2_040(vvp_replacement_036):
    feature = _clean(vvp_replacement_036)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_040'] = {'inputs': ['vvp_replacement_036'], 'func': vvp_replacement_d2_040}


def vvp_replacement_d2_041(vvp_replacement_037):
    feature = _clean(vvp_replacement_037)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_041'] = {'inputs': ['vvp_replacement_037'], 'func': vvp_replacement_d2_041}


def vvp_replacement_d2_042(vvp_replacement_038):
    feature = _clean(vvp_replacement_038)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_042'] = {'inputs': ['vvp_replacement_038'], 'func': vvp_replacement_d2_042}


def vvp_replacement_d2_043(vvp_replacement_039):
    feature = _clean(vvp_replacement_039)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_043'] = {'inputs': ['vvp_replacement_039'], 'func': vvp_replacement_d2_043}


def vvp_replacement_d2_044(vvp_replacement_040):
    feature = _clean(vvp_replacement_040)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_044'] = {'inputs': ['vvp_replacement_040'], 'func': vvp_replacement_d2_044}


def vvp_replacement_d2_045(vvp_replacement_041):
    feature = _clean(vvp_replacement_041)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_045'] = {'inputs': ['vvp_replacement_041'], 'func': vvp_replacement_d2_045}


def vvp_replacement_d2_046(vvp_replacement_042):
    feature = _clean(vvp_replacement_042)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_046'] = {'inputs': ['vvp_replacement_042'], 'func': vvp_replacement_d2_046}


def vvp_replacement_d2_047(vvp_replacement_043):
    feature = _clean(vvp_replacement_043)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_047'] = {'inputs': ['vvp_replacement_043'], 'func': vvp_replacement_d2_047}


def vvp_replacement_d2_048(vvp_replacement_044):
    feature = _clean(vvp_replacement_044)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_048'] = {'inputs': ['vvp_replacement_044'], 'func': vvp_replacement_d2_048}


def vvp_replacement_d2_049(vvp_replacement_045):
    feature = _clean(vvp_replacement_045)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_049'] = {'inputs': ['vvp_replacement_045'], 'func': vvp_replacement_d2_049}


def vvp_replacement_d2_050(vvp_replacement_046):
    feature = _clean(vvp_replacement_046)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_050'] = {'inputs': ['vvp_replacement_046'], 'func': vvp_replacement_d2_050}


def vvp_replacement_d2_051(vvp_replacement_047):
    feature = _clean(vvp_replacement_047)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_051'] = {'inputs': ['vvp_replacement_047'], 'func': vvp_replacement_d2_051}


def vvp_replacement_d2_052(vvp_replacement_048):
    feature = _clean(vvp_replacement_048)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_052'] = {'inputs': ['vvp_replacement_048'], 'func': vvp_replacement_d2_052}


def vvp_replacement_d2_053(vvp_replacement_049):
    feature = _clean(vvp_replacement_049)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_053'] = {'inputs': ['vvp_replacement_049'], 'func': vvp_replacement_d2_053}


def vvp_replacement_d2_054(vvp_replacement_050):
    feature = _clean(vvp_replacement_050)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_054'] = {'inputs': ['vvp_replacement_050'], 'func': vvp_replacement_d2_054}


def vvp_replacement_d2_055(vvp_replacement_051):
    feature = _clean(vvp_replacement_051)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_055'] = {'inputs': ['vvp_replacement_051'], 'func': vvp_replacement_d2_055}


def vvp_replacement_d2_056(vvp_replacement_052):
    feature = _clean(vvp_replacement_052)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_056'] = {'inputs': ['vvp_replacement_052'], 'func': vvp_replacement_d2_056}


def vvp_replacement_d2_057(vvp_replacement_053):
    feature = _clean(vvp_replacement_053)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_057'] = {'inputs': ['vvp_replacement_053'], 'func': vvp_replacement_d2_057}


def vvp_replacement_d2_058(vvp_replacement_054):
    feature = _clean(vvp_replacement_054)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_058'] = {'inputs': ['vvp_replacement_054'], 'func': vvp_replacement_d2_058}


def vvp_replacement_d2_059(vvp_replacement_055):
    feature = _clean(vvp_replacement_055)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_059'] = {'inputs': ['vvp_replacement_055'], 'func': vvp_replacement_d2_059}


def vvp_replacement_d2_060(vvp_replacement_056):
    feature = _clean(vvp_replacement_056)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_060'] = {'inputs': ['vvp_replacement_056'], 'func': vvp_replacement_d2_060}


def vvp_replacement_d2_061(vvp_replacement_057):
    feature = _clean(vvp_replacement_057)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_061'] = {'inputs': ['vvp_replacement_057'], 'func': vvp_replacement_d2_061}


def vvp_replacement_d2_062(vvp_replacement_058):
    feature = _clean(vvp_replacement_058)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_062'] = {'inputs': ['vvp_replacement_058'], 'func': vvp_replacement_d2_062}


def vvp_replacement_d2_063(vvp_replacement_059):
    feature = _clean(vvp_replacement_059)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_063'] = {'inputs': ['vvp_replacement_059'], 'func': vvp_replacement_d2_063}


def vvp_replacement_d2_064(vvp_replacement_060):
    feature = _clean(vvp_replacement_060)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_064'] = {'inputs': ['vvp_replacement_060'], 'func': vvp_replacement_d2_064}


def vvp_replacement_d2_065(vvp_replacement_061):
    feature = _clean(vvp_replacement_061)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_065'] = {'inputs': ['vvp_replacement_061'], 'func': vvp_replacement_d2_065}


def vvp_replacement_d2_066(vvp_replacement_062):
    feature = _clean(vvp_replacement_062)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_066'] = {'inputs': ['vvp_replacement_062'], 'func': vvp_replacement_d2_066}


def vvp_replacement_d2_067(vvp_replacement_063):
    feature = _clean(vvp_replacement_063)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_067'] = {'inputs': ['vvp_replacement_063'], 'func': vvp_replacement_d2_067}


def vvp_replacement_d2_068(vvp_replacement_064):
    feature = _clean(vvp_replacement_064)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_068'] = {'inputs': ['vvp_replacement_064'], 'func': vvp_replacement_d2_068}


def vvp_replacement_d2_069(vvp_replacement_065):
    feature = _clean(vvp_replacement_065)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_069'] = {'inputs': ['vvp_replacement_065'], 'func': vvp_replacement_d2_069}


def vvp_replacement_d2_070(vvp_replacement_066):
    feature = _clean(vvp_replacement_066)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_070'] = {'inputs': ['vvp_replacement_066'], 'func': vvp_replacement_d2_070}


def vvp_replacement_d2_071(vvp_replacement_067):
    feature = _clean(vvp_replacement_067)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_071'] = {'inputs': ['vvp_replacement_067'], 'func': vvp_replacement_d2_071}


def vvp_replacement_d2_072(vvp_replacement_068):
    feature = _clean(vvp_replacement_068)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_072'] = {'inputs': ['vvp_replacement_068'], 'func': vvp_replacement_d2_072}


def vvp_replacement_d2_073(vvp_replacement_069):
    feature = _clean(vvp_replacement_069)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_073'] = {'inputs': ['vvp_replacement_069'], 'func': vvp_replacement_d2_073}


def vvp_replacement_d2_074(vvp_replacement_070):
    feature = _clean(vvp_replacement_070)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_074'] = {'inputs': ['vvp_replacement_070'], 'func': vvp_replacement_d2_074}


def vvp_replacement_d2_075(vvp_replacement_071):
    feature = _clean(vvp_replacement_071)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_075'] = {'inputs': ['vvp_replacement_071'], 'func': vvp_replacement_d2_075}


def vvp_replacement_d2_076(vvp_replacement_072):
    feature = _clean(vvp_replacement_072)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_076'] = {'inputs': ['vvp_replacement_072'], 'func': vvp_replacement_d2_076}


def vvp_replacement_d2_077(vvp_replacement_073):
    feature = _clean(vvp_replacement_073)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_077'] = {'inputs': ['vvp_replacement_073'], 'func': vvp_replacement_d2_077}


def vvp_replacement_d2_078(vvp_replacement_074):
    feature = _clean(vvp_replacement_074)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_078'] = {'inputs': ['vvp_replacement_074'], 'func': vvp_replacement_d2_078}


def vvp_replacement_d2_079(vvp_replacement_075):
    feature = _clean(vvp_replacement_075)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_079'] = {'inputs': ['vvp_replacement_075'], 'func': vvp_replacement_d2_079}


def vvp_replacement_d2_080(vvp_replacement_076):
    feature = _clean(vvp_replacement_076)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_080'] = {'inputs': ['vvp_replacement_076'], 'func': vvp_replacement_d2_080}


def vvp_replacement_d2_081(vvp_replacement_077):
    feature = _clean(vvp_replacement_077)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_081'] = {'inputs': ['vvp_replacement_077'], 'func': vvp_replacement_d2_081}


def vvp_replacement_d2_082(vvp_replacement_078):
    feature = _clean(vvp_replacement_078)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_082'] = {'inputs': ['vvp_replacement_078'], 'func': vvp_replacement_d2_082}


def vvp_replacement_d2_083(vvp_replacement_079):
    feature = _clean(vvp_replacement_079)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_083'] = {'inputs': ['vvp_replacement_079'], 'func': vvp_replacement_d2_083}


def vvp_replacement_d2_084(vvp_replacement_080):
    feature = _clean(vvp_replacement_080)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_084'] = {'inputs': ['vvp_replacement_080'], 'func': vvp_replacement_d2_084}


def vvp_replacement_d2_085(vvp_replacement_081):
    feature = _clean(vvp_replacement_081)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_085'] = {'inputs': ['vvp_replacement_081'], 'func': vvp_replacement_d2_085}


def vvp_replacement_d2_086(vvp_replacement_082):
    feature = _clean(vvp_replacement_082)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_086'] = {'inputs': ['vvp_replacement_082'], 'func': vvp_replacement_d2_086}


def vvp_replacement_d2_087(vvp_replacement_083):
    feature = _clean(vvp_replacement_083)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_087'] = {'inputs': ['vvp_replacement_083'], 'func': vvp_replacement_d2_087}


def vvp_replacement_d2_088(vvp_replacement_084):
    feature = _clean(vvp_replacement_084)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_088'] = {'inputs': ['vvp_replacement_084'], 'func': vvp_replacement_d2_088}


def vvp_replacement_d2_089(vvp_replacement_085):
    feature = _clean(vvp_replacement_085)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_089'] = {'inputs': ['vvp_replacement_085'], 'func': vvp_replacement_d2_089}


def vvp_replacement_d2_090(vvp_replacement_086):
    feature = _clean(vvp_replacement_086)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_090'] = {'inputs': ['vvp_replacement_086'], 'func': vvp_replacement_d2_090}


def vvp_replacement_d2_091(vvp_replacement_087):
    feature = _clean(vvp_replacement_087)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_091'] = {'inputs': ['vvp_replacement_087'], 'func': vvp_replacement_d2_091}


def vvp_replacement_d2_092(vvp_replacement_088):
    feature = _clean(vvp_replacement_088)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_092'] = {'inputs': ['vvp_replacement_088'], 'func': vvp_replacement_d2_092}


def vvp_replacement_d2_093(vvp_replacement_089):
    feature = _clean(vvp_replacement_089)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_093'] = {'inputs': ['vvp_replacement_089'], 'func': vvp_replacement_d2_093}


def vvp_replacement_d2_094(vvp_replacement_090):
    feature = _clean(vvp_replacement_090)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_094'] = {'inputs': ['vvp_replacement_090'], 'func': vvp_replacement_d2_094}


def vvp_replacement_d2_095(vvp_replacement_091):
    feature = _clean(vvp_replacement_091)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_095'] = {'inputs': ['vvp_replacement_091'], 'func': vvp_replacement_d2_095}


def vvp_replacement_d2_096(vvp_replacement_092):
    feature = _clean(vvp_replacement_092)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_096'] = {'inputs': ['vvp_replacement_092'], 'func': vvp_replacement_d2_096}


def vvp_replacement_d2_097(vvp_replacement_093):
    feature = _clean(vvp_replacement_093)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_097'] = {'inputs': ['vvp_replacement_093'], 'func': vvp_replacement_d2_097}


def vvp_replacement_d2_098(vvp_replacement_094):
    feature = _clean(vvp_replacement_094)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_098'] = {'inputs': ['vvp_replacement_094'], 'func': vvp_replacement_d2_098}


def vvp_replacement_d2_099(vvp_replacement_095):
    feature = _clean(vvp_replacement_095)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_099'] = {'inputs': ['vvp_replacement_095'], 'func': vvp_replacement_d2_099}


def vvp_replacement_d2_100(vvp_replacement_096):
    feature = _clean(vvp_replacement_096)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_100'] = {'inputs': ['vvp_replacement_096'], 'func': vvp_replacement_d2_100}


def vvp_replacement_d2_101(vvp_replacement_097):
    feature = _clean(vvp_replacement_097)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_101'] = {'inputs': ['vvp_replacement_097'], 'func': vvp_replacement_d2_101}


def vvp_replacement_d2_102(vvp_replacement_098):
    feature = _clean(vvp_replacement_098)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_102'] = {'inputs': ['vvp_replacement_098'], 'func': vvp_replacement_d2_102}


def vvp_replacement_d2_103(vvp_replacement_099):
    feature = _clean(vvp_replacement_099)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_103'] = {'inputs': ['vvp_replacement_099'], 'func': vvp_replacement_d2_103}


def vvp_replacement_d2_104(vvp_replacement_100):
    feature = _clean(vvp_replacement_100)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_104'] = {'inputs': ['vvp_replacement_100'], 'func': vvp_replacement_d2_104}


def vvp_replacement_d2_105(vvp_replacement_101):
    feature = _clean(vvp_replacement_101)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_105'] = {'inputs': ['vvp_replacement_101'], 'func': vvp_replacement_d2_105}


def vvp_replacement_d2_106(vvp_replacement_102):
    feature = _clean(vvp_replacement_102)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_106'] = {'inputs': ['vvp_replacement_102'], 'func': vvp_replacement_d2_106}


def vvp_replacement_d2_107(vvp_replacement_103):
    feature = _clean(vvp_replacement_103)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_107'] = {'inputs': ['vvp_replacement_103'], 'func': vvp_replacement_d2_107}


def vvp_replacement_d2_108(vvp_replacement_104):
    feature = _clean(vvp_replacement_104)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_108'] = {'inputs': ['vvp_replacement_104'], 'func': vvp_replacement_d2_108}


def vvp_replacement_d2_109(vvp_replacement_105):
    feature = _clean(vvp_replacement_105)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_109'] = {'inputs': ['vvp_replacement_105'], 'func': vvp_replacement_d2_109}


def vvp_replacement_d2_110(vvp_replacement_106):
    feature = _clean(vvp_replacement_106)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_110'] = {'inputs': ['vvp_replacement_106'], 'func': vvp_replacement_d2_110}


def vvp_replacement_d2_111(vvp_replacement_107):
    feature = _clean(vvp_replacement_107)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_111'] = {'inputs': ['vvp_replacement_107'], 'func': vvp_replacement_d2_111}


def vvp_replacement_d2_112(vvp_replacement_108):
    feature = _clean(vvp_replacement_108)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_112'] = {'inputs': ['vvp_replacement_108'], 'func': vvp_replacement_d2_112}


def vvp_replacement_d2_113(vvp_replacement_109):
    feature = _clean(vvp_replacement_109)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_113'] = {'inputs': ['vvp_replacement_109'], 'func': vvp_replacement_d2_113}


def vvp_replacement_d2_114(vvp_replacement_110):
    feature = _clean(vvp_replacement_110)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_114'] = {'inputs': ['vvp_replacement_110'], 'func': vvp_replacement_d2_114}


def vvp_replacement_d2_115(vvp_replacement_111):
    feature = _clean(vvp_replacement_111)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_115'] = {'inputs': ['vvp_replacement_111'], 'func': vvp_replacement_d2_115}


def vvp_replacement_d2_116(vvp_replacement_112):
    feature = _clean(vvp_replacement_112)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_116'] = {'inputs': ['vvp_replacement_112'], 'func': vvp_replacement_d2_116}


def vvp_replacement_d2_117(vvp_replacement_113):
    feature = _clean(vvp_replacement_113)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_117'] = {'inputs': ['vvp_replacement_113'], 'func': vvp_replacement_d2_117}


def vvp_replacement_d2_118(vvp_replacement_114):
    feature = _clean(vvp_replacement_114)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_118'] = {'inputs': ['vvp_replacement_114'], 'func': vvp_replacement_d2_118}


def vvp_replacement_d2_119(vvp_replacement_115):
    feature = _clean(vvp_replacement_115)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_119'] = {'inputs': ['vvp_replacement_115'], 'func': vvp_replacement_d2_119}


def vvp_replacement_d2_120(vvp_replacement_116):
    feature = _clean(vvp_replacement_116)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_120'] = {'inputs': ['vvp_replacement_116'], 'func': vvp_replacement_d2_120}


def vvp_replacement_d2_121(vvp_replacement_117):
    feature = _clean(vvp_replacement_117)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_121'] = {'inputs': ['vvp_replacement_117'], 'func': vvp_replacement_d2_121}


def vvp_replacement_d2_122(vvp_replacement_118):
    feature = _clean(vvp_replacement_118)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_122'] = {'inputs': ['vvp_replacement_118'], 'func': vvp_replacement_d2_122}


def vvp_replacement_d2_123(vvp_replacement_119):
    feature = _clean(vvp_replacement_119)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_123'] = {'inputs': ['vvp_replacement_119'], 'func': vvp_replacement_d2_123}


def vvp_replacement_d2_124(vvp_replacement_120):
    feature = _clean(vvp_replacement_120)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_124'] = {'inputs': ['vvp_replacement_120'], 'func': vvp_replacement_d2_124}


def vvp_replacement_d2_125(vvp_replacement_121):
    feature = _clean(vvp_replacement_121)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_125'] = {'inputs': ['vvp_replacement_121'], 'func': vvp_replacement_d2_125}


def vvp_replacement_d2_126(vvp_replacement_122):
    feature = _clean(vvp_replacement_122)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_126'] = {'inputs': ['vvp_replacement_122'], 'func': vvp_replacement_d2_126}


def vvp_replacement_d2_127(vvp_replacement_123):
    feature = _clean(vvp_replacement_123)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_127'] = {'inputs': ['vvp_replacement_123'], 'func': vvp_replacement_d2_127}


def vvp_replacement_d2_128(vvp_replacement_124):
    feature = _clean(vvp_replacement_124)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_128'] = {'inputs': ['vvp_replacement_124'], 'func': vvp_replacement_d2_128}


def vvp_replacement_d2_129(vvp_replacement_125):
    feature = _clean(vvp_replacement_125)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_129'] = {'inputs': ['vvp_replacement_125'], 'func': vvp_replacement_d2_129}


def vvp_replacement_d2_130(vvp_replacement_126):
    feature = _clean(vvp_replacement_126)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_130'] = {'inputs': ['vvp_replacement_126'], 'func': vvp_replacement_d2_130}


def vvp_replacement_d2_131(vvp_replacement_127):
    feature = _clean(vvp_replacement_127)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_131'] = {'inputs': ['vvp_replacement_127'], 'func': vvp_replacement_d2_131}


def vvp_replacement_d2_132(vvp_replacement_128):
    feature = _clean(vvp_replacement_128)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_132'] = {'inputs': ['vvp_replacement_128'], 'func': vvp_replacement_d2_132}


def vvp_replacement_d2_133(vvp_replacement_129):
    feature = _clean(vvp_replacement_129)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_133'] = {'inputs': ['vvp_replacement_129'], 'func': vvp_replacement_d2_133}


def vvp_replacement_d2_134(vvp_replacement_130):
    feature = _clean(vvp_replacement_130)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_134'] = {'inputs': ['vvp_replacement_130'], 'func': vvp_replacement_d2_134}


def vvp_replacement_d2_135(vvp_replacement_131):
    feature = _clean(vvp_replacement_131)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_135'] = {'inputs': ['vvp_replacement_131'], 'func': vvp_replacement_d2_135}


def vvp_replacement_d2_136(vvp_replacement_132):
    feature = _clean(vvp_replacement_132)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_136'] = {'inputs': ['vvp_replacement_132'], 'func': vvp_replacement_d2_136}


def vvp_replacement_d2_137(vvp_replacement_133):
    feature = _clean(vvp_replacement_133)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_137'] = {'inputs': ['vvp_replacement_133'], 'func': vvp_replacement_d2_137}


def vvp_replacement_d2_138(vvp_replacement_134):
    feature = _clean(vvp_replacement_134)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_138'] = {'inputs': ['vvp_replacement_134'], 'func': vvp_replacement_d2_138}


def vvp_replacement_d2_139(vvp_replacement_135):
    feature = _clean(vvp_replacement_135)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_139'] = {'inputs': ['vvp_replacement_135'], 'func': vvp_replacement_d2_139}


def vvp_replacement_d2_140(vvp_replacement_136):
    feature = _clean(vvp_replacement_136)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_140'] = {'inputs': ['vvp_replacement_136'], 'func': vvp_replacement_d2_140}


def vvp_replacement_d2_141(vvp_replacement_137):
    feature = _clean(vvp_replacement_137)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_141'] = {'inputs': ['vvp_replacement_137'], 'func': vvp_replacement_d2_141}


def vvp_replacement_d2_142(vvp_replacement_138):
    feature = _clean(vvp_replacement_138)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_142'] = {'inputs': ['vvp_replacement_138'], 'func': vvp_replacement_d2_142}


def vvp_replacement_d2_143(vvp_replacement_139):
    feature = _clean(vvp_replacement_139)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_143'] = {'inputs': ['vvp_replacement_139'], 'func': vvp_replacement_d2_143}


def vvp_replacement_d2_144(vvp_replacement_140):
    feature = _clean(vvp_replacement_140)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_144'] = {'inputs': ['vvp_replacement_140'], 'func': vvp_replacement_d2_144}


def vvp_replacement_d2_145(vvp_replacement_141):
    feature = _clean(vvp_replacement_141)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_145'] = {'inputs': ['vvp_replacement_141'], 'func': vvp_replacement_d2_145}


def vvp_replacement_d2_146(vvp_replacement_142):
    feature = _clean(vvp_replacement_142)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_146'] = {'inputs': ['vvp_replacement_142'], 'func': vvp_replacement_d2_146}


def vvp_replacement_d2_147(vvp_replacement_143):
    feature = _clean(vvp_replacement_143)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_147'] = {'inputs': ['vvp_replacement_143'], 'func': vvp_replacement_d2_147}


def vvp_replacement_d2_148(vvp_replacement_144):
    feature = _clean(vvp_replacement_144)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_148'] = {'inputs': ['vvp_replacement_144'], 'func': vvp_replacement_d2_148}


def vvp_replacement_d2_149(vvp_replacement_145):
    feature = _clean(vvp_replacement_145)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_149'] = {'inputs': ['vvp_replacement_145'], 'func': vvp_replacement_d2_149}


def vvp_replacement_d2_150(vvp_replacement_146):
    feature = _clean(vvp_replacement_146)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_150'] = {'inputs': ['vvp_replacement_146'], 'func': vvp_replacement_d2_150}


def vvp_replacement_d2_151(vvp_replacement_147):
    feature = _clean(vvp_replacement_147)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_151'] = {'inputs': ['vvp_replacement_147'], 'func': vvp_replacement_d2_151}


def vvp_replacement_d2_152(vvp_replacement_148):
    feature = _clean(vvp_replacement_148)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_152'] = {'inputs': ['vvp_replacement_148'], 'func': vvp_replacement_d2_152}


def vvp_replacement_d2_153(vvp_replacement_149):
    feature = _clean(vvp_replacement_149)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_153'] = {'inputs': ['vvp_replacement_149'], 'func': vvp_replacement_d2_153}


def vvp_replacement_d2_154(vvp_replacement_150):
    feature = _clean(vvp_replacement_150)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_154'] = {'inputs': ['vvp_replacement_150'], 'func': vvp_replacement_d2_154}


def vvp_replacement_d2_155(vvp_replacement_151):
    feature = _clean(vvp_replacement_151)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_155'] = {'inputs': ['vvp_replacement_151'], 'func': vvp_replacement_d2_155}


def vvp_replacement_d2_156(vvp_replacement_152):
    feature = _clean(vvp_replacement_152)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_156'] = {'inputs': ['vvp_replacement_152'], 'func': vvp_replacement_d2_156}


def vvp_replacement_d2_157(vvp_replacement_153):
    feature = _clean(vvp_replacement_153)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_157'] = {'inputs': ['vvp_replacement_153'], 'func': vvp_replacement_d2_157}


def vvp_replacement_d2_158(vvp_replacement_154):
    feature = _clean(vvp_replacement_154)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_158'] = {'inputs': ['vvp_replacement_154'], 'func': vvp_replacement_d2_158}


def vvp_replacement_d2_159(vvp_replacement_155):
    feature = _clean(vvp_replacement_155)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_159'] = {'inputs': ['vvp_replacement_155'], 'func': vvp_replacement_d2_159}


def vvp_replacement_d2_160(vvp_replacement_156):
    feature = _clean(vvp_replacement_156)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_160'] = {'inputs': ['vvp_replacement_156'], 'func': vvp_replacement_d2_160}


def vvp_replacement_d2_161(vvp_replacement_157):
    feature = _clean(vvp_replacement_157)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_161'] = {'inputs': ['vvp_replacement_157'], 'func': vvp_replacement_d2_161}


def vvp_replacement_d2_162(vvp_replacement_158):
    feature = _clean(vvp_replacement_158)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_162'] = {'inputs': ['vvp_replacement_158'], 'func': vvp_replacement_d2_162}


def vvp_replacement_d2_163(vvp_replacement_159):
    feature = _clean(vvp_replacement_159)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_163'] = {'inputs': ['vvp_replacement_159'], 'func': vvp_replacement_d2_163}


def vvp_replacement_d2_164(vvp_replacement_160):
    feature = _clean(vvp_replacement_160)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_164'] = {'inputs': ['vvp_replacement_160'], 'func': vvp_replacement_d2_164}


def vvp_replacement_d2_165(vvp_replacement_161):
    feature = _clean(vvp_replacement_161)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_165'] = {'inputs': ['vvp_replacement_161'], 'func': vvp_replacement_d2_165}


def vvp_replacement_d2_166(vvp_replacement_162):
    feature = _clean(vvp_replacement_162)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_166'] = {'inputs': ['vvp_replacement_162'], 'func': vvp_replacement_d2_166}


def vvp_replacement_d2_167(vvp_replacement_163):
    feature = _clean(vvp_replacement_163)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00167000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_167'] = {'inputs': ['vvp_replacement_163'], 'func': vvp_replacement_d2_167}


def vvp_replacement_d2_168(vvp_replacement_164):
    feature = _clean(vvp_replacement_164)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00168000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_168'] = {'inputs': ['vvp_replacement_164'], 'func': vvp_replacement_d2_168}


def vvp_replacement_d2_169(vvp_replacement_165):
    feature = _clean(vvp_replacement_165)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00169000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_169'] = {'inputs': ['vvp_replacement_165'], 'func': vvp_replacement_d2_169}


def vvp_replacement_d2_170(vvp_replacement_166):
    feature = _clean(vvp_replacement_166)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00170000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_170'] = {'inputs': ['vvp_replacement_166'], 'func': vvp_replacement_d2_170}


def vvp_replacement_d2_171(vvp_replacement_167):
    feature = _clean(vvp_replacement_167)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00171000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_171'] = {'inputs': ['vvp_replacement_167'], 'func': vvp_replacement_d2_171}


def vvp_replacement_d2_172(vvp_replacement_168):
    feature = _clean(vvp_replacement_168)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00172000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_172'] = {'inputs': ['vvp_replacement_168'], 'func': vvp_replacement_d2_172}


def vvp_replacement_d2_173(vvp_replacement_169):
    feature = _clean(vvp_replacement_169)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00173000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_173'] = {'inputs': ['vvp_replacement_169'], 'func': vvp_replacement_d2_173}


def vvp_replacement_d2_174(vvp_replacement_170):
    feature = _clean(vvp_replacement_170)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00174000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_174'] = {'inputs': ['vvp_replacement_170'], 'func': vvp_replacement_d2_174}


def vvp_replacement_d2_175(vvp_replacement_171):
    feature = _clean(vvp_replacement_171)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00175000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_175'] = {'inputs': ['vvp_replacement_171'], 'func': vvp_replacement_d2_175}


def vvp_replacement_d2_176(vvp_replacement_172):
    feature = _clean(vvp_replacement_172)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00176000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_176'] = {'inputs': ['vvp_replacement_172'], 'func': vvp_replacement_d2_176}


def vvp_replacement_d2_177(vvp_replacement_173):
    feature = _clean(vvp_replacement_173)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00177000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_177'] = {'inputs': ['vvp_replacement_173'], 'func': vvp_replacement_d2_177}


def vvp_replacement_d2_178(vvp_replacement_174):
    feature = _clean(vvp_replacement_174)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00178000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_178'] = {'inputs': ['vvp_replacement_174'], 'func': vvp_replacement_d2_178}


def vvp_replacement_d2_179(vvp_replacement_175):
    feature = _clean(vvp_replacement_175)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00179000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_179'] = {'inputs': ['vvp_replacement_175'], 'func': vvp_replacement_d2_179}


def vvp_replacement_d2_180(vvp_replacement_176):
    feature = _clean(vvp_replacement_176)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00180000).reindex(feature.index)
VVP_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vvp_replacement_d2_180'] = {'inputs': ['vvp_replacement_176'], 'func': vvp_replacement_d2_180}


# Base-universe derivative extensions for repaired first-base features.
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def vvp_base_universe_d2_001_vvp_005_peer_relative_pe_z_126(vvp_005_peer_relative_pe_z_126):
    return _base_universe_d2(vvp_005_peer_relative_pe_z_126, 1)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_001_vvp_005_peer_relative_pe_z_126'] = {'inputs': ['vvp_005_peer_relative_pe_z_126'], 'func': vvp_base_universe_d2_001_vvp_005_peer_relative_pe_z_126}


def vvp_base_universe_d2_002_vvp_006_peer_relative_pb_z_189(vvp_006_peer_relative_pb_z_189):
    return _base_universe_d2(vvp_006_peer_relative_pb_z_189, 2)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_002_vvp_006_peer_relative_pb_z_189'] = {'inputs': ['vvp_006_peer_relative_pb_z_189'], 'func': vvp_base_universe_d2_002_vvp_006_peer_relative_pb_z_189}


def vvp_base_universe_d2_003_vvp_011_peer_relative_pe_z_1008(vvp_011_peer_relative_pe_z_1008):
    return _base_universe_d2(vvp_011_peer_relative_pe_z_1008, 3)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_003_vvp_011_peer_relative_pe_z_1008'] = {'inputs': ['vvp_011_peer_relative_pe_z_1008'], 'func': vvp_base_universe_d2_003_vvp_011_peer_relative_pe_z_1008}


def vvp_base_universe_d2_004_vvp_012_peer_relative_pb_z_1260(vvp_012_peer_relative_pb_z_1260):
    return _base_universe_d2(vvp_012_peer_relative_pb_z_1260, 4)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_004_vvp_012_peer_relative_pb_z_1260'] = {'inputs': ['vvp_012_peer_relative_pb_z_1260'], 'func': vvp_base_universe_d2_004_vvp_012_peer_relative_pb_z_1260}


def vvp_base_universe_d2_005_vvp_017_peer_relative_pe_z_42(vvp_017_peer_relative_pe_z_42):
    return _base_universe_d2(vvp_017_peer_relative_pe_z_42, 5)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_005_vvp_017_peer_relative_pe_z_42'] = {'inputs': ['vvp_017_peer_relative_pe_z_42'], 'func': vvp_base_universe_d2_005_vvp_017_peer_relative_pe_z_42}


def vvp_base_universe_d2_006_vvp_018_peer_relative_pb_z_63(vvp_018_peer_relative_pb_z_63):
    return _base_universe_d2(vvp_018_peer_relative_pb_z_63, 6)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_006_vvp_018_peer_relative_pb_z_63'] = {'inputs': ['vvp_018_peer_relative_pb_z_63'], 'func': vvp_base_universe_d2_006_vvp_018_peer_relative_pb_z_63}


def vvp_base_universe_d2_007_vvp_023_peer_relative_pe_z_378(vvp_023_peer_relative_pe_z_378):
    return _base_universe_d2(vvp_023_peer_relative_pe_z_378, 7)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_007_vvp_023_peer_relative_pe_z_378'] = {'inputs': ['vvp_023_peer_relative_pe_z_378'], 'func': vvp_base_universe_d2_007_vvp_023_peer_relative_pe_z_378}


def vvp_base_universe_d2_008_vvp_024_peer_relative_pb_z_504(vvp_024_peer_relative_pb_z_504):
    return _base_universe_d2(vvp_024_peer_relative_pb_z_504, 8)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_008_vvp_024_peer_relative_pb_z_504'] = {'inputs': ['vvp_024_peer_relative_pb_z_504'], 'func': vvp_base_universe_d2_008_vvp_024_peer_relative_pb_z_504}


def vvp_base_universe_d2_009_vvp_030_peer_relative_pb_z_252(vvp_030_peer_relative_pb_z_252):
    return _base_universe_d2(vvp_030_peer_relative_pb_z_252, 9)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_009_vvp_030_peer_relative_pb_z_252'] = {'inputs': ['vvp_030_peer_relative_pb_z_252'], 'func': vvp_base_universe_d2_009_vvp_030_peer_relative_pb_z_252}


def vvp_base_universe_d2_010_vvp_basefill_002(vvp_basefill_002):
    return _base_universe_d2(vvp_basefill_002, 10)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_010_vvp_basefill_002'] = {'inputs': ['vvp_basefill_002'], 'func': vvp_base_universe_d2_010_vvp_basefill_002}


def vvp_base_universe_d2_011_vvp_basefill_003(vvp_basefill_003):
    return _base_universe_d2(vvp_basefill_003, 11)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_011_vvp_basefill_003'] = {'inputs': ['vvp_basefill_003'], 'func': vvp_base_universe_d2_011_vvp_basefill_003}


def vvp_base_universe_d2_012_vvp_basefill_004(vvp_basefill_004):
    return _base_universe_d2(vvp_basefill_004, 12)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_012_vvp_basefill_004'] = {'inputs': ['vvp_basefill_004'], 'func': vvp_base_universe_d2_012_vvp_basefill_004}


def vvp_base_universe_d2_013_vvp_basefill_007(vvp_basefill_007):
    return _base_universe_d2(vvp_basefill_007, 13)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_013_vvp_basefill_007'] = {'inputs': ['vvp_basefill_007'], 'func': vvp_base_universe_d2_013_vvp_basefill_007}


def vvp_base_universe_d2_014_vvp_basefill_008(vvp_basefill_008):
    return _base_universe_d2(vvp_basefill_008, 14)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_014_vvp_basefill_008'] = {'inputs': ['vvp_basefill_008'], 'func': vvp_base_universe_d2_014_vvp_basefill_008}


def vvp_base_universe_d2_015_vvp_basefill_009(vvp_basefill_009):
    return _base_universe_d2(vvp_basefill_009, 15)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_015_vvp_basefill_009'] = {'inputs': ['vvp_basefill_009'], 'func': vvp_base_universe_d2_015_vvp_basefill_009}


def vvp_base_universe_d2_016_vvp_basefill_010(vvp_basefill_010):
    return _base_universe_d2(vvp_basefill_010, 16)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_016_vvp_basefill_010'] = {'inputs': ['vvp_basefill_010'], 'func': vvp_base_universe_d2_016_vvp_basefill_010}


def vvp_base_universe_d2_017_vvp_basefill_013(vvp_basefill_013):
    return _base_universe_d2(vvp_basefill_013, 17)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_017_vvp_basefill_013'] = {'inputs': ['vvp_basefill_013'], 'func': vvp_base_universe_d2_017_vvp_basefill_013}


def vvp_base_universe_d2_018_vvp_basefill_014(vvp_basefill_014):
    return _base_universe_d2(vvp_basefill_014, 18)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_018_vvp_basefill_014'] = {'inputs': ['vvp_basefill_014'], 'func': vvp_base_universe_d2_018_vvp_basefill_014}


def vvp_base_universe_d2_019_vvp_basefill_015(vvp_basefill_015):
    return _base_universe_d2(vvp_basefill_015, 19)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_019_vvp_basefill_015'] = {'inputs': ['vvp_basefill_015'], 'func': vvp_base_universe_d2_019_vvp_basefill_015}


def vvp_base_universe_d2_020_vvp_basefill_016(vvp_basefill_016):
    return _base_universe_d2(vvp_basefill_016, 20)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_020_vvp_basefill_016'] = {'inputs': ['vvp_basefill_016'], 'func': vvp_base_universe_d2_020_vvp_basefill_016}


def vvp_base_universe_d2_021_vvp_basefill_019(vvp_basefill_019):
    return _base_universe_d2(vvp_basefill_019, 21)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_021_vvp_basefill_019'] = {'inputs': ['vvp_basefill_019'], 'func': vvp_base_universe_d2_021_vvp_basefill_019}


def vvp_base_universe_d2_022_vvp_basefill_020(vvp_basefill_020):
    return _base_universe_d2(vvp_basefill_020, 22)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_022_vvp_basefill_020'] = {'inputs': ['vvp_basefill_020'], 'func': vvp_base_universe_d2_022_vvp_basefill_020}


def vvp_base_universe_d2_023_vvp_basefill_021(vvp_basefill_021):
    return _base_universe_d2(vvp_basefill_021, 23)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_023_vvp_basefill_021'] = {'inputs': ['vvp_basefill_021'], 'func': vvp_base_universe_d2_023_vvp_basefill_021}


def vvp_base_universe_d2_024_vvp_basefill_022(vvp_basefill_022):
    return _base_universe_d2(vvp_basefill_022, 24)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_024_vvp_basefill_022'] = {'inputs': ['vvp_basefill_022'], 'func': vvp_base_universe_d2_024_vvp_basefill_022}


def vvp_base_universe_d2_025_vvp_basefill_025(vvp_basefill_025):
    return _base_universe_d2(vvp_basefill_025, 25)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_025_vvp_basefill_025'] = {'inputs': ['vvp_basefill_025'], 'func': vvp_base_universe_d2_025_vvp_basefill_025}


def vvp_base_universe_d2_026_vvp_basefill_026(vvp_basefill_026):
    return _base_universe_d2(vvp_basefill_026, 26)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_026_vvp_basefill_026'] = {'inputs': ['vvp_basefill_026'], 'func': vvp_base_universe_d2_026_vvp_basefill_026}


def vvp_base_universe_d2_027_vvp_basefill_027(vvp_basefill_027):
    return _base_universe_d2(vvp_basefill_027, 27)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_027_vvp_basefill_027'] = {'inputs': ['vvp_basefill_027'], 'func': vvp_base_universe_d2_027_vvp_basefill_027}


def vvp_base_universe_d2_028_vvp_basefill_028(vvp_basefill_028):
    return _base_universe_d2(vvp_basefill_028, 28)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_028_vvp_basefill_028'] = {'inputs': ['vvp_basefill_028'], 'func': vvp_base_universe_d2_028_vvp_basefill_028}


def vvp_base_universe_d2_029_vvp_basefill_029(vvp_basefill_029):
    return _base_universe_d2(vvp_basefill_029, 29)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_029_vvp_basefill_029'] = {'inputs': ['vvp_basefill_029'], 'func': vvp_base_universe_d2_029_vvp_basefill_029}


def vvp_base_universe_d2_030_vvp_basefill_031(vvp_basefill_031):
    return _base_universe_d2(vvp_basefill_031, 30)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_030_vvp_basefill_031'] = {'inputs': ['vvp_basefill_031'], 'func': vvp_base_universe_d2_030_vvp_basefill_031}


def vvp_base_universe_d2_031_vvp_basefill_032(vvp_basefill_032):
    return _base_universe_d2(vvp_basefill_032, 31)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_031_vvp_basefill_032'] = {'inputs': ['vvp_basefill_032'], 'func': vvp_base_universe_d2_031_vvp_basefill_032}


def vvp_base_universe_d2_032_vvp_basefill_033(vvp_basefill_033):
    return _base_universe_d2(vvp_basefill_033, 32)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_032_vvp_basefill_033'] = {'inputs': ['vvp_basefill_033'], 'func': vvp_base_universe_d2_032_vvp_basefill_033}


def vvp_base_universe_d2_033_vvp_basefill_034(vvp_basefill_034):
    return _base_universe_d2(vvp_basefill_034, 33)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_033_vvp_basefill_034'] = {'inputs': ['vvp_basefill_034'], 'func': vvp_base_universe_d2_033_vvp_basefill_034}


def vvp_base_universe_d2_034_vvp_basefill_035(vvp_basefill_035):
    return _base_universe_d2(vvp_basefill_035, 34)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_034_vvp_basefill_035'] = {'inputs': ['vvp_basefill_035'], 'func': vvp_base_universe_d2_034_vvp_basefill_035}


def vvp_base_universe_d2_035_vvp_basefill_036(vvp_basefill_036):
    return _base_universe_d2(vvp_basefill_036, 35)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_035_vvp_basefill_036'] = {'inputs': ['vvp_basefill_036'], 'func': vvp_base_universe_d2_035_vvp_basefill_036}


def vvp_base_universe_d2_036_vvp_basefill_037(vvp_basefill_037):
    return _base_universe_d2(vvp_basefill_037, 36)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_036_vvp_basefill_037'] = {'inputs': ['vvp_basefill_037'], 'func': vvp_base_universe_d2_036_vvp_basefill_037}


def vvp_base_universe_d2_037_vvp_basefill_038(vvp_basefill_038):
    return _base_universe_d2(vvp_basefill_038, 37)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_037_vvp_basefill_038'] = {'inputs': ['vvp_basefill_038'], 'func': vvp_base_universe_d2_037_vvp_basefill_038}


def vvp_base_universe_d2_038_vvp_basefill_039(vvp_basefill_039):
    return _base_universe_d2(vvp_basefill_039, 38)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_038_vvp_basefill_039'] = {'inputs': ['vvp_basefill_039'], 'func': vvp_base_universe_d2_038_vvp_basefill_039}


def vvp_base_universe_d2_039_vvp_basefill_040(vvp_basefill_040):
    return _base_universe_d2(vvp_basefill_040, 39)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_039_vvp_basefill_040'] = {'inputs': ['vvp_basefill_040'], 'func': vvp_base_universe_d2_039_vvp_basefill_040}


def vvp_base_universe_d2_040_vvp_basefill_041(vvp_basefill_041):
    return _base_universe_d2(vvp_basefill_041, 40)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_040_vvp_basefill_041'] = {'inputs': ['vvp_basefill_041'], 'func': vvp_base_universe_d2_040_vvp_basefill_041}


def vvp_base_universe_d2_041_vvp_basefill_042(vvp_basefill_042):
    return _base_universe_d2(vvp_basefill_042, 41)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_041_vvp_basefill_042'] = {'inputs': ['vvp_basefill_042'], 'func': vvp_base_universe_d2_041_vvp_basefill_042}


def vvp_base_universe_d2_042_vvp_basefill_043(vvp_basefill_043):
    return _base_universe_d2(vvp_basefill_043, 42)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_042_vvp_basefill_043'] = {'inputs': ['vvp_basefill_043'], 'func': vvp_base_universe_d2_042_vvp_basefill_043}


def vvp_base_universe_d2_043_vvp_basefill_044(vvp_basefill_044):
    return _base_universe_d2(vvp_basefill_044, 43)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_043_vvp_basefill_044'] = {'inputs': ['vvp_basefill_044'], 'func': vvp_base_universe_d2_043_vvp_basefill_044}


def vvp_base_universe_d2_044_vvp_basefill_045(vvp_basefill_045):
    return _base_universe_d2(vvp_basefill_045, 44)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_044_vvp_basefill_045'] = {'inputs': ['vvp_basefill_045'], 'func': vvp_base_universe_d2_044_vvp_basefill_045}


def vvp_base_universe_d2_045_vvp_basefill_046(vvp_basefill_046):
    return _base_universe_d2(vvp_basefill_046, 45)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_045_vvp_basefill_046'] = {'inputs': ['vvp_basefill_046'], 'func': vvp_base_universe_d2_045_vvp_basefill_046}


def vvp_base_universe_d2_046_vvp_basefill_047(vvp_basefill_047):
    return _base_universe_d2(vvp_basefill_047, 46)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_046_vvp_basefill_047'] = {'inputs': ['vvp_basefill_047'], 'func': vvp_base_universe_d2_046_vvp_basefill_047}


def vvp_base_universe_d2_047_vvp_basefill_048(vvp_basefill_048):
    return _base_universe_d2(vvp_basefill_048, 47)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_047_vvp_basefill_048'] = {'inputs': ['vvp_basefill_048'], 'func': vvp_base_universe_d2_047_vvp_basefill_048}


def vvp_base_universe_d2_048_vvp_basefill_049(vvp_basefill_049):
    return _base_universe_d2(vvp_basefill_049, 48)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_048_vvp_basefill_049'] = {'inputs': ['vvp_basefill_049'], 'func': vvp_base_universe_d2_048_vvp_basefill_049}


def vvp_base_universe_d2_049_vvp_basefill_050(vvp_basefill_050):
    return _base_universe_d2(vvp_basefill_050, 49)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_049_vvp_basefill_050'] = {'inputs': ['vvp_basefill_050'], 'func': vvp_base_universe_d2_049_vvp_basefill_050}


def vvp_base_universe_d2_050_vvp_basefill_051(vvp_basefill_051):
    return _base_universe_d2(vvp_basefill_051, 50)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_050_vvp_basefill_051'] = {'inputs': ['vvp_basefill_051'], 'func': vvp_base_universe_d2_050_vvp_basefill_051}


def vvp_base_universe_d2_051_vvp_basefill_052(vvp_basefill_052):
    return _base_universe_d2(vvp_basefill_052, 51)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_051_vvp_basefill_052'] = {'inputs': ['vvp_basefill_052'], 'func': vvp_base_universe_d2_051_vvp_basefill_052}


def vvp_base_universe_d2_052_vvp_basefill_053(vvp_basefill_053):
    return _base_universe_d2(vvp_basefill_053, 52)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_052_vvp_basefill_053'] = {'inputs': ['vvp_basefill_053'], 'func': vvp_base_universe_d2_052_vvp_basefill_053}


def vvp_base_universe_d2_053_vvp_basefill_054(vvp_basefill_054):
    return _base_universe_d2(vvp_basefill_054, 53)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_053_vvp_basefill_054'] = {'inputs': ['vvp_basefill_054'], 'func': vvp_base_universe_d2_053_vvp_basefill_054}


def vvp_base_universe_d2_054_vvp_basefill_055(vvp_basefill_055):
    return _base_universe_d2(vvp_basefill_055, 54)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_054_vvp_basefill_055'] = {'inputs': ['vvp_basefill_055'], 'func': vvp_base_universe_d2_054_vvp_basefill_055}


def vvp_base_universe_d2_055_vvp_basefill_056(vvp_basefill_056):
    return _base_universe_d2(vvp_basefill_056, 55)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_055_vvp_basefill_056'] = {'inputs': ['vvp_basefill_056'], 'func': vvp_base_universe_d2_055_vvp_basefill_056}


def vvp_base_universe_d2_056_vvp_basefill_057(vvp_basefill_057):
    return _base_universe_d2(vvp_basefill_057, 56)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_056_vvp_basefill_057'] = {'inputs': ['vvp_basefill_057'], 'func': vvp_base_universe_d2_056_vvp_basefill_057}


def vvp_base_universe_d2_057_vvp_basefill_058(vvp_basefill_058):
    return _base_universe_d2(vvp_basefill_058, 57)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_057_vvp_basefill_058'] = {'inputs': ['vvp_basefill_058'], 'func': vvp_base_universe_d2_057_vvp_basefill_058}


def vvp_base_universe_d2_058_vvp_basefill_059(vvp_basefill_059):
    return _base_universe_d2(vvp_basefill_059, 58)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_058_vvp_basefill_059'] = {'inputs': ['vvp_basefill_059'], 'func': vvp_base_universe_d2_058_vvp_basefill_059}


def vvp_base_universe_d2_059_vvp_basefill_060(vvp_basefill_060):
    return _base_universe_d2(vvp_basefill_060, 59)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_059_vvp_basefill_060'] = {'inputs': ['vvp_basefill_060'], 'func': vvp_base_universe_d2_059_vvp_basefill_060}


def vvp_base_universe_d2_060_vvp_basefill_061(vvp_basefill_061):
    return _base_universe_d2(vvp_basefill_061, 60)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_060_vvp_basefill_061'] = {'inputs': ['vvp_basefill_061'], 'func': vvp_base_universe_d2_060_vvp_basefill_061}


def vvp_base_universe_d2_061_vvp_basefill_062(vvp_basefill_062):
    return _base_universe_d2(vvp_basefill_062, 61)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_061_vvp_basefill_062'] = {'inputs': ['vvp_basefill_062'], 'func': vvp_base_universe_d2_061_vvp_basefill_062}


def vvp_base_universe_d2_062_vvp_basefill_063(vvp_basefill_063):
    return _base_universe_d2(vvp_basefill_063, 62)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_062_vvp_basefill_063'] = {'inputs': ['vvp_basefill_063'], 'func': vvp_base_universe_d2_062_vvp_basefill_063}


def vvp_base_universe_d2_063_vvp_basefill_064(vvp_basefill_064):
    return _base_universe_d2(vvp_basefill_064, 63)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_063_vvp_basefill_064'] = {'inputs': ['vvp_basefill_064'], 'func': vvp_base_universe_d2_063_vvp_basefill_064}


def vvp_base_universe_d2_064_vvp_basefill_065(vvp_basefill_065):
    return _base_universe_d2(vvp_basefill_065, 64)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_064_vvp_basefill_065'] = {'inputs': ['vvp_basefill_065'], 'func': vvp_base_universe_d2_064_vvp_basefill_065}


def vvp_base_universe_d2_065_vvp_basefill_066(vvp_basefill_066):
    return _base_universe_d2(vvp_basefill_066, 65)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_065_vvp_basefill_066'] = {'inputs': ['vvp_basefill_066'], 'func': vvp_base_universe_d2_065_vvp_basefill_066}


def vvp_base_universe_d2_066_vvp_basefill_067(vvp_basefill_067):
    return _base_universe_d2(vvp_basefill_067, 66)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_066_vvp_basefill_067'] = {'inputs': ['vvp_basefill_067'], 'func': vvp_base_universe_d2_066_vvp_basefill_067}


def vvp_base_universe_d2_067_vvp_basefill_068(vvp_basefill_068):
    return _base_universe_d2(vvp_basefill_068, 67)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_067_vvp_basefill_068'] = {'inputs': ['vvp_basefill_068'], 'func': vvp_base_universe_d2_067_vvp_basefill_068}


def vvp_base_universe_d2_068_vvp_basefill_069(vvp_basefill_069):
    return _base_universe_d2(vvp_basefill_069, 68)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_068_vvp_basefill_069'] = {'inputs': ['vvp_basefill_069'], 'func': vvp_base_universe_d2_068_vvp_basefill_069}


def vvp_base_universe_d2_069_vvp_basefill_070(vvp_basefill_070):
    return _base_universe_d2(vvp_basefill_070, 69)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_069_vvp_basefill_070'] = {'inputs': ['vvp_basefill_070'], 'func': vvp_base_universe_d2_069_vvp_basefill_070}


def vvp_base_universe_d2_070_vvp_basefill_071(vvp_basefill_071):
    return _base_universe_d2(vvp_basefill_071, 70)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_070_vvp_basefill_071'] = {'inputs': ['vvp_basefill_071'], 'func': vvp_base_universe_d2_070_vvp_basefill_071}


def vvp_base_universe_d2_071_vvp_basefill_072(vvp_basefill_072):
    return _base_universe_d2(vvp_basefill_072, 71)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_071_vvp_basefill_072'] = {'inputs': ['vvp_basefill_072'], 'func': vvp_base_universe_d2_071_vvp_basefill_072}


def vvp_base_universe_d2_072_vvp_basefill_073(vvp_basefill_073):
    return _base_universe_d2(vvp_basefill_073, 72)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_072_vvp_basefill_073'] = {'inputs': ['vvp_basefill_073'], 'func': vvp_base_universe_d2_072_vvp_basefill_073}


def vvp_base_universe_d2_073_vvp_basefill_074(vvp_basefill_074):
    return _base_universe_d2(vvp_basefill_074, 73)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_073_vvp_basefill_074'] = {'inputs': ['vvp_basefill_074'], 'func': vvp_base_universe_d2_073_vvp_basefill_074}


def vvp_base_universe_d2_074_vvp_basefill_075(vvp_basefill_075):
    return _base_universe_d2(vvp_basefill_075, 74)
VVP_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vvp_base_universe_d2_074_vvp_basefill_075'] = {'inputs': ['vvp_basefill_075'], 'func': vvp_base_universe_d2_074_vvp_basefill_075}
