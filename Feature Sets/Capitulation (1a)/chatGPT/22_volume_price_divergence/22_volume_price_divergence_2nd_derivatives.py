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



def vpd_151_vpd_001_volume_spike_ratio_5_001_roc_1(vpd_001_volume_spike_ratio_5_001):
    feature = _s(vpd_001_volume_spike_ratio_5_001)
    return (_roc(feature, 1)).reindex(feature.index)

def vpd_152_vpd_007_volume_spike_ratio_126_007_roc_5(vpd_007_volume_spike_ratio_126_007):
    feature = _s(vpd_007_volume_spike_ratio_126_007)
    return (_roc(feature, 5)).reindex(feature.index)

def vpd_153_vpd_013_volume_spike_ratio_1008_013_roc_42(vpd_013_volume_spike_ratio_1008_013):
    feature = _s(vpd_013_volume_spike_ratio_1008_013)
    return (_roc(feature, 42)).reindex(feature.index)

def vpd_154_vpd_019_volume_spike_ratio_42_019_roc_126(vpd_019_volume_spike_ratio_42_019):
    feature = _s(vpd_019_volume_spike_ratio_42_019)
    return (_roc(feature, 126)).reindex(feature.index)

def vpd_155_vpd_025_volume_spike_ratio_378_025_roc_378(vpd_025_volume_spike_ratio_378_025):
    feature = _s(vpd_025_volume_spike_ratio_378_025)
    return (_roc(feature, 378)).reindex(feature.index)






















