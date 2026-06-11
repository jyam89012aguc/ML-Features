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



def vtr_151_vtr_001_volume_spike_ratio_5_001_roc_1(vtr_001_volume_spike_ratio_5_001):
    feature = _s(vtr_001_volume_spike_ratio_5_001)
    return (_roc(feature, 1)).reindex(feature.index)

def vtr_152_vtr_007_volume_spike_ratio_126_007_roc_5(vtr_007_volume_spike_ratio_126_007):
    feature = _s(vtr_007_volume_spike_ratio_126_007)
    return (_roc(feature, 5)).reindex(feature.index)

def vtr_153_vtr_013_volume_spike_ratio_1008_013_roc_42(vtr_013_volume_spike_ratio_1008_013):
    feature = _s(vtr_013_volume_spike_ratio_1008_013)
    return (_roc(feature, 42)).reindex(feature.index)

def vtr_154_vtr_019_volume_spike_ratio_42_019_roc_126(vtr_019_volume_spike_ratio_42_019):
    feature = _s(vtr_019_volume_spike_ratio_42_019)
    return (_roc(feature, 126)).reindex(feature.index)

def vtr_155_vtr_025_volume_spike_ratio_378_025_roc_378(vtr_025_volume_spike_ratio_378_025):
    feature = _s(vtr_025_volume_spike_ratio_378_025)
    return (_roc(feature, 378)).reindex(feature.index)






















