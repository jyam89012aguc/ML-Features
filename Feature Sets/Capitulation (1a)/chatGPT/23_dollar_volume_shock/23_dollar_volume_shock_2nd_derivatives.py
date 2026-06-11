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



def dvs_151_dvs_001_volume_spike_ratio_5_001_roc_1(dvs_001_volume_spike_ratio_5_001):
    feature = _s(dvs_001_volume_spike_ratio_5_001)
    return (_roc(feature, 1)).reindex(feature.index)

def dvs_152_dvs_007_volume_spike_ratio_126_007_roc_5(dvs_007_volume_spike_ratio_126_007):
    feature = _s(dvs_007_volume_spike_ratio_126_007)
    return (_roc(feature, 5)).reindex(feature.index)

def dvs_153_dvs_013_volume_spike_ratio_1008_013_roc_42(dvs_013_volume_spike_ratio_1008_013):
    feature = _s(dvs_013_volume_spike_ratio_1008_013)
    return (_roc(feature, 42)).reindex(feature.index)

def dvs_154_dvs_019_volume_spike_ratio_42_019_roc_126(dvs_019_volume_spike_ratio_42_019):
    feature = _s(dvs_019_volume_spike_ratio_42_019)
    return (_roc(feature, 126)).reindex(feature.index)

def dvs_155_dvs_025_volume_spike_ratio_378_025_roc_378(dvs_025_volume_spike_ratio_378_025):
    feature = _s(dvs_025_volume_spike_ratio_378_025)
    return (_roc(feature, 378)).reindex(feature.index)






















