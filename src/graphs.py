# import matplotlib.pyplot as plt
import pandas as pd
# plt.style.use('ggplot')

# plotting the error
# error = pd.read_csv('../data/processed/errors.csv')

# fig = plt.figure(figsize=(4,3))
# plt.plot(error.n_comps,error.error,'b-*',lw=3)
# plt.xlabel('no. of clusters')
# plt.ylabel('$\Delta \; AUC$')
# plt.savefig('visualization/error_curve.png',bbox_inches='tight',dpi=300)
# plt.show()

# plotting the distributions
wb = pd.ExcelFile('../data/processed/distributions.xlsx')
print(wb.sheet_names)
# def plt_distro():
#     pass