VOLUME_TREND_REGISTRY_2ND_DERIVATIVES = {
    'vtr_151_vtr_001_volume_spike_ratio_5_001_roc_1': {'inputs': ['vtr_001_volume_spike_ratio_5_001'], 'func': vtr_151_vtr_001_volume_spike_ratio_5_001_roc_1},
    'vtr_152_vtr_007_volume_spike_ratio_126_007_roc_5': {'inputs': ['vtr_007_volume_spike_ratio_126_007'], 'func': vtr_152_vtr_007_volume_spike_ratio_126_007_roc_5},
    'vtr_153_vtr_013_volume_spike_ratio_1008_013_roc_42': {'inputs': ['vtr_013_volume_spike_ratio_1008_013'], 'func': vtr_153_vtr_013_volume_spike_ratio_1008_013_roc_42},
    'vtr_154_vtr_019_volume_spike_ratio_42_019_roc_126': {'inputs': ['vtr_019_volume_spike_ratio_42_019'], 'func': vtr_154_vtr_019_volume_spike_ratio_42_019_roc_126},
    'vtr_155_vtr_025_volume_spike_ratio_378_025_roc_378': {'inputs': ['vtr_025_volume_spike_ratio_378_025'], 'func': vtr_155_vtr_025_volume_spike_ratio_378_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def vt_replacement_d2_001(vt_replacement_001):
    feature = _clean(vt_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_001'] = {'inputs': ['vt_replacement_001'], 'func': vt_replacement_d2_001}


def vt_replacement_d2_002(vt_replacement_002):
    feature = _clean(vt_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_002'] = {'inputs': ['vt_replacement_002'], 'func': vt_replacement_d2_002}


def vt_replacement_d2_003(vt_replacement_003):
    feature = _clean(vt_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_003'] = {'inputs': ['vt_replacement_003'], 'func': vt_replacement_d2_003}


def vt_replacement_d2_004(vt_replacement_004):
    feature = _clean(vt_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_004'] = {'inputs': ['vt_replacement_004'], 'func': vt_replacement_d2_004}


def vt_replacement_d2_005(vt_replacement_005):
    feature = _clean(vt_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_005'] = {'inputs': ['vt_replacement_005'], 'func': vt_replacement_d2_005}


def vt_replacement_d2_006(vt_replacement_006):
    feature = _clean(vt_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_006'] = {'inputs': ['vt_replacement_006'], 'func': vt_replacement_d2_006}


def vt_replacement_d2_007(vt_replacement_007):
    feature = _clean(vt_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_007'] = {'inputs': ['vt_replacement_007'], 'func': vt_replacement_d2_007}


def vt_replacement_d2_008(vt_replacement_008):
    feature = _clean(vt_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_008'] = {'inputs': ['vt_replacement_008'], 'func': vt_replacement_d2_008}


def vt_replacement_d2_009(vt_replacement_009):
    feature = _clean(vt_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_009'] = {'inputs': ['vt_replacement_009'], 'func': vt_replacement_d2_009}


def vt_replacement_d2_010(vt_replacement_010):
    feature = _clean(vt_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_010'] = {'inputs': ['vt_replacement_010'], 'func': vt_replacement_d2_010}


def vt_replacement_d2_011(vt_replacement_011):
    feature = _clean(vt_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_011'] = {'inputs': ['vt_replacement_011'], 'func': vt_replacement_d2_011}


def vt_replacement_d2_012(vt_replacement_012):
    feature = _clean(vt_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_012'] = {'inputs': ['vt_replacement_012'], 'func': vt_replacement_d2_012}


def vt_replacement_d2_013(vt_replacement_013):
    feature = _clean(vt_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_013'] = {'inputs': ['vt_replacement_013'], 'func': vt_replacement_d2_013}


def vt_replacement_d2_014(vt_replacement_014):
    feature = _clean(vt_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_014'] = {'inputs': ['vt_replacement_014'], 'func': vt_replacement_d2_014}


def vt_replacement_d2_015(vt_replacement_015):
    feature = _clean(vt_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_015'] = {'inputs': ['vt_replacement_015'], 'func': vt_replacement_d2_015}


def vt_replacement_d2_016(vt_replacement_016):
    feature = _clean(vt_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_016'] = {'inputs': ['vt_replacement_016'], 'func': vt_replacement_d2_016}


def vt_replacement_d2_017(vt_replacement_017):
    feature = _clean(vt_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_017'] = {'inputs': ['vt_replacement_017'], 'func': vt_replacement_d2_017}


def vt_replacement_d2_018(vt_replacement_018):
    feature = _clean(vt_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_018'] = {'inputs': ['vt_replacement_018'], 'func': vt_replacement_d2_018}


def vt_replacement_d2_019(vt_replacement_019):
    feature = _clean(vt_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_019'] = {'inputs': ['vt_replacement_019'], 'func': vt_replacement_d2_019}


def vt_replacement_d2_020(vt_replacement_020):
    feature = _clean(vt_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_020'] = {'inputs': ['vt_replacement_020'], 'func': vt_replacement_d2_020}


def vt_replacement_d2_021(vt_replacement_021):
    feature = _clean(vt_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_021'] = {'inputs': ['vt_replacement_021'], 'func': vt_replacement_d2_021}


def vt_replacement_d2_022(vt_replacement_022):
    feature = _clean(vt_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_022'] = {'inputs': ['vt_replacement_022'], 'func': vt_replacement_d2_022}


def vt_replacement_d2_023(vt_replacement_023):
    feature = _clean(vt_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_023'] = {'inputs': ['vt_replacement_023'], 'func': vt_replacement_d2_023}


def vt_replacement_d2_024(vt_replacement_024):
    feature = _clean(vt_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_024'] = {'inputs': ['vt_replacement_024'], 'func': vt_replacement_d2_024}


def vt_replacement_d2_025(vt_replacement_025):
    feature = _clean(vt_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_025'] = {'inputs': ['vt_replacement_025'], 'func': vt_replacement_d2_025}


def vt_replacement_d2_026(vt_replacement_026):
    feature = _clean(vt_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_026'] = {'inputs': ['vt_replacement_026'], 'func': vt_replacement_d2_026}


def vt_replacement_d2_027(vt_replacement_027):
    feature = _clean(vt_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_027'] = {'inputs': ['vt_replacement_027'], 'func': vt_replacement_d2_027}


def vt_replacement_d2_028(vt_replacement_028):
    feature = _clean(vt_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_028'] = {'inputs': ['vt_replacement_028'], 'func': vt_replacement_d2_028}


def vt_replacement_d2_029(vt_replacement_029):
    feature = _clean(vt_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_029'] = {'inputs': ['vt_replacement_029'], 'func': vt_replacement_d2_029}


def vt_replacement_d2_030(vt_replacement_030):
    feature = _clean(vt_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_030'] = {'inputs': ['vt_replacement_030'], 'func': vt_replacement_d2_030}


def vt_replacement_d2_031(vt_replacement_031):
    feature = _clean(vt_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_031'] = {'inputs': ['vt_replacement_031'], 'func': vt_replacement_d2_031}


def vt_replacement_d2_032(vt_replacement_032):
    feature = _clean(vt_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_032'] = {'inputs': ['vt_replacement_032'], 'func': vt_replacement_d2_032}


def vt_replacement_d2_033(vt_replacement_033):
    feature = _clean(vt_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_033'] = {'inputs': ['vt_replacement_033'], 'func': vt_replacement_d2_033}


def vt_replacement_d2_034(vt_replacement_034):
    feature = _clean(vt_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_034'] = {'inputs': ['vt_replacement_034'], 'func': vt_replacement_d2_034}


def vt_replacement_d2_035(vt_replacement_035):
    feature = _clean(vt_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_035'] = {'inputs': ['vt_replacement_035'], 'func': vt_replacement_d2_035}


def vt_replacement_d2_036(vt_replacement_036):
    feature = _clean(vt_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_036'] = {'inputs': ['vt_replacement_036'], 'func': vt_replacement_d2_036}


def vt_replacement_d2_037(vt_replacement_037):
    feature = _clean(vt_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_037'] = {'inputs': ['vt_replacement_037'], 'func': vt_replacement_d2_037}


def vt_replacement_d2_038(vt_replacement_038):
    feature = _clean(vt_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_038'] = {'inputs': ['vt_replacement_038'], 'func': vt_replacement_d2_038}


def vt_replacement_d2_039(vt_replacement_039):
    feature = _clean(vt_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_039'] = {'inputs': ['vt_replacement_039'], 'func': vt_replacement_d2_039}


def vt_replacement_d2_040(vt_replacement_040):
    feature = _clean(vt_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_040'] = {'inputs': ['vt_replacement_040'], 'func': vt_replacement_d2_040}


def vt_replacement_d2_041(vt_replacement_041):
    feature = _clean(vt_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_041'] = {'inputs': ['vt_replacement_041'], 'func': vt_replacement_d2_041}


def vt_replacement_d2_042(vt_replacement_042):
    feature = _clean(vt_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_042'] = {'inputs': ['vt_replacement_042'], 'func': vt_replacement_d2_042}


def vt_replacement_d2_043(vt_replacement_043):
    feature = _clean(vt_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_043'] = {'inputs': ['vt_replacement_043'], 'func': vt_replacement_d2_043}


def vt_replacement_d2_044(vt_replacement_044):
    feature = _clean(vt_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_044'] = {'inputs': ['vt_replacement_044'], 'func': vt_replacement_d2_044}


def vt_replacement_d2_045(vt_replacement_045):
    feature = _clean(vt_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_045'] = {'inputs': ['vt_replacement_045'], 'func': vt_replacement_d2_045}


def vt_replacement_d2_046(vt_replacement_046):
    feature = _clean(vt_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_046'] = {'inputs': ['vt_replacement_046'], 'func': vt_replacement_d2_046}


def vt_replacement_d2_047(vt_replacement_047):
    feature = _clean(vt_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_047'] = {'inputs': ['vt_replacement_047'], 'func': vt_replacement_d2_047}


def vt_replacement_d2_048(vt_replacement_048):
    feature = _clean(vt_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_048'] = {'inputs': ['vt_replacement_048'], 'func': vt_replacement_d2_048}


def vt_replacement_d2_049(vt_replacement_049):
    feature = _clean(vt_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_049'] = {'inputs': ['vt_replacement_049'], 'func': vt_replacement_d2_049}


def vt_replacement_d2_050(vt_replacement_050):
    feature = _clean(vt_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_050'] = {'inputs': ['vt_replacement_050'], 'func': vt_replacement_d2_050}


def vt_replacement_d2_051(vt_replacement_051):
    feature = _clean(vt_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_051'] = {'inputs': ['vt_replacement_051'], 'func': vt_replacement_d2_051}


def vt_replacement_d2_052(vt_replacement_052):
    feature = _clean(vt_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_052'] = {'inputs': ['vt_replacement_052'], 'func': vt_replacement_d2_052}


def vt_replacement_d2_053(vt_replacement_053):
    feature = _clean(vt_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_053'] = {'inputs': ['vt_replacement_053'], 'func': vt_replacement_d2_053}


def vt_replacement_d2_054(vt_replacement_054):
    feature = _clean(vt_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_054'] = {'inputs': ['vt_replacement_054'], 'func': vt_replacement_d2_054}


def vt_replacement_d2_055(vt_replacement_055):
    feature = _clean(vt_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_055'] = {'inputs': ['vt_replacement_055'], 'func': vt_replacement_d2_055}


def vt_replacement_d2_056(vt_replacement_056):
    feature = _clean(vt_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_056'] = {'inputs': ['vt_replacement_056'], 'func': vt_replacement_d2_056}


def vt_replacement_d2_057(vt_replacement_057):
    feature = _clean(vt_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_057'] = {'inputs': ['vt_replacement_057'], 'func': vt_replacement_d2_057}


def vt_replacement_d2_058(vt_replacement_058):
    feature = _clean(vt_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_058'] = {'inputs': ['vt_replacement_058'], 'func': vt_replacement_d2_058}


def vt_replacement_d2_059(vt_replacement_059):
    feature = _clean(vt_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_059'] = {'inputs': ['vt_replacement_059'], 'func': vt_replacement_d2_059}


def vt_replacement_d2_060(vt_replacement_060):
    feature = _clean(vt_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_060'] = {'inputs': ['vt_replacement_060'], 'func': vt_replacement_d2_060}


def vt_replacement_d2_061(vt_replacement_061):
    feature = _clean(vt_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_061'] = {'inputs': ['vt_replacement_061'], 'func': vt_replacement_d2_061}


def vt_replacement_d2_062(vt_replacement_062):
    feature = _clean(vt_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_062'] = {'inputs': ['vt_replacement_062'], 'func': vt_replacement_d2_062}


def vt_replacement_d2_063(vt_replacement_063):
    feature = _clean(vt_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_063'] = {'inputs': ['vt_replacement_063'], 'func': vt_replacement_d2_063}


def vt_replacement_d2_064(vt_replacement_064):
    feature = _clean(vt_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_064'] = {'inputs': ['vt_replacement_064'], 'func': vt_replacement_d2_064}


def vt_replacement_d2_065(vt_replacement_065):
    feature = _clean(vt_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_065'] = {'inputs': ['vt_replacement_065'], 'func': vt_replacement_d2_065}


def vt_replacement_d2_066(vt_replacement_066):
    feature = _clean(vt_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_066'] = {'inputs': ['vt_replacement_066'], 'func': vt_replacement_d2_066}


def vt_replacement_d2_067(vt_replacement_067):
    feature = _clean(vt_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_067'] = {'inputs': ['vt_replacement_067'], 'func': vt_replacement_d2_067}


def vt_replacement_d2_068(vt_replacement_068):
    feature = _clean(vt_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_068'] = {'inputs': ['vt_replacement_068'], 'func': vt_replacement_d2_068}


def vt_replacement_d2_069(vt_replacement_069):
    feature = _clean(vt_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_069'] = {'inputs': ['vt_replacement_069'], 'func': vt_replacement_d2_069}


def vt_replacement_d2_070(vt_replacement_070):
    feature = _clean(vt_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_070'] = {'inputs': ['vt_replacement_070'], 'func': vt_replacement_d2_070}


def vt_replacement_d2_071(vt_replacement_071):
    feature = _clean(vt_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_071'] = {'inputs': ['vt_replacement_071'], 'func': vt_replacement_d2_071}


def vt_replacement_d2_072(vt_replacement_072):
    feature = _clean(vt_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_072'] = {'inputs': ['vt_replacement_072'], 'func': vt_replacement_d2_072}


def vt_replacement_d2_073(vt_replacement_073):
    feature = _clean(vt_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_073'] = {'inputs': ['vt_replacement_073'], 'func': vt_replacement_d2_073}


def vt_replacement_d2_074(vt_replacement_074):
    feature = _clean(vt_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_074'] = {'inputs': ['vt_replacement_074'], 'func': vt_replacement_d2_074}


def vt_replacement_d2_075(vt_replacement_075):
    feature = _clean(vt_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_075'] = {'inputs': ['vt_replacement_075'], 'func': vt_replacement_d2_075}


def vt_replacement_d2_076(vt_replacement_076):
    feature = _clean(vt_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_076'] = {'inputs': ['vt_replacement_076'], 'func': vt_replacement_d2_076}


def vt_replacement_d2_077(vt_replacement_077):
    feature = _clean(vt_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_077'] = {'inputs': ['vt_replacement_077'], 'func': vt_replacement_d2_077}


def vt_replacement_d2_078(vt_replacement_078):
    feature = _clean(vt_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_078'] = {'inputs': ['vt_replacement_078'], 'func': vt_replacement_d2_078}


def vt_replacement_d2_079(vt_replacement_079):
    feature = _clean(vt_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_079'] = {'inputs': ['vt_replacement_079'], 'func': vt_replacement_d2_079}


def vt_replacement_d2_080(vt_replacement_080):
    feature = _clean(vt_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_080'] = {'inputs': ['vt_replacement_080'], 'func': vt_replacement_d2_080}


def vt_replacement_d2_081(vt_replacement_081):
    feature = _clean(vt_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_081'] = {'inputs': ['vt_replacement_081'], 'func': vt_replacement_d2_081}


def vt_replacement_d2_082(vt_replacement_082):
    feature = _clean(vt_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_082'] = {'inputs': ['vt_replacement_082'], 'func': vt_replacement_d2_082}


def vt_replacement_d2_083(vt_replacement_083):
    feature = _clean(vt_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_083'] = {'inputs': ['vt_replacement_083'], 'func': vt_replacement_d2_083}


def vt_replacement_d2_084(vt_replacement_084):
    feature = _clean(vt_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_084'] = {'inputs': ['vt_replacement_084'], 'func': vt_replacement_d2_084}


def vt_replacement_d2_085(vt_replacement_085):
    feature = _clean(vt_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_085'] = {'inputs': ['vt_replacement_085'], 'func': vt_replacement_d2_085}


def vt_replacement_d2_086(vt_replacement_086):
    feature = _clean(vt_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_086'] = {'inputs': ['vt_replacement_086'], 'func': vt_replacement_d2_086}


def vt_replacement_d2_087(vt_replacement_087):
    feature = _clean(vt_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_087'] = {'inputs': ['vt_replacement_087'], 'func': vt_replacement_d2_087}


def vt_replacement_d2_088(vt_replacement_088):
    feature = _clean(vt_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_088'] = {'inputs': ['vt_replacement_088'], 'func': vt_replacement_d2_088}


def vt_replacement_d2_089(vt_replacement_089):
    feature = _clean(vt_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_089'] = {'inputs': ['vt_replacement_089'], 'func': vt_replacement_d2_089}


def vt_replacement_d2_090(vt_replacement_090):
    feature = _clean(vt_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_090'] = {'inputs': ['vt_replacement_090'], 'func': vt_replacement_d2_090}


def vt_replacement_d2_091(vt_replacement_091):
    feature = _clean(vt_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_091'] = {'inputs': ['vt_replacement_091'], 'func': vt_replacement_d2_091}


def vt_replacement_d2_092(vt_replacement_092):
    feature = _clean(vt_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_092'] = {'inputs': ['vt_replacement_092'], 'func': vt_replacement_d2_092}


def vt_replacement_d2_093(vt_replacement_093):
    feature = _clean(vt_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_093'] = {'inputs': ['vt_replacement_093'], 'func': vt_replacement_d2_093}


def vt_replacement_d2_094(vt_replacement_094):
    feature = _clean(vt_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_094'] = {'inputs': ['vt_replacement_094'], 'func': vt_replacement_d2_094}


def vt_replacement_d2_095(vt_replacement_095):
    feature = _clean(vt_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_095'] = {'inputs': ['vt_replacement_095'], 'func': vt_replacement_d2_095}


def vt_replacement_d2_096(vt_replacement_096):
    feature = _clean(vt_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_096'] = {'inputs': ['vt_replacement_096'], 'func': vt_replacement_d2_096}


def vt_replacement_d2_097(vt_replacement_097):
    feature = _clean(vt_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_097'] = {'inputs': ['vt_replacement_097'], 'func': vt_replacement_d2_097}


def vt_replacement_d2_098(vt_replacement_098):
    feature = _clean(vt_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_098'] = {'inputs': ['vt_replacement_098'], 'func': vt_replacement_d2_098}


def vt_replacement_d2_099(vt_replacement_099):
    feature = _clean(vt_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_099'] = {'inputs': ['vt_replacement_099'], 'func': vt_replacement_d2_099}


def vt_replacement_d2_100(vt_replacement_100):
    feature = _clean(vt_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_100'] = {'inputs': ['vt_replacement_100'], 'func': vt_replacement_d2_100}


def vt_replacement_d2_101(vt_replacement_101):
    feature = _clean(vt_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_101'] = {'inputs': ['vt_replacement_101'], 'func': vt_replacement_d2_101}


def vt_replacement_d2_102(vt_replacement_102):
    feature = _clean(vt_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_102'] = {'inputs': ['vt_replacement_102'], 'func': vt_replacement_d2_102}


def vt_replacement_d2_103(vt_replacement_103):
    feature = _clean(vt_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_103'] = {'inputs': ['vt_replacement_103'], 'func': vt_replacement_d2_103}


def vt_replacement_d2_104(vt_replacement_104):
    feature = _clean(vt_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_104'] = {'inputs': ['vt_replacement_104'], 'func': vt_replacement_d2_104}


def vt_replacement_d2_105(vt_replacement_105):
    feature = _clean(vt_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_105'] = {'inputs': ['vt_replacement_105'], 'func': vt_replacement_d2_105}


def vt_replacement_d2_106(vt_replacement_106):
    feature = _clean(vt_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_106'] = {'inputs': ['vt_replacement_106'], 'func': vt_replacement_d2_106}


def vt_replacement_d2_107(vt_replacement_107):
    feature = _clean(vt_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_107'] = {'inputs': ['vt_replacement_107'], 'func': vt_replacement_d2_107}


def vt_replacement_d2_108(vt_replacement_108):
    feature = _clean(vt_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_108'] = {'inputs': ['vt_replacement_108'], 'func': vt_replacement_d2_108}


def vt_replacement_d2_109(vt_replacement_109):
    feature = _clean(vt_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_109'] = {'inputs': ['vt_replacement_109'], 'func': vt_replacement_d2_109}


def vt_replacement_d2_110(vt_replacement_110):
    feature = _clean(vt_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_110'] = {'inputs': ['vt_replacement_110'], 'func': vt_replacement_d2_110}


def vt_replacement_d2_111(vt_replacement_111):
    feature = _clean(vt_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_111'] = {'inputs': ['vt_replacement_111'], 'func': vt_replacement_d2_111}


def vt_replacement_d2_112(vt_replacement_112):
    feature = _clean(vt_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_112'] = {'inputs': ['vt_replacement_112'], 'func': vt_replacement_d2_112}


def vt_replacement_d2_113(vt_replacement_113):
    feature = _clean(vt_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_113'] = {'inputs': ['vt_replacement_113'], 'func': vt_replacement_d2_113}


def vt_replacement_d2_114(vt_replacement_114):
    feature = _clean(vt_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_114'] = {'inputs': ['vt_replacement_114'], 'func': vt_replacement_d2_114}


def vt_replacement_d2_115(vt_replacement_115):
    feature = _clean(vt_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_115'] = {'inputs': ['vt_replacement_115'], 'func': vt_replacement_d2_115}


def vt_replacement_d2_116(vt_replacement_116):
    feature = _clean(vt_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_116'] = {'inputs': ['vt_replacement_116'], 'func': vt_replacement_d2_116}


def vt_replacement_d2_117(vt_replacement_117):
    feature = _clean(vt_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_117'] = {'inputs': ['vt_replacement_117'], 'func': vt_replacement_d2_117}


def vt_replacement_d2_118(vt_replacement_118):
    feature = _clean(vt_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_118'] = {'inputs': ['vt_replacement_118'], 'func': vt_replacement_d2_118}


def vt_replacement_d2_119(vt_replacement_119):
    feature = _clean(vt_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_119'] = {'inputs': ['vt_replacement_119'], 'func': vt_replacement_d2_119}


def vt_replacement_d2_120(vt_replacement_120):
    feature = _clean(vt_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_120'] = {'inputs': ['vt_replacement_120'], 'func': vt_replacement_d2_120}


def vt_replacement_d2_121(vt_replacement_121):
    feature = _clean(vt_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_121'] = {'inputs': ['vt_replacement_121'], 'func': vt_replacement_d2_121}


def vt_replacement_d2_122(vt_replacement_122):
    feature = _clean(vt_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_122'] = {'inputs': ['vt_replacement_122'], 'func': vt_replacement_d2_122}


def vt_replacement_d2_123(vt_replacement_123):
    feature = _clean(vt_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_123'] = {'inputs': ['vt_replacement_123'], 'func': vt_replacement_d2_123}


def vt_replacement_d2_124(vt_replacement_124):
    feature = _clean(vt_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_124'] = {'inputs': ['vt_replacement_124'], 'func': vt_replacement_d2_124}


def vt_replacement_d2_125(vt_replacement_125):
    feature = _clean(vt_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_125'] = {'inputs': ['vt_replacement_125'], 'func': vt_replacement_d2_125}


def vt_replacement_d2_126(vt_replacement_126):
    feature = _clean(vt_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_126'] = {'inputs': ['vt_replacement_126'], 'func': vt_replacement_d2_126}


def vt_replacement_d2_127(vt_replacement_127):
    feature = _clean(vt_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_127'] = {'inputs': ['vt_replacement_127'], 'func': vt_replacement_d2_127}


def vt_replacement_d2_128(vt_replacement_128):
    feature = _clean(vt_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_128'] = {'inputs': ['vt_replacement_128'], 'func': vt_replacement_d2_128}


def vt_replacement_d2_129(vt_replacement_129):
    feature = _clean(vt_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_129'] = {'inputs': ['vt_replacement_129'], 'func': vt_replacement_d2_129}


def vt_replacement_d2_130(vt_replacement_130):
    feature = _clean(vt_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_130'] = {'inputs': ['vt_replacement_130'], 'func': vt_replacement_d2_130}


def vt_replacement_d2_131(vt_replacement_131):
    feature = _clean(vt_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_131'] = {'inputs': ['vt_replacement_131'], 'func': vt_replacement_d2_131}


def vt_replacement_d2_132(vt_replacement_132):
    feature = _clean(vt_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_132'] = {'inputs': ['vt_replacement_132'], 'func': vt_replacement_d2_132}


def vt_replacement_d2_133(vt_replacement_133):
    feature = _clean(vt_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_133'] = {'inputs': ['vt_replacement_133'], 'func': vt_replacement_d2_133}


def vt_replacement_d2_134(vt_replacement_134):
    feature = _clean(vt_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_134'] = {'inputs': ['vt_replacement_134'], 'func': vt_replacement_d2_134}


def vt_replacement_d2_135(vt_replacement_135):
    feature = _clean(vt_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_135'] = {'inputs': ['vt_replacement_135'], 'func': vt_replacement_d2_135}


def vt_replacement_d2_136(vt_replacement_136):
    feature = _clean(vt_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_136'] = {'inputs': ['vt_replacement_136'], 'func': vt_replacement_d2_136}


def vt_replacement_d2_137(vt_replacement_137):
    feature = _clean(vt_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_137'] = {'inputs': ['vt_replacement_137'], 'func': vt_replacement_d2_137}


def vt_replacement_d2_138(vt_replacement_138):
    feature = _clean(vt_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_138'] = {'inputs': ['vt_replacement_138'], 'func': vt_replacement_d2_138}


def vt_replacement_d2_139(vt_replacement_139):
    feature = _clean(vt_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_139'] = {'inputs': ['vt_replacement_139'], 'func': vt_replacement_d2_139}


def vt_replacement_d2_140(vt_replacement_140):
    feature = _clean(vt_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_140'] = {'inputs': ['vt_replacement_140'], 'func': vt_replacement_d2_140}


def vt_replacement_d2_141(vt_replacement_141):
    feature = _clean(vt_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_141'] = {'inputs': ['vt_replacement_141'], 'func': vt_replacement_d2_141}


def vt_replacement_d2_142(vt_replacement_142):
    feature = _clean(vt_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_142'] = {'inputs': ['vt_replacement_142'], 'func': vt_replacement_d2_142}


def vt_replacement_d2_143(vt_replacement_143):
    feature = _clean(vt_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_143'] = {'inputs': ['vt_replacement_143'], 'func': vt_replacement_d2_143}


def vt_replacement_d2_144(vt_replacement_144):
    feature = _clean(vt_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_144'] = {'inputs': ['vt_replacement_144'], 'func': vt_replacement_d2_144}


def vt_replacement_d2_145(vt_replacement_145):
    feature = _clean(vt_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_145'] = {'inputs': ['vt_replacement_145'], 'func': vt_replacement_d2_145}


def vt_replacement_d2_146(vt_replacement_146):
    feature = _clean(vt_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_146'] = {'inputs': ['vt_replacement_146'], 'func': vt_replacement_d2_146}


def vt_replacement_d2_147(vt_replacement_147):
    feature = _clean(vt_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_147'] = {'inputs': ['vt_replacement_147'], 'func': vt_replacement_d2_147}


def vt_replacement_d2_148(vt_replacement_148):
    feature = _clean(vt_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_148'] = {'inputs': ['vt_replacement_148'], 'func': vt_replacement_d2_148}


def vt_replacement_d2_149(vt_replacement_149):
    feature = _clean(vt_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_149'] = {'inputs': ['vt_replacement_149'], 'func': vt_replacement_d2_149}


def vt_replacement_d2_150(vt_replacement_150):
    feature = _clean(vt_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_150'] = {'inputs': ['vt_replacement_150'], 'func': vt_replacement_d2_150}


def vt_replacement_d2_151(vt_replacement_151):
    feature = _clean(vt_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_151'] = {'inputs': ['vt_replacement_151'], 'func': vt_replacement_d2_151}


def vt_replacement_d2_152(vt_replacement_152):
    feature = _clean(vt_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_152'] = {'inputs': ['vt_replacement_152'], 'func': vt_replacement_d2_152}


def vt_replacement_d2_153(vt_replacement_153):
    feature = _clean(vt_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_153'] = {'inputs': ['vt_replacement_153'], 'func': vt_replacement_d2_153}


def vt_replacement_d2_154(vt_replacement_154):
    feature = _clean(vt_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_154'] = {'inputs': ['vt_replacement_154'], 'func': vt_replacement_d2_154}


def vt_replacement_d2_155(vt_replacement_155):
    feature = _clean(vt_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_155'] = {'inputs': ['vt_replacement_155'], 'func': vt_replacement_d2_155}


def vt_replacement_d2_156(vt_replacement_156):
    feature = _clean(vt_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_156'] = {'inputs': ['vt_replacement_156'], 'func': vt_replacement_d2_156}


def vt_replacement_d2_157(vt_replacement_157):
    feature = _clean(vt_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_157'] = {'inputs': ['vt_replacement_157'], 'func': vt_replacement_d2_157}


def vt_replacement_d2_158(vt_replacement_158):
    feature = _clean(vt_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_158'] = {'inputs': ['vt_replacement_158'], 'func': vt_replacement_d2_158}


def vt_replacement_d2_159(vt_replacement_159):
    feature = _clean(vt_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_159'] = {'inputs': ['vt_replacement_159'], 'func': vt_replacement_d2_159}


def vt_replacement_d2_160(vt_replacement_160):
    feature = _clean(vt_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
VT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vt_replacement_d2_160'] = {'inputs': ['vt_replacement_160'], 'func': vt_replacement_d2_160}


# Base-universe derivative extensions for repaired first-base features.
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def vtr_base_universe_d2_001_vtr_002_volume_zscore_10_002(vtr_002_volume_zscore_10_002):
    return _base_universe_d2(vtr_002_volume_zscore_10_002, 1)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_001_vtr_002_volume_zscore_10_002'] = {'inputs': ['vtr_002_volume_zscore_10_002'], 'func': vtr_base_universe_d2_001_vtr_002_volume_zscore_10_002}


def vtr_base_universe_d2_002_vtr_003_down_volume_share_21_003(vtr_003_down_volume_share_21_003):
    return _base_universe_d2(vtr_003_down_volume_share_21_003, 2)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_002_vtr_003_down_volume_share_21_003'] = {'inputs': ['vtr_003_down_volume_share_21_003'], 'func': vtr_base_universe_d2_002_vtr_003_down_volume_share_21_003}


def vtr_base_universe_d2_003_vtr_004_dollar_volume_shock_42_004(vtr_004_dollar_volume_shock_42_004):
    return _base_universe_d2(vtr_004_dollar_volume_shock_42_004, 3)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_003_vtr_004_dollar_volume_shock_42_004'] = {'inputs': ['vtr_004_dollar_volume_shock_42_004'], 'func': vtr_base_universe_d2_003_vtr_004_dollar_volume_shock_42_004}


def vtr_base_universe_d2_004_vtr_005_volume_trend_slope_63_005(vtr_005_volume_trend_slope_63_005):
    return _base_universe_d2(vtr_005_volume_trend_slope_63_005, 4)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_004_vtr_005_volume_trend_slope_63_005'] = {'inputs': ['vtr_005_volume_trend_slope_63_005'], 'func': vtr_base_universe_d2_004_vtr_005_volume_trend_slope_63_005}


def vtr_base_universe_d2_005_vtr_006_price_volume_divergence_84_006(vtr_006_price_volume_divergence_84_006):
    return _base_universe_d2(vtr_006_price_volume_divergence_84_006, 5)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_005_vtr_006_price_volume_divergence_84_006'] = {'inputs': ['vtr_006_price_volume_divergence_84_006'], 'func': vtr_base_universe_d2_005_vtr_006_price_volume_divergence_84_006}


def vtr_base_universe_d2_006_vtr_008_volume_zscore_189_008(vtr_008_volume_zscore_189_008):
    return _base_universe_d2(vtr_008_volume_zscore_189_008, 6)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_006_vtr_008_volume_zscore_189_008'] = {'inputs': ['vtr_008_volume_zscore_189_008'], 'func': vtr_base_universe_d2_006_vtr_008_volume_zscore_189_008}


def vtr_base_universe_d2_007_vtr_009_down_volume_share_252_009(vtr_009_down_volume_share_252_009):
    return _base_universe_d2(vtr_009_down_volume_share_252_009, 7)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_007_vtr_009_down_volume_share_252_009'] = {'inputs': ['vtr_009_down_volume_share_252_009'], 'func': vtr_base_universe_d2_007_vtr_009_down_volume_share_252_009}


def vtr_base_universe_d2_008_vtr_010_dollar_volume_shock_378_010(vtr_010_dollar_volume_shock_378_010):
    return _base_universe_d2(vtr_010_dollar_volume_shock_378_010, 8)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_008_vtr_010_dollar_volume_shock_378_010'] = {'inputs': ['vtr_010_dollar_volume_shock_378_010'], 'func': vtr_base_universe_d2_008_vtr_010_dollar_volume_shock_378_010}


def vtr_base_universe_d2_009_vtr_011_volume_trend_slope_504_011(vtr_011_volume_trend_slope_504_011):
    return _base_universe_d2(vtr_011_volume_trend_slope_504_011, 9)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_009_vtr_011_volume_trend_slope_504_011'] = {'inputs': ['vtr_011_volume_trend_slope_504_011'], 'func': vtr_base_universe_d2_009_vtr_011_volume_trend_slope_504_011}


def vtr_base_universe_d2_010_vtr_012_price_volume_divergence_756_012(vtr_012_price_volume_divergence_756_012):
    return _base_universe_d2(vtr_012_price_volume_divergence_756_012, 10)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_010_vtr_012_price_volume_divergence_756_012'] = {'inputs': ['vtr_012_price_volume_divergence_756_012'], 'func': vtr_base_universe_d2_010_vtr_012_price_volume_divergence_756_012}


def vtr_base_universe_d2_011_vtr_014_volume_zscore_1260_014(vtr_014_volume_zscore_1260_014):
    return _base_universe_d2(vtr_014_volume_zscore_1260_014, 11)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_011_vtr_014_volume_zscore_1260_014'] = {'inputs': ['vtr_014_volume_zscore_1260_014'], 'func': vtr_base_universe_d2_011_vtr_014_volume_zscore_1260_014}


def vtr_base_universe_d2_012_vtr_015_down_volume_share_1512_015(vtr_015_down_volume_share_1512_015):
    return _base_universe_d2(vtr_015_down_volume_share_1512_015, 12)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_012_vtr_015_down_volume_share_1512_015'] = {'inputs': ['vtr_015_down_volume_share_1512_015'], 'func': vtr_base_universe_d2_012_vtr_015_down_volume_share_1512_015}


def vtr_base_universe_d2_013_vtr_016_dollar_volume_shock_5_016(vtr_016_dollar_volume_shock_5_016):
    return _base_universe_d2(vtr_016_dollar_volume_shock_5_016, 13)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_013_vtr_016_dollar_volume_shock_5_016'] = {'inputs': ['vtr_016_dollar_volume_shock_5_016'], 'func': vtr_base_universe_d2_013_vtr_016_dollar_volume_shock_5_016}


def vtr_base_universe_d2_014_vtr_017_volume_trend_slope_10_017(vtr_017_volume_trend_slope_10_017):
    return _base_universe_d2(vtr_017_volume_trend_slope_10_017, 14)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_014_vtr_017_volume_trend_slope_10_017'] = {'inputs': ['vtr_017_volume_trend_slope_10_017'], 'func': vtr_base_universe_d2_014_vtr_017_volume_trend_slope_10_017}


def vtr_base_universe_d2_015_vtr_018_price_volume_divergence_21_018(vtr_018_price_volume_divergence_21_018):
    return _base_universe_d2(vtr_018_price_volume_divergence_21_018, 15)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_015_vtr_018_price_volume_divergence_21_018'] = {'inputs': ['vtr_018_price_volume_divergence_21_018'], 'func': vtr_base_universe_d2_015_vtr_018_price_volume_divergence_21_018}


def vtr_base_universe_d2_016_vtr_020_volume_zscore_63_020(vtr_020_volume_zscore_63_020):
    return _base_universe_d2(vtr_020_volume_zscore_63_020, 16)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_016_vtr_020_volume_zscore_63_020'] = {'inputs': ['vtr_020_volume_zscore_63_020'], 'func': vtr_base_universe_d2_016_vtr_020_volume_zscore_63_020}


def vtr_base_universe_d2_017_vtr_021_down_volume_share_84_021(vtr_021_down_volume_share_84_021):
    return _base_universe_d2(vtr_021_down_volume_share_84_021, 17)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_017_vtr_021_down_volume_share_84_021'] = {'inputs': ['vtr_021_down_volume_share_84_021'], 'func': vtr_base_universe_d2_017_vtr_021_down_volume_share_84_021}


def vtr_base_universe_d2_018_vtr_022_dollar_volume_shock_126_022(vtr_022_dollar_volume_shock_126_022):
    return _base_universe_d2(vtr_022_dollar_volume_shock_126_022, 18)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_018_vtr_022_dollar_volume_shock_126_022'] = {'inputs': ['vtr_022_dollar_volume_shock_126_022'], 'func': vtr_base_universe_d2_018_vtr_022_dollar_volume_shock_126_022}


def vtr_base_universe_d2_019_vtr_023_volume_trend_slope_189_023(vtr_023_volume_trend_slope_189_023):
    return _base_universe_d2(vtr_023_volume_trend_slope_189_023, 19)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_019_vtr_023_volume_trend_slope_189_023'] = {'inputs': ['vtr_023_volume_trend_slope_189_023'], 'func': vtr_base_universe_d2_019_vtr_023_volume_trend_slope_189_023}


def vtr_base_universe_d2_020_vtr_024_price_volume_divergence_252_024(vtr_024_price_volume_divergence_252_024):
    return _base_universe_d2(vtr_024_price_volume_divergence_252_024, 20)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_020_vtr_024_price_volume_divergence_252_024'] = {'inputs': ['vtr_024_price_volume_divergence_252_024'], 'func': vtr_base_universe_d2_020_vtr_024_price_volume_divergence_252_024}


def vtr_base_universe_d2_021_vtr_026_volume_zscore_504_026(vtr_026_volume_zscore_504_026):
    return _base_universe_d2(vtr_026_volume_zscore_504_026, 21)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_021_vtr_026_volume_zscore_504_026'] = {'inputs': ['vtr_026_volume_zscore_504_026'], 'func': vtr_base_universe_d2_021_vtr_026_volume_zscore_504_026}


def vtr_base_universe_d2_022_vtr_027_down_volume_share_756_027(vtr_027_down_volume_share_756_027):
    return _base_universe_d2(vtr_027_down_volume_share_756_027, 22)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_022_vtr_027_down_volume_share_756_027'] = {'inputs': ['vtr_027_down_volume_share_756_027'], 'func': vtr_base_universe_d2_022_vtr_027_down_volume_share_756_027}


def vtr_base_universe_d2_023_vtr_028_dollar_volume_shock_1008_028(vtr_028_dollar_volume_shock_1008_028):
    return _base_universe_d2(vtr_028_dollar_volume_shock_1008_028, 23)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_023_vtr_028_dollar_volume_shock_1008_028'] = {'inputs': ['vtr_028_dollar_volume_shock_1008_028'], 'func': vtr_base_universe_d2_023_vtr_028_dollar_volume_shock_1008_028}


def vtr_base_universe_d2_024_vtr_029_volume_trend_slope_1260_029(vtr_029_volume_trend_slope_1260_029):
    return _base_universe_d2(vtr_029_volume_trend_slope_1260_029, 24)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_024_vtr_029_volume_trend_slope_1260_029'] = {'inputs': ['vtr_029_volume_trend_slope_1260_029'], 'func': vtr_base_universe_d2_024_vtr_029_volume_trend_slope_1260_029}


def vtr_base_universe_d2_025_vtr_030_price_volume_divergence_1512_030(vtr_030_price_volume_divergence_1512_030):
    return _base_universe_d2(vtr_030_price_volume_divergence_1512_030, 25)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_025_vtr_030_price_volume_divergence_1512_030'] = {'inputs': ['vtr_030_price_volume_divergence_1512_030'], 'func': vtr_base_universe_d2_025_vtr_030_price_volume_divergence_1512_030}


def vtr_base_universe_d2_026_vtr_basefill_031(vtr_basefill_031):
    return _base_universe_d2(vtr_basefill_031, 26)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_026_vtr_basefill_031'] = {'inputs': ['vtr_basefill_031'], 'func': vtr_base_universe_d2_026_vtr_basefill_031}


def vtr_base_universe_d2_027_vtr_basefill_032(vtr_basefill_032):
    return _base_universe_d2(vtr_basefill_032, 27)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_027_vtr_basefill_032'] = {'inputs': ['vtr_basefill_032'], 'func': vtr_base_universe_d2_027_vtr_basefill_032}


def vtr_base_universe_d2_028_vtr_basefill_033(vtr_basefill_033):
    return _base_universe_d2(vtr_basefill_033, 28)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_028_vtr_basefill_033'] = {'inputs': ['vtr_basefill_033'], 'func': vtr_base_universe_d2_028_vtr_basefill_033}


def vtr_base_universe_d2_029_vtr_basefill_034(vtr_basefill_034):
    return _base_universe_d2(vtr_basefill_034, 29)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_029_vtr_basefill_034'] = {'inputs': ['vtr_basefill_034'], 'func': vtr_base_universe_d2_029_vtr_basefill_034}


def vtr_base_universe_d2_030_vtr_basefill_035(vtr_basefill_035):
    return _base_universe_d2(vtr_basefill_035, 30)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_030_vtr_basefill_035'] = {'inputs': ['vtr_basefill_035'], 'func': vtr_base_universe_d2_030_vtr_basefill_035}


def vtr_base_universe_d2_031_vtr_basefill_036(vtr_basefill_036):
    return _base_universe_d2(vtr_basefill_036, 31)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_031_vtr_basefill_036'] = {'inputs': ['vtr_basefill_036'], 'func': vtr_base_universe_d2_031_vtr_basefill_036}


def vtr_base_universe_d2_032_vtr_basefill_037(vtr_basefill_037):
    return _base_universe_d2(vtr_basefill_037, 32)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_032_vtr_basefill_037'] = {'inputs': ['vtr_basefill_037'], 'func': vtr_base_universe_d2_032_vtr_basefill_037}


def vtr_base_universe_d2_033_vtr_basefill_038(vtr_basefill_038):
    return _base_universe_d2(vtr_basefill_038, 33)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_033_vtr_basefill_038'] = {'inputs': ['vtr_basefill_038'], 'func': vtr_base_universe_d2_033_vtr_basefill_038}


def vtr_base_universe_d2_034_vtr_basefill_039(vtr_basefill_039):
    return _base_universe_d2(vtr_basefill_039, 34)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_034_vtr_basefill_039'] = {'inputs': ['vtr_basefill_039'], 'func': vtr_base_universe_d2_034_vtr_basefill_039}


def vtr_base_universe_d2_035_vtr_basefill_040(vtr_basefill_040):
    return _base_universe_d2(vtr_basefill_040, 35)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_035_vtr_basefill_040'] = {'inputs': ['vtr_basefill_040'], 'func': vtr_base_universe_d2_035_vtr_basefill_040}


def vtr_base_universe_d2_036_vtr_basefill_041(vtr_basefill_041):
    return _base_universe_d2(vtr_basefill_041, 36)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_036_vtr_basefill_041'] = {'inputs': ['vtr_basefill_041'], 'func': vtr_base_universe_d2_036_vtr_basefill_041}


def vtr_base_universe_d2_037_vtr_basefill_042(vtr_basefill_042):
    return _base_universe_d2(vtr_basefill_042, 37)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_037_vtr_basefill_042'] = {'inputs': ['vtr_basefill_042'], 'func': vtr_base_universe_d2_037_vtr_basefill_042}


def vtr_base_universe_d2_038_vtr_basefill_043(vtr_basefill_043):
    return _base_universe_d2(vtr_basefill_043, 38)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_038_vtr_basefill_043'] = {'inputs': ['vtr_basefill_043'], 'func': vtr_base_universe_d2_038_vtr_basefill_043}


def vtr_base_universe_d2_039_vtr_basefill_044(vtr_basefill_044):
    return _base_universe_d2(vtr_basefill_044, 39)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_039_vtr_basefill_044'] = {'inputs': ['vtr_basefill_044'], 'func': vtr_base_universe_d2_039_vtr_basefill_044}


def vtr_base_universe_d2_040_vtr_basefill_045(vtr_basefill_045):
    return _base_universe_d2(vtr_basefill_045, 40)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_040_vtr_basefill_045'] = {'inputs': ['vtr_basefill_045'], 'func': vtr_base_universe_d2_040_vtr_basefill_045}


def vtr_base_universe_d2_041_vtr_basefill_046(vtr_basefill_046):
    return _base_universe_d2(vtr_basefill_046, 41)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_041_vtr_basefill_046'] = {'inputs': ['vtr_basefill_046'], 'func': vtr_base_universe_d2_041_vtr_basefill_046}


def vtr_base_universe_d2_042_vtr_basefill_047(vtr_basefill_047):
    return _base_universe_d2(vtr_basefill_047, 42)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_042_vtr_basefill_047'] = {'inputs': ['vtr_basefill_047'], 'func': vtr_base_universe_d2_042_vtr_basefill_047}


def vtr_base_universe_d2_043_vtr_basefill_048(vtr_basefill_048):
    return _base_universe_d2(vtr_basefill_048, 43)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_043_vtr_basefill_048'] = {'inputs': ['vtr_basefill_048'], 'func': vtr_base_universe_d2_043_vtr_basefill_048}


def vtr_base_universe_d2_044_vtr_basefill_049(vtr_basefill_049):
    return _base_universe_d2(vtr_basefill_049, 44)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_044_vtr_basefill_049'] = {'inputs': ['vtr_basefill_049'], 'func': vtr_base_universe_d2_044_vtr_basefill_049}


def vtr_base_universe_d2_045_vtr_basefill_050(vtr_basefill_050):
    return _base_universe_d2(vtr_basefill_050, 45)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_045_vtr_basefill_050'] = {'inputs': ['vtr_basefill_050'], 'func': vtr_base_universe_d2_045_vtr_basefill_050}


def vtr_base_universe_d2_046_vtr_basefill_051(vtr_basefill_051):
    return _base_universe_d2(vtr_basefill_051, 46)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_046_vtr_basefill_051'] = {'inputs': ['vtr_basefill_051'], 'func': vtr_base_universe_d2_046_vtr_basefill_051}


def vtr_base_universe_d2_047_vtr_basefill_052(vtr_basefill_052):
    return _base_universe_d2(vtr_basefill_052, 47)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_047_vtr_basefill_052'] = {'inputs': ['vtr_basefill_052'], 'func': vtr_base_universe_d2_047_vtr_basefill_052}


def vtr_base_universe_d2_048_vtr_basefill_053(vtr_basefill_053):
    return _base_universe_d2(vtr_basefill_053, 48)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_048_vtr_basefill_053'] = {'inputs': ['vtr_basefill_053'], 'func': vtr_base_universe_d2_048_vtr_basefill_053}


def vtr_base_universe_d2_049_vtr_basefill_054(vtr_basefill_054):
    return _base_universe_d2(vtr_basefill_054, 49)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_049_vtr_basefill_054'] = {'inputs': ['vtr_basefill_054'], 'func': vtr_base_universe_d2_049_vtr_basefill_054}


def vtr_base_universe_d2_050_vtr_basefill_055(vtr_basefill_055):
    return _base_universe_d2(vtr_basefill_055, 50)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_050_vtr_basefill_055'] = {'inputs': ['vtr_basefill_055'], 'func': vtr_base_universe_d2_050_vtr_basefill_055}


def vtr_base_universe_d2_051_vtr_basefill_056(vtr_basefill_056):
    return _base_universe_d2(vtr_basefill_056, 51)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_051_vtr_basefill_056'] = {'inputs': ['vtr_basefill_056'], 'func': vtr_base_universe_d2_051_vtr_basefill_056}


def vtr_base_universe_d2_052_vtr_basefill_057(vtr_basefill_057):
    return _base_universe_d2(vtr_basefill_057, 52)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_052_vtr_basefill_057'] = {'inputs': ['vtr_basefill_057'], 'func': vtr_base_universe_d2_052_vtr_basefill_057}


def vtr_base_universe_d2_053_vtr_basefill_058(vtr_basefill_058):
    return _base_universe_d2(vtr_basefill_058, 53)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_053_vtr_basefill_058'] = {'inputs': ['vtr_basefill_058'], 'func': vtr_base_universe_d2_053_vtr_basefill_058}


def vtr_base_universe_d2_054_vtr_basefill_059(vtr_basefill_059):
    return _base_universe_d2(vtr_basefill_059, 54)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_054_vtr_basefill_059'] = {'inputs': ['vtr_basefill_059'], 'func': vtr_base_universe_d2_054_vtr_basefill_059}


def vtr_base_universe_d2_055_vtr_basefill_060(vtr_basefill_060):
    return _base_universe_d2(vtr_basefill_060, 55)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_055_vtr_basefill_060'] = {'inputs': ['vtr_basefill_060'], 'func': vtr_base_universe_d2_055_vtr_basefill_060}


def vtr_base_universe_d2_056_vtr_basefill_061(vtr_basefill_061):
    return _base_universe_d2(vtr_basefill_061, 56)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_056_vtr_basefill_061'] = {'inputs': ['vtr_basefill_061'], 'func': vtr_base_universe_d2_056_vtr_basefill_061}


def vtr_base_universe_d2_057_vtr_basefill_062(vtr_basefill_062):
    return _base_universe_d2(vtr_basefill_062, 57)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_057_vtr_basefill_062'] = {'inputs': ['vtr_basefill_062'], 'func': vtr_base_universe_d2_057_vtr_basefill_062}


def vtr_base_universe_d2_058_vtr_basefill_063(vtr_basefill_063):
    return _base_universe_d2(vtr_basefill_063, 58)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_058_vtr_basefill_063'] = {'inputs': ['vtr_basefill_063'], 'func': vtr_base_universe_d2_058_vtr_basefill_063}


def vtr_base_universe_d2_059_vtr_basefill_064(vtr_basefill_064):
    return _base_universe_d2(vtr_basefill_064, 59)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_059_vtr_basefill_064'] = {'inputs': ['vtr_basefill_064'], 'func': vtr_base_universe_d2_059_vtr_basefill_064}


def vtr_base_universe_d2_060_vtr_basefill_065(vtr_basefill_065):
    return _base_universe_d2(vtr_basefill_065, 60)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_060_vtr_basefill_065'] = {'inputs': ['vtr_basefill_065'], 'func': vtr_base_universe_d2_060_vtr_basefill_065}


def vtr_base_universe_d2_061_vtr_basefill_066(vtr_basefill_066):
    return _base_universe_d2(vtr_basefill_066, 61)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_061_vtr_basefill_066'] = {'inputs': ['vtr_basefill_066'], 'func': vtr_base_universe_d2_061_vtr_basefill_066}


def vtr_base_universe_d2_062_vtr_basefill_067(vtr_basefill_067):
    return _base_universe_d2(vtr_basefill_067, 62)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_062_vtr_basefill_067'] = {'inputs': ['vtr_basefill_067'], 'func': vtr_base_universe_d2_062_vtr_basefill_067}


def vtr_base_universe_d2_063_vtr_basefill_068(vtr_basefill_068):
    return _base_universe_d2(vtr_basefill_068, 63)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_063_vtr_basefill_068'] = {'inputs': ['vtr_basefill_068'], 'func': vtr_base_universe_d2_063_vtr_basefill_068}


def vtr_base_universe_d2_064_vtr_basefill_069(vtr_basefill_069):
    return _base_universe_d2(vtr_basefill_069, 64)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_064_vtr_basefill_069'] = {'inputs': ['vtr_basefill_069'], 'func': vtr_base_universe_d2_064_vtr_basefill_069}


def vtr_base_universe_d2_065_vtr_basefill_070(vtr_basefill_070):
    return _base_universe_d2(vtr_basefill_070, 65)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_065_vtr_basefill_070'] = {'inputs': ['vtr_basefill_070'], 'func': vtr_base_universe_d2_065_vtr_basefill_070}


def vtr_base_universe_d2_066_vtr_basefill_071(vtr_basefill_071):
    return _base_universe_d2(vtr_basefill_071, 66)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_066_vtr_basefill_071'] = {'inputs': ['vtr_basefill_071'], 'func': vtr_base_universe_d2_066_vtr_basefill_071}


def vtr_base_universe_d2_067_vtr_basefill_072(vtr_basefill_072):
    return _base_universe_d2(vtr_basefill_072, 67)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_067_vtr_basefill_072'] = {'inputs': ['vtr_basefill_072'], 'func': vtr_base_universe_d2_067_vtr_basefill_072}


def vtr_base_universe_d2_068_vtr_basefill_073(vtr_basefill_073):
    return _base_universe_d2(vtr_basefill_073, 68)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_068_vtr_basefill_073'] = {'inputs': ['vtr_basefill_073'], 'func': vtr_base_universe_d2_068_vtr_basefill_073}


def vtr_base_universe_d2_069_vtr_basefill_074(vtr_basefill_074):
    return _base_universe_d2(vtr_basefill_074, 69)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_069_vtr_basefill_074'] = {'inputs': ['vtr_basefill_074'], 'func': vtr_base_universe_d2_069_vtr_basefill_074}


def vtr_base_universe_d2_070_vtr_basefill_075(vtr_basefill_075):
    return _base_universe_d2(vtr_basefill_075, 70)
VTR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vtr_base_universe_d2_070_vtr_basefill_075'] = {'inputs': ['vtr_basefill_075'], 'func': vtr_base_universe_d2_070_vtr_basefill_075}
