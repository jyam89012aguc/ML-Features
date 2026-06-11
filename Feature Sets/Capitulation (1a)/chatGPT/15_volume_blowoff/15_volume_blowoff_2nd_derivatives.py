import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _safe_div(a, b):
    b = _s(b).replace(0, np.nan)
    if np.isscalar(a):
        return a / b
    a = _s(a)
    return a / b


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


def _true_range(high, low, close):
    high = _s(high)
    low = _s(low)
    prev_close = _s(close).shift(1)
    return pd.concat([high - low, (high - prev_close).abs(), (low - prev_close).abs()], axis=1).max(axis=1)


def _streak(mask):
    mask = pd.Series(mask).fillna(False).astype(bool)
    groups = mask.ne(mask.shift()).cumsum()
    return mask.groupby(groups).cumcount().add(1).where(mask, 0).astype(float)



def vb_151_vb_001_volume_spike_ratio_5_001_roc_1(vb_001_volume_spike_ratio_5_001):
    feature = _s(vb_001_volume_spike_ratio_5_001)
    return (_roc(feature, 1)).reindex(feature.index)

def vb_152_vb_007_volume_spike_ratio_126_007_roc_5(vb_007_volume_spike_ratio_126_007):
    feature = _s(vb_007_volume_spike_ratio_126_007)
    return (_roc(feature, 5)).reindex(feature.index)

def vb_153_vb_013_volume_spike_ratio_1008_013_roc_42(vb_013_volume_spike_ratio_1008_013):
    feature = _s(vb_013_volume_spike_ratio_1008_013)
    return (_roc(feature, 42)).reindex(feature.index)

def vb_154_vb_019_volume_spike_ratio_42_019_roc_126(vb_019_volume_spike_ratio_42_019):
    feature = _s(vb_019_volume_spike_ratio_42_019)
    return (_roc(feature, 126)).reindex(feature.index)

def vb_155_vb_025_volume_spike_ratio_378_025_roc_378(vb_025_volume_spike_ratio_378_025):
    feature = _s(vb_025_volume_spike_ratio_378_025)
    return (_roc(feature, 378)).reindex(feature.index)






















