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



def vp_176_vp_001_volume_spike_ratio_5_001_accel_1(vp_151_vp_001_volume_spike_ratio_5_001_roc_1):
    feature = _s(vp_151_vp_001_volume_spike_ratio_5_001_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def vp_177_vp_007_volume_spike_ratio_126_007_accel_5(vp_152_vp_007_volume_spike_ratio_126_007_roc_5):
    feature = _s(vp_152_vp_007_volume_spike_ratio_126_007_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def vp_178_vp_013_volume_spike_ratio_1008_013_accel_42(vp_153_vp_013_volume_spike_ratio_1008_013_roc_42):
    feature = _s(vp_153_vp_013_volume_spike_ratio_1008_013_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def vp_179_vp_019_volume_spike_ratio_42_019_accel_126(vp_154_vp_019_volume_spike_ratio_42_019_roc_126):
    feature = _s(vp_154_vp_019_volume_spike_ratio_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def vp_180_vp_025_volume_spike_ratio_378_025_accel_378(vp_155_vp_025_volume_spike_ratio_378_025_roc_378):
    feature = _s(vp_155_vp_025_volume_spike_ratio_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















VOLUME_PERSISTENCE_REGISTRY_3RD_DERIVATIVES = {
    'vp_176_vp_001_volume_spike_ratio_5_001_accel_1': {'inputs': ['vp_151_vp_001_volume_spike_ratio_5_001_roc_1'], 'func': vp_176_vp_001_volume_spike_ratio_5_001_accel_1},
    'vp_177_vp_007_volume_spike_ratio_126_007_accel_5': {'inputs': ['vp_152_vp_007_volume_spike_ratio_126_007_roc_5'], 'func': vp_177_vp_007_volume_spike_ratio_126_007_accel_5},
    'vp_178_vp_013_volume_spike_ratio_1008_013_accel_42': {'inputs': ['vp_153_vp_013_volume_spike_ratio_1008_013_roc_42'], 'func': vp_178_vp_013_volume_spike_ratio_1008_013_accel_42},
    'vp_179_vp_019_volume_spike_ratio_42_019_accel_126': {'inputs': ['vp_154_vp_019_volume_spike_ratio_42_019_roc_126'], 'func': vp_179_vp_019_volume_spike_ratio_42_019_accel_126},
    'vp_180_vp_025_volume_spike_ratio_378_025_accel_378': {'inputs': ['vp_155_vp_025_volume_spike_ratio_378_025_roc_378'], 'func': vp_180_vp_025_volume_spike_ratio_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def vp_replacement_d3_001(vp_replacement_d2_001):
    feature = _clean(vp_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_001'] = {'inputs': ['vp_replacement_d2_001'], 'func': vp_replacement_d3_001}


def vp_replacement_d3_002(vp_replacement_d2_002):
    feature = _clean(vp_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_002'] = {'inputs': ['vp_replacement_d2_002'], 'func': vp_replacement_d3_002}


def vp_replacement_d3_003(vp_replacement_d2_003):
    feature = _clean(vp_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_003'] = {'inputs': ['vp_replacement_d2_003'], 'func': vp_replacement_d3_003}


def vp_replacement_d3_004(vp_replacement_d2_004):
    feature = _clean(vp_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_004'] = {'inputs': ['vp_replacement_d2_004'], 'func': vp_replacement_d3_004}


def vp_replacement_d3_005(vp_replacement_d2_005):
    feature = _clean(vp_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_005'] = {'inputs': ['vp_replacement_d2_005'], 'func': vp_replacement_d3_005}


def vp_replacement_d3_006(vp_replacement_d2_006):
    feature = _clean(vp_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_006'] = {'inputs': ['vp_replacement_d2_006'], 'func': vp_replacement_d3_006}


def vp_replacement_d3_007(vp_replacement_d2_007):
    feature = _clean(vp_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_007'] = {'inputs': ['vp_replacement_d2_007'], 'func': vp_replacement_d3_007}


def vp_replacement_d3_008(vp_replacement_d2_008):
    feature = _clean(vp_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_008'] = {'inputs': ['vp_replacement_d2_008'], 'func': vp_replacement_d3_008}


def vp_replacement_d3_009(vp_replacement_d2_009):
    feature = _clean(vp_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_009'] = {'inputs': ['vp_replacement_d2_009'], 'func': vp_replacement_d3_009}


def vp_replacement_d3_010(vp_replacement_d2_010):
    feature = _clean(vp_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_010'] = {'inputs': ['vp_replacement_d2_010'], 'func': vp_replacement_d3_010}


def vp_replacement_d3_011(vp_replacement_d2_011):
    feature = _clean(vp_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_011'] = {'inputs': ['vp_replacement_d2_011'], 'func': vp_replacement_d3_011}


def vp_replacement_d3_012(vp_replacement_d2_012):
    feature = _clean(vp_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_012'] = {'inputs': ['vp_replacement_d2_012'], 'func': vp_replacement_d3_012}


def vp_replacement_d3_013(vp_replacement_d2_013):
    feature = _clean(vp_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_013'] = {'inputs': ['vp_replacement_d2_013'], 'func': vp_replacement_d3_013}


def vp_replacement_d3_014(vp_replacement_d2_014):
    feature = _clean(vp_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_014'] = {'inputs': ['vp_replacement_d2_014'], 'func': vp_replacement_d3_014}


def vp_replacement_d3_015(vp_replacement_d2_015):
    feature = _clean(vp_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_015'] = {'inputs': ['vp_replacement_d2_015'], 'func': vp_replacement_d3_015}


def vp_replacement_d3_016(vp_replacement_d2_016):
    feature = _clean(vp_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_016'] = {'inputs': ['vp_replacement_d2_016'], 'func': vp_replacement_d3_016}


def vp_replacement_d3_017(vp_replacement_d2_017):
    feature = _clean(vp_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_017'] = {'inputs': ['vp_replacement_d2_017'], 'func': vp_replacement_d3_017}


def vp_replacement_d3_018(vp_replacement_d2_018):
    feature = _clean(vp_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_018'] = {'inputs': ['vp_replacement_d2_018'], 'func': vp_replacement_d3_018}


def vp_replacement_d3_019(vp_replacement_d2_019):
    feature = _clean(vp_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_019'] = {'inputs': ['vp_replacement_d2_019'], 'func': vp_replacement_d3_019}


def vp_replacement_d3_020(vp_replacement_d2_020):
    feature = _clean(vp_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_020'] = {'inputs': ['vp_replacement_d2_020'], 'func': vp_replacement_d3_020}


def vp_replacement_d3_021(vp_replacement_d2_021):
    feature = _clean(vp_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_021'] = {'inputs': ['vp_replacement_d2_021'], 'func': vp_replacement_d3_021}


def vp_replacement_d3_022(vp_replacement_d2_022):
    feature = _clean(vp_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_022'] = {'inputs': ['vp_replacement_d2_022'], 'func': vp_replacement_d3_022}


def vp_replacement_d3_023(vp_replacement_d2_023):
    feature = _clean(vp_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_023'] = {'inputs': ['vp_replacement_d2_023'], 'func': vp_replacement_d3_023}


def vp_replacement_d3_024(vp_replacement_d2_024):
    feature = _clean(vp_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_024'] = {'inputs': ['vp_replacement_d2_024'], 'func': vp_replacement_d3_024}


def vp_replacement_d3_025(vp_replacement_d2_025):
    feature = _clean(vp_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_025'] = {'inputs': ['vp_replacement_d2_025'], 'func': vp_replacement_d3_025}


def vp_replacement_d3_026(vp_replacement_d2_026):
    feature = _clean(vp_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_026'] = {'inputs': ['vp_replacement_d2_026'], 'func': vp_replacement_d3_026}


def vp_replacement_d3_027(vp_replacement_d2_027):
    feature = _clean(vp_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_027'] = {'inputs': ['vp_replacement_d2_027'], 'func': vp_replacement_d3_027}


def vp_replacement_d3_028(vp_replacement_d2_028):
    feature = _clean(vp_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_028'] = {'inputs': ['vp_replacement_d2_028'], 'func': vp_replacement_d3_028}


def vp_replacement_d3_029(vp_replacement_d2_029):
    feature = _clean(vp_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_029'] = {'inputs': ['vp_replacement_d2_029'], 'func': vp_replacement_d3_029}


def vp_replacement_d3_030(vp_replacement_d2_030):
    feature = _clean(vp_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_030'] = {'inputs': ['vp_replacement_d2_030'], 'func': vp_replacement_d3_030}


def vp_replacement_d3_031(vp_replacement_d2_031):
    feature = _clean(vp_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_031'] = {'inputs': ['vp_replacement_d2_031'], 'func': vp_replacement_d3_031}


def vp_replacement_d3_032(vp_replacement_d2_032):
    feature = _clean(vp_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_032'] = {'inputs': ['vp_replacement_d2_032'], 'func': vp_replacement_d3_032}


def vp_replacement_d3_033(vp_replacement_d2_033):
    feature = _clean(vp_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_033'] = {'inputs': ['vp_replacement_d2_033'], 'func': vp_replacement_d3_033}


def vp_replacement_d3_034(vp_replacement_d2_034):
    feature = _clean(vp_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_034'] = {'inputs': ['vp_replacement_d2_034'], 'func': vp_replacement_d3_034}


def vp_replacement_d3_035(vp_replacement_d2_035):
    feature = _clean(vp_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_035'] = {'inputs': ['vp_replacement_d2_035'], 'func': vp_replacement_d3_035}


def vp_replacement_d3_036(vp_replacement_d2_036):
    feature = _clean(vp_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_036'] = {'inputs': ['vp_replacement_d2_036'], 'func': vp_replacement_d3_036}


def vp_replacement_d3_037(vp_replacement_d2_037):
    feature = _clean(vp_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_037'] = {'inputs': ['vp_replacement_d2_037'], 'func': vp_replacement_d3_037}


def vp_replacement_d3_038(vp_replacement_d2_038):
    feature = _clean(vp_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_038'] = {'inputs': ['vp_replacement_d2_038'], 'func': vp_replacement_d3_038}


def vp_replacement_d3_039(vp_replacement_d2_039):
    feature = _clean(vp_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_039'] = {'inputs': ['vp_replacement_d2_039'], 'func': vp_replacement_d3_039}


def vp_replacement_d3_040(vp_replacement_d2_040):
    feature = _clean(vp_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_040'] = {'inputs': ['vp_replacement_d2_040'], 'func': vp_replacement_d3_040}


def vp_replacement_d3_041(vp_replacement_d2_041):
    feature = _clean(vp_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_041'] = {'inputs': ['vp_replacement_d2_041'], 'func': vp_replacement_d3_041}


def vp_replacement_d3_042(vp_replacement_d2_042):
    feature = _clean(vp_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_042'] = {'inputs': ['vp_replacement_d2_042'], 'func': vp_replacement_d3_042}


def vp_replacement_d3_043(vp_replacement_d2_043):
    feature = _clean(vp_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_043'] = {'inputs': ['vp_replacement_d2_043'], 'func': vp_replacement_d3_043}


def vp_replacement_d3_044(vp_replacement_d2_044):
    feature = _clean(vp_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_044'] = {'inputs': ['vp_replacement_d2_044'], 'func': vp_replacement_d3_044}


def vp_replacement_d3_045(vp_replacement_d2_045):
    feature = _clean(vp_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_045'] = {'inputs': ['vp_replacement_d2_045'], 'func': vp_replacement_d3_045}


def vp_replacement_d3_046(vp_replacement_d2_046):
    feature = _clean(vp_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_046'] = {'inputs': ['vp_replacement_d2_046'], 'func': vp_replacement_d3_046}


def vp_replacement_d3_047(vp_replacement_d2_047):
    feature = _clean(vp_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_047'] = {'inputs': ['vp_replacement_d2_047'], 'func': vp_replacement_d3_047}


def vp_replacement_d3_048(vp_replacement_d2_048):
    feature = _clean(vp_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_048'] = {'inputs': ['vp_replacement_d2_048'], 'func': vp_replacement_d3_048}


def vp_replacement_d3_049(vp_replacement_d2_049):
    feature = _clean(vp_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_049'] = {'inputs': ['vp_replacement_d2_049'], 'func': vp_replacement_d3_049}


def vp_replacement_d3_050(vp_replacement_d2_050):
    feature = _clean(vp_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_050'] = {'inputs': ['vp_replacement_d2_050'], 'func': vp_replacement_d3_050}


def vp_replacement_d3_051(vp_replacement_d2_051):
    feature = _clean(vp_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_051'] = {'inputs': ['vp_replacement_d2_051'], 'func': vp_replacement_d3_051}


def vp_replacement_d3_052(vp_replacement_d2_052):
    feature = _clean(vp_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_052'] = {'inputs': ['vp_replacement_d2_052'], 'func': vp_replacement_d3_052}


def vp_replacement_d3_053(vp_replacement_d2_053):
    feature = _clean(vp_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_053'] = {'inputs': ['vp_replacement_d2_053'], 'func': vp_replacement_d3_053}


def vp_replacement_d3_054(vp_replacement_d2_054):
    feature = _clean(vp_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_054'] = {'inputs': ['vp_replacement_d2_054'], 'func': vp_replacement_d3_054}


def vp_replacement_d3_055(vp_replacement_d2_055):
    feature = _clean(vp_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_055'] = {'inputs': ['vp_replacement_d2_055'], 'func': vp_replacement_d3_055}


def vp_replacement_d3_056(vp_replacement_d2_056):
    feature = _clean(vp_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_056'] = {'inputs': ['vp_replacement_d2_056'], 'func': vp_replacement_d3_056}


def vp_replacement_d3_057(vp_replacement_d2_057):
    feature = _clean(vp_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_057'] = {'inputs': ['vp_replacement_d2_057'], 'func': vp_replacement_d3_057}


def vp_replacement_d3_058(vp_replacement_d2_058):
    feature = _clean(vp_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_058'] = {'inputs': ['vp_replacement_d2_058'], 'func': vp_replacement_d3_058}


def vp_replacement_d3_059(vp_replacement_d2_059):
    feature = _clean(vp_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_059'] = {'inputs': ['vp_replacement_d2_059'], 'func': vp_replacement_d3_059}


def vp_replacement_d3_060(vp_replacement_d2_060):
    feature = _clean(vp_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_060'] = {'inputs': ['vp_replacement_d2_060'], 'func': vp_replacement_d3_060}


def vp_replacement_d3_061(vp_replacement_d2_061):
    feature = _clean(vp_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_061'] = {'inputs': ['vp_replacement_d2_061'], 'func': vp_replacement_d3_061}


def vp_replacement_d3_062(vp_replacement_d2_062):
    feature = _clean(vp_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_062'] = {'inputs': ['vp_replacement_d2_062'], 'func': vp_replacement_d3_062}


def vp_replacement_d3_063(vp_replacement_d2_063):
    feature = _clean(vp_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_063'] = {'inputs': ['vp_replacement_d2_063'], 'func': vp_replacement_d3_063}


def vp_replacement_d3_064(vp_replacement_d2_064):
    feature = _clean(vp_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_064'] = {'inputs': ['vp_replacement_d2_064'], 'func': vp_replacement_d3_064}


def vp_replacement_d3_065(vp_replacement_d2_065):
    feature = _clean(vp_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_065'] = {'inputs': ['vp_replacement_d2_065'], 'func': vp_replacement_d3_065}


def vp_replacement_d3_066(vp_replacement_d2_066):
    feature = _clean(vp_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_066'] = {'inputs': ['vp_replacement_d2_066'], 'func': vp_replacement_d3_066}


def vp_replacement_d3_067(vp_replacement_d2_067):
    feature = _clean(vp_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_067'] = {'inputs': ['vp_replacement_d2_067'], 'func': vp_replacement_d3_067}


def vp_replacement_d3_068(vp_replacement_d2_068):
    feature = _clean(vp_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_068'] = {'inputs': ['vp_replacement_d2_068'], 'func': vp_replacement_d3_068}


def vp_replacement_d3_069(vp_replacement_d2_069):
    feature = _clean(vp_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_069'] = {'inputs': ['vp_replacement_d2_069'], 'func': vp_replacement_d3_069}


def vp_replacement_d3_070(vp_replacement_d2_070):
    feature = _clean(vp_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_070'] = {'inputs': ['vp_replacement_d2_070'], 'func': vp_replacement_d3_070}


def vp_replacement_d3_071(vp_replacement_d2_071):
    feature = _clean(vp_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_071'] = {'inputs': ['vp_replacement_d2_071'], 'func': vp_replacement_d3_071}


def vp_replacement_d3_072(vp_replacement_d2_072):
    feature = _clean(vp_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_072'] = {'inputs': ['vp_replacement_d2_072'], 'func': vp_replacement_d3_072}


def vp_replacement_d3_073(vp_replacement_d2_073):
    feature = _clean(vp_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_073'] = {'inputs': ['vp_replacement_d2_073'], 'func': vp_replacement_d3_073}


def vp_replacement_d3_074(vp_replacement_d2_074):
    feature = _clean(vp_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_074'] = {'inputs': ['vp_replacement_d2_074'], 'func': vp_replacement_d3_074}


def vp_replacement_d3_075(vp_replacement_d2_075):
    feature = _clean(vp_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_075'] = {'inputs': ['vp_replacement_d2_075'], 'func': vp_replacement_d3_075}


def vp_replacement_d3_076(vp_replacement_d2_076):
    feature = _clean(vp_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_076'] = {'inputs': ['vp_replacement_d2_076'], 'func': vp_replacement_d3_076}


def vp_replacement_d3_077(vp_replacement_d2_077):
    feature = _clean(vp_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_077'] = {'inputs': ['vp_replacement_d2_077'], 'func': vp_replacement_d3_077}


def vp_replacement_d3_078(vp_replacement_d2_078):
    feature = _clean(vp_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_078'] = {'inputs': ['vp_replacement_d2_078'], 'func': vp_replacement_d3_078}


def vp_replacement_d3_079(vp_replacement_d2_079):
    feature = _clean(vp_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_079'] = {'inputs': ['vp_replacement_d2_079'], 'func': vp_replacement_d3_079}


def vp_replacement_d3_080(vp_replacement_d2_080):
    feature = _clean(vp_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_080'] = {'inputs': ['vp_replacement_d2_080'], 'func': vp_replacement_d3_080}


def vp_replacement_d3_081(vp_replacement_d2_081):
    feature = _clean(vp_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_081'] = {'inputs': ['vp_replacement_d2_081'], 'func': vp_replacement_d3_081}


def vp_replacement_d3_082(vp_replacement_d2_082):
    feature = _clean(vp_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_082'] = {'inputs': ['vp_replacement_d2_082'], 'func': vp_replacement_d3_082}


def vp_replacement_d3_083(vp_replacement_d2_083):
    feature = _clean(vp_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_083'] = {'inputs': ['vp_replacement_d2_083'], 'func': vp_replacement_d3_083}


def vp_replacement_d3_084(vp_replacement_d2_084):
    feature = _clean(vp_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_084'] = {'inputs': ['vp_replacement_d2_084'], 'func': vp_replacement_d3_084}


def vp_replacement_d3_085(vp_replacement_d2_085):
    feature = _clean(vp_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_085'] = {'inputs': ['vp_replacement_d2_085'], 'func': vp_replacement_d3_085}


def vp_replacement_d3_086(vp_replacement_d2_086):
    feature = _clean(vp_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_086'] = {'inputs': ['vp_replacement_d2_086'], 'func': vp_replacement_d3_086}


def vp_replacement_d3_087(vp_replacement_d2_087):
    feature = _clean(vp_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_087'] = {'inputs': ['vp_replacement_d2_087'], 'func': vp_replacement_d3_087}


def vp_replacement_d3_088(vp_replacement_d2_088):
    feature = _clean(vp_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_088'] = {'inputs': ['vp_replacement_d2_088'], 'func': vp_replacement_d3_088}


def vp_replacement_d3_089(vp_replacement_d2_089):
    feature = _clean(vp_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_089'] = {'inputs': ['vp_replacement_d2_089'], 'func': vp_replacement_d3_089}


def vp_replacement_d3_090(vp_replacement_d2_090):
    feature = _clean(vp_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_090'] = {'inputs': ['vp_replacement_d2_090'], 'func': vp_replacement_d3_090}


def vp_replacement_d3_091(vp_replacement_d2_091):
    feature = _clean(vp_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_091'] = {'inputs': ['vp_replacement_d2_091'], 'func': vp_replacement_d3_091}


def vp_replacement_d3_092(vp_replacement_d2_092):
    feature = _clean(vp_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_092'] = {'inputs': ['vp_replacement_d2_092'], 'func': vp_replacement_d3_092}


def vp_replacement_d3_093(vp_replacement_d2_093):
    feature = _clean(vp_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_093'] = {'inputs': ['vp_replacement_d2_093'], 'func': vp_replacement_d3_093}


def vp_replacement_d3_094(vp_replacement_d2_094):
    feature = _clean(vp_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_094'] = {'inputs': ['vp_replacement_d2_094'], 'func': vp_replacement_d3_094}


def vp_replacement_d3_095(vp_replacement_d2_095):
    feature = _clean(vp_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_095'] = {'inputs': ['vp_replacement_d2_095'], 'func': vp_replacement_d3_095}


def vp_replacement_d3_096(vp_replacement_d2_096):
    feature = _clean(vp_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_096'] = {'inputs': ['vp_replacement_d2_096'], 'func': vp_replacement_d3_096}


def vp_replacement_d3_097(vp_replacement_d2_097):
    feature = _clean(vp_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_097'] = {'inputs': ['vp_replacement_d2_097'], 'func': vp_replacement_d3_097}


def vp_replacement_d3_098(vp_replacement_d2_098):
    feature = _clean(vp_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_098'] = {'inputs': ['vp_replacement_d2_098'], 'func': vp_replacement_d3_098}


def vp_replacement_d3_099(vp_replacement_d2_099):
    feature = _clean(vp_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_099'] = {'inputs': ['vp_replacement_d2_099'], 'func': vp_replacement_d3_099}


def vp_replacement_d3_100(vp_replacement_d2_100):
    feature = _clean(vp_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_100'] = {'inputs': ['vp_replacement_d2_100'], 'func': vp_replacement_d3_100}


def vp_replacement_d3_101(vp_replacement_d2_101):
    feature = _clean(vp_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_101'] = {'inputs': ['vp_replacement_d2_101'], 'func': vp_replacement_d3_101}


def vp_replacement_d3_102(vp_replacement_d2_102):
    feature = _clean(vp_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_102'] = {'inputs': ['vp_replacement_d2_102'], 'func': vp_replacement_d3_102}


def vp_replacement_d3_103(vp_replacement_d2_103):
    feature = _clean(vp_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_103'] = {'inputs': ['vp_replacement_d2_103'], 'func': vp_replacement_d3_103}


def vp_replacement_d3_104(vp_replacement_d2_104):
    feature = _clean(vp_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_104'] = {'inputs': ['vp_replacement_d2_104'], 'func': vp_replacement_d3_104}


def vp_replacement_d3_105(vp_replacement_d2_105):
    feature = _clean(vp_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_105'] = {'inputs': ['vp_replacement_d2_105'], 'func': vp_replacement_d3_105}


def vp_replacement_d3_106(vp_replacement_d2_106):
    feature = _clean(vp_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_106'] = {'inputs': ['vp_replacement_d2_106'], 'func': vp_replacement_d3_106}


def vp_replacement_d3_107(vp_replacement_d2_107):
    feature = _clean(vp_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_107'] = {'inputs': ['vp_replacement_d2_107'], 'func': vp_replacement_d3_107}


def vp_replacement_d3_108(vp_replacement_d2_108):
    feature = _clean(vp_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_108'] = {'inputs': ['vp_replacement_d2_108'], 'func': vp_replacement_d3_108}


def vp_replacement_d3_109(vp_replacement_d2_109):
    feature = _clean(vp_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_109'] = {'inputs': ['vp_replacement_d2_109'], 'func': vp_replacement_d3_109}


def vp_replacement_d3_110(vp_replacement_d2_110):
    feature = _clean(vp_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_110'] = {'inputs': ['vp_replacement_d2_110'], 'func': vp_replacement_d3_110}


def vp_replacement_d3_111(vp_replacement_d2_111):
    feature = _clean(vp_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_111'] = {'inputs': ['vp_replacement_d2_111'], 'func': vp_replacement_d3_111}


def vp_replacement_d3_112(vp_replacement_d2_112):
    feature = _clean(vp_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_112'] = {'inputs': ['vp_replacement_d2_112'], 'func': vp_replacement_d3_112}


def vp_replacement_d3_113(vp_replacement_d2_113):
    feature = _clean(vp_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_113'] = {'inputs': ['vp_replacement_d2_113'], 'func': vp_replacement_d3_113}


def vp_replacement_d3_114(vp_replacement_d2_114):
    feature = _clean(vp_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_114'] = {'inputs': ['vp_replacement_d2_114'], 'func': vp_replacement_d3_114}


def vp_replacement_d3_115(vp_replacement_d2_115):
    feature = _clean(vp_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_115'] = {'inputs': ['vp_replacement_d2_115'], 'func': vp_replacement_d3_115}


def vp_replacement_d3_116(vp_replacement_d2_116):
    feature = _clean(vp_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_116'] = {'inputs': ['vp_replacement_d2_116'], 'func': vp_replacement_d3_116}


def vp_replacement_d3_117(vp_replacement_d2_117):
    feature = _clean(vp_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_117'] = {'inputs': ['vp_replacement_d2_117'], 'func': vp_replacement_d3_117}


def vp_replacement_d3_118(vp_replacement_d2_118):
    feature = _clean(vp_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_118'] = {'inputs': ['vp_replacement_d2_118'], 'func': vp_replacement_d3_118}


def vp_replacement_d3_119(vp_replacement_d2_119):
    feature = _clean(vp_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_119'] = {'inputs': ['vp_replacement_d2_119'], 'func': vp_replacement_d3_119}


def vp_replacement_d3_120(vp_replacement_d2_120):
    feature = _clean(vp_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_120'] = {'inputs': ['vp_replacement_d2_120'], 'func': vp_replacement_d3_120}


def vp_replacement_d3_121(vp_replacement_d2_121):
    feature = _clean(vp_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_121'] = {'inputs': ['vp_replacement_d2_121'], 'func': vp_replacement_d3_121}


def vp_replacement_d3_122(vp_replacement_d2_122):
    feature = _clean(vp_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_122'] = {'inputs': ['vp_replacement_d2_122'], 'func': vp_replacement_d3_122}


def vp_replacement_d3_123(vp_replacement_d2_123):
    feature = _clean(vp_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_123'] = {'inputs': ['vp_replacement_d2_123'], 'func': vp_replacement_d3_123}


def vp_replacement_d3_124(vp_replacement_d2_124):
    feature = _clean(vp_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_124'] = {'inputs': ['vp_replacement_d2_124'], 'func': vp_replacement_d3_124}


def vp_replacement_d3_125(vp_replacement_d2_125):
    feature = _clean(vp_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_125'] = {'inputs': ['vp_replacement_d2_125'], 'func': vp_replacement_d3_125}


def vp_replacement_d3_126(vp_replacement_d2_126):
    feature = _clean(vp_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_126'] = {'inputs': ['vp_replacement_d2_126'], 'func': vp_replacement_d3_126}


def vp_replacement_d3_127(vp_replacement_d2_127):
    feature = _clean(vp_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_127'] = {'inputs': ['vp_replacement_d2_127'], 'func': vp_replacement_d3_127}


def vp_replacement_d3_128(vp_replacement_d2_128):
    feature = _clean(vp_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_128'] = {'inputs': ['vp_replacement_d2_128'], 'func': vp_replacement_d3_128}


def vp_replacement_d3_129(vp_replacement_d2_129):
    feature = _clean(vp_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_129'] = {'inputs': ['vp_replacement_d2_129'], 'func': vp_replacement_d3_129}


def vp_replacement_d3_130(vp_replacement_d2_130):
    feature = _clean(vp_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_130'] = {'inputs': ['vp_replacement_d2_130'], 'func': vp_replacement_d3_130}


def vp_replacement_d3_131(vp_replacement_d2_131):
    feature = _clean(vp_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_131'] = {'inputs': ['vp_replacement_d2_131'], 'func': vp_replacement_d3_131}


def vp_replacement_d3_132(vp_replacement_d2_132):
    feature = _clean(vp_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_132'] = {'inputs': ['vp_replacement_d2_132'], 'func': vp_replacement_d3_132}


def vp_replacement_d3_133(vp_replacement_d2_133):
    feature = _clean(vp_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_133'] = {'inputs': ['vp_replacement_d2_133'], 'func': vp_replacement_d3_133}


def vp_replacement_d3_134(vp_replacement_d2_134):
    feature = _clean(vp_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_134'] = {'inputs': ['vp_replacement_d2_134'], 'func': vp_replacement_d3_134}


def vp_replacement_d3_135(vp_replacement_d2_135):
    feature = _clean(vp_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_135'] = {'inputs': ['vp_replacement_d2_135'], 'func': vp_replacement_d3_135}


def vp_replacement_d3_136(vp_replacement_d2_136):
    feature = _clean(vp_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_136'] = {'inputs': ['vp_replacement_d2_136'], 'func': vp_replacement_d3_136}


def vp_replacement_d3_137(vp_replacement_d2_137):
    feature = _clean(vp_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_137'] = {'inputs': ['vp_replacement_d2_137'], 'func': vp_replacement_d3_137}


def vp_replacement_d3_138(vp_replacement_d2_138):
    feature = _clean(vp_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_138'] = {'inputs': ['vp_replacement_d2_138'], 'func': vp_replacement_d3_138}


def vp_replacement_d3_139(vp_replacement_d2_139):
    feature = _clean(vp_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_139'] = {'inputs': ['vp_replacement_d2_139'], 'func': vp_replacement_d3_139}


def vp_replacement_d3_140(vp_replacement_d2_140):
    feature = _clean(vp_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_140'] = {'inputs': ['vp_replacement_d2_140'], 'func': vp_replacement_d3_140}


def vp_replacement_d3_141(vp_replacement_d2_141):
    feature = _clean(vp_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_141'] = {'inputs': ['vp_replacement_d2_141'], 'func': vp_replacement_d3_141}


def vp_replacement_d3_142(vp_replacement_d2_142):
    feature = _clean(vp_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_142'] = {'inputs': ['vp_replacement_d2_142'], 'func': vp_replacement_d3_142}


def vp_replacement_d3_143(vp_replacement_d2_143):
    feature = _clean(vp_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_143'] = {'inputs': ['vp_replacement_d2_143'], 'func': vp_replacement_d3_143}


def vp_replacement_d3_144(vp_replacement_d2_144):
    feature = _clean(vp_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_144'] = {'inputs': ['vp_replacement_d2_144'], 'func': vp_replacement_d3_144}


def vp_replacement_d3_145(vp_replacement_d2_145):
    feature = _clean(vp_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_145'] = {'inputs': ['vp_replacement_d2_145'], 'func': vp_replacement_d3_145}


def vp_replacement_d3_146(vp_replacement_d2_146):
    feature = _clean(vp_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_146'] = {'inputs': ['vp_replacement_d2_146'], 'func': vp_replacement_d3_146}


def vp_replacement_d3_147(vp_replacement_d2_147):
    feature = _clean(vp_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_147'] = {'inputs': ['vp_replacement_d2_147'], 'func': vp_replacement_d3_147}


def vp_replacement_d3_148(vp_replacement_d2_148):
    feature = _clean(vp_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_148'] = {'inputs': ['vp_replacement_d2_148'], 'func': vp_replacement_d3_148}


def vp_replacement_d3_149(vp_replacement_d2_149):
    feature = _clean(vp_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_149'] = {'inputs': ['vp_replacement_d2_149'], 'func': vp_replacement_d3_149}


def vp_replacement_d3_150(vp_replacement_d2_150):
    feature = _clean(vp_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_150'] = {'inputs': ['vp_replacement_d2_150'], 'func': vp_replacement_d3_150}


def vp_replacement_d3_151(vp_replacement_d2_151):
    feature = _clean(vp_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_151'] = {'inputs': ['vp_replacement_d2_151'], 'func': vp_replacement_d3_151}


def vp_replacement_d3_152(vp_replacement_d2_152):
    feature = _clean(vp_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_152'] = {'inputs': ['vp_replacement_d2_152'], 'func': vp_replacement_d3_152}


def vp_replacement_d3_153(vp_replacement_d2_153):
    feature = _clean(vp_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_153'] = {'inputs': ['vp_replacement_d2_153'], 'func': vp_replacement_d3_153}


def vp_replacement_d3_154(vp_replacement_d2_154):
    feature = _clean(vp_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_154'] = {'inputs': ['vp_replacement_d2_154'], 'func': vp_replacement_d3_154}


def vp_replacement_d3_155(vp_replacement_d2_155):
    feature = _clean(vp_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_155'] = {'inputs': ['vp_replacement_d2_155'], 'func': vp_replacement_d3_155}


def vp_replacement_d3_156(vp_replacement_d2_156):
    feature = _clean(vp_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_156'] = {'inputs': ['vp_replacement_d2_156'], 'func': vp_replacement_d3_156}


def vp_replacement_d3_157(vp_replacement_d2_157):
    feature = _clean(vp_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_157'] = {'inputs': ['vp_replacement_d2_157'], 'func': vp_replacement_d3_157}


def vp_replacement_d3_158(vp_replacement_d2_158):
    feature = _clean(vp_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_158'] = {'inputs': ['vp_replacement_d2_158'], 'func': vp_replacement_d3_158}


def vp_replacement_d3_159(vp_replacement_d2_159):
    feature = _clean(vp_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_159'] = {'inputs': ['vp_replacement_d2_159'], 'func': vp_replacement_d3_159}


def vp_replacement_d3_160(vp_replacement_d2_160):
    feature = _clean(vp_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
VP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vp_replacement_d3_160'] = {'inputs': ['vp_replacement_d2_160'], 'func': vp_replacement_d3_160}


# Third-derivative extensions for repaired first-base features.
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def vp_base_universe_d3_001_vp_002_volume_zscore_10_002(vp_base_universe_d2_001_vp_002_volume_zscore_10_002):
    return _base_universe_d3(vp_base_universe_d2_001_vp_002_volume_zscore_10_002, 1)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_001_vp_002_volume_zscore_10_002'] = {'inputs': ['vp_base_universe_d2_001_vp_002_volume_zscore_10_002'], 'func': vp_base_universe_d3_001_vp_002_volume_zscore_10_002}


def vp_base_universe_d3_002_vp_003_down_volume_share_21_003(vp_base_universe_d2_002_vp_003_down_volume_share_21_003):
    return _base_universe_d3(vp_base_universe_d2_002_vp_003_down_volume_share_21_003, 2)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_002_vp_003_down_volume_share_21_003'] = {'inputs': ['vp_base_universe_d2_002_vp_003_down_volume_share_21_003'], 'func': vp_base_universe_d3_002_vp_003_down_volume_share_21_003}


def vp_base_universe_d3_003_vp_004_dollar_volume_shock_42_004(vp_base_universe_d2_003_vp_004_dollar_volume_shock_42_004):
    return _base_universe_d3(vp_base_universe_d2_003_vp_004_dollar_volume_shock_42_004, 3)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_003_vp_004_dollar_volume_shock_42_004'] = {'inputs': ['vp_base_universe_d2_003_vp_004_dollar_volume_shock_42_004'], 'func': vp_base_universe_d3_003_vp_004_dollar_volume_shock_42_004}


def vp_base_universe_d3_004_vp_005_volume_trend_slope_63_005(vp_base_universe_d2_004_vp_005_volume_trend_slope_63_005):
    return _base_universe_d3(vp_base_universe_d2_004_vp_005_volume_trend_slope_63_005, 4)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_004_vp_005_volume_trend_slope_63_005'] = {'inputs': ['vp_base_universe_d2_004_vp_005_volume_trend_slope_63_005'], 'func': vp_base_universe_d3_004_vp_005_volume_trend_slope_63_005}


def vp_base_universe_d3_005_vp_006_price_volume_divergence_84_006(vp_base_universe_d2_005_vp_006_price_volume_divergence_84_006):
    return _base_universe_d3(vp_base_universe_d2_005_vp_006_price_volume_divergence_84_006, 5)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_005_vp_006_price_volume_divergence_84_006'] = {'inputs': ['vp_base_universe_d2_005_vp_006_price_volume_divergence_84_006'], 'func': vp_base_universe_d3_005_vp_006_price_volume_divergence_84_006}


def vp_base_universe_d3_006_vp_008_volume_zscore_189_008(vp_base_universe_d2_006_vp_008_volume_zscore_189_008):
    return _base_universe_d3(vp_base_universe_d2_006_vp_008_volume_zscore_189_008, 6)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_006_vp_008_volume_zscore_189_008'] = {'inputs': ['vp_base_universe_d2_006_vp_008_volume_zscore_189_008'], 'func': vp_base_universe_d3_006_vp_008_volume_zscore_189_008}


def vp_base_universe_d3_007_vp_009_down_volume_share_252_009(vp_base_universe_d2_007_vp_009_down_volume_share_252_009):
    return _base_universe_d3(vp_base_universe_d2_007_vp_009_down_volume_share_252_009, 7)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_007_vp_009_down_volume_share_252_009'] = {'inputs': ['vp_base_universe_d2_007_vp_009_down_volume_share_252_009'], 'func': vp_base_universe_d3_007_vp_009_down_volume_share_252_009}


def vp_base_universe_d3_008_vp_010_dollar_volume_shock_378_010(vp_base_universe_d2_008_vp_010_dollar_volume_shock_378_010):
    return _base_universe_d3(vp_base_universe_d2_008_vp_010_dollar_volume_shock_378_010, 8)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_008_vp_010_dollar_volume_shock_378_010'] = {'inputs': ['vp_base_universe_d2_008_vp_010_dollar_volume_shock_378_010'], 'func': vp_base_universe_d3_008_vp_010_dollar_volume_shock_378_010}


def vp_base_universe_d3_009_vp_011_volume_trend_slope_504_011(vp_base_universe_d2_009_vp_011_volume_trend_slope_504_011):
    return _base_universe_d3(vp_base_universe_d2_009_vp_011_volume_trend_slope_504_011, 9)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_009_vp_011_volume_trend_slope_504_011'] = {'inputs': ['vp_base_universe_d2_009_vp_011_volume_trend_slope_504_011'], 'func': vp_base_universe_d3_009_vp_011_volume_trend_slope_504_011}


def vp_base_universe_d3_010_vp_012_price_volume_divergence_756_012(vp_base_universe_d2_010_vp_012_price_volume_divergence_756_012):
    return _base_universe_d3(vp_base_universe_d2_010_vp_012_price_volume_divergence_756_012, 10)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_010_vp_012_price_volume_divergence_756_012'] = {'inputs': ['vp_base_universe_d2_010_vp_012_price_volume_divergence_756_012'], 'func': vp_base_universe_d3_010_vp_012_price_volume_divergence_756_012}


def vp_base_universe_d3_011_vp_014_volume_zscore_1260_014(vp_base_universe_d2_011_vp_014_volume_zscore_1260_014):
    return _base_universe_d3(vp_base_universe_d2_011_vp_014_volume_zscore_1260_014, 11)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_011_vp_014_volume_zscore_1260_014'] = {'inputs': ['vp_base_universe_d2_011_vp_014_volume_zscore_1260_014'], 'func': vp_base_universe_d3_011_vp_014_volume_zscore_1260_014}


def vp_base_universe_d3_012_vp_015_down_volume_share_1512_015(vp_base_universe_d2_012_vp_015_down_volume_share_1512_015):
    return _base_universe_d3(vp_base_universe_d2_012_vp_015_down_volume_share_1512_015, 12)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_012_vp_015_down_volume_share_1512_015'] = {'inputs': ['vp_base_universe_d2_012_vp_015_down_volume_share_1512_015'], 'func': vp_base_universe_d3_012_vp_015_down_volume_share_1512_015}


def vp_base_universe_d3_013_vp_016_dollar_volume_shock_5_016(vp_base_universe_d2_013_vp_016_dollar_volume_shock_5_016):
    return _base_universe_d3(vp_base_universe_d2_013_vp_016_dollar_volume_shock_5_016, 13)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_013_vp_016_dollar_volume_shock_5_016'] = {'inputs': ['vp_base_universe_d2_013_vp_016_dollar_volume_shock_5_016'], 'func': vp_base_universe_d3_013_vp_016_dollar_volume_shock_5_016}


def vp_base_universe_d3_014_vp_017_volume_trend_slope_10_017(vp_base_universe_d2_014_vp_017_volume_trend_slope_10_017):
    return _base_universe_d3(vp_base_universe_d2_014_vp_017_volume_trend_slope_10_017, 14)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_014_vp_017_volume_trend_slope_10_017'] = {'inputs': ['vp_base_universe_d2_014_vp_017_volume_trend_slope_10_017'], 'func': vp_base_universe_d3_014_vp_017_volume_trend_slope_10_017}


def vp_base_universe_d3_015_vp_018_price_volume_divergence_21_018(vp_base_universe_d2_015_vp_018_price_volume_divergence_21_018):
    return _base_universe_d3(vp_base_universe_d2_015_vp_018_price_volume_divergence_21_018, 15)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_015_vp_018_price_volume_divergence_21_018'] = {'inputs': ['vp_base_universe_d2_015_vp_018_price_volume_divergence_21_018'], 'func': vp_base_universe_d3_015_vp_018_price_volume_divergence_21_018}


def vp_base_universe_d3_016_vp_020_volume_zscore_63_020(vp_base_universe_d2_016_vp_020_volume_zscore_63_020):
    return _base_universe_d3(vp_base_universe_d2_016_vp_020_volume_zscore_63_020, 16)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_016_vp_020_volume_zscore_63_020'] = {'inputs': ['vp_base_universe_d2_016_vp_020_volume_zscore_63_020'], 'func': vp_base_universe_d3_016_vp_020_volume_zscore_63_020}


def vp_base_universe_d3_017_vp_021_down_volume_share_84_021(vp_base_universe_d2_017_vp_021_down_volume_share_84_021):
    return _base_universe_d3(vp_base_universe_d2_017_vp_021_down_volume_share_84_021, 17)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_017_vp_021_down_volume_share_84_021'] = {'inputs': ['vp_base_universe_d2_017_vp_021_down_volume_share_84_021'], 'func': vp_base_universe_d3_017_vp_021_down_volume_share_84_021}


def vp_base_universe_d3_018_vp_022_dollar_volume_shock_126_022(vp_base_universe_d2_018_vp_022_dollar_volume_shock_126_022):
    return _base_universe_d3(vp_base_universe_d2_018_vp_022_dollar_volume_shock_126_022, 18)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_018_vp_022_dollar_volume_shock_126_022'] = {'inputs': ['vp_base_universe_d2_018_vp_022_dollar_volume_shock_126_022'], 'func': vp_base_universe_d3_018_vp_022_dollar_volume_shock_126_022}


def vp_base_universe_d3_019_vp_023_volume_trend_slope_189_023(vp_base_universe_d2_019_vp_023_volume_trend_slope_189_023):
    return _base_universe_d3(vp_base_universe_d2_019_vp_023_volume_trend_slope_189_023, 19)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_019_vp_023_volume_trend_slope_189_023'] = {'inputs': ['vp_base_universe_d2_019_vp_023_volume_trend_slope_189_023'], 'func': vp_base_universe_d3_019_vp_023_volume_trend_slope_189_023}


def vp_base_universe_d3_020_vp_024_price_volume_divergence_252_024(vp_base_universe_d2_020_vp_024_price_volume_divergence_252_024):
    return _base_universe_d3(vp_base_universe_d2_020_vp_024_price_volume_divergence_252_024, 20)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_020_vp_024_price_volume_divergence_252_024'] = {'inputs': ['vp_base_universe_d2_020_vp_024_price_volume_divergence_252_024'], 'func': vp_base_universe_d3_020_vp_024_price_volume_divergence_252_024}


def vp_base_universe_d3_021_vp_026_volume_zscore_504_026(vp_base_universe_d2_021_vp_026_volume_zscore_504_026):
    return _base_universe_d3(vp_base_universe_d2_021_vp_026_volume_zscore_504_026, 21)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_021_vp_026_volume_zscore_504_026'] = {'inputs': ['vp_base_universe_d2_021_vp_026_volume_zscore_504_026'], 'func': vp_base_universe_d3_021_vp_026_volume_zscore_504_026}


def vp_base_universe_d3_022_vp_027_down_volume_share_756_027(vp_base_universe_d2_022_vp_027_down_volume_share_756_027):
    return _base_universe_d3(vp_base_universe_d2_022_vp_027_down_volume_share_756_027, 22)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_022_vp_027_down_volume_share_756_027'] = {'inputs': ['vp_base_universe_d2_022_vp_027_down_volume_share_756_027'], 'func': vp_base_universe_d3_022_vp_027_down_volume_share_756_027}


def vp_base_universe_d3_023_vp_028_dollar_volume_shock_1008_028(vp_base_universe_d2_023_vp_028_dollar_volume_shock_1008_028):
    return _base_universe_d3(vp_base_universe_d2_023_vp_028_dollar_volume_shock_1008_028, 23)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_023_vp_028_dollar_volume_shock_1008_028'] = {'inputs': ['vp_base_universe_d2_023_vp_028_dollar_volume_shock_1008_028'], 'func': vp_base_universe_d3_023_vp_028_dollar_volume_shock_1008_028}


def vp_base_universe_d3_024_vp_029_volume_trend_slope_1260_029(vp_base_universe_d2_024_vp_029_volume_trend_slope_1260_029):
    return _base_universe_d3(vp_base_universe_d2_024_vp_029_volume_trend_slope_1260_029, 24)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_024_vp_029_volume_trend_slope_1260_029'] = {'inputs': ['vp_base_universe_d2_024_vp_029_volume_trend_slope_1260_029'], 'func': vp_base_universe_d3_024_vp_029_volume_trend_slope_1260_029}


def vp_base_universe_d3_025_vp_030_price_volume_divergence_1512_030(vp_base_universe_d2_025_vp_030_price_volume_divergence_1512_030):
    return _base_universe_d3(vp_base_universe_d2_025_vp_030_price_volume_divergence_1512_030, 25)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_025_vp_030_price_volume_divergence_1512_030'] = {'inputs': ['vp_base_universe_d2_025_vp_030_price_volume_divergence_1512_030'], 'func': vp_base_universe_d3_025_vp_030_price_volume_divergence_1512_030}


def vp_base_universe_d3_026_vp_basefill_031(vp_base_universe_d2_026_vp_basefill_031):
    return _base_universe_d3(vp_base_universe_d2_026_vp_basefill_031, 26)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_026_vp_basefill_031'] = {'inputs': ['vp_base_universe_d2_026_vp_basefill_031'], 'func': vp_base_universe_d3_026_vp_basefill_031}


def vp_base_universe_d3_027_vp_basefill_032(vp_base_universe_d2_027_vp_basefill_032):
    return _base_universe_d3(vp_base_universe_d2_027_vp_basefill_032, 27)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_027_vp_basefill_032'] = {'inputs': ['vp_base_universe_d2_027_vp_basefill_032'], 'func': vp_base_universe_d3_027_vp_basefill_032}


def vp_base_universe_d3_028_vp_basefill_033(vp_base_universe_d2_028_vp_basefill_033):
    return _base_universe_d3(vp_base_universe_d2_028_vp_basefill_033, 28)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_028_vp_basefill_033'] = {'inputs': ['vp_base_universe_d2_028_vp_basefill_033'], 'func': vp_base_universe_d3_028_vp_basefill_033}


def vp_base_universe_d3_029_vp_basefill_034(vp_base_universe_d2_029_vp_basefill_034):
    return _base_universe_d3(vp_base_universe_d2_029_vp_basefill_034, 29)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_029_vp_basefill_034'] = {'inputs': ['vp_base_universe_d2_029_vp_basefill_034'], 'func': vp_base_universe_d3_029_vp_basefill_034}


def vp_base_universe_d3_030_vp_basefill_035(vp_base_universe_d2_030_vp_basefill_035):
    return _base_universe_d3(vp_base_universe_d2_030_vp_basefill_035, 30)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_030_vp_basefill_035'] = {'inputs': ['vp_base_universe_d2_030_vp_basefill_035'], 'func': vp_base_universe_d3_030_vp_basefill_035}


def vp_base_universe_d3_031_vp_basefill_036(vp_base_universe_d2_031_vp_basefill_036):
    return _base_universe_d3(vp_base_universe_d2_031_vp_basefill_036, 31)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_031_vp_basefill_036'] = {'inputs': ['vp_base_universe_d2_031_vp_basefill_036'], 'func': vp_base_universe_d3_031_vp_basefill_036}


def vp_base_universe_d3_032_vp_basefill_037(vp_base_universe_d2_032_vp_basefill_037):
    return _base_universe_d3(vp_base_universe_d2_032_vp_basefill_037, 32)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_032_vp_basefill_037'] = {'inputs': ['vp_base_universe_d2_032_vp_basefill_037'], 'func': vp_base_universe_d3_032_vp_basefill_037}


def vp_base_universe_d3_033_vp_basefill_038(vp_base_universe_d2_033_vp_basefill_038):
    return _base_universe_d3(vp_base_universe_d2_033_vp_basefill_038, 33)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_033_vp_basefill_038'] = {'inputs': ['vp_base_universe_d2_033_vp_basefill_038'], 'func': vp_base_universe_d3_033_vp_basefill_038}


def vp_base_universe_d3_034_vp_basefill_039(vp_base_universe_d2_034_vp_basefill_039):
    return _base_universe_d3(vp_base_universe_d2_034_vp_basefill_039, 34)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_034_vp_basefill_039'] = {'inputs': ['vp_base_universe_d2_034_vp_basefill_039'], 'func': vp_base_universe_d3_034_vp_basefill_039}


def vp_base_universe_d3_035_vp_basefill_040(vp_base_universe_d2_035_vp_basefill_040):
    return _base_universe_d3(vp_base_universe_d2_035_vp_basefill_040, 35)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_035_vp_basefill_040'] = {'inputs': ['vp_base_universe_d2_035_vp_basefill_040'], 'func': vp_base_universe_d3_035_vp_basefill_040}


def vp_base_universe_d3_036_vp_basefill_041(vp_base_universe_d2_036_vp_basefill_041):
    return _base_universe_d3(vp_base_universe_d2_036_vp_basefill_041, 36)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_036_vp_basefill_041'] = {'inputs': ['vp_base_universe_d2_036_vp_basefill_041'], 'func': vp_base_universe_d3_036_vp_basefill_041}


def vp_base_universe_d3_037_vp_basefill_042(vp_base_universe_d2_037_vp_basefill_042):
    return _base_universe_d3(vp_base_universe_d2_037_vp_basefill_042, 37)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_037_vp_basefill_042'] = {'inputs': ['vp_base_universe_d2_037_vp_basefill_042'], 'func': vp_base_universe_d3_037_vp_basefill_042}


def vp_base_universe_d3_038_vp_basefill_043(vp_base_universe_d2_038_vp_basefill_043):
    return _base_universe_d3(vp_base_universe_d2_038_vp_basefill_043, 38)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_038_vp_basefill_043'] = {'inputs': ['vp_base_universe_d2_038_vp_basefill_043'], 'func': vp_base_universe_d3_038_vp_basefill_043}


def vp_base_universe_d3_039_vp_basefill_044(vp_base_universe_d2_039_vp_basefill_044):
    return _base_universe_d3(vp_base_universe_d2_039_vp_basefill_044, 39)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_039_vp_basefill_044'] = {'inputs': ['vp_base_universe_d2_039_vp_basefill_044'], 'func': vp_base_universe_d3_039_vp_basefill_044}


def vp_base_universe_d3_040_vp_basefill_045(vp_base_universe_d2_040_vp_basefill_045):
    return _base_universe_d3(vp_base_universe_d2_040_vp_basefill_045, 40)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_040_vp_basefill_045'] = {'inputs': ['vp_base_universe_d2_040_vp_basefill_045'], 'func': vp_base_universe_d3_040_vp_basefill_045}


def vp_base_universe_d3_041_vp_basefill_046(vp_base_universe_d2_041_vp_basefill_046):
    return _base_universe_d3(vp_base_universe_d2_041_vp_basefill_046, 41)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_041_vp_basefill_046'] = {'inputs': ['vp_base_universe_d2_041_vp_basefill_046'], 'func': vp_base_universe_d3_041_vp_basefill_046}


def vp_base_universe_d3_042_vp_basefill_047(vp_base_universe_d2_042_vp_basefill_047):
    return _base_universe_d3(vp_base_universe_d2_042_vp_basefill_047, 42)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_042_vp_basefill_047'] = {'inputs': ['vp_base_universe_d2_042_vp_basefill_047'], 'func': vp_base_universe_d3_042_vp_basefill_047}


def vp_base_universe_d3_043_vp_basefill_048(vp_base_universe_d2_043_vp_basefill_048):
    return _base_universe_d3(vp_base_universe_d2_043_vp_basefill_048, 43)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_043_vp_basefill_048'] = {'inputs': ['vp_base_universe_d2_043_vp_basefill_048'], 'func': vp_base_universe_d3_043_vp_basefill_048}


def vp_base_universe_d3_044_vp_basefill_049(vp_base_universe_d2_044_vp_basefill_049):
    return _base_universe_d3(vp_base_universe_d2_044_vp_basefill_049, 44)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_044_vp_basefill_049'] = {'inputs': ['vp_base_universe_d2_044_vp_basefill_049'], 'func': vp_base_universe_d3_044_vp_basefill_049}


def vp_base_universe_d3_045_vp_basefill_050(vp_base_universe_d2_045_vp_basefill_050):
    return _base_universe_d3(vp_base_universe_d2_045_vp_basefill_050, 45)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_045_vp_basefill_050'] = {'inputs': ['vp_base_universe_d2_045_vp_basefill_050'], 'func': vp_base_universe_d3_045_vp_basefill_050}


def vp_base_universe_d3_046_vp_basefill_051(vp_base_universe_d2_046_vp_basefill_051):
    return _base_universe_d3(vp_base_universe_d2_046_vp_basefill_051, 46)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_046_vp_basefill_051'] = {'inputs': ['vp_base_universe_d2_046_vp_basefill_051'], 'func': vp_base_universe_d3_046_vp_basefill_051}


def vp_base_universe_d3_047_vp_basefill_052(vp_base_universe_d2_047_vp_basefill_052):
    return _base_universe_d3(vp_base_universe_d2_047_vp_basefill_052, 47)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_047_vp_basefill_052'] = {'inputs': ['vp_base_universe_d2_047_vp_basefill_052'], 'func': vp_base_universe_d3_047_vp_basefill_052}


def vp_base_universe_d3_048_vp_basefill_053(vp_base_universe_d2_048_vp_basefill_053):
    return _base_universe_d3(vp_base_universe_d2_048_vp_basefill_053, 48)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_048_vp_basefill_053'] = {'inputs': ['vp_base_universe_d2_048_vp_basefill_053'], 'func': vp_base_universe_d3_048_vp_basefill_053}


def vp_base_universe_d3_049_vp_basefill_054(vp_base_universe_d2_049_vp_basefill_054):
    return _base_universe_d3(vp_base_universe_d2_049_vp_basefill_054, 49)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_049_vp_basefill_054'] = {'inputs': ['vp_base_universe_d2_049_vp_basefill_054'], 'func': vp_base_universe_d3_049_vp_basefill_054}


def vp_base_universe_d3_050_vp_basefill_055(vp_base_universe_d2_050_vp_basefill_055):
    return _base_universe_d3(vp_base_universe_d2_050_vp_basefill_055, 50)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_050_vp_basefill_055'] = {'inputs': ['vp_base_universe_d2_050_vp_basefill_055'], 'func': vp_base_universe_d3_050_vp_basefill_055}


def vp_base_universe_d3_051_vp_basefill_056(vp_base_universe_d2_051_vp_basefill_056):
    return _base_universe_d3(vp_base_universe_d2_051_vp_basefill_056, 51)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_051_vp_basefill_056'] = {'inputs': ['vp_base_universe_d2_051_vp_basefill_056'], 'func': vp_base_universe_d3_051_vp_basefill_056}


def vp_base_universe_d3_052_vp_basefill_057(vp_base_universe_d2_052_vp_basefill_057):
    return _base_universe_d3(vp_base_universe_d2_052_vp_basefill_057, 52)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_052_vp_basefill_057'] = {'inputs': ['vp_base_universe_d2_052_vp_basefill_057'], 'func': vp_base_universe_d3_052_vp_basefill_057}


def vp_base_universe_d3_053_vp_basefill_058(vp_base_universe_d2_053_vp_basefill_058):
    return _base_universe_d3(vp_base_universe_d2_053_vp_basefill_058, 53)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_053_vp_basefill_058'] = {'inputs': ['vp_base_universe_d2_053_vp_basefill_058'], 'func': vp_base_universe_d3_053_vp_basefill_058}


def vp_base_universe_d3_054_vp_basefill_059(vp_base_universe_d2_054_vp_basefill_059):
    return _base_universe_d3(vp_base_universe_d2_054_vp_basefill_059, 54)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_054_vp_basefill_059'] = {'inputs': ['vp_base_universe_d2_054_vp_basefill_059'], 'func': vp_base_universe_d3_054_vp_basefill_059}


def vp_base_universe_d3_055_vp_basefill_060(vp_base_universe_d2_055_vp_basefill_060):
    return _base_universe_d3(vp_base_universe_d2_055_vp_basefill_060, 55)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_055_vp_basefill_060'] = {'inputs': ['vp_base_universe_d2_055_vp_basefill_060'], 'func': vp_base_universe_d3_055_vp_basefill_060}


def vp_base_universe_d3_056_vp_basefill_061(vp_base_universe_d2_056_vp_basefill_061):
    return _base_universe_d3(vp_base_universe_d2_056_vp_basefill_061, 56)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_056_vp_basefill_061'] = {'inputs': ['vp_base_universe_d2_056_vp_basefill_061'], 'func': vp_base_universe_d3_056_vp_basefill_061}


def vp_base_universe_d3_057_vp_basefill_062(vp_base_universe_d2_057_vp_basefill_062):
    return _base_universe_d3(vp_base_universe_d2_057_vp_basefill_062, 57)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_057_vp_basefill_062'] = {'inputs': ['vp_base_universe_d2_057_vp_basefill_062'], 'func': vp_base_universe_d3_057_vp_basefill_062}


def vp_base_universe_d3_058_vp_basefill_063(vp_base_universe_d2_058_vp_basefill_063):
    return _base_universe_d3(vp_base_universe_d2_058_vp_basefill_063, 58)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_058_vp_basefill_063'] = {'inputs': ['vp_base_universe_d2_058_vp_basefill_063'], 'func': vp_base_universe_d3_058_vp_basefill_063}


def vp_base_universe_d3_059_vp_basefill_064(vp_base_universe_d2_059_vp_basefill_064):
    return _base_universe_d3(vp_base_universe_d2_059_vp_basefill_064, 59)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_059_vp_basefill_064'] = {'inputs': ['vp_base_universe_d2_059_vp_basefill_064'], 'func': vp_base_universe_d3_059_vp_basefill_064}


def vp_base_universe_d3_060_vp_basefill_065(vp_base_universe_d2_060_vp_basefill_065):
    return _base_universe_d3(vp_base_universe_d2_060_vp_basefill_065, 60)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_060_vp_basefill_065'] = {'inputs': ['vp_base_universe_d2_060_vp_basefill_065'], 'func': vp_base_universe_d3_060_vp_basefill_065}


def vp_base_universe_d3_061_vp_basefill_066(vp_base_universe_d2_061_vp_basefill_066):
    return _base_universe_d3(vp_base_universe_d2_061_vp_basefill_066, 61)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_061_vp_basefill_066'] = {'inputs': ['vp_base_universe_d2_061_vp_basefill_066'], 'func': vp_base_universe_d3_061_vp_basefill_066}


def vp_base_universe_d3_062_vp_basefill_067(vp_base_universe_d2_062_vp_basefill_067):
    return _base_universe_d3(vp_base_universe_d2_062_vp_basefill_067, 62)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_062_vp_basefill_067'] = {'inputs': ['vp_base_universe_d2_062_vp_basefill_067'], 'func': vp_base_universe_d3_062_vp_basefill_067}


def vp_base_universe_d3_063_vp_basefill_068(vp_base_universe_d2_063_vp_basefill_068):
    return _base_universe_d3(vp_base_universe_d2_063_vp_basefill_068, 63)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_063_vp_basefill_068'] = {'inputs': ['vp_base_universe_d2_063_vp_basefill_068'], 'func': vp_base_universe_d3_063_vp_basefill_068}


def vp_base_universe_d3_064_vp_basefill_069(vp_base_universe_d2_064_vp_basefill_069):
    return _base_universe_d3(vp_base_universe_d2_064_vp_basefill_069, 64)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_064_vp_basefill_069'] = {'inputs': ['vp_base_universe_d2_064_vp_basefill_069'], 'func': vp_base_universe_d3_064_vp_basefill_069}


def vp_base_universe_d3_065_vp_basefill_070(vp_base_universe_d2_065_vp_basefill_070):
    return _base_universe_d3(vp_base_universe_d2_065_vp_basefill_070, 65)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_065_vp_basefill_070'] = {'inputs': ['vp_base_universe_d2_065_vp_basefill_070'], 'func': vp_base_universe_d3_065_vp_basefill_070}


def vp_base_universe_d3_066_vp_basefill_071(vp_base_universe_d2_066_vp_basefill_071):
    return _base_universe_d3(vp_base_universe_d2_066_vp_basefill_071, 66)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_066_vp_basefill_071'] = {'inputs': ['vp_base_universe_d2_066_vp_basefill_071'], 'func': vp_base_universe_d3_066_vp_basefill_071}


def vp_base_universe_d3_067_vp_basefill_072(vp_base_universe_d2_067_vp_basefill_072):
    return _base_universe_d3(vp_base_universe_d2_067_vp_basefill_072, 67)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_067_vp_basefill_072'] = {'inputs': ['vp_base_universe_d2_067_vp_basefill_072'], 'func': vp_base_universe_d3_067_vp_basefill_072}


def vp_base_universe_d3_068_vp_basefill_073(vp_base_universe_d2_068_vp_basefill_073):
    return _base_universe_d3(vp_base_universe_d2_068_vp_basefill_073, 68)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_068_vp_basefill_073'] = {'inputs': ['vp_base_universe_d2_068_vp_basefill_073'], 'func': vp_base_universe_d3_068_vp_basefill_073}


def vp_base_universe_d3_069_vp_basefill_074(vp_base_universe_d2_069_vp_basefill_074):
    return _base_universe_d3(vp_base_universe_d2_069_vp_basefill_074, 69)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_069_vp_basefill_074'] = {'inputs': ['vp_base_universe_d2_069_vp_basefill_074'], 'func': vp_base_universe_d3_069_vp_basefill_074}


def vp_base_universe_d3_070_vp_basefill_075(vp_base_universe_d2_070_vp_basefill_075):
    return _base_universe_d3(vp_base_universe_d2_070_vp_basefill_075, 70)
VP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vp_base_universe_d3_070_vp_basefill_075'] = {'inputs': ['vp_base_universe_d2_070_vp_basefill_075'], 'func': vp_base_universe_d3_070_vp_basefill_075}
