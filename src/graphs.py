import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('ggplot')

# plotting the error
# error = pd.read_csv('../data/processed/errors.csv')

# fig = plt.figure(figsize=(4, 3))
# plt.plot(error.n_comps, error.error, 'b-*', lw=3)
# plt.xlabel('no. of clusters', fontsize=14)
# plt.ylabel('$\Delta \; AUC$', fontsize=14)
# plt.savefig('visualization/error_curve.png', bbox_inches='tight', dpi=300)
# plt.show()

# # plotting the distributions
wb = pd.ExcelFile('../data/processed/distributions.xlsx')
ncomps = ['nComps3', 'nComps4']

# comparing the predictions based on number of clusters


# def plt_distros(wb, ncomps):

#     fig, axs = plt.subplots(1, 2, figsize=(10, 5))
#     n = 3
#     for sheet in range(len(ncomps)):
#         df = wb.parse(ncomps[sheet])
#         axs[sheet].plot(df.iloc[:, 0], df.iloc[:, 1], 'k:', lw=2)
#         for curve in range(2, len(df.columns)):
#             axs[sheet].plot(df.iloc[:, 0], df.iloc[:, curve],
#                             ls='-.', lw=3, label=f'cluster {curve-1}')
#         axs[sheet].set_title(f'no. of clusters = {n}')
#         axs[sheet].legend()
#         n += 1
#     fig.supxlabel('$Log \; M$', fontsize=14)
#     fig.supylabel('$dw/dLogM$', fontsize=14)
#     plt.savefig('visualization/comparison_nclusters.png',
#                 bbox_inches='tight', dpi=300)
#     plt.show()
#     return None


# plt_distros(wb, ncomps)


df_3comp = wb.parse(sheet_name='nComps3')
cols = df_3comp.columns[df_3comp.columns.str.contains('cur')]
df_curves = df_3comp[cols]
df_3comp['overall'] = df_curves.sum(axis=1)

fig = plt.figure(figsize=(5, 4))
ax = plt.subplot(111)
ax.plot(df_3comp.iloc[:, 0], df_3comp.iloc[:, 1],
        'k', lw=2, label='original distribution')
ax.plot(df_3comp.iloc[:, 0], df_3comp.overall,
        'r-.', lw=2, label='sum of clusters')
lmw = df_curves[['curve1', 'curve2']].sum(axis=1)
hmw = df_curves['curve3']

ax.plot(df_3comp.iloc[:, 0], lmw, 'b', lw=3, label='low weights', alpha=0.7)
ax.plot(df_3comp.iloc[:, 0], hmw, 'g', lw=3, label='high weights', alpha=0.7)
plt.legend(loc='best')
ax.set_xlabel('$Log \; M$', fontsize=14)
ax.set_ylabel('$dw/dLogM$', fontsize=14)
plt.title('Deconvolution of molecular weight distribution')
plt.savefig('visualization/deconvoluted.png',
            bbox_inches='tight', dpi=300)
plt.show()