VOLUME_BLOWOFF_REGISTRY_2ND_DERIVATIVES = {
    'vb_151_vb_001_volume_spike_ratio_5_001_roc_1': {'inputs': ['vb_001_volume_spike_ratio_5_001'], 'func': vb_151_vb_001_volume_spike_ratio_5_001_roc_1},
    'vb_152_vb_007_volume_spike_ratio_126_007_roc_5': {'inputs': ['vb_007_volume_spike_ratio_126_007'], 'func': vb_152_vb_007_volume_spike_ratio_126_007_roc_5},
    'vb_153_vb_013_volume_spike_ratio_1008_013_roc_42': {'inputs': ['vb_013_volume_spike_ratio_1008_013'], 'func': vb_153_vb_013_volume_spike_ratio_1008_013_roc_42},
    'vb_154_vb_019_volume_spike_ratio_42_019_roc_126': {'inputs': ['vb_019_volume_spike_ratio_42_019'], 'func': vb_154_vb_019_volume_spike_ratio_42_019_roc_126},
    'vb_155_vb_025_volume_spike_ratio_378_025_roc_378': {'inputs': ['vb_025_volume_spike_ratio_378_025'], 'func': vb_155_vb_025_volume_spike_ratio_378_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def vb_replacement_d2_001(vb_replacement_001):
    feature = _clean(vb_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_001'] = {'inputs': ['vb_replacement_001'], 'func': vb_replacement_d2_001}


def vb_replacement_d2_002(vb_replacement_002):
    feature = _clean(vb_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_002'] = {'inputs': ['vb_replacement_002'], 'func': vb_replacement_d2_002}


def vb_replacement_d2_003(vb_replacement_003):
    feature = _clean(vb_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_003'] = {'inputs': ['vb_replacement_003'], 'func': vb_replacement_d2_003}


def vb_replacement_d2_004(vb_replacement_004):
    feature = _clean(vb_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_004'] = {'inputs': ['vb_replacement_004'], 'func': vb_replacement_d2_004}


def vb_replacement_d2_005(vb_replacement_005):
    feature = _clean(vb_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_005'] = {'inputs': ['vb_replacement_005'], 'func': vb_replacement_d2_005}


def vb_replacement_d2_006(vb_replacement_006):
    feature = _clean(vb_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_006'] = {'inputs': ['vb_replacement_006'], 'func': vb_replacement_d2_006}


def vb_replacement_d2_007(vb_replacement_007):
    feature = _clean(vb_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_007'] = {'inputs': ['vb_replacement_007'], 'func': vb_replacement_d2_007}


def vb_replacement_d2_008(vb_replacement_008):
    feature = _clean(vb_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_008'] = {'inputs': ['vb_replacement_008'], 'func': vb_replacement_d2_008}


def vb_replacement_d2_009(vb_replacement_009):
    feature = _clean(vb_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_009'] = {'inputs': ['vb_replacement_009'], 'func': vb_replacement_d2_009}


def vb_replacement_d2_010(vb_replacement_010):
    feature = _clean(vb_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_010'] = {'inputs': ['vb_replacement_010'], 'func': vb_replacement_d2_010}


def vb_replacement_d2_011(vb_replacement_011):
    feature = _clean(vb_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_011'] = {'inputs': ['vb_replacement_011'], 'func': vb_replacement_d2_011}


def vb_replacement_d2_012(vb_replacement_012):
    feature = _clean(vb_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_012'] = {'inputs': ['vb_replacement_012'], 'func': vb_replacement_d2_012}


def vb_replacement_d2_013(vb_replacement_013):
    feature = _clean(vb_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_013'] = {'inputs': ['vb_replacement_013'], 'func': vb_replacement_d2_013}


def vb_replacement_d2_014(vb_replacement_014):
    feature = _clean(vb_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_014'] = {'inputs': ['vb_replacement_014'], 'func': vb_replacement_d2_014}


def vb_replacement_d2_015(vb_replacement_015):
    feature = _clean(vb_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_015'] = {'inputs': ['vb_replacement_015'], 'func': vb_replacement_d2_015}


def vb_replacement_d2_016(vb_replacement_016):
    feature = _clean(vb_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_016'] = {'inputs': ['vb_replacement_016'], 'func': vb_replacement_d2_016}


def vb_replacement_d2_017(vb_replacement_017):
    feature = _clean(vb_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_017'] = {'inputs': ['vb_replacement_017'], 'func': vb_replacement_d2_017}


def vb_replacement_d2_018(vb_replacement_018):
    feature = _clean(vb_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_018'] = {'inputs': ['vb_replacement_018'], 'func': vb_replacement_d2_018}


def vb_replacement_d2_019(vb_replacement_019):
    feature = _clean(vb_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_019'] = {'inputs': ['vb_replacement_019'], 'func': vb_replacement_d2_019}


def vb_replacement_d2_020(vb_replacement_020):
    feature = _clean(vb_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_020'] = {'inputs': ['vb_replacement_020'], 'func': vb_replacement_d2_020}


def vb_replacement_d2_021(vb_replacement_021):
    feature = _clean(vb_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_021'] = {'inputs': ['vb_replacement_021'], 'func': vb_replacement_d2_021}


def vb_replacement_d2_022(vb_replacement_022):
    feature = _clean(vb_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_022'] = {'inputs': ['vb_replacement_022'], 'func': vb_replacement_d2_022}


def vb_replacement_d2_023(vb_replacement_023):
    feature = _clean(vb_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_023'] = {'inputs': ['vb_replacement_023'], 'func': vb_replacement_d2_023}


def vb_replacement_d2_024(vb_replacement_024):
    feature = _clean(vb_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_024'] = {'inputs': ['vb_replacement_024'], 'func': vb_replacement_d2_024}


def vb_replacement_d2_025(vb_replacement_025):
    feature = _clean(vb_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_025'] = {'inputs': ['vb_replacement_025'], 'func': vb_replacement_d2_025}


def vb_replacement_d2_026(vb_replacement_026):
    feature = _clean(vb_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_026'] = {'inputs': ['vb_replacement_026'], 'func': vb_replacement_d2_026}


def vb_replacement_d2_027(vb_replacement_027):
    feature = _clean(vb_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_027'] = {'inputs': ['vb_replacement_027'], 'func': vb_replacement_d2_027}


def vb_replacement_d2_028(vb_replacement_028):
    feature = _clean(vb_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_028'] = {'inputs': ['vb_replacement_028'], 'func': vb_replacement_d2_028}


def vb_replacement_d2_029(vb_replacement_029):
    feature = _clean(vb_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_029'] = {'inputs': ['vb_replacement_029'], 'func': vb_replacement_d2_029}


def vb_replacement_d2_030(vb_replacement_030):
    feature = _clean(vb_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_030'] = {'inputs': ['vb_replacement_030'], 'func': vb_replacement_d2_030}


def vb_replacement_d2_031(vb_replacement_031):
    feature = _clean(vb_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_031'] = {'inputs': ['vb_replacement_031'], 'func': vb_replacement_d2_031}


def vb_replacement_d2_032(vb_replacement_032):
    feature = _clean(vb_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_032'] = {'inputs': ['vb_replacement_032'], 'func': vb_replacement_d2_032}


def vb_replacement_d2_033(vb_replacement_033):
    feature = _clean(vb_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_033'] = {'inputs': ['vb_replacement_033'], 'func': vb_replacement_d2_033}


def vb_replacement_d2_034(vb_replacement_034):
    feature = _clean(vb_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_034'] = {'inputs': ['vb_replacement_034'], 'func': vb_replacement_d2_034}


def vb_replacement_d2_035(vb_replacement_035):
    feature = _clean(vb_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_035'] = {'inputs': ['vb_replacement_035'], 'func': vb_replacement_d2_035}


def vb_replacement_d2_036(vb_replacement_036):
    feature = _clean(vb_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_036'] = {'inputs': ['vb_replacement_036'], 'func': vb_replacement_d2_036}


def vb_replacement_d2_037(vb_replacement_037):
    feature = _clean(vb_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_037'] = {'inputs': ['vb_replacement_037'], 'func': vb_replacement_d2_037}


def vb_replacement_d2_038(vb_replacement_038):
    feature = _clean(vb_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_038'] = {'inputs': ['vb_replacement_038'], 'func': vb_replacement_d2_038}


def vb_replacement_d2_039(vb_replacement_039):
    feature = _clean(vb_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_039'] = {'inputs': ['vb_replacement_039'], 'func': vb_replacement_d2_039}


def vb_replacement_d2_040(vb_replacement_040):
    feature = _clean(vb_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_040'] = {'inputs': ['vb_replacement_040'], 'func': vb_replacement_d2_040}


def vb_replacement_d2_041(vb_replacement_041):
    feature = _clean(vb_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_041'] = {'inputs': ['vb_replacement_041'], 'func': vb_replacement_d2_041}


def vb_replacement_d2_042(vb_replacement_042):
    feature = _clean(vb_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_042'] = {'inputs': ['vb_replacement_042'], 'func': vb_replacement_d2_042}


def vb_replacement_d2_043(vb_replacement_043):
    feature = _clean(vb_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_043'] = {'inputs': ['vb_replacement_043'], 'func': vb_replacement_d2_043}


def vb_replacement_d2_044(vb_replacement_044):
    feature = _clean(vb_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_044'] = {'inputs': ['vb_replacement_044'], 'func': vb_replacement_d2_044}


def vb_replacement_d2_045(vb_replacement_045):
    feature = _clean(vb_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_045'] = {'inputs': ['vb_replacement_045'], 'func': vb_replacement_d2_045}


def vb_replacement_d2_046(vb_replacement_046):
    feature = _clean(vb_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_046'] = {'inputs': ['vb_replacement_046'], 'func': vb_replacement_d2_046}


def vb_replacement_d2_047(vb_replacement_047):
    feature = _clean(vb_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_047'] = {'inputs': ['vb_replacement_047'], 'func': vb_replacement_d2_047}


def vb_replacement_d2_048(vb_replacement_048):
    feature = _clean(vb_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_048'] = {'inputs': ['vb_replacement_048'], 'func': vb_replacement_d2_048}


def vb_replacement_d2_049(vb_replacement_049):
    feature = _clean(vb_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_049'] = {'inputs': ['vb_replacement_049'], 'func': vb_replacement_d2_049}


def vb_replacement_d2_050(vb_replacement_050):
    feature = _clean(vb_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_050'] = {'inputs': ['vb_replacement_050'], 'func': vb_replacement_d2_050}


def vb_replacement_d2_051(vb_replacement_051):
    feature = _clean(vb_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_051'] = {'inputs': ['vb_replacement_051'], 'func': vb_replacement_d2_051}


def vb_replacement_d2_052(vb_replacement_052):
    feature = _clean(vb_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_052'] = {'inputs': ['vb_replacement_052'], 'func': vb_replacement_d2_052}


def vb_replacement_d2_053(vb_replacement_053):
    feature = _clean(vb_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_053'] = {'inputs': ['vb_replacement_053'], 'func': vb_replacement_d2_053}


def vb_replacement_d2_054(vb_replacement_054):
    feature = _clean(vb_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_054'] = {'inputs': ['vb_replacement_054'], 'func': vb_replacement_d2_054}


def vb_replacement_d2_055(vb_replacement_055):
    feature = _clean(vb_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_055'] = {'inputs': ['vb_replacement_055'], 'func': vb_replacement_d2_055}


def vb_replacement_d2_056(vb_replacement_056):
    feature = _clean(vb_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_056'] = {'inputs': ['vb_replacement_056'], 'func': vb_replacement_d2_056}


def vb_replacement_d2_057(vb_replacement_057):
    feature = _clean(vb_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_057'] = {'inputs': ['vb_replacement_057'], 'func': vb_replacement_d2_057}


def vb_replacement_d2_058(vb_replacement_058):
    feature = _clean(vb_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_058'] = {'inputs': ['vb_replacement_058'], 'func': vb_replacement_d2_058}


def vb_replacement_d2_059(vb_replacement_059):
    feature = _clean(vb_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_059'] = {'inputs': ['vb_replacement_059'], 'func': vb_replacement_d2_059}


def vb_replacement_d2_060(vb_replacement_060):
    feature = _clean(vb_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_060'] = {'inputs': ['vb_replacement_060'], 'func': vb_replacement_d2_060}


def vb_replacement_d2_061(vb_replacement_061):
    feature = _clean(vb_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_061'] = {'inputs': ['vb_replacement_061'], 'func': vb_replacement_d2_061}


def vb_replacement_d2_062(vb_replacement_062):
    feature = _clean(vb_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_062'] = {'inputs': ['vb_replacement_062'], 'func': vb_replacement_d2_062}


def vb_replacement_d2_063(vb_replacement_063):
    feature = _clean(vb_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_063'] = {'inputs': ['vb_replacement_063'], 'func': vb_replacement_d2_063}


def vb_replacement_d2_064(vb_replacement_064):
    feature = _clean(vb_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_064'] = {'inputs': ['vb_replacement_064'], 'func': vb_replacement_d2_064}


def vb_replacement_d2_065(vb_replacement_065):
    feature = _clean(vb_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_065'] = {'inputs': ['vb_replacement_065'], 'func': vb_replacement_d2_065}


def vb_replacement_d2_066(vb_replacement_066):
    feature = _clean(vb_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_066'] = {'inputs': ['vb_replacement_066'], 'func': vb_replacement_d2_066}


def vb_replacement_d2_067(vb_replacement_067):
    feature = _clean(vb_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_067'] = {'inputs': ['vb_replacement_067'], 'func': vb_replacement_d2_067}


def vb_replacement_d2_068(vb_replacement_068):
    feature = _clean(vb_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_068'] = {'inputs': ['vb_replacement_068'], 'func': vb_replacement_d2_068}


def vb_replacement_d2_069(vb_replacement_069):
    feature = _clean(vb_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_069'] = {'inputs': ['vb_replacement_069'], 'func': vb_replacement_d2_069}


def vb_replacement_d2_070(vb_replacement_070):
    feature = _clean(vb_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_070'] = {'inputs': ['vb_replacement_070'], 'func': vb_replacement_d2_070}


def vb_replacement_d2_071(vb_replacement_071):
    feature = _clean(vb_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_071'] = {'inputs': ['vb_replacement_071'], 'func': vb_replacement_d2_071}


def vb_replacement_d2_072(vb_replacement_072):
    feature = _clean(vb_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_072'] = {'inputs': ['vb_replacement_072'], 'func': vb_replacement_d2_072}


def vb_replacement_d2_073(vb_replacement_073):
    feature = _clean(vb_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_073'] = {'inputs': ['vb_replacement_073'], 'func': vb_replacement_d2_073}


def vb_replacement_d2_074(vb_replacement_074):
    feature = _clean(vb_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_074'] = {'inputs': ['vb_replacement_074'], 'func': vb_replacement_d2_074}


def vb_replacement_d2_075(vb_replacement_075):
    feature = _clean(vb_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_075'] = {'inputs': ['vb_replacement_075'], 'func': vb_replacement_d2_075}


def vb_replacement_d2_076(vb_replacement_076):
    feature = _clean(vb_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_076'] = {'inputs': ['vb_replacement_076'], 'func': vb_replacement_d2_076}


def vb_replacement_d2_077(vb_replacement_077):
    feature = _clean(vb_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_077'] = {'inputs': ['vb_replacement_077'], 'func': vb_replacement_d2_077}


def vb_replacement_d2_078(vb_replacement_078):
    feature = _clean(vb_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_078'] = {'inputs': ['vb_replacement_078'], 'func': vb_replacement_d2_078}


def vb_replacement_d2_079(vb_replacement_079):
    feature = _clean(vb_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_079'] = {'inputs': ['vb_replacement_079'], 'func': vb_replacement_d2_079}


def vb_replacement_d2_080(vb_replacement_080):
    feature = _clean(vb_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_080'] = {'inputs': ['vb_replacement_080'], 'func': vb_replacement_d2_080}


def vb_replacement_d2_081(vb_replacement_081):
    feature = _clean(vb_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_081'] = {'inputs': ['vb_replacement_081'], 'func': vb_replacement_d2_081}


def vb_replacement_d2_082(vb_replacement_082):
    feature = _clean(vb_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_082'] = {'inputs': ['vb_replacement_082'], 'func': vb_replacement_d2_082}


def vb_replacement_d2_083(vb_replacement_083):
    feature = _clean(vb_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_083'] = {'inputs': ['vb_replacement_083'], 'func': vb_replacement_d2_083}


def vb_replacement_d2_084(vb_replacement_084):
    feature = _clean(vb_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_084'] = {'inputs': ['vb_replacement_084'], 'func': vb_replacement_d2_084}


def vb_replacement_d2_085(vb_replacement_085):
    feature = _clean(vb_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_085'] = {'inputs': ['vb_replacement_085'], 'func': vb_replacement_d2_085}


def vb_replacement_d2_086(vb_replacement_086):
    feature = _clean(vb_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_086'] = {'inputs': ['vb_replacement_086'], 'func': vb_replacement_d2_086}


def vb_replacement_d2_087(vb_replacement_087):
    feature = _clean(vb_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_087'] = {'inputs': ['vb_replacement_087'], 'func': vb_replacement_d2_087}


def vb_replacement_d2_088(vb_replacement_088):
    feature = _clean(vb_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_088'] = {'inputs': ['vb_replacement_088'], 'func': vb_replacement_d2_088}


def vb_replacement_d2_089(vb_replacement_089):
    feature = _clean(vb_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_089'] = {'inputs': ['vb_replacement_089'], 'func': vb_replacement_d2_089}


def vb_replacement_d2_090(vb_replacement_090):
    feature = _clean(vb_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_090'] = {'inputs': ['vb_replacement_090'], 'func': vb_replacement_d2_090}


def vb_replacement_d2_091(vb_replacement_091):
    feature = _clean(vb_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_091'] = {'inputs': ['vb_replacement_091'], 'func': vb_replacement_d2_091}


def vb_replacement_d2_092(vb_replacement_092):
    feature = _clean(vb_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_092'] = {'inputs': ['vb_replacement_092'], 'func': vb_replacement_d2_092}


def vb_replacement_d2_093(vb_replacement_093):
    feature = _clean(vb_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_093'] = {'inputs': ['vb_replacement_093'], 'func': vb_replacement_d2_093}


def vb_replacement_d2_094(vb_replacement_094):
    feature = _clean(vb_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_094'] = {'inputs': ['vb_replacement_094'], 'func': vb_replacement_d2_094}


def vb_replacement_d2_095(vb_replacement_095):
    feature = _clean(vb_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_095'] = {'inputs': ['vb_replacement_095'], 'func': vb_replacement_d2_095}


def vb_replacement_d2_096(vb_replacement_096):
    feature = _clean(vb_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_096'] = {'inputs': ['vb_replacement_096'], 'func': vb_replacement_d2_096}


def vb_replacement_d2_097(vb_replacement_097):
    feature = _clean(vb_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_097'] = {'inputs': ['vb_replacement_097'], 'func': vb_replacement_d2_097}


def vb_replacement_d2_098(vb_replacement_098):
    feature = _clean(vb_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_098'] = {'inputs': ['vb_replacement_098'], 'func': vb_replacement_d2_098}


def vb_replacement_d2_099(vb_replacement_099):
    feature = _clean(vb_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_099'] = {'inputs': ['vb_replacement_099'], 'func': vb_replacement_d2_099}


def vb_replacement_d2_100(vb_replacement_100):
    feature = _clean(vb_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_100'] = {'inputs': ['vb_replacement_100'], 'func': vb_replacement_d2_100}


def vb_replacement_d2_101(vb_replacement_101):
    feature = _clean(vb_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_101'] = {'inputs': ['vb_replacement_101'], 'func': vb_replacement_d2_101}


def vb_replacement_d2_102(vb_replacement_102):
    feature = _clean(vb_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_102'] = {'inputs': ['vb_replacement_102'], 'func': vb_replacement_d2_102}


def vb_replacement_d2_103(vb_replacement_103):
    feature = _clean(vb_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_103'] = {'inputs': ['vb_replacement_103'], 'func': vb_replacement_d2_103}


def vb_replacement_d2_104(vb_replacement_104):
    feature = _clean(vb_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_104'] = {'inputs': ['vb_replacement_104'], 'func': vb_replacement_d2_104}


def vb_replacement_d2_105(vb_replacement_105):
    feature = _clean(vb_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_105'] = {'inputs': ['vb_replacement_105'], 'func': vb_replacement_d2_105}


def vb_replacement_d2_106(vb_replacement_106):
    feature = _clean(vb_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_106'] = {'inputs': ['vb_replacement_106'], 'func': vb_replacement_d2_106}


def vb_replacement_d2_107(vb_replacement_107):
    feature = _clean(vb_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_107'] = {'inputs': ['vb_replacement_107'], 'func': vb_replacement_d2_107}


def vb_replacement_d2_108(vb_replacement_108):
    feature = _clean(vb_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_108'] = {'inputs': ['vb_replacement_108'], 'func': vb_replacement_d2_108}


def vb_replacement_d2_109(vb_replacement_109):
    feature = _clean(vb_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_109'] = {'inputs': ['vb_replacement_109'], 'func': vb_replacement_d2_109}


def vb_replacement_d2_110(vb_replacement_110):
    feature = _clean(vb_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_110'] = {'inputs': ['vb_replacement_110'], 'func': vb_replacement_d2_110}


def vb_replacement_d2_111(vb_replacement_111):
    feature = _clean(vb_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_111'] = {'inputs': ['vb_replacement_111'], 'func': vb_replacement_d2_111}


def vb_replacement_d2_112(vb_replacement_112):
    feature = _clean(vb_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_112'] = {'inputs': ['vb_replacement_112'], 'func': vb_replacement_d2_112}


def vb_replacement_d2_113(vb_replacement_113):
    feature = _clean(vb_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_113'] = {'inputs': ['vb_replacement_113'], 'func': vb_replacement_d2_113}


def vb_replacement_d2_114(vb_replacement_114):
    feature = _clean(vb_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_114'] = {'inputs': ['vb_replacement_114'], 'func': vb_replacement_d2_114}


def vb_replacement_d2_115(vb_replacement_115):
    feature = _clean(vb_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_115'] = {'inputs': ['vb_replacement_115'], 'func': vb_replacement_d2_115}


def vb_replacement_d2_116(vb_replacement_116):
    feature = _clean(vb_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_116'] = {'inputs': ['vb_replacement_116'], 'func': vb_replacement_d2_116}


def vb_replacement_d2_117(vb_replacement_117):
    feature = _clean(vb_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_117'] = {'inputs': ['vb_replacement_117'], 'func': vb_replacement_d2_117}


def vb_replacement_d2_118(vb_replacement_118):
    feature = _clean(vb_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_118'] = {'inputs': ['vb_replacement_118'], 'func': vb_replacement_d2_118}


def vb_replacement_d2_119(vb_replacement_119):
    feature = _clean(vb_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_119'] = {'inputs': ['vb_replacement_119'], 'func': vb_replacement_d2_119}


def vb_replacement_d2_120(vb_replacement_120):
    feature = _clean(vb_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_120'] = {'inputs': ['vb_replacement_120'], 'func': vb_replacement_d2_120}


def vb_replacement_d2_121(vb_replacement_121):
    feature = _clean(vb_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_121'] = {'inputs': ['vb_replacement_121'], 'func': vb_replacement_d2_121}


def vb_replacement_d2_122(vb_replacement_122):
    feature = _clean(vb_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_122'] = {'inputs': ['vb_replacement_122'], 'func': vb_replacement_d2_122}


def vb_replacement_d2_123(vb_replacement_123):
    feature = _clean(vb_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_123'] = {'inputs': ['vb_replacement_123'], 'func': vb_replacement_d2_123}


def vb_replacement_d2_124(vb_replacement_124):
    feature = _clean(vb_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_124'] = {'inputs': ['vb_replacement_124'], 'func': vb_replacement_d2_124}


def vb_replacement_d2_125(vb_replacement_125):
    feature = _clean(vb_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_125'] = {'inputs': ['vb_replacement_125'], 'func': vb_replacement_d2_125}


def vb_replacement_d2_126(vb_replacement_126):
    feature = _clean(vb_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_126'] = {'inputs': ['vb_replacement_126'], 'func': vb_replacement_d2_126}


def vb_replacement_d2_127(vb_replacement_127):
    feature = _clean(vb_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_127'] = {'inputs': ['vb_replacement_127'], 'func': vb_replacement_d2_127}


def vb_replacement_d2_128(vb_replacement_128):
    feature = _clean(vb_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_128'] = {'inputs': ['vb_replacement_128'], 'func': vb_replacement_d2_128}


def vb_replacement_d2_129(vb_replacement_129):
    feature = _clean(vb_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_129'] = {'inputs': ['vb_replacement_129'], 'func': vb_replacement_d2_129}


def vb_replacement_d2_130(vb_replacement_130):
    feature = _clean(vb_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_130'] = {'inputs': ['vb_replacement_130'], 'func': vb_replacement_d2_130}


def vb_replacement_d2_131(vb_replacement_131):
    feature = _clean(vb_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_131'] = {'inputs': ['vb_replacement_131'], 'func': vb_replacement_d2_131}


def vb_replacement_d2_132(vb_replacement_132):
    feature = _clean(vb_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_132'] = {'inputs': ['vb_replacement_132'], 'func': vb_replacement_d2_132}


def vb_replacement_d2_133(vb_replacement_133):
    feature = _clean(vb_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_133'] = {'inputs': ['vb_replacement_133'], 'func': vb_replacement_d2_133}


def vb_replacement_d2_134(vb_replacement_134):
    feature = _clean(vb_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_134'] = {'inputs': ['vb_replacement_134'], 'func': vb_replacement_d2_134}


def vb_replacement_d2_135(vb_replacement_135):
    feature = _clean(vb_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_135'] = {'inputs': ['vb_replacement_135'], 'func': vb_replacement_d2_135}


def vb_replacement_d2_136(vb_replacement_136):
    feature = _clean(vb_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_136'] = {'inputs': ['vb_replacement_136'], 'func': vb_replacement_d2_136}


def vb_replacement_d2_137(vb_replacement_137):
    feature = _clean(vb_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_137'] = {'inputs': ['vb_replacement_137'], 'func': vb_replacement_d2_137}


def vb_replacement_d2_138(vb_replacement_138):
    feature = _clean(vb_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_138'] = {'inputs': ['vb_replacement_138'], 'func': vb_replacement_d2_138}


def vb_replacement_d2_139(vb_replacement_139):
    feature = _clean(vb_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_139'] = {'inputs': ['vb_replacement_139'], 'func': vb_replacement_d2_139}


def vb_replacement_d2_140(vb_replacement_140):
    feature = _clean(vb_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_140'] = {'inputs': ['vb_replacement_140'], 'func': vb_replacement_d2_140}


def vb_replacement_d2_141(vb_replacement_141):
    feature = _clean(vb_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_141'] = {'inputs': ['vb_replacement_141'], 'func': vb_replacement_d2_141}


def vb_replacement_d2_142(vb_replacement_142):
    feature = _clean(vb_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_142'] = {'inputs': ['vb_replacement_142'], 'func': vb_replacement_d2_142}


def vb_replacement_d2_143(vb_replacement_143):
    feature = _clean(vb_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_143'] = {'inputs': ['vb_replacement_143'], 'func': vb_replacement_d2_143}


def vb_replacement_d2_144(vb_replacement_144):
    feature = _clean(vb_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_144'] = {'inputs': ['vb_replacement_144'], 'func': vb_replacement_d2_144}


def vb_replacement_d2_145(vb_replacement_145):
    feature = _clean(vb_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_145'] = {'inputs': ['vb_replacement_145'], 'func': vb_replacement_d2_145}


def vb_replacement_d2_146(vb_replacement_146):
    feature = _clean(vb_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_146'] = {'inputs': ['vb_replacement_146'], 'func': vb_replacement_d2_146}


def vb_replacement_d2_147(vb_replacement_147):
    feature = _clean(vb_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_147'] = {'inputs': ['vb_replacement_147'], 'func': vb_replacement_d2_147}


def vb_replacement_d2_148(vb_replacement_148):
    feature = _clean(vb_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_148'] = {'inputs': ['vb_replacement_148'], 'func': vb_replacement_d2_148}


def vb_replacement_d2_149(vb_replacement_149):
    feature = _clean(vb_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_149'] = {'inputs': ['vb_replacement_149'], 'func': vb_replacement_d2_149}


def vb_replacement_d2_150(vb_replacement_150):
    feature = _clean(vb_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_150'] = {'inputs': ['vb_replacement_150'], 'func': vb_replacement_d2_150}


def vb_replacement_d2_151(vb_replacement_151):
    feature = _clean(vb_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_151'] = {'inputs': ['vb_replacement_151'], 'func': vb_replacement_d2_151}


def vb_replacement_d2_152(vb_replacement_152):
    feature = _clean(vb_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_152'] = {'inputs': ['vb_replacement_152'], 'func': vb_replacement_d2_152}


def vb_replacement_d2_153(vb_replacement_153):
    feature = _clean(vb_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_153'] = {'inputs': ['vb_replacement_153'], 'func': vb_replacement_d2_153}


def vb_replacement_d2_154(vb_replacement_154):
    feature = _clean(vb_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_154'] = {'inputs': ['vb_replacement_154'], 'func': vb_replacement_d2_154}


def vb_replacement_d2_155(vb_replacement_155):
    feature = _clean(vb_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_155'] = {'inputs': ['vb_replacement_155'], 'func': vb_replacement_d2_155}


def vb_replacement_d2_156(vb_replacement_156):
    feature = _clean(vb_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_156'] = {'inputs': ['vb_replacement_156'], 'func': vb_replacement_d2_156}


def vb_replacement_d2_157(vb_replacement_157):
    feature = _clean(vb_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_157'] = {'inputs': ['vb_replacement_157'], 'func': vb_replacement_d2_157}


def vb_replacement_d2_158(vb_replacement_158):
    feature = _clean(vb_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_158'] = {'inputs': ['vb_replacement_158'], 'func': vb_replacement_d2_158}


def vb_replacement_d2_159(vb_replacement_159):
    feature = _clean(vb_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_159'] = {'inputs': ['vb_replacement_159'], 'func': vb_replacement_d2_159}


def vb_replacement_d2_160(vb_replacement_160):
    feature = _clean(vb_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
VB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vb_replacement_d2_160'] = {'inputs': ['vb_replacement_160'], 'func': vb_replacement_d2_160}


# Base-universe derivative extensions for repaired first-base features.
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def vb_base_universe_d2_001_vb_002_volume_zscore_10_002(vb_002_volume_zscore_10_002):
    return _base_universe_d2(vb_002_volume_zscore_10_002, 1)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_001_vb_002_volume_zscore_10_002'] = {'inputs': ['vb_002_volume_zscore_10_002'], 'func': vb_base_universe_d2_001_vb_002_volume_zscore_10_002}


def vb_base_universe_d2_002_vb_003_down_volume_share_21_003(vb_003_down_volume_share_21_003):
    return _base_universe_d2(vb_003_down_volume_share_21_003, 2)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_002_vb_003_down_volume_share_21_003'] = {'inputs': ['vb_003_down_volume_share_21_003'], 'func': vb_base_universe_d2_002_vb_003_down_volume_share_21_003}


def vb_base_universe_d2_003_vb_004_dollar_volume_shock_42_004(vb_004_dollar_volume_shock_42_004):
    return _base_universe_d2(vb_004_dollar_volume_shock_42_004, 3)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_003_vb_004_dollar_volume_shock_42_004'] = {'inputs': ['vb_004_dollar_volume_shock_42_004'], 'func': vb_base_universe_d2_003_vb_004_dollar_volume_shock_42_004}


def vb_base_universe_d2_004_vb_005_volume_trend_slope_63_005(vb_005_volume_trend_slope_63_005):
    return _base_universe_d2(vb_005_volume_trend_slope_63_005, 4)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_004_vb_005_volume_trend_slope_63_005'] = {'inputs': ['vb_005_volume_trend_slope_63_005'], 'func': vb_base_universe_d2_004_vb_005_volume_trend_slope_63_005}


def vb_base_universe_d2_005_vb_006_price_volume_divergence_84_006(vb_006_price_volume_divergence_84_006):
    return _base_universe_d2(vb_006_price_volume_divergence_84_006, 5)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_005_vb_006_price_volume_divergence_84_006'] = {'inputs': ['vb_006_price_volume_divergence_84_006'], 'func': vb_base_universe_d2_005_vb_006_price_volume_divergence_84_006}


def vb_base_universe_d2_006_vb_008_volume_zscore_189_008(vb_008_volume_zscore_189_008):
    return _base_universe_d2(vb_008_volume_zscore_189_008, 6)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_006_vb_008_volume_zscore_189_008'] = {'inputs': ['vb_008_volume_zscore_189_008'], 'func': vb_base_universe_d2_006_vb_008_volume_zscore_189_008}


def vb_base_universe_d2_007_vb_009_down_volume_share_252_009(vb_009_down_volume_share_252_009):
    return _base_universe_d2(vb_009_down_volume_share_252_009, 7)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_007_vb_009_down_volume_share_252_009'] = {'inputs': ['vb_009_down_volume_share_252_009'], 'func': vb_base_universe_d2_007_vb_009_down_volume_share_252_009}


def vb_base_universe_d2_008_vb_010_dollar_volume_shock_378_010(vb_010_dollar_volume_shock_378_010):
    return _base_universe_d2(vb_010_dollar_volume_shock_378_010, 8)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_008_vb_010_dollar_volume_shock_378_010'] = {'inputs': ['vb_010_dollar_volume_shock_378_010'], 'func': vb_base_universe_d2_008_vb_010_dollar_volume_shock_378_010}


def vb_base_universe_d2_009_vb_011_volume_trend_slope_504_011(vb_011_volume_trend_slope_504_011):
    return _base_universe_d2(vb_011_volume_trend_slope_504_011, 9)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_009_vb_011_volume_trend_slope_504_011'] = {'inputs': ['vb_011_volume_trend_slope_504_011'], 'func': vb_base_universe_d2_009_vb_011_volume_trend_slope_504_011}


def vb_base_universe_d2_010_vb_012_price_volume_divergence_756_012(vb_012_price_volume_divergence_756_012):
    return _base_universe_d2(vb_012_price_volume_divergence_756_012, 10)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_010_vb_012_price_volume_divergence_756_012'] = {'inputs': ['vb_012_price_volume_divergence_756_012'], 'func': vb_base_universe_d2_010_vb_012_price_volume_divergence_756_012}


def vb_base_universe_d2_011_vb_014_volume_zscore_1260_014(vb_014_volume_zscore_1260_014):
    return _base_universe_d2(vb_014_volume_zscore_1260_014, 11)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_011_vb_014_volume_zscore_1260_014'] = {'inputs': ['vb_014_volume_zscore_1260_014'], 'func': vb_base_universe_d2_011_vb_014_volume_zscore_1260_014}


def vb_base_universe_d2_012_vb_015_down_volume_share_1512_015(vb_015_down_volume_share_1512_015):
    return _base_universe_d2(vb_015_down_volume_share_1512_015, 12)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_012_vb_015_down_volume_share_1512_015'] = {'inputs': ['vb_015_down_volume_share_1512_015'], 'func': vb_base_universe_d2_012_vb_015_down_volume_share_1512_015}


def vb_base_universe_d2_013_vb_016_dollar_volume_shock_5_016(vb_016_dollar_volume_shock_5_016):
    return _base_universe_d2(vb_016_dollar_volume_shock_5_016, 13)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_013_vb_016_dollar_volume_shock_5_016'] = {'inputs': ['vb_016_dollar_volume_shock_5_016'], 'func': vb_base_universe_d2_013_vb_016_dollar_volume_shock_5_016}


def vb_base_universe_d2_014_vb_017_volume_trend_slope_10_017(vb_017_volume_trend_slope_10_017):
    return _base_universe_d2(vb_017_volume_trend_slope_10_017, 14)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_014_vb_017_volume_trend_slope_10_017'] = {'inputs': ['vb_017_volume_trend_slope_10_017'], 'func': vb_base_universe_d2_014_vb_017_volume_trend_slope_10_017}


def vb_base_universe_d2_015_vb_018_price_volume_divergence_21_018(vb_018_price_volume_divergence_21_018):
    return _base_universe_d2(vb_018_price_volume_divergence_21_018, 15)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_015_vb_018_price_volume_divergence_21_018'] = {'inputs': ['vb_018_price_volume_divergence_21_018'], 'func': vb_base_universe_d2_015_vb_018_price_volume_divergence_21_018}


def vb_base_universe_d2_016_vb_020_volume_zscore_63_020(vb_020_volume_zscore_63_020):
    return _base_universe_d2(vb_020_volume_zscore_63_020, 16)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_016_vb_020_volume_zscore_63_020'] = {'inputs': ['vb_020_volume_zscore_63_020'], 'func': vb_base_universe_d2_016_vb_020_volume_zscore_63_020}


def vb_base_universe_d2_017_vb_021_down_volume_share_84_021(vb_021_down_volume_share_84_021):
    return _base_universe_d2(vb_021_down_volume_share_84_021, 17)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_017_vb_021_down_volume_share_84_021'] = {'inputs': ['vb_021_down_volume_share_84_021'], 'func': vb_base_universe_d2_017_vb_021_down_volume_share_84_021}


def vb_base_universe_d2_018_vb_022_dollar_volume_shock_126_022(vb_022_dollar_volume_shock_126_022):
    return _base_universe_d2(vb_022_dollar_volume_shock_126_022, 18)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_018_vb_022_dollar_volume_shock_126_022'] = {'inputs': ['vb_022_dollar_volume_shock_126_022'], 'func': vb_base_universe_d2_018_vb_022_dollar_volume_shock_126_022}


def vb_base_universe_d2_019_vb_023_volume_trend_slope_189_023(vb_023_volume_trend_slope_189_023):
    return _base_universe_d2(vb_023_volume_trend_slope_189_023, 19)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_019_vb_023_volume_trend_slope_189_023'] = {'inputs': ['vb_023_volume_trend_slope_189_023'], 'func': vb_base_universe_d2_019_vb_023_volume_trend_slope_189_023}


def vb_base_universe_d2_020_vb_024_price_volume_divergence_252_024(vb_024_price_volume_divergence_252_024):
    return _base_universe_d2(vb_024_price_volume_divergence_252_024, 20)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_020_vb_024_price_volume_divergence_252_024'] = {'inputs': ['vb_024_price_volume_divergence_252_024'], 'func': vb_base_universe_d2_020_vb_024_price_volume_divergence_252_024}


def vb_base_universe_d2_021_vb_026_volume_zscore_504_026(vb_026_volume_zscore_504_026):
    return _base_universe_d2(vb_026_volume_zscore_504_026, 21)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_021_vb_026_volume_zscore_504_026'] = {'inputs': ['vb_026_volume_zscore_504_026'], 'func': vb_base_universe_d2_021_vb_026_volume_zscore_504_026}


def vb_base_universe_d2_022_vb_027_down_volume_share_756_027(vb_027_down_volume_share_756_027):
    return _base_universe_d2(vb_027_down_volume_share_756_027, 22)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_022_vb_027_down_volume_share_756_027'] = {'inputs': ['vb_027_down_volume_share_756_027'], 'func': vb_base_universe_d2_022_vb_027_down_volume_share_756_027}


def vb_base_universe_d2_023_vb_028_dollar_volume_shock_1008_028(vb_028_dollar_volume_shock_1008_028):
    return _base_universe_d2(vb_028_dollar_volume_shock_1008_028, 23)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_023_vb_028_dollar_volume_shock_1008_028'] = {'inputs': ['vb_028_dollar_volume_shock_1008_028'], 'func': vb_base_universe_d2_023_vb_028_dollar_volume_shock_1008_028}


def vb_base_universe_d2_024_vb_029_volume_trend_slope_1260_029(vb_029_volume_trend_slope_1260_029):
    return _base_universe_d2(vb_029_volume_trend_slope_1260_029, 24)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_024_vb_029_volume_trend_slope_1260_029'] = {'inputs': ['vb_029_volume_trend_slope_1260_029'], 'func': vb_base_universe_d2_024_vb_029_volume_trend_slope_1260_029}


def vb_base_universe_d2_025_vb_030_price_volume_divergence_1512_030(vb_030_price_volume_divergence_1512_030):
    return _base_universe_d2(vb_030_price_volume_divergence_1512_030, 25)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_025_vb_030_price_volume_divergence_1512_030'] = {'inputs': ['vb_030_price_volume_divergence_1512_030'], 'func': vb_base_universe_d2_025_vb_030_price_volume_divergence_1512_030}


def vb_base_universe_d2_026_vb_basefill_031(vb_basefill_031):
    return _base_universe_d2(vb_basefill_031, 26)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_026_vb_basefill_031'] = {'inputs': ['vb_basefill_031'], 'func': vb_base_universe_d2_026_vb_basefill_031}


def vb_base_universe_d2_027_vb_basefill_032(vb_basefill_032):
    return _base_universe_d2(vb_basefill_032, 27)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_027_vb_basefill_032'] = {'inputs': ['vb_basefill_032'], 'func': vb_base_universe_d2_027_vb_basefill_032}


def vb_base_universe_d2_028_vb_basefill_033(vb_basefill_033):
    return _base_universe_d2(vb_basefill_033, 28)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_028_vb_basefill_033'] = {'inputs': ['vb_basefill_033'], 'func': vb_base_universe_d2_028_vb_basefill_033}


def vb_base_universe_d2_029_vb_basefill_034(vb_basefill_034):
    return _base_universe_d2(vb_basefill_034, 29)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_029_vb_basefill_034'] = {'inputs': ['vb_basefill_034'], 'func': vb_base_universe_d2_029_vb_basefill_034}


def vb_base_universe_d2_030_vb_basefill_035(vb_basefill_035):
    return _base_universe_d2(vb_basefill_035, 30)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_030_vb_basefill_035'] = {'inputs': ['vb_basefill_035'], 'func': vb_base_universe_d2_030_vb_basefill_035}


def vb_base_universe_d2_031_vb_basefill_036(vb_basefill_036):
    return _base_universe_d2(vb_basefill_036, 31)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_031_vb_basefill_036'] = {'inputs': ['vb_basefill_036'], 'func': vb_base_universe_d2_031_vb_basefill_036}


def vb_base_universe_d2_032_vb_basefill_037(vb_basefill_037):
    return _base_universe_d2(vb_basefill_037, 32)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_032_vb_basefill_037'] = {'inputs': ['vb_basefill_037'], 'func': vb_base_universe_d2_032_vb_basefill_037}


def vb_base_universe_d2_033_vb_basefill_038(vb_basefill_038):
    return _base_universe_d2(vb_basefill_038, 33)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_033_vb_basefill_038'] = {'inputs': ['vb_basefill_038'], 'func': vb_base_universe_d2_033_vb_basefill_038}


def vb_base_universe_d2_034_vb_basefill_039(vb_basefill_039):
    return _base_universe_d2(vb_basefill_039, 34)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_034_vb_basefill_039'] = {'inputs': ['vb_basefill_039'], 'func': vb_base_universe_d2_034_vb_basefill_039}


def vb_base_universe_d2_035_vb_basefill_040(vb_basefill_040):
    return _base_universe_d2(vb_basefill_040, 35)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_035_vb_basefill_040'] = {'inputs': ['vb_basefill_040'], 'func': vb_base_universe_d2_035_vb_basefill_040}


def vb_base_universe_d2_036_vb_basefill_041(vb_basefill_041):
    return _base_universe_d2(vb_basefill_041, 36)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_036_vb_basefill_041'] = {'inputs': ['vb_basefill_041'], 'func': vb_base_universe_d2_036_vb_basefill_041}


def vb_base_universe_d2_037_vb_basefill_042(vb_basefill_042):
    return _base_universe_d2(vb_basefill_042, 37)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_037_vb_basefill_042'] = {'inputs': ['vb_basefill_042'], 'func': vb_base_universe_d2_037_vb_basefill_042}


def vb_base_universe_d2_038_vb_basefill_043(vb_basefill_043):
    return _base_universe_d2(vb_basefill_043, 38)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_038_vb_basefill_043'] = {'inputs': ['vb_basefill_043'], 'func': vb_base_universe_d2_038_vb_basefill_043}


def vb_base_universe_d2_039_vb_basefill_044(vb_basefill_044):
    return _base_universe_d2(vb_basefill_044, 39)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_039_vb_basefill_044'] = {'inputs': ['vb_basefill_044'], 'func': vb_base_universe_d2_039_vb_basefill_044}


def vb_base_universe_d2_040_vb_basefill_045(vb_basefill_045):
    return _base_universe_d2(vb_basefill_045, 40)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_040_vb_basefill_045'] = {'inputs': ['vb_basefill_045'], 'func': vb_base_universe_d2_040_vb_basefill_045}


def vb_base_universe_d2_041_vb_basefill_046(vb_basefill_046):
    return _base_universe_d2(vb_basefill_046, 41)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_041_vb_basefill_046'] = {'inputs': ['vb_basefill_046'], 'func': vb_base_universe_d2_041_vb_basefill_046}


def vb_base_universe_d2_042_vb_basefill_047(vb_basefill_047):
    return _base_universe_d2(vb_basefill_047, 42)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_042_vb_basefill_047'] = {'inputs': ['vb_basefill_047'], 'func': vb_base_universe_d2_042_vb_basefill_047}


def vb_base_universe_d2_043_vb_basefill_048(vb_basefill_048):
    return _base_universe_d2(vb_basefill_048, 43)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_043_vb_basefill_048'] = {'inputs': ['vb_basefill_048'], 'func': vb_base_universe_d2_043_vb_basefill_048}


def vb_base_universe_d2_044_vb_basefill_049(vb_basefill_049):
    return _base_universe_d2(vb_basefill_049, 44)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_044_vb_basefill_049'] = {'inputs': ['vb_basefill_049'], 'func': vb_base_universe_d2_044_vb_basefill_049}


def vb_base_universe_d2_045_vb_basefill_050(vb_basefill_050):
    return _base_universe_d2(vb_basefill_050, 45)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_045_vb_basefill_050'] = {'inputs': ['vb_basefill_050'], 'func': vb_base_universe_d2_045_vb_basefill_050}


def vb_base_universe_d2_046_vb_basefill_051(vb_basefill_051):
    return _base_universe_d2(vb_basefill_051, 46)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_046_vb_basefill_051'] = {'inputs': ['vb_basefill_051'], 'func': vb_base_universe_d2_046_vb_basefill_051}


def vb_base_universe_d2_047_vb_basefill_052(vb_basefill_052):
    return _base_universe_d2(vb_basefill_052, 47)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_047_vb_basefill_052'] = {'inputs': ['vb_basefill_052'], 'func': vb_base_universe_d2_047_vb_basefill_052}


def vb_base_universe_d2_048_vb_basefill_053(vb_basefill_053):
    return _base_universe_d2(vb_basefill_053, 48)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_048_vb_basefill_053'] = {'inputs': ['vb_basefill_053'], 'func': vb_base_universe_d2_048_vb_basefill_053}


def vb_base_universe_d2_049_vb_basefill_054(vb_basefill_054):
    return _base_universe_d2(vb_basefill_054, 49)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_049_vb_basefill_054'] = {'inputs': ['vb_basefill_054'], 'func': vb_base_universe_d2_049_vb_basefill_054}


def vb_base_universe_d2_050_vb_basefill_055(vb_basefill_055):
    return _base_universe_d2(vb_basefill_055, 50)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_050_vb_basefill_055'] = {'inputs': ['vb_basefill_055'], 'func': vb_base_universe_d2_050_vb_basefill_055}


def vb_base_universe_d2_051_vb_basefill_056(vb_basefill_056):
    return _base_universe_d2(vb_basefill_056, 51)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_051_vb_basefill_056'] = {'inputs': ['vb_basefill_056'], 'func': vb_base_universe_d2_051_vb_basefill_056}


def vb_base_universe_d2_052_vb_basefill_057(vb_basefill_057):
    return _base_universe_d2(vb_basefill_057, 52)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_052_vb_basefill_057'] = {'inputs': ['vb_basefill_057'], 'func': vb_base_universe_d2_052_vb_basefill_057}


def vb_base_universe_d2_053_vb_basefill_058(vb_basefill_058):
    return _base_universe_d2(vb_basefill_058, 53)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_053_vb_basefill_058'] = {'inputs': ['vb_basefill_058'], 'func': vb_base_universe_d2_053_vb_basefill_058}


def vb_base_universe_d2_054_vb_basefill_059(vb_basefill_059):
    return _base_universe_d2(vb_basefill_059, 54)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_054_vb_basefill_059'] = {'inputs': ['vb_basefill_059'], 'func': vb_base_universe_d2_054_vb_basefill_059}


def vb_base_universe_d2_055_vb_basefill_060(vb_basefill_060):
    return _base_universe_d2(vb_basefill_060, 55)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_055_vb_basefill_060'] = {'inputs': ['vb_basefill_060'], 'func': vb_base_universe_d2_055_vb_basefill_060}


def vb_base_universe_d2_056_vb_basefill_061(vb_basefill_061):
    return _base_universe_d2(vb_basefill_061, 56)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_056_vb_basefill_061'] = {'inputs': ['vb_basefill_061'], 'func': vb_base_universe_d2_056_vb_basefill_061}


def vb_base_universe_d2_057_vb_basefill_062(vb_basefill_062):
    return _base_universe_d2(vb_basefill_062, 57)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_057_vb_basefill_062'] = {'inputs': ['vb_basefill_062'], 'func': vb_base_universe_d2_057_vb_basefill_062}


def vb_base_universe_d2_058_vb_basefill_063(vb_basefill_063):
    return _base_universe_d2(vb_basefill_063, 58)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_058_vb_basefill_063'] = {'inputs': ['vb_basefill_063'], 'func': vb_base_universe_d2_058_vb_basefill_063}


def vb_base_universe_d2_059_vb_basefill_064(vb_basefill_064):
    return _base_universe_d2(vb_basefill_064, 59)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_059_vb_basefill_064'] = {'inputs': ['vb_basefill_064'], 'func': vb_base_universe_d2_059_vb_basefill_064}


def vb_base_universe_d2_060_vb_basefill_065(vb_basefill_065):
    return _base_universe_d2(vb_basefill_065, 60)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_060_vb_basefill_065'] = {'inputs': ['vb_basefill_065'], 'func': vb_base_universe_d2_060_vb_basefill_065}


def vb_base_universe_d2_061_vb_basefill_066(vb_basefill_066):
    return _base_universe_d2(vb_basefill_066, 61)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_061_vb_basefill_066'] = {'inputs': ['vb_basefill_066'], 'func': vb_base_universe_d2_061_vb_basefill_066}


def vb_base_universe_d2_062_vb_basefill_067(vb_basefill_067):
    return _base_universe_d2(vb_basefill_067, 62)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_062_vb_basefill_067'] = {'inputs': ['vb_basefill_067'], 'func': vb_base_universe_d2_062_vb_basefill_067}


def vb_base_universe_d2_063_vb_basefill_068(vb_basefill_068):
    return _base_universe_d2(vb_basefill_068, 63)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_063_vb_basefill_068'] = {'inputs': ['vb_basefill_068'], 'func': vb_base_universe_d2_063_vb_basefill_068}


def vb_base_universe_d2_064_vb_basefill_069(vb_basefill_069):
    return _base_universe_d2(vb_basefill_069, 64)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_064_vb_basefill_069'] = {'inputs': ['vb_basefill_069'], 'func': vb_base_universe_d2_064_vb_basefill_069}


def vb_base_universe_d2_065_vb_basefill_070(vb_basefill_070):
    return _base_universe_d2(vb_basefill_070, 65)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_065_vb_basefill_070'] = {'inputs': ['vb_basefill_070'], 'func': vb_base_universe_d2_065_vb_basefill_070}


def vb_base_universe_d2_066_vb_basefill_071(vb_basefill_071):
    return _base_universe_d2(vb_basefill_071, 66)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_066_vb_basefill_071'] = {'inputs': ['vb_basefill_071'], 'func': vb_base_universe_d2_066_vb_basefill_071}


def vb_base_universe_d2_067_vb_basefill_072(vb_basefill_072):
    return _base_universe_d2(vb_basefill_072, 67)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_067_vb_basefill_072'] = {'inputs': ['vb_basefill_072'], 'func': vb_base_universe_d2_067_vb_basefill_072}


def vb_base_universe_d2_068_vb_basefill_073(vb_basefill_073):
    return _base_universe_d2(vb_basefill_073, 68)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_068_vb_basefill_073'] = {'inputs': ['vb_basefill_073'], 'func': vb_base_universe_d2_068_vb_basefill_073}


def vb_base_universe_d2_069_vb_basefill_074(vb_basefill_074):
    return _base_universe_d2(vb_basefill_074, 69)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_069_vb_basefill_074'] = {'inputs': ['vb_basefill_074'], 'func': vb_base_universe_d2_069_vb_basefill_074}


def vb_base_universe_d2_070_vb_basefill_075(vb_basefill_075):
    return _base_universe_d2(vb_basefill_075, 70)
VB_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vb_base_universe_d2_070_vb_basefill_075'] = {'inputs': ['vb_basefill_075'], 'func': vb_base_universe_d2_070_vb_basefill_075}
