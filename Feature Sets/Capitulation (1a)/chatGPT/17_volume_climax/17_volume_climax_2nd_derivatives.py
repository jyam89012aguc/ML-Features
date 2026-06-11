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



def vcx_151_vcx_001_volume_spike_ratio_5_001_roc_1(vcx_001_volume_spike_ratio_5_001):
    feature = _s(vcx_001_volume_spike_ratio_5_001)
    return (_roc(feature, 1)).reindex(feature.index)

def vcx_152_vcx_007_volume_spike_ratio_126_007_roc_5(vcx_007_volume_spike_ratio_126_007):
    feature = _s(vcx_007_volume_spike_ratio_126_007)
    return (_roc(feature, 5)).reindex(feature.index)

def vcx_153_vcx_013_volume_spike_ratio_1008_013_roc_42(vcx_013_volume_spike_ratio_1008_013):
    feature = _s(vcx_013_volume_spike_ratio_1008_013)
    return (_roc(feature, 42)).reindex(feature.index)

def vcx_154_vcx_019_volume_spike_ratio_42_019_roc_126(vcx_019_volume_spike_ratio_42_019):
    feature = _s(vcx_019_volume_spike_ratio_42_019)
    return (_roc(feature, 126)).reindex(feature.index)

def vcx_155_vcx_025_volume_spike_ratio_378_025_roc_378(vcx_025_volume_spike_ratio_378_025):
    feature = _s(vcx_025_volume_spike_ratio_378_025)
    return (_roc(feature, 378)).reindex(feature.index)






















