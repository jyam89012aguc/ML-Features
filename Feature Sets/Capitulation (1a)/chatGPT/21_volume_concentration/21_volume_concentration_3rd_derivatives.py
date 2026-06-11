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



def vcc_176_vcc_001_volume_spike_ratio_5_001_accel_1(vcc_151_vcc_001_volume_spike_ratio_5_001_roc_1):
    feature = _s(vcc_151_vcc_001_volume_spike_ratio_5_001_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def vcc_177_vcc_007_volume_spike_ratio_126_007_accel_5(vcc_152_vcc_007_volume_spike_ratio_126_007_roc_5):
    feature = _s(vcc_152_vcc_007_volume_spike_ratio_126_007_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def vcc_178_vcc_013_volume_spike_ratio_1008_013_accel_42(vcc_153_vcc_013_volume_spike_ratio_1008_013_roc_42):
    feature = _s(vcc_153_vcc_013_volume_spike_ratio_1008_013_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def vcc_179_vcc_019_volume_spike_ratio_42_019_accel_126(vcc_154_vcc_019_volume_spike_ratio_42_019_roc_126):
    feature = _s(vcc_154_vcc_019_volume_spike_ratio_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def vcc_180_vcc_025_volume_spike_ratio_378_025_accel_378(vcc_155_vcc_025_volume_spike_ratio_378_025_roc_378):
    feature = _s(vcc_155_vcc_025_volume_spike_ratio_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















VOLUME_CONCENTRATION_REGISTRY_3RD_DERIVATIVES = {
    'vcc_176_vcc_001_volume_spike_ratio_5_001_accel_1': {'inputs': ['vcc_151_vcc_001_volume_spike_ratio_5_001_roc_1'], 'func': vcc_176_vcc_001_volume_spike_ratio_5_001_accel_1},
    'vcc_177_vcc_007_volume_spike_ratio_126_007_accel_5': {'inputs': ['vcc_152_vcc_007_volume_spike_ratio_126_007_roc_5'], 'func': vcc_177_vcc_007_volume_spike_ratio_126_007_accel_5},
    'vcc_178_vcc_013_volume_spike_ratio_1008_013_accel_42': {'inputs': ['vcc_153_vcc_013_volume_spike_ratio_1008_013_roc_42'], 'func': vcc_178_vcc_013_volume_spike_ratio_1008_013_accel_42},
    'vcc_179_vcc_019_volume_spike_ratio_42_019_accel_126': {'inputs': ['vcc_154_vcc_019_volume_spike_ratio_42_019_roc_126'], 'func': vcc_179_vcc_019_volume_spike_ratio_42_019_accel_126},
    'vcc_180_vcc_025_volume_spike_ratio_378_025_accel_378': {'inputs': ['vcc_155_vcc_025_volume_spike_ratio_378_025_roc_378'], 'func': vcc_180_vcc_025_volume_spike_ratio_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def vc_replacement_d3_001(vc_replacement_d2_001):
    feature = _clean(vc_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_001'] = {'inputs': ['vc_replacement_d2_001'], 'func': vc_replacement_d3_001}


def vc_replacement_d3_002(vc_replacement_d2_002):
    feature = _clean(vc_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_002'] = {'inputs': ['vc_replacement_d2_002'], 'func': vc_replacement_d3_002}


def vc_replacement_d3_003(vc_replacement_d2_003):
    feature = _clean(vc_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_003'] = {'inputs': ['vc_replacement_d2_003'], 'func': vc_replacement_d3_003}


def vc_replacement_d3_004(vc_replacement_d2_004):
    feature = _clean(vc_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_004'] = {'inputs': ['vc_replacement_d2_004'], 'func': vc_replacement_d3_004}


def vc_replacement_d3_005(vc_replacement_d2_005):
    feature = _clean(vc_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_005'] = {'inputs': ['vc_replacement_d2_005'], 'func': vc_replacement_d3_005}


def vc_replacement_d3_006(vc_replacement_d2_006):
    feature = _clean(vc_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_006'] = {'inputs': ['vc_replacement_d2_006'], 'func': vc_replacement_d3_006}


def vc_replacement_d3_007(vc_replacement_d2_007):
    feature = _clean(vc_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_007'] = {'inputs': ['vc_replacement_d2_007'], 'func': vc_replacement_d3_007}


def vc_replacement_d3_008(vc_replacement_d2_008):
    feature = _clean(vc_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_008'] = {'inputs': ['vc_replacement_d2_008'], 'func': vc_replacement_d3_008}


def vc_replacement_d3_009(vc_replacement_d2_009):
    feature = _clean(vc_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_009'] = {'inputs': ['vc_replacement_d2_009'], 'func': vc_replacement_d3_009}


def vc_replacement_d3_010(vc_replacement_d2_010):
    feature = _clean(vc_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_010'] = {'inputs': ['vc_replacement_d2_010'], 'func': vc_replacement_d3_010}


def vc_replacement_d3_011(vc_replacement_d2_011):
    feature = _clean(vc_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_011'] = {'inputs': ['vc_replacement_d2_011'], 'func': vc_replacement_d3_011}


def vc_replacement_d3_012(vc_replacement_d2_012):
    feature = _clean(vc_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_012'] = {'inputs': ['vc_replacement_d2_012'], 'func': vc_replacement_d3_012}


def vc_replacement_d3_013(vc_replacement_d2_013):
    feature = _clean(vc_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_013'] = {'inputs': ['vc_replacement_d2_013'], 'func': vc_replacement_d3_013}


def vc_replacement_d3_014(vc_replacement_d2_014):
    feature = _clean(vc_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_014'] = {'inputs': ['vc_replacement_d2_014'], 'func': vc_replacement_d3_014}


def vc_replacement_d3_015(vc_replacement_d2_015):
    feature = _clean(vc_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_015'] = {'inputs': ['vc_replacement_d2_015'], 'func': vc_replacement_d3_015}


def vc_replacement_d3_016(vc_replacement_d2_016):
    feature = _clean(vc_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_016'] = {'inputs': ['vc_replacement_d2_016'], 'func': vc_replacement_d3_016}


def vc_replacement_d3_017(vc_replacement_d2_017):
    feature = _clean(vc_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_017'] = {'inputs': ['vc_replacement_d2_017'], 'func': vc_replacement_d3_017}


def vc_replacement_d3_018(vc_replacement_d2_018):
    feature = _clean(vc_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_018'] = {'inputs': ['vc_replacement_d2_018'], 'func': vc_replacement_d3_018}


def vc_replacement_d3_019(vc_replacement_d2_019):
    feature = _clean(vc_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_019'] = {'inputs': ['vc_replacement_d2_019'], 'func': vc_replacement_d3_019}


def vc_replacement_d3_020(vc_replacement_d2_020):
    feature = _clean(vc_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_020'] = {'inputs': ['vc_replacement_d2_020'], 'func': vc_replacement_d3_020}


def vc_replacement_d3_021(vc_replacement_d2_021):
    feature = _clean(vc_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_021'] = {'inputs': ['vc_replacement_d2_021'], 'func': vc_replacement_d3_021}


def vc_replacement_d3_022(vc_replacement_d2_022):
    feature = _clean(vc_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_022'] = {'inputs': ['vc_replacement_d2_022'], 'func': vc_replacement_d3_022}


def vc_replacement_d3_023(vc_replacement_d2_023):
    feature = _clean(vc_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_023'] = {'inputs': ['vc_replacement_d2_023'], 'func': vc_replacement_d3_023}


def vc_replacement_d3_024(vc_replacement_d2_024):
    feature = _clean(vc_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_024'] = {'inputs': ['vc_replacement_d2_024'], 'func': vc_replacement_d3_024}


def vc_replacement_d3_025(vc_replacement_d2_025):
    feature = _clean(vc_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_025'] = {'inputs': ['vc_replacement_d2_025'], 'func': vc_replacement_d3_025}


def vc_replacement_d3_026(vc_replacement_d2_026):
    feature = _clean(vc_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_026'] = {'inputs': ['vc_replacement_d2_026'], 'func': vc_replacement_d3_026}


def vc_replacement_d3_027(vc_replacement_d2_027):
    feature = _clean(vc_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_027'] = {'inputs': ['vc_replacement_d2_027'], 'func': vc_replacement_d3_027}


def vc_replacement_d3_028(vc_replacement_d2_028):
    feature = _clean(vc_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_028'] = {'inputs': ['vc_replacement_d2_028'], 'func': vc_replacement_d3_028}


def vc_replacement_d3_029(vc_replacement_d2_029):
    feature = _clean(vc_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_029'] = {'inputs': ['vc_replacement_d2_029'], 'func': vc_replacement_d3_029}


def vc_replacement_d3_030(vc_replacement_d2_030):
    feature = _clean(vc_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_030'] = {'inputs': ['vc_replacement_d2_030'], 'func': vc_replacement_d3_030}


def vc_replacement_d3_031(vc_replacement_d2_031):
    feature = _clean(vc_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_031'] = {'inputs': ['vc_replacement_d2_031'], 'func': vc_replacement_d3_031}


def vc_replacement_d3_032(vc_replacement_d2_032):
    feature = _clean(vc_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_032'] = {'inputs': ['vc_replacement_d2_032'], 'func': vc_replacement_d3_032}


def vc_replacement_d3_033(vc_replacement_d2_033):
    feature = _clean(vc_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_033'] = {'inputs': ['vc_replacement_d2_033'], 'func': vc_replacement_d3_033}


def vc_replacement_d3_034(vc_replacement_d2_034):
    feature = _clean(vc_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_034'] = {'inputs': ['vc_replacement_d2_034'], 'func': vc_replacement_d3_034}


def vc_replacement_d3_035(vc_replacement_d2_035):
    feature = _clean(vc_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_035'] = {'inputs': ['vc_replacement_d2_035'], 'func': vc_replacement_d3_035}


def vc_replacement_d3_036(vc_replacement_d2_036):
    feature = _clean(vc_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_036'] = {'inputs': ['vc_replacement_d2_036'], 'func': vc_replacement_d3_036}


def vc_replacement_d3_037(vc_replacement_d2_037):
    feature = _clean(vc_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_037'] = {'inputs': ['vc_replacement_d2_037'], 'func': vc_replacement_d3_037}


def vc_replacement_d3_038(vc_replacement_d2_038):
    feature = _clean(vc_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_038'] = {'inputs': ['vc_replacement_d2_038'], 'func': vc_replacement_d3_038}


def vc_replacement_d3_039(vc_replacement_d2_039):
    feature = _clean(vc_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_039'] = {'inputs': ['vc_replacement_d2_039'], 'func': vc_replacement_d3_039}


def vc_replacement_d3_040(vc_replacement_d2_040):
    feature = _clean(vc_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_040'] = {'inputs': ['vc_replacement_d2_040'], 'func': vc_replacement_d3_040}


def vc_replacement_d3_041(vc_replacement_d2_041):
    feature = _clean(vc_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_041'] = {'inputs': ['vc_replacement_d2_041'], 'func': vc_replacement_d3_041}


def vc_replacement_d3_042(vc_replacement_d2_042):
    feature = _clean(vc_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_042'] = {'inputs': ['vc_replacement_d2_042'], 'func': vc_replacement_d3_042}


def vc_replacement_d3_043(vc_replacement_d2_043):
    feature = _clean(vc_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_043'] = {'inputs': ['vc_replacement_d2_043'], 'func': vc_replacement_d3_043}


def vc_replacement_d3_044(vc_replacement_d2_044):
    feature = _clean(vc_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_044'] = {'inputs': ['vc_replacement_d2_044'], 'func': vc_replacement_d3_044}


def vc_replacement_d3_045(vc_replacement_d2_045):
    feature = _clean(vc_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_045'] = {'inputs': ['vc_replacement_d2_045'], 'func': vc_replacement_d3_045}


def vc_replacement_d3_046(vc_replacement_d2_046):
    feature = _clean(vc_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_046'] = {'inputs': ['vc_replacement_d2_046'], 'func': vc_replacement_d3_046}


def vc_replacement_d3_047(vc_replacement_d2_047):
    feature = _clean(vc_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_047'] = {'inputs': ['vc_replacement_d2_047'], 'func': vc_replacement_d3_047}


def vc_replacement_d3_048(vc_replacement_d2_048):
    feature = _clean(vc_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_048'] = {'inputs': ['vc_replacement_d2_048'], 'func': vc_replacement_d3_048}


def vc_replacement_d3_049(vc_replacement_d2_049):
    feature = _clean(vc_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_049'] = {'inputs': ['vc_replacement_d2_049'], 'func': vc_replacement_d3_049}


def vc_replacement_d3_050(vc_replacement_d2_050):
    feature = _clean(vc_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_050'] = {'inputs': ['vc_replacement_d2_050'], 'func': vc_replacement_d3_050}


def vc_replacement_d3_051(vc_replacement_d2_051):
    feature = _clean(vc_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_051'] = {'inputs': ['vc_replacement_d2_051'], 'func': vc_replacement_d3_051}


def vc_replacement_d3_052(vc_replacement_d2_052):
    feature = _clean(vc_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_052'] = {'inputs': ['vc_replacement_d2_052'], 'func': vc_replacement_d3_052}


def vc_replacement_d3_053(vc_replacement_d2_053):
    feature = _clean(vc_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_053'] = {'inputs': ['vc_replacement_d2_053'], 'func': vc_replacement_d3_053}


def vc_replacement_d3_054(vc_replacement_d2_054):
    feature = _clean(vc_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_054'] = {'inputs': ['vc_replacement_d2_054'], 'func': vc_replacement_d3_054}


def vc_replacement_d3_055(vc_replacement_d2_055):
    feature = _clean(vc_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_055'] = {'inputs': ['vc_replacement_d2_055'], 'func': vc_replacement_d3_055}


def vc_replacement_d3_056(vc_replacement_d2_056):
    feature = _clean(vc_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_056'] = {'inputs': ['vc_replacement_d2_056'], 'func': vc_replacement_d3_056}


def vc_replacement_d3_057(vc_replacement_d2_057):
    feature = _clean(vc_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_057'] = {'inputs': ['vc_replacement_d2_057'], 'func': vc_replacement_d3_057}


def vc_replacement_d3_058(vc_replacement_d2_058):
    feature = _clean(vc_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_058'] = {'inputs': ['vc_replacement_d2_058'], 'func': vc_replacement_d3_058}


def vc_replacement_d3_059(vc_replacement_d2_059):
    feature = _clean(vc_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_059'] = {'inputs': ['vc_replacement_d2_059'], 'func': vc_replacement_d3_059}


def vc_replacement_d3_060(vc_replacement_d2_060):
    feature = _clean(vc_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_060'] = {'inputs': ['vc_replacement_d2_060'], 'func': vc_replacement_d3_060}


def vc_replacement_d3_061(vc_replacement_d2_061):
    feature = _clean(vc_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_061'] = {'inputs': ['vc_replacement_d2_061'], 'func': vc_replacement_d3_061}


def vc_replacement_d3_062(vc_replacement_d2_062):
    feature = _clean(vc_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_062'] = {'inputs': ['vc_replacement_d2_062'], 'func': vc_replacement_d3_062}


def vc_replacement_d3_063(vc_replacement_d2_063):
    feature = _clean(vc_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_063'] = {'inputs': ['vc_replacement_d2_063'], 'func': vc_replacement_d3_063}


def vc_replacement_d3_064(vc_replacement_d2_064):
    feature = _clean(vc_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_064'] = {'inputs': ['vc_replacement_d2_064'], 'func': vc_replacement_d3_064}


def vc_replacement_d3_065(vc_replacement_d2_065):
    feature = _clean(vc_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_065'] = {'inputs': ['vc_replacement_d2_065'], 'func': vc_replacement_d3_065}


def vc_replacement_d3_066(vc_replacement_d2_066):
    feature = _clean(vc_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_066'] = {'inputs': ['vc_replacement_d2_066'], 'func': vc_replacement_d3_066}


def vc_replacement_d3_067(vc_replacement_d2_067):
    feature = _clean(vc_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_067'] = {'inputs': ['vc_replacement_d2_067'], 'func': vc_replacement_d3_067}


def vc_replacement_d3_068(vc_replacement_d2_068):
    feature = _clean(vc_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_068'] = {'inputs': ['vc_replacement_d2_068'], 'func': vc_replacement_d3_068}


def vc_replacement_d3_069(vc_replacement_d2_069):
    feature = _clean(vc_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_069'] = {'inputs': ['vc_replacement_d2_069'], 'func': vc_replacement_d3_069}


def vc_replacement_d3_070(vc_replacement_d2_070):
    feature = _clean(vc_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_070'] = {'inputs': ['vc_replacement_d2_070'], 'func': vc_replacement_d3_070}


def vc_replacement_d3_071(vc_replacement_d2_071):
    feature = _clean(vc_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_071'] = {'inputs': ['vc_replacement_d2_071'], 'func': vc_replacement_d3_071}


def vc_replacement_d3_072(vc_replacement_d2_072):
    feature = _clean(vc_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_072'] = {'inputs': ['vc_replacement_d2_072'], 'func': vc_replacement_d3_072}


def vc_replacement_d3_073(vc_replacement_d2_073):
    feature = _clean(vc_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_073'] = {'inputs': ['vc_replacement_d2_073'], 'func': vc_replacement_d3_073}


def vc_replacement_d3_074(vc_replacement_d2_074):
    feature = _clean(vc_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_074'] = {'inputs': ['vc_replacement_d2_074'], 'func': vc_replacement_d3_074}


def vc_replacement_d3_075(vc_replacement_d2_075):
    feature = _clean(vc_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_075'] = {'inputs': ['vc_replacement_d2_075'], 'func': vc_replacement_d3_075}


def vc_replacement_d3_076(vc_replacement_d2_076):
    feature = _clean(vc_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_076'] = {'inputs': ['vc_replacement_d2_076'], 'func': vc_replacement_d3_076}


def vc_replacement_d3_077(vc_replacement_d2_077):
    feature = _clean(vc_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_077'] = {'inputs': ['vc_replacement_d2_077'], 'func': vc_replacement_d3_077}


def vc_replacement_d3_078(vc_replacement_d2_078):
    feature = _clean(vc_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_078'] = {'inputs': ['vc_replacement_d2_078'], 'func': vc_replacement_d3_078}


def vc_replacement_d3_079(vc_replacement_d2_079):
    feature = _clean(vc_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_079'] = {'inputs': ['vc_replacement_d2_079'], 'func': vc_replacement_d3_079}


def vc_replacement_d3_080(vc_replacement_d2_080):
    feature = _clean(vc_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_080'] = {'inputs': ['vc_replacement_d2_080'], 'func': vc_replacement_d3_080}


def vc_replacement_d3_081(vc_replacement_d2_081):
    feature = _clean(vc_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_081'] = {'inputs': ['vc_replacement_d2_081'], 'func': vc_replacement_d3_081}


def vc_replacement_d3_082(vc_replacement_d2_082):
    feature = _clean(vc_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_082'] = {'inputs': ['vc_replacement_d2_082'], 'func': vc_replacement_d3_082}


def vc_replacement_d3_083(vc_replacement_d2_083):
    feature = _clean(vc_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_083'] = {'inputs': ['vc_replacement_d2_083'], 'func': vc_replacement_d3_083}


def vc_replacement_d3_084(vc_replacement_d2_084):
    feature = _clean(vc_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_084'] = {'inputs': ['vc_replacement_d2_084'], 'func': vc_replacement_d3_084}


def vc_replacement_d3_085(vc_replacement_d2_085):
    feature = _clean(vc_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_085'] = {'inputs': ['vc_replacement_d2_085'], 'func': vc_replacement_d3_085}


def vc_replacement_d3_086(vc_replacement_d2_086):
    feature = _clean(vc_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_086'] = {'inputs': ['vc_replacement_d2_086'], 'func': vc_replacement_d3_086}


def vc_replacement_d3_087(vc_replacement_d2_087):
    feature = _clean(vc_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_087'] = {'inputs': ['vc_replacement_d2_087'], 'func': vc_replacement_d3_087}


def vc_replacement_d3_088(vc_replacement_d2_088):
    feature = _clean(vc_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_088'] = {'inputs': ['vc_replacement_d2_088'], 'func': vc_replacement_d3_088}


def vc_replacement_d3_089(vc_replacement_d2_089):
    feature = _clean(vc_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_089'] = {'inputs': ['vc_replacement_d2_089'], 'func': vc_replacement_d3_089}


def vc_replacement_d3_090(vc_replacement_d2_090):
    feature = _clean(vc_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_090'] = {'inputs': ['vc_replacement_d2_090'], 'func': vc_replacement_d3_090}


def vc_replacement_d3_091(vc_replacement_d2_091):
    feature = _clean(vc_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_091'] = {'inputs': ['vc_replacement_d2_091'], 'func': vc_replacement_d3_091}


def vc_replacement_d3_092(vc_replacement_d2_092):
    feature = _clean(vc_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_092'] = {'inputs': ['vc_replacement_d2_092'], 'func': vc_replacement_d3_092}


def vc_replacement_d3_093(vc_replacement_d2_093):
    feature = _clean(vc_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_093'] = {'inputs': ['vc_replacement_d2_093'], 'func': vc_replacement_d3_093}


def vc_replacement_d3_094(vc_replacement_d2_094):
    feature = _clean(vc_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_094'] = {'inputs': ['vc_replacement_d2_094'], 'func': vc_replacement_d3_094}


def vc_replacement_d3_095(vc_replacement_d2_095):
    feature = _clean(vc_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_095'] = {'inputs': ['vc_replacement_d2_095'], 'func': vc_replacement_d3_095}


def vc_replacement_d3_096(vc_replacement_d2_096):
    feature = _clean(vc_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_096'] = {'inputs': ['vc_replacement_d2_096'], 'func': vc_replacement_d3_096}


def vc_replacement_d3_097(vc_replacement_d2_097):
    feature = _clean(vc_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_097'] = {'inputs': ['vc_replacement_d2_097'], 'func': vc_replacement_d3_097}


def vc_replacement_d3_098(vc_replacement_d2_098):
    feature = _clean(vc_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_098'] = {'inputs': ['vc_replacement_d2_098'], 'func': vc_replacement_d3_098}


def vc_replacement_d3_099(vc_replacement_d2_099):
    feature = _clean(vc_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_099'] = {'inputs': ['vc_replacement_d2_099'], 'func': vc_replacement_d3_099}


def vc_replacement_d3_100(vc_replacement_d2_100):
    feature = _clean(vc_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_100'] = {'inputs': ['vc_replacement_d2_100'], 'func': vc_replacement_d3_100}


def vc_replacement_d3_101(vc_replacement_d2_101):
    feature = _clean(vc_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_101'] = {'inputs': ['vc_replacement_d2_101'], 'func': vc_replacement_d3_101}


def vc_replacement_d3_102(vc_replacement_d2_102):
    feature = _clean(vc_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_102'] = {'inputs': ['vc_replacement_d2_102'], 'func': vc_replacement_d3_102}


def vc_replacement_d3_103(vc_replacement_d2_103):
    feature = _clean(vc_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_103'] = {'inputs': ['vc_replacement_d2_103'], 'func': vc_replacement_d3_103}


def vc_replacement_d3_104(vc_replacement_d2_104):
    feature = _clean(vc_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_104'] = {'inputs': ['vc_replacement_d2_104'], 'func': vc_replacement_d3_104}


def vc_replacement_d3_105(vc_replacement_d2_105):
    feature = _clean(vc_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_105'] = {'inputs': ['vc_replacement_d2_105'], 'func': vc_replacement_d3_105}


def vc_replacement_d3_106(vc_replacement_d2_106):
    feature = _clean(vc_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_106'] = {'inputs': ['vc_replacement_d2_106'], 'func': vc_replacement_d3_106}


def vc_replacement_d3_107(vc_replacement_d2_107):
    feature = _clean(vc_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_107'] = {'inputs': ['vc_replacement_d2_107'], 'func': vc_replacement_d3_107}


def vc_replacement_d3_108(vc_replacement_d2_108):
    feature = _clean(vc_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_108'] = {'inputs': ['vc_replacement_d2_108'], 'func': vc_replacement_d3_108}


def vc_replacement_d3_109(vc_replacement_d2_109):
    feature = _clean(vc_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_109'] = {'inputs': ['vc_replacement_d2_109'], 'func': vc_replacement_d3_109}


def vc_replacement_d3_110(vc_replacement_d2_110):
    feature = _clean(vc_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_110'] = {'inputs': ['vc_replacement_d2_110'], 'func': vc_replacement_d3_110}


def vc_replacement_d3_111(vc_replacement_d2_111):
    feature = _clean(vc_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_111'] = {'inputs': ['vc_replacement_d2_111'], 'func': vc_replacement_d3_111}


def vc_replacement_d3_112(vc_replacement_d2_112):
    feature = _clean(vc_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_112'] = {'inputs': ['vc_replacement_d2_112'], 'func': vc_replacement_d3_112}


def vc_replacement_d3_113(vc_replacement_d2_113):
    feature = _clean(vc_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_113'] = {'inputs': ['vc_replacement_d2_113'], 'func': vc_replacement_d3_113}


def vc_replacement_d3_114(vc_replacement_d2_114):
    feature = _clean(vc_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_114'] = {'inputs': ['vc_replacement_d2_114'], 'func': vc_replacement_d3_114}


def vc_replacement_d3_115(vc_replacement_d2_115):
    feature = _clean(vc_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_115'] = {'inputs': ['vc_replacement_d2_115'], 'func': vc_replacement_d3_115}


def vc_replacement_d3_116(vc_replacement_d2_116):
    feature = _clean(vc_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_116'] = {'inputs': ['vc_replacement_d2_116'], 'func': vc_replacement_d3_116}


def vc_replacement_d3_117(vc_replacement_d2_117):
    feature = _clean(vc_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_117'] = {'inputs': ['vc_replacement_d2_117'], 'func': vc_replacement_d3_117}


def vc_replacement_d3_118(vc_replacement_d2_118):
    feature = _clean(vc_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_118'] = {'inputs': ['vc_replacement_d2_118'], 'func': vc_replacement_d3_118}


def vc_replacement_d3_119(vc_replacement_d2_119):
    feature = _clean(vc_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_119'] = {'inputs': ['vc_replacement_d2_119'], 'func': vc_replacement_d3_119}


def vc_replacement_d3_120(vc_replacement_d2_120):
    feature = _clean(vc_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_120'] = {'inputs': ['vc_replacement_d2_120'], 'func': vc_replacement_d3_120}


def vc_replacement_d3_121(vc_replacement_d2_121):
    feature = _clean(vc_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_121'] = {'inputs': ['vc_replacement_d2_121'], 'func': vc_replacement_d3_121}


def vc_replacement_d3_122(vc_replacement_d2_122):
    feature = _clean(vc_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_122'] = {'inputs': ['vc_replacement_d2_122'], 'func': vc_replacement_d3_122}


def vc_replacement_d3_123(vc_replacement_d2_123):
    feature = _clean(vc_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_123'] = {'inputs': ['vc_replacement_d2_123'], 'func': vc_replacement_d3_123}


def vc_replacement_d3_124(vc_replacement_d2_124):
    feature = _clean(vc_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_124'] = {'inputs': ['vc_replacement_d2_124'], 'func': vc_replacement_d3_124}


def vc_replacement_d3_125(vc_replacement_d2_125):
    feature = _clean(vc_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_125'] = {'inputs': ['vc_replacement_d2_125'], 'func': vc_replacement_d3_125}


def vc_replacement_d3_126(vc_replacement_d2_126):
    feature = _clean(vc_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_126'] = {'inputs': ['vc_replacement_d2_126'], 'func': vc_replacement_d3_126}


def vc_replacement_d3_127(vc_replacement_d2_127):
    feature = _clean(vc_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_127'] = {'inputs': ['vc_replacement_d2_127'], 'func': vc_replacement_d3_127}


def vc_replacement_d3_128(vc_replacement_d2_128):
    feature = _clean(vc_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_128'] = {'inputs': ['vc_replacement_d2_128'], 'func': vc_replacement_d3_128}


def vc_replacement_d3_129(vc_replacement_d2_129):
    feature = _clean(vc_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_129'] = {'inputs': ['vc_replacement_d2_129'], 'func': vc_replacement_d3_129}


def vc_replacement_d3_130(vc_replacement_d2_130):
    feature = _clean(vc_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_130'] = {'inputs': ['vc_replacement_d2_130'], 'func': vc_replacement_d3_130}


def vc_replacement_d3_131(vc_replacement_d2_131):
    feature = _clean(vc_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_131'] = {'inputs': ['vc_replacement_d2_131'], 'func': vc_replacement_d3_131}


def vc_replacement_d3_132(vc_replacement_d2_132):
    feature = _clean(vc_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_132'] = {'inputs': ['vc_replacement_d2_132'], 'func': vc_replacement_d3_132}


def vc_replacement_d3_133(vc_replacement_d2_133):
    feature = _clean(vc_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_133'] = {'inputs': ['vc_replacement_d2_133'], 'func': vc_replacement_d3_133}


def vc_replacement_d3_134(vc_replacement_d2_134):
    feature = _clean(vc_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_134'] = {'inputs': ['vc_replacement_d2_134'], 'func': vc_replacement_d3_134}


def vc_replacement_d3_135(vc_replacement_d2_135):
    feature = _clean(vc_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_135'] = {'inputs': ['vc_replacement_d2_135'], 'func': vc_replacement_d3_135}


def vc_replacement_d3_136(vc_replacement_d2_136):
    feature = _clean(vc_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_136'] = {'inputs': ['vc_replacement_d2_136'], 'func': vc_replacement_d3_136}


def vc_replacement_d3_137(vc_replacement_d2_137):
    feature = _clean(vc_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_137'] = {'inputs': ['vc_replacement_d2_137'], 'func': vc_replacement_d3_137}


def vc_replacement_d3_138(vc_replacement_d2_138):
    feature = _clean(vc_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_138'] = {'inputs': ['vc_replacement_d2_138'], 'func': vc_replacement_d3_138}


def vc_replacement_d3_139(vc_replacement_d2_139):
    feature = _clean(vc_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_139'] = {'inputs': ['vc_replacement_d2_139'], 'func': vc_replacement_d3_139}


def vc_replacement_d3_140(vc_replacement_d2_140):
    feature = _clean(vc_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_140'] = {'inputs': ['vc_replacement_d2_140'], 'func': vc_replacement_d3_140}


def vc_replacement_d3_141(vc_replacement_d2_141):
    feature = _clean(vc_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_141'] = {'inputs': ['vc_replacement_d2_141'], 'func': vc_replacement_d3_141}


def vc_replacement_d3_142(vc_replacement_d2_142):
    feature = _clean(vc_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_142'] = {'inputs': ['vc_replacement_d2_142'], 'func': vc_replacement_d3_142}


def vc_replacement_d3_143(vc_replacement_d2_143):
    feature = _clean(vc_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_143'] = {'inputs': ['vc_replacement_d2_143'], 'func': vc_replacement_d3_143}


def vc_replacement_d3_144(vc_replacement_d2_144):
    feature = _clean(vc_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_144'] = {'inputs': ['vc_replacement_d2_144'], 'func': vc_replacement_d3_144}


def vc_replacement_d3_145(vc_replacement_d2_145):
    feature = _clean(vc_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_145'] = {'inputs': ['vc_replacement_d2_145'], 'func': vc_replacement_d3_145}


def vc_replacement_d3_146(vc_replacement_d2_146):
    feature = _clean(vc_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_146'] = {'inputs': ['vc_replacement_d2_146'], 'func': vc_replacement_d3_146}


def vc_replacement_d3_147(vc_replacement_d2_147):
    feature = _clean(vc_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_147'] = {'inputs': ['vc_replacement_d2_147'], 'func': vc_replacement_d3_147}


def vc_replacement_d3_148(vc_replacement_d2_148):
    feature = _clean(vc_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_148'] = {'inputs': ['vc_replacement_d2_148'], 'func': vc_replacement_d3_148}


def vc_replacement_d3_149(vc_replacement_d2_149):
    feature = _clean(vc_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_149'] = {'inputs': ['vc_replacement_d2_149'], 'func': vc_replacement_d3_149}


def vc_replacement_d3_150(vc_replacement_d2_150):
    feature = _clean(vc_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_150'] = {'inputs': ['vc_replacement_d2_150'], 'func': vc_replacement_d3_150}


def vc_replacement_d3_151(vc_replacement_d2_151):
    feature = _clean(vc_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_151'] = {'inputs': ['vc_replacement_d2_151'], 'func': vc_replacement_d3_151}


def vc_replacement_d3_152(vc_replacement_d2_152):
    feature = _clean(vc_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_152'] = {'inputs': ['vc_replacement_d2_152'], 'func': vc_replacement_d3_152}


def vc_replacement_d3_153(vc_replacement_d2_153):
    feature = _clean(vc_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_153'] = {'inputs': ['vc_replacement_d2_153'], 'func': vc_replacement_d3_153}


def vc_replacement_d3_154(vc_replacement_d2_154):
    feature = _clean(vc_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_154'] = {'inputs': ['vc_replacement_d2_154'], 'func': vc_replacement_d3_154}


def vc_replacement_d3_155(vc_replacement_d2_155):
    feature = _clean(vc_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_155'] = {'inputs': ['vc_replacement_d2_155'], 'func': vc_replacement_d3_155}


def vc_replacement_d3_156(vc_replacement_d2_156):
    feature = _clean(vc_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_156'] = {'inputs': ['vc_replacement_d2_156'], 'func': vc_replacement_d3_156}


def vc_replacement_d3_157(vc_replacement_d2_157):
    feature = _clean(vc_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_157'] = {'inputs': ['vc_replacement_d2_157'], 'func': vc_replacement_d3_157}


def vc_replacement_d3_158(vc_replacement_d2_158):
    feature = _clean(vc_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_158'] = {'inputs': ['vc_replacement_d2_158'], 'func': vc_replacement_d3_158}


def vc_replacement_d3_159(vc_replacement_d2_159):
    feature = _clean(vc_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_159'] = {'inputs': ['vc_replacement_d2_159'], 'func': vc_replacement_d3_159}


def vc_replacement_d3_160(vc_replacement_d2_160):
    feature = _clean(vc_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
VC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vc_replacement_d3_160'] = {'inputs': ['vc_replacement_d2_160'], 'func': vc_replacement_d3_160}


# Third-derivative extensions for repaired first-base features.
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def vcc_base_universe_d3_001_vcc_002_volume_zscore_10_002(vcc_base_universe_d2_001_vcc_002_volume_zscore_10_002):
    return _base_universe_d3(vcc_base_universe_d2_001_vcc_002_volume_zscore_10_002, 1)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_001_vcc_002_volume_zscore_10_002'] = {'inputs': ['vcc_base_universe_d2_001_vcc_002_volume_zscore_10_002'], 'func': vcc_base_universe_d3_001_vcc_002_volume_zscore_10_002}


def vcc_base_universe_d3_002_vcc_003_down_volume_share_21_003(vcc_base_universe_d2_002_vcc_003_down_volume_share_21_003):
    return _base_universe_d3(vcc_base_universe_d2_002_vcc_003_down_volume_share_21_003, 2)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_002_vcc_003_down_volume_share_21_003'] = {'inputs': ['vcc_base_universe_d2_002_vcc_003_down_volume_share_21_003'], 'func': vcc_base_universe_d3_002_vcc_003_down_volume_share_21_003}


def vcc_base_universe_d3_003_vcc_004_dollar_volume_shock_42_004(vcc_base_universe_d2_003_vcc_004_dollar_volume_shock_42_004):
    return _base_universe_d3(vcc_base_universe_d2_003_vcc_004_dollar_volume_shock_42_004, 3)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_003_vcc_004_dollar_volume_shock_42_004'] = {'inputs': ['vcc_base_universe_d2_003_vcc_004_dollar_volume_shock_42_004'], 'func': vcc_base_universe_d3_003_vcc_004_dollar_volume_shock_42_004}


def vcc_base_universe_d3_004_vcc_005_volume_trend_slope_63_005(vcc_base_universe_d2_004_vcc_005_volume_trend_slope_63_005):
    return _base_universe_d3(vcc_base_universe_d2_004_vcc_005_volume_trend_slope_63_005, 4)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_004_vcc_005_volume_trend_slope_63_005'] = {'inputs': ['vcc_base_universe_d2_004_vcc_005_volume_trend_slope_63_005'], 'func': vcc_base_universe_d3_004_vcc_005_volume_trend_slope_63_005}


def vcc_base_universe_d3_005_vcc_006_price_volume_divergence_84_006(vcc_base_universe_d2_005_vcc_006_price_volume_divergence_84_006):
    return _base_universe_d3(vcc_base_universe_d2_005_vcc_006_price_volume_divergence_84_006, 5)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_005_vcc_006_price_volume_divergence_84_006'] = {'inputs': ['vcc_base_universe_d2_005_vcc_006_price_volume_divergence_84_006'], 'func': vcc_base_universe_d3_005_vcc_006_price_volume_divergence_84_006}


def vcc_base_universe_d3_006_vcc_008_volume_zscore_189_008(vcc_base_universe_d2_006_vcc_008_volume_zscore_189_008):
    return _base_universe_d3(vcc_base_universe_d2_006_vcc_008_volume_zscore_189_008, 6)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_006_vcc_008_volume_zscore_189_008'] = {'inputs': ['vcc_base_universe_d2_006_vcc_008_volume_zscore_189_008'], 'func': vcc_base_universe_d3_006_vcc_008_volume_zscore_189_008}


def vcc_base_universe_d3_007_vcc_009_down_volume_share_252_009(vcc_base_universe_d2_007_vcc_009_down_volume_share_252_009):
    return _base_universe_d3(vcc_base_universe_d2_007_vcc_009_down_volume_share_252_009, 7)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_007_vcc_009_down_volume_share_252_009'] = {'inputs': ['vcc_base_universe_d2_007_vcc_009_down_volume_share_252_009'], 'func': vcc_base_universe_d3_007_vcc_009_down_volume_share_252_009}


def vcc_base_universe_d3_008_vcc_010_dollar_volume_shock_378_010(vcc_base_universe_d2_008_vcc_010_dollar_volume_shock_378_010):
    return _base_universe_d3(vcc_base_universe_d2_008_vcc_010_dollar_volume_shock_378_010, 8)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_008_vcc_010_dollar_volume_shock_378_010'] = {'inputs': ['vcc_base_universe_d2_008_vcc_010_dollar_volume_shock_378_010'], 'func': vcc_base_universe_d3_008_vcc_010_dollar_volume_shock_378_010}


def vcc_base_universe_d3_009_vcc_011_volume_trend_slope_504_011(vcc_base_universe_d2_009_vcc_011_volume_trend_slope_504_011):
    return _base_universe_d3(vcc_base_universe_d2_009_vcc_011_volume_trend_slope_504_011, 9)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_009_vcc_011_volume_trend_slope_504_011'] = {'inputs': ['vcc_base_universe_d2_009_vcc_011_volume_trend_slope_504_011'], 'func': vcc_base_universe_d3_009_vcc_011_volume_trend_slope_504_011}


def vcc_base_universe_d3_010_vcc_012_price_volume_divergence_756_012(vcc_base_universe_d2_010_vcc_012_price_volume_divergence_756_012):
    return _base_universe_d3(vcc_base_universe_d2_010_vcc_012_price_volume_divergence_756_012, 10)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_010_vcc_012_price_volume_divergence_756_012'] = {'inputs': ['vcc_base_universe_d2_010_vcc_012_price_volume_divergence_756_012'], 'func': vcc_base_universe_d3_010_vcc_012_price_volume_divergence_756_012}


def vcc_base_universe_d3_011_vcc_014_volume_zscore_1260_014(vcc_base_universe_d2_011_vcc_014_volume_zscore_1260_014):
    return _base_universe_d3(vcc_base_universe_d2_011_vcc_014_volume_zscore_1260_014, 11)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_011_vcc_014_volume_zscore_1260_014'] = {'inputs': ['vcc_base_universe_d2_011_vcc_014_volume_zscore_1260_014'], 'func': vcc_base_universe_d3_011_vcc_014_volume_zscore_1260_014}


def vcc_base_universe_d3_012_vcc_015_down_volume_share_1512_015(vcc_base_universe_d2_012_vcc_015_down_volume_share_1512_015):
    return _base_universe_d3(vcc_base_universe_d2_012_vcc_015_down_volume_share_1512_015, 12)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_012_vcc_015_down_volume_share_1512_015'] = {'inputs': ['vcc_base_universe_d2_012_vcc_015_down_volume_share_1512_015'], 'func': vcc_base_universe_d3_012_vcc_015_down_volume_share_1512_015}


def vcc_base_universe_d3_013_vcc_016_dollar_volume_shock_5_016(vcc_base_universe_d2_013_vcc_016_dollar_volume_shock_5_016):
    return _base_universe_d3(vcc_base_universe_d2_013_vcc_016_dollar_volume_shock_5_016, 13)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_013_vcc_016_dollar_volume_shock_5_016'] = {'inputs': ['vcc_base_universe_d2_013_vcc_016_dollar_volume_shock_5_016'], 'func': vcc_base_universe_d3_013_vcc_016_dollar_volume_shock_5_016}


def vcc_base_universe_d3_014_vcc_017_volume_trend_slope_10_017(vcc_base_universe_d2_014_vcc_017_volume_trend_slope_10_017):
    return _base_universe_d3(vcc_base_universe_d2_014_vcc_017_volume_trend_slope_10_017, 14)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_014_vcc_017_volume_trend_slope_10_017'] = {'inputs': ['vcc_base_universe_d2_014_vcc_017_volume_trend_slope_10_017'], 'func': vcc_base_universe_d3_014_vcc_017_volume_trend_slope_10_017}


def vcc_base_universe_d3_015_vcc_018_price_volume_divergence_21_018(vcc_base_universe_d2_015_vcc_018_price_volume_divergence_21_018):
    return _base_universe_d3(vcc_base_universe_d2_015_vcc_018_price_volume_divergence_21_018, 15)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_015_vcc_018_price_volume_divergence_21_018'] = {'inputs': ['vcc_base_universe_d2_015_vcc_018_price_volume_divergence_21_018'], 'func': vcc_base_universe_d3_015_vcc_018_price_volume_divergence_21_018}


def vcc_base_universe_d3_016_vcc_020_volume_zscore_63_020(vcc_base_universe_d2_016_vcc_020_volume_zscore_63_020):
    return _base_universe_d3(vcc_base_universe_d2_016_vcc_020_volume_zscore_63_020, 16)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_016_vcc_020_volume_zscore_63_020'] = {'inputs': ['vcc_base_universe_d2_016_vcc_020_volume_zscore_63_020'], 'func': vcc_base_universe_d3_016_vcc_020_volume_zscore_63_020}


def vcc_base_universe_d3_017_vcc_021_down_volume_share_84_021(vcc_base_universe_d2_017_vcc_021_down_volume_share_84_021):
    return _base_universe_d3(vcc_base_universe_d2_017_vcc_021_down_volume_share_84_021, 17)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_017_vcc_021_down_volume_share_84_021'] = {'inputs': ['vcc_base_universe_d2_017_vcc_021_down_volume_share_84_021'], 'func': vcc_base_universe_d3_017_vcc_021_down_volume_share_84_021}


def vcc_base_universe_d3_018_vcc_022_dollar_volume_shock_126_022(vcc_base_universe_d2_018_vcc_022_dollar_volume_shock_126_022):
    return _base_universe_d3(vcc_base_universe_d2_018_vcc_022_dollar_volume_shock_126_022, 18)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_018_vcc_022_dollar_volume_shock_126_022'] = {'inputs': ['vcc_base_universe_d2_018_vcc_022_dollar_volume_shock_126_022'], 'func': vcc_base_universe_d3_018_vcc_022_dollar_volume_shock_126_022}


def vcc_base_universe_d3_019_vcc_023_volume_trend_slope_189_023(vcc_base_universe_d2_019_vcc_023_volume_trend_slope_189_023):
    return _base_universe_d3(vcc_base_universe_d2_019_vcc_023_volume_trend_slope_189_023, 19)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_019_vcc_023_volume_trend_slope_189_023'] = {'inputs': ['vcc_base_universe_d2_019_vcc_023_volume_trend_slope_189_023'], 'func': vcc_base_universe_d3_019_vcc_023_volume_trend_slope_189_023}


def vcc_base_universe_d3_020_vcc_024_price_volume_divergence_252_024(vcc_base_universe_d2_020_vcc_024_price_volume_divergence_252_024):
    return _base_universe_d3(vcc_base_universe_d2_020_vcc_024_price_volume_divergence_252_024, 20)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_020_vcc_024_price_volume_divergence_252_024'] = {'inputs': ['vcc_base_universe_d2_020_vcc_024_price_volume_divergence_252_024'], 'func': vcc_base_universe_d3_020_vcc_024_price_volume_divergence_252_024}


def vcc_base_universe_d3_021_vcc_026_volume_zscore_504_026(vcc_base_universe_d2_021_vcc_026_volume_zscore_504_026):
    return _base_universe_d3(vcc_base_universe_d2_021_vcc_026_volume_zscore_504_026, 21)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_021_vcc_026_volume_zscore_504_026'] = {'inputs': ['vcc_base_universe_d2_021_vcc_026_volume_zscore_504_026'], 'func': vcc_base_universe_d3_021_vcc_026_volume_zscore_504_026}


def vcc_base_universe_d3_022_vcc_027_down_volume_share_756_027(vcc_base_universe_d2_022_vcc_027_down_volume_share_756_027):
    return _base_universe_d3(vcc_base_universe_d2_022_vcc_027_down_volume_share_756_027, 22)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_022_vcc_027_down_volume_share_756_027'] = {'inputs': ['vcc_base_universe_d2_022_vcc_027_down_volume_share_756_027'], 'func': vcc_base_universe_d3_022_vcc_027_down_volume_share_756_027}


def vcc_base_universe_d3_023_vcc_028_dollar_volume_shock_1008_028(vcc_base_universe_d2_023_vcc_028_dollar_volume_shock_1008_028):
    return _base_universe_d3(vcc_base_universe_d2_023_vcc_028_dollar_volume_shock_1008_028, 23)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_023_vcc_028_dollar_volume_shock_1008_028'] = {'inputs': ['vcc_base_universe_d2_023_vcc_028_dollar_volume_shock_1008_028'], 'func': vcc_base_universe_d3_023_vcc_028_dollar_volume_shock_1008_028}


def vcc_base_universe_d3_024_vcc_029_volume_trend_slope_1260_029(vcc_base_universe_d2_024_vcc_029_volume_trend_slope_1260_029):
    return _base_universe_d3(vcc_base_universe_d2_024_vcc_029_volume_trend_slope_1260_029, 24)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_024_vcc_029_volume_trend_slope_1260_029'] = {'inputs': ['vcc_base_universe_d2_024_vcc_029_volume_trend_slope_1260_029'], 'func': vcc_base_universe_d3_024_vcc_029_volume_trend_slope_1260_029}


def vcc_base_universe_d3_025_vcc_030_price_volume_divergence_1512_030(vcc_base_universe_d2_025_vcc_030_price_volume_divergence_1512_030):
    return _base_universe_d3(vcc_base_universe_d2_025_vcc_030_price_volume_divergence_1512_030, 25)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_025_vcc_030_price_volume_divergence_1512_030'] = {'inputs': ['vcc_base_universe_d2_025_vcc_030_price_volume_divergence_1512_030'], 'func': vcc_base_universe_d3_025_vcc_030_price_volume_divergence_1512_030}


def vcc_base_universe_d3_026_vcc_basefill_031(vcc_base_universe_d2_026_vcc_basefill_031):
    return _base_universe_d3(vcc_base_universe_d2_026_vcc_basefill_031, 26)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_026_vcc_basefill_031'] = {'inputs': ['vcc_base_universe_d2_026_vcc_basefill_031'], 'func': vcc_base_universe_d3_026_vcc_basefill_031}


def vcc_base_universe_d3_027_vcc_basefill_032(vcc_base_universe_d2_027_vcc_basefill_032):
    return _base_universe_d3(vcc_base_universe_d2_027_vcc_basefill_032, 27)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_027_vcc_basefill_032'] = {'inputs': ['vcc_base_universe_d2_027_vcc_basefill_032'], 'func': vcc_base_universe_d3_027_vcc_basefill_032}


def vcc_base_universe_d3_028_vcc_basefill_033(vcc_base_universe_d2_028_vcc_basefill_033):
    return _base_universe_d3(vcc_base_universe_d2_028_vcc_basefill_033, 28)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_028_vcc_basefill_033'] = {'inputs': ['vcc_base_universe_d2_028_vcc_basefill_033'], 'func': vcc_base_universe_d3_028_vcc_basefill_033}


def vcc_base_universe_d3_029_vcc_basefill_034(vcc_base_universe_d2_029_vcc_basefill_034):
    return _base_universe_d3(vcc_base_universe_d2_029_vcc_basefill_034, 29)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_029_vcc_basefill_034'] = {'inputs': ['vcc_base_universe_d2_029_vcc_basefill_034'], 'func': vcc_base_universe_d3_029_vcc_basefill_034}


def vcc_base_universe_d3_030_vcc_basefill_035(vcc_base_universe_d2_030_vcc_basefill_035):
    return _base_universe_d3(vcc_base_universe_d2_030_vcc_basefill_035, 30)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_030_vcc_basefill_035'] = {'inputs': ['vcc_base_universe_d2_030_vcc_basefill_035'], 'func': vcc_base_universe_d3_030_vcc_basefill_035}


def vcc_base_universe_d3_031_vcc_basefill_036(vcc_base_universe_d2_031_vcc_basefill_036):
    return _base_universe_d3(vcc_base_universe_d2_031_vcc_basefill_036, 31)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_031_vcc_basefill_036'] = {'inputs': ['vcc_base_universe_d2_031_vcc_basefill_036'], 'func': vcc_base_universe_d3_031_vcc_basefill_036}


def vcc_base_universe_d3_032_vcc_basefill_037(vcc_base_universe_d2_032_vcc_basefill_037):
    return _base_universe_d3(vcc_base_universe_d2_032_vcc_basefill_037, 32)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_032_vcc_basefill_037'] = {'inputs': ['vcc_base_universe_d2_032_vcc_basefill_037'], 'func': vcc_base_universe_d3_032_vcc_basefill_037}


def vcc_base_universe_d3_033_vcc_basefill_038(vcc_base_universe_d2_033_vcc_basefill_038):
    return _base_universe_d3(vcc_base_universe_d2_033_vcc_basefill_038, 33)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_033_vcc_basefill_038'] = {'inputs': ['vcc_base_universe_d2_033_vcc_basefill_038'], 'func': vcc_base_universe_d3_033_vcc_basefill_038}


def vcc_base_universe_d3_034_vcc_basefill_039(vcc_base_universe_d2_034_vcc_basefill_039):
    return _base_universe_d3(vcc_base_universe_d2_034_vcc_basefill_039, 34)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_034_vcc_basefill_039'] = {'inputs': ['vcc_base_universe_d2_034_vcc_basefill_039'], 'func': vcc_base_universe_d3_034_vcc_basefill_039}


def vcc_base_universe_d3_035_vcc_basefill_040(vcc_base_universe_d2_035_vcc_basefill_040):
    return _base_universe_d3(vcc_base_universe_d2_035_vcc_basefill_040, 35)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_035_vcc_basefill_040'] = {'inputs': ['vcc_base_universe_d2_035_vcc_basefill_040'], 'func': vcc_base_universe_d3_035_vcc_basefill_040}


def vcc_base_universe_d3_036_vcc_basefill_041(vcc_base_universe_d2_036_vcc_basefill_041):
    return _base_universe_d3(vcc_base_universe_d2_036_vcc_basefill_041, 36)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_036_vcc_basefill_041'] = {'inputs': ['vcc_base_universe_d2_036_vcc_basefill_041'], 'func': vcc_base_universe_d3_036_vcc_basefill_041}


def vcc_base_universe_d3_037_vcc_basefill_042(vcc_base_universe_d2_037_vcc_basefill_042):
    return _base_universe_d3(vcc_base_universe_d2_037_vcc_basefill_042, 37)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_037_vcc_basefill_042'] = {'inputs': ['vcc_base_universe_d2_037_vcc_basefill_042'], 'func': vcc_base_universe_d3_037_vcc_basefill_042}


def vcc_base_universe_d3_038_vcc_basefill_043(vcc_base_universe_d2_038_vcc_basefill_043):
    return _base_universe_d3(vcc_base_universe_d2_038_vcc_basefill_043, 38)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_038_vcc_basefill_043'] = {'inputs': ['vcc_base_universe_d2_038_vcc_basefill_043'], 'func': vcc_base_universe_d3_038_vcc_basefill_043}


def vcc_base_universe_d3_039_vcc_basefill_044(vcc_base_universe_d2_039_vcc_basefill_044):
    return _base_universe_d3(vcc_base_universe_d2_039_vcc_basefill_044, 39)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_039_vcc_basefill_044'] = {'inputs': ['vcc_base_universe_d2_039_vcc_basefill_044'], 'func': vcc_base_universe_d3_039_vcc_basefill_044}


def vcc_base_universe_d3_040_vcc_basefill_045(vcc_base_universe_d2_040_vcc_basefill_045):
    return _base_universe_d3(vcc_base_universe_d2_040_vcc_basefill_045, 40)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_040_vcc_basefill_045'] = {'inputs': ['vcc_base_universe_d2_040_vcc_basefill_045'], 'func': vcc_base_universe_d3_040_vcc_basefill_045}


def vcc_base_universe_d3_041_vcc_basefill_046(vcc_base_universe_d2_041_vcc_basefill_046):
    return _base_universe_d3(vcc_base_universe_d2_041_vcc_basefill_046, 41)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_041_vcc_basefill_046'] = {'inputs': ['vcc_base_universe_d2_041_vcc_basefill_046'], 'func': vcc_base_universe_d3_041_vcc_basefill_046}


def vcc_base_universe_d3_042_vcc_basefill_047(vcc_base_universe_d2_042_vcc_basefill_047):
    return _base_universe_d3(vcc_base_universe_d2_042_vcc_basefill_047, 42)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_042_vcc_basefill_047'] = {'inputs': ['vcc_base_universe_d2_042_vcc_basefill_047'], 'func': vcc_base_universe_d3_042_vcc_basefill_047}


def vcc_base_universe_d3_043_vcc_basefill_048(vcc_base_universe_d2_043_vcc_basefill_048):
    return _base_universe_d3(vcc_base_universe_d2_043_vcc_basefill_048, 43)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_043_vcc_basefill_048'] = {'inputs': ['vcc_base_universe_d2_043_vcc_basefill_048'], 'func': vcc_base_universe_d3_043_vcc_basefill_048}


def vcc_base_universe_d3_044_vcc_basefill_049(vcc_base_universe_d2_044_vcc_basefill_049):
    return _base_universe_d3(vcc_base_universe_d2_044_vcc_basefill_049, 44)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_044_vcc_basefill_049'] = {'inputs': ['vcc_base_universe_d2_044_vcc_basefill_049'], 'func': vcc_base_universe_d3_044_vcc_basefill_049}


def vcc_base_universe_d3_045_vcc_basefill_050(vcc_base_universe_d2_045_vcc_basefill_050):
    return _base_universe_d3(vcc_base_universe_d2_045_vcc_basefill_050, 45)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_045_vcc_basefill_050'] = {'inputs': ['vcc_base_universe_d2_045_vcc_basefill_050'], 'func': vcc_base_universe_d3_045_vcc_basefill_050}


def vcc_base_universe_d3_046_vcc_basefill_051(vcc_base_universe_d2_046_vcc_basefill_051):
    return _base_universe_d3(vcc_base_universe_d2_046_vcc_basefill_051, 46)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_046_vcc_basefill_051'] = {'inputs': ['vcc_base_universe_d2_046_vcc_basefill_051'], 'func': vcc_base_universe_d3_046_vcc_basefill_051}


def vcc_base_universe_d3_047_vcc_basefill_052(vcc_base_universe_d2_047_vcc_basefill_052):
    return _base_universe_d3(vcc_base_universe_d2_047_vcc_basefill_052, 47)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_047_vcc_basefill_052'] = {'inputs': ['vcc_base_universe_d2_047_vcc_basefill_052'], 'func': vcc_base_universe_d3_047_vcc_basefill_052}


def vcc_base_universe_d3_048_vcc_basefill_053(vcc_base_universe_d2_048_vcc_basefill_053):
    return _base_universe_d3(vcc_base_universe_d2_048_vcc_basefill_053, 48)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_048_vcc_basefill_053'] = {'inputs': ['vcc_base_universe_d2_048_vcc_basefill_053'], 'func': vcc_base_universe_d3_048_vcc_basefill_053}


def vcc_base_universe_d3_049_vcc_basefill_054(vcc_base_universe_d2_049_vcc_basefill_054):
    return _base_universe_d3(vcc_base_universe_d2_049_vcc_basefill_054, 49)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_049_vcc_basefill_054'] = {'inputs': ['vcc_base_universe_d2_049_vcc_basefill_054'], 'func': vcc_base_universe_d3_049_vcc_basefill_054}


def vcc_base_universe_d3_050_vcc_basefill_055(vcc_base_universe_d2_050_vcc_basefill_055):
    return _base_universe_d3(vcc_base_universe_d2_050_vcc_basefill_055, 50)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_050_vcc_basefill_055'] = {'inputs': ['vcc_base_universe_d2_050_vcc_basefill_055'], 'func': vcc_base_universe_d3_050_vcc_basefill_055}


def vcc_base_universe_d3_051_vcc_basefill_056(vcc_base_universe_d2_051_vcc_basefill_056):
    return _base_universe_d3(vcc_base_universe_d2_051_vcc_basefill_056, 51)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_051_vcc_basefill_056'] = {'inputs': ['vcc_base_universe_d2_051_vcc_basefill_056'], 'func': vcc_base_universe_d3_051_vcc_basefill_056}


def vcc_base_universe_d3_052_vcc_basefill_057(vcc_base_universe_d2_052_vcc_basefill_057):
    return _base_universe_d3(vcc_base_universe_d2_052_vcc_basefill_057, 52)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_052_vcc_basefill_057'] = {'inputs': ['vcc_base_universe_d2_052_vcc_basefill_057'], 'func': vcc_base_universe_d3_052_vcc_basefill_057}


def vcc_base_universe_d3_053_vcc_basefill_058(vcc_base_universe_d2_053_vcc_basefill_058):
    return _base_universe_d3(vcc_base_universe_d2_053_vcc_basefill_058, 53)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_053_vcc_basefill_058'] = {'inputs': ['vcc_base_universe_d2_053_vcc_basefill_058'], 'func': vcc_base_universe_d3_053_vcc_basefill_058}


def vcc_base_universe_d3_054_vcc_basefill_059(vcc_base_universe_d2_054_vcc_basefill_059):
    return _base_universe_d3(vcc_base_universe_d2_054_vcc_basefill_059, 54)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_054_vcc_basefill_059'] = {'inputs': ['vcc_base_universe_d2_054_vcc_basefill_059'], 'func': vcc_base_universe_d3_054_vcc_basefill_059}


def vcc_base_universe_d3_055_vcc_basefill_060(vcc_base_universe_d2_055_vcc_basefill_060):
    return _base_universe_d3(vcc_base_universe_d2_055_vcc_basefill_060, 55)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_055_vcc_basefill_060'] = {'inputs': ['vcc_base_universe_d2_055_vcc_basefill_060'], 'func': vcc_base_universe_d3_055_vcc_basefill_060}


def vcc_base_universe_d3_056_vcc_basefill_061(vcc_base_universe_d2_056_vcc_basefill_061):
    return _base_universe_d3(vcc_base_universe_d2_056_vcc_basefill_061, 56)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_056_vcc_basefill_061'] = {'inputs': ['vcc_base_universe_d2_056_vcc_basefill_061'], 'func': vcc_base_universe_d3_056_vcc_basefill_061}


def vcc_base_universe_d3_057_vcc_basefill_062(vcc_base_universe_d2_057_vcc_basefill_062):
    return _base_universe_d3(vcc_base_universe_d2_057_vcc_basefill_062, 57)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_057_vcc_basefill_062'] = {'inputs': ['vcc_base_universe_d2_057_vcc_basefill_062'], 'func': vcc_base_universe_d3_057_vcc_basefill_062}


def vcc_base_universe_d3_058_vcc_basefill_063(vcc_base_universe_d2_058_vcc_basefill_063):
    return _base_universe_d3(vcc_base_universe_d2_058_vcc_basefill_063, 58)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_058_vcc_basefill_063'] = {'inputs': ['vcc_base_universe_d2_058_vcc_basefill_063'], 'func': vcc_base_universe_d3_058_vcc_basefill_063}


def vcc_base_universe_d3_059_vcc_basefill_064(vcc_base_universe_d2_059_vcc_basefill_064):
    return _base_universe_d3(vcc_base_universe_d2_059_vcc_basefill_064, 59)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_059_vcc_basefill_064'] = {'inputs': ['vcc_base_universe_d2_059_vcc_basefill_064'], 'func': vcc_base_universe_d3_059_vcc_basefill_064}


def vcc_base_universe_d3_060_vcc_basefill_065(vcc_base_universe_d2_060_vcc_basefill_065):
    return _base_universe_d3(vcc_base_universe_d2_060_vcc_basefill_065, 60)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_060_vcc_basefill_065'] = {'inputs': ['vcc_base_universe_d2_060_vcc_basefill_065'], 'func': vcc_base_universe_d3_060_vcc_basefill_065}


def vcc_base_universe_d3_061_vcc_basefill_066(vcc_base_universe_d2_061_vcc_basefill_066):
    return _base_universe_d3(vcc_base_universe_d2_061_vcc_basefill_066, 61)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_061_vcc_basefill_066'] = {'inputs': ['vcc_base_universe_d2_061_vcc_basefill_066'], 'func': vcc_base_universe_d3_061_vcc_basefill_066}


def vcc_base_universe_d3_062_vcc_basefill_067(vcc_base_universe_d2_062_vcc_basefill_067):
    return _base_universe_d3(vcc_base_universe_d2_062_vcc_basefill_067, 62)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_062_vcc_basefill_067'] = {'inputs': ['vcc_base_universe_d2_062_vcc_basefill_067'], 'func': vcc_base_universe_d3_062_vcc_basefill_067}


def vcc_base_universe_d3_063_vcc_basefill_068(vcc_base_universe_d2_063_vcc_basefill_068):
    return _base_universe_d3(vcc_base_universe_d2_063_vcc_basefill_068, 63)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_063_vcc_basefill_068'] = {'inputs': ['vcc_base_universe_d2_063_vcc_basefill_068'], 'func': vcc_base_universe_d3_063_vcc_basefill_068}


def vcc_base_universe_d3_064_vcc_basefill_069(vcc_base_universe_d2_064_vcc_basefill_069):
    return _base_universe_d3(vcc_base_universe_d2_064_vcc_basefill_069, 64)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_064_vcc_basefill_069'] = {'inputs': ['vcc_base_universe_d2_064_vcc_basefill_069'], 'func': vcc_base_universe_d3_064_vcc_basefill_069}


def vcc_base_universe_d3_065_vcc_basefill_070(vcc_base_universe_d2_065_vcc_basefill_070):
    return _base_universe_d3(vcc_base_universe_d2_065_vcc_basefill_070, 65)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_065_vcc_basefill_070'] = {'inputs': ['vcc_base_universe_d2_065_vcc_basefill_070'], 'func': vcc_base_universe_d3_065_vcc_basefill_070}


def vcc_base_universe_d3_066_vcc_basefill_071(vcc_base_universe_d2_066_vcc_basefill_071):
    return _base_universe_d3(vcc_base_universe_d2_066_vcc_basefill_071, 66)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_066_vcc_basefill_071'] = {'inputs': ['vcc_base_universe_d2_066_vcc_basefill_071'], 'func': vcc_base_universe_d3_066_vcc_basefill_071}


def vcc_base_universe_d3_067_vcc_basefill_072(vcc_base_universe_d2_067_vcc_basefill_072):
    return _base_universe_d3(vcc_base_universe_d2_067_vcc_basefill_072, 67)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_067_vcc_basefill_072'] = {'inputs': ['vcc_base_universe_d2_067_vcc_basefill_072'], 'func': vcc_base_universe_d3_067_vcc_basefill_072}


def vcc_base_universe_d3_068_vcc_basefill_073(vcc_base_universe_d2_068_vcc_basefill_073):
    return _base_universe_d3(vcc_base_universe_d2_068_vcc_basefill_073, 68)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_068_vcc_basefill_073'] = {'inputs': ['vcc_base_universe_d2_068_vcc_basefill_073'], 'func': vcc_base_universe_d3_068_vcc_basefill_073}


def vcc_base_universe_d3_069_vcc_basefill_074(vcc_base_universe_d2_069_vcc_basefill_074):
    return _base_universe_d3(vcc_base_universe_d2_069_vcc_basefill_074, 69)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_069_vcc_basefill_074'] = {'inputs': ['vcc_base_universe_d2_069_vcc_basefill_074'], 'func': vcc_base_universe_d3_069_vcc_basefill_074}


def vcc_base_universe_d3_070_vcc_basefill_075(vcc_base_universe_d2_070_vcc_basefill_075):
    return _base_universe_d3(vcc_base_universe_d2_070_vcc_basefill_075, 70)
VCC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcc_base_universe_d3_070_vcc_basefill_075'] = {'inputs': ['vcc_base_universe_d2_070_vcc_basefill_075'], 'func': vcc_base_universe_d3_070_vcc_basefill_075}
