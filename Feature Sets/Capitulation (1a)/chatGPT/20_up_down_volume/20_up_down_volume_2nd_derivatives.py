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



def udv_151_udv_001_volume_spike_ratio_5_001_roc_1(udv_001_volume_spike_ratio_5_001):
    feature = _s(udv_001_volume_spike_ratio_5_001)
    return (_roc(feature, 1)).reindex(feature.index)

def udv_152_udv_007_volume_spike_ratio_126_007_roc_5(udv_007_volume_spike_ratio_126_007):
    feature = _s(udv_007_volume_spike_ratio_126_007)
    return (_roc(feature, 5)).reindex(feature.index)

def udv_153_udv_013_volume_spike_ratio_1008_013_roc_42(udv_013_volume_spike_ratio_1008_013):
    feature = _s(udv_013_volume_spike_ratio_1008_013)
    return (_roc(feature, 42)).reindex(feature.index)

def udv_154_udv_019_volume_spike_ratio_42_019_roc_126(udv_019_volume_spike_ratio_42_019):
    feature = _s(udv_019_volume_spike_ratio_42_019)
    return (_roc(feature, 126)).reindex(feature.index)

def udv_155_udv_025_volume_spike_ratio_378_025_roc_378(udv_025_volume_spike_ratio_378_025):
    feature = _s(udv_025_volume_spike_ratio_378_025)
    return (_roc(feature, 378)).reindex(feature.index)






















