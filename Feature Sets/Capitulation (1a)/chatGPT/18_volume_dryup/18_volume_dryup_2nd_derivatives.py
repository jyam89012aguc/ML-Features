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



def vdry_151_vdry_001_volume_spike_ratio_5_001_roc_1(vdry_001_volume_spike_ratio_5_001):
    feature = _s(vdry_001_volume_spike_ratio_5_001)
    return (_roc(feature, 1)).reindex(feature.index)

def vdry_152_vdry_007_volume_spike_ratio_126_007_roc_5(vdry_007_volume_spike_ratio_126_007):
    feature = _s(vdry_007_volume_spike_ratio_126_007)
    return (_roc(feature, 5)).reindex(feature.index)

def vdry_153_vdry_013_volume_spike_ratio_1008_013_roc_42(vdry_013_volume_spike_ratio_1008_013):
    feature = _s(vdry_013_volume_spike_ratio_1008_013)
    return (_roc(feature, 42)).reindex(feature.index)

def vdry_154_vdry_019_volume_spike_ratio_42_019_roc_126(vdry_019_volume_spike_ratio_42_019):
    feature = _s(vdry_019_volume_spike_ratio_42_019)
    return (_roc(feature, 126)).reindex(feature.index)

def vdry_155_vdry_025_volume_spike_ratio_378_025_roc_378(vdry_025_volume_spike_ratio_378_025):
    feature = _s(vdry_025_volume_spike_ratio_378_025)
    return (_roc(feature, 378)).reindex(feature.index)






















