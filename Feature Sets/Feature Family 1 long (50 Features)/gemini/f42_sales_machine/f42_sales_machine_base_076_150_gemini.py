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

def _sm_efficiency(rev, sga, w): return rev.pct_change(w) / sga.pct_change(w).replace(0, np.nan)

def f42_sales_machine_sga_base_w34_v076_signal(sga) -> pd.Series:
    """Base feature for f42_sales_machine. Input: sga, Variation: 76. This monitors 34-period trends."""
    res = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 34)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_base_w35_v077_signal(revenue) -> pd.Series:
    """Base feature for f42_sales_machine. Input: revenue, Variation: 77. This monitors 35-period trends."""
    res = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_base_w36_v078_signal(sga) -> pd.Series:
    """Base feature for f42_sales_machine. Input: sga, Variation: 78. This monitors 36-period trends."""
    res = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 36)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_base_w37_v079_signal(revenue) -> pd.Series:
    """Base feature for f42_sales_machine. Input: revenue, Variation: 79. This monitors 37-period trends."""
    res = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 37)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_base_w38_v080_signal(sga) -> pd.Series:
    """Base feature for f42_sales_machine. Input: sga, Variation: 80. This monitors 38-period trends."""
    res = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 38)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_base_w39_v081_signal(revenue) -> pd.Series:
    """Base feature for f42_sales_machine. Input: revenue, Variation: 81. This monitors 39-period trends."""
    res = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 39)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_base_w40_v082_signal(sga) -> pd.Series:
    """Base feature for f42_sales_machine. Input: sga, Variation: 82. This monitors 40-period trends."""
    res = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 40)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_base_w41_v083_signal(revenue) -> pd.Series:
    """Base feature for f42_sales_machine. Input: revenue, Variation: 83. This monitors 41-period trends."""
    res = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 41)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_base_w42_v084_signal(sga) -> pd.Series:
    """Base feature for f42_sales_machine. Input: sga, Variation: 84. This monitors 42-period trends."""
    res = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_base_w43_v085_signal(revenue) -> pd.Series:
    """Base feature for f42_sales_machine. Input: revenue, Variation: 85. This monitors 43-period trends."""
    res = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 43)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_base_w44_v086_signal(sga) -> pd.Series:
    """Base feature for f42_sales_machine. Input: sga, Variation: 86. This monitors 44-period trends."""
    res = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 44)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_base_w45_v087_signal(revenue) -> pd.Series:
    """Base feature for f42_sales_machine. Input: revenue, Variation: 87. This monitors 45-period trends."""
    res = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_base_w46_v088_signal(sga) -> pd.Series:
    """Base feature for f42_sales_machine. Input: sga, Variation: 88. This monitors 46-period trends."""
    res = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 46)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_base_w47_v089_signal(revenue) -> pd.Series:
    """Base feature for f42_sales_machine. Input: revenue, Variation: 89. This monitors 47-period trends."""
    res = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 47)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_base_w48_v090_signal(sga) -> pd.Series:
    """Base feature for f42_sales_machine. Input: sga, Variation: 90. This monitors 48-period trends."""
    res = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 48)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_base_w49_v091_signal(revenue) -> pd.Series:
    """Base feature for f42_sales_machine. Input: revenue, Variation: 91. This monitors 49-period trends."""
    res = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 49)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_base_w50_v092_signal(sga) -> pd.Series:
    """Base feature for f42_sales_machine. Input: sga, Variation: 92. This monitors 50-period trends."""
    res = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 50)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_base_w51_v093_signal(revenue) -> pd.Series:
    """Base feature for f42_sales_machine. Input: revenue, Variation: 93. This monitors 51-period trends."""
    res = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 51)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_base_w52_v094_signal(sga) -> pd.Series:
    """Base feature for f42_sales_machine. Input: sga, Variation: 94. This monitors 52-period trends."""
    res = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 52)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_base_w53_v095_signal(revenue) -> pd.Series:
    """Base feature for f42_sales_machine. Input: revenue, Variation: 95. This monitors 53-period trends."""
    res = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 53)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_base_w54_v096_signal(sga) -> pd.Series:
    """Base feature for f42_sales_machine. Input: sga, Variation: 96. This monitors 54-period trends."""
    res = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 54)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_base_w55_v097_signal(revenue) -> pd.Series:
    """Base feature for f42_sales_machine. Input: revenue, Variation: 97. This monitors 55-period trends."""
    res = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_base_w56_v098_signal(sga) -> pd.Series:
    """Base feature for f42_sales_machine. Input: sga, Variation: 98. This monitors 56-period trends."""
    res = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 56)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_base_w57_v099_signal(revenue) -> pd.Series:
    """Base feature for f42_sales_machine. Input: revenue, Variation: 99. This monitors 57-period trends."""
    res = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 57)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_base_w58_v100_signal(sga) -> pd.Series:
    """Base feature for f42_sales_machine. Input: sga, Variation: 100. This monitors 58-period trends."""
    res = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 58)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_base_w59_v101_signal(revenue) -> pd.Series:
    """Base feature for f42_sales_machine. Input: revenue, Variation: 101. This monitors 59-period trends."""
    res = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 59)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_base_w60_v102_signal(sga) -> pd.Series:
    """Base feature for f42_sales_machine. Input: sga, Variation: 102. This monitors 60-period trends."""
    res = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 60)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_base_w61_v103_signal(revenue) -> pd.Series:
    """Base feature for f42_sales_machine. Input: revenue, Variation: 103. This monitors 61-period trends."""
    res = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 61)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_base_w62_v104_signal(sga) -> pd.Series:
    """Base feature for f42_sales_machine. Input: sga, Variation: 104. This monitors 62-period trends."""
    res = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 62)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_base_w63_v105_signal(revenue) -> pd.Series:
    """Base feature for f42_sales_machine. Input: revenue, Variation: 105. This monitors 63-period trends."""
    res = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_base_w64_v106_signal(sga) -> pd.Series:
    """Base feature for f42_sales_machine. Input: sga, Variation: 106. This monitors 64-period trends."""
    res = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 64)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_base_w65_v107_signal(revenue) -> pd.Series:
    """Base feature for f42_sales_machine. Input: revenue, Variation: 107. This monitors 65-period trends."""
    res = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_base_w66_v108_signal(sga) -> pd.Series:
    """Base feature for f42_sales_machine. Input: sga, Variation: 108. This monitors 66-period trends."""
    res = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 66)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_base_w67_v109_signal(revenue) -> pd.Series:
    """Base feature for f42_sales_machine. Input: revenue, Variation: 109. This monitors 67-period trends."""
    res = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 67)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_base_w68_v110_signal(sga) -> pd.Series:
    """Base feature for f42_sales_machine. Input: sga, Variation: 110. This monitors 68-period trends."""
    res = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 68)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_base_w69_v111_signal(revenue) -> pd.Series:
    """Base feature for f42_sales_machine. Input: revenue, Variation: 111. This monitors 69-period trends."""
    res = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 69)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_base_w70_v112_signal(sga) -> pd.Series:
    """Base feature for f42_sales_machine. Input: sga, Variation: 112. This monitors 70-period trends."""
    res = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 70)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_base_w71_v113_signal(revenue) -> pd.Series:
    """Base feature for f42_sales_machine. Input: revenue, Variation: 113. This monitors 71-period trends."""
    res = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 71)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_base_w72_v114_signal(sga) -> pd.Series:
    """Base feature for f42_sales_machine. Input: sga, Variation: 114. This monitors 72-period trends."""
    res = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 72)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_base_w73_v115_signal(revenue) -> pd.Series:
    """Base feature for f42_sales_machine. Input: revenue, Variation: 115. This monitors 73-period trends."""
    res = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 73)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_base_w74_v116_signal(sga) -> pd.Series:
    """Base feature for f42_sales_machine. Input: sga, Variation: 116. This monitors 74-period trends."""
    res = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 74)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_base_w75_v117_signal(revenue) -> pd.Series:
    """Base feature for f42_sales_machine. Input: revenue, Variation: 117. This monitors 75-period trends."""
    res = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_base_w76_v118_signal(sga) -> pd.Series:
    """Base feature for f42_sales_machine. Input: sga, Variation: 118. This monitors 76-period trends."""
    res = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 76)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_base_w77_v119_signal(revenue) -> pd.Series:
    """Base feature for f42_sales_machine. Input: revenue, Variation: 119. This monitors 77-period trends."""
    res = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 77)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_base_w78_v120_signal(sga) -> pd.Series:
    """Base feature for f42_sales_machine. Input: sga, Variation: 120. This monitors 78-period trends."""
    res = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 78)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_base_w79_v121_signal(revenue) -> pd.Series:
    """Base feature for f42_sales_machine. Input: revenue, Variation: 121. This monitors 79-period trends."""
    res = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 79)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_base_w80_v122_signal(sga) -> pd.Series:
    """Base feature for f42_sales_machine. Input: sga, Variation: 122. This monitors 80-period trends."""
    res = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 80)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_base_w81_v123_signal(revenue) -> pd.Series:
    """Base feature for f42_sales_machine. Input: revenue, Variation: 123. This monitors 81-period trends."""
    res = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 81)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_base_w82_v124_signal(sga) -> pd.Series:
    """Base feature for f42_sales_machine. Input: sga, Variation: 124. This monitors 82-period trends."""
    res = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 82)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_base_w83_v125_signal(revenue) -> pd.Series:
    """Base feature for f42_sales_machine. Input: revenue, Variation: 125. This monitors 83-period trends."""
    res = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 83)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_base_w21_v126_signal(sga) -> pd.Series:
    """Base feature for f42_sales_machine. Input: sga, Variation: 126. This monitors 21-period trends."""
    res = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_base_w22_v127_signal(revenue) -> pd.Series:
    """Base feature for f42_sales_machine. Input: revenue, Variation: 127. This monitors 22-period trends."""
    res = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_base_w23_v128_signal(sga) -> pd.Series:
    """Base feature for f42_sales_machine. Input: sga, Variation: 128. This monitors 23-period trends."""
    res = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 23)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_base_w24_v129_signal(revenue) -> pd.Series:
    """Base feature for f42_sales_machine. Input: revenue, Variation: 129. This monitors 24-period trends."""
    res = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 24)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_base_w25_v130_signal(sga) -> pd.Series:
    """Base feature for f42_sales_machine. Input: sga, Variation: 130. This monitors 25-period trends."""
    res = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_base_w26_v131_signal(revenue) -> pd.Series:
    """Base feature for f42_sales_machine. Input: revenue, Variation: 131. This monitors 26-period trends."""
    res = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 26)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_base_w27_v132_signal(sga) -> pd.Series:
    """Base feature for f42_sales_machine. Input: sga, Variation: 132. This monitors 27-period trends."""
    res = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 27)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_base_w28_v133_signal(revenue) -> pd.Series:
    """Base feature for f42_sales_machine. Input: revenue, Variation: 133. This monitors 28-period trends."""
    res = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 28)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_base_w29_v134_signal(sga) -> pd.Series:
    """Base feature for f42_sales_machine. Input: sga, Variation: 134. This monitors 29-period trends."""
    res = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 29)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_base_w30_v135_signal(revenue) -> pd.Series:
    """Base feature for f42_sales_machine. Input: revenue, Variation: 135. This monitors 30-period trends."""
    res = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 30)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_base_w31_v136_signal(sga) -> pd.Series:
    """Base feature for f42_sales_machine. Input: sga, Variation: 136. This monitors 31-period trends."""
    res = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 31)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_base_w32_v137_signal(revenue) -> pd.Series:
    """Base feature for f42_sales_machine. Input: revenue, Variation: 137. This monitors 32-period trends."""
    res = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 32)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_base_w33_v138_signal(sga) -> pd.Series:
    """Base feature for f42_sales_machine. Input: sga, Variation: 138. This monitors 33-period trends."""
    res = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 33)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_base_w34_v139_signal(revenue) -> pd.Series:
    """Base feature for f42_sales_machine. Input: revenue, Variation: 139. This monitors 34-period trends."""
    res = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 34)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_base_w35_v140_signal(sga) -> pd.Series:
    """Base feature for f42_sales_machine. Input: sga, Variation: 140. This monitors 35-period trends."""
    res = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_base_w36_v141_signal(revenue) -> pd.Series:
    """Base feature for f42_sales_machine. Input: revenue, Variation: 141. This monitors 36-period trends."""
    res = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 36)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_base_w37_v142_signal(sga) -> pd.Series:
    """Base feature for f42_sales_machine. Input: sga, Variation: 142. This monitors 37-period trends."""
    res = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 37)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_base_w38_v143_signal(revenue) -> pd.Series:
    """Base feature for f42_sales_machine. Input: revenue, Variation: 143. This monitors 38-period trends."""
    res = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 38)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_base_w39_v144_signal(sga) -> pd.Series:
    """Base feature for f42_sales_machine. Input: sga, Variation: 144. This monitors 39-period trends."""
    res = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 39)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_base_w40_v145_signal(revenue) -> pd.Series:
    """Base feature for f42_sales_machine. Input: revenue, Variation: 145. This monitors 40-period trends."""
    res = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 40)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_base_w41_v146_signal(sga) -> pd.Series:
    """Base feature for f42_sales_machine. Input: sga, Variation: 146. This monitors 41-period trends."""
    res = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 41)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_base_w42_v147_signal(revenue) -> pd.Series:
    """Base feature for f42_sales_machine. Input: revenue, Variation: 147. This monitors 42-period trends."""
    res = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_base_w43_v148_signal(sga) -> pd.Series:
    """Base feature for f42_sales_machine. Input: sga, Variation: 148. This monitors 43-period trends."""
    res = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 43)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_revenue_base_w44_v149_signal(revenue) -> pd.Series:
    """Base feature for f42_sales_machine. Input: revenue, Variation: 149. This monitors 44-period trends."""
    res = _sm_efficiency(revenue if 'revenue' == 'sga' else sga, revenue, 44)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_sales_machine_sga_base_w45_v150_signal(sga) -> pd.Series:
    """Base feature for f42_sales_machine. Input: sga, Variation: 150. This monitors 45-period trends."""
    res = _sm_efficiency(revenue if 'sga' == 'sga' else sga, sga, 45)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    df = pd.DataFrame({
        "sga": np.random.normal(1000, 100, n).cumsum() + 1000,
        "revenue": np.random.normal(1000, 100, n).cumsum() + 1000
    })
    
    funcs = [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f42_sales_machine_"))]
    
    print(f"Testing {len(funcs)} functions for f42_sales_machine...")
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

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f42_sales_machine_"))]}
F42_SALES_MACHINE_REGISTRY_BASE_076_150 = REGISTRY
