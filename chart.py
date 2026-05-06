import matplotlib.pyplot as plt
import numpy as np

labels = ['prompt 1', 'prompt 2', 'prompt 3']
x = np.arange(len(labels))
width = 0.2

watermarked       = [0.54067034, 0.5438647,  0.5255109]
unwatermarked     = [0.5014837,  0.49444446, 0.5007122]
w_watermarked     = [0.55214715, 0.55291194, 0.5339827]
w_unwatermarked   = [0.5001665,  0.49458373, 0.498771]

fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(x - 1.5*width, watermarked,     width, label='Watermarked',            color='#185FA5')
ax.bar(x - 0.5*width, unwatermarked,   width, label='Unwatermarked',          color='#0F6E56')
ax.bar(x + 0.5*width, w_watermarked,   width, label='Weighted Watermarked',   color='#378ADD')
ax.bar(x + 1.5*width, w_unwatermarked, width, label='Weighted Unwatermarked', color='#1D9E75')

ax.set_ylim(0.48, 0.57)
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Score')
ax.set_title('Mean Scores: Watermarked vs Unwatermarked Responses')
ax.legend()
ax.yaxis.grid(True, linestyle='--', alpha=0.5)
ax.set_axisbelow(True)

plt.tight_layout()
plt.savefig('watermark_scores.png', dpi=150)
plt.show()