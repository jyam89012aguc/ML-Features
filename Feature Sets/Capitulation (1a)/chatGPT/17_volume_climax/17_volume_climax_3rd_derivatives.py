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



def vcx_176_vcx_001_volume_spike_ratio_5_001_accel_1(vcx_151_vcx_001_volume_spike_ratio_5_001_roc_1):
    feature = _s(vcx_151_vcx_001_volume_spike_ratio_5_001_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def vcx_177_vcx_007_volume_spike_ratio_126_007_accel_5(vcx_152_vcx_007_volume_spike_ratio_126_007_roc_5):
    feature = _s(vcx_152_vcx_007_volume_spike_ratio_126_007_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def vcx_178_vcx_013_volume_spike_ratio_1008_013_accel_42(vcx_153_vcx_013_volume_spike_ratio_1008_013_roc_42):
    feature = _s(vcx_153_vcx_013_volume_spike_ratio_1008_013_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def vcx_179_vcx_019_volume_spike_ratio_42_019_accel_126(vcx_154_vcx_019_volume_spike_ratio_42_019_roc_126):
    feature = _s(vcx_154_vcx_019_volume_spike_ratio_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def vcx_180_vcx_025_volume_spike_ratio_378_025_accel_378(vcx_155_vcx_025_volume_spike_ratio_378_025_roc_378):
    feature = _s(vcx_155_vcx_025_volume_spike_ratio_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















VOLUME_CLIMAX_REGISTRY_3RD_DERIVATIVES = {
    'vcx_176_vcx_001_volume_spike_ratio_5_001_accel_1': {'inputs': ['vcx_151_vcx_001_volume_spike_ratio_5_001_roc_1'], 'func': vcx_176_vcx_001_volume_spike_ratio_5_001_accel_1},
    'vcx_177_vcx_007_volume_spike_ratio_126_007_accel_5': {'inputs': ['vcx_152_vcx_007_volume_spike_ratio_126_007_roc_5'], 'func': vcx_177_vcx_007_volume_spike_ratio_126_007_accel_5},
    'vcx_178_vcx_013_volume_spike_ratio_1008_013_accel_42': {'inputs': ['vcx_153_vcx_013_volume_spike_ratio_1008_013_roc_42'], 'func': vcx_178_vcx_013_volume_spike_ratio_1008_013_accel_42},
    'vcx_179_vcx_019_volume_spike_ratio_42_019_accel_126': {'inputs': ['vcx_154_vcx_019_volume_spike_ratio_42_019_roc_126'], 'func': vcx_179_vcx_019_volume_spike_ratio_42_019_accel_126},
    'vcx_180_vcx_025_volume_spike_ratio_378_025_accel_378': {'inputs': ['vcx_155_vcx_025_volume_spike_ratio_378_025_roc_378'], 'func': vcx_180_vcx_025_volume_spike_ratio_378_025_accel_378},
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
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def vcx_base_universe_d3_001_vcx_002_volume_zscore_10_002(vcx_base_universe_d2_001_vcx_002_volume_zscore_10_002):
    return _base_universe_d3(vcx_base_universe_d2_001_vcx_002_volume_zscore_10_002, 1)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_001_vcx_002_volume_zscore_10_002'] = {'inputs': ['vcx_base_universe_d2_001_vcx_002_volume_zscore_10_002'], 'func': vcx_base_universe_d3_001_vcx_002_volume_zscore_10_002}


def vcx_base_universe_d3_002_vcx_003_down_volume_share_21_003(vcx_base_universe_d2_002_vcx_003_down_volume_share_21_003):
    return _base_universe_d3(vcx_base_universe_d2_002_vcx_003_down_volume_share_21_003, 2)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_002_vcx_003_down_volume_share_21_003'] = {'inputs': ['vcx_base_universe_d2_002_vcx_003_down_volume_share_21_003'], 'func': vcx_base_universe_d3_002_vcx_003_down_volume_share_21_003}


def vcx_base_universe_d3_003_vcx_004_dollar_volume_shock_42_004(vcx_base_universe_d2_003_vcx_004_dollar_volume_shock_42_004):
    return _base_universe_d3(vcx_base_universe_d2_003_vcx_004_dollar_volume_shock_42_004, 3)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_003_vcx_004_dollar_volume_shock_42_004'] = {'inputs': ['vcx_base_universe_d2_003_vcx_004_dollar_volume_shock_42_004'], 'func': vcx_base_universe_d3_003_vcx_004_dollar_volume_shock_42_004}


def vcx_base_universe_d3_004_vcx_005_volume_trend_slope_63_005(vcx_base_universe_d2_004_vcx_005_volume_trend_slope_63_005):
    return _base_universe_d3(vcx_base_universe_d2_004_vcx_005_volume_trend_slope_63_005, 4)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_004_vcx_005_volume_trend_slope_63_005'] = {'inputs': ['vcx_base_universe_d2_004_vcx_005_volume_trend_slope_63_005'], 'func': vcx_base_universe_d3_004_vcx_005_volume_trend_slope_63_005}


def vcx_base_universe_d3_005_vcx_006_price_volume_divergence_84_006(vcx_base_universe_d2_005_vcx_006_price_volume_divergence_84_006):
    return _base_universe_d3(vcx_base_universe_d2_005_vcx_006_price_volume_divergence_84_006, 5)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_005_vcx_006_price_volume_divergence_84_006'] = {'inputs': ['vcx_base_universe_d2_005_vcx_006_price_volume_divergence_84_006'], 'func': vcx_base_universe_d3_005_vcx_006_price_volume_divergence_84_006}


def vcx_base_universe_d3_006_vcx_008_volume_zscore_189_008(vcx_base_universe_d2_006_vcx_008_volume_zscore_189_008):
    return _base_universe_d3(vcx_base_universe_d2_006_vcx_008_volume_zscore_189_008, 6)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_006_vcx_008_volume_zscore_189_008'] = {'inputs': ['vcx_base_universe_d2_006_vcx_008_volume_zscore_189_008'], 'func': vcx_base_universe_d3_006_vcx_008_volume_zscore_189_008}


def vcx_base_universe_d3_007_vcx_009_down_volume_share_252_009(vcx_base_universe_d2_007_vcx_009_down_volume_share_252_009):
    return _base_universe_d3(vcx_base_universe_d2_007_vcx_009_down_volume_share_252_009, 7)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_007_vcx_009_down_volume_share_252_009'] = {'inputs': ['vcx_base_universe_d2_007_vcx_009_down_volume_share_252_009'], 'func': vcx_base_universe_d3_007_vcx_009_down_volume_share_252_009}


def vcx_base_universe_d3_008_vcx_010_dollar_volume_shock_378_010(vcx_base_universe_d2_008_vcx_010_dollar_volume_shock_378_010):
    return _base_universe_d3(vcx_base_universe_d2_008_vcx_010_dollar_volume_shock_378_010, 8)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_008_vcx_010_dollar_volume_shock_378_010'] = {'inputs': ['vcx_base_universe_d2_008_vcx_010_dollar_volume_shock_378_010'], 'func': vcx_base_universe_d3_008_vcx_010_dollar_volume_shock_378_010}


def vcx_base_universe_d3_009_vcx_011_volume_trend_slope_504_011(vcx_base_universe_d2_009_vcx_011_volume_trend_slope_504_011):
    return _base_universe_d3(vcx_base_universe_d2_009_vcx_011_volume_trend_slope_504_011, 9)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_009_vcx_011_volume_trend_slope_504_011'] = {'inputs': ['vcx_base_universe_d2_009_vcx_011_volume_trend_slope_504_011'], 'func': vcx_base_universe_d3_009_vcx_011_volume_trend_slope_504_011}


def vcx_base_universe_d3_010_vcx_012_price_volume_divergence_756_012(vcx_base_universe_d2_010_vcx_012_price_volume_divergence_756_012):
    return _base_universe_d3(vcx_base_universe_d2_010_vcx_012_price_volume_divergence_756_012, 10)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_010_vcx_012_price_volume_divergence_756_012'] = {'inputs': ['vcx_base_universe_d2_010_vcx_012_price_volume_divergence_756_012'], 'func': vcx_base_universe_d3_010_vcx_012_price_volume_divergence_756_012}


def vcx_base_universe_d3_011_vcx_014_volume_zscore_1260_014(vcx_base_universe_d2_011_vcx_014_volume_zscore_1260_014):
    return _base_universe_d3(vcx_base_universe_d2_011_vcx_014_volume_zscore_1260_014, 11)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_011_vcx_014_volume_zscore_1260_014'] = {'inputs': ['vcx_base_universe_d2_011_vcx_014_volume_zscore_1260_014'], 'func': vcx_base_universe_d3_011_vcx_014_volume_zscore_1260_014}


def vcx_base_universe_d3_012_vcx_015_down_volume_share_1512_015(vcx_base_universe_d2_012_vcx_015_down_volume_share_1512_015):
    return _base_universe_d3(vcx_base_universe_d2_012_vcx_015_down_volume_share_1512_015, 12)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_012_vcx_015_down_volume_share_1512_015'] = {'inputs': ['vcx_base_universe_d2_012_vcx_015_down_volume_share_1512_015'], 'func': vcx_base_universe_d3_012_vcx_015_down_volume_share_1512_015}


def vcx_base_universe_d3_013_vcx_016_dollar_volume_shock_5_016(vcx_base_universe_d2_013_vcx_016_dollar_volume_shock_5_016):
    return _base_universe_d3(vcx_base_universe_d2_013_vcx_016_dollar_volume_shock_5_016, 13)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_013_vcx_016_dollar_volume_shock_5_016'] = {'inputs': ['vcx_base_universe_d2_013_vcx_016_dollar_volume_shock_5_016'], 'func': vcx_base_universe_d3_013_vcx_016_dollar_volume_shock_5_016}


def vcx_base_universe_d3_014_vcx_017_volume_trend_slope_10_017(vcx_base_universe_d2_014_vcx_017_volume_trend_slope_10_017):
    return _base_universe_d3(vcx_base_universe_d2_014_vcx_017_volume_trend_slope_10_017, 14)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_014_vcx_017_volume_trend_slope_10_017'] = {'inputs': ['vcx_base_universe_d2_014_vcx_017_volume_trend_slope_10_017'], 'func': vcx_base_universe_d3_014_vcx_017_volume_trend_slope_10_017}


def vcx_base_universe_d3_015_vcx_018_price_volume_divergence_21_018(vcx_base_universe_d2_015_vcx_018_price_volume_divergence_21_018):
    return _base_universe_d3(vcx_base_universe_d2_015_vcx_018_price_volume_divergence_21_018, 15)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_015_vcx_018_price_volume_divergence_21_018'] = {'inputs': ['vcx_base_universe_d2_015_vcx_018_price_volume_divergence_21_018'], 'func': vcx_base_universe_d3_015_vcx_018_price_volume_divergence_21_018}


def vcx_base_universe_d3_016_vcx_020_volume_zscore_63_020(vcx_base_universe_d2_016_vcx_020_volume_zscore_63_020):
    return _base_universe_d3(vcx_base_universe_d2_016_vcx_020_volume_zscore_63_020, 16)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_016_vcx_020_volume_zscore_63_020'] = {'inputs': ['vcx_base_universe_d2_016_vcx_020_volume_zscore_63_020'], 'func': vcx_base_universe_d3_016_vcx_020_volume_zscore_63_020}


def vcx_base_universe_d3_017_vcx_021_down_volume_share_84_021(vcx_base_universe_d2_017_vcx_021_down_volume_share_84_021):
    return _base_universe_d3(vcx_base_universe_d2_017_vcx_021_down_volume_share_84_021, 17)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_017_vcx_021_down_volume_share_84_021'] = {'inputs': ['vcx_base_universe_d2_017_vcx_021_down_volume_share_84_021'], 'func': vcx_base_universe_d3_017_vcx_021_down_volume_share_84_021}


def vcx_base_universe_d3_018_vcx_022_dollar_volume_shock_126_022(vcx_base_universe_d2_018_vcx_022_dollar_volume_shock_126_022):
    return _base_universe_d3(vcx_base_universe_d2_018_vcx_022_dollar_volume_shock_126_022, 18)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_018_vcx_022_dollar_volume_shock_126_022'] = {'inputs': ['vcx_base_universe_d2_018_vcx_022_dollar_volume_shock_126_022'], 'func': vcx_base_universe_d3_018_vcx_022_dollar_volume_shock_126_022}


def vcx_base_universe_d3_019_vcx_023_volume_trend_slope_189_023(vcx_base_universe_d2_019_vcx_023_volume_trend_slope_189_023):
    return _base_universe_d3(vcx_base_universe_d2_019_vcx_023_volume_trend_slope_189_023, 19)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_019_vcx_023_volume_trend_slope_189_023'] = {'inputs': ['vcx_base_universe_d2_019_vcx_023_volume_trend_slope_189_023'], 'func': vcx_base_universe_d3_019_vcx_023_volume_trend_slope_189_023}


def vcx_base_universe_d3_020_vcx_024_price_volume_divergence_252_024(vcx_base_universe_d2_020_vcx_024_price_volume_divergence_252_024):
    return _base_universe_d3(vcx_base_universe_d2_020_vcx_024_price_volume_divergence_252_024, 20)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_020_vcx_024_price_volume_divergence_252_024'] = {'inputs': ['vcx_base_universe_d2_020_vcx_024_price_volume_divergence_252_024'], 'func': vcx_base_universe_d3_020_vcx_024_price_volume_divergence_252_024}


def vcx_base_universe_d3_021_vcx_026_volume_zscore_504_026(vcx_base_universe_d2_021_vcx_026_volume_zscore_504_026):
    return _base_universe_d3(vcx_base_universe_d2_021_vcx_026_volume_zscore_504_026, 21)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_021_vcx_026_volume_zscore_504_026'] = {'inputs': ['vcx_base_universe_d2_021_vcx_026_volume_zscore_504_026'], 'func': vcx_base_universe_d3_021_vcx_026_volume_zscore_504_026}


def vcx_base_universe_d3_022_vcx_027_down_volume_share_756_027(vcx_base_universe_d2_022_vcx_027_down_volume_share_756_027):
    return _base_universe_d3(vcx_base_universe_d2_022_vcx_027_down_volume_share_756_027, 22)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_022_vcx_027_down_volume_share_756_027'] = {'inputs': ['vcx_base_universe_d2_022_vcx_027_down_volume_share_756_027'], 'func': vcx_base_universe_d3_022_vcx_027_down_volume_share_756_027}


def vcx_base_universe_d3_023_vcx_028_dollar_volume_shock_1008_028(vcx_base_universe_d2_023_vcx_028_dollar_volume_shock_1008_028):
    return _base_universe_d3(vcx_base_universe_d2_023_vcx_028_dollar_volume_shock_1008_028, 23)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_023_vcx_028_dollar_volume_shock_1008_028'] = {'inputs': ['vcx_base_universe_d2_023_vcx_028_dollar_volume_shock_1008_028'], 'func': vcx_base_universe_d3_023_vcx_028_dollar_volume_shock_1008_028}


def vcx_base_universe_d3_024_vcx_029_volume_trend_slope_1260_029(vcx_base_universe_d2_024_vcx_029_volume_trend_slope_1260_029):
    return _base_universe_d3(vcx_base_universe_d2_024_vcx_029_volume_trend_slope_1260_029, 24)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_024_vcx_029_volume_trend_slope_1260_029'] = {'inputs': ['vcx_base_universe_d2_024_vcx_029_volume_trend_slope_1260_029'], 'func': vcx_base_universe_d3_024_vcx_029_volume_trend_slope_1260_029}


def vcx_base_universe_d3_025_vcx_030_price_volume_divergence_1512_030(vcx_base_universe_d2_025_vcx_030_price_volume_divergence_1512_030):
    return _base_universe_d3(vcx_base_universe_d2_025_vcx_030_price_volume_divergence_1512_030, 25)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_025_vcx_030_price_volume_divergence_1512_030'] = {'inputs': ['vcx_base_universe_d2_025_vcx_030_price_volume_divergence_1512_030'], 'func': vcx_base_universe_d3_025_vcx_030_price_volume_divergence_1512_030}


def vcx_base_universe_d3_026_vcx_basefill_031(vcx_base_universe_d2_026_vcx_basefill_031):
    return _base_universe_d3(vcx_base_universe_d2_026_vcx_basefill_031, 26)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_026_vcx_basefill_031'] = {'inputs': ['vcx_base_universe_d2_026_vcx_basefill_031'], 'func': vcx_base_universe_d3_026_vcx_basefill_031}


def vcx_base_universe_d3_027_vcx_basefill_032(vcx_base_universe_d2_027_vcx_basefill_032):
    return _base_universe_d3(vcx_base_universe_d2_027_vcx_basefill_032, 27)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_027_vcx_basefill_032'] = {'inputs': ['vcx_base_universe_d2_027_vcx_basefill_032'], 'func': vcx_base_universe_d3_027_vcx_basefill_032}


def vcx_base_universe_d3_028_vcx_basefill_033(vcx_base_universe_d2_028_vcx_basefill_033):
    return _base_universe_d3(vcx_base_universe_d2_028_vcx_basefill_033, 28)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_028_vcx_basefill_033'] = {'inputs': ['vcx_base_universe_d2_028_vcx_basefill_033'], 'func': vcx_base_universe_d3_028_vcx_basefill_033}


def vcx_base_universe_d3_029_vcx_basefill_034(vcx_base_universe_d2_029_vcx_basefill_034):
    return _base_universe_d3(vcx_base_universe_d2_029_vcx_basefill_034, 29)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_029_vcx_basefill_034'] = {'inputs': ['vcx_base_universe_d2_029_vcx_basefill_034'], 'func': vcx_base_universe_d3_029_vcx_basefill_034}


def vcx_base_universe_d3_030_vcx_basefill_035(vcx_base_universe_d2_030_vcx_basefill_035):
    return _base_universe_d3(vcx_base_universe_d2_030_vcx_basefill_035, 30)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_030_vcx_basefill_035'] = {'inputs': ['vcx_base_universe_d2_030_vcx_basefill_035'], 'func': vcx_base_universe_d3_030_vcx_basefill_035}


def vcx_base_universe_d3_031_vcx_basefill_036(vcx_base_universe_d2_031_vcx_basefill_036):
    return _base_universe_d3(vcx_base_universe_d2_031_vcx_basefill_036, 31)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_031_vcx_basefill_036'] = {'inputs': ['vcx_base_universe_d2_031_vcx_basefill_036'], 'func': vcx_base_universe_d3_031_vcx_basefill_036}


def vcx_base_universe_d3_032_vcx_basefill_037(vcx_base_universe_d2_032_vcx_basefill_037):
    return _base_universe_d3(vcx_base_universe_d2_032_vcx_basefill_037, 32)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_032_vcx_basefill_037'] = {'inputs': ['vcx_base_universe_d2_032_vcx_basefill_037'], 'func': vcx_base_universe_d3_032_vcx_basefill_037}


def vcx_base_universe_d3_033_vcx_basefill_038(vcx_base_universe_d2_033_vcx_basefill_038):
    return _base_universe_d3(vcx_base_universe_d2_033_vcx_basefill_038, 33)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_033_vcx_basefill_038'] = {'inputs': ['vcx_base_universe_d2_033_vcx_basefill_038'], 'func': vcx_base_universe_d3_033_vcx_basefill_038}


def vcx_base_universe_d3_034_vcx_basefill_039(vcx_base_universe_d2_034_vcx_basefill_039):
    return _base_universe_d3(vcx_base_universe_d2_034_vcx_basefill_039, 34)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_034_vcx_basefill_039'] = {'inputs': ['vcx_base_universe_d2_034_vcx_basefill_039'], 'func': vcx_base_universe_d3_034_vcx_basefill_039}


def vcx_base_universe_d3_035_vcx_basefill_040(vcx_base_universe_d2_035_vcx_basefill_040):
    return _base_universe_d3(vcx_base_universe_d2_035_vcx_basefill_040, 35)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_035_vcx_basefill_040'] = {'inputs': ['vcx_base_universe_d2_035_vcx_basefill_040'], 'func': vcx_base_universe_d3_035_vcx_basefill_040}


def vcx_base_universe_d3_036_vcx_basefill_041(vcx_base_universe_d2_036_vcx_basefill_041):
    return _base_universe_d3(vcx_base_universe_d2_036_vcx_basefill_041, 36)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_036_vcx_basefill_041'] = {'inputs': ['vcx_base_universe_d2_036_vcx_basefill_041'], 'func': vcx_base_universe_d3_036_vcx_basefill_041}


def vcx_base_universe_d3_037_vcx_basefill_042(vcx_base_universe_d2_037_vcx_basefill_042):
    return _base_universe_d3(vcx_base_universe_d2_037_vcx_basefill_042, 37)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_037_vcx_basefill_042'] = {'inputs': ['vcx_base_universe_d2_037_vcx_basefill_042'], 'func': vcx_base_universe_d3_037_vcx_basefill_042}


def vcx_base_universe_d3_038_vcx_basefill_043(vcx_base_universe_d2_038_vcx_basefill_043):
    return _base_universe_d3(vcx_base_universe_d2_038_vcx_basefill_043, 38)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_038_vcx_basefill_043'] = {'inputs': ['vcx_base_universe_d2_038_vcx_basefill_043'], 'func': vcx_base_universe_d3_038_vcx_basefill_043}


def vcx_base_universe_d3_039_vcx_basefill_044(vcx_base_universe_d2_039_vcx_basefill_044):
    return _base_universe_d3(vcx_base_universe_d2_039_vcx_basefill_044, 39)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_039_vcx_basefill_044'] = {'inputs': ['vcx_base_universe_d2_039_vcx_basefill_044'], 'func': vcx_base_universe_d3_039_vcx_basefill_044}


def vcx_base_universe_d3_040_vcx_basefill_045(vcx_base_universe_d2_040_vcx_basefill_045):
    return _base_universe_d3(vcx_base_universe_d2_040_vcx_basefill_045, 40)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_040_vcx_basefill_045'] = {'inputs': ['vcx_base_universe_d2_040_vcx_basefill_045'], 'func': vcx_base_universe_d3_040_vcx_basefill_045}


def vcx_base_universe_d3_041_vcx_basefill_046(vcx_base_universe_d2_041_vcx_basefill_046):
    return _base_universe_d3(vcx_base_universe_d2_041_vcx_basefill_046, 41)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_041_vcx_basefill_046'] = {'inputs': ['vcx_base_universe_d2_041_vcx_basefill_046'], 'func': vcx_base_universe_d3_041_vcx_basefill_046}


def vcx_base_universe_d3_042_vcx_basefill_047(vcx_base_universe_d2_042_vcx_basefill_047):
    return _base_universe_d3(vcx_base_universe_d2_042_vcx_basefill_047, 42)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_042_vcx_basefill_047'] = {'inputs': ['vcx_base_universe_d2_042_vcx_basefill_047'], 'func': vcx_base_universe_d3_042_vcx_basefill_047}


def vcx_base_universe_d3_043_vcx_basefill_048(vcx_base_universe_d2_043_vcx_basefill_048):
    return _base_universe_d3(vcx_base_universe_d2_043_vcx_basefill_048, 43)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_043_vcx_basefill_048'] = {'inputs': ['vcx_base_universe_d2_043_vcx_basefill_048'], 'func': vcx_base_universe_d3_043_vcx_basefill_048}


def vcx_base_universe_d3_044_vcx_basefill_049(vcx_base_universe_d2_044_vcx_basefill_049):
    return _base_universe_d3(vcx_base_universe_d2_044_vcx_basefill_049, 44)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_044_vcx_basefill_049'] = {'inputs': ['vcx_base_universe_d2_044_vcx_basefill_049'], 'func': vcx_base_universe_d3_044_vcx_basefill_049}


def vcx_base_universe_d3_045_vcx_basefill_050(vcx_base_universe_d2_045_vcx_basefill_050):
    return _base_universe_d3(vcx_base_universe_d2_045_vcx_basefill_050, 45)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_045_vcx_basefill_050'] = {'inputs': ['vcx_base_universe_d2_045_vcx_basefill_050'], 'func': vcx_base_universe_d3_045_vcx_basefill_050}


def vcx_base_universe_d3_046_vcx_basefill_051(vcx_base_universe_d2_046_vcx_basefill_051):
    return _base_universe_d3(vcx_base_universe_d2_046_vcx_basefill_051, 46)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_046_vcx_basefill_051'] = {'inputs': ['vcx_base_universe_d2_046_vcx_basefill_051'], 'func': vcx_base_universe_d3_046_vcx_basefill_051}


def vcx_base_universe_d3_047_vcx_basefill_052(vcx_base_universe_d2_047_vcx_basefill_052):
    return _base_universe_d3(vcx_base_universe_d2_047_vcx_basefill_052, 47)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_047_vcx_basefill_052'] = {'inputs': ['vcx_base_universe_d2_047_vcx_basefill_052'], 'func': vcx_base_universe_d3_047_vcx_basefill_052}


def vcx_base_universe_d3_048_vcx_basefill_053(vcx_base_universe_d2_048_vcx_basefill_053):
    return _base_universe_d3(vcx_base_universe_d2_048_vcx_basefill_053, 48)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_048_vcx_basefill_053'] = {'inputs': ['vcx_base_universe_d2_048_vcx_basefill_053'], 'func': vcx_base_universe_d3_048_vcx_basefill_053}


def vcx_base_universe_d3_049_vcx_basefill_054(vcx_base_universe_d2_049_vcx_basefill_054):
    return _base_universe_d3(vcx_base_universe_d2_049_vcx_basefill_054, 49)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_049_vcx_basefill_054'] = {'inputs': ['vcx_base_universe_d2_049_vcx_basefill_054'], 'func': vcx_base_universe_d3_049_vcx_basefill_054}


def vcx_base_universe_d3_050_vcx_basefill_055(vcx_base_universe_d2_050_vcx_basefill_055):
    return _base_universe_d3(vcx_base_universe_d2_050_vcx_basefill_055, 50)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_050_vcx_basefill_055'] = {'inputs': ['vcx_base_universe_d2_050_vcx_basefill_055'], 'func': vcx_base_universe_d3_050_vcx_basefill_055}


def vcx_base_universe_d3_051_vcx_basefill_056(vcx_base_universe_d2_051_vcx_basefill_056):
    return _base_universe_d3(vcx_base_universe_d2_051_vcx_basefill_056, 51)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_051_vcx_basefill_056'] = {'inputs': ['vcx_base_universe_d2_051_vcx_basefill_056'], 'func': vcx_base_universe_d3_051_vcx_basefill_056}


def vcx_base_universe_d3_052_vcx_basefill_057(vcx_base_universe_d2_052_vcx_basefill_057):
    return _base_universe_d3(vcx_base_universe_d2_052_vcx_basefill_057, 52)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_052_vcx_basefill_057'] = {'inputs': ['vcx_base_universe_d2_052_vcx_basefill_057'], 'func': vcx_base_universe_d3_052_vcx_basefill_057}


def vcx_base_universe_d3_053_vcx_basefill_058(vcx_base_universe_d2_053_vcx_basefill_058):
    return _base_universe_d3(vcx_base_universe_d2_053_vcx_basefill_058, 53)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_053_vcx_basefill_058'] = {'inputs': ['vcx_base_universe_d2_053_vcx_basefill_058'], 'func': vcx_base_universe_d3_053_vcx_basefill_058}


def vcx_base_universe_d3_054_vcx_basefill_059(vcx_base_universe_d2_054_vcx_basefill_059):
    return _base_universe_d3(vcx_base_universe_d2_054_vcx_basefill_059, 54)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_054_vcx_basefill_059'] = {'inputs': ['vcx_base_universe_d2_054_vcx_basefill_059'], 'func': vcx_base_universe_d3_054_vcx_basefill_059}


def vcx_base_universe_d3_055_vcx_basefill_060(vcx_base_universe_d2_055_vcx_basefill_060):
    return _base_universe_d3(vcx_base_universe_d2_055_vcx_basefill_060, 55)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_055_vcx_basefill_060'] = {'inputs': ['vcx_base_universe_d2_055_vcx_basefill_060'], 'func': vcx_base_universe_d3_055_vcx_basefill_060}


def vcx_base_universe_d3_056_vcx_basefill_061(vcx_base_universe_d2_056_vcx_basefill_061):
    return _base_universe_d3(vcx_base_universe_d2_056_vcx_basefill_061, 56)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_056_vcx_basefill_061'] = {'inputs': ['vcx_base_universe_d2_056_vcx_basefill_061'], 'func': vcx_base_universe_d3_056_vcx_basefill_061}


def vcx_base_universe_d3_057_vcx_basefill_062(vcx_base_universe_d2_057_vcx_basefill_062):
    return _base_universe_d3(vcx_base_universe_d2_057_vcx_basefill_062, 57)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_057_vcx_basefill_062'] = {'inputs': ['vcx_base_universe_d2_057_vcx_basefill_062'], 'func': vcx_base_universe_d3_057_vcx_basefill_062}


def vcx_base_universe_d3_058_vcx_basefill_063(vcx_base_universe_d2_058_vcx_basefill_063):
    return _base_universe_d3(vcx_base_universe_d2_058_vcx_basefill_063, 58)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_058_vcx_basefill_063'] = {'inputs': ['vcx_base_universe_d2_058_vcx_basefill_063'], 'func': vcx_base_universe_d3_058_vcx_basefill_063}


def vcx_base_universe_d3_059_vcx_basefill_064(vcx_base_universe_d2_059_vcx_basefill_064):
    return _base_universe_d3(vcx_base_universe_d2_059_vcx_basefill_064, 59)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_059_vcx_basefill_064'] = {'inputs': ['vcx_base_universe_d2_059_vcx_basefill_064'], 'func': vcx_base_universe_d3_059_vcx_basefill_064}


def vcx_base_universe_d3_060_vcx_basefill_065(vcx_base_universe_d2_060_vcx_basefill_065):
    return _base_universe_d3(vcx_base_universe_d2_060_vcx_basefill_065, 60)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_060_vcx_basefill_065'] = {'inputs': ['vcx_base_universe_d2_060_vcx_basefill_065'], 'func': vcx_base_universe_d3_060_vcx_basefill_065}


def vcx_base_universe_d3_061_vcx_basefill_066(vcx_base_universe_d2_061_vcx_basefill_066):
    return _base_universe_d3(vcx_base_universe_d2_061_vcx_basefill_066, 61)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_061_vcx_basefill_066'] = {'inputs': ['vcx_base_universe_d2_061_vcx_basefill_066'], 'func': vcx_base_universe_d3_061_vcx_basefill_066}


def vcx_base_universe_d3_062_vcx_basefill_067(vcx_base_universe_d2_062_vcx_basefill_067):
    return _base_universe_d3(vcx_base_universe_d2_062_vcx_basefill_067, 62)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_062_vcx_basefill_067'] = {'inputs': ['vcx_base_universe_d2_062_vcx_basefill_067'], 'func': vcx_base_universe_d3_062_vcx_basefill_067}


def vcx_base_universe_d3_063_vcx_basefill_068(vcx_base_universe_d2_063_vcx_basefill_068):
    return _base_universe_d3(vcx_base_universe_d2_063_vcx_basefill_068, 63)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_063_vcx_basefill_068'] = {'inputs': ['vcx_base_universe_d2_063_vcx_basefill_068'], 'func': vcx_base_universe_d3_063_vcx_basefill_068}


def vcx_base_universe_d3_064_vcx_basefill_069(vcx_base_universe_d2_064_vcx_basefill_069):
    return _base_universe_d3(vcx_base_universe_d2_064_vcx_basefill_069, 64)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_064_vcx_basefill_069'] = {'inputs': ['vcx_base_universe_d2_064_vcx_basefill_069'], 'func': vcx_base_universe_d3_064_vcx_basefill_069}


def vcx_base_universe_d3_065_vcx_basefill_070(vcx_base_universe_d2_065_vcx_basefill_070):
    return _base_universe_d3(vcx_base_universe_d2_065_vcx_basefill_070, 65)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_065_vcx_basefill_070'] = {'inputs': ['vcx_base_universe_d2_065_vcx_basefill_070'], 'func': vcx_base_universe_d3_065_vcx_basefill_070}


def vcx_base_universe_d3_066_vcx_basefill_071(vcx_base_universe_d2_066_vcx_basefill_071):
    return _base_universe_d3(vcx_base_universe_d2_066_vcx_basefill_071, 66)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_066_vcx_basefill_071'] = {'inputs': ['vcx_base_universe_d2_066_vcx_basefill_071'], 'func': vcx_base_universe_d3_066_vcx_basefill_071}


def vcx_base_universe_d3_067_vcx_basefill_072(vcx_base_universe_d2_067_vcx_basefill_072):
    return _base_universe_d3(vcx_base_universe_d2_067_vcx_basefill_072, 67)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_067_vcx_basefill_072'] = {'inputs': ['vcx_base_universe_d2_067_vcx_basefill_072'], 'func': vcx_base_universe_d3_067_vcx_basefill_072}


def vcx_base_universe_d3_068_vcx_basefill_073(vcx_base_universe_d2_068_vcx_basefill_073):
    return _base_universe_d3(vcx_base_universe_d2_068_vcx_basefill_073, 68)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_068_vcx_basefill_073'] = {'inputs': ['vcx_base_universe_d2_068_vcx_basefill_073'], 'func': vcx_base_universe_d3_068_vcx_basefill_073}


def vcx_base_universe_d3_069_vcx_basefill_074(vcx_base_universe_d2_069_vcx_basefill_074):
    return _base_universe_d3(vcx_base_universe_d2_069_vcx_basefill_074, 69)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_069_vcx_basefill_074'] = {'inputs': ['vcx_base_universe_d2_069_vcx_basefill_074'], 'func': vcx_base_universe_d3_069_vcx_basefill_074}


def vcx_base_universe_d3_070_vcx_basefill_075(vcx_base_universe_d2_070_vcx_basefill_075):
    return _base_universe_d3(vcx_base_universe_d2_070_vcx_basefill_075, 70)
VCX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vcx_base_universe_d3_070_vcx_basefill_075'] = {'inputs': ['vcx_base_universe_d2_070_vcx_basefill_075'], 'func': vcx_base_universe_d3_070_vcx_basefill_075}