VOLUME_DRYUP_REGISTRY_2ND_DERIVATIVES = {
    'vdry_151_vdry_001_volume_spike_ratio_5_001_roc_1': {'inputs': ['vdry_001_volume_spike_ratio_5_001'], 'func': vdry_151_vdry_001_volume_spike_ratio_5_001_roc_1},
    'vdry_152_vdry_007_volume_spike_ratio_126_007_roc_5': {'inputs': ['vdry_007_volume_spike_ratio_126_007'], 'func': vdry_152_vdry_007_volume_spike_ratio_126_007_roc_5},
    'vdry_153_vdry_013_volume_spike_ratio_1008_013_roc_42': {'inputs': ['vdry_013_volume_spike_ratio_1008_013'], 'func': vdry_153_vdry_013_volume_spike_ratio_1008_013_roc_42},
    'vdry_154_vdry_019_volume_spike_ratio_42_019_roc_126': {'inputs': ['vdry_019_volume_spike_ratio_42_019'], 'func': vdry_154_vdry_019_volume_spike_ratio_42_019_roc_126},
    'vdry_155_vdry_025_volume_spike_ratio_378_025_roc_378': {'inputs': ['vdry_025_volume_spike_ratio_378_025'], 'func': vdry_155_vdry_025_volume_spike_ratio_378_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def vd_replacement_d2_001(vd_replacement_001):
    feature = _clean(vd_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_001'] = {'inputs': ['vd_replacement_001'], 'func': vd_replacement_d2_001}


def vd_replacement_d2_002(vd_replacement_002):
    feature = _clean(vd_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_002'] = {'inputs': ['vd_replacement_002'], 'func': vd_replacement_d2_002}


def vd_replacement_d2_003(vd_replacement_003):
    feature = _clean(vd_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_003'] = {'inputs': ['vd_replacement_003'], 'func': vd_replacement_d2_003}


def vd_replacement_d2_004(vd_replacement_004):
    feature = _clean(vd_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_004'] = {'inputs': ['vd_replacement_004'], 'func': vd_replacement_d2_004}


def vd_replacement_d2_005(vd_replacement_005):
    feature = _clean(vd_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_005'] = {'inputs': ['vd_replacement_005'], 'func': vd_replacement_d2_005}


def vd_replacement_d2_006(vd_replacement_006):
    feature = _clean(vd_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_006'] = {'inputs': ['vd_replacement_006'], 'func': vd_replacement_d2_006}


def vd_replacement_d2_007(vd_replacement_007):
    feature = _clean(vd_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_007'] = {'inputs': ['vd_replacement_007'], 'func': vd_replacement_d2_007}


def vd_replacement_d2_008(vd_replacement_008):
    feature = _clean(vd_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_008'] = {'inputs': ['vd_replacement_008'], 'func': vd_replacement_d2_008}


def vd_replacement_d2_009(vd_replacement_009):
    feature = _clean(vd_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_009'] = {'inputs': ['vd_replacement_009'], 'func': vd_replacement_d2_009}


def vd_replacement_d2_010(vd_replacement_010):
    feature = _clean(vd_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_010'] = {'inputs': ['vd_replacement_010'], 'func': vd_replacement_d2_010}


def vd_replacement_d2_011(vd_replacement_011):
    feature = _clean(vd_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_011'] = {'inputs': ['vd_replacement_011'], 'func': vd_replacement_d2_011}


def vd_replacement_d2_012(vd_replacement_012):
    feature = _clean(vd_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_012'] = {'inputs': ['vd_replacement_012'], 'func': vd_replacement_d2_012}


def vd_replacement_d2_013(vd_replacement_013):
    feature = _clean(vd_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_013'] = {'inputs': ['vd_replacement_013'], 'func': vd_replacement_d2_013}


def vd_replacement_d2_014(vd_replacement_014):
    feature = _clean(vd_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_014'] = {'inputs': ['vd_replacement_014'], 'func': vd_replacement_d2_014}


def vd_replacement_d2_015(vd_replacement_015):
    feature = _clean(vd_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_015'] = {'inputs': ['vd_replacement_015'], 'func': vd_replacement_d2_015}


def vd_replacement_d2_016(vd_replacement_016):
    feature = _clean(vd_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_016'] = {'inputs': ['vd_replacement_016'], 'func': vd_replacement_d2_016}


def vd_replacement_d2_017(vd_replacement_017):
    feature = _clean(vd_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_017'] = {'inputs': ['vd_replacement_017'], 'func': vd_replacement_d2_017}


def vd_replacement_d2_018(vd_replacement_018):
    feature = _clean(vd_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_018'] = {'inputs': ['vd_replacement_018'], 'func': vd_replacement_d2_018}


def vd_replacement_d2_019(vd_replacement_019):
    feature = _clean(vd_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_019'] = {'inputs': ['vd_replacement_019'], 'func': vd_replacement_d2_019}


def vd_replacement_d2_020(vd_replacement_020):
    feature = _clean(vd_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_020'] = {'inputs': ['vd_replacement_020'], 'func': vd_replacement_d2_020}


def vd_replacement_d2_021(vd_replacement_021):
    feature = _clean(vd_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_021'] = {'inputs': ['vd_replacement_021'], 'func': vd_replacement_d2_021}


def vd_replacement_d2_022(vd_replacement_022):
    feature = _clean(vd_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_022'] = {'inputs': ['vd_replacement_022'], 'func': vd_replacement_d2_022}


def vd_replacement_d2_023(vd_replacement_023):
    feature = _clean(vd_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_023'] = {'inputs': ['vd_replacement_023'], 'func': vd_replacement_d2_023}


def vd_replacement_d2_024(vd_replacement_024):
    feature = _clean(vd_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_024'] = {'inputs': ['vd_replacement_024'], 'func': vd_replacement_d2_024}


def vd_replacement_d2_025(vd_replacement_025):
    feature = _clean(vd_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_025'] = {'inputs': ['vd_replacement_025'], 'func': vd_replacement_d2_025}


def vd_replacement_d2_026(vd_replacement_026):
    feature = _clean(vd_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_026'] = {'inputs': ['vd_replacement_026'], 'func': vd_replacement_d2_026}


def vd_replacement_d2_027(vd_replacement_027):
    feature = _clean(vd_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_027'] = {'inputs': ['vd_replacement_027'], 'func': vd_replacement_d2_027}


def vd_replacement_d2_028(vd_replacement_028):
    feature = _clean(vd_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_028'] = {'inputs': ['vd_replacement_028'], 'func': vd_replacement_d2_028}


def vd_replacement_d2_029(vd_replacement_029):
    feature = _clean(vd_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_029'] = {'inputs': ['vd_replacement_029'], 'func': vd_replacement_d2_029}


def vd_replacement_d2_030(vd_replacement_030):
    feature = _clean(vd_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_030'] = {'inputs': ['vd_replacement_030'], 'func': vd_replacement_d2_030}


def vd_replacement_d2_031(vd_replacement_031):
    feature = _clean(vd_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_031'] = {'inputs': ['vd_replacement_031'], 'func': vd_replacement_d2_031}


def vd_replacement_d2_032(vd_replacement_032):
    feature = _clean(vd_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_032'] = {'inputs': ['vd_replacement_032'], 'func': vd_replacement_d2_032}


def vd_replacement_d2_033(vd_replacement_033):
    feature = _clean(vd_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_033'] = {'inputs': ['vd_replacement_033'], 'func': vd_replacement_d2_033}


def vd_replacement_d2_034(vd_replacement_034):
    feature = _clean(vd_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_034'] = {'inputs': ['vd_replacement_034'], 'func': vd_replacement_d2_034}


def vd_replacement_d2_035(vd_replacement_035):
    feature = _clean(vd_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_035'] = {'inputs': ['vd_replacement_035'], 'func': vd_replacement_d2_035}


def vd_replacement_d2_036(vd_replacement_036):
    feature = _clean(vd_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_036'] = {'inputs': ['vd_replacement_036'], 'func': vd_replacement_d2_036}


def vd_replacement_d2_037(vd_replacement_037):
    feature = _clean(vd_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_037'] = {'inputs': ['vd_replacement_037'], 'func': vd_replacement_d2_037}


def vd_replacement_d2_038(vd_replacement_038):
    feature = _clean(vd_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_038'] = {'inputs': ['vd_replacement_038'], 'func': vd_replacement_d2_038}


def vd_replacement_d2_039(vd_replacement_039):
    feature = _clean(vd_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_039'] = {'inputs': ['vd_replacement_039'], 'func': vd_replacement_d2_039}


def vd_replacement_d2_040(vd_replacement_040):
    feature = _clean(vd_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_040'] = {'inputs': ['vd_replacement_040'], 'func': vd_replacement_d2_040}


def vd_replacement_d2_041(vd_replacement_041):
    feature = _clean(vd_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_041'] = {'inputs': ['vd_replacement_041'], 'func': vd_replacement_d2_041}


def vd_replacement_d2_042(vd_replacement_042):
    feature = _clean(vd_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_042'] = {'inputs': ['vd_replacement_042'], 'func': vd_replacement_d2_042}


def vd_replacement_d2_043(vd_replacement_043):
    feature = _clean(vd_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_043'] = {'inputs': ['vd_replacement_043'], 'func': vd_replacement_d2_043}


def vd_replacement_d2_044(vd_replacement_044):
    feature = _clean(vd_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_044'] = {'inputs': ['vd_replacement_044'], 'func': vd_replacement_d2_044}


def vd_replacement_d2_045(vd_replacement_045):
    feature = _clean(vd_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_045'] = {'inputs': ['vd_replacement_045'], 'func': vd_replacement_d2_045}


def vd_replacement_d2_046(vd_replacement_046):
    feature = _clean(vd_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_046'] = {'inputs': ['vd_replacement_046'], 'func': vd_replacement_d2_046}


def vd_replacement_d2_047(vd_replacement_047):
    feature = _clean(vd_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_047'] = {'inputs': ['vd_replacement_047'], 'func': vd_replacement_d2_047}


def vd_replacement_d2_048(vd_replacement_048):
    feature = _clean(vd_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_048'] = {'inputs': ['vd_replacement_048'], 'func': vd_replacement_d2_048}


def vd_replacement_d2_049(vd_replacement_049):
    feature = _clean(vd_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_049'] = {'inputs': ['vd_replacement_049'], 'func': vd_replacement_d2_049}


def vd_replacement_d2_050(vd_replacement_050):
    feature = _clean(vd_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_050'] = {'inputs': ['vd_replacement_050'], 'func': vd_replacement_d2_050}


def vd_replacement_d2_051(vd_replacement_051):
    feature = _clean(vd_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_051'] = {'inputs': ['vd_replacement_051'], 'func': vd_replacement_d2_051}


def vd_replacement_d2_052(vd_replacement_052):
    feature = _clean(vd_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_052'] = {'inputs': ['vd_replacement_052'], 'func': vd_replacement_d2_052}


def vd_replacement_d2_053(vd_replacement_053):
    feature = _clean(vd_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_053'] = {'inputs': ['vd_replacement_053'], 'func': vd_replacement_d2_053}


def vd_replacement_d2_054(vd_replacement_054):
    feature = _clean(vd_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_054'] = {'inputs': ['vd_replacement_054'], 'func': vd_replacement_d2_054}


def vd_replacement_d2_055(vd_replacement_055):
    feature = _clean(vd_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_055'] = {'inputs': ['vd_replacement_055'], 'func': vd_replacement_d2_055}


def vd_replacement_d2_056(vd_replacement_056):
    feature = _clean(vd_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_056'] = {'inputs': ['vd_replacement_056'], 'func': vd_replacement_d2_056}


def vd_replacement_d2_057(vd_replacement_057):
    feature = _clean(vd_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_057'] = {'inputs': ['vd_replacement_057'], 'func': vd_replacement_d2_057}


def vd_replacement_d2_058(vd_replacement_058):
    feature = _clean(vd_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_058'] = {'inputs': ['vd_replacement_058'], 'func': vd_replacement_d2_058}


def vd_replacement_d2_059(vd_replacement_059):
    feature = _clean(vd_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_059'] = {'inputs': ['vd_replacement_059'], 'func': vd_replacement_d2_059}


def vd_replacement_d2_060(vd_replacement_060):
    feature = _clean(vd_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_060'] = {'inputs': ['vd_replacement_060'], 'func': vd_replacement_d2_060}


def vd_replacement_d2_061(vd_replacement_061):
    feature = _clean(vd_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_061'] = {'inputs': ['vd_replacement_061'], 'func': vd_replacement_d2_061}


def vd_replacement_d2_062(vd_replacement_062):
    feature = _clean(vd_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_062'] = {'inputs': ['vd_replacement_062'], 'func': vd_replacement_d2_062}


def vd_replacement_d2_063(vd_replacement_063):
    feature = _clean(vd_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_063'] = {'inputs': ['vd_replacement_063'], 'func': vd_replacement_d2_063}


def vd_replacement_d2_064(vd_replacement_064):
    feature = _clean(vd_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_064'] = {'inputs': ['vd_replacement_064'], 'func': vd_replacement_d2_064}


def vd_replacement_d2_065(vd_replacement_065):
    feature = _clean(vd_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_065'] = {'inputs': ['vd_replacement_065'], 'func': vd_replacement_d2_065}


def vd_replacement_d2_066(vd_replacement_066):
    feature = _clean(vd_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_066'] = {'inputs': ['vd_replacement_066'], 'func': vd_replacement_d2_066}


def vd_replacement_d2_067(vd_replacement_067):
    feature = _clean(vd_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_067'] = {'inputs': ['vd_replacement_067'], 'func': vd_replacement_d2_067}


def vd_replacement_d2_068(vd_replacement_068):
    feature = _clean(vd_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_068'] = {'inputs': ['vd_replacement_068'], 'func': vd_replacement_d2_068}


def vd_replacement_d2_069(vd_replacement_069):
    feature = _clean(vd_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_069'] = {'inputs': ['vd_replacement_069'], 'func': vd_replacement_d2_069}


def vd_replacement_d2_070(vd_replacement_070):
    feature = _clean(vd_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_070'] = {'inputs': ['vd_replacement_070'], 'func': vd_replacement_d2_070}


def vd_replacement_d2_071(vd_replacement_071):
    feature = _clean(vd_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_071'] = {'inputs': ['vd_replacement_071'], 'func': vd_replacement_d2_071}


def vd_replacement_d2_072(vd_replacement_072):
    feature = _clean(vd_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_072'] = {'inputs': ['vd_replacement_072'], 'func': vd_replacement_d2_072}


def vd_replacement_d2_073(vd_replacement_073):
    feature = _clean(vd_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_073'] = {'inputs': ['vd_replacement_073'], 'func': vd_replacement_d2_073}


def vd_replacement_d2_074(vd_replacement_074):
    feature = _clean(vd_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_074'] = {'inputs': ['vd_replacement_074'], 'func': vd_replacement_d2_074}


def vd_replacement_d2_075(vd_replacement_075):
    feature = _clean(vd_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_075'] = {'inputs': ['vd_replacement_075'], 'func': vd_replacement_d2_075}


def vd_replacement_d2_076(vd_replacement_076):
    feature = _clean(vd_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_076'] = {'inputs': ['vd_replacement_076'], 'func': vd_replacement_d2_076}


def vd_replacement_d2_077(vd_replacement_077):
    feature = _clean(vd_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_077'] = {'inputs': ['vd_replacement_077'], 'func': vd_replacement_d2_077}


def vd_replacement_d2_078(vd_replacement_078):
    feature = _clean(vd_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_078'] = {'inputs': ['vd_replacement_078'], 'func': vd_replacement_d2_078}


def vd_replacement_d2_079(vd_replacement_079):
    feature = _clean(vd_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_079'] = {'inputs': ['vd_replacement_079'], 'func': vd_replacement_d2_079}


def vd_replacement_d2_080(vd_replacement_080):
    feature = _clean(vd_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_080'] = {'inputs': ['vd_replacement_080'], 'func': vd_replacement_d2_080}


def vd_replacement_d2_081(vd_replacement_081):
    feature = _clean(vd_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_081'] = {'inputs': ['vd_replacement_081'], 'func': vd_replacement_d2_081}


def vd_replacement_d2_082(vd_replacement_082):
    feature = _clean(vd_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_082'] = {'inputs': ['vd_replacement_082'], 'func': vd_replacement_d2_082}


def vd_replacement_d2_083(vd_replacement_083):
    feature = _clean(vd_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_083'] = {'inputs': ['vd_replacement_083'], 'func': vd_replacement_d2_083}


def vd_replacement_d2_084(vd_replacement_084):
    feature = _clean(vd_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_084'] = {'inputs': ['vd_replacement_084'], 'func': vd_replacement_d2_084}


def vd_replacement_d2_085(vd_replacement_085):
    feature = _clean(vd_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_085'] = {'inputs': ['vd_replacement_085'], 'func': vd_replacement_d2_085}


def vd_replacement_d2_086(vd_replacement_086):
    feature = _clean(vd_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_086'] = {'inputs': ['vd_replacement_086'], 'func': vd_replacement_d2_086}


def vd_replacement_d2_087(vd_replacement_087):
    feature = _clean(vd_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_087'] = {'inputs': ['vd_replacement_087'], 'func': vd_replacement_d2_087}


def vd_replacement_d2_088(vd_replacement_088):
    feature = _clean(vd_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_088'] = {'inputs': ['vd_replacement_088'], 'func': vd_replacement_d2_088}


def vd_replacement_d2_089(vd_replacement_089):
    feature = _clean(vd_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_089'] = {'inputs': ['vd_replacement_089'], 'func': vd_replacement_d2_089}


def vd_replacement_d2_090(vd_replacement_090):
    feature = _clean(vd_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_090'] = {'inputs': ['vd_replacement_090'], 'func': vd_replacement_d2_090}


def vd_replacement_d2_091(vd_replacement_091):
    feature = _clean(vd_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_091'] = {'inputs': ['vd_replacement_091'], 'func': vd_replacement_d2_091}


def vd_replacement_d2_092(vd_replacement_092):
    feature = _clean(vd_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_092'] = {'inputs': ['vd_replacement_092'], 'func': vd_replacement_d2_092}


def vd_replacement_d2_093(vd_replacement_093):
    feature = _clean(vd_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_093'] = {'inputs': ['vd_replacement_093'], 'func': vd_replacement_d2_093}


def vd_replacement_d2_094(vd_replacement_094):
    feature = _clean(vd_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_094'] = {'inputs': ['vd_replacement_094'], 'func': vd_replacement_d2_094}


def vd_replacement_d2_095(vd_replacement_095):
    feature = _clean(vd_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_095'] = {'inputs': ['vd_replacement_095'], 'func': vd_replacement_d2_095}


def vd_replacement_d2_096(vd_replacement_096):
    feature = _clean(vd_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_096'] = {'inputs': ['vd_replacement_096'], 'func': vd_replacement_d2_096}


def vd_replacement_d2_097(vd_replacement_097):
    feature = _clean(vd_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_097'] = {'inputs': ['vd_replacement_097'], 'func': vd_replacement_d2_097}


def vd_replacement_d2_098(vd_replacement_098):
    feature = _clean(vd_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_098'] = {'inputs': ['vd_replacement_098'], 'func': vd_replacement_d2_098}


def vd_replacement_d2_099(vd_replacement_099):
    feature = _clean(vd_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_099'] = {'inputs': ['vd_replacement_099'], 'func': vd_replacement_d2_099}


def vd_replacement_d2_100(vd_replacement_100):
    feature = _clean(vd_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_100'] = {'inputs': ['vd_replacement_100'], 'func': vd_replacement_d2_100}


def vd_replacement_d2_101(vd_replacement_101):
    feature = _clean(vd_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_101'] = {'inputs': ['vd_replacement_101'], 'func': vd_replacement_d2_101}


def vd_replacement_d2_102(vd_replacement_102):
    feature = _clean(vd_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_102'] = {'inputs': ['vd_replacement_102'], 'func': vd_replacement_d2_102}


def vd_replacement_d2_103(vd_replacement_103):
    feature = _clean(vd_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_103'] = {'inputs': ['vd_replacement_103'], 'func': vd_replacement_d2_103}


def vd_replacement_d2_104(vd_replacement_104):
    feature = _clean(vd_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_104'] = {'inputs': ['vd_replacement_104'], 'func': vd_replacement_d2_104}


def vd_replacement_d2_105(vd_replacement_105):
    feature = _clean(vd_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_105'] = {'inputs': ['vd_replacement_105'], 'func': vd_replacement_d2_105}


def vd_replacement_d2_106(vd_replacement_106):
    feature = _clean(vd_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_106'] = {'inputs': ['vd_replacement_106'], 'func': vd_replacement_d2_106}


def vd_replacement_d2_107(vd_replacement_107):
    feature = _clean(vd_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_107'] = {'inputs': ['vd_replacement_107'], 'func': vd_replacement_d2_107}


def vd_replacement_d2_108(vd_replacement_108):
    feature = _clean(vd_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_108'] = {'inputs': ['vd_replacement_108'], 'func': vd_replacement_d2_108}


def vd_replacement_d2_109(vd_replacement_109):
    feature = _clean(vd_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_109'] = {'inputs': ['vd_replacement_109'], 'func': vd_replacement_d2_109}


def vd_replacement_d2_110(vd_replacement_110):
    feature = _clean(vd_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_110'] = {'inputs': ['vd_replacement_110'], 'func': vd_replacement_d2_110}


def vd_replacement_d2_111(vd_replacement_111):
    feature = _clean(vd_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_111'] = {'inputs': ['vd_replacement_111'], 'func': vd_replacement_d2_111}


def vd_replacement_d2_112(vd_replacement_112):
    feature = _clean(vd_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_112'] = {'inputs': ['vd_replacement_112'], 'func': vd_replacement_d2_112}


def vd_replacement_d2_113(vd_replacement_113):
    feature = _clean(vd_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_113'] = {'inputs': ['vd_replacement_113'], 'func': vd_replacement_d2_113}


def vd_replacement_d2_114(vd_replacement_114):
    feature = _clean(vd_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_114'] = {'inputs': ['vd_replacement_114'], 'func': vd_replacement_d2_114}


def vd_replacement_d2_115(vd_replacement_115):
    feature = _clean(vd_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_115'] = {'inputs': ['vd_replacement_115'], 'func': vd_replacement_d2_115}


def vd_replacement_d2_116(vd_replacement_116):
    feature = _clean(vd_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_116'] = {'inputs': ['vd_replacement_116'], 'func': vd_replacement_d2_116}


def vd_replacement_d2_117(vd_replacement_117):
    feature = _clean(vd_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_117'] = {'inputs': ['vd_replacement_117'], 'func': vd_replacement_d2_117}


def vd_replacement_d2_118(vd_replacement_118):
    feature = _clean(vd_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_118'] = {'inputs': ['vd_replacement_118'], 'func': vd_replacement_d2_118}


def vd_replacement_d2_119(vd_replacement_119):
    feature = _clean(vd_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_119'] = {'inputs': ['vd_replacement_119'], 'func': vd_replacement_d2_119}


def vd_replacement_d2_120(vd_replacement_120):
    feature = _clean(vd_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_120'] = {'inputs': ['vd_replacement_120'], 'func': vd_replacement_d2_120}


def vd_replacement_d2_121(vd_replacement_121):
    feature = _clean(vd_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_121'] = {'inputs': ['vd_replacement_121'], 'func': vd_replacement_d2_121}


def vd_replacement_d2_122(vd_replacement_122):
    feature = _clean(vd_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_122'] = {'inputs': ['vd_replacement_122'], 'func': vd_replacement_d2_122}


def vd_replacement_d2_123(vd_replacement_123):
    feature = _clean(vd_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_123'] = {'inputs': ['vd_replacement_123'], 'func': vd_replacement_d2_123}


def vd_replacement_d2_124(vd_replacement_124):
    feature = _clean(vd_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_124'] = {'inputs': ['vd_replacement_124'], 'func': vd_replacement_d2_124}


def vd_replacement_d2_125(vd_replacement_125):
    feature = _clean(vd_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_125'] = {'inputs': ['vd_replacement_125'], 'func': vd_replacement_d2_125}


def vd_replacement_d2_126(vd_replacement_126):
    feature = _clean(vd_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_126'] = {'inputs': ['vd_replacement_126'], 'func': vd_replacement_d2_126}


def vd_replacement_d2_127(vd_replacement_127):
    feature = _clean(vd_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_127'] = {'inputs': ['vd_replacement_127'], 'func': vd_replacement_d2_127}


def vd_replacement_d2_128(vd_replacement_128):
    feature = _clean(vd_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_128'] = {'inputs': ['vd_replacement_128'], 'func': vd_replacement_d2_128}


def vd_replacement_d2_129(vd_replacement_129):
    feature = _clean(vd_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_129'] = {'inputs': ['vd_replacement_129'], 'func': vd_replacement_d2_129}


def vd_replacement_d2_130(vd_replacement_130):
    feature = _clean(vd_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_130'] = {'inputs': ['vd_replacement_130'], 'func': vd_replacement_d2_130}


def vd_replacement_d2_131(vd_replacement_131):
    feature = _clean(vd_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_131'] = {'inputs': ['vd_replacement_131'], 'func': vd_replacement_d2_131}


def vd_replacement_d2_132(vd_replacement_132):
    feature = _clean(vd_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_132'] = {'inputs': ['vd_replacement_132'], 'func': vd_replacement_d2_132}


def vd_replacement_d2_133(vd_replacement_133):
    feature = _clean(vd_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_133'] = {'inputs': ['vd_replacement_133'], 'func': vd_replacement_d2_133}


def vd_replacement_d2_134(vd_replacement_134):
    feature = _clean(vd_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_134'] = {'inputs': ['vd_replacement_134'], 'func': vd_replacement_d2_134}


def vd_replacement_d2_135(vd_replacement_135):
    feature = _clean(vd_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_135'] = {'inputs': ['vd_replacement_135'], 'func': vd_replacement_d2_135}


def vd_replacement_d2_136(vd_replacement_136):
    feature = _clean(vd_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_136'] = {'inputs': ['vd_replacement_136'], 'func': vd_replacement_d2_136}


def vd_replacement_d2_137(vd_replacement_137):
    feature = _clean(vd_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_137'] = {'inputs': ['vd_replacement_137'], 'func': vd_replacement_d2_137}


def vd_replacement_d2_138(vd_replacement_138):
    feature = _clean(vd_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_138'] = {'inputs': ['vd_replacement_138'], 'func': vd_replacement_d2_138}


def vd_replacement_d2_139(vd_replacement_139):
    feature = _clean(vd_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_139'] = {'inputs': ['vd_replacement_139'], 'func': vd_replacement_d2_139}


def vd_replacement_d2_140(vd_replacement_140):
    feature = _clean(vd_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_140'] = {'inputs': ['vd_replacement_140'], 'func': vd_replacement_d2_140}


def vd_replacement_d2_141(vd_replacement_141):
    feature = _clean(vd_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_141'] = {'inputs': ['vd_replacement_141'], 'func': vd_replacement_d2_141}


def vd_replacement_d2_142(vd_replacement_142):
    feature = _clean(vd_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_142'] = {'inputs': ['vd_replacement_142'], 'func': vd_replacement_d2_142}


def vd_replacement_d2_143(vd_replacement_143):
    feature = _clean(vd_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_143'] = {'inputs': ['vd_replacement_143'], 'func': vd_replacement_d2_143}


def vd_replacement_d2_144(vd_replacement_144):
    feature = _clean(vd_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_144'] = {'inputs': ['vd_replacement_144'], 'func': vd_replacement_d2_144}


def vd_replacement_d2_145(vd_replacement_145):
    feature = _clean(vd_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_145'] = {'inputs': ['vd_replacement_145'], 'func': vd_replacement_d2_145}


def vd_replacement_d2_146(vd_replacement_146):
    feature = _clean(vd_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_146'] = {'inputs': ['vd_replacement_146'], 'func': vd_replacement_d2_146}


def vd_replacement_d2_147(vd_replacement_147):
    feature = _clean(vd_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_147'] = {'inputs': ['vd_replacement_147'], 'func': vd_replacement_d2_147}


def vd_replacement_d2_148(vd_replacement_148):
    feature = _clean(vd_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_148'] = {'inputs': ['vd_replacement_148'], 'func': vd_replacement_d2_148}


def vd_replacement_d2_149(vd_replacement_149):
    feature = _clean(vd_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_149'] = {'inputs': ['vd_replacement_149'], 'func': vd_replacement_d2_149}


def vd_replacement_d2_150(vd_replacement_150):
    feature = _clean(vd_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_150'] = {'inputs': ['vd_replacement_150'], 'func': vd_replacement_d2_150}


def vd_replacement_d2_151(vd_replacement_151):
    feature = _clean(vd_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_151'] = {'inputs': ['vd_replacement_151'], 'func': vd_replacement_d2_151}


def vd_replacement_d2_152(vd_replacement_152):
    feature = _clean(vd_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_152'] = {'inputs': ['vd_replacement_152'], 'func': vd_replacement_d2_152}


def vd_replacement_d2_153(vd_replacement_153):
    feature = _clean(vd_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_153'] = {'inputs': ['vd_replacement_153'], 'func': vd_replacement_d2_153}


def vd_replacement_d2_154(vd_replacement_154):
    feature = _clean(vd_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_154'] = {'inputs': ['vd_replacement_154'], 'func': vd_replacement_d2_154}


def vd_replacement_d2_155(vd_replacement_155):
    feature = _clean(vd_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_155'] = {'inputs': ['vd_replacement_155'], 'func': vd_replacement_d2_155}


def vd_replacement_d2_156(vd_replacement_156):
    feature = _clean(vd_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_156'] = {'inputs': ['vd_replacement_156'], 'func': vd_replacement_d2_156}


def vd_replacement_d2_157(vd_replacement_157):
    feature = _clean(vd_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_157'] = {'inputs': ['vd_replacement_157'], 'func': vd_replacement_d2_157}


def vd_replacement_d2_158(vd_replacement_158):
    feature = _clean(vd_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_158'] = {'inputs': ['vd_replacement_158'], 'func': vd_replacement_d2_158}


def vd_replacement_d2_159(vd_replacement_159):
    feature = _clean(vd_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_159'] = {'inputs': ['vd_replacement_159'], 'func': vd_replacement_d2_159}


def vd_replacement_d2_160(vd_replacement_160):
    feature = _clean(vd_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
VD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vd_replacement_d2_160'] = {'inputs': ['vd_replacement_160'], 'func': vd_replacement_d2_160}


# Base-universe derivative extensions for repaired first-base features.
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def vdry_base_universe_d2_001_vdry_002_volume_zscore_10_002(vdry_002_volume_zscore_10_002):
    return _base_universe_d2(vdry_002_volume_zscore_10_002, 1)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_001_vdry_002_volume_zscore_10_002'] = {'inputs': ['vdry_002_volume_zscore_10_002'], 'func': vdry_base_universe_d2_001_vdry_002_volume_zscore_10_002}


def vdry_base_universe_d2_002_vdry_003_down_volume_share_21_003(vdry_003_down_volume_share_21_003):
    return _base_universe_d2(vdry_003_down_volume_share_21_003, 2)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_002_vdry_003_down_volume_share_21_003'] = {'inputs': ['vdry_003_down_volume_share_21_003'], 'func': vdry_base_universe_d2_002_vdry_003_down_volume_share_21_003}


def vdry_base_universe_d2_003_vdry_004_dollar_volume_shock_42_004(vdry_004_dollar_volume_shock_42_004):
    return _base_universe_d2(vdry_004_dollar_volume_shock_42_004, 3)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_003_vdry_004_dollar_volume_shock_42_004'] = {'inputs': ['vdry_004_dollar_volume_shock_42_004'], 'func': vdry_base_universe_d2_003_vdry_004_dollar_volume_shock_42_004}


def vdry_base_universe_d2_004_vdry_005_volume_trend_slope_63_005(vdry_005_volume_trend_slope_63_005):
    return _base_universe_d2(vdry_005_volume_trend_slope_63_005, 4)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_004_vdry_005_volume_trend_slope_63_005'] = {'inputs': ['vdry_005_volume_trend_slope_63_005'], 'func': vdry_base_universe_d2_004_vdry_005_volume_trend_slope_63_005}


def vdry_base_universe_d2_005_vdry_006_price_volume_divergence_84_006(vdry_006_price_volume_divergence_84_006):
    return _base_universe_d2(vdry_006_price_volume_divergence_84_006, 5)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_005_vdry_006_price_volume_divergence_84_006'] = {'inputs': ['vdry_006_price_volume_divergence_84_006'], 'func': vdry_base_universe_d2_005_vdry_006_price_volume_divergence_84_006}


def vdry_base_universe_d2_006_vdry_008_volume_zscore_189_008(vdry_008_volume_zscore_189_008):
    return _base_universe_d2(vdry_008_volume_zscore_189_008, 6)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_006_vdry_008_volume_zscore_189_008'] = {'inputs': ['vdry_008_volume_zscore_189_008'], 'func': vdry_base_universe_d2_006_vdry_008_volume_zscore_189_008}


def vdry_base_universe_d2_007_vdry_009_down_volume_share_252_009(vdry_009_down_volume_share_252_009):
    return _base_universe_d2(vdry_009_down_volume_share_252_009, 7)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_007_vdry_009_down_volume_share_252_009'] = {'inputs': ['vdry_009_down_volume_share_252_009'], 'func': vdry_base_universe_d2_007_vdry_009_down_volume_share_252_009}


def vdry_base_universe_d2_008_vdry_010_dollar_volume_shock_378_010(vdry_010_dollar_volume_shock_378_010):
    return _base_universe_d2(vdry_010_dollar_volume_shock_378_010, 8)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_008_vdry_010_dollar_volume_shock_378_010'] = {'inputs': ['vdry_010_dollar_volume_shock_378_010'], 'func': vdry_base_universe_d2_008_vdry_010_dollar_volume_shock_378_010}


def vdry_base_universe_d2_009_vdry_011_volume_trend_slope_504_011(vdry_011_volume_trend_slope_504_011):
    return _base_universe_d2(vdry_011_volume_trend_slope_504_011, 9)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_009_vdry_011_volume_trend_slope_504_011'] = {'inputs': ['vdry_011_volume_trend_slope_504_011'], 'func': vdry_base_universe_d2_009_vdry_011_volume_trend_slope_504_011}


def vdry_base_universe_d2_010_vdry_012_price_volume_divergence_756_012(vdry_012_price_volume_divergence_756_012):
    return _base_universe_d2(vdry_012_price_volume_divergence_756_012, 10)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_010_vdry_012_price_volume_divergence_756_012'] = {'inputs': ['vdry_012_price_volume_divergence_756_012'], 'func': vdry_base_universe_d2_010_vdry_012_price_volume_divergence_756_012}


def vdry_base_universe_d2_011_vdry_014_volume_zscore_1260_014(vdry_014_volume_zscore_1260_014):
    return _base_universe_d2(vdry_014_volume_zscore_1260_014, 11)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_011_vdry_014_volume_zscore_1260_014'] = {'inputs': ['vdry_014_volume_zscore_1260_014'], 'func': vdry_base_universe_d2_011_vdry_014_volume_zscore_1260_014}


def vdry_base_universe_d2_012_vdry_015_down_volume_share_1512_015(vdry_015_down_volume_share_1512_015):
    return _base_universe_d2(vdry_015_down_volume_share_1512_015, 12)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_012_vdry_015_down_volume_share_1512_015'] = {'inputs': ['vdry_015_down_volume_share_1512_015'], 'func': vdry_base_universe_d2_012_vdry_015_down_volume_share_1512_015}


def vdry_base_universe_d2_013_vdry_016_dollar_volume_shock_5_016(vdry_016_dollar_volume_shock_5_016):
    return _base_universe_d2(vdry_016_dollar_volume_shock_5_016, 13)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_013_vdry_016_dollar_volume_shock_5_016'] = {'inputs': ['vdry_016_dollar_volume_shock_5_016'], 'func': vdry_base_universe_d2_013_vdry_016_dollar_volume_shock_5_016}


def vdry_base_universe_d2_014_vdry_017_volume_trend_slope_10_017(vdry_017_volume_trend_slope_10_017):
    return _base_universe_d2(vdry_017_volume_trend_slope_10_017, 14)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_014_vdry_017_volume_trend_slope_10_017'] = {'inputs': ['vdry_017_volume_trend_slope_10_017'], 'func': vdry_base_universe_d2_014_vdry_017_volume_trend_slope_10_017}


def vdry_base_universe_d2_015_vdry_018_price_volume_divergence_21_018(vdry_018_price_volume_divergence_21_018):
    return _base_universe_d2(vdry_018_price_volume_divergence_21_018, 15)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_015_vdry_018_price_volume_divergence_21_018'] = {'inputs': ['vdry_018_price_volume_divergence_21_018'], 'func': vdry_base_universe_d2_015_vdry_018_price_volume_divergence_21_018}


def vdry_base_universe_d2_016_vdry_020_volume_zscore_63_020(vdry_020_volume_zscore_63_020):
    return _base_universe_d2(vdry_020_volume_zscore_63_020, 16)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_016_vdry_020_volume_zscore_63_020'] = {'inputs': ['vdry_020_volume_zscore_63_020'], 'func': vdry_base_universe_d2_016_vdry_020_volume_zscore_63_020}


def vdry_base_universe_d2_017_vdry_021_down_volume_share_84_021(vdry_021_down_volume_share_84_021):
    return _base_universe_d2(vdry_021_down_volume_share_84_021, 17)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_017_vdry_021_down_volume_share_84_021'] = {'inputs': ['vdry_021_down_volume_share_84_021'], 'func': vdry_base_universe_d2_017_vdry_021_down_volume_share_84_021}


def vdry_base_universe_d2_018_vdry_022_dollar_volume_shock_126_022(vdry_022_dollar_volume_shock_126_022):
    return _base_universe_d2(vdry_022_dollar_volume_shock_126_022, 18)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_018_vdry_022_dollar_volume_shock_126_022'] = {'inputs': ['vdry_022_dollar_volume_shock_126_022'], 'func': vdry_base_universe_d2_018_vdry_022_dollar_volume_shock_126_022}


def vdry_base_universe_d2_019_vdry_023_volume_trend_slope_189_023(vdry_023_volume_trend_slope_189_023):
    return _base_universe_d2(vdry_023_volume_trend_slope_189_023, 19)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_019_vdry_023_volume_trend_slope_189_023'] = {'inputs': ['vdry_023_volume_trend_slope_189_023'], 'func': vdry_base_universe_d2_019_vdry_023_volume_trend_slope_189_023}


def vdry_base_universe_d2_020_vdry_024_price_volume_divergence_252_024(vdry_024_price_volume_divergence_252_024):
    return _base_universe_d2(vdry_024_price_volume_divergence_252_024, 20)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_020_vdry_024_price_volume_divergence_252_024'] = {'inputs': ['vdry_024_price_volume_divergence_252_024'], 'func': vdry_base_universe_d2_020_vdry_024_price_volume_divergence_252_024}


def vdry_base_universe_d2_021_vdry_026_volume_zscore_504_026(vdry_026_volume_zscore_504_026):
    return _base_universe_d2(vdry_026_volume_zscore_504_026, 21)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_021_vdry_026_volume_zscore_504_026'] = {'inputs': ['vdry_026_volume_zscore_504_026'], 'func': vdry_base_universe_d2_021_vdry_026_volume_zscore_504_026}


def vdry_base_universe_d2_022_vdry_027_down_volume_share_756_027(vdry_027_down_volume_share_756_027):
    return _base_universe_d2(vdry_027_down_volume_share_756_027, 22)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_022_vdry_027_down_volume_share_756_027'] = {'inputs': ['vdry_027_down_volume_share_756_027'], 'func': vdry_base_universe_d2_022_vdry_027_down_volume_share_756_027}


def vdry_base_universe_d2_023_vdry_028_dollar_volume_shock_1008_028(vdry_028_dollar_volume_shock_1008_028):
    return _base_universe_d2(vdry_028_dollar_volume_shock_1008_028, 23)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_023_vdry_028_dollar_volume_shock_1008_028'] = {'inputs': ['vdry_028_dollar_volume_shock_1008_028'], 'func': vdry_base_universe_d2_023_vdry_028_dollar_volume_shock_1008_028}


def vdry_base_universe_d2_024_vdry_029_volume_trend_slope_1260_029(vdry_029_volume_trend_slope_1260_029):
    return _base_universe_d2(vdry_029_volume_trend_slope_1260_029, 24)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_024_vdry_029_volume_trend_slope_1260_029'] = {'inputs': ['vdry_029_volume_trend_slope_1260_029'], 'func': vdry_base_universe_d2_024_vdry_029_volume_trend_slope_1260_029}


def vdry_base_universe_d2_025_vdry_030_price_volume_divergence_1512_030(vdry_030_price_volume_divergence_1512_030):
    return _base_universe_d2(vdry_030_price_volume_divergence_1512_030, 25)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_025_vdry_030_price_volume_divergence_1512_030'] = {'inputs': ['vdry_030_price_volume_divergence_1512_030'], 'func': vdry_base_universe_d2_025_vdry_030_price_volume_divergence_1512_030}


def vdry_base_universe_d2_026_vdry_basefill_031(vdry_basefill_031):
    return _base_universe_d2(vdry_basefill_031, 26)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_026_vdry_basefill_031'] = {'inputs': ['vdry_basefill_031'], 'func': vdry_base_universe_d2_026_vdry_basefill_031}


def vdry_base_universe_d2_027_vdry_basefill_032(vdry_basefill_032):
    return _base_universe_d2(vdry_basefill_032, 27)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_027_vdry_basefill_032'] = {'inputs': ['vdry_basefill_032'], 'func': vdry_base_universe_d2_027_vdry_basefill_032}


def vdry_base_universe_d2_028_vdry_basefill_033(vdry_basefill_033):
    return _base_universe_d2(vdry_basefill_033, 28)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_028_vdry_basefill_033'] = {'inputs': ['vdry_basefill_033'], 'func': vdry_base_universe_d2_028_vdry_basefill_033}


def vdry_base_universe_d2_029_vdry_basefill_034(vdry_basefill_034):
    return _base_universe_d2(vdry_basefill_034, 29)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_029_vdry_basefill_034'] = {'inputs': ['vdry_basefill_034'], 'func': vdry_base_universe_d2_029_vdry_basefill_034}


def vdry_base_universe_d2_030_vdry_basefill_035(vdry_basefill_035):
    return _base_universe_d2(vdry_basefill_035, 30)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_030_vdry_basefill_035'] = {'inputs': ['vdry_basefill_035'], 'func': vdry_base_universe_d2_030_vdry_basefill_035}


def vdry_base_universe_d2_031_vdry_basefill_036(vdry_basefill_036):
    return _base_universe_d2(vdry_basefill_036, 31)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_031_vdry_basefill_036'] = {'inputs': ['vdry_basefill_036'], 'func': vdry_base_universe_d2_031_vdry_basefill_036}


def vdry_base_universe_d2_032_vdry_basefill_037(vdry_basefill_037):
    return _base_universe_d2(vdry_basefill_037, 32)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_032_vdry_basefill_037'] = {'inputs': ['vdry_basefill_037'], 'func': vdry_base_universe_d2_032_vdry_basefill_037}


def vdry_base_universe_d2_033_vdry_basefill_038(vdry_basefill_038):
    return _base_universe_d2(vdry_basefill_038, 33)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_033_vdry_basefill_038'] = {'inputs': ['vdry_basefill_038'], 'func': vdry_base_universe_d2_033_vdry_basefill_038}


def vdry_base_universe_d2_034_vdry_basefill_039(vdry_basefill_039):
    return _base_universe_d2(vdry_basefill_039, 34)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_034_vdry_basefill_039'] = {'inputs': ['vdry_basefill_039'], 'func': vdry_base_universe_d2_034_vdry_basefill_039}


def vdry_base_universe_d2_035_vdry_basefill_040(vdry_basefill_040):
    return _base_universe_d2(vdry_basefill_040, 35)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_035_vdry_basefill_040'] = {'inputs': ['vdry_basefill_040'], 'func': vdry_base_universe_d2_035_vdry_basefill_040}


def vdry_base_universe_d2_036_vdry_basefill_041(vdry_basefill_041):
    return _base_universe_d2(vdry_basefill_041, 36)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_036_vdry_basefill_041'] = {'inputs': ['vdry_basefill_041'], 'func': vdry_base_universe_d2_036_vdry_basefill_041}


def vdry_base_universe_d2_037_vdry_basefill_042(vdry_basefill_042):
    return _base_universe_d2(vdry_basefill_042, 37)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_037_vdry_basefill_042'] = {'inputs': ['vdry_basefill_042'], 'func': vdry_base_universe_d2_037_vdry_basefill_042}


def vdry_base_universe_d2_038_vdry_basefill_043(vdry_basefill_043):
    return _base_universe_d2(vdry_basefill_043, 38)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_038_vdry_basefill_043'] = {'inputs': ['vdry_basefill_043'], 'func': vdry_base_universe_d2_038_vdry_basefill_043}


def vdry_base_universe_d2_039_vdry_basefill_044(vdry_basefill_044):
    return _base_universe_d2(vdry_basefill_044, 39)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_039_vdry_basefill_044'] = {'inputs': ['vdry_basefill_044'], 'func': vdry_base_universe_d2_039_vdry_basefill_044}


def vdry_base_universe_d2_040_vdry_basefill_045(vdry_basefill_045):
    return _base_universe_d2(vdry_basefill_045, 40)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_040_vdry_basefill_045'] = {'inputs': ['vdry_basefill_045'], 'func': vdry_base_universe_d2_040_vdry_basefill_045}


def vdry_base_universe_d2_041_vdry_basefill_046(vdry_basefill_046):
    return _base_universe_d2(vdry_basefill_046, 41)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_041_vdry_basefill_046'] = {'inputs': ['vdry_basefill_046'], 'func': vdry_base_universe_d2_041_vdry_basefill_046}


def vdry_base_universe_d2_042_vdry_basefill_047(vdry_basefill_047):
    return _base_universe_d2(vdry_basefill_047, 42)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_042_vdry_basefill_047'] = {'inputs': ['vdry_basefill_047'], 'func': vdry_base_universe_d2_042_vdry_basefill_047}


def vdry_base_universe_d2_043_vdry_basefill_048(vdry_basefill_048):
    return _base_universe_d2(vdry_basefill_048, 43)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_043_vdry_basefill_048'] = {'inputs': ['vdry_basefill_048'], 'func': vdry_base_universe_d2_043_vdry_basefill_048}


def vdry_base_universe_d2_044_vdry_basefill_049(vdry_basefill_049):
    return _base_universe_d2(vdry_basefill_049, 44)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_044_vdry_basefill_049'] = {'inputs': ['vdry_basefill_049'], 'func': vdry_base_universe_d2_044_vdry_basefill_049}


def vdry_base_universe_d2_045_vdry_basefill_050(vdry_basefill_050):
    return _base_universe_d2(vdry_basefill_050, 45)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_045_vdry_basefill_050'] = {'inputs': ['vdry_basefill_050'], 'func': vdry_base_universe_d2_045_vdry_basefill_050}


def vdry_base_universe_d2_046_vdry_basefill_051(vdry_basefill_051):
    return _base_universe_d2(vdry_basefill_051, 46)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_046_vdry_basefill_051'] = {'inputs': ['vdry_basefill_051'], 'func': vdry_base_universe_d2_046_vdry_basefill_051}


def vdry_base_universe_d2_047_vdry_basefill_052(vdry_basefill_052):
    return _base_universe_d2(vdry_basefill_052, 47)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_047_vdry_basefill_052'] = {'inputs': ['vdry_basefill_052'], 'func': vdry_base_universe_d2_047_vdry_basefill_052}


def vdry_base_universe_d2_048_vdry_basefill_053(vdry_basefill_053):
    return _base_universe_d2(vdry_basefill_053, 48)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_048_vdry_basefill_053'] = {'inputs': ['vdry_basefill_053'], 'func': vdry_base_universe_d2_048_vdry_basefill_053}


def vdry_base_universe_d2_049_vdry_basefill_054(vdry_basefill_054):
    return _base_universe_d2(vdry_basefill_054, 49)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_049_vdry_basefill_054'] = {'inputs': ['vdry_basefill_054'], 'func': vdry_base_universe_d2_049_vdry_basefill_054}


def vdry_base_universe_d2_050_vdry_basefill_055(vdry_basefill_055):
    return _base_universe_d2(vdry_basefill_055, 50)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_050_vdry_basefill_055'] = {'inputs': ['vdry_basefill_055'], 'func': vdry_base_universe_d2_050_vdry_basefill_055}


def vdry_base_universe_d2_051_vdry_basefill_056(vdry_basefill_056):
    return _base_universe_d2(vdry_basefill_056, 51)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_051_vdry_basefill_056'] = {'inputs': ['vdry_basefill_056'], 'func': vdry_base_universe_d2_051_vdry_basefill_056}


def vdry_base_universe_d2_052_vdry_basefill_057(vdry_basefill_057):
    return _base_universe_d2(vdry_basefill_057, 52)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_052_vdry_basefill_057'] = {'inputs': ['vdry_basefill_057'], 'func': vdry_base_universe_d2_052_vdry_basefill_057}


def vdry_base_universe_d2_053_vdry_basefill_058(vdry_basefill_058):
    return _base_universe_d2(vdry_basefill_058, 53)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_053_vdry_basefill_058'] = {'inputs': ['vdry_basefill_058'], 'func': vdry_base_universe_d2_053_vdry_basefill_058}


def vdry_base_universe_d2_054_vdry_basefill_059(vdry_basefill_059):
    return _base_universe_d2(vdry_basefill_059, 54)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_054_vdry_basefill_059'] = {'inputs': ['vdry_basefill_059'], 'func': vdry_base_universe_d2_054_vdry_basefill_059}


def vdry_base_universe_d2_055_vdry_basefill_060(vdry_basefill_060):
    return _base_universe_d2(vdry_basefill_060, 55)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_055_vdry_basefill_060'] = {'inputs': ['vdry_basefill_060'], 'func': vdry_base_universe_d2_055_vdry_basefill_060}


def vdry_base_universe_d2_056_vdry_basefill_061(vdry_basefill_061):
    return _base_universe_d2(vdry_basefill_061, 56)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_056_vdry_basefill_061'] = {'inputs': ['vdry_basefill_061'], 'func': vdry_base_universe_d2_056_vdry_basefill_061}


def vdry_base_universe_d2_057_vdry_basefill_062(vdry_basefill_062):
    return _base_universe_d2(vdry_basefill_062, 57)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_057_vdry_basefill_062'] = {'inputs': ['vdry_basefill_062'], 'func': vdry_base_universe_d2_057_vdry_basefill_062}


def vdry_base_universe_d2_058_vdry_basefill_063(vdry_basefill_063):
    return _base_universe_d2(vdry_basefill_063, 58)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_058_vdry_basefill_063'] = {'inputs': ['vdry_basefill_063'], 'func': vdry_base_universe_d2_058_vdry_basefill_063}


def vdry_base_universe_d2_059_vdry_basefill_064(vdry_basefill_064):
    return _base_universe_d2(vdry_basefill_064, 59)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_059_vdry_basefill_064'] = {'inputs': ['vdry_basefill_064'], 'func': vdry_base_universe_d2_059_vdry_basefill_064}


def vdry_base_universe_d2_060_vdry_basefill_065(vdry_basefill_065):
    return _base_universe_d2(vdry_basefill_065, 60)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_060_vdry_basefill_065'] = {'inputs': ['vdry_basefill_065'], 'func': vdry_base_universe_d2_060_vdry_basefill_065}


def vdry_base_universe_d2_061_vdry_basefill_066(vdry_basefill_066):
    return _base_universe_d2(vdry_basefill_066, 61)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_061_vdry_basefill_066'] = {'inputs': ['vdry_basefill_066'], 'func': vdry_base_universe_d2_061_vdry_basefill_066}


def vdry_base_universe_d2_062_vdry_basefill_067(vdry_basefill_067):
    return _base_universe_d2(vdry_basefill_067, 62)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_062_vdry_basefill_067'] = {'inputs': ['vdry_basefill_067'], 'func': vdry_base_universe_d2_062_vdry_basefill_067}


def vdry_base_universe_d2_063_vdry_basefill_068(vdry_basefill_068):
    return _base_universe_d2(vdry_basefill_068, 63)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_063_vdry_basefill_068'] = {'inputs': ['vdry_basefill_068'], 'func': vdry_base_universe_d2_063_vdry_basefill_068}


def vdry_base_universe_d2_064_vdry_basefill_069(vdry_basefill_069):
    return _base_universe_d2(vdry_basefill_069, 64)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_064_vdry_basefill_069'] = {'inputs': ['vdry_basefill_069'], 'func': vdry_base_universe_d2_064_vdry_basefill_069}


def vdry_base_universe_d2_065_vdry_basefill_070(vdry_basefill_070):
    return _base_universe_d2(vdry_basefill_070, 65)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_065_vdry_basefill_070'] = {'inputs': ['vdry_basefill_070'], 'func': vdry_base_universe_d2_065_vdry_basefill_070}


def vdry_base_universe_d2_066_vdry_basefill_071(vdry_basefill_071):
    return _base_universe_d2(vdry_basefill_071, 66)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_066_vdry_basefill_071'] = {'inputs': ['vdry_basefill_071'], 'func': vdry_base_universe_d2_066_vdry_basefill_071}


def vdry_base_universe_d2_067_vdry_basefill_072(vdry_basefill_072):
    return _base_universe_d2(vdry_basefill_072, 67)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_067_vdry_basefill_072'] = {'inputs': ['vdry_basefill_072'], 'func': vdry_base_universe_d2_067_vdry_basefill_072}


def vdry_base_universe_d2_068_vdry_basefill_073(vdry_basefill_073):
    return _base_universe_d2(vdry_basefill_073, 68)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_068_vdry_basefill_073'] = {'inputs': ['vdry_basefill_073'], 'func': vdry_base_universe_d2_068_vdry_basefill_073}


def vdry_base_universe_d2_069_vdry_basefill_074(vdry_basefill_074):
    return _base_universe_d2(vdry_basefill_074, 69)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_069_vdry_basefill_074'] = {'inputs': ['vdry_basefill_074'], 'func': vdry_base_universe_d2_069_vdry_basefill_074}


def vdry_base_universe_d2_070_vdry_basefill_075(vdry_basefill_075):
    return _base_universe_d2(vdry_basefill_075, 70)
VDRY_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vdry_base_universe_d2_070_vdry_basefill_075'] = {'inputs': ['vdry_basefill_075'], 'func': vdry_base_universe_d2_070_vdry_basefill_075}
