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



def vtr_176_vtr_001_volume_spike_ratio_5_001_accel_1(vtr_151_vtr_001_volume_spike_ratio_5_001_roc_1):
    feature = _s(vtr_151_vtr_001_volume_spike_ratio_5_001_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def vtr_177_vtr_007_volume_spike_ratio_126_007_accel_5(vtr_152_vtr_007_volume_spike_ratio_126_007_roc_5):
    feature = _s(vtr_152_vtr_007_volume_spike_ratio_126_007_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def vtr_178_vtr_013_volume_spike_ratio_1008_013_accel_42(vtr_153_vtr_013_volume_spike_ratio_1008_013_roc_42):
    feature = _s(vtr_153_vtr_013_volume_spike_ratio_1008_013_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def vtr_179_vtr_019_volume_spike_ratio_42_019_accel_126(vtr_154_vtr_019_volume_spike_ratio_42_019_roc_126):
    feature = _s(vtr_154_vtr_019_volume_spike_ratio_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def vtr_180_vtr_025_volume_spike_ratio_378_025_accel_378(vtr_155_vtr_025_volume_spike_ratio_378_025_roc_378):
    feature = _s(vtr_155_vtr_025_volume_spike_ratio_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















VOLUME_TREND_REGISTRY_3RD_DERIVATIVES = {
    'vtr_176_vtr_001_volume_spike_ratio_5_001_accel_1': {'inputs': ['vtr_151_vtr_001_volume_spike_ratio_5_001_roc_1'], 'func': vtr_176_vtr_001_volume_spike_ratio_5_001_accel_1},
    'vtr_177_vtr_007_volume_spike_ratio_126_007_accel_5': {'inputs': ['vtr_152_vtr_007_volume_spike_ratio_126_007_roc_5'], 'func': vtr_177_vtr_007_volume_spike_ratio_126_007_accel_5},
    'vtr_178_vtr_013_volume_spike_ratio_1008_013_accel_42': {'inputs': ['vtr_153_vtr_013_volume_spike_ratio_1008_013_roc_42'], 'func': vtr_178_vtr_013_volume_spike_ratio_1008_013_accel_42},
    'vtr_179_vtr_019_volume_spike_ratio_42_019_accel_126': {'inputs': ['vtr_154_vtr_019_volume_spike_ratio_42_019_roc_126'], 'func': vtr_179_vtr_019_volume_spike_ratio_42_019_accel_126},
    'vtr_180_vtr_025_volume_spike_ratio_378_025_accel_378': {'inputs': ['vtr_155_vtr_025_volume_spike_ratio_378_025_roc_378'], 'func': vtr_180_vtr_025_volume_spike_ratio_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def vt_replacement_d3_001(vt_replacement_d2_001):
    feature = _clean(vt_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_001'] = {'inputs': ['vt_replacement_d2_001'], 'func': vt_replacement_d3_001}


def vt_replacement_d3_002(vt_replacement_d2_002):
    feature = _clean(vt_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_002'] = {'inputs': ['vt_replacement_d2_002'], 'func': vt_replacement_d3_002}


def vt_replacement_d3_003(vt_replacement_d2_003):
    feature = _clean(vt_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_003'] = {'inputs': ['vt_replacement_d2_003'], 'func': vt_replacement_d3_003}


def vt_replacement_d3_004(vt_replacement_d2_004):
    feature = _clean(vt_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_004'] = {'inputs': ['vt_replacement_d2_004'], 'func': vt_replacement_d3_004}


def vt_replacement_d3_005(vt_replacement_d2_005):
    feature = _clean(vt_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_005'] = {'inputs': ['vt_replacement_d2_005'], 'func': vt_replacement_d3_005}


def vt_replacement_d3_006(vt_replacement_d2_006):
    feature = _clean(vt_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_006'] = {'inputs': ['vt_replacement_d2_006'], 'func': vt_replacement_d3_006}


def vt_replacement_d3_007(vt_replacement_d2_007):
    feature = _clean(vt_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_007'] = {'inputs': ['vt_replacement_d2_007'], 'func': vt_replacement_d3_007}


def vt_replacement_d3_008(vt_replacement_d2_008):
    feature = _clean(vt_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_008'] = {'inputs': ['vt_replacement_d2_008'], 'func': vt_replacement_d3_008}


def vt_replacement_d3_009(vt_replacement_d2_009):
    feature = _clean(vt_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_009'] = {'inputs': ['vt_replacement_d2_009'], 'func': vt_replacement_d3_009}


def vt_replacement_d3_010(vt_replacement_d2_010):
    feature = _clean(vt_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_010'] = {'inputs': ['vt_replacement_d2_010'], 'func': vt_replacement_d3_010}


def vt_replacement_d3_011(vt_replacement_d2_011):
    feature = _clean(vt_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_011'] = {'inputs': ['vt_replacement_d2_011'], 'func': vt_replacement_d3_011}


def vt_replacement_d3_012(vt_replacement_d2_012):
    feature = _clean(vt_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_012'] = {'inputs': ['vt_replacement_d2_012'], 'func': vt_replacement_d3_012}


def vt_replacement_d3_013(vt_replacement_d2_013):
    feature = _clean(vt_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_013'] = {'inputs': ['vt_replacement_d2_013'], 'func': vt_replacement_d3_013}


def vt_replacement_d3_014(vt_replacement_d2_014):
    feature = _clean(vt_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_014'] = {'inputs': ['vt_replacement_d2_014'], 'func': vt_replacement_d3_014}


def vt_replacement_d3_015(vt_replacement_d2_015):
    feature = _clean(vt_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_015'] = {'inputs': ['vt_replacement_d2_015'], 'func': vt_replacement_d3_015}


def vt_replacement_d3_016(vt_replacement_d2_016):
    feature = _clean(vt_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_016'] = {'inputs': ['vt_replacement_d2_016'], 'func': vt_replacement_d3_016}


def vt_replacement_d3_017(vt_replacement_d2_017):
    feature = _clean(vt_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_017'] = {'inputs': ['vt_replacement_d2_017'], 'func': vt_replacement_d3_017}


def vt_replacement_d3_018(vt_replacement_d2_018):
    feature = _clean(vt_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_018'] = {'inputs': ['vt_replacement_d2_018'], 'func': vt_replacement_d3_018}


def vt_replacement_d3_019(vt_replacement_d2_019):
    feature = _clean(vt_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_019'] = {'inputs': ['vt_replacement_d2_019'], 'func': vt_replacement_d3_019}


def vt_replacement_d3_020(vt_replacement_d2_020):
    feature = _clean(vt_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_020'] = {'inputs': ['vt_replacement_d2_020'], 'func': vt_replacement_d3_020}


def vt_replacement_d3_021(vt_replacement_d2_021):
    feature = _clean(vt_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_021'] = {'inputs': ['vt_replacement_d2_021'], 'func': vt_replacement_d3_021}


def vt_replacement_d3_022(vt_replacement_d2_022):
    feature = _clean(vt_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_022'] = {'inputs': ['vt_replacement_d2_022'], 'func': vt_replacement_d3_022}


def vt_replacement_d3_023(vt_replacement_d2_023):
    feature = _clean(vt_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_023'] = {'inputs': ['vt_replacement_d2_023'], 'func': vt_replacement_d3_023}


def vt_replacement_d3_024(vt_replacement_d2_024):
    feature = _clean(vt_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_024'] = {'inputs': ['vt_replacement_d2_024'], 'func': vt_replacement_d3_024}


def vt_replacement_d3_025(vt_replacement_d2_025):
    feature = _clean(vt_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_025'] = {'inputs': ['vt_replacement_d2_025'], 'func': vt_replacement_d3_025}


def vt_replacement_d3_026(vt_replacement_d2_026):
    feature = _clean(vt_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_026'] = {'inputs': ['vt_replacement_d2_026'], 'func': vt_replacement_d3_026}


def vt_replacement_d3_027(vt_replacement_d2_027):
    feature = _clean(vt_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_027'] = {'inputs': ['vt_replacement_d2_027'], 'func': vt_replacement_d3_027}


def vt_replacement_d3_028(vt_replacement_d2_028):
    feature = _clean(vt_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_028'] = {'inputs': ['vt_replacement_d2_028'], 'func': vt_replacement_d3_028}


def vt_replacement_d3_029(vt_replacement_d2_029):
    feature = _clean(vt_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_029'] = {'inputs': ['vt_replacement_d2_029'], 'func': vt_replacement_d3_029}


def vt_replacement_d3_030(vt_replacement_d2_030):
    feature = _clean(vt_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_030'] = {'inputs': ['vt_replacement_d2_030'], 'func': vt_replacement_d3_030}


def vt_replacement_d3_031(vt_replacement_d2_031):
    feature = _clean(vt_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_031'] = {'inputs': ['vt_replacement_d2_031'], 'func': vt_replacement_d3_031}


def vt_replacement_d3_032(vt_replacement_d2_032):
    feature = _clean(vt_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_032'] = {'inputs': ['vt_replacement_d2_032'], 'func': vt_replacement_d3_032}


def vt_replacement_d3_033(vt_replacement_d2_033):
    feature = _clean(vt_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_033'] = {'inputs': ['vt_replacement_d2_033'], 'func': vt_replacement_d3_033}


def vt_replacement_d3_034(vt_replacement_d2_034):
    feature = _clean(vt_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_034'] = {'inputs': ['vt_replacement_d2_034'], 'func': vt_replacement_d3_034}


def vt_replacement_d3_035(vt_replacement_d2_035):
    feature = _clean(vt_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_035'] = {'inputs': ['vt_replacement_d2_035'], 'func': vt_replacement_d3_035}


def vt_replacement_d3_036(vt_replacement_d2_036):
    feature = _clean(vt_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_036'] = {'inputs': ['vt_replacement_d2_036'], 'func': vt_replacement_d3_036}


def vt_replacement_d3_037(vt_replacement_d2_037):
    feature = _clean(vt_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_037'] = {'inputs': ['vt_replacement_d2_037'], 'func': vt_replacement_d3_037}


def vt_replacement_d3_038(vt_replacement_d2_038):
    feature = _clean(vt_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_038'] = {'inputs': ['vt_replacement_d2_038'], 'func': vt_replacement_d3_038}


def vt_replacement_d3_039(vt_replacement_d2_039):
    feature = _clean(vt_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_039'] = {'inputs': ['vt_replacement_d2_039'], 'func': vt_replacement_d3_039}


def vt_replacement_d3_040(vt_replacement_d2_040):
    feature = _clean(vt_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_040'] = {'inputs': ['vt_replacement_d2_040'], 'func': vt_replacement_d3_040}


def vt_replacement_d3_041(vt_replacement_d2_041):
    feature = _clean(vt_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_041'] = {'inputs': ['vt_replacement_d2_041'], 'func': vt_replacement_d3_041}


def vt_replacement_d3_042(vt_replacement_d2_042):
    feature = _clean(vt_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_042'] = {'inputs': ['vt_replacement_d2_042'], 'func': vt_replacement_d3_042}


def vt_replacement_d3_043(vt_replacement_d2_043):
    feature = _clean(vt_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_043'] = {'inputs': ['vt_replacement_d2_043'], 'func': vt_replacement_d3_043}


def vt_replacement_d3_044(vt_replacement_d2_044):
    feature = _clean(vt_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_044'] = {'inputs': ['vt_replacement_d2_044'], 'func': vt_replacement_d3_044}


def vt_replacement_d3_045(vt_replacement_d2_045):
    feature = _clean(vt_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_045'] = {'inputs': ['vt_replacement_d2_045'], 'func': vt_replacement_d3_045}


def vt_replacement_d3_046(vt_replacement_d2_046):
    feature = _clean(vt_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_046'] = {'inputs': ['vt_replacement_d2_046'], 'func': vt_replacement_d3_046}


def vt_replacement_d3_047(vt_replacement_d2_047):
    feature = _clean(vt_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_047'] = {'inputs': ['vt_replacement_d2_047'], 'func': vt_replacement_d3_047}


def vt_replacement_d3_048(vt_replacement_d2_048):
    feature = _clean(vt_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_048'] = {'inputs': ['vt_replacement_d2_048'], 'func': vt_replacement_d3_048}


def vt_replacement_d3_049(vt_replacement_d2_049):
    feature = _clean(vt_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_049'] = {'inputs': ['vt_replacement_d2_049'], 'func': vt_replacement_d3_049}


def vt_replacement_d3_050(vt_replacement_d2_050):
    feature = _clean(vt_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_050'] = {'inputs': ['vt_replacement_d2_050'], 'func': vt_replacement_d3_050}


def vt_replacement_d3_051(vt_replacement_d2_051):
    feature = _clean(vt_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_051'] = {'inputs': ['vt_replacement_d2_051'], 'func': vt_replacement_d3_051}


def vt_replacement_d3_052(vt_replacement_d2_052):
    feature = _clean(vt_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_052'] = {'inputs': ['vt_replacement_d2_052'], 'func': vt_replacement_d3_052}


def vt_replacement_d3_053(vt_replacement_d2_053):
    feature = _clean(vt_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_053'] = {'inputs': ['vt_replacement_d2_053'], 'func': vt_replacement_d3_053}


def vt_replacement_d3_054(vt_replacement_d2_054):
    feature = _clean(vt_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_054'] = {'inputs': ['vt_replacement_d2_054'], 'func': vt_replacement_d3_054}


def vt_replacement_d3_055(vt_replacement_d2_055):
    feature = _clean(vt_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_055'] = {'inputs': ['vt_replacement_d2_055'], 'func': vt_replacement_d3_055}


def vt_replacement_d3_056(vt_replacement_d2_056):
    feature = _clean(vt_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_056'] = {'inputs': ['vt_replacement_d2_056'], 'func': vt_replacement_d3_056}


def vt_replacement_d3_057(vt_replacement_d2_057):
    feature = _clean(vt_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_057'] = {'inputs': ['vt_replacement_d2_057'], 'func': vt_replacement_d3_057}


def vt_replacement_d3_058(vt_replacement_d2_058):
    feature = _clean(vt_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_058'] = {'inputs': ['vt_replacement_d2_058'], 'func': vt_replacement_d3_058}


def vt_replacement_d3_059(vt_replacement_d2_059):
    feature = _clean(vt_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_059'] = {'inputs': ['vt_replacement_d2_059'], 'func': vt_replacement_d3_059}


def vt_replacement_d3_060(vt_replacement_d2_060):
    feature = _clean(vt_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_060'] = {'inputs': ['vt_replacement_d2_060'], 'func': vt_replacement_d3_060}


def vt_replacement_d3_061(vt_replacement_d2_061):
    feature = _clean(vt_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_061'] = {'inputs': ['vt_replacement_d2_061'], 'func': vt_replacement_d3_061}


def vt_replacement_d3_062(vt_replacement_d2_062):
    feature = _clean(vt_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_062'] = {'inputs': ['vt_replacement_d2_062'], 'func': vt_replacement_d3_062}


def vt_replacement_d3_063(vt_replacement_d2_063):
    feature = _clean(vt_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_063'] = {'inputs': ['vt_replacement_d2_063'], 'func': vt_replacement_d3_063}


def vt_replacement_d3_064(vt_replacement_d2_064):
    feature = _clean(vt_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_064'] = {'inputs': ['vt_replacement_d2_064'], 'func': vt_replacement_d3_064}


def vt_replacement_d3_065(vt_replacement_d2_065):
    feature = _clean(vt_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_065'] = {'inputs': ['vt_replacement_d2_065'], 'func': vt_replacement_d3_065}


def vt_replacement_d3_066(vt_replacement_d2_066):
    feature = _clean(vt_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_066'] = {'inputs': ['vt_replacement_d2_066'], 'func': vt_replacement_d3_066}


def vt_replacement_d3_067(vt_replacement_d2_067):
    feature = _clean(vt_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_067'] = {'inputs': ['vt_replacement_d2_067'], 'func': vt_replacement_d3_067}


def vt_replacement_d3_068(vt_replacement_d2_068):
    feature = _clean(vt_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_068'] = {'inputs': ['vt_replacement_d2_068'], 'func': vt_replacement_d3_068}


def vt_replacement_d3_069(vt_replacement_d2_069):
    feature = _clean(vt_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_069'] = {'inputs': ['vt_replacement_d2_069'], 'func': vt_replacement_d3_069}


def vt_replacement_d3_070(vt_replacement_d2_070):
    feature = _clean(vt_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_070'] = {'inputs': ['vt_replacement_d2_070'], 'func': vt_replacement_d3_070}


def vt_replacement_d3_071(vt_replacement_d2_071):
    feature = _clean(vt_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_071'] = {'inputs': ['vt_replacement_d2_071'], 'func': vt_replacement_d3_071}


def vt_replacement_d3_072(vt_replacement_d2_072):
    feature = _clean(vt_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_072'] = {'inputs': ['vt_replacement_d2_072'], 'func': vt_replacement_d3_072}


def vt_replacement_d3_073(vt_replacement_d2_073):
    feature = _clean(vt_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_073'] = {'inputs': ['vt_replacement_d2_073'], 'func': vt_replacement_d3_073}


def vt_replacement_d3_074(vt_replacement_d2_074):
    feature = _clean(vt_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_074'] = {'inputs': ['vt_replacement_d2_074'], 'func': vt_replacement_d3_074}


def vt_replacement_d3_075(vt_replacement_d2_075):
    feature = _clean(vt_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_075'] = {'inputs': ['vt_replacement_d2_075'], 'func': vt_replacement_d3_075}


def vt_replacement_d3_076(vt_replacement_d2_076):
    feature = _clean(vt_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_076'] = {'inputs': ['vt_replacement_d2_076'], 'func': vt_replacement_d3_076}


def vt_replacement_d3_077(vt_replacement_d2_077):
    feature = _clean(vt_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_077'] = {'inputs': ['vt_replacement_d2_077'], 'func': vt_replacement_d3_077}


def vt_replacement_d3_078(vt_replacement_d2_078):
    feature = _clean(vt_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_078'] = {'inputs': ['vt_replacement_d2_078'], 'func': vt_replacement_d3_078}


def vt_replacement_d3_079(vt_replacement_d2_079):
    feature = _clean(vt_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_079'] = {'inputs': ['vt_replacement_d2_079'], 'func': vt_replacement_d3_079}


def vt_replacement_d3_080(vt_replacement_d2_080):
    feature = _clean(vt_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_080'] = {'inputs': ['vt_replacement_d2_080'], 'func': vt_replacement_d3_080}


def vt_replacement_d3_081(vt_replacement_d2_081):
    feature = _clean(vt_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_081'] = {'inputs': ['vt_replacement_d2_081'], 'func': vt_replacement_d3_081}


def vt_replacement_d3_082(vt_replacement_d2_082):
    feature = _clean(vt_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_082'] = {'inputs': ['vt_replacement_d2_082'], 'func': vt_replacement_d3_082}


def vt_replacement_d3_083(vt_replacement_d2_083):
    feature = _clean(vt_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_083'] = {'inputs': ['vt_replacement_d2_083'], 'func': vt_replacement_d3_083}


def vt_replacement_d3_084(vt_replacement_d2_084):
    feature = _clean(vt_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_084'] = {'inputs': ['vt_replacement_d2_084'], 'func': vt_replacement_d3_084}


def vt_replacement_d3_085(vt_replacement_d2_085):
    feature = _clean(vt_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_085'] = {'inputs': ['vt_replacement_d2_085'], 'func': vt_replacement_d3_085}


def vt_replacement_d3_086(vt_replacement_d2_086):
    feature = _clean(vt_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_086'] = {'inputs': ['vt_replacement_d2_086'], 'func': vt_replacement_d3_086}


def vt_replacement_d3_087(vt_replacement_d2_087):
    feature = _clean(vt_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_087'] = {'inputs': ['vt_replacement_d2_087'], 'func': vt_replacement_d3_087}


def vt_replacement_d3_088(vt_replacement_d2_088):
    feature = _clean(vt_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_088'] = {'inputs': ['vt_replacement_d2_088'], 'func': vt_replacement_d3_088}


def vt_replacement_d3_089(vt_replacement_d2_089):
    feature = _clean(vt_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_089'] = {'inputs': ['vt_replacement_d2_089'], 'func': vt_replacement_d3_089}


def vt_replacement_d3_090(vt_replacement_d2_090):
    feature = _clean(vt_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_090'] = {'inputs': ['vt_replacement_d2_090'], 'func': vt_replacement_d3_090}


def vt_replacement_d3_091(vt_replacement_d2_091):
    feature = _clean(vt_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_091'] = {'inputs': ['vt_replacement_d2_091'], 'func': vt_replacement_d3_091}


def vt_replacement_d3_092(vt_replacement_d2_092):
    feature = _clean(vt_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_092'] = {'inputs': ['vt_replacement_d2_092'], 'func': vt_replacement_d3_092}


def vt_replacement_d3_093(vt_replacement_d2_093):
    feature = _clean(vt_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_093'] = {'inputs': ['vt_replacement_d2_093'], 'func': vt_replacement_d3_093}


def vt_replacement_d3_094(vt_replacement_d2_094):
    feature = _clean(vt_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_094'] = {'inputs': ['vt_replacement_d2_094'], 'func': vt_replacement_d3_094}


def vt_replacement_d3_095(vt_replacement_d2_095):
    feature = _clean(vt_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_095'] = {'inputs': ['vt_replacement_d2_095'], 'func': vt_replacement_d3_095}


def vt_replacement_d3_096(vt_replacement_d2_096):
    feature = _clean(vt_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_096'] = {'inputs': ['vt_replacement_d2_096'], 'func': vt_replacement_d3_096}


def vt_replacement_d3_097(vt_replacement_d2_097):
    feature = _clean(vt_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_097'] = {'inputs': ['vt_replacement_d2_097'], 'func': vt_replacement_d3_097}


def vt_replacement_d3_098(vt_replacement_d2_098):
    feature = _clean(vt_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_098'] = {'inputs': ['vt_replacement_d2_098'], 'func': vt_replacement_d3_098}


def vt_replacement_d3_099(vt_replacement_d2_099):
    feature = _clean(vt_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_099'] = {'inputs': ['vt_replacement_d2_099'], 'func': vt_replacement_d3_099}


def vt_replacement_d3_100(vt_replacement_d2_100):
    feature = _clean(vt_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_100'] = {'inputs': ['vt_replacement_d2_100'], 'func': vt_replacement_d3_100}


def vt_replacement_d3_101(vt_replacement_d2_101):
    feature = _clean(vt_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_101'] = {'inputs': ['vt_replacement_d2_101'], 'func': vt_replacement_d3_101}


def vt_replacement_d3_102(vt_replacement_d2_102):
    feature = _clean(vt_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_102'] = {'inputs': ['vt_replacement_d2_102'], 'func': vt_replacement_d3_102}


def vt_replacement_d3_103(vt_replacement_d2_103):
    feature = _clean(vt_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_103'] = {'inputs': ['vt_replacement_d2_103'], 'func': vt_replacement_d3_103}


def vt_replacement_d3_104(vt_replacement_d2_104):
    feature = _clean(vt_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_104'] = {'inputs': ['vt_replacement_d2_104'], 'func': vt_replacement_d3_104}


def vt_replacement_d3_105(vt_replacement_d2_105):
    feature = _clean(vt_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_105'] = {'inputs': ['vt_replacement_d2_105'], 'func': vt_replacement_d3_105}


def vt_replacement_d3_106(vt_replacement_d2_106):
    feature = _clean(vt_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_106'] = {'inputs': ['vt_replacement_d2_106'], 'func': vt_replacement_d3_106}


def vt_replacement_d3_107(vt_replacement_d2_107):
    feature = _clean(vt_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_107'] = {'inputs': ['vt_replacement_d2_107'], 'func': vt_replacement_d3_107}


def vt_replacement_d3_108(vt_replacement_d2_108):
    feature = _clean(vt_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_108'] = {'inputs': ['vt_replacement_d2_108'], 'func': vt_replacement_d3_108}


def vt_replacement_d3_109(vt_replacement_d2_109):
    feature = _clean(vt_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_109'] = {'inputs': ['vt_replacement_d2_109'], 'func': vt_replacement_d3_109}


def vt_replacement_d3_110(vt_replacement_d2_110):
    feature = _clean(vt_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_110'] = {'inputs': ['vt_replacement_d2_110'], 'func': vt_replacement_d3_110}


def vt_replacement_d3_111(vt_replacement_d2_111):
    feature = _clean(vt_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_111'] = {'inputs': ['vt_replacement_d2_111'], 'func': vt_replacement_d3_111}


def vt_replacement_d3_112(vt_replacement_d2_112):
    feature = _clean(vt_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_112'] = {'inputs': ['vt_replacement_d2_112'], 'func': vt_replacement_d3_112}


def vt_replacement_d3_113(vt_replacement_d2_113):
    feature = _clean(vt_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_113'] = {'inputs': ['vt_replacement_d2_113'], 'func': vt_replacement_d3_113}


def vt_replacement_d3_114(vt_replacement_d2_114):
    feature = _clean(vt_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_114'] = {'inputs': ['vt_replacement_d2_114'], 'func': vt_replacement_d3_114}


def vt_replacement_d3_115(vt_replacement_d2_115):
    feature = _clean(vt_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_115'] = {'inputs': ['vt_replacement_d2_115'], 'func': vt_replacement_d3_115}


def vt_replacement_d3_116(vt_replacement_d2_116):
    feature = _clean(vt_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_116'] = {'inputs': ['vt_replacement_d2_116'], 'func': vt_replacement_d3_116}


def vt_replacement_d3_117(vt_replacement_d2_117):
    feature = _clean(vt_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_117'] = {'inputs': ['vt_replacement_d2_117'], 'func': vt_replacement_d3_117}


def vt_replacement_d3_118(vt_replacement_d2_118):
    feature = _clean(vt_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_118'] = {'inputs': ['vt_replacement_d2_118'], 'func': vt_replacement_d3_118}


def vt_replacement_d3_119(vt_replacement_d2_119):
    feature = _clean(vt_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_119'] = {'inputs': ['vt_replacement_d2_119'], 'func': vt_replacement_d3_119}


def vt_replacement_d3_120(vt_replacement_d2_120):
    feature = _clean(vt_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_120'] = {'inputs': ['vt_replacement_d2_120'], 'func': vt_replacement_d3_120}


def vt_replacement_d3_121(vt_replacement_d2_121):
    feature = _clean(vt_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_121'] = {'inputs': ['vt_replacement_d2_121'], 'func': vt_replacement_d3_121}


def vt_replacement_d3_122(vt_replacement_d2_122):
    feature = _clean(vt_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_122'] = {'inputs': ['vt_replacement_d2_122'], 'func': vt_replacement_d3_122}


def vt_replacement_d3_123(vt_replacement_d2_123):
    feature = _clean(vt_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_123'] = {'inputs': ['vt_replacement_d2_123'], 'func': vt_replacement_d3_123}


def vt_replacement_d3_124(vt_replacement_d2_124):
    feature = _clean(vt_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_124'] = {'inputs': ['vt_replacement_d2_124'], 'func': vt_replacement_d3_124}


def vt_replacement_d3_125(vt_replacement_d2_125):
    feature = _clean(vt_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_125'] = {'inputs': ['vt_replacement_d2_125'], 'func': vt_replacement_d3_125}


def vt_replacement_d3_126(vt_replacement_d2_126):
    feature = _clean(vt_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_126'] = {'inputs': ['vt_replacement_d2_126'], 'func': vt_replacement_d3_126}


def vt_replacement_d3_127(vt_replacement_d2_127):
    feature = _clean(vt_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_127'] = {'inputs': ['vt_replacement_d2_127'], 'func': vt_replacement_d3_127}


def vt_replacement_d3_128(vt_replacement_d2_128):
    feature = _clean(vt_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_128'] = {'inputs': ['vt_replacement_d2_128'], 'func': vt_replacement_d3_128}


def vt_replacement_d3_129(vt_replacement_d2_129):
    feature = _clean(vt_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_129'] = {'inputs': ['vt_replacement_d2_129'], 'func': vt_replacement_d3_129}


def vt_replacement_d3_130(vt_replacement_d2_130):
    feature = _clean(vt_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_130'] = {'inputs': ['vt_replacement_d2_130'], 'func': vt_replacement_d3_130}


def vt_replacement_d3_131(vt_replacement_d2_131):
    feature = _clean(vt_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_131'] = {'inputs': ['vt_replacement_d2_131'], 'func': vt_replacement_d3_131}


def vt_replacement_d3_132(vt_replacement_d2_132):
    feature = _clean(vt_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_132'] = {'inputs': ['vt_replacement_d2_132'], 'func': vt_replacement_d3_132}


def vt_replacement_d3_133(vt_replacement_d2_133):
    feature = _clean(vt_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_133'] = {'inputs': ['vt_replacement_d2_133'], 'func': vt_replacement_d3_133}


def vt_replacement_d3_134(vt_replacement_d2_134):
    feature = _clean(vt_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_134'] = {'inputs': ['vt_replacement_d2_134'], 'func': vt_replacement_d3_134}


def vt_replacement_d3_135(vt_replacement_d2_135):
    feature = _clean(vt_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_135'] = {'inputs': ['vt_replacement_d2_135'], 'func': vt_replacement_d3_135}


def vt_replacement_d3_136(vt_replacement_d2_136):
    feature = _clean(vt_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_136'] = {'inputs': ['vt_replacement_d2_136'], 'func': vt_replacement_d3_136}


def vt_replacement_d3_137(vt_replacement_d2_137):
    feature = _clean(vt_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_137'] = {'inputs': ['vt_replacement_d2_137'], 'func': vt_replacement_d3_137}


def vt_replacement_d3_138(vt_replacement_d2_138):
    feature = _clean(vt_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_138'] = {'inputs': ['vt_replacement_d2_138'], 'func': vt_replacement_d3_138}


def vt_replacement_d3_139(vt_replacement_d2_139):
    feature = _clean(vt_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_139'] = {'inputs': ['vt_replacement_d2_139'], 'func': vt_replacement_d3_139}


def vt_replacement_d3_140(vt_replacement_d2_140):
    feature = _clean(vt_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_140'] = {'inputs': ['vt_replacement_d2_140'], 'func': vt_replacement_d3_140}


def vt_replacement_d3_141(vt_replacement_d2_141):
    feature = _clean(vt_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_141'] = {'inputs': ['vt_replacement_d2_141'], 'func': vt_replacement_d3_141}


def vt_replacement_d3_142(vt_replacement_d2_142):
    feature = _clean(vt_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_142'] = {'inputs': ['vt_replacement_d2_142'], 'func': vt_replacement_d3_142}


def vt_replacement_d3_143(vt_replacement_d2_143):
    feature = _clean(vt_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_143'] = {'inputs': ['vt_replacement_d2_143'], 'func': vt_replacement_d3_143}


def vt_replacement_d3_144(vt_replacement_d2_144):
    feature = _clean(vt_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_144'] = {'inputs': ['vt_replacement_d2_144'], 'func': vt_replacement_d3_144}


def vt_replacement_d3_145(vt_replacement_d2_145):
    feature = _clean(vt_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_145'] = {'inputs': ['vt_replacement_d2_145'], 'func': vt_replacement_d3_145}


def vt_replacement_d3_146(vt_replacement_d2_146):
    feature = _clean(vt_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_146'] = {'inputs': ['vt_replacement_d2_146'], 'func': vt_replacement_d3_146}


def vt_replacement_d3_147(vt_replacement_d2_147):
    feature = _clean(vt_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_147'] = {'inputs': ['vt_replacement_d2_147'], 'func': vt_replacement_d3_147}


def vt_replacement_d3_148(vt_replacement_d2_148):
    feature = _clean(vt_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_148'] = {'inputs': ['vt_replacement_d2_148'], 'func': vt_replacement_d3_148}


def vt_replacement_d3_149(vt_replacement_d2_149):
    feature = _clean(vt_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_149'] = {'inputs': ['vt_replacement_d2_149'], 'func': vt_replacement_d3_149}


def vt_replacement_d3_150(vt_replacement_d2_150):
    feature = _clean(vt_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_150'] = {'inputs': ['vt_replacement_d2_150'], 'func': vt_replacement_d3_150}


def vt_replacement_d3_151(vt_replacement_d2_151):
    feature = _clean(vt_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_151'] = {'inputs': ['vt_replacement_d2_151'], 'func': vt_replacement_d3_151}


def vt_replacement_d3_152(vt_replacement_d2_152):
    feature = _clean(vt_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_152'] = {'inputs': ['vt_replacement_d2_152'], 'func': vt_replacement_d3_152}


def vt_replacement_d3_153(vt_replacement_d2_153):
    feature = _clean(vt_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_153'] = {'inputs': ['vt_replacement_d2_153'], 'func': vt_replacement_d3_153}


def vt_replacement_d3_154(vt_replacement_d2_154):
    feature = _clean(vt_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_154'] = {'inputs': ['vt_replacement_d2_154'], 'func': vt_replacement_d3_154}


def vt_replacement_d3_155(vt_replacement_d2_155):
    feature = _clean(vt_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_155'] = {'inputs': ['vt_replacement_d2_155'], 'func': vt_replacement_d3_155}


def vt_replacement_d3_156(vt_replacement_d2_156):
    feature = _clean(vt_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_156'] = {'inputs': ['vt_replacement_d2_156'], 'func': vt_replacement_d3_156}


def vt_replacement_d3_157(vt_replacement_d2_157):
    feature = _clean(vt_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_157'] = {'inputs': ['vt_replacement_d2_157'], 'func': vt_replacement_d3_157}


def vt_replacement_d3_158(vt_replacement_d2_158):
    feature = _clean(vt_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_158'] = {'inputs': ['vt_replacement_d2_158'], 'func': vt_replacement_d3_158}


def vt_replacement_d3_159(vt_replacement_d2_159):
    feature = _clean(vt_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_159'] = {'inputs': ['vt_replacement_d2_159'], 'func': vt_replacement_d3_159}


def vt_replacement_d3_160(vt_replacement_d2_160):
    feature = _clean(vt_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
VT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vt_replacement_d3_160'] = {'inputs': ['vt_replacement_d2_160'], 'func': vt_replacement_d3_160}


# Third-derivative extensions for repaired first-base features.
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def vtr_base_universe_d3_001_vtr_002_volume_zscore_10_002(vtr_base_universe_d2_001_vtr_002_volume_zscore_10_002):
    return _base_universe_d3(vtr_base_universe_d2_001_vtr_002_volume_zscore_10_002, 1)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_001_vtr_002_volume_zscore_10_002'] = {'inputs': ['vtr_base_universe_d2_001_vtr_002_volume_zscore_10_002'], 'func': vtr_base_universe_d3_001_vtr_002_volume_zscore_10_002}


def vtr_base_universe_d3_002_vtr_003_down_volume_share_21_003(vtr_base_universe_d2_002_vtr_003_down_volume_share_21_003):
    return _base_universe_d3(vtr_base_universe_d2_002_vtr_003_down_volume_share_21_003, 2)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_002_vtr_003_down_volume_share_21_003'] = {'inputs': ['vtr_base_universe_d2_002_vtr_003_down_volume_share_21_003'], 'func': vtr_base_universe_d3_002_vtr_003_down_volume_share_21_003}


def vtr_base_universe_d3_003_vtr_004_dollar_volume_shock_42_004(vtr_base_universe_d2_003_vtr_004_dollar_volume_shock_42_004):
    return _base_universe_d3(vtr_base_universe_d2_003_vtr_004_dollar_volume_shock_42_004, 3)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_003_vtr_004_dollar_volume_shock_42_004'] = {'inputs': ['vtr_base_universe_d2_003_vtr_004_dollar_volume_shock_42_004'], 'func': vtr_base_universe_d3_003_vtr_004_dollar_volume_shock_42_004}


def vtr_base_universe_d3_004_vtr_005_volume_trend_slope_63_005(vtr_base_universe_d2_004_vtr_005_volume_trend_slope_63_005):
    return _base_universe_d3(vtr_base_universe_d2_004_vtr_005_volume_trend_slope_63_005, 4)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_004_vtr_005_volume_trend_slope_63_005'] = {'inputs': ['vtr_base_universe_d2_004_vtr_005_volume_trend_slope_63_005'], 'func': vtr_base_universe_d3_004_vtr_005_volume_trend_slope_63_005}


def vtr_base_universe_d3_005_vtr_006_price_volume_divergence_84_006(vtr_base_universe_d2_005_vtr_006_price_volume_divergence_84_006):
    return _base_universe_d3(vtr_base_universe_d2_005_vtr_006_price_volume_divergence_84_006, 5)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_005_vtr_006_price_volume_divergence_84_006'] = {'inputs': ['vtr_base_universe_d2_005_vtr_006_price_volume_divergence_84_006'], 'func': vtr_base_universe_d3_005_vtr_006_price_volume_divergence_84_006}


def vtr_base_universe_d3_006_vtr_008_volume_zscore_189_008(vtr_base_universe_d2_006_vtr_008_volume_zscore_189_008):
    return _base_universe_d3(vtr_base_universe_d2_006_vtr_008_volume_zscore_189_008, 6)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_006_vtr_008_volume_zscore_189_008'] = {'inputs': ['vtr_base_universe_d2_006_vtr_008_volume_zscore_189_008'], 'func': vtr_base_universe_d3_006_vtr_008_volume_zscore_189_008}


def vtr_base_universe_d3_007_vtr_009_down_volume_share_252_009(vtr_base_universe_d2_007_vtr_009_down_volume_share_252_009):
    return _base_universe_d3(vtr_base_universe_d2_007_vtr_009_down_volume_share_252_009, 7)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_007_vtr_009_down_volume_share_252_009'] = {'inputs': ['vtr_base_universe_d2_007_vtr_009_down_volume_share_252_009'], 'func': vtr_base_universe_d3_007_vtr_009_down_volume_share_252_009}


def vtr_base_universe_d3_008_vtr_010_dollar_volume_shock_378_010(vtr_base_universe_d2_008_vtr_010_dollar_volume_shock_378_010):
    return _base_universe_d3(vtr_base_universe_d2_008_vtr_010_dollar_volume_shock_378_010, 8)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_008_vtr_010_dollar_volume_shock_378_010'] = {'inputs': ['vtr_base_universe_d2_008_vtr_010_dollar_volume_shock_378_010'], 'func': vtr_base_universe_d3_008_vtr_010_dollar_volume_shock_378_010}


def vtr_base_universe_d3_009_vtr_011_volume_trend_slope_504_011(vtr_base_universe_d2_009_vtr_011_volume_trend_slope_504_011):
    return _base_universe_d3(vtr_base_universe_d2_009_vtr_011_volume_trend_slope_504_011, 9)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_009_vtr_011_volume_trend_slope_504_011'] = {'inputs': ['vtr_base_universe_d2_009_vtr_011_volume_trend_slope_504_011'], 'func': vtr_base_universe_d3_009_vtr_011_volume_trend_slope_504_011}


def vtr_base_universe_d3_010_vtr_012_price_volume_divergence_756_012(vtr_base_universe_d2_010_vtr_012_price_volume_divergence_756_012):
    return _base_universe_d3(vtr_base_universe_d2_010_vtr_012_price_volume_divergence_756_012, 10)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_010_vtr_012_price_volume_divergence_756_012'] = {'inputs': ['vtr_base_universe_d2_010_vtr_012_price_volume_divergence_756_012'], 'func': vtr_base_universe_d3_010_vtr_012_price_volume_divergence_756_012}


def vtr_base_universe_d3_011_vtr_014_volume_zscore_1260_014(vtr_base_universe_d2_011_vtr_014_volume_zscore_1260_014):
    return _base_universe_d3(vtr_base_universe_d2_011_vtr_014_volume_zscore_1260_014, 11)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_011_vtr_014_volume_zscore_1260_014'] = {'inputs': ['vtr_base_universe_d2_011_vtr_014_volume_zscore_1260_014'], 'func': vtr_base_universe_d3_011_vtr_014_volume_zscore_1260_014}


def vtr_base_universe_d3_012_vtr_015_down_volume_share_1512_015(vtr_base_universe_d2_012_vtr_015_down_volume_share_1512_015):
    return _base_universe_d3(vtr_base_universe_d2_012_vtr_015_down_volume_share_1512_015, 12)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_012_vtr_015_down_volume_share_1512_015'] = {'inputs': ['vtr_base_universe_d2_012_vtr_015_down_volume_share_1512_015'], 'func': vtr_base_universe_d3_012_vtr_015_down_volume_share_1512_015}


def vtr_base_universe_d3_013_vtr_016_dollar_volume_shock_5_016(vtr_base_universe_d2_013_vtr_016_dollar_volume_shock_5_016):
    return _base_universe_d3(vtr_base_universe_d2_013_vtr_016_dollar_volume_shock_5_016, 13)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_013_vtr_016_dollar_volume_shock_5_016'] = {'inputs': ['vtr_base_universe_d2_013_vtr_016_dollar_volume_shock_5_016'], 'func': vtr_base_universe_d3_013_vtr_016_dollar_volume_shock_5_016}


def vtr_base_universe_d3_014_vtr_017_volume_trend_slope_10_017(vtr_base_universe_d2_014_vtr_017_volume_trend_slope_10_017):
    return _base_universe_d3(vtr_base_universe_d2_014_vtr_017_volume_trend_slope_10_017, 14)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_014_vtr_017_volume_trend_slope_10_017'] = {'inputs': ['vtr_base_universe_d2_014_vtr_017_volume_trend_slope_10_017'], 'func': vtr_base_universe_d3_014_vtr_017_volume_trend_slope_10_017}


def vtr_base_universe_d3_015_vtr_018_price_volume_divergence_21_018(vtr_base_universe_d2_015_vtr_018_price_volume_divergence_21_018):
    return _base_universe_d3(vtr_base_universe_d2_015_vtr_018_price_volume_divergence_21_018, 15)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_015_vtr_018_price_volume_divergence_21_018'] = {'inputs': ['vtr_base_universe_d2_015_vtr_018_price_volume_divergence_21_018'], 'func': vtr_base_universe_d3_015_vtr_018_price_volume_divergence_21_018}


def vtr_base_universe_d3_016_vtr_020_volume_zscore_63_020(vtr_base_universe_d2_016_vtr_020_volume_zscore_63_020):
    return _base_universe_d3(vtr_base_universe_d2_016_vtr_020_volume_zscore_63_020, 16)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_016_vtr_020_volume_zscore_63_020'] = {'inputs': ['vtr_base_universe_d2_016_vtr_020_volume_zscore_63_020'], 'func': vtr_base_universe_d3_016_vtr_020_volume_zscore_63_020}


def vtr_base_universe_d3_017_vtr_021_down_volume_share_84_021(vtr_base_universe_d2_017_vtr_021_down_volume_share_84_021):
    return _base_universe_d3(vtr_base_universe_d2_017_vtr_021_down_volume_share_84_021, 17)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_017_vtr_021_down_volume_share_84_021'] = {'inputs': ['vtr_base_universe_d2_017_vtr_021_down_volume_share_84_021'], 'func': vtr_base_universe_d3_017_vtr_021_down_volume_share_84_021}


def vtr_base_universe_d3_018_vtr_022_dollar_volume_shock_126_022(vtr_base_universe_d2_018_vtr_022_dollar_volume_shock_126_022):
    return _base_universe_d3(vtr_base_universe_d2_018_vtr_022_dollar_volume_shock_126_022, 18)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_018_vtr_022_dollar_volume_shock_126_022'] = {'inputs': ['vtr_base_universe_d2_018_vtr_022_dollar_volume_shock_126_022'], 'func': vtr_base_universe_d3_018_vtr_022_dollar_volume_shock_126_022}


def vtr_base_universe_d3_019_vtr_023_volume_trend_slope_189_023(vtr_base_universe_d2_019_vtr_023_volume_trend_slope_189_023):
    return _base_universe_d3(vtr_base_universe_d2_019_vtr_023_volume_trend_slope_189_023, 19)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_019_vtr_023_volume_trend_slope_189_023'] = {'inputs': ['vtr_base_universe_d2_019_vtr_023_volume_trend_slope_189_023'], 'func': vtr_base_universe_d3_019_vtr_023_volume_trend_slope_189_023}


def vtr_base_universe_d3_020_vtr_024_price_volume_divergence_252_024(vtr_base_universe_d2_020_vtr_024_price_volume_divergence_252_024):
    return _base_universe_d3(vtr_base_universe_d2_020_vtr_024_price_volume_divergence_252_024, 20)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_020_vtr_024_price_volume_divergence_252_024'] = {'inputs': ['vtr_base_universe_d2_020_vtr_024_price_volume_divergence_252_024'], 'func': vtr_base_universe_d3_020_vtr_024_price_volume_divergence_252_024}


def vtr_base_universe_d3_021_vtr_026_volume_zscore_504_026(vtr_base_universe_d2_021_vtr_026_volume_zscore_504_026):
    return _base_universe_d3(vtr_base_universe_d2_021_vtr_026_volume_zscore_504_026, 21)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_021_vtr_026_volume_zscore_504_026'] = {'inputs': ['vtr_base_universe_d2_021_vtr_026_volume_zscore_504_026'], 'func': vtr_base_universe_d3_021_vtr_026_volume_zscore_504_026}


def vtr_base_universe_d3_022_vtr_027_down_volume_share_756_027(vtr_base_universe_d2_022_vtr_027_down_volume_share_756_027):
    return _base_universe_d3(vtr_base_universe_d2_022_vtr_027_down_volume_share_756_027, 22)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_022_vtr_027_down_volume_share_756_027'] = {'inputs': ['vtr_base_universe_d2_022_vtr_027_down_volume_share_756_027'], 'func': vtr_base_universe_d3_022_vtr_027_down_volume_share_756_027}


def vtr_base_universe_d3_023_vtr_028_dollar_volume_shock_1008_028(vtr_base_universe_d2_023_vtr_028_dollar_volume_shock_1008_028):
    return _base_universe_d3(vtr_base_universe_d2_023_vtr_028_dollar_volume_shock_1008_028, 23)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_023_vtr_028_dollar_volume_shock_1008_028'] = {'inputs': ['vtr_base_universe_d2_023_vtr_028_dollar_volume_shock_1008_028'], 'func': vtr_base_universe_d3_023_vtr_028_dollar_volume_shock_1008_028}


def vtr_base_universe_d3_024_vtr_029_volume_trend_slope_1260_029(vtr_base_universe_d2_024_vtr_029_volume_trend_slope_1260_029):
    return _base_universe_d3(vtr_base_universe_d2_024_vtr_029_volume_trend_slope_1260_029, 24)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_024_vtr_029_volume_trend_slope_1260_029'] = {'inputs': ['vtr_base_universe_d2_024_vtr_029_volume_trend_slope_1260_029'], 'func': vtr_base_universe_d3_024_vtr_029_volume_trend_slope_1260_029}


def vtr_base_universe_d3_025_vtr_030_price_volume_divergence_1512_030(vtr_base_universe_d2_025_vtr_030_price_volume_divergence_1512_030):
    return _base_universe_d3(vtr_base_universe_d2_025_vtr_030_price_volume_divergence_1512_030, 25)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_025_vtr_030_price_volume_divergence_1512_030'] = {'inputs': ['vtr_base_universe_d2_025_vtr_030_price_volume_divergence_1512_030'], 'func': vtr_base_universe_d3_025_vtr_030_price_volume_divergence_1512_030}


def vtr_base_universe_d3_026_vtr_basefill_031(vtr_base_universe_d2_026_vtr_basefill_031):
    return _base_universe_d3(vtr_base_universe_d2_026_vtr_basefill_031, 26)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_026_vtr_basefill_031'] = {'inputs': ['vtr_base_universe_d2_026_vtr_basefill_031'], 'func': vtr_base_universe_d3_026_vtr_basefill_031}


def vtr_base_universe_d3_027_vtr_basefill_032(vtr_base_universe_d2_027_vtr_basefill_032):
    return _base_universe_d3(vtr_base_universe_d2_027_vtr_basefill_032, 27)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_027_vtr_basefill_032'] = {'inputs': ['vtr_base_universe_d2_027_vtr_basefill_032'], 'func': vtr_base_universe_d3_027_vtr_basefill_032}


def vtr_base_universe_d3_028_vtr_basefill_033(vtr_base_universe_d2_028_vtr_basefill_033):
    return _base_universe_d3(vtr_base_universe_d2_028_vtr_basefill_033, 28)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_028_vtr_basefill_033'] = {'inputs': ['vtr_base_universe_d2_028_vtr_basefill_033'], 'func': vtr_base_universe_d3_028_vtr_basefill_033}


def vtr_base_universe_d3_029_vtr_basefill_034(vtr_base_universe_d2_029_vtr_basefill_034):
    return _base_universe_d3(vtr_base_universe_d2_029_vtr_basefill_034, 29)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_029_vtr_basefill_034'] = {'inputs': ['vtr_base_universe_d2_029_vtr_basefill_034'], 'func': vtr_base_universe_d3_029_vtr_basefill_034}


def vtr_base_universe_d3_030_vtr_basefill_035(vtr_base_universe_d2_030_vtr_basefill_035):
    return _base_universe_d3(vtr_base_universe_d2_030_vtr_basefill_035, 30)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_030_vtr_basefill_035'] = {'inputs': ['vtr_base_universe_d2_030_vtr_basefill_035'], 'func': vtr_base_universe_d3_030_vtr_basefill_035}


def vtr_base_universe_d3_031_vtr_basefill_036(vtr_base_universe_d2_031_vtr_basefill_036):
    return _base_universe_d3(vtr_base_universe_d2_031_vtr_basefill_036, 31)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_031_vtr_basefill_036'] = {'inputs': ['vtr_base_universe_d2_031_vtr_basefill_036'], 'func': vtr_base_universe_d3_031_vtr_basefill_036}


def vtr_base_universe_d3_032_vtr_basefill_037(vtr_base_universe_d2_032_vtr_basefill_037):
    return _base_universe_d3(vtr_base_universe_d2_032_vtr_basefill_037, 32)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_032_vtr_basefill_037'] = {'inputs': ['vtr_base_universe_d2_032_vtr_basefill_037'], 'func': vtr_base_universe_d3_032_vtr_basefill_037}


def vtr_base_universe_d3_033_vtr_basefill_038(vtr_base_universe_d2_033_vtr_basefill_038):
    return _base_universe_d3(vtr_base_universe_d2_033_vtr_basefill_038, 33)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_033_vtr_basefill_038'] = {'inputs': ['vtr_base_universe_d2_033_vtr_basefill_038'], 'func': vtr_base_universe_d3_033_vtr_basefill_038}


def vtr_base_universe_d3_034_vtr_basefill_039(vtr_base_universe_d2_034_vtr_basefill_039):
    return _base_universe_d3(vtr_base_universe_d2_034_vtr_basefill_039, 34)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_034_vtr_basefill_039'] = {'inputs': ['vtr_base_universe_d2_034_vtr_basefill_039'], 'func': vtr_base_universe_d3_034_vtr_basefill_039}


def vtr_base_universe_d3_035_vtr_basefill_040(vtr_base_universe_d2_035_vtr_basefill_040):
    return _base_universe_d3(vtr_base_universe_d2_035_vtr_basefill_040, 35)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_035_vtr_basefill_040'] = {'inputs': ['vtr_base_universe_d2_035_vtr_basefill_040'], 'func': vtr_base_universe_d3_035_vtr_basefill_040}


def vtr_base_universe_d3_036_vtr_basefill_041(vtr_base_universe_d2_036_vtr_basefill_041):
    return _base_universe_d3(vtr_base_universe_d2_036_vtr_basefill_041, 36)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_036_vtr_basefill_041'] = {'inputs': ['vtr_base_universe_d2_036_vtr_basefill_041'], 'func': vtr_base_universe_d3_036_vtr_basefill_041}


def vtr_base_universe_d3_037_vtr_basefill_042(vtr_base_universe_d2_037_vtr_basefill_042):
    return _base_universe_d3(vtr_base_universe_d2_037_vtr_basefill_042, 37)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_037_vtr_basefill_042'] = {'inputs': ['vtr_base_universe_d2_037_vtr_basefill_042'], 'func': vtr_base_universe_d3_037_vtr_basefill_042}


def vtr_base_universe_d3_038_vtr_basefill_043(vtr_base_universe_d2_038_vtr_basefill_043):
    return _base_universe_d3(vtr_base_universe_d2_038_vtr_basefill_043, 38)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_038_vtr_basefill_043'] = {'inputs': ['vtr_base_universe_d2_038_vtr_basefill_043'], 'func': vtr_base_universe_d3_038_vtr_basefill_043}


def vtr_base_universe_d3_039_vtr_basefill_044(vtr_base_universe_d2_039_vtr_basefill_044):
    return _base_universe_d3(vtr_base_universe_d2_039_vtr_basefill_044, 39)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_039_vtr_basefill_044'] = {'inputs': ['vtr_base_universe_d2_039_vtr_basefill_044'], 'func': vtr_base_universe_d3_039_vtr_basefill_044}


def vtr_base_universe_d3_040_vtr_basefill_045(vtr_base_universe_d2_040_vtr_basefill_045):
    return _base_universe_d3(vtr_base_universe_d2_040_vtr_basefill_045, 40)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_040_vtr_basefill_045'] = {'inputs': ['vtr_base_universe_d2_040_vtr_basefill_045'], 'func': vtr_base_universe_d3_040_vtr_basefill_045}


def vtr_base_universe_d3_041_vtr_basefill_046(vtr_base_universe_d2_041_vtr_basefill_046):
    return _base_universe_d3(vtr_base_universe_d2_041_vtr_basefill_046, 41)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_041_vtr_basefill_046'] = {'inputs': ['vtr_base_universe_d2_041_vtr_basefill_046'], 'func': vtr_base_universe_d3_041_vtr_basefill_046}


def vtr_base_universe_d3_042_vtr_basefill_047(vtr_base_universe_d2_042_vtr_basefill_047):
    return _base_universe_d3(vtr_base_universe_d2_042_vtr_basefill_047, 42)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_042_vtr_basefill_047'] = {'inputs': ['vtr_base_universe_d2_042_vtr_basefill_047'], 'func': vtr_base_universe_d3_042_vtr_basefill_047}


def vtr_base_universe_d3_043_vtr_basefill_048(vtr_base_universe_d2_043_vtr_basefill_048):
    return _base_universe_d3(vtr_base_universe_d2_043_vtr_basefill_048, 43)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_043_vtr_basefill_048'] = {'inputs': ['vtr_base_universe_d2_043_vtr_basefill_048'], 'func': vtr_base_universe_d3_043_vtr_basefill_048}


def vtr_base_universe_d3_044_vtr_basefill_049(vtr_base_universe_d2_044_vtr_basefill_049):
    return _base_universe_d3(vtr_base_universe_d2_044_vtr_basefill_049, 44)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_044_vtr_basefill_049'] = {'inputs': ['vtr_base_universe_d2_044_vtr_basefill_049'], 'func': vtr_base_universe_d3_044_vtr_basefill_049}


def vtr_base_universe_d3_045_vtr_basefill_050(vtr_base_universe_d2_045_vtr_basefill_050):
    return _base_universe_d3(vtr_base_universe_d2_045_vtr_basefill_050, 45)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_045_vtr_basefill_050'] = {'inputs': ['vtr_base_universe_d2_045_vtr_basefill_050'], 'func': vtr_base_universe_d3_045_vtr_basefill_050}


def vtr_base_universe_d3_046_vtr_basefill_051(vtr_base_universe_d2_046_vtr_basefill_051):
    return _base_universe_d3(vtr_base_universe_d2_046_vtr_basefill_051, 46)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_046_vtr_basefill_051'] = {'inputs': ['vtr_base_universe_d2_046_vtr_basefill_051'], 'func': vtr_base_universe_d3_046_vtr_basefill_051}


def vtr_base_universe_d3_047_vtr_basefill_052(vtr_base_universe_d2_047_vtr_basefill_052):
    return _base_universe_d3(vtr_base_universe_d2_047_vtr_basefill_052, 47)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_047_vtr_basefill_052'] = {'inputs': ['vtr_base_universe_d2_047_vtr_basefill_052'], 'func': vtr_base_universe_d3_047_vtr_basefill_052}


def vtr_base_universe_d3_048_vtr_basefill_053(vtr_base_universe_d2_048_vtr_basefill_053):
    return _base_universe_d3(vtr_base_universe_d2_048_vtr_basefill_053, 48)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_048_vtr_basefill_053'] = {'inputs': ['vtr_base_universe_d2_048_vtr_basefill_053'], 'func': vtr_base_universe_d3_048_vtr_basefill_053}


def vtr_base_universe_d3_049_vtr_basefill_054(vtr_base_universe_d2_049_vtr_basefill_054):
    return _base_universe_d3(vtr_base_universe_d2_049_vtr_basefill_054, 49)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_049_vtr_basefill_054'] = {'inputs': ['vtr_base_universe_d2_049_vtr_basefill_054'], 'func': vtr_base_universe_d3_049_vtr_basefill_054}


def vtr_base_universe_d3_050_vtr_basefill_055(vtr_base_universe_d2_050_vtr_basefill_055):
    return _base_universe_d3(vtr_base_universe_d2_050_vtr_basefill_055, 50)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_050_vtr_basefill_055'] = {'inputs': ['vtr_base_universe_d2_050_vtr_basefill_055'], 'func': vtr_base_universe_d3_050_vtr_basefill_055}


def vtr_base_universe_d3_051_vtr_basefill_056(vtr_base_universe_d2_051_vtr_basefill_056):
    return _base_universe_d3(vtr_base_universe_d2_051_vtr_basefill_056, 51)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_051_vtr_basefill_056'] = {'inputs': ['vtr_base_universe_d2_051_vtr_basefill_056'], 'func': vtr_base_universe_d3_051_vtr_basefill_056}


def vtr_base_universe_d3_052_vtr_basefill_057(vtr_base_universe_d2_052_vtr_basefill_057):
    return _base_universe_d3(vtr_base_universe_d2_052_vtr_basefill_057, 52)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_052_vtr_basefill_057'] = {'inputs': ['vtr_base_universe_d2_052_vtr_basefill_057'], 'func': vtr_base_universe_d3_052_vtr_basefill_057}


def vtr_base_universe_d3_053_vtr_basefill_058(vtr_base_universe_d2_053_vtr_basefill_058):
    return _base_universe_d3(vtr_base_universe_d2_053_vtr_basefill_058, 53)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_053_vtr_basefill_058'] = {'inputs': ['vtr_base_universe_d2_053_vtr_basefill_058'], 'func': vtr_base_universe_d3_053_vtr_basefill_058}


def vtr_base_universe_d3_054_vtr_basefill_059(vtr_base_universe_d2_054_vtr_basefill_059):
    return _base_universe_d3(vtr_base_universe_d2_054_vtr_basefill_059, 54)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_054_vtr_basefill_059'] = {'inputs': ['vtr_base_universe_d2_054_vtr_basefill_059'], 'func': vtr_base_universe_d3_054_vtr_basefill_059}


def vtr_base_universe_d3_055_vtr_basefill_060(vtr_base_universe_d2_055_vtr_basefill_060):
    return _base_universe_d3(vtr_base_universe_d2_055_vtr_basefill_060, 55)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_055_vtr_basefill_060'] = {'inputs': ['vtr_base_universe_d2_055_vtr_basefill_060'], 'func': vtr_base_universe_d3_055_vtr_basefill_060}


def vtr_base_universe_d3_056_vtr_basefill_061(vtr_base_universe_d2_056_vtr_basefill_061):
    return _base_universe_d3(vtr_base_universe_d2_056_vtr_basefill_061, 56)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_056_vtr_basefill_061'] = {'inputs': ['vtr_base_universe_d2_056_vtr_basefill_061'], 'func': vtr_base_universe_d3_056_vtr_basefill_061}


def vtr_base_universe_d3_057_vtr_basefill_062(vtr_base_universe_d2_057_vtr_basefill_062):
    return _base_universe_d3(vtr_base_universe_d2_057_vtr_basefill_062, 57)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_057_vtr_basefill_062'] = {'inputs': ['vtr_base_universe_d2_057_vtr_basefill_062'], 'func': vtr_base_universe_d3_057_vtr_basefill_062}


def vtr_base_universe_d3_058_vtr_basefill_063(vtr_base_universe_d2_058_vtr_basefill_063):
    return _base_universe_d3(vtr_base_universe_d2_058_vtr_basefill_063, 58)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_058_vtr_basefill_063'] = {'inputs': ['vtr_base_universe_d2_058_vtr_basefill_063'], 'func': vtr_base_universe_d3_058_vtr_basefill_063}


def vtr_base_universe_d3_059_vtr_basefill_064(vtr_base_universe_d2_059_vtr_basefill_064):
    return _base_universe_d3(vtr_base_universe_d2_059_vtr_basefill_064, 59)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_059_vtr_basefill_064'] = {'inputs': ['vtr_base_universe_d2_059_vtr_basefill_064'], 'func': vtr_base_universe_d3_059_vtr_basefill_064}


def vtr_base_universe_d3_060_vtr_basefill_065(vtr_base_universe_d2_060_vtr_basefill_065):
    return _base_universe_d3(vtr_base_universe_d2_060_vtr_basefill_065, 60)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_060_vtr_basefill_065'] = {'inputs': ['vtr_base_universe_d2_060_vtr_basefill_065'], 'func': vtr_base_universe_d3_060_vtr_basefill_065}


def vtr_base_universe_d3_061_vtr_basefill_066(vtr_base_universe_d2_061_vtr_basefill_066):
    return _base_universe_d3(vtr_base_universe_d2_061_vtr_basefill_066, 61)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_061_vtr_basefill_066'] = {'inputs': ['vtr_base_universe_d2_061_vtr_basefill_066'], 'func': vtr_base_universe_d3_061_vtr_basefill_066}


def vtr_base_universe_d3_062_vtr_basefill_067(vtr_base_universe_d2_062_vtr_basefill_067):
    return _base_universe_d3(vtr_base_universe_d2_062_vtr_basefill_067, 62)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_062_vtr_basefill_067'] = {'inputs': ['vtr_base_universe_d2_062_vtr_basefill_067'], 'func': vtr_base_universe_d3_062_vtr_basefill_067}


def vtr_base_universe_d3_063_vtr_basefill_068(vtr_base_universe_d2_063_vtr_basefill_068):
    return _base_universe_d3(vtr_base_universe_d2_063_vtr_basefill_068, 63)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_063_vtr_basefill_068'] = {'inputs': ['vtr_base_universe_d2_063_vtr_basefill_068'], 'func': vtr_base_universe_d3_063_vtr_basefill_068}


def vtr_base_universe_d3_064_vtr_basefill_069(vtr_base_universe_d2_064_vtr_basefill_069):
    return _base_universe_d3(vtr_base_universe_d2_064_vtr_basefill_069, 64)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_064_vtr_basefill_069'] = {'inputs': ['vtr_base_universe_d2_064_vtr_basefill_069'], 'func': vtr_base_universe_d3_064_vtr_basefill_069}


def vtr_base_universe_d3_065_vtr_basefill_070(vtr_base_universe_d2_065_vtr_basefill_070):
    return _base_universe_d3(vtr_base_universe_d2_065_vtr_basefill_070, 65)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_065_vtr_basefill_070'] = {'inputs': ['vtr_base_universe_d2_065_vtr_basefill_070'], 'func': vtr_base_universe_d3_065_vtr_basefill_070}


def vtr_base_universe_d3_066_vtr_basefill_071(vtr_base_universe_d2_066_vtr_basefill_071):
    return _base_universe_d3(vtr_base_universe_d2_066_vtr_basefill_071, 66)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_066_vtr_basefill_071'] = {'inputs': ['vtr_base_universe_d2_066_vtr_basefill_071'], 'func': vtr_base_universe_d3_066_vtr_basefill_071}


def vtr_base_universe_d3_067_vtr_basefill_072(vtr_base_universe_d2_067_vtr_basefill_072):
    return _base_universe_d3(vtr_base_universe_d2_067_vtr_basefill_072, 67)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_067_vtr_basefill_072'] = {'inputs': ['vtr_base_universe_d2_067_vtr_basefill_072'], 'func': vtr_base_universe_d3_067_vtr_basefill_072}


def vtr_base_universe_d3_068_vtr_basefill_073(vtr_base_universe_d2_068_vtr_basefill_073):
    return _base_universe_d3(vtr_base_universe_d2_068_vtr_basefill_073, 68)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_068_vtr_basefill_073'] = {'inputs': ['vtr_base_universe_d2_068_vtr_basefill_073'], 'func': vtr_base_universe_d3_068_vtr_basefill_073}


def vtr_base_universe_d3_069_vtr_basefill_074(vtr_base_universe_d2_069_vtr_basefill_074):
    return _base_universe_d3(vtr_base_universe_d2_069_vtr_basefill_074, 69)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_069_vtr_basefill_074'] = {'inputs': ['vtr_base_universe_d2_069_vtr_basefill_074'], 'func': vtr_base_universe_d3_069_vtr_basefill_074}


def vtr_base_universe_d3_070_vtr_basefill_075(vtr_base_universe_d2_070_vtr_basefill_075):
    return _base_universe_d3(vtr_base_universe_d2_070_vtr_basefill_075, 70)
VTR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vtr_base_universe_d3_070_vtr_basefill_075'] = {'inputs': ['vtr_base_universe_d2_070_vtr_basefill_075'], 'func': vtr_base_universe_d3_070_vtr_basefill_075}
