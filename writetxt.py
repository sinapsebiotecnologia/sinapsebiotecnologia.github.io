import json

import streamlit as st
import pandas
import requests as req
# import pip
# pip.main(["install", "openpyxl"])

def main():


    dict = req.get("https://sinapsebiotecnologia.github.io/teste.json")
    dict = dict.json()

    excel_data_df = pandas.read_excel('teste.xlsx')
    json_str = excel_data_df.to_json()

    print(dict)
    print(json_str)
    # if json_str != "None":
    #     with open("teste.json", "w") as arquivo:
    #         json.dump(json_str,arquivo)

if __name__ == '__main__':
    main()