UP_DOWN_VOLUME_REGISTRY_2ND_DERIVATIVES = {
    'udv_151_udv_001_volume_spike_ratio_5_001_roc_1': {'inputs': ['udv_001_volume_spike_ratio_5_001'], 'func': udv_151_udv_001_volume_spike_ratio_5_001_roc_1},
    'udv_152_udv_007_volume_spike_ratio_126_007_roc_5': {'inputs': ['udv_007_volume_spike_ratio_126_007'], 'func': udv_152_udv_007_volume_spike_ratio_126_007_roc_5},
    'udv_153_udv_013_volume_spike_ratio_1008_013_roc_42': {'inputs': ['udv_013_volume_spike_ratio_1008_013'], 'func': udv_153_udv_013_volume_spike_ratio_1008_013_roc_42},
    'udv_154_udv_019_volume_spike_ratio_42_019_roc_126': {'inputs': ['udv_019_volume_spike_ratio_42_019'], 'func': udv_154_udv_019_volume_spike_ratio_42_019_roc_126},
    'udv_155_udv_025_volume_spike_ratio_378_025_roc_378': {'inputs': ['udv_025_volume_spike_ratio_378_025'], 'func': udv_155_udv_025_volume_spike_ratio_378_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def udv_replacement_d2_001(udv_replacement_001):
    feature = _clean(udv_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_001'] = {'inputs': ['udv_replacement_001'], 'func': udv_replacement_d2_001}


def udv_replacement_d2_002(udv_replacement_002):
    feature = _clean(udv_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_002'] = {'inputs': ['udv_replacement_002'], 'func': udv_replacement_d2_002}


def udv_replacement_d2_003(udv_replacement_003):
    feature = _clean(udv_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_003'] = {'inputs': ['udv_replacement_003'], 'func': udv_replacement_d2_003}


def udv_replacement_d2_004(udv_replacement_004):
    feature = _clean(udv_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_004'] = {'inputs': ['udv_replacement_004'], 'func': udv_replacement_d2_004}


def udv_replacement_d2_005(udv_replacement_005):
    feature = _clean(udv_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_005'] = {'inputs': ['udv_replacement_005'], 'func': udv_replacement_d2_005}


def udv_replacement_d2_006(udv_replacement_006):
    feature = _clean(udv_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_006'] = {'inputs': ['udv_replacement_006'], 'func': udv_replacement_d2_006}


def udv_replacement_d2_007(udv_replacement_007):
    feature = _clean(udv_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_007'] = {'inputs': ['udv_replacement_007'], 'func': udv_replacement_d2_007}


def udv_replacement_d2_008(udv_replacement_008):
    feature = _clean(udv_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_008'] = {'inputs': ['udv_replacement_008'], 'func': udv_replacement_d2_008}


def udv_replacement_d2_009(udv_replacement_009):
    feature = _clean(udv_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_009'] = {'inputs': ['udv_replacement_009'], 'func': udv_replacement_d2_009}


def udv_replacement_d2_010(udv_replacement_010):
    feature = _clean(udv_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_010'] = {'inputs': ['udv_replacement_010'], 'func': udv_replacement_d2_010}


def udv_replacement_d2_011(udv_replacement_011):
    feature = _clean(udv_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_011'] = {'inputs': ['udv_replacement_011'], 'func': udv_replacement_d2_011}


def udv_replacement_d2_012(udv_replacement_012):
    feature = _clean(udv_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_012'] = {'inputs': ['udv_replacement_012'], 'func': udv_replacement_d2_012}


def udv_replacement_d2_013(udv_replacement_013):
    feature = _clean(udv_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_013'] = {'inputs': ['udv_replacement_013'], 'func': udv_replacement_d2_013}


def udv_replacement_d2_014(udv_replacement_014):
    feature = _clean(udv_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_014'] = {'inputs': ['udv_replacement_014'], 'func': udv_replacement_d2_014}


def udv_replacement_d2_015(udv_replacement_015):
    feature = _clean(udv_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_015'] = {'inputs': ['udv_replacement_015'], 'func': udv_replacement_d2_015}


def udv_replacement_d2_016(udv_replacement_016):
    feature = _clean(udv_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_016'] = {'inputs': ['udv_replacement_016'], 'func': udv_replacement_d2_016}


def udv_replacement_d2_017(udv_replacement_017):
    feature = _clean(udv_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_017'] = {'inputs': ['udv_replacement_017'], 'func': udv_replacement_d2_017}


def udv_replacement_d2_018(udv_replacement_018):
    feature = _clean(udv_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_018'] = {'inputs': ['udv_replacement_018'], 'func': udv_replacement_d2_018}


def udv_replacement_d2_019(udv_replacement_019):
    feature = _clean(udv_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_019'] = {'inputs': ['udv_replacement_019'], 'func': udv_replacement_d2_019}


def udv_replacement_d2_020(udv_replacement_020):
    feature = _clean(udv_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_020'] = {'inputs': ['udv_replacement_020'], 'func': udv_replacement_d2_020}


def udv_replacement_d2_021(udv_replacement_021):
    feature = _clean(udv_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_021'] = {'inputs': ['udv_replacement_021'], 'func': udv_replacement_d2_021}


def udv_replacement_d2_022(udv_replacement_022):
    feature = _clean(udv_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_022'] = {'inputs': ['udv_replacement_022'], 'func': udv_replacement_d2_022}


def udv_replacement_d2_023(udv_replacement_023):
    feature = _clean(udv_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_023'] = {'inputs': ['udv_replacement_023'], 'func': udv_replacement_d2_023}


def udv_replacement_d2_024(udv_replacement_024):
    feature = _clean(udv_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_024'] = {'inputs': ['udv_replacement_024'], 'func': udv_replacement_d2_024}


def udv_replacement_d2_025(udv_replacement_025):
    feature = _clean(udv_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_025'] = {'inputs': ['udv_replacement_025'], 'func': udv_replacement_d2_025}


def udv_replacement_d2_026(udv_replacement_026):
    feature = _clean(udv_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_026'] = {'inputs': ['udv_replacement_026'], 'func': udv_replacement_d2_026}


def udv_replacement_d2_027(udv_replacement_027):
    feature = _clean(udv_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_027'] = {'inputs': ['udv_replacement_027'], 'func': udv_replacement_d2_027}


def udv_replacement_d2_028(udv_replacement_028):
    feature = _clean(udv_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_028'] = {'inputs': ['udv_replacement_028'], 'func': udv_replacement_d2_028}


def udv_replacement_d2_029(udv_replacement_029):
    feature = _clean(udv_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_029'] = {'inputs': ['udv_replacement_029'], 'func': udv_replacement_d2_029}


def udv_replacement_d2_030(udv_replacement_030):
    feature = _clean(udv_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_030'] = {'inputs': ['udv_replacement_030'], 'func': udv_replacement_d2_030}


def udv_replacement_d2_031(udv_replacement_031):
    feature = _clean(udv_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_031'] = {'inputs': ['udv_replacement_031'], 'func': udv_replacement_d2_031}


def udv_replacement_d2_032(udv_replacement_032):
    feature = _clean(udv_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_032'] = {'inputs': ['udv_replacement_032'], 'func': udv_replacement_d2_032}


def udv_replacement_d2_033(udv_replacement_033):
    feature = _clean(udv_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_033'] = {'inputs': ['udv_replacement_033'], 'func': udv_replacement_d2_033}


def udv_replacement_d2_034(udv_replacement_034):
    feature = _clean(udv_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_034'] = {'inputs': ['udv_replacement_034'], 'func': udv_replacement_d2_034}


def udv_replacement_d2_035(udv_replacement_035):
    feature = _clean(udv_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_035'] = {'inputs': ['udv_replacement_035'], 'func': udv_replacement_d2_035}


def udv_replacement_d2_036(udv_replacement_036):
    feature = _clean(udv_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_036'] = {'inputs': ['udv_replacement_036'], 'func': udv_replacement_d2_036}


def udv_replacement_d2_037(udv_replacement_037):
    feature = _clean(udv_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_037'] = {'inputs': ['udv_replacement_037'], 'func': udv_replacement_d2_037}


def udv_replacement_d2_038(udv_replacement_038):
    feature = _clean(udv_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_038'] = {'inputs': ['udv_replacement_038'], 'func': udv_replacement_d2_038}


def udv_replacement_d2_039(udv_replacement_039):
    feature = _clean(udv_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_039'] = {'inputs': ['udv_replacement_039'], 'func': udv_replacement_d2_039}


def udv_replacement_d2_040(udv_replacement_040):
    feature = _clean(udv_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_040'] = {'inputs': ['udv_replacement_040'], 'func': udv_replacement_d2_040}


def udv_replacement_d2_041(udv_replacement_041):
    feature = _clean(udv_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_041'] = {'inputs': ['udv_replacement_041'], 'func': udv_replacement_d2_041}


def udv_replacement_d2_042(udv_replacement_042):
    feature = _clean(udv_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_042'] = {'inputs': ['udv_replacement_042'], 'func': udv_replacement_d2_042}


def udv_replacement_d2_043(udv_replacement_043):
    feature = _clean(udv_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_043'] = {'inputs': ['udv_replacement_043'], 'func': udv_replacement_d2_043}


def udv_replacement_d2_044(udv_replacement_044):
    feature = _clean(udv_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_044'] = {'inputs': ['udv_replacement_044'], 'func': udv_replacement_d2_044}


def udv_replacement_d2_045(udv_replacement_045):
    feature = _clean(udv_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_045'] = {'inputs': ['udv_replacement_045'], 'func': udv_replacement_d2_045}


def udv_replacement_d2_046(udv_replacement_046):
    feature = _clean(udv_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_046'] = {'inputs': ['udv_replacement_046'], 'func': udv_replacement_d2_046}


def udv_replacement_d2_047(udv_replacement_047):
    feature = _clean(udv_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_047'] = {'inputs': ['udv_replacement_047'], 'func': udv_replacement_d2_047}


def udv_replacement_d2_048(udv_replacement_048):
    feature = _clean(udv_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_048'] = {'inputs': ['udv_replacement_048'], 'func': udv_replacement_d2_048}


def udv_replacement_d2_049(udv_replacement_049):
    feature = _clean(udv_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_049'] = {'inputs': ['udv_replacement_049'], 'func': udv_replacement_d2_049}


def udv_replacement_d2_050(udv_replacement_050):
    feature = _clean(udv_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_050'] = {'inputs': ['udv_replacement_050'], 'func': udv_replacement_d2_050}


def udv_replacement_d2_051(udv_replacement_051):
    feature = _clean(udv_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_051'] = {'inputs': ['udv_replacement_051'], 'func': udv_replacement_d2_051}


def udv_replacement_d2_052(udv_replacement_052):
    feature = _clean(udv_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_052'] = {'inputs': ['udv_replacement_052'], 'func': udv_replacement_d2_052}


def udv_replacement_d2_053(udv_replacement_053):
    feature = _clean(udv_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_053'] = {'inputs': ['udv_replacement_053'], 'func': udv_replacement_d2_053}


def udv_replacement_d2_054(udv_replacement_054):
    feature = _clean(udv_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_054'] = {'inputs': ['udv_replacement_054'], 'func': udv_replacement_d2_054}


def udv_replacement_d2_055(udv_replacement_055):
    feature = _clean(udv_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_055'] = {'inputs': ['udv_replacement_055'], 'func': udv_replacement_d2_055}


def udv_replacement_d2_056(udv_replacement_056):
    feature = _clean(udv_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_056'] = {'inputs': ['udv_replacement_056'], 'func': udv_replacement_d2_056}


def udv_replacement_d2_057(udv_replacement_057):
    feature = _clean(udv_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_057'] = {'inputs': ['udv_replacement_057'], 'func': udv_replacement_d2_057}


def udv_replacement_d2_058(udv_replacement_058):
    feature = _clean(udv_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_058'] = {'inputs': ['udv_replacement_058'], 'func': udv_replacement_d2_058}


def udv_replacement_d2_059(udv_replacement_059):
    feature = _clean(udv_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_059'] = {'inputs': ['udv_replacement_059'], 'func': udv_replacement_d2_059}


def udv_replacement_d2_060(udv_replacement_060):
    feature = _clean(udv_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_060'] = {'inputs': ['udv_replacement_060'], 'func': udv_replacement_d2_060}


def udv_replacement_d2_061(udv_replacement_061):
    feature = _clean(udv_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_061'] = {'inputs': ['udv_replacement_061'], 'func': udv_replacement_d2_061}


def udv_replacement_d2_062(udv_replacement_062):
    feature = _clean(udv_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_062'] = {'inputs': ['udv_replacement_062'], 'func': udv_replacement_d2_062}


def udv_replacement_d2_063(udv_replacement_063):
    feature = _clean(udv_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_063'] = {'inputs': ['udv_replacement_063'], 'func': udv_replacement_d2_063}


def udv_replacement_d2_064(udv_replacement_064):
    feature = _clean(udv_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_064'] = {'inputs': ['udv_replacement_064'], 'func': udv_replacement_d2_064}


def udv_replacement_d2_065(udv_replacement_065):
    feature = _clean(udv_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_065'] = {'inputs': ['udv_replacement_065'], 'func': udv_replacement_d2_065}


def udv_replacement_d2_066(udv_replacement_066):
    feature = _clean(udv_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_066'] = {'inputs': ['udv_replacement_066'], 'func': udv_replacement_d2_066}


def udv_replacement_d2_067(udv_replacement_067):
    feature = _clean(udv_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_067'] = {'inputs': ['udv_replacement_067'], 'func': udv_replacement_d2_067}


def udv_replacement_d2_068(udv_replacement_068):
    feature = _clean(udv_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_068'] = {'inputs': ['udv_replacement_068'], 'func': udv_replacement_d2_068}


def udv_replacement_d2_069(udv_replacement_069):
    feature = _clean(udv_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_069'] = {'inputs': ['udv_replacement_069'], 'func': udv_replacement_d2_069}


def udv_replacement_d2_070(udv_replacement_070):
    feature = _clean(udv_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_070'] = {'inputs': ['udv_replacement_070'], 'func': udv_replacement_d2_070}


def udv_replacement_d2_071(udv_replacement_071):
    feature = _clean(udv_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_071'] = {'inputs': ['udv_replacement_071'], 'func': udv_replacement_d2_071}


def udv_replacement_d2_072(udv_replacement_072):
    feature = _clean(udv_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_072'] = {'inputs': ['udv_replacement_072'], 'func': udv_replacement_d2_072}


def udv_replacement_d2_073(udv_replacement_073):
    feature = _clean(udv_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_073'] = {'inputs': ['udv_replacement_073'], 'func': udv_replacement_d2_073}


def udv_replacement_d2_074(udv_replacement_074):
    feature = _clean(udv_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_074'] = {'inputs': ['udv_replacement_074'], 'func': udv_replacement_d2_074}


def udv_replacement_d2_075(udv_replacement_075):
    feature = _clean(udv_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_075'] = {'inputs': ['udv_replacement_075'], 'func': udv_replacement_d2_075}


def udv_replacement_d2_076(udv_replacement_076):
    feature = _clean(udv_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_076'] = {'inputs': ['udv_replacement_076'], 'func': udv_replacement_d2_076}


def udv_replacement_d2_077(udv_replacement_077):
    feature = _clean(udv_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_077'] = {'inputs': ['udv_replacement_077'], 'func': udv_replacement_d2_077}


def udv_replacement_d2_078(udv_replacement_078):
    feature = _clean(udv_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_078'] = {'inputs': ['udv_replacement_078'], 'func': udv_replacement_d2_078}


def udv_replacement_d2_079(udv_replacement_079):
    feature = _clean(udv_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_079'] = {'inputs': ['udv_replacement_079'], 'func': udv_replacement_d2_079}


def udv_replacement_d2_080(udv_replacement_080):
    feature = _clean(udv_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_080'] = {'inputs': ['udv_replacement_080'], 'func': udv_replacement_d2_080}


def udv_replacement_d2_081(udv_replacement_081):
    feature = _clean(udv_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_081'] = {'inputs': ['udv_replacement_081'], 'func': udv_replacement_d2_081}


def udv_replacement_d2_082(udv_replacement_082):
    feature = _clean(udv_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_082'] = {'inputs': ['udv_replacement_082'], 'func': udv_replacement_d2_082}


def udv_replacement_d2_083(udv_replacement_083):
    feature = _clean(udv_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_083'] = {'inputs': ['udv_replacement_083'], 'func': udv_replacement_d2_083}


def udv_replacement_d2_084(udv_replacement_084):
    feature = _clean(udv_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_084'] = {'inputs': ['udv_replacement_084'], 'func': udv_replacement_d2_084}


def udv_replacement_d2_085(udv_replacement_085):
    feature = _clean(udv_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_085'] = {'inputs': ['udv_replacement_085'], 'func': udv_replacement_d2_085}


def udv_replacement_d2_086(udv_replacement_086):
    feature = _clean(udv_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_086'] = {'inputs': ['udv_replacement_086'], 'func': udv_replacement_d2_086}


def udv_replacement_d2_087(udv_replacement_087):
    feature = _clean(udv_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_087'] = {'inputs': ['udv_replacement_087'], 'func': udv_replacement_d2_087}


def udv_replacement_d2_088(udv_replacement_088):
    feature = _clean(udv_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_088'] = {'inputs': ['udv_replacement_088'], 'func': udv_replacement_d2_088}


def udv_replacement_d2_089(udv_replacement_089):
    feature = _clean(udv_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_089'] = {'inputs': ['udv_replacement_089'], 'func': udv_replacement_d2_089}


def udv_replacement_d2_090(udv_replacement_090):
    feature = _clean(udv_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_090'] = {'inputs': ['udv_replacement_090'], 'func': udv_replacement_d2_090}


def udv_replacement_d2_091(udv_replacement_091):
    feature = _clean(udv_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_091'] = {'inputs': ['udv_replacement_091'], 'func': udv_replacement_d2_091}


def udv_replacement_d2_092(udv_replacement_092):
    feature = _clean(udv_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_092'] = {'inputs': ['udv_replacement_092'], 'func': udv_replacement_d2_092}


def udv_replacement_d2_093(udv_replacement_093):
    feature = _clean(udv_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_093'] = {'inputs': ['udv_replacement_093'], 'func': udv_replacement_d2_093}


def udv_replacement_d2_094(udv_replacement_094):
    feature = _clean(udv_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_094'] = {'inputs': ['udv_replacement_094'], 'func': udv_replacement_d2_094}


def udv_replacement_d2_095(udv_replacement_095):
    feature = _clean(udv_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_095'] = {'inputs': ['udv_replacement_095'], 'func': udv_replacement_d2_095}


def udv_replacement_d2_096(udv_replacement_096):
    feature = _clean(udv_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_096'] = {'inputs': ['udv_replacement_096'], 'func': udv_replacement_d2_096}


def udv_replacement_d2_097(udv_replacement_097):
    feature = _clean(udv_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_097'] = {'inputs': ['udv_replacement_097'], 'func': udv_replacement_d2_097}


def udv_replacement_d2_098(udv_replacement_098):
    feature = _clean(udv_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_098'] = {'inputs': ['udv_replacement_098'], 'func': udv_replacement_d2_098}


def udv_replacement_d2_099(udv_replacement_099):
    feature = _clean(udv_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_099'] = {'inputs': ['udv_replacement_099'], 'func': udv_replacement_d2_099}


def udv_replacement_d2_100(udv_replacement_100):
    feature = _clean(udv_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_100'] = {'inputs': ['udv_replacement_100'], 'func': udv_replacement_d2_100}


def udv_replacement_d2_101(udv_replacement_101):
    feature = _clean(udv_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_101'] = {'inputs': ['udv_replacement_101'], 'func': udv_replacement_d2_101}


def udv_replacement_d2_102(udv_replacement_102):
    feature = _clean(udv_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_102'] = {'inputs': ['udv_replacement_102'], 'func': udv_replacement_d2_102}


def udv_replacement_d2_103(udv_replacement_103):
    feature = _clean(udv_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_103'] = {'inputs': ['udv_replacement_103'], 'func': udv_replacement_d2_103}


def udv_replacement_d2_104(udv_replacement_104):
    feature = _clean(udv_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_104'] = {'inputs': ['udv_replacement_104'], 'func': udv_replacement_d2_104}


def udv_replacement_d2_105(udv_replacement_105):
    feature = _clean(udv_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_105'] = {'inputs': ['udv_replacement_105'], 'func': udv_replacement_d2_105}


def udv_replacement_d2_106(udv_replacement_106):
    feature = _clean(udv_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_106'] = {'inputs': ['udv_replacement_106'], 'func': udv_replacement_d2_106}


def udv_replacement_d2_107(udv_replacement_107):
    feature = _clean(udv_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_107'] = {'inputs': ['udv_replacement_107'], 'func': udv_replacement_d2_107}


def udv_replacement_d2_108(udv_replacement_108):
    feature = _clean(udv_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_108'] = {'inputs': ['udv_replacement_108'], 'func': udv_replacement_d2_108}


def udv_replacement_d2_109(udv_replacement_109):
    feature = _clean(udv_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_109'] = {'inputs': ['udv_replacement_109'], 'func': udv_replacement_d2_109}


def udv_replacement_d2_110(udv_replacement_110):
    feature = _clean(udv_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_110'] = {'inputs': ['udv_replacement_110'], 'func': udv_replacement_d2_110}


def udv_replacement_d2_111(udv_replacement_111):
    feature = _clean(udv_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_111'] = {'inputs': ['udv_replacement_111'], 'func': udv_replacement_d2_111}


def udv_replacement_d2_112(udv_replacement_112):
    feature = _clean(udv_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_112'] = {'inputs': ['udv_replacement_112'], 'func': udv_replacement_d2_112}


def udv_replacement_d2_113(udv_replacement_113):
    feature = _clean(udv_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_113'] = {'inputs': ['udv_replacement_113'], 'func': udv_replacement_d2_113}


def udv_replacement_d2_114(udv_replacement_114):
    feature = _clean(udv_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_114'] = {'inputs': ['udv_replacement_114'], 'func': udv_replacement_d2_114}


def udv_replacement_d2_115(udv_replacement_115):
    feature = _clean(udv_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_115'] = {'inputs': ['udv_replacement_115'], 'func': udv_replacement_d2_115}


def udv_replacement_d2_116(udv_replacement_116):
    feature = _clean(udv_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_116'] = {'inputs': ['udv_replacement_116'], 'func': udv_replacement_d2_116}


def udv_replacement_d2_117(udv_replacement_117):
    feature = _clean(udv_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_117'] = {'inputs': ['udv_replacement_117'], 'func': udv_replacement_d2_117}


def udv_replacement_d2_118(udv_replacement_118):
    feature = _clean(udv_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_118'] = {'inputs': ['udv_replacement_118'], 'func': udv_replacement_d2_118}


def udv_replacement_d2_119(udv_replacement_119):
    feature = _clean(udv_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_119'] = {'inputs': ['udv_replacement_119'], 'func': udv_replacement_d2_119}


def udv_replacement_d2_120(udv_replacement_120):
    feature = _clean(udv_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_120'] = {'inputs': ['udv_replacement_120'], 'func': udv_replacement_d2_120}


def udv_replacement_d2_121(udv_replacement_121):
    feature = _clean(udv_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_121'] = {'inputs': ['udv_replacement_121'], 'func': udv_replacement_d2_121}


def udv_replacement_d2_122(udv_replacement_122):
    feature = _clean(udv_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_122'] = {'inputs': ['udv_replacement_122'], 'func': udv_replacement_d2_122}


def udv_replacement_d2_123(udv_replacement_123):
    feature = _clean(udv_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_123'] = {'inputs': ['udv_replacement_123'], 'func': udv_replacement_d2_123}


def udv_replacement_d2_124(udv_replacement_124):
    feature = _clean(udv_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_124'] = {'inputs': ['udv_replacement_124'], 'func': udv_replacement_d2_124}


def udv_replacement_d2_125(udv_replacement_125):
    feature = _clean(udv_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_125'] = {'inputs': ['udv_replacement_125'], 'func': udv_replacement_d2_125}


def udv_replacement_d2_126(udv_replacement_126):
    feature = _clean(udv_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_126'] = {'inputs': ['udv_replacement_126'], 'func': udv_replacement_d2_126}


def udv_replacement_d2_127(udv_replacement_127):
    feature = _clean(udv_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_127'] = {'inputs': ['udv_replacement_127'], 'func': udv_replacement_d2_127}


def udv_replacement_d2_128(udv_replacement_128):
    feature = _clean(udv_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_128'] = {'inputs': ['udv_replacement_128'], 'func': udv_replacement_d2_128}


def udv_replacement_d2_129(udv_replacement_129):
    feature = _clean(udv_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_129'] = {'inputs': ['udv_replacement_129'], 'func': udv_replacement_d2_129}


def udv_replacement_d2_130(udv_replacement_130):
    feature = _clean(udv_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_130'] = {'inputs': ['udv_replacement_130'], 'func': udv_replacement_d2_130}


def udv_replacement_d2_131(udv_replacement_131):
    feature = _clean(udv_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_131'] = {'inputs': ['udv_replacement_131'], 'func': udv_replacement_d2_131}


def udv_replacement_d2_132(udv_replacement_132):
    feature = _clean(udv_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_132'] = {'inputs': ['udv_replacement_132'], 'func': udv_replacement_d2_132}


def udv_replacement_d2_133(udv_replacement_133):
    feature = _clean(udv_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_133'] = {'inputs': ['udv_replacement_133'], 'func': udv_replacement_d2_133}


def udv_replacement_d2_134(udv_replacement_134):
    feature = _clean(udv_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_134'] = {'inputs': ['udv_replacement_134'], 'func': udv_replacement_d2_134}


def udv_replacement_d2_135(udv_replacement_135):
    feature = _clean(udv_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_135'] = {'inputs': ['udv_replacement_135'], 'func': udv_replacement_d2_135}


def udv_replacement_d2_136(udv_replacement_136):
    feature = _clean(udv_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_136'] = {'inputs': ['udv_replacement_136'], 'func': udv_replacement_d2_136}


def udv_replacement_d2_137(udv_replacement_137):
    feature = _clean(udv_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_137'] = {'inputs': ['udv_replacement_137'], 'func': udv_replacement_d2_137}


def udv_replacement_d2_138(udv_replacement_138):
    feature = _clean(udv_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_138'] = {'inputs': ['udv_replacement_138'], 'func': udv_replacement_d2_138}


def udv_replacement_d2_139(udv_replacement_139):
    feature = _clean(udv_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_139'] = {'inputs': ['udv_replacement_139'], 'func': udv_replacement_d2_139}


def udv_replacement_d2_140(udv_replacement_140):
    feature = _clean(udv_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_140'] = {'inputs': ['udv_replacement_140'], 'func': udv_replacement_d2_140}


def udv_replacement_d2_141(udv_replacement_141):
    feature = _clean(udv_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_141'] = {'inputs': ['udv_replacement_141'], 'func': udv_replacement_d2_141}


def udv_replacement_d2_142(udv_replacement_142):
    feature = _clean(udv_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_142'] = {'inputs': ['udv_replacement_142'], 'func': udv_replacement_d2_142}


def udv_replacement_d2_143(udv_replacement_143):
    feature = _clean(udv_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_143'] = {'inputs': ['udv_replacement_143'], 'func': udv_replacement_d2_143}


def udv_replacement_d2_144(udv_replacement_144):
    feature = _clean(udv_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_144'] = {'inputs': ['udv_replacement_144'], 'func': udv_replacement_d2_144}


def udv_replacement_d2_145(udv_replacement_145):
    feature = _clean(udv_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_145'] = {'inputs': ['udv_replacement_145'], 'func': udv_replacement_d2_145}


def udv_replacement_d2_146(udv_replacement_146):
    feature = _clean(udv_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_146'] = {'inputs': ['udv_replacement_146'], 'func': udv_replacement_d2_146}


def udv_replacement_d2_147(udv_replacement_147):
    feature = _clean(udv_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_147'] = {'inputs': ['udv_replacement_147'], 'func': udv_replacement_d2_147}


def udv_replacement_d2_148(udv_replacement_148):
    feature = _clean(udv_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_148'] = {'inputs': ['udv_replacement_148'], 'func': udv_replacement_d2_148}


def udv_replacement_d2_149(udv_replacement_149):
    feature = _clean(udv_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_149'] = {'inputs': ['udv_replacement_149'], 'func': udv_replacement_d2_149}


def udv_replacement_d2_150(udv_replacement_150):
    feature = _clean(udv_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_150'] = {'inputs': ['udv_replacement_150'], 'func': udv_replacement_d2_150}


def udv_replacement_d2_151(udv_replacement_151):
    feature = _clean(udv_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_151'] = {'inputs': ['udv_replacement_151'], 'func': udv_replacement_d2_151}


def udv_replacement_d2_152(udv_replacement_152):
    feature = _clean(udv_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_152'] = {'inputs': ['udv_replacement_152'], 'func': udv_replacement_d2_152}


def udv_replacement_d2_153(udv_replacement_153):
    feature = _clean(udv_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_153'] = {'inputs': ['udv_replacement_153'], 'func': udv_replacement_d2_153}


def udv_replacement_d2_154(udv_replacement_154):
    feature = _clean(udv_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_154'] = {'inputs': ['udv_replacement_154'], 'func': udv_replacement_d2_154}


def udv_replacement_d2_155(udv_replacement_155):
    feature = _clean(udv_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_155'] = {'inputs': ['udv_replacement_155'], 'func': udv_replacement_d2_155}


def udv_replacement_d2_156(udv_replacement_156):
    feature = _clean(udv_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_156'] = {'inputs': ['udv_replacement_156'], 'func': udv_replacement_d2_156}


def udv_replacement_d2_157(udv_replacement_157):
    feature = _clean(udv_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_157'] = {'inputs': ['udv_replacement_157'], 'func': udv_replacement_d2_157}


def udv_replacement_d2_158(udv_replacement_158):
    feature = _clean(udv_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_158'] = {'inputs': ['udv_replacement_158'], 'func': udv_replacement_d2_158}


def udv_replacement_d2_159(udv_replacement_159):
    feature = _clean(udv_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_159'] = {'inputs': ['udv_replacement_159'], 'func': udv_replacement_d2_159}


def udv_replacement_d2_160(udv_replacement_160):
    feature = _clean(udv_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
UDV_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['udv_replacement_d2_160'] = {'inputs': ['udv_replacement_160'], 'func': udv_replacement_d2_160}


# Base-universe derivative extensions for repaired first-base features.
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def udv_base_universe_d2_001_udv_002_volume_zscore_10_002(udv_002_volume_zscore_10_002):
    return _base_universe_d2(udv_002_volume_zscore_10_002, 1)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_001_udv_002_volume_zscore_10_002'] = {'inputs': ['udv_002_volume_zscore_10_002'], 'func': udv_base_universe_d2_001_udv_002_volume_zscore_10_002}


def udv_base_universe_d2_002_udv_003_down_volume_share_21_003(udv_003_down_volume_share_21_003):
    return _base_universe_d2(udv_003_down_volume_share_21_003, 2)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_002_udv_003_down_volume_share_21_003'] = {'inputs': ['udv_003_down_volume_share_21_003'], 'func': udv_base_universe_d2_002_udv_003_down_volume_share_21_003}


def udv_base_universe_d2_003_udv_004_dollar_volume_shock_42_004(udv_004_dollar_volume_shock_42_004):
    return _base_universe_d2(udv_004_dollar_volume_shock_42_004, 3)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_003_udv_004_dollar_volume_shock_42_004'] = {'inputs': ['udv_004_dollar_volume_shock_42_004'], 'func': udv_base_universe_d2_003_udv_004_dollar_volume_shock_42_004}


def udv_base_universe_d2_004_udv_005_volume_trend_slope_63_005(udv_005_volume_trend_slope_63_005):
    return _base_universe_d2(udv_005_volume_trend_slope_63_005, 4)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_004_udv_005_volume_trend_slope_63_005'] = {'inputs': ['udv_005_volume_trend_slope_63_005'], 'func': udv_base_universe_d2_004_udv_005_volume_trend_slope_63_005}


def udv_base_universe_d2_005_udv_006_price_volume_divergence_84_006(udv_006_price_volume_divergence_84_006):
    return _base_universe_d2(udv_006_price_volume_divergence_84_006, 5)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_005_udv_006_price_volume_divergence_84_006'] = {'inputs': ['udv_006_price_volume_divergence_84_006'], 'func': udv_base_universe_d2_005_udv_006_price_volume_divergence_84_006}


def udv_base_universe_d2_006_udv_008_volume_zscore_189_008(udv_008_volume_zscore_189_008):
    return _base_universe_d2(udv_008_volume_zscore_189_008, 6)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_006_udv_008_volume_zscore_189_008'] = {'inputs': ['udv_008_volume_zscore_189_008'], 'func': udv_base_universe_d2_006_udv_008_volume_zscore_189_008}


def udv_base_universe_d2_007_udv_009_down_volume_share_252_009(udv_009_down_volume_share_252_009):
    return _base_universe_d2(udv_009_down_volume_share_252_009, 7)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_007_udv_009_down_volume_share_252_009'] = {'inputs': ['udv_009_down_volume_share_252_009'], 'func': udv_base_universe_d2_007_udv_009_down_volume_share_252_009}


def udv_base_universe_d2_008_udv_010_dollar_volume_shock_378_010(udv_010_dollar_volume_shock_378_010):
    return _base_universe_d2(udv_010_dollar_volume_shock_378_010, 8)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_008_udv_010_dollar_volume_shock_378_010'] = {'inputs': ['udv_010_dollar_volume_shock_378_010'], 'func': udv_base_universe_d2_008_udv_010_dollar_volume_shock_378_010}


def udv_base_universe_d2_009_udv_011_volume_trend_slope_504_011(udv_011_volume_trend_slope_504_011):
    return _base_universe_d2(udv_011_volume_trend_slope_504_011, 9)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_009_udv_011_volume_trend_slope_504_011'] = {'inputs': ['udv_011_volume_trend_slope_504_011'], 'func': udv_base_universe_d2_009_udv_011_volume_trend_slope_504_011}


def udv_base_universe_d2_010_udv_012_price_volume_divergence_756_012(udv_012_price_volume_divergence_756_012):
    return _base_universe_d2(udv_012_price_volume_divergence_756_012, 10)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_010_udv_012_price_volume_divergence_756_012'] = {'inputs': ['udv_012_price_volume_divergence_756_012'], 'func': udv_base_universe_d2_010_udv_012_price_volume_divergence_756_012}


def udv_base_universe_d2_011_udv_014_volume_zscore_1260_014(udv_014_volume_zscore_1260_014):
    return _base_universe_d2(udv_014_volume_zscore_1260_014, 11)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_011_udv_014_volume_zscore_1260_014'] = {'inputs': ['udv_014_volume_zscore_1260_014'], 'func': udv_base_universe_d2_011_udv_014_volume_zscore_1260_014}


def udv_base_universe_d2_012_udv_015_down_volume_share_1512_015(udv_015_down_volume_share_1512_015):
    return _base_universe_d2(udv_015_down_volume_share_1512_015, 12)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_012_udv_015_down_volume_share_1512_015'] = {'inputs': ['udv_015_down_volume_share_1512_015'], 'func': udv_base_universe_d2_012_udv_015_down_volume_share_1512_015}


def udv_base_universe_d2_013_udv_016_dollar_volume_shock_5_016(udv_016_dollar_volume_shock_5_016):
    return _base_universe_d2(udv_016_dollar_volume_shock_5_016, 13)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_013_udv_016_dollar_volume_shock_5_016'] = {'inputs': ['udv_016_dollar_volume_shock_5_016'], 'func': udv_base_universe_d2_013_udv_016_dollar_volume_shock_5_016}


def udv_base_universe_d2_014_udv_017_volume_trend_slope_10_017(udv_017_volume_trend_slope_10_017):
    return _base_universe_d2(udv_017_volume_trend_slope_10_017, 14)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_014_udv_017_volume_trend_slope_10_017'] = {'inputs': ['udv_017_volume_trend_slope_10_017'], 'func': udv_base_universe_d2_014_udv_017_volume_trend_slope_10_017}


def udv_base_universe_d2_015_udv_018_price_volume_divergence_21_018(udv_018_price_volume_divergence_21_018):
    return _base_universe_d2(udv_018_price_volume_divergence_21_018, 15)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_015_udv_018_price_volume_divergence_21_018'] = {'inputs': ['udv_018_price_volume_divergence_21_018'], 'func': udv_base_universe_d2_015_udv_018_price_volume_divergence_21_018}


def udv_base_universe_d2_016_udv_020_volume_zscore_63_020(udv_020_volume_zscore_63_020):
    return _base_universe_d2(udv_020_volume_zscore_63_020, 16)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_016_udv_020_volume_zscore_63_020'] = {'inputs': ['udv_020_volume_zscore_63_020'], 'func': udv_base_universe_d2_016_udv_020_volume_zscore_63_020}


def udv_base_universe_d2_017_udv_021_down_volume_share_84_021(udv_021_down_volume_share_84_021):
    return _base_universe_d2(udv_021_down_volume_share_84_021, 17)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_017_udv_021_down_volume_share_84_021'] = {'inputs': ['udv_021_down_volume_share_84_021'], 'func': udv_base_universe_d2_017_udv_021_down_volume_share_84_021}


def udv_base_universe_d2_018_udv_022_dollar_volume_shock_126_022(udv_022_dollar_volume_shock_126_022):
    return _base_universe_d2(udv_022_dollar_volume_shock_126_022, 18)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_018_udv_022_dollar_volume_shock_126_022'] = {'inputs': ['udv_022_dollar_volume_shock_126_022'], 'func': udv_base_universe_d2_018_udv_022_dollar_volume_shock_126_022}


def udv_base_universe_d2_019_udv_023_volume_trend_slope_189_023(udv_023_volume_trend_slope_189_023):
    return _base_universe_d2(udv_023_volume_trend_slope_189_023, 19)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_019_udv_023_volume_trend_slope_189_023'] = {'inputs': ['udv_023_volume_trend_slope_189_023'], 'func': udv_base_universe_d2_019_udv_023_volume_trend_slope_189_023}


def udv_base_universe_d2_020_udv_024_price_volume_divergence_252_024(udv_024_price_volume_divergence_252_024):
    return _base_universe_d2(udv_024_price_volume_divergence_252_024, 20)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_020_udv_024_price_volume_divergence_252_024'] = {'inputs': ['udv_024_price_volume_divergence_252_024'], 'func': udv_base_universe_d2_020_udv_024_price_volume_divergence_252_024}


def udv_base_universe_d2_021_udv_026_volume_zscore_504_026(udv_026_volume_zscore_504_026):
    return _base_universe_d2(udv_026_volume_zscore_504_026, 21)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_021_udv_026_volume_zscore_504_026'] = {'inputs': ['udv_026_volume_zscore_504_026'], 'func': udv_base_universe_d2_021_udv_026_volume_zscore_504_026}


def udv_base_universe_d2_022_udv_027_down_volume_share_756_027(udv_027_down_volume_share_756_027):
    return _base_universe_d2(udv_027_down_volume_share_756_027, 22)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_022_udv_027_down_volume_share_756_027'] = {'inputs': ['udv_027_down_volume_share_756_027'], 'func': udv_base_universe_d2_022_udv_027_down_volume_share_756_027}


def udv_base_universe_d2_023_udv_028_dollar_volume_shock_1008_028(udv_028_dollar_volume_shock_1008_028):
    return _base_universe_d2(udv_028_dollar_volume_shock_1008_028, 23)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_023_udv_028_dollar_volume_shock_1008_028'] = {'inputs': ['udv_028_dollar_volume_shock_1008_028'], 'func': udv_base_universe_d2_023_udv_028_dollar_volume_shock_1008_028}


def udv_base_universe_d2_024_udv_029_volume_trend_slope_1260_029(udv_029_volume_trend_slope_1260_029):
    return _base_universe_d2(udv_029_volume_trend_slope_1260_029, 24)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_024_udv_029_volume_trend_slope_1260_029'] = {'inputs': ['udv_029_volume_trend_slope_1260_029'], 'func': udv_base_universe_d2_024_udv_029_volume_trend_slope_1260_029}


def udv_base_universe_d2_025_udv_030_price_volume_divergence_1512_030(udv_030_price_volume_divergence_1512_030):
    return _base_universe_d2(udv_030_price_volume_divergence_1512_030, 25)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_025_udv_030_price_volume_divergence_1512_030'] = {'inputs': ['udv_030_price_volume_divergence_1512_030'], 'func': udv_base_universe_d2_025_udv_030_price_volume_divergence_1512_030}


def udv_base_universe_d2_026_udv_basefill_031(udv_basefill_031):
    return _base_universe_d2(udv_basefill_031, 26)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_026_udv_basefill_031'] = {'inputs': ['udv_basefill_031'], 'func': udv_base_universe_d2_026_udv_basefill_031}


def udv_base_universe_d2_027_udv_basefill_032(udv_basefill_032):
    return _base_universe_d2(udv_basefill_032, 27)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_027_udv_basefill_032'] = {'inputs': ['udv_basefill_032'], 'func': udv_base_universe_d2_027_udv_basefill_032}


def udv_base_universe_d2_028_udv_basefill_033(udv_basefill_033):
    return _base_universe_d2(udv_basefill_033, 28)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_028_udv_basefill_033'] = {'inputs': ['udv_basefill_033'], 'func': udv_base_universe_d2_028_udv_basefill_033}


def udv_base_universe_d2_029_udv_basefill_034(udv_basefill_034):
    return _base_universe_d2(udv_basefill_034, 29)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_029_udv_basefill_034'] = {'inputs': ['udv_basefill_034'], 'func': udv_base_universe_d2_029_udv_basefill_034}


def udv_base_universe_d2_030_udv_basefill_035(udv_basefill_035):
    return _base_universe_d2(udv_basefill_035, 30)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_030_udv_basefill_035'] = {'inputs': ['udv_basefill_035'], 'func': udv_base_universe_d2_030_udv_basefill_035}


def udv_base_universe_d2_031_udv_basefill_036(udv_basefill_036):
    return _base_universe_d2(udv_basefill_036, 31)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_031_udv_basefill_036'] = {'inputs': ['udv_basefill_036'], 'func': udv_base_universe_d2_031_udv_basefill_036}


def udv_base_universe_d2_032_udv_basefill_037(udv_basefill_037):
    return _base_universe_d2(udv_basefill_037, 32)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_032_udv_basefill_037'] = {'inputs': ['udv_basefill_037'], 'func': udv_base_universe_d2_032_udv_basefill_037}


def udv_base_universe_d2_033_udv_basefill_038(udv_basefill_038):
    return _base_universe_d2(udv_basefill_038, 33)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_033_udv_basefill_038'] = {'inputs': ['udv_basefill_038'], 'func': udv_base_universe_d2_033_udv_basefill_038}


def udv_base_universe_d2_034_udv_basefill_039(udv_basefill_039):
    return _base_universe_d2(udv_basefill_039, 34)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_034_udv_basefill_039'] = {'inputs': ['udv_basefill_039'], 'func': udv_base_universe_d2_034_udv_basefill_039}


def udv_base_universe_d2_035_udv_basefill_040(udv_basefill_040):
    return _base_universe_d2(udv_basefill_040, 35)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_035_udv_basefill_040'] = {'inputs': ['udv_basefill_040'], 'func': udv_base_universe_d2_035_udv_basefill_040}


def udv_base_universe_d2_036_udv_basefill_041(udv_basefill_041):
    return _base_universe_d2(udv_basefill_041, 36)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_036_udv_basefill_041'] = {'inputs': ['udv_basefill_041'], 'func': udv_base_universe_d2_036_udv_basefill_041}


def udv_base_universe_d2_037_udv_basefill_042(udv_basefill_042):
    return _base_universe_d2(udv_basefill_042, 37)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_037_udv_basefill_042'] = {'inputs': ['udv_basefill_042'], 'func': udv_base_universe_d2_037_udv_basefill_042}


def udv_base_universe_d2_038_udv_basefill_043(udv_basefill_043):
    return _base_universe_d2(udv_basefill_043, 38)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_038_udv_basefill_043'] = {'inputs': ['udv_basefill_043'], 'func': udv_base_universe_d2_038_udv_basefill_043}


def udv_base_universe_d2_039_udv_basefill_044(udv_basefill_044):
    return _base_universe_d2(udv_basefill_044, 39)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_039_udv_basefill_044'] = {'inputs': ['udv_basefill_044'], 'func': udv_base_universe_d2_039_udv_basefill_044}


def udv_base_universe_d2_040_udv_basefill_045(udv_basefill_045):
    return _base_universe_d2(udv_basefill_045, 40)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_040_udv_basefill_045'] = {'inputs': ['udv_basefill_045'], 'func': udv_base_universe_d2_040_udv_basefill_045}


def udv_base_universe_d2_041_udv_basefill_046(udv_basefill_046):
    return _base_universe_d2(udv_basefill_046, 41)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_041_udv_basefill_046'] = {'inputs': ['udv_basefill_046'], 'func': udv_base_universe_d2_041_udv_basefill_046}


def udv_base_universe_d2_042_udv_basefill_047(udv_basefill_047):
    return _base_universe_d2(udv_basefill_047, 42)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_042_udv_basefill_047'] = {'inputs': ['udv_basefill_047'], 'func': udv_base_universe_d2_042_udv_basefill_047}


def udv_base_universe_d2_043_udv_basefill_048(udv_basefill_048):
    return _base_universe_d2(udv_basefill_048, 43)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_043_udv_basefill_048'] = {'inputs': ['udv_basefill_048'], 'func': udv_base_universe_d2_043_udv_basefill_048}


def udv_base_universe_d2_044_udv_basefill_049(udv_basefill_049):
    return _base_universe_d2(udv_basefill_049, 44)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_044_udv_basefill_049'] = {'inputs': ['udv_basefill_049'], 'func': udv_base_universe_d2_044_udv_basefill_049}


def udv_base_universe_d2_045_udv_basefill_050(udv_basefill_050):
    return _base_universe_d2(udv_basefill_050, 45)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_045_udv_basefill_050'] = {'inputs': ['udv_basefill_050'], 'func': udv_base_universe_d2_045_udv_basefill_050}


def udv_base_universe_d2_046_udv_basefill_051(udv_basefill_051):
    return _base_universe_d2(udv_basefill_051, 46)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_046_udv_basefill_051'] = {'inputs': ['udv_basefill_051'], 'func': udv_base_universe_d2_046_udv_basefill_051}


def udv_base_universe_d2_047_udv_basefill_052(udv_basefill_052):
    return _base_universe_d2(udv_basefill_052, 47)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_047_udv_basefill_052'] = {'inputs': ['udv_basefill_052'], 'func': udv_base_universe_d2_047_udv_basefill_052}


def udv_base_universe_d2_048_udv_basefill_053(udv_basefill_053):
    return _base_universe_d2(udv_basefill_053, 48)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_048_udv_basefill_053'] = {'inputs': ['udv_basefill_053'], 'func': udv_base_universe_d2_048_udv_basefill_053}


def udv_base_universe_d2_049_udv_basefill_054(udv_basefill_054):
    return _base_universe_d2(udv_basefill_054, 49)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_049_udv_basefill_054'] = {'inputs': ['udv_basefill_054'], 'func': udv_base_universe_d2_049_udv_basefill_054}


def udv_base_universe_d2_050_udv_basefill_055(udv_basefill_055):
    return _base_universe_d2(udv_basefill_055, 50)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_050_udv_basefill_055'] = {'inputs': ['udv_basefill_055'], 'func': udv_base_universe_d2_050_udv_basefill_055}


def udv_base_universe_d2_051_udv_basefill_056(udv_basefill_056):
    return _base_universe_d2(udv_basefill_056, 51)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_051_udv_basefill_056'] = {'inputs': ['udv_basefill_056'], 'func': udv_base_universe_d2_051_udv_basefill_056}


def udv_base_universe_d2_052_udv_basefill_057(udv_basefill_057):
    return _base_universe_d2(udv_basefill_057, 52)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_052_udv_basefill_057'] = {'inputs': ['udv_basefill_057'], 'func': udv_base_universe_d2_052_udv_basefill_057}


def udv_base_universe_d2_053_udv_basefill_058(udv_basefill_058):
    return _base_universe_d2(udv_basefill_058, 53)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_053_udv_basefill_058'] = {'inputs': ['udv_basefill_058'], 'func': udv_base_universe_d2_053_udv_basefill_058}


def udv_base_universe_d2_054_udv_basefill_059(udv_basefill_059):
    return _base_universe_d2(udv_basefill_059, 54)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_054_udv_basefill_059'] = {'inputs': ['udv_basefill_059'], 'func': udv_base_universe_d2_054_udv_basefill_059}


def udv_base_universe_d2_055_udv_basefill_060(udv_basefill_060):
    return _base_universe_d2(udv_basefill_060, 55)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_055_udv_basefill_060'] = {'inputs': ['udv_basefill_060'], 'func': udv_base_universe_d2_055_udv_basefill_060}


def udv_base_universe_d2_056_udv_basefill_061(udv_basefill_061):
    return _base_universe_d2(udv_basefill_061, 56)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_056_udv_basefill_061'] = {'inputs': ['udv_basefill_061'], 'func': udv_base_universe_d2_056_udv_basefill_061}


def udv_base_universe_d2_057_udv_basefill_062(udv_basefill_062):
    return _base_universe_d2(udv_basefill_062, 57)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_057_udv_basefill_062'] = {'inputs': ['udv_basefill_062'], 'func': udv_base_universe_d2_057_udv_basefill_062}


def udv_base_universe_d2_058_udv_basefill_063(udv_basefill_063):
    return _base_universe_d2(udv_basefill_063, 58)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_058_udv_basefill_063'] = {'inputs': ['udv_basefill_063'], 'func': udv_base_universe_d2_058_udv_basefill_063}


def udv_base_universe_d2_059_udv_basefill_064(udv_basefill_064):
    return _base_universe_d2(udv_basefill_064, 59)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_059_udv_basefill_064'] = {'inputs': ['udv_basefill_064'], 'func': udv_base_universe_d2_059_udv_basefill_064}


def udv_base_universe_d2_060_udv_basefill_065(udv_basefill_065):
    return _base_universe_d2(udv_basefill_065, 60)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_060_udv_basefill_065'] = {'inputs': ['udv_basefill_065'], 'func': udv_base_universe_d2_060_udv_basefill_065}


def udv_base_universe_d2_061_udv_basefill_066(udv_basefill_066):
    return _base_universe_d2(udv_basefill_066, 61)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_061_udv_basefill_066'] = {'inputs': ['udv_basefill_066'], 'func': udv_base_universe_d2_061_udv_basefill_066}


def udv_base_universe_d2_062_udv_basefill_067(udv_basefill_067):
    return _base_universe_d2(udv_basefill_067, 62)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_062_udv_basefill_067'] = {'inputs': ['udv_basefill_067'], 'func': udv_base_universe_d2_062_udv_basefill_067}


def udv_base_universe_d2_063_udv_basefill_068(udv_basefill_068):
    return _base_universe_d2(udv_basefill_068, 63)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_063_udv_basefill_068'] = {'inputs': ['udv_basefill_068'], 'func': udv_base_universe_d2_063_udv_basefill_068}


def udv_base_universe_d2_064_udv_basefill_069(udv_basefill_069):
    return _base_universe_d2(udv_basefill_069, 64)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_064_udv_basefill_069'] = {'inputs': ['udv_basefill_069'], 'func': udv_base_universe_d2_064_udv_basefill_069}


def udv_base_universe_d2_065_udv_basefill_070(udv_basefill_070):
    return _base_universe_d2(udv_basefill_070, 65)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_065_udv_basefill_070'] = {'inputs': ['udv_basefill_070'], 'func': udv_base_universe_d2_065_udv_basefill_070}


def udv_base_universe_d2_066_udv_basefill_071(udv_basefill_071):
    return _base_universe_d2(udv_basefill_071, 66)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_066_udv_basefill_071'] = {'inputs': ['udv_basefill_071'], 'func': udv_base_universe_d2_066_udv_basefill_071}


def udv_base_universe_d2_067_udv_basefill_072(udv_basefill_072):
    return _base_universe_d2(udv_basefill_072, 67)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_067_udv_basefill_072'] = {'inputs': ['udv_basefill_072'], 'func': udv_base_universe_d2_067_udv_basefill_072}


def udv_base_universe_d2_068_udv_basefill_073(udv_basefill_073):
    return _base_universe_d2(udv_basefill_073, 68)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_068_udv_basefill_073'] = {'inputs': ['udv_basefill_073'], 'func': udv_base_universe_d2_068_udv_basefill_073}


def udv_base_universe_d2_069_udv_basefill_074(udv_basefill_074):
    return _base_universe_d2(udv_basefill_074, 69)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_069_udv_basefill_074'] = {'inputs': ['udv_basefill_074'], 'func': udv_base_universe_d2_069_udv_basefill_074}


def udv_base_universe_d2_070_udv_basefill_075(udv_basefill_075):
    return _base_universe_d2(udv_basefill_075, 70)
UDV_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['udv_base_universe_d2_070_udv_basefill_075'] = {'inputs': ['udv_basefill_075'], 'func': udv_base_universe_d2_070_udv_basefill_075}
