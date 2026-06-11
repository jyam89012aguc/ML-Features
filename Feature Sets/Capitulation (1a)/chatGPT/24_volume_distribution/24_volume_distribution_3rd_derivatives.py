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



def vds_176_vds_001_volume_spike_ratio_5_001_accel_1(vds_151_vds_001_volume_spike_ratio_5_001_roc_1):
    feature = _s(vds_151_vds_001_volume_spike_ratio_5_001_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def vds_177_vds_007_volume_spike_ratio_126_007_accel_5(vds_152_vds_007_volume_spike_ratio_126_007_roc_5):
    feature = _s(vds_152_vds_007_volume_spike_ratio_126_007_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def vds_178_vds_013_volume_spike_ratio_1008_013_accel_42(vds_153_vds_013_volume_spike_ratio_1008_013_roc_42):
    feature = _s(vds_153_vds_013_volume_spike_ratio_1008_013_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def vds_179_vds_019_volume_spike_ratio_42_019_accel_126(vds_154_vds_019_volume_spike_ratio_42_019_roc_126):
    feature = _s(vds_154_vds_019_volume_spike_ratio_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def vds_180_vds_025_volume_spike_ratio_378_025_accel_378(vds_155_vds_025_volume_spike_ratio_378_025_roc_378):
    feature = _s(vds_155_vds_025_volume_spike_ratio_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















VOLUME_DISTRIBUTION_REGISTRY_3RD_DERIVATIVES = {
    'vds_176_vds_001_volume_spike_ratio_5_001_accel_1': {'inputs': ['vds_151_vds_001_volume_spike_ratio_5_001_roc_1'], 'func': vds_176_vds_001_volume_spike_ratio_5_001_accel_1},
    'vds_177_vds_007_volume_spike_ratio_126_007_accel_5': {'inputs': ['vds_152_vds_007_volume_spike_ratio_126_007_roc_5'], 'func': vds_177_vds_007_volume_spike_ratio_126_007_accel_5},
    'vds_178_vds_013_volume_spike_ratio_1008_013_accel_42': {'inputs': ['vds_153_vds_013_volume_spike_ratio_1008_013_roc_42'], 'func': vds_178_vds_013_volume_spike_ratio_1008_013_accel_42},
    'vds_179_vds_019_volume_spike_ratio_42_019_accel_126': {'inputs': ['vds_154_vds_019_volume_spike_ratio_42_019_roc_126'], 'func': vds_179_vds_019_volume_spike_ratio_42_019_accel_126},
    'vds_180_vds_025_volume_spike_ratio_378_025_accel_378': {'inputs': ['vds_155_vds_025_volume_spike_ratio_378_025_roc_378'], 'func': vds_180_vds_025_volume_spike_ratio_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def vd_replacement_d3_001(vd_replacement_d2_001):
    feature = _clean(vd_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_001'] = {'inputs': ['vd_replacement_d2_001'], 'func': vd_replacement_d3_001}


def vd_replacement_d3_002(vd_replacement_d2_002):
    feature = _clean(vd_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_002'] = {'inputs': ['vd_replacement_d2_002'], 'func': vd_replacement_d3_002}


def vd_replacement_d3_003(vd_replacement_d2_003):
    feature = _clean(vd_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_003'] = {'inputs': ['vd_replacement_d2_003'], 'func': vd_replacement_d3_003}


def vd_replacement_d3_004(vd_replacement_d2_004):
    feature = _clean(vd_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_004'] = {'inputs': ['vd_replacement_d2_004'], 'func': vd_replacement_d3_004}


def vd_replacement_d3_005(vd_replacement_d2_005):
    feature = _clean(vd_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_005'] = {'inputs': ['vd_replacement_d2_005'], 'func': vd_replacement_d3_005}


def vd_replacement_d3_006(vd_replacement_d2_006):
    feature = _clean(vd_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_006'] = {'inputs': ['vd_replacement_d2_006'], 'func': vd_replacement_d3_006}


def vd_replacement_d3_007(vd_replacement_d2_007):
    feature = _clean(vd_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_007'] = {'inputs': ['vd_replacement_d2_007'], 'func': vd_replacement_d3_007}


def vd_replacement_d3_008(vd_replacement_d2_008):
    feature = _clean(vd_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_008'] = {'inputs': ['vd_replacement_d2_008'], 'func': vd_replacement_d3_008}


def vd_replacement_d3_009(vd_replacement_d2_009):
    feature = _clean(vd_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_009'] = {'inputs': ['vd_replacement_d2_009'], 'func': vd_replacement_d3_009}


def vd_replacement_d3_010(vd_replacement_d2_010):
    feature = _clean(vd_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_010'] = {'inputs': ['vd_replacement_d2_010'], 'func': vd_replacement_d3_010}


def vd_replacement_d3_011(vd_replacement_d2_011):
    feature = _clean(vd_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_011'] = {'inputs': ['vd_replacement_d2_011'], 'func': vd_replacement_d3_011}


def vd_replacement_d3_012(vd_replacement_d2_012):
    feature = _clean(vd_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_012'] = {'inputs': ['vd_replacement_d2_012'], 'func': vd_replacement_d3_012}


def vd_replacement_d3_013(vd_replacement_d2_013):
    feature = _clean(vd_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_013'] = {'inputs': ['vd_replacement_d2_013'], 'func': vd_replacement_d3_013}


def vd_replacement_d3_014(vd_replacement_d2_014):
    feature = _clean(vd_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_014'] = {'inputs': ['vd_replacement_d2_014'], 'func': vd_replacement_d3_014}


def vd_replacement_d3_015(vd_replacement_d2_015):
    feature = _clean(vd_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_015'] = {'inputs': ['vd_replacement_d2_015'], 'func': vd_replacement_d3_015}


def vd_replacement_d3_016(vd_replacement_d2_016):
    feature = _clean(vd_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_016'] = {'inputs': ['vd_replacement_d2_016'], 'func': vd_replacement_d3_016}


def vd_replacement_d3_017(vd_replacement_d2_017):
    feature = _clean(vd_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_017'] = {'inputs': ['vd_replacement_d2_017'], 'func': vd_replacement_d3_017}


def vd_replacement_d3_018(vd_replacement_d2_018):
    feature = _clean(vd_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_018'] = {'inputs': ['vd_replacement_d2_018'], 'func': vd_replacement_d3_018}


def vd_replacement_d3_019(vd_replacement_d2_019):
    feature = _clean(vd_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_019'] = {'inputs': ['vd_replacement_d2_019'], 'func': vd_replacement_d3_019}


def vd_replacement_d3_020(vd_replacement_d2_020):
    feature = _clean(vd_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_020'] = {'inputs': ['vd_replacement_d2_020'], 'func': vd_replacement_d3_020}


def vd_replacement_d3_021(vd_replacement_d2_021):
    feature = _clean(vd_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_021'] = {'inputs': ['vd_replacement_d2_021'], 'func': vd_replacement_d3_021}


def vd_replacement_d3_022(vd_replacement_d2_022):
    feature = _clean(vd_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_022'] = {'inputs': ['vd_replacement_d2_022'], 'func': vd_replacement_d3_022}


def vd_replacement_d3_023(vd_replacement_d2_023):
    feature = _clean(vd_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_023'] = {'inputs': ['vd_replacement_d2_023'], 'func': vd_replacement_d3_023}


def vd_replacement_d3_024(vd_replacement_d2_024):
    feature = _clean(vd_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_024'] = {'inputs': ['vd_replacement_d2_024'], 'func': vd_replacement_d3_024}


def vd_replacement_d3_025(vd_replacement_d2_025):
    feature = _clean(vd_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_025'] = {'inputs': ['vd_replacement_d2_025'], 'func': vd_replacement_d3_025}


def vd_replacement_d3_026(vd_replacement_d2_026):
    feature = _clean(vd_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_026'] = {'inputs': ['vd_replacement_d2_026'], 'func': vd_replacement_d3_026}


def vd_replacement_d3_027(vd_replacement_d2_027):
    feature = _clean(vd_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_027'] = {'inputs': ['vd_replacement_d2_027'], 'func': vd_replacement_d3_027}


def vd_replacement_d3_028(vd_replacement_d2_028):
    feature = _clean(vd_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_028'] = {'inputs': ['vd_replacement_d2_028'], 'func': vd_replacement_d3_028}


def vd_replacement_d3_029(vd_replacement_d2_029):
    feature = _clean(vd_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_029'] = {'inputs': ['vd_replacement_d2_029'], 'func': vd_replacement_d3_029}


def vd_replacement_d3_030(vd_replacement_d2_030):
    feature = _clean(vd_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_030'] = {'inputs': ['vd_replacement_d2_030'], 'func': vd_replacement_d3_030}


def vd_replacement_d3_031(vd_replacement_d2_031):
    feature = _clean(vd_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_031'] = {'inputs': ['vd_replacement_d2_031'], 'func': vd_replacement_d3_031}


def vd_replacement_d3_032(vd_replacement_d2_032):
    feature = _clean(vd_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_032'] = {'inputs': ['vd_replacement_d2_032'], 'func': vd_replacement_d3_032}


def vd_replacement_d3_033(vd_replacement_d2_033):
    feature = _clean(vd_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_033'] = {'inputs': ['vd_replacement_d2_033'], 'func': vd_replacement_d3_033}


def vd_replacement_d3_034(vd_replacement_d2_034):
    feature = _clean(vd_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_034'] = {'inputs': ['vd_replacement_d2_034'], 'func': vd_replacement_d3_034}


def vd_replacement_d3_035(vd_replacement_d2_035):
    feature = _clean(vd_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_035'] = {'inputs': ['vd_replacement_d2_035'], 'func': vd_replacement_d3_035}


def vd_replacement_d3_036(vd_replacement_d2_036):
    feature = _clean(vd_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_036'] = {'inputs': ['vd_replacement_d2_036'], 'func': vd_replacement_d3_036}


def vd_replacement_d3_037(vd_replacement_d2_037):
    feature = _clean(vd_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_037'] = {'inputs': ['vd_replacement_d2_037'], 'func': vd_replacement_d3_037}


def vd_replacement_d3_038(vd_replacement_d2_038):
    feature = _clean(vd_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_038'] = {'inputs': ['vd_replacement_d2_038'], 'func': vd_replacement_d3_038}


def vd_replacement_d3_039(vd_replacement_d2_039):
    feature = _clean(vd_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_039'] = {'inputs': ['vd_replacement_d2_039'], 'func': vd_replacement_d3_039}


def vd_replacement_d3_040(vd_replacement_d2_040):
    feature = _clean(vd_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_040'] = {'inputs': ['vd_replacement_d2_040'], 'func': vd_replacement_d3_040}


def vd_replacement_d3_041(vd_replacement_d2_041):
    feature = _clean(vd_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_041'] = {'inputs': ['vd_replacement_d2_041'], 'func': vd_replacement_d3_041}


def vd_replacement_d3_042(vd_replacement_d2_042):
    feature = _clean(vd_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_042'] = {'inputs': ['vd_replacement_d2_042'], 'func': vd_replacement_d3_042}


def vd_replacement_d3_043(vd_replacement_d2_043):
    feature = _clean(vd_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_043'] = {'inputs': ['vd_replacement_d2_043'], 'func': vd_replacement_d3_043}


def vd_replacement_d3_044(vd_replacement_d2_044):
    feature = _clean(vd_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_044'] = {'inputs': ['vd_replacement_d2_044'], 'func': vd_replacement_d3_044}


def vd_replacement_d3_045(vd_replacement_d2_045):
    feature = _clean(vd_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_045'] = {'inputs': ['vd_replacement_d2_045'], 'func': vd_replacement_d3_045}


def vd_replacement_d3_046(vd_replacement_d2_046):
    feature = _clean(vd_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_046'] = {'inputs': ['vd_replacement_d2_046'], 'func': vd_replacement_d3_046}


def vd_replacement_d3_047(vd_replacement_d2_047):
    feature = _clean(vd_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_047'] = {'inputs': ['vd_replacement_d2_047'], 'func': vd_replacement_d3_047}


def vd_replacement_d3_048(vd_replacement_d2_048):
    feature = _clean(vd_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_048'] = {'inputs': ['vd_replacement_d2_048'], 'func': vd_replacement_d3_048}


def vd_replacement_d3_049(vd_replacement_d2_049):
    feature = _clean(vd_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_049'] = {'inputs': ['vd_replacement_d2_049'], 'func': vd_replacement_d3_049}


def vd_replacement_d3_050(vd_replacement_d2_050):
    feature = _clean(vd_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_050'] = {'inputs': ['vd_replacement_d2_050'], 'func': vd_replacement_d3_050}


def vd_replacement_d3_051(vd_replacement_d2_051):
    feature = _clean(vd_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_051'] = {'inputs': ['vd_replacement_d2_051'], 'func': vd_replacement_d3_051}


def vd_replacement_d3_052(vd_replacement_d2_052):
    feature = _clean(vd_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_052'] = {'inputs': ['vd_replacement_d2_052'], 'func': vd_replacement_d3_052}


def vd_replacement_d3_053(vd_replacement_d2_053):
    feature = _clean(vd_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_053'] = {'inputs': ['vd_replacement_d2_053'], 'func': vd_replacement_d3_053}


def vd_replacement_d3_054(vd_replacement_d2_054):
    feature = _clean(vd_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_054'] = {'inputs': ['vd_replacement_d2_054'], 'func': vd_replacement_d3_054}


def vd_replacement_d3_055(vd_replacement_d2_055):
    feature = _clean(vd_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_055'] = {'inputs': ['vd_replacement_d2_055'], 'func': vd_replacement_d3_055}


def vd_replacement_d3_056(vd_replacement_d2_056):
    feature = _clean(vd_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_056'] = {'inputs': ['vd_replacement_d2_056'], 'func': vd_replacement_d3_056}


def vd_replacement_d3_057(vd_replacement_d2_057):
    feature = _clean(vd_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_057'] = {'inputs': ['vd_replacement_d2_057'], 'func': vd_replacement_d3_057}


def vd_replacement_d3_058(vd_replacement_d2_058):
    feature = _clean(vd_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_058'] = {'inputs': ['vd_replacement_d2_058'], 'func': vd_replacement_d3_058}


def vd_replacement_d3_059(vd_replacement_d2_059):
    feature = _clean(vd_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_059'] = {'inputs': ['vd_replacement_d2_059'], 'func': vd_replacement_d3_059}


def vd_replacement_d3_060(vd_replacement_d2_060):
    feature = _clean(vd_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_060'] = {'inputs': ['vd_replacement_d2_060'], 'func': vd_replacement_d3_060}


def vd_replacement_d3_061(vd_replacement_d2_061):
    feature = _clean(vd_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_061'] = {'inputs': ['vd_replacement_d2_061'], 'func': vd_replacement_d3_061}


def vd_replacement_d3_062(vd_replacement_d2_062):
    feature = _clean(vd_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_062'] = {'inputs': ['vd_replacement_d2_062'], 'func': vd_replacement_d3_062}


def vd_replacement_d3_063(vd_replacement_d2_063):
    feature = _clean(vd_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_063'] = {'inputs': ['vd_replacement_d2_063'], 'func': vd_replacement_d3_063}


def vd_replacement_d3_064(vd_replacement_d2_064):
    feature = _clean(vd_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_064'] = {'inputs': ['vd_replacement_d2_064'], 'func': vd_replacement_d3_064}


def vd_replacement_d3_065(vd_replacement_d2_065):
    feature = _clean(vd_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_065'] = {'inputs': ['vd_replacement_d2_065'], 'func': vd_replacement_d3_065}


def vd_replacement_d3_066(vd_replacement_d2_066):
    feature = _clean(vd_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_066'] = {'inputs': ['vd_replacement_d2_066'], 'func': vd_replacement_d3_066}


def vd_replacement_d3_067(vd_replacement_d2_067):
    feature = _clean(vd_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_067'] = {'inputs': ['vd_replacement_d2_067'], 'func': vd_replacement_d3_067}


def vd_replacement_d3_068(vd_replacement_d2_068):
    feature = _clean(vd_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_068'] = {'inputs': ['vd_replacement_d2_068'], 'func': vd_replacement_d3_068}


def vd_replacement_d3_069(vd_replacement_d2_069):
    feature = _clean(vd_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_069'] = {'inputs': ['vd_replacement_d2_069'], 'func': vd_replacement_d3_069}


def vd_replacement_d3_070(vd_replacement_d2_070):
    feature = _clean(vd_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_070'] = {'inputs': ['vd_replacement_d2_070'], 'func': vd_replacement_d3_070}


def vd_replacement_d3_071(vd_replacement_d2_071):
    feature = _clean(vd_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_071'] = {'inputs': ['vd_replacement_d2_071'], 'func': vd_replacement_d3_071}


def vd_replacement_d3_072(vd_replacement_d2_072):
    feature = _clean(vd_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_072'] = {'inputs': ['vd_replacement_d2_072'], 'func': vd_replacement_d3_072}


def vd_replacement_d3_073(vd_replacement_d2_073):
    feature = _clean(vd_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_073'] = {'inputs': ['vd_replacement_d2_073'], 'func': vd_replacement_d3_073}


def vd_replacement_d3_074(vd_replacement_d2_074):
    feature = _clean(vd_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_074'] = {'inputs': ['vd_replacement_d2_074'], 'func': vd_replacement_d3_074}


def vd_replacement_d3_075(vd_replacement_d2_075):
    feature = _clean(vd_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_075'] = {'inputs': ['vd_replacement_d2_075'], 'func': vd_replacement_d3_075}


def vd_replacement_d3_076(vd_replacement_d2_076):
    feature = _clean(vd_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_076'] = {'inputs': ['vd_replacement_d2_076'], 'func': vd_replacement_d3_076}


def vd_replacement_d3_077(vd_replacement_d2_077):
    feature = _clean(vd_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_077'] = {'inputs': ['vd_replacement_d2_077'], 'func': vd_replacement_d3_077}


def vd_replacement_d3_078(vd_replacement_d2_078):
    feature = _clean(vd_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_078'] = {'inputs': ['vd_replacement_d2_078'], 'func': vd_replacement_d3_078}


def vd_replacement_d3_079(vd_replacement_d2_079):
    feature = _clean(vd_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_079'] = {'inputs': ['vd_replacement_d2_079'], 'func': vd_replacement_d3_079}


def vd_replacement_d3_080(vd_replacement_d2_080):
    feature = _clean(vd_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_080'] = {'inputs': ['vd_replacement_d2_080'], 'func': vd_replacement_d3_080}


def vd_replacement_d3_081(vd_replacement_d2_081):
    feature = _clean(vd_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_081'] = {'inputs': ['vd_replacement_d2_081'], 'func': vd_replacement_d3_081}


def vd_replacement_d3_082(vd_replacement_d2_082):
    feature = _clean(vd_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_082'] = {'inputs': ['vd_replacement_d2_082'], 'func': vd_replacement_d3_082}


def vd_replacement_d3_083(vd_replacement_d2_083):
    feature = _clean(vd_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_083'] = {'inputs': ['vd_replacement_d2_083'], 'func': vd_replacement_d3_083}


def vd_replacement_d3_084(vd_replacement_d2_084):
    feature = _clean(vd_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_084'] = {'inputs': ['vd_replacement_d2_084'], 'func': vd_replacement_d3_084}


def vd_replacement_d3_085(vd_replacement_d2_085):
    feature = _clean(vd_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_085'] = {'inputs': ['vd_replacement_d2_085'], 'func': vd_replacement_d3_085}


def vd_replacement_d3_086(vd_replacement_d2_086):
    feature = _clean(vd_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_086'] = {'inputs': ['vd_replacement_d2_086'], 'func': vd_replacement_d3_086}


def vd_replacement_d3_087(vd_replacement_d2_087):
    feature = _clean(vd_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_087'] = {'inputs': ['vd_replacement_d2_087'], 'func': vd_replacement_d3_087}


def vd_replacement_d3_088(vd_replacement_d2_088):
    feature = _clean(vd_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_088'] = {'inputs': ['vd_replacement_d2_088'], 'func': vd_replacement_d3_088}


def vd_replacement_d3_089(vd_replacement_d2_089):
    feature = _clean(vd_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_089'] = {'inputs': ['vd_replacement_d2_089'], 'func': vd_replacement_d3_089}


def vd_replacement_d3_090(vd_replacement_d2_090):
    feature = _clean(vd_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_090'] = {'inputs': ['vd_replacement_d2_090'], 'func': vd_replacement_d3_090}


def vd_replacement_d3_091(vd_replacement_d2_091):
    feature = _clean(vd_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_091'] = {'inputs': ['vd_replacement_d2_091'], 'func': vd_replacement_d3_091}


def vd_replacement_d3_092(vd_replacement_d2_092):
    feature = _clean(vd_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_092'] = {'inputs': ['vd_replacement_d2_092'], 'func': vd_replacement_d3_092}


def vd_replacement_d3_093(vd_replacement_d2_093):
    feature = _clean(vd_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_093'] = {'inputs': ['vd_replacement_d2_093'], 'func': vd_replacement_d3_093}


def vd_replacement_d3_094(vd_replacement_d2_094):
    feature = _clean(vd_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_094'] = {'inputs': ['vd_replacement_d2_094'], 'func': vd_replacement_d3_094}


def vd_replacement_d3_095(vd_replacement_d2_095):
    feature = _clean(vd_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_095'] = {'inputs': ['vd_replacement_d2_095'], 'func': vd_replacement_d3_095}


def vd_replacement_d3_096(vd_replacement_d2_096):
    feature = _clean(vd_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_096'] = {'inputs': ['vd_replacement_d2_096'], 'func': vd_replacement_d3_096}


def vd_replacement_d3_097(vd_replacement_d2_097):
    feature = _clean(vd_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_097'] = {'inputs': ['vd_replacement_d2_097'], 'func': vd_replacement_d3_097}


def vd_replacement_d3_098(vd_replacement_d2_098):
    feature = _clean(vd_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_098'] = {'inputs': ['vd_replacement_d2_098'], 'func': vd_replacement_d3_098}


def vd_replacement_d3_099(vd_replacement_d2_099):
    feature = _clean(vd_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_099'] = {'inputs': ['vd_replacement_d2_099'], 'func': vd_replacement_d3_099}


def vd_replacement_d3_100(vd_replacement_d2_100):
    feature = _clean(vd_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_100'] = {'inputs': ['vd_replacement_d2_100'], 'func': vd_replacement_d3_100}


def vd_replacement_d3_101(vd_replacement_d2_101):
    feature = _clean(vd_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_101'] = {'inputs': ['vd_replacement_d2_101'], 'func': vd_replacement_d3_101}


def vd_replacement_d3_102(vd_replacement_d2_102):
    feature = _clean(vd_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_102'] = {'inputs': ['vd_replacement_d2_102'], 'func': vd_replacement_d3_102}


def vd_replacement_d3_103(vd_replacement_d2_103):
    feature = _clean(vd_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_103'] = {'inputs': ['vd_replacement_d2_103'], 'func': vd_replacement_d3_103}


def vd_replacement_d3_104(vd_replacement_d2_104):
    feature = _clean(vd_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_104'] = {'inputs': ['vd_replacement_d2_104'], 'func': vd_replacement_d3_104}


def vd_replacement_d3_105(vd_replacement_d2_105):
    feature = _clean(vd_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_105'] = {'inputs': ['vd_replacement_d2_105'], 'func': vd_replacement_d3_105}


def vd_replacement_d3_106(vd_replacement_d2_106):
    feature = _clean(vd_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_106'] = {'inputs': ['vd_replacement_d2_106'], 'func': vd_replacement_d3_106}


def vd_replacement_d3_107(vd_replacement_d2_107):
    feature = _clean(vd_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_107'] = {'inputs': ['vd_replacement_d2_107'], 'func': vd_replacement_d3_107}


def vd_replacement_d3_108(vd_replacement_d2_108):
    feature = _clean(vd_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_108'] = {'inputs': ['vd_replacement_d2_108'], 'func': vd_replacement_d3_108}


def vd_replacement_d3_109(vd_replacement_d2_109):
    feature = _clean(vd_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_109'] = {'inputs': ['vd_replacement_d2_109'], 'func': vd_replacement_d3_109}


def vd_replacement_d3_110(vd_replacement_d2_110):
    feature = _clean(vd_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_110'] = {'inputs': ['vd_replacement_d2_110'], 'func': vd_replacement_d3_110}


def vd_replacement_d3_111(vd_replacement_d2_111):
    feature = _clean(vd_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_111'] = {'inputs': ['vd_replacement_d2_111'], 'func': vd_replacement_d3_111}


def vd_replacement_d3_112(vd_replacement_d2_112):
    feature = _clean(vd_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_112'] = {'inputs': ['vd_replacement_d2_112'], 'func': vd_replacement_d3_112}


def vd_replacement_d3_113(vd_replacement_d2_113):
    feature = _clean(vd_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_113'] = {'inputs': ['vd_replacement_d2_113'], 'func': vd_replacement_d3_113}


def vd_replacement_d3_114(vd_replacement_d2_114):
    feature = _clean(vd_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_114'] = {'inputs': ['vd_replacement_d2_114'], 'func': vd_replacement_d3_114}


def vd_replacement_d3_115(vd_replacement_d2_115):
    feature = _clean(vd_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_115'] = {'inputs': ['vd_replacement_d2_115'], 'func': vd_replacement_d3_115}


def vd_replacement_d3_116(vd_replacement_d2_116):
    feature = _clean(vd_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_116'] = {'inputs': ['vd_replacement_d2_116'], 'func': vd_replacement_d3_116}


def vd_replacement_d3_117(vd_replacement_d2_117):
    feature = _clean(vd_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_117'] = {'inputs': ['vd_replacement_d2_117'], 'func': vd_replacement_d3_117}


def vd_replacement_d3_118(vd_replacement_d2_118):
    feature = _clean(vd_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_118'] = {'inputs': ['vd_replacement_d2_118'], 'func': vd_replacement_d3_118}


def vd_replacement_d3_119(vd_replacement_d2_119):
    feature = _clean(vd_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_119'] = {'inputs': ['vd_replacement_d2_119'], 'func': vd_replacement_d3_119}


def vd_replacement_d3_120(vd_replacement_d2_120):
    feature = _clean(vd_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_120'] = {'inputs': ['vd_replacement_d2_120'], 'func': vd_replacement_d3_120}


def vd_replacement_d3_121(vd_replacement_d2_121):
    feature = _clean(vd_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_121'] = {'inputs': ['vd_replacement_d2_121'], 'func': vd_replacement_d3_121}


def vd_replacement_d3_122(vd_replacement_d2_122):
    feature = _clean(vd_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_122'] = {'inputs': ['vd_replacement_d2_122'], 'func': vd_replacement_d3_122}


def vd_replacement_d3_123(vd_replacement_d2_123):
    feature = _clean(vd_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_123'] = {'inputs': ['vd_replacement_d2_123'], 'func': vd_replacement_d3_123}


def vd_replacement_d3_124(vd_replacement_d2_124):
    feature = _clean(vd_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_124'] = {'inputs': ['vd_replacement_d2_124'], 'func': vd_replacement_d3_124}


def vd_replacement_d3_125(vd_replacement_d2_125):
    feature = _clean(vd_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_125'] = {'inputs': ['vd_replacement_d2_125'], 'func': vd_replacement_d3_125}


def vd_replacement_d3_126(vd_replacement_d2_126):
    feature = _clean(vd_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_126'] = {'inputs': ['vd_replacement_d2_126'], 'func': vd_replacement_d3_126}


def vd_replacement_d3_127(vd_replacement_d2_127):
    feature = _clean(vd_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_127'] = {'inputs': ['vd_replacement_d2_127'], 'func': vd_replacement_d3_127}


def vd_replacement_d3_128(vd_replacement_d2_128):
    feature = _clean(vd_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_128'] = {'inputs': ['vd_replacement_d2_128'], 'func': vd_replacement_d3_128}


def vd_replacement_d3_129(vd_replacement_d2_129):
    feature = _clean(vd_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_129'] = {'inputs': ['vd_replacement_d2_129'], 'func': vd_replacement_d3_129}


def vd_replacement_d3_130(vd_replacement_d2_130):
    feature = _clean(vd_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_130'] = {'inputs': ['vd_replacement_d2_130'], 'func': vd_replacement_d3_130}


def vd_replacement_d3_131(vd_replacement_d2_131):
    feature = _clean(vd_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_131'] = {'inputs': ['vd_replacement_d2_131'], 'func': vd_replacement_d3_131}


def vd_replacement_d3_132(vd_replacement_d2_132):
    feature = _clean(vd_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_132'] = {'inputs': ['vd_replacement_d2_132'], 'func': vd_replacement_d3_132}


def vd_replacement_d3_133(vd_replacement_d2_133):
    feature = _clean(vd_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_133'] = {'inputs': ['vd_replacement_d2_133'], 'func': vd_replacement_d3_133}


def vd_replacement_d3_134(vd_replacement_d2_134):
    feature = _clean(vd_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_134'] = {'inputs': ['vd_replacement_d2_134'], 'func': vd_replacement_d3_134}


def vd_replacement_d3_135(vd_replacement_d2_135):
    feature = _clean(vd_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_135'] = {'inputs': ['vd_replacement_d2_135'], 'func': vd_replacement_d3_135}


def vd_replacement_d3_136(vd_replacement_d2_136):
    feature = _clean(vd_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_136'] = {'inputs': ['vd_replacement_d2_136'], 'func': vd_replacement_d3_136}


def vd_replacement_d3_137(vd_replacement_d2_137):
    feature = _clean(vd_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_137'] = {'inputs': ['vd_replacement_d2_137'], 'func': vd_replacement_d3_137}


def vd_replacement_d3_138(vd_replacement_d2_138):
    feature = _clean(vd_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_138'] = {'inputs': ['vd_replacement_d2_138'], 'func': vd_replacement_d3_138}


def vd_replacement_d3_139(vd_replacement_d2_139):
    feature = _clean(vd_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_139'] = {'inputs': ['vd_replacement_d2_139'], 'func': vd_replacement_d3_139}


def vd_replacement_d3_140(vd_replacement_d2_140):
    feature = _clean(vd_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_140'] = {'inputs': ['vd_replacement_d2_140'], 'func': vd_replacement_d3_140}


def vd_replacement_d3_141(vd_replacement_d2_141):
    feature = _clean(vd_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_141'] = {'inputs': ['vd_replacement_d2_141'], 'func': vd_replacement_d3_141}


def vd_replacement_d3_142(vd_replacement_d2_142):
    feature = _clean(vd_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_142'] = {'inputs': ['vd_replacement_d2_142'], 'func': vd_replacement_d3_142}


def vd_replacement_d3_143(vd_replacement_d2_143):
    feature = _clean(vd_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_143'] = {'inputs': ['vd_replacement_d2_143'], 'func': vd_replacement_d3_143}


def vd_replacement_d3_144(vd_replacement_d2_144):
    feature = _clean(vd_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_144'] = {'inputs': ['vd_replacement_d2_144'], 'func': vd_replacement_d3_144}


def vd_replacement_d3_145(vd_replacement_d2_145):
    feature = _clean(vd_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_145'] = {'inputs': ['vd_replacement_d2_145'], 'func': vd_replacement_d3_145}


def vd_replacement_d3_146(vd_replacement_d2_146):
    feature = _clean(vd_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_146'] = {'inputs': ['vd_replacement_d2_146'], 'func': vd_replacement_d3_146}


def vd_replacement_d3_147(vd_replacement_d2_147):
    feature = _clean(vd_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_147'] = {'inputs': ['vd_replacement_d2_147'], 'func': vd_replacement_d3_147}


def vd_replacement_d3_148(vd_replacement_d2_148):
    feature = _clean(vd_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_148'] = {'inputs': ['vd_replacement_d2_148'], 'func': vd_replacement_d3_148}


def vd_replacement_d3_149(vd_replacement_d2_149):
    feature = _clean(vd_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_149'] = {'inputs': ['vd_replacement_d2_149'], 'func': vd_replacement_d3_149}


def vd_replacement_d3_150(vd_replacement_d2_150):
    feature = _clean(vd_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_150'] = {'inputs': ['vd_replacement_d2_150'], 'func': vd_replacement_d3_150}


def vd_replacement_d3_151(vd_replacement_d2_151):
    feature = _clean(vd_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_151'] = {'inputs': ['vd_replacement_d2_151'], 'func': vd_replacement_d3_151}


def vd_replacement_d3_152(vd_replacement_d2_152):
    feature = _clean(vd_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_152'] = {'inputs': ['vd_replacement_d2_152'], 'func': vd_replacement_d3_152}


def vd_replacement_d3_153(vd_replacement_d2_153):
    feature = _clean(vd_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_153'] = {'inputs': ['vd_replacement_d2_153'], 'func': vd_replacement_d3_153}


def vd_replacement_d3_154(vd_replacement_d2_154):
    feature = _clean(vd_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_154'] = {'inputs': ['vd_replacement_d2_154'], 'func': vd_replacement_d3_154}


def vd_replacement_d3_155(vd_replacement_d2_155):
    feature = _clean(vd_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_155'] = {'inputs': ['vd_replacement_d2_155'], 'func': vd_replacement_d3_155}


def vd_replacement_d3_156(vd_replacement_d2_156):
    feature = _clean(vd_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_156'] = {'inputs': ['vd_replacement_d2_156'], 'func': vd_replacement_d3_156}


def vd_replacement_d3_157(vd_replacement_d2_157):
    feature = _clean(vd_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_157'] = {'inputs': ['vd_replacement_d2_157'], 'func': vd_replacement_d3_157}


def vd_replacement_d3_158(vd_replacement_d2_158):
    feature = _clean(vd_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_158'] = {'inputs': ['vd_replacement_d2_158'], 'func': vd_replacement_d3_158}


def vd_replacement_d3_159(vd_replacement_d2_159):
    feature = _clean(vd_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_159'] = {'inputs': ['vd_replacement_d2_159'], 'func': vd_replacement_d3_159}


def vd_replacement_d3_160(vd_replacement_d2_160):
    feature = _clean(vd_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
VD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vd_replacement_d3_160'] = {'inputs': ['vd_replacement_d2_160'], 'func': vd_replacement_d3_160}


# Third-derivative extensions for repaired first-base features.
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def vds_base_universe_d3_001_vds_002_volume_zscore_10_002(vds_base_universe_d2_001_vds_002_volume_zscore_10_002):
    return _base_universe_d3(vds_base_universe_d2_001_vds_002_volume_zscore_10_002, 1)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_001_vds_002_volume_zscore_10_002'] = {'inputs': ['vds_base_universe_d2_001_vds_002_volume_zscore_10_002'], 'func': vds_base_universe_d3_001_vds_002_volume_zscore_10_002}


def vds_base_universe_d3_002_vds_003_down_volume_share_21_003(vds_base_universe_d2_002_vds_003_down_volume_share_21_003):
    return _base_universe_d3(vds_base_universe_d2_002_vds_003_down_volume_share_21_003, 2)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_002_vds_003_down_volume_share_21_003'] = {'inputs': ['vds_base_universe_d2_002_vds_003_down_volume_share_21_003'], 'func': vds_base_universe_d3_002_vds_003_down_volume_share_21_003}


def vds_base_universe_d3_003_vds_004_dollar_volume_shock_42_004(vds_base_universe_d2_003_vds_004_dollar_volume_shock_42_004):
    return _base_universe_d3(vds_base_universe_d2_003_vds_004_dollar_volume_shock_42_004, 3)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_003_vds_004_dollar_volume_shock_42_004'] = {'inputs': ['vds_base_universe_d2_003_vds_004_dollar_volume_shock_42_004'], 'func': vds_base_universe_d3_003_vds_004_dollar_volume_shock_42_004}


def vds_base_universe_d3_004_vds_005_volume_trend_slope_63_005(vds_base_universe_d2_004_vds_005_volume_trend_slope_63_005):
    return _base_universe_d3(vds_base_universe_d2_004_vds_005_volume_trend_slope_63_005, 4)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_004_vds_005_volume_trend_slope_63_005'] = {'inputs': ['vds_base_universe_d2_004_vds_005_volume_trend_slope_63_005'], 'func': vds_base_universe_d3_004_vds_005_volume_trend_slope_63_005}


def vds_base_universe_d3_005_vds_006_price_volume_divergence_84_006(vds_base_universe_d2_005_vds_006_price_volume_divergence_84_006):
    return _base_universe_d3(vds_base_universe_d2_005_vds_006_price_volume_divergence_84_006, 5)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_005_vds_006_price_volume_divergence_84_006'] = {'inputs': ['vds_base_universe_d2_005_vds_006_price_volume_divergence_84_006'], 'func': vds_base_universe_d3_005_vds_006_price_volume_divergence_84_006}


def vds_base_universe_d3_006_vds_008_volume_zscore_189_008(vds_base_universe_d2_006_vds_008_volume_zscore_189_008):
    return _base_universe_d3(vds_base_universe_d2_006_vds_008_volume_zscore_189_008, 6)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_006_vds_008_volume_zscore_189_008'] = {'inputs': ['vds_base_universe_d2_006_vds_008_volume_zscore_189_008'], 'func': vds_base_universe_d3_006_vds_008_volume_zscore_189_008}


def vds_base_universe_d3_007_vds_009_down_volume_share_252_009(vds_base_universe_d2_007_vds_009_down_volume_share_252_009):
    return _base_universe_d3(vds_base_universe_d2_007_vds_009_down_volume_share_252_009, 7)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_007_vds_009_down_volume_share_252_009'] = {'inputs': ['vds_base_universe_d2_007_vds_009_down_volume_share_252_009'], 'func': vds_base_universe_d3_007_vds_009_down_volume_share_252_009}


def vds_base_universe_d3_008_vds_010_dollar_volume_shock_378_010(vds_base_universe_d2_008_vds_010_dollar_volume_shock_378_010):
    return _base_universe_d3(vds_base_universe_d2_008_vds_010_dollar_volume_shock_378_010, 8)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_008_vds_010_dollar_volume_shock_378_010'] = {'inputs': ['vds_base_universe_d2_008_vds_010_dollar_volume_shock_378_010'], 'func': vds_base_universe_d3_008_vds_010_dollar_volume_shock_378_010}


def vds_base_universe_d3_009_vds_011_volume_trend_slope_504_011(vds_base_universe_d2_009_vds_011_volume_trend_slope_504_011):
    return _base_universe_d3(vds_base_universe_d2_009_vds_011_volume_trend_slope_504_011, 9)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_009_vds_011_volume_trend_slope_504_011'] = {'inputs': ['vds_base_universe_d2_009_vds_011_volume_trend_slope_504_011'], 'func': vds_base_universe_d3_009_vds_011_volume_trend_slope_504_011}


def vds_base_universe_d3_010_vds_012_price_volume_divergence_756_012(vds_base_universe_d2_010_vds_012_price_volume_divergence_756_012):
    return _base_universe_d3(vds_base_universe_d2_010_vds_012_price_volume_divergence_756_012, 10)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_010_vds_012_price_volume_divergence_756_012'] = {'inputs': ['vds_base_universe_d2_010_vds_012_price_volume_divergence_756_012'], 'func': vds_base_universe_d3_010_vds_012_price_volume_divergence_756_012}


def vds_base_universe_d3_011_vds_014_volume_zscore_1260_014(vds_base_universe_d2_011_vds_014_volume_zscore_1260_014):
    return _base_universe_d3(vds_base_universe_d2_011_vds_014_volume_zscore_1260_014, 11)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_011_vds_014_volume_zscore_1260_014'] = {'inputs': ['vds_base_universe_d2_011_vds_014_volume_zscore_1260_014'], 'func': vds_base_universe_d3_011_vds_014_volume_zscore_1260_014}


def vds_base_universe_d3_012_vds_015_down_volume_share_1512_015(vds_base_universe_d2_012_vds_015_down_volume_share_1512_015):
    return _base_universe_d3(vds_base_universe_d2_012_vds_015_down_volume_share_1512_015, 12)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_012_vds_015_down_volume_share_1512_015'] = {'inputs': ['vds_base_universe_d2_012_vds_015_down_volume_share_1512_015'], 'func': vds_base_universe_d3_012_vds_015_down_volume_share_1512_015}


def vds_base_universe_d3_013_vds_016_dollar_volume_shock_5_016(vds_base_universe_d2_013_vds_016_dollar_volume_shock_5_016):
    return _base_universe_d3(vds_base_universe_d2_013_vds_016_dollar_volume_shock_5_016, 13)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_013_vds_016_dollar_volume_shock_5_016'] = {'inputs': ['vds_base_universe_d2_013_vds_016_dollar_volume_shock_5_016'], 'func': vds_base_universe_d3_013_vds_016_dollar_volume_shock_5_016}


def vds_base_universe_d3_014_vds_017_volume_trend_slope_10_017(vds_base_universe_d2_014_vds_017_volume_trend_slope_10_017):
    return _base_universe_d3(vds_base_universe_d2_014_vds_017_volume_trend_slope_10_017, 14)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_014_vds_017_volume_trend_slope_10_017'] = {'inputs': ['vds_base_universe_d2_014_vds_017_volume_trend_slope_10_017'], 'func': vds_base_universe_d3_014_vds_017_volume_trend_slope_10_017}


def vds_base_universe_d3_015_vds_018_price_volume_divergence_21_018(vds_base_universe_d2_015_vds_018_price_volume_divergence_21_018):
    return _base_universe_d3(vds_base_universe_d2_015_vds_018_price_volume_divergence_21_018, 15)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_015_vds_018_price_volume_divergence_21_018'] = {'inputs': ['vds_base_universe_d2_015_vds_018_price_volume_divergence_21_018'], 'func': vds_base_universe_d3_015_vds_018_price_volume_divergence_21_018}


def vds_base_universe_d3_016_vds_020_volume_zscore_63_020(vds_base_universe_d2_016_vds_020_volume_zscore_63_020):
    return _base_universe_d3(vds_base_universe_d2_016_vds_020_volume_zscore_63_020, 16)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_016_vds_020_volume_zscore_63_020'] = {'inputs': ['vds_base_universe_d2_016_vds_020_volume_zscore_63_020'], 'func': vds_base_universe_d3_016_vds_020_volume_zscore_63_020}


def vds_base_universe_d3_017_vds_021_down_volume_share_84_021(vds_base_universe_d2_017_vds_021_down_volume_share_84_021):
    return _base_universe_d3(vds_base_universe_d2_017_vds_021_down_volume_share_84_021, 17)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_017_vds_021_down_volume_share_84_021'] = {'inputs': ['vds_base_universe_d2_017_vds_021_down_volume_share_84_021'], 'func': vds_base_universe_d3_017_vds_021_down_volume_share_84_021}


def vds_base_universe_d3_018_vds_022_dollar_volume_shock_126_022(vds_base_universe_d2_018_vds_022_dollar_volume_shock_126_022):
    return _base_universe_d3(vds_base_universe_d2_018_vds_022_dollar_volume_shock_126_022, 18)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_018_vds_022_dollar_volume_shock_126_022'] = {'inputs': ['vds_base_universe_d2_018_vds_022_dollar_volume_shock_126_022'], 'func': vds_base_universe_d3_018_vds_022_dollar_volume_shock_126_022}


def vds_base_universe_d3_019_vds_023_volume_trend_slope_189_023(vds_base_universe_d2_019_vds_023_volume_trend_slope_189_023):
    return _base_universe_d3(vds_base_universe_d2_019_vds_023_volume_trend_slope_189_023, 19)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_019_vds_023_volume_trend_slope_189_023'] = {'inputs': ['vds_base_universe_d2_019_vds_023_volume_trend_slope_189_023'], 'func': vds_base_universe_d3_019_vds_023_volume_trend_slope_189_023}


def vds_base_universe_d3_020_vds_024_price_volume_divergence_252_024(vds_base_universe_d2_020_vds_024_price_volume_divergence_252_024):
    return _base_universe_d3(vds_base_universe_d2_020_vds_024_price_volume_divergence_252_024, 20)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_020_vds_024_price_volume_divergence_252_024'] = {'inputs': ['vds_base_universe_d2_020_vds_024_price_volume_divergence_252_024'], 'func': vds_base_universe_d3_020_vds_024_price_volume_divergence_252_024}


def vds_base_universe_d3_021_vds_026_volume_zscore_504_026(vds_base_universe_d2_021_vds_026_volume_zscore_504_026):
    return _base_universe_d3(vds_base_universe_d2_021_vds_026_volume_zscore_504_026, 21)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_021_vds_026_volume_zscore_504_026'] = {'inputs': ['vds_base_universe_d2_021_vds_026_volume_zscore_504_026'], 'func': vds_base_universe_d3_021_vds_026_volume_zscore_504_026}


def vds_base_universe_d3_022_vds_027_down_volume_share_756_027(vds_base_universe_d2_022_vds_027_down_volume_share_756_027):
    return _base_universe_d3(vds_base_universe_d2_022_vds_027_down_volume_share_756_027, 22)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_022_vds_027_down_volume_share_756_027'] = {'inputs': ['vds_base_universe_d2_022_vds_027_down_volume_share_756_027'], 'func': vds_base_universe_d3_022_vds_027_down_volume_share_756_027}


def vds_base_universe_d3_023_vds_028_dollar_volume_shock_1008_028(vds_base_universe_d2_023_vds_028_dollar_volume_shock_1008_028):
    return _base_universe_d3(vds_base_universe_d2_023_vds_028_dollar_volume_shock_1008_028, 23)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_023_vds_028_dollar_volume_shock_1008_028'] = {'inputs': ['vds_base_universe_d2_023_vds_028_dollar_volume_shock_1008_028'], 'func': vds_base_universe_d3_023_vds_028_dollar_volume_shock_1008_028}


def vds_base_universe_d3_024_vds_029_volume_trend_slope_1260_029(vds_base_universe_d2_024_vds_029_volume_trend_slope_1260_029):
    return _base_universe_d3(vds_base_universe_d2_024_vds_029_volume_trend_slope_1260_029, 24)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_024_vds_029_volume_trend_slope_1260_029'] = {'inputs': ['vds_base_universe_d2_024_vds_029_volume_trend_slope_1260_029'], 'func': vds_base_universe_d3_024_vds_029_volume_trend_slope_1260_029}


def vds_base_universe_d3_025_vds_030_price_volume_divergence_1512_030(vds_base_universe_d2_025_vds_030_price_volume_divergence_1512_030):
    return _base_universe_d3(vds_base_universe_d2_025_vds_030_price_volume_divergence_1512_030, 25)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_025_vds_030_price_volume_divergence_1512_030'] = {'inputs': ['vds_base_universe_d2_025_vds_030_price_volume_divergence_1512_030'], 'func': vds_base_universe_d3_025_vds_030_price_volume_divergence_1512_030}


def vds_base_universe_d3_026_vds_basefill_031(vds_base_universe_d2_026_vds_basefill_031):
    return _base_universe_d3(vds_base_universe_d2_026_vds_basefill_031, 26)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_026_vds_basefill_031'] = {'inputs': ['vds_base_universe_d2_026_vds_basefill_031'], 'func': vds_base_universe_d3_026_vds_basefill_031}


def vds_base_universe_d3_027_vds_basefill_032(vds_base_universe_d2_027_vds_basefill_032):
    return _base_universe_d3(vds_base_universe_d2_027_vds_basefill_032, 27)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_027_vds_basefill_032'] = {'inputs': ['vds_base_universe_d2_027_vds_basefill_032'], 'func': vds_base_universe_d3_027_vds_basefill_032}


def vds_base_universe_d3_028_vds_basefill_033(vds_base_universe_d2_028_vds_basefill_033):
    return _base_universe_d3(vds_base_universe_d2_028_vds_basefill_033, 28)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_028_vds_basefill_033'] = {'inputs': ['vds_base_universe_d2_028_vds_basefill_033'], 'func': vds_base_universe_d3_028_vds_basefill_033}


def vds_base_universe_d3_029_vds_basefill_034(vds_base_universe_d2_029_vds_basefill_034):
    return _base_universe_d3(vds_base_universe_d2_029_vds_basefill_034, 29)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_029_vds_basefill_034'] = {'inputs': ['vds_base_universe_d2_029_vds_basefill_034'], 'func': vds_base_universe_d3_029_vds_basefill_034}


def vds_base_universe_d3_030_vds_basefill_035(vds_base_universe_d2_030_vds_basefill_035):
    return _base_universe_d3(vds_base_universe_d2_030_vds_basefill_035, 30)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_030_vds_basefill_035'] = {'inputs': ['vds_base_universe_d2_030_vds_basefill_035'], 'func': vds_base_universe_d3_030_vds_basefill_035}


def vds_base_universe_d3_031_vds_basefill_036(vds_base_universe_d2_031_vds_basefill_036):
    return _base_universe_d3(vds_base_universe_d2_031_vds_basefill_036, 31)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_031_vds_basefill_036'] = {'inputs': ['vds_base_universe_d2_031_vds_basefill_036'], 'func': vds_base_universe_d3_031_vds_basefill_036}


def vds_base_universe_d3_032_vds_basefill_037(vds_base_universe_d2_032_vds_basefill_037):
    return _base_universe_d3(vds_base_universe_d2_032_vds_basefill_037, 32)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_032_vds_basefill_037'] = {'inputs': ['vds_base_universe_d2_032_vds_basefill_037'], 'func': vds_base_universe_d3_032_vds_basefill_037}


def vds_base_universe_d3_033_vds_basefill_038(vds_base_universe_d2_033_vds_basefill_038):
    return _base_universe_d3(vds_base_universe_d2_033_vds_basefill_038, 33)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_033_vds_basefill_038'] = {'inputs': ['vds_base_universe_d2_033_vds_basefill_038'], 'func': vds_base_universe_d3_033_vds_basefill_038}


def vds_base_universe_d3_034_vds_basefill_039(vds_base_universe_d2_034_vds_basefill_039):
    return _base_universe_d3(vds_base_universe_d2_034_vds_basefill_039, 34)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_034_vds_basefill_039'] = {'inputs': ['vds_base_universe_d2_034_vds_basefill_039'], 'func': vds_base_universe_d3_034_vds_basefill_039}


def vds_base_universe_d3_035_vds_basefill_040(vds_base_universe_d2_035_vds_basefill_040):
    return _base_universe_d3(vds_base_universe_d2_035_vds_basefill_040, 35)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_035_vds_basefill_040'] = {'inputs': ['vds_base_universe_d2_035_vds_basefill_040'], 'func': vds_base_universe_d3_035_vds_basefill_040}


def vds_base_universe_d3_036_vds_basefill_041(vds_base_universe_d2_036_vds_basefill_041):
    return _base_universe_d3(vds_base_universe_d2_036_vds_basefill_041, 36)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_036_vds_basefill_041'] = {'inputs': ['vds_base_universe_d2_036_vds_basefill_041'], 'func': vds_base_universe_d3_036_vds_basefill_041}


def vds_base_universe_d3_037_vds_basefill_042(vds_base_universe_d2_037_vds_basefill_042):
    return _base_universe_d3(vds_base_universe_d2_037_vds_basefill_042, 37)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_037_vds_basefill_042'] = {'inputs': ['vds_base_universe_d2_037_vds_basefill_042'], 'func': vds_base_universe_d3_037_vds_basefill_042}


def vds_base_universe_d3_038_vds_basefill_043(vds_base_universe_d2_038_vds_basefill_043):
    return _base_universe_d3(vds_base_universe_d2_038_vds_basefill_043, 38)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_038_vds_basefill_043'] = {'inputs': ['vds_base_universe_d2_038_vds_basefill_043'], 'func': vds_base_universe_d3_038_vds_basefill_043}


def vds_base_universe_d3_039_vds_basefill_044(vds_base_universe_d2_039_vds_basefill_044):
    return _base_universe_d3(vds_base_universe_d2_039_vds_basefill_044, 39)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_039_vds_basefill_044'] = {'inputs': ['vds_base_universe_d2_039_vds_basefill_044'], 'func': vds_base_universe_d3_039_vds_basefill_044}


def vds_base_universe_d3_040_vds_basefill_045(vds_base_universe_d2_040_vds_basefill_045):
    return _base_universe_d3(vds_base_universe_d2_040_vds_basefill_045, 40)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_040_vds_basefill_045'] = {'inputs': ['vds_base_universe_d2_040_vds_basefill_045'], 'func': vds_base_universe_d3_040_vds_basefill_045}


def vds_base_universe_d3_041_vds_basefill_046(vds_base_universe_d2_041_vds_basefill_046):
    return _base_universe_d3(vds_base_universe_d2_041_vds_basefill_046, 41)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_041_vds_basefill_046'] = {'inputs': ['vds_base_universe_d2_041_vds_basefill_046'], 'func': vds_base_universe_d3_041_vds_basefill_046}


def vds_base_universe_d3_042_vds_basefill_047(vds_base_universe_d2_042_vds_basefill_047):
    return _base_universe_d3(vds_base_universe_d2_042_vds_basefill_047, 42)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_042_vds_basefill_047'] = {'inputs': ['vds_base_universe_d2_042_vds_basefill_047'], 'func': vds_base_universe_d3_042_vds_basefill_047}


def vds_base_universe_d3_043_vds_basefill_048(vds_base_universe_d2_043_vds_basefill_048):
    return _base_universe_d3(vds_base_universe_d2_043_vds_basefill_048, 43)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_043_vds_basefill_048'] = {'inputs': ['vds_base_universe_d2_043_vds_basefill_048'], 'func': vds_base_universe_d3_043_vds_basefill_048}


def vds_base_universe_d3_044_vds_basefill_049(vds_base_universe_d2_044_vds_basefill_049):
    return _base_universe_d3(vds_base_universe_d2_044_vds_basefill_049, 44)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_044_vds_basefill_049'] = {'inputs': ['vds_base_universe_d2_044_vds_basefill_049'], 'func': vds_base_universe_d3_044_vds_basefill_049}


def vds_base_universe_d3_045_vds_basefill_050(vds_base_universe_d2_045_vds_basefill_050):
    return _base_universe_d3(vds_base_universe_d2_045_vds_basefill_050, 45)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_045_vds_basefill_050'] = {'inputs': ['vds_base_universe_d2_045_vds_basefill_050'], 'func': vds_base_universe_d3_045_vds_basefill_050}


def vds_base_universe_d3_046_vds_basefill_051(vds_base_universe_d2_046_vds_basefill_051):
    return _base_universe_d3(vds_base_universe_d2_046_vds_basefill_051, 46)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_046_vds_basefill_051'] = {'inputs': ['vds_base_universe_d2_046_vds_basefill_051'], 'func': vds_base_universe_d3_046_vds_basefill_051}


def vds_base_universe_d3_047_vds_basefill_052(vds_base_universe_d2_047_vds_basefill_052):
    return _base_universe_d3(vds_base_universe_d2_047_vds_basefill_052, 47)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_047_vds_basefill_052'] = {'inputs': ['vds_base_universe_d2_047_vds_basefill_052'], 'func': vds_base_universe_d3_047_vds_basefill_052}


def vds_base_universe_d3_048_vds_basefill_053(vds_base_universe_d2_048_vds_basefill_053):
    return _base_universe_d3(vds_base_universe_d2_048_vds_basefill_053, 48)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_048_vds_basefill_053'] = {'inputs': ['vds_base_universe_d2_048_vds_basefill_053'], 'func': vds_base_universe_d3_048_vds_basefill_053}


def vds_base_universe_d3_049_vds_basefill_054(vds_base_universe_d2_049_vds_basefill_054):
    return _base_universe_d3(vds_base_universe_d2_049_vds_basefill_054, 49)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_049_vds_basefill_054'] = {'inputs': ['vds_base_universe_d2_049_vds_basefill_054'], 'func': vds_base_universe_d3_049_vds_basefill_054}


def vds_base_universe_d3_050_vds_basefill_055(vds_base_universe_d2_050_vds_basefill_055):
    return _base_universe_d3(vds_base_universe_d2_050_vds_basefill_055, 50)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_050_vds_basefill_055'] = {'inputs': ['vds_base_universe_d2_050_vds_basefill_055'], 'func': vds_base_universe_d3_050_vds_basefill_055}


def vds_base_universe_d3_051_vds_basefill_056(vds_base_universe_d2_051_vds_basefill_056):
    return _base_universe_d3(vds_base_universe_d2_051_vds_basefill_056, 51)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_051_vds_basefill_056'] = {'inputs': ['vds_base_universe_d2_051_vds_basefill_056'], 'func': vds_base_universe_d3_051_vds_basefill_056}


def vds_base_universe_d3_052_vds_basefill_057(vds_base_universe_d2_052_vds_basefill_057):
    return _base_universe_d3(vds_base_universe_d2_052_vds_basefill_057, 52)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_052_vds_basefill_057'] = {'inputs': ['vds_base_universe_d2_052_vds_basefill_057'], 'func': vds_base_universe_d3_052_vds_basefill_057}


def vds_base_universe_d3_053_vds_basefill_058(vds_base_universe_d2_053_vds_basefill_058):
    return _base_universe_d3(vds_base_universe_d2_053_vds_basefill_058, 53)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_053_vds_basefill_058'] = {'inputs': ['vds_base_universe_d2_053_vds_basefill_058'], 'func': vds_base_universe_d3_053_vds_basefill_058}


def vds_base_universe_d3_054_vds_basefill_059(vds_base_universe_d2_054_vds_basefill_059):
    return _base_universe_d3(vds_base_universe_d2_054_vds_basefill_059, 54)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_054_vds_basefill_059'] = {'inputs': ['vds_base_universe_d2_054_vds_basefill_059'], 'func': vds_base_universe_d3_054_vds_basefill_059}


def vds_base_universe_d3_055_vds_basefill_060(vds_base_universe_d2_055_vds_basefill_060):
    return _base_universe_d3(vds_base_universe_d2_055_vds_basefill_060, 55)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_055_vds_basefill_060'] = {'inputs': ['vds_base_universe_d2_055_vds_basefill_060'], 'func': vds_base_universe_d3_055_vds_basefill_060}


def vds_base_universe_d3_056_vds_basefill_061(vds_base_universe_d2_056_vds_basefill_061):
    return _base_universe_d3(vds_base_universe_d2_056_vds_basefill_061, 56)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_056_vds_basefill_061'] = {'inputs': ['vds_base_universe_d2_056_vds_basefill_061'], 'func': vds_base_universe_d3_056_vds_basefill_061}


def vds_base_universe_d3_057_vds_basefill_062(vds_base_universe_d2_057_vds_basefill_062):
    return _base_universe_d3(vds_base_universe_d2_057_vds_basefill_062, 57)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_057_vds_basefill_062'] = {'inputs': ['vds_base_universe_d2_057_vds_basefill_062'], 'func': vds_base_universe_d3_057_vds_basefill_062}


def vds_base_universe_d3_058_vds_basefill_063(vds_base_universe_d2_058_vds_basefill_063):
    return _base_universe_d3(vds_base_universe_d2_058_vds_basefill_063, 58)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_058_vds_basefill_063'] = {'inputs': ['vds_base_universe_d2_058_vds_basefill_063'], 'func': vds_base_universe_d3_058_vds_basefill_063}


def vds_base_universe_d3_059_vds_basefill_064(vds_base_universe_d2_059_vds_basefill_064):
    return _base_universe_d3(vds_base_universe_d2_059_vds_basefill_064, 59)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_059_vds_basefill_064'] = {'inputs': ['vds_base_universe_d2_059_vds_basefill_064'], 'func': vds_base_universe_d3_059_vds_basefill_064}


def vds_base_universe_d3_060_vds_basefill_065(vds_base_universe_d2_060_vds_basefill_065):
    return _base_universe_d3(vds_base_universe_d2_060_vds_basefill_065, 60)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_060_vds_basefill_065'] = {'inputs': ['vds_base_universe_d2_060_vds_basefill_065'], 'func': vds_base_universe_d3_060_vds_basefill_065}


def vds_base_universe_d3_061_vds_basefill_066(vds_base_universe_d2_061_vds_basefill_066):
    return _base_universe_d3(vds_base_universe_d2_061_vds_basefill_066, 61)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_061_vds_basefill_066'] = {'inputs': ['vds_base_universe_d2_061_vds_basefill_066'], 'func': vds_base_universe_d3_061_vds_basefill_066}


def vds_base_universe_d3_062_vds_basefill_067(vds_base_universe_d2_062_vds_basefill_067):
    return _base_universe_d3(vds_base_universe_d2_062_vds_basefill_067, 62)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_062_vds_basefill_067'] = {'inputs': ['vds_base_universe_d2_062_vds_basefill_067'], 'func': vds_base_universe_d3_062_vds_basefill_067}


def vds_base_universe_d3_063_vds_basefill_068(vds_base_universe_d2_063_vds_basefill_068):
    return _base_universe_d3(vds_base_universe_d2_063_vds_basefill_068, 63)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_063_vds_basefill_068'] = {'inputs': ['vds_base_universe_d2_063_vds_basefill_068'], 'func': vds_base_universe_d3_063_vds_basefill_068}


def vds_base_universe_d3_064_vds_basefill_069(vds_base_universe_d2_064_vds_basefill_069):
    return _base_universe_d3(vds_base_universe_d2_064_vds_basefill_069, 64)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_064_vds_basefill_069'] = {'inputs': ['vds_base_universe_d2_064_vds_basefill_069'], 'func': vds_base_universe_d3_064_vds_basefill_069}


def vds_base_universe_d3_065_vds_basefill_070(vds_base_universe_d2_065_vds_basefill_070):
    return _base_universe_d3(vds_base_universe_d2_065_vds_basefill_070, 65)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_065_vds_basefill_070'] = {'inputs': ['vds_base_universe_d2_065_vds_basefill_070'], 'func': vds_base_universe_d3_065_vds_basefill_070}


def vds_base_universe_d3_066_vds_basefill_071(vds_base_universe_d2_066_vds_basefill_071):
    return _base_universe_d3(vds_base_universe_d2_066_vds_basefill_071, 66)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_066_vds_basefill_071'] = {'inputs': ['vds_base_universe_d2_066_vds_basefill_071'], 'func': vds_base_universe_d3_066_vds_basefill_071}


def vds_base_universe_d3_067_vds_basefill_072(vds_base_universe_d2_067_vds_basefill_072):
    return _base_universe_d3(vds_base_universe_d2_067_vds_basefill_072, 67)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_067_vds_basefill_072'] = {'inputs': ['vds_base_universe_d2_067_vds_basefill_072'], 'func': vds_base_universe_d3_067_vds_basefill_072}


def vds_base_universe_d3_068_vds_basefill_073(vds_base_universe_d2_068_vds_basefill_073):
    return _base_universe_d3(vds_base_universe_d2_068_vds_basefill_073, 68)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_068_vds_basefill_073'] = {'inputs': ['vds_base_universe_d2_068_vds_basefill_073'], 'func': vds_base_universe_d3_068_vds_basefill_073}


def vds_base_universe_d3_069_vds_basefill_074(vds_base_universe_d2_069_vds_basefill_074):
    return _base_universe_d3(vds_base_universe_d2_069_vds_basefill_074, 69)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_069_vds_basefill_074'] = {'inputs': ['vds_base_universe_d2_069_vds_basefill_074'], 'func': vds_base_universe_d3_069_vds_basefill_074}


def vds_base_universe_d3_070_vds_basefill_075(vds_base_universe_d2_070_vds_basefill_075):
    return _base_universe_d3(vds_base_universe_d2_070_vds_basefill_075, 70)
VDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vds_base_universe_d3_070_vds_basefill_075'] = {'inputs': ['vds_base_universe_d2_070_vds_basefill_075'], 'func': vds_base_universe_d3_070_vds_basefill_075}
