import pandas as pd
import numpy as np

def _sma(s, w):
    """Simple Moving Average with min_periods handling."""
    return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()

def _std(s, w):
    """Standard Deviation with min_periods handling."""
    return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()

def _z(s, w):
    """Z-score calculation."""
    return (s - _sma(s, w)) / _std(s, w).replace(0, np.nan)

def _ce_div(s1, s2, w): return (s1 - s2).rolling(w).mean()

def f39_cash_earnings_divergence_ni_base_w34_v076_signal(ni) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ni, Variation: 76. This monitors 34-period trends."""
    res = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 34)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_base_w35_v077_signal(ncfo) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 77. This monitors 35-period trends."""
    res = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_base_w36_v078_signal(ni) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ni, Variation: 78. This monitors 36-period trends."""
    res = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 36)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_base_w37_v079_signal(ncfo) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 79. This monitors 37-period trends."""
    res = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 37)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_base_w38_v080_signal(ni) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ni, Variation: 80. This monitors 38-period trends."""
    res = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 38)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_base_w39_v081_signal(ncfo) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 81. This monitors 39-period trends."""
    res = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 39)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_base_w40_v082_signal(ni) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ni, Variation: 82. This monitors 40-period trends."""
    res = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 40)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_base_w41_v083_signal(ncfo) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 83. This monitors 41-period trends."""
    res = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 41)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_base_w42_v084_signal(ni) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ni, Variation: 84. This monitors 42-period trends."""
    res = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_base_w43_v085_signal(ncfo) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 85. This monitors 43-period trends."""
    res = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 43)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_base_w44_v086_signal(ni) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ni, Variation: 86. This monitors 44-period trends."""
    res = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 44)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_base_w45_v087_signal(ncfo) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 87. This monitors 45-period trends."""
    res = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_base_w46_v088_signal(ni) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ni, Variation: 88. This monitors 46-period trends."""
    res = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 46)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_base_w47_v089_signal(ncfo) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 89. This monitors 47-period trends."""
    res = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 47)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_base_w48_v090_signal(ni) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ni, Variation: 90. This monitors 48-period trends."""
    res = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 48)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_base_w49_v091_signal(ncfo) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 91. This monitors 49-period trends."""
    res = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 49)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_base_w50_v092_signal(ni) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ni, Variation: 92. This monitors 50-period trends."""
    res = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 50)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_base_w51_v093_signal(ncfo) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 93. This monitors 51-period trends."""
    res = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 51)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_base_w52_v094_signal(ni) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ni, Variation: 94. This monitors 52-period trends."""
    res = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 52)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_base_w53_v095_signal(ncfo) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 95. This monitors 53-period trends."""
    res = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 53)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_base_w54_v096_signal(ni) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ni, Variation: 96. This monitors 54-period trends."""
    res = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 54)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_base_w55_v097_signal(ncfo) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 97. This monitors 55-period trends."""
    res = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_base_w56_v098_signal(ni) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ni, Variation: 98. This monitors 56-period trends."""
    res = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 56)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_base_w57_v099_signal(ncfo) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 99. This monitors 57-period trends."""
    res = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 57)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_base_w58_v100_signal(ni) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ni, Variation: 100. This monitors 58-period trends."""
    res = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 58)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_base_w59_v101_signal(ncfo) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 101. This monitors 59-period trends."""
    res = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 59)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_base_w60_v102_signal(ni) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ni, Variation: 102. This monitors 60-period trends."""
    res = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 60)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_base_w61_v103_signal(ncfo) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 103. This monitors 61-period trends."""
    res = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 61)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_base_w62_v104_signal(ni) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ni, Variation: 104. This monitors 62-period trends."""
    res = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 62)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_base_w63_v105_signal(ncfo) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 105. This monitors 63-period trends."""
    res = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_base_w64_v106_signal(ni) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ni, Variation: 106. This monitors 64-period trends."""
    res = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 64)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_base_w65_v107_signal(ncfo) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 107. This monitors 65-period trends."""
    res = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_base_w66_v108_signal(ni) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ni, Variation: 108. This monitors 66-period trends."""
    res = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 66)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_base_w67_v109_signal(ncfo) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 109. This monitors 67-period trends."""
    res = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 67)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_base_w68_v110_signal(ni) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ni, Variation: 110. This monitors 68-period trends."""
    res = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 68)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_base_w69_v111_signal(ncfo) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 111. This monitors 69-period trends."""
    res = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 69)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_base_w70_v112_signal(ni) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ni, Variation: 112. This monitors 70-period trends."""
    res = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 70)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_base_w71_v113_signal(ncfo) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 113. This monitors 71-period trends."""
    res = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 71)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_base_w72_v114_signal(ni) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ni, Variation: 114. This monitors 72-period trends."""
    res = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 72)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_base_w73_v115_signal(ncfo) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 115. This monitors 73-period trends."""
    res = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 73)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_base_w74_v116_signal(ni) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ni, Variation: 116. This monitors 74-period trends."""
    res = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 74)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_base_w75_v117_signal(ncfo) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 117. This monitors 75-period trends."""
    res = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_base_w76_v118_signal(ni) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ni, Variation: 118. This monitors 76-period trends."""
    res = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 76)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_base_w77_v119_signal(ncfo) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 119. This monitors 77-period trends."""
    res = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 77)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_base_w78_v120_signal(ni) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ni, Variation: 120. This monitors 78-period trends."""
    res = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 78)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_base_w79_v121_signal(ncfo) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 121. This monitors 79-period trends."""
    res = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 79)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_base_w80_v122_signal(ni) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ni, Variation: 122. This monitors 80-period trends."""
    res = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 80)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_base_w81_v123_signal(ncfo) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 123. This monitors 81-period trends."""
    res = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 81)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_base_w82_v124_signal(ni) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ni, Variation: 124. This monitors 82-period trends."""
    res = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 82)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_base_w83_v125_signal(ncfo) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 125. This monitors 83-period trends."""
    res = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 83)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_base_w21_v126_signal(ni) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ni, Variation: 126. This monitors 21-period trends."""
    res = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_base_w22_v127_signal(ncfo) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 127. This monitors 22-period trends."""
    res = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_base_w23_v128_signal(ni) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ni, Variation: 128. This monitors 23-period trends."""
    res = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 23)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_base_w24_v129_signal(ncfo) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 129. This monitors 24-period trends."""
    res = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 24)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_base_w25_v130_signal(ni) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ni, Variation: 130. This monitors 25-period trends."""
    res = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_base_w26_v131_signal(ncfo) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 131. This monitors 26-period trends."""
    res = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 26)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_base_w27_v132_signal(ni) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ni, Variation: 132. This monitors 27-period trends."""
    res = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 27)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_base_w28_v133_signal(ncfo) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 133. This monitors 28-period trends."""
    res = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 28)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_base_w29_v134_signal(ni) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ni, Variation: 134. This monitors 29-period trends."""
    res = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 29)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_base_w30_v135_signal(ncfo) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 135. This monitors 30-period trends."""
    res = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 30)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_base_w31_v136_signal(ni) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ni, Variation: 136. This monitors 31-period trends."""
    res = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 31)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_base_w32_v137_signal(ncfo) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 137. This monitors 32-period trends."""
    res = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 32)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_base_w33_v138_signal(ni) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ni, Variation: 138. This monitors 33-period trends."""
    res = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 33)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_base_w34_v139_signal(ncfo) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 139. This monitors 34-period trends."""
    res = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 34)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_base_w35_v140_signal(ni) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ni, Variation: 140. This monitors 35-period trends."""
    res = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_base_w36_v141_signal(ncfo) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 141. This monitors 36-period trends."""
    res = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 36)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_base_w37_v142_signal(ni) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ni, Variation: 142. This monitors 37-period trends."""
    res = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 37)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_base_w38_v143_signal(ncfo) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 143. This monitors 38-period trends."""
    res = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 38)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_base_w39_v144_signal(ni) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ni, Variation: 144. This monitors 39-period trends."""
    res = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 39)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_base_w40_v145_signal(ncfo) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 145. This monitors 40-period trends."""
    res = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 40)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_base_w41_v146_signal(ni) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ni, Variation: 146. This monitors 41-period trends."""
    res = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 41)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_base_w42_v147_signal(ncfo) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 147. This monitors 42-period trends."""
    res = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_base_w43_v148_signal(ni) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ni, Variation: 148. This monitors 43-period trends."""
    res = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 43)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ncfo_base_w44_v149_signal(ncfo) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ncfo, Variation: 149. This monitors 44-period trends."""
    res = _ce_div(ncfo, ni if 'ncfo' == 'ncfo' else ncfo, 44)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_cash_earnings_divergence_ni_base_w45_v150_signal(ni) -> pd.Series:
    """Base feature for f39_cash_earnings_divergence. Input: ni, Variation: 150. This monitors 45-period trends."""
    res = _ce_div(ni, ni if 'ni' == 'ncfo' else ncfo, 45)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    df = pd.DataFrame({
        "ni": np.random.normal(1000, 100, n).cumsum() + 1000,
        "ncfo": np.random.normal(1000, 100, n).cumsum() + 1000
    })
    
    funcs = [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f39_cash_earnings_divergence_"))]
    
    print(f"Testing {len(funcs)} functions for f39_cash_earnings_divergence...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        y1 = func(*args)
        y2 = func(*args)
        pd.testing.assert_series_equal(y1, y2)
        
        q = y1.iloc[504:].dropna()
        if len(q) == 0:
            continue
        assert q.nunique() > 10, f"{func.__name__} has too few unique values: {q.nunique()}"

    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f39_cash_earnings_divergence_"))]}
F39_CASH_EARNINGS_DIVERGENCE_REGISTRY_BASE_076_150 = REGISTRY
