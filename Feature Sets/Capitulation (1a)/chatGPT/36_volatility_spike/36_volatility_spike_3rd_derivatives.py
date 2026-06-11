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



def vsp_001_realized_vol_z_accel_1(vsp_001_realized_vol_z_roc_1):
    feature = _s(vsp_001_realized_vol_z_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def vsp_007_realized_vol_z_accel_5(vsp_007_realized_vol_z_roc_5):
    feature = _s(vsp_007_realized_vol_z_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def vsp_013_realized_vol_z_accel_42(vsp_013_realized_vol_z_roc_42):
    feature = _s(vsp_013_realized_vol_z_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def vsp_179_vsp_019_realized_vol_z_42_019_accel_126(vsp_154_vsp_019_realized_vol_z_42_019_roc_126):
    feature = _s(vsp_154_vsp_019_realized_vol_z_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def vsp_180_vsp_025_realized_vol_z_378_025_accel_378(vsp_155_vsp_025_realized_vol_z_378_025_roc_378):
    feature = _s(vsp_155_vsp_025_realized_vol_z_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















VOLATILITY_SPIKE_REGISTRY_3RD_DERIVATIVES = {
    'vsp_001_realized_vol_z_accel_1': {'inputs': ['vsp_001_realized_vol_z_roc_1'], 'func': vsp_001_realized_vol_z_accel_1},
    'vsp_007_realized_vol_z_accel_5': {'inputs': ['vsp_007_realized_vol_z_roc_5'], 'func': vsp_007_realized_vol_z_accel_5},
    'vsp_013_realized_vol_z_accel_42': {'inputs': ['vsp_013_realized_vol_z_roc_42'], 'func': vsp_013_realized_vol_z_accel_42},
    'vsp_179_vsp_019_realized_vol_z_42_019_accel_126': {'inputs': ['vsp_154_vsp_019_realized_vol_z_42_019_roc_126'], 'func': vsp_179_vsp_019_realized_vol_z_42_019_accel_126},
    'vsp_180_vsp_025_realized_vol_z_378_025_accel_378': {'inputs': ['vsp_155_vsp_025_realized_vol_z_378_025_roc_378'], 'func': vsp_180_vsp_025_realized_vol_z_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def vs_replacement_d3_001(vs_replacement_d2_001):
    feature = _clean(vs_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_001'] = {'inputs': ['vs_replacement_d2_001'], 'func': vs_replacement_d3_001}


def vs_replacement_d3_002(vs_replacement_d2_002):
    feature = _clean(vs_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_002'] = {'inputs': ['vs_replacement_d2_002'], 'func': vs_replacement_d3_002}


def vs_replacement_d3_003(vs_replacement_d2_003):
    feature = _clean(vs_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_003'] = {'inputs': ['vs_replacement_d2_003'], 'func': vs_replacement_d3_003}


def vs_replacement_d3_004(vs_replacement_d2_004):
    feature = _clean(vs_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_004'] = {'inputs': ['vs_replacement_d2_004'], 'func': vs_replacement_d3_004}


def vs_replacement_d3_005(vs_replacement_d2_005):
    feature = _clean(vs_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_005'] = {'inputs': ['vs_replacement_d2_005'], 'func': vs_replacement_d3_005}


def vs_replacement_d3_006(vs_replacement_d2_006):
    feature = _clean(vs_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_006'] = {'inputs': ['vs_replacement_d2_006'], 'func': vs_replacement_d3_006}


def vs_replacement_d3_007(vs_replacement_d2_007):
    feature = _clean(vs_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_007'] = {'inputs': ['vs_replacement_d2_007'], 'func': vs_replacement_d3_007}


def vs_replacement_d3_008(vs_replacement_d2_008):
    feature = _clean(vs_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_008'] = {'inputs': ['vs_replacement_d2_008'], 'func': vs_replacement_d3_008}


def vs_replacement_d3_009(vs_replacement_d2_009):
    feature = _clean(vs_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_009'] = {'inputs': ['vs_replacement_d2_009'], 'func': vs_replacement_d3_009}


def vs_replacement_d3_010(vs_replacement_d2_010):
    feature = _clean(vs_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_010'] = {'inputs': ['vs_replacement_d2_010'], 'func': vs_replacement_d3_010}


def vs_replacement_d3_011(vs_replacement_d2_011):
    feature = _clean(vs_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_011'] = {'inputs': ['vs_replacement_d2_011'], 'func': vs_replacement_d3_011}


def vs_replacement_d3_012(vs_replacement_d2_012):
    feature = _clean(vs_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_012'] = {'inputs': ['vs_replacement_d2_012'], 'func': vs_replacement_d3_012}


def vs_replacement_d3_013(vs_replacement_d2_013):
    feature = _clean(vs_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_013'] = {'inputs': ['vs_replacement_d2_013'], 'func': vs_replacement_d3_013}


def vs_replacement_d3_014(vs_replacement_d2_014):
    feature = _clean(vs_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_014'] = {'inputs': ['vs_replacement_d2_014'], 'func': vs_replacement_d3_014}


def vs_replacement_d3_015(vs_replacement_d2_015):
    feature = _clean(vs_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_015'] = {'inputs': ['vs_replacement_d2_015'], 'func': vs_replacement_d3_015}


def vs_replacement_d3_016(vs_replacement_d2_016):
    feature = _clean(vs_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_016'] = {'inputs': ['vs_replacement_d2_016'], 'func': vs_replacement_d3_016}


def vs_replacement_d3_017(vs_replacement_d2_017):
    feature = _clean(vs_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_017'] = {'inputs': ['vs_replacement_d2_017'], 'func': vs_replacement_d3_017}


def vs_replacement_d3_018(vs_replacement_d2_018):
    feature = _clean(vs_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_018'] = {'inputs': ['vs_replacement_d2_018'], 'func': vs_replacement_d3_018}


def vs_replacement_d3_019(vs_replacement_d2_019):
    feature = _clean(vs_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_019'] = {'inputs': ['vs_replacement_d2_019'], 'func': vs_replacement_d3_019}


def vs_replacement_d3_020(vs_replacement_d2_020):
    feature = _clean(vs_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_020'] = {'inputs': ['vs_replacement_d2_020'], 'func': vs_replacement_d3_020}


def vs_replacement_d3_021(vs_replacement_d2_021):
    feature = _clean(vs_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_021'] = {'inputs': ['vs_replacement_d2_021'], 'func': vs_replacement_d3_021}


def vs_replacement_d3_022(vs_replacement_d2_022):
    feature = _clean(vs_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_022'] = {'inputs': ['vs_replacement_d2_022'], 'func': vs_replacement_d3_022}


def vs_replacement_d3_023(vs_replacement_d2_023):
    feature = _clean(vs_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_023'] = {'inputs': ['vs_replacement_d2_023'], 'func': vs_replacement_d3_023}


def vs_replacement_d3_024(vs_replacement_d2_024):
    feature = _clean(vs_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_024'] = {'inputs': ['vs_replacement_d2_024'], 'func': vs_replacement_d3_024}


def vs_replacement_d3_025(vs_replacement_d2_025):
    feature = _clean(vs_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_025'] = {'inputs': ['vs_replacement_d2_025'], 'func': vs_replacement_d3_025}


def vs_replacement_d3_026(vs_replacement_d2_026):
    feature = _clean(vs_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_026'] = {'inputs': ['vs_replacement_d2_026'], 'func': vs_replacement_d3_026}


def vs_replacement_d3_027(vs_replacement_d2_027):
    feature = _clean(vs_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_027'] = {'inputs': ['vs_replacement_d2_027'], 'func': vs_replacement_d3_027}


def vs_replacement_d3_028(vs_replacement_d2_028):
    feature = _clean(vs_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_028'] = {'inputs': ['vs_replacement_d2_028'], 'func': vs_replacement_d3_028}


def vs_replacement_d3_029(vs_replacement_d2_029):
    feature = _clean(vs_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_029'] = {'inputs': ['vs_replacement_d2_029'], 'func': vs_replacement_d3_029}


def vs_replacement_d3_030(vs_replacement_d2_030):
    feature = _clean(vs_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_030'] = {'inputs': ['vs_replacement_d2_030'], 'func': vs_replacement_d3_030}


def vs_replacement_d3_031(vs_replacement_d2_031):
    feature = _clean(vs_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_031'] = {'inputs': ['vs_replacement_d2_031'], 'func': vs_replacement_d3_031}


def vs_replacement_d3_032(vs_replacement_d2_032):
    feature = _clean(vs_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_032'] = {'inputs': ['vs_replacement_d2_032'], 'func': vs_replacement_d3_032}


def vs_replacement_d3_033(vs_replacement_d2_033):
    feature = _clean(vs_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_033'] = {'inputs': ['vs_replacement_d2_033'], 'func': vs_replacement_d3_033}


def vs_replacement_d3_034(vs_replacement_d2_034):
    feature = _clean(vs_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_034'] = {'inputs': ['vs_replacement_d2_034'], 'func': vs_replacement_d3_034}


def vs_replacement_d3_035(vs_replacement_d2_035):
    feature = _clean(vs_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_035'] = {'inputs': ['vs_replacement_d2_035'], 'func': vs_replacement_d3_035}


def vs_replacement_d3_036(vs_replacement_d2_036):
    feature = _clean(vs_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_036'] = {'inputs': ['vs_replacement_d2_036'], 'func': vs_replacement_d3_036}


def vs_replacement_d3_037(vs_replacement_d2_037):
    feature = _clean(vs_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_037'] = {'inputs': ['vs_replacement_d2_037'], 'func': vs_replacement_d3_037}


def vs_replacement_d3_038(vs_replacement_d2_038):
    feature = _clean(vs_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_038'] = {'inputs': ['vs_replacement_d2_038'], 'func': vs_replacement_d3_038}


def vs_replacement_d3_039(vs_replacement_d2_039):
    feature = _clean(vs_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_039'] = {'inputs': ['vs_replacement_d2_039'], 'func': vs_replacement_d3_039}


def vs_replacement_d3_040(vs_replacement_d2_040):
    feature = _clean(vs_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_040'] = {'inputs': ['vs_replacement_d2_040'], 'func': vs_replacement_d3_040}


def vs_replacement_d3_041(vs_replacement_d2_041):
    feature = _clean(vs_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_041'] = {'inputs': ['vs_replacement_d2_041'], 'func': vs_replacement_d3_041}


def vs_replacement_d3_042(vs_replacement_d2_042):
    feature = _clean(vs_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_042'] = {'inputs': ['vs_replacement_d2_042'], 'func': vs_replacement_d3_042}


def vs_replacement_d3_043(vs_replacement_d2_043):
    feature = _clean(vs_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_043'] = {'inputs': ['vs_replacement_d2_043'], 'func': vs_replacement_d3_043}


def vs_replacement_d3_044(vs_replacement_d2_044):
    feature = _clean(vs_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_044'] = {'inputs': ['vs_replacement_d2_044'], 'func': vs_replacement_d3_044}


def vs_replacement_d3_045(vs_replacement_d2_045):
    feature = _clean(vs_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_045'] = {'inputs': ['vs_replacement_d2_045'], 'func': vs_replacement_d3_045}


def vs_replacement_d3_046(vs_replacement_d2_046):
    feature = _clean(vs_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_046'] = {'inputs': ['vs_replacement_d2_046'], 'func': vs_replacement_d3_046}


def vs_replacement_d3_047(vs_replacement_d2_047):
    feature = _clean(vs_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_047'] = {'inputs': ['vs_replacement_d2_047'], 'func': vs_replacement_d3_047}


def vs_replacement_d3_048(vs_replacement_d2_048):
    feature = _clean(vs_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_048'] = {'inputs': ['vs_replacement_d2_048'], 'func': vs_replacement_d3_048}


def vs_replacement_d3_049(vs_replacement_d2_049):
    feature = _clean(vs_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_049'] = {'inputs': ['vs_replacement_d2_049'], 'func': vs_replacement_d3_049}


def vs_replacement_d3_050(vs_replacement_d2_050):
    feature = _clean(vs_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_050'] = {'inputs': ['vs_replacement_d2_050'], 'func': vs_replacement_d3_050}


def vs_replacement_d3_051(vs_replacement_d2_051):
    feature = _clean(vs_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_051'] = {'inputs': ['vs_replacement_d2_051'], 'func': vs_replacement_d3_051}


def vs_replacement_d3_052(vs_replacement_d2_052):
    feature = _clean(vs_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_052'] = {'inputs': ['vs_replacement_d2_052'], 'func': vs_replacement_d3_052}


def vs_replacement_d3_053(vs_replacement_d2_053):
    feature = _clean(vs_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_053'] = {'inputs': ['vs_replacement_d2_053'], 'func': vs_replacement_d3_053}


def vs_replacement_d3_054(vs_replacement_d2_054):
    feature = _clean(vs_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_054'] = {'inputs': ['vs_replacement_d2_054'], 'func': vs_replacement_d3_054}


def vs_replacement_d3_055(vs_replacement_d2_055):
    feature = _clean(vs_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_055'] = {'inputs': ['vs_replacement_d2_055'], 'func': vs_replacement_d3_055}


def vs_replacement_d3_056(vs_replacement_d2_056):
    feature = _clean(vs_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_056'] = {'inputs': ['vs_replacement_d2_056'], 'func': vs_replacement_d3_056}


def vs_replacement_d3_057(vs_replacement_d2_057):
    feature = _clean(vs_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_057'] = {'inputs': ['vs_replacement_d2_057'], 'func': vs_replacement_d3_057}


def vs_replacement_d3_058(vs_replacement_d2_058):
    feature = _clean(vs_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_058'] = {'inputs': ['vs_replacement_d2_058'], 'func': vs_replacement_d3_058}


def vs_replacement_d3_059(vs_replacement_d2_059):
    feature = _clean(vs_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_059'] = {'inputs': ['vs_replacement_d2_059'], 'func': vs_replacement_d3_059}


def vs_replacement_d3_060(vs_replacement_d2_060):
    feature = _clean(vs_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_060'] = {'inputs': ['vs_replacement_d2_060'], 'func': vs_replacement_d3_060}


def vs_replacement_d3_061(vs_replacement_d2_061):
    feature = _clean(vs_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_061'] = {'inputs': ['vs_replacement_d2_061'], 'func': vs_replacement_d3_061}


def vs_replacement_d3_062(vs_replacement_d2_062):
    feature = _clean(vs_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_062'] = {'inputs': ['vs_replacement_d2_062'], 'func': vs_replacement_d3_062}


def vs_replacement_d3_063(vs_replacement_d2_063):
    feature = _clean(vs_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_063'] = {'inputs': ['vs_replacement_d2_063'], 'func': vs_replacement_d3_063}


def vs_replacement_d3_064(vs_replacement_d2_064):
    feature = _clean(vs_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_064'] = {'inputs': ['vs_replacement_d2_064'], 'func': vs_replacement_d3_064}


def vs_replacement_d3_065(vs_replacement_d2_065):
    feature = _clean(vs_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_065'] = {'inputs': ['vs_replacement_d2_065'], 'func': vs_replacement_d3_065}


def vs_replacement_d3_066(vs_replacement_d2_066):
    feature = _clean(vs_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_066'] = {'inputs': ['vs_replacement_d2_066'], 'func': vs_replacement_d3_066}


def vs_replacement_d3_067(vs_replacement_d2_067):
    feature = _clean(vs_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_067'] = {'inputs': ['vs_replacement_d2_067'], 'func': vs_replacement_d3_067}


def vs_replacement_d3_068(vs_replacement_d2_068):
    feature = _clean(vs_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_068'] = {'inputs': ['vs_replacement_d2_068'], 'func': vs_replacement_d3_068}


def vs_replacement_d3_069(vs_replacement_d2_069):
    feature = _clean(vs_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_069'] = {'inputs': ['vs_replacement_d2_069'], 'func': vs_replacement_d3_069}


def vs_replacement_d3_070(vs_replacement_d2_070):
    feature = _clean(vs_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_070'] = {'inputs': ['vs_replacement_d2_070'], 'func': vs_replacement_d3_070}


def vs_replacement_d3_071(vs_replacement_d2_071):
    feature = _clean(vs_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_071'] = {'inputs': ['vs_replacement_d2_071'], 'func': vs_replacement_d3_071}


def vs_replacement_d3_072(vs_replacement_d2_072):
    feature = _clean(vs_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_072'] = {'inputs': ['vs_replacement_d2_072'], 'func': vs_replacement_d3_072}


def vs_replacement_d3_073(vs_replacement_d2_073):
    feature = _clean(vs_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_073'] = {'inputs': ['vs_replacement_d2_073'], 'func': vs_replacement_d3_073}


def vs_replacement_d3_074(vs_replacement_d2_074):
    feature = _clean(vs_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_074'] = {'inputs': ['vs_replacement_d2_074'], 'func': vs_replacement_d3_074}


def vs_replacement_d3_075(vs_replacement_d2_075):
    feature = _clean(vs_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_075'] = {'inputs': ['vs_replacement_d2_075'], 'func': vs_replacement_d3_075}


def vs_replacement_d3_076(vs_replacement_d2_076):
    feature = _clean(vs_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_076'] = {'inputs': ['vs_replacement_d2_076'], 'func': vs_replacement_d3_076}


def vs_replacement_d3_077(vs_replacement_d2_077):
    feature = _clean(vs_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_077'] = {'inputs': ['vs_replacement_d2_077'], 'func': vs_replacement_d3_077}


def vs_replacement_d3_078(vs_replacement_d2_078):
    feature = _clean(vs_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_078'] = {'inputs': ['vs_replacement_d2_078'], 'func': vs_replacement_d3_078}


def vs_replacement_d3_079(vs_replacement_d2_079):
    feature = _clean(vs_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_079'] = {'inputs': ['vs_replacement_d2_079'], 'func': vs_replacement_d3_079}


def vs_replacement_d3_080(vs_replacement_d2_080):
    feature = _clean(vs_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_080'] = {'inputs': ['vs_replacement_d2_080'], 'func': vs_replacement_d3_080}


def vs_replacement_d3_081(vs_replacement_d2_081):
    feature = _clean(vs_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_081'] = {'inputs': ['vs_replacement_d2_081'], 'func': vs_replacement_d3_081}


def vs_replacement_d3_082(vs_replacement_d2_082):
    feature = _clean(vs_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_082'] = {'inputs': ['vs_replacement_d2_082'], 'func': vs_replacement_d3_082}


def vs_replacement_d3_083(vs_replacement_d2_083):
    feature = _clean(vs_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_083'] = {'inputs': ['vs_replacement_d2_083'], 'func': vs_replacement_d3_083}


def vs_replacement_d3_084(vs_replacement_d2_084):
    feature = _clean(vs_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_084'] = {'inputs': ['vs_replacement_d2_084'], 'func': vs_replacement_d3_084}


def vs_replacement_d3_085(vs_replacement_d2_085):
    feature = _clean(vs_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_085'] = {'inputs': ['vs_replacement_d2_085'], 'func': vs_replacement_d3_085}


def vs_replacement_d3_086(vs_replacement_d2_086):
    feature = _clean(vs_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_086'] = {'inputs': ['vs_replacement_d2_086'], 'func': vs_replacement_d3_086}


def vs_replacement_d3_087(vs_replacement_d2_087):
    feature = _clean(vs_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_087'] = {'inputs': ['vs_replacement_d2_087'], 'func': vs_replacement_d3_087}


def vs_replacement_d3_088(vs_replacement_d2_088):
    feature = _clean(vs_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_088'] = {'inputs': ['vs_replacement_d2_088'], 'func': vs_replacement_d3_088}


def vs_replacement_d3_089(vs_replacement_d2_089):
    feature = _clean(vs_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_089'] = {'inputs': ['vs_replacement_d2_089'], 'func': vs_replacement_d3_089}


def vs_replacement_d3_090(vs_replacement_d2_090):
    feature = _clean(vs_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_090'] = {'inputs': ['vs_replacement_d2_090'], 'func': vs_replacement_d3_090}


def vs_replacement_d3_091(vs_replacement_d2_091):
    feature = _clean(vs_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_091'] = {'inputs': ['vs_replacement_d2_091'], 'func': vs_replacement_d3_091}


def vs_replacement_d3_092(vs_replacement_d2_092):
    feature = _clean(vs_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_092'] = {'inputs': ['vs_replacement_d2_092'], 'func': vs_replacement_d3_092}


def vs_replacement_d3_093(vs_replacement_d2_093):
    feature = _clean(vs_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_093'] = {'inputs': ['vs_replacement_d2_093'], 'func': vs_replacement_d3_093}


def vs_replacement_d3_094(vs_replacement_d2_094):
    feature = _clean(vs_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_094'] = {'inputs': ['vs_replacement_d2_094'], 'func': vs_replacement_d3_094}


def vs_replacement_d3_095(vs_replacement_d2_095):
    feature = _clean(vs_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_095'] = {'inputs': ['vs_replacement_d2_095'], 'func': vs_replacement_d3_095}


def vs_replacement_d3_096(vs_replacement_d2_096):
    feature = _clean(vs_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_096'] = {'inputs': ['vs_replacement_d2_096'], 'func': vs_replacement_d3_096}


def vs_replacement_d3_097(vs_replacement_d2_097):
    feature = _clean(vs_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_097'] = {'inputs': ['vs_replacement_d2_097'], 'func': vs_replacement_d3_097}


def vs_replacement_d3_098(vs_replacement_d2_098):
    feature = _clean(vs_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_098'] = {'inputs': ['vs_replacement_d2_098'], 'func': vs_replacement_d3_098}


def vs_replacement_d3_099(vs_replacement_d2_099):
    feature = _clean(vs_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_099'] = {'inputs': ['vs_replacement_d2_099'], 'func': vs_replacement_d3_099}


def vs_replacement_d3_100(vs_replacement_d2_100):
    feature = _clean(vs_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_100'] = {'inputs': ['vs_replacement_d2_100'], 'func': vs_replacement_d3_100}


def vs_replacement_d3_101(vs_replacement_d2_101):
    feature = _clean(vs_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_101'] = {'inputs': ['vs_replacement_d2_101'], 'func': vs_replacement_d3_101}


def vs_replacement_d3_102(vs_replacement_d2_102):
    feature = _clean(vs_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_102'] = {'inputs': ['vs_replacement_d2_102'], 'func': vs_replacement_d3_102}


def vs_replacement_d3_103(vs_replacement_d2_103):
    feature = _clean(vs_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_103'] = {'inputs': ['vs_replacement_d2_103'], 'func': vs_replacement_d3_103}


def vs_replacement_d3_104(vs_replacement_d2_104):
    feature = _clean(vs_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_104'] = {'inputs': ['vs_replacement_d2_104'], 'func': vs_replacement_d3_104}


def vs_replacement_d3_105(vs_replacement_d2_105):
    feature = _clean(vs_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_105'] = {'inputs': ['vs_replacement_d2_105'], 'func': vs_replacement_d3_105}


def vs_replacement_d3_106(vs_replacement_d2_106):
    feature = _clean(vs_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_106'] = {'inputs': ['vs_replacement_d2_106'], 'func': vs_replacement_d3_106}


def vs_replacement_d3_107(vs_replacement_d2_107):
    feature = _clean(vs_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_107'] = {'inputs': ['vs_replacement_d2_107'], 'func': vs_replacement_d3_107}


def vs_replacement_d3_108(vs_replacement_d2_108):
    feature = _clean(vs_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_108'] = {'inputs': ['vs_replacement_d2_108'], 'func': vs_replacement_d3_108}


def vs_replacement_d3_109(vs_replacement_d2_109):
    feature = _clean(vs_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_109'] = {'inputs': ['vs_replacement_d2_109'], 'func': vs_replacement_d3_109}


def vs_replacement_d3_110(vs_replacement_d2_110):
    feature = _clean(vs_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_110'] = {'inputs': ['vs_replacement_d2_110'], 'func': vs_replacement_d3_110}


def vs_replacement_d3_111(vs_replacement_d2_111):
    feature = _clean(vs_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_111'] = {'inputs': ['vs_replacement_d2_111'], 'func': vs_replacement_d3_111}


def vs_replacement_d3_112(vs_replacement_d2_112):
    feature = _clean(vs_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_112'] = {'inputs': ['vs_replacement_d2_112'], 'func': vs_replacement_d3_112}


def vs_replacement_d3_113(vs_replacement_d2_113):
    feature = _clean(vs_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_113'] = {'inputs': ['vs_replacement_d2_113'], 'func': vs_replacement_d3_113}


def vs_replacement_d3_114(vs_replacement_d2_114):
    feature = _clean(vs_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_114'] = {'inputs': ['vs_replacement_d2_114'], 'func': vs_replacement_d3_114}


def vs_replacement_d3_115(vs_replacement_d2_115):
    feature = _clean(vs_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_115'] = {'inputs': ['vs_replacement_d2_115'], 'func': vs_replacement_d3_115}


def vs_replacement_d3_116(vs_replacement_d2_116):
    feature = _clean(vs_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_116'] = {'inputs': ['vs_replacement_d2_116'], 'func': vs_replacement_d3_116}


def vs_replacement_d3_117(vs_replacement_d2_117):
    feature = _clean(vs_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_117'] = {'inputs': ['vs_replacement_d2_117'], 'func': vs_replacement_d3_117}


def vs_replacement_d3_118(vs_replacement_d2_118):
    feature = _clean(vs_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_118'] = {'inputs': ['vs_replacement_d2_118'], 'func': vs_replacement_d3_118}


def vs_replacement_d3_119(vs_replacement_d2_119):
    feature = _clean(vs_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_119'] = {'inputs': ['vs_replacement_d2_119'], 'func': vs_replacement_d3_119}


def vs_replacement_d3_120(vs_replacement_d2_120):
    feature = _clean(vs_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_120'] = {'inputs': ['vs_replacement_d2_120'], 'func': vs_replacement_d3_120}


def vs_replacement_d3_121(vs_replacement_d2_121):
    feature = _clean(vs_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_121'] = {'inputs': ['vs_replacement_d2_121'], 'func': vs_replacement_d3_121}


def vs_replacement_d3_122(vs_replacement_d2_122):
    feature = _clean(vs_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_122'] = {'inputs': ['vs_replacement_d2_122'], 'func': vs_replacement_d3_122}


def vs_replacement_d3_123(vs_replacement_d2_123):
    feature = _clean(vs_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_123'] = {'inputs': ['vs_replacement_d2_123'], 'func': vs_replacement_d3_123}


def vs_replacement_d3_124(vs_replacement_d2_124):
    feature = _clean(vs_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_124'] = {'inputs': ['vs_replacement_d2_124'], 'func': vs_replacement_d3_124}


def vs_replacement_d3_125(vs_replacement_d2_125):
    feature = _clean(vs_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_125'] = {'inputs': ['vs_replacement_d2_125'], 'func': vs_replacement_d3_125}


def vs_replacement_d3_126(vs_replacement_d2_126):
    feature = _clean(vs_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_126'] = {'inputs': ['vs_replacement_d2_126'], 'func': vs_replacement_d3_126}


def vs_replacement_d3_127(vs_replacement_d2_127):
    feature = _clean(vs_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_127'] = {'inputs': ['vs_replacement_d2_127'], 'func': vs_replacement_d3_127}


def vs_replacement_d3_128(vs_replacement_d2_128):
    feature = _clean(vs_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_128'] = {'inputs': ['vs_replacement_d2_128'], 'func': vs_replacement_d3_128}


def vs_replacement_d3_129(vs_replacement_d2_129):
    feature = _clean(vs_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_129'] = {'inputs': ['vs_replacement_d2_129'], 'func': vs_replacement_d3_129}


def vs_replacement_d3_130(vs_replacement_d2_130):
    feature = _clean(vs_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_130'] = {'inputs': ['vs_replacement_d2_130'], 'func': vs_replacement_d3_130}


def vs_replacement_d3_131(vs_replacement_d2_131):
    feature = _clean(vs_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_131'] = {'inputs': ['vs_replacement_d2_131'], 'func': vs_replacement_d3_131}


def vs_replacement_d3_132(vs_replacement_d2_132):
    feature = _clean(vs_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_132'] = {'inputs': ['vs_replacement_d2_132'], 'func': vs_replacement_d3_132}


def vs_replacement_d3_133(vs_replacement_d2_133):
    feature = _clean(vs_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_133'] = {'inputs': ['vs_replacement_d2_133'], 'func': vs_replacement_d3_133}


def vs_replacement_d3_134(vs_replacement_d2_134):
    feature = _clean(vs_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_134'] = {'inputs': ['vs_replacement_d2_134'], 'func': vs_replacement_d3_134}


def vs_replacement_d3_135(vs_replacement_d2_135):
    feature = _clean(vs_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_135'] = {'inputs': ['vs_replacement_d2_135'], 'func': vs_replacement_d3_135}


def vs_replacement_d3_136(vs_replacement_d2_136):
    feature = _clean(vs_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_136'] = {'inputs': ['vs_replacement_d2_136'], 'func': vs_replacement_d3_136}


def vs_replacement_d3_137(vs_replacement_d2_137):
    feature = _clean(vs_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_137'] = {'inputs': ['vs_replacement_d2_137'], 'func': vs_replacement_d3_137}


def vs_replacement_d3_138(vs_replacement_d2_138):
    feature = _clean(vs_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_138'] = {'inputs': ['vs_replacement_d2_138'], 'func': vs_replacement_d3_138}


def vs_replacement_d3_139(vs_replacement_d2_139):
    feature = _clean(vs_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_139'] = {'inputs': ['vs_replacement_d2_139'], 'func': vs_replacement_d3_139}


def vs_replacement_d3_140(vs_replacement_d2_140):
    feature = _clean(vs_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_140'] = {'inputs': ['vs_replacement_d2_140'], 'func': vs_replacement_d3_140}


def vs_replacement_d3_141(vs_replacement_d2_141):
    feature = _clean(vs_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_141'] = {'inputs': ['vs_replacement_d2_141'], 'func': vs_replacement_d3_141}


def vs_replacement_d3_142(vs_replacement_d2_142):
    feature = _clean(vs_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_142'] = {'inputs': ['vs_replacement_d2_142'], 'func': vs_replacement_d3_142}


def vs_replacement_d3_143(vs_replacement_d2_143):
    feature = _clean(vs_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_143'] = {'inputs': ['vs_replacement_d2_143'], 'func': vs_replacement_d3_143}


def vs_replacement_d3_144(vs_replacement_d2_144):
    feature = _clean(vs_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_144'] = {'inputs': ['vs_replacement_d2_144'], 'func': vs_replacement_d3_144}


def vs_replacement_d3_145(vs_replacement_d2_145):
    feature = _clean(vs_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_145'] = {'inputs': ['vs_replacement_d2_145'], 'func': vs_replacement_d3_145}


def vs_replacement_d3_146(vs_replacement_d2_146):
    feature = _clean(vs_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_146'] = {'inputs': ['vs_replacement_d2_146'], 'func': vs_replacement_d3_146}


def vs_replacement_d3_147(vs_replacement_d2_147):
    feature = _clean(vs_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_147'] = {'inputs': ['vs_replacement_d2_147'], 'func': vs_replacement_d3_147}


def vs_replacement_d3_148(vs_replacement_d2_148):
    feature = _clean(vs_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_148'] = {'inputs': ['vs_replacement_d2_148'], 'func': vs_replacement_d3_148}


def vs_replacement_d3_149(vs_replacement_d2_149):
    feature = _clean(vs_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_149'] = {'inputs': ['vs_replacement_d2_149'], 'func': vs_replacement_d3_149}


def vs_replacement_d3_150(vs_replacement_d2_150):
    feature = _clean(vs_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_150'] = {'inputs': ['vs_replacement_d2_150'], 'func': vs_replacement_d3_150}


def vs_replacement_d3_151(vs_replacement_d2_151):
    feature = _clean(vs_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_151'] = {'inputs': ['vs_replacement_d2_151'], 'func': vs_replacement_d3_151}


def vs_replacement_d3_152(vs_replacement_d2_152):
    feature = _clean(vs_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_152'] = {'inputs': ['vs_replacement_d2_152'], 'func': vs_replacement_d3_152}


def vs_replacement_d3_153(vs_replacement_d2_153):
    feature = _clean(vs_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_153'] = {'inputs': ['vs_replacement_d2_153'], 'func': vs_replacement_d3_153}


def vs_replacement_d3_154(vs_replacement_d2_154):
    feature = _clean(vs_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_154'] = {'inputs': ['vs_replacement_d2_154'], 'func': vs_replacement_d3_154}


def vs_replacement_d3_155(vs_replacement_d2_155):
    feature = _clean(vs_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_155'] = {'inputs': ['vs_replacement_d2_155'], 'func': vs_replacement_d3_155}


def vs_replacement_d3_156(vs_replacement_d2_156):
    feature = _clean(vs_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_156'] = {'inputs': ['vs_replacement_d2_156'], 'func': vs_replacement_d3_156}


def vs_replacement_d3_157(vs_replacement_d2_157):
    feature = _clean(vs_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_157'] = {'inputs': ['vs_replacement_d2_157'], 'func': vs_replacement_d3_157}


def vs_replacement_d3_158(vs_replacement_d2_158):
    feature = _clean(vs_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_158'] = {'inputs': ['vs_replacement_d2_158'], 'func': vs_replacement_d3_158}


def vs_replacement_d3_159(vs_replacement_d2_159):
    feature = _clean(vs_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_159'] = {'inputs': ['vs_replacement_d2_159'], 'func': vs_replacement_d3_159}


def vs_replacement_d3_160(vs_replacement_d2_160):
    feature = _clean(vs_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_160'] = {'inputs': ['vs_replacement_d2_160'], 'func': vs_replacement_d3_160}


def vs_replacement_d3_161(vs_replacement_d2_161):
    feature = _clean(vs_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_161'] = {'inputs': ['vs_replacement_d2_161'], 'func': vs_replacement_d3_161}


def vs_replacement_d3_162(vs_replacement_d2_162):
    feature = _clean(vs_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_162'] = {'inputs': ['vs_replacement_d2_162'], 'func': vs_replacement_d3_162}


def vs_replacement_d3_163(vs_replacement_d2_163):
    feature = _clean(vs_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_163'] = {'inputs': ['vs_replacement_d2_163'], 'func': vs_replacement_d3_163}


def vs_replacement_d3_164(vs_replacement_d2_164):
    feature = _clean(vs_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_164'] = {'inputs': ['vs_replacement_d2_164'], 'func': vs_replacement_d3_164}


def vs_replacement_d3_165(vs_replacement_d2_165):
    feature = _clean(vs_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_165'] = {'inputs': ['vs_replacement_d2_165'], 'func': vs_replacement_d3_165}


def vs_replacement_d3_166(vs_replacement_d2_166):
    feature = _clean(vs_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_166'] = {'inputs': ['vs_replacement_d2_166'], 'func': vs_replacement_d3_166}


def vs_replacement_d3_167(vs_replacement_d2_167):
    feature = _clean(vs_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_167'] = {'inputs': ['vs_replacement_d2_167'], 'func': vs_replacement_d3_167}


def vs_replacement_d3_168(vs_replacement_d2_168):
    feature = _clean(vs_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_168'] = {'inputs': ['vs_replacement_d2_168'], 'func': vs_replacement_d3_168}


def vs_replacement_d3_169(vs_replacement_d2_169):
    feature = _clean(vs_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_169'] = {'inputs': ['vs_replacement_d2_169'], 'func': vs_replacement_d3_169}


def vs_replacement_d3_170(vs_replacement_d2_170):
    feature = _clean(vs_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_170'] = {'inputs': ['vs_replacement_d2_170'], 'func': vs_replacement_d3_170}


def vs_replacement_d3_171(vs_replacement_d2_171):
    feature = _clean(vs_replacement_d2_171)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_171'] = {'inputs': ['vs_replacement_d2_171'], 'func': vs_replacement_d3_171}


def vs_replacement_d3_172(vs_replacement_d2_172):
    feature = _clean(vs_replacement_d2_172)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_172'] = {'inputs': ['vs_replacement_d2_172'], 'func': vs_replacement_d3_172}


def vs_replacement_d3_173(vs_replacement_d2_173):
    feature = _clean(vs_replacement_d2_173)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_173'] = {'inputs': ['vs_replacement_d2_173'], 'func': vs_replacement_d3_173}


def vs_replacement_d3_174(vs_replacement_d2_174):
    feature = _clean(vs_replacement_d2_174)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087000).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_174'] = {'inputs': ['vs_replacement_d2_174'], 'func': vs_replacement_d3_174}


def vs_replacement_d3_175(vs_replacement_d2_175):
    feature = _clean(vs_replacement_d2_175)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087500).reindex(feature.index)
VS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vs_replacement_d3_175'] = {'inputs': ['vs_replacement_d2_175'], 'func': vs_replacement_d3_175}


# Third-derivative extensions for repaired first-base features.
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def vsp_base_universe_d3_001_vsp_002_range_expansion_10_002(vsp_base_universe_d2_001_vsp_002_range_expansion_10_002):
    return _base_universe_d3(vsp_base_universe_d2_001_vsp_002_range_expansion_10_002, 1)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_001_vsp_002_range_expansion_10_002'] = {'inputs': ['vsp_base_universe_d2_001_vsp_002_range_expansion_10_002'], 'func': vsp_base_universe_d3_001_vsp_002_range_expansion_10_002}


def vsp_base_universe_d3_002_vsp_004_close_location_42_004(vsp_base_universe_d2_002_vsp_004_close_location_42_004):
    return _base_universe_d3(vsp_base_universe_d2_002_vsp_004_close_location_42_004, 2)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_002_vsp_004_close_location_42_004'] = {'inputs': ['vsp_base_universe_d2_002_vsp_004_close_location_42_004'], 'func': vsp_base_universe_d3_002_vsp_004_close_location_42_004}


def vsp_base_universe_d3_003_vsp_005_atr_move_63_005(vsp_base_universe_d2_003_vsp_005_atr_move_63_005):
    return _base_universe_d3(vsp_base_universe_d2_003_vsp_005_atr_move_63_005, 3)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_003_vsp_005_atr_move_63_005'] = {'inputs': ['vsp_base_universe_d2_003_vsp_005_atr_move_63_005'], 'func': vsp_base_universe_d3_003_vsp_005_atr_move_63_005}


def vsp_base_universe_d3_004_vsp_008_range_expansion_189_008(vsp_base_universe_d2_004_vsp_008_range_expansion_189_008):
    return _base_universe_d3(vsp_base_universe_d2_004_vsp_008_range_expansion_189_008, 4)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_004_vsp_008_range_expansion_189_008'] = {'inputs': ['vsp_base_universe_d2_004_vsp_008_range_expansion_189_008'], 'func': vsp_base_universe_d3_004_vsp_008_range_expansion_189_008}


def vsp_base_universe_d3_005_vsp_010_close_location_378_010(vsp_base_universe_d2_005_vsp_010_close_location_378_010):
    return _base_universe_d3(vsp_base_universe_d2_005_vsp_010_close_location_378_010, 5)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_005_vsp_010_close_location_378_010'] = {'inputs': ['vsp_base_universe_d2_005_vsp_010_close_location_378_010'], 'func': vsp_base_universe_d3_005_vsp_010_close_location_378_010}


def vsp_base_universe_d3_006_vsp_011_atr_move_504_011(vsp_base_universe_d2_006_vsp_011_atr_move_504_011):
    return _base_universe_d3(vsp_base_universe_d2_006_vsp_011_atr_move_504_011, 6)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_006_vsp_011_atr_move_504_011'] = {'inputs': ['vsp_base_universe_d2_006_vsp_011_atr_move_504_011'], 'func': vsp_base_universe_d3_006_vsp_011_atr_move_504_011}


def vsp_base_universe_d3_007_vsp_014_range_expansion_1260_014(vsp_base_universe_d2_007_vsp_014_range_expansion_1260_014):
    return _base_universe_d3(vsp_base_universe_d2_007_vsp_014_range_expansion_1260_014, 7)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_007_vsp_014_range_expansion_1260_014'] = {'inputs': ['vsp_base_universe_d2_007_vsp_014_range_expansion_1260_014'], 'func': vsp_base_universe_d3_007_vsp_014_range_expansion_1260_014}


def vsp_base_universe_d3_008_vsp_016_close_location_5_016(vsp_base_universe_d2_008_vsp_016_close_location_5_016):
    return _base_universe_d3(vsp_base_universe_d2_008_vsp_016_close_location_5_016, 8)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_008_vsp_016_close_location_5_016'] = {'inputs': ['vsp_base_universe_d2_008_vsp_016_close_location_5_016'], 'func': vsp_base_universe_d3_008_vsp_016_close_location_5_016}


def vsp_base_universe_d3_009_vsp_017_atr_move_10_017(vsp_base_universe_d2_009_vsp_017_atr_move_10_017):
    return _base_universe_d3(vsp_base_universe_d2_009_vsp_017_atr_move_10_017, 9)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_009_vsp_017_atr_move_10_017'] = {'inputs': ['vsp_base_universe_d2_009_vsp_017_atr_move_10_017'], 'func': vsp_base_universe_d3_009_vsp_017_atr_move_10_017}


def vsp_base_universe_d3_010_vsp_020_range_expansion_63_020(vsp_base_universe_d2_010_vsp_020_range_expansion_63_020):
    return _base_universe_d3(vsp_base_universe_d2_010_vsp_020_range_expansion_63_020, 10)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_010_vsp_020_range_expansion_63_020'] = {'inputs': ['vsp_base_universe_d2_010_vsp_020_range_expansion_63_020'], 'func': vsp_base_universe_d3_010_vsp_020_range_expansion_63_020}


def vsp_base_universe_d3_011_vsp_022_close_location_126_022(vsp_base_universe_d2_011_vsp_022_close_location_126_022):
    return _base_universe_d3(vsp_base_universe_d2_011_vsp_022_close_location_126_022, 11)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_011_vsp_022_close_location_126_022'] = {'inputs': ['vsp_base_universe_d2_011_vsp_022_close_location_126_022'], 'func': vsp_base_universe_d3_011_vsp_022_close_location_126_022}


def vsp_base_universe_d3_012_vsp_023_atr_move_189_023(vsp_base_universe_d2_012_vsp_023_atr_move_189_023):
    return _base_universe_d3(vsp_base_universe_d2_012_vsp_023_atr_move_189_023, 12)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_012_vsp_023_atr_move_189_023'] = {'inputs': ['vsp_base_universe_d2_012_vsp_023_atr_move_189_023'], 'func': vsp_base_universe_d3_012_vsp_023_atr_move_189_023}


def vsp_base_universe_d3_013_vsp_026_range_expansion_504_026(vsp_base_universe_d2_013_vsp_026_range_expansion_504_026):
    return _base_universe_d3(vsp_base_universe_d2_013_vsp_026_range_expansion_504_026, 13)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_013_vsp_026_range_expansion_504_026'] = {'inputs': ['vsp_base_universe_d2_013_vsp_026_range_expansion_504_026'], 'func': vsp_base_universe_d3_013_vsp_026_range_expansion_504_026}


def vsp_base_universe_d3_014_vsp_028_close_location_1008_028(vsp_base_universe_d2_014_vsp_028_close_location_1008_028):
    return _base_universe_d3(vsp_base_universe_d2_014_vsp_028_close_location_1008_028, 14)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_014_vsp_028_close_location_1008_028'] = {'inputs': ['vsp_base_universe_d2_014_vsp_028_close_location_1008_028'], 'func': vsp_base_universe_d3_014_vsp_028_close_location_1008_028}


def vsp_base_universe_d3_015_vsp_029_atr_move_1260_029(vsp_base_universe_d2_015_vsp_029_atr_move_1260_029):
    return _base_universe_d3(vsp_base_universe_d2_015_vsp_029_atr_move_1260_029, 15)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_015_vsp_029_atr_move_1260_029'] = {'inputs': ['vsp_base_universe_d2_015_vsp_029_atr_move_1260_029'], 'func': vsp_base_universe_d3_015_vsp_029_atr_move_1260_029}


def vsp_base_universe_d3_016_vsp_basefill_001(vsp_base_universe_d2_016_vsp_basefill_001):
    return _base_universe_d3(vsp_base_universe_d2_016_vsp_basefill_001, 16)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_016_vsp_basefill_001'] = {'inputs': ['vsp_base_universe_d2_016_vsp_basefill_001'], 'func': vsp_base_universe_d3_016_vsp_basefill_001}


def vsp_base_universe_d3_017_vsp_basefill_003(vsp_base_universe_d2_017_vsp_basefill_003):
    return _base_universe_d3(vsp_base_universe_d2_017_vsp_basefill_003, 17)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_017_vsp_basefill_003'] = {'inputs': ['vsp_base_universe_d2_017_vsp_basefill_003'], 'func': vsp_base_universe_d3_017_vsp_basefill_003}


def vsp_base_universe_d3_018_vsp_basefill_006(vsp_base_universe_d2_018_vsp_basefill_006):
    return _base_universe_d3(vsp_base_universe_d2_018_vsp_basefill_006, 18)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_018_vsp_basefill_006'] = {'inputs': ['vsp_base_universe_d2_018_vsp_basefill_006'], 'func': vsp_base_universe_d3_018_vsp_basefill_006}


def vsp_base_universe_d3_019_vsp_basefill_007(vsp_base_universe_d2_019_vsp_basefill_007):
    return _base_universe_d3(vsp_base_universe_d2_019_vsp_basefill_007, 19)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_019_vsp_basefill_007'] = {'inputs': ['vsp_base_universe_d2_019_vsp_basefill_007'], 'func': vsp_base_universe_d3_019_vsp_basefill_007}


def vsp_base_universe_d3_020_vsp_basefill_009(vsp_base_universe_d2_020_vsp_basefill_009):
    return _base_universe_d3(vsp_base_universe_d2_020_vsp_basefill_009, 20)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_020_vsp_basefill_009'] = {'inputs': ['vsp_base_universe_d2_020_vsp_basefill_009'], 'func': vsp_base_universe_d3_020_vsp_basefill_009}


def vsp_base_universe_d3_021_vsp_basefill_012(vsp_base_universe_d2_021_vsp_basefill_012):
    return _base_universe_d3(vsp_base_universe_d2_021_vsp_basefill_012, 21)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_021_vsp_basefill_012'] = {'inputs': ['vsp_base_universe_d2_021_vsp_basefill_012'], 'func': vsp_base_universe_d3_021_vsp_basefill_012}


def vsp_base_universe_d3_022_vsp_basefill_013(vsp_base_universe_d2_022_vsp_basefill_013):
    return _base_universe_d3(vsp_base_universe_d2_022_vsp_basefill_013, 22)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_022_vsp_basefill_013'] = {'inputs': ['vsp_base_universe_d2_022_vsp_basefill_013'], 'func': vsp_base_universe_d3_022_vsp_basefill_013}


def vsp_base_universe_d3_023_vsp_basefill_015(vsp_base_universe_d2_023_vsp_basefill_015):
    return _base_universe_d3(vsp_base_universe_d2_023_vsp_basefill_015, 23)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_023_vsp_basefill_015'] = {'inputs': ['vsp_base_universe_d2_023_vsp_basefill_015'], 'func': vsp_base_universe_d3_023_vsp_basefill_015}


def vsp_base_universe_d3_024_vsp_basefill_018(vsp_base_universe_d2_024_vsp_basefill_018):
    return _base_universe_d3(vsp_base_universe_d2_024_vsp_basefill_018, 24)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_024_vsp_basefill_018'] = {'inputs': ['vsp_base_universe_d2_024_vsp_basefill_018'], 'func': vsp_base_universe_d3_024_vsp_basefill_018}


def vsp_base_universe_d3_025_vsp_basefill_019(vsp_base_universe_d2_025_vsp_basefill_019):
    return _base_universe_d3(vsp_base_universe_d2_025_vsp_basefill_019, 25)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_025_vsp_basefill_019'] = {'inputs': ['vsp_base_universe_d2_025_vsp_basefill_019'], 'func': vsp_base_universe_d3_025_vsp_basefill_019}


def vsp_base_universe_d3_026_vsp_basefill_021(vsp_base_universe_d2_026_vsp_basefill_021):
    return _base_universe_d3(vsp_base_universe_d2_026_vsp_basefill_021, 26)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_026_vsp_basefill_021'] = {'inputs': ['vsp_base_universe_d2_026_vsp_basefill_021'], 'func': vsp_base_universe_d3_026_vsp_basefill_021}


def vsp_base_universe_d3_027_vsp_basefill_024(vsp_base_universe_d2_027_vsp_basefill_024):
    return _base_universe_d3(vsp_base_universe_d2_027_vsp_basefill_024, 27)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_027_vsp_basefill_024'] = {'inputs': ['vsp_base_universe_d2_027_vsp_basefill_024'], 'func': vsp_base_universe_d3_027_vsp_basefill_024}


def vsp_base_universe_d3_028_vsp_basefill_025(vsp_base_universe_d2_028_vsp_basefill_025):
    return _base_universe_d3(vsp_base_universe_d2_028_vsp_basefill_025, 28)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_028_vsp_basefill_025'] = {'inputs': ['vsp_base_universe_d2_028_vsp_basefill_025'], 'func': vsp_base_universe_d3_028_vsp_basefill_025}


def vsp_base_universe_d3_029_vsp_basefill_027(vsp_base_universe_d2_029_vsp_basefill_027):
    return _base_universe_d3(vsp_base_universe_d2_029_vsp_basefill_027, 29)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_029_vsp_basefill_027'] = {'inputs': ['vsp_base_universe_d2_029_vsp_basefill_027'], 'func': vsp_base_universe_d3_029_vsp_basefill_027}


def vsp_base_universe_d3_030_vsp_basefill_030(vsp_base_universe_d2_030_vsp_basefill_030):
    return _base_universe_d3(vsp_base_universe_d2_030_vsp_basefill_030, 30)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_030_vsp_basefill_030'] = {'inputs': ['vsp_base_universe_d2_030_vsp_basefill_030'], 'func': vsp_base_universe_d3_030_vsp_basefill_030}


def vsp_base_universe_d3_031_vsp_basefill_031(vsp_base_universe_d2_031_vsp_basefill_031):
    return _base_universe_d3(vsp_base_universe_d2_031_vsp_basefill_031, 31)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_031_vsp_basefill_031'] = {'inputs': ['vsp_base_universe_d2_031_vsp_basefill_031'], 'func': vsp_base_universe_d3_031_vsp_basefill_031}


def vsp_base_universe_d3_032_vsp_basefill_032(vsp_base_universe_d2_032_vsp_basefill_032):
    return _base_universe_d3(vsp_base_universe_d2_032_vsp_basefill_032, 32)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_032_vsp_basefill_032'] = {'inputs': ['vsp_base_universe_d2_032_vsp_basefill_032'], 'func': vsp_base_universe_d3_032_vsp_basefill_032}


def vsp_base_universe_d3_033_vsp_basefill_033(vsp_base_universe_d2_033_vsp_basefill_033):
    return _base_universe_d3(vsp_base_universe_d2_033_vsp_basefill_033, 33)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_033_vsp_basefill_033'] = {'inputs': ['vsp_base_universe_d2_033_vsp_basefill_033'], 'func': vsp_base_universe_d3_033_vsp_basefill_033}


def vsp_base_universe_d3_034_vsp_basefill_034(vsp_base_universe_d2_034_vsp_basefill_034):
    return _base_universe_d3(vsp_base_universe_d2_034_vsp_basefill_034, 34)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_034_vsp_basefill_034'] = {'inputs': ['vsp_base_universe_d2_034_vsp_basefill_034'], 'func': vsp_base_universe_d3_034_vsp_basefill_034}


def vsp_base_universe_d3_035_vsp_basefill_035(vsp_base_universe_d2_035_vsp_basefill_035):
    return _base_universe_d3(vsp_base_universe_d2_035_vsp_basefill_035, 35)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_035_vsp_basefill_035'] = {'inputs': ['vsp_base_universe_d2_035_vsp_basefill_035'], 'func': vsp_base_universe_d3_035_vsp_basefill_035}


def vsp_base_universe_d3_036_vsp_basefill_036(vsp_base_universe_d2_036_vsp_basefill_036):
    return _base_universe_d3(vsp_base_universe_d2_036_vsp_basefill_036, 36)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_036_vsp_basefill_036'] = {'inputs': ['vsp_base_universe_d2_036_vsp_basefill_036'], 'func': vsp_base_universe_d3_036_vsp_basefill_036}


def vsp_base_universe_d3_037_vsp_basefill_037(vsp_base_universe_d2_037_vsp_basefill_037):
    return _base_universe_d3(vsp_base_universe_d2_037_vsp_basefill_037, 37)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_037_vsp_basefill_037'] = {'inputs': ['vsp_base_universe_d2_037_vsp_basefill_037'], 'func': vsp_base_universe_d3_037_vsp_basefill_037}


def vsp_base_universe_d3_038_vsp_basefill_038(vsp_base_universe_d2_038_vsp_basefill_038):
    return _base_universe_d3(vsp_base_universe_d2_038_vsp_basefill_038, 38)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_038_vsp_basefill_038'] = {'inputs': ['vsp_base_universe_d2_038_vsp_basefill_038'], 'func': vsp_base_universe_d3_038_vsp_basefill_038}


def vsp_base_universe_d3_039_vsp_basefill_039(vsp_base_universe_d2_039_vsp_basefill_039):
    return _base_universe_d3(vsp_base_universe_d2_039_vsp_basefill_039, 39)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_039_vsp_basefill_039'] = {'inputs': ['vsp_base_universe_d2_039_vsp_basefill_039'], 'func': vsp_base_universe_d3_039_vsp_basefill_039}


def vsp_base_universe_d3_040_vsp_basefill_040(vsp_base_universe_d2_040_vsp_basefill_040):
    return _base_universe_d3(vsp_base_universe_d2_040_vsp_basefill_040, 40)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_040_vsp_basefill_040'] = {'inputs': ['vsp_base_universe_d2_040_vsp_basefill_040'], 'func': vsp_base_universe_d3_040_vsp_basefill_040}


def vsp_base_universe_d3_041_vsp_basefill_041(vsp_base_universe_d2_041_vsp_basefill_041):
    return _base_universe_d3(vsp_base_universe_d2_041_vsp_basefill_041, 41)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_041_vsp_basefill_041'] = {'inputs': ['vsp_base_universe_d2_041_vsp_basefill_041'], 'func': vsp_base_universe_d3_041_vsp_basefill_041}


def vsp_base_universe_d3_042_vsp_basefill_042(vsp_base_universe_d2_042_vsp_basefill_042):
    return _base_universe_d3(vsp_base_universe_d2_042_vsp_basefill_042, 42)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_042_vsp_basefill_042'] = {'inputs': ['vsp_base_universe_d2_042_vsp_basefill_042'], 'func': vsp_base_universe_d3_042_vsp_basefill_042}


def vsp_base_universe_d3_043_vsp_basefill_043(vsp_base_universe_d2_043_vsp_basefill_043):
    return _base_universe_d3(vsp_base_universe_d2_043_vsp_basefill_043, 43)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_043_vsp_basefill_043'] = {'inputs': ['vsp_base_universe_d2_043_vsp_basefill_043'], 'func': vsp_base_universe_d3_043_vsp_basefill_043}


def vsp_base_universe_d3_044_vsp_basefill_044(vsp_base_universe_d2_044_vsp_basefill_044):
    return _base_universe_d3(vsp_base_universe_d2_044_vsp_basefill_044, 44)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_044_vsp_basefill_044'] = {'inputs': ['vsp_base_universe_d2_044_vsp_basefill_044'], 'func': vsp_base_universe_d3_044_vsp_basefill_044}


def vsp_base_universe_d3_045_vsp_basefill_045(vsp_base_universe_d2_045_vsp_basefill_045):
    return _base_universe_d3(vsp_base_universe_d2_045_vsp_basefill_045, 45)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_045_vsp_basefill_045'] = {'inputs': ['vsp_base_universe_d2_045_vsp_basefill_045'], 'func': vsp_base_universe_d3_045_vsp_basefill_045}


def vsp_base_universe_d3_046_vsp_basefill_046(vsp_base_universe_d2_046_vsp_basefill_046):
    return _base_universe_d3(vsp_base_universe_d2_046_vsp_basefill_046, 46)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_046_vsp_basefill_046'] = {'inputs': ['vsp_base_universe_d2_046_vsp_basefill_046'], 'func': vsp_base_universe_d3_046_vsp_basefill_046}


def vsp_base_universe_d3_047_vsp_basefill_047(vsp_base_universe_d2_047_vsp_basefill_047):
    return _base_universe_d3(vsp_base_universe_d2_047_vsp_basefill_047, 47)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_047_vsp_basefill_047'] = {'inputs': ['vsp_base_universe_d2_047_vsp_basefill_047'], 'func': vsp_base_universe_d3_047_vsp_basefill_047}


def vsp_base_universe_d3_048_vsp_basefill_048(vsp_base_universe_d2_048_vsp_basefill_048):
    return _base_universe_d3(vsp_base_universe_d2_048_vsp_basefill_048, 48)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_048_vsp_basefill_048'] = {'inputs': ['vsp_base_universe_d2_048_vsp_basefill_048'], 'func': vsp_base_universe_d3_048_vsp_basefill_048}


def vsp_base_universe_d3_049_vsp_basefill_049(vsp_base_universe_d2_049_vsp_basefill_049):
    return _base_universe_d3(vsp_base_universe_d2_049_vsp_basefill_049, 49)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_049_vsp_basefill_049'] = {'inputs': ['vsp_base_universe_d2_049_vsp_basefill_049'], 'func': vsp_base_universe_d3_049_vsp_basefill_049}


def vsp_base_universe_d3_050_vsp_basefill_050(vsp_base_universe_d2_050_vsp_basefill_050):
    return _base_universe_d3(vsp_base_universe_d2_050_vsp_basefill_050, 50)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_050_vsp_basefill_050'] = {'inputs': ['vsp_base_universe_d2_050_vsp_basefill_050'], 'func': vsp_base_universe_d3_050_vsp_basefill_050}


def vsp_base_universe_d3_051_vsp_basefill_051(vsp_base_universe_d2_051_vsp_basefill_051):
    return _base_universe_d3(vsp_base_universe_d2_051_vsp_basefill_051, 51)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_051_vsp_basefill_051'] = {'inputs': ['vsp_base_universe_d2_051_vsp_basefill_051'], 'func': vsp_base_universe_d3_051_vsp_basefill_051}


def vsp_base_universe_d3_052_vsp_basefill_052(vsp_base_universe_d2_052_vsp_basefill_052):
    return _base_universe_d3(vsp_base_universe_d2_052_vsp_basefill_052, 52)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_052_vsp_basefill_052'] = {'inputs': ['vsp_base_universe_d2_052_vsp_basefill_052'], 'func': vsp_base_universe_d3_052_vsp_basefill_052}


def vsp_base_universe_d3_053_vsp_basefill_053(vsp_base_universe_d2_053_vsp_basefill_053):
    return _base_universe_d3(vsp_base_universe_d2_053_vsp_basefill_053, 53)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_053_vsp_basefill_053'] = {'inputs': ['vsp_base_universe_d2_053_vsp_basefill_053'], 'func': vsp_base_universe_d3_053_vsp_basefill_053}


def vsp_base_universe_d3_054_vsp_basefill_054(vsp_base_universe_d2_054_vsp_basefill_054):
    return _base_universe_d3(vsp_base_universe_d2_054_vsp_basefill_054, 54)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_054_vsp_basefill_054'] = {'inputs': ['vsp_base_universe_d2_054_vsp_basefill_054'], 'func': vsp_base_universe_d3_054_vsp_basefill_054}


def vsp_base_universe_d3_055_vsp_basefill_055(vsp_base_universe_d2_055_vsp_basefill_055):
    return _base_universe_d3(vsp_base_universe_d2_055_vsp_basefill_055, 55)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_055_vsp_basefill_055'] = {'inputs': ['vsp_base_universe_d2_055_vsp_basefill_055'], 'func': vsp_base_universe_d3_055_vsp_basefill_055}


def vsp_base_universe_d3_056_vsp_basefill_056(vsp_base_universe_d2_056_vsp_basefill_056):
    return _base_universe_d3(vsp_base_universe_d2_056_vsp_basefill_056, 56)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_056_vsp_basefill_056'] = {'inputs': ['vsp_base_universe_d2_056_vsp_basefill_056'], 'func': vsp_base_universe_d3_056_vsp_basefill_056}


def vsp_base_universe_d3_057_vsp_basefill_057(vsp_base_universe_d2_057_vsp_basefill_057):
    return _base_universe_d3(vsp_base_universe_d2_057_vsp_basefill_057, 57)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_057_vsp_basefill_057'] = {'inputs': ['vsp_base_universe_d2_057_vsp_basefill_057'], 'func': vsp_base_universe_d3_057_vsp_basefill_057}


def vsp_base_universe_d3_058_vsp_basefill_058(vsp_base_universe_d2_058_vsp_basefill_058):
    return _base_universe_d3(vsp_base_universe_d2_058_vsp_basefill_058, 58)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_058_vsp_basefill_058'] = {'inputs': ['vsp_base_universe_d2_058_vsp_basefill_058'], 'func': vsp_base_universe_d3_058_vsp_basefill_058}


def vsp_base_universe_d3_059_vsp_basefill_059(vsp_base_universe_d2_059_vsp_basefill_059):
    return _base_universe_d3(vsp_base_universe_d2_059_vsp_basefill_059, 59)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_059_vsp_basefill_059'] = {'inputs': ['vsp_base_universe_d2_059_vsp_basefill_059'], 'func': vsp_base_universe_d3_059_vsp_basefill_059}


def vsp_base_universe_d3_060_vsp_basefill_060(vsp_base_universe_d2_060_vsp_basefill_060):
    return _base_universe_d3(vsp_base_universe_d2_060_vsp_basefill_060, 60)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_060_vsp_basefill_060'] = {'inputs': ['vsp_base_universe_d2_060_vsp_basefill_060'], 'func': vsp_base_universe_d3_060_vsp_basefill_060}


def vsp_base_universe_d3_061_vsp_basefill_061(vsp_base_universe_d2_061_vsp_basefill_061):
    return _base_universe_d3(vsp_base_universe_d2_061_vsp_basefill_061, 61)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_061_vsp_basefill_061'] = {'inputs': ['vsp_base_universe_d2_061_vsp_basefill_061'], 'func': vsp_base_universe_d3_061_vsp_basefill_061}


def vsp_base_universe_d3_062_vsp_basefill_062(vsp_base_universe_d2_062_vsp_basefill_062):
    return _base_universe_d3(vsp_base_universe_d2_062_vsp_basefill_062, 62)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_062_vsp_basefill_062'] = {'inputs': ['vsp_base_universe_d2_062_vsp_basefill_062'], 'func': vsp_base_universe_d3_062_vsp_basefill_062}


def vsp_base_universe_d3_063_vsp_basefill_063(vsp_base_universe_d2_063_vsp_basefill_063):
    return _base_universe_d3(vsp_base_universe_d2_063_vsp_basefill_063, 63)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_063_vsp_basefill_063'] = {'inputs': ['vsp_base_universe_d2_063_vsp_basefill_063'], 'func': vsp_base_universe_d3_063_vsp_basefill_063}


def vsp_base_universe_d3_064_vsp_basefill_064(vsp_base_universe_d2_064_vsp_basefill_064):
    return _base_universe_d3(vsp_base_universe_d2_064_vsp_basefill_064, 64)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_064_vsp_basefill_064'] = {'inputs': ['vsp_base_universe_d2_064_vsp_basefill_064'], 'func': vsp_base_universe_d3_064_vsp_basefill_064}


def vsp_base_universe_d3_065_vsp_basefill_065(vsp_base_universe_d2_065_vsp_basefill_065):
    return _base_universe_d3(vsp_base_universe_d2_065_vsp_basefill_065, 65)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_065_vsp_basefill_065'] = {'inputs': ['vsp_base_universe_d2_065_vsp_basefill_065'], 'func': vsp_base_universe_d3_065_vsp_basefill_065}


def vsp_base_universe_d3_066_vsp_basefill_066(vsp_base_universe_d2_066_vsp_basefill_066):
    return _base_universe_d3(vsp_base_universe_d2_066_vsp_basefill_066, 66)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_066_vsp_basefill_066'] = {'inputs': ['vsp_base_universe_d2_066_vsp_basefill_066'], 'func': vsp_base_universe_d3_066_vsp_basefill_066}


def vsp_base_universe_d3_067_vsp_basefill_067(vsp_base_universe_d2_067_vsp_basefill_067):
    return _base_universe_d3(vsp_base_universe_d2_067_vsp_basefill_067, 67)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_067_vsp_basefill_067'] = {'inputs': ['vsp_base_universe_d2_067_vsp_basefill_067'], 'func': vsp_base_universe_d3_067_vsp_basefill_067}


def vsp_base_universe_d3_068_vsp_basefill_068(vsp_base_universe_d2_068_vsp_basefill_068):
    return _base_universe_d3(vsp_base_universe_d2_068_vsp_basefill_068, 68)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_068_vsp_basefill_068'] = {'inputs': ['vsp_base_universe_d2_068_vsp_basefill_068'], 'func': vsp_base_universe_d3_068_vsp_basefill_068}


def vsp_base_universe_d3_069_vsp_basefill_069(vsp_base_universe_d2_069_vsp_basefill_069):
    return _base_universe_d3(vsp_base_universe_d2_069_vsp_basefill_069, 69)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_069_vsp_basefill_069'] = {'inputs': ['vsp_base_universe_d2_069_vsp_basefill_069'], 'func': vsp_base_universe_d3_069_vsp_basefill_069}


def vsp_base_universe_d3_070_vsp_basefill_070(vsp_base_universe_d2_070_vsp_basefill_070):
    return _base_universe_d3(vsp_base_universe_d2_070_vsp_basefill_070, 70)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_070_vsp_basefill_070'] = {'inputs': ['vsp_base_universe_d2_070_vsp_basefill_070'], 'func': vsp_base_universe_d3_070_vsp_basefill_070}


def vsp_base_universe_d3_071_vsp_basefill_071(vsp_base_universe_d2_071_vsp_basefill_071):
    return _base_universe_d3(vsp_base_universe_d2_071_vsp_basefill_071, 71)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_071_vsp_basefill_071'] = {'inputs': ['vsp_base_universe_d2_071_vsp_basefill_071'], 'func': vsp_base_universe_d3_071_vsp_basefill_071}


def vsp_base_universe_d3_072_vsp_basefill_072(vsp_base_universe_d2_072_vsp_basefill_072):
    return _base_universe_d3(vsp_base_universe_d2_072_vsp_basefill_072, 72)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_072_vsp_basefill_072'] = {'inputs': ['vsp_base_universe_d2_072_vsp_basefill_072'], 'func': vsp_base_universe_d3_072_vsp_basefill_072}


def vsp_base_universe_d3_073_vsp_basefill_073(vsp_base_universe_d2_073_vsp_basefill_073):
    return _base_universe_d3(vsp_base_universe_d2_073_vsp_basefill_073, 73)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_073_vsp_basefill_073'] = {'inputs': ['vsp_base_universe_d2_073_vsp_basefill_073'], 'func': vsp_base_universe_d3_073_vsp_basefill_073}


def vsp_base_universe_d3_074_vsp_basefill_074(vsp_base_universe_d2_074_vsp_basefill_074):
    return _base_universe_d3(vsp_base_universe_d2_074_vsp_basefill_074, 74)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_074_vsp_basefill_074'] = {'inputs': ['vsp_base_universe_d2_074_vsp_basefill_074'], 'func': vsp_base_universe_d3_074_vsp_basefill_074}


def vsp_base_universe_d3_075_vsp_basefill_075(vsp_base_universe_d2_075_vsp_basefill_075):
    return _base_universe_d3(vsp_base_universe_d2_075_vsp_basefill_075, 75)
VSP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vsp_base_universe_d3_075_vsp_basefill_075'] = {'inputs': ['vsp_base_universe_d2_075_vsp_basefill_075'], 'func': vsp_base_universe_d3_075_vsp_basefill_075}
