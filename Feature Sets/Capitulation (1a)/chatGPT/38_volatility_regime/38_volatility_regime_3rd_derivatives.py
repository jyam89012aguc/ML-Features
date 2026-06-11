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



def vrg_001_realized_vol_z_accel_1(vrg_001_realized_vol_z_roc_1):
    feature = _s(vrg_001_realized_vol_z_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def vrg_007_realized_vol_z_accel_5(vrg_007_realized_vol_z_roc_5):
    feature = _s(vrg_007_realized_vol_z_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def vrg_013_realized_vol_z_accel_42(vrg_013_realized_vol_z_roc_42):
    feature = _s(vrg_013_realized_vol_z_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def vrg_179_vrg_019_realized_vol_z_42_019_accel_126(vrg_154_vrg_019_realized_vol_z_42_019_roc_126):
    feature = _s(vrg_154_vrg_019_realized_vol_z_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def vrg_180_vrg_025_realized_vol_z_378_025_accel_378(vrg_155_vrg_025_realized_vol_z_378_025_roc_378):
    feature = _s(vrg_155_vrg_025_realized_vol_z_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















VOLATILITY_REGIME_REGISTRY_3RD_DERIVATIVES = {
    'vrg_001_realized_vol_z_accel_1': {'inputs': ['vrg_001_realized_vol_z_roc_1'], 'func': vrg_001_realized_vol_z_accel_1},
    'vrg_007_realized_vol_z_accel_5': {'inputs': ['vrg_007_realized_vol_z_roc_5'], 'func': vrg_007_realized_vol_z_accel_5},
    'vrg_013_realized_vol_z_accel_42': {'inputs': ['vrg_013_realized_vol_z_roc_42'], 'func': vrg_013_realized_vol_z_accel_42},
    'vrg_179_vrg_019_realized_vol_z_42_019_accel_126': {'inputs': ['vrg_154_vrg_019_realized_vol_z_42_019_roc_126'], 'func': vrg_179_vrg_019_realized_vol_z_42_019_accel_126},
    'vrg_180_vrg_025_realized_vol_z_378_025_accel_378': {'inputs': ['vrg_155_vrg_025_realized_vol_z_378_025_roc_378'], 'func': vrg_180_vrg_025_realized_vol_z_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def vr_replacement_d3_001(vr_replacement_d2_001):
    feature = _clean(vr_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_001'] = {'inputs': ['vr_replacement_d2_001'], 'func': vr_replacement_d3_001}


def vr_replacement_d3_002(vr_replacement_d2_002):
    feature = _clean(vr_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_002'] = {'inputs': ['vr_replacement_d2_002'], 'func': vr_replacement_d3_002}


def vr_replacement_d3_003(vr_replacement_d2_003):
    feature = _clean(vr_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_003'] = {'inputs': ['vr_replacement_d2_003'], 'func': vr_replacement_d3_003}


def vr_replacement_d3_004(vr_replacement_d2_004):
    feature = _clean(vr_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_004'] = {'inputs': ['vr_replacement_d2_004'], 'func': vr_replacement_d3_004}


def vr_replacement_d3_005(vr_replacement_d2_005):
    feature = _clean(vr_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_005'] = {'inputs': ['vr_replacement_d2_005'], 'func': vr_replacement_d3_005}


def vr_replacement_d3_006(vr_replacement_d2_006):
    feature = _clean(vr_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_006'] = {'inputs': ['vr_replacement_d2_006'], 'func': vr_replacement_d3_006}


def vr_replacement_d3_007(vr_replacement_d2_007):
    feature = _clean(vr_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_007'] = {'inputs': ['vr_replacement_d2_007'], 'func': vr_replacement_d3_007}


def vr_replacement_d3_008(vr_replacement_d2_008):
    feature = _clean(vr_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_008'] = {'inputs': ['vr_replacement_d2_008'], 'func': vr_replacement_d3_008}


def vr_replacement_d3_009(vr_replacement_d2_009):
    feature = _clean(vr_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_009'] = {'inputs': ['vr_replacement_d2_009'], 'func': vr_replacement_d3_009}


def vr_replacement_d3_010(vr_replacement_d2_010):
    feature = _clean(vr_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_010'] = {'inputs': ['vr_replacement_d2_010'], 'func': vr_replacement_d3_010}


def vr_replacement_d3_011(vr_replacement_d2_011):
    feature = _clean(vr_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_011'] = {'inputs': ['vr_replacement_d2_011'], 'func': vr_replacement_d3_011}


def vr_replacement_d3_012(vr_replacement_d2_012):
    feature = _clean(vr_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_012'] = {'inputs': ['vr_replacement_d2_012'], 'func': vr_replacement_d3_012}


def vr_replacement_d3_013(vr_replacement_d2_013):
    feature = _clean(vr_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_013'] = {'inputs': ['vr_replacement_d2_013'], 'func': vr_replacement_d3_013}


def vr_replacement_d3_014(vr_replacement_d2_014):
    feature = _clean(vr_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_014'] = {'inputs': ['vr_replacement_d2_014'], 'func': vr_replacement_d3_014}


def vr_replacement_d3_015(vr_replacement_d2_015):
    feature = _clean(vr_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_015'] = {'inputs': ['vr_replacement_d2_015'], 'func': vr_replacement_d3_015}


def vr_replacement_d3_016(vr_replacement_d2_016):
    feature = _clean(vr_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_016'] = {'inputs': ['vr_replacement_d2_016'], 'func': vr_replacement_d3_016}


def vr_replacement_d3_017(vr_replacement_d2_017):
    feature = _clean(vr_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_017'] = {'inputs': ['vr_replacement_d2_017'], 'func': vr_replacement_d3_017}


def vr_replacement_d3_018(vr_replacement_d2_018):
    feature = _clean(vr_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_018'] = {'inputs': ['vr_replacement_d2_018'], 'func': vr_replacement_d3_018}


def vr_replacement_d3_019(vr_replacement_d2_019):
    feature = _clean(vr_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_019'] = {'inputs': ['vr_replacement_d2_019'], 'func': vr_replacement_d3_019}


def vr_replacement_d3_020(vr_replacement_d2_020):
    feature = _clean(vr_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_020'] = {'inputs': ['vr_replacement_d2_020'], 'func': vr_replacement_d3_020}


def vr_replacement_d3_021(vr_replacement_d2_021):
    feature = _clean(vr_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_021'] = {'inputs': ['vr_replacement_d2_021'], 'func': vr_replacement_d3_021}


def vr_replacement_d3_022(vr_replacement_d2_022):
    feature = _clean(vr_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_022'] = {'inputs': ['vr_replacement_d2_022'], 'func': vr_replacement_d3_022}


def vr_replacement_d3_023(vr_replacement_d2_023):
    feature = _clean(vr_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_023'] = {'inputs': ['vr_replacement_d2_023'], 'func': vr_replacement_d3_023}


def vr_replacement_d3_024(vr_replacement_d2_024):
    feature = _clean(vr_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_024'] = {'inputs': ['vr_replacement_d2_024'], 'func': vr_replacement_d3_024}


def vr_replacement_d3_025(vr_replacement_d2_025):
    feature = _clean(vr_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_025'] = {'inputs': ['vr_replacement_d2_025'], 'func': vr_replacement_d3_025}


def vr_replacement_d3_026(vr_replacement_d2_026):
    feature = _clean(vr_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_026'] = {'inputs': ['vr_replacement_d2_026'], 'func': vr_replacement_d3_026}


def vr_replacement_d3_027(vr_replacement_d2_027):
    feature = _clean(vr_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_027'] = {'inputs': ['vr_replacement_d2_027'], 'func': vr_replacement_d3_027}


def vr_replacement_d3_028(vr_replacement_d2_028):
    feature = _clean(vr_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_028'] = {'inputs': ['vr_replacement_d2_028'], 'func': vr_replacement_d3_028}


def vr_replacement_d3_029(vr_replacement_d2_029):
    feature = _clean(vr_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_029'] = {'inputs': ['vr_replacement_d2_029'], 'func': vr_replacement_d3_029}


def vr_replacement_d3_030(vr_replacement_d2_030):
    feature = _clean(vr_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_030'] = {'inputs': ['vr_replacement_d2_030'], 'func': vr_replacement_d3_030}


def vr_replacement_d3_031(vr_replacement_d2_031):
    feature = _clean(vr_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_031'] = {'inputs': ['vr_replacement_d2_031'], 'func': vr_replacement_d3_031}


def vr_replacement_d3_032(vr_replacement_d2_032):
    feature = _clean(vr_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_032'] = {'inputs': ['vr_replacement_d2_032'], 'func': vr_replacement_d3_032}


def vr_replacement_d3_033(vr_replacement_d2_033):
    feature = _clean(vr_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_033'] = {'inputs': ['vr_replacement_d2_033'], 'func': vr_replacement_d3_033}


def vr_replacement_d3_034(vr_replacement_d2_034):
    feature = _clean(vr_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_034'] = {'inputs': ['vr_replacement_d2_034'], 'func': vr_replacement_d3_034}


def vr_replacement_d3_035(vr_replacement_d2_035):
    feature = _clean(vr_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_035'] = {'inputs': ['vr_replacement_d2_035'], 'func': vr_replacement_d3_035}


def vr_replacement_d3_036(vr_replacement_d2_036):
    feature = _clean(vr_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_036'] = {'inputs': ['vr_replacement_d2_036'], 'func': vr_replacement_d3_036}


def vr_replacement_d3_037(vr_replacement_d2_037):
    feature = _clean(vr_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_037'] = {'inputs': ['vr_replacement_d2_037'], 'func': vr_replacement_d3_037}


def vr_replacement_d3_038(vr_replacement_d2_038):
    feature = _clean(vr_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_038'] = {'inputs': ['vr_replacement_d2_038'], 'func': vr_replacement_d3_038}


def vr_replacement_d3_039(vr_replacement_d2_039):
    feature = _clean(vr_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_039'] = {'inputs': ['vr_replacement_d2_039'], 'func': vr_replacement_d3_039}


def vr_replacement_d3_040(vr_replacement_d2_040):
    feature = _clean(vr_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_040'] = {'inputs': ['vr_replacement_d2_040'], 'func': vr_replacement_d3_040}


def vr_replacement_d3_041(vr_replacement_d2_041):
    feature = _clean(vr_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_041'] = {'inputs': ['vr_replacement_d2_041'], 'func': vr_replacement_d3_041}


def vr_replacement_d3_042(vr_replacement_d2_042):
    feature = _clean(vr_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_042'] = {'inputs': ['vr_replacement_d2_042'], 'func': vr_replacement_d3_042}


def vr_replacement_d3_043(vr_replacement_d2_043):
    feature = _clean(vr_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_043'] = {'inputs': ['vr_replacement_d2_043'], 'func': vr_replacement_d3_043}


def vr_replacement_d3_044(vr_replacement_d2_044):
    feature = _clean(vr_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_044'] = {'inputs': ['vr_replacement_d2_044'], 'func': vr_replacement_d3_044}


def vr_replacement_d3_045(vr_replacement_d2_045):
    feature = _clean(vr_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_045'] = {'inputs': ['vr_replacement_d2_045'], 'func': vr_replacement_d3_045}


def vr_replacement_d3_046(vr_replacement_d2_046):
    feature = _clean(vr_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_046'] = {'inputs': ['vr_replacement_d2_046'], 'func': vr_replacement_d3_046}


def vr_replacement_d3_047(vr_replacement_d2_047):
    feature = _clean(vr_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_047'] = {'inputs': ['vr_replacement_d2_047'], 'func': vr_replacement_d3_047}


def vr_replacement_d3_048(vr_replacement_d2_048):
    feature = _clean(vr_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_048'] = {'inputs': ['vr_replacement_d2_048'], 'func': vr_replacement_d3_048}


def vr_replacement_d3_049(vr_replacement_d2_049):
    feature = _clean(vr_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_049'] = {'inputs': ['vr_replacement_d2_049'], 'func': vr_replacement_d3_049}


def vr_replacement_d3_050(vr_replacement_d2_050):
    feature = _clean(vr_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_050'] = {'inputs': ['vr_replacement_d2_050'], 'func': vr_replacement_d3_050}


def vr_replacement_d3_051(vr_replacement_d2_051):
    feature = _clean(vr_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_051'] = {'inputs': ['vr_replacement_d2_051'], 'func': vr_replacement_d3_051}


def vr_replacement_d3_052(vr_replacement_d2_052):
    feature = _clean(vr_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_052'] = {'inputs': ['vr_replacement_d2_052'], 'func': vr_replacement_d3_052}


def vr_replacement_d3_053(vr_replacement_d2_053):
    feature = _clean(vr_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_053'] = {'inputs': ['vr_replacement_d2_053'], 'func': vr_replacement_d3_053}


def vr_replacement_d3_054(vr_replacement_d2_054):
    feature = _clean(vr_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_054'] = {'inputs': ['vr_replacement_d2_054'], 'func': vr_replacement_d3_054}


def vr_replacement_d3_055(vr_replacement_d2_055):
    feature = _clean(vr_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_055'] = {'inputs': ['vr_replacement_d2_055'], 'func': vr_replacement_d3_055}


def vr_replacement_d3_056(vr_replacement_d2_056):
    feature = _clean(vr_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_056'] = {'inputs': ['vr_replacement_d2_056'], 'func': vr_replacement_d3_056}


def vr_replacement_d3_057(vr_replacement_d2_057):
    feature = _clean(vr_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_057'] = {'inputs': ['vr_replacement_d2_057'], 'func': vr_replacement_d3_057}


def vr_replacement_d3_058(vr_replacement_d2_058):
    feature = _clean(vr_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_058'] = {'inputs': ['vr_replacement_d2_058'], 'func': vr_replacement_d3_058}


def vr_replacement_d3_059(vr_replacement_d2_059):
    feature = _clean(vr_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_059'] = {'inputs': ['vr_replacement_d2_059'], 'func': vr_replacement_d3_059}


def vr_replacement_d3_060(vr_replacement_d2_060):
    feature = _clean(vr_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_060'] = {'inputs': ['vr_replacement_d2_060'], 'func': vr_replacement_d3_060}


def vr_replacement_d3_061(vr_replacement_d2_061):
    feature = _clean(vr_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_061'] = {'inputs': ['vr_replacement_d2_061'], 'func': vr_replacement_d3_061}


def vr_replacement_d3_062(vr_replacement_d2_062):
    feature = _clean(vr_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_062'] = {'inputs': ['vr_replacement_d2_062'], 'func': vr_replacement_d3_062}


def vr_replacement_d3_063(vr_replacement_d2_063):
    feature = _clean(vr_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_063'] = {'inputs': ['vr_replacement_d2_063'], 'func': vr_replacement_d3_063}


def vr_replacement_d3_064(vr_replacement_d2_064):
    feature = _clean(vr_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_064'] = {'inputs': ['vr_replacement_d2_064'], 'func': vr_replacement_d3_064}


def vr_replacement_d3_065(vr_replacement_d2_065):
    feature = _clean(vr_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_065'] = {'inputs': ['vr_replacement_d2_065'], 'func': vr_replacement_d3_065}


def vr_replacement_d3_066(vr_replacement_d2_066):
    feature = _clean(vr_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_066'] = {'inputs': ['vr_replacement_d2_066'], 'func': vr_replacement_d3_066}


def vr_replacement_d3_067(vr_replacement_d2_067):
    feature = _clean(vr_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_067'] = {'inputs': ['vr_replacement_d2_067'], 'func': vr_replacement_d3_067}


def vr_replacement_d3_068(vr_replacement_d2_068):
    feature = _clean(vr_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_068'] = {'inputs': ['vr_replacement_d2_068'], 'func': vr_replacement_d3_068}


def vr_replacement_d3_069(vr_replacement_d2_069):
    feature = _clean(vr_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_069'] = {'inputs': ['vr_replacement_d2_069'], 'func': vr_replacement_d3_069}


def vr_replacement_d3_070(vr_replacement_d2_070):
    feature = _clean(vr_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_070'] = {'inputs': ['vr_replacement_d2_070'], 'func': vr_replacement_d3_070}


def vr_replacement_d3_071(vr_replacement_d2_071):
    feature = _clean(vr_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_071'] = {'inputs': ['vr_replacement_d2_071'], 'func': vr_replacement_d3_071}


def vr_replacement_d3_072(vr_replacement_d2_072):
    feature = _clean(vr_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_072'] = {'inputs': ['vr_replacement_d2_072'], 'func': vr_replacement_d3_072}


def vr_replacement_d3_073(vr_replacement_d2_073):
    feature = _clean(vr_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_073'] = {'inputs': ['vr_replacement_d2_073'], 'func': vr_replacement_d3_073}


def vr_replacement_d3_074(vr_replacement_d2_074):
    feature = _clean(vr_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_074'] = {'inputs': ['vr_replacement_d2_074'], 'func': vr_replacement_d3_074}


def vr_replacement_d3_075(vr_replacement_d2_075):
    feature = _clean(vr_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_075'] = {'inputs': ['vr_replacement_d2_075'], 'func': vr_replacement_d3_075}


def vr_replacement_d3_076(vr_replacement_d2_076):
    feature = _clean(vr_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_076'] = {'inputs': ['vr_replacement_d2_076'], 'func': vr_replacement_d3_076}


def vr_replacement_d3_077(vr_replacement_d2_077):
    feature = _clean(vr_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_077'] = {'inputs': ['vr_replacement_d2_077'], 'func': vr_replacement_d3_077}


def vr_replacement_d3_078(vr_replacement_d2_078):
    feature = _clean(vr_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_078'] = {'inputs': ['vr_replacement_d2_078'], 'func': vr_replacement_d3_078}


def vr_replacement_d3_079(vr_replacement_d2_079):
    feature = _clean(vr_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_079'] = {'inputs': ['vr_replacement_d2_079'], 'func': vr_replacement_d3_079}


def vr_replacement_d3_080(vr_replacement_d2_080):
    feature = _clean(vr_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_080'] = {'inputs': ['vr_replacement_d2_080'], 'func': vr_replacement_d3_080}


def vr_replacement_d3_081(vr_replacement_d2_081):
    feature = _clean(vr_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_081'] = {'inputs': ['vr_replacement_d2_081'], 'func': vr_replacement_d3_081}


def vr_replacement_d3_082(vr_replacement_d2_082):
    feature = _clean(vr_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_082'] = {'inputs': ['vr_replacement_d2_082'], 'func': vr_replacement_d3_082}


def vr_replacement_d3_083(vr_replacement_d2_083):
    feature = _clean(vr_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_083'] = {'inputs': ['vr_replacement_d2_083'], 'func': vr_replacement_d3_083}


def vr_replacement_d3_084(vr_replacement_d2_084):
    feature = _clean(vr_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_084'] = {'inputs': ['vr_replacement_d2_084'], 'func': vr_replacement_d3_084}


def vr_replacement_d3_085(vr_replacement_d2_085):
    feature = _clean(vr_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_085'] = {'inputs': ['vr_replacement_d2_085'], 'func': vr_replacement_d3_085}


def vr_replacement_d3_086(vr_replacement_d2_086):
    feature = _clean(vr_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_086'] = {'inputs': ['vr_replacement_d2_086'], 'func': vr_replacement_d3_086}


def vr_replacement_d3_087(vr_replacement_d2_087):
    feature = _clean(vr_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_087'] = {'inputs': ['vr_replacement_d2_087'], 'func': vr_replacement_d3_087}


def vr_replacement_d3_088(vr_replacement_d2_088):
    feature = _clean(vr_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_088'] = {'inputs': ['vr_replacement_d2_088'], 'func': vr_replacement_d3_088}


def vr_replacement_d3_089(vr_replacement_d2_089):
    feature = _clean(vr_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_089'] = {'inputs': ['vr_replacement_d2_089'], 'func': vr_replacement_d3_089}


def vr_replacement_d3_090(vr_replacement_d2_090):
    feature = _clean(vr_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_090'] = {'inputs': ['vr_replacement_d2_090'], 'func': vr_replacement_d3_090}


def vr_replacement_d3_091(vr_replacement_d2_091):
    feature = _clean(vr_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_091'] = {'inputs': ['vr_replacement_d2_091'], 'func': vr_replacement_d3_091}


def vr_replacement_d3_092(vr_replacement_d2_092):
    feature = _clean(vr_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_092'] = {'inputs': ['vr_replacement_d2_092'], 'func': vr_replacement_d3_092}


def vr_replacement_d3_093(vr_replacement_d2_093):
    feature = _clean(vr_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_093'] = {'inputs': ['vr_replacement_d2_093'], 'func': vr_replacement_d3_093}


def vr_replacement_d3_094(vr_replacement_d2_094):
    feature = _clean(vr_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_094'] = {'inputs': ['vr_replacement_d2_094'], 'func': vr_replacement_d3_094}


def vr_replacement_d3_095(vr_replacement_d2_095):
    feature = _clean(vr_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_095'] = {'inputs': ['vr_replacement_d2_095'], 'func': vr_replacement_d3_095}


def vr_replacement_d3_096(vr_replacement_d2_096):
    feature = _clean(vr_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_096'] = {'inputs': ['vr_replacement_d2_096'], 'func': vr_replacement_d3_096}


def vr_replacement_d3_097(vr_replacement_d2_097):
    feature = _clean(vr_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_097'] = {'inputs': ['vr_replacement_d2_097'], 'func': vr_replacement_d3_097}


def vr_replacement_d3_098(vr_replacement_d2_098):
    feature = _clean(vr_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_098'] = {'inputs': ['vr_replacement_d2_098'], 'func': vr_replacement_d3_098}


def vr_replacement_d3_099(vr_replacement_d2_099):
    feature = _clean(vr_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_099'] = {'inputs': ['vr_replacement_d2_099'], 'func': vr_replacement_d3_099}


def vr_replacement_d3_100(vr_replacement_d2_100):
    feature = _clean(vr_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_100'] = {'inputs': ['vr_replacement_d2_100'], 'func': vr_replacement_d3_100}


def vr_replacement_d3_101(vr_replacement_d2_101):
    feature = _clean(vr_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_101'] = {'inputs': ['vr_replacement_d2_101'], 'func': vr_replacement_d3_101}


def vr_replacement_d3_102(vr_replacement_d2_102):
    feature = _clean(vr_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_102'] = {'inputs': ['vr_replacement_d2_102'], 'func': vr_replacement_d3_102}


def vr_replacement_d3_103(vr_replacement_d2_103):
    feature = _clean(vr_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_103'] = {'inputs': ['vr_replacement_d2_103'], 'func': vr_replacement_d3_103}


def vr_replacement_d3_104(vr_replacement_d2_104):
    feature = _clean(vr_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_104'] = {'inputs': ['vr_replacement_d2_104'], 'func': vr_replacement_d3_104}


def vr_replacement_d3_105(vr_replacement_d2_105):
    feature = _clean(vr_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_105'] = {'inputs': ['vr_replacement_d2_105'], 'func': vr_replacement_d3_105}


def vr_replacement_d3_106(vr_replacement_d2_106):
    feature = _clean(vr_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_106'] = {'inputs': ['vr_replacement_d2_106'], 'func': vr_replacement_d3_106}


def vr_replacement_d3_107(vr_replacement_d2_107):
    feature = _clean(vr_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_107'] = {'inputs': ['vr_replacement_d2_107'], 'func': vr_replacement_d3_107}


def vr_replacement_d3_108(vr_replacement_d2_108):
    feature = _clean(vr_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_108'] = {'inputs': ['vr_replacement_d2_108'], 'func': vr_replacement_d3_108}


def vr_replacement_d3_109(vr_replacement_d2_109):
    feature = _clean(vr_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_109'] = {'inputs': ['vr_replacement_d2_109'], 'func': vr_replacement_d3_109}


def vr_replacement_d3_110(vr_replacement_d2_110):
    feature = _clean(vr_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_110'] = {'inputs': ['vr_replacement_d2_110'], 'func': vr_replacement_d3_110}


def vr_replacement_d3_111(vr_replacement_d2_111):
    feature = _clean(vr_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_111'] = {'inputs': ['vr_replacement_d2_111'], 'func': vr_replacement_d3_111}


def vr_replacement_d3_112(vr_replacement_d2_112):
    feature = _clean(vr_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_112'] = {'inputs': ['vr_replacement_d2_112'], 'func': vr_replacement_d3_112}


def vr_replacement_d3_113(vr_replacement_d2_113):
    feature = _clean(vr_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_113'] = {'inputs': ['vr_replacement_d2_113'], 'func': vr_replacement_d3_113}


def vr_replacement_d3_114(vr_replacement_d2_114):
    feature = _clean(vr_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_114'] = {'inputs': ['vr_replacement_d2_114'], 'func': vr_replacement_d3_114}


def vr_replacement_d3_115(vr_replacement_d2_115):
    feature = _clean(vr_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_115'] = {'inputs': ['vr_replacement_d2_115'], 'func': vr_replacement_d3_115}


def vr_replacement_d3_116(vr_replacement_d2_116):
    feature = _clean(vr_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_116'] = {'inputs': ['vr_replacement_d2_116'], 'func': vr_replacement_d3_116}


def vr_replacement_d3_117(vr_replacement_d2_117):
    feature = _clean(vr_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_117'] = {'inputs': ['vr_replacement_d2_117'], 'func': vr_replacement_d3_117}


def vr_replacement_d3_118(vr_replacement_d2_118):
    feature = _clean(vr_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_118'] = {'inputs': ['vr_replacement_d2_118'], 'func': vr_replacement_d3_118}


def vr_replacement_d3_119(vr_replacement_d2_119):
    feature = _clean(vr_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_119'] = {'inputs': ['vr_replacement_d2_119'], 'func': vr_replacement_d3_119}


def vr_replacement_d3_120(vr_replacement_d2_120):
    feature = _clean(vr_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_120'] = {'inputs': ['vr_replacement_d2_120'], 'func': vr_replacement_d3_120}


def vr_replacement_d3_121(vr_replacement_d2_121):
    feature = _clean(vr_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_121'] = {'inputs': ['vr_replacement_d2_121'], 'func': vr_replacement_d3_121}


def vr_replacement_d3_122(vr_replacement_d2_122):
    feature = _clean(vr_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_122'] = {'inputs': ['vr_replacement_d2_122'], 'func': vr_replacement_d3_122}


def vr_replacement_d3_123(vr_replacement_d2_123):
    feature = _clean(vr_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_123'] = {'inputs': ['vr_replacement_d2_123'], 'func': vr_replacement_d3_123}


def vr_replacement_d3_124(vr_replacement_d2_124):
    feature = _clean(vr_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_124'] = {'inputs': ['vr_replacement_d2_124'], 'func': vr_replacement_d3_124}


def vr_replacement_d3_125(vr_replacement_d2_125):
    feature = _clean(vr_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_125'] = {'inputs': ['vr_replacement_d2_125'], 'func': vr_replacement_d3_125}


def vr_replacement_d3_126(vr_replacement_d2_126):
    feature = _clean(vr_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_126'] = {'inputs': ['vr_replacement_d2_126'], 'func': vr_replacement_d3_126}


def vr_replacement_d3_127(vr_replacement_d2_127):
    feature = _clean(vr_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_127'] = {'inputs': ['vr_replacement_d2_127'], 'func': vr_replacement_d3_127}


def vr_replacement_d3_128(vr_replacement_d2_128):
    feature = _clean(vr_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_128'] = {'inputs': ['vr_replacement_d2_128'], 'func': vr_replacement_d3_128}


def vr_replacement_d3_129(vr_replacement_d2_129):
    feature = _clean(vr_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_129'] = {'inputs': ['vr_replacement_d2_129'], 'func': vr_replacement_d3_129}


def vr_replacement_d3_130(vr_replacement_d2_130):
    feature = _clean(vr_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_130'] = {'inputs': ['vr_replacement_d2_130'], 'func': vr_replacement_d3_130}


def vr_replacement_d3_131(vr_replacement_d2_131):
    feature = _clean(vr_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_131'] = {'inputs': ['vr_replacement_d2_131'], 'func': vr_replacement_d3_131}


def vr_replacement_d3_132(vr_replacement_d2_132):
    feature = _clean(vr_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_132'] = {'inputs': ['vr_replacement_d2_132'], 'func': vr_replacement_d3_132}


def vr_replacement_d3_133(vr_replacement_d2_133):
    feature = _clean(vr_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_133'] = {'inputs': ['vr_replacement_d2_133'], 'func': vr_replacement_d3_133}


def vr_replacement_d3_134(vr_replacement_d2_134):
    feature = _clean(vr_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_134'] = {'inputs': ['vr_replacement_d2_134'], 'func': vr_replacement_d3_134}


def vr_replacement_d3_135(vr_replacement_d2_135):
    feature = _clean(vr_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_135'] = {'inputs': ['vr_replacement_d2_135'], 'func': vr_replacement_d3_135}


def vr_replacement_d3_136(vr_replacement_d2_136):
    feature = _clean(vr_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_136'] = {'inputs': ['vr_replacement_d2_136'], 'func': vr_replacement_d3_136}


def vr_replacement_d3_137(vr_replacement_d2_137):
    feature = _clean(vr_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_137'] = {'inputs': ['vr_replacement_d2_137'], 'func': vr_replacement_d3_137}


def vr_replacement_d3_138(vr_replacement_d2_138):
    feature = _clean(vr_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_138'] = {'inputs': ['vr_replacement_d2_138'], 'func': vr_replacement_d3_138}


def vr_replacement_d3_139(vr_replacement_d2_139):
    feature = _clean(vr_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_139'] = {'inputs': ['vr_replacement_d2_139'], 'func': vr_replacement_d3_139}


def vr_replacement_d3_140(vr_replacement_d2_140):
    feature = _clean(vr_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_140'] = {'inputs': ['vr_replacement_d2_140'], 'func': vr_replacement_d3_140}


def vr_replacement_d3_141(vr_replacement_d2_141):
    feature = _clean(vr_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_141'] = {'inputs': ['vr_replacement_d2_141'], 'func': vr_replacement_d3_141}


def vr_replacement_d3_142(vr_replacement_d2_142):
    feature = _clean(vr_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_142'] = {'inputs': ['vr_replacement_d2_142'], 'func': vr_replacement_d3_142}


def vr_replacement_d3_143(vr_replacement_d2_143):
    feature = _clean(vr_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_143'] = {'inputs': ['vr_replacement_d2_143'], 'func': vr_replacement_d3_143}


def vr_replacement_d3_144(vr_replacement_d2_144):
    feature = _clean(vr_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_144'] = {'inputs': ['vr_replacement_d2_144'], 'func': vr_replacement_d3_144}


def vr_replacement_d3_145(vr_replacement_d2_145):
    feature = _clean(vr_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_145'] = {'inputs': ['vr_replacement_d2_145'], 'func': vr_replacement_d3_145}


def vr_replacement_d3_146(vr_replacement_d2_146):
    feature = _clean(vr_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_146'] = {'inputs': ['vr_replacement_d2_146'], 'func': vr_replacement_d3_146}


def vr_replacement_d3_147(vr_replacement_d2_147):
    feature = _clean(vr_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_147'] = {'inputs': ['vr_replacement_d2_147'], 'func': vr_replacement_d3_147}


def vr_replacement_d3_148(vr_replacement_d2_148):
    feature = _clean(vr_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_148'] = {'inputs': ['vr_replacement_d2_148'], 'func': vr_replacement_d3_148}


def vr_replacement_d3_149(vr_replacement_d2_149):
    feature = _clean(vr_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_149'] = {'inputs': ['vr_replacement_d2_149'], 'func': vr_replacement_d3_149}


def vr_replacement_d3_150(vr_replacement_d2_150):
    feature = _clean(vr_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_150'] = {'inputs': ['vr_replacement_d2_150'], 'func': vr_replacement_d3_150}


def vr_replacement_d3_151(vr_replacement_d2_151):
    feature = _clean(vr_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_151'] = {'inputs': ['vr_replacement_d2_151'], 'func': vr_replacement_d3_151}


def vr_replacement_d3_152(vr_replacement_d2_152):
    feature = _clean(vr_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_152'] = {'inputs': ['vr_replacement_d2_152'], 'func': vr_replacement_d3_152}


def vr_replacement_d3_153(vr_replacement_d2_153):
    feature = _clean(vr_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_153'] = {'inputs': ['vr_replacement_d2_153'], 'func': vr_replacement_d3_153}


def vr_replacement_d3_154(vr_replacement_d2_154):
    feature = _clean(vr_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_154'] = {'inputs': ['vr_replacement_d2_154'], 'func': vr_replacement_d3_154}


def vr_replacement_d3_155(vr_replacement_d2_155):
    feature = _clean(vr_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_155'] = {'inputs': ['vr_replacement_d2_155'], 'func': vr_replacement_d3_155}


def vr_replacement_d3_156(vr_replacement_d2_156):
    feature = _clean(vr_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_156'] = {'inputs': ['vr_replacement_d2_156'], 'func': vr_replacement_d3_156}


def vr_replacement_d3_157(vr_replacement_d2_157):
    feature = _clean(vr_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_157'] = {'inputs': ['vr_replacement_d2_157'], 'func': vr_replacement_d3_157}


def vr_replacement_d3_158(vr_replacement_d2_158):
    feature = _clean(vr_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_158'] = {'inputs': ['vr_replacement_d2_158'], 'func': vr_replacement_d3_158}


def vr_replacement_d3_159(vr_replacement_d2_159):
    feature = _clean(vr_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_159'] = {'inputs': ['vr_replacement_d2_159'], 'func': vr_replacement_d3_159}


def vr_replacement_d3_160(vr_replacement_d2_160):
    feature = _clean(vr_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_160'] = {'inputs': ['vr_replacement_d2_160'], 'func': vr_replacement_d3_160}


def vr_replacement_d3_161(vr_replacement_d2_161):
    feature = _clean(vr_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_161'] = {'inputs': ['vr_replacement_d2_161'], 'func': vr_replacement_d3_161}


def vr_replacement_d3_162(vr_replacement_d2_162):
    feature = _clean(vr_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_162'] = {'inputs': ['vr_replacement_d2_162'], 'func': vr_replacement_d3_162}


def vr_replacement_d3_163(vr_replacement_d2_163):
    feature = _clean(vr_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_163'] = {'inputs': ['vr_replacement_d2_163'], 'func': vr_replacement_d3_163}


def vr_replacement_d3_164(vr_replacement_d2_164):
    feature = _clean(vr_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_164'] = {'inputs': ['vr_replacement_d2_164'], 'func': vr_replacement_d3_164}


def vr_replacement_d3_165(vr_replacement_d2_165):
    feature = _clean(vr_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_165'] = {'inputs': ['vr_replacement_d2_165'], 'func': vr_replacement_d3_165}


def vr_replacement_d3_166(vr_replacement_d2_166):
    feature = _clean(vr_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_166'] = {'inputs': ['vr_replacement_d2_166'], 'func': vr_replacement_d3_166}


def vr_replacement_d3_167(vr_replacement_d2_167):
    feature = _clean(vr_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_167'] = {'inputs': ['vr_replacement_d2_167'], 'func': vr_replacement_d3_167}


def vr_replacement_d3_168(vr_replacement_d2_168):
    feature = _clean(vr_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_168'] = {'inputs': ['vr_replacement_d2_168'], 'func': vr_replacement_d3_168}


def vr_replacement_d3_169(vr_replacement_d2_169):
    feature = _clean(vr_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_169'] = {'inputs': ['vr_replacement_d2_169'], 'func': vr_replacement_d3_169}


def vr_replacement_d3_170(vr_replacement_d2_170):
    feature = _clean(vr_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_170'] = {'inputs': ['vr_replacement_d2_170'], 'func': vr_replacement_d3_170}


def vr_replacement_d3_171(vr_replacement_d2_171):
    feature = _clean(vr_replacement_d2_171)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_171'] = {'inputs': ['vr_replacement_d2_171'], 'func': vr_replacement_d3_171}


def vr_replacement_d3_172(vr_replacement_d2_172):
    feature = _clean(vr_replacement_d2_172)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_172'] = {'inputs': ['vr_replacement_d2_172'], 'func': vr_replacement_d3_172}


def vr_replacement_d3_173(vr_replacement_d2_173):
    feature = _clean(vr_replacement_d2_173)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_173'] = {'inputs': ['vr_replacement_d2_173'], 'func': vr_replacement_d3_173}


def vr_replacement_d3_174(vr_replacement_d2_174):
    feature = _clean(vr_replacement_d2_174)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087000).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_174'] = {'inputs': ['vr_replacement_d2_174'], 'func': vr_replacement_d3_174}


def vr_replacement_d3_175(vr_replacement_d2_175):
    feature = _clean(vr_replacement_d2_175)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087500).reindex(feature.index)
VR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vr_replacement_d3_175'] = {'inputs': ['vr_replacement_d2_175'], 'func': vr_replacement_d3_175}


# Third-derivative extensions for repaired first-base features.
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def vrg_base_universe_d3_001_vrg_002_range_expansion_10_002(vrg_base_universe_d2_001_vrg_002_range_expansion_10_002):
    return _base_universe_d3(vrg_base_universe_d2_001_vrg_002_range_expansion_10_002, 1)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_001_vrg_002_range_expansion_10_002'] = {'inputs': ['vrg_base_universe_d2_001_vrg_002_range_expansion_10_002'], 'func': vrg_base_universe_d3_001_vrg_002_range_expansion_10_002}


def vrg_base_universe_d3_002_vrg_004_close_location_42_004(vrg_base_universe_d2_002_vrg_004_close_location_42_004):
    return _base_universe_d3(vrg_base_universe_d2_002_vrg_004_close_location_42_004, 2)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_002_vrg_004_close_location_42_004'] = {'inputs': ['vrg_base_universe_d2_002_vrg_004_close_location_42_004'], 'func': vrg_base_universe_d3_002_vrg_004_close_location_42_004}


def vrg_base_universe_d3_003_vrg_005_atr_move_63_005(vrg_base_universe_d2_003_vrg_005_atr_move_63_005):
    return _base_universe_d3(vrg_base_universe_d2_003_vrg_005_atr_move_63_005, 3)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_003_vrg_005_atr_move_63_005'] = {'inputs': ['vrg_base_universe_d2_003_vrg_005_atr_move_63_005'], 'func': vrg_base_universe_d3_003_vrg_005_atr_move_63_005}


def vrg_base_universe_d3_004_vrg_008_range_expansion_189_008(vrg_base_universe_d2_004_vrg_008_range_expansion_189_008):
    return _base_universe_d3(vrg_base_universe_d2_004_vrg_008_range_expansion_189_008, 4)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_004_vrg_008_range_expansion_189_008'] = {'inputs': ['vrg_base_universe_d2_004_vrg_008_range_expansion_189_008'], 'func': vrg_base_universe_d3_004_vrg_008_range_expansion_189_008}


def vrg_base_universe_d3_005_vrg_010_close_location_378_010(vrg_base_universe_d2_005_vrg_010_close_location_378_010):
    return _base_universe_d3(vrg_base_universe_d2_005_vrg_010_close_location_378_010, 5)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_005_vrg_010_close_location_378_010'] = {'inputs': ['vrg_base_universe_d2_005_vrg_010_close_location_378_010'], 'func': vrg_base_universe_d3_005_vrg_010_close_location_378_010}


def vrg_base_universe_d3_006_vrg_011_atr_move_504_011(vrg_base_universe_d2_006_vrg_011_atr_move_504_011):
    return _base_universe_d3(vrg_base_universe_d2_006_vrg_011_atr_move_504_011, 6)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_006_vrg_011_atr_move_504_011'] = {'inputs': ['vrg_base_universe_d2_006_vrg_011_atr_move_504_011'], 'func': vrg_base_universe_d3_006_vrg_011_atr_move_504_011}


def vrg_base_universe_d3_007_vrg_014_range_expansion_1260_014(vrg_base_universe_d2_007_vrg_014_range_expansion_1260_014):
    return _base_universe_d3(vrg_base_universe_d2_007_vrg_014_range_expansion_1260_014, 7)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_007_vrg_014_range_expansion_1260_014'] = {'inputs': ['vrg_base_universe_d2_007_vrg_014_range_expansion_1260_014'], 'func': vrg_base_universe_d3_007_vrg_014_range_expansion_1260_014}


def vrg_base_universe_d3_008_vrg_016_close_location_5_016(vrg_base_universe_d2_008_vrg_016_close_location_5_016):
    return _base_universe_d3(vrg_base_universe_d2_008_vrg_016_close_location_5_016, 8)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_008_vrg_016_close_location_5_016'] = {'inputs': ['vrg_base_universe_d2_008_vrg_016_close_location_5_016'], 'func': vrg_base_universe_d3_008_vrg_016_close_location_5_016}


def vrg_base_universe_d3_009_vrg_017_atr_move_10_017(vrg_base_universe_d2_009_vrg_017_atr_move_10_017):
    return _base_universe_d3(vrg_base_universe_d2_009_vrg_017_atr_move_10_017, 9)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_009_vrg_017_atr_move_10_017'] = {'inputs': ['vrg_base_universe_d2_009_vrg_017_atr_move_10_017'], 'func': vrg_base_universe_d3_009_vrg_017_atr_move_10_017}


def vrg_base_universe_d3_010_vrg_020_range_expansion_63_020(vrg_base_universe_d2_010_vrg_020_range_expansion_63_020):
    return _base_universe_d3(vrg_base_universe_d2_010_vrg_020_range_expansion_63_020, 10)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_010_vrg_020_range_expansion_63_020'] = {'inputs': ['vrg_base_universe_d2_010_vrg_020_range_expansion_63_020'], 'func': vrg_base_universe_d3_010_vrg_020_range_expansion_63_020}


def vrg_base_universe_d3_011_vrg_022_close_location_126_022(vrg_base_universe_d2_011_vrg_022_close_location_126_022):
    return _base_universe_d3(vrg_base_universe_d2_011_vrg_022_close_location_126_022, 11)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_011_vrg_022_close_location_126_022'] = {'inputs': ['vrg_base_universe_d2_011_vrg_022_close_location_126_022'], 'func': vrg_base_universe_d3_011_vrg_022_close_location_126_022}


def vrg_base_universe_d3_012_vrg_023_atr_move_189_023(vrg_base_universe_d2_012_vrg_023_atr_move_189_023):
    return _base_universe_d3(vrg_base_universe_d2_012_vrg_023_atr_move_189_023, 12)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_012_vrg_023_atr_move_189_023'] = {'inputs': ['vrg_base_universe_d2_012_vrg_023_atr_move_189_023'], 'func': vrg_base_universe_d3_012_vrg_023_atr_move_189_023}


def vrg_base_universe_d3_013_vrg_026_range_expansion_504_026(vrg_base_universe_d2_013_vrg_026_range_expansion_504_026):
    return _base_universe_d3(vrg_base_universe_d2_013_vrg_026_range_expansion_504_026, 13)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_013_vrg_026_range_expansion_504_026'] = {'inputs': ['vrg_base_universe_d2_013_vrg_026_range_expansion_504_026'], 'func': vrg_base_universe_d3_013_vrg_026_range_expansion_504_026}


def vrg_base_universe_d3_014_vrg_028_close_location_1008_028(vrg_base_universe_d2_014_vrg_028_close_location_1008_028):
    return _base_universe_d3(vrg_base_universe_d2_014_vrg_028_close_location_1008_028, 14)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_014_vrg_028_close_location_1008_028'] = {'inputs': ['vrg_base_universe_d2_014_vrg_028_close_location_1008_028'], 'func': vrg_base_universe_d3_014_vrg_028_close_location_1008_028}


def vrg_base_universe_d3_015_vrg_029_atr_move_1260_029(vrg_base_universe_d2_015_vrg_029_atr_move_1260_029):
    return _base_universe_d3(vrg_base_universe_d2_015_vrg_029_atr_move_1260_029, 15)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_015_vrg_029_atr_move_1260_029'] = {'inputs': ['vrg_base_universe_d2_015_vrg_029_atr_move_1260_029'], 'func': vrg_base_universe_d3_015_vrg_029_atr_move_1260_029}


def vrg_base_universe_d3_016_vrg_basefill_001(vrg_base_universe_d2_016_vrg_basefill_001):
    return _base_universe_d3(vrg_base_universe_d2_016_vrg_basefill_001, 16)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_016_vrg_basefill_001'] = {'inputs': ['vrg_base_universe_d2_016_vrg_basefill_001'], 'func': vrg_base_universe_d3_016_vrg_basefill_001}


def vrg_base_universe_d3_017_vrg_basefill_003(vrg_base_universe_d2_017_vrg_basefill_003):
    return _base_universe_d3(vrg_base_universe_d2_017_vrg_basefill_003, 17)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_017_vrg_basefill_003'] = {'inputs': ['vrg_base_universe_d2_017_vrg_basefill_003'], 'func': vrg_base_universe_d3_017_vrg_basefill_003}


def vrg_base_universe_d3_018_vrg_basefill_006(vrg_base_universe_d2_018_vrg_basefill_006):
    return _base_universe_d3(vrg_base_universe_d2_018_vrg_basefill_006, 18)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_018_vrg_basefill_006'] = {'inputs': ['vrg_base_universe_d2_018_vrg_basefill_006'], 'func': vrg_base_universe_d3_018_vrg_basefill_006}


def vrg_base_universe_d3_019_vrg_basefill_007(vrg_base_universe_d2_019_vrg_basefill_007):
    return _base_universe_d3(vrg_base_universe_d2_019_vrg_basefill_007, 19)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_019_vrg_basefill_007'] = {'inputs': ['vrg_base_universe_d2_019_vrg_basefill_007'], 'func': vrg_base_universe_d3_019_vrg_basefill_007}


def vrg_base_universe_d3_020_vrg_basefill_009(vrg_base_universe_d2_020_vrg_basefill_009):
    return _base_universe_d3(vrg_base_universe_d2_020_vrg_basefill_009, 20)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_020_vrg_basefill_009'] = {'inputs': ['vrg_base_universe_d2_020_vrg_basefill_009'], 'func': vrg_base_universe_d3_020_vrg_basefill_009}


def vrg_base_universe_d3_021_vrg_basefill_012(vrg_base_universe_d2_021_vrg_basefill_012):
    return _base_universe_d3(vrg_base_universe_d2_021_vrg_basefill_012, 21)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_021_vrg_basefill_012'] = {'inputs': ['vrg_base_universe_d2_021_vrg_basefill_012'], 'func': vrg_base_universe_d3_021_vrg_basefill_012}


def vrg_base_universe_d3_022_vrg_basefill_013(vrg_base_universe_d2_022_vrg_basefill_013):
    return _base_universe_d3(vrg_base_universe_d2_022_vrg_basefill_013, 22)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_022_vrg_basefill_013'] = {'inputs': ['vrg_base_universe_d2_022_vrg_basefill_013'], 'func': vrg_base_universe_d3_022_vrg_basefill_013}


def vrg_base_universe_d3_023_vrg_basefill_015(vrg_base_universe_d2_023_vrg_basefill_015):
    return _base_universe_d3(vrg_base_universe_d2_023_vrg_basefill_015, 23)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_023_vrg_basefill_015'] = {'inputs': ['vrg_base_universe_d2_023_vrg_basefill_015'], 'func': vrg_base_universe_d3_023_vrg_basefill_015}


def vrg_base_universe_d3_024_vrg_basefill_018(vrg_base_universe_d2_024_vrg_basefill_018):
    return _base_universe_d3(vrg_base_universe_d2_024_vrg_basefill_018, 24)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_024_vrg_basefill_018'] = {'inputs': ['vrg_base_universe_d2_024_vrg_basefill_018'], 'func': vrg_base_universe_d3_024_vrg_basefill_018}


def vrg_base_universe_d3_025_vrg_basefill_019(vrg_base_universe_d2_025_vrg_basefill_019):
    return _base_universe_d3(vrg_base_universe_d2_025_vrg_basefill_019, 25)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_025_vrg_basefill_019'] = {'inputs': ['vrg_base_universe_d2_025_vrg_basefill_019'], 'func': vrg_base_universe_d3_025_vrg_basefill_019}


def vrg_base_universe_d3_026_vrg_basefill_021(vrg_base_universe_d2_026_vrg_basefill_021):
    return _base_universe_d3(vrg_base_universe_d2_026_vrg_basefill_021, 26)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_026_vrg_basefill_021'] = {'inputs': ['vrg_base_universe_d2_026_vrg_basefill_021'], 'func': vrg_base_universe_d3_026_vrg_basefill_021}


def vrg_base_universe_d3_027_vrg_basefill_024(vrg_base_universe_d2_027_vrg_basefill_024):
    return _base_universe_d3(vrg_base_universe_d2_027_vrg_basefill_024, 27)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_027_vrg_basefill_024'] = {'inputs': ['vrg_base_universe_d2_027_vrg_basefill_024'], 'func': vrg_base_universe_d3_027_vrg_basefill_024}


def vrg_base_universe_d3_028_vrg_basefill_025(vrg_base_universe_d2_028_vrg_basefill_025):
    return _base_universe_d3(vrg_base_universe_d2_028_vrg_basefill_025, 28)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_028_vrg_basefill_025'] = {'inputs': ['vrg_base_universe_d2_028_vrg_basefill_025'], 'func': vrg_base_universe_d3_028_vrg_basefill_025}


def vrg_base_universe_d3_029_vrg_basefill_027(vrg_base_universe_d2_029_vrg_basefill_027):
    return _base_universe_d3(vrg_base_universe_d2_029_vrg_basefill_027, 29)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_029_vrg_basefill_027'] = {'inputs': ['vrg_base_universe_d2_029_vrg_basefill_027'], 'func': vrg_base_universe_d3_029_vrg_basefill_027}


def vrg_base_universe_d3_030_vrg_basefill_030(vrg_base_universe_d2_030_vrg_basefill_030):
    return _base_universe_d3(vrg_base_universe_d2_030_vrg_basefill_030, 30)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_030_vrg_basefill_030'] = {'inputs': ['vrg_base_universe_d2_030_vrg_basefill_030'], 'func': vrg_base_universe_d3_030_vrg_basefill_030}


def vrg_base_universe_d3_031_vrg_basefill_031(vrg_base_universe_d2_031_vrg_basefill_031):
    return _base_universe_d3(vrg_base_universe_d2_031_vrg_basefill_031, 31)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_031_vrg_basefill_031'] = {'inputs': ['vrg_base_universe_d2_031_vrg_basefill_031'], 'func': vrg_base_universe_d3_031_vrg_basefill_031}


def vrg_base_universe_d3_032_vrg_basefill_032(vrg_base_universe_d2_032_vrg_basefill_032):
    return _base_universe_d3(vrg_base_universe_d2_032_vrg_basefill_032, 32)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_032_vrg_basefill_032'] = {'inputs': ['vrg_base_universe_d2_032_vrg_basefill_032'], 'func': vrg_base_universe_d3_032_vrg_basefill_032}


def vrg_base_universe_d3_033_vrg_basefill_033(vrg_base_universe_d2_033_vrg_basefill_033):
    return _base_universe_d3(vrg_base_universe_d2_033_vrg_basefill_033, 33)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_033_vrg_basefill_033'] = {'inputs': ['vrg_base_universe_d2_033_vrg_basefill_033'], 'func': vrg_base_universe_d3_033_vrg_basefill_033}


def vrg_base_universe_d3_034_vrg_basefill_034(vrg_base_universe_d2_034_vrg_basefill_034):
    return _base_universe_d3(vrg_base_universe_d2_034_vrg_basefill_034, 34)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_034_vrg_basefill_034'] = {'inputs': ['vrg_base_universe_d2_034_vrg_basefill_034'], 'func': vrg_base_universe_d3_034_vrg_basefill_034}


def vrg_base_universe_d3_035_vrg_basefill_035(vrg_base_universe_d2_035_vrg_basefill_035):
    return _base_universe_d3(vrg_base_universe_d2_035_vrg_basefill_035, 35)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_035_vrg_basefill_035'] = {'inputs': ['vrg_base_universe_d2_035_vrg_basefill_035'], 'func': vrg_base_universe_d3_035_vrg_basefill_035}


def vrg_base_universe_d3_036_vrg_basefill_036(vrg_base_universe_d2_036_vrg_basefill_036):
    return _base_universe_d3(vrg_base_universe_d2_036_vrg_basefill_036, 36)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_036_vrg_basefill_036'] = {'inputs': ['vrg_base_universe_d2_036_vrg_basefill_036'], 'func': vrg_base_universe_d3_036_vrg_basefill_036}


def vrg_base_universe_d3_037_vrg_basefill_037(vrg_base_universe_d2_037_vrg_basefill_037):
    return _base_universe_d3(vrg_base_universe_d2_037_vrg_basefill_037, 37)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_037_vrg_basefill_037'] = {'inputs': ['vrg_base_universe_d2_037_vrg_basefill_037'], 'func': vrg_base_universe_d3_037_vrg_basefill_037}


def vrg_base_universe_d3_038_vrg_basefill_038(vrg_base_universe_d2_038_vrg_basefill_038):
    return _base_universe_d3(vrg_base_universe_d2_038_vrg_basefill_038, 38)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_038_vrg_basefill_038'] = {'inputs': ['vrg_base_universe_d2_038_vrg_basefill_038'], 'func': vrg_base_universe_d3_038_vrg_basefill_038}


def vrg_base_universe_d3_039_vrg_basefill_039(vrg_base_universe_d2_039_vrg_basefill_039):
    return _base_universe_d3(vrg_base_universe_d2_039_vrg_basefill_039, 39)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_039_vrg_basefill_039'] = {'inputs': ['vrg_base_universe_d2_039_vrg_basefill_039'], 'func': vrg_base_universe_d3_039_vrg_basefill_039}


def vrg_base_universe_d3_040_vrg_basefill_040(vrg_base_universe_d2_040_vrg_basefill_040):
    return _base_universe_d3(vrg_base_universe_d2_040_vrg_basefill_040, 40)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_040_vrg_basefill_040'] = {'inputs': ['vrg_base_universe_d2_040_vrg_basefill_040'], 'func': vrg_base_universe_d3_040_vrg_basefill_040}


def vrg_base_universe_d3_041_vrg_basefill_041(vrg_base_universe_d2_041_vrg_basefill_041):
    return _base_universe_d3(vrg_base_universe_d2_041_vrg_basefill_041, 41)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_041_vrg_basefill_041'] = {'inputs': ['vrg_base_universe_d2_041_vrg_basefill_041'], 'func': vrg_base_universe_d3_041_vrg_basefill_041}


def vrg_base_universe_d3_042_vrg_basefill_042(vrg_base_universe_d2_042_vrg_basefill_042):
    return _base_universe_d3(vrg_base_universe_d2_042_vrg_basefill_042, 42)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_042_vrg_basefill_042'] = {'inputs': ['vrg_base_universe_d2_042_vrg_basefill_042'], 'func': vrg_base_universe_d3_042_vrg_basefill_042}


def vrg_base_universe_d3_043_vrg_basefill_043(vrg_base_universe_d2_043_vrg_basefill_043):
    return _base_universe_d3(vrg_base_universe_d2_043_vrg_basefill_043, 43)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_043_vrg_basefill_043'] = {'inputs': ['vrg_base_universe_d2_043_vrg_basefill_043'], 'func': vrg_base_universe_d3_043_vrg_basefill_043}


def vrg_base_universe_d3_044_vrg_basefill_044(vrg_base_universe_d2_044_vrg_basefill_044):
    return _base_universe_d3(vrg_base_universe_d2_044_vrg_basefill_044, 44)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_044_vrg_basefill_044'] = {'inputs': ['vrg_base_universe_d2_044_vrg_basefill_044'], 'func': vrg_base_universe_d3_044_vrg_basefill_044}


def vrg_base_universe_d3_045_vrg_basefill_045(vrg_base_universe_d2_045_vrg_basefill_045):
    return _base_universe_d3(vrg_base_universe_d2_045_vrg_basefill_045, 45)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_045_vrg_basefill_045'] = {'inputs': ['vrg_base_universe_d2_045_vrg_basefill_045'], 'func': vrg_base_universe_d3_045_vrg_basefill_045}


def vrg_base_universe_d3_046_vrg_basefill_046(vrg_base_universe_d2_046_vrg_basefill_046):
    return _base_universe_d3(vrg_base_universe_d2_046_vrg_basefill_046, 46)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_046_vrg_basefill_046'] = {'inputs': ['vrg_base_universe_d2_046_vrg_basefill_046'], 'func': vrg_base_universe_d3_046_vrg_basefill_046}


def vrg_base_universe_d3_047_vrg_basefill_047(vrg_base_universe_d2_047_vrg_basefill_047):
    return _base_universe_d3(vrg_base_universe_d2_047_vrg_basefill_047, 47)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_047_vrg_basefill_047'] = {'inputs': ['vrg_base_universe_d2_047_vrg_basefill_047'], 'func': vrg_base_universe_d3_047_vrg_basefill_047}


def vrg_base_universe_d3_048_vrg_basefill_048(vrg_base_universe_d2_048_vrg_basefill_048):
    return _base_universe_d3(vrg_base_universe_d2_048_vrg_basefill_048, 48)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_048_vrg_basefill_048'] = {'inputs': ['vrg_base_universe_d2_048_vrg_basefill_048'], 'func': vrg_base_universe_d3_048_vrg_basefill_048}


def vrg_base_universe_d3_049_vrg_basefill_049(vrg_base_universe_d2_049_vrg_basefill_049):
    return _base_universe_d3(vrg_base_universe_d2_049_vrg_basefill_049, 49)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_049_vrg_basefill_049'] = {'inputs': ['vrg_base_universe_d2_049_vrg_basefill_049'], 'func': vrg_base_universe_d3_049_vrg_basefill_049}


def vrg_base_universe_d3_050_vrg_basefill_050(vrg_base_universe_d2_050_vrg_basefill_050):
    return _base_universe_d3(vrg_base_universe_d2_050_vrg_basefill_050, 50)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_050_vrg_basefill_050'] = {'inputs': ['vrg_base_universe_d2_050_vrg_basefill_050'], 'func': vrg_base_universe_d3_050_vrg_basefill_050}


def vrg_base_universe_d3_051_vrg_basefill_051(vrg_base_universe_d2_051_vrg_basefill_051):
    return _base_universe_d3(vrg_base_universe_d2_051_vrg_basefill_051, 51)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_051_vrg_basefill_051'] = {'inputs': ['vrg_base_universe_d2_051_vrg_basefill_051'], 'func': vrg_base_universe_d3_051_vrg_basefill_051}


def vrg_base_universe_d3_052_vrg_basefill_052(vrg_base_universe_d2_052_vrg_basefill_052):
    return _base_universe_d3(vrg_base_universe_d2_052_vrg_basefill_052, 52)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_052_vrg_basefill_052'] = {'inputs': ['vrg_base_universe_d2_052_vrg_basefill_052'], 'func': vrg_base_universe_d3_052_vrg_basefill_052}


def vrg_base_universe_d3_053_vrg_basefill_053(vrg_base_universe_d2_053_vrg_basefill_053):
    return _base_universe_d3(vrg_base_universe_d2_053_vrg_basefill_053, 53)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_053_vrg_basefill_053'] = {'inputs': ['vrg_base_universe_d2_053_vrg_basefill_053'], 'func': vrg_base_universe_d3_053_vrg_basefill_053}


def vrg_base_universe_d3_054_vrg_basefill_054(vrg_base_universe_d2_054_vrg_basefill_054):
    return _base_universe_d3(vrg_base_universe_d2_054_vrg_basefill_054, 54)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_054_vrg_basefill_054'] = {'inputs': ['vrg_base_universe_d2_054_vrg_basefill_054'], 'func': vrg_base_universe_d3_054_vrg_basefill_054}


def vrg_base_universe_d3_055_vrg_basefill_055(vrg_base_universe_d2_055_vrg_basefill_055):
    return _base_universe_d3(vrg_base_universe_d2_055_vrg_basefill_055, 55)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_055_vrg_basefill_055'] = {'inputs': ['vrg_base_universe_d2_055_vrg_basefill_055'], 'func': vrg_base_universe_d3_055_vrg_basefill_055}


def vrg_base_universe_d3_056_vrg_basefill_056(vrg_base_universe_d2_056_vrg_basefill_056):
    return _base_universe_d3(vrg_base_universe_d2_056_vrg_basefill_056, 56)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_056_vrg_basefill_056'] = {'inputs': ['vrg_base_universe_d2_056_vrg_basefill_056'], 'func': vrg_base_universe_d3_056_vrg_basefill_056}


def vrg_base_universe_d3_057_vrg_basefill_057(vrg_base_universe_d2_057_vrg_basefill_057):
    return _base_universe_d3(vrg_base_universe_d2_057_vrg_basefill_057, 57)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_057_vrg_basefill_057'] = {'inputs': ['vrg_base_universe_d2_057_vrg_basefill_057'], 'func': vrg_base_universe_d3_057_vrg_basefill_057}


def vrg_base_universe_d3_058_vrg_basefill_058(vrg_base_universe_d2_058_vrg_basefill_058):
    return _base_universe_d3(vrg_base_universe_d2_058_vrg_basefill_058, 58)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_058_vrg_basefill_058'] = {'inputs': ['vrg_base_universe_d2_058_vrg_basefill_058'], 'func': vrg_base_universe_d3_058_vrg_basefill_058}


def vrg_base_universe_d3_059_vrg_basefill_059(vrg_base_universe_d2_059_vrg_basefill_059):
    return _base_universe_d3(vrg_base_universe_d2_059_vrg_basefill_059, 59)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_059_vrg_basefill_059'] = {'inputs': ['vrg_base_universe_d2_059_vrg_basefill_059'], 'func': vrg_base_universe_d3_059_vrg_basefill_059}


def vrg_base_universe_d3_060_vrg_basefill_060(vrg_base_universe_d2_060_vrg_basefill_060):
    return _base_universe_d3(vrg_base_universe_d2_060_vrg_basefill_060, 60)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_060_vrg_basefill_060'] = {'inputs': ['vrg_base_universe_d2_060_vrg_basefill_060'], 'func': vrg_base_universe_d3_060_vrg_basefill_060}


def vrg_base_universe_d3_061_vrg_basefill_061(vrg_base_universe_d2_061_vrg_basefill_061):
    return _base_universe_d3(vrg_base_universe_d2_061_vrg_basefill_061, 61)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_061_vrg_basefill_061'] = {'inputs': ['vrg_base_universe_d2_061_vrg_basefill_061'], 'func': vrg_base_universe_d3_061_vrg_basefill_061}


def vrg_base_universe_d3_062_vrg_basefill_062(vrg_base_universe_d2_062_vrg_basefill_062):
    return _base_universe_d3(vrg_base_universe_d2_062_vrg_basefill_062, 62)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_062_vrg_basefill_062'] = {'inputs': ['vrg_base_universe_d2_062_vrg_basefill_062'], 'func': vrg_base_universe_d3_062_vrg_basefill_062}


def vrg_base_universe_d3_063_vrg_basefill_063(vrg_base_universe_d2_063_vrg_basefill_063):
    return _base_universe_d3(vrg_base_universe_d2_063_vrg_basefill_063, 63)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_063_vrg_basefill_063'] = {'inputs': ['vrg_base_universe_d2_063_vrg_basefill_063'], 'func': vrg_base_universe_d3_063_vrg_basefill_063}


def vrg_base_universe_d3_064_vrg_basefill_064(vrg_base_universe_d2_064_vrg_basefill_064):
    return _base_universe_d3(vrg_base_universe_d2_064_vrg_basefill_064, 64)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_064_vrg_basefill_064'] = {'inputs': ['vrg_base_universe_d2_064_vrg_basefill_064'], 'func': vrg_base_universe_d3_064_vrg_basefill_064}


def vrg_base_universe_d3_065_vrg_basefill_065(vrg_base_universe_d2_065_vrg_basefill_065):
    return _base_universe_d3(vrg_base_universe_d2_065_vrg_basefill_065, 65)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_065_vrg_basefill_065'] = {'inputs': ['vrg_base_universe_d2_065_vrg_basefill_065'], 'func': vrg_base_universe_d3_065_vrg_basefill_065}


def vrg_base_universe_d3_066_vrg_basefill_066(vrg_base_universe_d2_066_vrg_basefill_066):
    return _base_universe_d3(vrg_base_universe_d2_066_vrg_basefill_066, 66)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_066_vrg_basefill_066'] = {'inputs': ['vrg_base_universe_d2_066_vrg_basefill_066'], 'func': vrg_base_universe_d3_066_vrg_basefill_066}


def vrg_base_universe_d3_067_vrg_basefill_067(vrg_base_universe_d2_067_vrg_basefill_067):
    return _base_universe_d3(vrg_base_universe_d2_067_vrg_basefill_067, 67)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_067_vrg_basefill_067'] = {'inputs': ['vrg_base_universe_d2_067_vrg_basefill_067'], 'func': vrg_base_universe_d3_067_vrg_basefill_067}


def vrg_base_universe_d3_068_vrg_basefill_068(vrg_base_universe_d2_068_vrg_basefill_068):
    return _base_universe_d3(vrg_base_universe_d2_068_vrg_basefill_068, 68)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_068_vrg_basefill_068'] = {'inputs': ['vrg_base_universe_d2_068_vrg_basefill_068'], 'func': vrg_base_universe_d3_068_vrg_basefill_068}


def vrg_base_universe_d3_069_vrg_basefill_069(vrg_base_universe_d2_069_vrg_basefill_069):
    return _base_universe_d3(vrg_base_universe_d2_069_vrg_basefill_069, 69)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_069_vrg_basefill_069'] = {'inputs': ['vrg_base_universe_d2_069_vrg_basefill_069'], 'func': vrg_base_universe_d3_069_vrg_basefill_069}


def vrg_base_universe_d3_070_vrg_basefill_070(vrg_base_universe_d2_070_vrg_basefill_070):
    return _base_universe_d3(vrg_base_universe_d2_070_vrg_basefill_070, 70)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_070_vrg_basefill_070'] = {'inputs': ['vrg_base_universe_d2_070_vrg_basefill_070'], 'func': vrg_base_universe_d3_070_vrg_basefill_070}


def vrg_base_universe_d3_071_vrg_basefill_071(vrg_base_universe_d2_071_vrg_basefill_071):
    return _base_universe_d3(vrg_base_universe_d2_071_vrg_basefill_071, 71)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_071_vrg_basefill_071'] = {'inputs': ['vrg_base_universe_d2_071_vrg_basefill_071'], 'func': vrg_base_universe_d3_071_vrg_basefill_071}


def vrg_base_universe_d3_072_vrg_basefill_072(vrg_base_universe_d2_072_vrg_basefill_072):
    return _base_universe_d3(vrg_base_universe_d2_072_vrg_basefill_072, 72)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_072_vrg_basefill_072'] = {'inputs': ['vrg_base_universe_d2_072_vrg_basefill_072'], 'func': vrg_base_universe_d3_072_vrg_basefill_072}


def vrg_base_universe_d3_073_vrg_basefill_073(vrg_base_universe_d2_073_vrg_basefill_073):
    return _base_universe_d3(vrg_base_universe_d2_073_vrg_basefill_073, 73)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_073_vrg_basefill_073'] = {'inputs': ['vrg_base_universe_d2_073_vrg_basefill_073'], 'func': vrg_base_universe_d3_073_vrg_basefill_073}


def vrg_base_universe_d3_074_vrg_basefill_074(vrg_base_universe_d2_074_vrg_basefill_074):
    return _base_universe_d3(vrg_base_universe_d2_074_vrg_basefill_074, 74)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_074_vrg_basefill_074'] = {'inputs': ['vrg_base_universe_d2_074_vrg_basefill_074'], 'func': vrg_base_universe_d3_074_vrg_basefill_074}


def vrg_base_universe_d3_075_vrg_basefill_075(vrg_base_universe_d2_075_vrg_basefill_075):
    return _base_universe_d3(vrg_base_universe_d2_075_vrg_basefill_075, 75)
VRG_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vrg_base_universe_d3_075_vrg_basefill_075'] = {'inputs': ['vrg_base_universe_d2_075_vrg_basefill_075'], 'func': vrg_base_universe_d3_075_vrg_basefill_075}
