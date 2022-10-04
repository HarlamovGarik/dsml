import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


def age_group(age: int):
    if age == 18:
        return "18"
    elif 18 < age <= 24:
        return "18-24"
    elif 25 <= age <= 34:
        return "25-34"
    elif 35 <= age <= 44:
        return "35-44"
    elif 45 <= age <= 54:
        return "45-54"
    elif 55 <= age <= 64:
        return "55-64"
    elif age >= 65:
        return "65+"
    return None


fig, axs = plt.subplots(5, 7, sharey='col', sharex='row')
days = ["Вівторок", "Середа", "Четверг", "П'ятниця", "Субота", "Неділя", "Понеділок"]
for i in range(0, 31):
    try:
        data = pd.read_csv("dateset/nyt/nyt" + str(i + 1) + ".csv")
        data_no_null_age = data[data.Age >= 18]
        data_no_null_age.insert(1, "Age_Group", [age_group(age) for age in data_no_null_age.Age.to_list()])
        data = data_no_null_age.groupby(["Age_Group"], as_index=False).count()
        sns.barplot(ax=axs[i // 7, i % 7], x=data.Age_Group, y=data.Signed_In)
    except FileNotFoundError:
        break

for i, ax in enumerate(axs.flat):
    # ax.get_xaxis().set_visible(False)
    ax.set(xlabel=days[i % 7], ylabel='тиждень-' + str(i // 7 + 1))
    ax.label_outer()

plt.show()
