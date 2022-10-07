import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import re
import os


def find_path(value: str):
    return re.search("(?<=_)(.*?)(?=\.)", value).group(0)


def add_build_category(category: str):
    buffer = ""
    building_categories = ["homes", "condos", "apartments", "buildings", "residential", "factories", "garages",
                           "warehouses", "land", "facilities"]
    for type in building_categories:
        if type.upper() in category:
            buffer = type
            break
    return buffer if buffer != "" else "other"


DIR_PATH = "dataset/rollingsales/"
datas = []
if __name__ == "__main__":
    for index, path in enumerate(os.listdir(DIR_PATH)):
        borough_name = find_path(path)
        data = pd.read_excel(str(DIR_PATH + path), skiprows=4)
        data.columns = [column.lower().replace("\n", " ").replace("-", " ").replace(" ", "_") for column in
                        data.columns]
        data.borough = borough_name
        filter_data = data
        datas.append(filter_data)

    datas = pd.concat(datas)
    # print(datas.sale_date)
    # datas.insert(1, "quarter_group", [str(value.quarter) + "-квартал" for value in datas.sale_date.to_list()])
    # datas.insert(2, "type_building", [add_build_category(category) for category in datas.building_class_category.to_list()])
    # group_by_new_building = datas[datas.year_built == 0].groupby(["borough"], as_index=False, group_keys=True).count()
    # group_by_sale_quarter = datas[datas.year_built == 0].groupby(["borough", "quarter_group"], as_index=False).sum()
    # print(group_by_new_building)
    # ax = sns.barplot(data=group_by_new_building,
    #                  x=group_by_new_building.borough,
    #                  y=group_by_new_building.zip_code)
    # ax.set(title="Кількісна характеристика нових будівництв", ylabel="Кількість будівництв")
    #
    # ax = sns.barplot(data=group_by_sale_quarter,
    #                  x=group_by_sale_quarter.borough,
    #                  y=group_by_sale_quarter.sale_price,
    #                  hue=group_by_sale_quarter.quarter_group)
    # ax.set(title="Кількісна характеристика нових будівництв", ylabel="Кількість будівництв")
    # # data_by_sale_price_zero = filter_data[filter_data.sale_price <= 10].borough.count()
    # # data_by_sale_price_larger_than_zero = filter_data[filter_data.sale_price > 10].borough.count()
    # # print("Different: {}% zero - {}, is larger than zero - {}".format(
    # #     data_by_sale_price_zero / data_by_sale_price_larger_than_zero * 100, data_by_sale_price_zero,
    # #     data_by_sale_price_larger_than_zero))
    # # ax = sns.barplot(
    # #     x=[0, 0],
    # #     y=[data_by_sale_price_zero, data_by_sale_price_larger_than_zero],
    # #     hue=["zero", "> zero"])
    # # ax.set(title="Different between {} and {}".format(data_by_sale_price_zero, data_by_sale_price_larger_than_zero),
    # #        ylabel="Number of transactions")
    # # data_building_class = filter_data.groupby(["building_class_at_present"]).count()
    # # print(data_building_class)
    group_by_type_building = datas.groupby(["quarter_group","type_building"], as_index=False).sum()
    sns.barplot(data=group_by_type_building,
                x=group_by_type_building.type_building,
                hue=group_by_type_building.quarter_group)

    group_by_max_sale_quarter = datas[datas.sale_price > 10 ** 8]
    print(group_by_max_sale_quarter)
    plt.show()