DOLLAR_VOLUME_SHOCK_REGISTRY_2ND_DERIVATIVES = {
    'dvs_151_dvs_001_volume_spike_ratio_5_001_roc_1': {'inputs': ['dvs_001_volume_spike_ratio_5_001'], 'func': dvs_151_dvs_001_volume_spike_ratio_5_001_roc_1},
    'dvs_152_dvs_007_volume_spike_ratio_126_007_roc_5': {'inputs': ['dvs_007_volume_spike_ratio_126_007'], 'func': dvs_152_dvs_007_volume_spike_ratio_126_007_roc_5},
    'dvs_153_dvs_013_volume_spike_ratio_1008_013_roc_42': {'inputs': ['dvs_013_volume_spike_ratio_1008_013'], 'func': dvs_153_dvs_013_volume_spike_ratio_1008_013_roc_42},
    'dvs_154_dvs_019_volume_spike_ratio_42_019_roc_126': {'inputs': ['dvs_019_volume_spike_ratio_42_019'], 'func': dvs_154_dvs_019_volume_spike_ratio_42_019_roc_126},
    'dvs_155_dvs_025_volume_spike_ratio_378_025_roc_378': {'inputs': ['dvs_025_volume_spike_ratio_378_025'], 'func': dvs_155_dvs_025_volume_spike_ratio_378_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def dvs_replacement_d2_001(dvs_replacement_001):
    feature = _clean(dvs_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_001'] = {'inputs': ['dvs_replacement_001'], 'func': dvs_replacement_d2_001}


def dvs_replacement_d2_002(dvs_replacement_002):
    feature = _clean(dvs_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_002'] = {'inputs': ['dvs_replacement_002'], 'func': dvs_replacement_d2_002}


def dvs_replacement_d2_003(dvs_replacement_003):
    feature = _clean(dvs_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_003'] = {'inputs': ['dvs_replacement_003'], 'func': dvs_replacement_d2_003}


def dvs_replacement_d2_004(dvs_replacement_004):
    feature = _clean(dvs_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_004'] = {'inputs': ['dvs_replacement_004'], 'func': dvs_replacement_d2_004}


def dvs_replacement_d2_005(dvs_replacement_005):
    feature = _clean(dvs_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_005'] = {'inputs': ['dvs_replacement_005'], 'func': dvs_replacement_d2_005}


def dvs_replacement_d2_006(dvs_replacement_006):
    feature = _clean(dvs_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_006'] = {'inputs': ['dvs_replacement_006'], 'func': dvs_replacement_d2_006}


def dvs_replacement_d2_007(dvs_replacement_007):
    feature = _clean(dvs_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_007'] = {'inputs': ['dvs_replacement_007'], 'func': dvs_replacement_d2_007}


def dvs_replacement_d2_008(dvs_replacement_008):
    feature = _clean(dvs_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_008'] = {'inputs': ['dvs_replacement_008'], 'func': dvs_replacement_d2_008}


def dvs_replacement_d2_009(dvs_replacement_009):
    feature = _clean(dvs_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_009'] = {'inputs': ['dvs_replacement_009'], 'func': dvs_replacement_d2_009}


def dvs_replacement_d2_010(dvs_replacement_010):
    feature = _clean(dvs_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_010'] = {'inputs': ['dvs_replacement_010'], 'func': dvs_replacement_d2_010}


def dvs_replacement_d2_011(dvs_replacement_011):
    feature = _clean(dvs_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_011'] = {'inputs': ['dvs_replacement_011'], 'func': dvs_replacement_d2_011}


def dvs_replacement_d2_012(dvs_replacement_012):
    feature = _clean(dvs_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_012'] = {'inputs': ['dvs_replacement_012'], 'func': dvs_replacement_d2_012}


def dvs_replacement_d2_013(dvs_replacement_013):
    feature = _clean(dvs_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_013'] = {'inputs': ['dvs_replacement_013'], 'func': dvs_replacement_d2_013}


def dvs_replacement_d2_014(dvs_replacement_014):
    feature = _clean(dvs_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_014'] = {'inputs': ['dvs_replacement_014'], 'func': dvs_replacement_d2_014}


def dvs_replacement_d2_015(dvs_replacement_015):
    feature = _clean(dvs_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_015'] = {'inputs': ['dvs_replacement_015'], 'func': dvs_replacement_d2_015}


def dvs_replacement_d2_016(dvs_replacement_016):
    feature = _clean(dvs_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_016'] = {'inputs': ['dvs_replacement_016'], 'func': dvs_replacement_d2_016}


def dvs_replacement_d2_017(dvs_replacement_017):
    feature = _clean(dvs_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_017'] = {'inputs': ['dvs_replacement_017'], 'func': dvs_replacement_d2_017}


def dvs_replacement_d2_018(dvs_replacement_018):
    feature = _clean(dvs_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_018'] = {'inputs': ['dvs_replacement_018'], 'func': dvs_replacement_d2_018}


def dvs_replacement_d2_019(dvs_replacement_019):
    feature = _clean(dvs_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_019'] = {'inputs': ['dvs_replacement_019'], 'func': dvs_replacement_d2_019}


def dvs_replacement_d2_020(dvs_replacement_020):
    feature = _clean(dvs_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_020'] = {'inputs': ['dvs_replacement_020'], 'func': dvs_replacement_d2_020}


def dvs_replacement_d2_021(dvs_replacement_021):
    feature = _clean(dvs_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_021'] = {'inputs': ['dvs_replacement_021'], 'func': dvs_replacement_d2_021}


def dvs_replacement_d2_022(dvs_replacement_022):
    feature = _clean(dvs_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_022'] = {'inputs': ['dvs_replacement_022'], 'func': dvs_replacement_d2_022}


def dvs_replacement_d2_023(dvs_replacement_023):
    feature = _clean(dvs_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_023'] = {'inputs': ['dvs_replacement_023'], 'func': dvs_replacement_d2_023}


def dvs_replacement_d2_024(dvs_replacement_024):
    feature = _clean(dvs_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_024'] = {'inputs': ['dvs_replacement_024'], 'func': dvs_replacement_d2_024}


def dvs_replacement_d2_025(dvs_replacement_025):
    feature = _clean(dvs_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_025'] = {'inputs': ['dvs_replacement_025'], 'func': dvs_replacement_d2_025}


def dvs_replacement_d2_026(dvs_replacement_026):
    feature = _clean(dvs_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_026'] = {'inputs': ['dvs_replacement_026'], 'func': dvs_replacement_d2_026}


def dvs_replacement_d2_027(dvs_replacement_027):
    feature = _clean(dvs_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_027'] = {'inputs': ['dvs_replacement_027'], 'func': dvs_replacement_d2_027}


def dvs_replacement_d2_028(dvs_replacement_028):
    feature = _clean(dvs_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_028'] = {'inputs': ['dvs_replacement_028'], 'func': dvs_replacement_d2_028}


def dvs_replacement_d2_029(dvs_replacement_029):
    feature = _clean(dvs_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_029'] = {'inputs': ['dvs_replacement_029'], 'func': dvs_replacement_d2_029}


def dvs_replacement_d2_030(dvs_replacement_030):
    feature = _clean(dvs_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_030'] = {'inputs': ['dvs_replacement_030'], 'func': dvs_replacement_d2_030}


def dvs_replacement_d2_031(dvs_replacement_031):
    feature = _clean(dvs_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_031'] = {'inputs': ['dvs_replacement_031'], 'func': dvs_replacement_d2_031}


def dvs_replacement_d2_032(dvs_replacement_032):
    feature = _clean(dvs_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_032'] = {'inputs': ['dvs_replacement_032'], 'func': dvs_replacement_d2_032}


def dvs_replacement_d2_033(dvs_replacement_033):
    feature = _clean(dvs_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_033'] = {'inputs': ['dvs_replacement_033'], 'func': dvs_replacement_d2_033}


def dvs_replacement_d2_034(dvs_replacement_034):
    feature = _clean(dvs_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_034'] = {'inputs': ['dvs_replacement_034'], 'func': dvs_replacement_d2_034}


def dvs_replacement_d2_035(dvs_replacement_035):
    feature = _clean(dvs_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_035'] = {'inputs': ['dvs_replacement_035'], 'func': dvs_replacement_d2_035}


def dvs_replacement_d2_036(dvs_replacement_036):
    feature = _clean(dvs_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_036'] = {'inputs': ['dvs_replacement_036'], 'func': dvs_replacement_d2_036}


def dvs_replacement_d2_037(dvs_replacement_037):
    feature = _clean(dvs_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_037'] = {'inputs': ['dvs_replacement_037'], 'func': dvs_replacement_d2_037}


def dvs_replacement_d2_038(dvs_replacement_038):
    feature = _clean(dvs_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_038'] = {'inputs': ['dvs_replacement_038'], 'func': dvs_replacement_d2_038}


def dvs_replacement_d2_039(dvs_replacement_039):
    feature = _clean(dvs_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_039'] = {'inputs': ['dvs_replacement_039'], 'func': dvs_replacement_d2_039}


def dvs_replacement_d2_040(dvs_replacement_040):
    feature = _clean(dvs_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_040'] = {'inputs': ['dvs_replacement_040'], 'func': dvs_replacement_d2_040}


def dvs_replacement_d2_041(dvs_replacement_041):
    feature = _clean(dvs_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_041'] = {'inputs': ['dvs_replacement_041'], 'func': dvs_replacement_d2_041}


def dvs_replacement_d2_042(dvs_replacement_042):
    feature = _clean(dvs_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_042'] = {'inputs': ['dvs_replacement_042'], 'func': dvs_replacement_d2_042}


def dvs_replacement_d2_043(dvs_replacement_043):
    feature = _clean(dvs_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_043'] = {'inputs': ['dvs_replacement_043'], 'func': dvs_replacement_d2_043}


def dvs_replacement_d2_044(dvs_replacement_044):
    feature = _clean(dvs_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_044'] = {'inputs': ['dvs_replacement_044'], 'func': dvs_replacement_d2_044}


def dvs_replacement_d2_045(dvs_replacement_045):
    feature = _clean(dvs_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_045'] = {'inputs': ['dvs_replacement_045'], 'func': dvs_replacement_d2_045}


def dvs_replacement_d2_046(dvs_replacement_046):
    feature = _clean(dvs_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_046'] = {'inputs': ['dvs_replacement_046'], 'func': dvs_replacement_d2_046}


def dvs_replacement_d2_047(dvs_replacement_047):
    feature = _clean(dvs_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_047'] = {'inputs': ['dvs_replacement_047'], 'func': dvs_replacement_d2_047}


def dvs_replacement_d2_048(dvs_replacement_048):
    feature = _clean(dvs_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_048'] = {'inputs': ['dvs_replacement_048'], 'func': dvs_replacement_d2_048}


def dvs_replacement_d2_049(dvs_replacement_049):
    feature = _clean(dvs_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_049'] = {'inputs': ['dvs_replacement_049'], 'func': dvs_replacement_d2_049}


def dvs_replacement_d2_050(dvs_replacement_050):
    feature = _clean(dvs_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_050'] = {'inputs': ['dvs_replacement_050'], 'func': dvs_replacement_d2_050}


def dvs_replacement_d2_051(dvs_replacement_051):
    feature = _clean(dvs_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_051'] = {'inputs': ['dvs_replacement_051'], 'func': dvs_replacement_d2_051}


def dvs_replacement_d2_052(dvs_replacement_052):
    feature = _clean(dvs_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_052'] = {'inputs': ['dvs_replacement_052'], 'func': dvs_replacement_d2_052}


def dvs_replacement_d2_053(dvs_replacement_053):
    feature = _clean(dvs_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_053'] = {'inputs': ['dvs_replacement_053'], 'func': dvs_replacement_d2_053}


def dvs_replacement_d2_054(dvs_replacement_054):
    feature = _clean(dvs_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_054'] = {'inputs': ['dvs_replacement_054'], 'func': dvs_replacement_d2_054}


def dvs_replacement_d2_055(dvs_replacement_055):
    feature = _clean(dvs_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_055'] = {'inputs': ['dvs_replacement_055'], 'func': dvs_replacement_d2_055}


def dvs_replacement_d2_056(dvs_replacement_056):
    feature = _clean(dvs_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_056'] = {'inputs': ['dvs_replacement_056'], 'func': dvs_replacement_d2_056}


def dvs_replacement_d2_057(dvs_replacement_057):
    feature = _clean(dvs_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_057'] = {'inputs': ['dvs_replacement_057'], 'func': dvs_replacement_d2_057}


def dvs_replacement_d2_058(dvs_replacement_058):
    feature = _clean(dvs_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_058'] = {'inputs': ['dvs_replacement_058'], 'func': dvs_replacement_d2_058}


def dvs_replacement_d2_059(dvs_replacement_059):
    feature = _clean(dvs_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_059'] = {'inputs': ['dvs_replacement_059'], 'func': dvs_replacement_d2_059}


def dvs_replacement_d2_060(dvs_replacement_060):
    feature = _clean(dvs_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_060'] = {'inputs': ['dvs_replacement_060'], 'func': dvs_replacement_d2_060}


def dvs_replacement_d2_061(dvs_replacement_061):
    feature = _clean(dvs_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_061'] = {'inputs': ['dvs_replacement_061'], 'func': dvs_replacement_d2_061}


def dvs_replacement_d2_062(dvs_replacement_062):
    feature = _clean(dvs_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_062'] = {'inputs': ['dvs_replacement_062'], 'func': dvs_replacement_d2_062}


def dvs_replacement_d2_063(dvs_replacement_063):
    feature = _clean(dvs_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_063'] = {'inputs': ['dvs_replacement_063'], 'func': dvs_replacement_d2_063}


def dvs_replacement_d2_064(dvs_replacement_064):
    feature = _clean(dvs_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_064'] = {'inputs': ['dvs_replacement_064'], 'func': dvs_replacement_d2_064}


def dvs_replacement_d2_065(dvs_replacement_065):
    feature = _clean(dvs_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_065'] = {'inputs': ['dvs_replacement_065'], 'func': dvs_replacement_d2_065}


def dvs_replacement_d2_066(dvs_replacement_066):
    feature = _clean(dvs_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_066'] = {'inputs': ['dvs_replacement_066'], 'func': dvs_replacement_d2_066}


def dvs_replacement_d2_067(dvs_replacement_067):
    feature = _clean(dvs_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_067'] = {'inputs': ['dvs_replacement_067'], 'func': dvs_replacement_d2_067}


def dvs_replacement_d2_068(dvs_replacement_068):
    feature = _clean(dvs_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_068'] = {'inputs': ['dvs_replacement_068'], 'func': dvs_replacement_d2_068}


def dvs_replacement_d2_069(dvs_replacement_069):
    feature = _clean(dvs_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_069'] = {'inputs': ['dvs_replacement_069'], 'func': dvs_replacement_d2_069}


def dvs_replacement_d2_070(dvs_replacement_070):
    feature = _clean(dvs_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_070'] = {'inputs': ['dvs_replacement_070'], 'func': dvs_replacement_d2_070}


def dvs_replacement_d2_071(dvs_replacement_071):
    feature = _clean(dvs_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_071'] = {'inputs': ['dvs_replacement_071'], 'func': dvs_replacement_d2_071}


def dvs_replacement_d2_072(dvs_replacement_072):
    feature = _clean(dvs_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_072'] = {'inputs': ['dvs_replacement_072'], 'func': dvs_replacement_d2_072}


def dvs_replacement_d2_073(dvs_replacement_073):
    feature = _clean(dvs_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_073'] = {'inputs': ['dvs_replacement_073'], 'func': dvs_replacement_d2_073}


def dvs_replacement_d2_074(dvs_replacement_074):
    feature = _clean(dvs_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_074'] = {'inputs': ['dvs_replacement_074'], 'func': dvs_replacement_d2_074}


def dvs_replacement_d2_075(dvs_replacement_075):
    feature = _clean(dvs_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_075'] = {'inputs': ['dvs_replacement_075'], 'func': dvs_replacement_d2_075}


def dvs_replacement_d2_076(dvs_replacement_076):
    feature = _clean(dvs_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_076'] = {'inputs': ['dvs_replacement_076'], 'func': dvs_replacement_d2_076}


def dvs_replacement_d2_077(dvs_replacement_077):
    feature = _clean(dvs_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_077'] = {'inputs': ['dvs_replacement_077'], 'func': dvs_replacement_d2_077}


def dvs_replacement_d2_078(dvs_replacement_078):
    feature = _clean(dvs_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_078'] = {'inputs': ['dvs_replacement_078'], 'func': dvs_replacement_d2_078}


def dvs_replacement_d2_079(dvs_replacement_079):
    feature = _clean(dvs_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_079'] = {'inputs': ['dvs_replacement_079'], 'func': dvs_replacement_d2_079}


def dvs_replacement_d2_080(dvs_replacement_080):
    feature = _clean(dvs_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_080'] = {'inputs': ['dvs_replacement_080'], 'func': dvs_replacement_d2_080}


def dvs_replacement_d2_081(dvs_replacement_081):
    feature = _clean(dvs_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_081'] = {'inputs': ['dvs_replacement_081'], 'func': dvs_replacement_d2_081}


def dvs_replacement_d2_082(dvs_replacement_082):
    feature = _clean(dvs_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_082'] = {'inputs': ['dvs_replacement_082'], 'func': dvs_replacement_d2_082}


def dvs_replacement_d2_083(dvs_replacement_083):
    feature = _clean(dvs_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_083'] = {'inputs': ['dvs_replacement_083'], 'func': dvs_replacement_d2_083}


def dvs_replacement_d2_084(dvs_replacement_084):
    feature = _clean(dvs_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_084'] = {'inputs': ['dvs_replacement_084'], 'func': dvs_replacement_d2_084}


def dvs_replacement_d2_085(dvs_replacement_085):
    feature = _clean(dvs_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_085'] = {'inputs': ['dvs_replacement_085'], 'func': dvs_replacement_d2_085}


def dvs_replacement_d2_086(dvs_replacement_086):
    feature = _clean(dvs_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_086'] = {'inputs': ['dvs_replacement_086'], 'func': dvs_replacement_d2_086}


def dvs_replacement_d2_087(dvs_replacement_087):
    feature = _clean(dvs_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_087'] = {'inputs': ['dvs_replacement_087'], 'func': dvs_replacement_d2_087}


def dvs_replacement_d2_088(dvs_replacement_088):
    feature = _clean(dvs_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_088'] = {'inputs': ['dvs_replacement_088'], 'func': dvs_replacement_d2_088}


def dvs_replacement_d2_089(dvs_replacement_089):
    feature = _clean(dvs_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_089'] = {'inputs': ['dvs_replacement_089'], 'func': dvs_replacement_d2_089}


def dvs_replacement_d2_090(dvs_replacement_090):
    feature = _clean(dvs_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_090'] = {'inputs': ['dvs_replacement_090'], 'func': dvs_replacement_d2_090}


def dvs_replacement_d2_091(dvs_replacement_091):
    feature = _clean(dvs_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_091'] = {'inputs': ['dvs_replacement_091'], 'func': dvs_replacement_d2_091}


def dvs_replacement_d2_092(dvs_replacement_092):
    feature = _clean(dvs_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_092'] = {'inputs': ['dvs_replacement_092'], 'func': dvs_replacement_d2_092}


def dvs_replacement_d2_093(dvs_replacement_093):
    feature = _clean(dvs_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_093'] = {'inputs': ['dvs_replacement_093'], 'func': dvs_replacement_d2_093}


def dvs_replacement_d2_094(dvs_replacement_094):
    feature = _clean(dvs_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_094'] = {'inputs': ['dvs_replacement_094'], 'func': dvs_replacement_d2_094}


def dvs_replacement_d2_095(dvs_replacement_095):
    feature = _clean(dvs_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_095'] = {'inputs': ['dvs_replacement_095'], 'func': dvs_replacement_d2_095}


def dvs_replacement_d2_096(dvs_replacement_096):
    feature = _clean(dvs_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_096'] = {'inputs': ['dvs_replacement_096'], 'func': dvs_replacement_d2_096}


def dvs_replacement_d2_097(dvs_replacement_097):
    feature = _clean(dvs_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_097'] = {'inputs': ['dvs_replacement_097'], 'func': dvs_replacement_d2_097}


def dvs_replacement_d2_098(dvs_replacement_098):
    feature = _clean(dvs_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_098'] = {'inputs': ['dvs_replacement_098'], 'func': dvs_replacement_d2_098}


def dvs_replacement_d2_099(dvs_replacement_099):
    feature = _clean(dvs_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_099'] = {'inputs': ['dvs_replacement_099'], 'func': dvs_replacement_d2_099}


def dvs_replacement_d2_100(dvs_replacement_100):
    feature = _clean(dvs_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_100'] = {'inputs': ['dvs_replacement_100'], 'func': dvs_replacement_d2_100}


def dvs_replacement_d2_101(dvs_replacement_101):
    feature = _clean(dvs_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_101'] = {'inputs': ['dvs_replacement_101'], 'func': dvs_replacement_d2_101}


def dvs_replacement_d2_102(dvs_replacement_102):
    feature = _clean(dvs_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_102'] = {'inputs': ['dvs_replacement_102'], 'func': dvs_replacement_d2_102}


def dvs_replacement_d2_103(dvs_replacement_103):
    feature = _clean(dvs_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_103'] = {'inputs': ['dvs_replacement_103'], 'func': dvs_replacement_d2_103}


def dvs_replacement_d2_104(dvs_replacement_104):
    feature = _clean(dvs_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_104'] = {'inputs': ['dvs_replacement_104'], 'func': dvs_replacement_d2_104}


def dvs_replacement_d2_105(dvs_replacement_105):
    feature = _clean(dvs_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_105'] = {'inputs': ['dvs_replacement_105'], 'func': dvs_replacement_d2_105}


def dvs_replacement_d2_106(dvs_replacement_106):
    feature = _clean(dvs_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_106'] = {'inputs': ['dvs_replacement_106'], 'func': dvs_replacement_d2_106}


def dvs_replacement_d2_107(dvs_replacement_107):
    feature = _clean(dvs_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_107'] = {'inputs': ['dvs_replacement_107'], 'func': dvs_replacement_d2_107}


def dvs_replacement_d2_108(dvs_replacement_108):
    feature = _clean(dvs_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_108'] = {'inputs': ['dvs_replacement_108'], 'func': dvs_replacement_d2_108}


def dvs_replacement_d2_109(dvs_replacement_109):
    feature = _clean(dvs_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_109'] = {'inputs': ['dvs_replacement_109'], 'func': dvs_replacement_d2_109}


def dvs_replacement_d2_110(dvs_replacement_110):
    feature = _clean(dvs_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_110'] = {'inputs': ['dvs_replacement_110'], 'func': dvs_replacement_d2_110}


def dvs_replacement_d2_111(dvs_replacement_111):
    feature = _clean(dvs_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_111'] = {'inputs': ['dvs_replacement_111'], 'func': dvs_replacement_d2_111}


def dvs_replacement_d2_112(dvs_replacement_112):
    feature = _clean(dvs_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_112'] = {'inputs': ['dvs_replacement_112'], 'func': dvs_replacement_d2_112}


def dvs_replacement_d2_113(dvs_replacement_113):
    feature = _clean(dvs_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_113'] = {'inputs': ['dvs_replacement_113'], 'func': dvs_replacement_d2_113}


def dvs_replacement_d2_114(dvs_replacement_114):
    feature = _clean(dvs_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_114'] = {'inputs': ['dvs_replacement_114'], 'func': dvs_replacement_d2_114}


def dvs_replacement_d2_115(dvs_replacement_115):
    feature = _clean(dvs_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_115'] = {'inputs': ['dvs_replacement_115'], 'func': dvs_replacement_d2_115}


def dvs_replacement_d2_116(dvs_replacement_116):
    feature = _clean(dvs_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_116'] = {'inputs': ['dvs_replacement_116'], 'func': dvs_replacement_d2_116}


def dvs_replacement_d2_117(dvs_replacement_117):
    feature = _clean(dvs_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_117'] = {'inputs': ['dvs_replacement_117'], 'func': dvs_replacement_d2_117}


def dvs_replacement_d2_118(dvs_replacement_118):
    feature = _clean(dvs_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_118'] = {'inputs': ['dvs_replacement_118'], 'func': dvs_replacement_d2_118}


def dvs_replacement_d2_119(dvs_replacement_119):
    feature = _clean(dvs_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_119'] = {'inputs': ['dvs_replacement_119'], 'func': dvs_replacement_d2_119}


def dvs_replacement_d2_120(dvs_replacement_120):
    feature = _clean(dvs_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_120'] = {'inputs': ['dvs_replacement_120'], 'func': dvs_replacement_d2_120}


def dvs_replacement_d2_121(dvs_replacement_121):
    feature = _clean(dvs_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_121'] = {'inputs': ['dvs_replacement_121'], 'func': dvs_replacement_d2_121}


def dvs_replacement_d2_122(dvs_replacement_122):
    feature = _clean(dvs_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_122'] = {'inputs': ['dvs_replacement_122'], 'func': dvs_replacement_d2_122}


def dvs_replacement_d2_123(dvs_replacement_123):
    feature = _clean(dvs_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_123'] = {'inputs': ['dvs_replacement_123'], 'func': dvs_replacement_d2_123}


def dvs_replacement_d2_124(dvs_replacement_124):
    feature = _clean(dvs_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_124'] = {'inputs': ['dvs_replacement_124'], 'func': dvs_replacement_d2_124}


def dvs_replacement_d2_125(dvs_replacement_125):
    feature = _clean(dvs_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_125'] = {'inputs': ['dvs_replacement_125'], 'func': dvs_replacement_d2_125}


def dvs_replacement_d2_126(dvs_replacement_126):
    feature = _clean(dvs_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_126'] = {'inputs': ['dvs_replacement_126'], 'func': dvs_replacement_d2_126}


def dvs_replacement_d2_127(dvs_replacement_127):
    feature = _clean(dvs_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_127'] = {'inputs': ['dvs_replacement_127'], 'func': dvs_replacement_d2_127}


def dvs_replacement_d2_128(dvs_replacement_128):
    feature = _clean(dvs_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_128'] = {'inputs': ['dvs_replacement_128'], 'func': dvs_replacement_d2_128}


def dvs_replacement_d2_129(dvs_replacement_129):
    feature = _clean(dvs_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_129'] = {'inputs': ['dvs_replacement_129'], 'func': dvs_replacement_d2_129}


def dvs_replacement_d2_130(dvs_replacement_130):
    feature = _clean(dvs_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_130'] = {'inputs': ['dvs_replacement_130'], 'func': dvs_replacement_d2_130}


def dvs_replacement_d2_131(dvs_replacement_131):
    feature = _clean(dvs_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_131'] = {'inputs': ['dvs_replacement_131'], 'func': dvs_replacement_d2_131}


def dvs_replacement_d2_132(dvs_replacement_132):
    feature = _clean(dvs_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_132'] = {'inputs': ['dvs_replacement_132'], 'func': dvs_replacement_d2_132}


def dvs_replacement_d2_133(dvs_replacement_133):
    feature = _clean(dvs_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_133'] = {'inputs': ['dvs_replacement_133'], 'func': dvs_replacement_d2_133}


def dvs_replacement_d2_134(dvs_replacement_134):
    feature = _clean(dvs_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_134'] = {'inputs': ['dvs_replacement_134'], 'func': dvs_replacement_d2_134}


def dvs_replacement_d2_135(dvs_replacement_135):
    feature = _clean(dvs_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_135'] = {'inputs': ['dvs_replacement_135'], 'func': dvs_replacement_d2_135}


def dvs_replacement_d2_136(dvs_replacement_136):
    feature = _clean(dvs_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_136'] = {'inputs': ['dvs_replacement_136'], 'func': dvs_replacement_d2_136}


def dvs_replacement_d2_137(dvs_replacement_137):
    feature = _clean(dvs_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_137'] = {'inputs': ['dvs_replacement_137'], 'func': dvs_replacement_d2_137}


def dvs_replacement_d2_138(dvs_replacement_138):
    feature = _clean(dvs_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_138'] = {'inputs': ['dvs_replacement_138'], 'func': dvs_replacement_d2_138}


def dvs_replacement_d2_139(dvs_replacement_139):
    feature = _clean(dvs_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_139'] = {'inputs': ['dvs_replacement_139'], 'func': dvs_replacement_d2_139}


def dvs_replacement_d2_140(dvs_replacement_140):
    feature = _clean(dvs_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_140'] = {'inputs': ['dvs_replacement_140'], 'func': dvs_replacement_d2_140}


def dvs_replacement_d2_141(dvs_replacement_141):
    feature = _clean(dvs_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_141'] = {'inputs': ['dvs_replacement_141'], 'func': dvs_replacement_d2_141}


def dvs_replacement_d2_142(dvs_replacement_142):
    feature = _clean(dvs_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_142'] = {'inputs': ['dvs_replacement_142'], 'func': dvs_replacement_d2_142}


def dvs_replacement_d2_143(dvs_replacement_143):
    feature = _clean(dvs_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_143'] = {'inputs': ['dvs_replacement_143'], 'func': dvs_replacement_d2_143}


def dvs_replacement_d2_144(dvs_replacement_144):
    feature = _clean(dvs_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_144'] = {'inputs': ['dvs_replacement_144'], 'func': dvs_replacement_d2_144}


def dvs_replacement_d2_145(dvs_replacement_145):
    feature = _clean(dvs_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_145'] = {'inputs': ['dvs_replacement_145'], 'func': dvs_replacement_d2_145}


def dvs_replacement_d2_146(dvs_replacement_146):
    feature = _clean(dvs_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_146'] = {'inputs': ['dvs_replacement_146'], 'func': dvs_replacement_d2_146}


def dvs_replacement_d2_147(dvs_replacement_147):
    feature = _clean(dvs_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_147'] = {'inputs': ['dvs_replacement_147'], 'func': dvs_replacement_d2_147}


def dvs_replacement_d2_148(dvs_replacement_148):
    feature = _clean(dvs_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_148'] = {'inputs': ['dvs_replacement_148'], 'func': dvs_replacement_d2_148}


def dvs_replacement_d2_149(dvs_replacement_149):
    feature = _clean(dvs_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_149'] = {'inputs': ['dvs_replacement_149'], 'func': dvs_replacement_d2_149}


def dvs_replacement_d2_150(dvs_replacement_150):
    feature = _clean(dvs_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_150'] = {'inputs': ['dvs_replacement_150'], 'func': dvs_replacement_d2_150}


def dvs_replacement_d2_151(dvs_replacement_151):
    feature = _clean(dvs_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_151'] = {'inputs': ['dvs_replacement_151'], 'func': dvs_replacement_d2_151}


def dvs_replacement_d2_152(dvs_replacement_152):
    feature = _clean(dvs_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_152'] = {'inputs': ['dvs_replacement_152'], 'func': dvs_replacement_d2_152}


def dvs_replacement_d2_153(dvs_replacement_153):
    feature = _clean(dvs_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_153'] = {'inputs': ['dvs_replacement_153'], 'func': dvs_replacement_d2_153}


def dvs_replacement_d2_154(dvs_replacement_154):
    feature = _clean(dvs_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_154'] = {'inputs': ['dvs_replacement_154'], 'func': dvs_replacement_d2_154}


def dvs_replacement_d2_155(dvs_replacement_155):
    feature = _clean(dvs_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_155'] = {'inputs': ['dvs_replacement_155'], 'func': dvs_replacement_d2_155}


def dvs_replacement_d2_156(dvs_replacement_156):
    feature = _clean(dvs_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_156'] = {'inputs': ['dvs_replacement_156'], 'func': dvs_replacement_d2_156}


def dvs_replacement_d2_157(dvs_replacement_157):
    feature = _clean(dvs_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_157'] = {'inputs': ['dvs_replacement_157'], 'func': dvs_replacement_d2_157}


def dvs_replacement_d2_158(dvs_replacement_158):
    feature = _clean(dvs_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_158'] = {'inputs': ['dvs_replacement_158'], 'func': dvs_replacement_d2_158}


def dvs_replacement_d2_159(dvs_replacement_159):
    feature = _clean(dvs_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_159'] = {'inputs': ['dvs_replacement_159'], 'func': dvs_replacement_d2_159}


def dvs_replacement_d2_160(dvs_replacement_160):
    feature = _clean(dvs_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
DVS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['dvs_replacement_d2_160'] = {'inputs': ['dvs_replacement_160'], 'func': dvs_replacement_d2_160}


# Base-universe derivative extensions for repaired first-base features.
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def dvs_base_universe_d2_001_dvs_002_volume_zscore_10_002(dvs_002_volume_zscore_10_002):
    return _base_universe_d2(dvs_002_volume_zscore_10_002, 1)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_001_dvs_002_volume_zscore_10_002'] = {'inputs': ['dvs_002_volume_zscore_10_002'], 'func': dvs_base_universe_d2_001_dvs_002_volume_zscore_10_002}


def dvs_base_universe_d2_002_dvs_003_down_volume_share_21_003(dvs_003_down_volume_share_21_003):
    return _base_universe_d2(dvs_003_down_volume_share_21_003, 2)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_002_dvs_003_down_volume_share_21_003'] = {'inputs': ['dvs_003_down_volume_share_21_003'], 'func': dvs_base_universe_d2_002_dvs_003_down_volume_share_21_003}


def dvs_base_universe_d2_003_dvs_004_dollar_volume_shock_42_004(dvs_004_dollar_volume_shock_42_004):
    return _base_universe_d2(dvs_004_dollar_volume_shock_42_004, 3)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_003_dvs_004_dollar_volume_shock_42_004'] = {'inputs': ['dvs_004_dollar_volume_shock_42_004'], 'func': dvs_base_universe_d2_003_dvs_004_dollar_volume_shock_42_004}


def dvs_base_universe_d2_004_dvs_005_volume_trend_slope_63_005(dvs_005_volume_trend_slope_63_005):
    return _base_universe_d2(dvs_005_volume_trend_slope_63_005, 4)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_004_dvs_005_volume_trend_slope_63_005'] = {'inputs': ['dvs_005_volume_trend_slope_63_005'], 'func': dvs_base_universe_d2_004_dvs_005_volume_trend_slope_63_005}


def dvs_base_universe_d2_005_dvs_006_price_volume_divergence_84_006(dvs_006_price_volume_divergence_84_006):
    return _base_universe_d2(dvs_006_price_volume_divergence_84_006, 5)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_005_dvs_006_price_volume_divergence_84_006'] = {'inputs': ['dvs_006_price_volume_divergence_84_006'], 'func': dvs_base_universe_d2_005_dvs_006_price_volume_divergence_84_006}


def dvs_base_universe_d2_006_dvs_008_volume_zscore_189_008(dvs_008_volume_zscore_189_008):
    return _base_universe_d2(dvs_008_volume_zscore_189_008, 6)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_006_dvs_008_volume_zscore_189_008'] = {'inputs': ['dvs_008_volume_zscore_189_008'], 'func': dvs_base_universe_d2_006_dvs_008_volume_zscore_189_008}


def dvs_base_universe_d2_007_dvs_009_down_volume_share_252_009(dvs_009_down_volume_share_252_009):
    return _base_universe_d2(dvs_009_down_volume_share_252_009, 7)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_007_dvs_009_down_volume_share_252_009'] = {'inputs': ['dvs_009_down_volume_share_252_009'], 'func': dvs_base_universe_d2_007_dvs_009_down_volume_share_252_009}


def dvs_base_universe_d2_008_dvs_010_dollar_volume_shock_378_010(dvs_010_dollar_volume_shock_378_010):
    return _base_universe_d2(dvs_010_dollar_volume_shock_378_010, 8)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_008_dvs_010_dollar_volume_shock_378_010'] = {'inputs': ['dvs_010_dollar_volume_shock_378_010'], 'func': dvs_base_universe_d2_008_dvs_010_dollar_volume_shock_378_010}


def dvs_base_universe_d2_009_dvs_011_volume_trend_slope_504_011(dvs_011_volume_trend_slope_504_011):
    return _base_universe_d2(dvs_011_volume_trend_slope_504_011, 9)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_009_dvs_011_volume_trend_slope_504_011'] = {'inputs': ['dvs_011_volume_trend_slope_504_011'], 'func': dvs_base_universe_d2_009_dvs_011_volume_trend_slope_504_011}


def dvs_base_universe_d2_010_dvs_012_price_volume_divergence_756_012(dvs_012_price_volume_divergence_756_012):
    return _base_universe_d2(dvs_012_price_volume_divergence_756_012, 10)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_010_dvs_012_price_volume_divergence_756_012'] = {'inputs': ['dvs_012_price_volume_divergence_756_012'], 'func': dvs_base_universe_d2_010_dvs_012_price_volume_divergence_756_012}


def dvs_base_universe_d2_011_dvs_014_volume_zscore_1260_014(dvs_014_volume_zscore_1260_014):
    return _base_universe_d2(dvs_014_volume_zscore_1260_014, 11)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_011_dvs_014_volume_zscore_1260_014'] = {'inputs': ['dvs_014_volume_zscore_1260_014'], 'func': dvs_base_universe_d2_011_dvs_014_volume_zscore_1260_014}


def dvs_base_universe_d2_012_dvs_015_down_volume_share_1512_015(dvs_015_down_volume_share_1512_015):
    return _base_universe_d2(dvs_015_down_volume_share_1512_015, 12)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_012_dvs_015_down_volume_share_1512_015'] = {'inputs': ['dvs_015_down_volume_share_1512_015'], 'func': dvs_base_universe_d2_012_dvs_015_down_volume_share_1512_015}


def dvs_base_universe_d2_013_dvs_016_dollar_volume_shock_5_016(dvs_016_dollar_volume_shock_5_016):
    return _base_universe_d2(dvs_016_dollar_volume_shock_5_016, 13)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_013_dvs_016_dollar_volume_shock_5_016'] = {'inputs': ['dvs_016_dollar_volume_shock_5_016'], 'func': dvs_base_universe_d2_013_dvs_016_dollar_volume_shock_5_016}


def dvs_base_universe_d2_014_dvs_017_volume_trend_slope_10_017(dvs_017_volume_trend_slope_10_017):
    return _base_universe_d2(dvs_017_volume_trend_slope_10_017, 14)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_014_dvs_017_volume_trend_slope_10_017'] = {'inputs': ['dvs_017_volume_trend_slope_10_017'], 'func': dvs_base_universe_d2_014_dvs_017_volume_trend_slope_10_017}


def dvs_base_universe_d2_015_dvs_018_price_volume_divergence_21_018(dvs_018_price_volume_divergence_21_018):
    return _base_universe_d2(dvs_018_price_volume_divergence_21_018, 15)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_015_dvs_018_price_volume_divergence_21_018'] = {'inputs': ['dvs_018_price_volume_divergence_21_018'], 'func': dvs_base_universe_d2_015_dvs_018_price_volume_divergence_21_018}


def dvs_base_universe_d2_016_dvs_020_volume_zscore_63_020(dvs_020_volume_zscore_63_020):
    return _base_universe_d2(dvs_020_volume_zscore_63_020, 16)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_016_dvs_020_volume_zscore_63_020'] = {'inputs': ['dvs_020_volume_zscore_63_020'], 'func': dvs_base_universe_d2_016_dvs_020_volume_zscore_63_020}


def dvs_base_universe_d2_017_dvs_021_down_volume_share_84_021(dvs_021_down_volume_share_84_021):
    return _base_universe_d2(dvs_021_down_volume_share_84_021, 17)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_017_dvs_021_down_volume_share_84_021'] = {'inputs': ['dvs_021_down_volume_share_84_021'], 'func': dvs_base_universe_d2_017_dvs_021_down_volume_share_84_021}


def dvs_base_universe_d2_018_dvs_022_dollar_volume_shock_126_022(dvs_022_dollar_volume_shock_126_022):
    return _base_universe_d2(dvs_022_dollar_volume_shock_126_022, 18)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_018_dvs_022_dollar_volume_shock_126_022'] = {'inputs': ['dvs_022_dollar_volume_shock_126_022'], 'func': dvs_base_universe_d2_018_dvs_022_dollar_volume_shock_126_022}


def dvs_base_universe_d2_019_dvs_023_volume_trend_slope_189_023(dvs_023_volume_trend_slope_189_023):
    return _base_universe_d2(dvs_023_volume_trend_slope_189_023, 19)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_019_dvs_023_volume_trend_slope_189_023'] = {'inputs': ['dvs_023_volume_trend_slope_189_023'], 'func': dvs_base_universe_d2_019_dvs_023_volume_trend_slope_189_023}


def dvs_base_universe_d2_020_dvs_024_price_volume_divergence_252_024(dvs_024_price_volume_divergence_252_024):
    return _base_universe_d2(dvs_024_price_volume_divergence_252_024, 20)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_020_dvs_024_price_volume_divergence_252_024'] = {'inputs': ['dvs_024_price_volume_divergence_252_024'], 'func': dvs_base_universe_d2_020_dvs_024_price_volume_divergence_252_024}


def dvs_base_universe_d2_021_dvs_026_volume_zscore_504_026(dvs_026_volume_zscore_504_026):
    return _base_universe_d2(dvs_026_volume_zscore_504_026, 21)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_021_dvs_026_volume_zscore_504_026'] = {'inputs': ['dvs_026_volume_zscore_504_026'], 'func': dvs_base_universe_d2_021_dvs_026_volume_zscore_504_026}


def dvs_base_universe_d2_022_dvs_027_down_volume_share_756_027(dvs_027_down_volume_share_756_027):
    return _base_universe_d2(dvs_027_down_volume_share_756_027, 22)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_022_dvs_027_down_volume_share_756_027'] = {'inputs': ['dvs_027_down_volume_share_756_027'], 'func': dvs_base_universe_d2_022_dvs_027_down_volume_share_756_027}


def dvs_base_universe_d2_023_dvs_028_dollar_volume_shock_1008_028(dvs_028_dollar_volume_shock_1008_028):
    return _base_universe_d2(dvs_028_dollar_volume_shock_1008_028, 23)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_023_dvs_028_dollar_volume_shock_1008_028'] = {'inputs': ['dvs_028_dollar_volume_shock_1008_028'], 'func': dvs_base_universe_d2_023_dvs_028_dollar_volume_shock_1008_028}


def dvs_base_universe_d2_024_dvs_029_volume_trend_slope_1260_029(dvs_029_volume_trend_slope_1260_029):
    return _base_universe_d2(dvs_029_volume_trend_slope_1260_029, 24)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_024_dvs_029_volume_trend_slope_1260_029'] = {'inputs': ['dvs_029_volume_trend_slope_1260_029'], 'func': dvs_base_universe_d2_024_dvs_029_volume_trend_slope_1260_029}


def dvs_base_universe_d2_025_dvs_030_price_volume_divergence_1512_030(dvs_030_price_volume_divergence_1512_030):
    return _base_universe_d2(dvs_030_price_volume_divergence_1512_030, 25)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_025_dvs_030_price_volume_divergence_1512_030'] = {'inputs': ['dvs_030_price_volume_divergence_1512_030'], 'func': dvs_base_universe_d2_025_dvs_030_price_volume_divergence_1512_030}


def dvs_base_universe_d2_026_dvs_basefill_031(dvs_basefill_031):
    return _base_universe_d2(dvs_basefill_031, 26)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_026_dvs_basefill_031'] = {'inputs': ['dvs_basefill_031'], 'func': dvs_base_universe_d2_026_dvs_basefill_031}


def dvs_base_universe_d2_027_dvs_basefill_032(dvs_basefill_032):
    return _base_universe_d2(dvs_basefill_032, 27)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_027_dvs_basefill_032'] = {'inputs': ['dvs_basefill_032'], 'func': dvs_base_universe_d2_027_dvs_basefill_032}


def dvs_base_universe_d2_028_dvs_basefill_033(dvs_basefill_033):
    return _base_universe_d2(dvs_basefill_033, 28)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_028_dvs_basefill_033'] = {'inputs': ['dvs_basefill_033'], 'func': dvs_base_universe_d2_028_dvs_basefill_033}


def dvs_base_universe_d2_029_dvs_basefill_034(dvs_basefill_034):
    return _base_universe_d2(dvs_basefill_034, 29)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_029_dvs_basefill_034'] = {'inputs': ['dvs_basefill_034'], 'func': dvs_base_universe_d2_029_dvs_basefill_034}


def dvs_base_universe_d2_030_dvs_basefill_035(dvs_basefill_035):
    return _base_universe_d2(dvs_basefill_035, 30)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_030_dvs_basefill_035'] = {'inputs': ['dvs_basefill_035'], 'func': dvs_base_universe_d2_030_dvs_basefill_035}


def dvs_base_universe_d2_031_dvs_basefill_036(dvs_basefill_036):
    return _base_universe_d2(dvs_basefill_036, 31)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_031_dvs_basefill_036'] = {'inputs': ['dvs_basefill_036'], 'func': dvs_base_universe_d2_031_dvs_basefill_036}


def dvs_base_universe_d2_032_dvs_basefill_037(dvs_basefill_037):
    return _base_universe_d2(dvs_basefill_037, 32)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_032_dvs_basefill_037'] = {'inputs': ['dvs_basefill_037'], 'func': dvs_base_universe_d2_032_dvs_basefill_037}


def dvs_base_universe_d2_033_dvs_basefill_038(dvs_basefill_038):
    return _base_universe_d2(dvs_basefill_038, 33)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_033_dvs_basefill_038'] = {'inputs': ['dvs_basefill_038'], 'func': dvs_base_universe_d2_033_dvs_basefill_038}


def dvs_base_universe_d2_034_dvs_basefill_039(dvs_basefill_039):
    return _base_universe_d2(dvs_basefill_039, 34)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_034_dvs_basefill_039'] = {'inputs': ['dvs_basefill_039'], 'func': dvs_base_universe_d2_034_dvs_basefill_039}


def dvs_base_universe_d2_035_dvs_basefill_040(dvs_basefill_040):
    return _base_universe_d2(dvs_basefill_040, 35)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_035_dvs_basefill_040'] = {'inputs': ['dvs_basefill_040'], 'func': dvs_base_universe_d2_035_dvs_basefill_040}


def dvs_base_universe_d2_036_dvs_basefill_041(dvs_basefill_041):
    return _base_universe_d2(dvs_basefill_041, 36)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_036_dvs_basefill_041'] = {'inputs': ['dvs_basefill_041'], 'func': dvs_base_universe_d2_036_dvs_basefill_041}


def dvs_base_universe_d2_037_dvs_basefill_042(dvs_basefill_042):
    return _base_universe_d2(dvs_basefill_042, 37)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_037_dvs_basefill_042'] = {'inputs': ['dvs_basefill_042'], 'func': dvs_base_universe_d2_037_dvs_basefill_042}


def dvs_base_universe_d2_038_dvs_basefill_043(dvs_basefill_043):
    return _base_universe_d2(dvs_basefill_043, 38)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_038_dvs_basefill_043'] = {'inputs': ['dvs_basefill_043'], 'func': dvs_base_universe_d2_038_dvs_basefill_043}


def dvs_base_universe_d2_039_dvs_basefill_044(dvs_basefill_044):
    return _base_universe_d2(dvs_basefill_044, 39)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_039_dvs_basefill_044'] = {'inputs': ['dvs_basefill_044'], 'func': dvs_base_universe_d2_039_dvs_basefill_044}


def dvs_base_universe_d2_040_dvs_basefill_045(dvs_basefill_045):
    return _base_universe_d2(dvs_basefill_045, 40)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_040_dvs_basefill_045'] = {'inputs': ['dvs_basefill_045'], 'func': dvs_base_universe_d2_040_dvs_basefill_045}


def dvs_base_universe_d2_041_dvs_basefill_046(dvs_basefill_046):
    return _base_universe_d2(dvs_basefill_046, 41)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_041_dvs_basefill_046'] = {'inputs': ['dvs_basefill_046'], 'func': dvs_base_universe_d2_041_dvs_basefill_046}


def dvs_base_universe_d2_042_dvs_basefill_047(dvs_basefill_047):
    return _base_universe_d2(dvs_basefill_047, 42)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_042_dvs_basefill_047'] = {'inputs': ['dvs_basefill_047'], 'func': dvs_base_universe_d2_042_dvs_basefill_047}


def dvs_base_universe_d2_043_dvs_basefill_048(dvs_basefill_048):
    return _base_universe_d2(dvs_basefill_048, 43)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_043_dvs_basefill_048'] = {'inputs': ['dvs_basefill_048'], 'func': dvs_base_universe_d2_043_dvs_basefill_048}


def dvs_base_universe_d2_044_dvs_basefill_049(dvs_basefill_049):
    return _base_universe_d2(dvs_basefill_049, 44)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_044_dvs_basefill_049'] = {'inputs': ['dvs_basefill_049'], 'func': dvs_base_universe_d2_044_dvs_basefill_049}


def dvs_base_universe_d2_045_dvs_basefill_050(dvs_basefill_050):
    return _base_universe_d2(dvs_basefill_050, 45)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_045_dvs_basefill_050'] = {'inputs': ['dvs_basefill_050'], 'func': dvs_base_universe_d2_045_dvs_basefill_050}


def dvs_base_universe_d2_046_dvs_basefill_051(dvs_basefill_051):
    return _base_universe_d2(dvs_basefill_051, 46)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_046_dvs_basefill_051'] = {'inputs': ['dvs_basefill_051'], 'func': dvs_base_universe_d2_046_dvs_basefill_051}


def dvs_base_universe_d2_047_dvs_basefill_052(dvs_basefill_052):
    return _base_universe_d2(dvs_basefill_052, 47)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_047_dvs_basefill_052'] = {'inputs': ['dvs_basefill_052'], 'func': dvs_base_universe_d2_047_dvs_basefill_052}


def dvs_base_universe_d2_048_dvs_basefill_053(dvs_basefill_053):
    return _base_universe_d2(dvs_basefill_053, 48)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_048_dvs_basefill_053'] = {'inputs': ['dvs_basefill_053'], 'func': dvs_base_universe_d2_048_dvs_basefill_053}


def dvs_base_universe_d2_049_dvs_basefill_054(dvs_basefill_054):
    return _base_universe_d2(dvs_basefill_054, 49)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_049_dvs_basefill_054'] = {'inputs': ['dvs_basefill_054'], 'func': dvs_base_universe_d2_049_dvs_basefill_054}


def dvs_base_universe_d2_050_dvs_basefill_055(dvs_basefill_055):
    return _base_universe_d2(dvs_basefill_055, 50)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_050_dvs_basefill_055'] = {'inputs': ['dvs_basefill_055'], 'func': dvs_base_universe_d2_050_dvs_basefill_055}


def dvs_base_universe_d2_051_dvs_basefill_056(dvs_basefill_056):
    return _base_universe_d2(dvs_basefill_056, 51)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_051_dvs_basefill_056'] = {'inputs': ['dvs_basefill_056'], 'func': dvs_base_universe_d2_051_dvs_basefill_056}


def dvs_base_universe_d2_052_dvs_basefill_057(dvs_basefill_057):
    return _base_universe_d2(dvs_basefill_057, 52)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_052_dvs_basefill_057'] = {'inputs': ['dvs_basefill_057'], 'func': dvs_base_universe_d2_052_dvs_basefill_057}


def dvs_base_universe_d2_053_dvs_basefill_058(dvs_basefill_058):
    return _base_universe_d2(dvs_basefill_058, 53)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_053_dvs_basefill_058'] = {'inputs': ['dvs_basefill_058'], 'func': dvs_base_universe_d2_053_dvs_basefill_058}


def dvs_base_universe_d2_054_dvs_basefill_059(dvs_basefill_059):
    return _base_universe_d2(dvs_basefill_059, 54)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_054_dvs_basefill_059'] = {'inputs': ['dvs_basefill_059'], 'func': dvs_base_universe_d2_054_dvs_basefill_059}


def dvs_base_universe_d2_055_dvs_basefill_060(dvs_basefill_060):
    return _base_universe_d2(dvs_basefill_060, 55)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_055_dvs_basefill_060'] = {'inputs': ['dvs_basefill_060'], 'func': dvs_base_universe_d2_055_dvs_basefill_060}


def dvs_base_universe_d2_056_dvs_basefill_061(dvs_basefill_061):
    return _base_universe_d2(dvs_basefill_061, 56)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_056_dvs_basefill_061'] = {'inputs': ['dvs_basefill_061'], 'func': dvs_base_universe_d2_056_dvs_basefill_061}


def dvs_base_universe_d2_057_dvs_basefill_062(dvs_basefill_062):
    return _base_universe_d2(dvs_basefill_062, 57)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_057_dvs_basefill_062'] = {'inputs': ['dvs_basefill_062'], 'func': dvs_base_universe_d2_057_dvs_basefill_062}


def dvs_base_universe_d2_058_dvs_basefill_063(dvs_basefill_063):
    return _base_universe_d2(dvs_basefill_063, 58)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_058_dvs_basefill_063'] = {'inputs': ['dvs_basefill_063'], 'func': dvs_base_universe_d2_058_dvs_basefill_063}


def dvs_base_universe_d2_059_dvs_basefill_064(dvs_basefill_064):
    return _base_universe_d2(dvs_basefill_064, 59)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_059_dvs_basefill_064'] = {'inputs': ['dvs_basefill_064'], 'func': dvs_base_universe_d2_059_dvs_basefill_064}


def dvs_base_universe_d2_060_dvs_basefill_065(dvs_basefill_065):
    return _base_universe_d2(dvs_basefill_065, 60)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_060_dvs_basefill_065'] = {'inputs': ['dvs_basefill_065'], 'func': dvs_base_universe_d2_060_dvs_basefill_065}


def dvs_base_universe_d2_061_dvs_basefill_066(dvs_basefill_066):
    return _base_universe_d2(dvs_basefill_066, 61)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_061_dvs_basefill_066'] = {'inputs': ['dvs_basefill_066'], 'func': dvs_base_universe_d2_061_dvs_basefill_066}


def dvs_base_universe_d2_062_dvs_basefill_067(dvs_basefill_067):
    return _base_universe_d2(dvs_basefill_067, 62)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_062_dvs_basefill_067'] = {'inputs': ['dvs_basefill_067'], 'func': dvs_base_universe_d2_062_dvs_basefill_067}


def dvs_base_universe_d2_063_dvs_basefill_068(dvs_basefill_068):
    return _base_universe_d2(dvs_basefill_068, 63)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_063_dvs_basefill_068'] = {'inputs': ['dvs_basefill_068'], 'func': dvs_base_universe_d2_063_dvs_basefill_068}


def dvs_base_universe_d2_064_dvs_basefill_069(dvs_basefill_069):
    return _base_universe_d2(dvs_basefill_069, 64)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_064_dvs_basefill_069'] = {'inputs': ['dvs_basefill_069'], 'func': dvs_base_universe_d2_064_dvs_basefill_069}


def dvs_base_universe_d2_065_dvs_basefill_070(dvs_basefill_070):
    return _base_universe_d2(dvs_basefill_070, 65)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_065_dvs_basefill_070'] = {'inputs': ['dvs_basefill_070'], 'func': dvs_base_universe_d2_065_dvs_basefill_070}


def dvs_base_universe_d2_066_dvs_basefill_071(dvs_basefill_071):
    return _base_universe_d2(dvs_basefill_071, 66)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_066_dvs_basefill_071'] = {'inputs': ['dvs_basefill_071'], 'func': dvs_base_universe_d2_066_dvs_basefill_071}


def dvs_base_universe_d2_067_dvs_basefill_072(dvs_basefill_072):
    return _base_universe_d2(dvs_basefill_072, 67)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_067_dvs_basefill_072'] = {'inputs': ['dvs_basefill_072'], 'func': dvs_base_universe_d2_067_dvs_basefill_072}


def dvs_base_universe_d2_068_dvs_basefill_073(dvs_basefill_073):
    return _base_universe_d2(dvs_basefill_073, 68)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_068_dvs_basefill_073'] = {'inputs': ['dvs_basefill_073'], 'func': dvs_base_universe_d2_068_dvs_basefill_073}


def dvs_base_universe_d2_069_dvs_basefill_074(dvs_basefill_074):
    return _base_universe_d2(dvs_basefill_074, 69)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_069_dvs_basefill_074'] = {'inputs': ['dvs_basefill_074'], 'func': dvs_base_universe_d2_069_dvs_basefill_074}


def dvs_base_universe_d2_070_dvs_basefill_075(dvs_basefill_075):
    return _base_universe_d2(dvs_basefill_075, 70)
DVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['dvs_base_universe_d2_070_dvs_basefill_075'] = {'inputs': ['dvs_basefill_075'], 'func': dvs_base_universe_d2_070_dvs_basefill_075}