VOLUME_PRICE_DIVERGENCE_REGISTRY_2ND_DERIVATIVES = {
    'vpd_151_vpd_001_volume_spike_ratio_5_001_roc_1': {'inputs': ['vpd_001_volume_spike_ratio_5_001'], 'func': vpd_151_vpd_001_volume_spike_ratio_5_001_roc_1},
    'vpd_152_vpd_007_volume_spike_ratio_126_007_roc_5': {'inputs': ['vpd_007_volume_spike_ratio_126_007'], 'func': vpd_152_vpd_007_volume_spike_ratio_126_007_roc_5},
    'vpd_153_vpd_013_volume_spike_ratio_1008_013_roc_42': {'inputs': ['vpd_013_volume_spike_ratio_1008_013'], 'func': vpd_153_vpd_013_volume_spike_ratio_1008_013_roc_42},
    'vpd_154_vpd_019_volume_spike_ratio_42_019_roc_126': {'inputs': ['vpd_019_volume_spike_ratio_42_019'], 'func': vpd_154_vpd_019_volume_spike_ratio_42_019_roc_126},
    'vpd_155_vpd_025_volume_spike_ratio_378_025_roc_378': {'inputs': ['vpd_025_volume_spike_ratio_378_025'], 'func': vpd_155_vpd_025_volume_spike_ratio_378_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def vpd_replacement_d2_001(vpd_replacement_001):
    feature = _clean(vpd_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_001'] = {'inputs': ['vpd_replacement_001'], 'func': vpd_replacement_d2_001}


def vpd_replacement_d2_002(vpd_replacement_002):
    feature = _clean(vpd_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_002'] = {'inputs': ['vpd_replacement_002'], 'func': vpd_replacement_d2_002}


def vpd_replacement_d2_003(vpd_replacement_003):
    feature = _clean(vpd_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_003'] = {'inputs': ['vpd_replacement_003'], 'func': vpd_replacement_d2_003}


def vpd_replacement_d2_004(vpd_replacement_004):
    feature = _clean(vpd_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_004'] = {'inputs': ['vpd_replacement_004'], 'func': vpd_replacement_d2_004}


def vpd_replacement_d2_005(vpd_replacement_005):
    feature = _clean(vpd_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_005'] = {'inputs': ['vpd_replacement_005'], 'func': vpd_replacement_d2_005}


def vpd_replacement_d2_006(vpd_replacement_006):
    feature = _clean(vpd_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_006'] = {'inputs': ['vpd_replacement_006'], 'func': vpd_replacement_d2_006}


def vpd_replacement_d2_007(vpd_replacement_007):
    feature = _clean(vpd_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_007'] = {'inputs': ['vpd_replacement_007'], 'func': vpd_replacement_d2_007}


def vpd_replacement_d2_008(vpd_replacement_008):
    feature = _clean(vpd_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_008'] = {'inputs': ['vpd_replacement_008'], 'func': vpd_replacement_d2_008}


def vpd_replacement_d2_009(vpd_replacement_009):
    feature = _clean(vpd_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_009'] = {'inputs': ['vpd_replacement_009'], 'func': vpd_replacement_d2_009}


def vpd_replacement_d2_010(vpd_replacement_010):
    feature = _clean(vpd_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_010'] = {'inputs': ['vpd_replacement_010'], 'func': vpd_replacement_d2_010}


def vpd_replacement_d2_011(vpd_replacement_011):
    feature = _clean(vpd_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_011'] = {'inputs': ['vpd_replacement_011'], 'func': vpd_replacement_d2_011}


def vpd_replacement_d2_012(vpd_replacement_012):
    feature = _clean(vpd_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_012'] = {'inputs': ['vpd_replacement_012'], 'func': vpd_replacement_d2_012}


def vpd_replacement_d2_013(vpd_replacement_013):
    feature = _clean(vpd_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_013'] = {'inputs': ['vpd_replacement_013'], 'func': vpd_replacement_d2_013}


def vpd_replacement_d2_014(vpd_replacement_014):
    feature = _clean(vpd_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_014'] = {'inputs': ['vpd_replacement_014'], 'func': vpd_replacement_d2_014}


def vpd_replacement_d2_015(vpd_replacement_015):
    feature = _clean(vpd_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_015'] = {'inputs': ['vpd_replacement_015'], 'func': vpd_replacement_d2_015}


def vpd_replacement_d2_016(vpd_replacement_016):
    feature = _clean(vpd_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_016'] = {'inputs': ['vpd_replacement_016'], 'func': vpd_replacement_d2_016}


def vpd_replacement_d2_017(vpd_replacement_017):
    feature = _clean(vpd_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_017'] = {'inputs': ['vpd_replacement_017'], 'func': vpd_replacement_d2_017}


def vpd_replacement_d2_018(vpd_replacement_018):
    feature = _clean(vpd_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_018'] = {'inputs': ['vpd_replacement_018'], 'func': vpd_replacement_d2_018}


def vpd_replacement_d2_019(vpd_replacement_019):
    feature = _clean(vpd_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_019'] = {'inputs': ['vpd_replacement_019'], 'func': vpd_replacement_d2_019}


def vpd_replacement_d2_020(vpd_replacement_020):
    feature = _clean(vpd_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_020'] = {'inputs': ['vpd_replacement_020'], 'func': vpd_replacement_d2_020}


def vpd_replacement_d2_021(vpd_replacement_021):
    feature = _clean(vpd_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_021'] = {'inputs': ['vpd_replacement_021'], 'func': vpd_replacement_d2_021}


def vpd_replacement_d2_022(vpd_replacement_022):
    feature = _clean(vpd_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_022'] = {'inputs': ['vpd_replacement_022'], 'func': vpd_replacement_d2_022}


def vpd_replacement_d2_023(vpd_replacement_023):
    feature = _clean(vpd_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_023'] = {'inputs': ['vpd_replacement_023'], 'func': vpd_replacement_d2_023}


def vpd_replacement_d2_024(vpd_replacement_024):
    feature = _clean(vpd_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_024'] = {'inputs': ['vpd_replacement_024'], 'func': vpd_replacement_d2_024}


def vpd_replacement_d2_025(vpd_replacement_025):
    feature = _clean(vpd_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_025'] = {'inputs': ['vpd_replacement_025'], 'func': vpd_replacement_d2_025}


def vpd_replacement_d2_026(vpd_replacement_026):
    feature = _clean(vpd_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_026'] = {'inputs': ['vpd_replacement_026'], 'func': vpd_replacement_d2_026}


def vpd_replacement_d2_027(vpd_replacement_027):
    feature = _clean(vpd_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_027'] = {'inputs': ['vpd_replacement_027'], 'func': vpd_replacement_d2_027}


def vpd_replacement_d2_028(vpd_replacement_028):
    feature = _clean(vpd_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_028'] = {'inputs': ['vpd_replacement_028'], 'func': vpd_replacement_d2_028}


def vpd_replacement_d2_029(vpd_replacement_029):
    feature = _clean(vpd_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_029'] = {'inputs': ['vpd_replacement_029'], 'func': vpd_replacement_d2_029}


def vpd_replacement_d2_030(vpd_replacement_030):
    feature = _clean(vpd_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_030'] = {'inputs': ['vpd_replacement_030'], 'func': vpd_replacement_d2_030}


def vpd_replacement_d2_031(vpd_replacement_031):
    feature = _clean(vpd_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_031'] = {'inputs': ['vpd_replacement_031'], 'func': vpd_replacement_d2_031}


def vpd_replacement_d2_032(vpd_replacement_032):
    feature = _clean(vpd_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_032'] = {'inputs': ['vpd_replacement_032'], 'func': vpd_replacement_d2_032}


def vpd_replacement_d2_033(vpd_replacement_033):
    feature = _clean(vpd_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_033'] = {'inputs': ['vpd_replacement_033'], 'func': vpd_replacement_d2_033}


def vpd_replacement_d2_034(vpd_replacement_034):
    feature = _clean(vpd_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_034'] = {'inputs': ['vpd_replacement_034'], 'func': vpd_replacement_d2_034}


def vpd_replacement_d2_035(vpd_replacement_035):
    feature = _clean(vpd_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_035'] = {'inputs': ['vpd_replacement_035'], 'func': vpd_replacement_d2_035}


def vpd_replacement_d2_036(vpd_replacement_036):
    feature = _clean(vpd_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_036'] = {'inputs': ['vpd_replacement_036'], 'func': vpd_replacement_d2_036}


def vpd_replacement_d2_037(vpd_replacement_037):
    feature = _clean(vpd_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_037'] = {'inputs': ['vpd_replacement_037'], 'func': vpd_replacement_d2_037}


def vpd_replacement_d2_038(vpd_replacement_038):
    feature = _clean(vpd_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_038'] = {'inputs': ['vpd_replacement_038'], 'func': vpd_replacement_d2_038}


def vpd_replacement_d2_039(vpd_replacement_039):
    feature = _clean(vpd_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_039'] = {'inputs': ['vpd_replacement_039'], 'func': vpd_replacement_d2_039}


def vpd_replacement_d2_040(vpd_replacement_040):
    feature = _clean(vpd_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_040'] = {'inputs': ['vpd_replacement_040'], 'func': vpd_replacement_d2_040}


def vpd_replacement_d2_041(vpd_replacement_041):
    feature = _clean(vpd_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_041'] = {'inputs': ['vpd_replacement_041'], 'func': vpd_replacement_d2_041}


def vpd_replacement_d2_042(vpd_replacement_042):
    feature = _clean(vpd_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_042'] = {'inputs': ['vpd_replacement_042'], 'func': vpd_replacement_d2_042}


def vpd_replacement_d2_043(vpd_replacement_043):
    feature = _clean(vpd_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_043'] = {'inputs': ['vpd_replacement_043'], 'func': vpd_replacement_d2_043}


def vpd_replacement_d2_044(vpd_replacement_044):
    feature = _clean(vpd_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_044'] = {'inputs': ['vpd_replacement_044'], 'func': vpd_replacement_d2_044}


def vpd_replacement_d2_045(vpd_replacement_045):
    feature = _clean(vpd_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_045'] = {'inputs': ['vpd_replacement_045'], 'func': vpd_replacement_d2_045}


def vpd_replacement_d2_046(vpd_replacement_046):
    feature = _clean(vpd_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_046'] = {'inputs': ['vpd_replacement_046'], 'func': vpd_replacement_d2_046}


def vpd_replacement_d2_047(vpd_replacement_047):
    feature = _clean(vpd_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_047'] = {'inputs': ['vpd_replacement_047'], 'func': vpd_replacement_d2_047}


def vpd_replacement_d2_048(vpd_replacement_048):
    feature = _clean(vpd_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_048'] = {'inputs': ['vpd_replacement_048'], 'func': vpd_replacement_d2_048}


def vpd_replacement_d2_049(vpd_replacement_049):
    feature = _clean(vpd_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_049'] = {'inputs': ['vpd_replacement_049'], 'func': vpd_replacement_d2_049}


def vpd_replacement_d2_050(vpd_replacement_050):
    feature = _clean(vpd_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_050'] = {'inputs': ['vpd_replacement_050'], 'func': vpd_replacement_d2_050}


def vpd_replacement_d2_051(vpd_replacement_051):
    feature = _clean(vpd_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_051'] = {'inputs': ['vpd_replacement_051'], 'func': vpd_replacement_d2_051}


def vpd_replacement_d2_052(vpd_replacement_052):
    feature = _clean(vpd_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_052'] = {'inputs': ['vpd_replacement_052'], 'func': vpd_replacement_d2_052}


def vpd_replacement_d2_053(vpd_replacement_053):
    feature = _clean(vpd_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_053'] = {'inputs': ['vpd_replacement_053'], 'func': vpd_replacement_d2_053}


def vpd_replacement_d2_054(vpd_replacement_054):
    feature = _clean(vpd_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_054'] = {'inputs': ['vpd_replacement_054'], 'func': vpd_replacement_d2_054}


def vpd_replacement_d2_055(vpd_replacement_055):
    feature = _clean(vpd_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_055'] = {'inputs': ['vpd_replacement_055'], 'func': vpd_replacement_d2_055}


def vpd_replacement_d2_056(vpd_replacement_056):
    feature = _clean(vpd_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_056'] = {'inputs': ['vpd_replacement_056'], 'func': vpd_replacement_d2_056}


def vpd_replacement_d2_057(vpd_replacement_057):
    feature = _clean(vpd_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_057'] = {'inputs': ['vpd_replacement_057'], 'func': vpd_replacement_d2_057}


def vpd_replacement_d2_058(vpd_replacement_058):
    feature = _clean(vpd_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_058'] = {'inputs': ['vpd_replacement_058'], 'func': vpd_replacement_d2_058}


def vpd_replacement_d2_059(vpd_replacement_059):
    feature = _clean(vpd_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_059'] = {'inputs': ['vpd_replacement_059'], 'func': vpd_replacement_d2_059}


def vpd_replacement_d2_060(vpd_replacement_060):
    feature = _clean(vpd_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_060'] = {'inputs': ['vpd_replacement_060'], 'func': vpd_replacement_d2_060}


def vpd_replacement_d2_061(vpd_replacement_061):
    feature = _clean(vpd_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_061'] = {'inputs': ['vpd_replacement_061'], 'func': vpd_replacement_d2_061}


def vpd_replacement_d2_062(vpd_replacement_062):
    feature = _clean(vpd_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_062'] = {'inputs': ['vpd_replacement_062'], 'func': vpd_replacement_d2_062}


def vpd_replacement_d2_063(vpd_replacement_063):
    feature = _clean(vpd_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_063'] = {'inputs': ['vpd_replacement_063'], 'func': vpd_replacement_d2_063}


def vpd_replacement_d2_064(vpd_replacement_064):
    feature = _clean(vpd_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_064'] = {'inputs': ['vpd_replacement_064'], 'func': vpd_replacement_d2_064}


def vpd_replacement_d2_065(vpd_replacement_065):
    feature = _clean(vpd_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_065'] = {'inputs': ['vpd_replacement_065'], 'func': vpd_replacement_d2_065}


def vpd_replacement_d2_066(vpd_replacement_066):
    feature = _clean(vpd_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_066'] = {'inputs': ['vpd_replacement_066'], 'func': vpd_replacement_d2_066}


def vpd_replacement_d2_067(vpd_replacement_067):
    feature = _clean(vpd_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_067'] = {'inputs': ['vpd_replacement_067'], 'func': vpd_replacement_d2_067}


def vpd_replacement_d2_068(vpd_replacement_068):
    feature = _clean(vpd_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_068'] = {'inputs': ['vpd_replacement_068'], 'func': vpd_replacement_d2_068}


def vpd_replacement_d2_069(vpd_replacement_069):
    feature = _clean(vpd_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_069'] = {'inputs': ['vpd_replacement_069'], 'func': vpd_replacement_d2_069}


def vpd_replacement_d2_070(vpd_replacement_070):
    feature = _clean(vpd_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_070'] = {'inputs': ['vpd_replacement_070'], 'func': vpd_replacement_d2_070}


def vpd_replacement_d2_071(vpd_replacement_071):
    feature = _clean(vpd_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_071'] = {'inputs': ['vpd_replacement_071'], 'func': vpd_replacement_d2_071}


def vpd_replacement_d2_072(vpd_replacement_072):
    feature = _clean(vpd_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_072'] = {'inputs': ['vpd_replacement_072'], 'func': vpd_replacement_d2_072}


def vpd_replacement_d2_073(vpd_replacement_073):
    feature = _clean(vpd_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_073'] = {'inputs': ['vpd_replacement_073'], 'func': vpd_replacement_d2_073}


def vpd_replacement_d2_074(vpd_replacement_074):
    feature = _clean(vpd_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_074'] = {'inputs': ['vpd_replacement_074'], 'func': vpd_replacement_d2_074}


def vpd_replacement_d2_075(vpd_replacement_075):
    feature = _clean(vpd_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_075'] = {'inputs': ['vpd_replacement_075'], 'func': vpd_replacement_d2_075}


def vpd_replacement_d2_076(vpd_replacement_076):
    feature = _clean(vpd_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_076'] = {'inputs': ['vpd_replacement_076'], 'func': vpd_replacement_d2_076}


def vpd_replacement_d2_077(vpd_replacement_077):
    feature = _clean(vpd_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_077'] = {'inputs': ['vpd_replacement_077'], 'func': vpd_replacement_d2_077}


def vpd_replacement_d2_078(vpd_replacement_078):
    feature = _clean(vpd_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_078'] = {'inputs': ['vpd_replacement_078'], 'func': vpd_replacement_d2_078}


def vpd_replacement_d2_079(vpd_replacement_079):
    feature = _clean(vpd_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_079'] = {'inputs': ['vpd_replacement_079'], 'func': vpd_replacement_d2_079}


def vpd_replacement_d2_080(vpd_replacement_080):
    feature = _clean(vpd_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_080'] = {'inputs': ['vpd_replacement_080'], 'func': vpd_replacement_d2_080}


def vpd_replacement_d2_081(vpd_replacement_081):
    feature = _clean(vpd_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_081'] = {'inputs': ['vpd_replacement_081'], 'func': vpd_replacement_d2_081}


def vpd_replacement_d2_082(vpd_replacement_082):
    feature = _clean(vpd_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_082'] = {'inputs': ['vpd_replacement_082'], 'func': vpd_replacement_d2_082}


def vpd_replacement_d2_083(vpd_replacement_083):
    feature = _clean(vpd_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_083'] = {'inputs': ['vpd_replacement_083'], 'func': vpd_replacement_d2_083}


def vpd_replacement_d2_084(vpd_replacement_084):
    feature = _clean(vpd_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_084'] = {'inputs': ['vpd_replacement_084'], 'func': vpd_replacement_d2_084}


def vpd_replacement_d2_085(vpd_replacement_085):
    feature = _clean(vpd_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_085'] = {'inputs': ['vpd_replacement_085'], 'func': vpd_replacement_d2_085}


def vpd_replacement_d2_086(vpd_replacement_086):
    feature = _clean(vpd_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_086'] = {'inputs': ['vpd_replacement_086'], 'func': vpd_replacement_d2_086}


def vpd_replacement_d2_087(vpd_replacement_087):
    feature = _clean(vpd_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_087'] = {'inputs': ['vpd_replacement_087'], 'func': vpd_replacement_d2_087}


def vpd_replacement_d2_088(vpd_replacement_088):
    feature = _clean(vpd_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_088'] = {'inputs': ['vpd_replacement_088'], 'func': vpd_replacement_d2_088}


def vpd_replacement_d2_089(vpd_replacement_089):
    feature = _clean(vpd_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_089'] = {'inputs': ['vpd_replacement_089'], 'func': vpd_replacement_d2_089}


def vpd_replacement_d2_090(vpd_replacement_090):
    feature = _clean(vpd_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_090'] = {'inputs': ['vpd_replacement_090'], 'func': vpd_replacement_d2_090}


def vpd_replacement_d2_091(vpd_replacement_091):
    feature = _clean(vpd_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_091'] = {'inputs': ['vpd_replacement_091'], 'func': vpd_replacement_d2_091}


def vpd_replacement_d2_092(vpd_replacement_092):
    feature = _clean(vpd_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_092'] = {'inputs': ['vpd_replacement_092'], 'func': vpd_replacement_d2_092}


def vpd_replacement_d2_093(vpd_replacement_093):
    feature = _clean(vpd_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_093'] = {'inputs': ['vpd_replacement_093'], 'func': vpd_replacement_d2_093}


def vpd_replacement_d2_094(vpd_replacement_094):
    feature = _clean(vpd_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_094'] = {'inputs': ['vpd_replacement_094'], 'func': vpd_replacement_d2_094}


def vpd_replacement_d2_095(vpd_replacement_095):
    feature = _clean(vpd_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_095'] = {'inputs': ['vpd_replacement_095'], 'func': vpd_replacement_d2_095}


def vpd_replacement_d2_096(vpd_replacement_096):
    feature = _clean(vpd_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_096'] = {'inputs': ['vpd_replacement_096'], 'func': vpd_replacement_d2_096}


def vpd_replacement_d2_097(vpd_replacement_097):
    feature = _clean(vpd_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_097'] = {'inputs': ['vpd_replacement_097'], 'func': vpd_replacement_d2_097}


def vpd_replacement_d2_098(vpd_replacement_098):
    feature = _clean(vpd_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_098'] = {'inputs': ['vpd_replacement_098'], 'func': vpd_replacement_d2_098}


def vpd_replacement_d2_099(vpd_replacement_099):
    feature = _clean(vpd_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_099'] = {'inputs': ['vpd_replacement_099'], 'func': vpd_replacement_d2_099}


def vpd_replacement_d2_100(vpd_replacement_100):
    feature = _clean(vpd_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_100'] = {'inputs': ['vpd_replacement_100'], 'func': vpd_replacement_d2_100}


def vpd_replacement_d2_101(vpd_replacement_101):
    feature = _clean(vpd_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_101'] = {'inputs': ['vpd_replacement_101'], 'func': vpd_replacement_d2_101}


def vpd_replacement_d2_102(vpd_replacement_102):
    feature = _clean(vpd_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_102'] = {'inputs': ['vpd_replacement_102'], 'func': vpd_replacement_d2_102}


def vpd_replacement_d2_103(vpd_replacement_103):
    feature = _clean(vpd_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_103'] = {'inputs': ['vpd_replacement_103'], 'func': vpd_replacement_d2_103}


def vpd_replacement_d2_104(vpd_replacement_104):
    feature = _clean(vpd_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_104'] = {'inputs': ['vpd_replacement_104'], 'func': vpd_replacement_d2_104}


def vpd_replacement_d2_105(vpd_replacement_105):
    feature = _clean(vpd_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_105'] = {'inputs': ['vpd_replacement_105'], 'func': vpd_replacement_d2_105}


def vpd_replacement_d2_106(vpd_replacement_106):
    feature = _clean(vpd_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_106'] = {'inputs': ['vpd_replacement_106'], 'func': vpd_replacement_d2_106}


def vpd_replacement_d2_107(vpd_replacement_107):
    feature = _clean(vpd_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_107'] = {'inputs': ['vpd_replacement_107'], 'func': vpd_replacement_d2_107}


def vpd_replacement_d2_108(vpd_replacement_108):
    feature = _clean(vpd_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_108'] = {'inputs': ['vpd_replacement_108'], 'func': vpd_replacement_d2_108}


def vpd_replacement_d2_109(vpd_replacement_109):
    feature = _clean(vpd_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_109'] = {'inputs': ['vpd_replacement_109'], 'func': vpd_replacement_d2_109}


def vpd_replacement_d2_110(vpd_replacement_110):
    feature = _clean(vpd_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_110'] = {'inputs': ['vpd_replacement_110'], 'func': vpd_replacement_d2_110}


def vpd_replacement_d2_111(vpd_replacement_111):
    feature = _clean(vpd_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_111'] = {'inputs': ['vpd_replacement_111'], 'func': vpd_replacement_d2_111}


def vpd_replacement_d2_112(vpd_replacement_112):
    feature = _clean(vpd_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_112'] = {'inputs': ['vpd_replacement_112'], 'func': vpd_replacement_d2_112}


def vpd_replacement_d2_113(vpd_replacement_113):
    feature = _clean(vpd_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_113'] = {'inputs': ['vpd_replacement_113'], 'func': vpd_replacement_d2_113}


def vpd_replacement_d2_114(vpd_replacement_114):
    feature = _clean(vpd_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_114'] = {'inputs': ['vpd_replacement_114'], 'func': vpd_replacement_d2_114}


def vpd_replacement_d2_115(vpd_replacement_115):
    feature = _clean(vpd_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_115'] = {'inputs': ['vpd_replacement_115'], 'func': vpd_replacement_d2_115}


def vpd_replacement_d2_116(vpd_replacement_116):
    feature = _clean(vpd_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_116'] = {'inputs': ['vpd_replacement_116'], 'func': vpd_replacement_d2_116}


def vpd_replacement_d2_117(vpd_replacement_117):
    feature = _clean(vpd_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_117'] = {'inputs': ['vpd_replacement_117'], 'func': vpd_replacement_d2_117}


def vpd_replacement_d2_118(vpd_replacement_118):
    feature = _clean(vpd_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_118'] = {'inputs': ['vpd_replacement_118'], 'func': vpd_replacement_d2_118}


def vpd_replacement_d2_119(vpd_replacement_119):
    feature = _clean(vpd_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_119'] = {'inputs': ['vpd_replacement_119'], 'func': vpd_replacement_d2_119}


def vpd_replacement_d2_120(vpd_replacement_120):
    feature = _clean(vpd_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_120'] = {'inputs': ['vpd_replacement_120'], 'func': vpd_replacement_d2_120}


def vpd_replacement_d2_121(vpd_replacement_121):
    feature = _clean(vpd_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_121'] = {'inputs': ['vpd_replacement_121'], 'func': vpd_replacement_d2_121}


def vpd_replacement_d2_122(vpd_replacement_122):
    feature = _clean(vpd_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_122'] = {'inputs': ['vpd_replacement_122'], 'func': vpd_replacement_d2_122}


def vpd_replacement_d2_123(vpd_replacement_123):
    feature = _clean(vpd_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_123'] = {'inputs': ['vpd_replacement_123'], 'func': vpd_replacement_d2_123}


def vpd_replacement_d2_124(vpd_replacement_124):
    feature = _clean(vpd_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_124'] = {'inputs': ['vpd_replacement_124'], 'func': vpd_replacement_d2_124}


def vpd_replacement_d2_125(vpd_replacement_125):
    feature = _clean(vpd_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_125'] = {'inputs': ['vpd_replacement_125'], 'func': vpd_replacement_d2_125}


def vpd_replacement_d2_126(vpd_replacement_126):
    feature = _clean(vpd_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_126'] = {'inputs': ['vpd_replacement_126'], 'func': vpd_replacement_d2_126}


def vpd_replacement_d2_127(vpd_replacement_127):
    feature = _clean(vpd_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_127'] = {'inputs': ['vpd_replacement_127'], 'func': vpd_replacement_d2_127}


def vpd_replacement_d2_128(vpd_replacement_128):
    feature = _clean(vpd_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_128'] = {'inputs': ['vpd_replacement_128'], 'func': vpd_replacement_d2_128}


def vpd_replacement_d2_129(vpd_replacement_129):
    feature = _clean(vpd_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_129'] = {'inputs': ['vpd_replacement_129'], 'func': vpd_replacement_d2_129}


def vpd_replacement_d2_130(vpd_replacement_130):
    feature = _clean(vpd_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_130'] = {'inputs': ['vpd_replacement_130'], 'func': vpd_replacement_d2_130}


def vpd_replacement_d2_131(vpd_replacement_131):
    feature = _clean(vpd_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_131'] = {'inputs': ['vpd_replacement_131'], 'func': vpd_replacement_d2_131}


def vpd_replacement_d2_132(vpd_replacement_132):
    feature = _clean(vpd_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_132'] = {'inputs': ['vpd_replacement_132'], 'func': vpd_replacement_d2_132}


def vpd_replacement_d2_133(vpd_replacement_133):
    feature = _clean(vpd_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_133'] = {'inputs': ['vpd_replacement_133'], 'func': vpd_replacement_d2_133}


def vpd_replacement_d2_134(vpd_replacement_134):
    feature = _clean(vpd_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_134'] = {'inputs': ['vpd_replacement_134'], 'func': vpd_replacement_d2_134}


def vpd_replacement_d2_135(vpd_replacement_135):
    feature = _clean(vpd_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_135'] = {'inputs': ['vpd_replacement_135'], 'func': vpd_replacement_d2_135}


def vpd_replacement_d2_136(vpd_replacement_136):
    feature = _clean(vpd_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_136'] = {'inputs': ['vpd_replacement_136'], 'func': vpd_replacement_d2_136}


def vpd_replacement_d2_137(vpd_replacement_137):
    feature = _clean(vpd_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_137'] = {'inputs': ['vpd_replacement_137'], 'func': vpd_replacement_d2_137}


def vpd_replacement_d2_138(vpd_replacement_138):
    feature = _clean(vpd_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_138'] = {'inputs': ['vpd_replacement_138'], 'func': vpd_replacement_d2_138}


def vpd_replacement_d2_139(vpd_replacement_139):
    feature = _clean(vpd_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_139'] = {'inputs': ['vpd_replacement_139'], 'func': vpd_replacement_d2_139}


def vpd_replacement_d2_140(vpd_replacement_140):
    feature = _clean(vpd_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_140'] = {'inputs': ['vpd_replacement_140'], 'func': vpd_replacement_d2_140}


def vpd_replacement_d2_141(vpd_replacement_141):
    feature = _clean(vpd_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_141'] = {'inputs': ['vpd_replacement_141'], 'func': vpd_replacement_d2_141}


def vpd_replacement_d2_142(vpd_replacement_142):
    feature = _clean(vpd_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_142'] = {'inputs': ['vpd_replacement_142'], 'func': vpd_replacement_d2_142}


def vpd_replacement_d2_143(vpd_replacement_143):
    feature = _clean(vpd_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_143'] = {'inputs': ['vpd_replacement_143'], 'func': vpd_replacement_d2_143}


def vpd_replacement_d2_144(vpd_replacement_144):
    feature = _clean(vpd_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_144'] = {'inputs': ['vpd_replacement_144'], 'func': vpd_replacement_d2_144}


def vpd_replacement_d2_145(vpd_replacement_145):
    feature = _clean(vpd_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_145'] = {'inputs': ['vpd_replacement_145'], 'func': vpd_replacement_d2_145}


def vpd_replacement_d2_146(vpd_replacement_146):
    feature = _clean(vpd_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_146'] = {'inputs': ['vpd_replacement_146'], 'func': vpd_replacement_d2_146}


def vpd_replacement_d2_147(vpd_replacement_147):
    feature = _clean(vpd_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_147'] = {'inputs': ['vpd_replacement_147'], 'func': vpd_replacement_d2_147}


def vpd_replacement_d2_148(vpd_replacement_148):
    feature = _clean(vpd_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_148'] = {'inputs': ['vpd_replacement_148'], 'func': vpd_replacement_d2_148}


def vpd_replacement_d2_149(vpd_replacement_149):
    feature = _clean(vpd_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_149'] = {'inputs': ['vpd_replacement_149'], 'func': vpd_replacement_d2_149}


def vpd_replacement_d2_150(vpd_replacement_150):
    feature = _clean(vpd_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_150'] = {'inputs': ['vpd_replacement_150'], 'func': vpd_replacement_d2_150}


def vpd_replacement_d2_151(vpd_replacement_151):
    feature = _clean(vpd_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_151'] = {'inputs': ['vpd_replacement_151'], 'func': vpd_replacement_d2_151}


def vpd_replacement_d2_152(vpd_replacement_152):
    feature = _clean(vpd_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_152'] = {'inputs': ['vpd_replacement_152'], 'func': vpd_replacement_d2_152}


def vpd_replacement_d2_153(vpd_replacement_153):
    feature = _clean(vpd_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_153'] = {'inputs': ['vpd_replacement_153'], 'func': vpd_replacement_d2_153}


def vpd_replacement_d2_154(vpd_replacement_154):
    feature = _clean(vpd_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_154'] = {'inputs': ['vpd_replacement_154'], 'func': vpd_replacement_d2_154}


def vpd_replacement_d2_155(vpd_replacement_155):
    feature = _clean(vpd_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_155'] = {'inputs': ['vpd_replacement_155'], 'func': vpd_replacement_d2_155}


def vpd_replacement_d2_156(vpd_replacement_156):
    feature = _clean(vpd_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_156'] = {'inputs': ['vpd_replacement_156'], 'func': vpd_replacement_d2_156}


def vpd_replacement_d2_157(vpd_replacement_157):
    feature = _clean(vpd_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_157'] = {'inputs': ['vpd_replacement_157'], 'func': vpd_replacement_d2_157}


def vpd_replacement_d2_158(vpd_replacement_158):
    feature = _clean(vpd_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_158'] = {'inputs': ['vpd_replacement_158'], 'func': vpd_replacement_d2_158}


def vpd_replacement_d2_159(vpd_replacement_159):
    feature = _clean(vpd_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_159'] = {'inputs': ['vpd_replacement_159'], 'func': vpd_replacement_d2_159}


def vpd_replacement_d2_160(vpd_replacement_160):
    feature = _clean(vpd_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
VPD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vpd_replacement_d2_160'] = {'inputs': ['vpd_replacement_160'], 'func': vpd_replacement_d2_160}


# Base-universe derivative extensions for repaired first-base features.
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def vpd_base_universe_d2_001_vpd_002_volume_zscore_10_002(vpd_002_volume_zscore_10_002):
    return _base_universe_d2(vpd_002_volume_zscore_10_002, 1)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_001_vpd_002_volume_zscore_10_002'] = {'inputs': ['vpd_002_volume_zscore_10_002'], 'func': vpd_base_universe_d2_001_vpd_002_volume_zscore_10_002}


def vpd_base_universe_d2_002_vpd_003_down_volume_share_21_003(vpd_003_down_volume_share_21_003):
    return _base_universe_d2(vpd_003_down_volume_share_21_003, 2)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_002_vpd_003_down_volume_share_21_003'] = {'inputs': ['vpd_003_down_volume_share_21_003'], 'func': vpd_base_universe_d2_002_vpd_003_down_volume_share_21_003}


def vpd_base_universe_d2_003_vpd_004_dollar_volume_shock_42_004(vpd_004_dollar_volume_shock_42_004):
    return _base_universe_d2(vpd_004_dollar_volume_shock_42_004, 3)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_003_vpd_004_dollar_volume_shock_42_004'] = {'inputs': ['vpd_004_dollar_volume_shock_42_004'], 'func': vpd_base_universe_d2_003_vpd_004_dollar_volume_shock_42_004}


def vpd_base_universe_d2_004_vpd_005_volume_trend_slope_63_005(vpd_005_volume_trend_slope_63_005):
    return _base_universe_d2(vpd_005_volume_trend_slope_63_005, 4)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_004_vpd_005_volume_trend_slope_63_005'] = {'inputs': ['vpd_005_volume_trend_slope_63_005'], 'func': vpd_base_universe_d2_004_vpd_005_volume_trend_slope_63_005}


def vpd_base_universe_d2_005_vpd_006_price_volume_divergence_84_006(vpd_006_price_volume_divergence_84_006):
    return _base_universe_d2(vpd_006_price_volume_divergence_84_006, 5)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_005_vpd_006_price_volume_divergence_84_006'] = {'inputs': ['vpd_006_price_volume_divergence_84_006'], 'func': vpd_base_universe_d2_005_vpd_006_price_volume_divergence_84_006}


def vpd_base_universe_d2_006_vpd_008_volume_zscore_189_008(vpd_008_volume_zscore_189_008):
    return _base_universe_d2(vpd_008_volume_zscore_189_008, 6)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_006_vpd_008_volume_zscore_189_008'] = {'inputs': ['vpd_008_volume_zscore_189_008'], 'func': vpd_base_universe_d2_006_vpd_008_volume_zscore_189_008}


def vpd_base_universe_d2_007_vpd_009_down_volume_share_252_009(vpd_009_down_volume_share_252_009):
    return _base_universe_d2(vpd_009_down_volume_share_252_009, 7)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_007_vpd_009_down_volume_share_252_009'] = {'inputs': ['vpd_009_down_volume_share_252_009'], 'func': vpd_base_universe_d2_007_vpd_009_down_volume_share_252_009}


def vpd_base_universe_d2_008_vpd_010_dollar_volume_shock_378_010(vpd_010_dollar_volume_shock_378_010):
    return _base_universe_d2(vpd_010_dollar_volume_shock_378_010, 8)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_008_vpd_010_dollar_volume_shock_378_010'] = {'inputs': ['vpd_010_dollar_volume_shock_378_010'], 'func': vpd_base_universe_d2_008_vpd_010_dollar_volume_shock_378_010}


def vpd_base_universe_d2_009_vpd_011_volume_trend_slope_504_011(vpd_011_volume_trend_slope_504_011):
    return _base_universe_d2(vpd_011_volume_trend_slope_504_011, 9)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_009_vpd_011_volume_trend_slope_504_011'] = {'inputs': ['vpd_011_volume_trend_slope_504_011'], 'func': vpd_base_universe_d2_009_vpd_011_volume_trend_slope_504_011}


def vpd_base_universe_d2_010_vpd_012_price_volume_divergence_756_012(vpd_012_price_volume_divergence_756_012):
    return _base_universe_d2(vpd_012_price_volume_divergence_756_012, 10)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_010_vpd_012_price_volume_divergence_756_012'] = {'inputs': ['vpd_012_price_volume_divergence_756_012'], 'func': vpd_base_universe_d2_010_vpd_012_price_volume_divergence_756_012}


def vpd_base_universe_d2_011_vpd_014_volume_zscore_1260_014(vpd_014_volume_zscore_1260_014):
    return _base_universe_d2(vpd_014_volume_zscore_1260_014, 11)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_011_vpd_014_volume_zscore_1260_014'] = {'inputs': ['vpd_014_volume_zscore_1260_014'], 'func': vpd_base_universe_d2_011_vpd_014_volume_zscore_1260_014}


def vpd_base_universe_d2_012_vpd_015_down_volume_share_1512_015(vpd_015_down_volume_share_1512_015):
    return _base_universe_d2(vpd_015_down_volume_share_1512_015, 12)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_012_vpd_015_down_volume_share_1512_015'] = {'inputs': ['vpd_015_down_volume_share_1512_015'], 'func': vpd_base_universe_d2_012_vpd_015_down_volume_share_1512_015}


def vpd_base_universe_d2_013_vpd_016_dollar_volume_shock_5_016(vpd_016_dollar_volume_shock_5_016):
    return _base_universe_d2(vpd_016_dollar_volume_shock_5_016, 13)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_013_vpd_016_dollar_volume_shock_5_016'] = {'inputs': ['vpd_016_dollar_volume_shock_5_016'], 'func': vpd_base_universe_d2_013_vpd_016_dollar_volume_shock_5_016}


def vpd_base_universe_d2_014_vpd_017_volume_trend_slope_10_017(vpd_017_volume_trend_slope_10_017):
    return _base_universe_d2(vpd_017_volume_trend_slope_10_017, 14)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_014_vpd_017_volume_trend_slope_10_017'] = {'inputs': ['vpd_017_volume_trend_slope_10_017'], 'func': vpd_base_universe_d2_014_vpd_017_volume_trend_slope_10_017}


def vpd_base_universe_d2_015_vpd_018_price_volume_divergence_21_018(vpd_018_price_volume_divergence_21_018):
    return _base_universe_d2(vpd_018_price_volume_divergence_21_018, 15)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_015_vpd_018_price_volume_divergence_21_018'] = {'inputs': ['vpd_018_price_volume_divergence_21_018'], 'func': vpd_base_universe_d2_015_vpd_018_price_volume_divergence_21_018}


def vpd_base_universe_d2_016_vpd_020_volume_zscore_63_020(vpd_020_volume_zscore_63_020):
    return _base_universe_d2(vpd_020_volume_zscore_63_020, 16)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_016_vpd_020_volume_zscore_63_020'] = {'inputs': ['vpd_020_volume_zscore_63_020'], 'func': vpd_base_universe_d2_016_vpd_020_volume_zscore_63_020}


def vpd_base_universe_d2_017_vpd_021_down_volume_share_84_021(vpd_021_down_volume_share_84_021):
    return _base_universe_d2(vpd_021_down_volume_share_84_021, 17)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_017_vpd_021_down_volume_share_84_021'] = {'inputs': ['vpd_021_down_volume_share_84_021'], 'func': vpd_base_universe_d2_017_vpd_021_down_volume_share_84_021}


def vpd_base_universe_d2_018_vpd_022_dollar_volume_shock_126_022(vpd_022_dollar_volume_shock_126_022):
    return _base_universe_d2(vpd_022_dollar_volume_shock_126_022, 18)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_018_vpd_022_dollar_volume_shock_126_022'] = {'inputs': ['vpd_022_dollar_volume_shock_126_022'], 'func': vpd_base_universe_d2_018_vpd_022_dollar_volume_shock_126_022}


def vpd_base_universe_d2_019_vpd_023_volume_trend_slope_189_023(vpd_023_volume_trend_slope_189_023):
    return _base_universe_d2(vpd_023_volume_trend_slope_189_023, 19)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_019_vpd_023_volume_trend_slope_189_023'] = {'inputs': ['vpd_023_volume_trend_slope_189_023'], 'func': vpd_base_universe_d2_019_vpd_023_volume_trend_slope_189_023}


def vpd_base_universe_d2_020_vpd_024_price_volume_divergence_252_024(vpd_024_price_volume_divergence_252_024):
    return _base_universe_d2(vpd_024_price_volume_divergence_252_024, 20)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_020_vpd_024_price_volume_divergence_252_024'] = {'inputs': ['vpd_024_price_volume_divergence_252_024'], 'func': vpd_base_universe_d2_020_vpd_024_price_volume_divergence_252_024}


def vpd_base_universe_d2_021_vpd_026_volume_zscore_504_026(vpd_026_volume_zscore_504_026):
    return _base_universe_d2(vpd_026_volume_zscore_504_026, 21)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_021_vpd_026_volume_zscore_504_026'] = {'inputs': ['vpd_026_volume_zscore_504_026'], 'func': vpd_base_universe_d2_021_vpd_026_volume_zscore_504_026}


def vpd_base_universe_d2_022_vpd_027_down_volume_share_756_027(vpd_027_down_volume_share_756_027):
    return _base_universe_d2(vpd_027_down_volume_share_756_027, 22)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_022_vpd_027_down_volume_share_756_027'] = {'inputs': ['vpd_027_down_volume_share_756_027'], 'func': vpd_base_universe_d2_022_vpd_027_down_volume_share_756_027}


def vpd_base_universe_d2_023_vpd_028_dollar_volume_shock_1008_028(vpd_028_dollar_volume_shock_1008_028):
    return _base_universe_d2(vpd_028_dollar_volume_shock_1008_028, 23)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_023_vpd_028_dollar_volume_shock_1008_028'] = {'inputs': ['vpd_028_dollar_volume_shock_1008_028'], 'func': vpd_base_universe_d2_023_vpd_028_dollar_volume_shock_1008_028}


def vpd_base_universe_d2_024_vpd_029_volume_trend_slope_1260_029(vpd_029_volume_trend_slope_1260_029):
    return _base_universe_d2(vpd_029_volume_trend_slope_1260_029, 24)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_024_vpd_029_volume_trend_slope_1260_029'] = {'inputs': ['vpd_029_volume_trend_slope_1260_029'], 'func': vpd_base_universe_d2_024_vpd_029_volume_trend_slope_1260_029}


def vpd_base_universe_d2_025_vpd_030_price_volume_divergence_1512_030(vpd_030_price_volume_divergence_1512_030):
    return _base_universe_d2(vpd_030_price_volume_divergence_1512_030, 25)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_025_vpd_030_price_volume_divergence_1512_030'] = {'inputs': ['vpd_030_price_volume_divergence_1512_030'], 'func': vpd_base_universe_d2_025_vpd_030_price_volume_divergence_1512_030}


def vpd_base_universe_d2_026_vpd_basefill_031(vpd_basefill_031):
    return _base_universe_d2(vpd_basefill_031, 26)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_026_vpd_basefill_031'] = {'inputs': ['vpd_basefill_031'], 'func': vpd_base_universe_d2_026_vpd_basefill_031}


def vpd_base_universe_d2_027_vpd_basefill_032(vpd_basefill_032):
    return _base_universe_d2(vpd_basefill_032, 27)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_027_vpd_basefill_032'] = {'inputs': ['vpd_basefill_032'], 'func': vpd_base_universe_d2_027_vpd_basefill_032}


def vpd_base_universe_d2_028_vpd_basefill_033(vpd_basefill_033):
    return _base_universe_d2(vpd_basefill_033, 28)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_028_vpd_basefill_033'] = {'inputs': ['vpd_basefill_033'], 'func': vpd_base_universe_d2_028_vpd_basefill_033}


def vpd_base_universe_d2_029_vpd_basefill_034(vpd_basefill_034):
    return _base_universe_d2(vpd_basefill_034, 29)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_029_vpd_basefill_034'] = {'inputs': ['vpd_basefill_034'], 'func': vpd_base_universe_d2_029_vpd_basefill_034}


def vpd_base_universe_d2_030_vpd_basefill_035(vpd_basefill_035):
    return _base_universe_d2(vpd_basefill_035, 30)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_030_vpd_basefill_035'] = {'inputs': ['vpd_basefill_035'], 'func': vpd_base_universe_d2_030_vpd_basefill_035}


def vpd_base_universe_d2_031_vpd_basefill_036(vpd_basefill_036):
    return _base_universe_d2(vpd_basefill_036, 31)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_031_vpd_basefill_036'] = {'inputs': ['vpd_basefill_036'], 'func': vpd_base_universe_d2_031_vpd_basefill_036}


def vpd_base_universe_d2_032_vpd_basefill_037(vpd_basefill_037):
    return _base_universe_d2(vpd_basefill_037, 32)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_032_vpd_basefill_037'] = {'inputs': ['vpd_basefill_037'], 'func': vpd_base_universe_d2_032_vpd_basefill_037}


def vpd_base_universe_d2_033_vpd_basefill_038(vpd_basefill_038):
    return _base_universe_d2(vpd_basefill_038, 33)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_033_vpd_basefill_038'] = {'inputs': ['vpd_basefill_038'], 'func': vpd_base_universe_d2_033_vpd_basefill_038}


def vpd_base_universe_d2_034_vpd_basefill_039(vpd_basefill_039):
    return _base_universe_d2(vpd_basefill_039, 34)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_034_vpd_basefill_039'] = {'inputs': ['vpd_basefill_039'], 'func': vpd_base_universe_d2_034_vpd_basefill_039}


def vpd_base_universe_d2_035_vpd_basefill_040(vpd_basefill_040):
    return _base_universe_d2(vpd_basefill_040, 35)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_035_vpd_basefill_040'] = {'inputs': ['vpd_basefill_040'], 'func': vpd_base_universe_d2_035_vpd_basefill_040}


def vpd_base_universe_d2_036_vpd_basefill_041(vpd_basefill_041):
    return _base_universe_d2(vpd_basefill_041, 36)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_036_vpd_basefill_041'] = {'inputs': ['vpd_basefill_041'], 'func': vpd_base_universe_d2_036_vpd_basefill_041}


def vpd_base_universe_d2_037_vpd_basefill_042(vpd_basefill_042):
    return _base_universe_d2(vpd_basefill_042, 37)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_037_vpd_basefill_042'] = {'inputs': ['vpd_basefill_042'], 'func': vpd_base_universe_d2_037_vpd_basefill_042}


def vpd_base_universe_d2_038_vpd_basefill_043(vpd_basefill_043):
    return _base_universe_d2(vpd_basefill_043, 38)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_038_vpd_basefill_043'] = {'inputs': ['vpd_basefill_043'], 'func': vpd_base_universe_d2_038_vpd_basefill_043}


def vpd_base_universe_d2_039_vpd_basefill_044(vpd_basefill_044):
    return _base_universe_d2(vpd_basefill_044, 39)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_039_vpd_basefill_044'] = {'inputs': ['vpd_basefill_044'], 'func': vpd_base_universe_d2_039_vpd_basefill_044}


def vpd_base_universe_d2_040_vpd_basefill_045(vpd_basefill_045):
    return _base_universe_d2(vpd_basefill_045, 40)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_040_vpd_basefill_045'] = {'inputs': ['vpd_basefill_045'], 'func': vpd_base_universe_d2_040_vpd_basefill_045}


def vpd_base_universe_d2_041_vpd_basefill_046(vpd_basefill_046):
    return _base_universe_d2(vpd_basefill_046, 41)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_041_vpd_basefill_046'] = {'inputs': ['vpd_basefill_046'], 'func': vpd_base_universe_d2_041_vpd_basefill_046}


def vpd_base_universe_d2_042_vpd_basefill_047(vpd_basefill_047):
    return _base_universe_d2(vpd_basefill_047, 42)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_042_vpd_basefill_047'] = {'inputs': ['vpd_basefill_047'], 'func': vpd_base_universe_d2_042_vpd_basefill_047}


def vpd_base_universe_d2_043_vpd_basefill_048(vpd_basefill_048):
    return _base_universe_d2(vpd_basefill_048, 43)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_043_vpd_basefill_048'] = {'inputs': ['vpd_basefill_048'], 'func': vpd_base_universe_d2_043_vpd_basefill_048}


def vpd_base_universe_d2_044_vpd_basefill_049(vpd_basefill_049):
    return _base_universe_d2(vpd_basefill_049, 44)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_044_vpd_basefill_049'] = {'inputs': ['vpd_basefill_049'], 'func': vpd_base_universe_d2_044_vpd_basefill_049}


def vpd_base_universe_d2_045_vpd_basefill_050(vpd_basefill_050):
    return _base_universe_d2(vpd_basefill_050, 45)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_045_vpd_basefill_050'] = {'inputs': ['vpd_basefill_050'], 'func': vpd_base_universe_d2_045_vpd_basefill_050}


def vpd_base_universe_d2_046_vpd_basefill_051(vpd_basefill_051):
    return _base_universe_d2(vpd_basefill_051, 46)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_046_vpd_basefill_051'] = {'inputs': ['vpd_basefill_051'], 'func': vpd_base_universe_d2_046_vpd_basefill_051}


def vpd_base_universe_d2_047_vpd_basefill_052(vpd_basefill_052):
    return _base_universe_d2(vpd_basefill_052, 47)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_047_vpd_basefill_052'] = {'inputs': ['vpd_basefill_052'], 'func': vpd_base_universe_d2_047_vpd_basefill_052}


def vpd_base_universe_d2_048_vpd_basefill_053(vpd_basefill_053):
    return _base_universe_d2(vpd_basefill_053, 48)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_048_vpd_basefill_053'] = {'inputs': ['vpd_basefill_053'], 'func': vpd_base_universe_d2_048_vpd_basefill_053}


def vpd_base_universe_d2_049_vpd_basefill_054(vpd_basefill_054):
    return _base_universe_d2(vpd_basefill_054, 49)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_049_vpd_basefill_054'] = {'inputs': ['vpd_basefill_054'], 'func': vpd_base_universe_d2_049_vpd_basefill_054}


def vpd_base_universe_d2_050_vpd_basefill_055(vpd_basefill_055):
    return _base_universe_d2(vpd_basefill_055, 50)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_050_vpd_basefill_055'] = {'inputs': ['vpd_basefill_055'], 'func': vpd_base_universe_d2_050_vpd_basefill_055}


def vpd_base_universe_d2_051_vpd_basefill_056(vpd_basefill_056):
    return _base_universe_d2(vpd_basefill_056, 51)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_051_vpd_basefill_056'] = {'inputs': ['vpd_basefill_056'], 'func': vpd_base_universe_d2_051_vpd_basefill_056}


def vpd_base_universe_d2_052_vpd_basefill_057(vpd_basefill_057):
    return _base_universe_d2(vpd_basefill_057, 52)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_052_vpd_basefill_057'] = {'inputs': ['vpd_basefill_057'], 'func': vpd_base_universe_d2_052_vpd_basefill_057}


def vpd_base_universe_d2_053_vpd_basefill_058(vpd_basefill_058):
    return _base_universe_d2(vpd_basefill_058, 53)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_053_vpd_basefill_058'] = {'inputs': ['vpd_basefill_058'], 'func': vpd_base_universe_d2_053_vpd_basefill_058}


def vpd_base_universe_d2_054_vpd_basefill_059(vpd_basefill_059):
    return _base_universe_d2(vpd_basefill_059, 54)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_054_vpd_basefill_059'] = {'inputs': ['vpd_basefill_059'], 'func': vpd_base_universe_d2_054_vpd_basefill_059}


def vpd_base_universe_d2_055_vpd_basefill_060(vpd_basefill_060):
    return _base_universe_d2(vpd_basefill_060, 55)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_055_vpd_basefill_060'] = {'inputs': ['vpd_basefill_060'], 'func': vpd_base_universe_d2_055_vpd_basefill_060}


def vpd_base_universe_d2_056_vpd_basefill_061(vpd_basefill_061):
    return _base_universe_d2(vpd_basefill_061, 56)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_056_vpd_basefill_061'] = {'inputs': ['vpd_basefill_061'], 'func': vpd_base_universe_d2_056_vpd_basefill_061}


def vpd_base_universe_d2_057_vpd_basefill_062(vpd_basefill_062):
    return _base_universe_d2(vpd_basefill_062, 57)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_057_vpd_basefill_062'] = {'inputs': ['vpd_basefill_062'], 'func': vpd_base_universe_d2_057_vpd_basefill_062}


def vpd_base_universe_d2_058_vpd_basefill_063(vpd_basefill_063):
    return _base_universe_d2(vpd_basefill_063, 58)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_058_vpd_basefill_063'] = {'inputs': ['vpd_basefill_063'], 'func': vpd_base_universe_d2_058_vpd_basefill_063}


def vpd_base_universe_d2_059_vpd_basefill_064(vpd_basefill_064):
    return _base_universe_d2(vpd_basefill_064, 59)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_059_vpd_basefill_064'] = {'inputs': ['vpd_basefill_064'], 'func': vpd_base_universe_d2_059_vpd_basefill_064}


def vpd_base_universe_d2_060_vpd_basefill_065(vpd_basefill_065):
    return _base_universe_d2(vpd_basefill_065, 60)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_060_vpd_basefill_065'] = {'inputs': ['vpd_basefill_065'], 'func': vpd_base_universe_d2_060_vpd_basefill_065}


def vpd_base_universe_d2_061_vpd_basefill_066(vpd_basefill_066):
    return _base_universe_d2(vpd_basefill_066, 61)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_061_vpd_basefill_066'] = {'inputs': ['vpd_basefill_066'], 'func': vpd_base_universe_d2_061_vpd_basefill_066}


def vpd_base_universe_d2_062_vpd_basefill_067(vpd_basefill_067):
    return _base_universe_d2(vpd_basefill_067, 62)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_062_vpd_basefill_067'] = {'inputs': ['vpd_basefill_067'], 'func': vpd_base_universe_d2_062_vpd_basefill_067}


def vpd_base_universe_d2_063_vpd_basefill_068(vpd_basefill_068):
    return _base_universe_d2(vpd_basefill_068, 63)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_063_vpd_basefill_068'] = {'inputs': ['vpd_basefill_068'], 'func': vpd_base_universe_d2_063_vpd_basefill_068}


def vpd_base_universe_d2_064_vpd_basefill_069(vpd_basefill_069):
    return _base_universe_d2(vpd_basefill_069, 64)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_064_vpd_basefill_069'] = {'inputs': ['vpd_basefill_069'], 'func': vpd_base_universe_d2_064_vpd_basefill_069}


def vpd_base_universe_d2_065_vpd_basefill_070(vpd_basefill_070):
    return _base_universe_d2(vpd_basefill_070, 65)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_065_vpd_basefill_070'] = {'inputs': ['vpd_basefill_070'], 'func': vpd_base_universe_d2_065_vpd_basefill_070}


def vpd_base_universe_d2_066_vpd_basefill_071(vpd_basefill_071):
    return _base_universe_d2(vpd_basefill_071, 66)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_066_vpd_basefill_071'] = {'inputs': ['vpd_basefill_071'], 'func': vpd_base_universe_d2_066_vpd_basefill_071}


def vpd_base_universe_d2_067_vpd_basefill_072(vpd_basefill_072):
    return _base_universe_d2(vpd_basefill_072, 67)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_067_vpd_basefill_072'] = {'inputs': ['vpd_basefill_072'], 'func': vpd_base_universe_d2_067_vpd_basefill_072}


def vpd_base_universe_d2_068_vpd_basefill_073(vpd_basefill_073):
    return _base_universe_d2(vpd_basefill_073, 68)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_068_vpd_basefill_073'] = {'inputs': ['vpd_basefill_073'], 'func': vpd_base_universe_d2_068_vpd_basefill_073}


def vpd_base_universe_d2_069_vpd_basefill_074(vpd_basefill_074):
    return _base_universe_d2(vpd_basefill_074, 69)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_069_vpd_basefill_074'] = {'inputs': ['vpd_basefill_074'], 'func': vpd_base_universe_d2_069_vpd_basefill_074}


def vpd_base_universe_d2_070_vpd_basefill_075(vpd_basefill_075):
    return _base_universe_d2(vpd_basefill_075, 70)
VPD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vpd_base_universe_d2_070_vpd_basefill_075'] = {'inputs': ['vpd_basefill_075'], 'func': vpd_base_universe_d2_070_vpd_basefill_075}
