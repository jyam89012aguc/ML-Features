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



def vb_176_vb_001_volume_spike_ratio_5_001_accel_1(vb_151_vb_001_volume_spike_ratio_5_001_roc_1):
    feature = _s(vb_151_vb_001_volume_spike_ratio_5_001_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def vb_177_vb_007_volume_spike_ratio_126_007_accel_5(vb_152_vb_007_volume_spike_ratio_126_007_roc_5):
    feature = _s(vb_152_vb_007_volume_spike_ratio_126_007_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def vb_178_vb_013_volume_spike_ratio_1008_013_accel_42(vb_153_vb_013_volume_spike_ratio_1008_013_roc_42):
    feature = _s(vb_153_vb_013_volume_spike_ratio_1008_013_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def vb_179_vb_019_volume_spike_ratio_42_019_accel_126(vb_154_vb_019_volume_spike_ratio_42_019_roc_126):
    feature = _s(vb_154_vb_019_volume_spike_ratio_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def vb_180_vb_025_volume_spike_ratio_378_025_accel_378(vb_155_vb_025_volume_spike_ratio_378_025_roc_378):
    feature = _s(vb_155_vb_025_volume_spike_ratio_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















VOLUME_BLOWOFF_REGISTRY_3RD_DERIVATIVES = {
    'vb_176_vb_001_volume_spike_ratio_5_001_accel_1': {'inputs': ['vb_151_vb_001_volume_spike_ratio_5_001_roc_1'], 'func': vb_176_vb_001_volume_spike_ratio_5_001_accel_1},
    'vb_177_vb_007_volume_spike_ratio_126_007_accel_5': {'inputs': ['vb_152_vb_007_volume_spike_ratio_126_007_roc_5'], 'func': vb_177_vb_007_volume_spike_ratio_126_007_accel_5},
    'vb_178_vb_013_volume_spike_ratio_1008_013_accel_42': {'inputs': ['vb_153_vb_013_volume_spike_ratio_1008_013_roc_42'], 'func': vb_178_vb_013_volume_spike_ratio_1008_013_accel_42},
    'vb_179_vb_019_volume_spike_ratio_42_019_accel_126': {'inputs': ['vb_154_vb_019_volume_spike_ratio_42_019_roc_126'], 'func': vb_179_vb_019_volume_spike_ratio_42_019_accel_126},
    'vb_180_vb_025_volume_spike_ratio_378_025_accel_378': {'inputs': ['vb_155_vb_025_volume_spike_ratio_378_025_roc_378'], 'func': vb_180_vb_025_volume_spike_ratio_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def vb_replacement_d3_001(vb_replacement_d2_001):
    feature = _clean(vb_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_001'] = {'inputs': ['vb_replacement_d2_001'], 'func': vb_replacement_d3_001}


def vb_replacement_d3_002(vb_replacement_d2_002):
    feature = _clean(vb_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_002'] = {'inputs': ['vb_replacement_d2_002'], 'func': vb_replacement_d3_002}


def vb_replacement_d3_003(vb_replacement_d2_003):
    feature = _clean(vb_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_003'] = {'inputs': ['vb_replacement_d2_003'], 'func': vb_replacement_d3_003}


def vb_replacement_d3_004(vb_replacement_d2_004):
    feature = _clean(vb_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_004'] = {'inputs': ['vb_replacement_d2_004'], 'func': vb_replacement_d3_004}


def vb_replacement_d3_005(vb_replacement_d2_005):
    feature = _clean(vb_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_005'] = {'inputs': ['vb_replacement_d2_005'], 'func': vb_replacement_d3_005}


def vb_replacement_d3_006(vb_replacement_d2_006):
    feature = _clean(vb_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_006'] = {'inputs': ['vb_replacement_d2_006'], 'func': vb_replacement_d3_006}


def vb_replacement_d3_007(vb_replacement_d2_007):
    feature = _clean(vb_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_007'] = {'inputs': ['vb_replacement_d2_007'], 'func': vb_replacement_d3_007}


def vb_replacement_d3_008(vb_replacement_d2_008):
    feature = _clean(vb_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_008'] = {'inputs': ['vb_replacement_d2_008'], 'func': vb_replacement_d3_008}


def vb_replacement_d3_009(vb_replacement_d2_009):
    feature = _clean(vb_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_009'] = {'inputs': ['vb_replacement_d2_009'], 'func': vb_replacement_d3_009}


def vb_replacement_d3_010(vb_replacement_d2_010):
    feature = _clean(vb_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_010'] = {'inputs': ['vb_replacement_d2_010'], 'func': vb_replacement_d3_010}


def vb_replacement_d3_011(vb_replacement_d2_011):
    feature = _clean(vb_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_011'] = {'inputs': ['vb_replacement_d2_011'], 'func': vb_replacement_d3_011}


def vb_replacement_d3_012(vb_replacement_d2_012):
    feature = _clean(vb_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_012'] = {'inputs': ['vb_replacement_d2_012'], 'func': vb_replacement_d3_012}


def vb_replacement_d3_013(vb_replacement_d2_013):
    feature = _clean(vb_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_013'] = {'inputs': ['vb_replacement_d2_013'], 'func': vb_replacement_d3_013}


def vb_replacement_d3_014(vb_replacement_d2_014):
    feature = _clean(vb_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_014'] = {'inputs': ['vb_replacement_d2_014'], 'func': vb_replacement_d3_014}


def vb_replacement_d3_015(vb_replacement_d2_015):
    feature = _clean(vb_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_015'] = {'inputs': ['vb_replacement_d2_015'], 'func': vb_replacement_d3_015}


def vb_replacement_d3_016(vb_replacement_d2_016):
    feature = _clean(vb_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_016'] = {'inputs': ['vb_replacement_d2_016'], 'func': vb_replacement_d3_016}


def vb_replacement_d3_017(vb_replacement_d2_017):
    feature = _clean(vb_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_017'] = {'inputs': ['vb_replacement_d2_017'], 'func': vb_replacement_d3_017}


def vb_replacement_d3_018(vb_replacement_d2_018):
    feature = _clean(vb_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_018'] = {'inputs': ['vb_replacement_d2_018'], 'func': vb_replacement_d3_018}


def vb_replacement_d3_019(vb_replacement_d2_019):
    feature = _clean(vb_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_019'] = {'inputs': ['vb_replacement_d2_019'], 'func': vb_replacement_d3_019}


def vb_replacement_d3_020(vb_replacement_d2_020):
    feature = _clean(vb_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_020'] = {'inputs': ['vb_replacement_d2_020'], 'func': vb_replacement_d3_020}


def vb_replacement_d3_021(vb_replacement_d2_021):
    feature = _clean(vb_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_021'] = {'inputs': ['vb_replacement_d2_021'], 'func': vb_replacement_d3_021}


def vb_replacement_d3_022(vb_replacement_d2_022):
    feature = _clean(vb_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_022'] = {'inputs': ['vb_replacement_d2_022'], 'func': vb_replacement_d3_022}


def vb_replacement_d3_023(vb_replacement_d2_023):
    feature = _clean(vb_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_023'] = {'inputs': ['vb_replacement_d2_023'], 'func': vb_replacement_d3_023}


def vb_replacement_d3_024(vb_replacement_d2_024):
    feature = _clean(vb_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_024'] = {'inputs': ['vb_replacement_d2_024'], 'func': vb_replacement_d3_024}


def vb_replacement_d3_025(vb_replacement_d2_025):
    feature = _clean(vb_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_025'] = {'inputs': ['vb_replacement_d2_025'], 'func': vb_replacement_d3_025}


def vb_replacement_d3_026(vb_replacement_d2_026):
    feature = _clean(vb_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_026'] = {'inputs': ['vb_replacement_d2_026'], 'func': vb_replacement_d3_026}


def vb_replacement_d3_027(vb_replacement_d2_027):
    feature = _clean(vb_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_027'] = {'inputs': ['vb_replacement_d2_027'], 'func': vb_replacement_d3_027}


def vb_replacement_d3_028(vb_replacement_d2_028):
    feature = _clean(vb_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_028'] = {'inputs': ['vb_replacement_d2_028'], 'func': vb_replacement_d3_028}


def vb_replacement_d3_029(vb_replacement_d2_029):
    feature = _clean(vb_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_029'] = {'inputs': ['vb_replacement_d2_029'], 'func': vb_replacement_d3_029}


def vb_replacement_d3_030(vb_replacement_d2_030):
    feature = _clean(vb_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_030'] = {'inputs': ['vb_replacement_d2_030'], 'func': vb_replacement_d3_030}


def vb_replacement_d3_031(vb_replacement_d2_031):
    feature = _clean(vb_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_031'] = {'inputs': ['vb_replacement_d2_031'], 'func': vb_replacement_d3_031}


def vb_replacement_d3_032(vb_replacement_d2_032):
    feature = _clean(vb_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_032'] = {'inputs': ['vb_replacement_d2_032'], 'func': vb_replacement_d3_032}


def vb_replacement_d3_033(vb_replacement_d2_033):
    feature = _clean(vb_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_033'] = {'inputs': ['vb_replacement_d2_033'], 'func': vb_replacement_d3_033}


def vb_replacement_d3_034(vb_replacement_d2_034):
    feature = _clean(vb_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_034'] = {'inputs': ['vb_replacement_d2_034'], 'func': vb_replacement_d3_034}


def vb_replacement_d3_035(vb_replacement_d2_035):
    feature = _clean(vb_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_035'] = {'inputs': ['vb_replacement_d2_035'], 'func': vb_replacement_d3_035}


def vb_replacement_d3_036(vb_replacement_d2_036):
    feature = _clean(vb_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_036'] = {'inputs': ['vb_replacement_d2_036'], 'func': vb_replacement_d3_036}


def vb_replacement_d3_037(vb_replacement_d2_037):
    feature = _clean(vb_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_037'] = {'inputs': ['vb_replacement_d2_037'], 'func': vb_replacement_d3_037}


def vb_replacement_d3_038(vb_replacement_d2_038):
    feature = _clean(vb_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_038'] = {'inputs': ['vb_replacement_d2_038'], 'func': vb_replacement_d3_038}


def vb_replacement_d3_039(vb_replacement_d2_039):
    feature = _clean(vb_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_039'] = {'inputs': ['vb_replacement_d2_039'], 'func': vb_replacement_d3_039}


def vb_replacement_d3_040(vb_replacement_d2_040):
    feature = _clean(vb_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_040'] = {'inputs': ['vb_replacement_d2_040'], 'func': vb_replacement_d3_040}


def vb_replacement_d3_041(vb_replacement_d2_041):
    feature = _clean(vb_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_041'] = {'inputs': ['vb_replacement_d2_041'], 'func': vb_replacement_d3_041}


def vb_replacement_d3_042(vb_replacement_d2_042):
    feature = _clean(vb_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_042'] = {'inputs': ['vb_replacement_d2_042'], 'func': vb_replacement_d3_042}


def vb_replacement_d3_043(vb_replacement_d2_043):
    feature = _clean(vb_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_043'] = {'inputs': ['vb_replacement_d2_043'], 'func': vb_replacement_d3_043}


def vb_replacement_d3_044(vb_replacement_d2_044):
    feature = _clean(vb_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_044'] = {'inputs': ['vb_replacement_d2_044'], 'func': vb_replacement_d3_044}


def vb_replacement_d3_045(vb_replacement_d2_045):
    feature = _clean(vb_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_045'] = {'inputs': ['vb_replacement_d2_045'], 'func': vb_replacement_d3_045}


def vb_replacement_d3_046(vb_replacement_d2_046):
    feature = _clean(vb_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_046'] = {'inputs': ['vb_replacement_d2_046'], 'func': vb_replacement_d3_046}


def vb_replacement_d3_047(vb_replacement_d2_047):
    feature = _clean(vb_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_047'] = {'inputs': ['vb_replacement_d2_047'], 'func': vb_replacement_d3_047}


def vb_replacement_d3_048(vb_replacement_d2_048):
    feature = _clean(vb_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_048'] = {'inputs': ['vb_replacement_d2_048'], 'func': vb_replacement_d3_048}


def vb_replacement_d3_049(vb_replacement_d2_049):
    feature = _clean(vb_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_049'] = {'inputs': ['vb_replacement_d2_049'], 'func': vb_replacement_d3_049}


def vb_replacement_d3_050(vb_replacement_d2_050):
    feature = _clean(vb_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_050'] = {'inputs': ['vb_replacement_d2_050'], 'func': vb_replacement_d3_050}


def vb_replacement_d3_051(vb_replacement_d2_051):
    feature = _clean(vb_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_051'] = {'inputs': ['vb_replacement_d2_051'], 'func': vb_replacement_d3_051}


def vb_replacement_d3_052(vb_replacement_d2_052):
    feature = _clean(vb_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_052'] = {'inputs': ['vb_replacement_d2_052'], 'func': vb_replacement_d3_052}


def vb_replacement_d3_053(vb_replacement_d2_053):
    feature = _clean(vb_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_053'] = {'inputs': ['vb_replacement_d2_053'], 'func': vb_replacement_d3_053}


def vb_replacement_d3_054(vb_replacement_d2_054):
    feature = _clean(vb_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_054'] = {'inputs': ['vb_replacement_d2_054'], 'func': vb_replacement_d3_054}


def vb_replacement_d3_055(vb_replacement_d2_055):
    feature = _clean(vb_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_055'] = {'inputs': ['vb_replacement_d2_055'], 'func': vb_replacement_d3_055}


def vb_replacement_d3_056(vb_replacement_d2_056):
    feature = _clean(vb_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_056'] = {'inputs': ['vb_replacement_d2_056'], 'func': vb_replacement_d3_056}


def vb_replacement_d3_057(vb_replacement_d2_057):
    feature = _clean(vb_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_057'] = {'inputs': ['vb_replacement_d2_057'], 'func': vb_replacement_d3_057}


def vb_replacement_d3_058(vb_replacement_d2_058):
    feature = _clean(vb_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_058'] = {'inputs': ['vb_replacement_d2_058'], 'func': vb_replacement_d3_058}


def vb_replacement_d3_059(vb_replacement_d2_059):
    feature = _clean(vb_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_059'] = {'inputs': ['vb_replacement_d2_059'], 'func': vb_replacement_d3_059}


def vb_replacement_d3_060(vb_replacement_d2_060):
    feature = _clean(vb_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_060'] = {'inputs': ['vb_replacement_d2_060'], 'func': vb_replacement_d3_060}


def vb_replacement_d3_061(vb_replacement_d2_061):
    feature = _clean(vb_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_061'] = {'inputs': ['vb_replacement_d2_061'], 'func': vb_replacement_d3_061}


def vb_replacement_d3_062(vb_replacement_d2_062):
    feature = _clean(vb_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_062'] = {'inputs': ['vb_replacement_d2_062'], 'func': vb_replacement_d3_062}


def vb_replacement_d3_063(vb_replacement_d2_063):
    feature = _clean(vb_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_063'] = {'inputs': ['vb_replacement_d2_063'], 'func': vb_replacement_d3_063}


def vb_replacement_d3_064(vb_replacement_d2_064):
    feature = _clean(vb_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_064'] = {'inputs': ['vb_replacement_d2_064'], 'func': vb_replacement_d3_064}


def vb_replacement_d3_065(vb_replacement_d2_065):
    feature = _clean(vb_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_065'] = {'inputs': ['vb_replacement_d2_065'], 'func': vb_replacement_d3_065}


def vb_replacement_d3_066(vb_replacement_d2_066):
    feature = _clean(vb_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_066'] = {'inputs': ['vb_replacement_d2_066'], 'func': vb_replacement_d3_066}


def vb_replacement_d3_067(vb_replacement_d2_067):
    feature = _clean(vb_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_067'] = {'inputs': ['vb_replacement_d2_067'], 'func': vb_replacement_d3_067}


def vb_replacement_d3_068(vb_replacement_d2_068):
    feature = _clean(vb_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_068'] = {'inputs': ['vb_replacement_d2_068'], 'func': vb_replacement_d3_068}


def vb_replacement_d3_069(vb_replacement_d2_069):
    feature = _clean(vb_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_069'] = {'inputs': ['vb_replacement_d2_069'], 'func': vb_replacement_d3_069}


def vb_replacement_d3_070(vb_replacement_d2_070):
    feature = _clean(vb_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_070'] = {'inputs': ['vb_replacement_d2_070'], 'func': vb_replacement_d3_070}


def vb_replacement_d3_071(vb_replacement_d2_071):
    feature = _clean(vb_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_071'] = {'inputs': ['vb_replacement_d2_071'], 'func': vb_replacement_d3_071}


def vb_replacement_d3_072(vb_replacement_d2_072):
    feature = _clean(vb_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_072'] = {'inputs': ['vb_replacement_d2_072'], 'func': vb_replacement_d3_072}


def vb_replacement_d3_073(vb_replacement_d2_073):
    feature = _clean(vb_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_073'] = {'inputs': ['vb_replacement_d2_073'], 'func': vb_replacement_d3_073}


def vb_replacement_d3_074(vb_replacement_d2_074):
    feature = _clean(vb_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_074'] = {'inputs': ['vb_replacement_d2_074'], 'func': vb_replacement_d3_074}


def vb_replacement_d3_075(vb_replacement_d2_075):
    feature = _clean(vb_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_075'] = {'inputs': ['vb_replacement_d2_075'], 'func': vb_replacement_d3_075}


def vb_replacement_d3_076(vb_replacement_d2_076):
    feature = _clean(vb_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_076'] = {'inputs': ['vb_replacement_d2_076'], 'func': vb_replacement_d3_076}


def vb_replacement_d3_077(vb_replacement_d2_077):
    feature = _clean(vb_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_077'] = {'inputs': ['vb_replacement_d2_077'], 'func': vb_replacement_d3_077}


def vb_replacement_d3_078(vb_replacement_d2_078):
    feature = _clean(vb_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_078'] = {'inputs': ['vb_replacement_d2_078'], 'func': vb_replacement_d3_078}


def vb_replacement_d3_079(vb_replacement_d2_079):
    feature = _clean(vb_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_079'] = {'inputs': ['vb_replacement_d2_079'], 'func': vb_replacement_d3_079}


def vb_replacement_d3_080(vb_replacement_d2_080):
    feature = _clean(vb_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_080'] = {'inputs': ['vb_replacement_d2_080'], 'func': vb_replacement_d3_080}


def vb_replacement_d3_081(vb_replacement_d2_081):
    feature = _clean(vb_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_081'] = {'inputs': ['vb_replacement_d2_081'], 'func': vb_replacement_d3_081}


def vb_replacement_d3_082(vb_replacement_d2_082):
    feature = _clean(vb_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_082'] = {'inputs': ['vb_replacement_d2_082'], 'func': vb_replacement_d3_082}


def vb_replacement_d3_083(vb_replacement_d2_083):
    feature = _clean(vb_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_083'] = {'inputs': ['vb_replacement_d2_083'], 'func': vb_replacement_d3_083}


def vb_replacement_d3_084(vb_replacement_d2_084):
    feature = _clean(vb_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_084'] = {'inputs': ['vb_replacement_d2_084'], 'func': vb_replacement_d3_084}


def vb_replacement_d3_085(vb_replacement_d2_085):
    feature = _clean(vb_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_085'] = {'inputs': ['vb_replacement_d2_085'], 'func': vb_replacement_d3_085}


def vb_replacement_d3_086(vb_replacement_d2_086):
    feature = _clean(vb_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_086'] = {'inputs': ['vb_replacement_d2_086'], 'func': vb_replacement_d3_086}


def vb_replacement_d3_087(vb_replacement_d2_087):
    feature = _clean(vb_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_087'] = {'inputs': ['vb_replacement_d2_087'], 'func': vb_replacement_d3_087}


def vb_replacement_d3_088(vb_replacement_d2_088):
    feature = _clean(vb_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_088'] = {'inputs': ['vb_replacement_d2_088'], 'func': vb_replacement_d3_088}


def vb_replacement_d3_089(vb_replacement_d2_089):
    feature = _clean(vb_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_089'] = {'inputs': ['vb_replacement_d2_089'], 'func': vb_replacement_d3_089}


def vb_replacement_d3_090(vb_replacement_d2_090):
    feature = _clean(vb_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_090'] = {'inputs': ['vb_replacement_d2_090'], 'func': vb_replacement_d3_090}


def vb_replacement_d3_091(vb_replacement_d2_091):
    feature = _clean(vb_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_091'] = {'inputs': ['vb_replacement_d2_091'], 'func': vb_replacement_d3_091}


def vb_replacement_d3_092(vb_replacement_d2_092):
    feature = _clean(vb_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_092'] = {'inputs': ['vb_replacement_d2_092'], 'func': vb_replacement_d3_092}


def vb_replacement_d3_093(vb_replacement_d2_093):
    feature = _clean(vb_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_093'] = {'inputs': ['vb_replacement_d2_093'], 'func': vb_replacement_d3_093}


def vb_replacement_d3_094(vb_replacement_d2_094):
    feature = _clean(vb_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_094'] = {'inputs': ['vb_replacement_d2_094'], 'func': vb_replacement_d3_094}


def vb_replacement_d3_095(vb_replacement_d2_095):
    feature = _clean(vb_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_095'] = {'inputs': ['vb_replacement_d2_095'], 'func': vb_replacement_d3_095}


def vb_replacement_d3_096(vb_replacement_d2_096):
    feature = _clean(vb_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_096'] = {'inputs': ['vb_replacement_d2_096'], 'func': vb_replacement_d3_096}


def vb_replacement_d3_097(vb_replacement_d2_097):
    feature = _clean(vb_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_097'] = {'inputs': ['vb_replacement_d2_097'], 'func': vb_replacement_d3_097}


def vb_replacement_d3_098(vb_replacement_d2_098):
    feature = _clean(vb_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_098'] = {'inputs': ['vb_replacement_d2_098'], 'func': vb_replacement_d3_098}


def vb_replacement_d3_099(vb_replacement_d2_099):
    feature = _clean(vb_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_099'] = {'inputs': ['vb_replacement_d2_099'], 'func': vb_replacement_d3_099}


def vb_replacement_d3_100(vb_replacement_d2_100):
    feature = _clean(vb_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_100'] = {'inputs': ['vb_replacement_d2_100'], 'func': vb_replacement_d3_100}


def vb_replacement_d3_101(vb_replacement_d2_101):
    feature = _clean(vb_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_101'] = {'inputs': ['vb_replacement_d2_101'], 'func': vb_replacement_d3_101}


def vb_replacement_d3_102(vb_replacement_d2_102):
    feature = _clean(vb_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_102'] = {'inputs': ['vb_replacement_d2_102'], 'func': vb_replacement_d3_102}


def vb_replacement_d3_103(vb_replacement_d2_103):
    feature = _clean(vb_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_103'] = {'inputs': ['vb_replacement_d2_103'], 'func': vb_replacement_d3_103}


def vb_replacement_d3_104(vb_replacement_d2_104):
    feature = _clean(vb_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_104'] = {'inputs': ['vb_replacement_d2_104'], 'func': vb_replacement_d3_104}


def vb_replacement_d3_105(vb_replacement_d2_105):
    feature = _clean(vb_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_105'] = {'inputs': ['vb_replacement_d2_105'], 'func': vb_replacement_d3_105}


def vb_replacement_d3_106(vb_replacement_d2_106):
    feature = _clean(vb_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_106'] = {'inputs': ['vb_replacement_d2_106'], 'func': vb_replacement_d3_106}


def vb_replacement_d3_107(vb_replacement_d2_107):
    feature = _clean(vb_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_107'] = {'inputs': ['vb_replacement_d2_107'], 'func': vb_replacement_d3_107}


def vb_replacement_d3_108(vb_replacement_d2_108):
    feature = _clean(vb_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_108'] = {'inputs': ['vb_replacement_d2_108'], 'func': vb_replacement_d3_108}


def vb_replacement_d3_109(vb_replacement_d2_109):
    feature = _clean(vb_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_109'] = {'inputs': ['vb_replacement_d2_109'], 'func': vb_replacement_d3_109}


def vb_replacement_d3_110(vb_replacement_d2_110):
    feature = _clean(vb_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_110'] = {'inputs': ['vb_replacement_d2_110'], 'func': vb_replacement_d3_110}


def vb_replacement_d3_111(vb_replacement_d2_111):
    feature = _clean(vb_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_111'] = {'inputs': ['vb_replacement_d2_111'], 'func': vb_replacement_d3_111}


def vb_replacement_d3_112(vb_replacement_d2_112):
    feature = _clean(vb_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_112'] = {'inputs': ['vb_replacement_d2_112'], 'func': vb_replacement_d3_112}


def vb_replacement_d3_113(vb_replacement_d2_113):
    feature = _clean(vb_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_113'] = {'inputs': ['vb_replacement_d2_113'], 'func': vb_replacement_d3_113}


def vb_replacement_d3_114(vb_replacement_d2_114):
    feature = _clean(vb_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_114'] = {'inputs': ['vb_replacement_d2_114'], 'func': vb_replacement_d3_114}


def vb_replacement_d3_115(vb_replacement_d2_115):
    feature = _clean(vb_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_115'] = {'inputs': ['vb_replacement_d2_115'], 'func': vb_replacement_d3_115}


def vb_replacement_d3_116(vb_replacement_d2_116):
    feature = _clean(vb_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_116'] = {'inputs': ['vb_replacement_d2_116'], 'func': vb_replacement_d3_116}


def vb_replacement_d3_117(vb_replacement_d2_117):
    feature = _clean(vb_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_117'] = {'inputs': ['vb_replacement_d2_117'], 'func': vb_replacement_d3_117}


def vb_replacement_d3_118(vb_replacement_d2_118):
    feature = _clean(vb_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_118'] = {'inputs': ['vb_replacement_d2_118'], 'func': vb_replacement_d3_118}


def vb_replacement_d3_119(vb_replacement_d2_119):
    feature = _clean(vb_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_119'] = {'inputs': ['vb_replacement_d2_119'], 'func': vb_replacement_d3_119}


def vb_replacement_d3_120(vb_replacement_d2_120):
    feature = _clean(vb_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_120'] = {'inputs': ['vb_replacement_d2_120'], 'func': vb_replacement_d3_120}


def vb_replacement_d3_121(vb_replacement_d2_121):
    feature = _clean(vb_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_121'] = {'inputs': ['vb_replacement_d2_121'], 'func': vb_replacement_d3_121}


def vb_replacement_d3_122(vb_replacement_d2_122):
    feature = _clean(vb_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_122'] = {'inputs': ['vb_replacement_d2_122'], 'func': vb_replacement_d3_122}


def vb_replacement_d3_123(vb_replacement_d2_123):
    feature = _clean(vb_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_123'] = {'inputs': ['vb_replacement_d2_123'], 'func': vb_replacement_d3_123}


def vb_replacement_d3_124(vb_replacement_d2_124):
    feature = _clean(vb_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_124'] = {'inputs': ['vb_replacement_d2_124'], 'func': vb_replacement_d3_124}


def vb_replacement_d3_125(vb_replacement_d2_125):
    feature = _clean(vb_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_125'] = {'inputs': ['vb_replacement_d2_125'], 'func': vb_replacement_d3_125}


def vb_replacement_d3_126(vb_replacement_d2_126):
    feature = _clean(vb_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_126'] = {'inputs': ['vb_replacement_d2_126'], 'func': vb_replacement_d3_126}


def vb_replacement_d3_127(vb_replacement_d2_127):
    feature = _clean(vb_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_127'] = {'inputs': ['vb_replacement_d2_127'], 'func': vb_replacement_d3_127}


def vb_replacement_d3_128(vb_replacement_d2_128):
    feature = _clean(vb_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_128'] = {'inputs': ['vb_replacement_d2_128'], 'func': vb_replacement_d3_128}


def vb_replacement_d3_129(vb_replacement_d2_129):
    feature = _clean(vb_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_129'] = {'inputs': ['vb_replacement_d2_129'], 'func': vb_replacement_d3_129}


def vb_replacement_d3_130(vb_replacement_d2_130):
    feature = _clean(vb_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_130'] = {'inputs': ['vb_replacement_d2_130'], 'func': vb_replacement_d3_130}


def vb_replacement_d3_131(vb_replacement_d2_131):
    feature = _clean(vb_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_131'] = {'inputs': ['vb_replacement_d2_131'], 'func': vb_replacement_d3_131}


def vb_replacement_d3_132(vb_replacement_d2_132):
    feature = _clean(vb_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_132'] = {'inputs': ['vb_replacement_d2_132'], 'func': vb_replacement_d3_132}


def vb_replacement_d3_133(vb_replacement_d2_133):
    feature = _clean(vb_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_133'] = {'inputs': ['vb_replacement_d2_133'], 'func': vb_replacement_d3_133}


def vb_replacement_d3_134(vb_replacement_d2_134):
    feature = _clean(vb_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_134'] = {'inputs': ['vb_replacement_d2_134'], 'func': vb_replacement_d3_134}


def vb_replacement_d3_135(vb_replacement_d2_135):
    feature = _clean(vb_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_135'] = {'inputs': ['vb_replacement_d2_135'], 'func': vb_replacement_d3_135}


def vb_replacement_d3_136(vb_replacement_d2_136):
    feature = _clean(vb_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_136'] = {'inputs': ['vb_replacement_d2_136'], 'func': vb_replacement_d3_136}


def vb_replacement_d3_137(vb_replacement_d2_137):
    feature = _clean(vb_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_137'] = {'inputs': ['vb_replacement_d2_137'], 'func': vb_replacement_d3_137}


def vb_replacement_d3_138(vb_replacement_d2_138):
    feature = _clean(vb_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_138'] = {'inputs': ['vb_replacement_d2_138'], 'func': vb_replacement_d3_138}


def vb_replacement_d3_139(vb_replacement_d2_139):
    feature = _clean(vb_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_139'] = {'inputs': ['vb_replacement_d2_139'], 'func': vb_replacement_d3_139}


def vb_replacement_d3_140(vb_replacement_d2_140):
    feature = _clean(vb_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_140'] = {'inputs': ['vb_replacement_d2_140'], 'func': vb_replacement_d3_140}


def vb_replacement_d3_141(vb_replacement_d2_141):
    feature = _clean(vb_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_141'] = {'inputs': ['vb_replacement_d2_141'], 'func': vb_replacement_d3_141}


def vb_replacement_d3_142(vb_replacement_d2_142):
    feature = _clean(vb_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_142'] = {'inputs': ['vb_replacement_d2_142'], 'func': vb_replacement_d3_142}


def vb_replacement_d3_143(vb_replacement_d2_143):
    feature = _clean(vb_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_143'] = {'inputs': ['vb_replacement_d2_143'], 'func': vb_replacement_d3_143}


def vb_replacement_d3_144(vb_replacement_d2_144):
    feature = _clean(vb_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_144'] = {'inputs': ['vb_replacement_d2_144'], 'func': vb_replacement_d3_144}


def vb_replacement_d3_145(vb_replacement_d2_145):
    feature = _clean(vb_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_145'] = {'inputs': ['vb_replacement_d2_145'], 'func': vb_replacement_d3_145}


def vb_replacement_d3_146(vb_replacement_d2_146):
    feature = _clean(vb_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_146'] = {'inputs': ['vb_replacement_d2_146'], 'func': vb_replacement_d3_146}


def vb_replacement_d3_147(vb_replacement_d2_147):
    feature = _clean(vb_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_147'] = {'inputs': ['vb_replacement_d2_147'], 'func': vb_replacement_d3_147}


def vb_replacement_d3_148(vb_replacement_d2_148):
    feature = _clean(vb_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_148'] = {'inputs': ['vb_replacement_d2_148'], 'func': vb_replacement_d3_148}


def vb_replacement_d3_149(vb_replacement_d2_149):
    feature = _clean(vb_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_149'] = {'inputs': ['vb_replacement_d2_149'], 'func': vb_replacement_d3_149}


def vb_replacement_d3_150(vb_replacement_d2_150):
    feature = _clean(vb_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_150'] = {'inputs': ['vb_replacement_d2_150'], 'func': vb_replacement_d3_150}


def vb_replacement_d3_151(vb_replacement_d2_151):
    feature = _clean(vb_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_151'] = {'inputs': ['vb_replacement_d2_151'], 'func': vb_replacement_d3_151}


def vb_replacement_d3_152(vb_replacement_d2_152):
    feature = _clean(vb_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_152'] = {'inputs': ['vb_replacement_d2_152'], 'func': vb_replacement_d3_152}


def vb_replacement_d3_153(vb_replacement_d2_153):
    feature = _clean(vb_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_153'] = {'inputs': ['vb_replacement_d2_153'], 'func': vb_replacement_d3_153}


def vb_replacement_d3_154(vb_replacement_d2_154):
    feature = _clean(vb_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_154'] = {'inputs': ['vb_replacement_d2_154'], 'func': vb_replacement_d3_154}


def vb_replacement_d3_155(vb_replacement_d2_155):
    feature = _clean(vb_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_155'] = {'inputs': ['vb_replacement_d2_155'], 'func': vb_replacement_d3_155}


def vb_replacement_d3_156(vb_replacement_d2_156):
    feature = _clean(vb_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_156'] = {'inputs': ['vb_replacement_d2_156'], 'func': vb_replacement_d3_156}


def vb_replacement_d3_157(vb_replacement_d2_157):
    feature = _clean(vb_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_157'] = {'inputs': ['vb_replacement_d2_157'], 'func': vb_replacement_d3_157}


def vb_replacement_d3_158(vb_replacement_d2_158):
    feature = _clean(vb_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_158'] = {'inputs': ['vb_replacement_d2_158'], 'func': vb_replacement_d3_158}


def vb_replacement_d3_159(vb_replacement_d2_159):
    feature = _clean(vb_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_159'] = {'inputs': ['vb_replacement_d2_159'], 'func': vb_replacement_d3_159}


def vb_replacement_d3_160(vb_replacement_d2_160):
    feature = _clean(vb_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
VB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vb_replacement_d3_160'] = {'inputs': ['vb_replacement_d2_160'], 'func': vb_replacement_d3_160}


# Third-derivative extensions for repaired first-base features.
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def vb_base_universe_d3_001_vb_002_volume_zscore_10_002(vb_base_universe_d2_001_vb_002_volume_zscore_10_002):
    return _base_universe_d3(vb_base_universe_d2_001_vb_002_volume_zscore_10_002, 1)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_001_vb_002_volume_zscore_10_002'] = {'inputs': ['vb_base_universe_d2_001_vb_002_volume_zscore_10_002'], 'func': vb_base_universe_d3_001_vb_002_volume_zscore_10_002}


def vb_base_universe_d3_002_vb_003_down_volume_share_21_003(vb_base_universe_d2_002_vb_003_down_volume_share_21_003):
    return _base_universe_d3(vb_base_universe_d2_002_vb_003_down_volume_share_21_003, 2)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_002_vb_003_down_volume_share_21_003'] = {'inputs': ['vb_base_universe_d2_002_vb_003_down_volume_share_21_003'], 'func': vb_base_universe_d3_002_vb_003_down_volume_share_21_003}


def vb_base_universe_d3_003_vb_004_dollar_volume_shock_42_004(vb_base_universe_d2_003_vb_004_dollar_volume_shock_42_004):
    return _base_universe_d3(vb_base_universe_d2_003_vb_004_dollar_volume_shock_42_004, 3)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_003_vb_004_dollar_volume_shock_42_004'] = {'inputs': ['vb_base_universe_d2_003_vb_004_dollar_volume_shock_42_004'], 'func': vb_base_universe_d3_003_vb_004_dollar_volume_shock_42_004}


def vb_base_universe_d3_004_vb_005_volume_trend_slope_63_005(vb_base_universe_d2_004_vb_005_volume_trend_slope_63_005):
    return _base_universe_d3(vb_base_universe_d2_004_vb_005_volume_trend_slope_63_005, 4)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_004_vb_005_volume_trend_slope_63_005'] = {'inputs': ['vb_base_universe_d2_004_vb_005_volume_trend_slope_63_005'], 'func': vb_base_universe_d3_004_vb_005_volume_trend_slope_63_005}


def vb_base_universe_d3_005_vb_006_price_volume_divergence_84_006(vb_base_universe_d2_005_vb_006_price_volume_divergence_84_006):
    return _base_universe_d3(vb_base_universe_d2_005_vb_006_price_volume_divergence_84_006, 5)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_005_vb_006_price_volume_divergence_84_006'] = {'inputs': ['vb_base_universe_d2_005_vb_006_price_volume_divergence_84_006'], 'func': vb_base_universe_d3_005_vb_006_price_volume_divergence_84_006}


def vb_base_universe_d3_006_vb_008_volume_zscore_189_008(vb_base_universe_d2_006_vb_008_volume_zscore_189_008):
    return _base_universe_d3(vb_base_universe_d2_006_vb_008_volume_zscore_189_008, 6)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_006_vb_008_volume_zscore_189_008'] = {'inputs': ['vb_base_universe_d2_006_vb_008_volume_zscore_189_008'], 'func': vb_base_universe_d3_006_vb_008_volume_zscore_189_008}


def vb_base_universe_d3_007_vb_009_down_volume_share_252_009(vb_base_universe_d2_007_vb_009_down_volume_share_252_009):
    return _base_universe_d3(vb_base_universe_d2_007_vb_009_down_volume_share_252_009, 7)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_007_vb_009_down_volume_share_252_009'] = {'inputs': ['vb_base_universe_d2_007_vb_009_down_volume_share_252_009'], 'func': vb_base_universe_d3_007_vb_009_down_volume_share_252_009}


def vb_base_universe_d3_008_vb_010_dollar_volume_shock_378_010(vb_base_universe_d2_008_vb_010_dollar_volume_shock_378_010):
    return _base_universe_d3(vb_base_universe_d2_008_vb_010_dollar_volume_shock_378_010, 8)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_008_vb_010_dollar_volume_shock_378_010'] = {'inputs': ['vb_base_universe_d2_008_vb_010_dollar_volume_shock_378_010'], 'func': vb_base_universe_d3_008_vb_010_dollar_volume_shock_378_010}


def vb_base_universe_d3_009_vb_011_volume_trend_slope_504_011(vb_base_universe_d2_009_vb_011_volume_trend_slope_504_011):
    return _base_universe_d3(vb_base_universe_d2_009_vb_011_volume_trend_slope_504_011, 9)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_009_vb_011_volume_trend_slope_504_011'] = {'inputs': ['vb_base_universe_d2_009_vb_011_volume_trend_slope_504_011'], 'func': vb_base_universe_d3_009_vb_011_volume_trend_slope_504_011}


def vb_base_universe_d3_010_vb_012_price_volume_divergence_756_012(vb_base_universe_d2_010_vb_012_price_volume_divergence_756_012):
    return _base_universe_d3(vb_base_universe_d2_010_vb_012_price_volume_divergence_756_012, 10)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_010_vb_012_price_volume_divergence_756_012'] = {'inputs': ['vb_base_universe_d2_010_vb_012_price_volume_divergence_756_012'], 'func': vb_base_universe_d3_010_vb_012_price_volume_divergence_756_012}


def vb_base_universe_d3_011_vb_014_volume_zscore_1260_014(vb_base_universe_d2_011_vb_014_volume_zscore_1260_014):
    return _base_universe_d3(vb_base_universe_d2_011_vb_014_volume_zscore_1260_014, 11)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_011_vb_014_volume_zscore_1260_014'] = {'inputs': ['vb_base_universe_d2_011_vb_014_volume_zscore_1260_014'], 'func': vb_base_universe_d3_011_vb_014_volume_zscore_1260_014}


def vb_base_universe_d3_012_vb_015_down_volume_share_1512_015(vb_base_universe_d2_012_vb_015_down_volume_share_1512_015):
    return _base_universe_d3(vb_base_universe_d2_012_vb_015_down_volume_share_1512_015, 12)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_012_vb_015_down_volume_share_1512_015'] = {'inputs': ['vb_base_universe_d2_012_vb_015_down_volume_share_1512_015'], 'func': vb_base_universe_d3_012_vb_015_down_volume_share_1512_015}


def vb_base_universe_d3_013_vb_016_dollar_volume_shock_5_016(vb_base_universe_d2_013_vb_016_dollar_volume_shock_5_016):
    return _base_universe_d3(vb_base_universe_d2_013_vb_016_dollar_volume_shock_5_016, 13)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_013_vb_016_dollar_volume_shock_5_016'] = {'inputs': ['vb_base_universe_d2_013_vb_016_dollar_volume_shock_5_016'], 'func': vb_base_universe_d3_013_vb_016_dollar_volume_shock_5_016}


def vb_base_universe_d3_014_vb_017_volume_trend_slope_10_017(vb_base_universe_d2_014_vb_017_volume_trend_slope_10_017):
    return _base_universe_d3(vb_base_universe_d2_014_vb_017_volume_trend_slope_10_017, 14)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_014_vb_017_volume_trend_slope_10_017'] = {'inputs': ['vb_base_universe_d2_014_vb_017_volume_trend_slope_10_017'], 'func': vb_base_universe_d3_014_vb_017_volume_trend_slope_10_017}


def vb_base_universe_d3_015_vb_018_price_volume_divergence_21_018(vb_base_universe_d2_015_vb_018_price_volume_divergence_21_018):
    return _base_universe_d3(vb_base_universe_d2_015_vb_018_price_volume_divergence_21_018, 15)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_015_vb_018_price_volume_divergence_21_018'] = {'inputs': ['vb_base_universe_d2_015_vb_018_price_volume_divergence_21_018'], 'func': vb_base_universe_d3_015_vb_018_price_volume_divergence_21_018}


def vb_base_universe_d3_016_vb_020_volume_zscore_63_020(vb_base_universe_d2_016_vb_020_volume_zscore_63_020):
    return _base_universe_d3(vb_base_universe_d2_016_vb_020_volume_zscore_63_020, 16)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_016_vb_020_volume_zscore_63_020'] = {'inputs': ['vb_base_universe_d2_016_vb_020_volume_zscore_63_020'], 'func': vb_base_universe_d3_016_vb_020_volume_zscore_63_020}


def vb_base_universe_d3_017_vb_021_down_volume_share_84_021(vb_base_universe_d2_017_vb_021_down_volume_share_84_021):
    return _base_universe_d3(vb_base_universe_d2_017_vb_021_down_volume_share_84_021, 17)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_017_vb_021_down_volume_share_84_021'] = {'inputs': ['vb_base_universe_d2_017_vb_021_down_volume_share_84_021'], 'func': vb_base_universe_d3_017_vb_021_down_volume_share_84_021}


def vb_base_universe_d3_018_vb_022_dollar_volume_shock_126_022(vb_base_universe_d2_018_vb_022_dollar_volume_shock_126_022):
    return _base_universe_d3(vb_base_universe_d2_018_vb_022_dollar_volume_shock_126_022, 18)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_018_vb_022_dollar_volume_shock_126_022'] = {'inputs': ['vb_base_universe_d2_018_vb_022_dollar_volume_shock_126_022'], 'func': vb_base_universe_d3_018_vb_022_dollar_volume_shock_126_022}


def vb_base_universe_d3_019_vb_023_volume_trend_slope_189_023(vb_base_universe_d2_019_vb_023_volume_trend_slope_189_023):
    return _base_universe_d3(vb_base_universe_d2_019_vb_023_volume_trend_slope_189_023, 19)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_019_vb_023_volume_trend_slope_189_023'] = {'inputs': ['vb_base_universe_d2_019_vb_023_volume_trend_slope_189_023'], 'func': vb_base_universe_d3_019_vb_023_volume_trend_slope_189_023}


def vb_base_universe_d3_020_vb_024_price_volume_divergence_252_024(vb_base_universe_d2_020_vb_024_price_volume_divergence_252_024):
    return _base_universe_d3(vb_base_universe_d2_020_vb_024_price_volume_divergence_252_024, 20)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_020_vb_024_price_volume_divergence_252_024'] = {'inputs': ['vb_base_universe_d2_020_vb_024_price_volume_divergence_252_024'], 'func': vb_base_universe_d3_020_vb_024_price_volume_divergence_252_024}


def vb_base_universe_d3_021_vb_026_volume_zscore_504_026(vb_base_universe_d2_021_vb_026_volume_zscore_504_026):
    return _base_universe_d3(vb_base_universe_d2_021_vb_026_volume_zscore_504_026, 21)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_021_vb_026_volume_zscore_504_026'] = {'inputs': ['vb_base_universe_d2_021_vb_026_volume_zscore_504_026'], 'func': vb_base_universe_d3_021_vb_026_volume_zscore_504_026}


def vb_base_universe_d3_022_vb_027_down_volume_share_756_027(vb_base_universe_d2_022_vb_027_down_volume_share_756_027):
    return _base_universe_d3(vb_base_universe_d2_022_vb_027_down_volume_share_756_027, 22)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_022_vb_027_down_volume_share_756_027'] = {'inputs': ['vb_base_universe_d2_022_vb_027_down_volume_share_756_027'], 'func': vb_base_universe_d3_022_vb_027_down_volume_share_756_027}


def vb_base_universe_d3_023_vb_028_dollar_volume_shock_1008_028(vb_base_universe_d2_023_vb_028_dollar_volume_shock_1008_028):
    return _base_universe_d3(vb_base_universe_d2_023_vb_028_dollar_volume_shock_1008_028, 23)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_023_vb_028_dollar_volume_shock_1008_028'] = {'inputs': ['vb_base_universe_d2_023_vb_028_dollar_volume_shock_1008_028'], 'func': vb_base_universe_d3_023_vb_028_dollar_volume_shock_1008_028}


def vb_base_universe_d3_024_vb_029_volume_trend_slope_1260_029(vb_base_universe_d2_024_vb_029_volume_trend_slope_1260_029):
    return _base_universe_d3(vb_base_universe_d2_024_vb_029_volume_trend_slope_1260_029, 24)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_024_vb_029_volume_trend_slope_1260_029'] = {'inputs': ['vb_base_universe_d2_024_vb_029_volume_trend_slope_1260_029'], 'func': vb_base_universe_d3_024_vb_029_volume_trend_slope_1260_029}


def vb_base_universe_d3_025_vb_030_price_volume_divergence_1512_030(vb_base_universe_d2_025_vb_030_price_volume_divergence_1512_030):
    return _base_universe_d3(vb_base_universe_d2_025_vb_030_price_volume_divergence_1512_030, 25)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_025_vb_030_price_volume_divergence_1512_030'] = {'inputs': ['vb_base_universe_d2_025_vb_030_price_volume_divergence_1512_030'], 'func': vb_base_universe_d3_025_vb_030_price_volume_divergence_1512_030}


def vb_base_universe_d3_026_vb_basefill_031(vb_base_universe_d2_026_vb_basefill_031):
    return _base_universe_d3(vb_base_universe_d2_026_vb_basefill_031, 26)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_026_vb_basefill_031'] = {'inputs': ['vb_base_universe_d2_026_vb_basefill_031'], 'func': vb_base_universe_d3_026_vb_basefill_031}


def vb_base_universe_d3_027_vb_basefill_032(vb_base_universe_d2_027_vb_basefill_032):
    return _base_universe_d3(vb_base_universe_d2_027_vb_basefill_032, 27)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_027_vb_basefill_032'] = {'inputs': ['vb_base_universe_d2_027_vb_basefill_032'], 'func': vb_base_universe_d3_027_vb_basefill_032}


def vb_base_universe_d3_028_vb_basefill_033(vb_base_universe_d2_028_vb_basefill_033):
    return _base_universe_d3(vb_base_universe_d2_028_vb_basefill_033, 28)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_028_vb_basefill_033'] = {'inputs': ['vb_base_universe_d2_028_vb_basefill_033'], 'func': vb_base_universe_d3_028_vb_basefill_033}


def vb_base_universe_d3_029_vb_basefill_034(vb_base_universe_d2_029_vb_basefill_034):
    return _base_universe_d3(vb_base_universe_d2_029_vb_basefill_034, 29)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_029_vb_basefill_034'] = {'inputs': ['vb_base_universe_d2_029_vb_basefill_034'], 'func': vb_base_universe_d3_029_vb_basefill_034}


def vb_base_universe_d3_030_vb_basefill_035(vb_base_universe_d2_030_vb_basefill_035):
    return _base_universe_d3(vb_base_universe_d2_030_vb_basefill_035, 30)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_030_vb_basefill_035'] = {'inputs': ['vb_base_universe_d2_030_vb_basefill_035'], 'func': vb_base_universe_d3_030_vb_basefill_035}


def vb_base_universe_d3_031_vb_basefill_036(vb_base_universe_d2_031_vb_basefill_036):
    return _base_universe_d3(vb_base_universe_d2_031_vb_basefill_036, 31)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_031_vb_basefill_036'] = {'inputs': ['vb_base_universe_d2_031_vb_basefill_036'], 'func': vb_base_universe_d3_031_vb_basefill_036}


def vb_base_universe_d3_032_vb_basefill_037(vb_base_universe_d2_032_vb_basefill_037):
    return _base_universe_d3(vb_base_universe_d2_032_vb_basefill_037, 32)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_032_vb_basefill_037'] = {'inputs': ['vb_base_universe_d2_032_vb_basefill_037'], 'func': vb_base_universe_d3_032_vb_basefill_037}


def vb_base_universe_d3_033_vb_basefill_038(vb_base_universe_d2_033_vb_basefill_038):
    return _base_universe_d3(vb_base_universe_d2_033_vb_basefill_038, 33)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_033_vb_basefill_038'] = {'inputs': ['vb_base_universe_d2_033_vb_basefill_038'], 'func': vb_base_universe_d3_033_vb_basefill_038}


def vb_base_universe_d3_034_vb_basefill_039(vb_base_universe_d2_034_vb_basefill_039):
    return _base_universe_d3(vb_base_universe_d2_034_vb_basefill_039, 34)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_034_vb_basefill_039'] = {'inputs': ['vb_base_universe_d2_034_vb_basefill_039'], 'func': vb_base_universe_d3_034_vb_basefill_039}


def vb_base_universe_d3_035_vb_basefill_040(vb_base_universe_d2_035_vb_basefill_040):
    return _base_universe_d3(vb_base_universe_d2_035_vb_basefill_040, 35)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_035_vb_basefill_040'] = {'inputs': ['vb_base_universe_d2_035_vb_basefill_040'], 'func': vb_base_universe_d3_035_vb_basefill_040}


def vb_base_universe_d3_036_vb_basefill_041(vb_base_universe_d2_036_vb_basefill_041):
    return _base_universe_d3(vb_base_universe_d2_036_vb_basefill_041, 36)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_036_vb_basefill_041'] = {'inputs': ['vb_base_universe_d2_036_vb_basefill_041'], 'func': vb_base_universe_d3_036_vb_basefill_041}


def vb_base_universe_d3_037_vb_basefill_042(vb_base_universe_d2_037_vb_basefill_042):
    return _base_universe_d3(vb_base_universe_d2_037_vb_basefill_042, 37)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_037_vb_basefill_042'] = {'inputs': ['vb_base_universe_d2_037_vb_basefill_042'], 'func': vb_base_universe_d3_037_vb_basefill_042}


def vb_base_universe_d3_038_vb_basefill_043(vb_base_universe_d2_038_vb_basefill_043):
    return _base_universe_d3(vb_base_universe_d2_038_vb_basefill_043, 38)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_038_vb_basefill_043'] = {'inputs': ['vb_base_universe_d2_038_vb_basefill_043'], 'func': vb_base_universe_d3_038_vb_basefill_043}


def vb_base_universe_d3_039_vb_basefill_044(vb_base_universe_d2_039_vb_basefill_044):
    return _base_universe_d3(vb_base_universe_d2_039_vb_basefill_044, 39)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_039_vb_basefill_044'] = {'inputs': ['vb_base_universe_d2_039_vb_basefill_044'], 'func': vb_base_universe_d3_039_vb_basefill_044}


def vb_base_universe_d3_040_vb_basefill_045(vb_base_universe_d2_040_vb_basefill_045):
    return _base_universe_d3(vb_base_universe_d2_040_vb_basefill_045, 40)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_040_vb_basefill_045'] = {'inputs': ['vb_base_universe_d2_040_vb_basefill_045'], 'func': vb_base_universe_d3_040_vb_basefill_045}


def vb_base_universe_d3_041_vb_basefill_046(vb_base_universe_d2_041_vb_basefill_046):
    return _base_universe_d3(vb_base_universe_d2_041_vb_basefill_046, 41)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_041_vb_basefill_046'] = {'inputs': ['vb_base_universe_d2_041_vb_basefill_046'], 'func': vb_base_universe_d3_041_vb_basefill_046}


def vb_base_universe_d3_042_vb_basefill_047(vb_base_universe_d2_042_vb_basefill_047):
    return _base_universe_d3(vb_base_universe_d2_042_vb_basefill_047, 42)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_042_vb_basefill_047'] = {'inputs': ['vb_base_universe_d2_042_vb_basefill_047'], 'func': vb_base_universe_d3_042_vb_basefill_047}


def vb_base_universe_d3_043_vb_basefill_048(vb_base_universe_d2_043_vb_basefill_048):
    return _base_universe_d3(vb_base_universe_d2_043_vb_basefill_048, 43)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_043_vb_basefill_048'] = {'inputs': ['vb_base_universe_d2_043_vb_basefill_048'], 'func': vb_base_universe_d3_043_vb_basefill_048}


def vb_base_universe_d3_044_vb_basefill_049(vb_base_universe_d2_044_vb_basefill_049):
    return _base_universe_d3(vb_base_universe_d2_044_vb_basefill_049, 44)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_044_vb_basefill_049'] = {'inputs': ['vb_base_universe_d2_044_vb_basefill_049'], 'func': vb_base_universe_d3_044_vb_basefill_049}


def vb_base_universe_d3_045_vb_basefill_050(vb_base_universe_d2_045_vb_basefill_050):
    return _base_universe_d3(vb_base_universe_d2_045_vb_basefill_050, 45)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_045_vb_basefill_050'] = {'inputs': ['vb_base_universe_d2_045_vb_basefill_050'], 'func': vb_base_universe_d3_045_vb_basefill_050}


def vb_base_universe_d3_046_vb_basefill_051(vb_base_universe_d2_046_vb_basefill_051):
    return _base_universe_d3(vb_base_universe_d2_046_vb_basefill_051, 46)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_046_vb_basefill_051'] = {'inputs': ['vb_base_universe_d2_046_vb_basefill_051'], 'func': vb_base_universe_d3_046_vb_basefill_051}


def vb_base_universe_d3_047_vb_basefill_052(vb_base_universe_d2_047_vb_basefill_052):
    return _base_universe_d3(vb_base_universe_d2_047_vb_basefill_052, 47)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_047_vb_basefill_052'] = {'inputs': ['vb_base_universe_d2_047_vb_basefill_052'], 'func': vb_base_universe_d3_047_vb_basefill_052}


def vb_base_universe_d3_048_vb_basefill_053(vb_base_universe_d2_048_vb_basefill_053):
    return _base_universe_d3(vb_base_universe_d2_048_vb_basefill_053, 48)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_048_vb_basefill_053'] = {'inputs': ['vb_base_universe_d2_048_vb_basefill_053'], 'func': vb_base_universe_d3_048_vb_basefill_053}


def vb_base_universe_d3_049_vb_basefill_054(vb_base_universe_d2_049_vb_basefill_054):
    return _base_universe_d3(vb_base_universe_d2_049_vb_basefill_054, 49)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_049_vb_basefill_054'] = {'inputs': ['vb_base_universe_d2_049_vb_basefill_054'], 'func': vb_base_universe_d3_049_vb_basefill_054}


def vb_base_universe_d3_050_vb_basefill_055(vb_base_universe_d2_050_vb_basefill_055):
    return _base_universe_d3(vb_base_universe_d2_050_vb_basefill_055, 50)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_050_vb_basefill_055'] = {'inputs': ['vb_base_universe_d2_050_vb_basefill_055'], 'func': vb_base_universe_d3_050_vb_basefill_055}


def vb_base_universe_d3_051_vb_basefill_056(vb_base_universe_d2_051_vb_basefill_056):
    return _base_universe_d3(vb_base_universe_d2_051_vb_basefill_056, 51)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_051_vb_basefill_056'] = {'inputs': ['vb_base_universe_d2_051_vb_basefill_056'], 'func': vb_base_universe_d3_051_vb_basefill_056}


def vb_base_universe_d3_052_vb_basefill_057(vb_base_universe_d2_052_vb_basefill_057):
    return _base_universe_d3(vb_base_universe_d2_052_vb_basefill_057, 52)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_052_vb_basefill_057'] = {'inputs': ['vb_base_universe_d2_052_vb_basefill_057'], 'func': vb_base_universe_d3_052_vb_basefill_057}


def vb_base_universe_d3_053_vb_basefill_058(vb_base_universe_d2_053_vb_basefill_058):
    return _base_universe_d3(vb_base_universe_d2_053_vb_basefill_058, 53)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_053_vb_basefill_058'] = {'inputs': ['vb_base_universe_d2_053_vb_basefill_058'], 'func': vb_base_universe_d3_053_vb_basefill_058}


def vb_base_universe_d3_054_vb_basefill_059(vb_base_universe_d2_054_vb_basefill_059):
    return _base_universe_d3(vb_base_universe_d2_054_vb_basefill_059, 54)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_054_vb_basefill_059'] = {'inputs': ['vb_base_universe_d2_054_vb_basefill_059'], 'func': vb_base_universe_d3_054_vb_basefill_059}


def vb_base_universe_d3_055_vb_basefill_060(vb_base_universe_d2_055_vb_basefill_060):
    return _base_universe_d3(vb_base_universe_d2_055_vb_basefill_060, 55)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_055_vb_basefill_060'] = {'inputs': ['vb_base_universe_d2_055_vb_basefill_060'], 'func': vb_base_universe_d3_055_vb_basefill_060}


def vb_base_universe_d3_056_vb_basefill_061(vb_base_universe_d2_056_vb_basefill_061):
    return _base_universe_d3(vb_base_universe_d2_056_vb_basefill_061, 56)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_056_vb_basefill_061'] = {'inputs': ['vb_base_universe_d2_056_vb_basefill_061'], 'func': vb_base_universe_d3_056_vb_basefill_061}


def vb_base_universe_d3_057_vb_basefill_062(vb_base_universe_d2_057_vb_basefill_062):
    return _base_universe_d3(vb_base_universe_d2_057_vb_basefill_062, 57)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_057_vb_basefill_062'] = {'inputs': ['vb_base_universe_d2_057_vb_basefill_062'], 'func': vb_base_universe_d3_057_vb_basefill_062}


def vb_base_universe_d3_058_vb_basefill_063(vb_base_universe_d2_058_vb_basefill_063):
    return _base_universe_d3(vb_base_universe_d2_058_vb_basefill_063, 58)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_058_vb_basefill_063'] = {'inputs': ['vb_base_universe_d2_058_vb_basefill_063'], 'func': vb_base_universe_d3_058_vb_basefill_063}


def vb_base_universe_d3_059_vb_basefill_064(vb_base_universe_d2_059_vb_basefill_064):
    return _base_universe_d3(vb_base_universe_d2_059_vb_basefill_064, 59)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_059_vb_basefill_064'] = {'inputs': ['vb_base_universe_d2_059_vb_basefill_064'], 'func': vb_base_universe_d3_059_vb_basefill_064}


def vb_base_universe_d3_060_vb_basefill_065(vb_base_universe_d2_060_vb_basefill_065):
    return _base_universe_d3(vb_base_universe_d2_060_vb_basefill_065, 60)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_060_vb_basefill_065'] = {'inputs': ['vb_base_universe_d2_060_vb_basefill_065'], 'func': vb_base_universe_d3_060_vb_basefill_065}


def vb_base_universe_d3_061_vb_basefill_066(vb_base_universe_d2_061_vb_basefill_066):
    return _base_universe_d3(vb_base_universe_d2_061_vb_basefill_066, 61)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_061_vb_basefill_066'] = {'inputs': ['vb_base_universe_d2_061_vb_basefill_066'], 'func': vb_base_universe_d3_061_vb_basefill_066}


def vb_base_universe_d3_062_vb_basefill_067(vb_base_universe_d2_062_vb_basefill_067):
    return _base_universe_d3(vb_base_universe_d2_062_vb_basefill_067, 62)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_062_vb_basefill_067'] = {'inputs': ['vb_base_universe_d2_062_vb_basefill_067'], 'func': vb_base_universe_d3_062_vb_basefill_067}


def vb_base_universe_d3_063_vb_basefill_068(vb_base_universe_d2_063_vb_basefill_068):
    return _base_universe_d3(vb_base_universe_d2_063_vb_basefill_068, 63)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_063_vb_basefill_068'] = {'inputs': ['vb_base_universe_d2_063_vb_basefill_068'], 'func': vb_base_universe_d3_063_vb_basefill_068}


def vb_base_universe_d3_064_vb_basefill_069(vb_base_universe_d2_064_vb_basefill_069):
    return _base_universe_d3(vb_base_universe_d2_064_vb_basefill_069, 64)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_064_vb_basefill_069'] = {'inputs': ['vb_base_universe_d2_064_vb_basefill_069'], 'func': vb_base_universe_d3_064_vb_basefill_069}


def vb_base_universe_d3_065_vb_basefill_070(vb_base_universe_d2_065_vb_basefill_070):
    return _base_universe_d3(vb_base_universe_d2_065_vb_basefill_070, 65)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_065_vb_basefill_070'] = {'inputs': ['vb_base_universe_d2_065_vb_basefill_070'], 'func': vb_base_universe_d3_065_vb_basefill_070}


def vb_base_universe_d3_066_vb_basefill_071(vb_base_universe_d2_066_vb_basefill_071):
    return _base_universe_d3(vb_base_universe_d2_066_vb_basefill_071, 66)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_066_vb_basefill_071'] = {'inputs': ['vb_base_universe_d2_066_vb_basefill_071'], 'func': vb_base_universe_d3_066_vb_basefill_071}


def vb_base_universe_d3_067_vb_basefill_072(vb_base_universe_d2_067_vb_basefill_072):
    return _base_universe_d3(vb_base_universe_d2_067_vb_basefill_072, 67)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_067_vb_basefill_072'] = {'inputs': ['vb_base_universe_d2_067_vb_basefill_072'], 'func': vb_base_universe_d3_067_vb_basefill_072}


def vb_base_universe_d3_068_vb_basefill_073(vb_base_universe_d2_068_vb_basefill_073):
    return _base_universe_d3(vb_base_universe_d2_068_vb_basefill_073, 68)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_068_vb_basefill_073'] = {'inputs': ['vb_base_universe_d2_068_vb_basefill_073'], 'func': vb_base_universe_d3_068_vb_basefill_073}


def vb_base_universe_d3_069_vb_basefill_074(vb_base_universe_d2_069_vb_basefill_074):
    return _base_universe_d3(vb_base_universe_d2_069_vb_basefill_074, 69)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_069_vb_basefill_074'] = {'inputs': ['vb_base_universe_d2_069_vb_basefill_074'], 'func': vb_base_universe_d3_069_vb_basefill_074}


def vb_base_universe_d3_070_vb_basefill_075(vb_base_universe_d2_070_vb_basefill_075):
    return _base_universe_d3(vb_base_universe_d2_070_vb_basefill_075, 70)
VB_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vb_base_universe_d3_070_vb_basefill_075'] = {'inputs': ['vb_base_universe_d2_070_vb_basefill_075'], 'func': vb_base_universe_d3_070_vb_basefill_075}