VOLUME_CLIMAX_REGISTRY_2ND_DERIVATIVES = {
    'vcx_151_vcx_001_volume_spike_ratio_5_001_roc_1': {'inputs': ['vcx_001_volume_spike_ratio_5_001'], 'func': vcx_151_vcx_001_volume_spike_ratio_5_001_roc_1},
    'vcx_152_vcx_007_volume_spike_ratio_126_007_roc_5': {'inputs': ['vcx_007_volume_spike_ratio_126_007'], 'func': vcx_152_vcx_007_volume_spike_ratio_126_007_roc_5},
    'vcx_153_vcx_013_volume_spike_ratio_1008_013_roc_42': {'inputs': ['vcx_013_volume_spike_ratio_1008_013'], 'func': vcx_153_vcx_013_volume_spike_ratio_1008_013_roc_42},
    'vcx_154_vcx_019_volume_spike_ratio_42_019_roc_126': {'inputs': ['vcx_019_volume_spike_ratio_42_019'], 'func': vcx_154_vcx_019_volume_spike_ratio_42_019_roc_126},
    'vcx_155_vcx_025_volume_spike_ratio_378_025_roc_378': {'inputs': ['vcx_025_volume_spike_ratio_378_025'], 'func': vcx_155_vcx_025_volume_spike_ratio_378_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def vc_replacement_d2_001(vc_replacement_001):
    feature = _clean(vc_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_001'] = {'inputs': ['vc_replacement_001'], 'func': vc_replacement_d2_001}


def vc_replacement_d2_002(vc_replacement_002):
    feature = _clean(vc_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_002'] = {'inputs': ['vc_replacement_002'], 'func': vc_replacement_d2_002}


def vc_replacement_d2_003(vc_replacement_003):
    feature = _clean(vc_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_003'] = {'inputs': ['vc_replacement_003'], 'func': vc_replacement_d2_003}


def vc_replacement_d2_004(vc_replacement_004):
    feature = _clean(vc_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_004'] = {'inputs': ['vc_replacement_004'], 'func': vc_replacement_d2_004}


def vc_replacement_d2_005(vc_replacement_005):
    feature = _clean(vc_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_005'] = {'inputs': ['vc_replacement_005'], 'func': vc_replacement_d2_005}


def vc_replacement_d2_006(vc_replacement_006):
    feature = _clean(vc_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_006'] = {'inputs': ['vc_replacement_006'], 'func': vc_replacement_d2_006}


def vc_replacement_d2_007(vc_replacement_007):
    feature = _clean(vc_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_007'] = {'inputs': ['vc_replacement_007'], 'func': vc_replacement_d2_007}


def vc_replacement_d2_008(vc_replacement_008):
    feature = _clean(vc_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_008'] = {'inputs': ['vc_replacement_008'], 'func': vc_replacement_d2_008}


def vc_replacement_d2_009(vc_replacement_009):
    feature = _clean(vc_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_009'] = {'inputs': ['vc_replacement_009'], 'func': vc_replacement_d2_009}


def vc_replacement_d2_010(vc_replacement_010):
    feature = _clean(vc_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_010'] = {'inputs': ['vc_replacement_010'], 'func': vc_replacement_d2_010}


def vc_replacement_d2_011(vc_replacement_011):
    feature = _clean(vc_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_011'] = {'inputs': ['vc_replacement_011'], 'func': vc_replacement_d2_011}


def vc_replacement_d2_012(vc_replacement_012):
    feature = _clean(vc_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_012'] = {'inputs': ['vc_replacement_012'], 'func': vc_replacement_d2_012}


def vc_replacement_d2_013(vc_replacement_013):
    feature = _clean(vc_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_013'] = {'inputs': ['vc_replacement_013'], 'func': vc_replacement_d2_013}


def vc_replacement_d2_014(vc_replacement_014):
    feature = _clean(vc_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_014'] = {'inputs': ['vc_replacement_014'], 'func': vc_replacement_d2_014}


def vc_replacement_d2_015(vc_replacement_015):
    feature = _clean(vc_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_015'] = {'inputs': ['vc_replacement_015'], 'func': vc_replacement_d2_015}


def vc_replacement_d2_016(vc_replacement_016):
    feature = _clean(vc_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_016'] = {'inputs': ['vc_replacement_016'], 'func': vc_replacement_d2_016}


def vc_replacement_d2_017(vc_replacement_017):
    feature = _clean(vc_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_017'] = {'inputs': ['vc_replacement_017'], 'func': vc_replacement_d2_017}


def vc_replacement_d2_018(vc_replacement_018):
    feature = _clean(vc_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_018'] = {'inputs': ['vc_replacement_018'], 'func': vc_replacement_d2_018}


def vc_replacement_d2_019(vc_replacement_019):
    feature = _clean(vc_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_019'] = {'inputs': ['vc_replacement_019'], 'func': vc_replacement_d2_019}


def vc_replacement_d2_020(vc_replacement_020):
    feature = _clean(vc_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_020'] = {'inputs': ['vc_replacement_020'], 'func': vc_replacement_d2_020}


def vc_replacement_d2_021(vc_replacement_021):
    feature = _clean(vc_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_021'] = {'inputs': ['vc_replacement_021'], 'func': vc_replacement_d2_021}


def vc_replacement_d2_022(vc_replacement_022):
    feature = _clean(vc_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_022'] = {'inputs': ['vc_replacement_022'], 'func': vc_replacement_d2_022}


def vc_replacement_d2_023(vc_replacement_023):
    feature = _clean(vc_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_023'] = {'inputs': ['vc_replacement_023'], 'func': vc_replacement_d2_023}


def vc_replacement_d2_024(vc_replacement_024):
    feature = _clean(vc_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_024'] = {'inputs': ['vc_replacement_024'], 'func': vc_replacement_d2_024}


def vc_replacement_d2_025(vc_replacement_025):
    feature = _clean(vc_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_025'] = {'inputs': ['vc_replacement_025'], 'func': vc_replacement_d2_025}


def vc_replacement_d2_026(vc_replacement_026):
    feature = _clean(vc_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_026'] = {'inputs': ['vc_replacement_026'], 'func': vc_replacement_d2_026}


def vc_replacement_d2_027(vc_replacement_027):
    feature = _clean(vc_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_027'] = {'inputs': ['vc_replacement_027'], 'func': vc_replacement_d2_027}


def vc_replacement_d2_028(vc_replacement_028):
    feature = _clean(vc_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_028'] = {'inputs': ['vc_replacement_028'], 'func': vc_replacement_d2_028}


def vc_replacement_d2_029(vc_replacement_029):
    feature = _clean(vc_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_029'] = {'inputs': ['vc_replacement_029'], 'func': vc_replacement_d2_029}


def vc_replacement_d2_030(vc_replacement_030):
    feature = _clean(vc_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_030'] = {'inputs': ['vc_replacement_030'], 'func': vc_replacement_d2_030}


def vc_replacement_d2_031(vc_replacement_031):
    feature = _clean(vc_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_031'] = {'inputs': ['vc_replacement_031'], 'func': vc_replacement_d2_031}


def vc_replacement_d2_032(vc_replacement_032):
    feature = _clean(vc_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_032'] = {'inputs': ['vc_replacement_032'], 'func': vc_replacement_d2_032}


def vc_replacement_d2_033(vc_replacement_033):
    feature = _clean(vc_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_033'] = {'inputs': ['vc_replacement_033'], 'func': vc_replacement_d2_033}


def vc_replacement_d2_034(vc_replacement_034):
    feature = _clean(vc_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_034'] = {'inputs': ['vc_replacement_034'], 'func': vc_replacement_d2_034}


def vc_replacement_d2_035(vc_replacement_035):
    feature = _clean(vc_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_035'] = {'inputs': ['vc_replacement_035'], 'func': vc_replacement_d2_035}


def vc_replacement_d2_036(vc_replacement_036):
    feature = _clean(vc_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_036'] = {'inputs': ['vc_replacement_036'], 'func': vc_replacement_d2_036}


def vc_replacement_d2_037(vc_replacement_037):
    feature = _clean(vc_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_037'] = {'inputs': ['vc_replacement_037'], 'func': vc_replacement_d2_037}


def vc_replacement_d2_038(vc_replacement_038):
    feature = _clean(vc_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_038'] = {'inputs': ['vc_replacement_038'], 'func': vc_replacement_d2_038}


def vc_replacement_d2_039(vc_replacement_039):
    feature = _clean(vc_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_039'] = {'inputs': ['vc_replacement_039'], 'func': vc_replacement_d2_039}


def vc_replacement_d2_040(vc_replacement_040):
    feature = _clean(vc_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_040'] = {'inputs': ['vc_replacement_040'], 'func': vc_replacement_d2_040}


def vc_replacement_d2_041(vc_replacement_041):
    feature = _clean(vc_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_041'] = {'inputs': ['vc_replacement_041'], 'func': vc_replacement_d2_041}


def vc_replacement_d2_042(vc_replacement_042):
    feature = _clean(vc_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_042'] = {'inputs': ['vc_replacement_042'], 'func': vc_replacement_d2_042}


def vc_replacement_d2_043(vc_replacement_043):
    feature = _clean(vc_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_043'] = {'inputs': ['vc_replacement_043'], 'func': vc_replacement_d2_043}


def vc_replacement_d2_044(vc_replacement_044):
    feature = _clean(vc_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_044'] = {'inputs': ['vc_replacement_044'], 'func': vc_replacement_d2_044}


def vc_replacement_d2_045(vc_replacement_045):
    feature = _clean(vc_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_045'] = {'inputs': ['vc_replacement_045'], 'func': vc_replacement_d2_045}


def vc_replacement_d2_046(vc_replacement_046):
    feature = _clean(vc_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_046'] = {'inputs': ['vc_replacement_046'], 'func': vc_replacement_d2_046}


def vc_replacement_d2_047(vc_replacement_047):
    feature = _clean(vc_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_047'] = {'inputs': ['vc_replacement_047'], 'func': vc_replacement_d2_047}


def vc_replacement_d2_048(vc_replacement_048):
    feature = _clean(vc_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_048'] = {'inputs': ['vc_replacement_048'], 'func': vc_replacement_d2_048}


def vc_replacement_d2_049(vc_replacement_049):
    feature = _clean(vc_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_049'] = {'inputs': ['vc_replacement_049'], 'func': vc_replacement_d2_049}


def vc_replacement_d2_050(vc_replacement_050):
    feature = _clean(vc_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_050'] = {'inputs': ['vc_replacement_050'], 'func': vc_replacement_d2_050}


def vc_replacement_d2_051(vc_replacement_051):
    feature = _clean(vc_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_051'] = {'inputs': ['vc_replacement_051'], 'func': vc_replacement_d2_051}


def vc_replacement_d2_052(vc_replacement_052):
    feature = _clean(vc_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_052'] = {'inputs': ['vc_replacement_052'], 'func': vc_replacement_d2_052}


def vc_replacement_d2_053(vc_replacement_053):
    feature = _clean(vc_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_053'] = {'inputs': ['vc_replacement_053'], 'func': vc_replacement_d2_053}


def vc_replacement_d2_054(vc_replacement_054):
    feature = _clean(vc_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_054'] = {'inputs': ['vc_replacement_054'], 'func': vc_replacement_d2_054}


def vc_replacement_d2_055(vc_replacement_055):
    feature = _clean(vc_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_055'] = {'inputs': ['vc_replacement_055'], 'func': vc_replacement_d2_055}


def vc_replacement_d2_056(vc_replacement_056):
    feature = _clean(vc_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_056'] = {'inputs': ['vc_replacement_056'], 'func': vc_replacement_d2_056}


def vc_replacement_d2_057(vc_replacement_057):
    feature = _clean(vc_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_057'] = {'inputs': ['vc_replacement_057'], 'func': vc_replacement_d2_057}


def vc_replacement_d2_058(vc_replacement_058):
    feature = _clean(vc_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_058'] = {'inputs': ['vc_replacement_058'], 'func': vc_replacement_d2_058}


def vc_replacement_d2_059(vc_replacement_059):
    feature = _clean(vc_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_059'] = {'inputs': ['vc_replacement_059'], 'func': vc_replacement_d2_059}


def vc_replacement_d2_060(vc_replacement_060):
    feature = _clean(vc_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_060'] = {'inputs': ['vc_replacement_060'], 'func': vc_replacement_d2_060}


def vc_replacement_d2_061(vc_replacement_061):
    feature = _clean(vc_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_061'] = {'inputs': ['vc_replacement_061'], 'func': vc_replacement_d2_061}


def vc_replacement_d2_062(vc_replacement_062):
    feature = _clean(vc_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_062'] = {'inputs': ['vc_replacement_062'], 'func': vc_replacement_d2_062}


def vc_replacement_d2_063(vc_replacement_063):
    feature = _clean(vc_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_063'] = {'inputs': ['vc_replacement_063'], 'func': vc_replacement_d2_063}


def vc_replacement_d2_064(vc_replacement_064):
    feature = _clean(vc_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_064'] = {'inputs': ['vc_replacement_064'], 'func': vc_replacement_d2_064}


def vc_replacement_d2_065(vc_replacement_065):
    feature = _clean(vc_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_065'] = {'inputs': ['vc_replacement_065'], 'func': vc_replacement_d2_065}


def vc_replacement_d2_066(vc_replacement_066):
    feature = _clean(vc_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_066'] = {'inputs': ['vc_replacement_066'], 'func': vc_replacement_d2_066}


def vc_replacement_d2_067(vc_replacement_067):
    feature = _clean(vc_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_067'] = {'inputs': ['vc_replacement_067'], 'func': vc_replacement_d2_067}


def vc_replacement_d2_068(vc_replacement_068):
    feature = _clean(vc_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_068'] = {'inputs': ['vc_replacement_068'], 'func': vc_replacement_d2_068}


def vc_replacement_d2_069(vc_replacement_069):
    feature = _clean(vc_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_069'] = {'inputs': ['vc_replacement_069'], 'func': vc_replacement_d2_069}


def vc_replacement_d2_070(vc_replacement_070):
    feature = _clean(vc_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_070'] = {'inputs': ['vc_replacement_070'], 'func': vc_replacement_d2_070}


def vc_replacement_d2_071(vc_replacement_071):
    feature = _clean(vc_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_071'] = {'inputs': ['vc_replacement_071'], 'func': vc_replacement_d2_071}


def vc_replacement_d2_072(vc_replacement_072):
    feature = _clean(vc_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_072'] = {'inputs': ['vc_replacement_072'], 'func': vc_replacement_d2_072}


def vc_replacement_d2_073(vc_replacement_073):
    feature = _clean(vc_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_073'] = {'inputs': ['vc_replacement_073'], 'func': vc_replacement_d2_073}


def vc_replacement_d2_074(vc_replacement_074):
    feature = _clean(vc_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_074'] = {'inputs': ['vc_replacement_074'], 'func': vc_replacement_d2_074}


def vc_replacement_d2_075(vc_replacement_075):
    feature = _clean(vc_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_075'] = {'inputs': ['vc_replacement_075'], 'func': vc_replacement_d2_075}


def vc_replacement_d2_076(vc_replacement_076):
    feature = _clean(vc_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_076'] = {'inputs': ['vc_replacement_076'], 'func': vc_replacement_d2_076}


def vc_replacement_d2_077(vc_replacement_077):
    feature = _clean(vc_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_077'] = {'inputs': ['vc_replacement_077'], 'func': vc_replacement_d2_077}


def vc_replacement_d2_078(vc_replacement_078):
    feature = _clean(vc_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_078'] = {'inputs': ['vc_replacement_078'], 'func': vc_replacement_d2_078}


def vc_replacement_d2_079(vc_replacement_079):
    feature = _clean(vc_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_079'] = {'inputs': ['vc_replacement_079'], 'func': vc_replacement_d2_079}


def vc_replacement_d2_080(vc_replacement_080):
    feature = _clean(vc_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_080'] = {'inputs': ['vc_replacement_080'], 'func': vc_replacement_d2_080}


def vc_replacement_d2_081(vc_replacement_081):
    feature = _clean(vc_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_081'] = {'inputs': ['vc_replacement_081'], 'func': vc_replacement_d2_081}


def vc_replacement_d2_082(vc_replacement_082):
    feature = _clean(vc_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_082'] = {'inputs': ['vc_replacement_082'], 'func': vc_replacement_d2_082}


def vc_replacement_d2_083(vc_replacement_083):
    feature = _clean(vc_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_083'] = {'inputs': ['vc_replacement_083'], 'func': vc_replacement_d2_083}


def vc_replacement_d2_084(vc_replacement_084):
    feature = _clean(vc_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_084'] = {'inputs': ['vc_replacement_084'], 'func': vc_replacement_d2_084}


def vc_replacement_d2_085(vc_replacement_085):
    feature = _clean(vc_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_085'] = {'inputs': ['vc_replacement_085'], 'func': vc_replacement_d2_085}


def vc_replacement_d2_086(vc_replacement_086):
    feature = _clean(vc_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_086'] = {'inputs': ['vc_replacement_086'], 'func': vc_replacement_d2_086}


def vc_replacement_d2_087(vc_replacement_087):
    feature = _clean(vc_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_087'] = {'inputs': ['vc_replacement_087'], 'func': vc_replacement_d2_087}


def vc_replacement_d2_088(vc_replacement_088):
    feature = _clean(vc_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_088'] = {'inputs': ['vc_replacement_088'], 'func': vc_replacement_d2_088}


def vc_replacement_d2_089(vc_replacement_089):
    feature = _clean(vc_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_089'] = {'inputs': ['vc_replacement_089'], 'func': vc_replacement_d2_089}


def vc_replacement_d2_090(vc_replacement_090):
    feature = _clean(vc_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_090'] = {'inputs': ['vc_replacement_090'], 'func': vc_replacement_d2_090}


def vc_replacement_d2_091(vc_replacement_091):
    feature = _clean(vc_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_091'] = {'inputs': ['vc_replacement_091'], 'func': vc_replacement_d2_091}


def vc_replacement_d2_092(vc_replacement_092):
    feature = _clean(vc_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_092'] = {'inputs': ['vc_replacement_092'], 'func': vc_replacement_d2_092}


def vc_replacement_d2_093(vc_replacement_093):
    feature = _clean(vc_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_093'] = {'inputs': ['vc_replacement_093'], 'func': vc_replacement_d2_093}


def vc_replacement_d2_094(vc_replacement_094):
    feature = _clean(vc_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_094'] = {'inputs': ['vc_replacement_094'], 'func': vc_replacement_d2_094}


def vc_replacement_d2_095(vc_replacement_095):
    feature = _clean(vc_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_095'] = {'inputs': ['vc_replacement_095'], 'func': vc_replacement_d2_095}


def vc_replacement_d2_096(vc_replacement_096):
    feature = _clean(vc_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_096'] = {'inputs': ['vc_replacement_096'], 'func': vc_replacement_d2_096}


def vc_replacement_d2_097(vc_replacement_097):
    feature = _clean(vc_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_097'] = {'inputs': ['vc_replacement_097'], 'func': vc_replacement_d2_097}


def vc_replacement_d2_098(vc_replacement_098):
    feature = _clean(vc_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_098'] = {'inputs': ['vc_replacement_098'], 'func': vc_replacement_d2_098}


def vc_replacement_d2_099(vc_replacement_099):
    feature = _clean(vc_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_099'] = {'inputs': ['vc_replacement_099'], 'func': vc_replacement_d2_099}


def vc_replacement_d2_100(vc_replacement_100):
    feature = _clean(vc_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_100'] = {'inputs': ['vc_replacement_100'], 'func': vc_replacement_d2_100}


def vc_replacement_d2_101(vc_replacement_101):
    feature = _clean(vc_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_101'] = {'inputs': ['vc_replacement_101'], 'func': vc_replacement_d2_101}


def vc_replacement_d2_102(vc_replacement_102):
    feature = _clean(vc_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_102'] = {'inputs': ['vc_replacement_102'], 'func': vc_replacement_d2_102}


def vc_replacement_d2_103(vc_replacement_103):
    feature = _clean(vc_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_103'] = {'inputs': ['vc_replacement_103'], 'func': vc_replacement_d2_103}


def vc_replacement_d2_104(vc_replacement_104):
    feature = _clean(vc_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_104'] = {'inputs': ['vc_replacement_104'], 'func': vc_replacement_d2_104}


def vc_replacement_d2_105(vc_replacement_105):
    feature = _clean(vc_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_105'] = {'inputs': ['vc_replacement_105'], 'func': vc_replacement_d2_105}


def vc_replacement_d2_106(vc_replacement_106):
    feature = _clean(vc_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_106'] = {'inputs': ['vc_replacement_106'], 'func': vc_replacement_d2_106}


def vc_replacement_d2_107(vc_replacement_107):
    feature = _clean(vc_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_107'] = {'inputs': ['vc_replacement_107'], 'func': vc_replacement_d2_107}


def vc_replacement_d2_108(vc_replacement_108):
    feature = _clean(vc_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_108'] = {'inputs': ['vc_replacement_108'], 'func': vc_replacement_d2_108}


def vc_replacement_d2_109(vc_replacement_109):
    feature = _clean(vc_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_109'] = {'inputs': ['vc_replacement_109'], 'func': vc_replacement_d2_109}


def vc_replacement_d2_110(vc_replacement_110):
    feature = _clean(vc_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_110'] = {'inputs': ['vc_replacement_110'], 'func': vc_replacement_d2_110}


def vc_replacement_d2_111(vc_replacement_111):
    feature = _clean(vc_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_111'] = {'inputs': ['vc_replacement_111'], 'func': vc_replacement_d2_111}


def vc_replacement_d2_112(vc_replacement_112):
    feature = _clean(vc_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_112'] = {'inputs': ['vc_replacement_112'], 'func': vc_replacement_d2_112}


def vc_replacement_d2_113(vc_replacement_113):
    feature = _clean(vc_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_113'] = {'inputs': ['vc_replacement_113'], 'func': vc_replacement_d2_113}


def vc_replacement_d2_114(vc_replacement_114):
    feature = _clean(vc_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_114'] = {'inputs': ['vc_replacement_114'], 'func': vc_replacement_d2_114}


def vc_replacement_d2_115(vc_replacement_115):
    feature = _clean(vc_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_115'] = {'inputs': ['vc_replacement_115'], 'func': vc_replacement_d2_115}


def vc_replacement_d2_116(vc_replacement_116):
    feature = _clean(vc_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_116'] = {'inputs': ['vc_replacement_116'], 'func': vc_replacement_d2_116}


def vc_replacement_d2_117(vc_replacement_117):
    feature = _clean(vc_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_117'] = {'inputs': ['vc_replacement_117'], 'func': vc_replacement_d2_117}


def vc_replacement_d2_118(vc_replacement_118):
    feature = _clean(vc_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_118'] = {'inputs': ['vc_replacement_118'], 'func': vc_replacement_d2_118}


def vc_replacement_d2_119(vc_replacement_119):
    feature = _clean(vc_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_119'] = {'inputs': ['vc_replacement_119'], 'func': vc_replacement_d2_119}


def vc_replacement_d2_120(vc_replacement_120):
    feature = _clean(vc_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_120'] = {'inputs': ['vc_replacement_120'], 'func': vc_replacement_d2_120}


def vc_replacement_d2_121(vc_replacement_121):
    feature = _clean(vc_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_121'] = {'inputs': ['vc_replacement_121'], 'func': vc_replacement_d2_121}


def vc_replacement_d2_122(vc_replacement_122):
    feature = _clean(vc_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_122'] = {'inputs': ['vc_replacement_122'], 'func': vc_replacement_d2_122}


def vc_replacement_d2_123(vc_replacement_123):
    feature = _clean(vc_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_123'] = {'inputs': ['vc_replacement_123'], 'func': vc_replacement_d2_123}


def vc_replacement_d2_124(vc_replacement_124):
    feature = _clean(vc_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_124'] = {'inputs': ['vc_replacement_124'], 'func': vc_replacement_d2_124}


def vc_replacement_d2_125(vc_replacement_125):
    feature = _clean(vc_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_125'] = {'inputs': ['vc_replacement_125'], 'func': vc_replacement_d2_125}


def vc_replacement_d2_126(vc_replacement_126):
    feature = _clean(vc_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_126'] = {'inputs': ['vc_replacement_126'], 'func': vc_replacement_d2_126}


def vc_replacement_d2_127(vc_replacement_127):
    feature = _clean(vc_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_127'] = {'inputs': ['vc_replacement_127'], 'func': vc_replacement_d2_127}


def vc_replacement_d2_128(vc_replacement_128):
    feature = _clean(vc_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_128'] = {'inputs': ['vc_replacement_128'], 'func': vc_replacement_d2_128}


def vc_replacement_d2_129(vc_replacement_129):
    feature = _clean(vc_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_129'] = {'inputs': ['vc_replacement_129'], 'func': vc_replacement_d2_129}


def vc_replacement_d2_130(vc_replacement_130):
    feature = _clean(vc_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_130'] = {'inputs': ['vc_replacement_130'], 'func': vc_replacement_d2_130}


def vc_replacement_d2_131(vc_replacement_131):
    feature = _clean(vc_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_131'] = {'inputs': ['vc_replacement_131'], 'func': vc_replacement_d2_131}


def vc_replacement_d2_132(vc_replacement_132):
    feature = _clean(vc_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_132'] = {'inputs': ['vc_replacement_132'], 'func': vc_replacement_d2_132}


def vc_replacement_d2_133(vc_replacement_133):
    feature = _clean(vc_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_133'] = {'inputs': ['vc_replacement_133'], 'func': vc_replacement_d2_133}


def vc_replacement_d2_134(vc_replacement_134):
    feature = _clean(vc_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_134'] = {'inputs': ['vc_replacement_134'], 'func': vc_replacement_d2_134}


def vc_replacement_d2_135(vc_replacement_135):
    feature = _clean(vc_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_135'] = {'inputs': ['vc_replacement_135'], 'func': vc_replacement_d2_135}


def vc_replacement_d2_136(vc_replacement_136):
    feature = _clean(vc_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_136'] = {'inputs': ['vc_replacement_136'], 'func': vc_replacement_d2_136}


def vc_replacement_d2_137(vc_replacement_137):
    feature = _clean(vc_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_137'] = {'inputs': ['vc_replacement_137'], 'func': vc_replacement_d2_137}


def vc_replacement_d2_138(vc_replacement_138):
    feature = _clean(vc_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_138'] = {'inputs': ['vc_replacement_138'], 'func': vc_replacement_d2_138}


def vc_replacement_d2_139(vc_replacement_139):
    feature = _clean(vc_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_139'] = {'inputs': ['vc_replacement_139'], 'func': vc_replacement_d2_139}


def vc_replacement_d2_140(vc_replacement_140):
    feature = _clean(vc_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_140'] = {'inputs': ['vc_replacement_140'], 'func': vc_replacement_d2_140}


def vc_replacement_d2_141(vc_replacement_141):
    feature = _clean(vc_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_141'] = {'inputs': ['vc_replacement_141'], 'func': vc_replacement_d2_141}


def vc_replacement_d2_142(vc_replacement_142):
    feature = _clean(vc_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_142'] = {'inputs': ['vc_replacement_142'], 'func': vc_replacement_d2_142}


def vc_replacement_d2_143(vc_replacement_143):
    feature = _clean(vc_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_143'] = {'inputs': ['vc_replacement_143'], 'func': vc_replacement_d2_143}


def vc_replacement_d2_144(vc_replacement_144):
    feature = _clean(vc_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_144'] = {'inputs': ['vc_replacement_144'], 'func': vc_replacement_d2_144}


def vc_replacement_d2_145(vc_replacement_145):
    feature = _clean(vc_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_145'] = {'inputs': ['vc_replacement_145'], 'func': vc_replacement_d2_145}


def vc_replacement_d2_146(vc_replacement_146):
    feature = _clean(vc_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_146'] = {'inputs': ['vc_replacement_146'], 'func': vc_replacement_d2_146}


def vc_replacement_d2_147(vc_replacement_147):
    feature = _clean(vc_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_147'] = {'inputs': ['vc_replacement_147'], 'func': vc_replacement_d2_147}


def vc_replacement_d2_148(vc_replacement_148):
    feature = _clean(vc_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_148'] = {'inputs': ['vc_replacement_148'], 'func': vc_replacement_d2_148}


def vc_replacement_d2_149(vc_replacement_149):
    feature = _clean(vc_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_149'] = {'inputs': ['vc_replacement_149'], 'func': vc_replacement_d2_149}


def vc_replacement_d2_150(vc_replacement_150):
    feature = _clean(vc_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_150'] = {'inputs': ['vc_replacement_150'], 'func': vc_replacement_d2_150}


def vc_replacement_d2_151(vc_replacement_151):
    feature = _clean(vc_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_151'] = {'inputs': ['vc_replacement_151'], 'func': vc_replacement_d2_151}


def vc_replacement_d2_152(vc_replacement_152):
    feature = _clean(vc_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_152'] = {'inputs': ['vc_replacement_152'], 'func': vc_replacement_d2_152}


def vc_replacement_d2_153(vc_replacement_153):
    feature = _clean(vc_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_153'] = {'inputs': ['vc_replacement_153'], 'func': vc_replacement_d2_153}


def vc_replacement_d2_154(vc_replacement_154):
    feature = _clean(vc_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_154'] = {'inputs': ['vc_replacement_154'], 'func': vc_replacement_d2_154}


def vc_replacement_d2_155(vc_replacement_155):
    feature = _clean(vc_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_155'] = {'inputs': ['vc_replacement_155'], 'func': vc_replacement_d2_155}


def vc_replacement_d2_156(vc_replacement_156):
    feature = _clean(vc_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_156'] = {'inputs': ['vc_replacement_156'], 'func': vc_replacement_d2_156}


def vc_replacement_d2_157(vc_replacement_157):
    feature = _clean(vc_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_157'] = {'inputs': ['vc_replacement_157'], 'func': vc_replacement_d2_157}


def vc_replacement_d2_158(vc_replacement_158):
    feature = _clean(vc_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_158'] = {'inputs': ['vc_replacement_158'], 'func': vc_replacement_d2_158}


def vc_replacement_d2_159(vc_replacement_159):
    feature = _clean(vc_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_159'] = {'inputs': ['vc_replacement_159'], 'func': vc_replacement_d2_159}


def vc_replacement_d2_160(vc_replacement_160):
    feature = _clean(vc_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_160'] = {'inputs': ['vc_replacement_160'], 'func': vc_replacement_d2_160}


# Base-universe derivative extensions for repaired first-base features.
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def vcx_base_universe_d2_001_vcx_002_volume_zscore_10_002(vcx_002_volume_zscore_10_002):
    return _base_universe_d2(vcx_002_volume_zscore_10_002, 1)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_001_vcx_002_volume_zscore_10_002'] = {'inputs': ['vcx_002_volume_zscore_10_002'], 'func': vcx_base_universe_d2_001_vcx_002_volume_zscore_10_002}


def vcx_base_universe_d2_002_vcx_003_down_volume_share_21_003(vcx_003_down_volume_share_21_003):
    return _base_universe_d2(vcx_003_down_volume_share_21_003, 2)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_002_vcx_003_down_volume_share_21_003'] = {'inputs': ['vcx_003_down_volume_share_21_003'], 'func': vcx_base_universe_d2_002_vcx_003_down_volume_share_21_003}


def vcx_base_universe_d2_003_vcx_004_dollar_volume_shock_42_004(vcx_004_dollar_volume_shock_42_004):
    return _base_universe_d2(vcx_004_dollar_volume_shock_42_004, 3)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_003_vcx_004_dollar_volume_shock_42_004'] = {'inputs': ['vcx_004_dollar_volume_shock_42_004'], 'func': vcx_base_universe_d2_003_vcx_004_dollar_volume_shock_42_004}


def vcx_base_universe_d2_004_vcx_005_volume_trend_slope_63_005(vcx_005_volume_trend_slope_63_005):
    return _base_universe_d2(vcx_005_volume_trend_slope_63_005, 4)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_004_vcx_005_volume_trend_slope_63_005'] = {'inputs': ['vcx_005_volume_trend_slope_63_005'], 'func': vcx_base_universe_d2_004_vcx_005_volume_trend_slope_63_005}


def vcx_base_universe_d2_005_vcx_006_price_volume_divergence_84_006(vcx_006_price_volume_divergence_84_006):
    return _base_universe_d2(vcx_006_price_volume_divergence_84_006, 5)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_005_vcx_006_price_volume_divergence_84_006'] = {'inputs': ['vcx_006_price_volume_divergence_84_006'], 'func': vcx_base_universe_d2_005_vcx_006_price_volume_divergence_84_006}


def vcx_base_universe_d2_006_vcx_008_volume_zscore_189_008(vcx_008_volume_zscore_189_008):
    return _base_universe_d2(vcx_008_volume_zscore_189_008, 6)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_006_vcx_008_volume_zscore_189_008'] = {'inputs': ['vcx_008_volume_zscore_189_008'], 'func': vcx_base_universe_d2_006_vcx_008_volume_zscore_189_008}


def vcx_base_universe_d2_007_vcx_009_down_volume_share_252_009(vcx_009_down_volume_share_252_009):
    return _base_universe_d2(vcx_009_down_volume_share_252_009, 7)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_007_vcx_009_down_volume_share_252_009'] = {'inputs': ['vcx_009_down_volume_share_252_009'], 'func': vcx_base_universe_d2_007_vcx_009_down_volume_share_252_009}


def vcx_base_universe_d2_008_vcx_010_dollar_volume_shock_378_010(vcx_010_dollar_volume_shock_378_010):
    return _base_universe_d2(vcx_010_dollar_volume_shock_378_010, 8)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_008_vcx_010_dollar_volume_shock_378_010'] = {'inputs': ['vcx_010_dollar_volume_shock_378_010'], 'func': vcx_base_universe_d2_008_vcx_010_dollar_volume_shock_378_010}


def vcx_base_universe_d2_009_vcx_011_volume_trend_slope_504_011(vcx_011_volume_trend_slope_504_011):
    return _base_universe_d2(vcx_011_volume_trend_slope_504_011, 9)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_009_vcx_011_volume_trend_slope_504_011'] = {'inputs': ['vcx_011_volume_trend_slope_504_011'], 'func': vcx_base_universe_d2_009_vcx_011_volume_trend_slope_504_011}


def vcx_base_universe_d2_010_vcx_012_price_volume_divergence_756_012(vcx_012_price_volume_divergence_756_012):
    return _base_universe_d2(vcx_012_price_volume_divergence_756_012, 10)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_010_vcx_012_price_volume_divergence_756_012'] = {'inputs': ['vcx_012_price_volume_divergence_756_012'], 'func': vcx_base_universe_d2_010_vcx_012_price_volume_divergence_756_012}


def vcx_base_universe_d2_011_vcx_014_volume_zscore_1260_014(vcx_014_volume_zscore_1260_014):
    return _base_universe_d2(vcx_014_volume_zscore_1260_014, 11)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_011_vcx_014_volume_zscore_1260_014'] = {'inputs': ['vcx_014_volume_zscore_1260_014'], 'func': vcx_base_universe_d2_011_vcx_014_volume_zscore_1260_014}


def vcx_base_universe_d2_012_vcx_015_down_volume_share_1512_015(vcx_015_down_volume_share_1512_015):
    return _base_universe_d2(vcx_015_down_volume_share_1512_015, 12)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_012_vcx_015_down_volume_share_1512_015'] = {'inputs': ['vcx_015_down_volume_share_1512_015'], 'func': vcx_base_universe_d2_012_vcx_015_down_volume_share_1512_015}


def vcx_base_universe_d2_013_vcx_016_dollar_volume_shock_5_016(vcx_016_dollar_volume_shock_5_016):
    return _base_universe_d2(vcx_016_dollar_volume_shock_5_016, 13)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_013_vcx_016_dollar_volume_shock_5_016'] = {'inputs': ['vcx_016_dollar_volume_shock_5_016'], 'func': vcx_base_universe_d2_013_vcx_016_dollar_volume_shock_5_016}


def vcx_base_universe_d2_014_vcx_017_volume_trend_slope_10_017(vcx_017_volume_trend_slope_10_017):
    return _base_universe_d2(vcx_017_volume_trend_slope_10_017, 14)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_014_vcx_017_volume_trend_slope_10_017'] = {'inputs': ['vcx_017_volume_trend_slope_10_017'], 'func': vcx_base_universe_d2_014_vcx_017_volume_trend_slope_10_017}


def vcx_base_universe_d2_015_vcx_018_price_volume_divergence_21_018(vcx_018_price_volume_divergence_21_018):
    return _base_universe_d2(vcx_018_price_volume_divergence_21_018, 15)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_015_vcx_018_price_volume_divergence_21_018'] = {'inputs': ['vcx_018_price_volume_divergence_21_018'], 'func': vcx_base_universe_d2_015_vcx_018_price_volume_divergence_21_018}


def vcx_base_universe_d2_016_vcx_020_volume_zscore_63_020(vcx_020_volume_zscore_63_020):
    return _base_universe_d2(vcx_020_volume_zscore_63_020, 16)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_016_vcx_020_volume_zscore_63_020'] = {'inputs': ['vcx_020_volume_zscore_63_020'], 'func': vcx_base_universe_d2_016_vcx_020_volume_zscore_63_020}


def vcx_base_universe_d2_017_vcx_021_down_volume_share_84_021(vcx_021_down_volume_share_84_021):
    return _base_universe_d2(vcx_021_down_volume_share_84_021, 17)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_017_vcx_021_down_volume_share_84_021'] = {'inputs': ['vcx_021_down_volume_share_84_021'], 'func': vcx_base_universe_d2_017_vcx_021_down_volume_share_84_021}


def vcx_base_universe_d2_018_vcx_022_dollar_volume_shock_126_022(vcx_022_dollar_volume_shock_126_022):
    return _base_universe_d2(vcx_022_dollar_volume_shock_126_022, 18)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_018_vcx_022_dollar_volume_shock_126_022'] = {'inputs': ['vcx_022_dollar_volume_shock_126_022'], 'func': vcx_base_universe_d2_018_vcx_022_dollar_volume_shock_126_022}


def vcx_base_universe_d2_019_vcx_023_volume_trend_slope_189_023(vcx_023_volume_trend_slope_189_023):
    return _base_universe_d2(vcx_023_volume_trend_slope_189_023, 19)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_019_vcx_023_volume_trend_slope_189_023'] = {'inputs': ['vcx_023_volume_trend_slope_189_023'], 'func': vcx_base_universe_d2_019_vcx_023_volume_trend_slope_189_023}


def vcx_base_universe_d2_020_vcx_024_price_volume_divergence_252_024(vcx_024_price_volume_divergence_252_024):
    return _base_universe_d2(vcx_024_price_volume_divergence_252_024, 20)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_020_vcx_024_price_volume_divergence_252_024'] = {'inputs': ['vcx_024_price_volume_divergence_252_024'], 'func': vcx_base_universe_d2_020_vcx_024_price_volume_divergence_252_024}


def vcx_base_universe_d2_021_vcx_026_volume_zscore_504_026(vcx_026_volume_zscore_504_026):
    return _base_universe_d2(vcx_026_volume_zscore_504_026, 21)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_021_vcx_026_volume_zscore_504_026'] = {'inputs': ['vcx_026_volume_zscore_504_026'], 'func': vcx_base_universe_d2_021_vcx_026_volume_zscore_504_026}


def vcx_base_universe_d2_022_vcx_027_down_volume_share_756_027(vcx_027_down_volume_share_756_027):
    return _base_universe_d2(vcx_027_down_volume_share_756_027, 22)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_022_vcx_027_down_volume_share_756_027'] = {'inputs': ['vcx_027_down_volume_share_756_027'], 'func': vcx_base_universe_d2_022_vcx_027_down_volume_share_756_027}


def vcx_base_universe_d2_023_vcx_028_dollar_volume_shock_1008_028(vcx_028_dollar_volume_shock_1008_028):
    return _base_universe_d2(vcx_028_dollar_volume_shock_1008_028, 23)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_023_vcx_028_dollar_volume_shock_1008_028'] = {'inputs': ['vcx_028_dollar_volume_shock_1008_028'], 'func': vcx_base_universe_d2_023_vcx_028_dollar_volume_shock_1008_028}


def vcx_base_universe_d2_024_vcx_029_volume_trend_slope_1260_029(vcx_029_volume_trend_slope_1260_029):
    return _base_universe_d2(vcx_029_volume_trend_slope_1260_029, 24)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_024_vcx_029_volume_trend_slope_1260_029'] = {'inputs': ['vcx_029_volume_trend_slope_1260_029'], 'func': vcx_base_universe_d2_024_vcx_029_volume_trend_slope_1260_029}


def vcx_base_universe_d2_025_vcx_030_price_volume_divergence_1512_030(vcx_030_price_volume_divergence_1512_030):
    return _base_universe_d2(vcx_030_price_volume_divergence_1512_030, 25)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_025_vcx_030_price_volume_divergence_1512_030'] = {'inputs': ['vcx_030_price_volume_divergence_1512_030'], 'func': vcx_base_universe_d2_025_vcx_030_price_volume_divergence_1512_030}


def vcx_base_universe_d2_026_vcx_basefill_031(vcx_basefill_031):
    return _base_universe_d2(vcx_basefill_031, 26)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_026_vcx_basefill_031'] = {'inputs': ['vcx_basefill_031'], 'func': vcx_base_universe_d2_026_vcx_basefill_031}


def vcx_base_universe_d2_027_vcx_basefill_032(vcx_basefill_032):
    return _base_universe_d2(vcx_basefill_032, 27)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_027_vcx_basefill_032'] = {'inputs': ['vcx_basefill_032'], 'func': vcx_base_universe_d2_027_vcx_basefill_032}


def vcx_base_universe_d2_028_vcx_basefill_033(vcx_basefill_033):
    return _base_universe_d2(vcx_basefill_033, 28)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_028_vcx_basefill_033'] = {'inputs': ['vcx_basefill_033'], 'func': vcx_base_universe_d2_028_vcx_basefill_033}


def vcx_base_universe_d2_029_vcx_basefill_034(vcx_basefill_034):
    return _base_universe_d2(vcx_basefill_034, 29)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_029_vcx_basefill_034'] = {'inputs': ['vcx_basefill_034'], 'func': vcx_base_universe_d2_029_vcx_basefill_034}


def vcx_base_universe_d2_030_vcx_basefill_035(vcx_basefill_035):
    return _base_universe_d2(vcx_basefill_035, 30)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_030_vcx_basefill_035'] = {'inputs': ['vcx_basefill_035'], 'func': vcx_base_universe_d2_030_vcx_basefill_035}


def vcx_base_universe_d2_031_vcx_basefill_036(vcx_basefill_036):
    return _base_universe_d2(vcx_basefill_036, 31)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_031_vcx_basefill_036'] = {'inputs': ['vcx_basefill_036'], 'func': vcx_base_universe_d2_031_vcx_basefill_036}


def vcx_base_universe_d2_032_vcx_basefill_037(vcx_basefill_037):
    return _base_universe_d2(vcx_basefill_037, 32)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_032_vcx_basefill_037'] = {'inputs': ['vcx_basefill_037'], 'func': vcx_base_universe_d2_032_vcx_basefill_037}


def vcx_base_universe_d2_033_vcx_basefill_038(vcx_basefill_038):
    return _base_universe_d2(vcx_basefill_038, 33)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_033_vcx_basefill_038'] = {'inputs': ['vcx_basefill_038'], 'func': vcx_base_universe_d2_033_vcx_basefill_038}


def vcx_base_universe_d2_034_vcx_basefill_039(vcx_basefill_039):
    return _base_universe_d2(vcx_basefill_039, 34)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_034_vcx_basefill_039'] = {'inputs': ['vcx_basefill_039'], 'func': vcx_base_universe_d2_034_vcx_basefill_039}


def vcx_base_universe_d2_035_vcx_basefill_040(vcx_basefill_040):
    return _base_universe_d2(vcx_basefill_040, 35)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_035_vcx_basefill_040'] = {'inputs': ['vcx_basefill_040'], 'func': vcx_base_universe_d2_035_vcx_basefill_040}


def vcx_base_universe_d2_036_vcx_basefill_041(vcx_basefill_041):
    return _base_universe_d2(vcx_basefill_041, 36)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_036_vcx_basefill_041'] = {'inputs': ['vcx_basefill_041'], 'func': vcx_base_universe_d2_036_vcx_basefill_041}


def vcx_base_universe_d2_037_vcx_basefill_042(vcx_basefill_042):
    return _base_universe_d2(vcx_basefill_042, 37)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_037_vcx_basefill_042'] = {'inputs': ['vcx_basefill_042'], 'func': vcx_base_universe_d2_037_vcx_basefill_042}


def vcx_base_universe_d2_038_vcx_basefill_043(vcx_basefill_043):
    return _base_universe_d2(vcx_basefill_043, 38)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_038_vcx_basefill_043'] = {'inputs': ['vcx_basefill_043'], 'func': vcx_base_universe_d2_038_vcx_basefill_043}


def vcx_base_universe_d2_039_vcx_basefill_044(vcx_basefill_044):
    return _base_universe_d2(vcx_basefill_044, 39)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_039_vcx_basefill_044'] = {'inputs': ['vcx_basefill_044'], 'func': vcx_base_universe_d2_039_vcx_basefill_044}


def vcx_base_universe_d2_040_vcx_basefill_045(vcx_basefill_045):
    return _base_universe_d2(vcx_basefill_045, 40)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_040_vcx_basefill_045'] = {'inputs': ['vcx_basefill_045'], 'func': vcx_base_universe_d2_040_vcx_basefill_045}


def vcx_base_universe_d2_041_vcx_basefill_046(vcx_basefill_046):
    return _base_universe_d2(vcx_basefill_046, 41)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_041_vcx_basefill_046'] = {'inputs': ['vcx_basefill_046'], 'func': vcx_base_universe_d2_041_vcx_basefill_046}


def vcx_base_universe_d2_042_vcx_basefill_047(vcx_basefill_047):
    return _base_universe_d2(vcx_basefill_047, 42)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_042_vcx_basefill_047'] = {'inputs': ['vcx_basefill_047'], 'func': vcx_base_universe_d2_042_vcx_basefill_047}


def vcx_base_universe_d2_043_vcx_basefill_048(vcx_basefill_048):
    return _base_universe_d2(vcx_basefill_048, 43)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_043_vcx_basefill_048'] = {'inputs': ['vcx_basefill_048'], 'func': vcx_base_universe_d2_043_vcx_basefill_048}


def vcx_base_universe_d2_044_vcx_basefill_049(vcx_basefill_049):
    return _base_universe_d2(vcx_basefill_049, 44)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_044_vcx_basefill_049'] = {'inputs': ['vcx_basefill_049'], 'func': vcx_base_universe_d2_044_vcx_basefill_049}


def vcx_base_universe_d2_045_vcx_basefill_050(vcx_basefill_050):
    return _base_universe_d2(vcx_basefill_050, 45)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_045_vcx_basefill_050'] = {'inputs': ['vcx_basefill_050'], 'func': vcx_base_universe_d2_045_vcx_basefill_050}


def vcx_base_universe_d2_046_vcx_basefill_051(vcx_basefill_051):
    return _base_universe_d2(vcx_basefill_051, 46)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_046_vcx_basefill_051'] = {'inputs': ['vcx_basefill_051'], 'func': vcx_base_universe_d2_046_vcx_basefill_051}


def vcx_base_universe_d2_047_vcx_basefill_052(vcx_basefill_052):
    return _base_universe_d2(vcx_basefill_052, 47)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_047_vcx_basefill_052'] = {'inputs': ['vcx_basefill_052'], 'func': vcx_base_universe_d2_047_vcx_basefill_052}


def vcx_base_universe_d2_048_vcx_basefill_053(vcx_basefill_053):
    return _base_universe_d2(vcx_basefill_053, 48)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_048_vcx_basefill_053'] = {'inputs': ['vcx_basefill_053'], 'func': vcx_base_universe_d2_048_vcx_basefill_053}


def vcx_base_universe_d2_049_vcx_basefill_054(vcx_basefill_054):
    return _base_universe_d2(vcx_basefill_054, 49)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_049_vcx_basefill_054'] = {'inputs': ['vcx_basefill_054'], 'func': vcx_base_universe_d2_049_vcx_basefill_054}


def vcx_base_universe_d2_050_vcx_basefill_055(vcx_basefill_055):
    return _base_universe_d2(vcx_basefill_055, 50)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_050_vcx_basefill_055'] = {'inputs': ['vcx_basefill_055'], 'func': vcx_base_universe_d2_050_vcx_basefill_055}


def vcx_base_universe_d2_051_vcx_basefill_056(vcx_basefill_056):
    return _base_universe_d2(vcx_basefill_056, 51)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_051_vcx_basefill_056'] = {'inputs': ['vcx_basefill_056'], 'func': vcx_base_universe_d2_051_vcx_basefill_056}


def vcx_base_universe_d2_052_vcx_basefill_057(vcx_basefill_057):
    return _base_universe_d2(vcx_basefill_057, 52)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_052_vcx_basefill_057'] = {'inputs': ['vcx_basefill_057'], 'func': vcx_base_universe_d2_052_vcx_basefill_057}


def vcx_base_universe_d2_053_vcx_basefill_058(vcx_basefill_058):
    return _base_universe_d2(vcx_basefill_058, 53)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_053_vcx_basefill_058'] = {'inputs': ['vcx_basefill_058'], 'func': vcx_base_universe_d2_053_vcx_basefill_058}


def vcx_base_universe_d2_054_vcx_basefill_059(vcx_basefill_059):
    return _base_universe_d2(vcx_basefill_059, 54)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_054_vcx_basefill_059'] = {'inputs': ['vcx_basefill_059'], 'func': vcx_base_universe_d2_054_vcx_basefill_059}


def vcx_base_universe_d2_055_vcx_basefill_060(vcx_basefill_060):
    return _base_universe_d2(vcx_basefill_060, 55)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_055_vcx_basefill_060'] = {'inputs': ['vcx_basefill_060'], 'func': vcx_base_universe_d2_055_vcx_basefill_060}


def vcx_base_universe_d2_056_vcx_basefill_061(vcx_basefill_061):
    return _base_universe_d2(vcx_basefill_061, 56)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_056_vcx_basefill_061'] = {'inputs': ['vcx_basefill_061'], 'func': vcx_base_universe_d2_056_vcx_basefill_061}


def vcx_base_universe_d2_057_vcx_basefill_062(vcx_basefill_062):
    return _base_universe_d2(vcx_basefill_062, 57)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_057_vcx_basefill_062'] = {'inputs': ['vcx_basefill_062'], 'func': vcx_base_universe_d2_057_vcx_basefill_062}


def vcx_base_universe_d2_058_vcx_basefill_063(vcx_basefill_063):
    return _base_universe_d2(vcx_basefill_063, 58)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_058_vcx_basefill_063'] = {'inputs': ['vcx_basefill_063'], 'func': vcx_base_universe_d2_058_vcx_basefill_063}


def vcx_base_universe_d2_059_vcx_basefill_064(vcx_basefill_064):
    return _base_universe_d2(vcx_basefill_064, 59)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_059_vcx_basefill_064'] = {'inputs': ['vcx_basefill_064'], 'func': vcx_base_universe_d2_059_vcx_basefill_064}


def vcx_base_universe_d2_060_vcx_basefill_065(vcx_basefill_065):
    return _base_universe_d2(vcx_basefill_065, 60)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_060_vcx_basefill_065'] = {'inputs': ['vcx_basefill_065'], 'func': vcx_base_universe_d2_060_vcx_basefill_065}


def vcx_base_universe_d2_061_vcx_basefill_066(vcx_basefill_066):
    return _base_universe_d2(vcx_basefill_066, 61)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_061_vcx_basefill_066'] = {'inputs': ['vcx_basefill_066'], 'func': vcx_base_universe_d2_061_vcx_basefill_066}


def vcx_base_universe_d2_062_vcx_basefill_067(vcx_basefill_067):
    return _base_universe_d2(vcx_basefill_067, 62)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_062_vcx_basefill_067'] = {'inputs': ['vcx_basefill_067'], 'func': vcx_base_universe_d2_062_vcx_basefill_067}


def vcx_base_universe_d2_063_vcx_basefill_068(vcx_basefill_068):
    return _base_universe_d2(vcx_basefill_068, 63)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_063_vcx_basefill_068'] = {'inputs': ['vcx_basefill_068'], 'func': vcx_base_universe_d2_063_vcx_basefill_068}


def vcx_base_universe_d2_064_vcx_basefill_069(vcx_basefill_069):
    return _base_universe_d2(vcx_basefill_069, 64)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_064_vcx_basefill_069'] = {'inputs': ['vcx_basefill_069'], 'func': vcx_base_universe_d2_064_vcx_basefill_069}


def vcx_base_universe_d2_065_vcx_basefill_070(vcx_basefill_070):
    return _base_universe_d2(vcx_basefill_070, 65)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_065_vcx_basefill_070'] = {'inputs': ['vcx_basefill_070'], 'func': vcx_base_universe_d2_065_vcx_basefill_070}


def vcx_base_universe_d2_066_vcx_basefill_071(vcx_basefill_071):
    return _base_universe_d2(vcx_basefill_071, 66)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_066_vcx_basefill_071'] = {'inputs': ['vcx_basefill_071'], 'func': vcx_base_universe_d2_066_vcx_basefill_071}


def vcx_base_universe_d2_067_vcx_basefill_072(vcx_basefill_072):
    return _base_universe_d2(vcx_basefill_072, 67)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_067_vcx_basefill_072'] = {'inputs': ['vcx_basefill_072'], 'func': vcx_base_universe_d2_067_vcx_basefill_072}


def vcx_base_universe_d2_068_vcx_basefill_073(vcx_basefill_073):
    return _base_universe_d2(vcx_basefill_073, 68)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_068_vcx_basefill_073'] = {'inputs': ['vcx_basefill_073'], 'func': vcx_base_universe_d2_068_vcx_basefill_073}


def vcx_base_universe_d2_069_vcx_basefill_074(vcx_basefill_074):
    return _base_universe_d2(vcx_basefill_074, 69)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_069_vcx_basefill_074'] = {'inputs': ['vcx_basefill_074'], 'func': vcx_base_universe_d2_069_vcx_basefill_074}


def vcx_base_universe_d2_070_vcx_basefill_075(vcx_basefill_075):
    return _base_universe_d2(vcx_basefill_075, 70)
VCX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcx_base_universe_d2_070_vcx_basefill_075'] = {'inputs': ['vcx_basefill_075'], 'func': vcx_base_universe_d2_070_vcx_basefill_075}
